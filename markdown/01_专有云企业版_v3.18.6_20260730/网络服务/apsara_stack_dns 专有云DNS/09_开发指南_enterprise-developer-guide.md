---
title: "专有云DNS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 222
source_pdf: "09_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apsara_stack_dns/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 专有云DNS 开发指南

专有云DNS

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
专有云DNS
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

专有云DNS

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
专有云DNS 您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
专有云DNS

## 准备工作

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

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 专有云DNS AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

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
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
专有云DNS
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
2. 单击顶部菜单栏**产品**，选择**开发者工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发者工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **开发与工具** > **开发与运维** > **API****网关**。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。
专有云DNS

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
专有云DNS

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
专有云DNS

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

专有云DNS

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
专有云DNS
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

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

专有云DNS `//` 创建`DefaultAcsClient`实例并初始化。

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

专有云DNS

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

`//`必填值，调用来源说明专有云DNS `//` 必填值，调用来源说明

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

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。
专有云DNS

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 专有云DNS

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 专有云DNS

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 专有云DNS

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

专有云DNS

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

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

专有云DNS
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

专有云DNS

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

) 专有云DNS

## API参考

### 简介

#### 使用方式

通过用户AK/SK进行调用，具体调用方式可以使用各语言的SDK，也可以自己依据POP网关提供的签名说明，自己编写Clitent进行调用。

#### 支持形式

主账号AK/SK 主账号临时AK/SK Ram子账号AK/SK Ram子账号临时AK/SK

#### 说明

AK是AccessKeyId，识别用户用的。 SK是AccessKeySerect，计算请求签名时用的密钥。

#### 时间格式

除非API有特殊说明，时间字符串为UTC+0时间，格式为YYYY-MM-DDTHH:mm:ssZ，例如：2018-01- 16T09:00:01Z，对应UT+8时间为2018-01-16 17:00:01。

### API概述

当前版本共输出六个API接口，列表如下：

| API | 描述 |
|---|---|
| ObtainGlobalAuthZoneList | 获取全局权威Zone列表 |
| ObtainGlobalAuthRecordList | 获取权威记录列表 |
| AddGlobalRrSet | 添加全局RrSet |
| DeleteGlobalRrSet | 删除全局RrSet |
| UpdateGlobalRrSet | 更新全局RrSet |
| RemarkGlobalRrSet | 备注全局RrSet |

### SDK使用要求

#### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。 专有云DNS

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

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
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
专有云DNS
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

#### 获取EndPoint

**操作步骤**

1. 管理员登录天基控制台。
2. 在上方的导航栏中选择**运维** > **集群运维**，进入**集群运维**页面。
3. 在**Project**下拉菜单中选择dnsProduct。
4. 单击dnsService后面的**详情**。
5. 在下列出的两台服务器中选择一台，单击**终端**进入控制台。
专有云DNS
6. 运行指令 `sudo docker ps -l` ，获取当前运行的container id。
7. 运行指令 sudo docker inspect ${container id} |grep env ，获取当前环境的endpoint值。
其中，pop_out_endpoint对应的value值（api.开头的字符串）即为endpoint。

### SDK示例

#### 创建Client

通过regionId, accessKey, accessKeySecret创建Client：

**GO SDK**

```
1.    if client, err := genesisdns.NewClientWithAccessKey(RegionId, AccessKey,
AccessSecret); err == nil {
```

2. 常的业务逻辑

```
3.    } else {
```

4. 常的业务逻辑

```
5.    }
```

**Python SDK**

```
1.    from aliyunsdkcore.client import AcsClient
2.    from aliyunsdkcore.acs_exception.exceptions import ClientException
3.    from aliyunsdkcore.acs_exception.exceptions import ServerException
```

`4.` `5.`

```
6.    client = AcsClient("<access-key-id>",
7.       "<access-key-secret>",
8.       "<region-id>");
```

**JAVA SDK**

```
1.    public static void main(String[] args) {
2.         DefaultProfile profile = DefaultProfile.getProfile("{regionid}","{ak}", "{se
cret}");
3.         IAcsClient client = new DefaultAcsClient(profile);
4.    }
```

#### 云内API参考

##### 备节点切换主节点：TransferLeadership

调用TransferLeadership接口将备节点切换成主节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 343778269185 | 节点ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Id | String | 343778269185 | 切换成主节点的节点ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=TransferLeadership &Id=343778269185
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>343778269185</Id> <Code>error code </Code>
```

专有云DNS

##### 查询DnsGtmAgent探测节点：

**DescribeDnsGtmAgents**

调用DescribeDnsGtmAgents接口查询地址池健康检查的探测节点列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 1 | 探测节点的ID。 |
| -Ip | String | 127.0.0.1 | 探测节点的IP。 |
| -Dimension | String | ["region","vpcId","z one"], | 探测范围。取值： region：region信息。 vpcId：VPC信息。 zone：区信息。 |
| - DimensionValu e | String | ["chengdu","az1","" ] | 探测范围的值。 |
| - AssignedTaskC ount | Integer | 0 | 默认水位（0 - 1000）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAgents
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "DimensionValue":"[\"chengdu\",\"az1\",\"\"]",
  "Ip":"127.0.0.1",
  "AssignedTaskCount":0,
  "Id":"1",
  "Dimension":"[\"region\",\"vpcId\",\"zone\"],"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <DimensionValue>[&quot;chengdu&quot;,&quot;az1&quot;,&quot;&quot;]</DimensionValue>
 <Ip>127.0.0.1</Ip>
 <AssignedTaskCount>0</AssignedTaskCount>
 <Id>1</Id>
 <Dimension>[&quot;region&quot;,&quot;vpcId&quot;,&quot;zone&quot;],</Dimension>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

专有云DNS

##### 删除PrivateDefaultForward租户默认转发域名：

**DeletePrivateDefaultForwardZone**

调用DeletePrivateDefaultForwardZone接口删除租户默认转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 租户默认转发域名ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户默认转发域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateDefaultForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改PrivateZone租户内网域名的解析记录：

**UpdatePrivateZoneRecord**

调用UpdatePrivateZoneRecord接口修改租户内网域名的解析记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录的ID。 |
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户内网域名的ID。 |
| Name | Strin g | Body | 否 | www | 解析记录的名称。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |
| Ttl | Integ er | Body | 是 | 300 | 记录缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| RDatas | Repe atList | Body | 是 |  | 记录值集合。 |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |
| LineIds | Strin g | Body | 是 | ["default"] | 解析线路列表。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRecord
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code</Code>
```

##### 添加GlobalLine全局线路：AddGlobalLine

调用AddGlobalLine接口添加全局线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddGlobalLine &Name=name &Priority=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改GlobalZone全局内网域名的解析记录：

**UpdateGlobalZoneRecord**

调用UpdateGlobalZoneRecord接口修改全局内网域名的解析记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录的ID。 |
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 全局内网域名的ID。 |
| Name | Strin g | Body | 否 | www | 解析记录的名称。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |
| Ttl | Integ er | Body | 是 | 300 | 记录缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| RDatas | Repe atList | Body | 是 |  | 记录值集合。 |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |
| LineIds | Strin g | Body | 是 | ["default"] | 线路列表。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRecord
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 查询PrivateForwardZone租户转发配置列表：

**DescribePrivateForwardZones**

调用DescribePrivateForwardZones接口查询租户转发配置列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 专有云DNS

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | com. | 查询域名名称（按照包含匹配）。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | region信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.1.1"] | 转发目的IP列表。 |
| - RegionAndVpc s | Array |  | 已经绑定的VPC信息和Region信息。 |
| --Vpcs | Array |  | 已经绑定的VPC信息。 |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | VPC的ID。 |
| ---Name | String | vpc-name | VPC的名称。 |
| --RegionId | String | cn-region-env1- d01 | VPC的region信息。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 转发域名ID。 |
| -Name | String | com. | 转发域名名称。 |
| -CallerUid | String | 126760529569940 0 | 系统参数。 |
| -VpcCount | Integer | 1 | 已关联VPC个数。 |
| -Remark | String | remark | 备注。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -ForwardMode | String | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY: 全部转发模式(建议)-全部 _ 请求只做转发(不作任何递归)。 FORWARD FIRST:优先转发模式-转发失败降 _ 级到互联网递归。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePrivateForwardZones
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.1.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":""
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.1.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400
 </CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name</Name>
  </--Vpcs>
  <RegionId  />
 </-RegionAndVpcs>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 删除RecursorAcl递归ACL配置：

**DeleteRecursorAcl**

调用DeleteRecursorAcl接口删除递归ACL配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 递归ACL配置ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 递归ACL配置ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteRecursorAcl
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 解除租户内网域名绑定的VPC：DeleteZoneVpc

调用DeleteZoneVpc接口，解除租户内网域名绑定的VPC。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | 是 |  | 解绑的VPC列表。 |
| -Id | Strin g |  | 是 | vpc- 9gd80vqxu8zq5j5st90yx | VPC的ID。 |
| -Name | Strin g |  | 否 | vpc-name | VPC的名称。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | VPC的region信息。 |
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户内网域名的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteZoneVpc
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

专有云DNS

##### 查询节点管理列表：DescribeNodes

调用DescribeNodes接口查询节点管理列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -AnycastAddr | String | 10.1.0.12,10.1.0.13 | anycast服务地址。 |
| -Id | String | 343778269185 | 节点ID。 |
| -LocalAddr | String | 10.1.24.1 | 节点IP。 |
| -RegionId | String | cn-region-env1- d01 | regionID。 |
| -Description | String | description | 描述。 |
| -Role | String | leader | 节点角色类型。取值说明： leader：leader节点（选举节点）。 follower ：follower节点（选举节点）。 learner：learner节点（非选举节点）。 candidate：异常状态节点。 |
| -Index | Integer | 1 | 最新同步logid。 |
| -IsOnline | Boolean | true | 工作状态。取值说明： true：正常。 false：离线。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - IsInEmergency | Boolean | false | 是否是应急组状态。取值说明： true：是。 false：不是。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Total | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeNodes
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "Role":"leader",
  "Description":"description",
  "AnycastAddr":"10.1.0.12,10.1.0.13",
  "IsInEmergency":false,
  "Index":1,
  "Id":"343778269185",
  "RegionId":"cn-region-env1-d01",
  "LocalAddr":"10.1.24.1",
  "IsOnline":true
 },
 "Code":"error code"
}
```

专有云DNS `XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <Role>leader</Role>
 <Description>description</Description>
 <AnycastAddr>10.1.0.12,10.1.0.13
 </AnycastAddr>
 <IsInEmergency>false</IsInEmergency>
 <Index>1</Index>
 <Id>343778269185
 </Id>
 <RegionId>cn-region-env1-d01
 </RegionId>
 <LocalAddr>10.1.24.1</LocalAddr>
 <IsOnline>true</IsOnline>
