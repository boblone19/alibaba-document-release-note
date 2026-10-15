---
title: "数据库自治服务 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 58
source_pdf: "05_开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/hdm/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 数据库自治服务 开发指南

数据库自治服务

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
数据库自治服务
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关或ASAPI网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**说明**

历史版本使用ASAPI网关调用专有云API的方式仍然有效，详情请参见ASAPI网关调用流程说明、生成 ASAPI的Endpoint、获取ASAPI的SDK包。

**流程图**

数据库自治服务

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

|  | resourcegroupid>， |
|---|---|

不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
数据库自治服务您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
数据库自治服务

## 准备工作

### 登录API与工具控制台

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。
5. 在页面顶部的菜单栏中，选择**产品** > **其他** **> API****与工具**。

### 查看API信息

您在使用SDK时，需要获取产品名称、API名称和API版本。本文介绍如何查看API信息。

**背景信息**

API目录中的API仅供调用参考，具体API的使用方式需要参见各云产品的API文档。如果发生不一致情况，以 API支持情况为准。

**操作步骤**

1. 登录API与工具控制台。
2. 在左侧导航栏中选择**API****目录**。
数据库自治服务
3. 在**API****目录**页面，在下拉列表中选择对应的产品，输入API名称的关键词进行搜索。
4. 查看并记录对应的产品名称、API名称和API版本。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

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
数据库自治服务 Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

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

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。更多STS内容请参见什么是STS。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com>，请替换为实际的STS Endpoint。 数据库自治服务

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `//` 请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`

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

`//` 获取到`STS`三元组

```java
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
} private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
```

