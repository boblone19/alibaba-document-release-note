---
title: "云安全中心（态势感知） 漏洞扫描开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 215
source_pdf: "45_漏洞扫描开发指南_empty-manual-1.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/sas/zh/empty-manual-1.pdf"
converter: line-classifier (PyMuPDF)
---

# 云安全中心（态势感知） 漏洞扫描开发指南

## 快速入门

### API调用流程说明

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

### 开发文档使用说明

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

本文档介绍如何安装及调用Python SDK。

##### 使用CommonRequest进行调用

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
package main "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "fmt"
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

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
阿里云产品的API有RPC和RESTful两种风格，不同风格的API的CommonRequest的调用方法也不同。 通常API参数中包含Action参数的是RPC风格，包含PathPattern参数的是RESTful风格。一般情况下，每个产品内，所有API的调用风格是统一的。每个API仅支持特定的一种风格调用，传入错误的标识，可能会调用到其他API，或收到 `ApiNotFound` 的错误信息。 发起一次CommonRequest请求，您需要获取以下几个参数的值。关于以下参数的更多说明，请参见API公共参数。 接入点（endpoint）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 接口信息：要调用的接口名称。 当调用的API为RPC风格（大部分阿里云产品API为RPC风格，如Sas）时，需要获取Action参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 当调用的API为RESTful风格（如容器服务）时，需要获取PathPattern参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定RESTful路径。

**示例：使用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用接口：

```java
package main
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

| Product | Strin g | 是 | 接口对应的产品名称。取值： Auditprivate：云盾基础组件。 yundunnextsoc：云安全管理中心（SOC）。 Sas：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy：网络流量检测与响应。 Ddosprivate：DDos 清洗。 hsm-private：加密服务。 Cloudfw：云防火墙。 Sddp：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |
|---|---|---|---|
| EndpointPre | Strin g | 是 | 接口对应的域名前缀。取值： auditprivate：云盾基础组件。 yundunnextsoc-pop：云安全管理中心（SOC）。 tds：态势感知。 aegis：安骑士。 yundun-css：容器防护。 secspy-share：网络流量检测与响应。 ddosprivate：DDos 清洗。 hsmprivate：加密服务。 cloudfw：云防火墙。 sddp-api：敏感数据保护。 semawaf：Web应用防火墙。 soar：云安全管理中心（SOC）-编排响应。 |

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

## 漏洞扫描

### 任务模版相关接口

#### TemplateAssetDetectionAdd

调用TemplateAssetDetectionAdd接口v3.1.0 add template asset detection api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateAssetDetectio nAdd | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| alive port _ s | Strin g | Body | 否 |  | 探活端口。 |
| baseline | Integ er | Body | 否 | 1 | 基线id。 |
| baseline r _ ule | Integ er | Body | 否 | 1 | baseline。 |
| custom p _ ort | Strin g | Body | 否 |  | 附加端口。 |
| disable su _ bdomain _ api | Integ er | Body | 否 | 1 | 子域名接口查询。 |
| disable su _ bdomain _ dict | Integ er | Body | 否 | 1 | 子域名字典爆破。 |
| exclude p _ orts | Strin g | Body | 否 |  | 排除端口。 |
| icmp ech _ o | Integ er | Body | 否 | 1 | ICMP ECHO。 _ |

| 漏洞扫描开发指 | 南·漏洞扫 | 描 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| inherit att _ rs | Integ er | Body | 否 | 1 | 自动同步资产信息。 |
| ip2domain | Integ er | Body | 否 | 1 | ip反查域名。 |
| ip scan _ | Integ er | Body | 否 | 1 | 自动导入关联ip。 |
| name | Strin g | Body | 否 | 全量风险扫描模板 | 模版名称。 |
| no status _ | Integ er | Body | 否 | 1 | asset scan。 |
| port area _ | Strin g | Body | 否 | ALL | 端口范围。 |
| retry time _ s | Integ er | Body | 否 | 1 | 重试次数。 |
| scan spee _ d | Strin g | Body | 否 |  | 扫描速率。 |
| sctp | Integ er | Body | 否 | 1 | SCTP。 |
| spc ports _ | Strin g | Body | 否 |  |  |
| sub doma _ in brute r _ _ ate | Integ er | Body | 否 | 1 | 子域名爆破速率。 |
| sub doma _ in scan _ | Integ er | Body | 否 | 1 | 子域名查询。 |
| tcp ack _ | Integ er | Body | 否 | 1 | TCP ACK。 _ |
| tcp syn _ | Integ er | Body | 否 | 1 | TCP SYN。 _ |
| udp | Integ er | Body | 否 | 1 | UDP。 |
| vpc id _ | Strin g | Body | 否 |  | vpcID。 |
| wait time _ out | Integ er | Body | 否 | 1 | 3.4.1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | Integer | 1 | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateAssetDetectionAdd&RegionId=cnhangzhou&alive_ports=&baseline=1&baseline_rule=1&custom_port=&disable_subdomain_api=1&dis le_subdomain_dict=1&exclude_ports=&icmp_echo=1&inherit_attrs=1&ip2domain=1&ip_scan=1&name
```

全量风险扫描模板

```
&no_status=1&port_area=ALL&retry_times=1&scan_speed=&sctp=1&sub_domain_brute_rate=1&sub_d ain_scan=1&tcp_ack=1&tcp_syn=1&udp=1&vpc_id=&wait_timeout=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateListGetByType

调用TemplateListGetByType接口v3.1.0 get template by id。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateListGetByTyp e | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| template _ type | Integ er | Body | 否 | 1 | 模版类型 enum[1:资产风险扫描模板类型\|4:可用性监控模板\|5:资产扫描模板]。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -create tm _ | Integer |  | 创建时间。 |
| -creator | String |  | 创建者。 |
| -id | Integer |  | id。 |
| -is default _ | Integer |  | 是否默认。 |
| -name | String |  | 模版名。 |
| -org full id _ _ | String |  | Unknown。 |
| -org id _ | String |  | Unknown。 |

|  |  |  |  | 漏洞扫描开发指南·漏洞扫描 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -type | Integer |  | 模版类型。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateListGetByType&RegionId=cn-hangzhou&template_type=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "creator":"",
            "create_tm":"",
            "org_id":"",
            "name":"",
            "id":"",
            "is_default":"",
            "type":"",
            "org_full_id":""
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
    <data>
        <create_tm></create_tm>
        <creator></creator>
        <id></id>
        <is_default></is_default>
        <name></name>
        <org_full_id></org_full_id>
        <org_id></org_id>
        <type></type>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateRiskScanAdd

调用TemplateRiskScanAdd接口v3.1.0 add risk_scan template api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateRiskScanAdd | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| advanced scan _ | Strin g | Body | 否 |  | 高级扫描配置。 |
| basic sca _ n | Strin g | Body | 否 |  | 基础扫描配置。 |
| emergent scan _ | Strin g | Body | 否 |  | 应急扫描配置。 |
| exclude p _ orts | Strin g | Body | 否 |  | 排除端口。 |
| name | Strin g | Body | 否 | 全量风险扫描模板 | 模版名称。 |
| user agen _ t | Strin g | Body | 否 |  | user agent。 _ |
| vpc id _ | Strin g | Body | 否 |  | vpcID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | Integer | 1 | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateRiskScanAdd&RegionId=cnhangzhou&advanced_scan=&basic_scan=&emergent_scan=&exclude_ports=&name=全量风险扫描模板&us er_agent=&vpc_id=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateAssetDetectionDetail

调用TemplateAssetDetectionDetail接口v3.1.0 get template asset detection detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateAssetDetectio nDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| alive ports _ | String |  | 探活端口。 |
| baseline id _ | Integer |  | 基线id。 |
| baseline name _ | String |  | 基线名。 |
| baseline rule _ | Integer |  | baseline。 |
| custom port _ | String |  | 附加端口。 |
| disable subdo _ main api _ | Integer |  | 子域名接口查询。 |
| disable subdo _ main dict _ | Integer |  | 子域名字典爆破。 |
| exclude ports _ | String |  | 排除端口。 |
| icmp echo _ | Integer |  | ICMP ECHO。 _ |
| inherit attrs _ | Integer |  | 自动同步资产信息。 |
| ip2domain | Integer |  | ip反查域名。 |
| ip scan _ | Integer |  | 自动导入关联ip。 |
| name | String |  | 名称。 |
| no status _ | Integer |  | asset scan。 |
| opt | String |  | 选项。 |
| port area _ | String |  | 端口范围。 |
| retry times _ | Integer |  | 重试次数。 |

| 漏洞扫描开发指南· | 漏洞扫描 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| scan speed _ | String |  | 扫描速率。 |
| sctp | Integer |  | SCTP。 |
| sub domain b _ _ rute rate _ | Integer |  | 子域名爆破速率。 |
| sub domain s _ _ can | Integer |  | 子域名查询。 |
| target type _ | String |  | 目标类型。 |
| tcp ack _ | Integer |  | TCP ACK。 _ |
| tcp syn _ | Integer |  | TCP SYN。 _ |
| type | String |  | 类型。 |
| udp | Integer |  | UDP。 |
| value | String |  | 值。 |
| vpc id _ | String |  | vpcID。 |
| wait timeout _ | Integer |  | 3.4.1。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateAssetDetectionDetail&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "alive_ports":"",
    "baseline_id":"",
    "baseline_name":"",
    "baseline_rule":"",
    "custom_port":"",
    "disable_subdomain_api":"",
    "disable_subdomain_dict":"",
    "exclude_ports":"",
    "icmp_echo":"",
    "inherit_attrs":"",
    "ip2domain":"",
    "ip_scan":"",
    "name":"",
    "no_status":"",
    "opt":"",
    "port_area":"",
    "retry_times":"",
    "scan_speed":"",
    "sctp":"",
    "sub_domain_brute_rate":"",
    "sub_domain_scan":"",
    "target_type":"",
    "tcp_ack":"",
    "tcp_syn":"",
    "type":"",
    "udp":"",
    "value":"",
    "vpc_id":"",
    "wait_timeout":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <alive_ports></alive_ports>
    <baseline_id></baseline_id>
    <baseline_name></baseline_name>
    <baseline_rule></baseline_rule>
    <custom_port></custom_port>
    <disable_subdomain_api></disable_subdomain_api>
    <disable_subdomain_dict></disable_subdomain_dict>
    <exclude_ports></exclude_ports>
    <icmp_echo></icmp_echo>
    <inherit_attrs></inherit_attrs>
    <ip2domain></ip2domain>
    <ip_scan></ip_scan>
    <name></name>
    <no_status></no_status>
    <opt></opt>
    <port_area></port_area>
    <retry_times></retry_times>
    <scan_speed></scan_speed>
    <sctp></sctp>
    <sub_domain_brute_rate></sub_domain_brute_rate>
    <sub_domain_scan></sub_domain_scan>
    <target_type></target_type>
    <tcp_ack></tcp_ack>
    <tcp_syn></tcp_syn>
    <type></type>
    <udp></udp>
    <value></value>
    <vpc_id></vpc_id>
    <wait_timeout></wait_timeout>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### GetAssetImportTaskInfo

调用GetAssetImportTaskInfo接口v3.1.0 get asset_import task info api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:GetAssetImportTaskInf o | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| asset list _ | String |  | 资产列表 1.1.1.1。 |
| tag names _ | String |  | 标签。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| group id _ | Integer | 1 | 组别id。 |
| screen shot _ | Integer | 1 | 是否开启网站截图 enum[0:关闭\|1:开启]。 |
| staff id _ | Integer | 1 | 负责人id。 |
| task name _ | String | test | 任务名称。 |
| template id _ | Integer | 1 | 任务模板ID。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetAssetImportTaskInfo&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "group_id":1,
    "screen_shot":1,
    "staff_id":1,
    "task_name":"test",
    "template_id":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <asset_list>
        <asset_list></asset_list>
    </asset_list>
    <group_id>1</group_id>
    <screen_shot>1</screen_shot>
    <staff_id>1</staff_id>
    <tag_names>
        <tag_name></tag_name>
    </tag_names>
    <task_name>test</task_name>
    <template_id>1</template_id>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### GetRiskScanTaskTemplate

调用GetRiskScanTaskTemplate接口获取风险扫描任务运行时的模版信息。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:GetRiskScanTaskTempl ate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| exclude ports _ | String |  | 排除端口。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| advanced sca _ n | Map |  | 高级扫描。 |
| basic scan _ | Map |  | 基础扫描。 |
| emergent sca _ n | Map |  | 应急扫描。 |
| name | String | 资产扫描模板-测试 | 名称。 |
| user agent _ | String | xxx | UserAgent。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetRiskScanTaskTemplate&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "advanced_scan":"",
    "basic_scan":"",
    "emergent_scan":"",
```

`"name":"`资产扫描模板-测试`",`

```json
    "user_agent":"xxx"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <advanced_scan></advanced_scan>
    <basic_scan></basic_scan>
    <emergent_scan></emergent_scan>
    <exclude_ports>
        <exclude_port></exclude_port>
    </exclude_ports>
```

`<name>`资产扫描模板-测试`</name>`