</Data> <Code>error code </Code>
```

##### 添加PrivateDefaultForwardZone租户默认转发

**配置：AddPrivateDefaultForwardZone**

调用AddPrivateDefaultForwardZone接口添加租户默认转发配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY:全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1","1.1.1.2"] | 转发目的IP列表。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | 地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户默认转发配置的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddPrivateDefaultForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

##### 清除缓存：FlushCache

调用FlushCache接口清除缓存。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 清除缓存的域名名称。 |
| IncludeSu bDomain | Boole an | Body | 是 | true | 域名匹配方式。取值说明： true：后缀匹配。 false：精确匹配。 |
| MemberId | Long | Body | 是 | 343778263564 | 节点ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=FlushCache
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Code>error code </Code>
```

##### 查询DnsGtmAddressPool地址池列表：

**DescribeDnsGtmAddressPools**

调用DescribeDnsGtmAddressPools接口查询地址池列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ip | Strin g | Body | 否 | 1.1.1.1 | 地址池包含的IP（支持模糊搜索）。 |
| Id | Strin g | Body | 否 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 地址池的ID。 |
| Name | Strin g | Body | 否 | name | 地址池的名称（支持模糊搜索）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Addrs | Array |  |  |
| --Value | String | 1.1.1.1 | 地址值。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Mode | String | SMART | 模式。取值说明： SMART：智能返回。 ONLINE：永远在线。 OFFLINE：永远离线。 |
| --LbaWeight | Integer | 100 | 权重。非权重类型不用填写。 |
| --Available | Boolean | true | 地址是否可用。取值说明： true：可用。 false：不可用。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 地址池ID。 |
| -Name | String | name | 地址池名称。 |
| -Type | String | A | 地址池类型。取值说明： A：IPV4地址。 AAAA：IPV6地址。 CNAME：域名。 |
| -LbaStrategy | String | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址（非权重）。 _ RATIO：按权重返回地址（权重）。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| MonitoredAddr essCount | Integer | 1 | 健康检查任务统计数。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalItems | Integer | 10 | 总数 。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAddressPools
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "MonitoredAddressCount":1,
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Type":"A",
  "LbaStrategy":"ALL_RR",
  "-Addrs":{
   "LbaWeight":100,
   "Mode":"SMART",
   "Value":"1.1.1.1",
   "Available":true
  },
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<MonitoredAddressCount>1</MonitoredAddressCount> <RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Type>A</Type>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-Addrs>
  <LbaWeight>100</LbaWeight>
  <Mode>SMART</Mode>
  <Value>1.1.1.1</Value>
  <Available>true</Available>
 </-Addrs>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 删除DnsGtmAddressPool地址池：

**DeleteDnsGtmAddressPool**

调用DeleteDnsGtmAddressPool接口删除地址池。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 地址池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 地址池ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmAddressPool
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改PrivateDefaultForwardZone租户默认转发

**配置的备注：**

**UpdatePrivateDefaultForwardZoneRemark**

调用UpdatePrivateDefaultForwardZoneRemark接口修改租户默认转发配置的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 租户默认转发配置ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户默认转发配置ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateDefaultForwardZoneRemark &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 添加GlobalZone解析记录:

**AddGlobalZoneRecord**

调用AddGlobalZoneRecord接口添加全局内网域名的解析配置记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 全局内网域名的ID。 |
| Name | Strin g | Body | 否 | www | 记录名称。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |
| Ttl | Integ er | Body | 是 | 300 | 记录缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| Remark | Strin g | Body | 否 | 备注 | 解析记录备注。 |
| RDatas | Repe atList | Body | 是 |  | 记录值集合。 |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |
| LineIds | Strin g | Body | 是 | ["default"] | 解析线路。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 解析记录的ID。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=AddGlobalZoneRecord? ZoneId=aaa&Name=www&Type=A&Ttl=300&LbaStrategy=RATIO&Remark=remark&LineIds= ["default"]&RDatas.1.Value=1.1.1.1&RDatas.1.LbaWeight=100
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除PrivateForwardZone租户转发域名：

**DeletePrivateForwardZone**

调用DeletePrivateForwardZone接口删除租户转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 租户转发域名的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户转发域名的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

##### 查询GlobalForwardZone全局转发域名列表：

**DescribeGlobalForwardZones**

调用DescribeGlobalForwardZones接口查询全局转发域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | com. | 查询域名名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.1.1"] | 转发目的IP列表。 |
| - RegionAndVpc s | Array |  | 已经绑定的VPC信息和Region信息。 |
| --Vpcs | Array |  | 已经绑定的VPC信息。 |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | VPC的ID。 |
| ---Name | String | vpc-name | VPC的名称。 |
| --RegionId | String | cn-region-env1- d01 | VPC的region信息。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 转发域名ID。 |
| -Name | String | com. | 转发域名名称。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -CallerUid | String | 126760529569940 0 | 系统参数。 |
| -VpcCount | Integer | 1 | 已关联VPC个数。 |
| -Remark | String | remark | 备注。 |
| -ForwardMode | String | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY: 全部转发模式(建议)-全部 _ 请求只做转发(不作任何递归)。 FORWARD FIRST:优先转发模式-转发失败降 _ 级到互联网递归。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalForwardZones
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.1.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.1.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400</CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name</Name>
  </--Vpcs>
  <RegionId>cn-region-env1-d01
  </RegionId>
 </-RegionAndVpcs>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 查询ResolveConf全局递归配置：

**DescribeResolveConf**

调用DescribeResolveConf接口查询全局递归配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Code | String | error code | 异常请求的编码。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Enable | Boolean | true | 递归设置。取值说明： true：允许递归。 false：不允许递归。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeResolveConf
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "UpdateTime":"1702460677",
 "Enable":true,
 "UpdateTimestamp":1702460677,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <UpdateTime>1702460677</UpdateTime> <Enable>true</Enable> <UpdateTimestamp>1702460677</UpdateTimestamp> <Code>error code </Code>