`// <sts.aliyuns.com>` 请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
    request.setSysDomain("<sts.aliyuns.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`<yourRoleSessionName>`请您替换为实际值

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`<yourRoleArn>`请替换为上一步获取到的实际`Ram Role ARN`

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
数据库自治服务

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// <yourRegionID>`请替换为您实际的地域`ID` `// <yourStsAccessKeyID>, <yourStsAccessKeySecret>`请替换为前一步获取到的`STS`三元组中`Acce`

```xml
ssKeyID、AccessKeySecret
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

`//<yourRegionID>`请替换为您实际的地域`ID`

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// <yourStsToken>`请替换为您前一步获取到的`STS`三元组中`SecurityToken`

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,请替换为您实际的资源集`ID`

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为您实际的组织`ID`

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

数据库自治服务

### 获取公共Header参数

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，获取方式请参见获取Region ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取实例ID。 |

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理**>**地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看Region ID。

**获取组织ID**

组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。

**获取资源集ID**

资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**获取实例ID**

请各云产品自行修改替换产品名及获取实例ID流程实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以ECS为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**弹性计算**>**云服务器****ECS**。
3. 在左侧导航栏中，单击**实例**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

数据库自治服务对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 获取产品名的Endpoint

本文介绍了如何获取产品名Endpoint。标题及短描述中产品名，请各云产品自行替换

**背景信息**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以通过如下方法自行获取Endpoint。

**操作步骤**

**警告**

1. 2. 3. 4. 数据库自治服务

## 通过POP网关调用专有云API

### 调用前置

阿里云专有云与公有云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

阿里云专有云既支持通过ASAPI网关调用专有云API，也支持通过POP网关调用专有云API。为了使专有云保持与公有云相同的使用方式，使您拥有和更方便，更一致的体验，建议通过POP网关调用专有云API。

**获取云产品的Endpoint**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。 您也可以自行获取Endpoint，本文以ECS为例为您介绍获取云产品业务域Endpoint的方法。
1. 登录天基。
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏单击**运维**。 iii. 在左侧导航栏中选择**产品运维管理**>**产品列表**。 iv. 单击**天基**。
2. 在左侧导航栏中单击**报表**。
3. 在**全部报表**页面搜索服务注册变量，单击报表名称。
4. 在**服务注册变量**页面，单击**Service**旁的
图标，搜索 `ECS` 。
5. 在 `ecs-yaochi` 服务的**Service Registration**列中，单击鼠标右键，选择**显示更多**。
在**详情**页面，查看的**internal.openapi.endpoint**值，即 `Endpoint` 。

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

数据库自治服务通过阿里云开发工具包（SDK）下载对应产品的安装依赖。 HTTPS访问设置为忽略SSL证书验证。

**调用示例**

RPC调用，示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeInstances {
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
        request.setSysDomain("<ecsEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2014-05-26");
        // 设置LocationProduct
        request.setSysLocationProduct("Ecs");
```

`//` 设置访问接口的名称

```
        request.setSysAction("DescribeInstances");
```

`//` 当使用`sts ak`调用`RPC`接口时需要在参数中加上`SecurityToken`字段

```
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
```

`//` 业务参数

```
        request.putBodyParameter("PageSize", "10");
        request.putBodyParameter("PageNumber", "1");
```

`//`必填值，调用来源说明数据库自治服务 `//` 必填值，调用来源说明

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

`//` 必填组织`ID`

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
```

数据库自治服务

```
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

`//` 非必填，资源集`ID`

```
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 必填组织`ID`

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

设置HTTPS访问，一定要设置忽略SSL证书验证。 数据库自治服务

### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

通过阿里云开发工具包（SDK）下载对应产品的安装依赖。

**背景信息**

当前支持RPC和ROA的方式调用API。

**调用示例**

RPC方式调用示例接口信息：产品（ECS）、接口（DescribeInstances）、版本（2014-05-26）。 示例代码如下： 数据库自治服务

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
    request.Domain = "<ECSEndpoint>"
    request.Version = "2014-05-26"
    request.ApiName = "DescribeInstances"
    request.Product = "Ecs"
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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 数据库自治服务

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 数据库自治服务

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

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

通过阿里云开发工具包（SDK）下载对应产品的安装依赖。

**背景信息**

目前仅支持通过RPC方式调用API。

**调用示例**

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

`timeout=1000, #` 设置超时时间 `verify=False, #` 忽略证书或者 `verify='<`证书位置`>'`

```
);
```

# 和`https`一起使用

```bash
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
```

数据库自治服务

```python
def hello_ecs_instance():
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
    request.set_body_params(params)
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
    request.set_version("2014-05-26")
    request.set_action_name("DescribeInstances")
    request.set_endpoint("<ecsEndpoint>")   //Endpoint请替换为真实地址
    request.set_product("Ecs")
    request.set_method("POST")
```

# 发起`API`请求并显示返回值

```python
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    hello_ecs_instance()
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

数据库自治服务

## API参考

### 公共参数

**公共请求参数**

公共请求参数是每个接口调用都需要提供的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | Strin g | 否 | 返回值的类型，仅支持JSON。 |
| Version | Strin g | 是 | API 版本号，以日期形式YYYY-MM-DD输入，取值： 2019-05-10。 |
| AccessKeyId | Strin g | 是 | 访问服务使用的密钥ID。 |
| AccessKeySe cret | Strin g | 是 | 访问服务使用的密钥值。 |
| RegionId | Strin g | 是 | 访问服务所使用的的地域ID。 |
| Product | Strin g | 是 | 接口对应的产品名称。 |

您也可以通过Apsara Uni-manager运营控制台获取接口所需要的 `Product` 和 `Version` 参数。具体操作步骤如下。
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中选择**产品** > **其他** **> API****与工具**。
3. 在左侧导航栏中单击**API****目录**。
4. 在**API****名称**文本框中输入接口名称，即可查询接口的信息。

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织 ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取实例ID。 |

数据库自治服务在调用各云产品接口调用时，您需要在调用代码的请求头Header中添加**x-acs-**

**说明**

**organizationid**、**x-acs-resourcegroupid**、**x-acs-instanceid**等参数的实际值，用于指定当
前实例的实例ID（在创建实例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。 若未添加相关Header参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

### Key分析

#### 获取排名前100的大Key

调用DescribeTopBigKeys接口，获取一段时间内排名前100的大Key。 对数据结构为 List、Hash、Set、Zset 的 Key，按照 Key 中元素的数量排序并展示排名前 3 的 Key，记录为大 Key。 在使用阿里云 SDK 时，需要保证 aliyun-sdk-core 的版本大于 4.3.3，建议使用最新版本。 使用 DAS 的 SDK 的版本为 1.0.2 或以上。 本接口只适用于如下 Redis 实例： 实例为社区版（5.0 及以上版本）或企业版（性能增强型）。 实例的小版本为最新。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ConsoleCo ntext | Strin g | Query | 否 | None | 备用参数。 |
| InstanceId | Strin g | Query | 是 | r-bp18ff4a195d**** | Redis实例ID，您可以调用DescribeInstances接口获取。 |
| NodeId | Strin g | Query | 否 | r-x****-db-0 | Redis实例的数据分片ID， 您可以调用DescribeRoleZoneInfo 接口获取。 |

数据库自治服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| StartTime | Strin g | Query | 是 | 1596177993000 | 查询任务开始时间，格式为 Unix时间戳，单位为毫秒。 |
| EndTime | Strin g | Query | 是 | 1596177993001 | 查询任务结束时间，格式为 Unix时间戳，单位为毫秒。 查询任务结束时间需晚于查询任务开始时间。 仅支持最大查询时间范围为4天内的数据。 StartTime 和E ndTime 最大查询间隔为3小时内。 |
| Action | Strin g | Query | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Array |  | 大Key详细信息列表。 查询时间段内没有大Key时，返回为空。 |
| -Key | String | abc:def:eng | 具体的Key。 |
| -Db | Integer | 0 | Key所在的DB。 |
| -KeyType | String | zset | Key的类型。 |
| -Size | Long | 2 | 元素的个数。 |
| -NodeId | String | r-x****-db-0 | Redis实例的数据分片ID。 |
| Code | String | 200 | 返回的状态码。 |

| 开发指南·API参考 |  |  | 数据库自治服务 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeTopBigKeys &InstanceId=r-bp18ff4a195d**** &StartTime=1596177993000 &EndTime=1596177993001 &Action=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":[
  {
   "KeyType":"zset",
   "Size":2,
   "NodeId":"r-x****-db-0",
   "Key":"abc:def:eng",
   "Db":0
  }
```

`],`

```json
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

#### 实时获取当前热Key和大Key

调用DescribeHotBigKeys接口，实时获取当前内存中的热Key和大Key。 数据库自治服务对数据结构为 List、Hash、Set、Zset 的 Key，按照 Key 中元素的数量排序并展示排名前 3 的 Key，记录为大 Key；当某个 Key 的 QPS 大于 3,000 时会被记录为热点 Key。 在使用阿里云 SDK 时，需要保证 aliyun-sdk-core 的版本大于 4.3.3，建议使用最新版本。 使用 DAS 的 SDK 的版本为 1.0.2 或以上。 本接口只适用于如下 Redis 实例： 实例为社区版（5.0 及以上版本）或企业版（性能增强型）。 实例的小版本为最新。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ConsoleCo ntext | Strin g | Quer y | 否 | None | 备用参数。 |
| InstanceId | Strin g | Quer y | 是 | r-bp18ff4a195d**** | Redis实例ID，您可以调用DescribeInstances接口获取。 |
| NodeId | Strin g | Quer y | 否 | r-****-db-0 | Redis实例的数据分片ID，您可以调用DescribeRoleZoneInfo接口获取。 |
| Action | Strin g | Quer y | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Struct |  | 详情信息列表。 |
| -HotKeyMsg | String | current version doesn't support | 获取热Key失败的原因。 |

数据库自治服务

| -BigKeyMsg | String | current version doesn't support | 获取大Key失败的原因。 |
|---|---|---|---|
| -HotKeys | Array |  | 热键详细列表。 |
| --Key | String |  |  |
| --Db | Integer |  |  |
| --Hot | String |  |  |
| --KeyType | String |  |  |
| --Lfu | Integer |  |  |
| --NodeId | String |  |  |
| -BigKeys | Array |  | 大Key的详细列表。 |
| --Db | Integer |  |  |
| --Key | String |  |  |
| --KeyType | String |  |  |
| --Size | Long |  |  |
| --NodeId | String |  |  |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true：执行成功。 false：执行失败。 |

**示例**

请求示例数据库自治服务

```
http(s)://[Endpoint]/?Action=DescribeHotBigKeys &InstanceId=r-bp18ff4a195d**** &Action=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":{
  "HotKeys":[
   {
    "KeyType":"",
    "NodeId":"",
    "Lfu":"",
    "Hot":"",
    "Key":"",
    "Db":""
   }
```

`],`

```json
  "BigKeyMsg":"current version doesn't support",
  "HotKeyMsg":"current version doesn't support",
  "BigKeys":[
   {
    "KeyType":"",
    "Size":"",
    "NodeId":"",
    "Db":"",
    "Key":""
   }
```

]

```json
 },
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

DAS 数据库自治服务 2020-01-16 DescribeHotBigKeys

#### 获取排名前100的热Key

调用DescribeTopHotKeys接口，获取一段时间内排名前100的热Key。 当某个 Key 的 QPS 大于 3,000 时会被记录为热点 Key。 在使用阿里云 SDK 时，需要保证 aliyun-sdk-core 的版本大于 4.3.3，建议使用最新版本。 使用 DAS 的 SDK 的版本为 1.0.2 或以上。 本接口只适用于如下 Redis 实例： 实例为社区版（4.0 及以上版本）或企业版（性能增强型）。 实例的小版本为最新。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ConsoleCo ntext | Strin g | Quer y | 否 | None | 备用参数。 |
| InstanceId | Strin g | Quer y | 是 | r-bp18ff4a195d**** | Redis实例ID，您可以调用DescribeInstances接口获取。 |
| NodeId | Strin g | Quer y | 否 | r-****-db-0 | Redis实例的数据分片ID，您可以调用DescribeRoleZoneInfo接口获取。 |
| StartTime | Strin g | Quer y | 是 | 1596177993000 | 查询任务开始时间，格式为 Unix时间戳，单位为毫秒。 |
| EndTime | Strin g | Quer y | 是 | 1596177993001 | 查询任务结束时间，格式为 Unix时间戳，单位为毫秒。 |
| Action | Strin g | Quer y | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

数据库自治服务

| Message | String | Successful | 请求返回消息。 |
|---|---|---|---|
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Array |  | 热Key详细信息列表。 |
| -Db | Integer | 0 | Key所在的DB。 |
| -Key | String | abc:def:eng | 具体的Key。 |
| -Hot | String | 5500~6000 | Key的访问频次，即Key的每秒访问数。 |
| -KeyType | String | zset | Key类型。 |
| -Lfu | Integer | 253 | LFU算法的统计值。 |
| -NodeId | String | r-x****-db-0 | Redis实例的数据分片ID。 |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true：执行成功。 false：执行失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeTopHotKeys &InstanceId=r-bp18ff4a195d**** &StartTime=1596177993000 &EndTime=1596177993001 &Action=
```

&公共请求参数正常返回示例 `JSON` 格式数据库自治服务

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":[
  {
   "KeyType":"zset",
   "NodeId":"r-x****-db-0",
   "Lfu":253,
   "Hot":"5500~6000",
   "Db":0,
   "Key":"abc:def:eng"
  }
```

`],`

```json
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

DAS 2020-01-16 DescribeTopHotKeys

#### 查询实例当前的热Key

调用DescribeHotKeys接口，查询Redis实例的热Key。 使用该接口需满足以下前提条件： 在使用阿里云 SDK 时，需要保证 aliyun-sdk-core 的版本大于 4.3.3，建议使用最新版本。 使用 DAS 的 SDK 的版本为 1.0.2 或以上。 本接口只适用于如下 Redis 实例： 实例为社区版（4.0 及以上版本）或企业版（性能增强型）。 实例的小版本为最新。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

数据库自治服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | 是 | r-bp18ff4a195d**** | Redis实例ID，您可以调用DescribeInstances接口获取。 |
| NodeId | Strin g | Quer y | 否 | r-x****-db-0 | Redis实例的数据分片ID，您可以调用DescribeRoleZoneInfo接口获取。 |
| Action | Strin g | Quer y | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Array |  | 详细信息列表。 |
| -Key | String | abc:def:eng | 具体的Key。 |
| -Db | Integer | 0 | Key所在的DB。 |
| -Hot | String | 5500~6000 | Key的访问频次，即Key的每秒访问数。 |
| -KeyType | String | zset | Key的类型。 |
| -Size | Long | 2 | 元素的个数。 |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true：执行成功。 false：执行失败。 |

数据库自治服务

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeHotKeys &InstanceId=r-bp18ff4a195d**** &Action=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":[
  {
   "KeyType":"zset",
   "Size":2,
   "Hot":"5500~6000",
   "Key":"abc:def:eng",
   "Db":0
  }
```

`],`

```json
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

DAS 2020-01-16 DescribeHotKeys

### 缓存分析

#### 查询缓存分析任务列表

调用DescribeCacheAnalysisJobs接口，查询缓存分析任务列表。 使用该接口需满足以下前提条件： 数据库自治服务使用阿里云或 DAS 的 SDK 时，建议使用最新版本。 本接口只适用于 Redis 引擎。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Quer y | 是 | r-bp18ff4a195d**** | 实例ID。 |
| StartTime | Strin g | Quer y | 是 | 1596177993000 | 查询任务开始时间，格式为 Unix时间戳，单位为毫秒。 |
| EndTime | Strin g | Quer y | 是 | 1596177993001 | 查询任务结束时间，格式为 Unix时间戳，单位为毫秒。 |
| PageNo | Strin g | Quer y | 否 | 1 | 页码，取值大于0且不超过 Integer数据类型的最大值， 默认值为1。 |
| PageSize | Strin g | Quer y | 否 | 10 | 每页最大记录数，默认值为 10。 |
| Action | Strin g | Quer y | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Struct |  | 信息列表。 |

数据库自治服务

| -PageNo | Long | 1 | 页码，取值大于0且不超过Integer数据类型的最大值，默认值为1。 |
|---|---|---|---|
| -PageSize | Long | 10 | 每页最大记录数，默认值为10。 |
| -Extra | String | None | 备用参数。 |
| -Total | Long | 4 | 结果数量。 |
| -List | Array |  | 信息详情。 |
| --TaskState | String |  |  |
| --JobId | String |  |  |
| --Message | String |  |  |
| --InstanceId | String |  |  |
| --NodeId | String |  |  |
| --BigKeys | Array |  |  |
| ---Type | String |  |  |
| ---Db | Integer |  |  |
| --- ExpirationTim eMillis | Long |  |  |
| ---Key | String |  |  |
| ---Encoding | String |  |  |
| ---Bytes | Long |  |  |
| ---NodeId | String |  |  |

数据库自治服务

| ---Count | Long |  |  |
|---|---|---|---|
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true：执行成功。 false：执行失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCacheAnalysisJobs &InstanceId=r-bp18ff4a195d**** &StartTime=1596177993000 &EndTime=1596177993001 &Action=
```

&公共请求参数正常返回示例 `JSON` 格式数据库自治服务

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":{
  "PageSize":10,
  "Extra":"None",
  "List":[
   {
    "Message":"",
    "InstanceId":"",
    "BigKeys":[
     {
      "Bytes":"",
      "Type":"",
      "NodeId":"",
      "ExpirationTimeMillis":"",
      "Encoding":"",
      "Count":"",
      "Db":"",
      "Key":""
     }
```

`],`

```json
    "NodeId":"",
    "TaskState":"",
    "JobId":""
   }
```

`],`

```json
  "Total":4,
  "PageNo":1
 },
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

DAS 2020-01-16 DescribeCacheAnalysisJobs

#### 创建缓存分析任务

数据库自治服务使用该接口需满足以下前提条件： 使用阿里云或 DAS 的 SDK 时，建议使用最新版本。 只支持分析 Redis 数据结构和以下 Tair 自研数据结构：TairString、TairHash、TairGIS、 TairBloom、TairDoc、TairCpc、TairZset，暂不支持分析其他 Tair 自研数据结构。 如果目标实例规格已发生变更，则不支持分析实例变更前的备份文件。 暂不支持 Tair 磁盘型实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 |  |  |
| InstanceId | Strin g | Query | 是 | r-bp18ff4a195d**** | Redis实例ID。 |
| NodeId | Strin g | Query | 否 | r-x****-db-0 | 实例的数据节点ID，传入本参数可查询指定节点的监控信息。 当您传入 BackupSetId参数， 系统会忽略此参数，您可调用DescribeLogicInst anceTopology接口查询节点ID。 |
| BackupSe tId | Strin g | Query | 否 | 12345 | 备份文件ID，可以通过DescribeBackups接口获取。 如需传入多个备份文件 ID，请使用英文逗号 （,）分隔，例如 12345,67890 。 如果不传入本参数，系统会自动执行备份并对该备份文件执行缓存分析。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |
| Data | Struct |  | 详细信息列表。 |
| -BigKeys | Array |  | 大Key详细信息，根据Key占用字节数降序排列。 |
| --Type | String |  |  |
| --Db | Integer |  |  |
| -- ExpirationTim eMillis | Long |  |  |
| --Key | String |  |  |
| --Encoding | String |  |  |
| --Bytes | Long |  |  |
| --NodeId | String |  |  |
| --Count | Long |  |  |
| -TaskState | String | BACKUP | 缓存分析任务的状态： BACKUP ：备份中。 ANALYZING ：分析中。 FINISHED ：分析完成。 FAILED ：出现错误。 |

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -JobId | String | sf79-sd99-sa37- **** | 缓存分析任务ID。 此参数可用于查询缓存分析任务使用，当您调用该API时，由于创建缓存分析任务需要一定的时间，不会立即返回分析结果，您需要通过此参数，结合DescribeCacheAnalysisJob接口，查询具体的分析结果。 |
| -Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| -InstanceId | String | r-bp18ff4a195d**** | 实例ID。 |
| -NodeId | String | r-x****-db-0 | 实例的数据节点ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateCacheAnalysisJob &InstanceId=r-bp18ff4a195d**** &Action=
```

&公共请求参数正常返回示例 `JSON` 格式数据库自治服务

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":{
  "Message":"Successful",
  "InstanceId":"r-bp18ff4a195d****",
  "NodeId":"r-x****-db-0",
  "BigKeys":[
   {
    "Bytes":"",
    "Type":"",
    "NodeId":"",
    "ExpirationTimeMillis":"",
    "Encoding":"",
    "Count":"",
    "Db":"",
    "Key":""
   }
```

`],`

```json
  "TaskState":"BACKUP",
  "JobId":"sf79-sd99-sa37-****"
 },
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

#### 查询缓存分析任务详情

使用该接口需满足以下前提条件： 使用阿里云或 DAS 的 SDK 时，建议使用最新版本。 本接口只适用于 Redis 引擎。 调用本接口可查询实例缓存分析任务中排名前 500 的 Key 信息。

**说明**

**说明**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

数据库自治服务使用该接口需满足以下前提条件：
  - 使用阿里云或 `DAS` 的 `SDK` 时，建议使用最新版本。
  - 本接口只适用于 `Redis` 引擎。
`> **`说明`**` 调用本接口可查询实例缓存分析任务中排名前 `500` 的 `Key` 信息。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | r-bp18ff4a195d**** | 实例ID。 |
| JobId | Strin g | Query | 是 | sf79-sd99-sa37-**** | 缓存分析任务ID，您可通过调用CreateCacheAnalysisJ ob接口获取返回参数的 JobId。 |
| Action | Strin g | Query | 是 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Data | Struct |  | 详细信息列表。 |
| -TaskState | String | BACKUP | 缓存分析任务的状态： BACKUP ：备份中。 ANALYZING ：分析中。 FINISHED ：分析完成。 FAILED ：出现错误。 |
| -JobId | String | sf79-sd99-sa37- **** | 缓存分析任务ID。 |

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| -InstanceId | String | r-bp18ff4a195d**** | 实例ID。 |
| -NodeId | String | r-x****-db-0 | 实例的数据节点ID。 |
| -BigKeys | Array |  | 大Key详细信息，根据Key占用字节数降序排列。 |
| --Type | String |  |  |
| --Db | Integer |  |  |
| -- ExpirationTim eMillis | Long |  |  |
| --Key | String |  |  |
| --Encoding | String |  |  |
| --Bytes | Long |  |  |
| --NodeId | String |  |  |
| --Count | Long |  |  |
| -KeyPrefixes | Array |  | Key前缀列表。 |
| --KeyNum | Long |  |  |
| --Type | String |  |  |
| --Bytes | Long |  |  |
| --Prefix | String |  |  |
| --Count | Long |  |  |
| - BigKeysOfNum | Array |  | 大Key详细信息，根据Key数量降序排列。 |
| --Type | String |  |  |
| --Db | Integer |  |  |

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- ExpirationTim eMillis | Long |  |  |
| --Key | String |  |  |
| --Encoding | String |  |  |
| --Bytes | Long |  |  |
| --NodeId | String |  |  |
| --Count | Long |  |  |
| - UnexBigKeysO fBytes | Array |  | 永不过期Key的详细信息，根据Key占用字节数降序排列。 |
| --Type | String |  |  |
| --Db | Integer |  |  |
| -- ExpirationTim eMillis | Long |  |  |
| --Key | String |  |  |
| --Encoding | String |  |  |
| --Bytes | Long |  |  |
| --NodeId | String |  |  |
| --Count | Long |  |  |
| - UnexBigKeysO fNum | Array |  | 永不过期Key的详细信息，根据Key数量降序排列。 |
| --Type | String |  |  |
| --Db | Integer |  |  |
| -- ExpirationTim eMillis | Long |  |  |
| --Key | String |  |  |
| --Encoding | String |  |  |
| --Bytes | Long |  |  |
| --NodeId | String |  |  |
| --Count | Long |  |  |

| 开发指南·API参考 |  |  | 数据库自治服务 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ExpiryKeysLev elCount | Array |  |  |
| --AnalysisTs | Long |  |  |
| --Level | Integer |  |  |
| --TotalBytes | Long |  |  |
| --TotalKeys | Long |  |  |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeCacheAnalysisJob &InstanceId=r-bp18ff4a195d**** &JobId=sf79-sd99-sa37-**** &Action=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Data":{
  "BigKeysOfNum":[
   {
    "Bytes":"",
    "Type":"",
    "NodeId":"",
    "ExpirationTimeMillis":"",
    "Encoding":"",
    "Count":"",
    "Db":"",
    "Key":""
   }
```

`],`

```json
  "UnexBigKeysOfBytes":[
   {
    "Bytes":"",
    "Type":"",
```

数据库自治服务

```json
    "NodeId":"",
    "ExpirationTimeMillis":"",
    "Encoding":"",
    "Count":"",
    "Db":"",
    "Key":""
   }
```

`],`

```json
  "Message":"Successful",
  "InstanceId":"r-bp18ff4a195d****",
  "NodeId":"r-x****-db-0",
  "ExpiryKeysLevelCount":[
   {
    "TotalBytes":"",
    "Level":"",
    "AnalysisTs":"",
    "TotalKeys":""
   }
```

`],`

```json
  "BigKeys":[
   {
    "Bytes":"",
    "Type":"",
    "NodeId":"",
    "ExpirationTimeMillis":"",
    "Encoding":"",
    "Count":"",
    "Db":"",
    "Key":""
   }
```

`],`

```json
  "KeyPrefixes":[
   {
    "Bytes":"",
    "Type":"",
    "KeyNum":"",
    "Prefix":"",
    "Count":""
   }
```

`],`

```json
  "UnexBigKeysOfNum":[
   {
    "Bytes":"",
    "Type":"",
    "NodeId":"",
    "ExpirationTimeMillis":"",
    "Encoding":"",
    "Count":"",
    "Db":"",
    "Key":""
   }
```

`],`

```json
  "TaskState":"BACKUP",
  "JobId":"sf79-sd99-sa37-****"
```

数据库自治服务

```json
 },
 "Code":"200",
 "Success":"true"
}
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | -1001 | InvalidParams | The request parameters are invalid. |
| 403 | 403 | NoPermission | You are not authorized to do this action. |

### GetSlowRequestRecords

获取慢日志请求记录。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | System | 是 | GetSlowRequestRecords | 系统规定参数。取值： GetSlowRequestRecords |
| InstanceId | Strin g | Query | 否 | pxc-unrs3lrchgzfid | 实例ID。 |
| NodeId | Strin g | Query | 否 | pxc-unrs3lrchgzfiddawj- cn#pxc-i-qaibfzqlqo | 节点ID。 |
| DbName | Strin g | Query | 否 | testDB | 数据库名。 |
| Start | Strin g | Query | 否 | 1749431640000 | 统计开始时间。 |
| End | Strin g | Query | 否 | 1749435240000 | 统计结束时间。 |
| PageNo | Strin g | Query | 否 | 1 | 页码。 |
| PageSize | Strin g | Query | 否 | 30 | 分页查询，每页大小。 |

**返回数据**

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Synchro | String | true | 备用参数。 |
| Data | String | { "total":1, "pageNo":1, "pageSize":30, "list":[ { "schema":"***", "rows examined":- _ 1, "sql id":" 1676873 _ _ 441%7C46", "max rows examin _ _ ed":-1, "count":1, "max query time": _ _ 1.494, "sql":"****", "lock time":0.0, _ "rows sent":0, _ "database":"***", "host":"10.***", "max lock time":0. _ _ 0, "user":"***", "max rows sent":0 _ _ , "query time":1.494 _ , "timestamp":1752 227282000 } ] } | "schema": 数据库名。 "rows examined": 总扫描行数。 _ "sql id": 实例的SQLId。 _ "max rows examined": 最大扫描行数。 _ _ "count":执行总次数。 "max query time": 最大SQL时间（秒）。 _ _ "sql": SQL语句。 "lock time": lock等待时间。 _ "rows sent": 总返回行数。 _ "database": 数据库名。 "host": 客户端ip。 "max lock time": 最大lock等待时间。 _ _ "user": 用户名。 "max rows sent":最大返回行数。 _ _ "query time": SQL运行时间（秒）。 _ "timestamp": 执行时间。 |
| Code | String | 200 | 状态码。 |
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetSlowRequestRecords
```

&公共请求参数正常返回示例 `JSON` 格式数据库自治服务

```json
{
 "Message":"Successful",
 "RequestId":"B6D17591-B48B-4D31-9CD6-9B9796B2****",
 "Synchro":"true",
 "Data":"{\t\t\"total\":1,\t\t\"pageNo\":1,\t\t\"pageSize\":30,\t\t\"list\":[\t\t\t{\t\
t\t\t\"schema\":\"***\",\t\t\t\t\"rows_examined\":- 1,\t\t\t\t\"sql_id\":\"_1676873441%7C46\",\t\t\t\t\"max_rows_examined\":- 1,\t\t\t\t\"count\":1,\t\t\t\t\"max_query_time\":1.494,\t\t\t\t\"sql\":\"****\",\t\t\t\t\ ock_time\":0.0,\t\t\t\t\"rows_sent\":0,\t\t\t\t\"database\":\"***\",\t\t\t\t\"host\":\"10
**\",\t\t\t\t\"max_lock_time\":0.0,\t\t\t\t\"user\":\"***\",\t\t\t\t\"max_rows_sent\":0,\
t\t\t\"query_time\":1.494,\t\t\t\t\"timestamp\":1752227282000\t\t\t}\t]}",
 "Code":"200",
 "Success":"true"
}
```

`XML` 格式

```xml
<Message>Successful</Message> <RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2****</RequestId> <Synchro>true</Synchro> <Data>{
  &quot;total&quot;:1,
  &quot;pageNo&quot;:1,
  &quot;pageSize&quot;:30,
  &quot;list&quot;:[
   {
    &quot;schema&quot;:&quot;***&quot;,
    &quot;rows_examined&quot;:-1,
    &quot;sql_id&quot;:&quot;_1676873441%7C46&quot;,
    &quot;max_rows_examined&quot;:-1,
    &quot;count&quot;:1,
    &quot;max_query_time&quot;:1.494,
    &quot;sql&quot;:&quot;****&quot;,
    &quot;lock_time&quot;:0.0,
    &quot;rows_sent&quot;:0,
    &quot;database&quot;:&quot;***&quot;,
    &quot;host&quot;:&quot;10.***&quot;,
    &quot;max_lock_time&quot;:0.0,
    &quot;user&quot;:&quot;***&quot;,
    &quot;max_rows_sent&quot;:0,
    &quot;query_time&quot;:1.494,
    &quot;timestamp&quot;:1752227282000
   }
```

]