```xml
    <user_agent>xxx</user_agent>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateDelete

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateDelete | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ids | Strin g | Body | 否 |  | 模版id列表 example: [85,86]。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateDelete&RegionId=cn-hangzhou&ids=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateList

调用TemplateList接口v3.1.0 list all task templates。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TemplateList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2024-08-01 23:59:59 | 时间区间-结束。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| search | Strin g | Body | 否 | 模版 | 搜索条件，支持模版名称的模糊查找。 |
| start time _ | Strin g | Body | 否 | 2024-07-01 00:00:00 | 时间区间-开始。 |
| template _ types | Strin g | Body | 否 |  | 模版类型 enum[1:资产风险扫描模板类型\|4:可用性监控模板\|5:资产扫描模板]。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -create tm _ | Integer |  | 创建时间。 |
| -creator | String |  | 创建者。 |
| -id | Integer |  | id。 |
| -is default _ | Integer |  | 是否默认。 |
| -name | String |  | 模版名。 |
| -org full id _ _ | String |  | Unknown。 |
| -org id _ | String |  | Unknown。 |
| -type | Integer |  | 模版类型。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 总数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateList&RegionId=cn-hangzhou&end_time=2024-08-01 23:59: 59&page=1&page_size=10&search=模版&start_time=2024-07-01 00:00:00&template_types=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "creator":"",
            "create_tm":"",
            "org_id":"",
            "name":"",
            "id":"",
            "is_default":"",
            "type":"",
            "org_full_id":""
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
    <count></count>
    <results>
        <create_tm></create_tm>
        <creator></creator>
        <id></id>
        <is_default></is_default>
        <name></name>
        <org_full_id></org_full_id>
        <org_id></org_id>
        <type></type>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateRiskScanDetail

调用TemplateRiskScanDetail接口v3.1.0 Get template risk_scan detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateRiskScanDeta il | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| exclude ports _ | String |  | 排除端口。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| advanced sca _ n | Map |  | 高级扫描。 |
| basic scan _ | Map |  | 基础扫描。 |
| emergent sca _ n | Map |  | 应急扫描。 |
| name | String | 资产扫描模板-测试 | 名称。 |
| user agent _ | String | xxx | UserAgent。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateRiskScanDetail&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "advanced_scan":"",
    "basic_scan":"",
    "emergent_scan":"",
```

`"name":"`资产扫描模板-测试`",`

```json
    "user_agent":"xxx"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <advanced_scan></advanced_scan>
    <basic_scan></basic_scan>
    <emergent_scan></emergent_scan>
    <exclude_ports>
        <exclude_port></exclude_port>
    </exclude_ports>
```

`<name>`资产扫描模板-测试`</name>`

```xml
    <user_agent>xxx</user_agent>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TemplateWebMonitorConf

调用TemplateWebMonitorConf接口v3.1.0 get web_monitor config api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TemplateWebMonitorC onf | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| default crawl _ _ depth | Integer |  | 默认爬虫深度。 |
| default monito _ r cycle _ | String |  | 默认监控周期。 |
| default url lim _ _ it | Integer |  | 默认URL限制。 |
| monitor optio _ n | Map |  | 监控参数。 |
| scan param _ | Map |  | 扫描参数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TemplateWebMonitorConf&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "default_crawl_depth":"",
    "default_monitor_cycle":"",
    "default_url_limit":"",
    "monitor_option":"",
    "scan_param":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <default_crawl_depth></default_crawl_depth>
    <default_monitor_cycle></default_monitor_cycle>
    <default_url_limit></default_url_limit>
    <monitor_option></monitor_option>
    <scan_param></scan_param>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### BasicRiskOption

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BasicRiskOption | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | Integ er | Body | 否 |  | 风险扫描类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -define | String |  | 定义。 |
| -name | String |  | 名称。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BasicRiskOption&RegionId=cn-hangzhou&type=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "define":"",
            "name":""
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
    <data>
        <define></define>
        <name></name>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### GetCommonVulnItemList

调用GetCommonVulnItemList接口common_vuln_item_list api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:GetCommonVulnItemLi st | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| general ty _ pe | Strin g | Body | 否 |  | 类型。 |
| page | Integ er | Body | 否 |  | 页码。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| page size _ | Integ er | Body | 否 |  | 列表数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -module count _ | Integer |  | 模块数量。 |
| -name | String |  | 漏洞名。 |
| -risk count _ | Integer |  | 风险数。 |
| -status | Integer |  | 漏洞状态。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 分页数据条数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetCommonVulnItemList&RegionId=cnhangzhou&general_type=&page=&page_size=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "risk_count":"",
            "module_count":"",
            "name":"",
            "status":""
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
    <count></count>
    <results>
        <module_count></module_count>
        <name></name>
        <risk_count></risk_count>
        <status></status>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

### 任务相关接口

#### BatchStartTasks

调用BatchStartTasks接口v3.2.0 batch start task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BatchStartTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -task id _ | Integer | 173 | 任务ID。 |
| - task instance _ _ id | Integer | 208 | 任务实例ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BatchStartTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00: 00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "task_instance_id":208,
            "task_id":173
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
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetScanCreate

调用TaskAssetScanCreate接口v3.1.0 create asset_scan task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetScanCreate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cycle | Strin g | Body | 否 | SPEC | 周期 SPEC，MONTH，WEEK。 |
| end tm _ | Strin g | Body | 否 | 24:00 | 结束时间 24:00。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| is immedi _ ately | Integ er | Body | 否 | 1 | 是否立即执行。 |
| month | Strin g | Body | 否 |  | 每月example:[1,2]。 |
| screen sh _ ot | Integ er | Body | 否 | 1 | 屏幕截图 enum[1\|0]。 |
| spec cycl _ e | Integ er | Body | 否 | 1 | 自定义天数。 |
| start tm _ | Strin g | Body | 否 | 2023-09-14 16:36:18 | 开始时间周期任务 00:00 一次性任务 2023-09-14 16:36:18。 |
| targets | Strin g | Body | 否 |  | 检测目标 ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]。 |
| task nam _ e | Strin g | Body | 否 | 风险扫描任务-测试 | 任务名。 |
| template i _ d | Integ er | Body | 否 | 1 | 模版id。 |
| vpc id _ | Strin g | Body | 否 | 1 | vpc id。 _ |
| week | Strin g | Body | 否 |  | 每周 example:[1,2]。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | Integer | 1 | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetScanCreate&RegionId=cnhangzhou&cycle=SPEC&end_tm=24:00&is_immediately=1&month=&screen_shot=1&spec_cycle=1&start m=2023-09-14 16:36:18&targets=&task_name=风险扫描任务-测试&template_id=1&vpc_id=1&week=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskList

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -asset info _ | String |  | 资产信息 1.1.1.1。 |
| -creator | String | admin | 创建者。 |
| -cycle count _ | Integer | 10 | 周期次数。 |
| -end time _ | Integer | 1620000000 | 结束时间。 |
| -id | Integer | 1 | id。 |
| -inster time _ | Integer | 1620000000 | 插入时间。 |
| - is immediately _ | Integer | 1 | 是否立即执行 enum[1:是\|0:否]。 |
| - is public asset _ _ | Integer | 1 | 是否公网资产 enum[1:是\|0:否]。 |
| -process | String | 100% | 进度。 |
| -start time _ | Integer | 1620000000 | 创建时间。 |
| -status | String | INIT | 状态 enum[INIT:初始化\|RUNNING:运行\|FINISH:完成\|STOP:停止]。 |
| -sub type _ | Integer | 1 | 子类型。 |
| -task cycle _ | Integer | 0 | 任务周期。 |
| - task instance _ _ id | Integer | 123 | 任务实例id。 |
| -task name _ | String | 资产扫描任务-测试 | 任务名。 |
| -task type _ | Integer | 6 | 任务类型。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| count | Integer | 10 | 总数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskList&RegionId=cn-hangzhou&end_time=2020-01-01 00:00:00&p age=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":10,
    "results":[
        {
            "cycle_count":10,
```

`"task_name":"`资产扫描任务-测试`",`

```json
            "creator":"admin",
            "process":"100%",
            "end_time":1620000000,
            "inster_time":1620000000,
            "is_public_asset":1,
            "task_instance_id":123,
            "start_time":1620000000,
            "task_cycle":0,
            "sub_type":1,
            "id":1,
            "is_immediately":1,
            "task_type":6,
            "status":"INIT"
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
    <count>10</count>
    <results>
        <asset_info>
            <asset_info></asset_info>
        </asset_info>
        <creator>admin</creator>
        <cycle_count>10</cycle_count>
        <end_time>1620000000</end_time>
        <id>1</id>
        <inster_time>1620000000</inster_time>
        <is_immediately>1</is_immediately>
        <is_public_asset>1</is_public_asset>
        <process>100%</process>
        <start_time>1620000000</start_time>
        <status>INIT</status>
        <sub_type>1</sub_type>
        <task_cycle>0</task_cycle>
        <task_instance_id>123</task_instance_id>
        <task_type>6</task_type>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### BatchStopTasks

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BatchStopTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BatchStopTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00:0 0:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&statuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### BatchDeleteTasks

调用BatchDeleteTasks接口v3.2.0 batch delete task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BatchDeleteTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BatchDeleteTasks&RegionId=cn-hangzhou&end_time=2020-01-01 00 :00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00&s tatuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskProcessV2

调用TaskProcessV2接口v3.1.0 get task process api v2。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskProcessV2 | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| all | Boole an | Body | 否 | True | 是否全部 enum[true\|false]。 |
| insert tm _ _ order | Integ er | Body | 否 | 1 | 插入时间排序 enum[1\|- 1]。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页面数量。 |
| risk type _ | Integ er | Body | 否 | 2 | 风险类型 enum[2:安全漏洞\|3:合规漏洞]。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框。 |
| task insta _ nce id _ | Integ er | Body | 否 | 1 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -insert tm _ | Integer | 1620000000 | 插入时间。 |
| -risk addr _ | String | http://1.1.1.1 | 风险地址。 |
| -risk id _ | Integer | 1 | 风险id。 |
| -risk level _ | String | LOW | 风险等级 enum[LOW:低\|MEDIUM:中\|HIGH: 高]。 |
| -risk name _ | String | xxx安全漏洞 | 风险名称。 |
| -risk type _ | Integer | 3 | 风险类型 enum[2:安全漏洞\|3:合规漏洞]。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 总数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskProcessV2&RegionId=cnhangzhou&all=True&insert_tm_order=1&page=1&page_size=10&risk_type=2&search=1_1_1_1_1&task nstance_id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "risk_addr":"http://1.1.1.1",
            "risk_level":"LOW",
            "risk_id":1,
            "risk_type":3,
            "insert_tm":1620000000,
```

`"risk_name":"xxx`安全漏洞"

```
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
    <count></count>
    <results>
        <insert_tm>1620000000</insert_tm>
        <risk_addr>http://1.1.1.1</risk_addr>
        <risk_id>1</risk_id>
        <risk_level>LOW</risk_level>
        <risk_name>xxx安全漏洞</risk_name>
        <risk_type>3</risk_type>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskStart

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskStart | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -task id _ | Integer | 173 | 任务ID。 |
| - task instance _ _ id | Integer | 208 | 任务实例ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskStart&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "task_instance_id":208,
            "task_id":173
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
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskStop

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskStop | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskStop&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### BatchSuspendTasks

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BatchSuspendTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |

|  |  |  |  |  | 漏洞扫描开发指南·漏洞扫描 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BatchSuspendTasks&RegionId=cn-hangzhou&end_time=2020-01-01 0 0:00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00& statuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskProcess

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskProcess | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| all | Boole an | Body | 否 | True | 是否全部 enum[true\|false]。 |
| insert tm _ _ order | Integ er | Body | 否 | 1 | 插入时间排序 enum[1\|- 1]。 |
| page | Integ er | Body | 否 | 1 | 页码。 |

|  |  |  |  |  | 漏洞扫描开发指南·漏洞扫描 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| page size _ | Integ er | Body | 否 | 10 | 页面数量。 |
| risk type _ | Integ er | Body | 否 | 2 | 风险类型 enum[2:安全漏洞\|3:合规漏洞]。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框。 |
| task insta _ nce id _ | Integ er | Body | 否 | 1 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -asset id _ | Integer | 1 | 资产ID。 |
| -behavior | String | 检测网站：.... | 行为。 |
| -id | Integer | 1 | ID。 |
| -insert tm _ | Integer | 1620000000 | 插入时间。 |
| -is deleted _ | Integer | 0 | 是否删除 enum[1:是\|0:否]。 |
| -risk id _ | Integer | 1 | 风险ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 分页数据条数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskProcess&RegionId=cnhangzhou&all=True&insert_tm_order=1&page=1&page_size=10&risk_type=2&search=1_1_1_1_1&task nstance_id=1
```

正常返回示例 `JSON` 格式

|  | HTTP/1.1 200 OK Content-Type:application/json { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "count":"", "results":[ { "risk id":1, _ "is deleted":0, _ "insert tm":1620000000, _ "asset id":1, _ "id":1, "behavior":"检测网站：...." } ] } |
|---|---|

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count></count>
    <results>
        <asset_id>1</asset_id>
```

`<behavior>`检测网站：`....</behavior>`

```xml
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>0</is_deleted>
        <risk_id>1</risk_id>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskRestart

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskRestart | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -task id _ | Integer | 173 | 任务ID。 |
| - task instance _ _ id | Integer | 208 | 任务实例ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskRestart&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "task_instance_id":208,
            "task_id":173
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
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskDelete

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:TaskDelete | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskDelete&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskRiskScanDetail

调用TaskRiskScanDetail接口v3.1.0 get risk_scan task detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskRiskScanDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| targets | Array |  |  |
| -target | String |  | 目标。 |
| -type | String | ALL | 类型。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle count _ | Integer | 10 | 循环次数。 |

|  |  |  | 漏洞扫描开发指南·漏洞扫描 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| finish time _ | Integer | 1600000000 | 结束时间。 |
| host risk coun _ _ t | Integer | 10 | 主机漏洞数。 |
| id | Integer | 1 | ID。 |
| insert tm _ | Integer | 1600000000 | 插入时间。 |
| name | String | xx风险扫描 | 名称。 |
| process | String | 100% | 进度。 |
| risk count _ | Integer | 10 | 安全漏洞数。 |
| start tm _ | Integer | 1600000000 | 开始时间。 |
| status | String | RUNNING | 运行状态 enum: [INIT\|RUNNING\|STOP\|FINISH]。 |
| task instance _ _ id | Integer | 1 | 任务实例ID。 |
| template id _ | Integer | 1 | 任务模板ID。 |
| template nam _ e | String | xx风险扫描模板 | 任务模板名。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskRiskScanDetail&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "host_risk_count":10,
    "id":1,
    "insert_tm":1600000000,
