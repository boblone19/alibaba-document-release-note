---
title: "网关 API网关 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 333
source_pdf: "18_API网关 开发指南_ai-gateway-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apigateway/zh/ai-gateway-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 网关 API网关 开发指南

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
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

| 获取API信息获取AccessKey或STS AccessKey 获取公共Header参数 |  |
|---|---|
| 获取AI网关的Endpoint 获取AI网关的SDK包调用API |  |

准备工正式调

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

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|

| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
| x-acs-instanceid | 进行操作的实例ID，例如，ECS的实例ID可以从ECS列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

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
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例， 获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **中间件** > **应用集成** > **API** **网关**。
3. 在左侧导航栏中，单击**实例列表**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|

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
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。

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

3. 通过STS可以调用云产品的接口，示例如下。

```java
import com.aliyun.credentials.Client; import com.aliyun.credentials.models.Config;
```

`//` 以下示例演示如何使用`STS Token`初始化凭据客户端（不包含如何获取到`STS Token`的过程）。

```java
public class DemoStsTest {
    public static void main(String[] args) {
        Config credentialConfig = new Config();
        credentialConfig.setType("sts");
```

`//` 请替换为前一步获取到的`STS`三元组中`AccessKeyI`。

```
        credentialConfig.setAccessKeyId("your_AccessKeyId");
```

`//` 请替换为前一步获取到的`STS`三元组中`AccessKeySecret`

```
        credentialConfig.setAccessKeySecret("your__AccessKeySecret");
```

`//` 请替换为前一步获取到的`STS`三元组中`SecurityToken`

```
        credentialConfig.setSecurityToken("your__SecurityToken");
        Client credentialClient = new Client(credentialConfig);
```

`//` 继续调用`API`，完整参考的`API`文档

```
    }
}
```

### 获取用户和角色信息

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 创建用户。
i. 在顶部菜单栏，选择**企业**。 ii. 在左侧导航栏，选择**人员管理** > **用户管理**。 iii. 在**系统用户**页签，单击**创建用户。** iv. 在**创建用户**对话框，配置用户信息后，单击**确定**。 更多配置信息请参考**《统一云管平台****用户指南》** > **创建用户**章节。
3. 创建角色。
i. 在左侧导航栏，选择**权限管理**> **角色授权**。 ii. 在角色列表上方，单击**创建自定义角色**。 iii. 设置**基础配置**，单击**下一步**。
**管理范围**：选择**资源集**。
iv. 设置**管理权限**，在权限列表勾选**查看****RAM****服务角色**和**创建****RAM****服务角色**权限后，单击**下一步**。
4. 为用户添加角色。
i. 在左侧导航栏，选择**人员管理** > **用户管理**。 ii. 在**系统用户**页签，找到新创建的用户，单击用户**操作**列的 ，选择**角色授权**。 iii. 在**角色授权**对话框，添加新创建的用户角色后，单击**确定**。
5. 将用户添加到资源集。
i. 在**系统用户**页签，找到新创建的用户，单击用户名。 ii. 在**所属资源集**页签下，单击列表上方的**加入资源集**。 iii. 在**加入资源集**对话框中，**选择角色类型**下拉列表选择用户的角色，**选择资源集**列表勾选需要加入的资源集，单击**确定**。

### 获取地域ID和组织ID

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**企业**。
3. 在左侧导航栏，选择**资源管理** > **地域管理**。
4. 在左侧组织架构，单击目标组织，在右侧的**Region****列表**中，获取Region ID。

**获取组织ID**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **中间件** > **应用集成** **> API** **网关**。
3. 在左侧导航栏，选择**API****网关** > **实例列表**或**AI****网关**。
4. 在**网关实例**页面，打开开发者工具，单击Network页签，然后刷新页面。
5. 在搜索框输入**ListResourceGroupByOrgId**，单击接口名称，在右侧的Preview页签获取组织ID。

## 通过POP网关调用专有云API

### Java版本

**环境要求**

支持 JDK8~JDK19，Platform 支持：Linux、Mac、Windows。

**安装说明代码**

使用 Maven 依赖配置：

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
```

<!-- 注意：版本号请以您专有云环境的开发者文档为准 `-->`

```xml
    <version>4.6.0</version>
</dependency> <dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.53</version>
</dependency>
```

**安装说明文档**

**配置说明**

| 配置项 | 说明 |
|---|---|
| regionId | 地域ID。 参考获取地域ID和组织ID。 |
| AccessKeyId | 用户AccessKey ID。 参考获取AccessKey。 |
| AccessKeySecret | 用户AccessKey Secret。 参考获取AccessKey。 |
| endpoint | API访问域名。 参考获取API信息及其EndPoint。 |
| organizationId | 组织ID。 参考获取地域ID和组织ID。 |

| httpProxy | 代理地址（可选）。 请联系阿里云驻场人员获取。 |
|---|---|

**代码示例**

```java
package com.aliyun.apsarastack; import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONArray; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.AcsResponse; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.HttpResponse; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; /**
```

`*/`

```java
public class Sample {
    private static IAcsClient client;
```

`// API`路径定义

```java
    private static final String LIST_ROUTES = "/route/listRoutes";
    public static void main(String[] args) throws ClientException {
        listRoutes();
    }
    /**
```

* 查询路由列表示例
`*/`

```java
    private static void listRoutes() throws ClientException {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);
        request.put("size", 10);
        request.put("gwInstanceId", "your_instance_id");
        CommonResponse response = getCommonResponse(request, LIST_ROUTES,
MethodType.POST);
        HttpResponse httpResponse = response.getHttpResponse();
```

```java
        if (httpResponse.getStatus() == 200) {
            JSONObject jsonObject =
JSON.parseObject(httpResponse.getHttpContentString());
            if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
                Object data = jsonObject.get("data");
                if (data instanceof JSONObject) {
                    JSONObject dataObj = (JSONObject) data;
                    JSONArray records = (JSONArray) dataObj.get("records");
                    records.forEach(record -> {
                        System.out.println(JSON.toJSONString(record));
                    });
                }
            }
            System.out.println(jsonObject);
        }
    }
    /**
```

* 通用请求方法
* `* @param param` 请求参数

```
     * @param path API路径
     * @param methodType HTTP方法类型
```

`* @return` 响应结果 `* @throws ClientException` 客户端异常 `*/`

```
    public static CommonResponse getCommonResponse(Object param, String path, MethodTyp
e methodType) throws ClientException {
        CommonRequest request = new CommonRequest();
        request.setSysUriPattern(path);
        request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8",
FormatType.JSON);
        initDefaultHeader(request, methodType);
        return client.getCommonResponse(request);
    }
    static {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
                "<your-regionId>",      // 地域ID
                "<AccessKey ID>",        // AccessKey ID
                "<AccessKey Secret>");   // AccessKey Secret
```

`//` 可选：设置代理

```
        HttpClientConfig httpClientConfig = HttpClientConfig.getDefault();
        httpClientConfig.setHttpProxy("http://127.0.0.1:9898");
        profile.setHttpClientConfig(httpClientConfig);
        client = new DefaultAcsClient(profile);
    }
    /**
```

* 设置请求`Header`
* `* @param request` 请求对象

```
     * @param methodType HTTP方法类型
```

`* @param <T>` 响应类型 `*/`

```java
    private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request
, MethodType methodType) {
```

`//` 必填：调用来源说明，通常使用调用方应用的唯一标识

```
        request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name");
```

`//` 必填：组织`ID`

```
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
```

`//` 可选：资源组`ID`

```
        // request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
```

`//` 可选：角色`ID`

```
        // request.putHeadParameter("x-acs-roleId", "<your-roleId>");
```

`//` 设置请求方式

```
        request.setSysMethod(methodType);
```

`//` 设置云产品`Endpoint`

```
        request.setSysDomain("<your-endpoint>");
        // 设置LocationProduct
        request.setSysProduct("csb-cop");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2023-02-06");
    }
}
```

**步骤示例**

1. .** **初始化客户端**
创建 `DefaultProfile` 并配置 AccessKey、Secret 和 Endpoint 等信息：

```
DefaultProfile profile = DefaultProfile.getProfile(
        "<your-regionId>",      // 地域ID
        "<AccessKey ID>",        // AccessKey ID
        "<AccessKey Secret>");   // AccessKey Secret
```

`//` 可选：设置代理

```
HttpClientConfig httpClientConfig = HttpClientConfig.getDefault(); httpClientConfig.setHttpProxy("http://127.0.0.1:9898"); profile.setHttpClientConfig(httpClientConfig); IAcsClient client = new DefaultAcsClient(profile);
```

2. .** **构建请求参数**
根据具体 API 的要求构建请求参数 Map：

```
Map<String, Object> request = new HashMap<>(); request.put("current", 1); request.put("size", 10); request.put("gwInstanceId", "your_instance_id");
```

3. .** **创建** **CommonRequest**
设置请求路径、请求体和请求方式：

```
CommonRequest request = new CommonRequest(); request.setSysUriPattern("/route/listRoutes"); request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8", FormatType.JSON);
```

4. .** **设置请求** **Header**
设置必要的 Header 信息：

```
request.putHeadParameter("x-acs-caller-sdk-source", "your-app-name"); request.putHeadParameter("x-acs-organizationid", "<your-organizationid>"); request.setSysMethod(MethodType.POST); request.setSysDomain("<your-endpoint>"); request.setSysProduct("csb-cop"); request.setSysVersion("2023-02-06");
```

5. .** **发送请求并处理响应**

```
CommonResponse response = client.getCommonResponse(request); HttpResponse httpResponse = response.getHttpResponse(); if (httpResponse.getStatus() == 200) {
    JSONObject jsonObject = JSON.parseObject(httpResponse.getHttpContentString());
    if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
        Object data = jsonObject.get("data");
```

`//` 处理返回数据

```java
        System.out.println(JSON.toJSONString(data));
    }
}
```

6. .** **异常处理**

```
try {
    CommonResponse response = client.getCommonRequest(request);
```

`//` 处理响应

```
} catch (ClientException e) {
```

`//` 处理客户端异常

```java
    System.out.println("ErrorCode: " + e.getErrCode());
    System.out.println("ErrorMessage: " + e.getErrMsg());
}
```

**自建 ACK 环境调用方式**

如果是用户自建 ACK 环境，不需要 AK/SK/Proxy 等信息，通过控制台服务的 endpoint 调用即可。

**获取控制台 Endpoint**

`kubectl get svc -n <`控制台服务所在`namespace>` 找到 `cop-gateway-admin-svc` 的 IP 地址作为 endpoint。

**代码示例**

```
static {
```

`//` 创建`DefaultAcsClient`实例并初始化

```java
    DefaultProfile profile = DefaultProfile.getProfile(
            "-",  // regionId 不需要
            "-",  // AccessKey ID 不需要
            "-"); // AccessKey Secret 不需要
    client = new DefaultAcsClient(profile);
} private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request, Me thodType methodType) {
```

`//` 自建`ACK`环境特有的认证`Header`

```
    request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
    request.putHeadParameter("X-CSB-OPENAPI", "true");
    request.setSysMethod(methodType);
    request.setSysDomain("<控制台服务IP>");
    request.setSysProduct("csb-cop");
    request.setSysVersion("2023-02-06");
}
```

**常见 API 路径**

| 功能 | API路径 |
|---|---|
| 查询实例列表 | /gatewayInstance/listInstances |
| 创建服务 | /microservice/createService |
| 查询路由列表 | /route/listRoutes |
| 创建路由 | /route/createRoute |
| 查询域名列表 | /domain/listDomains |

### 常用接口调用方式

**概述**

本文档描述API网关控制台的通用接口调用方式，包括请求格式、响应格式、认证方式等。适用于API网关 （SCG）的所有接口。

**接口基本信息**

| 项目 | 说明 |
|---|---|
| 接口协议 | HTTP/HTTPS |
| 请求方式 | POST（主要）、GET |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |
| 接口前缀 | / |

**统一请求格式**

**请求头**

| 参数 | 必填 | 说明 |
|---|---|---|
| Content-Type | 是 | application/json 。 |
| Authorization | 是 | 用户认证令牌。 |
| x-acs-request-id | 否 | 请求追踪ID，用于日志追踪。 |

**请求体**

所有接口采用JSON格式请求体，基本结构如下：

```json
{
  "gwInstanceId": "xxx",
```

`... //` 其他业务参数

```
}
```

**说明**

大部分接口需要传入 gwInstanceId 参数，用于指定操作的网关实例。

**统一响应格式**

**响应结构**

| 参数 | 类型 | 说明 |
|---|---|---|
| requestId | String | 请求追踪ID。 |
| code | Integer | 响应状态码。 |
| msg | String | 响应消息（错误时返回错误信息）。 |
| data | Object | 响应数据（业务数据）。 |

**状态码说明**

| 状态码 | 说明 |
|---|---|
| 200 | 请求成功。 |
| 500 | 请求失败（业务异常）。 |
| 400 | 请求参数错误。 |
| 401 | 未授权/认证失败。 |

**成功响应示例**

```json
{
  "requestId": "abc****456",
  "code": 200,
  "msg": null,
  "data": {
    "routeId": "route-001",
    "routeName": "test-route"
  }
}
```

**失败响应示例**

```json
{
  "requestId": "ab****f456",
  "code": 500,
  "msg": "Route not found",
  "data": null
}
```

**分页响应示例**

```json
{
  "requestId": "ab****456",
  "code": 200,
  "msg": null,
  "data": {
    "size": 10,
    "current": 1,
    "total": 100,
    "records": [
      { "id": "1", "name": "item-1" },
      { "id": "2", "name": "item-2" }
```

]

```
  }
}
```

**认证方式**

**用户认证**

通过 `Authorization` 请求头传递认证令牌：

```
Authorization: Bearer <token>
```

或使用Cookie认证（Web控制台方式）。

**消费者认证（API调用）**

调用网关API时，消费者通过以下方式传递API Key：

| 方式 | 说明 |
|---|---|
| 请求头 | Authorization: Bearer <api-key> 或 x- api-key: <api-key> 。 |
| 查询参数 | ?api key=<api-key> 。 _ |

|  |  | Authorization: Bearer <api-key> |
|---|---|---|
|  | api-key: <api-key> |  |

具体认证方式由网关实例的认证配置决定。

**通用参数说明**

**网关实例ID（gwInstanceId）**

大部分接口需要传入网关实例ID，用于区分操作的目标实例。系统会根据实例ID自动识别网关类型，并执行相应的处理逻辑。

**分页参数**

列表查询接口支持分页参数：

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| current | Integer | 1 | 当前页码。 |
| size | Integer | 10 | 每页条数。 |

**搜索参数**

列表查询接口支持搜索参数：

| 参数 | 类型 | 说明 |
|---|---|---|
| searchName | String | 搜索关键字（按名称模糊匹配）。 |

**接口分类概览**

| 模块 | 接口路径 | 说明 |
|---|---|---|
| 路由管理 | /route | 路由配置管理。 |
| 服务管理 | /service | 服务注册管理。 |
| 域名管理 | /domain | 域名绑定管理。 |
| 消费者管理 | /app | 消费者/API Key管理。 |
| 证书管理 | /certificate | SSL证书管理。 |
| 来源管理 | /source | 服务来源管理。 |
| 策略管理 | /strategy | 路由策略配置。 |

| 策略配置 | /strategyConfig | 策略实例管理。 |
|---|---|---|
| 实例管理 | /gatewayInstance | 网关实例管理。 |
| 集群管理 | /k8sCluster | K8s集群管理。 |

**错误处理**

**业务异常**

当业务逻辑出现异常时，返回：

```json
{
  "code": 500,
```

`"msg": "<`错误信息`>",`

```json
  "data": null
}
```

常见业务异常：

| 错误信息 | 说明 |
|---|---|
| Route not found | 路由不存在。 |
| Service not found | 服务不存在。 |
| Permission denied | 权限不足。 |
| Instance not found | 网关实例不存在。 |

**参数校验异常**

当请求参数校验失败时，返回：

```json
{
  "code": 500,
  "msg": "<field> <error message>",
  "data": null
}
```

示例：

```json
{
  "code": 500,
  "msg": "gwInstanceId must not be blank",
  "data": null
}
```

**请求示例**

**cURL示例**

# 创建路由

```json
curl -X POST 'http://localhost:8080/route/createRoute' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <token>' \
  -d '{
    "gwInstanceId": "instance-001",
    "routeName": "test-route",
    "path": "/api/test",
    "serviceId": "service-001"
  }'
```

**HTTP请求示例**

```json
Host: localhost:8080 Content-Type: application/json Authorization: Bearer <token> {
  "gwInstanceId": "instance-001",
  "routeName": "test-route",
  "path": "/api/test",
  "serviceId": "service-001"
}
```

**最佳实践**

1. .** **请求追踪**
始终在请求头中携带唯一的 `x-acs-request-id` 。 响应中会返回相同的 requestId，便于日志追踪和问题排查。
2. .** **错误处理**
检查响应中的 `code` 字段判断请求是否成功。 `code=200` 表示成功，其他值表示失败。 错误信息通过 `msg` 字段获取。
3. .** **分页查询**
列表接口使用分页参数避免数据量过大。 通过 `total` 字段获取总记录数。 通过 `records` 字段获取当前页数据。
4. .** **实例区分**
操作前确认 `gwInstanceId` 对应的网关类型。 通过 `/gatewayInstance/getInstance` 查询实例详情确认类型。

#### API 调用-集群管理

**概述**

集群管理模块提供Kubernetes集群的导入、查询、更新等功能。集群是网关实例的部署环境，支持自建 Kubernetes和容器服务Kubernetes两种类型。
**适用引擎**：SCG / Higress
**API****路径前缀**： `/k8s`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**导入集群**

**接口说明**

导入一个Kubernetes集群到网关控制台。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/importCluster |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 ImportK8sClusterRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| k8sClusterName | String | 是 | 集群名称，长度为2-128 字符，以英文字母开头。 |

| k8sClusterType | String | 否 | 集群类型： self-built：自建K8s container-service： 容器服务K8s |
|---|---|---|---|
| configContent | String | 条件必填 | KubeConfig配置内容。 说明自建集群时必填。 |
| k8sClusterAttribute | Object | 条件必填 | 集群扩展属性。 说明容器服务集群时必填。 |

**k8sClusterAttribute 结构**

| 参数名 | 类型 | 必填 |  | 说明 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| csClusterId | String | 条件必填 |  | 容器服务集群ID。 说明 container- service 类型时必填。 |  |  |  |  |
|  |  |  |  |  |  | container- |  |  |
|  |  |  |  |  | service |  |  |  |

**查询集群列表**

**接口说明**

分页查询Kubernetes集群列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/listClusters |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 ListK8sClusterRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| clusterName | String | 否 | 集群名称（模糊搜索）。 |

**查询全部集群**

**接口说明**

查询所有Kubernetes集群列表（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/getClusterList |
| Method | POST |
| Content-Type | application/json |

**请求参数**

无需请求参数。

**更新集群**

**接口说明**

更新Kubernetes集群信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/updateCluster |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 UpdateK8sClusterRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clusterCode | String | 是 | 集群编码。 |
| k8sClusterAttribute | String | 是 | 集群扩展属性（JSON字符串）。 |

**取消导入集群**

**接口说明**

取消导入Kubernetes集群。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/cancelImportCluster |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 CancelImportK8sClusterRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| k8sClusterCode | String | 是 | 集群编码。 |

**测试集群连接**

**接口说明**

测试Kubernetes集群连接是否正常。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/checkConnectCluster |

| Method | POST |
|---|---|
| Content-Type | application/json |

**请求参数（基于 CheckK8sClusterConnectRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clusterCode | String | 是 | 集群编码。 |

**查询集群名称**

**接口说明**

根据集群编码查询集群名称。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/getK8sClusterName |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clusterCode | String | 是 | 集群编码。 |

**查询实例关联集群信息**

**接口说明**

根据实例ID查询关联的Kubernetes集群信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /k8s/getK8sClusterInfoByGwInstanceId |

| Method | POST |
|---|---|
| Content-Type | application/json |

**请求参数（基于 GetK8sClusterInfoRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用集群管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class ClusterApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 导入自建`K8s`集群 `==========`

```
        String clusterCode = importSelfBuiltCluster(client);
```

`// ==========` 导入容器服务`K8s`集群 `==========`

```
        // String csClusterCode = importContainerServiceCluster(client);
```

`// ==========` 测试集群连接 `==========`

```
checkConnect(client clusterCode);
```

```
        checkConnect(client, clusterCode);
```

`// ==========` 查询集群列表 `==========`

```
        listClusters(client);
```

`// ==========` 查询全部集群 `==========`

```
        getClusterList(client);
```

`// ==========` 查询集群名称 `==========`

```
        getK8sClusterName(client, clusterCode);
```

`// ==========` 取消导入集群 `==========`