```xml
}</Data>
 <Code>200</Code>
 <Success>true</Success>
```

### 接入数据库实例

其他系统比如DMS,跳转到HDM控制台前需要传递的信息内容数据库自治服务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 否 | xxx | 接口名称 |
| InstanceA rea | Strin g | Query | 否 | ECS | 实例区域 |
| InstanceId | Strin g | Query | 否 | rm-2ze1jdv45i7l6**** | 实例ID |
| Ip | Strin g | Query | 否 | rm- 2ze1jdv45i7l6****.mysql .rds.aliyuncs.com | IP地址 |
| Port | Strin g | Query | 否 | 3306 | 端口 |
| Engine | Strin g | Query | 否 | mysql | 引擎 |
| Username | Strin g | Query | 否 | test**** | 用户名 |
| Password | Strin g | Query | 否 | 122**** | 密码 |
| InstanceAl ias | Strin g | Query | 否 | yuecq--test**** | region区 |
| NetworkT ype | Strin g | Query | 否 | VPC | 网络类型 |
| VpcId | Strin g | Query | 否 | vpc- m5e666n89m2bx8jar*** * | VPC的ID |
| Region | Strin g | Query | 否 | cn-hangzhou | 区域 |
| CallerBid | Strin g | Query | 否 | None | pop层面传递 |
| OwnerId | Strin g | Query | 否 | 325**** | 实例拥有者 |
| TenantId | Strin g | Query | 否 | L0EPfLS****=SCE00000* **** | 租户ID |
| OwnerIdSi gnature | Strin g | Query | 否 | B6D17591-B48B- 4D3**** | 签名 |