```

`"name":"xx`风险扫描`",`

```json
    "process":"100%",
    "risk_count":10,
    "start_tm":1600000000,
    "status":"RUNNING",
    "targets":[
        {
            "type":"ALL"
        }
```

`],`

```json
    "task_instance_id":1,
    "template_id":1,
```

`"template_name":"xx`风险扫描模板"

```
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <host_risk_count>10</host_risk_count>
    <id>1</id>
    <insert_tm>1600000000</insert_tm>
```

`<name>xx`风险扫描`</name>`

```xml
    <process>100%</process>
    <risk_count>10</risk_count>
    <start_tm>1600000000</start_tm>
    <status>RUNNING</status>
    <targets>
        <target>
            <target></target>
        </target>
        <type>ALL</type>
    </targets>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<template_name>xx`风险扫描模板`</template_name>`

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### GetAssetScanTaskInfo

调用GetAssetScanTaskInfo接口v3.1.0 get asset_scan task info api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:GetAssetScanTaskInfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| month | Integer |  | 每月example:[1,2]。 |
| week | Integer |  | 每周 example:[1,2]。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle | String | SPEC | 周期 SPEC，MONTH，WEEK。 |

|  | 漏洞扫描开发指南· | 漏洞扫描 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| end tm _ | String | 24:00 | 结束时间 24:00。 |
| is immediately _ | Integer | 1 | 是否立即执行。 |
| screen shot _ | Integer | 1 | 截屏 enum[0:关闭\|1:开启]。 |
| spec cycle _ | Integer | 1 | 自定义天数。 |
| start tm _ | String | 2023-09-14 16:36:18 | 开始时间周期任务 00:00 一次性任务 2023- 09-14 16:36:18。 |
| targets | Map |  | 目标。 |
| task name _ | String | test | 任务名。 |
| task type _ | Integer | 6 | 任务类型。 |
| template id _ | Integer | 1 | 模版id。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetAssetScanTaskInfo&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":"SPEC",
    "end_tm":"24:00",
    "is_immediately":1,
    "screen_shot":1,
    "spec_cycle":1,
    "start_tm":"2023-09-14 16:36:18",
    "targets":"",
    "task_name":"test",
    "task_type":6,
    "template_id":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>SPEC</cycle>
    <end_tm>24:00</end_tm>
    <is_immediately>1</is_immediately>
    <month>
        <month></month>
    </month>
    <screen_shot>1</screen_shot>
    <spec_cycle>1</spec_cycle>
    <start_tm>2023-09-14 16:36:18</start_tm>
    <targets></targets>
    <task_name>test</task_name>
    <task_type>6</task_type>
    <template_id>1</template_id>
    <week>
        <week></week>
    </week>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetImportDetail

调用TaskAssetImportDetail接口v3.1.0 get task asset import detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetImportDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| asset typ _ e | Strin g | Body | 否 | IP | 资产类型 enum[IP\|WEBSITE\|DOMA IN]。 |
| is new _ | Integ er | Body | 否 | 1 | 是否新上线。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页面数量。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框。 |
| task insta _ nce id _ | Integ er | Body | 否 | 1 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -children | String |  | 子资产。 |
| -asset name _ | String | 1.1.1.1 | 资产名。 |
| -asset source _ | String | 主机导入 | 资产源。 |
| -has childs _ | Integer | 0 | 是否子资产 enum[1:是\|0:否]。 |
| -id | Integer | 1 | ID。 |
| -insert tm _ | Integer | 1620000000 | 插入时间。 |
| -is deleted _ | Boolean | False | 是否删除 enum[1:是\|0:否]。 |
| -is new _ | Integer | 1 | 是否新发现 enum[1:是\|0:否]。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - task instance _ _ id | Integer | 1 | 任务实例ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 分页数据条数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetImportDetail&RegionId=cnhangzhou&asset_type=IP&is_new=1&page=1&page_size=10&search=1_1_1_1_1&task_instance_id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
```

`"asset_source":"`主机导入`",`

```json
            "task_instance_id":1,
            "has_childs":0,
            "insert_tm":1620000000,
            "id":1
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
    <count></count>
    <results>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>主机导入</asset_source>
        <children>
            <children></children>
        </children>
        <has_childs>0</has_childs>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
        <task_instance_id>1</task_instance_id>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetScanDetail

调用TaskAssetScanDetail接口v3.1.0 get asset_scan task detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetScanDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| targets | Array |  |  |
| -target | String |  | 目标。 |
| -type | String | ALL | 类型。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle count _ | Integer | 10 | 循环次数。 |
| finish time _ | Integer | 1600000000 | 结束时间。 |
| host risk coun _ _ t | Integer | 10 | 主机漏洞数。 |
| id | Integer | 1 | ID。 |
| import count _ | Map |  | 导入数量。 |
| insert tm _ | Integer | 1600000000 | 插入时间。 |
| name | String | xx资产扫描 | 名称。 |
| process | String | 100% | 进度。 |
| risk count _ | Integer | 10 | 安全漏洞数。 |
| start tm _ | Integer | 1600000000 | 开始时间。 |
| status | String | RUNNING | 运行状态 enum: [INIT\|RUNNING\|STOP\|FINISH]。 |
| task instance _ _ id | Integer | 1 | 任务实例ID。 |

| 漏洞扫描开发指南· | 漏洞扫描 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| template id _ | Integer | 1 | 任务模板ID。 |
| template nam _ e | String | xx资产扫描模板 | 任务模板名。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetScanDetail&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "host_risk_count":10,
    "id":1,
    "import_count":"",
    "insert_tm":1600000000,
```

`"name":"xx`资产扫描`",`

```json
    "process":"100%",
    "risk_count":10,
    "start_tm":1600000000,
    "status":"RUNNING",
    "targets":[
        {
            "type":"ALL"
        }
```

`],`

```json
    "task_instance_id":1,
    "template_id":1,
```

`"template_name":"xx`资产扫描模板"

```
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <host_risk_count>10</host_risk_count>
    <id>1</id>
    <import_count></import_count>
    <insert_tm>1600000000</insert_tm>
```

`<name>xx`资产扫描`</name>`

```xml
    <process>100%</process>
    <risk_count>10</risk_count>
    <start_tm>1600000000</start_tm>
    <status>RUNNING</status>
    <targets>
        <target>
            <target></target>
        </target>
        <type>ALL</type>
    </targets>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<template_name>xx`资产扫描模板`</template_name>`

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetImportChildDetail

调用TaskAssetImportChildDetail接口v3.1.0 get import asset child task detail api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetImportChildD etail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| asset id _ | Integ er | Body | 否 | 1 | 资产id。 |
| is new _ | Integ er | Body | 否 | 1 | 是否新上线 enum[1\|0]。 |
| task insta _ nce id _ | Integ er | Body | 否 | 1 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -children | String |  | 子资产。 |
| -asset name _ | String | 1.1.1.1 | 资产名。 |
| -asset source _ | String | 主机导入 | 资产源。 |
| -has childs _ | Integer | 0 | 是否子资产 enum[1:是\|0:否]。 |
| -id | Integer | 1 | ID。 |
| -insert tm _ | Integer | 1620000000 | 插入时间。 |
| -is deleted _ | Boolean | False | 是否删除 enum[1:是\|0:否]。 |
| -is new _ | Integer | 1 | 是否新发现 enum[1:是\|0:否]。 |
| - task instance _ _ id | Integer | 1 | 任务实例ID。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetImportChildDetail&RegionId=cnhangzhou&asset_id=1&is_new=1&task_instance_id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
```

`"asset_source":"`主机导入`",`

```json
            "task_instance_id":1,
            "has_childs":0,
            "insert_tm":1620000000,
            "id":1
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
    <data>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>主机导入</asset_source>
        <children>
            <children></children>
        </children>
        <has_childs>0</has_childs>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
        <task_instance_id>1</task_instance_id>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### CycleTaskAssetStats

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:CycleTaskAssetStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=CycleTaskAssetStats&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetScanCycleRunning

调用TaskAssetScanCycleRunning接口v3.4.0 获取资产巡检任务是否有周期任务。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetScanCycleRu nning | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetScanCycleRunning&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetImport

调用TaskAssetImport接口v3.1.0 import asset task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetImport | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| asset met _ adatas | Strin g | Body | 否 |  | 资产元数据。 |
| content m _ onitor | Integ er | Body | 否 |  |  |
| customize asset list _ _ | Strin g | Body | 否 |  |  |
| group id _ | Integ er | Body | 否 | 0 | 组别id。 |
| is immedi _ ately | Integ er | Body | 否 | 1 | 4.1.1。 |
| is public _ _ asset | Integ er | Body | 否 |  | 是否公网资产。 |
| network t _ ype | Integ er | Body | 否 | 1 | 网络类型 1, 2。 |
| not alive _ _ report | Integ er | Body | 否 | 1 | 非存活资产是否上报。 |
| screen sh _ ot | Integ er | Body | 否 | 1 | 是否开启网站截图 1 开启 0 关闭。 |
| staff id _ | Integ er | Body | 否 | 1 | 负责人id。 |
| start tm _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| tag ids _ | Strin g | Body | 否 |  | 标签id [1,2,3]。 |
| targets | Strin g | Body | 否 |  | 检测目标 ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]。 |
| task nam _ e | Strin g | Body | 否 | 风险扫描任务-测试 | 任务名。 |
| template i _ d | Integ er | Body | 否 | 1 | 模版id。 |
| vpc id _ | Strin g | Body | 否 | 1 | vpc id。 _ |
| web moni _ tor | Integ er | Body | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | Integer | 1 | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetImport&RegionId=cnhangzhou&asset_metadatas=&group_id=0&is_immediately=1&is_public_asset=&network_type=1&not live_report=1&screen_shot=1&staff_id=1&start_tm=2020-01-01 00:00:00&tag_ids=&targets=&task_name=风险扫描任务-测试&template_id=1&vpc_id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskRiskScanCreate

调用TaskRiskScanCreate接口v3.1.0 create risk scan task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskRiskScanCreate | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cycle | Strin g | Body | 否 | SPEC | 周期 SPEC，MONTH，WEEK。 |
| end tm _ | Strin g | Body | 否 | 24:00 | 结束时间 24:00。 |
| is immedi _ ately | Integ er | Body | 否 | 1 | 是否立即执行。 |
| month | Strin g | Body | 否 |  | 每月example:[1,2]。 |
| scan spee _ d | Strin g | Body | 否 |  | 扫描速率废弃。 |
| spec cycl _ e | Integ er | Body | 否 | 1 | 自定义天数。 |
| start tm _ | Strin g | Body | 否 | 2023-09-14 16:36:18 | 开始时间周期任务 00:00 一次性任务 2023-09-14 16:36:18。 |
| targets | Strin g | Body | 否 |  | 检测目标 ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3]。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task nam _ e | Strin g | Body | 否 | 风险扫描任务-测试 | 任务名。 |
| template i _ d | Integ er | Body | 否 | 1 | 模版id。 |
| vpc id _ | Strin g | Body | 否 | 1 | vpc id。 _ |
| week | Strin g | Body | 否 |  | 每周 example:[1,2]。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | Integer | 1 | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskRiskScanCreate&RegionId=cnhangzhou&cycle=SPEC&end_tm=24:00&is_immediately=1&month=&scan_speed=&spec_cycle=1&start_t 2023-09-14 16:36:18&targets=&task_name=风险扫描任务-测试&template_id=1&vpc_id=1&week=
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data>1</data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetImportDetailExists

调用TaskAssetImportDetailExists接口v3.1.0 get asset import task existed task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetImportDetail Exists | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| asset typ _ e | Strin g | Body | 否 | IP | 资产类型 enum[IP\|WEBSITE\|DOMA IN]。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页面数量。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框。 |
| task insta _ nce id _ | Integ er | Body | 否 | 1 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -asset name _ | String | 1.1.1.1 | 资产名。 |
| -asset source _ | String | 主机导入 | 资产源。 |
| -id | Integer | 1 | ID。 |
| -insert tm _ | Integer | 1620000000 | 插入时间。 |
| -is deleted _ | Boolean | False | 是否删除 enum[0:未删除 1:已删除]。 |
| -is new _ | Integer | 1 | 是否新发现 enum[0:否 1:是]。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | 分页数据条数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetImportDetailExists&RegionId=cnhangzhou&asset_type=IP&page=1&page_size=10&search=1_1_1_1_1&task_instance_id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "is_deleted":false,
            "asset_name":"1.1.1.1",
            "is_new":1,
```

`"asset_source":"`主机导入`",`

```json
            "insert_tm":1620000000,
            "id":1
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
    <count></count>
    <results>
        <asset_name>1.1.1.1</asset_name>
        <asset_source>主机导入</asset_source>
        <id>1</id>
        <insert_tm>1620000000</insert_tm>
        <is_deleted>False</is_deleted>
        <is_new>1</is_new>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskQueueTaskDetail

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskQueueTaskDetail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Strin g | Body | 否 | 207 1 1 11 0 _ _ _ _ | 子任务id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| result | Map |  | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskQueueTaskDetail&RegionId=cn-hangzhou&id=207_1_1_11_0
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "result":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <result></result>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskAssetImportBaseInfo

调用TaskAssetImportBaseInfo接口v3.1.0 get task asset import base info api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskAssetImportBaseIn fo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task insta _ nce id _ | Integ er | Body | 否 | 85 | 任务实例id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle count _ | Integer | 10 | 任务周期。 |
| finish time _ | Integer | 1600000000 | 结束时间。 |
| id | Integer | 1 | 任务ID。 |
| import count _ | Map |  | 导入数量。 |
| import mode _ | String | MANUAL IMPORT _ | 导入方式 enum[MANUAL IMPORT:手动导 _ 入\|EXCEL IMPORT:模版导入]。 _ |
| import res _ | Map |  | 导入数据。 |
| insert tm _ | Integer | 1600000000 | 插入时间。 |
| is immediately _ | Integer | 1 | 是否立即执行 enum[1:是\|0:否]。 |
| is public asset _ _ | Integer | 1 | 是否公网资产导入 enum[1:是\|0:否]。 |
| network type _ | Integer | 1 | 网络类型废弃。 |
| not alive repo _ _ rt | Integer | 1 | 非存活资产是否上报 enum[1:是\|0:否]。 |
| process | String | 100% | 进度。 |
| screen shot _ | Integer | 1 | 是否开启网站截图, 模版导入。 |
| start time _ | Integer | 1600000000 | 开始时间。 |
| status | String | INIT | 运行状态 enum[INIT:初始化\|RUNNING:运行中\|FINISH:完成\|STOP:停止]。 |
| target | Map |  | 目标废弃。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| task instance _ _ id | Integer | 1 | 任务实例ID。 |
| task name _ | String | 资产扫描任务-测试 | 任务名。 |
| template id _ | Integer | 1 | 任务模板ID。 |
| template nam _ e | String | 资产扫描模板-测试 | 任务模板名。 |
| username | String | admin | 用户名。 |
| view detail _ | Map |  | 查看详情返回一个MAP或者一个下载链接和导入方式相关。 |
| vpc id _ | String | 1 | VPCID。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskAssetImportBaseInfo&RegionId=cnhangzhou&task_instance_id=85
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle_count":10,
    "finish_time":1600000000,
    "id":1,
    "import_count":"",
    "import_mode":"MANUAL_IMPORT",
    "import_res":"",
    "insert_tm":1600000000,
    "is_immediately":1,
    "is_public_asset":1,
    "network_type":1,
    "not_alive_report":1,
    "process":"100%",
    "screen_shot":1,
    "start_time":1600000000,
    "status":"INIT",
    "target":"",
    "task_instance_id":1,
```

`"task_name":"`资产扫描任务-测试`",`

```json
    "template_id":1,
```

`"template_name":"`资产扫描模板-测试`",`

```json
    "username":"admin",
    "view_detail":"",
    "vpc_id":"1"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle_count>10</cycle_count>
    <finish_time>1600000000</finish_time>
    <id>1</id>
    <import_count></import_count>
    <import_mode>MANUAL_IMPORT</import_mode>
    <import_res></import_res>
    <insert_tm>1600000000</insert_tm>
    <is_immediately>1</is_immediately>
    <is_public_asset>1</is_public_asset>
    <network_type>1</network_type>
    <not_alive_report>1</not_alive_report>
    <process>100%</process>
    <screen_shot>1</screen_shot>
    <start_time>1600000000</start_time>
    <status>INIT</status>
    <target></target>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<template_name>`资产扫描模板-测试`</template_name>`

```xml
    <username>admin</username>
    <view_detail></view_detail>
    <vpc_id>1</vpc_id>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskRiskScanCycleRunning

调用TaskRiskScanCycleRunning接口v3.4.0 获取风险扫描任务是否有任务。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskRiskScanCycleRun ning | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskRiskScanCycleRunning&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### GetAssetRiskScanTaskInfo

调用GetAssetRiskScanTaskInfo接口v3.1.0 get asset_risk_scan task info api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:GetAssetRiskScanTaskI nfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integ er | Body | 否 | 1 | Unknown。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| month | Integer |  | 每月example:[1,2]。 |
| week | Integer |  | 每周 example:[1,2]。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle | String | SPEC | 周期 SPEC，MONTH，WEEK。 |
| end tm _ | String | 24:00 | 结束时间 24:00。 |
| is immediately _ | Integer | 1 | 是否立即执行。 |
| scan speed _ | String |  | 扫描速度废弃。 |
| spec cycle _ | Integer | 1 | 自定义天数。 |

|  | 漏洞扫描开发指南· | 漏洞扫描 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| start tm _ | String | 2023-09-14 16:36:18 | 开始时间周期任务 00:00 一次性任务 2023- 09-14 16:36:18。 |
| targets | Map |  | 扫描目标,JSON格式 {'ALL IP':0,'ALL WEBSITE':0,'ALL ASSET':0 _ _ _ ,'IP':[1],'WEBSITE':[1],'GROUP':[1]}序列化， 每次请求只可选择其中一项作为请求内容数组中为对应id，其他为是否选择,0:未选择,1:选择。 |
| task name _ | String | test | 任务名称。 |
| task type _ | Integer | 6 | 任务类型。 |
| template id _ | Integer | 1 | 任务模板ID。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetAssetRiskScanTaskInfo&RegionId=cn-hangzhou&id=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":"SPEC",
    "end_tm":"24:00",
    "is_immediately":1,
    "scan_speed":"",
    "spec_cycle":1,
    "start_tm":"2023-09-14 16:36:18",
    "targets":"",
    "task_name":"test",
    "task_type":6,
    "template_id":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>SPEC</cycle>
    <end_tm>24:00</end_tm>
    <is_immediately>1</is_immediately>
    <month>
        <month></month>
    </month>
    <scan_speed></scan_speed>
    <spec_cycle>1</spec_cycle>
    <start_tm>2023-09-14 16:36:18</start_tm>
    <targets></targets>
    <task_name>test</task_name>
    <task_type>6</task_type>
    <template_id>1</template_id>
    <week>
        <week></week>
    </week>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### BatchRestartTasks

调用BatchRestartTasks接口v3.2.0 batch restart task api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:BatchRestartTasks | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| end time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 结束时间。 |
| page | Integ er | Body | 否 | 1 | 页码。 |
| page size _ | Integ er | Body | 否 | 10 | 页大小。 |
| parent ta _ sk id _ | Integ er | Body | 否 |  |  |
| run types _ | Strin g | Body | 否 |  | 运行方式，cycle，once, immediately。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 任务ID;任务名称；资产地址。 |
| start time _ | Strin g | Body | 否 | 2020-01-01 00:00:00 | 开始时间。 |
| statuses | Strin g | Body | 否 |  | 任务状态枚举值: RUNNING\|INIT\|FINISH\|ST OP。 |
| task id _ | Integ er | Body | 否 | 1 | 任务id。 |
| task ids _ | Strin g | Body | 否 |  | 任务id example:[1,2,3]。 |
| task types _ | Strin g | Body | 否 |  | 任务类型枚举值: assetImport\|assetRisk\|a ssetScan。 |
| template | Integ er | Body | 否 | 1 | 模版。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -task id _ | Integer | 173 | 任务ID。 |
| - task instance _ _ id | Integer | 208 | 任务实例ID。 |

|  |  |  | 漏洞扫描开发指南·漏洞扫描 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=BatchRestartTasks&RegionId=cn-hangzhou&end_time=2020-01-01 0 0:00:00&page=1&page_size=10&run_types=&search=1_1_1_1_1&start_time=2020-01-01 00:00:00& statuses=&task_id=1&task_ids=&task_types=&template=1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "task_instance_id":208,
            "task_id":173
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
    <data>
        <task_id>173</task_id>
        <task_instance_id>208</task_instance_id>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskQueueTaskList

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskQueueTaskList | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| page | Integ er | Body | 否 | 1 | 页数。 |
| page size _ | Integ er | Body | 否 | 10 | 页面大小。 |
| search | Strin g | Body | 否 | 1 1 1 1 1 _ _ _ _ | 过滤条件，暂时只支持过滤子任务id的模式匹配。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -group id _ | Integer | 0 | 设备组编号。 |
| -id | String | 0 11 0 _ _ | 队列名称。 |
| -list type _ | String | asset list _ | 队列类型 enum[asset list\|vuln list]。 _ _ |

|  |  |  |  | 漏洞扫描开发指南·漏洞扫描 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskQueueTaskList&RegionId=cnhangzhou&page=1&page_size=10&search=1_1_1_1_1
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "list_type":"asset_list",
            "group_id":0,
            "id":"0_11_0"
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
    <count></count>
    <results>
        <group_id>0</group_id>
        <id>0_11_0</id>
        <list_type>asset_list</list_type>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskQueueTaskInfo

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskQueueTaskInfo | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| mode | Integ er | Body | 否 | 1 | 任务状态 enum[0:等待中 ｜1:正在执行]。 |
| page | Integ er | Body | 否 | 1 | 页数。 |
| page size _ | Integ er | Body | 否 | 10 | 页面大小。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -insert tm _ | Integer | 1722477664 | 任务创建时间，时间戳格式。 |
| - task instance _ _ id | Integer | 206 | 任务实例id。 |