```java
        // cancelImportCluster(client, clusterCode);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 导入自建`Kubernetes`集群（基于 `ImportK8sClusterRequest`）
`*/`

```java
    private static String importSelfBuiltCluster(IAcsClient client) throws Exception {
```

p g p

```
(
```

) p

```
{
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-self-built-cluster");         // 【必填】集群名
```

称

```
        request.put("k8sClusterType", "self-built");                    // 【可选】集群类型
：self-built
        request.put("configContent", "your-kubeconfig-content");        // 【必填】KubeCo
```

`nfig`配置

```java
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importSelfBuiltCluster success, clusterCode: " +
clusterCode);
            return clusterCode;
        } else {
            System.out.println("importSelfBuiltCluster failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 导入容器服务`Kubernetes`集群（基于 `ImportK8sClusterRequest`）
`*/`

```java
    private static String importContainerServiceCluster(IAcsClient client) throws Excep
tion {
        Map<String, Object> attribute = new HashMap<>();
        attribute.put("csClusterId", "ce********b5587f5ec1c");  // 【必填】容器服务集群ID
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-cs-cluster");                  // 【必填】集群名
```

称

```
        request.put("k8sClusterType", "container-service");              // 【必填】集群类
型：container-service
        request.put("k8sClusterAttribute", attribute);                   // 【必填】集群扩
```

展属性

```
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
```

```java
            System.out.println("importContainerServiceCluster success, clusterCode: " +
clusterCode);
            return clusterCode;
        } else {
            System.out.println("importContainerServiceCluster failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询集群列表（基于 `ListK8sClusterRequest`）
`*/`

```java
    private static void listClusters(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);                                       // 【必填】当前页码
        request.put("size", 10);                                         // 【必填】每页条数
        // request.put("clusterName", "");                                  // 【可选】集群
```

名称（模糊搜索）

```
        CommonRequest commonRequest = createBaseRequest("/k8s/listClusters");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询全部集群
`*/`

```java
    private static void getClusterList(IAcsClient client) throws Exception {
        CommonRequest commonRequest = createBaseRequest("/k8s/getClusterList");
        commonRequest.setHttpContent(new byte[0], "UTF-8", FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getClusterList: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 测试集群连接（基于 `CheckK8sClusterConnectRequest`）
`*/`

```java
    private static void checkConnect(IAcsClient client, String clusterCode) throws Exce
ption {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编
```

码

```
        CommonRequest commonRequest = createBaseRequest("/k8s/checkConnectCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getK8sClusterName(IAcsClient client, String clusterCode) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编
```

码

```
        CommonRequest commonRequest = createBaseRequest("/k8s/getK8sClusterName");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询实例关联集群信息（基于 `GetK8sClusterInfoRequest`）
`*/`

```java
    private static void getK8sClusterInfoByGwInstanceId(IAcsClient client, String gwIns
tanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】网关实
```

例`ID`

```java
        CommonRequest commonRequest =
createBaseRequest("/k8s/getK8sClusterInfoByGwInstanceId");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getK8sClusterInfoByGwInstanceId: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 更新集群（基于 `UpdateK8sClusterRequest`）
`*/`

```java
    private static void updateCluster(IAcsClient client, String clusterCode) throws Exc
eption {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编
```

码

```
        request.put("k8sClusterAttribute", "{\"key\":\"value\"}");       // 【必填】集群扩
```

展属性`JSON`

```
        CommonRequest commonRequest = createBaseRequest("/k8s/updateCluster");
```

R t

```
tHttC
```

t

```
t(JSONObj ttJSONBt (
```

`t)`

```
"UTF8"
```

```
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 取消导入集群（基于 `CancelImportK8sClusterRequest`）
`*/`

```java
    private static void cancelImportCluster(IAcsClient client, String clusterCode) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterCode", clusterCode);                      // 【必填】集群编
```

码

```
        CommonRequest commonRequest = createBaseRequest("/k8s/cancelImportCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**集群类型说明**

| k8sClusterType | 说明 |
|---|---|
| self-built | 自建 Kubernetes 集群，需提供 KubeConfig。 |
| container-service | 容器服务 Kubernetes 集群，需提供集群ID。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误. |

#### API 调用-来源管理

**概述**

来源管理模块提供服务注册中心的增删改查功能。来源用于服务发现，SCG支持Nacos、微服务空间 (EDAS)、Eureka、Database四种来源类型。
**API****路径前缀**： `/source`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建来源**

**接口说明**

创建一个服务注册中心来源。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /source/createSource |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| sourceName | String | 是 | 来源名称。 |
| sourceType | Integer | 是 | 来源类型： 1：Nacos 2：微服务空间 （EDAS） 3：Eureka 5：Database |

| description | String | 否 | 来源描述。 |
|---|---|---|---|
| sourceStruct | Object | 是 | 来源配置结构。 说明不同的来源类型配置结构不同。 |

**不同来源类型的 sourceStruct 配置**

**Nacos（sourceType=1）：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| nacosRegistry | String | 是 | Nacos注册中心地址。 |
| nacosNamespaceId | String | 是 | Nacos命名空间ID。 |
| nacosGroupName | String | 否 | Nacos分组名，默认为 DEFAULT GROUP。 _ |
| nacosAccessKey | String | 否 | Nacos认证AccessKey。 |
| nacosSecretKey | String | 否 | Nacos认证SecretKey。 |
| checkType | Integer | 否 | 校验类型： 0：不校验 1：校验连接 |

**微服务空间/EDAS（sourceType=2）：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| edasNameSpaceId | String | 是 | EDAS命名空间ID。 |
| type | Integer | 是 | 类型： 0：Nacos（DNCS） 1： ConfigServer（DNCS） |

| edasEndPoint | String | 条件必填 | EDAS Endpoint。 说明地址服务器模式时必填。 |
|---|---|---|---|
| edasServerAddr | String | 条件必填 | EDAS服务器地址。 说明直连模式时必填。 |
| edasAccessKey | String | 是 | EDAS AccessKey。 |
| edasSecretKey | String | 是 | EDAS SecretKey。 |

**Eureka（sourceType=3）：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| eurekaRegistry | String | 是 | Eureka注册中心地址。 |
| checkType | Integer | 否 | 校验类型： 0：不校验 1：校验连接 |

**Database（sourceType=5）：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| databaseType | Integer | 是 | 数据库类型： 0：MySQL 1：PostgreSQL |
| jdbcUrl | String | 是 | JDBC连接地址。 |
| username | String | 是 | 数据库用户名。 |
| password | String | 是 | 数据库密码。 |

| maxConnection | Integer | 否 | 最大连接数。 |
|---|---|---|---|
| maxIdleConnection | Integer | 否 | 最大空闲连接数。 |
| connectionIdleTime | Integer | 否 | 连接空闲时间（秒）。 |

**查询来源列表**

**接口说明**

分页查询来源列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /source/listSources |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| sourceName | String | 否 | 来源名称（模糊搜索）。 |
| sourceType | Integer | 否 | 来源类型筛选。 |

**查询来源详情**

**接口说明**

根据来源ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /source/getSource |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| sourceId | String | 是 | 来源ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改来源**

**接口说明**

修改已存在的来源配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /source/modifySource |
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建来源参数相同，额外需要指定 `sourceId` 。

**删除来源**

**接口说明**

删除指定的来源。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /source/deleteSource |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| sourceId | String | 是 | 来源ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用来源管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class SourceApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
```

```
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== 创建Nacos来源 ==========
        String nacosSourceId = createNacosSource(client);
```

`// ==========` 创建微服务空间来源 `==========`

```
        // String edasSourceId = createEdasSource(client);
        // ========== 创建Eureka来源 ==========
        // String eurekaSourceId = createEurekaSource(client);
        // ========== 创建Database来源 ==========
        // String dbSourceId = createDatabaseSource(client);
```

`// ==========` 查询来源列表 `==========`

```
        listSources(client);
```

`// ==========` 查询来源详情 `==========`

```java
        getSource(client, nacosSourceId);
        // ========== 修改来源 ==========
        modifySource(client, nacosSourceId);
        // ========== 删除来源 ==========
        deleteSource(client, nacosSourceId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
```

```
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建`Nacos`来源
`*/`

```java
    private static String createNacosSource(IAcsClient client) throws Exception {
```

`// Nacos`配置结构

```
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");       // 【必填】N
```

`acos`注册中心地址

```
        sourceStruct.put("nacosNamespaceId", "public");                      // 【必填】Na
```

`cos`命名空间`ID`

```
        sourceStruct.put("nacosGroupName", "DEFAULT_GROUP");                 // 【可选】N
```

`acos`分组名

```
        // sourceStruct.put("nacosAccessKey", "");                             // 【可选】
Nacos认证AccessKey
        // sourceStruct.put("nacosSecretKey", "");                             // 【可选】
Nacos认证SecretKey
        sourceStruct.put("checkType", 0);                                    // 【可选】校
```

验类型：`0-`不校验

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("sourceName", "my-nacos-source");                       // 【必填】来
```

源名称

```
        request.put("sourceType", 1);                                       // 【必填】来源
```

类型：`1-NACOS`

```
        request.put("sourceStruct", sourceStruct);                          // 【必填】来
```

源配置结构

```
        request.put("description", "Nacos service registry");               // 【可选】来
```

源描述

```java
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createNacosSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
Systemoutprintln("createNacosSourcefailed:"+resultgetString("msg"));
```

```java
            System.out.println("createNacosSource failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建微服务空间`(EDAS)`来源
`*/`

```java
    private static String createEdasSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("edasNameSpaceId", "edas-ns-xxx");                  // 【必
```

填】`EDAS`命名空间`ID`

```
        sourceStruct.put("type", 0);                                         // 【必填】类
型：0-Nacos(DNCS), 1-ConfigServer(DNCS)
        sourceStruct.put("edasEndPoint", "edas-endpoint.aliyuncs.com");      // 【条件必
填】EDAS Endpoint
        sourceStruct.put("edasServerAddr", "edas-server_addr");              // 【条件必填
```

】`EDAS`服务器地址

```
        sourceStruct.put("edasAccessKey", "your-edas-ak");                   // 【必
填】EDAS AccessKey
        sourceStruct.put("edasSecretKey", "your-edas-sk");                   // 【必
填】EDAS SecretKey
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-edas-source");
        request.put("sourceType", 2);                                       // 【必填】来源
```

类型：`2-`微服务空间`(EDAS)`

```java
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEdasSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEdasSource failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`Eureka`来源
`*/`

```java
    private static String createEurekaSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("eurekaRegistry", "http://eureka-server:8761/eureka/");  // 【
```

必填】`Eureka`注册中心地址必填】`Eureka`注册中心地址

```
        sourceStruct.put("checkType", 0);                                    // 【可选】校
```

验类型

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-eureka-source");
        request.put("sourceType", 3);                                       // 【必填】来源
```

类型：`3-Eureka`

```java
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createEurekaSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createEurekaSource failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`Database`来源
`*/`

```java
    private static String createDatabaseSource(IAcsClient client) throws Exception {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("databaseType", 0);                                 // 【必填】数
```

据库类型：`0-MySQL, 1-PostgreSQL`

```
        sourceStruct.put("jdbcUrl", "jdbc:mysql://mysql-server:3306/mydb");  // 【必填】J
```

`DBC`连接地址

```
        sourceStruct.put("username", "db_user");                             // 【必填】数
```

据库用户名

```
        sourceStruct.put("password", "db_password");                         // 【必填】数
```

据库密码

```
        // sourceStruct.put("maxConnection", 100);                             // 【可选】
```

最大连接数

```
        // sourceStruct.put("maxIdleConnection", 20);                          // 【可选】
```

最大空闲连接数

```
        // sourceStruct.put("connectionIdleTime", 300);                        // 【可选】
```

连接空闲时间（秒）

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("sourceName", "my-database-source");
        request.put("sourceType", 5);                                       // 【必填】来源
```

类型：`5-Database`

```java
        request.put("sourceStruct", sourceStruct);
        CommonRequest commonRequest = createBaseRequest("/source/createSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String sourceId = result.getString("data");
            System.out.println("createDatabaseSource success, sourceId: " + sourceId);
            return sourceId;
        } else {
            System.out.println("createDatabaseSource failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询来源列表
`*/`

```java
    private static void listSources(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("sourceName", "");                                     // 【可选】来
```

源名称（模糊搜索）

```
        // request.put("sourceType", 1);                                      // 【可选】来
```

源类型筛选

```
        CommonRequest commonRequest = createBaseRequest("/source/listSources");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询来源详情
`*/`

```java
    private static void getSource(IAcsClient client, String sourceId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【必填】来源
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/source/getSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改来源
`*/`

```java
    private static void modifySource(IAcsClient client, String sourceId) throws Excepti
on {
        Map<String, Object> sourceStruct = new HashMap<>();
        sourceStruct.put("nacosRegistry", "http://nacos-server:8848");
        sourceStruct.put("nacosNamespaceId", "public");
        sourceStruct.put("checkType", 0);
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【必填】来源
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("sourceName", "my-nacos-source-modified");              // 【必填】来
```

源名称

```
        request.put("sourceType", 1);                                       // 【必填】来源
```

类型

```
        request.put("sourceStruct", sourceStruct);                          // 【必填】来
```

源配置结构

```
        CommonRequest commonRequest = createBaseRequest("/source/modifySource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除来源
`*/`

```java
    private static void deleteSource(IAcsClient client, String sourceId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("sourceId", sourceId);                                  // 【必填】来源
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/source/deleteSource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**来源类型说明（SCG）**

| sourceType | 类型名称 | 说明 |
|---|---|---|
| 1 | Nacos | Nacos注册中心。 |
| 2 | 微服务空间(EDAS) | EDAS微服务空间。 |
| 3 | Eureka | Eureka注册中心。 |
| 5 | Database | 数据库来源 （MySQL/PostgreSQL）。 |

**数据库类型说明**

| databaseType | 类型名称 | 说明 |
|---|---|---|
| 0 | MySQL | MySQL数据库。 |
| 1 | PostgreSQL | PostgreSQL数据库。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-服务管理

**概述**

服务管理模块提供后端服务的增删改查功能。服务是路由转发的目标，可以是固定节点、服务发现或导入的服务。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/microservice/**`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建服务**

**接口说明**

创建一个新的后端服务。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/createService |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 CreateMicroserviceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| name | String | 是 | 服务名称（网关中的标识）。 |
| upstreamType | Integer | 是 | 上游类型： 1：固定节点 2：服务发现 3：服务导入 |

| loadBalanceType | Integer | 是 | 负载均衡类型（见下方说明）。 |
|---|---|---|---|
| protocol | String | 是 | 协议： HTTP GRPC Webservice、 Dubbo、 HSF |
| serviceStruct | Object | 是 | 服务结构配置（见下方详细说明）。 |
| serviceType | Integer | 否 | 服务类型： 0：RPC服务 1：数据库说明默认为0。 |
| description | String | 否 | 服务描述。 |
| serviceName | String | 条件必填 | 注册中心服务名。 说明服务发现时使用。 |
| serviceSourceType | Integer | 条件必填 | 来源类型。 说明服务发现时使用。 |
| isOpenHealthCheck | Boolean | 否 | 是否开启健康检查。 |
| healthCheckStruct | HealthCheckStruct | 否 | 健康检查配置（SCG）。 |
| activeHealthCheckStru ct | ActiveHealthCheckStru ct | 否 | 主动健康检查配置 （Higress）。 |

| proxyServerName | String | 否 | 代理服务器名称。 |
|---|---|---|---|
| isDisasterRecovery | Boolean | 否 | 是否为容灾服务，默认为 false。 |

**负载均衡类型说明（基于 LoadBalanceTypeEnum）**

| 值 | 类型名称 | 说明 | 适用场景 |
|---|---|---|---|
| 1 | WEIGHT ROUND ROBI _ _ N | 加权轮询。 | 仅固定节点 |
| 2 | WEIGHT RANDOM _ | 加权随机。 | 仅固定节点 |
| 3 | ROUND ROBIN _ | 轮询。 | 通用 |
| 4 | RANDOM | 随机。 | 通用 |
| 5 | LEAST REQUEST _ | 最少请求。 | Higress Nacos |
| 6 | CONSISTENT HASH _ | 一致性哈希。 | Higress Nacos |
| 7 | LEAST CONN _ | 最少连接。 | Higress Nacos |

**serviceStruct 配置说明**

**固定节点（upstreamType=1）：**

```json
{
    "nodes": [
        {
```

`"ip": "192***.*.100", //` 【必填】节点`IP`地址 `"port": 8080, //` 【必填】端口 `"weight": 100, //` 【可选】权重，默认`100` `"enable": true //` 【可选】是否启用，默认`true`

```
        }
```

]

```
}
```

**Nacos服务发现（upstreamType=2）：**

```
{
```

`"nacosNamespaceId": "public", //` 【必填】`Nacos`命名空间`ID`

```json
    "nacosGroupName": "DEFAULT_GROUP"  // 【可选】Nacos分组名
}
```

**HealthCheckStruct 结构（SCG健康检查）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| type | int | 是 | 检查类型。 |
| healthPath | String | 是 | 检查路径。 |
| httpStatuses | String | 是 | 健康状态码，如“200、 301”。 |
| timeout | int | 是 | 请求超时（秒）。 |
| healthInterval | int | 是 | 健康检查间隔（秒）。 |
| unHealthInterval | int | 是 | 不健康检查间隔（秒）。 |
| httpSuccesses | int | 是 | 成功阈值。 |
| httpFailures | int | 是 | 失败阈值。 |

**ActiveHealthCheckStruct 结构（Higress主动健康检查）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enable | Boolean | 是 | 是否启用。 |
| protocol | String | 是 | 协议： http tcp |
| timeout | Integer | 是 | 超时时间（秒）。 |
| interval | Integer | 是 | 检查间隔（秒）。 |
| healthyThreshold | Integer | 是 | 健康阈值。 |
| unhealthyThreshold | Integer | 是 | 不健康阈值。 |

| httpPath | String | 条件必填 | HTTP检查路径。 说明 protocol=http 时配置。 |
|---|---|---|---|
| httpHost | String | 否 | HTTP检查Host。 |
| expectedStatuses | List | 条件必填 | 预期状态码，如 ["200","301"]。 |

|  |  |  | protocol=http |
|---|---|---|---|

**查询服务列表**

**接口说明**

分页查询服务列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/listServices |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 GatewayServiceListByPageRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| serviceName | String | 否 | 服务名称（模糊搜索）。 |

| serviceId | String | 否 | 服务ID（精确搜索）。 |
|---|---|---|---|
| sourceName | String | 否 | 来源名称。 |
| isDisasterRecovery | Boolean | 否 | 是否容灾服务筛选。 |
| sourceTypeList | List | 否 | 来源类型列表。 |
| provider | String | 否 | AI网关提供商。 |

**查询服务详情**

**接口说明**

根据服务ID查询服务详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/getService |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serviceId | String | 是 | 服务ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改服务**

**接口说明**

修改已存在的服务配置。

**请求信息**

| 项目 | 内容 |
|---|---|

| URL | /microservice/modifyService |
|---|---|
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建服务参数相同，额外需要指定 `serviceId` 。

**修改服务节点**

**接口说明**

单独修改服务的节点配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/modifyNode |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 UpdateNodeRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serviceId | String | 是 | 服务ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |
| nodes | List | 是 | 节点列表。 |

**删除服务**

**接口说明**

删除指定的服务。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/deleteService |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serviceId | String | 是 | 服务ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**批量删除服务**

**接口说明**

批量删除多个服务。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/batchDeleteService |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serviceIds | List | 是 | 服务ID列表。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**查询所有服务**

**接口说明**

查询网关实例下的所有服务（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /microservice/listAllServices |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| serviceType | Integer | 否 | 服务类型筛选。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用服务管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class ServiceApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========` `//` 自建`ACK`环境配置是自建

```java
    private static final boolean IS_SELF_HOSTED = true;                     // 是否自建
```

`ACK`环境

```java
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // 自建ACK控
```

制台地址 `//` 企业版环境配置（当 `IS_SELF_HOSTED = false` 时使用）

```java
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
```

`//` 网关实例`ID`

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 创建固定节点服务 `==========`

```
        String serviceId = createFixedNodeService(client);
```

`// ==========` 创建`Nacos`服务发现服务 `==========`

```
        // String nacosServiceId = createNacosService(client);
```

`// ==========` 查询服务列表 `==========`

```
        listServices(client);
```

`// ==========` 查询服务详情 `==========`

```
        getService(client, serviceId);
        // ========== 修改服务 ==========
        modifyService(client, serviceId);
        // ========== 删除服务 ==========
        deleteService(client, serviceId);
    }
    /**
```

* 创建客户端（自建`ACK`和企业版通用）
`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
```

i t

```
tti
```

`id`

```
tAthH
```

d

```
(C
```

R t

```
t){
```

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建固定节点服务
`*/`

```java
    private static String createFixedNodeService(IAcsClient client) throws Exception {
```

`//` 节点配置（基于 `Node` 结构）

```
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.100");                                    // 【必填】节点
```

`IP`地址

```
        node.put("port", 8080);                                             // 【必填】端口
        node.put("weight", 100);                                            // 【可选】权重
```

，默认`100`

```
        node.put("enable", true);                                           // 【可选】是否
```

启用，默认`true` `//` 服务结构配置

```
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
```

`//` 创建请求（基于 `CreateMicroserviceRequest`）

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "service-demo-01");                             // 【必填】服务
```

名称（网关中标识）

```
        request.put("upstreamType", 1);                                     // 【必填】上游
```

类型：`1-`固定节点

```
        request.put("loadBalanceType", 3);                                  // 【必填】负载
```

均衡类型：`3-`轮询

```
        request.put("protocol", "HTTP");                                    // 【必填】协议
        request.put("serviceStruct", serviceStruct);                        // 【必填】服
```

务结构配置

```
        request.put("serviceType", 0);                                      // 【可选】服务
```

类型：`0-RPC`服务 `//`【可选】服

```
requestput("description" "demobackendservice");
```

```
        request.put(description, demo backend service);                 // 【可选】服
```

务描述

```
        request.put("isOpenHealthCheck", false);                            // 【可选】是否
```

开启健康检查

```java
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createFixedNodeService success, serviceId: " +
serviceId);
            return serviceId;
        } else {
            System.out.println("createFixedNodeService failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`Nacos`服务发现服务
`*/`

```java
    private static String createNacosService(IAcsClient client) throws Exception {
```

`// Nacos`服务结构配置

```
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nacosNamespaceId", "public");                    // 【必填】Nac
```

`os`命名空间`ID`

```
        serviceStruct.put("nacosGroupName", "DEFAULT_GROUP");               // 【可选】Na
```

`cos`分组名 `//` 创建请求

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "service-nacos-demo");                          // 【必填】服
```

务名称

```
        request.put("upstreamType", 2);                                     // 【必填】上游
```

类型：`2-`服务发现

```
        request.put("loadBalanceType", 3);                                  // 【必填】负载
```

均衡类型

```
        request.put("protocol", "HTTP");                                    // 【必填】协议
        request.put("serviceName", "user-service");                         // 【必填】注
```

册中心服务名

```
        request.put("serviceSourceType", 1);                                // 【必填】来源
```

类型：`1-NACOS`

```
        request.put("sourceId", "nacos-source-id");                         // 【必填】来
```

源`ID`

```
        request.put("serviceStruct", serviceStruct);                        // 【必填】服
```

务结构配置务结构配置

```java
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createNacosService success, serviceId: " + serviceId);
            return serviceId;
        } else {
            System.out.println("createNacosService failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建带健康检查的服务
`*/`

```java
    private static String createServiceWithHealthCheck(IAcsClient client) throws Except
ion {
```

`//` 节点配置

```
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.168.1.100");
        node.put("port", 8080);
        node.put("weight", 100);
        node.put("enable", true);
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
```

`// SCG`健康检查配置（基于 `HealthCheckStruct`）

```
        Map<String, Object> healthCheckStruct = new HashMap<>();
        healthCheckStruct.put("type", 0);                                   // 【必填】检查
```

类型

```
        healthCheckStruct.put("healthPath", "/health");                     // 【必填】检
```

查路径

```
        healthCheckStruct.put("httpStatuses", "200,301");                   // 【必填】健
```

康状态码

```
        healthCheckStruct.put("timeout", 5);                                // 【必填】请求
```

超时（秒）

```
        healthCheckStruct.put("healthInterval", 30);                        // 【必填】健
```

康检查间隔（秒）

```
        healthCheckStruct.put("unHealthInterval", 60);                      // 【必填】不
```

健康检查间隔（秒）

```
        healthCheckStruct.put("httpSuccesses", 3);                          // 【必填】成
```

功阈值

```
        healthCheckStruct.put("httpFailures", 3);                           // 【必填】失
```

败阈值 `// Higress`主动健康检查配置（基于 `ActiveHealthCheckStruct`）

```
        // Map<String, Object> activeHealthCheckStruct = new HashMap<>();
        // activeHealthCheckStruct.put("enable", true);                       // 【必填】
```

是否启用

```
        // activeHealthCheckStruct.put("protocol", "http");                   // 【必填】
```

协议

```
        // activeHealthCheckStruct.put("timeout", 5);                         // 【必填】
```

超时时间（秒）

```
        // activeHealthCheckStruct.put("interval", 30);                       // 【必填】
```

检查间隔（秒）

```
        // activeHealthCheckStruct.put("healthyThreshold", 3);                // 【必填】
```

健康阈值

```
        // activeHealthCheckStruct.put("unhealthyThreshold", 3);              // 【必填】
```

不健康阈值

```
        // activeHealthCheckStruct.put("httpPath", "/health");                // 【必填】
```

`HTTP`检查路径

```
        // activeHealthCheckStruct.put("expectedStatuses", Arrays.asList("200",
```

"301")); // 【必填】预期状态码

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("name", "service-health-check");
        request.put("upstreamType", 1);
        request.put("loadBalanceType", 3);
        request.put("protocol", "HTTP");
        request.put("serviceStruct", serviceStruct);
        request.put("isOpenHealthCheck", true);                             // 【必填】开启
```

健康检查

```
        request.put("healthCheckStruct", healthCheckStruct);                // 【必填】健
```

康检查配置

```java
        CommonRequest commonRequest = createBaseRequest("/microservice/createService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String serviceId = result.getString("data");
            System.out.println("createServiceWithHealthCheck success, serviceId: " +
serviceId);
            return serviceId;
        } else {
            System.out.println("createServiceWithHealthCheck failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询服务列表（基于 `GatewayServiceListByPageRequest`）
`*/`

```java
    private static void listServices(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("serviceName", "");                                    // 【可选】服
```

务名称（模糊搜索）

```
        // request.put("serviceId", "");                                      // 【可选】服
```

务`ID`（精确搜索）

```
        // request.put("isDisasterRecovery", false);                          // 【可选】
```

是否容灾服务筛选

```
        CommonRequest commonRequest = createBaseRequest("/microservice/listServices");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询服务详情
`*/`

```java
    private static void getService(IAcsClient client, String serviceId) throws Exceptio
n {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // 【必填】服务
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/microservice/getService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改服务
`*/`

```java
    private static void modifyService(IAcsClient client, String serviceId) throws Excep
tion {
        Map<String, Object> node = new HashMap<>();
        node.put("ip", "192.***.*.101");
        node.put("port", 8081);
        node.put("weight", 100);
        node.put("enable", true);
```

```
        Map<String, Object> serviceStruct = new HashMap<>();
        serviceStruct.put("nodes", Arrays.asList(node));
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // 【必填】要修
```

改的服务`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "service-demo-modified");                       // 【必填】服
```

务名称

```
        request.put("upstreamType", 1);                                     // 【必填】上游
```

类型

```
        request.put("loadBalanceType", 1);                                  // 【必填】负载
```

均衡类型

```
        request.put("protocol", "HTTP");                                    // 【必填】协议
        request.put("serviceStruct", serviceStruct);                        // 【必填】服
```

务结构配置

```
        CommonRequest commonRequest = createBaseRequest("/microservice/modifyService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除服务
`*/`

```java
    private static void deleteService(IAcsClient client, String serviceId) throws Excep
tion {
        Map<String, Object> request = new HashMap<>();
        request.put("serviceId", serviceId);                                // 【必填】服务
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/microservice/deleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 批量删除服务
`*/`

```java
    private static void batchDeleteServices(IAcsClient client, List<String> serviceIds)
throws Exception {
        Map<String, Object> request = new HashMap<>();
```

`//`【必填】服务

```
requestput("serviceIds" serviceIds);
```

```
        request.put(serviceIds, serviceIds);                              // 【必填】服务
```

`ID`列表

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest =
createBaseRequest("/microservice/batchDeleteService");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**上游类型说明**

| upstreamType | 说明 | 配置方式 |
|---|---|---|
| 1 | 固定节点 | 在 serviceStruct.nodes 中配置IP/端口/权重。 |
| 2 | 服务发现 | 通过 serviceName 指定注册中心服务名，需配置 sourceId 。 |
| 3 | 服务导入 | 从已有来源导入服务。 |

**协议类型说明**

| protocol | 说明 |
|---|---|
| HTTP | HTTP/HTTPS 协议。 |
| GRPC | gRPC 协议。 |
| Webservice | WebService 协议。 |
| Dubbo | Dubbo RPC 协议。 |
| HSF | HSF RPC 协议。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-实例管理

**概述**

实例管理模块提供网关实例的增删改查功能。实例是网关的运行实体，可在Kubernetes集群上部署，支持 SCG和Higress两种引擎类型。
**适用引擎**：SCG / Higress
**API****路径前缀**： `/gatewayInstance`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建实例**

**接口说明**

创建一个新的网关实例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/createInstance |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 CreateGwInstanceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceName | String | 是 | 实例名称，长度为2-128 字符，以英文字母开头。 |
| clusterCode | String | 是 | 集群编码。 |
| namespace | String | 是 | Kubernetes命名空间。 |
| brokerEngineType | String | 否 | 引擎类型： SCG HIGRESS SHARED SCG _ CLOUD NATIVE GAT _ _ EWAY |
| deployMode | String | 否 | 部署模式：adp、edas、 tiangong、custom、 k8s等。 |
| instanceClass | String | 否 | 实例规格。 |
| instanceNumber | String | 否 | 实例节点数。 |
| vpcId | String | 否 | VPC ID。 |
| vswId | String | 否 | 虚拟交换机ID。 |
| ingressName | String | 否 | Ingress名称。 |
| deployConfigContent | String | 否 | 自定义部署配置。 |
| accessModeConfigCon tent | String | 否 | 访问模式配置。 |

**查询实例列表**

**接口说明**

分页查询网关实例列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/listInstances |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 ListGwInstancesRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| name | String | 否 | 实例名称（模糊搜索）。 |
| gwInstanceId | String | 否 | 实例ID筛选。 |
| deployMode | String | 否 | 部署模式筛选。 |
| status | Integer | 否 | 实例状态筛选。 |
| brokerEngineType | String | 否 | 引擎类型筛选。 |

**查询全部实例**

**接口说明**

查询当前所有网关实例列表（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/listAllInstances |
| Method | POST |

| Content-Type | application/json |
|---|---|

**请求参数**

无需请求参数。

**查询实例详情**

**接口说明**

根据实例ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/getInstanceInfo |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |

**修改实例**

**接口说明**

修改实例名称。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/modifyInstance |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |
| instanceName | String | 是 | 新的实例名称。 |

**删除实例**

**接口说明**

删除指定的网关实例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/deleteInstance |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 DeleteGwInstanceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |

**重启实例**

**接口说明**

重启指定的网关实例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/restartInstance |
| Method | POST |

| Content-Type | application/json |
|---|---|

**请求参数（基于 RestartGwInstanceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID |

**停止实例**

**接口说明**

停止指定的网关实例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/stopInstance |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |

**升级实例**

**接口说明**

升级实例到最新版本。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/upgradeInstance |
| Method | POST |

| Content-Type | application/json |
|---|---|

**请求参数（基于 UpgradeGwInstanceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |

**修改实例资源**

**接口说明**

实例扩容或缩容，修改实例规格与节点数。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/modifyResource |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |
| instanceClass | String | 否 | 实例规格。 |
| instanceNumber | Integer | 否 | 实例节点数。 |
| specificationTemplate | Integer | 否 | 规格模板。 |

**查询实例资源**

**接口说明**

查询实例规格与节点信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/getResource |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 GetInstanceResourceRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用实例管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class InstanceApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== 创建实例 ==========
        String instanceId = createInstance(client);
```

`// ==========` 查询实例列表 `==========`

```
        listInstances(client);
```

`// ==========` 查询实例详情 `==========`

```
        getInstanceInfo(client, instanceId);
```

`// ==========` 修改实例名称 `==========`

```
        modifyInstance(client, instanceId);
```

`// ==========` 查询实例资源 `==========`

```java
        getResource(client, instanceId);
        // ========== 删除实例 ==========
        // deleteInstance(client, instanceId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建实例（基于 `CreateGwInstanceRequest`）
`*/`

```java
    private static String createInstance(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceName", "my-gateway-instance");            // 【必填】实例名
```

称

```
        request.put("clusterCode", "cluster-code-xxx");                  // 【必填】集群编
```

码

```
        request.put("namespace", "default");                             // 【必填】K8s命名
```

空间

```
        request.put("brokerEngineType", "SCG");                          // 【可选】引擎类
```

型：`SCG/HIGRESS`

```
        // request.put("deployMode", "adp");                                // 【可选】部署
```

模式

```
        // request.put("instanceClass", "standard");                        // 【可选】实
```

例规格

```
        // request.put("instanceNumber", "2");                              // 【可选】节点
```

数

```java
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/createInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String instanceId = result.getString("data");
            System.out.println("createInstance success, instanceId: " + instanceId);
            return instanceId;
        } else {
            System.out.println("createInstance failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询实例列表（基于 `ListGwInstancesRequest`）
`*/`

```java
    private static void listInstances(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("current", 1);                                       // 【必填】当前页码
        request.put("size", 10);                                         // 【必填】每页条数
        // request.put("name", "");                                         // 【可选】实例
```

名称（模糊搜索）

```
        // request.put("brokerEngineType", "SCG");                          // 【可选】引
```

擎类型筛选

```
        // request.put("status", 2);                                        // 【可选】状态
```

筛选：`2-running`

```
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/listInstances");
```

```
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getInstanceInfo(IAcsClient client, String gwInstanceId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/getInstanceInfo");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void modifyInstance(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        request.put("instanceName", "modified-instance-name");           // 【必填】新实例
```

名称

```
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/modifyInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询实例资源（基于 `GetInstanceResourceRequest`）
`*/`

```java
    private static void getResource(IAcsClient client, String gwInstanceId) throws Exce
ption {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
CommonReqestcommonReqest
```

```
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/getResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void modifyResource(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        request.put("instanceClass", "large");                           // 【可选】实例规
```

格

```
        request.put("instanceNumber", 3);                                // 【可选】节点数
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/modifyResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 重启实例（基于 `RestartGwInstanceRequest`）
`*/`

```java
    private static void restartInstance(IAcsClient client, String gwInstanceId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/restartInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void stopInstance(IAcsClient client, String gwInstanceId) throws Exc
eption { Map<String,Object>request=newHashMap<>();
```

```
        Map<String, Object> request  new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/stopInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除实例（基于 `DeleteGwInstanceRequest`）
`*/`

```java
    private static void deleteInstance(IAcsClient client, String gwInstanceId) throws E
xception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest =
createBaseRequest("/gatewayInstance/deleteInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**实例状态说明**

| status | 状态名称 | 说明 |
|---|---|---|
| 0 | starting | 实例启动中。 |
| 1 | error | 实例异常。 |
| 2 | running | 实例运行中。 |
| 3 | unknown | 状态未知。 |
| 4 | stopped | 实例已停止。 |
| 5 | wait deploy _ | 等待部署。 |

| 6 | updating | 更新中（升级/扩缩容）。 |
|---|---|---|
| 7 | stopping | 实例停止中。 |

**引擎类型说明**

| brokerEngineType | 说明 |
|---|---|
| SCG | Spring Cloud Gateway（API网关）。 |
| HIGRESS | Higress（AI网关）。 |
| SHARED SCG _ | 共享型Spring Cloud Gateway。 |
| CLOUD NATIVE GATEWAY _ _ | 云原生网关。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-分组管理

**概述**

分组管理模块提供路由分组的增删改查功能。分组用于对路由进行逻辑分类，可以配置分组的基础路径、默认域名等。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/group`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建分组**

**接口说明**

创建一个新的路由分组。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/createGroup |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| name | String | 是 | 分组名称。 |
| basePath | String | 是 | 分组基础路径，如 /api/v1 。 |
| groupId | String | 否 | 分组ID（可选，系统自动生成）。 |
| description | String | 否 | 分组描述。 |
| needDefaultDomain | boolean | 否 | 是否需要默认域名，默认为false。 |
| defaultDomainForRout e | Boolean | 否 | 是否为路由生成默认域名，默认为false。 |
| domainIds | List | 否 | 关联域名ID列表。 |

| isDisasterRecovery | Boolean | 否 | 是否为容灾分组，默认为 false。 |
|---|---|---|---|

**查询分组列表**

**接口说明**

分页查询路由分组列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/listGroups |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| groupId | String | 否 | 分组ID筛选。 |
| groupIdList | List | 否 | 分组ID列表筛选。 |
| name | String | 否 | 分组名称（模糊搜索）。 |
| defaultDomainIsNull | Boolean | 否 | 默认域名是否为空筛选。 |
| editable | Boolean | 否 | 是否可编辑筛选。 |
| isDisasterRecovery | Boolean | 否 | 是否容灾分组筛选。 |

**查询分组详情**

**接口说明**

根据分组ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/getGroup |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| groupId | String | 是 | 分组ID。 |

**修改分组**

**接口说明**

修改已存在的分组配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/modifyGroup |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|

| gwInstanceId | String | 是 | 网关实例ID。 |
|---|---|---|---|
| groupId | String | 是 | 分组ID。 |
| name | String | 否 | 分组名称。 |
| basePath | String | 否 | 分组基础路径。 |
| description | String | 否 | 分组描述。 |
| domainIds | List | 否 | 关联域名ID列表。 |
| defaultDomainForRout e | Boolean | 否 | 是否为路由生成默认域名。 |

**删除分组**

**接口说明**

删除指定的分组。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/deleteGroup |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| groupId | String | 是 | 分组ID。 |

**添加分组域名**

**接口说明**

为分组添加关联域名。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/addGroupDomain |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| groupId | String | 是 | 分组ID。 |
| domainIds | List | 是 | 要添加的域名ID列表。 |

**删除分组域名**

**接口说明**

删除分组关联的域名。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/deleteGroupDomain |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| groupId | String | 是 | 分组ID。 |
| domainId | String | 是 | 要删除的域名ID。 |

**查询所有分组**

**接口说明**

查询网关实例下的所有分组（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /group/getAllGroups |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用分组管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.Arrays;
```

```java
import java.util.HashMap; import java.util.List; import java.util.Map; public class GroupApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== 创建分组 ==========
        String groupId = createGroup(client);
```

`// ==========` 查询分组列表 `==========`

```
        listGroups(client);
```

`// ==========` 查询分组详情 `==========`

```
        getGroup(client, groupId);
        // ========== 修改分组 ==========
        modifyGroup(client, groupId);
```

`// ==========` 添加分组域名 `==========`

```
        addGroupDomain(client, groupId, Arrays.asList("domain-id-xxx"));
```

`// ==========` 删除分组域名 `==========`

```java
        deleteGroupDomain(client, groupId, "domain-id-xxx");
        // ========== 删除分组 ==========
        deleteGroup(client, groupId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
```

i t

```
tti Sti tEd it(){
```

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

`*/`

```java
    private static String createGroup(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "api-group-demo");                              // 【必填】分组
```

名称

```
        request.put("basePath", "/api/v1");                                 // 【必填】分组
```

基础路径

```
        request.put("description", "API demo group");                       // 【可选】分
```

组描述

```
        // request.put("groupId", "");                                         // 【可选】
```

分组`ID`（系统自动生成）

```
        // request.put("needDefaultDomain", false);                            // 【可选】
```

是否需要默认域名

```
        // request.put("defaultDomainForRoute", false);                        // 【可选】
```

是否为路由生成默认域名

```
        // request.put("domainIds", Arrays.asList("domain-id-xxx"));           // 【可选
```

】关联域名`ID`列表

```
        // request.put("isDisasterRecovery", false);                           // 【可选】
```

是否为容灾分组

```
        CommonRequest commonRequest = createBaseRequest("/group/createGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
JSONObjectresult=
```

```java
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String groupId = result.getString("data");
            System.out.println("createGroup success, groupId: " + groupId);
            return groupId;
        } else {
            System.out.println("createGroup failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

`*/`

```java
    private static void listGroups(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("name", "");                                            // 【可选】
```

分组名称（模糊搜索）

```
        // request.put("editable", true);                                      // 【可选】
```

是否可编辑筛选

```
        // request.put("isDisasterRecovery", false);                           // 【可选】
```

是否容灾分组筛选

```
        CommonRequest commonRequest = createBaseRequest("/group/listGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getGroup(IAcsClient client, String groupId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("groupId", groupId);                                    // 【必填】分组
```

`ID`

```
        CommonRequest commonRequest = createBaseRequest("/group/getGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
```

`Co` o

```
espose espose
```

c

```
et.getCo
```

o

```
espose(co
```

o

```
equest); response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void modifyGroup(IAcsClient client, String groupId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("groupId", groupId);                                    // 【必填】分组
```

`ID`

```
        request.put("name", "api-group-modified");                          // 【可选】分组
```

名称

```
        request.put("basePath", "/api/v2");                                 // 【可选】分组
```

基础路径

```
        request.put("description", "Modified group description");           // 【可选】分
```

组描述

```
        CommonRequest commonRequest = createBaseRequest("/group/modifyGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void addGroupDomain(IAcsClient client, String groupId, List<String>
domainIds) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("groupId", groupId);                                    // 【必填】分组
```

`ID`

```
        request.put("domainIds", domainIds);                                // 【必填】要添
```

加的域名`ID`列表

```
        CommonRequest commonRequest = createBaseRequest("/group/addGroupDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void deleteGroupDomain(IAcsClient client, String groupId, String dom
ainId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("groupId", groupId);                                    // 【必填】分组
```

`ID`

```
        request.put("domainId", domainId);                                  // 【必填】要删
```

除的域名`ID`

```
        CommonRequest commonRequest = createBaseRequest("/group/deleteGroupDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除分组
`*/`

```java
    private static void deleteGroup(IAcsClient client, String groupId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("groupId", groupId);                                    // 【必填】分组
```

`ID`

```
        CommonRequest commonRequest = createBaseRequest("/group/deleteGroup");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询所有分组
`*/`

```java
    private static void getAllGroups(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/group/getAllGroups");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
```

```
response.getHttpResponse().getHttpContentString());
    }
}
```

**分组属性说明**

| 属性 | 说明 |
|---|---|
| groupId | 分组唯一标识。 |
| name | 分组名称。 |
| basePath | 分组基础路径，所有该分组下的路由都会继承此路径前缀。 |
| description | 分组描述。 |
| defaultDomain | 分组默认域名。 |
| editable | 是否可编辑： true：可编辑。 false：不可编辑（如DEFAULT分组）。 |
| isDisasterRecovery | 是否为容灾分组。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-路由管理

**概述**

路由管理模块提供路由的增删改查功能。路由用于定义请求如何从网关转发到后端服务。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/route`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建路由前校验**

**接口说明**

创建路由前进行参数校验，检查路由名称是否重复等。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/checkCreateRoute |
| Method | POST |
| Content-Type | application/json |

**创建路由**

**接口说明**

创建一个新的路由规则。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/createRoute |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 RouteCreateRequest + AbstractRouteRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|

| gwInstanceId | String | 是 | 网关实例ID。 |
|---|---|---|---|
| routeName | String | 是 | 路由名称，唯一标识。 |
| groupId | String | 是 | 分组ID，默认分组为“DEFAULT”。 |
| routePath | List | 是 | 路径列表，支持Ant风格通配符。 |
| serviceType | String | 是 | 服务类型： SINGLE：单服务 WEIGHTED：加权 |
| serviceId | String | 条件必填 | 后端服务ID。 说明单服务模式必填。 |
| serviceIds | List | 条件必填 | 服务列表及权重。 说明加权模式必填。 |
| path | RoutePath | 否 | 新版路径匹配配置，优先级高于 routePath 。 |
| order | int | 否 | 路由优先级，数字越小优先级越高，默认为0。 |
| enableStatus | Boolean | 否 | 启用状态，默认为true。 |
| openStripPrefix | boolean | 否 | 是否开启路径前缀剥离， 默认为false。 |
| stripPrefix | int | 否 | 剥离前缀层数，配合 openStripPrefix使用。 |
| methods | List | 否 | HTTP方法限制， 如 ["GET","POST"] 。 |

| header | List | 否 | Header匹配条件列表。 |
|---|---|---|---|
| cookie | List | 否 | Cookie匹配条件列表。 |
| queryParam | List | 否 | Query参数匹配条件列表。 |
| domainIds | List | 否 | 关联域名ID列表。 |
| requestTimeout | Integer | 否 | 请求超时时间（毫秒）。 |
| isDisasterRecovery | Boolean | 否 | 是否为容灾路由。 |
| disasterRecoveryServi ceId | String | 否 | 容灾服务ID。 |
| disasterRecoveryServi ceIds | List | 否 | 容灾服务ID列表及权重。 |
| hsfMethodMappingCon fig | HsfMethodMappingCon fig | 否 | HSF方法映射配置（仅 HSF协议配置）。 |

**RoutePath 结构**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| matchType | String | 是 | 匹配类型： PRE：前缀 EXACT：精确 REGEX：正则 |
| matchValue | String | 否 | 匹配值。 |
| caseSensitive | Boolean | 否 | 是否区分大小写。 |

**KvPair 结构**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| key | String | 是 | 键名。 |

| value | String | 是 | 键值。 |
|---|---|---|---|

**ServiceAndWeight 结构**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| serviceId | String | 是 | 服务ID。 |
| weight | Integer | 是 | 权重（0-100）。 |

**查询路由列表**

**接口说明**

分页查询路由列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/listRoutes |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 RouteListRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| routeName | String | 否 | 路由名称（模糊搜索）。 |
| serviceName | String | 否 | 服务名称（模糊搜索）。 |

| exactServiceId | String | 否 | 服务ID（精确搜索）。 |
|---|---|---|---|
| enableStatus | Boolean | 否 | 启用状态筛选。 |
| routeId | String | 否 | 路由ID。 |
| groupName | String | 否 | 分组名称。 |
| domainName | String | 否 | 域名名称。 |
| routePath | String | 否 | 路由路径（模糊搜索）。 |
| isDisasterRecovery | Boolean | 否 | 是否容灾路由。 |

**查询路由详情**

**接口说明**

根据路由ID查询路由详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/getRoute |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| routeId | String | 是 | 路由ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改路由**

**接口说明**

修改已存在的路由配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/modifyRoute |
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建路由参数相同，额外需要指定 `routeId` 。

**删除路由**

**接口说明**

删除指定的路由。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/deleteRoute |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| routeId | String | 是 | 路由ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改路由启用状态**

**接口说明**

启用或禁用路由。

**说明**

仅适用于 SCG 引擎，Higress 引擎不支持此接口。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/changeRouteStatus |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| routeId | String | 是 | 路由ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |
| enableStatus | Boolean | 是 | true：启用 false：禁用 |

**批量删除路由**

**接口说明**

批量删除多个路由。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/batchDeleteRoute |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| routeIds | List | 是 | 路由ID列表。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用路由管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class RouteApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========` `//` 自建`ACK`环境配置

```java
    private static final boolean IS_SELF_HOSTED = true;                     // 是否自建
```

`ACK`环境

```java
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // 自建ACK控
```

制台地址 `//` 企业版环境配置（当 `IS_SELF_HOSTED = false` 时使用）

```java
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
```

`//` 网关实例`ID`和后端服务`ID`

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String SERVICE_ID = "your-service-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 创建路由前校验 `==========`

```
        checkCreateRoute(client);
        // ========== 创建路由 ==========
        String routeId = createRoute(client);
```

`// ==========` 查询路由列表 `==========`

```
        listRoutes(client);
```

`// ==========` 查询路由详情 `==========`

```
        getRoute(client, routeId);
        // ========== 修改路由 ==========
        modifyRoute(client, routeId);
```

`// ==========` 修改路由状态 `==========`

```
        changeRouteStatus(client, routeId, false);
        // ========== 删除路由 ==========
        deleteRoute(client, routeId);
    }
    /**
```

* 创建客户端（自建`ACK`和企业版通用）
`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
```

t `tS`

```
Mthd(MthdT POST)
```

```
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建路由前校验
`*/`

```java
    private static void checkCreateRoute(IAcsClient client) throws Exception {
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/checkCreateRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 创建路由
`*/`

```java
    private static String createRoute(IAcsClient client) throws Exception {
        Map<String, Object> request = buildRouteRequest();
        CommonRequest commonRequest = createBaseRequest("/route/createRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonRequest(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String routeId = result.getString("data");
            System.out.println("createRoute success, routeId: " + routeId);
            return routeId;
        } else {
            System.out.println("createRoute failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 构建路由请求参数
`*/`

```java
    private static Map<String, Object> buildRouteRequest() {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeName", "route-demo-01");                          // 【必填】路
```

由名称

```
        request.put("groupId", "DEFAULT");                                  // 【必填】分组
```

`ID` `ID`

```
        request.put("routePath", Arrays.asList("/api-demo/**"));            // 【必填】路
```

径列表

```
        request.put("serviceType", "SINGLE");                               // 【必填】服务
```

类型：`SINGLE/WEIGHTED`

```
        request.put("serviceId", SERVICE_ID);                               // 【必填】后端
```

服务`ID`（`SINGLE`模式）

```
        request.put("enableStatus", true);                                  // 【可选】启用
```

状态

```
        request.put("order", 100);                                          // 【可选】路由
```

优先级

```
        // request.put("openStripPrefix", false);                             // 【可选】
```

是否开启路径前缀剥离

```
        // request.put("stripPrefix", 1);                                     // 【可选】剥
```

离前缀层数

```
        // request.put("methods", Arrays.asList("GET", "POST"));              // 【可选】
```

`HTTP`方法限制

```
        // request.put("domainIds", new ArrayList<>());                        // 【可选】
```

关联域名`ID`列表 `//` 新版路径匹配配置（优先级高于`routePath`）

```
        // Map<String, Object> path = new HashMap<>();
        // path.put("matchType", "PRE");                                      // PRE/EXAC
T/REGEX
        // path.put("matchValue", "");                                        // 匹配值
        // path.put("caseSensitive", false);                                  // 是否区分大
```

小写

```
        // request.put("path", path);
```

`//` 加权模式服务列表（`WEIGHTED`模式）

```
        // List<Map<String, Object>> serviceIds = new ArrayList<>();
        // Map<String, Object> service1 = new HashMap<>();
        // service1.put("serviceId", "service-id-1");
        // service1.put("weight", 80);
        // Map<String, Object> service2 = new HashMap<>();
        // service2.put("serviceId", "service-id-2");
        // service2.put("weight", 20);
        // serviceIds.add(service1);
        // serviceIds.add(service2);
        // request.put("serviceIds", serviceIds);
```

`// Header`匹配条件

```
        // List<Map<String, Object>> header = new ArrayList<>();
        // Map<String, Object> headerCondition = new HashMap<>();
        // headerCondition.put("key", "X-Version");
        // headerCondition.put("value", "v1");
        // header.add(headerCondition);
        // request.put("header", header);
```

`// Cookie`匹配条件

```
        // List<Map<String, Object>> cookie = new ArrayList<>();
        // Map<String, Object> cookieCondition = new HashMap<>();
        // cookieCondition.put("key", "sessionId");
        // cookieCondition.put("value", "session-*");
        // cookie.add(cookieCondition);
```

```
        // cookie.add(cookieCondition);
        // request.put("cookie", cookie);
```

`// Query`参数匹配条件

```
        // List<Map<String, Object>> queryParam = new ArrayList<>();
        // Map<String, Object> queryCondition = new HashMap<>();
        // queryCondition.put("key", "version");
        // queryCondition.put("value", "1.0");
        // queryParam.add(queryCondition);
        // request.put("queryParam", queryParam);
```

`//` 容灾路由配置

```
        // request.put("isDisasterRecovery", true);                           // 【可选】
```

是否为容灾路由

```
        // request.put("disasterRecoveryServiceId", "disaster-service-id");   // 【可选】
```

容灾服务`ID`

```
        return request;
    }
    /**
```

* 查询路由列表
`*/`

```java
    private static void listRoutes(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("routeName", "");                                      // 【可选】路
```

由名称（模糊搜索）

```
        // request.put("serviceName", "");                                    // 【可选】服
```

务名称（模糊搜索）

```
        // request.put("enableStatus", true);                                 // 【可选】
```

启用状态筛选

```
        CommonRequest commonRequest = createBaseRequest("/route/listRoutes");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询路由详情
`*/`

```java
    private static void getRoute(IAcsClient client, String routeId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // 【必填】路由
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/route/getRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改路由
`*/`

```java
    private static void modifyRoute(IAcsClient client, String routeId) throws Exception
{
        Map<String, Object> request = buildRouteRequest();
        request.put("routeId", routeId);                                    // 【必填】要修
```

改的路由`ID`

```
        request.put("routeName", "route-demo-01-modified");                 // 【可选】修
```

改路由名称

```
        request.put("order", 200);                                          // 【可选】修改
```

优先级

```
        CommonRequest commonRequest = createBaseRequest("/route/modifyRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改路由状态
`*/`

```java
    private static void changeRouteStatus(IAcsClient client, String routeId, boolean en
ableStatus) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // 【必填】路由
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("enableStatus", enableStatus);                          // 【必填】启
```

用状态

```
        CommonRequest commonRequest = createBaseRequest("/route/changeRouteStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
```

```
    /**
```

* 删除路由
`*/`

```java
    private static void deleteRoute(IAcsClient client, String routeId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("routeId", routeId);                                    // 【必填】路由
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/route/deleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 批量删除路由
`*/`

```java
    private static void batchDeleteRoutes(IAcsClient client, List<String> routeIds) thr
ows Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("routeIds", routeIds);                                  // 【必填】路由
```

`ID`列表

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/route/batchDeleteRoute");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**路径匹配类型说明**

| matchType | 说明 | 示例 |
|---|---|---|
| PRE | 前缀匹配 | /api/** 匹配所有 /api/ 开头的路径。 |

| EXACT | 精确匹配 | /api/user 仅匹配 /api/user 。 |
|---|---|---|
| REGEX | 正则匹配 | 使用正则表达式匹配路径。 |

**服务类型说明**

| serviceType | 说明 | 使用方式 |
|---|---|---|
| SINGLE | 单服务 | 使用 serviceId 指定一个后端服务 |
| WEIGHTED | 加权服务 | 使用 serviceIds 指定多个服务及权重 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-策略配置管理

**概述**

策略配置管理模块提供策略的增删改查功能。策略用于配置路由、服务、消费者的各种行为，如限流、熔断、重试、跨域等。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/strategyConfig/**`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建策略配置**

**接口说明**

创建一个新的策略配置。不同策略类型的 `config` 字段结构不同，详见下方策略配置示例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /strategyConfig/createStrategyConfig |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| strategyName | String | 是 | 策略类型的英文名称。 |
| strategyConfigName | String | 否 | 策略配置名称。 |
| config | Object | 否 | 策略配置参数（Map格式）。 |
| rawConfig | String | 否 | 策略配置参数（YAML格式）。 |
| routeIds | List | 否 | 关联的路由ID列表。 |
| serviceIds | List | 否 | 关联的服务ID列表。 |
| appIds | List | 否 | 关联的消费者ID列表。 |
| domainIds | List | 否 | 关联的域名ID列表。 |

**查询策略配置列表**

**接口说明**

分页查询策略配置列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /strategyConfig/listStrategyConfigs |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| strategyName | String | 否 | 策略类型名称筛选。 |
| routeId | String | 否 | 关联的路由ID筛选。 |
| serviceId | String | 否 | 关联的服务ID筛选。 |
| appId | String | 否 | 关联的消费者ID筛选。 |

**查询策略配置详情**

**接口说明**

根据策略配置ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /strategyConfig/getStrategyConfig |

| Method | POST |
|---|---|
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| strategyConfigId | String | 是 | 策略配置ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改策略配置**

**接口说明**

修改已存在的策略配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /strategyConfig/modifyStrategyConfig |
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建策略配置参数相同，额外需要指定 `strategyConfigId` 。

**修改策略配置状态**

**接口说明**

启用或禁用策略配置。

**请求信息**

| 项目 |  | 内容 |  |  |
|---|---|---|---|---|
| URL |  | /strategyConfig/modifyStrategyConfigStatus |  |  |
|  |  |  | /strategyConfig/modifyStrategyConfigStatus |  |
|  | RL |  |  |  |

| 17 | > 文档版本：2026072 |
|---|---|

| PI 网关 | 开发指南·通过POP网关调用专有云A |
|---|---|

| Method | POST |
|---|---|
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| strategyConfigId | String | 是 | 策略配置ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |
| isOpen | Boolean | 是 | true：启用 false：禁用 |

**删除策略配置**

**接口说明**

删除指定的策略配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /strategyConfig/deleteStrategyConfig |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| strategyConfigId | String | 是 | 策略配置ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用策略配置管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.ArrayList; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class StrategyConfigApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========` `//` 自建`ACK`环境配置

```java
    private static final boolean IS_SELF_HOSTED = true;                     // 是否自建
```

`ACK`环境

```java
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // 自建ACK控
```

制台地址 `//` 企业版环境配置（当 `IS_SELF_HOSTED = false` 时使用）

```java
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";  //
```

企业版`Endpoint`

```java
    private static final String ACCESS_KEY_ID = "your-access-key-id";                //
AccessKey ID
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";        //
AccessKey Secret
    private static final String ORGANIZATION_ID = "your-org-id";                     //
```

企业组织`ID` `//` 网关实例`ID`

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
```

`//` 初始化客户端

```
        IAcsClient client = createClient();
```

`// ==========` 示例：创建不同类型的策略配置 `==========` `// 1.` 流控策略

```
        String flowControlStrategyId = createFlowControlStrategy(client);
```

`// 2.` 超时策略

```
        String timeoutStrategyId = createTimeoutStrategy(client);
```

熔断策略

```
//3
```

`// 3.` 熔断策略

```
        String circuitBreakerStrategyId = createCircuitBreakerStrategy(client);
```

`// 4.` 跨域策略

```
        String corsStrategyId = createCorsStrategy(client);
```

`// 5.` 缓存策略

```
        String cacheStrategyId = createCacheStrategy(client);
```

`// 6. IP`黑白名单策略

```
        String ipBlockStrategyId = createIpBlockStrategy(client);
```

`// 7. ACL`权限控制策略

```
        String aclStrategyId = createAclStrategy(client);
```

`// 8. Mock`策略

```
        String mockStrategyId = createMockStrategy(client);
```

`// 9.` 请求追踪策略

```
        String tracingStrategyId = createTracingStrategy(client);
```

`// 10.` 请求体大小限制策略

```
        String requestSizeStrategyId = createRequestSizeStrategy(client);
```

`// ==========` 查询策略配置列表 `==========`

```
        listStrategyConfigs(client);
```

`// ==========` 查询策略配置详情 `==========`

```
        getStrategyConfig(client, flowControlStrategyId);
```

`// ==========` 修改策略配置状态 `==========`

```
        modifyStrategyConfigStatus(client, flowControlStrategyId, false);
```

`// ==========` 删除策略配置 `==========`

```
        deleteStrategyConfig(client, flowControlStrategyId);
    }
    /**
```

* 创建客户端（自建`ACK`和企业版通用）
`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
```

`//` 自建`ACK`环境：`AK/SK`不需要填写

```
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
```

`//` 企业版环境：需要有效的`AK/SK`

```
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    /**
```

* 获取`Endpoint`
获取 p `*/`

```java
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    /**
```

* 设置认证`Header`（自建`ACK`和企业版通用）
`*/`

```java
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
```

`//` 自建`ACK`环境认证

```
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
```

`//` 企业版环境认证

```
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    /**
```

* 创建基础请求对象
`*/`

```java
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
```

`// ==========` 策略配置创建示例 `==========`

```
    /**
     * 1. 流控策略 (Flow Control Policy)
     * config结构: CacheGatewayFlowRule
```

`*/`

```java
    private static String createFlowControlStrategy(IAcsClient client) throws Exception
{
```

`//` 流控规则配置

```
        Map<String, Object> flowRule = new HashMap<>();
        flowRule.put("resource", "route-id-xxx");                           // 【必填】资源
```

名称（路由`ID`）

```
        flowRule.put("resourceMode", 0);                                    // 【必填】资源
```

模式：`0-`路由`ID, 1-API`分组

```
        flowRule.put("grade", 1);                                           // 【必填】限流
```

阈值类型：`1-QPS`

```
        flowRule.put("count", 100.0);                                       // 【必填】限流
```

阈值（`QPS`数量）

```
        flowRule.put("controlBehavior", 0);                                 // 【可选】流控
```

效果：`0-`快速失败`, 2-`匀速排队

```
        flowRule.put("intervalSec", 1L);                                    // 【可选】统计
```

时间窗口（秒）

```
        flowRule.put("burst", 20);                                          // 【可选】突发
```

容量

```
        flowRule.put("maxQueueingTimeoutMs", 500);                          // 【可选】最大
```

排队等待时间（毫秒）

```
        flowRule.put("enable", true);                                       // 【可选】是否
```

启用 `//` 可选：参数限流配置

```
        // Map<String, Object> paramItem = new HashMap<>();
        // paramItem.put("parseStrategy", 0);                                // 参数提取策
```

略：`0-`客户端`IP, 1-Host, 2-Header, 3-URL`参数

```
        // paramItem.put("fieldName", "X-User-Id");                          // 参数字段名
        // paramItem.put("pattern", "user-*");                               // 匹配模式
        // paramItem.put("matchStrategy", 0);                                // 匹配策略：
```

`0-`精确`, 1-`正则

```
        // flowRule.put("paramItem", paramItem);
        List<Map<String, Object>> gatewayFlowRules = new ArrayList<>();
        gatewayFlowRules.add(flowRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenTrafficControl", true);                           // 【必填】是
```

否开启流控

```
        config.put("gatewayFlowRules", gatewayFlowRules);                   // 【必填】流
```

控规则列表

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Flow Control Policy");
        request.put("strategyConfigName", "route-flow-control");
        request.put("config", config);
        return executeCreate(client, request, "Flow Control Policy");
    }
    /**
```

`* 2.` 超时策略 `(Timeout Policy)`

```
     * config结构: RequestTimeoutConfig
```

`*/`

```java
    private static String createTimeoutStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("timeout", 30000);                                       // 【必填】超时
```

时间（毫秒）

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Timeout Policy");
        request.put("strategyConfigName", "route-timeout");
        request.put("config", config);
        return executeCreate(client, request, "Timeout Policy");
    }
```

```
    /**
     * 3. 熔断策略 (Circuit Breaker Policy)
     * config结构: CacheRouteFuse
```

`*/`

```java
    private static String createCircuitBreakerStrategy(IAcsClient client) throws Except
ion {
```

`//` 熔断条件配置

```
        Map<String, Object> fuseCondition = new HashMap<>();
        fuseCondition.put("type", 2);                                       // 【必填】规则
```

类型：`1-`平均响应时间`, 2-`异常数`, 3-`后端超时

```
        fuseCondition.put("operator", "in");                                // 【必填】比较
```

符：`gt(`大于`), in(`包含`), notIn(`不包含)

```
        fuseCondition.put("judgValue", "500,502,503");                      // 【必填】判
```

断值（错误码列表或响应时间）

```
        fuseCondition.put("errorCount", 5.0);                               // 【可选】错误
```

次数阈值

```
        fuseCondition.put("statInterval", 30);                              // 【可选】判断
```

时间窗口（秒）

```
        fuseCondition.put("timeWindow", 20);                                // 【可选】断路
```

器持续时间（秒）

```
        fuseCondition.put("minRequestAmount", 10);                          // 【可选】最
```

小请求数

```
        List<Map<String, Object>> routeFusesCondition = new ArrayList<>();
        routeFusesCondition.add(fuseCondition);
```

`//` 降级`Mock`配置（当`degradeStrategy=1`时使用）

```
        Map<String, Object> fuseMock = new HashMap<>();
        fuseMock.put("isOpen", 1);                                          // 0-关闭, 1-
```

开启

```
        fuseMock.put("responseCode", 200);                                  // 【可选】响应
```

状态码

```
        fuseMock.put("responseBody", "{\"code\":0,\"msg\":\"service degraded\"}");  //
```

【可选】响应体

```
        fuseMock.put("responseHeader", Arrays.asList("Content-Type:application/json"));
```

`//` 【可选】响应头列表

```
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenFuse", true);                                     // 【必填】是否
```

开启熔断

```
        config.put("combinedCondition", "any");                             // 【可选】组合
```

条件：`all(`全部满足`), any(`任一满足)

```
        config.put("routeFusesCondition", routeFusesCondition);             // 【必填】熔
```

断条件列表

```
        config.put("degradeStrategy", 1);                                   // 【可选】降级
```

策略：`1-Mock`响应

```
        config.put("fuseMock", fuseMock);                                   // 【可选】降级
```

`Mock`配置

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Circuit Breaker Policy");
        request.put("strategyConfigName", "route-circuit-breaker");
```

t

```
t(" fi" fi)
```

```
        request.put("config", config);
        return executeCreate(client, request, "Circuit Breaker Policy");
    }
    /**
     * 4. 跨域策略 (Cross-domain Policy)
     * config结构: RouteCross
```

`*/`

```java
    private static String createCorsStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenCross", true);                                    // 【必填】是否
```

开启跨域

```
        config.put("crossType", "cors");                                    // 【可选】跨域
```

类型：`cors, jsonp`

```
        config.put("allowedOrigins", "*");                                  // 【必填】允许
```

的来源（*表示全部）

```
        config.put("allowedMethods", Arrays.asList("GET", "POST", "PUT", "DELETE",
```

"OPTIONS")); // 【必填】允许的方法

```
        config.put("allowedHeaders", "*");                                  // 【可选】允许
```

的请求头

```
        config.put("exposedHeaders", "X-Custom-Header");                    // 【可选】暴
```

露的响应头

```
        config.put("allowedCredentials", true);                             // 【可选】是否
```

允许携带凭证

```
        config.put("maxAge", 3600L);                                        // 【可选】预检
```

请求缓存时间（秒）

```
        config.put("callbackFunc", "callback");                             // 【可选】JSO
```

`NP`回调函数名

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Cross-domain Policy");
        request.put("strategyConfigName", "route-cors");
        request.put("config", config);
        return executeCreate(client, request, "Cross-domain Policy");
    }
    /**
```

`* 5.` 缓存策略 `(Caching Policy)`

```
     * config结构: ResponseCache
```

`*/`

```java
    private static String createCacheStrategy(IAcsClient client) throws Exception {
```

`//` 缓存接口配置

```
        Map<String, Object> cacheRequest = new HashMap<>();
        cacheRequest.put("routeId", "route-id-xxx");                        // 【必填】路
```

由`ID`

```
        cacheRequest.put("cacheKey", "query:userId");                       // 【可选】缓
```

存`Key`规则

```
        List<Map<String, Object>> routeInterfaceList = new ArrayList<>();
        routeInterfaceList.add(cacheRequest);
Map<String Object>config=newHashMap<>();
```

```
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenResponseCache", true);                            // 【必填】是否
```

开启缓存

```
        config.put("routeInterfaceList", routeInterfaceList);               // 【可选】缓
```

存接口列表

```
        config.put("isOpenCacheControl", true);                             // 【可选】是否
```

开启浏览器缓存控制

```
        config.put("maxAge", 300L);                                         // 【可选】浏览
```

器缓存时间（秒）

```
        config.put("allowedStatusCodes", Arrays.asList(200, 301, 302));     // 【可选】允
```

许缓存的状态码

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Caching Policy");
        request.put("strategyConfigName", "route-cache");
        request.put("config", config);
        return executeCreate(client, request, "Caching Policy");
    }
    /**
     * 6. IP黑白名单策略 (IP Blacklist and Whitelist Policy)
     * config结构: RouteIpBlockConfig
```

`*/`

```java
    private static String createIpBlockStrategy(IAcsClient client) throws Exception {
```

`// IP`规则配置

```
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("ip", "192.168.1.100");                               // 【必填】IP
```

地址（支持`CIDR`格式）

```
        allowRule.put("policy", "allow");                                   // 【必填】策略
```

：`allow-`白名单`, deny-`黑名单

```
        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("ip", "10.0.0.0/8");                                   // 【必填】IP地
```

址（`CIDR`格式）

```
        denyRule.put("policy", "deny");                                     // 【必填】策略
        List<Map<String, Object>> ipBlockRules = new ArrayList<>();
        ipBlockRules.add(allowRule);
        ipBlockRules.add(denyRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenIpBlock", true);                                  // 【必填】是否
```

开启`IP`黑白名单

```
        config.put("ipBlockRules", ipBlockRules);                           // 【必填】IP
```

规则列表

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "IP Blacklist and Whitelist Policy");
        request.put("strategyConfigName", "route-ip-block");
        request.put("config", config);
        return executeCreate(client, request, "IP Blacklist and Whitelist Policy");
```

```
        return executeCreate(client, request, IP Blacklist and Whitelist Policy);
    }
    /**
     * 7. ACL权限控制策略 (ACL Permission Control Policy)
     * config结构: RouteACLConfig
```

`*/`

```java
    private static String createAclStrategy(IAcsClient client) throws Exception {
```

`// ACL`规则配置

```
        Map<String, Object> allowRule = new HashMap<>();
        allowRule.put("group", "consumer-group-allow");                     // 【必填】消
```

费者分组`/ID`

```
        allowRule.put("policy", "allow");                                   // 【必填】策略
```

：`allow-`允许`, deny-`拒绝

```
        Map<String, Object> denyRule = new HashMap<>();
        denyRule.put("group", "consumer-group-deny");                       // 【必填】消
```

费者分组`/ID`

```
        denyRule.put("policy", "deny");                                     // 【必填】策略
        List<Map<String, Object>> aclRules = new ArrayList<>();
        aclRules.add(allowRule);
        aclRules.add(denyRule);
        Map<String, Object> config = new HashMap<>();
        config.put("isEnableACL", true);                                    // 【必填】是否
```

开启`ACL`权限控制

```
        config.put("aclRules", aclRules);                                   // 【必填】ACL
```

规则列表

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "ACL Permission Control Policy");
        request.put("strategyConfigName", "route-acl");
        request.put("config", config);
        return executeCreate(client, request, "ACL Permission Control Policy");
    }
    /**
     * 8. Mock策略 (MOCK Policy)
     * config结构: CacheMockConfig
```

`*/`

```java
    private static String createMockStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isOpenMock", true);                                     // 【必填】是否
```

开启`Mock`

```
        config.put("responseCode", 200);                                    // 【可选】响应
```

状态码

```
        config.put("responseBody", "{\"code\":0,\"data\":{\"id\":1}}");     // 【可选】响
```

应体

```
        config.put("responseHeader", Arrays.asList(                         // 【可选】响
```

应头列表

```
            "Content-Type:application/json",
            "X-Mock:true"
```

```
        ));
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "MOCK Policy");
        request.put("strategyConfigName", "route-mock");
        request.put("config", config);
        return executeCreate(client, request, "MOCK Policy");
    }
    /**
```

`* 9.` 请求追踪策略 `(Request Tracing Policy)`

```
     * config结构: RouteTracingConfig
```

`*/`

```java
    private static String createTracingStrategy(IAcsClient client) throws Exception {
        Map<String, Object> config = new HashMap<>();
        config.put("isEnableTracing", true);                                // 【必填】是否
```

开启追踪

```
        config.put("traceHeader", "X-Trace-Id");                            // 【必填】追踪
```

`Header`名称

```
        config.put("isEnableDownstream", true);                             // 【可选】是否
```

传递给下游服务

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Tracing Policy");
        request.put("strategyConfigName", "route-tracing");
        request.put("config", config);
        return executeCreate(client, request, "Request Tracing Policy");
    }
    /**
```

`* 10.` 请求体大小限制策略 `(Request Size Limit Policy)`

```
     * config结构: DataSize
```

`*/`

```java
    private static String createRequestSizeStrategy(IAcsClient client) throws Exception
{
        Map<String, Object> config = new HashMap<>();
        config.put("dataSize", "10MB");                                     // 【必填】请求
```

体最大大小（支持`KB/MB/GB`单位）

```
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("strategyName", "Request Size Limit Policy");
        request.put("strategyConfigName", "route-request-size");
        request.put("config", config);
        return executeCreate(client, request, "Request Size Limit Policy");
    }
```

`// ==========` 通用操作方法 `==========`

```
    /**
```

* 执行创建策略配置
`*/`

```java
    private static String executeCreate(IAcsClient client, Map<String, Object> request,
String strategyName) throws Exception {
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/createStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String strategyId = result.getString("data");
            System.out.println("create " + strategyName + " success, strategyId: " + st
rategyId);
            return strategyId;
        } else {
            System.out.println("create " + strategyName + " failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询策略配置列表
`*/`

```java
    private static void listStrategyConfigs(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("current", 1);
        request.put("size", 10);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/listStrategyConfigs");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询策略配置详情
`*/`

```java
    private static void getStrategyConfig(IAcsClient client, String strategyConfigId) t
hrows Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
```

```
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/getStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改策略配置状态
`*/`

```java
    private static void modifyStrategyConfigStatus(IAcsClient client, String
strategyConfigId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        request.put("isOpen", isOpen);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/modifyStrategyConfigStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyStrategyConfigStatus: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除策略配置
`*/`

```java
    private static void deleteStrategyConfig(IAcsClient client, String
strategyConfigId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("strategyConfigId", strategyConfigId);
        request.put("gwInstanceId", GW_INSTANCE_ID);
        CommonRequest commonRequest =
createBaseRequest("/strategyConfig/deleteStrategyConfig");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**策略类型说明（strategyName）**

策略类型使用英文 `strategyName` 作为标识，不同引擎支持的策略类型不同。

**SCG 策略（适用于 SCG 引擎）**

| strategyName | 中文名称 | 分类 | 说明 |
|---|---|---|---|
| Authentication Policy | 鉴权策略 | 认证 | 包含JWT、BASIC、 APIKEY等认证方式以及自定义认证，保护程序安全。 |
| Flow Control Policy | 流控策略 | 流量 | 限制请求的速率，防止瞬间海量数据对网络造成冲击。 |
| Timeout Policy | 超时策略 | 流量 | 限制网关转发请求的最大超时时间。 |
| Circuit Breaker Policy | 熔断策略 | 流量 | 在网关侧阻止对服务提供者的调用，以保护应用服务。 |
| MOCK Policy | MOCK策略 | 转换 | 设置过滤规则和返回值， 解决不易构造或获取的数据对象。 |
| Signature Policy | 签名策略 | 安全 | 对经过网关的请求生成签名。 |
| Cross-domain Policy | 跨域策略 | 转换 | 一个域下的文档或脚本通过网关可以请求另一个域下的资源。 |
| Caching Policy | 缓存策略 | 流量 | 缓存返回的响应，避免对后端服务重复请求相同资源。 |
| IP Blacklist and Whitelist Policy | IP黑白名单策略 | 安全 | 限制请求来源IP，增强后端服务安全性。 |
| Request Tracing Policy | 请求追踪策略 | 可观测性 | 对经过本网关的请求增加请求追踪头，追踪请求链路。 |
| ACL Permission Control Policy | ACL权限控制策略 | 认证 | 控制哪些消费者可以访问服务。 |

|  | Authentication | 鉴 |
|---|---|---|
| Policy |  |  |

|  |  | Flow Control |  |
|---|---|---|---|
|  | Policy |  |  |

|  | Circuit Breaker | 熔断 |
|---|---|---|
| Policy |  |  |

|  |  | Cross-domain |  |
|---|---|---|---|
|  | Policy |  |  |

|  | IP Blacklist and | IP黑白名单策略 |
|---|---|---|
| Whitelist Policy |  |  |

|  | Request Tracing | 请求 |
|---|---|---|
| Policy |  |  |

|  | ACL Permission | ACL权限控制 |
|---|---|---|
| Control Policy |  |  |

|  | Request Size Limit Policy |  | 请求体大小限制策略 | 流量 | 限制请求体的最大大小。 |
|---|---|---|---|---|---|
|  |  | Request Size | 请求体大 |  |  |
|  | Limit Policy |  |  |  |  |
|  | HSF Protocol Mapping Policy |  | HSF协议映射策略 | 转换 | 控制路由指向的HSF具体方法，设置HTTP->HSF 参数格式映射。 |
|  |  | HSF Protocol | HSF协议映 |  |  |
|  | Mapping Policy |  |  |  |  |

**Higress 策略（适用于 Higress 引擎）**

**认证类策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| basic-auth | Basic 认证 | 基于 HTTP Basic Auth 标准进行认证鉴权。 |
| hmac-auth | HMAC 认证 | 基于 HMAC 算法生成签名，实现身份认证和鉴权。 |
| jwt-auth | JWT 认证 | 基于 JSON Web Token 认证鉴权。 |
| key-auth | Key 认证 | 基于 API Key 实现身份认证和鉴权。 |
| oauth | OAuth2 认证 | 基于 OAuth2 实现身份认证和鉴权。 |
| oidc | OIDC 认证 | 基于 OpenID Connect 标准的用户身份验证。 |
| ext-auth | 外部认证 | 向外部授权服务发送鉴权请求检查客户端请求授权。 |

**安全类策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| bot-detect | 机器人拦截 | 识别并阻止互联网爬虫对站点资源的爬取。 |
| ip-restriction | IP 限制 | 将 IP 地址列入白名单或黑名单限制访问。 |

| request-block | 请求屏蔽 | 基于 URI、请求头等特征屏蔽 HTTP 请求。 |
|---|---|---|
| request-validation | 请求校验 | 验证转发请求的 Body 和 Header 数据。 |
| waf | WAF 防护 | 基于 OWASP ModSecurity CRS 的 WAF 规则配置。 |

**流量类策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| key-rate-limit | 基于 Key 限流 | 根据特定键值实现限流。 |
| cluster-key-rate-limit | 基于 Key 集群限流 | 根据特定键值实现集群层面限流。 |
| cache-control | 浏览器缓存控制 | 为响应头部添加 Expires 和 Cache- Control 头部。 |
| cors | 跨域资源共享 | 为服务端启用 CORS 返回 HTTP 响应头。 |

**转换类策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| custom-response | 自定义应答 | 配置自定义 HTTP 应答状态码、头和 Body。 |
| de-graphql | DeGraphQL | 将 Restful API 转换为 GraphQL 请求。 |
| transformer | 请求/响应转换 | 对请求/响应头、查询参数、体参数进行转换。 |
| geo-ip | IP 地理位置 | 根据 IP 查询地理位置信息传递给后续插件。 |
| frontend-gray | 前端灰度 | 实现前端用户灰度功能，用于业务 A/B 实验。 |

| model-mapper | 模型映射 | 将 LLM 协议中的模型参数取值按规则映射。 |
|---|---|---|
| model-router | 模型路由 | 基于 LLM 协议中的 model 参数路由。 |

**可观测性类策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| traffic-tag | 流量染色 | 根据权重或请求内容通过添加请求头标记流量。 |
| log-request-response | Log 请求响应记录 | 记录请求和响应信息用于调试和监控。 |

**其他策略**

| strategyName | 中文名称 | 说明 |
|---|---|---|
| opa | OPA 策略 | 实现 OPA 策略控制。 |

**策略作用域说明（scope）**

策略可以应用于不同的作用域，优先级为：**路由** > **域名** > **服务** > **消费者** > **实例。**

| scope | 中文名称 | bitMask | 说明 |
|---|---|---|---|
| INSTANCE | 实例/全局 | 1 | 策略应用于整个网关实例。 |
| ROUTE | 路由 | 2 | 策略应用于特定路由。 |
| SERVICE | 服务 | 4 | 策略应用于特定服务。 |
| CONSUMER | 消费者 | 8 | 策略应用于特定消费者。 |
| DOMAIN | 域名 | 16 | 策略应用于特定域名。 |

**复合作用域**：策略可同时应用于多个作用域，如 `scope=3` 表示同时应用于实例和路由（INSTANCE +
ROUTE = 1 + 2 = 3）。

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-消费者管理

**概述**

消费者管理模块提供消费者的增删改查功能。消费者用于API认证和授权，可以绑定到路由进行访问控制。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/application`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建消费者**

**接口说明**

创建一个新的消费者（应用）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/createApp |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| appName | String | 是 | 消费者名称。 |
| authType | Integer | 是 | 认证类型： 1：BASIC 2：OAuth2 3：JWT 4：CUSTOM 5：API KEY _ 6：API GATEWAY _ 7：CSB AUTH _ |
| key | String | 是 | 认证密钥（API Key或用户名）。 |
| password | String | 条件必填 | 密码。 说明 BASIC认证时使用。 |
| description | String | 否 | 消费者描述。 |
| expireTime | Long | 否 | 过期时间戳（毫秒）， null 表示长期有效。 |

**查询消费者列表**

**接口说明**

分页查询消费者列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/listApps |

| Method | POST |
|---|---|
| Content-Type | application/json |

**请求参数（基于 AppRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| appName | String | 否 | 消费者名称（模糊搜索）。 |
| authType | String | 否 | 认证类型筛选。 |
| appType | Integer | 否 | 应用类别： 0：后台应用 1：门户应用 |
| isDisasterRecovery | Boolean | 否 | 是否容灾消费者筛选。 |

**查询消费者详情**

**接口说明**

根据消费者ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/getApp |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| appId | String | 是 | 消费者ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改消费者**

**接口说明**

修改已存在的消费者配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/modifyApp |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| appId | String | 是 | 消费者ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |
| appName | String | 是 | 消费者名称。 |
| description | String | 否 | 消费者描述。 |

**删除消费者**

**接口说明**

删除指定的消费者。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/deleteApp |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| appId | String | 是 | 消费者ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**批量删除消费者**

**接口说明**

批量删除多个消费者。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/batchDeleteApp |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| appIds | List | 是 | 消费者ID列表。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**刷新Token**

**接口说明**

刷新消费者的Token（认证凭证）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/refreshToken |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| appId | String | 是 | 消费者ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**查询所有消费者**

**接口说明**

查询网关实例下的所有消费者（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /application/listAppsByGwInstanceId |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|

| gwInstanceId | String | 是 | 网关实例ID。 |
|---|---|---|---|

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用消费者管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.Arrays; import java.util.HashMap; import java.util.List; import java.util.Map; public class ConsumerApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========` `//` 自建`ACK`环境配置

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
```

`//` 企业版环境配置（当 `IS_SELF_HOSTED = false` 时使用）

```java
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
```

`//` 网关实例`ID`

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 创建消费者（`BASIC`认证）`==========`

```
        String appId = createBasicConsumer(client);
```

`// ==========` 创建消费者（`API Key`认证）`==========`

```
        // String apiKeyAppId = createApiKeyConsumer(client);
```

`// ==========` 查询消费者列表 `==========`

```
        listApps(client);
```

`// ==========` 查询消费者详情 `==========`

```
        getApp(client, appId);
```

`// ==========` 修改消费者 `==========`

```
        modifyApp(client, appId);
```

`// ==========` 删除消费者 `==========`

```java
        deleteApp(client, appId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建`BASIC`认证消费者
`*/`

```java
    private static String createBasicConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("appName", "consumer-demo-01");                         // 【必填】消
```

费者名称

```
        request.put("authType", 1);                                         // 【必填】认证
```

类型类型：`1-BASIC`

```
        request.put("key", "user-001");                                     // 【必填】用户
```

名

```
        request.put("password", "secret-password");                         // 【必填】密
```

码（`BASIC`认证）

```
        request.put("description", "API consumer application");             // 【可选】消
```

费者描述

```
        // request.put("expireTime", 315360000000L);                         // 【可选】过
```

期时间戳（毫秒）

```java
        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createBasicConsumer success, appId: " + appId);
            return appId;
        } else {
            System.out.println("createBasicConsumer failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`API Key`认证消费者
`*/`

```java
    private static String createApiKeyConsumer(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("appName", "consumer-apikey-demo");                     // 【必填】消
```

费者名称

```
        request.put("authType", 5);                                         // 【必填】认证
```

类型：`5-API_KEY`

```
        request.put("key", "api-key-xxx");                                  // 【必填】API
```

`Key`值

```java
        CommonRequest commonRequest = createBaseRequest("/application/createApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String appId = result.getString("data");
            System.out.println("createApiKeyConsumer success, appId: " + appId);
```

t `Id`

```java
            return appId;
        } else {
            System.out.println("createApiKeyConsumer failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询消费者列表
`*/`

```java
    private static void listApps(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("appName", "");                                        // 【可选】消
```

费者名称（模糊搜索）

```
        // request.put("authType", "1");                                      // 【可选】认
```

证类型筛选

```
        // request.put("appType", 0);                                         // 【可选】应
```

用类别：`0-`后台，`1-`门户

```
        CommonRequest commonRequest = createBaseRequest("/application/listApps");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询消费者详情
`*/`

```java
    private static void getApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【必填】消费
```

者`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/application/getApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
/**
```

/
* 修改消费者
`*/`

```java
    private static void modifyApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【必填】消费
```

者`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("appName", "consumer-demo-modified");                   // 【必填】消
```

费者名称

```
        request.put("description", "Updated description");                  // 【可选】消
```

费者描述

```
        CommonRequest commonRequest = createBaseRequest("/application/modifyApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除消费者
`*/`

```java
    private static void deleteApp(IAcsClient client, String appId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【必填】消费
```

者`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/application/deleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 批量删除消费者
`*/`

```java
    private static void batchDeleteApps(IAcsClient client, List<String> appIds) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("appIds", appIds);                                      // 【必填】消费
```

者`ID`列表

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/application/batchDeleteApp");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
```

q p

```
(
```

j y

```
(
```

q `),` ,

```
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 刷新`Token`
`*/`

```java
    private static void refreshToken(IAcsClient client, String appId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("appId", appId);                                        // 【必填】消费
```

者`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/application/refreshToken");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**认证类型说明**

| authType | 类型名称 | 说明 |
|---|---|---|
| 1 | BASIC | HTTP Basic认证，用户名密码。 |
| 2 | OAuth2.0 | OAuth2认证。 |
| 3 | JWT | JWT认证。 |
| 4 | CUSTOM | 自定义认证。 |
| 5 | API KEY _ | API Key认证。 |
| 6 | API GATEWAY _ | API网关认证。 |
| 7 | CSB AUTH _ | CSB认证。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-域名管理

**概述**

域名管理模块提供域名的增删改查功能。域名用于配置网关对外服务的访问域名，支持HTTP和HTTPS协议。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/domain`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建域名**

**接口说明**

创建一个新的域名配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/createDomain |
| Method | POST |
| Content-Type | application/json |

**请求参数（基于 CreateOrUpdateDomainRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| domain | String | 是 | 域名， 如： api.example.com 。 |
| protocol | String | 是 | 协议类型：HTTP 或 HTTPS。 |
| certificateId | String | 条件必填 | 证书ID。 说明 HTTPS协议时必填。 |
| caCertificateId | String | 否 | CA证书ID（双向认证时使用）。 |
| clientAuth | Integer | 否 | 客户端认证类型： 0：无 1：开启 |
| subjectDn | String | 否 | 客户端证书所有者信息头部。 |
| issuerDn | String | 否 | 客户端证书颁发者信息头部。 |

**查询域名列表**

**接口说明**

分页查询域名列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/listDomains |
| Method | POST |

| Content-Type | application/json |
|---|---|

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| domain | String | 否 | 域名（模糊搜索）。 |
| protocol | String | 否 | 协议类型筛选。 |

**查询域名详情**

**接口说明**

根据域名ID查询域名详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/getDomain |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| domainId | String | 是 | 域名ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改域名**

**接口说明**

修改已存在的域名配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/modifyDomain |
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建域名参数相同，额外需要指定 `domainId` 。

**删除域名**

**接口说明**

删除指定的域名。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/deleteDomain |
| Method | POST |
| Content-Type | application/json |

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| domainId | String | 是 | 域名ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**查询所有域名**

**接口说明**

查询网关实例下的所有域名（不分页）。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /domain/listAllDomains |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用域名管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class DomainApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========` `//` 自建`ACK`环境配置

```java
    private static final boolean IS_SELF_HOSTED = true;                     // 是否自建
```

`ACK`环境

```java
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";    // 自建ACK控
```

制台地址 `//` 企业版环境配置（当 `IS_SELF_HOSTED = false` 时使用）

```java
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
privatestaticfinalStringACCESSKEYSECRET="your-access-key-secret";
```

```java
    private static final String ACCESS_KEY_SECRET = youraccesskeysecret;
    private static final String ORGANIZATION_ID = "your-org-id";
```

`//` 网关实例`ID`

```java
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
        // ========== 创建HTTP域名 ==========
        String httpDomainId = createHttpDomain(client);
```

`// ==========` 创建`HTTPS`域名（带证书）`==========`

```
        // String httpsDomainId = createHttpsDomain(client);
```

`// ==========` 查询域名列表 `==========`

```
        listDomains(client);
```

`// ==========` 查询域名详情 `==========`

```
        getDomain(client, httpDomainId);
        // ========== 修改域名 ==========
        modifyDomain(client, httpDomainId);
        // ========== 删除域名 ==========
        deleteDomain(client, httpDomainId);
    }
    /**
```

* 创建客户端（自建`ACK`和企业版通用）
`*/`

```java
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
```

```java
}
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建`HTTP`域名（基于 `CreateOrUpdateDomainRequest`）
`*/`

```java
    private static String createHttpDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("domain", "api.example.com");                           // 【必填】域
```

名

```
        request.put("protocol", "HTTP");                                    // 【必填】协议
```

类型：`HTTP`

```java
        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpDomain failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`HTTPS`域名（带证书）
`*/`

```java
    private static String createHttpsDomain(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("domain", "secure.example.com");                        // 【必填】域
```

名

```
        request.put("protocol", "HTTPS");                                   // 【必填】协议
```

类型：`HTTPS`

```
        request.put("certificateId", "cert-id-xxx");                        // 【必填】证
```

书`ID`（`HTTPS`时必填）

```
        // request.put("caCertificateId", "ca-cert-id");                     // 【可选】CA
```

证书`ID`（双向认证时使用）

```
        // request.put("clientAuth", 1);                                     // 【可选】客
```

户端认证类型：`0-`无，`1-`开启

```
        // request.put("subjectDn", "CN=client");                            // 【可选】客
```

户端证书所有者信息头部

```
        // request.put("issuerDn", "CN=issuer");                             // 【可选】客
```

户端证书颁发者信息头部

```java
        CommonRequest commonRequest = createBaseRequest("/domain/createDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String domainId = result.getString("data");
            System.out.println("createHttpsDomain success, domainId: " + domainId);
            return domainId;
        } else {
            System.out.println("createHttpsDomain failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

`*/`

```java
    private static void listDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("domain", "example");                                 // 【可选】域
```

名（模糊搜索）

```
        // request.put("protocol", "HTTP");                                  // 【可选】协
```

议类型筛选

```
        CommonRequest commonRequest = createBaseRequest("/domain/listDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getDomain(IAcsClient client, String domainId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // 【必填】域名
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/domain/getDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改域名
`*/`

```java
    private static void modifyDomain(IAcsClient client, String domainId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // 【必填】要修
```

改的域名`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("domain", "api-new.example.com");                       // 【必填】域
```

名

```
        request.put("protocol", "HTTP");                                    // 【必填】协议
```

类型

```
        CommonRequest commonRequest = createBaseRequest("/domain/modifyDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonRequest(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void deleteDomain(IAcsClient client, String domainId) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("domainId", domainId);                                  // 【必填】域名
```

`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID` R t R t tB R

```
t("/d i/dltD i")
```

```
        CommonRequest commonRequest = createBaseRequest("/domain/deleteDomain");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询所有域名
`*/`

```java
    private static void listAllDomains(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/domain/listAllDomains");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**协议类型说明**

| protocol | 说明 |
|---|---|
| HTTP | HTTP协议，无需证书。 |
| HTTPS | HTTPS协议，需绑定SSL证书。 |

**客户端认证类型说明**

| clientAuth | 说明 |
|---|---|
| 0 | 无客户端认证。 |
| 1 | 开启双向认证。 |

**响应码说明**

| 55 | > 文档版本：2026072 |
|---|---|

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-路由插件管理

**概述**

路由插件管理模块提供路由级别的插件配置功能。插件可以为路由添加额外功能，如请求/响应处理、认证、 日志等。
**适用引擎**：仅 SCG （Higress引擎不支持此接口，请使用策略配置模块）
**API****路径前缀**： `/route`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建路由插件**

**接口说明**

为路由创建插件配置。

**重要**

仅适用于SCG引擎。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/createRoutePlugin |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| routeId | String | 是 | 路由ID。 |
| pluginId | String | 是 | 插件ID（需先查询插件列表）。 |
| pluginName | String | 是 | 插件名称。 |
| pluginConfig | Object | 是 | 插件配置（JSON格式）。 |
| isOpen | Boolean | 否 | 是否启用，默认为true。 |

**查询路由插件列表**

**接口说明**

查询路由下的插件列表。

**重要**

仅适用于SCG引擎。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/listRoutePlugins |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |

| routeId | String | 是 | 路由ID。 |
|---|---|---|---|
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |

**修改路由插件**

**接口说明**

修改路由的插件配置。

**重要**

仅适用于SCG引擎。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/modifyRoutePlugin |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| routeId | String | 是 | 路由ID。 |
| routePluginId | String | 是 | 路由插件ID。 |
| pluginConfig | Object | 是 | 新的插件配置。 |

**修改路由插件状态**

**接口说明**

启用或禁用路由插件。

**重要**

仅适用于SCG引擎。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /route/modifyRoutePluginStatus |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| routeId | String | 是 | 路由ID。 |
| routePluginId | String | 是 | 路由插件ID。 |
| isOpen | Boolean | 是 | true：启用 false：禁用 |

**删除路由插件**

**接口说明**

删除路由的插件配置。

**重要**

仅适用于SCG引擎。

**请求信息**

| 项目 | 内容 |
|---|---|

| URL | /route/deleteRoutePlugin |
|---|---|
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| routeId | String | 是 | 路由ID。 |
| routePluginId | String | 是 | 路由插件ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用路由插件管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class RoutePluginApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-h****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    private static final String ROUTE_ID = "your-route-id";
```

```java
    private static final String PLUGIN_ID = "your-plugin-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 创建路由插件 `==========`

```
        String routePluginId = createRoutePlugin(client);
```

`// ==========` 查询路由插件列表 `==========`

```
        listRoutePlugins(client);
```

`// ==========` 修改路由插件 `==========`

```
        modifyRoutePlugin(client, routePluginId);
```

`// ==========` 修改路由插件状态 `==========`

```
        modifyRoutePluginStatus(client, routePluginId, false);
```

`// ==========` 删除路由插件 `==========`

```java
        deleteRoutePlugin(client, routePluginId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
```

```
        return request;
    }
    /**
```

* 创建路由插件
`*/`

```java
    private static String createRoutePlugin(IAcsClient client) throws Exception {
```

`//` 插件配置示例（`Header`修改插件）

```
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "custom-value");
        pluginConfig.put("addHeaders", addHeaders);
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeId", ROUTE_ID);                                   // 【必填】路由
```

`ID`

```
        request.put("pluginId", PLUGIN_ID);                                 // 【必填】插件
```

`ID`

```
        request.put("pluginName", "request-header-modifier");               // 【必填】插
```

件名称

```
        request.put("pluginConfig", pluginConfig);                          // 【必填】插
```

件配置

```
        request.put("isOpen", true);                                        // 【可选】是否
```

启用

```java
        CommonRequest commonRequest = createBaseRequest("/route/createRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String routePluginId = result.getString("data");
            System.out.println("createRoutePlugin success, routePluginId: " +
routePluginId);
            return routePluginId;
        } else {
            System.out.println("createRoutePlugin failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询路由插件列表
`*/`

```java
    private static void listRoutePlugins(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeId", ROUTE_ID);                                   // 【必填】路由
```

`ID` `ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        CommonRequest commonRequest = createBaseRequest("/route/listRoutePlugins");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改路由插件
`*/`

```java
    private static void modifyRoutePlugin(IAcsClient client, String routePluginId) thro
ws Exception {
        Map<String, Object> pluginConfig = new HashMap<>();
        Map<String, Object> addHeaders = new HashMap<>();
        addHeaders.put("X-Custom-Header", "new-value");
        pluginConfig.put("addHeaders", addHeaders);
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeId", ROUTE_ID);                                   // 【必填】路由
```

`ID`

```
        request.put("routePluginId", routePluginId);                        // 【必填】路
```

由插件`ID`

```
        request.put("pluginConfig", pluginConfig);                          // 【必填】新
```

的插件配置

```
        CommonRequest commonRequest = createBaseRequest("/route/modifyRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改路由插件状态
`*/`

```java
    private static void modifyRoutePluginStatus(IAcsClient client, String
routePluginId, boolean isOpen) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeId", ROUTE_ID);                                   // 【必填】路由
```

`ID` `//`【必填】路

```
requestput("routePluginId" routePluginId);
```

```
        request.put(routePluginId, routePluginId);                        // 【必填】路
```

由插件`ID`

```
        request.put("isOpen", isOpen);                                      // 【必填】tru
```

e启用，`false`禁用

```java
        CommonRequest commonRequest =
createBaseRequest("/route/modifyRoutePluginStatus");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyRoutePluginStatus: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除路由插件
`*/`

```java
    private static void deleteRoutePlugin(IAcsClient client, String routePluginId) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("routeId", ROUTE_ID);                                   // 【必填】路由
```

`ID`

```
        request.put("routePluginId", routePluginId);                        // 【必填】路
```

由插件`ID`

```
        CommonRequest commonRequest = createBaseRequest("/route/deleteRoutePlugin");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**注意事项**

路由插件仅适用于SCG引擎，Higress引擎请使用策略配置模块。 创建路由插件前需先查询插件列表获取有效的 `pluginId` 。 插件配置格式因插件类型不同而异。

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |

| 400 | 参数错误。 |
|---|---|
| 403 | 权限不足。 |
| 500 | 服务器内部错误。 |

#### API 调用-证书管理

**概述**

证书管理模块提供SSL/TLS证书的增删改查功能。证书用于HTTPS域名配置，支持服务端证书和CA证书。
**适用引擎**：SCG / Higress （不区分引擎，接口通用）
**API****路径前缀**： `/certificate`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，
并使用有效的 AK/SK。

**创建证书**

**接口说明**

创建一个SSL/TLS证书。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /certificate/createCertificate |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| name | String | 是 | 证书名称。 |

| certType | Integer | 是 | 证书类型： 0：服务端证书 1：CA证书 |
|---|---|---|---|
| cert | String | 是 | 证书内容（PEM格式）。 |
| key | String | 条件必填 | 私钥内容。 说明服务端证书时必填。 |

**查询证书列表**

**接口说明**

分页查询证书列表。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /certificate/listCertificates |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |
| current | Integer | 是 | 当前页码，从1开始。 |
| size | Integer | 是 | 每页条数。 |
| name | String | 否 | 证书名称（模糊搜索）。 |
| certType | Integer | 否 | 证书类型筛选。 |

**查询证书详情**

**接口说明**

根据证书ID查询详细信息。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /certificate/getCertificate |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| certificateId | String | 是 | 证书ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**修改证书**

**接口说明**

修改已存在的证书配置。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /certificate/modifyCertificate |
| Method | POST |
| Content-Type | application/json |

**请求参数**

与创建证书参数相同，额外需要指定 `certificateId` 。

**删除证书**

**接口说明**

删除指定的证书。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /certificate/deleteCertificate |
| Method | POST |
| Content-Type | application/json |

**请求参数**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| certificateId | String | 是 | 证书ID。 |
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用证书管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class CertificateApiDemo {
```

`// ==========` 环境配置（根据实际环境修改） `==========`

```java
    private static final boolean IS_SELF_HOSTED = true;
    private static final String SELF_HOSTED_ENDPOINT = "127.0.0.1:8080";
    private static final String ENTERPRISE_ENDPOINT = "csb.cn-****.aliyuncs.com";
    private static final String ACCESS_KEY_ID = "your-access-key-id";
```

```java
    private static final String ACCESS_KEY_SECRET = "your-access-key-secret";
    private static final String ORGANIZATION_ID = "your-org-id";
    private static final String GW_INSTANCE_ID = "your-gw-instance-id";
    public static void main(String[] args) throws Exception {
        IAcsClient client = createClient();
```

`// ==========` 创建服务端证书 `==========`

```
        String certId = createServerCertificate(client);
        // ========== 创建CA证书 ==========
        // String caCertId = createCACertificate(client);
```

`// ==========` 查询证书列表 `==========`

```
        listCertificates(client);
```

`// ==========` 查询证书详情 `==========`

```java
        getCertificate(client, certId);
        // ========== 删除证书 ==========
        deleteCertificate(client, certId);
    }
    private static IAcsClient createClient() {
        if (IS_SELF_HOSTED) {
            DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-");
            return new DefaultAcsClient(profile);
        } else {
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou",
ACCESS_KEY_ID, ACCESS_KEY_SECRET);
            return new DefaultAcsClient(profile);
        }
    }
    private static String getEndpoint() {
        return IS_SELF_HOSTED ? SELF_HOSTED_ENDPOINT : ENTERPRISE_ENDPOINT;
    }
    private static void setAuthHeaders(CommonRequest request) {
        if (IS_SELF_HOSTED) {
            request.putHeadParameter("X-CSB-TOKEN", "csb@2022");
            request.putHeadParameter("X-CSB-OPENAPI", "true");
        } else {
            request.putHeadParameter("x-acs-organizationid", ORGANIZATION_ID);
            request.putHeadParameter("x-acs-caller-sdk-source", "OpenApiDemo");
        }
    }
    private static CommonRequest createBaseRequest(String uriPattern) {
        CommonRequest request = new CommonRequest();
        request.setSysDomain(getEndpoint());
        request.setSysUriPattern(uriPattern);
        request.setSysMethod(MethodType.POST);
```

t `tS` P d

```
t("
```

b `")`

```
        request.setSysProduct("csb-cop");
        request.setSysVersion("2023-02-06");
        setAuthHeaders(request);
        return request;
    }
    /**
```

* 创建服务端证书
`*/`

```java
    private static String createServerCertificate(IAcsClient client) throws Exception {
```

`// PEM`格式的证书内容（实际使用时替换为真实证书）

```
        String certContent = "-----BEGIN CERTIFICATE-----\n" +
                "**********************" +
                "-----END CERTIFICATE-----";
        String keyContent = "-----BEGIN PRIVATE KEY-----\n" +
                "**********************\n" +
                "-----END PRIVATE KEY-----";
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "my-server-cert");                              // 【必填】证书
```

名称

```
        request.put("certType", 0);                                         // 【必填】证书
```

类型：`0-`服务端证书

```
        request.put("cert", certContent);                                   // 【必填】证书
```

内容（`PEM`格式）

```
        request.put("key", keyContent);                                     // 【必填】私钥
```

内容（服务端证书必填）

```java
        CommonRequest commonRequest =
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createServerCertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createServerCertificate failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 创建`CA`证书
`*/`

```
privatestaticStringcreateCACertificate(IAcsClientclient)throwsException{
```

```java
    private static String createCACertificate(IAcsClient client) throws Exception {
        String caCertContent = "-----BEGIN CERTIFICATE-----\n" +
                "MIIBkTCB+wIJAKHHCgVZUffVMA0GCSqGSIb3DQEBCwUAMBExDzANBglghkgBZQME\n" +
                "-----END CERTIFICATE-----";
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "my-ca-cert");                                  // 【必填】证书
```

名称

```
        request.put("certType", 1);                                         // 【必填】证书
```

类型：`1-CA`证书

```
        request.put("cert", caCertContent);                                 // 【必填】证书
```

内容（`PEM`格式）

```java
        CommonRequest commonRequest =
createBaseRequest("/certificate/createCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String certId = result.getString("data");
            System.out.println("createCACertificate success, certId: " + certId);
            return certId;
        } else {
            System.out.println("createCACertificate failed: " +
result.getString("msg"));
            return null;
        }
    }
    /**
```

* 查询证书列表
`*/`

```java
    private static void listCertificates(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("current", 1);                                          // 【必填】当前
```

页码

```
        request.put("size", 10);                                            // 【必填】每页
```

条数

```
        // request.put("name", "");                                            // 【可选】
```

证书名称（模糊搜索）

```
        // request.put("certType", 1);                                         // 【可选】
```

证书类型筛选

```
        CommonRequest commonRequest =
createBaseRequest("/certificate/listCertificates");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

o

```
atype.JSO);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 查询证书详情
`*/`

```java
    private static void getCertificate(IAcsClient client, String certificateId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 【必填】证
```

书`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest = createBaseRequest("/certificate/getCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 修改证书
`*/`

```java
    private static void modifyCertificate(IAcsClient client, String certificateId) thro
ws Exception {
        String certContent = "-----BEGIN CERTIFICATE-----\n...新证书内容...\n-----END
CERTIFICATE-----";
        String keyContent = "-----BEGIN PRIVATE KEY-----\n...新私钥内容...\n-----END PRIVA
TE KEY-----";
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 【必填】证
```

书`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        request.put("name", "my-server-cert-modified");                     // 【必填】证
```

书名称

```
        request.put("certType", 1);                                         // 【必填】证书
```

类型

```
        request.put("cert", certContent);                                   // 【必填】证书
```

内容

```
        request.put("key", keyContent);                                     // 【必填】私钥
```

内容

```
        CommonRequest commonRequest =
createBaseRequest("/certificate/modifyCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
```

```
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 删除证书
`*/`

```java
    private static void deleteCertificate(IAcsClient client, String certificateId) thro
ws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("certificateId", certificateId);                        // 【必填】证
```

书`ID`

```
        request.put("gwInstanceId", GW_INSTANCE_ID);                        // 【必填】网
```

关实例`ID`

```
        CommonRequest commonRequest =
createBaseRequest("/certificate/deleteCertificate");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
}
```

**证书类型说明**

| certType | 类型名称 | 说明 |
|---|---|---|
| 0 | 服务器证书 | 用于HTTPS域名，需提供证书和私钥。 |
| 1 | CA证书 | 用于双向TLS认证。 |

**响应码说明**

| code | 说明 |
|---|---|
| 200 | 成功。 |
| 400 | 参数错误。 |

| 403 | 权限不足。 |
|---|---|
| 500 | 服务器内部错误。 |

## API 网关

### 集群管理

#### ListClusters

查询集群列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| clusterNa me | Strin g | Body | 否 | my-cluster | 集群名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| -- k8sClusterCod e | String | k8s-cluster-001 | Kubernetes集群编码 |
| -- k8sClusterNa me | String | production-cluster | Kubernetes集群名称 |
| --masterUrl | String | https://k8s- master.example.co m:6443 | Master节点URL |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- k8sClusterStat us | Integer | 1 | Kubernetes集群状态 |
| -- k8sClusterStat usDesc | String | 运行中 | Kubernetes集群状态描述 |
| -- k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | Kubernetes集群导入时间 |
| -- k8sClusterTyp e | String | ACK | Kubernetes集群类型 |
| -- k8sClusterAttri bute | Struct | {} | Kubernetes集群属性 |
| ---csClusterId | String | c-123456abcdef | 容器服务集群ID |
| --- csClusterNam e | String | prod-k8s-cluster | 容器服务集群名称 |
| ---slbType | String | alb | 负载均衡器类型 |
| ---vpcId | String | vpc-bp1234567890 | VPC网络ID |
| ---mappingIP | String | 10.0.0.1 | 映射IP地址 |
| ---mappingPort | Integer | 8080 | 映射端口 |
| ---tunnelName | String | vpn-tunnel-001 | 通道名称 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |
| -size | Integer | 100 | 大小 |

#### GetK8sClusterInfoByGwInstanceId

查询根据网关实例ID查询Kubernetes集群信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| - k8sClusterCod e | String | k8s-cluster-001 | Kubernetes集群编码 |
| - k8sClusterNa me | String | production-cluster | Kubernetes集群名称 |
| -masterUrl | String | https://k8s- master.example.co m:6443 | Master节点URL |
| - k8sClusterStat us | Integer | 1 | Kubernetes集群状态 |
| - k8sClusterStat usDesc | String | 运行中 | Kubernetes集群状态描述 |
| - k8sClusterImp ortDateTime | String | 2024-10-14 10:00:00 | Kubernetes集群导入时间 |

#### GetK8sClusterName

查询Kubernetes集群名称。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ImportCluster

导入集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configCon tent | Strin g | Body | 否 | key=value | 配置内容 |
| k8sCluster Name | Strin g | Body | 否 | production-cluster | Kubernetes集群名称 |
| k8sCluster Type | Strin g | Body | 否 | ACK | Kubernetes集群类型 |
| k8sCluster Attribute | Json | Body | 否 | {} | Kubernetes集群属性 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### UpdateCluster

更新集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| clusterCo de | Strin g | Body | 否 | cluster-001 | 集群编码 |
| k8sCluster Attribute | Strin g | Body | 否 | {} | Kubernetes集群属性 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### CancelImportCluster

取消导入集群。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| k8sCluster Code | Strin g | Body | 否 | k8s-cluster-001 | Kubernetes集群编码 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Map | {} | 数据 |

#### CheckConnectCluster

检查集群连接状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configCon tent | Strin g | Body | 否 | key=value | 配置内容 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -connectStatus | Integer | 1 | 连接状态 |
| - connectStatus Desc | String | 已连接 | 连接状态描述 |

#### ListK8sAllNamespaces

查询Kubernetes所有命名空间列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| clusterCo de | Strin g | Body | 否 | cluster-001 | 集群编码 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### ListAllNamespaces

查询所有命名空间列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -namespaceId | String | ns-abc123 | 命名空间ID |
| - namespaceNa me | String | 生产环境 | 命名空间名称 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

### 实例管理

#### ListInstances

查询实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| name | Strin g | Body | 否 | my-resource | 名称 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| deployMo de | Strin g | Body | 否 | rolling | 部署模式 |
| status | Integ er | Body | 否 | 1 | 状态 |
| brokerEng ineType | Strin g | Body | 否 | RocketMQ | 消息引擎类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --accessMode | Array | [] | 接入模式列表 |
| ---ips | String | [] | IP地址列表 |
| ---ports | String | [] | 端口列表 |
| ---externalIps | String | [] | 外部IP列表 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| ---clusterIp | String | [] | 集群IP列表 |
| --- accessModeTy pe | String | public | 接入模式类型 |
| --- loadBalancerN etworkType | String | public | 负载均衡网络类型 |
| --- loadBalancerA ddressType | String | internet | 负载均衡地址类型 |
| --- serviceName | String | user-service | 服务名称 |
| --edasAppInfos | Array | [] | EDAS应用信息列表 |
| ---appId | String | 12345678 | 应用ID |
| --- edasNamespa ceId | String | edas-ns-001 | EDAS命名空间ID |
| ---k8sClusterId | String | c-abc123def456 | Kubernetes集群ID |
| --- k8sNamespac e | String | default | Kubernetes命名空间 |
| --status | Integer | 1 | 状态 |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --name | String | my-resource | 名称 |
| -- instanceName | String | instance-001 | 实例名称 |
| -- deployCluster Namespace | String | production | 部署集群命名空间 |
| -- deployCluster Code | String | deploy-cluster-001 | 部署集群编码 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- deployCluster Name | String | 生产集群 | 部署集群名称 |
| -- k8sServiceNa me | String | my-service | Kubernetes服务名称 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --modifyTime | String | 2024-10-14 12:30:00 | 修改时间 |
| --tid | String | t-123456789 | 任务ID |
| --vpcId | String | vpc-bp1234567890 | VPC网络ID |
| --regionId | String | cn-hangzhou | 地域ID |
| --zoneId | String | cn-hangzhou-b | 可用区ID |
| --deployMode | String | rolling | 部署模式 |
| --edasAppId | String | edas-app-123456 | EDAS应用ID |
| -- edasNamespa ceId | String | edas-ns-001 | EDAS命名空间ID |
| --k8sClusterId | String | c-abc123def456 | Kubernetes集群ID |
| -- k8sNamespac e | String | default | Kubernetes命名空间 |
| -- instanceClass | String | ecs.g6.large | 实例规格 |
| --department | String | 技术部 | 部门 |
| -- resourceGroup | String | rg-default | 资源组 |
| -- ingressClassN ame | String | nginx | Ingress类名 |

| ·API |  |  | API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- brokerEngineT ype | String | RocketMQ | 消息引擎类型 |
| -- brokerEngineV ersion | String | 5.0 | 消息引擎版本 |
| -- brokerLatestE ngineVersion | String | 5.1.0 | 消息引擎最新版本 |
| -- deployCluster Attribute | String | {"zone":"cn- hangzhou-a"} | 部署集群属性 |
| --nodeNumber | Integer | 5 | 节点数量 |
| -- sharedInstanc e | Boolean | false | 是否共享实例 |
| -- sharedInstanc eSource | String | aliyun | 共享实例来源 |
| --vSwitchId | String | vsw- bp1234567890 | 虚拟交换机ID |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |
| -size | Integer | 100 | 大小 |

#### ListAllInstances

查询所有实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -accessMode | Array | [] | 接入模式列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ips | String | [] | IP地址列表 |
| --ports | String | [] | 端口列表 |
| --externalIps | String | [] | 外部IP列表 |
| --clusterIp | String | [] | 集群IP列表 |
| -- accessModeTy pe | String | public | 接入模式类型 |
| -- loadBalancerN etworkType | String | public | 负载均衡网络类型 |
| -- loadBalancerA ddressType | String | internet | 负载均衡地址类型 |
| --serviceName | String | user-service | 服务名称 |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -name | String | my-resource | 名称 |
| -status | Integer | 1 | 状态 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### ListInstancesByServiceId

查询实例列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -serviceStruct | Map | {} | 服务结构 |
| -instanceList | Map | {} | 实例列表 |

#### GetInstanceInfo

查询实例信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -accessMode | Array | [] | 接入模式列表 |
| --ips | String | [] | IP地址列表 |
| --ports | String | [] | 端口列表 |
| --externalIps | String | [] | 外部IP列表 |
| --clusterIp | String | [] | 集群IP列表 |
| -- accessModeTy pe | String | public | 接入模式类型 |
| -- loadBalancerN etworkType | String | public | 负载均衡网络类型 |
| -- loadBalancerA ddressType | String | internet | 负载均衡地址类型 |
| --serviceName | String | user-service | 服务名称 |
| -edasAppInfos | Array | [] | EDAS应用信息列表 |
| --appId | String | 12345678 | 应用ID |
| -- edasNamespa ceId | String | edas-ns-001 | EDAS命名空间ID |
| --k8sClusterId | String | c-abc123def456 | Kubernetes集群ID |
| -- k8sNamespac e | String | default | Kubernetes命名空间 |
| -status | Integer | 1 | 状态 |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -name | String | my-resource | 名称 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - instanceName | String | instance-001 | 实例名称 |
| - deployCluster Namespace | String | production | 部署集群命名空间 |
| - deployCluster Code | String | deploy-cluster-001 | 部署集群编码 |
| - deployCluster Name | String | 生产集群 | 部署集群名称 |
| - k8sServiceNa me | String | my-service | Kubernetes服务名称 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -modifyTime | String | 2024-10-14 12:30:00 | 修改时间 |
| -tid | String | t-123456789 | 任务ID |
| -vpcId | String | vpc-bp1234567890 | VPC网络ID |
| -regionId | String | cn-hangzhou | 地域ID |
| -zoneId | String | cn-hangzhou-b | 可用区ID |
| -deployMode | String | rolling | 部署模式 |
| -edasAppId | String | edas-app-123456 | EDAS应用ID |
| - edasNamespa ceId | String | edas-ns-001 | EDAS命名空间ID |
| -k8sClusterId | String | c-abc123def456 | Kubernetes集群ID |
| - k8sNamespac e | String | default | Kubernetes命名空间 |
| -instanceClass | String | ecs.g6.large | 实例规格 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -department | String | 技术部 | 部门 |
| - resourceGroup | String | rg-default | 资源组 |
| - ingressClassN ame | String | nginx | Ingress类名 |
| - brokerEngineT ype | String | RocketMQ | 消息引擎类型 |
| - brokerEngineV ersion | String | 5.0 | 消息引擎版本 |
| - brokerLatestE ngineVersion | String | 5.1.0 | 消息引擎最新版本 |
| - deployCluster Attribute | String | {"zone":"cn- hangzhou-a"} | 部署集群属性 |
| -nodeNumber | Integer | 5 | 节点数量 |
| - sharedInstanc e | Boolean | false | 是否共享实例 |
| - sharedInstanc eSource | String | aliyun | 共享实例来源 |
| -vSwitchId | String | vsw- bp1234567890 | 虚拟交换机ID |

#### CreateInstance

创建实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eName | Strin g | Body | 否 | 生产网关实例 | 网关实例名称 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| clusterCo de | Strin g | Body | 否 | cluster-001 | 集群编码 |
| deployCon figContent | Strin g | Body | 否 | replicas: 3 image: nginx:latest | 部署配置内容 |
| accessMo deConfigC ontent | Strin g | Body | 否 | mode: public enabled: true | 接入模式配置内容 |
| namespac e | Strin g | Body | 否 | prod-ns | 命名空间 |
| vpcId | Strin g | Body | 否 | vpc-bp1234567890 | VPC网络ID |
| vswId | Strin g | Body | 否 | vsw-1234567890 | 交换机ID |
| ingressNa me | Strin g | Body | 否 | my-ingress | Ingress名称 |
| brokerEng ineType | Strin g | Body | 否 | RocketMQ | 消息引擎类型 |
| instanceCl ass | Strin g | Body | 否 | ecs.g6.large | 实例规格 |
| instanceN umber | Strin g | Body | 否 | INS20240101001 | 实例编号 |
| o11y | Json | Body | 否 | {"enabled":true,"metrics ":"prometheus"} | 可观测性配置 |
| deployMo de | Strin g | Body | 否 | rolling | 部署模式 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### AscmCreateInstance

创建实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eName | Strin g | Body | 否 | 生产网关实例 | 网关实例名称 |
| clusterCo de | Strin g | Body | 否 | cluster-001 | 集群编码 |
| instanceN umber | Strin g | Body | 否 | INS20240101001 | 实例编号 |
| instanceCl ass | Strin g | Body | 否 | ecs.g6.large | 实例规格 |
| vpcId | Strin g | Body | 否 | vpc-bp1234567890 | VPC网络ID |
| backupZo neId | Strin g | Body | 否 | cn-hangzhou-h | 备份可用区ID |
| backupVS witchId | Strin g | Body | 否 | vsw-bp1234567890 | 备份虚拟交换机ID |
| thirdZoneI d | Strin g | Body | 否 | cn-hangzhou-c | 第三可用区ID |
| thirdVSwit chId | Strin g | Body | 否 | vsw-third-001 | 第三可用区交换机ID |
| zoneType | Strin g | Body | 否 | primary | 可用区类型 |
| uid | Strin g | Body | 否 | user-1234567890 | 用户ID |
| deployMo de | Strin g | Body | 否 | rolling | 部署模式 |
| edasNam espaceId | Strin g | Body | 否 | edas-ns-001 | EDAS命名空间ID |
| k8sCluster Id | Strin g | Body | 否 | c-abc123def456 | Kubernetes集群ID |
| k8sNames pace | Strin g | Body | 否 | default | Kubernetes命名空间 |
| edasAppIn fos | Repe atList | Body | 否 | [] | EDAS应用信息列表 |
| -appId | Strin g | Body | 否 | 12345678 | 应用ID |

| 开发指南·API 网 | 关 |  |  |  | API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| - edasNam espaceId | Strin g | Body | 否 | edas-ns-001 | EDAS命名空间ID |
| - k8sCluster Id | Strin g | Body | 否 | c-abc123def456 | Kubernetes集群ID |
| - k8sNames pace | Strin g | Body | 否 | default | Kubernetes命名空间 |
| deployCon figContent | Strin g | Body | 否 | replicas: 3 image: nginx:latest | 部署配置内容 |
| accessMo deConfigC ontent | Strin g | Body | 否 | mode: public enabled: true | 接入模式配置内容 |
| namespac e | Strin g | Body | 否 | prod-ns | 命名空间 |
| brokerEng ineType | Strin g | Body | 否 | RocketMQ | 消息引擎类型 |
| ingressCla ssName | Strin g | Body | 否 | nginx | Ingress类名 |
| o11y | Json | Body | 否 | {"enabled":true,"metrics ":"prometheus"} | 可观测性配置 |
| Departme nt | Strin g | Body | 否 | 1 | 部门ID |
| Resource Group | Strin g | Body | 否 | rg-acfmxazb4ph6aiy | 资源组 |
| RegionId | Strin g | Body | 否 | cn-hangzhou | 地域ID |
| ZoneId | Strin g | Body | 否 | cn-hangzhou-a | 可用区ID |
| vSwitchId | Strin g | Body | 否 | vsw-bp1234567890 | 虚拟交换机ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

| A | PI 网关 |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 数据 |

#### ModifyInstance

修改实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| instanceN ame | Strin g | Body | 否 | instance-001 | 实例名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Boolean | {} | 数据 |

#### ModifyInstanceImageUrl

修改实例镜像地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| imageUrl | Strin g | Body | 否 | https://example.com/log o.png | 图片URL |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Boolean | {} | 数据 |

#### UpgradeInstance

升级实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### DeleteInstance

删除实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

| PI |  |  |  |  | ·API |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| forcedDel ete | Boole an | Body | 否 | false | 是否强制删除 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### RestartInstance

重启实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### StopInstance

停止实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Boolean | {} | 数据 |

#### RefreshInstance

刷新实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eCode | Strin g | Body | 否 | gw-instance-001 | 网关实例编码 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -accessMode | Array | [] | 接入模式列表 |
| --ips | String | [] | IP地址列表 |
| --ports | String | [] | 端口列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --externalIps | String | [] | 外部IP列表 |
| --clusterIp | String | [] | 集群IP列表 |
| -- accessModeTy pe | String | public | 接入模式类型 |
| -status | Integer | 1 | 状态 |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -name | String | my-resource | 名称 |
| - deployCluster Namespace | String | production | 部署集群命名空间 |
| - deployCluster Code | String | deploy-cluster-001 | 部署集群编码 |
| - deployCluster Name | String | 生产集群 | 部署集群名称 |
| - k8sServiceNa me | String | my-service | Kubernetes服务名称 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -modifyTime | String | 2024-10-14 12:30:00 | 修改时间 |
| -tid | String | t-123456789 | 任务ID |

#### CreateInstanceDeployConfig

创建实例部署配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuReque st | Strin g | Body | 否 | 1000m | CPU请求 |
| cpuLimit | Strin g | Body | 否 | 2000m | CPU限制 |
| memoryR equest | Strin g | Body | 否 | 512Mi | 内存请求 |
| memoryLi mit | Strin g | Body | 否 | 1Gi | 内存限制 |
| replicas | Integ er | Body | 否 | 3 | 副本数 |
| jvmArgs | Strin g | Body | 否 | -Xms512m -Xmx1024m | JVM参数 |
| gwInstanc eName | Strin g | Body | 否 | 生产网关实例 | 网关实例名称 |
| accessMo deType | Strin g | Body | 否 | public | 接入模式类型 |
| ports | Repe atList | Body | 否 | [] | 端口列表 |
| -port | Integ er | Body | 否 | 8080 | 端口号 |
| - targetPort | Strin g | Body | 否 | 8080 | 目标端口 |
| -nodePort | Integ er | Body | 否 | 30080 | 节点端口 |
| -name | Strin g | Body | 否 | my-resource | 名称 |
| -protocol | Strin g | Body | 否 | HTTP | 协议 |
| namespac e | Strin g | Body | 否 | prod-ns | 命名空间 |
| externalTr afficPolicy | Strin g | Body | 否 | Local | 外部流量策略 |
| ipType | Strin g | Body | 否 | IPv4 | IP类型 |
| vpcId | Strin g | Body | 否 | vpc-bp1234567890 | VPC网络ID |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| vswId | Strin g | Body | 否 | vsw-1234567890 | 交换机ID |
| uid | Strin g | Body | 否 | user-1234567890 | 用户ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| - deployConfigY amlStr | String | apiVersion: apps/v1 kind: Deployment | 部署配置YAML字符串 |
| - accessModeCo nfigYamlStr | String | mode: public enabled: true | 接入模式配置YAML字符串 |

#### GetInstanceDeployDeployConfig

查询实例部署配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 数据 |

#### GetInstanceDeployMsg

查询实例部署消息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| - accessModeLis t | Array | [] | 接入模式列表 |
| -- intranetUrlStrL ist | String | [] | 内网URL列表 |
| -- networkUrlStrL ist | String | [] | 网络URL列表 |
| --name | String | my-resource | 名称 |
| --type | String | 1 | 类型 |
| -podInfoList | Array | [] | Pod信息列表 |
| --ipList | Array | [] | IP列表 |

| A | PI 网关 |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---ip | String | 192.168.1.100 | IP地址 |
| ---ipType | String | IPv4 | IP类型 |
| --name | String | my-resource | 名称 |
| --isReady | Boolean | true | 是否就绪 |
| - deploymentNa me | String | app-deployment | 部署名称 |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| - instanceName | String | instance-001 | 实例名称 |
| - engineSpecific ation | String | MSE GTW 16 32 2 _ _ _ _ 00 c _ | 引擎规格 |
| -vpcId | String | vpc-bp1234567890 | VPC网络ID |
| -regionId | String | cn-hangzhou | 地域ID |
| -zoneId | String | cn-hangzhou-b | 可用区ID |
| -vSwitchId | String | vsw- bp1234567890 | 虚拟交换机ID |
| -resConfig | Struct | {} | 响应配置 |
| --cpuRequest | String | 1000m | CPU请求 |
| -- memoryReque st | String | 512Mi | 内存请求 |
| --cpuLimit | String | 2000m | CPU限制 |
| --memoryLimit | String | 1Gi | 内存限制 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --replicas | Integer | 3 | 副本数 |
| --jvmArgs | String | -Xms512m - Xmx1024m | JVM参数 |
| -clusterConfig | Struct | {} | 集群配置 |
| --clusterName | String | my-cluster | 集群名称 |
| --namespace | String | prod-ns | 命名空间 |
| --clusterCode | String | cluster-001 | 集群编码 |

#### GetCustomDeployConfig

查询自定义部署配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| - deploymentYa mlStr | String | apiVersion: apps/v1 kind: Deployment | 部署YAML字符串 |
| - serviceYamlStr | String | apiVersion: v1 kind: Service | 服务YAML字符串 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -jarStr | String | my-service.jar | JAR文件名 |
| -wgetStr | String | wget https://example.co m/file | Wget命令字符串 |

#### GetInstanceAccessModeConfig

查询实例访问模式配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### GetResource

查询实例资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -replicas | Integer | 3 | 副本数 |
| -jvmArgs | String | -Xms512m - Xmx1024m | JVM参数 |
| - instanceName | String | instance-001 | 实例名称 |
| - engineSpecific ation | String | MSE GTW 16 32 2 _ _ _ _ 00 c _ | 引擎规格 |
| -vpcId | String | vpc-bp1234567890 | VPC网络ID |
| -regionId | String | cn-hangzhou | 地域ID |
| -zoneId | String | cn-hangzhou-b | 可用区ID |
| -backupZoneId | String | cn-hangzhou-h | 备份可用区ID |
| - backupVSwitc hId | String | vsw- bp1234567890 | 备份虚拟交换机ID |
| -thirdZoneId | String | cn-hangzhou-c | 第三可用区ID |
| - thirdVSwitchId | String | vsw-third-001 | 第三可用区交换机ID |
| -zoneType | String | primary | 可用区类型 |
| -vSwitchId | String | vsw- bp1234567890 | 虚拟交换机ID |
| -cpuRequest | Struct | 1000m | CPU请求 |
| --amount | String | 100.00 | 金额 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --unit | String | requests/second | 单位 |
| - memoryReque st | Struct | 512Mi | 内存请求 |
| --amount | String | 100.00 | 金额 |
| --unit | String | requests/second | 单位 |
| -cpuLimit | Struct | 2000m | CPU限制 |
| --amount | String | 100.00 | 金额 |
| --unit | String | requests/second | 单位 |
| -memoryLimit | Struct | 1Gi | 内存限制 |
| --amount | String | 100.00 | 金额 |
| --unit | String | requests/second | 单位 |

#### ModifyResource

修改实例资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| replicas | Integ er | Body | 否 | 3 | 副本数 |
| specificati onTempla te | Integ er | Body | 否 | 1 | 规格模板 |
| source | Strin g | Body | 否 | manual | 来源 |

| 开发指南·API 网 | 关 |  |  |  | API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceCl ass | Strin g | Body | 否 | ecs.g6.large | 实例规格 |
| backupZo neId | Strin g | Body | 否 | cn-hangzhou-h | 备份可用区ID |
| backupVS witchId | Strin g | Body | 否 | vsw-bp1234567890 | 备份虚拟交换机ID |
| thirdZoneI d | Strin g | Body | 否 | cn-hangzhou-c | 第三可用区ID |
| thirdVSwit chId | Strin g | Body | 否 | vsw-third-001 | 第三可用区交换机ID |
| zoneType | Strin g | Body | 否 | primary | 可用区类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

### 分组管理

#### ModifyGroup

修改分组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 否 | my-resource | 名称。 |
| basePath | Strin g | Body | 否 | /api/v1 | 基础路径。 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述。 |
| domainIds | Repe atList | Body | 否 | [] | 域名ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | String | {} | 数据。 |

#### CreateGroup

创建分组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| name | Strin g | Body | 否 | my-resource | 名称。 |
| basePath | Strin g | Body | 否 | /api/v1 | 基础路径。 |
| needDefa ultDomain | Boole an | Body | 否 | true | 是否需要默认域名。 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述。 |
| domainIds | Repe atList | Body | 否 | [] | 域名ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | String | {} | 数据。 |

#### ListGroups

查询分组列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID |
| name | Strin g | Body | 否 | my-resource | 名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --domains | Array | [] | 域名列表 |
| ---domainId | String | domain-123456 | 域名ID |
| ---domain | String | api.example.com | 域名 |
| ---protocol | String | HTTP | 协议 |
| ---createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --groupId | String | group-123456 | 分组ID |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --name | String | my-resource | 名称 |
| --basePath | String | /api/v1 | 基础路径 |
| --description | String | 这是一个示例服务 | 描述 |
| -- defaultDomain | String | api.example.com | 默认域名 |
| --editable | Boolean | true | 是否可编辑 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |
| -size | Integer | 100 | 大小 |

#### GetAllGroups

查询所有分组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -domains | Array | [] | 域名列表 |
| --domainId | String | domain-123456 | 域名ID |
| --domain | String | api.example.com | 域名 |
| --protocol | String | HTTP | 协议 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -groupId | String | group-123456 | 分组ID |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -name | String | my-resource | 名称 |
| -basePath | String | /api/v1 | 基础路径 |
| -description | String | 这是一个示例服务 | 描述 |
| - defaultDomain | String | api.example.com | 默认域名 |
| -editable | Boolean | true | 是否可编辑 |

| A | PI 网关 |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetGroup

查询分组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -domains | Array | [] | 域名列表 |
| --domainId | String | domain-123456 | 域名ID |
| --domain | String | api.example.com | 域名 |
| --protocol | String | HTTP | 协议 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -groupId | String | group-123456 | 分组ID |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -name | String | my-resource | 名称 |
| -basePath | String | /api/v1 | 基础路径 |
| -description | String | 这是一个示例服务 | 描述 |
| - defaultDomain | String | api.example.com | 默认域名 |
| -editable | Boolean | true | 是否可编辑 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |

#### DeleteGroup

删除分组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### AddGroupDomain

添加分组域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | gw-cn-wwo36s5y001 | 网关实例ID |
| groupId | Strin g | Body | 否 | 16782 | API分组ID |
| domainIds | Repe atList | Body | 否 | ["3412", "3413"] | 要绑定的域名ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 返回码。200表示成功，其他值表示异常。 |
| msg | String | success | 返回信息。成功时返回'success'，异常时返回错误信息。 |
| data | String | true | 返回数据。操作成功时返回字符串'true'。 |

**示例**

请求示例

```json
{
  "gwInstanceId": "gw-cn-wwo36s5y001",
  "groupId": "16782",
  "domainIds": [
    "3412",
    "3413"
```

]

```
}
```

正常返回示例 `JSON` 格式

```json
{
  "code": 200,
  "msg": "success",
  "data": "true"
}
```

#### DeleteGroupDomain

删除分组域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID |
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

### 路由管理

#### CreateRoute

创建路由。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```json
{
  "gwInstanceId": "string",
  "groupId": "string",
  "serviceId": "string",
  "routeName": "string",
  "routePath": [
    "string"
```

`],`

```json
  "path": {
    "matchType": "string",
    "matchValue": "string",
    "caseSensitive": true
  },
  "openStripPrefix": true,
  "serviceType": "string",
  "serviceIds": [
    {
      "serviceId": "string",
      "weight": 0
    }
```

`],`

```json
  "enableStatus": true,
  "stripPrefix": 0,
  "order": 0,
  "methods": [
    "string"
```

`],`

```json
  "header": [
    {
      "key": "string",
      "value": "string"
    }
```

`],`

```json
  "cookie": [
    {
      "key": "string",
      "value": "string"
    }
```

`],`

```json
  "queryParam": [
    {
      "key": "string",
```

```json
      "value": "string"
    }
```

`],`

```json
  "domainIds": [
    "string"
```

`],`

```json
  "routeId": "string",
  "hsfMethodMappingConfig": {
    "hsfMethod": "string",
    "parameterMappingList": [
      {
        "name": "string",
        "schema": {
          "type": "string",
          "items": "string",
          "array": true,
          "primitive": true,
          "generic": true
        },
        "location": "string",
        "required": true,
        "order": 0
      }
```

]

```
  }
}
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| order | Integ er | Body | 否 | 100 | 排序号。 |
| filters | Strin g | Body | 否 | path=/api/** | 过滤器。 |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID。 |
| routeNam e | Strin g | Body | 否 | user-service-route | 路由名称。 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID。 |
| serviceTy pe | Strin g | Body | 否 | REST | 服务类型。 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| methods | Repe atList | Body | 否 | [] | 请求方法列表。 |

| A | PI 网关 |  |  |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| header | Repe atList | Body | 否 | [] | 请求头列表。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |
| -value | Strin g | Body | 否 | example-value | 值 |
| cookie | Repe atList | Body | 否 | [] | Cookie列表。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |
| -value | Strin g | Body | 否 | example-value | 值 |
| queryPara m | Repe atList | Body | 否 | [] | 查询参数列表。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |
| -value | Strin g | Body | 否 | example-value | 值 |
| domainIds | Repe atList | Body | 否 | [] | 域名ID列表。 |
| routePath | Repe atList | Body | 否 | /api/v1/users | 路由路径。 |
| stripPrefix | Integ er | Body | 否 | 1 | 前缀剥离层级。 |
| requestTi meout | Integ er | Body | 否 | 30000 | 请求超时时间（毫秒）。 |
| openStrip Prefix | Boole an | Body | 否 | true | 是否开启前缀剥离。 |
| enableFor ceNonceC heck | Boole an | Body | 否 | false | 是否强制检查随机数。 |
| path | Json | Body | 否 | /api/v1/resource | 路径。 |
| serviceIds | Repe atList | Body | 否 | [] | 服务ID列表。 |
| -serviceId | Strin g | Body | 否 | service-123456 | 服务ID |

| 开发指南·API 网 | 关 |  |  |  | API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -weight | Integ er | Body | 否 | 100 | 权重 |
| groupId | Strin g | Body | 否 | group-123456 | 分组ID。 |
| enableSta tus | Boole an | Body | 否 | true | 启用状态。 |
| hsfMethod MappingC onfig | Json | Body | 否 | {"method":"invoke","par ams":[]} | HSF方法映射配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | String | {} | 数据。 |

#### BatchDeleteRoute

批量删除路由。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| routeIds | Repe atList | Body | 否 | [] | 路由ID列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 数据。 |
| -successIds | String | [] | 成功ID列表。 |
| -failedIds | String | [] | 失败ID列表。 |

#### ListRoutes

查询路由列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 10 | 分页查询时每页的行数。 |
| current | Integ er | Body | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为 1，表示从第1页开始显示。 |
| routeNam e | Strin g | Body | 否 | demo-route | 路由名称。 |
| serviceNa me | Strin g | Body | 否 | demo-service | 服务名称。 |
| exactServi ceId | Strin g | Body | 否 | 1001 | 指定精确服务ID为1001， 用于唯一标识某一具体服务实例 |
| enableSta tus | Boole an | Body | 否 | true | 开启状态。 |
| gwInstanc eId | Strin g | Body | 否 | i-demo | 网关实例 ID。 |
| routeId | Strin g | Body | 否 | xxx-xxx-xxx-xxx | 路由ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| groupNam e | Strin g | Body | 否 | test | 分组名称。 |
| domainNa me | Strin g | Body | 否 | example.com | 域名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | The Request is not authorization. | 错误信息。 |
| data | Struct | {} | 返回数据。 |
| -records | Array | [] | 返回数据结果记录。 |
| --routePath | String | /reviews/v1 | 路由路径 |
| --domains | String | ["example.com", "www.example.co m"] | 域名名称列表。 |
| --routeId | String | RouteId 1 _ | 路由ID。 |
| --routeName | String | http-route | 路由名称。 |
| --enableStatus | Boolean | true | 是否启用 disable禁用 enable 启用 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --serviceId | String | service-123456 | 服务ID |
| --serviceName | String | user-service | 服务名称 |
| --groupId | String | group-123456 | 分组ID |
| --groupName | String | 默认分组 | 分组名称 |
| --path | Struct | /api/v1/resource | 路径 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---matchType | String | prefix | 匹配类型 |
| ---matchValue | String | /v1/users | 匹配值 |
| --- caseSensitive | Boolean | false | 是否区分大小写 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式

```json
{
 "msg":"",
 "code":"",
 "data":{
  "total":"",
  "current":"",
  "size":"",
  "records":[
   {
    "routePath":"",
    "groupName":"",
    "routeId":"",
    "createTime":"",
    "groupId":"",
    "domains":"",
    "serviceId":"",
    "serviceName":"",
    "enableStatus":"",
    "path":[
     {
      "matchType":"",
      "caseSensitive":"",
      "matchValue":""
     }
```

`],`

```json
    "routeName":""
   }
```

]

```
 }
}
```

#### ListRoutesByAppId

查询路由列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| total | Integ er | Body | 否 | 1000 | 总数 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| routeNam e | Strin g | Body | 否 | user-service-route | 路由名称 |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --routeId | String | route-123456 | 路由ID |
| --routeName | String | user-service-route | 路由名称 |
| --routePath | String | /api/v1/users | 路由路径 |
| --serviceId | String | service-123456 | 服务ID |
| --serviceName | String | user-service | 服务名称 |
| -- serviceProtoco l | String | HTTP | 服务协议 |
| --authId | String | auth 123456 _ | 认证ID |
| --authStatus | Integer | 1 | 认证状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListRoutesByGwInstanceId

查询路由列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -routeId | String | route-123456 | 路由ID |
| -routeName | String | user-service-route | 路由名称 |
| -routePath | String | /api/v1/users | 路由路径 |
| -serviceId | String | service-123456 | 服务ID |
| -serviceName | String | user-service | 服务名称 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - serviceProtoco l | String | HTTP | 服务协议 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetAllRoutePath

查询所有路由路径。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| body | Strin g | Body | 否 | {"key":"value"} | 请求体内容 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 响应码 |
| Msg | String | 操作成功 | 消息 |
| Data | Struct | {} | 数据 |
| -RoutePaths | String | [] | 路由路径列表 |

#### GetRoute

查询路由。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -routePath | String | /api/v1/users | 路由路径 |
| -methods | String | [] | 请求方法列表 |
| -header | Array | [] | 请求头列表 |
| --key | String | api-key-001 | 密钥 |
| --value | String | example-value | 值 |
| -cookie | Array | [] | Cookie列表 |
| --key | String | api-key-001 | 密钥 |
| --value | String | example-value | 值 |
| -queryParam | Array | [] | 查询参数列表 |
| --key | String | api-key-001 | 密钥 |
| --value | String | example-value | 值 |
| -plugins | Array | [] | 插件列表 |

| A | PI 网关 |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --key | String | api-key-001 | 密钥 |
| --value | String | example-value | 值 |
| - sigSchemeDT OList | Array | [] | 签名方案列表 |
| -- sigSchemeStat us | Integer | 1 | 签名方案状态 |
| -- sigSchemeNa me | String | HMAC-SHA256 | 签名方案名称 |
| --sigSchemeId | String | sig-scheme-001 | 签名方案ID |
| --sigAlg | String | SHA256withRSA | 签名算法 |
| --secretKey | String | sk 1234567890abc _ def | 密钥 |
| -domainVO | Array | [] | 域名视图对象列表 |
| --domainId | String | domain-123456 | 域名ID |
| --domain | String | api.example.com | 域名 |
| --protocol | String | HTTP | 协议 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| - groupDomainV O | Array | [] | 分组域名视图对象列表 |
| --domainId | String | domain-123456 | 域名ID |
| --domain | String | api.example.com | 域名 |
| --protocol | String | HTTP | 协议 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| - strategyConfig s | Array | [] | 策略配置列表 |
| --scopes | String | [] | 授权范围列表 |
| -- strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -- strategyConfig Name | String | 默认策略 | 策略配置名称 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --scope | Struct | openid profile | 授权范围 |
| ---scopes | String | [] | 授权范围列表 |
| ---routeInfos | Array | [] | 路由信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---serviceInfos | Array | [] | 服务信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---appInfos | Array | [] | 应用信息列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---domainInfos | Array | [] | 域名信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| --- mcpServerInfo s | Array | [] | MCP服务器信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| -serviceIds | Array | [] | 服务ID列表 |
| -routeId | String | route-123456 | 路由ID |
| -routeName | String | user-service-route | 路由名称 |
| -enableStatus | Boolean | true | 启用状态 |
| - openStripPrefi x | Boolean | true | 是否开启前缀剥离 |
| -stripPrefix | Integer | 1 | 前缀剥离层级 |
| -order | Integer | 100 | 排序号 |
| - routeCreateTi me | String | 2024-10-14 09:00:00 | 路由创建时间 |
| -groupId | String | group-123456 | 分组ID |
| -groupName | String | 默认分组 | 分组名称 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -basePath | String | /api/v1 | 基础路径 |
| -serviceName | String | user-service | 服务名称 |
| -serviceId | String | service-123456 | 服务ID |
| - serviceDescrip tion | String | 用户管理服务 | 服务描述 |
| - upstreamType | Integer | 1 | 上游类型 |
| - upstreamType Name | String | HTTP服务 | 上游类型名称 |
| - loadBalanceTy pe | Integer | 1 | 负载均衡类型 |
| - loadBalanceTy peName | String | 轮询 | 负载均衡类型名称 |
| - serviceCreateT ime | String | 2024-10-14 08:00:00 | 服务创建时间 |
| - isOpenFreeCer t | Boolean | false | 是否开启免费证书 |
| -isOpenTraffic | Boolean | true | 是否开启流量控制 |
| -isOpenMock | Boolean | false | 是否开启Mock |
| - isOpenTimeOu t | Boolean | true | 是否开启超时 |
| - requestTimeo ut | Integer | 30000 | 请求超时时间（毫秒） |
| -isOpenPlugin | Boolean | true | 是否开启插件 |
| -isOpenFuse | Boolean | true | 是否开启熔断 |
| -isOpenSig | Boolean | true | 是否开启签名 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| -isRewrite | Boolean | true | 是否重写 |
|---|---|---|---|
| -isOpenCross | Boolean | true | 是否开启跨域 |
| - isOpenRespon seCache | Boolean | true | 是否开启响应缓存 |
| -serviceType | String | REST | 服务类型 |
| -path | Struct | /api/v1/resource | 路径 |
| --matchType | String | prefix | 匹配类型 |
| --matchValue | String | /v1/users | 匹配值 |
| -- caseSensitive | Boolean | false | 是否区分大小写 |
| -trafficControl | Struct | {} | 流量控制配置 |
| --id | Integer | 123456 | ID |
| --userId | String | uid-123456 | 用户ID |
| --namespace | String | prod-ns | 命名空间 |
| --routeId | String | route-123456 | 路由ID |
| -- resourceMode | Integer | 1 | 资源模式 |
| -- thresholdType | Integer | 1 | 阈值类型 |
| --count | Float | 10.5 | 数量 |
| -- controlBehavio r | Integer | 1 | 流控行为 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --intervalSec | Integer | 30 | 时间间隔（秒） |
| --burst | Integer | 100 | 突发流量上限 |
| -- maxQueueing TimeoutMs | Integer | 5000 | 最大排队超时时间（毫秒） |
| --isRequestAttr | Boolean | false | 是否请求属性 |
| --enable | Boolean | true | 是否启用 |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --attrStr | Struct | {} | 属性结构 |
| ---paramAttr | Integer | 1 | 参数属性 |
| --- paramAttrDeta il | String | query | 参数属性详情 |
| --- isOpenMatch | Integer | 1 | 是否开启匹配 |
| ---matchMode | Integer | 1 | 匹配模式 |
| ---matchString | String | /api/* | 匹配字符串 |
| -- thresholdByQp s | Struct | {} | QPS阈值配置 |
| --- qpsThreshold | Integer | 1000 | QPS阈值 |
| ---timeInterval | Integer | 300 | 时间间隔（秒） |
| ---timeUnit | Integer | 1 | 时间单位 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| --- flowControlMe thod | Integer | 1 | 流控方法 |
|---|---|---|---|
| --- flowControlInf o | Integer | 1 | 流控信息 |
| -- thresholdByTh readVo | Struct | {} | 线程数阈值配置 |
| ---threadNum | Integer | 10 | 线程数 |
| - routeMockCon figVo | Struct | {} | 路由Mock配置 |
| -- responseHead er | String | [] | 响应头列表 |
| --isOpen | Integer | true | 是否开启 |
| -- responseBody | String | {"code":200,"data" :{}} | 响应体 |
| -- responseCode | Integer | 200 | 响应码 |
| - routeFusesCon figVo | Struct | {} | 路由熔断配置 |
| -- routeFusesCon dition | Array | [] | 路由熔断条件列表 |
| ---id | Integer | 123456 | ID |
| ---type | Integer | 1 | 类型 |
| ---operator | String | admin | 操作人 |
| ---judgValue | String | 100 | 判断值 |
| ---errorCount | Float | 5.0 | 错误数量 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---statInterval | Integer | 60 | 统计间隔（秒） |
| ---timeWindow | Integer | 60 | 时间窗口（秒） |
| --- minRequestA mount | Integer | 10 | 最小请求数量 |
| --- halfOpenBase AmountPerSte p | Integer | 5 | 半开状态每步基础请求数 |
| --- halfOpenReco veryStepNum | Integer | 3 | 半开状态恢复步骤数 |
| --resourceId | String | res-abc123 | 资源ID |
| -- combinedCond ition | String | A AND B | 组合条件表达式 |
| -- degradeStrate gy | Integer | 1 | 降级策略 |
| --fuseMock | Struct | {} | 熔断Mock配置 |
| --- responseHead er | String | [] | 响应头列表 |
| ---isOpen | Integer | true | 是否开启 |
| --- responseBody | String | {"code":200,"data" :{}} | 响应体 |
| --- responseCode | Integer | 200 | 响应码 |
| -routeAuthVO | Struct | {} | 路由认证配置 |
| -- requestHeader | String | Content-Type | 请求头 |
| --authType | Integer | jwt | 认证类型 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- appCodeAuthT ype | String | oauth2 | 应用编码认证类型 |
| --customAuth | Struct | {} | 自定义认证配置 |
| --- authRequestH eader | String | [] | 认证请求头列表 |
| --- authResponse Header | String | [] | 认证响应头列表 |
| --- authServerHos t | String | auth.example.com | 认证服务器主机 |
| --- authServerUri | String | /oauth/token | 认证服务器URI |
| ---authTimeout | Integer | 30000 | 认证超时时间（毫秒） |
| ---keepAlive | Integer | 60 | 保持连接时间（秒） |
| --- tokenExpiratio n | Integer | 7200 | 令牌过期时间（秒） |
| --- authAssertTyp e | String | header | 认证断言类型 |
| --- authAssertVal ue | String | Bearer token | 认证断言值 |
| --- openLoosePatt ern | Boolean | false | 是否开启宽松模式 |
| --- cachedClient | Map | {} | 缓存的客户端信息 |
| --apiKey | Struct | {} | API密钥配置 |
| --- enableInHead er | Boolean | true | 是否在请求头中启用 |
| --- enableInQuery | Boolean | true | 是否在查询参数中启用 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---apiKeyName | String | my-api-key | API密钥名称 |
| --- enableRmPara m | Boolean | false | 是否启用移除参数 |
| --- enableOptions FreeAuth | Boolean | true | 是否启用OPTIONS请求免认证 |
| -crossConfig | Struct | {} | 跨域配置 |
| -- allowedMetho ds | String | [] | 允许的请求方法列表 |
| --isOpenCross | Boolean | true | 是否开启跨域 |
| --crossType | String | CORS | 跨域类型 |
| -- allowedOrigins | String | * | 允许的来源域名 |
| -- exposedHeade rs | String | X-Custom- Header,X-Request- Id | 暴露的响应头 |
| -- allowedHeader s | String | Content- Type,Authorization | 允许的请求头 |
| -- allowedCreden tials | Boolean | true | 是否允许凭证 |
| --maxAge | Integer | 3600 | 最大缓存时间（秒） |
| --callbackFunc | String | handleCallback | 回调函数名称 |
| - responseCach eConfig | Struct | {} | 响应缓存配置 |
| -- routeInterface List | Array | [] | 路由接口列表 |
| ---method | String | GET | 请求方法 |
| ---headers | String | Content-Type: application/json | 请求头 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| ---path | String | /api/v1/resource | 路径 |
|---|---|---|---|
| --- queryParams | String | page=1&size=10 | 查询参数字符串 |
| --maxAge | Integer | 3600 | 最大缓存时间（秒） |
| -- isOpenCacheC ontrol | Boolean | true | 是否开启缓存控制 |
| -- allowedStatus Code | String | 200,201,204 | 允许的状态码 |
| -- isOpenRespon seCache | Boolean | true | 是否开启响应缓存 |
| - routeIpBlockC onfigVO | Struct | {} | 路由IP封禁配置 |
| --ipBlockRules | Array | [] | IP封禁规则列表 |
| ---ip | String | 192.168.1.100 | IP地址 |
| ---policy | String | allow | 策略 |
| -- isOpenIpBlock | Boolean | false | 是否开启IP封禁 |
| - routeACLConfi g | Struct | {} | 路由访问控制配置 |
| --aclRules | Array | [] | 访问控制规则列表 |
| ---group | String | default-group | 分组 |
| ---policy | String | allow | 策略 |
| --isEnableACL | Boolean | true | 是否启用访问控制 |

| ·API |  |  | API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - routeTracingC onfig | Struct | {} | 路由链路追踪配置 |
| --traceHeader | String | X-Trace-Id | 链路追踪请求头 |
| -- isEnableDown stream | Boolean | true | 是否启用下游 |
| -- isEnableTracin g | Boolean | true | 是否启用链路追踪 |

#### GetProtocolByRoute

查询路由协议。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| type | Integ er | Body | 否 | 1 | 类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyRoute

修改路由。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| order | Integ er | Body | 否 | 100 | 路由执行的优先级，数值越小优先级越高。用于处理多个路由可能匹配同一请求的场景。 |
| filters | Strin g | Body | 否 | [{"name":"jwtAuthFilter" }, {"name":"rateLimitFilter "}] | 路由关联的过滤器链，通常为JSON字符串，定义了请求处理流程中的各种插件，如鉴权、限流等。 |
| routeId | Strin g | Body | 否 | rt-a1b2c3d4e5f6 | 需要修改的路由的唯一ID。 |
| routeNam e | Strin g | Body | 否 | 用户服务V2路由 | 路由的人类可读名称，方便识别和管理。 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |
| serviceTy pe | Strin g | Body | 否 | HTTP | 后端服务类型，例如 HTTP、GRPC等。 |
| gwInstanc eId | Strin g | Body | 否 | gw-prod-cluster-01 | 路由所属的网关实例ID。 |
| methods | Repe atList | Body | 否 | ["GET", "POST"] | 路由匹配的HTTP方法列表 （如GET, POST）。 |
| header | Repe atList | Body | 否 | [{"key":"X-Version", "value":"v2"}] | 路由匹配的请求头条件列表，用于实现基于Header 的路由。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |
| -value | Strin g | Body | 否 | example-value | 值 |
| cookie | Repe atList | Body | 否 | [{"key":"user-group", "value":"canary"}] | 路由匹配的Cookie条件列表。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -value | Strin g | Body | 否 | example-value | 值 |
| queryPara m | Repe atList | Body | 否 | [{"key":"env", "value":"test"}] | 路由匹配的URL查询参数条件列表。 |
| -key | Strin g | Body | 否 | api-key-001 | 密钥 |
| -value | Strin g | Body | 否 | example-value | 值 |
| domainIds | Repe atList | Body | 否 | ["dm-api-example-com"] | 路由匹配的域名ID列表。请求的Host头需要匹配其中之一。 |
| routePath | Repe atList | Body | 否 | ["/api/v2/users/*"] | 路由匹配的URL路径模式列表，支持星号(*)通配符。 |
| stripPrefix | Integ er | Body | 否 | 2 | 当openStripPrefix为true 时，指定在转发到后端服务前要剥离的路径层级数。例如，路径为/api/v2/users，stripPre fix为2，则后端收到/users。 |
| requestTi meout | Integ er | Body | 否 | 5000 | 网关请求后端服务的超时时间（单位：毫秒）。 |
| openStrip Prefix | Boole an | Body | 否 | true | 是否启用路径前缀剥离功能。 |
| enableFor ceNonceC heck | Boole an | Body | 否 | false | 是否强制开启Nonce校验以防止签名重放攻击。 |
| path | Json | Body | 否 | /api/v1/resource | 路径 |
| serviceIds | Repe atList | Body | 否 | [{"serviceId":"svc-user- v2-stable", "weight":80}, {"serviceId":"svc-user- v2-canary", "weight":20}] | （多服务/灰度发布模式）路由转发的目标服务列表及其权重。所有服务的权重之和应为100。 |
| -serviceId | Strin g | Body | 否 | service-123456 | 服务ID |
| -weight | Integ er | Body | 否 | 100 | 权重 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 业务返回码。200表示成功，其他值表示失败。 |
| msg | String | success | 返回的描述信息，成功时通常为'success'。 |
| data | String | rt-a1b2c3d4e5f6 | 返回的数据。操作成功时，通常是修改后的路由 ID。 |

#### DeleteRoute

删除路由。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ChangeRouteStatus

变更路由状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| enableSta tus | Boole an | Body | 否 | true | 启用状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

### 来源管理

#### ListSources

查询来源列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |
| sourceNa me | Strin g | Body | 否 | 内部系统 | 来源名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --sourceId | String | src-123456 | 来源ID |
| --sourceName | String | 内部系统 | 来源名称 |
| --sourceType | Integer | 1 | 来源类型 |
| -- sourceTypeNa me | String | Kubernetes | 来源类型名称 |
| --description | String | 这是一个示例服务 | 描述 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListAllSources

查询所有来源列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -sourceId | String | src-123456 | 来源ID |
| -sourceName | String | 内部系统 | 来源名称 |
| -sourceType | Integer | 1 | 来源类型 |
| - sourceTypeNa me | String | Kubernetes | 来源类型名称 |
| -sourceStruct | Map | {} | 来源结构 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetSource

查询来源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -sourceId | String | src-123456 | 来源ID |
| -sourceName | String | 内部系统 | 来源名称 |
| -sourceType | Integer | 1 | 来源类型 |
| - sourceTypeNa me | String | Kubernetes | 来源类型名称 |
| -sourceStruct | Map | {} | 来源结构 |
| -description | String | 这是一个示例服务 | 描述 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |

#### CreateSource

创建来源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| sourceNa me | Strin g | Body | 否 | 内部系统 | 来源名称 |
| host | Strin g | Body | 否 | api.example.com | 主机地址 |
| port | Integ er | Body | 否 | 8080 | 端口号 |
| username | Strin g | Body | 否 | zhangsan | 用户账号 |
| password | Strin g | Body | 否 | ******** | 密码 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| sourceTyp e | Integ er | Body | 否 | 1 | 来源类型 |
| sourceStr uct | Json | Body | 否 | {} | 来源结构 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifySource

修改来源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| sourceNa me | Strin g | Body | 否 | 内部系统 | 来源名称 |
| sourceStr uct | Json | Body | 否 | {} | 来源结构 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| sourceTyp e | Integ er | Body | 否 | 1 | 来源类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteSource

删除来源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### BatchDeleteSource

批量删除来源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceIds | Repe atList | Body | 否 | [] | 资源ID列表。 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | Struct | {} | 数据。 |
| -successIds | String | [] | 成功ID列表。 |
| -failedIds | String | [] | 失败ID列表。 |

### 服务管理

#### ListServices

查询服务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceNa me | Strin g | Body | 否 | user-service | 服务名称 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |
| sourceNa me | Strin g | Body | 否 | 内部系统 | 来源名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --nodes | Array | [] | 节点列表 |
| ---ip | String | 192.168.1.100 | IP地址 |
| ---port | Integer | 8080 | 端口号 |
| ---weight | Integer | 100 | 权重 |
| ---enable | Boolean | true | 是否启用 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --serviceId | String | service-123456 | 服务ID |
| --name | String | my-resource | 名称 |
| -- upstreamType | Integer | 1 | 上游类型 |
| --serviceType | Integer | REST | 服务类型 |
| -- upstreamType Name | String | HTTP服务 | 上游类型名称 |
| -- serviceProtoco l | String | HTTP | 服务协议 |
| --sourceId | String | src-123456 | 来源ID |
| --sourceName | String | 内部系统 | 来源名称 |
| --sourceType | Integer | 1 | 来源类型 |
| -- sourceTypeNa me | String | Kubernetes | 来源类型名称 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListAllServices

查询所有服务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -serviceId | String | service-123456 | 服务ID |
| -serviceName | String | user-service | 服务名称 |
| -protocol | String | HTTP | 协议 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetService

查询服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i- c0a81bb16a1524a1700 | 网关实例id |
| serviceId | Strin g | Body | 否 | bailian | 服务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -zones | String | [] | 可用区列表 |
| -routeList | Array | [] | 路由列表 |
| --routePath | String | /api/v1/users | 路由路径 |
| --routeId | String | route-123456 | 路由ID |
| --routeName | String | user-service-route | 路由名称 |
| - strategyConfig s | Array | [] | 策略配置列表 |
| --scopes | String | [] | 授权范围列表 |
| -- strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -- strategyConfig Name | String | 默认策略 | 策略配置名称 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --scope | Struct | openid profile | 授权范围 |
| ---scopes | String | [] | 授权范围列表 |
| ---routeInfos | Array | [] | 路由信息列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---serviceInfos | Array | [] | 服务信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---appInfos | Array | [] | 应用信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---domainInfos | Array | [] | 域名信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| --- mcpServerInfo s | Array | [] | MCP服务器信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| -serviceId | String | service-123456 | 服务ID |
| -name | String | my-resource | 名称 |
| -serviceName | String | user-service | 服务名称 |
| -description | String | 这是一个示例服务 | 描述 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -protocol | String | HTTP | 协议 |
| -serviceType | Integer | REST | 服务类型 |
| - upstreamType | Integer | 1 | 上游类型 |
| - upstreamType Name | String | HTTP服务 | 上游类型名称 |
| - loadBalanceTy pe | Integer | 1 | 负载均衡类型 |
| - loadBalanceTy peName | String | 轮询 | 负载均衡类型名称 |
| -sourceType | Integer | 1 | 来源类型 |
| - serviceSource Type | Integer | 1 | 服务来源类型 |
| -serviceStruct | Map | {} | 服务结构 |
| - isOpenHealthC heck | Boolean | true | 是否开启健康检查 |
| - healthCheckSt ruct | Struct | {} | 健康检查配置 |
| --type | Integer | 1 | 类型 |
| --healthPath | String | /health | 健康检查路径 |
| --httpStatuses | String | 200,201,204 | HTTP状态码 |
| --timeout | Integer | 30000 | 超时时间（毫秒） |
| -- healthInterval | Integer | 30 | 健康检查间隔（秒） |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- unHealthInterv al | Integer | 10 | 不健康检查间隔（秒） |
| -- httpSuccesses | Integer | 3 | HTTP成功次数 |
| --httpFailures | Integer | 5 | HTTP失败次数 |

#### CreateService

创建服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |
| name | Strin g | Body | 否 | my-resource | 名称 |
| upstream Type | Integ er | Body | 否 | 1 | 上游类型 |
| serviceSo urceType | Integ er | Body | 否 | 1 | 服务来源类型 |
| serviceNa me | Strin g | Body | 否 | user-service | 服务名称 |
| loadBalan ceType | Integ er | Body | 否 | 1 | 负载均衡类型 |
| serviceStr uct | Json | Body | 否 | {} | 服务结构 |
| isOpenHe althCheck | Boole an | Body | 否 | true | 是否开启健康检查 |
| healthChe ckStruct | Json | Body | 否 | {} | 健康检查配置 |

|  | 开发指南·API 网 | 关 |  |  |  | API 网关 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| protocol | Strin g | Body | 否 | HTTP | 协议 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyService

修改服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| name | Strin g | Body | 否 | my-resource | 名称 |
| serviceNa me | Strin g | Body | 否 | user-service | 服务名称 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| upstream Type | Integ er | Body | 否 | 1 | 上游类型 |
| serviceSo urceType | Integ er | Body | 否 | 1 | 服务来源类型 |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| loadBalan ceType | Integ er | Body | 否 | 1 | 负载均衡类型 |
| serviceStr uct | Json | Body | 否 | {} | 服务结构 |
| isOpenHe althCheck | Boole an | Body | 否 | true | 是否开启健康检查 |
| healthChe ckStruct | Json | Body | 否 | {} | 健康检查配置 |
| protocol | Strin g | Body | 否 | HTTP | 协议 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyNode

修改服务节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |
| serviceSo urceType | Integ er | Body | 否 | 1 | 服务来源类型 |
| serviceStr uct | Json | Body | 否 | {} | 服务结构 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteService

删除服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | test-service | 实例ID |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式

```json
{
 "msg":"",
 "code":"",
 "data":""
}
```

#### BatchDeleteService

批量删除服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceIds | Repe atList | Body | 否 | [] | 服务ID列表 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -successIds | String | [] | 成功ID列表 |
| -failedIds | String | [] | 失败ID列表 |

#### ImportServices

导入Services。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述。 |
| loadBalan ceType | Integ er | Body | 否 | 1 | 负载均衡类型。 |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型。 |
| sourceId | Strin g | Body | 否 | src-123456 | 来源ID。 |
| sourceNa mespaceI d | Strin g | Body | 否 | ns-source-001 | 来源命名空间ID。 |
| groupNam e | Strin g | Body | 否 | 默认分组 | 分组名称。 |
| port | Integ er | Body | 否 | 8080 | 端口号。 |
| serviceLis t | Repe atList | Body | 否 | [] | 服务列表。 |
| protocol | Strin g | Body | 否 | HTTP | 协议。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 数据。 |
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |

### 消费者管理

#### ListApps

查询消费者列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| appName | Strin g | Body | 否 | 示例应用 | 应用名称 |
| appTags | Strin g | Body | 否 | [] | 应用标签列表 |
| authType | Strin g | Body | 否 | jwt | 认证类型 |
| userId | Strin g | Body | 否 | uid-123456 | 用户ID |
| userName | Strin g | Body | 否 | 张三 | 用户名 |
| email | Strin g | Body | 否 | admin@example.com | 邮箱 |
| status | Integ er | Body | 否 | 1 | 状态 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| appType | Integ er | Body | 否 | 1 | 应用类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ipWhiteList | String | [] | IP白名单 |
| --groups | String | [] | 分组列表 |
| --appTags | Array | [] | 应用标签列表 |
| --appId | String | 12345678 | 应用ID |
| --appName | String | 示例应用 | 应用名称 |
| --appAddress | String | https://example.co m | 应用地址 |
| --useAuth | Boolean | true | 是否使用认证 |
| --authType | Integer | jwt | 认证类型 |
| -- authTypeNam e | String | JWT | 认证类型名称 |
| --useWhiteList | Boolean | true | 是否使用白名单 |
| --description | String | 这是一个示例服务 | 描述 |
| -- chargePerson Name | String | 张三 | 负责人姓名 |
| --createBy | Integer | 1001 | 创建人ID |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateBy | Integer | 1001 | 更新人ID |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --userId | String | uid-123456 | 用户ID |
| --userName | String | 张三 | 用户名 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --delFlag | String | 0 | 删除标志 |
| --isDisable | Boolean | false | 是否禁用 |
| --enable | Boolean | true | 是否启用 |
| --timeOut | Boolean | false | 是否超时 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |
| -size | Integer | 100 | 大小 |

#### ListAppsByGwInstanceId

查询AppsByGwInstanceId列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -groups | String | [] | 分组列表 |
| -appTags | Array | [] | 应用标签列表 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - strategyConfig s | Array | [] | 策略配置列表 |
| --scopes | String | [] | 授权范围列表 |
| -- strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -- strategyConfig Name | String | 默认策略 | 策略配置名称 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -appId | String | 12345678 | 应用ID |
| -appName | String | 示例应用 | 应用名称 |
| -useAuth | Boolean | true | 是否使用认证 |
| -authType | Integer | jwt | 认证类型 |
| - requestHeader | String | Content-Type | 请求头 |
| - authTypeNam e | String | JWT | 认证类型名称 |
| -ipWhiteList | String | [] | IP白名单 |
| -useWhiteList | Boolean | true | 是否使用白名单 |
| -description | String | 这是一个示例服务 | 描述 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9. .. | 令牌 |
| -appSecret | String | as abcdefghijklmn _ op | 应用密文 |
| -isDisable | Boolean | false | 是否禁用 |
| -enable | Boolean | true | 是否启用 |
| -key | String | api-key-001 | 密钥 |
| -password | String | ******** | 密码 |
| -expireTime | Integer | 2025-10-14 23:59:59 | 过期时间 |
| -appCode | String | APP20240101 | 应用编码 |
| -accessKey | String | LTAI5tFhqxxxxxxx | 访问密钥 |
| -secretKey | String | sk 1234567890abc _ def | 密钥 |
| -payload | Struct | {} | 请求负载 |
| --subject | String | CN=example.com | 证书主题 |
| --issuer | String | https://auth.examp le.com | 颁发者 |
| - oauth2Payload | Struct | {} | OAuth2负载 |
| --scopes | String | [] | 授权范围列表 |
| -- authorizationC ode | Boolean | true | 是否启用授权码模式 |
| -- clientCredenti als | Boolean | true | 是否启用客户端凭证模式 |
| --implicitGrant | Boolean | false | 是否启用隐式授权 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- passwordGran t | Boolean | true | 是否启用密码授权 |
| -- tokenExpiratio n | Integer | 7200 | 令牌过期时间（秒） |
| -- refreshTokenE xpiration | Integer | 86400 | 刷新令牌过期时间（秒） |
| --clientId | String | client 123456 _ | 客户端ID |
| --clientSecret | String | secret abc123 _ | 客户端密钥 |
| --redirectUris | String | https://example.co m/callback | 重定向URI |
| --pkce | Boolean | true | 是否启用PKCE |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetApp

查询消费者。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| A | PI 网关 |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -groups | String | [] | 分组列表 |
| -appTags | Array | [] | 应用标签列表 |
| - strategyConfig s | Array | [] | 策略配置列表 |
| --scopes | String | [] | 授权范围列表 |
| -- strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -- strategyConfig Name | String | 默认策略 | 策略配置名称 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --scope | Struct | openid profile | 授权范围 |
| ---scopes | String | [] | 授权范围列表 |
| ---routeInfos | Array | [] | 路由信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---serviceInfos | Array | [] | 服务信息列表 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---appInfos | Array | [] | 应用信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---domainInfos | Array | [] | 域名信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| --- mcpServerInfo s | Array | [] | MCP服务器信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| -appId | String | 12345678 | 应用ID |
| -appName | String | 示例应用 | 应用名称 |
| -useAuth | Boolean | true | 是否使用认证 |
| -authType | Integer | jwt | 认证类型 |
| - requestHeader | String | Content-Type | 请求头 |
| - authTypeNam e | String | JWT | 认证类型名称 |
| -ipWhiteList | String | [] | IP白名单 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -useWhiteList | Boolean | true | 是否使用白名单 |
| -description | String | 这是一个示例服务 | 描述 |
| -token | String | eyJhbGciOiJIUzI1NiI sInR5cCI6IkpXVCJ9. .. | 令牌 |
| -appSecret | String | as abcdefghijklmn _ op | 应用密文 |
| -isDisable | Boolean | false | 是否禁用 |
| -enable | Boolean | true | 是否启用 |
| -key | String | api-key-001 | 密钥 |
| -password | String | ******** | 密码 |
| -expireTime | Integer | 2025-10-14 23:59:59 | 过期时间 |
| -appCode | String | APP20240101 | 应用编码 |
| -accessKey | String | LTAI5tFhqxxxxxxx | 访问密钥 |
| -secretKey | String | sk 1234567890abc _ def | 密钥 |
| -payload | Struct | {} | 请求负载 |
| --subject | String | CN=example.com | 证书主题 |
| --issuer | String | https://auth.examp le.com | 颁发者 |
| - oauth2Payload | Struct | {} | OAuth2负载 |
| --scopes | String | [] | 授权范围列表 |
| -- authorizationC ode | Boolean | true | 是否启用授权码模式 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -- clientCredenti als | Boolean | true | 是否启用客户端凭证模式 |
| --implicitGrant | Boolean | false | 是否启用隐式授权 |
| -- passwordGran t | Boolean | true | 是否启用密码授权 |
| -- tokenExpiratio n | Integer | 7200 | 令牌过期时间（秒） |
| -- refreshTokenE xpiration | Integer | 86400 | 刷新令牌过期时间（秒） |
| --clientId | String | client 123456 _ | 客户端ID |
| --clientSecret | String | secret abc123 _ | 客户端密钥 |
| --redirectUris | String | https://example.co m/callback | 重定向URI |
| --pkce | Boolean | true | 是否启用PKCE |

#### CreateApp

创建消费者。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | Strin g | Body | 否 | api-key-001 | 密钥 |
| payload | Json | Body | 否 | {} | 请求负载 |
| oauth2Pa yload | Json | Body | 否 | {} | OAuth2负载 |
| password | Strin g | Body | 否 | ******** | 密码 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| expireTim e | Integ er | Body | 否 | 2025-10-14 23:59:59 | 过期时间 |
| appSecret | Strin g | Body | 否 | as abcdefghijklmnop _ | 应用密文 |
| requestHe ader | Strin g | Body | 否 | Content-Type | 请求头 |
| token | Strin g | Body | 否 | eyJhbGciOiJIUzI1NiIsInR5 cCI6IkpXVCJ9... | 令牌 |
| useAuth | Boole an | Body | 否 | true | 是否使用认证 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| authType | Integ er | Body | 否 | jwt | 认证类型 |
| useWhiteL ist | Boole an | Body | 否 | true | 是否使用白名单 |
| ipWhiteLis t | Strin g | Body | 否 | [] | IP白名单 |
| appName | Strin g | Body | 否 | 示例应用 | 应用名称 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| userId | Strin g | Body | 否 | uid-123456 | 用户ID |
| userName | Strin g | Body | 否 | 张三 | 用户名 |
| appKey | Strin g | Body | 否 | ak 1234567890abcdef _ | 应用密钥 |
| groups | Repe atList | Body | 否 | [] | 分组列表 |
| appCode | Strin g | Body | 否 | APP20240101 | 应用编码 |
| accessKey | Strin g | Body | 否 | LTAI5tFhqxxxxxxx | 访问密钥 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| secretKey | Strin g | Body | 否 | sk 1234567890abcdef _ | 密钥 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyApp

修改消费者。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | Strin g | Body | 否 | api-key-001 | 密钥 |
| payload | Json | Body | 否 | {} | 请求负载 |
| oauth2Pa yload | Json | Body | 否 | {} | OAuth2负载 |
| password | Strin g | Body | 否 | ******** | 密码 |
| expireTim e | Integ er | Body | 否 | 2025-10-14 23:59:59 | 过期时间 |
| appSecret | Strin g | Body | 否 | as abcdefghijklmnop _ | 应用密文 |
| requestHe ader | Strin g | Body | 否 | Content-Type | 请求头 |
| token | Strin g | Body | 否 | eyJhbGciOiJIUzI1NiIsInR5 cCI6IkpXVCJ9... | 令牌 |
| useAuth | Boole an | Body | 否 | true | 是否使用认证 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| authType | Integ er | Body | 否 | jwt | 认证类型 |
| useWhiteL ist | Boole an | Body | 否 | true | 是否使用白名单 |
| ipWhiteLis t | Strin g | Body | 否 | [] | IP白名单 |
| appName | Strin g | Body | 否 | 示例应用 | 应用名称 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| userId | Strin g | Body | 否 | uid-123456 | 用户ID |
| userName | Strin g | Body | 否 | 张三 | 用户名 |
| appKey | Strin g | Body | 否 | ak 1234567890abcdef _ | 应用密钥 |
| groups | Repe atList | Body | 否 | [] | 分组列表 |
| appCode | Strin g | Body | 否 | APP20240101 | 应用编码 |
| accessKey | Strin g | Body | 否 | LTAI5tFhqxxxxxxx | 访问密钥 |
| secretKey | Strin g | Body | 否 | sk 1234567890abcdef _ | 密钥 |
| appAddre ss | Strin g | Body | 否 | https://example.com | 应用地址 |
| appTagsSt r | Strin g | Body | 否 | tag1,tag2,tag3 | 应用标签字符串 |
| chargePer sonName | Strin g | Body | 否 | 张三 | 负责人姓名 |
| openCross | Boole an | Body | 否 | true | 是否开启跨域 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| allowedOri gins | Strin g | Body | 否 | * | 允许的来源域名 |
| allowedHe aders | Strin g | Body | 否 | Content- Type,Authorization | 允许的请求头 |
| allowedM ethods | Strin g | Body | 否 | [] | 允许的请求方法列表 |
| isDisable | Boole an | Body | 否 | false | 是否禁用 |
| appType | Integ er | Body | 否 | 1 | 应用类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteApp

删除消费者。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyAppOpenStatus

修改消费者开放状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| enable | Boole an | Body | 否 | true | 是否启用 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### ModifyAppWhiteListStatus

修改消费者白名单状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| isOpen | Boole an | Body | 否 | true | 是否开启 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### GetAppAuth

查询消费者授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| authId | Strin g | Body | 否 | auth 123456 _ | 认证ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -authId | Integer | auth 123456 _ | 认证ID |
| -appId | String | 12345678 | 应用ID |
| -routeId | String | route-123456 | 路由ID |
| -routePath | String | /api/v1/users | 路由路径 |
| -serviceId | Integer | service-123456 | 服务ID |
| -serviceName | String | user-service | 服务名称 |
| - serviceProtoco l | String | HTTP | 服务协议 |
| -authStatus | Integer | 1 | 认证状态 |

#### CreateAppAuth

创建消费者授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| body | Strin g | Body | 否 | {"key":"value"} | 请求体内容 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 响应码 |
| Msg | String | 操作成功 | 消息 |
| Data | String | {} | 数据 |

#### BatchCreateAppAuthByRoute

批量创建消费者授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| routeId | Repe atList | Body | 否 | route-123456 | 路由ID |
| authStatu s | Integ er | Body | 否 | 1 | 认证状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyAppAuthStatus

修改消费者授权状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| authId | Strin g | Body | 否 | auth 123456 _ | 认证ID |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| authStatu s | Integ er | Body | 否 | 1 | 认证状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -id | Integer | 123456 | ID |
| -createBy | Integer | 1001 | 创建人ID |
| -updateBy | Integer | 1001 | 更新人ID |
| -appId | String | 12345678 | 应用ID |
| -authId | String | auth 123456 _ | 认证ID |
| -routeId | String | route-123456 | 路由ID |
| -authStatus | Integer | 1 | 认证状态 |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |

#### DeleteAppAuth

删除消费者授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| authId | Strin g | Body | 否 | auth 123456 _ | 认证ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### RefreshToken

刷新令牌。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | Strin g | Body | 否 | api-key-001 | 密钥 |
| payload | Json | Body | 否 | {} | 请求负载 |
| oauth2Pa yload | Json | Body | 否 | {} | OAuth2负载 |
| password | Strin g | Body | 否 | ******** | 密码 |
| expireTim e | Integ er | Body | 否 | 2025-10-14 23:59:59 | 过期时间 |
| appSecret | Strin g | Body | 否 | as abcdefghijklmnop _ | 应用密文 |
| requestHe ader | Strin g | Body | 否 | Content-Type | 请求头 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| token | Strin g | Body | 否 | eyJhbGciOiJIUzI1NiIsInR5 cCI6IkpXVCJ9... | 令牌 |
| useAuth | Boole an | Body | 否 | true | 是否使用认证 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| authType | Integ er | Body | 否 | jwt | 认证类型 |
| useWhiteL ist | Boole an | Body | 否 | true | 是否使用白名单 |
| ipWhiteLis t | Strin g | Body | 否 | [] | IP白名单 |
| appName | Strin g | Body | 否 | 示例应用 | 应用名称 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| userId | Strin g | Body | 否 | uid-123456 | 用户ID |
| userName | Strin g | Body | 否 | 张三 | 用户名 |
| appKey | Strin g | Body | 否 | ak 1234567890abcdef _ | 应用密钥 |
| groups | Repe atList | Body | 否 | [] | 分组列表 |
| appCode | Strin g | Body | 否 | APP20240101 | 应用编码 |
| accessKey | Strin g | Body | 否 | LTAI5tFhqxxxxxxx | 访问密钥 |
| secretKey | Strin g | Body | 否 | sk 1234567890abcdef _ | 密钥 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### ResetSecretKey

重置密钥。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Boolean | {} | 数据 |

#### HandlerConsumerAuth

查询消费者认证。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| isOpen | Boole an | Body | 否 | true | 是否开启 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 否 | my-resource | 名称 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### CreateAppAuthByRoute

创建消费者授权。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| appId | Strin g | Body | 否 | 12345678 | 应用ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| authStatu s | Integ er | Body | 否 | 1 | 认证状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### BatchDeleteApp

批量删除消费者。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appIds | Repe atList | Body | 否 | [] | 应用ID列表。 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | Struct | {} | 数据。 |
| -successIds | String | [] | 成功ID列表 |
| -failedIds | String | [] | 失败ID列表 |

### 插件管理

#### ListPlugins

查询插件列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| searchNa me | Strin g | Body | 否 | 搜索关键词 | 搜索名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --config | Array | [] | 配置列表 |
| ---name | String | my-resource | 名称 |
| ---required | Boolean | true | 是否必需 |
| --pluginId | String | plugin-123456 | 插件ID |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --pluginName | String | rate-limiter | 插件名称 |
| --description | String | 这是一个示例服务 | 描述 |
| --downloadURL | String | https://example.co m/download/file.zip | 下载URL |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --type | Integer | 1 | 类型 |
| --used | Boolean | false | 是否已使用 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListOpenPlugins

查询开放插件列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| searchNa me | Strin g | Body | 否 | 搜索关键词 | 搜索名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -config | Array | [] | 配置列表 |
| --name | String | my-resource | 名称 |
| --required | Boolean | true | 是否必需 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -pluginId | String | plugin-123456 | 插件ID |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -pluginName | String | rate-limiter | 插件名称 |
| -description | String | 这是一个示例服务 | 描述 |
| -downloadURL | String | https://example.co m/download/file.zip | 下载URL |
| -type | Integer | 1 | 类型 |
| -used | Boolean | false | 是否已使用 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### ListGlobalPlugins

查询全局插件列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| searchNa me | Strin g | Body | 否 | 搜索关键词 | 搜索名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --pluginId | String | plugin-123456 | 插件ID |
| --routePluginId | String | plugin-route-001 | 路由插件ID |
| --pluginName | String | rate-limiter | 插件名称 |
| --config | String | [] | 配置列表 |
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --order | Integer | 100 | 排序号 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListRoutePlugins

查询路由插件列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| searchNa me | Strin g | Body | 否 | 搜索关键词 | 搜索名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| --routeId | String | route-123456 | 路由ID |
| --pluginId | String | plugin-123456 | 插件ID |
| --routePluginId | String | plugin-route-001 | 路由插件ID |
| --pluginName | String | rate-limiter | 插件名称 |
| --config | String | [] | 配置列表 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --status | Boolean | 1 | 状态 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --order | Integer | 100 | 排序号 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### GetPlugin

查询插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -config | Array | [] | 配置列表 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --name | String | my-resource | 名称 |
| --required | Boolean | true | 是否必需 |
| -pluginId | String | plugin-123456 | 插件ID |
| -gwInstanceId | String | i- c0a81bb16a1524a 17 | 网关实例ID |
| -pluginName | String | rate-limiter | 插件名称 |
| -description | String | 这是一个示例服务 | 描述 |
| -downloadURL | String | https://example.co m/download/file.zip | 下载URL |
| -type | Integer | 1 | 类型 |
| -used | Boolean | false | 是否已使用 |

#### CreatePlugin

创建插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginNa me | Strin g | Body | 否 | rate-limiter | 插件名称 |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| download URL | Strin g | Body | 否 | https://example.com/do wnload/file.zip | 下载URL |
| config | Repe atList | Body | 否 | [] | 配置列表 |

|  | 开发指南·API 网 | 关 |  |  |  | API 网关 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -name | Strin g | Body | 否 | my-resource | 名称 |
| -required | Boole an | Body | 否 | true | 是否必需 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### CreateGlobalPlugin

创建全局插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| status | Boole an | Body | 否 | 1 | 状态 |
| config | Strin g | Body | 否 | [] | 配置列表 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### CreateRoutePlugin

创建路由插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| status | Boole an | Body | 否 | 1 | 状态 |
| config | Strin g | Body | 否 | [] | 配置列表 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyPlugin

修改插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |
| descriptio n | Strin g | Body | 否 | 这是一个示例服务 | 描述 |
| download URL | Strin g | Body | 否 | https://example.com/do wnload/file.zip | 下载URL |
| config | Repe atList | Body | 否 | [] | 配置列表 |
| -name | Strin g | Body | 否 | my-resource | 名称 |
| -required | Boole an | Body | 否 | true | 是否必需 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyGlobalPlugin

修改全局插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

| A | PI 网关 |  |  |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| config | Strin g | Body | 否 | [] | 配置列表 |
| status | Boole an | Body | 否 | 1 | 状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyRoutePlugin

修改路由插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| config | Strin g | Body | 否 | [] | 配置列表 |
| status | Boole an | Body | 否 | 1 | 状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeletePlugin

删除插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteGlobalPlugin

删除全局插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteRoutePlugin

删除路由插件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyGlobalPluginStatus

修改全局插件状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| config | Strin g | Body | 否 | [] | 配置列表 |
| status | Boole an | Body | 否 | 1 | 状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyRoutePluginStatus

修改路由插件状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |
| routePlugi nId | Strin g | Body | 否 | plugin-route-001 | 路由插件ID |
| order | Integ er | Body | 否 | 100 | 排序号 |
| config | Strin g | Body | 否 | [] | 配置列表 |
| status | Boole an | Body | 否 | 1 | 状态 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ListPluginUsage

查询插件使用情况列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | Integ er | Body | 否 | 1 | 当前页码 |
| size | Integ er | Body | 否 | 100 | 大小 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| pluginId | Strin g | Body | 否 | plugin-123456 | 插件ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --routeId | String | route-123456 | 路由ID |
| --routeName | String | user-service-route | 路由名称 |
| --status | Boolean | 1 | 状态 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

### 策略管理

#### ModifyStrategyConfig

修改策略配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| strategyC onfigNam e | Strin g | Body | 否 | 默认策略 | 策略配置名称。 |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID。 |
| strategyN ame | Strin g | Body | 否 | 流量控制策略 | 策略名称。 |

| A | PI 网关 |  |  |  |  | 开发指南·API 网关 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| config | Json | Body | 否 | [] | 配置列表。 |
| rawConfig | Strin g | Body | 否 | {"timeout":30} | 原始配置。 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID。 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID。 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID。 |
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID。 |
| routeIds | Repe atList | Body | 否 | [] | 路由ID列表。 |
| serviceIds | Repe atList | Body | 否 | [] | 服务ID列表。 |
| appIds | Repe atList | Body | 否 | [] | 应用ID列表。 |
| domainIds | Repe atList | Body | 否 | [] | 域名ID列表。 |
| mcpIds | Repe atList | Body | 否 | [] | MCP ID列表。 |
| status | Boole an | Body | 否 | 1 | 状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | String | {} | 数据。 |

#### CreateStrategyConfig

创建策略配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| strategyC onfigNam e | Strin g | Body | 否 | 默认策略 | 策略配置名称。 |
| strategyN ame | Strin g | Body | 否 | default | 策略名称。 |
| config | Json | Body | 否 | [] | 配置列表。 |
| rawConfig | Strin g | Body | 否 | {"timeout":30} | 原始配置。 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID。 |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID。 |
| serviceId | Strin g | Body | 否 | service-123456 | 服务ID。 |
| appId | Strin g | Body | 否 | 12345678 | 应用ID。 |
| mcpServe rId | Strin g | Body | 否 | mcp-server-001 | MCP服务器ID。 |
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID。 |
| routeIds | Repe atList | Body | 否 | [] | 路由ID列表。 |
| serviceIds | Repe atList | Body | 否 | [] | 服务ID列表。 |
| appIds | Repe atList | Body | 否 | [] | 应用ID列表。 |
| domainIds | Repe atList | Body | 否 | [] | 域名ID列表。 |
| mcpIds | Repe atList | Body | 否 | [] | MCP ID列表。 |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码。 |
| msg | String | 操作成功 | 消息。 |
| data | String | {} | 数据。 |

#### ListStrategies

查询策略列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| scope | Strin g | Body | 否 | openid profile | 授权范围 |
| strategyN ame | Strin g | Body | 否 | 流量控制策略 | 策略名称 |
| brokerEng ineType | Strin g | Body | 否 | RocketMQ | 消息引擎类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -strategies | Array | [] | 策略列表 |
| --scopes | String | [] | 授权范围列表 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --uiStyles | String | [] | UI样式列表 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --strategyTitle | String | 高级流控 | 策略标题 |
| --description | String | 这是一个示例服务 | 描述 |
| -- supportCascad e | Integer | 1 | 是否支持级联 |
| -- rawConfigExa mple | String | {"enabled":true} | 原始配置示例 |
| --order | Integer | 100 | 排序号 |
| --document | String | API接口文档 | 文档 |
| -category | Struct | {} | 分类信息 |
| --name | String | my-resource | 名称 |
| --title | String | 接口标题 | 标题 |
| --order | Integer | 100 | 排序号 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### ListStrategyConfigs

查询策略配置列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| strategyC onfigNam e | Strin g | Body | 否 | 默认策略 | 策略配置名称 |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID |
| strategyN ame | Strin g | Body | 否 | 流量控制策略 | 策略名称 |
| scope | Json | Body | 否 | openid profile | 授权范围 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --scopes | String | [] | 授权范围列表 |
| -- strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -- strategyConfig Name | String | 默认策略 | 策略配置名称 |
| -- strategyName | String | 流量控制策略 | 策略名称 |
| --status | Boolean | 1 | 状态 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --scope | Struct | openid profile | 授权范围 |
| ---scopes | String | [] | 授权范围列表 |
| ---routeInfos | Array | [] | 路由信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---serviceInfos | Array | [] | 服务信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---appInfos | Array | [] | 应用信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| ---domainInfos | Array | [] | 域名信息列表 |
| ----name | String | my-resource | 名称 |
| ----id | String | 123456 | ID |
| --- mcpServerInfo s | Array | [] | MCP服务器信息列表 |
| ----name | String | my-resource | 名称 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----id | String | 123456 | ID |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |
| -size | Integer | 100 | 大小 |

#### GetStrategy

查询策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| strategyN ame | Strin g | Body | 否 | 流量控制策略 | 策略名称 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -scopes | String | [] | 授权范围列表 |
| -uiStyles | String | [] | UI样式列表 |
| -strategyName | String | 流量控制策略 | 策略名称 |
| -strategyTitle | String | 高级流控 | 策略标题 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -description | String | 这是一个示例服务 | 描述 |
| - supportCascad e | Integer | 1 | 是否支持级联 |
| - rawConfigExa mple | String | {"enabled":true} | 原始配置示例 |
| -order | Integer | 100 | 排序号 |
| -document | String | API接口文档 | 文档 |

#### GetStrategyConfig

查询策略配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -scopes | String | [] | 授权范围列表 |
| - strategyConfig Name | String | 默认策略 | 策略配置名称 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| - strategyConfig Id | String | strategy-config- 001 | 策略配置ID |
| -strategyName | String | 流量控制策略 | 策略名称 |
| -routeId | String | route-123456 | 路由ID |
| -routeName | String | user-service-route | 路由名称 |
| -serviceId | String | service-123456 | 服务ID |
| -serviceName | String | user-service | 服务名称 |
| -appId | String | 12345678 | 应用ID |
| -appName | String | 示例应用 | 应用名称 |
| -domainId | String | domain-123456 | 域名ID |
| -domainName | String | example.com | 域名名称 |
| -status | Boolean | 1 | 状态 |
| -config | Map | [] | 配置列表 |
| -rawConfig | String | {"timeout":30} | 原始配置 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -scope | Struct | openid profile | 授权范围 |
| --scopes | String | [] | 授权范围列表 |
| --routeInfos | Array | [] | 路由信息列表 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---name | String | my-resource | 名称 |
| ---id | String | 123456 | ID |
| --serviceInfos | Array | [] | 服务信息列表 |
| ---name | String | my-resource | 名称 |
| ---id | String | 123456 | ID |
| --appInfos | Array | [] | 应用信息列表 |
| ---name | String | my-resource | 名称 |
| ---id | String | 123456 | ID |
| --domainInfos | Array | [] | 域名信息列表 |
| ---name | String | my-resource | 名称 |
| ---id | String | 123456 | ID |
| -- mcpServerInfo s | Array | [] | MCP服务器信息列表 |
| ---name | String | my-resource | 名称 |
| ---id | String | 123456 | ID |

#### GetRoutePolicies

查询路由策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -rewrite | Struct | {} | 重写配置 |
| --enabled | Boolean | true | 是否启用 |
| --path | String | /api/v1/resource | 路径 |
| --host | String | api.example.com | 主机地址 |
| -headerControl | Struct | {} | 请求头控制配置 |
| --enabled | Boolean | true | 是否启用 |
| --request | Struct | {} | 请求结构 |
| ---remove | String | [] | 移除列表 |
| ---add | Array | [] | 添加列表 |
| ----key | String | api-key-001 | 密钥 |
| ----value | String | example-value | 值 |
| ---set | Array | [] | 设置列表 |

|  | 开发指南·API 网关 |  |  | API 网关 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----key | String | api-key-001 | 密钥 |
| ----value | String | example-value | 值 |
| --response | Struct | {} | 响应结构 |
| ---remove | String | [] | 移除列表 |
| ---add | Array | [] | 添加列表 |
| ----key | String | api-key-001 | 密钥 |
| ----value | String | example-value | 值 |
| ---set | Array | [] | 设置列表 |
| ----key | String | api-key-001 | 密钥 |
| ----value | String | example-value | 值 |
| -timeoutConfig | Struct | {} | 超时配置 |
| --enabled | Boolean | true | 是否启用 |
| --timeout | Integer | 30000 | 超时时间（毫秒） |
| -fallbackConfig | Struct | {} | 降级配置 |
| -- responseCode s | String | [] | 响应码列表 |
| --services | Array | [] | 服务列表 |
| ---name | String | my-resource | 名称 |
| ---port | Integer | 8080 | 端口号 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---version | String | 1.0.0 | 版本号 |
| ---weight | Integer | 100 | 权重 |
| --enabled | Boolean | true | 是否启用 |
| -- fallbackStrate gy | String | default | 降级策略 |

#### ModifyRoutePolicy

修改路由策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configTyp e | Strin g | Body | 否 | yaml | 配置类型 |
| configDat a | Json | Body | 否 | {} | 配置数据 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| routeId | Strin g | Body | 否 | route-123456 | 路由ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteStrategyConfig

删除策略配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyStrategyConfigStatus

修改策略配置状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| isOpen | Boole an | Body | 否 | true | 是否开启 |
| strategyC onfigId | Strin g | Body | 否 | strategy-config-001 | 策略配置ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

### 域名管理

#### ListDomains

查询域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 10 | 分页查询时每页的行数。 |
| current | Integ er | Body | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为 1，表示从第1页开始显示。 |
| domain | Strin g | Body | 否 | www.aliyun.com | 域名 |
| gwInstanc eId | Strin g | Body | 否 | i-xxxxxxx | 网关实例 ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 接口状态或POP错误码。 |
| Msg | String | success | 状态描述信息，Code为"200"时，Msg一般为空。 |
| Data | Struct | {} | 返回数据。 |
| -Records | Array | [] | 返回数据结果记录。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --DomainId | String | 00efd71a-770e- 4255-b54e- 6fe5659baffe | 域名ID。 |
| --CertificateId | String | 12345678-1234- 1234-1234- 12345678**** | 证书ID。 |
| -- CertificateNam e | String | myCertificate | SSL证书名称 |
| --Domain | String | www.aliyun.com | 域名。 |
| --Protocol | String | HTTP | 协议类型。 |
| --CreateTime | String | 2024-03- 15T01:46Z | 创建时间。 |
| --UpdateTime | String | 2024-03- 15T01:46Z | 更新时间。 |
| --ClientAuth | Integer | 0 | 是否开启双向认证。0：不开启。1：开启 |
| -- CaCertificateId | String | 00efd71a-770e- 4255-b54e- 6fe5659baffe | CA证书ID。 |
| -- CaCertificateN ame | String | test | CA证书的名称。 |
| -Size | Long | 20 | 每页数量。 |
| -Total | Long | 1 | 总数。 |
| -Current | Long | 1 | 当前页。 |

**示例**

`JSON` 格式

```json
{
 "Msg":"success",
 "Data":{
  "Records":[
   {
    "DomainId":"00efd71a-770e-4255-b54e-6fe5659baffe",
    "CertificateId":"12345678-1234-1234-1234-12345678****",
    "CreateTime":"2024-03-15T01:46Z",
    "UpdateTime":"2024-03-15T01:46Z",
    "CertificateName":"myCertificate",
    "Domain":"www.aliyun.com",
    "Protocol":"HTTP",
    "ClientAuth":0,
    "CaCertificateName":"test",
    "CaCertificateId":"00efd71a-770e-4255-b54e-6fe5659baffe"
   }
```

`],`

```json
  "Size":20,
  "Total":1,
  "Current":1
 },
 "Code":200
}
```

#### ListAllDomains

查询所有域名列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |
| -domainId | String | domain-123456 | 域名ID |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -certificateId | String | cert-987654 | 证书ID |
| - certificateNam e | String | MyCert | 证书名称 |
| -domain | String | api.example.com | 域名 |
| -protocol | String | HTTP | 协议 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -clientAuth | Integer | 1 | 客户端认证方式 |
| - caCertificateId | String | cert-123456 | CA证书ID |
| - caCertificateN ame | String | MyCA | CA证书名称 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetDomain

查询域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -routeInfos | Array | [] | 路由信息列表 |
| --routeId | String | route-123456 | 路由ID |
| --routeName | String | user-service-route | 路由名称 |
| --serviceId | String | service-123456 | 服务ID |
| --serviceName | String | user-service | 服务名称 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -domainId | String | domain-123456 | 域名ID |
| -domain | String | api.example.com | 域名 |
| -protocol | String | HTTP | 协议 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -certificateId | String | cert-987654 | 证书ID |
| -clientAuth | Integer | 1 | 客户端认证方式 |
| - caCertificateId | String | cert-123456 | CA证书ID |
| -subjectDn | String | CN=example.com, O=Example,C=CN | 证书主题DN |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -issuerDn | String | CN=Example CA, O=Example Inc, C=CN | 颁发者DN |

#### CreateDomain

创建域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| protocol | Strin g | Body | 否 | HTTP | 协议 |
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| domain | Strin g | Body | 否 | api.example.com | 域名 |
| clientAuth | Integ er | Body | 否 | 1 | 客户端认证方式 |
| caCertific ateId | Strin g | Body | 否 | cert-123456 | CA证书ID |
| subjectDn | Strin g | Body | 否 | CN=example.com,O=Ex ample,C=CN | 证书主题DN |
| issuerDn | Strin g | Body | 否 | CN=Example CA, O=Example Inc, C=CN | 颁发者DN |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 数据 |

#### ModifyDomain

修改域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| protocol | Strin g | Body | 否 | HTTP | 协议 |
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| domain | Strin g | Body | 否 | api.example.com | 域名 |
| clientAuth | Integ er | Body | 否 | 1 | 客户端认证方式 |
| caCertific ateId | Strin g | Body | 否 | cert-123456 | CA证书ID |
| subjectDn | Strin g | Body | 否 | CN=example.com,O=Ex ample,C=CN | 证书主题DN |
| issuerDn | Strin g | Body | 否 | CN=Example CA, O=Example Inc, C=CN | 颁发者DN |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteDomain

删除域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| domainId | Strin g | Body | 否 | domain-123456 | 域名ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

### 证书管理

#### ListCertificates

查询证书列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | Integ er | Body | 否 | 100 | 大小 |
| current | Integ er | Body | 否 | 1 | 当前页码 |
| sni | Strin g | Body | 否 | example.com | SNI域名 |

| PI 网关 |  |  |  |  | 开发指南·API 网关 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certType | Integ er | Body | 否 | 1 | 证书类型 |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -records | Array | [] | 记录列表 |
| --snis | String | [] | SNI域名列表 |
| --expireTime | String | 2025-10-14 23:59:59 | 过期时间 |
| --updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| --createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| -- certificateNam e | String | MyCert | 证书名称 |
| --certificateId | String | cert-987654 | 证书ID |
| --certType | Integer | 1 | 证书类型 |
| -size | Integer | 100 | 大小 |
| -total | Integer | 1000 | 总数 |
| -current | Integer | 1 | 当前页码 |

#### ListAllServerCertificates

查询所有服务器证书列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Map | {} | 数据 |

#### ListAllCACertificates

查询所有CA证书列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| serviceTy pe | Integ er | Body | 否 | REST | 服务类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 数据 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -snis | String | [] | SNI域名列表 |
| -expireTime | String | 2025-10-14 23:59:59 | 过期时间 |
| -updateTime | String | 2024-10-14 15:00:00 | 更新时间 |
| -createTime | String | 2024-10-14 08:00:00 | 创建时间 |
| - certificateNam e | String | MyCert | 证书名称 |
| -certificateId | String | cert-987654 | 证书ID |
| -certType | Integer | 1 | 证书类型 |
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

#### GetCertificate

查询证书。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -snis | String | [] | SNI域名列表 |
| -signTime | String | 2024-10-14 10:30:00 | 签名时间 |
| -expireTime | String | 2025-10-14 23:59:59 | 过期时间 |
| -algorithm | String | sha256 | 算法类型 |
| - privateKeyLen | Integer | 2048 | 私钥长度 |
| -fingerPrint | String | a1b2c3d4e5f6 | 指纹 |
| -signerCN | String | Example Corp | 签名者通用名 |
| -signerOU | String | IT Department | 签名者组织单位 |
| - certificateNam e | String | MyCert | 证书名称 |
| -certificateId | String | cert-987654 | 证书ID |
| -domainId | String | domain-123456 | 域名ID |
| -certType | Integer | 1 | 证书类型 |
| -SN | String | SN12345678 | 序列号 |

#### CreateCertificate

创建证书。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| certificate s | Strin g | Body | 否 | cert1,cert2 | 证书列表 |
| privateKe y | Strin g | Body | 否 | -----BEGIN PRIVATE KEY-- --- | 私钥 |
| certificate Name | Strin g | Body | 否 | MyCert | 证书名称 |
| certType | Integ er | Body | 否 | 1 | 证书类型 |
| isImport | Boole an | Body | 否 | false | 是否导入 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### ModifyCertificate

修改证书。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |
| certificate s | Strin g | Body | 否 | cert1,cert2 | 证书列表 |

| 开发指南·API 网 | 关 |  |  |  | API 网关 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| privateKe y | Strin g | Body | 否 | -----BEGIN PRIVATE KEY-- --- | 私钥 |
| certificate Name | Strin g | Body | 否 | MyCert | 证书名称 |
| certType | Integ er | Body | 否 | 1 | 证书类型 |
| isImport | Boole an | Body | 否 | false | 是否导入 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | String | {} | 数据 |

#### DeleteCertificate

删除证书。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certificate Id | Strin g | Body | 否 | cert-987654 | 证书ID |
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 数据 |

### 其他

#### GetTotalityInfo

查询总体信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanc eId | Strin g | Body | 否 | i-c0a81bb16a1524a17 | 网关实例ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| -routeTotal | Integer | 150 | 路由总数 |
| -serverCount | Integer | 5 | 服务器数量 |
| - interfaceCount | Integer | 50 | 接口数量 |
| - todayRequest Count | Integer | 15000 | 今日请求数 |
| - portalAppTotal | Integer | 50 | 门户应用总数 |
| -backAppTotal | Integer | 10 | 后端应用总数 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - mcpServerCou nt | Integer | 3 | MCP服务器数量 |
| -strategyCount | Integer | 5 | 策略数量 |

#### GetSettings

查询系统设置参数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| brokerEng ineType | Strin g | Body | 否 | RocketMQ | 消息引擎类型 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 响应码 |
| msg | String | 操作成功 | 消息 |
| data | Struct | {} | 数据 |
| - supportDeploy Modes | String | [] | 支持的部署模式列表 |
| -licenseInfoList | Array | [] | 许可证信息列表 |
| --region | String | cn-hangzhou | 地域 |
| --vcpuCount | Integer | 4 | 虚拟CPU核数 |
| --upLimitNum | Integer | 10000 | 上限数量 |
| --routeCount | Integer | 25 | 路由数量 |

| PI 网关 |  |  | 开发指南·API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --aiProxyCount | Integer | 10 | AI代理数量 |
| --percentage | Float | 85.5 | 百分比 |
| --warn | Boolean | false | 是否警告 |
| --error | Boolean | false | 是否错误 |
| - capacityPlatfor mEnable | Boolean | true | 是否启用容量平台 |
| -licenseEnable | Boolean | true | 是否启用许可证 |
| - customPluginE nable | Boolean | true | 是否启用自定义插件 |

#### GetSlsStatistics

查询SLS统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| body | Strin g | Body | 否 | {"key":"value"} | 请求体内容 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | Integer | 200 | 响应码 |
| Msg | String | 操作成功 | 消息 |
| Data | Struct | {} | 数据 |
| -Records | Array | [] | 记录列表 |

| 开发指南·API 网关 |  |  | API 网关 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ServiceId | String | service-123456 | 服务ID |
| -- ServiceGroupI d | String | group-001 | 服务组ID |
| --ConsumerId | String | consumer-123 | 消费者ID |
| --Time | String | 2024-10-14 14:00:00 | 时间 |
| --InputToken | Long | 1024 | 输入令牌数 |
| --OutputToken | Long | 2048 | 输出令牌数 |
| -- TotalRequestC ount | Long | 500000 | 总请求数 |
| -- FailedRequest Count | Long | 150 | 失败请求数 |
| -Total | Long | 1000 | 总数 |
| -Current | Long | 1 | 当前页码 |
| -Size | Long | 100 | 大小 |