```

##### 查询PrivateLine私有线路列表：

**DescribePrivateLines**

调用DescribePrivateLines接口查询私有线路列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ip | Strin g | Body | 否 | 1.1.1.1 | 查询IP，IPV4支持模糊查询，IPV6只支持精确查询。 |
| Name | Strin g | Body | 否 | name | 线路名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| RegionId | Strin g | Body | 否 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | IPV4地址列表。 |
| -V6Addresses | String | ["2400:3200::7777 "] | IPV6地址列表。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 地址池ID。 |
| -Name | String | name | 线路名称。 |
| -Priority | Integer | 1 | 线路优先级，1优先级最高，数值越大优先级越低。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |

|  | 专有云DNS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePrivateLines
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 修改PrivateLine私有线路：

**UpdatePrivateLine**

调用UpdatePrivateLine接口修改私有线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateLine
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 查询和VPC私有域名冲突的域名：

**DescribeConflictPrivateZones**

调用DescribeConflictPrivateZones接口查询和VPC私有域名冲突的域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 专有云DNS

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | com. | 域名名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |
| -Name | String | com. | 域名名称。 |
| -IsForward | Boolean | true | 是否是转发域名。取值说明： true：是。 false：不是。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| TotalItems | Integer | 10 | 总数。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeConflictPrivateZones
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "IsForward":true,
  "Name":"com."
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <IsForward>true</IsForward>
 <Name>com.
 </Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 删除DnsGtmMonitor地址池健康检查：

**DeleteDnsGtmMonitor**

调用DeleteDnsGtmMonitor接口删除地址池健康检查。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 健康检查ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 健康检查ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmMonitor
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 删除PrivateZone租户内网域名：

**DeletePrivateZone**

调用DeletePrivateZone接口删除租户内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 专有云DNS

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 域名ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户内网域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

##### 查询DnsGtmMonitor地址池健康检查：

**DescribeDnsGtmMonitor**

调用DescribeDnsGtmMonitor接口查询地址池健康检查。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| GtmAddre ssPoolId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 地址池ID。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -AgentIds | String | ["agent- id1","agent-id1"] | 探测节点的ID列表。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 健康检查的ID。 |
| -ProtocolType | String | HTTP | 探测类型。取值说明： ICMP：ICMP类型探测。 TCP：TCP类型探测。 UDP：UDP类型探测。 HTTP：HTTP类型探测。 HTTPS：HTTPS类型探测。 |
| -Enable | String | true | 是否开启。取值说明： true：开启探测。 false: 关闭探测。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - MonitorExtend Info | String | {"code":200,"path" :"index.htm","host" :"aliyun.com"} | 扩展信息，各协议检查所需参数： HTTP(S)： port：检查端口。 host：Host设置。 path：URL路径。 code：返回码大于多少报错。 TCP(UDP)： port：检查端口。 ICMP：无。 |
| -Interval | Integer | 15 | 检查间隔（秒）。 |
| -Timeout | Integer | 3 | 超时时间（秒）。 |
| - EvaluationCou nt | Integer | 5 | 重试次数。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmMonitor
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ProtocolType":"HTTP",
  "Timeout":3,
  "AgentIds":"[\"agent-id1\",\"agent-id1\"]",
  "Enable":"true",
  "EvaluationCount":5,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "MonitorExtendInfo":"{\"code\":200,\"path\":\"index.htm\",\"host\":\"aliyun.com\"}",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Interval":15
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ProtocolType>HTTP</ProtocolType>
 <Timeout>3</Timeout>
 <AgentIds>[&quot;agent-id1&quot;,&quot;agent-id1&quot;]
 </AgentIds>
 <Enable>true</Enable>
 <EvaluationCount>5</EvaluationCount>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <MonitorExtendInfo>
{&quot;code&quot;:200,&quot;path&quot;:&quot;index.htm&quot;,&quot;host&quot;:&quot;aliyu com&quot;}</MonitorExtendInfo>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Interval>15</Interval>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 添加PrivateLine私有线路：AddPrivateLine

调用AddPrivateLine接口添加私有线路。

**请求头**

专有云DNS 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级，1的优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddPrivateLine &Name=name &Priority=1 &RegionId=cn-region-env1-d01
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 查询DnsGtmAccessStrategy访问策略列表：

**DescribeDnsGtmAccessStrategies**

调用DescribeDnsGtmAccessStrategies接口查询访问策略列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| GtmInstan ceId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 调度实例的ID。 |
| Name | Strin g | Body | 否 | name | 访问策略的名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | 线路列表。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 访问策略ID。 |
| -Name | String | name | 访问策略名称。 |
| - GtmInstanceId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 调度实例ID。 |
| - DefaultGtmAd dressPoolType | String | IPV4 | 主地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| - DefaultGtmAd dressPoolId | String | b42155a3-029f- 4d56-bfcb- 0c82657dc7c7 | 主地址池ID。 |
| - DefaultGtmAd dressPoolNam e | String | address-pool- name1 | 主地址池名称。 |
| - DefaultMinAva ilableAddrNum | Integer | 1 | 主地址池最小可用地址数量。 |
| - DefaultAvailab leAddrNum | Integer | 2 | 主地址池当前可用地址数量。 |
| - FailoverGtmAd dressPoolId | String | 90b574f8-6978- 46e4-be85- 159232b981a7 | 备地址池ID。 |
| - FailoverGtmAd dressPoolNam e | String | address-pool- name2 | 备地址池名称。 |
| - FailoverGtmAd dressPoolType | String | IPV4 | 备地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| - FailoverMinAv ailableAddrNu m | Integer | 1 | 备地址池最小可用地址数量。 |
| - FailoverAvaila bleAddrNum | Integer | 2 | 备地址池当前可用地址数量。 |

|  | 开发指南·API参考 |  |  | 专有云DN | S |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - SpecifiedGtmA ddressPool | String | DEFAULT | 手动指定当前使用的地址池。取值说明： DEFAULT：主地址池。 FAILOVER：备地址池。 |
| -SwitchMode | String | BY PROBE RESULT _ _ | 生效地址池切换策略。取值说明： BY HAND：手动。 _ BY PROBE RESULT：自动。 _ _ |
| - InUseGtmAddr essPoolId | String | b42155a3-029f- 4d56-bfcb- 0c82657dc7c7 | 当前使用的地址池ID。 |
| - InUseGtmAddr essPoolName | String | address-pool- name1 | 当前使用的地址池名称。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmAccessStrategies
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "FailoverMinAvailableAddrNum":1,
  "DefaultGtmAddressPoolName":"address-pool-name1",
  "FailoverGtmAddressPoolType":"IPV4",
  "LineIds":"[\"default\"]",
  "DefaultAvailableAddrNum":2,
  "SpecifiedGtmAddressPool":"DEFAULT",
  "DefaultGtmAddressPoolId":"b42155a3-029f-4d56-bfcb-0c82657dc7c7",
  "SwitchMode":"BY_PROBE_RESULT",
  "FailoverAvailableAddrNum":2,
  "Name":"name",
  "DefaultMinAvailableAddrNum":1,
  "FailoverGtmAddressPoolId":"90b574f8-6978-46e4-be85-159232b981a7",
  "DefaultGtmAddressPoolType":"IPV4",
  "FailoverGtmAddressPoolName":"address-pool-name2",
  "InUseGtmAddressPoolName":"address-pool-name1",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "GtmInstanceId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "InUseGtmAddressPoolId":"b42155a3-029f-4d56-bfcb-0c82657dc7c7"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <FailoverMinAvailableAddrNum>1</FailoverMinAvailableAddrNum>
 <DefaultGtmAddressPoolName>address-pool-name1</DefaultGtmAddressPoolName>
 <FailoverGtmAddressPoolType>IPV4</FailoverGtmAddressPoolType>
 <LineIds>[&quot;default&quot;]</LineIds>
 <DefaultAvailableAddrNum>2</DefaultAvailableAddrNum>
 <SpecifiedGtmAddressPool>DEFAULT</SpecifiedGtmAddressPool>
 <DefaultGtmAddressPoolId>b42155a3-029f-4d56-bfcb-0c82657dc7c7
 </DefaultGtmAddressPoolId>
 <SwitchMode>BY_PROBE_RESULT</SwitchMode>
 <FailoverAvailableAddrNum>2</FailoverAvailableAddrNum>
 <Name>name</Name>
 <DefaultMinAvailableAddrNum>1</DefaultMinAvailableAddrNum>
 <FailoverGtmAddressPoolId>90b574f8-6978-46e4-be85-159232b981a7
 </FailoverGtmAddressPoolId>
 <DefaultGtmAddressPoolType>IPV4</DefaultGtmAddressPoolType>
 <FailoverGtmAddressPoolName>address-pool-name2</FailoverGtmAddressPoolName>
 <InUseGtmAddressPoolName>address-pool-name1</InUseGtmAddressPoolName>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <GtmInstanceId>56bab908-04e0-44ee-b126-1cbdbcd24507</GtmInstanceId>
 <InUseGtmAddressPoolId>b42155a3-029f-4d56-bfcb-0c82657dc7c7
 </InUseGtmAddressPoolId>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 修改PrivateForwardZone租户转发域名：

**UpdatePrivateForwardZone**

调用UpdatePrivateForwardZone接口修改租户转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户转发域名的ID。 |
| Name | Strin g | Body | 是 | com. | 租户转发域名的名称。 |

| 专有云DNS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY:全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1","1.1.1.2"] | 转发目的IP列表。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 租户转发域名的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 添加GlobalForwardZone全局转发域名：

**AddGlobalForwardZone**

调用AddGlobalForwardZone接口添加全局转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 转发域名名称。 |
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY:全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1"] | 转发目的IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 转发域名ID。 |

**示例**

专有云DNS 请求示例

```
http(s)://[Endpoint]/?Action=AddGlobalForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 查询和云内全局域名冲突的域名：

**DescribeConflictGlobalZones**

调用DescribeConflictGlobalZones接口查询和云内全局域名冲突的域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | com. | 域名名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |
| -Name | String | com. | 域名名称。 |
| -IsForward | Boolean |  | 是否是转发域名。取值说明： true：是。 false：不是。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| TotalItems | Integer | 10 | 总数。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeConflictGlobalZones
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "IsForward":"",
  "Name":"com."
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <IsForward  />
 <Name>com.</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 修改PrivateZoneRecord租户内网域名解析记录的

**备注：UpdatePrivateZoneRecordRemark**

调用UpdatePrivatejZoneRecordRemark接口修改租户内网域名解析记录的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录备注。 |

**示例**

请求示例专有云DNS

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRecordRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改DnsGtmInstance调度实例：

**UpdateDnsGtmInstance**

调用UpdateDnsGtmInstance接口修改调度实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 调度实例ID。 |
| Name | Strin g | Body | 是 | name | 调度实例名称。 |
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 归属调度域的域名ID。 |
| Ttl | Integ er | Body | 是 | 300 | 缓存时间。 |
| Prefix | Strin g | Body | 是 | www | 调度域名。 |

