---
title: "云数据库RDS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 351
source_pdf: "15_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/rds/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云数据库RDS 开发指南

云数据库RDS

## 调用云产品SDK

### 准备工作

#### 登录开发者门户

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
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者服务**。

#### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。 云数据库RDS

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

#### 获取AccessKey

访问身份验证中通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。本文将为您描述如何获取通过RAM授权的AccessKey。

**前提条件**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**背景信息**

AccessKey支持两种授权模式： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 本文仅为您介绍如何获取通过RAM授权的AccessKey。 云数据库RDS 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，将鼠标悬停在当前登录用户的头像上，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
云数据库RDS
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

#### 获取公共Header参数

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
云数据库RDS
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

#### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。
云数据库RDS

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
云数据库RDS

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

### 通过POP网关调用专有云API

#### 调用前置

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

**获取云产品的Endpoint**

**通过开发者门户获取**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
云数据库RDS
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
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

**获取公共参数**

云数据库RDS 通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请

#### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下：

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

云数据库RDS `//` 设置访问接口版本

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

ROA调用，示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
```

云数据库RDS

```
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
```

云数据库RDS

```java
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

#### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **开发**
**工具** > **API****与工具** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 云数据库RDS

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 云数据库RDS

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 云数据库RDS

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

云数据库RDS

#### Python版

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

云数据库RDS
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

云数据库RDS

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

) 云数据库RDS

## API参考

### 实例管理

#### 创建RDS实例

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 否 | CreateDBInsta nce | 系统规定参数。取值：CreateDBInstance。 |
| RegionId | Strin g | Quer y | 是 | cn-hangzhou | 地域ID。可以通过接口DescribeRegions查看可用的地域ID。 |
| Engine | Strin g | Quer y | 是 | MySQL | 数据库类型。取值： MySQL SQLServer（已停售） PostgreSQL POLARDB |
| EngineVers ion | Strin g | Quer y | 是 | 5.6 | 数据库版本。取值： MySQL：5.5/5.6/5.7/8.0 SQL Server： 2008r2/08r2 ent ha/2012/2012 ent ha/20 _ _ _ _ 12 std ha/2012 web/2014 std ha/2016 en _ _ _ _ _ _ t ha/2016 std ha/2016 web/2017 std ha/2 _ _ _ _ _ _ 017 ent/2019 std ha/2019 ent _ _ _ _ PostgreSQL：9.4/10.0/11.0/12.0/13.0 POLARDB：11 |
| DBInstance Class | Strin g | Quer y | 是 | rds.mysql.s1.s mall | 实例规格。详情请参见云数据库RDS > 产品简介中的实例规格表。您也可以调用 DescribeAvailableResource接口查询目标地域中可用的实例规格列表。 |

云数据库RDS

| DBInstance Storage | Inte ger | Quer y | 是 | 20 | 实例存储空间。单位：GB。每5GB进行递增，取值范围请参见云数据库RDS > 产品简介中的实例规格表。您也可以调用DescribeAvailableResource接口查询目标实例规格中可用的存储空间范围。 |
|---|---|---|---|---|---|
| DBInstance StorageTyp e | Strin g | Quer y | 否 | cloud ssd _ | 实例存储类型。取值： local ssd：本地SSD盘（推荐） _ cloud ssd：SSD云盘 _ cloud essd：ESSD PL1云盘 _ cloud essd2：ESSD PL2云盘 _ cloud essd3：ESSD PL3云盘 _ |
| DBInstance NetType | Strin g | Quer y | 是 | Internet | 实例的网络连接类型。取值： Internet：公网连接。 Intranet：内网连接。 |
| DBInstance Description | Strin g | Quer y | 否 | 测试数据库 | 实例名称。长度为2~255个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线 （ ）、短横线（-）。 _ 说明不能以 http:// 和 https:// 开头。 |
| SecurityIPLi st | Strin g | Quer y | 是 | 10.23.12.27/2 4 | 该实例的IP白名单。多条记录请以英文逗号（,）隔开，不可重复，最多1000条记录。支持如下两种格式： IP地址形式，例如：10.23.12.24。 CIDR形式，例如：10.23.12.24/24（无类域间路由，24表示地址中前缀的长度，范围为 1~32）。 |
| ClientToke n | Strin g | Quer y | 否 | ETnLKlblzczsh OTUbOCzxxxx xxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非 ASCII字符。 |
| PayType | Strin g | Quer y | 是 | Postpaid | 实例的付费类型。取值固定为Postpaid（按量付费）。 |

云数据库RDS

| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-b | 主节点可用区ID。 指定了VPC和交换机时，为匹配交换机对应的可用区，该参数必填。 对于高可用版实例，还需传入ZoneIdSlave1，以决定实例是单可用区部署还是多可用区部署。 |
|---|---|---|---|---|---|
| InstanceNe tworkType | Strin g | Quer y | 否 | Classic | 实例的网络类型。取值： VPC：VPC网络。 Classic：经典网络（默认）。 |
| Connection Mode | Strin g | Quer y | 否 | Standard | 实例的访问模式。取值： Standard：标准访问模式。 Safe：数据库代理模式。 说明 SQL Server 2012、2016、2017只支持标准访问模式。 |
| VPCId | Strin g | Quer y | 否 | vpc- xxxxxxxxxxxx | 专有网络（VPC） ID。 说明 InstanceNetworkType必须为VPC。 |
| VSwitchId | Strin g | Quer y | 否 | vsw- xxxxxxxxxxx | 虚拟交换机（VSwitch） ID。多个值用英文逗号 （,）隔开。 说明 InstanceNetworkType必须为VPC。 |
| PrivateIpAd dress | Strin g | Quer y | 否 | 172.XX.XXX.69 | 设置实例的内网IP。需要在指定交换机的IP地址范围内。系统默认通过VPCId和VSwitchId自动分配。 |
| ResourceGr oupId | Strin g | Quer y | 否 | rg-acfmy****** | 资源组ID。 |
| Category | Strin g | Quer y | 否 | HighAvailabilit y | 实例系列。取值： Basic：基础版 HighAvailability：高可用版 AlwaysOn：集群版 |

云数据库RDS

| ZoneIdSlav e1 | Strin g | Quer y | 否 | cn-hangzhou-c | 备节点可用区ID。如果和ZoneId相同，则为单可用区部署；如果和ZoneId不同，则为多可用区部署。 |
|---|---|---|---|---|---|
| ZoneIdSlav e2 | Strin g | Quer y | 否 | cn-hangzhou-d | 日志节点可用区ID。如果和ZoneId相同，则为单可用区部署；如果和ZoneId不同，则为多可用区部署。 |
| Encryption Key | Strin g | Quer y | 否 | 0d24xxxx- da7b-4786- b981- 9a164dxxxxxx | 同地域内的云盘加密的密钥ID。您可以在密钥管理服务控制台查看密钥ID，也可以创建新的密钥。 说明传入此参数表示开启云盘加密（开启后无法关闭），且需要传入RoleARN。 |
| RoleARN | Strin g | Quer y | 否 | acs:ram::1406 xxxxxx:role/ali yunrdsinstanc eencryptiondef aultrole | 主账号授权RDS云服务账号访问KMS权限的全局资源描述符（ARN）。 |
| TdeStatus | Inte ger | Quer y | 否 | 0 | 是否开启TDE。 0：不开启 1：开启 |
| EncryptAlg orithm | Strin g | Quer y | 否 | aes-256 | 指定TDE的加密算法。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |
| DBInstanceId | String | rm-uf6wjk5****** | 实例ID。 |
| OrderId | String | 1007893702xxxxx | 订单ID。 |
| ConnectionStri ng | String | rm- uf6wjk5xxxxxxx.my sql.rds.aliyuncs.co m | 数据库连接地址。 说明参数DBInstanceNetType决定该地址为内网或外网。 |

云数据库RDS

| Port | String | 3306 | 数据库连接端口。 说明参数DBInstanceNetType决定该地址为内网或外网。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateDBInstance &RegionId=cn-hangzhou &Engine=MySQL &EngineVersion=5.6 &DBInstanceClass=rds.mysql.s1.small &DBInstanceStorage=20 &DBInstanceNetType=Internet &SecurityIPList=10.23.12.27/24 &PayType=Postpaid
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC",
 "DBInstanceId":"rm-uf6wjk5******",
 "Port":"3306",
 "OrderId":"100789370******",
 "ConnectionString":"rm-uf6wjk5******.mysql.rds.aliyuncs.com"
}
```

`XML` 格式

```xml
<RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId> <DBInstanceId>rm-uf6wjk5******</DBInstanceId> <Port>3306</Port> <OrderId>100789370******</OrderId> <ConnectionString>rm-uf6wjk5******.mysql.rds.aliyuncs.com</ConnectionString>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidIzNo.NotSup ported | InvalidZoneId.NotSupported | The Specified vpc Zone not supported. |

云数据库RDS

| 400 | InvalidZone.NotSup ported | InvalidZone.NotSupported | The Specified Zone not supported. |
|---|---|---|---|
| 500 | InsufficientResourc eCapacity | InsufficientResourceCapacity | %s |
| 500 | IncorrectEngineVer sion | IncorrectEngineVersion | Current DB instance engine version does not support this operation. |
| 500 | InvalidCpuType | InvalidCpuType | Specified parameter CpuType is not valid. |
| 500 | InvalidDBInstanceS torage.Format | InvalidDBInstanceStorage.For mat | The specified DBInstanceStorage is invalid. |
| 500 | VPC CLOUD INSTA _ _ NCEIP USED _ | VPC CLOUD INSTANCEIP USE _ _ _ D | the vpc cloudinstanceIp is use. |
| 500 | SUBNET IP EXHAU _ _ STED | SUBNET IP EXHAUSTED _ _ | error subnet ip exhaust |
| 400 | SpecifiedMinorVersi onProcessFailed | SpecifiedMinorVersionProcessF ailed | Specified minor version process failed. |

#### 查询实例详细信息

调用DescribeDBInstanceAttribute接口查询RDS实例的详细信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInstance Attribute | 系统规定参数，取值：DescribeDBInstanceAttribute。 |
| DBInstanceI d | String | 是 | rm- uf6wjk5xxxxxxxxxx | 实例ID。可以一次输入最多30个，以英文逗号（,）分隔。 |
| Expired | String | 否 | False | 实例过期状态，取值： True：已过期 False：未过期 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of DBInstanceAtt ribute |  | 实例属性列表。 |
| DBInstanceAttri bute |  |  |  |
| DBInstanceId | String | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |
| PayType | String | Postpaid | 实例付费方式，取值： Postpaid：按量付费 Prepaid：包年包月 |
| DBInstanceTyp e | String | Primary | 实例类型，取值： Primary：主实例 Readonly：只读实例 Guard：灾备实例 Temp：临时实例 |
| Category | String | Basic | 实例系列，取值： Basic：基础版 HighAvailability：高可用版 AlwaysOn：集群版 |
| InstanceNetwor kType | String | Classic | 实例的网络类型，取值： Classic：经典网络 VPC：专有网络 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| ZoneId | String | cn-hangzhou-a | 可用区ID。 |
| ConnectionStri ng | String | rm- uf6wjk5xxxxxxx xxx.mysql.rds.al iyuncs.com | 内网连接地址。 |

云数据库RDS

| Port | String | 3306 | 内网连接端口。 |
|---|---|---|---|
| Engine | String | MySQL | 数据库类型。 |
| EngineVersion | String | 5.5 | 数据库版本。 |
| DBInstanceClas sType | String | s | 实例规格族，取值： s：共享型 x：通用型 d：独享套餐 h：独占物理机 |
| DBInstanceClas s | String | rds.mys2.small | 实例规格，详情请参见云数据库RDS > 产品简介中的实例规格。 |
| DBInstanceMe mory | Long | 4096 | 实例内存，单位：M。 |
| DBInstanceStor age | Integer | 10 | 实例存储空间，单位：GB。 |
| DBInstanceNet Type | String | Internet | 实例是内网或外网，取值： Internet：外网 Intranet：内网 |
| DBInstanceStat us | String | Running | 实例状态，详情请参见本手册中的实例状态表。 |
| DBInstanceDes cription | String | 测试数据库 | 实例备注。 |
| LockMode | String | Unlock | 实例锁定模式： Unlock：正常 ManualLock：手动触发锁定 LockByExpiration：实例过期自动锁定 LockByRestoration：实例回滚前的自动锁定 LockByDiskQuota：实例空间满自动锁定 LockReadInstanceByDiskQuota：只读实例空间满自动锁定 |

云数据库RDS

| LockReason | String | instance expire _ d | 锁定原因。 |
|---|---|---|---|
| DBMaxQuantity | Integer | 200 | 一个实例下可创建最大数据库数量。 |
| AccountMaxQu antity | Integer | 50 | 可创建账号的最大数量。 |
| CreationTime | String | 2011-05- 30T12:11:04Z | 创建时间。yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| ExpireTime | String | 2019-03- 27T16:00:00Z | 到期时间。yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 说明按量付费实例无到期时间。 |
| MaintainTime | String | 00:00Z-02:00Z | 实例可维护时间段，是UTC时间，+8小时才是控制台上显示的可维护时间段。 |
| AvailabilityValu e | String | 100.0% | 实例可用性状态，单位：百分比。 |
| MaxIOPS | Integer | 150 | 最大每秒IO请求次数。 |
| MaxConnection s | Integer | 60 | 最大并发连接数。 |
| MasterInstance Id | String | rm- uf6wjk5xxxxxxx xxx | 主实例的ID，如果没有返回此参数则表示该实例是主实例。 |
| IncrementSour ceDBInstanceId | String | rm- uf6wjk5xxxxxxx xxx | 增量数据来源的实例ID，如灾备实例的增量数据来源是主实例。只读实例的增量数据来源是主实例，如果没有返回此参数则表示该实例是主实例。 |
| GuardDBInstan ceId | String | rm- uf64zsuxxxxxxx xxx | 该实例如果挂载着灾备实例，即为灾备实例的ID。 |
| TempDBInstan ceId | String | rm- uf64zsuxxxxxxx xxx | 该实例如果挂载着临时实例，即为临时实例ID。 |

云数据库RDS

| ReadOnlyDBIns tanceIds | Array of ReadOnlyDBIn stanceId |  | 主实例下挂载的只读实例ID列表。 |
|---|---|---|---|
| ReadOnlyDBIns tanceId |  |  |  |
| DBInstanceId | String | rm- bpxxxxxxxxx | 只读实例ID。 |
| AdvancedFeatu res | String | LinkedServer | 目前只针对SQL Server，获取高级特性值，多个值之间用英文逗号（,）隔开，现返回值如下： LinkedServer：链接服务器 DistributeTransaction：分布式事务 |
| AutoUpgradeMi norVersion | String | Auto | 实例升级小版本的方式，取值： Auto：自动升级小版本 Manual：不自动升级，仅在当前版本下线时才强制升级 |
| Collation | String | Chinese PRC CI _ _ AS _ | 系统字符集排序规则。 |
| ConnectionMod e | String | Standard | 实例的访问模式，取值： Standard：标准访问模式 Safe：数据库代理模式 |
| ConsoleVersion | String | 2 | 实例的代理类型。取值： 1：共享代理 2：独享代理说明不建议使用该参数，请使用返回参数ProxyType。 |
| CurrentKernelV ersion | String | rds 20181010 _ | 当前内核版本。 |
| DBInstanceStor ageType | String | local ssd _ | 实例储存类型，取值： local ssd/ephemeral ssd：本地SSD盘 _ _ cloud ssd：SSD云盘 _ cloud essd：ESSD云盘 _ |

云数据库RDS

| DispenseMode | String | 无 | 无效参数。 |
|---|---|---|---|
| EncryptionKey | String | 无 | 无效参数。 |
| EncryptionKey | String | 无 | 无效参数。 |
| Extra | Struct |  | 无效参数。 |
| ActiveReplicaD BInstanceID | String | 无 | 无效参数。 |
| DBInstanceId | List | 无 | 无效参数。 |
| ReplicaGroupID | String | 无 | 无效参数。 |
| ReplicaGroupSt atus | String | 无 | 无效参数。 |
| LatestKernelVe rsion | String | rds 20201031 _ | 当前实例支持的最新内核版本。 |
| MasterZone | String | 5454284 | 主可用区ID。 |
| ProxyType | Integer | 1 | 实例支持的代理类型，取值： 0：表示不支持开通代理 1：表示支持开通共享代理（多租户模式） 2：表示支持开通独享代理（单租户模式） |
| ReadonlyInstan ceSQLDelayedT ime | String | 30 | 只读实例延迟复制时间，只读实例延迟ReadonlyInstanceSQLDelayedTime的时间后再同步主实例数据，单位：秒。 |
| ResourceGroup Id | String | rg- acfmyxxxxxxxx xx | 资源组ID。 |

云数据库RDS

| SecurityIPMode | String | normal | 白名单模式。取值： normal：通用模式 safety：高安全模式 |
|---|---|---|---|
| SlaveConnectio nString | String | 无 | 无效参数。 |
| SlaveZones | Array of SlaveZone |  | 组成SlaveZones的参数。 |
| SlaveZone |  |  |  |
| ZoneId | String | cn-hangzhou-a | 可用区。 |
| TimeZone | String | Central Standard Time | 时区。 |
| VSwitchId | String | vsw-xxxxxx | 交换机ID。 |
| VpcCloudInstan ceId | String | vpc- 23rsxdfxxxxxxx | 专有网络实例ID。 |
| VpcId | String | vpc-xxxxxxxxx | VPC ID。 |
| RequestId | String | 1AD222E9- E606-4A42- BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceAttributeResponse>
  <RequestId>BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E</RequestId>
  <Items>
        <DBInstanceAttribute>
              <DBInstanceMemory>8192</DBInstanceMemory>
              <ResourceGroupId>rg-acfmyxxxxxxxxxx</ResourceGroupId>
```

/ 云数据库RDS

```xml
              <Port>3306</Port>
              <MasterZone>cn-hangzhou-h</MasterZone>
              <LatestKernelVersion>rds_20201031</LatestKernelVersion>
              <DBInstanceType>Primary</DBInstanceType>
              <ConsoleVersion>2</ConsoleVersion>
              <InstanceNetworkType>VPC</InstanceNetworkType>
              <DBInstanceClassType>x</DBInstanceClassType>
              <DBInstanceId>rm-uf6wjk5xxxxxxxxxx</DBInstanceId>
              <AutoUpgradeMinorVersion>Auto</AutoUpgradeMinorVersion>
              <DBInstanceStorage>150</DBInstanceStorage>
              <AvailabilityValue>100.0%</AvailabilityValue>
              <Engine>MySQL</Engine>
              <DBInstanceDescription>test1</DBInstanceDescription>
              <IPType>IPv4</IPType>
              <EngineVersion>8.0</EngineVersion>
              <DBInstanceStatus>Running</DBInstanceStatus>
              <MaxConnections>2000</MaxConnections>
              <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
              <AccountMaxQuantity>99999</AccountMaxQuantity>
              <VSwitchId>vsw-xxxxxx</VSwitchId>
              <PayType>Prepaid</PayType>
              <LockMode>Unlock</LockMode>
              <GuardDBInstanceId>rm-uf64zsuxxxxxxxxxx</GuardDBInstanceId>
              <SupportCreateSuperAccount>No</SupportCreateSuperAccount>
              <InsId>1</InsId>
              <VpcId>vpc-xxxxxxxxx</VpcId>
              <CurrentKernelVersion>rds_20200831</CurrentKernelVersion>
              <TempUpgradeTimeStart>2021-01-10 00:00:00</TempUpgradeTimeStart>
              <TempUpgradeTimeEnd>2021-06-18 00:00:00</TempUpgradeTimeEnd>
              <CreationTime>2020-06-17T09:03:57Z</CreationTime>
              <ConnectionMode>Standard</ConnectionMode>
              <VpcCloudInstanceId>vpc-23rsxdfxxxxxxx</VpcCloudInstanceId>
              <ProxyType>2</ProxyType>
              <ConnectionString>rm-
uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
              <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
              <DBMaxQuantity>99999</DBMaxQuantity>
              <Category>HighAvailability</Category>
              <DBInstanceNetType>Intranet</DBInstanceNetType>
              <SuperPermissionMode></SuperPermissionMode>
              <DedicatedHostGroupId></DedicatedHostGroupId>
              <DBInstanceCPU>4</DBInstanceCPU>
              <GuardDBInstanceName>rm-m5xxxxx</GuardDBInstanceName>
              <SecurityIPList>42.xx.xx.xx</SecurityIPList>
              <OriginConfiguration></OriginConfiguration>
              <ReadOnlyDBInstanceIds>
        </ReadOnlyDBInstanceIds>
              <SecurityIPMode>normal</SecurityIPMode>
              <MaintainTime>23:00Z-00:00Z</MaintainTime>
              <DispenseMode>MultiAVZDispenseMode</DispenseMode>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <DBInstanceStorageType>local_ssd</DBInstanceStorageType>
              <AccountType>Mix</AccountType>
              <MaxIOPS>5000</MaxIOPS>
<SupportUpgradeAccountType>No</SupportUpgradeAccountType>
```

云数据库RDS

```xml
              <SupportUpgradeAccountType>No</SupportUpgradeAccountType>
              <SlaveZones>
                    <SlaveZone>
                          <ZoneId>cn-hangzhou-h</ZoneId>
                    </SlaveZone>
              </SlaveZones>
              <Extra>
                    <DBInstanceIds>
            </DBInstanceIds>
              </Extra>
              <CanTempUpgrade>true</CanTempUpgrade>
              <RegionId>cn-hangzhou</RegionId>
        </DBInstanceAttribute>
  </Items>
</DescribeDBInstanceAttributeResponse>
```

`JSON` 格式

```json
{
 "RequestId": "BD3A30D8-32E7-40CF-AAEA-6BFD4E3DC55E",
 "Items": {
  "DBInstanceAttribute": [
   {
    "DBInstanceMemory": 8192,
    "ResourceGroupId": "rg-acfmyxxxxxxxxxx",
    "Port": "3306",
    "MasterZone": "cn-hangzhou-h",
    "LatestKernelVersion": "rds_20201031",
    "DBInstanceType": "Primary",
    "ConsoleVersion": "2",
    "InstanceNetworkType": "VPC",
    "DBInstanceClassType": "x",
    "DBInstanceId": "rm-uf6wjk5xxxxxxxxxx",
    "AutoUpgradeMinorVersion": "Auto",
    "DBInstanceStorage": 150,
    "AvailabilityValue": "100.0%",
    "Engine": "MySQL",
    "DBInstanceDescription": "test1",
    "IPType": "IPv4",
    "EngineVersion": "8.0",
    "DBInstanceStatus": "Running",
    "MaxConnections": 2000,
    "DBInstanceClass": "rds.mysql.s3.large",
    "AccountMaxQuantity": 99999,
    "VSwitchId": "vsw-xxxxxx",
    "PayType": "Prepaid",
    "LockMode": "Unlock",
    "GuardDBInstanceId": "rm-uf64zsuxxxxxxxxxx",
    "SupportCreateSuperAccount": "No",
    "InsId": 1,
    "VpcId": "vpc-xxxxxxxxx",
    "CurrentKernelVersion": "rds_20200831",
    "TempUpgradeTimeStart": "2021-01-10 00:00:00",
    "TempUpgradeTimeEnd": "2021-06-18 00:00:00",
```

云数据库RDS

```json
    "CreationTime": "2020-06-17T09:03:57Z",
    "ConnectionMode": "Standard",
    "VpcCloudInstanceId": "vpc-23rsxdfxxxxxxx",
    "ProxyType": 2,
    "ConnectionString": "rm-uf6wjk5xxxxxxxxxx.mysql.rds.aliyuncs.com",
    "ExpireTime": "2021-06-17T16:00:00Z",
    "DBMaxQuantity": 99999,
    "Category": "HighAvailability",
    "DBInstanceNetType": "Intranet",
    "SuperPermissionMode": "",
    "DedicatedHostGroupId": "",
    "DBInstanceCPU": "4",
    "GuardDBInstanceName": "rm-m5xxxxx",
    "SecurityIPList": "42.xx.xx.xx",
    "OriginConfiguration": "",
    "ReadOnlyDBInstanceIds": {
     "ReadOnlyDBInstanceId": []
    },
    "SecurityIPMode": "normal",
    "MaintainTime": "23:00Z-00:00Z",
    "DispenseMode": "MultiAVZDispenseMode",
    "ZoneId": "cn-hangzhou-h",
    "DBInstanceStorageType": "local_ssd",
    "AccountType": "Mix",
    "MaxIOPS": 5000,
    "SupportUpgradeAccountType": "No",
    "SlaveZones": {
     "SlaveZone": [
      {
       "ZoneId": "cn-hangzhou-h"
      }
```

]

```json
    },
    "Extra": {
     "DBInstanceIds": {
      "DBInstanceId": []
     }
    },
    "CanTempUpgrade": true,
    "RegionId": "cn-hangzhou"
   }
```

]

```
 }
}
```

#### 查询实例列表

调用DescribeDBInstances接口查询RDS实例列表。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nces | 系统规定参数，取值：DescribeDBInstances。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| proxyId | String | 否 | API | 代理模式ID。 |
| Engine | String | 否 | MySQL | 数据库类型，取值： MySQL SQLServer PostgreSQL PolarDB 默认返回所有数据库类型。 |
| ZoneId | String | 否 | cn-hangzhou-a | 可用区ID。 |
| ResourceGroupI d | String | 否 | rg-acfmyxxxxx | 资源组ID。 |
| DBInstanceStatu s | String | 否 | Running | 实例状态，详情请参见本手册的实例状态表。 |
| Expired | String | 否 | True | 实例的过期状态，取值： True：已过期 False：未过期 |
| SearchKey | String | 否 | rm-uf6w | 可基于实例ID或者实例备注模糊搜索。 |
| DBInstanceId | String | 否 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

云数据库RDS

| DBInstanceType | String | 否 | Primary | 实例类型，取值： Primary：主实例 Readonly：只读实例 Guard：灾备实例 Temp：临时实例默认返回所有实例类型。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 30 | 每页记录数，取值：1~100。 默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |
| InstanceNetwork Type | String | 否 | Classic | 实例的网络类型，取值： VPC：专有网络下的实例 Classic：经典网络下的实例默认返回所有网络类型下的实例。 |
| VpcId | String | 否 | vpc- uf6f7l4fg90xxxx xxxxxx | VPC ID。 |
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xxxxxxx | 交换机ID。 |
| DBInstanceClass | String | 否 | rds.mys2.small | 实例规格，详情请参见云数据库RDS > 产品简介中的实例规格表。 |
| EngineVersion | String | 否 | 5.7 | 数据库版本。 |
| PayType | String | 否 | Postpaid | 付费类型，取值： Postpaid：按量付费 Prepaid：包年包月 |
| ConnectionMode | String | 否 | Standard | 实例的访问模式，取值： Standard：标准访问模式 Safe：数据库代理模式默认返回所有访问模式下的实例。 |

云数据库RDS

| Tag.1.key | String | 否 | testkey1 | 第一个标签键。 |
|---|---|---|---|---|
| Tag.2.key | String | 否 | testkey2 | 第二个标签键。 |
| Tag.3.key | String | 否 | testkey3 | 第三个标签键。 |
| Tag.4.key | String | 否 | testkey4 | 第四个标签键。 |
| Tag.5.key | String | 否 | testkey5 | 第五个标签键。 |
| Tag.1.value | String | 否 | testvalue1 | 第一个标签键对应的标签值。 |
| Tag.2.value | String | 否 | testvalue2 | 第二个标签键对应的标签值。 |
| Tag.3.value | String | 否 | testvalue3 | 第三个标签键对应的标签值。 |
| Tag.4.value | String | 否 | testvalue4 | 第四个标签键对应的标签值。 |
| Tag.5.value | String | 否 | testvalue5 | 第五个标签键对应的标签值。 |
| Tags | String | 否 | {"key1":"value1 "} | 查询绑定有该标签的实例，包括TagKey和 TagValue。单次最多支持传入5组值，格式： {"key1":"value1","key2":"value2"...} 。 |
| DedicatedHostG roupId | String | 否 | dhg- 7a9xxxxxxxx | 专属集群ID。 |
| DedicatedHostId | String | 否 | i-bpxxxxxxx | 专属集群内的主机ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageRecordCo unt | Integer | 10 | 当前页实例个数。 |
| TotalRecordCo unt | Integer | 100 | 总记录数。 |

云数据库RDS

| PageNumber | Integer | 1 | 页码。 |
|---|---|---|---|
| Items | Array of DBInstance |  | 由实例信息组成的数组。 |
| DBInstance |  |  |  |
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | 实例ID。 |
| DBInstanceDe scription | String | 测试数据库 | 实例描述。 |
| PayType | String | Postpaid | 实例的付费类型，取值Postpaid（按量付费）。 |
| DBInstanceTy pe | String | Primary | 实例类型，取值： Primary：主实例 ReadOnly：只读实例 Guard：灾备实例 Temp：临时实例 |
| InstanceNetwo rkType | String | Classic | 实例的网络类型，取值： Classic：经典网络 VPC：VPC网络 |
| ConnectionMo de | String | Performance | 实例的访问模式，取值： Standard：标准访问模式 Safe：数据库代理模式 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| ExpireTime | String | 2019-02- 27T16:00:00Z | 到期时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明按量付费实例无到期时间。 |
| DBInstanceSta tus | String | Running | 实例状态，详情请参见本手册的实例状态表。 |

云数据库RDS

| Engine | String | MySQL | 数据库类型。 |
|---|---|---|---|
| DBInstanceNet Type | String | Internet | 实例的网络连接类型，取值： Internet：外网连接 Intranet：内网连接 |
| LockMode | String | Unlock | 实例的锁定状态。取值： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前自动锁定。 LockByDiskQuota：实例空间满自动锁定。 Released：实例已释放。此时实例无法进行解锁，只能使用备份数据重新创建新实例，重建时间较长，请耐心等待。 |
| LockReason | String | instance expired _ | 实例被锁定的原因。 |
| MasterInstanc eId | String | rm- uf6wjk5xxxxxxxxxx | 主实例的ID，如果没有返回此参数（即为null） 则表示该实例是主实例。 |
| GuardDBInsta nceId | String | rm- uf64zsuxxxxxxxxxx | 主实例如果有灾备实例，该参数即为灾备实例的 ID。 |
| TempDBInstan ceId | String | rm- uf64zsuxxxxxxxxxx | 主实例如果有临时实例，该参数即为临时实例的 ID。 |
| Category | String | Basic | 实例系列： Basic：基础版 HighAvailability：高可用版 Finance：三节点企业版 |
| CreateTime | String | 2018-11- 05T11:26:02Z | 创建时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DBInstanceCla ss | String | rds.mys2.small | 实例规格，详见云数据库RDS > 产品简介中的实例规格表。 |
| DBInstanceSto rageType | String | ModuleList.4.Modul eCode | 实例储存类型。 |

云数据库RDS

| DestroyTime | String | 2018-11- 05T11:26:02Z | 销毁时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| DispenseMode | String | 无 | 实例的部署模式。 |
| EngineVersion | String | 5.7 | 数据库版本。 |
| InsId | Integer | 0 | 无效参数。 |
| MasterZone | String | 无 | 无效参数。 |
| MutriORsignle | Boolean | true | 是否是多可用区，取值：true \| false |
| ReadOnlyDBIn stanceIds | Array of ReadOnlyDBIn stanceId |  | 主实例下如果有只读实例，该参数为只读实例的 ID列表。 |
| ReadOnlyDBIn stanceId |  |  |  |
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | 只读实例ID。 |
| ReplicateId | String | 无 | 无效参数。 |
| ResourceGrou pId | String | rg-acfmyxxxxxxx | 资源组ID。 |
| SlaveZones | Array of SlaveZone |  | 备实例可用区列表。 |
| SlaveZone |  |  |  |
| ZoneId | String | cn-hangzhou-h | 备实例所在可用区的可用区ID。 |
| VSwitchId | String | vsw- uf6adz52c2pxxxxx xx | 交换机ID。 |
| VpcCloudInsta nceId | String | rm-uf6wjk5xxxxxxx | 专有网络实例ID。 |

云数据库RDS

| VpcId | String | vpc- uf6f7l4fg90xxxxxx x | VPC ID。 |
|---|---|---|---|
| ZoneId | String | cn-hangzhou-a | 可用区ID。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstances
                    &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBInstancesResponse>
                    <TotalRecordCount>1</TotalRecordCount>
                    <PageRecordCount>1</PageRecordCount>
                    <RequestId>B4309486-26EF-47B3-ADDE-6140B4C1109D</RequestId>
                    <PageNumber>1</PageNumber>
                    <Items>
                    <DBInstance>
                    <ResourceGroupId>rg-acxxxxx</ResourceGroupId>
                    <DBInstanceNetType>Intranet</DBInstanceNetType>
                    <DBInstanceType>Primary</DBInstanceType>
                    <MutriORsignle>false</MutriORsignle>
                    <InstanceNetworkType>VPC</InstanceNetworkType>
                    <DBInstanceId>rm-bpxxxxx</DBInstanceId>
                    <ReadOnlyDBInstanceIds>
                    </ReadOnlyDBInstanceIds>
                    <LockReason></LockReason>
                    <DBInstanceDescription>test</DBInstanceDescription>
                    <Engine>MySQL</Engine>
                    <EngineVersion>8.0</EngineVersion>
                    <DBInstanceStatus>Running</DBInstanceStatus>
                    <ZoneId>cn-hangzhou-h</ZoneId>
                    <DBInstanceClass>rds.mysql.s3.large</DBInstanceClass>
                    <CreateTime>2020-06-17T09:03:57Z</CreateTime>
                    <VSwitchId>vsw-bpxxxxx</VSwitchId>
                    <PayType>Prepaid</PayType>
                    <LockMode>Unlock</LockMode>
                    <GuardDBInstanceId>rm-m5xxxxx</GuardDBInstanceId>
                    <InsId>1</InsId>
                    <VpcId>vpc-bpxxxxx</VpcId>
                    <VpcName>test-huadong</VpcName>
                    <ConnectionMode>Standard</ConnectionMode>
                    <VpcCloudInstanceId>rm-bpxxxxx-1</VpcCloudInstanceId>
                    <RegionId>cn-hangzhou</RegionId>
                    <ExpireTime>2021-06-17T16:00:00Z</ExpireTime>
                    </DBInstance>
                    </Items>
                    </DescribeDBInstancesResponse>
```

`JSON` 格式云数据库RDS

```json
{
                    "TotalRecordCount": 1,
                    "PageRecordCount": 1,
                    "RequestId": "B4309486-26EF-47B3-ADDE-6140B4C1109D",
                    "PageNumber": 1,
                    "Items": {
                    "DBInstance": [
                    {
                    "ResourceGroupId": "rg-acxxxxx",
                    "DBInstanceNetType": "Intranet",
                    "DBInstanceType": "Primary",
                    "MutriORsignle": false,
                    "InstanceNetworkType": "VPC",
                    "DBInstanceId": "rm-bpxxxxx",
                    "ReadOnlyDBInstanceIds": {
                    "ReadOnlyDBInstanceId": []
                    },
                    "LockReason": "",
                    "DBInstanceDescription": "test",
                    "Engine": "MySQL",
                    "EngineVersion": "8.0",
                    "DBInstanceStatus": "Running",
                    "ZoneId": "cn-hangzhou-h",
                    "DBInstanceClass": "rds.mysql.s3.large",
                    "CreateTime": "2020-06-17T09:03:57Z",
                    "VSwitchId": "vsw-bpxxxxx",
                    "PayType": "Prepaid",
                    "LockMode": "Unlock",
                    "GuardDBInstanceId": "rm-m5xxxxx",
                    "InsId": 1,
                    "VpcId": "vpc-bpxxxxx",
                    "VpcName": "test-huadong",
                    "ConnectionMode": "Standard",
                    "VpcCloudInstanceId": "rm-bpxxxxx-1",
                    "RegionId": "cn-hangzhou",
                    "ExpireTime": "2021-06-17T16:00:00Z"
                    }
```

]

```
                    }
                    }
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBInstanceT ype.ValueNotSuppo rt | The specified parameter"DBInstanceType" is not valid. | 操作失败，指定实例类型无效。请选择正确的实例类型。 |

云数据库RDS

#### 变更配置

调用ModifyDBInstanceSpec接口变更RDS实例的（包括常规实例和只读实例，不包括灾备实例和临时实例）的规格或存储空间。 升级调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例没有正在执行的备份任务。 请求参数中必须至少指定实例规格（DBInstanceClass）和存储空间（DBInstanceStorage）其中一个参数。 若降低磁盘空间配置，输入的磁盘空间不能小于实际使用空间大小的1.1倍。 当前只支持对常规实例和只读实例变更配置，不支持灾备实例和临时实例。

**说明**

升级数据库版本（例如从基础版升级高可用版），选择相应的实例规格即可。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eSpec | 系统规定参数，取值：ModifyDBInstanceSpec。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 待变更配置的实例ID。 |
| PayType | String | 是 | Postpaid | 实例当前的付费类型，取值固定为Postpaid（按量付费）。 |
| DBInstanceClass | String | 否 | rds.mys2.small | 目标实例规格，详情请参见云数据库RDS > 产品简介中的实例规格。您也可以调用 DescribeAvailableClasses接口查询目标地域中可用的实例规格列表。 说明本参数和DBInstanceStorage参数两者至少传入一项。 |

云数据库RDS

| DBInstanceStora ge | Integer | 否 | 20 | 目标存储空间大小，单位：GB。每5GB进行递增，详情请参见云数据库RDS > 产品简介中的实例规格。您也可以调用 DescribeAvailableClasses接口查询目标实例规格中可用的存储空间范围。 说明本参数和DBInstanceClass参数两者至少传入一项。 RDS MySQL高可用版本地盘实例支持存储空间缩容，每 5GB递减。 |
|---|---|---|---|---|
| EffectiveTime | String | 否 | MaintainTime | 生效时间，取值： Immediate：立即生效。 MaintainTime：在可运维时间段内生效。 默认值：Immediate。 |
| SourceBiz | String | 否 | 不涉及 | 弃用参数。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| Category | String | 否 | HighAvailability | 实例系列。取值： Basic：基础版 HighAvailability：高可用版 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 3C5CFDEE-F774- 4DED-89A2- 1D76EC63C575 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=rm-uf6wjk5xxxxxxx &PayType=Postpaid &DBInstanceClass=rds.mys2.small
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceSpecResponse>
  <RequestId>3C5CFDEE-F774-4DED-89A2-1D76EC63C575</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
  <OrderId>207938506080728</OrderId>
</ModifyDBInstanceSpecResponse>
```

`JSON` 格式

```json
{
 "RequestId": "3C5CFDEE-F774-4DED-89A2-1D76EC63C575",
 "DBInstanceId": "rm-uf6wjk5xxxxxxx",
 "OrderId": 207938506080728
}
```

#### 释放RDS实例

调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例已关闭读写分离。 实例类型为主实例、只读实例、灾备实例、临时实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDBInstanc e | 系统规定参数，取值：DeleteDBInstance。 |
| DBInstanceId | String | 是 | rm- uf6wjk5********* * | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz********** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

云数据库RDS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DeleteDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteDBInstanceResponse>
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
  <RegionId>ap-southeast-1</RegionId>
</DeleteDBInstanceResponse>
```

`JSON` 格式

```json
{
  "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64",
  "RegionId":"ap-southeast-1"
}
```

#### 重启实例

调用RestartDBInstance接口重启RDS实例。 如果有大量的事务需要提交或回滚，可能会延长1分钟左右。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中； 实例没有进行中的备份。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RestartDBInstan ce | 系统规定参数，取值：RestartDBInstance。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

云数据库RDS

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=RestartDBInstance &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RestartDBInstanceResponse>
   <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</RestartDBInstanceResponse>
```

`JSON` 格式

```json
{
    "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 查询地域信息

调用DescribeRegions接口查询所有RDS地域的详情。 调用创建实例接口CreateDBInstance之前，可以先用本接口查询RegionId和ZoneId。

**说明**

多可用区包含MAZ字样，例如cn-hangzhou-MAZ6(b,f)、cn-hangzhou-MAZ5(b,e,f)。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 系统规定参数，取值：DescribeRegions。 |

云数据库RDS

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of RDSRegion |  | 可选的地域和可用区列表。 |
| RDSRegion |  |  |  |
| RegionId | String | cn-hangzhou | 地域ID。 |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
https://rds.example.com/?Action=DescribeRegions
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeRegionsResponse>
  <RequestId>1CE1DC20-7EFC-464F-9583-0AB8915C5697</RequestId>
  <Regions>
        <RDSRegion>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
        <RDSRegion>
              <ZoneId>cn-hangzhou-MAZ8(f,g)</ZoneId>
              <RegionId>cn-hangzhou</RegionId>
              <LocalName>China (Hangzhou)</LocalName>
              <RegionEndpoint>rds.aliyuncs.com</RegionEndpoint>
        </RDSRegion>
  </Regions>
</DescribeRegionsResponse>
```

`JSON` 格式

```json
{
  "RequestId": "1CE1DC20-7EFC-464F-9583-0AB8915C5697",
  "Regions": {
    "RDSRegion": [
      {
        "ZoneId": "cn-hangzhou-h",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      },
      {
        "ZoneId": "cn-hangzhou-MAZ10(h,i)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      },
      {
        "ZoneId": "cn-hangzhou-MAZ8(f,g)",
        "RegionId": "cn-hangzhou",
        "LocalName": "China (Hangzhou)",
        "RegionEndpoint": "rds.aliyuncs.com"
      }
```

]

```
  }
}
```

云数据库RDS

#### 迁移可用区

调用MigrateToOtherZone接口将RDS实例迁移至其他可用区。 例如，实例目前位于华东1（杭州）的cn-hangzhou-a可用区，调用此接口可以将该实例迁移至杭州的cnhangzhou-b可用区。 仅支持迁移到同一地域的其它可用区，不支持迁移到其它地域的可用区，如华东1（杭州）

**说明**

可用区内的实例不支持迁移至华北1（青岛）的可用区。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | MigrateToOther Zone | 系统规定参数，取值：MigrateToOtherZone。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |
| ZoneId | String | 是 | cn-hangzhou-b | 目标可用区ID，可以通过 DescribeRegions接口查看。 |
| EffectiveTime | String | 否 | Immediate | 生效时间，取值： Immediate：立即生效。 MaintainTime：在可运维时间段内生效。 默认值：Immediate。 |
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xxxx | 交换机ID。 说明专有网络实例迁移可用区时必须传入该参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=MigrateToOtherZone &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &ZoneId=cn-hangzhou-b
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<MigrateToOtherZoneResponse>
   <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</MigrateToOtherZoneResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectDBInstanc eLockMode.ValueN otSupported | The Current DB instance lock mode does not support this operation. | 操作失败，当前数据库实例锁模式不支持此操作。 |
| 403 | OperationDenied.O utofUsage | The resource is out of usage. | 当前集群的资源不足，请选择其它可用区。 |
| 404 | InvalidVPCId.NotFo und | Specified virtual vpc is not found. | 参数VPC ID不存在，请检查该参数的正确性。 |

#### 修改实例名称

调用ModifyDBInstanceDescription接口修改RDS实例的名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eDescription | 系统规定参数，取值为ModifyDBInstanceDescription。 |
| DBInstanceDesc ription | String | 是 | 阿里云测试环境实例 | RDS实例名称。 说明长度为2-64个字符。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceDescription
```

`&DBInstanceDescription=`阿里云测试环境实例

```
&DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceDescriptionResponse>
           <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyDBInstanceDescriptionResponse>
```

`JSON` 格式

```json
{
    "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### 修改可维护时间段

调用ModifyDBInstanceMaintainTime接口修改RDS实例可维护时间段。 实例可维护时间段一般设置为业务的低峰时间段。阿里云会在您设置的可维护时间段内进行实例维护，保证对业务的影响降到最低。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eMaintainTime | 系统规定参数，取值：ModifyDBInstanceMaintainTi me。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| MaintainTime | String | 是 | 22:00Z-02:00Z | 实例的可维护时间段。格式：HH:mmZ-HH:mmZ（UTC时间）。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMaintainTime &DBInstanceId=rm-uf6wjk5xxxxxxx &MaintainTime=22:00Z-02:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceMaintainTimeResponse>
           <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceMaintainTimeResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 查询RDS支持的字符集

调用DescribeCharacterSetName接口查询RDS实例支持的字符集。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeCharact erSetName | 系统规定参数。取值：DescribeCharacterSetName。 |
| Engine | String | 是 | mysql | 数据库引擎类型。取值： mysql：MySQL mssql：SQL Server PostgreSQL：PostgreSQL MariaDB：MariaDB |
| RegionId | String | 是 | cn-hangzhou | RDS实例所在的地域ID。您可以通过 DescribeRegions查看。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CharacterSetN ameItems | List | ["gbk","utf8","euckr ","ascii"] | 支持的字符集列表。 |
| Engine | String | mysql | 数据库引擎类型。 |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |

**示例**

请求示例

```
http(s)://example/?Action=DescribeCharacterSetName &Engine=mysql &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId> <CharacterSetNameItems>
    <CharacterSetName>["gbk","utf8","euckr","ascii"]</CharacterSetName>
</CharacterSetNameItems> <Engine>mysql</Engine>
```

`JSON` 格式

```json
{
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC",
    "CharacterSetNameItems": {
        "CharacterSetName": "[\"gbk\",\"utf8\",\"euckr\",\"ascii\"]"
    },
    "Engine": "mysql"
}
```

#### 查询底层ECS实例

调用DescribeDBInstanceIpHostname接口查询RDS实例的底层ECS实例的hostname。 RDS实例是基于ECS实例搭建的，本接口用于设置分布式事务白名单时查询RDS实例的底层ECS实例的 hostname。 仅适用于RDS SQL Server高可用系列（2012标准版、2012企业版、2014标准版、2016标准版、2016 企业版、2017标准版）。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceIpHostname | 系统规定参数，取值：DescribeDBInstanceIpHostna me。 |
| DBInstanceId | String | 是 | rm- uf6wjk5****** | RDS实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5****** | 实例ID。 |
| IpHostnameInf os | String | 172.16.xx.xx,sdxxx xxxxxB;172.16.xx.x x,sdxxxxxxxxA | RDS实例所在ECS实例的内网IP和ECS主机名， 包含主备实例。格式： ip1,hostname1;ip2,hostname2。 |
| RequestId | String | 67CD4719-51E3- 4A76-A38C- 02F45FAE7E36 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIpHostname &DBInstanceId=rm-uf6wjk5******
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceIpHostnameResponse>
  <IpHostnameInfos>172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xxx,sdxxxxxxxxA</IpHostnameInfos>
   <DBInstanceId>rm-uf6wjk5******</DBInstanceId>
   <RequestId>67CD4719-51E3-4A76-A38C-02F45FAE7E36</RequestId>
</DescribeDBInstanceIpHostnameResponse>
```

`JSON` 格式

```json
{
 "IpHostnameInfos": "172.16.xx.xx,sdxxxxxxxxB;172.16.xx.xx,sdxxxxxxxxA",
 "DBInstanceId": "rm-uf6wjk5******",
 "RequestId": "67CD4719-51E3-4A76-A38C-02F45FAE7E36"
}
```

云数据库RDS

#### 修改实例资源组

调用ModifyResourceGroup接口将RDS实例移动到指定资源组。 通过资源管理服务，您可以按照业务需要搭建合适的资源组织关系，使用目录、资源夹、账号以及资源组， 分层次地组织和管理您的云资源。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyResource Group | 系统规定参数，取值：ModifyResourceGroup。 |
| DBInstanceId | String | 是 | rm-bpxxxxx | 实例ID。 |
| ResourceGroupI d | String | 是 | rg-acxxxxx | 资源组ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyResourceGroup &DBInstanceId=rm-bpxxxxx &ResourceGroupId=rg-acxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyResourceGroupResponse>
  <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyResourceGroupResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestId": "65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ResourceGroupId.In Valid | The Specified resource group id is not found. | 资源组ID不存在。请检查ID是否正确。 |

### 只读实例

#### 创建只读实例

调用CreateReadOnlyDBInstance接口为某个实例创建一个只读实例。 主实例（非专属集群）的版本必须为以下其中一种： MySQL 8.0高可用版 MySQL 5.7高可用版 MySQL 5.6 SQL Server 2017集群版 PostgreSQL 10（本地SSD盘）、11、12高可用版对于MySQL实例： 如果主实例内存≥64GB，最多允许创建10个只读实例。 如果主实例内存＜64GB，最多允许创建5个只读实例。 对于SQL Server实例，最多允许创建7个只读实例。 对于PostgreSQL实例，本地盘主实例最多允许创建5个只读实例，云盘主实例最多允许创建32个只读实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateReadOnly DBInstance | 系统规定参数，取值：CreateReadOnlyDBInstance。 |
| DBInstanceClass | String | 是 | rds.mys2.small | 实例规格。更多信息，请参见云数据库 RDS > 产品简介中的实例规格表。建议只读实例规格不小于主实例规格，否则易导致只读实例延迟高、负载高等现象。 |

云数据库RDS

| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 主实例ID。可调用DescribeDBInstances 获取。 |
|---|---|---|---|---|
| DBInstanceStora ge | Integer | 是 | 20 | 存储空间，取值：5-3000，每5GB进行递增，单位：GB。 说明不同版本实例，支持的取值范围不同，请以控制台创建只读实例页面为准。 |
| EngineVersion | String | 是 | 5.6 | 数据库版本号。必须与主实例相同。 MySQL数据库取值：5.6、5.7、8.0。 SQL Server数据库取值：2017 ent、2019 ent。 _ _ PostgreSQL数据库取值：10.0、11.0、12.0。 |
| PayType | String | 是 | Postpaid | 付费类型，取值固定为Postpaid（按量付费）。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID。只读实例的地域必须和主实例相同。可以通过接口DescribeRegions查看地域列表。 |
| ZoneId | String | 是 | cn-hangzhou-b | 可用区ID。可以通过接口 DescribeRegions查看可用区列表。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| DBInstanceStora geType | String | 否 | local ssd _ | 实例储存类型，取值： local ssd：本地SSD盘 _ cloud ssd：SSD云盘 _ 说明 MySQL仅支持本地盘存储类型，SQL Server仅支持云盘存储类型。 |

云数据库RDS

| DBInstanceDesc ription | String | 否 | 测试只读实例 | 实例描述，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（ ）、短横线（-）。 _ 说明不能以 http:// 和 https:// 开头。 |
|---|---|---|---|---|
| InstanceNetwork Type | String | 否 | Classic | 只读实例的网络类型，取值： VPC：专有网络 Classic：经典网络默认创建专有网络实例，需要传入VPCId和VSwitchId。 说明只读实例的网络类型可以和主实例不同。 |
| VPCId | String | 否 | vpc- uf6f7l4fg90xxxx xxxxxx | 只读实例的专有网络VPC ID。 当InstanceNetworkType配置为空或VPC时需要传入。 说明主实例的存储类型为本地 SSD盘时，只读实例可以选择任意VPC网络。 主实例的存储类型为云盘时，只读实例VPC必须和主实例保持一致。 |
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xxxxxxx | 只读实例的虚拟交换机ID。 当InstanceNetworkType配置为空或VPC时需要传入。 |
| PrivateIpAddress | String | 否 | 172.16.201.69 | 设置只读实例的内网IP，需要在指定交换机的IP地址范围内。系统默认通过VPCId和VSwitchId自动分配。 |
| ResourceGroupI d | String | 否 | rg- acfmyxxxxxxxxx x | 资源组ID。 |

云数据库RDS

| Category | String | 否 | HighAvailability | 实例系列，取值： Basic：基础版 HighAvailability：高可用版（默认值） 说明 PostgreSQL云盘实例的只读实例为基础版，因此必须传入Basic。 |
|---|---|---|---|---|
| DedicatedHostG roupId | String | 否 | 无 | 废弃参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rr-uf6wjk5xxxxxxx | 创建的只读实例ID。 |
| OrderId | String | 10078937xxxxx | 订单ID。 |
| ConnectionStri ng | String | rr- xxxxx.mysql.rds.ali yuncs.com | 创建的只读实例内网数据库连接地址。 |
| Port | String | 3306 | 创建的只读实例内网数据库连接端口。 |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateReadOnlyDBInstance &RegionId=cn-hangzhou &ZoneId=cn-hangzhou-b &DBInstanceId=rm-uf6wjk5xxxxxxx &DBInstanceClass=rds.mys2.small &DBInstanceStorage=20 &EngineVersion=5.6 &PayType=Postpaid &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<CreateReadOnlyDBInstanceResponse>
      <OrderId>10078937xxxxx</OrderId>
      <ConnectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</ConnectionString>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <Port>3306</Port>
      <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CreateReadOnlyDBInstanceResponse>
```

`JSON` 格式

```json
{
    "CreateReadOnlyDBInstanceResponse": {
        "OrderId": "10078937xxxxx",
        "ConnectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "Port": 3306,
        "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidEngineVersio n.Malformed | The specified parameter "EngineVersion" is not valid. | 无效的引擎版本参数。 |
| 400 | InvalidSecurityIPLis t.Malformed | The specified parameter "SecurityIPList" is not valid. | 目标实例的IP白名单配置无效。 |
| 400 | InvalidSecurityIPLis t.Duplicate | The Security IP address is not in the available range or occupied. | 当前的安全IP地址已被占用或不在有效区间内，请重新设置安全IP地址。 |
| 400 | InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 实例ID（DBInstanceId）无效， 请检查该参数的正确性。 |
| 403 | OperationDenied.Pr imaryDBInstanceSt atus | The operation is not permitted due to status of primary instance. | 操作失败，无法迁移专属集群内非运行状态的RDS实例。 |
| 400 | OperationDenied | VPC IP is in use, please check. | 操作失败，当前VPC IP已经被使用。 |

云数据库RDS

| 404 | IncorrectDBInstanc eConnType | Current DB instance conn type does not support this operation. | 当前数据库实例的连接类型不支持此操作。 |
|---|---|---|---|
| 400 | InvalidZoneId.NotS upported | The Specified vpc Zone not supported. | 当前可用区不支持创建VPC网络类型实例，请更换可用区。 |

#### 查询只读实例延迟信息

调用DescribeReadDBInstanceDelay接口查询RDS只读实例的延迟信息。 调用该接口时，实例必须满足以下条件： 实例为MySQL、PostgreSQL、PolarDB。 实例已有只读实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeReadDB InstanceDelay | 系统规定参数。取值：DescribeReadDBInstanceDela y。 |
| DBInstanceId | String | 是 | rm-bpxxxxxxx | 主实例ID。 |
| ReadInstanceId | String | 是 | rr-bpxxxxxxx | 只读实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-bpxxxxxxx | 主实例ID。 |
| DelayTime | Integer | 0 | 延迟时间。 |
| Items | Array of Items |  | 延迟信息列表。 |
| Items |  |  |  |
| DBInstanceId | String | rm-bpxxxxxxx | 主实例ID。 |
| ReadDBInstan ceNames | List | "ReadDBInstanceN ame": ["rr- bpxxxxx"] | 只读实例的信息列表。 说明仅MySQL返回此参数。 |

云数据库RDS

| ReadDelayTim es | List | "ReadDelayTime": ["0"] | 延迟时间列表。 说明仅MySQL返回此参数。 |
|---|---|---|---|
| ReadonlyInsta nceDelay | Array of ReadonlyInsta nceDelay |  | 预写式日志（WAL）延迟信息列表。 说明仅PostgreSQL和PPAS返回此参数。 |
| ReadonlyInsta nceDelay |  |  |  |
| FlushLag | String | 0 | 预写式日志（WAL）持久化延迟时间。单位： 秒。 |
| FlushLatency | String | 0 | 预写式日志（WAL）持久化延迟空间。单位： MB。 |
| ReadDBInstan ceName | String | rr-bpxxxxxxx | 只读实例ID。 |
| ReplayLag | String | 0 | 预写式日志（WAL）回放延迟时间。单位：秒。 |
| ReplayLatency | String | 0 | 预写式日志（WAL）回放延迟空间。单位： MB。 |
| SendLatency | String | 0 | 预写式日志（WAL）发送延迟空间。单位： MB。 |
| WriteLag | String | 0 | 预写式日志（WAL）回写延迟时间。单位：秒。 |
| WriteLatency | String | 0 | 预写式日志（WAL）回写延迟空间。单位： MB。 |
| ReadDBInstan ceId | String | rr-bpxxxxxxx | 只读实例ID。 |
| RequestId | String | F1BDDEA8-452D- 450B-AB10- CD5C5BAFC5DF | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=DescribeReadDBInstanceDelay &RegionId=cn-hangzhou &DBInstanceId=rm-bpxxxxxxx &ReadInstanceId=rr-bpxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeReadDBInstanceDelayResponse>
  <RequestId>11152741-D854-4E18-920E-64E75D484D57</RequestId>
  <DBInstanceId>rm-bpxxxxx</DBInstanceId>
  <Items>
        <Items>
              <ReadDBInstanceNames>
                    <ReadDBInstanceName>rr-bpxxxxx</ReadDBInstanceName>
              </ReadDBInstanceNames>
              <ReadDelayTimes>
                    <ReadDelayTime>0</ReadDelayTime>
              </ReadDelayTimes>
              <DBInstanceId>rm-bpxxxxx</DBInstanceId>
              <ReadonlyInstanceDelay>
        </ReadonlyInstanceDelay>
        </Items>
  </Items>
  <DelayTime>0</DelayTime>
</DescribeReadDBInstanceDelayResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "RequestId": "11152741-D854-4E18-920E-64E75D484D57",
 "DBInstanceId": "rm-bpxxxxx",
 "Items": {
  "Items": [
   {
    "ReadDBInstanceNames": {
     "ReadDBInstanceName": [
      "rr-bpxxxxx"
```

]

```json
    },
    "ReadDelayTimes": {
     "ReadDelayTime": [
      "0"
```

]

```json
    },
    "DBInstanceId": "rm-bpxxxxx",
    "ReadonlyInstanceDelay": {
     "ReadonlyInstanceDelay": []
    }
   }
```

]

```json
 },
 "DelayTime": "0"
}
```

### 版本升级

#### 修改小版本升级方式

调用ModifyDBInstanceAutoUpgradeMinorVersion接口修改RDS实例升级小版本的方式。 仅支持MySQL实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eAutoUpgradeMi norVersion | 系统规定参数，取值：ModifyDBInstanceAutoUpgra deMinorVersion。 |
| AutoUpgradeMin orVersion | String | 是 | Auto | 实例升级小版本的方式，取值： Auto：自动升级小版本。 Manual：不自动升级，仅在当前版本下线时才强制升级。 |
| DBInstanceId | String | 是 | rm-uf6wjk5xxx | 实例ID。 |

云数据库RDS

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A31818D5-0550- 4A81-8D13- B45948D7193F | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceAutoUpgradeMinorVersion &DBInstanceId=rm-uf6wjk5xxx &AutoUpgradeMinorVersion=Auto
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceAutoUpgradeMinorVersionResponse>
    <RequestId>A31818D5-0550-4A81-8D13-B45948D7193F</RequestId>
</ModifyDBInstanceAutoUpgradeMinorVersionResponse>
```

`JSON` 格式

```json
{
 "RequestId": "A31818D5-0550-4A81-8D13-B45948D7193F"
}
```

#### 升级内核小版本

调用UpgradeDBInstanceKernelVersion接口升级RDS实例的内核小版本。 核小版本的升级涉及性能提升、新功能或问题修复等。更多信息，请参见MySQL升级内核小版本、SQL 该接口当前仅支持RDS MySQL、RDS SQL Server、RDS PostgreSQL实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | UpgradeDBInsta nceKernelVersio n | 系统规定参数，取值：UpgradeDBInstanceKernelVer sion。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm-bpxxxxx | 实例ID。仅支持RDS MySQL、RDS SQL Server和RDS PostgreSQL实例。 说明 PostgreSQL实例的存储类型必须为云盘。本地盘实例可以通过RestartDBInstance 接口重启，以自动升级到最新的小版本。 SQL Server实例仅2019版本支持小版本升级。 |
| SwitchTime | String | 否 | 2020-01- 15T00:00:00Z | 指定时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明 UpgradeTime= SpecifyTime时传入此参数有效。 |
| SwitchTimeMode | String | 否 | Immediately | 升级小版本的执行时间，取值： Immediately：默认值，立即执行。 MaintainTime：实例可运维时间段内执行。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceNa me | String | rm-bpxxxxx | 实例ID。 |
| RequestId | String | DA2ECBA0-4745- 4491-9166- 799FF8984AC9 | 请求ID。 |
| TargetMinorVe rsion | String | xcluster80 202103 _ 05 | 升级的目标内核小版本。 |
| TaskId | String | 226917711 | 任务ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=UpgradeDBInstanceKernelVersion &DBInstanceId=rm-bpxxxxx &UpgradeTime=SpecifyTime &SwitchTime=2020-01-15T00:00:00Z &TargetMinorVersion=xcluster80_20210305
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UpgradeDBInstanceKernelVersion>
      <TaskId>226917711</TaskId>
      <RequestId>DA2ECBA0-4745-4491-9166-799FF8984AC9</RequestId>
      <TargetMinorVersion>xcluster80_20210305</TargetMinorVersion>
      <DBInstanceName>rm-bpxxxxx</DBInstanceName>
</UpgradeDBInstanceKernelVersion>
```

`JSON` 格式

```json
{
 "TaskId": "226917711",
 "RequestId": "DA2ECBA0-4745-4491-9166-799FF8984AC9",
 "TargetMinorVersion": "xcluster80_20210305",
 "DBInstanceName": "rm-bpxxxxx"
}
```

### 网络与连接地址

#### 申请外网地址

调用AllocateInstancePublicConnection接口申请实例的外网地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AllocateInstance PublicConnectio n | 系统规定参数，取值：AllocateInstancePublicConnec tion。 |
| ConnectionStrin gPrefix | String | 是 | test1234 | 外网连接地址的前缀。完整外网连接地址为：前缀.引擎名.rds.aliyuncs.com。例如test1234.mysql.rds.aliyuncs.com。 说明长度5~40，不能包含汉字和非法字符（~!#%^&*=+\| {};:'",<>/?），建议由字母、数字、短横线（-）组成。 |

云数据库RDS

| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
|---|---|---|---|---|
| Port | String | 是 | 3306 | 外网连接端口，取值：1000-5999。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=AllocateInstancePublicConnection &ConnectionStringPrefix=test1234 &DBInstanceId=rm-uf6wjk5xxxxxxx &Port=3306
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<AllocateInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</AllocateInstancePublicConnectionResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 释放外网地址

调用ReleaseInstancePublicConnection接口释放实例的外网连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ReleaseInstance PublicConnectio n | 系统规定参数，取值：ReleaseInstancePublicConnec tion。 |

云数据库RDS

| CurrentConnecti onString | String | 是 | rm- uf6wjk5xxxx.my sql.rds.aliyuncs. com | 外网连接地址。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ReleaseInstancePublicConnection &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ReleaseInstancePublicConnectionResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ReleaseInstancePublicConnectionResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 切换内外网地址

为了节约地址资源，您可以使用该接口进行内外网切换，即原来是内网，则会切换到外网，反之亦然。切换后连接地址会发生变化，需要您修改代码中的连接地址并重启应用。 必须满足以下条件，否则将修改失败： 实例只有内网地址和外网地址其中一个。 实例状态为运行中。 24小时内切换次数低于20次。 实例的网络类型为经典网络。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SwitchDBInstanc eNetType | 系统规定参数，取值：SwitchDBInstanceNetType。 |
| ConnectionStrin gPrefix | String | 是 | test1234 | 自定义连接地址的前辍。由字母，数字组成，小写字母开头，8~64个字符。完整连接地址为：前缀.引擎名.rds.aliyuncs.com。例如 test1234.mysql.rds.aliyuncs.com。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| Port | String | 否 | 3306 | 端口号，取值：3001~3999。 |
| ConnectionStrin gType | String | 否 | Normal | 连接地址类型，取值： Normal：普通连接 ReadWriteSplitting：读写分离连接默认返回所有连接。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=SwitchDBInstanceNetType &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionStringPrefix=rm-xxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<SwitchDBInstanceNetTypeResponse>
   <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</SwitchDBInstanceNetTypeResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 查询连接地址

调用DescribeDBInstanceNetInfo接口查询实例的所有连接地址信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceNetInfo | 系统规定参数，取值：DescribeDBInstanceNetInfo。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| Flag | String | 否 | 不涉及 | 备用参数。 |
| DBInstanceNetR WSplitType | String | 否 | Normal | 连接地址类型，取值： Normal：普通连接地址 ReadWriteSplitting：读写分离连接地址说明默认返回所有类型连接地址。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceNet Infos | Array of DBInstanceNet Info |  | 实例的连接地址信息列表。 |
| DBInstanceNet Info |  |  |  |

云数据库RDS

| ConnectionStri ng | String | rm- uf6wxxxxx.mysql.r ds.aliyuncs.com | 连接地址。 |
|---|---|---|---|
| IPAddress | String | 192.168.12.84 | IP地址。 |
| IPType | String | Public | 网络类型。 经典网络类型取值： Inner：内网 Public：外网 VPC类型取值： Private：内网 Public：外网 |
| Port | String | 3306 | 连接端口。 |
| VPCId | String | vpc- uf6f7l4fg90xxxxxx xxxx | VPC ID。 |
| VSwitchId | String | vsw- uf6adz52c2pxxxxx xxxxx | 交换机ID。 |
| ConnectionStri ngType | String | Normal | 连接地址类型，取值： Normal：普通连接地址 ReadWriteSplitting：读写分离连接地址 |
| MaxDelayTime | String | 12 | 延迟阈值，只在读写分离连接地址返回该参数， 单位：秒。 说明超过该延迟阈值的只读实例不会被分配流量。 |
| DistributionTy pe | String | Standard | 读请求分配策略，只在读写分离连接地址返回该参数，取值： Standard：按规格权重自动分配 Custom：自定义分配权重 |
| DBInstanceWe ights | Array of DBInstanceWe ight |  | 实例权重信息列表，开通了读写分离地址的实例会返回该参数。 |
| DBInstanceWe ight |  |  |  |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

| DBInstanceTy pe | String | Master | 实例类型，取值： Master：主实例； Readonly：只读实例。 |
|---|---|---|---|
| Weight | String | 100 | 实例当前权重。 |
| Availability | String | Unavailable | 实例可用状态，取值： Unavailable：不可用； Available：可用。 |
| ExpiredTime | String | 1209534 | 混访模式下，经典网络的剩余时间，单位：秒。 |
| SecurityIPGrou ps | Array of securityIPGrou p |  | 实例的IP白名单分组列表。 |
| securityIPGrou p |  |  |  |
| SecurityIPGrou pName | String | Default | IP白名单分组名称。 |
| SecurityIPs | String | 127.0.0.1 | 白名单IP。 |
| Upgradeable | String | Disabled | IP版本是否能够升级，取值：Enable \| Disabled 说明 IPv4版本可以升级到IPv6版本。 |
| InstanceNetwo rkType | String | VPC | 网络类型，取值： Classic：经典网络 VPC：专有网络 |
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | 请求ID。 |
| SecurityIPMod e | String | safety | 白名单模式，取值： normal：通用模式 safety：高安全模式 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=DescribeDBInstanceNetInfo &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceNetInfoResponse>
   <dBInstanceNetInfos>
      <connectionString>rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com</connectionString>
      <connectionStringType>Normal</connectionStringType>
      <iPAddress>192.168.xx.xx</iPAddress>
      <iPType>Public</iPType>
      <port>3306</port>
      <upgradeable>Disabled</upgradeable>
      <vPCId></vPCId>
   </dBInstanceNetInfos>
   <instanceNetworkType>Classic</instanceNetworkType>
   <requestId>777C4593-8053-427B-99E2-105593277CAB</requestId>
</DescribeDBInstanceNetInfoResponse>
```

`JSON` 格式

```json
{
    "dBInstanceNetInfos": [
        {
            "connectionString": "rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com",
            "connectionStringType": "Normal",
            "dBInstanceWeights": [],
            "iPAddress": "192.168.xx.xx",
            "iPType": "Public",
            "port": "3306",
            "securityIPGroups": [],
            "upgradeable": "Disabled",
            "vPCId": ""
        }
```

`],`

```json
    "instanceNetworkType": "Classic",
    "requestId": "777C4593-8053-427B-99E2-105593277CAB"
}
```

#### 修改连接地址

调用ModifyDBInstanceConnectionString接口修改实例的连接地址和端口。 目前RDS提供内外网两种连接地址，同时也支持混访模式下的专有网络和经典网络地址并存。 云数据库RDS

**说明**

不支持修改读写分离地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eConnectionStri ng | 系统规定参数，取值：ModifyDBInstanceConnection String。 |
| ConnectionStrin gPrefix | String | 是 | rm-xxxxxx | 目标连接地址的前缀，即只能修改CurrentConnectionString参数的前缀部分。 说明长度8~64，不能包含汉字和非法字符（~!#%^&*=+\\| {};:'",<>/?），建议由字母、数字、短横线（-）组成。 |
| CurrentConnecti onString | String | 是 | rm- uf6wjk5xxxxxxx. mysql.rds.aliyun cs.com | 实例当前的某个连接地址，可以是内外网地址，或者混访模式下的经典网络地址。 说明不支持修改读写分离地址。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| Port | String | 是 | 3306 | 目标端口。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceConnectionString &DBInstanceId=rm-uf6wjk5xxxxxxx &CurrentConnectionString=rm-uf6wjk5xxxxxxx.mysql.rds.aliyuncs.com &ConnectionStringPrefix=rm-xxxxxx &Port=3306
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceConnectionStringResponse>
         <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 释放实例连接地址

调用ReleaseInstanceConnection接口释放RDS实例的连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ReleaseInstance Connection | 系统规定参数。取值：ReleaseInstanceConnection。 |
| CurrentConnecti onString | String | 是 | rm- uf6wjk5xxxx.my sql.rds.aliyuncs. com | 当前的外网连接地址。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| InstanceNetwork Type | String | 是 | Classic | 实例的网络类型。取值： VPC：VPC网络 Classic：经典网络 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=ReleaseInstanceConnection &CurrentConnectionString=rm-uf6wjk5xxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ReleaseInstanceConnectionResponse>
      <RequestId>65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ReleaseInstanceConnectionResponse>
```

`JSON` 格式

```json
{
    "RequestId":"65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

#### 切换网络类型

调用ModifyDBInstanceNetworkType接口切换RDS实例网络类型。 该接口用于将实例的网络类型从专有网络切换成经典网络，或从经典网络切换成专有网络。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eNetworkType | 系统规定参数，取值：ModifyDBInstanceNetworkTy pe。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| InstanceNetwork Type | String | 是 | Classic | 目标网络类型，取值： VPC：专有网络 Classic：经典网络 |
| RetainClassic | String | 否 | True | 是否保留经典网络地址，取值： True：保留 False：不保留默认值：False。 说明从经典网络切换到专有网络时该参数有效。 |

云数据库RDS

| ClassicExpiredD ays | String | 否 | 7 | 经典网络地址保留的天数，取值1-120， 单位：天。默认值：7。 说明若传入参数RetainClassic=True，则该参数必传。 |
|---|---|---|---|---|
| ReadWriteSplitti ngClassicExpired Days | Integer | 否 | 7 | 读写分离的经典网络地址保留的天数，取值1-120，单位：天。默认值：7。 说明当实例存在经典网络类型的读写分离地址， 且RetainClassic=True，本参数有效。 |
| VPCId | String | 否 | vpc- uf6f7l4fg90xxxx xx | VPC ID。 |
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xx | 交换机ID，若传入VPCId，则该参数必传。 |
| PrivateIpAddress | String | 否 | 172.10.40.25 | 设置实例的内网IP，需要在指定交换机的 IP地址范围内。系统默认通过VPCId和VSwitchId自动分配。 |
| ReadWriteSplitti ngPrivateIpAddr ess | String | 否 | 192.168.0.22 | 设置实例的内网读写分离地址的IP，需要在指定交换机的IP地址范围内。系统默认通过VPCId和VSwitchId自动分配。 说明当前实例存在经典网络类型的读写分离地址时，该值有效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |
| TaskId | String | 1025486523574 | 任务ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkType &DBInstanceId=rm-uf6wjk5xxxxxxx &InstanceNetworkType=Classic
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceNetworkTypeResponse>
   <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</ModifyDBInstanceNetworkTypeResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NetTypeExists | Specified network type already exists. | 网络类型切换失败，当前网络类型已经存在。 |
| 403 | OperationDenied.D BInstanceConnTyp e | The current DB instance connection type does not support this operation. | 操作失败，当前的网络连接类型不支持该操作。 |

#### 切换VPC或交换机

调用SwitchDBInstanceVpc接口切换RDS实例的专有网络VPC或交换机。 实例必须是RDS MySQL或RDS PostgreSQL（云盘版）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SwitchDBInstanc eVpc | 系统规定参数。取值：SwitchDBInstanceVpc。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 说明实例必须是RDS MySQL或 RDSPostgreSQL（云盘版）。 实例必须处于运行状态。 实例的网络类型必须是专有网络。 实例不能是临时实例或共享实例。 |

云数据库RDS

| VPCId | String | 否 | vpc- uf6f7l4fg90xxxx xxxxxx | VPC ID。 说明与RDS实例需属于同一地域。 仅当RDS实例为RDS MySQL本地盘版时，才可以更换VPC。 |
|---|---|---|---|---|
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xxxxxxx | 交换机ID。 说明与RDS实例需属于同一可用区。 |
| PrivateIpAddress | String | 否 | 10.23.xx.xx | 指定实例的私有IP地址，必须在VSwitchId参数中指定的交换机的网段范围内。 说明您可以调用 DescribeVSwitches查询目标交换机的网段。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 10xxxxxxxxxx | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=SwitchDBInstanceVpc &DBInstanceId=rm-uf6wjk5xxxxxxx &VPCId=vpc-uf6f7l4fg90xxxxxxxxxx &VSwitchId=vsw-uf6adz52c2pxxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>777C4593-8053-427B-99E2-10xxxxxxxxxx </RequestId>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestId": "777C4593-8053-427B-99E2-10xxxxxxxxxx"
}
```

#### 修改地址过期时间

调用ModifyDBInstanceNetworkExpireTime接口修改连接地址过期时间。 当实例在混访模式下（同时包含VPC连接地址和经典网络连接地址），该接口用于延长保留的经典网络地址过期时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eNetworkExpire Time | 系统规定参数，取值：ModifyDBInstanceNetworkEx pireTime。 |
| ConnectionStrin g | String | 是 | rm- uf6wjk5xxxxx.m ysql.rds.aliyuncs .com | 要延期的经典网络连接地址，经典网络连接地址有两种： 经典网络内网地址经典网络读写分离地址 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClassicExpiredD ays | Integer | 否 | 7 | 经典网络连接地址保留天数，取值：1~120，单位：天。 |
| RdsClassicexpire d | String | 否 | 无 | 无效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 4C467B38-3910- 447D-87BC- AC049166F216 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceNetworkExpireTime &DBInstanceId=rm-uf6wjk5xxxxxxx &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &ClassicExpiredDays=7
```

`&<`公共请求参数> 正常返回示例云数据库RDS `XML` 格式

```xml
<ModifyDBInstanceNetworkExpireTimeResponse>
   <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    </ModifyDBInstanceNetworkExpireTimeResponse>
```

`JSON` 格式

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
}
```

### 数据库管理

#### 创建数据库

如需进行数据变更、结构设计等数据管理任务，请使用数据管理DMS。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例中的数据库数量没有超出实例最大数据库数量，可以通过接口DescribeDBInstanceAttribute查询最大数据库数量。 实例类型不能为只读实例。 该接口暂不支持PostgreSQL（本地SSD盘）和SQL Server 2017集群版，您可以通过

**说明**

SQL做CREATE DATABASE操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDatabase | 系统规定参数，取值：CreateDatabase。 |

云数据库RDS

| CharacterSetNa me | String | 是 | gbk | 字符集，取值： MySQL类型：utf8、gbk、latin1、 utf8mb4 SQL Server类型：Chinese PRC CI AS、 _ _ _ Chinese PRC CS AS、 _ _ _ SQL Latin1 General CP1 CI AS _ _ _ _ _ 、 SQL Latin1 General CP1 CS A _ _ _ _ _ S、Chinese PRC BIN _ _ PostgreSQL类型：KOI8U、UTF8、 WIN866、WIN874、WIN1250、 WIN1251、WIN1252、 WIN1253、WIN1254、 WIN1255、WIN1256、 WIN1257、WIN1258、EUC CN、 _ EUC KR、EUC TW、EUC JP、 _ _ _ EUC JIS 2004、KOI8R、 _ _ MULE INTERNAL、LATIN1、 _ LATIN2、LATIN3、LATIN4、 LATIN5、LATIN6、LATIN7、 LATIN8、LATIN9、LATIN10、 ISO 8859 5、ISO 8859 6、 _ _ _ _ ISO 8859 7、ISO 8859 8、 _ _ _ _ SQL ASCII _ |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。可调用DescribeDBInstances获取。 |
| DBName | String | 是 | rds mysql _ | 数据库名称。 说明长度为2~64个字符。 以字母开头，以字母或数字结尾。 由小写字母、数字、下划线或中划线组成。 数据库名称在实例内必须是唯一的。 其他非法字符，详见本手册中的禁用关键字表。 |
| DBDescription | String | 否 | 测试用数据库 | 数据库描述，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（ ）、短横线（-）。 _ 说明不能以 http:// 和 https:// 开头。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | 请求 ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateDatabase &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBName=rds_mysql &CharacterSetName=gbk
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateDatabaseResponse>
    <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
</CreateDatabaseResponse>
```

`JSON` 格式

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

#### 删除数据库

调用DeleteDatabase接口删除实例下的某个数据库。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例类型为主实例。 数据库类型为MySQL、SQL Server。 该接口不支持PostgreSQL类型的实例，您可以通过SQL做DROP DATABASE操作。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDatabase | 系统规定参数，取值：DeleteDatabase。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| DBName | String | 是 | testdb01 | 数据库名称。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 07F6177E-6DE4- 408A-BB4F- 0723301340F3 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DeleteDatabase &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testdb01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteDatabaseResponse>
   <RequestId>07F6177E-6DE4-408A-BB4F-0723301340F3</RequestId></DeleteDatabaseResponse>
```

`JSON` 格式

```json
{
    "RequestId":"07F6177E-6DE4-408A-BB4F-0723301340F3"
}
```

#### 查询数据库信息

调用DescribeDatabases接口查询RDS实例下的数据库信息。 如果请求参数错误，返回数据为空。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDataba ses | 系统规定参数，取值：DescribeDatabases。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| DBName | String | 否 | testDB01 | 数据库名称。 |

云数据库RDS

| DBStatus | String | 否 | Creating | 数据库状态，取值： Creating：创建中 Running：使用中 Deleting：删除中 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30 50 100 默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Databases | Array of Database |  | 数据库信息列表。 |
| Database |  |  |  |
| DBName | String | testDB01 | 数据库名称。 |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 数据库所属实例ID。 |
| Engine | String | MySQL | 数据库实例类型。 |
| DBStatus | String | Creating | 数据库状态，取值： Creating：创建中 Running：使用中 Deleting：删除中 |
| CharacterSetN ame | String | utf8 | 字符集。 |
| DBDescription | String | 测试数据库 | 数据库描述。 |
| Accounts | Array of AccountPrivile geInfo |  | 拥有数据库相关权限的账号信息。 |
| AccountPrivile geInfo |  |  |  |

云数据库RDS

| Account | String | test | 账号名称。 |
|---|---|---|---|
| AccountPrivile ge | String | DMLOnly | 账号对该数据库拥有的权限。取值： ReadWrite：读写 ReadOnly：只读 DMLOnly：仅DML DDLOnly：仅DDL |
| RequestId | String | 2603CA96-B17D- 4903-BC04- 61A2C829CD94 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDatabases &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDatabasesResponse>
   <RequestId>2603CA96-B17D-4903-BC04-61A2C829CD94</RequestId>
   <Databases>
      <Database>
         <Engine>MySQL</Engine>
         <CharacterSetName>utf8</CharacterSetName>
         <DBStatus>Creating</DBStatus>
         <DBDescription></DBDescription>
         <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
         <Accounts></Accounts>
         <DBName>testdb</DBName>
      </Database>
      <Database>
         <Engine>MySQL</Engine>
         <CharacterSetName>gbk</CharacterSetName>
         <DBStatus>Creating</DBStatus>
         <DBDescription></DBDescription>
         <DBInstanceId>rdsaiiabnaiiabn</DBInstanceId>
         <Accounts></Accounts>
         <DBName>testdb2</DBName>
      </Database>
   </Databases></DescribeDatabasesResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestId": "2603CA96-B17D-4903-BC04-61A2C829CD94",
    "Databases": {
        "Database": [
            {
                "Engine": "MySQL",
                "CharacterSetName": "utf8",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
                },
                "DBName": "testdb"
            },
            {
                "Engine": "MySQL",
                "CharacterSetName": "gbk",
                "DBStatus": "Creating",
                "DBDescription": "",
                "DBInstanceId": "rdsaiiabnaiiabn",
                "Accounts": {
                    " AccountPrivilegeInfo": []
                },
                "DBName": "testdb2"
            }
```

]

```
    }
}
```

#### 修改数据库备注

该接口不支持PostgreSQL和PolarDB实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBDescri ption | 系统规定参数，取值：ModifyDBDescription。 |
| DBDescription | String | 是 | 测试数据库A | 数据库描述。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| DBName | String | 是 | testDB01 | 数据库名称。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBDescription
```

`&DBDescription=`测试数据库A

```
&DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB01
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBDescriptionResponse>
   <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyDBDescriptionResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### 复制数据库

调用CopyDatabaseBetweenInstances接口在RDS实例间复制数据库。 该接口还适用于按时间点或备份集恢复到已有实例。 调用该接口时，实例必须满足以下条件，否则将操作失败： 源实例和目标实例同属于一个账户。 源实例和目标实例的版本相同。 源实例和目标实例在同一地域，可用区可以不同，网络类型需相同。 目标实例中没有和源实例同名的数据库。 仅适用于RDS SQL Server 2012/2016实例。您可以恢复RDS MySQL实例的某些数据库

**说明**

或表到原实例或新实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | CopyDatabaseB etweenInstances | 系统规定参数，取值为CopyDatabaseBetweenInstance s。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 源实例ID。 |
| DbNames | String | 是 | {"test1":"test2"} | 复制数据库名称列表，格式：{"源实例数据库名称":"目标实例数据库名称"}。 |
| TargetDBInstanc eId | String | 是 | rm- ut5ajk3xxxxxxx | 目标实例ID，不能与源实例ID相同。 |
| BackupId | String | 否 | 1065238746521 | 源实例备份集ID。按备份集复制数据库时，可以通过查询备份列表接口 DescribeBackups获取备份集ID。 说明 BackupId和RestoreTime传入一个即可。 |
| RestoreTime | String | 否 | 2011-06- 11T16:00:00Z | 按时间点复制数据库，可以选择备份保留周期内的任意时间点。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明 BackupId和RestoreTime传入一个即可。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | 实例ID。 |
| RequestId | String | 803D11AF-C370- 465B-AB46- CB3A642DC303 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CopyDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &TargetDBInstanceId=rm-ut5ajk3xxxxxxx &DbNames={"test1":"test2"}
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<CopyDatabaseBetweenInstancesResponse>
   <RequestId>803D11AF-C370-465B-AB46-CB3A642DC303</RequestId>
</CopyDatabaseBetweenInstancesResponse>
```

`JSON` 格式

```json
{
    "RequestId": "803D11AF-C370-465B-AB46-CB3A642DC303"
}
```

### 账号管理

#### 创建数据库账号

调用CreateAccount接口创建管理数据库的账号。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 数据库状态为运行中。 没有超出单个实例内的最大账号数量。

**说明**

该接口仅适用于MySQL、MariaDB、PostgreSQL、SQL Server（除SQL Server 2017集群版和2019集群版）实例。 PostgreSQL云盘版支持多个高权限账号以及多个普通账号。 PostgreSQL 9.4和10.0本地盘版本实例只能创建一个高权限账号。 PPAS实例仅能创建一个高权限账号，普通账号可以连接数据库后使用SQL语句创建。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateAccount | 系统规定参数，取值：CreateAccount。 |

云数据库RDS

| AccountName | String | 是 | test1 | 数据库账号名称。 说明名称唯一。 以字母开头，以字母或数字结尾。 由小写字母、数字或下划线组成。 长度： MySQL 5.6支持账号长度为2~16个字符，MySQL 5.7和 8.0支持账号长度为 2~32个字符。 SQL Server支持账号长度为2~64个字符。 PostgreSQL云盘版支持账号长度为 2~63个字符，本地盘版支持账号长度为 2~16个字符。 MariaDB支持账号长度为2~16个字符。 其他非法字符，参见本手册中的禁用关键字表。 |
|---|---|---|---|---|
| AccountPasswor d | String | 是 | Test123456 | 数据库账号的密码。 说明长度为8~32个字符。 由大写字母、小写字母、数字、特殊字符中的任意三种组成。 特殊字符为!@#$%^&* () +-= _ |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| AccountDescripti on | String | 否 | 测试账号A | 账号描述，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（ ）、短横线（-）。 _ 说明不能以 http:// 和 https:// 开头。 |

云数据库RDS

| AccountType | String | 否 | Normal | 账号类型，取值： Normal：普通账号 Super：高权限账号默认值：Normal。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateAccount &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateAccountResponse>
         <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</CreateAccountResponse>
```

`JSON` 格式

```json
{
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### 删除数据库账号

调用该接口时，实例状态需要为运行中，否则将操作失败：

**说明**

该接口暂不支持SQL Server 2017集群版、PostgreSQL本地盘、PPAS实例。 对于PostgreSQL云盘实例，如果要删除的账号有数据库、表或其他对象的权限，执行删除账号操作只会锁定账号，取消相关权限后才能正常删除账号。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteAccount | 系统规定参数，取值：DeleteAccount。 |
| AccountName | String | 是 | test1 | 需要删除的数据库账号名称。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 91E855E5-7E80- 4955-929B- C74EE1D38C66 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DeleteAccount &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteAccountResponse>
   <RequestID>91E855E5-7E80-4955-929B-C74EE1D38C66</RequestID>
</DeleteAccountResponse>
```

`JSON` 格式

```json
{
    "RequestID":"91E855E5-7E80-4955-929B-C74EE1D38C66"
}
```

#### 查询实例账号名称

调用CheckAccountNameAvailable接口查询目标需要创建的账号名称是否可用。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | CheckAccountN ameAvailable | 系统规定参数。取值：CheckAccountNameAvailable 。 |
|---|---|---|---|---|
| AccountName | String | 是 | DatabaseTest | 需要创建的账号名称。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5E4AA101-1EE5- 41C0-AE6D- 0F066331AC1C | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CheckAccountNameAvailable &AccountName=DatabaseTest &DBInstanceId=rm-uf6wjk5xxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CheckAccountNameAvailableResponse>
      <RequestId>5E4AA101-1EE5-41C0-AE6D-0F066331AC1C</RequestId>
</CheckAccountNameAvailableResponse>
```

`JSON` 格式

```json
{
    "RequestId":"5E4AA101-1EE5-41C0-AE6D-0F066331AC1C"
}
```

#### 检查数据库名称可用性

调用CheckDBNameAvailable接口检查数据库名称是否重复或不符合命名规范。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CheckDBNameA vailable | 系统规定参数，取值：CheckDBNameAvailable。 |
| DBInstanceId | String | 是 | rm-t4n3axxxxx | 实例ID。 |
| DBName | String | 是 | test1 | 待检查的数据库名称。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6EF82B07-28D2- 48D1-B5D6- 7E78FED277C7 | 请求ID。 说明仅返回请求ID时，表示数据库名称可用，否则会返回报错信息，提示数据库名称重复或不符合命名规范。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CheckDBNameAvailable &DBInstanceId=rm-t4n3axxxxx &DBName=test1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CheckDBNameAvailableResponse>
  <RequestId>6EF82B07-28D2-48D1-B5D6-7E78FED277C7</RequestId>
</CheckDBNameAvailableResponse>
```

`JSON` 格式

```json
{"RequestId":"6EF82B07-28D2-48D1-B5D6-7E78FED277C7"}
```

#### 查询账号信息

云数据库RDS 调用DescribeAccounts接口查询实例的账号信息。

**说明**

该接口暂不支持SQL Server 2017集群版、PostgreSQL实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccount s | 系统规定参数，取值：DescribeAccounts。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| AccountName | String | 否 | test1 | 数据库账号名称。 |
| PageSize | Integer | 否 | 30 | 每页记录数。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Accounts | Array of DBInstanceAcc ount |  | 账号信息列表。 |
| DBInstanceAcc ount |  |  |  |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 账号所属实例ID。 |
| AccountName | String | test1 | 数据库账号名称。 |
| AccountStatus | String | Available | 账号状态： Unavailable：不可用 Available：可用 |
| AccountDescri ption | String | 测试数据库账号 | 账号描述。 |
| DatabasePrivil eges | Array of DatabasePrivil ege |  | 账号拥有的数据库权限列表。 |

云数据库RDS

| DatabasePrivil ege |  |  |  |
|---|---|---|---|
| DBName | String | test1 | 数据库名称。 |
| AccountPrivile ge | String | ReadWrite | 账号的权限类型，取值： ReadWrite：读写 ReadOnly：只读 DDLOnly：仅DDL DMLOnly：只DML Custom：自定义（可以通过SQL命令修改） |
| AccountPrivile geDetail | String | SELECT,INSERT | 账号权限类型对应的具体权限。请参见账号权限列表。 |
| AccountType | String | Normal | 账号类型，取值： Normal：普通账号 Super：高权限账号 Sysadmin：具备超级权限（SA）的账号 |
| PrivExceeded | String | 0 | 账号管理的数据库是否超过最大数量限制，取值： 1：是 0：否 |
| RequestId | String | A2E94301-D07F- 4457-9B49- 6AA2BB388C85 | 请求ID。 |
| SystemAdmin AccountFirstAc tivationTime | String | 2020-02- 06T11:00:00Z | 超级权限账号首次启用时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明仅当SysadminAccount为 True时返回，其余情况为空。 |
| SystemAdmin AccountStatus | String | True | 超级权限账号是否启用。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeAccounts &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例云数据库RDS `XML` 格式

```xml
<DescribeAccountsResponse>
   <Accounts>
      <DBInstanceAccount>
         <DatabasePrivileges>
            <DatabasePrivilege>
               <AccountPrivilege>ReadWrite</AccountPrivilege>
<AccountPrivilegeDetail>SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,INDEX,ALTER,CR TE TEMPORARY TABLES,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,EVENT,TRIGGER</AccountPrivilegeDetail>
               <DBName>testdb</DBName>
            </DatabasePrivilege>
         </DatabasePrivileges>
         <AccountStatus>Available</AccountStatus>
         <AccountDescription></AccountDescription>
         <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
         <AccountName>testacc02</AccountName>
         <PrivExceeded>0</PrivExceeded>
         <AccountType>Normal</AccountType>
      </DBInstanceAccount>
   </Accounts>
   <RequestId>A2E94301-D07F-4457-9B49-6AA2BB388C85</RequestId>
</DescribeAccountsResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "Accounts": {
        "DBInstanceAccount": [
            {
                "DatabasePrivileges": {
                    "DatabasePrivilege": [
                        {
                            "AccountPrivilege": "ReadWrite",
                            "AccountPrivilegeDetail":
"SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,REFERENCES,INDEX,ALTER,CREATE TEMPORARY TABLES ,LOCK TABLES,CREATE VIEW,SHOW VIEW,CREATE ROUTINE,ALTER ROUTINE,EXECUTE,EVENT,TRIGGER",
                            "DBName": "testdb"
                        }
```

]

```json
                },
                "AccountStatus": "Available",
                "AccountDescription": "",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "AccountName": "testacc02",
                "PrivExceeded": "0",
                "AccountType": "Normal"
            }
```

]

```json
    },
    "RequestId": "A2E94301-D07F-4457-9B49-6AA2BB388C85"
}
```

#### 授权账号

调用GrantAccountPrivilege接口授权账号访问数据库。 一个账号可授权访问一个或多个数据库。调用该接口时，请确保实例状态为运行中，否则将操作失败。 该接口暂不支持SQL Server 2017集群版、PostgreSQL本地盘版、PolarDB实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GrantAccountPri vilege | 系统规定参数，取值：GrantAccountPrivilege。 |
| AccountName | String | 是 | test1 | 账号名称。 |

云数据库RDS

| AccountPrivilege | String | 是 | ReadWrite | 账号权限，取值： ReadWrite：读写 ReadOnly：只读 DDLOnly：仅执行DDL DMLOnly：只执行DML DBOwner：数据库所有者说明 MySQL可传入ReadWrite、ReadOnl y、DDLOnly或DMLOnly 。 SQL Server可传入ReadWrite、ReadOnl y或DBOwner。 PostgreSQL云盘版可传入DBOwner。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |
| DBName | String | 是 | testDB | 需要授权访问的数据库名称。 |
| KillConnection | String | 否 | 无 | 无效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=GrantAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=test &AccountPrivilege=ReadWrite
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<GrantAccountPrivilegeResponse>
   <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
</GrantAccountPrivilegeResponse>
```

云数据库RDS `JSON` 格式

```json
{
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
}
```

#### 撤销账号权限

调用RevokeAccountPrivilege接口撤销账号对数据库的访问权限。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 数据库状态为运行中。

**说明**

具体撤销的权限包括SELECT、INSERT、UPDATE、DELETE、CREATE、DROP、 REFERENCES、INDEX、ALTER、CREATE TEMPORARY TABLES、LOCK TABLES、 EXECUTE、CREATE VIEW、SHOW VIEW、CREATE ROUTINE 、ALTER ROUTINE、 EVENT、TRIGGER； 该接口暂不支持SQL Server 2017集群版、PostgreSQL、POLARDB实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RevokeAccountP rivilege | 系统规定参数，取值：RevokeAccountPrivilege。 |
| AccountName | String | 是 | test1 | 账号名称。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| DBName | String | 是 | testDB | 数据库名称，撤销账号对该数据库的所有权限。多个数据库用英文逗号（,）隔开。 |
| KillConnection | String | 否 | 无 | 无效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E22099CA-A61E- 4992-A0B7- CE82DC175626 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=RevokeAccountPrivilege &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &DBName=testDB
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RevokeAccountPrivilegeResponse>
   <RequestId>E22099CA-A61E-4992-A0B7-CE82DC175626</RequestId>
</RevokeAccountPrivilegeResponse>
```

`JSON` 格式

```json
{
       "RequestId":"E22099CA-A61E-4992-A0B7-CE82DC175626"
}
```

#### 修改数据库账号描述

调用ModifyAccountDescription接口修改数据库账号的描述。 该接口暂不支持SQL Server 2017集群版、PostgreSQL、PolarDB实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAccountD escription | 系统规定参数，取值：ModifyAccountDescription。 |
| AccountDescripti on | String | 是 | 测试账号A | 账号描述，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（ ）、短横线（-）。 _ 说明不能以 http:// 和 https:// 开头。 |
| AccountName | String | 是 | test1 | 账号名称。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyAccountDescription
```

`&AccountDescription=`测试账号A

```
&AccountName=test1 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyAccountDescriptionResponse>
   <RequestId> 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</ModifyAccountDescriptionResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### 重置数据库账号密码

实例状态需要为运行中，否则操作将失败。 该接口暂不支持对SQL Server 2017集群版、PostgreSQL、PolarDB实例通过SQL创建

**说明**

的账号进行密码重置。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetAccountPa ssword | 系统规定参数，取值：ResetAccountPassword。 |
| AccountName | String | 是 | test1 | 数据库账号名称。 |

云数据库RDS

| AccountPasswor d | String | 是 | Test123456 | 新密码。 说明长度为8~32个字符。 由大写字母、小写字母、数字、特殊字符中的任意三种组成。 特殊字符为!@#$&%^* () +-= _ |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ResetAccountPassword &DBInstanceId=rm-uf6wjk5xxxxxxx &AccountName=test1 &AccountPassword=Test123456
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ResetAccountPasswordResponse>
   <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</ResetAccountPasswordResponse>
```

`JSON` 格式

```json
{
       "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### 重置高权限账号权限

调用ResetAccount接口重置高权限账号的权限。 该接口不适用于没有高权限账号的SQL Server 2008 R2实例。

**说明**

云数据库RDS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetAccount | 系统规定参数，取值：ResetAccount。 |
| AccountName | String | 是 | test1 | 高权限账号名称。 |
| AccountPasswor d | String | 是 | Test123456 | 设置新的高权限账号的密码。 说明长度为8~32个字符。 由大写字母、小写字母、数字、特殊字符中的任意三种组成。 特殊字符为!@#$&amp;%^*() +- _ = |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 81BC9559-7B22- 4B7F-B705- 5F56DEECDEA7 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ResetAccount &AccountName=test1 &AccountPassword=Test123456 &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ResetAccountResponse>
   <RequestId>81BC9559-7B22-4B7F-B705-5F56DEECDEA7</RequestId>
</ResetAccountResponse>
```

`JSON` 格式云数据库RDS

```json
{
       "RequestId":"81BC9559-7B22-4B7F-B705-5F56DEECDEA7"
}
```

#### 授予服务账号权限

调用GrantOperatorPermission接口为RDS服务账号授权。 当您在使用RDS过程中需要阿里云技术支持时，您需要授权RDS服务账号，技术支持人员才可以通过服务账号提供技术支持服务。 该接口仅支持如下实例： RDS MySQL RDS SQL Server RDS PostgreSQL

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GrantOperatorP ermission | 系统规定参数，取值： GrantOperatorPermission。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID |
| ExpiredTime | String | 是 | 2019-03- 27T16:00:00Z | 权限过期时间。yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Privileges | String | 是 | Control | 授权类型。取值： Control：配置权限。支持查看、修改实例配置。 Data：数据权限。支持查看表结构、 索引和SQL。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=GrantOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx &ExpiredTime=2019-03-27T16:00:00Z &Privileges=Control
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<GrantOperatorPermissionResponse>
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
</GrantOperatorPermissionResponse>
```

`JSON` 格式

```json
{
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
}
```

#### 锁定账号

调用LockAccount接口锁定RDS PostgreSQL实例的账号。 RDS PostgreSQL云盘实例支持锁定账号，被锁定的账号无法登录实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | LockAccount | 系统规定参数，取值：LockAccount。 |
| AccountName | String | 是 | testaccount | 要锁定的账号名称。单次只能锁定一个账号。 |
| DBInstanceId | String | 是 | pgm-bpxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1B291C4B-DDCD- 4D0A-8F6D- 7F3241DE9228 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=LockAccount &AccountName=testaccount &DBInstanceId=pgm-bpxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<LockAccountResponse>
    <RequestId>1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228</RequestId>
</LockAccountResponse>
```

`JSON` 格式

```json
{
 "RequestId": "1B291C4B-DDCD-4D0A-8F6D-7F3241DE9228"
}
```

#### 撤销服务账号权限

调用RevokeOperatorPermission接口撤销阿里云服务账号对RDS实例的访问权限。 当阿里云技术支持通过服务账号解决了您的问题后，您可以通过该接口释放阿里云服务账号对您RDS实例的访问权限。 该接口仅支持如下实例： RDS MySQL RDS SQL Server RDS PostgreSQL

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RevokeOperator Permission | 系统规定参数。取值：RevokeOperatorPermission。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 842B73C8-5776- 4BD9-9872- 69C8C46DD7D3 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=RevokeOperatorPermission &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RevokeOperatorPermissionResponse>
      <RequestId>842B73C8-5776-4BD9-9872-69C8C46DD7D3</RequestId>
</RevokeOperatorPermissionResponse>
```

`JSON` 格式

```json
{
    "RequestId":"842B73C8-5776-4BD9-9872-69C8C46DD7D3"
}
```

#### 解锁账号

调用UnlockAccount接口解锁RDS PostgreSQL实例的账号。 RDS PostgreSQL云盘实例被锁定的账号无法使用，需要解锁后才能继续使用。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UnlockAccount | 系统规定参数，取值：UnlockAccount。 |
| AccountName | String | 是 | testaccount | 要解锁的账号名称。单次只能解锁一个账号。 |
| DBInstanceId | String | 是 | pgm-bpxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | AA65190D-852A- 4C9B-88DA- E92698CAA350 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=UnlockAccount &AccountName=testaccount &DBInstanceId=pgm-bpxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UnlockAccountResponse>
  <RequestId>AA65190D-852A-4C9B-88DA-E92698CAA350</RequestId>
</UnlockAccountResponse>
```

`JSON` 格式

```json
{
 "RequestId": "AA65190D-852A-4C9B-88DA-E92698CAA350"
}
```

### 备份恢复

#### 创建备份

调用CreateBackup接口为实例创建一个备份集。 本接口调用的是RDS自带的备份功能接口，您也可以使用数据库备份DBS。更多信息，请参见**数据库备份**
**DBS** > **开发指南**中的**API****概览**。
调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 没有正在执行中的备份任务。 单个实例一天内可创建的备份集数量不超过20个。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateBackup | 系统规定参数，取值：CreateBackup。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| DBName | String | 否 | rds mysql _ | 数据库列表，多个数据库之间用英文逗号 （,）隔开。 说明 MySQL进行单库逻辑备份或SQL Server进行单库全量物理备份时可传入该参数。 |

云数据库RDS

| BackupStrategy | String | 否 | db | 备份策略，取值： db：单库备份 instance：实例备份说明 MySQL进行逻辑备份或 SQL Server进行全量物理备份时可传入该参数。 |
|---|---|---|---|---|
| BackupMethod | String | 否 | Physical | 备份类型，取值： Logical：逻辑备份 Physical：物理备份 Snapshot：快照备份默认值：Physical。 说明实例必须存在数据库才能进行逻辑备份。 各实例支持的备份类型请参见对应实例的用户指南手册。 SQL Server云盘实例进行快照备份时请填写Snapshot。 |
| BackupType | String | 否 | Auto | 备份方式，取值： Auto：自动选择全量备份或增量备份 FullBackup：全量备份默认值：Auto。 说明仅SQL Server需要填写此参数，其他引擎不用填写。 该值仅在BackupMethod参数为Physical时有效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupJobId | String | 5073731 | 备份任务ID。 |
| RequestId | String | 2C125605-266F- 41CA-8AC5- 3A643D4F42C5 | 请求ID。 |

云数据库RDS

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateBackup &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateBackupResponse>
   <RequestId>2C125605-266F-41CA-8AC5-3A643D4F42C5</RequestId>
   <BackupJobId>5073731</BackupJobId>
</CreateBackupResponse>
```

`JSON` 格式

```json
{
    "RequestId": "2C125605-266F-41CA-8AC5-3A643D4F42C5",
    "BackupJobId": "5073731"
}
```

#### 恢复数据（克隆实例）

调用CloneDBInstance接口将历史数据恢复至一个新实例（称为克隆实例）。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例当前没有正在执行的迁移任务。 实例已开启日志备份（用于按时间点恢复）。 若要按备份集克隆实例，则主实例必须至少有一个已完成备份的备份集。 RDS支持RAM子账号创建克隆实例，请务必保证子账号已添加克隆实例的授权策略。

**说明**

实例内数据库账号信息克隆以及其他功能的设置克隆将遵循如下方式： 实例内的白名单设置、SQL洞察（SQL审计）设置、阈值报警设置、备份设置、参数设置将和当前实例状态保持一致。 实例内的数据信息、账号信息与备份文件或时间点当时信息一致。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CloneDBInstanc e | 系统规定参数，取值：CloneDBInstance。 |
| PayType | String | 是 | Postpaid | 付费类型，取值固定为Postpaid（按量付费）。 |

云数据库RDS

| DBInstanceClass | String | 否 | mysql.n1.micro. 1 | 实例规格，详见云数据库RDS > 产品简介中的实例规格。 说明默认规格和主实例一致。 |
|---|---|---|---|---|
| DBInstanceStora ge | Integer | 否 | 1000 | 实例存储空间，单位：GB。每5GB进行递增，详见云数据库RDS > 产品简介中的实例规格。 说明默认存储空间和主实例一致。 |
| InstanceNetwork Type | String | 否 | VPC | 实例的网络类型，取值： VPC：专有网络 Classic：经典网络说明默认网络类型和主实例一致。 |
| DBInstanceId | String | 否 | rm- uf6wjk5xxxxxxx xxx | 实例ID。可调用DescribeDBInstances获取。 |
| BackupId | String | 否 | 9026262 | 备份集ID。 您可以通过DescribeBackups接口获取备份列表。 说明 BackupId和RestoreTime两者至少传入一个。 |
| RestoreTime | String | 否 | 2011-06- 11T16:00:00Z | 备份保留周期内的任意时间点。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 说明 BackupId和RestoreTime两者至少传入一个。 |
| VPCId | String | 否 | vpc- uf6f7l4fg90xxxx xxxxxx | 专有网络VPC ID。 说明请确保VPC属于对应的地域。 |
| VSwitchId | String | 否 | vsw- uf6adz52c2pxxx xxxxxxx | 虚拟交换机ID。 说明请确保虚拟交换机属于对应的和VPC和地域。 |

| 开发指南·API参考 |  |  |  | 云数据库RD |
|---|---|---|---|---|

| PrivateIpAddress | String | 否 | 172.16.201.69 | 新实例的内网IP，需要在指定交换机的IP 地址范围内。系统默认通过VPCId和VSwitchId自动分配。 |
|---|---|---|---|---|
| UsedTime | String | 否 | 无 | 无效参数。 |
| Period | String | 否 | 无 | 无效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| OrderId | String | 100789370xxxxx | 订单ID。 |
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CloneDBInstance &PayType=Postpaid &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceStorageType=cloud_essd
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CloneDBInstanceResponse>
   <OrderId>100789370xxxxx</OrderId>
   <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
   <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</CloneDBInstanceResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "OrderId": "100789370xxxxx",
    "DBInstanceId": "rm-uf6wjk5xxxxxxx",
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
}
```

#### 查看备份列表

调用DescribeBackups接口查看备份集列表。 备份集的状态**BackupStatus**必须是**Success**，才能用于恢复。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup s | 系统规定参数，取值：DescribeBackups。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| BackupId | String | 否 | 327329803 | 备份集ID。 |
| BackupStatus | String | 否 | Success | 备份集状态。取值： Success：已完成备份 Failed：备份失败 |
| BackupMode | String | 否 | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
| StartTime | String | 否 | 2011-06- 01T16:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 否 | 2011-06- 15T16:00Z | 查询结束时间，需要大于查询开始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30 50 100 默认值：30。 |

| 开发指南·API参考 |  |  |  | 云数据库RD |
|---|---|---|---|---|

| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalRecordCo unt | String | 100 | 总记录数。 |
| PageNumber | String | 1 | 页码。 |
| PageRecordCo unt | String | 30 | 本页备份集个数。 |
| Items | Array of Backup |  | 备份集列表。 |
| Backup |  |  |  |
| BackupId | String | 321020562 | 备份集ID。 |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| HostInstanceI D | String | 5882781 | 产生备份集的实例编号，用于区分该备份集产生于主实例或备实例。 |
| BackupStatus | String | Success | 备份集状态。 |
| BackupStartTi me | String | 2019-02- 03T12:20:00Z | 本次备份开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| BackupEndTim e | String | 2019-02- 13T12:20:00Z | 本次备份结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| BackupType | String | FullBackup | 备份类型，取值： FullBackup：全量备份 IncrementalBackup：增量备份 |

云数据库RDS

| BackupMode | String | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
|---|---|---|---|
| BackupMethod | String | Physical | 备份方式，取值： Logical：逻辑备份 Physical：物理备份 Snapshot：快照备份 |
| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | 公网下载地址，若当前不可下载，则返回空值。 说明例如：备份方式为快照备份的 SQL Server实例会返回空值。 |
| BackupIntrane tDownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | 内网下载地址，若当前不可下载，则返回空值。 说明例如：备份方式为快照备份的 SQL Server实例会返回空值。 |
| BackupSize | Long | 2167808 | 备份文件大小，单位：Byte。 |
| StoreStatus | String | Disabled | 该数据备份是否可删除，取值： Enabled：可删除 Disabled：不可删除 |
| MetaStatus | String | OK | 库表恢复的备份集状态，取值： OK：正常。 LARGE：表数量过多，不能用于库表恢复。 EMPTY：备份失败的备份集。 说明空串表示未开通库表恢复的备份集。 |
| SlaveStatus | String | 无 | 无效参数。 |
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeBackups &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<DescribeBackupsResponse>
      <TotalRecordCount>100</TotalRecordCount>
      <TotalEcsSnapshotSize>0</TotalEcsSnapshotSize>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>1A6D328C-84B8-40DC-BF49-6C73984D7494</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <BackupInitiator>System</BackupInitiator>
                  <StorageClass>0</StorageClass>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-interna
l.aliyuncs.com/xxxxx</BackupIntranetDownloadURL>
                  <BackupSize>2167808</BackupSize>
                  <BackupMode>Automated</BackupMode>
                  <BackupId>321020562</BackupId>
                  <IsAvail>1</IsAvail>
                  <Encryption>{}</Encryption>
                  <HostInstanceID>5882781</HostInstanceID>
                  <StoreStatus>Disabled</StoreStatus>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/xxxxx</BackupDownloadURL>
                  <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                  <CopyOnlyBackup>0</CopyOnlyBackup>
                  <BackupEndTime>2019-02-13T12:20:00Z</BackupEndTime>
                  <ConsistentTime>1576506856</ConsistentTime>
                  <BackupStartTime>2019-02-03T12:20:00Z</BackupStartTime>
                  <MetaStatus>OK</MetaStatus>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
                  <BackupDownloadLinkByDB>
                        <BackupDownloadLinkByDB>
                              <DownloadLink>https://cn-
hangzhou.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1</DownloadLink>
                              <IntranetDownloadLink>https://cn-hangzhou-
internal.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1</IntranetDownloadLink>
                              <DataBase>dbs</DataBase>
                        </BackupDownloadLinkByDB>
                  </BackupDownloadLinkByDB>
            </Backup>
      </Items>
</DescribeBackupsResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "DescribeBackupsResponse": {
        "TotalRecordCount": 100,
        "TotalEcsSnapshotSize": 0,
        "PageRecordCount": 30,
        "RequestId": "1A6D328C-84B8-40DC-BF49-6C73984D7494",
        "PageNumber": 1,
        "Items": {
            "Backup": {
                "BackupMethod": "Physical",
                "BackupInitiator": "System",
                "StorageClass": 0,
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-intern
al.aliyuncs.com/xxxxx",
                "BackupSize": 2167808,
                "BackupMode": "Automated",
                "BackupId": 321020562,
                "IsAvail": 1,
                "Encryption": "{}",
                "HostInstanceID": 5882781,
                "StoreStatus": "Disabled",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/xxxxx",
                "DBInstanceId": "rm-uf6wjk5xxxxxxx",
                "CopyOnlyBackup": 0,
                "BackupEndTime": "2019-02-13T12:20:00Z",
                "ConsistentTime": 1576506856,
                "BackupStartTime": "2019-02-03T12:20:00Z",
                "MetaStatus": "OK",
                "BackupType": "FullBackup",
                "BackupStatus": "Success",
                "BackupDownloadLinkByDB": {
                    "BackupDownloadLinkByDB": {
                        "DownloadLink": "https://cn-
hangzhou.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1",
                        "IntranetDownloadLink": "https://cn-hangzhou-
internal.bak.rds.aliyuncs.com/custins53664665/hins18676859_2021072909473127987849.zip?E xpires=*****&amp;dbList=tb1",
                        "DataBase": "dbs"
                    }
                }
            }
        }
    }
}
```

#### 查询备份设置

调用DescribeBackupPolicy接口查询实例备份设置。

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup Policy | 系统规定参数，取值：DescribeBackupPolicy。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可通过接口 DescribeDBInstances获取。 |
| BackupPolicyMo de | String | 否 | DataBackupPolic y | 备份类型，取值： DataBackupPolicy：数据备份 LogBackupPolicy：日志备份 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupRetenti onPeriod | Integer | 7 | 数据备份保留天数。 |
| PreferredBack upTime | String | 15:00Z-16:00Z | 数据备份时间，格式：HH:mmZ-HH:mmZ（UTC时间）。 |
| PreferredBack upPeriod | String | Monday,Wednesda y,Friday,Sunday | 数据备份周期，多个取值用英文逗号（,）隔开， 取值： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| BackupLog | String | Enable | 日志备份开关，取值：Enable \| Disabled |
| LogBackupRet entionPeriod | Integer | 7 | 日志备份保留天数。 |
| EnableBackup Log | String | 1 | 是否开启日志备份，取值： 1：表示开启 0：表示关闭 |
| HighSpaceUsa geProtection | String | Enable | 实例使用空间大于80%，或者剩余空间小于5GB 时，是否强制清理Binlog： Disable：不清理 Enable：清理 |

云数据库RDS

| LocalLogReten tionHours | Integer | 0 | 本地日志备份保留小时数。 |
|---|---|---|---|
| LocalLogReten tionSpace | String | 30 | 本地日志最大空间使用率。 |
| LogBackupFre quency | String | LogInterval | 日志备份频率，取值： LogInterval：每30分钟备份一次； 默认与数据备份周期PreferredBackupPeriod一致。 说明参数LogBackupFrequency仅适用于SQL Server。 |
| PreferredNext BackupTime | String | 2018-01- 19T15:15Z | 下次备份时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| RequestId | String | B87E2AB3-B7C9- 4394-9160- 7F639F732031 | 请求ID。 |
| ArchiveBackup KeepCount | String | 1 | 归档备份的保留个数。 |
| ArchiveBackup KeepPolicy | String | ByMonth | 归档备份的保留周期。 |
| ArchiveBackup RetentionPerio d | String | 365 | 归档备份的保留天数。 |
| CompressType | Integer | 1 | 备份压缩方式，取值： 0：不压缩 1：zlib压缩 2：并行zlib压缩 4：quicklz压缩，开启了库表恢复 8：MySQL8.0 quicklz压缩但是还未支持库表恢复 |
| Duplication | String | 无 | 无效参数。 |
| DuplicationCo ntent | String | 无 | 无效参数。 |
| DuplicationLoc ation | Struct |  | 无效参数。 |
| Location | Struct |  | 无效参数。 |
| Bucket | String | 无 | 无效参数。 |

云数据库RDS

| Endpoint | String | 无 | 无效参数。 |
|---|---|---|---|
| Sotrage | String | 无 | 无效参数。 |
| LogBackupLoc alRetentionNu mber | Integer | 60 | 本地Binlog保留个数。 |
| ReleasedKeep Policy | String | None | 已删除实例的归档备份保留策略。取值： None：不保留 Lastest：保留最后一个 All：全部保留 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeBackupPolicyResponse>
  <Category>Standard</Category>
  <ArchiveBackupRetentionPeriod>0</ArchiveBackupRetentionPeriod>
  <RequestId>292884FE-D689-47A2-9829-C05E63366201</RequestId>
  <Duplication></Duplication>
  <ReleasedKeepPolicy>None</ReleasedKeepPolicy>
  <ArchiveBackupKeepPolicy>ByMonth</ArchiveBackupKeepPolicy>
  <PreferredBackupTime>00:00Z-01:00Z</PreferredBackupTime>
  <LocalLogRetentionHours>18</LocalLogRetentionHours>
  <PreferredNextBackupTime>2021-01-07T00:40Z</PreferredNextBackupTime>
  <DuplicationLocation>
        <Sotrage>OSS</Sotrage>
        <Location>
              <Endpoint></Endpoint>
              <Bucket></Bucket>
        </Location>
  </DuplicationLocation>
  <HighSpaceUsageProtection>Enable</HighSpaceUsageProtection>
  <CompressType>1</CompressType>
  <LogBackupFrequency>LogInterval</LogBackupFrequency>
  <PreferredBackupPeriod>Tuesday,Thursday,Saturday</PreferredBackupPeriod>
  <ArchiveBackupKeepCount>1</ArchiveBackupKeepCount>
  <LogBackupRetentionPeriod>7</LogBackupRetentionPeriod>
  <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
  <BackupLog>Enable</BackupLog>
  <EnableBackupLog>1</EnableBackupLog>
  <SupportReleasedKeep>0</SupportReleasedKeep>
  <SupportVolumeShadowCopy>1</SupportVolumeShadowCopy>
  <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
  <BackupRetentionPeriod>10</BackupRetentionPeriod>
  <DuplicationContent></DuplicationContent>
  <BackupInterval>30</BackupInterval>
</DescribeBackupPolicyResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "Category": "Standard",
 "ArchiveBackupRetentionPeriod": 0,
 "RequestId": "292884FE-D689-47A2-9829-C05E63366201",
 "Duplication": "",
 "ReleasedKeepPolicy": "None",
 "ArchiveBackupKeepPolicy": "ByMonth",
 "PreferredBackupTime": "00:00Z-01:00Z",
 "LocalLogRetentionHours": "18",
 "PreferredNextBackupTime": "2021-01-07T00:40Z",
 "DuplicationLocation": {
  "Sotrage": "OSS",
  "Location": {
   "Endpoint": "",
   "Bucket": ""
  }
 },
 "HighSpaceUsageProtection": "Enable",
 "CompressType": "1",
 "LogBackupFrequency": "LogInterval",
 "PreferredBackupPeriod": "Tuesday,Thursday,Saturday",
 "ArchiveBackupKeepCount": 1,
 "LogBackupRetentionPeriod": "7",
 "LogBackupLocalRetentionNumber": 60,
 "BackupLog": "Enable",
 "EnableBackupLog": "1",
 "SupportReleasedKeep": 0,
    "SupportVolumeShadowCopy": 1,
 "LocalLogRetentionSpace": "30",
 "BackupRetentionPeriod": 10,
 "DuplicationContent": "",
 "BackupInterval": "30"
}
```

#### 修改备份设置

调用ModifyBackupPolicy接口修改RDS实例备份设置。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例不能为只读实例。 实例状态为运行中。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupPo licy | 系统规定参数，取值：ModifyBackupPolicy。 |

云数据库RDS

| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可通过接口 DescribeDBInstances获取。 |
|---|---|---|---|---|
| BackupPolicyMo de | String | 否 | DataBackupPolic y | 备份类型： DataBackupPolicy：数据备份 LogBackupPolicy：日志备份 |
| PreferredBackup Time | String | 否 | 00:00Z-01:00Z | 执行备份任务的时间。格式：HH:mmZ-HH:mmZ（UTC时间）。 说明 BackupPolicyMode为D ataBackupPolicy时，该参数必传。 仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |

云数据库RDS

| PreferredBackup Period | String | 否 | Monday | 备份周期。至少需要指定2天，多个取值用英文逗号（,）隔开。取值： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日说明与BackupInterval参数共同决定备份策略。例如：本参数指定周六周日备份，BackupInterval参数指定30分钟，则在每周的周六和周日每隔30分钟执行一次备份。 BackupPolicyMode参数为DataBackupPolicy时 ，该参数必传。 仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |
|---|---|---|---|---|
| BackupRetentio nPeriod | String | 否 | 7 | 数据备份保留天数，取值：7~730。 说明 BackupPolicyMode为D ataBackupPolicy时，该参数必传。 仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |

云数据库RDS

| BackupLog | String | 否 | Enable | 是否开启日志备份。取值： Enable：开启。 Disabled：关闭。 说明 BackupPolicyMode为D ataBackupPolicy时，用于开启或关闭日志备份。 仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |
|---|---|---|---|---|
| LogBackupReten tionPeriod | String | 否 | 7 | 日志备份保留天数。取值：7~730，且不大于数据备份保留天数。 说明当开启日志备份时，可设置日志备份文件的保留天数， 目前仅支持MySQL、 PostgreSQL、PPAS实例设置该值。 BackupPolicyMode参数为DataBackupPolicy或L ogBackupPolicy时都适用。 |
| EnableBackupLo g | String | 否 | 1 | 是否开启日志备份。取值： True或1：开启。 False或0：关闭。 说明 BackupPolicyMode为L ogBackupPolicy时，用于开启或关闭日志备份。 仅在BackupPolicyMode参数为LogBackupPolicy时生效。 |

云数据库RDS

| LocalLogRetenti onHours | String | 否 | 18 | 日志备份本地保留小时数。取值：0~7*24，0表示不保留。 说明 BackupPolicyMode为L ogBackupPolicy时，该参数必传。 仅在BackupPolicyMode参数为LogBackupPolicy时生效。 |
|---|---|---|---|---|
| LocalLogRetenti onSpace | String | 否 | 30 | 本地日志最大循环空间使用率，超出后， 则从最早的Binlog开始清理，直到空间使用率低于该比例。取值：0~50。默认不修改。 说明 BackupPolicyMode为L ogBackupPolicy时，该参数必传。 仅在BackupPolicyMode参数为LogBackupPolicy时生效。 |
| HighSpaceUsage Protection | String | 否 | Enable | 实例使用空间大于80%，或者剩余空间小于5GB时，是否无条件清理Binlog。取值：Enable \| Disable。默认不修改。 说明 BackupPolicyMode为L ogBackupPolicy时，该参数必传。 仅在BackupPolicyMode参数为LogBackupPolicy时生效。 |
| Duplication | String | 否 | 无 | 无效参数。 |
| DuplicationCont ent | String | 否 | 无 | 无效参数。 |
| DuplicationLocat ion | String | 否 | 无 | 无效参数。 |

云数据库RDS

| LogBackupFrequ ency | String | 否 | LogInterval | 日志备份频率，取值： LogInterval：每30分钟备份一次。 默认与数据备份频率一致。 说明 LogInterval参数仅适用于 SQL Server。 仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |
|---|---|---|---|---|
| CompressType | String | 否 | 4 | 备份压缩方式。取值： 1：zlib压缩，格式为tar.gz。 4：quicklz压缩，格式为xb.gz。仅适用于MySQL 5.6/5.7，此备份压缩方式可用于单库单表恢复。 8：quicklz压缩，格式为xb.gz。仅适用于MySQL 8.0。暂不支持单库单表恢复。 说明仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |
| ReleasedKeepPo licy | String | 否 | None | 已删除实例的归档备份保留策略。默认为 None。取值： None：不保留 Lastest：保留最后一个 All：全部保留说明仅在BackupPolicyMode参数为DataBackupPolicy时生效。 |
| LogBackupLocal RetentionNumbe r | Integer | 否 | 60 | 本地Binlog保留个数。默认为60。取值：6~100。 说明仅在BackupPolicyMode参数为LogBackupPolicy时生效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| CompressType | String | 4 | 备份压缩方式，取值： 0：不压缩。 1：zlib压缩。 2：并行zlib压缩。 4：quicklz压缩，开启了库表恢复。 8：MySQL8.0 quicklz压缩但是还未支持库表恢复。 |
|---|---|---|---|
| DBInstanceID | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| EnableBackup Log | String | 1 | 是否开启了日志备份。取值： 1：开启 0：关闭 |
| HighSpaceUsa geProtection | String | Disable | 实例使用空间大于80%，或者剩余空间小于5GB 时，是否无条件清理Binlog。 |
| LocalLogReten tionHours | Integer | 18 | 日志备份本地保留小时数。 |
| LocalLogReten tionSpace | String | 30 | 本地日志最大循环空间使用率。 |
| LogBackupLoc alRetentionNu mber | Integer | 60 | 本地Binlog保留个数。 |
| RequestId | String | DA147739-AEAD- 4417-9089- 65E9B1D8240D | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyBackupPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<ModifyBackupPolicyResponse>
        <HighSpaceUsageProtection>Disable</HighSpaceUsageProtection>
   <DBInstanceID>rm-bp1z3xxxxx</DBInstanceID>
   <RequestId>E4BF5598-ED12-4406-AAA4-F375428BE741</RequestId>
   <LocalLogRetentionHours>18</LocalLogRetentionHours>
   <EnableBackupLog>1</EnableBackupLog>
   <LocalLogRetentionSpace>30</LocalLogRetentionSpace>
      <LogBackupLocalRetentionNumber>60</LogBackupLocalRetentionNumber>
</ModifyBackupPolicyResponse>
```

`JSON` 格式

```json
{
    "HighSpaceUsageProtection": "Disable",
    "DBInstanceID": "rm-bp1z3xxxxx",
    "RequestId": "E4BF5598-ED12-4406-AAA4-F375428BE741",
    "LocalLogRetentionHours": "18",
    "EnableBackupLog": "1",
    "LocalLogRetentionSpace": "30",
    "LogBackupLocalRetentionNumber": 60
}
```

#### 删除数据备份

调用该接口删除数据备份文件只删除实例自身的备份集，不会删除所关联实例（只读、灾备、克隆等）的备份集。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例为MySQL、PostgreSQL的高可用版本。 如果日志备份已关闭，RDS实例不支持按时间点恢复功能。此时您可以删除已生成超过7天的任意数据备份文件。 如果日志备份已开启，且日志备份保留时间小于数据备份保留时间，则超过日志备份保留时间的数据备份文件可以删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBackup | 系统规定参数，取值：DeleteBackup。 |
| BackupId | String | 是 | 324909958 | 备份集ID。可通过接口DescribeBackups 查询。多组值以英文逗号（,）隔开，单次最多传入100个。 说明只支持删除 DescribeBackups 中StoreStatus为Enabled的备份集。 |

云数据库RDS

| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 37441409-FFD1- 40AA-8EC5- 9ECF5E2F7C29 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DeleteBackup &DBInstanceId=rm-uf6wjk5xxxxxxx &BackupId=324909958
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DeleteBackupResponse>
   <RequestId>37441409-FFD1-40AA-8EC5-9ECF5E2F7C29</RequestId>
</DeleteBackupResponse>
```

`JSON` 格式

```json
{
    "RequestId": "37441409-FFD1-40AA-8EC5-9ECF5E2F7C29"
}
```

#### 删除SQL Server备份

调用DeleteBackupFile接口删除RDS SQL Server的备份文件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteBackupFil e | 系统规定参数。取值：DeleteBackupFile。 |
| DBInstanceId | String | 是 | rm- bp6wjk5xxxxxx | 实例ID。 |

云数据库RDS

| RegionId | String | 否 | cn-hangzhou | 地域ID。 说明可以通过接口 DescribeRegions查看可用的地域 ID。 |
|---|---|---|---|---|
| BackupId | String | 否 | 293044600 | 备份集ID。单次最多传入100个备份集 ID，多个值之间用英文逗号（,）隔开。 说明 SQL Server仅支持传入单库备份ID。 可以通过接口 DescribeBackups查询备份集ID。 |
| DBName | String | 否 | testdb | 数据库名称。 |
| BackupTime | String | 否 | 2011-06- 11T16:00:00Z | 删除该时间点之前的备份文件。格式为 *yyyy-MM-dd*T*HH:mm:ss*Z（UTC时间）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DeletedBakset Ids | Integer | 293044600 | 已删除的备份集ID。 |
| RequestId | String | C7B3A91C-0ACD- 4948-ACAE- xxxxxxxD4069 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DeleteBackupFile &DBInstanceId=rm-bp6wjk5xxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069</RequestId> <DeletedBaksetIds>
    <DeletedBaksetIds>1111</DeletedBaksetIds>
</DeletedBaksetIds>
```

`JSON` 格式云数据库RDS

```json
{"RequestId":"C7B3A91C-0ACD-4948-ACAE-xxxxxxxD4069","DeletedBaksetIds": {"DeletedBaksetIds":"1111"}}
```

#### 查询备份任务

调用DescribeBackupTasks接口查询实例的备份任务列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup Tasks | 系统规定参数，取值：DescribeBackupTasks。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| Flag | String | 否 | 无 | 备用参数。 |
| BackupJobId | String | 否 | 4762614 | 备份任务ID。 |
| BackupMode | String | 否 | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
| BackupJobStatus | String | 否 | NoStart | 备份任务状态，取值： NoStart：未开始 Progressing：正在进行中默认为所有状态。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of BackupJob |  | 备份任务详情。 |
| BackupJob |  |  |  |

云数据库RDS

| BackupId | String | 346650271 | 任务生成的备份集ID。 说明当返回参数BackupStatus=Finished之后，传入请求参数BackupJobId才能够查看到备份集ID。 |
|---|---|---|---|
| BackupJobId | String | 4762614 | 备份任务ID。 |
| BackupProgres sStatus | String | NoStart | 备份程序状态。取值： NoStart：未开始 Preparing：准备中 Waiting：等待中 Uploading：上传中 Checking：检查中 Finished：已完成 |
| BackupStatus | String | NoStart | 备份任务状态。取值： NoStart：未开始 Checking：检查备份 Preparing：准备备份 Waiting：等待备份 Uploading：上传备份 Finished：完成备份 Failed：备份失败说明有任务执行时才会返回本参数。 |
| JobMode | String | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
| Process | String | 25 | 任务进度百分比。 |
| TaskAction | String | NormalBackupTask | 任务类型，取值： TempBackupTask：临时备份任务 NormalBackupTask：普通备份任务 |
| RequestId | String | 90496720-2319- 42A8-87CD- FCE4DF95EBED | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=DescribeBackupTasks &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeBackupTasksResponse>
   <Items>
      <BackupJob>
         <JobMode>Automated</JobMode>
         <BackupProgressStatus>NoStart</BackupProgressStatus>
         <TaskAction>NormalBackupTask</TaskAction>
         <BackupStatus>NoStart</BackupStatus>
         <BackupJobId>4762614</BackupJobId>
      </BackupJob>
   </Items>
   <RequestId>90496720-2319-42A8-87CD-FCE4DF95EBED</RequestId>
</DescribeBackupTasksResponse>
```

`JSON` 格式

```json
{
    "Items": {
        "BackupJob": [
            {
                "JobMode": "Automated",
                "BackupProgressStatus": "NoStart",
                "TaskAction": "NormalBackupTask",
                "BackupStatus": "NoStart",
                "BackupJobId": 4762614
            }
```

]

```json
    },
    "RequestId": "90496720-2319-42A8-87CD-FCE4DF95EBED"
}
```

#### 查询日志备份

调用DescribeLogBackupFiles接口查询实例的日志备份文件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLogBac kupFiles | 系统规定参数。取值：DescribeLogBackupFiles。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

| EndTime | String | 是 | 2018-10- 31T08:40Z | 查询结束时间，必须晚于查询开始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
|---|---|---|---|---|
| StartTime | String | 是 | 2018-10- 01T08:40Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30~1000。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of BinLogFile |  | 日志文件列表。 |
| BinLogFile |  |  |  |
| DownloadLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | HTTP协议的下载链接。若当前不可下载，则为空串。 |
| FileSize | Long | 788480 | 日志文件大小。单位：Byte。 |
| IntranetDownl oadLink | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | 内网下载地址，若当前不可下载，则为空串。有效期1小时。 |
| LinkExpiredTi me | String | 2019-03- 01T15:04:13Z | 链接过期时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| LogBeginTime | String | 2018-10- 31T08:40Z | 日志文件记录的开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| LogEndTime | String | 2018-10- 31T08:40Z | 日志文件记录的结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 100 | 本页日志文件个数。 |

云数据库RDS

| RequestId | String | F8EC669C-FC85- 43D7-AF06- C3641626B37E | 请求ID。 |
|---|---|---|---|
| TotalFileSize | Long | 2300 | 所有日志文件大小之和，单位：Byte。 |
| TotalRecordCo unt | Integer | 17 | 日志文件总数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeLogBackupFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2018-10-01T08:40Z &EndTime=2018-10-31T08:40Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeLogBackupFilesResponse>
   <Items></Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>0</TotalRecordCount>
   <RequestId>F8EC669C-FC85-43D7-AF06-C3641626B37E</RequestId>
   <PageRecordCount>0</PageRecordCount>
</DescribeLogBackupFilesResponse>
```

`JSON` 格式

```json
{
    "Items": {
        "BinLogFile": [ ]
    },
    "PageNumber": 1,
    "TotalRecordCount": 0,
    "RequestId": "F8EC669C-FC85-43D7-AF06-C3641626B37E",
    "PageRecordCount": 0
}
```

#### 查询备份集的库表信息

调用DescribeMetaList查询目标备份集中可恢复的库表信息。 在使用RestoreTable接口进行MySQL单库单表恢复之前，您可以通过本接口查询可恢复的库表信息。 实例为MySQL 8.0、5.7、5.6高可用版（本地SSD盘）。

**说明**

云数据库RDS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMetaLis t | 系统规定参数。取值：DescribeMetaList。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| RestoreType | String | 否 | BackupSetID | 恢复方式，取值： BackupSetID：基于备份集恢复，您还需要传入参数BackupSetID。 RestoreTime：基于时间点恢复，您还需要传入参数RestoreTime。 默认值：BackupSetID |
| BackupSetID | String | 否 | 14358 | 基于备份集查询时，使用的备份集的ID。 可调用DescribeBackups获取。 说明 RestoreType为BackupSetID时必传。 |
| RestoreTime | String | 否 | 2019-05- 30T03:29:10Z | 基于时间点查询时，使用的时间节点，需要早于当前时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。可调用 DescribeBackups获取。 说明 RestoreType为RestoreTime时必传 。 |
| GetDbName | String | 否 | testdb1 | 要查询的数据库名。精确匹配，会返回具体的数据库名以及库内所有的表。 说明为空则返回包含所有数据库的列表。 |

云数据库RDS

| Pattern | String | 否 | test | 要查询的数据库名。模糊匹配，只返回匹配的数据库名，不返回表名。 说明例如传入 test 匹配 testdb1 和 testdb2 ，确定目标数据库名称后再通过GetDbName参数传入精确的数据库名称查看目标库下所有表的信息。 |
|---|---|---|---|---|
| PageSize | String | 否 | 1 | 每页记录数。默认值：1。 说明需要和PageIndex一起传入才生效。 |
| PageIndex | String | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。默认值：1。 说明需要和PageSize一起传入才生效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceNa me | String | rm-uf6wjk5xxxxxxx | 实例名称。 |
| Items | Array of Meta |  | 备份中的库表信息列表。 |
| Meta |  |  |  |
| Database | String | testdb1 | 数据库名称。 |
| Size | String | 64 | 表的大小，单位：KB。 |
| Tables | String | test1 | 表名称。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 本页记录数。 |
| RequestId | String | 60F9A12A-16B8- 4728-B099- 4CA38D32C31C | 请求ID。 |

云数据库RDS

| TotalPageCou nt | Integer | 1 | 总页数。 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeMetaList &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeMetaList>
      <TotalPageCount>1</TotalPageCount>
      <TotalRecordCount>1</TotalRecordCount>
      <PageRecordCount>1</PageRecordCount>
      <RequestId>60F9A12A-16B8-4728-B099-4CA38D32C31C</RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Meta>
                  <Size>64</Size>
                  <Database>testdb1</Database>
                  <Tables>test1</Tables>
            </Meta>
      </Items>
      <DBInstanceName>rm-uf6wjk5xxxxxxx</DBInstanceName>
</DescribeMetaList>
```

`JSON` 格式

```json
{
 "TotalPageCount": "1",
 "TotalRecordCount": "1",
 "PageRecordCount": "1",
 "RequestId": "60F9A12A-16B8-4728-B099-4CA38D32C31C",
 "PageNumber": "1",
 "Items": {
  "Meta": [{
   "Size": "64",
   "Database": "testdb1",
   "Tables": "test1"
  }]
 },
 "DBInstanceName": "rm-uf6wjk5xxxxxxx"
}
```

云数据库RDS

#### 单库单表恢复

调用RestoreTable接口恢复RDS实例的某些数据库或表到原实例。 RDS MySQL支持单库和单表的数据恢复，可以通过备份指定恢复误删的数据库或表，快速恢复MySQL的数据。详情请参见单库单表备份。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例状态为运行中。 实例当前没有正在执行的迁移任务。 如果需要按时间点恢复，实例必须已开启日志备份。 实例已开启单库单表备份，并且开启后已创建新的备份。 恢复后的表名在实例中不存在。 仅适用于RDS MySQL实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RestoreTable | 系统规定参数，取值：RestoreTable。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。可调用DescribeDBInstances获取。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| BackupId | String | 否 | 9026262 | 备份集ID。 您可以通过DescribeBackups接口获取备份集列表。 说明 BackupId和RestoreTime两者至少传入一个。 |
| RestoreTime | String | 否 | 2011-06- 11T16:00:00Z | 备份保留周期内的任意时间点。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 说明 BackupId和RestoreTim e两者至少传入一个。 实例必须已开启日志备份。 |

云数据库RDS

| TableMeta | String | 否 | [{"type":"db","n ame":"testdb1"," newname":"test db1 new","table _ s": [{"type":"table", "name":"testdb1 table1","newna me":"testdb1tab le1 new"}]}] _ | 指定恢复的库表。格式： [{"type":"db","name":"<数据库 1名称>","newname":"<新数据库1名称>","tables": [{"type":"table","name":"<数据库1内的表1名称>","newname":"< 新的表1名称>"}, {"type":"table","name":"<数据库1内的表2名称>","newname":"<新的表2名称>"}]}, {"type":"db","name":"<数据库2 名称>","newname":"<新数据库2名称>","tables": [{"type":"table","name":"<数据库2内的表3名称>","newname":"< 新的表3名称>"}, {"type":"table","name":"<数据库2内的表4名称>","newname":"<新的表4名称>"}]}] |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | EA2D4F34-01A7- 46EB-A339- D80882135206 | 请求ID。 |

**示例**

请求示例

```json
http(s)://rds.example.com/?Action=RestoreTable &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &RestoreTime=2019-08-20T16:00:00Z &TableMeta=[{"type":"db","name":"dtstestdata","newname":"dtstestdata","tables":[{"type" :"table","name":"customer_old","newname":"customer_old123"}, {"type":"table","name":"order","newname":"order123"}]}]
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RestoreTableResponse>
  <RequestId>EA2D4F34-01A7-46EB-A339-D80882135206</RequestId>
</RestoreTableResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "RequestId": "EA2D4F34-01A7-46EB-A339-D80882135206"
}
```

#### 查看已删除实例的备份

调用DescribeDetachedBackups接口查看已删除实例的备份集列表。 本接口适用于RDS MySQL的本地盘实例。关于如何在实例释放后保留备份，请参见自动备份。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDetach edBackups | 系统规定参数。取值：DescribeDetachedBackups。 |
| Region | String | 是 | cn-hangzhou | 实例所在的地域。 |
| DBInstanceId | String | 否 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| BackupId | String | 否 | 327xxxxx3 | 备份集ID。 |
| BackupLocation | String | 否 | cn-hangzhou | 备份集所在地域。 |
| BackupStatus | String | 否 | Success | 备份集状态。取值： Success Failed |
| BackupMode | String | 否 | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
| StartTime | String | 否 | 2021-03- 01T16:00Z | 查询开始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 否 | 2021-03- 15T16:00Z | 查询结束时间，需要大于查询开始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |

云数据库RDS

| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30（默认值） 50 100 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 页码。 取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Backup | Array of Items |  | 备份集列表。 |
| Items |  |  |  |
| BackupDBNam es | String | testdb | 数据库名称。 |
| BackupDownlo adURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | 公网下载地址，若当前不可下载，则为空串。 |
| BackupEndTim e | String | 2019-02- 13T12:20:00Z | 本次备份结束时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| BackupExtract ionStatus | String | 无 | 备份集的状态。 |
| BackupId | String | 327xxxxx3 | 备份集ID。 |
| BackupIntrane tDownloadURL | String | http://rdsbak-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxx | 内网下载地址，若当前不可下载，则为空串。 |
| BackupLocatio n | String | cn-hangzhou | 备份集所在地域。 |
| BackupMethod | String | Physical | 备份方式，取值： Logical：逻辑备份 Physical：物理备份 |

云数据库RDS

| BackupMode | String | Automated | 备份模式，取值： Automated：系统自动备份 Manual：手动备份 |
|---|---|---|---|
| BackupScale | String | 无 | 备份集的扩展性。 |
| BackupSize | Long | 2167808 | 备份文件大小，单位：Byte。 |
| BackupStartTi me | String | 2019-02- 03T12:20:00Z | 本次备份开始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| BackupStatus | String | Success | 备份集状态。 |
| BackupType | String | FullBackup | 备份类型，取值： FullBackup：全量备份 IncrementalBackup：增量备份 |
| ConsistentTim e | Long | 1576506856 | 备份集的一致性时间点。返回值为时间戳。 说明仅MySQL 5.6返回本参数， 其他版本返回0。 |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| HostInstanceId | String | 5882781 | 产生备份集的实例编号，用于区分该备份集产生于主实例或备实例。 |
| MetaStatus | String | OK | 库表恢复的备份集状态，取值： OK：正常。 LARGE：表数量过多，不能用于库表恢复。 EMPTY：备份失败的备份集。 |
| SlaveStatus | String | 无 | 备库的状态。 |
| StoreStatus | String | Disabled | 该数据备份是否可删除，取值： Enabled：可删除 Disabled：不可删除 |
| TotalBackupSi ze | Long | 2167808 | 所有备份文件的大小，单位：Byte。 |
| PageNumber | String | 1 | 页码。 |

云数据库RDS

| PageRecordCo unt | String | 30 | 本页备份集个数。 |
|---|---|---|---|
| RequestId | String | 1A6D328C-84B8- 40DC-BF49- 6C73984D7494 | 请求ID。 |
| TotalBackupSi ze | Long | 2167808 | 所有备份文件的大小，单位：Byte。 |
| TotalRecordCo unt | String | 100 | 总记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDetachedBackups &Region=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDetachedBackupsResponse>
    <TotalRecordCount>1</TotalRecordCount>
    <PageRecordCount>1</PageRecordCount>
    <RequestId>B0BBC25A-6B3E-4BFD-A052-48664294E20D</RequestId>
    <PageNumber>1</PageNumber>
    <Items>
            <Backup>
                    <BackupMethod>Snapshot</BackupMethod>
                    <BackupInitiator>System</BackupInitiator>
                    <StorageClass>0</StorageClass>
                    <BackupMode>Automated</BackupMode>
                    <BackupSize>161061273600</BackupSize>
                    <BackupId>677987116</BackupId>
                    <IsAvail>1</IsAvail>
                    <HostInstanceID>9232003</HostInstanceID>
                    <BackupDBNames></BackupDBNames>
                    <StoreStatus>Disabled</StoreStatus>
                    <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
                    <BackupDownloadURL></BackupDownloadURL>
                    <BackupEndTime>2020-07-11T05:07:33Z</BackupEndTime>
                    <BackupStartTime>2020-07-11T05:07:33Z</BackupStartTime>
                    <ConsistentTime>0</ConsistentTime>
                    <BackupType>FullBackup</BackupType>
                    <MetaStatus></MetaStatus>
                    <BackupScale>DBInstance</BackupScale>
                    <BackupStatus>Success</BackupStatus>
                    <BackupLocation>OSS</BackupLocation>
            </Backup>
    </Items>
    <TotalBackupSize>161061273600</TotalBackupSize>
</DescribeDetachedBackupsResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "TotalRecordCount": 1,
 "PageRecordCount": 1,
 "RequestId": "B0BBC25A-6B3E-4BFD-A052-48664294E20D",
 "PageNumber": 1,
 "Items": {
  "Backup": [
   {
          "BackupMethod":"Physical",
     "BackupIntranetDownloadURL":"http://...",
     "BackupMode":"Automated",
     "BackupSize":9405440,
     "BackupId":509538643,
     "IsAvail":1,
     "HostInstanceID":100453678,
     "BackupDBNames":"",
     "StoreStatus":"Enabled",
     "DBInstanceId":"rm-uf6wjk5xxxxxxx",
     "BackupDownloadURL":"https://...",
     "BackupEndTime":"2020-09-04T02:55:36Z",
     "BackupStartTime":"2020-09-04T02:54:04Z",
     "ConsistentTime":"1599188049",
     "BackupType":"FullBackup",
     "MetaStatus":"OK",
     "BackupScale":"DBInstance",
     "BackupStatus":"Success",
     "BackupLocation":"OSS"
   }
```

]

```json
 },
 "TotalBackupSize": "161061273600"
}
```

### 数据库代理

#### 查询系统权重分配值

在开启读写分离的情况下，该接口用于计算系统指定的权重。如果是自定义读权重，请使用 DescribeDBInstanceNetInfo接口。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例使用的是共享代理。 实例为如下版本： MySQL 5.7高可用版（本地SSD盘） MySQL 5.6 SQL Server 2017集群版

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CalculateDBInst anceWeight | 系统规定参数，取值：CalculateDBInstanceWeight。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 主实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of DBInstanceWe ight |  | 系统指定权重列表。 |
| DBInstanceWe ight |  |  |  |
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| DBInstanceTy pe | String | Master | 实例类型，取值： Master：主实例 Readonly：只读实例 |
| Weight | String | 100 | 系统实时计算的实例权重。 |
| ReadonlyInsta nceSQLDelaye dTime | String | 30 | 只读实例延迟复制时间，只读实例延迟ReadonlyInstanceSQLDelayedTime 的时间后再同步主实例数据，单位：秒。 |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CalculateDBInstanceWeight &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<CalculateDBInstanceWeightResponse>
   <items>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <DBInstanceType>Master</DBInstanceType>
      <Weight></Weight>
      <Availability></Availability>
   </items>
   <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
</CalculateDBInstanceWeightResponse>
```

`JSON` 格式

```json
{
    "items": [
        {
            "DBInstanceId": "rm-uf6wjk5xxxxxxx",
            "DBInstanceType": "Master",
            "Weight": "",
            "Availability": ""
        }
```

`],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
}
```

#### 查询数据库代理设置

调用DescribeDBInstanceProxyConfiguration接口查看数据库代理设置。 该API查看的为原数据库代理的设置，而不是最新的数据库独享代理。查看数据库独享代理请参见 DescribeDBProxy。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例使用的是共享代理。 实例已开通读写分离。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceProxyConfigu ration | 系统规定参数，取值为：DescribeDBInstanceProxyCon figuration。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| AttacksProtect ionConfigurati on | String | {\"check interval s _ _ econds\":\"0\",\"ma x failed login atte _ _ _ mpts\":\"0\",\"block ing seconds\":\"0\", _ \"status\":\"Disable \"} | 是否开启防暴力破解： Enable：开启 Disable：关闭返回值格式为JSON字符串，如： {"status":"Disable", "check interval seconds": 60, _ _ "max failed login attempts": 60, _ _ _ "blocking seconds": 600} _ 参数说明及取值范围： 对于每一个客户端，check interval seconds秒内最多允许 _ _ max failed login attempts次错误密码登 _ _ _ 录，否则将对该客户端IP禁止登录 blocking seconds秒钟。 _ 取值范围： check interval seconds：30-600，单 _ _ 位为秒。 max failed login attempts：10- _ _ _ 5000，单位为次。 blocking seconds：30-3600，单位为 _ 秒。 |
|---|---|---|---|
| PersistentCon nectionsConfig uration | String | {\"status\":\"Disabl e\"} | 是否开启短连接优化： Enable：开启 Disable：关闭返回值格式为JSON字符串，如： {"status":"Disable"}。 |
| TransparentSw itchConfigurati on | String | {\"status\":\"Enabl e\"} | 是否开启透明切换： Enable：开启 Disable：关闭返回值格式为JSON字符串，如： {"status":"Enable"}。 |
| RequestId | String | E9DD55F4-1A5F- 48CA-BA57- DFB3CA8C4C34 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?DBInstanceId=rm-uf6wjk5xxxxxxxxxx &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```json
<DescribeDBInstanceProxyConfigurationResponse>
   <PersistentConnectionsConfiguration>{"status":"Disable"}
</PersistentConnectionsConfiguration>
   <TransparentSwitchConfiguration>{"status":"Enable"}</TransparentSwitchConfiguration>
   <AttacksProtectionConfiguration>
{"check_interval_seconds":"0","max_failed_login_attempts":"0","blocking_seconds":"0","sta s":"Disable"}</AttacksProtectionConfiguration>
   <RequestId>E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34</RequestId>
</DescribeDBInstanceProxyConfigurationResponse>
```

`JSON` 格式

```json
{
    "PersistentConnectionsConfiguration": "{\"status\":\"Disable\"}",
    "TransparentSwitchConfiguration": "{\"status\":\"Enable\"}",
    "AttacksProtectionConfiguration": "
{\"check_interval_seconds\":\"0\",\"max_failed_login_attempts\":\"0\",\"blocking_seconds\ \"0\",\"status\":\"Disable\"}",
    "RequestId": "E9DD55F4-1A5F-48CA-BA57-DFB3CA8C4C34"
}
```

#### 查询独享代理设置详情

调用DescribeDBProxy接口查询RDS实例的数据库独享代理设置详情。 RDS提供数据库独享代理服务，包括读写分离、短连接优化等能力。 调用该接口时，需要实例为如下版本： MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBProx y | 系统规定参数，取值：DescribeDBProxy。 |
| DBInstanceId | String | 是 | rm- bp1ja4f56s7us** ** | 实例ID。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |

**返回数据**

云数据库RDS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBProxyConne ctStringItems | Array of DBProxyConne ctStringItems |  | 独享代理的连接地址信息列表。 |
| DBProxyConne ctStringItems |  |  |  |
| DBProxyConne ctString | String | gos787jog2wk0ye1 ****- rw4rm.rwlb.rds.aliy uncs.com | 代理终端连接地址。 |
| DBProxyConne ctStringNetTyp e | String | InnerString | 代理连接地址的网络类型。取值： InnerString：内网。 OuterString：外网。 |
| DBProxyConne ctStringNetWo rkType | String | 1 | 代理网络类型，取值： 0：公网。 1：经典网络。 2：专有网络。 |
| DBProxyConne ctStringPort | String | 3306 | 代理连接地址的端口。 |
| DBProxyEndpo intId | String | 20**** | 后端代理终端ID。 |
| DBProxyEndpo intName | String | gos787jog2wk0ye1 **** | 代理终端名称，真实服务的代理终端ID。 |
| DBProxyVpcIn stanceId | String | rm- bp145737x5****13 1161274792**** | 代理的实例ID。 |
| DBProxyInstan ceCurrentMino rVersion | String | 1.13.11 | 代理实例当前版本。 |
| DBProxyInstan ceLatestMinor Version | String | 1.13.12 | 代理实例最新版本。 |

云数据库RDS

| DBProxyInstan ceNum | Integer | 1 | 开通的代理实例数量。 |
|---|---|---|---|
| DBProxyInstan ceStatus | String | Running | 代理地址的运行状态，取值： CREATING：创建中。 ACTIVATION：运行中。 DELETING：删除中。 RESTARTING：重启中。 CLASS CHANGING：变配中。 _ TRANSING：迁移中。 MINOR VERSION UPGRADING：小版 _ _ 本升级中。 |
| DBProxyInstan ceType | String | 2 | 代理服务类型。取值： 1：共享代理服务。 2：独享代理服务。 |
| DBProxyServic eStatus | String | Startup | 数据库独享代理功能开关状态，取值： Startup：开启。 Shutdown：关闭。 |
| RequestId | String | 909A69EE-71C8- 4417-A0B9- FF085407E1E3 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBProxy &DBInstanceId=rm-bp1ja4f56s7us****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBProxyResponse>
      <DBProxyInstanceName>gos787jog2wk0ye1****</DBProxyInstanceName>
      <DBProxyInstanceCurrentMinorVersion>1.13.11</DBProxyInstanceCurrentMinorVersion>
      <DBProxyServiceStatus>Startup</DBProxyServiceStatus>
      <DBProxyInstanceNum>1</DBProxyInstanceNum>
      <DBProxyInstanceLatestMinorVersion>1.13.12</DBProxyInstanceLatestMinorVersion>
      <RequestId>909A69EE-71C8-4417-A0B9-FF085407E1E3</RequestId>
      <DbProxyEndpointItems>
            <DbProxyEndpointItems>
                  <DbProxyEndpointName>gos787jog2wk0ye1****</DbProxyEndpointName>
                  <DbProxyEndpointAliases>proxy-test</DbProxyEndpointAliases>
                  <DbProxyEndpointType>RWSplit</DbProxyEndpointType>
                  <DbProxyReadWriteMode>ReadWrite</DbProxyReadWriteMode>
            </DbProxyEndpointItems>
      </DbProxyEndpointItems>
      <DBProxyConnectStringItems>
            <DBProxyConnectStringItems>
                  <DBProxyConnectString>gos787jog2wk0ye1****-
rw4rm.rwlb.rds.aliyuncs.com</DBProxyConnectString>
                  <DBProxyEndpointId>209090</DBProxyEndpointId>
                  <DBProxyEndpointName>gos787jog2wk0ye1****</DBProxyEndpointName>
                  <DBProxyConnectStringNetWorkType>2</DBProxyConnectStringNetWorkType>
                  <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
                  <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
                  <DBProxyVpcInstanceId>rm-bp145737x5****131161274792****</DBProxyVpcIns
tanceId>
            </DBProxyConnectStringItems>
      </DBProxyConnectStringItems>
      <DBProxyInstanceStatus>Running</DBProxyInstanceStatus>
      <DBProxyInstanceType>2</DBProxyInstanceType>
</DescribeDBProxyResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "DBProxyInstanceName": "gos787jog2wk0ye1****",
 "DBProxyInstanceCurrentMinorVersion": "1.13.11",
 "DBProxyServiceStatus": "Startup",
 "DBProxyInstanceNum": 1,
 "DBProxyInstanceLatestMinorVersion": "1.13.12",
 "RequestId": "909A69EE-71C8-4417-A0B9-FF085407E1E3",
 "DbProxyEndpointItems": {
  "DbProxyEndpointItems": [
   {
    "DbProxyEndpointName": "gos787jog2wk0ye1****",
    "DbProxyEndpointAliases": "proxy-test",
    "DbProxyEndpointType": "RWSplit",
    "DbProxyReadWriteMode": "ReadWrite"
   }
```

]

```json
 },
 "DBProxyConnectStringItems": {
  "DBProxyConnectStringItems": [
   {
    "DBProxyConnectString": "gos787jog2wk0ye1****-rw4rm.rwlb.rds.aliyuncs.com",
    "DBProxyEndpointId": 209090,
    "DBProxyEndpointName": "gos787jog2wk0ye1****",
    "DBProxyConnectStringNetWorkType": 2,
    "DBProxyConnectStringNetType": "InnerString",
    "DBProxyConnectStringPort": "3306",
    "DBProxyVpcInstanceId": "rm-bp145737x5****131161274792****"
   }
```

]

```json
 },
 "DBProxyInstanceStatus": "Running",
 "DBProxyInstanceType": "2"
}
```

#### 查询独享代理地址信息

调用DescribeDBProxyEndpoint接口查询RDS实例独享代理的连接地址信息。 RDS提供数据库独享代理服务，包括读写分离、短连接优化等能力。 调用该接口时，需要实例为如下版本： MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | DescribeDBProx yEndpoint | 系统规定参数，取值：DescribeDBProxyEndpoint。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- bp1ja4f56s7us** ** | 实例ID。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |
| DBProxyEndpoin tId | String | 否 | keaxncrjluwu0g ue**** | 代理终端名称。 |
| DBProxyConnect String | String | 否 | testproxy****.rw lb.rds.aliyuncs.c om | 代理连接地址。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBProxyConne ctString | String | testproxy****.rwlb. rds.aliyuncs.com | 代理连接地址。 |
| DBProxyConne ctStringNetTyp e | String | InnerString | 代理连接地址的网络类型，取值： InnerString：内网地址。 OuterString：外网地址。 |
| DBProxyConne ctStringPort | String | 3306 | 代理连接地址端口。 |
| DBProxyEndpo intId | String | keaxncrjluwu0gue* *** | 代理连接地址ID。可以通过本接口查询。 |
| DBProxyFeatur es | String | TransactionReadSq lRouteOptimizeStat us:1;ConnectionPer sist:0;ReadWriteSpl iting:1 | 代理终端的设置信息，格式为JSON，包含下述参数： TransactionReadSqlRouteOptimize Status：事务拆分设置，取值为0（关闭） 或1（开启）。 ConnectionPersist：连接池设置：取值为0（关闭）、1（会话级连接池）或2（事务级连接池）。 ReadWriteSpliting：读写分离设置，取值为0（关闭）或1（开启）。 |

云数据库RDS

| ReadOnlyInsta nceDistributio nType | String | Standard | 读权重分配模式。取值： Standard：按规格权重自动分配。 Custom：自定义分配权重。 |
|---|---|---|---|
| ReadOnlyInsta nceMaxDelayT ime | String | 30 | 读写分离的延迟阈值，当只读实例延迟时间超过该阈值时，读取流量不发往该实例，单位：秒。 |
| ReadOnlyInsta nceWeight | String | [{\"Availability\":\" Available\",\"DBInst anceId\":\"rr- bp176984qewd8** **\",\"DBInstanceTy pe\":\"ReadOnly\",\ "Weight\":400}, {\"Availability\":\"A vailable\",\"DBInsta nceId\":\"rm- bp1ja4f56s7us****\ ",\"DBInstanceType \":\"Master\",\"Weig ht\":0}] | 读权重分配信息，即传入主实例和只读实例的读请求权重，格式为JSON，包含下述参数： DBInstanceId：实例ID。 DBInstanceType：实例类型，取值为Master（主实例）或ReadOnly（只读实例）。 Weight：读请求权重，以100递增，最大值为10000。 说明如果该实例下没有只读实例，本参数返回null。 |
| RequestId | String | 847BA085-B377- 4BFA-8267- F82345ECE1D2 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBProxyEndpoint &DBInstanceId=rm-bp1ja4f56s7us**** &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```json
<DescribeDBProxyEndpointResponse>
      <DbProxyEndpointReadWriteMode>ReadWrite</DbProxyEndpointReadWriteMode>
      <ReadOnlyInstanceDistributionType>Standard</ReadOnlyInstanceDistributionType>
      <DBProxyConnectString>testproxy****.rwlb.rds.aliyuncs.com</DBProxyConnectString>
      <RequestId>336E33D5-8C02-4265-9627-704BF9F3954B</RequestId>
      <DBProxyEndpointId>keaxncrjluwu0guehzae</DBProxyEndpointId>
      <DbProxyEndpointAliases>proxyterminal-test</DbProxyEndpointAliases>
<DBProxyFeatures>TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWriteSpl ing:1;PinPreparedStmt:0</DBProxyFeatures>
      <ReadOnlyInstanceWeight>[{"Availability":"Available","DBInstanceId":"rr-
bp176984qewd8****","DBInstanceType":"ReadOnly","Weight":400}, {"Availability":"Available","DBInstanceId":"rmbp1ja4f56s7us****","DBInstanceType":"Master","Weight":0}]</ReadOnlyInstanceWeight>
      <ReadOnlyInstanceMaxDelayTime>30</ReadOnlyInstanceMaxDelayTime>
      <DBProxyConnectStringNetType>InnerString</DBProxyConnectStringNetType>
      <EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>2</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
<DbProxyEndpointConnectString>testproxy****.rwlb.rds.aliyuncs.com</DbProxyEndpointConnect ring>
            </EndpointConnectItems>
            <EndpointConnectItems>
                  <DbProxyEndpointNetType>0</DbProxyEndpointNetType>
                  <DbProxyEndpointPort>3306</DbProxyEndpointPort>
<DbProxyEndpointConnectString>test****.rwlb.rds.aliyuncs.com</DbProxyEndpointConnectStrin
            </EndpointConnectItems>
      </EndpointConnectItems>
      <DBProxyConnectStringPort>3306</DBProxyConnectStringPort>
</DescribeDBProxyEndpointResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "DbProxyEndpointReadWriteMode": "ReadWrite",
 "ReadOnlyInstanceDistributionType": "Standard",
 "DBProxyConnectString": "testproxy****.rwlb.rds.aliyuncs.com",
 "RequestId": "336E33D5-8C02-4265-9627-704BF9F3954B",
 "DBProxyEndpointId": "keaxncrjluwu0guehzae",
 "DbProxyEndpointAliases": "proxyterminal-test",
 "DBProxyFeatures":
"TransactionReadSqlRouteOptimizeStatus:1;ConnectionPersist:0;ReadWriteSpliting:1;PinPrepa dStmt:0",
 "ReadOnlyInstanceWeight": "[{\"Availability\":\"Available\",\"DBInstanceId\":\"rr-bp17
6984qewd8****\",\"DBInstanceType\":\"ReadOnly\",\"Weight\":400}, {\"Availability\":\"Available\",\"DBInstanceId\":\"rmbp1ja4f56s7us****\",\"DBInstanceType\":\"Master\",\"Weight\":0}]",
 "ReadOnlyInstanceMaxDelayTime": "30",
 "DBProxyConnectStringNetType": "InnerString",
 "EndpointConnectItems": {
  "EndpointConnectItems": [
   {
    "DbProxyEndpointNetType": "2",
    "DbProxyEndpointPort": "3306",
    "DbProxyEndpointConnectString": "testproxy****.rwlb.rds.aliyuncs.com"
   },
   {
    "DbProxyEndpointNetType": "0",
    "DbProxyEndpointPort": "3306",
    "DbProxyEndpointConnectString": "test****.rwlb.rds.aliyuncs.com"
   }
```

]

```json
 },
 "DBProxyConnectStringPort": "3306"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | Endpoint.NotFound | Specified endpoint is not found. | 未找到指定独享代理连接地址的端口。 |

#### 查询独享代理性能

调用DescribeDBProxyPerformance接口查询独享代理的性能数据。 RDS提供数据库独享代理服务，包括读写分离、短连接优化等能力。 调用该接口时，实例必须满足以下条件： 实例已开通数据库独享代理功能。 实例版本如下： 云数据库RDS MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBProx yPerformance | 系统规定参数，取值：DescribeDBProxyPerformance 。 |
| DBInstanceId | String | 是 | rm-t4n3axxxxx | 实例ID。 |
| EndTime | String | 是 | 2019-09- 21T18:00:00Z | 查询结束时间，不能早于查询开始时间。 格式：yyyy-MM-ddTHH:mm:ssZ（UTC 时间）。 |
| MetricsName | String | 是 | Maxscale CpuUs _ age | 性能指标，根据DBProxyInstanceType决定有哪些性能指标可以查询。 当DBProxyInstanceType=Dedicat edProxy，仅支持Maxscale CpuUsage：CPU使用 _ 率。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |
| StartTime | String | 是 | 2019-09- 19T01:00:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DBProxyInstance Type | String | 否 | DedicatedProxy | 代理服务类型。当前仅支持独享代理服务，取值：DedicatedProxy。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | lsmexxxxxxx | 监控实例的ID。 |
| EndTime | String | 2019-09- 21T18:00:00Z | 查询结束时间。 |

云数据库RDS

| PerformanceK eys | Array of PerformanceK ey |  | 性能列表。 |
|---|---|---|---|
| PerformanceK ey |  |  |  |
| Key | String | cpu ratio _ | 性能参数。 |
| ValueFormat | String | docker container c _ _ pu | 性能值的格式。 |
| Values | Array of PerformanceV alue |  | 数组格式：{value1, value2, …}。 |
| PerformanceV alue |  |  |  |
| Date | String | 2019-10- 10T09:00:00Z | 记录日期。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Value | String | 2.83 | 性能值。 |
| RequestId | String | DD31056F-A0CE- 41D7-AD39- 689B6ABAE982 | 请求ID。 |
| StartTime | String | 2019-09- 19T01:00:00Z | 查询开始时间。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBProxyPerformance &RegionId=cn-hangzhou &DBInstanceId=rm-t4n3axxxxx &MetricsName=Maxscale_CpuUsage &StartTime=2019-09-19T01:00:00Z &EndTime=2019-09-21T18:00:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBProxyPerformanceResponse>
  <DBInstanceId>lsmexxxxxxx</DBInstanceId>
  <RequestId>DD31056F-A0CE-41D7-AD39-689B6ABAE982</RequestId>
  <PerformanceKeys>
        <PerformanceKey>
              <Values>
                    <PerformanceValue>
                          <Value>2.83</Value>
                          <Date>2019-10-10T09:00:00Z</Date>
                    </PerformanceValue>
              </Values>
              <Key>cpu_ratio</Key>
              <ValueFormat>docker_container_cpu</ValueFormat>
        </PerformanceKey>
  </PerformanceKeys>
  <EndTime>2019-10-10T09:39:28Z</EndTime>
  <StartTime>2019-10-01T09:39:28Z</StartTime>
</DescribeDBProxyPerformanceResponse>
```

`JSON` 格式

```json
{
 "DBInstanceId": "lsmexxxxxxx",
 "RequestId": "DD31056F-A0CE-41D7-AD39-689B6ABAE982",
 "PerformanceKeys": {
  "PerformanceKey": [
   {
    "Values": {
     "PerformanceValue": [
      {
       "Value": "2.83",
       "Date": "2019-10-10T09:00:00Z"
      }
```

]

```json
    },
    "Key": "cpu_ratio",
    "ValueFormat": "docker_container_cpu"
   }
```

]

```json
 },
 "EndTime": "2019-10-10T09:39:28Z",
 "StartTime": "2019-10-01T09:39:28Z"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云数据库RDS

| 404 | Endpoint.NotFound | Specified endpoint is not found. | 未找到指定独享代理连接地址的端口。 |
|---|---|---|---|

#### 开关独享代理

调用ModifyDBProxy接口开启或者关闭RDS实例的数据库独享代理功能。 RDS提供数据库独享代理服务，包括读写分离、短连接优化等能力。 调用该接口时，需要实例为如下版本： MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBPro xy | 系统规定参数，取值：ModifyDBProxy。 |
| ConfigDBProxyS ervice | String | 是 | Startup | 开启或关闭数据库独享代理，取值： Startup：开启代理服务 Shutdown：关闭代理服务 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxx xx | 实例ID。可调用DescribeDBInstances获取。 |
| DBProxyInstance Num | String | 否 | 1 | 开通代理实例数量，取值：1~60。默认值：1。 说明更多的代理实例能处理更多的请求，您可以根据监控数据了解代理实例的负载，然后设置合理的代理实例数量。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions查看地域 ID。 |
| InstanceNetwork Type | String | 否 | VPC | 实例的网络类型。当前仅支持VPC网络，取值：VPC。 |

云数据库RDS

| VPCId | String | 否 | vpc- xxxxxxxxxxx x | 实例所属VPC ID。 |
|---|---|---|---|---|
| VSwitchId | String | 否 | CloudInstanc eId | 实例所属虚拟交换机ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FC452BB1-EED8-4278- 95C7-0324B3710DF1 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBProxy &DBInstanceId=rm-uf6wjk5xxxxxxx &ConfigDBProxyService=Startup
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBProxyResponse>
    <RequestId>FC452BB1-EED8-4278-95C7-0324B3710DF1</RequestId>
</ModifyDBProxyResponse>
```

`JSON` 格式

```json
{
 "RequestId": "FC452BB1-EED8-4278-95C7-0324B3710DF1"
}
```

#### 修改独享代理终端设置

调用ModifyDBProxyEndpoint接口修改RDS实例独享代理终端设置。 RDS提供数据库独享代理服务，包括读写分离、连接池等能力。 调用该接口时，实例必须满足以下条件： 实例已开通数据库独享代理功能。 实例版本如下： MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） 云数据库RDS MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 |  | 示例值 | 描述 |  |  |
|---|---|---|---|---|---|---|---|
| Action | String | 是 |  | ModifyDBProxyE ndpoint | 系统规定参数，取值：ModifyDBProxyEndpoint。 |  |  |
| DBInstanceId | String | 是 |  | rm- bp145737x5bi6* *** | 实例ID。 |  |  |
| DBProxyEndpoin tId | String | 是 |  | gos787jog2wk0y **** | 代理连接地址ID。可以通过接口 DescribeDBProxyEndpoint查看。 说明当DbEndpointOperator取值为Delete或Modify时，本参数必须传入。 |  |  |
| ConfigDBProxyF eatures | String | 否 |  |  | 设置代理连接地址想要开通的独享代理功能，各功能之间以英文分号（;）隔开。格式： 功能1:开通情况;功能2:开通情况;... 功能取值： ReadWriteSpliting：读写分离 ConnectionPersist：连接池 TransactionReadSqlRouteOpti mizeStatus：事务拆分开通情况取值： 1：功能已开通 0：功能未开通 |  |  |
|  |  |  |  |  |  | 功能1:开通情况;功能2:开通情 |  |
|  |  |  |  |  | 况;... |  |  |
|  |  |  |  | ReadWriteSplitin g:1;ConnectionP ersist:0; |  |  |  |
| RegionId | String | 否 |  | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |  |  |
| ReadOnlyInstanc eMaxDelayTime | String | 否 |  | 30 | 读写分离的延迟阈值，当只读实例延迟时间超过该阈值时，读取流量不发往该实例，单位：秒。不传该参数则保持原值。 取值：30~3600。默认值：30。 说明开通读写分离时才需要传入该参数。 |  |  |

云数据库RDS

| ReadOnlyInstanc eDistributionTyp e | String | 否 | Standard | 读权重分配模式。取值： Standard：按规格权重自动分配。 Custom：自定义分配权重。 说明开通读写分离时才需要传入该参数。 |
|---|---|---|---|---|
| ReadOnlyInstanc eWeight | String | 否 | {“rm- uf6wjk5xxxx“:”5 00”,”rr- tfhfgk5xxx”:”20 0”...} | 自定义读权重分配，即传入主实例和只读实例的读请求权重。以100递增，最大值为10000，格式： {“实例1ID“:”权重”,”实例2ID”:”权重”...} 。 说明当ReadOnlyInstanceDistributi onType取值为Custom时，您需要传入本参数。 |

|  |  | {“实例1ID“:”权 |
|---|---|---|
| m- | 重”,”实例2ID”:”权重”...} |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6B50D92C-1960- 4D4F-A290- AFADD6B1A5C8 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBProxyEndpoint &DBInstanceId=rm-bp145737x5bi6**** &DBProxyEndpointId=gos787jog2wk0y**** &ConfigDBProxyFeatures=ReadWriteSpliting:1;ConnectionPersist:1; &ReadOnlyInstanceMaxDelayTime=30 &ReadOnlyInstanceDistributionType=Standard
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBProxyEndpointResponse>
    <RequestId>6B50D92C-1960-4D4F-A290-AFADD6B1A5C8</RequestId>
</ModifyDBProxyEndpointResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "RequestId": "6B50D92C-1960-4D4F-A290-AFADD6B1A5C8"
}
```

#### 修改独享代理设置

调用ModifyDBProxyInstance接口修改RDS数据库独享代理设置。 RDS提供数据库独享代理服务，包括读写分离、短连接优化等能力。 调用该接口时，实例必须满足以下条件： 实例已开通数据库独享代理功能。 实例版本如下： MySQL 8.0高可用版（内核小版本20190915或以上） MySQL 5.7高可用版（内核小版本20190925或以上） MySQL 5.6高可用版（内核小版本20200229或以上）

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBProxyI nstance | 系统规定参数，取值：ModifyDBProxyInstance。 |
| DBInstanceId | String | 是 | rm-t4n3axxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| DBProxyInstance Num | String | 是 | 2 | 设置代理实例数量。当取值为0的时候，表示这个实例关闭此种类型代理服务。取值：0~60。 说明更多的代理实例能处理更多的请求， 您可以根据监控数据了解代理实例的负载，然后设置合理的代理实例数量。 |
| DBProxyInstance Type | String | 是 | DedicatedProxy | 代理服务类型。当前仅支持独享代理服务，取值：DedicatedProxy。 |

云数据库RDS

| EffectiveTime | String | 否 | MaintainTime | 生效时间，取值： Immediate：立即生效。 MaintainTime：在可运维时间段内生效。 SpecificTime：指定时间生效。 默认值：MaintainTime。 |
|---|---|---|---|---|
| EffectiveSpecific Time | String | 否 | 2019-07- 10T13:15:12Z | 指定时间生效。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明 EffectiveTime = SpecificTime时必传。 |
| RegionId | String | 否 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65C55572-530E- 4A53-BE03- 1D08CAF0F046 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBProxyInstance &DBInstanceId=rm-t4n3axxxxx &DBProxyInstanceType=DedicatedProxy &DBProxyInstanceNum=2 &EffectiveTime=Immediate
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBProxyInstanceResponse>
    <RequestId>65C55572-530E-4A53-BE03-1D08CAF0F046</RequestId>
</ModifyDBProxyInstanceResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "RequestId": "65C55572-530E-4A53-BE03-1D08CAF0F046"
}
```

#### 修改读权重和延迟阈值

调用ModifyReadWriteSplittingConnection接口修改读写分离链路的延迟阈值和各个实例的读权重。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例使用的是共享代理。 实例已开通读写分离。 实例为如下版本： MySQL 5.7高可用版（本地SSD盘） MySQL 5.6 SQL Server 2017集群版

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyReadWrit eSplittingConne ction | 系统规定参数，取值：ModifyReadWriteSplittingCon nection。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 主实例ID。可调用DescribeDBInstances 获取。 |
| ConnectionStrin gPrefix | String | 否 | rm- m5xxxxxxxxrw. mysql.rds.aliyun cs.com | 读写分离地址前缀名，不可重复，由小写字母和中划线组成，需以字母开头，长度不超过30个字符。 说明默认以“实例名+rw”字符串组成前缀。 |
| Port | String | 否 | 3306 | 读写分离地址端口号。 |
| MaxDelayTime | String | 否 | 12 | 延迟阈值，单位为秒。当只读实例延迟时间超过该阈值时，读取流量不发往该实例。不传该参数则保持原值。 说明参数MaxDelayTime不适用于SQL Server 2017集群版实例。 至少传入MaxDelayTime或Dist ributionType中的一个。 |

云数据库RDS

| DistributionType | String | 否 | Standard | 读权重分配模式，取值： Standard：按规格权重自动分配 Custom：自定义分配权重说明至少传入MaxDelayTime或Distributio nType中的一个。 |
|---|---|---|---|---|
| Weight | String | 否 | {“Instanceid1“:” 100”,”Instanceid 2”:”200”} | 读权重分配，即传入主实例和只读实例的读请求权重。以100递增，最大值为 10000，格式： {“Instanceid1“:”Weight”,”Instanceid 2”:”Weight”...}。 说明当DistributionType为C ustom时，必须传入该参数。 当DisrtibutionType为St andard时，传入该参数无效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyReadWriteSplittingConnection &DistributionType=Standard &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyReadWriteSplittingConnectionResponse>
   <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ModifyReadWriteSplittingConnectionResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

#### 释放读写分离地址

调用ReleaseReadWriteSplittingConnection接口释放读写分离地址。 调用该接口时，实例必须满足以下条件，否则将操作失败： 实例使用的是共享代理。 实例已开通读写分离。 实例为如下版本： MySQL 5.7高可用版（本地SSD盘） MySQL 5.6 SQL Server 2017集群版

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ReleaseReadWri teSplittingConne ction | 系统规定参数，取值：ReleaseReadWriteSplittingCo nnection。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 主实例ID。可调用DescribeDBInstances 获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ReleaseReadWriteSplittingConnection &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ReleaseReadWriteSplittingConnectionResponse>
   <RequestID>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestID>
</ReleaseReadWriteSplittingConnectionResponse>
```

云数据库RDS `JSON` 格式

```json
{
    "RequestID":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
  }
```

### 主备高可用和数据复制方式

#### 查询高可用模式

调用DescribeDBInstanceHAConfig接口查询RDS实例高可用模式和数据复制方式。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceHAConfig | 系统规定参数，取值：DescribeDBInstanceHAConfig 。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxx | 实例ID。 |
| HAMode | String | RPO | 高可用模式，取值： RPO：数据一致性优先，实例会尽可能保障数据的可靠性，即数据丢失量最少。对于数据一致性要求比较高的用户应该使用RPO模式。 RTO：实例可用性优先，实例会尽快恢复服务，即可用时间最长。对于数据库在线时间要求比较高的用户应该使用RTO模式。 说明仅MySQL实例返回此参数。 |
| SyncMode | String | Sync | 数据复制方式，取值： Sync：强同步 Semi-sync：半同步 Async：异步说明仅MySQL实例返回此参数。 |
| HostInstanceIn fos | Array of NodeInfo |  | 主备实例信息列表。 |

云数据库RDS

| NodeInfo |  |  |  |
|---|---|---|---|
| NodeId | String | 3397027 | 实例的唯一标识。 |
| NodeType | String | Master | 节点类型，取值： Master：主节点 Slave：备节点 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |
| SyncStatus | String | NotAvailable | 同步状态，取值： NotAvailable：不可用，即发生故障。 Syncing：同步中，切换可能会发生数据丢失。 Synchronized：完成同步。 NotSupport：引擎类型或者版本不涉及主备同步。 |
| LogSyncTime | String | 2018-05- 05T15:15:00Z | 备实例收到主实例日志的时间。格式：yyyy- MM-ddTHH:mm:ssZ（UTC时间）。 |
| DataSyncTime | String | 2018-05- 05T15:15:00Z | 备实例执行日志完成数据同步的时间。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |
| SwitchMode | String | 无 | 废弃参数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceHAConfig &DBInstanceId=rm-uf6wjk5xxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBInstanceHAConfigResponse>
  <RequestId>103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxxx</DBInstanceId>
  <HAMode>RPO</HAMode>
  <HostInstanceInfos>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Slave</NodeType>
              <NodeId>13567431</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
        <NodeInfo>
              <DataSyncTime></DataSyncTime>
              <ZoneId>cn-hangzhou-h</ZoneId>
              <LogSyncTime></LogSyncTime>
              <NodeType>Master</NodeType>
              <NodeId>14565107</NodeId>
              <SyncStatus>NotSupport</SyncStatus>
              <RegionId>cn-hangzhou</RegionId>
        </NodeInfo>
  </HostInstanceInfos>
  <SyncMode>Semi-sync</SyncMode>
</DescribeDBInstanceHAConfigResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "RequestId": "103D4ACC-F2F9-4A7E-9ACC-14B0A25613E0",
 "DBInstanceId": "rm-uf6wjk5xxxxxx",
 "HAMode": "RPO",
 "HostInstanceInfos": {
  "NodeInfo": [
   {
    "DataSyncTime": "",
    "ZoneId": "cn-hangzhou-h",
    "LogSyncTime": "",
    "NodeType": "Slave",
    "NodeId": "13567431",
    "SyncStatus": "NotSupport",
    "RegionId": "cn-hangzhou"
   },
   {
    "DataSyncTime": "",
    "ZoneId": "cn-hangzhou-h",
    "LogSyncTime": "",
    "NodeType": "Master",
    "NodeId": "14565107",
    "SyncStatus": "NotSupport",
    "RegionId": "cn-hangzhou"
   }
```

]

```json
 },
 "SyncMode": "Semi-sync"
}
```

#### 修改高可用模式

调用ModifyDBInstanceHAConfig接口修改实例的高可用模式和数据复制方式。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eHAConfig | 系统规定参数，取值：ModifyDBInstanceHAConfig。 |
| DbInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| SyncMode | String | 否 | Sync | 数据复制方式，取值： Sync：强同步 Semi-sync：半同步 Async：异步说明暂不支持SQL Server 2017集群版。 |

云数据库RDS

| HAMode | String | 否 | RPO | 高可用模式，取值： RPO：数据一致性优先，实例会尽可能保障数据的可靠性，即数据丢失量最少。对于数据一致性要求比较高的用户应该使用RPO模式。 RTO：实例可用性优先，实例会尽快恢复服务，即可用时间最长。对于数据库在线时间要求比较高的用户应该使用 RTO模式。 |
|---|---|---|---|---|
| SwitchMode | String | 否 | 0 | 切换主备节点的时间点。取值： 0：立即切换。 1：在可运维时间段内切换。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | D4D4BE8A-DD46- 440A-BFCD- EE31DA81C9DD | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceHAConfig &DbInstanceId=rm-uf6wjk5xxxxxxx &HAMode=RPO &SyncMode=Sync
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceHAConfigResponse>
   <RequestId>D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD</RequestId>
</ModifyDBInstanceHAConfigResponse>
```

`JSON` 格式

```json
{
    "RequestId":"D4D4BE8A-DD46-440A-BFCD-EE31DA81C9DD"
}
```

#### 查看主备切换日志

调用DescribeDBInstanceSwitchLog接口查看实例的主备切换日志。 该接口用于查看实例的主备切换日志，适用于MySQL实例、SQL Server实例、PostgreSQL实例、 PolarDB实例。 云数据库RDS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceSwitchLog | 系统规定参数，取值为：DescribeDBInstanceSwitchLo g。 |
| EndTime | String | 是 | 2018-06- 11T15:00Z | 查询结束时间，格式如：2011-06- 11T16:00Z，必须大于查询开始时间。 |
| StartTime | String | 是 | 2014-06- 11T15:00Z | 查询开始时间，格式如：2011-06- 11T15:00Z。 |
| DBInstanceId | String | 否 | rdsaiiabnaiiabn | 实例ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30/50/100，默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为：大于0，且不超过30。默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceNa me | String | rdsaiiabnaiiabn | 实例名称。 |
| Items | Array of Item |  | 主备日志列表。 |
| Item |  |  |  |
| AffectedSessio ns | String | 无 | 切换时影响会话数。 |
| HAStatus | String | 无 | 无 |
| SwitchCauseC ode | String | 无 | 切换原因。 |
| SwitchFinishTi me | String | 无 | 切换结束时间。 |
| SwitchId | String | 无 | 切换实例的ID。 |
| SwitchStartTi me | String | 无 | 切换开始时间。 |

云数据库RDS

| TotalSessions | String | 无 | 切换时总会话数。 |
|---|---|---|---|
| PageNumber | Integer | 1 | 当前页数。 |
| PageRecordCo unt | Integer | 60 | 每页显示记录数。 |
| RequestId | String | D1CA494F-CC13- 4EB6-8C4D- 5352EE4045BD | 请求ID。 |
| TotalRecordCo unt | Integer | 5 | 总记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSwitchLog &EndTime=2018-06-11T15:00Z &StartTime=2014-06-11T15:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceSwitchLogResponse>
   <Items></Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>5</TotalRecordCount>
   <RequestId>D1CA494F-CC13-4EB6-8C4D-5352EE4045BD</RequestId>
   <PageRecordCount>60</PageRecordCount>
   <DBInstanceName>rm-m5el220b25im05g7g</DBInstanceName>
</DescribeDBInstanceSwitchLogResponse>
```

`JSON` 格式

```json
{
    "Items": {},
    "PageNumber": 1,
    "TotalRecordCount": 5,
    "RequestId": "D1CA494F-CC13-4EB6-8C4D-5352EE4045BD",
    "PageRecordCount": 60,
    "DBInstanceName": "rm-m5el220b25im05g7g"
}
```

#### 查询主备切换设置

调用DescribeHASwitchConfig接口查询RDS实例主备自动切换设置。 主备实例切换后原来的主实例会变成备实例。 云数据库RDS 调用该接口时，实例必须为高可用版或集群版。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeHASwit chConfig | 系统规定参数，取值：DescribeHASwitchConfig。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| HAConfig | String | Manual | 主备自动切换设置，取值： Auto：出现故障时自动切换主备实例。 Manual：已临时关闭自动切换。 |
| ManualHATim e | String | 2019-08- 29T15:00:00Z | 临时关闭截止时间。 |
| RequestId | String | 4FDF4B79-2741- 4C5F-8C76- 4B953FC5C2B1 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeHASwitchConfigResponse>
   <ManualHATime>2019-08-29T15:00:00Z</ManualHATime>
   <RequestId>4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1</RequestId>
   <HAConfig>Manual</HAConfig>
</DescribeHASwitchConfigResponse>
```

`JSON` 格式

```json
{
 "ManualHATime": "2019-08-29T15:00:00Z",
 "RequestId": "4FDF4B79-2741-4C5F-8C76-4B953FC5C2B1",
 "HAConfig": "Manual"
}
```

#### 切换主备实例

调用SwitchDBInstanceHA接口切换RDS实例的主备实例。 本接口可用于切换非基础版RDS实例的主备实例，切换主备实例后，原来的备实例成为主实例并承担业务流量。

**注意事项**

（重要）主备实例的数据会实时同步，备实例仅可作为只读实例或备份形式存在，请不要对备实例做任何修改，否则可能导致主实例的数据被误删或覆盖，造成不可挽回的业务损失。 （重要）如果将备实例作为只读实例，需要考虑发生主备切换时，备实例成为新主实例后承担的读写压力。建议提前做好资源预留和规划。 主备实例切换过程中可能会有闪断，请确保您的应用程序具有自动重连机制。 如果实例下挂载有只读实例，那么主备实例切换后，只读实例的数据同步会有几分钟的延迟，因为需要重建复制链路、同步增量数据等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SwitchDBInstanc eHA | 系统规定参数，取值：SwitchDBInstanceHA。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 主实例ID。可调用DescribeDBInstances 获取。 |
| NodeId | String | 是 | 349054 | 备实例的唯一标识，通过接口 DescribeDBInstanceHAConfig可查询该值。 |
| Operation | String | 否 | 无 | 无效参数。 |

云数据库RDS

| Force | String | 否 | No | 切换方式，取值： Yes：强制 No：非强制默认值：No。 |
|---|---|---|---|---|
| EffectiveTime | String | 否 | Immediate | 生效时间，取值： Immediate：立即执行 MaintainTime：可维护时间内执行默认值：Immediate。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=SwitchDBInstanceHA &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &NodeId=349054
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<SwitchDBInstanceHAResponse>
   <RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId>
</SwitchDBInstanceHAResponse>
```

`JSON` 格式

```json
{
    "RequestId": "1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC"
  }
```

#### 设置主备自动切换

调用ModifyHASwitchConfig接口开启或关闭RDS实例的主备自动切换功能。 本接口可用于切换非基础版RDS实例的主备实例，切换主备实例后，原来的备实例成为主实例并承担业务流量。

**注意事项**

（重要）主备实例的数据会实时同步，备实例仅可作为只读实例或备份形式存在，请不要对备实例做任何云数据库RDS 修改，否则可能导致主实例的数据被误删或覆盖，造成不可挽回的业务损失。 （重要）如果将备实例作为只读实例，需要考虑发生主备切换时，备实例成为新主实例后承担的读写压力。建议提前做好资源预留和规划。 主备实例切换过程中可能会有闪断，请确保您的应用程序具有自动重连机制。 如果实例下挂载有只读实例，那么主备实例切换后，只读实例的数据同步会有几分钟的延迟，因为需要重建复制链路、同步增量数据等。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyHASwitch Config | 系统规定参数，取值：ModifyHASwitchConfig。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx xxx | 实例ID。可调用DescribeDBInstances获取。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |
| HAConfig | String | 否 | Manual | 主备切换设置，取值： Auto：出现故障时自动切换主备实例。 Manual：临时关闭自动切换。 默认值：Auto。 说明取值为Manual时，必须传入参数ManualHATime。 |
| ManualHATime | String | 否 | 2019-08- 29T15:00:00Z | 临时关闭的截止时间。最晚可设置为7天后的23:59:59。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明仅当参数HAConfig取值为Manual时，本参数有效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B6AE1448-D846- 4831-B1C7- CFF3E99D5470 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=ModifyHASwitchConfig &RegionId=cn-hangzhou &DBInstanceId=rm-uf6wjk5xxxxxxxxxx &HAConfig=Manual &ManualHATime=2019-08-28T15:00:00
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyHASwitchConfigResponse>
   <RequestId>B6AE1448-D846-4831-B1C7-CFF3E99D5470</RequestId>
</ModifyHASwitchConfigResponse>
```

`JSON` 格式

```json
{
 "RequestId": "B6AE1448-D846-4831-B1C7-CFF3E99D5470"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | HaConfig.Format | The value of HaConfig must be auto or manual | 主备自动切换值必须配置为自动或手动。 |
| 400 | HaConfigIsNull | HaConfig is null. | 主备自动切换参数值为null。 |

### 安全加密

#### 查询IP白名单

调用DescribeDBInstanceIPArrayList接口查询RDS实例IP白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceIPArrayList | 系统规定参数，取值：DescribeDBInstanceIPArrayLi st。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

| WhitelistNetwork Type | String | 否 | VPC | 白名单的网络类型，取值： Classic：高安全白名单模式下的经典网络 VPC：高安全白名单模式下的专有网络 MIX：通用白名单模式默认返回所有网络类型的白名单IP。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of DBInstanceIPA rray |  | IP白名单分组列表。 |
| DBInstanceIPA rray |  |  |  |
| DBInstanceIPA rrayName | String | rds default _ | IP白名单分组名称。 |
| DBInstanceIPA rrayAttribute | String | hidden | 白名单分组属性，默认为空。 说明控制台不显示带有hidden属性的分组，带有该标签的分组通常是用于访问DTS等服务的。 |
| SecurityIPList | String | 192.168.1.0/24 | IP白名单分组下的IP列表。 |
| SecurityIPType | String | IPv4 | IP地址的类型。返回值： IPv4 IPv6 |
| RequestId | String | E2B6AF71-DC32- 4055-B477- 43B348798D10 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceIPArrayList &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBInstanceIPArrayListResponse>
   <Items>
      <DBInstanceIPArray>
         <DBInstanceIPArrayName>rds_default</DBInstanceIPArrayName>
         <DBInstanceIPArrayAttribute></DBInstanceIPArrayAttribute>
         <WhitelistNetworkType>VPC</WhitelistNetworkType>
         <SecurityIPList>192.168.1.0/24</SecurityIPList>
         <SecurityIPType>IPv4</SecurityIPType>
      </DBInstanceIPArray>
   </Items>
   <RequestId>E2B6AF71-DC32-4055-B477-43B348798D10</RequestId>
</DescribeDBInstanceIPArrayListResponse>
```

`JSON` 格式

```json
{
 "Items": {
  "DBInstanceIPArray": [
   {
    "DBInstanceIPArrayName": "rds_default",
    "DBInstanceIPArrayAttribute": "",
    "WhitelistNetworkType": "VPC",
    "SecurityIPList": "192.168.1.0/24",
    "SecurityIPType": "IPv4"
   }
```

]

```json
 },
 "RequestId": "E2B6AF71-DC32-4055-B477-43B348798D10"
}
```

#### 修改IP白名单

调用ModifySecurityIps接口修改RDS实例IP白名单。 添加IP地址到IP白名单内，允许这些IP地址访问该RDS实例。 调用该接口时，实例状态必须为运行中，否则将操作失败。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySecurityIp s | 系统规定参数，取值：ModifySecurityIps。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

| SecurityIps | String | 是 | 10.23.12.24 | 该实例的IP白名单，多个IP地址请以英文逗号（,）隔开，不可重复。支持IPv4和 IPv6两种格式的IP地址，并且支持如下两种形式： IP地址形式，例如：10.23.12.24。 CIDR形式，例如：10.23.12.0/24（无类域间路由，24表示了地址中前缀的长度，范围为1~32）。 说明每个实例最多添加 1000个IP或IP段，即所有IP白名单分组内的IP或IP段总和不能超过1000。 当IP较多时，建议合并为IP段填入， 例如10.23.12.0/24。 |
|---|---|---|---|---|
| DBInstanceIPArr ayName | String | 否 | test | 需要修改的IP白名单分组名称，默认操作“Default”分组。 说明单个实例最多支持200 个白名单分组。 |
| DBInstanceIPArr ayAttribute | String | 否 | hidden | 白名单分组属性，默认为空。 说明控制台不显示带有 hidden属性的分组，带有该标签的分组通常是用于访问DTS等服务的。 |
| SecurityIPType | String | 否 | IPv4 | IP地址类型。 |
| SecurityGroupId | String | 否 | sg-xxxxxxx | 安全组ID。 |
| ModifyMode | String | 否 | Cover | 修改方式，取值： Cover：使用SecurityIps参数的值覆盖原IP白名单。 Append：在原IP白名单中增加SecurityIps参数中输入的IP地址。 Delete：在原IP白名单中删除SecurityIps参数中输入的IP地址。 至少需要保留一个IP地址。 默认值：Cover。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |
|---|---|---|---|
| TaskId | String | 115855279 | 任务ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifySecurityIps &DBInstanceId=rm-uf6wjk5xxxxxxx &SecurityIps=10.23.12.24
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifySecurityIpsResponse>
   <RequestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId>
   <TaskId>115855279</TaskId>
</ModifySecurityIpsResponse>
```

`JSON` 格式

```json
{
    "RequestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "TaskId": 115855279
}
```

#### 查询云盘加密状态及密钥详情

调用DescribeDBInstanceEncryptionKey查询RDS实例是否开启了云盘加密，以及密钥详情。 本接口支持MySQL、SQL Server、PostgreSQL实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceEncryptionKe y | 系统规定参数，取值：DescribeDBInstanceEncryptio nKey。 |
| DBInstanceId | String | 否 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances接口获取。 |
| EncryptionKey | String | 否 | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | 自定义密钥ID。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Creator | String | 1443*****9604 | 密钥的创建者。 |
| DeleteDate | String | 2022-05- 08T08:14:16Z | 预计删除密钥时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Description | String | Description of the key | 密钥描述。 |
| EncryptionKey | String | 5306d1b6-7fd3- 42d9-9511- xxxxxxx | 密钥ID。 |
| EncryptionKey Status | String | Enabled | 密钥的状态。取值： Enabled：启用 Disabled：未启用 |
| KeyUsage | String | ENCRYPT/DECRYPT | 密钥用途。 |
| MaterialExpire Time | String | 2021-10- 18T08:14:16Z | 密钥过期时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Origin | String | Aliyun KMS _ | 密钥的来源。 |
| RequestId | String | 3BC2768E-DEDA- 40FC-BBE9- 6B884F3626AF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceEncryptionKey &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeDBInstanceEncryptionKeyResponse>
      <Origin>Aliyun_KMS</Origin>
      <Description>Description of the key</Description>
      <EncryptionKeyStatus>Enabled</EncryptionKeyStatus>
      <RequestId>3BC2768E-DEDA-40FC-BBE9-6B884F3626AF</RequestId>
      <MaterialExpireTime>2021-10-18T08:14:16Z</MaterialExpireTime>
      <KeyUsage>ENCRYPT/DECRYPT</KeyUsage>
      <EncryptionKey>5306d1b6-7fd3-42d9-9511-xxxxxxx</EncryptionKey>
      <Creator>1443*****9604</Creator>
      <DeleteDate>2022-05-08T08:14:16Z</DeleteDate>
</DescribeDBInstanceEncryptionKeyResponse>
```

`JSON` 格式

```json
{
    "Origin": "Aliyun_KMS",
    "Description": "Description of the key",
    "EncryptionKeyStatus": "Enabled",
    "RequestId": "3BC2768E-DEDA-40FC-BBE9-6B884F3626AF",
    "MaterialExpireTime": "2021-10-18T08:14:16Z",
    "KeyUsage": "ENCRYPT/DECRYPT",
    "EncryptionKey": "5306d1b6-7fd3-42d9-9511-xxxxxxx",
    "Creator": "1443*****9604",
    "DeleteDate": "2022-05-08T08:14:16Z"
}
```

#### 设置分布式事务白名单

调用ModifyDTCSecurityIpHostsForSQLServer接口设置分布式事务白名单。 分布式事务白名单可以让ECS实例和RDS实例之间支持分布式事务。 仅适用于RDS SQL Server高可用系列（2012标准版、2012企业版、2014标准版、2016标准版、2016 企业版、2017标准版）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDTCSecur ityIpHostsForSQ LServer | 系统规定参数，取值：ModifyDTCSecurityIpHostsFor SQLServer。 |
| DBInstanceId | String | 是 | rm- uf6wjk5******** | RDS实例ID。 |
| SecurityIpHosts | String | 是 | 192.168.1.100,k 3ecstest | ECS实例的IP地址和Windows系统的计算机名。格式：ip,hostname。多个实例之间以英文分号（;）隔开。 |

云数据库RDS

| WhiteListGroupN ame | String | 是 | test1 | 白名单分组名称。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5******** | RDS实例ID。 |
| DTCSetResult | String | Success | 设置白名单的结果，取值： Success：设置成功 Fail：设置失败 |
| RequestId | String | 671B6D32-B907- 4EFF-A3B7- 94D2EAD5E3A3 | 请求ID。 |
| TaskId | String | 17896**** | 设置任务ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5******** &SecurityIpHosts=192.168.1.100,k3ecstest &WhiteListGroupName=test1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDTCSecurityIpHostsForSQLServerResponse>
  <RequestId>671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3</RequestId>
   <DBInstanceId>rm-uf6wjk5********</DBInstanceId>
   <DTCSetResult>Success</DTCSetResult>
   <TaskId>17896****</TaskId>
</ModifyDTCSecurityIpHostsForSQLServerResponse>
```

`JSON` 格式

```json
{
 "RequestId": "671B6D32-B907-4EFF-A3B7-94D2EAD5E3A3",
 "DBInstanceId": "rm-uf6wjk5********",
 "DTCSetResult": "Success",
 "TaskId": "17896****"
}
```

云数据库RDS

#### 查询分布式事务白名单

调用DescribeDTCSecurityIpHostsForSQLServer接口查询RDS实例的分布式事务白名单信息。 仅适用于RDS SQL Server高可用系列（2012标准版、2012企业版、2014标准版、2016标准版、2016 企业版、2017标准版）。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDTCSec urityIpHostsForS QLServer | 系统规定参数，取值：DescribeDTCSecurityIpHostsF orSQLServer。 |
| DBInstanceId | String | 是 | rm- uf6wjk5******** | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5******** | 实例ID。 |
| IpHostPairNum | String | 1 | 分布式事务白名单条目数。 |
| Items | Array of WhiteListGrou ps |  | 分布式事务白名单分组列表。 |
| WhiteListGrou ps |  |  |  |
| SecurityIpHost s | String | 192.168.1.100,k3e cstest | ECS实例的IP地址和Windows系统的计算机名。 格式：ip,hostname。多个实例之间以英文分号 （;）隔开。 |
| WhitelistGroup Name | String | test1 | 分布式事务白名单分组名称。 |
| RequestId | String | 2CA62A70-2203- 45C6-8E90- 8971D5ACC0C2 | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=DescribeDTCSecurityIpHostsForSQLServer &DBInstanceId=rm-uf6wjk5********
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDTCSecurityIpHostsForSQLServerResponse>
  <Items>
      <WhiteListGroups>
         <WhitelistGroupName>test1</WhitelistGroupName>
         <SecurityIpHosts>192.168.1.100,k3ecstest</SecurityIpHosts>
      </WhiteListGroups>
   </Items>
   <IpHostPairNum>1</IpHostPairNum>
   <RequestId>2CA62A70-2203-45C6-8E90-8971D5ACC0C2</RequestId>
</DescribeDTCSecurityIpHostsForSQLServerResponse>
```

`JSON` 格式

```json
{
 "Items": {
  "WhiteListGroups": [
   {
    "WhitelistGroupName": "test1",
    "SecurityIpHosts": "192.168.1.100,k3ecstest"
   }
```

]

```json
 },
 "IpHostPairNum": 1,
 "RequestId": "2CA62A70-2203-45C6-8E90-8971D5ACC0C2"
}
```

#### 查询SSL设置

调用DescribeDBInstanceSSL接口查询实例SSL设置。 该接口支持MySQL 5.6、MySQL 5.7高可用本地盘、MySQL 8.0高可用本地盘、SQL

**说明**

Server所有版本和PostgreSQL云盘版本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceSSL | 系统规定参数，取值：DescribeDBInstanceSSL。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConnectionStri ng | String | rm- uf6wjk5xxxxxx.mys ql.rds.aliyuncs.com | 受SSL保护的连接地址。 |
| SSLExpireTime | String | 2022-05- 08T08:14:16Z | SSL证书有效期。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| RequireUpdate | String | Yes | 是否需要更新。 MySQL或SQL Server时取值： No：不需要更新 Yes：需要更新 PostgreSQL时取值： 0：不需要更新 1：需要更新 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |
| RequireUpdate Reason | String | - | 该参数仅RDS PostgreSQL云盘版支持，表示需要更新证书的原因。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<ClientCertRevocationList>-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL-----</ ClientCertRevocationList> <RequestId>1AD222E9-E606-4A42-BF6D-8A4442913CEF</RequestId> <RequireUpdateItem>-</RequireUpdateItem> <CAType>aliyun</CAType> <LastModifyStatus>setting</LastModifyStatus> <ACL>cert</ACL> <RequireUpdate>Yes</RequireUpdate> <ModifyStatusReason>Modify DB Instance SSL Config.</ModifyStatusReason> <ClientCACertExpireTime>-</ClientCACertExpireTime> <ServerKey>-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----</ServerKey
```

>

```xml
<SSLExpireTime>2022-05-08T08:14:16Z</SSLExpireTime> <SSLCreateTime>-</SSLCreateTime> <ServerCert>-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----</ServerCer
```

`t>`

```xml
<SSLEnabled>on</SSLEnabled> <ClientCACert>-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----</Client CACert> <ReplicationACL>cert</ReplicationACL> <RequireUpdateReason>-</RequireUpdateReason> <ConnectionString>rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com</ConnectionString> <ServerCAUrl>-</ServerCAUrl>
```

`JSON` 格式

```json
{
    "ClientCertRevocationList": "-----BEGIN X509 CRL-----MIIB****19mg==-----END X509 CRL
-----",
    "RequestId": "1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "RequireUpdateItem": "-",
    "CAType": "aliyun",
    "LastModifyStatus": "setting",
    "ACL": "cert",
    "RequireUpdate": "Yes",
    "ModifyStatusReason": "Modify DB Instance SSL Config.",
    "ClientCACertExpireTime": "-",
    "ServerKey": "-----BEGIN PRIVATE KEY-----MIIE****ihfg==-----END PRIVATE KEY-----",
    "SSLExpireTime": "2022-05-08T08:14:16Z",
    "SSLCreateTime": "-",
    "ServerCert": "-----BEGIN CERTIFICATE-----MIID*****QqEP-----END CERTIFICATE-----",
    "SSLEnabled": "on",
    "ClientCACert": "-----BEGIN CERTIFICATE-----MIID*****viXk=-----END CERTIFICATE-----"
```

,

```json
    "ReplicationACL": "cert",
    "RequireUpdateReason": "-",
    "ConnectionString": "rm-uf6wjk5xxxxxx.mysql.rds.aliyuncs.com",
    "ServerCAUrl": "-"
}
```

#### 修改SSL设置

云数据库RDS 调用ModifyDBInstanceSSL接口修改实例SSL链路。 该接口用于为实例设置SSL（Secure Sockets Layer）加密。

**说明**

支持MySQL 5.6、MySQL 5.7高可用本地盘版、8.0高可用本地盘版、SQL Server所有版本和 PostgreSQL云盘版本。 读写分离地址不支持SSL加密。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eSSL | 系统规定参数，取值：ModifyDBInstanceSSL。 |
| ConnectionStrin g | String | 是 | rm- uf6wjk5xxxxx.m ysql.rds.aliyuncs .com | 需要创建或更新服务器证书的内网或外网连接地址。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| SSLEnabled | Integer | 否 | 1 | 开启或关闭SSL，取值： 1：开启 0：关闭 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceSSL &ConnectionString=rm-uf6wjk5xxxxx.mysql.rds.aliyuncs.com &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
}
```

#### 开启TDE

调用ModifyDBInstanceTDE接口开启RDS实例透明数据加密功能。 透明数据加密TDE可对数据文件执行实时I/O加密和解密，数据在写入磁盘之前进行加密，从磁盘读入内存时进行解密。 调用该接口时，实例必须满足以下条件，否则将操作失败： 已开通KMS。如果您未开通KMS，可在开通TDE过程中根据引导开通KMS。 实例类型为： MySQL 5.6 MySQL 5.7高可用版（本地SSD盘） SQL Server 2019标准版或SQL Server企业版

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eTDE | 系统规定参数，取值：ModifyDBInstanceTDE。 |
| DBInstanceId | String | 是 | rm-uf6wjk5**** | 实例ID。可调用DescribeDBInstances获取。 |
| TDEStatus | String | 是 | Enabled | TDE状态，取值： Enabled Disabled |
| DBName | String | 否 | testDB | 想要开启TDE的数据库名称，可以一次输入多个，以英文逗号（,）分隔，最多传入 50个。 说明此参数仅SQL Server 2019标准版和SQL Server企业版实例可用（必传）。 |
| EncryptionKey | String | 否 | 749c1df7-****- ****-****-**** | 自定义密钥ID。 说明仅MySQL实例可以传入此参数。 |

云数据库RDS

| RoleArn | String | 否 | acs:ram::14069 26****:role/aliyu nrdsinstanceenc ryptiondefaultrol e | 角色的全局资源描述符，用来指定具体角色。 说明仅MySQL实例可以传入此参数。 |
|---|---|---|---|---|
| EncryptAlgorith m | String | 否 | SM4 | TDE的加密方式。取值： SM4：通过国密方式加密。 AES 256 CBC：通过AES256的CBC _ _ 模式加密。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 777C4593-8053- 427B-99E2- 105593277CAB | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceTDE &DBInstanceId=rm-uf6wjk5**** &TDEStatus=Enabled
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceTDEResponse>
      <RequestId>777C4593-8053-427B-99E2-105593277CAB</RequestId>
</ModifyDBInstanceTDEResponse>
```

`JSON` 格式

```json
{
    "ModifyDBInstanceTDEResponse": {
        "RequestId": "777C4593-8053-427B-99E2-105593277CAB"
    }
}
```

#### 查询TDE设置

调用DescribeDBInstanceTDE接口查询实例数据加密状态。 该接口用于查看实例的透明数据加密TDE（Transparent Data Encryption）配置。 云数据库RDS 该接口只支持MySQL 5.6、SQL Server 2019标准版和SQL Server企业版实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceTDE | 系统规定参数，取值：DescribeDBInstanceTDE。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TDEStatus | String | Enabled | 实例级别的TDE状态，取值：Enabled \| Disabled |
| Databases | Array of Database |  | 数据库级别的TDE状态列表。 说明对于SQL Server 2019标准版和SQL Server企业版实例，可以在实例级别的TDE开启时，控制数据库级别的TDE 开启或关闭。 |
| Database |  |  |  |
| DBName | String | test02 | 数据库名称。 |
| TDEStatus | String | Enabled | 数据库级别的TDE状态，取值：Enabled \| Disabled |
| EncryptAlgorit hm | String | AES 256 CBC _ _ | TDE的加密方式。返回值： SM4：通过国密方式加密。 AES 256 CBC：通过AES256的CBC模式 _ _ 加密。 |
| RequestId | String | C816A4BF-A6EC- 4722-95F9- 2055859CCFD2 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceTDE &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceTDEResponse>
   <TDEStatus>Enabled</TDEStatus>
   <Databases>
      <DBName>test02</DBName>
      <TDEStatus>Enabled</TDEStatus>
   </Databases>
   <requestId>C816A4BF-A6EC-4722-95F9-2055859CCFD2</requestId>
</DescribeDBInstanceTDEResponse>
```

`JSON` 格式

```json
{
    "TDEStatus": "Enabled",
    "Databases": [
        {
            "DBName": "test02",
            "TDEStatus": "Enabled"
        }
```

`],`

```json
    "requestId": "C816A4BF-A6EC-4722-95F9-2055859CCFD2"
}
```

### 监控管理

#### 查询空间使用信息

调用DescribeResourceUsage接口查询RDS实例的空间使用信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeResourc eUsage | 系统规定参数，取值：DescribeResourceUsage。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
|---|---|---|---|
| Engine | String | MySQL | 数据库类型。 |
| DiskUsed | Long | 2337275904 | 已用空间（DataSize+LogSize），单位： Byte。-1表示没有数据。 |
| DataSize | Long | 1292094741 | 数据文件占用空间，单位：Byte。-1表示没有数据。 |
| LogSize | Long | 1045181163 | 日志占用空间，单位：Byte。-1表示没有数据。 |
| BackupSize | Long | 53002759 | 备份占用空间，单位：Byte。-1表示没有数据。 |
| ColdBackupSiz e | Long | 2337275904 | 冷备份的占用空间，单位：Byte。-1表示没有数据。 |
| SQLSize | Long | 315052751 | SQL的占用空间，单位：Byte。-1表示没有数据。 |
| BackupOssDat aSize | Long | 8821760 | OSS中备份集的数据文件大小，单位：Byte。0 表示没有数据。 |
| BackupOssLog Size | Long | 44180999 | OSS中备份集的日志文件大小，单位：Byte。0 表示没有数据。 |
| RequestId | String | F937E173-559C- 4498-8D90- 38D32342B9E4 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeResourceUsage &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeResourceUsageResponse>
  <PaidBackupSize>0</PaidBackupSize>
  <RequestId>28E73580-103C-4925-A48D-9A7E25F24297</RequestId>
  <BackupSize>51305057407</BackupSize>
  <ArchiveBackupSize>0</ArchiveBackupSize>
  <ColdBackupSize>-1</ColdBackupSize>
  <LogSize>2097152</LogSize>
  <BackupOssLogSize>48565375</BackupOssLogSize>
  <DBInstanceId> rm-uf6wjk5xxxxxxx</DBInstanceId>
  <BackupDataSize>51256492032</BackupDataSize>
  <DataSize>3198156800</DataSize>
  <BackupLogSize>48565375</BackupLogSize>
  <BackupOssDataSize>0</BackupOssDataSize>
  <SQLSize>446228522</SQLSize>
  <DiskUsed>3200253952</DiskUsed>
  <Engine>MySQL</Engine>
</DescribeResourceUsageResponse>
```

`JSON` 格式

```json
{
 "PaidBackupSize": 0,
 "RequestId": "28E73580-103C-4925-A48D-9A7E25F24297",
 "BackupSize": 51305057407,
 "ArchiveBackupSize": 0,
 "ColdBackupSize": -1,
 "LogSize": 2097152,
 "BackupOssLogSize": "48565375",
 "DBInstanceId": " rm-uf6wjk5xxxxxxx",
 "BackupDataSize": 51256492032,
 "DataSize": 3198156800,
 "BackupLogSize": 48565375,
 "BackupOssDataSize": "0",
 "SQLSize": 446228522,
 "DiskUsed": 3200253952,
 "Engine": "MySQL"
}
```

#### 查询性能数据

调用DescribeDBInstancePerformance接口查询实例性能数据。 根据性能参数查询某个实例、某时间段范围内的性能监控数据。根据版本、监控频率 （ModifyDBInstanceMonitor）和查询时间范围的不同，有如下几种输出形式： MySQL： 监控频率为5秒： 查询时间范围大于7天，数据粒度为1天； 查询时间范围大于1天，小于等于7天，数据粒度为1小时； 查询时间范围大于等于1小时，小于等于1天，数据粒度为1分钟； 查询时间范围小于1小时，数据粒度为5秒。 云数据库RDS 监控频率为60秒： 查询范围大于30天，数据粒度为1天； 查询范围大于7天小于等于30天，数据粒度为1小时； 查询范围小于等于7天，数据粒度为1分钟。 监控频率为300秒： 查询范围大于30天，数据粒度为1天； 查询范围大于7天小于等于30天，数据粒度为1小时； 查询范围小于等于7天，数据粒度为5分钟。 PostgreSQL本地盘和云盘版： 查询范围小于等于1小时，数据粒度为5秒； 查询范围小于等于2小时，数据粒度为10秒； 查询范围小于等于6小时，数据粒度为30秒； 查询范围小于等于12小时，数据粒度为1分钟； 查询范围小于等于1天，数据粒度为2分钟； 查询范围小于等于5天，数据粒度为10分钟； 查询范围小于等于15天，数据粒度为30分钟； 查询范围小于等于30天，数据粒度为1小时； 查询范围大于30天，数据粒度为1天。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta ncePerformance | 系统规定参数，取值：DescribeDBInstancePerforma nce。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| Key | String | 是 | MySQL Sessions _ | 想要查询的性能指标，多个值用英文逗号 （,）分隔，详细参数请参见本手册的性能参数表。 说明 Key为MySQL SpaceUsage或S _ QLServer SpaceUsage时，仅 _ 支持查询1天内的监控数据。 |
| StartTime | String | 是 | 2012-06- 08T15:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 说明开始和结束时间间隔需要大于您实例的监控频率，否则可能返回空列表。 |

云数据库RDS

| EndTime | String | 是 | 2012-06- 18T15:00Z | 查询结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 说明开始和结束时间间隔需要大于您实例的监控频率，否则可能返回空列表。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm- uf6wjk5xxxxxxxxxx | 实例ID。 |
| Engine | String | MySQL | 数据库类型。 |
| StartTime | String | 2012-06- 10T15:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 2012-06- 19T15:00Z | 查询结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PerformanceK eys | Array of PerformanceK ey |  | 实例性能参数列表。 |
| PerformanceK ey |  |  |  |
| Key | String | MySQL Sessions _ | 性能参数。 |
| Unit | String | KB | 数据单位。 |
| ValueFormat | String | recv k&sent k _ _ | 性能值的格式。如果性能值由多个参数构成， 以“&amp;”分隔，例如 com delete&amp;com insert&amp;com in _ _ _ sert select&amp;com replace。 _ _ |
| Values | Array of PerformanceV alue |  | 数组格式：{value1, value2, …}。 |
| PerformanceV alue |  |  |  |
| Value | String | 0.0&13.6 | 性能值。 |

云数据库RDS

| Date | String | 2011-05- 30T03:29:00Z | 记录日期。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstancePerformance &DBInstanceId= rm-uf6wjk5xxxxxxx &Key=MySQL_Sessions &StartTime=2012-06-08T15:00Z &EndTime=2012-06-18T15:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstancePerformanceResponse>
   <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
   <DBInstanceID> rm-uf6wjk5xxxxxxx</DBInstanceID>
   <StartTime>2012-06-11T15:00Z</StartTime>
   <EndTime>2013-10-17T15:00Z</EndTime>
   <Engine>MySQL</Engine>
   <PerformanceKeys>
      <PerformanceKey>
         <Key>MySQL_NetworkTraffic</Key>
         <Unit>KB</Unit>
         <ValueFormat>recv_k&amp;sent_k</ValueFormat>
         <Values></Values>
      </PerformanceKey>
   </PerformanceKeys>
</DescribeDBInstancePerformanceResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "DBInstanceID": " rm-uf6wjk5xxxxxxx",
    "StartTime": "2012-06-11T15:00Z",
    "EndTime": "2013-10-17T15:00Z",
    "Engine": "MySQL",
    "PerformanceKeys": {
        "PerformanceKey": [
            {
                "Key": "MySQL_NetworkTraffic",
                "Unit": "KB",
                "ValueFormat": "recv_k&sent_k",
                "Values": {
                    "PerformanceValue": []
                }
            }
```

]

```
    }
}
```

#### 查询监控频率

该接口不适用于PostgreSQL，PostgreSQL根据查询时间范围自适应时间粒度。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceMonitor | 系统规定参数，取值：DescribeDBInstanceMonitor。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Period | String | 60 | 监控的采集数据间隔，单位：秒。 |

云数据库RDS

| RequestId | String | 30829FD4-1A84- 4C2A-A625- 2EADECB95CA3 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstanceMonitorResponse>
   <period>60</period>
   <requestId>30829FD4-1A84-4C2A-A625-2EADECB95CA3</requestId>
</DescribeDBInstanceMonitorResponse>
```

`JSON` 格式

```json
{
    "period": "60",
    "requestId": "30829FD4-1A84-4C2A-A625-2EADECB95CA3"
}
```

#### 修改监控频率

阿里云对不同实例提供不同的监控频率，详情请参见**云数据库****RDS** > **用户指南**中的**设置监控频率**。 该接口不适用于PostgreSQL，PostgreSQL根据查询时间范围自适应时间粒度。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eMonitor | 系统规定参数，取值：ModifyDBInstanceMonitor。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |

云数据库RDS

| Period | String | 是 | 60 | 监控的采集间隔，取值： 5 10 60 300 单位：秒。 |
|---|---|---|---|---|
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 52B9805C-432C- 4ED1-83FD- 2F916B6D2733 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyDBInstanceMonitor &DBInstanceId=rm-uf6wjk5xxxxxxx &Period=60
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyDBInstanceMonitorResponse>
   <requestId>52B9805C-432C-4ED1-83FD-2F916B6D2733</requestId>
</ModifyDBInstanceMonitorResponse>
```

`JSON` 格式

```json
{
    "requestId": "52B9805C-432C-4ED1-83FD-2F916B6D2733"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstanceI d.NotFound | The DBInstanceId provided does not exist in our records. | 指定的实例不存在，请检查该实例是否存在，未被删除。 |

云数据库RDS

### 参数管理

#### 查询参数配置

调用DescribeParameters接口查询实例当前的参数配置。 该接口适用的实例如下： MySQL PostgreSQL PolarDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeParame ters | 系统规定参数，取值：DescribeParameters。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Engine | String | MySQL | 数据库类型。 |
| EngineVersion | String | 5.7 | 数据库版本号。 |
| RunningParam eters | Array of DBInstancePar ameter |  | 当前运行的参数列表。 |
| DBInstancePar ameter |  |  |  |
| ParameterNa me | String | fill factor | 参数名称。 |
| ParameterValu e | String | 0 | 参数值。 |

云数据库RDS

| ParameterDes cription | String | 此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。 | 参数描述。 |
|---|---|---|---|
| ConfigParamet ers | Array of DBInstancePar ameter |  | 正在同步的参数列表。修改并提交参数后，需要等待实例同步参数，同步结束后从此列表删除。 |
| DBInstancePar ameter |  |  |  |
| ParameterNa me | String | fill factor | 参数名称。 |
| ParameterValu e | String | 50 | 参数值。 |
| ParameterDes cription | String | 此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。 | 参数描述。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeParameters &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeParametersResponse>
   <ConfigParameters>
      <DBInstanceParameter>
```

`<ParameterDescription>`此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。`</ParameterDescription>`

```xml
         <ParameterName>fill factor</ParameterName>
         <ParameterValue>50</ParameterValue>
      </DBInstanceParameter>
   </ConfigParameters>
   <Engine>mssql</Engine>
   <EngineVersion>2008r2</EngineVersion>
   <RunningParameters>
      <DBInstanceParameter>
```

`<ParameterDescription>`此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。`</ParameterDescription>`

```xml
         <ParameterName>fill factor</ParameterName>
         <ParameterValue>0</ParameterValue>
      </DBInstanceParameter>
   </RunningParameters>
   <RequestId>2A748162-8040-4D6B-813E-6910C8C033F1</RequestId>
</DescribeParametersResponse>
```

`JSON` 格式

```json
{
  "ConfigParameters": {
      "DBInstanceParameter": [
          {
```

`"ParameterDescription": "`此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。`",`

```json
              "ParameterName": "fill factor",
              "ParameterValue": "50"
          }
```

]

```json
  },
  "Engine": "mysql",
  "EngineVersion": "5.7",
  "RunningParameters": {
      "DBInstanceParameter": [
          {
```

`"ParameterDescription": "`此选项设置服务器范围内的默认填充因子值。提供填充因子是为了优化索引数据存储和性能。`",`

```json
              "ParameterName": "fill factor",
              "ParameterValue": "0"
          }
```

]

```json
  },
  "RequestId": "2A748162-8040-4D6B-813E-6910C8C033F1"
}
```

#### 修改实例参数

云数据库RDS 调用ModifyParameter接口修改RDS实例参数。 您可以直接修改RDS实例的参数值，也可以通过参数模板修改。提交修改请求后，RDS将下发任务，将新修改的参数应用到实例，如果所提交的参数中有需要重启数据库的，RDS将重启数据库。 RDS会在执行任务前检查参数是否存在、是否可修改以及是否合法。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyParamete r | 系统规定参数，取值：ModifyParameter。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| Parameters | String | 否 | {"delayed insert _ timeout":"600", _ "max length for _ _ sort data":"204 _ _ 8"} | 参数及其值的JSON串，参数的值都是字符串类型。格式：{"参数名称1":"参数值 1","参数名称2":"参数值2"...} 说明传入该参数，则无需传入参数ParameterGroupId。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| Forcerestart | Boolean | 否 | false | 修改参数是否重启数据库，取值： true：强制重启（若修改的参数当中， 有需要重启的参数，则必须传入true， 否则修改将不生效）。 false：不强制重启。 默认值：false。 |
| ParameterGroup Id | String | 否 | rpg-xxxxxxxxx | 参数模板ID。 说明传入该参数，则无需传入参数Parameters。 如果应用参数模板需要重启实例，需要传入参数Forcerestart。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库RDS

| RequestId | String | 542BB8D6-4268- 45CC-A557- B03EFD7AB30A | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ModifyParameter &DBInstanceId=rm-uf6wjk5xxxxxxx &Parameters={"delayed_insert_timeout":"600","max_length_for_sort_data":"2048"}
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifyParameterResponse>
         <RequestId>542BB8D6-4268-45CC-A557-B03EFD7AB30A</RequestId>
</ModifyParameterResponse>
```

`JSON` 格式

```json
{
       "RequestId":"542BB8D6-4268-45CC-A557-B03EFD7AB30A"
}
```

#### 查询参数修改日志

调用DescribeModifyParameterLog接口查询RDS实例的参数修改日志。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeModifyP arameterLog | 系统规定参数，取值：DescribeModifyParameterLog 。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxx | 实例ID。 |
| StartTime | String | 是 | 2020-03- 01T00:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2020-03- 01T10:00Z | 查询结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |

云数据库RDS

| PageSize | Integer | 否 | 30 | 每页记录数。取值： 30 50 100 默认值：30。 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxx | 实例ID。 |
| Engine | String | mysql | 数据库类型。 |
| EngineVersion | String | 5.6 | 数据库版本。 |
| Items | Array of ParameterCha ngeLog |  | 日志记录列表。 |
| ParameterCha ngeLog |  |  |  |
| ModifyTime | String | 1584076066000 | 修改参数的Unix时间戳。单位：毫秒。 |
| NewParameter Value | String | 3 | 修改后参数值。 |
| OldParameter Value | String | 8 | 修改前参数值。 |
| ParameterNa me | String | innodb stats samp _ _ le pages _ | 参数名称。 |
| Status | String | Syncing | 状态。取值： Applied：已生效。 Syncing：正在应用，尚未生效。 |
| PageNumber | Integer | 1 | 页数。 |
| PageRecordCo unt | Integer | 1 | 每页记录数。 |

云数据库RDS

| RequestId | String | C8E88DED-533F- 4B3C-9207- 731FBF394CCA | 请求ID。 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 1 | 日志记录总数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeModifyParameterLog &DBInstanceId=rm-uf6wjk5xxxxx &StartTime=2020-03-01T00:00Z &EndTime=2020-03-01T10:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeModifyParameterLogResponse>
  <EngineVersion>5.6</EngineVersion>
  <Engine>mysql</Engine>
  <RequestId>C8E88DED-533F-4B3C-9207-731FBF394CCA</RequestId>
  <DBInstanceId>rm-uf6wjk5xxxxx</DBInstanceId>
  <PageNumber>1</PageNumber>
  <PageRecordCount>1</PageRecordCount>
  <TotalRecordCount>1</TotalRecordCount>
  <Items>
        <ParameterChangeLog>
              <Status>Syncing</Status>
              <ModifyTime>1584076066000</ModifyTime>
              <NewParameterValue>3</NewParameterValue>
              <OldParameterValue>8</OldParameterValue>
              <ParameterName>innodb_stats_sample_pages</ParameterName>
        </ParameterChangeLog>
  </Items>
</DescribeModifyParameterLogResponse>
```

`JSON` 格式云数据库RDS

```json
{"EngineVersion":"5.6",
   "Engine":"mysql",
   "RequestId":"C8E88DED-533F-4B3C-9207-731FBF394CCA",
   "DBInstanceId":"rm-uf6wjk5xxxxx",
   "PageNumber":"1",
   "PageRecordCount":"1",
   "TotalRecordCount":"1",
   "Items":
    {"ParameterChangeLog":
      [{"Status":"Syncing",
        "ModifyTime":"1584076066000",
        "NewParameterValue":"3",
        "OldParameterValue":"8",
        "ParameterName":"innodb_stats_sample_pages"}]}
   }
```

### 日志管理

#### 查询慢日志统计

**注意事项**

本接口仅支持MySQL引擎。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | DescribeSlowLogs | 系统规定参数。取值： DescribeSlowLogs |
| DBInstanc eId | Strin g | Query | 是 | REDLINE LOG STATISTIC _ _ S-rm-uf6wjk5**** | 实例ID。可调用 DescribeDBInstances获取。 |
| StartTime | Strin g | Query | 是 | 2025-05-17T16:00:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | Strin g | Query | 是 | 2025-05-18T16:00:00Z | 查询结束时间，需要大于查询开始时间，与查询开始时间间隔小于15天。格式： yyyy-MM- ddTHH:mmZ（UTC时间）。 |

云数据库RDS

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBName | Strin g | Query | 否 | testDB | 目标数据库名称。 |
| Engine | Strin g | Query | 否 | MySQL | 数据库类型。 该参数当前仅支持传入 MySQL值，且为必填参数。 |
| SortKey | Strin g | Query | 否 | TotalExecutionCounts | 排序依据，取值： TotalExecutionCoun ts ：总执行次数最多 TotalQueryTimes ：总执行时间最多 TotalLogicalRead s ：总逻辑读最多 TotalPhysicalRead s ：总物理读最多 |
| PageSize | Integ er | Query | 否 | 30 | 每页记录数，取值：30 ~100 。默认值：30 。 |
| PageNum ber | Integ er | Query | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Items | Array | { "ONLINE": 1， "OFFLINE": 9 } | 慢日志信息列表。 |
| -SlowLogId | Long | 26584213 | 慢查询汇总标识ID。 |
| -SQLId | Long | 1111 | SQL ID。 |
| -SQLHASH | String | U2FsdGVk**** | 慢日志明细里的SQL语句唯一标识符。 |
| -SQLIdStr | String | None | 对应的是慢日志统计模板SQL的ID，现已废弃， 请使用SQLHASH 。 |
| -DBName | String | testDB | 数据库名称。 |

| 云数据库RDS |  |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -SQLText | String | select sleep(2) | SQL命令详情。 |
| - MySQLTotalEx ecutionCounts | Long | 1 | MySQL执行次数（总值）。 |
| - MySQLTotalEx ecutionTimes | Long | 1 | MySQL执行时长（总值），单位：秒。 |
| - TotalLockTime s | Long | 0 | 锁定时长（总值），单位：秒。 |
| -MaxLockTime | Long | 0 | 锁定时长（最大值），单位：秒。 |
| - ParseTotalRow Counts | Long | 1 | 解析的SQL行数（总值）。 |
| - ParseMaxRow Count | Long | 1 | 解析的SQL行数（最大值）。 |
| - ReturnTotalRo wCounts | Long | 1 | 返回的SQL行数（总值）。 |
| - ReturnMaxRo wCount | Long | 1 | 返回的SQL行数（最大值）。 |
| -CreateTime | String | 2025-05- 18T12:11:04Z | 数据生成日期。 |
| - TotalLogicalRe adCounts | Long | 1 | 逻辑读次数（总值）。 |
| - TotalPhysicalR eadCounts | Long | 1 | 物理读次数（总值）。 |
| -ReportTime | String | 2025-05- 17T16:00:00Z | 运行报告生成时间。 |
| - MaxExecution Time | Long | 60 | 执行时长（最大值），单位：秒。 |
| - AvgExecutionT ime | Long | 1 | 执行时间（平均值），单位：秒。 |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | 请求ID。 |

| 开发指南·API参考 |  |  | 云数据库RD |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| DBInstanceId | String | REDLINE LOG STA _ _ TISTICS-rm- uf6wjk5**** | 实例ID。 |
| Engine | String | MySQL | 实例的数据库引擎。 |
| StartTime | String | 2025-05- 17T16:00:00Z | 查询开始时间。 |
| EndTime | String | 2025-05- 18T16:00:00Z | 查询结束时间。 |
| TotalRecordCo unt | Integer | 3 | 记录总数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 本页记录个数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSlowLogs &Action=DescribeSlowLogs &DBInstanceId=REDLINE_LOG_STATISTICS-rm-uf6wjk5**** &StartTime=2025-05-17T16:00Z &EndTime=2025-05-18T16:00Z
```

&公共请求参数正常返回示例 `JSON` 格式云数据库RDS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":3,
 "PageRecordCount":30,
 "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
 "EndTime":"2025-05-18T16:00:00Z",
 "DBInstanceId":"REDLINE_LOG_STATISTICS-rm-uf6wjk5****",
 "PageNumber":1,
 "StartTime":"2025-05-17T16:00:00Z",
 "Items":[
  {
   "MaxLockTime":0,
   "CreateTime":"2025-05-18T12:11:04Z",
   "SlowLogId":26584213,
   "TotalPhysicalReadCounts":1,
   "TotalLogicalReadCounts":1,
   "TotalLockTimes":0,
   "ReturnMaxRowCount":1,
   "AvgExecutionTime":1,
   "SQLText":"select sleep(2)",
   "ParseMaxRowCount":1,
   "MaxExecutionTime":60,
   "ReportTime":"2025-05-17T16:00:00Z",
   "SQLHASH":"U2FsdGVk****",
   "SQLIdStr":"None",
   "ReturnTotalRowCounts":1,
   "MySQLTotalExecutionCounts":1,
   "ParseTotalRowCounts":1,
   "DBName":"testDB",
   "SQLId":1111,
   "MySQLTotalExecutionTimes":1
  }
```

`],`

```json
 "Engine":"MySQL"
}
```

`XML` 格式云数据库RDS

```xml
<TotalRecordCount>3</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId> <EndTime>2025-05-18T16:00:00Z</EndTime> <DBInstanceId>REDLINE_LOG_STATISTICS-rm-uf6wjk5****</DBInstanceId> <PageNumber>1</PageNumber> <StartTime>2025-05-17T16:00:00Z</StartTime> <Items>
 <MaxLockTime>0</MaxLockTime>
 <CreateTime>2025-05-18T12:11:04Z</CreateTime>
 <SlowLogId>26584213</SlowLogId>
 <TotalPhysicalReadCounts>1</TotalPhysicalReadCounts>
 <TotalLogicalReadCounts>1</TotalLogicalReadCounts>
 <TotalLockTimes>0</TotalLockTimes>
 <ReturnMaxRowCount>1</ReturnMaxRowCount>
 <AvgExecutionTime>1</AvgExecutionTime>
 <SQLText>select sleep(2)</SQLText>
 <ParseMaxRowCount>1</ParseMaxRowCount>
 <MaxExecutionTime>60</MaxExecutionTime>
 <ReportTime>2025-05-17T16:00:00Z</ReportTime>
 <SQLHASH>U2FsdGVk****</SQLHASH>
 <SQLIdStr>None</SQLIdStr>
 <ReturnTotalRowCounts>1</ReturnTotalRowCounts>
 <MySQLTotalExecutionCounts>1</MySQLTotalExecutionCounts>
 <ParseTotalRowCounts>1</ParseTotalRowCounts>
 <DBName>testDB</DBName>
 <SQLId>1111</SQLId>
 <MySQLTotalExecutionTimes>1</MySQLTotalExecutionTimes>
</Items> <Engine>MySQL</Engine>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | Specified db does not exist or DB status does not support this operation. |
| 404 | InvalidEngine.NotF ound | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
| 400 | InvalidTask.NotFou nd | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatu s | OperationDenied.IncorrectTask Status | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationS tatus | OperationDenied.IncorrectMigr ationStatus | Migration status does not support this operation. |

| 云数据库RDS |  |  | 开发指南·API参考 |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidMigrationID. NotFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.P ayType | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotA ccess | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAc cess | No availble cluster. |
| 403 | IncorrectSQLLogAct iveStatus | OperationDenied.SQLLogActiv eStatus | The operation is not permitted due to SQLLogActive status. |
| 403 | InvalidClassicNetw ork.ValueNotSuppo rted | OperationDenied.ClassicNetwo rkNotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceS yncMode | OperationDenied.DBInstanceS yncMode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.R esource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvali d | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.Account NoFound | OperationDenied.AccountNoFo und | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUse Type.NotSupport | OperationDenied.DBInstanceU seTypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ LIMIT _ | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT _ | TIME RANGE OVER LIMIT.AUDI _ _ _ T | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT DOW _ _ NLOAD | TIME RANGE OVER LIMIT.AUDI _ _ _ T DOWNLOAD _ | search time range cannot be longer than 7 days for exporting files. |
| 400 | TIME RANGE OVER _ _ LIMIT.SLOW LOG _ _ | TIME RANGE OVER LIMIT.SLO _ _ _ W LOG _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.ERROR LOG _ _ | TIME RANGE OVER LIMIT.ERR _ _ _ OR LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWN _ _ LOAD REQUEST T _ _ O OSS _ | TOO MANY DOWNLOAD REQU _ _ _ EST TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUST _ _ ER DEACTIVATED _ | IGNITE LOG CLUSTER DEACTI _ _ _ VATED | backend app is upgrading, please try again later. |

|  | 开发指南·API参 | 考 |  | 云数据库RD | S |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IdempotenceParam NotMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSup port | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionN otFound | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkTyp e.NotSupport | ClassicNetworkType.NotSuppo rt | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswi tchId.NotSupported | InvalidVpcIdOrVswitchId.NotSu pported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion .NotSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Mal formed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotCl oudInstanceIp | InvalidCloudInstanceIp.NotFou nd | The specified cloud instance ip is not exist. |
| 400 | InvalidRetainInstan ce.Format | InvalidRestoreTime.Malformed | The specified retain instance is not valid. |
| 400 | InvalidRestoreTime .Format | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 404 | InvalidBackupSetID .NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotF ound | OperationDenied.NotFoundBac kup | The operation is not permitted due to no backup. |
| 403 | InvalidBackupSetId OrRestoreTime.Not Found | OperationDenied.NotFoundBac kupSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
| 403 | IncorrectBackupSet Method | OperationDenied.BackupMetho d | The operation is not permitted method of backup. |
| 403 | InvalidBackupLogSt atus | OperationDenied.BackupLogSt atus | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Dupli cate | OperationDenied.SecurityIPList Duplicate | The Specified same security IP already exists. |
| 403 | BackupSetDeleteN otSupport | OperationDenied.BackupSetDe leteNotSupport | The Specified backup does not support this operation. |

| 云数据库RDS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 25659 | InvalidRegion.ValueNotSupport ed | The specified parameter "Region" is not valid. |
|---|---|---|---|
| 403 | ReadDBInstanceEx ceeded | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS QUOTA ERR _ _ OR | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS TYPE ERROR _ _ | OperationDenied.PrimaryDBIns tanceType | The operation is not permitted due to type of primary instance. |
| 403 | LX RDS BIZ QUER _ _ _ Y INSTANCE ERRO _ _ R | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInsta nceId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | InvalidLogRetentio n | InvalidLogRetention.NotSuppor t | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceed ed | QuotaExceeded.Upload | The quota of file exceeds. |
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.M alformed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Mal formed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malfor med | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinsta nceNetType.ValueN otSupported | InvalidDBinstanceNetType.Val ueNotSupport | The specified parameter "DBinstanceNetType" is not valid. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | InvalidDBInstanceType.ValueN otSupport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidPageSize.Ma lformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod .Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersio n.Malformed | InvalidEngineVersion.ValueNot Support | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfo rmed | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupR etentionPeriod.Malf ormed | InvalidLogBackupRetentionPeri od.Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.D BInstanceType | IncorrectDBInstanceType.Child DBInstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSet State | OperationDenied.BackupStatu s | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupS etID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |
| 404 | OASBackupSetExtr actFinished | QuotaExceeded.BackupExtract Finished | The Specified OAS backup set had extracted finish. |
| 400 | OASExtractTimesE xceeded | QuotaExceeded.OASExtractTi mesExceeded | The Current DB Instance backup set had extracted too many times from OAS today. |
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceSto rage | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Form at | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInst anceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.Fo rmat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |

| RDS |  |  | ·API |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidFileName.No tFound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotCompleted | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Ma lformed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceN ame.Format | InvalidDBInstanceId.MalForme d | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAss ociate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintain Time | InvalidMaintainTime.MalForme d | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfo rmed | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST _ NOT NULL _ _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERRO _ R | PARAMETER ERROR _ | The parameter must not be null. |
| 404 | IntranetNetTypeNo tExists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mi smatch | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |
| 404 | InvalidVPCId.NotFo und | InvalidVPCId.NotFound | Specified VPC ID is not found. |
| 400 | InvalidVSwitchId.N otFound | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsR dsMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | VPC SYSTEM ERRO _ _ R | OperationDenied | VPC system error, please check params. |
| 400 | VPC CLOUD INSTA _ _ NCEIP USED _ | InvalidPrivateIpAddress.Duplic ated | Specified private IP address is duplicated. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Invalid.TargetCloud InstanceIp | InvalidPrivateIpAddress.Misma tch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceN etworkType | InvalidInstanceNetworkType.V alueNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanc eId.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |
| 400 | InvalidIzNo.NotSup ported | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.S witchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstanc e.ID | InvalidDBInstanceName.NotFo und | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExcee ded | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.N otFound | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | INST NOT BELONG _ _ TO USER _ _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26915 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | MissingParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX RDS BIZ INSTA _ _ _ NCE UPGRADE ER _ _ ROR | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClas sOrdbInstanceStor age.MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LX BARDS BIZ UP _ _ _ GRADE INSTANCE _ _ ERROR | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAG _ | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAGE _ _ ERROR | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26914 | InvaildDBInstanceClassInRegio n.NotAvailable | The DBInstanceClass in the Region is not available. |
| 403 | LX RDS BIZ STATU _ _ _ S ERROR _ | OperationDenied.DBInstanceSt atus | The operation is not permitted due to instance status. |
| 400 | ILLEGAL ARGUMEN _ T | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDatab aseUserName.Malf ormed | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.F ormat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |
| 400 | Abs.SourceDatabas ePort.Malformed | InvalidSourceDatabasePort.Mal formed | The specified parameter 'SourceDatabasePort' is not valid. |
| 400 | Abs.ImportDataTyp e.Malformed | InvalidImportDataType.Malfor med | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSup oort | OperationDenied.DBInstnceInR egion | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge .NotSupport | InvalidOrderCharge.NotSuppor t | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceU seType | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationI D | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | HaStatusNotSuppor t | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Ta gOnDBInstance | QuotaExceeded.TagOnDBInsta nce | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFo undag-Value is mismatch. |
| 400 | InvalidTag.1.key.M alformed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.M alformed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.M alformed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.M alformed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.M alformed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value. Malformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |
| 400 | InvalidTag.2.value. Malformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value. Malformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |
| 400 | InvalidTag.4.value. Malformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value. Malformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |
| 400 | TAG KEY ILLEGAL _ _ | Tag.Malformed | The specified parameter Tag is not valid. |
| 400 | TAG VALUE ILLEGA _ _ L | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExi st | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNot BeAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |

|  | 云数据库RDS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Tag.NoDBInstanceI dExist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBIns tanceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |
| 400 | Tag.TooManyTagsF orOneInstance | Tag.TooManyTagsForOneInsta nce | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtT woParamters | Tag.SetTagInfoAtTwoParamter s | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWi th.aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLon g | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLo ng | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPar amter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePeri od | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |
| 400 | Abs.InvalidStartTim e | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | Abs.InvalidEndTime | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSup port | OperationDenied.EnabledSSLN otSupport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.Not Finished | OperationDenied.RequestNotFi nished | The specified request not finished. |
| 403 | InvalidRequest.Exis ts | OperationDenied.RequestExist s | The specified request already exists. |
| 400 | Abs.instanceNames .Malformed | InvalidDBInstanceId.QuotaExc eeded | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.N otSupport | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |
| 400 | RenewChange.Exis t | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INVITATION CODE _ _ BIZ FAIL _ | InvalidEActionCode.CodeBizNo tSupported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26080 | InvalidEngine.VauleNotSupport ed | The specified parameter "Engine" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26063 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26035 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26036 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersio n.ValueNotSupport ed | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26062 | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClas s.NotFound | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ MissingParameter | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26037 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | InvalidDBInstanceS torage.ValueNotSu pported | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.dbInstanceNet Type.ValueNotSupp orted | InvalidDBInstanceNetType.Val ueNotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIF _ _ _ Y FAIL _ | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |
| 400 | QUERY PRICE RES _ _ PONSE ERROR _ | QueryPriceResonse.Failed | query price response error. |

|  | 云数据库RDS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LX CREATE ORDER _ _ FAILED _ | CreateOrder.Failed | Create order failed. |
| 404 | InvalidRegion.NotF ound | InvalidRegionId.NotFound | The provided RegionId does not exist. |
| 404 | INQUERY ORDER F _ _ EE FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.Not Found | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ NotFound _ | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26038 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | Abs.dbInstanceDes cription.Malformed | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26044 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26045 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26175 | InvaildEngineInRegion.NotAvail able | The engine type in this region is not available. |
| 403 | InvalidUserRegionP rivilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COM _ _ _ MODITY COUNT EX _ _ CEEDED LIMIT _ | QuotaExceeded.CreateInstanc e | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID _ _ _ ORDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |
| 403 | GET COMMODITY F _ _ AILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN _ _ 100 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge .NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.MissingOwnerI dOrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParam eter | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceC onnType.Format | InvalidDBInstanceConnType.Fo rmat | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPLis t.Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLo cation | InvalidBackupLocation.Malform ed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters. Format | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.Valu eNotSupported | The specified SQLCollectorStatus value not support. |
| 400 | InvalidSqlLog.Malfo rmed | InvalidSQLCollectorStatus.Malf ormed | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Sta rtDiagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 400 | InvalidDBInstanceD escription.Format | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Malfor med | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName. Format | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStat us.ValueNotSuppor ted | InvalidBackupStatus.ValueNot Support | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.Value NotSupported | InvalidBackupMode.ValueNotS upport | The specified parameter "BackupMode" is not valid. |
| 400 | Abs.InvalidDescript ion.Malformed | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.backupTime.Va lueNotSupported | InvalidPreferredBackupTime.M alformed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod. Malformed | InvalidPreferredBackupPeriod. Malformed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Malfor med | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExcee ded | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitE xceeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.F ormat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionM ode | InvalidConnectionMode.ValueN otSupported | The specified parameter "ConnectionMode" is not valid. |
| 400 | InvalidAccountPrivil ege.Malformed | InvalidAccountPrivilege.ValueN otSupport | The specified "AccountPrivilege" is not valid. |
| 400 | IncorrectEngineVer sion | InvaildEngineInRegion.ValueNo tSupported | The engine is not supported in the region. |
| 400 | InvalidDBName.For mat | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Du plicate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSe tName.Format | InvalidCharsetName.ValueNotS upport | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescriptio n.Format | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.For bid | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |

|  | 开发指南·API参 | 考 |  | 云数据库RD | S |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidUserType.No tSupport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime .Format | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |
| 400 | InvalidBackupMeth od.Format | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog. Malformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.Fo rmat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.For mat | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecords PerPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malf ormed | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod. Malformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malform ed | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malform ed | InvalidPerformanceKey.Malfor med | The specified parameter "Key" is not valid. |
| 400 | InvalidQueryKeywo rd.NotSupport | InvalidQueryKeyword.Malform ed | the query key contains exception character. |
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime. Malformed | The end time must be greater than the start time. |
| 400 | InvalidParameter.R esourceOwnerAcco unt | InvalidParameter.ResourceOw nerAccount | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.For mat | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenB ySubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |
| 403 | RAM.ApiNotSupport ed | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |

|  | 云数据库RDS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | RISK CONTROL RE _ _ SULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotS upport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |
| 403 | IncorrectDBInstanc eState | OperationDenied.DBInstanceSt atus | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstanc eType | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceN otSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstanc eEngine | OperationDenied.DBInstanceE ngine | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstanc eNetType | OperationDenied.DBInstanceN etType | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstanc eConnType | OperationDenied.PublicConnec tionExists | The specified public connection already existed. |
| 403 | InsufficientResourc eCapacity | OperationDenied | The resource is out of usage. |
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSu pport | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstanc e | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |
| 403 | IncorrectGuardDBI nstanceVersion | OperationDenied.GuardDBInst anceLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBI nstanceState | OperationDenied.MasterDBInst anceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountSt atus | OperationDenied.AccountStatu s | The operation is not permitted due to status of account. |
| 403 | IncorrectAccountTy pe | OperationDenied.AccountType | The operation is not permitted due to type of account. |

|  | 开发指南·API参 | 考 |  | 云数据库RD | S |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ConcurrentTaskExc eeded | OperationDenied.TaskExceede d | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstanc eAccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccou ntPrivilegeCount | OperationDenied.DBNameAnd AccountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWro ng | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExi sts | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod. ValueNotSupported | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Va lueNotSupported | InvalidBackupType.ValueNotSu pport | The specified parameter "BackupType" is not valid. |
| 404 | INSUFFICIENT BAL _ ANCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL I _ _ _ NSUFFICIENT BALA _ NCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | INSTANCE PRODUC _ E FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceN ame.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance. NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | RAM.InstanceNotFo und | Forbidden.InstanceNotFound | The specified instance is not found. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidConnectionS tring.Duplicate | InvalidConnectionStringPrefix. Duplicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTyp eExists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionS tringOrPort.Duplica te | InvalidConnectionString.Duplic ate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionS tring.NotFound | InvalidConnectionString.NotFo und | The specified connection string or network type is not found. |
| 404 | ConnectionStringLe ngthExceeded | ConnectionStringLengthExcee ded | The specified connection string is too long. |
| 404 | InvalidSecurityIPLis t.QuotaExceeded | InvalidSecurityIPListLength.Mal formed | The security IP address is not in the available range or occupied. |
| 404 | InvalidSecurityIPLis t.NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPLis t.Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceN etType.NotFound | InvalidDBInstanceNetType.Not Found | The specified instance network type is not found. |
| 403 | ChildDBInstanceExi sts | OperationDenied.ChildDBInsta nceExists | The specified instance had child instance. |
| 404 | GuardInstance.Exis t | InvalidGuardInstanceId.Exist | The guard instance has exist. |
| 404 | InvalidDBInstanceC lass.NotFound | InvalidDBInstanceClass.NotFou nd | The specified instance class is not found. |
| 404 | InvalidUser.NotFou nd | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPer mission.NotFound | InvalidOperatorPermission.Not Found | The permission provided does not exist. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account is not found. |

|  | 开发指南·API参 | 考 |  | 云数据库RD | S |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Invalid.Request | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unkown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unknown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -101 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -130 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 200 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 400 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 403 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |

#### 查看慢日志明细

调用DescribeSlowLogRecords接口查看实例的慢日志明细。

**注意事项**

云数据库RDS 慢日志明细至多查询1000条。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Query | 是 | rm-uf6wjk5**** | 实例ID。可调用 DescribeDBInstances获取。 |
| StartTime | Strin g | Query | 是 | 2025-05-17T16:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | Strin g | Query | 是 | 2025-05-18T16:00Z | 查询结束时间，需要大于查询开始时间，与查询开始时间间隔小于15天。格式： yyyy-MM- ddTHH:mmZ（UTC时间）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Items | Array | { "ONLINE": 1， "OFFLINE": 9 } | 慢日志信息列表。 |
| -HostAddress | String | rm-uf6wjk5**** [****] @ [100.14.XX.XX] | 连接数据库的客户端名称及地址。 |
| -DBName | String | testDB | 数据库名称。 |
| -SQLText | String | select sleep(2) | SQL命令详情。 |
| -QueryTimes | Long | 2 | 执行时长。单位：秒（s）。 |
| -QueryTimeMS | Long | 2001 | 执行时长。单位：毫秒（ms）。 |
| -LockTimes | Long | 0 | 锁定时长。单位：秒（s）。 |
| - ParseRowCoun ts | Long | 1 | 解析行数。 |

| 开发指南·API参考 |  |  | 云数据库RD |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ReturnRowCou nts | Long | 1 | 返回行数。 |
| - ExecutionStart Time | String | 2025-05- 18T01:40:44Z | 执行开始时间。 |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | 请求ID。 |
| DBInstanceId | String | rm-uf6wjk5**** | 实例ID。 |
| Engine | String | MySQL | 实例的数据库引擎。 |
| TotalRecordCo unt | Integer | 3 | 记录总数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 本页记录个数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSlowLogRecords &DBInstanceId=rm-uf6wjk5**** &StartTime=2025-05-17T16:00Z &EndTime=2025-05-18T16:00Z
```

&公共请求参数正常返回示例 `JSON` 格式云数据库RDS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":3,
 "PageRecordCount":1,
 "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828",
 "DBInstanceId":"rm-uf6wjk5****",
 "PageNumber":1,
 "Items":[
  {
   "QueryTimes":2,
   "ExecutionStartTime":"2025-05-18T01:40:44Z",
   "ReturnRowCounts":1,
   "LockTimes":0,
   "DBName":"testDB",
   "ParseRowCounts":1,
   "HostAddress":"rm-uf6wjk5****[****] @  [100.14.XX.XX]",
   "QueryTimeMS":2001,
   "SQLText":"select sleep(2)"
  }
```

`],`

```json
 "Engine":"MySQL"
}
```

`XML` 格式

```xml
<TotalRecordCount>3</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId> <DBInstanceId>rm-uf6wjk5****</DBInstanceId> <PageNumber>1</PageNumber> <Items>
 <QueryTimes>2</QueryTimes>
 <ExecutionStartTime>2025-05-18T01:40:44Z</ExecutionStartTime>
 <ReturnRowCounts>1</ReturnRowCounts>
 <LockTimes>0</LockTimes>
 <DBName>testDB</DBName>
 <ParseRowCounts>1</ParseRowCounts>
 <HostAddress>rm-uf6wjk5****[****] @  [100.14.XX.XX]</HostAddress>
 <QueryTimeMS>2001</QueryTimeMS>
 <SQLText>select sleep(2)</SQLText>
</Items> <Engine>MySQL</Engine>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | Specified db does not exist or DB status does not support this operation. |
| 404 | InvalidEngine.NotF ound | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
| 400 | InvalidTask.NotFou nd | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatu s | OperationDenied.IncorrectTask Status | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationS tatus | OperationDenied.IncorrectMigr ationStatus | Migration status does not support this operation. |
| 404 | InvalidMigrationID. NotFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.P ayType | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotA ccess | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAc cess | No availble cluster. |
| 403 | IncorrectSQLLogAct iveStatus | OperationDenied.SQLLogActiv eStatus | The operation is not permitted due to SQLLogActive status. |
| 403 | InvalidClassicNetw ork.ValueNotSuppo rted | OperationDenied.ClassicNetwo rkNotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceS yncMode | OperationDenied.DBInstanceS yncMode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.R esource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvali d | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.Account NoFound | OperationDenied.AccountNoFo und | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUse Type.NotSupport | OperationDenied.DBInstanceU seTypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ LIMIT _ | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT _ | TIME RANGE OVER LIMIT.AUDI _ _ _ T | search time range cannot be longer than 7 days. |

|  | 云数据库RDS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TIME RANGE OVER _ _ LIMIT.AUDIT DOW _ _ NLOAD | TIME RANGE OVER LIMIT.AUDI _ _ _ T DOWNLOAD _ | search time range cannot be longer than 7 days for exporting files. |
| 400 | TIME RANGE OVER _ _ LIMIT.SLOW LOG _ _ | TIME RANGE OVER LIMIT.SLO _ _ _ W LOG _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ LIMIT.ERROR LOG _ _ | TIME RANGE OVER LIMIT.ERR _ _ _ OR LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWN _ _ LOAD REQUEST T _ _ O OSS _ | TOO MANY DOWNLOAD REQU _ _ _ EST TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUST _ _ ER DEACTIVATED _ | IGNITE LOG CLUSTER DEACTI _ _ _ VATED | backend app is upgrading, please try again later. |
| 400 | IdempotenceParam NotMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSup port | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionN otFound | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkTyp e.NotSupport | ClassicNetworkType.NotSuppo rt | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswi tchId.NotSupported | InvalidVpcIdOrVswitchId.NotSu pported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion .NotSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.N otSupported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Mal formed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotCl oudInstanceIp | InvalidCloudInstanceIp.NotFou nd | The specified cloud instance ip is not exist. |
| 400 | InvalidRetainInstan ce.Format | InvalidRestoreTime.Malformed | The specified retain instance is not valid. |
| 400 | InvalidRestoreTime .Format | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 404 | InvalidBackupSetID .NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotF ound | OperationDenied.NotFoundBac kup | The operation is not permitted due to no backup. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 403 | InvalidBackupSetId OrRestoreTime.Not Found | OperationDenied.NotFoundBac kupSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
|---|---|---|---|
| 403 | IncorrectBackupSet Method | OperationDenied.BackupMetho d | The operation is not permitted method of backup. |
| 403 | InvalidBackupLogSt atus | OperationDenied.BackupLogSt atus | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Dupli cate | OperationDenied.SecurityIPList Duplicate | The Specified same security IP already exists. |
| 403 | BackupSetDeleteN otSupport | OperationDenied.BackupSetDe leteNotSupport | The Specified backup does not support this operation. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 25659 | InvalidRegion.ValueNotSupport ed | The specified parameter "Region" is not valid. |
| 403 | ReadDBInstanceEx ceeded | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS QUOTA ERR _ _ OR | QuotaExceeded.ReadonlyDBIn stanceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAI _ _ _ NRDS TYPE ERROR _ _ | OperationDenied.PrimaryDBIns tanceType | The operation is not permitted due to type of primary instance. |
| 403 | LX RDS BIZ QUER _ _ _ Y INSTANCE ERRO _ _ R | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInsta nceId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | InvalidLogRetentio n | InvalidLogRetention.NotSuppor t | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceed ed | QuotaExceeded.Upload | The quota of file exceeds. |
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.M alformed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Mal formed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malfor med | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinsta nceNetType.ValueN otSupported | InvalidDBinstanceNetType.Val ueNotSupport | The specified parameter "DBinstanceNetType" is not valid. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | InvalidDBInstanceType.ValueN otSupport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidPageSize.Ma lformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod .Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersio n.Malformed | InvalidEngineVersion.ValueNot Support | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfo rmed | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupR etentionPeriod.Malf ormed | InvalidLogBackupRetentionPeri od.Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.D BInstanceType | IncorrectDBInstanceType.Child DBInstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSet State | OperationDenied.BackupStatu s | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupS etID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |
| 404 | OASBackupSetExtr actFinished | QuotaExceeded.BackupExtract Finished | The Specified OAS backup set had extracted finish. |
| 400 | OASExtractTimesE xceeded | QuotaExceeded.OASExtractTi mesExceeded | The Current DB Instance backup set had extracted too many times from OAS today. |

|  | 开发指南·API参 | 考 |  | 云数据库RD | S |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceSto rage | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Form at | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInst anceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.Fo rmat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |
| 404 | InvalidFileName.No tFound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotCompleted | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Ma lformed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceN ame.Format | InvalidDBInstanceId.MalForme d | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAss ociate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintain Time | InvalidMaintainTime.MalForme d | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfo rmed | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST _ NOT NULL _ _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERRO _ R | PARAMETER ERROR _ | The parameter must not be null. |
| 404 | IntranetNetTypeNo tExists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mi smatch | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |

| 云数据库RDS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 404 | InvalidVPCId.NotFo und | InvalidVPCId.NotFound | Specified VPC ID is not found. |
|---|---|---|---|
| 400 | InvalidVSwitchId.N otFound | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsR dsMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | VPC SYSTEM ERRO _ _ R | OperationDenied | VPC system error, please check params. |
| 400 | VPC CLOUD INSTA _ _ NCEIP USED _ | InvalidPrivateIpAddress.Duplic ated | Specified private IP address is duplicated. |
| 400 | Invalid.TargetCloud InstanceIp | InvalidPrivateIpAddress.Misma tch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceN etworkType | InvalidInstanceNetworkType.V alueNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanc eId.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |
| 400 | InvalidIzNo.NotSup ported | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.S witchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstanc e.ID | InvalidDBInstanceName.NotFo und | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExcee ded | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.N otFound | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | INST NOT BELONG _ _ TO USER _ _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26915 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 400 | MissingParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
|---|---|---|---|
| 400 | LX RDS BIZ INSTA _ _ _ NCE UPGRADE ER _ _ ROR | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClas sOrdbInstanceStor age.MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX BARDS BIZ UP _ _ _ GRADE INSTANCE _ _ ERROR | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedT ype.ValueNotSuppo rted | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAG _ | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UP _ _ _ GRADE STORAGE _ _ ERROR | OperationDenied.DBInstanceSt orageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26914 | InvaildDBInstanceClassInRegio n.NotAvailable | The DBInstanceClass in the Region is not available. |
| 403 | LX RDS BIZ STATU _ _ _ S ERROR _ | OperationDenied.DBInstanceSt atus | The operation is not permitted due to instance status. |
| 400 | ILLEGAL ARGUMEN _ T | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDatab aseUserName.Malf ormed | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.F ormat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |
| 400 | Abs.SourceDatabas ePort.Malformed | InvalidSourceDatabasePort.Mal formed | The specified parameter 'SourceDatabasePort' is not valid. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.ImportDataTyp e.Malformed | InvalidImportDataType.Malfor med | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSup oort | OperationDenied.DBInstnceInR egion | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge .NotSupport | InvalidOrderCharge.NotSuppor t | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceU seType | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationI D | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |
| 403 | HaStatusNotSuppor t | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Ta gOnDBInstance | QuotaExceeded.TagOnDBInsta nce | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFo undag-Value is mismatch. |
| 400 | InvalidTag.1.key.M alformed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.M alformed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.M alformed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.M alformed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.M alformed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value. Malformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |
| 400 | InvalidTag.2.value. Malformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value. Malformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |
| 400 | InvalidTag.4.value. Malformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value. Malformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |

| 400 | TAG KEY ILLEGAL _ _ | Tag.Malformed | The specified parameter Tag is not valid. |
|---|---|---|---|
| 400 | TAG VALUE ILLEGA _ _ L | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExi st | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNot BeAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |
| 400 | Tag.NoDBInstanceI dExist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBIns tanceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |
| 400 | Tag.TooManyTagsF orOneInstance | Tag.TooManyTagsForOneInsta nce | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtT woParamters | Tag.SetTagInfoAtTwoParamter s | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWi th.aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLon g | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLo ng | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPar amter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePeri od | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |
| 400 | Abs.InvalidStartTim e | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidEndTime | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSup port | OperationDenied.EnabledSSLN otSupport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.Not Finished | OperationDenied.RequestNotFi nished | The specified request not finished. |
| 403 | InvalidRequest.Exis ts | OperationDenied.RequestExist s | The specified request already exists. |
| 400 | Abs.instanceNames .Malformed | InvalidDBInstanceId.QuotaExc eeded | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.N otSupport | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |
| 400 | RenewChange.Exis t | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |
| 400 | INVITATION CODE _ _ BIZ FAIL _ | InvalidEActionCode.CodeBizNo tSupported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26080 | InvalidEngine.VauleNotSupport ed | The specified parameter "Engine" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26063 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26035 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26036 | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersio n.ValueNotSupport ed | InvalidEngineVersion.ValueNot Supported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26062 | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClas s.NotFound | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ MissingParameter | InvalidDBInstanceClass.ValueN otSupported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26037 | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBInstanceS torage.ValueNotSu pported | InvalidDBInstanceStorage.Valu eNotSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.dbInstanceNet Type.ValueNotSupp orted | InvalidDBInstanceNetType.Val ueNotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIF _ _ _ Y FAIL _ | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |
| 400 | QUERY PRICE RES _ _ PONSE ERROR _ | QueryPriceResonse.Failed | query price response error. |
| 400 | LX CREATE ORDER _ _ FAILED _ | CreateOrder.Failed | Create order failed. |
| 404 | InvalidRegion.NotF ound | InvalidRegionId.NotFound | The provided RegionId does not exist. |
| 404 | INQUERY ORDER F _ _ EE FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.Not Found | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ NotFound _ | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26038 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | Abs.dbInstanceDes cription.Malformed | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26044 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26045 | InvalidEngineVersionInRegion. NotAvailable | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL _ _ _ 26175 | InvaildEngineInRegion.NotAvail able | The engine type in this region is not available. |

云数据库RDS

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidUserRegionP rivilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COM _ _ _ MODITY COUNT EX _ _ CEEDED LIMIT _ | QuotaExceeded.CreateInstanc e | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID _ _ _ ORDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |
| 403 | GET COMMODITY F _ _ AILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN _ _ 100 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge .NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |
| 400 | Abs.MissingOwnerI dOrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParam eter | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceC onnType.Format | InvalidDBInstanceConnType.Fo rmat | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPLis t.Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLo cation | InvalidBackupLocation.Malform ed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters. Format | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.Valu eNotSupported | The specified SQLCollectorStatus value not support. |
| 400 | InvalidSqlLog.Malfo rmed | InvalidSQLCollectorStatus.Malf ormed | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Sta rtDiagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 400 | InvalidDBInstanceD escription.Format | InvalidDBInstanceDescription. Malformed | The specified parameter "DBInstanceDescription" is not valid. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Malfor med | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName. Format | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStat us.ValueNotSuppor ted | InvalidBackupStatus.ValueNot Support | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.Value NotSupported | InvalidBackupMode.ValueNotS upport | The specified parameter "BackupMode" is not valid. |
| 400 | Abs.InvalidDescript ion.Malformed | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | Abs.backupTime.Va lueNotSupported | InvalidPreferredBackupTime.M alformed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod. Malformed | InvalidPreferredBackupPeriod. Malformed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Malfor med | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExcee ded | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitE xceeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.F ormat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionM ode | InvalidConnectionMode.ValueN otSupported | The specified parameter "ConnectionMode" is not valid. |
| 400 | InvalidAccountPrivil ege.Malformed | InvalidAccountPrivilege.ValueN otSupport | The specified "AccountPrivilege" is not valid. |
| 400 | IncorrectEngineVer sion | InvaildEngineInRegion.ValueNo tSupported | The engine is not supported in the region. |

| RDS |  |  | ·API |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBName.For mat | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Du plicate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSe tName.Format | InvalidCharsetName.ValueNotS upport | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescriptio n.Format | InvalidDBDescription.Malforme d | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.For bid | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |
| 400 | InvalidUserType.No tSupport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime .Format | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |
| 400 | InvalidBackupMeth od.Format | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog. Malformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.Fo rmat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.For mat | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecords PerPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malf ormed | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod. Malformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malform ed | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malform ed | InvalidPerformanceKey.Malfor med | The specified parameter "Key" is not valid. |
| 400 | InvalidQueryKeywo rd.NotSupport | InvalidQueryKeyword.Malform ed | the query key contains exception character. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime. Malformed | The end time must be greater than the start time. |
| 400 | InvalidParameter.R esourceOwnerAcco unt | InvalidParameter.ResourceOw nerAccount | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.For mat | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenB ySubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |
| 403 | RAM.ApiNotSupport ed | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |
| 403 | RISK CONTROL RE _ _ SULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotS upport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |
| 403 | IncorrectDBInstanc eState | OperationDenied.DBInstanceSt atus | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstanc eType | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceN otSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNo tSupport | OperationDenied.DBInstanceT ype | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstanc eEngine | OperationDenied.DBInstanceE ngine | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstanc eNetType | OperationDenied.DBInstanceN etType | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstanc eConnType | OperationDenied.PublicConnec tionExists | The specified public connection already existed. |
| 403 | InsufficientResourc eCapacity | OperationDenied | The resource is out of usage. |

|  | 云数据库RDS |  |  | 开发指南·API参考 |  |
|---|---|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSu pport | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstanc e | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |
| 403 | IncorrectGuardDBI nstanceVersion | OperationDenied.GuardDBInst anceLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBI nstanceState | OperationDenied.MasterDBInst anceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountSt atus | OperationDenied.AccountStatu s | The operation is not permitted due to status of account. |
| 403 | IncorrectAccountTy pe | OperationDenied.AccountType | The operation is not permitted due to type of account. |
| 403 | ConcurrentTaskExc eeded | OperationDenied.TaskExceede d | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstanc eAccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccou ntPrivilegeCount | OperationDenied.DBNameAnd AccountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWro ng | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExi sts | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod. ValueNotSupported | InvalidBackupMethod.ValueNot Support | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Va lueNotSupported | InvalidBackupType.ValueNotSu pport | The specified parameter "BackupType" is not valid. |
| 404 | INSUFFICIENT BAL _ ANCE | InsufficientBalance | Your account does not have enough balance. |
| 400 | FUWU BIZ COMMO _ _ DITY VERIFY FAIL I _ _ _ NSUFFICIENT BALA _ NCE | InsufficientBalance | Your account does not have enough balance. |

| ·API |  |  | RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | INSTANCE PRODUC _ E FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceN ame.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFoun d | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance. NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | RAM.InstanceNotFo und | Forbidden.InstanceNotFound | The specified instance is not found. |
| 404 | InvalidConnectionS tring.Duplicate | InvalidConnectionStringPrefix. Duplicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTyp eExists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionS tringOrPort.Duplica te | InvalidConnectionString.Duplic ate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionS tring.NotFound | InvalidConnectionString.NotFo und | The specified connection string or network type is not found. |
| 404 | ConnectionStringLe ngthExceeded | ConnectionStringLengthExcee ded | The specified connection string is too long. |
| 404 | InvalidSecurityIPLis t.QuotaExceeded | InvalidSecurityIPListLength.Mal formed | The security IP address is not in the available range or occupied. |
| 404 | InvalidSecurityIPLis t.NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPLis t.Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceN etType.NotFound | InvalidDBInstanceNetType.Not Found | The specified instance network type is not found. |
| 403 | ChildDBInstanceExi sts | OperationDenied.ChildDBInsta nceExists | The specified instance had child instance. |
| 404 | GuardInstance.Exis t | InvalidGuardInstanceId.Exist | The guard instance has exist. |

| 云数据库RDS |  |  | 开发指南·API参考 |
|---|---|---|---|
| HttpCo de | 错误码 | 错误信息 | 描述 |
| 404 | InvalidDBInstanceC lass.NotFound | InvalidDBInstanceClass.NotFou nd | The specified instance class is not found. |
| 404 | InvalidUser.NotFou nd | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPer mission.NotFound | InvalidOperatorPermission.Not Found | The permission provided does not exist. |
| 404 | InvalidDBName.Not Found | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |
| 404 | InvalidAccountNam e.NotFound | InvalidAccountName.NotFound | The specified account is not found. |
| 500 | Invalid.Request | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unkown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unknown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -101 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -130 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 200 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 400 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 403 | InternalError | The request processing has failed due to some unknown error, exception or failure. |

| 开发指南·API参 | 考 |  | 云数据库RD |
|---|---|---|---|

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |

#### 查询错误日志

调用DescribeErrorLogs接口查询实例某段时间内的错误日志。 错误日志包含具体的错误信息和错误日志生成时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeErrorLo gs | 系统规定参数，取值：DescribeErrorLogs。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| EndTime | String | 是 | 2011-05- 30T20:10Z | 查询结束时间，大于查询开始时间，与查询开始时间间隔小于31天。格式：yyyy- MM-ddTHH:mmZ（UTC时间）。 |
| StartTime | String | 是 | 2011-05- 01T20:10Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30~100。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | 总记录数。 |

云数据库RDS

| PageNumber | Integer | 1 | 页码。 |
|---|---|---|---|
| PageRecordCo unt | Integer | 30 | 本页错误日志个数。 |
| Items | Array of ErrorLog |  | 错误日志明细列表。 |
| ErrorLog |  |  |  |
| ErrorInfo | String | spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informational message only; no user action is required | 错误日志信息。 |
| CreateTime | String | 2011-05- 30T12:11:04Z | 错误日志生成时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| RequestId | String | 98504E07-BB0E- 40FC-B152- E4882615812C | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeErrorLogs &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-05-01T20:10Z &EndTime=2011-05-30T20:10Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeErrorLogsResponse>
   <RequestId>98504E07-BB0E-40FC-B152-E4882615812C</RequestId>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <PageRecordCount>1</PageRecordCount>
   <Items>
      <ErrorLog>
         <ErrorInfo>spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an i
nformational message only; no user action is required</ErrorInfo>
         <CreateTime>2013-06-04T15:00:00</CreateTime>
      </ErrorLog>
      </Items>
</DescribeErrorLogsResponse>
```

云数据库RDS `JSON` 格式

```json
{ "RequestId":"98504E07-BB0E-40FC-B152-E4882615812C", "PageNumber":1, "TotalRecordCount":1, "PageRecordCount":1, "Items": {"ErrorLog":
```

[

```json
{ "ErrorInfo":"spid52 DBCC TRACEON 3499, server process ID (SPID) 52. This is an informat ional message only; no user action is required", "CreateTime":"2013-06-04T15:00:00" }
```

]

```
} }
```

#### 查询Binlog日志

当**DownloadLink**为NULL时，表示RDS没有提供下载链接URL； 当**DownloadLink**不为NULL时，用户可以根据此URL下载备份文件，此URL已设置过期时间**LinkExpiredTime**，请在过期时间之前下载。 返回的日志列表为日志记录结束时间在查询开始时间之后，并且日志记录开始时间在查询结束时间之前的所有日志，即LogEndTime>=StartTime and LogBeginTime<=EndTime。 本接口不适用于SQL Server实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBinlogFi les | 系统规定参数，取值：DescribeBinlogFiles。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| EndTime | String | 是 | 2011-06- 20T15:00:00Z | 查询结束时间，大于查询开始时间。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| StartTime | String | 是 | 2011-06- 01T15:00:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30~100。默认值：30。 |

云数据库RDS

| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | Binlog文件总数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 当前页Binlog文件个数。 |
| Items | Array of BinLogFile |  | Binlog明细列表。 |
| BinLogFile |  |  |  |
| FileSize | Long | 2269410 | Binlog文件大小，单位：Byte。 |
| LogBeginTime | String | 2019-02- 09T17:45:21Z | Binlog文件记录的开始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| LogEndTime | String | 2019-02- 15T13:10:28Z | Binlog文件记录的结束时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DownloadLink | String | http://rdsxxxxx.oss. aliyuncs.com/xxxx xx | 支持HTTP协议的下载链接URL，NULL表示没有下载链接。 |
| HostInstanceI D | String | 5841973 | Binlog所在实例编号，用户区分该Binlog日志产生于主实例或备实例。 |
| LinkExpiredTi me | String | 2013-06- 09T18:00:00Z | URL过期时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Checksum | String | 183583043934687 01857 | 校验和。 |
| IntranetDownl oadLink | String | http://rdslog-hz- v3.oss-cn- hangzhou- internal.aliyuncs.co m/xxxxxx | 内网下载链接URL。 |
| LogFileName | String | 000000040000000 000000019 | Binlog文件名称。 |

云数据库RDS

| RequestId | String | ED169A3E-1657- 4104-82AB- 24EA8CD0DB75 | 请求ID。 |
|---|---|---|---|
| TotalFileSize | Long | 2269410 | Binlog文件总大小。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeBinlogFiles &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-20T15:00:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeBinlogFilesResponse>
   <Items></Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>0</TotalRecordCount>
   <TotalFileSize>0</TotalFileSize>
   <RequestId>ED169A3E-1657-4104-82AB-24EA8CD0DB75</RequestId>
   <PageRecordCount>0</PageRecordCount>
</DescribeBinlogFilesResponse>
```

`JSON` 格式

```json
{
 "Items": {
  "BinLogFile": []
 },
 "PageNumber": 1,
 "TotalRecordCount": 0,
 "TotalFileSize": "0",
 "RequestId": "ED169A3E-1657-4104-82AB-24EA8CD0DB75",
 "PageRecordCount": 0
}
```

#### 查询SQL洞察（SQL审计）状态

调用DescribeSQLCollectorPolicy接口查询RDS实例的SQL洞察（SQL审计）功能是否开启。 支持的实例版本如下： MySQL PostgreSQL PolarDB 云数据库RDS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSQLColl ectorPolicy | 系统规定参数，取值：DescribeSQLCollectorPolicy。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| SQLCollectorSt atus | String | Enable | SQL洞察（SQL审计）开启情况，取值： Enable：开启 Disabled：关闭 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |
| StoragePeriod | Integer | 0 | 无 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSQLCollectorPolicyResponse>
   <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
   <SQLCollectorStatus>Enable</SQLCollectorStatus></DescribeSQLCollectorPolicyResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
    "SQLCollectorStatus": "Enable"
}
```

#### 开关SQL洞察（SQL审计）

调用ModifySQLCollectorPolicy接口开启或关闭实例的SQL洞察（SQL审计）功能。 支持的实例版本如下： MySQL PostgreSQL PolarDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifySQLCollec torPolicy | 系统规定参数，取值：ModifySQLCollectorPolicy。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| SQLCollectorStat us | String | 是 | Enable | 开启或关闭SQL洞察（SQL审计），取值：Enable \| Disabled |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| StoragePeriod | Integer | 否 | 0 | 无效参数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例云数据库RDS

```
http(s)://rds.example.com/?Action=ModifySQLCollectorPolicy &DBInstanceId=rm-uf6wjk5xxxxxxx &SQLCollectorStatus=Enable
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ModifySQLCollectorPolicyResponse>
   <requestId>C3565F9F-76E9-4F7E-A662-D1B2488EC2FC</requestId>
</ModifySQLCollectorPolicyResponse>
```

`JSON` 格式

```json
{
    "requestId": "C3565F9F-76E9-4F7E-A662-D1B2488EC2FC",
}
```

#### 查询SQL洞察（SQL审计）日志

调用DescribeSQLLogRecords接口查询实例的SQL洞察（SQL审计）日志。 支持的实例如下： MySQL PostgreSQL PolarDB

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSQLLog Records | 系统规定参数，取值：DescribeSQLLogRecords。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| EndTime | String | 是 | 2011-06- 11T15:00:00Z | 查询结束时间，大于查询开始时间，与查询开始时间间隔小于31天。格式：yyyy- MM-ddTHH:mm:ssZ（UTC时间）。 |
| StartTime | String | 是 | 2011-06- 01T15:00:00Z | 查询开始时间，格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

云数据库RDS

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|
| SQLId | Long | 否 | 25623548 | SQL语句唯一标识ID。 |
| QueryKeywords | String | 否 | rds | 用于查询的关键字，多个关键字以空格分隔，不超过10个关键字。 |
| Database | String | 否 | Database | 数据库名称。默认为所有数据库，也可以输入数据库名称查询，一次只能输入一个。 |
| User | String | 否 | user | 用户名称。默认为所有用户，也可以输入用户名称查询，一次只能输入一个。 |
| Form | String | 否 | Stream | 触发审计文件的生成或者返回SQL记录列表，取值： File：若传入这个值，则触发审计文件的生成，只返回公共参数，需再调用 DescribeSQLLogFiles接口获取文件的最终下载地址。 Stream：默认值，返回SQL记录列表。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30~100。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 100 | 总记录数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 本页SQL审计日志个数。 |

云数据库RDS

| Items | Array of SQLRecord |  | SQL审计日志列表。 |
|---|---|---|---|
| SQLRecord |  |  |  |
| DBName | String | testDB | 数据库名称。 |
| AccountName | String | accounttest | 执行操作的账号名称。 |
| HostAddress | String | 192.168.0.121 | 连接数据库的客户端IP地址。 |
| SQLText | String | update test.zxb set id=0 limit 1 | SQL语句。 |
| TotalExecution Times | Long | 600 | 执行耗时，单位：微秒。 |
| ReturnRowCou nts | Long | 30 | 返回记录数。 |
| ThreadID | String | 1025865428 | 线程ID。 |
| ExecuteTime | String | 2011-06- 11T15:00:23Z | 执行时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSQLLogRecords &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2011-06-01T15:00:00Z &EndTime=2011-06-11T15:00:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeSQLLogRecordsResponse>
   <PageNumber>1</PageNumber>
   <TotalRecordCounts>1</TotalRecordCounts>
   <ItemsCounts>1</ItemsCounts>
   <SQLItems>
      <SQLItem>
         <DBName>test</DBName>
         <AccountName>accounttest</AccountName>
         <HostAddress>192.168.0.121</HostAddress>
         <SQLText>update test.zxb set id=0 limit 1</SQLText>
         <TotalExecutionTimes>12</TotalExecutionTimes>
         <ReturnRowCounts>34</ReturnRowCounts>
         <ExecuteTime>2011-06-11T15:00:23Z</ExecuteTime>
      </SQLItem>
   </SQLItems>
   <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
</DescribeSQLLogRecordsResponse>
```

`JSON` 格式

```json
{ "PageNumber":1, "TotalRecordCounts":1, "ItemsCounts":1, "SQLItems": {"SQLItem":
```

[

```json
{ "DBName":"test", "AccountName":"accounttest", "HostAddress":"192.168.0.121", "SQLText":"update test.zxb set id=0 limit 1", "TotalExecutionTimes":12, "ReturnRowCounts":34, "ExecuteTime":"2011-06-11T15:00:23Z" }
```

]

```json
}, "RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828" }
```

#### 查询SQL洞察（SQL审计）列表

支持的实例版本如下： MySQL SQL Server 2008 R2 PostgreSQL PolarDB 云数据库RDS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSQLLog Files | 系统规定参数，取值：DescribeSQLLogFiles。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxx | 实例ID。 |
| FileName | String | 否 | custinsxxxxx.csv | 审计文件名称。 |
| PageSize | Integer | 否 | 20 | 每页记录数，取值：30~200。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：1-100000。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 10 | 总记录数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 10 | 本页记录数。 |
| Items | Array of LogFile |  | 审计文件列表。 |
| LogFile |  |  |  |
| FileID | String | custinsxxxxx.csv | 文件名称。 |
| LogStatus | String | Success | 文件当前状态，取值： Success：生成成功 Failed：生成失败 Generating：生成中 |
| LogStartTime | String | 2015-05- 23T07:00:00Z | SQL起始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| LogEndTime | String | 2015-05- 24T07:00:00Z | SQL结束时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

云数据库RDS

| LogDownloadU RL | String | http://rdslog-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | 下载地址。若当前不可下载，则为空。 |
|---|---|---|---|
| LogSize | String | 3000 | 日志文件大小，单位：Byte。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSQLLogFiles &DBInstanceId=rm-uf6wjk5xxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSQLLogFilesResponse>
   <items>
      <FileID>ZUBaS964T3OYtxxxxxxxx</FileID>
      <LogStatus>Success</LogStatus>
      <LogStartTime>2015-05-23T07:00:00Z</LogStartTime>
      <LogEndTime>2015-05-23T07:00:00Z</LogEndTime>
      <LogDownloadURL>xxxxxx.cn-hangzhou.oss.aliyun-inc.com/xxxxx</LogDownloadURL>
      <LogSize>257</LogSize>
   </items>
   <pageRecordCount>1</pageRecordCount>
   <requestId> 1AD222E9-E606-4A42-BF6D-8A4442913CEF</requestId>
   <totalRecordCount>1</totalRecordCount>
</DescribeSQLLogFilesResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "items": [
        {
            "FileID": "ZUBaS964T3OYtxxxxxxxx",
            "LogStatus": "Success",
            "LogStartTime": "2015-05-23T07:00:00Z",
            "LogEndTime": "2015-05-23T07:00:00Z",
            "LogDownloadURL": "xxxxxx.cn-hangzhou.oss.aliyun-inc.com/xxxxx",
            "LogSize": "257"
        }
```

`],`

```json
    "pageRecordCount": 1,
    "requestId": " 1AD222E9-E606-4A42-BF6D-8A4442913CEF",
    "totalRecordCount": 1
}
```

#### 查看SQL日志运行报告列表

调用DescribeSQLLogReportList接口查看SQL日志运行报告列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSQLLog ReportList | 系统规定参数。取值：DescribeSQLLogReportList。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可调用DescribeDBInstances获取。 |
| EndTime | String | 是 | 2021-03- 18T16:00:00Z | 查询结束时间，格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明必须大于查询开始时间 |
| StartTime | String | 是 | 2021-03- 13T16:00:00Z | 查询开始时间，格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数。取值： 30 50 100 默认值：30 |

云数据库RDS

| PageNumber | Integer | 否 | 1 | 页码。大于0，且不超过Integer类型的最大值。 默认值：1 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of Item |  | SQL日志运行报告列表。 |
| Item |  |  |  |
| LatencyTopNIt ems | Array of LatencyTopNIt em |  | 延迟最高的SQL列表。 |
| LatencyTopNIt em |  |  |  |
| AvgLatency | Long | 500 | SQL平均执行时间。单位：ms |
| SQLExecuteTi mes | Long | 5 | SQL执行次数。 |
| SQLText | String | SELECT * FROM table name; _ | SQL语句。 说明展示SQL语句的前128个字符，仅统计执行时间大于100ms的SQL。 |
| QPSTopNItems | Array of QPSTopNItem |  | 执行次数最多的SQL列表。 |
| QPSTopNItem |  |  |  |
| SQLExecuteTi mes | Long | 5 | SQL执行次数。 |
| SQLText | String | SELECT * FROM table name; _ | SQL语句。 说明展示SQL语句的前128个字符，仅统计执行时间大于5ms的SQL。 |
| ReportTime | String | 2019-03- 27T16:00:00Z | 运行报告生成时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间） |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 本页SQL日志运行报告个数。 |

云数据库RDS

| RequestId | String | 08A3B71B-FE08- 4B03-974F- CC7EA6DB1828 | 请求ID。 |
|---|---|---|---|
| TotalRecordCo unt | Integer | 60 | 总记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeSQLLogReportList &DBInstanceId=rm-uf6wjk5xxxxxxx &EndTime=2021-03-18T16:00:00Z &StartTime=2021-03-13T16:00:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeSQLLogReportListResponse>
      <TotalRecordCount>60</TotalRecordCount>
      <PageRecordCount>30</PageRecordCount>
      <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828 </RequestId>
      <PageNumber>1</PageNumber>
      <Items>
            <Item>
                  <ReportTime>2019-03-27T16:00:00Z</ReportTime>
                  <LatencyTopNItems>
                        <LatencyTopNItem>
                              <AvgLatency>500</AvgLatency>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </LatencyTopNItem>
                  </LatencyTopNItems>
                  <QPSTopNItems>
                        <QPSTopNItem>
                              <SQLExecuteTimes>5</SQLExecuteTimes>
                              <SQLText>SELECT * FROM table_name;</SQLText>
                        </QPSTopNItem>
                  </QPSTopNItems>
            </Item>
      </Items>
</DescribeSQLLogReportListResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "TotalRecordCount": "60",
 "PageRecordCount": "30",
 "RequestId": "08A3B71B-FE08-4B03-974F-CC7EA6DB1828\t",
 "PageNumber": "1",
 "Items": {
  "Item": [{
   "ReportTime": "2019-03-27T16:00:00Z",
   "LatencyTopNItems": {
    "LatencyTopNItem": [{
     "AvgLatency": "500",
     "SQLExecuteTimes": "5",
     "SQLText": "SELECT * FROM table_name;"
    }]
   },
   "QPSTopNItems": {
    "QPSTopNItem": [{
     "SQLExecuteTimes": "5",
     "SQLText": "SELECT * FROM table_name;"
    }]
   }
  }]
 }
}
```

#### 清理本地日志

调用PurgeDBInstanceLog接口清理RDS实例本地日志。 RDS实例有自动上传日志备份机制，但是在实例空间不足时，您可以使用本接口手动上传日志备份，提前释放存储空间。上传后系统会自动清理本地重复的日志备份。 调用本接口会将本地日志备份上传到OSS上（SQL Server会先收缩事务日志再上传），然后清理本地日志备份，释放存储空间。

**说明**

该接口仅适用于MySQL、SQL Server实例。 上传日志备份不会影响数据恢复功能。 释放的是存储空间，不是备份空间，因此不会降低备份空间使用量。 日志备份上传到的OSS由RDS提供，不需要您购买，同时也不支持访问此OSS。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | PurgeDBInstanc eLog | 系统规定参数，取值：PurgeDBInstanceLog。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 待清理或收缩日志的实例ID。 |

云数据库RDS

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 65BDA532-28AF- 4122-AA39- B382721EEE64 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=PurgeDBInstanceLog &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PurgeDBInstanceLogResponse>
   <RequestId> 65BDA532-28AF-4122-AA39-B382721EEE64</RequestId>
</PurgeDBInstanceLogResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 65BDA532-28AF-4122-AA39-B382721EEE64"
}
```

### 历史事件

#### 开启或关闭历史事件

调用ModifyActionEventPolicy接口开启或关闭RDS历史事件功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

云数据库RDS

| Action | Strin g | Syst em | 是 | ModifyActionEventPolicy | 系统规定参数。取值： ModifyActionEventPolicy |
|---|---|---|---|---|---|
| RegionId | Strin g | Quer y | 是 | cn-hangzhou | 需要开启或关闭历史事件功能的地域ID，可通过接口 DescribeRegions查看地域 ID。 |
| EnableEve ntLog | Strin g | Quer y | 是 | True | 是否开启历史事件记录功能。 取值： True False |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1E43AAE0-BEE8- 43DA-860D- EAF2AA0724DC | 请求ID。 |
| RegionId | String | cn-hangzhou | 开启或关闭历史事件功能的地域ID。 |
| EnableEventLo g | String | True | 历史事件功能的启用情况。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyActionEventPolicy &RegionId=cn-hangzhou &EnableEventLog=True
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC",
 "EnableEventLog":"True",
 "RegionId":"cn-hangzhou "
}
```

`XML` 格式云数据库RDS

```xml
<RequestId>1E43AAE0-BEE8-43DA-860D-EAF2AA0724DC</RequestId> <EnableEventLog>True</EnableEventLog> <RegionId>cn-hangzhou </RegionId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegion.NotF ound | InvalidRegion.NotFound | Specified Region does not exist in RDS. |

#### 查询历史事件功能是否开启

调用DescribeActionEventPolicy接口查询RDS历史事件功能是否开启。 RDS提供历史事件功能，开启后可查看所处地域内某时间段的历史事件。例如在某个时间创建了实例、修改了参数等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Syst em | 是 | DescribeActionEventPolic y | 系统规定参数。取值： DescribeActionEventPolic y |
| RegionId | Strin g | Quer y | 是 | cn-hangzhou | 地域ID，可以通过接口 DescribeRegions查看地域 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CCECD3CD-AB2D- 4F6D-BEDE- 47BC90A398D2 | 请求ID。 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| EnableEventLo g | String | True | 历史事件功能开启情况。 |

云数据库RDS

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeActionEventPolicy &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2",
 "EnableEventLog":"True",
 "RegionId":"cn-hangzhou"
}
```

`XML` 格式

```xml
<RequestId>CCECD3CD-AB2D-4F6D-BEDE-47BC90A398D2</RequestId> <EnableEventLog>True</EnableEventLog> <RegionId>cn-hangzhou</RegionId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidRegion.NotF ound | InvalidRegion.NotFound | Specified Region does not exist in RDS. |

#### 查询历史事件

调用DescribeEvents接口查询RDS历史事件记录列表。 RDS提供历史事件功能，开启后您可以在所处地域内查看某时间段的历史事件，例如在某个时间创建了实例、修改了参数等等。 调用该接口时，实例必须已开启历史事件功能，否则将操作失败。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeEvents | 系统规定参数，取值：DescribeEvents。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看地域ID。 |

云数据库RDS

| ResourceType | String | 否 | instance | 事件关联资源类型。当前仅支持传入Instance。 |
|---|---|---|---|---|
| ResourceName | String | 否 | rm- bp1z306******** ** | 事件关联资源名称。当前仅支持传入实例 ID。 |
| StartTime | String | 否 | 2019-06- 11T15:00:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| EndTime | String | 否 | 2019-06- 12T15:00:00Z | 查询结束时间，需要晚于开始时间。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30 50 100 默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| EventItems | Array of EventItems |  | 事件列表。 |
| EventItems |  |  |  |
| EventId | Integer | 11000053 | 事件ID。 |
| EventName | String | ModifySecurityIPLis t | 事件名称。 |
| EventPayload | String | {\"Domain\": \"rds- inc- share.aliyuncs.com \", \"Api\": \"ReleaseInstanceP ublicConnection\"} | 事件的请求参数或上下文参数。 |
| EventReason | String | FROM USER _ | 事件操作的来源。 |
| EventRecordTi me | String | 2019-08- 20T01:12:49Z | 事件的记录时间。会稍晚于事件的发生时间。 |

云数据库RDS

| EventTime | String | 2019-08- 20T01:08:22Z | 事件发生时间。 |
|---|---|---|---|
| EventType | String | NetworkManageme nt | 事件类型。 |
| EventUserTyp e | String | SYSTEM | 执行事件的用户类型。 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| ResourceNam e | String | rm- bp1z3065m9976ix 8a | 事件关联资源名称。当前仅有实例ID。 |
| ResourceType | String | instance | 事件关联资源类型。当前仅有实例。 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 30 | 每页记录数。 |
| RequestId | String | A103039D-B1B2- 4C57-B989- 7D7C0DA95426 | 请求ID。 |
| TotalRecordCo unt | Integer | 40 | 总记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeEvents &Region=cn-hangzhou &StartTime=2019-08-20T01:30:00Z &EndTime=2019-08-20T01:35:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeEventsResponse>
  <EventItems>
      <EventItems>
         <EventName>ModifySecurityIPList</EventName>
         <EventUserType>SYSTEM</EventUserType>
         <ResourceType>instance</ResourceType>
         <EventPayload></EventPayload>
         <EventTime>2019-08-20T01:33:43Z</EventTime>
         <RegionId>cn-hangzhou</RegionId>
         <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
         <EventReason>FROM_SYSTEM</EventReason>
         <EventId>11000048</EventId>
         <ResourceName>rm-bpxxxxxxx</ResourceName>
         <EventType>SecurityManagement</EventType>
      </EventItems>
      <EventItems>
         <EventName>ModifySecurityIPList</EventName>
         <EventUserType>SYSTEM</EventUserType>
         <ResourceType>instance</ResourceType>
         <EventPayload></EventPayload>
         <EventTime>2019-08-20T01:33:43Z</EventTime>
         <RegionId>cn-hangzhou</RegionId>
         <EventRecordTime>2019-08-20T01:33:57Z</EventRecordTime>
         <EventReason>FROM_SYSTEM</EventReason>
         <EventId>11000047</EventId>
         <ResourceName>rm-bpxxxxxxx</ResourceName>
         <EventType>SecurityManagement</EventType>
      </EventItems>
   </EventItems>
   <TotalRecordCount>2</TotalRecordCount>
   <PageNumber>1</PageNumber>
   <PageSize>2</PageSize>
   <RequestId>B5FF9EE6-830E-4DBE-8498-9890A62D2875</RequestId>
</DescribeEventsResponse>
```

`JSON` 格式云数据库RDS

```json
{
 "EventItems": {
  "EventItems": [
   {
    "EventName": "ModifySecurityIPList",
    "EventUserType": "SYSTEM",
    "ResourceType": "instance",
    "EventPayload": "",
    "EventTime": "2019-08-20T01:33:43Z",
    "RegionId": "cn-hangzhou",
    "EventRecordTime": "2019-08-20T01:33:57Z",
    "EventReason": "FROM_SYSTEM",
    "EventId": 11000048,
    "ResourceName": "rm-bpxxxxxxx",
    "EventType": "SecurityManagement"
   },
   {
    "EventName": "ModifySecurityIPList",
    "EventUserType": "SYSTEM",
    "ResourceType": "instance",
    "EventPayload": "",
    "EventTime": "2019-08-20T01:33:43Z",
    "RegionId": "cn-hangzhou",
    "EventRecordTime": "2019-08-20T01:33:57Z",
    "EventReason": "FROM_SYSTEM",
    "EventId": 11000047,
    "ResourceName": "rm-bpxxxxxxx",
    "EventType": "SecurityManagement"
   }
```

]

```json
 },
 "TotalRecordCount": 2,
 "PageNumber": 1,
 "PageSize": 2,
 "RequestId": "B5FF9EE6-830E-4DBE-8498-9890A62D2875"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidStartTime.Fo rmat | Specified start time is not valid. | 指定的起始时间无效。 |

### 性能优化诊断（CloudDBA）

#### 创建诊断报告

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateDiagnosti cReport | 系统规定参数。取值：CreateDiagnosticReport。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxx | 实例ID。 |
| StartTime | String | 是 | 2018-06- 11T15:00Z | 用于生成诊断报告的监控数据起始时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2018-06- 12T15:00Z | 用于生成诊断报告的监控数据结束时间。 格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ReportId | String | 10166270 | 诊断报告ID。 |
| RequestId | String | 8DA8956A-53DA- 423E-9540- 387428ED37FF- 5711 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateDiagnosticReport &DBInstanceId=rm-uf6wjk5xxxxxx &StartTime=2018-06-11T15:00Z &EndTime=2018-06-12T15:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CreateDiagnosticReportResponse>
   <reportId>10166270</reportId>
   <requestId>8DA8956A-53DA-423E-9540-387428ED37FF-5711</requestId>
</CreateDiagnosticReportResponse>
```

`JSON` 格式

```json
{
    "reportId": "10166270",
    "requestId": "8DA8956A-53DA-423E-9540-387428ED37FF-5711"
}
```

云数据库RDS

#### 查询诊断报告列表

调用DescribeDiagnosticReportList接口查询诊断报告列表。 返回诊断报告的数据采集时间、生成时间和下载地址等，诊断报告保留15天。 SQL Server 2017集群版不支持该接口。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDiagnos ticReportList | 系统规定参数。取值： DescribeDiagnosticReportList。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B7E9A79C-DE1B- 4398-845F- D654FC0958BD | 请求ID。 |
| ReportList | Array of Report |  | 返回的诊断报告列表。 |
| DiagnosticTim e | String | 2018-01- 17T12:46:09Z | 诊断时间。 |
| DownloadURL | String | http://rdsreport-hz- v3.oss-cn- hangzhou.aliyuncs. com/xxxxx | 公网下载地址，若当前不可下载，则为空串。 |
| EndTime | String | 2018-01- 10T15:31:00Z | 监控数据结束时间。 |
| Score | Integer | 100 | 诊断分数。 |
| StartTime | String | 2018-01- 10T15:30:00Z | 监控数据起始时间。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeDiagnosticReportList &DBInstanceId=rm-uf6wjk5xxxxxxx
```

`&<`公共请求参数> 云数据库RDS 正常返回示例 `XML` 格式

```xml
<DescribeDiagnosticReportListResponse>
   <reportList>
      <diagnosticTime>2018-01-17T12:46:09Z</diagnosticTime>
      <downloadURL>http://rdsreport-hzi-v2.oss-cn-hangzhou-
i.aliyuncs.com/xxxxx</downloadURL>
      <endTime>2018-01-10T15:31:00Z</endTime>
      <score>100</score>
      <startTime>2018-01-10T15:30:00Z</startTime>
   </reportList>
   <requestId>B7E9A79C-DE1B-4398-845F-D654FC0958BD</requestId>
</DescribeDiagnosticReportListResponse>
```

`JSON` 格式

```json
{
    "reportList": [
        {
            "diagnosticTime": "2018-01-17T12:46:09Z",
            "downloadURL": "http://rdsreport-hzi-v2.oss-cn-hangzhou-
i.aliyuncs.com/xxxxx",
            "endTime": "2018-01-10T15:31:00Z",
            "score": 100,
            "startTime": "2018-01-10T15:30:00Z"
        }
```

`],`

```json
    "requestId": "B7E9A79C-DE1B-4398-845F-D654FC0958BD"
}
```

### 数据迁移

#### 获取文件上传地址

调用CreateUploadPathForSQLServer接口获取文件上传地址。 该接口只适用于SQL Server类型的实例。

**说明**

创建文件服务器的账号、密码以及上传文件的路径信息。用户根据此信息，可上传数据文件，待上传完成， 调用导入数据接口，进行外部数据迁移操作。限制条件如下： 实例的状态：使用中。 数据库的状态：使用中。 一个数据库一天只能创建20个文件名，按24小时为一天计算，如上一次创建时间点为2012-03-15 18:30:12，则下次创建时间点大于2012-03-16 18:30:12。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | CreateUploadPat hForSQLServer | 系统规定参数，取值：CreateUploadPathForSQLServ er。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- bp1********** | 实例ID。可调用DescribeDBInstances获取。 |
| DBName | String | 是 | test | 数据库名。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| InternetFtpSer ver | String | 10.230.239.1 | 外网文件服务器。 |
| InternetPort | Integer | 3021 | 外网文件服务器端口。 |
| UserName | String | test | 文件服务器账号。 |
| Password | String | test12345 | 文件服务器账号密码。 |
| FileName | String | testdb01 1370572 _ 475975.bak | 文件名，带扩展名。 |
| IntranetFtpser ver | String | 无 | 内网服务器地址。 |
| Intranetport | Integer | 0 | 内网服务器端口。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateUploadPathForSQLServer &DBInstanceId=rdsaiiabnaiiabn &DBName=RDS_MySQL
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<CreateUploadPathForSQLServerResponse>
         <RequestId>66816822-CEC1-4C8D-AB26-2530A7D4DCA5</RequestId>
         <InternetFtpServer>10.230.239.1</InternetFtpServer>
         <InternetPort>3021</InternetPort>
         <IntranetFtpServer></IntranetFtpServer>
         <IntranetPort></IntranetPort>
         <UserName>test</UserName>
         <Password>test12345</Password>
         <FileName>testdb01_1370572475975.bak</FileName>
</CreateUploadPathForSQLServerResponse>
```

`JSON` 格式

```json
{
    "CreateUploadPathForSQLServerResponse": {
        "RequestId": "66816822-CEC1-4C8D-AB26-2530A7D4DCA5",
        "InternetFtpServer": "10.230.239.1",
        "InternetPort": "3021",
        "UserName": "test",
        "Password": "test12345",
        "FileName": "testdb01_1370572475975.bak"
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | FTPServiceUnavaila ble | The request has failed due to a temporary failure of the FTP server. | 操作失败，原因是FTP服务器发生临时故障。 |
| 403 | OperationDenied.D BStatus | The operation is not permitted due to status of database. | 操作失败，当前数据库状态不支持。实例和实例下的数据库是只读状态，支持SQLServer（仅限专享型实例） 必须满足以下条件：1、 实例状态：可用；2、当前实例没有临时备份任务；3、当前实例没有迁移任务；4、 当前实例没有恢复备份任务；5、文件已上传完成，并且是有效的。 |

#### 查询数据文件列表

通过该接口，您可以得到文件服务器上传账号。在数据文件上传结束后，RDS会更新数据文件状态。通过该接口，也可以查看数据文件是否可用。如果文件可用，则可以进行数据导入，并得到导入过程信息。 该接口只适用于SQL Server类型的实例。

**说明**

**请求参数**

云数据库RDS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFilesFor SQLServer | 系统规定参数，取值： DescribeFilesForSQLServer。 |
| DBInstanceId | String | 是 | rm- bp1842vmucoa5 w874 | 实例名。 |
| StartTime | String | 是 | 2011-06- 11T16:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| EndTime | String | 是 | 2011-06- 11T16:00Z | 查询结束时间，需要大于查询开始时间。 格式：yyyy-MM-ddTHH:mm:ssZ（UTC 时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30/50/100默认值： 30。 |
| PageNumber | Integer | 否 | 5 | 页码，大于0且不超过Integer的最大值； 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rdsaiiabnaiiabn | 实例名称。 |
| TotalRecordCo unt | Integer | 1 | 总记录数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 本页SQL语句个数。 |
| Items | Array of SQLServerUplo adFile |  | 无。 |
| SQLServerUplo adFile |  |  |  |
| DBName | String | testdb01 | 数据库名。 |
| FileName | String | testdb01 1370572 _ 475975.bak | 数据文件名，带扩展名。 |

云数据库RDS

| FileSize | Long | 1243435 | 数据文件大小，单位：Byte。 |
|---|---|---|---|
| InternetFtpSer ver | String | 10.230.239.1 | 文件服务器。 |
| InternetPort | Integer | 3021 | 文件服务器端口。 |
| IntranetFtpser ver | String | 空 | 内网服务器地址。 |
| Intranetport | Integer | 0 | 内网服务器端口。 |
| UserName | String | MKEakJbyG | 文件服务器账号。 |
| Password | String | aT2Y XN1GGnOLz _ m | 文件服务器账号密码。 |
| FileStatus | String | Success | 文件状态。 Unavailable：不可用； Available：可用； NotStarted：未开始； Uploading：正在上传； UploadFailed：上传失败； Virus：有病毒； Deleted：文件被删除； Success：上传成功。 |
| CreationTime | String | 2014-06- 11T15:02:40Z | FTP文件生成时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Description | String | 2 | 文件的状态说明。返回值： 0：未开始上传文件。 1：文件正在上传。 2：文件上传成功，可以进行数据导入。 3：文件上传失败，可能上传过程中被取消， 或者网络原因导致，可以继续上传。 4：文件上传成功，但检查到病毒。 5：文件已被删除。 |
| RequestId | String | 1AD222E9-E606- 4A42-BF6D- 8A4442913CEF | 请求ID。 |

**示例**

请求示例云数据库RDS

```
https://rds.example.com/?Action=DescribeFilesForSQLServer &DBInstanceId=rm-bp1842vmucoa5w874 &EndTime=2011-06-11T16:00Z &StartTime=2011-06-11T16:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeFilesForSQLServerResponse>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <PageRecordCount>1</PageRecordCount>
   <Items>
      <SQLServerUploadFile>
         <DBName>testdb01</DBName>
         <FileName>testdb01_1370572475975.bak</FileName>
         <FileSize>1243435</FileSize>
         <InternetFtpServer>10.230.239.1</InternetFtpServer>
         <InternetPort>3021</InternetPort>
         <IntranetFtpServer></IntranetFtpServer>
         <IntranetPort></IntranetPort>
         <UserName>MKEakJbyG</UserName>
         <Password>aT2Y_XN1GGnOLzm</Password>
         <FileStatus>Success </FileStatus>
         <CreationTime>2014-06-11T15:02:40Z</CreationTime>
      </SQLServerUploadFile>
   </Items>
   <RequestId>08A3B71B-FE08-4B03-974F-CC7EA6DB1828</RequestId>
</DescribeFilesForSQLServerResponse>
```

`JSON` 格式云数据库RDS

```json
{
    "PageNumber":1,
    "TotalRecordCount":1,
    "PageRecordCount":1,
    "Items":{
        "SQLServerUploadFile":[
            {
                "DBName":"testdb01",
                "FileName":"testdb01_1370572475975.bak",
                "FileSize ":"1243435",
                "InternetFtpServer ":"10.230.239.1",
                "InternetPort":3021,
                "IntranetFtpServer":"",
                "IntranetPort":"",
                "UserName":"MKEakJbyG",
                "Password":"aT2Y_XN1GGnOLzm",
                "FileStatus":"Success ",
                "CreationTime":"2014-06-11T15:02:40Z"
            }
```

]

```json
    },
    "RequestId":"08A3B71B-FE08-4B03-974F-CC7EA6DB1828"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | FTPServiceUnavaila ble | The request has failed due to a temporary failure of the FTP server. | 操作失败，原因是FTP服务器发生临时故障。 |

#### 迁入实例

调用ImportDatabaseBetweenInstances接口从其它RDS实例迁入数据。 建议您使用数据传输服务DTS，集数据迁移、订阅、同步于一体，为您提供稳定安全的传输链路。 迁移过程中，源实例的状态处于**迁移中**，目标实例的状态处于**数据导入中**。 调用该接口时，实例必须满足以下条件，否则将操作失败： 仅支持SQL Server的独享和独占规格的实例，关于实例规格详情，请参见**云数据库****RDS** > **产品简介**中的**实例规格**； 仅适用于不同实例间（实例都属于同一个用户）的数据库迁移； 实例状态为运行中； 数据库状态为运行中； 确保目标实例的剩余存储空间>源实例数据库的存储空间； 云数据库RDS

**说明**

暂不支持SQL Server 2017集群版实例。 支持批量数据库迁入。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ImportDatabase BetweenInstanc es | 系统规定参数，取值：ImportDatabaseBetweenInsta nces。 |
| DBInfo | String | 是 | {“DBNames”: [“mydb”,”mydb 2”]} | 待迁移实例的数据库信息，格式为JSON 串。 说明对于SQL Server实例，值为key-value对，key为原数据库，value为迁移目标数据库，SQL Server允许源数据库和目标数据库名称可以不一致。例如： {“DBNames”: {“srcdb”:”destdb”,”srcdb2 ”:”destmydb2”}} 表示将srcdb迁入至destdb，将 srcdb2迁入至destmydb2，但是多个源数据库名称不允许一样，多个目标数据库名称也不允许一样。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 目标实例ID。 |
| SourceDBInstan ceId | String | 是 | rm- g4a1jk8xxxxxxx | 源实例ID，不能与目标实例相同。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ImportId | String | 85265475235 | 导入任务的ID。 |

云数据库RDS

| RequestId | String | 5A77D650-27A1- 4E08-AD9E- 59008EDB6927 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ImportDatabaseBetweenInstances &DBInstanceId=rm-uf6wjk5xxxxxxx &SourceDBInstanceId=rm-g4a1jk8xxxxxxx &DBInfo={“DBNames”:[“mydb”,”mydb2”]}
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<ImportDatabaseBetweenInstancesResponse>
           <ImportId>2122321</ImportId>
         <RequestId>5A77D650-27A1-4E08-AD9E-59008EDB6927</RequestId>
</ImportDatabaseBetweenInstancesResponse>
```

`JSON` 格式

```json
{
       "ImportId":2122321,
       "RequestId":"5A77D650-27A1-4E08-AD9E-59008EDB6927"
}
```

#### 取消迁移任务

调用CancelImport接口取消RDS实例迁移任务。 支持SQL Server的独享和独占规格的实例。发起迁移任务请参见ImportDatabaseBetweenInstances。 该接口暂不支持SQL Server 2017 集群版实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CancelImport | 系统规定参数，取值：CancelImport。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |

云数据库RDS

| ImportId | Integer | 是 | 8562584 | 迁移任务ID。 说明发起迁移任务时会返回此参数，参见ImportDatabaseBetweenInsta nces。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 17F57FEE-EA4F- 4337-8D2E- 9C23CAA63D74 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CancelImport &DBInstanceId=rm-uf6wjk5xxxxxxx &ImportId=8562584
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<CancelImportResponse>
         <RequestId>17F57FEE-EA4F-4337-8D2E-9C23CAA63D74</RequestId>
</CancelImportResponse>
```

`JSON` 格式

```json
{
  "RequestId": " 17F57FEE-EA4F-4337-8D2E-9C23CAA63D74"
}
```

#### 创建上云任务

调用CreateMigrateTask接口将OSS上的备份文件还原到RDS SQL Server实例，实现数据上云。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateMigrateTa sk | 系统规定参数，取值：CreateMigrateTask。 |

云数据库RDS

| BackupMode | String | 是 | FULL | 迁移上云任务类型，取值： FULL：通过全量备份文件去执行还原操作。 UPDF：通过增量文件或者日志文件去还原增量部分的数据。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| DBName | String | 是 | testDB | 目标数据库名称。 |
| IsOnlineDB | String | 是 | True | 是否将还原后的数据库带上线，便于用户访问，取值： True：将数据库带上线。 False：不将数据库带上线。 说明目前SQL Server 2008 R2 版本该值恒定为True。 |
| CheckDBMode | String | 否 | AsyncExecuteDB Check | 打开数据库后一致性检查方法，取值： SyncExecuteDBCheck：同步执行 DB检查。 AsyncExecuteDBCheck：异步执行DB检查。 默认值为AsyncExecuteDBCheck（兼容 SQL Server 2008 R2）。 说明当 IsOnlineDB=True时，该值有效。 |
| OssObjectPositio ns | String | 否 | oss-ap- southeast- 1.aliyuncs.com:r dsmssqlsingapor e:autotest 2008 _ R2 TestMigratio _ n FULL.bak _ | OSS的组成部分。 取值由3段组成，用英文冒号（:）分隔： OSS Endpoint地址：oss-ap- southeast-1.aliyuncs.com。 OSS Bucket名字： rdsmssqlsingapore。 OSS上的备份文件Key： autotest 2008R2 TestMigration F _ _ _ ULL.bak。 说明该参数对于 SQL Server 2008 R2 版本实例是可选参数。 该参数对于 SQL Server 2008 R2 以上版本实例是必传参数。 |

云数据库RDS

| OSSUrls | String | 否 | check cdn oss.s _ _ h www.xxxxxx.mo bi | 备份文件所在OSS共享URL地址（Encode 编码后的URL）。 有多个地址时，先使用“\|”隔开，再编码后传入参数。 说明 SQL Server 2008 R2 必须传入该参数。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupMode | String | FULL | 迁移上云任务类型，取值为： FULL：通过全量备份文件去执行还原操作。 UPDF：通过增量文件或者日志文件去还原增量部分的数据。 |
| DBInstanceId | String | rm-uf6wjk5xxxxx | 实例ID。 |
| DBName | String | test02 | 数据库名称。 |
| MigrateTaskId | String | 564563256 | 迁移任务ID。 |
| RequestId | String | 866F5EB8-4650- 4061-87F0- 379F6F968BCE | 请求ID。 |
| TaskId | String | 5451225 | 任务ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=CreateMigrateTask &DBInstanceId=rm-uf6wjk5xxxxxxx &DBName=testDB &BackupMode=FULL &IsOnlineDB=True &OssObjectPositions=oss-ap-southeast- 1.aliyuncs.com:rdsmssqlsingapore:autotest_2008R2_TestMigration_FULL.bak
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<CreateMigrateTaskResponse>
   <MigrateTaskId>135847</MigrateTaskId>
   <DBInstanceId>rm-bp178grbxxxxxxx</DBInstanceId>
   <RequestId>5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2</RequestId>
   <BackupMode>UPDF</BackupMode>
   <TaskId>128301751</TaskId>
   <DBName>test02</DBName>
</CreateMigrateTaskResponse>
```

`JSON` 格式

```json
{
 "MigrateTaskId": "135847",
 "DBInstanceId": "rm-bp178grbxxxxxxx",
 "RequestId": "5F2B3757-BD56-40B3-B5F2-FCDD9FA0E2E2",
 "BackupMode": "UPDF",
 "TaskId": "128301751",
 "DBName": "test02"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBName | The instance does not have the specified DB name. | 目标数据库不存在，请确认目标数据库名称正确性及状态，或更换其他数据库。 |
| 400 | InvalidOSSURL | The Specified OSS URL is not valid | OSS的地址信息错误，请检查。 |

#### 查询实例迁移状态

调用DescibeImportsFromDatabase接口查看实例迁移状态列表。 因为仅MySQL和SQL Server可执行迁移任务，所以仅能查询这两个数据库类型的迁移任务。执行迁移任务请使用ImportDatabaseBetweenInstances接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescibeImportsF romDatabase | 系统规定参数，取值：DescibeImportsFromDatabas e。 |
| DBInstanceId | String | 是 | rm-bpxxxxx | 实例ID。 |
| EndTime | String | 是 | 2011-06- 11T16:00Z | 查询结束时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |

云数据库RDS

| Engine | String | 是 | MySQL | 数据库类型。取值： MySQL SQLServer |
|---|---|---|---|---|
| StartTime | String | 是 | 2011-06- 11T15:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| ImportId | Integer | 否 | 123 | 迁移任务的ID。 |
| PageSize | Integer | 否 | 30 | 每页记录数。取值： 30 50 100 默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of ImportResultFr omDB |  | 迁移状态列表。 |
| ImportResultFr omDB |  |  |  |
| ImportDataSta tus | String | NotStart | 迁移任务状态。取值： NotStart：未开始 FullExporting：全量导出中 FullImporting：全量导入中 Success：成功 Failed：失败 Canceled：已取消 Canceling：正在取消 IncrementalWaiting：增量同步等待 IncrementalImporting：增量同步中 StopSyncing：停止同步 |

云数据库RDS

| ImportDataSta tusDescription | String | 描述信息 | 迁移任务描述。 |
|---|---|---|---|
| ImportDataTy pe | String | Full | 迁移任务类型。取值： Full：全量迁移 Incremental：增量迁移 |
| ImportId | Integer | 123 | 迁移任务的ID。 |
| IncrementalIm portingTime | String | 2011-06- 11T15:00Z | 增量同步时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 每页记录数。 |
| RequestId | String | B000AA91-393D- 46F9-8D9B- 098E28931A3A | 请求ID。 |
| TotalRecordCo unt | Integer | 1 | 记录总数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescibeImportsFromDatabase &DBInstanceId=rm-bpxxxxx &EndTime=2011-06-11T16:00Z &Engine=MySQL &StartTime=2011-06-11T15:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescibeImportsFromDatabaseResponse>
  <TotalRecordCount>0</TotalRecordCount>
  <PageRecordCount>30</PageRecordCount>
  <RequestId>B000AA91-393D-46F9-8D9B-098E28931A3A</RequestId>
  <PageNumber>1</PageNumber>
  <Items>
        <ImportResultFromDB>
              <ImportId>123</ImportId>
              <ImportDataType>Full</ImportDataType>
              <ImportDataStatus>NotStart</ImportDataStatus>
              <ImportDataStatusDescription>描述信息</ImportDataStatusDescription>
              <IncrementalImportingTime></IncrementalImportingTime>
        </ImportResultFromDB>
  </Items>
</DescibeImportsFromDatabaseResponse>
```

`JSON` 格式

```json
{
  "TotalRecordCount": 0,
  "PageRecordCount": 30,
  "RequestId": "B000AA91-393D-46F9-8D9B-098E28931A3A",
  "PageNumber": 1,
  "Items": {
    "ImportResultFromDB": [
      {
        "ImportId":"123",
        "ImportDataType":"Full",
        "ImportDataStatus":"NotStart",
        "ImportDataStatusDescription":"描述信息",
        "IncrementalImportingTime":""
      }
```

]

```
  }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | OperationDenied.D BInstanceType | The operation is not permitted due to type of instance. | 实例类型不支持该操作，请核实是否是主实例。 |

#### 查询单个上云任务

调用DescribeMigrateTaskById查询SQL Server的某个OSS备份上云任务的信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库RDS

| Action | String | 是 | DescribeMigrate TaskById | 系统规定参数。取值 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | rm- bp11e1tzgxxxx4 ox | RDS SQL Server实例ID。 |
| MigrateTaskId | String | 是 | 235943 | 备份上云任务的ID，可以通过 DescribeMigrateTasks接口查询。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupMode | String | FULL | 备份数据上云任务类型，取值： FULL：表示通过全量备份文件去执行还原操作。 UPDF：表示通过增量文件或者日志文件去还原增量部分的数据。 |
| CreateTime | String | 2020-05- 30T12:11:04Z | 备份数据上云任务创建时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| DBInstanceNa me | String | rm- uf6wjk5xxxxxxxxxx | 实例ID。 |
| DBName | String | mytestdb | 数据库名称。 |
| Description | String | Success to DBCC checkdb asynchronously | 备份数据上云任务的描述信息。 |
| EndTime | String | 2021-05- 30T12:11:04Z | 备份数据上云任务结束时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| IsDBReplaced | String | False | 是否是覆盖性导入。取值： False：否 True：是 |
| MigrateTaskId | String | 235943 | OSS备份上云任务的ID。 |
| RequestId | String | 6ED3635A-01F9- 47BD-B9C8- CB3FD70A336E | 请求ID。 |

云数据库RDS

| Status | String | Success | 备份数据上云任务的状态，取值： NoStart：未开始 Running：运行中 Success：成功 Failed：失败 Waiting：等待（等待增量备份文件导入） |
|---|---|---|---|

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeMigrateTaskById &DBInstanceId=rm-bp11e1tzgxxxx4ox &MigrateTaskId=235943
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeMigrateTaskByIdResponse>
    <Status>Success</Status>
    <Description>Success to DBCC checkdb asynchronously</Description>
    <RequestId>B994DF29-44A1-43FD-A693-917930DFEBCE</RequestId>
    <EndTime>2021-03-04T13:50:23Z</EndTime>
    <MigrateTaskId>235943</MigrateTaskId>
    <CreateTime>2021-03-04T13:47:17Z</CreateTime>
    <BackupMode>FULL</BackupMode>
    <DBName>mytestdb</DBName>
    <DBInstanceName>rm-bp11e1tzgxxxxx4ox</DBInstanceName>
</DescribeMigrateTaskByIdResponse>
```

`JSON` 格式

```json
{
  "Status": "Success",
  "Description": "Success",
  "RequestId": "6ED3635A-01F9-47BD-B9C8-CB3FD70A336E",
  "EndTime": "2021-03-04T13:47:58Z",
  "MigrateTaskId": "235943",
  "CreateTime": "2021-03-04T13:47:17Z",
  "BackupMode": "FULL",
  "DBName": "mytestdb",
  "DBInstanceName": "rm-bp11e1tzgxxxxx4ox"
}
```

#### 查询上云任务列表

调用DescribeMigrateTasks接口查询RDS SQL Server实例备份数据上云任务列表。 该接口可以查询实例在最近一周内的备份数据上云任务记录。 云数据库RDS 该接口可以查询实例在最近周内的备份数据上云任务记录

**说明**

备份数据上云的源备份文件必须是全量备份（FULL）文件。 暂不支持SQL Server 2017集群版实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMigrate Tasks | 系统规定参数，取值：DescribeMigrateTasks。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 |
| EndTime | String | 是 | 2017-10- 25T01:00Z | 查询结束时间，必须大于开始时间。格式：yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| StartTime | String | 是 | 2017-10- 20T01:00Z | 查询开始时间。格式：yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30~100。默认值：30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值：大于0且不超过Integer的最大值。 默认值：1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| Items | Array of MigrateTask |  | 备份数据上云任务信息列表。 |
| MigrateTask |  |  |  |
| BackupMode | String | FULL | 备份数据上云任务类型，取值： FULL：表示通过全量备份文件去执行还原操作。 UPDF：表示通过增量文件或者日志文件去还原增量部分的数据。 |
| CreateTime | String | 2017-05- 30T12:11:04Z | 备份数据上云任务创建时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

云数据库RDS

| DBName | String | testDB | 数据库名称。 |
|---|---|---|---|
| Description | String | Api description | 备份数据上云任务的描述信息。 |
| EndTime | String | 2017-05- 30T13:11:04Z | 备份数据上云任务结束时间。格式：yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| IsDBReplaced | String | True | 是否是覆盖性导入。 |
| MigrateTaskId | String | 564522545 | 备份数据上云任务的ID。 |
| Status | String | Success | 备份数据上云任务的状态，取值： NoStart：未开始 Running：运行中 Success：成功 Failed：失败 Waiting：等待（等待增量备份文件导入） |
| PageRecordCo unt | Integer | 10 | 每页记录数。 |
| PageNumber | Integer | 1 | 获取第几页的数据。 |
| RequestId | String | 4E356DDF-6B83- 45DB-99D5- 4B1E8A0D286B | 请求ID。 |
| TotalRecordCo unt | Integer | 30 | 满足条件的总的记录数。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeMigrateTasks &DBInstanceId=rm-uf6wjk5xxxxxxx &StartTime=2017-10-20T01:00Z &EndTime=2017-10-25T01:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<DescribeMigrateTasksResponse>
   <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
   <PageRecordCount>1</PageRecordCount>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>10</TotalRecordCount>
   <Items>
      <MigrateTaskId>rm-bp1842vxxxxx</MigrateTaskId>
      <DBName>test02</DBName>
      <CreateTime>2017-05-30 T12:11:4Z</CreateTime>
      <EndTime>2017-05-30 T12:11:4Z</EndTime>
      <IsDBReplaced>True</IsDBReplaced>
      <Status>Success</Status>
      <BackupMode>FULL</BackupMode>
      <Description>Api description</Description>
   </Items>
</DescribeMigrateTasksResponse>
```

`JSON` 格式

```json
{
    "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
    "PageRecordCount": 1,
    "PageNumber": 1,
    "TotalRecordCount": 10,
    "Items": {
        "MigrateTaskId": "rm-bp1842vxxxxx",
        "DBName": "test02",
        "CreateTime": "2017-05-30 T12:11:4Z",
        "EndTime": "2017-05-30 T12:11:4Z",
        "IsDBReplaced": "True",
        "Status": "Success",
        "BackupMode": "FULL",
        "Description": "Api description"
    }
}
```

#### 查询上云任务文件

调用DescribeOssDownloads接口查询RDS SQL Server备份数据上云任务的文件详情。 该接口暂不支持SQL Server 2017企业版和2019 企业版实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeOssDow nloads | 系统规定参数，取值：DescribeOssDownloads。 |

云数据库RDS

| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可通过DescribeDBInstances接口查询。 |
|---|---|---|---|---|
| MigrateTaskId | String | 是 | 5625458541 | 迁移任务的ID，可通过 DescribeMigrateTasks接口查询。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| Items | Array of OssDownload |  | 导入的文件列表。 |
| OssDownload |  |  |  |
| BackupMode | String | Database | 备份类型，取值： Database：全量备份文件 Differential Database：增量备份文件 _ Transaction Log：日志备份文件 _ |
| CreateTime | String | 2017-08- 17T12:45:15Z | 备份文件在下载列表中的创建时间。格式：yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| Description | String | App description | 文件描述信息。 |
| FileName | String | test | 备份文件在OSS上的名称。 |
| FileSize | String | 2 | 备份文件大小，单位MB。 |
| IsAvailable | String | True | 是否可用，取值：True \| False |

云数据库RDS

| Status | String | Finished | 文件状态，取值： NoStart：未开始 Downloading：下载中 Finished：下载完成 DownloadFailed：下载失败 VerifyFailed：MD5校验失败 Deleted：已删除 DeleteFailed：删除失败 CheckSuccess：检查成功 CheckFailed：检查失败 Restoring：还原中 Restored：还原成功 RestoreFailed：还原失败 |
|---|---|---|---|
| MigrateTaskId | String | 562154852 | 迁移任务的ID。 |
| RequestId | String | A5409D02-D661- 4BF3-8F3D- 0A814D0574E7 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=DescribeOssDownloads &DBInstanceId=rm-uf6wjk5xxxxxxx &MigrateTaskId=5625458541
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeDBInstancesResponse>
      <RequestId>A5409D02-D661-4BF3-8F3D-0A814D0574E7</RequestId>
      <DBInstanceId>rm-uf6wjk5xxxxxxx</DBInstanceId>
      <MigrateTaskId>562154852</MigrateTaskId>
      <Items>
            <OssDownload>
                  <Status>Finished</Status>
                  <Description>App description</Description>
                  <EndTime>2017-08-27T12:45:15Z</EndTime>
                  <IsAvailable>True</IsAvailable>
                  <BackupMode>Database</BackupMode>
                  <CreateTime>2017-08-17T12:45:15Z</CreateTime>
                  <FileName>test</FileName>
                  <FileSize>2</FileSize>
            </OssDownload>
      </Items>
</DescribeDBInstancesResponse>
```

云数据库RDS `JSON` 格式

```json
{
    "DescribeDBInstancesResponse": {
        "RequestId": "A5409D02-D661-4BF3-8F3D-0A814D0574E7",
        "DBInstanceId": "rm-uf6wjk5xxxxxxx",
        "MigrateTaskId": 562154852,
        "Items": {
            "OssDownload": {
                "Status": "Finished",
                "Description": "App description",
                "EndTime": "2017-08-27T12:45:15Z",
                "IsAvailable": "True",
                "BackupMode": "Database",
                "CreateTime": "2017-08-17T12:45:15Z",
                "FileName": "test",
                "FileSize": 2
            }
        }
    }
}
```

### 标签管理

#### 创建标签

调用TagResources接口为指定的RDS实例创建并绑定标签。 在实例数量较多的情况下，您可以创建多个标签，为实例绑定不同的标签对其进行分类，之后通过标签进行实例筛选。 标签由一对键（key）值（value）组成，键在同账号同地域下唯一，值无此限制。 若设置的标签不存在，则自动创建该标签并绑定到目标实例。 若实例已经绑定了有相同键的标签，则进行覆盖绑定。 每个实例最多可以绑定20个标签。 每次调用最多设置50个实例进行批量标签绑定。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | TagResources | 系统规定参数。取值：TagResources。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看可用的地域ID。 |
| ResourceId.N | RepeatL ist | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可以同时对N个实例绑定标签，N 的取值范围：1~50。 |

云数据库RDS

| ResourceType | String | 是 | INSTANCE | 资源类型定义。唯一取值：INSTANCE。 |
|---|---|---|---|---|
| Tag.N.Key | String | 否 | testkey1 | 标签键。可以同时创建N个标签键，N的取值范围：1~20。不允许传入空字符串。 |
| Tag.N.Value | String | 否 | testvalue1 | 标签键对应的标签值。可以同时创建N个标签值，N的取值范围：1~20。允许传入空字符串。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=TagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1 &Tag.1.Value=testvalue1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TagResourcesResponse>
  <RequestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</RequestId>
</TagResourcesResponse>
```

`JSON` 格式

```json
{
 "RequestId":"224DB9F7-3100-4899-AB9C-C938BCCB43E7"
}
```

#### 绑定标签

调用AddTagsToResource接口为实例绑定标签。 为实例绑定已有的或新创建的标签，限制如下： 每个标签（Tag）由标签键（TagKey）和标签值（TagValue）组成，TagKey不能为空，TagValue可以为空； 云数据库RDS TagKey和TagValue的值不允许以aliyun开头； TagKey和TagValue不区分大小写； TagKey最长为64个字符，TagValue最长为128个字符； 每个实例最多绑定10个Tag，每个实例绑定的TagKey不能重复。若绑定带有重复TagKey的Tag，则后绑定的Tag将覆盖之前的Tag。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddTagsToReso urce | 系统规定参数，取值：AddTagsToResource。 |
| RegionId | String | 是 | cn-hagnzhou | 地域ID，可以通过接口DescribeRegions 查看可用的地域ID。 |
| DBInstanceId | String | 是 | rm- uf6wjk5xxxxxxx | 实例ID。 说明支持传入最多30个实例 ID进行批量操作，用英文逗号（,）隔开。 |
| Tags | String | 否 | {“key1”:”value1 ”,“key2”:””} | 需要绑定的Tag列表，包括TagKey和 TagValue。单次最多支持传入5组值，格式： {"key1":"value1","key2":"value2"...} 。 说明 TagKey不能为空，TagValue可以为空。 |
| Tag.1.key | String | 否 | key1 | 当前第一组key。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.2.key | String | 否 | key2 | 当前第二组key。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.3.key | String | 否 | key3 | 当前第三组key。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |

云数据库RDS

| Tag.4.key | String | 否 | key4 | 当前第四组key。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
|---|---|---|---|---|
| Tag.5.key | String | 否 | key5 | 当前第五组key。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.1.value | String | 否 | value1 | 当前第一组value。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.2.value | String | 否 | value2 | 当前第二组value。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.3.value | String | 否 | value3 | 当前第三组value。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.4.value | String | 否 | value4 | 当前第四组value。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| Tag.5.value | String | 否 | value5 | 当前第五组value。需要绑定的Tag，包括 TagKey和TagValue，单次最多支持传入 5组值。TagKey不能为空，TagValue可以为空。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
| proxyId | String | 否 | API | 代理模式ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 224DB9F7-3100- 4899-AB9C- C938BCCB43E7 | 请求ID。 |

云数据库RDS

**示例**

请求示例

```
http(s)://rds.example.com/?Action=AddTagsToResource &RegionId=cn-hagnzhou &DBInstanceId=rm-uf6wjk5xxxxxxx &Tags=%7B%22test%22%3A%221%22%7D
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<AddTagsToResourceResponse>
   <requestId>224DB9F7-3100-4899-AB9C-C938BCCB43E7</requestId>
</AddTagsToResourceResponse>
```

`JSON` 格式

```json
{
    "requestId": "224DB9F7-3100-4899-AB9C-C938BCCB43E7"
}
```

#### 查询标签

调用ListTagResources查询一个或多个RDS实例已经绑定的标签列表。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTagResource s | 系统规定参数。取值：ListTagResources。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看可用的地域ID。 |
| ResourceId.N | RepeatL ist | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可以同时查询N个实例的标签，N 的取值范围：1~50。 说明 ResourceId.N参数和Tag.N.Key参数至少传入一个。 |
| ResourceType | String | 是 | INSTANCE | 资源类型定义。唯一取值：INSTANCE。 |
| NextToken | String | 否 | 212db86sca438 4811e0b5e8707 ec21345 | 用来返回更多结果。第一次查询不需要提供这个参数，如果一次查询没有返回全部结果，则可在后续查询中传入前一次返回的token继续查询。 |

云数据库RDS

| Tag.N.Key | String | 否 | testkey1 | 标签键。可以同时查询N个标签键，N的取值范围：1~20。不允许传入空字符串。 说明 ResourceId.N参数和Tag.N.Key参数至少传入一个。 |
|---|---|---|---|---|
| Tag.N.Value | String | 否 | testvalue1 | 标签键对应的标签值。可以同时查询N个标签值，N的取值范围：1~20。允许传入空字符串。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NextToken | String | 212db86sca43848 11e0b5e8707ec21 345 | 如果一次查询没有返回全部结果，则可在后续查询中传入前一次返回的token继续查询。 |
| RequestId | String | 47A514A1-4B77- 4E30-B4C5- 2A880650B3FD | 请求ID。 |
| TagResources | Array of TagResource |  | 查询到的实例和标签的信息。 |
| TagResource |  |  |  |
| ResourceId | String | rm-uf6wjk5xxxxxxx | 实例ID。 |
| ResourceType | String | ALIYUN::RDS::INST ANCE | 资源类型， ALIYUN::RDS::INSTANCE 即云数据库RDS实例。 |
| TagKey | String | testkey1 | 标签键。 |
| TagValue | String | testvalue1 | 标签键对应的标签值。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=ListTagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &Tag.1.Key=testkey1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库RDS

```xml
<ListTagResourcesResponse>
  <TagResources>
        <TagResource>
              <ResourceType>ALIYUN::RDS::INSTANCE</ResourceType>
              <TagValue>testvalue1</TagValue>
              <ResourceId>rm-uf6wjk5xxxxxxx</ResourceId>
              <TagKey>testkey1</TagKey>
        </TagResource>
  </TagResources>
  <RequestId>47A514A1-4B77-4E30-B4C5-2A880650B3FD</RequestId>
</ListTagResourcesResponse>
```

`JSON` 格式

```json
{
 "TagResources":{
  "TagResource":[
   {
    "ResourceType":"ALIYUN::RDS::INSTANCE",
    "TagValue":"testvalue1",
    "ResourceId":"rm-uf6wjk5xxxxxxx",
    "TagKey":"testkey1"
   }
```

]

```json
 },
 "RequestId":"47A514A1-4B77-4E30-B4C5-2A880650B3FD"
}
```

#### 解绑标签

调用UntagResources接口为指定的RDS实例解绑标签。

**说明**

每次解绑的标签数量不能超过20个。 标签从一个实例解绑后，如果没有绑定到其它实例，则该标签自动被删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UntagResources | 系统规定参数。取值：UntagResources。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，可以通过接口DescribeRegions 查看可用的地域ID。 |
| ResourceId.N | RepeatL ist | 是 | rm- uf6wjk5xxxxxxx | 实例ID。可以同时对N个实例解绑标签，N 的取值范围：1~50。 |

云数据库RDS

| ResourceType | String | 是 | INSTANCE | 资源类型定义。唯一取值：INSTANCE。 |
|---|---|---|---|---|
| TagKey.N | RepeatL ist | 否 | testkey1 | 标签键。可以同时删除N个标签键，N的取值范围：1~20。不允许传入空字符串。 |
| All | Boolean | 否 | false | 是否删除实例的全部标签。取值： true false 默认值：false。 说明未传入TagKey.N时该参数有效。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 601B6F25-21E7- 4484-99D5- 3EF2625C0088 | 请求ID。 |

**示例**

请求示例

```
http(s)://rds.example.com/?Action=UntagResources &RegionId=cn-hangzhou &ResourceType=INSTANCE &ResourceId.1=rm-uf6wjk5xxxxxxx &TagKey.1=testkey1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<UntagResourcesResponse>
        <RequestId>601B6F25-21E7-4484-99D5-3EF2625C0088</RequestId>
</UntagResourcesResponse>
```

`JSON` 格式

```json
{
 "RequestId":"601B6F25-21E7-4484-99D5-3EF2625C0088"
}
```

### 如何使用RAM授权

**使用RAM实现RDS资源授权**

云数据库RDS 您通过云账号创建的RDS实例，都是该账号自己拥有的资源。默认情况下，账号对自己的资源拥有完整的操作权限。 使用阿里云的RAM（Resource Access Management）服务，您可以将您云账号下RDS资源的访问及管理权限授予RAM中子用户。 如果您不需要使用RAM，请略过此章节。

**RAM中可授权的RDS资源类型**

目前，可以在RAM中进行授权的资源类型仅一种：dbinstance。在通过RAM进行授权时，资源的描述方式如下：

| 资源类型 | 授权策略中的资源描述方式 |
|---|---|
| Instance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid acs:rds:$regionid:$accountid:dbinstance/ acs:rds:::dbinstance/ |

其中：所有$regionid应为某个region的id，或者”*“。所有$dbinstanceid应为某个instance的id，或者“*”。以此类推，$account-id是您云账号的数字ID，可以用”*“代替。

**RAM中可对RDS资源进行授权的Action**

在RAM中，可以对一个RDS资源进行以下Action的授权。

| Action1 | Action2 |
|---|---|
| CreateDBInstance | ModifyDBInstanceSpec |
| DeleteDBInstance | CreateReadonlyDBInstance |
| DescribeDBInstances | DescribeDBInstanceAttribute |
| SwitchDBInstanceNetType | RestartDBInstance |
| ModifyDBInstanceDescription | ModifySecurityIps |
| ModifyDBInstanceMaintainTime | UpgradeDBInstanceEngineVersion |
| PurgeDBInstanceLog | CreateDatabase |
| DeleteDatabase | DescribeDatabases |
| ModifyDBDescription | CreateUploadPathForSQLServer |
| DescribeFilesForSQLServer | ImportDataForSQLServer |
| DescribeImportsForSQLServer | ImportDataBaseBetweenInstances |
| CancelImport | CreateAccount |
| ResetAccountPassword | GrantAccountPrivilege |
| RevokeAccountPrivilege | DescribeAccounts |
| DeleteAccount | ModifyAccountDescription |

云数据库RDS

| CreateBackup | DescribeBackups |
|---|---|
| CreateTempDBInstance | DescribeBackupPolicy |
| ModifyBackupPolicy | DescribeResourceUsage |
| DescribeDBInstancePerformance | DescribeSlowLogs |
| DescribeSlowLogRecords | DescribeErrorLogs |
| DescribeBinlogFiles | DescribeSQLLogReports |
| DescribeSQLLogRecords | DescribeOptimizeAdviceOnStorage |
| DescribeOptimizeAdviceOnMissPK | DescribeOptimizeAdviceOnExcessIndex |
| DescribeOptimizeAdviceOnMissIndex | DescribeOptimizeAdviceByDBA |
| DescribeParameters | ModifyeParameter |

除了DescribeRegions，DescribeParameterTemplates参数外，其他接口都可以鉴

**说明**

权。

**授权访问鉴权规则**

当子用户通过RDS API进行资源访问时，RDS后台向RAM进行权限检查，以确保调用者拥有响应权限。每个不同的RDS API会根据涉及到的资源以及API的语义来确定需要检查哪些资源的权限。每个API的鉴权规则见下表：

| Action | 鉴权规则 |
|---|---|
| CreateDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| SwitchDBInstanceNetType | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBInstanceMaintainTime | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| PurgeDBInstanceLog | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DeleteDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyDBDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeFilesForSQLServer | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeImportsForSQLServer | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CancelImport | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ResetAccountPassword | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

云数据库RDS

| RevokeAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
|---|---|
| DeleteAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateBackup | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateTempDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstancePerformance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeBinlogFiles | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogRecords | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissPK | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnMissIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeParameters | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePrepaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPrepaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreatePostpaidDBInstanceForChannel | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyPostpaidDBInstanceSpec | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDBInstanceAttribute | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| RestartDBInstance | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifySecurityIps | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| UpgradeDBInstanceEngineVersion | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateDatabase | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeDatabases | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateUploadPathForSQLServer | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ImportDataForSQLServer | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ImportDataBaseBetweenInstances | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| CreateAccount | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| GrantAccountPrivilege | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeAccounts | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyAccountDescription | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

云数据库RDS

| DescribeBackups | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
|---|---|
| DescribeBackupPolicy | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeResourceUsage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSlowLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeErrorLogs | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeSQLLogReports | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnStorage | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceOnExcessIndex | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| DescribeOptimizeAdviceByDBA | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |
| ModifyeParameter | acs:rds:$regionid:$accountid:dbinstance/$dbinstanceid |

### 附表

#### 客户端错误代码表

##### 公共错误

| 错误代码 | 描述 | HTTP状态码 |
|---|---|---|
| MissingParameter | The input parameter "parameter name" that is mandatory for processing this request is not supplied. | 400 |
| InvalidParameter | The specified parameter "Action or Version" is not valid. | 400 |
| InvalidAccessKeyId.NotFo und | The Access Key ID provided does not exist in our records. | 404 |
| IncompleteSignature | The request signature does not conform to Aliyun standards. | 400 |
| IllegalTimestamp | The input parameter "Timestamp" that is mandatory for processing this request is not supplied. | 400 |
| InvalidOwnerId | The specified OwnerId is not valid. | 400 |
| InvalidOwnerAccount | The specified OwnerAccount is not valid. | 400 |
| InvalidOwner | OwnerId and OwnerAccount can't be used at one API access. | 400 |
| Throttling | Request was denied due to request throttling. | 400 |
| InvalidAction | The specified action is not valid. | 403 |
| ActionUnauthorized | The specified action is not available for you | 403 |

云数据库RDS

| UnsupportedHTTPMethod | This http method not supported. | 403 |
|---|---|---|
| UnsupportedParameter | The parameter "<parameter name>" is not supported. | 400 |
| Forbidden.InstanceNotFo und | The specified Instance is not found. | 404 |
| Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| Forbedden.NotSupportRA M | This action does not support accessed by RAM mode. | 403 |
| Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| InsufficientBalance | Your account does not have enough balance. | 400 |
| Forbidden.Authentication | This operation is forbidden by Aliyun Realname Authentication system. | 403 |
| Invalid<parameter name>.ValueNotSupport ed | The specified parameter “parameter name” is not valid. | 400 |
| Invalid<parameter name>.Malformed | The specified parameter "parameter name n" is not valid. | 400 |
| InvalidParameter | The specified parameter " parameter name n " is not valid. | 400 |

##### 特定错误

| 错误代码 | 描述 | HTTP状态码 |
|---|---|---|
| InvalidRegionId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
| InvalidSecurityIPList.Duplicate | The Security IP address is not in the available range or occupied. | 400 |
| InvalidSecurityIPListLength.Malform ed | The quota of security ip exceeds. | 400 |
| InvalidEngineVersionInRegion.NotAv ailable | The EngineVersion in the Region is not available. | 403 |
| InvaildEngineInRegion.NotAvailable | The Engine in the Region is not available. | 403 |
| InvaildDBInstanceClassInRegion.Not Available | The DBInstanceClass in the Region is not available. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| RegionUnauthorized | There is no authority to create instance in the specified region. | 403 |
| QuotaExceeded.CreateInstance | The quota of create instance exceeds. | 403 |

云数据库RDS

| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 404 |
|---|---|---|
| MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. | 400 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 400 |
| OperationDenied.DBInstanceStorag eReduce | The operation is not permitted due to reduce storage. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to instance status. | 403 |
| DependencyViolation | The operation is not permitted due to instance mount read only or guard instance. | 403 |
| InvalidConnectionStringPrefix.Dupli cate | The connection string is not in the available range or occupied. | 400 |
| QuotaExceeded.SwitchTime | The quota of switch time exceed. | 400 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| InvalidSecurityIps.Duplicate | The quota of security ip exceeds. | 400 |
| OperationDenied.CurrentEngineVer sion | The operation is not permitted due to specified current version . | 400 |
| OperationDenied.ReadOnlyDBInstan ceLower | The operation is not permitted due to higher read only instance version . | 403 |
| OperationDenied.GuardDBInstanceL ower | The operation is not permitted due to higher guard instance version . | 403 |
| OperationDenied.MasterDBInstance State | The operation is not permitted due to status of master instance. | 403 |
| QuotaExceeded.DBName | The quota of db exceeds. | 400 |
| InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| InvalidParameter.Keyword | The specified parameter "DBName" is keyword | 400 |
| OperationDenied.DBStatus | The operation is not permitted due to status of database. | 403 |
| OperationDenied.DBInstanceEngine | The operation is not permitted due to engine of instance. | 403 |
| FTPServiceUnavailable | The request has failed due to a temporary failure of the FTP server. | 403 |
| QuotaExceeded.Upload | The quota of file exceeds. | 403 |
| InvalidFileName.NotCompleted | The specified "FileName" is not completed . | 404 |

云数据库RDS

| InvalidFileName.NotAvailable | The specified "FileName" is not Available . | 404 |
|---|---|---|
| QuotaExceeded.FileSize | The quota of file size exceeds. | 403 |
| QuotaExceeded.DBInstanceStorage | The quota of instance storage exceeds. | 403 |
| InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. | 400 |
| OperationDenied.Region | The operation is not permitted due to different region. | 403 |
| OperationDenied.Engine | The operation is not permitted due to different engine. | 403 |
| OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. | 403 |
| InvalidTaskId.NotFound | The ImportId provided does not exist in our records. | 400 |
| OperationDenied.IncorrectTaskStat us | The operation is not permitted due to status of import. | 403 |
| InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. | 400 |
| InvalidAccountName.Duplicate | The Security db Name is not in the available range or occupied. | 400 |
| QuotaExceeded.AccountName | The quota of account exceeds. | 403 |
| OperationDenied.AccountStatus | The operation is not permitted due to status of account. | 403 |
| InvalidDBName.NotFound | The DBName provided does not exist in our records. | 404 |
| OperationDenied.AccountType | The operation is not permitted due to type of account. | 403 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| OperationDenied.NoDatabase | The operation is not permitted due to no database. | 403 |
| InvalidStartTimeAndEndTime.Malfor med | The end time must be greater than the start time | 400 |
| OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. | 403 |
| InvalidBackupId.NotFound | The BackupId provided does not exist in our records. | 404 |
| OperationDenied.NotFoundBackup | The operation is not permitted due to no backup. | 403 |

云数据库RDS

| OperationDenied.BackupStatus | The operation is not permitted due to type of backup. | 403 |
|---|---|---|
| OperationDenied.BackupMethod | The operation is not permitted method of backup. | 403 |
| OperationDenied.TempDBInstanceE xists | The operation is not permitted due to temp instance exist. | 403 |
| Forbidden.Authentication | The operation is forbidden by Aliyun Realname Authentication System. | 403 |
| IncorrectDBInstanceConnType | Current DB instance conn type does not support this operation. | 404 |
| IncorrecttVpcId.Mismatch | The specified parameter "VpcId " is not valid. | 400 |
| IntranetNetTypeNotExists | Current DB instance net type does not support this operation. | 404 |
| InvalidDBInstanceName.NotFound | The DBInstanceId provided does not exist in our records. | 403 |
| InvalidConnectionMode.ValueNotSu pported | The specified parameter "ConnectionMode" is not valid. | 400 |
| InvalidConnectionString.Duplicate Specified | connection string already exists in the Aliyun RDS. | 403 |
| InvalidConnectionString.Duplicate Specified | connection string or port want to be modified is the same with current net type. | 400 |
| InvalidConnectionStringPrefix.Dupli cated | Specified connection string already exists in the Aliyun RDS. | 403 |
| InvalidCurrentConnectionString.Not Found | Specified current connection string doesn't exist. | 400 |
| InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. | 400 |
| InvalidDBInstanceId.QuotaExceeded | The quota of instance id exceeds. | 400 |
| InvalidDBInstanceNetType.NotFoun d | The Specified DB instance net type is not found. | 404 |
| InvalidDBinstanceNetType.ValueNot Support | The specified parameter "DBinstanceNetType" is not valid. | 400 |
| InvalidDBInstanceType.ValueNotSu pport | The specified parameter "DBInstanceType" is not valid. | 400 |
| InvalidEngineVersion.Malformed | The specified parameter "EngineVersion" is not valid. | 400 |
| InvalidInstanceNetworkType.ValueN otSupported | The specified parameter "InstanceNetworkType" is not valid. | 400 |
| InvalidParameter | The specified parameter "dbInstanceId" is not valid. | 400 |

云数据库RDS

| InvalidPort.Malformed | Specified port is not valid. | 400 |
|---|---|---|
| InvalidPrivateIpAddress.Duplicated | Specified private IP address is duplicated. | 400 |
| InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. | 400 |
| InvalidVPCId.NotFound | Specified virtual vpc is not found. | 400 |
| InvalidVSwitchId.Mismatch | Specified instance and virtual switch are not in the same zone. | 400 |
| InvalidVSwitchId.NotFound | Specified virtual switch is not found in specified VPC. | 400 |
| NetTypeExists | Specified net type already existed. | 400 |
| NetTypeExists | Specified public net type already existed. | 403 |
| OperationDenied.DBInstanceNetTyp e | The operation is not permitted due to net type of instance. | 403 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |
| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
| OperationDenied.Switch | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |
| OperationDenied.DBInstanceStatus | The operation is not permitted due to status of instance. | 403 |
| OperationDenied.DBInstanceType | The operation is not permitted due to type of instance. | 403 |
| OperationDenied.LockMode | The operation is not permitted due to lock of instance. | 403 |

云数据库RDS

| OperationDenied.Switch | Specified instance cannot be switched. | 400 |
|---|---|---|
| OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. | 403 |
| OperationDenied | The resource is out of usage. | 403 |
| OperationDenied | The vpc cloudinstanceIp is use, please check params. | 406 |
| OperationDenied | The vpc service is error, please check params. | 400 |
| PARAMETER ERROR _ | The vpc request parameter may not be null. | 406 |
| PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. | 406 |
| PublicConnectionExists | PublicConnection exists. | 403 |
| bpcIzNoNotEqualsRdsMultIzNo | Specified vpc IzNo not equal rds IzNo. | 400 |

#### 服务器端错误代码表

| 错误代码 | 描述 | HTTP状态码 |
|---|---|---|
| ServiceUnavailabl e | The request has failed due to a temporary failure of the server. | 503 |
| InternalError | The request processing has failed due to some unknown error, exception or failure. | 500 |

#### 实例状态表

| 状态 | 说明 |
|---|---|
| Creating | 创建中 |
| Running | 使用中 |
| Deleting | 删除中 |
| Rebooting | 重启中 |
| DBInstanceClassChanging | 升降级中 |
| TRANSING | 迁移中 |
| EngineVersionUpgrading | 迁移版本中 |
| TransingToOthers | 迁移数据到其他RDS中 |
| GuardDBInstanceCreating | 生产灾备实例中 |
| Restoring | 备份恢复中 |
| Importing | 数据导入中 |

云数据库RDS

| ImportingFromOthers | 从其他RDS实例导入数据中 |
|---|---|
| DBInstanceNetTypeChanging | 内外网切换中 |
| GuardSwitching | 容灾切换中 |
| INS CLONING _ | 实例克隆中 |

#### 性能参数表

**云数据库MySQL版**

| API参数名 | 含义 |
|---|---|
| MySQL NetworkTraffic _ | MySQL实例平均每秒钟的输入流量，MySQL实例平均每秒钟的输出流量。单位为 KB。 |
| MySQL QPSTPS _ | 平均每秒SQL语句执行次数，平均每秒事务数 |
| MySQL Sessions _ | 当前活跃连接数，当前总连接数 |
| MySQL InnoDBBufferRatio _ | InnoDB缓冲池的读命中率，InnoDB缓冲池的利用率，InnoDB缓冲池脏块的百分率 |
| MySQL InnoDBDataReadW _ riten | InnoDB平均每秒钟读取的数据量，InnoDB平均每秒钟写入的数据量。单位为KB |
| MySQL InnoDBLogRequest _ s | 平均每秒向InnoDB缓冲池的读次数，平均每秒向InnoDB缓冲池的写次数 |
| MySQL InnoDBLogWrites _ | 平均每秒日志写请求数，平均每秒向日志文件的物理写次数，平均每秒向日志文件完成的fsync()写数量 |
| MySQL TempDiskTableCre _ ates | MySQL执行语句时在硬盘上自动创建的临时表的数量 |
| MySQL MyISAMKeyBufferR _ atio | MyISAM平均每秒Key Buffer利用率，MyISAM平均每秒Key Buffer读命中率，MyISAM平均每秒Key Buffer写命中率 |
| MySQL MyISAMKeyReadWr _ ites | MyISAM平均每秒钟从缓冲池中的读取次数，MyISAM平均每秒钟从缓冲池中的写入次数，MyISAM平均每秒钟从硬盘上读取的次数，MyISAM平均每秒钟从硬盘上写入的次数 |
| MySQL COMDML _ | 平均每秒Delete语句执行次数，平均每秒Insert语句执行次数， 平均每秒 Insert Select语句执行次数，平均每秒Replace语句执行次数，平均每秒 _ Replace Select语句执行次数，平均每秒Select语句执行次数，平均每秒Update _ 语句执行次数 |
| MySQL RowDML _ | 平均每秒从InnoDB表读取的行数，平均每秒从InnoDB表更新的行数，平均每秒从 InnoDB表删除的行数，平均每秒从InnoDB表插入的行数，平均每秒向日志文件的物理写次数 |
| MySQL MemCpuUsage _ | MySQL实例CPU使用率(占操作系统总数)，MySQL实例内存使用率(占操作系统总数) |
| MySQL IOPS _ | MySQL实例的IOPS（每秒IO请求次数） |

云数据库RDS

| MySQL DetailedSpaceUsag _ e | MySQL实例空间占用详情：ins size实例总空间使用量；data size数据空间； _ _ log size日志空间；tmp size临时空间；other size系统空间 _ _ _ |
|---|---|
| slavestat | 只读实例延迟 |

**云数据库SQL Server版**

| API参数名 | 含义 |
|---|---|
| SQLServer Transactions _ | 平均每秒事务数。 |
| SQLServer Sessions _ | 当前总连接数。 |
| SQLServer BufferHit _ | 缓存命中率。 |
| SQLServer FullScans _ | 平均每秒全表扫描次数。 |
| SQLServer SQLCompilations _ | 每秒SQL编译。 |
| SQLServer CheckPoint _ | 每秒检查点写入Page数。 |
| SQLServer Logins _ | 每秒登录次数。 |
| SQLServer LockTimeout _ | 每秒锁超时次数。 |
| SQLServer Deadlock _ | 每秒死锁次数。 |
| SQLServer LockWaits _ | 每秒锁等待次数。 |
| SQLServer NetworkTraffic _ | SQLServer实例平均每秒钟的输入/输出流量。单位为 KB。 |
| SQLServer QPS _ | 平均每秒SQL语句执行次数。 |
| SQLServer InstanceCPUUsage _ | MSSQL实例CPU使用率(占操作系统总数)。 |
| SQLServer IOPS _ | MSSQL实例的IOPS（每秒IO请求次数）。 |
| SQLServer SpaceUsage _ | MSSQL实例空间占用。 |

#### 禁用关键字表

**云数据库MySQL版**

| 参数字段 | 关键字描述 |
|---|---|

云数据库RDS

| DBName/ AccountName | admin,aurora,replicator,xtrabak,root（MySQL5.5/5.6）,mysql,test,eagleye,infor mation schema,guest,add,analyze,asc,between,blob,call,c _ hange,check,condition,continue,cross,current timestamp,database,day micros _ _ econd,dec,default,desc,distinct,double,e ach,enclosed,exit,fetch,float8,foreign,goto,having,hour minute,ignore,infile,inse _ nsitive,int1,int4,interval,iterate,keys,lea ding,like,lines,localtimestamp,longblob,low priority,mediumint,minute microse _ _ cond,modifies,no write to binlog,on, _ _ _ optionally,out,precision,purge,read,references,rename,require,revoke,schema,s elect,set,spatial,sqlexception,sql big re _ _ sult,ssl,table,tinyblob,to,true,unique,update,using,utc timestamp,varchar,when, _ with,xor,all,and,asensitive,bigint,both,c ascade,char,collate,connection,convert,current date,current user,databases,da _ _ y minute,decimal,delayed,describe,dis _ tinctrow,drop,else,escaped,explain,float,for,from,grant,high priority,hour secon _ _ d,in,inner,insert,int2,int8,into,join,kill,le ave,limit,load,lock,longtext,match,mediumtext,minute second,natural,null,opti _ mize,or,outer,primary,raid0,reads,regex p,repeat,restrict,right,schemas,sensitive,show,specific,sqlstate,sql calc found r _ _ _ ows,starting,terminated,tinyint,trailing, undo,unlock,usage,utc date,values,varcharacter,where,write,year month,alter, _ _ as,before,binary,by,case,character,colu mn,constraint,create,current time,cursor,day hour,day second,declare,delete, _ _ _ deterministic,div,dual,elseif,exists,false, float4,force,fulltext,group,hour microsecond,if,index,inout,int,int3,integer,is,key _ ,label,left,linear,localtime,long,loop,me diumblob,middleint,mod,not,numeric,option,order,outfile,procedure,range,real,r elease,replace,return,rlike,second mi _ crosecond,separator,smallint,sql,sqlwarning,sql small result,straight join,then,t _ _ _ inytext,trigger,union,unsigned,use,utc _ time,varbinary,varying,while,x509,zerofill,galaxy |
|---|---|

**云数据库SQL Server版**

| 参数字段 | 关键字描述 |
|---|---|

云数据库RDS

| DBName/ AccountName | root,admin,eagleye,master,aurora,sa,sysadmin,administrator,mssqld,public,security admin,serveradmin,setupadmin,pr ocessadmin,diskadmin,dbcreator,bulkadmin,tempdb,msdb,model,distribution,mssqls ystemresource,guest,add,except, percent,all,exec,plan,alter,execute,precision,and,exists,primary,any,exit,print,as,fetc h,proc,asc,file,procedure,authorizati on,fillfactor,public,backup,for,raiserror,begin,foreign,read,between,freetext,readtext, break,freetexttable,reconfigure,br owse,from,references,bulk,full,replication,by,function,restore,cascade,goto,restrict,c ase,grant,return,check,group,rev oke,checkpoint,having,right,close,holdlock,rollback,clustered,identity,rowcount,coale sce,identity insert,rowguidcol,coll _ ate,identitycol,rule,column,if,save,commit,in,schema,compute,index,select,constrain t,inner,session user,contains,insert, _ set,containstable,intersect,setuser,continue,into,shutdown,convert,is,some,create,jo in,statistics,cross,key,system user, _ current,kill,table,current date,left,textsize,current time,like,then,current timestamp, _ _ _ lineno,to,current user,load,top,cur _ sor,national,tran,database,nocheck,transaction,dbcc,nonclustered,trigger,deallocate ,not,truncate,declare,null,tsequal, default,nullif,union,delete,of,unique,deny,off,update,desc,offsets,updatetext,disk,on, use,distinct,open,user,distributed, opendatasource,values,double,openquery,varying,drop,openrowset,view,dummy,op enxml,waitfor,dump,option,when, else,or,where,end,order,while,errlvl,outer,with,escape,over,writetext,galaxy |
|---|---|

#### 实例规格

实例有不同的系列、版本、规格，性能也有区别。 表 1. RDS MySQL实例规格参数

| 系列 | 规格类型 | 规格代码 | CPU/内存 | 最大连接数 | 最大 IOPS | 磁盘空间 | 同城容灾部署情况 |
|---|---|---|---|---|---|---|---|
|  |  | 5.6、5.7、8.0 mysql.x8.medium .2 | 2核16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysql.x8.large.2 | 4核32GB | 5000 | 9000 | 50GB- 1000GB（ 步长5G） |  |
|  |  | 5.6、5.7、8.0 mysql.x8.xlarge.2 | 8核64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |

云数据库RDS

|  | 独享套餐 （X8） |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | 5.6、5.7、8.0 mysql.x8.2xlarge. 2 | 16核 128GB | 2000 0 | 3600 0 | 500GB- 3000GB （步长5G） |  |
| 双机高可用版本 |  |  |  |  |  |  | 单机房、 双机房 |
|  |  | 5.6、5.7、8.0 mysql.x8.4xlarge. 2 | 32核 256GB | 4000 0 | 7200 0 | 1000GB~6 000GB |  |
|  |  | 5.6、5.7、8.0 mysql.x8.8xlarge. 2 | 64核 512GB | 8000 0 | 1440 00 |  |  |
|  | 独享套餐 （X4） | 5.6、5.7、8.0 mysql.x4.large.2 | 4核16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysql.x4.xlarge.2 | 8核32GB | 5000 | 9000 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysql.x4.2xlarge. 2 | 16核64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysql.x4.4xlarge. 2 | 32核 128GB | 2000 0 | 3600 0 | 500GB- 3000GB （步长5G） |  |
|  | 独占物理机 | 5.6、5.7、8.0 rds.mysql.st.v52 | 90核 720GB | 1500 00 | 1400 00 | 1000GB- 6000GB |  |
|  |  | 5.6、5.7 rds.mysql.st.h43 | 60核 470GB | 1500 00 | 1200 00 |  |  |
|  | 独享型 （高 CPU） | 5.7 mysql.x4.large.25 | 4核16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.7 mysql.x4.xlarge.2 5 | 8核32GB | 5000 | 9000 | 500GB- 3000GB （步长5G） |  |

云数据库RDS

| 三节点企业版 |  |  |  |  |  |  | 支持单机房三节点形态 |
|---|---|---|---|---|---|---|---|
|  |  | 5.7 mysql.x4.2xlarge. 25 | 16核64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.7 mysql.x4.4xlarge. 25 | 32核 128GB | 2000 0 | 3600 0 | 1000GB- 3000GB （步长5G） |  |
|  | 独享型 （高内存） | 5.7 mysql.x8.medium .25 | 2核 16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.7 mysql.x8.xlarge.2 5 | 4核 32GB | 5000 | 9000 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.7 mysql.x8.xlarge.2 5 | 8核 64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.7 mysql.x8.2xlarge. 25 | 16核 128GB | 2000 0 | 3600 0 |  |  |
|  |  | 5.7 mysql.x8.4xlarge. 25 | 32核 256GB | 4000 0 | 7200 0 | 1000GB- 3000GB （步长5G） |  |
|  | 独占物理机型 | 5.7 mysql.st.8xlarge.2 5 | 60核 470GB | 1000 00 | 1200 00 | 1000GB- 6000GB （步长5G） |  |
|  |  | 5.7 mysql.st.12xlarge. 25 | 90核 720GB | 1500 00 | 1400 00 | 1000GB- 6000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x8.mediu m.1 | 2核16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x8.large. 1 | 4核32GB | 5000 | 9000 | 50GB- 1000GB （步长5G） |  |

| 开发指南·API | 参考 |  |  |  |  |  | 云数据库RD |
|---|---|---|---|---|---|---|---|
| 只读实例 | 独享套餐 （X8） |  |  |  |  |  | 单机房、 双机房 |
|  |  | 5.6、5.7、8.0 mysqlro.x8.xlarge .1 | 8核64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x8.2xlarg e.1 | 16核 128GB | 2000 0 | 3600 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x8.4xlarg e.1 | 32核 256GB | 4000 0 | 7200 0 | 1000GB- 6000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x8.8xlarg e.1 | 64核 512GB | 8000 0 | 1440 0 | 1000GB- 6000GB （步长5G） |  |
|  | 独享套餐 （X4） | 5.6、5.7、8.0 mysqlro.x4.large. 1 | 4核16GB | 2500 | 4500 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x4.xlarge .1 | 8核32GB | 5000 | 9000 | 50GB- 1000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x4.2xlarg e.1 | 16核64GB | 1000 0 | 1800 0 | 500GB- 3000GB （步长5G） |  |
|  |  | 5.6、5.7、8.0 mysqlro.x4.4xlarg e.1 | 32核 128GB | 2000 0 | 3600 0 | 500GB- 3000GB （步长5G） |  |
|  | 独占物理机 | 5.6、5.7、8.0 rds.mysql.st.v52 | 90核 720GB | 1500 00 | 1400 00 | 1000GB- 6000GB （步长5G） |  |
|  |  | 5.6、5.7 rds.mysql.st.h43 | 60核 470GB | 1000 00 | 1200 00 |  |  |

表 2. RDS SQL Server实例规格参数

| 系列 | 版本 | 规格类型 | 规格代码 | CPU/内存 | 最大连接数 | 最大 IOPS | 磁盘空间 | 同城容灾部署情况 |
|---|---|---|---|---|---|---|---|---|

云数据库RDS

| 双机高可用版本 | 2008 R2 | 独享套餐 | mssql.x8.mediu m.2 | 2核16GB | 2500 | 4500 | 250GB | 单机房、双机房， 不支持 V5机型，新局点不输出。 |
|---|---|---|---|---|---|---|---|---|
|  |  |  | mssql.x8.large.2 | 4核32GB | 5000 | 9000 | 500GB |  |
|  |  |  | mssql.x8.xlarge. 2 | 8核64GB | 1000 0 | 1800 0 | 1000GB |  |
|  |  |  | mssql.x8.2xlarg e.2 | 16核 128GB | 2000 0 | 3600 0 | 2000GB |  |
|  |  | 独占物理机 | rds.mssql.st.d13 | 30核 220GB | 6400 0 | 2000 0 | 2TB |  |
|  | 2012 企业版： 2012 ent _ _ ha 2016 企业版： 2016 ent _ _ ha | 独享型 | mssql.x4.mediu m.e2 | 2核 8GB |  |  |  |  |
|  |  |  | mssql.x8.mediu m.e2 | 2核 16GB |  |  |  |  |
|  |  |  | mssql.x4.large.e 2 | 4核 16GB |  |  |  |  |
|  |  |  | mssql.x8.large.e 2 | 4核 32GB |  |  |  |  |
|  |  |  | mssql.x4.xlarge. e2 | 8核 32GB |  |  |  |  |
|  |  |  | mssql.x8.xlarge. e2 | 8核 64GB |  |  |  |  |
|  |  |  | mssql.x4.2xlarg e.e2 | 16核 64GB |  |  |  |  |
|  |  |  | mssql.x8.2xlarg e.e2 | 16核 128GB |  |  |  |  |
|  |  |  | mssql.x4.3xlarg e.e2 | 24核 96GB |  |  |  |  |
|  |  |  | mssql.x4.4xlarg e.e2 | 32核 128GB |  |  |  |  |

云数据库RDS

|  |  |  |  |  | 无限制 | 取决于云盘性能 | 20GB- 4000GB | 仅支持单机房 |
|---|---|---|---|---|---|---|---|---|
|  |  |  | mssql.x8.4xlarg e.e2 | 32核 256GB |  |  |  |  |
|  |  |  | mssql.x8.7xlarg e.e2 | 56核 480GB |  |  |  |  |
|  |  |  | mssql.x4.8xlarg e.e2 | 64核 256GB |  |  |  |  |
|  |  |  | mssql.x8.8xlarg e.e2 | 64核 512GB |  |  |  |  |
|  |  |  | mssql.x4.mediu m.s2 | 2核 8GB |  |  |  |  |
|  |  |  | mssql.x8.mediu m.s2 | 2核 16GB |  |  |  |  |
|  |  |  | mssql.x4.large.s 2 | 4核 16GB |  |  |  |  |
|  | 2012 标准版： 2012 std _ _ ha 2016 标准版： 2016 std _ _ ha | 独享型 |  |  |  |  |  |  |
|  |  |  | mssql.x8.large.s 2 | 4核 32GB |  |  |  |  |
|  |  |  | mssql.x4.xlarge. s2 | 8核 32GB |  |  |  |  |
|  |  |  | mssql.x8.xlarge. s2 | 8核 64GB |  |  |  |  |
|  |  |  | mssql.x4.2xlarg e.s2 | 16核 64GB |  |  |  |  |
|  |  |  | mssql.x8.2xlarg e.s2 | 16核 128GB |  |  |  |  |
|  |  |  | mssql.x4.3xlarg e.s2 | 24核 96GB |  |  |  |  |

表 3. PolarDB实例规格参数

| 系列 | 版本 | 规格类型 | 规格代码 | CPU/内存 | 最大连接数 | 最大 IOPS | 磁盘空间 | 同城容灾部署情况 |
|---|---|---|---|---|---|---|---|---|

云数据库RDS

| 双机高可用版本 | 11 | 独享型 | polardb .x4.sma ll.2 | 1核 4GB | 200 | 5000 | 250GB | 单机房、 双机房 |
|---|---|---|---|---|---|---|---|---|
|  |  |  | polardb .x4.med ium.2 | 2核 8GB | 400 | 10000 |  |  |
|  |  |  | polardb .x8.med ium.2 | 2核 16GB | 2500 | 15000 |  |  |
|  |  |  | polardb .x4.larg e.2 | 4核 16GB | 2500 | 20000 | 250GB- 500GB （步长 5G） |  |
|  |  |  | polardb .x8.larg e.2 | 4核 32GB | 5000 | 30000 |  |  |
|  |  |  | polardb .x4.xlar ge.2 | 8核 32GB | 5000 | 40000 | 500GB- 1000GB （步长 5G） |  |
|  |  |  | polardb .x8.xlar ge.2 | 8核 64GB | 10000 | 60000 |  |  |
|  |  |  | polardb .x4.2xla rge.2 | 16核 64GB | 10000 | 80000 | 1000GB - 2000GB （步长 5G） |  |
|  |  |  | polardb .x8.2xla rge.2 | 16核 128GB | 12000 | 120000 |  |  |
|  |  |  | polardb .x4.4xla rge.2 | 32核 128GB | 12000 | 160000 | 2000GB - 3000GB （步长 5G） |  |
|  |  |  | polardb .x8.4xla rge.2 | 32核 256GB | 12000 | 240000 |  |  |
|  |  | 独占物理机型 | rds.pola rdb.st.h 43 | 60核 470GB | 12000 | 450000 | 6000GB |  |

云数据库RDS 表 4. RDS PostgreSQL实例规格参数

| 系列 | 版本 | 规格类型 | 规格代码 | CPU/内存 | 最大连接数 | 最大 IOPS | 磁盘空间 | 同城容灾部署情况 |
|---|---|---|---|---|---|---|---|---|
| 双机高可用版本/ 只读实例 | 9.4/10 | 独享型 （高内存） | pg.x8.m edium.2 | 2核 16GB | 2500 | 4500 | 20GB- 6000GB (步长 5G) | 单机房、 双机房 |
|  |  |  | pg.x8.la rge.2 | 4核 32GB | 5000 | 9000 |  |  |
|  |  |  | pg.x8.xl arge.2 | 8核 64GB | 10000 | 18000 |  |  |
|  |  |  | pg.x8.2 xlarge.2 | 16核 128GB | 12000 | 36000 |  |  |
|  |  | 独享型 （高 CPU） | pg.x4.la rge.2 | 4核 16GB | 2500 | 4500 |  |  |
|  |  |  | pg.x4.xl arge.2 | 8核 32GB | 5000 | 9000 |  |  |
|  |  |  | pg.x4.2 xlarge.2 | 16核 64GB | 10000 | 18000 |  |  |
|  |  |  | pg.x4.4 xlarge.2 | 32核 128GB | 12000 | 36000 |  |  |
|  |  | 独占物理机型 | rds.pg.s t.h43 | 60核 470GB | 4000 | 50000 |  |  |