| 开发指南·API参 | 考 |  |  |  | 数据库自治服务 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CallerTyp e | Strin g | Query | 否 | None | 账号类型，子账号还是主账号 |
| CallerUid | Strin g | Query | 否 | 31063db679**** | 来源ID |
| Target | Strin g | Query | 否 | None | 目标 |
| Product | Strin g | Query | 否 | None | 产品来源 |
| External | Strin g | Query | 否 | None | 附加信息，比如诊断信息中的SQL库表信息等 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回的消息 |
| RequestId | String | 40C6E9AF-6C23- 5614-AA83- 34344CC6**** | 请求ID。 |
| Synchro | String | None | 备用参数 |
| Data | String | None | 备用参数 |
| Code | String | 200 | 返回的状态码 |
| Success | String | true | 请求是否执行成功 |

**示例**

`JSON` 格式数据库自治服务

```
Code
```

:

```
Data
```

:

```
"a05f23b1ca12c47f88a22931d5e85134" Message
```

:

```
"Successful" RequestId
```

:

```
"bf950b45-adfb-4cfa-882f-163d40623f2f" Success
```

:

```
true asapiRequestId
```

:

```
"803273B7-FC4A-4E46-85B1-486FA9AC04E0" asapiSuccess
```

:

```
true eagleEyeTraceId
```

