---
title: "实时计算（流计算） Flink企业版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 532
source_pdf: "12_Flink企业版 开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sc/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 实时计算（流计算） Flink企业版 开发指南

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

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。 其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 实时计算（流计算） 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，

**警告**

组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请

**说明**

您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。
实时计算（流计算）

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
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调用成
功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源集ID。
接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

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

实时计算（流计算）

| ResourceGroupName | 资源集名称。 |
|---|---|
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

| 框中查看 RAM Role 。 |  |  |
|---|---|---|
| RAM Role | 获得 | stsAK |

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
实时计算（流计算）

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

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云 API。

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
实时计算（流计算）
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请参

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** >
**开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
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
```

实时计算（流计算）

```
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

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 实时计算（流计算） 调用示例如下：

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

实时计算（流计算） `//` 当使用`STS AK`调用`ROA`接口时需要在`Header`加上`x-acs-security-token`字段

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

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL/TLS 证书有效性，若您代码环境没有证书环境， 则会报错证书校验失败。 为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可以通过以下参数设置： Java

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

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** >
**开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07-14）。 示例代码如下： 实时计算（流计算）

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-RegionID>", "<AccessKey ID>", "<AccessK
ey Secret>")
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
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey("<your-regionid>", "<yourAccessKeyId>", "<your
AccessSecret>")
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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 实时计算（流计算）

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

使用HTTPS协议访问OpenAPI时，SDK会默认开启校验SSL证书有效性，若您代码环境没有证书环境，则会报错证书校验失败。为保障生产环境通信安全，建议您保持开启，若在测试环境必须忽略证书校验，可参考如下内容进行设置。 `//` 设置请求 `HTTPSInsecure`（只影响当前）

```
request.SetHTTPSInsecure(true) // 设置请求 HTTPSInsecure 为 true isInsecure := request.GetHTTPSInsecure() // 获取请求 HTTPSInsecure
```

当请求未设置时，客户端设置才能生效。 `//` 设置客户端 `HTTPSInsecure`（用于客户端发送的所有请求）。

```
client.SetHTTPSInsecure(true) // 设置客户端 HTTPSInsecure 为 true isInsecure := client.GetHTTPSInsecure() // 获取客户端 HTTPSInsecure
```

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。 实时计算（流计算）

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用服务** >
**开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

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

实时计算（流计算）

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

) 实时计算（流计算） API

## AppManager API

### 定义

#### ValidateSqlScript

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP /1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "statement": "Drop TABLE `vvp`.`default`.`test`" } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "validationResult": "VALIDATION RESUL _ T VALID DDL STATE _ _ _ MENT" } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） API 请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:validate HTTP /1.1 { "RegionId":"cn-wulan-env188-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"validationResult\":\"VALIDATION_RESULT_VALID_DDL_STATEMENT\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;validationResult&quot;:&quot;VALIDATION_RESULT_VALID_DDL_STATEMENT&quot;}</data
```

>

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### UpdateDeploymentDesiredState

调用UpdateDeploymentDesiredState，更新实时计算中的部署目标状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/state H TTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| paramsJso n | String | Body | 否 | {"state": "CANCELLED"} | 执行参数，sql脚本。 |

| F | link企业版开 API | 发指南·Ap | pManager |  |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04-28T01:59:31Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 28T02:16:43.68631 7Z", "resourceVersion": 134, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "23540697665705** **", "resource- plan.has.migrated": "true", "storage.disaster.rp o": "1800", "deployment.source -type": "EDITOR", "deployment.has.de ployed": "false", "deployment.parent. id": "", "modifier": "23540697665705** **", "creatorName": "flinkadmin", "plan.uri": "deployment/7325a c07-e466-4c1b- b598- 311c6f2c103b/resou rcePlan.json", "priority": "5", "priority.class.name ": "flink-p5", "migration.display.e nabled": "false", "deployment.exec- plan.uri.valid": "true", "com.dataartisans.a ppmanager.controll |  |

实时计算（流计算） API

| 参数名称 | 类型 | er.deployment.spec. v示e例rsion": "14", | 说明 |
|---|---|---|---|
|  |  | "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.dr aft.history.version": "3", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- jobs/namespaces/fli nkteam/jobs/b3e1db 6b-3cfe-41ac-a156- 48d8820f6d65/exec Plan.json", "deployment.refere nced.deployment.dr aft.id": "cee26b6e- d03b-4a03-a628- a6fe665c****", "taker": " \| vvp-0", "modifierName": "flinkadmin", "deployment.refere nced.deployment.dr aft.history.id": |  |
| data | String | "5bfca9e9-a50d- 483b-bad5- 1e1d5315****" }, "id": "7325ac07- e466-4c1b-b598- 311c6f2c****", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "fine-grained", "job.resource.total. memory.byte": "3724541952", "job.resource.total.c pu": "0.7", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 'connector' = '示da例tagen' | 说明 |
|---|---|---|---|
|  |  | ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined" : false, "flinkImageRegistry" : "cn-wulan-env**- d01- reg.docker.intra.env **.shuguang.com:80 /ververica-paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposito ry": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT", _ "allowNonRestoredS tate": false, "savepointId": "425dfb74-2bbb- 4879-8273- 0b087a97****" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat |  |

实时计算（流计算） API

| 参数名称 | 类型 | ionAttempts": 4, "示m例axJobCreationAtt | 说明 |
|---|---|---|---|
|  |  | empts": 1, "deploymentTargetI d": "a89ff052-38c6- 4fd3-9b91- e9c53f8e****" }, "status": { "startTime": 1777342472501, "state": "RUNNING", "endTime": 0 } } |  |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/state H TTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
28T01:59:31Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 28T02:16:43.686317Z\",\"resourceVersion\":134,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\", annotations\":{\"creator\":\"23540697665705****\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.source-type\":\" EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"modifier\":\"23 0697665705****\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/7325ac07-e466-4c1b -b598-311c6f2c103b/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5 \",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.version\":\ 4\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\":\"3 ,\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-jobs/namespace s/flinkteam/jobs/b3e1db6b-3cfe-41ac-a156- 48d8820f6d65/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4 a03-a628-a6fe665c****\",\"taker\":\" | vvp- 0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\":\"5b a9e9-a50d-483b-bad5-1e1d5315****\"},\"id\":\"7325ac07-e466-4c1b-b598- 311c6f2c****\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"temp late\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"3724541952\",\"job.resource.total.cpu\":\"0.7\" "native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\": {\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strn ame VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (st rname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SEL ECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FR OM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env**-d01 -reg.docker.intra.env**.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-flink-1 .17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"batchMod ":false,\"resources\":{\"jobmanager\":{\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\":{\"me mory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"425dfb74-2bbb -4879-8273-0b087a97****\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"deployme TargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8e****\"},\"status\": {\"startTime\":1777342472501,\"state\":\"RUNNING\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 28T01:59:31Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 28T02:16:43.686317Z&quot;,&quot;resourceVersion&quot;:134,&quot;name&quot;:&quot;sqlJob&quot;, uot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;23540697665705****&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&qu ;deployment.source-
```

实时计算（流计算） API

```xml
type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot;depl ment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;23540697665705****&quot;,&quot;cr torName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/7325ac07-e466-4c1 b-b598- 311c6f2c103b/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.class.n e&quot;:&quot;flinkp5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec-plan. uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deployment.spec. rsion&quot;:&quot;14&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.histo .version&quot;:&quot;3&quot;,&quot;deployment.exec-plan.uri&quot;:&quot;oss://flink-fullyman aged-9cuwr9g7y1hl19/flink-jobs/namespaces/flinkteam/jobs/b3e1db6b-3cfe-41ac-a156-48d8820f6d6 5/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&quot;cee26b6e-d 03b-4a03-a628-a6fe665c****&quot;,&quot;taker&quot;:&quot; | vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deployment raft.history.id&quot;:&quot;5bfca9e9-a50d-483b-bad5- 1e1d5315****&quot;},&quot;id&quot;:&quot;7325ac07-e466-4c1b-b598- 311c6f2c****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;spec&q t;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;3724541952&quot;,&quot;job.reso ce.total.cpu&quot;:&quot;0.7&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;f nk.queryablestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot; ,&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr-8.0.7manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPO RARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&
#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with (    &#x27;co
nnector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot;c wulan-env**-d01-reg.docker.intra.env**.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot;1.1 quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;:{&quot;jo bmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;sav ointId&quot;:&quot;425dfb74-2bbb-4879-8273- 0b087a97****&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;:{&qu ot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJobCreatio ttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8e****&qu ot;},&quot;status&quot;: {&quot;startTime&quot;:1777342472501,&quot;state&quot;:&quot;RUNNING&quot;,&quot;endTime&quot; }}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### UpdateDeployment

实时计算（流计算） API

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patch H TTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
|  |  |  |  | { "metadata": { "id": "7325ac07-e466-4c1b- b598-311c6f2c103b", "name": "sqlJob", "namespace": "flinkteam", "workspace": "9cuwr9g7y1hl19", "createdAt": "2026-04- 28T01:59:31Z", "modifiedAt": "2026-04- 28T02:07:18Z", "labels": {}, "annotations": { "creator": "235406976657057054", "resource- plan.has.migrated": "true", "storage.disaster.rpo": "1800", "deployment.has.deploye d": "false", "deployment.source- type": "EDITOR", "deployment.parent.id": "", "modifier": "235406976657057054", "creatorName": "flinkadmin", "plan.uri": "deployment/7325ac07- e466-4c1b-b598- 311c6f2c103b/resourcePl an.json", "priority": "5", "priority.class.name": "flink-p5", "migration.display.enable d": "false", "com.dataartisans.appma nager.controller.deploym ent.spec.version": "5", "default.resource- setting.has.migrated": |  |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | "true", "示de例ployment.referenced.d | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | eployment.draft.history.v ersion": "3", "deployment.referenced.d eployment.draft.id": "cee26b6e-d03b-4a03- a628-a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.referenced.d eployment.draft.history.id ": "5bfca9e9-a50d-483b- bad5-1e1d5315acaf", "one-time.retry": "false", "stop-with- savepoint.enabled": false }, "resourceVersion": 9 }, "spec": { "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": |  |
| paramsJso n | String | Body | 否 | "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreationAt tempts": 4, "maxJobCreationAttempts ": 1, "template": { "metadata": { "annotations": { "flink.resource.type": "fine-grained", "job.resource.total.memor y.byte": "0", "job.resource.total.cpu": "0.0", "native.kubernetes.mode" : "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.enabled ": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) _ AS BIGINT) AS lens | 执行参数，sql脚本。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | FROM d示a例tahub table;", _ | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | "flinkVersion": "1.17", "flinkImageTag": "1.17.0- vvr-8.0.7-manifest- 251107", "flinkImageRegistry": "cn- wulan-env**-d01- reg.docker.intra.env**.sh uguang.com:80/ververica- paas", "flinkImageRepository": "vvr" }, "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } }, "status": { "state": "SUSPENDED", "startTime": 1777341571990, "endTime": 0 } } |  |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:56:19.55614 7Z", "resourceVersion": 134, "name": "sqlJob", "namespace": "flinkteam", "annotations": { |  |

实时计算（流计算） API

| 参数名称 | 类型 | "storage.disaster.rp o示":例 "1800", | 说明 |
|---|---|---|---|
|  |  | "deployment.source -type": "EDITOR", "modifier": "235406976657057 054", "creatorName": "flinkadmin", "one- time.retry": "false", "priority.class.name ": "flink-p5", "deployment.exec- plan.uri.valid": "true", "default.resource- setting.has.migrate d": "true", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- jobs/namespaces/fli nkteam/jobs/f736bb d6-c9cf-48ab-973a- 9653bb0f8c0a/exec Plan.json", "deployment.refere nced.deployment.dr aft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "resources.from.job. has.migrated": "true", "taker": " \| vvp-0", "creator": "235406976657057 054", "resource- plan.has.migrated": "true", "restore- from.savepoint-id": "5cea0d88-303d- 44e5-a96e- 47f7217723d7", "stop-with- savepoint.enabled": "false", "deployment.has.de ployed": "false", "deployment.parent. id": "", "plan.uri": "deployment/a3d88 b2a-e076-4491- 86f2- 5a81ea4c7300/reso urcePlan.json", "priority": "5", "migration.display.e nabled": "false", "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "11", "deployment.refere nced.deployment.dr aft.history.version": "1", "modifierName": |  |

实时计算（流计算） API

| 参数名称 | 类型 | "flinkadmin", "示de例ployment.refere | 说明 |
|---|---|---|---|
| data | Integer | nced.deployment.dr aft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total.c pu": "0.0", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined" : false, "flinkImageRegistry" : "cn-wulan-env35- d01- reg.docker.intra.env 35.shuguang.com:8 | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 0/ververica-paas", "示ve例rsionName": | 说明 |
|---|---|---|---|
|  |  | "vvr-8.0.7-flink- 1.17", "flinkImageReposito ry": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT", _ "allowNonRestoredS tate": false, "savepointId": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "state": "SUSPENDED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002791356, "state": "SUSPENDED", "endTime": 0 } } |  |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） API

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/patch H TTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:56:19.556147Z\",\"resourceVersion\":134,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\", annotations\":{\"storage.disaster.rpo\":\"1800\",\"deployment.sourcetype\":\"EDITOR\",\"modifier\":\"235406976657057054\",\"creatorName\":\"flinkadmin\",\"one-t ime.retry\":\"false\",\"priority.class.name\":\"flink-p5\",\"deployment.exec-plan.uri.valid\ ":\"true\",\"default.resource-setting.has.migrated\":\"true\",\"deployment.execplan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinkjobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4 a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\" | vvp- 0\",\"creator\":\"235406976657057054\",\"resource-plan.has.migrated\":\"true\",\"restore-fro m.savepoint-id\":\"5cea0d88-303d-44e5-a96e-47f7217723d7\",\"stop-withsavepoint.enabled\":\"false\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\ ",\"plan.uri\":\"deployment/a3d88b2a-e076-4491-86f2- 5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"migration.display.enabled\":\"false\",\" m.dataartisans.appmanager.controller.deployment.spec.version\":\"11\",\"deployment.referenced. ployment.draft.history.version\":\"1\",\"modifierName\":\"flinkadmin\",\"deployment.referenced eployment.draft.history.id\":\"561a6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e07 6-4491-86f2-5a81ea4c7300\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{\"an notations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"native ubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\": {\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strn ame VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (st rname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SEL ECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FR OM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35-d01 -reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-flink-1 .17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"batchMod ":false,\"resources\":{\"jobmanager\":{\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\":{\"me mory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88-303d -44e5-a96e-47f7217723d7\"},\"state\":\"SUSPENDED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"deployme TargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002791356,\"state\":\"SUSPENDED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 24T03:56:19.556147Z&quot;,&quot;resourceVersion&quot;:134,&quot;name&quot;:&quot;sqlJob&quot;, uot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&quot;deployment.source-type&quot;:&quot;
```

实时计算（流计算） API

```xml
EDITOR&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;creatorName&quot;:&quot linkadmin&quot;,&quot;onetime.retry&quot;:&quot;false&quot;,&quot;priority.class.name&quot;:&quot;flink-p5&quot;,&quo t;deployment.exec-plan.uri.valid&quot;:&quot;true&quot;,&quot;default.resource-setting.has.m igrated&quot;:&quot;true&quot;,&quot;deployment.exec-plan.uri&quot;:&quot;oss://flink-fullym anaged-9cuwr9g7y1hl19/flink-jobs/namespaces/flinkteam/jobs/f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&quot;c 26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;taker&qu ;:&quot; | vvp-0&quot;,&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resource-pla n.has.migrated&quot;:&quot;true&quot;,&quot;restore-from.savepoint-id&quot;:&quot;5cea0d88-3 03d-44e5-a96e-47f7217723d7&quot;,&quot;stop-withsavepoint.enabled&quot;:&quot;false&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot &quot;deployment.parent.id&quot;:&quot;&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d88b2ae076-4491-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;migration.displa enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.appmanager.controller.deployment.spec.v sion&quot;:&quot;11&quot;,&quot;deployment.referenced.deployment.draft.history.version&quot;:& ot;1&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deploym t.draft.history.id&quot;:&quot;561a6a3d-7858-4056-acfbad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;spec&q t;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource.tota cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.quer blestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot; ,&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr-8.0.7manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPO RARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&
#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with (    &#x27;co
nnector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot;c wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot;1.1 quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;:{&quot;jo bmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;sav ointId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;upgradeStrategy&quot;:{&qu ot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJobCreatio ttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8ee019&qu ot;},&quot;status&quot;: {&quot;startTime&quot;:1777002791356,&quot;state&quot;:&quot;SUSPENDED&quot;,&quot;endTime&quo :0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

实时计算（流计算） API

#### ListSessionClusters

调用ListSessionClusters，列出指定工作区和命名空间下的所有会话集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "SessionClusterList", "items": [] } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/sessionclusters HTTP/1.1 &RegionId=cn-wulan-env***-d01 &workspace=default &namespace=flinkteam
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{},\"apiVersion\":\"v1\",\"kind\":\"SessionClusterList\",\"items\":[]
}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SessionClusterList&quot;,&quot tems&quot;:[]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ListSavepoints

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Query | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| jobId | String | Query | 否 | 5af678c0-7db0-4650- 94c2-d2604f0a**** | 作业实例ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "SavepointList", "items": [{ "metadata": { "createdAt": "2026- 04-24T03:55:16Z", "jobId": "f736bbd6- c9cf-48ab-973a- 9653bb0f8c0a", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:55:19Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 2, "namespace": "flinkteam", "annotations": { "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "9", "taker": " \| vvp-0" }, "comment": "", "id": "5cea0d88-303d- 44e5-a96e- 47f7217723d7" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "flinkSavepointId": "fc2e33c1-8132- 516f-2923- 7371060fb449", "savepointLocation": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- savepoints/namespa ces/flinkteam/deplo yments/a3d88b2a- e076-4491-86f2- 5a81ea4c7300/5cea 0d88-303d-44e5- a96e- 47f7217723d7/save point-f736bb- f467305080c0" }, "status": { "state": "COMPLETED" } }, { "metadata": { "createdAt": "2026- 04-24T03:52:08Z", "jobId": "e5c412be- c160-460a-9d7b- 0b7111c77e15", "workspace": "9 9 7 1hl19" | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | "9cuwr9g7y1hl19", "示na例tiveFormat": false, "modifiedAt": | 说明 |
|---|---|---|---|
|  |  | "2026-04- 24T03:52:13Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 2, "namespace": "flinkteam", "annotations": { "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "6", "taker": " \| vvp-0" }, "comment": "", "id": "58778df9-5082- 4da3-9890- d531fcc1200d" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "flinkSavepointId": "3ac331a3-6ef9- d8f7-e3e8- e3d5b2649180", "savepointLocation": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- savepoints/namespa ces/flinkteam/deplo yments/a3d88b2a- e076-4491-86f2- 5a81ea4c7300/5877 8df9-5082-4da3- 9890- d531fcc1200d/save point-e5c412- 8a27e8210de8" }, "status": { "state": "COMPLETED" } }] } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{},\"apiVersion\":\"v1\",\"kind\":\"SavepointList\",\"items\":[{\"met
adata\":{\"createdAt\":\"2026-04-24T03:55:16Z\",\"jobId\":\"f736bbd6-c9cf-48ab-973a-9653bb0f 8c0a\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2026-04-24T0 3:55:19Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinkteam\",\ nnotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"9\",\"taker\":\" | vvp-0\"},\"comment\":\"\",\"id\":\"5cea0d88-303d-44e5-a96e- 47f7217723d7\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"fc2e33c1-8132-516f-2923- 7371060fb449\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-savepoi nts/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/5cea0d88-303d- 44e5-a96e-47f7217723d7/savepoint-f736bb-f467305080c0\"},\"status\": {\"state\":\"COMPLETED\"}},{\"metadata\":{\"createdAt\":\"2026-04- 24T03:52:08Z\",\"jobId\":\"e5c412be-c160-460a-9d7b- 0b7111c77e15\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2026- 04-24T03:52:13Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":2,\"namespace\":\"flinkteam\",\ nnotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"6\",\"taker\":\" | vvp-0\"},\"comment\":\"\",\"id\":\"58778df9-5082-4da3-9890d531fcc1200d\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"flinkSavepointId\":\"3ac331a3-6ef9-d8f7-e3e8e3d5b2649180\",\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-savepoi nts/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9-5082- 4da3-9890-d531fcc1200d/savepoint-e5c412-8a27e8210de8\"},\"status\": {\"state\":\"COMPLETED\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;SavepointList&quot;,&quot;item quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:55:16Z&quot;,&quot;jobId&quot;:&quot;f736bbd6-c9cf-48ab-973a- 9653bb0f8c0a&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quot;:f se,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:55:19Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2-5a81ea4c7300&quot; ,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot;:2,&quot;namespace&quo :&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;9&quot;,&quo taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;5cea0d88-303d-44e5-a96e-47f72 17723d7&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint&quot;,&q t;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;fc2e33c1-8132-516f-2923-7371060fb449&quot;, &quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-savepoints /namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/5cea0d88-303d-44e5a96e-47f7217723d7/savepoint-f736bb-f467305080c0&quot;},&quot;status&quot;:{&quot;state&quot; :&quot;COMPLETED&quot;}},{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04-24T03:52 :08Z&quot;,&quot;jobId&quot;:&quot;e5c412be-c160-460a-9d7b- 0b7111c77e15&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quot;:f se,&quot;modifiedAt&quot;:&quot;2026-04- 24T03:52:13Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076-4491-86f2-5a81ea4c7300&quot; ,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot;:2,&quot;namespace&quo :&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;6&quot;,&quo taker&quot;:&quot; | vvp- 0&quot;},&quot;comment&quot;:&quot;&quot;,&quot;id&quot;:&quot;58778df9-5082-4da3-9890-d531f cc1200d&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint&quot;,&q t;spec&quot;:{&quot;flinkSavepointId&quot;:&quot;3ac331a3-6ef9-d8f7-e3e8-e3d5b2649180&quot;, &quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-savepoints /namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9-5082-4da3- 9890-d531fcc1200d/savepoint-e5c412-8a27e8210de8&quot;},&quot;status&quot;:{&quot;state&quot; :&quot;COMPLETED&quot;}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ListNetworkPolicyIpAddress

调用ListNetworkPolicyIpAddress，查询指定网络策略下的所有IP地址列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /flink/namespace/listIp HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | String | Path | 是 | blinkteam | Namespace名称。 |
| region | String | Path | 否 | cn-wulan-env***-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | / | 详细信息。 |
| -IpAddress | String | 192.168.XX.XX | IP地址。 |
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例

```
GET /flink/namespace/listIp HTTP/1.1 &RegionId=cn-wulan-env***-d01 &name=blinkteam
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "IpAddress":"192.168.XX.XX"
  }
```

`],`

```json
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>
 <IpAddress>192.168.XX.XX</IpAddress>
</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

实时计算（流计算） API

#### ListNamespaces

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/namespaces/v1/namespaces HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "@type": "type.googleapis.co m/vvp.namespaces. v1.ListNamespacesR esponse", "namespaces": [{ "roleBindings": [{ "role": "owner", "members": ["user:23540697665 705****"] }, { "role": "owner", "members": ["user:16640766570 0****"] }], "cluster": "", "isHa": false, "workspace": "9cuwr9g7y1hl19", "cpuBrand": "Intel", "previewSessionClus terName": "", "createTime": "2026-04- 24T03:33:43.68062 6Z", "lifecyclePhase": "LIFECYCLE PHASE _ _ ACTIVE", "name": "namespaces/flinkte am", "labels": {} }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

实时计算（流计算） API 请求示例

```
GET /pop/namespaces/v1/namespaces HTTP/1.1 &RegionId=cn-wulan-env***-d01
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse\",\"namespaces\":[ {\"roleBindings\":[{\"role\":\"owner\",\"members\":[\"user:23540697665705****\"]},{\"role\": \"owner\",\"members\": [\"user:166407665700****\"]}],\"cluster\":\"\",\"isHa\":false,\"workspace\":\"9cuwr9g7y1hl19\" "cpuBrand\":\"Intel\",\"previewSessionClusterName\":\"\",\"createTime\":\"2026-04-24T03:33:4 3.680626Z\",\"lifecyclePhase\":\"LIFECYCLE_PHASE_ACTIVE\",\"name\":\"namespaces/flinkteam\",\" bels\":{}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.namespaces.v1.ListNamespacesResponse&quot;,&q t;namespaces&quot;:[{&quot;roleBindings&quot;: [{&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:23540697665705****&quot;]}, {&quot;role&quot;:&quot;owner&quot;,&quot;members&quot;: [&quot;user:166407665700****&quot;]}],&quot;cluster&quot;:&quot;&quot;,&quot;isHa&quot;:false, uot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;cpuBrand&quot;:&quot;Intel&quot;,&quot;pr iewSessionClusterName&quot;:&quot;&quot;,&quot;createTime&quot;:&quot;2026-04-24T03:33:43.68 0626Z&quot;,&quot;lifecyclePhase&quot;:&quot;LIFECYCLE_PHASE_ACTIVE&quot;,&quot;name&quot;:&qu ;namespaces/flinkteam&quot;,&quot;labels&quot;:{}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ListDeploymentTargets

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": {}, "apiVersion": "v1", "kind": "DeploymentTarget List", "items": [{ "metadata": { "createdAt": "2026- 04-24T03:33:44Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:33:44Z", "resourceVersion": 1, "name": "dt- flinkteam", "namespace": "flinkteam", "annotations": { "creator": "149497451012584 6", "modifier": "149497451012584 6", "creatorName": "null", "modifierName": "null" }, "id": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentTarget" , "ha": false, "spec": { "kubernetes": { "namespace": "flinkteam" }, "kind": "kubernetes", "state": "ONLINE" } }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-targets HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
 "data":"{\"metadata\":{},\"apiVersion\":\"v1\",\"kind\":\"DeploymentTargetList\",\"items\":
[{\"metadata\":{\"createdAt\":\"2026-04- 24T03:33:44Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:33:44Z\",\"resourceVersion\":1,\"name\":\"dtflinkteam\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"1494974510125846\",\"modifier\":\"1494974510125846\",\"creatorName\":\"null\",\ odifierName\":\"null\"},\"id\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\",\"labels\":{}},\"api Version\":\"v1\",\"kind\":\"DeploymentTarget\",\"ha\":false,\"spec\":{\"kubernetes\":{\"name space\":\"flinkteam\"},\"kind\":\"kubernetes\",\"state\":\"ONLINE\"}}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;: {},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTargetList&quot;,&qu ;items&quot;:[{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:33:44Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04-24T03:33:44Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;dt-flinktea m&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;:{&quot;creator&q uot;:&quot;1494974510125846&quot;,&quot;modifier&quot;:&quot;1494974510125846&quot;,&quot;crea rName&quot;:&quot;null&quot;,&quot;modifierName&quot;:&quot;null&quot;},&quot;id&quot;:&quot;a ff052-38c6-4fd3-9b91-e9c53f8ee019&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentTarget&quot;,&quot; &quot;:false,&quot;spec&quot;:{&quot;kubernetes&quot;: {&quot;namespace&quot;:&quot;flinkteam&quot;},&quot;kind&quot;:&quot;kubernetes&quot;,&quot;st e&quot;:&quot;ONLINE&quot;}}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ListDeployments

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

|  |  |  |  | Flink企 | 业版开发指南·AppManager |
|---|---|---|---|---|---|

API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| pageSize | String | Query | 否 | 10 | 分页参数，表示所请求页码元素数量，最大值为100，最小值为1，默认值为10。 |
| pageIndex | String | Query | 否 | 1 | 分页参数，页码索引，表示所请求页码，最小值为1，默认值为1。 |
| sortName | String | Query | 否 | ["age", "name"] | 表示按年龄和姓名进行排序的字段列表。 |
| sortOrder | String | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：顺序。 默认值：DESC。 |
| creator | String | Query | 否 | 235406976657057054 | 规则创建者。 |
| modifier | String | Query | 否 | yunduntest | 更新人。 |
| priority | String | Query | 否 | 1 | 线路优先级。1优先级最高， 数值越大优先级越低。 |
| deploymen tId | String | Query | 否 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| name | String | Query | 否 | blinkteam | namespace名称。 |
| status | String | Query | 否 | 1 | 状态。 |
| state | String | Query | 否 | false | 剧本的运行状态： true： 发布流程。 false： 禁用流程。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchMode | Boole an | Query | 否 | false | 表示禁用批量处理模式，适用于逐个处理任务或数据的情况。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "DeploymentList", "items": [{ "metadata": { "createdAt": "2026- 04-30T03:54:19Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 30T05:38:17Z", "resourceVersion": 4, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "235406976657057 054", "resource- plan.has.migrated": "true", "storage.disaster.rp o": "1800", "deployment.has.de ployed": "false", "deployment.source -type": "EDITOR", "deployment.parent. id": "", "modifier": "235406976657057 054", "creatorName": "flinkadmin", "plan.uri": "deployment/91510 cd2-9d21-463a- abf4- 9c608d23e92e/reso urcePlan.json", "priority": "5", "priority.class.name ": "flink-p5", "migration.display.e nabled": "false", "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "2", "default.resource- |  |

实时计算（流计算） API

| 参数名称 | 类型 | setting.has.migrate d示":例 "true", | 说明 |
|---|---|---|---|
|  |  | "deployment.refere nced.deployment.dr aft.history.version": "7", "deployment.refere nced.deployment.dr aft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "modifierName": "flinkadmin", "taker": " \| vvp-0", "deployment.refere nced.deployment.dr aft.history.id": "c7819685-3abe- 4115-a26b- d40e73c58856" }, "id": "91510cd2- 9d21-463a-abf4- 9c608d23e92e", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "fine-grained", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": |  |
| data | String | "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- manifest-251107", "kind": "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | FROM d示a例tahub table;", _ | 说明 |
|---|---|---|---|
|  |  | "imageUserDefined" : false, "flinkImageRegistry" : "cn-wulan-env**- d01- reg.docker.intra.env **.shuguang.com:80 /ververica-paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposito ry": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 0, "state": "CANCELLED", "endTime": 0 } }] } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":
{\"totalSize\":1,\"totalPage\":1},\"apiVersion\":\"v1\",\"kind\":\"DeploymentList\",\"items\": [{\"metadata\":{\"createdAt\":\"2026-04- 30T03:54:19Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 30T05:38:17Z\",\"resourceVersion\":4,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"annotat ns\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.has.deployed\":\"f se\",\"deployment.sourcetype\":\"EDITOR\",\"deployment.parent.id\":\"\",\"modifier\":\"235406976657057054\",\"creatorN e\":\"flinkadmin\",\"plan.uri\":\"deployment/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5\",\"m igration.display.enabled\":\"false\",\"com.dataartisans.appmanager.controller.deployment.spec. rsion\":\"2\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\":\"7 ,\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4a03-a628-a6fe665c525e\",\"mo difierName\":\"flinkadmin\",\"taker\":\" | vvp- 0\",\"deployment.referenced.deployment.draft.history.id\":\"c7819685-3abe-4115-a26b-d40e73c5 8856\"},\"id\":\"91510cd2-9d21-463a-abf4-9c608d23e92e\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"template\":{\"metadata\":{\"an notations\":{\"flink.resource.type\":\"finegrained\",\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\": {\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strn ame VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (st rname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SEL ECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FR OM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env**-d01 -reg.docker.intra.env**.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-flink-1 .17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"batchMod ":false,\"resources\":{\"jobmanager\":{\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\":{\"me mory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgradeS ategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"deployme TargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":0,\"state\":\"CANCELLED\",\"endTime\":0}}]}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

实时计算（流计算） API `XML` 格式实时计算（流计算） API

```xml
<data>{&quot;metadata&quot;: {&quot;totalSize&quot;:1,&quot;totalPage&quot;:1},&quot;apiVersion&quot;:&quot;v1&quot;,&quot; nd&quot;:&quot;DeploymentList&quot;,&quot;items&quot;:[{&quot;metadata&quot;:{&quot;createdA t&quot;:&quot;2026-04- 30T03:54:19Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 30T05:38:17Z&quot;,&quot;resourceVersion&quot;:4,&quot;name&quot;:&quot;sqlJob&quot;,&quot;nam pace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&qu ;deployment.has.deployed&quot;:&quot;false&quot;,&quot;deployment.source-type&quot;:&quot;ED ITOR&quot;,&quot;deployment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;2354069766 057054&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deploym t/91510cd2-9d21-463a-abf4- 9c608d23e92e/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.class.n e&quot;:&quot;flinkp5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;com.dataartisans.appman er.controller.deployment.spec.version&quot;:&quot;2&quot;,&quot;default.resource-setting.has .migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.history.version& ot;:&quot;7&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&quot;cee26b6e-d03b- 4a03-a628a6fe665c525e&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;taker&quot;:&quot;
| vvp-0&quot;,&quot;deployment.referenced.deployment.draft.history.id&quot;:&quot;c7819685-3
abe-4115-a26b-d40e73c58856&quot;},&quot;id&quot;:&quot;91510cd2-9d21-463a-abf4- 9c608d23e92e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;spec&q t;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryable-stat e.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot;}},& ot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr-8.0.7-manife st-251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TE MPORARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datag en&#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( &#x27 ;connector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 1
0) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM
datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot;c wulan-env**-d01-reg.docker.intra.env**.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot;1.1 quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;:{&quot;jo bmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;stat quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJobCre ionAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8ee01 9&quot;},&quot;status&quot;: {&quot;startTime&quot;:0,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime&quot;:0}}]}</ data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

实时计算（流计算） API

#### ListArtifacts

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.artifacts.v1.Li stArtifactsResponse ", "artifacts": [{ "filename": "TopSpeedWindowin g.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "235406976657057 054", "namespace": "namespaces/flinkte am", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/arti facts/namespaces/fli nkteam/TopSpeedWi ndowing.jar", "content": "" }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:list HTTP/1.1 &RegionId=cn-wulan-env188-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse\",\"artifacts\":[{\" filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04-29T09:20:14Z\", \"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\",\"uri\":\"oss://fli -fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.ListArtifactsResponse&quot;,&quo artifacts&quot;: [{&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,&quot; eateTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&quot;:& ot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/ artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&quot;:&quot;&quot;}]} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### GetGlobalDeploymentDefaults

调用GetGlobalDeploymentDefaults，获取实时计算服务中的全局部署默认配置。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Header | 是 | flinkteam | 作业所在的项目空间名称。 |

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "apiVersion": "v1", "kind": "GlobalDeployment Defaults", "spec": { "template": { "metadata": { "annotations": { "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "kind": "JAR", "imageUserDefined" : false }, "parallelism": 1, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1 } } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/global-deployment-defaults HTTP/1.1 &RegionId=cn-wulan-env188-d01 &workspace=default
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
 "data":"{\"apiVersion\":\"v1\",\"kind\":\"GlobalDeploymentDefaults\",\"spec\":{\"template\"
:{\"metadata\":{\"annotations\":{\"native.kubernetes.mode\":\"true\",\"flink.queryable-state .enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\":{\"ki nd\":\"JAR\",\"imageUserDefined\":false},\"parallelism\":1,\"resources\":{\"jobmanager\":{\" memory\":\"4Gi\",\"cpu\":1.0},\"taskmanager\":{\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\": {\"log4jLoggers\":{\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgradeS ategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;GlobalDeploymentDefaults&quot;,& ot;spec&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryable-state.enabled&quo t;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot;}},&quot;spec&quo :{&quot;artifact&quot;: {&quot;kind&quot;:&quot;JAR&quot;,&quot;imageUserDefined&quot;:false},&quot;parallelism&quot;: &quot;resources&quot;:{&quot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;stat quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### GetDeploymentDefaults

调用GetDeploymentDefaults，查询实时计算中指定命名空间和工作区的部署默认配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2026- 04-24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "resourceVersion": 1, "name": "stream", "namespace": "flinkteam", "annotations": { "deployment.default s.type": "stream", "creator": "system", "modifier": "system" }, "id": "690e3396- 700a-4b77-9fcf- d14a592f****", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDefault s", "spec": { "template": { "spec": { "resources": {}, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "table.exec.state.ttl" : "36 h", "restart- strategy.fixed- delay.delay": "10 s", "restart- strategy.fixed- delay.attempts": "2147483647", "execution.checkpoi nting.min-pause": "180s", "restart- strategy": "fixed- delay" } } } } } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-defaults HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例实时计算（流计算） API `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:46:53Z\",\"resourceVersion\":1,\"name\":\"stream\",\"namespace\":\"flinkteam\",\"annotat ns\": {\"deployment.defaults.type\":\"stream\",\"creator\":\"system\",\"modifier\":\"system\"},\"id\ \"690e3396-700a-4b77-9fcf-d14a592f****\",\"labels\": {}},\"apiVersion\":\"v1\",\"kind\":\"DeploymentDefaults\",\"spec\":{\"template\":{\"spec\":{ \"resources\":{},\"flinkConfiguration\": {\"execution.checkpointing.interval\":\"180s\",\"table.exec.state.ttl\":\"36 h\",\"restart-s trategy.fixed-delay.delay\":\"10 s\",\"restart-strategy.fixeddelay.attempts\":\"2147483647\",\"execution.checkpointing.min-pause\":\"180s\",\"restart-str ategy\":\"fixed-delay\"}}}}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 24T03:46:53Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;stream&quot;,&quot;nam pace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;deployment.defaults.type&quot;:&quot;stream&quot;,&quot;creator&quot;:&quot;system&quot &quot;modifier&quot;:&quot;system&quot;},&quot;id&quot;:&quot;690e3396-700a-4b77-9fcf-d14a59 2f****&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDefaults&quot;,&quo spec&quot;:{&quot;template&quot;:{&quot;spec&quot;:{&quot;resources&quot;:{},&quot;flinkConf iguration&quot;: {&quot;execution.checkpointing.interval&quot;:&quot;180s&quot;,&quot;table.exec.state.ttl&quot &quot;36 h&quot;,&quot;restart-strategy.fixed-delay.delay&quot;:&quot;10 s&quot;,&quot;restart-strategy.fixeddelay.attempts&quot;:&quot;2147483647&quot;,&quot;execution.checkpointing.min-pause&quot;:&q uot;180s&quot;,&quot;restart-strategy&quot;:&quot;fixed-delay&quot;}}}}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### GetDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTT P/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "metadata": { "createdAt": "2026- 04-24T03:47:01Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:58:26Z", "resourceVersion": 174, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "creator": "235406976657057 054", "resource- plan.has.migrated": "true", "storage.disaster.rp o": "1800", "deployment.source -type": "EDITOR", "deployment.has.de ployed": "false", "deployment.parent. id": "", "modifier": "235406976657057 054", "creatorName": "flinkadmin", "plan.uri": "deployment/a3d88 b2a-e076-4491- 86f2- 5a81ea4c7300/reso urcePlan.json", "priority": "5", "priority.class.name ": "flink-p5", "migration.display.e |  |

实时计算（流计算） API

| 参数名称 | 类型 | nabled": "false", "示de例ployment.exec- | 说明 |
|---|---|---|---|
|  |  | plan.uri.valid": "true", "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "13", "default.resource- setting.has.migrate d": "true", "deployment.refere nced.deployment.dr aft.history.version": "1", "deployment.exec- plan.uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- jobs/namespaces/fli nkteam/jobs/c944e9 78-5cb9-4879-8312- c0872ee50182/exec |  |
| data | String | Plan.json", "deployment.refere nced.deployment.dr aft.id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "resources.from.job. has.migrated": "true", "taker": " \| vvp-0", "modifierName": "flinkadmin", "deployment.refere nced.deployment.dr aft.history.id": "561a6a3d-7858- 4056-acfb- ad0cdec09e55" }, "id": "a3d88b2a- e076-4491-86f2- 5a81ea4c7300", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "fine-grained", "job.resource.total. memory.byte": "0", "job.resource.total.c pu": "0.0", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.17.0-vvr-8.0.7- | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | manifest-251107", "示ki例nd": | 说明 |
|---|---|---|---|
|  |  | "SQLSCRIPT", "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table;", _ "imageUserDefined" : false, "flinkImageRegistry" : "cn-wulan-env35- d01- reg.docker.intra.env 35.shuguang.com:8 0/ververica-paas", "versionName": "vvr-8.0.7-flink- 1.17", "flinkImageReposito ry": "vvr", "flinkVersion": "1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "FROM SAVEPOINT", _ "allowNonRestoredS tate": false, "savepointId": |  |

实时计算（流计算） API

| 参数名称 | 类型 | "5cea0d88-303d- 4示4例e5-a96e- | 说明 |
|---|---|---|---|
|  |  | 47f7217723d7" }, "state": "CANCELLED", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019" }, "status": { "startTime": 1777002980004, "state": "CANCELLED", "endTime": 0 } } |  |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTT P/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:47:01Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:58:26Z\",\"resourceVersion\":174,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"annot ions\":{\"creator\":\"235406976657057054\",\"resourceplan.has.migrated\":\"true\",\"storage.disaster.rpo\":\"1800\",\"deployment.source-type\":\" EDITOR\",\"deployment.has.deployed\":\"false\",\"deployment.parent.id\":\"\",\"modifier\":\"23 06976657057054\",\"creatorName\":\"flinkadmin\",\"plan.uri\":\"deployment/a3d88b2a-e076-4491 -86f2-5a81ea4c7300/resourcePlan.json\",\"priority\":\"5\",\"priority.class.name\":\"flink-p5 \",\"migration.display.enabled\":\"false\",\"deployment.execplan.uri.valid\":\"true\",\"com.dataartisans.appmanager.controller.deployment.spec.version\":\ 3\",\"default.resourcesetting.has.migrated\":\"true\",\"deployment.referenced.deployment.draft.history.version\":\"1 ,\"deployment.exec-plan.uri\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-jobs/namespace s/flinkteam/jobs/c944e978-5cb9-4879-8312c0872ee50182/execPlan.json\",\"deployment.referenced.deployment.draft.id\":\"cee26b6e-d03b-4 a03-a628-a6fe665c525e\",\"resources.from.job.has.migrated\":\"true\",\"taker\":\" | vvp- 0\",\"modifierName\":\"flinkadmin\",\"deployment.referenced.deployment.draft.history.id\":\"56 6a3d-7858-4056-acfb-ad0cdec09e55\"},\"id\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"labels\":{}},\"apiVersion\":\"v1\",\"kind\":\"Deployment\",\"spec\":{\"temp late\":{\"metadata\":{\"annotations\":{\"flink.resource.type\":\"finegrained\",\"job.resource.total.memory.byte\":\"0\",\"job.resource.total.cpu\":\"0.0\",\"native ubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\": {\"flinkImageTag\":\"1.17.0-vvr-8.0.7-manifest- 251107\",\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"CREATE TEMPORARY TABLE `datahub_table` (strn ame VARCHAR)\with (\ 'connector' = 'datagen'\);\\CREATE TEMPORARY TABLE `kafka_table` (st rname VARCHAR, lens BIGINT)\with (\ 'connector' = 'print'\);\\INSERT INTO kafka_table\SEL ECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens\FR OM\ datahub_table;\",\"imageUserDefined\":false,\"flinkImageRegistry\":\"cn-wulan-env35-d01 -reg.docker.intra.env35.shuguang.com:80/ververica-paas\",\"versionName\":\"vvr-8.0.7-flink-1 .17\",\"flinkImageRepository\":\"vvr\",\"flinkVersion\":\"1.17\"},\"parallelism\":1,\"batchMod ":false,\"resources\":{\"jobmanager\":{\"memory\":\"2Gi\",\"cpu\":0.5},\"taskmanager\":{\"me mory\":\"3Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLoggers\": {\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"FROM_SAVEPOINT\",\"allowNonRestoredState\":false,\"savepointId\":\"5cea0d88-303d -44e5-a96e-47f7217723d7\"},\"state\":\"CANCELLED\",\"upgradeStrategy\": {\"kind\":\"NONE\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"deployme TargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"},\"status\": {\"startTime\":1777002980004,\"state\":\"CANCELLED\",\"endTime\":0}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:47:01Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 24T03:58:26Z&quot;,&quot;resourceVersion&quot;:174,&quot;name&quot;:&quot;sqlJob&quot;,&quot;n espace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;resourceplan.has.migrated&quot;:&quot;true&quot;,&quot;storage.disaster.rpo&quot;:&quot;1800&quot;,&qu ;deployment.source-
```

实时计算（流计算） API

```xml
type&quot;:&quot;EDITOR&quot;,&quot;deployment.has.deployed&quot;:&quot;false&quot;,&quot;depl ment.parent.id&quot;:&quot;&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;cr torName&quot;:&quot;flinkadmin&quot;,&quot;plan.uri&quot;:&quot;deployment/a3d88b2a-e076-449 1-86f2- 5a81ea4c7300/resourcePlan.json&quot;,&quot;priority&quot;:&quot;5&quot;,&quot;priority.class.n e&quot;:&quot;flinkp5&quot;,&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;deployment.exec-plan. uri.valid&quot;:&quot;true&quot;,&quot;com.dataartisans.appmanager.controller.deployment.spec. rsion&quot;:&quot;13&quot;,&quot;default.resourcesetting.has.migrated&quot;:&quot;true&quot;,&quot;deployment.referenced.deployment.draft.histo .version&quot;:&quot;1&quot;,&quot;deployment.exec-plan.uri&quot;:&quot;oss://flink-fullyman aged-9cuwr9g7y1hl19/flink-jobs/namespaces/flinkteam/jobs/c944e978-5cb9-4879-8312-c0872ee5018 2/execPlan.json&quot;,&quot;deployment.referenced.deployment.draft.id&quot;:&quot;cee26b6e-d 03b-4a03-a628a6fe665c525e&quot;,&quot;resources.from.job.has.migrated&quot;:&quot;true&quot;,&quot;taker&qu ;:&quot; | vvp- 0&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;deployment.referenced.deployment raft.history.id&quot;:&quot;561a6a3d-7858-4056-acfbad0cdec09e55&quot;},&quot;id&quot;:&quot;a3d88b2a-e076-4491-86f2- 5a81ea4c7300&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Deployment&quot;,&quot;spec&q t;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;flink.resource.type&quot;:&quot;finegrained&quot;,&quot;job.resource.total.memory.byte&quot;:&quot;0&quot;,&quot;job.resource.tota cpu&quot;:&quot;0.0&quot;,&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.quer blestate.enabled&quot;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot; ,&quot;spec&quot;:{&quot;artifact&quot;:{&quot;flinkImageTag&quot;:&quot;1.17.0-vvr-8.0.7manifest- 251107&quot;,&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;CREATE TEMPO RARY TABLE `datahub_table` (strname VARCHAR)with ( &#x27;connector&#x27; = &#x27;datagen&
#x27;);CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with (    &#x27;co
nnector&#x27; = &#x27;print&#x27;);INSERT INTO kafka_tableSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table;&quot;,&quot;imageUserDefined&quot;:false,&quot;flinkImageRegistry&quot;:&quot;c wulan-env35-d01-reg.docker.intra.env35.shuguang.com:80/ververicapaas&quot;,&quot;versionName&quot;:&quot;vvr-8.0.7-flink- 1.17&quot;,&quot;flinkImageRepository&quot;:&quot;vvr&quot;,&quot;flinkVersion&quot;:&quot;1.1 quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;:{&quot;jo bmanager&quot;: {&quot;memory&quot;:&quot;2Gi&quot;,&quot;cpu&quot;:0.5},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;3Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;FROM_SAVEPOINT&quot;,&quot;allowNonRestoredState&quot;:false,&quot;sav ointId&quot;:&quot;5cea0d88-303d-44e5-a96e- 47f7217723d7&quot;},&quot;state&quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;:{&qu ot;kind&quot;:&quot;NONE&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJobCreatio ttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f8ee019&qu ot;},&quot;status&quot;: {&quot;startTime&quot;:1777002980004,&quot;state&quot;:&quot;CANCELLED&quot;,&quot;endTime&quo :0}}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

实时计算（流计算） API

#### GetArtifactMetadata

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata HT TP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| filename | String | Query | 是 | test.csv | 文件名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "artifact": { "filename": "TopSpeedWindowin g.jar", "size": "0", "createTime": "2026-04- 29T09:20:14Z", "uploader": "235406976657057 054", "namespace": "namespaces/flinkte am", "uri": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/arti facts/namespaces/fli nkteam/TopSpeedWi ndowing.jar", "content": "" }, "@type": "type.googleapis.co m/vvp.artifacts.v1.G etArtifactMetadataR esponse" } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:getMetadata HT TP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &filename=test.csv &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"artifact\":
{\"filename\":\"TopSpeedWindowing.jar\",\"size\":\"0\",\"createTime\":\"2026-04-29T09:20:14Z \",\"uploader\":\"235406976657057054\",\"namespace\":\"namespaces/flinkteam\",\"uri\":\"oss:// ink-fullymanaged- 9cuwr9g7y1hl19/artifacts/namespaces/flinkteam/TopSpeedWindowing.jar\",\"content\":\"\"},\"@typ ":\"type.googleapis.com/vvp.artifacts.v1.GetArtifactMetadataResponse\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>{&quot;artifact&quot;: {&quot;filename&quot;:&quot;TopSpeedWindowing.jar&quot;,&quot;size&quot;:&quot;0&quot;,&quot;c ateTime&quot;:&quot;2026-04- 29T09:20:14Z&quot;,&quot;uploader&quot;:&quot;235406976657057054&quot;,&quot;namespace&quot;:& ot;namespaces/flinkteam&quot;,&quot;uri&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/ artifacts/namespaces/flinkteam/TopSpeedWindowing.jar&quot;,&quot;content&quot;:&quot;&quot;},& ot;@type&quot;:&quot;type.googleapis.com/vvp.artifacts.v1.GetArtifactMetadataResponse&quot;} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ExecuteSqlScript

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/ 1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | {"statement":"Drop TABLE `vvp`.`default`.`test`"} | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.E xecuteStatementsR esponse", "responses": [{ "result": "RESULT SUCCESS", _ "errorMessages": [] }] } | 详细信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute HTTP/ 1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"
{\"@type\":\"type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse\",\"responses\":[ {\"result\":\"RESULT_SUCCESS\",\"errorMessages\":[]}]}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data> {&quot;@type&quot;:&quot;type.googleapis.com/vvp.sql.v1beta1.ExecuteStatementsResponse&quot;,& ot;responses&quot;: [{&quot;result&quot;:&quot;RESULT_SUCCESS&quot;,&quot;errorMessages&quot;:[]}]}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### DeployDeploymentDraft

调用DeployDeploymentDraft，部署实时计算任务到指定的工作区和命名空间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） API

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP /1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
|  |  |  |  | { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "resourceVersion": 32, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "migration.display.enable d": "false", "creator": "235406976657057054", "modifier": "235406976657057054", "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5", "deployment.draft.referen ced.deployment.id": "7325ac07-e466-4c1b- b598-311c6f2c103b" }, "labels": {}, "lock": { "metadata": { "createdAt": "2026-04- 24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "235406976657057054", "modifier": "235406976657057054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, |  |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | "apiVersion": "v1", "kind": "示Lo例ck", "spec": { | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | "holderName": "flinkadmin", "holderId": "235406976657057054" } }, "id": "cee26b6e- d03b-4a03-a628- a6fe665c525e", "parentId": "cd1562be- 02ed-32cf-945b- 9769afe4c55e", "description": "cd1562be- 02ed-32cf-945b- 9769afe4c55e" }, "spec": { "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "restoreStrategy": { "kind": "LATEST STATE" _ }, "deploymentTargetId": "a89ff052-38c6-4fd3- 9b91-e9c53f8ee019", "maxSavepointCreationAt tempts": 4, "maxJobCreationAttempts ": 1, "template": { "metadata": { | 执行参数，sql脚本。 |
|  |  |  |  | "annotations": { "flink.resource.type": "fine-grained", "native.kubernetes.mode" : "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.enabled ": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "versionName": "vvr- 8.0.7-flink-1.17", "imageUserDefined": false, "sqlScript": "CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( 'connector' = 'datagen' ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( 'connector' = 'print' ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH (strname) _ AS BIGINT) AS lens FROM datahub table;" }, _ "parallelism": 1, "resources": { "jobmanager": { "memory": "2Gi", "cpu": 0.5 }, "taskmanager": { "memory": "3Gi", "cpu": 1.0 } }, "flinkConfiguration": {}, |  |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | "logging": { "示lo例g4jLoggers": { "": | 说明 |
|---|---|---|---|---|---|
|  |  |  |  | "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "batchMode": false } } } } |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2026- 04- 24T03:52:07.76400 1Z", "jobId": "e5c412be-c160- 460a-9d7b- 0b7111c77e15", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:52:07.76400 1Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 1, "namespace": "flinkteam", "annotations": { "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "6", "taker": " \| vvp-0" }, "id": "58778df9- 5082-4da3-9890- d531fcc1200d" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "savepointLocation": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- savepoints/namespa ces/flinkteam/deplo yments/a3d88b2a- e076-4491-86f2- 5a81ea4c7300/5877 8df9-5082-4da3- 9890- d531fcc1200d" }, "status": { "state": "STARTED" } } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/deploy HTTP /1.1 { "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-24T03:52:07.764001Z\",\"jobId\":\"e5c412be-c
160-460a-9d7b- 0b7111c77e15\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2026- 04-24T03:52:07.764001Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":1,\"namespace\":\"flinkteam\",\ nnotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"6\",\"taker\":\" | vvp-0\"},\"id\":\"58778df9-5082-4da3-9890d531fcc1200d\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9- 5082-4da3-9890-d531fcc1200d\"},\"status\":{\"state\":\"STARTED\"}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:52:07.764001Z&quot;,&quot;jobId&quot;:&quot;e5c412be-c160-460a-9d7b-0b7111c77e15&quot; ,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quot;:false,&quot;modifie t&quot;:&quot;2026-04-24T03:52:07.764001Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076 -4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot;:1,& ot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;6&quot;,&quo taker&quot;:&quot; | vvp-0&quot;},&quot;id&quot;:&quot;58778df9-5082-4da3-9890-d531fcc1200d& quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint&quot;,&quot;spec uot;:{&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-save points/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9-5082-4 da3-9890-d531fcc1200d&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;STARTED&quot;}} </data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### DeleteNetworkPolicyIpAddress

调用DeleteNetworkPolicyIpAddress，删除指定网络策略中的IP地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 实时计算（流计算） API

**请求语法**

```
DELETE /flink/namespace/deleteIp HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| name | String | Path | 是 | blinkteam | Namespace名称。 |
| region | String | Path | 否 | cn-wulan-env188-d01 | Region名称。 |
| ipAddress | String | Path | 是 | xxx.xxx.xx.xxx | IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | {} | 详细信息。 |

**示例**

请求示例

```
DELETE /flink/namespace/deleteIp HTTP/1.1 &RegionId=cn-wulan-env188-d01 &name=blinkteam &ipAddress= xxx.xxx.xx.xxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>{}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### DeleteDeployment

调用DeleteDeployment，删除指定的部署资源，释放相关工作负载及关联组件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） API

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTTP/1.1 &RegionId=cn-wulan-env***-d01 &namespace=flinkteam &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### DeleteArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP /1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| filename | String | Query | 是 | test.csv | 文件名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间 ID。您可以通过以下任意一种方式获取： 通过 ListNamespaces 获取。 在 Flink 全托管开发控制台工作空间详情中获取。 |

实时计算（流计算） API

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:delete HTTP /1.1 &RegionId=cn-wulan-env188-d01 &namespace=flinkteam &filename=test.csv &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### CreateSavepoint

调用CreateSavepoint，创建保存点，用于事务处理中标记一个可回滚的状态位置。

**请求头**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Header | 是 | cn-wulan-env188-d01 | Region名称。 |

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "deploymentId": "7325ac07-e466-4c1b- b598-311c6f2c103b" } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "createdAt": "2026- 04- 24T03:52:07.76400 1Z", "jobId": "e5c412be-c160- 460a-9d7b- 0b7111c77e15", "workspace": "9cuwr9g7y1hl19", "nativeFormat": false, "modifiedAt": "2026-04- 24T03:52:07.76400 1Z", "deploymentId": "a3d88b2a-e076- 4491-86f2- 5a81ea4c7300", "origin": "USER REQUEST", _ "resourceVersion": 1, "namespace": "flinkteam", "annotations": { "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "6", "taker": " \| vvp-0" }, "id": "58778df9- 5082-4da3-9890- d531fcc1200d" }, "apiVersion": "v1", "kind": "Savepoint", "spec": { "savepointLocation": "oss://flink- fullymanaged- 9cuwr9g7y1hl19/flin k- savepoints/namespa ces/flinkteam/deplo yments/a3d88b2a- e076-4491-86f2- 5a81ea4c7300/5877 8df9-5082-4da3- 9890- d531fcc1200d" }, "status": { "state": "STARTED" } } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/savepoints HTTP/1.1 { "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-24T03:52:07.764001Z\",\"jobId\":\"e5c412be-c
160-460a-9d7b- 0b7111c77e15\",\"workspace\":\"9cuwr9g7y1hl19\",\"nativeFormat\":false,\"modifiedAt\":\"2026- 04-24T03:52:07.764001Z\",\"deploymentId\":\"a3d88b2a-e076-4491-86f2- 5a81ea4c7300\",\"origin\":\"USER_REQUEST\",\"resourceVersion\":1,\"namespace\":\"flinkteam\",\ nnotations\": {\"com.dataartisans.appmanager.controller.deployment.spec.version\":\"6\",\"taker\":\" | vvp-0\"},\"id\":\"58778df9-5082-4da3-9890d531fcc1200d\"},\"apiVersion\":\"v1\",\"kind\":\"Savepoint\",\"spec\": {\"savepointLocation\":\"oss://flink-fullymanaged-9cuwr9g7y1hl19/flinksavepoints/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9- 5082-4da3-9890-d531fcc1200d\"},\"status\":{\"state\":\"STARTED\"}}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:52:07.764001Z&quot;,&quot;jobId&quot;:&quot;e5c412be-c160-460a-9d7b-0b7111c77e15&quot; ,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;nativeFormat&quot;:false,&quot;modifie t&quot;:&quot;2026-04-24T03:52:07.764001Z&quot;,&quot;deploymentId&quot;:&quot;a3d88b2a-e076 -4491-86f2- 5a81ea4c7300&quot;,&quot;origin&quot;:&quot;USER_REQUEST&quot;,&quot;resourceVersion&quot;:1,& ot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;com.dataartisans.appmanager.controller.deployment.spec.version&quot;:&quot;6&quot;,&quo taker&quot;:&quot; | vvp-0&quot;},&quot;id&quot;:&quot;58778df9-5082-4da3-9890-d531fcc1200d& quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Savepoint&quot;,&quot;spec uot;:{&quot;savepointLocation&quot;:&quot;oss://flink-fullymanaged-9cuwr9g7y1hl19/flink-save points/namespaces/flinkteam/deployments/a3d88b2a-e076-4491-86f2-5a81ea4c7300/58778df9-5082-4 da3-9890-d531fcc1200d&quot;},&quot;status&quot;:{&quot;state&quot;:&quot;STARTED&quot;}} </data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### CreateDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） API

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
|  |  | { "metadata": { "createdAt": "2026- 04- 24T03:46:53.34248 4Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53.34248 4Z", "resourceVersion": 1, "name": "sqlJob", "namespace": "flinkteam", "annotations": { "migration.display.e |  |

实时计算（流计算） API

|  |  | g p y |  |
|---|---|---|---|
| 参数名称 | 类型 | nabled": "false", 示例 "creator": | 说明 |
| data | String | "235406976657057 054", "modifier": "235406976657057 054", "creatorName": "flinkadmin", "modifierName": "flinkadmin", "priority": "5" }, "description": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "lock": { "metadata": { "createdAt": "2026- 04-24T03:46:53Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:46:53Z", "namespace": "flinkteam", "annotations": { "creator": "235406976657057 054", "modifier": "235406976657057 054" }, "id": "313fde08-4b44- 38b5-99c4- 7f3038449796" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "235406976657057 054" } }, "id": "cee26b6e-d03b- 4a03-a628- a6fe665c525e", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4c55e", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false", "flink.security.ssl.en abled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "INSERT INTO mySink SELECT | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | SELECT S示U例BSTRING(a,0,10) AS a, | 说明 |
|---|---|---|---|
|  |  | CAST(CHAR LENGT _ H(a) AS BIGINT) as cnt FROM mySource;", "imageUserDefined" : false, "versionName": "vvr-8.0.7-flink- 1.17" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 1.0 }, "taskmanager": { "memory": "4Gi", "cpu": 1.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": {} } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "a89ff052-38c6- 4fd3-9b91- e9c53f8ee019" } } |  |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments HTTP/1.1 { "RegionId":"cn-wulan-env***-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:46:53.342484Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04-24T03:46:53. 342484Z\",\"resourceVersion\":1,\"name\":\"sqlJob\",\"namespace\":\"flinkteam\",\"annotations\ {\"migration.display.enabled\":\"false\",\"creator\":\"235406976657057054\",\"modifier\":\"235 6976657057054\",\"creatorName\":\"flinkadmin\",\"modifierName\":\"flinkadmin\",\"priority\":\" "},\"description\":\"cd1562be-02ed-32cf-945b-9769afe4c55e\",\"lock\":{\"metadata\":{\"create dAt\":\"2026-04-24T03:46:53Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04-24T 03:46:53Z\",\"namespace\":\"flinkteam\",\"annotations\": {\"creator\":\"235406976657057054\",\"modifier\":\"235406976657057054\"},\"id\":\"313fde08-4 b44-38b5-99c4-7f3038449796\"},\"apiVersion\":\"v1\",\"kind\":\"Lock\",\"spec\":{\"holderName \":\"flinkadmin\",\"holderId\":\"235406976657057054\"}},\"id\":\"cee26b6e-d03b-4a03-a628-a6f e665c525e\",\"parentId\":\"cd1562be-02ed-32cf-945b-9769afe4c55e\",\"labels\":{}},\"apiVersio n\":\"v1\",\"kind\":\"DeploymentDraft\",\"spec\":{\"template\":{\"metadata\":{\"annotations\ ":{\"native.kubernetes.mode\":\"true\",\"flink.queryablestate.enabled\":\"false\",\"flink.security.ssl.enabled\":\"false\"}},\"spec\":{\"artifact\": {\"kind\":\"SQLSCRIPT\",\"sqlScript\":\"INSERT INTO mySink SELECT SUBSTRING(a,0,10) AS a, CA ST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;\",\"imageUserDefined\":false,\"versionName\":\"vvr-8.0.7-flink- 1.17\"},\"parallelism\":1,\"batchMode\":false,\"resources\":{\"jobmanager\":{\"memory\":\"4G i\",\"cpu\":1.0},\"taskmanager\":{\"memory\":\"4Gi\",\"cpu\":1.0}},\"logging\":{\"log4jLogge rs\":{\"\":\"INFO\"},\"logReservePolicy\": {\"expirationDays\":7,\"openHistory\":true},\"loggingProfile\":\"default\"},\"flinkConfigurati \":{}}},\"restoreStrategy\": {\"kind\":\"LATEST_STATE\",\"allowNonRestoredState\":false},\"state\":\"CANCELLED\",\"upgradeS ategy\": {\"kind\":\"STATELESS\"},\"maxSavepointCreationAttempts\":4,\"maxJobCreationAttempts\":1,\"dep ymentTargetId\":\"a89ff052-38c6-4fd3-9b91-e9c53f8ee019\"}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&qu ;:&quot;2026-04- 24T03:46:53.342484Z&quot;,&quot;resourceVersion&quot;:1,&quot;name&quot;:&quot;sqlJob&quot;,&q t;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;: {&quot;migration.display.enabled&quot;:&quot;false&quot;,&quot;creator&quot;:&quot;23540697665 57054&quot;,&quot;modifier&quot;:&quot;235406976657057054&quot;,&quot;creatorName&quot;:&quot; inkadmin&quot;,&quot;modifierName&quot;:&quot;flinkadmin&quot;,&quot;priority&quot;:&quot;5&qu ;},&quot;description&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;lock&quot;:{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026- 04- 24T03:46:53Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 24T03:46:53Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;annotations&quot;:{&quo t;creator&quot;:&quot;235406976657057054&quot;,&quot;modifier&quot;:&quot;235406976657057054&q t;},&quot;id&quot;:&quot;313fde08-4b44-38b5-99c4- 7f3038449796&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Lock&quot;,&q t;spec&quot;: {&quot;holderName&quot;:&quot;flinkadmin&quot;,&quot;holderId&quot;:&quot;235406976657057054&q t;}},&quot;id&quot;:&quot;cee26b6e-d03b-4a03-a628a6fe665c525e&quot;,&quot;parentId&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;,&quot;labels&quot;: {}},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;DeploymentDraft&quot;,&quot;s c&quot;:{&quot;template&quot;:{&quot;metadata&quot;:{&quot;annotations&quot;: {&quot;native.kubernetes.mode&quot;:&quot;true&quot;,&quot;flink.queryable-state.enabled&quo t;:&quot;false&quot;,&quot;flink.security.ssl.enabled&quot;:&quot;false&quot;}},&quot;spec&quo :{&quot;artifact&quot;: {&quot;kind&quot;:&quot;SQLSCRIPT&quot;,&quot;sqlScript&quot;:&quot;INSERT INTO mySink SELEC T SUBSTRING(a,0,10) AS a, CAST(CHAR_LENGTH(a) AS BIGINT) as cnt FROM mySource;&quot;,&quot;imageUserDefined&quot;:false,&quot;versionName&quot;:&quot;vvr-8.0.7-f link- 1.17&quot;},&quot;parallelism&quot;:1,&quot;batchMode&quot;:false,&quot;resources&quot;:{&qu ot;jobmanager&quot;: {&quot;memory&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0},&quot;taskmanager&quot;:{&quot;memo ry&quot;:&quot;4Gi&quot;,&quot;cpu&quot;:1.0}},&quot;logging&quot;: {&quot;log4jLoggers&quot;:{&quot;&quot;:&quot;INFO&quot;},&quot;logReservePolicy&quot;:{&quo t;expirationDays&quot;:7,&quot;openHistory&quot;:true},&quot;loggingProfile&quot;:&quot;defaul quot;},&quot;flinkConfiguration&quot;:{}}},&quot;restoreStrategy&quot;: {&quot;kind&quot;:&quot;LATEST_STATE&quot;,&quot;allowNonRestoredState&quot;:false},&quot;stat quot;:&quot;CANCELLED&quot;,&quot;upgradeStrategy&quot;: {&quot;kind&quot;:&quot;STATELESS&quot;},&quot;maxSavepointCreationAttempts&quot;:4,&quot;maxJ CreationAttempts&quot;:1,&quot;deploymentTargetId&quot;:&quot;a89ff052-38c6-4fd3-9b91-e9c53f 8ee019&quot;}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### AddNetworkPolicyIpAddress

调用AddNetworkPolicyIpAddress，向指定网络策略添加IP地址以增强安全访问控制。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） API

```
POST /flink/namespace/addIp HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| name | String | Path | 是 | blinkteam | namespace名称。 |
| region | String | Path | 否 | cn-wulan-env188-d01 | region名称。 |
| ipAddress | String | Path | 是 | xxx.xxx.xx.xxx | IP地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | {} | 详细信息。 |

**示例**

请求示例

```json
POST /flink/namespace/addIp HTTP/1.1 { "RegionId":"cn-wulan-env188-d01", "name":"blinkteam", "ipAddress":"xxx.xxx.xx.xxx" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":" {}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data> {}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### ListTables

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTables HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces 获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | catalog下数据库名称。 |
| RegionId | String | Host | 是 | cn-wulan-env230-d01 | region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 202107221428- KKE3K857WS | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"tables": [{"name":"blackhole ","schema": {"column": [{"name":"id","type" :"VARCHAR(214748 3647)","expression": ""}],"watermarkSpe c":[]},"properties": {"connector":"black hole"},"comment":" "}, {"name":"blackhole sink","schema": _ {"column": [{"name":"name","t ype":"VARCHAR(214 7483647)","expressi on":""}, {"name":"score","ty pe":"BIGINT","expre ssion":""}],"waterm arkSpec": []},"properties": {"connector":"black hole"},"comment":" blackhole sink table"}]} | 详细信息。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listTables HTTP/1.1
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "202107221428-KKE3K857WS",
  "success": true,
  "data": {
    "tables": [
      {
        "name": "blackhole",
        "schema": {
          "column": [
            {
              "name": "id",
              "type": "VARCHAR(2147483647)",
              "expression": ""
            }
```

`],`

```json
        },
        "properties": {
          "connector": "blackhole"
        },
        "comment": ""
      },
      {
        "name": "blackhole_sink",
        "schema": {
          "column": [
            {
              "name": "name",
              "type": "VARCHAR(2147483647)",
              "expression": ""
            },
            {
              "name": "score",
              "type": "BIGINT",
              "expression": ""
            }
```

`],`

```json
        },
        "properties": {
          "connector": "blackhole"
        },
        "comment": "blackhole sink table"
      }
```

]

```
  }
}
```

`XML` 格式实时计算（流计算） API

```xml
<requestId>202107221428-KKE3K857WS</requestId> <success>true</success> <data>
 <tables>
  <name>blackhole</name>
  <schema>
   <column>
    <name>id</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
  </schema>
  <properties>
   <connector>blackhole</connector>
  </properties>
  <comment  />
 </tables>
 <tables>
  <name>blackhole_sink</name>
  <schema>
   <column>
    <name>name</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
   <column>
    <name>score</name>
    <type>BIGINT</type>
    <expression  />
   </column>
  </schema>
  <properties>
   <connector>blackhole</connector>
  </properties>
  <comment>blackhole sink table</comment>
 </tables>
</data>
```

#### ListCatalogs

调用ListCatalogs，获取指定工作空间指定namespace下的catalog列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.List CatalogsResponse", "catalogs": [{"name":"namespa ces/flinkteam/catalo gs/vvp","properties" : {"defaultDatabase": "default","type":"vvp "}}]} | 详细数据。 |
| requestId | String | 31F99ADC-B72E- 4BA1-AD32- B938D5A57532 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs HTTP/1.1 &RegionId= &namespace= &workspace=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "31F99ADC-B72E-4BA1-AD32-B938D5A57532",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse",
    "catalogs": [
      {
        "name": "namespaces/flinkteam/catalogs/vvp",
        "properties": {
          "defaultDatabase": "default",
          "type": "vvp"
        }
      }
```

]

```
  }
}
```

`XML` 格式

```xml
<requestId>31F99ADC-B72E-4BA1-AD32-B938D5A57532</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListCatalogsResponse</@type>
 <catalogs>
  <name>namespaces/flinkteam/catalogs/vvp</name>
  <properties>
   <defaultDatabase>default</defaultDatabase>
   <type>vvp</type>
  </properties>
 </catalogs>
</data>
```

#### GetDatabase

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatabase HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env230-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.Get DatabaseResponse", "database": {"name":"default"," properties": {},"comment":"The default database"},"succes s":true,"message":"" } | 详细信息。 |
| requestId | String | C345CF08-769F- 4C28-A60F- 6C8A30FEAFA6 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDatabase HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database=
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "requestId": "C345CF08-769F-4C28-A60F-6C8A30FEAFA6",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse",
    "database": {
      "name": "default",
      "properties": {},
      "comment": "The default database"
    },
    "success": true,
    "message": ""
  }
}
```

`XML` 格式

```xml
<requestId>C345CF08-769F-4C28-A60F-6C8A30FEAFA6</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetDatabaseResponse</@type>
 <database>
  <name>default</name>
  <properties  />
  <comment>The default database</comment>
 </database>
 <success>true</success>
 <message  />
</data>
```

#### ListFunctions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunction HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region名称。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | catalog数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"@type":"type.goo gleapis.com/vvp.sql. catalog.v1beta2.List FunctionsResponse" ,"functions": [{"name":"Timesta mpProbe","classNa me":"com.alibaba.bl ink.udtf.TimestampP robe","functionLang uage":"FUNCTION L _ ANGUAGE JAVA","fu _ nctionType":"FUNCT ION TYPE FLINK","d _ _ escription":"This is a user-defined function"}, {"name":"Transform Udtf","className":" com.alibaba.blink.u dtf.TransformUdtf"," functionLanguage":" FUNCTION LANGUA _ GE JAVA","functionT _ ype":"FUNCTION TY _ PE FLINK","descripti _ on":"This is a user- defined function"}]} | 详细数据。 |
| requestId | String | 0ADBBDD0-E2E9- 4611-98C6- 6767A3AB87D2 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listFunction HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
  "requestId": "0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse",
    "functions": [
      {
        "name": "TimestampProbe",
        "className": "com.alibaba.blink.udtf.TimestampProbe",
        "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
        "functionType": "FUNCTION_TYPE_FLINK",
        "description": "This is a user-defined function"
      },
      {
        "name": "TransformUdtf",
        "className": "com.alibaba.blink.udtf.TransformUdtf",
        "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
        "functionType": "FUNCTION_TYPE_FLINK",
        "description": "This is a user-defined function"
      }
```

]

```
  }
}
```

`XML` 格式实时计算（流计算） API

```xml
<requestId>0ADBBDD0-E2E9-4611-98C6-6767A3AB87D2</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListFunctionsResponse</@type>
 <functions>
  <name>TimestampProbe</name>
  <className>com.alibaba.blink.udtf.TimestampProbe</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </functions>
 <functions>
  <name>TransformUdtf</name>
  <className>com.alibaba.blink.udtf.TransformUdtf</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </functions>
</data>
```

#### DatabaseExists

调用DatabaseExists，确认catalog下的指定database是否存在。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databaseExis HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | catalog下数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.DatabaseExi stsResponse", "exists": true } | 详细信息。 |
| requestId | String | 41CAB2BF-B428- 4240-A746- 1F6CE6DE36B3 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:databaseExis HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "requestId": "41CAB2BF-B428-4240-A746-1F6CE6DE36B3",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse",
    "exists": true
  }
}
```

`XML` 格式实时计算（流计算） API

```xml
<requestId>41CAB2BF-B428-4240-A746-1F6CE6DE36B3</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.DatabaseExistsResponse</@type>
 <exists>true</exists>
</data>
```

#### CreateConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "type": "hologres-fix", "name": "namespaces/flinkteam/c onnectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": true, "dependencies": [ "hdfs:///tmp/myconnector s/ververica-connector- hologres-1.15-vvr-6.0- fix.jar" ], "supportedFormats": [ "json", "csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | 新connector参数信息，包括 connector类型、名称、支持的连接参数、能否作为 sourc、sink、支持的 format、依赖的jar等。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "connector": { "lookup": true, "supportedFormats" : [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkte am/connectors/holo gres-fix", "source": true, "type": "hologres-fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myconn ectors/ververica- connector-hologres- 1.15-vvr-6.0-fix.jar" ] }, "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateConnectorResp onse" } | 新connector详细信息。 |
| requestId | String | 86E24541-89EE- 46F9-84CE- 0EC888B9414A | 请求ID。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "data": {
    "connector": {
      "lookup": true,
      "supportedFormats": [
        "json",
        "csv"
```

`],`

```json
      "environments": [],
      "sink": true,
      "name": "namespaces/flinkteam/connectors/hologres-fix",
      "source": true,
      "type": "hologres-fix",
      "properties": [
        {
          "defaultValue": "hologres-fix",
          "description": "",
          "definesFormat": false,
          "key": "connector",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "dbname",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "endpoint",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "tablename",
          "required": true
        }
```

`],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

]

```json
    },
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse"
  },
  "success": true,
  "requestId": "86E24541-89EE-46F9-84CE-0EC888B9414A"
}
```

实时计算（流计算） API `XML` 格式

```xml
<data>
 <connector>
  <lookup>true</lookup>
  <supportedFormats>json</supportedFormats>
  <supportedFormats>csv</supportedFormats>
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myconnectors/ververica-connector-hologres-1.15-vvr-6.0-
fix.jar</dependencies>
 </connector>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateConnectorResponse</@type>
</data> <success>true</success> <requestId>86E24541-89EE-46F9-84CE-0EC888B9414A</requestId>
```

#### CreateMember

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 实时计算（流计算） API

**请求语法**

```
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "role": "viewer", "member": "242425410145292209" } | 用户授权信息，为指定用户授予指定业务权限，权限枚举： viewer、owner、eidtor。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | E3D311D5-77CB- 452F-B9EA- C215C8201363 | 请求ID。 |
| data | String | { "@type": "type.googleapis.co m/vvp.members.v1. CreateMemberResp onse", "member": { "role": "viewer", "member": "user:24242541014 5292209" } } | 用户业务授权详细信息。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1 { "workspace":"", "namespace":"", "RegionId":"" }
```

实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "data": {
    "@type": "type.googleapis.com/vvp.members.v1.CreateMemberResponse",
    "member": {
      "role": "viewer",
      "member": "user:242425410145292209"
    }
  },
  "success": true,
  "requestId": "E3D311D5-77CB-452F-B9EA-C215C8201363"
}
```

`XML` 格式

```xml
<data>
 <@type>type.googleapis.com/vvp.members.v1.CreateMemberResponse</@type>
 <member>
  <role>viewer</role>
  <member>user:242425410145292209</member>
 </member>
</data> <success>true</success> <requestId>E3D311D5-77CB-452F-B9EA-C215C8201363</requestId>
```

#### CreateSecretValue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env17e-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | { "metadata": { "name": "secretKey" }, "spec": { "kind": "Plain", "value": "secretValue" } } | 请求参数，指定变量名称和变量值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "metadata": { "createdAt": "2024- 03- 11T03:32:51.57826 4Z", "modifiedAt": "2024-03- 11T03:32:51.57826 4Z", "resourceVersion": 1, "name": "secretKey", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6a17fb60-78df- 46f5-a6e2- 671ce61f8e6c", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "secretValue" } } | 详细数据。 |
| requestId | String | 19E71203-97A1- 4355-8C25- D566CA823F95 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "metadata": {
      "createdAt": "2024-03-11T03:32:51.578264Z",
      "modifiedAt": "2024-03-11T03:32:51.578264Z",
      "resourceVersion": 1,
      "name": "secretKey",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "modifierName": "flinkadmin"
      },
      "id": "6a17fb60-78df-46f5-a6e2-671ce61f8e6c",
      "labels": {}
    },
    "apiVersion": "v1",
    "kind": "SecretValue",
    "spec": {
      "kind": "Plain",
      "value": "secretValue"
    }
  },
  "success": true,
  "requestId": "19E71203-97A1-4355-8C25-D566CA823F95"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <metadata>
  <createdAt>2024-03-11T03:32:51.578264Z</createdAt>
  <modifiedAt>2024-03-11T03:32:51.578264Z</modifiedAt>
  <resourceVersion>1</resourceVersion>
  <name>secretKey</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <modifierName>flinkadmin</modifierName>
  </annotations>
  <id>6a17fb60-78df-46f5-a6e2-671ce61f8e6c</id>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>SecretValue</kind>
 <spec>
  <kind>Plain</kind>
  <value>secretValue</value>
 </spec>
</data> <success>true</success> <requestId>19E71203-97A1-4355-8C25-D566CA823F95</requestId>
```

#### CreateFormat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

| link企业版开 API | 发指南·Ap | pManager |  |  | 实时计算（流计算） |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | 自定format创建参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateFormatRespon se", "format": { "sink": false, "name": "namespaces/flinkte am/formats/customi zed-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myform ats/customized-csv- demo-1.0- SNAPSHOT.jar" ] } } | 新增format详细信息。 |
| requestId | String | 0ED81455-6971- 4EBA-BBD4- 3F686175080D | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse",
    "format": {
      "sink": false,
      "name": "namespaces/flinkteam/formats/customized-csv",
      "source": true,
      "type": "customized-csv",
      "properties": [
        {
          "defaultValue": ",",
          "description": "",
          "definesFormat": false,
          "key": "format.column-delimiter",
          "required": false
        }
```

`],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar"
```

]

```json
    }
  },
  "success": true,
  "requestId": "0ED81455-6971-4EBA-BBD4-3F686175080D"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateFormatResponse</@type>
 <format>
  <sink>false</sink>
  <name>namespaces/flinkteam/formats/customized-csv</name>
  <source>true</source>
  <type>customized-csv</type>
  <properties>
   <defaultValue>,</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>format.column-delimiter</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar</dependencies>
 </format>
</data> <success>true</success> <requestId>0ED81455-6971-4EBA-BBD4-3F686175080D</requestId>
```

#### CreateUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env17e-d01 | Region ID。 |
| paramsJso n | String | Body | 否 | { "name": "metric- transform-227", "jarUrl": "hdfs:///tmp/udf/metric- transform-2.2.7- shaded.jar" } | udf参数，指定待创建的udf 使用的jar包所在的存储路径及udf名称（注意：指定路径的udf jar必须真实存在）。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.C reateUdfArtifactRes ponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 11T02:54:24.82276 6Z", "uploader": "229852610122763 813", "jarUpdateTime": "2024-03- 11T02:54:24.82276 6Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "namespace": "flinkteam", "jarUrl": "hdfs:///tmp/udf/met ric-transform-2.2.7- shaded.jar", "updateTime": "2024-03- 11T02:54:24.82276 6Z" } } | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 8F0CFB56-7CE8- 45AA-A788- 41B7D2504E5F | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse",
    "collidingClasses": [],
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
        {
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
        },
        {
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
        }
```

`],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-11T02:54:24.822766Z",
      "uploader": "229852610122763813",
      "jarUpdateTime": "2024-03-11T02:54:24.822766Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227",
      "namespace": "flinkteam",
      "jarUrl": "hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-11T02:54:24.822766Z"
    }
  },
  "requestId": "8F0CFB56-7CE8-45AA-A788-41B7D2504E5F",
  "success": true
}
```

实时计算（流计算） API `XML` 格式

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.CreateUdfArtifactResponse</@type>
 <collidingClasses  />
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-11T02:54:24.822766Z</createTime>
  <uploader>229852610122763813</uploader>
  <jarUpdateTime>2024-03-11T02:54:24.822766Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227</name>
  <namespace>flinkteam</namespace>
  <jarUrl>hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-11T02:54:24.822766Z</updateTime>
 </udfArtifact>
</data> <requestId>8F0CFB56-7CE8-45AA-A788-41B7D2504E5F</requestId> <success>true</success>
```

#### DeleteConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP /1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | hologres-fix | 要删除的connector名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 7113AD53-5192- 46E5-B592- 81175BAF7F54 | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP /1.1 &RegionId= &workspace= &name= &namespace=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "success": true,
  "requestId": "7113AD53-5192-46E5-B592-81175BAF7F54"
}
```

`XML` 格式

```xml
<success>true</success> <requestId>7113AD53-5192-46E5-B592-81175BAF7F54</requestId>
```

实时计算（流计算） API

#### DeleteDeploymentDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployme ntDraftId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |
| deploymen tDraftId | String | Path | 是 | afb75048-590a-4ac3- 84d4-96f873b14659 | 待删除的draft ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "createdAt": "2024- 03-13T01:46:23Z", "modifiedAt": "2024-03- 13T01:56:47Z", "resourceVersion": 26, "name": "mytable", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", |  |

实时计算（流计算） API

| 参数名称 | 类型 | "comment": "", "示m例odifierName": | 说明 |
|---|---|---|---|
|  |  | "flinkadmin", "priority": "5" }, |  |
| data | String | "id": "afb75048- 590a-4ac3-84d4- 96f873b14659", "parentId": "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-13 09:46:19 -- Description: Write your description here -- ******************** ******************** ******************** ********-- INSERT INTO `vvp`.`default`.print Sink SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM `vvp`.`default`.data genSource; ", "imageUserDefined" : false, "versionName": "vvr-6.0.0-flink- 1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { | draft详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | "log4jLoggers": { "": "示IN例FO" }, | 说明 |
|---|---|---|---|
|  |  | "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" } } |  |
| requestId | String | 374ECDF6-D148- 4A78-9548- F550EA53255A | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployme ntDraftId] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "data": {
    "metadata": {
      "createdAt": "2024-03-13T01:46:23Z",
      "modifiedAt": "2024-03-13T01:56:47Z",
      "resourceVersion": 26,
      "name": "mytable",
      "namespace": "flinkteam",
      "annotations": {
"creator":"229852610122763813",
```

实时计算（流计算） API

```json
        creator: 229852610122763813,
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "comment": "",
        "modifierName": "flinkadmin",
        "priority": "5"
      },
      "id": "afb75048-590a-4ac3-84d4-96f873b14659",
      "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
      "labels": {}
    },
    "apiVersion": "v1",
    "kind": "DeploymentDraft",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
            "flink.queryable-state.enabled": "false"
          }
        },
        "spec": {
          "artifact": {
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-13 09:46:19-- Description: Write your descrip tion here--********************************************************************--INSERT INTO `vvp`.`default`.printSinkSELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM `vvp`.`default`.datagenSource;",
            "imageUserDefined": false,
            "versionName": "vvr-6.0.0-flink-1.15"
          },
          "parallelism": 1,
          "batchMode": false,
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            },
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            }
          },
          "logging": {
            "log4jLoggers": {
              "": "INFO"
            },
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
            },
            "loggingProfile": "default"
          },
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
}
```

实时计算（流计算） API

```json
          }
        }
      },
      "restoreStrategy": {
        "kind": "LATEST_STATE",
        "allowNonRestoredState": false
      },
      "state": "CANCELLED",
      "upgradeStrategy": {
        "kind": "STATELESS"
      },
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
    }
  },
  "success": true,
  "requestId": "374ECDF6-D148-4A78-9548-F550EA53255A"
}
```

`XML` 格式

```xml
<data>
 <metadata>
  <createdAt>2024-03-13T01:46:23Z</createdAt>
  <modifiedAt>2024-03-13T01:56:47Z</modifiedAt>
  <resourceVersion>26</resourceVersion>
  <name>mytable</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <comment  />
   <modifierName>flinkadmin</modifierName>
   <priority>5</priority>
  </annotations>
  <id>afb75048-590a-4ac3-84d4-96f873b14659</id>
  <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraft</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-13 09:46:19 -- Description: Write your description here
```

实时计算（流计算） API

```xml
--********************************************************************-- INSERT INTO `vvp`.`default`.printSink SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  `vvp`.`default`.datagenSource;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
    <flinkConfiguration>
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>CANCELLED</state>
  <upgradeStrategy>
   <kind>STATELESS</kind>
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
</data> <success>true</success> <requestId>374ECDF6-D148-4A78-9548-F550EA53255A</requestId>
```

实时计算（流计算） API

#### DeleteFormat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env****-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | customized-csv | 待删除的format名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | EC30D915-1E89- 4B66-B1AA- C5D161DAB50D | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1. &RegionId= &workspace= &name= &namespace=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{"requestId":"EC30D915-1E89-4B66-B1AA-C5D161DAB50D"}
```

`XML` 格式

```xml
<requestId>EC30D915-1E89-4B66-B1AA-C5D161DAB50D</requestId>
```

#### DeleteMember

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1
```

`.1`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |
| member | String | Path | 是 | user:2424254101452922 09 | 待解除授权的用户信息，格式：user:${uid}。 |
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 8AA170D4-F4D1- 4E90-A02D- 0CC211BE8171 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```
DELETE /pop/workspaces/[workspace]/members/v1/namespaces/[namespace]/members/[member] HTTP/1
```

`.1`

```
&workspace= &namespace= &member= &RegionId=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "success": true,
  "requestId": "8AA170D4-F4D1-4E90-A02D-0CC211BE8171"
}
```

`XML` 格式

```xml
<success>true</success> <requestId>8AA170D4-F4D1-4E90-A02D-0CC211BE8171</requestId>
```

#### DeleteSecretValue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1
```

`.1`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env17e-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 否 | secretKey | 变量名称。 |

实时计算（流计算） API

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 1CCA8A71-98C6- 491B-9A2D- ADDFC0939294 | 请求ID。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values/[name] HTTP/1
```

`.1`

```
&RegionId= &namespace= &workspace=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "success": true,
  "requestId": "1CCA8A71-98C6-491B-9A2D-ADDFC0939294"
}
```

`XML` 格式

```xml
<success>true</success> <requestId>1CCA8A71-98C6-491B-9A2D-ADDFC0939294</requestId>
```

#### DeleteUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |

|  | 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager AP | I |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "referencedClasses" : [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.D eleteUdfArtifactResp onse" } | 详细信息。 |
| requestId | String | 07E49735-A389- 4853-AFBA- 28F9EB0EFDC4 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1 &RegionId= &workspace= &namespace= &udfArtifactName=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "referencedClasses": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse"
  },
  "requestId": "07E49735-A389-4853-AFBA-28F9EB0EFDC4",
  "success": true
}
```

`XML` 格式

```xml
<data>
 <referencedClasses  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.DeleteUdfArtifactResponse</@type>
</data> <requestId>07E49735-A389-4853-AFBA-28F9EB0EFDC4</requestId> <success>true</success>
```

#### ExecuteSqlscriptsStatements

调用ExecuteSqlscriptsStatements，进行Function管理。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute-multi HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |
| paramsJso n | String | Body | 否 | {"executeFunctionStr": ["DROP FUNCTION `TimestampProbe`"]} | 执行参数，sql脚本。 |

**返回数据**

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istUdfArtifactsRespo nse", "udfArtifacts": [ { "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "jarUrl": "hdfs:///tmp/udf/met ric-transform-2.2.7- shaded.jar", "udfClasses": [ { "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ ", "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227", "functionNames": [ "TimestampProbe" ] } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "dependencyJarUris" : [], "uploader": "229852610122763 813", "namespace": "namespaces/flinkte am", "createTime": "2024-03- 11T02:54:25Z", "updateTime": "2024-03- 11T02:54:25Z", "jarUpdateTime": "2024-03- 11T02:54:25Z" } ] } | function详细信息。 |
| requestId | String | 151E1A19-091A- 4317-ADF9- FDD81C735414 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/sqlscripts:execute-multi HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "requestId": "151E1A19-091A-4317-ADF9-FDD81C735414",
  "success": true,
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse",
    "udfArtifacts": [
      {
        "name": "namespaces/flinkteam/udfartifacts/metric-transform-227",
        "jarUrl": "hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar",
        "udfClasses": [
          {
            "className": "com.alibaba.blink.udtf.TimestampProbe",
            "classType": "UDF_TYPE_SCALAR",
            "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227",
            "functionNames": [
              "TimestampProbe"
```

]

```
          }
```

`],`

```json
        "artifactType": "ARTIFACT_TYPE_JAVA",
        "dependencyJarUris": [],
        "uploader": "229852610122763813",
        "namespace": "namespaces/flinkteam",
        "createTime": "2024-03-11T02:54:25Z",
        "updateTime": "2024-03-11T02:54:25Z",
        "jarUpdateTime": "2024-03-11T02:54:25Z"
      }
```

]

```
  }
}
```

`XML` 格式实时计算（流计算） API

```xml
<requestId>151E1A19-091A-4317-ADF9-FDD81C735414</requestId> <success>true</success> <data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListUdfArtifactsResponse</@type>
 <udfArtifacts>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227</name>
  <jarUrl>hdfs:///tmp/udf/metric-transform-2.2.7-shaded.jar</jarUrl>
  <udfClasses>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227</udfArtifactName>
   <functionNames>TimestampProbe</functionNames>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <dependencyJarUris  />
  <uploader>229852610122763813</uploader>
  <namespace>namespaces/flinkteam</namespace>
  <createTime>2024-03-11T02:54:25Z</createTime>
  <updateTime>2024-03-11T02:54:25Z</updateTime>
  <jarUpdateTime>2024-03-11T02:54:25Z</jarUpdateTime>
 </udfArtifacts>
</data>
```

#### ForcefullyCreateLock

调用ForcefullyCreateLock，给指定资源加锁（通常是draft）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| workspace | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceTy pe | String | Query | 否 | DeploymentDraft | 欲锁定的资源类型，锁定 draft时传： DeploymentDraft。 |
| resourceId | String | Query | 否 | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | 欲锁定的资源ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 69DEC7C2-BCE5- 4E80-8CDA- FE7ADE09AAAD | 请求ID。 |
| data | String | { "metadata": { "createdAt": "2024- 03- 12T10:16:35.16403 4Z", "modifiedAt": "2024-03- 12T10:16:35.16403 4Z", "namespace": "flinkteam", "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } } | 资源锁定详情。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/locks HTTP/1.1 { "RegionId":"", "namespace":"", "workspace":"" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T10:16:35.164034Z",
      "modifiedAt": "2024-03-12T10:16:35.164034Z",
      "namespace": "flinkteam",
      "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
    },
    "apiVersion": "v1",
    "kind": "Lock",
    "spec": {
      "holderName": "flinkadmin",
      "holderId": "229852610122763813"
    }
  },
  "success": true,
  "requestId": "69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD"
}
```

`XML` 格式

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T10:16:35.164034Z</createdAt>
  <modifiedAt>2024-03-12T10:16:35.164034Z</modifiedAt>
  <namespace>flinkteam</namespace>
  <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>Lock</kind>
 <spec>
  <holderName>flinkadmin</holderName>
  <holderId>229852610122763813</holderId>
 </spec>
</data> <success>true</success> <requestId>69DEC7C2-BCE5-4E80-8CDA-FE7ADE09AAAD</requestId>
```

#### FunctionExists

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functionExis HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| function | String | Query | 是 | TransformUdtf | function名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.FunctionExis tsResponse", "exists": true } | 详细信息。 |
| requestId | String | D96DD415-AD97- 4EBA-832E- 99FADB6A4F87 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:functionExis HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &function=
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "requestId": "D96DD415-AD97-4EBA-832E-99FADB6A4F87",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse",
    "exists": true
  }
}
```

`XML` 格式

```xml
<requestId>D96DD415-AD97-4EBA-832E-99FADB6A4F87</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.FunctionExistsResponse</@type>
 <exists>true</exists>
</data>
```

#### GenerateResourcePlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an:generate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业deploymentId。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"default \",\"cpu\":0.2,\"heap\ ":\"768 mb\",\"offHeap\":\"3 2 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\"S treamExecTableSou rceScan\",\"desc\":\" Source: datahub table[4]\",\ _ "profile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":2,\"type\":\"St reamExecCalc\",\"de sc\":\"Calc[5]\",\"pro file\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":3,\"type\":\"St reamExecSink\",\"de sc\":\"Sink: kafka table[6]\",\"pr _ ofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}],\"edges\": [{\"source\":1,\"targ et\":2,\"mode\":\"PIP ELINED\",\"strategy\ ":\"FORWARD\"}, {\"source\":2,\"targe t\":3,\"mode\":\"PIPE LINED\",\"strategy\": \"FORWARD\"}],\"ve rtices\": {\"717c7b8afebbfb7 137f6f0f99beb2a94\ ":[1,2,3]}}" } | 资源配置计划详细信息。 |
| requestId | String | 58091710-5895- 4111-A4FF- BEA51550A359 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an:generate HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"", "deploymentId":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "success": true,
    "plan": "{\"ssgProfiles\":[{\"name\":\"default\",\"cpu\":0.2,\"heap\":\"768 mb\",\"offHe
ap\":\"32 mb\",\"managed\":{},\"extended\":{}}],\"nodes\": [{\"id\":1,\"type\":\"StreamExecTableSourceScan\",\"desc\":\"Source: datahub_table[4]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":2,\"type\":\"StreamExecCalc\",\"desc\":\"Calc[5]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":3,\"type\":\"StreamExecSink\",\"desc\":\"Sink: kafka_table[6]\",\"profile\":{\"group\": \"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}}],\"edges\":[{\ "source\":1,\"target\":2,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"},{\"source\":2,\"ta rget\":3,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"}],\"vertices\": {\"717c7b8afebbfb7137f6f0f99beb2a94\":[1,2,3]}}"
  },
  "success": true,
  "requestId": "58091710-5895-4111-A4FF-BEA51550A359"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <success>true</success>
 <plan>{&quot;ssgProfiles&quot;:
[{&quot;name&quot;:&quot;default&quot;,&quot;cpu&quot;:0.2,&quot;heap&quot;:&quot;768 mb&quo t;,&quot;offHeap&quot;:&quot;32 mb&quot;,&quot;managed&quot;:{},&quot;extended&quot;:{}}],&q uot;nodes&quot;: [{&quot;id&quot;:1,&quot;type&quot;:&quot;StreamExecTableSourceScan&quot;,&quot;desc&quot;:&qu ;Source: datahub_table[4]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:2,&quot;type&quot;:&quot;StreamExecCalc&quot;,&quot;desc&quot;:&quot;Calc[5]&q t;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:3,&quot;type&quot;:&quot;StreamExecSink&quot;,&quot;desc&quot;:&quot;Sink: k afka_table[6]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}],&quot;edges&quot;: [{&quot;source&quot;:1,&quot;target&quot;:2,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strat y&quot;:&quot;FORWARD&quot;}, {&quot;source&quot;:2,&quot;target&quot;:3,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strate &quot;:&quot;FORWARD&quot;}],&quot;vertices&quot;: {&quot;717c7b8afebbfb7137f6f0f99beb2a94&quot;:[1,2,3]}}</plan> </data> <success>true</success> <requestId>58091710-5895-4111-A4FF-BEA51550A359</requestId>
```

#### GetCatalog

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatalog HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetCatalogR esponse", "catalog": { "name": "namespaces/flinkte am/catalogs/vvp", "properties": { "defaultDatabase": "default", "type": "vvp" } } } | 详细信息。 |
| requestId | String | 0AFF0B61-35A5- 46D9-930F- 3826DCA3D3F9 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getCatalog HTTP/1.1 &RegionId= &namespace= &workspace= &cat=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "0AFF0B61-35A5-46D9-930F-3826DCA3D3F9",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse",
    "catalog": {
      "name": "namespaces/flinkteam/catalogs/vvp",
      "properties": {
        "defaultDatabase": "default",
        "type": "vvp"
      }
    }
  }
}
```

`XML` 格式

```xml
<requestId>0AFF0B61-35A5-46D9-930F-3826DCA3D3F9</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetCatalogResponse</@type>
 <catalog>
  <name>namespaces/flinkteam/catalogs/vvp</name>
  <properties>
   <defaultDatabase>default</defaultDatabase>
   <type>vvp</type>
  </properties>
 </catalog>
</data>
```

#### GetDefaultDatabase

调用GetDefaultDatabase，获取catalog下默认的database。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefaultDa base HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetDefaultD atabaseResponse", "database": "default" } | 详细信息。 |
| requestId | String | 59F6950E-FC05- 495E-A286- 08C111EC7A4B | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getDefaultDa base HTTP/1.1 &RegionId= &namespace= &workspace= &cat=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "59F6950E-FC05-495E-A286-08C111EC7A4B",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse",
    "database": "default"
  }
}
```

`XML` 格式

```xml
<requestId>59F6950E-FC05-495E-A286-08C111EC7A4B</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetDefaultDatabaseResponse</@type>
 <database>default</database>
</data>
```

#### GetDeploymentDraftById

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

| F | link企业版开 API | 发指南·Ap | pManager |  |  | 实时计算（流计算） |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deploymen tDraftId | String | Path | 是 | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | draft Id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:12:11Z", "resourceVersion": 5, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "comment": "", "modifierName": "flinkadmin", "deployment.draft.r eferenced.deployme nt.id": "d0b3abf0- 4bfe-46b1-a324- 5b7def580c00", "priority": "5" }, "lock": { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:11:40Z", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813" }, "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } }, "id": "c6f157ac-60b9- 4b38-8bad- |  |

实时计算（流计算） API

| 参数名称 | 类型 | d435387cfd59", "示pa例rentId": | 说明 |
|---|---|---|---|
| data | String | "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- ******************** ******************** ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ | draft详细信息。 |
|  |  | (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "versionName": |  |

实时计算（流计算） API

| 参数名称 | 类型 | "vvr-6.0.0-flink- 1示.1例5" }, | 说明 |
|---|---|---|---|
|  |  | "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" } } |  |
| requestId | String | 3EB9FFF4-A3A1- 4B85-89B4- 5987D4551AD9 | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T06:11:40Z",
      "modifiedAt": "2024-03-12T06:12:11Z",
      "resourceVersion": 5,
      "name": "sqljob",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "comment": "",
        "modifierName": "flinkadmin",
        "deployment.draft.referenced.deployment.id": "d0b3abf0-4bfe-46b1-a324-5b7def580c00",
        "priority": "5"
      },
      "lock": {
        "metadata": {
          "createdAt": "2024-03-12T06:11:40Z",
          "modifiedAt": "2024-03-12T06:11:40Z",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813"
          },
          "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
        },
        "apiVersion": "v1",
        "kind": "Lock",
        "spec": {
          "holderName": "flinkadmin",
          "holderId": "229852610122763813"
        }
      },
      "id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
      "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
      "labels": {}
    },
    "apiVersion": "v1",
    "kind": "DeploymentDraft",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
            "flink.queryable-state.enabled": "false"
          }
        },
        "spec": {
          "artifact": {
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATETEMPORARYTABLE`kafkatable`(strnameVARCHAR,lensBIGINT)with(
```

实时计算（流计算） API

```json
tagen\u0027 );CREATE TEMPORARY TABLE kafka_table (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
            "imageUserDefined": false,
            "versionName": "vvr-6.0.0-flink-1.15"
          },
          "parallelism": 1,
          "batchMode": false,
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            },
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            }
          },
          "logging": {
            "log4jLoggers": {
              "": "INFO"
            },
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
            },
            "loggingProfile": "default"
          },
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
          }
        }
      },
      "restoreStrategy": {
        "kind": "LATEST_STATE",
        "allowNonRestoredState": false
      },
      "state": "CANCELLED",
      "upgradeStrategy": {
        "kind": "STATELESS"
      },
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
    }
  },
  "success": true,
  "requestId": "3EB9FFF4-A3A1-4B85-89B4-5987D4551AD9"
}
```

`XML` 格式

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T06:11:40Z</createdAt>
```

实时计算（流计算） API

```xml
  <modifiedAt>2024-03-12T06:12:11Z</modifiedAt>
  <resourceVersion>5</resourceVersion>
  <name>sqljob</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <comment  />
   <modifierName>flinkadmin</modifierName>
   <deployment.draft.referenced.deployment.id>d0b3abf0-4bfe-46b1-a324-
5b7def580c00</deployment.draft.referenced.deployment.id>
   <priority>5</priority>
  </annotations>
  <lock>
   <metadata>
    <createdAt>2024-03-12T06:11:40Z</createdAt>
    <modifiedAt>2024-03-12T06:11:40Z</modifiedAt>
    <namespace>flinkteam</namespace>
    <annotations>
     <creator>229852610122763813</creator>
     <modifier>229852610122763813</modifier>
    </annotations>
    <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
   </metadata>
   <apiVersion>v1</apiVersion>
   <kind>Lock</kind>
   <spec>
    <holderName>flinkadmin</holderName>
    <holderId>229852610122763813</holderId>
   </spec>
  </lock>
  <id>c6f157ac-60b9-4b38-8bad-d435387cfd59</id>
  <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraft</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
  );
```

实时计算（流计算） API

```xml
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
  );
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  datahub_table;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
    <flinkConfiguration>
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>CANCELLED</state>
  <upgradeStrategy>
   <kind>STATELESS</kind>
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
</data> <success>true</success> <requestId>3EB9FFF4-A3A1-4B85-89B4-5987D4551AD9</requestId>
```

实时计算（流计算） API

#### GetDeploymentDraftByName

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/name/[deploymentDraftName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tDraftNam e | String | Path | 是 | sqljob | draft名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": {}, "apiVersion": "v1", "kind": "DeploymentDraftLi st", "items": [ { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:12:11Z", "resourceVersion": 5, "name": "sqljob", "namespace": "flinkteam", "annotations": { |  |

实时计算（流计算） API

|  |  | "creator": |  |
|---|---|---|---|
| 参数名称 | 类型 | "示22例9852610122763 | 说明 |
|  |  | 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "comment": "", "modifierName": "flinkadmin", "deployment.draft.r eferenced.deployme nt.id": "d0b3abf0- 4bfe-46b1-a324- 5b7def580c00", "priority": "5" }, "lock": { "metadata": { "createdAt": "2024- 03-12T06:11:40Z", "modifiedAt": "2024-03- 12T06:11:40Z", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813" }, "id": "ec62ce3c-fe33- 383e-8b31- 2fe9d89af2af" }, "apiVersion": "v1", "kind": "Lock", "spec": { "holderName": "flinkadmin", "holderId": "229852610122763 813" } }, "id": "c6f157ac-60b9- 4b38-8bad- d435387cfd59", "parentId": "99d3a304-a14b- 32da-945c- 765bb687aa61", "labels": {} }, "apiVersion": "v1", "kind": "DeploymentDraft", "spec": { "template": { "metadata": { "annotations": { "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: |  |

实时计算（流计算） API

| 参数名称 data | 类型 String | 2024-03-12 1示4例:11:38 | 说明 draft详细数据。 |
|---|---|---|---|
|  |  | -- Description: Write your description here -- ******************** ******************** ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "versionName": "vvr-6.0.0-flink- 1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { "execution.checkpoi nting.interval": "180s", "execution.checkpoi |  |

实时计算（流计算） API

| 参数名称 | 类型 | nting.min-pause": "示18例0s" } } }, | 说明 |
|---|---|---|---|
|  |  | "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "CANCELLED", "upgradeStrategy": { "kind": "STATELESS" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" } } ] } |  |
| requestId | String | AB731F2D-2B11- 4C4B-A45F- F419ED5CECBF | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/name/[deploymentDraftName] HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftName=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "data": {
    "metadata": {},
    "apiVersion": "v1",
    "kind": "DeploymentDraftList",
    "items": [
      {
        "metadata": {
          "createdAt": "2024-03-12T06:11:40Z",
          "modifiedAt": "2024-03-12T06:12:11Z",
          "resourceVersion": 5,
          "name": "sqljob",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813",
            "creatorName": "flinkadmin",
            "comment": "",
            "modifierName": "flinkadmin",
            "deployment.draft.referenced.deployment.id": "d0b3abf0-4bfe-46b1-a324-
```

实时计算（流计算） API

```json
5b7def580c00",
            "priority": "5"
          },
          "lock": {
            "metadata": {
              "createdAt": "2024-03-12T06:11:40Z",
              "modifiedAt": "2024-03-12T06:11:40Z",
              "namespace": "flinkteam",
              "annotations": {
                "creator": "229852610122763813",
                "modifier": "229852610122763813"
              },
              "id": "ec62ce3c-fe33-383e-8b31-2fe9d89af2af"
            },
            "apiVersion": "v1",
            "kind": "Lock",
            "spec": {
              "holderName": "flinkadmin",
              "holderId": "229852610122763813"
            }
          },
          "id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
          "parentId": "99d3a304-a14b-32da-945c-765bb687aa61",
          "labels": {}
        },
        "apiVersion": "v1",
        "kind": "DeploymentDraft",
        "spec": {
          "template": {
            "metadata": {
              "annotations": {
                "flink.queryable-state.enabled": "false"
              }
            },
            "spec": {
              "artifact": {
                "kind": "SQLSCRIPT",
                "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
                "imageUserDefined": false,
                "versionName": "vvr-6.0.0-flink-1.15"
              },
              "parallelism": 1,
              "batchMode": false,
              "resources": {
                "jobmanager": {
                  "memory": "4Gi",
                  "cpu": 2.0
                },
                "taskmanager": {
```

实时计算（流计算） API

```json
                  "memory": "4Gi",
                  "cpu": 2.0
                }
              },
              "logging": {
                "log4jLoggers": {
                  "": "INFO"
                },
                "logReservePolicy": {
                  "expirationDays": 7,
                  "openHistory": true
                },
                "loggingProfile": "default"
              },
              "flinkConfiguration": {
                "execution.checkpointing.interval": "180s",
                "execution.checkpointing.min-pause": "180s"
              }
            }
          },
          "restoreStrategy": {
            "kind": "LATEST_STATE",
            "allowNonRestoredState": false
          },
          "state": "CANCELLED",
          "upgradeStrategy": {
            "kind": "STATELESS"
          },
          "maxSavepointCreationAttempts": 4,
          "maxJobCreationAttempts": 1,
          "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
        }
      }
```

]

```json
  },
  "success": true,
  "requestId": "AB731F2D-2B11-4C4B-A45F-F419ED5CECBF"
}
```

`XML` 格式

```xml
<data>
 <metadata  />
 <apiVersion>v1</apiVersion>
 <kind>DeploymentDraftList</kind>
 <items>
  <metadata>
   <createdAt>2024-03-12T06:11:40Z</createdAt>
   <modifiedAt>2024-03-12T06:12:11Z</modifiedAt>
   <resourceVersion>5</resourceVersion>
   <name>sqljob</name>
   <namespace>flinkteam</namespace>
   <annotations>
    <creator>229852610122763813</creator>
    <modifier>229852610122763813</modifier>
    <creatorName>flinkadmin</creatorName>
```

/ 实时计算（流计算） API

```xml
    <comment  />
    <modifierName>flinkadmin</modifierName>
    <deployment.draft.referenced.deployment.id>d0b3abf0-4bfe-46b1-a324-
5b7def580c00</deployment.draft.referenced.deployment.id>
    <priority>5</priority>
   </annotations>
   <lock>
    <metadata>
     <createdAt>2024-03-12T06:11:40Z</createdAt>
     <modifiedAt>2024-03-12T06:11:40Z</modifiedAt>
     <namespace>flinkteam</namespace>
     <annotations>
      <creator>229852610122763813</creator>
      <modifier>229852610122763813</modifier>
     </annotations>
     <id>ec62ce3c-fe33-383e-8b31-2fe9d89af2af</id>
    </metadata>
    <apiVersion>v1</apiVersion>
    <kind>Lock</kind>
    <spec>
     <holderName>flinkadmin</holderName>
     <holderId>229852610122763813</holderId>
    </spec>
   </lock>
   <id>c6f157ac-60b9-4b38-8bad-d435387cfd59</id>
   <parentId>99d3a304-a14b-32da-945c-765bb687aa61</parentId>
   <labels  />
  </metadata>
  <apiVersion>v1</apiVersion>
  <kind>DeploymentDraft</kind>
  <spec>
   <template>
    <metadata>
     <annotations>
      <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
     </annotations>
    </metadata>
    <spec>
     <artifact>
      <kind>SQLSCRIPT</kind>
      <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************-- CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
  );
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
  );
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens
```

实时计算（流计算） API

```xml
FROM
  datahub_table;
      </sqlScript>
      <imageUserDefined>false</imageUserDefined>
      <versionName>vvr-6.0.0-flink-1.15</versionName>
     </artifact>
     <parallelism>1</parallelism>
     <batchMode>false</batchMode>
     <resources>
      <jobmanager>
       <memory>4Gi</memory>
       <cpu>2</cpu>
      </jobmanager>
      <taskmanager>
       <memory>4Gi</memory>
       <cpu>2</cpu>
      </taskmanager>
     </resources>
     <logging>
      <log4jLoggers>
       <>INFO</>
      </log4jLoggers>
      <logReservePolicy>
       <expirationDays>7</expirationDays>
       <openHistory>true</openHistory>
      </logReservePolicy>
      <loggingProfile>default</loggingProfile>
     </logging>
     <flinkConfiguration>
      <execution.checkpointing.interval>180s</execution.checkpointing.interval>
      <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
     </flinkConfiguration>
    </spec>
   </template>
   <restoreStrategy>
    <kind>LATEST_STATE</kind>
    <allowNonRestoredState>false</allowNonRestoredState>
   </restoreStrategy>
   <state>CANCELLED</state>
   <upgradeStrategy>
    <kind>STATELESS</kind>
   </upgradeStrategy>
   <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
   <maxJobCreationAttempts>1</maxJobCreationAttempts>
   <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
  </spec>
 </items>
</data> <success>true</success> <requestId>AB731F2D-2B11-4C4B-A45F-F419ED5CECBF</requestId>
```

#### GetDeploymentDraftResourcePlan

调用GetDeploymentDraftResourcePlan，获取draft资源配置计划。

**请求头**

实时计算（流计算） API 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/resource_plan HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tDraftId | String | Path | 是 | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | draft ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "success": true, "message": "", "plan": "" } | 资源配置详细信息。 |
| requestId | String | 49D8D2CA-51A8- 43FE-820A- F44970A83159 | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deploymentdrafts/[deploymentDraftId]/resource_plan HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentDraftId=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "success": true,
    "message": "",
    "plan": ""
  },
  "success": true,
  "requestId": "49D8D2CA-51A8-43FE-820A-F44970A83159"
}
```

`XML` 格式

```xml
<data>
 <success>true</success>
 <message  />
 <plan  />
</data> <success>true</success> <requestId>49D8D2CA-51A8-43FE-820A-F44970A83159</requestId>
```

**3.1.48.**

#### GetDeploymentDraftResourcePlanWithBestEffort

调用GetDeploymentDraftResourcePlanWithBestEffort，获取资源配置计划。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployment DraftId]/resource_plan:best-effort-merge HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

|  |  |  |  | Flink企 | 业版开发指南·AppManager |
|---|---|---|---|---|---|

API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deploymen tDraftId | String | Path | 是 | c6f157ac-60b9-4b38- 8bad-d435387cfd59 | draft ID。 |
| deploymen tId | String | Query | 否 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | deployment ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "success": true, "plan": " {\"ssgProfiles\": [{\"name\":\"default \",\"cpu\":0.2,\"heap\ ":\"768 mb\",\"offHeap\":\"3 2 mb\",\"managed\": {},\"extended\": {}}],\"nodes\": [{\"id\":1,\"type\":\"S treamExecTableSou rceScan\",\"desc\":\" Source: datahub table[11]\", _ \"profile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":2,\"type\":\"St reamExecCalc\",\"de sc\":\"Calc[12]\",\"pr ofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}, {\"id\":3,\"type\":\"St reamExecSink\",\"de sc\":\"Sink: kafka table[13]\",\"p _ rofile\": {\"group\":\"default\ ",\"parallelism\":1,\" maxParallelism\":32 768,\"minParallelism \":1}}],\"edges\": [{\"source\":1,\"targ et\":2,\"mode\":\"PIP ELINED\",\"strategy\ ":\"FORWARD\"}, {\"source\":2,\"targe t\":3,\"mode\":\"PIPE LINED\",\"strategy\": \"FORWARD\"}],\"ve rtices\": {\"717c7b8afebbfb7 137f6f0f99beb2a94\ ":[1,2,3]}}" } | 资源配置详细数据。 |
| requestId | String | 3B46A3C8-2D6A- 4DE6-8468- E6A72E7E5FE8 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
POST /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployment-drafts/[deployment DraftId]/resource_plan:best-effort-merge HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"", "deploymentDraftId":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "success": true,
    "plan": "{\"ssgProfiles\":[{\"name\":\"default\",\"cpu\":0.2,\"heap\":\"768 mb\",\"offHe
ap\":\"32 mb\",\"managed\":{},\"extended\":{}}],\"nodes\": [{\"id\":1,\"type\":\"StreamExecTableSourceScan\",\"desc\":\"Source: datahub_table[11]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":2,\"type\":\"StreamExecCalc\",\"desc\":\"Calc[12]\",\"profile\": {\"group\":\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}},{\" id\":3,\"type\":\"StreamExecSink\",\"desc\":\"Sink: kafka_table[13]\",\"profile\":{\"group\" :\"default\",\"parallelism\":1,\"maxParallelism\":32768,\"minParallelism\":1}}],\"edges\":[{ \"source\":1,\"target\":2,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"},{\"source\":2,\"t arget\":3,\"mode\":\"PIPELINED\",\"strategy\":\"FORWARD\"}],\"vertices\":{\"717c7b8afebbfb71 37f6f0f99beb2a94\":[1,2,3]}}"
  },
  "success": true,
  "requestId": "3B46A3C8-2D6A-4DE6-8468-E6A72E7E5FE8"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <success>true</success>
 <plan>{&quot;ssgProfiles&quot;:
[{&quot;name&quot;:&quot;default&quot;,&quot;cpu&quot;:0.2,&quot;heap&quot;:&quot;768 mb&quo t;,&quot;offHeap&quot;:&quot;32 mb&quot;,&quot;managed&quot;:{},&quot;extended&quot;:{}}],&q uot;nodes&quot;: [{&quot;id&quot;:1,&quot;type&quot;:&quot;StreamExecTableSourceScan&quot;,&quot;desc&quot;:&qu ;Source: datahub_table[11]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:2,&quot;type&quot;:&quot;StreamExecCalc&quot;,&quot;desc&quot;:&quot;Calc[12]& ot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}, {&quot;id&quot;:3,&quot;type&quot;:&quot;StreamExecSink&quot;,&quot;desc&quot;:&quot;Sink: k afka_table[13]&quot;,&quot;profile&quot;: {&quot;group&quot;:&quot;default&quot;,&quot;parallelism&quot;:1,&quot;maxParallelism&quot;:32 8,&quot;minParallelism&quot;:1}}],&quot;edges&quot;: [{&quot;source&quot;:1,&quot;target&quot;:2,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strat y&quot;:&quot;FORWARD&quot;}, {&quot;source&quot;:2,&quot;target&quot;:3,&quot;mode&quot;:&quot;PIPELINED&quot;,&quot;strate &quot;:&quot;FORWARD&quot;}],&quot;vertices&quot;: {&quot;717c7b8afebbfb7137f6f0f99beb2a94&quot;:[1,2,3]}}</plan> </data> <success>true</success> <requestId>3B46A3C8-2D6A-4DE6-8468-E6A72E7E5FE8</requestId>
```

#### GetFunction

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunction HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| function | String | Query | 是 | TransformUdtf | function名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetFunction Response", "function": { "name": "TransformUdtf", "className": "com.alibaba.blink.u dtf.TransformUdtf", "functionLanguage": "FUNCTION LANGUA _ GE JAVA", _ "functionType": "FUNCTION TYPE FL _ _ INK", "description": "This is a user- defined function" }, "success": true, "message": "" } | 详细信息。 |
| requestId | String | DD2A9970-CED3- 4AD6-B0F6- 8DFDD84AC6AC | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例实时计算（流计算） API

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getFunction HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &function=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "requestId": "DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse",
    "function": {
      "name": "TransformUdtf",
      "className": "com.alibaba.blink.udtf.TransformUdtf",
      "functionLanguage": "FUNCTION_LANGUAGE_JAVA",
      "functionType": "FUNCTION_TYPE_FLINK",
      "description": "This is a user-defined function"
    },
    "success": true,
    "message": ""
  }
}
```

`XML` 格式

```xml
<requestId>DD2A9970-CED3-4AD6-B0F6-8DFDD84AC6AC</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetFunctionResponse</@type>
 <function>
  <name>TransformUdtf</name>
  <className>com.alibaba.blink.udtf.TransformUdtf</className>
  <functionLanguage>FUNCTION_LANGUAGE_JAVA</functionLanguage>
  <functionType>FUNCTION_TYPE_FLINK</functionType>
  <description>This is a user-defined function</description>
 </function>
 <success>true</success>
 <message  />
</data>
```

实时计算（流计算） API

#### GetResourcePlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业deploymentId。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "success": true, "message": "", "plan": "" } | 作业资源配置计划详细信息。 |
| requestId | String | 87589423-CE39- 470D-81EA- 5AB477CF4CD4 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/resource_ an HTTP/1.1 &RegionId= &workspace= &namespace= &deploymentId=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "data": {
    "success": true,
    "message": "",
    "plan": ""
  },
  "success": true,
  "requestId": "87589423-CE39-470D-81EA-5AB477CF4CD4"
}
```

`XML` 格式

```xml
<data>
 <success>true</success>
 <message  />
 <plan  />
</data> <success>true</success> <requestId>87589423-CE39-470D-81EA-5AB477CF4CD4</requestId>
```

#### GetTable

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable H TTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

|  |  |  |  | Flink企 | 业版开发指南·AppManager |
|---|---|---|---|---|---|

API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| table | String | Query | 是 | mydatahub | table名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.GetTableRes ponse", "table": { "name": "mydatahub", "schema": { "column": [ { "name": "strname", "type": "VARCHAR(2147483 647)", "expression": "" } ], "watermarkSpec": [] }, "properties": { "accessId": "SVw******PtL", "endpoint": "https://datahub.cn- wulan-env188- d01.dh.inter.env188 .shuguang.com", "connector": "datahub", "accessKey": "RfE******VMB", "project": "datahub", "topic": "mysource" }, "comment": "" }, "success": true, "message": "" } | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | FCB6D11E-8FAA- 48F7-8E25- 28218A6878F5 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:getTable H TTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &table=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "FCB6D11E-8FAA-48F7-8E25-28218A6878F5",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse",
    "table": {
      "name": "mydatahub",
      "schema": {
        "column": [
          {
            "name": "strname",
            "type": "VARCHAR(2147483647)",
            "expression": ""
          }
```

`],`

```json
      },
      "properties": {
        "accessId": "SVw******PtL",
        "endpoint": "https://datahub.cn-wulan-env188-d01.dh.inter.env188.shuguang.com",
        "connector": "datahub",
        "accessKey": "RfE******VMB",
        "project": "datahub",
        "topic": "mysource"
      },
      "comment": ""
    },
    "success": true,
    "message": ""
  }
}
```

`XML` 格式实时计算（流计算） API

```xml
<requestId>FCB6D11E-8FAA-48F7-8E25-28218A6878F5</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.GetTableResponse</@type>
 <table>
  <name>mydatahub</name>
  <schema>
   <column>
    <name>strname</name>
    <type>VARCHAR(2147483647)</type>
    <expression  />
   </column>
  </schema>
  <properties>
   <accessId>SVw******PtL</accessId>
   <endpoint>https://datahub.cn-wulan-env188-d01.dh.inter.env188.shuguang.com</endpoint>
   <connector>datahub</connector>
   <accessKey>RfE******VMB</accessKey>
   <project>datahub</project>
   <topic>mysource</topic>
  </properties>
  <comment  />
 </table>
 <success>true</success>
 <message  />
</data>
```

#### GetUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| requireFun ctionName s | Boole an | Query | 是 | true | 是否返回funtion名称信息。 |

| 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager AP |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.v1beta1.G etUdfArtifactRespon se", "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [ "TimestampProbe" ], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [ "TransformUdtf" ], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "223474909869445 380", "jarUpdateTime": "2024-03- 08T08:13:57Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "namespace": "namespaces/flinkte am", "jarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/udfs/met ric-transform-227- shaded/2024-03- 08T08-13- 54.732313Z/metric- transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T08:13:57Z" } } | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C44A1880-5138- 4204-9165- DC65C4B059C2 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1 &RegionId= &requireFunctionNames= &workspace= &namespace= &udfArtifactName=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "@type": "type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse",
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
        {
          "functionNames": [
            "TimestampProbe"
```

`],`

```json
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

,

```json
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
        },
        {
          "functionNames": [
            "TransformUdtf"
```

`],`

```json
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

,

```json
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
        }
```

`],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-08T08:13:54Z",
      "uploader": "223474909869445380",
      "jarUpdateTime": "2024-03-08T08:13:57Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded",
      "namespace": "namespaces/flinkteam",
      "jarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-2
27-shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-08T08:13:57Z"
    }
  },
  "requestId": "C44A1880-5138-4204-9165-DC65C4B059C2",
  "success": true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <@type>type.googleapis.com/vvp.sql.v1beta1.GetUdfArtifactResponse</@type>
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames>TimestampProbe</functionNames>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames>TransformUdtf</functionNames>
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-08T08:13:54Z</createTime>
  <uploader>223474909869445380</uploader>
  <jarUpdateTime>2024-03-08T08:13:57Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</name>
  <namespace>namespaces/flinkteam</namespace>
  <jarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-
shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-08T08:13:57Z</updateTime>
 </udfArtifact>
</data> <requestId>C44A1880-5138-4204-9165-DC65C4B059C2</requestId> <success>true</success>
```

#### ListConnectors

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "connectors": [ { "lookup": false, "supportedFormats" : [], "environments": [ "PUBLIC CLOUD", _ "PRIVATE CLOUD", _ "ALIBABA GROUP", _ "VVC CLOUD" ], _ "sink": false, "name": "namespaces/flinkte am/connectors/data gen", "source": true, "type": "datagen", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027datagen\u00 27 to configure this connector.", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "Rows per second to control the emit rate, default 10000L.", "definesFormat": false, "key": "rows- per-second", "required": false }, { "defaultValue": "", "description": "Total number of rows to emit. By default, the source is unbounded.", "definesFormat": false, "key": "number-of-rows", "required": false } ], "packaged": true, "dependencies": [] } ], "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istConnectorsRespo nse" } | 详细数据。 |
| requestId | String | A62F262E-3055- 490B-B17B- 0C6BF83C4BE6 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```
GET /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors HTTP/1.1 &RegionId= &workspace= &namespace=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "connectors": [
      {
        "lookup": false,
        "supportedFormats": [],
        "environments": [
          "PUBLIC_CLOUD",
          "PRIVATE_CLOUD",
          "ALIBABA_GROUP",
          "VVC_CLOUD"
```

`],`

```json
        "sink": false,
        "name": "namespaces/flinkteam/connectors/datagen",
        "source": true,
        "type": "datagen",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027datagen\u0027 to configure this
connector.",
            "definesFormat": false,
            "key": "connector",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Rows per second to control the emit rate, default 10000L.",
            "definesFormat": false,
            "key": "rows-per-second",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Total number of rows to emit. By default, the source is unbounde
d.",
            "definesFormat": false,
            "key": "number-of-rows",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": []
      }
```

`],`

```json
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse"
  },
  "success": true,
  "requestId": "A62F262E-3055-490B-B17B-0C6BF83C4BE6"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <connectors>
  <lookup>false</lookup>
  <supportedFormats  />
  <environments>PUBLIC_CLOUD</environments>
  <environments>PRIVATE_CLOUD</environments>
  <environments>ALIBABA_GROUP</environments>
  <environments>VVC_CLOUD</environments>
  <sink>false</sink>
  <name>namespaces/flinkteam/connectors/datagen</name>
  <source>true</source>
  <type>datagen</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;datagen&#x27; to configure this connector.</description
```

>

```xml
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Rows per second to control the emit rate, default 10000L.</description>
   <definesFormat>false</definesFormat>
   <key>rows-per-second</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Total number of rows to emit. By default, the source is unbounded.</descript
ion>
   <definesFormat>false</definesFormat>
   <key>number-of-rows</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies  />
 </connectors>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListConnectorsResponse</@type>
</data> <success>true</success> <requestId>A62F262E-3055-490B-B17B-0C6BF83C4BE6</requestId>
```

#### ListDatabases

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDatabase HTTP/1.1
```

实时计算（流计算） API

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces 获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.ListDatabase sResponse", "databases": [ { "name": "default", "properties": {}, "comment": "The default database" } ] } | 详细信息。 |
| requestId | String | 76F325D7-3EC4- 4E34-81A8- 18B92D7EE606 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:listDatabase HTTP/1.1
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "requestId": "76F325D7-3EC4-4E34-81A8-18B92D7EE606",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse",
    "databases": [{
      "name": "default",
      "properties": {
      },
      "comment": "The default database"
    }]
  }
}
```

`XML` 格式

```xml
<requestId>76F325D7-3EC4-4E34-81A8-18B92D7EE606</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.ListDatabasesResponse</@type>
 <databases>
  <name>default</name>
  <properties  />
  <comment>The default database</comment>
 </databases>
</data>
```

#### ListFlinkVersions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
|  |  | { "defaultFlinkVersion Name": "vvr-6.0.0- flink-1.15", "flinkVersionMetada tas": [ { "supportFindUsedCa talogs": false, "useForJarFineGrain ed": false, "versionName": "vvr-3.0.9-flink- 1.12", "flinkVersion": "1.12", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": false, "supportDynamicLo gLevel": false, "supportDagExpansi on": false, "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": false, "supportNativeK8s": false, "supportJvmDebug": false, "supportLogArchive" : false, "useForSqlDeploym ents": true, "supportLogPaging": false }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-3.0.9- flink-1.12/vvr-3.0.9- flink-1.12- dist.tar.gz", "supportStateComp atibility": false, "defaultFor": [], |  |

实时计算（流计算） API

| 参数名称 | 类型 | "imageTag": 示例 "1.12.0-vvr-3.0.9- | 说明 |
|---|---|---|---|
| data | String | 1109", "vvrVersion": "3.0.9", "status": "DEPRECATED" }, { "supportFindUsedCa talogs": true, "useForJarFineGrain ed": false, "versionName": "vvr-4.0.18-flink- 1.13", "flinkVersion": "1.13", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": true, "supportDynamicLo gLevel": true, "supportDagExpansi on": false, "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": true, "supportNativeK8s": false, "supportJvmDebug": true, "supportLogArchive" : true, | 详细信息。 |
|  |  | "useForSqlDeploym ents": true, "supportLogPaging": true }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-4.0.18- flink-1.13/vvr- 4.0.18-flink-1.13- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.13.0-vvr-4.0.18- 22", "vvrVersion": "4.0.18", "status": "DEPRECATED" }, { "supportFindUsedCa talogs": true, "useForJarFineGrain ed": false, "versionName": "vvr-6.0.0-flink- 1.15", "flinkVersion": "1.15", "useForSqlDeploym ents": true, "labels": {}, "features": { "supportFindUsedCa talogs": true, "supportDynamicLo L l" |  |

实时计算（流计算） API

| 参数名称 | 类型 | gLevel": true, "示su例pportDagExpansi on": false, | 说明 |
|---|---|---|---|
|  |  | "useForJarFineGrain ed": false, "supportNativeSave point": false, "supportStateComp atibility": true, "supportNativeK8s": false, "supportJvmDebug": true, "supportLogArchive" : true, "useForSqlDeploym ents": true, "supportLogPaging": true }, "tarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/default/packaged- vvr-dist/vvr-6.0.7- flink-1.15/vvr-6.0.7- flink-1.15- dist.tar.gz", "supportStateComp atibility": true, "defaultFor": [], "imageTag": "1.15.0-vvr-6.0.7- 29", "vvrVersion": "6.0.7", "status": "STABLE" } ] } |  |
| requestId | String | 63269B06-8027- 4CD0-9AB5- D9791B185B82 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/flink-version-meta.json HTTP/1.1 &RegionId= &workspace=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "data": {
    "defaultFlinkVersionName": "vvr-6.0.0-flink-1.15",
    "flinkVersionMetadatas": [
      {
        "supportFindUsedCatalogs": false,
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
```

实时计算（流计算） API

```json
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": false,
          "supportLogPaging": false
        },
        "useForJarFineGrained": false,
        "supportStateCompatibility": false,
        "defaultFor": [],
        "versionName": "vvr-1.0.8-flink-1.10",
        "imageTag": "1.10.0-vvr-1.0.8-1",
        "flinkVersion": "1.10",
        "vvrVersion": "1.0.8",
        "useForSqlDeployments": false,
        "status": "DEPRECATED",
        "labels": {}
      },
      {
        "supportFindUsedCatalogs": false,
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": false,
          "supportLogPaging": false
        },
        "useForJarFineGrained": false,
        "supportStateCompatibility": false,
        "defaultFor": [],
        "versionName": "vvr-2.1.10-flink-1.11",
        "imageTag": "1.11.0-vvr-2.1.10-1151",
        "flinkVersion": "1.11",
        "vvrVersion": "2.1.10",
        "useForSqlDeployments": false,
        "status": "DEPRECATED",
        "labels": {}
      },
      {
        "supportFindUsedCatalogs": false,
        "useForJarFineGrained": false,
        "versionName": "vvr-3.0.9-flink-1.12",
        "flinkVersion": "1.12",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": false,
          "supportDynamicLogLevel": false,
```

实时计算（流计算） API

```json
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": false,
          "supportNativeK8s": false,
          "supportJvmDebug": false,
          "supportLogArchive": false,
          "useForSqlDeployments": true,
          "supportLogPaging": false
        },
        "tarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3
.0.9-flink-1.12/vvr-3.0.9-flink-1.12-dist.tar.gz",
        "supportStateCompatibility": false,
        "defaultFor": [],
        "imageTag": "1.12.0-vvr-3.0.9-1109",
        "vvrVersion": "3.0.9",
        "status": "DEPRECATED"
      },
      {
        "supportFindUsedCatalogs": true,
        "useForJarFineGrained": false,
        "versionName": "vvr-4.0.18-flink-1.13",
        "flinkVersion": "1.13",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": true,
          "supportDynamicLogLevel": true,
          "supportDagExpansion": false,
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": true,
          "supportNativeK8s": false,
          "supportJvmDebug": true,
          "supportLogArchive": true,
          "useForSqlDeployments": true,
          "supportLogPaging": true
        },
        "tarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4
.0.18-flink-1.13/vvr-4.0.18-flink-1.13-dist.tar.gz",
        "supportStateCompatibility": true,
        "defaultFor": [],
        "imageTag": "1.13.0-vvr-4.0.18-22",
        "vvrVersion": "4.0.18",
        "status": "DEPRECATED"
      },
      {
        "supportFindUsedCatalogs": true,
        "useForJarFineGrained": false,
        "versionName": "vvr-6.0.0-flink-1.15",
        "flinkVersion": "1.15",
        "useForSqlDeployments": true,
        "labels": {},
        "features": {
          "supportFindUsedCatalogs": true,
          "supportDynamicLogLevel": true,
          "supportDagExpansion": false,
```

实时计算（流计算） API `pp` g p ,

```json
          "useForJarFineGrained": false,
          "supportNativeSavepoint": false,
          "supportStateCompatibility": true,
          "supportNativeK8s": false,
          "supportJvmDebug": true,
          "supportLogArchive": true,
          "useForSqlDeployments": true,
          "supportLogPaging": true
        },
        "tarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6
.0.7-flink-1.15/vvr-6.0.7-flink-1.15-dist.tar.gz",
        "supportStateCompatibility": true,
        "defaultFor": [],
        "imageTag": "1.15.0-vvr-6.0.7-29",
        "vvrVersion": "6.0.7",
        "status": "STABLE"
      }
```

]

```json
  },
  "requestId": "63269B06-8027-4CD0-9AB5-D9791B185B82",
  "success": true
}
```

`XML` 格式

```xml
<data>
 <defaultFlinkVersionName>vvr-6.0.0-flink-1.15</defaultFlinkVersionName>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <features>
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>false</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <useForJarFineGrained>false</useForJarFineGrained>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <versionName>vvr-1.0.8-flink-1.10</versionName>
  <imageTag>1.10.0-vvr-1.0.8-1</imageTag>
  <flinkVersion>1.10</flinkVersion>
  <vvrVersion>1.0.8</vvrVersion>
  <useForSqlDeployments>false</useForSqlDeployments>
  <status>DEPRECATED</status>
  <labels  />
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <features>
```

实时计算（流计算） API

```xml
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>false</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <useForJarFineGrained>false</useForJarFineGrained>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <versionName>vvr-2.1.10-flink-1.11</versionName>
  <imageTag>1.11.0-vvr-2.1.10-1151</imageTag>
  <flinkVersion>1.11</flinkVersion>
  <vvrVersion>2.1.10</vvrVersion>
  <useForSqlDeployments>false</useForSqlDeployments>
  <status>DEPRECATED</status>
  <labels  />
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-3.0.9-flink-1.12</versionName>
  <flinkVersion>1.12</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
  <labels  />
  <features>
   <supportFindUsedCatalogs>false</supportFindUsedCatalogs>
   <supportDynamicLogLevel>false</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>false</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>false</supportJvmDebug>
   <supportLogArchive>false</supportLogArchive>
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>false</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-3.0.9-
flink-1.12/vvr-3.0.9-flink-1.12-dist.tar.gz</tarUrl>
  <supportStateCompatibility>false</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.12.0-vvr-3.0.9-1109</imageTag>
  <vvrVersion>3.0.9</vvrVersion>
  <status>DEPRECATED</status>
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-4.0.18-flink-1.13</versionName>
  <flinkVersion>1.13</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
```

实时计算（流计算） API

```xml
  <labels  />
  <features>
   <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
   <supportDynamicLogLevel>true</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>true</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>true</supportJvmDebug>
   <supportLogArchive>true</supportLogArchive>
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>true</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-4.0.18-
flink-1.13/vvr-4.0.18-flink-1.13-dist.tar.gz</tarUrl>
  <supportStateCompatibility>true</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.13.0-vvr-4.0.18-22</imageTag>
  <vvrVersion>4.0.18</vvrVersion>
  <status>DEPRECATED</status>
 </flinkVersionMetadatas>
 <flinkVersionMetadatas>
  <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
  <useForJarFineGrained>false</useForJarFineGrained>
  <versionName>vvr-6.0.0-flink-1.15</versionName>
  <flinkVersion>1.15</flinkVersion>
  <useForSqlDeployments>true</useForSqlDeployments>
  <labels  />
  <features>
   <supportFindUsedCatalogs>true</supportFindUsedCatalogs>
   <supportDynamicLogLevel>true</supportDynamicLogLevel>
   <supportDagExpansion>false</supportDagExpansion>
   <useForJarFineGrained>false</useForJarFineGrained>
   <supportNativeSavepoint>false</supportNativeSavepoint>
   <supportStateCompatibility>true</supportStateCompatibility>
   <supportNativeK8s>false</supportNativeK8s>
   <supportJvmDebug>true</supportJvmDebug>
   <supportLogArchive>true</supportLogArchive>
   <useForSqlDeployments>true</useForSqlDeployments>
   <supportLogPaging>true</supportLogPaging>
  </features>
  <tarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/default/packaged-vvr-dist/vvr-6.0.7-
flink-1.15/vvr-6.0.7-flink-1.15-dist.tar.gz</tarUrl>
  <supportStateCompatibility>true</supportStateCompatibility>
  <defaultFor  />
  <imageTag>1.15.0-vvr-6.0.7-29</imageTag>
  <vvrVersion>6.0.7</vvrVersion>
  <status>STABLE</status>
 </flinkVersionMetadatas>
</data> <requestId>63269B06-8027-4CD0-9AB5-D9791B185B82</requestId> <success>true</success>
```

#### ListFormats

实时计算（流计算） API

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | myudf | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "formats": [ { "sink": true, "name": "namespaces/flinkte am/formats/avro", "source": true, "type": "avro", "properties": [ { "defaultValue": "", "description": "Must be set to \u0027avro\u0027 to configure this format.", "definesFormat": false, "key": "format", "required": true } ], "packaged": true, "dependencies": [ "hdfs:///vvp/data/sql - artifacts/namespace s/ververica/connect ors/vvr-6.0.7-flink- 1.15/opt/formats/avr o/flink-sql-avro-1.15- vvr-6.0.7- SNAPSHOT.jar" ] } ], "@type": "type.googleapis.co m/vvp.sql.v1beta1.L istFormatsResponse " } | 详细信息。 |
| requestId | String | 6BFF2035-B5FB- 4E1A-8F32- 4CA636417A3D | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
/pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "formats": [
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/avro",
        "source": true,
        "type": "avro",
```

实时计算（流计算） API

```json
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027avro\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/avro-confluent",
        "source": true,
        "type": "avro-confluent",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027avro-confluent\u0027 to configure this form
at.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "The URL of the Confluent Schema Registry to fetch/register schem
as.",
            "definesFormat": false,
            "key": "schema-registry.url",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "The Confluent Schema Registry subject under which to register th
e schema used by this format during serialization. Required for sink table.",
            "definesFormat": false,
            "key": "schema-registry.subject",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/canal-json",
        "source": true,
```

实时计算（流计算） API

```json
        "type": "canal-json",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027canal-json\u0027 to configure this
format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
            "key": "fast-deserialization",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Only read changelog rows which match the specific database (by c
omparing the \"database\" meta field in the record).",
            "definesFormat": false,
            "key": "database.include",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Only read changelog rows which match the specific table (by comp
aring the \"table\" meta field in the record).",
            "definesFormat": false,
            "key": "table.include",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

实时计算（流计算） API ]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/csv",
        "source": true,
        "type": "csv",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027csv\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Optional field delimiter character (\u0027,\u0027 by default).",
            "definesFormat": false,
            "key": "field-delimiter",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to disabled quote character for enclosing field va
lues (false by default). If true, quote-character can not be set.",
            "definesFormat": false,
            "key": "disable-quote-character",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional quote character for enclosing field values
(\u0027\"\u0027 by default).",
            "definesFormat": false,
            "key": "quote-character",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to ignore comment lines that start with
\u0027#\u0027(disabled by default); if enabled, make sure to also ignore parse errors to allow empty rows.",
            "definesFormat": false,
            "key": "allow-comments",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
          },
          {
            "defaultValue": "",
```

实时计算（流计算） API

```json
            "description": "Optional array element delimiter string for separating array and
row element values (\u0027;\u0027 by default).",
            "definesFormat": false,
            "key": "array-element-delimiter",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional escape character for escaping values (disabled by defau
lt).",
            "definesFormat": false,
            "key": "escape-character",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional null literal string that is interpreted as a null value
(disabled by default).",
            "definesFormat": false,
            "key": "null-literal",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/csv/flink-csv-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/debezium-avro-confluent",
        "source": true,
        "type": "debezium-avro-confluent",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027debezium-avro-confluent\u0027 to configure
this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "The URL of the Confluent Schema Registry to fetch/register schem
as.",
            "definesFormat": false,
            "key": "url",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Basic auth credentials source for Schema Registry.",
            "definesFormat": false,
            "key": "basic-auth.credentials-source",
            "required": false
```

实时计算（流计算） API

```json
          },
          {
            "defaultValue": "",
            "description": "Basic auth user info for schema registry.",
            "definesFormat": false,
            "key": "basic-auth.user-info",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Bearer auth credentials source for Schema Registry.",
            "definesFormat": false,
            "key": "bearer-auth.credentials-source",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Bearer auth token for Schema Registry.",
            "definesFormat": false,
            "key": "bearer-auth.token",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Properties map that is forwarded to the underlying Schema Regist
ry. This is useful for options that are not officially exposed via Flink config options. However, note that Flink options have higher precedence.",
            "definesFormat": false,
            "key": "properties",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Location / File of SSL keystore.",
            "definesFormat": false,
            "key": "ssl.keystore.location",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Password for SSL keystore",
            "definesFormat": false,
            "key": "ssl.keystore.password",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Location / File of SSL truststore.",
            "definesFormat": false,
            "key": "ssl.truststore.location",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Password for SSL truststore.",
            "definesFormat": false,
            "key": "ssl.truststore.password",
```

实时计算（流计算） API y p ,

```json
            "required": false
          },
          {
            "defaultValue": "",
            "description": "The Confluent Schema Registry subject under which to register th
e schema used by this format during serialization. By default, \u0027kafka\u0027 and \u0027upsert-kafka\u0027 connectors use \u0027\u003ctopic_name\u003e-value\u0027 or \u0027\u 003ctopic_name\u003e-key\u0027 as the default subject name if this format is used as the value or key format. But for other connectors (e.g. \u0027filesystem\u0027), the subject option is required when used as sink.",
            "definesFormat": false,
            "key": "subject",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/debezium-json",
        "source": true,
        "type": "debezium-json",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027debezium-json\u0027 to configure this forma
t.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "When setting up a Debezium Kafka Connect, users can enable a Kaf
ka configuration \u0027value.converter.schemas.enable\u0027 to include schema in the message . This option indicates the Debezium JSON data include the schema in the message or not. Default is false.",
            "definesFormat": false,
            "key": "schema-include",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing; fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
          },
          {
            "defaultValue": "",
"description":"OptionalflagtouseJacksonStreamAPItodeserializejsonobje
```

实时计算（流计算） API

```json
            description: Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
            "key": "fast-deserialization",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/json",
        "source": true,
        "type": "json",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027json\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Optional flag to specify whether to fail if a field is missing o
r not, false by default.",
            "definesFormat": false,
            "key": "fail-on-missing-field",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to skip fields and rows with parse errors instead
of failing. Fields are set to null in case of errors, false by default.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to use Jackson Stream API to deserialize json obje
ct, which brings 30% performance gain.",
            "definesFormat": false,
"key":"fast-deserialization"
```

实时计算（流计算） API

```json
            key: fastdeserialization,
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to specify timestamp format, SQL by default. Optio
n ISO-8601 will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format and out put timestamp in the same format. Option SQL will parse input timestamp in \"yyyy-MM-dd HH:m m:ss.s{precision}\" format and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to recursively flatten the JSON OBJECT field into
columns in the top level schema. For a better understanding, the name of the flattened column will be composed of the path to get the column. For example, the field `col` in the json \"{ \\\"nested\\\": {\\\"col\\\": true} }\" is `nested.col` in the flattened schema. If the flattened field names get conflicts, currently the JsonParser will throw the exception t o stop the execution. Please use the option \"json.ignore-parse-errors\" to ignore the parse errors.",
            "definesFormat": false,
            "key": "infer-schema.flatten-nested-columns.enable",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Optional flag to infer primitive types as string type.",
            "definesFormat": false,
            "key": "infer-schema.primitive-as-string",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/maxwell-json",
        "source": true,
        "type": "maxwell-json",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027maxwell-json\u0027 to configure this format
.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Skip fields and rows with parse errors instead of failing. Field
saresettonullincaseoferrors"
```

实时计算（流计算） API

```json
s are set to null in case of errors.",
            "definesFormat": false,
            "key": "ignore-parse-errors",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Specify the input and output timestamp format. Currently support
ed values are \u0027SQL\u0027 and \u0027ISO-8601\u0027. Option \u0027SQL\u0027 will parse in put timestamp in \"yyyy-MM-dd HH:mm:ss.s{precision}\" format, e.g \u00272020-12-30 12:13:14. 123\u0027 and output timestamp in the same format. Option \u0027ISO-8601\u0027will parse input timestamp in \"yyyy-MM-ddTHH:mm:ss.s{precision}\" format, e.g \u00272020-12-30T12:13:1 4.123\u0027 and output timestamp in the same format.",
            "definesFormat": false,
            "key": "timestamp-format.standard",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Specify string literal to replace null key when \u0027maxwell-js
on.map-null-key.mode\u0027 is LITERAL.",
            "definesFormat": false,
            "key": "map-null-key.literal",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/orc",
        "source": true,
        "type": "orc",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027orc\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/orc/flink-sql-orc-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/parquet",
        "source": true,
        "type": "parquet",
```

" `ti` " [ 实时计算（流计算） API

```json
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027parquet\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Use UTC timezone or local timezone to the conversion between epo
ch time and LocalDateTime. Hive 0.x/1.x/2.x use local timezone. But Hive 3.x use UTC timezone.",
            "definesFormat": false,
            "key": "utc-timezone",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-flink-1.
15/opt/formats/parquet/flink-sql-parquet-1.15-vvr-6.0.7-SNAPSHOT.jar"
```

]

```json
      },
      {
        "sink": true,
        "name": "namespaces/flinkteam/formats/raw",
        "source": true,
        "type": "raw",
        "properties": [
          {
            "defaultValue": "",
            "description": "Must be set to \u0027raw\u0027 to configure this format.",
            "definesFormat": false,
            "key": "format",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "Specify the charset to encode the text string. \u0027UTF-8\u0027
will be used by default.",
            "definesFormat": false,
            "key": "charset",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "Specify the endianness to encode the bytes of numeric value. Val
id values are \u0027big-endian\u0027 and \u0027little-endian\u0027. \u0027big-endian\u0027 will be used by default.",
            "definesFormat": false,
            "key": "endianness",
            "required": false
          }
```

`],`

```json
        "packaged": true,
        "dependencies": []
```

实时计算（流计算） API

```
      }
```

`],`

```json
    "@type": "type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse"
  },
  "success": true,
  "requestId": "6BFF2035-B5FB-4E1A-8F32-4CA636417A3D"
}
```

`XML` 格式

```xml
<data>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/avro</name>
  <source>true</source>
  <type>avro</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;avro&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro/flink-sql-avro-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/avro-confluent</name>
  <source>true</source>
  <type>avro-confluent</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;avro-confluent&#x27; to configure this format.</descrip
tion>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The URL of the Confluent Schema Registry to fetch/register schemas.
</description>
   <definesFormat>false</definesFormat>
   <key>schema-registry.url</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The Confluent Schema Registry subject under which to register the schema
used by this format during serialization. Required for sink table.</description>
   <definesFormat>false</definesFormat>
   <key>schema-registry.subject</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
```

实时计算（流计算） API

```java
  packagedtrue/packaged
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/canal-json</name>
  <source>true</source>
  <type>canal-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;canal-json&#x27; to configure this format.</description
```

>

```xml
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Only read changelog rows which match the specific database (by comparing
the &quot;database&quot; meta field in the record).</description>
   <definesFormat>false</definesFormat>
   <key>database.include</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Only read changelog rows which match the specific table (by comparing the &q
uot;table&quot; meta field in the record).</description> <definesFormat>false</definesFormat>
```

实时计算（流计算） API

```xml
   <definesFormat>false</definesFormat>
   <key>table.include</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/csv</name>
  <source>true</source>
  <type>csv</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;csv&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional field delimiter character (&#x27;,&#x27; by default).</description>
   <definesFormat>false</definesFormat>
   <key>field-delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to disabled quote character for enclosing field values (false
by default). If true, quote-character can not be set.</description>
   <definesFormat>false</definesFormat>
   <key>disable-quote-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional quote character for enclosing field values (&#x27;&quot;&#x27; by d
efault).</description>
   <definesFormat>false</definesFormat>
   <key>quote-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to ignore comment lines that start with &#x27;#&#x27;(disabled
by default); if enabled, make sure to also ignore parse errors to allow empty rows.</descrip tion>
   <definesFormat>false</definesFormat>
   <key>allow-comments</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors.</description>
   <definesFormat>false</definesFormat>
<key>ignore-parse-errors</key>
```

实时计算（流计算） API

```xml
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional array element delimiter string for separating array and row element
values (&#x27;;&#x27; by default).</description>
   <definesFormat>false</definesFormat>
   <key>array-element-delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional escape character for escaping values (disabled by default).
</description>
   <definesFormat>false</definesFormat>
   <key>escape-character</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional null literal string that is interpreted as a null value (disabled b
y default).</description>
   <definesFormat>false</definesFormat>
   <key>null-literal</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/csv/flink-csv-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/debezium-avro-confluent</name>
  <source>true</source>
  <type>debezium-avro-confluent</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;debezium-avro-confluent&#x27; to configure this format.
</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The URL of the Confluent Schema Registry to fetch/register schemas.
</description>
   <definesFormat>false</definesFormat>
   <key>url</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Basic auth credentials source for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>basic-auth.credentials-source</key>
<reqired>false</reqired>
```

实时计算（流计算） API

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Basic auth user info for schema registry.</description>
   <definesFormat>false</definesFormat>
   <key>basic-auth.user-info</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Bearer auth credentials source for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>bearer-auth.credentials-source</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Bearer auth token for Schema Registry.</description>
   <definesFormat>false</definesFormat>
   <key>bearer-auth.token</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Properties map that is forwarded to the underlying Schema Registry. This is
useful for options that are not officially exposed via Flink config options. However, note that Flink options have higher precedence.</description>
   <definesFormat>false</definesFormat>
   <key>properties</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Location / File of SSL keystore.</description>
   <definesFormat>false</definesFormat>
   <key>ssl.keystore.location</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Password for SSL keystore</description>
   <definesFormat>false</definesFormat>
   <key>ssl.keystore.password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Location / File of SSL truststore.</description>
   <definesFormat>false</definesFormat>
   <key>ssl.truststore.location</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Password for SSL truststore.</description>
   <definesFormat>false</definesFormat>
```

k lt tt

```
d/k
```

实时计算（流计算） API

```xml
   <key>ssl.truststore.password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>The Confluent Schema Registry subject under which to register the schema
used by this format during serialization. By default, &#x27;kafka&#x27; and &#x27;upsertkafka&#x27; connectors use &#x27;&lt;topic_name&gt;-value&#x27; or &#x27;&lt;topic_name&gt;key&#x27; as the default subject name if this format is used as the value or key format. But for other connectors (e.g. &#x27;filesystem&#x27;), the subject option is required when used as sink.</description>
   <definesFormat>false</definesFormat>
   <key>subject</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/avro-confluent/flink-sql-avro-confluent-registry-1.15-vvr-6.0.7- SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/debezium-json</name>
  <source>true</source>
  <type>debezium-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;debezium-json&#x27; to configure this format.</descript
ion>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>When setting up a Debezium Kafka Connect, users can enable a Kafka configura
tion &#x27;value.converter.schemas.enable&#x27; to include schema in the message. This option indicates the Debezium JSON data include the schema in the message or not. Default is false.</description>
   <definesFormat>false</definesFormat>
   <key>schema-include</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing;
fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
```

实时计算（流计算） API

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/json</name>
  <source>true</source>
  <type>json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;json&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify whether to fail if a field is missing or not, false
by default.</description>
   <definesFormat>false</definesFormat>
   <key>fail-on-missing-field</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to skip fields and rows with parse errors instead of failing.
Fields are set to null in case of errors, false by default.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to use Jackson Stream API to deserialize json object, which br
ings 30% performance gain.</description>
   <definesFormat>false</definesFormat>
   <key>fast-deserialization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to specify timestamp format, SQL by default. Option ISO-8601
will parse input timestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format and
```

实时计算（流计算） API

```xml
output timestamp in the same format. Option SQL will parse input timestamp in &quot;yyyy-MMdd HH:mm:ss.s{precision}&quot; format and output timestamp in the same format. </description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to recursively flatten the JSON OBJECT field into columns in t
he top level schema. For a better understanding, the name of the flattened column will be c omposed of the path to get the column. For example, the field `col` in the json &quot;{ \&quot;nested\&quot;: {\&quot;col\&quot;: true} }&quot; is `nested.col` in the flattened sch ema. If the flattened field names get conflicts, currently the JsonParser will throw the exception to stop the execution. Please use the option &quot;json.ignore-parse-errors&quot; to ignore the parse errors.</description>
   <definesFormat>false</definesFormat>
   <key>infer-schema.flatten-nested-columns.enable</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Optional flag to infer primitive types as string type.</description>
   <definesFormat>false</definesFormat>
   <key>infer-schema.primitive-as-string</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/maxwell-json</name>
  <source>true</source>
  <type>maxwell-json</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;maxwell-json&#x27; to configure this format.</descripti
on>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Skip fields and rows with parse errors instead of failing. Fields are set
to null in case of errors.</description>
   <definesFormat>false</definesFormat>
   <key>ignore-parse-errors</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the input and output timestamp format. Currently supported values ar
e &#x27;SQL&#x27; and &#x27;ISO-8601&#x27;. Option &#x27;SQL&#x27; will parse input timestam p in &quot;yyyy-MM-dd HH:mm:ss.s{precision}&quot; format, e.g &#x27;2020-12-30 12:13:14.123&
```

实时计算（流计算） API

```xml
#x27; and output timestamp in the same format. Option &#x27;ISO-8601&#x27;will parse input t
imestamp in &quot;yyyy-MM-ddTHH:mm:ss.s{precision}&quot; format, e.g &#x27;2020-12- 30T12:13:14.123&#x27; and output timestamp in the same format.</description>
   <definesFormat>false</definesFormat>
   <key>timestamp-format.standard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify string literal to replace null key when &#x27;maxwell-json.map-null-
key.mode&#x27; is LITERAL.</description>
   <definesFormat>false</definesFormat>
   <key>map-null-key.literal</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/json/flink-json-1.15-vvr-6.0.7-SNAPSHOT-sql-jar.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/orc</name>
  <source>true</source>
  <type>orc</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;orc&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <packaged>true</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/orc/flink-sql-orc-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/parquet</name>
  <source>true</source>
  <type>parquet</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;parquet&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Use UTC timezone or local timezone to the conversion between epoch time and
LocalDateTime. Hive 0.x/1.x/2.x use local timezone. But Hive 3.x use UTC timezone. </description>
   <definesFormat>false</definesFormat>
   <key>utc-timezone</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
```

实时计算（流计算） API

```xml
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/ververica/connectors/vvr-6.0.7-fli
nk-1.15/opt/formats/parquet/flink-sql-parquet-1.15-vvr-6.0.7-SNAPSHOT.jar</dependencies>
 </formats>
 <formats>
  <sink>true</sink>
  <name>namespaces/flinkteam/formats/raw</name>
  <source>true</source>
  <type>raw</type>
  <properties>
   <defaultValue  />
   <description>Must be set to &#x27;raw&#x27; to configure this format.</description>
   <definesFormat>false</definesFormat>
   <key>format</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the charset to encode the text string. &#x27;UTF-8&#x27; will be use
d by default.</description>
   <definesFormat>false</definesFormat>
   <key>charset</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description>Specify the endianness to encode the bytes of numeric value. Valid values ar
e &#x27;big-endian&#x27; and &#x27;little-endian&#x27;. &#x27;big-endian&#x27; will be used by default.</description>
   <definesFormat>false</definesFormat>
   <key>endianness</key>
   <required>false</required>
  </properties>
  <packaged>true</packaged>
  <dependencies  />
 </formats>
 <@type>type.googleapis.com/vvp.sql.v1beta1.ListFormatsResponse</@type>
</data> <success>true</success> <requestId>6BFF2035-B5FB-4E1A-8F32-4CA636417A3D</requestId>
```

#### ListSecretValues

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-qingdao-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 5CC1B23C-CCA3- 4283-B275- 0F969CDFD34F | 请求ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "metadata": { "totalSize": 1, "totalPage": 1 }, "apiVersion": "v1", "kind": "SecretValueList", "items": [ { "metadata": { "createdAt": "2024- 03-11T03:07:09Z", "modifiedAt": "2024-03- 11T03:07:09Z", "resourceVersion": 1, "name": "secretkey", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "6dd63491-f0bf- 4af3-a38e- 7001d479addc", "labels": {} }, "apiVersion": "v1", "kind": "SecretValue", "spec": { "kind": "Plain", "value": "******" } } ] } | 详细数据。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/secret-values HTTP/1.1 &RegionId= &namespace= &workspace=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "metadata": {
      "totalSize": 1,
      "totalPage": 1
    },
    "apiVersion": "v1",
    "kind": "SecretValueList",
    "items": [
      {
        "metadata": {
          "createdAt": "2024-03-11T03:07:09Z",
          "modifiedAt": "2024-03-11T03:07:09Z",
          "resourceVersion": 1,
          "name": "secretkey",
          "namespace": "flinkteam",
          "annotations": {
            "creator": "229852610122763813",
            "modifier": "229852610122763813",
            "creatorName": "flinkadmin",
            "modifierName": "flinkadmin"
          },
          "id": "6dd63491-f0bf-4af3-a38e-7001d479addc",
          "labels": {}
        },
        "apiVersion": "v1",
        "kind": "SecretValue",
        "spec": {
          "kind": "Plain",
          "value": "******"
        }
      }
```

]

```json
  },
  "success": true,
  "requestId": "5CC1B23C-CCA3-4283-B275-0F969CDFD34F"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <metadata>
  <totalSize>1</totalSize>
  <totalPage>1</totalPage>
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>SecretValueList</kind>
 <items>
  <metadata>
   <createdAt>2024-03-11T03:07:09Z</createdAt>
   <modifiedAt>2024-03-11T03:07:09Z</modifiedAt>
   <resourceVersion>1</resourceVersion>
   <name>secretkey</name>
   <namespace>flinkteam</namespace>
   <annotations>
    <creator>229852610122763813</creator>
    <modifier>229852610122763813</modifier>
    <creatorName>flinkadmin</creatorName>
    <modifierName>flinkadmin</modifierName>
   </annotations>
   <id>6dd63491-f0bf-4af3-a38e-7001d479addc</id>
   <labels  />
  </metadata>
  <apiVersion>v1</apiVersion>
  <kind>SecretValue</kind>
  <spec>
   <kind>Plain</kind>
   <value>******</value>
  </spec>
 </items>
</data> <success>true</success> <requestId>5CC1B23C-CCA3-4283-B275-0F969CDFD34F</requestId>
```

#### ParseConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyze-jars HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | {"jarUris": ["hdfs:///vvp/data/sql- artifacts/namespaces/flink team/custom- connectors/2024-03- 12T01-50- 56.079896Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar"]} | 待解析的自定已connector jar包路径列表。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | {"connectors": [{"lookup":false,"su pportedFormats": [],"environments": [],"sink":true,"name" :"namespaces/flinkt eam/connectors/hol ogres- fix","source":true,"ty pe":"hologres- fix","properties": [{"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"poolsize","re quired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"async","requ ired":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"cacheReloadTi meBlackList","requir ed":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"password","req uired":false}, {"defaultValue":"fal se","description":""," d fi F t" f l |  |

实时计算（流计算） API

| 参数名称 | 类型 | definesFormat":false ,示"k例ey":"bhclientignor ebeforeupdate","req | 说明 |
|---|---|---|---|
|  |  | uired":false}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"jdbcretrysle epinitms","required" :false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"insertifnotexi sts","required":false }, {"defaultValue":"25 6","description":""," definesFormat":false |  |
|  |  | ,"key":"jdbcscanfetc hsize","required":fal se}, {"defaultValue":"- 1","description":""," definesFormat":false ,"key":"starttimems" ,"required":false}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"jdbcenabled efaultfornotnullcolu mn","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"binlog","requ ired":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"binlogbatchr eadsize","required": false}, {"defaultValue":"50 0","description":""," definesFormat":false ,"key":"clientmaxpa use","required":fals e}, {"defaultValue":"2", "description":"","defi nesFormat":false,"k ey":"errorcount","re quired":false}, {"defaultValue":"25 6","description":""," definesFormat":false ,"key":"jdbcwritebat chsize","required":fa lse}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"jdbcuselegac yputhandler","requir ed":false}, {"defaultValue":"12 8","description":""," definesFormat":false |  |

实时计算（流计算） API

|  |  | definesFormat :false |  |
|---|---|---|---|
| 参数名称 | 类型 | ,示"k例ey":"jdbcreadbatc hsize","required":fal | 说明 |
|  |  | se}, {"defaultValue":"4", "description":"","defi nesFormat":false,"k ey":"bhclientthread pool","required":fals e}, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"jdbcreadretryc ount","required":fals e}, {"defaultValue":"10 0000","description": "","definesFormat":f alse,"key":"cacheSiz e","required":false}, {"defaultValue":"10 000","description":"" ,"definesFormat":fal se,"key":"maxinque ue","required":false }, {"defaultValue":"10 0000","description": "","definesFormat":f alse,"key":"maxRow Count","required":fa lse}, {"defaultValue":"60 0000","description": "","definesFormat":f alse,"key":"bhclient asynctimeout","requ ired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enable direc _ t connect","required _ ":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"rpcrequeste veryfailures","requir ed":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"usebhclient mode","required":fal se}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"enablethrottl e","required":false}, {"defaultValue":"3", "description":"","defi nesFormat":false,"k ey":"connectionsize" ,"required":false}, {"defaultValue":"0", "description":"","defi nesFormat":false,"k ey":"jdbcreadtimeou |  |

实时计算（流计算） API

|  |  | y j |  |
|---|---|---|---|
| 参数名称 | 类型 | tms","required":fals 示例 e}, | 说明 |
|  |  | {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"jdbcretrycou nt","required":false} , {"defaultValue":"Ex ception","descriptio n":"","definesFormat ":false,"key":"action oninsert","required": false}, {"defaultValue":"hol ogres- fix","description":""," definesFormat":false ,"key":"connector"," required":true}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"username","req uired":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"bhclientread erqueue","required" :false}, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"maxconcurrenc ypershard","require d":false}, {"defaultValue":"20 48","description":"", "definesFormat":fals e,"key":"bhclientasy ncqueue","required" :false}, {"defaultValue":"\\u 0002","description": "","definesFormat":f alse,"key":"arraydeli miter","required":fal se}, {"defaultValue":"2", "description":"","defi nesFormat":false,"k ey":"bhclientwriterb atch","required":fals e}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"sqlretryinte rval","required":fals e}, {"defaultValue":"90 000","description":"" ,"definesFormat":fal se,"key":"bhclientti meout","required":f alse}, {"defaultValue":"20 97152","description ":"","definesFormat" |  |

实时计算（流计算） API

| 参数名称 | 类型 | :false,"key":"jdbcwri t示eb例atchbytesize","re | 说明 |
|---|---|---|---|
|  |  | quired":false}, {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"binlogretryi ntervalms","require d":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"fieldnametol ower","required":fal se}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"ignoredelete ","required":false}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"storerpcti meout","required":f alse}, {"defaultValue":"def ault","description":"" ,"definesFormat":fal se,"key":"resource _ group","required":fa lse}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"clientpause", "required":false}, {"defaultValue":"ins ertOrIgnore","descri ption":"","definesFor mat":false,"key":"m utatetype","required ":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"disablebinlo g","required":false}, {"defaultValue":"AL L","description":"","d efinesFormat":false, "key":"cache","requi red":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"sink.parallelism ","required":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"jdbcbinlogslotn ame","required":fals e}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"asynccapacit y","required":false}, {"defaultValue":"10 0" "description":"" " |  |

实时计算（流计算） API

| 参数名称 | 类型 | 0 , description : , d示e例finesFormat":false ,"key":"cacheScanLi | 说明 |
|---|---|---|---|
| data | String | mit","required":false }, {"defaultValue":"20 971520","descriptio n":"","definesFormat ":false,"key":"jdbcwr itebatchtotalbytesiz e","required":false}, {"defaultValue":"5", "description":"","defi nesFormat":false,"k ey":"rpcretries","req uired":false}, {"defaultValue":"10 24","description":"", "definesFormat":fals e,"key":"bhclientrea derbatch","required ":false}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"jdbcmetac achettl","required":f alse}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"splitstrategy" ,"required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"partitionrout er","required":false} , {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"connectionpool name","required":fal se}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal se,"key":"jdbcconne ctionmaxidlems","re quired":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"dbname","requi red":true}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enabletypen ormalization","requi red":false}, {"defaultValue":"26 2144","description": "","definesFormat":f alse,"key":"splitdata size","required":fals e}, {"defaultValue":"60 000","description":"" ,"definesFormat":fal | 自定义connector解析详细信息。 |

实时计算（流计算） API

|  |  | , definesFormat :fal |  |
|---|---|---|---|
| 参数名称 | 类型 | se,"key":"binlogrequ 示例 esttimeoutms","req | 说明 |
|  |  | uired":false}, {"defaultValue":"32 ","description":"","d efinesFormat":false, "key":"splitlength","r equired":false}, {"defaultValue":"18 0000","description": "","definesFormat":f alse,"key":"asynctim eoutms","required":f alse}, {"defaultValue":"bin ary","description":"", "definesFormat":fals e,"key":"jdbccopyfor mat","required":fals e}, {"defaultValue":"50 00","description":"", "definesFormat":fals e,"key":"jdbcretrysle epstepms","required ":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"userpcmode","r equired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"cdcmode","r equired":false}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"enableBinar yCache","required":f alse}, {"defaultValue":"10 000","description":"" ,"definesFormat":fal se,"key":"jdbcwritefl ushinterval","requir ed":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"shardrpcretri es","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"partial- insert.enabled","req uired":false}, {"defaultValue":"60 ","description":"","d efinesFormat":false, "key":"jdbcscantime outseconds","requir ed":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"insertorupda |  |

实时计算（流计算） API

| 参数名称 | 类型 | te","required":false} ,示例 | 说明 |
|---|---|---|---|
|  |  | {"defaultValue":"10 00","description":"", "definesFormat":fals e,"key":"scanbatchsi ze","required":false }, {"defaultValue":"1", "description":"","defi nesFormat":false,"k ey":"asynccallbackp ool","required":false }, {"defaultValue":":"," description":"","defi nesFormat":false,"k ey":"primarykeysep" ,"required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"createpartta ble","required":false }, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"reportmetric s","required":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"starttime","req uired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"useholohub mode","required":fal se}, {"defaultValue":"un ordered","descriptio n":"","definesFormat ":false,"key":"asyncr esultorder","require d":false}, {"defaultValue":"25 6","description":""," definesFormat":false ,"key":"jdbcreadbatc hqueuesize","requir ed":false}, {"defaultValue":"- 1","description":""," definesFormat":false ,"key":"jdbcmetaaut orefreshfactor","req uired":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"binlogmaxret rytimes","required":f alse}, {"defaultValue":"no ne","description":"", "definesFormat":fals e,"key":"sdkmode"," required":false}, {"d f ltV l " "92 |  |

实时计算（流计算） API

| 参数名称 | 类型 | {"defaultValue":"92 2示3例37203685477580 7","description":""," | 说明 |
|---|---|---|---|
|  |  | definesFormat":false ,"key":"cacheTTLMs ","required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"upsertsource ","required":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"bhclientignor edelete","required":f alse}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"remove- u0000-in- text.enabled","requi red":false}, {"defaultValue":"ear liestOffset","descript ion":"","definesForm at":false,"key":"binl ogstartupmode","re quired":false}, {"defaultValue":"10 0","description":""," definesFormat":false ,"key":"sqlretries","r equired":false}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"supportcolu mnstorageformat"," required":false}, {"defaultValue":"10 ","description":"","d efinesFormat":false, "key":"channelthrea dcount","required":f alse}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"ignorenullwh enupdate","required ":false}, {"defaultValue":"str eam","description":" ","definesFormat":fa lse,"key":" tablena __ me ","required":fal __ se}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"nullvalues","re quired":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"endpoint","req uired":true}, {"defaultValue":"10 000" "description":"" |  |

实时计算（流计算） API

|  |  | 000 , description : |  |
|---|---|---|---|
| 参数名称 | 类型 | ,示"d例efinesFormat":fal se,"key":"refreshint | 说明 |
|  |  | erval","required":fal se}, {"defaultValue":"\\u 0002","description": "","definesFormat":f alse,"key":"field deli _ miter","required":fal se}, {"defaultValue":"fal se","description":""," definesFormat":false ,"key":"enable filter _ push down","requir _ _ ed":false}, {"defaultValue":""," description":"","defi nesFormat":false,"k ey":"tablename","re quired":true}, {"defaultValue":"tru e","description":""," definesFormat":false ,"key":"cacheEmpty ","required":false}, {"defaultValue":"pu blic","description":"" ,"definesFormat":fal se,"key":"schemana me","required":false }, {"defaultValue":"60 0","description":""," definesFormat":false ,"key":"jdbcscantran sactionsessiontimeo utseconds","require d":false}],"package d":false,"dependenc ies": ["hdfs:///vvp/data/sq l- artifacts/namespace s/flinkteam/custom- connectors/2024- 03-12T01-50- 56.079896Z/ververi ca-connector- hologres-1.15-vvr- 6.0- fix.jar"]}],"@type":"t ype.googleapis.com/ vvp.sql.v1beta1.Ana lyzeConnectorJarsRe sponse","duplicated SourceFactoriesCon nectors": [],"duplicatedSinkFa ctoriesConnectors": []} |  |
| requestId | String | 05AEEA60-8B59- 4CCD-9F35- B27EE47F4D4E | 请求ID。 |

**示例**

实时计算（流计算） API 请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors:analyze-jars HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "connectors": [
      {
        "lookup": false,
        "supportedFormats": [],
        "environments": [],
        "sink": true,
        "name": "namespaces/flinkteam/connectors/hologres-fix",
        "source": true,
        "type": "hologres-fix",
        "properties": [
          {
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "poolsize",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "async",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "cacheReloadTimeBlackList",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "password",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
"dfi
```

F `t"` fl 实时计算（流计算） API

```json
            "definesFormat": false,
            "key": "bhclientignorebeforeupdate",
            "required": false
          },
          {
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcretrysleepinitms",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "insertifnotexists",
            "required": false
          },
          {
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscanfetchsize",
            "required": false
          },
          {
            "defaultValue": "-1",
            "description": "",
            "definesFormat": false,
            "key": "starttimems",
            "required": false
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "jdbcenabledefaultfornotnullcolumn",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "binlog",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "binlogbatchreadsize",
            "required": false
          },
          {
            "defaultValue": "500",
            "description": "",
            "definesFormat": false,
```

实时计算（流计算） API

```json
            "key": "clientmaxpause",
            "required": false
          },
          {
            "defaultValue": "2",
            "description": "",
            "definesFormat": false,
            "key": "errorcount",
            "required": false
          },
          {
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchsize",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "jdbcuselegacyputhandler",
            "required": false
          },
          {
            "defaultValue": "128",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadbatchsize",
            "required": false
          },
          {
            "defaultValue": "4",
            "description": "",
            "definesFormat": false,
            "key": "bhclientthreadpool",
            "required": false
          },
          {
            "defaultValue": "1",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadretrycount",
            "required": false
          },
          {
            "defaultValue": "100000",
            "description": "",
            "definesFormat": false,
            "key": "cacheSize",
            "required": false
          },
          {
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "maxinqueue",
```

实时计算（流计算） API

```json
            "required": false
          },
          {
            "defaultValue": "100000",
            "description": "",
            "definesFormat": false,
            "key": "maxRowCount",
            "required": false
          },
          {
            "defaultValue": "600000",
            "description": "",
            "definesFormat": false,
            "key": "bhclientasynctimeout",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enable_direct_connect",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "rpcrequesteveryfailures",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "usebhclientmode",
            "required": false
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "enablethrottle",
            "required": false
          },
          {
            "defaultValue": "3",
            "description": "",
            "definesFormat": false,
            "key": "connectionsize",
            "required": false
          },
          {
            "defaultValue": "0",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadtimeoutms",
            "required": false
```

实时计算（流计算） API

```json
          },
          {
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "jdbcretrycount",
            "required": false
          },
          {
            "defaultValue": "Exception",
            "description": "",
            "definesFormat": false,
            "key": "actiononinsert",
            "required": false
          },
          {
            "defaultValue": "hologres-fix",
            "description": "",
            "definesFormat": false,
            "key": "connector",
            "required": true
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "username",
            "required": false
          },
          {
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "bhclientreaderqueue",
            "required": false
          },
          {
            "defaultValue": "1",
            "description": "",
            "definesFormat": false,
            "key": "maxconcurrencypershard",
            "required": false
          },
          {
            "defaultValue": "2048",
            "description": "",
            "definesFormat": false,
            "key": "bhclientasyncqueue",
            "required": false
          },
          {
            "defaultValue": "\u0002",
            "description": "",
            "definesFormat": false,
            "key": "arraydelimiter",
            "required": false
          },
```

实时计算（流计算） API

```json
          {
            "defaultValue": "2",
            "description": "",
            "definesFormat": false,
            "key": "bhclientwriterbatch",
            "required": false
          },
          {
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "sqlretryinterval",
            "required": false
          },
          {
            "defaultValue": "90000",
            "description": "",
            "definesFormat": false,
            "key": "bhclienttimeout",
            "required": false
          },
          {
            "defaultValue": "2097152",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchbytesize",
            "required": false
          },
          {
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "binlogretryintervalms",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "fieldnametolower",
            "required": false
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "ignoredelete",
            "required": false
          },
          {
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "storerpctimeout",
            "required": false
          },
          {
```

实时计算（流计算） API

```json
            "defaultValue": "default",
            "description": "",
            "definesFormat": false,
            "key": "resource_group",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "clientpause",
            "required": false
          },
          {
            "defaultValue": "insertOrIgnore",
            "description": "",
            "definesFormat": false,
            "key": "mutatetype",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "disablebinlog",
            "required": false
          },
          {
            "defaultValue": "ALL",
            "description": "",
            "definesFormat": false,
            "key": "cache",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "sink.parallelism",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "jdbcbinlogslotname",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "asynccapacity",
            "required": false
          },
          {
            "defaultValue": "100",
```

实时计算（流计算） API ,

```json
            "description": "",
            "definesFormat": false,
            "key": "cacheScanLimit",
            "required": false
          },
          {
            "defaultValue": "20971520",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwritebatchtotalbytesize",
            "required": false
          },
          {
            "defaultValue": "5",
            "description": "",
            "definesFormat": false,
            "key": "rpcretries",
            "required": false
          },
          {
            "defaultValue": "1024",
            "description": "",
            "definesFormat": false,
            "key": "bhclientreaderbatch",
            "required": false
          },
          {
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcmetacachettl",
            "required": false
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "splitstrategy",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "partitionrouter",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "connectionpoolname",
            "required": false
          },
          {
            "defaultValue": "60000",
"description":"",
```

实时计算（流计算） API

```
            description:
```

,

```json
            "definesFormat": false,
            "key": "jdbcconnectionmaxidlems",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "dbname",
            "required": true
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enabletypenormalization",
            "required": false
          },
          {
            "defaultValue": "262144",
            "description": "",
            "definesFormat": false,
            "key": "splitdatasize",
            "required": false
          },
          {
            "defaultValue": "60000",
            "description": "",
            "definesFormat": false,
            "key": "binlogrequesttimeoutms",
            "required": false
          },
          {
            "defaultValue": "32",
            "description": "",
            "definesFormat": false,
            "key": "splitlength",
            "required": false
          },
          {
            "defaultValue": "180000",
            "description": "",
            "definesFormat": false,
            "key": "asynctimeoutms",
            "required": false
          },
          {
            "defaultValue": "binary",
            "description": "",
            "definesFormat": false,
            "key": "jdbccopyformat",
            "required": false
          },
          {
            "defaultValue": "5000",
            "description": "",
"definesFormat":false
```

实时计算（流计算） API

```json
            definesFormat: false,
            "key": "jdbcretrysleepstepms",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "userpcmode",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "cdcmode",
            "required": false
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "enableBinaryCache",
            "required": false
          },
          {
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "jdbcwriteflushinterval",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "shardrpcretries",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "partial-insert.enabled",
            "required": false
          },
          {
            "defaultValue": "60",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscantimeoutseconds",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
"key":"insertorupdate"
```

实时计算（流计算） API

```json
            "key": "insertorupdate",
            "required": false
          },
          {
            "defaultValue": "1000",
            "description": "",
            "definesFormat": false,
            "key": "scanbatchsize",
            "required": false
          },
          {
            "defaultValue": "1",
            "description": "",
            "definesFormat": false,
            "key": "asynccallbackpool",
            "required": false
          },
          {
            "defaultValue": ":",
            "description": "",
            "definesFormat": false,
            "key": "primarykeysep",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "createparttable",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "reportmetrics",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "starttime",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "useholohubmode",
            "required": false
          },
          {
            "defaultValue": "unordered",
            "description": "",
            "definesFormat": false,
            "key": "asyncresultorder",
```

" i `d"` fl 实时计算（流计算） API

```json
            "required": false
          },
          {
            "defaultValue": "256",
            "description": "",
            "definesFormat": false,
            "key": "jdbcreadbatchqueuesize",
            "required": false
          },
          {
            "defaultValue": "-1",
            "description": "",
            "definesFormat": false,
            "key": "jdbcmetaautorefreshfactor",
            "required": false
          },
          {
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "binlogmaxretrytimes",
            "required": false
          },
          {
            "defaultValue": "none",
            "description": "",
            "definesFormat": false,
            "key": "sdkmode",
            "required": false
          },
          {
            "defaultValue": "9223372036854775807",
            "description": "",
            "definesFormat": false,
            "key": "cacheTTLMs",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "upsertsource",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "bhclientignoredelete",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "remove-u0000-in-text.enabled",
            "required": false
```

实时计算（流计算） API

```json
          },
          {
            "defaultValue": "earliestOffset",
            "description": "",
            "definesFormat": false,
            "key": "binlogstartupmode",
            "required": false
          },
          {
            "defaultValue": "100",
            "description": "",
            "definesFormat": false,
            "key": "sqlretries",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "supportcolumnstorageformat",
            "required": false
          },
          {
            "defaultValue": "10",
            "description": "",
            "definesFormat": false,
            "key": "channelthreadcount",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "ignorenullwhenupdate",
            "required": false
          },
          {
            "defaultValue": "stream",
            "description": "",
            "definesFormat": false,
            "key": "__tablename__",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "nullvalues",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "endpoint",
            "required": true
          },
```

实时计算（流计算） API

```json
          {
            "defaultValue": "10000",
            "description": "",
            "definesFormat": false,
            "key": "refreshinterval",
            "required": false
          },
          {
            "defaultValue": "\u0002",
            "description": "",
            "definesFormat": false,
            "key": "field_delimiter",
            "required": false
          },
          {
            "defaultValue": "false",
            "description": "",
            "definesFormat": false,
            "key": "enable_filter_push_down",
            "required": false
          },
          {
            "defaultValue": "",
            "description": "",
            "definesFormat": false,
            "key": "tablename",
            "required": true
          },
          {
            "defaultValue": "true",
            "description": "",
            "definesFormat": false,
            "key": "cacheEmpty",
            "required": false
          },
          {
            "defaultValue": "public",
            "description": "",
            "definesFormat": false,
            "key": "schemaname",
            "required": false
          },
          {
            "defaultValue": "600",
            "description": "",
            "definesFormat": false,
            "key": "jdbcscantransactionsessiontimeoutseconds",
            "required": false
          }
```

`],`

```json
        "packaged": false,
        "dependencies": [
          "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-12T
01-50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

]

```
      }
```

`],` 实时计算（流计算） API

```json
    "@type": "type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse",
    "duplicatedSourceFactoriesConnectors": [],
    "duplicatedSinkFactoriesConnectors": []
  },
  "success": true,
  "requestId": "05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E"
}
```

`XML` 格式

```xml
<data>
 <connectors>
  <lookup>false</lookup>
  <supportedFormats  />
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>poolsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>async</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheReloadTimeBlackList</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>password</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientignorebeforeupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
<description
```

`/>` 实时计算（流计算） API

```xml
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrysleepinitms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>insertifnotexists</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcscanfetchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>-1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>starttimems</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcenabledefaultfornotnullcolumn</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlog</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogbatchreadsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>500</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>clientmaxpause</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2</defaultValue>
   <description  />
<definesFormat>false</definesFormat>
```

实时计算（流计算） API

```xml
   <definesFormat>false</definesFormat>
   <key>errorcount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcuselegacyputhandler</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>128</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadbatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>4</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientthreadpool</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadretrycount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheSize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>maxinqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
```

k `/k` 实时计算（流计算） API

```xml
   <key>maxRowCount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>600000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientasynctimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enable_direct_connect</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>rpcrequesteveryfailures</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>usebhclientmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enablethrottle</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>3</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connectionsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>0</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcreadtimeoutms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrycount</key>
```

实时计算（流计算） API

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>Exception</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>actiononinsert</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>username</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientreaderqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>maxconcurrencypershard</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2048</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientasyncqueue</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue></defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>arraydelimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientwriterbatch</key>
   <required>false</required>
```

实时计算（流计算） API

```xml
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sqlretryinterval</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>90000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclienttimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>2097152</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchbytesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogretryintervalms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>fieldnametolower</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>ignoredelete</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>storerpctimeout</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>default</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>resource_group</key>
   <required>false</required>
  </properties>
```

实时计算（流计算） API

```xml
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>clientpause</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>insertOrIgnore</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>mutatetype</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>disablebinlog</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>ALL</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cache</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>sink.parallelism</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcbinlogslotname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynccapacity</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheScanLimit</key>
   <required>false</required>
  </properties>
  <properties>
```

实时计算（流计算） API

```xml
   <defaultValue>20971520</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwritebatchtotalbytesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>5</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>rpcretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1024</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientreaderbatch</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcmetacachettl</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitstrategy</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>partitionrouter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>connectionpoolname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcconnectionmaxidlems</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
```

实时计算（流计算） API

```xml
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enabletypenormalization</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>262144</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitdatasize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogrequesttimeoutms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>32</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>splitlength</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>180000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynctimeoutms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>binary</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbccopyformat</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>5000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcretrysleepstepms</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
```

实时计算（流计算） API p /

```xml
   <definesFormat>false</definesFormat>
   <key>userpcmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cdcmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enableBinaryCache</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcwriteflushinterval</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>shardrpcretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>partial-insert.enabled</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>60</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcscantimeoutseconds</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>insertorupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1000</defaultValue>
   <description  />
<definesFormat>false</definesFormat>
```

实时计算（流计算） API

```xml
   <definesFormat>false</definesFormat>
   <key>scanbatchsize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asynccallbackpool</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>:</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>primarykeysep</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>createparttable</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>reportmetrics</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>starttime</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>useholohubmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>unordered</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>asyncresultorder</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>256</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
<key>jdbcreadbatchqueuesize</key>
```

实时计算（流计算） API

```xml
   <key>jdbcreadbatchqueuesize</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>-1</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcmetaautorefreshfactor</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogmaxretrytimes</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>none</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sdkmode</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>9223372036854775807</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheTTLMs</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>upsertsource</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>bhclientignoredelete</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>remove-u0000-in-text.enabled</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>earliestOffset</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>binlogstartupmode</key>
<required>false</required>
```

实时计算（流计算） API

```xml
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>100</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>sqlretries</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>supportcolumnstorageformat</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>10</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>channelthreadcount</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>ignorenullwhenupdate</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>stream</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>__tablename__</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>nullvalues</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>10000</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>refreshinterval</key>
   <required>false</required>
```

`</` `ti` > 实时计算（流计算） API

```xml
  </properties>
  <properties>
   <defaultValue></defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>field_delimiter</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>false</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>enable_filter_push_down</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue>true</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>cacheEmpty</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>public</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>schemaname</key>
   <required>false</required>
  </properties>
  <properties>
   <defaultValue>600</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>jdbcscantransactionsessiontimeoutseconds</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-0
3-12T01-50-56.079896Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar</dependencies>
 </connectors>
 <@type>type.googleapis.com/vvp.sql.v1beta1.AnalyzeConnectorJarsResponse</@type>
 <duplicatedSourceFactoriesConnectors  />
 <duplicatedSinkFactoriesConnectors  />
</data> <success>true</success> <requestId>05AEEA60-8B59-4CCD-9F35-B27EE47F4D4E</requestId>
```

#### ParseFormat

实时计算（流计算） API

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jars HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | { "jarUris": [ "hdfs:///vvp/data/sql- artifacts/namespaces/ver verica/connectors/vvr- 6.0.7-flink- 1.15/opt/formats/csv/flink- csv-1.15-vvr-6.0.7- SNAPSHOT-sql-jar.jar" ] } | 待解析format jar包列表。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "duplicatedSinkFact oriesFormats": [], "formats": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.A nalyzeFormatJarsRe sponse", "duplicatedFilesyste mFormatFactoriesFo rmats": [], "duplicatedSourceFa ctoriesFormats": [] } | Format解析结果详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C95A189B-7314- 48BF-90B0- 2F27D1C8816F | 请求ID。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats:analyze-jars HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "duplicatedSinkFactoriesFormats": [],
    "formats": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse",
    "duplicatedFilesystemFormatFactoriesFormats": [],
    "duplicatedSourceFactoriesFormats": []
  },
  "success": true,
  "requestId": "C95A189B-7314-48BF-90B0-2F27D1C8816F"
}
```

`XML` 格式

```xml
<data>
 <duplicatedSinkFactoriesFormats  />
 <formats  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.AnalyzeFormatJarsResponse</@type>
 <duplicatedFilesystemFormatFactoriesFormats  />
 <duplicatedSourceFactoriesFormats  />
</data> <success>true</success> <requestId>C95A189B-7314-48BF-90B0-2F27D1C8816F</requestId>
```

#### SearchFoldersByKeyword

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

实时计算（流计算） API

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| paramsJso n | String | Body | 否 | null | 请求参数，可不传。 |
| keyword | String | Query | 否 | my | 查询关键字。 |
| type | String | Query | 否 | development | 类型，查询文件夹传入： development。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | [ { "name": "myfolder", "id": "e777f423-b4de- 434c-a6db- 23e88e080a5e", "type": "Folder" } ] | 文件夹详细信息。 |
| requestId | String | B29F2776-C7FF- 4740-9284- 1821297B0085 | 请求ID。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders HTTP/1.1 &RegionId= &workspace= &namespace=
```

&公共请求参数实时计算（流计算） API 正常返回示例 `JSON` 格式

```json
{
  "data": [
    {
      "name": "myfolder",
      "id": "e777f423-b4de-434c-a6db-23e88e080a5e",
      "type": "Folder"
    }
```

`],`

```json
  "success": true,
  "requestId": "B29F2776-C7FF-4740-9284-1821297B0085"
}
```

`XML` 格式

```xml
<data>
 <name>myfolder</name>
 <id>e777f423-b4de-434c-a6db-23e88e080a5e</id>
 <type>Folder</type>
</data> <success>true</success> <requestId>B29F2776-C7FF-4740-9284-1821297B0085</requestId>
```

#### SetDeploymentResourceMode

调用SetDeploymentResourceMode，设置作业resourceMode。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/set-res ource HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| paramsJso n | String | Body | 否 | { "deploymentResourceMod eBase": { "kind": "auto" } } | 请求参数，kind可选项： auto、fine-grained、 coarse-grained。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
|  |  | { "metadata": { "createdAt": "2024- 03-12T06:12:17Z", "modifiedAt": "2024-03- 12T06:44:00.82332 3Z", "resourceVersion": 15, "name": "sqljob", "namespace": "flinkteam", "annotations": { "creator": "229852610122763 813", "resource- plan.has.migrated": "true", "deployment.has.de ployed": "false", "deployment.source -type": "EDITOR", "deployment.parent. id": "", "modifier": "229852610122763 813", "creatorName": "flinkadmin", "priority": "5", "priority.class.name ": "", "autopilot.mode": "monitor", "com.dataartisans.a ppmanager.controll er.deployment.spec. version": "3", "deployment.refere nced.deployment.dr aft.history.version": "1", "x-namespace- owner-master-uid": "105291012272990 9", "default.resource- setting.has.migrate |  |

实时计算（流计算） API

| 参数名称 | 类型 | d": "true", "示de例ployment.exec- | 说明 |
|---|---|---|---|
|  |  | plan.uri": "hdfs:///vvp/data/pla n/namespaces/flinkt eam/deployment/d0 b3abf0-4bfe-46b1- a324- 5b7def580c00/exec Plan.json", "deployment.refere nced.deployment.dr aft.id": "c6f157ac- 60b9-4b38-8bad- d435387cfd59", "comment": "", "modifierName": "flinkadmin", "taker": "default- cluster \| 0", "deployment.refere nced.deployment.dr aft.history.id": "1fbfefd4-9b1c- 4e94-b6ad- 268a5c6b64cd" }, "workspaceName": "default", "id": "d0b3abf0-4bfe- 46b1-a324- |  |
| data | String | 5b7def580c00", "labels": {} }, "apiVersion": "v1", "kind": "Deployment", "spec": { "template": { "metadata": { "annotations": { "flink.resource.type" : "auto", "job.resource.total. memory.byte": "8589934592", "job.resource.total.c pu": "4.0", "native.kubernetes. mode": "true", "flink.queryable- state.enabled": "false" } }, "spec": { "artifact": { "flinkImageTag": "1.15.0-vvr-6.0.7- 29", "kind": "SQLSCRIPT", "sqlScript": "-- ******************** ******************** ******************** ********-- -- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here -- | 详细数据。 |

实时计算（流计算） API

| 参数名称 | 类型 | ******************** *示**例***************** | 说明 |
|---|---|---|---|
|  |  | ******************** ********-- CREATE TEMPORARY TABLE `datahub table` _ (strname VARCHAR) with ( \u0027connector\u0 027 \u003d \u0027datagen\u00 27 ); CREATE TEMPORARY TABLE `kafka table` _ (strname VARCHAR, lens BIGINT) with ( \u0027connector\u0 027 \u003d \u0027print\u0027 ); INSERT INTO kafka table _ SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR LENGTH _ (strname) AS BIGINT) AS lens FROM datahub table; _ ", "imageUserDefined" : false, "flinkImageRegistry" : "cn-qingdao- env17e-d01- reg.docker.intra.env 17e.shuguang.com: 80/ververica-paas", "versionName": "vvr-6.0.0-flink- 1.15", "flinkImageReposito ry": "vvr", "flinkVersion": "1.15" }, "parallelism": 1, "batchMode": false, "resources": { "jobmanager": { "memory": "4Gi", "cpu": 2.0 }, "taskmanager": { "memory": "4Gi", "cpu": 2.0 } }, "logging": { "log4jLoggers": { "": "INFO" }, "logReservePolicy": { "expirationDays": 7, "openHistory": true }, "loggingProfile": "default" }, "flinkConfiguration": { |  |

实时计算（流计算） API

| 参数名称 | 类型 | "execution.checkpoi n示ti例ng.interval": | 说明 |
|---|---|---|---|
|  |  | "180s", "execution.checkpoi nting.min-pause": "180s" } } }, "restoreStrategy": { "kind": "LATEST STATE", _ "allowNonRestoredS tate": false }, "state": "RUNNING", "upgradeStrategy": { "kind": "NONE" }, "maxSavepointCreat ionAttempts": 4, "maxJobCreationAtt empts": 1, "deploymentTargetI d": "f2ed6708-a7e1- 4e86-a99e- 327fac9265c2" }, "status": { "startTime": 0, "state": "RUNNING", "endTime": 0 } } |  |
| requestId | String | BCC13432-238D- 41D7-B0A6- 582241A6B572 | 请求ID。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId]/set-res ource HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"", "deploymentId":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "metadata": {
      "createdAt": "2024-03-12T06:12:17Z",
      "modifiedAt": "2024-03-12T06:44:00.823323Z",
      "resourceVersion": 15,
      "name": "sqljob",
      "namespace": "flinkteam",
      "annotations": {
        "creator": "229852610122763813",
        "resource-plan.has.migrated": "true",
        "deployment.has.deployed": "false",
        "deployment.source-type": "EDITOR",
        "deployment.parent.id": "",
```

实时计算（流计算） API

```json
        "modifier": "229852610122763813",
        "creatorName": "flinkadmin",
        "priority": "5",
        "priority.class.name": "",
        "autopilot.mode": "monitor",
        "com.dataartisans.appmanager.controller.deployment.spec.version": "3",
        "deployment.referenced.deployment.draft.history.version": "1",
        "x-namespace-owner-master-uid": "1052910122729909",
        "default.resource-setting.has.migrated": "true",
        "deployment.exec-plan.uri":
"hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-4bfe-46b1-a324-5b7def580c00/ execPlan.json",
        "deployment.referenced.deployment.draft.id": "c6f157ac-60b9-4b38-8bad-d435387cfd59",
        "comment": "",
        "modifierName": "flinkadmin",
        "taker": "default-cluster | 0",
        "deployment.referenced.deployment.draft.history.id": "1fbfefd4-9b1c-4e94-b6ad-268a5c
6b64cd"
      },
      "workspaceName": "default",
      "id": "d0b3abf0-4bfe-46b1-a324-5b7def580c00",
      "labels": {}
    },
    "apiVersion": "v1",
    "kind": "Deployment",
    "spec": {
      "template": {
        "metadata": {
          "annotations": {
            "flink.resource.type": "auto",
            "job.resource.total.memory.byte": "8589934592",
            "job.resource.total.cpu": "4.0",
            "native.kubernetes.mode": "true",
            "flink.queryable-state.enabled": "false"
          }
        },
        "spec": {
          "artifact": {
            "flinkImageTag": "1.15.0-vvr-6.0.7-29",
            "kind": "SQLSCRIPT",
            "sqlScript": "--
********************************************************************---- Author:         Wri
te your name here-- Created Time: 2024-03-12 14:11:38-- Description: Write your descrip tion here--********************************************************************--CREATE TEMP ORARY TABLE `datahub_table` (strname VARCHAR)with ( \u0027connector\u0027 \u003d \u0027da tagen\u0027 );CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT)with ( \u0027connector\u0027 \u003d \u0027print\u0027 );INSERT INTO kafka_tableSELECT SUBSTRING (s trname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lensFROM datahub_table ;",
            "imageUserDefined": false,
            "flinkImageRegistry": "cn-qingdao-env17e-d01-
reg.docker.intra.env17e.shuguang.com:80/ververica-paas",
            "versionName": "vvr-6.0.0-flink-1.15",
            "flinkImageRepository": "vvr",
            "flinkVersion": "1.15"
          },
          "parallelism": 1,
```

实时计算（流计算） API p ,

```json
          "batchMode": false,
          "resources": {
            "jobmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            },
            "taskmanager": {
              "memory": "4Gi",
              "cpu": 2.0
            }
          },
          "logging": {
            "log4jLoggers": {
              "": "INFO"
            },
            "logReservePolicy": {
              "expirationDays": 7,
              "openHistory": true
            },
            "loggingProfile": "default"
          },
          "flinkConfiguration": {
            "execution.checkpointing.interval": "180s",
            "execution.checkpointing.min-pause": "180s"
          }
        }
      },
      "restoreStrategy": {
        "kind": "LATEST_STATE",
        "allowNonRestoredState": false
      },
      "state": "RUNNING",
      "upgradeStrategy": {
        "kind": "NONE"
      },
      "maxSavepointCreationAttempts": 4,
      "maxJobCreationAttempts": 1,
      "deploymentTargetId": "f2ed6708-a7e1-4e86-a99e-327fac9265c2"
    },
    "status": {
      "startTime": 0,
      "state": "RUNNING",
      "endTime": 0
    }
  },
  "success": true,
  "requestId": "BCC13432-238D-41D7-B0A6-582241A6B572"
}
```

`XML` 格式

```xml
<data>
 <metadata>
  <createdAt>2024-03-12T06:12:17Z</createdAt>
  <modifiedAt>2024-03-12T06:44:00.823323Z</modifiedAt>
  <resourceVersion>15</resourceVersion>
```

实时计算（流计算） API

```xml
  <name>sqljob</name>
  <namespace>flinkteam</namespace>
  <annotations>
   <creator>229852610122763813</creator>
   <resource-plan.has.migrated>true</resource-plan.has.migrated>
   <deployment.has.deployed>false</deployment.has.deployed>
   <deployment.source-type>EDITOR</deployment.source-type>
   <deployment.parent.id />
   <modifier>229852610122763813</modifier>
   <creatorName>flinkadmin</creatorName>
   <priority>5</priority>
   <priority.class.name />
   <autopilot.mode>monitor</autopilot.mode>
<com.dataartisans.appmanager.controller.deployment.spec.version>3</com.dataartisans.appmanager ontroller.deployment.spec.version> <deployment.referenced.deployment.draft.history.version>1</deployment.referenced.deployment.dr t.history.version>
   <x-namespace-owner-master-uid>1052910122729909</x-namespace-owner-master-uid>
   <default.resource-setting.has.migrated>true</default.resource-setting.has.migrated>
   <deployment.exec-plan.uri>hdfs:///vvp/data/plan/namespaces/flinkteam/deployment/d0b3abf0-
4bfe-46b1-a324-5b7def580c00/execPlan.json</deployment.exec-plan.uri>
   <deployment.referenced.deployment.draft.id>c6f157ac-60b9-4b38-8bad-
d435387cfd59</deployment.referenced.deployment.draft.id>
   <comment  />
   <modifierName>flinkadmin</modifierName>
   <taker>default-cluster | 0</taker>
   <deployment.referenced.deployment.draft.history.id>1fbfefd4-9b1c-4e94-b6ad-268a5c6b64cd</
deployment.referenced.deployment.draft.history.id>
  </annotations>
  <workspaceName>default</workspaceName>
  <id>d0b3abf0-4bfe-46b1-a324-5b7def580c00</id>
  <labels  />
 </metadata>
 <apiVersion>v1</apiVersion>
 <kind>Deployment</kind>
 <spec>
  <template>
   <metadata>
    <annotations>
     <flink.resource.type>auto</flink.resource.type>
     <job.resource.total.memory.byte>8589934592</job.resource.total.memory.byte>
     <job.resource.total.cpu>4.0</job.resource.total.cpu>
     <native.kubernetes.mode>true</native.kubernetes.mode>
     <flink.queryable-state.enabled>false</flink.queryable-state.enabled>
    </annotations>
   </metadata>
   <spec>
    <artifact>
     <flinkImageTag>1.15.0-vvr-6.0.7-29</flinkImageTag>
     <kind>SQLSCRIPT</kind>
     <sqlScript>--********************************************************************--
-- Author: Write your name here -- Created Time: 2024-03-12 14:11:38 -- Description: Write your description here --********************************************************************--
```

实时计算（流计算） API

```xml
CREATE TEMPORARY TABLE `datahub_table` (strname VARCHAR) with (
    &#x27;connector&#x27; = &#x27;datagen&#x27;
  );
CREATE TEMPORARY TABLE `kafka_table` (strname VARCHAR, lens BIGINT) with (
    &#x27;connector&#x27; = &#x27;print&#x27;
  );
INSERT INTO kafka_table SELECT SUBSTRING (strname, 0, 10) AS strname, CAST (CHAR_LENGTH (strname) AS BIGINT) AS lens FROM
  datahub_table;
     </sqlScript>
     <imageUserDefined>false</imageUserDefined>
     <flinkImageRegistry>cn-qingdao-env17e-d01-
reg.docker.intra.env17e.shuguang.com:80/ververica-paas</flinkImageRegistry>
     <versionName>vvr-6.0.0-flink-1.15</versionName>
     <flinkImageRepository>vvr</flinkImageRepository>
     <flinkVersion>1.15</flinkVersion>
    </artifact>
    <parallelism>1</parallelism>
    <batchMode>false</batchMode>
    <resources>
     <jobmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </jobmanager>
     <taskmanager>
      <memory>4Gi</memory>
      <cpu>2</cpu>
     </taskmanager>
    </resources>
    <logging>
     <log4jLoggers>
      <>INFO</>
     </log4jLoggers>
     <logReservePolicy>
      <expirationDays>7</expirationDays>
      <openHistory>true</openHistory>
     </logReservePolicy>
     <loggingProfile>default</loggingProfile>
    </logging>
    <flinkConfiguration>
     <execution.checkpointing.interval>180s</execution.checkpointing.interval>
     <execution.checkpointing.min-pause>180s</execution.checkpointing.min-pause>
    </flinkConfiguration>
   </spec>
  </template>
  <restoreStrategy>
   <kind>LATEST_STATE</kind>
   <allowNonRestoredState>false</allowNonRestoredState>
  </restoreStrategy>
  <state>RUNNING</state>
  <upgradeStrategy>
   <kind>NONE</kind>
```

实时计算（流计算） API

```xml
  </upgradeStrategy>
  <maxSavepointCreationAttempts>4</maxSavepointCreationAttempts>
  <maxJobCreationAttempts>1</maxJobCreationAttempts>
  <deploymentTargetId>f2ed6708-a7e1-4e86-a99e-327fac9265c2</deploymentTargetId>
 </spec>
 <status>
  <startTime>0</startTime>
  <state>RUNNING</state>
  <endTime>0</endTime>
 </status>
</data> <success>true</success> <requestId>BCC13432-238D-41D7-B0A6-582241A6B572</requestId>
```

#### TableExists

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExists HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | ververica | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| cat | String | Path | 是 | vvp | catalog名称。 |
| database | String | Query | 是 | default | database名称。 |
| table | String | Query | 是 | mydatahub | table名称。 |

**返回数据**

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "@type": "type.googleapis.co m/vvp.sql.catalog.v 1beta2.TableExistsR esponse", "exists": true } | 详细信息。 |
| requestId | String | 39253EC3-B674- 4B11-AD97- C221D6DB1003 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/catalog/v1beta2/namespaces/[namespace]/catalogs/[cat]:tableExists HTTP/1.1 &RegionId= &namespace= &workspace= &cat= &database= &table=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "requestId": "39253EC3-B674-4B11-AD97-C221D6DB1003",
  "success": true,
  "httpCode": 200,
  "message": "",
  "reason": "",
  "data": {
    "@type": "type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse",
    "exists": true
  }
}
```

`XML` 格式

```xml
<requestId>39253EC3-B674-4B11-AD97-C221D6DB1003</requestId> <success>true</success> <httpCode>200</httpCode> <message /> <reason /> <data>
 <@type>type.googleapis.com/vvp.sql.catalog.v1beta2.TableExistsResponse</@type>
 <exists>true</exists>
</data>
```

实时计算（流计算） API

#### UpdateConnector

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1.
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | hologres-fix | 要变更的connector名称。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "type": "hologres-fix", "name": "namespaces/flinkteam/c onnectors/hologres-fix", "packaged": false, "source": true, "sink": true, "lookup": false, "dependencies": [ "hdfs:///vvp/data/sql- artifacts/namespaces/flink team/custom- connectors/2024-03- 11T05-51- 25.289740Z/ververica- connector-hologres-1.15- vvr-6.0-fix.jar" ], "supportedFormats": [ "json","csv" ], "properties": [ { "key": "connector", "required": true, "defaultValue": "hologres-fix", "description": "", "definesFormat": false }, { "key": "dbname", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "endpoint", "required": true, "defaultValue": "", "description": "", "definesFormat": false }, { "key": "tablename", "required": true, "defaultValue": "", "description": "", "definesFormat": false } ] } | 变更参数，用于声明 connector的属性，例如：类型名称、必填的连接参数、可否作为source、sink、依赖的jar包等。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "affectedTables": [], "connector": { "lookup": true, "supportedFormats" : [ "json", "csv" ], "environments": [], "sink": true, "name": "namespaces/flinkte am/connectors/holo gres-fix", "source": true, "type": "hologres-fix", "properties": [ { "defaultValue": "hologres-fix", "description": "", "definesFormat": false, "key": "connector", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "dbname", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "endpoint", "required": true }, { "defaultValue": "", "description": "", "definesFormat": false, "key": "tablename", "required": true } ], "packaged": false, "dependencies": [ "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/custom- connectors/2024- 03-11T05-51- 25.289740Z/ververi ca-connector- hologres-1.15-vvr- 6.0-fix.jar" ] }, "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateConnectorRes ponse" } | 详细数据。 |
| requestId | String | 4FA46133-1C97- 4B48-96E3- 3B7DFFFEC707 | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/connectors/[name] HTTP/1. { "RegionId":"", "workspace":"", "name":"", "namespace":"" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "affectedTables": [],
    "connector": {
      "lookup": true,
      "supportedFormats": [
        "json",
        "csv"
```

`],`

```json
      "environments": [],
      "sink": true,
      "name": "namespaces/flinkteam/connectors/hologres-fix",
      "source": true,
      "type": "hologres-fix",
      "properties": [
        {
          "defaultValue": "hologres-fix",
          "description": "",
          "definesFormat": false,
          "key": "connector",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "dbname",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "endpoint",
          "required": true
        },
        {
          "defaultValue": "",
          "description": "",
          "definesFormat": false,
          "key": "tablename",
          "required": true
        }
```

`],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-03-11T05
-51-25.289740Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar"
```

]

```json
    },
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse"
  },
  "success": true,
  "requestId": "4FA46133-1C97-4B48-96E3-3B7DFFFEC707"
}
```

实时计算（流计算） API `XML` 格式

```xml
<data>
 <affectedTables  />
 <connector>
  <lookup>true</lookup>
  <supportedFormats>json</supportedFormats>
  <supportedFormats>csv</supportedFormats>
  <environments  />
  <sink>true</sink>
  <name>namespaces/flinkteam/connectors/hologres-fix</name>
  <source>true</source>
  <type>hologres-fix</type>
  <properties>
   <defaultValue>hologres-fix</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>connector</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>dbname</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>endpoint</key>
   <required>true</required>
  </properties>
  <properties>
   <defaultValue  />
   <description  />
   <definesFormat>false</definesFormat>
   <key>tablename</key>
   <required>true</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/custom-connectors/2024-0
3-11T05-51-25.289740Z/ververica-connector-hologres-1.15-vvr-6.0-fix.jar</dependencies>
 </connector>
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateConnectorResponse</@type>
</data> <success>true</success> <requestId>4FA46133-1C97-4B48-96E3-3B7DFFFEC707</requestId>
```

#### UpdateFormat

调用UpdateFormat，用于Format变更，包含是否可为source、sink、format参数、依赖的jar包等。

**请求头**

实时计算（流计算） API 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| name | String | Path | 是 | customized-csv | 待变更的format名称。 |
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | format变更参数。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "affectedTables": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateFormatRespon se", "format": { "sink": false, "name": "namespaces/flinkte am/formats/customi zed-csv", "source": true, "type": "customized-csv", "properties": [ { "defaultValue": ",", "description": "", "definesFormat": false, "key": "format.column- delimiter", "required": false } ], "packaged": false, "dependencies": [ "hdfs:///tmp/myform ats/customized-csv- demo-1.0- SNAPSHOT.jar" ] } } | format变更后详细信息。 |
| requestId | String | 208EF7F3-647B- 4701-BCAD- 6A14FC4696FC | 请求ID。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/formats/[name] HTTP/1.1 { "RegionId":"", "workspace":"", "name":"", "namespace":"" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "affectedTables": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse",
    "format": {
      "sink": false,
      "name": "namespaces/flinkteam/formats/customized-csv",
      "source": true,
      "type": "customized-csv",
      "properties": [
        {
          "defaultValue": ",",
          "description": "",
          "definesFormat": false,
          "key": "format.column-delimiter",
          "required": false
        }
```

`],`

```json
      "packaged": false,
      "dependencies": [
        "hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar"
```

]

```json
    }
  },
  "success": true,
  "requestId": "208EF7F3-647B-4701-BCAD-6A14FC4696FC"
}
```

`XML` 格式

```xml
<data>
 <affectedTables  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateFormatResponse</@type>
 <format>
  <sink>false</sink>
  <name>namespaces/flinkteam/formats/customized-csv</name>
  <source>true</source>
  <type>customized-csv</type>
  <properties>
   <defaultValue>,</defaultValue>
   <description  />
   <definesFormat>false</definesFormat>
   <key>format.column-delimiter</key>
   <required>false</required>
  </properties>
  <packaged>false</packaged>
  <dependencies>hdfs:///tmp/myformats/customized-csv-demo-1.0-SNAPSHOT.jar</dependencies>
 </format>
</data> <success>true</success> <requestId>208EF7F3-647B-4701-BCAD-6A14FC4696FC</requestId>
```

#### UpdateMember

实时计算（流计算） API

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "role": "owner", "member": "242425410145292209" } | 用户业务权限变更参数。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名。 |
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 29F07013-6BE2- 4F99-90B6- 9E27BF2A26C4 | 请求ID。 |
| data | String | { "@type": "type.googleapis.co m/vvp.members.v1. UpdateMemberResp onse", "member": { "role": "owner", "member": "user:24242541014 5292209" } } | 变更后用户的业务权限详细信息。 |

**示例**

请求示例实时计算（流计算） API

```json
PUT /pop/workspaces/[workspace]/members/v1/namespaces/[namespace] HTTP/1.1 { "workspace":"", "namespace":"", "RegionId":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "data": {
    "@type": "type.googleapis.com/vvp.members.v1.UpdateMemberResponse",
    "member": {
      "role": "owner",
      "member": "user:242425410145292209"
    }
  },
  "success": true,
  "requestId": "29F07013-6BE2-4F99-90B6-9E27BF2A26C4"
}
```

`XML` 格式

```xml
<data>
 <@type>type.googleapis.com/vvp.members.v1.UpdateMemberResponse</@type>
 <member>
  <role>owner</role>
  <member>user:242425410145292209</member>
 </member>
</data> <success>true</success> <requestId>29F07013-6BE2-4F99-90B6-9E27BF2A26C4</requestId>
```

#### UpdateUdfArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| link企业版开 API | 发指南·Ap | pManager |  |  | 实时计算（流计算） |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "jarUrl": "hdfs:///vvp/data/sql- artifacts/namespaces/flink team/udfs/metric- transform-227- shaded/2024-03-08T08- 13-54.732313Z/metric- transform-2.2.7- shaded.jar" } | 变更参数。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| udfArtifact Name | String | Path | 是 | metric-transform-227- shaded | udf名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "missingClasses": [], "@type": "type.googleapis.co m/vvp.sql.v1beta1.U pdateUdfArtifactRes ponse", "collidingClasses": [], "udfArtifact": { "dependencyJarUris" : [], "udfClasses": [ { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TimestampProbe ", "classType": "UDF TYPE SCALAR _ _ " }, { "functionNames": [], "udfArtifactName": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "className": "com.alibaba.blink.u dtf.TransformUdtf", "classType": "UDF TYPE TABLE" _ _ } ], "artifactType": "ARTIFACT TYPE JA _ _ VA", "createTime": "2024-03- 08T08:13:54Z", "uploader": "223474909869445 380", "jarUpdateTime": "2024-03- 08T09:04:22.53111 3Z", "name": "namespaces/flinkte am/udfartifacts/metr ic-transform-227- shaded", "namespace": "namespaces/flinkte am", "jarUrl": "hdfs:///vvp/data/sql - artifacts/namespace s/flinkteam/udfs/met ric-transform-227- shaded/2024-03- 08T08-13- 54.732313Z/metric- transform-2.2.7- shaded.jar", "updateTime": "2024-03- 08T09:04:22.53111 3Z" } } | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | A2E6AB81-9FA6- 48EE-BF0D- 3829017F3C14 | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
PUT /pop/workspaces/[workspace]/sql/v1beta1/namespaces/[namespace]/udfartifacts/[udfArtifactName] HTTP/1.1 { "RegionId":"", "workspace":"", "namespace":"", "udfArtifactName":"" }
```

正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "missingClasses": [],
    "@type": "type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse",
    "collidingClasses": [],
    "udfArtifact": {
      "dependencyJarUris": [],
      "udfClasses": [
        {
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

,

```json
          "className": "com.alibaba.blink.udtf.TimestampProbe",
          "classType": "UDF_TYPE_SCALAR"
        },
        {
          "functionNames": [],
          "udfArtifactName": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded"
```

,

```json
          "className": "com.alibaba.blink.udtf.TransformUdtf",
          "classType": "UDF_TYPE_TABLE"
        }
```

`],`

```json
      "artifactType": "ARTIFACT_TYPE_JAVA",
      "createTime": "2024-03-08T08:13:54Z",
      "uploader": "223474909869445380",
      "jarUpdateTime": "2024-03-08T09:04:22.531113Z",
      "name": "namespaces/flinkteam/udfartifacts/metric-transform-227-shaded",
      "namespace": "namespaces/flinkteam",
      "jarUrl": "hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-2
27-shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar",
      "updateTime": "2024-03-08T09:04:22.531113Z"
    }
  },
  "requestId": "A2E6AB81-9FA6-48EE-BF0D-3829017F3C14",
  "success": true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <missingClasses  />
 <@type>type.googleapis.com/vvp.sql.v1beta1.UpdateUdfArtifactResponse</@type>
 <collidingClasses  />
 <udfArtifact>
  <dependencyJarUris  />
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TimestampProbe</className>
   <classType>UDF_TYPE_SCALAR</classType>
  </udfClasses>
  <udfClasses>
   <functionNames  />
   <udfArtifactName>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</udfArtifa
ctName>
   <className>com.alibaba.blink.udtf.TransformUdtf</className>
   <classType>UDF_TYPE_TABLE</classType>
  </udfClasses>
  <artifactType>ARTIFACT_TYPE_JAVA</artifactType>
  <createTime>2024-03-08T08:13:54Z</createTime>
  <uploader>223474909869445380</uploader>
  <jarUpdateTime>2024-03-08T09:04:22.531113Z</jarUpdateTime>
  <name>namespaces/flinkteam/udfartifacts/metric-transform-227-shaded</name>
  <namespace>namespaces/flinkteam</namespace>
  <jarUrl>hdfs:///vvp/data/sql-artifacts/namespaces/flinkteam/udfs/metric-transform-227-
shaded/2024-03-08T08-13-54.732313Z/metric-transform-2.2.7-shaded.jar</jarUrl>
  <updateTime>2024-03-08T09:04:22.531113Z</updateTime>
 </udfArtifact>
</data> <requestId>A2E6AB81-9FA6-48EE-BF0D-3829017F3C14</requestId> <success>true</success>
```

#### CreateNamespace

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /flink/namespace/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| name | String | Path | 是 | blinkteam | Namespace名称。 |

|  | 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager AP | I |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuBrand | String | Path | 是 | Intel | Namespace绑定的CPU类型，作业将调度到该CPU类型的机器上。 |
| region | String | Path | 否 | cn-wulan-env188-d01 | Region名称。 |
| allocateCu | String | Path | 是 | 10 | Namespace申请的CU。 |
| ownerUid | String | Path | 是 | 229852610122763813 | 资源ownerUid。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | E39BDDB3-7017- 410E-9A79- EF50218BEDBA | 请求ID。 |
| data | String | blinkteam | 创建完成的Namespace名称。 |

**示例**

请求示例

```json
POST /flink/namespace/create HTTP/1.1 { "RegionId":"", "name":"", "allocateCu":"", "ownerUid":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "eagleEyeTraceId": "0a11353617103145127224622d00c1",
  "asapiSuccess": true,
  "asapiRequestId": "E39BDDB3-7017-410E-9A79-EF50218BEDBA",
  "data": "blinkteam",
  "success": true,
  "requestId": "E39BDDB3-7017-410E-9A79-EF50218BEDBA"
}
```

`XML` 格式实时计算（流计算） API

```xml
<eagleEyeTraceId>0a11353617103145127224622d00c1</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>E39BDDB3-7017-410E-9A79-EF50218BEDBA</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>E39BDDB3-7017-410E-9A79-EF50218BEDBA</requestId>
```

#### DescribeNamespaces

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /flink/namespace/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| region | String | Path | 否 | cn-wulan-env188-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | { "data": [ { "Uid": "229852610122763 813", "MemUsed": "40802189312", "CpuBrand": "Intel", "CreateTime": 1710122900722, "Region": "cn- qingdao-env***- d01", "GuaranteeQuota": "15", "RoleBindings": " [{\"members\": [\"user:2298526101 22763813\"],\"role\" :\"owner\"}, {\"members\": [\"user:1052910122 729909\"],\"role\":\" owner\"}]", "VvpPortal": "realtime-compute- cn-qingdao-env17e- d01.console.con.env 17e.shuguang.com", "CpuUsed": "12.0", "Queue": "k8s- flinkteam", "Members": " [{\"member\":\"user :105291012272990 9\",\"role\":\"owner\" }, {\"member\":\"user: 2298526101227638 13\",\"role\":\"owner \"}]", "Name": "flinkteam" } ], "success": true, "requestId": "A26F6DD1-A0BE- 4842-BF85- E24E60E9019D" } | 返回信息。 |
| -Region | String | cn-qingdao-env17e- d01 | region名称 |
| -Cluster | String | default | 集群名称 |
| -Queue | String | k8s-blinkteam | 队列名称 |
| -Name | String | blinkteam | namespace名称 |
| -CpuBrand | String | Intel | name绑定的cpu类型，绑定后，作业将调度到该 cpu类型的机器上（目前仅支持同架构芯片的混布） |
| -CreateTime | Long | 1710314513015 | 创建时间 |

| link企业版开发指 API | 南·AppManager |  | 实时计算（流计算） |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| - GuaranteeQuot a | String | 10 | 资源配额 |
| -Uid | String | 2298526101227638 13 | owner uid |
| -RoleBindings | String | [{\"members\": [\"user:2298526101 22763813\"],\"role\" :\"owner\"}, {\"members\": [\"user:1052910122 729909\"],\"role\":\" owner\"}] | 资源角色绑定 |
| -Members | String | [{\"member\":\"user :105291012272990 9\",\"role\":\"owner\" }, {\"member\":\"user: 2298526101227638 13\",\"role\":\"owner \"}] | 业务授权信息 |
| -CpuUsed | String | 0 | 已使用cpu |
| -MemUsed | String | 0 | 已使用mem |
| -VvpPortal | String | realtime-compute- xxxxxconsole.con.xx xxx.com | vvp portal url |
| success | Boolean | true | 请求是否成功。 |
| requestId | String | A26F6DD1-A0BE- 4842-BF85- E24E60E9019D | 请求ID。 |

**示例**

请求示例

```
GET /flink/namespace/list HTTP/1.1 &RegionId=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": [
    {
      "MemUsed": "0.0",
      "CpuBrand": "Intel",
      "CreateTime": 1710314513015,
      "Region": "cn-qingdao-env***-d01",
      "GuaranteeQuota": "15",
      "RoleBindings": "[{\"members\":[\"user:229852610122763813\"],\"role\":\"owner\"},{\"me
mbers\":[\"user:1052910122729909\"],\"role\":\"owner\"}]",
      "VvpPortal": "realtime-compute-cn-qingdao-env***-d01.console.con.env***.shuguang.com",
      "CpuUsed": "0.0",
      "Queue": "k8s-blinkteam",
      "Members": "[{\"member\":\"user:1052910122729909\",\"role\":\"owner\"},
{\"member\":\"user:229852610122763813\",\"role\":\"owner\"}]",
      "Name": "blinkteam"
    },
    {
      "Uid": "229852610122763813",
      "MemUsed": "40802189312",
      "CpuBrand": "Intel",
      "CreateTime": 1710122900722,
      "Region": "cn-qingdao-env17e-d01",
      "GuaranteeQuota": "15",
      "RoleBindings": "[{\"members\":[\"user:229852610122763813\"],\"role\":\"owner\"},{\"me
mbers\":[\"user:1052910122729909\"],\"role\":\"owner\"}]",
      "VvpPortal": "realtime-compute-cn-qingdao-env***-d01.console.con.env***.shuguang.com",
      "CpuUsed": "12.0",
      "Queue": "k8s-flinkteam",
      "Members": "[{\"member\":\"user:1052910122729909\",\"role\":\"owner\"},
{\"member\":\"user:229852610122763813\",\"role\":\"owner\"}]",
      "Name": "flinkteam"
    }
```

`],`

```json
  "success": true,
  "requestId": "A26F6DD1-A0BE-4842-BF85-E24E60E9019D"
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>
 <MemUsed>0.0</MemUsed>
 <CpuBrand>Intel</CpuBrand>
 <CreateTime>1710314513015</CreateTime>
 <Region>cn-qingdao-env***-d01</Region>
 <GuaranteeQuota>15</GuaranteeQuota>
 <RoleBindings>[{&quot;members&quot;:
[&quot;user:229852610122763813&quot;],&quot;role&quot;:&quot;owner&quot;},{&quot;members&quo t;:[&quot;user:1052910122729909&quot;],&quot;role&quot;:&quot;owner&quot;}]</RoleBindings>
 <VvpPortal>realtime-compute-cn-qingdao-env***-
d01.console.con.env***.shuguang.com</VvpPortal>
 <CpuUsed>0.0</CpuUsed>
 <Queue>k8s-blinkteam</Queue>
 <Members>
[{&quot;member&quot;:&quot;user:1052910122729909&quot;,&quot;role&quot;:&quot;owner&quot;},{ &quot;member&quot;:&quot;user:229852610122763813&quot;,&quot;role&quot;:&quot;owner&quot;}]< /Members>
 <Name>blinkteam</Name>
</data> <data>
 <Uid>229852610122763813</Uid>
 <MemUsed>40802189312</MemUsed>
 <CpuBrand>Intel</CpuBrand>
 <CreateTime>1710122900722</CreateTime>
 <Region>cn-qingdao-env***-d01</Region>
 <GuaranteeQuota>15</GuaranteeQuota>
 <RoleBindings>[{&quot;members&quot;:
[&quot;user:229852610122763813&quot;],&quot;role&quot;:&quot;owner&quot;},{&quot;members&quo t;:[&quot;user:1052910122729909&quot;],&quot;role&quot;:&quot;owner&quot;}]</RoleBindings>
 <VvpPortal>realtime-compute-cn-qingdao-env***-
d01.console.con.env***.shuguang.com</VvpPortal>
 <CpuUsed>12.0</CpuUsed>
 <Queue>k8s-flinkteam</Queue>
 <Members>
[{&quot;member&quot;:&quot;user:1052910122729909&quot;,&quot;role&quot;:&quot;owner&quot;},{ &quot;member&quot;:&quot;user:229852610122763813&quot;,&quot;role&quot;:&quot;owner&quot;}]< /Members>
 <Name>flinkteam</Name>
</data> <success>true</success> <requestId>A26F6DD1-A0BE-4842-BF85-E24E60E9019D</requestId>
```

#### GetCluster

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /flink/cluster/get HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | Region ID。 |
| region | String | Path | 否 | cn-wulan-env188-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | A2A95BB4-44FE- 407D-8486- 80B3BD5B4779 | 请求ID。 |
| data | String | { "data": { "clusterResources": [ { "cpuBrand": "Intel", "cpuTotal": 189.0, "memTotal": 751.77, "memRequest": 177.0, "allocatedCu": "133.0", "cpuRequest": 55.22 } ], "enableNetworkPolic y": true }, "success": true, "requestId": "A2A95BB4-44FE- 407D-8486- 80B3BD5B4779" } | 集群资源信息。 |

**示例**

请求示例

```
GET /flink/cluster/get HTTP/1.1 &RegionId=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "data": {
    "clusterResources": [
      {
        "cpuBrand": "Intel",
        "cpuTotal": 189.0,
        "memTotal": 751.77,
        "memRequest": 177.0,
        "allocatedCu": "133.0",
        "cpuRequest": 55.22
      }
```

`],`

```json
    "enableNetworkPolicy": true
  },
  "success": true,
  "requestId": "A2A95BB4-44FE-407D-8486-80B3BD5B4779"
}
```

`XML` 格式

```xml
<data>
 <clusterResources>
  <cpuBrand>Intel</cpuBrand>
  <cpuTotal>189</cpuTotal>
  <memTotal>751.77</memTotal>
  <memRequest>177</memRequest>
  <allocatedCu>133.0</allocatedCu>
  <cpuRequest>55.22</cpuRequest>
 </clusterResources>
 <enableNetworkPolicy>true</enableNetworkPolicy>
</data> <success>true</success> <requestId>A2A95BB4-44FE-407D-8486-80B3BD5B4779</requestId>
```

#### UpdateNamespace

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /flink/namespace/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env230-d01 | Region ID。 |
| name | String | Path | 是 | blinkteam | Namespace名称。 |

| 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager AP |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| region | String | Path | 否 | cn-wulan-env230-d01 | Region名称。 |
| allocateCu | String | Path | 是 | 15 | 申请的CU数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | 53F11F14-0514- 4B46-9C59- 270F3C94DCD3 | 请求ID。 |
| data | String | blinkteam | 已变更的Namespace名称。 |

**示例**

请求示例

```json
PUT /flink/namespace/update HTTP/1.1 { "RegionId":"", "name":"", "allocateCu":"" }
```

正常返回示例 `JSON` 格式

```json
{
  "eagleEyeTraceId": "0a112ca217103152416904683d00c8",
  "asapiSuccess": true,
  "asapiRequestId": "53F11F14-0514-4B46-9C59-270F3C94DCD3",
  "data": "blinkteam",
  "success": true,
  "requestId": "53F11F14-0514-4B46-9C59-270F3C94DCD3"
}
```

`XML` 格式

```xml
<eagleEyeTraceId>0a112ca217103152416904683d00c8</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>53F11F14-0514-4B46-9C59-270F3C94DCD3</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>53F11F14-0514-4B46-9C59-270F3C94DCD3</requestId>
```

实时计算（流计算） API

#### DeleteNamespace

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /flink/namespace/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| name | String | Path | 是 | blinkteam | 要删除的Namespace名称。 |
| region | String | Path | 否 | cn-wulan-env230-d01 | Region名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CCF11162-0068- 4302-B226- 403D46673F0F | 请求ID。 |
| data | String | blinkteam | 删除的Namespace名称。 |

**示例**

请求示例

```
DELETE /flink/namespace/delete HTTP/1.1 &RegionId= &name=
```

&公共请求参数正常返回示例 `JSON` 格式实时计算（流计算） API

```json
{
  "eagleEyeTraceId": "0a11353617103175009232076d00c1",
  "asapiSuccess": true,
  "asapiRequestId": "CCF11162-0068-4302-B226-403D46673F0F",
  "data": "blinkteam",
  "success": true,
  "requestId": "CCF11162-0068-4302-B226-403D46673F0F"
}
```

`XML` 格式

```xml
<eagleEyeTraceId>0a11353617103175009232076d00c1</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <asapiRequestId>CCF11162-0068-4302-B226-403D46673F0F</asapiRequestId> <data>blinkteam</data> <success>true</success> <requestId>CCF11162-0068-4302-B226-403D46673F0F</requestId>
```

#### UpdateFolder

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | System | 是 | UpdateFolder | 系统规定参数。 |
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间 ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| folderId | String | Path | 是 | 123 | 文件夹ID。 |

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | 执行参数，sql脚本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| data | String | { "metadata": { "createdAt": "2026- 04-24T03:39:26Z", "workspace": "9cuwr9g7y1hl19", "modifiedAt": "2026-04- 24T03:39:27.04468 2Z", "namespace": "flinkteam", "name": "changsha after", _ "annotations": { "creator": "235406976657057 054", "modifier": "235406976657057 054", "creatorName": "flinkadmin", "modifierName": "flinkadmin" }, "id": "8fe51597-1450- 4b9c-94c9- 55382dc6c598", "parentId": "cd1562be-02ed- 32cf-945b- 9769afe4c55e" }, "apiVersion": "v1", "kind": "Folder", "spec": { "children": [] } } | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |

**示例**

请求示例实时计算（流计算） API

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1 { "Action":"UpdateFolder", "RegionId":"cn-wulan-env***-d01", "workspace":"default", "namespace":"flinkteam", "folderId":"123" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"metadata\":{\"createdAt\":\"2026-04-
24T03:39:26Z\",\"workspace\":\"9cuwr9g7y1hl19\",\"modifiedAt\":\"2026-04- 24T03:39:27.044682Z\",\"namespace\":\"flinkteam\",\"name\":\"changsha_after\",\"annotations\": {\"creator\":\"235406976657057054\",\"modifier\":\"235406976657057054\",\"creatorName\":\"flin dmin\",\"modifierName\":\"flinkadmin\"},\"id\":\"8fe51597-1450-4b9c-94c9-55382dc6c598\",\"pa rentId\":\"cd1562be-02ed-32cf-945b- 9769afe4c55e\"},\"apiVersion\":\"v1\",\"kind\":\"Folder\",\"spec\":{\"children\":[]}}",
 "success":true,
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****"
}
```

`XML` 格式

```xml
<data>{&quot;metadata&quot;:{&quot;createdAt&quot;:&quot;2026-04- 24T03:39:26Z&quot;,&quot;workspace&quot;:&quot;9cuwr9g7y1hl19&quot;,&quot;modifiedAt&quot;:&qu ;2026-04- 24T03:39:27.044682Z&quot;,&quot;namespace&quot;:&quot;flinkteam&quot;,&quot;name&quot;:&quot;c ngsha_after&quot;,&quot;annotations&quot;: {&quot;creator&quot;:&quot;235406976657057054&quot;,&quot;modifier&quot;:&quot;235406976657057 4&quot;,&quot;creatorName&quot;:&quot;flinkadmin&quot;,&quot;modifierName&quot;:&quot;flinkadm &quot;},&quot;id&quot;:&quot;8fe51597-1450-4b9c-94c9- 55382dc6c598&quot;,&quot;parentId&quot;:&quot;cd1562be-02ed-32cf-945b- 9769afe4c55e&quot;},&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Folder&quot;, uot;spec&quot;:{&quot;children&quot;:[]}}</data> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

#### DeleteFolder

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1
```

**请求参数**

实时计算（流计算） API

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | region名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间 ID。您可以通过以下任意一种方式获取： 通过 ListNamespaces 获取。 在Flink 全托管开发控制台工作空间详情中获取 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| folderId | String | Path | 是 | 123 | 文件夹ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
DELETE /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/folders/[folderId] HTTP/1.1 &RegionId=cn-wulan-env188-d01 &workspace=default &namespace=flinkteam &folderId=123
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

实时计算（流计算） API

#### UploadArtifactByOSSUrl

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTT P/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env188-d01 | region名称。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间 ID。您可以通过以下任意一种方式获取： 通过 ListNamespaces 获取。 在 Flink 全托管开发控制台工作空间详情中获取。 |
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | 执行参数，sql脚本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | String | { "success": true, "message": "", "plan": "" } | 详细信息。 |

| link企业版开发指 | 南·AppManager |  |  |
|---|---|---|---|

API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```json
POST /pop/workspaces/[workspace]/artifacts/v1/namespaces/[namespace]/artifacts:uploadByOSSUrl HTT P/1.1 { "RegionId":"cn-wulan-env188-d01", "namespace":"flinkteam", "workspace":"default" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{  \"success\": true,  \"message\": \"\",  \"plan\": \"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式

```xml
<data>{
  &quot;success&quot;: true,
  &quot;message&quot;: &quot;&quot;,
  &quot;plan&quot;: &quot;&quot;
}</data>
 <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
 <success>true</success>
```

#### ListJobs

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |

| 实时计算（流计 | 算） |  |  | Flink企 | 业版开发指南·AppManager AP |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| deploymen tId | String | Query | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {"success": true,"message": "","plan": ""} | 详细信息。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/jobs HTTP/1.1 &RegionId=cn-wulan-env188-d01 &deploymentId=d0b3abf0-4bfe-46b1-a324-5b7def580c00 &namespace=flinkteam &workspace=default
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"success\": true,\"message\": \"\",\"plan\": \"\"}",
 "requestId":"CBC799F0-AS7S-1D30-8A4F-882ED4DD****",
 "success":true
}
```

`XML` 格式实时计算（流计算） API

```xml
<data>{&quot;success&quot;: true,&quot;message&quot;: &quot;&quot;,&quot;plan&quot;: &quot;& quot;}</data> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId> <success>true</success>
```

#### ReplaceDeployment

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTT P/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Host | 是 | cn-wulan-env***-d01 | Region ID。 |
| namespac e | String | Path | 是 | flinkteam | 作业所在的项目空间名称。 |
| deploymen tId | String | Path | 是 | d0b3abf0-4bfe-46b1- a324-5b7def580c00 | 作业ID。 |
| paramsJso n | String | Body | 否 | { "name": "namespaces/flinkteam/fo rmats/customized-csv", "type": "customized-csv", "source": true, "sink": false, "properties": [ { "key": "format.column- delimiter", "required": false, "defaultValue": ",", "description": "" } ], "dependencies": [ "hdfs:///tmp/myformats/cu stomized-csv-demo-1.0- SNAPSHOT.jar" ] } | 执行参数，sql脚本。 |
| workspace | String | Path | 是 | default | 作业所在的工作空间ID。您可以通过以下任意一种方式获取： 通过ListNamespaces获取。 在Flink全托管开发控制台工作空间详情中获取。 |

**返回数据**

实时计算（流计算） API

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 请求是否成功。 |
| requestId | String | CBC799F0-AS7S- 1D30-8A4F- 882ED4DD**** | 请求ID。 |
| data | Integer | { "deploymentId" : "7f4143a2-2eee- 4c5c-8803- a50d388514ac", "name" : "jarjob", "executionMode" : "STREAMING", "streamingResource Setting" : { "resourceSettingMo de" : "BASIC", "basicResourceSetti ng" : { "parallelism" : 1, "jobmanagerResour ceSettingSpec" : { "cpu" : 1.0, "memory" : "4Gi" }, "taskmanagerResou rceSettingSpec" : { "cpu" : 1.0, "memory" : "4Gi" } } }, "kerberosConfig" : { "kerberosEnabled" : false }, "labels" : { }, "engineVersion" : "vvr-11.5.0-flink- 1.20", "referencedDeploym entDraftId" : "", "deploymentHasCha nged" : true, "taker" : " \| vvp-0", "priority" : 5, "resourceTuning" : { "mode" : "none", "resourceTuningId" : "", "resourceTuningNa me" : "", "scheduledPlanIsCa ncelling" : false }, "autopilot" : { "mode" : "", "recommendation" : "", "ignoreRecommend ation" : "" }, "deploymentTarget" : { "mode" : "PER JOB", "name" : _ "dt-flinkteam" }, "artifact" : { "kind" : "JAR", "jarArtifact" : { "jarUri" : "oss://flink- fullymanaged- apmd99ri0du673/art | 详细信息。 |

实时计算（流计算） API

| 参数名称 | 类型 | ifacts/namespaces/fl i示nk例team/TopSpeedW | 说明 |
|---|---|---|---|
|  |  | indowing.jar" } }, "flinkConf" : { "execution.checkpoi nting.interval" : "180s", "restart- strategy.fixed- delay.attempts" : "2147483647", "table.exec.state.ttl" : "36 h", "restart- strategy" : "fixed- delay", "execution.checkpoi nting.min-pause" : "180s", "restart- strategy.fixed- delay.delay" : "10 s" }, "logging" : { "loggingProfile" : "default", "log4jLoggers" : [ { "loggerName" : "", "loggerLevel" : "INFO" } ], "logReservePolicy" : { "openHistory" : true, "expirationDays" : 7 } }, "jobSummary" : { "starting" : 0, "running" : 0, "cancelling" : 0, "cancelled" : 0, "finished" : 0, "failed" : 0 }, "workspace" : "apmd99ri0du673", "namespace" : "flinkteam", "creator" : "206789961887523 346", |  |
|  |  | "creatorName" : "flinkadmin", "modifier" : "206789961887523 346", "modifierName" : "flinkadmin", "createdAt" : 1777526754, "modifiedAt" : 1777526754 } |  |

**示例**

请求示例实时计算（流计算） API

```json
PUT /pop/workspaces/[workspace]/api/v1/namespaces/[namespace]/deployments/[deploymentId] HTT P/1.1 { "RegionId":"cn-wulan-env188-d01", "namespace":"flinkteam", "deploymentId":"d0b3abf0-4bfe-46b1-a324-5b7def580c00", "workspace":"default" }
```

正常返回示例 `XML` 格式

```xml
<data /> <success>true</success> <requestId>CBC799F0-AS7S-1D30-8A4F-882ED4DD****</requestId>
```

### API示例

#### 示例

**注意事项**

凡是带有Resp的接口都要用固定的方式解析。所有put、post都要设置content-type以及使用自带的JsonUtil序列化。

**示例代码**

```java
package sample; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; import com.aliyuncs.ververica.model.v20200501.*; import com.fasterxml.jackson.core.JsonProcessingException; import com.fasterxml.jackson.core.type.TypeReference; import com.ververica.common.model.ResultModel; import com.ververica.common.model.deployment.Artifact; import com.ververica.common.model.deployment.Deployment; import com.ververica.common.model.deployment.DeploymentState; import com.ververica.common.model.namespace.Namespace; import com.ververica.common.params.*; import com.ververica.common.resp.*; import com.ververica.common.util.JsonUtil; import com.ververica.common.util.SdkUtil; import java.util.List; public class SdkSample {
 /**
```

* 正常格式：

```
 * {
 * "requestId":"202008030937-4TFJR5MK2R",
```

#为`true`时，结果中仅展示`requestId`，`false`时会抛出`reason`和`message`

```
*"success":true
```

实时计算（流计算） API `success``: true, #`为`true`时，结果中仅展示`requestId`，`false`时会抛出`reason`和`message`

```
 * "message": "",
 * "reason": "",
```

`* "data":` 数据内容（`Object`）

```
 * }
```

`*/`

```
   public static void main(String[] args) throws JsonProcessingException, ClientException {
 String regionId = "cn-hangzhou";
 DefaultProfile.addEndpoint(regionId, "ververica", "ververica-share.aliyuncs.com");
 IClientProfile profile = DefaultProfile.getProfile(regionId, "**************", "***********
*****");
 DefaultAcsClient client = new DefaultAcsClient(profile);
 /**
```

目前支持以下4个`region`

```
 ververica-share.cn-hangzhou.aliyuncs.com
 ververica-share.cn-shanghai.aliyuncs.com
 ververica-share.cn-shenzhen.aliyuncs.com
 ververica-share.cn-beijing.aliyuncs.com
```

`*/`

```
 String deploymentId = "placeholder";
```

`//namespace/deploymentId`根据实际环境作业配置 `//` 获取`namespaces`列表

```java
 ListNamespacesRequest listNamespacesRequest = new ListNamespacesRequest();
 ResultModel<ListNamespacesResp>listNamespacesRespResultModel =
JsonUtil.toBean(SdkUtil.getHttpContentString(client, listNamespacesRequest), new TypeReference<ResultModel<ListNamespacesResp>>() {
 });
List<Namespace> namespaceList = listNamespacesRespResultModel.getData().getNamespaces(); System.out.println(JsonUtil.toJson(namespaceList));
 String workspaceName = namespaceList.get(0).getWorkspace();
 String namespace = namespaceList.get(0).getName();
 // 获取deployment
 GetDeploymentRequest getDeploymentRequest = new GetDeploymentRequest();
    getDeploymentRequest.setWorkspace(workspaceName);
    getDeploymentRequest.setNamespace(namespace);
    getDeploymentRequest.setDeploymentId(deploymentId);
 String data = client.doAction(getDeploymentRequest).getHttpContentString();
 System.out.println(data);
 ResultModel<GetDeploymentResp> getDeploymentRespResultModel = JsonUtil.toBean(data, new
TypeReference<ResultModel<GetDeploymentResp>>() {
 });
 Deployment deployment = getDeploymentRespResultModel.getData();
    deployment.getMetadata().getAnnotations().put("update-flag", "zdbox");
 deployment.getMetadata().getLabels().put("key2", "value2");
    deployment.getSpec().setState(DeploymentState.RUNNING);
```

`//` 更新`deployment`状态

```
 UpdateDeploymentDesiredStateParams updateDeploymentDesiredStateParams = new
UpdateDeploymentDesiredStateParams(); updateDeploymentDesiredStateParams.setState(DeploymentState.CANCELLED); updateDeploymentDesiredStateRequest = new UpdateDeploymentDesiredStateRequest(); updateDeploymentDesiredStateRequest.setWorkspace(workspaceName); updateDeploymentDesiredStateRequest.setNamespace(namespace); updateDeploymentDesiredStateRequest.setDeploymentId(deploymentId); updateDeploymentDesiredStateRequest.setParamsJson(JsonUtil.toJson(updateDeploymentDesiredState rams));
```

实时计算（流计算） API

```java
rams)); updateDeploymentDesiredStateRequest.setHttpContentType(FormatType.JSON); System.out.println(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString()
 ResultModel<UpdateDeploymentDesiredStateResp>
updateDeploymentDesiredStateRespResultModel = JsonUtil.toBean(client.doAction(updateDeploymentDesiredStateRequest).getHttpContentString(), new TypeReference<ResultModel<UpdateDeploymentDesiredStateResp>>() {
 });
 System.out.println(JsonUtil.toJson(updateDeploymentDesiredStateRespResultModel));
```

`// Create savepoint:`如果`data`为空，则说明触发失败，请查看`message`

```
 /**
```

* 成功包含`data`字段返回数据：`{"data":{"metadata":{"createdAt":"2020-08-`

```json
18T07:04:40.379926Z","jobId":"d0d6720f-00ac-47cc-8d54-7d88a4d7b446","modifiedAt":"2020-08-18 T07:04:40.379926Z","deploymentId":"0cb796fc-2641-488e-bde8- 52b2199c5747","origin":"USER_REQUEST","resourceVersion":1,"namespace":"test","annotations":{ "com.dataartisans.appmanager.controller.deployment.spec.version":"4"},"id":"c4e40dc9-69c7-4b a0-8add-5f862ecb00ef"},"apiVersion":"v1","kind":"Savepoint","spec": {"savepointLocation":"oss://qiqi-zp/vvp/flinksavepoints/namespaces/test/deployments/0cb796fc-2641-488e-bde8-52b2199c5747/c4e40dc9-69c7- 4ba0-8add-5f862ecb00ef"},"status":{"state":"STARTED"}},"requestId":"188B1FFC-2729-458E-A404- D3CD5D972DA0"}
```

* 失败无`data`字段，并且有`message`：`{"RequestId":"B545121D-ED4C-4E71-9D76-`

```
CBD510A04E5B","HostId":"ververica-share.cnshanghai.aliyuncs.com","Code":"BadRequest","Message":"No active job for a deployment."}
```

`*/`

```java
createSavepointRequest = new CreateSavepointRequest(); createSavepointRequest.setWorkspace(workspaceName); createSavepointRequest.setNamespace(namespace);
 CreateSavepointParams createSavepointParams
= new CreateSavepointParams(); createSavepointParams.setDeploymentId(deploymentId); createSavepointRequest.setParamsJson(JsonUtil.toJson(createSavepointParams)); createSavepointRequest.setHttpContentType(FormatType.JSON);
 System.out.println(client.doAction(createSavepointRequest).getHttpContentString());
 ResultModel<CreateSavepointResp> savepoint =
JsonUtil.toBean(client.doAction(createSavepointRequest).getHttpContentString(), new TypeReference<ResultModel<CreateSavepointResp>>() {
 });
 System.out.println(JsonUtil.toJson(savepoint));
```

`//` 获取`savepoints`列表

```java
 ListSavepointsRequest listSavepointsRequest
= new ListSavepointsRequest(); listSavepointsRequest.setWorkspace(workspaceName); listSavepointsRequest.setNamespace(namespace); listSavepointsRequest.setDeploymentId(deploymentId); ResultModel<ListSavepointsResp> savepoints = JsonUtil.toBean(client.doAction(listSavepointsRequest).getHttpContentString(), new TypeRefer
 });
 System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints()));
```

S t t

```
itl(J UtiltJ (
```

it

```
tDt()
```

`tS`

```
it()
```

i

```
()))
```

实时计算（流计算） API

```java
System.out.println(JsonUtil.toJson(savepoints.getData().getSavepoints().size()));
```

`//` 获取`jobs`列表

```java
 ListJobsRequest listJobsRequest = new ListJobsRequest();
 listJobsRequest.setWorkspace(workspaceName);
 listJobsRequest.setNamespace(namespace);
listJobsRequest.setDeploymentId(deploymentId); JsonUtil.toBean(client.doAction(listJobsRequest).getHttpContentString(), new TypeReference<R
 });
System.out.println(JsonUtil.toJson(jobs.getData().getJobs()));
```

`//` 获取部署目标列表

```java
listDeploymentTargetsRequest = new ListDeploymentTargetsRequest(); listDeploymentTargetsRequest.setWorkspace(workspaceName); listDeploymentTargetsRequest.setNamespace(namespace);
 ResultModel<ListDeploymentTargetsResp> deploymentTargets =
JsonUtil.toBean(client.doAction(listDeploymentTargetsRequest).getHttpContentString(), new TypeReference<ResultModel<ListDeploymentTargetsResp>>() {
 });
System.out.println(JsonUtil.toJson(deploymentTargets.getData().getDeploymentTargets()));
```

`//sql`语法检查，成功则`validationResult`：`VALIDATION_RESULT_VALID_INSERT_QUERY`或者

```java
VALIDATION_RESULT_VALID_DDL_STATEMENT，其他查看errorDetails validateSqlScriptRequest = new ValidateSqlScriptRequest(); validateSqlScriptRequest.setWorkspace(workspaceName); validateSqlScriptRequest.setNamespace(namespace); validateSqlScriptParams = new ValidateSqlScriptParams();
 validateSqlScriptParams.setStatement("CREATE TABLE
RANDOM_TABLE(`name` STRING) with ('connector'='random','type'='random')"); validateSqlScriptRequest.setParamsJson(JsonUtil.toJson(validateSqlScriptParams)); validateSqlScriptRequest.setHttpContentType(FormatType.JSON); validateSqlScriptRespResultModel = JsonUtil.toBean(SdkUtil.getHttpContentString(client, validateSqlScriptRequest), new TypeReference<ResultModel<ValidateSqlScriptResp>>() { }); System.out.println(JsonUtil.toJson(validateSqlScriptRespResultModel));
```

`//` 执行`ddl`操作:如果成功data.result='RESULT_SUCCESS|RESULT_SUCCESS_WITH_ROWS',否则查看`message`

```
executeSqlScriptRequest = new ExecuteSqlScriptRequest(); executeSqlScriptRequest.setWorkspace(workspaceName); executeSqlScriptRequest.setNamespace(namespace);
 ExecuteSqlScriptParams executeSqlScriptParams
= new ExecuteSqlScriptParams();
 executeSqlScriptParams.setStatement("create table
abaaaa (a varchar) with ('connector' = 'random', 'type' = 'random');"); tables;"); executeSqlScriptRequest.setParamsJson(JsonUtil.toJson(executeSqlScriptParams)); executeSqlScriptRequest.setHttpContentType(FormatType.JSON); JsonUtil.toBean(client.doAction(executeSqlScriptRequest).getHttpContentString(), new TypeReference<ResultModel<ExecuteSqlScriptResp>>() {
```

实时计算（流计算） API

```java
 });
System.out.println(JsonUtil.toJson(executeSqlScriptRespResultModel));
```

`//`创建`deployment(sql`作业)

```java
 GetGlobalDeploymentDefaultsRequest getGlobalDeploymentDefaultsRequest
= new GetGlobalDeploymentDefaultsRequest(); getGlobalDeploymentDefaultsRequest.setWorkspace(workspaceName); getGlobalDeploymentDefaultsRequest.setNamespace(namespace); System.out.println(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString())
 ResultModel<GetGlobalDeploymentDefaultsResp> globalDefaults =
JsonUtil.toBean(client.doAction(getGlobalDeploymentDefaultsRequest).getHttpContentString(), new TypeReference<ResultModel<GetGlobalDeploymentDefaultsResp>>() {
 });
System.out.println(JsonUtil.toJson(globalDefaults.getData()));
 Deployment.DeploymentSpec spec =
globalDefaults.getData().getSpec();
 spec.setState(DeploymentState.RUNNING);
```

`// SQL`作业

```
 Artifact.SqlScriptArtifact
sqlScriptArtifact = new Artifact.SqlScriptArtifact();
 sqlScriptArtifact.setSqlScript("INSERT INTO
PRINT_TABLE SELECT /* comments */ UPPER(name) FROM RANDOM_TABLE"); spec.getTemplate().getSpec().setArtifact(sqlScriptArtifact);
```

`//` 创建`DataStream`作业只需要传入不同的`Artifact`即可

```java
 Artifact.JarArtifact jarArtifact = new
Artifact.JarArtifact();
 jarArtifact.setJarUri("oss://qiqi-zp/multioss/artifacts/namespaces/test/job-1.0-SNAPSHOT2.j
ar");
 // spec.getTemplate().getSpec().setArtifact(jarArtifact);
createDeploymentParams = new CreateDeploymentParams();
 Deployment.DeploymentMetadata metadata = new
Deployment.DeploymentMetadata();
 metadata.setName("lxg-sdk-sql-test-5");
 spec.setDeploymentTargetId("3965ca94-2fa9-47ee-818b-ff89ddf4ba4f");
createDeploymentParams.setMetadata(metadata);
 createDeploymentParams.setSpec(spec);
createDeploymentRequest = new CreateDeploymentRequest();
 createDeploymentRequest.setWorkspace(workspaceName);
createDeploymentRequest.setNamespace(namespace);
 String paramsStr = JsonUtil.toJson(createDeploymentParams);
 System.out.printf("##########params:\n%s\n", paramsStr);
createDeploymentRequest.setParamsJson(paramsStr);
 createDeploymentRequest.setHttpContentType(FormatType.JSON);
System.out.println(client.doAction(createDeploymentRequest).getHttpContentString()); JsonUtil.toBean(client.doAction(createDeploymentRequest).getHttpContentString(), new TypeReference<ResultModel<CreateDeploymentResp>>() {
 });
System.out.println(JsonUtil.toJson(createDeploymentRespResultModel));
```

获取列表实时计算（流计算） API `//` 获取`artifacts`列表

```java
 ListArtifactsRequest listArtifactsRequest = new
ListArtifactsRequest(); listArtifactsRequest.setWorkspace(workspaceName); listArtifactsRequest.setNamespace(namespace); JsonUtil.toBean(client.doAction(listArtifactsRequest).getHttpContentString(), new TypeRefere
 });
System.out.println(JsonUtil.toJson(artifacts));
```

`//` 获取`artifact`

```java
getArtifactMetadataRequest = new GetArtifactMetadataRequest();
 getArtifactMetadataRequest.setWorkspace(workspaceName);
getArtifactMetadataRequest.setNamespace(namespace); getArtifactMetadataRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar"); System.out.println(client.doAction(getArtifactMetadataRequest).getHttpContentString());
 ResultModel<GetArtifactMetadataResp> artifact =
JsonUtil.toBean(client.doAction(getArtifactMetadataRequest).getHttpContentString(), new TypeReference<ResultModel<GetArtifactMetadataResp>>() {
 });
System.out.println(JsonUtil.toJson(artifact));
```

`//` 删除`artifact`

```java
 DeleteArtifactRequest deleteArtifactRequest
= new DeleteArtifactRequest(); deleteArtifactRequest.setWorkspace(workspaceName); deleteArtifactRequest.setNamespace(namespace);
 deleteArtifactRequest.setFilename("flip-75-demo-1.0-SNAPSHOT-1.jar");
deleteArtifactResponse = client.getAcsResponse(deleteArtifactRequest); System.out.println(JsonUtil.toJson(deleteArtifactResponse));
```

`//` 获取`deployments`列表

```java
 ListDeploymentsRequest listDeploymentsRequest
= new ListDeploymentsRequest(); listDeploymentsRequest.setWorkspace(workspaceName); listDeploymentsRequest.setNamespace(namespace);
 ResultModel<ListDeploymentsResp> deployments =
JsonUtil.toBean(client.doAction(listDeploymentsRequest).getHttpContentString(), new TypeReference<ResultModel<ListDeploymentsResp>>() {
 });
System.out.println(JsonUtil.toJson(deployments));
```

`//` 删除`deployment` 指定已存在的且状态为`CANCELLED`的`DeploymentId`

```java
deleteDeploymentRequest = new DeleteDeploymentRequest(); deleteDeploymentRequest.setWorkspace(workspaceName); deleteDeploymentRequest.setNamespace(namespace); deleteDeploymentRequest.setDeploymentId(deploymentId); deleteDeploymentResponse = client.getAcsResponse(deleteDeploymentRequest); System.out.println(JsonUtil.toJson(deleteDeploymentResponse));
```

#### pom.xml

实时计算（流计算） API

```xml
<?xml version="1.0" encoding="UTF-8"?> <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-
4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.aliyun</groupId>
    <artifactId>vvp-sdk-sample-java</artifactId>
    <version>0.0.1</version>
    <properties>
        <junit.version>4.12</junit.version>
        <slf4j.version>1.7.25</slf4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.3</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.25</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-ververica</artifactId>
            <version>0.0.3-SNAPSHOT</version>
            <classifier>shaded</classifier>
        </dependency>
</dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>8</source>
                    <target>8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

实时计算（流计算）

## Flink SQL参考

### 概述

Flink SQL是实时计算为简化实时计算模型，降低用户使用实时计算门槛而设计的一套符合标准SQL语义的实时计算SQL。Flink SQL有以下优势： 开发成本低。使用阿里云Flink SQL，可以不再编写长达数千行的Storm代码，通过一两句简单的SQL即可描述复杂且多变的业务逻辑。 维护成本低。使用阿里云Flink SQL，可以不用再维护数千行的Storm代码。 使用最原始的Storm编程模式，您必须考虑各类系统异常情况，包括系统异常、系统宕机、错误情况下数据准确性等各类细节问题。 阿里云团队将上述各类问题均在SQL语义中进行抽象和解决。实时计算具备以下特点。 数据的准确性。实时计算独特的Exactly-Once Processing语义保证，能够保证各种Failover场景的数据准确性。 性能的可优化性。实时计算集成SQL优化逻辑，将SQL翻译为最底层的执行代码的普通人员编写的Storm代码，效率更高，提高编写SQL代码的效率。 编程的可扩展性。实时计算支持UFD的扩展功能，对于SQL无法表达的、或者业务定制化逻辑，阿里实时计算通过自定义UFD进行功能扩展。 系统的可扩展性。实时计算在保证任务和系统稳定性同时，在数据突增时（如，双11）可以做到弹性扩容。

### 关键字

本文为您介绍Flink关键字。 Flink V1.11关键字详情，请参见Reserved Keywords。 如果您需要在DDL中定义Flink关键字，请在关键字两端添加反引号（`），例如｀`value`｀。

**说明**

### 创建数据视图

**背景信息**

通常，业务逻辑比较复杂，需要将多层嵌套写在DML语句中，但是这种方式定位问题比较困难。此时，您可以通过定义数据视图的方式，将多层嵌套写在数据视图中，简化开发过程。

**说明**

数据视图仅用于辅助计算逻辑的描述，不会产生数据的物理存储。

**语法**

```
CREATE TEMPORARY VIEW viewName AS [ (columnName[ , columnName]* ) ] queryStatement;
```

viewName：视图名称。 columnName：字段名称。 queryStatement：嵌套语句别名。

**示例**

实时计算（流计算）

```
CREATE TEMPORARY VIEW tmp_view AS SELECT
```

*

```
FROM
    datagen_source;
    rds_output
SELECT
```

`r,` `t,` `c,` u

```
FROM
    tmp_view;
```

### 基本概念

#### Watermark

实时计算可以基于时间属性对数据进行窗口聚合。基于Event Time时间属性的窗口函数作业中，数据源表的声明 WATERMARK 定义了表的事件时间属性，其形式为WATERMARK FOR rowtime_column_name ASwatermark_strategy_expression。rowtime_column_name把一个现有的列定义为一个为表标记事件时间的属性。该列的类型必须为 TIMESTAMP(3)，且是 schema 中的顶层列，它也可以是一个计算列。 watermark_strategy_expression定义了watermark的生成策略。它允许使用包括计算列在内的任意非查询表达式来计算watermark，表达式的返回类型必须是TIMESTAMP(3)，表示了从Epoch以来的经过的时间。返回的 watermark只有当其不为空且其值大于之前发出的本地watermark时才会被发出（以保证 watermark 递增）。每条记录的watermark生成表达式计算都会由框架完成。框架会定期发出所生成的最大的watermark， 如果当前watermark仍然与前一个watermark相同、为空、或返回的 watermark 的值小于最后一个发出的 watermark，则新的 watermark不会被发出。Watermark根据pipeline.auto-watermark-interval中所配置的间隔发出。若watermark的间隔是0ms，那么每条记录都会产生一个watermark，且watermark会在不为空使用事件时间语义时，表必须包含事件时间属性和 watermark 策略。Flink提供了几种常用的watermark策略： 严格递增时间戳：WATERMARK FOR rowtime_column AS rowtime_column。 发出到目前为止已观察到的最大时间戳的watermark，时间戳大于最大时间戳的行被认为没有迟到。 递增时间戳：WATERMARK FOR rowtime_column AS rowtime_column -INTERVAL '0.001' SECOND。 发出到目前为止已观察到的最大时间戳减1的watermark，时间戳大于或等于最大时间戳的行被认为没有迟到。 有界乱序时间戳：WATERMARK FOR rowtime_column AS rowtime_column- INTERVAL 'string' timeUnit。 发出到目前为止已观察到的最大时间戳减去指定延迟的watermark，例如， WATERMARK FOR rowtime_column AS rowtime_column - INTERVAL '5'SECOND是一个5秒延迟的watermark策略。

```
CREATE TABLE Orders (
 user BIGINT,
 product STRING,
 order_time TIMESTAMP(3),
 WATERMARK FOR order_time AS order_time -INTERVAL '5' SECOND
) WITH ( . . . );
```

实时计算（流计算） Watermark含义是所有时间戳 `t'< t` 的事件都已经发生。假如watermark t 已经生效，那么后续Event Time小于 t 的记录都会被丢弃掉（目前实时计算的处理方式是丢弃这些来的更晚的数据，后续支持用户配置让更晚的数据也能继续更新）。 针对乱序的流，watermark至关重要。即使一些事件延迟到达，也不至于过于影响窗口计算的正确性。 并行数据流中，当算子（Operator）有多个输入流时，算子的Event Time以最小流Event Time为准。

#### 计算列

计算列可以使用其它列的数据，计算出其所属列的数值。如果您的数据源表中没有TIMESTAMP类型的列，可以使用计算列方法从其它类型的字段进行转换。

**计算列概念**

计算列是虚拟列，并非实际存储在表中。计算列可以通过表达式、内置函数、或是自定义函数等方式，使用其它列的数据，计算出其所属列的数值。计算列在Flink SQL中可以像普通字段一样被使用。

**计算列的用途**

目前Watermark的Event Time（也称为rowtime）列只支持TIMESTAMP类型（未来会支持LONG类型）。 watermark只能定义在源表DDL中，如果您的源表中没有TIMESTAMP类型的列，可以使用计算列从其他类型的字段进行转换。

**计算列语法**

```
column_name AS computed_column_expression
```

**计算列示例**

watermark的rowtime必须是TIMESTAMP数据类型。当前实时计算支持毫秒级别的、在Unix时间戳里是13位 TIMESTAMP数据类型。如果DataHub的TIME字段是微秒级别的（16位Unix时间戳），可以用计算列方法转换为13位的时间戳，如下所示。

```
CREATE TABLE test_stream(
  a INT,
  b BIGINT,
  `TIME` BIGINT,
```

`ts AS TO_TIMESTAMP(TIME/1000), --`利用计算列，将`16`位时间戳转换为`13`位时间戳。

```
) WITH (
  'connector' = 'datahub',
  ...
);
```

实时计算（流计算）

| TIME |  |
|---|---|
|  | ts |

#### 时间属性

本文为您介绍Flink SQL支持的Event Time和Processing Time数据类型。 Flink SQL支持2种时间类型Event Time和Processing Time。 Event Time：您提供的事件时间（通常是数据的最原始的创建时间），Event time必须是您提供在Schema 里的数据。 Processing Time：系统对事件进行处理的本地系统时间。 下图是不同时间属性在实时计算流程中的位置。 从上图的定义可以看出，Ingestion Time和Processing Time是系统为流式记录增加的时间属性，您并不能控制。Event Time则是流记录本身携带的时间属性。由于数据本身存在乱序以及网络抖动等其它原因，Event Time为t1（对应partition1）时刻的纪录，有可能会晚于t2（对应prtition2）时刻的被Flink处理，即t2 > t1。

**Event Time**

EventTime也称为rowtime。EventTime时间属性必须在源表DDL中声明，可以将源表中的某一字段声明成 EventTime。目前只支持将TIMESTAMP类型（将来会支持 LONG 类型）声明成rowtime字段。如果不是 TIMESTAMP类型，需要借助计算列，基于现有列构造出一个TIMESTAMP类型的列。 但由于数据本身会有乱序，加之网络抖动或其它原因，数据到达的顺序和被处理的顺序可能是不一致的（乱序）。因此定义一个rowtime字段，需要显示地定义一个Watermark计算方法。 窗口函数基于Event Time聚合的示例如下。 实时计算（流计算）

```
CREATE TABLE tt_stream(
  a VARCHAR,
  b VARCHAR,
  c TIMESTAMP,
  WATERMARK wk1 FOR c as withOffset(c, 1000)  --watermark计算方法
) WITH (
  'connector' = 'sls',
  'topic' = 'yourTopicName',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
); CREATE TABLE rds_output(
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) WITH (
  'connector' = 'rds',
  'url' = 'jdbc:mysql://****3306/test',
  'tableName' = 'yourTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
); INSERT INTO rds_output SELECT a AS id,
     SESSION_START(c, INTERVAL '1' SECOND) AS c,
     CAST(SESSION_END(c, INTERVAL '1' SECOND) AS TIMESTAMP) AS f,
     COUNT(a) AS cnt
FROM tt_stream GROUP BY SESSION(c, INTERVAL '1' SECOND), a
```

**Processing Time**

Processing Time是系统产生的，不在您的原始数据中，您需要在数据源表的声明中显式的定义一个Processing Time列。

```
filedName as PROCTIME()
```

窗口函数基于Processing Time聚合的示例如下。 实时计算（流计算）

```
CREATE TABLE mq_stream (
  a VARCHAR,
  b VARCHAR,
  c BIGINT,
```

`d AS PROCTIME() ---`在数据源表的声明中显式的定义一个`Processing Time`列。

```
) WITH (
  'connector' = 'mq',
  'topic' = 'yourTopic',
  'accessId' = 'yourAccessId',
  'accessKey' = 'yourAccessSecret'
); CREATE TABLE rds_output (
  id VARCHAR,
  c TIMESTAMP,
  f TIMESTAMP,
  cnt BIGINT
) with (
  'connector' = 'rds',
  'url' = 'yourDatebaseURL',
  'tableName' = 'yourDatabasTableName',
  'userName' = 'yourUserName',
  'password' = 'yourPassword'
); INSERT INTO rds_output SELECT a AS id,
     SESSION_START(d, INTERVAL '1' SECOND) AS c,
     SESSION_END(d, INTERVAL '1' SECOND) AS f,
     COUNT(a) AS cnt
FROM mq_stream GROUP BY SESSION(d, INTERVAL '1' SECOND), a
```

**时间属性字段传递**

目前，时间属性字段经过如下两种操作后会失去时间属性： 非window的group by 双流join 如果经过以上两种操作后，继续使用该时间属性字段进行窗口函数运算会出现类

```
似 org.apache.flink.table.api.ValidationException: Window can only be defined over a time
```

`attribute column.` 的报错。

### DDL语句

#### 创建数据源表

##### 日志服务SLS源表

本文为您介绍日志服务SLS源表的DDL定义、WITH参数、类型映射、属性字段和代码示例。

**什么是日志服务**

实时计算（流计算） 日志服务SLS是针对日志类数据的一站式服务。日志服务可以帮助您快捷地完成数据采集、消费、投递以及查询分析，提升运维和运营效率，建立海量日志处理能力。

**前提条件**

已创建日志服务Project和Logstore。

**使用限制**

仅VVR 2.0.0及以上版本支持日志服务SLS Connector。

**DDL定义**

```
create table sls_source(
  a int,
  b int,
  c varchar
) with (
  'connector' = 'sls',
  'endPoint' = '<yourEndPoint>',
  'accessId' = '<yourAccessId>',
  'accessKey' = '<yourAccessKey>',
  'startTime' = '<yourStartTime>',
  'project' = '<yourProjectName>',
  'logStore' = '<yourLogStoreName>',
  'consumerGroup' = '<yourConsumerGroupName>'
);
```

**说明**

SLS暂不支持MAP类型的数据。 SLS对于不存在字段会置为Null。 DDL定义中字段顺序可以为无序，建议和物理表中字段顺序保持一致。

**WITH参数**

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 源表类型。 | 是 | 固定值为 sls 。 |
| endPoint | 消费端点信息。 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID。 | 是 | 无。 |
| accessKey | AccessKey Secret。 | 是 | 无。 |
| project | SLS项目名称。 | 是 | 无。 |
| logStore | LogStore名称。 | 是 | 无。 |
| startTime | 消费日志的开始时间。 | 是 | 无。 |
| consumerGroup | 消费组名称。 | 否 | 您可以自定义消费组名（没有固定格式）。 |

实时计算（流计算）

| batchGetSize | 单次读取logGroup的条数。 | 否 | 默认值为100。 说明 batchGetSize设置不能超过 1000，否则会报错。 batchGetSize设置单次读取logGroup的条数。如果单条 logItem的大小和batchGetSize都很大，则可能会导致频繁的垃圾回收 （Garbage Collection），您可以适当减小batchGetSize参数值。 |
|---|---|---|---|

**类型映射**

日志服务和Flink字段类型对应关系如下。建议您使用该对应关系进行DDL声明。

| 日志服务字段类型 | Flink字段类型 |
|---|---|
| STRING | VARCHAR |

**属性字段**

|  | 字段名 |  | 字段类型 | 说明 |
|---|---|---|---|---|
|  | source __ __ |  | STRING METADATA VIRTUAL | 消息源。 |
|  | topic __ __ |  | STRING METADATA VIRTUAL | 消息主题。 |
|  | timestamp __ __ |  | BIGINT METADATA VIRTUAL | 日志时间。 |
|  |  | timestamp __ |  |  |
|  | __ |  |  |  |
|  | tag __ __ |  | MAP<VARCHAR, VARCHAR> METADATA VIRTUAL | 消息TAG。对于属性" tag : receive time ":"1616742274"，' __ __ __ _ __ __ receive time '和'1616742274'会被作为KV对，记录 _ __ 在Map中，在SQL中通过 tag [' receive time ']的方式访问。 __ __ __ _ __ |

|  |  | source __ __ |
|---|---|---|

仅在VVR 3.0.1版本及以后版本支持获取以上SLS属性字段。

**说明**

**代码示例**

实时计算（流计算）

```
create table sls_input(
  `time` bigint,
  `url` string,
  dt string,
  float_field float,
  double_field double,
  boolean_field boolean,
  `__topic__` STRING METADATA VIRTUAL,
  `__source__` STRING METADATA VIRTUAL,
  `__timestamp__` BIGINT METADATA VIRTUAL,
  proctime as PROCTIME()
) with (
  'connector' = 'sls',
  'endpoint' = '<yourEndPoint>',
  'accessid' = '<yourAccessId>',
  'accesskey' = '<yourAccessKey>',
  'starttime' = '2001-08-01 00:00:00',
  'project' = 'sls-test',
  'logstore' = 'sls-input'
);
```

##### 消息队列Kafka源表

**什么是Kafka源表**

消息队列Kafka版是阿里云提供的分布式、高吞吐、可扩展的消息队列服务。消息队列Kafka版广泛用于日志收集、监控数据聚合、流式数据处理、在线和离线分析等大数据领域。

**DDL定义**

```
create table kafka_source(
  user_id BIGINT,
  item_id BIGINT,
  category_id BIGINT,
  behavior STRING,
  ts TIMESTAMP(3)
) with (
  'connector' = 'kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'properties.group.id' = '<yourKafkaConsumerGroupId>',
  'format' = 'csv',
  'scan.startup.mode' = 'earliest-offset'
);
```

**WITH参数**

| 参数 | 说明 | 是否必选 | 数据类型 | 备注 |
|---|---|---|---|---|
| connector | 源表类型 | 是 | STRI NG | 固定值为 kafka 。 |

实时计算（流计算）

| topic | 源表对应的Topic | 是 | STRI NG | 无 |
|---|---|---|---|---|
| properties.bo otstrap.server s | Kafka Broker地址 | 是 | STRI NG | 请联系阿里云运维工程师获取。 |
| properties.gro up.id | Kafka消费组ID | 是 | STRI NG | 无 |
| format | Flink Kafka Connector在反序列化来自Kafka的消息时使用的格式。 | 是 | STRI NG | 格式取值如下： csv json avro debezium-json canal-json |
| scan.startup. mode | Kafka消费启动位点 | 否 | STRI NG | 启动位点取值如下： group-offsets（默认值）：根据Group 读取。 earliest-offset：从Kafka最早分区开始读取。 latest-offset：从Kafka最新位点开始读取。 timestamp：从Kafka指定时间点读取。 需要在WITH参数中指定scan.startup.timestamp-millis参数。 specific offsets：从Kafka指定分区指定 _ 偏移量读取。 需要在WITH参数中指定scan.startup.specific-offsets参数。 |
| scan.startup.s pecific-offsets | 在specific-offsets启动模式下，指定每个分区的启动偏移量。 | 否 | STRI NG | 例如：partition:0,offset:42;partition:1, offset:300 |
| scan.startup.ti mestamp- millis | 在timestamp启动模式下， 指定启动位点时间戳。 | 否 | LON G | 单位为毫秒。 |

如果您还需要直接配置Connector使用的Kafka Consumer，可以在Kafka Consumer配置参数前添加 `properties` 前缀，并将该Kafka Consumer配置信息追加至WITH参数。例如Kafka集群需要 SASL（Simple Authentication and Security Layer）认证。

```
CREATE TABLE kafkaTable (
    ...
) WITH (
    ...
    'properties.security.protocol' = 'SASL_PLAINTEXT',
    'properties.sasl.mechanism' = 'PLAIN',
    'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule
required username="USERNAME" password="PASSWORD";' );
```

Kafka Consumer配置项详情请参见 Consumer Configs。 实时计算（流计算）

**从kafka中读取数据后插入Kafka示例**

从名称为source的Topic中读取Kafka数据，再写入名称为sink的Topic，数据使用CSV格式。

```
CREATE TEMPORARY TABLE Kafka_source (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'kafka',
    'topic' = '<yourTopicName>',
    'properties.bootstrap.servers' = '<yourKafkaBrokers>',
    'properties.group.id' = '<yourKafkaConsumerGroupId>',
    'format' = 'csv'
); CREATE TEMPORARY TABLE Kafka_sink (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'kafka',
    'topic' = '<yourTopicName>',
    'properties.bootstrap.servers' = '<yourKafkaBrokers>',
    'properties.group.id' = '<yourKafkaConsumerGroupId>',
    'format' = 'csv'
); INSERT INTO Kafka_sink SELECT id, name, age FROM Kafka_source;
```

**常见问题**

Q：Flink中的COMMIT OFFSET有什么作用？ A：Flink默认采用**commitOffsetOnCheckpointing**，用户设置的Commit Offset策略不生效。只有开启**checkpoint**后，在每次**checkpoint**成功时，才会**commit**当前分区消费的**offset**至Kafka，以便在作业失败恢复过程中，从上一次**checkpoint**的**commit**位点开始消费，保证计算的Exactly Once。如果将**checkpoint**间隔设置过大，Kafka端可能会查询不到当前消费**offset**。

##### 数据总线DataHub源表

本文为您介绍数据总线DataHub源表的DDL定义、WITH参数、类型映射、属性字段和常见问题。

**什么是数据总线DataHub**

是流式数据（Streaming Data）的处理平台，提供对流式数据的发布（Publish）、订阅（Subscribe）和分发功能，让您可以轻松构建基于流式数据的分析和应用。

**前提条件**

已创建DataHub的Project和Topic，详情请参见创建Project和Topic。

**使用限制**

仅Flink计算引擎VVR 2.0.0及以上版本支持数据总线DataHub Connector。

**DDL定义**

实时计算（流计算）

```
create table datahub_source(
  name VARCHAR,
  age BIGINT,
  birthday BIGINT
) with (
  'connector' = 'datahub',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'subId' = '<yourSubId>',
  'accessId' = '<yourAccessId>',
  'accessKey' = '<yourAccessKey>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型。 | 是 | 固定值为 datahub 。 |
| endPoint | 消费端点信息。 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID。 | 是 | 无。 |
| accessKey | AccessKey Secret。 | 是 | 无。 |
| project | 项目名称。 | 是 | 无。 |
| topic | Topic名称。 | 是 | 无。 |
| subId | Topic的订阅ID。 | 是 | 多个任务不能同时使用同一个订阅。如何查看订阅ID，请参见查看订阅。 |
| startTime | 启动位点的时间。 | 否 | 格式为 yyyy-MM-dd hh:mm:ss 。 |
| retryTimeout | 最大持续重试时间。 | 否 | 单位为毫秒，默认值为1800000毫秒（半小时）。 |
| retryInterval | 重试间隔。 | 否 | 单位为毫秒，默认值为1000。 |
| maxFetchSize | 单次读取条数。 | 否 | 默认值为50。 |
| maxBufferSize | 异步读取的最大缓存数据条数。 | 否 | 默认值为50。 |

实时计算（流计算）

| lengthCheck | 单行字段条数检查策略。 | 否 | NONE（默认值）： 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过该行数据。 SKIP：解析出的字段数和定义字段数不同时跳过该行数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，按从左到右的顺序，在行尾用Null填充缺少的字段。 |
|---|---|---|---|
| columnErrorDe bug | 是否打开调试开关。 | 否 | false（默认值）：关闭调试功能。 true：打开调试开关，打印解析异常的日志。 |
| CompressType | 读写的压缩策略。 | 否 | lz4 （默认值）：使用lz4压缩。 deflate：使用deflate压缩。 ""（空字符串）：表示关闭数据压缩。 说明仅VVR 6.0.5及以上版本支持指定CompressType参数。 |
| fetchLatestDel ay | 数据源没有数据时，sleep 的时间。 | 否 | 单位为毫秒，默认值为500。在数据源频繁没有数据的情况下，影响吞吐，建议调小。 |

**类型映射**

DataHub和Flink字段类型对应关系如下，建议使用该对应关系进行DDL声明。

| DataHub字段类型 | Flink字段类型 |
|---|---|
| STRING | VARCHAR |
| TIMESTAMP | BIGINT |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INTEGER | INTEGER |

实时计算（流计算）

| BIGINT | BIGINT |
|---|---|
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |

**说明**

如果您DataHub中存储的是二进制BLOB类型数据时，则Flink字段需要声明为VARBINARY类型，与METAQ 类似。

**属性字段**

| 字段名 | 字段类型 | 说明 |
|---|---|---|
| shard-id | BIGINT METADATA VIRTUAL | Shard的ID。 |
| sequence | STRING METADATA VIRTUAL | 数据顺序。 |
| system-time | TIMESTAMP METADATA VIRTUAL | 系统时间。 |

**说明**

仅在VVR 3.0.1及以上版本支持获取以上DataHub属性字段。

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datahub_input (
  `time` BIGINT,
  `sequence`  STRING METADATA VIRTUAL,
  `shard-id` BIGINT METADATA VIRTUAL,
  `system-time` TIMESTAMP METADATA VIRTUAL
) WITH (
  'connector' = 'datahub',
  'subId' = '<yourSubId>',
  'endPoint' = '<yourEndPoint>',
  'project' = '<yourProjectName>',
  'topic' = '<yourTopicName>',
  'accessid' = '<yourAccessId>',
  'accesskey' = '<yourAccessKey>'
); CREATE TEMPORARY TABLE test_out (
  `time` BIGINT,
  `sequence`  STRING,
  `shard-id` BIGINT,
  `system-time` TIMESTAMP
) WITH (
  'connector' = 'print',
  'logger' = 'true'
); INSERT INTO test_out SELECT
  `time`,
  `sequence` ,
  `shard-id`,
  `system-time`
FROM datahub_input;
```

##### 全量MaxCompute源表

本文为您介绍全量MaxCompute源表DDL定义、WITH参数、类型映射和常见问题。

**DDL定义**

```
create table odps_source(
   id INT,
   user_name VARCHAR,
   content VARCHAR
) with (
   'connector' = 'odps',
   'endpoint' = '<yourEndpoint>',
   'tunnelEndpoint' = '<yourTunnelEndpoint>',
   'project' = '<yourProjectName>',
   'tablename' = '<yourTableName>',
   'accessid' = '<yourAccessKeyId>',
   'accesskey' = '<yourAccessKeySecret>',
   'partition' = 'ds=2018****'
);
```

实时计算（流计算） WITH参数需要全部小写。

**说明**

**WITH参数**

| 参数 | 说明 |  |  | 是否必填 | 备注 |
|---|---|---|---|---|---|
| connector | 源表类型 |  |  | 是 | 固定值为 odps 。 |
| endPoint | MaxCompute服务地址 |  |  | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoint | MaxCompute Tunnel服务的连接地址 |  |  | 否 | 请联系阿里云运维工程师获取。 |
| project | MaxCompute项目名称 |  |  | 是 | 无 |
| tableName | MaxCompute表名 |  |  | 是 | 无 |
| accessId | AccessKey ID |  |  | 是 | 无 |
| accessKey | AccessKey Secret |  |  | 是 | 无 |
| partition | 分区名 |  |  |  | 只存在一级分区的MaxCompute表例如，如果只存在1个分区列 ds ， 则 `partition` = 'ds=20180905' 表示读 ds=20180905 分区的数据。 ，值存在多级分区的MaxCompute表例如，如果存在2个分区列 ds 和 hh ， 则 `partition`='ds=20180905,hh=*' 表示读 ds=20180905 分区的数据。 说明分区过滤时需要声明所有分区的值。例如，上述示例中，只声明 `partition` = 'ds=20180905' ，则不会读取任何分区。 |
|  |  |  |  | 否 |  |

|  |  |  | `partition` = |  |
|---|---|---|---|---|
|  |  | 'ds=20180905' |  |  |

**类型映射**

| MaxCompute字段类型 | Flink字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INT | INT |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |

实时计算（流计算）

| BOOLEAN | BOOLEAN |
|---|---|
| DATETIME | TIMESTAMP |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |
| STRING | VARCHAR |

**代码示例**

```
CREATE TEMPORARY TABLE odps_source (
   cid varchar,
   rt DOUBLE
) with (
   'connector' = 'odps',
   'endpoint' = '<yourEndpointName>',
   'tunnelEndpoint' = '<yourTunnelEndpoint>',
   'project' = '<yourProjectName>',
   'tablename' = '<yourTableName>',
   'accessid' = '<yourAccessId>',
   'accesskey' = '<yourAccessPassword>',
   'partition' = 'ds=20180905'
); CREATE TEMPORARY TABLE blackhole_sink (
   cid varchar,
   invoke_count BIGINT
) with (
   'connector'='blackhole'
); INSERT INTO blackhole_sink SELECT
   cid,
   count(*) as invoke_count
FROM odps_source GROUP BY cid;
```

##### 增量MaxCompute源表

本文为您介绍增量MaxCompute源表DDL定义、WITH参数、类型映射和常见问题。

**DDL定义**

实时计算（流计算）

```
create table odps_source(
    id INT,
    user_name VARCHAR,
    content VARCHAR
) with (
    'connector' = 'continuous-odps',
    'endpoint' = '<yourEndpoint>',
    'tunnelEndpoint' = '<yourTunnelEndpoint>',
    'project' = '<yourProjectName>',
    'tablename' = '<yourTableName>',
    'accessid' = '<yourAccessKeyId>',
    'accesskey' = '<yourAccessKeySecret>',
    'startpartition' = 'ds=2018****'
);
```

**说明**

WITH参数需要全部小写。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型 | 是 | 固定值为 continuous-odps 。 |
| endPoint | MaxCompute服务本身的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoin t | MaxCompute Tunnel服务的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | 表所属的project名称 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |

实时计算（流计算）

| startPartition | 指定读取的起始分区。系统加载分区列表时，会把每个分区列表的所有分区和startPartition按照字母顺序进行比较，加载满足条件的分区的数据。 此外，增量MaxCompute源表可以持续监听增量MaxCompute分区表。读完已有的分区后，任务不会退出，且持续监听并读入新分区。 说明增量MaxCompute源表中必须存在一级分区，二级分区可选。 如果指定二级分区，必须写在一级分区的后面。 如果startPartition指定的分区不存在，系统会从下一个分区开始读取数据。 | 是 | 例如，指定startPartition 是ds=20191201，表示加载增量 MaxCompute表里所有满足ds >= 20191201的分区数据。 如果一个增量MaxCompute分区表， 有一级分区ds和二级分区type两个分区列，假设表里有以下5个分区： ds=20191201,type=a ds=20191201,type=b ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c 不同startPartition，满足分区的列表如下： ds=20191202 ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c ds=20191201,type=c ds=20191202,type=a ds=20191202,type=b ds=20191202,type=c |
|---|---|---|---|

**类型映射**

| MaxCompute字段类型 | Flink字段类型 |
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

实时计算（流计算）

**重要**

增量MaxCompute源表暂不支持CHAR、VARCHAR、ARRAY、MAP和STRUCT数据类型。 您可以临时使用STRING替换VARCHAR。

**代码示例**

增量MaxCompute源表每天产生一个分区，分区列是ds，从**ds=20191201**分区开始，加载后续的所有分区， 并一直监听新分区的产生。 `--`读增量`MaxCompute`表，读取的分区范围是`[ds=20191201`，∞)。

```
CREATE TEMPORARY TABLE odps_source (
    cid VARCHAR,
    rt DOUBLE
) with (
    'connector' = 'continuous-odps',
    'endpoint' = '<yourEndpoint>',
    'tunnelEndpoint' = '<yourTunnelEndpoint>',
    'project' = '<yourProjectName>',
    'tablename' = '<yourTableName>',
    'accessid' = '<yourAccessKeyId>',
    'accesskey' = '<yourAccessKeySecret>',
    'startpartition' = 'ds=2018****'
); CREATE TEMPORARY TABLE blackhole_sink (
    cid VARCHAR,
    rt DOUBLE
) WITH (
    'connector'='blackhole'
); INSERT INTO blackhole_sink SELECT
    cid, rt FROM odps_source;
```

##### 消息队列RocketMQ版源表

本文为您介绍消息队列RocketMQ版源表DDL定义、WITH参数、类型映射和代码示例。

**说明**

RocketMQ Connector可以作为Stream作业和Batch作业的源表使用。

**什么是消息队列RocketMQ版**

消息队列 RocketMQ版是阿里云基于Apache RocketMQ构建的低延迟、高并发、高可用和高可靠的分布式消息中间件。消息队列RocketMQ版既可为分布式应用系统提供异步解耦和削峰填谷的能力，同时也具备互联网应用所需的海量消息堆积、高吞吐和可靠重试等特性。

**DDL定义**

实时计算（流计算）

```
create table mq_source(
   x varchar,
   y varchar,
   z varchar
) with (
   'connector'='mq',
   'topic'='<yourTopicName>',
   'endpoint'='<yourEndpoint>',
   'pullIntervalMs'='1000',
   'accessId'='<yourAccessId>',
   'accessKey'='<yourAccessSecret>',
   'startMessageOffset'='1000',
   'consumerGroup'='<yourConsumerGroup>',
   'fieldDelimiter'='|'
);
```

MQ是非结构化存储格式的消息中间件，对于数据的Schema不提供强制定义，完全由业务层指

**说明**

定。Flink仅支持CSV和二进制格式的MQ消息。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型 | 是 | 固定值为 mq 。 |
| topic | topic名称 | 是 | 无 |
| endPoint | endPoint地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| consumerGroup | 订阅消费group名称 | 是 | 无 |
| pullIntervalMs | 拉取时间间隔 | 是 | 单位为毫秒。 |
| nameServerSubgr oup | NameServer组 | 否 | 内网服务（阿里云经典网络/VPC）：必须配置'nameServerSubgroup' = 'nsaddr4client-internal' 公网服务：无需配置nameServerSubgroup 说明仅VVR 2.1.1及以上版本支持该参数。 |
| startTime | 消息消费启动的时间点 | 否 | 无 |
| startMessageOffse t | 消息开始的偏移量 | 否 | 如果填写，将优先以startMessageoffset的位点开始加载数据。 |
| tag | 订阅的标签 | 否 | 无 |
| lineDelimiter | 解析Block时，行分隔符 | 否 | 默认值为 \n 。 |

实时计算（流计算）

| fieldDelimiter | 字段分隔符 | 否 | 默认值为 \u0001 。表示在只读模式下以 \u0001 （ \u0001 在只读模式不可见）作为分隔符，在编辑模式下以 ^A 作为分隔符。 |
|---|---|---|---|
| encoding | 编码格式 | 否 | 默认值为 utf-8 。 |
| lengthCheck | 单行字段条数检查策略 | 否 | 默认值为NONE，表示： 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，跳过这行数据。 其它可选值为SKIP、EXCEPTION和PAD。 SKIP：解析出的字段数和定义字段数不同时跳过这行数据。 EXCEPTION：解析出的字段数和定义字段数不同时提示异常。 PAD：按从左到右顺序填充。 解析出的字段数大于定义字段数时，按从左到右的顺序，取定义字段数量的数据。 解析出的字段数小于定义字段数时，在行尾用null填充缺少的字段。 |
| columnErrorDebug | 是否打开调试开关。 | 否 | 默认值为FALSE。如果设置为TRUE，则打印解析异常的Log。 |
| instanceID | 实例ID | 否 | 根据MQ实例是否有独立命名空间，执行如下操作： 是，必须配置instanceID参数。 否，不能配置instanceID参数。 |

|  | \u0001 |  |
|---|---|---|
| \u0001 |  |  |

**类型映射**

| MQ字段类型 | Flink字段类型 |
|---|---|
| STRING | VARCHAR |

**代码示例**

CSV格式假设您的1条CSV格式消息记录如下。

```
1,name,male 2,name,female
```

**说明**

1条MQ消息可以包括0条到多条数据记录，记录之间使用 \n 分隔。 Flink作业中，声明MQ数据源表的DDL如下。 实时计算（流计算）

```
create table mq_source(
   id varchar,
   name varchar,
   gender varchar
) with (
   'connector'='mq',
   'topic'='<yourTopicName>',
   'endpoint'='<yourEndpoint>',
   'pullIntervalMs'='1000',
   'accessId'='<yourAccessId>',
   'accessKey'='<yourAccessSecret>',
   'startMessageOffset'='1000',
   'consumerGroup'='<yourConsumerGroup>',
   'fieldDelimiter'='|'
);
```

二进制格式

```
create table mq_source (
   mess varbinary
) with (
   'connector'='mq',
   'endpoint'='<yourEndpoint>',
   'pullIntervalMs'='500',
   'accessId'='<yourAccessId>',
   'accessKey'='<yourAccessSecret>',
   'topic'='<yourTopicName>',
   'consumerGroup'='<yourConsumerGroup>'
);
```

##### 交互式分析Hologres源表

本文为您介绍交互式分析Hologres源表DDL定义、WITH参数、代码示例和类型映射。

**什么是交互式分析Hologres**

交互式分析Hologres兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析处理PB级数据，让您轻松使用现有BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**DDL定义**

```
create table hologres_source(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username'='<yourAccessID>',
  'password'='<yourAccessSecret>',
  'endpoint'='<yourEndpoint>',
```

'field_delimiter'='|' --该参数可选。

```
);
```

实时计算（流计算）

**说明**

Flink不支持源表中定义计算列。 Flink以批模式读取Hologres源表数据，即只扫描一次Hologres全表，扫描结束，消费结束，新到 Hologres源表的数据不会被读取。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型 | 是 | 固定值为hologres。 |
| dbname | 数据库名称 | 是 | 无。 |
| tablename | 表名称说明如果Schema不为 Public时，则tableName需要填写为schema.tableName。 | 是 | 无。 |
| username | 用户名，请填写阿里云账号的 AccessKey ID。 | 是 | 无。 |
| password | 密码，请填写阿里云账号的AccessKey Secret。 | 是 | 无。 |
| endpoint | Hologres端点 | 是 | 请联系阿里云运维工程师获取。 |
| field delimiter _ | 导出数据时，不同行之间使用的分隔符。 说明只有在bulkread = true时有效。 | 否 | 默认值为"\u0002"。 |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE hologres_source (
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username'='<yourAccessID>',
  'password'='<yourAccessSecret>',
  'endpoint'='<yourEndpoint>',
```

'field_delimiter'='|' --该参数可选。

```
); CREATE TEMPORARY TABLE blackhole_sink(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  'connector'='blackhole'
); INSERT INTO blackhole_sink SELECT
   name, age, birthday
from hologres_source;
```

**类型映射**

交互式分析Hologres和Flink字段类型对应关系如下，建议使用该对应关系进行DDL声明。

| Hologres字段类型 | Flink字段类型 |
|---|---|
| INT | INT |
| INT[] | ARRAY |
| BIGINT | BIGINT |
| BIGINT[] | ARRAY |
| REAL | FLOAT |
| REAL[] | ARRAY |
| DOUBLE PRECISION | DOUBLE |
| DOUBLE PRECISION[] | ARRAY |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY |
| TEXT | VARCHAR |
| TEXT[] | ARRAY |
| NUMERIC | DECIMAL |

实时计算（流计算）

| DATE | DATE |
|---|---|
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

##### 全量Elasticsearch源表

本文为您介绍全量Elasticsearch（ES）源表DDL定义、WITH参数、类型映射和代码示例。

**重要**

仅支持Elasticsearch 5.5及以上版本。 仅支持全量Elasticsearch源表，不支持增量Elasticsearch源表。 DDL中的字段均对应Elasticsearch文档中的字段，不支持将文档ID写入表中。

**DDL定义**

```
 CREATE TABLE elasticsearch_source(
   name STRING,
   location STRING,
   `value` FLOAT
) WITH (
   'connector' ='elasticsearch',
   'endPoint' = '<yourEndPoint>',
   'accessId' = '<yourAccessId>',
   'accessKey' = '<yourAccessSecret>',
   'indexName' = '<yourIndexName>',
   'typeNames' = '<yourTypeName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型 | 是 | 固定值为 elasticsearch 。 |
| endPoint | Server地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | Elasticsearch实例的用户名 | 否 | 无 |
| accessKey | Elasticsearch实例的密码 | 否 | 无 |
| indexName | 文档索引名称 | 是 | 无 |
| typeNames | Type名称 | 否 | 默认值为 doc 。 _ 说明 Elasticsearch 7.0以上版本不建议设置该参数。 |
| batchSize | 每个scroll请求从 Elasticsearch集群获取的最大文档数 | 否 | 默认值为2000。 |
| keepScrollAliveSec s | scroll上下文保留的最长时间 | 否 | 单位为秒，默认值为3600。 |

实时计算（流计算）

**类型映射**

Flink以JSON来解析Elasticsearch数据，详情请参见数据类型映射关系。

**代码示例**

```
CREATE TEMPORARY TABLE elasticsearch_source (
   name STRING,
   location STRING,
   `value` FLOAT
) WITH (
   'connector' ='elasticsearch',
   'endPoint' = '<yourEndPoint>',
   'accessId' = '<yourAccessId>',
   'accessKey' = '<yourAccessSecret>',
   'indexName' = '<yourIndexName>',
   'typeNames' = '<yourTypeName>'
); CREATE TEMPORARY TABLE blackhole_sink (
   name STRING,
   location STRING,
   `value` FLOAT
) WITH (
   'connector' ='blackhole'
); INSERT INTO blackhole_sink SELECT name, location, `value` FROM elasticsearch_source;
```

##### Postgres的CDC源表（公测中）

本文为您介绍Postgres的CDC（Change Data Capture）源表DDL定义、WITH参数、类型映射和代码示例。 Postgres的CDC源表正处于公测中，如果您对作业稳定性要求较高时，建议不要使用Postgres

**重要**

的CDC源表。

**什么是Postgres的CDC源表**

Postgres的CDC源表，即Postgres的流式源表，用于依次读取PostgreSQL数据库全量快照数据和变更数据，保证不多读一条也不少读一条数据。即使发生故障，也能采用Exactly Once方式处理。 如果您使用的是开源的PostgreSQL数据库，Postgres CDC connector支持读取的Postgres版

**说明**

本为9.6及以上版本。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE postgrescdc_source (
  shipment_id INT,
  order_id INT,
  origin STRING,
  destination STRING,
  is_arrived BOOLEAN
) WITH (
  'connector' = 'postgres-cdc',
  'hostname' = '<yourHostname>',
  'port' = '5432',
  'username' = '<yourUserName>',
  'password' = '<yourPassWord>',
  'database-name' = '<yourDatabaseName>',
  'schema-name' = '<yourSchemaName>',
  'table-name' = '<yourTableName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 数据类型 | 备注 |
|---|---|---|---|---|
| connecto r | 源表类型 | 是 | STRING | 固定值为 postgres-cdc 。 |
| hostnam e | Postgres数据库的IP地址或者 Hostname。 | 是 | STRING | 无 |
| usernam e | Postgres数据库服务的用户名。 | 是 | STRING | 无 |
| password | Postgres数据库服务的密码 | 是 | STRING | 无 |
| database -name | 数据库名称 | 是 | STRING | 数据库名称支持正则表达式以读取多个数据库的数据。 |
| schema- name | Postgres Schema名称 | 是 | STRING | Schema名称支持正则表达式以读取多个Schema的数据。 |
| table- name | Postgres表名 | 是 | STRING | 表名支持正则表达式去读取多个表的数据。 |
| port | Postgres数据库服务的端口号 | 否 | INTEGER | 默认值为5432。 |

实时计算（流计算）

| decoding .plugin.n ame | Postgres Logical Decoding插件名称 |  | 否 | STRING | 根据Postgres服务上安装的插件确定。支持的插件列表如下： decoderbufs（默认值） wal2json wal2json rds _ wal2json streaming _ wal2json rds streaming _ _ pgoutput 说明如果您使用的是阿里云RDS PostgreSQL，你需要开启逻辑解码（wal2json） 功能 |  |  |
|---|---|---|---|---|---|---|---|
| debeziu m.* | Debezium属性参数 |  | 否 | STRING | 更细粒度控制Debezium客户端的行为。例如 'debezium.snapshot.mode' = 'never' ， 详情请参见配置属性。 说明建议每个表都设置 debezium.slot.name 参数，以避免出现 PSQLException: ERROR: replication slot "debezium" is active for PID 974 报错。 |  |  |
|  |  |  |  |  |  | slot "debezium" is active for PID |  |
|  |  |  |  |  |  | 974 |  |

**类型映射**

Postgres CDC和Flink字段类型对应关系如下。

| Postgres CDC字段类型 | Flink字段类型 |
|---|---|
| SMALLINT | SMALLINT |
| INT2 |  |
| SMALLSERIAL |  |
| SERIAL2 |  |
| INTEGER | INT |
| SERIAL |  |
| BIGINT | BIGINT |
| BIGSERIAL |  |
| BIGINT | BIGINT |
| REAL | FLOAT |
| FLOAT4 |  |
| FLOAT8 | DOUBLE |
| DOUBLE PRECISION |  |
| NUMERIC(p, s) | DECIMAL(p, s) |

| 实时计算（流计算） | Flink企业版开发指南·Flink SQL参考 |
|---|---|
| DECIMAL(p, s) |  |
| BOOLEAN | BOOLEAN |
| DATE | DATE |
| TIME [(p)] [WITHOUT TIMEZONE] | TIME [(p)] [WITHOUT TIMEZONE] |
| TIMESTAMP [(p)] [WITHOUT TIMEZONE] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| CHAR(n) | STRING |
| CHARACTER(n) |  |
| VARCHAR(n) |  |
| CHARACTER VARYING(n) |  |
| TEXT |  |
| BYTEA | BYTES |

##### MySQL的CDC源表（公测中）

本文为您介绍MySQL的CDC（Change Data Capture）源表DDL定义、WITH参数、类型映射和代码示例。

**重要**

MySQL的CDC源表正处于公测中，如果您对作业稳定性要求较高时，建议不要使用MySQL的CDC源表。 本文仅适用于VVP 2.3.0及以上版本。 仅支持单并发消费CDC-MySQL数据。 在全量读取MYSQL CDC源表时，Checkpoint不生效，因此读取全量MYSQL CDC源表时，不建议开启自动调优。 MySQL CDC 源表目前不支持定义Watermark。如果您需要进行窗口聚合，您可以采用非窗口聚合

**什么是MySQL的CDC源表**

MySQL的CDC源表，即MySQL的流式源表，支持对MySQL数据库的全量和增量读取，并保证Exactly Once， 不多读一条也不少读一条数据。其工作机制是，在启动扫描全表前，先加一个全局读锁（FLUSH TABLES WITH READ LOCK），然后获取此时的Binlog位点以及表的schema，紧接着释放全局读锁。随后开始扫描全表，当全表数据读取完后，会从之前获取的Binlog位点获取增量的变更记录。在Flink作业运行期间会周期性执行 checkpoint，记录下Binlog位点，当作业发生Failover，便会从之前记录的Binlog位点继续处理，从而实现 Exactly Once语义。 MySQL的CDC源表需要一个有特定权限（包括SELECT、RELOAD、SHOW DATABASES、

**说明**

REPLICATION SLAVE和REPLICATION CLIENT）的MySQL用户，才能读取全量和增量数据。MySQL CDC Connector支持读取的MySQL版本为5.7和8.0。

**注意事项**

建议对MySQL用户授予RELOAD权限如果您未对MySQL用户授予RELOAD权限，则全局读锁会降级为表级读锁，而使用表级读锁需要等到全表扫描完成，才能释放锁，所以持锁时间会较长，而读锁会阻塞往表内写入数据，影响线上业务。 全局读锁（FLUSH TABLES WITH READ LOCK）的影响实时计算（流计算） 全局读锁阶段会去获取Binlog位点以及表的Schema，因此其持锁耗时与表的数量成正比，数据库持锁耗时可能达到秒级，例如上千张表大概两三秒。而读锁是会阻塞写入操作，因此仍可能对线上业务造成影响。如果您希望跳过锁阶段，且能容忍非Exactly Once语义，则可以通过增加 `'debezium.snapshot.locking.mode' =` `'none'` 属性来显式跳过锁阶段。 每个作业需显式配置不同的SERVER ID 每个同步数据库数据的客户端，都会有一个唯一ID，即SERVER ID。MySQL SERVER会根据该ID来维护网络连接以及Binlog位点。因此如果有大量不同的SERVER ID的客户端一起连接MySQL SERVER，可能导致 MySQL SERVER的CPU陡增，影响线上业务稳定性。此外，多个作业共享相同的SERVER ID，会导致Binlog 位点错乱，多读或少读数据。因此建议您通过动态Hints，在每个CDC作业都配置上不同的SERVER ID，例如 SELECT * FROM source_table /*+ OPTIONS('server-id'='123456') */ ; 。动态Hints详情请参见动态Hints。 全表扫描阶段无法执行checkpoint 在扫描全表数据时，没有可用于恢复的位点，所以无法在全表扫描阶段去执行checkpoint。为了不执行 checkpoint，MySQL的CDC源表会让执行中的checkpoint一直等待，甚至checkpoint超时（如果表超级大，扫描耗时非常长时）。超时的checkpoint会被认为是failed checkpoint，Flink默认配置下，会触发Flink 的Failover。因此建议当表超大时，为了避免因为checkpoint超时而导致作业失败，可以配置如下作业参数：

```
execution.checkpointing.interval: 10min # checkpoint间隔时间 execution.checkpointing.tolerable-failed-checkpoints: 100 #checkpoint失败容忍次数 restart-strategy: fixed-delay #重试策略 restart-strategy.fixed-delay.attempts: 2147483647 #重试次数
```

**DDL定义**

```
CREATE TABLE mysqlcdc_source (
  order_id INT,
  order_date TIMESTAMP(0),
  customer_name STRING,
  price DECIMAL(10, 5),
  product_id INT,
  order_status BOOLEAN
) WITH (
  'connector' = 'mysql-cdc',
  'hostname' = '<yourHostname>',
  'port' = '3306',
  'username' = '<yourUsername>',
  'password' = '<yourPassword>',
  'database-name' = '<yourDatabaseName>',
  'table-name' = '<yourTableName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 数据类型 | 备注 |
|---|---|---|---|---|
| connecto r | 源表类型 | 是 | STRING | 固定值为 mysql-cdc 。 |
| hostnam e | MySQL数据库的 IP地址或者 Hostname | 是 | STRING | 无 |
| usernam e | MySQL数据库服务的用户名 | 是 | STRING | 无 |
| password | MySQL数据库服务的密码 | 是 | STRING | 无 |

实时计算（流计算）

| database -name | MySQL数据库名称 | 是 | STRING | 数据库名称支持正则表达式以读取多个数据库的数据。 |
|---|---|---|---|---|
| table- name | MySQL表名 | 是 | STRING | 表名支持正则表达式以读取多个表的数据。 |
| port | MySQL数据库服务的端口号 | 否 | INTEGER | 默认值为3306。 |
| server-id | 数据库客户端的一个ID | 否 | STRING | 该ID必须是MySQL集群中全局唯一的。建议针对同一个数据库的每个作业都设置一个不同的ID。默认会随机生成一个5400~6400的值。 |
| server- time- zone | 数据库在使用的会话时区 | 否 | STRING | 例如Asia/Shanghai，该参数控制了MySQL中的 TIMESTAMP类型如何转成STRING类型。 |
| debeziu m.min.ro w.count.t o.stream. results | 当表的条数大于该值时，会使用分批读取模式。 | 否 | INTEGER | 默认值为1000。Flink采用以下方式读取MySQL源表数据： 全量读取：直接将整个表的数据读取到内存里。优点是速度快，缺点是会消耗对应大小的内存，如果源表数据量非常大，可能会有OOM风险。 分批读取：分多次读取，每次读取一定数量的行数， 直到读取完所有数据。优点是读取数据量比较大的表没有OOM风险，缺点是读取速度相对较慢。 |
| debeziu m.snaps hot.fetch. size | 在Snapshot阶段，每次读取 MySQL源表数据行数的最大值。 | 否 | INTEGER | 仅当分批读取模式时，该参数生效。 |
| debeziu m.* | Debezium属性参数 | 否 | STRING | 从更细粒度控制Debezium客户端的行为。例如 'debezium.snapshot.mode' = 'never' ， 详情请参见配置属性。 |

**类型映射**

MySQL的CDC和Flink字段类型对应关系如下。

| MySQL CDC字段类型 | Flink字段类型 |
|---|---|
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED |  |
| INT | INT |
| MEDIUMINT |  |
| SMALLINT UNSIGNED |  |
| BIGINT | BIGINT |
| INT UNSIGNED |  |
| BIGINT UNSIGNED | DECIMAL(20, 0) |
| BIGINT | BIGINT |
| FLOAT | FLOAT |

实时计算（流计算）

| DOUBLE | DOUBLE |
|---|---|
| DOUBLE PRECISION |  |
| NUMERIC(p, s) | DECIMAL(p, s) |
| DECIMAL(p, s) |  |
| BOOLEAN | BOOLEAN |
| TINYINT(1) |  |
| DATE | DATE |
| TIME [(p)] | TIME [(p)] [WITHOUT TIMEZONE] |
| DATETIME [(p)] | TIMESTAMP [(p)] [WITHOUT TIMEZONE] |
| TIMESTAMP [(p)] | TIMESTAMP [(p)] |
|  | TIMESTAMP [(p)] WITH LOCAL TIME ZONE |
| CHAR(n) | STRING |
| VARCHAR(n) |  |
| TEXT |  |
| BINARY | BYTES |
| VARBINARY |  |
| BLOB |  |

**常见问题**

如果您需要在MySQL CDC源表上进行窗口聚合，可以考虑采用非窗口聚合的方式，即将时间字段转换成窗口值，然后根据窗口值进行GROUP BY聚合。例如，统计每个店铺每分钟的订单数和销量，代码为 `SELECT`

```
shop_id, DATE_FORMAT(order_ts, 'yyyy-MM-dd HH:mm'), COUNT(*), SUM(price) FROM order_mysql_cdc GROUP BY shop_id, DATE_FORMAT(order_ts, 'yyyy-MM-dd HH:mm') 。
```

如何跳过Snapshot阶段，只从变更数据开始读取？ 可以通过WITH参数**debezium.snapshot.mode**来控制，您可以设置为： never：在启动时，不读取数据库的快照，而是直接从变更的最开始位置读取。但需要注意MySQL的变更旧数据可能会被自动清理，因此不能保证变更数据中包含了全量的数据，读取的数据不完整。 schema_only：如果你不需要保证数据的一致性，只关心作业启动后数据库的新增变更，则可以设置为 schema_only，仅快照schema，不快照数据，从变更的最新数据开始读取。 如何读取一个分库分表的MySQL数据库？ 如果MySQL是一个分库分表的数据库，分成了user_00、user_02和user_99等多个表，且所有表的schema 一致。则可以通过table-name选项，指定一个正则表达式来匹配读取多张表，例如设置table-name 为**user_.***，监控所有**user_**前缀的表。database-name选项也支持该功能，但需要所有的表schema一致。 全表读取阶段效率慢、存在反压，应该如何解决？ 可能是下游节点处理太慢导致反压了。因此您需要先排查下游节点是否存在反压。如果存在，则需要先解决下游节点的反压问题。您可以通过以下方式处理： 增加并发度。 开启minibatch等聚合优化参数（下游聚合节点）。 实时计算（流计算）

##### Upsert Kafka源表

**什么是Upsert Kafka**

Upsert Kafka基于开源Flink社区的Upsert-Kafka版本实现，详情请参见Upsert Kafka SQL 连接器。Upsert Kafka可以产生Changelog流，支持以UPSERT方式从Kafka Topic中读取数据或将数据写入Kafka Topic。其中每条数据记录代表一个更新或删除事件，原理如下： Kafka Topic中存在相应的Key，则以UPDATE操作将Key的值更新为数据记录中的Value。 Kafka Topic中不存在相应的Key，则以INSERT操作将Key的值写入Kafka Topic。 Key对应的Value为空，会被视作DELETE操作。

**前提条件**

已创建消息队列Kafka资源。

**使用限制**

仅VVR 3.0.1及以上版本支持Upsert Kafka Connector。

**DDL定义**

以表名pageviews_per_region为例介绍DDL定义。

```
CREATE TABLE pageviews_per_region (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '<yourServers>',
  'key.format' = 'avro',
  'value.format' = 'avro'
);
```

Upsert Kafka必须声明主键。

**说明**

**WITH参数**

| 参数 | 说明 | 是否必选 | 数据类型 | 备注 |
|---|---|---|---|---|
| connector | 源表类型 | 是 | String | 固定值为 upsert-kafka 。 |
| topic | 源表对应的Topic | 是 | String | 无 |
| properties.boots trap.servers | Kafka Broker地址 | 是 | String | 格式为 host:port,host:port,host:port ， 以英文逗号（,）分割。 |
| key.format | Upsert Kafka消息中Key部分反序列化的格式 | 是 | String | 支持的格式如下： csv json avro |

实时计算（流计算）

| value.format |  | Upsert Kafka消息中Value部分反序列化的格式 | 是 |  | String | 支持的格式如下： csv json avro |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| value.fields- include |  | 指定出现在Value 中的字段 | 是 |  | String | 取值如下： ALL：默认值，Schema中所有字段，包括主键字段。 EXCEPT KEY：Schema中所有字段，不包括主键 _ 字段。 |  |  |  |  |
| key.fields-prefix |  | 为主键的所有字段定义一个自定义前缀，避免Key与 Value字段的名称冲突。 | 否 |  | String | 默认情况下，前缀为空。如果定义了前缀，则表的 Schema和key.fields都将使用前缀名称。 当构造Kafka Key对应格式的数据类型时，主键名中的前缀将被删除，并采用名字中非前缀部分作为最终的名字。 说明 key.fields-prefix参数生效，要求value.fields-include必须设置为EXCEPT KEY。 _ |  |  |  |  |
| properties.* |  |  |  |  |  | 后缀名必须匹配定义在Apache Kafka文档中的参数名。Flink会自动移除properties.前缀，并将转换后的参数名及值传入Kafka客户端。例如，您可以通过设置 'properties.allow.auto.create.topics' = 'false' 来禁止自动创建Topic。 说明参数 key.deserializer 和 value.deseri alizer 是不允许通过该方式指定参数的，因为 Flink会重写这些参数的值。 |  |  |  |  |
|  |  |  |  |  |  |  |  | 'properties.allow.auto.create.topics' |  |  |
|  |  |  |  |  |  | = 'false' |  |  |  |  |
|  |  | 指定Kafka参数 | 否 |  | String |  | 说明参数 key.deserializer 和 value.deseri alizer 是不允许通过该方式指定参数的，因为 Flink会重写这些参数的值。 |  |  |  |
|  |  |  |  |  |  |  |  |  | key.deserializer |  |
|  |  |  |  |  |  |  | alizer |  |  |  |

| value.deseri |  |  |
|---|---|---|

**示例**

实时计算（流计算） `--`创建`upsert-kafka`类型源表。

```
CREATE TABLE pageviews_per_region (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '<yourServers>',
  'key.format' = 'avro',
  'value.format' = 'avro'
);
```

`--`创建`Kafka`类型结果表。

```
CREATE TABLE pageviews_per_region_db (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'format' = 'csv'
); INSERT INTO pageviews_per_region_db SELECT user_region, pv, uv FROM pageviews_per_region;
```

##### 全量数据湖Iceberg源表

本文为您介绍全量数据湖Iceberg源表的DDL定义、WITH参数、类型映射和代码示例。

**什么是数据湖Iceberg**

Apache Iceberg是一种开放的数据湖表格格式。您可以借助Apache Iceberg快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并借助开源大数据生态的Flink、Spark、Hive、Presto等计算引擎来实现数据湖的分析。目前Apache Iceberg提供以下核心能力： 基于HDFS或者对象存储构建低成本的轻量级数据湖存储服务。 完善的ACID语义。 支持历史版本回溯。 支持高效的数据过滤。 支持Schema Evolution。 支持Partition Evolution。 您可以借助Flink高效的容错能力和流处理能力，把海量的日志行为数据实时导入到Apache Iceberg数据湖内， 再借助Flink或者其他分析引擎来实现数据价值的提取。

**说明**

Iceberg Connector既可以作为Flink Stream作业的结果表，也可以作为Flink批作业的源表和结果表。本文主要介绍Iceberg表作为Flink批作业的源表。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE dlf_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-type' = 'custom',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '<yourAccessKeyId>',
  'access.key.secret' = '<yourAccessKeySecret>',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
);
```

**WITH参数**

| 参数 | 说明 |  | 是否必选 | 备注 |  |  |
|---|---|---|---|---|---|---|
| connector | 源表类型。 |  | 是 | 固定值为 iceberg 。 |  |  |
| catalog-name | Catalog名称。 |  | 是 | 请填写为自定义的英文名。 |  |  |
| catalog-type | Catalog类型。 |  | 是 | 固定值为custom。 |  |  |
| catalog- database | 数据库名称。 |  | 是 | 对应用户在DLF上创建的数据库名称，例如 dlf db。 _ |  |  |
| io-impl | 分布式文件系统的实现类名。 |  | 是 | 固定值为 org.apache.iceberg.aliyun.oss.OSSFil eIO 。 |  |  |
|  |  |  |  |  | org.apache.iceberg.aliyun.oss.OSSFil |  |
|  |  |  |  | eIO |  |  |
| oss.endpoint | 阿里云对象存储服务OSS的 Endpoint。 |  | 否 | 请联系阿里云运维工程师获取。 |  |  |
| access.key.id | 阿里云账号的Access Key。 |  | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |  |  |
| access.key.secr et | 阿里云账号的Access Secret。 |  | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |  |  |
| catalog-impl | Catalog的Class类名。 |  | 是 | 固定值为 org.apache.iceberg.aliyun.dlf.DlfCat alog |  |  |
|  |  |  |  |  | org.apache.iceberg.aliyun.dlf.DlfCat |  |
|  |  |  |  | alog |  |  |
| warehouse | 表数据存放在OSS的路径。 |  | 是 | 无。 |  |  |
| dlf.catalog-id | 阿里云账号的账号ID。 |  | 是 | 在系统界面右上角，单击当前登录用户的头像，选择个人信息，查看UID信息。 |  |  |
| dlf.endpoint | DLF服务的Endpoint。 |  | 是 | 请联系阿里云运维工程师获取。 |  |  |

实时计算（流计算）

| dlf.region-id | DLF服务的地域名。 | 是 | 请联系阿里云运维工程师获取。 |
|---|---|---|---|

**类型映射**

| Iceberg字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| INT | INT |
| LONG | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(P,S) | DECIMAL(P,S) |
| DATE | DATE |
| TIME | TIME 说明 Iceberg时间戳精度为微秒，Flink时间戳精度为毫秒。在使用Flink读取Iceberg数据时，时间精度会对齐到毫秒。 |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP LTZ _ |
| STRING | STRING |
| FIXED(L) | BYTES |
| BINARY | VARBINARY |
| STRUCT<...> | ROW |
| LIST<E> | LIST |
| MAP<K, V> | MAP |

**代码示例**

以下内容将为您介绍如何通过Flink作业将Iceberg源表的数据导入到另一个Iceberg结果表中，实现基本的ETL操作。
1. 确认已成功创建了DLF数据库。
创建数据库选择OSS路径时，请将名称设置为${warehouse}/${database_name}.db。

**说明**

例如，如果您将warehouse地址设置为oss://iceberg-test/warehouse，数据库的名称设置为dlf_db， 则dlf_db的OSS路径需要设置为oss://iceberg-test/warehouse/dlf_db.db。
2. 编写Flink Batch SQL作业生成测试数据，并导入到另一个Iceberg表中。
i. 在左侧导航栏，单击**作业开发**。 实时计算（流计算） ii. 在页面左上角，单击**新建**，文件类型选择为批作业的SQL。 iii. 在文本编辑区域编写SQL，代码示例如下。 实时计算（流计算）

```
CREATE TEMPORARY TABLE src_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-type' = 'custom',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '<yourAccessKeyId>',
  'access.key.secret' = '<yourAccessKeySecret>',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
); CREATE TEMPORARY TABLE dst_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-type' = 'custom',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '<yourAccessKeyId>',
  'access.key.secret' = '<yourAccessKeySecret>',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
); BEGIN STATEMENT SET; INSERT INTO src_iceberg VALUES (1, 'AAA'), (2, 'BBB'), (3, 'CCC'), (4, 'DDD'), (5, 'EEE'); INSERT INTO dst_iceberg SELECT * FROM src_iceberg; END;
```

3. 在作业开发页面右侧**高级配置**面版中，引擎版本配置为**vvr-4.0.8-flink-1.13vvr-4.0.11-flink-1.13**。
实时计算（流计算）
4. 单击**验证**。
5. 单击**上线**。
6. 在OSS控制台查看写入的测试数据。
等整个批作业完成后，您就可以在OSS路径下查看dst_iceberg表中写入的数据了。

##### Datagen源表

Datagen源表是系统内置的Connector，可以周期性地生成Datagen源表对应类型的随机数据。如果您在注册其他类型的Connector源表时报错，但您不确定是Flink系统问题还是源表WITH参数错误，您可以将WITH参数修改为**'connector' = 'datagen'**后，单击**运行**。如果不再报错，则证明Flink系统没有问题，您需要确认修改 WITH参数。

**DDL定义**

```
CREATE TABLE datagen_source (
    name VARCHAR,
    score BIGINT
) WITH (
   'connector' = 'datagen'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 源表类型 | 是 | 固定值为datagen。 |

实时计算（流计算）

| rows-per-second | 生成随机数据的速率 | 否 | 默认值为10000条/秒。 |
|---|---|---|---|
| fields.#.length | 生成随机字符串数据的长度。 | 否 | 默认值为100。支持 CHAR、VARCHAR和 STRING。 |
| fields.#.kind | 在数据源是无界的， 即fields.#.kind为随机生成器（默认值）。 在数据源是有界的， 即fields.#.kind为序列生成器。 | 否 | 无 |
| fields.#.max | 随机发生器的最大值 | 否 | 仅支持数字类型 |
| fields.#.min | 随机发生器的最小值 | 否 | 仅支持数字类型 |
| fields.#.start | 序列发生器的起始值 | 否 | 无 |
| fields.#.end | 序列发生器的结束值 | 否 | 无 |

**代码示例**

```
CREATE TEMPORARY table datahub_source(
  name VARCHAR
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY table datahub_sink(
  name  VARCHAR
) with (
  'connector'='datahub',
  'endpoint'='<yourEndpoint>',
  'project'='<yourProject>',
  'topic'='<yourTopic>',
  'accessId'='<yourAccessId>',
  'accessKey'='<yourAccessKey>'
); INSERT INTO datahub_sink SELECT
  LOWER(name)
from datahub_source;
```

##### 流式数据湖仓Paimon源表

**什么是流式数据湖仓Paimon**

Paimon是一种流批统一的湖存储格式，支持高吞吐的写入和低延迟的查询。目前阿里云开源大数据平台E- MapReduce常见的计算引擎（例如Flink、Spark、Hive或Trino）都与Paimon有着较为完善的集成度。您可以借助Apache Paimon快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并接入上述计算引擎实现数据湖的分析，详情请参见Apache Paimon。

**使用限制**

实时计算（流计算） 仅Flink计算引擎VVR 8.0.7及以上版本支持Paimon连接器。

**DDL定义**

```
CREATE TABLE paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  ...
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|
| connect or | 表类型。 | String | 否 | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则固定值为 paimon 。 |
| path | 表存储路径。 | String | 否 | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则为表在HDFS或OSS中的存储目录。 |
| auto- create | 创建Paimon临时表时，若指定路径不存在Paimon 表文件，是否自动创建文件。 | Boolean | 否 | false | 参数取值如下： false（默认）：如果指定路径不存在Paimon表文件，则报错。 true：如果指定路径不存在，则Flink系统自动创建 Paimon表文件。 |
| bucket | 每个分区的分桶数。 | Integer | 否 | 1 | 写入Paimon表的数据将按 bucket-key 打散至每个bucket中。 说明建议每个Bucket的数据量在5 GB以下。 |

实时计算（流计算）

| bucket- key | 分桶关键列。 | String | 否 |  |  | 指定将写入Paimon表的数据按哪些列的值打散至不同的Bucket中。 列名之间用英文逗号（,）分隔，例如 'bucket- key' = 'order id,cust id' 会将数据按 _ _ order id列和cust id列的值进行打散。 _ _ 说明如果该参数未填写，则按primary key 进行打散。 如果Paimon表未指定primary key，则按所有列的值进行打散。 |
|---|---|---|---|---|---|---|
|  |  |  |  |  | 无 |  |
| changel og- produc er | 增量数据产生机制。 | String | 否 |  | non e | Paimon可以为任意输入数据流产生完整的增量数据 （所有的update after数据都有对应的 _ update before数据），方便下游消费者。增量数据 _ 产生机制的可选值如下： none（默认值）：不额外产生增量数据。下游仍然可以流读Paimon表，但读到的增量数据是不完整的（只有update after数据，没有对应的 _ update before数据）。 _ input：将输入数据流双写至增量数据文件中，作为增量数据。 full-compaction：每次Full Compaction产生完整的增量数据。 lookup：每次commit snapshot前产生完整的增量数据。 |
| full- compac tion.del ta- commit s | Full Compaction最大间隔。 | Integer | 否 |  | 无 | 该参数指定了每commit snapshot多少次之后，一定会进行一次Full Compaction。 |
| merge- engine | 相同primary key数据的合并机制。 | String | 否 |  | ded uplic ate | 参数取值如下： deduplicate：仅保留最新一条。 partial-update：用最新数据中非null的列更新相同primary key的现有数据，其它列保持不变。 aggregation：通过指定聚合函数进行预聚合。 |

实时计算（流计算）

| partial- update. ignore- delete | 在partial- update合并机制中，是否忽略 delete消息。 | Boolean | 否 | false | 参数取值如下： true：忽略delete消息。 false：碰到delete消息，Flink系统会报错。 说明并非所有场景下忽略delete消息都是正确的，您需要结合自己的实际场景配置该参数。 |
|---|---|---|---|---|---|
| partitio n.defau lt-name | 分区默认名称。 | String | 否 | D __ EFA ULT PA _ RTIT ION _ _ | 如果分区列的值为null或空字符串，将会采用该默认名称作为分区名。 |
| partitio n.expir ation- check- interval | 多久检查一次分区过期。 | String | 否 | 1h | 无。 |
| partitio n.expir ation- time | 分区的过期时长。 | String | 否 | 无 | 当一个分区的存活时长超过该值时，该分区将会过期，默认永不过期。 |
| partitio n.times tamp- formatt er | 将时间字符串转换为时间戳的格式串。 | String | 否 | 无 | 无。 |
| partitio n.times tamp- pattern | 将分区值转换为时间字符串的格式串。 | String | 否 | 无 | 无。 |
| scan.bo unded. waterm ark | 当Paimon源表产生的数据的 watermark超过该值时，Paimon 源表将会结束产生数据。 | Long | 否 | 无 | 无。 |
| scan.m ode | 指定Paimon源表的消费位点。 | String | 否 | defa ult | 无。 |
| scan.sn apshot- id | 指定Paimon源表从哪个snapshot 开始消费。 | Integer | 否 | 无 | 无。 |

实时计算（流计算）

| scan.ti mesta mp- millis | 指定Paimon源表从哪个时间点开始消费。 | Integer | 否 | 无 | 无。 |
|---|---|---|---|---|---|
| snapsh ot.num- retaine d.max | 至多保留几个最新Snapshot不过期。 | Integer | 否 | 214 748 364 7 | 只要满足该配置或snapshot.time-retained其中之一，并同时满足snapshot.num-retained.min，就会触发Snapshot过期。 |
| snapsh ot.num- retaine d.min | 至少保留几个最新Snapshot不过期。 | Integer | 否 | 10 | 无。 |
| snapsh ot.time- retaine d | Snapshot产生多久以后会过期。 | String | 否 | 1h | 只要满足该配置或snapshot.num-retained.max其中之一，并同时满足snapshot.num- retained.min，就会触发snapshot过期。 |
| scan.inf er- paralleli sm | 是否自动推断 Paimon源表的并发度。 | Boolean | 否 | false | 参数取值如下： true：将会根据分桶数自动推断Paimon源表的并发度。 false：按VVP配置的默认并发。如果是专家模式就按用户配置的并发。 |
| scan.pa rallelis m | Paimon源表的并发度。 | Integer | 否 | 无 | 无。 |

**说明**

更多配置项详情请参见Apache Paimon官方文档。

#### 创建数据结果表

##### 日志服务SLS结果表

**什么是日志服务**

日志服务SLS是针对日志类数据的一站式服务。日志服务可以帮助您快捷地完成数据采集、消费、投递以及查询分析，提升运维和运营效率，建立海量日志处理能力。日志服务本身是流数据存储，Flink支持将其作为流式数据的输出。

**DDL定义**

实时计算（流计算）

```
create table sls_sink(
 name varchar,
 age int,
 birthday int
)with(
 'connector'='sls',
 'endPoint'='<endPoint>',
 'accessId'='<yourAccessId>',
 'accessKey'='<yourAccessKey>',
 'project'='<yourProjectName>',
 'logstore'='<yourLogstoreName>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 sls 。 |
| endPoint | EndPoint地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | 项目名 | 是 | 无 |
| logstore | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |

**类型映射**

日志服务和Flink字段类型对应关系如下，建议您使用该对应关系进行DDL声明。

| 日志服务字段类型 | Flink字段类型 |
|---|---|
| STRING | VARCHAR |

##### 消息队列Kafka结果表

**什么是消息队列Kafka**

消息队列Kafka版是阿里云提供的分布式、高吞吐、可扩展的消息队列服务。消息队列Kafka版广泛用于日志收集、监控数据聚合、流式数据处理、在线和离线分析等大数据领域。

**DDL定义**

实时计算（流计算）

```
create table kafka_sink(
  user_id BIGINT,
  item_id BIGINT,
  category_id BIGINT,
  behavior STRING,
  ts TIMESTAMP(3)
) with (
  'connector' = 'kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '<yourKafkaBrokers>',
  'format' = 'csv'
);
```

**WITH参数**

| 参数 | 说明 | 是否必选 | 数据类型 | 备注 |
|---|---|---|---|---|
| connector | 结果表类型 | 是 | STRI NG | 固定值为 kafka 。 |
| topic | 结果表对应的Topic | 是 | STRI NG | 无 |
| properties.bo otstrap.server s | Kafka Broker地址 | 是 | STRI NG | 请联系阿里云运维工程师获取。 |
| format | Flink Kafka Connector在反序列化来自Kafka的消息时使用的格式。 | 是 | STRI NG | 格式取值如下： csv json avro |
| sink.partitione r | 从Flink分区到Kafka分区的映射模式。 | 否 | STRI NG | 映射模式取值如下： fixed：每个Flink分区对应至多一个Kafka 分区。 round-robin：Flink分区中的数据将被轮流分配至Kafka的各个分区。 自定义FlinkKafkaPartitioner的子类：如果 fixed和round-robin不满足您的需求，您可以自定义映射模式到FlinkKafkaPartitioner 的子类。例如 org.mycompany.MyPartitioner 。 |

如果您还需要直接配置Connector使用的Kafka Producer，可以在Kafka Producer配置参数前添加 `properties` 前缀，并将该Kafka Producer配置信息追加至WITH参数。例如Kafka集群需要 SASL（Simple Authentication and Security Layer）认证。 实时计算（流计算）

```
CREATE TABLE kafkaTable (
    ...
) WITH (
    ...
    'properties.security.protocol' = 'SASL_PLAINTEXT',
    'properties.sasl.mechanism' = 'PLAIN',
    'properties.sasl.jaas.config' = 'org.apache.kafka.common.security.plain.PlainLoginModule
required username="USERNAME" password="PASSWORD";' );
```

Kafka Producer配置项详情请参见Producer Configs。

**从Kafka中读取数据后插入Kafka示例**

从名称为source的Topic中读取Kafka数据，再写入名称为sink的Topic，数据使用CSV格式。

```
CREATE TEMPORARY TABLE kafka_source (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'kafka',
    'topic' = '<yourTopicName>',
    'properties.bootstrap.servers' = '<yourKafkaBrokers>',
    'properties.group.id' = '<yourPropertiesGroupid>',
    'format' = 'csv'
); CREATE TEMPORARY TABLE kafka_sink (
    id INT,
    name STRING,
    age INT
) WITH (
    'connector' = 'kafka',
    'topic' = '<yourTopicName>',
    'properties.bootstrap.servers' = '<yourKafkaBrokers>',
    'format' = 'csv'
); INSERT INTO kafka_sink SELECT id, name, age FROM kafka_source;
```

##### 数据总线DataHub结果表

**什么是数据总线DataHub**

阿里云流数据处理平台DataHub是流式数据（Streaming Data）的处理平台，提供对流式数据的发布 （Publish）、订阅（Subscribe）和分发功能，让您可以轻松构建基于流式数据的分析和应用。Flink支持将 DataHub作为流式数据的输出。

**DDL定义**

实时计算（流计算）

```
create table datahub_sink(
  name varchar,
  age BIGINT,
  birthday BIGINT
)with(
  'connector'='datahub',
  'endpoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'accessId'='<yourAccessId>',
  'accessKey'='<yourAccessKey>',
  'batchCount'='500',
  'batchSize'='512000',
  'flushInterval'='5000'
);
```

**WITH参数**

| 参数 | 注释说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 datahub 。 |
| endPoint | 消费端点信息 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| project | 读取的项目 | 是 | 无 |
| topic | Project下的具体的Topic名称 | 是 | 无 |
| retryTimeout | 最大持续重试时间 | 否 | 单位为毫秒，默认值为180000（半小时）。 |
| retryInterval | 重试间隔 | 否 | 单位为毫秒，默认值为1000。 |
| batchCount | 每次批量写入数据的最大数据条数 | 否 | 默认值为500。 |
| batchSize | 每次批量写入数据的大小 | 否 | 默认值为512000 Byte。 |
| flushInterval | 缓存数据的最大超时时间 | 否 | 单位毫秒，默认值为5000。 |
| partitionBy | 写入Sink节点前会根据 partitionBy值进行hash， 数据会流向对应的Sink节点。 | 否 | 默认值为空，随机发送。 |
| hashFields | 指定列名后，相同列的值会写入到同一个Shard。 | 否 | 默认值为Null，即随机写可以指明多个列值，用逗号（,）分隔。例如 hashFields=a,b 。 |

**类型映射**

DataHub和Flink字段类型对应关系如下，建议使用该对应关系时进行DDL声明。

| DataHub字段类型 | Flink字段类型 |
|---|---|

实时计算（流计算）

| STRING | VARCHAR |
|---|---|
| TIMESTAMP | BIGINT |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| INTEGER | INTEGER |
| BIGINT | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| BOOLEAN | BOOLEAN |
| DECIMAL | DECIMAL |

**代码示例**

```
CREATE TEMPORARY table datahub_source(
  name VARCHAR
) with (
  'connector'='datahub',
  'endpoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'subId'='<yourSubId>',
  'accessId'='<yourAccessId>',
  'accessKey'='<yourAccessKey>',
  'startTime'='2018-06-01 00:00:00'
); CREATE TEMPORARY table datahub_sink(
  name varchar
)with(
  'connector'='datahub',
  'endpoint'='<endPoint>',
  'project'='<yourProjectName>',
  'topic'='<yourTopicName>',
  'accessId'='<yourAccessId>',
  'accessKey'='<yourAccessKey>',
  'batchSize'='512000',
  'batchCount'='500'
); INSERT INTO datahub_sink SELECT
  LOWER(name)
from datahub_source;
```

##### 表格存储Tablestore结果表

本文为您介绍表格存储Tablestore结果表的DDL定义、WITH参数和映射关系。 实时计算（流计算）

**什么是表格存储Tablestore**

表格存储Tablestore是基于阿里云飞天分布式系统的分布式NoSQL数据存储服务。表格存储通过数据分片和负载均衡技术，实现数据规模与访问并发的无缝扩展，提供海量结构化数据的存储和实时访问服务。Flink支持将 Tablestore作为流式数据的输出。

**DDL定义**

```
CREATE TABLE ots_sink (
    name VARCHAR,
    age BIGINT,
    birthday BIGINT,
    primary key(name,age) not enforced
) WITH (
    'connector'='ots',
    'instanceName'='<yourInstanceName>',
    'tableName'='<yourTableName>',
    'accessId'='<yourAccessId>',
    'accessKey'='<yourAccessSecret>',
    'endPoint'='<yourEndpoint>',
    'valueColumns'='birthday'
);
```

Tablestore结果表必须定义有 `Primary Key` ，输出数据以Update方式追加Tablestore表。

**说明**

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 ots 。 |
| instanceName | 实例名 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| endPoint | 实例访问地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| valueColumns | 指定插入的字段列名 | 是 | 多个字段以英文逗号（,）分割，例如 ID,NAME 。 |
| bufferSize | 流入多少条数据后开始输出 | 否 | 默认值为5000，表示输入的数据达到5000条就开始输出。 |
| batchWriteTimeou tMs | 写入超时的时间 | 否 | 单位为毫秒，默认值为5000。表示如果缓存中的数据在等待5秒后，依然没有达到输出条件， 系统会自动输出缓存中的所有数据。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为100。 |
| retryIntervalMs | 重试间隔时间 | 否 | 单位为毫秒，默认值为1000。 |
| maxRetryTimes | 最大重试次数 | 否 | 默认值为10。 |

实时计算（流计算）

| ignoreDelete | 是否忽略DELETE操作 | 否 | 默认值为False。 |
|---|---|---|---|
| connectTimeout | Connector连接 Tablestore的超时时间 | 否 | 单位毫秒，默认值为30000（30秒）。 |
| socketTimeout | Connector连接 Tablestore的 Socket超时时间 | 否 | 单位毫秒，默认值为30000（30秒）。 |

**类型映射**

| Tablestore字段类型 | Flink字段类型 |
|---|---|
| INTEGER | BIGINT |
| STRING | STRING |
| BOOLEAN | BOOLEAN |
| DOUBLE | DOUBLE |

##### MaxCompute结果表

本文为您介绍MaxCompute结果表的DDL定义、WITH参数、类型映射和代码示例。

**实现原理**

MaxCompute Sink可以分为以下两个阶段：
1. 写入数据。调用MaxCompute SDK中的接口将数据写入缓冲区，在缓冲区大小超过64 MB或者每隔指定的时
间间隔时，上传数据到MaxCompute的临时文件中。
2. 提交会话。在任务进行Checkpoint时， MaxCompute Sink会调用Tunnel的Commit方法，提交会话，移动
临时文件到MaxCompute表的数据目录，并修改元数据。 Commit方法不能提供原子性。因此，MaxCompute Sink提供的是At least Once方式，而

**说明**

不是Exactly Once方式。

**DDL定义**

Flink支持将MaxCompute作为结果输出，示例代码如下。

```
create table odps_sink(
    id INT,
    user_name VARCHAR,
    content VARCHAR
) with (
    'connector' = 'odps',
    'endpoint' = '<yourEndpoint>',
    'tunnelEndpoint' = '<yourTunnelEndpoint>',
    'project' = '<yourProjectName>',
    'tablename' = '<yourTableName>',
    'accessid' = '<yourAccessKeyId>',
    'accesskey' = '<yourAccessKeySecret>',
    'partition' = 'ds=2018****'
);
```

实时计算（流计算）

**说明**

WITH参数需要全部小写。 DDL定义中的字段名称、顺序和类型必须与MaxCompute物理表保持一致，否则可能导致 MaxCompute物理表中查询的数据为 `/n` 。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 数据结果表类型 | 是 | 固定值为 odps 。 |
| endPoint | MaxCompute服务地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoi nt | MaxCompute Tunnel服务的连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| project | MaxCompute项目名称 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| partition | 分区名 | 否 | 如果存在分区表，则必填partition。填写partition需要注意以下两点： 固定分区例如 `partition` = 'ds=20180905' 表示将数据写入分区 ds= 20180905 。 动态分区如果未明文显示分区值，则根据写入数据中分区列具体值，写入对应分区。例如 `partition`='ds' 表示根据 ds 字段值写入对应分区。 如果要创建多级动态分区，Partition中多个字段顺序必须和MaxCompute物理表保持一致，各个分区字段之间使用逗号（,）分割。 说明动态分区列需要显式写在建表语句中。 在动态分区字段为空时，如果数据源中 ds=null 或者 ds='' ，则输出结果为ds=NULL的分区。 |

实时计算（流计算）

| flushInterval Ms |  | Odps tunnel writer 缓冲区Flush间隔。 MaxCompute Sink 写入记录时，先放入数据到MaxCompute 的缓冲区中，等缓冲区溢出或者每隔一段时间 （flushIntervalMs） 时，再把缓冲区里的数据写到目标 MaxCompute表。 | 否 | 单位为毫秒，默认值为30000（30秒）。 |  |
|---|---|---|---|---|---|
| partitionBy |  | 写入Sink节点前，系统会根据该值做Hash Shuffle，数据就会流向对应的Sink节点。 | 否 | 系统按照多个列进行Hash Shuffle，各个列名之间使用逗号 （,）分割。默认为空。 |  |
| dynamicParti tionLimit |  | 分区数目最大值 | 否 | 默认值为100，系统会把已写入的分区和 TunnelBufferedWriter的映射关系维护到一个Map里，如果该Map大小超过了dynamicPartitionLimit设定值，则会出现 Too many dynamic partitions: 100, which exceeds the size limit: 100 报错。 |  |
|  |  |  |  |  | Too many dynamic partitions: 100, which |
|  |  |  |  | exceeds the size limit: 100 |  |

**类型映射**

| MaxCompute字段类型 | Flink字段类型 |
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

写入固定分区实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
    id INT,
    len INT,
    content VARCHAR
) with (
    'connector' = 'datagen'
); CREATE TEMPORARY TABLE odps_sink (
    id INT,
    len INT,
    content VARCHAR
) with (
    'connector' = 'odps',
    'endpoint' = '<yourEndpoint>',
    'tunnelEndpoint' = '<yourTunnelEndpoint>',
    'project' = '<yourProjectName>',
    'tablename' = '<yourTableName>',
    'accessid' = '<yourAccessKeyId>',
    'accesskey' = '<yourAccessKeySecret>',
    'partition' = 'ds=20180905'
); INSERT INTO odps_sink SELECT
     id, len, content
FROM datagen_source;
```

写入动态分区实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
    id INT,
    len INT,
    content VARCHAR,
    c TIMESTAMP
) with (
    'connector' = 'datagen'
); CREATE TEMPORARY TABLE odps_sink (
     id  INT,
     len INT,
     content VARCHAR,
```

`ds VARCHAR --`动态分区列需要显式声明。

```
) with (
     'connector' = 'odps',
     'endpoint' = '<yourEndpoint>',
     'tunnelEndpoint' = '<yourTunnelEndpoint>',
     'project' = '<yourProjectName>',
     'tablename' = '<yourTableName>',
     'accessid' = '<yourAccessKeyId>',
     'accesskey' = '<yourAccessKeySecret>',
```

`'partition' ='ds' --`不写分区的值，表示根据`ds`字段的值写入不同分区。

```
); INSERT INTO odps_sink SELECT
      id,
      len,
      content,
FROM datagen_source;
```

##### 消息队列RocketMQ版结果表

本文为您介绍消息队列RocketMQ版结果表DDL定义、WITH参数和示例代码等。

**什么是消息队列RocketMQ版**

消息队列 RocketMQ版是阿里云基于Apache RocketMQ构建的低延迟、高并发、高可用和高可靠的分布式消息中间件。消息队列RocketMQ版既可为分布式应用系统提供异步解耦和削峰填谷的能力，同时也具备互联网应用所需的海量消息堆积、高吞吐和可靠重试等特性。Flink支持将消息队列MQ作为流式数据的输出。

**DDL定义**

```
create table mq_sink(
   x varchar,
   y varchar,
   z varchar
) with (
   'connector'='mq',
   'topic'='<yourTopicName>',
   'endpoint'='<yourEndpoint>',
   'accessId'='<yourAccessId>',
   'accessKey'='<yourAccessSecret>'
);
```

实时计算（流计算） MQ是非结构化存储格式的消息中间件，对于数据的Schema不提供强制定义，完全由业务层指

**说明**

定。Flink仅支持CSV和二进制格式的MQ消息。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 mq 。 |
| topic | topic名称 | 是 | 无 |
| endpoint | 地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| producerGroup | 写入的群组 | 是 | 无 |
| tag | 写入的标签 | 否 | 默认值为空。 |
| nameServerSu bgroup | NameServer组 | 否 | 内网服务（阿里云经典网络/VPC）：nsaddr4client- internal 公网服务：nsaddr4client-internet 说明仅VVR 2.1.1及以上版本支持该参数。 |
| encoding | 编码类型 | 否 | 默认值为 utf-8 。 |
| retryTimes | 写入的重试次数 | 否 | 默认值为10。 |
| sleepTimeMs | 重试间隔时间 | 否 | 默认值为1000（毫秒）。 |
| instanceID | MQ实例ID | 否 | 如果MQ实例无独立命名空间，则不可以使用instanceID参数。 如果MQ实例有独立命名空间，则instanceID参数必选。 |

**代码示例**

CSV格式实时计算（流计算）

```
create table mq_sink (
    id INTEGER,
    len BIGINT,
    content VARCHAR
) with (
    'connector'='mq',
    'endpoint'='<yourEndpoint>',
    'accessId'='<yourAccessId>',
    'accessKey'='<yourAccessSecret>',
    'topic'='<yourTopicName>',
    'producerGroup'='<yourGroupName>',
    'tag'='<yourTagName>',
    'encoding'='utf-8',
    'retryTimes'='5',
    'sleepTimeMs'='500'
);
```

二进制格式

```
CREATE TEMPORARY TABLE datagen_source (
    commodity VARCHAR
) WITH (
    'connector' = 'datagen'
); CREATE TEMPORARY TABLE mq_sink (
    mess VARBINARY
) WITH (
    'connector'='mq',
    'endpoint'='<yourEndpoint>',
    'accessId'='<yourAccessId>',
    'accessKey'='<yourAccessSecret>',
    'topic'='<yourTopicName>',
    'producerGroup'='<yourGroupName>'
); INSERT INTO mq_sink SELECT
     CAST(SUBSTRING(commodity,0,5) AS VARBINARY) AS mess
FROM datagen_source;
```

##### 云数据库HBase版结果表

本文为您介绍云数据库HBase版结果表DDL定义、WITH参数、转换关系、动态表和代码示例。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE hbase_sink(
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q2 STRING, q3 BIGINT>,
  family3 ROW<q4 DOUBLE, q5 BOOLEAN, q6 STRING>
) with (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
);
```

HBase的列族（Column Family）必须声明为ROW类型，列族名即该ROW的字段名。例如，DDL定义中声明了family1、family2和family3三个列族。 HBase列族中的列（Cloumn）与对应ROW中嵌套的每个字段对应，列名即字段名。例如，DDL定义中列族 family2声明了q2和q3两列。 结果表中不需要将HBase表的所有列族和列都进行声明，只声明需要的即可。 除了类型为ROW的字段外，只能有一个原始类型（Atomic Type）的字段（例如STRING或BIGINT），该字段将被视作HBase的行键（Row Key），例如DDL定义中的rowkey。 必须将HBase的行键定义为结果表的主键（Primary Key），如果没有显示定义主键，默认使用行键作为主键。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 cloudhbase 。 |
| table-name | HBase表名 | 是 | 无 |
| zookeeper. quorum | HBase的zookeeper地址 | 是 | 无 |
| zookeeper. znode.pare nt | HBase在zookeeper中的根目录 | 否 | 默认值为 /hbase 。 说明仅在HBase标准版中生效。 |
| userName | 用户名 | 否 | 说明仅在HBase增强版中生效。 |
| password | 密码 | 否 | 说明仅在HBase增强版中生效。 |
| haclient.clu ster.id | HBase高可用实例ID | 否 | 只有访问同城主备实例时才需要配置。 说明仅在HBase增强版中生效。 |
| retries.num ber | 连接HBase客户端的重试次数 | 否 | 默认值为31。 |
| null-string- literal | HBase字段类型为字符串时，如果Flink字段数据为null，则将该字段赋值为null-string- literal，并写入 Hbase。 | 否 | 默认值为null。 |

实时计算（流计算）

| sink.buffer- flush.max- size | 写入HBase前，内存中缓存的数据量（字节） 大小。调大该值有利于提高HBase写入性能， 但会增加写入延迟和内存使用。 | 否 | 默认值为2 MB，支持字节单位B、KB、MB和GB，不区分大小写。 设置为0表示不进行缓存。 |
|---|---|---|---|
| sink.buffer- flush.max- rows | 写入HBase前，内存中缓存的数据条数。调大该值有利于提高HBase 写入性能，但会增加写入延迟和内存使用。 | 否 | 默认值为1000，设置为0表示不进行缓存。 |
| sink.buffer- flush.interv al | 将缓存数据周期性写入到HBase的间隔，可以控制写入HBase的延迟。 | 否 | 默认值为1秒，支持时间单位ms、s、min、h和d。设置为0表示关闭定期写入。 |

**转换关系**

HBase数据通过**org.apache.hadoop.hbase.util.Bytes**转换成Flink的数据类型。解码过程有以下两种情况： 当数据为null时，对于非字符串类型的数据，会编码为空字节数组。 对于字符串类型的数据，取决于**null-string-literal**的值。 Flink与HBase的数据转换关系如下。

| Flink类型 | HBase转换函数 |
|---|---|
| CHAR | byte[] toBytes(String s) |
| VARCHAR |  |
| STRING |  |
| BOOLEAN | byte[] toBytes(boolean b) |
| BINARY | byte[] |
| VARBINARY |  |
| DECIMAL | byte[] toBytes(BigDecimal v) |
| TINYINT | new byte[] { val } |
| SMALLINT | byte[] toBytes(short val) |
| INT | byte[] toBytes(int val) |
| BIGINT | byte[] toBytes(long val) |
| FLOAT | byte[] toBytes(float val) |
| DOUBLE | byte[] toBytes(double val) |
| DATE | 将日期转换成自1970.01.01以来的天数，用int表示，并通过byte[] toBytes(int val) 转换成字节数组。 |
| TIME | 将时间转换成自00:00:00以来的毫秒数，用int表示，并通过byte[] toBytes(int val) 转换成字节数组。 |
| TIMESTAMP | 将时间戳转换成自1970-01-01 00:00:00以来的毫秒数，用long表示，并通过 byte[] toBytes(long val) 转换成字节数组。 |

实时计算（流计算）

| ARRAY | 不支持 |
|---|---|
| MAP | 不支持 |
| MULTISET |  |
| ROW | 不支持 |

**动态表**

Flink部分结果数据需要按某列的值，作为动态列输入HBase。例如，某商品每小时的成交额作为动态列的数据， 示例如下。

```
CREATE TEMPORARY TABLE datagen_source (
    id INT,
    f1hour STRING,
    f1deal BIGINT,
    f2day STRING,
    f2deal BIGINT
) with (
    'connector'='datagen'
); CREATE TEMPORARY TABLE hbase_sink (
    rowkey INT,
    f1 ROW<`hour` STRING, deal BIGINT>,
    f2 ROW<`day` STRING, deal BIGINT>
) with (
    'connector'='cloudhbase',
    'table-name'='<yourTableName>',
    'zookeeper.quorum'='<yourZookeeperQuorum>',
    'dynamic.table'='true'
); INSERT INTO hbase_sink SELECT id, ROW(f1hour, f1deal), ROW(f2day, f2deal) FROM datagen_source;
```

**说明**

当**dynamic.table**参数值为true时，表明该表为支持动态列的HBase表。 每个列族对应的ROW中必须声明两个字段：第1个字段的值表示动态列，第2个字段的值表示动态列的值。 如果src表存在一条(1, "10", 100, "2020-7-26", 10000)数据，代表ID为1的商品，在10:00- 11:00点之间的成交额是100，在2020年7月26日当天的成交额是10000，则HBase中将插入行键为1的行，其中f1:10为100，f2:2020-7-26为10000。

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
   rowkey INT,
   f1q1 INT,
   f2q1 STRING,
   f2q2 BIGINT,
   f3q1 DOUBLE,
   f3q2 BOOLEAN,
   f3q3 STRING
) with (
   'connector'='datagen'
); CREATE TEMPORARY TABLE hbase_sink (
   rowkey INT,
   family1 ROW<q1 INT>,
   family2 ROW<q1 STRING, q2 BIGINT>,
   family3 ROW<q1 DOUBLE, q2 BOOLEAN, q3 STRING>,
   PRIMARY KEY (rowkey) NOT ENFORCE
) with (
   'connector'='cloudhbase',
   'table-name'='<yourTableName>',
   'zookeeper.quorum'='<yourZookeeperQuorum>'
); INSERT INTO hbase_sink SELECT rowkey, ROW(f1q1), ROW(f2q1, f2q2), ROW(f3q1, f3q2, f3q3) FROM datagen_source;
```

##### 云数据库Redis版结果表

本文为您介绍云数据库Redis版结果表DDL定义、WITH参数、类型映射和代码示例。 支持自建Redis服务。

**说明**

**什么是云数据库Redis版**

阿里云数据库Redis版是兼容开源Redis协议标准、提供内存加硬盘混合存储的数据库服务，基于高可靠双机热备架构及可平滑扩展的集群架构，充分满足高吞吐、低延迟及弹性变配的业务需求。Flink支持将其作为流式数据的输出。

**DDL定义**

STRING类型 DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 `set key value` 。 实时计算（流计算）

```
create table redis_sink (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED -- 必填。
) with (
  'connector' = 'redis',
  'mode' = 'string',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'dbNum' = '<yourDbNum>',
```

`'ignoreDelete' = 'true' --` 收到`Retraction`时，是否删除已插入的数据，默认值为`false`。

```
);
```

LIST类型 DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 `lpush key value` 。

```
create table redis_sink (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED -- 必填。
) with (
  'connector' = 'redis',
  'mode' = 'list',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'dbNum' = '<yourDbNum>',
```

`'ignoreDelete' = 'true' --` 收到`Retraction`时，是否删除已插入的数据，默认值为`false`。

```
);
```

SET类型 DDL为两列：第1列为key，第2列为value。Redis插入数据的命令为 `sadd key value` 。

```
create table redis_sink (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED -- 必填。
) with (
  'connector' = 'redis',
  'mode' = 'set',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'dbNum' = '<yourDbNum>',
```

`'ignoreDelete' = 'true' --` 收到`Retraction`时，是否删除已插入的数据，默认值为`false`。

```
);
```

HASHMAP类型 DDL为三列：第1列为key，第2列为hash_key，第3列为hash_key对应的hash_value。Redis插入数据的命

```
令为 hmset key hash_key hash_value 。
```

实时计算（流计算）

```
create table redis_sink (
  a STRING,
  b STRING,
  c STRING,
  PRIMARY KEY (a) NOT ENFORCED -- 必填。
) with (
  'connector' = 'redis',
  'mode' = 'hashmap',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'dbNum' = '<yourDbNum>',
```

`'ignoreDelete' = 'true' --` 收到`Retraction`时，是否删除已插入的数据，默认值为`false`。

```
);
```

SORTEDSET类型 DDL为三列：第1列为key，第2列为score，第3列为value。Redis插入数据的命令为 `zadd key score`

| value 。 |  |
|---|---|
|  | create table redis sink ( _ a STRING, b DOUBLE, --必须为DOUBLE类型。 c STRING, PRIMARY KEY (a) NOT ENFORCED -- 必填。 ) with ( 'connector' = 'redis', 'mode' = 'sortedset', 'host' = '<yourHost>', 'port' = '<yourPort>', 'password' = '<yourPassword>', 'dbNum' = '<yourDbNum>', 'ignoreDelete' = 'true' -- 收到Retraction时，是否删除已插入的数据，默认值为false。 ); |

**WITH参数**

| 参数 | 说明 | 是否必填 | 取值 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 redis 。 |
| mode | 对应Redis的数据结构 |  | 取值如下： string list set hashmap sortedset |
| host | Redis Server连接地址 |  | 请联系阿里云运维工程师获取。 |
| port | Redis Server连接端口 | 否 | 请联系阿里云运维工程师获取。 |
| password | Redis密码 |  | 默认值为空，不进行权限验证。 |
| dbNum | 选择操作的数据库 |  | 默认值为0。 |
| 91 |  |  | > 文档版本：2026072 |

| ignoreDelete | 是否忽略Retraction 消息。 |  | 默认值为false，可取值为true或false。如果设置为false，收到Retraction时，同时删除数据对应的key及已插入的数据。 |
|---|---|---|---|
| clusterMode | Redis集群是否为 cluster模式。 |  | 默认值为false。 |

**类型映射**

| Redis字段类型 | Flink字段类型 |
|---|---|
| STRING | STRING |
| SCORE | DOUBLE |

因为Redis的SCORE类型应用于SORTEDSET（有序集合），所以需要手动为每个Value设置一

**说明**

个DOUBLE类型的SCORE，Value才能按照该SCORE从小到大进行排序。

**代码示例**

```
CREATE TEMPORARY TABLE datagen_source (
  v STRING,
  p STRING
) with (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE redis_sink (
  a STRING,
  b STRING,
  PRIMARY KEY (a) NOT ENFORCED
) with (
  'connector' = 'redis',
  'mode' = 'string',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
); INSERT INTO redis_sink SELECT v, p FROM datagen_source;
```

##### 交互式分析Hologres结果表

本文为您介绍交互式分析Hologres结果表DDL定义、WITH参数、流式语义和类型映射。

**什么是交互式分析Hologres**

交互式分析Hologres兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析处理PB级数据，让您轻松使用现有BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**DDL定义**

实时计算（流计算）

```
create table hologres_sink(
  name varchar,
  age BIGINT,
  birthday BIGINT
) with (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username'='<yourUsername>',
  'password'='<yourPassword>',
  'endpoint'='<yourEndpoint>',
```

'field_delimiter'='|' --该参数可选。

```
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为hologres。 |
| dbname | 数据库名称 | 是 | 无 |
| tablename | 表名称说明如果 Schema不为Public时， 则tableName需要填写为schema.tableNam e。 | 是 | 无 |
| username | 用户名 | 是 | 无 |
| password | 密码 | 是 | 无 |
| endpoint | Hologres端点 | 是 | 请联系阿里云运维工程师获取。 |
| field delimiter _ | Hologres Sink支持将一个 STRING字段按照 field delimiter切分成数组导 _ 入Hologres。 | 否 | 默认值为"\u0002"。 |
| mutatetype | 数据写入模式，详情请参见流式语义。 | 否 | 默认值为insertorignore。 |
| partitionrouter | 是否写入分区表。 | 否 | 默认值为false。 |
| ignoredelete | 是否忽略撤回消息。 | 否 | 默认值为false。 说明仅在使用流式语义时生效。 |

实时计算（流计算）

| createparttable | 当写入分区表时，是否根据分区值自动创建不存在的分区表。 说明如果分区值中存在短划线（-），暂不支持自动创建分区表。 | 否 | false（默认值）：不会自动创建。 true：自动创建。 说明 VVR 2.1以上版本支持该参数。 请确保分区值不会出现脏数据， 否则会创建错误的分区表导致 Failover，建议慎用该参数。 |
|---|---|---|---|

**流式语义**

流处理，也称为流数据或流事件处理，即对一系列无界数据或事件连续处理。执行流数据或流事件处理的系统通常允许您指定一种可靠性模式或处理语义，保证整个系统处理数据的准确性，因为网络或设备故障等可能会导致数据丢失。 根据Hologres Sink的配置和Hologres表的属性，流式语义分为以下两种：
**Exactly-once**（仅一次）：即使在发生各种故障的情况下，系统只处理一次数据或事件。
**At-least-once**（至少一次）：如果在系统完全处理之前丢失了数据或事件，则从源头重新传输，因此可以多
次处理数据或事件。如果第一次重试成功，则不必进行后续重试。 在Hologres结果表中使用流式语义，您需要注意以下内容： 如果Hologres物理表未设置主键，则Hologres Sink使用**At-least-once**语义。 如果Hologres物理表已设置主键，则Hologres Sink通过主键确保**Exactly-once**语义。当同主键数据出现多次时，您需要设置**mutatetype**参数确定更新结果表的方式，**mutatetype**取值如下：
**insertorignore**（默认值）：保留首次出现的数据，忽略后续所有数据。
**insertorreplace**：整行替换已有数据。
**insertorupdate**：替换部分已有数据。例如一张表有a、b、c和d四个字段，a是PK（Primary Key），
写入Hologres时只写入a和b两个字段，在PK重复的情况下，系统只会更新b字段，c和d保持不变。

**说明**

当**mutatetype**设置为**insertorupdate**或**insertorreplace**时，系统根据主键更新数据。 Flink定义的结果表中的数据列数不一定要和Hologres物理表的列数一致，您需要保证缺失的列没有非空约束，即列值可以为Null，否则会报错。 默认情况下，Hologres Sink只能向一张表导入数据。如果导入数据至分区表的父表，即使导入成功，也会查询数据失败。您可以设置参数**partitionRouter**为true，开启自动将数据路由到对应分区表的功能。注意事项如下：
**tablename**参数需要填写为父表的表名。
Connector不会自动创建分区表，因此，需要您提前手动创建需要导入数据的分区表，否则会导入失败。

**宽表Merge和局部更新功能**

在把多个流的数据写到一张Hologres宽表的场景中，会涉及到宽表Merge和数据的局部更新。下面通过一个示例来介绍如何设置。 假设有两个Flink数据流，一个数据流中包含A、B和C字段，另一个数据流中包含A、D和E字段，Hologres宽表 WIDE_TABLE包含A、B、C、D和E字段，其中A字段为主键。具体操作如下：
1. 使用Flink SQL创建两张Hologres结果表，其中一张表只声明A、B和C字段，另一张表只声明A、D和E字段。
这两张表都映射至宽表WIDE_TABLE。
2. 两张结果表的属性设置：
**mutatetype**设置为**insertorupdate**，可以根据主键更新数据。
实时计算（流计算）
**ignoredelete**设置为**true**，防止回撤消息产生Delete请求。
3. 将两个Flink数据流的数据分别INSERT至对应的结果表中。
在上述场景中，有如下限制：

**说明**

宽表必须有主键。 每个数据流的数据都必须包含完整的主键字段。 列存模式的宽表Merge场景在高RPS的情况下，CPU使用率会偏高，建议关闭表中字段的Dictionary encoding功能。

**类型映射**

| Hologres字段类型 | Flink字段类型 |
|---|---|
| INT | INT |
| INT[] | ARRAY |
| BIGINT | BIGINT |
| BIGINT[] | ARRAY |
| REAL | FLOAT |
| REAL[] | ARRAY |
| DOUBLE PRECISION | DOUBLE |
| DOUBLE PRECISION[] | ARRAY |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY |
| TEXT | VARCHAR |
| TEXT[] | ARRAY |
| NUMERIC | DECIMAL |
| DATE | DATE |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

##### 云数据库MongoDB版结果表

仅支持将MongoDB作为结果表使用。

**说明**

**DDL定义**

实时计算（流计算）

```
CREATE TABLE mongodb_sink(
   id INT,
   number INT
) with (
   'connector' = 'mongodb',
   'database' = '<yourDatabase>',
   'collection' = '<yourCollection>',
   'uri' = '<yourUri>',
   'maxConnectionIdleTime' = '<yourMaxConnectionIdleTime>',
   'batchSize' = '1024'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 mongodb 。 |
| database | 数据库名称 | 是 | 无 |
| collection | 数据集合 | 是 | 无 |
| uri | MongoDB连接串 | 是 | 请联系阿里云运维工程师获取。 |
| maxConnectionIdl eTime | 连接超时时长 | 否 | 默认值为60000。 |
| batchSize | 每次批量写入的条数 | 否 | 默认值为1024。 |

**代码示例**

```
CREATE TEMPORARY TABLE datagen_source (
   v INT,
   p INT
) with (
   'connector' = 'datagen'
); CREATE TEMPORARY TABLE mongodb_sink(
   id INT,
   number INT
) with (
   'connector'='mongodb',
   'database' = '<yourDatabase>',
   'collection' = '<yourCollection>',
   'uri'='<yourUri>'
); INSERT INTO mongodb_sink
   SELECT v, p
FROM datagen_source;
```

##### Elasticsearch结果表

本文为您介绍Elasticsearch（ES）结果表DDL定义、WITH参数、类型映射和代码示例。 实时计算（流计算） 该Connector支持的功能是和阿里云Elasticsearch产品对齐的，暂不支持HTTPS加密访问形

**说明**

式。

**DDL定义**

```
 CREATE TABLE es_sink(
   user_id   STRING,
   user_name   STRING,
   uv BIGINT,
   pv BIGINT,
```

`PRIMARY KEY (user_id) NOT ENFORCED --` 主键可选，如果定义了主键，则作为文档`ID`，否则文档`ID`将为随机值。

```
) WITH (
   'connector' = 'elasticsearch-7',
   'hosts' = '<yourHosts>',
   'index' = '<yourIndex>',
   'document-type' = '<yourEelasticsearch.types>',
   'username' ='<yourElasticsearch.accessId>',
   'password' ='<yourElasticsearch.accessKey>'
);
```

**说明**

仅支持Elasticsearch 6.0和7.0版本。 DDL中的字段均对应Elasticsearch文档中的字段，不支持将文档ID写入表中。

**WITH参数**

| 参数 | 说明 |  | 是否必填 |  |  | 备注 |
|---|---|---|---|---|---|---|
| connector | 结果表类型 |  | 是 |  |  | 固定值为 elasticsearch- 6 或 elasticsearch-7 。 |
| hosts | Server地址 |  | 是 |  |  | 请联系阿里云运维工程师获取。 |
| index | 文档索引名称 |  | 是 |  |  | 默认为空，不进行权限验证。 |
| document-type | Type名称 |  | elasticsearc h-6 ：必填 |  |  | 无 |
|  |  |  |  | elasticsearc |  |  |
|  |  |  | h-6 |  |  |  |
|  |  |  |  |  | ：必填 |  |
|  |  |  |  | elasticsearc |  | 无 |
|  |  |  | h-7 |  |  |  |
| username | 访问实例ID |  | 否 |  |  | 默认为空，不进行权限验证。 |
| password | 访问实例密钥 |  | 否 |  |  | 如果定义了username，则必须定义非空的 password。 |
| document-id.key- delimiter | 文档ID的分隔符 |  | 否 |  |  | 默认值为 。 _ |

|  | elasticsearch- |
|---|---|
| elasticsearch-7 |  |

|  | 6 |
|---|---|

实时计算（流计算）

| failure-handler | Elasticsearch请求失败时的故障处理策略。 | 否 | 可选策略如下： fail（默认值）：如果请求失败，则作业失败。 ignore：忽略失败并删除请求。 retry rejected：重新添加由于队列容量满 _ 而失败的请求。 custom class name：用于使用 ActionRequestFailureHandler子类进行故障处理。 |
|---|---|---|---|
| sink.flush-on- checkpoint | 是否在checkpoint 时执行flush。 | 否 | 默认值为true。禁用该功能后，在 Elasticsearch进行Checkpoint 时，connector将不等待确认所有pending请求已完成。因此，connector不会为请求提供at-least-once保证。 |
| sink.bulk- flush.backoff.strat egy | 如果由于临时请求错误导致flush操作失败，则设置sink.bulk- flush.backoff.str ategy指定重试策略。 | 否 | DISABLED（默认值）：不执行重试，即第一次请求错误后失败。 CONSTANT：常量回退，即每次回退等待时间相同。 EXPONENTIAL：指数回退，即每次回退等待时间指数递增。 |
| sink.bulk- flush.backoff.max- retries | 最大回退重试次数。 | 否 | 默认值为8。 |
| sink.bulk- flush.backoff.dela y | 每次回退尝试之间的延迟。 | 否 | CONSTANT：每次重试之间的延迟。 EXPONENTIAL：这是初始基准延迟。 |
| sink.bulk- flush.max-actions | 每个批量请求的最大缓冲操作数。 | 否 | 默认值为1000，0表示禁用该功能。 |
| sink.bulk- flush.max-size | 存放请求的缓冲区内存最大值。 | 否 | 单位为MB，默认值为2，0表示禁用该功能。 |
| sink.bulk- flush.interval | flush的间隔。 | 否 | 默认值为1s，0表示禁用该功能。 |
| connection.path- prefix | 要添加到每个REST 通信中的前缀字符串。 | 否 | 默认值为空。 |

**文档ID**

Elasticsearch Sink可以根据是否定义了主键确定是其在upsert模式还是在append模式下工作。如果定义了主键，Elasticsearch Sink将在upsert模式下工作，该模式可以消费包含UPDATE和DELETE的消息。如果未定义主键，Elasticsearch Sink将以append模式工作，该模式只能消费INSERT消息。 在Elasticsearch Sink中，主键用于计算Elasticsearch的文档ID。文档ID为最多512个字节不包含空格的字符串。Elasticsearch Sink通过使用**document-id.key-delimiter**指定的键分隔符按照DDL中定义的顺序连接所有主键字段，从而为每一行生成一个文档ID字符串。某些类型（例如BYTES、ROW、ARRAY和MAP等）由于没有对应的字符串表示形式，所以不允许其作为主键字段。如果未指定主键，Elasticsearch将自动生成随机的文档ID。

**动态索引**

Elasticsearch Sink同时支持静态索引和动态索引： 如果使用静态索引，则索引选项值应为纯字符串，例如myusers，所有记录都将被写入myusers索引。 如果使用动态索引，可以使用 `{field_name}` 引用记录中的字段值以动态生成目标索引。您还可以使用
**{field_name|date_format_string}**将TIMESTAMP、DATE和TIME类型的字段值转换
实时计算（流计算） 为**date_format_string**指定的格式。**date_format_string**与Java的DateTimeFormatter兼容。例如， 如果设置为**myusers-{log_ts|yyyy-MM-dd}**，则log_ts字段值为**2020-03-27 12:25:55**的记录将被写入**myusers-2020-03-27**索引。

**类型映射**

Flink以JSON来解析Elasticsearch数据，详情请参见数据类型映射关系。

**代码示例**

```
CREATE TEMPORARY TABLE datagen_source (
  id STRING,
  name STRING,
  uv BIGINT
) with (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE es_sink (
   user_id STRING,
   user_name STRING,
   uv BIGINT,
```

`PRIMARY KEY (user_id) NOT ENFORCED --` 主键可选，如果定义了主键，则作为文档`ID`，否则文档`ID`将为随机值 。

```
) WITH (
   'connector' = 'elasticsearch-7',
   'hosts' = '<yourHosts>',
   'index' = '<yourIndex>',
   'document-type' = '<yourElasticsearch.types>',
   'username' ='<yourElasticsearch.accessId>',
   'password' ='<yourElasticsearch.accessKey>'
); INSERT INTO es_sink
   SELECT id, name, uv
FROM datagen_source;
```

##### Phoenix5结果表

**重要**

**DDL定义**

实时计算（流计算）

```
create table phoenix5_sink (
  `STATE` varchar,
  CITY varchar,
  POPULATION BIGINT,
  PRIMARY KEY (`STATE`, CITY)
) WITH (
  'connector' = 'phoenix5',
  'serverUrl' = '<yourserverUrl>',
  'tableName' = '<yourTableName>',
  'batchsize' = '25'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 默认值为 phoenix5 。 |
| serverUrl | Phoenix5的Query Server地址： 如果Phoenix5是在集群中创建的，则serverUrl是负载均衡服务的URL地址。 如果Phoenix5是在单机中创建的，则serverUrl是单机的URL地址。 | 是 | 请联系阿里云运维工程师获取。 |
| tableName | Phoenix5表名 | 是 | 无。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为20。 |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY table datagen_source (
  `id` varchar,
  `name` varchar,
  `age` varchar,
  `birthday` varchar
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY table phoenix5_sink (
  `id` varchar,
  `name` varchar,
  `age` varchar,
  `birthday` varchar,
  primary key (id)
) WITH (
  'connector' = 'phoenix5',
  'serverurl' = '<yourserverUrl>',
  'tablename' = '<yourTableName>',
  'batchsize' = '25'
); INSERT INTO phoenix5_sink
  SELECT  `id` ,`name` , `age` ,`birthday`
FROM datagen_source;
```

##### 云数据库RDS MySQL结果表

**语法示例**

```
CREATE TABLE rds_sink (
   id INT,
   num BIGINT,
   PRIMARY KEY (id) NOT ENFORCED
) WITH (
   'connector' = 'rds',
   'password' = '<yourPassword>',
   'tableName' = '<yourTablename>',
   'url' = '<yourUrl>',
   'userName' = '<yourUsername>'
);
```

| 说明 Flink写入RDS或DRDS数据库结果表原理：针对Flink每行结果数据，拼接成一行SQL语句，输入至目标端数据库，然后执行。如果使用批量写，需要在URL后面加上参数 ? rewriteBatchedStatements=true ，以提高系统性能。 RDS MySQL数据库支持自增主键，因此在DDL中不声明该自增字段。例如ID是自增字段，Flink DDL不声明该自增字段，则数据库在一行数据写入过程中会自动填补相关自增字段。 如果DRDS有分区表，拆分键必须在DDL里PRIMARY KEY（）中声明，否则拆分的表无法写入。 DDL声明的字段必须至少存在一个非主键的字段，否则产生报错。 |  |  |
|---|---|---|
|  | ? |  |

实时计算（流计算）

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 rds 。 |
| password | 密码 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| url | URL地址 | 是 | 请联系阿里云运维工程师获取。 |
| userName | 用户名 | 是 | 无 |
| maxRetryTim es | 写入数据失败后， 重试写入的次数 | 否 | 默认值为3。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为5000。 |
| flushInterval Ms | 清空缓存的时间间隔 | 否 | 单位为毫秒，默认值为 0，即默认不开启缓存flush。如果设置值为 2000，表示如果缓存中的数据在等待2秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |

**类型映射**

| RDS字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED | SMALLINT |
| INT | INT |
| SMALLINT UNSIGNED | INT |
| BIGINT | BIGINT |
| INT UNSIGNED | BIGINT |
| BIGINT UNSIGNED | DECIMAL(20,0) |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |

实时计算（流计算）

| VARBINARY | VARBINARY |
|---|---|

**代码示例**

```
CREATE TEMPORARY TABLE datagen_source (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE rds_sink (
  `name` VARCHAR,
  `age` INT
)WITH (
  'connector' = 'rds',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>'
); INSERT INTO rds_sink SELECT * FROM datagen_source;
```

**FAQ**

Q：Flink的结果数据写入RDS表，是按主键更新的，还是生成1条新的记录？ A：如果在DDL中定义了主键，会采用 `INSERT INTO tablename(field1,field2, field3, ...)`

```
VALUES(value1, value2, value3, ...) ON DUPLICATE KEY UPDATE field1=value1,field2=value2,
```

field3=value3, ...; 的方式更新记录，即对于不存在的主键字段会直接插入，存在的主键字段则更新相应的值。如果DDL中没有声明PRIMARY KEY，则会用 `insert into` 方式插入记录，追加数据。 Q：使用RDS表中的唯一索引进行GROUP BY时需要注意什么？ A： 需要在作业中的GROUP BY中声明该唯一索引。 RDS中只有一个自增主键，Flink作业中不能声明为PRIMARY KEY。

##### 云原生数据仓库AnalyticDB MySQL版3.0结果表

本文为您介绍云原生数据仓库AnalyticDB MySQL版3.0结果表的DDL定义、WITH参数和类型映射。

**DDL定义**

```
CREATE TABLE adb_sink (
  id INT,
  num BIGINT
) WITH (
  'connector' = 'adb3.0',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = 'jdbc:mysql://<yourNetworkAddress>:<PortId>/<yourDatabaseName>',
  'userName' = '<yourUsername>'
);
```

实时计算（流计算）

**WITH参数**

| 参数 | 注释说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为 adb3.0 。 |
| password | 密码 | 是 | 无 |
| tableName | 名 | 是 | 无 |
| url | jdbc连接地址 | 是 | 请联系阿里云运维工程师获取。 |
| username | 用户名 | 是 | 无 |
| maxRetryTimes | 写入数据失败后，重试写入的次数 | 否 | 默认值为3。 |
| batchSize | 一次批量写入的条数 | 否 | 默认值为5000。 |
| flushIntervalMs | 清空缓存的时间间隔 | 否 | 单位为毫秒，默认值为0，即默认不开启缓存flush。如果设置值为 2000，表示如果缓存中的数据在等待2秒后，依然没有达到输出条件，系统会自动输出缓存中的所有数据。 |

**类型映射**

| 云原生数据仓库AnalyticDB MySQL版3.0字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | INT |
| SMALLINT | INT |
| INT | INT |
| BIGINT | BIGINT |
| DOUBLE | DOUBLE |
| VARCHAR | VARCHAR |
| DATETIME | TIMESTAMP |
| DATE | DATE |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE adb_sink (
  `name` VARCHAR,
  `age` INT
) WITH (
  'connector' = 'adb3.0',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>'
); INSERT INTO adb_sink SELECT * FROM datagen_source;
```

##### Lindorm结果表

本文为您介绍云原生多模数据库Lindorm的宽表作为结果表的DDL定义、WITH参数、类型映射和代码示例。

**什么是云原生多模数据库Lindorm**

Lindorm是面向物联网、互联网、车联网等设计和优化的云原生多模超融合数据库，适用于日志、监控、账单、 广告、社交、出行、风控等场景，是为阿里巴巴核心业务提供支撑的数据库之一。 Lindorm具备以下特性： 支持宽表、时序、文本、对象、流、空间等多种数据的统一访问和融合处理。 兼容SQL、HBase/Cassandra/S3、TSDB、HDFS、Solr、Kafka等多种标准接口和无缝集成三方生态工具。

**使用限制**

仅Flink计算引擎VVR 4.0.8及以上版本支持Lindorm。

**DDL定义**

```
CREATE TABLE lindorm_dynamic_output( pk1 VARCHAR, pk2 VARCHAR, pk3 VARCHAR, c1 VARCHAR, c2 VARCHAR, PRIMARY KEY (pk1,pk2,pk3) NOT ENFORCED ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>' );
```

实时计算（流计算）

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 表类型。 | 是 | 固定值为lindorm。 |
| seedserver | Lindorm服务器的连接地址。 | 是 | 实时计算Flink版使用HBase Java API的方式连接并使用Lindorm宽表引擎。Lindorm服务器的连接地址的格式为 host:port 。 |
| namespace | Lindorm的命名空间。 | 是 | 无。 |
| username | 连接Lindorm所用到的用户名。 | 是 | 无。 |
| password | 连接Lindorm所用到的密码。 | 是 | 无。 |
| tableName | Lindorm表名。 | 是 | 无。 |
| columnFamily | Lindorm表的列族名。 | 是 | 如果创建Lindorm表时未指定列族名，则填写为f。 |
| retryInterval Ms | 写入失败时，重试写入的时间间隔。 | 否 | 单位为ms，默认值为1000ms。 |
| maxRetryTim es | 最大尝试次数。 | 否 | 默认值为5次。 |
| bufferSize | 一次批量写入数据的条数。 | 否 | 默认值为500条。 |
| flushInterval Ms | 当数据量比较少时，多长时间写入一次。 | 否 | 单位为ms，默认值为2000ms。 |
| ignoreDelete | 是否忽略Delete操作。 | 否 | 参数取值如下： true：忽略。 false（默认）：不忽略。 |

实时计算（流计算）

| dynamicColu mnSink | 是否开启动态表模式。关于动态表模式的介绍，请参见动态表模式一节。 | 否 | 参数取值如下： true：开启动态表模式。 false（默认）：不开启动态表模式。 说明实时计算引擎VVR 6.0.2及以上版本支持该参数。 |
|---|---|---|---|

**动态表模式**

动态表模式适用于在表定义中并未指定列名的情况，根据作业运行情况动态创建数据列并插入的场景。例如统计每天每小时的交易量，以天作为主键，小时作为列，每个小时的数据都是动态生成的，如下：

| 主键 | 列名：0点 | 列名：1点 |
|---|---|---|
| 2025-06-01 | 45 | 32 |
| 2025-06-02 | 76 | 34 |

动态表需要遵循特殊的DDL定义。其主键需要定义为前若干列，最后两列中前一列的值作为列名变量，最后一列的值作为该列对应的值，且要求最后两列的类型均为varchar。具体例子如下：

```
CREATE TABLE lindorm_dynamic_output( pk1 VARCHAR, pk2 VARCHAR, pk3 VARCHAR, c1 VARCHAR, c2 VARCHAR, PRIMARY KEY (pk1,pk2,pk3) NOT ENFORCED ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>' );
```

上述定义中，pk1、pk2、pk3 为主键，c1、c2 为动态表模式所必须的两列且一定为最后两列，不可存在其他的非主键的列。每次写入数据时，会将主键<pk1, pk2, pk3>对应的条目中添加/更改一列，列名为c1的值，该列的值为c2的值。每次一条数据来临时，只会添加/更改一列对应的值，其他列的值不会改变。

**类型映射**

Lindorm中数据均为二进制形式，通过Flink某个字段类型来转换或解析二进制的Bytes方法如下。

| Flink SQL类型 | 转换为写入的Bytes使用的方法 |
|---|---|

实时计算（流计算）

| CHAR | org.apache.flink.table.data.StringData::toBytes |
|---|---|
| VARCHAR |  |
| BOOLEAN | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(boolean) |
| BINARY | 直接为bytes的形式。 |
| VARBINARY |  |
| DECIMAL | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(BigDecimal) |
| TINYINT | 直接将数据封装成byte[]的第一个byte。 |
| SMALLINT | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(short) |
| INT | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(int) |
| BIGINT | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(long) |
| FLOAT | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(float) |
| DOUBLE | com.alibaba.lindorm.client.core.utils.Bytes::toBytes(double) |
| DATE | 获取自1970.01.01以来的天数后，调用 com.alibaba.lindorm.client.core.utils.Bytes::toBytes(int)。 |
| TIME | 获取自当天00:00:00以来的毫秒数后，调用 com.alibaba.lindorm.client.core.utils.Bytes::toBytes(int)。 |
| TIMESTAMP | 获取自1970.01.01 00:00:00以来的毫秒数后，调用 com.alibaba.lindorm.client.core.utils.Bytes::toBytes(long)。 |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE example_source(
 id INT,
 proc_time AS PROCTIME()
) WITH (
 'connector' = 'datagen',
 'number-of-rows' = '10',
 'fields.id.kind' = 'sequence',
 'fields.id.start' = '0',
 'fields.id.end' = '9'
); CREATE TEMPORARY TABLE lindorm_hbase_dim(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_dim_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); CREATE TEMPORARY TABLE lindorm_hbase_sink(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_sink_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); INSERT INTO lindorm_hbase_sink SELECT example_source.id as id, lindorm_hbase_dim.name as name, lindorm_hbase_dim.birth as b irth FROM example_source JOIN lindorm_hbase_dim FOR SYSTEM_TIME AS OF PROCTIME() ON example_sourc e.id = lindorm_hbase_dim.id;
```

##### ClickHouse结果表

本文为您介绍ClickHouse结果表的DDL定义，以及创建结果表时使用的WITH参数、类型映射和代码示例。

**使用限制**

仅Flink计算引擎VVR 3.0.2及以上版本支持ClickHouse Connector。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE clickhouse_sink (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'maxRetryTimes' = '3',
  'batchSize' = '8000',
  'flushIntervalMs' = '1000'
```

)

**WITH参数**

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为clickhouse。 |
| url | ClickHouse的JDBC连接地址 | 是 | 请联系阿里云运维工程师获取。 如果不写数据库名称，则使用默认的default数据库。 |
| userName | ClickHouse的用户名 | 是 | 无。 |
| password | ClickHouse的密码 | 是 | 无。 |
| tableName | ClickHouse的表名称 | 是 | 无。 |
| maxRetryTim es | 向结果表插入数据失败后的最大尝试次数 | 否 | 默认值为3。 |
| batchSize | 一次批量写入的数据条数 | 否 | 默认值为100。 |
| flushInterval Ms | 清空缓存的时间间隔 | 否 | 默认值为1000，单位为毫秒。表示如果缓存中的数据在等待1秒后，数据的条数依然没达到 batchSize的数量，系统会自动将缓存中的数据写入ClickHouse表中。 |

**类型映射**

| ClickHouse字段类型 | Flink字段类型 |
|---|---|
| UInt8 | BOOLEN |
| Int8 | TINYINT |
| Int16 | SMALLINT |
| Int32 | INTEGER |
| Int64 | BIGINT |
| Float32 | FLOAT |

实时计算（流计算）

| Float64 | DOUBLE |
|---|---|
| FixedString | CHAR |
| String | VARCHA |
| FixedString | BINARY |
| String | VARBINARY |
| Date | DATE |
| DateTime | TIMESTAMP(0) |
| Datetime64(x) | TIMESTAMP(x) |
| Decimal | DECIMAL |
| Array | ARRAY |
| 不支持 | TIME |
| 不支持 | MAP |
| 不支持 | MULTISET |
| 不支持 | ROW |

ClickHouse的DateTime类型可以精确到秒，Datetime64可以精确到纳秒。因为ClickHouse

**重要**

官方提供的JDBC写Datetime64数据类型会出现精度丢失，只能精确到秒的问题。所以目前通过Flink只能写入秒级别的TIMESTAMP，即TIMESTAMP(0)。

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE clickhouse_source (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'datagen',
  'rows-per-second' = '50'
); CREATE TEMPORARY TABLE clickhouse_output (
  id INT,
  name VARCHAR,
  age BIGINT,
  rate FLOAT
) WITH (
  'connector' = 'clickhouse',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
); INSERT INTO clickhouse_output SELECT
  id,
  name,
  age,
  rate
FROM clickhouse_source;
```

##### print结果表

本文为您介绍print结果表的DDL定义，以及创建print结果表时使用的WITH参数。您可以通过print结果表测试流作业或者调试生产作业，验证数据结果是否符合预期。

**说明**

如果您需要查看print结果表的结果数据，则需要将日志级别调至info，因为print sink数据输出为 info日志。 应安全部门要求，系统对taskmanager.log日志展示数据条数进行了限制。如果您有排查脏数据或特定数据等需求，建议在Where条件中指定业务场景相关条件后，进行print操作，以避免因为数据条数限制无法排查。

**DDL定义**

```
CREATE TABLE print_table (
  a INT,
  b varchar
) WITH (
  'connector'='print',
  'logger'='true'
);
```

实时计算（流计算）

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型 | 是 | 固定值为print。 |
| logger | 控制台是否显示数据结果 | 否 | 取值如下： false（默认值）：不显示。 true：显示。 |
| print-identifier | 数据结果标识 | 否 | 在日志中通过数据结果标识检索信息。 |
| sink.parallelism | 结果表并行度 | 否 | 默认与上游并行度一致。 |

**常见问题**

Q：如何在控制台查看print数据结果？ A：查看print数据结果的步骤，有以下两种方式： 在Flink开发控制台查看： a. 在目标作业**Task Manager**页签，单击**Path, ID**。 b. 在**logs**页签，查看print数据结果。 跳转到Flink UI界面查看： a. 在目标作业**作业总览**页签，单击**Flink UI**。 b. 单击**Task Managers**。 c. 单击**Path, ID**。 d. 在**logs**页签，查看print数据结果。

##### Upsert Kafka结果表

**什么是Upsert Kafka**

Upsert Kafka基于开源Flink社区的Upsert Kafka版实现，详情请参见Upsert Kafka SQL连接器。Upsert Kafka可以消费ChangeLog流，支持Flink将INSERT和UPDATE_AFTER数据作为正常的Kafka消息写入Kafka Topic，并将DELETE数据以Value为空的Kafka消息写入Kafka Topic，即以Upsert方式将数据写入Kafka Topic。此外，Flink将根据主键列的值对数据进行分区，从而保证主键上的消息有序，因此同一主键上的更新或删除消息将落在同一分区中。

**使用限制**

仅Flink计算引擎VVR 2.1.4及以上版本支持Upsert Kafka Connector。 Upsert Kafka Connector仅支持将结果数据写入到kafka 0.10及以上版本。 Upsert Kafka Connector仅支持Kafka 2.4版本的生产者配置项，详情请参见生产者配置项。

**DDL定义**

以表名upsert_kafka_sink为例介绍DDL定义。 实时计算（流计算）

```
CREATE TABLE upsert_kafka_sink (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '...',
  'key.format' = 'avro',
  'value.format' = 'avro'
);
```

Upsert Kafka必须声明主键。

**说明**

**WITH参数**

| 参数 | 说明 | 是否必选 | 数据类型 | 备注 |
|---|---|---|---|---|
| connector | 结果表类型。 | 是 | STRI NG | 固定值为 upsert-kafka 。 |
| topic | 结果表对应的Topic。 | 是 | STRI NG | 无。 |
| properties.bo otstrap.server s | Kafka Broker地址。 | 是 | STRI NG | 请联系阿里云运维工程师获取。 |
| key.format | Upsert Kafka消息中Key部分序列化的格式。 | 是 | STRI NG | 支持的格式如下： csv json avro |
| value.format | Upsert Kafka消息中Value部分序列化的格式。 | 是 | STRI NG | 支持的格式如下： csv json avro |
| value.fields- include | 指定出现在Value中的字段。 | 否 | Strin g | 取值如下： ALL（默认值）：Schema中所有字段，包括主键字段。 EXCEPT KEY：Schema中所有字段，不包 _ 括主键字段。 |

实时计算（流计算）

| properties.* | 指定Kafka参数。 |  |  |  |  | 后缀名必须匹配定义在Apache Kafka文档中的参数名。Flink会自动移除properties. 前缀，并将转换后的参数名及值传入Kafka客户端。例如，您可以通过设置 'properties.allow.auto.create.top ics' = 'false' 来禁止自动创建Topic。 说明已在WITH参数定义的Kafka 参数是不允许通过该方式指定参数，因为 Flink会重写该参数的值。例如 'key.deserializer' 和 'valu e.deserializer' 。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | 'properties.allow.auto.create.top |  |
|  |  |  |  |  |  | ics' = 'false' |  |  |  |
|  |  |  | 否 | Strin g |  |  | 说明已在WITH参数定义的Kafka 参数是不允许通过该方式指定参数，因为 Flink会重写该参数的值。例如 'key.deserializer' 和 'valu e.deserializer' 。 |  |  |
|  |  |  |  |  |  |  |  |  | 'key.deserializer' |
|  |  |  |  |  |  |  | e.deserializer' |  |  |

| 'valu |  |  |
|---|---|---|

Kafka Producer配置参数详情请参见Kafka官网生产者配置项列表。如果您还需要直接配置Connector使用的 Kafka Producer，可以在Kafka Producer配置参数前添加 `properties` 前缀，并将该Kafka Producer配置信息追加至WITH参数。例如Kafka集群需要SASL（Simple Authentication and Security Layer）认证，代码示例如下。

```
CREATE TABLE kafkaTable (
    ...
) WITH (
    ...
    'properties.security.protocol' = 'SASL_PLAINTEXT',
    'properties.sasl.mechanism' = 'PLAIN',
    'properties.sasl.jaas.config' =
'org.apache.flink.kafka.shaded.org.apache.kafka.common.security.plain.PlainLoginModule requi red username="USERNAME" password="PASSWORD";' );
```

**示例**

实时计算（流计算） `--`创建统计`PV`和`UV`的源表。

```
CREATE TABLE pageviews (
  user_id BIGINT,
  page_id BIGINT,
  viewtime TIMESTAMP,
  user_region STRING,
  WATERMARK FOR viewtime AS viewtime - INTERVAL '2' SECOND
) WITH (
  'connector' = 'kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '...',
  'format' = 'json'
); CREATE TABLE pageviews_per_region (
  user_region STRING,
  pv BIGINT,
  uv BIGINT,
  PRIMARY KEY (user_region) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = '<yourTopicName>',
  'properties.bootstrap.servers' = '...',
  'key.format' = 'avro',
  'value.format' = 'avro'
);
```

`--`将统计的`PV`、`UV`数据写入结果表中。

```
INSERT INTO pageviews_per_region SELECT
  user_region,
  COUNT(*),
  COUNT(DISTINCT user_id)
FROM pageviews GROUP BY user_region;
```

##### 数据湖Iceberg结果表

您可以通过Flink将数据写入Hive Metastore或者DLF Catalog下的Iceberg表。本文为您介绍如何将数据写入到数据湖Iceberg结果，包括DDL定义、WITH参数、类型映射和代码示例等。

**背景信息**

Apache Iceberg是一种开放的数据湖表格格式。您可以借助Apache Iceberg快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并借助开源大数据生态的Flink、Spark、Hive、Presto等计算引擎来实现数据湖的分析。目前Apache Iceberg提供以下核心能力： 基于HDFS或者对象存储构建低成本的轻量级数据湖存储服务。 完善的ACID语义。 支持历史版本回溯。 支持高效的数据过滤。 支持Schema Evolution。 支持Partition Evolution。 您可以借助Flink高效的容错能力和流处理能力，把海量的日志行为数据实时导入到Apache Iceberg数据湖内， 实时计算（流计算） 再借助Flink或者其他分析引擎来实现数据价值的提取。您可以通过以下任意一种方式来使用Iceberg Connector： 将数据写入至Hive Metastore下的Iceberg表 Apache Hive Metastore通常被作为开源大数据的统一元数据中心。如果您的元数据被维护在Apache Hive Metastore，希望通过Flink将数据写入Iceberg表内，然后将数据存储在阿里云OSS上，可以采用该方式来使用Iceberg Connector。 将数据写入至DLF Catalog下的Iceberg表是基于阿里云大数据生态产品设计和研发的统一元数据中心。借助该元数据中心您可以方便地采用开源大数据计算引擎（Spark、Hive、Presto或Flink）访问同一份数据湖内的数据。如果您希望元数据被存储在阿里云 DLF上，可以采用该方式来使用Iceberg Connector。 Iceberg Connector既可以作为Flink Stream作业的结果表，也可以作为Flink批作业的源表和

**说明**

结果表。

**前提条件**

将数据写入至DLF Catalog下的Iceberg表前，需要已开通阿里云DLF。

**使用限制**

Iceberg Connector仅支持日志数据入湖，暂不支持CDC或者Binlog数据入湖。 Iceberg Connector仅支持采用Hive Metastore和阿里云DLF作为Catalog，文件系统采用阿里云OSS服务。 暂不支持采用开源HDFS作为Iceberg表的文件系统。

**类型映射**

| Iceberg字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| INT | INT |
| LONG | BIGINT |
| FLOAT | FLOAT |
| DOUBLE | DOUBLE |
| DECIMAL(P,S) | DECIMAL(P,S) |
| DATE | DATE |
| TIME | TIME 说明 Iceberg时间戳精度为微秒，Flink时间戳精度为毫秒。在使用Flink读取Iceberg数据时，时间精度会对齐到毫秒。 |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP LTZ _ |
| STRING | STRING |
| FIXED(L) | BYTES |
| BINARY | VARBINARY |
| STRUCT<...> | ROW |

实时计算（流计算）

| LIST<E> | LIST |
|---|---|
| MAP<K, V> | MAP |

**将数据写入至Hive Metastore下的Iceberg表**

下面为您介绍如何通过Flink将数据写入到Apache Hive Metastore上的Iceberg表。
1. 验证Hive Metastore依赖的Hadoop能否正确访问阿里云OSS数据。
无论您使用的是阿里云EMR上的Hive Metastore，还是自建的Hive Metastore，都需要确保Hive Metastore所依赖的Hadoop能正确访问阿里云OSS上的数据。具体的确认方法如下： 阿里云EMR上的Hive Metastore。 通常，阿里云EMR上的Hive Metastore是可以直接访问该账号下的OSS数据的。如果您需要确认，则可以登录到Hive Metastore所在的主机。然后通过以下命令来验证Hadoop能否正确访问OSS数据。假如您需要访问oss://table-format/路径，则验证命令如下。

```
hdfs dfs -ls oss://table-format/
```

oss://table-format/为示例值。在实际验证时，需要替换为您账号下的Bucket名称和OSS

**说明**

路径。 自建的Hive Metastore。 如果您使用的是自建Hive Metastore，则需要手动配置Hadoop以便能正确地访问OSS数据。操作步骤详情如下。 a. 打开Hadoop的阿里云OSS插件开关，让Hadoop classpath可以自动加载阿里云OSS的相关依赖。不同 Hadoop版本的操作方式如下表所示。

| Hadoop版本 | 操作方式 |
|---|---|
| hadoop 3.x.x | 在$HADOOP HOME/etc/hadoop/hadoop-env.sh中新增如下内容。 _ export HADOOP OPTIONAL TOOLS="hadoop-aliyun" _ _ |
| hadoop 2.9.x | 在$HADOOP HOME/libexec/hadoop-config.sh中新增如下内容。 _ CLASSPATH=${CLASSPATH}:${TOOL PATH} _ |
| hadoop 2.8.x及以下版本 | 不支持访问阿里云OSS服务。 |

实时计算（流计算） b. 在$HADOOP_HOME/etc/hadoop/core-site.xml中新增如下内容，并将**fs.oss.endpoint**、**fs.oss.accessKeyId**和**fs.oss.accessKeySecret**参数值替换为您的实际值。

```xml
<property>
    <name>fs.AbstractFileSystem.oss.impl</name>
    <value>org.apache.hadoop.fs.aliyun.oss.OSS</value>
</property> <property>
    <name>fs.oss.impl</name>
    <value>org.apache.hadoop.fs.aliyun.oss.AliyunOSSFileSystem</value>
</property> <property>
    <name>fs.oss.endpoint</name>
    <value>${YOUR_OSS_ENDPOINT}</value>
</property> <property>
    <name>fs.oss.accessKeyId</name>
    <value>${YOUR_ACCESS_KEY_ID}</value>
</property> <property>
    <name>fs.oss.accessKeySecret</name>
    <value>${YOUR_ACCESS_KEY_SECRET}</value>
</property>
```

其中涉及的参数解释如下表所示。

| 参数 | 说明 |
|---|---|
| fs.oss.endpoint | 阿里云对象存储OSS的域名。 |
| fs.oss.accessKeyId | 阿里云账号的Access Key。 |
| fs.oss.accessKeySecret | 阿里云账号的AccessKey Secret。 |

c. 通过hdfs命令行来验证是否可以正确读取OSS数据。

```
hdfs dfs -ls oss://table-format/
```

oss://table-format/为示例值。在实际验证时，需要替换为您账号下的Bucket名称和

**说明**

OSS路径。
2. 配置网络以便Flink可以正确地访问Hive Metastore端口。
3. 编写SQL并执行入湖作业。
实时计算（流计算）

```
CREATE TEMPORARY TABLE flink_source(
  id BIGINT,
  data STRING
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE iceberg_sink (
  id BIGINT,
  data STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = 'hive_prod',
  'catalog-type' = 'hive',
  'engine.hive.enabled' = 'true',
  'uri' = 'thrift://<host>:<port>',
  'location' = 'oss://<oss-bucket>/<oss-object>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<aliyun-oss-endpoint>',
  'access.key.id' = '<aliyun-oss-access-key>',
  'access.key.secret' = '<aliyun-oss-access-key-secret>'
); INSERT INTO iceberg_sink SELECT * FROM flink_source;
```

WITH参数解释如下表所示。

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 结果表类型。 | 是 | 固定值为 iceberg 。 |
| catalog-name | Catalog名称。 | 是 | 请填写为自定义的英文名。 |
| catalog-type | Catalog类型。 | 是 | 固定值为hive。 |
| catalog- database | 数据库名称。 | 是 | 对应用户在Hive Metastore上创建的数据库名称，例如iceberg db。 _ |
| engine.hive.e nabled | 存放在Hive Metastore中的 Iceberg表的元数据是否能被Hive 计算引擎读取。 | 否 | 参数取值如下： true（推荐值）：可以被Hive计算引擎直接读取。 false：不可以被Hive计算引擎直接读取。 |
| uri | Hive Metastore的thrift server 的地址。 | 是 | 格式为thrift://<host>:<port>。其中： host表示Hive Metastore的IP地址。 port表示Hive Metstore的端口，默认值为 9083。 |
| location | 结果表存放的OSS路径。 | 是 | 格式为oss://<bucket>/<object>。其中： bucket表示您创建的OSS Bucket名称。 object表示您存放数据的路径。 |
| io-impl | 分布式文件系统的实现类名称。 | 是 | 固定值为 org.apache.iceberg.aliyun.oss.OSSFileIO。 |

实时计算（流计算）

| oss.endpoint | 阿里云对象存储服务OSS的 Endpoint。 | 是 | 请联系阿里云运维工程师获取。 |
|---|---|---|---|
| access.key.id | 阿里云账号的AccessKey ID。 | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |
| access.key.se cret | 阿里云账号的AccessKey Secret。 | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |

**将数据写入至DLF Catalog下的Iceberg表**

下面为您介绍如何通过Flink将数据写入到阿里云DLF上的Iceberg表。 DDL定义

```
CREATE TABLE dlf_iceberg (
  id   BIGINT,
  data STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-type' = 'custom',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '<yourAccessKeyId>',
  'access.key.secret' = '<yourAccessKeySecret>',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
);
```

WITH参数说明

| 参数 | 说明 |  | 是否必选 | 备注 |  |  |
|---|---|---|---|---|---|---|
| connector | 结果表类型。 |  | 是 | 固定值为 iceberg 。 |  |  |
| catalog-name | Catalog名称。 |  | 是 | 请填写为自定义的英文名。 |  |  |
| catalog-type | Catalog类型。 |  | 是 | 固定值为custom。 |  |  |
| catalog- database | 数据库名称。 |  | 是 | 对应用户在DLF上创建的数据库名称，例如 dlf db。 _ |  |  |
| io-impl | 分布式文件系统的实现类名。 |  | 是 | 固定值为 org.apache.iceberg.aliyun.oss.OSSFi leIO 。 |  |  |
|  |  |  |  |  | org.apache.iceberg.aliyun.oss.OSSFi |  |
|  |  |  |  | leIO |  |  |
| oss.endpoint | 阿里云对象存储服务OSS的 Endpoint。 |  | 是 | 请联系阿里云运维工程师获取。 |  |  |
| access.key.id | 阿里云账号的AccessKey ID。 |  | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |  |  |

实时计算（流计算）

| access.key.se cret | 阿里云账号的Access Secret。 |  | 是 | 请在Apsara Uni-manager运营控制台，将鼠标悬停在当前登录用户的头像上，单击个人信息进行查看。。 |  |  |
|---|---|---|---|---|---|---|
| catalog-impl | Catalog的Class类名。 |  | 是 | 固定值为 org.apache.iceberg.aliyun.dlf.DlfCa talog |  |  |
|  |  |  |  |  | org.apache.iceberg.aliyun.dlf.DlfCa |  |
|  |  |  |  | talog |  |  |
| warehouse | 表数据存放在OSS的路径。 |  | 是 | 无。 |  |  |
| dlf.catalog-id | 阿里云账号的账号ID。 |  | 是 | 在系统界面右上角，单击当前登录用户的头像，选择个人信息，查看UID信息。 |  |  |
| dlf.endpoint | DLF服务的Endpoint。 |  | 是 | 请联系阿里云运维工程师获取。 |  |  |
| dlf.region-id | DLF服务的地域名。 |  | 是 | 说明请和dlf.endpoint选择的地域保持一致。 |  |  |

代码示例 i. 创建DLF数据库。 创建数据库选择OSS路径时，请将DLF数据库OSS路径选择

**说明**

为${warehouse}/${database_name}.db。例如，如果您将warehouse地址设置为oss://icebergtest/warehouse，数据库的名称设置为dlf_db，则dlf_db的OSS路径需要选择为oss://icebergtest/warehouse/dlf_db.db。 ii. 在**作业开发**页面，在文本编辑区域，编写SQL设计流作业。

```
CREATE TEMPORARY TABLE datagen(
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE dlf_iceberg (
  id    BIGINT,
  data  STRING
) WITH (
  'connector' = 'iceberg',
  'catalog-name' = '<yourCatalogName>',
  'catalog-type' = 'custom',
  'catalog-database' = '<yourDatabaseName>',
  'io-impl' = 'org.apache.iceberg.aliyun.oss.OSSFileIO',
  'oss.endpoint' = '<yourOSSEndpoint>',
  'access.key.id' = '<yourAccessKeyId>',
  'access.key.secret' = '<yourAccessKeySecret>',
  'catalog-impl' = 'org.apache.iceberg.aliyun.dlf.DlfCatalog',
  'warehouse' = '<yourOSSWarehousePath>',
  'dlf.catalog-id' = '<yourCatalogId>',
  'dlf.endpoint' = '<yourDLFEndpoint>',
  'dlf.region-id' = '<yourDLFRegionId>'
); INSERT INTO dlf_iceberg SELECT * FROM datagen;
```

iii. 在作业开发页面右侧**高级配置**面版中，引擎版本配置为**vvr-4.0.11-flink-1.13**。 实时计算（流计算） iv. 单击**验证**。 v. 单击**上线**。 vi. 单击**确认**。 vii. 在OSS控制台查看写入的测试数据。 等第一次Checkpoint完成之后，您将能看到写入的测试数据了。

##### Blackhole结果表

Blackhole结果表是系统内置的Connector。如果您在注册其他类型的Connector结果表时报错，但您不确定是系统问题还是结果表WITH参数错误，您可以将WITH参数修改为**'connector' = 'blackhole'**后，单击**运行**。 如果不再报错，则证明系统没有问题，您需要确认修改WITH参数。

**DDL定义**

```
create table blackhole_sink(
  name VARCHAR,
  score BIGINT
) with (
  'connector' = 'blackhole'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|

实时计算（流计算）

| connector | 结果表类型 | 是 | 固定值为blackhole。 |
|---|---|---|---|

**代码示例**

```
CREATE TEMPORARY table datahub_source(
  name VARCHAR
) with (
  'connector'='datahub',
  'endpoint'='<yourEndpoint>',
  'project'='<yourProject>',
  'topic'='<yourTopic>',
  'subId'='<yourSubId>',
  'accessId'='<yourAccessId>',
  'accessKey'='<yourAccessKey>',
  'startTime'='2018-06-01 00:00:00'
); CREATE TEMPORARY table blackhole_sink(
  name  VARCHAR
) with (
  'connector' = 'blackhole'
); INSERT INTO blackhole_sink SELECT
  LOWER(name)
from datahub_source;
```

##### InfluxDB结果表

本文为您介绍InfluxDB结果表的DDL定义、WITH参数、类型映射和代码示例。

**什么是时序数据库InfluxDB®版**

时序数据库InfluxDB®版是一款专门处理高写入和查询负载的时序数据库，用于存储大规模的时序数据并进行实时分析，包括来自DevOps监控、应用指标和IoT传感器上的数据。

**前提条件**

已创建InfluxDB的数据库，详情请参见管理用户账号和数据库。

**DDL定义**

Flink支持使用InfluxDB作为结果表输出，示例代码如下。 实时计算（流计算）

```
CREATE TABLE stream_test_influxdb(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `tag_value1` VARCHAR,
 `field_fieldValue1` DOUBLE
) WITH (
  'connector' = 'influxdb',
  'url' = 'http://service.cn.influxdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='300',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
);
```

建表默认格式： 第0列：metric（VARCHAR），必填。 第1列：timestamp（BIGINT），必填，单位为毫秒。 第2列：tag_value1（VARCHAR），必填，最少填写一个。 第3列：field_fieldValue1（DOUBLE），必填，最少填写一个。 写入多个field_fieldValue时，您需要按照如下格式填写。

```
field_fieldValue1 类型, field_fieldValue2 类型, ... field_fieldValueN 类型
```

示例如下。

```
field_fieldValue1 DOUBLE, field_fieldValue2 INTEGER, ... field_fieldValueNINTEGER
```

结果表中只支持**metric**、**timestamp**、**tag_***和**field_***，不能出现其他的字段。

**说明**

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 结果表类型。 | 是 | 固定值为influxdb。 |
| url | InfluxDB的服务地址。 | 是 | 请联系阿里云运维工程师获取。 |
| database | InfluxDB的数据库名称。 | 是 | 例如db-flink。 |
| username | 数据库的用户名。 | 是 | 需要对目标数据库有写权限。用户名详情请参见管理用户账号和数据库。 |
| password | 数据库的密码。 | 是 | 密码详情请参见管理用户账号和数据库。 |
| batchSize | 批量提交的记录条数。 | 否 | 默认每次批量提交300条记录。 |

实时计算（流计算）

| retentionPoli cy | 保留策略。 | 否 | 如果您不配置该参数时，该参数会被默认填写为每个数据库的默认保留策略autogen，保留策略详情请参见管理用户账号和数据库。 |
|---|---|---|---|
| ignoreErrorD ata | 是否忽略异常数据。 | 否 | 取值如下： true：忽略异常数据。 false（默认值）：不忽略异常数据。 |

**类型映射**

| InfluxDB字段类型 | Flink版字段类型 |
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

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datahub_source(
 `metric` VARCHAR,
 `timestamp` BIGINT,
 `filedvalue` DOUBLE,
 `tagvalue` VARCHAR
) WITH (
  'connector' = 'datagen',
  'fields.metric.length' = 3,
  'fields.tagvalue.length' = 3,
  'fields.timestamp.min' = 1587539547000,
  'fields.timestamp.max' = 1619075547000,
  'fields.filedvalue.min' = 1,
  'fields.filedvalue.max' = 100000,
  'rows-per-second' = 50
); CREATE TEMPORARY TABLE influxdb_sink(
  `metric` VARCHAR,
  `timestamp` BIGINT,
  `field_fieldValue1` DOUBLE,
  `tag_value1` VARCHAR
) WITH (
  'connector' = 'influxdb',
  'url' = 'https://***********.influxdata.tsdb.aliyuncs.com:****',
  'database' = '<yourDatabaseName>',
  'username' = '<yourDatabaseUserName>',
  'password' = '<yourDatabasePassword>',
  'batchSize' ='100',
  'retentionPolicy' = 'autogen',
  'ignoreErrorData' = 'false'
); INSERT INTO influxdb_sink SELECT
   `metric`,
   `timestamp`,
   `filedvalue`,
   `tagvalue`
FROM datahub_source;
```

##### 流式数据湖仓Paimon结果表

**什么是流式数据湖仓Paimon**

Paimon是一种流批统一的湖存储格式，支持高吞吐的写入和低延迟的查询。目前阿里云开源大数据平台E- MapReduce常见的计算引擎（例如Flink、Spark、Hive或Trino）都与Paimon有着较为完善的集成度。您可以借助Apache Paimon快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并接入上述计算引擎实现数据湖的分析，详情请参见Apache Paimon。

**使用限制**

仅Flink计算引擎VVR 8.0.7及以上版本支持Paimon连接器。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  ...
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 |  | 默认值 | 备注 |
|---|---|---|---|---|---|---|
| connect or | 表类型。 | String | 否 |  | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则固定值为 paimon 。 |
| path | 表存储路径。 | String | 否 |  | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则为表在HDFS或OSS中的存储目录。 |
| auto- create | 创建Paimon临时表时，若指定路径不存在Paimon 表文件，是否自动创建文件。 | Boolean | 否 |  | false | 参数取值如下： false（默认）：如果指定路径不存在Paimon表文件，则报错。 true：如果指定路径不存在，则Flink系统自动创建 Paimon表文件。 |
| bucket | 每个分区的分桶数。 | Integer | 否 |  | 1 | 写入Paimon表的数据将按 bucket-key 打散至每个bucket中。 说明建议每个Bucket的数据量在5 GB以下。 |
| bucket- key | 分桶关键列。 | String | 否 |  |  | 指定将写入Paimon表的数据按哪些列的值打散至不同的Bucket中。 列名之间用英文逗号（,）分隔，例如 'bucket- key' = 'order id,cust id' 会将数据按 _ _ order id列和cust id列的值进行打散。 _ _ 说明如果该参数未填写，则按primary key 进行打散。 如果Paimon表未指定primary key，则按所有列的值进行打散。 |
|  |  |  |  |  | 无 |  |

实时计算（流计算）

| changel og- produc er | 增量数据产生机制。 | String | 否 | non e | Paimon可以为任意输入数据流产生完整的增量数据 （所有的update after数据都有对应的 _ update before数据），方便下游消费者。增量数据 _ 产生机制的可选值如下： none（默认值）：不额外产生增量数据。下游仍然可以流读Paimon表，但读到的增量数据是不完整的（只有update after数据，没有对应的 _ update before数据）。 _ input：将输入数据流双写至增量数据文件中，作为增量数据。 full-compaction：每次Full Compaction产生完整的增量数据。 lookup：每次commit snapshot前产生完整的增量数据。 |
|---|---|---|---|---|---|
| full- compac tion.del ta- commit s | Full Compaction最大间隔。 | Integer | 否 | 无 | 该参数指定了每commit snapshot多少次之后，一定会进行一次Full Compaction。 |
| merge- engine | 相同primary key数据的合并机制。 | String | 否 | ded uplic ate | 参数取值如下： deduplicate：仅保留最新一条。 partial-update：用最新数据中非null的列更新相同primary key的现有数据，其它列保持不变。 aggregation：通过指定聚合函数进行预聚合。 |
| partial- update. ignore- delete | 在partial- update合并机制中，是否忽略 delete消息。 | Boolean | 否 | false | 参数取值如下： true：忽略delete消息。 false：碰到delete消息，Flink系统会报错。 说明并非所有场景下忽略delete消息都是正确的，您需要结合自己的实际场景配置该参数。 |
| partitio n.defau lt-name | 分区默认名称。 | String | 否 | D __ EFA ULT PA _ RTIT ION _ _ | 如果分区列的值为null或空字符串，将会采用该默认名称作为分区名。 |
| partitio n.expir ation- check- interval | 多久检查一次分区过期。 | String | 否 | 1h | 无。 |

实时计算（流计算）

| partitio n.expir ation- time | 分区的过期时长。 | String | 否 | 无 | 当一个分区的存活时长超过该值时，该分区将会过期，默认永不过期。 |
|---|---|---|---|---|---|
| partitio n.times tamp- formatt er | 将时间字符串转换为时间戳的格式串。 | String | 否 | 无 | 无。 |
| partitio n.times tamp- pattern | 将分区值转换为时间字符串的格式串。 | String | 否 | 无 | 无。 |
| snapsh ot.num- retaine d.max | 至多保留几个最新Snapshot不过期。 | Integer | 否 | 214 748 364 7 | 只要满足该配置或snapshot.time-retained其中之一，并同时满足snapshot.num-retained.min，就会触发Snapshot过期。 |
| snapsh ot.num- retaine d.min | 至少保留几个最新Snapshot不过期。 | Integer | 否 | 10 | 无。 |
| snapsh ot.time- retaine d | Snapshot产生多久以后会过期。 | String | 否 | 1h | 只要满足该配置或snapshot.num-retained.max其中之一，并同时满足snapshot.num- retained.min，就会触发snapshot过期。 |
| write- mode | Paimon表的写入模式。 | String | 否 | cha nge- log | 参数取值如下： change-log：Paimon表支持根据primary key进行数据的插入、删除和更新。 append-only：Paimon表只接受数据的插入，且不支持primary key。该模式比change-log模式更加高效。 |
| sink.par allelism | Paimon结果表的并发度。 | Integer | 否 | 无 | 无。 |

**说明**

更多配置项详情请参见Apache Paimon官方文档。

**特色功能详解**

**数据新鲜度与一致性保证**

实时计算（流计算） Paimon结果表使用两阶段提交协议，在每次Flink作业的checkpoint期间提交写入的数据，因此数据新鲜度即为 Flink作业的checkpoint间隔。每次提交将会产生至多两个snapshot。 当两个Flink作业同时写入一张Paimon表时，如果两个作业的数据没有写入同一个分桶，则能保证serializable级别的一致性。如果两个作业的数据写入了同一个分桶，则只能保证snapshot isolation级别的一致性。也就是说，表中的数据可能混合了两个作业的结果，但不会有数据丢失。

**数据合并机制**

当Paimon结果表收到多条具有相同primary key的数据时，为了保持primary key的唯一性，Paimon结果表会将这些数据合并成一条数据。通过指定 `merge-engine` 参数，您可以指定数据合并的具体行为。数据合并机制详情如下表所示。

| 合并机制 | 详情 |  |  |  |
|---|---|---|---|---|
| 去重 （Deduplicate） | 去重机制（deduplicate）是默认的数据合并机制。对于多条具有相同primary key的数据，Paimon结果表仅会保留最新一条数据，并丢弃其它具有primary key的数据。 说明如果最新一条数据是一条delete消息，所有具有该primary key的数据都将被丢弃。 |  |  |  |
| 部分更新（Partial Update） | 通过指定部分更新机制（partial-update），您可以通过多条消息对数据进行逐步更新，并最终得到完整的数据。具体来说，具有相同primary key的新数据将会覆盖原来的数据，但值为null的列不会进行覆盖。 例如，假设Paimon结果表按顺序收到了以下三条数据： <1, 23.0, 10, NULL> <1, NULL, NULL, 'This is a book'> <1, 25.2, NULL, NULL> 第一列是primary key，则最终结果为<1, 25.2, 10, 'This is a book'>。 说明如果需要流读partial-update的结果，必须将 changelog-producer 参数设置为 lookup或full-compaction。 partial-update无法处理delete消息。您可以设置 partial-update.ignore- delete 参数以忽略delete消息。 |  |  |  |
|  |  | partial-update.ignore- |  |  |

|  |  | delete |
|---|---|---|

实时计算（流计算）

|  | 预聚合 （Aggregation） | 部分场景下，可能只关心聚合后的值。预聚合机制（aggregation）将具有相同primary key的数据根据您指定的聚合函数进行聚合。对于不属于primary key的每一列，都需要通过 fields. <field-name>.aggregate-function 指定一个聚合函数，否则该列将默认使用 last non null value 聚合函数。例如，考虑以下Paimon表的定义。 _ _ _ CREATE TABLE MyTable ( product id BIGINT, _ price DOUBLE, sales BIGINT, PRIMARY KEY (product id) NOT ENFORCED _ ) WITH ( 'merge-engine' = 'aggregation', 'fields.price.aggregate-function' = 'max', 'fields.sales.aggregate-function' = 'sum' ); price列将会根据max函数进行聚合，而sales列将会根据sum函数进行聚合。给定两条输入数据 <1, 23.0, 15>和 <1, 30.2, 20>，最终结果为<1, 30.2, 35>。当前支持的聚合函数与对应的数据类型如下： sum：支持DECIMAL、TINYINT、SMALLINT、INTEGER、BIGINT、FLOAT和DOUBLE。 min和max：支持DECIMAL、TINYINT、SMALLINT、INTEGER、BIGINT、FLOAT、 DOUBLE、DATE、TIME、TIMESTAMP和TIMESTAMP LTZ。 _ last value和last non null value：支持所有数据类型。 _ _ _ _ listagg：支持STRING。 bool and和bool or：支持BOOLEAN。 _ _ 说明只有sum函数支持回撤与删除数据，其它聚合函数不支持回撤与删除。如果您需要某些列忽略回撤与删除消息，可以设置 'fields.${field name}.ignore- _ retract'='true' 。 如果需要流读aggregation的结果，必须将 changelog-producer 参数设置为 lookup或full-compaction。 |  |
|---|---|---|---|
|  |  |  | retract'='true' |

|  | <field-name>.aggregate-function |
|---|---|

| 'fields.${field name}.ignore- _ |  |  |
|---|---|---|

**增量数据产生机制**

通过changelog-producer参数设置相应的增量数据产生机制，Paimon可以为任意输入数据流产生完整的增量数据（所有的update_after数据都有对应的update_before数据）。以下列举了所有的增量数据产生机制，更加详细的介绍请参见Apache Paimon官方文档。

| 机制 | 详情 |
|---|---|

实时计算（流计算）

|  | None | 设置 changelog-producer 为none（默认值）后，此时，对于同一个primary key，下游的 Paimon源表只能看到数据的最新情况。但这些最新情况无法让下游消费者方便地了解完整的增量数据，从而进行正确的计算。因为它只能确定对应数据是否被删除了，或最新数据是什么，无法得知更改之前的数据是什么。 例如，假设下游消费者需要计算某一列的总和，如果消费者只看到了最新数据5，它无法断定该如何更新总和。因为如果之前的数据是4，它应该将总和增加1；如果之前的数据是6，它应该将总和减去1。此类消费者对update before较为敏感，建议不要将增量数据产生机制配置为None，但是 _ 其他增量数据产生机制会带来性能损耗。 说明如果您的下游是数据库之类的对update before数据不敏感的消费者，则可以将增量数据产 _ 生机制配置为None。因此，建议您根据实际需要配置增量数据产生机制。 |  |  |
|---|---|---|---|---|
|  | Input | 设置 changelog-producer 为input后，Paimon结果表会将输入数据流双写至增量数据文件中，作为增量数据。 因此，只有当输入数据流本身是完整的增量数据时（例如CDC数据），才能使用这一增量数据产生机制。 |  |  |
|  | Lookup | 设置 changelog-producer 为lookup后，Paimon结果表会通过一种类似于维表的点查机制，在每次commit snapshot之前产生本次snapshot对应的完整增量数据。无论输入数据是否为完整的增量数据，这一增量数据产生机制均能产生完整的增量数据。 与下文的Full Compaction机制相比，Lookup机制产生增量数据的时效性更好，但总体来看耗费的资源更多。 推荐在对增量数据的新鲜度有较高要求（例如分钟级）的情况下使用。 |  |  |
|  |  | 设置 changelog-producer 为full-compaction后，Paimon结果表会在每一次full compaction时产生完整的增量数据。无论输入数据是否为完整的增量数据，这一增量数据产生机制均能产生完整的增量数据。Full compaction的时间间隔由 full-compaction.delta- commits 参数指定。 与上文的Lookup机制相比，Full Compaction机制产生增量数据的时效性更差，但它利用了数据的full compaction过程，不产生额外计算，因此总体来看耗费的资源更少。 推荐在对增量数据的新鲜度要求不高（例如小时级）的情况下使用。 |  |  |
|  |  |  | full-compaction.delta- |  |
|  | Full Compaction | commits |  |  |

**写入模式**

Paimon表目前支持的写入模式如下。

| 模式 | 详情 |
|---|---|
| Change-log | change-log写入模式是Paimon表的默认写入模式。该写入模式支持根据primary key对数据进行插入、删除与更新，您也可以在该写入模式下使用上文提到的数据合并机制与增量数据产生机制。 |

实时计算（流计算）

| Append-only | append-only写入模式仅支持数据的插入，且不支持primary key。该模式比change-log模式更加高效，可在对数据新鲜度要求一般的场景下（例如分钟级新鲜度）作为消息队列的替代品。 关于append-only写入模式的详细介绍，请参见Apache Paimon官方文档。在使用append-only 写入模式时，需要注意以下两点： 建议您根据实际需求设置 bucket-key 参数，否则Paimon表将根据所有列的值进行分桶， 计算效率较低。 append-only写入模式可在一定程度上保证数据的产出顺序，具体的产出顺序为： i. 如果两条数据来自不同的分区，若设置了 scan.plan-sort-partition 参数，则分区值较小的数据将首先产出。否则来自较早创建的分区的数据将首先产出。 ii. 如果两条数据来自同一分区的同一分桶，则较早写入的数据将首先产出。 iii. 如果两条数据来自同一分区的不同分桶，由于不同分桶由不同的并发进行处理，因此不保证两条数据的产出顺序。 |
|---|---|

#### 创建数据维表

##### 云数据库HBase版维表

本文为您介绍云数据库HBase版维表的DDL定义、WITH参数、CACHE参数和转换关系。

**DDL定义**

```
CREATE TABLE hbase_dim(
  rowkey INT,
  family1 ROW<q1 INT>,
  family2 ROW<q2 STRING, q3 BIGINT>,
  family3 ROW<q4 DOUBLE, q5 BOOLEAN, q6 STRING>
) with (
  'connector'='cloudhbase',
  'table-name'='<yourTableName>',
  'zookeeper.quorum'='<yourZookeeperQuorum>'
);
```

HBase的列族（Column Family）必须声明为ROW类型，列族名即该ROW的字段名。例如，DDL定义中声明了family1、family2和family3三个列族。 HBase列族中的列（Cloumn）与对应ROW中嵌套的每个字段对应，列名即字段名。例如，DDL定义中列族 family2声明了q2和q3两列。 除了类型为ROW的字段外，只能有一个原始类型（Atomic Type）的字段（例如STRING或BIGINT），该字段将被视作HBase的行键（Row Key），例如DDL定义中的rowkey。 必须将HBase的行键定义为结果表的主键（Primary Key），如果没有显示定义主键，默认使用行键作为主键。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 cloudhbase 。 |
| table-name | HBase表名 | 是 | 无 |

实时计算（流计算）

| zookeeper. quorum | HBase的zookeeper地址 | 是 | 无 |
|---|---|---|---|
| zookeeper. znode.pare nt | HBase在zookeeper中的根目录 | 否 | 默认值为 /hbase 。 说明仅在HBase标准版中生效。 |
| userName | 用户名 | 否 | 说明仅在HBase增强版中生效。 |
| password | 密码 | 否 | 说明仅在HBase增强版中生效。 |
| haclient.clu ster.id | HBase高可用实例ID | 否 | 只有访问同城主备实例时才需要配置。 说明仅在HBase增强版中生效。 |
| retries.num ber | HBase客户端的重试次数 | 否 | 默认值为31。 |
| null-string- literal | 字段类型为字符串时， 如果HBase中的数据为该值的字节数组，则该字段的值为null。 | 否 | 默认值为Null。 |

**CACHE参数**

| 参数 | 描述 | 是否必选 | 示例值 |
|---|---|---|---|
| cache | 缓存策略 | 否 | 目前云数据库HBase版维表支持以下三种缓存策略： None：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 ALL（默认值）：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查找数据都会通过Cache进行。如果在Cache 中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表 JOIN时，ON条件无法关联）特别多的场景。 需要配置相关参数：缓存更新时间间隔 （cacheTTLMs），更新时间黑名单 （cacheReloadTimeBlackList）。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
| cacheSize | 缓存大小 | 否 | 当缓存策略选择LRU时，可以设置缓存大小，默认为10000行。 |

实时计算（流计算）

| cacheTTLMs | 缓存失效时间，单位为毫秒 |  | 否 | 当缓存策略选择LRU时，可以设置缓存失效时间，默认不过期。 当缓存策略选择ALL时，缓存失效时间为缓存重新加载的间隔时间，默认不重新加载。 |  |  |
|---|---|---|---|---|---|---|
| cacheEmpty | 是否缓存空结果 |  | 否 | 默认值为true。 |  |  |
|  | 更新时间黑名单。在缓存策略选择为ALL |  |  | 默认为空，格式为 2017-10-24 14:00 -> 2017-10- |  |  |
|  |  |  |  |  | 2017-10-24 14:00 -> 2017-10- |  |
|  |  | 更新时间黑名单。在缓存策略选择为ALL |  | 24 15:00, 2017-11-10 23:30 -> 2017-11-11 |  |  |
| cacheReloadTime | 时，启用更新时间黑 |  |  |  |  |  |
|  |  |  | 否 | 08:00 。分隔符的使用情况如下所示： 用逗号 , 来分隔多个黑名单。 用箭头 -> 来分割黑名单的起始结束时间。 |  |  |
| BlackList | 名单，防止在此时间内做Cache更新（例如双11场景）。 |  |  |  |  |  |
| cacheScanLimit | 缓存策略选择ALL时启用。读取全量 HBase数据，RPC（Remote Procedure Call Protocol）服务端一次返回给客户端的行数。 |  | 否 | 默认值为100条。 |  |  |

**转换关系**

HBase数据通过**org.apache.hadoop.hbase.util.Bytes**转换成Flink的数据类型。解码过程有以下两种情况： 对于Flink的非字符串类型，如果HBase中的值为空字节数组，则解码为null。 对于Flink的字符串类型，如果HBase中的值为**null-string-literal**字节数组，则解码为null。 Flink与HBase的数据转换关系如下。

| Flink类型 | HBase转换函数 |
|---|---|
| CHAR | String toString(byte[] b) |
| VARCHAR |  |
| STRING |  |
| BOOLEAN | boolean toBoolean(byte[] b) |
| BINARY | byte[] |
| VARBINARY |  |
| DECIMAL | BigDecimal toBigDecimal(byte[] b) |
| TINYINT | bytes[0] |
| SMALLINT | short toShort(byte[] bytes) |
| INT | int toInt(byte[] bytes) |
| BIGINT | long toLong(byte[] bytes) |
| FLOAT | float toFloat(byte[] bytes) |
| DOUBLE | double toDouble(byte[] bytes) |

实时计算（流计算）

| DATE | HBase字节数组通过int toInt(byte[] bytes) 转换成int，表示自1970.01.01以来的天数。 |
|---|---|
| TIME | HBase字节数组通过int toInt(byte[] bytes) 转换成int，表示自00:00:00以来的毫秒数。 |
| TIMESTAMP | HBase字节数组通过long toLong(byte[] bytes) 转换成long，表示自1970-01- 01 00:00:00以来的毫秒数。 |
| ARRAY | 不支持 |
| MAP / MULTISET | 不支持 |
| ROW | 不支持 |

**代码示例**

包含HBase维表的实时计算作业代码示例如下。

```
CREATE TABLE datagen_source (
  a INT,
  b BIGINT,
  c STRING,
  `proc_time` AS PROCTIME()
) with (
  'connector'='datagen'
); CREATE TABLE hbase_dim (
  rowkey INT,
  family1 ROW<col1 INT>,
  family2 ROW<col1 STRING, col2 BIGINT>,
  family3 ROW<col1 DOUBLE, col2 BOOLEAN, col3 STRING>
) WITH (
  'connector' = 'cloudhbase',
  'table-name' = '<yourTableName>',
  'zookeeper.quorum' = '<yourZookeeperQuorum>'
); CREATE TABLE blackhole_sink(
  a INT,
  f1c1 INT,
  f3c3 STRING
) with (
  'connector' = 'blackhole'
); INSERT INTO blackhole_sink
     SELECT a, family1.col1 as f1c1,  family3.col3 as f3c3 FROM datagen_source
JOIN hbase_dim FOR SYSTEM_TIME AS OF src.`proc_time` as h ON src.a = h.rowkey;
```

##### 表格存储Tablestore维表

本文为您介绍表格存储Tablestore维表DDL定义、WITH参数和CACHE参数。

**什么是表格存储Tablestore**

实时计算（流计算） 表格存储Tablestore是构建在阿里云飞天分布式系统之上的分布式NoSQL数据存储服务。表格存储通过数据分片和负载均衡技术，实现数据规模与访问并发的无缝扩展，提供海量结构化数据的存储和实时访问服务。

**DDL定义**

```
CREATE TABLE ots_dim (
   id int,
   len int,
   content STRING
) WITH (
   'connector'='ots',
   'endPoint'='<yourEndpoint>',
   'instanceName'='<yourInstanceName>',
   'tableName'='<yourTableName>',
   'accessId'='<yourAccessId>',
   'accessKey'='<yourAccessKey>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 ots 。 |
| instanceName | 实例名 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| endPoint | 实例访问地址 | 是 | 无 |
| accessId | AccessKey ID | 是 | 无 |
| accessKey | AccessKey Secret | 是 | 无 |
| retryIntervalMs | 重试间隔时间 | 否 | 单位毫秒，默认值为1000（1 秒）。 |
| maxRetryTimes | 最大重试次数 | 否 | 默认值为100。 |
| connectTimeout | Connector连接Tablestore的超时时间 | 否 | 单位毫秒，默认值为 30000（30秒）。 |
| socketTimeout | Connector连接Tablestore的 Socket超时时间 | 否 | 单位毫秒，默认值为 30000（30秒）。 |

**CACHE参数**

| 参数 | 说明 | 备注 |
|---|---|---|
| cache | 缓存策略 | 表格存储维表支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 |

实时计算（流计算）

| cacheSize | 缓存大小 | 当选择LRU缓存策略后，可以设置缓存大小，默认值为 10000行。 |
|---|---|---|
| cacheTTLMs | 缓存超时时间 | 单位为毫秒，当选择LRU缓存策略后，可以设置缓存失效的超时时间。 |

**常见问题**

Q：维表进行JOIN时，查询不到数据，应该如何处理？

##### MaxCompute维表

本文为您介绍MaxCompute维表的DDL定义、WITH参数、CACHE参数、类型映射和常见问题。

**DDL定义**

```
create table odps_dim(
    id VARCHAR,
    name VARCHAR,
    age int,
    PRIMARY KEY (id, name) not enforced
) with (
    'connector' = 'odps',
    'endpoint' = '<yourEndpoint>',
    'tunnelEndpoint' = '<yourTunnelEndpoint>',
    'project' = '<yourProjectName>',
    'tablename' = '<yourTableName>',
    'accessid' = '<yourAccessKeyId>',
    'accesskey' = '<yourAccessKeySecret>',
    'partition' = 'ds=2018****',
    'cache' = 'ALL'
);
```

**说明**

声明维表时，必须要指名主键，MaxCompute维表主键必须具有唯一性，否则会被去重。 在维表进行JOIN时，ON条件必须包含所有主键的等值条件。 主键字段必须按照PRIMARY KEY括号中字段的先后顺序，放在非主键字段之前。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 odps 。 |
| endPoint | MaxCompute服务地址 | 是 | 请联系阿里云运维工程师获取。 |
| tunnelEndpoi nt | MaxCompute Tunnel服务的连接地址 | 是 | 请联系阿里云运维工程师获取。 |

实时计算（流计算）

| project | MaxCompute项目名称 | 是 | 无 |  |  |
|---|---|---|---|---|---|
| tableName | 表名 | 是 | 无 |  |  |
| accessId | AccessKey ID | 是 | 无 |  |  |
| accessKey | AccessKey Secret | 是 | 无 |  |  |
| partition | 分区名 | 否 | 固定分区只存在一个分区MaxCompute表例如，如果只存在1个分区列 ds ， 则 `partition` = 'ds=20180905' 表示读 ds=20180905 分区的数据。 存在多个分区的MaxCompute表例如，如果存在2个分区列 ds 和 hh ， 则 `partition`='ds=20180905,hh=*' 表示读 ds=20180905 分区的数据。 说明分区过滤时需要声明所有分区的值。 例如，上述示例中，只声明 `partition` = 'ds=20180905' ，则不会读取任何分区。 非固定分区支持 `partition` = 'max pt()' ， 即每次加 _ 载所有分区列表中字典序最大的分区。 支持 `partition` = 'max pt with done()' ，即每次加载所有分区列 _ _ _ 表中字典序最大且伴随有 .done 的分区。 |  |  |

|  |  | 'ds=20180905' |
|---|---|---|

|  |  | `partition` = |  |
|---|---|---|---|
|  | 'max pt with done()' _ _ _ |  |  |

**CACHE参数**

| 参数 | 参数说明 | 备注 |
|---|---|---|

实时计算（流计算）

| cache |  | 缓存策略 | 目前MaxCompute维表仅支持 ALL 策略，必须显式声明。 ALL策略：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查询都会通过Cache进行。 如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。需要配置缓存更新时间间隔 （cacheTTLMs）和更新时间黑名单 （cacheReloadTimeBlackList）参数。 说明因为系统会异步加载维表数据，所以在使用CACHE ALL时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的至少4倍，具体值与MaxCompute 存储压缩算法有关。 在使用超大MaxCompute维表时，如果频繁 GC（Allocation Failure）导致作业异常，且在增加维表JOIN节点的内存仍无改善的情况下，建议改为支持 LRU cache策略的KV型维表，例如云数据库Hbase版维表。 |  |
|---|---|---|---|---|
| cacheSize |  | 缓存大小 | 可以设置缓存大小，MaxCompute默认缓存值为100000行。 |  |
| cacheTTLMs |  | 缓存超时时间 | 单位为毫秒，如果cache选择为 ALL 策略，则为缓存加载的间隔时间，默认为不重新加载。 |  |
| cacheReloa dTimeBlack List |  |  | 默认为空，格式为 2017-10-24 14:00 -> 2017-10-24 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00 。分隔符的使用情况如下所示： 用逗号 , 来分隔多个黑名单。 用箭头 -> 来分割黑名单的起始结束时间。 |  |
|  |  |  |  | 2017-10-24 14:00 -> 2017-10-24 |
|  | a | 更新时间黑名单。在缓存策略选 | 15:00, 2017-11-10 23:30 -> 2017-11-11 08:00 |  |
|  |  | 择为ALL时，启用更新时间黑名单，防止在此时间内做Cache更新（例如双11场景）。 |  |  |

**类型映射**

| MaxCompute字段类型 | Flink字段类型 |
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

实时计算（流计算）

| STRING | VARCHAR |
|---|---|
| DECIMAL | DECIMAL |
| BINARY | VARBINARY |

##### 云数据库Redis版维表

本文为您介绍云数据库Redis维表DDL定义、WITH参数、CACHE参数、类型映射和代码示例。

**重要**

Redis维表仅支持引用Redis数据存储中STRING类型的数据。 Redis维表必须声明且只能声明一个主键。 Redis维表仅支持声明两个字段，且字段类型必须为STRING。 维表JOIN时，ON条件必须包含所有主键的等值条件。 Redis仅支持None和LRU两种缓存策略。 支持自建Redis服务。

**什么是云数据库Redis版**

阿里云数据库Redis版是兼容开源Redis协议标准、提供内存加硬盘混合存储的数据库服务，基于高可靠双机热备架构及可平滑扩展的集群架构，充分满足高吞吐、低延迟及弹性变配的业务需求。

**DDL定义**

```
CREATE TABLE redis_dim (
  id STRING,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>',
  'dbNum' = '<yourDbNum>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 redis 。 |
| host | Redis连接地址 | 是 | 无 |
| port | Redis连接端口 | 否 | 默认值为6379。 |
| dbNum | 选择操作的数据库 | 否 | 默认值为0。 |
| password | Redis密码 | 否 | 默认值为空，不进行权限验证。 |
| clusterMode | Redis集群是否为cluster 模式。 | 否 | 默认值为false。 |

实时计算（流计算）

| hashName | Hash模式下的Hash Key 名称。 | 否 | 默认值为空。通常，Redis维表中的数据类型为 STRING类型，即 key-value 对。如果设置hashName参数，则Redis维表中的数据类型为 HASHMAP类型，即 key-{field-value} 对，其中： key为hashName参数值。 field为您在CREATE TABLE中指明的key参数值。 value为key对应的赋值，和STRING类型 key- value 中value语义相同。 |
|---|---|---|---|

| key- |  |
|---|---|

|  | value |
|---|---|

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | 云数据库Redis维表支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据，如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小（cacheSize）和缓存更新时间间隔（cacheTTLMs）。 |
| cacheSize | 缓存大小 | 否 | 选择LRU缓存策略后，可以设置缓存大小，默认为10000 行。 |
| cacheTTLMs | 缓存超时时长 | 否 | 默认缓存不超时，单位为毫秒。可选LRU缓存策略，即设置缓存失效的超时时长。 |
| cacheEmpty | 是否缓存空结果 | 否 | 默认值为true。 |

**类型映射**

| Redis字段类型 | Flink字段类型 |
|---|---|
| STRING | VARCHAR |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
  id STRING,
  data STRING,
  proctime as PROCTIME()
) with (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE redis_dim (
  id STRING,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED --Redis中的Row Key字段。
) WITH (
  'connector' = 'redis',
  'host' = '<yourHost>',
  'port' = '<yourPort>',
  'password' = '<yourPassword>'
); CREATE TEMPORARY blackhole_sink (
  id STRING,
  data STRING,
  name STRING
) WITH (
  'connector' = 'blackhole'
); INSERT INTO blackhole_sink SELECT e.*, w.* FROM datagen_source AS e JOIN redis_dim FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

##### Elasticsearch维表

本文为您介绍Elasticsearch（ES）维表DDL定义、WITH参数、CACHE参数和代码示例。 该Connector支持的功能是和阿里云Elasticsearch产品对齐的，暂不支持HTTPS加密访问形

**说明**

式。

**DDL定义**

```
 CREATE TABLE es_dim(
```

`field1 LONG, ---`作为`JOIN`时的`key`，必须为`STRING`类型。

```
   field2 VARBINARY,
   field3 VARCHAR
) WITH (
   'connector' ='elasticsearch',
   'endPoint' = '<yourEndPoint>',
   'accessId' = '<yourAccessId>',
   'accessKey' = '<yourAccessSecret>',
   'indexName' = '<yourIndexName>',
   'typeNames' = '<yourTypeName>'
);
```

实时计算（流计算）

**说明**

维表JOIN时的key有且只能有1个，且为Elasticsearch对应索引的文档ID。 支持Elasticsearch 5.5及以上版本。

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 elasticsearch 。 |
| endPoint | Server地址 | 是 | 请联系阿里云运维工程师获取。 |
| accessId | Elasticsearch实例的用户名 | 否 | 无 |
| accessKey | Elasticsearch实例的密码 | 否 | 无 |
| indexName | 文档索引名称 | 是 | 无 |
| typeNames | Type名称 | 否 | 默认值为 doc 。 _ 说明 Elasticsearch 7.0以上版本不建议设置该参数。 |

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | Elasticsearch仅支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据， 如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小 （cacheSize）和缓存更新时间间隔 （cacheTTLMs）。 |
| cacheSize | 缓存大小 | 否 | 选择 LRU 缓存策略后，可以设置缓存大小， 默认值为10000行。 |
| cacheTTLMs | 缓存更新时间间隔 | 否 | 默认缓存不超时，单位为毫秒。不同缓存策略下的功能如下： LRU：设置缓存失效的超时时长。 ALL：设置缓存加载的间隔时长，默认不重新加载。 |
| cacheEmpty | 是否缓存空结果。 | 否 | 默认值为true。 |

**类型映射**

Flink以JSON来解析Elasticsearch数据，详情请参见数据类型映射关系。

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
   id STRING,
   data STRING,
   proctime as PROCTIME()
) with (
   'connector' = 'datagen'
); CREATE TEMPORARY TABLE es_dim (
   id STRING,
   `value` FLOAT
) WITH (
   'connector' ='elasticsearch',
   'endPoint' = '<yourEndPoint>',
   'accessId' = '<yourAccessId>',
   'accessKey' = '<yourAccessSecret>',
   'indexName' = '<yourIndexName>',
   'typeNames' = '<yourTypeName>'
); CREATE TEMPORARY TABLE blackhole_sink (
  id STRING,
  data STRING,
  `value` FLOAT
) WITH (
  'connector' = 'blackhole'
); INSERT INTO blackhole_sink SELECT e.*, w.*
  FROM datagen_source AS e
JOIN es_dim FOR SYSTEM_TIME AS OF e.proctime AS w ON e.id = w.id;
```

##### 交互式分析Hologres维表

本文为您介绍交互式分析Hologres维表DDL定义、WITH参数、CACHE参数和代码示例。

**什么是交互式分析Hologres**

交互式分析Hologres兼容PostgreSQL协议，与大数据生态紧密连接，支持高并发、低延时实时分析处理PB级数据，让您轻松使用现有BI（Business Intelligence）工具对数据进行多维分析和业务探索。

**使用限制**

创建Hologres维表时建议选择行存模式，列存模式对于点查场景性能开销较大。 选择行存模式创建维表时必须设置主键，并且将主键设置为clustering key才可以工作。示例语句如下：

```
begin; create table test(a int primary key, b text, c text, d float8, e int8); call set_table_property('test', 'orientation', 'row'); call set_table_property('test', 'clustering_key', 'a'); commit;
```

Hologres维表的主键必须是Flink Join On的字段，Flink Join On的字段也必须是维表完整的主键字段，两者必须完全匹配。 实时计算（流计算） Hologres Flink Connector的维表功能不支持一对多的输出。

**DDL定义**

```
CREATE TABLE hologres_dim(
 id INT,
 len INT,
 content VARCHAR
) with (
  'connector'='hologres',
  'dbname'='<yourDbname>',
  'tablename'='<yourTablename>',
  'username'='<yourUsername>',
  'password'='<yourPassword>',
  'endpoint'='<yourEndpoint>'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 hologres （小写）。 |
| endPoint | hologres endpoint | 是 | 请联系阿里云运维工程师获取。 |
| tablename | 表名称说明如果Schema不为Public时，则 tableName需要填写为schema.ta bleName。 | 是 | 无。 |
| dbname | 数据库名称 | 是 | 无。 |
| username | 用户名，请填写阿里云账号的AccessKey ID。 | 是 | 无。 |
| password | 密码，请填写阿里云账号的AccessKey Secret。 | 否 | 无。 |
| connectionSize | 单个Flink结果表任务所创建的JDBC连接池大小。 | 否 | 默认值大小为3。如果作业性能不足，建议您增加连接池大小。连接池大小和数据吞吐成正比。 |

实时计算（流计算）

| connectionPoolNa me | 连接池名称。同一个 TaskManager中， 配置相同名称的连接池的表可以共享连接池。 | 否 | 取值为非 'default' 的任意字符串。如果多个表设置相同的连接池，则这些使用相同连接池的表的connectionSize参数也需要相同。 说明此参数可以按需配置，例如作业中有维表 A，B以及结果表C，D，E五张hologres 表，可以A表和B表使用pool1，C表和D 表使用pool2，E表流量较大，单独使用 pool3。 |
|---|---|---|---|

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | Hologres仅支持以下两种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在Cache中查找数据， 如果没有找到，则去物理维表中查找。 需要配置相关参数：缓存大小 （cacheSize）和缓存更新时间间隔 （cacheTTLMs）。 |
| cacheSize | 缓存大小 | 否 | 选择 LRU 缓存策略后，可以设置缓存大小， 默认值为10000行。 |
| cacheTTLMs | 缓存更新时间间隔 | 否 | 当选择LRU缓存策略后，可以设置缓存失效的超时时间，默认不过期。 |
| async | 是否异步同步数据 | 否 | 取值如下： true：表示异步同步数据。 false（默认值）：表示不进行异步同步数据。 |

**类型映射**

| Hologres字段类型 | Flink字段类型 |
|---|---|
| INT | INT |
| INT[] | ARRAY |
| BIGINT | BIGINT |

实时计算（流计算）

| BIGINT[] | ARRAY |
|---|---|
| REAL | FLOAT |
| REAL[] | ARRAY |
| DOUBLE PRECISION | DOUBLE |
| DOUBLE PRECISION[] | ARRAY |
| BOOLEAN | BOOLEAN |
| BOOLEAN[] | ARRAY |
| TEXT | VARCHAR |
| TEXT[] | ARRAY |
| NUMERIC | DECIMAL |
| DATE | DATE |
| TIMESTAMP WITH TIMEZONE | TIMESTAMP |

**说明**

上表中未列出的Hologres类型，Connector还未支持转换。

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source (
   a INT,
   b BIGINT,
   c STRING,
   proctime AS PROCTIME()
) with (
   'connector' = 'datagen'
); CREATE TEMPORARY TABLE hologres_dim (
   a INT,
   b VARCHAR,
   c VARCHAR
) with (
   'connector' = 'hologres',
   ...
); CREATE TEMPORARY TABLE blackhole_sink (
   a INT,
   b STRING
) with (
   'connector' = 'blackhole'
); insert into blackhole_sink select T.a,H.b FROM datagen_source AS T JOIN hologres_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

##### 云数据库RDS MySQL维表

本文为您介绍云数据库RDS MySQL维表DDL定义、WITH参数、CACHE参数、类型映射和代码示例。

**语法示例**

```
CREATE TABLE rds_dim (
  id1 INT,
  id2 VARCHAR
) WITH (
  'connector' = 'rds',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>',
  'cache' = 'ALL'
);
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 rds 。 |

实时计算（流计算）

| password | 密码 | 是 | 无 |
|---|---|---|---|
| tableName | 表名 | 是 | 无 |
| url | URL地址 | 是 | 请联系阿里云运维工程师获取。 |
| userName | 用户名 | 是 | 无 |
| maxRetryTim es | 写入数据失败后， 重试写入的次数 | 否 | 默认值为3。 |
| CACHE | 缓存策略、缓存大小和缓存超时时间 | 否 | 详情请参见CACHE参数。 |

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| cache | 缓存策略 | 否 | 云数据库RDS（DRDS）版维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在 Cache中查找数据，如果没有找到，则去物理维表中查找。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查找数据都会通过Cache进行。 如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 说明使用ALL或LRU缓存策略时，必须配置cacheSize参数。 如果使用CACHE ALL时，请注意节点内存大小，防止出现 OOM。 因为系统会异步加载维表数据，所以在使用CACHE ALL 时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
| cacheS ize | 缓存大小 | 否 | 默认为空，即未配置该参数，当选择LRU或者ALL缓存策略后，必须设置缓存大小。 |
| cacheT TLMs | 缓存超时时间，单位为毫秒 | 否 | 当选择 LRU 缓存策略后，可以设置缓存失效的超时时间。当选择 ALL 策略，则为缓存加载的间隔时间，默认值为10s。 |

|  | LRU |
|---|---|
| ALL |  |

**类型映射**

| RDS字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | TINYINT |
| SMALLINT | SMALLINT |
| TINYINT UNSIGNED | SMALLINT |
| INT | INT |

实时计算（流计算）

| SMALLINT UNSIGNED | INT |
|---|---|
| BIGINT | BIGINT |
| INT UNSIGNED | BIGINT |
| BIGINT UNSIGNED | DECIMAL(20,0) |
| FLOAT | FLOAT |
| DECIMAL | DECIMAL |
| DOUBLE | DOUBLE |
| DATE | DATE |
| TIME | TIME |
| TIMESTAMP | TIMESTAMP |
| VARCHAR | VARCHAR |
| VARBINARY | VARBINARY |

**代码示例**

```
CREATE TEMPORARY TABLE datagen_source(
  a INT,
  b BIGINT,
  c STRING,
  `proctime` AS PROCTIME()
) with (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE rds_dim (
  a INT,
  b VARCHAR,
  c VARCHAR
) with (
  'connector' = 'rds',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = 'jdbc:mysql://xxx',
  'userName' = '<yourUsername>'
); CREATE TEMPORARY TABLE blackhole_sink(
  a INT,
  b STRING
) with (
  'connector' = 'blackhole'
); insert into blackhole_sink select T.a,H.b FROM datagen_source AS T JOIN rds_dim FOR SYSTEM_TIME AS OF T.`proctime` AS H ON T.a = H.a;
```

实时计算（流计算）

##### 云原生数据仓库AnalyticDB MySQL版3.0维表

本文为您介绍云原生数据仓库AnalyticDB MySQL版3.0维表的DDL定义、WITH参数、CACHE参数和类型映射。

**DDL定义**

```
CREATE TABLE adb30_dim (
    id1 INT,
    id2 VARCHAR
) WITH (
    'connector' = 'adb3.0',
    'password' = '<yourPassword>',
    'tableName' = '<yourTablename>',
    'url' = '<yourUrl>',
    'userName' = '<yourUsername>',
    'cache' = 'ALL',
    'cacheSize' = '500'
);
```

**WITH参数**

| 参数 | 注释说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为 adb3.0 。 |
| password | 密码 | 是 | 无 |
| tableName | 表名 | 是 | 无 |
| url | URL地址 | 是 | 云原生数据仓库AnalyticDB MySQL版3.0的专有网络 VPC地址。 |
| username | 用户名 | 是 | 无 |
| maxRetryTimes | 写入数据失败后，重试写入的次数 | 否 | 默认值为3。 |
| CACHE | 缓存策略、缓存大小和缓存超时时间 | 否 | 详情请参见CACHE参数。 |

**CACHE参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|

实时计算（流计算）

| cache | 缓存策略 | 否 | 云原生数据仓库AnalyticDB MySQL版3.0维表支持以下三种缓存策略： None（默认值）：无缓存。 LRU：缓存维表里的部分数据。源表的每条数据都会触发系统先在 Cache中查找数据，如果没有找到，则去物理维表中查找。 ALL：缓存维表里的所有数据。在Job运行前，系统会将维表中所有数据加载到Cache中，之后所有的维表查找数据都会通过Cache进行。 如果在Cache中无法找到数据，则KEY不存在，并在Cache过期后重新加载一遍全量Cache。 适用于远程表数据量小且MISS KEY（源表数据和维表JOIN时，ON条件无法关联）特别多的场景。 说明使用ALL或LRU缓存策略时，必须配置cacheSize参数。 如果使用CACHE ALL时，请注意节点内存大小，防止出现 OOM。 因为系统会异步加载维表数据，所以在使用CACHE ALL 时，需要增加维表JOIN节点的内存，增加的内存大小为远程表数据量的两倍。 |
|---|---|---|---|
| cacheS ize | 缓存大小，即缓存多少行数据。 | 否 | cacheSize配置和cache有关： 如果cache配置为None，则不用配置cacheSize参数（默认为空）。 如果cache配置为LRU，则必须配置cacheSize参数。 如果cache配置为ALL，则必须配置cacheSize参数。 |
| cacheT TLMs | 缓存超时时间，单位为毫秒 | 否 | cacheTTLMs配置和cache有关： 如果cache配置为ALL，则cacheTTLMs为缓存加载的间隔时间，默认值为10000ms。 如果cache配置为LRU，则cacheTTLMs为缓存失效的超时时间， 默认值为10000ms。 |

**类型映射**

| 云原生数据仓库AnalyticDB MySQL版3.0字段类型 | Flink字段类型 |
|---|---|
| BOOLEAN | BOOLEAN |
| TINYINT | INT |
| SMALLINT | INT |
| INT | INT |
| BIGINT | BIGINT |
| DOUBLE | DOUBLE |
| VARCHAR | VARCHAR |
| DATETIME | TIMESTAMP |
| DATE | DATE |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE datagen_source(
  a INT,
  b VARCHAR,
  c STRING,
  `proctime` AS PROCTIME()
) with (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE adb_dim (
  a INT,
  b VARCHAR,
  c VARCHAR
) with (
  'connector' = 'adb3.0',
  'password' = '<yourPassword>',
  'tableName' = '<yourTablename>',
  'url' = '<yourUrl>',
  'userName' = '<yourUsername>'
); CREATE TEMPORARY TABLE blackhole_sink(
  a INT,
  b VARCHAR
) with (
  'connector' = 'blackhole'
); insert into blackhole_sink select T.a,H.b FROM datagen_source AS T JOIN adb_dim FOR SYSTEM_TIME AS OF T.proctime AS H ON T.a = H.a;
```

##### Lindorm维表

本文为您介绍云原生多模数据库Lindorm的宽表作为维表的DDL定义、WITH参数、类型映射和代码示例。

**什么是云原生多模数据库Lindorm**

Lindorm是面向物联网、互联网、车联网等设计和优化的云原生多模超融合数据库，适用于日志、监控、账单、 广告、社交、出行、风控等场景，也是为阿里巴巴核心业务提供支撑的数据库之一。 Lindorm具备以下特性： 支持宽表、时序、文本、对象、流、空间等多种数据的统一访问和融合处理。 兼容SQL、HBase/Cassandra/S3、TSDB、HDFS、Solr、Kafka等多种标准接口和无缝集成三方生态工具。

**使用限制**

仅Flink计算引擎VVR 4.0.8及以上版本支持Lindorm。

**注意事项**

声明维表时，必须要指名主键，维表JOIN时，ON的条件必须包含所有主键的等值条件。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE white_list ( id varchar, name varchar, age int, PRIMARY KEY (id) NOT ENFORCED ) WITH ( 'connector' = 'lindorm', 'seedserver' = '<yourSeedServer>', 'namespace' = '<yourNamespace>', 'username' = '<yourUsername>', 'password' = '<yourPassword>', 'tableName' = '<yourTableName>', 'columnFamily' = '<yourColumnFamily>' );
```

**WITH参数**

| 参数 | 说明 | 是否必填 | 备注 |
|---|---|---|---|
| connector | 表类型。 | 是 | 固定值为lindorm。 |
| seedserver | Lindorm服务器的连接地址。 | 是 | 实时计算Flink版使用HBase Java API的方式连接并使用Lindorm宽表引擎。Lindorm服务器的连接地址的格式为 host:port 。 |
| namespace | Lindorm的命名空间。 | 是 | 无。 |
| username | 连接Lindorm所用到的用户名。 | 是 | 无。 |
| password | 连接Lindorm所用到的密码。 | 是 | 无。 |
| tableName | Lindorm表名。 | 是 | 无。 |
| columnFamily | Lindorm表的列族名。 | 是 | 如果创建Lindorm表时未指定列族名，则需要您填写为f。 |
| retryInterval Ms | 读取失败时，再次重试读取的时间间隔。 | 否 | 单位为ms，默认值为1000ms。 |
| maxRetryTim es | 最大尝试次数。 | 否 | 默认值为5次。 |

实时计算（流计算）

| partitionedJoi n | 是否额外使用JoinKey进行分区。 | 否 | 参数取值如下： true：用JoinKey进行分区，将数据分发到Join节点，提高缓存命中率。 false（默认值）：不使用JoinKey进行分区。 |
|---|---|---|---|
| shuffleEmpty Key | 遇到空Key时，是否将Key为空的记录随机向下游 Shuffle。 | 否 | 参数取值如下： true：随机往下游做Shuffle。 false（默认值）：从下游中编号为0的并发开始做Shuffle，即从第一个并发开始。 |
| cache | 缓存策略。 | 否 | 目前Lindorm支持以下两种缓存策略： None（默认值）：无缓存。 LRU：只保留最近使用的数据。 需要配置相关参数：缓存大小（cacheSize）和缓存失效超时时间（cacheTTLMs）。 |
| cacheSize | 缓存数据的行数。 | 否 | 默认值为10000行。当选择LRU缓存策略后，可以设置缓存大小。 |
| cacheTTLMs | 缓存失效超时时间。 | 否 | 单位为毫秒。当选择LRU缓存策略后，可以设置缓存失效的超时时间，默认不过期。 |
| cacheEmpty | 是否缓存join结果为空的数据。 | 否 | 无。 |
| async | 是否异步返回数据。 | 否 | 参数取值如下： true：表示异步返回数据。 false（默认值）：表示不进行异步返回数据。 |
| asyncLindorm RpcTimeoutM s | 在异步请求数据时的超时时间。 | 否 | 单位ms，默认值是300000ms。 |

**类型映射**

Lindorm中数据均为二进制形式，通过Flink某个字段类型来转换或解析二进制的Bytes方法如下。

| Flink SQL类型 | 从Lindorm读取Bytes之后的解析 |
|---|---|
| CHAR | org.apache.flink.table.data.StringData::fromBytes |
| VARCHAR |  |
| BOOLEAN | com.alibaba.lindorm.client.core.utils.Bytes::toBigDecimal |

实时计算（流计算）

| BINARY | 直接返回bytes。 |
|---|---|
| VARBINARY |  |
| DECIMAL | com.alibaba.lindorm.client.core.utils.Bytes::toBigDecimal |
| TINYINT | 直接返回bytes[0]。 |
| SMALLINT | com.alibaba.lindorm.client.core.utils.Bytes::toShort |
| INT | com.alibaba.lindorm.client.core.utils.Bytes::toInt |
| BIGINT | com.alibaba.lindorm.client.core.utils.Bytes::toLong |
| FLOAT | com.alibaba.lindorm.client.core.utils.Bytes::toFloat |
| DOUBLE | com.alibaba.lindorm.client.core.utils.Bytes::toDouble |
| DATE | com.alibaba.lindorm.client.core.utils.Bytes::toInt 得到自1970.01.01以来的天数。 |
| TIME | com.alibaba.lindorm.client.core.utils.Bytes::toInt 得到自当天00:00:00以来的毫秒数。 |
| TIMESTAMP | com.alibaba.lindorm.client.core.utils.Bytes::toLong 得到自1970.01.01 00:00:00以来的毫秒数。 |

**代码示例**

实时计算（流计算）

```
CREATE TEMPORARY TABLE example_source(
 id INT,
 proc_time AS PROCTIME()
) WITH (
 'connector' = 'datagen',
 'number-of-rows' = '10',
 'fields.id.kind' = 'sequence',
 'fields.id.start' = '0',
 'fields.id.end' = '9'
); CREATE TEMPORARY TABLE lindorm_hbase_dim(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_dim_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); CREATE TEMPORARY TABLE lindorm_hbase_sink(
 `id` INT,
 `name` VARCHAR,
 `birth` VARCHAR,
 PRIMARY KEY (id) NOT ENFORCED
) WITH (
 'connector'='lindorm',
 'tablename'='${lindorm_sink_table}',
 'seedserver'='${lindorm_seed_server}',
 'namespace'='default',
 'username'='${lindorm_username}',
 'password'='${lindorm_username}'
); INSERT INTO lindorm_hbase_sink SELECT example_source.id as id, lindorm_hbase_dim.name as name, lindorm_hbase_dim.birth as b irth FROM example_source JOIN lindorm_hbase_dim FOR SYSTEM_TIME AS OF PROCTIME() ON example_sourc e.id = lindorm_hbase_dim.id;
```

##### FileSystem维表

本文为您介绍FileSystem维表的DDL定义，以及创建维表时使用的WITH参数和代码示例。

**DDL定义**

实时计算（流计算）

```
CREATE TABLE filesystem_dim (
  id STRING,
  name STRING
) WITH (
  'connector' = 'filesystem',
  'path' = 'csv/json/avro/parquet/orc/raw',
  'format' = 'CSV'
```

)

**WITH 参数**

| 参数 | 说明 | 是否必选 | 备注 |
|---|---|---|---|
| connector | 维表类型 | 是 | 固定值为filesystem。 |
| path | 文件路径 | 是 | URI格式，例如：oss://my path/my file。 _ _ |
| format | 文件格式 | 是 | 参数取值如下： CSV JSON AVRO PARQUET ORC RAW format参数详情请参见formats。 |
| lookup.join.cac he.ttl | 重新读取数据的TTL时间 | 否 | 默认值为60分钟，即每隔60分钟重新读取数据。 |

**代码示例**

实时计算（流计算） `--`创建`event`源表。

```
CREATE TABLE event (
  id STRING,
  data STRING
) WITH (
  'connector' = 'datahub'
   ...
);
```

`--`创建`white_list`维表。

```
CREATE TABLE white_list (
  id STRING,
  name STRING,
) WITH (
  'connector' = 'filesystem',
  'path' = '${remote_path_uri}',
  'format' = '${format}'
);
```

`--`关联`event`源表和`white_list`维表。

```
SELECT e.*, w.* FROM event AS e JOIN white_list FOR SYSTEM_TIME AS OF proctime() AS w ON e.id = w.id;
```

##### 流式数据湖仓Paimon维表

**什么是流式数据湖仓Paimon**

Paimon是一种流批统一的湖存储格式，支持高吞吐的写入和低延迟的查询。目前阿里云开源大数据平台E- MapReduce常见的计算引擎（例如Flink、Spark、Hive或Trino）都与Paimon有着较为完善的集成度。您可以借助Apache Paimon快速地在HDFS或者云端OSS上构建自己的数据湖存储服务，并接入上述计算引擎实现数据湖的分析，详情请参见Apache Paimon。

**使用限制**

仅Flink计算引擎VVR 8.0.7及以上版本支持Paimon连接器。

**DDL定义**

```
CREATE TABLE paimon_table (
  id BIGINT,
  data STRING,
  PRIMARY KEY (id) NOT ENFORCED
) WITH (
  ...
);
```

**WITH参数**

| 参数 | 说明 | 数据类型 | 是否必填 | 默认值 | 备注 |
|---|---|---|---|---|---|

实时计算（流计算）

| connect or | 表类型。 | String | 否 |  | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则固定值为 paimon 。 |
|---|---|---|---|---|---|---|
| path | 表存储路径。 | String | 否 |  | 无 | 如果在Paimon Catalog中创建Paimon表，则无需填写。 如果在其他Catalog中创建Paimon临时表，则为表在HDFS或OSS中的存储目录。 |
| auto- create | 创建Paimon临时表时，若指定路径不存在Paimon 表文件，是否自动创建文件。 | Boolean | 否 |  | false | 参数取值如下： false（默认）：如果指定路径不存在Paimon表文件，则报错。 true：如果指定路径不存在，则Flink系统自动创建 Paimon表文件。 |
| bucket | 每个分区的分桶数。 | Integer | 否 |  | 1 | 写入Paimon表的数据将按 bucket-key 打散至每个bucket中。 说明建议每个Bucket的数据量在5 GB以下。 |
| bucket- key | 分桶关键列。 | String | 否 |  |  | 指定将写入Paimon表的数据按哪些列的值打散至不同的Bucket中。 列名之间用英文逗号（,）分隔，例如 'bucket- key' = 'order id,cust id' 会将数据按 _ _ order id列和cust id列的值进行打散。 _ _ 说明如果该参数未填写，则按primary key 进行打散。 如果Paimon表未指定primary key，则按所有列的值进行打散。 |
|  |  |  |  |  | 无 |  |

实时计算（流计算）

| changel og- produc er | 增量数据产生机制。 | String | 否 | non e | Paimon可以为任意输入数据流产生完整的增量数据 （所有的update after数据都有对应的 _ update before数据），方便下游消费者。增量数据 _ 产生机制的可选值如下： none（默认值）：不额外产生增量数据。下游仍然可以流读Paimon表，但读到的增量数据是不完整的（只有update after数据，没有对应的 _ update before数据）。 _ input：将输入数据流双写至增量数据文件中，作为增量数据。 full-compaction：每次Full Compaction产生完整的增量数据。 lookup：每次commit snapshot前产生完整的增量数据。 |
|---|---|---|---|---|---|
| full- compac tion.del ta- commit s | Full Compaction最大间隔。 | Integer | 否 | 无 | 该参数指定了每commit snapshot多少次之后，一定会进行一次Full Compaction。 |
| lookup. cache- max- memor y-size | Paimon维表的内存缓存大小。 | String | 否 | 256 MB | 该参数值会同时影响维表缓存大小和lookup changelog-producer的缓存大小，两个机制的缓存大小都由该参数配置。 |
| merge- engine | 相同primary key数据的合并机制。 | String | 否 | ded uplic ate | 参数取值如下： deduplicate：仅保留最新一条。 partial-update：用最新数据中非null的列更新相同primary key的现有数据，其它列保持不变。 aggregation：通过指定聚合函数进行预聚合。 |
| partial- update. ignore- delete | 在partial- update合并机制中，是否忽略 delete消息。 | Boolean | 否 | false | 参数取值如下： true：忽略delete消息。 false：碰到delete消息，Flink系统会报错。 说明并非所有场景下忽略delete消息都是正确的，您需要结合自己的实际场景配置该参数。 |
| partitio n.defau lt-name | 分区默认名称。 | String | 否 | D __ EFA ULT PA _ RTIT ION _ _ | 如果分区列的值为null或空字符串，将会采用该默认名称作为分区名。 |

实时计算（流计算）

| partitio n.expir ation- check- interval | 多久检查一次分区过期。 | String | 否 | 1h | 无。 |
|---|---|---|---|---|---|
| partitio n.expir ation- time | 分区的过期时长。 | String | 否 | 无 | 当一个分区的存活时长超过该值时，该分区将会过期，默认永不过期。 |
| partitio n.times tamp- formatt er | 将时间字符串转换为时间戳的格式串。 | String | 否 | 无 | 无。 |
| partitio n.times tamp- pattern | 将分区值转换为时间字符串的格式串。 | String | 否 | 无 | 无。 |
| snapsh ot.num- retaine d.max | 至多保留几个最新Snapshot不过期。 | Integer | 否 | 214 748 364 7 | 只要满足该配置或snapshot.time-retained其中之一，并同时满足snapshot.num-retained.min，就会触发Snapshot过期。 |
| snapsh ot.num- retaine d.min | 至少保留几个最新Snapshot不过期。 | Integer | 否 | 10 | 无。 |
| snapsh ot.time- retaine d | Snapshot产生多久以后会过期。 | String | 否 | 1h | 只要满足该配置或snapshot.num-retained.max其中之一，并同时满足snapshot.num- retained.min，就会触发snapshot过期。 |
| write- mode | Paimon表的写入模式。 | String | 否 | cha nge- log | 参数取值如下： change-log：Paimon表支持根据primary key进行数据的插入、删除和更新。 append-only：Paimon表只接受数据的插入，且不支持primary key。该模式比change-log模式更加高效。 |

**说明**

更多配置项详情请参见Apache Paimon官方文档。

### DML语句

实时计算（流计算）

#### INSERT INTO语句

本文为您介绍如何在一个作业中写入一个Sink或多个Sink。

**写入一个Sink示例**

源表

```
CREATE TABLE datagen_source (
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'datagen'
);
```

结果表

```
create table blackhole_sink(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
);
```

DML

```
INSERT INTO blackhole_sink SELECT UPPER(name), score FROM datagen_source;
```

**写入多个Sink示例**

源表

```
CREATE TABLE datagen_source (
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'datagen'
);
```

结果表A

```
CREATE TABLE blackhole_sinkA(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
);
```

结果表B

```
CREATE TABLE blackhole_sinkB(
  name VARCHAR,
  score BIGINT
) WITH (
  'connector' = 'blackhole'
);
```

DML 本文以写入两个Sink为例进行介绍。 实时计算（流计算） BEGIN STATEMENT SET; --写入多个`Sink`时，必填。

```
INSERT INTO blackhole_sinkA
  SELECT UPPER(name), sum(score)
  FROM datagen_source
  GROUP BY UPPER(name);
INSERT INTO blackhole_sinkB
  SELECT LOWER(name), max(score)
  FROM datagen_source
  GROUP BY LOWER(name);
```

END; --写入多个`Sink`时，必填。 写入多个Sink语句时，需要以**BEGIN STATEMENT SET;**开头，以**END;**结尾。

**说明**

### QUERY语句

### 窗口函数

#### 概述

本文为您介绍Flink SQL支持的窗口函数以及窗口函数支持的时间属性和窗口类型。

### 窗口函数

窗口函数Flink SQL支持基于无限大窗口的聚合（无需在SQL Query中，显式定义任何窗口）以及对一个特定的窗口的聚合。例如，需要统计在过去的1分钟内有多少用户点击了某个的网页，可以通过定义一个窗口来收集最近 1分钟内的数据，并对这个窗口内的数据进行计算。 Flink SQL支持的窗口聚合主要是两种：Window聚合和Over聚合。本文档主要为您介绍Window聚合。 Window聚合支持Event Time和Processing Time两种时间属性定义窗口。每种时间属性类型支持三种窗口类型：滚动窗口（TUMBLE）、滑动窗口（HOP）和会话窗口（SESSION）。

#### 时间属性

Flink SQL支持以下两种时间属性。Flink可以基于这两种时间属性对数据进行窗口聚合。 Event Time：您提供的事件时间（通常是数据的最原始的创建时间），Event Time一定是您提供在Schema 里的数据。 Processing Time：对事件进行处理的本地系统时间。 Flink时间属性详情，请参见时间属性。

**说明**

**级联窗口**

| 数值 | TUMBLE ROWTIME _ |  |
|---|---|---|
|  | max(rowtime) | 作 。 |
| window end - 1 _ |  |  |

示例逻辑为：基于1分钟的滚动窗口聚合结果，进行1小时的滚动窗口聚合，可以满足您的多维度开窗需求。 实时计算（流计算）

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); CREATE TEMPORARY VIEW one_minute_window_output AS SELECT
  TUMBLE_ROWTIME(ts, INTERVAL '1' MINUTE) as rowtime,  --使用TUMBLE_ROWTIME作为二级Window的聚合
```

时间。

```
  username,
  COUNT(click_url) as cnt
FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username; BEGIN statement set; INSERT INTO tumble_output SELECT
  TUMBLE_START(rowtime, INTERVAL '1' HOUR),
  TUMBLE_END(rowtime, INTERVAL '1' HOUR),
  username,
  SUM(cnt)
FROM one_minute_window_output GROUP BY TUMBLE(rowtime, INTERVAL '1' HOUR), username; END;
```

#### 滚动窗口

本文为您介绍如何使用Flink滚动窗口函数。

**定义**

滚动窗口（TUMBLE）将每个元素分配到一个指定大小的窗口中。通常，滚动窗口有一个固定的大小，并且不会出现重叠。例如，如果指定了一个5分钟大小的滚动窗口，无限流的数据会根据时间划分为 `[0:00,` `0:05)` 、 `[0:05, 0:10)` 、 `[0:10, 0:15)` 等窗口。下图展示了一个30秒的滚动窗口。 实时计算（流计算）

**语法**

TUMBLE函数用在GROUP BY子句中，用来定义滚动窗口。

```xml
TUMBLE(<time-attr>, <size-interval>) <size-interval>: INTERVAL 'string' timeUnit
```

`<time-attr>` 参数必须是时间流中的一个合法的时间属性字段，指定为Processing Time或

**说明**

Event Time，请参见概述，了解如何定义时间属性。

**标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 |  | 返回类型 |  | 描述 |
|---|---|---|---|---|
| TUMBLE START(time- _ |  | TIMESTAMP |  | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 窗口，返回 00:10 。 |
|  | TUMBLE START(time- _ |  |  |  |
| attr, size- |  |  |  |  |
| interval) |  |  |  |  |
| TUMBLE END(time- _ |  |  |  | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15] 窗口，返回 00:15 。 |
|  | TUMBLE END(time- _ |  |  |  |
| attr, size- |  |  |  |  |
|  |  | TIMESTAMP |  | 00:15] |
| interval) |  |  |  |  |
| TUMBLE ROWTIME(time _ |  | TIMESTAMP(rowtime- attr) |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个 rowtime attribute，即可以基于该字段进行时间属性的操作，例如，级联窗口只能用在基于Event Time的Window 上，详情请参见级联窗口。 |
|  | TUMBLE ROWTIME(time _ | TIMESTAMP(rowtime- |  |  |
|  |  |  | ime- |  |
| -attr, size- |  |  |  |  |
| interval) |  |  |  |  |

| [00:00, |  |
|---|---|

实时计算（流计算）

| TUMBLE PROCTIME(tim _ |  | TIMESTAMP(rowtime- attr) |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15] 窗口，返回 00:14:59.999 。返回值是一个 Proctime Attribute，即可以基于该字段进行时间属性的操作。例如，级联窗口只能用在基于Processing Time的 Window上，详情请参见级联窗口。 |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | [00:00, |  |
|  | TUMBLE PROCTIME(tim _ | TIMESTAMP(rowtime- |  |  |  |  |
|  |  |  | ime- |  |  |  |
| e-attr, size- |  |  |  |  |  |  |
| interval) |  |  |  |  |  |  |

**使用Event Time统计每个用户每分钟在指定网站的单击数示例**

测试数据

| username（VARCHAR） | click url（VARCHAR） _ | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE) as window_start, TUMBLE_END(ts, INTERVAL '1' MINUTE) as window_end, username, COUNT(click_url) FROM user_clicks GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE),username;
```

测试结果实时计算（流计算）

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username（VARCHA R） | clicks（BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 3 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:01:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | T |  |
|  | 10:02:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:00.0 |  |  |  |  |

**使用Processing Time统计每个用户每分钟在指定网站的单击数示例**

测试数据

| username （VARCHAR） | click url（VARCHAR） _ |
|---|---|
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Jark | http://taobao.com/xxx |
| Timo | http://taobao.com/xxx |

测试语句实时计算（流计算）

```
CREATE TEMPORARY TABLE window_test (
  username   VARCHAR,
  click_url  VARCHAR,
  ts as PROCTIME()
) WITH (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE tumble_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO tumble_output SELECT TUMBLE_START(ts, INTERVAL '1' MINUTE), TUMBLE_END(ts, INTERVAL '1' MINUTE), username, COUNT(click_url) FROM window_test GROUP BY TUMBLE(ts, INTERVAL '1' MINUTE), username;
```

测试结果

|  | window start _ （TIMESTAMP） |  |  |  |  | window end _ （TIMESTAMP） |  |  |  | username （VARCHAR） | clicks（BIGINT） |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 2019-04-11 |  |  |  |  |  |  |  |  | Jark | 5 |
|  |  | 2019-04-11 |  |  |  |  | 2 | 019-04-11 |  | Jark |  |
|  | 14:43:00.00 |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 0 |  |  | 14:44:00.000 |  |  |  |  |  |
|  | 2019-04-11 |  |  |  |  |  |  |  |  | Timo | 1 |
|  |  | 2019-04-11 |  |  |  |  | 20 |  | 19-04-11 | Tim |  |
|  | 14:43:00.00 |  |  |  |  |  |  |  |  |  |  |
|  |  |  | 0 |  |  | 14:44:00.000 |  |  |  |  |  |

#### 滑动窗口

本文为您介绍如何使用Flink滑动窗口函数。

**定义**

滑动窗口（HOP），也被称作Sliding Window。不同于滚动窗口，滑动窗口的窗口可以重叠。 滑动窗口有两个参数：**slide**和**size**。**slide**为每次滑动的步长，**size**为窗口的大小。
**slide < size**，则窗口会重叠，每个元素会被分配到多个窗口。
**slide = size**，则等同于滚动窗口（TUMBLE）。
**slide > size**，则为跳跃窗口，窗口之间不重叠且有间隙。
通常，大部分元素符合多个窗口情景，窗口是重叠的。因此，滑动窗口在计算移动平均数（moving averages） 时很实用。例如，计算过去5分钟数据的平均值，每10秒钟更新一次，可以设置**slide**为10秒，**size**为5分钟。下图为您展示间隔为30秒，窗口大小为1分钟的滑动窗口。 实时计算（流计算）

**函数语法**

HOP函数用在GROUP BY子句中，用来定义滑动窗口。

```xml
HOP(<time-attr>, <slide-interval>,<size-interval>) <slide-interval>: INTERVAL 'string' timeUnit <size-interval>: INTERVAL 'string' timeUnit
```

**说明**

`<time-attr>` 参数必须是流中的一个合法的时间属性字段，指定为Processing Time或Event Time。请参见概述，了解如何定义时间属性。

**标识函数**

使用滑动窗口标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

|  | 窗口标识函数 |  | 返回类型 |  |  | 描述 |
|---|---|---|---|---|---|---|
|  | HOP START（<time- _ |  |  |  |  | 返回窗口的起始时间（包含边界）。例如 [00:10, 00:15) 窗口，返回 00:10 。 |
|  |  | HOP START（<time- _ |  |  |  |  |
|  | attr>, <slide- |  |  |  |  |  |
|  |  |  | TIMESTAMP |  |  |  |
|  |  |  | TIMEST |  |  | 00:15) |
|  | interval>, <size- |  |  |  |  |  |
|  | interval>） |  |  |  |  |  |
|  | HOP END（<time- _ |  |  |  |  | 返回窗口的结束时间（包含边界）。例如 [00:00, 00:15) 窗口，返回 00:15 。 |
|  |  | HOP END（<time- _ |  |  |  |  |
|  | attr>, <slide- |  |  |  |  |  |
|  |  |  | TIMESTAMP |  |  |  |
|  |  |  | TIMEST |  |  | 00:15) |
|  | interval>, <size- |  |  |  |  |  |
|  | interval>） |  |  |  |  |  |

| [00:10, |  |
|---|---|

| [00:00, |  |
|---|---|

实时计算（流计算）

| HOP ROWTIME（<time- _ |  |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, 00:15) 窗口，返回 00:14:59.999 。返回值是一个 rowtime attribute，即可以基于该字段做时间类型的操作，例如级联窗口，只能用在基于event time的window 上。 |  |  |
|---|---|---|---|---|---|---|---|
|  | HOP ROWTIME（<time- _ |  |  |  | 返回窗口的结束时间（ |  |  |
| attr>, <slide- |  | TIMESTAMP（row | time- |  | 00:15) |  |  |
| interval>, <size- |  | attr） |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |
| HOP PROCTIME（<time- _ |  |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00, |  |  |
|  | HOP PROCTIME（<time- _ |  |  |  | 返回窗口的结束时间（ | [00:00, |  |
| attr>, <slide- |  | TIMESTAMP（row | time- |  | 00:15) |  |  |
| interval>, <size- |  | attr） |  |  |  |  |  |
| interval>） |  |  |  |  |  |  |  |

| [00:00, |  |
|---|---|

**示例**

统计每个用户过去1分钟的单击次数，每30秒更新1次，即1分钟的窗口，30秒滑动1次。 测试数据

| username（VARCHAR） | click url（VARCHAR） _ | ts（TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算）

```
CREATE TEMPORARY TABLE user_clicks (
  username VARCHAR,
  click_url VARCHAR,
  eventtime VARCHAR,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE hop_output (
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
);
    hop_output
SELECT
    HOP_START (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    HOP_END (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),
    username,
    COUNT (click_url)
FROM
    user_clicks
GROUP BY
    HOP (ts, INTERVAL '30' SECOND, INTERVAL '1' MINUTE),username;
```

测试结果

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 09:59:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:00:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 3 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:00:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:01:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:00.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:01:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:30.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | T |  |
|  | 10:02:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:00.0 |  |  |  |  |

实时计算（流计算）

|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | T |  |
|  | 10:02:30.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:03:30.0 |  |  |  |  |

HOP窗口无法读取数据进入的时间，第一个窗口的开启时间会前移。**前移时长**=**窗口时长**-**滑动步长**，示例如下表。

| 窗口时长 （秒） | 滑动步长（秒） |  | Event Time |  |  |  | 第一个窗口 StartTime |  |  |  |  | 第一个窗口EndTime |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 120 | 30 |  | 2019-07-31 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 2019-07-31 |  |  |  | 20 | 19-07-31 |  |  |  | 20 | 19-07-31 |  |
|  |  |  | 10:00:00 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | .0 |  | 09:58:30 |  |  | .0 |  | 10:00:30.0 |  |  |  |
| 60 | 10 |  | 2019-07-31 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 2019-07-31 |  |  |  | 20 | 19-07-31 |  |  |  | 20 | 19-07-31 |  |
|  |  |  | 10:00:00 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | .0 |  | 09:59:10 |  |  | .0 |  | 10:00:10.0 |  |  |  |

#### 会话窗口

本文为您介绍如何使用Flink会话窗口函数。

**定义**

会话窗口（SESSION）通过SESSION活动来对元素进行分组。会话窗口与滚动窗口和滑动窗口相比，没有窗口重叠，没有固定窗口大小。相反，当它在一个固定的时间周期内不再收到元素，即会话断开时，该窗口就会关闭。 会话窗口通过一个间隔时间（Gap）来配置，这个间隔定义了非活跃周期的长度。例如，一个表示鼠标单击活动的数据流可能具有长时间的空闲时间，并在两段空闲之间散布着高浓度的单击。如果数据在指定的间隔（Gap） 之后到达，则会开始一个新的窗口。 会话窗口示例如下图，每个Key由于不同的数据分布，形成了不同的Window。 实时计算（流计算）

**函数语法**

SESSION函数用于在GROUP BY子句中定义会话窗口。

```xml
SESSION(<time-attr>, <gap-interval>) <gap-interval>: INTERVAL 'string' timeUnit
```

`<time-attr>` 参数必须是数据流中的一个合法的时间属性字段，指定为Processing Time或

**说明**

Event Time，详情请参见概述，了解如何定义时间属性。

**标识函数**

使用标识函数选出窗口的起始时间或者结束时间，窗口的时间属性用于下级Window的聚合。

| 窗口标识函数 |  | 返回类型 |  | 描述 |  |
|---|---|---|---|---|---|
| SESSION START（<time _ |  |  |  | 返回窗口的起始时间（包含边界）。例如 [00:10,00:15) 的窗口，返回 00:10 ，即为此会话窗口内第一条记录的时间。 |  |
|  | SESSION START（<time _ |  |  |  |  |
| -attr>, <gap- |  |  |  |  |  |
|  |  | Ti |  |  |  |
| interval>） |  |  |  |  |  |
| SESSION END（<time- |  | Timestamp |  | 返回窗口的结束时间（包含边界）。例如 [00:00,00:15) 的窗口，返回 00:15 ，即为此会话窗口内最后一条记录的时间+ <gap-interval> 。 |  |
|  | SESSION END（<time- |  |  |  |  |
| _ attr>, <gap- | _ |  |  |  |  |
|  |  | T |  |  |  |
| interval>） |  |  |  |  |  |
| SESSION ROWTIME（<ti _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个rowtime attribute，也就是可以基于该字段进行时间类型的操作，例如级联窗口。该参数只能用于基于Event Time的Window。 |  |
|  | SESSION ROWTIME（<ti _ |  |  | 如 | [00:00,00:15) |
| me-attr>, <gap- |  | Tim attr | （rowtime- |  |  |
| interval>） |  |  |  |  |  |
| SESSION PROCTIME（<t _ |  |  |  | 返回窗口的结束时间（不包含边界）。例如 [00:00,00:15) 的窗口，返回 00:14:59.999 。返回值是一个Proctime Attribute，也就是可以基于该字段进行时间类型的操作，例如级联窗口。该参数只能用于基于Processing Time的Window。 |  |
|  | SESSION PROCTIME（<t _ | Timestamp（rowtime- |  | 如 | [00:00,00:15) |
| ime-attr>, <gap- |  | Time |  |  |  |
|  |  | attr） |  |  |  |
| interval>） |  |  |  |  |  |

**示例**

统计每个用户在每个活跃会话期间的单击次数，会话超时时长为30秒。 测试数据

| username （VARCHAR） | click url （VARCHAR） _ | ts （TIMESTAMP） |
|---|---|---|
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:00.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:10.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:00:49.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:05.0 |
| Jark | http://taobao.com/xxx | 2017-10-10 10:01:58.0 |
| Timo | http://taobao.com/xxx | 2017-10-10 10:02:10.0 |

测试语句实时计算（流计算）

```
CREATE TEMPORARY TABLE user_clicks(
  username varchar,
  click_url varchar,
  eventtime varchar,
  ts AS TO_TIMESTAMP(eventtime),
  WATERMARK FOR ts AS ts - INTERVAL '2' SECOND  --为Rowtime定义Watermark。
) with (
  'connector'='sls',
  ...
); CREATE TEMPORARY TABLE session_output(
  window_start TIMESTAMP,
  window_end TIMESTAMP,
  username VARCHAR,
  clicks BIGINT
) with (
```

`'connector'='datahub' --`目前`SLS`只支持输出`VARCHAR`类型的`DDL`，所以使用`DataHub`存储。

```
  ...
); INSERT INTO session_output SELECT SESSION_START(ts, INTERVAL '30' SECOND), SESSION_END(ts, INTERVAL '30' SECOND), username, COUNT(click_url) FROM user_clicks GROUP BY SESSION(ts, INTERVAL '30' SECOND), username;
```

测试结果

|  | window start _ （TIMESTAMP） |  |  |  | window end _ （TIMESTAMP） |  |  | username （VARCHAR） | clicks （BIGINT） |
|---|---|---|---|---|---|---|---|---|---|
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:00:00.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:00:40.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 2 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:00:49.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:01:35.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Jark | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | J |  |
|  | 10:01:58.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:28.0 |  |  |  |  |
|  | 2017-10-10 |  |  |  |  |  |  | Timo | 1 |
|  |  | 2017-10-10 |  |  |  |  | 2017-10-10 | T |  |
|  | 10:02:10.0 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 10:02:40.0 |  |  |  |  |

#### OVER窗口

OVER窗口（OVER Window）是传统数据库的标准开窗，不同于Group By Window，OVER窗口中每1个元素都对应1个窗口。OVER窗口可以按照实际元素的行或实际的元素值（时间戳值）确定窗口，因此流数据元素可能分布在多个窗口中。 在应用OVER窗口的流式数据中，每1个元素都对应1个OVER窗口。每1个元素都触发1次数据计算，每个触发计算的元素所确定的行，都是该元素所在窗口的最后1行。在实时计算的底层实现中，OVER窗口的数据进行全局统一管理（数据只存储1份），逻辑上为每1个元素维护1个OVER窗口，为每1个元素进行窗口计算，完成计算后会清除过期的数据。 实时计算（流计算）

**语法**

```
SELECT
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

窗口数据 ROWS OVER Window的每个元素都确定一个窗口。ROWS OVER Window分为Unbounded（无界流）和 Bounded（有界流）两种情况。 Unbounded ROWS OVER Window数据示例如下图所示。 实时计算（流计算） 虽然上图所示窗口user1的w7、w8及user2的窗口w3、w4都是同一时刻到达，但它们仍然

**说明**

在不同的窗口，这一点与RANGE OVER Window不同。 Bounded ROWS OVER Window数据以3个元素（往前2个元素）的窗口为例，如下图所示。 虽然上图所示窗口user1的w5、w6及user2的窗口w1、w2都是同一时刻到达，但它们仍然

**说明**

在不同的窗口，这一点与RANGE OVER Window不同。 窗口语法实时计算（流计算）

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     ROWS
     BETWEEN (UNBOUNDED | rowCount) PRECEDING AND CURRENT ROW) AS colName, ...
FROM Tab1;
```

value_expression：分区值表达式。 timeCol：元素排序的时间字段。 rowCount：定义根据当前行开始向前追溯几行元素。 案例以Bounded ROWS OVER Window场景为例。假设，一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。要求输出在当前商品上架之前同类的3个商品中的最高价格。 测试数据

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

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:01:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:02:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:05:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:06:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:07:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:08:00 |  |  |

实时计算（流计算） 测试代码

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  --为Rowtime定义Watermark
```

。

```
) WITH (
  'connector' = 'sls',
   ...
); SELECT
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

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:01:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:02:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:03:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:03:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:05:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:06:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| ronic | 10:07:00 |  |

|  |  | 2017-11-11 |
|---|---|---|
| es | 10:08:00 |  |

**RANGE OVER Window语义**

窗口数据实时计算（流计算） RANGE OVER Window所有具有共同元素值（元素时间戳）的元素行确定一个窗口，RANGE OVER Window分为Unbounded和Bounded的两种情况。 Unbounded RANGE OVER Window数据示例如下图所示。 上图所示窗口user1的w7、user2的窗口w3，两个元素同一时刻到达，属于相同的

**说明**

window，这一点与ROWS OVER Window不同。 Bounded RANGE OVER Window数据，以3秒中数据 `(INTERVAL '2' SECOND)` 的窗口为例，如下图所示。 上图所示窗口user1的w6、user2的窗口w3，元素都是同一时刻到达，属于相同的

**说明**

window，这一点与ROWS OVER Window不同。 实时计算（流计算） 窗口语法

```
SELECT
    agg1(col1) OVER(
     [PARTITION BY (value_expression1,..., value_expressionN)]
     ORDER BY timeCol
     RANGE
     BETWEEN (UNBOUNDED | timeInterval) PRECEDING AND CURRENT ROW) AS colName,
... FROM Tab1;
```

value_expression：进行分区的字表达式。 timeCol：元素排序的时间字段。 timeInterval：定义根据当前行开始向前追溯指定时间的元素行。 案例 Bounded RANGE OVER Window场景示例：假设一张商品上架表，包含有商品ID、商品类型、商品上架时间、商品价格数据。需要求比当前商品上架时间早2分钟的同类商品中的最高价格。 测试数据

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

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:01:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:02:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:03:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:05:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:06:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:07:00 |  |  |

|  |  | 2017-11-11 |  |
|---|---|---|---|
|  | 10:08:00 |  |  |

实时计算（流计算） 测试代码

```
CREATE TEMPORARY TABLE tmall_item(
  itemID VARCHAR,
  itemType VARCHAR,
  eventtime varchar,
  onSellTime AS TO_TIMESTAMP(eventtime),
  price DOUBLE,
  WATERMARK FOR onSellTime AS onSellTime - INTERVAL '0' SECOND  --为Rowtime定义Watermark
```

。

```
) WITH (
  'connector' = 'sls',
   ...
); SELECT
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

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| nic | 10:01:00 |  |  |

|  |  | 2017-11-11 | 50 |
|---|---|---|---|
| nic | 10:02:00 |  |  |

|  |  | 2017-11-11 | 30 |
|---|---|---|---|
| nic | 10:03:00 |  |  |

|  |  | 2017-11-11 | 60 |
|---|---|---|---|
| nic | 10:03:00 |  |  |

|  |  | 2017-11-11 | 40 |
|---|---|---|---|
| nic | 10:05:00 |  |  |

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| nic | 10:06:00 |  |  |

|  |  | 2017-11-11 | 70 |
|---|---|---|---|
| nic | 10:07:00 |  |  |

|  |  | 2017-11-11 | 20 |
|---|---|---|---|
| s | 10:08:00 |  |  |

### 内置函数

实时计算（流计算）

#### 概述

本文为您介绍Flink提供的用于数据转换的内置函数。 Flink V1.11：请参见Flink V1.11内置函数。 Flink V1.12：请参见Flink V1.12内置函数。

**说明**

Flink全托管VVR 3.0.0版本在Flink V1.12的基础上增加了部分内置函数，详情请参见标量函数。 如果内置函数中不存在您所需的函数，您可以通过自定义函数实现，自定义函数详情请参见概述。

#### 标量函数

##### BITAND

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

输入和输出类型均为整型，且类型一致。

**说明**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |
| number2 | INT |

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句

```
FROM T1;
```

测试结果

**intt(INT)**

实时计算（流计算）

##### BITNOT

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

输入和输出类型均为整型，且类型一致。

**说明**

**入参**

| 参数 | 数据类型 |
|---|---|
| number | INT |

**示例**

测试数据

**a(INT)**

测试语句

```
FROM T1;
```

测试结果

**var1(INT)**

-8

##### BITOR

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |

实时计算（流计算）

| number2 | INT |
|---|---|

输入和输出类型均为整型，且类型一致。

**说明**

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句

```
FROM T1;
```

测试结果

**var1(INT)**

-3

##### BITXOR

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| number1 | INT |
| number2 | INT |

输入和输出类型均为整型，且类型一致。

**说明**

**示例**

测试数据

| a(INT) | b(INT) |
|---|---|
| 2 | 3 |

测试语句实时计算（流计算）

```
FROM T1;
```

测试结果

**var1(INT)**

##### CONV

本文为您介绍如何使用CONV函数，对数字或字符类型的数值进行进制转换。

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。
**CONV()**精度为64位。

**语法**

```
VARCHAR CONV(BIGINT number, INT FROM_BASE, INT TO_BASE)
```

`or`

```
VARCHAR CONV(VARCHAR number, INT FROM_BASE, INT TO_BASE)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| number | BIGINT、VARCHAR | 说明当number为NULL 或非法字符时，结果返回为 NULL。 |
| FROM BASE _ | INT | 取值范围[2, 36]。 |
| TO BASE _ | INT | 可以为正数，取值范围[2, 36]；也可以为负数，取值范围[-36, -2]。 |

**示例**

测试数据

| id(INT) | x(BIGINT) | y (VARCHAR) |
|---|---|---|
| 1 | 12L | '12' |
| 2 | 10L | '10' |
| 3 | 0L | 'test' |
| 4 | NULL | NULL |

测试语句

```
SELECT id, conv(x, 10, 16) as var1, conv(y, 10, 2) as var2 FROM T1;
```

实时计算（流计算） 测试结果

| id(INT) | var1(VARCHAR) | var2(VARCHAR) |
|---|---|---|
| 1 | C | 1100 |
| 2 | A | 1010 |
| 3 | 0 | NULL |
| 4 | NULL | NULL |

##### DATEDIFF

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
INT DATEDIFF(VARCHAR enddate, VARCHAR startdate) INT DATEDIFF(TIMESTAMP enddate, VARCHAR startdate) INT DATEDIFF(VARCHAR enddate, TIMESTAMP startdate) INT DATEDIFF(TIMESTAMP enddate, TIMESTAMP startdate)
```

**入参**

| 参数 | 数据类型 |
|---|---|
| startdate | TIMESTAMP、VARCHAR |
| enddate | TIMESTAMP、VARCHAR |

**说明**

VARCHAR日期格式：**yyyy-MM-dd**或**yyyy-MM-dd HH:mm:ss**。 如果入参中任何一个为NULL或解析错误，则返回为NULL。

**示例**

测试数据

| datetime1(VARCHAR) | datetime2(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 2017-10-15 00:00:00 | 2017-09-15 00:00:00 | NULL |

测试语句实时计算（流计算）

```
SELECT DATEDIFF(datetime1, datetime2) as int1,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',datetime2) as int2,
        DATEDIFF(datetime2,TIMESTAMP '2017-10-15 23:00:00') as int3,
        DATEDIFF(datetime2,nullstr) as int4,
        DATEDIFF(nullstr,TIMESTAMP '2017-10-15 23:00:00') as int5,
        DATEDIFF(nullstr,datetime2) as int6,
        DATEDIFF(TIMESTAMP '2017-10-15 23:00:00',TIMESTAMP '2017-9-15 00:00:00')as int7
FROM T1;
```

测试结果

| int1(INT) | int2(INT) | int3(INT) | int4(INT) | int5(INT) | int6(INT) | int7(INT) |
|---|---|---|---|---|---|---|
| 30 | 31 | -31 | NULL | NULL | NULL | 31 |

##### DATE_ADD

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| startdate | TIMESTAMP、VARCHAR 说明 VARCHAR类型日期格式为yyyy-MM-dd或yyyy-MM-dd HH:mm:ss。 |
| time | TIMESTAMP |
| days | INT |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| datetime1(VATCHAR) | nullstr(VATCHAR) |
|---|---|
| 2017-09-15 00:00:00 | null |

测试语句实时计算（流计算）

```
SELECT DATE_ADD(datetime1, 30) as var1,
 DATE_ADD(TIMESTAMP '2017-09-15 23:00:00',30) as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-10-15 | 2017-10-15 | null |

##### DATE_FORMAT

本文为您介绍如何使用DATE_FORMAT函数，将字符串类型的日期从原格式转换至目标格式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR DATE_FORMAT(TIMESTAMP time, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR to_format) VARCHAR DATE_FORMAT(VARCHAR date, VARCHAR from_format, VARCHAR to_format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| time | TIMESTAMP | 源字符串。 |
| date | VARCHAR | 源字符串，默认格式为：yyyy-MM-dd HH:mm:ss。 |
| from format _ | VARCHAR | 可选，原格式，默认格式为yyyy-MM-dd hh:mm:ss。 |
| to format _ | VARCHAR | 目标格式。 |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| date1(VARCHAR) | datetime1(VARCHAR) | nullstr(VARCHAR) |
|---|---|---|
| 0915-2017 | 2017-09-15 00:00:00 | NULL |

测试语句

```
SELECT DATE_FORMAT(datetime1, 'yyMMdd') as var1,
 DATE_FORMAT(nullstr, 'yyMMdd') as var2,
 DATE_FORMAT(datetime1, nullstr) as var3,
 DATE_FORMAT(date1, 'MMdd-yyyy', nullstr) as var4,
 DATE_FORMAT(date1, 'MMdd-yyyy', 'yyyyMMdd') as var5,
 DATE_FORMAT(TIMESTAMP '2017-09-15 23:00:00', 'yyMMdd') as var6
FROM T1;
```

实时计算（流计算） 测试结果

| var1(VARCH AR) | var2(VARCH AR) | var3(VARCH AR) | var4(VARCH AR) | var5(VARCH AR) | var6(VARCH AR) |
|---|---|---|---|---|---|
| 170915 | null | null | null | 20170915 | 170915 |

##### DATE_FORMAT_TZ

本文为您介绍如何使用DATE_FORMAT_TZ函数，将时间戳类型的数据根据指定的时区，转成指定格式的字符串。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR format, VARCHAR timezone) VARCHAR DATE_FORMAT_TZ(TIMESTAMP timestamp, VARCHAR timezone)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timestamp | TIMESTAMP | 时间类型。 |
| format | VARCHAR | 输出日期格式，例如yyyy-MM-dd HH:mm:ss。 |
| timezone | VARCHAR | 指定时区，例如Asia/Shanghai。 |

**示例**

测试数据

| timestamp1(TIMESTAMP) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 0 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

测试语句

```
SELECT
   DATE_FORMAT_TZ(timestamp1, format1, timezone1) as var1,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) |
|---|---|
| 1970-01-01 08:00:00 | 1970-01-01 08:00:00 |

##### DATE_SUB

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

实时计算（流计算）

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| startdate | VARCHAR 说明 VARCHAR类型日期格式为yyyy-MM-dd或yyyy-MM-dd HH:mm:ss。 |
| time | TIMESTAMP |
| days | INT |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| date1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| 2017-10-15 | NULL |

测试语句

```
SELECT DATE_SUB(date1, 30) as var1,
 DATE_SUB(TIMESTAMP '2017-10-15 23:00:00',30) as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 | 2017-09-15 | NULL |

##### FROM_UNIXTIME

本文为您介绍如何使用FROM_UNIXTIME函数，返回VARCHAR类型的日期值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR FROM_UNIXTIME(BIGINT unixtime, VARCHAR format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|

实时计算（流计算）

| unixtime | BIGINT | 以秒为单位的时间戳。 |
|---|---|---|
| format | VARCHAR | 可选，日志格式，默认格式为yyyy-MM-dd HH:mm:ss。 |

如果入参中任何一个为NULL或解析错误，则返回为NULL。

**说明**

**示例**

测试数据

| unixtime1(BIGINT) | nullstr(VARCHAR) |
|---|---|
| 1505404800 | NULL |

测试语句

```
SELECT FROM_UNIXTIME(unixtime1) as var1,
 FROM_UNIXTIME(unixtime1,'MMdd-yyyy') as var2,
FROM T1;
```

测试结果

| var1(VARCHAR) | var2(VARCHAR) | var3(VARCHAR) |
|---|---|---|
| 2017-09-15 00:00:00 | 0915-2017 | NULL |

##### ISNAN

本文为您介绍如何使用ISNAN函数，判断指定的浮点数是否为NaN（Not a number），类似于Java中本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| d | DOUBLE |
| f | FLOAT |

**示例**

测试数据表 1. T1

| d | f |
|---|---|
| 0.1 | 0.1 |

实时计算（流计算）

| 0 | 0 |
|---|---|

测试语句

```
SELECT ISNAN(CAST(d AS DOUBLE)) as d1, FROM T1;
```

测试结果

| d1(BOOLEAN) | d2(BOOLEAN) |
|---|---|
| false | false |
| false | false |

##### JSON_VALUE

本文为您介绍如何使用JSON_VALUE函数，从JSON字符串中提取指定路径的表达式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR JSON_VALUE(VARCHAR content, VARCHAR path)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| content | VARCHAR | 需要解析的JSON对象。 |
| path | VARCHAR | 指定路径表达式。自定义路径需要使用单引号（'），示例如下。 JSON VALUE(json,'$.passenger name') AS _ _ ABC 目前路径支持的符号及功能如下： $：根对象。 []：数组下标。 *：数组通配符。 .：取子元素。 |

如果入参中有不合法的JSON和NULL，则返回为NULL。

**说明**

**示例**

测试数据表 1. T1

| id(INT) | json(VARCHAR) | path1(VARCHAR) |
|---|---|---|
| 1 | [10, 20, [30, 40]] | $[2][*] |

实时计算（流计算）

| 2 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg","hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[*] |
|---|---|---|
| 3 | {"aaa":"bbb","ccc": {"ddd":"eee","fff":"ggg",hhh": ["h0","h1","h2"]},"iii":"jjj"} | $.ccc.hhh[1] |
| 4 | [10, 20, [30, 40]] | NULL |
| 5 | NULL | $[2][*] |
| 6 | "{xx]" | "$[2][*]" |

测试语句

```
SELECT
```

`id`，

```
FROM
    T1;
```

测试结果

| id (INT) | value (VARCHAR) |
|---|---|
| 1 | [30,40] |
| 2 | ["h0","h1","h2"] |
| 3 | H1 |
| 4 | NULL |
| 5 | NULL |
| 6 | NULL |

##### KEYVALUE

本文为您介绍如何使用KEYVALUE函数，将目标字符串按照split1分隔符拆分成Key-Value（KV）对，然后按照本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 待拆分的目标字符串。 |
| split1 | VARCHAR | 按照split1分隔符，将目标字符串拆分成Key-Value（KV） 对。 |

实时计算（流计算）

| split2 | VARCHAR | 按照split2分隔符将Key-Value对分开。 |
|---|---|---|
| key name _ | VARCHAR | Key的名称。 |

**说明**

如果split1或split2为NULL时，则返回NULL。 如果str或者key_name为NULL时，则返回NULL。 如果没有匹配的Key时，则返回NULL。

**示例**

测试数据表 1. T1

| str(VARCHAR) | split1(VARCHAR) | split2(VARCHAR) | key1(VARCHAR) |
|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k2 |
| NULL | ; | \| | : |
| k1:v1\|k2:v2 | NULL | = | : |
| k1:v1\|k2:v2 | \| | = | NULL |
| k1:v1\|k2:v2 | \| | = | : |

测试语句

```
SELECT KEYVALUE(str, split1, split2, key1) as `result` FROM T1;
```

测试结果

**result(VARCHAR)**

v2 NULL NULL NULL NULL

##### MURMUR_HASH

本文为您介绍如何使用MURMUR_HASH函数，按Murmur 32哈希算法计算指定参数的32位哈希值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

实时计算（流计算）

**入参**

| 参数 | 数据类型 |
|---|---|
| value | VARCHAR或数值类型。 |

**示例1**

测试数据表 1. T1 This is a test String. NULL test 测试语句

```
FROM T1;
```

测试结果

**intt(VARCHAR)**

740959099 NULL 271330425

**示例2**

测试数据表 2. T2

**str**

4.5 NULL 测试语句

```
FROM T2;
```

测试结果

**intt(VARCHAR)**

-2130121231 NULL 1863595885 实时计算（流计算）

##### MURMUR_HASH_64

本文为您介绍如何使用MURMUR_HASH_64函数，按Murmur 128哈希算法计算指定参数的64位哈希值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| value | VARCHAR或数值类型。 |

**示例1**

测试数据表 1. T1 This is a test String. NULL test 测试语句

```
FROM T1;
```

测试结果

**big(VARCHAR)**

2706826604463634835 NULL 5010266691562018262

**示例2**

测试数据表 2. T2 4.5 NULL 测试语句实时计算（流计算）

```
FROM T2;
```

测试结果

**big(VARCHAR)**

8033179276572534397 NULL -6697622088025985219

##### PARSE_URL

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR PARSE_URL(VARCHAR urlStr, VARCHAR partToExtract [, VARCHAR key])
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| urlStr | VARCHAR | 目标URL。 说明如果urlStr参数值为NULL时，则返回值为NULL。 |
| partToExtract | VARCHAR | 指定链接中解析的部分。取值如下： HOST PATH QUERY REF PROTOCOL FILE AUTHORITY USERINFO |
| key | VARCHAR | 可选，指定截取部分，具体的键。 |

**示例**

测试数据

| url1(VARCHAR) | nullstr(VARCHAR) |
|---|---|
| http://facebook.com/path/p1.php?query=1 | NULL |

测试语句实时计算（流计算）

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
FROM T1;
```

测试结果

| var1( VARC HAR) | var2( VARC HAR) | var3( VARC HAR) | var4( VARC HAR) | var5( VARC HAR) | var6( VARC HAR) | var7( VARC HAR) | var8( VARC HAR) | var9( VARC HAR) | var1 0(VA RCH AR) | var1 1(VA RCH AR) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | query =1 | faceb ook.c om | /path/ p1.ph p | NULL | http | /path/ p1.ph p? query =1 | faceb ook.c om | NULL | NULL | NULL |

##### REGEXP

本文为您介绍如何使用REGEXP函数，对指定的字符串执行一个正则表达式搜索，并返回一个Boolean值表示是否找到指定的匹配模式。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 指定的字符串。 |
| pattern | VARCHAR | 指定的匹配模式。 |

如果str或pattern为空或为NULL，则返回false。

**说明**

**示例**

测试数据表 1. T1

| str1(VARCHAR) | pattern1(VARCHAR) |
|---|---|
| k1=v1;k2=v2 | k2* |
| k1:v1\|k2:v2 | k3 |

实时计算（流计算）

| NULL | k3 |
|---|---|
| k1:v1\|k2:v2 | NULL |
| k1:v1\|k2:v2 | ( |

测试语句

```
FROM T1;
```

测试结果

**result(BOOLEAN)**

true false false false false

##### REGEXP_REPLACE

本文为您介绍如何使用REGEXP_REPLACE函数，用目标字符串替换指定字符串，并返回新的字符串。

**重要**

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**语法**

```
VARCHAR REGEXP_REPLACE(VARCHAR str, VARCHAR pattern, VARCHAR replacement)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 指定的字符串。 |
| pattern | VARCHAR | 被替换的字符串。 |
| replacement | VARCHAR | 用于替换的目标字符串。 |

**重要**

如果入参为NULL或者正则不合法时，则返回NULL。 系统会将pattern和replacement的字符串解析成正则表达式，正则表达式使用Java Pattern进行处理，因此pattern和replacement的字符串需遵从Java Regex语法。

**示例**

测试数据表 1. T1 实时计算（流计算）

| str1(VARCHAR) | pattern1(VARCHAR) | replace1(VARCHAR) |
|---|---|---|
| 2014-03-13 | - | ‘’ |
| ‘‘ | - | ‘‘ |
| 2014-03-13 | '' | s |
| 2014-03-13 | ( | s |
| 100-200 | (\d+) | num |

测试语句

```
SELECT REGEXP_REPLACE(str1, pattern1, replace1) as result FROM T1;
```

测试结果

**result(VARCHAR)**

20140313 空 s2s0s1s4s-s0s3s-s1s3s null num-num

##### SPLIT_INDEX

本文为您介绍如何使用SPLIT_INDEX函数，将目标字符串按照指定分隔符分割成若干段，返回指定位置的字段信息。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
VARCHAR SPLIT_INDEX(VARCHAR str, VARCHAR sep, INT index)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 目标字符串。 |
| sep | VARCHAR | 分隔符。 |
| index | INT | 字段位置，index从0开始。 说明如果获取不到字段，则返回NULL。 |

实时计算（流计算） 如果入参任何一个为NULL，则返回NULL。

**说明**

**示例**

测试数据表 1. T1

| str(VARCHAR) | sep(VARCHAR) | index(INT) |
|---|---|---|
| Jack,John,Mary | , | 2 |
| Jack,John,Mary | , | 3 |
| Jack,John,Mary | NULL | 0 |
| NULL | , | 0 |

测试语句

```
FROM T1;
```

测试结果

**var1(VARCHAR)**

Mary NULL NULL NULL

##### TO_DATE

本文为您介绍如何使用TO_DATE函数，将INT类型或者VARCHAR类型的日期转换成DATE类型。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| time | INT | 表示从1970-1-1到所表示时间之间天数。 |
| date | VARCHAR | 默认格式为yyyy-MM-dd。 |
| format | VARCHAR | 日期格式。 |

**示例**

实时计算（流计算） 测试数据表 1. T1

| date1(INT) | date2(VARCHAR) | date3(VARCHAR) |
|---|---|---|
| 100 | 2017-09-15 | 20170915 |

测试语句

```
SELECT TO_DATE(date1) as var1,
 TO_DATE(date2) as var2,
FROM T1;
```

测试结果

| var1(DATE) | var2(DATE) | var3(DATE) |
|---|---|---|
| 1970-04-11 | 2017-09-15 | 2017-09-15 |

##### TO_TIMESTAMP_TZ

本文为您介绍如何使用TO_TIMESTAMP_TZ函数，将VARCHAR类型的日期根据指定时区转换成TIMESTAMP类型。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR timezone) TIMESTAMP TO_TIMESTAMP_TZ(VARCHAR date, VARCHAR format，VARCHAR timezone)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timezone | VARCHAR | 字符串表示的时区，例如Asia/Shanghai。 |
| date | VARCHAR | 默认格式为yyyy-MM-dd HH:mm:ss。 |
| format | VARCHAR | 日期格式。 |

**示例**

测试数据表 1. T1

| timestamp1(VARCHAR) | format1(VARCHAR) | timezone1(VARCHAR) |
|---|---|---|
| 1970-01-01 00:00:00 | yyyy-MM-dd HH:mm:ss | Asia/Shanghai |

测试语句

```
SELECT
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, timezone1)) as var1,
     UNIX_TIMESTAMP(TO_TIMESTAMP_TZ(timestamp1, format1, timezone1)) as var2
FROM T1;
```

测试结果实时计算（流计算）

| var1(BIGINT) | var2(BIGINT) |
|---|---|
| -28800 | -28800 |

##### UNIX_TIMESTAMP

本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
BIGINT UNIX_TIMESTAMP(VARCHAR date, VARCHAR format)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| timestamp | TIMESTAMP | 无。 |
| date | VARCHAR | 默认日期格式为 yyyy-MM-dd HH:mm:ss 。 |
| format | VARCHAR | 默认日期格式为 yyyy-MM-dd hh:mm:ss 。 |

**示例**

测试数据表 1. T1

| date1(VARCHAR) | date2(VARCHAR) |
|---|---|
| 2021-03-25 00:00:00 | 1970-01-01 00:00:00 |

测试语句

```
SELECT UNIX_TIMESTAMP(to_timestamp_tz(date1)) as big1, FROM T1;
```

测试结果

| big1（BIGINT） | big2（BIGINT） |
|---|---|
| 1616601600 | -28800 |

#### 表值函数

##### GENERATE_SERIES

本文为您介绍如何使用GENERATE_SERIES函数，按from、from+1、from+2 … to-1的规则，生成一系列填充数据。 实时计算（流计算） 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 |
|---|---|
| from | INT类型，指定下界，包含下界值。 |
| to | INT类型，指定上界，不包含上界值。 |

**示例**

测试数据表 1. T1

| s(INT) | e(INT) |
|---|---|
| 1 | 3 |
| -2 | 1 |

测试语句

```
SELECT s, e, v as v;
```

测试结果

| s(INT) | e(INT) | v(INT) |
|---|---|---|
| 1 | 3 | 1 |
| 1 | 3 | 2 |
| -2 | 1 | -2 |
| -2 | 1 | -1 |
| -2 | 1 | 0 |

##### JSON_TUPLE

本文为您介绍如何使用JSON_TUPLE函数，从JSON字符串中取出各路径字符串所表示的值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

实时计算（流计算）

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | JSON字符串。 |
| path1～pathN | VARCHAR | 表示路径的字符串，前面不需要 $ 。 |

**示例**

测试数据表 1. T1

| d(VARCHAR) | s(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | qwe3 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | qwe2 |

测试语句

```
SELECT d, v AS T(v);
```

测试结果

| d(VARCHAR) | v(VARCHAR) |
|---|---|
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd |
| {"qwe":"asd","qwe2":"asd2","qwe3":"asd3"} | asd3 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd4 |
| {"qwe":"asd4","qwe2":"asd5","qwe3":"asd3"} | asd5 |

##### MULTI_KEYVALUE

本文为您介绍如何使用MULTI_KEYVALUE函数，将目标字符串中拆分为Key-Value（KV）对，匹配split1和 split2的KV对，并返回key_name1和key_name2对应的Value值。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

```
MULTI_KEYVALUE(VARCHAR str, VARCHAR split1, VARCHAR split2, VARCHAR key_name1, VARCHAR key_n ame2, ...)
```

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| str | VARCHAR | 目标字符串。 |
| split1 | VARCHAR | KV对的分隔符。 当split1为NULL时，表示按照空格作为KV对的分割符。当 split1的长度>1时，split1仅表示分隔符的集合，每个字符都表示一个有效的分隔符。 |

实时计算（流计算）

| split2 | VARCHAR | KV的分隔符。 当split2为NULL时，表示按照空格作为KV的分割符。当 split2的长度>1时，split2仅表示分隔符的集合，每个字符都表示一个有效的分隔符。 |
|---|---|---|
| key name1, _ key name2, ... _ | VARCHAR | 需要获取Value的Key值列表。 |

**示例**

测试数据表 1. T1

| str(VARCHAR) | split1(VARCHAR ) | split2(VARCHAR ) | key1(VARCHAR) | key2(VARCHAR) |
|---|---|---|---|---|
| k1=v1;k2=v2 | ; | = | k1 | k2 |
| NULL | ; | = | k1 | k2 |
| k1:v1;k2:v2 | ; | : | k1 | k3 |
| k1:v1;k2:v2 | ; | = | k1 | k2 |
| k1:v1;k2:v2 | , | : | k1 | k2 |
| k1:v1;k2=v2 | ; | : | k1 | k2 |
| k1:v1abck2:v2 | abc | : | k1 | k2 |
| k1:v1;k2=v2 | ; | := | k1 | k2 |
| k1:v1 k2:v2 | NULL | : | k1 | k2 |
| k1 v1;k2 v2 | ; | NULL | k1 | k2 |

测试语句

```
SELECT c1, c2 FROM T1, lateral table(MULTI_KEYVALUE(str, split1, split2, key1, key2)) as T(c1, c2);
```

测试结果

| c1(VARCHAR) | c2(VARCHAR) |
|---|---|
| v1 | v2 |
| NULL | NULL |
| v1 | NULL |
| NULL | NULL |
| NULL | NULL |
| v1 | NULL |
| v1 | v2 |
| v1 | v2 |

实时计算（流计算）

| v1 | v2 |
|---|---|
| v1 | v2 |

##### STRING_SPLIT

本文为您介绍如何使用STRING_SPLIT函数，根据指定的分隔符将目标字符串拆分为子字符串，并返回子字符串列表。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| string | VARCHAR | 目标字符串。 |
| separator | VARCHAR | 指定的分隔符。 说明 separator暂不支持多字符串形式，只支持单字符串形式。 |

**说明**

如果string为NULL，则返回一个空行。 如果string包含两个或多个连续出现的分隔符时，则返回长度为零的空子字符串。 如果string未包含指定分隔符，则返回目标字符串。

**示例**

测试数据表 1. T1

| d(varchar) | s(varchar) |
|---|---|
| abc-bcd | - |
| hhh | - |

测试语句

```
SELECT d,v FROM T1, lateral table(string_split(d, s)) as T(v);
```

测试结果

| d(varchar) | v(varchar) |
|---|---|
| abc-bcd | abc |
| abc-bcd | bcd |

实时计算（流计算）

| hhh | hhh |
|---|---|

#### 聚合函数

##### APPROX_COUNT_DISTINCT

本文为您可以介绍如何使用APPROX_COUNT_DISTINCT函数，提升作业性能。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**背景信息**

Count Distinct优化时，Aggregate节点的State需要保存所有Distinct Key信息。当Distinct Key数目过大时，State的读写开销太大，因此Count Distinct优化存在性能瓶颈。但在很多场景，完全精确的统计并不那么必要。如果您希望牺牲部分精确度来换取性能上的提升，您可以使用新增的内置函数**APPROX_COUNT_DISTINCT**提升作业性能。**APPROX_COUNT_DISTINCT**支持MiniBatch或Local- Global等Aggregate上的优化，但是需要注意以下几点： 输入不含有撤回消息。 Distinct Key数目需要足够大，例如UV。如果Distinct Key数目不大，**APPROX_COUNT_DISTINCT**性能相对精确计算提升不大。

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| col | 任意类型 | 字段名称 |
| accuracy | FLOAT | 可选，准确率，取值范围为(0.0, 1.0)，默认值为0.99，取值越高，准确率越高，state开销越大，性能越低。 |

**示例**

测试数据表 1. T1

| a (VARCHAR) | c (BIGINT) |
|---|---|
| Hi | 1 |
| Hi | 2 |
| Hi | 3 |
| Hi | 4 |
| Hi | 5 |
| Hi | 6 |

测试代码实时计算（流计算）

```
SELECT
```

`a,`

```
  APPROX_COUNT_DISTINCT(b) as b,
FROM T1 GROUP BY a;
```

测试结果

| a (VARCHAR) | b (BIGINT) | c (BIGINT) |
|---|---|---|
| Hi | 6 | 6 |

##### FIRST_VALUE

本文为您介绍如何使用FIRST_VALUE函数，返回指定数据流的第1条非NULL数据。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| value | 任意参数类型 | 指定数据流。 说明如果输入数据全为NULL，则返回NULL。 |
| order | BIGINT | 根据order判定FIRST VALUE所在行，取order值最小的记 _ 录作为FIRST VALUE。 _ |

所有输入参数需要为相同的数据类型。

**重要**

**示例**

测试数据表 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |
| 4 | 4 | Hello |
| 5 | 5 | Hello |
| 6 | 6 | Hello |

实时计算（流计算）

| 7 | 7 | NULL |
|---|---|---|
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

测试语句

```
OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

测试结果

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| Hello | 1 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 7 |
| Hello World | 7 |

##### LAST_VALUE

本文为您介绍如何使用LAST_VALUE函数，返回指定数据流的最后1条非NULL数据。 本文仅适用于VVP 2.4.0且VVR 3.0.0及以上版本。

**重要**

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| value | 任意参数类型 | 指定数据流。 |
| order | BIGINT | 根据order判定LAST VALUE所在的行，取order值最大的 _ 记录作为LAST VALUE。 _ |

实时计算（流计算） 所有输入参数需要为相同的数据类型。

**重要**

**示例**

测试数据表 1. T1

| a(BIGINT) | b(INT) | c(VARCHAR) |
|---|---|---|
| 1 | 1 | Hello |
| 2 | 2 | Hello |
| 3 | 3 | Hello |
| 4 | 4 | Hello |
| 5 | 5 | Hello |
| 6 | 6 | Hello |
| 7 | 7 | NULL |
| 8 | 7 | Hello World |
| 9 | 8 | Hello World |
| 10 | 20 | Hello World |

测试语句

```
OVER (PARTITION BY c ORDER BY PROCTIME() RANGE UNBOUNDED PRECEDING) AS var1 FROM T1;
```

测试结果

| c(VARCHAR) | var1(INT) |
|---|---|
| Hello | 1 |
| Hello | 2 |
| Hello | 3 |
| Hello | 4 |
| Hello | 5 |
| Hello | 6 |
| NULL | 7 |
| Hello World | 7 |
| Hello World | 8 |
| Hello World | 20 |

### 自定义函数（Datastream）

实时计算（流计算）

#### 概述

本文为您介绍Flink自定义函数开发时的注意事项、自定义函数的分类、定义和参数传递方法。

**注意事项**

为了避免JAR包依赖冲突，在开发自定义函数时您需要注意以下几点： 作业开发页面选择的Flink版本，请和Pom依赖中的Flink版本保持一致。 Flink相关依赖，scope请使用provided，即在依赖中添加 `<scope>provided</scope>` 。 其他第三方依赖请采用Shade方式打包，Shade打包详情请参见Apache Maven Shade Plugin。

**自定义函数分类**

Flink支持以下3类自定义函数。

| 分类 | 描述 |
|---|---|
| UDF（User Defined Scalar Function） | 用户自定义标量值函数，将0个、1个或多个标量值映射到一个新的标量值。其输入与输出是一对一的关系，即读入一行数据，写出一条输出值。 详情请参见自定义标量函数（UDF）。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数，将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。详情请参见自定义聚合函数 （UDAF）。 |
| UDTF（User Defined Table-valued Function） | 自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。详情请参见自定义表值函数 （UDTF）。 |

**自定义函数参数传递**

如果您的自定义函数中某些参数值后期需要修改，直接在UDF代码里修改会很麻烦。此时，您可以在Flink全托管控制台更多Flink配置项中配置该参数后，在UDF代码中使用该参数。后续您可以直接在Flink全托管控制台修改该参数值，从而达到快速修改UDF参数值的目的。 自定义函数中提供了可选的open(FunctionContext context)方法，FunctionContext具备参数传递功能，自定义配置项通过此对象来传递。自定义函数的参数传递操作步骤如下：
1. 在作业开发页面右侧**高级配置**面板**更多****Flink****配置**中添加参数及取值。代码示例如下。

```
maxJobCreationAttempts: value
```

2. 在UDF代码中通过ConfigOptions.key()方式获取自定义函数参数。代码示例如下。

```
String strValue = context.getJobParameter("key","default_value"); Integer intValue = Integer.parseInt(context.getJobParameter("key","default_value"));
```

如果函数参数是key-value格式的，只能使用FunctionContext#getJobParameter方法获取 pipeline.global-job-parameters配置项的值。在pipeline.global-job-parameters中定义key-value 时，key和value之间需要通过半角冒号（:）分隔，不同kv之间需要通过逗号（,）分隔。如果key或value中含有半角冒号或逗号，需要使用半角双引号（"）包围起来。如果在此情况下key或value中还含有半角双引号，则需要通过连写两个半角双引号（""）进行转义。代码示例如下。

```
pipeline.global-job-parameters: 'json1:"{k1:""value1""}",json2:"k2"'
```

该配置就定义了以下的map。

| key | value |
|---|---|
| json1 | {k1:""value1""} |

实时计算（流计算）

| json2 | k2 |
|---|---|

此时就能通过FunctionContext#getJobParameter获取上述map的各项内容。

```
context.getJobParameter("json1", null); // 获得字符串{k1:""value1""} context.getJobParameter("json2", null); // 获得字符串k2
```

**自定义函数注册方法**

自定义函数分为全局自定义函数和作业级自定义函数，注册方法详情如下所示： 全局自定义函数 i. 登录实时计算开发平台。 ii. 在左侧导航栏上，单击**作业开发**。 iii. 在**UDFs**页签，单击图标。 iv. 上传自定义函数JAR文件。 您可以通过以下任何一种方式上传自定义函数JAR文件：
**上传文件**：单击**选择文件**项右侧的**选择文件**后，选择您的目标自定义函数JAR文件。如果有依赖文件，单
击**依赖文件**项右侧的**选择文件**，选择您的目标自定义函数JAR所依赖的文件。
**外部****URL**：输入外部URL地址。

**说明**

您的自定义函数JAR文件会被上传到您选择的OSS Bucket中的sql-artifacts目录下。此外，Flink开发控制台会解析自定义函数JAR文件中是否使用了Flink UDF、UDAF和UDTF接口的类，并自动提取类名，填充到Function Name字段中。 对于Java类型的UDF，其依赖可以打包到自定义函数JAR包中，也可以通过依赖文件项进行上传。 在自定义函数文件或者其依赖文件比较大时，推荐通过外部URL的方式进行上传。需要注意的是，如果外部URL是OSS Bucket地址，其依赖文件必须位于sqlartifacts/namespaces/{namespace}目录下。 v. 单击**确认**。 在SQL编辑器页面左侧**UDFs**列表，您可以看到所有注册成功的UDF。 作业级自定义函数因全局自定义函数（Catalog Function）在注册时，默认使用最新的Flink版本解析。如果您在作业中使用全局自定义函数，同时在高级配置选中了非最新的Flink版本，则有可能出现不兼容的问题。此时，您可以根据作实时计算（流计算） 业需要使用的引擎版本来实现UDF代码，并通过作业级自定义函数的方式解决此问题。作业级自定义函数的使用流程如下： i. 上传自定义函数JAR包。 在左侧导航栏**资源上传**中，上传自定义函数JAR包。 ii. 在作业中指定作业级自定义函数。 在作业**附加依赖文件**中，指定自定义函数JAR包。 iii. 注册自定义函数。 通过 `CREATE TEMPORARY FUNCTION` 语法注册作业级自定义函数。

```
CREATE TEMPORARY FUNCTION MyScalarFunc AS 'com.test.MyScalarFunc';
```

#### 自定义标量函数（UDF）

**定义**

自定义标量函数（UDF）将0个、1个或多个标量值映射到一个新的标量值。输入与输出是一对一的关系，即读入一行数据，写出一条输出值。

**UDF开发**

Flink为您提供了UDX示例，便于您快速开发业务。Flink UDX示例中包含UDF、UDAF和UDTF

**说明**

的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规则、缺
陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDF.java**：自定义标量函数（UDF）示例的Java代
码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDF后，根据您的业务，配置**ASI_UDF.java**。
该示例中，**ASI_UDF.java**已配置了获取每条数据中从begin~end位的字符的代码。

```java
package ASI_UDF; import org.apache.flink.table.functions.ScalarFunction; public class ASI_UDF extends ScalarFunction {
    public String eval(String s, Integer begin, Integer end) {
        return s.substring(begin, end);
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。 实时计算（流计算）

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDF开发工作。

**UDF注册**

UDF注册过程，请参见管理自定义函数（UDF）。

**UDF使用**

在注册UDF完成后，您就可以使用UDF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDF_Source表中a字段中每行字符串中第2~4位的字符，代码示例如下。 实时计算（流计算）

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDF_Sink SELECT ASI_UDF('a',2,4) FROM ASI_UDF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDF_Sink表每行会被插入ASI_UDF_Source表中a字段每行字符串的第2~4位字符。

#### 自定义聚合函数（UDAF）

**定义**

自定义聚合函数（UDAF），将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。

**UDAF开发**

**说明**

Flink为您提供了UDF示例，便于您快速开发业务。Flink UDF示例中包含UDSF、UDAF和UDTF的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规则、缺
陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDAF\ASI_UDAF.java**：自定义聚合函数（UDAF）示例的
Java代码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDAF后，根据您的业务，配置**ASI_UDAF.java**。
该示例中，**ASI_UDAF.java**已配置了当前数据和历史数求和的代码。例如，第1个数据是1，第2个数据是2， 第3个数据是3，则第一个结果是1，第2个结果是3，第3个结果是6。 实时计算（流计算）

```java
package ASI_UDAF; import org.apache.flink.table.functions.AggregateFunction; public class ASI_UDAF{
    public static class AcSum {
        public long sum;
    }
    public static class WeightedSum extends AggregateFunction<Long, AcSum> {
        @Override
        public Long getValue(AcSum acSum) {
            return acSum.sum;
        }
        @Override
        public AcSum createAccumulator() {
            AcSum acCount = new AcSum();
            acCount.sum = 0;
            return acCount;
        }
        public void accumulate(AcSum acc, long acSum) {
            acc.sum += acSum;
        }
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。 实时计算（流计算）

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDAF开发工作。

**UDAF注册**

UDAF注册过程，请参见管理自定义函数（UDF）。

**UDAF使用**

在注册UDAF完成后，您就可以使用UDAF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDAF_Source表中a字段当前数据和历史数据之和，代码示例如下。

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  sum  BIGINT
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDAF_Sink SELECT `ASI_UDAF$WeightedSum`(a) FROM ASI_UDAF_Source;
```

实时计算（流计算）
2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDAF_Sink表每行会被插入ASI_UDAF_Source表中a字段当前数据和历史数据之和。

#### 自定义表值函数（UDTF）

**定义**

自定义表值函数（UDTF），自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。

**UDTF开发**

**说明**

Flink为您提供了UDF示例，便于您快速开发业务。Flink UDF示例中包含UDSF、UDAF和UDTF的实现，示例中已为您配置对应版本的开发环境，您无需进行环境搭建。
1. 下载并解压ASI_UDX_Demo示例到本地。
解压完成后，会生成**ASI_UDX-main**文件夹。其中：
**pom.xml**：项目级别的配置文件，主要描述了项目的Maven坐标、依赖关系，开发者需要遵循的规则、缺
陷管理系统，组织和Licenses，以及其他所有的项目相关因素。
**\ASI_UDX-main\src\main\java\ASI_UDF\ASI_UDTF.java**：自定义表值函数（UDTF）示例的Java
代码。
2. 在Intellij IDEA中，单击**file > open**，打开刚才解压缩完成的**ASI_UDX-main**。
3. 双击打开\ASI_UDX-main\src\main\java\ASI_UDTF后，根据您的业务，修改**ASI_UDTF.java**文件内容。
该示例中，**ASI_UDTF.java**已配置了将一行字符串按照竖线（|）分割成多列字符串的代码。

```java
package ASI_UDTF; import org.apache.flink.api.java.tuple.Tuple2; import org.apache.flink.table.functions.TableFunction; public class ASI_UDTF extends TableFunction<Tuple2<String,String>> {
    public void eval(String str){
        String[] split = str.split("\\|");
        String name = split[0];
        String place = split[1];
        Tuple2<String,String> tuple2 = Tuple2.of(name,place);
        collect(tuple2);
    }
}
```

4. 双击打开\ASI_UDX-main\后，配置**pom.xml**。
该示例中，**pom.xml**文件已配置了Flink 1.11版依赖的主要JAR包信息。如果您的业务： Flink 1.11版依赖的主要JAR包如下。 实时计算（流计算）

```xml
<dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-streaming-java_2.12</artifactId>
            <version>1.11.0</version>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table</artifactId>
            <version>1.11.0</version>
            <type>pom</type>
            <!--<scope>provided</scope>-->
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-core</artifactId>
            <version>1.11.0</version>
        </dependency>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-table-common</artifactId>
            <version>1.11.0</version>
        </dependency>
    </dependencies>
```

5. 在下载文件中**pom.xml**所在的目录执行如下命令打包文件。

```
mvn package -Dcheckstyle.skip
```

\ASI_UDX-main\target\目录下会出现**ASI_UDX-1.0-SNAPSHOT.jar**的JAR包，即代表完成了UDTF开发工作。

**UDTF注册**

UDTF注册过程，请参见管理自定义函数（UDF）。

**UDTF使用**

在注册UDTF完成后，您就可以使用UDTF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
ASI_UDTF_Source表中message字段每行字符串按照竖线（|）分割成多列，代码示例如下。 实时计算（流计算）

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH (
  'connector'='datagen'
); CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(ASI_UDTF(`message`)) as T(name,place);
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDTF_Sink表会被插入ASI_UDTF_Source表中message字段按照竖线（|）分割成多列的字符。

### 自定义函数（Python）

#### 概述

Flink支持在SQL作业中使用Python自定义函数，本文为您介绍Flink自定义函数UDX的分类、定义和依赖，以及如何进行调试和调优。

**UDX分类**

Flink支持以下3类自定义函数。

| UDX分类 | 描述 |
|---|---|
| UDF（User Defined Scalar Function） | 用户自定义标量函数，将0个、1个或多个标量值映射到一个新的标量值。其输入与输出是一对一的关系，即读入一行数据，写出一条输出值。详情请参见自定义标量函数（UDF）。 |
| UDAF（User Defined Aggregation Function） | 自定义聚合函数，将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。详情请参见自定义聚合函数 （UDAF）。 |
| UDTF（User Defined Table-valued Function） | 自定义表值函数，将0个、1个或多个标量值作为输入参数（可以是变长参数）。与自定义的标量函数类似，但与标量函数不同。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。详情请参见自定义表值函数（UDTF）。 |

**依赖**

Flink集群已预装了Pandas、NumPy和PyArrow等常用的Python包，您可以在作业开发页面，了解Flink集群中已安装的第三方Python包列表。 此外，您也可以在Python自定义函数中使用其它类型的第三方Python包。需要注意的是，如果使用了非预装的第三方Python包，在注册Python UDF时，需要将其作为依赖文件上传，详情请参见管理自定义函数和使用 Python依赖。

**调试**

您可以在Python自定义函数的代码实现中，通过Logging的方式，输出日志信息，方便问题定位，示例如下。 实时计算（流计算）

```python
@udf(result_type=DataTypes.BIGINT()) def add(i, j):
  logging.info("hello world")
  return i + j
```

日志输出后，您可以在TaskManager的日志文件中查看日志。

**调优**

使用Pandas库除了普通Python自定义函数之外，Flink也支持您使用Pandas自定义函数。对于Pandas自定义函数，输入数据的类型是Pandas中定义的数据结构，例如pandas.Series和pandas.DataFrame等，您可以在Pandas自定义函数中使用Pandas和Numpy等高性能的Python库，开发出高性能的Python自定义函数，详情请参见Vectorized User-defined Functions。 配置以下参数 Python自定义函数的性能在很大程度取决于Python自定义函数自身的实现，如果遇到性能问题，您需要尽可能优化Python自定义函数的实现。除此之外，Python自定义函数的性能也受以下参数取值的影响。

| 参数 | 说明 |
|---|---|
| python.fn-execution.bundle.size | Python UDF的计算是异步的，在执行过程中，Java算子将数据异步发送给 Python进程进行处理。Java算子在将数据发送给Python进程之前，会先将数据缓存起来，到达一定阈值之后，再发送给Python进程。python.fn- execution.bundle.size参数可用来控制可缓存的数据最大条数。 默认值为100000，单位是条数。 |
| python.fn-execution.bundle.time | 用来控制数据的最大缓存时间。当缓存的数据条数到达python.fn- execution.bundle.size定义的阈值或缓存时间到达python.fn- execution.bundle.time定义的阈值时，会触发缓存数据的计算。 默认值为1000，单位是毫秒。 |
| python.fn- execution.arrow.batch.size | 使用Pandas UDF时，一个arrow batch可容纳的数据最大条数，默认值为 10000。 说明 python.fn-execution.arrow.batch.size参数值不能大于 python.fn-execution.bundle.size参数值。 |

以上3个参数并不是配置的越大越好，当这些参数取值配置过大时，可能会导致Checkpoint

**说明**

时，需要处理过多的数据，从而导致Checkpoint时间过长，甚至会导致Checkpoint失败。以上参数的更多详情，请参见Configuration。

#### 自定义标量函数（UDF）

本文为您介绍Python自定义标量函数（UDF）的使用限制、开发、注册和使用流程。

**定义**

自定义标量函数（UDF）将0个、1个或多个标量值映射到一个新的标量值。输入与输出是一对一的关系，即读入一行数据，写出一条输出值。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 实时计算（流计算） 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的JAR包依赖。

**UDF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包含了

**说明**

Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行 UDF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udfs.py后，根据您的业务，修改**udfs.py**。
该示例中，**sub_string**定义了获取每条数据中从begin~end位的字符的代码。

```python
from pyflink.table import DataTypes from pyflink.table.udf import udf @udf(result_type=DataTypes.STRING()) def sub_string(s: str, begin: int, end: int):
    return s[begin:end]
```

4. 在下载文件中udx所在的目录（即\python_demo-master目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo-master\目录下会出现**python_demo.zip**ZIP包，即代表完成了Python UDF的开发工作。

**UDF注册**

UDF注册过程，请参见注册自定义函数。

**UDF使用**

在完成注册UDF后，您就可以使用UDF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDF_Source表中a字段中每行字符串中第2~4位的字符，代码示例如下。

```
CREATE TEMPORARY TABLE ASI_UDF_Source (
  a VARCHAR,
  b INT,
  c INT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE ASI_UDF_Sink (
  a VARCHAR
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDF_Sink SELECT ASI_UDF(a,2,4) FROM ASI_UDF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDF_Sink表每行会被插入ASI_UDF_Source表中a字段每行字符串的第2~4位字符。 实时计算（流计算）

#### 自定义聚合函数（UDAF）

本文为您介绍Python自定义聚合函数（UDAF）的使用限制、开发、注册和使用流程。

**定义**

自定义聚合函数（UDAF），将多条记录聚合成1条记录。其输入与输出是多对一的关系，即将多条输入记录聚合成一条输出值。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的JAR包依赖。

**UDAF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包含了

**说明**

Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行 UDAF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udafs.py后，根据您的业务，配置**udafs.py**。
该示例中，**weighted_avg**定义了当前数据和历史数据求含权重的均值的代码。 实时计算（流计算）

```python
from pyflink.common import Row from pyflink.table import AggregateFunction, DataTypes from pyflink.table.udf import udaf class WeightedAvg(AggregateFunction):
    def create_accumulator(self):
        # Row(sum, count)
        return Row(0, 0)
    def get_value(self, accumulator: Row) -> float:
        if accumulator[1] == 0:
            return 0
        else:
            return accumulator[0] / accumulator[1]
    def accumulate(self, accumulator: Row, value, weight):
        accumulator[0] += value * weight
        accumulator[1] += weight
    def retract(self, accumulator: Row, value, weight):
        accumulator[0] -= value * weight
        accumulator[1] -= weight
weighted_avg = udaf(f=WeightedAvg(),
                    result_type=DataTypes.DOUBLE(),
                    accumulator_type=DataTypes.ROW([
                        DataTypes.FIELD("f0", DataTypes.BIGINT()),
                        DataTypes.FIELD("f1", DataTypes.BIGINT())]))
```

4. 在下载文件中udx所在的目录（即\python_demo-master目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo-master\目录下会出现**python_demo.zip**的ZIP包，即代表完成了UDAF开发工作。

**UDAF注册**

UDAF注册过程，请参见注册自定义函数。

**UDAF使用**

在完成注册UDAF后，您就可以使用UDAF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
获取ASI_UDAF_Source表中a字段以b字段为权重的a字段当前数据和历史数据的均值，代码示例如下。 实时计算（流计算）

```
CREATE TEMPORARY TABLE ASI_UDAF_Source (
  a   BIGINT,
  b   BIGINT
) WITH (
  'connector' = 'datagen'
); CREATE TEMPORARY TABLE ASI_UDAF_Sink (
  avg_value  DOUBLE
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDAF_Sink SELECT weighted_avg(a, b) FROM ASI_UDAF_Source;
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDAF_Sink表每行会被插入ASI_UDAF_Source表中以b字段为权重的a字段当前数据和历史数据的均值。

#### 自定义表值函数（UDTF）

本文为您介绍Python自定义表值函数（UDTF）的使用限制、开发、注册和使用流程。

**定义**

自定义表值函数（UDTF），将0个、1个或多个标量值作为输入参数（可以是变长参数）。表值函数可以返回任意数量的行作为输出，而不仅是1个值。返回的行可以由1个或多个列组成。调用一次函数输出多行或多列数据。 与自定义的标量函数类似，但与标量函数不同。

**使用限制**

由于Flink产品受部署环境和网络环境等因素的影响，所以开发Python自定义函数时，需要注意以下限制： 仅支持开源Flink V1.12及以上版本。 Flink集群上已预装了Python 3.7.9，因此需要您在Python 3.7.9版本开发代码。 Flink运行环境使用的是JDK 1.8，如果Python作业中依赖第三方JAR包，请确保JAR包兼容JDK 1.8。 仅支持开源Scala V2.11版本，如果Python作业中依赖第三方JAR包，请确保使用Scala V2.11对应的JAR包依赖。

**UDTF开发**

Flink为您提供了Python UDX示例，便于您快速开发UDX。Flink Python UDX示例中包含了

**说明**

Python UDF、Python UDAF和Python UDTF的实现。本文以Windows操作系统为例，为您介绍如何进行 UDTF开发。
1. 下载并解压python_demo-master示例到本地。
2. 在PyCharm中，单击**file > open**，打开刚才解压缩完成的**python_demo-master**。
3. 双击打开\python_demo-master\udx\udtfs.py后，根据您的业务，修改**udtfs.py**文件内容。
该示例中，**split**定义了将一行字符串按照竖线（|）分割成多列字符串的代码。 实时计算（流计算）

```python
from pyflink.table import DataTypes from pyflink.table.udf import udtf @udtf(result_types=[DataTypes.STRING(), DataTypes.STRING()]) def split(s: str):
    splits = s.split("|")
    yield splits[0], splits[1]
```

4. 在下载文件中udx所在的目录（即\python_demo目录）下执行如下命令打包文件。

```
zip -r python_demo.zip udx
```

\python_demo\目录下会出现**python_demo.zip**的ZIP包，即代表完成了UDTF开发工作。

**UDTF注册**

UDTF注册过程，请参见注册自定义函数。

**UDTF使用**

在完成UDTF注册后，您就可以使用UDTF，详细的操作步骤如下。
1. Flink SQL作业开发。详情请参见作业开发。
ASI_UDTF_Source表中每行字符串的message字段与字符串aa按照竖线（|）连接之后，按照竖线（|）分割成多列，代码示例如下。

```
CREATE TEMPORARY TABLE ASI_UDTF_Source (
  `message`  VARCHAR
) WITH (
  'connector'='datagen'
); CREATE TEMPORARY TABLE ASI_UDTF_Sink (
  name  VARCHAR,
  place  VARCHAR
) WITH (
  'connector' = 'blackhole'
); INSERT INTO ASI_UDTF_Sink SELECT name,place FROM ASI_UDTF_Source,lateral table(split(concat_ws('|', `message`, 'aa'))) as T(name,place );
```

2. 在**作业列表**中，单击目标作业名称**操作**列的**启动**。
启动成功后，ASI_UDTF_Sink表会被插入两列数据，这两列数据是ASI_UDTF_Source表中message和aa字段按照竖线（|）连接后，再按照竖线（|）分割成多列的字符。

### 机器学习函数

#### CLUSTER_SERVING

本文以输入格式为input_shape=(?,128)的Tensorflow SavedMode模型为例，为您介绍如何使用机器学习函

**使用限制**

本文仅适用于VVP 2.4.2及以上版本。 实时计算（流计算）

**背景信息**

Analytics Zoo是英特尔®开源的统一大数据分析和AI平台，支持分布式TensorFlow及PyTorch的训练和推理， 通过英特尔® OpenVINO工具套件和DL Boost指令集等，提升深度学习工作负载的性能。Analytics Zoo Cluster Serving是Analytics Zoo的分布式推理解决方案，可以部署在Apache Flink集群上进行分布式运算。 通过使用Cluster Serving，您无需编写任何机器学习相关代码，即可实现端到端的分布式机器学习推理流程。 Analytics Zoo详情请参见Analytics Zoo。 Cluster Serving将其部分功能集成在Flink的内置函数中，支持TensorFlow、PyTorch和OpenVINO的推理模型。您可以直接在Flink开发控制台中调用CLUSTER_SERVING函数，进行分布式机器学习推理。使用 CLUSTER_SERVING函数时，您只需要提供模型文件和数据文件，即可完成机器学习端到端的应用。

**语法**

**入参**

| 参数 | 数据类型 | 说明 |
|---|---|---|
| uri | String | 数据ID。 |
| data | String | 数据。 |

**示例**

测试数据表 1. input.csv

| uri(String) | data(String) |
|---|---|
| my-data | 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 |

测试步骤 i. 登录OSS控制台，上传测试数据input.csv文件至oss://***/input.csv目录。 ii. 在Flink开发控制台，创建源表和结果表、加载模型并将CLUSTER_SERVING函数在线推理的数据插入结果表。 实时计算（流计算）

```
   uri STRING,
  `data` STRING
) WITH (
   'connector' = 'filesystem',
   'path' = 'oss://alink-vvp/artifacts/namespaces/test-module-default/input.csv',
   'format' = 'csv'
);
   uri1 STRING,
   data1 STRING
 ) WITH (
   'connector' = 'print'
); LOAD MODULE `cluster-serving`; INSERT INTO ClusterServingOutput SELECT cluster_serving(uri, `data`) FROM ClusterServing Input;
```

iii. 在作业**高级配置**的**更多****Flink****配置**和Preview Session集群**其他配置**均增加以下配置，并单击**保存**。

```
pipeline.global-job-parameters: '"modelPath:""[模型目录地址]"""'
```

其中，模型目录地址为您模型文件的OSS存放目录，例如oss://***/tf_auto/。 iv. 在作业运维界面，单击目标作业**操作**列下的**启动**。 测试结果

| uri1 | data1 |
|---|---|
| 0.03932024,0.017788976,-2.2538425E- 4,0.021853039,0.030905273,0.052324444,0.053021688,0.08776946 ,0.0625467,0.12149326,0.048770625,0.04533424,0.09271586,0.023 119276,0.0037812046,0.052707616,0.029312208,0.023519568,0.07 501668,0.037939064,0.06363185,0.04994791,0.08504477,0.069405 96,0.052632406,0.028651983,0.02205597,0.05861686,0.040175162 ,0.04682718,0.05283319,0.01967535,0.111778766,0.03182444,0.04 509241,0.09942829,0.009491239,0.038903005,0.11488753,0.01950 3327,0.0346709,0.060727723,0.03718308,0.1295206,0.04292037,0. 13272661,0.009957914,0.050370887,0.03016096,0.067269124,0.09 981682,0.08606887,0.085193545,0.041775055,0.02956512,0.02714 2545,0.09836763,0.029330501,0.040107135,0.0753366,0.06851786 4,0.020111244,0.086271614,0.04449262,0.107297346,0.07932708, 0.036529146,0.014892701,0.08245985,0.04272034,0.076421194,0. 035283472,0.028554386,0.019374546,0.048012834,0.011391987,0. 028220229,0.054405782,0.037807927,0.085761145,0.07974813,0.0 4150249,- 0.017132144,0.08219319,0.019887058,0.034193676,0.06221051,0. 07516215,0.0598385,0.09159884,0.038117558,0.05329266,0.02103 8251,0.072046585,0.05561088,0.017538168,0.025691401,0.085806 02,0.02225845,0.117060736,0.060743354,0.11840888,0.065381594 ,0.08059649,0.045638822,0.06399781,0.011646094,0.043574452,0. 123603456,0.045708194,0.05672055,0.08402837,0.118181005,0.09 657015,0.08259893,0.0010145458,0.031954847,0.07388758,0.0353 80267,0.070080444,0.06764534,0.058731187,0.022044828,0.09435 9346,0.05559277,0.032255664,0.07360537,0.11992536 | 128 |
