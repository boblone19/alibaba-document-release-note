---
title: "实时计算（流计算） 开发指南（Blink）"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 246
source_pdf: "05_开发指南（Blink）_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） 开发指南（Blink）

实时计算（流计算）

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

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**背景信息**

AccessKey支持两种授权模式： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 本文仅为您介绍如何获取通过RAM授权的AccessKey，通过STS授权的AccessKey获取方式请参见获取STS AccessKey。 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList文档。 |

实时计算（流计算）

| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见Apsara Uni-manager 运营控制台开发指南中的ListResourceGroup文档。 |
|---|---|
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，将鼠标悬停在当前登录用户的头像上，单击**个人信息**。
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
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见A
psara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。 实时计算（流计算）
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中
的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例，获取步骤如下：
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

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。

| 框中查看 | RAM Role |  |  | 。 |
|---|---|---|---|---|
| RAM Role |  | 获得 | stsAK |  |

实时计算（流计算）

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

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
```

`//` 调用云产品的`API`

```
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
} public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, String stsToken) {
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

实时计算（流计算）

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
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看apigateway.openapi.endpoint值，即 `Endpoint` 。
实时计算（流计算）

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请参见获取公共Header参数。

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 调用示例如下： 实时计算（流计算）

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

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 实时计算（流计算）

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

实时计算（流计算）

### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 示例代码如下：

```java
import (
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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 实时计算（流计算）

```java
import (
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

实时计算（流计算） 使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

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

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

目前仅支持通过RPC方式调用API。

**CommonRequest调用示例**

调用示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 示例代码如下： 实时计算（流计算）

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

实时计算（流计算）

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

) 实时计算（流计算）

## Flink SQL

### 概述

Flink SQL是实时计算为简化实时计算模型，降低用户使用实时计算门槛而设计的一套符合标准SQL语义的实时计算SQL。Flink SQL有以下优势： 开发成本低。使用阿里云Flink SQL，可以不再编写长达数千行的Storm代码，通过一两句简单的SQL即可描述复杂且多变的业务逻辑。 使用最原始的Storm编程模式，您必须考虑各类系统异常情况，包括系统异常、系统宕机、错误情况下数据准确性等各类细节问题。 阿里云团队将上述各类问题均在SQL语义中进行抽象和解决。实时计算具备以下特点。 数据的准确性。实时计算独特的Exactly-Once Processing语义保证，能够保证各种Failover场景的数据准确性。 性能的可优化性。实时计算集成SQL优化逻辑，将SQL翻译为最底层的执行代码的普通人员编写的Storm代码，效率更高，提高编写SQL代码的效率。 编程的可扩展性。实时计算支持UFD的扩展功能，对于SQL无法表达的、或者业务定制化逻辑，阿里实时计算通过自定义UFD进行功能扩展。 系统的可扩展性。实时计算在保证任务和系统稳定性同时，在数据突增时（如，双11）可以做到弹性扩容。

### 关键字

本文为您介绍实时计算关键字。

**实时计算关键字**

表 1. 常用关键字

| 常用类型 | 关键字 |
|---|---|
| 数据类型 | VARCHAR、INT、BIGINT、DOUBLE 、DATE 、BOOLEAN 、TINYINT、 SMALLINT 、FLOAT 、DECIMAL、VARBINARY |
| DDL | CREATE TABLE、CREATE FUNCTION 、CREATE VIEW |
| DML | INSERT INTO |
| SELECT 子句 | SELECT FROM、WHERE、GROUP BY 、JOIN |

**命名规则**

源表名称、结果表名称、view表名称、别名名称遵循标准数据库命名规则定义，必须以字母开头，并且只能包含字母、数字和下划线。

**保留关键字**

| ` | ，例如 | ｀value｀ |
|---|---|---|

```
 A,ABS,ABSOLUTE,ACTION,ADA,ADD,ADMIN,AFTER,ALL,ALLOCATE,ALLOW,ALTER,ALWAYS,AND,ANY,ARE,ARRAY,AS,ASC,ASENSITIVE,ASSERTION,ASSIGNMENT,ASYMMETRIC,AT,A
EXEC,EPOCH,EQUALS,ESCAPE,EVERY,EXCEPT,EXCEPTION,EXCLUDE,EXCLUDING,EXEC,EXECUTE,EXISTS,EXP,EXPLAIN,EXTEND,EXTERNAL,EXTRACT,FALSE,FETCH,FILTER,FINAL,
```

### 基本概念

#### 3.3.1. 时间属性

本文为您介绍Flink SQL所支持的Event Time和Processing Time时间类型及属性。 Flink支持三种与流数据处理相关的时间概念：Processing Time、Event Time和Ingestion Time。 Blink SQL仅支持其中的两种时间类型Event Time和Processing Time： Event Time：您提供的事件时间（通常是数据的最原始的创建时间）。Event Time必须是您提供在数据储存里的数据。 Processing Time：系统对事件进行处理的本地系统时间，单位为毫秒。

**Event Time**

Event Time也称为Row Time。EventTime时间属性必须在源表DDL中声明，可以将源表中的某一字段声明成Event Time。目前只支持将TIMESTAMP类型（将来会支持 LONG类型）声明成Row Time字段。如果源表中需要声明为Event Time的列不是TIMESTAMP类型，需要借助计算列，基于现有列构造出一个TIMESTAMP类型的列。 由于数据本身的乱序、网络的抖动（网络堵塞导致的数据传输延迟的变化）或者其它原因，导致了数据到达的顺序和被处理的顺序，可能是不一致的（乱序）。因此需要首先窗口函数基于Event Time聚合的示例如下。 实时计算（流计算）

```
CREATE TABLE tt_stream (
  a VARCHAR,
  b VARCHAR,
  ts TIMESTAMP,
  WATERMARK wk1 FOR ts as withOffset (ts, 1000) --Watermark计算方法。
) WITH (
  type = 'sls',
  topic = '<yourTopicName>',
  accessId = '<yourAccessId>',
  accessKey = '<yourAccessSecret>'
); CREATE TABLE rds_output (
  id VARCHAR,
  win_start TIMESTAMP,
  win_end TIMESTAMP,
  cnt BIGINT
) WITH (
  type = 'rds',
  url = 'jdbc:mysql://****3306/test',
  tableName = '<yourTableName>',
  userName = '<yourUserName>',
  password = '<yourPassword>'
);
  INTO rds_output
  a AS id,
  SESSION_START (ts, INTERVAL '1' SECOND) AS win_start,
  SESSION_END (ts, INTERVAL '1' SECOND) AS win_end,
FROM
  tt_stream
  BY SESSION (ts, INTERVAL '1' SECOND),
```

a

**Processing Time**

Processing Time是系统产生的，不在您的原始数据中，您需要在数据源表的声明中明文定义一个Processing Time列。

```
filedName as PROCTIME()
```

窗口函数基于Processing Time聚合的示例如下。

```
CREATE TABLE mq_stream (
    a VARCHAR,
    b VARCHAR,
    c BIGINT,
```

`ts AS PROCTIME () --`在数据源表的声明中明文定义一个`Processing Time`列。

```
  ) WITH (
    type = 'mq',
    topic = '<yourTopic>',
    accessId = '<yourAccessId>',
    accessKey = '<yourAccessSecret>'
  );
CREATE TABLE rds_output (
  id VARCHAR,
  win_start TIMESTAMP,
  win_end TIMESTAMP,
  cnt BIGINT
) with (
  type = 'rds',
  url = '<yourDatebaseURL>',
  tableName = '<yourDatabasTableName>',
  userName = '<yourUserName>',
  password = '<yourPassword>'
);
  INTO rds_output
  a AS id,
  SESSION_START (ts, INTERVAL '1' SECOND) AS win_start,
  SESSION_END (ts, INTERVAL '1' SECOND) AS win_end,
FROM
  mq_stream
  BY SESSION (ts, INTERVAL '1' SECOND),
```

a

**时间属性字段传递**

时间属性字段经过如下操作后会失去时间属性特性： 对时间属性字段以外的字段进行GROUP BY（滚动窗口、滑动窗口或会话窗口中的GROUP BY除外）操作。 双流JOIN操作。 实时计算（流计算）

**说明**

UNION操作。**UNION = RETRACT**＋**UNION ALL**。 如果经过以上操作后，继续使用该时间属性字段进行窗口函数运算，会出现类似 `org.apache.flink.table.api.ValidationException: Window can only be defined`

```
over a time attribute column. 的报错。
```

#### 3.3.2. Watermark

实时计算可以基于时间属性对数据进行窗口聚合。基于Event Time时间属性的窗口函数作业中，数据源表的声明中需要使用Watermark方法。

**定义**

Watermark是一种衡量Event Time进展的机制，它是数据本身的一个隐藏属性，Watermark的定义是数据源表DDL定义的一部分。Watermark语法定义如下。

```
WATERMARK [watermarkName] FOR <rowtime_field> AS withOffset(<rowtime_field>, offset)
```

**说明**

实时计算时间属性详情，请参见时间属性。

| 参数 | 是否必填 | 说明 |
|---|---|---|
| watermarkName | 否 | 标识Watermark的名字。 |
| <rowtimefield> _ | 是 | <rowtime _field>必须是表中已定义的一列（当前仅支持TIMESTAMP类型），基于该列生成Watermark，并且标识该列为Event Time列。您可以使用<rowtime _field>在作业代码中定义窗口。 |
| withOffset | 是 | Watermark的生成策略，根据<rowtime _field> - offset生成Watermark的值。withOffset的第一个参数必须是<rowtime _field>。 |
| offset | 是 | Watermark值与Event Time值的偏移量，单位为毫秒。 |

通常，一条记录中的某个字段就代表了该记录的发生时间。例如，表中rowtime字段的类型为TIMESTAMP， `1501750584000`（`2017-08-03 08:56:24.000`）。定义一个基

```
WATERMARK FOR rowtime AS withOffset(rowtime, 4000)
```

这条数据的Watermark时间为 `1501750584000 - 4000 = 1501750580000`（`2017-08-03 08:56:20.000`）。这条数据的Watermark时间含义：时间戳小于 `1501750580000`（`2017-08-03 08:56:20.000`）的数据已经全部到达。

**说明**

在使用Event Time Watermark时的rowtime必须是TIMESTAMP类型。当前支持毫秒级别的、在Unix时间戳里为13位。如果是其他类型或是在Unix时间戳不是13位，建议使用计算列完成转换。 Event Time和Processing Time只能在源表上声明。

**使用总结**

Watermark含义是所有时间戳**t'< t**的事件已经全部发生。如果t（Watermark）已经生效，则后续Event Time小于t的记录将全部丢弃（后续支持用户配置，使Event Time小于t的数据可以更新）。 针对乱序的流，Watermark至关重要。即使部分事件延迟到达，也不会影响窗口计算的正确性。 并行数据流中，当算子（Operator）有多个输入流时，算子的Event Time以最小流Event Time为准。

#### 3.3.3. 计算列

计算列可以使用其它列的数据，计算出其所属列的数值。如果您的数据源表中没有TIMESTAMP类型的列，可以使用计算列方法从其它类型的字段进行转换。

**计算列概念**

计算列是虚拟列，并非实际存储在表中。计算列可以通过表达式、内置函数、或是自定义函数等方式，使用其它列的数据，计算出其所属列的数值。计算列在Flink SQL中可以像普通字段一样被使用。 实时计算（流计算）

**计算列的用途**

目前Watermark的Event Time（也称为Rowtime）列只支持TIMESTAMP类型（未来将支持LONG类型）。Watermark只能定义在源表DDL中，如果您的源表中没有 TIMESTAMP类型的列，可以使用计算列从其他类型的字段进行转换。

**计算列语法**

```
column_name AS computed_column_expression
```

**计算列示例**

Watermark的Rowtime必须是TIMESTAMP数据类型。当前实时计算支持毫秒级别的、在Unix时间戳里是13位TIMESTAMP数据类型。如果DataHub的TIME字段是微秒级别的（16位Unix时间戳），可以用计算列方法转换为13位的时间戳，如下所示。

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
```

ts AS TO_TIMESTAMP(`TIME`/1000), --使用计算列方法，将`16`位时间戳转换为`13`位时间戳。

```
) WITH (
  type = 'datahub',
  ...
);
```

源表数据中的字段 `TIME` 包含时间信息，为BIGINT类型。用计算列的功能将字段 `TIME` 转换成13位时间戳（TIMESTAMP）类型字段 `ts` ，并将 `ts` 字段作为

### 数据类型

### 3.4.1. 数据类型

本文为您介绍实时计算数据类型。

**支持的数据类型**

| 数据类型 | 描述 | 值域 |
|---|---|---|
| VARCHAR | 可变长度字符串 | 最大容量为4Mb |
| BOOLEAN | 逻辑值 | 取值为TRUE、FALSE或UNKNOWN。 |
| TINYINT | 微整型，1字节整数。 | -128到127 |
| SMALLINT | 短整型，2字节整数。 | -32768到32767 |
| INT | 整型，4字节整数。 | -2147483648到2147483647 |
| BIGINT | 长整型，8字节整数。 | -9223372036854775808到9223372036854775807 |
| FLOAT | 4字节浮点数 | 6位数字精度 |
| DECIMAL | 小数类型 | 示例： 123.45 是 DECIMAL(5,2) 的值。 |
| DOUBLE | 浮点，8字节浮点数 | 15位十进制精度 |
| DATE | 日期类型 | 示例： DATE'1969-07-20' 。 |
| TIME | 时间类型 | 示例： TIME '20：17：40' 。 |
| TIMESTAMP | 时间戳，日期和时间 | 示例： TIMESTAMP '1969-07-20 20:17:40' 。 |
| VARBINARY | 二进制数据 | byte[] 数组 |

**类型转换**

**类型转换示例**

测试数据：

| var1(VARCHAR) | big1(BIGINT) |
|---|---|

实时计算（流计算）

| 1000 | 323 |
|---|---|

测试语句：

```
CAST(var1 AS BIGINT) AS AA; CAST(big1 AS VARCHAR) AS BB;
```

测试结果：

| AA(BIGINT) | BB(VARCHAR) |
|---|---|
| 1000 | 323 |

#### 3.4.2. 数据类型之间运算关系

本文为您介绍实时计算数据之间的运算关系。 数据类型之间的运算关系涉及数学和逻辑运算，如下表所示。

| 运算语句 | 描述 | numeric1和numeric2支持的数据类型 | 示例 |
|---|---|---|---|
| numeric1 + numeric2 | 加 | INT,DOUBLE,DECIMAL,BIGINT | 2+4.2 |
| numeric1 - numeric2 | 减 |  | 3-5.3 |
| numeric1 * numeric2 | 乘 |  | 2*4 |
| numeric1 / numeric2 | 除 |  | 2.4/5 |
| numeric1 > numeric2 | > |  | 2.4>5 |
| numeric1 < numeric2 | < |  | 2.4<5 |
| numeric1 >= numeric2 | >= |  | 2.4>=5 |
| numeric1 <= numeric2 | <= |  | 2.4<=5 |
| numeric1 = numeric2 | = | INT,DOUBLE,DECIMAL,BIGINT,VARCHAR | ‘iphone’ = 5 |
| numeric1 <> numeric2 | <> |  | ‘iphone’ <> 5 |

### DDL语句

**3.5.1. 概述**

**语法**

```
CREATE TABLE tableName
     (columnName dataType [, columnName dataType ]*)
     [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

**说明**

阿里云实时计算本身不带有数据存储功能，因此所有的涉及表创建DDL操作实际上均是对于外部数据表/存储的引用声明。示例如下：

```
create table tt_stream(
    a varchar,
    b varchar,
    c varchar
    ) with (
    type='DataHub',
    topic='blink_tt_test',
    accessId='yourAccessId',
    accessKey='yourAccessSecret'
    );
```

此处是在实时计算 Flink SQL中并非创建一个DataHub的Topic，仅仅声明了一个名称为tt_stream的表引用，下游所有的对这张DataHub的Topic相关DML操作均可以使用 tt_stream别名来进行操作。 实时计算对于声明表的作用域是在当前作业（一个SQL文件提交后生成一实时计算作业），即上述有关tt_stream的声明仅在当前SQL有效。在同一个Project下的其他SQL 文件同样可以声明名称为tt_stream的表。 按照SQL标准定义，DDL语法中关键字、表名、列名等是不区分大小写的。 表名、列名必须以字母或者数字开头，表名、列名中只能包含字母、数字、下划线。 DDL声明不完全根据名称进行映射（取决于上游插件的性质），如果插件支持根据key取值（如DataHub），则不要求字段个数完全一致，但名称需要一致，如果上游插件不支持根据key取值，则要求字段个数以及顺序完全一致。建议DDL中声明的字段名称、个数和外部表一致，避免出现定义混乱导致数据错乱的情况。

**字段映射**

外部数据源按照有无Schema分为两大类别。 顺序映射以MQ为代表的不带有Schema系统，这类系统通常是非结构化存储系统，推荐您在DDL SQL声明中字段名称可以自定义，但须按照外部表字段的类型、列数进行对齐。 以MQ为例，MQ的一条记录格式，如下所示。 实时计算（流计算）

```
asavfa,sddd32,sdfdsv
```

TT的字段名按照命名规范来设置。

```
create table tt_stream(
      a varchar,
      b varchar,
      c varchar
      ) with (
      type='mq',
      topic='blink_mq_test',
      accessId='yourAccessId',
      accessKey='yourAccessSecret'
      );
```

名称映射以DataHub为代表的带有Schema系统，这类系统在表存储级别定义了字段名称以及字段类型，强烈推荐您在实时计算SQL中严格按照外部数据存储Schema进行定义， 包括名称、列数、顺序完全一致。

**说明**

如果外部数据存储的字段名称是大小写敏感类型（例如OTS），那么用户在实时计算SQL中需要在区分大小写的字段名称使用‘｀’进行转换。以DataHub 为例，在DDL语法中，声明字段名和目标表的字段名需要名称完全一致。 DataHub定义的Schema如下所示。 Table 1. DataHub定义的Schema

| 字段名 | 类型 |
|---|---|
| name | varchar |
| age | bigint |
| value | varchar |

推荐您将所有列进行声明引用，注意可以少字段，不可以多字段。针对上述DataHub声明的DDL如下所示。

```
create table stream_result (
     name varchar,
     age bigint,
     value varchar
     ) with (
     type='DataHub',
     endpoint='http://dh-cn-hangzhou.aliyuncs.com',
     accessId='yourAccessId',
     accessKey='yourAccessSecret',
     project='project',
     topic='topic'
     );
```

**大小写不敏感**

SQL标准定义中，大小写是不敏感的，示例如下。

```
create table stream_result (
    name             varchar,
    value            varchar
    );
```

和

```
create table STREAM_RESULT (
     NAME             varchar,
     VALUE            varchar
     );
```

但实时计算引用大量外部数据源，这类数据源可能要求大小写敏感，例如TableStore对于大小写是敏感的。如果在TableStore定义了一个NAME的大写字段，应该进行如下定义。

```
create table STREAM_RESULT (
    `NAME`            varchar,
    `VALUE`           varchar
    );
```

而后所有的DML操作中，对于这个字段引用均需要添加反引号，示例如下。

```
INSERT INTO Table_A
    `NAME`,
    `VALUE`
    FROM
    Table_B;
```

#### 3.5.2. 创建数据源表

**3.5.2.1. 概述**

实时计算源表的流式数据驱动实时计的运行。因此，实时计算计作业必须提供至少1个数据源表，用于存储流式数据。

**语法**

实时计算（流计算）

```
  CREATE TABLE tableName
      (columnName dataType [, columnName dataType ]*)
      [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

**示例**

```
CREATE TABLE datahub_stream(
  name VARCHAR,
  age BIGINT,
  birthday BIGINT
) WITH (
  type='datahub',
  endPoint='<yourEndpoint>',
  project='<yourProjectName>',
  topic='<yourTopicName>',
  accessId='<yourAccessId>',
  accessKey='<yourAccessKey>',
  startTime='2017-07-21 00:00:00'
); CREATE TABLE metaq_stream(
 x VARCHAR,
 y VARCHAR,
 z VARCHAR
) WITH (
 type='mq',
 topic='<yourTopicName>',
 endpoint='<yourEndpointName>',
 pullIntervalMs='1000',
 accessId='<yourAccessId>',
 accessKey='<yourAccessKey>',
 startMessageOffset='1000',
 consumerGroup='<yourConsumerGroup>',
 fieldDelimiter='|'
);
```

**获取数据源表属性字段**

获取数据源表属性字段语法

| CREATE TABLE sourcetable ( `timestamp` VARCHAR HEADER, name VARCHAR， MsgID VARCHAR )WITH( type='RDS' ); |  |  |  |  |
|---|---|---|---|---|
| 上面示例中 | `timestamp` | 字段定义为 | HEADER | ，可从数据的属性字段读取数值，后续当成普通字段使用。 |
| 说明不同的源表（DataHub、Log Service或MQ等）存在不同的默认属性字段，部分源表支持设置自定义的属性字段，具体请参见对应的源表文档。 |  |  |  |  |

获取源表属性字段示例以日志服务（LogService）为例，为您介绍如何获取源表属性字段。目前日志服务支持如下3种属性字段。

| 字段名 | 说明 |
|---|---|
| source | 消息源 |
| topic | 消息主题 |
| timestamp | 数据进入日志服务的时间 |

获取属性字段，除了按照正常逻辑声明外，还需要在类型声明后面加上 `HEADER` 。

**说明**

示例如下： 示例数据

```
__topic__: ens_altar_flow
        result:  {"MsgID":"ems0a","Version":"0.0.1"}
```

实时计算（流计算） 示例语句

```
CREATE TABLE sls_log (
  __topic__  VARCHAR HEADER,
  result     VARCHAR
)WITH(
  type ='sls'
); CREATE TABLE sls_out (
  name     varchar,
  MsgID    varchar,
  Version  varchar
)WITH(
  type ='RDS'
); INSERT INTO sls_out __topic__, JSON_VALUE(result,'$.MsgID'), FROM sls_log
```

测试结果

| name(VARCHAT) | MsgID(VARCHAT) | Version(VARCHAT) |
|---|---|---|
| ensaltarflow _ _ | ems0a | 0.0.1 |

**包含窗口函数的数据源表**

实时计算可以基于Event Time和Processing Time这两种时间属性对数据进行窗口聚合。包含窗口函数的作业中，数据源表的声明中需要使用到Watermark和计算列方法。实时计算基于时间属性的聚合详情，请参见时间属性。

##### 3.5.2.2. 创建数据总线DataHub源表

本文为您介绍如何创建数据总线DataHub源表以及创建过程涉及到的属性字段、WITH参数和类型映射。

**重要**

本文仅适用于Blink 1.4.5及以上版本。

**什么是数据总线**

阿里云流数据处理平台DataHub是流式数据（Streaming Data）的处理平台，提供对流式数据的发布（Publish）、订阅（Subscribe）和分发功能，让您可以轻松构建基于流式数据的分析和应用。实时计算Flink版使用DataHub作为流式数据存储源头或输出目的端。

**语法示例**

DataHub可以作为实时计算Flink版的数据输入，示例如下。

```
CREATE TABLE datahub_stream(
  name VARCHAR,
  age BIGINT,
  birthday BIGINT
) WITH (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
  project='<yourProjectName>',
  topic='<yourTopic>',
  accessId='<yourAccessID>',
  accessKey='<yourAccessSecret>',
  startTime='2017-07-21 00:00:00'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为 datahub 。 |
| endPoint | 消费端点信息 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| project | 读取的项目 | 是 | 无 |
| topic | Project下的具体的Topic名称 | 是 | 无重要目前只支持Tuple模式的Topic。 |
| startTime | 启动位点的时间 | 否 | 批处理时必填，格式为 yyyy-MM-dd hh:mm:ss 。 |
| endTime | DataHub日志结束时间 | 否 | 批处理时必填，格式为 yyyy-MM-dd hh:mm:ss 。 |
| maxRetryTimes | 读取最大重试次数 | 否 | 不同版本中，该参数的默认值如下： Blink 2.2.7以下版本：3 Blink 2.2.7及以上版本：20 |

实时计算（流计算）

| retryIntervalMs | 重试间隔 | 否 | 不同版本中，该参数的默认值如下（单位为毫秒）： Blink 2.2.7以下版本：1000 Blink 2.2.7及以上版本：50 |
|---|---|---|---|
| batchReadSize | 单次读取条数 | 否 | 默认值为10，可设置的最大值为1000。 |
| lengthCheck | 单行字段条数检查策略 | 否 | NONE（默认值）： 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过这行数据。 SKIP：解析出的字段数和定义字段数不同时跳过这行数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 说明解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，按从左到右的顺序，在行尾用Null填充缺少的字段。 |
| columnErrorDebug | 是否开启调试功能 | 否 | false（默认值）：关闭调试功能。 true：开启调试功能，将打印解析异常的日志。 |
| isBlob | DataHub是否为BLOB类型 | 否 | 默认值为false。 重要仅Blink 3.4.x 及以上版本支持该参数。 使用BLOB类型时，字段需要声明为VARBINARY类型，与METAQ类似。 |

**类型映射**

DataHub和实时计算Flink版字段类型对应关系如下，建议使用该对应关系时进行DDL声明。

| DataHub字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BIGINT | BIGINT |
| TIMESTAMP |  |
| STRING | VARCHAR |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |

**属性字段**

Flink SQL支持获取DataHub的属性字段。通过读取属性字段可以获得每条信息输入DataHub的系统时间（System Time）。

| 字段名 | 说明 |
|---|---|
| timestamp | 每条记录写入DataHub的系统时间（System Time） |

**示例代码**

包含DataHub源表的实时计算Flink版作业代码示例如下。 实时计算（流计算）

```
create table datahub_input(
  name VARCHAR
) with (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
  project='test1',
  topic='topic1',
  accessId='<yourAccessID>',
  accessKey='<yourAccessSecret>',
  startTime='2018-06-01 00:00:00'
); create table test_out(
 name  VARCHAR
) with (
  type='print'
); INSERT INTO test_out from datahub_input;
```

**常见问题**

Q：DataHub和实时计算Flink版中的TIMESTAMP的精确级别不同，如何进行转换？ A：DataHub的TIMESTAMP是精确到微秒，在Unix时间戳里是16位，但实时计算Flink版定义的TIMESTAMP是精确到毫秒，在Unix时间戳里是13位，所以建议您使用 BIGINT映射。如果您需要使用TIMESTAMP，建议使用计算列进行转换，详情请参见计算列，代码示例如下。

```
CREATE TABLE datahub_test (
  id                 VARCHAR,
  `type`             VARCHAR,
  `value`            DOUBLE,
  `time`             BIGINT,
   ts as TO_TIMESTAMP(`time`/1000),
) WITH (
  type = 'datahub'
);
```

Q：分裂或者缩容DataHub Topic后导致实时计算Flink版作业失败，如何恢复？ A：Blink 2.2.0以下版本不支持DataHub Shard扩容和缩容功能，如果分裂或者缩容了某个实时计算正在读取的Topic，会导致任务持续出错，无法自行恢复。该情况下需要重新启动（停止->启动）来使任务恢复正常。 Q：可以删除正在使用的DataHub Topic吗？ A：所有版本均不支持删除或重建正在引用的DataHub Topic。

##### 3.5.2.3. 创建消息队列Kafka源表

本文为您介绍如何创建实时计算Flink版消息队列Kafka源表、Kafka版本对应关系及Kafka消息解析示例。

**重要**

本文仅适用于Blink 2.0及以上版本。 本文仅适用于独享模式。 Kafka源表支持读取自建Kafka集群，但需要注意版本对应关系，以及自建集群和实时计算Flink版集群的网络环境配置。

**什么是Kafka源表**

消息队列Kafka版是阿里云提供的分布式、高吞吐、可扩展的消息队列服务。消息队列Kafka版广泛用于日志收集、监控数据聚合、流式数据处理、在线和离线分析等大数据领域。实时计算Flink版支持将 Kafka作为流式数据的数据源表或结果表。 从Kafka输出的数据为序列化后的VARBINARY（二进制）格式。对于输出的每条数据，需要您编写自定义表值函数（UDTF）将其解析为序列化前的数据结构。Kafka源表数据解析流程通常为：Kafka Source Table -> UDTF -> Realtime Compute for Apache Flink -> Sink。此外，Flink SQL中也支持通过CAST函数将VARBINARY解析为

**DDL定义**

Kafka源表定义DDL部分必须与以下SQL完全一致，可以更改WITH参数中的设置。 `create table kafka_stream( --`必须和`Kafka`源表中的5个字段的顺序和类型保持一致。

```
  messageKey VARBINARY,
  `message`    VARBINARY,
  topic      VARCHAR,
  `partition`  INT,
  `offset`     BIGINT
) with (
  type ='kafka010',
  topic = '<yourTopicName>',
  `group.id` = '<yourGroupId>',
  ...
);
```

**WITH参数**

通用配置

| 参数 | 注释说明 | 是否必选 | 备注 |
|---|---|---|---|

实时计算（流计算）

| type | Kafka对应版本 | 是 | Kafka版本需要是Kafka08、Kafka09、Kafka010或Kafka011。版本对应关系请参见Kafka版本对应关系。 |  |  |
|---|---|---|---|---|---|
| topic | 读取的单个topic | 是 | 无 |  |  |
| topicPattern | 读取一批topic的表达式 | 否 | Topic用竖线（\|）分割。例如， topic1\|topic2\|topic3 。详情请参见Class Pattern。 |  |  |
| startupMode | 启动位点 | 否说明建议手动配置该参数。 | 启动位点取值如下： GROUP _OFFSETS（默认值）：根据Group读取。 EARLIEST：从Kafka最早分区开始读取。 LATEST：从Kafka最新位点开始读取。 TIMESTAMP：从指定的时间点读取。 您可以在WITH参数中指定startTimeMs（时间戳）或startTime参数（按照 yyyy-MM-dd HH:mm:ss 格式）。优先使用startTimeMs，不指定则按实时计算Flink版指定的启动位点时间开始消费。 说明如果没有明文指定，则默认为GROUP _OFFSETS模式。 设置为TIMESTAMP模式时，需要在作业参数中明文指定时区。例如 blink.job.timeZone=Asia/Shanghai 。 GROUP _OFFSETS模式下，GroupID的第一次消费，没有设置偏移（Offset）值，默认从Kafka分区末尾开始读取数据。 仅Kafka010和Kafka011版本支持TIMESTAMP。 |  |  |
|  |  |  |  | yyyy-MM-dd |  |
| partitionDiscoveryI ntervalMS | 定时检查是否有新分区产生 | 否 | Kafka 08版本：系统默认开启该功能。 Kafka 09版本及以上版本：不支持partitionDiscoveryIntervalMS参数。您可以通过设置 WITH参数，extraConfig=‘flink.partition-discovery.interval-millis=60000’达到相同的效果。 单位为毫秒，默认值为60000，即1分钟。 |  |  |
| extraConfig | 额外的 KafkaConsumer配置项目 | 否 | 不在可选配置项中，但是期望额外增加的配置。例如： `fetch.message.max.bytes=104857600` ，多个配置使用分号（;）分隔。 |  |  |

|  | HH:mm:ss |
|---|---|

Kafka08配置 Kafka08必选配置

| 参数 | 注释说明 | 是否必选 |
|---|---|---|
| group.id | 消费组ID | 是 |
| zookeeper.connect | zk链接地址 | 是 |

可选配置Key consumer.id socket.timeout.ms fetch.message.max.bytes num.consumer.fetchers auto.commit.enable auto.commit.interval.ms rebalance.max.retries fetch.min.bytes fetch.wait.max.ms rebalance.backoff.ms refresh.leader.backoff.ms auto.offset.reset consumer.timeout.ms exclude.internal.topics partition.assignment.strategy client.id zookeeper.session.timeout.ms zookeeper.connection.timeout.ms zookeeper.sync.time.ms offsets.storage offsets.channel.backoff.ms offsets.channel.socket.timeout.ms offsets.commit.max.retries dual.commit.enabled partition.assignment.strategy socket.receive.buffer.bytes fetch.min.bytes Kafka09/Kafka010/Kafka011配置实时计算（流计算） Kafka09/Kafka010/Kafka011必选配置

| 参数 | 注释说明 |
|---|---|
| group.id | 消费组ID |
| bootstrap.servers | Kafka集群地址 |

Kafka09/Kafka010/Kafka011可选配置，请参见如下Kafka官方文档进行配置： Kafka09 Kafka010 Kafka011

| 加 | `security.protocol` | 、 | `sasl.mechanism` | 和 | `sasl.jaas.config` 3 | 个参数，示例如下。 |
|---|---|---|---|---|---|---|
| create table kafka_stream( messageKey varbinary, `message` varbinary, topic varchar, `partition` int, `offset` bigint ) with ( type ='kafka010', topic = '<yourTopicName>', `group.id` = '<yourGroupId>', ..., `security.protocol`='SASL_PLAINTEXT', `sasl.mechanism`='PLAIN', `sasl.jaas.config`='org.apache.kafka.common.security.plain.PlainLoginModule required username="<yourUserName>" password=" <yourPassword>";' ); |  |  |  |  |  |  |

**Kafka版本对应关系**

| type | Kafka版本 |
|---|---|
| Kafka08 | 0.8.22 |
| Kafka09 | 0.9.0.1 |
| Kafka010 | 0.10.2.1 |
| Kafka011 | 0.11.0.2及以上 |

**Kafka消息解析示例**

场景1：将Kafka中的数据进行计算，并将计算结果输出到RDS。 Kafka中保存了JSON格式数据，需要使用实时计算Flink版进行计算，消息格式示例如下。

```json
{
  "name":"Alice",
  "age":13,
  "grade":"A"
}
```

方法1：Kafka SOURCE->Realtime Compute for Apache Flink->RDS SINK Blink 2.2.7及以上版本支持将VARBINARY类型通过CAST函数转换为VARCHAR类型，再通过JSON_VALUE函数对Kafka数据进行解析，示例如下。

```
CREATE TABLE kafka_src (
  messageKey  VARBINARY,
  `message`   VARBINARY,
  topic       VARCHAR,
  `partition` INT,
  `offset`    BIGINT
) WITH (
```

`type = 'kafka010' --`请参见`Kafka`版本对应关系。

```
); CREATE TABLE rds_sink (
  `name`       VARCHAR,
  age         VARCHAR,
  grade       VARCHAR
) WITH(
  type='rds'
); CREATE VIEW input_view AS
  SELECT CAST(`message` as VARCHAR ) as `message`
FROM kafka_src; INSERT INTO rds_sink
  JSON_VALUE(`message`,'$.name'),
  JSON_VALUE(`message`,'$.age'),
FROM input_view;
```

方法2：Kafka Source->UDTF->Realtime Compute for Apache Flink->RDS Sink 实时计算（流计算） 针对不规则数据、复杂JSON数据，需要您自行编写UDTF代码进行解析，示例如下。 SQL `--` 定义解析`Kafka message`的`UDTF`。

```
CREATE FUNCTION kafkaparser AS 'com.alibaba.kafkaUDTF';
```

`--` 定义源表。注意：`Kafka`源表`DDL`字段必须与以下示例完全一致。`WITH`中参数可以修改。

```
CREATE TABLE kafka_src (
  messageKey  VARBINARY,
  `message`   VARBINARY,
  topic       VARCHAR,
  `partition` INT,
  `offset`    BIGINT
) WITH (
```

`type = 'kafka010', --`请参见`Kafka`版本对应关系。

```
  topic = 'test_kafka_topic',
  `group.id` = 'test_kafka_consumer_group',
  bootstrap.servers = 'ip1:port1,ip2:port2,ip3:port3'
); CREATE TABLE rds_sink (
  name       VARCHAR,
  age        INT,
  grade      VARCHAR,
  updateTime TIMESTAMP
) WITH(
  type='rds',
  url='jdbc:mysql://localhost:3306/test',
  tableName='test4',
  userName='test',
  password='<yourDatabasePassword>'
);
```

`--` 使用`UDTF`，将二进制数据解析成格式化数据。

```
CREATE VIEW input_view (
  name,
  age,
  grade,
  updateTime
) AS
  T.name,
  T.age,
  T.grade,
  T.updateTime
FROM
  kafka_src as S,
  LATERAL TABLE (kafkaparser (`message`)) as T (
  name,
  age,
  grade,
  updateTime
);
```

`--` 使用解析出的格式化数据进行计算，并将结果输出到`RDS`。

```
INSERT INTO rds_sink
  name,
  age,
  grade,
  updateTime
FROM input_view;
```

UDTF UDTF创建步骤请参见自定义表值函数（UDTF）。Blink 2.2.4版本Maven依赖，示例如下。 实时计算（流计算）

```java
    <dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.11</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table_2.11</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.9</version>
        </dependency>
    </dependencies>
package com.alibaba; import com.alibaba.fastjson.JSONObject; import org.apache.flink.table.functions.TableFunction; import org.apache.flink.table.types.DataType; import org.apache.flink.table.types.DataTypes; import org.apache.flink.types.Row; import java.io.UnsupportedEncodingException; import java.sql.Timestamp; public class kafkaUDTF extends TableFunction<Row> {
    public void eval(byte[] message) {
        try {
            /* input message :
                {
                  "name":"Alice",
                  "age":13,
                  "grade":"A",
                  "updateTime":1544173862
                }
```

`*/`

```java
            String msg = new String(message, "UTF-8");
            try {
                JSONObject data = JSON.parseObject(msg);
                if (data != null) {
                    String name = data.getString("name") == null ? "null" : data.getString("name");
                    Integer age = data.getInteger("age") == null ? 0 : data.getInteger("age");
                    String grade = data.getString("grade") == null ? "null" : data.getString("grade");
                    Timestamp updateTime = data.getTimestamp("updateTime");
                    Row row = new Row(4);
                    row.setField(0, name);
                    row.setField(1, age);
                    row.setField(2, grade);
                    row.setField(3,updateTime );
                    System.out.println("Kafka message str ==>" + row.toString());
                    collect(row);
                }
            } catch (ClassCastException e) {
                System.out.println("Input data format error. Input data " + msg + "is not json string");
            }
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
    @Override
```

`//` 如果返回值是`Row`，重新加载`UDTF`这个方法，并指明系统返回的字段类型。

```
    public DataType getResultType(Object[] arguments, Class[] argTypes) {
        return DataTypes.createRowType(DataTypes.STRING, DataTypes.INT, DataTypes.STRING, DataTypes.TIMESTAMP);
    }
}
```

场景2：从Kafka读取数据，输入实时计算Flink版进行窗口计算。 按照实时计算Flink版目前的设计，滚动或滑动等窗口操作，必须在源表DDL上定义Watermark。Kafka源表比较特殊。如果要以Kafka中message字段中的Event Time 进行窗口操作，需要先从message字段使用UDX解析出Event Time，才能定义Watermark。在Kafka源表场景中，需要使用计算列。例如Kafka中写入数据： `2018-` 11-11 00:00:00|1|Anna|female 。计算流程为：Kafka Source->UDTF->Realtime Compute for Apache Flink->RDS Sink。 实时计算（流计算） 方法1：Kafka SOURCE->Realtime Compute for Apache Flink->RDS SINK Blink 2.2.7及以上版本支持将VARBINARY类型通过CAST函数转换为VARCHAR类型，再通过JSON_VALUE函数对Kafka数据进行解析，示例如下。

```
CREATE TABLE kafka_src (
  messageKey VARBINARY,
  `message` VARBINARY,
  topic VARCHAR,
  `partition` INT,
  `offset` BIGINT,
  ts as to_timestamp(json_value(cast(`message` as VARCHAR ),'$.nodes.time')),
```

`) WITH (type = 'kafka' --`请参见`Kafka`版本对应关系。

```
); CREATE TABLE rds_sink (
  starttime TIMESTAMP ,
  endtime   TIMESTAMP ,
  `message` BIGINT
) WITH (type = 'rds');
  INTO rds_sink
  TUMBLE_START(ts, INTERVAL '1' MINUTE),
  TUMBLE_END(ts, INTERVAL '1' MINUTE),
FROM
  kafka_src
GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE);
```

方法2：Kafka SOURCE->UDTF->Realtime Compute for Apache Flink->RDS SINK 实时计算（流计算） SQL `--` 定义解析`Kafka message`的`UDTF`。

```
CREATE FUNCTION kafkapaser AS 'com.alibaba.kafkaUDTF'; CREATE FUNCTION kafkaUDF AS 'com.alibaba.kafkaUDF';
```

`--` 定义源表，注意：`Kafka`源表`DDL`字段必须与以下示例一模一样。`WITH`中参数可改。

```
create table kafka_src (
  messageKey VARBINARY,
  `message` VARBINARY,
  topic VARCHAR,
  `partition` INT,
  `offset` BIGINT,
```

ctime AS TO_TIMESTAMP(kafkaUDF(`message`)), -- 定义计算列，计算列可理解为占位符，源表中并没有这一列，其中的数据可经过下游计算得出。注意:计算列的类型必须

```
  watermark for `ctime` as withoffset(`ctime`,0) -- 在计算列上定义Watermark。
) WITH (
```

`type = 'kafka010', --` 请参见`Kafka`版本对应关系。

```
  topic = 'test_kafka_topic',
  `group.id` = 'test_kafka_consumer_group',
  bootstrap.servers = 'ip1:port1,ip2:port2,ip3:port3'
); create table rds_sink (
  `name` VARCHAR,
  age INT,
  grade VARCHAR,
  updateTime TIMESTAMP
) WITH(
  type='rds',
  url='jdbc:mysql://localhost:3306/test',
  tableName='test4',
  userName='test',
  password='<yourPassword>'
);
```

`--` 使用`UDTF`，将二进制数据解析成格式化数据。

```
CREATE VIEW input_view AS
  S.ctime,
  T.`order`,
  T.`name`,
  T.sex
  from
  kafka_src as S,
  LATERAL TABLE (kafkapaser (`message`)) as T (
  ctime,
  `order`,
  `name`,
  sex
);
```

`--` 对`input_view`中输出的数据做计算。

```
CREATE VIEW view2 (
  cnt,
  sex
) AS
  COUNT(*) as cnt,
  T.sex
  from
  input_view
Group BY sex, TUMBLE(ctime, INTERVAL '1' MINUTE);
```

`--` 使用解析出的格式化数据进行计算，并将结果输出到`RDS`。

```
insert into rds_sink
  cnt,sex
from view2;
```

UDF&UDTF UDF和UDTF创建步骤请参见自定义标量函数（UDF）和自定义表值函数（UDTF）。Blink 2.2.4版本Maven依赖，示例如下。 实时计算（流计算）

```xml
  <dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.11</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table_2.11</artifactId>
            <version>blink-2.2.4-SNAPSHOT</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.9</version>
        </dependency>
    </dependencies>
```

UDTF

```java
package com.alibaba; import com.alibaba.fastjson.JSONObject; import org.apache.flink.table.functions.TableFunction; import org.apache.flink.table.types.DataType; import org.apache.flink.table.types.DataTypes; import org.apache.flink.types.Row; import java.io.UnsupportedEncodingException; /**
```

以下例子解析输入`Kafka`中的`JSON`字符串，并将其格式化输出。

```java
**/
public class kafkaUDTF extends TableFunction<Row> {
    public void eval(byte[] message) {
        try {
```

`//` 读入一个二进制数据，并将其转换为`String`格式。

```
            String msg = new String(message, "UTF-8");
```

`//` 提取`JSON Object`中各字段。

```
                    String ctime = Timestamp.valueOf(data.split('\\|')[0]);
                    String order = data.split('\\|')[1];
                    String name = data.split('\\|')[2];
                    String sex = data.split('\\|')[3];
```

`//` 将解析出的字段放到要输出的`Row()`对象。

```java
                    Row row = new Row(4);
                    row.setField(0, ctime);
                    row.setField(1, age);
                    row.setField(2, grade);
                    row.setField(3, updateTime);
                    System.out.println("Kafka message str ==>" + row.toString());
```

`//` 输出一行。

```java
                    collect(row);
            } catch (ClassCastException e) {
                System.out.println("Input data format error. Input data " + msg + "is not json string");
            }
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
    @Override
```

`//` 如果返回值是`Row`，重新加载`UDTF`这个方法，并指明系统返回的字段类型。 `//` 定义输出`Row()`对象的字段类型。

```
    public DataType getResultType(Object[] arguments, Class[] argTypes) {
        return DataTypes.createRowType(DataTypes.TIMESTAMP,DataTypes.STRING, DataTypes.Integer, DataTypes.STRING,DataTypes.STRING);
    }
}
```

实时计算（流计算） UDF

```java
package com.alibaba; package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.ScalarFunction; public class KafkaUDF extends ScalarFunction {
```

`//` 可选，`open`方法可以不写。

```
    // 需要import org.apache.flink.table.functions.FunctionContext;
    public String eval(byte[] message) {
```

`//` 读入一个二进制数据，并将其转换为`String`格式。

```
        String msg = new String(message, "UTF-8");
        return msg.split('\\|')[0];
    }
    public long eval(String b, String c) {
        return eval(b) + eval(c);
    }
```

`//`可选，`close`方法可以不写。

```java
    @Override
    public void close() {
        }
}
```

**自建Kafka**

示例

```
create table kafka_stream(
  messageKey VARBINARY,
  `message` VARBINARY,
  topic varchar,
  `partition` int,
  `offset` bigint
) with (
  type ='kafka011',
  topic = 'kafka_01',
  `group.id` = 'CID_blink',
  bootstrap.servers = '192.168.0.251:****'
);
```

WITH参数详情请参见WITH参数。

**说明**

**bootstrap.servers**参数需要填写自建的地址和端口号。
仅在Blink 2.2.6及以上版本支持阿里云Kafka或自建Kafka显示TPS和RPS等指标信息。

**常见问题**

Q：作业启动时产生如下报错，应该如何处理？

```
ERR_ID:
     SQL-00010007
CAUSE:
     Could not create table 'kafka_source' as source table
ACTION:
     Please refer to details section for hint.
     If it doesn't help, please contact customer support
DETAIL:
     java.lang.IllegalArgumentException: Startup time[1566481803000] must be before current time[1566453003356].
```

A：时区设置错误导致以上报错。请在作业参数中增加如下参数。

```
blink.job.timeZone=Asia/Shanghai
```

Q：自建Kafka消费不到数据，应该如何排查？ A： 问题原因 Kafka各**broker**会向**zookeeper**汇报自身Meta信息，Kafka **consumer**最终会根据**broker** Meta信息**listener_security_protocol**中的**Endpoint**地址（例如 IP或本机域名加端口）访问**broker**拉取数据。如果实时计算Flink版作业所在机器无法访问**Endpoint**地址，则**connector**中**consumer**将无法拉取数据，导致流程的停滞。 实时计算（流计算） 排查思路 a. 查看**zookeeper > broker > listener_security_protocol > Endpoint**信息。 b. 通过**网络探测**功能检测**Endpoint**的IP或域名是否可访问。 c. 登录机器再次确认。 解决方案如果**Endpoint**采用的是IP形式，则确认Kafka服务端是否配置了白名单。如果未配置，请配置后重试。 如果**Endpoint**采用的是域名形式，由于实时计算Flink版独享集群内部无法解析域名，所以需要在白名单已配置的情况下，通过以下两种解方案解决： 不能重启Kafka服务购买云解析PrivateZone，配置所有Kafka Broker的域名解析，通过域名进行网络探测成功后，重启实时计算Flink版作业。 可以重启Kafka服务将Kafka的**advertised.listeners**属性配置为相应Broker的IP和端口（通常为**boostrap.servers**中IP和Port），以保证网络畅通，然后重启实时计算Flink版作业。 Q：消费Kafka时，为什么作业一启动后马上就结束了？ A：Blink 3.3.0以下版本的Kafka Connector，使用**timestamp**模式时。如果设置启动位点后，Kafka的所有partition均没数据，则Connector会判定没有partition消费而结束作业。通常对应的 `TaskManager.log` 日志中会存在类似 `Consumer subtask {} initially has no partitions to read from.` 的日志信息。建议升级至 Blink 3.3.0及以上版本。 Q：实时计算Flink版中的COMMIT OFFSET有什么作用？ A：实时计算Flink版默认采用**commitOffsetOnCheckpointing**，用户设置的Commit Offset策略不生效。只有开启**checkpoint**后，在每次checkpoint成功时，才会**commit**当前分区消费的**offset**至Kafka，以便在作业失败恢复过程中，从上一次**checkpoint**的**commit**位点开始消费，保证计算的Exactly Once。如果将**checkpoint**间隔设置过大，Kafka端可能会查询不到当前消费**offset**。

##### 3.5.2.4. 创建Oracle数据库源表

本文为您介绍如何创建Oracle数据库源表，以及创建源表时使用的WITH参数、类型映射、代码示例和常见问题。

**重要**

本文仅适用于Blink 3.4.x及以上版本。 请不要手动修改Oracle Source节点的并发数量，默认一个Table对应一个并发。

**语法示例**

实时计算Flink版支持使用Oracle数据库作为源表，代码示例如下。

```
create table oracle_source (
    EMPLOYEE_ID BIGINT,
    START_DATE TIMESTAMP,
    END_DATE TIMESTAMP,
    JOB_ID VARCHAR,
    DEPARTMENT_ID VARCHAR
) with (
    type = 'oracle',
    url = 'jdbc:oracle:thin:@//127.0.0.1:1521/ORACLE',
    userName = 'userName',
    password = 'password',
    dbName = 'hr',
    tableName = 'job_history',
    timeField = 'START_DATE',
    startTime = '2007-1-1 00:00:00'
);
```

**WITH 参数**

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为oracle。 |
| url | 数据库连接串 | 是 | 请联系阿里云运维工程师获取。 |
| userName | 登录数据库的用户名 | 是 | 无 |
| password | 登录数据库的密码 | 是 | 无 |
| tableName | 数据库的表名。数据库的表名有以下两种表达方式： 表名1,表名2 数据库名.表名1,表名2 说明多个表名之间用英文逗号（,）隔开。 | 是 | table1,table2 db1.table1,table2 |
| timeField | 更新数据库的时间 | 是 | 无 |

实时计算（流计算）

| dbName | 数据库名 | 否 | 如果tableName参数配置了数据库名，则dbName不需要重复配置。 |
|---|---|---|---|
| startTime | 读取数据的开始时间 | 否 | 2019-5-15 00:00:00 |
| timeZone | 数据库时区 | 否 | Asia/Shanghai", "UTC |
| queryTimeRangeMs | 获取数据的时长，单位为毫秒。 说明 queryTimeRangeMs参数的取值需要大于queryIntervalMs参数。 | 否 | 默认值为5000。 |
| queryIntervalMs | 查询数据库的时间间隔，单位为毫秒。 | 否 | 默认值为100。 |
| connectionMaxActi ve | 最大活跃连接数 | 否 | 默认值为10。 |
| maxRetry | 最大连接失败重试次数 | 否 | 默认值为3。 |
| escapeFields | 是否对数据库字段名进行转义。 | 否 | escapeFields参数的取值如下： false（默认值），不区分大小写。 true，区分大小写。 |
| lengthCheck | 单行字段条数的检查策略 | 否 | lengthCheck参数的取值如下： NONE（默认值）： 当解析的字段个数大于定义个数时，按从左到右的顺序，取定义字段的数据使用。 当解析的字段个数小于定义个数时，跳过当前行数据。 SKIP：当解析的字段个数和定义个数不同时，跳过当前行数据。 EXCEPTION：当解析的字段个数和定义个数不同时，系统提示异常。 PAD： 当解析的字段个数大于定义个数时，按从左到右的顺序，取定义字段的数据使用。 当解析的字段个数小于定义个数时，按从左到右顺序，在行尾用null填充缺少的字段。 |
| columnErrorDebug | 是否打开调试开关。 说明如果打开调试开关，则会将解析异常的日志打印出来。 | 否 | 默认值为false。 |

**类型映射**

| Oracle字段类型 | 实时计算Flink版字段类型 |
|---|---|
| CHAR VARCHAR VARCHAR2 | VARCHAR |
| FLOAT | DOUBLE |
| NUMBER | BIGINT |
| DECIMAL | DECIMAL |

**代码示例**

实时计算Flink版包含Oracle数据库源表的代码示例如下。 实时计算（流计算）

```
create table oracle_source (
    EMPLOYEE_ID BIGINT,
    START_DATE TIMESTAMP,
    END_DATE TIMESTAMP,
    JOB_ID VARCHAR,
    DEPARTMENT_ID VARCHAR
) with (
    type = 'oracle',
    url = 'jdbc:oracle:thin:@//127.0.0.1:1521/ORACLE',
    userName = 'userName',
    password = 'password',
    dbName = 'hr',
    tableName = 'job_history',
    timeField = 'START_DATE',
    startTime = '2007-1-1 00:00:00'
); create table test_out(
    EMPLOYEE_ID BIGINT,
    START_DATE TIMESTAMP,
    END_DATE TIMESTAMP,
    JOB_ID VARCHAR,
    DEPARTMENT_ID VARCHAR
) with (
    type='print'
); INSERT INTO test_out
    EMPLOYEE_ID,
    START_DATE,
    END_DATE,
    JOB_ID,
    DEPARTMENT_ID
from oracle_source;
```

**常见问题**

Q：查询不到数据该如何处理？ A：查询不到数据是因为Blink运行故障。您需要查看TaskManager的 `Round start:[{}], end:[{}]` 和 `Round read records` 日志，如果未查询到日志数据，则Blink 运行故障。

**说明**

##### 3.5.2.5. 创建日志服务SLS源表

本文为您介绍如何创建日志服务SLS源表，以及创建过程涉及到的属性字段、WITH参数和类型映射。

**重要**

本文仅适用于Blink 1.4.5及以上版本。

**什么是日志服务**

日志服务SLS是针对日志类数据的一站式服务，对于日志服务而言，数据格式类似JSON，示例如下。

```json
{
    "a": 1000,
    "b": 1234,
    "c": "li"
}
```

日志服务本身是流数据存储，实时计算Flink版能将其作为流式数据的输入。

**语法示例**

| 实时计算Flink版日志服务源表DDL示例如下（代码中的 | sls | 代表日志服务）。 |
|---|---|---|
| create table sls_stream( a INT, b INT, c VARCHAR ) with ( type ='sls', endPoint ='http://cn-hangzhou-share.log.aliyuncs.com', accessId ='<yourAccessId>', accessKey ='<yourAccessKey>', startTime = '2017-07-05 00:00:00', project ='<yourProjectName>', logStore ='<yourLogStoreName>', consumerGroup ='<yourConsumerGroupName>' ); |  |  |

**WITH参数**

实时计算（流计算）

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为sls。 |
| endPoint | 消费端点信息 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| project | 读取的SLS项目名称 | 是 | 无 |
| logStore | Project下的具体的LogStore名称 | 是 | 无 |
| startTime | 日志消费的开始时间 | 否 | 无 |
| consumerGroup | 消费组名 | 否 | 您可以自定义消费组名（没有固定格式）。 |
| heartBeatIntervalMills | 消费客户端心跳间隔时间 | 否 | 默认值为10000，单位为毫秒。 |
| maxRetryTimes | 读取最大尝试次数 | 否 | 默认值为5。 |
| batchGetSize | 单次读取logGroup的条数 | 否 | 默认值为100。 |
| columnErrorDebug | 是否打开调试开关 | 否 | 默认值为false，不打开。如果选择打开，则打印解析异常的日志。 |
| startupMode | 启动消费模式 | 否 | 取值如下： TIMESTAMP（默认值）：每个Shard从指定时间开始消费。 Earliest：每个Shard从最早位置开始消费。 Latest：每个Shard从最新位置开始消费。 Group _Offsets：每个Shard优先从服务端保存的Checkpoint开始消费，必须指定consumerGroup。消费模式有以下几种情况： 如果从Flink State中恢复状态成功，则从Flink状态中的Checkpoint开始消费。 如果从Flink State中恢复状态失败： 如果consumerGroup中存在Checkpoint，则尝试从consumerGroup 的Checkpoint开始消费。 如果consumerGroup中不存在Checkpoint： 指定了startTime：从startTime开始消费。 未指定startTime：每个shard从最早位置开始消费。 重要仅Blink 3.6.5及以上版本支持该参数。 仅当state中不存在Checkpoint时，上述配置才有效。 |

**说明**

实时计算Flink版1.6.0及以下版本，在指定consumerGroup的Shards数目时，可能会影响读取性能，该缺陷正在修复。 SLS暂不支持MAP类型的数据。 SLS对于不存在字段会置为Null。 字段顺序支持无序（建议字段顺序和表中定义一致）。 输入数据源为JSON形式时，注意定义分隔符，并且需要采用内置函数JSON_VALUE分析，否则就会解析失败，报错如下。

```
2017-12-25 15:24:43,467 WARN [Topology-0 (1/1)] com.alibaba.blink.streaming.connectors.common.source.parse.DefaultSourceCollector - Field missing error, table column number: 3, data column number: 3, data filed number: 1, data: [{"lg_order_code":"LP00000005","activity_code":"TEST_CODE1","occur_time":"2017-12-10 00:00:01"}]
```

**batchGetSize**设置不能超过1000，否则会报错。
**batchGetSize**指明的是logGroup获取的数量。如果单条logItem的大小和**batchGetSize**都很大，有可能会导致频繁的垃圾回收（Garbage Collection），
这种情况下该参数应调小。

**类型映射**

日志服务和实时计算Flink版字段类型对应关系如下。建议您使用该对应关系进行DDL声明。

| 日志服务字段类型 | 实时计算Flink版字段类型 |
|---|---|
| STRING | VARCHAR |

**属性字段**

目前Flink SQL默认支持3个SLS属性字段的获取，也支持其它自定义字段的写入。

| 字段名 | 注释说明 |
|---|---|
| __source__ | 消息源 |
| __topic__ | 消息主题 |
| __timestamp__ | 日志时间 |

**代码示例**

实时计算（流计算）

```
create table sls_input(
  a int,
  b int,
  c varchar
) with (
  type ='sls',
  endPoint ='http://cn-hangzhou-share.log.aliyuncs.com',
  accessId ='<yourAccessI>',
  accessKey ='<yourAccessKey>',
  startTime = '2017-07-05 00:00:00',
  project ='ali-cloud-streamtest',
  logStore ='stream-test',
  consumerGroup ='consumerGroupTest1'
); create table print_output(
 a int,
 b int,
 c varchar
) with (
  type='print'
); INSERT INTO print_output
  a, b, c
from sls_input;
```

**常见问题**

Q：为什么Job的整体延迟增加，或有窗口聚合的Job无输出？ A：如果一个Partition没有新数据写入，会导致上述情况，只需要把并发数调整为读写的Partition数量即可。 Q：如何设置并发数？ A：并发数建议等于Partition数量，否则当两个Partition读取速度差异较大时，理论上在追数据场景，存在数据被过滤掉和数据延迟的风险。 Q：Flink Job延迟增大应该如何排查？ A：SLS源表可能会发生Shard分裂，分裂后的Shard index会不连续，导致Flink延迟增大。如果发现Flink Job延迟增大，请查看SLS源是否发生分裂。

##### 3.5.2.6. 创建全量MaxCompute源表

本文为您介绍如何创建全量MaxCompute源表，以及创建源表时使用的WITH参数和类型映射。

**重要**

本文仅适用于Blink 2.2.7及以上版本。 与数据总线DataHub、Kafka等数据源不同，全量MaxCompute源表通常作为有限流表使用。Blink 3.4.4版本临时支持将全量MaxCompute源表作为无限流表使用，实现不间断监听并读取新增分区的功能。Blink 3.5.0版本废弃该功能，如果您需要使用无限流MaxCompute源表，请参见创建增量MaxCompute源表。

**DDL定义**

实时计算Flink版支持使用全量MaxCompute作为源表输入，示例代码如下。

```
create table odps_source(
    id INT,
    user_name VARCHAR,
    content VARCHAR
) with (
    type = 'odps',
    endPoint = 'http://service.cn.maxcompute.aliyun-inc.com/api',
    project = '<projectName>',
    tableName = '<tableName>',
    accessId = '<yourAccessKeyId>',
    accessKey = '<yourAccessKeySecret>',
```

`partition` = 'ds=2018****' --如果您的`MaxCompute`源表为非分区表，不声明该参数即可。

```
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| endPoint | MaxCompute服务地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoint | MaxCompute Tunnel服务的连接地址 | 否 | 请联系阿里云运维工程师获取。 |
| project | MaxCompute项目名称 | 是 | 无 |
| tableName | MaxCompute表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |

实时计算（流计算）

| partition | 分区名 | 否 | 只存在一个分区的全量MaxCompute表例如，如果只存在1个分区列 ds ，则 `partition` = 'ds=20180905' 表示读 ds=20180905 分区的数据。 存在多个分区的全量MaxCompute表例如，如果存在2个分区列 ds 和 hh ， 则 `partition`='ds=20180905,hh=*' 表示读 ds=20180905 分区的数据。 说明分区过滤时需要声明所有分区的值。例如，上述示例中，只声明 `partition` = 'ds=20180905' ，则不会读取任何分区。 |
|---|---|---|---|
| subscribeNewPartition | 是否监听符合条件的新分区 | 否 | 默认值为false，不监听新产生的分区。 说明 subscribeNewPartition参数值为 true 时，不可以指定 partition的参数值 ，否则会造成无法读取新产生的分区的状况。 该参数只在Blink 3.4.4版本临时存在，Blink 3.5.0版本废弃该参数， 请使用创建增量MaxCompute源表。 |
| subscribeIntervalInSec | 监听新分区的间隔 | 否 | 默认值为30，单位为秒。 说明监听间隔设置太小，会对全量MaxCompute MetaData服务造成压力，有可能导致监听服务失败。 |

|  | 'ds=20180905' |
|---|---|

**类型映射**

| 全量MaxCompute字段类型 | 实时计算Flink版字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |
| STRING | VARCHAR |

**代码示例**

包含全量MaxCompute源表的实时计算Flink版作业代码示例如下。

```
CREATE TABLE odps_source (
    cid varchar,
    rt DOUBLE,
) with (
    type = 'odps',
    endPoint = '<yourEndpointName>',
    project = '<yourProjectName>',
    tableName = '<yourTableName>',
    accessId = '<yourAccessId>',
    accessKey = '<yourAccessPassword>',
    partition = 'ds=20190712'
); CREATE TABLE test (
    cid varchar,
) with (
  type='print'
); INSERT INTO test
    cid,
FROM odps_source GROUP BY cid;
```

##### 3.5.2.7. 创建消息队列MQ源表

实时计算（流计算） 本文为您介绍实时计算如何创建消息队列MQ源表以及创建过程涉及到的CSV类格式、WITH参数和类型映射。

**说明**

如果您需要使用带独立命名空间的MQ，请使用Blink 3.x作业版本。

**什么是消息队列MQ**

消息队列MQ是阿里云专业消息中间件，是企业级互联网架构的核心产品。实时计算可以将消息队列作为流式数据输入。

**示例**

```
create table mq_stream(
  x varchar,
  y varchar,
  z varchar
) with (
  type='mq',
  topic='<yourTopicName>',
  endpoint='<yourEndpoint>',
  pullIntervalMs='1000',
  accessId='<yourAccessId>',
  accessKey='<yourAccessSecret>',
  startMessageOffset='1000',
  consumerGroup='<yourConsumerGroup>',
  fieldDelimiter='|'
);
```

**说明**

MQ实际上是一个非结构化存储格式，对于数据的Schema不提供强制定义，完全由业务层指定。目前实时计算支持类CSV格式文本和二进制格式。

**CSV格式**

假设您的1条CSV格式消息记录如下。

```
1,name,male 2,name,female
```

1条MQ消息可以包括0条到多条数据记录，记录之间使用 \n 分隔。

**说明**

在实时计算作业中，声明MQ数据源表的DDL如下。

```
create table mq_stream(
  id varchar,
  name varchar,
  gender varchar
) with (
  type='mq',
  topic='<yourTopicName>',
  endpoint='<ourEndpoint>',
  pullIntervalMs='1000',
  accessId='<yourAccessId>',
  accessKey='<yourAccessSecret>',
  startMessageOffset='1000',
  consumerGroup='<yourConsumerGroup>',
  fieldDelimiter='|'
);
```

**二进制格式**

二进制格式测试代码如下。

```
create table source_table (
  mess varbinary
) with (
  type = 'mq',
  endpoint = '<yourEndpoint>',
  pullIntervalMs='500',
  accessId='<yourAccessId>',
  accessKey='<yourAccessSecret>',
  topic = '<yourTopicName>',
  consumerGroup='<yourConsumerGroup>'
); create table out_table (
  commodity varchar
) with (
  type='print'
); INSERT INTO out_table
  cast(mess as varchar)
FROM source_table;
```

实时计算（流计算）

**说明**

`cast(mess as varchar)` 需在实时计算2.0及以上版本使用，如果版本低于2.0，请先升级。 VARBINARY只能入参一次。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为mq。 |
| topic | topic名称 | 是 | 无。 |
| endPoint | endPoint地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| consumerGroup | 订阅消费group名称 | 是 | 无 |
| pullIntervalMs | 拉取时间间隔 | 否 | 单位为毫秒。 |
| startTime | 消息消费启动的时间点 | 否 | 无 |
| startMessageOffs et | 消息开始的偏移量 | 否 | 如果填写，将优先以startMessageoffset的位点开始加载。 |
| tag | 订阅的标签 | 否 | 无 |
| lineDelimiter | 解析block时行分隔符 | 否 | 默认值为 \n 。 |
| fieldDelimiter | 字段分隔符 | 否 | 默认值为 \u0001 。表示在只读模式下以 \u0001 （ \u0001 在只读模式不可见）作为分隔符，在编辑模式下以 ^A 作为分隔符。 |
| encoding | 编码格式 | 否 | 默认值为 utf-8 。 |
| lengthCheck | 单行字段条数检查策略 | 否 | 默认值为NONE，表示： 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过这行数据。 其它可选值为SKIP、EXCEPTION和PAD。 SKIP：解析出的字段数和定义字段数不同时跳过这行数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，在行尾用null填充缺少的字段。 |
| columnErrorDebu g | 是否打开调试开关 | 否 | 默认值为FALSE。如果设置为TRUE，则打印解析异常的Log。 |
| instanceID | MQ实例ID | 否 | 如果MQ实例无独立命名空间，则不可以使用instanceID参数。如果MQ实例有独立命名空间， 则instanceID参数必选。 |

**类型映射**

| MQ字段类型 | 实时计算字段类型 |
|---|---|
| STRING | VARCHAR |

##### 3.5.2.8. 创建表格存储Tablestore源表

本文为您介绍如何创建实时计算Flink版表格存储Tablestore源表。

**重要**

本文仅适用于实时计算Flink版3.2.2及以上版本。

**什么是表格存储Tablestore**

表格存储Tablestore是构建在阿里云飞天分布式系统之上的分布式NoSQL数据存储服务。表格存储通过数据分片和负载均衡技术，实现数据规模与访问并发上的无缝扩展， 提供海量结构化数据的存储和实时访问服务。

**表格存储通道服务**

表格存储通道服务是基于表格存储数据接口的全增量一体化服务，通过Tunnel Service API和SDK，为您提供了增量、全量和增量加全量三种类型的分布式数据实时消费通道。通过Tunnel Service数据通道，您可以使用流式计算的方式，消费表中存量或新增数据。实时计算Flink版可以将Tunnel Service数据通道作为流式数据的输入，每条数据类似一个JSON格式。Tunnel Service数据通道的示例如下。 实时计算（流计算）

```
{
```

`"OtsRecordType": "PUT", //` 数据操作类型，包括`PUT`、`UPDATE`和`DELETE`。 `"OtsRecordTimestamp": 1506416585740836, //`数据写入时间（单位为微秒），全量数据时为0。

```json
            "PrimaryKey": [
                {
```

`"ColumnName": "pk_1", //`第1主键列。

```json
                    "Value": 1506416585881590900
                },
                {
```

`"ColumnName": "pk_2", //`第2主键列。

```json
                    "Value": "string_pk_value"
                }
```

`],`

```json
            "Columns": [
                {
                    "OtsColumnType": "PUT", // 列操作类型，包括PUT、DELETE_ONE_VERSION和DELETE_ALL_VERSION。
                    "ColumnName": "attr_0",
                    "Value": "hello_table_store",
                },
                {
                    "OtsColumnType": "DELETE_ONE_VERSION", // DELETE操作没有Value字段。
                    "ColumnName": "attr_1"
                }
```

]

```
}
```

**DDL定义**

实时计算Flink版支持使用Tablestore作为源表，示例代码如下。

```
create table tablestore_stream(
  pk_1 BIGINT,
  pk_2 VARCHAR,
  attr_0 VARCHAR,
  attr_1 DOUBLE,
```

`OtsRecordType VARCHAR HEADER //`属性字段后边需要增加`HEADER`。

```
) with (
  type ='ots',
  endPoint ='http://blink-demo.cn-hangzhou.vpc.tablestore.aliyuncs.com',
  instanceName = 'blink-demo',
  tableName ='demo_table',
  tunnelName = 'blink-demo-stream',
  accessId ='<yourAccessID>',
  accessKey ='<yourAccessSecret>',
```

`ignoreDelete = 'false' //`是否忽略`DELETE`操作的数据。

```
);
```

**属性字段**

| 字段名 | 说明 |
|---|---|
| OtsRecordType | 数据操作类型 |
| OtsRecordTimestamp | 数据操作时间（全量数据时， OtsRecordTimestamp 为0） |
| <列名>_OtsColumnType | 某列的操作类型 |

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | connector类型 | 固定值为 ots 。 |
| endPoint | 表格存储的实例访问地址 | 请联系阿里云运维工程师获取。 |
| instanceName | 表格存储的实例名称 | 无 |
| tableName | 表格存储的数据表名 | 实时计算读取Tablestore源表数据时，已读取的数据不会再被读取，如果您有再次读取全量数据的需求，则需要重新创建新的数据通道。 |
| tunnelName | 表格存储数据表的数据通道名 | 无 |
| accessId | 表格存储读取的AccessKey ID | 无 |
| accessKey | 表格存储读取的密钥AccessKey Secret | 无 |
| ignoreDelete | 是否忽略DELETE操作的数据。 | 可选，默认值为 false 。 |

##### 3.5.2.9. 创建交互式分析Hologres源表

本文为您介绍创建交互式分析Hologres源表DDL定义，以及创建源表时用到的WITH参数、类型映射和代码示例。 实时计算（流计算）

**重要**

建议您使用Hologres 0.7及以上版本。 仅支持行存储Hologres表作为实时计算Flink源表。 Hologres源表支持Projection Pushdown操作，您可以只读取需要的列。 并发的Blink作业都可以读取一个或多个Hologres Shard，建议您配置的Blink并发数小于等于Hologres的Shard数。 在流数据和批数据处理中都可以使用Hologres源表。 Hologres源表使用快照语句高速读取当前数据，读取完后结束作业。如果出现读取数据失败，将重新执行读取操作。

**什么是交互式分析Hologres**

交互式分析Hologres兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析处理PB级数据，让您轻松使用现有BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**DDL定义**

```
create table mysource(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  type='hologres',
  dbname='...',
  tablename='...',
  username='...',
  password='...',
  endpoint='...',
```

`field_delimiter='...' --`该参数可选。

```
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为hologres。 |
| dbname | 数据库名称 | 是 | 无 |
| tablename | 表名称 | 是 | 无 |
| username | 用户名，请填写阿里云账号的AccessKey ID。 | 是 | 无 |
| password | 密码，请填写阿里云账号的AccessKey Secret。 | 是 | 无 |
| endpoint | Hologres端点 | 是 | 请联系阿里云运维工程师获取。 |
| fielddelimiter _ | 导出数据时，不同行之间使用的分隔符。 重要不能在数据中插入分隔符。 | 是 | 默认值为"\u0002"。 |

**类型映射**

| Hologres | BLINK |
|---|---|
| INT | INT |
| INT[] | ARRAY<INT> |
| BIGINT | BIGINT |
| BIGINT[] | ARRAY<BIGINT> |
| REAL | FLOAT |
| REAL[] | ARRAY<FLOAT> |
| DOUBLE PRECISION | DOUBLE |
| DOUBLE PRECISION[] | ARRAY<DOUBLE> |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY<BOOLEAN> |
| TEXT | VARCHAR |
| TEXT[] | ARRAY<VARCHAR> |
| NUMERIC | DECIMAL |
| DATE | DATE |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

**代码示例**

包含Hologres源表的实时计算作业代码示例如下。 实时计算（流计算）

```
create table mysource(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  type='hologres',
  dbname='...',
  tablename='...',
  username='...',
  password='...',
  endpoint='...',
```

`field_delimiter='...' --`该参数可选。

```
); create table print_output(
 a varchar,
 b BIGINT,
 c BIGINT
) with (
  type='print'
); INSERT INTO print_output
  a, b, c
from mysource;
```

##### 3.5.2.10. 创建增量MaxCompute源表

本文为您介绍如何创建增量MaxCompute源表，以及创建维表时使用的WITH参数、类型映射和常见问题。

**重要**

本文仅适用于Blink 3.5.0 hotfix版本。 增量MaxCompute源表不支持作为维表使用。 增量MaxCompute源表只支持MaxCompute分区表，不支持非分区表。

**语法示例**

```
create table odps_source(
    id int,
    user_name VARCHAR,
    content VARCHAR
) with (
    type = 'continuous-odps',
    endPoint = 'your_end_point_name',
    project = 'your_project_name',
    tableName = 'your_table_name',
    accessId = 'your_access_id',
    accessKey = 'your_access_key',
    startPartition = 'ds=20180905'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | connector类型 | 是 | 固定值为 continuous-odps 。 |
| endPoint | MaxCompute服务本身的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoint | MaxCompute Tunnel服务的连接地址 | 是：VPC环境必填否：其他非VPC环境 | 请联系阿里云运维工程师获取。 |
| project | 表所属的project名称 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |

实时计算（流计算）

| startPartition | 指定读取的起始分区。系统加载分区列表时，会把每个分区列表的所有分区和startPartition按照字母顺序进行比较，加载满足条件的分区的数据。 此外，增量MaxCompute源表可以持续监听增量 MaxCompute分区表。读完已有的分区后，任务不会退出， 且持续监听并读入新分区。 说明增量MaxCompute源表中必须存在一级分区， 二级分区可选。 如果指定二级分区，必须写在一级分区的后面。 如果startPartition指定的分区不存在，系统会从下一个分区开始读取数据。 | 是 | 例如，指定startPartition是ds=20191201，表示加载增量MaxCompute表里所有满足ds >= 20191201的分区数据。 如果一个增量MaxCompute分区表，有一级分区ds和二级分区type两个分区列，假设表里有以下5个分区： ds=20191201,type=a ds=20191201,type=b ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c 不同startPartition，满足分区的列表如下： ds=20191202 ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c ds=20191201,type=c ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c |
|---|---|---|---|

**类型映射**

| MaxCompute字段类型 | 实时计算Flink版字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |
| STRING | VARCHAR |

**重要**

增量MaxCompute源表暂不支持CHAR、VARCHAR、ARRAY、MAP和STRUCT数据类型。 您可以临时使用STRING替换VARCHAR。

**代码示例**

增量MaxCompute源表每天产生一个分区，分区列是ds，从**ds=20191201**分区开始，加载后续的所有分区，并一直监听新分区的产生。 `--`读增量`MaxCompute`表，读取的分区范围是`[ds=20191201`，∞)。

```
CREATE TABLE odps_source (
    cid VARCHAR,
    rt DOUBLE,
) with (
    type = 'continuous-odps',
    endPoint = 'your_end_point_name',
    project = 'your_project_name',
    tableName = 'your_table_name',
    accessId = 'xxxx',
    accessKey = 'xxxx',
    startPartition = 'ds=20191201'
); CREATE TABLE test (
    cid VARCHAR,
    rt DOUBLE,
) with (
    type='print'
); INSERT INTO test
    cid, rt FROM odps_source;
```

#### 3.5.3. 创建数据结果表

实时计算（流计算）

**3.5.3.1. 概述**

实时计算使用 `CREATE TABLE` 作为输出结果数据的格式定义，同时定义数据如何写入到目的数据存储。 实时计算结果表有Append类型和Update类型。 Append类型：如果输出存储是日志系统、消息系统、或未定义主键的RDS数据库，数据流的输出结果会以追加的方式写入到存储中，不会修改存储中原有的数据。 Update类型：如果输出存储是声明了主键（primary key）的数据库（例如，RDS和HBase），数据流的输出结果有以下2种情况。 如果根据主键查询的数据在数据库中不存在，则会将该数据插入数据库。 如果根据主键查询的数据在数据库中存在，则会根据主键更新数据。

**结果表语法**

```
CREATE TABLE tableName
    (columnName dataType [, columnName dataType ]*)
    [ WITH (propertyName=propertyValue [, propertyName=propertyValue ]*) ];
```

**结果表示例**

```
CREATE TABLE rds_output( id INT, len INT, content VARCHAR, PRIMARY KEY(id) ) WITH ( type='rds', url='yourDatabaseURL', tableName='yourTableName', userName='yourDatabaseUserName', password='yourDatabasePassword' );
```

##### 3.5.3.2. 创建数据总线DataHub结果表

本文为您介绍如何创建实时计算数据总线DataHub结果表，以及创建结果表时使用的WITH参数和类型映射。 本文仅适用于Blink 1.4.5及以上版本。

**重要**

**什么是数据总线DataHub**

阿里云流数据处理平台DataHub是流式数据（Streaming Data）的处理平台，提供对流式数据的发布（Publish）、订阅（Subscribe）和分发功能，让您可以轻松构建基于流式数据的分析和应用。实时计算Flink版使用DataHub作为流式数据存储源头或输出目的端。

**DDL定义**

实时计算支持使用DataHub作为数据输出结果表，DataHub结果表声明示例如下。

```
create table datahub_output(
  name VARCHAR,
  age BIGINT,
  birthday BIGINT
)with(
  type='datahub',
  endPoint='<yourEndpoint>,
  project='<yourProjectName>',
  topic='<yourTopicName>',
  accessId='<yourAccessId>',
  accessKey='<yourAccessKey>',
  batchSize='<yourBatchSize>',
  batchWriteTimeoutMs='1000'
);
```

**WITH参数**

| 参数 | 参数说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 源表类型 | 是 | 固定值为 datahub 。 |
| endPoint | endPoint地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | DataHub项目名称 | 是 | 无 |
| topic | DataHub中Topic名称 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| maxRetryTimes | 读取最大重试次数 | 否 | 不同版本中，该参数的默认值如下： Blink 2.2.7以下版本：3 Blink 2.2.7及以上版本：20 |
| batchSize | 一次批量写入的条数 | 否 | 不同版本中，该参数的默认值如下： Blink 3.3以下版本：300 Blink 3.3及以上版本：100 |

实时计算（流计算）

| batchWriteTimeoutMs | 缓存数据的超时时间 | 否 | 可选，单位为毫秒，默认值为5000。表示如果缓存中的数据在等待5秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |
|---|---|---|---|
| maxBlockMessages | 每次写入的最大Block数 | 否 | 默认值为100。 |
| reserveMilliSecond | TIMESTAMP类型是否保留毫秒 | 否 | 默认值为false。 重要仅实时计算2.2.6以上版本支持该功能。 |
| partitionBy | 写入结果表前会根据该值进行Hash分类，数据会流向对应的结果表。 | 否 | 默认值为空，随机进行数据分配。 说明 partitionBy决定数据流到Blink的哪个Subtask。 |
| hashFields | 指定了列名之后，相同列的值会写入到同一个Shard。 | 否 | 默认值为Null，即随机写入。可以指明多个列值，用逗号（,）分隔。例如， hashFields='a,b' 。 重要仅Blink 3.3.0及以上版本支持该功能。 hashFields决定数据流写到DataHub的哪个Shard。 |

**类型映射**

DataHub和实时计算字段类型对应关系如下，建议使用该对应关系时进行DDL声明。

| DataHub字段类型 | 实时计算字段类型 |
|---|---|
| BIGINT | BIGINT |
| TIMESTAMP | BIGINT 说明 DataHub的TIMESTAMP精确到微秒，在Unix时间戳中为16位，但实时计算定义的TIMESTAMP精确到毫秒，在Unix时间戳中为13位，所以建议您使用BIGINT进行映射。 如果您需要使用TIMESTAMP，建议使用计算列进行转换，详情请参见计算列。 |
| STRING | VARCHAR |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |

**代码示例**

包含DataHub结果表的实时计算作业代码示例如下。

```
create table datahub_input(
  name VARCHAR
) with (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
  project='test1',
  topic='topic1',
  accessId='<yourAccessID>',
  accessKey='<yourAccessSecret>',
  startTime='2018-06-01 00:00:00'
); create table datahub_output(
  name varchar
)with(
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
  project='test2',
  topic='topic2',
  accessId='<yourAccessID>',
  accessKey='<yourAccessSecret>',
  batchSize='1000',
  batchWriteTimeoutMs='500'
); INSERT INTO datahub_output from datahub_input;
```

##### 3.5.3.3. 创建消息队列MQ结果表

本文为您介绍如何创建实时计算Flink版消息队列MQ结果表，以及创建过程涉及到的WITH参数。

**重要**

本文仅适用于Blink 1.4.5及以上版本。 如果您需要使用带独立命名空间的MQ，请使用Blink 3.x作业版本。 实时计算（流计算）

**什么是消息列队MQ**

消息队列MQ（Message Queue）是阿里云商用的专业消息中间件，是企业级互联网架构的核心产品。消息列队基于高可用分布式集群技术，搭建了包括发布订阅、消息轨迹、资源统计、定时（延时）和监控报警等一套完整的消息云服务。

**CSV格式**

实时计算Flink版可以将消息队列作为流式数据进行输出，CSV格式输出示例如下。

```
CREATE TABLE stream_test_hotline_agent ( id INTEGER, len BIGINT, content VARCHAR ) WITH ( type='mq', endpoint='<yourEndpoint>', accessID='<yourAccessId>', accessKey='<yourAccessSecret>', topic='<yourTopicName>', producerGroup='<yourGroupName>', tag='<yourTagName>', encoding='utf-8', fieldDelimiter=',', retryTimes='5', sleepTimeMs='500' );
```

**二进制格式**

实时计算Flink版可以将消息队列作为流式数据进行输出，二进制格式输出示例如下。

```
CREATE TABLE source_table (
  commodity VARCHAR
)WITH(
  type='random'
); CREATE TABLE result_table (
  mess VARBINARY
) WITH (
  type = 'mq',
  endpoint='<yourEndpoint>',
  accessID='<yourAccessId>',
  accessKey='<yourAccessSecret>',
  topic='<yourTopicName>',
  producerGroup='<yourGroupName>'
); INSERT INTO result_table CAST(SUBSTRING(commodity,0,5) AS VARBINARY) AS mess FROM source_table;
```

`cast(varchar as varbinary)` 需要在Blink 2.0及以上版本使用。如果版本低于2.0，请先完成版本升级。

**说明**

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | 结果表类型 | 固定值为mq。 |
| topic | Message Queue队列名称 | 无 |
| endpoint | 地址 | 请联系阿里云运维工程师获取。 |
| accessID | AccessKey ID | 无 |
| accessKey | AccessKey Secret | 无 |
| producerGroup | 写入的群组 | 无 |
| tag | 写入的标签 | 可选，默认值为空。 |
| fieldDelimiter | 字段分割符 | 可选，默认值为 \u0001 。分隔符的使用情况如下所示： 只读模式：以 \u0001 作为分隔符， \u0001 在只读模式不可见。 编辑模式：以 ^A 作为分隔符。 |
| encoding | 编码类型 | 可选，默认值为 utf-8 。 |
| retryTimes | 写入的重试次数 | 可选，默认值为10。 |
| sleepTimeMs | 重试间隔时间 | 可选，默认值为1000（毫秒）。 |
| instanceID | MQ实例ID | 如果MQ实例无独立命名空间，则不可以使用instanceID参数。 如果MQ实例有独立命名空间，则instanceID参数必选。 |

实时计算（流计算）

##### 3.5.3.4. 创建云数据库RDS版结果表

本文为您介绍如何创建实时计算云数据库（RDS和DRDS）结果表以及云数据库（RDS和DRDS）实时计算字段类型之间的映射关系。

**关系型数据库（RDS）**

阿里云关系型数据库（Relational Database Service，RDS）是一种稳定可靠、可弹性伸缩的在线数据库服务。基于阿里云分布式文件系统和高性能存储，RDS支持 MySQL、SQL Server、PostgreSQL和PPAS（Postgre Plus Advanced Server，一种高度兼容Oracle的数据库）引擎，并且提供了备份、恢复、监控、迁移等方面的全套解决方案。

**说明**

关系型数据库（RDS和DRDS）插件中的**with**参数一致，可以通用。在使用关系型数据库（RDS和DRDS）作为结果表时，RDS和DRDS中必须要有真实的表存在。

**DDL定义**

实时计算支持使用RDS和DRDS作为结果输出（目前仅支持MySQL数据存储类型）。示例代码如下。

```
create table rds_output(
 id int,
 len int,
 content varchar,
 primary key(id,len)
) with (
 type='rds',
 url='<yourDatabaseURL>',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
);
```

实时计算写入RDS和DRDS数据库结果表原理：针对实时计算每行结果数据，拼接成一行SQL向目标端数据库进行执行。如果使用批量写，需要在URL后面加上参数?
**rewriteBatchedStatements=true**，否则性能较差。
云数据库MySQL版支持自增主键。如果需要让实时计算写入数据支持自增主键，在DDL中不声明该自增字段即可。例如，ID是自增字段，实时计算DDL不写出该自增字段，则数据库在一行数据写入过程中会自动填补相关的自增字段。 如果DRDS有分区表，拆分键必须在实时计算DDL里**PRIMARY KEY****（）**中声明，否则拆分的表无法写入。

**WITH参数**

| 参数 | 注释说明 | 备注 |
|---|---|---|
| url | 地址 | 无。 |
| tableName | 表名 | 无。 |
| userName | 用户名 | 无。 |
| password | 密码 | 无。 |
| maxRetryTimes | 最大尝试插入次数 | 可选，默认为3。 |
| batchSize | 每次写的批次大小 | 可选，默认值50，表示每次写多少条。 |
| bufferSize | 去重的buffer大小，需要指定主键才生效 | 可选，默认值为1，（实时计算从1.4.1版本之后，默认值为 1000），表示输入的数据达到1条就开始输出。 |
| flushIntervalMs | 写超时时间 | 可选，单位毫秒，默认值5000，表示数据超过了5秒。如果还没有写过，就会将缓存的数据都写一次。 |
| excludeUpdateColumns | 对相同key的值更新时排除掉相应的column | 可选，默认不指定该参数（PRIMARY KEY字段默认会排除）。 |
| ignoreDelete | 是否忽略delete操作 | 默认为false。 |
| partitionBy | 数据在插入sink节点之前，实时计算会根据该值进行hash， 然后数据就会被插入到相应的hash节点。 | 可选，默认不指定该参数。 |

**类型映射**

| RDS字段类型 | 实时计算字段类型 |
|---|---|
| TEXT | VARCHAR |
| BYTE | VARCHAR |
| INTGER | INT |
| LONG | BIGINT |
| DOUBLE | DOUBLE |
| DATE | VARCHAR |
| DATETIME | VARCHAR |
| TIMESTAMP | VARCHAR |
| TIME | VARCHAR |
| YEAR | VARCHAR |

实时计算（流计算）

| FLOAT | FLOAT |
|---|---|
| DECIMAL | DECIMAL |
| CHAR | VARCHAR |

**JDBC 连接参数**

| 参数名称 | 参数说明 | 缺省值 | 云数据库RDS SQL Server的最低版本要求 |
|---|---|---|---|
| useUnicode | 是否使用Unicode字符集，如果参数characterEncoding设置为gb2312或gbk，本参数值必须设置为 true。 | false | 1.1g |
| characterEncoding | 当useUnicode设置为true时，指定字符编码。例如可设置为gb2312或gbk。 | false | 1.1g |
| autoReconnect | 当数据库连接异常中断时，是否自动重新连接。 | false | 1.1 |
| autoReconnectForPools | 是否使用针对数据库连接池的重连策略。 | false | 3.1.3 |
| failOverReadOnly | 自动重连成功后，主机是否启用只读模式。 | true | 3.0.12 |
| maxReconnects | autoReconnect设置为true时，重试连接的次数。 | 3 | 1.1 |
| initialTimeout | autoReconnect设置为true时，两次重连之间的时间间隔，单位：秒。 | 2 | 1.1 |
| connectTimeout | 和数据库服务器建立socket连接时的超时， 单位：毫秒。0表示永不超时，适用于JDK 1.4及更高版本。 | 0 | 3.0.1 |
| socketTimeout | socket操作（读写）超时，单位：毫秒。 0 表示永不超时。 | 0 | 3.0.1 |

**FAQ**

Q：实时计算的结果数据写入RDS表，是按主键更新，还是新生成一条记录？

```
A：如果在DDL中定义了主键，会采用 INSERT INTO tablename(field1,field2, field3, ...) VALUES(value1, value2, value3, ...) ON DUPLICATE KEY UPDATE
```

field1=value1,field2=value2, field3=value3, ...; 的方式更新记录，即对于不存在的主键字段会直接插入，存在的主键字段则更新相应的值。如果DDL中没有声明 PRIMARY KEY，则会用 `insert into` 方式插入记录，追加数据。 Q：使用RDS表中的唯一索引进行GROUP BY需要注意什么？ A：如果RDS结果表中有自增主键，实时计算作业的DDL中不能将这个自增主键字段声明为PRIMARY KEY。如果需要使用RDS表中的唯一索引进行GROUP BY，需要在实

##### 3.5.3.5. 创建时序数据库结果表

本文为您介绍如何创建实时计算Flink版时序数据库（TSDB）结果表以及创建结果表时使用的WITH参数。 本文仅适用于Blink 2.0及以上版本。

**重要**

**什么是时间序列数据库（TSDB）**

阿里云时序数据库（Time Series Database，简称TSDB）是一种集时序数据高效读写、压缩存储、实时计算能力为一体的数据库服务，可以广泛应用于物联网和互联网领域，实现对设备及业务服务的实时监控，实时预测告警。

**DDL定义**

实时计算Flink版支持使用TSDB作为结果输出，示例代码如下。

```
CREATE TABLE stream_test_hitsdb (
    metric      VARCHAR,
    `timestamp` INTEGER,
    `value`     DOUBLE,
    tagk1       VARCHAR,
    tagk2       VARCHAR,
    tagk3       VARCHAR
) WITH (
    type='hitsdb',
    host='<yourHostName>',
    virtualDomainSwitch = 'false',
    httpConnectionPool = '20',
    batchPutSize = '1000'
);
```

建表默认格式： 第0列：metric（VARCHAR）。 第1列：timestamp（INTEGER），单位为秒。 第2列：value（DOUBLE）。 第3~N列：TagKey，即时间序列数据库中的fieldName。 实时计算（流计算）

**说明**

**tag**可以为多列。
必须声明**metric**、**timestamp**和**value**，且字段名称、字段顺序和字段数据类型必须和TSDB保持完全一致。

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | 结果表类型 | 固定值为 hitsdb 。 |
| host | IP或VIP域名 | 连接实例。填写注册实例的Host。 |
| port | 端口 | 默认值为8242。 |
| virtualDomainSwitch | 是否使用VIPServer | 默认值为false，如果需要使用VIPServer，则virtualDomainSwitch设置为true。 |
| httpConnectionPool | HTTP连接池 | 默认值为10。 |
| httpCompress | 使用GZIP压缩 | 默认值为false，即不压缩。 |
| httpConnectTimeout | HTTP连接超时时间 | 默认值为0。 |
| ioThreadCount | IO线程数 | 默认值为1。 |
| batchPutBufferSize | 缓冲区大小 | 默认值为10000。 |
| batchPutRetryCount | 写入重试次数 | 默认值为3。 |
| batchPutSize | 每次提交数据量 | 默认每次提交500个数据点。 |
| batchPutTimeLimit | 缓冲区等待时间 | 默认值为200，单位为毫秒。 |
| batchPutConsumerThreadCount | 序列化线程数 | 默认值为1。 |

**Blink写入TSDB模型**

Blink 3.2 及以上版本支持6种Blink写入TSDB的模型，分别是： 支持单值无tag数据点的写入，其schema格式如下所示，包括3个字段，这3个字段名称不可使用其他名称代替。

```
metric,timestamp,value
```

支持单值带tag数据点的写入，其schema格式如下所示，除metric、timestamp和value关键词名字必须保持一致外，tag的名称可以任意指定。

```
metric,timestamp,value，tagKey1,....,tagKeyN
```

支持单值带不确定tag个数的数据点的写入，其schema格式如下所示，包括4个字段，这4个字段名称不可使用其他名称代替。

```
metric,timestamp,value,tags
```

其中，tags的内容为形如如下格式的JSON字符串，便于绕过Blink table schema需要固定tag个数的限制。

```json
{"tagKey1":"tagValue1","tagKey2":"tagValue2",……,"tagKeyN":"tagValueN"}
```

支持多值无tag数据点的写入，其schema格式如下所示。

```
metric,timestamp,field_name1,field_name2,……,field_nameN
```

其中metric和timestamp字段名称不可使用其他名称代替。对于多值的fields，由于需要区分tag和field，同时兼容之前的单值写入，这里约定需要给每个field加上固定前缀field，自动识别field字段。例如，对于一个field名称 `field_name1` ，在写入TSDB时，会自动将前缀 `field_` 去掉，只保留name1，即对于上面的schema，实际写入TSDB的格式如下，name1和name2是多值field的名称。

```
metric,timestamp,name1,name2,……,nameN
```

支持多值带tag数据点的写入，其schema格式如下所示，除metric和timestamp关键词名字必须保持一致外，tag的名称可以任意指定。

```
metric,timestamp，tagKey1,....,tagKeyN，field_name1,field_name2,……,field_nameN
```

支持单值带不确定tag个数的数据点的写入，其schema格式如下所示。

```
metric,timestamp,tags,field_name1,field_name2,……,field_nameN
```

其中，tags的内容类似如下JSON字符串，便于绕过Blink table schema需要固定tag个数的限制。

```json
{"tagKey1":"tagValue1","tagKey2":"tagValue2",……,"tagKeyN":"tagValueN"}
```

**常见问题**

Q：为什么Failover中会报错：LONG类型不能转换成INT类型？ A：Blink 2.2.5以下版本仅支持INT类型。Blink 2.2.5及以上版本支持BIGINT类型。

##### 3.5.3.6. 创建云数据库Redis版结果表

本文为您介绍如何创建实时计算Flink版云数据库Redis版结果表以及创建过程中涉及的WITH参数、类型映射和属性字段。

**重要**

本文仅适用于Blink 3.2.0及以上版本。 实时计算Flink版Redis结果表支持自建Redis服务。

**什么是云数据库Redis版**

实时计算（流计算） 阿里云数据库Redis版是兼容开源Redis协议标准、提供内存加硬盘混合存储的数据库服务，基于高可靠双机热备架构及可平滑扩展的集群架构，充分满足高吞吐、低延迟及弹性变配的业务需求。实时计算Flink版支持将云数据库Redis版作为流式数据的输出。

**语法示例**

云数据库Redis版结果表支持5种Redis数据结构，其DDL定义如下：

| DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 | set key value | 。 |
|---|---|---|
| create table resik_output ( a varchar, b varchar, primary key(a) ) with ( type = 'redis', mode = 'string', host = '${redisHost}', -- 例如，'127.0.0.1'。 port = '${redisPort}', -- 例如，'6379'。 dbNum = '${dbNum}', -- 默认值为0。 ignoreDelete = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |  |  |

| DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 | lpush key value | 。 |
|---|---|---|
| create table resik_output ( a varchar, b varchar, primary key(a) ) with ( type = 'redis', mode = 'list', host = '${redisHost}', -- 例如，'127.0.0.1'。 port = '${redisPort}', -- 例如，'6379'。 dbNum = '${dbNum}', -- 默认值为0。 ignoreDelete = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |  |  |

| DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 | sadd key value | 。 |
|---|---|---|
| create table resik_output ( a varchar, b varchar, primary key(a) ) with ( type = 'redis', mode = 'set', host = '${redisHost}', -- 例如，'127.0.0.1'。 port = '${redisPort}', -- 例如，'6379'。 dbNum = '${dbNum}', -- 默认值为0。 ignoreDelete = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |  |  |

| DDL为三列：第1列为key，第2列为hash key，第3列为hash key对应的hash value。Redis插入数据的命令为 _ _ _ | hmset key hash_key hash_value | 。 |
|---|---|---|
| create table resik_output ( a varchar, b varchar, c varchar, primary key(a) ) with ( type = 'redis', mode = 'hashmap', host = '${redisHost}', -- 例如，'127.0.0.1'。 port = '${redisPort}', -- 例如，'6379'。 dbNum = '${dbNum}', -- 默认值为0。 ignoreDelete = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |  |  |

| DDL为三列：第1列为key，第2列为score，第3列为value。Redis插入数据的命令为 | add key score value | 。 |
|---|---|---|
| create table resik_output ( a varchar, b double, --必须为DOUBLE类型。 c varchar, primary key(a) ) with ( type = 'redis', mode = 'sortedset', host = '${redisHost}', -- 例如，'127.0.0.1'。 port = '${redisPort}', -- 例如，'6379'。 dbNum = '${dbNum}', -- 默认值为0。 ignoreDelete = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |  |  |

**WITH参数**

实时计算（流计算）

| 参数 | 参数说明 | 是否必填 | 取值 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为 redis 。 |
| mode | 对应Redis的数据结构 |  | 取值如下： string list set hashmap sortedset |
| host | Redis Server对应地址 |  | 取值示例： 127.0.0.1 。 |
| port | Redis Server对应端口 | 否 | 默认值为6379。 |
| dbNum | Redis Server对应数据库序号 |  | 默认值为0。 |
| ignoreDelete | 是否忽略Retraction消息 |  | 默认值为false，可取值为true或false。如果设置为false，收到 Retraction时，同时删除数据对应的key及已插入的数据。 |
| password | Redis Server对应的密码 |  | 默认值为空，不进行权限验证。 |
| clusterMode | Redis是否为集群模式 |  | 取值如下： true：Redis为集群模式。 flalse（默认值）：Redis为单机模式。 说明仅Blink 3.6.x及以上版本支持该参数。 |

**类型映射**

Redis和实时计算Flink版字段类型对应关系如下。建议您使用该对应关系进行DDL声明。

| Redis字段类型 | 实时计算Flink版字段类型 |
|---|---|
| STRING | VARCHAR |
| SCORE | DOUBLE |

因为Redis的SCORE类型应用于SORTEDSET（有序集合），所以需要手动为每个Value设置一个DOUBLE类型的SCORE，Value才能按照该SCORE从小

**说明**

到大进行排序。

**代码示例**

包含Redis结果表的实时计算Flink版作业代码示例如下。

```
CREATE TABLE random_stream (
  v VARCHAR,
  p VARCHAR) with (
    type = 'random'
); create table resik_output (
  a VARCHAR,
  b VARCHAR,
  primary key(a)
) with (
  type = 'redis',
  mode = 'string',
  host = '<yourRedisHost>',
  password = '<yourRedisPassword>'
); INSERT INTO resik_output SELECT v, p FROM random_stream;
```

##### 3.5.3.7. 创建云原生数据仓库AnalyticDB MySQL版2.0结果表

本文为您介绍如何创建云原生数据仓库AnalyticDB MySQL版2.0结果表，以及云原生数据仓库AnalyticDB MySQL版和实时计算Flink版字段类型之间的映射关系。

**重要**

本文仅适用于Blink 1.4.5及以上版本。 云原生数据仓库AnalyticDB MySQL版2.0数据库支持自增主键。如果实时计算Flink版写入数据支持自增主键，则在DDL中不声明该自增字段。例如，ID是自增字段，实时计算Flink版DDL不声明该自增字段，则数据库在一行数据写入过程中会自动填补相关自增字段。

**什么是云原生数据仓库AnalyticDB MySQL版**

云原生数据仓库AnalyticDB MySQL版是阿里巴巴自主研发的海量数据实时高并发在线分析（Realtime OLAP）云计算服务，支持在毫秒级单位时间内，对千亿级数据进行实时地多维分析透视和业务探索。

**DDL定义**

云原生数据仓库AnalyticDB MySQL版3.0结果表DDL请参见创建云原生数据仓库AnalyticDB MySQL版3.0结果表。

**说明**

实时计算（流计算） 实时计算Flink版支持使用云原生数据仓库AnalyticDB MySQL版2.0作为结果输出。示例代码如下。

```
CREATE TABLE stream_test_hotline_agent ( id INTEGER, len BIGINT, content VARCHAR， PRIMARY KEY(id) ) WITH ( type='ads', url='yourDatabaseURL', tableName='<yourDatabaseTableName>', userName='<yourDatabaseUserName>', password='<yourDatabasePassword>', batchSize='20' );
```

**说明**

云原生数据仓库AnalyticDB MySQL版结果表声明中的主键要和云原生数据仓库AnalyticDB MySQL版里的主键保持一致，大小写敏感。如果不一致，则会导致数组索引越界的异常现象。

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | 结果表类型 | 固定值为ads。 |
| url | JDBC连接地址 | 请联系阿里云运维工程师获取。 |
| tableName | 表名 | 无 |
| username | 账号 | 无 |
| password | 密码 | 无 |
| maxRetryTimes | 写入重试次数 | 可选，默认值为10。 |
| bufferSize | 流入多少条数据后开始去重 | 可选，默认值为5000，表示输入的数据达到5000条就开始输出。 |
| batchSize | 一次批量写入的条数 | 可选，默认值为1000。 说明如果错误码是20015，则表示batchSize设置过大。云原生数据仓库AnalyticDB MySQL 版batchSize不能超过1 MB。例如，batchSize设置为 1000 ，则平均每条记录大小不能超过1 KB。 |
| batchWriteTimeoutMs | 写入超时时间 | 可选，单位为毫秒，默认值为5000。表示如果缓存中的数据在等待5秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |
| connectionMaxActive | 单连接池最大连接数 | 可选，默认值为30。 |
| ignoreDelete | 是否忽略delete操作 | 默认值为false。 |

**类型映射**

建议使用云原生数据仓库AnalyticDB MySQL版和实时计算Flink版字段类型对应关系进行DDL声明。

| 云原生数据仓库AnalyticDB MySQL版字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | INT |
| SMALLINT |  |
| INT |  |
| BIGINT | BIGINT |
| DOUBEL | DOUBLE |
| VARCHAR | VARCHAR |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |

##### 3.5.3.8. 创建云原生数据仓库AnalyticDB MySQL版3.0结果表

本文为您介绍如何创建云原生数据仓库AnalyticDB MySQL版3.0结果表，以及创建过程中涉及的WITH参数。

**重要**

云原生数据仓库AnalyticDB MySQL版3.0结果表暂不支持注册存储功能。 本文仅适用于 `Blink 3.3.0` 及以上版本。 云原生数据仓库AnalyticDB MySQL版2.0结果表创建说明，请参见创建云原生数据仓库AnalyticDB MySQL版2.0结果表。 云原生数据仓库AnalyticDB MySQL版3.0数据库支持自增主键。如果实时计算Flink版写入数据支持自增主键，则在DDL中不声明该自增字段。例如，ID是自增字段，实时计算Flink版DDL不声明该自增字段，则数据库在一行数据写入过程中会自动填补相关自增字段。

**DDL定义**

实时计算（流计算） 实时计算Flink版支持使用云原生数据仓库AnalyticDB MySQL版3.0版本作为结果表输出。示例代码如下。

```
CREATE TABLE rds_output ( id INT, len INT, content VARCHAR， PRIMARY KEY(id,len) ) WITH ( type='ADB30', url='jdbc:mysql://<yourNetworkAddress>:<PortId>/<yourDatabaseName>', tableName='<yourDatabaseTableName>', userName='<yourDatabaseUserName>', password='<yourDatabasePassword>' );
```

**实现原理**

实时计算Flink版写入云原生数据仓库AnalyticDB MySQL版3.0结果表可以分为以下两个阶段：
1. 将实时计算Flink版每行的结果数据拼接为一行SQL。
2. 在目标数据库执行拼接后的SQL。

**WITH参数**

| 参数 | 注释说明 | 是否必选 | 备注 |
|---|---|---|---|
| type | connector类型 | 是 | 固定值为 ADB30 。 |
| url | jdbc连接地址 | 是 | 云原生数据仓库AnalyticDB MySQL版数据库地址。 说明 databaseName为云原生数据仓库AnalyticDB MySQL版数据库名称。 |
| tableName | 表名 | 是 | 无 |
| username | 账号 | 是 | 无 |
| password | 密码 | 是 | 无 |
| maxRetryTimes | 写入重试次数 | 否 | 默认值为3。 |
| bufferSize | 流入多少条数据后开始去重 | 否 | 默认值为1000，表示输入的数据达到1000条则开始输出。 说明需要指定主键后才能生效。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为1000。 说明需要指定主键后才能生效。 |
| flushIntervalMs | 清空缓存的时间间隔 | 否 | 单位为毫秒，默认值为3000。表示如果缓存中的数据在等待3秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |
| ignoreDelete | 是否忽略DELETE操作 | 否 | 默认值为false，表示支持DELETE功能。 |
| replaceMode | 是否采用replace into语法插入数据 | 否 | 取值如下： true（默认）：采用replace into语法插入数据。 false：采用insert into on duplicate key语法插入数据。 说明 replaceMode参数生效，需要满足以下两个条件： Blink为3.x及以上版本。 ADB为3.1.3.5及以上版本。 |
| excludeUpdateColumns | 在更新主键值相同的数据时，忽略指定字段的更新。 | 否 | 如果要忽略的字段为多个，则需要使用英文逗号（,）分割。例如 excludeUpdateColumns=column1,column2 。 |
| reserveMilliSecond | TimeStamp类型是否保留毫秒 | 否 | 默认值为false，不保留毫秒数值。 |

##### 3.5.3.9. 创建日志服务SLS结果表

本文为您介绍如何创建实时计算Flink版日志服务SLS结果表。

**重要**

本文仅适用于Blink 1.4.5及以上版本。 日志服务SLS结果表仅支持VARCHAR类型的字段。

**什么是日志服务**

日志服务SLS是针对日志类数据的一站式服务。日志服务可以帮助您快捷地完成数据采集、消费、投递以及查询分析，提升运维和运营效率，建立海量日志处理能力。日志服务本身是流数据存储，实时计算Flink版能将其作为流式数据的输入。

**DDL定义**

实时计算Flink版支持使用日志服务作为结果输出。日志服务结果表声明示例如下。 实时计算（流计算）

```
create table sls_stream(
 `name` VARCHAR,
 age BIGINT,
 birthday BIGINT
)with(
 type='sls',
 endPoint='http://cn-hangzhou-corp.sls.aliyuncs.com',
 accessId='<yourAccessId>',
 accessKey='<yourAccessKey>',
 project='<yourProjectName>',
 logstore='<yourLogstoreName>'
);
```

**WITH参数**

| 参数 | 注释说明 | 是否必填 | 备注 |
|---|---|---|---|
| endPoint | EndPoint地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | 项目名 | 是 | 无 |
| logstore | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| topic | 属性字段 | 否 | 默认值为空，可以将选定的字段作为属性字段 topic 填充。 |
| timestampColumn | 属性字段 | 否 | 默认值为空，可以将选定的字段作为属性字段 timestamp 填充（类型必须为 INT）。如果未指定，则默认填充当前时间。 说明实时计算Flink版2.2.2及以上版本支持该参数。 |
| source | 属性字段。日志的来源地，例如产生该日志机器的IP地址。 | 否 | 默认值为空，可以将选定的字段作为属性字段 source 填充。 |
| partitionColumn | 分区列 | 否 | 如果 mode 为 partition ，则该参数必填。 |
| flushIntervalMs | 触发数据写入的周期 | 否 | 默认值为2000，单位为毫秒。 |
| reserveMilliSecond | TIMESTAMP类型是否保留毫秒值。 | 否 | 默认值为false，不保留。 说明实时计算Flink版2.2.6及以上版本支持该参数。 |

**类型映射**

日志服务和实时计算Flink版字段类型对应关系如下。建议您使用该对应关系进行DDL声明。

| 日志服务字段类型 | 实时计算Flink版字段类型 |
|---|---|
| STRING | VARCHAR |

**代码示例**

包含日志服务SLS结果表的实时计算Flink版作业代码示例如下。

```
CREATE TABLE random_input (
  a VARCHAR,
  b VARCHAR) with (
    type = 'random'
); create table sls_output(
 a varchar,
 b varchar
)with(
 type='sls',
 endPoint='http://cn-hangzhou-corp.sls.aliyuncs.com',
 accessId='<yourAccessId>',
 accessKey='<yourAccessKey>',
 project='ali-cloud-streamtest',
 logStore='stream-test2'
); INSERT INTO sls_output SELECT a, b FROM random_input;
```

**常见问题**

Q：如何配置输出结果表中的**topic**？ A：需要配置**topic**为结果表中的一个字段。例如，本文示例代码中设置 `topic='age'` 。配置完成后，结果值中 `age` 字段的值会写入日志服务，同时日志服务不会把 `age` 字段写入下游。

##### 3.5.3.10. 创建表格存储Tablestore结果表

实时计算（流计算） 本文为您介绍如何创建实时计算Flink版表格存储结果表，以及表格存储和实时计算Flink版字段类型之间的映射关系。

**重要**

本文仅适用于Blink 1.4.5及以上版本。

**什么是表格存储Tablestore**

表格存储Tablestore是基于阿里云飞天分布式系统的分布式NoSQL数据存储服务。表格存储通过数据分片和负载均衡技术，实现数据规模与访问并发上的无缝扩展，提供海量结构化数据的存储和实时访问服务。

**DDL定义**

实时计算Flink版支持使用Tablestore作为结果输出，示例代码如下。

```
CREATE TABLE stream_test_hotline_agent (
 name VARCHAR,
 age BIGINT,
 birthday BIGINT,
 PRIMARY KEY (name,age)
) WITH (
 type='ots',
 instanceName='<yourInstanceName>',
 tableName='<yourTableName>',
 accessId='<yourAccessId>',
 accessKey='<yourAccessSecret>',
 endPoint='<yourEndpoint>',
 valueColumns='birthday'
);
```

**说明**

valueColumns值不能是声明的主键，可以是主键之外的任意字段。 Tablestore结果表声明中，除主键列外，至少包含一个属性列。

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | 结果表类型 | 固定值为ots。 |
| instanceName | 实例名 | 无 |
| tableName | 表名 | 无 |
| endPoint | 实例访问地址 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 无 |
| accessKey | AccessKey Secret | 无 |
| valueColumns | 指定插入的字段列名 | 插入多个字段以英文逗号（,）分割。例如 'ID,NAME' 。 |
| bufferSize | 流入多少条数据后开始输出 | 可选，默认值为5000，表示输入的数据达到5000条就开始输出。 说明在实时计算Flink版系统，bufferSize根据Tablestore主键对结果数据进行去重后，再在bufferSize的基础上进行batchSize。 |
| batchWriteTimeoutMs | 写入超时的时间 | 可选，单位为毫秒，默认值为5000。表示如果缓存中的数据在等待5秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |
| batchSize | 一次批量写入的条数 | 可选，默认值为100。 |
| retryIntervalMs | 重试间隔时间 | 可选，单位毫秒，默认值为1000。 |
| maxRetryTimes | 最大重试次数 | 可选，默认值为100。 |
| ignoreDelete | 是否忽略DELETE操作 | 默认值为False。 |

**类型映射**

| Tablestore字段类型 | 实时计算Flink版字段类型 |
|---|---|
| INTEGER | BIGINT |
| STRING | VARCHAR |
| BOOLEAN | BOOLEAN |
| DOUBLE | DOUBLE |

**说明**

Tablestore结果表必须定义有 `Primary Key` ，以Update方式写入结果数据到Tablestore表。

##### 3.5.3.11. 创建MaxCompute结果表

本文为您介绍如何创建MaxCompute结果表，以及创建过程中及到的WITH参数、类型映射和常见问题。 实时计算（流计算）

**重要**

仅Blink 1.5.1及以上版本支持MaxCompute结果表。 MaxCompute中的Clustered Table表不支持作为MaxCompute结果表。

**实现原理**

MaxCompute Sink可以分为以下两个阶段：
1. 写入数据。调用MaxCompute SDK中的接口将数据写入缓冲区，在缓冲区大小超过64 MB或者每隔指定的时间间隔时，上传数据到MaxCompute的临时文件中。
2. 提交会话。在任务进行Checkpoint时， MaxCompute Sink会调用Tunnel的Commit方法，提交会话，移动临时文件到MaxCompute表的数据目录，并修改元数据。

**说明**

Commit方法不能提供原子性。因此，MaxCompute Sink提供的是At least Once方式，而不是Exactly Once方式。

**语法示例**

实时计算Flink版支持使用MaxCompute作为结果输出，示例代码如下。

**说明**

DDL中定义的字段需要与MaxCompute物理表中的字段名称、顺序以及类型保持一致，否则可能导致MaxCompute物理表中查询的数据为 `/n` 。

```
create table odps_output(
    id INT,
    user_name VARCHAR,
    content VARCHAR
) with (
    type = 'odps',
    endPoint = '<YourEndPoint>',
    project = '<YourProjectName>',
    tableName = '<YourtableName>',
    accessId = '<yourAccessKeyId>',
    accessKey = '<yourAccessKeySecret>',
    `partition` = 'ds=2018****'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为 odps 。 |
| endPoint | MaxCompute服务地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoint | MaxCompute Tunnel服务的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | MaxCompute项目名称 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| partition | 分区名 | 否 | 如果存在分区表则必填： 固定分区例如 `partition` = 'ds=20180905' 表示将数据写入分区 ds= 20180905 。 动态分区（Blink 3.2.1及以上版本支持） 如果不明文显示分区的值，则会根据写入数据中的分区列具体的值，写入到不同的分区中。例如 `partition`='ds' 表示根据 ds 字段的值写入分区。 如果要创建多级动态分区，With参数中Partition的字段顺序和结果表的DDL中的分区字段顺序，必须与物理表一致，各个分区字段之间使用逗号（,）分割。 说明动态分区列需要显式写在建表语句中。 对于动态分区字段为空的情况，如果数据源中 ds=null 或者 ds='' ，则输出结果为： 3.2.1及以前的版本会抛出空指针异常（NPE）。 3.2.2及以后的版本会创建ds=NULL的分区。 |
| flushIntervalMs | Odps tunnel writer缓冲区Flush间隔，单位毫秒。 MaxCompute Sink写入记录时， 先放入数据到MaxCompute的缓冲区中，等缓冲区溢出或者每隔一段时间（flushIntervalMs）时，再把缓冲区里的数据写到目标 MaxCompute表。 | 否 | 默认值是30000毫秒，即30秒。 说明 Blink 3.6.0及以上版本支持该参数。 |

实时计算（流计算）

| partitionBy | 写入Sink节点前，系统会根据该值做Hash Shuffle，数据就会流向对应的Sink节点。 | 否 |  | 系统按照多个列进行Hash Shuffle，各个列名之间使用逗号（,）分割。默认为空。 说明 Blink 3.6.0及以上版本支持该参数。 |  |
|---|---|---|---|---|---|
| isOverwrite | 写入Sink节点前，是否将结果表清空。 | 否 |  | Blink 3.2以下版本默认参数值为true。 Blink 3.2及以上版本默认参数值为false。在声明MaxCompute的流式作业结果表时，isOverwrite参数必须为false，否则在编译时会抛出异常。 说明 Blink 3.2及以上版本支持isOverwrite参数值变更为true。Blink 3.2以下版本如需变更isOverwrite参数值，请升级版本。 |  |
| dynamicPartitionLimit | 底层框架统计分区数目 | 否 |  | 默认值是100，内存中会把出现过的分区和Tunnel/writer的映射关系维护到一个Map里，如果这个Map的大小超过了dynamicPartitionLimit设定值，则会出现 Too many dynamic |  |
|  |  |  |  |  | Too many dynamic |
|  |  |  |  | partitions: 100, which exceeds the size limit: 100 报错。 |  |

**类型映射**

| MaxCompute字段类型 | 实时计算Flink版字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| STRING | VARCHAR |
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |

**代码示例**

包含MaxCompute结果表的实时计算Flink版作业代码示例如下： 写入固定分区

```
CREATE TABLE source (
   id INT,
   len INT,
   content VARCHAR
) with (
   type = 'random'
); create table odps_sink (
   id INT,
   len INT,
   content VARCHAR
) with (
   type = 'odps',
   endPoint = '<yourEndpoint>',
   project = '<yourProjectName>',
   tableName = '<yourTableName>',
   accessId = '<yourAccessId>',
   accessKey = '<yourAccessPassword>',
   `partition` = 'ds=20180418'
); INSERT INTO odps_sink
   id, len, content
FROM source;
```

写入动态分区实时计算（流计算）

```
CREATE TABLE source (
   id INT,
   len INT,
   content VARCHAR,
   c TIMESTAMP
) with (
   type = 'random'
); create table odps_sink (
   id INT,
   len INT,
   content VARCHAR,
```

`ds VARCHAR --`动态分区列需要显式写在建表语句中。

```
) with (
   type = 'odps',
   endPoint = '<yourEndpoint>',
   project = '<yourProjectName>',
   tableName = '<yourTableName>',
   accessId = '<yourAccessId>',
   accessKey = '<yourAccessPassword>',
```

`partition`='ds' --不写分区的值，表示根据`ds`字段的值写入不同分区。

```
); INSERT INTO odps_sink
   id,
   len,
   content,
FROM source;
```

**常见问题**

Q：公共云的endPoint和tunnelEndpoint是什么？配置错误会产生什么结果？ A：endPoint和tunnelEndpoint参数说明参见配置Endpoint。VPC环境中这两个参数如果配置错误可能会导致任务异常。 endPoint配置错误：任务上线停滞在91%的进度。 tunnelEndpoint配置错误：任务运行失败。 Q: Stream模式的MaxCompute结果表是否支持**isOverwrite**为**true**？ A：Blink 3.2以下版本支持，Blink3.2及以上版本不支持。
**isOverwrite**为**true**，即写入结果表之前会把结果表或者结果数据清空。作业每次启动后和暂停恢复后、写入之前会把原来结果表或者结果分区里的内容删除。
Blink 3.2以下版本**isOverwrite**默认值是**true**，且不支持修改。流式作业完成暂停或恢复操作后，会造成数据丢失。 Blink 3.2及以上版本**isOverwrite**默认值是**false**，且在声明MaxCompute流式作业结果表时，**isOverwrite**参数值需要设置为**false**，否则在编译时会抛出异常。 Stream模式的MaxCompute结果表具备At Least Once数据保障机制，在作业运行失败后，可能会出现数据重复。

##### 3.5.3.12. 创建Elasticsearch结果表

本文为您介绍如何创建实时计算Flink版Elasticsearch（ES）结果表以及创建结果表时使用的WITH参数。 本文仅适用于Blink 3.2.2及以上版本。

**重要**

**DDL定义**

实时计算Flink版支持使用ES作为结果输出，示例代码如下。

```
 CREATE TABLE es_stream_sink(
  field1 LONG,
  field2 VARBINARY,
  field3 VARCHAR,
  PRIMARY KEY(field1)
)WITH(
  type ='elasticsearch',
  endPoint = 'http://es-cn-mp****.public.elasticsearch.aliyuncs.com:****',
  accessId = '<yourAccessId>',
  accessKey = '<yourAccessSecret>',
  index = '<yourIndex>',
  typeName = '<yourTypeName>'
);
```

**说明**

ES支持根据PRIMARY KEY进行UPDATE，且PRIMARY KEY只能为1个字段。 在指定PRIMARY KEY后，Document的ID为PRIMARY KEY字段的值。 在未指定PRIMARY KEY时，Document的ID为随机，详情请参见Index API。 在full更新模式下，新增的doc会完全覆盖已存在的doc。 在inc更新模式下，系统会依据输入的字段值更新对应的字段。 所有的更新默认为UPSERT语义，即INSERT或UPDATE。

**WITH参数（通用配置）**

| 参数 | 说明 | 默认值 | 是否必选 |
|---|---|---|---|

实时计算（流计算）

| type | connector类型 | elasticsearch | 是 |
|---|---|---|---|
| endPoint | Server地址，例入：http://127.0.0.1:9211。 | 无 | 是 |
| accessId | 创建ES时的登录名说明如果您通过Kibana插件操作ES，请填写Kibana登录 ID。 | 无 | 是 |
| accessKey | 创建ES时的登录密码说明如果您通过Kibana插件操作ES，请填写Kibana登录密码。 | 无 | 是 |
| index | 索引名称，类似于数据库Database的名称。 | 无 | 是 |
| typeName | Type名称，类似于数据库的Table名称。 | 无 | 是 |
| bufferSize | 流入多少条数据后开始去重。 | 1000 | 否 |
| maxRetryTimes | 异常重试次数。 | 30 | 否 |
| timeout | 读超时，单位为毫秒。 | 600000 | 否 |
| discovery | 是否开启节点发现。如果开启，客户端每5分钟刷新一次Server List。 | false | 否 |
| compression | 是否使用GZIP压缩Request Bodies。 | true | 否 |
| multiThread | 是否开启JestClient多线程。 | true | 否 |
| ignoreWriteError | 是否忽略写入异常。 | false | 否 |
| settings | 创建Index的Settings配置。 | 无 | 否 |
| updateMode | 指定主键（PRIMARY KEY）后的更新模式： full：全量覆盖 inc：增量更新 | full | 否 |

**WITH参数（动态索引相关）**

| 参数 | 说明 | 默认值 | 是否必选 |
|---|---|---|---|
| dynamicIndex | 是否开启动态索引： true：开启 false：不开启 | false | 否 |
| indexField | 抽取索引的字段名 | 无 | dynamicIndex为true时必填，只支持TIMESTAMP（以秒为单位）、 DATE和LONG3种数据类型。 |
| indexInterval | 切换索引的周期 | d | dynamicIndex为true时必填 ，可选参数值如下： d：天 m：月 w：周 |
| mapping | 启用动态索引时，设置文档各字段的类型与格式。 | 空 | 否。Blink 3.7.0版本及以上版本支持该参数。例如，设置名为sendTime 字段的格式： { "properties": { "sendTime": { "type": "date", "format": "yyyy-MM-dd HH:mm:ss" } } } |

**说明**

仅Blink 2.2.7及以上版本支持动态索引功能。 当开启动态索引后，基本配置中的 `index` 名称会作为后续创建索引的统一Alias，Alias和索引为一对多关系。 不同的 `indexInterval` 对应的真实索引名称：

**d -> Alias "yyyyMMdd"**

**m -> Alias "yyyyMM"**

**w -> Alias "yyyyMMW"**

对于单个的真实索引可使用Index API进行修改，但对于Alias只支持 `get` 功能。如果需要更新Alias，请参见Index Aliases。

##### 3.5.3.13. 创建消息队列Kafka结果表

本文档为您介绍如何创建实时计算Flink版消息队列Kafka结果表，以及Kafka版本对应关系。 实时计算（流计算）

**重要**

本文仅适用于实时计算2.0及以上版本。 本文仅适用于独享模式。 Kafka结果表支持写入自建Kafka集群，但需注意版本对应关系，以及自建集群和实时计算集群的网络环境配置。

**什么是Kafka结果表**

消息队列Kafka版是阿里云提供的分布式、高吞吐、可扩展的消息队列服务。消息队列Kafka版广泛用于日志收集、监控数据聚合、流式数据处理、在线和离线分析等大数据领域。实时计算采用Kafka作为流式数据的数据源表或结果表。

**DDL定义**

消息队列Kafka结果表需要定义的DDL如下。

```
create table sink_kafka (
  messageKey VARBINARY,
  `message` VARBINARY,
  PRIMARY KEY (messageKey)
) with (
  type = 'kafka010',
  topic = '<yourTopicName>',
  bootstrap.servers = '<yourServerAddress>'
);
```

**说明**

创建Kafka结果表时，必须明文指定 `PRIMARY KEY (messageKey)` 。 仅Blink 2.2.6及以上版本，支持阿里云Kafka或自建Kafka的TPS和RPS等指标信息的显示。

**WITH参数**

通用配置

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| type | Kafka对应版本 | 是 | 必须是Kafka08、Kafka09、Kafka010、Kafka011中的一种，版本对应关系请参见Kafka 版本对应关系。 |
| topic | Topic名称 | 是 | 无 |

必选配置 Kafka08必选配置

| 参数 | 说明 |
|---|---|
| zookeeper.connect | zk连接ID |

Kafka09/Kafka010/Kafka011必选配置

| 参数 | 说明 |
|---|---|
| bootstrap.servers | Kafka集群地址 |

可选配置参数

```
 consumer.id
 socket.timeout.ms
 fetch.message.max.bytes
 num.consumer.fetchers
 auto.commit.enable
 auto.commit.interval.ms
 rebalance.max.retries
 fetch.min.bytes
 fetch.wait.max.ms
 rebalance.backoff.ms
 refresh.leader.backoff.ms
 auto.offset.reset
 consumer.timeout.ms
 exclude.internal.topics
 partition.assignment.strategy
 client.id
 zookeeper.session.timeout.ms
 zookeeper.connection.timeout.ms
 zookeeper.sync.time.ms
 offsets.storage
 offsets.channel.backoff.ms
 offsets.channel.socket.timeout.ms
```

实时计算（流计算）

```
 offsets.commit.max.retries
 dual.commit.enabled
 partition.assignment.strategy
 socket.receive.buffer.bytes
 fetch.min.bytes
```

其它可选配置项请参见以下Kafka官方文档：

**说明**

Kafka09 Kafka010 Kafka011

**Kafka版本对应关系**

| type | Kafka版本 |
|---|---|
| Kafka08 | 0.8.22 |
| Kafka09 | 0.9.0.1 |
| Kafka010 | 0.10.2.1 |
| Kafka011 | 0.11.0.2及以上 |

**示例**

```
create table datahub_input (
  id VARCHAR,
  nm VARCHAR
) with (
  type = 'datahub'
); create table sink_kafka (
  messageKey VARBINARY,
  `message` VARBINARY,
  PRIMARY KEY (messageKey)
) with (
 type = 'kafka010',
 topic = '<yourTopicName>',
 bootstrap.servers = '<yourServerAddress>'
);
 sink_kafka
cast(id as VARBINARY) as messageKey,
 cast(nm as VARBINARY) as `message`
FROM
 datahub_input;
```

##### 3.5.3.14. 创建云数据库RDS SQL Server版结果表

本文为您介绍如何创建云数据库RDS SQL Server版结果表，以及创建结果表时使用的WITH参数、类型映射和JDBC连接参数。

**重要**

本文仅适用于Blink 3.2.0及以上版本。 实时计算Flink版暂不支持引用RDS SQL Server版本作为数据存储。

**语法示例**

实时计算Flink版支持使用云数据库RDS SQL Server版作为结果表输出，示例代码如下。

```
create table ss_output(
 id INT,
 len INT,
 content VARCHAR,
 primary key(id,len)
) with (
 type='jdbc',
 url='jdbc:sqlserver://ip:port;database=****',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
);
```

实时计算（流计算）

**说明**

实时计算Flink版写入RDS和DRDS数据库结果表原理：针对实时计算Flink版每行结果数据，拼接成一行SQL语句，输入至目标端数据库。如果使用批量写，需要在URL后面加上参数**?rewriteBatchedStatements=true**，以提高系统性能。 RDS SQL Server数据库支持自增主键。如果需要让实时计算Flink版写入数据支持自增主键，则在DDL中不声明该自增字段。例如，ID是自增字段，实时计算 Flink版DDL不写出该自增字段，则数据库在一行数据写入过程中会自动填补相关的自增字段。 如果DRDS有分区表，拆分键必须在实时计算Flink版DDL里**primary key****（）**中声明，否则拆分的表无法写入。 DDL声明的字段必选至少存在一个非主键的字段，否则产生报错。

**WITH参数**

| 参数 | 参数说明 | 是否必填 | 备注 |
|---|---|---|---|
| url | JDBC（Java DataBase Connectivity）连接地址 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| username | 账号 | 是 | 无 |
| password | 密码 | 是 | 无 |
| maxRetryTimes | 写入重试次数 | 否 | 默认值为10。 |
| bufferSize | 流入多少条数据后开始去重 | 否 | 默认值为10000，表示输入的数据达到10000条开始去重。 |
| flushIntervalMs | 清空缓存的时间间隔 | 否 | 单位为毫秒，默认值为2000，表示如果缓存中的数据在等待2秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |
| excludeUpdateColumns | 忽略指定字段的更新 | 否 | 可选，默认值为空（默认忽略Primary Key字段），表示更新主键值相同的数据时，忽略指定字段的更新。 |
| ignoreDelete | 是否忽略Delete操作 | 否 | 默认值为False。 |

**类型映射**

| RDS字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARBINARY | VARBINARY |

**JDBC连接参数**

| 参数名称 | 参数说明 | 缺省值 | 最低版本要求 |
|---|---|---|---|
| useUnicode | 是否使用Unicode字符集。如果参数 CharacterEncoding设置为GB2312或 GBK，useUnicode值必须设置为True。 | False | 1.1g |
| characterEncoding | 当useUnicode设置为True时，指定字符编码。例如可设置为GB2312或GBK。 | False | 1.1g |
| autoReconnect | 当数据库连接异常中断时，是否自动重新连接。 | False | 1.1 |
| autoReconnectForPools | 是否使用针对数据库连接池的重连策略。 | False | 3.1.3 |
| failOverReadOnly | 自动重连成功后，连接是否设置为只读。 | True | 3.0.12 |
| maxReconnects | autoReconnect设置为True时，重试连接的次数。 | 3 | 1.1 |
| initialTimeout | autoReconnect设置为True时，两次重连之间的时间间隔，单位为秒。 | 2 | 1.1 |
| connectTimeout | 和数据库服务器建立socket连接时的超时， 单位为毫秒。 | 0，表示永不超时，适用于JDK 1.4及以上版本。 | 3.0.1 |
| socketTimeout | socket操作（读写）超时，单位为毫秒。 | 0，表示永不超时。 | 3.0.1 |

实时计算（流计算）

**代码示例**

包含云数据库RDS SQL Server版结果表的实时计算Flink版作业代码示例如下。

```
CREATE TABLE source (
   id INT,
   len INT,
   content VARCHAR
) with (
   type = 'random'
); CREATE TABLE rds_output(
 id INT,
 len INT,
 content VARCHAR,
 PRIMARY KEY (id,len)
) WITH (
 type='jdbc',
 url='<yourDatabaseURL>',
 tableName='<yourDatabaseTable>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
); INSERT INTO rds_output SELECT id, len, content FROM source;
```

**常见问题**

Q：实时计算Flink版的结果数据写入RDS表，是按主键更新，还是生成1条新的记录？ A：根据DDL中是否定义主键，分为以下两种方式： DDL中定义主键：采用 `insert into on duplicate key update` 的方式更新记录，即对于不存在的主键字段会直接插入，存在的主键字段则更新相应的值。 DDL中没有定义主键：采用 `insert into` 的方式插入记录，追加数据。 Q：使用RDS表中的唯一索引进行GROUP BY操作需要注意什么？ A：需要注意以下两点： 在作业中的主键（Primary Key）中声明该唯一索引。 RDS中只有一个自增主键，实时计算Flink版作业中不能将该自增主键声明为主键。

##### 3.5.3.15. 创建云数据库MongoDB版结果表

本文为您介绍如何创建实时计算Flink版云数据库MongoDB版结果表，以及创建过程中涉及到的WITH参数。

**重要**

本文仅适用于Blink 3.2.2及以上版本。 MongoDB结果表不支持主键更新，数据输入形式为重复插入。

**DDL定义**

实时计算Flink版支持使用MongoDB作为数据输出的结果表，示例代码如下。

```
CREATE TABLE mongodb_sink (
  `a`  VARCHAR
) WITH (
   type = 'mongodb',
   database = '<yourDatabaseName>',
   collection= '<yourCollectionName>',
   uri='mongodb://{<databaseAccount>}:{<atabasePassword>}@{host}:****?replicaSet=mgset-1224****',
   keepAlive='true',
   maxConnectionIdleTime='20000',
   batchSize='2000'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | Connector类型 | 是 | 固定值为mongodb。 |
| database | 数据库名称 | 是 | 无 |
| collection | 数据集合 | 是 | 无 |
| uri | MongoDB连接串 | 是 | 无 |
| keepAlive | 是否保持长连接 | 否 | 默认值为true。 |
| maxConnectionIdleTime | 连接超时时长 | 否 | 整型值，不能为负数，单位为毫秒。默认值为60000。0表示无连接超时限制。 |
| batchSize | 每次批量写入的条数 | 否 | 整型值，默认值为1024。系统会设定一个大小为batchSize的缓冲条数， 当数据的条数达到batchSize时，触发数据的输出。 说明当Checkpoint时间达到时，即使数据未到达batchSize 值，也将触发数据的输出。 |

实时计算（流计算）

##### 3.5.3.16. 创建Oracle数据库结果表

本文为您介绍如何创建Oracle结果表，以及创建结果表时使用的WITH参数、类型映射和注意事项。

**重要**

本文仅适用于Blink 3.6.0及以上版本。

**注意事项**

实时计算Flink版将每行结果数据拼接成一行SQL语句写入目标数据库。 根据数据库中是否存在需要的表，执行以下操作： 当数据库中不存在需要的表时，Oracle结果表会新建一个用于写入结果的表。 当数据库中存在需要的表时，Oracle结果表会向该表中写入或者更新数据。 逻辑表和物理表的主键不一定完全相同，要求逻辑表的主键包含物理表的主键。 使用以下两种函数处理Oracle数据库结果表的数据： 如果没有定义主键，则执行Append函数向表中插入数据。 如果已经定义主键，则执行Upsert函数向表中插入数据。当主键不存在时，则插入主键；当主键存在时，则更新主键。

**语法示例**

实时计算Flink版支持使用Oracle数据库作为结果表，代码示例如下。

```
CREATE TABLE oracle_sink(
  employee_id BIGINT,
  employee_name VARCHAR,
  employee_age INT,
  PRIMARY KEY(employee_id)
) WITH (
    type = 'oracle',
    url = '<yourUrl>',
    userName = '<yourUserName>',
    password = '<yourPassword>',
    tableName = '<yourTableName>'
);
```

**WITH 参数**

| 参数 | 描述 | 是否必选 | 示例值 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为oracle。 |
| url | 数据库连接串 | 是 | 请联系阿里云运维工程师获取。 |
| userName | 登录数据库的用户名 | 是 | 无 |
| password | 登录数据库的密码 | 是 | 无 |
| tableName | 数据库的表名 | 是 | 无 |
| maxRetryTimes | 向结果表插入数据的最大尝试次数 | 否 | 默认值为10。 |
| batchSize | 单次写入数据的批次大小说明指定主键后batchSize参数才生效。 batchSize或bufferSize参数达到阈值时都会触发数据写入。 | 否 | 默认值为50。 |
| bufferSize | 去重的缓存大小说明指定主键后batchSize参数才生效。 batchSize或bufferSize参数达到阈值时都会触发数据写入。 | 否 | 默认值为500。 |
| flushIntervalMs | 写超时时间，单位为毫秒。 说明如果在写超时时间内没有向数据库写入数据，系统会将缓存的数据再写一次。 | 否 | 默认值为500。 |
| excludeUpdateColumns | 更新表的某行数据时，是否不更新该行指定的列数据。 说明更新表的某行数据时，默认不更新主键数据。 | 否 | 默认不填写。 |
| ignoreDelete | 是否忽略删除操作。 | 否 | 默认值为false。 |

**类型映射**

| Oracle 字段类型 | 实时计算Flink版字段类型 |
|---|---|

实时计算（流计算）

| CHAR VARCHAR VARCHAR2 | VARCHAR |
|---|---|
| FLOAT | DOUBLE |
| NUMBER | BIGINT |
| DECIMAL | DECIMAL |

**代码示例**

实时计算Flink版包含Oracle数据库结果表的代码示例如下。

```
CREATE TABLE oracle_source (
  employee_id BIGINT,
  employee_name VARCHAR,
  employ_age INT
) WITH (
  type = 'random'
); CREATE TABLE oracle_sink(
  employee_id BIGINT,
  employee_name VARCHAR,
  employ_age INT,
  primary key(employee_id)
)with(
  type = 'oracle',
  url = 'jdbc:oracle:thin:@192.168.171.62:1521:sit0',
  userName = 'blink_test',
  password = 'blink_test',
  tableName = 'oracle_sink'
); INSERT INTO oracle_sink SELECT * FROM oracle_source;
```

##### 3.5.3.17. 创建InfluxDB结果表

本文为您介绍如何创建实时计算Flink版InfluxDB结果表，以及创建结果表时使用的WITH参数和类型映射。

**重要**

InfluxDB暂不支持注册存储功能。 本文仅适用于Blink 3.5.0-hotfix及以上版本。

**DDL定义**

实时计算Flink版支持使用InfluxDB作为结果输出，示例代码如下。

```
create table stream_test_influxdb(
    `metric` varchar,
    `timestamp` BIGINT,
    `tag_value1` varchar,
    `field_fieldValue1` Double
)with(
    type = 'influxdb',
    endpoint = 'http://service.cn.influxdb.aliyuncs.com:****',
    database = '<yourDatabaseName>',
    batchPutsize = '1',
    username = '<yourDatabaseUserName>',
    password = '<yourDatabasePassword>'
);
```

建表默认格式： 第0列：metric（VARCHAR），必填。 第1列：timestamp（BIGINT），必填，单位为毫秒。 第2列：tag_value1（VARCHAR），必填，最少填写一个。 第3列：field_fieldValue1（DOUBLE），必填，最少填写一个。 写入多个field_fieldValue时，您需要按照如下格式填写。

```
field_fieldValue1 类型, field_fieldValue2 类型, ... field_fieldValueN 类型
```

示例如下。

```
field_fieldValue1 Double, field_fieldValue2 INTEGER, ... field_fieldValueNINTEGER
```

结果表中只支持**metric**、**timestamp**、**tag_***和**field_***，不能出现其他的字段。

**说明**

实时计算（流计算）

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为InfluxDB。 |
| endpoint | InfluxDB的Endpoint | 是 | 请联系阿里云运维工程师获取。 |
| database | InfluxDB的数据库名 | 是 | 例如：db-blink或者blink。 |
| batchPutSize | 批量提交的记录条数 | 否 | 默认每次提交500个数据点。 |
| username | InfluxDB的用户名 | 是 | 需要对写入的数据库有写权限。 |
| password | InfluxDB的密码 | 是 | 默认值为0。 |
| retentionPolicy | 保留策略 | 否 | 为空时，默认填写为每个database的默认保留策略。 |

**类型映射**

| InfluxDB字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |

##### 3.5.3.18. 创建Phoenix5结果表

本文为您介绍如何创建实时计算Flink版云数据库Phoenix5结果表。

**重要**

本文仅适用于实时计算Flink版独享模式。 本文仅适用于Blink 3.4.0以上版本。 Phoenix5仅支持5.x版本。 Phoenix5是云数据库HBase实例中的一种HBase SQL服务，须在云数据库HBase实例中开启HBase SQL服务后才可以使用Phoenix5。

**DDL定义**

实时计算Flink版支持使用Phoenix5作为结果输出，示例代码如下。

```
create table US_POPULATION_SINK (
  `STATE` varchar,
  CITY varchar,
  POPULATION BIGINT,
  PRIMARY KEY (`STATE`, CITY)  --主键必填。
) WITH (
  type = 'PHOENIX5',
  serverUrl = '<yourserverUrl>',
  tableName = '<yourTableName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为 PHOENIX5 。 |
| serverUrl | Phoenix5的Query Server地址： 如果Phoenix5是在集群中创建的，则 serverUrl是负载均衡服务的URL地址。 如果Phoenix5是在单机中创建的，则 serverUrl是单机的URL地址。 | 是 | 您需要在云数据库HBase实例中开启Hbase SQL服务。 serverUrl格式为http://host:port，其中： host：Phoenix5服务的域名。 port：Phoenix5服务的端口号，固定值为 8765。 |

实时计算（流计算）

| tableName | 读取Phoenix5表名。 | 是 | Phoenix5表名格式为 SchemaName.TableName，其中： SchemaName：模式名，可以为空，即不写模式名，仅写表名，表示使用数据库的默认模式。 TableName：表名。 |
|---|---|---|---|

**代码示例**

包含Phoenix5结果表的实时计算Flink版作业代码示例如下。

```
create table `source` (
  `id` varchar,
  `name` varchar,
  `age` varchar,
  `birthday` varchar
) WITH (
   type = 'random'
); create table sink (
  `id` varchar,
  `name` varchar,
  `age` varchar,
  `birthday` varchar,
  primary key (id)
) WITH (
  type = 'PHOENIX5',
  serverUrl = '<yourserverUrl>',
  tableName = '<yourTableName>'
); INSERT INTO sink
  SELECT  `id` ,`name` , `age` ,`birthday`
FROM `source`;
```

##### 3.5.3.19. 创建交互式分析Hologres结果表

本文为您介绍如何创建交互式分析Hologres结果表，以及创建结果表时使用的WITH参数、流式语义和类型映射。

**重要**

本文仅适用于Blink 3.6.0及以上版本。 建议您使用Hologres 0.7及以上版本。 由于Hologres是异步写入数据的，因此需要添加**blink.checkpoint.fail_on_checkpoint_error=true** 作业参数，作业异常时才会触发Failover。

**什么是交互式分析Hologres**

交互式分析Hologres兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析处理PB级数据，让您轻松使用现有BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**语法示例**

实时计算Flink版支持使用Hologres作为结果表，代码示例如下。

```
create table Hologres_sink(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  type='hologres',
  dbname='<yourDbname>',
  tablename='<yourTablename>',
  username='<yourUsername>',
  password='<yourPassword>',
  endpoint='<yourEndpoint>',
```

field_delimiter='|' --该参数可选。

```
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为hologres。 |
| dbname | 数据库名称说明如果Schema不为Public时，则tableName需要填写为schema.tableName。 | 是 | 无 |
| tablename | 表名称 | 是 | 无 |
| username | 用户名 | 是 | 无 |
| password | 密码 | 是 | 无 |
| endpoint | Hologres VPC 端点信息 | 是 | 请联系阿里云运维工程师获取。 |

实时计算（流计算）

| fielddelimiter _ | 导出数据时，不同行之间使用的分隔符。 重要不能在数据中插入分隔符，且需要与bulkload语义一同使用。 | 否 | 默认值为"\u0002"。 |
|---|---|---|---|
| mutateType | 流式写入语义，详情请参见流式语义。 | 否 | 默认值为insertorignore。 |
| partitionrouter | 分区表写入 | 否 | 默认值为false。 说明 3.6.x版本 Hologres Sink暂不支持自动创建分区表。因此，在写入分区表之前，需要您在Hologres中手工创建对应的子表。 |
| ignoredelete | 是否忽略撤回消息。 | 否 | 默认值为false。 说明仅在使用流式语义时生效。 |
| createPartTable | 当写入分区表时，是否根据分区值自动创建不存在的分区表。 说明如果分区值中存在短划线（-），暂不支持自动创建分区表。 | 否 | false（默认值）：不会自动创建。 true：自动创建。 说明仅Blink 3.7以上版本支持该参数。 |

**流式语义**

流处理，也称为流数据或流事件处理，即对一系列无界数据或事件连续处理。执行流数据或流事件处理的系统通常允许您指定一种可靠性模式或处理语义，保证整个系统处理数据的准确性，因为网络或设备故障等可能会导致数据丢失。 根据Hologres Sink的配置和Hologres表的属性，流式语义分为以下两种：
**Exactly-once**（仅一次）：即使在发生各种故障的情况下，系统只处理一次数据或事件。
**At-least-once**（至少一次）：如果在系统完全处理之前丢失了数据或事件，则从源头重新传输，因此可以多次处理数据或事件。如果第一次重试成功，则不必进行后续
重试。 在Hologres结果表中使用流式语义，您需要注意以下几点： 如果Hologres物理表未设置主键，则Hologres Sink使用**At-least-once**语义。 如果Hologres物理表已设置主键，则Hologres Sink通过主键确保**Exactly-once**语义。当同主键数据出现多次时，您需要设置**mutateType**参数确定更新结果表的方式，**mutateType**取值如下：
**insertorignore**（默认值）：保留首次出现的数据，忽略后续所有数据。
**insertorreplace**：使用后续出现的数据整行替换已有数据。
**insertorupdate**：使用后续出现的数据选择性替换已有数据。

**说明**

当**mutateType**设置为**insertorupdate**或**insertorreplace**时，系统根据主键更新数据。 Blink定义的结果表中的数据列数不一定要和Hologres物理表的列数一致，您需要保证缺失的列没有非空约束，即列值可以为Null，否则会报错。 默认情况下，Hologres Sink只能向一张表导入数据。如果导入数据至分区表的父表，即使导入成功，也会查询数据失败。您可以设置参数**partitionRouter**为true，开启自动将数据路由到对应分区表的功能。注意事项如下：
**tablename**参数需要填写为父表的表名。
Blink Connector不会自动创建分区表，因此，需要您提前手动创建需要导入数据的分区表，否则会导入失败。

**宽表Merge和局部更新功能**

在把多个流的数据写到一张Hologres宽表的场景中，会涉及到宽表Merge和数据的局部更新。下面通过一个示例来介绍如何设置。 假设有两个Flink数据流，一个数据流中包含A、B和C字段，另一个数据流中包含A、D和E字段，Hologres宽表WIDE_TABLE包含A、B、C、D和E字段，其中A字段为主键。 具体操作如下：
1. 使用Flink SQL创建两张Hologres结果表，其中一张表只声明A、B和C字段，另一张表只声明A、D和E字段。这两张表都映射至宽表WIDE_TABLE。
2. 两张结果表的属性设置：
**mutatetype**设置为**insertorupdate**，可以根据主键更新数据。
**ignoredelete**设置为**true**，防止回撤消息产生Delete请求。
3. 将两个Flink数据流的数据分别INSERT至对应的结果表中。
在上述场景中，有如下限制：

**说明**

宽表必须有主键。 每个数据流的数据都必须包含完整的主键字段。 列存模式的宽表Merge场景在高RPS的情况下，CPU使用率会偏高，建议关闭表中字段的Dictionary encoding功能。

**类型映射**

| Hologres | BLINK |
|---|---|
| INT | INT |
| INT[] | ARRAY<INT> |
| BIGINT | BIGINT |
| BIGINT[] | ARRAY<BIGINT> |
| REAL | FLOAT |
| REAL[] | ARRAY<FLOAT> |

实时计算（流计算）

| DOUBLE PRECISION | DOUBLE |
|---|---|
| DOUBLE PRECISION[] | ARRAY<DOUBLE> |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY<BOOLEAN> |
| TEXT | VARCHAR |
| TEXT[] | ARRAY<VARCHAR> |
| NUMERIC | DECIMAL |
| DATE | DATE |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

##### 3.5.3.20. 创建分析型数据库PostgreSQL版结果表

本文为您介绍如何创建分析型数据库PostgreSQL版结果表，以及创建过程中涉及到的WITH参数和类型映射。

**重要**

本文仅适用于Blink 3.6.0及以上版本。

**实现原理**

实时计算Flink版写入分析型数据库PostgreSQL结果表可以分为以下两个阶段：
1. 将实时计算Flink版每行的结果数据拼接为一行SQL。
2. 在目标数据库执行拼接后的SQL。

**DDL定义**

实时计算Flink版支持使用分析型数据库PostgreSQL版作为结果输出。示例代码如下。

```
create table rds_output(
  id INT,
  len INT,
  content VARCHAR,
  PRIMARY KEY(id)
) with (
  type='adbpg',
  url='jdbc:postgresql://<yourNetworkAddress>:<PortId>/<yourDatabaseName>',
  tableName='<yourDatabaseTableName>',
  userName='<yourDatabaseUserName>',
  password='<yourDatabasePassword>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 源表类型。 | 是 | 固定值为 adbpg 。 |
| url | JDBC连接地址。 | 是 | 请联系阿里云运维工程师获取。 |
| tableName | 表名。 | 是 | 无。 |
| username | 账号。 | 是 | 无。 |
| password | 密码。 | 是 | 无。 |
| maxRetryTimes | 写入重试次数。 | 否 | 默认值为3。 |
| useCopy | 是否采用Copy API写入数据。 | 否 | 参数取值如下： 0（默认值）：采用INSERT方式写入数据。 1：采用copy API方式写入数据。 |
| batchSize | 一次批量写入的条数。 | 否 | 默认值为5000。 |
| exceptionMode | 数据写入过程中出现异常时的处理策略。 | 否 | 支持以下两种处理策略： ignore（默认值）：忽略出现异常时写入的数据。 strict：数据写入异常时，Failover报错。 |
| conflictMode | 当主键冲突或唯一索引出现冲突时的处理策略。 | 否 | 支持以下三种处理策略： ignore（默认值）：忽略主键冲突，保留之前的数据。 strict：主键冲突时，Failover报错。 update：主键冲突时，更新新到的数据。 |
| targetSchema | Schema名称。 | 否 | 默认值为public。 |
| connectionMaxActi ve | 单个task允许的最大连接数。 | 否 | 请根据实际的并发task个数，以及目标端数据库允许的最大连接数进行设置。 |

**类型映射**

分析型数据库PostgreSQL和实时计算Flink版字段类型对应关系如下。 实时计算（流计算）

| 分析型数据库PostgreSQL版字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| SMALLINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| DOUBLE PRECISION | DOUBLE |
| TEXT | VARCHAR |
| TIMESTAMP | DATETIME |
| DATE | DATE |
| REAL | FLOAT |
| DOUBLE PRECISION | DECIMAL |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |

##### 3.5.3.21. 创建云数据库HBase版结果表

本文为您介绍如何创建实时计算云数据库HBase版结果表。

**重要**

本文档仅适用于实时计算独享模式。 Blink 3.3.0以下版本仅支持HBase标准版。 Blink 3.3.0及以上版本同时支持HBase标准版和HBase增强版。 Blink 3.5.0及以上版本支持HBase写入主备切换。 实时计算HBase结果表不支持自建的开源HBase。

**DDL定义**

实时计算支持使用HBase作为结果输出。 HBase标准版示例代码如下。

```
create table liuxd_user_behavior_test_front (
    row_key varchar,
    from_topic varchar,
    origin_data varchar,
    record_create_time varchar,
    primary key (row_key)
) with (
    type = 'cloudhbase',
    zkQuorum = '2',
    columnFamily = '<yourColumnFamily>',
    tableName = '<yourTableName>',
    batchSize = '500'
);
```

HBase增强版示例代码如下。

```
create table liuxd_user_behavior_test_front (
    row_key varchar,
    from_topic varchar,
    origin_data varchar,
    record_create_time varchar,
    primary key (row_key)
) with (
    type = 'cloudhbase',
```

`endPoint = '<host:port>', ----HBase`增强版的`Java API`访问地址。 `userName = 'root', --`用户名。

```
    password = 'root', --密码。
    columnFamily = '<yourColumnFamily>',
    tableName = '<yourTableName>',
    batchSize = '500'
);
```

Blink 3.5.0及以上HBase增强版示例代码如下。 实时计算（流计算）

```
create table liuxd_user_behavior_test_front (
    row_key varchar,
    from_topic varchar,
    origin_data varchar,
    record_create_time varchar,
    primary key (row_key)
) with (
    type = 'cloudhbase',
```

`zkQuorum = '<host:port>', ----HBase`增强版的`Java API`访问地址。 `userName = 'root', --`用户名。

```
    password = 'root', --密码。
    columnFamily = '<yourColumnFamily>',
    tableName = '<yourTableName>',
    batchSize = '500'
);
```

Blink 3.5.0及以上HBase写入主备切换示例代码如下。

```
create table liuxd_user_behavior_test_front (
    row_key varchar,
    from_topic varchar,
    origin_data varchar,
    record_create_time varchar,
    primary key (row_key)
) with (
    type = 'cloudhbase',
```

`zkQuorum = '<host:port>', ----HBase`高可用访问地址。 `userName = 'root', --`用户名。

```
    password = 'root', --密码。
    columnFamily = '<yourColumnFamily>',
    tableName = '<yourTableName>',
    batchSize = '500'
);
```

**说明**

PRIMARY KEY支持定义多字段。多字段以 `rowkeyDelimiter` （默认为 : ）作为分隔符进行连接。 HBase执行撤回删除操作时，如果COLUMN定义了多版本，将清空所有版本的COLUMN值。 HBase标准版和HBase增强版DDL的区别为连接参数不同： HBase标准版使用连接参数 `zkQuorum` 。 HBase增强版使用连接参数 `endPoint` 。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 结果表类型 | 是 | 固定值为cloudhbase。 |
| zkQuorum | HBase集群配置的zk地址 | 是 | 可以在hbase-site.xml文件中查看hbase.zookeeper.quorum相关配置。 说明仅在HBase标准版中生效。 |
| zkNodeParent | 集群配置在zk上的路径 | 否 | 可以在hbase-site.xml文件中查看hbase.zookeeper.quorum相关配置。 说明仅在HBase标准版中生效。 |
| endPoint | HBase地域名称 | 是 | 请联系阿里云运维工程师获取。 |
| userName | 用户名 | 否 | 仅在HBase增强版中生效。 |
| password | 密码 | 否 | 仅在HBase增强版中生效。 |
| tableName | HBase表名 | 是 | 无 |
| columnFamily | 列族名 | 是 | 仅支持插入同一列族。 |
| maxRetryTimes | 最大尝试次数 | 否 | 默认值为10。 说明仅实时计算3.2.3及以上版本支持maxRetryTimes参数。 |
| bufferSize | 流入多少条数据后进行去重 | 否 | 默认值为5000。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为100。 说明建议batchSize参数值为200~300。过大的batchSize值可能导致任务 OOM（内存不足）报错。 |
| flushIntervalMs | 周期性清理buffer的间隔，可以减少写入 HBase的延迟。 | 否 | 默认值为2000，单位为毫秒。 |
| writePkValue | 是否写入主键值 | 否 | 默认值为false。 |
| stringWriteMod | 是否都按照STRING插入 | 否 | 默认值为false。 |

实时计算（流计算）

| rowkeyDelimiter | rowKey的分隔符 | 否 | 默认值为冒号（:）。 |
|---|---|---|---|
| isDynamicTable | 是否为动态表 | 否 | 默认值为false。 |
| haClustserID | HBase高可用实例ID | 否 | 只有访问同城主备实例时才需要配置。 |

**动态表**

实时计算部分结果数据需要按某列的值，作为动态列输入HBase。HBase中，以每小时的成交额作为动态列的数据，示例如下。

| rowkey | cf:0 | cf:1 | cf:2 |
|---|---|---|---|
| 20170707 | 100 | cf:1 | 300 |

当**isDynamicTable**参数值为true时，表明该表为支持动态列的HBase表。 动态表仅支持3列输出，例如，ROW_KEY、COLUMN和VALUE。此时第2列（本示例中的COLUMN）为动态列，动态表中的其它参数与HBase的WITH参数一致。 使用动态表时，所有数据类型需要先转换为STRING类型，再进行输入。

**说明**

```
CREATE TABLE stream_test_hotline_agent (
  name varchar,
  age varchar,
  birthday varchar,
  primary key (name)
) WITH (
  type = 'cloudhbase',
  ...
  columnFamily = 'cf',
  isDynamicTable ='true'
);
```

**说明**

|  | birthday |
|---|---|
| cf:18 |  |

DDL中必选按照从上到下的顺序，声明ROW_KEY（本示例中的 `name` ）、COLUMN（本示例中的 `age` ）和VALUE（本示例中的 `birthday` ），且声明 ROW_KEY为PRIMARY KEY。

**代码示例**

包含HBase结果表的实时计算作业代码示例如下。

```
create table source (
  id   TINYINT,
  name BIGINT
) with (
  type = 'random'
); create table sink (
  id    TINYINT,
  name  BIGINT,
  primary key (id)
) with (
  type = 'cloudhbase',
  zkQuorum = '<yourZkQuorum>',
  columnFamily = '<yourColumnFamily>',
  tableName = '<yourTableName>'
); INSERT INTO sink SELECT id, name FROM source;
```

**常见问题**

Q：为什么HBase结果表作业运行时会报错 `cloudHbase update error, No columns to insert for #10 item` ？ A：HBase结果表要求写入的单条记录的列数据（不包括rowkey）不能全为NULL。请先过滤全为NULL的数据，再输入HBase。

#### 3.5.4. 创建数据维表

**3.5.4.1. 概述**

在标准的create table语法基础上，增加一行 `PERIOD FOR SYSTEM_TIME` 的声明，即可实现维表功能。 `PERIOD FOR SYSTEM_TIME` 声明定义了维表的变化周期，即表明该表是一张会变化的表。 实时计算（流计算）

```
CREATE TABLE white_list (
   id varchar,
   name varchar,
   age int,
```

`PRIMARY KEY (id), --` 声明为维表时，必须有声明的主键 `PERIOD FOR SYSTEM_TIME --` 定义了维表的变化周期

```
   ) with (
   type = 'rds',
   ...
```

)

**说明**

声明维表时，必须要指名主键。 维表JOIN时，ON的条件必须包含所有主键的等值条件。

##### 3.5.4.2. 创建表格存储Tablestore维表

本文为您介绍如何创建实时计算Flink版表格存储Tablestore维表。 本文仅适用于Blink 1.4.5及以上版本。

**重要**

**什么是表格存储Tablestore**

表格存储Tablestore是构建在阿里云飞天分布式系统之上的分布式NoSQL数据存储服务。表格存储通过数据分片和负载均衡技术，实现数据规模与访问并发上的无缝扩展， 提供海量结构化数据的存储和实时访问服务。

**示例**

实时计算Flink版支持表格存储Tablestore作为维表，示例如下。

```
CREATE TABLE ots_dim_table (
 id int,
 len int,
 content VARCHAR,
 PRIMARY KEY (id),
```

`PERIOD FOR SYSTEM_TIME--`定义了维表的变化周期。

```
) WITH (
 type='ots',
 endPoint='<yourEndpoint>',
 instanceName='<yourInstanceName>',
 tableName='<yourTableName>',
 accessId='<yourAccessId>',
 accessKey='<yourAccessKey>'
);
```

**说明**

在声明维表时，必须要指名主键。 在维表JOIN时，ON条件必须包含所有主键的等值条件。 Tablestore的主键即表的Rowkey。

**WITH参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| type | 维表类型 | 固定值为 ots 。 |
| endPoint | 表格存储的实例访问地址 | 请联系阿里云运维工程师获取。 |
| instanceName | 表格存储的实例名称 | 无 |
| tableName | 表格存储的数据表名 | 无 |
| accessId | 表格存储读取的AccessKey ID | 无 |
| accessKey | 表格存储读取的密钥AccessKey Secret | 无 |

**CACHE参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| cache | 缓存策略 | 表格存储维表支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表来一条数据，系统会先查找Cache，如果没有找到，则去物理维表中查询。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 |
| cacheSize | 缓存大小 | 当选择LRU缓存策略后，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存超时时间，单位为毫秒。 | 当选择LRU缓存策略后，可以设置缓存失效的超时时间。 |

**代码示例**

实时计算（流计算）

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH ( type='datahub' ); CREATE TABLE phoneNumber( name VARCHAR, phoneNumber bigint, primary key(name),
```

`PERIOD FOR SYSTEM_TIME--`维表标识。

```
)with( type='ots' ); CREATE TABLE result_infor( id bigint, phoneNumber bigint, name VARCHAR )with( type='rds' ); INSERT INTO result_infor t.id, w.phoneNumber, t.name FROM datahub_input1 as t
```

`JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w --`维表`JOIN`时必须指定此声明。

```
ON t.name = w.name;
```

##### 3.5.4.3. 创建云数据库HBase版维表

本文为您介绍如何创建实时计算云数据库HBase版维表，以及创建维表时使用的WITH参数和CACHE参数。

**重要**

Blink 3.3.0以下版本仅支持HBase企业标准版。 Blink 3.3.0及以上版本同时支持HBase企业标准版和HBase性能增强版。 Blink 3.5.0及以上版本支持HBase写入主备切换。 实时计算HBase维表不支持自建的开源HBase。 HBase维表仅支持一个PK（Primary Key）。

**DDL定义**

HBase企业标准版

```
CREATE TABLE hbase (
  `key` varchar,
  `name` varchar,
  PRIMARY KEY (`key`), --HBase中的rowkey字段。
```

`PERIOD FOR SYSTEM_TIME --`维表标识。

```
) with (
  TYPE = 'cloudhbase',
  zkQuorum = '<yourzkQuorum>',
  columnFamily = '<yourColumnFamilyName>',
  tableName = '<yourTableName>'
);
```

HBase性能增强版

```
CREATE TABLE hbase (
  `key` varchar,
  `name` varchar,
  PRIMARY KEY (`key`), --HBase中的rowkey字段。
```

`PERIOD FOR SYSTEM_TIME --`维表标识。

```
) with (
  TYPE = 'cloudhbase',
```

`endPoint = '<host:port>',--HBase`增强版的`Java API`访问地址。

```
  userName  = 'root', --HBase用户名。
  password = 'root', --HBase密码。
  columnFamily = '<yourColumnFamilyName>',
  tableName = '<yourTableName>'
);
```

Blink-3.5.0以上HBase性能增强版实时计算（流计算）

```
create table liuxd_user_behavior_test_front (
  row_key varchar,
  from_topic varchar,
  origin_data varchar,
  record_create_time varchar,
  primary key (row_key)
) with (
  type = 'cloudhbase',
```

`zkQuorum = '<host:port>', --HBase`增强版的`Java API`访问地址。

```
  userName  = 'root', --HBase用户名。
  password = 'root', --HBase密码。
  columnFamily = '<yourColumnFamily>',
  tableName = '<yourTableName>',
  batchSize = '500'
);
```

Blink-3.5.0以上支持HBase写入主备切换

```
create table liuxd_user_behavior_test_front (
  row_key varchar,
  from_topic varchar,
  origin_data varchar,
  record_create_time varchar,
  primary key (row_key)
) with (
  type = 'cloudhbase',
```

`zkQuorum = '<host:port>', --HBase`高可用访问地址。

```
  userName  = 'root', --HBase用户名。
  password = 'root', --HBase密码。
  columnFamily = '<yourColumnFamily>',
  tableName = '<yourTableName>',
  batchSize = '500'
);
```

**说明**

在声明维表时，必须要指名主键。 在维表进行JOIN时，ON的条件必须包含所有主键的等值条件。示例中HBase中的主键是**row_key**。 HBase企业标准版和HBase性能增强版DDL的区别为连接参数不同：

| zkQuorum |  |
|---|---|
| endPoint |  |
|  | zkQuorum |

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 维表类型 | 是 | 固定值为 cloudhbase 。 |
| zkQuorum | HBase集群配置的zk地址，是以逗号 （,）分隔的主机列表。 | 是 | 可以在hbase-site.xml文件中查看hbase.zookeeper.quorum相关配置。 说明仅在HBase企业标准版中生效。 |
| zkNodeParent | 集群配置在zk上的路径 | 否 | 可以在hbase-site.xml文件中查看hbase.zookeeper.quorum相关配置。 说明仅在HBase企业标准版中生效。 |
| endPoint | HBase地域名称 | 是 | 可在购买的HBase实例控制台中获取。 说明仅在HBase性能增强版中生效。 |
| userName | 用户名 | 否 | 说明仅在HBase性能增强版中生效。 |
| password | 密码 | 否 | 说明仅在HBase性能增强版中生效。 |
| tableName | HBase表名 | 是 | 无 |
| columnFamily | 列族名 | 是 | 仅支持插入同一列族。 |
| maxRetryTimes | 最大尝试次数 | 否 | 默认值为10次。 |
| partitionedJoin | 是否使用joinKey进行分区。 | 否 | 默认值为False。在设置partitionedJoin为True时，使用joinKey进行分区，将数据分发到各JOIN节点，提高缓存命中率。 |
| shuffleEmptyKey | 是否将上游EMPTY KEY随机发送到下游节点。 | 否 | 默认值为True。参数取值如下： True：如果上游有多个EMPTY KEY，会将所有EMPTY KEY随机发送到各个JOIN节点。 False：如果上游有多个EMPTY KEY，会将所有EMPTY KEY发送至一个JOIN节点。 说明 shuffleEmptyKey在partitionedJoin生效后才能使用。 |

**CACHE参数**

实时计算（流计算）

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | HBase维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔 （cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到 Cache中，之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔（cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
| cacheSize | 缓存大小 | 否 | 当选择 LRU 缓存策略后，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存超时时间，单位为毫秒。 | 否 | 当选择 LRU 缓存策略后，可以设置缓存失效的超时时间，默认不过期。当选择 ALL 策略，则为缓存加载的间隔时间，默认不重新加载。 |
| cacheReloadTimeBlackList | 缓存策略选择 ALL 时启用。更新时间黑名单，防止在此时间内做Cache更新 （例如双11场景）。 | 否 | 默认为空。自定义输入格式如下。 2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00 使用逗号（,）分隔多个黑名单，使用箭头（->）分割黑名单的起始和结束时间。 |
| cacheScanLimit | 缓存策略选择 ALL 时启用。读取全量 HBase数据，服务端一次RPC返回给客户端的行数。 | 否 | 默认值为100条。 |

**代码示例**

包含HBase维表的实时计算作业代码示例如下。

```
create table source (
  id   TINYINT,
  name BIGINT
) with (
  type = 'random'
); create table dim (
  id   TINYINT,
  score BIGINT
  primary key(id),
  PERIOD FOR SYSTEM_TIME
)with(
  type = 'cloudhbase',
  zkQuorum = '<yourzkQuorum>',
  columnFamily = '<yourColumnFamilyName>',
  tableName = '<yourTableName>'
); CREATE table result_infor(
  id BIGINT,
  score BIGINT
)with(
  type='rds'
); INSERT INTO result_infor
  t.id,
  w.score
FROM source as t JOIN dim FOR SYSTEM_TIME AS OF PROCTIME() as w ON t.id = w.id;
```

##### 3.5.4.4. 创建云数据库Redis维表

本文为您介绍如何创建云数据库Redis维表，以及创建过程中涉及的WITH参数、CACHE参数、类型映射和代码示例。

**重要**

本文仅适用于Blink 3.2.2及以上版本。 实时计算Flink版Redis维表仅支持引用Redis数据存储中STRING类型的数据。 实时计算Flink版Redis维表支持自建Redis服务。

**语法示例**

实时计算Flink版支持使用Redis作为数据存储维表。Redis维表语法示例如下。 实时计算（流计算）

```
CREATE TABLE white_list (
  id VARCHAR,
  name VARCHAR,
  PRIMARY KEY (id),  --Redis中的Row Key字段。
```

`PERIOD FOR SYSTEM_TIME --`维表标识。

```
) WITH (
  type = 'redis',
  host = '<yourHostName>',
  port = '<yourPort>',
  password = '<yourPassword>',
  dbNum = '<yourDatabaseNumber>'
);
```

**说明**

Redis维表必须声明且只能声明一个主键。 维表JOIN时，ON条件必须包含所有主键的等值条件。 Redis维表仅支持声明两个字段，且字段类型必须为VARCHAR。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |  |  |
|---|---|---|---|---|---|
| type | 维表类型 | 是 | 固定值为 redis 。 |  |  |
| host | Redis连接地址 | 是 | 无 |  |  |
| port | Redis连接端口 | 否 | 默认值为6379。 |  |  |
| dbNum | 选择操作的数据库 | 否 | 默认值为0。 |  |  |
| password | Redis密码 | 否 | 默认值为空，不进行权限验证。 |  |  |
| hashName | Hash模式下的Hash Key名称 | 否 | 默认值为空，实时计算Flink版从Redis中读取STRING类型的数据。 通常，Redis维表中的数据类型为STRING类型，即 key-value 对。如果设置hashName参数，则Redis维表中的数据类型为HASHMAP类型，即 key- {field-value} 对，其中： key为hashName参数值。 field为您在CREATE TABLE中指明的key参数值。 value为key对应的赋值，和STRING类型 key-value 中value语义相同。 |  |  |
|  |  |  |  | key- |  |

|  | {field-value} |
|---|---|

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | 云数据库Redis维表支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表来一条数据，系统会先查找Cache，如果没有找到，则去物理维表中查询。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 |
| cacheSize | 缓存大小 | 否 | 选择 LRU 缓存策略后，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存超时时长 | 否 | 默认缓存不超时，单位为毫秒。可选LRU缓存策略，即设置缓存失效的超时时长。 |
| cacheEmpty | 是否缓存空结果 | 否 | 默认值为true。 |

**类型映射**

Redis和实时计算Flink版字段类型对应关系如下。建议您使用该对应关系进行DDL声明。

| Redis字段类型 | 实时计算Flink版字段类型 |
|---|---|
| STRING | VARCHAR |

**代码示例**

包含Redis维表的实时计算Flink版作业代码示例如下。 实时计算（流计算）

```
CREATE TABLE event (
  id VARCHAR,
  data VARCHAR) with (
  type = 'random'
); CREATE TABLE white_list (
  id VARCHAR,
  name VARCHAR,
  PRIMARY KEY (id),  --Redis中的Row Key字段。
```

`PERIOD FOR SYSTEM_TIME --`维表的标识。

```
) WITH (
  type = 'redis',
  host = '<yourRedisHost>',
  password = '<yourRedisPassword>'
); SELECT e.*, w.* FROM event AS e JOIN white_list FOR SYSTEM_TIME AS OF PROCTIME() AS w ON e.id = w.id;
```

##### 3.5.4.5. 创建云数据库RDS MySQL版维表

本文为您介绍如何创建实时计算云数据库RDS MySQL版维表，以及创建维表时使用的WITH参数、CACHE参数和类型映射。 RDS MySQL基于阿里巴巴的MySQL源码分支，经过双十一高并发、大数据量的考验，拥有优良的性能。RDS MySQL支持实例管理、账号管理、数据库管理、备份恢复、白名单、透明数据加密以及数据迁移等基本功能。

**使用限制**

实时计算Flink版暂不支持通过数据存储功能中存储注册的方式使用RDS MySQL 8.0版本，建议您使用明文方式使用RDS MySQL 8.0版本。数据存储功能详情请参见概述。

**语法示例**

实时计算Flink版支持使用RDS MySQL版作为维表，示例代码如下。

```
CREATE TABLE rds_dim_table(
 id INT,
 len INT,
 content VARCHAR,
 PRIMARY KEY (id),
```

`PERIOD FOR SYSTEM_TIME --`定义维表的变化周期。

```
) with (
 type='rds',
 url='<yourDatabaseURL>',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
);
```

**说明**

声明维表时，必须要指名主键。维表JOIN时，ON条件必须包含所有主键的等值条件。RDS或DRDS的主键可以定义为表的主键或唯一索引列。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 维表类型 | 是 | 固定值为 rds 。 |
| url | JDBC（Java DataBase Connectivity）连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| tableName | 表名 | 是 | 无 |
| userName | 用户名 | 是 | 无 |
| password | 密码 | 是 | 无 |
| maxRetryTim es | 最大尝试连接次数 | 否 | 默认值为10。 |

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|

实时计算（流计算）

| cache | 缓存策略 | 否 | 云数据库RDS（DRDS）版维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔（cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |  |
|---|---|---|---|---|
| cacheSize | 缓存大小 | 否 | 当选择 LRU 缓存策略后，可以设置缓存大小，默认10000行。 |  |
| cacheTTLMs | 缓存超时时间，单位为毫秒 | 否 | 当选择 LRU 缓存策略后，可以设置缓存失效的超时时间，默认不过期。当选择 ALL 策略，则为缓存加载的间隔时间，默认不重新加载。 |  |
| cacheReload | 缓存策略选择 ALL 时启用。更 |  | 默认为空。自定义输入格式为 2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00 。用逗号（,）来分隔多个黑名单，用箭头（->）来分割黑名单的起始结束时间。 |  |
| TimeBlackLis t | 新时间黑名单，防止在此时间内做 cache更新（例如双11场景）。 | 否 | 2017-11-11 08:00 |  |
| maxJoinRows | 主表中每一条数据查询维表时，匹配后最多返回的结果数。 | 否 | 默认值为1024。如果您可以预估一条数据对应的维表数据最多为n条，则可以设置maxJoinRows='n'，以确保实时计算匹配处理效率。 说明进行Join时，主表输入一条数据，对应维表匹配后返回的结果总数受该参数限制。 |  |

**说明**

CACHE底层原理请参见维表JOIN 与异步优化。

**代码示例**

包含云数据库RDS版维表的实时计算Flink版作业代码示例如下。

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyun-inc.com',
  project='<yourProjectName>',
  topic='<yourTopic>',
  accessId='<yourAccessID>',
  accessKey='<yourAccessSecret>',
  startTime='2017-07-21 00:00:00'
); create table phoneNumber( name VARCHAR, phoneNumber BIGINT, primary key(name),
```

`PERIOD FOR SYSTEM_TIME--`定义维表的变化周期。

```
)WITH(
 type='rds'，
 url='<yourDatabaseURL>',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
); CREATE table result_infor( id BIGINT, phoneNumber BIGINT, name VARCHAR )WITH(
 type='rds'，
 url='<yourDatabaseURL>',
 tableName='<yourDatabaseTableName>',
 userName='<yourDatabaseUserName>',
 password='<yourDatabasePassword>'
); INSERT INTO result_infor t.id, w.phoneNumber, t.name FROM datahub_input1 as t
```

`JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w --`维表`JOIN`时必须指定此声明。

```
ON t.name = w.name;
```

实时计算（流计算）

**类型映射**

| RDS字段类型 | 实时计算Flink版字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARBINARY | VARBINARY |

##### 3.5.4.6. 创建MaxCompute维表

本文为您介绍如何创建实时计算Flink版MaxCompute维表，以及创建维表时使用的WITH参数、CACHE参数和类型映射。

**重要**

Blink 2.1.1及以上版本支持MaxCompute维表。 使用MaxCompute表作为维表，需要先赋予MaxCompute账号读权限。

**DDL定义**

```
CREATE TABLE white_list (
  id varchar,
  name varchar,
  age int,
  PRIMARY KEY (id),
```

`PERIOD FOR SYSTEM_TIME --`维表的标识。

```
) WITH (
  type = 'odps',
  endPoint = '<YourEndPoint>',
  project = '<YourProjectName>',
  tableName = '<YourtableName>',
  accessId = '<yourAccessKeyId>',
  accessKey = '<yourAccessKeySecret>',
  `partition` = 'ds=2018****',
  cache = 'ALL'
);
```

**说明**

声明维表时，必须要指名主键，MaxCompute维表主键必须具有唯一性，否则会被去重。 在维表进行JOIN时，ON条件必须包含所有主键的等值条件。 partition是关键字，需要使用反引号（`）注释，例如 `partition` 。 如果是分区表，目前不支持将分区列写入到DDL定义中。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 维表类型 | 是 | 固定值为 odps 。 |
| endPoint | MaxCompute服务地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoint | MaxCompute Tunnel服务的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | MaxCompute项目名称 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |

实时计算（流计算）

| partition | 分区名 | 否 | 固定分区只存在一个分区MaxCompute表例如，如果只存在1个分区列 ds ，则 `partition` = 'ds=20180905' 表示读 ds=20180905 分区的数据。 存在多个分区的MaxCompute表例如，如果存在2个分区列 ds 和 hh ，则 `partition`='ds=20180905,hh=*' 表示读 ds=20180905 分区的数据。 说明分区过滤时需要声明所有分区的值。例如，上述示例中，只声明 `partition` = 'ds=20180905' ，则不会读取任何分区。 非固定分区 Blink 2.2.0及以上版本支持 `partition` = 'max_pt()' 功能， 即每次加载所有分区列表中字典序最大的分区。 Blink 3.2.2及以上版本支持 `partition` = 'max_pt_with_done()' 功能，即每次加载所有分区列表中字典序最大且伴随有 .done 的分区。 |
|---|---|---|---|
| maxRowCount | 可加载的最大表格数量 | 否 | 默认值为100000。 说明如果您的数据超过100000，需要设置maxRowCount参数。建议设定值比实际值大。 |

**CACHE参数**

| 参数 | 说明 | 备注 |  |  |
|---|---|---|---|---|
| cache | 缓存策略 | 目前MaxCompute维表仅支持 ALL 策略，必须显式声明。 ALL策略：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查询都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。需要配置缓存更新时间间隔（cacheTTLMs）和更新时间黑名单（cacheReloadTimeBlackList）参数。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的至少4倍，具体值与MaxCompute存储压缩算法有关。 在使用超大MaxCompute维表时，如果频繁GC（Allocation Failure）导致作业异常，且在增加维表JOIN节点的内存仍无改善的情况下，建议： Blink 3.6.0及以后版本，设置参数partitionedJoin = 'true' ，即打开 PartitionedJoin优化。 改为支持LRU 缓存策略的KV型维表，例如云数据库Hbase版维表。 |  |  |
| cacheSize | 缓存大小 | 可以设置缓存大小，MaxCompute默认缓存值为100000行。 |  |  |
| cacheTTLMs | 缓存超时时间 | 单位为毫秒，当cache选择为 ALL 策略，则为缓存加载的间隔时间，默认为不重新加载。 |  |  |
|  |  | 默认为空，格式为 2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017- 11-11 08:00 。分隔符的使用情况如下所示： 用逗号 , 来分隔多个黑名单。 用箭头 -> 来分割黑名单的起始结束时间。 |  |  |
| cacheReloadTimeBla | 更新时间黑名单。在缓存策略选择为ALL时，启用更 | 11-11 08:00 |  |  |
| ckList | 新时间黑名单，防止在此时间内做Cache更新（例如双11场景）。 |  | , 来 |  |
|  |  |  | -> |  |
| partitionedJoin | 当开启PartitionedJoin优化时，每个并发内存里只缓存维表的部分数据，即该并发上需要的缓存数据。 | 可选，默认值为false，表示每个并发内存里缓存全量维表数据。 |  |  |

**代码示例**

包含MaxCompute维表的实时计算Flink版作业代码示例如下。 实时计算（流计算）

```
CREATE TABLE datahub_input1 (
   id    BIGINT,
   name  VARCHAR,
   age   BIGINT
) with (
   type='datahub'
); CREATE TABLE odps_dim (
   name VARCHAR,
   phoneNumber BIGINT,
   PRIMARY KEY (name),
```

`PERIOD FOR SYSTEM_TIME --`维表的标识。

```
) with (
   type = 'odps',
   endPoint = '<yourEndpointName>',
   project = '<yourProjectName>',
   tableName = '<yourTableName>',
   accessId = '<yourAccessId>',
   accessKey = '<yourAccessPassword>',
```

`partition` = 'ds=20180905',--动态分区、固定分区请参考`WITH`参数说明。

```
  cache = 'ALL'
); CREATE table result_infor(
  id BIGINT,
  phoneNumber BIGINT,
  name VARCHAR
)with(
  type='print'
); INSERT INTO result_infor
  t.id,
  w.phoneNumber,
  t.name
FROM datahub_input1 as t
```

`JOIN odps_dim FOR SYSTEM_TIME AS OF PROCTIME() as w --`维表`JOIN`时必须指定此声明。

```
ON t.name = w.name;
```

**类型映射**

MaxCompute和Flink全托管字段类型对应关系如下，建议使用该对应关系时进行DDL声明。

| MaxCompute | BLINK |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |
| STRING | VARCHAR |

实时计算Flink版MaxCompute维表仅支持上述MaxCompute字段类型。

**说明**

##### 3.5.4.7. 创建分析型数据库MySQL版3.0维表

本文为您介绍如何创建分析型数据库MySQL版3.0维表、以及创建维表时使用的WITH参数和CACHE参数。 本文仅适用于**Blink-3.5.0-hotfix**及以上版本。

**重要**

**语法示例**

实时计算（流计算）

```
CREATE TABLE dim_ads(
    `name` VARCHAR,
    id VARCHAR,
    PRIMARY KEY (`name`),
    PERIOD FOR SYSTEM_TIME
)with(
    type='ADB30',
    url='jdbc:mysql://<内网地址>/<databaseName>',
    tableName='xxx',
    userName='xxx',
    password='xxx'
);
```

**说明**

在声明一个维表时，必须指明主键。 在维表进行JOIN时，ON条件必须包含所有主键的等值条件。 分析型数据库MySQL版的主键可以定义为表的主键或唯一索引列。

**WITH参数**

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| type | 维表类型 | 是 | 固定值为ADB30。 |
| url | 分析型数据库MySQL版数据库地址 | 是 | 请联系阿里云运维工程师获取。 |
| tableName | 表名 | 是 | 无 |
| userName | 用户名 | 是 | 无 |
| password | 密码 | 是 | 无 |
| maxRetryTimes | 写入重试次数。 | 否 | 默认值为3。 |

**CACHE参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| cache | 缓存策略 | 目前分析型数据库MySQL版3.0支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表来一条数据，系统会先查找Cache，如果没有找到，则去物理维表中查询。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查询都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔（cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 对于数据量比较大的维表，选择CACHE ALL时，可能会出现OOM或者Full GC耗时很久的情况，针对这个问题，可以选择以下两种解决方式： 对于支持Cache All策略的维表，开启PartitionedJoin优化。3.6.0版本之前，每个并发默认加载维表全量数据。3.6.0版本之后，CACHE ALL策略支持PartitionedJoin优化。开启PartitionJoin优化后，每个并发只缓存自己并发所需要的数据。 使用HBase或者RDS等Key-Value类型的维表。 |
| cacheSize | 缓存大小 | 当选择LRU缓存策略后，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存更新时间间隔。系统会根据您设置的缓存更新时间间隔，重新加载一次维表中的最新数据，保证源表能JOIN到维表的最新数据。 | 单位为毫秒。默认不设置此参数，表示不重新加载维表中的新数据。 |
| cacheReloadTimeBla ckList | 更新时间黑名单。在缓存策略选择为ALL时，启用更新时间黑名单，防止在此时间内做Cache更新（例如双11场景）。 | 可选，默认空，格式为 '2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00' 。其中分割符使用情况如下： 用逗号（,）来分隔多个黑名单。 用箭头（->）来分割黑名单的起始结束时间。 |
| partitionedJoin | 是否开启partitionedJoin。在开启partitionedJoin 优化时，主表会在关联维表前，先按照Join KEY进行 Shuffle，这样做有以下优点： 在缓存策略为LRU时，可以提高缓存命中率。 在缓存策略为ALL时，节省内存资源，因为每个并发只缓存自己并发所需要的数据。 | 默认情况下为false，表示不开启partitionedJoin。 说明使用partitionedJoin优化前，需要您手动设置partitionedJoin = 'true'。 |

**代码示例**

实时计算（流计算）

```
CREATE TABLE datahub_input1 (
  id      BIGINT,
  name    VARCHAR,
  age     BIGINT
) WITH (
  type='datahub'
); create table phoneNumber (
  name VARCHAR,
  phoneNumber BIGINT,
  primary key(name),
```

`PERIOD FOR SYSTEM_TIME--`维表标识。

```
) with (
  type='ADB30'
); CREATE table result_infor (
  id BIGINT,
  phoneNumber BIGINT,
  name VARCHAR
) with (
  type='rds'
); INSERT INTO result_infor
  t.id,
  w.phoneNumber,
  t.name
FROM datahub_input1 as t
```

`JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w --`维表`JOIN`时必须指定该声明。

```
ON t.name = w.name;
```

##### 3.5.4.8. 创建交互式分析Hologres维表

本文为您介绍如何创建交互式分析Hologres维表，以及创建维表时使用的WITH参数、CACHE参数和类型映射。

**重要**

本文仅适用于Blink 3.6.0及以上版本。如果您的Blink为3.6.0以下的版本，您可以提交工单获取需要的JAR文件，安装使用。 建议您使用Hologres 0.7及以上版本。

**什么是交互式分析Hologres**

交互式分析Hologres是实时交互分析产品，兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析与处理PB级数据，让您轻松使用现有 BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**语法示例**

实时计算Flink版支持使用Hologres作为维表，代码示例如下。

```
CREATE TABLE rds_dim_table(
  id INT,
  len INT,
  content VARCHAR,
  PRIMARY KEY (id),
```

`PERIOD FOR SYSTEM_TIME --`定义维表的变化周期。

```
) with (
  type='hologres',
  endpoint='...',
  dbname='...',
  tablename='...',
  username='...',
  password='...'
);
```

**WITH参数**

| 参数 | 描述 | 是否必选 | 备注 |
|---|---|---|---|
| type | 数据库类型 | 是 | 固定值为hologres。 |
| endpoint | Hologres端点 | 是 | 无 |
| tablename | 读取的表 | 是 | 无 |
| dbname | 读取的数据库 | 是 | 无 |
| username | 用户名 | 是 | 无 |
| password | 密码 | 是 | 无 |

**CACHE参数**

| 参数 | 描述 | 是否必选 | 示例值 |
|---|---|---|---|

实时计算（流计算）

| cache | 缓存策略 | 否 | 目前交互式分析Hologres维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中， 之后所有的维表查找数据都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔（cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN 节点的内存，增加的内存大小为远程表数据量的两倍。 对于数据量比较大的维表，选择CACHE ALL时，可能会出现OOM或者Full GC 耗时很久的情况，针对这个问题，可以选择以下两种解决方式： 对于支持Cache All策略的维表，开启PartitionedJoin优化。3.6.0版本之前，每个并发默认加载维表全量数据；3.6.0版本之后，CACHE ALL策略支持PartitionedJoin优化。开启PartitionJoin优化后，每个并发只缓存自己并发所需要的数据。 使用HBase或者RDS等Key-Value类型的维表。 |
|---|---|---|---|
| cacheSize | 缓存大小 | 否 | 当缓存策略选择LRU时，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存失效时间，单位为毫秒 | 否 | 当缓存策略选择LRU时，可以设置缓存失效时间，默认不过期。 当缓存策略选择ALL时，缓存失效时间为缓存重新加载的间隔时间，默认不重新加载。 |
| partitionedJoin | 根据分区查找数据 | 否 | partitionedJoin参数的取值如下： false（默认值） true |
| async | 是否异步读取数据 | 否 | async参数的取值如下： false（默认值） true |

**类型映射**

| Hologres字段类型 | 实时计算Flink版字段类型 |
|---|---|
| INT | INT |
| INT[] | ARRAY<INT> |
| BIGINT | BIGINT |
| BIGINT[] | ARRAY<BIGINT> |
| REAL | FLOAT |
| REAL[] | ARRAY<FLOAT> |
| DOUBLE PRECISION | DOUBLE |
| DOUBLE PRECISION[] | ARRAY<DOUBLE> |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY<BOOLEAN> |
| TEXT | VARCHAR |
| TEXT[] | ARRAY<VARCHAR> |
| NUMERIC | DECIMAL |
| DATE | DATE |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

**代码示例**

实时计算Flink版包含Hologres维表的代码示例如下。 实时计算（流计算）

```
create table randomSource (a int, b VARCHAR, c VARCHAR) with (type = 'random'); create table test (
   a int,
   b VARCHAR,
   c VARCHAR,
   PRIMARY KEY (a, b), PERIOD FOR SYSTEM_TIME
) with (
   type = 'hologres',
   ...
); create table print_sink (
  a int,
  b VARCHAR
) with (
  type = 'print',
  `ignoreWrite` = 'false'
); insert into print_sink select randomSource.a, test.b from randomSource LEFT JOIN test FOR SYSTEM_TIME AS OF PROCTIME() on randomSource.a = test.a and randomSource.b = test.b;
```

##### 3.5.4.9. 创建Phoenix5维表

本文为您介绍如何创建实时计算Flink版Phoenix5维表，以及创建维表时使用的WITH参数和CACHE参数。 仅Blink 3.4.0以上版本支持Phoenix5维表。

**重要**

**语法示例**

```
create table US_POPULATION_DIM (
  `STATE` varchar,
  CITY varchar,
  POPULATION BIGINT,
  PRIMARY KEY (`STATE`, CITY),
  PERIOD FOR SYSTEM_TIME
) WITH (
  type = 'PHOENIX5',
  serverUrl = '<YourServerUrl>',
  tableName = '<YourTableName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| type | 维表类型 | 是 | 固定值为 PHOENIX5 。 |
| serverUrl | Phoenix5的Query Server地址： 如果Phoenix5是在集群中创建的，则serverUrl是负载均衡服务的URL地址。 如果Phoenix5是在单机中创建的，则serverUrl是单机的URL地址。 | 是 | 您需要在云数据库HBase实例中开启Hbase SQL服务。 serverUrl格式为http://host:port，其中： host：Phoenix5服务的域名。 port：Phoenix5服务的端口号，固定值为8765。 |
| tableName | Phoenix5表名 | 是 | Phoenix5表名格式为SchemaName.TableName，其中： SchemaName：模式名，可以为空，即不写模式名，仅写表名，表示使用数据库的默认模式。 TableName：表名。 |

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | 目前Phoenix5维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中， 之后所有的维表查询都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在， 并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔（cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表 JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |

实时计算（流计算）

| cacheSize | 缓存大小 | 否 | 选择LRU缓存策略后，可以设置缓存大小，默认为10000行。 |
|---|---|---|---|
| cacheTTLMs | 缓存超时时间，单位为毫秒。 | 否 | 当选择LRU缓存策略后，可以设置缓存失效的超时时间，默认不过期。当选择ALL策略，则为缓存加载的间隔时间，默认不重新加载。 |
| cacheReloadTime BlackList | 更新时间黑名单。在缓存策略选择为ALL时， 启用更新时间黑名单，防止在此时间内做 Cache更新（例如双11场景）。 | 否 | 可选，默认空，格式为 '2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00'。用逗号（,）来分隔多个黑名单，用箭头（->）来分割黑名单的起始或结束时间。 |

**代码示例**

```
CREATE TABLE datahub_input1 (
  id  BIGINT,
  name  VARCHAR,
  age   BIGINT
) WITH (
  type='datahub'
); create table phoneNumber(
  name VARCHAR,
  phoneNumber BIGINT,
  primary key(name),
```

`PERIOD FOR SYSTEM_TIME--`定义维表的变化周期。

```
)with(
  type='PHOENIX5'
); CREATE table result_infor(
  id BIGINT,
  phoneNumber BIGINT,
  name VARCHAR
)with(
  type='rds'
); INSERT INTO result_infor
  t.id,
  w.phoneNumber,
  t.name
FROM datahub_input1 as t
```

`JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w --`维表`JOIN`时必须指定该声明。

```
ON t.name = w.name;
```

##### 3.5.4.10. 创建Elasticsearch维表

本文为您介绍如何创建实时计算Flink版Elasticsearch（ES）维表，以及创建维表时使用的WITH参数和CACHE参数。 本文仅适用于Blink 3.2.2及以上版本。

**重要**

**DDL定义**

实时计算Flink版支持使用ES作为维表，示例代码如下。

```
 CREATE TABLE es_stream_sink(
  field1 LONG,
  field2 VARBINARY,
  field3 VARCHAR,
  PRIMARY KEY(field1),
  PERIOD FOR SYSTEM_TIME
) WITH (
  type ='elasticsearch',
  endPoint = '<yourEndPoint>',
  accessId = '<yourAccessId>',
  accessKey = '<yourAccessSecret>',
  index = '<yourIndex>',
  typeName = '<yourTypeName>'
);
```

**说明**

ES维表支持根据ES的PRIMARY KEY进行PRIMARY KEYUPDATE，且PRIMARY KEY只能为1个字段。

**WITH参数**

| 参数 | 说明 | 默认值 | 是否必选 |
|---|---|---|---|
| type | 维表类型 | elasticsearch | 是 |
| endPoint | Server地址，例如：http://127.0.0.1:9211。 | 无 | 是 |
| accessId | 访问实例ID | 无 | 是 |
| accessKey | 访问实例密钥 | 无 | 是 |
| index | 索引名称，类似于数据库Database的名称。 | 无 | 是 |

实时计算（流计算）

| typeName | Type名称，类似于数据库的Table名称。 | 无 | 是 |
|---|---|---|---|
| maxRetryTimes | 异常重试次数 | 30 | 否 |
| timeout | 读取超时时长，单位为毫秒。 | 600000 | 否 |
| discovery | 是否开启节点发现。如果开启，客户端每5分钟刷新一次Server List。 | false | 否 |
| compression | 是否使用GZIP压缩Request Bodies。 | true | 否 |
| multiThread | 是否开启JestClient多线程。 | true | 否 |

**CACHE参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| cache | 缓存策略 | None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表来一条数据，系统会先查找Cache，如果没有找到，则去物理维表中查询。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中， 之后所有的维表查询都会通过Cache进行。如果在Cache中无法找到数据，则KEY不存在， 并在Cache过期后重新加载一遍全量Cache。 |
| cacheSize | 缓存大小 | 选择 LRU 缓存策略后，可以设置缓存大小，默认为10000行。 |
| cacheTTLMs | 缓存更新时间间隔 | 默认缓存不超时，单位为毫秒。不同缓存策略下的功能如下： LRU：设置缓存失效的超时时长。 ALL：设置缓存加载的间隔时长，默认不重新加载。 |

### DML语句

#### 3.6.1. INSERT INTO语句

**语法**

```
INSERT INTO tableName
        [ (columnName[ , columnName]*) ]
            queryStatement;
```

**示例**

```
INSERT INTO LargeOrders SELECT * FROM Orders WHERE units > 1000; INSERT INTO Orders(z, v) SELECT c,d FROM OO;
```

单个实时计算作业支持在一个SQL作业里面包含多个DML操作，同样也允许包含多个数据源、多个数据目标端、多个维表。例如，在一个作业文件里面包含两段完全业务上独立的SQL，分别写出到不同的数据目标端。 实时计算不支持单独的select查询，必须有create view或这是在insert into内才能操作。 insert into支持update更新。例如，向RDS的表插入一个key值，如果这个key值存在就会更新；如果不存在就会插入一条新的key值。

**操作约束**

| 表类型 | 操作约束 |
|---|---|
| 源表 | 只能引用（from），不可执行insert。 |
| 维表 | 只能引用（join），不可执行insert。 |
| 结果表 | 仅支持insert操作 |
| 视图 | 只能引用（from） |

### QUERY语句

#### 3.7.1. SELECT语句

**语法**

```
SELECT [ DISTINCT ] FROM tableExpression;
```

**测试数据**

| a（VARCHAR） | b（INT） | c（DATE） |
|---|---|---|

实时计算（流计算）

| a1 | 211 | 1990-02-20 |
|---|---|---|
| b1 | 120 | 2018-05-12 |
| c1 | 89 | 2010-06-14 |
| a1 | 46 | 2016-04-05 |

**简单查询**

测试语句 `SELECT * FROM` 表名； 测试结果

| a（VARCHAR） | b（INT） | c（DATE） |
|---|---|---|
| a1 | 211 | 1990-02-20 |
| b1 | 120 | 2018-05-12 |
| c1 | 89 | 2010-06-14 |
| a1 | 46 | 2016-04-05 |

**重命名查询**

测试语句

```
SELECT a, c AS d FROM 表名；
```

测试结果

| a（VARCHAR） | d（DATE） |
|---|---|
| a1 | 1990-02-20 |
| b1 | 2018-05-12 |
| c1 | 2010-06-14 |
| a1 | 2016-04-05 |

**去重查询**

测试语句

```
SELECT DISTINCT a FROM 表名；
```

测试结果

**a（VARCHAR）**

a1 b1 c1

**子查询**

| 普通的SELECT是从几张表中读数据，例如 | SELECT column_1, column_2 … FROM table_name | ，但查询的对象也可以是另外一个SELECT操作。 |
|---|---|---|
| 说明当查询的对象是另一个SELECT操作时，必须为子查询加别名。 |  |  |

测试语句

```
INSERT INTO result_table SELECT * FROM
               (SELECT   t.a,
                         sum(t.b) AS sum_b
                FROM     t1 t
                GROUP BY t.a
               ) t1
WHERE t1.sum_b > 100;
```

测试结果

| a（VARCHAR） | b（INT） |
|---|---|
| a1 | 211 |
| b1 | 120 |
| a1 | 257 |

此结果为调试结果，会显示出计算过程。如果您的结果表是DataHub、消息队列Kafka或消息队列MQ等，正式上线也会显示过程数据。但如果您的结果

**说明**

表是云数据RDS等关系型数据库，正式上线，主键相同的记录显示为一条数据。 实时计算（流计算）

#### 3.7.2. WHERE语句

**语法**

```
SELECT [ ALL | DISTINCT ] FROM tableExpression [ WHERE booleanExpression ];
```

| 操作符 | 描述 |
|---|---|
| = | 等于 |
| <> | 不等于 |
| > | 大于 |
| >= | 大于等于 |
| < | 小于 |
| <= | 小于等于 |

**示例**

测试数据

| Address | City |
|---|---|
| Oxford Street | Beijing |
| Fifth Avenue | Beijing |
| Changan Street | shanghai |

测试语句

```
SELECT * FROM XXXX WHERE City='Beijing';
```

测试结果

| Address | City |
|---|---|
| Oxford Street | Beijing |
| Fifth Avenue | Beijing |

#### 3.7.3. HAVING语句

在使用聚合函数时，您需要添加HAVING语句，以实现与WHERE语句一样的过滤效果。

**语法**

```
  SELECT [ ALL | DISTINCT ]{ * | projectItem [, projectItem ]* }
  FROM tableExpression
  [ WHERE booleanExpression ]
  [ GROUP BY { groupItem [, groupItem ]* } ]
  [ HAVING booleanExpression ];
```

**示例**

测试数据

| Customer | OrderPrice |
|---|---|
| Bush | 1000 |
| Carter | 1600 |
| Bush | 700 |
| Bush | 300 |
| Adams | 2000 |
| Carter | 100 |

测试语句

```
SELECT Customer,SUM(OrderPrice) FROM XXX GROUP BY Customer HAVING SUM(OrderPrice)<2000;
```

测试结果实时计算（流计算）

| Customer | SUM（OrderPrice） |
|---|---|
| Carter | 1700 |

#### 3.7.4. GROUP BY语句

**语法**

```
SELECT [ DISTINCT ] FROM tableExpression [ GROUP BY { groupItem [, groupItem ]* } ];
```

**示例**

测试数据（T1）

| Customer | OrderPrice |
|---|---|
| Bush | 1000 |
| Carter | 1600 |
| Bush | 700 |
| Bush | 300 |
| Adams | 2000 |
| Carter | 100 |

测试语句

```
SELECT Customer,SUM(OrderPrice) FROM T1 GROUP BY Customer;
```

测试结果

| Customer | SUM(OrderPrice) |
|---|---|
| Bush | 2000 |
| Carter | 1700 |
| Adams | 2000 |

#### 3.7.5. JOIN语句

实时计算的JOIN和传统批处理JOIN的语义一致，都用于将两张表关联起来。区别为实时计算关联的是两张动态表，关联的结果也会动态更新，以保证最终结果和批处理结果一致。

**语法**

```
tableReference [, tableReference ]* | tableexpression [ LEFT ] JOIN tableexpression [ joinCondition ];
```

tableReference：表名称。 tableexpression：表达式。 joinCondition：JOIN条件。

**重要**

只支持等值连接，不支持非等值连接。 只支持INNER JOIN和LEFT OUTER JOIN两种JOIN方式。

**Orders JOIN Products表的数据示例**

测试数据表 1. Orders

| rowtime | productId | orderId | units |
|---|---|---|---|
| 10:17:00 | 30 | 5 | 4 |
| 10:17:05 | 10 | 6 | 1 |
| 10:18:05 | 20 | 7 | 2 |
| 10:18:07 | 30 | 8 | 20 |
| 11:02:00 | 10 | 9 | 6 |
| 11:04:00 | 10 | 10 | 1 |
| 11:09:30 | 40 | 11 | 12 |

实时计算（流计算）

| 11:24:11 | 10 | 12 | 4 |
|---|---|---|---|

表 2. Products

| productId | name | unitPrice |
|---|---|---|
| 30 | Cheese | 17 |
| 10 | Beer | 0.25 |
| 20 | Wine | 6 |
| 30 | Cheese | 17 |
| 10 | Beer | 0.25 |
| 10 | Beer | 0.25 |
| 40 | Bread | 100 |
| 10 | Beer | 0.25 |

测试语句

```
  SELECT o.rowtime, o.productId, o.orderId, o.units,p.name, p.unitPrice
  FROM Orders AS o
  JOIN Products AS p
  ON o.productId = p.productId;
```

测试结果

| o.rowtime | o.productId | o.orderId | o.units | p.name | p.unitPrice |
|---|---|---|---|---|---|
| 10:17:00 | 30 | 5 | 4 | Cheese | 17 |
| 10:17:05 | 10 | 6 | 1 | Beer | 0.25 |
| 10:18:05 | 20 | 7 | 2 | Wine | 6 |
| 10:18:07 | 30 | 8 | 20 | Cheese | 17 |
| 11:02:00 | 10 | 9 | 6 | Beer | 0.25 |
| 11:04:00 | 10 | 10 | 1 | Beer | 0.25 |
| 11:09:30 | 40 | 11 | 12 | Bread | 100 |
| 11:24:11 | 10 | 12 | 4 | Beer | 0.25 |

**datahub_stream1 JOIN datahub_stream2表的数据示例**

测试数据表 3. datahub_stream1

| a（BIGINT） | b（BIGINT） | c（VARCHAR） |
|---|---|---|
| 0 | 10 | test11 |
| 1 | 10 | test21 |

表 4. datahub_stream2

| a（BIGINT） | b（BIGINT） | c（VARCHAR） |
|---|---|---|
| 0 | 10 | test11 |
| 1 | 10 | test21 |
| 0 | 10 | test31 |
| 1 | 10 | test41 |

测试语句

```
SELECT s1.c,s2.c FROM datahub_stream1 AS s1 JOIN datahub_stream2 AS s2 ON s1.a =s2.a WHERE s1.a = 0;
```

测试结果

| s1.c（VARCHAR） | s2.c（VARCHAR） |
|---|---|
| test11 | test11 |
| test11 | test31 |

实时计算（流计算）

#### 3.7.6. 维表JOIN语句

对于每条流式数据，可以关联一个外部维表数据源，为实时计算Flink版提供数据关联查询。

**说明**

维表是一张不断变化的表，在维表JOIN时，需指明该条记录关联维表快照的时刻。维表JOIN仅支持对当前时刻维表快照的关联，未来会支持关联左表 rowtime所对应的维表快照。

**维表JOIN语法**

```
SELECT column-names FROM table1 [AS <alias1>] [LEFT] JOIN table2 FOR SYSTEM_TIME AS OF PROCTIME() [AS <alias2>] ON table1.column-name1 = table2.key-name1;
```

事件流JOIN白名单维表，示例如下。

```
SELECT e.*, w.* FROM event AS e JOIN white_list FOR SYSTEM_TIME AS OF PROCTIME() AS w ON e.id = w.id;
```

**说明**

维表支持 `INNER JOIN` 和 `LEFT JOIN` ，不支持 `RIGHT JOIN` 或 `FULL JOIN` 。 必须加上 `FOR SYSTEM_TIME AS OF PROCTIME()` ，表示JOIN维表当前时刻所看到的每条数据。 源表后面进来的数据只会关联当时维表的最新信息，即JOIN行为只发生在处理时间（Processing Time）。如果JOIN行为发生后，维表中的数据发生了变化（新增、更新或删除），则已关联的维表数据不会被同步变化。 ON条件中必须包含维表所有的PRIMARY KEY的等值条件（且要求与真实表定义一致）。此外，ON条件中也可以有其他等值条件。 如果您有一对多JOIN需求，请在维表DDL INDEX中指定关联的KEY。 维表和维表不能进行JOIN。 ON条件中维表字段不能使用CAST等类型转换函数。如果您有类型转换需求，请在源表字段进行操作。

**示例**

测试数据表 1. datahub_input1

| id（bigint） | name（varchar） | age（bigint） |
|---|---|---|
| 1 | lilei | 22 |
| 2 | hanmeimei | 20 |
| 3 | libai | 28 |

表 2. phoneNumber

| name（varchar） | phoneNumber（bigint） |
|---|---|
| dufu | 18867889855 |
| baijuyi | 18867889856 |
| libai | 18867889857 |
| lilei | 18867889858 |

测试语句实时计算（流计算）

```
CREATE TABLE datahub_input1 ( id BIGINT, name VARCHAR, age BIGINT ) WITH ( type='datahub' ); create table phoneNumber( name VARCHAR, phoneNumber bigint, primary key(name), PERIOD FOR SYSTEM_TIME )with( type='rds' ); CREATE table result_infor( id bigint, phoneNumber bigint, name VARCHAR )with( type='rds' ); INSERT INTO result_infor t.id, w.phoneNumber, t.name FROM datahub_input1 as t JOIN phoneNumber FOR SYSTEM_TIME AS OF PROCTIME() as w ON t.name = w.name;
```

测试结果

| id（bigint） | phoneNumber（bigint） | name（varchar） |
|---|---|---|
| 1 | 18867889858 | lilei |
| 3 | 18867889857 | libai |

#### 3.7.7. UNION ALL语句

UNION ALL语句将两个流式数据合并。两个流式数据的字段必须完全一致，包括字段类型和字段顺序。

**语法**

```
select_statement select_statement;
```

|  | 说明实时计算Flink版同样支持 UNION 函数。 UNION ALL 允许重复值， UNION 不允许重复值。在实时计算Flink版系统中， UNION 相当于 UNION ALL+Distinct ，运行效率低，通常不推荐使用 UNION 。 |  |  |
|---|---|---|---|
|  |  | UNION |  |
|  | ALL+Distinct |  |  |

| UNION |  |
|---|---|
|  | UNION |

**示例**

测试数据表 1. test_source_union1

| a（varchar） | b（bigint） | c（bigint） |
|---|---|---|
| test1 | 1 | 10 |

表 2. test_source_union2

| a（varchar） | b（bigint） | c（bigint） |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |

表 3. test_source_union3

| a（varchar） | b（bigint） | c（bigint） |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |
| test1 | 1 | 10 |

测试语句实时计算（流计算） `a,`

```
    sum(b) as d,
    sum(c) as e
FROM
    (SELECT * from test_source_union1
    SELECT * from test_source_union2
    SELECT * from test_source_union3
```

`)t`

```
 GROUP BY a;
```

测试结果

| a（varchar） | d（bigint） | e（bigint） |
|---|---|---|
| test1 | 1 | 10 |
| test2 | 2 | 20 |
| test1 | 2 | 20 |
| test1 | 3 | 30 |
| test2 | 4 | 40 |
| test1 | 4 | 40 |

此结果为调试结果，会显示出计算过程。如果您的结果表是DataHub、消息队列Kafka或消息队列MQ等，正式上线也会显示过程数据。但如果您的结果

**说明**

表是云数据RDS等关系型数据库，正式上线，主键相同的记录显示为一条数据。

#### 3.7.8. TopN语句

TopN语句用于对实时数据中某个指标的前N个最值的筛选。Flink SQL可以基于OVER窗口操作灵活地完成TopN的功能。

**语法**

```
SELECT * FROM (
  SELECT *,
    ROW_NUMBER() OVER ([PARTITION BY col1[, col2..]]
    ORDER BY col1 [asc|desc][, col2 [asc|desc]...]) AS rownum
  FROM table_name)
WHERE rownum <= N [AND conditions]
```

**说明**

`ROW_NUMBER()` ：行号计算函数 `OVER` 的窗口，行号计算从1开始。 `PARTITION BY col1[, col2..]` ：指定分区的列，可以不指定。 ORDER BY col1 [asc|desc][, col2 [asc|desc]...] ：指定排序的列和每列的排序方向。 如上语法所示，TopN需要两层Query： 查询中使用 `ROW_NUMBER()` 窗口函数来对数据根据排序列进行排序并标上排名。 外层查询中对排名进行过滤，只取前N条。例如N=10即为取前10条的数据。 在执行过程中，Flink SQL会对输入的数据流根据排序键进行排序。如果某个分区的前N条记录发生了改变，则会将改变的那几条数据以更新流的形式发给下游。 如果需要将TopN的数据输出到外部存储，后接的结果表必须是一个带主键的表。

**说明**

WHERE条件的限制为了使Flink SQL能识别出这是一个TopN的query，外层循环中必须要指定 `rownum <= N` 的格式来指定前N条记录。此时，您不可以将 `rownum` 置于某个表达式中，例如 `rownum - 5 <= N` 。WHERE条件中，可以额外带上其他条件，但是必须使用 `AND` 连接条件。

**示例1**

本例中，先统计查询流中每小时、每个城市和关键字被查询的次数，然后输出每小时、每个城市被查询最多的前100个关键字。在输出表中，小时、城市、排名三者可以唯一确定一条记录，所以需要将这三列声明成联合主键（在外部存储中也需要有同样的主键设置）。 实时计算（流计算）

```
CREATE TABLE rds_output (
  rownum BIGINT,
  start_time BIGINT,
  city VARCHAR,
  keyword VARCHAR,
  pv BIGINT,
  PRIMARY KEY (rownum, start_time, city)
) WITH (
  type = 'rds',
  ...
```

)

```
INSERT INTO rds_output SELECT rownum, start_time, city, keyword, pv FROM (
  SELECT *,
     ROW_NUMBER() OVER (PARTITION BY start_time, city ORDER BY pv desc) AS rownum
  FROM (
        SELECT SUBSTRING(time_str,1,12) AS start_time,
            keyword,
            count(1) AS pv,
            city
        FROM tmp_search
    ) a
) t WHERE rownum <= 100
```

**示例2**

测试数据

| ip（VARCHAR） | time（VARCHAR） |
|---|---|
| 192.168.1.1 | 100000000 |
| 192.168.1.2 | 100000000 |
| 192.168.1.2 | 100000000 |
| 192.168.1.3 | 100030000 |
| 192.168.1.3 | 100000000 |
| 192.168.1.3 | 100000000 |

测试语句实时计算（流计算）

```
CREATE TABLE source_table (
  IP VARCHAR,
  `TIME` VARCHAR
)WITH(
  type='datahub',
  endPoint='<yourEndpoint>',
  project='<yourProjectName>',
  topic='<yourTopicName>',
  accessId='<yourAccessId>',
  accessKey='<yourAccessSecret>'
); CREATE TABLE result_table (
  rownum BIGINT,
  start_time VARCHAR,
  IP VARCHAR,
  cc BIGINT,
  PRIMARY KEY (start_time, IP)
) WITH (
  type = 'rds',
  url='<yourDatabaseAddress>',
  tableName='blink_rds_test',
  userName='<yourDatabaseUserName>',
  password='<yourDatabasePassword>'
); INSERT INTO result_table SELECT rownum,start_time,IP,cc FROM (
  SELECT *,
     ROW_NUMBER() OVER (PARTITION BY start_time ORDER BY cc DESC) AS rownum
  FROM (
```

SELECT SUBSTRING(`TIME`,1,2) AS start_time,--可以根据真实时间取相应的数值，这里取得是测试数据。

```
        COUNT(IP) AS cc,
```

`IP`

```
        FROM  source_table
```

`)a`

```
) t
```

`WHERE rownum <= 3 --`可以根据真实`top`值取相应的数值，这里取得是测试数据。 测试结果

| rownum（BIGINT） | start _time（VARCHAR） | ip（VARCHAR） | cc（BIGINT） |
|---|---|---|---|
| 1 | 10 | 192.168.1.3 | 3 |
| 2 | 10 | 192.168.1.2 | 2 |
| 3 | 10 | 192.168.1.1 | 1 |

**无排名优化**

使用无排名优化，您可以解决数据膨胀问题。 数据膨胀问题根据TopN的语法， `rownum` 字段会作为结果表的主键字段之一写入结果表。但是这可能导致数据膨胀的问题。例如，收到一条原排名9的更新数据，更新后排名上升到 1，则从1到9的数据排名都发生变化了，需要将这些数据作为更新都写入结果表。这样就产生了数据膨胀，导致结果表因为收到了太多的数据而降低更新速度。 无排名优化方法结果表中不保存 `rownum` ，最终的 `rownum` 由前端计算。因为TopN的数据量通常不会很大，前端排序100个数据很快。当收到一条原排名9、更新后排名上升到1的数据，也只需要发送这一条数据，而不用把排名1到9的数据全发送下去。这种优化能够提升结果表的更新速度。 无排名优化语法

```
SELECT col1, col2, col3 FROM (
 SELECT col1, col2, col3
   ROW_NUMBER() OVER ([PARTITION BY col1[, col2..]]
   ORDER BY col1 [asc|desc][, col2 [asc|desc]...]) AS rownum
 FROM table_name)
WHERE rownum <= N [AND conditions]
```

语法与上文类似，只是在外层查询中将rownum字段裁剪掉即可。 在无rownum的场景中，对于结果表主键的定义需要特别小心。如果定义有误，会直接导致TopN结果的不正确。无rownum场景中，主键应为TopN上游

**说明**

GROUP BY节点的KEY列表。 无排名优化示例本示例来源于自视频行业的案例。用户每个视频在分发时会产生大量流量，依据视频产生的流量可以分析出最热门的视频。本例用于统计出每分钟流量最大的Top5的视频。 实时计算（流计算） 测试语句 `--`从`SLS`读取数据原始存储表。

```
CREATE TABLE sls_cdnlog_stream ( vid VARCHAR, -- video id
```

`rowtime TIMESTAMP, --` 观看视频的时间。 `response_size BIGINT, --` 观看产生的流量。

```
) WITH ( type='sls', ... );
```

`--1`分钟窗口统计`vid`带宽数。

```
CREATE VIEW cdnvid_group_view AS SELECT vid, TUMBLE_START(rowtime, INTERVAL '1' MINUTE) AS start_time, SUM(response_size) AS rss FROM sls_cdnlog_stream GROUP BY vid, TUMBLE(rowtime, INTERVAL '1' MINUTE);
```

`--`存储表。

```
CREATE TABLE hbase_out_cdnvidtoplog ( vid VARCHAR, rss BIGINT, start_time VARCHAR,
```

`--` 注意结果表中不存储`rownum`字段。 `--` 特别注意该主键的定义，为`TopN`上游`GROUP BY`的`KEY`。

```
PRIMARY KEY(start_time, vid) ) WITH ( type='RDS', ... );
```

`--` 统计每分钟`Top5`消耗流量的`vid`，并输出。

```
INSERT INTO hbase_out_cdnvidtoplog
```

`--` 注意次外层查询，不选出`rownum`字段。

```
SELECT vid, rss, start_time FROM ( vid, start_time, rss, ROW_NUMBER() OVER (PARTITION BY start_time ORDER BY rss DESC) as rownum FROM cdnvid_group_view
```

)

```
WHERE rownum <= 5;
```

测试数据

| vid（VARCHAR） | rowtime（Timestamp） | response _size（BIGINT） |
|---|---|---|
| 10000 | 2017-12-18 15:00:10 | 2000 |
| 10000 | 2017-12-18 15:00:15 | 4000 |
| 10000 | 2017-12-18 15:00:20 | 3000 |
| 10001 | 2017-12-18 15:00:20 | 3000 |
| 10002 | 2017-12-18 15:00:20 | 4000 |
| 10003 | 2017-12-18 15:00:20 | 1000 |
| 10004 | 2017-12-18 15:00:30 | 1000 |
| 10005 | 2017-12-18 15:00:30 | 5000 |
| 10006 | 2017-12-18 15:00:40 | 6000 |
| 10007 | 2017-12-18 15:00:50 | 8000 |

测试结果

| start _time（VARCHAR） | vid（VARCHAR） | rss（BIGINT） |
|---|---|---|
| 2017-12-18 15:00:00 | 10000 | 9000 |
| 2017-12-18 15:00:00 | 10007 | 8000 |
| 2017-12-18 15:00:00 | 10006 | 6000 |
| 2017-12-18 15:00:00 | 10005 | 5000 |
| 2017-12-18 15:00:00 | 10002 | 4000 |

实时计算（流计算）

#### 3.7.9. 复杂事件处理（CEP）语句

复杂事件处理（CEP）语句MATCH_RECOGNIZE，用于识别输入流中符合指定规则的事件，并按照指定方式输出。

**语法**

```
SELECT [ ALL | DISTINCT ] FROM tableExpression [MATCH_RECOGNIZE ( [PARTITION BY {partitionItem [, partitionItem]*}] [ORDER BY {orderItem [, orderItem]*}] [MEASURES {measureItem AS col [, measureItem AS col]*}] [ONE ROW PER MATCH|ALL ROWS PER MATCH|ONE ROW PER MATCH WITH TIMEOUT ROWS|ALL ROWS PER MATCH WITH TIMEOUT ROWS] [AFTER MATCH SKIP] PATTERN (patternVariable[quantifier] [ patternVariable[quantifier]]*) WITHIN intervalExpression DEFINE {patternVariable AS patternDefinationExpression [, patternVariable AS patternDefinationExpression]*} )];
```

| 参数 | 说明 |
|---|---|
| PARTITION BY | 分区的列，可选项。 |
| ORDER BY | 可以指定多列，但是必须以 EVENT TIME 或 PROCESS TIME 列作为排序的首列，可选项。 |
| MEASURES | 定义如何根据匹配成功的输入事件构造输出事件。 |
| ONE ROW PER MATCH | 对于每一次成功的匹配，只产生一个输出事件。 |
| ONE ROW PER MATCH WITH TIMEOUT ROWS | 除了匹配成功时产生的输出外，超时也会产生输出。超时时间由PATTERN语句中的WITHIN语句定义。 说明 Blink 3.6.0及以后版本，由于Calcite升级，不再支持ONE ROW PER MATCH WITH TIMEOUT ROWS参数。 |
| ALL ROWS PER MATCH | 对于每一次成功的匹配，对应于每一个输入事件，都会产生一个输出事件。 |
| ALL ROWS PER MATCH WITH TIMEOUT ROWS | 除了匹配成功时产生输出外，超时也会产生输出。超时时间由PATTERN语句中的WITHIN语句定义。 说明 Blink 3.6.0及以后版本，由于Calcite升级，不再支持ALL ROWS PER MATCH WITH TIMEOUT ROWS参数。 |
| [ONE ROW PER MATCH\|ALL ROWS PER MATCH\|ONE ROW PER MATCH WITH TIMEOUT ROWS\|ALL ROWS PER MATCH WITH TIMEOUT ROWS] | 可选项，默认为 ONE ROW PER MATCH 。 |
| AFTER MATCH SKIP TO NEXT ROW | 匹配成功后，从匹配成功的事件序列中的第一个事件的下一个事件开始进行下一次匹配。 |
| AFTER MATCH SKIP PAST LAST ROW | 匹配成功后，从匹配成功的事件序列中的最后一个事件的下一个事件开始进行下一次匹配。 |
| AFTER MATCH SKIP TO FIRST patternItem | 匹配成功后，从匹配成功的事件序列中第一个对应于patternItem的事件开始进行下一次匹配。 |
| AFTER MATCH SKIP TO LAST patternItem | 匹配成功后，从匹配成功的事件序列中最后一个对应于patternItem的事件开始进行下一次匹配。 |
| PATTERN | 定义待识别的事件序列需要满足的规则，需要定义在 () 中，由一系列自定义的patternVariable构成。 说明 patternVariable之间如果以空格间隔，表示符合这两种patternVariable的事件中间不存在其他事件。 patternVariable之间如果以->间隔，表示符合这两种patternVariable的事件之间可以存在其它事件。 Blink 3.6.0及以后版本，由于Calcite升级，不再支持PATTERN参数。 |

**参数解释**

**quantifier**

**quantifier**用于指定符合**patternVariable**定义事件的出现次数。

| 参数 | 说明 |
|---|---|
| * | 0次或多次 |
| + | 1次或多次 |
| ? | 0次或1次 |
| {n} | n次 |
| {n,} | 大于等于n次 |
| {n, m} | 大于等于n次，小于等于m次 |
| {,m} | 小于等于m次 |

默认为贪婪匹配。例如，对于 `pattern: A -> B+ -> C` ，输入为 `a bc1 bc2 c` （其中bc1和bc2表示既匹配B也匹配C），则输出为 `a bc1 bc2 c` 。可以在**quantifier**符号后面加？来表示非贪婪匹配。例如：

| *? |  |
|---|---|
| +? |  |
| {n}? |  |

实时计算（流计算）

|  | {n,}? |
|---|---|
|  | {n, m}? |
|  | {,m}? |
| 说明 Blink 3.x以上版本不支持(e1 e2+)贪婪匹配，您可以使用e1 e2+ e3 e3 as not e2绕行方案，但请务必要使用一个e3，才能有数据输出。 |  |

此时，对于上面例子中的**PATTERN**及输入，产生的输出为**a bc1 bc2,a bc1 bc2 c**。
**WITHIN**定义符合规则的事件序列的最大时间跨度。

| INTERVAL ‘string’ timeUnit [ TO timeUnit ] | 。例如： |
|---|---|

| INTERVAL intervalExpression | 。例如： | INTERVAL A.windowTime + 10 |
|---|---|---|

UDF，intervalExpression的结果必须为LONG，单位为millisecond，表示窗口的大小。 DEFINE定义在**PATTERN**中出现的**patternVariable**的具体含义，如果某个**patternVariable**在DEFINE中没有定义，则认为对于每一个事件， 该**patternVariable**都成立。

**MEASURES和DEFINE语句函数**

| 函数 | 说明 |
|---|---|
| Row Pattern Column References | 形式为 patternVariable.col 。表示访问patternVariable所对应的事件的指定的列。 |
| PREV | 只能用在DEFINE语句中，通常与 Row Pattern Column References 合用。用于访问指定的PATTERN所对应的事件之前，偏移指定的offset所对应的事件的指定的列。 例如， DOWN AS DOWN.price < PREV(DOWN.price) ， PREV(A.price) 表示当前事件的前一个事件的 price 列的值。 说明 DOWN.price 等价于 PREV(DOWN.price, 0) 。 PREV(DOWN.price) 等价于 PREV(DOWN.price, 1) 。 |
| FIRST、LAST | 一般与 Row Pattern Column References 合用，用于访问指定的PATTERN所对应的事件序列中的指定偏移位置的事件。例如： FIRST(A.price, 3) 表示 PATTERN A 所对应的事件序列中的第4个事件。 LAST(A.price, 3) 表示 PATTERN A 所对应的事件序列中的倒数第4个事件。 |

|  | PREV(DOWN.price, 0) |
|---|---|
| PREV(DOWN.price) |  |

**输出列**

| 函数 | 输出列 |
|---|---|
| ONE ROW PER MATCH | 包括 PARTITION BY 中指定的列及 MEASURES 中定义的列。对于 PARTITION BY 中已经指定的列， 在 MEASURES 中无需重复定义。 |
| ONE ROW PER MATCH WITH TIMEOUT ROWS | 除匹配成功的时候产生输出外，超时的时候也会产生输出，超时时间由PATTERN语句中的WITHIN语句定义。 |

**说明**

当定义**PATTERN**时，最好也定义**WITHIN**，否则可能会造成STATE越来越大。 ORDER BY中定义的首列必须为EVENT TIME列或者PROCESS TIME列。

**示例**

示例语法

```
SELECT * FROM Ticker MATCH_RECOGNIZE ( PARTITION BY symbol ORDER BY tstamp MEASURES STRT.tstamp AS start_tstamp, LAST(DOWN.tstamp) AS bottom_tstamp, LAST(UP.tstamp) AS end_tstamp ONE ROW PER MATCH AFTER MATCH SKIP TO NEXT ROW PATTERN (STRT DOWN+ UP+) WITHIN INTERVAL '10' SECOND DEFINE DOWN AS DOWN.price < PREV(DOWN.price), UP AS UP.price > PREV(UP.price) );
```

测试数据

| timestamp（TIMESTAMP） | cardid(VARCHAR) _ | location（VARCHAR） | action（VARCHAR） |
|---|---|---|---|
| 2018-04-13 12:00:00 | 1 | Beijing | Consumption |
| 2018-04-13 12:05:00 | 1 | Shanghai | Consumption |
| 2018-04-13 12:10:00 | 1 | Shenzhen | Consumption |
| 2018-04-13 12:20:00 | 1 | Beijing | Consumption |

测试语法当相同的card_id在十分钟内，在两个不同的location发生刷卡现象，就会触发报警机制，以便监测信用卡盗刷等现象。 实时计算（流计算）

```
CREATE TABLE datahub_stream (
    `timestamp`               TIMESTAMP,
    card_id                   VARCHAR,
    location                  VARCHAR,
    `action`                  VARCHAR,
    WATERMARK wf FOR `timestamp` AS withOffset(`timestamp`, 1000)
) WITH (
    type = 'datahub'
    ...
); CREATE TABLE rds_out (
    start_timestamp               TIMESTAMP,
    end_timestamp                 TIMESTAMP,
    card_id                       VARCHAR,
    event                         VARCHAR
) WITH (
    type= 'rds'
    ...
);
```

`--`定义计算逻辑。

```
insert into rds_out `start_timestamp`, `end_timestamp`, card_id, `event` from datahub_stream MATCH_RECOGNIZE (
```

`PARTITION BY card_id --`按`card_id`分区，将相同卡号的数据分发到同一个计算节点。 ORDER BY `timestamp` --在窗口内，对事件时间进行排序。 `MEASURES --`定义如何根据匹配成功的输入事件构造输出事件。

```
        e2.`action` as `event`,
```

e1.`timestamp` as `start_timestamp`, --第一次的事件时间为`start_timestamp`。

```
        LAST(e2.`timestamp`) as `end_timestamp` --最新的事件时间为end_timestamp。
```

`ONE ROW PER MATCH --`匹配成功输出一条。 `AFTER MATCH SKIP TO NEXT ROW --`匹配后跳转到下一行。

```
    PATTERN (e1 e2+) WITHIN INTERVAL '10' MINUTE  --定义两个事件，e1和e2。
```

`DEFINE --`定义在`PATTERN`中出现的`patternVariable`的具体含义。

```
        e1 as e1.action = 'Consumption',    --事件一的action标记为Consumption。
```

`e2 as e2.action = 'Consumption' and e2.location <> e1.location --`事件二的`action`标记为`Consumption`，且事件一和事件二的`location`不一致。

```
);
```

如果存在满足CEP条件的数据，但没有结果输出是因为只有**Watermark > e2.ts**的数据才会被处理，但由于e2后面已经没有数据了，导致Watermark

**说明**

一直是**e2.ts -1000**，所以e2的数据一直没有被处理，从而导致没有结果输出。 测试结果

| start _timestamp（TIMESTAMP） | end _timestamp（TIMESTAMP） | card _id（VARCHAR） | event（VARCHAR） |
|---|---|---|---|
| 2018-04-13 12:00:00.0 | 2018-04-13 12:05:00.0 | 1 | Consumption |
| 2018-04-13 12:05:00.0 | 2018-04-13 12:10:00.0 | 1 | Consumption |

### 创建数据视图

视图仅仅用于辅助计算逻辑的描述，不会产生数据的物理存储。视图是一种方便的方法，可以通过提供这些片段名称将SQL转换成可管理的视图块。因此，视图并不占用系统空间。

**命令格式**

```
CREATE VIEW viewName
        [ (columnName[ , columnName]*) ]
            AS queryStatement;
```

**示例1**

```
 CREATE VIEW  LargeOrders(r, t, c, u) AS
  SELECT rowtime,
    productId,
```

`c,`

```
    units
  FROM Orders;
  INSERT INTO rds_output
  r,t,c,u
  FROM LargeOrders;
```

**示例2**

表 1. 测试数据实时计算（流计算）

| a（VARCHAR） | b（BIGINT） | c（TIMESTAMP） |
|---|---|---|
| test1 | 1 | 1506823820000 |
| test2 | 1 | 1506823850000 |
| test1 | 1 | 1506823810000 |
| test2 | 1 | 1506823840000 |
| test2 | 1 | 1506823870000 |
| test1 | 1 | 1506823830000 |
| test2 | 1 | 1506823860000 |

测试案例

```
CREATE TABLE datahub_stream ( a VARCHAR, b BIGINT, c TIMESTAMP, d AS PROCTIME() ) WITH (
  type='datahub',
  endPoint='http://dh-cn-hangzhou.aliyuncs.com',
  project='blink_test',
  topic='window_count',
  accessId='yourAccessId',
  accessKey='yourAccessSecret'
); CREATE TABLE rds_output ( a varchar, b TIMESTAMP, cnt BIGINT, PRIMARY KEY(a) )with(
  type = 'rds',
  url='jdbc:mysql://rm-bp1gz4k20****.mysql.rds.aliyuncs.com:3306/****',
  tableName='yourTableName',
  userName='yourAccessUserName',
  password='yourAccessPassword'
); CREATE VIEW rds_view AS SELECT a,
   CAST(HOP_START(d, interval '5' second, interval '30' second) AS TIMESTAMP) AS cc,
   sum(b) AS cnt
FROM datahub_stream GROUP BY HOP(d, interval '5' second, interval '30' second),a; INSERT INTO rds_output
```

`a,`

```
cc, cnt FROM rds_view WHERE cnt=4
```

表 2. 测试结果

| a（VARCHAR） | b（TIMESTAMP） | cnt（BIGINT） |
|---|---|---|
| test2 | 2017-11-06 16:54:10 | 4 |

### 窗口函数

**3.9.1. 概述**

### 窗口函数

窗口函数Flink SQL支持基于无限大窗口的聚合（无需在SQL Query中，显式定义任何窗口）以及对一个特定的窗口的聚合。例如，需要统计在过去的1分钟内有多少用户点击了某个的网页，可以通过定义一个窗口来收集最近1分钟内的数据，并对这个窗口内的数据进行计算。 Flink SQL支持的窗口聚合主要是两种：Window聚合和Over聚合。本文档主要为您介绍Window聚合。Window聚合支持Event Time和Processing Time两种时间属性定义窗口。每种时间属性类型支持三种窗口类型：滚动窗口（TUMBLE）、滑动窗口（HOP）和会话窗口（SESSION）。

#### 时间属性

Flink SQL支持以下两种时间属性。实时计算可以基于这两种时间属性对数据进行窗口聚合。 Event Time：您提供的事件时间（通常是数据的最原始的创建时间），Event Time一定是您提供在Schema里的数据。 Processing Time：对事件进行处理的本地系统时间。

**说明**

实时计算时间属性详情，请参见时间属性。

**级联窗口**

实时计算（流计算） Rowtime列在经过窗口操作后，其Event Time属性将丢失。您可以使用辅助函数 `TUMBLE_ROWTIME` 、 `HOP_ROWTIME` 或 `SESSION_ROWTIME` ，获取窗口中的Rowtime列

| 大值 | max(rowtime) |  |
|---|---|---|
| 00:14:59.999 |  | 。 |

示例逻辑为：基于1分钟的滚动窗口聚合结果，进行1小时的滚动窗口聚合，可以满足您的多维度开窗需求。

```
CREATE TABLE user_clicks(
  username varchar,
  click_url varchar,
  ts timeStamp,
  WATERMARK wk FOR ts as withOffset(ts, 2000)  --为Rowtime定义Watermark。
) with (
  type='datahub',
  ...
); CREATE TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  type='print'
);
```

`//` 使用`TUMBLE_ROWTIME`作为二级`Window`的聚合时间。

```
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,
  username,
FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username; INSERT INTO tumble_output
  TUMBLE_START(rowtime, INTERVAL '1' HOUR),
  TUMBLE_END(rowtime, INTERVAL '1' HOUR),
  username,
  SUM(cnt)
GROUP BY TUMBLE(rowtime, INTERVAL '1' HOUR), username;
```

#### 3.9.2. 滚动窗口

本文为您介绍如何使用实时计算Flink版滚动窗口函数。

**定义**

滚动窗口（TUMBLE）将每个元素分配到一个指定大小的窗口中。通常，滚动窗口有一个固定的大小，并且不会出现重叠。例如，如果指定了一个5分钟大小的滚动窗口，无限流的数据会根据时间划分为 `[0:00, 0:05)` 、 `[0:05, 0:10)` 、 `[0:10, 0:15)` 等窗口。下图展示了一个30秒的滚动窗口。

**语法**

TUMBLE函数用在GROUP BY子句中，用来定义滚动窗口。 实时计算（流计算）

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

`<time-attr>` 参数必须是时间流中的一个合法的时间属性字段，指定为Processing Time或Event Time，请参见概述，了解如何定义时间属

**说明**

**标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 | 返回类型 | 描述 |
|---|---|---|
| TUMBLE_START(time-attr, size- | TIMES | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 窗口，返回 00:10 。 |
| interval) |  |  |
| TUMBLE_END(time-attr, size- | TIM | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15] 窗口，返回 00:15 。 |
| interval) |  |  |
| TUMBLE ROWTIME(time-attr, size- | TIMESTAMP(rowtime-attr) | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，即可以基于该字段做时间属性的操作，例如，级联窗口只能用在基于Event Time的Window上，详情请参见级联窗口。 |
| _ interval) |  |  |
| TUMBLE PROCTIME(time-attr, | TIMESTAMP(rowtime-attr) | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个Proctime Attribute，即可以基于该字段做时间属性的操作。例如，级联窗口只能用在基于Processing Time的Window上，详情请参见级联窗口。 |
| _ size-interval) |  |  |

**使用Event Time统计每个用户每分钟在指定网站的单击数示例**

测试数据

| username（VARCHAR） | click _url（VARCHAR） | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句

```
CREATE TABLE user_clicks(
  username varchar,
  click_url varchar,
  ts timeStamp,
  WATERMARK wk FOR ts as withOffset(ts, 2000) --为rowtime定义Watermark。
) with (
  type='datahub',
  ...
); CREATE TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  type='RDS'
); INSERT INTO tumble_output TUMBLE_START(ts, INTERVAL '1' MINUTE) as window_start, TUMBLE_END(ts, INTERVAL '1' MINUTE) as window_end, username, FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

测试结果

| window _start （TIMESTAMP） | window _end （TIMESTAMP） | username（VARCHAR） | clicks（BIGINT） |
|---|---|---|---|
| 2017-10-10 10:00:00.0 | 2017-10-10 10:01:00.0 | Jark | 3 |
| 2017-10-10 10:01:00.0 | 2017-10-10 10:02:00.0 | Jark | 2 |
| 2017-10-10 10:02:00.0 | 2017-10-10 10:03:00.0 | Timo | 1 |

**使用Processing Time统计每个用户每分钟在指定网站的单击数示例**

实时计算（流计算） 测试数据

| username （VARCHAR） | click _url（VARCHAR） |
|---|---|
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Timo | http://taobao.com/xxx |

测试语句

```
CREATE TABLE window_test (
  username   VARCHAR,
  click_url  VARCHAR,
  ts as PROCTIME()
) WITH (
  type='datahub',
  ...
); CREATE TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
  type='print'
); INSERT INTO tumble_output TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, FROM window_test GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

测试结果

| window _start （TIMESTAMP） | window _end （TIMESTAMP） | username （VARCHAR） | clicks（BIGINT） |
|---|---|---|---|
| 2019-04-11 14:43:00.000 | 2019-04-11 14:44:00.000 | Jark | 5 |
| 2019-04-11 14:43:00.000 | 2019-04-11 14:44:00.000 | Timo | 1 |

**说明**

因为本地调试是瞬时的，处理时间可能小于1秒，所以使用Processing Time时间属性对数据进行窗口聚合，可能会出现本地调试没有结果的情况。

#### 3.9.3. 滑动窗口

本文为您介绍如何使用实时计算滑动窗口函数。

**说明**

实时计算滑动窗口（HOP）暂不支持与LAST_VALUE、FIRST_VALUE或TopN函数共同使用。

**什么是滑动窗口**

滑动窗口（HOP），也被称作Sliding Window。不同于滚动窗口，滑动窗口的窗口可以重叠。 滑动窗口有两个参数：**slide**和**size**。**slide**为每次滑动的步长，**size**为窗口的大小。
**slide < size**，则窗口会重叠，每个元素会被分配到多个窗口。
**slide = size**，则等同于滚动窗口（TUMBLE）。
**slide > size**，则为跳跃窗口，窗口之间不重叠且有间隙。
通常，大部分元素符合多个窗口情景，窗口是重叠的。因此，滑动窗口在计算移动平均数（moving averages）时很实用。例如，计算过去5分钟数据的平均值，每10秒钟更新一次，可以设置**slide**为10秒，**size**为5分钟。下图为您展示间隔为30秒，窗口大小为1分钟的滑动窗口。 实时计算（流计算）

**滑动窗口函数语法**

HOP函数用在group by子句中，用来定义滑动窗口。

```xml
HOP(<time-attr>, <slide-interval>,<size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

**说明**

`<time-attr>` 参数必须是流中的一个合法的时间属性字段，指定为Processing Time或Event Time。请参见概述，了解如何定义时间属性和Watermark。

**滑动窗口标识函数**

使用滑动窗口标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 | 返回类型 | 描述 |
|---|---|---|
| HOP_START（<time-attr>, <slide- | TIMESTAMP | 返回窗口的起始时间（包含边界）。例如 [00:10, 00:15) 窗口，返回 00:10 。 |
| interval>, <size-interval>） |  |  |
| HOP_END（<time-attr>, <slide- | TIMESTAMP | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15) 窗口，返回 00:15 。 |
| interval>, <size-interval>） |  |  |
| HOP_ROWTIME（<time-attr>, |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15) 窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，即可以基于该字段做时间类型的操作，例如级联窗口，只能用在基于event time的window上。 |
| <slide-interval>, <size- |  |  |
| interval>） |  |  |
| HOP_PROCTIME（<time-attr>, |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15) 窗口，返回 00:14:59.999 。返回值是一个proctime attribute，即可以基于该字段做时间类型的操作，例如级联窗口，只能用在基于processing time的window上。 |
| <slide-interval>, <size- |  |  |
| interval>） |  |  |

**示例**

统计每个用户过去1分钟的单击次数，每30秒更新1次，即1分钟的窗口，30秒滑动1次。 测试数据

| username（VARCHAR） | click _url（VARCHAR） | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算）

```
CREATE TABLE user_clicks (
    username VARCHAR,
    click_url VARCHAR,
    ts TIMESTAMP,
    WATERMARK wk FOR ts AS WITHOFFSET (ts, 2000)--为rowtime定义Watermark。
) WITH ( TYPE = 'datahub',
        ...);
CREATE TABLE hop_output (
    window_start TIMESTAMP,
    window_end TIMESTAMP,
    username VARCHAR,
    clicks BIGINT
) WITH (TYPE = 'rds',
        ...);
    hop_output
    HOP_START (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    HOP_END (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    username,
FROM
    user_clicks
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    username
```

测试结果

| window _start （TIMESTAMP） | window _end （TIMESTAMP） | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|
| 2017-10-10 09:59:30.0 | 2017-10-10 10:00:30.0 | Jark | 2 |
| 2017-10-10 10:00:00.0 | 2017-10-10 10:01:00.0 | Jark | 3 |
| 2017-10-10 10:00:30.0 | 2017-10-10 10:01:30.0 | Jark | 2 |
| 2017-10-10 10:01:00.0 | 2017-10-10 10:02:00.0 | Jark | 2 |
| 2017-10-10 10:01:30.0 | 2017-10-10 10:02:30.0 | Jark | 1 |
| 2017-10-10 10:02:00.0 | 2017-10-10 10:03:00.0 | Timo | 1 |
| 2017-10-10 10:02:30.0 | 2017-10-10 10:03:30.0 | Timo | 1 |

HOP窗口无法读取数据进入的时间，第一个窗口的开启时间会前移。**前移时长**=**窗口时长**-**滑动步长**，示例如下表。

| 窗口时长（秒） | 滑动步长（秒） | Event Time | 第一个窗口StartTime | 第一个窗口EndTime |
|---|---|---|---|---|
| 120 | 30 | 2019-07-31 10:00:00.0 | 2019-07-31 09:58:30.0 | 2019-07-31 10:00:30.0 |
| 60 | 10 | 2019-07-31 10:00:00.0 | 2019-07-31 09:59:10.0 | 2019-07-31 10:00:10.0 |

#### 3.9.4. 会话窗口

本文为您介绍如何使用实时计算Flink版会话窗口函数。

**什么是会话窗口**

会话窗口（SESSION）通过SESSION活动来对元素进行分组。会话窗口与滚动窗口和滑动窗口相比，没有窗口重叠，没有固定窗口大小。相反，当它在一个固定的时间周期内不再收到元素，即会话断开时，该窗口就会关闭。 会话窗口通过一个间隔时间（Gap）来配置，这个间隔定义了非活跃周期的长度。例如，一个表示鼠标单击活动的数据流可能具有长时间的空闲时间，并在两段空闲之间散布着高浓度的单击。如果数据在指定的间隔（Gap）之后到达，则会开始一个新的窗口。 会话窗口示例如下图，每个Key由于不同的数据分布，形成了不同的Window。 实时计算（流计算）

**会话窗口函数语法**

SESSION函数用于在GROUP BY子句中定义会话窗口。

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

`<time-attr>` 参数必须是数据流中的一个合法的时间属性字段，指定为Processing Time或Event Time，详情请参见概述，了解如何定义时间属

**说明**

**会话窗口标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 | 返回类型 | 描述 |
|---|---|---|
| SESSION_START（<time-attr>, | Timestamp | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 的窗口，返回 00:10 ，即为此会话窗口内第一条记录的时间。 |
| <gap-interval>） |  |  |
| SESSION_END（<time-attr>, <gap- | Timestam | 返回窗口的结束时间（包含边界）。例如 [00:00,00:15) 的窗口，返回 00:15 ，即为此会话窗口内最后一条记录的时间+ <gap-interval> 。 |
| interval>） |  |  |
| SESSION ROWTIME（<time-attr>, | Timestamp（rowtime-attr） | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，也就是可以基于该字段进行时间类型的操作，如级联窗口。该参数只能用于基于Event Time的Window。 |
| _ <gap-interval>） |  |  |
| SESSION PROCTIME（<time-attr>, | Timestamp（rowtime-attr） | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个Proctime Attribute，也就是可以基于该字段进行时间类型的操作，如级联窗口。该参数只能用于基于Processing Time的Window。 |
| _ <gap-interval>） |  |  |

**示例**

统计每个用户在每个活跃会话期间的单击次数，会话超时时长为30秒。 测试数据

| username （VARCHAR） | click _url （VARCHAR） | ts （TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算）

```
CREATE TABLE user_clicks( username varchar, click_url varchar, ts timeStamp, WATERMARK wk FOR ts as withOffset(ts, 2000) -- 为rowtime定义watermark ) with ( type='datahub', ... ); CREATE TABLE session_output( window_start TIMESTAMP, window_end TIMESTAMP, username VARCHAR, clicks BIGINT ) with ( type='rds'， ... ); INSERT INTO session_output SESSION_START(ts, INTERVAL '30' SECOND), SESSION_END(ts, INTERVAL '30' SECOND), username, FROM user_clicks GROUP BY SESSION(ts, INTERVAL '30' SECOND), username;
```

测试结果

| window _start （TIMESTAMP） | window _end （TIMESTAMP） | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|
| 2017-10-10 10:00:00.0 | 2017-10-10 10:00:40.0 | Jark | 2 |
| 2017-10-10 10:00:49.0 | 2017-10-10 10:01:35.0 | Jark | 2 |
| 2017-10-10 10:01:58.0 | 2017-10-10 10:02:28.0 | Jark | 1 |
| 2017-10-10 10:02:10.0 | 2017-10-10 10:02:40.0 | Timo | 1 |

#### 3.9.5. OVER窗口

OVER窗口（OVER Window）是传统数据库的标准开窗，不同于Group By Window，OVER窗口中每1个元素都对应1个窗口。OVER窗口可以按照实际元素的行或实际的元素值（时间戳值）确定窗口，因此流数据元素可能分布在多个窗口中。 在应用OVER窗口的流式数据中，每1个元素都对应1个OVER窗口。每1个元素都触发1次数据计算，每个触发计算的元素所确定的行，都是该元素所在窗口的最后1行。在实时计算的底层实现中，OVER窗口的数据进行全局统一管理（数据只存储1份），逻辑上为每1个元素维护1个OVER窗口，为每1个元素进行窗口计算，完成计算后会清除过期的数据。

**语法**

```
    agg1(col1) OVER (definition1) AS colName,
    ...
    aggN(colN) OVER (definition1) AS colNameN
FROM Tab1;
```

agg1(col1)：按照GROUP BY指定col1列对输入数据进行聚合计算。 AS colName：别名。

**说明**

agg1到aggN所对应的OVER definition1必须相同。 外层SQL可以通过AS的别名查询数据。

**类型**

Flink SQL中对OVER窗口的定义遵循标准SQL的定义语法，传统OVER窗口没有对其进行更细粒度的窗口类型命名划分。按照计算行的定义方式，OVER Window可以分为以下两类： ROWS OVER Window：每1行元素都被视为新的计算行，即每1行都是一个新的窗口。 RANGE OVER Window：具有相同时间值的所有元素行视为同一计算行，即具有相同时间值的所有行都是同一个窗口。

**属性**

| 正交属性 | 说明 | proctime | eventtime |
|---|---|---|---|
| ROWS OVER Window | 按照实际元素的行确定窗口。 | 支持 | 支持 |
| RANGE OVER Window | 按照实际的元素值（时间戳值）确定窗口。 | 支持 | 支持 |

**Rows OVER Window语义**

窗口数据 ROWS OVER Window的每个元素都确定一个窗口。ROWS OVER Window分为Unbounded（无界流）和Bounded（有界流）两种情况。 实时计算（流计算） Unbounded ROWS OVER Window数据示例如下图所示。 虽然上图所示窗口user1的w7、w8及user2的窗口w3、w4都是同一时刻到达，但它们仍然在不同的窗口，这一点与RANGE OVER Window不同。

**说明**

Bounded ROWS OVER Window数据以3个元素（往前2个元素）的窗口为例，如下图所示。 虽然上图所示窗口user1的w5、w6及user2的窗口w1、w2都是同一时刻到达，但它们仍然在不同的窗口，这一点与RANGE OVER Window不同。

**说明**

窗口语法

```
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     ROWS
     BETWEEN (UNBOUNDED | rowCount) PRECEDING AND CURRENT ROW) AS colName, ...
FROM Tab1;
```

value_expression：分区值表达式。 timeCol：元素排序的时间字段。 案例以Bounded ROWS OVER Window场景为例。假设，一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。要求输出在当前商品上架之前同类的3 个商品中的最高价格。 实时计算（流计算） 测试数据

| 商品ID | 商品类型 | 上架时间 | 销售价格 |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

测试代码

```
CREATE TABLE tmall_item(
   itemID VARCHAR,
   itemType VARCHAR,
   onSellTime TIMESTAMP,
   price DOUBLE,
   WATERMARK onSellTime FOR onSellTime as withOffset(onSellTime, 0)
```

)

```
WITH (
  type = 'sls',
   ...
);
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        ROWS BETWEEN 2 preceding AND CURRENT ROW) AS maxPrice
  FROM tmall_item;
```

测试结果

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 60 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

**RANGE OVER Window语义**

窗口数据 RANGE OVER Window所有具有共同元素值（元素时间戳）的元素行确定一个窗口，RANGE OVER Window分为Unbounded和Bounded的两种情况。 Unbounded RANGE OVER Window数据示例如下图所示。 实时计算（流计算）

| 说明上图所示窗口user1的w7、user2的窗口w3，两个元素同一时刻到达，属于相同的window，这一点与ROWS OVER Window不同。 |  |  |
|---|---|---|
| Bounded RANGE OVER Window数据，以3秒中数据 | (INTERVAL '2' SECOND) | 的窗口为例，如下图所示。 |

上图所示窗口user1的w6、user2的窗口w3，元素都是同一时刻到达，属于相同的window，这一点与ROWS OVER Window不同。

**说明**

窗口语法

```
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1;
```

value_expression：进行分区的字表达式。 timeCol：元素排序的时间字段。 timeInterval：定义根据当前行开始向前追溯指定时间的元素行。 案例 Bounded RANGE OVER Window场景示例：假设一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。需要求比当前商品上架时间早2分钟的同类商品中的最高价格。 实时计算（流计算） 测试数据

| 商品ID | 商品类型 | 上架时间 | 销售价格 |
|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 |

测试代码

```
CREATE TABLE tmall_item(
   itemID VARCHAR,
   itemType VARCHAR,
   onSellTime TIMESTAMP,
   price DOUBLE,
   WATERMARK onSellTime FOR onSellTime as withOffset(onSellTime, 0)
```

)

```
WITH (
  type = 'sls',
   ...
);
    itemID,
    itemType,
    onSellTime,
    price,
    MAX(price) OVER (
        PARTITION BY itemType
        ORDER BY onSellTime
        RANGE BETWEEN INTERVAL '2' MINUTE preceding AND CURRENT ROW) AS maxPrice
  FROM tmall_item;
```

测试结果

| itemID | itemType | onSellTime | price | maxPrice |
|---|---|---|---|---|
| ITEM001 | Electronic | 2017-11-11 10:01:00 | 20 | 20 |
| ITEM002 | Electronic | 2017-11-11 10:02:00 | 50 | 50 |
| ITEM003 | Electronic | 2017-11-11 10:03:00 | 30 | 50 |
| ITEM004 | Electronic | 2017-11-11 10:03:00 | 60 | 60 |
| ITEM005 | Electronic | 2017-11-11 10:05:00 | 40 | 60 |
| ITEM006 | Electronic | 2017-11-11 10:06:00 | 20 | 40 |
| ITEM007 | Electronic | 2017-11-11 10:07:00 | 70 | 70 |
| ITEM008 | Clothes | 2017-11-11 10:08:00 | 20 | 20 |

### 逻辑操作

**3.10.1. =**

**语法**

```
 A = B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A等于B，返回TRUE，否则返回FALSE。 实时计算（流计算）

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 65 | 65 |

测试语句

```
SELECT int1 as aa FROM T1 WHERE int3 = int2;
```

测试结果

**aa(INT)**

**3.10.2. >**

**语法**

```
 A > B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A大于B，返回TRUE，否则返回FALSE。

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 65 | 100 |

测试语句

```
SELECT int1 as aa FROM T1 WHERE int3 > int2;
```

测试结果

**aa(INT)**

**3.10.3. >=**

**语法**

```
 A >= B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A大于等于B，返回TRUE，否则返回FALSE。

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 65 | 65 |
| 9 | 6 | 61 |

测试语句实时计算（流计算）

```
SELECT int1 as aa FROM T1 WHERE int3 >= int2;
```

测试结果

**aa(INT)**

**3.10.4. <**

**语法**

```
 A < B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A小于B，返回TRUE，否则返回FALSE。

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 66 | 65 |
| 9 | 6 | 5 |

测试语句

```
SELECT int1 as aa FROM T1 WHERE int3 < int2;
```

测试结果

**aa(INT)**

**3.10.5. <=**

**语法**

```
 A <= B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A小于等于B，返回TRUE，否则返回FALSE。

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 66 | 65 |
| 9 | 6 | 5 |

测试语句

```
SELECT int1 as aa FROM T1 WHERE int3 <= int2;
```

实时计算（流计算） 测试结果

**aa(INT)**

**3.10.6. <>**

**语法**

```
 A <> B
```

**入参**

| 参数 | 数据类型 |
|---|---|
| A | INT |
| B | INT |

**功能描述**

如果A不等于B，返回TRUE，否则返回FALSE。

**示例**

测试数据

| int1(INT) | int2(INT) | int3(INT) |
|---|---|---|
| 97 | 66 | 6 |

测试语句

```
SELECT int1 as aa FROM T1 WHERE int3 <> int2;
```

测试结果

**aa(INT)**

#### 3.10.7. AND

**命令格式**

```
 A AND B
```

**入参**：A，B：BOOLEAN类型。

**功能描述**

如果A和B均为TRUE，则为TRUE；否则为FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 255 | 97 | 65 |

测试case

```
SELECT int2 as aa FROM T1 WHERE int1=255 AND int3=65;
```

表 2. 测试结果

**aa（int）**

#### 3.10.8. BETWEEN AND

**命令格式**

```
A BETWEEN B AND C
```

**入参**：A，B，C：DOUBLE、BIGINT、INT、VARCHAR、DATE、TIMESTAMP、TIME 类型。
实时计算（流计算）

**功能描述**

BETWEEN 操作符用于选取介于两个值之间的数据范围内的值。

**命令示例一**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 90 | 80 | 100 |
| 11 | 10 | 7 |

测试case

```
SELECT int1 as aa FROM T1 WHERE int1 BETWEEN int2 AND int3;
```

表 2. 测试结果

**aa（int）**

**命令示例二**

表 3. 测试数据

| var1(varchar) | var1(varchar) | var1(varchar) |
|---|---|---|
| b | a | c |

测试case

```
SELECT var1 as aa FROM T1 WHERE var1 BETWEEN var2 AND var3;
```

表 4. 测试结果

**aa（varchar）**

b

**命令示例三**

表 5. 测试数据

| TIMESTAMP1(TIMESTAMP) | TIMESTAMP2(TIMESTAMP) | TIMESTAMP3(TIMESTAMP) |
|---|---|---|
| 1969-07-20 20:17:30 | 1969-07-20 20:17:20 | 1969-07-20 20:17:45 |

测试case

```
SELECT TIMESTAMP1 as aa FROM T1 WHERE TIMESTAMP1 BETWEEN TIMESTAMP2 AND TIMESTAMP3;
```

表 6. 测试结果

**aa（TIMESTAMP）**

1969-07-20 20:17:30

#### 3.10.9. IS NOT FALSE

**命令格式**

**入参**：A：BOOLEAN类型。

**功能描述**

如果A是TRUE，返回TRUE。如果A是FALSE，返回FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 255 | 97 |

测试case 实时计算（流计算）

```
SELECT int2 as aa FROM T1 WHERE int1=255 IS NOT FALSE;
```

表 2. 测试结果

**aa（int）**

#### 3.10.10. IS NOT NULL

**命令格式**

**入参**：A：INT类型。

**功能描述**

如果A不为NULL，返回TRUE，否则返回FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（VARCHAR） |
|---|---|
| 97 | null |
| 9 | ww123 |

此处的 null表示空，而不是‘null’字符串。

**说明**

测试case

```
SELECT int1 as aa FROM T1 WHERE int2 IS NOT NULL;
```

表 2. 测试结果

**aa（int）**

#### 3.10.11. IS NOT TRUE

**命令格式**

**入参**：A：BOOLEAN类型。

**功能描述**

如果A是TRUE，返回FALSE、如果A是FALSE，返回TRUE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 255 | 97 |

测试case

```
SELECT int2 as aa FROM T1 WHERE int1=25 IS NOT TRUE;
```

表 2. 测试结果

**aa（int）**

#### 3.10.12. IS NOT UNKNOWN

**命令格式**

实时计算（流计算）
**入参**：A：BOOLEAN类型。

**功能描述**

A为逻辑比较表达式，例如： 6<8。 正常情况下< numeric > 与 < numeric >作逻辑比较时，A的值为TRUE 或者FALSE。当其中一个不为< numeric >数据类型时，就会出现无法比较的情况，**IS NOT**
**UNKNOWN**就是判断这种情况是否存在，即当两边无法进行正常的逻辑判断时，即A值既不是TRUE也不是FALSE，返回**FALSE**；可正常逻辑判断时，即A值为TRUE或者
FALSE，返回**TRUE**。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 255 | 97 |

测试case1

```
SELECT int2 as aa FROM T1 WHERE int1=25 IS NOT UNKNOWN;
```

表 2. 测试结果1

**aa（int）**

测试case2

```
SELECT int2 as aa FROM T1 WHERE int1 < null IS NOT UNKNOWN;
```

表 3. 测试结果2

**aa（int）**

空

#### 3.10.13. IS NULL

**命令格式**

**入参**：value ：任意类型。

**功能描述**

如果A为NULL，返回TRUE，否则返回FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（VARCHAR） |
|---|---|
| 97 | null |
| 9 | www |

**说明**

此处的 null表示空，非‘null’字符串。 测试case

```
SELECT int1 as aa FROM T1 WHERE int2 IS NULL;
```

表 2. 测试结果

**aa（int）**

#### 3.10.14. IS TRUE

**命令格式**

**入参**：A：BOOLEAN类型。

**功能描述**

实时计算（流计算） 如果A是TRUE，返回TRUE、如果A是FALSE，返回FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 255 | 97 |

测试case

```
SELECT int2 as aa FROM T1 WHERE int1=255 IS TRUE;
```

表 2. 测试结果

**aa（int）**

#### 3.10.15. IS UNKNOWN

**命令格式**

**入参**：A：BOOLEAN类型。

**功能描述**

A为逻辑比较表达式，例如： 6<>8。 正常情况下< numeric > 与 < numeric >作逻辑比较时，A值为TRUE 或者FALSE。当其中一个不为< numeric >数据类型时，就会出现无法比较的情况，**IS**
**UNKNOWN**就是判断这种情况是否存在，即当两边无法进行正常的逻辑判断时，即A值既不是TRUE也不是FALSE，返回**TRUE**；可正常逻辑判断时，即A值为TRUE或者
FALSE，返回**FALSE**。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 255 | 97 |

测试case1

```
SELECT int2 as aa FROM T1 WHERE int1=25 IS UNKNOWN;
```

表 2. 测试结果1

**aa（int）**

空测试case2

```
SELECT int2 as aa FROM T1 WHERE int1 > null IS UNKNOWN;
```

表 3. 测试结果2

**aa（int）**

#### 3.10.16. LIKE

**命令格式**

```
A LIKE B
```

**入参**：A，B：VARCHAR类型。

**功能描述**

如果匹配，返回TRUE，否则返回FALSE。 百分号（%）可用于定义通配符。

**说明**

**命令示例**

表 1. 测试数据实时计算（流计算）

**int1（INT）**

**测试case一**

```
SELECT int1 as aa FROM T1 WHERE VARCHAR2 LIKE 'ss%';
```

表 2. 测试结果一

**aa（int）**

**测试case二**

```
SELECT int1 as aa FROM T1 WHERE VARCHAR3 LIKE '%ss';
```

表 3. 测试结果二

**aa（int）**

**测试case三**

```
SELECT int1 as aa FROM T1 WHERE VARCHAR3 LIKE '%ho%';
```

表 4. 测试结果三

**aa（int）**

#### 3.10.17. NOT

**命令格式**

```
NOT A
```

**入参**：A：BOOLEAN类型。

**功能描述**

如果A是TRUE，返回FALSE、如果A是FALSE，返回TRUE。

**命令示例**

表 1. 测试数据

| int2（INT） | int3（INT） |
|---|---|
| 97 | 65 |

测试case

```
SELECT int2 as aa FROM T1 WHERE NOT int3=62;
```

实时计算（流计算） 表 2. 测试结果

**aa（int）**

#### 3.10.18. NOT BETWEEN AND

**命令格式**

```
A NOT BETWEEN B AND C
```

**入参**：A，B，C：DOUBLE、BIGINT、INT、VARCHAR、DATE、TIMESTAMP、TIME 类型。

**功能描述**

NOT BETWEEN 操作符用于选取不存在与两个值之间的数据范围内的值。

**命令示例一**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 90 | 97 | 80 |
| 11 | 10 | 7 |

测试case

```
SELECT int1 as aa FROM T1 WHERE int1 NOT BETWEEN int2 AND int3;
```

表 2. 测试结果

**aa（int）**

**命令示例二**

表 3. 测试数据

| var1(varchar) | var1(varchar) | var1(varchar) |
|---|---|---|
| d | a | c |

测试case

```
SELECT var1 as aa FROM T1 WHERE var1 NOT BETWEEN var2 AND var3;
```

表 4. 测试结果

**aa（varchar）**

d

**命令示例三**

表 5. 测试数据

| TIMESTAMP1(TIMESTAMP) | TIMESTAMP2(TIMESTAMP) | TIMESTAMP3(TIMESTAMP) |
|---|---|---|
| 1969-07-20 20:17:30 | 1969-07-20 20:17:40 | 1969-07-20 20:17:45 |

测试case

```
SELECT TIMESTAMP1 as aa FROM T1 WHERE TIMESTAMP1 NOT BETWEEN TIMESTAMP2 AND TIMESTAMP3;
```

表 6. 测试结果

**aa（TIMESTAMP）**

1969-07-20 20:17:30

**3.10.19. OR**

**命令格式**

```
 A OR B
```

**入参**：A，B：BOOLEAN类型。
实时计算（流计算）

**功能描述**

如果A和B均为TRUE，则为TRUE；否则为FALSE。

**命令示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 255 | 97 | 65 |

测试case

```
SELECT int2 as aa FROM T1 WHERE int1=255 OR int3=65;
```

表 2. 测试结果

**aa（int）**

**3.10.20. IN**

**命令格式**

```
SELECT column_name(s)
  FROM table_name
 WHERE column_name IN (value1,value2,...)
```

**入参**：value1,value2 ：必须为常数。

**功能描述**

用来查找在参数中的记录。

**命令示例**

Table 1. 测试数据

| id(Int) | LastName(Varchar) |
|---|---|
| 1 | Adams |
| 2 | Bush |
| 3 | Carter |

测试case

```
SELECT * FROM T1
 WHERE LastName IN ('Adams','Carter')
```

Table 2. 测试结果

| id(Int) | LastName(Varchar) |
|---|---|
| 1 | Adams |
| 3 | Carter |

#### 3.10.21. NOT IN

**命令格式**

```
SELECT column_name(s)
  FROM table_name
```

**入参**：value1,value2 ：必须为常数。

**功能描述**

用来查找不在参数中的记录。

**命令示例**

Table 1. 测试数据

| id(Int) | LastName(Varchar) |
|---|---|
| 1 | Adams |
| 2 | Bush |
| 3 | Carter |

实时计算（流计算） 测试case

```
SELECT * FROM T1
```

Table 2. 测试结果

| id(Int) | LastName(Varchar) |
|---|---|
| 2 | Bush |

#### 3.10.22. IS DISTINCT FROM

**命令格式**

**入参**：A,B ：泛型。

**功能描述**

两个值是否相等，不同则返回true，不同类型的数据类型返回true，两值数据类型、值相同返回false，将空值视为相同。

**命令示例**

Table 1. 测试数据

| A(Int) | B(Varchar) |
|---|---|
| 97 | 97 |
| null | sss |
| null | null |

测试case

```
FROM T1
```

Table 2. 测试结果

**result(BOOLEAN)**

true true

#### 3.10.23. IS NOT DISTINCT FROM

**命令格式**

**入参**：A,B ：泛型。

**功能描述**

两个值是否相等，不同则返回false，不同类型的数据类型返回false，两值数据类型、值相同返回true，将空值视为相同。

**命令示例**

Table 1. 测试数据

| A(Int) | B(Varchar) |
|---|---|
| 97 | 97 |
| null | sss |
| null | null |

测试case

```
FROM T1
```

Table 2. 测试结果

**result(BOOLEAN)**

实时计算（流计算） true

### 内置函数

#### 3.11.1. 字符串函数

**3.11.1.1. 概述**

入参：A－VARCHAR类型。 功能描述：返回字符串中的字符数。 示例Table 1. 测试数据

**var1（VARCHAR）**

ss 231ee 测试case

```
FROM T1;
```

Table 2. 测试结果

**aa（INT）**

**ASCII2STR**

函数定义： `string ascii2str(int ascii)` 功能说明：将数字转换成对应的 ascii 字符；任一参数为 NULL，返回NULL。 参数说明：ascii 取值在 1-127 之间，其他值抛出异常。 示例：

```
ascii2str(9) = '\t' ascii2str(65) = 'A'
```

功能说明：字符串连接函数，将所有参数拼接成新的字符串返回；任一参数为 NULL，返回 NULL。 示例：

```
函数定义： string concat_ws(string separator, string a, string b, ...)
```

功能说明：字符串连接函数，与 concat() 函数类型，用户可以指定拼接字符串之间的分隔符 separator ；任一参数为 NULL，返回 NULL。 示例： 函数定义：

```
string substr(string a, int start) string substr(string a, int start, int len)
```

功能说明：获取字符串子串，截取从位置 start 开始长度为 len 的子串，若未指定 len 则截取到字符串结尾 start 从 1 开始，为负数时表示从字符串末尾计算位置；任一参数为 NULL，返回 NULL。 示例：

```
substr('galaxy_sql', 5) = 'xy_sql' substr('galaxy_sql', -5) = 'y_sql' substr('galaxy_sql', 5, 2) = 'xy'
```

函数定义：

```
string lcase(string a)
```

实时计算（流计算） 功能说明：将字符串中的大写字母转成小写字母，若参数为 NULL，返回 NULL 。 函数定义：

```
string ucase(string a)
```

功能说明：将字符串中的小写字母转成小写字母，若参数为 NULL，返回 NULL 。

##### TRIM

函数定义： `string trim(string a)` 功能说明：删除字符串两端的空格，若参数为 NULL，返回 NULL 。

```
示例： trim(' foobar\t ') = 'foobar\t'
```

**LTRIM**

函数定义： `string ltrim(string a)` 功能说明：删除字符串左端的空白字符，若参数为 NULL，返回 NULL 。

```
示例： ltrim(' foobar ') = 'foobar '
```

**RTRIM**

函数定义： `string rtrim(string a)` 功能说明：删除字符串右端的空格，若参数为 NULL，返回 NULL 。

```
示例： rtrim(' foobar ') = ' foobar'
```

##### LPAD

```
函数定义： string lpad(string str, int len, string pad)
```

功能说明：字符串 str 左端填充若干个字符串 pad , 直到新的字符串达到指定长度 len 为止，任一参数为 NULL，返回 NULL。 示例：

```
lpad('hi', 5, '??') = '???hi' lpad('hi', 1, '??') = 'h' lpad('---', 10, 'abc') = 'abcabca---'
```

##### RPAD

```
函数定义： string rpad(string str, int len, string pad)
```

功能说明：字符串 str 右端填充若干个字符串 pad , 直到新的字符串达到指定长度 len 为止，任一参数为NULL，返回NULL 。 示例：

```
rpad('hi', 5, '??') = 'hi???' rpad('hi', 1, '??') = 'h' rpad('---', 10, 'abc') = '---abcabca'
```

函数定义： `int length(string str)` 功能说明：计算字符串长度，任一参数为NULL，返回NULL 。 示例：

```
length('hi') = 2 length('我') = 1 length(NULL) = NULL
```

功能说明：以字符串 str 重复 n 产生新的字符串，任一参数为 NULL，返回 NULL 。 功能说明：反转字符串，任一参数为 NULL，返回 NULL 。

**SPLIT_EX**

```
函数定义： string split_ex(string str, string sep, int index)
```

功能说明：以 sep 作为分隔符，将字符串 str 分隔成若干段，取其中的第 index 段，取不到返回NULL， index 从0开始任一参数为 NULL，返回 NULL。 示例：

```
split_ex('1.2.3.4', '.', 1) = '2' split_ex('1.2.3.4', '.', -1) = NULL split_ex('1.2.3.4', '.', 4) = NULL
```

实时计算（流计算）

```
函数定义： string regexp_replace(string str, string pattern, string
      replacement)
```

功能说明：用字符串 replacement 替换字符串 str 中正则模式为 pattern 的子串，返回新的字符串。 注意：正则表达式中的斜杠（\)需要转义，任一参数为 NULL，返回 NULL。 示例：

```
regexp_replace('100-200', '(\\d+)', 'num') = 'num-num' 函数定义： string regexp_extract(string str, string pattern, int index)
```

功能说明：使用正则模式 pattern 匹配抽取字符串 str 中的第 index 个子串， index 从1开始。 注意：正则表达式中的斜杠（\)需要转义，任一参数为 NULL，返回 NULL 。 示例：

```
regexp_extract('foothebar', 'foo(.*?)(bar)', 2) = 'bar'
```

**INSTR**

```
函数定义： int instr(string str, string substr)
```

功能说明：返回字符串 str 中第一次出现字符串 substr 的位置，从1开始；若不存在该子串则返回 0。任一参数为 NULL，返回 NULL。 示例：

```
instr('foobar', 'foo') = 1 instr('foobar', 'abc') = 0 函数定义： string keyvalue(string str, string split1, string split2, string
       key_name)
```

功能说明：解析字符串中的 key-value 对，获取指定 key_name 对应的值；若不存在则返回 NULL，任一参数为 NULL，返回 NULL 。 示例：

**HASH**

函数定义： `int hash(string str)` 功能说明：返回字符串的 hashCode() 的绝对值，任一参数为 NULL，返回 NULL。

**MD5**

函数定义： `string md5(string str)` 功能说明：返回字符串的 MD5 值，如果参数为 NULL 或空串，返回空串。

##### 3.11.1.2. CHAR_LENGTH

**函数定义**

**入参**

A：VARCHAR类型。

**功能描述**

返回字符串中的字符数。

**函数示例**

表 1. 测试数据

**var1（VARCHAR）**

ss 231ee 测试case

```
FROM T1;
```

表 2. 测试结果

**aa（INT）**

实时计算（流计算）

##### 3.11.1.3. CHR

**函数定义**

```
VARCHAR CHR(INT ascii)
```

**入参**

ascii：INT 类型，是0到255之间的整数。如果不在此范围内，则返回NULL。

**功能描述**

将ascii码转换为字符。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 255 | 97 | 65 |

测试case

```
SELECT CHR(int1) as var1, CHR(int2) as var2, CHR(int3) as var3 FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| ÿ | a | A |

##### 3.11.1.4. CONCAT

**函数定义**

**入参**

var1：VARCHAR类型，普通字符串值。 var2：VARCHAR 类型，普通字符串值。

**功能描述**

连接两个或多个字符串值从而组成一个新的字符串。任一参数为NULL，跳过该参数。

**函数示例**

表 1. 测试数据

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| Hello | My | World |
| Hello | null | World |
| null | null | World |
| null | null | null |

测试case

```
FROM T1
```

表 2. 测试结果

**var（VARCHAR）**

HelloMyWorld HelloWorld World “”

##### 3.11.1.5. CONCAT_WS

**函数定义**

```
VARCHAR CONCAT_WS(VARCHAR separator, VARCHAR var1, VARCHAR var2, ...)
```

**入参**

实时计算（流计算） separator：VARCHAR类型，指的是分隔符号。 var1：VARCHAR类型的参数值。 var2：VARCHAR类型的参数值。

**功能描述**

将每个参数值和第一个参数separator指定的分隔符依次连接到一起组成新的字符串，长度和类型取决于输入值。

**说明**

当separator取值为null，则将separator视作空串进行拼接。 当其它参数为NULL，在执行拼接过程中跳过该为NULL的参数。

**函数示例**

表 1. 测试数据

| sep（VARCHAR） | str1（VARCHAR） | str2（VARCHAR） | str3（VARCHAR） |
|---|---|---|---|
| \| | Jack | Harry | John |
| null | Jack | Harry | John |
| \| | null | Harry | John |
| \| | Jack | null | null |

测试case

```
FROM T1
```

表 2. 测试结果

**var（VARCHAR）**

Jack|Harry|John JackHarryJohn Harry|John Jack

##### 3.11.1.6. FROM_BASE64

**函数定义**

**入参**

str：VARCHAR 类型，base64编码的字符串。

**功能描述**

将base64编码的字符串str解析成对应的binary类型数据输出。

**函数示例**

表 1. 测试数据

| a（INT） | b（BIGINT） | c（VARCHAR） |
|---|---|---|
| 1 | 1L | null |

测试case

```
from_base64(c) as var1,from_base64('SGVsbG8gd29ybGQ=') as var2 FROM T1
```

表 2. 测试结果

| var1(BINARY) | var2(BINARY) |
|---|---|
| null | Byte Array: [72(‘H’), 101(‘e’), 108(‘l’), 108(‘l’), 111(‘o’), 32(‘ ‘), 119(‘w’), 111(‘o’), 114(‘r’), 108(‘l’), 100(‘d’)] |

##### 3.11.1.7. HASH_CODE

**函数定义**

**入参**

str：VARCHAR类型。 实时计算（流计算）

**功能描述**

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | str2（VARCHAR） | nullstr（VARCHAR） |
|---|---|---|
| k1=v1;k2=v2 | k1:v1,k2:v2 | null |

测试case

```
SELECT HASH_CODE(str1) as var1, HASH_CODE(str2) as var2, HASH_CODE(nullstr) as var3 FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| 1099348823 | 401392878 | null |

##### 3.11.1.8. INITCAP

**函数定义**

**入参**

A：VARCHAR类型。

**功能描述**

返回字符串，每个字转换器的第一个字母大写，其余为小写。

**函数示例**

表 1. 测试数据

**var1（VARCHAR）**

aADvbn 测试case

```
FROM T1;
```

表 2. 测试结果

**aa（VARCHAR）**

Aadvbn

##### 3.11.1.9. JSON_VALUE

**函数定义**

```
VARCHAR JSON_VALUE(VARCHAR content, VARCHAR path)
```

**入参**

content：VARCHAR类型，需要解析的JSON对象，使用字符串表示。 path：VARCHAR类型，解析JSON的路径表达式。目前Path支持如下表达式。表 1. Path支持的表达式

| 符号 | 功能 |
|---|---|
| $ | 根对象 |
| [] | 数组下标 |
| * | 数组通配符 |
| . | 取子元素 |

**功能描述**

从JSON字符串中提取指定path的值，不合法的json和null都统一返回null。

**函数示例**

表 2. 测试数据

| id（INT） | json（VARCHAR） | path（VARCHAR） |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |

实时计算（流计算）

| 2 | {“aaa”:“bbb”,“ccc”:{“ddd”:“eee”,“fff”:“ggg”,” +”“hhh”:[“h0”,“h1”,“h2”]},“iii”:“jjj”} | $.ccc.hhh[*] |
|---|---|---|
| 3 | {“aaa”:“bbb”,“ccc”:{“ddd”:“eee”,“fff”:“ggg”,” +”“hhh”:[“h0”,“h1”,“h2”]},“iii”:“jjj”} | $.ccc.hhh[1] |
| 4 | [10, 20, [30, 40]] | NULL |
| 5 | NULL | $[2][*] |
| 6 | “{xx]” | “$[2][*]” |

测试case `id`，

```
FROM
```

`T1` 表 3. 测试结果

| id（INT） | value（VARCHAR） |
|---|---|
| 1 | [30,40] |
| 2 | [“h0”,“h1”,“h2”] |
| 3 | H1 |
| 4 | NULL |
| 5 | NULL |
| 6 | NULL |

##### 3.11.1.10. KEYVALUE

**函数定义**

```
VARCHAR KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name)
```

**入参**

split1：VARCHAR类型，kv对的分隔符。 split2：VARCHAR类型，kv的分隔符。 key_name：VARCHAR类型，kv的值。

**功能描述**

解析str字符串中的key-value对，匹配有split1（kv对的分隔符）和split2（kv的分隔符）key-value对。key_name返回对应的数值。key_name值不存在或者异常返回 NULL。

**函数示例**

表 1. 测试数据

| str（VARCHAR） | split1（VARCHAR） | split2（VARCHAR） | key1（VARCHAR） |
|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k2 |
| null | ; | \| | : |
| k1:v1\|k2:v2 | null | = | : |
| k1:v1\|k2:v2 | \| | = | null |
| k1:v1\|k2:v2 | \| | = | : |
| k1:v1\|k2:v2 | \| | = | : |

测试case

```
SELECT KEYVALUE(str, split1, split2, key1) as result FROM T1
```

表 2. 测试结果

**result（VARCHAR）**

v2 null null null null 实时计算（流计算） null

##### 3.11.1.11. LOWER

**函数定义**

**入参**

A：VARCHAR类型。

**功能描述**

返回转换为小写字符的字符串。

**函数示例**

表 1. 测试数据

**var1（VARCHAR）**

Ss yyT 测试case

```
FROM T1;
```

表 2. 测试结果

**aa（VARCHAR）**

ss yyt

##### 3.11.1.12. LPAD

**函数定义**

```
VARCHAR LPAD(VARCHAR str, INT len, VARCHAR pad)
```

**入参**

str：VARCHAR类型，起始的字符串。 len：INT类型，新的字符串的长度。 pad：VARCHAR类型，需要重复补充的字符串。

**功能描述**

字符串str左端填充若干个字符串pad，直到新的字符串达到指定长度len为止。任意参数为null时返回null，主字符串为空串或目标长度为负数时返回为null，pad为空串时， 若len不大于主字符串长度，返回主字符串裁剪后的结果，若len大于主字符串长度，返回null。

**函数示例**

表 1. 测试数据

| str（VARCHAR） | len（INT） | pad（VARCHAR） |
|---|---|---|
| “” | -2 | “” |
| HelloWorld | 15 | John |
| John | 2 | C |
| C | 4 | HelloWorld |
| null | 2 | C |
| c | 2 | null |
| asd | 2 | “” |
| “” | 2 | s |
| asd | 4 | “” |
| “” | 0 | “” |

测试case

```
SELECT LPAD(str, len, pad) AS result FROM T1
```

表 2. 测试结果实时计算（流计算）

**result（VARCHAR）**

null JohnJHelloWorld Jo HelC null null as ss null “”

**3.11.1.13. MD5**

**函数定义**

```
VARCHAR MD5(VARCHAR str)
```

**入参**

str：VARCHAR类型。

**功能描述**

返回字符串的MD5值，如果参数为NULL返回NULL，参数为空串，则返回空串。

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | str2（VARCHAR） |
|---|---|
| k1=v1;k2=v2 | null |

测试case

```
   MD5(str1) as var1,
   MD5(str2) as var2
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） |
|---|---|
| 19c17f42b4d6a90f7f9ffc2ea9bdd775 |  |

##### 3.11.1.14. OVERLAY

**函数定义**

```
VARCHAR OVERLAY ( (VARCHAR x PLACING VARCHAR y FROM INT start_position [ FOR INT length ]) )
```

**入参**

x：VARCHAR类型。 y：VARCHAR类型。 length（可选）：INT类型。

**功能描述**

用 y 替换 x 的子串。下标从 start_position 开始，替换 length+1 个字符。

**函数示例**

测试case

```
OVERLAY('abcdefg' PLACING 'hij' FROM 2 FOR 2) as result FROM T1
```

Table 1. 测试结果

**result(VARCHAR)**

ahijdefg 实时计算（流计算）

##### 3.11.1.15. PARSE_URL

**函数定义**

```
VARCHAR PARSE_URL(VARCHAR urlStr, VARCHAR partToExtract [, VARCHAR key])
```

**入参**

urlStr：VARCHAR 类型，url的字符串。 partToExtract：VARCHAR 类型，解析后获取的值。 key：VARCHAR 类型，指的是参数名。

**功能描述**

解析url，获取partToExtract的值，如partToExtract=‘QUERY’，获取url参数key的值partToExtract可取HOST、PATH、QUERY、REF、PROTOCOL、FILE、 AUTHORITY、USERINFO。

**说明**

参数为null返回null。

**函数示例**

表 1. 测试数据

| url1（VARCHAR） | nullstr（VARCHAR） |
|---|---|
| http://facebook.com/path/p1.php?query=1 | null |

测试case

```
SELECT PARSE_URL(url1, 'QUERY', 'query') as var1,
       PARSE_URL(url1, 'QUERY') as var2,
       PARSE_URL(url1, 'HOST') as var3,
       PARSE_URL(url1, 'PATH') as var4,
       PARSE_URL(url1, 'REF') as var5,
       PARSE_URL(url1, 'PROTOCOL') as var6,
       PARSE_URL(url1, 'FILE') as var7,
       PARSE_URL(url1, 'AUTHORITY') as var8,
       PARSE_URL(nullstr, 'QUERY') as var9,
       PARSE_URL(url1, 'USERINFO') as var10,
FROM T1
```

表 2. 测试结果

| var1(VARC HAR) | var2(VARC HAR) | var3(VARC HAR) | var4(VARC HAR) | var5(VARC HAR) | var6(VARC HAR) | var7(VARC HAR) | var8(VARC HAR) | var9(VARC HAR) | var10(VAR CHAR) | var11(VAR CHAR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query=1 | facebook.c om | /path/p1.ph p | null | http | /path/p1.ph p?query=1 | facebook.c om | null | null | null |

##### 3.11.1.16. POSITION

**函数定义**

**入参**

x：VARCHAR类型。 y：VARCHAR类型。

**功能描述**

返回要查询的字符串x在被查询字符串y里第一次出现的位置，类似于 LOCATE(substr,str)。

**函数示例**

测试case

```
FROM T1
```

Table 1. 测试结果

**result(INT)**

##### 3.11.1.17. REGEXP

**函数定义**

实时计算（流计算）

**入参**

str：VARCHAR 类型，指定的字符串。 pattern：VARCHAR 类型，指定的匹配模式。

**功能描述**

指定str的字符串是否匹配指定的pattern进行正则匹配，str或者pattern为空或NULL返回false。

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | pattern1（VARCHAR） |
|---|---|
| k1=v1;k2=v2 | k2* |
| k1:v1\|k2:v2 | k3 |
| null | k3 |
| k1:v1\|k2:v2 | null |
| k1:v1\|k2:v2 | ( |

测试case

```
FROM T1
```

表 2. 测试结果

**result（BOOLEAN）**

true null null

##### 3.11.1.18. REGEXP_EXTRACT

**函数定义**

```
VARCHAR REGEXP_EXTRACT(VARCHAR str, VARCHAR pattern, INT index)
```

**入参**

str：VARCHAR类型，指定的字符串。 pattern：VARCHAR类型，匹配的字符串。 index：INT类型，第几个被匹配的字符串。 正则常量请按照 Java 代码来写，因为SQL常量字符串会完全地codegen成Java代码。所以如果要描述一个数字（\d），需要写成 ‘\d’，也就是像在Java代

**说明**

码中写正则一样。

**功能描述**

使用正则模式pattern匹配抽取字符串str中的第index个子串，index从1开始正则匹配提取，参数为null或者正则不合法返回null。

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | pattern1（VARCHAR） | index1（INT） |
|---|---|---|
| foothebar | foo(.*?)(bar) | 2 |
| 100-200 | (\d+)-(\d+) | 1 |
| null | foo(.*?)(bar) | 2 |
| foothebar | null | 2 |
| foothebar | “” | 2 |
| foothebar | ( | 2 |

测试case

```
SELECT REGEXP_EXTRACT(str1, pattern1, index1) as result FROM T1
```

表 2. 测试结果

**result（VARCHAR）**

实时计算（流计算） bar null null null null

##### 3.11.1.19. REGEXP_REPLACE

**函数定义**

```
VARCHAR REGEXP_REPLACE(VARCHAR str, VARCHAR pattern, VARCHAR replacement)
```

**入参**

str：VARCHAR类型，指定的字符串。 pattern：VARCHAR类型，被替换的字符串。 replacement：VARCHAR类型，用于替换的字符串。

**说明**

正则常量请按照 Java 代码来写，因为SQL常量字符串会完全地codegen成Java代码。所以如果要描述一个数字（\d），需要写成 ‘\d’，也就是像在Java代码中写正则一样。

**功能描述**

用字符串replacement替换字符串str中正则模式为pattern的子串，返回新的字符串。正则匹配替换，参数为null或者正则不合法返回null。

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | pattern1（VARCHAR） | replace1（VARCHAR） |
|---|---|---|
| 2014-03-13 | - | “” |
| null | - | “” |
| 2014-03-13 | - | null |
| 2014-03-13 | “” | s |
| 2014-03-13 | ( | s |
| 100-200 | (\d+) | num |

测试case

```
SELECT REGEXP_REPLACE(str1, pattern1, replace1) as result FROM T1
```

表 2. 测试结果

**result（VARCHAR）**

20140313 null null 2014-03-13 null num-num

##### 3.11.1.20. REPEAT

**函数定义**

**入参**

str：VARCHAR类型，重复字符串值。 n：INT 类型，重复次数。

**功能描述**

返回以str重复字符串值，重复次数为N的新的字符串。参数为null返回null，重复次数为0或负数返回空串。

**函数示例**

表 1. 测试数据实时计算（流计算）

| str（VARCHAR） | n（INT） |
|---|---|
| J | 9 |
| Hello | 2 |
| Hello | -9 |
| null | 9 |

测试case

```
FROM T1
```

表 2. 测试结果

**result（VARCHAR）**

JJJJJJJJJ HelloHello “” null

##### 3.11.1.21. REVERSE

**函数定义**

**入参**

str：VARCHAR 类型，普通字符串值。

**功能描述**

反转字符串，返回字符串值的相反顺序。任一参数为NULL，返回NULL。

**函数示例**

表 1. 测试数据

| str1（VARCHAR） | str2（VARCHAR） | str3（VARCHAR） | str4（VARCHAR） |
|---|---|---|---|
| iPhoneX | Alibaba | World | null |

测试case

```
SELECT REVERSE(str1) as var1 ,REVERSE(str2) as var2, FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） | var4（VARCHAR） |
|---|---|---|---|
| XenohPi | ababilA | dlroW | null |

##### 3.11.1.22. RPAD

**函数定义**

```
VARCHAR RPAD(VARCHAR str, INT len, VARCHAR pad)
```

**入参**

str：VARCHAR类型，起始的字符串。 len：INT类型，新的字符串的长度。 pad：VARCHAR类型，需要重复补充的字符串。

**功能描述**

字符串str右端填充若干个字符串pad，直到新的字符串达到指定长度len为止，任意参数为null时返回null，主字符串为空串或目标长度为负数时为null，pad为空串时，若 len不大于主字符串长度，返回主字符串裁剪后的结果，若len大于主字符串长度，返回null。

**函数示例**

表 1. 测试数据

| str（VARCHAR） | len（INT） | pad（VARCHAR） |
|---|---|---|
| “” | -2 | “” |
| HelloWorld | 15 | John |

实时计算（流计算）

| John | 2 | C |
|---|---|---|
| C | 4 | HelloWorld |
| null | 2 | C |
| c | 2 | null |
| asd | 2 | “” |
| “” | 2 | s |
| asd | 4 | “” |
| “” | 0 | “” |

测试case

```
SELECT RPAD(str, len, pad) as result FROM T1
```

表 2. 测试结果

**result（VARCHAR）**

null HelloWorldJohnJ Jo CHel null null as ss null “”

##### 3.11.1.23. SPLIT_INDEX

**函数定义**

```
VARCHAR SPLIT_INDEX(VARCHAR str, VARCHAR sep, INT index)
```

**入参**

str：VARCHAR类型，被分隔的字符串。 sep：VARCHAR类型，以什么为分隔符的字符串。 index：INT类型，获取的第几段参数值。

**功能描述**

以sep作为分隔符，将字符串str分隔成若干段，取其中的第index段，取不到返回NULL，index从0开始任一参数为NULL，返回NULL。

**函数示例**

表 1. 测试数据

| str（VARCHAR） | sep（VARCHAR） | index（INT） |
|---|---|---|
| Jack,John,Mary | , | 2 |
| Jack,John,Mary | , | 3 |
| Jack,John,Mary | null | 0 |
| null | , | 0 |

测试case

```
FROM T1
```

表 2. 测试结果

**var1（VARCHAR）**

Mary null null 实时计算（流计算） null

##### 3.11.1.24. STR_TO_MAP

**函数定义**

```
MAP STR_TO_MAP(VARCHAR text, VARCHAR listDelimiter, VARCHAR keyValueDelimiter)
```

**入参**

text：VARCHAR 类型，输入文本。 listDelimiter：VARCHAR 类型，用来将 text 分隔成 K-V 对，默认为逗号（,）。 keyValueDelimiter ：VARCHAR 类型，用来分隔每个 key 和 value，默认为等于号（ =）。

**说明**

Delimiter 使用的是 java 的 regex,，遇到特殊字符需要转义。

**功能描述**

使用listDelimiter将text分隔成K-V对，然后使用keyValueDelimiter分隔每个K-V对，组装成MAP返回。

**函数示例**

测试case

```
FROM T1
```

Table 1. 测试结果

**a(VARCHAR)**

v1

##### 3.11.1.25. SUBSTRING

**函数定义**

**入参**

a：VARCHAR类型，指定的字符串。 len：INT类型，截取的长度。 start：INT类型，截取从字符串a开始的位置。

**功能描述**

获取字符串子串，截取从位置start开始长度为len的子串，若未指定len则截取到字符串结尾。start 从1开始，start为零当1看待,为负数时表示从字符串末尾计算位置。

**函数示例**

表 1. 测试数据

| str（VARCHAR） | nullstr（VARCHAR） |
|---|---|
| k1=v1;k2=v2 | null |

测试case

```
SELECT SUBSTRING('', 222222222) as var1,
       SUBSTRING(str, 2) as var2,
       SUBSTRING(str, -2) as var3,
       SUBSTRING(str, -2, 1) as var4,
       SUBSTRING(str, 2, 1) as var5,
       SUBSTRING(str, 22) as var6,
       SUBSTRING(str, -22) as var7,
       SUBSTRING(str, 1) as var8,
       SUBSTRING(str, 0) as var9,
FROM T1
```

表 2. 测试结果

| var1（VARC HAR） | var2（VARC HAR） | var3（VARC HAR） | var4（VARC HAR） | var5（VARC HAR） | var6（VARC HAR） | var7（VARC HAR） | var8（VARC HAR） | var9（VARC HAR） | var10（VAR CHAR） |
|---|---|---|---|---|---|---|---|---|---|
| “” | 1=v1;k2=v2 | v2 | v | 1 | “” | “” | k1=v1;k2=v 2 | k1=v1;k2=v 2 | null |

##### 3.11.1.26. TO_BASE64

实时计算（流计算）

**函数定义**

**入参**

bin：BINARY类型。

**功能描述**

将BINARY类型数据转换成对应base64编码的字符串输出。

**函数示例**

表 1. 测试数据

**c(VARCHAR)**

SGVsbG8gd29ybGQ= SGk= SGVsbG8= 测试case

```
FROM T1
```

表 2. 测试结果

**var1（VARCHAR）**

SGVsbG8gd29ybGQ= SGk= SGVsbG8=

##### 3.11.1.27. TRIM

**函数定义**

```
VARCHAR TRIM( VARCHAR x )
```

**入参**

x：VARCHAR 类型。

**功能描述**

除掉一个字串中的字头或字尾。最常见的用途是移除字首或字尾的空白。

**函数示例**

测试case

```
SELECT TRIM(' Sample '); as result FROM T1
```

Table 1. 测试结果

**result（VARCHAR）**

Sample

##### 3.11.1.28. UPPER

**函数定义**

**入参**

A：VARCHAR类型。

**功能描述**

返回转换为大写字符的字符串。

**函数示例**

表 1. 测试数据

**var1（VARCHAR）**

ss ttee 实时计算（流计算） 测试case

```
FROM T1;
```

表 2. 测试结果

**aa(VARCHAR)**

SS TTEE

#### 3.11.2. 数学函数

**3.11.2.1. 加**

**函数定义**

```
A + B
```

**入参**

A，B：INT类型。

**功能描述**

返回A + B的结果。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 10 | 20 | 30 |

测试case

```
SELECT int1+int2+int3 as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

**3.11.2.2. 减**

**函数定义**

```
A - B
```

**入参**

A，B：INT类型。

**功能描述**

返回A - B的结果。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 10 | 10 | 30 |

测试case

```
SELECT int3 - int2 - int1 as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

**3.11.2.3. 乘**

**函数定义**

```
A * B
```

实时计算（流计算）

**入参**

A，B：INT类型。

**功能描述**

返回A * B的结果。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） | int3（INT） |
|---|---|---|
| 10 | 20 | 3 |

测试case

```
SELECT int1*int2*int3 as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

**3.11.2.4. 除**

**函数定义**

```
A / B
```

**入参**

A，B：INT类型。

**功能描述**

返回A / B的结果。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） |
|---|---|
| 8 | 4 |

测试case

```
SELECT int1 / int2 as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

##### 3.11.2.5. ABS

**函数定义**

```
DOUBLE ABS(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回A 的绝对值。

**函数示例**

表 1. 测试数据

**int1（DOUBLE）**

4.3 测试case

```
SELECT ABS(in1) as aa FROM T1;
```

表 2. 测试结果实时计算（流计算）

**aa（DOUBLE）**

4.3

##### 3.11.2.6. ACOS

**函数定义**

```
DOUBLE ACOS(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回A 的反余弦值。

**函数示例**

表 1. 测试数据

**int1（DOUBLE）**

0.7173560908995228 0.4 测试case

```
SELECT ACOS(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

0.7707963267948966 1.1592794807274085

##### 3.11.2.7. BIN

**函数定义**

```
VARCHAR BIN(BIGINT number)
```

**入参**

number：BIGINT类型。参数的隐式转换支持INT，其他类型参数不支持。

**功能描述**

将长整型参数转换为二进制形式表示，返回类型为字符串。

**函数示例**

表 1. 测试数据

| id（INT） | x（BIGINT） |
|---|---|
| 1 | 12L |
| 2 | 10L |
| 3 | 0L |
| 4 | 10000000000L |

测试case

```
SELECT id, bin(x) as var1 FROM T1
```

表 2. 测试结果

| id（INT） | var1（VARCHAR） |
|---|---|
| 1 | 1100 |
| 2 | 1010 |
| 3 | 0 |
| 4 | 1001010100000010111110010000000000 |

##### 3.11.2.8. ASIN

实时计算（流计算）

**函数定义**

```
DOUBLE ASIN(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回A的反正弦值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

0.7173560908995228 0.4 测试case

```
SELECT ASIN(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

0.8 0.41151684606748806

##### 3.11.2.9. ATAN

**函数定义**

```
DOUBLE ATAN(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回A的反正切值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

0.7173560908995228 0.4 测试case

```
SSELECT ATAN(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

0.6222796222326533 0.3805063771123649

##### 3.11.2.10. BITAND

**函数定义**

**入参**

number1：INT 类型，普通INT参数。 number2：INT 类型，普通INT参数。

**功能描述**

运算符按位与操作，输入和输出类型均为INT整型。

**函数示例**

实时计算（流计算） 表 1. 测试数据

| a（INT） | b（INT） |
|---|---|
| 2 | 3 |

测试case

```
FROM T1
```

表 2. 测试结果

**intt（INT）**

##### 3.11.2.11. BITNOT

**函数定义**

**入参**

number：INT 类型，普通INT参数。

**功能描述**

按位取反，输入和输出类型均为整型，且类型一致。

**函数示例**

表 1. 测试数据

**a（INT）**

测试case

```
SELECT BITNOT(a) as var1, FROM T1
```

表 2. 测试结果

**var1（INT）**

0xfff8

##### 3.11.2.12. BITOR

**函数定义**

**入参**

number1：INT 类型，普通INT参数。 number2：INT 类型，普通INT参数。

**功能描述**

按位取或，输入和输出类型均为整型，且类型一致。

**函数示例**

表 1. 测试数据

| a（INT） | b（INT） |
|---|---|
| 2 | 3 |

测试case

```
SELECT BITOR(a, b) as var1, FROM T1
```

表 2. 测试结果

**var1（INT）**

##### 3.11.2.13. BITXOR

实时计算（流计算）

**函数定义**

**入参**

number1：INT 类型，普通INT参数。 number2：INT 类型，普通INT参数。

**功能描述**

按位取异或，输入和输出类型均为整型，且类型一致。

**函数示例**

表 1. 测试数据

| a（INT） | b（INT） |
|---|---|
| 2 | 3 |

测试case

```
SELECT BITXOR(a, b) as var1, FROM T1
```

表 2. 测试结果

**var1（INT）**

##### 3.11.2.14. CARDINALITY

**函数定义**

**入参**

str：传入是一个数组。

**功能描述**

返回一个集合中的元素数量。

**函数示例**

表 1. 测试数据

| str（INT） | b（Array[INT]） |
|---|---|
| 1 | Array(1, 2, 3) |

测试case

```
FROM T1
```

表 2. 测试结果

**result（INT）**

##### 3.11.2.15. COS

**函数定义**

```
DOUBLE COS(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

计算数字的余弦值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

0.8 0.4 实时计算（流计算） 测试case

```
SELECT COS(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

0.6967067093471654 0.9210609940028851

##### 3.11.2.16. COT

**函数定义**

```
DOUBLE COT(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

计算数字的余切值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

0.8 0.4 测试case

```
SELECT COT(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

1.0296385570503641 0.4227932187381618

**3.11.2.17. E**

**函数定义**

```
DOUBLE E()
```

**入参**

DOUBLE类型。

**功能描述**

返回自然常数e的double类型值，返回常量 E。

**函数示例**

表 1. 测试数据

| id（INT） | X（DOUBLE） |
|---|---|
| 1 | 8.0 |

测试case

```
SELECT id, e() as dou1, E() as dou2 FROM T1
```

表 2. 测试结果

| id（INT） | dou1（DOUBLE） | dou2（DOUBLE） |
|---|---|---|
| 1 | 2.718281828459045 | 2.718281828459045 |

##### 3.11.2.18. EXP

**函数定义**

实时计算（流计算）

```
DOUBLE EXP(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回e（自然对数的底）的幂次方。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

8.0 10.0 测试case

```
SELECT EXP(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

2980.9579870417283 22026.465794806718

##### 3.11.2.19. FLOOR

**函数定义**

**入参**

A：DOUBLE类型。

**功能描述**

舍入数字，返回小于或等于数字的最大整数。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

8.123 10.321 测试case

```
FROM T1;
```

表 2. 测试结果

**aa（INT）**

**3.11.2.20. LN**

**函数定义**

```
DOUBLE ln(DOUBLE number)
```

**入参**

number：DOUBLE类型，若输入为VARCHAR类型或BIGINT类型会隐式转换到DOUBLE类型后参与运算。

**功能描述**

返回number的自然对数。返回值是DOUBLE类型的对数值。

**函数示例**

表 1. 测试数据

| ID（INT） | X（DOUBLE） |
|---|---|

实时计算（流计算）

| 1 | 100.0 |
|---|---|
| 2 | 8.0 |

测试case

```
SELECT id, ln(x) as dou1, ln(e()) as dou2 FROM T1
```

表 2. 测试结果

| ID（INT） | dou1（DOUBLE） | dou2（DOUBLE） |
|---|---|---|
| 1 | 4.605170185988092 | 1.0 |
| 2 | 2.0794415416798357 | 1.0 |

##### 3.11.2.21. LOG

**函数定义**

```
DOUBLE LOG(DOUBLE base, DOUBLE x) DOUBLE LOG(DOUBLE x)
```

**入参**

base：DOUBLE类型。 x：DOUBLE类型。

**功能描述**

返回以base为底的x的自然对数。返回值是DOUBLE类型的对数值，如果是只有一个参数的返回以x为底的自然对数。

**函数示例**

表 1. 测试数据

| ID（INT） | BASE（DOUBLE） | X（DOUBLE） |
|---|---|---|
| 1 | 10.0 | 100.0 |
| 2 | 2.0 | 8.0 |

测试case

```
SELECT id, LOG(base, x) as dou1, LOG(2) as dou2 FROM T1
```

表 2. 测试结果

| ID（INT） | dou1（DOUBLE） | dou2（DOUBLE） |
|---|---|---|
| 1 | 2.0 | 0.6931471805599453 |
| 2 | 3.0 | 0.6931471805599453 |

##### 3.11.2.22. LOG10

**函数定义**

**入参**

x：DOUBLE类型。

**功能描述**

返回以10为底的自然对数，若x为NULL，则返回NULL；若x为负数，会引发异常。

**函数示例**

表 1. 测试数据

| id（INT） | X（INT） |
|---|---|
| 1 | 100 |
| 2 | 10 |

测试case

```
FROM T1
```

表 2. 测试结果实时计算（流计算）

| ID（INT） | dou1（DOUBLE） |
|---|---|
| 1 | 2.0 |
| 2 | 1.0 |

##### 3.11.2.23. LOG2

**函数定义**

```
DOUBLE LOG2(DOUBLE x)
```

**入参**

x：DOUBLE类型，2的倍数。

**功能描述**

返回以2为底的自然对数，若x为NULL，则返回NULL；若x为负数，会引发异常。

**函数示例**

表 1. 测试数据

| id（INT） | X（INT） |
|---|---|
| 1 | 8 |
| 2 | 2 |

测试case

```
SELECT id, log2(x) as dou1 FROM T1
```

表 2. 测试结果

| ID（INT） | dou1（DOUBLE） |
|---|---|
| 1 | 3.0 |
| 2 | 1.0 |

**3.11.2.24. PI**

**函数定义**

```
DOUBLE PI( )
```

**功能描述**

获取圆周率常量PI值。

**函数示例**

表 1. 测试数据

| id（INT） | X（INT） |
|---|---|
| 1 | 8 |

测试case

```
SELECT id, PI() as dou1 FROM T1
```

表 2. 测试结果

| ID（INT） | dou1（DOUBLE） |
|---|---|
| 1 | 3.141592653589793 |

##### 3.11.2.25. POWER

**函数定义**

**入参**

A，B：DOUBLE类型。

**功能描述**

返回A的B次方。 实时计算（流计算）

**函数示例**

表 1. 测试数据

| in1（DOUBLE） | in2（DOUBLE） |
|---|---|
| 2.0 | 4.0 |

测试case

```
FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

16.0

##### 3.11.2.26. RAND

**函数定义**

```
DOUBLE RAND([BIGINT seed])
```

**入参**

seed：BIGINT类型随机数，决定随机数序列的起始值。

**功能描述**

返回大于等于0且小于1之间的DOUBLE类型随机数，返回值区间为 `[0,1)` 。

**函数示例**

表 1. 测试数据

| id（INT） | X（INT） |
|---|---|
| 1 | 8 |

测试case

```
SELECT id, rand(1) as dou1, rand(3) as dou2 FROM T1
```

表 2. 测试结果

| id（INT） | dou1（DOUBLE） | dou2（DOUBLE） |
|---|---|---|
| 1 | 0.7308781907032909 | 0.731057369148862 |

##### 3.11.2.27. SIN

**函数定义**

```
DOUBLE SIN(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回a的正弦值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

8.0 0.4 测试case

```
SELECT SIN(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

0.9893582466233818 0.3894183423086505 实时计算（流计算）

##### 3.11.2.28. SQRT

**函数定义**

```
DOUBLE SQRT(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

返回数字的平方根。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

8.0 测试case

```
SELECT SQRT(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

2.8284271247461903

##### 3.11.2.29. TAN

**函数定义**

```
DOUBLE TAN(A)
```

**入参**

A：DOUBLE类型。

**功能描述**

计算数字的正切值。

**函数示例**

表 1. 测试数据

**in1（DOUBLE）**

8.0 0.4 测试case

```
SELECT TAN(in1) as aa FROM T1;
```

表 2. 测试结果

**aa（DOUBLE）**

1.0296385570503641 0.4227932187381618

##### 3.11.2.30. CEIL

**函数定义**

```
value_class CEIL(value)
```

**入参**

value：INT、DOUBLE、BIGINT类型。

**功能描述**

产生大于或等于指定值（value）的最小整数；CEIL返回的数据类型value_class与value数据类型相同。

**函数示例**

Table 1. 测试数据实时计算（流计算）

| ID(INT) | value1(INT) | value2（DOUBLE） |
|---|---|---|
| 1 | 3 | 3.6 |

测试case

```
SELECT CEIL （value2） as result1 SELECT CEIL （value2） as result2 FROM T1
```

Table 2. 测试结果

| ID(INT) | result1(INT) | result2（DOUBLE） |
|---|---|---|
| 1 | 3 | 4.0 |

##### 3.11.2.31. CHARACTER_LENGTH

**函数定义**

**入参**

x：VARCHAR类型。

**功能描述**

返回字符串中的字符数。

**函数示例**

Table 1. 测试数据

| ID(INT) | X(VARCHAR) |
|---|---|
| 1 | StreamCompute |

测试case

```
FROM T1
```

Table 2. 测试结果

| ID(INT) | result(INT) |
|---|---|
| 1 | 13 |

##### 3.11.2.32. DEGREES

**函数定义**

**入参**

x：DOUBLE类型，弧度数值。

**功能描述**

返回X从弧度转换为度值。

**函数示例**

测试case

```
FROM T1
```

Table 1. 测试结果

**result(DOUBLE)**

180.0

##### 3.11.2.33. MOD

**函数定义**

```
Integer MOD(Integer x,Integer y)
```

**入参**

x：Integer类型。 y：Integer类型。 实时计算（流计算）

**功能描述**

整数运算中求一个整数x除以另一个整数y的余数的运算，且不考虑运算的商。当x为负值时，或者X、Y均为负值时，结果为负值。

**函数示例**

Table 1. 测试数据

| X（INT） | Y（INT） |
|---|---|
| 29 | 3 |
| -29 | 3 |
| -29 | -3 |

测试case

```
SELECT MOD(x,y) as result FROM T1
```

Table 2. 测试结果

| ID(INT) | result(INT) |
|---|---|
| 1 | 2 |
| 2 | -2 |
| 3 | -2 |

##### 3.11.2.34. ROUND

**函数定义**

**入参**

x：DECIMAL类型。

**功能描述**

把数值x字段舍入为指定的小数n位数。

**函数示例**

Table 1. 测试数据

**in1(DECIMAL)**

0.7173560908995228 0.4 测试case

```
FROM T1;
```

Table 2. 测试结果

**result(DECIMAL)**

0.72 0.40

#### 3.11.3. 日期函数

##### 3.11.3.1. CURRENT_TIMESTAMP

**函数定义**

**入参**

无

**功能描述**

返回当前UTC时间（GMT+0）的时间戳，小于北京时间8小时。

**函数示例**

测试case

```
FROM T1
```

实时计算（流计算） 表 1. 测试结果

**var1（TIMESTAMP）**

2007-04-30 13:10:02.047

##### 3.11.3.2. DATEDIFF

**函数定义**

```
INT DATEDIFF(VARCHAR enddate, VARCHAR startdate) INT DATEDIFF(TIMESTAMP enddate, VARCHAR startdate) INT DATEDIFF(VARCHAR enddate, TIMESTAMP startdate) INT DATEDIFF(TIMESTAMP enddate, TIMESTAMP startdate)
```

**入参**

startdate：TIMESTAMP类型或VARCHAR类型日期，日期格式：yyyy-MM-dd 或 yyyy-MM-dd HH:mm:ss。 enddate：TIMESTAMP类型或VARCHAR类型日期，日期格式：yyyy-MM-dd 或 yyyy-MM-dd HH:mm:ss。

**功能描述**

计算从enddate到startdate两个时间的天数差值，日期格式可以是 `yy-MM-dd` `HH:mm:ss` 或 `yy-MM-dd` 或timestamp，返回整数，若有参数为null或解析错误，返回null。

**函数示例**

表 1. 测试数据

| datetime1（VARCHAR） | datetime2（VARCHAR） | nullstr（VARCHAR） |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | null |

测试case

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as int7
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） | int7（INT） |
|---|---|---|---|---|---|---|
| 30 | 31 | -31 | null | null | null | 31 |

##### 3.11.3.3. DATE_ADD

**函数定义**

**入参**

startdate：VARCHAR类型日期，日期格式yyyy-MM-dd 或 yyyy-MM-dd HH:mm:ss。 time：TIMESTAMP类型日期。 days：INT类型，间隔的天数。

**功能描述**

返回指定startdate日期间隔后days天数的一个全新的VARCHAR类型日期，日期格式可以是yyyy-MM-dd hh:mm:ss或yyyy-MM-dd或timestamp，返回string格式的日期yyyy-MM-dd，若有参数为null或解析错误，返回null。

**函数示例**

表 1. 测试数据

| datetime1（VATCHAR） | nullstr（VATCHAR） |
|---|---|
| 2017-09-15 00:00:00 | null |

测试case

```
SELECT DATE_ADD(datetime1, 30) as var1,
        DATE_ADD(TIMESTAMP '2017-09-15 23:00:00',30) as var2,
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|

实时计算（流计算）

| 2017-10-15 | 2017-10-15 | null |
|---|---|---|

##### 3.11.3.4. DATE_FORMAT

**函数定义**

```
VARCHAR DATE_FORMAT(TIMESTAMP time, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR from_format, VARCHAR to_format)
```

入参 date：VARCHAR类型日期，默认日期格式：yyyy-MM-dd HH:mm:ss。 time：TIMESTAMP类型的日期。 from_format：指定输入日期格式。 to_format：指定输出日期格式。

**功能描述**

将字符串类型的日期从源格式转换至目标格式，第一个参数为源字符串，第二个参数from_format可选，为源字符串的格式，默认为yyyy-MM-dd hh:mm:ss，第三个参数为返回日期的的格式，返回值为转换格式后的字符串类型日期，若有参数为null或解析错误，返回null。

**函数示例**

表 1. 测试数据

| date1（VARCHAR） | datetime1（VARCHAR） | nullstr（VARCHAR） |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | null |

测试case

```
SELECT DATE_FORMAT(datetime1, 'yyMMdd') as var1,
        DATE_FORMAT(nullstr, 'yyMMdd') as var2,
        DATE_FORMAT(datetime1, nullstr) as var3,
        DATE_FORMAT(date1, 'MMdd-yyyy', nullstr) as var4,
        DATE_FORMAT(date1, 'MMdd-yyyy', 'yyyyMMdd') as var5,
        DATE_FORMAT(TIMESTAMP '2017-09-15 23:00:00', 'yyMMdd') as var6
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） | var4（VARCHAR） | var5（VARCHAR） | var6（VARCHAR） |
|---|---|---|---|---|---|
| 170915 | null | null | null | 20170915 | 170915 |

##### 3.11.3.5. DATE_SUB

**函数定义**

**入参**

startdate：VARCHAR类型日期，日期格式：yyyy-MM-dd 或 yyyy-MM-dd HH:mm:ss。 time：TIMESTAMP类型日期。 days：INT类型，指定偏移的天数。

**功能描述**

为日期减去天数，日期格式可以是yyyy-MM-dd hh:mm:ss或yyyy-MM-dd或TIMESTAMP，返回VARCHAR格式的日期yyyy-MM-dd，若有参数为null或解析错误，返回 null。

**函数示例**

表 1. 测试数据

| date1（VARCHAR） | nullstr（VARCHAR） |
|---|---|
| 2017-10-15 | null |

测试case

```
SELECT DATE_SUB(date1, 30) as var1,
        DATE_SUB(TIMESTAMP '2017-10-15 23:00:00',30) as var2,
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| 2017-09-15 | 2017-09-15 | null |

实时计算（流计算）

##### 3.11.3.6. DAYOFMONTH

**函数定义**

**入参**

date：DATE类型日期。 time：TIMESTAMP类型日期。

**功能描述**

返回输入时间参数中的日，范围1～31。

**函数示例**

表 1. 测试数据

| tsStr（VARCHAR） | dateStr（VARCHAR） | tdate（DATE） | ts（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

测试case

```
SELECT DAYOFMONTH(TIMESTAMP '2016-09-15 00:00:00') as int1,
       DAYOFMONTH(DATE '2017-09-22') as int2,
       DAYOFMONTH(tdate) as int3,
       DAYOFMONTH(ts) as int4,
       DAYOFMONTH(CAST(dateStr AS DATE)) as int5,
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） |
|---|---|---|---|---|---|
| 15 | 22 | 10 | 15 | 15 | 15 |

##### 3.11.3.7. FROM_UNIXTIME

**函数定义**

```
 VARCHAR FROM_UNIXTIME(BIGINT unixtime[, VARCHAR format])
```

入参 unixtime：BIGINT类型，秒数，unix格式的日期时间值，其它类型抛出异常。 format：VARCHAR类型，指定输出日期格式。

**功能描述**

第一个参数unixtime为长整型，是以秒为单位的时间戳，第二个参数format可选，为日期格式，默认为yyyy-MM-dd HH:mm:ss，返回VARCHAR类型的符合指定格式的日期，若有参数为null或解析错误，返回null。返回值为VARCHAR类型的日期值, 默认日期格式：yyyy-MM-dd HH:mm:ss，若指定日期格式按指定格式输出任一输入参数是 NULL，返回NULL。

**函数示例**

表 1. 测试数据

| unixtime1（INT） | nullstr（VARCHAR） |
|---|---|
| 1505404800 | null |

测试case

```
SELECT FROM_UNIXTIME(unixtime1) as var1,
        FROM_UNIXTIME(unixtime1,'MMdd-yyyy') as var2,
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| 2017-09-15 00:00:00 | 0915-2017 | null |

##### 3.11.3.8. HOUR

**函数定义**

```
  INT HOUR(TIMESTAMP timestamp)
 INT HOUR(TIME time)
```

实时计算（流计算）

**入参**

time：TIME类型时间。 time：TIMESTAMP类型时间。

**功能描述**

返回输入时间参数中的24小时制的小时数，范围0～23。

**函数示例**

表 1. 测试数据

| datetime1（VARCHAR） | time1（VARCHAR） | time2（TIME） | timestamp1（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

测试case

```
SELECT HOUR(TIMESTAMP '2016-09-20 23:33:33') as int1,
       HOUR(TIME '23:30:33') as int2,
       HOUR(time2) as int3,
       HOUR(timestamp1) as int4,
       HOUR(CAST(time1 AS TIME)) as int5,
       HOUR(CAST(datetime1 AS TIMESTAMP)) as int6
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） |
|---|---|---|---|---|---|
| 23 | 23 | 22 | 11 | 22 | 11 |

##### 3.11.3.9. LOCALTIME

**函数定义**

**入参**

无构造函数，可当作变量直接使用。

**功能描述**

以数据类型TIME的值返回会话时区中的当前时间。

**函数示例**

测试case

```
FROM T1
```

Table 1. 测试结果

**result(TIME)**

19:00:47

##### 3.11.3.10. MINUTE

**函数定义**

**入参**

time：TIME类型时间。 time：TIMESTAMP类型时间。

**功能描述**

返回输入时间参数中的分钟部分，范围0～59。

**函数示例**

表 1. 测试数据

| datetime1（VARCHAR） | time1（VARCHAR） | time2（TIME） | timestamp1（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

测试case 实时计算（流计算）

```
SELECT MINUTE(TIMESTAMP '2016-09-20 23:33:33') as int1,
       MINUTE(TIME '23:30:33') as int2,
       MINUTE(time2) as int3,
       MINUTE(timestamp1) as int4,
       MINUTE(CAST(time1 AS TIME)) as int5,
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） |
|---|---|---|---|---|---|
| 33 | 30 | 23 | 12 | 23 | 12 |

##### 3.11.3.11. MONTH

**函数定义**

入参 time：TIMESTAMP类型时间。 date：TIME类型时间。

**功能描述**

返回输入时间参数中的月份，范围1～12。

**函数示例**

表 1. 测试数据

| tsStr（VARCHAR） | dateStr（VARCHAR） | tdate（DATE） | ts（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

测试case

```
SELECT MONTH(TIMESTAMP '2016-09-15 00:00:00') as int1,
       MONTH(DATE '2017-09-22') as int2,
       MONTH(tdate) as int3,
       MONTH(ts) as int4,
       MONTH(CAST(dateStr AS DATE)) as int5,
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） |
|---|---|---|---|---|---|
| 9 | 9 | 11 | 10 | 9 | 10 |

##### 3.11.3.12. NOW

**函数定义**

```
BIGINT NOW()
```

**入参**

未指定参数时为当前系统时间的秒数。

**功能描述**

返回当前时区时间的时间戳，单位为秒，可以接受一个整型参数作为偏移值（单位：秒），加在当前时间戳上后返回UNIX_TIMESTAMP(CAST(NOW AS VARCHAR))。

**函数示例**

表 1. 测试数据

**b（VARCHAR）**

null 测试case

```
SELECT NOW() as big1, NOW(b) as big2 FROM T1
```

表 2. 测试结果

| big1（BIGINT） | big2（BIGINT） |
|---|---|
| 1403006911 | null |

实时计算（流计算）

##### 3.11.3.13. SECOND

**函数定义**

**入参**

time：TIME类型时间。 time：TIMESTAMP类型时间。

**功能描述**

返回输入时间参数中的秒数部分，范围0～59。

**函数示例**

表 1. 测试数据

| datetime1（VARCHAR） | time1（VARCHAR） | time2（TIME） | timestamp1（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 11:12:13 | 22:23:24 | 22:23:24 | 2017-10-15 11:12:13 |

测试case

```
SELECT SECOND(TIMESTAMP '2016-09-20 23:33:33') as int1,
       SECOND(TIME '23:30:33') as int2,
       SECOND(time2) as int3,
       SECOND(timestamp1) as int4,
       SECOND(CAST(time1 AS TIME)) as int5,
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） | int5（INT） | int6（INT） |
|---|---|---|---|---|---|
| 33 | 33 | 24 | 13 | 24 | 13 |

##### 3.11.3.14. TIMESTAMPADD

**函数定义**

```
TIMESTAMP TIMESTAMPADD(interval,INT int_expr,TIMESTAMP datetime_expr) DATE TIMESTAMPADD(interval,INT int_expr,DATE datetime_expr)
```

**入参**

interval

| FRACSECOND _ | 表示间隔是毫秒 |
|---|---|
| SECOND | 秒 |
| MINUTE | 分钟 |
| HOUR | 小时 |
| DAY | 天 |
| WEEK | 星期 |
| MONTH | 月 |
| QUARTER | 季度 |
| YEAR | 年 |

int_expr：增加的数量，整数。 datetime_expr：需要增加的目标时间戳或日期。

**功能描述**

函数返回数字类型与datetime_expr类型相同。将整型表达式int_expr 添加到日期或日期时间表达式 datetime_expr中。以datetime_expr的数据类型返回当前会话时区中的更新后的时间。

**函数示例**

Table 1. 测试数据

| a(TIMESTAMP) | b(DATE) |
|---|---|
| 2018-07-09 10:23:56 | 1990-02-20 |

测试语句实时计算（流计算）

```
TIMESTAMPADD(HOUR,3,a) AS `result1`, FROM T1
```

Table 2. 测试结果

| result1(TIMESTAMP) | result2(DATE) |
|---|---|
| 2018-07-09 13:23:56 | 1990-02-23 |

##### 3.11.3.15. TO_DATE

**函数定义**

**入参**

time：INT 类型，单位为天，表示从1970-1-1到当前时间的天数。 date：VARCHAR 类型，默认格式为 yyyy-MM-dd。 format：VARCHAR 类型，指定输入日期格式。

**功能描述**

将int类型的日期或者varchar类型的日期转换成Date类型。

**函数示例**

表 1. 测试数据

| date1（bigint） | date2（VARCHAR） | date3（VARCHAR） |
|---|---|---|
| 100 | 2017-09-15 | 20170915 |

测试case

```
SELECT TO_DATE(date1) as var1,
        TO_DATE(date2) as var2,
FROM T1
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） | var3（VARCHAR） |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### 3.11.3.16. TO_TIMESTAMP

**函数定义**

```
TIMESTAMP TO_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**入参**

time：BIGINT类型，单位为毫秒。 date：VARCHAR类型，默认格式为yyyy-MM-dd HH:mm:ss[.SSS]。 format：VARCHAR类型，指定输入日期格式。

**功能描述**

将bigint类型的日期或者varchar类型的日期转换成TimeStamp类型。

**函数示例**

表 1. 测试数据

| timestamp1（bigint） | timestamp2（VARCHAR） | timestamp3（VARCHAR） |
|---|---|---|
| 1513135677000 | 2017-09-15 00:00:00 | 20170915000000 |

测试case

```
SELECT TO_TIMESTAMP(timestamp1) as var1,
        TO_TIMESTAMP(timestamp2) as var2,
        TO_TIMESTAMP(timestamp3, "yyyyMMddHHmmss") as var3
FROM T1
```

表 2. 测试结果实时计算（流计算）

| var1（TIMESTAMP） | var2（TIMESTAMP） | var3（TIMESTAMP） |
|---|---|---|
| 2017-12-13 03:27:57.0 | 2017-09-15 00:00:00.0 | 2017-09-15 00:00:00.0 |

##### 3.11.3.17. UNIX_TIMESTAMP

**函数定义**

```
BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**入参**

date：VARCHAR类型日期，默认日期格式：yyyy-MM-dd HH:mm:ss。 format：VARCHAR类型, 指定输入参数日期格式。

**功能描述**

两个参数，均为可选，无参数时返回当前时间的时间戳，单位为秒，第一个参数是字符串类型的时间，第二个参数是时间的格式，默认为yyyy-MM-dd hh:mm:ss，返回值是第一个参数转换成的长整型的时间戳，单位为秒，若有参数为null或解析错误，返回null。

**函数示例**

表 1. 测试数据

**nullstr（VARCHAR）**

null 测试case

```
SELECT UNIX_TIMESTAMP() as big1, FROM T1
```

表 2. 测试结果

| big1（BIGINT） | big2（BIGINT） |
|---|---|
| 1403006911 | null |

##### 3.11.3.18. WEEK

**函数定义**

```
INT WEEK(DATE date) INT WEEK(TIMESTAMP time)
```

**入参**

date：DATE类型日期。 time：TIMESTAMP类型，时间戳格式的日期。

**功能描述**

计算指定日期在一年中的第几周，周数取值区间1~53。

**函数示例**

表 1. 测试数据

| dateStr（VARCHAR） | date1（DATE） | ts1（TIMESTAMP） |
|---|---|---|
| 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

测试case

```
SELECT WEEK(TIMESTAMP '2017-09-15 00:00:00') as int1,
        WEEK(date1) as int2, WEEK(ts1) as int3, WEEK(CAST(dateStr AS DATE)) as int4
FROM T1
```

表 2. 测试结果

| int1（INT） | int2（INT） | int3（INT） | int4（INT） |
|---|---|---|---|
| 37 | 45 | 41 | 37 |

##### 3.11.3.19. YEAR

**函数定义**

```
INT YEAR(TIMESTAMP time) INT YEAR(DATE date)
```

实时计算（流计算）

**入参**

date：DATE类型日期。 time：TIMESTAMP类型日期。

**功能描述**

返回传入时间的年份。

**函数示例**

表 1. 测试数据

| tsStr（VARCHAR） | dateStr（VARCHAR） | tdate（DATE） | ts（TIMESTAMP） |
|---|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 | 2017-11-10 | 2017-10-15 00:00:00 |

测试case

```
SELECT YEAR(TIMESTAMP '2016-09-15 00:00:00') as int1,
       YEAR(DATE '2017-09-22') as int2,
       YEAR(tdate) as int3,
       YEAR(ts) as int4,
       YEAR(CAST(dateStr AS DATE)) as int5,
       YEAR(CAST(tsStr AS TIMESTAMP))  as int6
FROM T1
```

表 2. 测试结果

| int1（BIGINT） | int2（BIGINT） | int3（BIGINT） | int4（BIGINT） | int5（BIGINT） | int6（BIGINT） |
|---|---|---|---|---|---|
| 2016 | 2017 | 2017 | 2017 | 2015 | 2017 |

#### 3.11.4. 条件函数

##### 3.11.4.1. CASE WHEN

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| a | BOOLEAN |
| b | BOOLEAN |
| c | BOOLEAN |
| d | BOOLEAN |
| e | BOOLEAN |

**功能描述**

如果a为TRUE，则返回b。 如果a为FALSE，c为TRUE，则返回d。 如果a，c均为FALSE，则返回e。

**示例**

**说明**

CASE WHEN返回常量字符串的时候，会在字符串后面补全空格。如下面的例子，返回值是 ‘ios ‘时，后面会补充数个空格。

```
then 'android' else 'ios' end as os
```

两种解决方法： 利用trim函数，去除空格。针对以上示例，可在用到os字段的位置，将os改为trim(os)。 利用cast将常量字符串转为VARCHAR类型。 测试数据

**device_type(VARCHAR)**

android ios win 测试语句1（解决方法1：利用TRIM函数） 实时计算（流计算） `trim(os), --` 这里使用了`trim`函数。

```
from(
     then 'android'
     else 'ios'
end as os FROM T1 );
```

测试语句2（解决方法2：利用CAST函数）

```
 os,
from
```

`then cast('android' as varchar) --` 这里使用了`cast`函数。 `else cast('ios' as varchar) --` 这里使用了`cast`函数。

```
end as os FROM T1 );
```

测试结果

| os(VARCHAR) | length(INT) |
|---|---|
| android | 7 |
| ios | 3 |
| ios | 3 |

##### 3.11.4.2. COALESCE

**函数定义**

**入参**

A，B是要测试的值，所有这些值类型必须相同或为Null，否则会引发异常。返回值类型和参数类型相同。

**功能描述**

该函数用于返回列表中第一个非Null的值，如果列表中所有的值都是Null，则返回Null。 至少要有一个参数，否则引发异常。

**说明**

**函数示例**

表 1. 测试数据

| var1（VARCHAR） | var2（VARCHAR） |
|---|---|
| null | 30 |

测试case

```
FROM T1;
```

表 2. 测试结果

**aa（VARCHAR）**

**3.11.4.3. IF**

**函数定义**

```
T IF(BOOLEAN testCondition, T valueTrue, T valueFalseOrNull)
```

**说明**

T 表示任意返回类型。

**入参**

testCondition：BOOLEAN类型。 valueTrue，valueFalseOrNull：参数类型必须一致，可以为任意类型。 实时计算（流计算）

**功能描述**

以第一个参数的布尔值为判断标准，若为true，则返回第二个参数，若为false，则返回第三个参数,第一个参数为null时看作false，剩下参数为null按照正常语义运行，返回值类型以T为准。

**函数示例**

表 1. 测试数据

| int1（INT） | int2（INT） | str1（VARCHAR） | str2（VARCHAR） |
|---|---|---|---|
| 1 | 2 | Jack | Harry |
| 1 | 2 | Jack | null |
| 1 | 2 | null | Harry |

测试case

```
SELECT IF(int1 < int2,str1, str2) as int1 FROM T1
```

表 2. 测试结果

**int1（VARCHAR）**

Jack Jack null

##### 3.11.4.4. IS_ALPHA

**函数定义**

**入参**

str：VARCHAR 类型，指定的字符串。

**功能描述**

str中只包含字母则返回TRUE，否则返回FALSE。

**函数示例**

表 1. 测试数据

| e（VARCHAR） | f（VARCHAR） | g（VARCHAR） |
|---|---|---|
| 3 | asd | null |

测试case

```
SELECT IS_ALPHA(e) as boo1,IS_ALPHA(f) as boo2,IS_ALPHA(g) as boo3 FROM T1
```

表 2. 测试结果

| boo1（BOOLEAN） | boo2（BOOLEAN） | boo3（BOOLEAN） |
|---|---|---|
| false | true | false |

##### 3.11.4.5. IS_DECIMAL

**函数定义**

**入参**

str：VARCHAR 类型，普通字符串。

**功能描述**

如果str字符串只包含十进制字符，则返回TRUE，否则返回FALSE。

**函数示例**

表 1. 测试数据

| a（VARCHAR） | b（VARCHAR） | c（VARCHAR） | d（VARCHAR） | e（VARCHAR） | f（VARCHAR） | g（VARCHAR） |
|---|---|---|---|---|---|---|
| 1 | 123 | 2 | 11.4445 | 3 | asd | null |

测试case 实时计算（流计算）

```
SELECT IS_DECIMAL(a) as boo1,IS_DECIMAL(b) as boo2,IS_DECIMAL(c) as boo3,
       IS_DECIMAL(d) as boo4,IS_DECIMAL(e) as boo5,IS_DECIMAL(f) as boo6,IS_DECIMAL(g) as boo7
FROM T1
```

表 2. 测试结果

| boo1（BOOLEAN） | boo2（BOOLEAN） | boo3（BOOLEAN） | boo4（BOOLEAN） | boo5（BOOLEAN） | boo6（BOOLEAN） | boo7（BOOLEAN） |
|---|---|---|---|---|---|---|
| true | true | true | true | true | false | false |

##### 3.11.4.6. IS_DIGIT

**函数定义**

**入参**

str：VARCHAR 类型，指定的字符串。

**功能描述**

str中只包含数字则返回TRUE，否则返回FALSE，返回值为BOOLEAN类型。

**函数示例**

表 1. 测试数据

| e（VARCHAR） | f（VARCHAR） | g（VARCHAR） |
|---|---|---|
| 3 | asd | null |

测试case

```
SELECT IS_DIGIT(e) as boo1,IS_DIGIT(f) as boo2,IS_DIGIT(g) as boo3 FROM T1
```

表 2. 测试结果

| boo1（BOOLEAN） | boo2（BOOLEAN） | boo3（BOOLEAN） |
|---|---|---|
| true | false | false |

##### 3.11.4.7. NULLIF

**函数定义**

**入参**

A，B：INT类型。

**功能描述**

如果值相同，则返回NULL ；如果值不同，则返回第一个参数的值。

**函数示例**

表 1. 测试数据

| var1（INT） | var2（INT） |
|---|---|
| 30 | 30 |

测试case

```
FROM T1;
```

表 2. 测试结果

**aa（VARCHAR）**

null

#### 3.11.5. 表值函数

##### 3.11.5.1. GENERATE_SERIES

**函数定义**

实时计算（流计算）

**入参**

from：INT类型，指定下界。 to：INT类型，指定上界。

**功能描述**

生成一串连续的数值，分别为from，from+1，from+2，… ，to-1

**函数示例**

表 1. 测试数据

| s（INT） | e（INT） |
|---|---|
| 1 | 3 |
| -2 | 1 |

测试case

```
SELECT s, e, v as T(v)
```

表 2. 测试结果

| s（INT） | e（INT） | v（INT） |
|---|---|---|
| 1 | 3 | 1 |
| 1 | 3 | 2 |
| -2 | 1 | -2 |
| -2 | 1 | -1 |
| -2 | 1 | -0 |

##### 3.11.5.2. JSON_TUPLE

**函数定义**

**入参**

str：JSON字符串。 path1～pathN：表示路径的字符串，前面不需要$。

**功能描述**

从JSON字符串中取出各路径字符串所表示的值。

**函数示例**

表 1. 测试数据

| d（VARCHAR） | s（VARCHAR） |
|---|---|
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”asd3”} | qwe3 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:”asd3”} | qwe2 |

测试case

```
SELECT d, v as T(v)
```

表 2. 测试结果

| d（VARCHAR） | v（VARCHAR） |
|---|---|
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”asd3”} | asd |
| {“qwe”:”asd”,”qwe2”:”asd2”,”qwe3”:”asd3”} | asd3 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:”asd3”} | asd4 |
| {“qwe”:”asd4”,”qwe2”:”asd5”,”qwe3”:”asd3”} | asd5 |

##### 3.11.5.3. STRING_SPLIT

**函数定义**

实时计算（流计算）

**入参**

separator：VARCHAR 类型，指定的分隔符的字符串。

**功能描述**

将字符串按照splitchar为分隔符分割成多个部分。

**函数示例**

表 1. 测试数据

| d（VARCHAR） | s（VARCHAR） |
|---|---|
| abc-bcd | - |
| hhh | - |

测试case

```
SELECT d, v as T(v)
```

表 2. 测试结果

| d（VARCHAR） | v（VARCHAR） |
|---|---|
| abc-bcd | abc |
| abc-bcd | bcd |
| hhh | hhh |

#### 3.11.6. 类型转换函数

##### 3.11.6.1. CAST

**函数定义**

```
CAST(A AS type)
```

**入参**

A：入参类型，详情请参见数据类型。

**功能描述**

将值转换为给定类型。

**函数示例**

表 1. 测试数据

| var1（VARCHAR） | var2（INT） |
|---|---|
| 1000 | 30 |

测试case

```
SELECT CAST(var1 AS INT) as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

#### 3.11.7. 聚合函数

##### 3.11.7.1. AVG

**函数定义**

```
AVG(A)
```

**入参**

A：支持的数值类型有TINYINT、SMALLINT、INT、BIGINT、FLOAT、DECIMAL和DOUBLE。

**功能描述**

返回平均数。

**函数示例**

表 1. 测试数据实时计算（流计算）

| var1（INT） | var2（INT） |
|---|---|
| 4 | 30 |
| 6 | 30 |

测试case

```
SELECT AVG(var1) as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

##### 3.11.7.2. CONCAT_AGG

**函数定义**

**入参**

连接符，目前只支持字符串常量。

**功能描述**

链接字符串连接本批对应字段，默认连接符“\n”。返回值VARCHAR类型连接完成后新生成的字符串。

**函数示例**

表 1. 测试数据

**c(VARCHAR)**

Hi Hi Hi Hi Hi Hi Hi Hi Hi Hi 测试case

```
SELECT concat_agg(c) as var1, FROM MyTable GROUP BY c
```

表 2. 测试结果

| var1（VARCHAR） | var2（VARCHAR） |
|---|---|
| Hi\nHi\nHi\nHi\nHi\nHi\nHi\nHi\nHi\nHi | Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi-Hi |

##### 3.11.7.3. COUNT

**函数定义**

**入参**

A 支持数值（TINYINT SMALLINT INT BIGINT FLOAT DECIMAL DOUBLE）/布尔（BOOLEAN）/字符串（VARCHAR）类型。 不支持DATE、TIME、TIMESTAMP和VARBINARY类型。

**功能描述**

返回输入数的个数。

**函数示例**

实时计算（流计算） 表 1. 测试数据

**var1（VARCHAR）**

测试case

```
FROM T1;
```

表 2. 测试结果

**aa（BIGINT）**

##### 3.11.7.4. FIRST_VALUE

**函数定义**

如果要根据参数取first，如下所示：

**入参**

value：可输入任意产生类型，只接受一个参数。 order：根据order来决定first是哪行，取order值更小的记录作为first。

**功能描述**

获取流的第一条非null数据。

**函数示例**

表 1. 测试数据

| a（BIGINT） | b（INT） | c（VARCHAR） |
|---|---|---|
| 1L | 1 | “Hello” |
| 2L | 2 | “Hello” |
| 3L | 3 | “Hello” |
| 4L | 4 | “Hello” |
| 5L | 5 | “Hello” |
| 6L | 6 | “Hello” |
| 7L | 7 | “Hello World” |
| 8L | 8 | “Hello World” |
| 20L | 20 | “Hello World” |

测试case `c,`

```
first_value(b) OVER (PARTITION BY c ORDER BY proctime RANGE UNBOUNDED preceding) as var1 from T1
```

表 2. 测试结果

| c（VARCHAR） | var1（INT） |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello World | 7 |

实时计算（流计算）

| Hello World | 7 |
|---|---|
| Hello World | 7 |

##### 3.11.7.5. LAST_VALUE

**函数定义**

如果要根据参数取last，如下所示：

**入参**

value：所有的数据类型。 order：根据order来决定last是哪行，取order值更大的记录作为last。

**功能描述**

获取流的最后一条数据。

**函数示例**

表 1. 测试数据

| a（BIGINT） | b（INT） | c（VARCHAR） |
|---|---|---|
| 1L | 1 | “Hello” |
| 2L | 2 | “Hello” |
| 3L | 3 | “Hello” |
| 4L | 4 | “Hello” |
| 5L | 5 | “Hello” |
| 6L | 6 | “Hello” |
| 7L | 7 | “Hello World” |
| 8L | 8 | “Hello World” |
| 20L | 20 | “Hello World” |

测试case `c,`

```
last_value(b) OVER (PARTITION BY c ORDER BY proctime RANGE UNBOUNDED preceding) as var1 from T1
```

表 2. 测试结果

| c（VARCHAR） | var1（INT） |
|---|---|
| Hello | 1 |
| Hello | 2 |
| Hello | 3 |
| Hello | 4 |
| Hello | 5 |
| Hello | 6 |
| Hello World | 7 |
| Hello World | 8 |
| Hello World | 20 |

##### 3.11.7.6. MAX

**函数定义**

```
 MAX(A)
```

**入参**

A 支持数值（TINYINT、SMALLINT、INT、BIGINT、FLOAT、DECIMAL和DOUBLE）/布尔（BOOLEAN）/字符串（VARCHAR）类型。 不支持DATE、TIME、TIMESTAMP和VARBINARY类型。 实时计算（流计算）

**功能描述**

返回所有输入值的值的最大值。

**函数示例**

表 1. 测试数据

**var1（INT）**

测试case

```
SELECT MAX(a) as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

##### 3.11.7.7. MIN

**函数定义**

```
 MIN(A)
```

**入参**

A 支持数值（TINYINT、SMALLINT、INT、BIGINT、FLOAT、DECIMAL和DOUBLE）/布尔（BOOLEAN）/字符串（VARCHAR）类型。 不支持DATE、TIME、TIMESTAMP和VARBINARY类型。

**功能描述**

返回所有输入值的值的最小值。

**函数示例**

表 1. 测试数据

**var1（INT）**

测试case

```
SELECT MIN(a) as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

##### 3.11.7.8. STDDEV_POP

**函数定义**

**入参**

value：BIGINT或DOUBLE类型数字。

**功能描述**

返回数值的总体标准差。

**函数示例**

表 1. 测试数据

| a（DOUBLE） | c（VARCHAR） |
|---|---|
| 0 | Hi |
| 1 | Hi |
| 2 | Hi |
| 3 | Hi |

实时计算（流计算）

| 4 | Hi |
|---|---|
| 5 | Hi |
| 6 | Hi |
| 7 | Hi |
| 8 | Hi |
| 9 | Hi |

测试case

```
FROM MyTable GROUP BY c
```

表 2. 测试结果

| c（VARCHAR） | dou1（DOUBLE） |
|---|---|
| Hi | 2.8722813232690143 |

##### 3.11.7.9. SUM

**函数定义**

```
SUM(A)
```

**入参**

A：支持数值类型（TINYINT、SMALLINT、INT、BIGINT、FLOAT、DECIMAL和DOUBLE）。

**功能描述**

返回所有输入值之间的数值之和。

**函数示例**

表 1. 测试数据

**var1（INT）**

测试case

```
SELECT sum(a) as aa FROM T1;
```

表 2. 测试结果

**aa（INT）**

##### 3.11.7.10. VAR_POP

**函数定义**

**入参**

value：数值型，可为BIGINT、DOUBLE等类型。

**功能描述**

返回指定表达式中所有值的总体统计方差。

**函数示例**

表 1. 测试数据

| a（BIGINT） | c（VARCHAR） |
|---|---|
| 2900 | Hi |
| 2500 | Hi |
| 2600 | Hi |
| 3100 | Hello |
| 11000 | Hello |

实时计算（流计算） 测试case

```
   VAR_POP(a) as `result`,
```

c

```
FROM MyTable GROUP BY c
```

表 2. 测试结果

| result(BIGINT) | c |
|---|---|
| 28889 | Hi |
| 15602500 | Hello |

#### 3.11.8. 其他函数

##### 3.11.8.1. UUID

**函数定义**

```
VARCHAR UUID()
```

**入参**

无

**功能描述**

返回通用唯一标识字符。

**函数示例**

测试case

```
SELECT uuid() as `result` FROM T1
```

表 1. 测试结果

**result（VARCHAR ）**

a364e414-e68b-4e5c-9166-65b3a153e257

### 自定义函数（UDX）

**3.12.1. 概述**

本文为您介绍如何搭建实时计算Flink版自定义函数的环境并使用自定义函数。

**重要**

仅独享模式支持自定义函数。 Blink在开源Flink SQL的基础上对性能进行了增强，Blink是阿里云实时计算版本的Flink。UDX函数仅适用于Blink，对开源Flink暂不适用。

**UDX分类**

实时计算Flink版支持以下3类自定义函数。

| UDX分类 | 描述 |
|---|---|
| UDF（User Defined Scalar Function） | 用户自定义标量值函数，其输入与输出是一对一的关系，即读入一行数据，写出一条输出值。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数，其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。可以与SQL中的GROUP BY语句一起使用。 |
| UDTF（User Defined Table-valued Function） | 自定义表值函数，调用一次函数输出多行或多列数据。 |

**UDX示例**

实时计算Flink版为您提供UDX示例，便于您快速开发业务。实时计算Flink版UDX示例中包含UDF、UDAF和UDTF的实现，示例如下。

**说明**

示例中已为您配置对应版本的开发环境，您无需进行环境搭建。 示例为Maven项目，您可以使用IntelliJ IDEA进行开发。 实时计算Flink版3.0版本 Blink_UDX_3x 实时计算Flink版2.0版本 Blink_UDX_2x 实时计算Flink版1.0版本 Blink_UDX_1x 实时计算（流计算）

**环境搭建**

以上示例主要使用的依赖JAR包如下，如果您需要单独使用，可以自行下载。 基于实时计算Flink版3.2.1以下版本 flink-streaming-java_2.11 flink-table_2.11 flink-core-blink-2.2.4 基于实时计算Flink版3.2.1及以上版本请根据需求自行添加开源版本所支持的POM依赖包。下载查看完整依赖包示例。

**说明**

如果您需要依赖Snapshot版本，可以自行添加Snapshot版本所支持的POM依赖包。

**注册使用**

1. 登录实时计算管理控制台。
2. 在顶部菜单中，单击**开发**。
3. 在左侧的导航栏中，单击**资源引用**。
4. 在**资源引用**页签的右上角，单击**新建资源**。
5. 在**上传资源**页面，输入资源配置信息。

| 参数名称 | 说明 |
|---|---|
| 上传方式 | 实时计算控制台上仅支持本地上传。 说明本地上传JAR包的大小上限为300 MB。如果JAR包大小超过300 MB，请在集群绑定的OSS控制台上，或通过OpenAPI的方式上传JAR包。 |
| 资源选择 | 单击选择资源，选择需要引用的资源。 |
| 资源名称 | 输入资源名称。 |
| 资源备注 | 输入资源备注信息。 |
| 资源类型 | 选择引用资源类型，JAR、DICTIONARY或PYTHON。 |

6. 在**资源引用**页签中，将鼠标悬停在对应作业的右侧的**更多**上。
7. 在下拉列表中，选择**引用**。
8. 在作业的编辑窗口的顶部，输入自定义函数声明，示例如下。

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

**参数与返回值类型**

实时计算Flink版支持定义Java UDX时，使用Java类型作为参数和返回值。下面为实时计算Flink版类型和Java类型的映射关系。

| 实时计算Flink版数据类型 | Java类型 |
|---|---|
| TINYINT | java.lang.Byte |
| SMALLINT | java.lang.Short |
| INT | java.lang.Integer |
| BIGINT | java.lang.Long |
| FLOAT | java.lang.Float |
| DOUBLE | java.lang.Double |
| DECIMAL | java.math.BigDecimal |
| BOOLEAN | java.lang.Boolean |
| DATE | java.sql.Date |
| TIME | java.sql.Time |
| TIMESTAMP | java.sql.Timestamp |
| CHAR | java.lang.Character |
| STRING | java.lang.String |
| VARBINARY | java.lang.byte[] |
| ARRAY | 暂不支持 |
| MAP | 暂不支持 |

**获取自定义函数参数**

自定义函数中提供了可选的 `open(FunctionContext context)` 方法， `FunctionContext` 具备参数传递功能，自定义配置项可以通过此对象来传递。 假设，您需要在作业中添加如下两个参数。

```
testKey1=lincoln test.key2=todd
```

以UDTF为例，在Open方法中通过 `context.getJobParameter` 即可获取，示例如下。 实时计算（流计算）

```
public void open(FunctionContext context) throws Exception {
      String key1 = context.getJobParameter("testKey1", "empty");
      String key2 = context.getJobParameter("test.key2", "empty");
      System.err.println(String.format("end open: key1:%s, key2:%s", key1, key2));
}
```

#### 3.12.2. 自定义标量函数（UDF）

本文为您介绍如何为实时计算Flink版自定义标量函数（UDF）搭建开发环境、编写业务代码及上线。 阿里云实时计算Flink版共享模式暂不支持自定义函数，仅独享模式支持自定义函数。

**重要**

**定义**

**搭建环境**

搭建开发环境，请参见环境搭建。

**业务代码**

UDF需要在ScalarFunction类中实现 `eval` 方法。 `open` 方法和 `close` 方法可选。 UDF默认对于相同的输入会有相同的输出。如果UDF不能保证相同的输出，例如，在UDF中调用外部服务，相同的输入值可能返回不同的结果，建议您使

**重要**

用 `override isDeterministic()` 方法，返回 `False` 。否则在某些条件下，输出结果不符合预期。例如，UDF算子前移。 以Java为例，示例代码如下。

```java
package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.ScalarFunction; public class StringLengthUdf extends ScalarFunction {
```

`//` 可选，`open`方法可以不写。

```java
    // 如果编写open方法需要声明'import org.apache.flink.table.functions.FunctionContext;'。
    @Override
    public void open(FunctionContext context) {
        }
    public long eval(String a) {
        return a == null ? 0 : a.length();
    }
    public long eval(String b, String c) {
        return eval(b) + eval(c);
    }
```

`//`可选，`close`方法可以不写。

```java
    @Override
    public void close() {
        }
}
```

**编写SQL语句**

在指定的Class中编写SQL语句，自定义函数中SQL语句示例如下。 实时计算（流计算）

```
-- udf str.length() CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf'; create table sls_stream(
    a int,
    b int,
    c varchar
) with (
    type='sls',
    endPoint='<yourEndpoint>',
    accessKeyId='<yourAccessId>',
    accessKeySecret='<yourAccessSecret>',
    startTime = '2017-07-04 00:00:00',
    project='<yourProjectName>',
    logStore='<yourLogStoreName>',
    consumerGroup='consumerGroupTest1'
); create table rds_output(
    id int,
    len bigint,
    content VARCHAR
) with (
    type='rds',
    url='yourDatabaseURL',
    tableName='<yourDatabaseTableName>',
    userName='<yourDatabaseUserName>',
    password='<yourDatabasePassword>'
); insert into rds_output
```

`a,`

```
    stringLengthUdf(c),
    c as content
from sls_stream;
```

**注册使用**

1. 登录实时计算管理控制台。
2. 在顶部菜单中，单击**开发**。
3. 在左侧的导航栏中，单击**资源引用**。
4. 在**资源引用**页签的右上角，单击**新建资源**。
5. 在**上传资源**页面，输入资源配置信息。

| 参数名称 | 说明 |
|---|---|
| 上传方式 | 实时计算控制台上仅支持本地上传。 说明本地上传JAR包的大小上限为300 MB。如果JAR包大小超过300 MB，请在集群绑定的OSS控制台上，或通过OpenAPI的方式上传JAR包。 |
| 资源选择 | 单击选择资源，选择需要引用的资源。 |
| 资源名称 | 输入资源名称。 |
| 资源备注 | 输入资源备注信息。 |
| 资源类型 | 选择引用资源类型，JAR、DICTIONARY或PYTHON。 |

6. 在**资源引用**页签中，将鼠标悬停在对应作业的右侧的**更多**上。
7. 在下拉列表中，选择**引用**。
8. 在作业的编辑窗口的顶部，输入自定义函数声明，示例如下。

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

**上线和启动**

在作业**开发**页面单击**上线**后，在**运维**页面单击**启动**，即可完成自定义函数的上线。

**常见问题**

Q：为什么实现了一个随机数生成函数，在运行时产生的值却一样？ A：如果自定义函数是无参的，并且没有声明是非确定性函数，编译期间可能会被优化成一个常量值。如果需要让函数变成非确定性函数，不被优化为常量，建议您使用 `override isDeterministic()` 方法，返回 `False` 。

#### 3.12.3. 自定义聚合函数（UDAF）

本文为您介绍如何为实时计算Flink版自定义聚合函数（UDAF）搭建开发环境、编写业务代码及上线。 阿里云实时计算Flink版共享模式暂不支持自定义函数，仅独享模式支持自定义函数。

**重要**

**定义**

实时计算（流计算）

**UDAF抽象类内部方法**

虽然UDAF可以使用Java或Scala实现，但是建议您使用Java，因为Scala的数据类型有时会造成不必要的性能损失。

**说明**

AggregateFunction的核心接口方法，如下所示： createAccumulator和getValue方法 `/*` `* @param <T> UDAF`的输出结果的类型。 `* @param <ACC> UDAF`的`accumulator`的类型。`accumulator`是`UDAF`计算中用来存放计算中间结果的数据类型。您可以需要根据需要自行设计每个`UDAF`的`accumulator`。 `*/`

```
public abstract class AggregateFunction<T, ACC> extends UserDefinedFunction {
```

`/*`

```
* 初始化AggregateFunction的accumulator。
```

* 系统在进行第一个`aggregate`计算之前，调用一次此方法。
`*/`

```
public ACC createAccumulator()；
```

`/*`
* 系统在每次`aggregate`计算完成后，调用此方法。
`*/`

```
public T getValue(ACC accumulator)； }
```

**说明**

createAccumulator和getValue可以定义在AggregateFunction抽象类内。 UDAF必须包含1个accumulate方法。 accumulate方法 `public void accumulate(ACC accumulator, ...[`用户指定的输入参数]...);

**说明**

您需要实现一个accumulate方法，来描述如何计算输入的数据，并更新数据到accumulator中。 accumulate方法的第一个参数必须是使用AggregateFunction的ACC类型的accumulator。在系统运行过程中，runtime代码会把accumulator的历史状态和您指定的上游数据（支持任意数量，任意类型的数据）作为参数，一起传递给accumulate方法。 retract和merge方法 createAccumulator、getValue和accumulate 3个方法一起使用，可以设计出一个最基本的UDAF。但是实时计算Flink版一些特殊的场景需要您提供retract和merge 两个方法才能完成。 通常，计算都是对无限流的一个提前的观测值（early firing）。既然有early firing，就会有对发出的结果的修改，这个操作叫作撤回（retract）。SQL翻译优化器会帮助您自动判断哪些情况下会产生撤回的数据，哪些操作需要处理带有撤回标记的数据。但是您需要实现一个retract方法来处理撤回的数据。

```
public void retract(ACC accumulator, ...[您指定的输入参数]...);
```

**说明**

retract方法是accumulate方法的逆操作。例如，实现Count功能的UDAF，在使用accumulate方法时，每来一条数据要加1；在使用retract方法时，就要减 1。 类似于accumulate方法，retract方法的第1个参数必须使用AggregateFunction的ACC类型的accumulator。在系统运行过程中，runtime代码会把 accumulator的历史状态，和您指定的上游数据（任意数量，任意类型的数据）一起发送给retract计算。 在实时计算Flink版中一些场景需要使用merge方法，例如session window。由于实时计算Flink版具有out of order的特性，后输入的数据有可能位于2个原本分开的 session中间，这样就把2个session合为1个session。此时，需要使用merge方法把多个accumulator合为1个accumulator。

```
public void merge(ACC accumulator, Iterable<ACC> its);
```

**说明**

merge方法的第1个参数，必须是使用AggregateFunction的ACC类型的accumulator，而且第1个accumulator是merge方法完成之后，状态所存放的地方。 merge方法的第2个参数是1个ACC类型的accumulator遍历迭代器，里面有可能存在1个或多个accumulator。

**搭建开发环境**

搭建开发环境请参见环境搭建。

**编写业务逻辑代码**

以Java为例，举例代码如下。 实时计算（流计算）

```java
import org.apache.flink.table.functions.AggregateFunction; public class CountUdaf extends AggregateFunction<Long, CountUdaf.CountAccum> {
        public long total;
    }
        CountAccum acc = new CountAccum();
        acc.total = 0;
        return acc;
    }
```

`//getValue`提供了如何通过存放状态的`accumulator`计算`count UDAF`的结果的方法。

```
        return accumulator.total;
    }
```

`//accumulate`提供了如何根据输入的数据更新`count UDAF`存放状态的`accumulator`。

```
    public void accumulate(CountAccum accumulator, Object iValue) {
        accumulator.total++;
    }
    public void merge(CountAccum accumulator, Iterable<CountAccum> its) {
            accumulator.total += other.total;
         }
    }
}
```

AggregateFunction的子类支持open和close方法作为可选方法，请参见自定义标量函数（UDF）或自定义表值函数（UDTF）的写法。

**说明**

**注册使用**

1. 登录实时计算管理控制台。
2. 在顶部菜单中，单击**开发**。
3. 在左侧的导航栏中，单击**资源引用**。
4. 在**资源引用**页签的左上角，单击**新建资源**。
5. 在**上传资源**页面，输入资源配置信息。

| 参数名称 | 说明 |
|---|---|
| 上传方式 | 实时计算控制台上仅支持本地上传。 说明本地上传JAR包的大小上限为300 MB。如果JAR包大小超过300 MB，请在集群绑定的OSS控制台上，或通过OpenAPI的方式上传JAR包。 |
| 资源选择 | 单击选择资源，选择需要引用的资源。 |
| 资源名称 | 输入资源名称。 |
| 资源备注 | 输入资源备注信息。 |
| 资源类型 | 选择引用资源类型，JAR、DICTIONARY或PYTHON。 |

6. 在**资源列表**中，将鼠标悬停在目标资源右侧的**更多**上。
7. 在下拉列表中，单击**引用**。
8. 在作业编辑窗口，输入自定义函数声明，示例如下。

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

**上线和启动**

**示例**

实时计算（流计算）

```
CREATE FUNCTION countUdaf AS 'com.hjc.test.blink.sql.udx.CountUdaf'; create table sls_stream(
   a int,
   b bigint,
   c varchar
) with (
   type='sls',
   endPoint='yourEndpoint',
   accessKeyId='yourAccessId',
   accessKeySecret='yourAccessSecret',
   startTime='2017-07-04 00:00:00',
   project='<yourPorjectName>',
   logStore='stream-test2',
   consumerGroup='consumerGroupTest3'
); create table rds_output(
   len1 bigint,
   len2 bigint
) with (
   type='rds',
   url='yourDatabaseURL',
   tableName='<yourDatabaseTableName>',
   userName='<yourDatabaseUserName>',
   password='<yourDatabasePassword>'
); insert into rds_output
   count(a),
from sls_stream;
```

#### 3.12.4. 自定义表值函数（UDTF）

本文为您介绍如何为实时计算Flink版自定义表值函数（UDTF）搭建开发环境、编写业务代码以及上线。 阿里云实时计算Flink版共享模式暂不支持自定义函数，仅独享模式支持自定义函数。

**说明**

**定义**

与自定义的标量函数类似，自定义的表值函数（UDTF）将0个、1个或多个标量值作为输入参数（可以是变长参数）。与标量函数不同，表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。

**搭建开发环境**

参见环境搭建。

**编写业务逻辑代码**

UDTF需要在TableFunction类中实现eval方法。open方法和close方法可选。以Java为例，示例代码如下。

```java
package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.TableFunction; public class SplitUdtf extends TableFunction<String> {
```

`//` 可选，`open`方法可不编写。如果编写，则需要添加声明'import org.apache.flink.table.functions.FunctionContext;'。

```java
    @Override
    public void open(FunctionContext context) {
        // ... ...
        }
    public void eval(String str) {
        String[] split = str.split("\\|");
        for (String s : split) {
            collect(s);
        }
    }
```

`//` 可选，`close`方法可不编写。

```java
    @Override
    public void close() {
        // ... ...
        }
}
```

**多行返回**

UDTF可以通过多次调用 `collect()` 实现将1行的数据转为多行返回。

**多列返回**

实时计算（流计算） UDTF不仅可以进行1行转多行，还可以1列转多列。如果您需要UDTF返回多列，只需要将返回值声明成Tuple或Row。Tuple或Row解释如下： 返回值为Tuple 实时计算Flink版支持使用Tuple1到Tuple25 ，定义1个字段到25个字段。用Tuple3来返回3个字段的UDTF示例如下。

```java
import org.apache.flink.api.java.tuple.Tuple3; import org.apache.flink.table.functions.TableFunction;
```

`//` 使用`Tuple`作为返回值，一定要显式声明`Tuple`的泛型类型, 例如，`String`、`Long`和`Integer`。

```java
public class ParseUdtf extends TableFunction<Tuple3<String, Long, Integer>> { public void eval(String str) { String[] split = str.split(",");
```

`//` 以下代码仅作示例，实际业务需要添加更多的校验逻辑。

```
String first = split[0]; long second = Long.parseLong(split[1]); int third = Integer.parseInt(split[2]); Tuple3<String, Long, Integer> tuple3 = Tuple3.of(first, second, third); collect(tuple3); } }
```

**说明**

使用Tuple时，字段值不能为null，且最多只能存在25个字段。 返回值为Row 使用Row来实现返回3个字段的UDTF示例如下。

```java
import org.apache.flink.table.types.DataType; import org.apache.flink.table.types.DataTypes; import org.apache.flink.table.functions.TableFunction; import org.apache.flink.types.Row; public class ParseUdtf extends TableFunction<Row> { public void eval(String str) { String[] split = str.split(","); String first = split[0]; long second = Long.parseLong(split[1]); int third = Integer.parseInt(split[2]); Row row = new Row(3); row.setField(0, first); row.setField(1, second); row.setField(2, third); collect(row); } @Override
```

`//` 如果返回值是`Row`，则必须重载实现`getResultType`方法，显式地声明返回的字段类型。

```
public DataType getResultType(Object[] arguments, Class[] argTypes) { return DataTypes.createRowType(DataTypes.STRING, DataTypes.LONG, DataTypes.INT); } }
```

**说明**

Row的字段值可以是null，但如果需要使用Row，必须重载实现 `getResultType` 方法。

**SQL语法**

| UDTF支持cross join和left join，在使用UDTF时需要添加 | lateral | 和 | table | 关键字。以 | ParseUdtf | 为例，需要先注册一个Function名字。 |
|---|---|---|---|---|---|---|
| CREATE FUNCTION parseUdtf AS 'com.alibaba.blink.sql.udtf.ParseUdtf'; |  |  |  |  |  |  |

cross join 左表的每一行数据都会关联上UDTF产出的每一行数据，如果UDTF不产出任何数据，则这1行不会输出。

```
select S.id, S.content, T.a, T.b, T.c from input_stream as S, lateral table(parseUdtf(content)) as T(a, b, c);
```

left join 左表的每一行数据都会关联上UDTF产出的每一行数据，如果UDTF不产出任何数据，则这1行的UDTF的字段会用null值填充。 left join UDTF语句后面必须添加 `on true` 参数。

**说明**

```
select S.id, S.content, T.a, T.b, T.c from input_stream as S left join lateral table(parseUdtf(content)) as T(a, b, c) on true;
```

**注册使用**

1. 登录实时计算管理控制台。
2. 在顶部菜单中，单击**开发**。
3. 在左侧的导航栏中，单击**资源引用**。
4. 在**资源引用**页签的右上角，单击**新建资源**。
5. 在**上传资源**页面，输入资源配置信息。

| 参数名称 | 说明 |
|---|---|

实时计算（流计算）

| 上传方式 | 实时计算控制台上仅支持本地上传。 说明本地上传JAR包的大小上限为300 MB。如果JAR包大小超过300 MB，请在集群绑定的OSS控制台上，或通过OpenAPI的方式上传JAR包。 |
|---|---|
| 资源选择 | 单击选择资源，选择需要引用的资源。 |
| 资源名称 | 输入资源名称。 |
| 资源备注 | 输入资源备注信息。 |
| 资源类型 | 选择引用资源类型，JAR、DICTIONARY或PYTHON。 |

6. 在**资源引用**页签中，将鼠标悬停在对应作业的右侧的**更多**上。
7. 在下拉列表中，选择**引用**。
8. 在作业的编辑窗口的顶部，输入自定义函数声明，示例如下。

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

**上线和启动**

自定义聚合函数（UDTF）的上线和启动步骤，请参见上线和启动。

**UDTF示例**

```
-- UDTF str.split("\\|"); create function splitUdtf as 'com.hjc.test.blink.sql.udx.SplitUdtf'; create table sls_stream( a INT, b BIGINT, c VARCHAR ) with ( type='sls', endPoint='yourEndpoint', accessKeyId='yourAccessKeyId', accessKeySecret='yourAccessSecret', startTime = '2017-07-04 00:00:00', project='yourProjectName', logStore='yourLogStoreName', consumerGroup='consumerGroupTest2' );
```

`--` 将c字段传入`splitUdtf`，切分后得到多行1列的表`T(s)`。s表示字段名字。

```
create view v1 as select a,b,c,s from sls_stream, lateral table(splitUdtf(c)) as T(s); create table rds_output( id INT, len BIGINT, content VARCHAR ) with ( type='rds', url='yourDatabaseURL', tableName='yourDatabaseTableName', userName='yourDatabaseUserName', password='yourDatabasePassword' ); insert into rds_output a,b,s from v1;
```

#### 3.12.5. 使用IntelliJ IDEA开发自定义函数

本文为您介绍如何使用IntelliJ IDEA开发实时计算Flink版自定义函数，包括搭建开发环境和实时计算Flink版作业中引用自定义函数。

**背景信息**

**重要**

仅独享模式支持自定义函数功能。 请使用IntelliJ IDEA工具开发自定义函数。

**配置Maven**

1. 下载Maven。
i. 登录Maven官网下载页面。 ii. 下载**apache-maven-3.5.3-bin.tar.gz**。 iii. 解压下载的安装包到指定目录，例如：/Users/<userName>/Documents/maven。 实时计算（流计算）
2. 配置环境变量。
i. 在Terminal中，执行 vim ~/.bash_profile 命令。 ii. 在**.bash_profile**文件中添加如下命令。

```
export M2_HOME=/Users/<userName>/Documents/maven/apache-maven-3.5.3 export PATH=$PATH:$M2_HOME/bin
```

iii. 保存并关闭**.bash_profile**文件。 iv. 执行 source ~/.bash_profile 命令使配置生效。
3. 执行 `mvn -v` 命令查看配置是否生效。
如果打印如下信息，则配置生效。

```
Apache Maven 3.5.0 (ff8f5e7444045639af65f6095c62210b5713f426; 2017-04-04T03:39:06+08:00) Maven home: /Users/<userName>/Documents/maven/apache-maven-3.5.0 Java version: 1.8.0_121, vendor: Oracle Corporation Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre Default locale: zh_CN, platform encoding: UTF-8 OS name: "mac os x", version: "10.12.6", arch: "x86_64", family: "mac"
```

**搭建开发环境**

1. 下载UDX示例。
2. 在Linux环境下解压下载文件。

```
tar xzvf RealtimeCompute-udxDemo.gz
```

3. 打开**IntelliJ IDEA**，单击**Open**打开下载的UDX示例。

**实时计算Flink版作业引用JAR包**

1. 创建Package。
ii. 在**New Package**中输入Package名称。本文以 `com.hjc.test.blink.sql.udx` 为例。 实时计算（流计算） iii. 单击**OK**。
2. 创建Class。
i. 右键单击**com.hjc.test.blink.sql.udx > New > Java Class**。 ii. 在**Create New Class**中，输入Class名称。
**Kind**保持默认选择**Class**。

**说明**

iii. 单击**OK**。
3. 在Class中输入以下代码。

| package com.hjc.test.blink.sql.udx; import org.apache.flink.table.functions.FunctionContext; import org.apache.flink.table.functions.ScalarFunction; public class StringLengthUdf extends ScalarFunction { // 可选，open方法可以不编写。 // 如果编写open方法，需要声明'import org.apache.flink.table.functions.FunctionContext;'。 @Override public void open(FunctionContext context) { } public long eval(String a) { return a == null ? 0 : a.length(); } public long eval(String b, String c) { return eval(b) + eval(c); } //可选，close方法可以不编写。 @Override public void close() { } } |  |  |  |  |
|---|---|---|---|---|
| 在Terminal中，执行 | mvn package | 或 | mvn assembly:assembly | ，将项目写入JAR包。 |
| 说明如果需要将第三方依赖写入JAR包，请使用 mvn assembly:assembly 。 编译后的JAR包为RealtimeCompute-udxDemo/target/RTCompute-udx-1.0-SNAPSHOT.jar或RealtimeCompute- udxDemo/target/RTCompute-udx-1.0-SNAPSHOT-jar-with-dependencies.jar（将第三方依赖写入JAR包）。 |  |  |  |  |

5. 实时计算Flink版作业引用JAR包。
i. 登录实时计算管理控制台。 ii. 在顶部菜单中，单击**开发**。 iii. 在左侧的导航栏中，单击**资源引用**。 iv. 在**资源引用**页签的右上角，单击**新建资源**。

| 参数名称 | 说明 |
|---|---|
| 上传方式 | 实时计算控制台上仅支持本地上传。 说明本地上传JAR包的大小上限为300 MB。如果JAR包大小超过300 MB，请在集群绑定的OSS控制台上，或通过OpenAPI的方式上传JAR包。 |
| 资源选择 | 单击选择资源，选择需要引用的资源。 |
| 资源名称 | 输入资源名称。 |
| 资源备注 | 输入资源备注信息。 |
| 资源类型 | 选择引用资源类型，JAR、DICTIONARY或PYTHON。 |

v. 在**资源引用**页签中，鼠标悬停在对应作业的右侧的**更多**上。 vi. 在下拉列表中，选择**引用**。 vii. 在作业的编辑窗口顶部，输入自定义函数声明，示例如下。

```
CREATE FUNCTION stringLengthUdf AS 'com.hjc.test.blink.sql.udx.StringLengthUdf';
```

实时计算（流计算）

## API

### 简介

您可以使用实时计算的OpenAPI来操作您在实时计算产品上的所有项目作业，达到和使用WebUI操作相同的效果。 使用OpenAPI时，您需要先构造一个 `DefaultAcsClient` 类的客户端，传入相关配置，通过构造的客户端来发送和接受请求相关信息

|  | x-request |
|---|---|
| response |  |

**机器型号**

| 机器型号和OpenAPI中 model 的对应关系，如下表所示。 |  |
|---|---|
| 机器型号 | 名称（model） |
| 4核16g | Ecs4c16g _ |
| 8核32g | Ecs8c32g _ |
| 16核64g | Ecs16c64g _ |
| 24核96g | Ecs24c96g _ |
| 32核128g | Ecs32c128g _ |
| 56核224g | Ecs56c224g _ |
| 64核256g | Ecs64c256g _ |

### OpenAPI概览

**作业**

| OpenAPI | 描述 |
|---|---|
| CheckRawPlanJson | 检测作业PlanJson的获取状态 |
| CommitJob | 提交作业 |
| CreateJob | 创建作业 |
| DeleteJob | 删除作业 |
| GetJob | 获取job信息 |
| ListJob | 搜索Job |
| OfflineJob | 下线作业 |
| StartJob | 启动作业 |
| UpdateJob | 更新作业 |
| ValidateJob | 作业语法检查 |

### 文件夹

| OpenAPI | 描述 |
|---|---|
| MVFolder | 移动文件夹 |
| CreateFolder | 创建文件夹 |
| DeleteFolder | 删除文件夹 |
| GetFolder | 获取文件夹 |
| ListChildFolder | 获取子目录 |

**实例**

| OpenAPI | 描述 |
|---|---|
| BatchGetInstanceRunSummary | 批量获取实例运行信息 |
| GetInstanceResource | 获取运行实例使用资源 |
| GetInstance | 获取运行实例详情 |
| GetInstanceCheckpoint | 获取运行实例的Checkpoint |
| GetInstanceConfig | 获取作业运行参数 |
| GetInstanceDetail | 获取实例运行的DAG图 |
| GetInstanceExceptions | 获取运行实例的Failover信息 |

实时计算（流计算）

| GetInstanceFinalState | 获取运行实例最终状态 |
|---|---|
| GetInstanceMetric | 获取运行实例的Metric信息 |
| GetInstanceRunSummary | 获取作业运行实例的运行概要 |
| ListInstance | 获取某个项目下所有的运行实例 |
| ModifyInstanceState | 修改实例状态 |
| GetRawPlanJson | 获取原始执行计划 |

| OpenAPI | 描述 |
|---|---|
| CreatePackage | 获取Package信息 |
| DeletePackage | 删除Package |
| GetPackage | 获得Package信息 |
| ListPackage | 搜索Package |
| GetRefPackageJob | 获取引用特定Package的作业 |
| UpdatePackage | 更新Package |

| OpenAPI | 描述 |
|---|---|
| CreateQueue | 创建Queue |
| DeleteQueue | 删除Queue |
| BindQueue | 绑定项目运行需要的Queue |
| UnbindQueue | 解绑项目运行的Queue |
| GetClusterQueueInfo | 获取集群中Queue的信息 |
| ListProjectBindQueue | 查询项目绑定的队列信息 |
| ListProjectBindQueueResource | 查询项目绑定的队列的资源信息 |

| OpenAPI | 描述 |
|---|---|
| CreateCluster | 创建集群 |
| ExpandCluster | 后付费集群升级 |
| DestroyCluster | 注销集群 |
| ShrinkCluster | 集群缩容 |
| ListCluster | 查询已存在集群信息 |
| ModifyMasterSpec | 变更Master机型规格 |
| GetClusterResource | 获取集群资源状态信息 |
| GetClusterEngineVersions | 获取集群引擎版本 |
| GetClusterDetails | 获取集群详情 |

| OpenAPI | 描述 |
|---|---|
| CreateProject | 创建项目 |
| DeleteProject | 删除项目 |
| GetProject | 获取项目详情 |
| ListProject | 查询您已有的项目 |

### RAM资源授权

默认情况下，您对自己创建的资源拥有完整的操作权限，可以使用本文档中列举的OpenAPI对资源进行操作。 但在主子账号的场景下，子账号刚创建时没有资格去操作主账号的资源。需要通过RAM授权的方式，给予子账号操作主账号资源的权限。 如果您不需要跨账户进行实例资源的授权和访问，您可以跳过此章节。跳过这些部分并不影响您对文档中其余部分的理解和使用。

**说明**

**授权策略（Policy）**

实时计算（流计算） 授权策略（Policy）描述授权的具体内容。授权内容主要包含效果（Effect）、资源（Resource）、对资源所授予的操作权限（Action）以及限制条件（Condition）这几个基本元素。以下内容以OpenAPI网关为例，为您介绍授权策略（Policy）。

**系统授权策略**

OpenAPI网关已经预置了两个系统权限， `AliyunApiGatewayFullAccess` 和 `AliyunApiGatewayReadOnlyAccess` ，可以在**RAM****控制台** > **策略管理**进行查看。 AliyunApiGatewayFullAccess: 管理员权限，拥有主帐号下包含OpenAPI分组、OpenAPI、流控策略、应用等所有资源的管理权限。 AliyunApiGatewayReadOnlyAccess：可以查看主帐号下包含OpenAPI分组、OpenAPI、流控策略、应用等所有资源，但不可以操作。

**授权策略**

您可以根据需要自定义管理权限，支持更为精细化的授权。可以为某个操作，也可以是某个资源。如： `GetUsers` 的编辑权限。 您可以在**RAM****控制台** > **策略管理** > **自定义授权策略**查看已经定义好的自定义授权。

**说明**

自定义授权查看、创建、修改、删除方法请参见授权策略管理。 授权策略内容填写方法请参见Policy 基本元素、Policy语法结构和下文的授权策略。

**示例:**

```json
{
  "Version": "1",
  "Statement": [
    {
  "Action": "apigateway:Describe*",
      "Resource": "*",
      "Effect": "Allow"
    }
```

]

```
}
```

此示例表示：允许所有的查看操作。

**Action（操作名称列表）格式为：**

```json
"Action":"<service-name>:<action-name>"
```

其中：

| service-name | 为：阿里云产品名称，请填写 apigateway 。 为：OpenAPI接口名称，请参照下表，支持通配符 * 。 |
|---|---|
| action-name |  |
| "Action": "apigateway:Describe*" --表示所有的查询操作。 "Action": "apigateway:*" --表示API网关所有操作。 |  |

**Resource（操作对象列表）**

Resource通常指操作对象， OpenAPI网关中的OpenAPI分组、流控策略、应用都被称为Resource，语法格式：

```
 acs:<service-name>:<region>:<account-id>:<relative-id>
```

其中：

| acs | ：Alibaba |
|---|---|
| service-name |  |
| region |  |
| account-id |  |
| relative-id |  |

| 品名称，请填写用通配符号 * |  | apigateway |
|---|---|---|
|  | * |  |
| 1234567890123456 |  |  |

Resource示例：

```
 acs:apigateway:$regionid:$accountid:apigroup/$groupId
```

Resource语法：

**鉴权规则**

以OpenAPI网关为例：

| action-name | 资源（Resource） |
|---|---|
| AbolishApi | acs:apigateway:$regionid:$accountid:apigroup/$groupId |

### 调用方式

#### 4.4.1. 签名机制

阿里云会对每个访问的请求进行身份验证，所以无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名（Signature）信息。通过使用 `Access Key ID` 和 `Access Key Secret` 进行对称加密的方法来验证请求的发送者身份。 `Access Key ID` 和 `Access Key Secret` 由阿里云官方颁发给访问者（可以通过阿里云官方网站申请和管理），其中 `Access Key ID` 用于标识访问者的身份； `Access Key Secret` 是用于加密签名字符串和服务器端验证签名字符串的密钥，仅您和阿里云知道秘钥信息，请严格保密。 阿里云提供了多种语言的SDK及第三方SDK，可以免去您对签名算法进行编码的工作。详情请参见阿里云开发工具包（SDK）。

**说明**

**签名操作**

您在访问时，需要按照下面的方法对请求进行签名处理。
1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
实时计算（流计算）

| 参数排序。 按照参数名称的字典顺序对请求中所有的请求参数（包括公共请求参数和接口的自定义参数，但不包括公共请求参数中的 | Signature | 参数）进行排序。 |
|---|---|---|
| 说明当使用GET方法提交请求时，这些参数就是请求URI中的参数部分（即URI中 ? 之后由 & 连接的部分）。 |  |  |

ii. **参数编码**。对排序之后的请求参数的名称和值分别用UTF-8字符集进行URL编码。编码的规则如下。

| 、0~9 以及字符 - 、 _ 、 . 、 ~ %XY 的格式，其中 XY 是字符对应ASCII 符，编码成 %XY%ZA… 的格式； 成 %20 ，而不是加号 + 。 的 application/x-www-form-urlencoded |  |  |  |
|---|---|---|---|
|  |  | %XY%ZA… |  |
|  | %20 | ，而不是加号 | + |
|  | application/x-www-form-urlencoded |  |  |

| - 、 | _ |
|---|---|

规则描述的编码字符串。这个算法可以用下面的percentEncode方法来实现：

```java
private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; }
```

iii. 将编码后的参数名称和值用英文等号 = 进行连接。 iv. 将等号连接得到的参数组合按参数排序排好的顺序依次使用 & 符号连接，即得到规范化请求字符串。
2. 将上一步构造的规范化字符串按照下面的规则构造成待签名的字符串。

```
StringToSign= HTTPMethod + “&” + percentEncode(“/”) + ”&” +
        percentEncode(CanonicalizedQueryString)
```

其中： `HTTPMethod` 是提交请求用的HTTP方法，比如GET。 percentEncode(“/”) 是按照参数排序中描述的URL编码规则对字符 / 进行编码得到的值，即 %2F 。 `percentEncode(CanonicalizedQueryString)` 是对步骤 1 中构造的规范化请求字符串按参数编码中描述的URL编码规则编码后得到的字符串。
3. 按照RFC2104的定义，计算待签名字符串StringToSign的HMAC值。
计算签名时使用的Key就是您持有的Access Key Secret并加上一个 & 字符（ASCII:38），使用的哈希算法是SHA1。

**说明**

4. 按照 Base64 编码规则把上面的 HMAC 值编码成字符串，即得到签名值（Signature）。
5. 将得到的签名值作为Signature参数添加到请求参数中，即完成对请求签名的过程。
得到的签名值在作为最后的请求参数值提交给ECS服务器时，要和其它参数一样，按照RFC3986的规则进行URL编码。

**说明**

**示例**

| 以DescribeRegions为例，假设使用的 | Access Key Id | 为 | testid | ， | Access Key Secret | 为 | testsecret | 。 那么签名前的请求 URL 为： |
|---|---|---|---|---|---|---|---|---|
| http://ecs.aliyuncs.com/ ?TimeStamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &Action=DescribeRegions &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2014-05-26 &SignatureVersion=1.0 |  |  |  |  |  |  |  |  |

| 计算得到的待签名字符串 | StringToSign | 为： |
|---|---|---|
| GET &%2F &AccessKeyId%3Dtestid &Action%3DDescribeRegions &Format%3DXML&SignatureMethod%3DHMAC-SHA1 &SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &SignatureVersion%3D1.0 &TimeStamp%3D2016-02-23T12%253A46%253A24Z &Version%3D2014-05-26 |  |  |

因为 `Access Key Secret` 为 `testsecret` ，所以用于计算HMAC的Key为 `testsecret&` ，计算得到的签名值为： `CT9X0VtwR86fNWSnsc6v8YGOjuE=` 将签名作为 Signature 参数加入到 URL 请求中，最后得到的 URL 为：

```
http://ecs.aliyuncs.com/ ?SignatureVersion=1.0 &Action=DescribeRegions &Format=XML &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2014-05-26 &AccessKeyId=testid &Signature=CT9X0VtwR86fNWSnsc6v8YGOjuE%3D &SignatureMethod=HMAC-SHA1 &TimeStamp=2016-02-23T12%3A46%3A24Z
```

#### 4.4.2. 请求结构

本文为您介绍OpenAPI服务的请求结构。 实时计算（流计算）

**服务地址**

API 的服务接入地址，如下所示：

| 地域 | 服务地址 |
|---|---|
| 杭州 | foas.aliyuncs.com |
| cn-shanghai:上海 | foas.[RegionId].aliyuncs.com |

**通信协议**

为了获得更高的安全性，仅支持使用HTTPS通道发送OpenAPI请求。

**字符编码**

请求及返回结果都使用UTF-8 字符集进行编码。

#### 4.4.3. 返回结果

**返回结果格式**

调用OpenAPI服务后返回数据采用统一格式：

| 返回的HTTP状态码为返回的HTTP状态码为 | 2xx | ，代表调用成功。 或 5xx ，代表调用失败。 |
|---|---|---|
|  | 4xx |  |
| 说明本文档中的返回示例为了便于用户查看，做了格式化处理，实际返回结果是没有进行换行、缩进等处理的。 |  |  |

**返回结果成功**

调用成功返回的数据格式主要有XML和JSON两种，外部系统可以在请求时传入参数来制定返回的数据格式，默认为XML格式。返回结果成功示例如下：

```
 {}
```

**返回结果错误**

调用接口出错后，将不会返回结果数据。调用方可根据每个接口对应的错误码以及下述公共错误码来定位错误原因。当调用出错时， `HTTP` 请求返回一个 `4xx` 或

| 5xx | 的 | HTTP |
|---|---|---|
| ID： HostId 。在 null |  |  |

**公共错误码**

请参见：公共错误码表。

#### 4.4.4. 公共参数

公共参数指的是所有接口调用都需要用到的参数，包含公共请求参数和公共返回参数两种。

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。

| 名称 | 类型 | 是否必选 |  | 描述 |  |
|---|---|---|---|---|---|
| Format | String | 否 |  | 返回值的类型，支持JSON与XML。默认为 XML。 |  |
| Version | String | 是 |  | OpenAPI版本号，为日期形式： YYYY-MM- DD ，本版本对应为 2018-11-11 。 |  |
| AccessKeyId | String | 是 |  | 阿里云颁发给用户的访问服务所用的密钥 ID。 |  |
| Signature | String | 是 |  | 签名结果串，关于签名的计算方法，请参见签名机制。 |  |
| SignatureMethod | String | 是 |  | 签名方式，目前支持 HMAC-SHA1 。 |  |
| Timestamp | String | 是 |  | 请求的时间戳。日期格式按照 ISO8601标准表示，并需要使用UTC时间。格式为： YYYY-MM-DDThh:mm:ssZ ，例如， 2014-05-26T12:00:00Z （为北京时间 2014年5月26日20点0分0秒）。 |  |
| SignatureVersion | String | 是 |  | 签名算法版本，目前版本是 1.0 。 |  |
| SignatureNonce | String | 是 |  | 唯一随机数，用于防止网络重放攻击。您在不同请求间要使用不同的随机数值 |  |
| ResourceOwnerAccount | String | 否 |  | 本次OpenAPI请求访问到的资源拥有者账户，即登录用户名。 此参数的使用方法，详见借助RAM实现子账号对主账号的资源访问 （只能在RAM中可对ECS资源进行授权的 Action中才能使用此参数，否则访问会被拒绝）。 |  |

公共请求参数示例实时计算（流计算）

```
https://foas.aliyuncs.com/ ?Format=xml &Version=2018-11-11 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dgI%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

…

**公共返回参数**

您发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码 `RequestId` 。 XML示例

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
<RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON示例

```json
{ "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

### 实例

#### 4.5.1. BatchGetInstanceRunSummary

根据作业类型和名称获BatchGetInstanceRunSummary（批量获取实例运行信息）接口用来批量获取某个项目下，某一类作业（批作业或者流作业）的多个Job的运行实例情况。

**调试**

您可以在OpenAPI Explorer中直接运行该接口，免去您计算签名的困扰。运行成功后，OpenAPI Explorer可以自动生成SDK代码示例。

**请求头**

除公共请求头，该接口还需要指定以下请求头。关于公共请求头，请参见公共请求参数文档。

| 名称 | 类型 | 是否必选 | 示例 | 描述 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou-pre | 集团内用户使用： 公共云预发：cn-hangzhou- pre 集团内生产：cn-hangzhou- internal 集团内预发：cn-hangzhou- internal-pre |

**请求语法**

```
GET /api/v2/projects/[projectName]/runsummary HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobNames | String | 是 | job1,job2 | 作业名称，逗号（,）分隔。 |
| jobType | String | 是 | FLINKSTREAM _ | 作业类型，批作业使用FLINK _BATCH；流作业使用FLINK _STREAM。 |
| projectName | String | 是 | testproject _ | 项目名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B10D2 | 请求ID。 |
| RunSummarys |  |  | 作业运行状态详情。 |
| RunSummary |  |  | 作业运行状态详情。 |

实时计算（流计算）

| ActualState | String | RUNNING | 返回作业的实际运行状态： WAITING：等待 RUNNING：正在运行 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |
|---|---|---|---|
| EngineJobHandler | String | aplicationx \| xxxxx _ | YARN中为作业分配的名称：ApplicationID \| JobID（JM分配的ID）。 |
| ExpectState | String | RUNNIBG | 作业期望状态： WAITING：等待 RUNNING：正在运行 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |
| Id | Long | 1 | 运行实例ID。 |
| InputDelay | Long | 300 | 业务延时。 |
| JobName | String | job1，job2 | 作业名称，多个逗号（,）分隔。 |
| LastErrorMessage | String | error | 上次错误信息。 |
| LastErrorTime | Long | 1548397575000 | 上次出现错误时间（时间戳，精确到毫秒）。 |

**示例**

请求示例

```
GET /api/v2/projects/[projectName]/runsummary HTTP/1.1 RegionId: cn-hangzhou-pre
```

公共请求头

```json
{
  "jobNames": "job1,job2"
  "jobType": "FLINK_STREAM"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <BatchGetInstanceRunSummaryResponse> <RunSummarys> <RunSummary> <ExpectState>RUNNING</ExpectState> <InputDelay>0</InputDelay> <JobName>test</JobName> <EngineJobHandler>application_1564648959240_0125\|6150954a90852814ce0c6eace9868691</EngineJobHandler> <ActualState>RUNNING</ActualState> <Id>177474</Id> </RunSummary> </RunSummarys> <RequestId>45BE0E07-8543-4EEE-BC4D-E846E4C1230D</RequestId> </BatchGetInstanceRunSummaryResponse> |  |

| JSON | 格式 |
|---|---|
| { "RunSummarys":{ "RunSummary":[ { "ExpectState":"RUNNING", "InputDelay":0, "JobName":"test", "EngineJobHandler":"application_1564648959240_0125\|6150954a90852814ce0c6eace9868691", "Id":177474, "ActualState":"RUNNING" } ] }, "RequestId":"45BE0E07-8543-4EEE-BC4D-E846E4C1230D" } |  |

**错误码**

实时计算（流计算） 访问错误中心查看更多错误码。

#### 4.5.2. GetInstance

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | 123 | InstanceID，可以通过 ListInstance 接口、 Startjob 等接口获得， 流作业当前运行实例默认填 - 1 。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 |  | 描述 |  |
|---|---|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |  |  |
|  |  |  | FF3E127B10D2 |  |  |  |
| Instance |  |  |  |  | Instance详情 |  |
| └Id | Long |  | 123 |  | InstanceID |  |
| └ProjectName | String |  | project1 |  | 项目名称 |  |
| └JobName | String |  | job1 |  | 作业名称 |  |
| └ActualState | String |  | RUNNING |  | Instance的实际状态： WAITING：等待 RUNNING：运行中 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |  |
| └ExpectState | String |  | RUNNING |  | 期望状态： RUNNING ：运行中 PAUSED：暂停 TERMINATED： 停止 SUCCESS：成功（批作业） FAILED：失败（流作业） |  |
| └JobType | String |  | FLINK_BATCH |  | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |  |
| └ApiType | String |  | SQL |  | API类型： DATASTREAM： Datastream作业 SQL ：SQL作业 |  |
| └Code | String |  | code |  | Instance的运行代码。SQL作业返回 SQL，datastream作业返回datastream配置。 |  |
| └Properties | String |  | K=V |  | 作业运行参数 |  |
| └Packages | String |  | package1.jar |  | Instance引用的package，引用多个 package逗号 , 分隔，未引用为空。 |  |
| └Starter | String |  | starter1 |  | 启动人 |  |
| └StartTime | Long |  | 1548397575000 |  | 开始时间 |  |
| └LastErrorTime | Long |  | 1548397575000 |  | 最近错误时间 |  |
| └LastErrorMessage | String |  | error |  | 最近一次错误信息 |  |
| └LastOperator | String |  | operator1 |  | 最近操作人 |  |
| └LastOperateTime | Long |  | 1548397575000 |  | 最近一次操作时间 |  |
| └PlanJson | String |  | {a:b} |  | 执行计划 |  |
| └EngineVersion | String |  | blink2.2.4 _ |  | 引擎版本 |  |
| └EngineJobHandler | String |  | application_xxxx \| xxxx |  | Instance在YARN中的名称： |  |
|  |  |  |  | application_xxxx \| xxxx | ApplicaitonID \| jobID（JM分配的Job |  |
|  |  |  |  |  | ID） 。 |  |

实时计算（流计算）

| └InputDelay | Long | 100 | 业务延迟（毫秒） |
|---|---|---|---|
| └ClusterId | String | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| └QueueName | String | root.default | 队列名称 |
| └EndTime | Long | 1548397575000 | 作业结束时间，未结束作业返回空值。 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.3. GetInstanceResource

GetInstanceResource API可以获取运行实例使用的CPU、Memory信息和提交时申请的CPU、Memory信息。未运行的作业调用GetInstanceResource OpenAPI会报错。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Resource |  |  |  | 资源情况 |
| └TotalMB | Long |  | 1024 | 实际运行使用的内存（MB） |
| └AllocatedMB | Long |  | 2048 | 作业分配的内存（MB） |
| └TotalVirtualCores | Long |  | 50 | 实际运行使用的vcore |
| └AllocatedVirtualCores | Long |  | 100 | 作业分配的vcore |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.4. GetInstanceCheckpoint

GetInstanceCheckpoint API可以获得正在运行实例作业的checkpoint，非运行状态的作业调用该方法会返回错误。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Checkpoints | String |  | {a:b} | checkpint的具体信息 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数> 实时计算（流计算）

#### 4.5.5. GetInstanceConfig

GetInstanceConfig API可以获取到运行实例的运行相关参数，返回值Config中是kv对，可以提取自己想要的运行参数。对于没有运行的作业调用本方法会报错。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Config | String |  | {a:b} | 作业运行的相关参数。 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.6. GetInstanceDetail

GetInstanceDetail API可以获得运行实例的DAG（有向无环图）图。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance接口或者Startjob接口获得。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Detail | String |  | {a:b} | 作业运行的DAG信息 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.7. GetInstanceExceptions

GetInstanceExceptions API可以获取作业运行failover的信息。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

实时计算（流计算）

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Exceptions | String |  | xxxxerror | failover的具体信息 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.8. GetInstanceFinalState

GetInstanceFinalState API可以查看运行实例在YARN上的最终状态。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填 -1L ，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Finalstate | String |  | RUNNING | YARN 上的最终状态 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.9. GetInstanceMetric

通过GetInstanceMetric API，您可以可以获取foas上某个运行实例的所有metric信息。 GetInstanceMetric API可以同时获取多个metric信息。metricjson参数详情请参见opentsdb标准协议。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称。 |

实时计算（流计算）

| metricJson | String | 是 | { "start":1547637620000, "limit":"avg:sample:50", "end":1547638420000, "queries":[ { "downsample":"20s-avg", "metric":"blink.bayes_team.huayuan_test_job. delay", "granularity":"20s", "aggregator":"max" }, { "downsample":"20s-avg", "metric":"blink.bayes_team.huayuan_test_job. fetched_delay", "granularity":"20s", "aggregator":"max" } ] } |  |  |  |  | 使用特定json来获取metric： start：metric开始时间（使用13位时间戳，精确到毫秒）。 limit： [取各条线值类型：max,avg,min]:[取值方 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | [取各条线值类型：max,avg,min]:[取值方 |  |
|  |  |  |  | max" |  |  |  | 式:bottom,above,sample]:[数目] |  |  |
|  |  |  |  |  |  | _ _ |  | max,avg,min] |  |  |
|  |  |  |  |  |  |  |  | metric： blink.[项目名称].[作业名称].[指标名称] 。常用指标名称如下表所示 ： granularity：采样时间（每隔多少秒取一个点，需要根据start和end时长来取，点数太多会造成调用超时）。 aggregator：聚合方式（按照采样时间将底层的点聚合后输出为一个点，聚合方式有最大值max，最小值 min，平均值avg三种）。 |  | blink.[项目名称].[作业名称].[指标名 |
|  |  |  |  |  | x" |  |  | 称] |  |  |
| projectName | String | 是 | project1 |  |  |  |  | 项目名称。 |  |  |
| instanceId | Long | 否 | -1 |  |  |  |  | InstanceID，流式作业只有一个运行实例，此处填 -1L ， 即在线上运行的，批作业可以通过ListInstance、Startjob等接口获得。 |  |  |

| [时间(秒)]-[取值方式： |  |
|---|---|

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Metrics.MetricName | String |  | delay | metric名称。 |
| Metrics.Dps | Map |  | k:v | 时间点和对应的metric值。 |
| Metrics.Summary | Float |  | 10.2 | 聚合后的metric值。 |
| Metrics.Tags | Map |  | k:v | metric标记。 |

**metric名称对应表**

| 参数名称 | 指标名称 |
|---|---|
| 业务延时（ms） | delay |
| 数据间隔延时（ms） | fetcheddelay _ |
| 数据等待延时（ms） | nodatadelay _ _ |
| 作业失败率 | taskfailover.rate _ |
| Source的tps数据输入 | tps.rate |
| Sink的数据输出 | sink.outTps.rate |
| Source的RPS数据输出 | parserTps.rate |
| Source的数据流量输入（byte） | inBps.rate |
| Source的脏数据比例 | parserSkipCount |
| Checkpoint Duration（ms） | lastCheckpointDuration |
| Checkpoint大小（byte） | lastCheckpointSize |
| checkpoint对齐时间（ns） | checkpointAlignmentTime |
| checkpoint数量 | checkpoints |
| 获取state的时间（ns） | rocksdbget.mean _ |
| 写入state的时间（ns） | rocksdbput.mean _ |
| seek（ns） | niagaraseek.meam / rocksdbseek.mean _ _ |

实时计算（流计算）

| state大小（byte） | state.statesize / state.statenewsize _ _ |
|---|---|
| GMS GC Time（ms） | Status.JVM.GarbageCollector.ConcurrentMarkSweep.Time |
| GMS GC Rate | Status.JVM.GarbageCollector.ConcurrentMarkSweep.Count |
| WaterMark Delay（ms） | watermarkLatency |
| 数据迟到丢弃TPS | lateRecordsDroppedRate |
| 数据迟到累计丢弃数 | numLateRecordsDropped |
| 读TT延时（ms） | input.tt.readLatency |
| Task Input TPS | numRecordsInPerSecond.rate |
| Task Output TPS | numRecordsOutPerSecond.rate |
| Input Queue Usage | buffers.inPoolUsage |
| Output Queue Usage | buffers.outPoolUsage |
| Time Used In Processing Per Second（ns） | taskLatency.sum |
| Time Used In Waiting Oputput Per Second（ns） | waitOutput.sum |
| TaskLatency Histogram Mean（ns） | taskLatency.histogram.mean |
| WaitOutput Histogram Mean（ns） | waitOutput.histogram.mean |
| WaitInput Histogram Mean（ns） | waitInput.histogram.mean |
| PartitionLatency Mean（ns） | partitionLatency.mean |
| Process MEM Rss（kb） | Status.JVM.Memory.Process.rss |
| CPU Usage | Status.JVM.CPU.Usage |
| Memory Heap Used（byte） | Status.JVM.Memory.Heap.Used |
| Memory NonHeap Used（byte） | Status.JVM.Memory.NonHeap.Used |
| Threads Count | Status.JVM.Threads.Count |
| GC(CMS) | Status.JVM.GarbageCollector.ConcurrentMarkSweep.Count |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.10. GetInstanceRunSummary

GetInstanceRunSummary OpenAPI是GetInstance接口的轻量级版本，返回作业运行时的部分信息。

| 参数 | 类型 | 是否必选 | 示例值 |  | 描述 |  |  |
|---|---|---|---|---|---|---|---|
| instanceId | Long | 是 | -1 |  | 实例ID。流作业只有一个运行实例，此处填 -1L ，指在线上运行的实例。批作业可以通过 ListInstance 、 Startj ob 等接口获得实例ID |  |  |
|  |  |  |  |  |  | Startj |  |
| jobName | String | 是 | job1 |  | 作业名称 |  |  |
| projectName | String | 是 | project1 |  | 项目名称 |  |  |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| RunSummary.Id | Long |  | 123 | InstanceID |
| RunSummary.ActualState | String |  | RUNNING | Instance的实际状态： WAITING：等待 RUNNING：运行中 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |

实时计算（流计算）

| RunSummary.ExpectState | String | RUNNING |  | 期望状态： RUNNING ：运行中 PAUSED：暂停 TERMINATED： 停止 SUCCESS：成功（批作业） FAILED：失败（流作业） |  |
|---|---|---|---|---|---|
| RunSummary.LastErrorTime | Long | 1548397575000 |  | 最近错误时间 |  |
| RunSummary.LastErrorMessage | String | error |  | 最近错误信息 |  |
| RunSummary.EngineJobHandler | String | application_**** \| **** |  | Instance在YARN中的名称： |  |
|  |  |  | application_**** \| **** | ApplicaitonID \| jobID（JM分配的Job |  |
|  |  |  |  | ID） 。 |  |
| RunSummary.InputDelay | Long | 20 |  | 业务延时（毫秒） |  |
| RunSummary.JobName | String | job1 |  | 作业名称 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.11. GetRawPlanJson

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |
| autoconfEnable | Boolean | 否 | true | 是否开启智能调优，开启或根据作业历史metric，生成一份执行计划；不开启则使用默认执行计划， 默认开启 |
| expectedCore | Float | 否 | 1 | 期望cpu数 |
| expectedGB | Float | 否 | 4 | 期望内存 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| SessionId | String |  | xxxxxx | 会话ID，需要传入checkrowplanjson接口中配合使用。 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.12. ListInstance

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 否 | job1 | 作业名称。 |
| jobType | String | 是 | FLINKSTREAM _ | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| projectName | String | 是 | project1 | 项目名称。 |
| actualState | String | 否 | RUNNING | Instance的实际状态： WAITING：等待 RUNNING：运行中 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |

实时计算（流计算）

| apiType | String | 否 | SQL | API类型：DATASTREAM，SQL。 |
|---|---|---|---|---|
| endBeginTs | Long | 否 | 1548397575000 | 停止时间范围的上限。和停止时间下限配合使用，搜索停止时间在该范围内的运行实例。使用13位时间戳，单位到毫秒。 |
| endEndTs | Long | 否 | 1548397575000 | 停止时间范围的下限。和停止时间上限配合使用，搜索停止时间在该范围内的运行实例。使用13位时间戳，单位到毫秒。 |
| expectState | String | 否 | RUNNING | 期望状态： RUNNING ：运行中 PAUSED：暂停 TERMINATED： 停止 SUCCESS：成功（批作业） FAILED：失败（流作业） |
| isArchived | Boolean | 否 | false | 是否搜索归档实例。默认搜索非归档实例（默认值false）。针对不同作业的归档方式如下： 流作业只存在一个实例，当作业启动或者恢复运行时，将生成了新的实例，历史版本实例会被归档。 批作业运行结束后两天的实例会被归档。 |
| pageIndex | Integer | 否 | 1 | 分页选项，第几页，从1开始。 |
| pageSize | Integer | 否 | 10 | 分页选项，每页的实例数 |
| startBeginTs | Long | 否 | 1548397575000 | 启动时间范围上限。和启动时间下限配合使用，搜索启动时间在该范围内的运行实例。使用13位时间戳，单位到毫秒 |
| startEndTs | Long | 否 | 1548397575000 | 启动时间范围下限。和启动时间上限配合使用，搜索启动时间在该范围内的运行实例。使用13位时间戳，单位到毫秒 |

| 参数 |  | 类型 | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId |  | String | FD0FF8C0-779A-45EB-9674- | 请求ID，方便foas定位问题 |
|  |  |  | FF3E127B10D2 |  |
| PageIndex |  | Integer | 1 | 分页属性，第几页，从1开始 |
| PageSize |  | Integer | 10 | 分页属性，每页多少实例 |
| TotalPage |  | Integer | 5 | 总页数 |
| TotalCount |  | Long | 50 | 总实例数目 |
| Instances.Id |  | Long | 123 | 实例ID |
| Instances.ProjectNa me |  | String | project1 | 项目名称 |
| Instances.JobName |  | String | job1 | 作业名称 |
| Instances.ActualStat e |  | String | RUNNING | Instance的实际状态： WAITING：等待 RUNNING：运行中 PAUSED：暂停 TERMINATED：停止 SUCCESS：成功（批作业） FAILED：失败（批作业） |
| Instances.ExpectStat e |  | String | RUNNING | 期望状态： RUNNING ：运行中 PAUSED：暂停 TERMINATED： 停止 SUCCESS：成功（批作业） FAILED：失败（流作业） |
| Instances.JobType |  | String | FLINKSTREAM _ | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| Instances.ApiType |  | String | SQL | API类型： DATASTREAM SQL |
| Instances.Code |  | String | code | 实例代码。 |
| Instances.Properties |  | String | k=v | 作业运行配置参数。 |
| Instances.Packages |  | String | package1.jar | Instance引用的package，多个逗号分隔，未引用为空。 |
| Instances.Starter |  | String | ABC | 启动人。 |
| Instances.StartTime |  | Long | 1548397575000 | 作业启动时间。 |

实时计算（流计算）

| Instances.LastErrorTi me | Long | 1548397575000 |  | 最近错误时间。 |  |
|---|---|---|---|---|---|
| Instances.LastErrorM essage | String | error |  | 最近一次错误信息。 |  |
| Instances.LastOpera tor | String | xxxx |  | 最近操作者。 |  |
| Instances.LastOpera teTime | Long | 1548397575000 |  | 最近操作时间。 |  |
| Instances.PlanJson | String | {a:b} |  | 作业上线执行计划。 |  |
| Instances.EngineVer sion | String | blink_2.2.4 |  | 引擎版本。 |  |
| Instances.EngineJob Handler | String | applicationxxxx \| xxxx _ |  | Instance在YARN中的名称： ApplicaitonID \| jobID（JM分配的Job ID） 。 |  |
|  |  |  | _ |  |  |
| Instances.InputDelay | Long | 20 |  | 业务延时（毫秒）。 |  |
| Instances.ClusterId | String | d6wxwo5tnrmuamx2ly3m7vkz |  | 集群ID。 |  |
| Instances.QueueNa me | String | root.default |  | 队列名称。 |  |
| Instances.EndTime | Long | 1548397575000 |  | 结束时间。 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.5.13. ModifyInstanceState

ModifyInstanceState API可以修改运行实例的状态，实现对实例的操作

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| expectState | String | 是 | RUNNING | 期望状态： RUNNING ：运行中 PAUSED：暂停 TERMINATED： 停止 SUCCESS：成功（批作业） FAILED：失败（流作业） |
| instanceId | Long | 是 | -1 | InstanceID，流作业只有一个运行实例，此处填-1L，指在线上运行的，批作业可以通过 ListInstance、Startjob等接口获得。 |
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |
| isFlush | Boolean | 否 | true | 作业恢复时使用，确认是否使用最新配置。其他情况使用该参数无效，默认使用。 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

### 文件夹

#### 4.6.1. CreateFolder

CreateFolder API可以为您为在项目对应的路径下创建文件夹，并在foas上保存文件夹ID，路径。 作业在foas控制台上显示的路径都是在作业开发目录之下，实际填写path的使用并不显示作业开发目录，作业开发目录对应根目录 / 。

**说明**

实时计算（流计算）

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| path | String | 是 | /path | 文件夹路径 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| FolderId | Long |  | 123 | 文件夹ID |

```
http(s)://[Endpoint]/api/v2/projects/[projectName]/folders
```

`&<`公共请求参数>

#### 4.6.2. DeleteFolder

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| path | String | 是 | /path1/path2 | 文件夹路径 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.6.3. GetFolder

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| path | String | 是 | /path1/path2 | 文件夹路径 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Folder |  |  |  | 文件夹详情 |
| └FolderId | Long |  | 123 | 文件夹ID |
| └Path | String |  | /path1/path2 | 文件夹路径 |

```
http(s)://[Endpoint]/?path=/aliyun &RegionId=reg
```

`&<`公共请求参数>

#### 4.6.4. ListChildFolder

实时计算（流计算）

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| path | String | 是 | /path | 主目录路径 |
| projectName | String | 是 | project | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Folders |  |  |  | 文件目录详情 |
| └FolderId | Long |  | 123 | 文件夹ID |
| └Path | String |  | /path | 文件夹目录 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.6.5. MVFolder

MVFolder API可以移动文件夹，需要注意的是非空文件夹移动时，会将文件夹下的作业一起移动。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| destPath | String | 是 | /folder1 | 目标路径 |
| projectName | String | 是 | p | 项目名称 |
| srcPath | String | 是 | /dets | 原路径 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?destPath=/folder1 &RegionId=region &srcPath=/dets
```

`&<`公共请求参数>

### 作业

#### 4.7.1. CheckRawPlanJson

您可以组合调用CheckRawPlanJson和GetRawPlanJson接口，来获取某个作业的planjson。CheckRawPlanJson接口发出调用请求后会返回一个session ID，GetRawPlanJson获取这个session ID后可以查询到planjson的详细情况。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 单个作业名称 |
| projectName | String | 是 | project1 | 项目名称 |
| sessionId | String | 是 | 123456 | 当使用CheckRawPlanJson发送请求后，会返回一个sessionId，将该sessionId填在此处。 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| PlanJsonInfo |  |  |  | PlanJson详情 |

实时计算（流计算）

| PlanJsonInfo.Status | String | success | GetRawPlanJson的执行状态： session in run：执行中 success ：成功 fail：失败 |
|---|---|---|---|
| PlanJsonInfo.PlanJson | String | {a:b} | 执行计划 |
| PlanJsonInfo.ErrorMessage | String | error | 错误信息 |

`&<`公共请求参数>

#### 4.7.2. CommitJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
https://[endpoint]/api/v2/projects/[projectName]/jobs/[jobName]/commit
```

`&<`公共请求参数>

#### 4.7.3. CreateJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| apiType | String | 是 | SQL | 创建API类型： DATASTREAM： Datastream 作业 SQL ：SQL作业 |
| clusterId | String | 是 | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| code | String | 是 | code1 | SQL作业填写SQL代码，DataStream作业填写Foas上提交DataStream作业的相关参数。 |
| engineVersion | String | 是 | blink_2.2.4 | 使用引擎的版本 |
| jobName | String | 是 | job1 | 作业名称 |
| jobType | String | 是 | FLINKSTREAM _ | 作业类型： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| planJson | String | 否 | {a:b} | 执行计划 |
| projectName | String | 是 | project1 | 项目名称 |
| queueName | String | 是 | root.default | 队列名称 |
| description | String | 否 | test | 对作业相关描述备注 |
| folderId | Long | 是 | 123 | 文件夹ID |
| packages | String | 否 | package1,package2 | jar包全名称，多个使用逗号分隔。 |
| properties | String | 否 | {k:v} | 作业运行的相关参数 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|

实时计算（流计算）

| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|---|---|---|---|---|
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.4. DeleteJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.5. GetJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Job |  |  |  | 作业详情 |
| └JobName | String |  | job1 | 作业名称 |
| └ProjectName | String |  | project | 项目名称 |
| └JobType | String |  | FLINKSTREAM _ | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| └ApiType | String |  | SQL | API类型： DATASTREAM： Datastream作业 SQL ：SQL作业 |
| └Code | String |  | code | 作业详情： SQL作业返回SQL代码； datastream作业返回foas上datdastream 作业的配置。 |
| └PlanJson | String |  | {a:b} | 作业上线的执行计划 |
| └Properties | String |  | k:v | 作业运行配置参数 |
| └Packages | String |  | package1.jar | 引用package名称，多个逗号分隔。 |
| └IsCommitted | Boolean |  | true | 是否上线状态 |
| └Creator | String |  | xxxx | 作业创建者 |
| └CreateTime | Long |  | 1548397575000 | 作业创建时间 |
| └Modifier | String |  | xxxx | 最近修改者 |
| └ModifyTime | Long |  | 1548397575000 | 最近修改时间 |

实时计算（流计算）

| └Description | String | test | 作业备注描述 |
|---|---|---|---|
| └EngineVersion | String | blink_2.2.4 | 引擎版本 |
| └ClusterId | String | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| └QueueName | String | root.default | 队列名称 |
| └FolderId | Long | 123 | 文件夹ID |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.6. ListJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| projectName | String | 是 | project1 | 项目名称 |
| apiType | String | 否 | SQL | API类型：DATASTREAM或SQL |
| clusterId | String | 否 | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| engineVersion | String | 否 | blink_2.2.4 | 引擎版本 |
| folderId | Long | 否 | 123 | 文件夹ID |
| jobName | String | 否 | job1 | 作业名称 |
| jobType | String | 否 | FLINKSTREAM _ | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| pageIndex | Integer | 否 | 1 | 分页属性，第几页 |
| pageSize | Integer | 否 | 10 | 分页属性，每页返回job数 |
| queueName | String | 否 | root.default | 队列名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| PageIndex | Integer |  | 1 | 分页属性，第几页 |
| PageSize | Integer |  | 10 | 分页属性，每页多少个job |
| TotalPage | Integer |  | 5 | 分页属性，总页数 |
| TotalCount | Long |  | 50 | 分页属性，总job数 |
| Jobs |  |  |  | 作业详情 |
| └JobName | String |  | job1 | 作业名称 |
| └ProjectName | String |  | project1 | 项目名称 |
| └JobType | String |  | FLINKSTREAM _ | 作业种类： FLINK _STREAM：流作业 FLINK _BATCH：批作业 |
| └ApiType | String |  | SQL | API类型：DATASTREAM或SQL |
| └Code | String |  | code | 作业代码 |
| └PlanJson | String |  | {a:b} | 执行计划 |
| └Properties | String |  | k:v | 作业运行配置 |
| └Packages | String |  | package1.jar | package名称 |
| └IsCommitted | Boolean |  | true | 作业是否已经提交运行 |
| └Creator | String |  | xxxx | 创建者 |
| └CreateTime | Long |  | 1548397575000 | 作业创建时间 |
| └Modifier | String |  | xxxx | 最近修改者 |

实时计算（流计算）

| └ModifyTime | Long | 1548397575000 | 最近修改时间 |
|---|---|---|---|
| └Description | String | test | 作业备注描述 |
| └EngineVersion | String | blink2.2.4 _ | 引擎版本 |
| └ClusterId | String | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| └QueueName | String | root.default | 队列名称 |
| └FolderId | Long | 123 | 文件夹ID |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.7. OfflineJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.8. StartJob

调用本API可以启动指定项目下的目标作业。

**调试**

您可以在OpenAPI Explorer中直接运行该接口，免去您计算签名的困扰。运行成功后，OpenAPI Explorer可以自动生成SDK代码示例。

**请求头**

除公共请求头，该接口还需要指定以下请求头。关于公共请求头，请参见公共请求参数文档。

| 名称 | 类型 | 是否必选 | 示例 | 描述 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou-pre | 集团内用户使用： cn-hangzhou- pre 公共云预发； cn-hangzhou- internal 集团内生产； cn- hangzhou-internal-pre 集团内预发； |

**请求语法**

```
POST /api/v2/projects/[projectName]/jobs/[jobName]/instance HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | startjobapi | 作业名称。 |
| projectName | String | 是 | apitest | 项目名称。 |
| parameterJson | Json | 否 | {"a":"b"} | 作业启动相关参数，使用JSON格式，参数有如startOffset（启动位点，13位时间戳）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B10D2 | 请求ID |

实时计算（流计算）

| instanceId | Long | 123 | 实例ID |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <StartJobRequest> <RequestId>7F7F7176-2462-4C1A-82AC-62D87E6868C5</RequestId> <instanceId>177270</instanceId> </StartJobRequest> |  |

| JSON | 格式 |
|---|---|
| { "RequestId":"7F7F7176-2462-4C1A-82AC-62D87E6868C5", "instanceId":177270 } |  |

**错误码**

访问错误中心查看更多错误码。

#### 4.7.9. UpdateJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| code | String | 否 | code | 作业代码 |
| engineVersion | String | 否 | blink_2.2.4 | 引擎版本 |
| jobName | String | 是 | job1 | 作业名称 |
| planJson | String | 否 | {a:b} | 作业执行计划 |
| projectName | String | 是 | project1 | 项目名称 |
| queueName | String | 否 | root.default | 队列名称 |
| description | String | 否 | test | 作业备注描述 |
| folderId | Long | 否 | 123 | 文件夹ID |
| packages | String | 否 | package1.jar | package名称 |
| properties | String | 否 | k:v | 作业运行配置参数 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.7.10. ValidateJob

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| jobName | String | 是 | job1 | 作业名称 |
| projectName | String | 是 | project1 | 项目名称 |

实时计算（流计算）

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| JobInOut |  |  |  | 作业输入输出 |
| └Inputs |  |  |  | 输入数组信息 |
| └Type | String |  | sls | 表类型 |
| └Workspace | String |  | xxxx | 表所属项目 |
| └Name | String |  | xxxx | 表名 |
| └Properties | Map |  | k:v | 配置组 |
| └Outputs |  |  |  | 返回数组信息 |
| └Type | String |  | sls | 表类型 |
| └Workspace | String |  | xxxx | 表所属项目 |
| └Name | String |  | xxxx | 表名 |
| └Properties | Map |  | k:v | 配置组 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

### Package

#### 4.8.1. CreatePackage

CreatePackage API可以获取到您在OSS中的package，将该package传送到作业的执行节点上来。 package的版本信息由您自行维护，上传时可以选填md5值，foas协助校验。公有云共享集群无法使用CreatePackage API，独享集群用户只能使用创建

**说明**

集群时的OSS信息，填写时无需填写完整信息（foas可以自动读取），只需要填写Osspath。

| 参数 | 类型 | 是否必选 |  |  |  | 示例值 | 描述 |
|---|---|---|---|---|---|---|---|
| ossBucket | String | 否 |  |  |  | blinktest2.oss-cn- |  |
|  |  |  |  |  |  | hangzhou- | OS |
|  |  |  |  |  |  | internal.aliyuncs.com |  |
| ossEndpoint | String | 否 |  |  |  | oss-cn-hangzhou- | OSS |
|  |  |  |  |  |  | internal.aliyuncs.com |  |
| ossOwner | String | 否 |  |  |  | user1 | OSS所有者 |
| ossPath | String | 是 |  |  |  | path1/path2/a.jar | package在oss中的路径 |
| packageName | String | 是 |  |  |  | package1.jar | package名称 |
| projectName | String | 是 |  |  |  | project1 | 项目名称 |
| type | String | 是 |  |  |  | JAR | package 类型： JAR：jar包 DICTIONARY：普通文件 SCRIPT：脚本 PYTHON：python文件或者zip 包 |
| description | String | 否 |  |  |  | test | package的备注描述 |
| md5 | String | 否 |  |  |  | md5值 | package的md5值 |
| originName | String | 否 |  |  |  | package2 | package别名 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

实时计算（流计算）

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.8.2. DeletePackage

DeletePackage API可以删除foas上通过createpackage保存的oss信息，删除后foas无法再获取对应的package信息。

**说明**

使用DeletePackage API删除foas上不存在的oss package信息时系统会报错。已经上线的作业如已经引用该package，则删除时也会报错。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| packageName | String | 是 | package.jar | package名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.8.3. GetPackage

GetPackage API只能获取到通过web或CreatePackage接口在foas上保存过相关信息的package。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| packageName | String | 是 | package1.jar | package名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  |  |  | 示例值 | 描述 |
|---|---|---|---|---|---|---|
| RequestId | String |  |  |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  |  |  | FF3E127B10D2 |  |
| Package |  |  |  |  |  | package详情 |
| └ProjectName | String |  |  |  | project1 | 项目名称 |
| └PackageName | String |  |  |  | package1.jar | package名称 |
| └Creator | String |  |  |  | xxxx | 创建者 |
| └Modifier | String |  |  |  | xxxx | 最近修改者 |
| └CreateTime | Long |  |  |  | 1548397575000 | 创建时间（13位时间戳，精确到毫秒）。 |
| └ModifyTime | Long |  |  |  | 1548397575000 | 最近修改时间 |
| └OriginName | String |  |  |  | package2.jar | package别名 |
| └Type | String |  |  |  | JAR | package 类型： JAR：jar包 DICTIONARY：普通文件 SCRIPT：脚本 PYTHON：python文件或者zip包 |
| └Md5 | String |  |  |  | md5zhi | package的md5值 |
| └Description | String |  |  |  | test | package备注描述 |
| └OssEndpoint | String |  |  |  | oss-cn-hangzhou- | Oss |
|  |  |  |  |  | internal.aliyuncs.com |  |
| └OssBucket | String |  |  |  | blinktest2.oss-cn-hangzhou- | Ossbucket |
|  |  |  |  |  | internal.aliyuncs.com |  |

实时计算（流计算）

| └OssOwner | String | xxxx | Oss所有者 |
|---|---|---|---|
| └OssPath | String | path1/path2/a.jar | Oss路径 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.8.4. GetRefPackageJob

GetRefPackageJob API可以获取引用指定package的所有作业详情。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| packageName | String | 是 | package1.jar | package名称 |
| projectName | String | 是 | project1 | 项目名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| PageIndex | Integer |  | 1 | 返回第几页 |
| PageSize | Integer |  | 10 | 每页包含的job数 |
| TotalCount | Long |  | 50 | 总计多少job |
| TotalPage | Integer |  | 5 | 总计多少页 |
| Jobs |  |  |  | 作业详情 |
| └JobName | String |  | job1 | 作业名称 |
| └ProjectName | String |  | project1 | 项目名称 |
| └JobType | String |  | FLINKSTREAM _ | 作业类型：FLINK _STREAM（流作业）或 FLINK _BATCH（批作业） |
| └ApiType | String |  | SQL | API类型：DATASTREAM或SQL |
| └Code | String |  | code | 作业code |
| └PlanJson | String |  | {a:b} | 作业上线的执行计划 |
| └Properties | String |  | k:v | 作业运行参数配置 |
| └Packages | String |  | package1.jar | 作业引用的package名称，多个逗号分隔 |
| └IsCommitted | Boolean |  | true | 是否上线 |
| └Creator | String |  | xxxx | 创建者 |
| └CreateTime | Long |  | 1548397575000 | 作业创建时间 |
| └Modifier | String |  | xxxx | 最近修改者 |
| └ModifyTime | Long |  | 1548397575000 | 最近修改时间 |
| └Description | String |  | test | 作业备注描述 |
| └EngineVersion | String |  | blink_2.2.4 | 引擎版本 |
| └ClusterId | String |  | d6wxwo5tnrmuamx2ly3m7vkz | 集群ID |
| └QueueName | String |  | root.default | 队列名称 |
| └FolderId | Long |  | 123 | 文件夹ID |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.8.5. ListPackage

ListPackage API可以搜索出指定project下满足特定条件的package信息。 实时计算（流计算）

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| packageName | String | 是 | package1 | package名称 |
| projectName | String | 是 | project1 | 项目名称 |
| pageIndex | Integer | 否 | 1 | 分页属性，第几页 |
| pageSize | Integer | 否 | 10 | 分页属性，每页包含package数量 |
| type | String | 否 | JAR | package 类型： JAR：jar包 DICTIONARY：普通文件 SCRIPT：脚本 PYTHON：python文件或者zip 包 |

| 参数 | 类型 |  |  |  | 示例值 | 描述 |
|---|---|---|---|---|---|---|
| RequestId | String |  |  |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  |  |  | FF3E127B10D2 |  |
| PageIndex | Integer |  |  |  | 1 | 分页属性，第几页 |
| PageSize | Integer |  |  |  | 10 | 分页属性，每页包含package数 |
| TotalPage | Integer |  |  |  | 5 | 分页属性，总页面数 |
| TotalCount | Long |  |  |  | 50 | 分页属性，package总数 |
| Packages |  |  |  |  |  | package详情 |
| └ProjectName | String |  |  |  | project1 | 项目名称 |
| └PackageName | String |  |  |  | package1.jar | package名称 |
| └Creator | String |  |  |  | xxxx | 创建者 |
| └Modifier | String |  |  |  | xxxx | 最近修改者 |
| └CreateTime | Long |  |  |  | 1548397575000 | 创建时间（13位时间戳，精确到毫秒） |
| └ModifyTime | Long |  |  |  | 1548397575000 | 最近修改时间 |
| └OriginName | String |  |  |  | package2.jar | package别名 |
| └Type | String |  |  |  | JAR | package 类型： JAR：jar包 DICTIONARY：普通文件 SCRIPT：脚本 PYTHON：python文件或者zip包 |
| └Md5 | String |  |  |  | md5值 | package的md5值 |
| └Description | String |  |  |  | test | package备注描述 |
| └OssEndpoint | String |  |  |  | oss-cn-hangzhou- | Oss |
|  |  |  |  |  | internal.aliyuncs.com |  |
| └OssBucket | String |  |  |  | blinktest2.oss-cn-hangzhou- | OssBucket |
|  |  |  |  |  | internal.aliyuncs.com |  |
| └OssOwner | String |  |  |  | xxxx | Oss拥有者 |
| └OssPath | String |  |  |  | path1/path2/a.jar | Oss路径 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.8.6. UpdatePackage

UpdatePackage API可以更新foas上保存的指定项目下package相关信息。

| 参数 | 类型 | 是否必选 |  |  | 示例值 | 描述 |
|---|---|---|---|---|---|---|
| ossBucket | String | 否 |  |  | blinktest2.oss-cn- |  |
|  |  |  |  |  | hangzhou- | oss |
|  |  |  |  |  | internal.aliyuncs.com |  |

实时计算（流计算）

| ossEndpoint | String | 否 |  | oss-cn-hangzhou- | oss |
|---|---|---|---|---|---|
|  |  |  |  | internal.aliyuncs.com |  |
| ossOwner | String | 否 |  | xxxx | oss所有者 |
| ossPath | String | 否 |  | path1/path2/a.jar | oss路径 |
| packageName | String | 是 |  | package1.jar | package名称 |
| projectName | String | 是 |  | project1 | 项目名称 |
| description | String | 否 |  | test | package注释描述 |
| md5 | String | 否 |  | md5值 | package的md5值 |
| originName | String | 否 |  | package2.jar | package别名 |
| tag | String | 否 |  | xxxx | package的标记 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

### Queue

#### 4.9.1. CreateQueue

CreateQueue OpenAPI将集群资源分配到创建的Queue中，供绑定了这个Queue的项目使用。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | d6wxwo5tnrmuamx2ly3m**** | 集群ID。 |
| gpu | Integer | 否 | 1 | GPU处理硬件块数。 |
| maxMemMB | Integer | 是 | 1024 | Queue拥有的最大Memory。 |
| maxVcore | Integer | 是 | 100 | Queue拥有的最大CPU。 |
| queueName | String | 是 | root.default | Queue的名称。 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-shanghai
```

`&<`公共请求参数>

#### 4.9.2. DeleteQueue

**说明**

需要删除的Queue已经被项目绑定，则需要先解绑项目，再使用DeleteQueue OpenAPI进行删除。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

实时计算（流计算）

| clusterId | String | 是 | d6wxwo5tnrmuamx2ly3m**** | 集群ID |
|---|---|---|---|---|
| queueName | String | 是 | root.default | Queue的名称 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k****
```

`&<`公共请求参数>

#### 4.9.3. BindQueue

项目创建成功后，需要使用BindQueue将项目绑定在已经存在并且没有被其他项目绑定的Queue上后，才能在改项目上创建和运行作业。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
| projectName |  |  | p1 | 项目的名称 |
| queueName |  |  | queue1 | 要绑定的Queue的名称 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

`&<`公共请求参数>

#### 4.9.4. UnbindQueue

您可以通过UnbindQueue OpenAPI将Queue中已经绑定的项目进行解绑。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
| projectName |  |  | p1 | 项目的名称 |
| queueName |  |  | queue1 | 要绑定的Queue的名称 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.9.5. GetClusterQueueInfo

您可以通过GetClusterQueueInfo OpenAPI查询集群上已存在的Queue的信息。 实时计算（流计算）

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | d6wxwo5tnrmuamx2ly3m**** | 集群ID |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B**** |  |
| Queues.ClusterId | String |  | d6wxwo5tnrmuamx2ly3m**** | 集群名称 |
| Queues.QueueName | String |  | root.default | 队列名称 |
| Queues.MinGpu | Integer |  | 2 | 最小GPU数 |
| Queues.MaxGpu | Integer |  | 10 | GPU最大值 |
| Queues.MinMem | Integer |  | 1024 | 最小内存数（MB） |
| Queues.MaxMem | Integer |  | 2048 | 内存最大值（MB） |
| Queues.MinVCore | Integer |  | 50 | 最小Vcore数 |
| Queues.MaxVCore | Integer |  | 100 | 最大Vcore数 |
| Queues.UsedVCore | Integer |  | 50 | 已使用Vcore |
| Queues.UsedGpu | Integer |  | 5 | 已使用GPU |
| Queues.UsedMem | Integer |  | 512 | 已使用内存（MB） |

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.9.6. ListProjectBindQueue

ListProjectBindQueue API可以查看指定项目对应的队列相关的信息。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | d6wxwo5tnrmuamx2ly3m**** | 集群ID |
| projectName | String | 是 | project1 | 项目名称 |
| queueName | String | 否 | root.default | 队列名称 |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B**** |  |
| Queues.ClusterId | String |  | d6wxwo5tnrmuamx2ly3m**** | 集群ID |
| Queues.QueueName | String |  | root.default | 集群名称 |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

#### 4.9.7. ListProjectBindQueueResource

ListProjectBindQueueResource API可以查询project关联的队列的资源信息，返回对应Queue资源情况的具体信息。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | d6wxwo5tnrmuamx2ly3m**** | 集群ID |
| projectName | String | 是 | project1 | 项目名称 |
| queueName | String | 否 | root.default | 队列名称 |

实时计算（流计算）

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Queues.ClusterId | String |  | d6wxwo5tnrmuamx2ly3m**** | 集群名称 |
| Queues.QueueName | String |  | root.default | 队列名称 |
| Queues.MinGpu | Integer |  | 2 | 最小GPU数 |
| Queues.MaxGpu | Integer |  | 10 | GPU最大值 |
| Queues.MinMem | Integer |  | 1024 | 最小内存数（MB） |
| Queues.MaxMem | Integer |  | 2048 | 内存最大值（MB） |
| Queues.MinVCore | Integer |  | 50 | 最小Vcore数 |
| Queues.MaxVCore | Integer |  | 100 | 最大Vcore数 |
| Queues.UsedVCore | Integer |  | 50 | 已使用Vcore |
| Queues.UsedGpu | Integer |  | 5 | 已使用GPU |
| Queues.UsedMem | Integer |  | 512 | 已使用内存（MB） |

```
http(s)://[Endpoint]/?Action=undefined
```

`&<`公共请求参数>

### Cluster

#### 4.10.1. CreateCluster

您完成购买后，可以通过订单的实例ID，使用CreateCluster OpenAPI创建集群。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| description | String | 否 | cluster1 | 集群描述 |
| displayName |  | 是 | clustername _ | 您创建的集群的名称 |
| orderId |  |  | blinkonecs1234 _ | 您下单生成的实例ID |
| userOssBucket |  |  | 12345 | 用户OSS的Bucket名称 |
| userVSwitch |  |  | vsw-abcd | 您指定的交换机名称 |
| userVpcId |  |  | vpc-abcd | 集群所在VPC名称说明实时计算需要和上下游数据存储处在同一个 VPC内，否则会则会造成无法联通的问题。 |
| zoneId |  |  | cn-shanghai-f | 可用区区号 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ClusterId | String | cmy99ugusuco66x9qc6k**** | FOAS为创建完成的集群分配的ID |

```
http(s)://[Endpoint]/?RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.2. DestroyCluster

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

实时计算（流计算）

| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
|---|---|---|---|---|

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

http(s)://[Endpoint]/?<公共请求参数>

#### 4.10.3. ExpandCluster

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
| count | Integer | 是 | 5 | 扩容后的机器台数 |
| model | String | 否 | Ecs4c16g _ | 机器型号。 说明目前不支持混部，扩容机型只能和已有 Slave机型一致。 |
| clusterId | String | 是 | vsw-abcd | 交换机名称。扩容提示vSwitch不足的时候需要填写。 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.4. ShrinkCluster

**说明**

同时配置instanceIds参数和modelTargetCount参数时，以instanceIds为准。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
| instanceIds | String | 否 | abcd | 机器实例ID。指定需要去除的 Slave实例。指定多个实例需用逗号（,）分割。 |
| modelTargetCount | String | 否 | {Ecs4c16g:2} _ | 指定缩容后，S实例的型号和台数。（缩容过程中随机去除Slave 实例）。 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B**** | 请求ID |

**请求示例**

实时计算（流计算）

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.5. ListCluster

您可以使用ListCluster OpenAPI，查询若干个集群的信息。查询的集群信息可根据参数选择，进行自由组合。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | cmy99ugusuco66x9qc6k**** | 集群ID |
| displayName | String |  | clustera | 集群名称 |
| pageIndex | Integer |  | 2 | 分页选项。指定查询的页码。 |
| pageSize | Integer |  | 1 | 分页选项。每页显示的集群数。 |
| region | String |  | cn-hangzhou | 集群所属地区 |
| state | String |  | RUNNING | 集群状态集群创建中 ：STARTING 集群扩容中（增加Slave机型台数）： EXPANDING 集群变配中（提高或者降低 Master型号） ：UPGRADING 集群注销中 ：DESTROYING 集群已销毁 ：DESTROYED 集群缩容中（减少Slave机型台数）：REDUCING 集群维护中：MAINTAINING |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |
| TotalCount | Long | 50 | 总集群数 |
| TotalPage | Integer | 5 | 总页数 |
| PageIndex | Integer | 1 | 分页选项。指定查询的页码。 |
| PageSize | Integer | 10 | 分页选项。每页显示的集群数。 |
| Clusters.ClusterId | String | cmy99ugusuco66x9qc6k**** | 集群ID |
| Clusters.RegionId | String | cn-hangzhou | 集群所属地区 |
| Clusters.ZoneId | String | cn-hangzhou-a | 可用地域ID |
| Clusters.State | String | RUNNING | 集群状态集群创建中 ：STARTING 集群扩容中（增加Slave机型台数）： EXPANDING 集群变配中（提高或者降低Master型号） ：UPGRADING 集群注销中 ：DESTROYING 集群已销毁 ：DESTROYED 集群缩容中（减少Slave机型台数）： REDUCING 集群维护中：MAINTAINING |
| Clusters.OwnerId | String | abcd | 集群拥有者UID |
| Clusters.Operator | String | abcd | 集群最后操作人UID |
| Clusters.DisplayName | String | abcd | 集群名称 |
| Clusters.Description | String | abcd | 集群备注 |
| Clusters.GmtCreate | Long | 1527494257000 | 集群VPC创建时间 |
| Clusters.GmtModified | Long | 1527494257000 | 集群VPC修改时间 |

**请求示例**

```
http(s)://[Endpoint]/?<公共请求http(s)://[Endpoint]/?RegionId=cn-hangzhou
```

`&<`公共请求参数`>>`

#### 4.10.6. GetClusterDetails

实时计算（流计算）

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| clusterId | String | cmy99ugusuco66x9qc6k**** | 集群ID |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B10D2 |  |
| Detail.ClusterId | String |  | cmy99ugusuco66x9qc6k**** | 集群ID |
| Detail.RegionId | String |  | cn-hangzhou | 可用区ID |
| Detail.ZoneId | String |  | cn-hangzhou-a | 作业类型：FLINK _STREAM（流作业）或 FLINK _BATCH（批作业） |
| Detail.State | String |  | RUNNING | 集群状态集群创建中 ：STARTING 集群扩容中（增加Slave机型台数）： EXPANDING 集群变配中（提高或者降低Master型号） ：UPGRADING 集群注销中 ：DESTROYING 集群已销毁 ：DESTROYED 集群缩容中（减少Slave机型台数）： REDUCING 集群维护中：MAINTAINING |
| Detail.Description | String |  | ClusterA | 集群描述 |
| Detail.DisplayName | String |  | clustername _ | 集群名称 |
| Detail.OwnerId | String |  | 1234 | 集群拥有者UID |
| Detail.Operator | String |  | 1234 | 集群最后操作人UID |
| Detail.StorageType | String |  | hdfs | 存储类型 |
| Detail.GmtCreate | Long |  | 1527494257000 | 集群VPC创建时间 |
| Detail.GmtModified | Long |  | 1548397575000 | 集群VPC修改时间 |
| Detail.UserOssInfo | String |  | {k:v} | 您的OSS信息。以JSO形式返回，包括 Bucket，Endpoint等。 |
| Detail.UserVpcId | String |  | vpc-abcd | VPC ID |
| Detail.UserSGId | String |  | sg-abcd | 安全组ID |
| Detail.UserVSwitchList | String |  | {vsw-****,vsw-****} | 您的VSW列表 |
| Detail.IsMixDeploy | Boolean |  | false | 是否为混部集群（存在多种型号Slave机型） |
| Detail.InstanceInfos | String |  | {k:v} | 集群Master机型和Slave机型的相关信息， 包括实例ID，ENI，IP和机器型号等。 |

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.7. GetClusterEngineVersions

您可以通过使用GetClusterEngineVersions OpenAPI，获取集群上可使用的引擎的版本号。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |
| EngineVersions |  | blink-2.2.7-1 | 引擎版本 |

**请求示例**

实时计算（流计算）

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.8. GetClusterResource

您可以使用GetClusterResource OpenAPI查看集群总资源的情况和当前已使用的资源情况。

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| clusterId | String | cmy99ugusuco66x9qc6k**** | 集群ID |

| 参数 | 类型 |  | 示例值 | 描述 |
|---|---|---|---|---|
| RequestId | String |  | FD0FF8C0-779A-45EB-9674- |  |
|  |  |  | FF3E127B**** |  |
| Resource.TotalMB | Long |  | 2048 | 集群总内存 |
| Resource.AllocatedMB |  |  | 1024 | 已使用的内存 |
| Resource.AvailableMB |  |  | 1024 | 可使用的内存 |
| Resource.TotalVirtualCores |  |  | 200 | 集群总VCore数 |
| Resource.AllocatedVirtualCores |  |  | 100 | 已经使用的VCore数 |
| Resource.AllocatedVirtualCores |  |  | 100 | 可使用的VCore数 |

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> JSON格式正常返回示例

```
{}
```

JSON格式异常返回示例

```
null http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.10.9. ModifyMasterSpec

您可以通过ModifyMasterSpec OpenAPI更改集群Master机型的规格，包括Master机型的升配和降配。

**说明**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 是 | cmy99ugusuco66x9qc6k**** | 集群ID |
| masterTargetModel | String | 是 | Ecs4c16g _ | Master机型变配的目标机器型号 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

### Project

#### 4.11.1. CreateProject

实时计算（流计算）

**描述**

独享集群：CreateProject OpenAPI仅创建项目，创建后如果需要在创建的项目中运行作业需要先使用BindQueue OpenAPI，将项目绑定在一个未被绑定的项目上。 共享集群：购买项目成功后即可使用CreateProject OpenAPI创建项目。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| clusterId | String | 否 | cmy99ugusuco66x9qc6k**** | 集群ID |
| deployType |  | 是 | public | 集群类型： 独享集群：cell 共享集群：public |
| description |  | 否 | 测试项目 | 项目描述 |
| managerIds |  | 是 | 1234567 | 主账号ID |
| name |  | 是 | projecta | 项目名称 |
| orderId |  | 否 | stream-abcd | 共享模式实例ID 说明仅共享模式用户需要填写。 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
http(s)://[Endpoint]/?clusterId=cmy99ugusuco66x9qc6k**** &deployType=public &managerIds=yourManagerId &orderId=stream-**** &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.11.2. DeleteProject

**描述**

**说明**

DeleteProject OpenAPI可以删除集群中指定项目。如果需要删除的项目已经和Queue绑定，也会将项目和Queue解绑（不会删除Queue）。为了防止资源浪费，请及时将

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| projectName | String | project1 | 项目名称 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |

**请求示例**

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.11.3. GetProject

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| projectName | String | project1 | 项目名称 |

实时计算（流计算）

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |
| Project.Name | String | project1 | 项目名称 |
| Project.State | String | ENABLE | 项目状态 |
| Project.Creator | String | creator1 | 项目创建者的UID |
| Project.CreateTime | Long | 1527494257000 | 项目创建时间 |
| Project.Modifier | String | modifer1 | 项目修改者UID |
| Project.ModifyTime | Long | 1527494257000 | 项目修改时间 |
| Project.Description | String | project1 | 项目描述 |
| Project.DeployType | String | cell | 集群类型： 独享集群：cell 共享集群： public |
| Project.ClusterId | String | cmy99ugusuco66x9qc6k**** | 集群ID |
| Project.ManagerIds | String | m1 | 管理员ID列表。对个ID使用逗号（,）分隔 |

**请求示例**

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.11.4. ListProject

您可以使用ListCluster OpenAPI，查询若干个项目的信息。查询的项目信息可根据参数选择，进行自由组合。

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| deployType | String | 是 | cell | 集群类型： 独享集群：cell 共享集群： public |
| clusterId | String | 否 | cmy99ugusuco66x9qc6k**** | 集群ID |
| name | String |  | p1 | 项目名称 |
| pageIndex | Integer |  | 2 | 分页选项。指定查询的页码。 |
| pageSize | Integer |  | 1 | 分页选项。每页显示的项目数。 |
| region | String |  | cn-hangzhou | 项目所属地区 |

| 参数 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |
| PageIndex | Integer | 1 | 分页选项。指定查询的页码。 |
| PageSize | Integer | 10 | 分页选项。每页显示的项目数。 |
| TotalCount | Long | 50 | 分页选项。总项目数。 |
| RequestId | String | FD0FF8C0-779A-45EB-9674- FF3E127B1**** | 请求ID |
| Project.Name | String | project1 | 项目名称 |
| Project.State | String | ENABLE | 项目状态 |
| Project.Creator | String | creator1 | 项目创建者的UID |
| Project.CreateTime | Long | 1527494257000 | 项目创建时间 |
| Project.Modifier | String | modifer1 | 项目修改者UID |
| Project.ModifyTime | Long | 1527494257000 | 项目修改时间 |
| Project.Description | String | project1 | 项目描述 |

实时计算（流计算）

| Project.DeployType | String | cell | 集群类型： 独享集群：cell 共享集群： public |
|---|---|---|---|
| Project.ClusterId | String | cmy99ugusuco66x9qc6k**** | 集群ID |
| Project.ManagerIds | String | m1 | 管理员ID列表。对个ID使用逗号（,）分隔 |

**请求示例**

```
http(s)://[Endpoint]/?deployType=cell &name=p1 &RegionId=cn-hangzhou
```

`&<`公共请求参数>

#### 4.11.5. UpdateProject

您可以通过UpdateProject OpenAPI修改项目参数，项目参数可应用于项目下的所有作业。

**调试**

您可以在OpenAPI Explorer中直接运行该接口，免去您计算签名的困扰。运行成功后，OpenAPI Explorer可以自动生成SDK代码示例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

| 名称 | 类型 | 是否必选 | 示例 | 描述 |
|---|---|---|---|---|
| RegionId | String | 否 | cn-hangzhou | 地域 |

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| globalJobConfig | String | FormData | 否 | sql.${key}=${value} | 项目参数 |
| projectName | String | Path | 是 | citybrain _ | 项目名称 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A017B343-33DC-4A97-BAC5- 4B57872D5B61 | 请求ID |

**示例**

请求示例

```
Host:foas.aliyuncs.com Content-Type:application/json
```

正常返回示例

| XML | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/xml <UpdateProjectResponse> <RequestId>A017B343-33DC-4A97-BAC5-4B57872D5B61</RequestId> </UpdateProjectResponse> |  |

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "RequestId" : "A017B343-33DC-4A97-BAC5-4B57872D5B61" } |  |

**错误码**

访问错误中心查看更多错误码。 实时计算（流计算）

#### 4.11.6. UpdateProjectConfig

您可以通过UpdateProjectConfig OpenAPI为项目开启或停止支持批SQL作业。

**调试**

您可以在OpenAPI Explorer中直接运行该接口，免去您计算签名的困扰。运行成功后，OpenAPI Explorer可以自动生成SDK代码示例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| IsOpenBatchSQL | Boolean | Query | 是 | true | 是否开启批SQL作业，参数取值如下： true：项目开启支持批SQL作业。 false：项目停止支持批SQL作业。 |
| ProjectName | String | Query | 是 | citybrain _ | 项目名 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Data | Boolean | true | 批SQL开启或停用成功 |
| RequestId | String | 2E62CA21-83FE-4CE1-B7E2- E868F7272E6B | 请求ID |

**示例**

请求示例

```
PUT /api/v2/project/config?IsOpenBatchSQL=true&ProjectName=city_brain HTTP/1.1 Host:foas.aliyuncs.com Content-Type:application/json
```

正常返回示例

| XML | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/xml <UpdateProjectConfigResponse> <Data>true</Data> <RequestId>2E62CA21-83FE-4CE1-B7E2-E868F7272E6B</RequestId> </UpdateProjectConfigResponse> |  |

| JSON | 格式 |
|---|---|
| HTTP/1.1 200 OK Content-Type:application/json { "Data" : true, "RequestId" : "2E62CA21-83FE-4CE1-B7E2-E868F7272E6B" } |  |

**错误码**

访问错误中心查看更多错误码。

### OpenAPI DEMO

本文为您介绍专有云环境下，使用实时计算Open API方式操作实时计算作业所需的POM依赖和Open API DEMO。

**POM依赖**

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-foas</artifactId>
    <version>2.2.0</version>
</dependency>
```

实时计算（流计算）

**说明**

若需要依赖aliyun-java-sdk-core，请使用4.3.0及以上版本。4.3.0版本依赖示例如下。

```java
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.3.0</version>
</dependency> package sample; import com.aliyuncs.AcsRequest; import com.aliyuncs.AcsResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.foas.model.v20181111.*; import com.aliyuncs.http.FormatType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; import com.google.gson.Gson; import java.util.HashMap; import java.util.Map; /**
```

* 适用于专有云环境
*
* 作业的一般流程是：
* 创建`Job->`获取`planjson->`更新`planjson`到`job->`上线`job->`启动`job->`停止`instance`。
`* Instance`的状态一般如下(流作业为例，括号里的为动作`):`

```
 * Job上线->UNKNOWN[启动job]->WAITING[等待]->RUNNING[暂停]->PAUSED[恢复]->RUNNING[停止]->TERMINATED
```

* `* Note:`以下示例仅供演示`foas`接口的调用方式，不保证逻辑上的严谨性，请按照自己的场景重新组织调用逻辑。 `*/`

```java
public class PublicSample {
```

`//`填写购买的`foas`所在的`regionId`，根据您的实际情况修改。

```java
    private static final String regionId = "cn-shanghai";
```

`//`云账号`AK`，支持子账号，需要自行保证该账号具有访问实时计算服务的权限(子账号需要得到主账号访问实时计算服务的权限授权)。

```java
    private static final String accessId = "<yourAccessId>";
    private static final String accessKey = "<yourAccessSecret>";
    private static final String projectName = "<yourProjectName>";
    private static final String jobName = "<yourJobName>";
```

`//` 文件夹与`linux`文件系统格式相同，以 / 开始，表示根目录，只支持绝对路径，不支持相对路径。

```java
    private static final String folderName = "/新手任务";
    private static final String clusterId = "<yourClusterId>";//可以通过listProjectBindQueue接口来获得。
    private static final String queueName = "root.<queueName>";//可以通过listProjectBindQueue接口来获得。
```

private static final String engineVersion = "current";//Blink或者`Flink`的版本，`current`表示使用推荐版本`,beta`表示使用测试版本。

```java
    private static final String packageName = "<packageName>";
    private static final String sql =
            "--SQL\n" +
                    "--********************************************************************--\n" +
                    "--CreateTime: 2018-12-29 14:35:04\n" +
```

`"--Comment:` 请输入业务注释信息\n" +

```java
                    "--********************************************************************--\n" +
                    "\n" +
                    "CREATE TABLE datahub_source (`name` INT, num VARCHAR) WITH (\n" +
                    "    type = 'random'\n" +
                    ");\n" +
                    "CREATE TABLE datahub_sink (`name` INT, cnt BIGINT) WITH (\n" +
                    "    type = 'PRINT'\n" +
                    ");\n" +
                    "INSERT INTO\n" +
                    "    datahub_sink\n" +
                    "SELECT\n" +
                    "    `name`,\n" +
                    "FROM\n" +
                    "    datahub_source\n" +
                    "GROUP BY\n" +
                    "    `name`";
    private static final String properties =
            "#checkpoint模式：EXACTLY_ONCE或者AT_LEAST_ONCE\n" +
                    "blink.checkpoint.mode=EXACTLY_ONCE\n" +
```

`"#checkpoint`间隔时间，单位毫秒\n" +

```
                    "blink.checkpoint.interval.ms=180000\n" +
```

`"#rocksdb`的数据生命周期，单位毫秒\n" + 实时计算（流计算） 的数据命周期单位毫秒\

```java
                    "#state.backend.rocksdb.ttl.ms=129600000\n";
    private static <T extends AcsResponse> T getResponse(IAcsClient client, AcsRequest<T> request) {
        AcsResponse response = null;
        try {
```

`//`必须设置为`json`。

```
            request.setHttpContentType(FormatType.JSON);
            request.setAcceptFormat(FormatType.JSON);
            response = client.getAcsResponse(request);
        } catch (Exception e) {
```

`//`处理异常的逻辑，请注意异常中的`requestId`字段，排查问题时，需要提供该值给服务端。

```java
            if (e instanceof ServerException) {
                ServerException serverException = (ServerException) e;
                System.out.println(serverException.getRequestId());//本次请求的requestId。
```

System.out.println(serverException.getErrCode());//本次请求失败的的错误码，用于排查错误。

```java
            }
            System.out.println(e.getMessage());
        }
        return (T) response;
    }
    private static String getClusterMetricJson(String clusterId) {
        return String.format(
                        "{\n" +
                        "\t\"queries\": [ {\n" +
                        "\t\t\"metric\": \"%s.system.cpu.user\",\n" +
                        "\t\t\"aggregator\": \"avg\",\n" +
                        "\t\t\"granularity\": \"20s\",\n" +
                        "\t\t\"downsample\": \"avg\"\n" +
                        "\t}, {\n" +
                        "\t\t\"metric\": \"%s.system.cpu.iowait\",\n" +
                        "\t\t\"aggregator\": \"avg\",\n" +
                        "\t\t\"granularity\": \"20s\",\n" +
                        "\t\t\"downsample\": \"avg\"\n" +
                        "\t}],\n" +
                        "\t\"start\": %s,\n" +
                        "\t\"end\": %s,\n" +
                        "\t\"limit\": \"avg:sample:50\"\n" +
                        "}",
                clusterId, clusterId, System.currentTimeMillis() - 3600 * 1000, System.currentTimeMillis()
        );
    }
    public static void main(String[] args) throws Exception {
        IClientProfile profile = DefaultProfile.getProfile(regionId, accessId, accessKey);
        DefaultAcsClient client = new DefaultAcsClient(profile);
```

client.setAutoRetry(false);//不进行自动重试。 `//`创建一个独享集群，该接口是异步接口，调用返回后需要调用`listCluster`接口来获取集群的状态来判断是否创建完成。

```
        CreateClusterRequest createClusterRequest = new CreateClusterRequest();
        createClusterRequest.setDescription("test cluster");
        createClusterRequest.setDisplayName("aaaa");
```

createClusterRequest.setOrderId("yyyyy");//填写购买独享集群下单后生成的订单`ID`。

```
        createClusterRequest.setUserOssBucket("myBucket");
        createClusterRequest.setUserVpcId("xxxxx");
        createClusterRequest.setUserVSwitch("yyyy");
        createClusterRequest.setZoneId("cn-shanghai-f");
        CreateClusterResponse createClusterResponse = PublicSample.getResponse(client, createClusterRequest);
```

System.out.println(new Gson().toJson(createClusterResponse));//该`response`中含有`clusterId`信息，这个是集群的索引，后面的大部分接口都需要使用到。 `//`根据条件搜索集群，不设置的条件留`null`。

```java
        ListClusterRequest listClusterRequest = new ListClusterRequest();
        listClusterRequest.setClusterId(clusterId);
        listClusterRequest.setRegion(regionId);
        ListClusterResponse listClusterResponse = PublicSample.getResponse(client, listClusterRequest);
        System.out.println(new Gson().toJson(listClusterResponse));
        CreateQueueRequest createQueueRequest = new CreateQueueRequest();
        createQueueRequest.setClusterId(clusterId);
        createQueueRequest.setQueueName(queueName);
        createQueueRequest.setMaxVcore(300);
        createQueueRequest.setMaxMemMB(4 * 1024);
        CreateQueueResponse createQueueResponse = PublicSample.getResponse(client, createQueueRequest);
        System.out.println(new Gson().toJson(createQueueResponse));
```

`//`获取集群的引擎版本信息。

```java
        GetClusterEngineVersionsRequest getClusterEngineVersionsRequest = new GetClusterEngineVersionsRequest();
        getClusterEngineVersionsRequest.setClusterId(clusterId);
        GetClusterEngineVersionsResponse getClusterEngineVersionsResponse = PublicSample.getResponse(client, getClusterEngineVersionsRequest);
        System.out.println(new Gson().toJson(getClusterEngineVersionsResponse));
```

`//`获取该集群的资源信息。

```
        GetClusterResourceRequest getClusterResourceRequest = new GetClusterResourceRequest();
getClusterResourceRequestsetClusterId(clusterId);
```

实时计算（流计算）

```java
        getClusterResourceRequest.setClusterId(clusterId);
        GetClusterResourceResponse getClusterResourceResponse = PublicSample.getResponse(client, getClusterResourceRequest);
        System.out.println(new Gson().toJson(getClusterResourceResponse));
        GetClusterQueueInfoRequest getClusterQueueInfoRequest = new GetClusterQueueInfoRequest();
        getClusterQueueInfoRequest.setClusterId(clusterId);
        GetClusterQueueInfoResponse getClusterQueueInfoResponse = PublicSample.getResponse(client, getClusterQueueInfoRequest);
        System.out.println(new Gson().toJson(getClusterQueueInfoResponse));
```

`//`获取集群的`detail`信息。

```java
        GetClusterDetailsRequest getClusterDetailsRequest = new GetClusterDetailsRequest();
        getClusterDetailsRequest.setClusterId(clusterId);
        GetClusterDetailsResponse getClusterDetailsResponse = PublicSample.getResponse(client, getClusterDetailsRequest);
        System.out.println(new Gson().toJson(getClusterDetailsResponse));
```

`//`获取集群的`metrics`曲线，最多只能获取最近两小时的数据。

```java
        GetClusterMetricsRequest getClusterMetricsRequest = new GetClusterMetricsRequest();
        getClusterMetricsRequest.setClusterId(clusterId);
        getClusterMetricsRequest.setMetricJson(getClusterMetricJson(clusterId));//指标的名称请查看文档。
        GetClusterMetricsResponse getClusterMetricsResponse = PublicSample.getResponse(client, getClusterMetricsRequest);
        System.out.println(new Gson().toJson(getClusterMetricsResponse));
```

`//`注意：以下操作独享集群的接口只支持按量付费的独享集群。 `//`扩容集群，该接口是异步接口，需要通过集群状态来判断是否操作完成。

```
        ExpandClusterRequest expandClusterRequest = new ExpandClusterRequest();
        expandClusterRequest.setClusterId(clusterId);
```

expandClusterRequest.setModel("Ecs_4c8g");//该参数可选，当前不支持混布，只能填与原有的机型一致的机型，或者不填写。

```java
        ExpandClusterResponse expandClusterResponse = PublicSample.getResponse(client, expandClusterRequest);
        System.out.println(new Gson().toJson(expandClusterResponse));
```

`//`修改集群`master`的机型配置，只能更改`master`机型，不能修改`master`数量。 `//`注意：该接口是异步接口，需要通过集群状态来判断是否操作完成。

```java
        ModifyMasterSpecRequest modifyMasterSpecRequest = new ModifyMasterSpecRequest();
        modifyMasterSpecRequest.setClusterId(clusterId);
        modifyMasterSpecRequest.setMasterTargetModel("Ecs_8c16g");
        ModifyMasterSpecResponse modifyMasterSpecResponse = PublicSample.getResponse(client, modifyMasterSpecRequest);
        System.out.println(new Gson().toJson(modifyMasterSpecResponse));
```

`//`缩容集群，缩容有两种参数提供形式（当前仅支持第一种形式。）: `//1.`直接填需要去除的实例`instanceId(`可以通过`getClusterDetails`接口获得)。 `//2.`提供每种机型的目标台数。 `//`注意：该接口是异步接口，需要通过集群状态来判断是否操作完成。

```java
        ShrinkClusterRequest shrinkClusterRequest = new ShrinkClusterRequest();
        shrinkClusterRequest.setClusterId(clusterId);
        shrinkClusterRequest.setInstanceIds("111,222,333");
        //shrinkClusterRequest.setModelTargetCount("{"Ecs_4c8g":2,"Ecs_8c16g":7}");
        ShrinkClusterResponse shrinkClusterResponse = PublicSample.getResponse(client, shrinkClusterRequest);
        System.out.println(new Gson().toJson(shrinkClusterResponse));
```

`//`销毁集群，只能销毁按量付费的集群。注意: 该接口操作风险高，请务必谨慎操作。

```java
        DestroyClusterRequest destroyClusterRequest = new DestroyClusterRequest();
        destroyClusterRequest.setClusterId(clusterId);
        DestroyClusterResponse destroyClusterResponse = PublicSample.getResponse(client, destroyClusterRequest);
        System.out.println(new Gson().toJson(destroyClusterResponse));
```

`//1.`购买的共享集群，需要提供订单`ID`。

```
        CreateProjectRequest createProjectRequest = new CreateProjectRequest();
```

//createProjectRequest.setOrderId();//在共享集群上创建`project`时必填，填写购买的订单`id`。

```
        createProjectRequest.setDescription("test project");
```

createProjectRequest.setDeployType("cell");//在共享集群上创建`project`时填`public`。 createProjectRequest.setClusterId(clusterId);//在共享集群上创建`project`时可不填。

```java
        createProjectRequest.setName(projectName);
        CreateProjectResponse createProjectResponse = PublicSample.getResponse(client, createProjectRequest);
        System.out.println(new Gson().toJson(createProjectResponse));
```

`//` 绑定`queue`到`project`，该操作类似于将资源（某个`queue`）指定给某个`project`使用，只有将资源绑定到了某个`project`上， `//` 该`project`里的作业才能使用该资源。当前只支持一对一的关系，即一个`project`只能绑定一个`queue`，一个`queue`只能被绑定至一个`project`上。

```java
        BindQueueRequest bindQueueRequest = new BindQueueRequest();
        bindQueueRequest.setProjectName(projectName);
        bindQueueRequest.setClusterId(clusterId);
        bindQueueRequest.setQueueName(queueName);
        BindQueueResponse bindQueueResponse = PublicSample.getResponse(client, bindQueueRequest);
        System.out.println(new Gson().toJson(bindQueueResponse));
        ListProjectBindQueueRequest listProjectBindQueueRequest = new ListProjectBindQueueRequest();
        listProjectBindQueueRequest.setProjectName(projectName);
        ListProjectBindQueueResponse listProjectBindQueueResponse = PublicSample.getResponse(client, listProjectBindQueueRequest);
        System.out.println(new Gson().toJson(listProjectBindQueueResponse));
        GetProjectRequest getProjectRequest = new GetProjectRequest();
        getProjectRequest.setProjectName(projectName);
```

实时计算（流计算）

```java
        GetProjectResponse getProjectResponse = PublicSample.getResponse(client, getProjectRequest);
        System.out.println(new Gson().toJson(getProjectResponse));
        ListProjectRequest listProjectRequest = new ListProjectRequest();
        listProjectRequest.setName(projectName);
        listProjectRequest.setDeployType("cell");
        listProjectRequest.setRegion("cn-shanghai");
        ListProjectResponse listProjectResponse = PublicSample.getResponse(client, listProjectRequest);
        System.out.println(new Gson().toJson(listProjectResponse));
        UnbindQueueRequest unbindQueueRequest = new UnbindQueueRequest();
        unbindQueueRequest.setProjectName(projectName);
        unbindQueueRequest.setClusterId(clusterId);
        unbindQueueRequest.setQueueName(queueName);
        UnbindQueueResponse unbindQueueResponse = PublicSample.getResponse(client, unbindQueueRequest);
        System.out.println(new Gson().toJson(unbindQueueResponse));
```

`//`删除`project`。注意:删除`project`是高危操作，请务必谨慎操作。删除的条件是该`project`下的所有作业均已下线。

```java
        DeleteProjectRequest deleteProjectRequest = new DeleteProjectRequest();
        deleteProjectRequest.setProjectName(projectName);
        DeleteProjectResponse deleteProjectResponse = PublicSample.getResponse(client, deleteProjectRequest);
        System.out.println(new Gson().toJson(deleteProjectResponse));
```

`//`获取文件夹列表。

```java
        ListChildFolderRequest listChildFolderRequest = new ListChildFolderRequest();
        listChildFolderRequest.setPath("/");
        listChildFolderRequest.setProjectName(projectName);
        ListChildFolderResponse listChildFolderResponse = PublicSample.getResponse(client, listChildFolderRequest);
        System.out.println(new Gson().toJson(listChildFolderResponse));
```

`//`获取文件夹。

```java
        GetFolderRequest getFolderRequest = new GetFolderRequest();
        getFolderRequest.setPath(folderName);
        getFolderRequest.setProjectName(projectName);
        GetFolderResponse getFolderResponse = PublicSample.getResponse(client, getFolderRequest);
        System.out.println(new Gson().toJson(getFolderResponse));
        Long folderId;
        GetFolderResponse.Folder folder = getFolderResponse.getFolder();
```

`//`创建文件夹。

```java
            CreateFolderRequest createFolderRequest = new CreateFolderRequest();
            createFolderRequest.setPath(folderName);
            createFolderRequest.setProjectName(projectName);
            CreateFolderResponse createFolderResponse = PublicSample.getResponse(client, createFolderRequest);
            System.out.println(new Gson().toJson(createFolderResponse));
            folderId = createFolderResponse.getFolderId();
        } else {
            folderId = folder.getFolderId();
        }
```

`// sdk`的`package`存在用户自己的`oss`上，需要将`package`通过`oss console`或者`oss sdk`上传到`oss`上。 `//` 此处需要将`oss meta`信息提供给`foas`， `//` 并对`foas`授权`bucket`读取权限`(ram role:AliyunStreamDefaultRole)`，`foas`在使用时会从用户指定的`oss`和`bucket`上下载`package`。 `//` 请确保`oss`的`region`与`foas`所在的`region`一致。 `//` 如果`project`建在独享集群集群上，则不需要提供`endpoint`，`bucket`等信息，只需要提供`package`的`ossPath`。 `//` 用户的`oss`信息在创建独享集群的时候已经提供过了，不需要重复提供。

```
        CreatePackageRequest createPackageRequest = new CreatePackageRequest();
        createPackageRequest.setProjectName(projectName);
        createPackageRequest.setPackageName(packageName);
        createPackageRequest.setType("jar");
        createPackageRequest.setDescription("test package");
        createPackageRequest.setOssEndpoint("oss-cn-hangzhou.aliyuncs.com");//提供的endpoint需要保证网络可通达。
        createPackageRequest.setOssBucket("your bucket");
        createPackageRequest.setOssOwner("111111111");//oss的主账号uid。
        createPackageRequest.setOssPath("aaa/bbb/ccc.jar");
```

createPackageRequest.setMd5("123456");//可不填。不填，则跳过`md5`校验；填写，则在下载时进行完整性校验。

```java
        CreatePackageResponse createPackageResponse = PublicSample.getResponse(client, createPackageRequest);
        System.out.println(new Gson().toJson(createPackageResponse));
        UpdatePackageRequest updatePackageRequest = new UpdatePackageRequest();
        updatePackageRequest.setProjectName(projectName);
        updatePackageRequest.setPackageName(packageName);
        updatePackageRequest.setOssPath("aaa/bbb/ddd.jar");
        UpdatePackageResponse updatePackageResponse = PublicSample.getResponse(client, updatePackageRequest);
        System.out.println(new Gson().toJson(updatePackageResponse));
        GetPackageRequest getPackageRequest = new GetPackageRequest();
        getPackageRequest.setProjectName(projectName);
        getPackageRequest.setPackageName(packageName);
        GetPackageResponse getPackageResponse = PublicSample.getResponse(client, getPackageRequest);
        System.out.println(new Gson().toJson(getPackageResponse));
```

实时计算（流计算）

```java
        ListPackageRequest listPackageRequest = new ListPackageRequest();
        listPackageRequest.setProjectName(projectName);
        listPackageRequest.setType("jar");
        ListPackageResponse listPackageResponse = PublicSample.getResponse(client, listPackageRequest);
        System.out.println(new Gson().toJson(listPackageResponse));
        ListProjectBindQueueRequest listProjectBindQueueRequest2 = new ListProjectBindQueueRequest();
        listProjectBindQueueRequest2.setProjectName(projectName);
        ListProjectBindQueueResponse listProjectBindQueueResponse2 = PublicSample.getResponse(client, listProjectBindQueueRequest2);
        System.out.println(new Gson().toJson(listProjectBindQueueResponse2));
        ListProjectBindQueueResourceRequest listProjectBindQueueResourceRequest = new ListProjectBindQueueResourceRequest();
        listProjectBindQueueResourceRequest.setProjectName(projectName);
        ListProjectBindQueueResourceResponse listProjectBindQueueResourceResponse = PublicSample.getResponse(client,
listProjectBindQueueResourceRequest);
        System.out.println(new Gson().toJson(listProjectBindQueueResourceResponse));
        ListJobRequest listJobRequest = new ListJobRequest();
        listJobRequest.setProjectName(projectName);
        listJobRequest.setJobType("flink_stream");
        listJobRequest.setApiType("sql");
```

`//`该参数控制返回的`job`信息中是否返回较长的字段（例如`code`）。填`false`，则返回的只有部分字段；不填或者填`true`，则返回所有字段。

```java
        listJobRequest.setIsShowFullField(false);
        ListJobResponse listJobResponse = PublicSample.getResponse(client, listJobRequest);
        System.out.println(new Gson().toJson(listJobResponse));
```

`//`获取作业。

```java
        GetJobRequest getJobRequest = new GetJobRequest();
        getJobRequest.setProjectName(projectName);
        getJobRequest.setJobName(jobName);
        GetJobResponse getJobResponse = PublicSample.getResponse(client, getJobRequest);
        System.out.println(new Gson().toJson(getJobResponse));
        GetJobResponse.Job job = getJobResponse.getJob();
```

`//`创建作业。

```
            CreateJobRequest createJobRequest = new CreateJobRequest();
            createJobRequest.setProjectName(projectName);
            createJobRequest.setJobName(jobName);
            createJobRequest.setCode(sql);
```

createJobRequest.setProperties(properties);//无，则不用设置。 `//clusterId`和`queueName`可以不配置。不配置，则随机从项目绑定的`cluster`和`queue`中选择一个。

```
            createJobRequest.setClusterId(clusterId);
            createJobRequest.setQueueName(queueName);
```

`//engineVersion`可以不配置。不配置，则使用`current`版本（推荐版本）。

```
            createJobRequest.setEngineVersion(engineVersion);
            createJobRequest.setDescription("test");
```

createJobRequest.setPackages(packageName);//多个`package`之间用英文逗号分隔。

```java
            createJobRequest.setJobType("flink_stream");//flink_stream/flink_batch大小写不敏感。
            createJobRequest.setApiType("sql");//datastream/sql大小写不敏感。
            createJobRequest.setFolderId(folderId);
            CreateJobResponse createJobResponse = PublicSample.getResponse(client, createJobRequest);
            System.out.println(new Gson().toJson(createJobResponse));
        } else {
```

`//`修改作业。

```
            UpdateJobRequest updateJobRequest = new UpdateJobRequest();
            updateJobRequest.setProjectName(projectName);
            updateJobRequest.setJobName(jobName);
```

updateJobRequest.setCode(sql);//设置需要修改的字段，不修改的字段不需要设置。

```java
            UpdateJobResponse updateJobResponse = PublicSample.getResponse(client, updateJobRequest);
            System.out.println(new Gson().toJson(updateJobResponse));
        }
```

`//`返回引用指定`package`的`job`，该接口查询上线后的`job`引用关系，未上线的`job`不会返回。

```java
        GetRefPackageJobRequest getRefPackageJobRequest = new GetRefPackageJobRequest();
        getRefPackageJobRequest.setProjectName(projectName);
        getRefPackageJobRequest.setPackageName(packageName);
        GetRefPackageJobResponse getRefPackageJobResponse = PublicSample.getResponse(client, getRefPackageJobRequest);
        System.out.println(new Gson().toJson(getRefPackageJobResponse));
```

`//`校验`job`是否存在语法错误。

```java
        ValidateJobRequest validateJobRequest = new ValidateJobRequest();
        validateJobRequest.setProjectName(projectName);
        validateJobRequest.setJobName(jobName);
        ValidateJobResponse validateJobResponse = PublicSample.getResponse(client, validateJobRequest);
        System.out.println(new Gson().toJson(validateJobResponse));
```

实时计算（流计算） `//`获取`job`的`planjson`。该接口是异步接口，提交完成之后，需要调用`CheckRawPlanJson`接口获取结果`:Session in run/success/fail`。

```
        GetRawPlanJsonRequest getRawPlanJsonRequest = new GetRawPlanJsonRequest();
        getRawPlanJsonRequest.setProjectName(projectName);
        getRawPlanJsonRequest.setJobName(jobName);
        getRawPlanJsonRequest.setAutoconfEnable(true);//可以不填，默认为false。
```

`//`设置这个`job`预期使用多少资源来运行，这个参数会影响到生成`plan`的大小，不提供的话，底层引擎会生成默认资源配置。 getRawPlanJsonRequest.setExpectedCore(2f);//这个参数与下面的参数可以同时提供，也可以同时不提供，不允许一个提供，一个不提供。

```java
        GetRawPlanJsonResponse getRawPlanJsonResponse = PublicSample.getResponse(client, getRawPlanJsonRequest);
        CheckRawPlanJsonRequest checkRawPlanJsonRequest = new CheckRawPlanJsonRequest();
        checkRawPlanJsonRequest.setProjectName(projectName);
        checkRawPlanJsonRequest.setJobName(jobName);
        checkRawPlanJsonRequest.setSessionId(getRawPlanJsonResponse.getSessionId());
        String planJson;
        CheckRawPlanJsonResponse checkRawPlanJsonResponse;
        while (true) {
            checkRawPlanJsonResponse = PublicSample.getResponse(client, checkRawPlanJsonRequest);
            System.out.println(checkRawPlanJsonResponse.getPlanJsonInfo().getStatus());
            if (checkRawPlanJsonResponse.getPlanJsonInfo().getStatus().equals("success")) {
                planJson = checkRawPlanJsonResponse.getPlanJsonInfo().getPlanJson();
                break;
            } else if (checkRawPlanJsonResponse.getPlanJsonInfo().getStatus().equals("fail")) {
                System.out.println(checkRawPlanJsonResponse.getPlanJsonInfo().getErrorMessage());
                return;
            }
```

Thread.sleep(1000);//每秒查询一次。

```
        }
```

`//`修改作业`planjson`

```java
        UpdateJobRequest updateJobRequest = new UpdateJobRequest();
        updateJobRequest.setProjectName(projectName);
        updateJobRequest.setJobName(jobName);
        updateJobRequest.setPlanJson(planJson);
        UpdateJobResponse updateJobResponse = PublicSample.getResponse(client, updateJobRequest);
        System.out.println(new Gson().toJson(updateJobResponse));
```

`//`预估当前`job`所配置的`planjson`需要的资源数，为上线接口需要提供的`maxCU`数值提供参考，仅`blink-3.2.1`及以上版本支持该功能。

```java
        CalcPlanJsonResourceRequest calcPlanJsonResourceRequest = new CalcPlanJsonResourceRequest();
        calcPlanJsonResourceRequest.setProjectName(projectName);
        calcPlanJsonResourceRequest.setJobName(jobName);
        CalcPlanJsonResourceResponse calcPlanJsonResourceResponse = PublicSample.getResponse(client, calcPlanJsonResourceRequest);
        System.out.println(new Gson().toJson(calcPlanJsonResourceResponse));
```

`//`获取作业上一次运行记录的最后一次自动调优的`planjson`，注意:是上一次的运行记录，包括停止的和暂停的。如果不存在话返回`null`。

```java
        GetJobLatestAutoScalePlanRequest getJobLatestAutoScalePlanRequest = new GetJobLatestAutoScalePlanRequest();
        getJobLatestAutoScalePlanRequest.setProjectName(projectName);
        getJobLatestAutoScalePlanRequest.setJobName(jobName);
        GetJobLatestAutoScalePlanResponse getJobLatestAutoScalePlanResponse = PublicSample.getResponse(client,
getJobLatestAutoScalePlanRequest);
        System.out.println(new Gson().toJson(getJobLatestAutoScalePlanResponse));
```

`//`上线作业。

```
        CommitJobRequest commitJobRequest = new CommitJobRequest();
        commitJobRequest.setProjectName(projectName);
        commitJobRequest.setJobName(jobName);
```

commitJobRequest.setIsOnOff(true);//是否开启`autoscale`自动调优。不填，表示不开启，仅`blink-3.2.1`及以上版本支持该功能。 commitJobRequest.setConfigure("{\"fetch_delay\":44.5}");//json格式，当前仅支持这一个配置项，大小写敏感，`value`是`double`型。

```java
        CommitJobResponse commitJobResponse = PublicSample.getResponse(client, commitJobRequest);
        System.out.println(new Gson().toJson(commitJobResponse));
```

`//`获取实例。

```
        GetInstanceRequest getInstanceRequest = new GetInstanceRequest();
        getInstanceRequest.setProjectName(projectName);
        getInstanceRequest.setJobName(jobName);
```

`//-1`表示获取流作业的当前运行实例(因为流作业某一时刻最多只会存在一个示例)。注意：批作业需要填实际的运行实例`id`。

```java
        getInstanceRequest.setInstanceId(-1L);
        GetInstanceResponse getInstanceResponse = PublicSample.getResponse(client, getInstanceRequest);
        System.out.println(new Gson().toJson(getInstanceResponse));
        GetInstanceResponse.Instance instance = getInstanceResponse.getInstance();
        {
```

`//`启动作业。

```
            if (instance == null || "UNKNOWN".equals(instance.getActualState()) || "TERMINATED".equals(instance.getActualState())) {
                StartJobRequest startJobRequest = new StartJobRequest();
                startJobRequest.setProjectName(projectName);
                startJobRequest.setJobName(jobName);
                Map map = new HashMap<String, String>();
```

`//startOffset`表示启动点位

```
                map.put("startOffset", String.valueOf(System.currentTimeMillis()));//精确到ms时间戳。
                startJobRequest.setParameterJson(new Gson().toJson(map));//json格式参数。
StartJobResponsestartJobResponse=PublicSamplegetResponse(client startJobRequest);
```

实时计算（流计算）

```java
                StartJobResponse startJobResponse = PublicSample.getResponse(client, startJobRequest);
                System.out.println(new Gson().toJson(startJobResponse));
```

`//`等待启动成功。

```java
                while (true) {
                    GetInstanceRunSummaryRequest getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
                    getInstanceRunSummaryRequest.setProjectName(projectName);
                    getInstanceRunSummaryRequest.setJobName(jobName);
                    getInstanceRunSummaryRequest.setInstanceId(-1L);
                    GetInstanceRunSummaryResponse getInstanceRunSummaryResponse = PublicSample.getResponse(client,
getInstanceRunSummaryRequest);
                    System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
                    if ("WAITING".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                        System.out.println(String.format("lastErrorTime[%s], lastErrorMessage[%s]",
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorTime(),
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorMessage()));
                        Thread.sleep(1000);
                    } else {
                        break;
                    }
                }
            }
        }
        {
```

`//` 作业启动成功后，可以调用如下的接口进行运维。 `//`获取`instance`的运行`dag`图。

```java
            GetInstanceDetailRequest getInstanceDetailRequest = new GetInstanceDetailRequest();
            getInstanceDetailRequest.setProjectName(projectName);
            getInstanceDetailRequest.setJobName(jobName);
            getInstanceDetailRequest.setInstanceId(-1L);
            GetInstanceDetailResponse getInstanceDetailResponse = PublicSample.getResponse(client, getInstanceDetailRequest);
            System.out.println(new Gson().toJson(getInstanceDetailResponse));
```

`//`获取`instance`的运行时配置。

```java
            GetInstanceConfigRequest getInstanceConfigRequest = new GetInstanceConfigRequest();
            getInstanceConfigRequest.setProjectName(projectName);
            getInstanceConfigRequest.setJobName(jobName);
            getInstanceConfigRequest.setInstanceId(-1L);
            GetInstanceConfigResponse getInstanceConfigResponse = PublicSample.getResponse(client, getInstanceConfigRequest);
            System.out.println(new Gson().toJson(getInstanceConfigResponse));
```

`//`获取`instance`的运行时`checkpoint`信息。

```java
            GetInstanceCheckpointRequest getInstanceCheckpointRequest = new GetInstanceCheckpointRequest();
            getInstanceCheckpointRequest.setProjectName(projectName);
            getInstanceCheckpointRequest.setJobName(jobName);
            getInstanceCheckpointRequest.setInstanceId(-1L);
            GetInstanceCheckpointResponse getInstanceCheckpointResponse = PublicSample.getResponse(client, getInstanceCheckpointRequest);
            System.out.println(new Gson().toJson(getInstanceCheckpointResponse));
```

`//`获取`instance`的运行时异常信息`(failover`信息)。

```java
            GetInstanceExceptionsRequest getInstanceExceptionsRequest = new GetInstanceExceptionsRequest();
            getInstanceExceptionsRequest.setProjectName(projectName);
            getInstanceExceptionsRequest.setJobName(jobName);
            getInstanceExceptionsRequest.setInstanceId(-1L);
            GetInstanceExceptionsResponse getInstanceExceptionsResponse = PublicSample.getResponse(client, getInstanceExceptionsRequest);
            System.out.println(new Gson().toJson(getInstanceExceptionsResponse));
```

`//`如果上线时作业开启了自动调优，调优效果不理想，可中途关闭自动调优，关闭之后也可以再次打开。

```
            UpdateAutoScaleConfigRequest updateAutoScaleConfigRequest = new UpdateAutoScaleConfigRequest();
            updateAutoScaleConfigRequest.setProjectName(projectName);
            updateAutoScaleConfigRequest.setJobName(jobName);
            updateAutoScaleConfigRequest.setInstanceId(-1L);
```

updateAutoScaleConfigRequest.setConfigJson("{\"autoscale.enable\":false}");//json格式，当前只支持这个`key`，大小写敏感，取值为`true`或者 `false`。

```java
            UpdateAutoScaleConfigResponse updateAutoScaleConfigResponse = PublicSample.getResponse(client, updateAutoScaleConfigRequest);
            System.out.println(new Gson().toJson(updateAutoScaleConfigResponse));
```

`//`查询`instance`的运行时各项指标的数据曲线信息。 `//`当前只支持查询最近两小时的曲线，`metric`的格式为：`blink.{projectName}.{jobName}.{metricName}`。

```
            String metricJson = "{\n" +
```

"\t\"start\": 1547637620000,\n" + //精确到`ms`时间戳。

```
                    "\t\"limit\": \"avg:sample:50\",\n" +
                    "\t\"end\": 1547638420000,\n" +
                    "\t\"queries\": [{\n" +
                    "\t\t\"downsample\": \"20s-avg\",\n" +
                    "\t\t\"metric\": \"blink.bayes_team.huayuan_test_job.delay\",\n" +
                    "\t\t\"granularity\": \"20s\",\n" +
                    "\t\t\"aggregator\": \"max\"\n" +
                    "\t}, {\n" +
                    "\t\t\"downsample\": \"20s-avg\",\n" +
                    "\t\t\"metric\": \"blink.bayes_team.huayuan_test_job.fetched_delay\",\n" +
                    "\t\t\"granularity\": \"20s\",\n" +
                    "\t\t\"aggregator\": \"max\"\n" +
                    "\t}]\n" +
                    "}";
```

实时计算（流计算）

```java
            GetInstanceMetricRequest getInstanceMetricRequest = new GetInstanceMetricRequest();
            getInstanceMetricRequest.setProjectName(projectName);
            getInstanceMetricRequest.setJobName(jobName);
            getInstanceMetricRequest.setInstanceId(-1L);
            getInstanceMetricRequest.setMetricJson(metricJson);
            GetInstanceMetricResponse getInstanceMetricResponse = PublicSample.getResponse(client, getInstanceMetricRequest);
            System.out.println(new Gson().toJson(getInstanceMetricResponse.getMetrics()));
```

`//`获取`instance`实际使用的资源信息（`cpu/memory`）。

```java
            GetInstanceResourceRequest getInstanceResourceRequest = new GetInstanceResourceRequest();
            getInstanceResourceRequest.setProjectName(projectName);
            getInstanceResourceRequest.setJobName(jobName);
            getInstanceResourceRequest.setInstanceId(-1L);
            GetInstanceResourceResponse getInstanceResourceResponse = PublicSample.getResponse(client, getInstanceResourceRequest);
            System.out.println(new Gson().toJson(getInstanceResourceResponse.getResource()));
```

`//`批量获取多个作业的运行时状态。

```
            BatchGetInstanceRunSummaryRequest batchGetInstanceRunSummaryRequest = new BatchGetInstanceRunSummaryRequest();
            batchGetInstanceRunSummaryRequest.setProjectName(projectName);
            batchGetInstanceRunSummaryRequest.setJobType("flink_stream");
```

batchGetInstanceRunSummaryRequest.setJobNames("job1,job2,job3");//多个`job`之间用英文逗号分隔，请确保都是`stream job`，并且`job`已存在且已上线，否则会忽略错误的`job`。

```java
            BatchGetInstanceRunSummaryResponse batchGetInstanceRunSummaryResponse = PublicSample.getResponse(client,
batchGetInstanceRunSummaryRequest);
            System.out.println(new Gson().toJson(batchGetInstanceRunSummaryResponse.getRunSummarys()));
        }
        {
```

`//`暂停作业。

```java
            GetInstanceRunSummaryRequest getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
            getInstanceRunSummaryRequest.setProjectName(projectName);
            getInstanceRunSummaryRequest.setJobName(jobName);
            getInstanceRunSummaryRequest.setInstanceId(-1L);
            GetInstanceRunSummaryResponse getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
            System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
            if ("RUNNING".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                ModifyInstanceStateRequest modifyInstanceStateRequest = new ModifyInstanceStateRequest();
                modifyInstanceStateRequest.setProjectName(projectName);
                modifyInstanceStateRequest.setJobName(jobName);
                modifyInstanceStateRequest.setInstanceId(-1L);
                modifyInstanceStateRequest.setExpectState("PAUSED");
                ModifyInstanceStateResponse modifyInstanceStateResponse = PublicSample.getResponse(client, modifyInstanceStateRequest);
                System.out.println(new Gson().toJson(modifyInstanceStateResponse));
```

`//`等待暂停成功。

```java
                while (true) {
                    getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
                    getInstanceRunSummaryRequest.setProjectName(projectName);
                    getInstanceRunSummaryRequest.setJobName(jobName);
                    getInstanceRunSummaryRequest.setInstanceId(-1L);
                    getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
                    System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
                    if ("RUNNING".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                        System.out.println(String.format("lastErrorTime[%s], lastErrorMessage[%s]",
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorTime(),
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorMessage()));
                        Thread.sleep(1000);
                    } else {
                        break;
                    }
                }
            }
        }
        {
```

`//`恢复作业。

```java
            GetInstanceRunSummaryRequest getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
            getInstanceRunSummaryRequest.setProjectName(projectName);
            getInstanceRunSummaryRequest.setJobName(jobName);
            getInstanceRunSummaryRequest.setInstanceId(-1L);
            GetInstanceRunSummaryResponse getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
            System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
            if ("PAUSED".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                ModifyInstanceStateRequest modifyInstanceStateRequest = new ModifyInstanceStateRequest();
                modifyInstanceStateRequest.setProjectName(projectName);
                modifyInstanceStateRequest.setJobName(jobName);
                modifyInstanceStateRequest.setInstanceId(-1L);
                modifyInstanceStateRequest.setExpectState("RUNNING");
                ModifyInstanceStateResponse modifyInstanceStateResponse = PublicSample.getResponse(client, modifyInstanceStateRequest);
                System.out.println(new Gson().toJson(modifyInstanceStateResponse));
```

`//`等待恢复成功。

```
                while (true) {
```

实时计算（流计算）

```java
                    getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
                    getInstanceRunSummaryRequest.setProjectName(projectName);
                    getInstanceRunSummaryRequest.setJobName(jobName);
                    getInstanceRunSummaryRequest.setInstanceId(-1L);
                    getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
                    System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
                    if ("PAUSED".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                        System.out.println(String.format("lastErrorTime[%s], lastErrorMessage[%s]",
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorTime(),
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorMessage()));
                        Thread.sleep(1000);
                    } else {
                        break;
                    }
                }
            }
        }
        {
```

`//`停止作业。

```java
            GetInstanceRunSummaryRequest getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
            getInstanceRunSummaryRequest.setProjectName(projectName);
            getInstanceRunSummaryRequest.setJobName(jobName);
            getInstanceRunSummaryRequest.setInstanceId(-1L);
            GetInstanceRunSummaryResponse getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
            System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
            if ("RUNNING".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                ModifyInstanceStateRequest modifyInstanceStateRequest = new ModifyInstanceStateRequest();
                modifyInstanceStateRequest.setProjectName(projectName);
                modifyInstanceStateRequest.setJobName(jobName);
                modifyInstanceStateRequest.setInstanceId(-1L);
                modifyInstanceStateRequest.setExpectState("TERMINATED");
                ModifyInstanceStateResponse modifyInstanceStateResponse = PublicSample.getResponse(client, modifyInstanceStateRequest);
                System.out.println(new Gson().toJson(modifyInstanceStateResponse));
```

`//`等待停止成功。

```java
                while (true) {
                    getInstanceRunSummaryRequest = new GetInstanceRunSummaryRequest();
                    getInstanceRunSummaryRequest.setProjectName(projectName);
                    getInstanceRunSummaryRequest.setJobName(jobName);
                    getInstanceRunSummaryRequest.setInstanceId(-1L);
                    getInstanceRunSummaryResponse = PublicSample.getResponse(client, getInstanceRunSummaryRequest);
                    System.out.println(new Gson().toJson(getInstanceRunSummaryResponse));
                    if ("RUNNING".equals(getInstanceRunSummaryResponse.getRunSummary().getActualState())) {
                        System.out.println(String.format("lastErrorTime[%s], lastErrorMessage[%s]",
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorTime(),
                                getInstanceRunSummaryResponse.getRunSummary().getLastErrorMessage()));
                        Thread.sleep(1000);
                    } else {
                        break;
                    }
                }
            }
        }
```

`//`下线作业。

```java
        OfflineJobRequest offlineJobRequest = new OfflineJobRequest();
        offlineJobRequest.setProjectName(projectName);
        offlineJobRequest.setJobName(jobName);
        OfflineJobResponse offlineJobResponse = PublicSample.getResponse(client, offlineJobRequest);
        System.out.println(new Gson().toJson(offlineJobResponse));
```

`//`删除作业。

```java
        DeleteJobRequest deleteJobRequest = new DeleteJobRequest();
        deleteJobRequest.setProjectName(projectName);
        deleteJobRequest.setJobName(jobName);
        DeleteJobResponse deleteJobResponse = PublicSample.getResponse(client, deleteJobRequest);
        System.out.println(new Gson().toJson(deleteJobResponse));
        DeletePackageRequest deletePackageRequest = new DeletePackageRequest();
        deletePackageRequest.setProjectName(projectName);
        deletePackageRequest.setPackageName(packageName);
        DeletePackageResponse deletePackageResponse = PublicSample.getResponse(client, deletePackageRequest);
        System.out.println(new Gson().toJson(deletePackageResponse));
    }
}
```