专有云DNS

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 调度实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmInstance
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code</Code>
```

##### 添加DnsGtmAccessStrategy访问策略：

**AddDnsGtmAccessStrategy**

调用AddDnsGtmAccessStrategy接口添加访问策略。

**请求头**

专有云DNS 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| GtmInstan ceId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 调度实例ID。 |
| Name | Strin g | Body | 是 | name | 策略名称。 |
| LineIds | Strin g | Body | 是 | ["default"] | 线路列表。 |
| DefaultGt mAddress PoolType | Strin g | Body | 是 | IPV4 | 主地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| DefaultGt mAddress PoolId | Strin g | Body | 是 | b42155a3-029f-4d56- bfcb-0c82657dc7c7 | 主地址池ID。 |
| DefaultMi nAvailable AddrNum | Integ er | Body | 是 | 1 | 主地址池最小可用地址数量。 |
| FailoverGt mAddress PoolId | Strin g | Body | 否 | 90b574f8-6978-46e4- be85-159232b981a7 | 备地址池Id。 |
| FailoverGt mAddress PoolType | Strin g | Body | 否 | IPV4 | 备地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| FailoverMi nAvailable AddrNum | Integ er | Body | 否 | 1 | 备地址池最小可用地址数量。 |
| Specified GtmAddre ssPool | Strin g | Body | 否 | DEFAULT | 手动指定当前使用的地址池。取值说明： DEFAULT：主地址池。 FAILOVER：备地址池。 |
| SwitchMo de | Strin g | Body | 是 | BY HAND _ | 生效地址池切换策略。取值说明： BY HAND：手动。 _ BY PROBE RESULT： _ _ 自动。 |

专有云DNS

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddDnsGtmAccessStrategy
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改DnsGtmInstance调度实例备注：

**UpdateDnsGtmInstanceRemark**

调用UpdateDnsGtmInstanceRemark接口修改调度实例备注。

**请求头**

专有云DNS 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 调度实例ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 调度实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmInstanceRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 设置全局默认转发配置：

**SetGlobalDefaultForward**

调用SetGlobalDefaultForward接口设置全局默认转发配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Enable | Boole an | Body | 否 | true | 递归设置。取值说明： true：开启递归。 false:：关闭递归。 |
| ForwardM ode | Strin g | Body | 否 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY: 全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 否 | ["2.2.2.2","3.3.3.3"] | 转发目的IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

专有云DNS 请求示例

```
http(s)://[Endpoint]/?Action=SetGlobalDefaultForward
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Code>error code </Code>
```

##### 查询PrivateDefaultForwardZone租户默认转发

**配置：DescribePrivateDefaultForwardZones**

调用DescribePrivateDefaultForwardZones接口查询租户默认转发配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | region的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Forwarders | String | ["1.1.11.1"] | 转发目的IP列表。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - RegionAndVpc s | Array |  | 已绑定的VPC和Region信息。 |
| --Vpcs | Array |  | 已绑定的VPC信息。 |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | VPC的ID。 |
| ---Name | String | vpc-name | VPC的name。 |
| --RegionId | String | cn-region-env1- d01 | VPC所属的region的ID。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户默认转发配置的ID。 |
| -CallerUid | String | 126760529569940 0 | 系统参数。 |
| -VpcCount | Integer | 1 | 已关联VPC个数。 |
| -Remark | String | remark | 备注。 |
| -ForwardMode | String | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY: 全部转发模式(建议)-全部 _ 请求只做转发(不作任何递归)。 FORWARD FIRST:优先转发模式-转发失败降 _ 级到互联网递归。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePrivateDefaultForwardZones
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "VpcCount":1,
  "ForwardMode":"FORWARD_ONLY",
  "Forwarders":"[\"1.1.11.1\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "CallerUid":"1267605295699400",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <VpcCount>1</VpcCount>
 <ForwardMode>FORWARD_ONLY</ForwardMode>
 <Forwarders>[&quot;1.1.11.1&quot;]</Forwarders>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <CallerUid>1267605295699400</CallerUid>
 <-RegionAndVpcs>
  <--Vpcs>
   <Id>vpc-9gd80vqxu8zq5j5st90yx
   </Id>
   <Name>vpc-name
   </Name>
  </--Vpcs>
  <RegionId>cn-region-env1-d01
  </RegionId>
 </-RegionAndVpcs>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 查询GlobalZone全局内网域名列表：

**DescribeGlobalZones**

调用DescribeGlobalZones接口查询全局内网域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | com. | 查询域名名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Masters | String | ["1.1.1.1:53","2.2.2. 2:53"] | 主域名DNS服务地址。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |
| -Name | String | com. | 域名名称。 |
| -KeyName | String | my-tsig | TSIG密钥名称。（TSIG密钥名称、TSIG密钥算法、TSIG密钥值需要都填写或都不填写。） |
| -KeyAlgorithm | String | HMAC-SHA512 | TSIG密钥算法。（TSIG密钥名称、TSIG密钥算法、TSIG密钥值需要都填写或都不填写。） |
| -KeySecret | String | Ok1qR5IW1ajVka5 cHPEJQIXfLyx5V3P SkFBROAzOn21Jum Dq6nIpoj6H8rfj5Uo +Ok55ZWQ0Wgrf3 02fDscHLw== | TSIG密钥值。（TSIG密钥名称、TSIG密钥算法、TSIG密钥值需要都填写或都不填写。） |
| -RecordCount | Integer | 1 | 解析记录集总数。 |
| - GtmInstanceC ount | Integer | 0 | 创建的调度实例的总数。 |
| -Remark | String | remark | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalZones
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "KeyName":"my-tsig",
  "Masters":"[\"1.1.1.1:53\",\"2.2.2.2:53\"]",
  "GtmInstanceCount":"",
"KeySecret":"Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf 2fDscHLw==",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
  "KeyAlgorithm":"HMAC-SHA512",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <KeyName>my-tsig</KeyName>
 <Masters>[&quot;1.1.1.1:53&quot;,&quot;2.2.2.2:53&quot;]</Masters>
 <GtmInstanceCount  />
<KeySecret>Ok1qR5IW1ajVka5cHPEJQIXfLyx5V3PSkFBROAzOn21JumDq6nIpoj6H8rfj5Uo+Ok55ZWQ0Wgrf30 DscHLw==</KeySecret>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <KeyAlgorithm>HMAC-SHA512</KeyAlgorithm>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 查询GlobalZoneRecord全局内网域名的解析记

**录：DescribeGlobalZoneRecords**

调用DescribeGlobalZoneRecords接口查询全局内网域名的解析记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | name | 查询名称（按照包含匹配）。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | 全局线路ID列表。 |
| -RDatas | Array |  |  |
| --Value | String | 1.1.1.1 | 值。 |
| --LbaWeight | String | 100 | 权重。非权重类型不用填写。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录ID。 |
| -Name | String | www | 解析记录名称。 |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |
| -ZoneName | String | com. | 域名名称。 |
| -Type | String | A | 记录类型。取值说明： A：将域名指向一个IPV4地址。 AAAA：将域名指向一个IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制255，通常做SPF记录 （反垃圾邮件）。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针，通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的DNS服务器解析。 |
| -Ttl | Integer | 300 | 缓存时间（秒）。 |
| -LbaStrategy | String | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址（非权重）。 _ RATIO：按权重返回地址（权重）。 |
| -Remark | String | remark | 备注。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalZoneRecords
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "Type":"A",
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "-RDatas":{
   "LbaWeight":"100",
   "Value":"1.1.1.1"
  },
  "LineIds":"[\"default\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"www",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507
 </ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>www</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 修改GlobalLine全局线路：UpdateGlobalLine

调用UpdateGlobalLine接口修改全局线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalLine
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId /> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 设置Recursor递归：EnableRecursor

专有云DNS 调用EnableRecursor接口设置递归。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Enable | Boole an | Body | 是 | true | 递归设置。取值说明： true：开启递归。 false:：关闭递归。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnableRecursor &Enable=true
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Code>error code </Code>
```

##### 查询GlobalLine全局线路列表：

**DescribeGlobalLines**

专有云DNS 调用DescribeGlobalLines接口查询全局线路列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ip | Strin g | Body | 否 | 1.1.1.1 | 查询IP，IPV4支持模糊查询，IPV6只支持精确查询。 |
| Name | Strin g | Body | 否 | name | 线路名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | IPV4地址列表。 |
| -V6Addresses | String | ["2400:3200::7777 "] | IPV6地址列表。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路的ID。 |
| -Name | String | name | 线路名称。 |
| -Priority | Integer | 1 | 线路优先级，1优先级最高，数值越大优先级越低。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalLines
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 查询节点qps信息：DescribeMetrics

调用DescribeMetrics接口查询qps信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 343778269185 | 节点ID。 |
| -CmdAddr | String | 10.200.2.12:80 | 解析节点IP和端口。 |
| -QPS | String | 1 | qps信息。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Total | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeMetrics
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "QPS":"1",
  "CmdAddr":"10.200.2.12:80",
  "Id":"343778269185"
 },
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <QPS>1</QPS>
 <CmdAddr>10.200.2.12:80</CmdAddr>
 <Id>343778269185</Id>
</Data> <Code>error code </Code>
```

专有云DNS

##### 查询DNS服务的anycast地址：

**DescribeDNSServerAddrs**

调用DescribeDNSServerAddrs接口查询DNS服务的anycast地址列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Addrs | String | ["10.200.0.12", "10.200.0.13"] | anycast服务地址。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDNSServerAddrs
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Addrs":"[\"10.200.0.12\", \"10.200.0.13\"]",
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<Addrs> [&quot;10.200.0.12&quot;, &quot;10.200.0.13&quot;]</Addrs>
 <RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0
 </RequestId>
 <Message>error message
 </Message>
 <Code>error code
 </Code>
```

##### 修改GlobalZone全局内网域名备注：

**UpdateGlobalZoneRemark**

调用UpdateGlobalZoneRemark接口修改全局内网域名备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 域名ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRemark
```

&公共请求参数专有云DNS 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 查询GlobalDefaultForward全局默认转发配置：

**DescribeGlobalDefaultForward**

调用DescribeGlobalDefaultForward接口查询全局默认转发配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Forwarders | String | ["2.2.2.2","3.3.3.3"] | 转发目的IP地址。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Code | String | error code | 异常请求的编码。 |
| UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| Enable | Boolean | true | 默认转发是否开启。取值说明： true：开启。 false：关闭。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ForwardMode | String |  | 转发模式。取值说明： FORWARD ONLY:全部转发模式(建议)-全部 _ 请求只做转发(不作任何递归)。 FORWARD FIRST:优先转发模式-转发失败降 _ 级到互联网递归。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalDefaultForward
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "ForwardMode":"",
 "Forwarders":"[\"2.2.2.2\",\"3.3.3.3\"]",
 "Enable":true,
 "UpdateTimestamp":1702460677,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <ForwardMode /> <Forwarders>[&quot;2.2.2.2&quot;,&quot;3.3.3.3&quot;]</Forwarders> <Enable>true</Enable> <UpdateTimestamp>1702460677</UpdateTimestamp> <Code>error code </Code>
```

##### 添加GlobalZone全局内网域名：

**AddGlobalZone**

调用AddGlobalZone接口添加全局内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 域名名称（必须以"."结尾）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 全局内网域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateDefaultForwardZone &Name=com.
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

##### 修改PrivateZone租户内网域名备注：

**UpdatePrivateZoneRemark**

调用UpdatePrivateZoneRemark接口修改租户内网域名备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 租户内网域名ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 租户内网域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateZoneRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

专有云DNS `XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 添加DnsGtmMonitor地址池健康检查：

**AddDnsGtmMonitor**

调用AddDnsGtmMonitor接口添加地址池健康检查。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ProtocolTy pe | Strin g | Body | 是 | HTTP | 探测类型。取值说明： ICMP：ICMP类型探测。 TCP：TCP类型探测。 UDP：UDP类型探测。 HTTP：HTTP类型探测。 HTTPS：HTTPS类型探测。 |
| GtmAddre ssPoolId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 地址池ID。 |
| Enable | Boole an | Body | 是 | true | 是否开启。取值说明： true：开启探测。 false: 关闭探测。 |
| MonitorEx tendInfo | Json | Body | 否 | {"code":200,"path":"ind ex.htm","host":"aliyun.c om"} | 扩展信息，各协议检查所需参数： HTTP(S)： port：检查端口。 host：Host设置。 path：URL路径。 code：返回码大于多少报错。 TCP(UDP)： port：检查端口。 ICMP：不填写。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Interval | Integ er | Body | 是 | 15 | 检查间隔（秒）。 |
| Timeout | Integ er | Body | 是 | 3 | 超时时间（秒）。 |
| Evaluation Count | Integ er | Body | 是 | 5 | 重试次数。 |
| AgentIds | Strin g | Body | 是 | ["agent-id1","agent-id1"] | 探测节点的ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 地址池ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddDnsGtmMonitor
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改DnsGtmAddressPool地址池：

**UpdateDnsGtmAddressPool**

调用UpdateDnsGtmAddressPool修改地址池。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 地址池ID。 |
| Name | Strin g | Body | 是 | name | 地址池名称。 |
| Type | Strin g | Body | 是 | A | 地址池类型。取值说明： A：IPV4地址。 AAAA：IPV6地址。 CNAME：域名。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| Addr | Repe atList | Body | 是 |  |  |
| -Value | Strin g |  | 是 | 1.1.1.1 | 地址值。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -Mode | Strin g |  | 是 | SMART | 模式。取值说明： SMART：智能返回。 ONLINE：永远在线。 OFFLINE：永远离线。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 地址池的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmAddressPool
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改PrivateLine私有线路优先级：

**UpdatePrivateLinePriority**

调用UpdatePrivateLinePriority接口修改私有线路优先级。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级，1优先级最高，数值越大优先级越低。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateLinePriority
```