:

```
"0ac8246917024589921981465e0031" eagleEyeTraceId
```

:

```
"0ac8246917024589921981465e0031" requestId
```

:

```
"bf950b45-adfb-4cfa-882f-163d40623f2f" successResponse
```

:

```
true
```

### AccessHDMInstanceByToken -

**接入实例**

通过Token找到DMS POST过来的实例，接入到实例元数据表中

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Token | Strin g | Query | 否 | 201b07d2d5b5d75bc58 653b20bc91229 | 调用AccessHDMInstance 接口后返回的token字符串 |

**返回数据**

数据库自治服务

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| RequestId | String | ac544623-f6ad- 45fd-9a74- 9be3db65**** | 请求ID。 |
| Synchro | String | None | 备用参数 |
| Data | String | { "instanceId": "pc- nj205fmvqra3q9m 9l", "role": "logical", "port": 5432, "ip": "pc- nj205fmvqra3q9m 9l", "vpcId": "vpc- nj24dnb0c1a3khj1 3wwhu", "gmtCreate": 1749991399000, "uuid": "hdm 929b5a868a _ 6f0f9a84b75c0710 167916", "token": "802884224851A7 F630E967FBD4616 99546E12BA1A7AF 7B9FC33362AEC99 F7804" } | 返回数据 |
| Code | String | 200 | 返回的状态码。 |
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |

### GetSlowRequestDirectly - 通过

**直连查询当前数据库的慢日志**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

数据库自治服务

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Uuid | Strin g | Query | 否 | hdm 2bdef9f8b34455a4 _ 0f617c4****** | 数据库实例在DAS中的唯一标识 |
| Num | Strin g | Query | 否 | 10 | 慢日志条数 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2**** | 请求ID。 |
| Synchro | String | None | 备用参数 |
| Data | String | { "host": "10.205.29.46:598 36", "queryTime": 61571, "id": 0, "sql": [ "KEYS", "*" ], "timestamp": 1747653552 } | 返回数据。 |
| Code | String | 200 | 状态码。 |
| Success | String | true | 请求是否执行成功： true ：执行成功。 false ：执行失败。 |