|  |  |  |  | 漏洞扫描开发指南·漏洞扫描 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -task name _ | String | dd | 任务名称。 |
| -task pri _ | String | high | 任务优先级 enum[emergent\|high\|mid\|low]。 |
| -task run num _ _ | Integer | 1 | 执行中的任务数。 |
| -task type _ | String | asset monitor task _ _ | 任务类型。 |
| - task wait num _ _ | Integer | 2 | 等待中的任务数。 |
| -username | String | admin | 用户名称。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskQueueTaskInfo&RegionId=cnhangzhou&mode=1&page=1&page_size=10
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "task_name":"dd",
            "task_wait_num":2,
            "task_instance_id":206,
            "insert_tm":1722477664,
            "task_type":"asset_monitor_task",
            "task_run_num":1,
            "task_pri":"high",
            "username":"admin"
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
    <count></count>
    <results>
        <insert_tm>1722477664</insert_tm>
        <task_instance_id>206</task_instance_id>
        <task_name>dd</task_name>
        <task_pri>high</task_pri>
        <task_run_num>1</task_run_num>
        <task_type>asset_monitor_task</task_type>
        <task_wait_num>2</task_wait_num>
        <username>admin</username>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskStatusStats

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskStatusStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  |  |
| -count | Integer | 10 | 数量。 |
| -status | String | RUNNING | 状态。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskStatusStats&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":[
        {
            "count":10,
            "status":"RUNNING"
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
    <data>
        <count>10</count>
        <status>RUNNING</status>
    </data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskQueueTaskListDetail

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskQueueTaskListDet ail | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| list name _ | Strin g | Body | 否 | 0 11 0 _ _ | 列表中的队列名称。 |
| page | Integ er | Body | 否 | 1 | 页数。 |
| page size _ | Integ er | Body | 否 | 10 | 页面大小。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -id | String | 208 1 1 11 0 _ _ _ _ | 任务ID。 |
| -list type _ | String | asset monitor task _ _ | 任务类型 enum[asset import task\|asset monitor ta _ _ _ _ sk\|basic monitor task\|vuln verify task]。 _ _ _ _ |
| -name | String | dd | 任务名称。 |
| -task level _ | String | high | 任务优先级 enum[emergent\|high\|mid\|low]。 |
| -user name _ | String | admin | 用户名。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer |  | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskQueueTaskListDetail&RegionId=cnhangzhou&list_name=0_11_0&page=1&page_size=10
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":"",
    "results":[
        {
            "list_type":"asset_monitor_task",
            "user_name":"admin",
            "name":"dd",
            "id":"208_1_1_11_0",
            "task_level":"high"
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
    <count></count>
    <results>
        <id>208_1_1_11_0</id>
        <list_type>asset_monitor_task</list_type>
        <name>dd</name>
        <task_level>high</task_level>
        <user_name>admin</user_name>
    </results>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskRunTypeStats

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskRunTypeStats | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| cycle | Integer | 10 | 周期性。 |
| immediately | Integer | 10 | 立即执行。 |
| once | Integer | 10 | 定时执行。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskRunTypeStats&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "cycle":10,
    "immediately":10,
    "once":10
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <cycle>10</cycle>
    <immediately>10</immediately>
    <once>10</once>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### TaskQueueTaskCount

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:TaskQueueTaskCount | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| await | Integer | 7 | 等待中任务数。 |
| run | Integer | 2 | 正在执行任务数。 |

|  |  |  | 漏洞扫描开发指南·漏洞扫描 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| task queue _ | Integer | 1 | 任务队列数。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=TaskQueueTaskCount&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "await":7,
    "run":2,
    "task_queue":1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <await>7</await>
    <run>2</run>
    <task_queue>1</task_queue>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

#### SuspendStatus

调用SuspendStatus接口system updates suspend api。

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:SuspendStatus | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| data | String |  | Unknown。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=SuspendStatus&RegionId=cn-hangzhou
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "data":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <data></data>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

## 漏洞扫描V2

### 资产相关接口

#### 主机资产

##### DescribeHostAssetList

获取主机资产列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeHostAssetList | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | vpc- l0miygn8aj171l811 5eg1 | VPC ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 资产负责人ID |
| tag ids _ | String | body | 否 | [11, 22] | 资产标签ID |
| is alive _ | Boolean | body | 否 | true | 是否存活 |

| asset source _ | String | body | 否 | ["AUTO", "MANUAL"] | 资产来源 MANUAL:手工导入 AUTO: 自动导入 |
|---|---|---|---|---|---|
| changings | String | body | 否 | ["NEW", "UPDATED"] | 资产变动 NEW:新上线 UPDATED:有更新 SAME:无更新 OFFLINE:已下线 |
| device types _ | String | body | 否 | ["net product- _ server", "net product- _ router"] | 设备类型 |
| fingerprints | String | body | 否 | ["PHP", "Apache"] | 资产指纹 |
| host port _ | String | body | 否 | [22, 3306] | 主机端口 |
| host service _ | String | body | 否 | ["ssh", "http"] | 主机服务 |
| insert tm en _ _ d | String | body | 否 | 2024-02-04 00:00:00 | 资产导入时间-止 |
| insert tm sta _ _ rt | String | body | 否 | 2024-01-04 00:00:00 | 资产导入时间-起 |
| is cdn _ | Boolean | body | 否 | true | 是否存在cdn识别 |
| os | String | body | 否 | ["Ubuntu", "Debian"] | 操作系统 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 20 | 每页返回数量 |
| risk levels _ | String | body | 否 | ["HIGH","MIDDLE"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 HEALTH:安全 |
| search | String | body | 否 | 192.168 | 搜索内容 |

| update tm e _ _ nd | String | body | 否 | 2024-02-04 00:00:00 | 资产更新时间-止 |
|---|---|---|---|---|---|
| update tm st _ _ art | String | body | 否 | 2024-01-04 00:00:00 | 资产更新时间-起 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | VPC ID |
| results[].asset id _ | Integer | 123 | 资产ID |
| results[].group id _ | Integer | 1 | 分组ID |
| results[].asset name _ | String | 192.168.100.100 | 资产名 |
| results[].group name _ | String | this is a group name | 分组名称 |
| results[].asset type _ | String | IP | 资产类型 |
| results[].status | String | OK | 状态 |
| results[].risk level _ | String | HIGH | 风险等级 |
| results[].changing | String | NEW | 资产改变类型 |
| results[].is alive _ | Integer | 1 | 存活状态 |

| results[].hostname | String | 192.168.100.100 | 主机名 |
|---|---|---|---|
| results[].service count _ | Integer | 100 | 开放端口数量 |
| results[].risk count _ | Integer | 100 | 安全漏洞个数 |
| results[].compliance ri _ sk count _ | Integer | 100 | 合规漏洞数量 |
| results[].remark | String | this is a reremark | 备注 |
| results[].cdn | String |  | CDN识别 |
| results[].finger print _ | Array | [{}] | 指纹 |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | 资产标签 |
| results[].asset tags[].t _ ag id _ | Integer | 11 | 资产标签ID |
| results[].asset tags[].t _ ag name _ | String | EIP | 标签名 |
| results[].staff | Object | {} | 负责人信息 |
| results[].asset source _ | String | System Discovered | 资产来源 |
| results[].device types _ | Array | [""] | 设备类型 |
| results[].os | String | Ubuntu | 操作系统 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].scan tm _ | Integer | 1774428275 | 扫描时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeHostAssetList&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "is_alive": true,
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "device_types": [
    "net_product-server",
    "net_product-router"
```

`],`

```json
  "fingerprints": [
    "PHP",
    "Apache"
```

`],`

```json
  "host_port": [
    22,
```

`],`

```json
  "host_service": [
    "ssh",
    "http"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_cdn": true,
  "os": [
    "Ubuntu",
    "Debian"
```

`],`

```json
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "this is a group name",
      "asset_type": "IP",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "hostname": "192.168.100.100",
      "service_count": 100,
      "risk_count": 100,
      "compliance_risk_count": 100,
      "remark": "this is a reremark",
      "cdn": "",
      "finger_print": [
        {}
```

`],`

```json
      "asset_tags": [
        {
          "tag_id": 11,
          "tag_name": "EIP"
        }
```

`],`

```json
      "staff": {},
      "asset_source": "System Discovered",
      "device_types": [
```

`""` `],`

```json
      "os": "Ubuntu",
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>this is a group name</group_name>
            <asset_type>IP</asset_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <hostname>192.168.100.100</hostname>
            <service_count>100</service_count>
            <risk_count>100</risk_count>
            <compliance_risk_count>100</compliance_risk_count>
            <remark>this is a reremark</remark>
            <cdn></cdn>
            <finger_print>
                <item></item>
            </finger_print>
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <asset_source>System Discovered</asset_source>
            <device_types>
                <item></item>
            </device_types>
            <os>Ubuntu</os>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 网站资产

##### DescribeWebsiteAssetList

获取网站资产列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeWebsiteAssetL ist | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | vpc- l0miygn8aj171l811 5eg1 | VPC ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 资产负责人ID |
| tag ids _ | String | body | 否 | [11, 22] | 资产标签ID |
| website type _ | String | body | 否 | ["IP", "DOMAIN"] | 网站类型 DOMAIN:域名类网站 IP:IP类网站 |
| is alive _ | Boolea n | body | 否 | true | 是否存活 |

| asset source _ | String | body | 否 | ["AUTO", "MANUAL"] | 资产来源 MANUAL:手工导入 AUTO: 自动导入 |
|---|---|---|---|---|---|
| changings | String | body | 否 | ["NEW", "UPDATED"] | 资产变动 NEW:新上线 UPDATED:有更新 SAME:无更新 OFFLINE:已下线 |
| fingerprints | String | body | 否 | ["PHP", "Apache"] | 资产指纹 |
| insert tm end _ _ | String | body | 否 | 2024-02-04 00:00:00 | 资产导入时间-止 |
| insert tm start _ _ | String | body | 否 | 2024-01-04 00:00:00 | 资产导入时间-起 |
| is waf _ | Boolea n | body | 否 | true | 是否存在waf防护 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 20 | 每页返回数量 |
| risk levels _ | String | body | 否 | ["HIGH","MIDDLE"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 HEALTH:安全 |
| search | String | body | 否 | https://163.com | 搜索内容 |
| status codes _ | String | body | 否 | [403, 404] | http状态码 |
| update tm end _ _ | String | body | 否 | 2024-02-04 00:00:00 | 资产更新时间-止 |
| update tm start _ _ | String | body | 否 | 2024-01-04 00:00:00 | 资产更新时间-起 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | VPC ID |
| results[].asset id _ | Integer | 123 | 资产ID |
| results[].group id _ | Integer | 1 | 分组ID |
| results[].asset name _ | String | 192.168.100.100 | 资产名 |
| results[].group name _ | String | this is a group name | 分组名称 |
| results[].asset type _ | String | IP | 资产类型 |
| results[].website type _ | String | DOMAIN | 网站类型 |
| results[].status | String | OK | 状态 |
| results[].risk level _ | String | HIGH | 风险等级 |
| results[].changing | String | NEW | 资产改变类型 |
| results[].is alive _ | Integer | 1 | 存活状态 |
| results[].service | String | Grafana | 网站服务 |
| results[].risk count _ | Integer | 100 | 安全漏洞数量 |

| results[].compliance ri _ sk count _ | Integer | 100 | 合规漏洞数量 |
|---|---|---|---|
| results[].title | String | this is a title | 网站标题 |
| results[].custom title _ | String |  | 自定义标题 |
| results[].remark | String | this is a reremark | 备注 |
| results[].waf | Boolean | true | waf |
| results[].finger print _ | Array | [{}] | 指纹 |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | 资产标签 |
| results[].asset tags[].t _ ag id _ | Integer | 11 | 资产标签ID |
| results[].asset tags[].t _ ag name _ | String | EIP | 标签名 |
| results[].staff | Object | {} | 负责人信息 |
| results[].asset source _ | String | System Discovered | 资产来源 |
| results[].screenshot | String |  | 网站截图 |
| results[].status code _ | Integer | 200 | 网站状态码 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].scan tm _ | Integer | 1774428275 | 扫描时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeWebsiteAssetList&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "website_type": [
    "IP",
    "DOMAIN"
```

`],`

```json
  "is_alive": true,
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "fingerprints": [
    "PHP",
    "Apache"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_waf": true,
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "status_codes": [
    403,
```

`],`

```json
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "this is a group name",
      "asset_type": "IP",
      "website_type": "DOMAIN",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "service": "Grafana",
      "risk_count": 100,
      "compliance_risk_count": 100,
      "title": "this is a title",
      "custom_title": "",
      "remark": "this is a reremark",
      "waf": true,
      "finger_print": [
        {}
```

`],`

```json
      "asset_tags": [
        {
          "tag_id": 11,
          "tag_name": "EIP"
        }
```

`],`

```json
      "staff": {},
      "asset_source": "System Discovered",
      "screenshot": "",
      "status_code": 200,
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>this is a group name</group_name>
            <asset_type>IP</asset_type>
            <website_type>DOMAIN</website_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <service>Grafana</service>
            <risk_count>100</risk_count>
            <compliance_risk_count>100</compliance_risk_count>
            <title>this is a title</title>
            <custom_title></custom_title>
            <remark>this is a reremark</remark>
            <waf>true</waf>
            <finger_print>
                <item></item>
            </finger_print>
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <asset_source>System Discovered</asset_source>
            <screenshot></screenshot>
            <status_code>200</status_code>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 域名资产

##### DescribeDomainAssetList

获取域名资产列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeDomainAssetL ist | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | vpc- l0miygn8aj17 1l8115eg1 | VPC ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 资产负责人ID |
| tag ids _ | String | body | 否 | [11, 22] | 资产标签ID |
| is alive _ | Boolean | body | 否 | true | 是否存活 |
| parse status _ | String | body | 否 | ["FAILED", "SUCCESS"] | 域名解析状态 FAILED:解析失败 SUCCESS:解析成功 |

| asset source _ | String | body | 否 | ["AUTO", "MANUAL"] | 资产来源 MANUAL:手工导入 AUTO: 自动导入 |
|---|---|---|---|---|---|
| changings | String | body | 否 | ["NEW", "UPDATED"] | 资产变动 NEW:新上线 UPDATED:有更新 SAME:无更新 OFFLINE:已下线 |
| insert tm en _ _ d | String | body | 否 | 2024-02-04 00:00:00 | 资产导入时间-止 |
| insert tm sta _ _ rt | String | body | 否 | 2024-01-04 00:00:00 | 资产导入时间-起 |
| is cdn _ | Boolean | body | 否 | true | 是否存在cdn识别 |
| is wildcard _ | Boolean | body | 否 | true | 是否是泛解析 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 20 | 每页返回数量 |
| risk levels _ | String | body | 否 | ["HIGH", "MIDDLE"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 HEALTH:安全 |
| search | String | body | 否 | baidu.com | 搜索内容 |
| update tm e _ _ nd | String | body | 否 | 2024-02-04 00:00:00 | 资产更新时间-止 |
| update tm st _ _ art | String | body | 否 | 2024-01-04 00:00:00 | 资产更新时间-起 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].vpc id _ | String | vpc- l0miygn8aj171l8115eg 1 | VPC ID |
| results[].asset id _ | Integer | 123 | 资产ID |
| results[].group id _ | Integer | 1 | 分组ID |
| results[].asset name _ | String | 192.168.100.100 | 资产名 |
| results[].group name _ | String | this is a group name | 分组名称 |
| results[].asset type _ | String | IP | 资产类型 |
| results[].status | String | OK | 状态 |
| results[].risk level _ | String | HIGH | 风险等级 |
| results[].changing | String | NEW | 资产改变类型 |
| results[].is alive _ | Integer | 1 | 存活状态 |
| results[].hostname | String | 192.168.100.100 | 主机名 |
| results[].remark | String | this is a reremark | 备注 |
| results[].parsed | String |  | 解析状态 |

| results[].parse err _ | String | this is a fail reason for domain resolution | 解析失败原因 |
|---|---|---|---|
| results[].cdn | String | 阿里云 | CDN识别 |
| results[].asset tags _ | Array | [{"tag id": 11, _ "tag name": "EIP"}] _ | 资产标签 |
| results[].asset tags[].t _ ag id _ | Integer | 11 | 资产标签ID |
| results[].asset tags[].t _ ag name _ | String | EIP | 标签名 |
| results[].staff | Object | {} | 负责人信息 |
| results[].domain parse _ d | Array | [{"id": 123, "ip": "192.168.131.100", "insert tm": _ 1774428275, "update tm": _ 1774428275}] | 域名解析记录 |
| results[].domain parse _ d[].id | Integer | 123 | 资产ID |
| results[].domain parse _ d[].ip | String | 192.168.131.100 | IP |
| results[].domain parse _ d[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].domain parse _ d[].update tm _ | Integer | 1774428275 | 更新时间 |
| results[].parsed histor _ y | Array | [{"id": 123, "ip": "192.168.131.100", "insert tm": _ 1774428275, "update tm": _ 1774428275}] | 域名解析历史记录 |
| results[].parsed histor _ y[].id | Integer | 123 | 资产ID |

| results[].parsed histor _ y[].ip | String | 192.168.131.100 | IP |
|---|---|---|---|
| results[].parsed histor _ y[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].parsed histor _ y[].update tm _ | Integer | 1774428275 | 更新时间 |
| results[].asset source _ | String | System Discovered | 资产来源 |
| results[].pan domain _ | Integer | 1 | 是否泛解析 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].scan tm _ | Integer | 1774428275 | 扫描时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeDomainAssetList&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "vpc-l0miygn8aj171l8115eg1",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
    11,
```

`],`

```json
  "is_alive": true,
  "parse_status": [
    "FAILED",
    "SUCCESS"
```

`],`

```json
  "asset_source": [
    "AUTO",
    "MANUAL"
```

`],`

```json
  "changings": [
    "NEW",
    "UPDATED"
```

`],`

```json
  "insert_tm_end": "2024-02-04 00:00:00",
  "insert_tm_start": "2024-01-04 00:00:00",
  "is_cdn": true,
  "is_wildcard": true,
  "page": 1,
  "page_size": 20,
  "risk_levels": [
    "HIGH",
    "MIDDLE"
```

`],`

```json
  "search": "",
  "update_tm_end": "2024-02-04 00:00:00",
  "update_tm_start": "2024-01-04 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
```

```json
  "count": 10,
  "results": [
    {
      "vpc_id": "vpc-l0miygn8aj171l8115eg1",
      "asset_id": 123,
      "group_id": 1,
      "asset_name": "192.168.100.100",
      "group_name": "this is a group name",
      "asset_type": "IP",
      "status": "OK",
      "risk_level": "HIGH",
      "changing": "NEW",
      "is_alive": 1,
      "hostname": "192.168.100.100",
      "remark": "this is a reremark",
      "parsed": "",
      "parse_err": "this is a fail reason for domain resolution",
```

`"cdn": "`阿里云`",`

```json
      "asset_tags": [
        {
          "tag_id": 11,
          "tag_name": "EIP"
        }
```

`],`

```json
      "staff": {},
      "domain_parsed": [
        {
          "id": 123,
          "ip": "192.168.131.100",
          "insert_tm": 1774428275,
          "update_tm": 1774428275
        }
```

`],`

```json
      "parsed_history": [
        {
          "id": 123,
          "ip": "192.168.131.100",
          "insert_tm": 1774428275,
          "update_tm": 1774428275
        }
```

`],`

```json
      "asset_source": "System Discovered",
      "pan_domain": 1,
      "insert_tm": 1774428275,
      "scan_tm": 1774428275,
      "update_tm": 1774428275
    }
```

]

```
}
```

`XML` 格式

```
HTTP/1.1 200 OK Content-Type:application/xml
```

```xml
Cotet ype:app cato/
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <count>10</count>
    <results>
        <item>
            <vpc_id>vpc-l0miygn8aj171l8115eg1</vpc_id>
            <asset_id>123</asset_id>
            <group_id>1</group_id>
            <asset_name>192.168.100.100</asset_name>
            <group_name>this is a group name</group_name>
            <asset_type>IP</asset_type>
            <status>OK</status>
            <risk_level>HIGH</risk_level>
            <changing>NEW</changing>
            <is_alive>1</is_alive>
            <hostname>192.168.100.100</hostname>
            <remark>this is a reremark</remark>
            <parsed></parsed>
            <parse_err>this is a fail reason for domain resolution</parse_err>
```

`<cdn>`阿里云`</cdn>`

```xml
            <asset_tags>
                <item>
                    <tag_id>11</tag_id>
                    <tag_name>EIP</tag_name>
                </item>
            </asset_tags>
            <staff></staff>
            <domain_parsed>
                <item>
                    <id>123</id>
                    <ip>192.168.131.100</ip>
                    <insert_tm>1774428275</insert_tm>
                    <update_tm>1774428275</update_tm>
                </item>
            </domain_parsed>
            <parsed_history>
                <item>
                    <id>123</id>
                    <ip>192.168.131.100</ip>
                    <insert_tm>1774428275</insert_tm>
                    <update_tm>1774428275</update_tm>
                </item>
            </parsed_history>
            <asset_source>System Discovered</asset_source>
            <pan_domain>1</pan_domain>
            <insert_tm>1774428275</insert_tm>
            <scan_tm>1774428275</scan_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### DeleteAsset

删除资产

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:DeleteAsset | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| add white _ | Integer | body | 否 | 1 | 是否加白 |
| ids | String | body | 否 | [123, 456] | 资产ID列表 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DeleteAsset&RegionId=cn-hangzhou Content-Type: application/json {
  "add_white": 1,
  "ids": [
    123,
```

]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

### 任务相关接口

#### 资产导入任务

##### CreateAssetImportTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:CreateAssetImportTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | vpc 1 _ | VPC ID |
| template id _ | Integer | body | 否 | 1 | 模版ID |
| group id _ | Integer | body | 否 | 0为默认分组 | 资产分组ID |
| staff id _ | Integer | body | 否 | 1 | 负责人ID |
| tag ids _ | String | body | 否 | [1, 2, 3] | 标签ID列表 |
| task name _ | String | body | 是 | 风险扫描任务- 测试 | 任务名 |
| network type _ | Integer | body | 否 | 1 | 网络类型 1公网 2 私网 |
| is immediatel _ y | Integer | body | 否 | 1 | 是否立即执行 |
| is public asse _ _ t | Integer | body | 否 | 1 | 是否公网资产 |

| asset metada _ tas | String | body | 否 | [{"hostName" : "xxlsk", "ip": "1.1.1.1", "instanceId": "xxx ss", _ "instanceNam e": "xxx ss", _ "osType": "linux"}] | 资产元数据列表 |
|---|---|---|---|---|---|
| not alive rep _ _ ort | Integer | body | 否 | 1 | 是否上报非存活资产 1 上报 0 不上报 |
| screen shot _ | Integer | body | 否 | 1 | 是否开启网站截图 1 开启 0 关闭 |
| start tm _ | String | body | 否 | 2020-01-01 00:00:00 | 开始时间 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| task instance id _ _ | Integer | 1 | 任务实例ID |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=CreateAssetImportTask&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "1",
  "template_id": 1,
  "group_id": 0,
  "staff_id": 1,
  "tag_ids": [
```

`1,` `2,` `],` `"task_name": "`风险扫描任务-测试`",`

```json
  "network_type": 1,
  "is_immediately": 1,
  "is_public_asset": 1,
  "asset_metadatas": [
    {
      "hostName": "xxlsk",
      "ip": "1.1.1.1",
      "instanceId": "xxx_ss",
      "instanceName": "xxx_ss",
      "osType": "linux"
    }
```

`],`

```json
  "not_alive_report": 1,
  "screen_shot": 1,
  "start_tm": "2020-01-01 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_instance_id": 1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_instance_id>1</task_instance_id>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

##### DescribeAssetImportTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeAssetImportTa sk | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | body | 否 | 1 | 任务实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| vpc id _ | String | 1 | VPC ID |
| id | Integer | 1 | 任务ID |

| task instance id _ _ | Integer | 1 | 任务实例ID |
|---|---|---|---|
| template id _ | Integer | 1 | 任务模板ID |
| task name _ | String | 资产扫描任务-测试 | 任务名 |
| template name _ | String | 资产扫描模板-测试 | 任务模板名 |
| import mode _ | String | MANUAL IMPORT _ | 导入方式 MANUAL IMPORT 手动导入 _ |
| network type _ | Integer | 1 | 网络类型 1 公网 2 私网 |
| status | String | INIT | 运行状态 INIT 初始化 |
| is immediately _ | Integer | 1 | 是否立即执行 1 是 0 否 |
| is public asset _ _ | Integer | 1 | 是否公网资产导入 1 是 0 否 |
| cycle count _ | Integer | 10 | 任务周期 |
| import count _ | Object | {} | 导入数量 |
| not alive report _ _ | Integer | 1 | 是否上报非存活资产 1 上报 0 不上报 |
| screen shot _ | Integer | 1 | 是否开启网站截图 1 开启 0 关闭 |
| finish time _ | Integer | 1774428275 | 结束时间 |

| insert tm _ | Integer | 1774428275 | 插入时间 |
|---|---|---|---|
| start time _ | Integer | 1774428275 | 开始时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeAssetImportTask&RegionId=cn-hangzhou Content-Type: application/json {
  "task_instance_id": 1
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "vpc_id": "1",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
```

`"task_name": "`资产扫描任务-测试`",` `"template_name": "`资产扫描模板-测试`",`

```json
  "import_mode": "MANUAL_IMPORT",
  "network_type": 1,
  "status": "INIT",
  "is_immediately": 1,
  "is_public_asset": 1,
  "cycle_count": 10,
  "import_count": {},
  "not_alive_report": 1,
  "screen_shot": 1,
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_time": 1774428275
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <vpc_id>1</vpc_id>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<template_name>`资产扫描模板-测试`</template_name>`

```xml
    <import_mode>MANUAL_IMPORT</import_mode>
    <network_type>1</network_type>
    <status>INIT</status>
    <is_immediately>1</is_immediately>
    <is_public_asset>1</is_public_asset>
    <cycle_count>10</cycle_count>
    <import_count></import_count>
    <not_alive_report>1</not_alive_report>
    <screen_shot>1</screen_shot>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_time>1774428275</start_time>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

##### DescribeAssetImportTaskResult

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeAssetImportTa skResult | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | body | 否 | 1 | 任务实例ID |
| asset type _ | String | body | 否 | IP | 资产类型 IP WEBSITE DOMAIN |
| is new _ | Integer | body | 否 | 1 | 是否新上线 1 是 0 否 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页面数量 |
| search | String | body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 100 | 分页数据条数 |
| results | Array |  | 结果集 |
| results[].id | Integer | 1 | ID |
| results[].task instance _ id _ | Integer | 1 | 任务实例ID |

| results[].asset name _ | String | 1.1.1.1 | 资产名 |
|---|---|---|---|
| results[].is new _ | Integer | 1 | 是否新发现 1 是 0 否 |
| results[].is deleted _ | Boolean | false | 是否已删除 1 是 0 否 |
| results[].asset source _ | String | 主机导入 | 资产源 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeAssetImportTaskResult&RegionId=cn-hangzhou Content-Type: application/json {
  "task_instance_id": 1,
  "asset_type": "IP",
  "is_new": 1,
  "page": 1,
  "page_size": 10,
  "search": "1_1_1_1_1"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 100,
  "results": [
    {
      "id": 1,
      "task_instance_id": 1,
      "asset_name": "1.1.1.1",
      "is_new": 1,
      "is_deleted": false,
```

`"asset_source": "`主机导入`",`

```json
      "insert_tm": 1774428275
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
    <count>100</count>
    <results>
        <item>
            <id>1</id>
            <task_instance_id>1</task_instance_id>
            <asset_name>1.1.1.1</asset_name>
            <is_new>1</is_new>
            <is_deleted>false</is_deleted>
            <asset_source>主机导入</asset_source>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 资产扫描任务

##### CreateAssetScanTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:CreateAssetScanTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | 1 | VPC ID |
| template id _ | Integer | body | 否 | 1 | 模版ID |
| task name _ | String | body | 是 | 风险扫描任务- 测试 | 任务名 |
| targets | String | body | 否 |  | 检测目标 ALL IP: 0/1 ALL WEBSITE: _ _ 0/1 ALL ASSET: 0/1 _ ALL DOMAIN: 0/1 GROUP: _ [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] DOMAIN: [1,2,3] |
| screen shot _ | Integer | body | 否 | 1 | 是否开启网站截图 1 开启 0 关闭 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| task id _ | Integer | 1 |  |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=CreateAssetScanTask&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "1",
  "template_id": 1,
```

`"task_name": "`风险扫描任务-测试`",`

```json
  "targets": "",
  "screen_shot": 1
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_id": 1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_id>1</task_id>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

| 500 | 101 | 服务端透传 | 服务端透传 |
|---|---|---|---|

##### DescribeAssetScanTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeAssetScanTas k | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | body | 否 | 1 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| id | Integer | 1 | ID |
| task instance id _ _ | Integer | 1 | 任务实例ID |
| template id _ | Integer | 1 | 任务模板ID |

| name | String | xx资产扫描 | 名称 |
|---|---|---|---|
| template name _ | String | xx资产扫描模板 | 任务模板名 |
| status | String | RUNNING | 运行状态 INIT 初始化 |
| targets | Array | [{"type": "ALL", "target": [""]}] | 目标 |
| targets[].type | String | ALL | 类型 |
| targets[].target | Array | [""] | 目标 |
| cycle count _ | Integer | 10 | 循环次数 |
| import count _ | Object | {} | 导入数量 |
| finish time _ | Integer | 1774428275 | 结束时间 |
| insert tm _ | Integer | 1774428275 | 插入时间 |
| start tm _ | Integer | 1774428275 | 开始时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeAssetScanTask&RegionId=cn-hangzhou Content-Type: application/json {
  "id": 1
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
```

`"name": "xx`资产扫描`",` `"template_name": "xx`资产扫描模板`",`

```json
  "status": "RUNNING",
  "targets": [
    {
      "type": "ALL",
      "target": [
```

`""` ]

```
    }
```

`],`

```json
  "cycle_count": 10,
  "import_count": {},
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_tm": 1774428275
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<name>xx`资产扫描`</name>` `<template_name>xx`资产扫描模板`</template_name>`

```xml
    <status>RUNNING</status>
    <targets>
        <item>
            <type>ALL</type>
            <target>
                <item></item>
            </target>
        </item>
    </targets>
    <cycle_count>10</cycle_count>
    <import_count></import_count>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_tm>1774428275</start_tm>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 风险扫描任务

##### CreateRiskScanTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:CreateRiskScanTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| template id _ | Integer | body | 否 | 1 | 模版ID |
| vpc ids _ | String | body | 否 | ["vpc 1", _ "vpc 2"] _ | VPC ID |
| task name _ | String | body | 是 | 风险扫描任务-测试 | 任务名 |
| targets | String | body | 否 |  | 检测目标 ALL IP: 0/1 _ ALL WEBSITE: 0/1 _ ALL ASSET: 0/1 _ GROUP: [1,2,3] IP: [1,2,3] WEBSITE: [1,2,3] |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| task id _ | Integer | 1 |  |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=CreateRiskScanTask&RegionId=cn-hangzhou Content-Type: application/json {
  "template_id": 1,
  "vpc_ids": [
    "vpc_1",
    "vpc_2"
```

`],` `"task_name": "`风险扫描任务-测试`",`

```json
  "targets": ""
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "task_id": 1
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <task_id>1</task_id>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

##### DescribeRiskScanTask

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|

| yundun- scanner:DescribeRiskScanTask | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | body | 否 | 1 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| id | Integer | 1 | ID |
| task instance id _ _ | Integer | 1 | 任务实例ID |
| template id _ | Integer | 1 | 任务模板ID |
| name | String | xx风险扫描 | 名称 |
| template name _ | String | xx风险扫描模板 | 任务模板名 |
| status | String | RUNNING | 运行状态 INIT 初始化 |
| targets | Array | [{"type": "ALL", "target": [""]}] | 目标 |
| targets[].type | String | ALL | 类型 |

| targets[].target | Array | [""] | 目标 |
|---|---|---|---|
| cycle count _ | Integer | 10 | 循环次数 |
| finish time _ | Integer | 1774428275 | 结束时间 |
| insert tm _ | Integer | 1774428275 | 插入时间 |
| start tm _ | Integer | 1774428275 | 开始时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeRiskScanTask&RegionId=cn-hangzhou Content-Type: application/json {
  "id": 1
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "id": 1,
  "task_instance_id": 1,
  "template_id": 1,
```

`"name": "xx`风险扫描`",` `"template_name": "xx`风险扫描模板`",`

```json
  "status": "RUNNING",
  "targets": [
    {
      "type": "ALL",
      "target": [
```

`""` ]

```
    }
```

`],`

```json
  "cycle_count": 10,
  "finish_time": 1774428275,
  "insert_tm": 1774428275,
  "start_tm": 1774428275
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <id>1</id>
    <task_instance_id>1</task_instance_id>
    <template_id>1</template_id>
```

`<name>xx`风险扫描`</name>` `<template_name>xx`风险扫描模板`</template_name>`

```xml
    <status>RUNNING</status>
    <targets>
        <item>
            <type>ALL</type>
            <target>
                <item></item>
            </target>
        </item>
    </targets>
    <cycle_count>10</cycle_count>
    <finish_time>1774428275</finish_time>
    <insert_tm>1774428275</insert_tm>
    <start_tm>1774428275</start_tm>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

##### DescribeRiskScanTaskResult

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeRiskScanTask Result | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task instance _ id _ | Integer | body | 否 | 1 | 任务实例ID |
| risk type _ | Integer | body | 否 | 2 | 风险类型 2 安全漏洞 3 合规漏洞 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页面数量 |
| search | String | body | 否 | 1 1 1 1 1 _ _ _ _ | 搜索框 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 100 | 总数 |
| results | Array |  | 结果 |
| results[].risk id _ | Integer | 1 | 风险ID |
| results[].risk name _ | String | xxx安全漏洞 | 风险名称 |
| results[].risk type _ | Integer | 3 | 风险类型 2 安全漏洞 3 合规漏洞 |

| results[].risk level _ | String | LOW | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 |
|---|---|---|---|
| results[].risk addr _ | String | http://1.1.1.1 | 风险地址 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeRiskScanTaskResult&RegionId=cn-hangzhou Content-Type: application/json {
  "task_instance_id": 1,
  "risk_type": 2,
  "page": 1,
  "page_size": 10,
  "search": "1_1_1_1_1"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 100,
  "results": [
    {
      "risk_id": 1,
```

`"risk_name": "xxx`安全漏洞`",`

```json
      "risk_type": 3,
      "risk_level": "LOW",
      "risk_addr": "http://1.1.1.1",
      "insert_tm": 1774428275
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
    <count>100</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <risk_name>xxx安全漏洞</risk_name>
            <risk_type>3</risk_type>
            <risk_level>LOW</risk_level>
            <risk_addr>http://1.1.1.1</risk_addr>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### DescribeTaskList

获取任务列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeTaskList | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| template id _ | Integer | body | 否 | 1 | 模版ID |
|---|---|---|---|---|---|
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页大小 |
| run types _ | String | body | 否 | cycle | 运行方式 cycle 周期执行 once 指定时间执行一次 immediately 立即执行 |
| search | String | body | 否 | 1 1 1 1 _ _ _ _ 1 | 搜索内容，支持： 任务ID 任务名称资产地址 |
| statuses | String | body | 否 | ["RUNNIN G", "INIT", "FINISH", "STOP"] | 任务状态 RUNNING 运行中 INIT 初始化 FINISH 任务完成 STOP 任务停止 |
| task types _ | String | body | 否 | ["assetIm port", "assetRis k", "assetSca n"] | 任务类型 assetImport 资产导入任务 assetScan 资产扫描任务 assetRIsk 风险扫描任务 |
| end time _ | String | body | 否 | 2020-01- 01 00:00:00 | 结束时间 |
| start time _ | String | body | 否 | 2020-01- 01 00:00:00 | 开始时间 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
|---|---|---|---|
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].id | Integer | 1 | ID |
| results[].task instance _ id _ | Integer | 123 | 任务实例ID |
| results[].task name _ | String | 资产扫描任务-测试 | 任务名 |
| results[].task type _ | Integer | 6 | 任务类型 |
| results[].status | String | INIT | 任务状态 RUNNING 运行中 INIT 初始化 FINISH 任务完成 STOP 任务停止 |
| results[].is immediatel _ y | Integer | 1 | 是否立即执行 1 是 0 否 |
| results[].is public asse _ _ t | Integer | 1 | 是否公网资产 1 是 0 否 |
| results[].cycle count _ | Integer | 10 | 周期次数 |
| results[].task cycle _ | Integer | 0 | 任务周期 |
| results[].start time _ | Integer | 1774428275 | 创建时间 |
| results[].end time _ | Integer | 1774428275 | 结束时间 |

| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
|---|---|---|---|

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeTaskList&RegionId=cn-hangzhou Content-Type: application/json {
  "template_id": 1,
  "page": 1,
  "page_size": 10,
  "run_types": "cycle",
  "search": "1_1_1_1_1",
  "statuses": [
    "RUNNING",
    "INIT",
    "FINISH",
    "STOP"
```

`],`

```json
  "task_types": [
    "assetImport",
    "assetRisk",
    "assetScan"
```

`],`

```json
  "end_time": "2020-01-01 00:00:00",
  "start_time": "2020-01-01 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "id": 1,
      "task_instance_id": 123,
```

`"task_name": "`资产扫描任务-测试`",`

```json
      "task_type": 6,
      "status": "INIT",
      "is_immediately": 1,
      "is_public_asset": 1,
      "cycle_count": 10,
      "task_cycle": 0,
      "start_time": 1774428275,
      "end_time": 1774428275,
      "insert_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <id>1</id>
            <task_instance_id>123</task_instance_id>
            <task_type>6</task_type>
            <status>INIT</status>
            <is_immediately>1</is_immediately>
            <is_public_asset>1</is_public_asset>
            <cycle_count>10</cycle_count>
            <task_cycle>0</task_cycle>
            <start_time>1774428275</start_time>
            <end_time>1774428275</end_time>
            <insert_tm>1774428275</insert_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### StartTask

开始任务

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:StartTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task ids _ | String | body | 否 | [1, 2, 3] | 任务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| data | Array | [{"task instance id": _ _ 208, "task id": 173}] _ |  |
| data[].task instance id _ _ | Integer | 208 | 任务实例ID |

| data[].task id _ | Integer | 173 | 任务ID |
|---|---|---|---|

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=StartTask&RegionId=cn-hangzhou Content-Type: application/json {
  "task_ids": [
```

`1,` `2,` ]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "data": [
    {
      "task_instance_id": 208,
      "task_id": 173
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
    <data>
        <item>
            <task_instance_id>208</task_instance_id>
            <task_id>173</task_id>
        </item>
    </data>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### StopTask

停止任务

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:StopTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task ids _ | String | body | 否 | [1, 2, 3] | 任务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| status | String | OK | 成功状态 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=StopTask&RegionId=cn-hangzhou Content-Type: application/json {
  "task_ids": [
```

`1,` `2,` ]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### SuspendTask

暂停任务

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|

| yundun-scanner:SuspendTask | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| task ids _ | String | body | 否 | [1, 2, 3] | 任务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| status | String | OK | 成功状态 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=SuspendTask&RegionId=cn-hangzhou Content-Type: application/json {
  "task_ids": [
```

`1,` `2,` ]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### DeleteTask

删除任务

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:DeleteTask | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| task ids _ | String | body | 否 | [1, 2, 3] | 任务ID |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| status | String | OK | 成功状态 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DeleteTask&RegionId=cn-hangzhou Content-Type: application/json {
  "task_ids": [
```

`1,` `2,` ]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "status": "OK"
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status>OK</status>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

### 风险相关接口

#### 安全漏洞

##### DescribeRiskList

获取安全漏洞列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:DescribeRiskList | undefined | acs:yundun-scanner:: {#accountId}: |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | public network _ _ asset | VPC ID |
| asset id _ | Integer | body | 否 | 1 | 资产ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 负责人ID |

| tag ids _ | String | body | 否 | [1, 2] | 标签ID |
|---|---|---|---|---|---|
| status | String | body | 否 | REPAIRED | 处理状态 REPAIRED:已修复 UNREPAIRED:未修复 |
| detect status _ | String | body | 否 | ["SUCCESS", "FAILED", "DETECTING"] | 检测状态 SUCCESS:检测成功 FAILED:检测失败 DETECTING:检测中 |
| source | String | body | 否 | ["1", "2"] | 风险来源 |
| insert tm end _ _ | String | body | 否 | 2021-01-04 00:00:00 | 发现结束时间 |
| insert tm start _ _ | String | body | 否 | 2021-01-04 00:00:00 | 发现时间 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页面数量 |
| process | String | body | 否 | ["NEW", "CONFIRMED", "IGNORED"] | 进度 NEW:未确认 CONFIRMED:已确认 IGNORED: 已忽略 |
| risk levels _ | String | body | 否 | ["LOW", "MIDDLE", "HIGH"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 |
| search | String | body | 否 | CVE-2021- 44228 | 搜索框 |
| update tm end _ _ | String | body | 否 | 2021-01-04 00:00:00 | 更新结束时间 |
| update tm start _ _ | String | body | 否 | 2021-01-04 00:00:00 | 更新时间 |

| vuln types _ | String | body | 否 | [1, 2] | 漏洞类型 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].risk id _ | Integer | 1 | 风险ID |
| results[].asset id _ | Integer | 1 | 资产ID |
| results[].vuln id _ | Integer | 1 | 漏洞ID |
| results[].risk name _ | String | foo | 风险名称 |
| results[].vuln type _ | String | XSS漏洞 | 漏洞类型 |
| results[].general type _ | String | web vuln _ | 风险类型 |
| results[].risk level _ | String | HIGH | 风险等级 |
| results[].risk status _ | String | SUCCESS | 风险状态 |
| results[].detect status _ | String | SUCCESS | 检测状态 |
| results[].risk process _ | String | NEW | 风险进度 |
| results[].source | String | AUTO | 风险来源 |
| results[].risk addr _ | String | 192.168.0.1:3306 | 风险地址 |

| results[].ip | String | 192.168.0.1 | IP |
|---|---|---|---|
| results[].related doma _ in | String | www.foo.com | 关联域名 |
| results[].fail reason _ | String | xxx | 失败原因 |
| results[].ignore comm _ ent | String | xxx | 忽略备注 |
| results[].risk sn _ | String | 2020-1-1- V100000000000 | 漏洞编号 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].last detect t _ _ m | Integer | 1774428275 | 最后检测时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeRiskList&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "public_network_asset",
  "asset_id": 1,
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
    "FAILED",
    "DETECTING"
```

`],`

```json
  "source": [
    "1",
    "2"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
  "update_tm_start": "2021-01-04 00:00:00",
  "vuln_types": [
```

`1,` ]

```
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "risk_id": 1,
      "asset_id": 1,
      "vuln_id": 1,
      "risk_name": "foo",
      "vuln_type": "XSS漏洞",
      "general_type": "web_vuln",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "source": "AUTO",
      "risk_addr": "192.168.0.1:3306",
      "ip": "192.168.0.1",
      "related_domain": "www.foo.com",
      "fail_reason": "xxx",
      "ignore_comment": "xxx",
      "risk_sn": "2020-1-1-V100000000000",
      "insert_tm": 1774428275,
      "last_detect_tm": 1774428275,
      "update_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <vuln_id>1</vuln_id>
            <risk_name>foo</risk_name>
            <vuln_type>XSS漏洞</vuln_type>
            <general_type>web_vuln</general_type>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <source>AUTO</source>
            <risk_addr>192.168.0.1:3306</risk_addr>
            <ip>192.168.0.1</ip>
            <related_domain>www.foo.com</related_domain>
            <fail_reason>xxx</fail_reason>
            <ignore_comment>xxx</ignore_comment>
            <risk_sn>2020-1-1-V100000000000</risk_sn>
            <insert_tm>1774428275</insert_tm>
            <last_detect_tm>1774428275</last_detect_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 对外暴露

##### DescribeBaselineRiskList

获取对外暴露列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|

| yundun- scanner:DescribeBaselineRiskLi st | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | public networ _ k asset _ | VPC ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 负责人ID |
| tag ids _ | String | body | 否 | [1, 2] | 标签ID |
| status | String | body | 否 | REPAIRED | 处理状态 REPAIRED:已修复 UNREPAIRED:未修复 |
| detect status _ | String | body | 否 | ["SUCCESS", "FAILED", "DETECTING"] | 检测状态 SUCCESS:检测成功 FAILED: 检测失败 DETECTING:检测中 |
| insert tm end _ _ | String | body | 否 | 2021-01-04 00:00:00 | 发现结束时间 |
| insert tm star _ _ t | String | body | 否 | 2021-01-04 00:00:00 | 发现时间 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页面数量 |

| process | String | body | 否 | ["NEW", "CONFIRMED", "IGNORED"] | 进度 NEW:未确认 CONFIRMED: 已确认 IGNORED:已忽略 |
|---|---|---|---|---|---|
| risk levels _ | String | body | 否 | ["LOW", "MIDDLE", "HIGH"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 |
| search | String | body | 否 | CVE-2021- 44228 | 搜索框 |
| update tm en _ _ d | String | body | 否 | 2021-01-04 00:00:00 | 更新结束时间 |
| update tm st _ _ art | String | body | 否 | 2021-01-04 00:00:00 | 更新时间 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].risk id _ | Integer | 1 | 风险ID |
| results[].asset id _ | Integer | 1 | 资产ID |
| results[].rule id _ | Integer | 1 | 规则ID |
| results[].risk name _ | String | foo | 风险名称 |
| results[].risk level _ | String | HIGH | 风险等级 |

| results[].risk status _ | String | SUCCESS | 风险状态 |
|---|---|---|---|
| results[].detect status _ | String | SUCCESS | 检测状态 |
| results[].risk process _ | String | NEW | 进度 |
| results[].risk addr _ | String | 192.168.0.1:443 | 风险地址 |
| results[].ip | String | 192.168.0.1 | IP |
| results[].related doma _ in | String | www.foo.com | 关联域名 |
| results[].ignore comm _ ent | String | xxx | 忽略备注 |
| results[].risk sn _ | String | 2020-1-1- V100000000000 | 风险编号 |
| results[].vuln addr _ | String | 192.168.0.1:443 | 漏洞地址 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```json
POST https://[Endpoint]/?Action=DescribeBaselineRiskList&RegionId=cn-hangzhou Content-Type: application/json {
  "vpc_id": "public_network_asset",
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
    "FAILED",
    "DETECTING"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
  "update_tm_start": "2021-01-04 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "risk_id": 1,
      "asset_id": 1,
      "rule_id": 1,
      "risk_name": "foo",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "risk_addr": "192.168.0.1:443",
      "ip": "192.168.0.1",
      "related_domain": "www.foo.com",
      "ignore_comment": "xxx",
      "risk_sn": "2020-1-1-V100000000000",
      "vuln_addr": "192.168.0.1:443",
      "insert_tm": 1774428275,
      "update_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <rule_id>1</rule_id>
            <risk_name>foo</risk_name>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <risk_addr>192.168.0.1:443</risk_addr>
            <ip>192.168.0.1</ip>
            <related_domain>www.foo.com</related_domain>
            <ignore_comment>xxx</ignore_comment>
            <risk_sn>2020-1-1-V100000000000</risk_sn>
            <vuln_addr>192.168.0.1:443</vuln_addr>
            <insert_tm>1774428275</insert_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

#### 合规漏洞

##### DescribeComplianceRiskList

获取合规漏洞列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|

| yundun- scanner:DescribeComplianceRis kList | undefined | acs:yundun-scanner:: {#accountId}: |
|---|---|---|

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vpc id _ | String | body | 否 | public netwo _ rk asset _ | VPC ID |
| asset id _ | Integer | body | 否 | 1 | 资产ID |
| host asset id _ _ | Integer | body | 否 | 1 | 主机资产ID |
| group ids _ | String | body | 否 | [1, 2] | 资产分组ID |
| staff ids _ | String | body | 否 | [1, 2] | 负责人ID |
| tag ids _ | String | body | 否 | [1, 2] | 标签ID |
| status | String | body | 否 | REPAIRED | 处理状态 REPAIRED:已修复 UNREPAIRED:未修复 |
| detect status _ | String | body | 否 | ["SUCCESS", "FAILED", "DETECTING" ] | 检测状态 SUCCESS:检测成功 FAILED: 检测失败 DETECTING:检测中 |
| source | String | body | 否 | ["1", "2"] | 风险来源 |

| attack compl _ exity | String | body | 否 | HIGH | 攻击复杂度 HIGH:高 LOW:低 |
|---|---|---|---|---|---|
| privileges re _ quired | String | body | 否 | LOW | 权限要求 HIGH:高 LOW:低 NONE:无 |
| availability i _ mpact | String | body | 否 | HIGH | 可用性影响 HIGH:高 LOW:低 NONE:无 |
| exploitability | String | body | 否 | ["UNPROOFE D", "POC", "EXP"] | 可利用性 UNPROOFED:未证实 POC:存在 POC EXP:存在可利用代码 |
| insert tm en _ _ d | String | body | 否 | 2021-01-04 00:00:00 | 发现结束时间 |
| insert tm sta _ _ rt | String | body | 否 | 2021-01-04 00:00:00 | 发现时间 |
| page | Integer | body | 否 | 1 | 页码 |
| page size _ | Integer | body | 否 | 10 | 页面数量 |
| ports | String | body | 否 | [80, 443] | 端口 |
| process | String | body | 否 | ["NEW", "CONFIRMED ", "IGNORED"] | 进度 NEW:未确认 CONFIRMED: 已确认 IGNORED:已忽略 |
| risk levels _ | String | body | 否 | ["LOW", "MIDDLE", "HIGH"] | 风险等级 HIGH:高危 MIDDLE:中危 LOW:低危 |

| search | String | body | 否 | CVE-2021- 44228 | 搜索框 |
|---|---|---|---|---|---|
| update tm e _ _ nd | String | body | 否 | 2021-01-04 00:00:00 | 更新结束时间 |
| update tm st _ _ art | String | body | 否 | 2021-01-04 00:00:00 | 更新时间 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1- 97C8-************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题 |
| count | Integer | 10 | 总数 |
| results | Array |  | 结果 |
| results[].risk id _ | Integer | 1 | 风险ID |
| results[].asset id _ | Integer | 1 | 资产ID |
| results[].risk name _ | String | foo | 风险名称 |
| results[].risk level _ | String | HIGH | 风险等级 |
| results[].risk status _ | String | SUCCESS | 风险状态 |
| results[].detect status _ | String | SUCCESS | 检测状态 |
| results[].risk process _ | String | NEW | 风险进度 |
| results[].source | String | AUTO | 风险来源 |
| results[].asset addr _ | String | 192.168.0.1 | 资产地址 |

| results[].ip | String | 192.168.0.1 | IP |
|---|---|---|---|
| results[].port | String | 443 | 端口 |
| results[].service | String | nginx | 服务 |
| results[].related doma _ in | String | www.foo.com | 关联域名 |
| results[].cve | String | CVE-2021-44228 | CVE编号 |
| results[].avd | String | AVD-2021-44228 | AVD编号 |
| results[].cnvd | String | CNVD-2021-95914 | CNVD编号 |
| results[].cnnvd | String | CNNVD-202112-799 | CNNVD编号 |
| results[].attack compl _ exity | String | HIGH | 攻击复杂度 enum[HIGH, LOW] |
| results[].privileges req _ uired | String | LOW | 权限要求 enum[LOW, HIGH, NONE] |
| results[].availability i _ mpact | String | HIGH | 可用性影响 enum[HIGH, LOW，NONE] |
| results[].exploitability | Array | ["UNPROOFED", "POC", "EXP"] | 可利用性 array enum[UNPROOFED, POC, EXP] |
| results[].ignore comm _ ent | String | xxx | 忽略备注 |
| results[].insert tm _ | Integer | 1774428275 | 插入时间 |
| results[].update tm _ | Integer | 1774428275 | 更新时间 |

**示例**

请求示例

```
POST https://[Endpoint]/?Action=DescribeComplianceRiskList&RegionId=cn-hangzhou Content-Type: application/json
```

```json
{
  "vpc_id": "public_network_asset",
  "asset_id": 1,
  "host_asset_id": 1,
  "group_ids": [
```

`1,` `],`

```json
  "staff_ids": [
```

`1,` `],`

```json
  "tag_ids": [
```

`1,` `],`

```json
  "status": "REPAIRED",
  "detect_status": [
    "SUCCESS",
    "FAILED",
    "DETECTING"
```

`],`

```json
  "source": [
    "1",
    "2"
```

`],`

```json
  "attack_complexity": "HIGH",
  "privileges_required": "LOW",
  "availability_impact": "HIGH",
  "exploitability": [
    "UNPROOFED",
    "POC",
    "EXP"
```

`],`

```json
  "insert_tm_end": "2021-01-04 00:00:00",
  "insert_tm_start": "2021-01-04 00:00:00",
  "page": 1,
  "page_size": 10,
  "ports": [
    80,
```

`],`

```json
  "process": [
    "NEW",
    "CONFIRMED",
    "IGNORED"
```

`],`

```json
  "risk_levels": [
    "LOW",
    "MIDDLE",
    "HIGH"
```

`],`

```json
  "search": "CVE-2021-44228",
  "update_tm_end": "2021-01-04 00:00:00",
```

```json
  "update_tm_start": "2021-01-04 00:00:00"
}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "RequestId": "F0A8A039-930D-5EC1-97C8-************",
  "count": 10,
  "results": [
    {
      "risk_id": 1,
      "asset_id": 1,
      "risk_name": "foo",
      "risk_level": "HIGH",
      "risk_status": "SUCCESS",
      "detect_status": "SUCCESS",
      "risk_process": "NEW",
      "source": "AUTO",
      "asset_addr": "192.168.0.1",
      "ip": "192.168.0.1",
      "port": "443",
      "service": "nginx",
      "related_domain": "www.foo.com",
      "cve": "CVE-2021-44228",
      "avd": "AVD-2021-44228",
      "cnvd": "CNVD-2021-95914",
      "cnnvd": "CNNVD-202112-799",
      "attack_complexity": "HIGH",
      "privileges_required": "LOW",
      "availability_impact": "HIGH",
      "exploitability": [
        "UNPROOFED",
        "POC",
        "EXP"
```

`],`

```json
      "ignore_comment": "xxx",
      "insert_tm": 1774428275,
      "update_tm": 1774428275
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
    <count>10</count>
    <results>
        <item>
            <risk_id>1</risk_id>
            <asset_id>1</asset_id>
            <risk_name>foo</risk_name>
            <risk_level>HIGH</risk_level>
            <risk_status>SUCCESS</risk_status>
            <detect_status>SUCCESS</detect_status>
            <risk_process>NEW</risk_process>
            <source>AUTO</source>
            <asset_addr>192.168.0.1</asset_addr>
            <ip>192.168.0.1</ip>
            <port>443</port>
            <service>nginx</service>
            <related_domain>www.foo.com</related_domain>
            <cve>CVE-2021-44228</cve>
            <avd>AVD-2021-44228</avd>
            <cnvd>CNVD-2021-95914</cnvd>
            <cnnvd>CNNVD-202112-799</cnnvd>
            <attack_complexity>HIGH</attack_complexity>
            <privileges_required>LOW</privileges_required>
            <availability_impact>HIGH</availability_impact>
            <exploitability>
                <item>UNPROOFED</item>
                <item>POC</item>
                <item>EXP</item>
            </exploitability>
            <ignore_comment>xxx</ignore_comment>
            <insert_tm>1774428275</insert_tm>
            <update_tm>1774428275</update_tm>
        </item>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 101 | 服务端透传 | 服务端透传 |

## 安全审计

### GetData

获取审计日志列表

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun-scanner:GetData | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| company i _ d | Integ er | Body | 否 | 0 | 租户id。 |
| csv | Integ er | Body | 否 | 1 | 是否导出报表 enum[0:否｜ 1:是]。 |
| end | Strin g | Body | 否 | 1722478948 | 结束时间，发生事件区间-结束。 |
| module | Strin g | Body | 否 | OTHER | 所属模块。 |
| page | Integ er | Body | 否 | 1 | 页数。 |
| page size _ | Integ er | Body | 否 | 10 | 页面大小。 |
| search | Strin g | Body | 否 | 192.168.30.67 | 搜索框，支持用户名、IP、事件为条件搜索。 |

| start | Strin g | Body | 否 | 1722478944 | 开始时间，发生事件区间-开始。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| results | Array |  |  |
| -audit event _ | String | 导入资产 | 日志事件。 |
| -event attr _ | String | 【rp】导入 | 日志属性。 |
| -event result _ | String | SUCCESS | 事件结果 enum[SUCCESS\|FAILED]。 |
| -id | Integer | 1947 | 事件ID。 |
| -insert tm _ | Integer | 1722478948 | 审计时间。 |
| -login ip _ | String | 192.168.102.18 | 登录IP。 |
| - login usernam _ e | String | aliens | 登录用户名。 |
| -module | String | ASSET | 日志模块 enum[ASSET\|RISK\|REPORT\|CONFIG\|OTHER ]。 |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| count | Integer | 150 | 分页数据条数。 |
| path | String | http://oss.xxxx.xxx x/xxx/xx | 下载路径。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=GetData&RegionId=cnhangzhou&company_id=0&csv=1&end=1722478948&module=OTHER&page=1&page_size=10&search=192.16 30.67&start=1722478944
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "count":150,
    "path":"http://oss.xxxx.xxxx/xxx/xx",
    "results":[
        {
```

`"audit_event":"`导入资产`",` `"event_attr":"`【`rp`】导入`",`

```json
            "module":"ASSET",
            "login_username":"aliens",
            "event_result":"SUCCESS",
            "insert_tm":1722478948,
            "id":1947,
            "login_ip":"192.168.102.18"
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
    <count>150</count>
    <path>http://oss.xxxx.xxxx/xxx/xx</path>
    <results>
        <audit_event>导入资产</audit_event>
        <event_attr>【rp】导入</event_attr>
        <event_result>SUCCESS</event_result>
        <id>1947</id>
        <insert_tm>1722478948</insert_tm>
        <login_ip>192.168.102.18</login_ip>
        <login_username>aliens</login_username>
        <module>ASSET</module>
    </results>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |

### LouauditCleanData

清理审计日志

**授权信息**

| 操作 | 访问级别 | 资源类型 |
|---|---|---|
| yundun- scanner:LouauditCleanData | undefined | acs:yundun-scanner:*: {#accountId}:* |

**流量控制**

单用户调用频率：10QPS。 API调用频率：100QPS。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| keep time _ | Integ er | Body | 否 | 1722478948 | 保留时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| status | String |  | 成功状态。 |

**示例**

请求示例

```
https://[Endpoint]/?Action=LouauditCleanData&RegionId=cn-hangzhou&keep_time=1722478948
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "status":""
}
```

`XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <RequestId>F0A8A039-930D-5EC1-97C8-************</RequestId>
    <status></status>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 100 | MissingParameter1001API | Parameter 1001API is mandatory for this action. |
| 500 |  | InternalError | The request processing has failed due to some unknown error. |