&公共请求参数专有云DNS 正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 删除DnsGtmInstance调度实例：

**DeleteDnsGtmInstance**

调用DeleteDnsGtmInstance删除调度实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 调度实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 调度实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmInstance
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改GlobalLine优先级：

**UpdateGlobalLinePriority**

调用UpdateGlobalLinePriority接口修改全局线路优先级。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Priority | Integ er | Body | 是 | 1 | 线路优先级，1的优先级最高，数值越大优先级越低。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalLinePriority
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

##### 创建DnsGtmInstance调度实例：

**AddDnsGtmInstance**

调用AddDnsGtmInstance接口创建调度实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | name | 调度实例名称。 |
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 归属调度域的域名ID。 |
| Ttl | Integ er | Body | 是 | 300 | 缓存时间。 |
| Prefix | Strin g | Body | 是 | www | 调度域名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 调度实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddDnsGtmInstance
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

##### 查询缓存：DescribeCache

调用DescribeCache接口查询缓存。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | com. | 缓存域名名称（按照包含匹配）。 |
| Type | Strin g | Body | 否 | A | 缓存数据类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -RRset | Array |  |  |
| --Rdatas | String | ["10.200.0.4"] | 缓存解析列表。 |
| --Name | String | com. | 缓存域名名称。 |
| --Type | String | A | 缓存记录类型。取值说明： A：将域名指向一个IPV4地址。 AAAA：将域名指向一个IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的DNS服务器解析。 |
| --Ttl | String | 300 | 缓存时间。 |
| -Id | String | 343778269185 | 节点的ID。 |
| -CmdAddr | String | 10.200.2.12:80 | 服务实例IP地址。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCache
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Data":{
  "-RRset":{
   "Type":"A",
   "Rdatas":"[\"10.200.0.4\"]",
   "Ttl":"300",
   "Name":"com."
  },
  "CmdAddr":"10.200.2.12:80",
  "Id":"343778269185"
 },
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Data>
 <-RRset>
  <Type>A</Type>
  <Rdatas>[&quot;10.200.0.4&quot;]</Rdatas>
  <Ttl>300</Ttl>
  <Name>com.</Name>
 </-RRset>
 <CmdAddr>10.200.2.12:80</CmdAddr>
 <Id>343778269185</Id>
</Data> <Code>error code</Code>
```

##### 查询DnsGtmInstance调度实例列表：

**DescribeDnsGtmInstances**

调用DescribeDnsGtmInstances接口查询调度实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | name | 调度实例名称（按照包含匹配）。 |

| DNS |  |  |  |  | ·API |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 调度实例ID。 |
| -Name | String | name | 调度实例名称。 |
| -ZoneId | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 归属调度域的域名ID。 |
| -ZoneName | String | com. | 域名名称。 |
| -Prefix | String | www | 调度域名。 |
| -Ttl | Integer | 300 | 全局TTL。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmInstances
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "ZoneId":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "VpcId":"",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "Prefix":"www",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <ZoneId>e8605e05-4320-4ef5-983d-c5dd48d05b49</ZoneId>
 <VpcId  />
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507
 </Id>
 <Prefix>www</Prefix>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 开启应急组：EnableEmergencyGroup

调用EnableEmergencyGroup接口开启应急组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ids | Strin g | Body | 是 | "1343778269181,34377 8269182,343778269183 " | 需要组建新集群的节点 ID（需要","号分割）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

专有云DNS 请求示例

```
http(s)://[Endpoint]/?Action=EnableEmergencyGroup
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Code>error code </Code>
```

##### 关闭应急组：DisableEmergencyGroup

调用DisableEmergencyGroup接口关闭应急组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisableEmergencyGroup
```

正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### 修改GlobalZone全局内网域名：

**AddGlobalZone**

调用AddGlobalZone接口修改全局内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 域名名称（必须以"."结尾）。 |
| Masters | Strin g | Body | 否 | ["1.1.1.1:53","2.2.2.2:53" ] | 主域名DNS服务地址。 |
| KeyName | Strin g | Body | 否 | my-tsig | TSIG密钥名称。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |
| KeyAlgorit hm | Strin g | Body | 否 | HMAC-SHA512 | TSIG密钥算法。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |
| KeySecret | Strin g | Body | 否 | Ok1qR5IW1ajVka5cHPEJ QIXfLyx5V3PSkFBROAzO n21JumDq6nIpoj6H8rfj5 Uo+Ok55ZWQ0Wgrf302 fDscHLw== | TSIG密钥值。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddGlobalZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"\terror code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code> error code</Code>
```

##### 修改RecursorAcl递归ACL备注：

**UpdateRecursorAclRemark**

调用UpdateRecursorAclRemark接口修改递归ACL备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 递归ACL的ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | ACL策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateRecursorAclRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message </Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

专有云DNS

##### 修改GlobalForward域名：

**UpdateGlobalForwardZone**

调用UpdateGlobalForwardZone接口修改全局转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 转发域名ID。 |
| Name | Strin g | Body | 是 | com. | 转发域名名称（必须以"."结尾）。 |
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY:全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1","1.1.1.2"] | 转发列表。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 转发域名ID。 |

**示例**

专有云DNS 请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 添加PrivateZone租户内网域名：

**AddPrivateZone**

调用AddPrivateZone接口添加租户内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 域名名称（必须以"."结尾）。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddPrivateZone &Name=com. &RegionId=cn-region-env1-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 添加PrivateForward转发域名：

**AddPrivateForwardZone**

调用AddPrivateForwardZone接口添加租户转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 域名名称（必须以"."结尾）。 |
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY: 全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1","1.1.1.2"] | 转发列表。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 转发域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddPrivateForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 修改DnsGtmAccessStrategy访问策略：

**UpdateDnsGtmAccessStrategy**

调用UpdateDnsGtmAccjiessStrategy接口修改访问策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 否 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 访问策略ID。 |
| GtmInstan ceId | Strin g | Body | 否 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 调度实例ID。 |
| Name | Strin g | Body | 否 | name | 策略名称。 |
| LineIds | Strin g | Body | 否 | ["default"] | 线路列表。 |
| DefaultGt mAddress PoolType | Strin g | Body | 否 | IPV4 | 主地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| DefaultGt mAddress PoolId | Strin g | Body | 否 | b42155a3-029f-4d56- bfcb-0c82657dc7c7 | 主地址池ID。 |
| DefaultMi nAvailable AddrNum | Integ er | Body | 否 | 1 | 主地址池最小可用地址数量。 |

| 专有云DNS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FailoverGt mAddress PoolId | Strin g | Body | 否 | 90b574f8-6978-46e4- be85-159232b981a7 | 备地址池ID。 |
| FailoverGt mAddress PoolType | Strin g | Body | 否 | IPV4 | 备地址池类型。取值说明： DOMAIN：域名。 IPV6：IPV6类型。 IPV4：IPV4类型。 |
| FailoverMi nAvailable AddrNum | Integ er | Body | 否 | 1 | 备地址池最小可用地址数量。 |
| Specified GtmAddre ssPool | Strin g | Body | 否 | DEFAULT | 手动指定当前使用的地址池。取值说明： DEFAULT：主地址池。 FAILOVER：备地址池。 |
| SwitchMo de | Strin g | Body | 否 | BY PROBE RESULT _ _ | 生效地址池切换策略。取值说明： BY HAND：手动。 _ BY PROBE RESULT： _ _ 自动。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 访问策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmAccessStrategy
```

&公共请求参数正常返回示例专有云DNS `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id> <Code>error code</Code>
```

##### 修改GlobalForwardZone备注：

**UpdateGlobalForwardZoneRemark**

调用UpdateGlobalForwardZoneRemark接口修改全局转发域名的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 全局转发域名ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 全局转发域名ID。 |

专有云DNS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalForwardZoneRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除PrivateLine私有线路：DeletePrivateLine

调用DeletePrivateLine接口删除私有线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 私有线路ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 私有线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateLine
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 租户内网域名绑定VPC：BindZoneVpc

调用BindZoneVpc接口，租户内网域名绑定VPC。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | 是 |  | 绑定的VPC列表。 |
| -Id | Strin g |  | 是 | vpc- 9gd80vqxu8zq5j5st90yx | VPC的ID。 |
| -Name | Strin g |  | 否 | vpc-name | VPC的名称。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | VPC的region信息。 |

| 专有云DNS |  |  |  |  | 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户内网域名ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=BindZoneVpc
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### 删除DnsGtmAccessStrategy：

**DeleteDnsGtmAccessStrategy**

调用DeleteDnsGtmAccessStrategy接口删除调度实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 调度实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 调度实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteDnsGtmAccessStrategy
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除GlobalForward域名：

**DeleteGlobalForwardZone**

专有云DNS 调用DeleteGlobalForwardZone接口删除全局转发域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteGlobalForwardZone &Id=56bab908-04e0-44ee-b126-1cbdbcd24507
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

专有云DNS

##### 修改GlobalZone：UpdateGlobalZone

调用UpdateGlobalZone接口修改全局内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |
| Name | Strin g | Body | 是 | com. | 域名名称（必须以"."结尾）。 |
| Masters | Strin g | Body | 否 | ["1.1.1.1:53","2.2.2.2:53" ] | 主域名DNS服务地址。 |
| KeyName | Strin g | Body | 否 | my-tsig | TSIG密钥名称。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |
| KeyAlgorit hm | Strin g | Body | 否 | HMAC-SHA512 | TSIG密钥算法。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |
| KeySecret | Strin g | Body | 否 | Ok1qR5IW1ajVka5cHPEJ QIXfLyx5V3PSkFBROAzO n21JumDq6nIpoj6H8rfj5 Uo+Ok55ZWQ0Wgrf302 fDscHLw== | TSIG密钥值。（TSIG密钥名称、TSIG密钥算法、 TSIG密钥值需要都填写或都不填写。） |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |

专有云DNS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalZone &Id=56bab908-04e0-44ee-b126-1cbdbcd24507 &Name=com.
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 修改RecursorAcl：UpdateRecursorAcl

调用UpdateRecursorAcl接口，修改递归ACL策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | ACL策略ID。 |
| Name | Strin g | Body | 是 | 策略名称。 | ACL策略名称。 |
| Policy | Strin g | Body | 是 | true | 允许递归。取值说明： true：允许递归。 false：不允许递归。 |
| LineIds | Strin g | Body | 是 | ["default"] | 线路ID列表。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | ACL策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateRecursorAcl &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49
```

`&Name=`策略名称。

```
&Policy=true &LineIds=["default"]
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 修改GlobalZone解析记录的备注：

**UpdateGlobalZoneRecordRemark**

调用UpdateGlobalZoneRecordRemark接口修改全局内网的域名解析记录的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 专有云DNS

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 解析记录的ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateGlobalZoneRecordRemark &Id=56bab908-04e0-44ee-b126-1cbdbcd24507
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

专有云DNS

##### 查询RecursorAcl策略列表：

**DescribeRecursorAcls**

调用DescribeRecursorAcls接口查询递归ACL策略列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | 策略名称 | 策略名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | 请求线路ID列表。 |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | ACL策略名称。 |
| -Name | String | name | ACL策略名称。 |
| -Policy | String | true | 允许递归。取值说明： true：允许递归。 false：不允许递归。 |
| -Remark | String | remark | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error messga | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecursorAcls
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error messga",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Policy":"true",
  "LineIds":"[\"default\"]",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error messga</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Policy>true</Policy>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 查询PrivateZones租户内网域名：

**DescribePrivateZones**

调用DescribePrivateZones接口查询租户内网域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Id | Strin g | Body | 否 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |
| Name | Strin g | Body | 否 | com | 域名名称（按照包含匹配）。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - RegionAndVpc s | Array |  | 关联的VPC列表和region信息。 |
| --Vpcs | Array |  | 关联的VPC列表。 |
| ---Id | String | vpc- 9gd80vqxu8zq5j5s t90yx | VPC的ID。 |
| ---Name | String | vpc-name | VPC的名称。 |
| --RegionId | String | cn-region-env1- d01 | VPC对应的region信息。 |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |
| -Name | String | com. | 域名名称。 |
| -CallerUid | String | 126760529569940 0 | 系统参数。 |
| -VpcCount | Integer | 1 | 已关联VPC个数。 |
| -RecordCount | Integer | 1 | 解析记录集总数。 |
| - GtmInstanceC ount | Integer | 0 | 创建的调度实例的总数。 |
| -Remark | String | remark | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |

|  | 开发指南·API参考 |  |  | 专有云DN | S |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePrivateZones
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":"",
  "VpcCount":1,
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "CallerUid":"",
  "-RegionAndVpcs":{
   "--Vpcs":{
    "Id":"vpc-9gd80vqxu8zq5j5st90yx",
    "Name":"vpc-name"
   },
   "RegionId":"cn-region-env1-d01"
  },
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId> 101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId>
 <PageSize>10</PageSize>
 <Message>error message</Message>
 <PageNumber>1</PageNumber>
 <Data>
  <GtmInstanceCount  />
  <VpcCount>1</VpcCount>
  <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
  <UpdateTimestamp>1702460677</UpdateTimestamp>
  <RecordCount>1</RecordCount>
  <CreateTimestamp>1702460677</CreateTimestamp>
  <CallerUid  />
  <-RegionAndVpcs>
   <--Vpcs>
    <Id>vpc-9gd80vqxu8zq5j5st90yx</Id>
    <Name>vpc-name</Name>
   </--Vpcs>
   <RegionId>cn-region-env1-d01</RegionId>
  </-RegionAndVpcs>
  <Name>com.</Name>
  <Remark>remark</Remark>
 </Data>
 <TotalItems>10</TotalItems>
 <Code>error code</Code>
```

##### 添加RecursorAcl：AddRecursorAcl

调用AddRecursorAcl接口查询递归ACL策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | 策略名称 | ACL策略名称。 |
| Policy | Strin g | Body | 是 | true | 允许递归。取值说明： true：允许递归。 false：不允许递归。 |
| LineIds | Strin g | Body | 是 | ["default"] | 请求来源。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 递归ACL策略的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddRecursorAcl
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id> <Code>error code</Code>
```

##### 修改地址池健康检查：UpdateDnsGtmMonitor

调用UpdateDnsGtmMonitor接口修改地址池健康检查。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 健康检查的ID。 |
| ProtocolTy pe | Strin g | Body | 是 | HTTP | 探测类型。取值说明： ICMP：ICMP类型探测。 TCP：TCP类型探测。 UDP：UDP类型探测。 HTTP：HTTP类型探测。 HTTPS：HTTPS类型探测。 |
| GtmAddre ssPoolId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 地址池ID。 |
| Enable | Boole an | Body | 是 | true | 是否开启。取值说明： true：开启探测。 false: 关闭探测。 |
| MonitorEx tendInfo | Json | Body | 否 | {"code":200,"path":"ind ex.htm","host":"aliyun.c om"} | 扩展信息，各协议检查所需参数： HTTP(S)： port：检查端口。 host：Host设置。 path：URL路径。 code：返回码大于多少报错。 TCP(UDP)： port：检查端口。 ICMP：不填写。 |
| Interval | Integ er | Body | 是 | 15 | 检查间隔（秒）。 |
| Timeout | Integ er | Body | 是 | 3 | 超时时间（秒）。 |
| Evaluation Count | Integ er | Body | 是 | 5 | 重试次数。 |
| AgentIds | Strin g | Body | 是 | ["agent-id1","agent-id1"] | 探测节点的ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |

|  | 开发指南·API参考 |  |  | 专有云DN | S |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 健康检查的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateDnsGtmMonitor
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 查询PrivateZone解析记录列表：

**DescribePrivateZoneRecords**

调用DescribePrivateZoneRecords接口查询租户内网域名的解析配置列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户内网域名的ID。 |

|  | 专有云DNS |  |  |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 否 | www | 解析记录名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | 私有线路ID集合。 |
| -RDatas | Array |  |  |
| --Value | String | 1.1.1.1 | 值。 |
| --LbaWeight | Integer | 100 | 权重。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 记录ID。 |
| -Name | String | www | 记录名称。 |
| -CallerUid | String | 126760529569940 0 | 系统参数。 |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 租户内网域名的ID。 |
| -ZoneName | String | com. | 租户内网域名的名称。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Type | String | A | 记录类型。取值说明： A：将域名指向一个IPV4地址。 AAAA：将域名指向一个IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的DNS服务器解析。 |
| -Ttl | Integer | 300 | 记录的缓存时间。 |
| -LbaStrategy | String | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址（非权重）。 _ RATIO：按权重返回地址（权重）。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| -Remark | String | remark | 备注。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribePrivateZoneRecords &ZoneId=56bab908-04e0-44ee-b126-1cbdbcd24507
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "LineIds":"[\"default\"]",
  "Ttl":300,
  "CallerUid":"1267605295699400",
  "Name":"www",
  "Remark":"remark",
  "ZoneName":"com.",
  "Type":"A",
  "-RDatas":{
   "LbaWeight":100,
   "Value":"1.1.1.1"
  },
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507</ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Ttl>300</Ttl>
 <CallerUid>1267605295699400
 </CallerUid>
 <Name>www</Name>
 <Remark>remark</Remark>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 查询GlobalZone的列表：

**DescribeGlobalZones**

调用DescribeGlobalZones接口查询全局内网域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | com | 域名名称（按照包含匹配）。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名的ID。 |
| -Name | String | com. | 域名的名称。 |
| -RecordCount | Integer | 1 | 解析记录集总数。 |
| - GtmInstanceC ount | Integer | 0 | 创建的调度实例的总数。 |
| -Remark | String | remark | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGlobalZones
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":0,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
  "Remark":"remark"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <GtmInstanceCount>0</GtmInstanceCount>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <Remark>remark</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 查询日志管理：DescribeDnsGtmLogs

调用DescribeDnsGtmLogs接口查询日志管理。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Keyword | Strin g | Body | 否 | keyword | 搜索关键字。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| EventType | Strin g | Body | 否 |  | 查询行为类型。取值说明： 主备地址池切换： addresspool-switch。 地址池不可用： addresspool-became- unavailable。 地址池恢复可用： addresspool-became- available。 地址不可用：address- became-unavailable。 地址恢复可用： address-became- available。 |
| StartTime stamp | Long | Body | 否 | 1707363894 | 开始时间戳（秒）。 |
| EndTimest amp | Long | Body | 否 | 1707363894 | 结束时间戳（秒）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 日志的ID。 |
| -Target | String | 对象 | 对象。 |
| - CreateTimesta mp | Long | 1707363894 | 时间。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -EventType | String |  | 行为类型。取值说明： 主备地址池切换：addresspool-switch。 地址池不可用：addresspool-became- unavailable。 地址池恢复可用：addresspool-became- available。 地址不可用：address-became- unavailable。 地址恢复可用：address-became- available。 |
| -Detail | String | detail | 内容。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDnsGtmLogs
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "Target":"对象",
  "EventType":"",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "CreateTimestamp":1707363894,
  "Detail":"detail"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <Target>对象</Target>
 <EventType  />
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <CreateTimestamp>1707363894</CreateTimestamp>
 <Detail>detail</Detail>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 删除GlobalZone：DeleteGlobalZone

调用DeleteGlobalZone接口删除全局内网域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 全局内网域名的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 全局内网域名的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteGlobalZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

##### 修改节点：UpdateNode

调用UpdateNode接口修改节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 343778269185 | 节点ID。 |
| Descriptio n | Strin g | Body | 否 | description | 描述。 |
| AnycastAd drs | Strin g | Body | 否 | 10.1.0.12,10.1.0.13 | anycast服务地址。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | regionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Id | String | 343778269185 | 节点的ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateNode
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### 添加PrivateZone解析记录:

**AddPrivateZoneRecord**

调用AddPrivateZoneRecord接口租户内网域名的解析配置记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户内网域名的ID。 |
| Name | Strin g | Body | 否 | www | 记录名称。 |
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ttl | Integ er | Body | 是 | 300 | 记录缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| RDatas | Repe atList | Body | 是 |  |  |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |
| LineIds | Strin g | Body | 是 | ["default"] | 解析线路列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 解析记录的ID。 |

**示例**

请求示例专有云DNS

```
http(s)://[Endpoint]/?Action=AddPrivateZoneRecord &ZoneId= &Type=A &Ttl=300 &LbaStrategy=ALL_RR &RDatas= &LineIds=["default"]
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 添加地址池：AddDnsGtmAddressPool

调用AddDnsGtmAddressPool接口，添加地址池。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | name | 地址池名称。 |
| Type | Strin g | Body | 是 | A | 地址池类型。取值说明： A：IPV4地址。 AAAA：IPV6地址。 CNAME：域名。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| Addr | Repe atList | Body | 是 |  |  |
| -Value | Strin g |  | 是 | 1.1.1.1 | 地址值。 |
| -Mode | Strin g |  | 是 | SMART | 模式。取值说明： SMART：智能返回。 ONLINE：永远在线。 OFFLINE：永远离线。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 地址池的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddDnsGtmAddressPool &Name=name &Type=A &LbaStrategy=ALL_RR &Addr=
```

&公共请求参数正常返回示例专有云DNS `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 修改PrivateForwardZone备注：

**UpdatePrivateForwardZoneRemark**

调用UpdatePrivateForwardZoneRemark接口，修改租户默认转发配置的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户默认转发配置的ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 租户默认转发配置的ID。 |

专有云DNS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateForwardZoneRemark &Id=56bab908-04e0-44ee-b126-1cbdbcd24507
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507 </Id> <Code>error code </Code>
```

##### 租户转发域名绑定VPC：BindForwardZoneVpc

调用BindForwardZoneVpc给租户转发域名绑定VPC。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | 是 |  | 绑定的VPC列表。 |
| -Id | Strin g |  | 是 | vpc- 9gd80vqxu8zq5j5st90yx | VPC的ID。 |
| -Name | Strin g |  | 否 | vpc-name | VPC的名称。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | region信息。 |

|  | 开发指南·API参 | 考 |  |  |  | 专有云DN | S |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户转发配置的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=BindForwardZoneVpc
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### 解除租户转发配置绑定的VPC：

**DeleteForwardZoneVpc**

调用DeleteForwardZoneVpc接口，解除租户转发配置绑定的VPC。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Vpcs | Repe atList | Body | 是 |  |  |
| -Id | Strin g |  | 是 | vpc- 9gd80vqxu8zq5j5st90yx | VPC的ID。 |
| -Name | Strin g |  | 否 | vpc-name | VPC的名称。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | VPC的region信息。 |
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户转发配置的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteForwardZoneVpc &Vpcs= &RegionId=cn-region-env1-d01 &Id=56bab908-04e0-44ee-b126-1cbdbcd24507
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Code>error code</Code>
```

##### 修改租户默认转发配置:

**UpdatePrivateDefaultForwardZone**

调用UpdatePrivateDefaultForwardZone接口，修改租户默认转发配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 租户默认转发配置的ID。 |
| ForwardM ode | Strin g | Body | 是 | FORWARD ONLY _ | 转发模式。取值说明： FORWARD ONLY:全部 _ 转发模式(建议)-全部请求只做转发(不作任何递归)。 FORWARD FIRST:优先 _ 转发模式-转发失败降级到互联网递归。 |
| Forwarder s | Strin g | Body | 是 | ["1.1.1.1","1.1.1.2"] | 转发目的IP列表。 |
| Remark | Strin g | Body | 否 | Remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 租户默认转发配置的ID。 |

专有云DNS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdatePrivateDefaultForwardZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除GlobalLine记录：DeleteGlobalLine

调用DeleteGlobalLine接口删除全局线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 全局线路的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

| 开发指南·API参考 |  |  | 专有云DN |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 全局线路的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteGlobalLine
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除GlobalZone解析记录:

**DeleteGlobalZoneRecord**

调用DeleteGlobalZoneRecord接口删除全局内网域名的解析配置记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 解析记录的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteGlobalZoneRecord&Id=56bab908-04e0-44ee-b126-1cbdbcd2
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 删除PrivateZone租户内网域名的解析记录：

**DeletePrivateZoneRecord**

调用DeletePrivateZoneRecord接口删除租户内网域名的解析记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeletePrivateZoneRecord
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

专有云DNS

#### 跨云API参考

##### 查询节点管理列表：DescribeNodes

调用DescribeNodes接口查询节点管理列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -AnycastAddr | String | 10.1.0.12,10.1.0.13 | anycast服务地址。 |
| -Id | String | 343778269185 | 节点ID。 |
| -LocalAddr | String | 10.1.24.1 | 节点IP。 |
| -RegionId | String | cn-region-env1- d01 | regionID。 |
| -Description | String | description | 描述。 |
| -Role | String | leader | 节点角色类型。取值说明： leader：leader节点（选举节点）。 follower ：follower节点（选举节点）。 learner：learner节点（非选举节点）。 candidate：异常状态节点。 |
| -Index | Integer | 1 | 最新同步logid。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -IsOnline | Boolean | true | 工作状态。取值说明： true：正常。 false：离线。 |
| - IsInEmergency | Boolean | false | 是否是应急组状态。取值说明： true：是。 false：不是。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Total | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeNodes
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Total":10,
 "Data":{
  "Role":"leader",
  "Description":"description",
  "AnycastAddr":"10.1.0.12,10.1.0.13",
  "RaftServicePort":"",
  "IsInEmergency":false,
  "Index":1,
  "Id":"343778269185",
  "RegionId":"cn-region-env1-d01",
  "CmdServicePort":"",
  "LocalAddr":"10.1.24.1",
  "IsOnline":true
 },
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <PageSize>10</PageSize> <Message>error message </Message> <PageNumber>1</PageNumber> <Total>10</Total> <Data>
 <Role>leader</Role>
 <Description>description</Description>
 <AnycastAddr>10.1.0.12,10.1.0.13
 </AnycastAddr>
 <RaftServicePort  />
 <IsInEmergency>false</IsInEmergency>
 <Index>1</Index>
 <Id>343778269185
 </Id>
 <RegionId>cn-region-env1-d01
 </RegionId>
 <CmdServicePort  />
 <LocalAddr>10.1.24.1</LocalAddr>
 <IsOnline>true</IsOnline>
</Data> <Code>error code </Code>
```

专有云DNS

##### 修改UniversalLine跨云解析线路的优先级：

**UpdateUniversalLinePriority**

调用UpdateUniversalLinePriority接口修改跨云解析线路的优先级。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级，1的优先级最高，数值越大优先级越低。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUniversalLinePriority
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

专有云DNS `XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 开启应急组：EnableEmergencyGroup

调用EnableEmergencyGroup接口开启应急组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ids | Strin g | Body | 是 | "1343778269181,34377 8269182,343778269183 " | 需要组建新集群的节点 ID（需要","号分割）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=EnableEmergencyGroup
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id /> <Code>error code </Code>
```

##### 添加UniversalZone全局共享域名：

**AddUniversalZone**

调用AddUniversalZone接口添加跨云共享域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | com. | 跨云共享域名名称（必须以"."结尾）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |

专有云DNS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUniversalZone
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改UniversalZoneRecord跨云共享域名解析记录

**的备注：UpdateUniversalZoneRecordRemark**

调用UpdateUniversalZoneRecordRemark接口修改跨云共享域名的解析记录的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录的ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRecordRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 关闭应急组：DisableEmergencyGroup

调用DisableEmergencyGroup接口关闭应急组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisableEmergencyGroup
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id /> <Code>error code </Code>
```

##### 修改UniversalZone跨云共享域名的备注：

**UpdateUniversalZoneRemark**

调用UpdateUniversalZoneRemark接口修改跨云共享域名的备注。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 域名ID。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRemark
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

##### 删除UniversalLine跨云解析线路：

**DeleteUniversalLine**

调用DeleteUniversalLine接口删除跨云解析线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUniversalLine &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"\terror message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message> error message</Message>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <Code>error code</Code>
```

专有云DNS

##### 修改UniversalLine跨云解析线路：

**UpdateUniversalLine**

调用UpdateUniversalLine接口修改跨云解析线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 线路ID。 |
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例专有云DNS

```
http(s)://[Endpoint]/?Action=UpdateUniversalLine &Id=e8605e05-4320-4ef5-983d-c5dd48d05b49 &Name=name &Priority=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改UniversalZoneRecord跨云共享域名的解析

**记录：UpdateUniversalZoneRecord**

调用UpdateUniversalZoneRecord接口修改跨云共享域名的解析记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 解析记录的ID。 |
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 跨云共享域名的ID。 |
| Name | Strin g | Body | 否 | www | 解析记录的名称。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针， 通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |
| Ttl | Integ er | Body | 是 | 300 | 记录缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| RDatas | Repe atList | Body | 是 |  | 记录值集合。 |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。非权重类型不用填写。 |
| LineIds | Strin g | Body | 是 | ["default"] | 线路列表。 |
| Remark | Strin g | Body | 否 | remark | 备注。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 解析记录的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateUniversalZoneRecord
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 修改节点：UpdateNode

调用UpdateNode接口修改节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 343778269185 | 节点ID。 |
| Descriptio n | Strin g | Body | 否 | description | 备注。 |
| AnycastAd drs | Strin g | Body | 否 | 10.1.0.12,10.1.0.13 | anycast服务地址。 |
| RegionId | Strin g | Body | 是 | cn-region-env1-d01 | RegionID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Id | String | 343778269185 | 节点的ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateNode
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message</Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### 删除UniversalZone跨云共享域名：

**DeleteUniversalZone**

调用DeleteUniversalZone接口删除跨云共享域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 域名ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 域名ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUniversalZone
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 备节点切换主节点：TransferLeadership

调用TransferLeadership接口将备节点切换成主节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | 343778269185 | 节点ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Id | String | 343778269185 | 切换成主节点的节点ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例专有云DNS

```
http(s)://[Endpoint]/?Action=TransferLeadership &Id=343778269185
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"343778269185",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>343778269185</Id> <Code>error code </Code>
```

##### 查询UniversalLine跨云解析线路列表：

**DescribeUniversalLines**

调用DescribeUniversalLines接口查询跨云解析线路列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Ip | Strin g | Body | 否 | 1.1.1.1 | 查询IP，IPV4支持模糊查询，IPV6只支持精确查询。 |
| Name | Strin g | Body | 否 | name | 地址池名称（按照包含匹配）。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |

专有云DNS

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -V4Addresses | String | ["1.1.1.1"] | IPV4地址列表。 |
| -V6Addresses | String | ["2400:3200::7777 "] | IPV6地址列表。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路的ID。 |
| -Name | String | name | 线路名称。 |
| -Priority | Integer | 1 | 线路优先级，1优先级最高，数值越大优先级越低。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUniversalLines
```

&公共请求参数正常返回示例专有云DNS `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "V4Addresses":"[\"1.1.1.1\"]",
  "V6Addresses":"[\"2400:3200::7777\"]",
  "Priority":1,
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "CreateTimestamp":1702460677,
  "Name":"name"
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <V4Addresses>[&quot;1.1.1.1&quot;]</V4Addresses>
 <V6Addresses>[&quot;2400:3200::7777&quot;]</V6Addresses>
 <Priority>1</Priority>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49
 </Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>name</Name>
</Data> <TotalItems>10</TotalItems> <Code>error code </Code>
```

##### 添加UniversalLine跨云解析线路：

**AddUniversalLine**

调用AddUniversalLine接口添加跨云解析线路。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Body | 是 | name | 线路名称。 |
| Priority | Integ er | Body | 是 | 1 | 线路优先级。1优先级最高，数值越大优先级越低。 |
| V4Addres ses | Strin g | Body | 否 | ["1.1.1.1","2.2.2.2"] | ipv4地址列表（ipv4和ipv6 最少填写一个）。 |
| V6Addres ses | Strin g | Body | 否 | ["2400:3200::7777"] | ipv6地址列表（ipv4和ipv6 最少填写一个）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 线路ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddUniversalLine &Name=name &Priority=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0 </RequestId> <Message>error message </Message> <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49 </Id> <Code>error code </Code>
```

##### 删除UniversalZone解析记录:

**DeleteUniversalZoneRecord**

调用DeleteUniversalZoneRecord接口删除跨云共享域名的解析配置记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Id | Strin g | Body | 是 | e8605e05-4320-4ef5- 983d-c5dd48d05b49 | 记录ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 记录ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteUniversalZoneRecord&Id=e8605e05-4320-4ef5-983d-c5dd4 8d05b49
```

&公共请求参数正常返回示例专有云DNS `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```

##### 获取UniversalZone解析列表:

**DescribeUniversalZoneRecords**

调用DescribeUniversalZoneRecords接口查询跨云共享域名的解析配置列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | www | 解析记录名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -LineIds | String | ["default"] | 解析线路。 |
| -RDatas | Array |  |  |

|  | 专有云DNS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --Value | String | 1.1.1.1 | 值。 |
| --LbaWeight | String | 100 | 权重。 |
| -Id | String | e8605e05-4320- 4ef5-983d- c5dd48d05b49 | 记录ID。 |
| -Name | String | www | 记录名称。 |
| -ZoneId | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |
| -ZoneName | String | com. | 域名名称。 |
| -Type | String | A | 记录类型。取值说明： A：将域名指向一个IPV4地址。 AAAA：将域名指向一个IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制255，通常做SPF记录 （反垃圾邮件）。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针，通常用于 ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的DNS服务器解析。 |
| -Ttl | Integer | 300 | 记录的缓存时间。 |
| -LbaStrategy | String | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址（非权重）。 _ RATIO：按权重返回地址（权重）。 |
| -Remark | String | 备注 | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| TotalItems | Integer | 10 | 总数。 |
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUniversalZoneRecords?ZoneId=56bab908-04e0-44ee-b12 6-1cbdbcd24507&PageNumber=1&PageSize=10
```

&公共请求参数正常返回示例 `JSON` 格式专有云DNS

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "PageSize":10,
 "PageNumber":1,
 "Data":{
  "ZoneName":"com.",
  "Type":"A",
  "ZoneId":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "LbaStrategy":"ALL_RR",
  "-RDatas":{
   "LbaWeight":"100",
   "Value":"1.1.1.1"
  },
  "LineIds":"[\"default\"]",
  "Id":"e8605e05-4320-4ef5-983d-c5dd48d05b49",
  "UpdateTimestamp":1702460677,
  "Ttl":300,
  "CreateTimestamp":1702460677,
  "Name":"www",
```

`"Remark":"`备注"

```json
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <PageSize>10</PageSize> <PageNumber>1</PageNumber> <Data>
 <ZoneName>com.</ZoneName>
 <Type>A</Type>
 <ZoneId>56bab908-04e0-44ee-b126-1cbdbcd24507</ZoneId>
 <LbaStrategy>ALL_RR</LbaStrategy>
 <-RDatas>
  <LbaWeight>100</LbaWeight>
  <Value>1.1.1.1</Value>
 </-RDatas>
 <LineIds>[&quot;default&quot;]</LineIds>
 <Id>e8605e05-4320-4ef5-983d-c5dd48d05b49</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <Ttl>300</Ttl>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>www</Name>
 <Remark>备注</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

专有云DNS

##### 获取UniversalZone列表:

**DescribeUniversalZones**

调用DescribeUniversalZones接口查询跨云共享域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageNum ber | Integ er | Body | 否 | 1 | 页数。 |
| PageSize | Integ er | Body | 否 | 10 | 每页显示数量。 |
| Name | Strin g | Body | 否 | www | 域名名称（按照包含匹配）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  |  |
| -Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 域名ID。 |
| -Name | String | com. | 域名名称。 |
| -RecordCount | Integer | 1 | 解析记录集总数。 |
| - GtmInstanceC ount | Integer |  | 无效字段。 |
| -Remark | String | 备注 | 备注。 |
| - CreateTimesta mp | Long | 1702460677 | 创建时间戳（秒）。 |
| - UpdateTimest amp | Long | 1702460677 | 修改时间戳（秒）。 |
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |

| 专有云DNS |  |  | 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| TotalItems | Integer | 10 | 总数量。 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页数。 |
| PageSize | Integer | 10 | 每页显示数量。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUniversalZones?PageNumber=1&PageSize=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "PageSize":10,
 "Message":"error message",
 "PageNumber":1,
 "Data":{
  "GtmInstanceCount":"",
  "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
  "UpdateTimestamp":1702460677,
  "RecordCount":1,
  "CreateTimestamp":1702460677,
  "Name":"com.",
```

`"Remark":"`备注"

```json
 },
 "TotalItems":10,
 "Code":"error code"
}
```

`XML` 格式专有云DNS

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <PageSize>10</PageSize> <Message>error message</Message> <PageNumber>1</PageNumber> <Data>
 <GtmInstanceCount  />
 <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id>
 <UpdateTimestamp>1702460677</UpdateTimestamp>
 <RecordCount>1</RecordCount>
 <CreateTimestamp>1702460677</CreateTimestamp>
 <Name>com.</Name>
 <Remark>备注</Remark>
</Data> <TotalItems>10</TotalItems> <Code>error code</Code>
```

##### 添加UniversalZone解析记录:

**AddUniversalZoneRecord**

调用AddUniversalZoneRecord接口添加跨云共享域名的解析配置记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ZoneId | Strin g | Body | 是 | 56bab908-04e0-44ee- b126-1cbdbcd24507 | 域名ID。 |
| Name | Strin g | Body | 否 | www | 记录名称。 |

专有云DNS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Type | Strin g | Body | 是 | A | 记录类型。取值说明： A：将域名指向一个IPV4 地址。 AAAA：将域名指向一个 IPV46。 CNAME：将域名指向另一个域名。 MX：将域名指向邮件服务器地址。 TXT：文本长度限制 255，通常做SPF记录 (反垃圾邮件)。 PTR：记录IP地址反向解析的域名。 SRV：记录提供特定的服务的服务器。 NAPRT：记录域名权威指针，通常用于ENUM。 CAA：为域名设置证书分发机构授权信息。 NS：将于明指向指定的 DNS服务器解析。 |
| Ttl | Integ er | Body | 是 | 300 | 记录的缓存时间。 |
| LbaStrate gy | Strin g | Body | 是 | ALL RR _ | 负载均衡策略。取值说明： ALL RR：返回全部地址 _ （非权重）。 RATIO：按权重返回地址 （权重）。 |
| Remark | Strin g | Body | 否 | 备注 | 备注。 |
| RDatas | Repe atList | Body | 是 |  | 记录值集合。 |
| -Value | Strin g |  | 是 | 1.1.1.1 | 值。 |
| - LbaWeigh t | Integ er |  | 否 | 100 | 权重。 |
| LineIds | Strin g | Body | 是 | ["default"] | 解析线路。 |

**返回数据**

专有云DNS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 101D8AB1-26D3- 4C06-8D0E- 2E133B5075A0 | 请求ID。 |
| Message | String | error message | 异常请求的信息。 |
| Code | String | error code | 异常请求的编码。 |
| Id | String | 56bab908-04e0- 44ee-b126- 1cbdbcd24507 | 解析记录的ID。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=AddUniversalZoneRecord? ZoneId=aaa&Name=www&Type=A&Ttl=300&LbaStrategy=RATIO&Remark=remark&LineIds= ["default"]&RDatas.1.Value=1.1.1.1&RDatas.1.LbaWeight=100
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"101D8AB1-26D3-4C06-8D0E-2E133B5075A0",
 "Message":"error message",
 "Id":"56bab908-04e0-44ee-b126-1cbdbcd24507",
 "Code":"error code"
}
```

`XML` 格式

```xml
<RequestId>101D8AB1-26D3-4C06-8D0E-2E133B5075A0</RequestId> <Message>error message</Message> <Id>56bab908-04e0-44ee-b126-1cbdbcd24507</Id> <Code>error code</Code>
```
