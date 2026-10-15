---
title: "智能体工厂 OpenTrek AI网关 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 413
source_pdf: "42_AI网关 开发指南_ai-gateway-development-guide-1.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/opentrek/zh/ai-gateway-development-guide-1.pdf"
converter: line-classifier (PyMuPDF)
---

# 智能体工厂 OpenTrek AI网关 开发指南

智能体工厂 OpenTrek

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
智能体工厂 OpenTrek
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

智能体工厂 OpenTrek

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
智能体工厂 OpenTrek

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

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中 AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取 STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey 相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |

智能体工厂 OpenTrek

| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
|---|---|
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
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
智能体工厂 OpenTrek
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调用成功
后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源集ID。接
口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以API网关为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品** > **中间件** > **应用集成** > **API** **网关**。
3. 在左侧导航栏中，单击**实例列表**。
4. 在实例列表中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

智能体工厂 OpenTrek

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择利用STS方式，调用专有云的产品API。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 使用以下代码，通过角色的 `RAM Role` 获得 `stsAK` 、 `stsSK` 和 `stsToken` 。
智能体工厂 OpenTrek

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
智能体工厂 OpenTrek

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
iv. 设置**管理权限**，在权限列表勾选**查看****RAM****服务角色**和**创建****RAM****服务角色**权限后，单击**下一步**。 v. 设置**应用权限**，在权限列表勾选**API****网关**的**只读权限**和**读写权限**后，单击**下一步**。 vi. 设置**菜单权限**，在列表勾选**API****网关**后，单击**下一步**或**创建**。
4. 为用户添加角色。
i. 在左侧导航栏，选择**人员管理** > **用户管理**。 ii. 在**系统用户**页签，找到新创建的用户，单击用户**操作**列的 ，选择**角色授权**。 iii. 在**角色授权**对话框，添加新创建的用户角色后，单击**确定**。
5. 将用户添加到资源集。
i. 在**系统用户**页签，找到新创建的用户，单击用户名。 ii. 在**所属资源集**页签下，单击列表上方的**加入资源集**。 智能体工厂 OpenTrek iii. 在**加入资源集**对话框中，**选择角色类型**下拉列表选择用户的角色，**选择资源集**列表勾选需要加入的资源集，单击**确定**。

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
智能体工厂 OpenTrek

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

**代码示例**

智能体工厂 OpenTrek 以下示例展示如何使用 common request 方式调用 API 网关控制台接口：

```java
package com.aliyun.apsarastack; import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONArray; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.AcsResponse; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.HttpResponse; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; /**
```

`* API`网关控制台 `Common Request` 调用示例 `*/`

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
        CommonResponse response = getCommonResponse(request, LIST_ROUTES, MethodType.POST);
        HttpResponse httpResponse = response.getHttpResponse();
        if (httpResponse.getStatus() == 200) {
            JSONObject jsonObject = JSON.parseObject(httpResponse.getHttpContentString());
            if (Integer.parseInt(jsonObject.get("code").toString()) == 200) {
                Object data = jsonObject.get("data");
                if (data instanceof JSONObject) {
                    JSONObject dataObj = (JSONObject) data;
                    JSONArray records = (JSONArray) dataObj.get("records");
                    records.forEach(record -> {
                        System.out.println(JSON.toJSONString(record));
                    });
                }
```

智能体工厂 OpenTrek

```java
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
    public static CommonResponse getCommonResponse(Object param, String path, MethodType
methodType) throws ClientException {
        CommonRequest request = new CommonRequest();
        request.setSysUriPattern(path);
        request.setHttpContent(JSONObject.toJSONBytes(param), "UTF-8", FormatType.JSON);
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
    private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request,
MethodType methodType) {
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

智能体工厂 OpenTrek `//` 设置请求方式

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
设置必要的 Header 信息： 智能体工厂 OpenTrek

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

智能体工厂 OpenTrek

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
} private static <T extends AcsResponse> void initDefaultHeader(CommonRequest request, MethodType methodType) {
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

本文档描述API网关控制台的通用接口调用方式，包括请求格式、响应格式、认证方式等。适用于API网关（SCG）和 AI网关（Higress）的所有接口。

**接口基本信息**

| 项目 | 说明 |
|---|---|
| 接口协议 | HTTP/HTTPS |

智能体工厂 OpenTrek

| 请求方式 | POST（主要）、GET |
|---|---|
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

智能体工厂 OpenTrek

| data | Object | 响应数据（业务数据）。 |
|---|---|---|

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

智能体工厂 OpenTrek

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

| 方式 | 说明 |  |  |
|---|---|---|---|
| 请求头 | Authorization: Bearer <api-key> 或 x-api- key: <api-key> 。 |  |  |
|  |  | x-api- |  |
| 查询参数 | ?api key=<api-key> 。 _ |  |  |

|  |  | Authorization: Bearer <api-key> |
|---|---|---|
|  | key: <api-key> |  |

具体认证方式由网关实例的认证配置决定。

**通用参数说明**

**网关实例ID（gwInstanceId）**

大部分接口需要传入网关实例ID，用于区分操作的目标实例。系统会根据实例ID自动识别网关类型（API网关或AI网关），并执行相应的处理逻辑。

**分页参数**

列表查询接口支持分页参数：

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| current | Integer | 1 | 当前页码。 |
| size | Integer | 10 | 每页条数。 |

| AI Gateway 开发指南·通过P 调用专有云API | OP网关 |  | 智能体工厂 OpenTre |
|---|---|---|---|

**搜索参数**

列表查询接口支持搜索参数：

| 参数 | 类型 | 说明 |
|---|---|---|
| searchName | String | 搜索关键字（按名称模糊匹配）。 |

**接口分类概览**

**API网关(SCG)接口**

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
| 实例管理 | /gatewayInstance | 网关实例管理。 |
| 集群管理 | /k8sCluster | K8s集群管理。 |

**AI网关（Higress）接口**

| 模块 | 接口路径 | 说明 |
|---|---|---|
| 插件管理 | /plugin | Wasm插件管理。 |

智能体工厂 OpenTrek

| 全局插件 | /globalPlugin | 全局插件配置。 |
|---|---|---|
| MCP管理 | /mcpServer | MCP服务器管理。 |
| 模型API | /modelapi | 模型API管理。 |
| 策略配置 | /strategyConfig | 插件策略配置。 |

**说明**

AI网关的路由、服务、域名、消费者、证书管理与API网关共用接口路径，但实现逻辑不同。

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

示例： 智能体工厂 OpenTrek

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
智能体工厂 OpenTrek 操作前确认 `gwInstanceId` 对应的网关类型。 API网关和AI网关部分接口共用路径但行为不同。 通过 `/gatewayInstance/getInstance` 查询实例详情确认类型。

#### API 调用-集群管理

**概述**

集群管理模块提供Kubernetes集群的导入、查询、更新等功能。集群是网关实例的部署环境，支持自建 Kubernetes和容器服务Kubernetes两种类型。
**适用引擎**：SCG / Higress
**API****路径前缀**： `/k8s`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，并使用有
效的 AK/SK。

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
| k8sClusterName | String | 是 | 集群名称，长度为2-128字符，以英文字母开头。 |
| k8sClusterType | String | 否 | 集群类型： self-built：自建K8s container-service：容器服务K8s |

智能体工厂 OpenTrek

| configContent | String | 条件必填 | KubeConfig配置内容。 说明自建集群时必填。 |
|---|---|---|---|
| k8sClusterAttribute | Object | 条件必填 | 集群扩展属性。 说明容器服务集群时必填。 |

**k8sClusterAttribute 结构**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| csClusterId | String | 条件必填 | 容器服务集群ID。 说明 container- service 类型时必填。 |

|  |  |  | container- |  |
|---|---|---|---|---|
|  |  | service |  |  |

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

智能体工厂 OpenTrek

| size | Integer | 是 | 每页条数。 |
|---|---|---|---|
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

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clusterCode | String | 是 | 集群编码。 |
| k8sClusterAttribute | String | 是 | 集群扩展属性（JSON字符串）。 |

| AI Gateway 开发指南·通过P 调用专有云API | OP网关 |  | 智能体工厂 OpenTre |
|---|---|---|---|

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
| Content-Type | application/json |

**请求参数（基于 CheckK8sClusterConnectRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| clusterCode | String | 是 | 集群编码。 |

智能体工厂 OpenTrek

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
| Content-Type | application/json |

**请求参数（基于 GetK8sClusterInfoRequest）**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| gwInstanceId | String | 是 | 网关实例ID。 |

**Common Request 调用示例**

以下示例展示如何使用 Common Request 方式调用集群管理 API。自建ACK环境和企业版环境的区别仅在于认证参数的设置。

```java
importcomalibabafastjsonJSON;
```

智能体工厂 OpenTrek

|  | import com.alibaba.fastjson.JSON; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; import java.util.HashMap; import java.util.Map; public class ClusterApiDemo { // ========== 环境配置（根据实际环境修改） ========== private static final boolean IS SELF HOSTED = true; _ _ private static final String SELF HOSTED ENDPOINT = "127.0.0.1:8080"; _ _ private static final String ENTERPRISE ENDPOINT = "csb.cn-****.aliyuncs.com"; _ private static final String ACCESS KEY ID = "your-access-key-id"; _ _ private static final String ACCESS KEY SECRET = "your-access-key-secret"; _ _ private static final String ORGANIZATION ID = "your-org-id"; _ public static void main(String[] args) throws Exception { IAcsClient client = createClient(); // ========== 导入自建K8s集群 ========== String clusterCode = importSelfBuiltCluster(client); // ========== 导入容器服务K8s集群 ========== // String csClusterCode = importContainerServiceCluster(client); // ========== 测试集群连接 ========== checkConnect(client, clusterCode); // ========== 查询集群列表 ========== listClusters(client); // ========== 查询全部集群 ========== getClusterList(client); // ========== 查询集群名称 ========== getK8sClusterName(client, clusterCode); // ========== 取消导入集群 ========== // cancelImportCluster(client, clusterCode); } private static IAcsClient createClient() { if (IS SELF HOSTED) { _ _ DefaultProfile profile = DefaultProfile.getProfile("-", "-", "-"); return new DefaultAcsClient(profile); } else { DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", ACCESS KEY ID, AC _ _ CESS KEY SECRET); _ _ return new DefaultAcsClient(profile); } |  |
|---|---|---|

智能体工厂 OpenTrek

```java
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
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-self-built-cluster");         // 【必填】集群名称
        request.put("k8sClusterType", "self-built");                    // 【可选】集群类型：self-b
uilt
        request.put("configContent", "your-kubeconfig-content");        // 【必填】KubeConfig配置
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importSelfBuiltCluster success, clusterCode: " + clusterCode);
            return clusterCode;
        } else {
            System.out.println("importSelfBuiltCluster failed: " + result.getString("msg"));
            return null;
        }
    }
    /**
```

* 导入容器服务`Kubernetes`集群（基于 `ImportK8sClusterRequest`）
`*/`

```
privatestaticStringimportContainerServiceCluster(IAcsClientclient)throwsException{
```

智能体工厂 OpenTrek

```java
    private static String importContainerServiceCluster(IAcsClient client) throws Exception {
        Map<String, Object> attribute = new HashMap<>();
        attribute.put("csClusterId", "ce********b5587f5ec1c");  // 【必填】容器服务集群ID
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterName", "my-cs-cluster");                  // 【必填】集群名称
        request.put("k8sClusterType", "container-service");              // 【必填】集群类型：
container-service
        request.put("k8sClusterAttribute", attribute);                   // 【必填】集群扩展属性
        CommonRequest commonRequest = createBaseRequest("/k8s/importCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        JSONObject result =
JSON.parseObject(response.getHttpResponse().getHttpContentString());
        if (result.getInteger("code") == 200) {
            String clusterCode = result.getString("data");
            System.out.println("importContainerServiceCluster success, clusterCode: " + cluster
Code);
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
        // request.put("clusterName", "");                                  // 【可选】集群名称（模
```

糊搜索）

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
```

智能体工厂 OpenTrek

```
    }
    /**
```

* 测试集群连接（基于 `CheckK8sClusterConnectRequest`）
`*/`

```java
    private static void checkConnect(IAcsClient client, String clusterCode) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编码
        CommonRequest commonRequest = createBaseRequest("/k8s/checkConnectCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getK8sClusterName(IAcsClient client, String clusterCode) throws Excepti
on {
        Map<String, Object> request = new HashMap<>();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编码
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
    private static void getK8sClusterInfoByGwInstanceId(IAcsClient client, String gwInstanceId)
throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】网关实例ID
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

`*/`

```java
    private static void updateCluster(IAcsClient client, String clusterCode) throws Exception
{
        Map<String, Object> request = new HashMap<>();
```

智能体工厂 OpenTrek p `g,` j q p

```
();
        request.put("clusterCode", clusterCode);                         // 【必填】集群编码
        request.put("k8sClusterAttribute", "{\"key\":\"value\"}");       // 【必填】集群扩展属性JS
```

`ON`

```java
        CommonRequest commonRequest = createBaseRequest("/k8s/updateCluster");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("updateCluster: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

* 取消导入集群（基于 `CancelImportK8sClusterRequest`）
`*/`

```java
    private static void cancelImportCluster(IAcsClient client, String clusterCode) throws Excep
tion {
        Map<String, Object> request = new HashMap<>();
        request.put("k8sClusterCode", clusterCode);                      // 【必填】集群编码
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

智能体工厂 OpenTrek

#### API 调用-实例管理

**概述**

实例管理模块提供网关实例的增删改查功能。实例是网关的运行实体，可在Kubernetes集群上部署，支持SCG和 Higress两种引擎类型。
**适用引擎**：SCG / Higress
**API****路径前缀**： `/gatewayInstance`

**认证方式**

**自建****ACK****环境**：需在请求Header中添加 `X-CSB-TOKEN: csb@2022` 和 `X-CSB-OPENAPI: true` 。
**企业版环境**：需在请求Header中添加 `x-acs-organizationid` 和 `x-acs-caller-sdk-source` ，并使用有
效的 AK/SK。

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
| gwInstanceName | String | 是 | 实例名称，长度为2-128字符，以英文字母开头。 |
| clusterCode | String | 是 | 集群编码。 |
| namespace | String | 是 | Kubernetes命名空间。 |
| brokerEngineType | String | 否 | 引擎类型： SCG HIGRESS SHARED SCG _ CLOUD NATIVE GATE _ _ WAY |

智能体工厂 OpenTrek

| deployMode | String | 否 | 部署模式：adp、edas、 tiangong、custom、k8s 等。 |
|---|---|---|---|
| instanceClass | String | 否 | 实例规格。 |
| instanceNumber | String | 否 | 实例节点数。 |
| vpcId | String | 否 | VPC ID。 |
| vswId | String | 否 | 虚拟交换机ID。 |
| ingressName | String | 否 | Ingress名称。 |
| deployConfigContent | String | 否 | 自定义部署配置。 |
| accessModeConfigConte nt | String | 否 | 访问模式配置。 |

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

智能体工厂 OpenTrek

| gwInstanceId | String | 否 | 实例ID筛选。 |
|---|---|---|---|
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

智能体工厂 OpenTrek

| gwInstanceId | String | 是 | 实例ID。 |
|---|---|---|---|

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

智能体工厂 OpenTrek

| gwInstanceId | String | 是 | 实例ID。 |
|---|---|---|---|

**重启实例**

**接口说明**

重启指定的网关实例。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/restartInstance |
| Method | POST |
| Content-Type | application/json |

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

智能体工厂 OpenTrek

**接口说明**

升级实例到最新版本。

**请求信息**

| 项目 | 内容 |
|---|---|
| URL | /gatewayInstance/upgradeInstance |
| Method | POST |
| Content-Type | application/json |

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

智能体工厂 OpenTrek

| specificationTemplate | Integer | 否 | 规格模板。 |
|---|---|---|---|

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
    private static final String ORGANIZATIONID = "your-org-id";
```

智能体工厂 OpenTrek p g _ y g

```
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
            DefaultProfile profile = DefaultProfile.getProfile("cn-hangzhou", ACCESS_KEY_ID, AC
CESS_KEY_SECRET);
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
```

智能体工厂 OpenTrek

```
    /**
```

* 创建实例（基于 `CreateGwInstanceRequest`）
`*/`

```java
    private static String createInstance(IAcsClient client) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceName", "my-gateway-instance");            // 【必填】实例名称
        request.put("clusterCode", "cluster-code-xxx");                  // 【必填】集群编码
        request.put("namespace", "default");                             // 【必填】K8s命名空间
        request.put("brokerEngineType", "SCG");                          // 【可选】引擎类型：SCG/H
        // request.put("deployMode", "adp");                                // 【可选】部署模式
        // request.put("instanceClass", "standard");                        // 【可选】实例规格
        // request.put("instanceNumber", "2");                              // 【可选】节点数
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/createInstance");
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
        // request.put("name", "");                                         // 【可选】实例名称（模
```

糊搜索）

```java
        // request.put("brokerEngineType", "SCG");                          // 【可选】引擎类型筛选
        // request.put("status", 2);                                        // 【可选】状态筛选：2-r
unning
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/listInstances");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("listInstances: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void getInstanceInfo(IAcsClient client, String gwInstanceId) throws
```

智能体工厂 OpenTrek

```
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/getInstanceInfo");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void modifyInstance(IAcsClient client, String gwInstanceId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        request.put("instanceName", "modified-instance-name");           // 【必填】新实例名称
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/modifyInstance");
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
    private static void getResource(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/getResource");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("getResource: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void modifyResource(IAcsClient client, String gwInstanceId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        request.put("instanceClass", "large");                           // 【可选】实例规格
        request.put("instanceNumber", 3);                                // 【可选】节点数
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/modifyResource");
commonRequestsetHttpContent(JSONObjecttoJSONBytes(request) "UTF-8"
```

智能体工厂 OpenTrek

```java
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), UTF-8,
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("modifyResource: " +
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void restartInstance(IAcsClient client, String gwInstanceId) throws
Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/restartInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
response.getHttpResponse().getHttpContentString());
    }
    /**
```

`*/`

```java
    private static void stopInstance(IAcsClient client, String gwInstanceId) throws Exception {
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/stopInstance");
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
    private static void deleteInstance(IAcsClient client, String gwInstanceId) throws Exception
{
        Map<String, Object> request = new HashMap<>();
        request.put("gwInstanceId", gwInstanceId);                       // 【必填】实例ID
        CommonRequest commonRequest = createBaseRequest("/gatewayInstance/deleteInstance");
        commonRequest.setHttpContent(JSONObject.toJSONBytes(request), "UTF-8",
FormatType.JSON);
        CommonResponse response = client.getCommonResponse(commonRequest);
        System.out.println("deleteInstance: " +
response.getHttpResponse().getHttpContentString());
    }
}
```

智能体工厂 OpenTrek

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

智能体工厂 OpenTrek

| 500 | 服务器内部错误。 |
|---|---|

智能体工厂 OpenTrek

## API参考

### AI服务

#### batchDeletesServices

**API 接口概述**

**中文名称：**批量删除服务
**功能概述：**服务管理 - 批量删除服务。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| serviceIds | string[] | body |  |  |  | ["service- |  |  |  |
|  |  |  |  |  |  |  | ["service- |  |  |
|  |  |  |  |  |  | 001", |  |  |  |
|  |  |  |  |  |  |  |  | 服务ID |  |
|  |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  | "service- |  |  |  |
|  |  |  |  |  |  | 002"] |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.successIds | string[] | ["service-001"] | 成功删除的服务ID列表。 |

智能体工厂 OpenTrek

| data.failedIds | string[] | ["service-002"] | 删除失败的服务ID列表。 |
|---|---|---|---|

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceIds": []
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "successIds": [],
        "failedIds": []
    }
}
```

#### createMicroservice

**API 接口概述**

**中文名称：**创建服务
**功能概述：**服务管理 - 创建服务。
**请求路径：** `/microservice/createService`
**请求方式：** `POST`
**区分说明**：此接口同时用于创建 AI服务和普通服务，通过参数区分：

| serviceSourceType: 9 传其他类型值，支持： 1 ( |  |  |
|---|---|---|
|  | 1 | ( |

名)

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string |  |  | body |  |  |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| description | string |  |  | body |  |  |  | 否 |  | 通义千问AI服务 |  | 服务描述，长度不超过200字符。 |  |
| serviceType | integer |  |  | body |  |  |  | 否 |  | 1 |  | 服务类型。 |  |
| name | string |  |  | body |  |  |  | 是 |  | qwen- service |  | 服务名称。AI服务命名规则：小写字母、数字、 点(.)和减号(-)， 长度不超过50， 不能以减号开头或结尾。 |  |
| upstreamType | integer |  |  | body |  |  |  | 否 |  | 1 |  | 上游类型。 |  |
| serviceSourceT ype | integer |  |  | body |  |  |  | 否 |  | 9 |  | 服务来源类型。AI服务传 9 ；普通服务可选值： 1 (Naco s服务发现)、 4 (K8s 集群)、 7 (固定地址)、 8 (DNS 域名)。 |  |
| serviceName | string |  |  | body |  |  |  | 否 |  | qwen- service |  | 服务名称。 |  |
| loadBalanceTy pe | integer |  |  | body |  |  |  | 否 |  | 1 |  | 负载均衡算法类型。 |  |
| serviceStruct | object |  |  | body |  |  |  |  |  | {"provider": |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"provider": |  |  |
|  |  |  |  |  |  |  |  |  |  | "qwen","aiPro |  |  |  |
|  |  | object |  |  | body |  |  |  |  |  |  | 服务配置结构。 |  |
|  |  |  |  |  |  |  |  | 否 |  |  |  | 服 |  |
|  |  |  |  |  |  |  |  |  |  | tocol":"opena |  |  |  |
|  |  |  |  |  |  |  |  |  |  | i"} |  |  |  |
| isOpenHealthC heck | boolean |  |  | body |  |  |  | 否 |  | false |  | 是否开启健康检查。 |  |
| healthCheckStr uct | object |  |  | body |  |  |  | 否 |  | {"type":1,"t |  | 健康检查配置。 |  |
|  |  |  |  |  |  |  |  |  |  |  | {"type":1,"t |  |  |
|  |  |  |  |  |  |  |  |  |  | imeout":5} |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | 通义千问AI服 |
|---|---|---|
|  | 务 |  |

|  |  | qwen- |
|---|---|---|
|  | service |  |

|  |  | qwen- |
|---|---|---|
|  | service |  |

智能体工厂 OpenTrek

| activeHealthCh eckStruct | object | body | 否 | {"enable":fa lse} | 主动健康检查配置。 |
|---|---|---|---|---|---|
| protocol | string | body | 是 | HTTP | 服务协议。AI服务默认为 HTTP 。 |
| serviceId | string | body | 否 | service- 001 | 服务ID。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| proxyServerNa me | string | body | 否 | proxy-001 | 代理服务器名称。 |

|  |  | {"enable":fa | 主动 |
|---|---|---|---|
|  | lse} |  |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

**healthCheckStruct 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | integer | body | 否 | 1 | 类型。 |
| healthPath | string | body | 否 | /health | 健康检查路径。 |
| httpStatuses | string | body | 否 | 200,301,302 | HTTP状态码。 |
| timeout | integer | body | 否 | 5 | 超时时间 （秒）。 |
| healthInterval | integer | body | 否 | 10 | 健康检查间隔。 |
| unHealthInterv al | integer | body | 否 | 30 | 不健康检查间隔。 |
| httpSuccesses | integer | body | 否 | 3 | HTTP成功次数阈值。 |
| httpFailures | integer | body | 否 | 3 | HTTP失败次数阈值。 |

|  |  | 200,301,302 |
|---|---|---|

**activeHealthCheckStruct 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| enable | boolean | body | 否 | false | 是否启用。 |
|---|---|---|---|---|---|
| protocol | string | body | 否 | HTTP | 服务协议。AI服务默认为 HTTP 。 |
| timeout | integer | body | 否 | 5 | 超时时间 （秒）。 |
| interval | integer | body | 否 | 10 | 检查间隔 （秒）。 |
| healthyThresho ld | integer | body | 否 | 3 | 健康阈值。 |
| unhealthyThres hold | integer | body | 否 | 3 | 不健康阈值。 |
| httpPath | string | body | 否 | /health | HTTP路径。 |
| httpHost | string | body | 否 | localhost | HTTP Host头。 |
| expectedStatus es | string[] | body | 否 | ["200"] | 期望的状态码列表。 |

**serviceStruct 对象结构**

**说明**：serviceStruct 根据 `serviceSourceType` 参数有不同的字段结构：

**当 serviceSourceType=9（AI服务）时：**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| provider | string | body | 是 | qwen | AI提供商类型。 可选值： selfbuil d (自建)、 qwen ( 通义千问)、 deepsee k 、 openai 、 azure 、 gemini 、 bedrock 、 c laude 、 moo nshot (月之暗面)、 baichua n (百川)、 yi (零一万物)、 zhipuai (智谱)、 hunyuan (混元)、 stepfun (阶跃)、 spark ( 讯飞星火)、 doubao (豆包)、 minimax 、 vertex ( Vertex AI)。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | azure |  |  |  |
|  |  |  |  |  |  |  | 、 、 |  |  |
|  |  |  |  |  |  |  |  | c |  |
|  |  |  |  |  |  |  | moo |  |  |
| aiProtocol | string | body | 是 | openai | AI协议类型。可选值： openai ( OpenAI/V1标准协议)、 origina l (原始协议)。 |  |  |  |  |

|  | d |
|---|---|

|  |  |  |  | k |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | bedrock |  |  |
|  |  |  |  | laude |  |  |
|  |  |  |  | nshot |  |  |

|  | n |
|---|---|

|  | l |
|---|---|

智能体工厂 OpenTrek

| baseUrl | string | body |  |  | 否 |  |  | https://api. |  |  |  | AI服务基础URL 地址。部分提供商有默认值，如 qwen 默认为 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | https://api. |  |  |  | https:/ | /dash |  |
|  |  |  |  |  |  |  |  | ope |  | nai.com |  | scope.aliyunc |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | s.com/compati |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | ble- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | mode/v1 |  |  |  |
| apiKeyList | string[] | body |  |  | 否 |  |  | ['sk- xxx'] |  |  |  | API Key列表。支持配置多个 API Key 实现负载均衡和容灾。自建 LLM时可省略。 |  |  |  |

**当 serviceSourceType 为其他值（普通服务）时：**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|
| nodes | object[] | body | 否 |  | [{"ip":"192. |  | 服务节点列表。 当 |  |
|  |  |  |  |  |  | [{"ip":"192. | serviceSourceT ype=7( |  |
|  |  |  |  |  | 168.1.1","por |  | ype=7( |  |
|  |  |  |  |  |  |  | 固址)或 |  |
|  |  |  |  |  | t":8080}] |  |  |  |
| sourceGroup | string | body | 否 |  | DEFAULT GROU _ P |  | Nacos分组名。 当 serviceSourceT ype=1(NACOS) 时使用，默认值为 DEFAULT GROU _ P 。 |  |
| sourceNamesp aceId | string | body | 否 |  | namespace- 001 |  | Nacos命名空间 ID。当 serviceSourceT ype=1(NACOS) 时使用。 |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | namespace- |  |
|---|---|---|---|
|  | 001 |  |  |

**nodes 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ip | string | body | 是 | 192.168.1.1 | 节点IP地址。 |
| port | integer | body | 是 | 8080 | 节点端口。 |

|  |  | 192.168.1.1 |
|---|---|---|

智能体工厂 OpenTrek

| weight | integer | body | 否 | 1 | 节点权重，用于负载均衡。默认值为 1。 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | true | 节点是否启用。 默认值为 true。 |
| vpcId | string | body | 否 | vpc-xxx- xxx | VPC ID（跨VPC 场景）。 |
| vpcMappingIp | string | body | 否 | 10.0.0.1 | VPC映射IP。 |
| vpcMappingPor t | integer | body | 否 | 8080 | VPC映射端口。 |

|  |  | vpc-xxx- |
|---|---|---|
|  | xxx |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | service-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /microservice/createService HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "description": "description_value",
  "serviceType": 0,
  "name": "name_value",
  "upstreamType": 0,
  "serviceSourceType": 9,
  "serviceName": "serviceName_value",
  "loadBalanceType": 0,
  "serviceStruct": {
    "provider": "qwen",
    "aiProtocol": "openai",
    "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "apiKeyList": [
      "sk-xxxxx"
```

]

```json
  },
  "isOpenHealthCheck": true,
  "healthCheckStruct": {
    "type": 0,
    "healthPath": "healthPath_value",
    "httpStatuses": "httpStatuses_value",
    "timeout": 0,
    "healthInterval": 0,
    "unHealthInterval": 0,
    "httpSuccesses": 0,
    "httpFailures": 0
  },
  "activeHealthCheckStruct": {
    "enable": true,
    "protocol": "protocol_value",
    "timeout": 0,
    "interval": 0,
    "healthyThreshold": 0,
    "unhealthyThreshold": 0,
    "httpPath": "httpPath_value",
    "httpHost": "httpHost_value",
    "expectedStatuses": []
  },
  "protocol": "protocol_value",
  "serviceId": "serviceId_value",
  "isDisasterRecovery": true,
  "proxyServerName": "proxyServerName_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteService

**API 接口概述**

**中文名称：**删除服务
**功能概述：**服务管理 - 删除服务。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| serviceId | string | body | 是 | service- 001 | 服务ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | service-001 | 响应数据。 |

**示例**

智能体工厂 OpenTrek

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceId": "serviceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getAllService

**API 接口概述**

**中文名称：**查询所有服务
**功能概述：**服务管理 - 查询所有服务列表。

```
请求路径： /microservice/listAllServices
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 智能体工厂 OpenTrek |  | AI | Gateway 开发指南·API参考 |
|---|---|---|---|

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | ServiceInfoResponse[ ] | - | 响应数据。 |
| data.serviceId | string | service-001 | 服务ID。 |
| data.serviceName | string | my-service | 服务名称。 |
| data.protocol | string | HTTP | 协议类型。 |

|  |  | ServiceInfoResponse[ |  |
|---|---|---|---|
| a | ] |  |  |

**示例**

**请求示例**

```json
POST /microservice/listAllServices HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": [
        {
            "serviceId": "service-001",
            "serviceName": "demo-service",
            "protocol": "HTTP"
        },
        {
            "serviceId": "service-002",
            "serviceName": "another-service",
            "protocol": "gRPC"
        }
```

]

```
}
```

#### getService

**API 接口概述**

**中文名称：**查询服务详情
**功能概述：**服务管理 - 根据ID查询服务。
**请求方式：** `POST`
**区分说明**：此接口同时支持查询 AI服务和普通服务的详情，根据 serviceId 查询，返回数据中 `sourceType=9` 表
示 AI服务。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| serviceId | string | body | 是 | service- 001 | 服务ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.serviceId | string | service-001 | 服务ID。 |
| data.name | string | qwen-service | 名称。 |
| data.serviceName | string | qwen-service | 服务名称。 |
| data.description | string | 通义千问AI服务 | 描述信息。 |
| data.createTime | string | 2024-01-01 12:00:00 | 创建时间。 |
| data.updateTime | string | 2024-01-01 12:00:00 | 更新时间。 |
| data.creator | string | admin | 创建者。 |
| data.updater | string | admin | 更新者。 |
| data.protocol | string | HTTP | 协议类型。 |
| data.serviceType | integer | 1 | 服务类型。 |
| data.upstreamType | integer | 1 | 上游类型。 |
| data.upstreamTypeNam e | string | AI服务 | upstreamTypeName字段。 |
| data.loadBalanceType | integer | 1 | 负载均衡算法类型。 |
| data.loadBalanceTypeNa me | string | 轮询 | loadBalanceTypeName字段。 |

智能体工厂 OpenTrek

| data.routeList |  | GetServiceInfoByIdRe sponse$RouteInfo[] |  |  |  | [] |  | routeList字段。 |
|---|---|---|---|---|---|---|---|---|
| data.routeList.routeId |  | string |  |  |  | route-001 |  | 路由ID。 |
| data.routeList.routeNam e |  | string |  |  |  | my-route |  | 路由名称。 |
| data.routeList.routePath |  | string[] |  |  |  | ["/api/v1/*"] |  | 路由路径。 |
| data.sourceType |  | integer |  |  |  | 9 |  | 来源类型。 9 表示AI服务；其他值表示普通服务： 1 (Nacos)、 4 (K 8s集群)、 7 (固定地址)、 8 (DNS域名)。 |
| data.serviceSourceType |  | integer |  |  |  | 9 |  | 服务来源类型。同 sourceType。 |
| data.serviceAddress |  | string |  |  |  | qwen- service.example.com |  | 服务地址。 |
| data.port |  | integer |  |  |  | 8080 |  | 端口。 |
| data.serviceStruct |  | object |  |  |  | {"provider":"qwen"," |  | 服务配置结构。 |
|  |  |  |  |  |  |  | {"provider":"qwen"," |  |
|  |  |  | o | bject |  | aiProtocol":"openai"} |  |  |
| data.isOpenHealthCheck |  | boolean |  |  |  | false |  | 是否开启健康检查。 |
| data.healthCheckStruct |  | object |  |  |  | {} |  | 健康检查配置。 |
| data.healthCheckStruct.t ype |  | integer |  |  |  | 1 |  | 类型。 |
| data.healthCheckStruct. healthPath |  | string |  |  |  | /health |  | 健康检查路径。 |
| data.healthCheckStruct. httpStatuses |  | string |  |  |  | 200,301,302 |  | HTTP状态码。 |
| data.healthCheckStruct.t imeout |  | integer |  |  |  | 5 |  | 超时时间（秒）。 |

|  |  | GetServiceInfoByIdRe |  |
|---|---|---|---|
| a.routeList | sponse$RouteInfo[] |  |  |

|  |  | qwen- | 服务 |
|---|---|---|---|
|  | service.example.com |  |  |

智能体工厂 OpenTrek

| data.healthCheckStruct. healthInterval | integer | 10 | 健康检查间隔。 |
|---|---|---|---|
| data.healthCheckStruct. unHealthInterval | integer | 30 | 不健康检查间隔。 |
| data.healthCheckStruct. httpSuccesses | integer | 3 | HTTP成功次数阈值。 |
| data.healthCheckStruct. httpFailures | integer | 3 | HTTP失败次数阈值。 |
| data.activeHealthCheckS truct | object | {} | 主动健康检查配置。 |
| data.activeHealthCheckS truct.enable | boolean | false | 是否启用。 |
| data.activeHealthCheckS truct.protocol | string | HTTP | 协议类型。 |
| data.activeHealthCheckS truct.timeout | integer | 5 | 超时时间（秒）。 |
| data.activeHealthCheckS truct.interval | integer | 10 | 检查间隔（秒）。 |
| data.activeHealthCheckS truct.healthyThreshold | integer | 3 | 健康阈值。 |
| data.activeHealthCheckS truct.unhealthyThreshold | integer | 3 | 不健康阈值。 |
| data.activeHealthCheckS truct.httpPath | string | /health | HTTP路径。 |
| data.activeHealthCheckS truct.httpHost | string | localhost | HTTP Host头。 |
| data.activeHealthCheckS truct.expectedStatuses | string[] | ["200"] | 期望的状态码列表。 |
| data.activeHealthCheckS tatusStruct | object | {} | activeHealthCheckStatus Struct字段。 |
| data.activeHealthCheckS tatusStruct.healthStatus | string | healthy | healthStatus字段。 |

智能体工厂 OpenTrek

| data.activeHealthCheckS tatusStruct.unhealthyEn dpoints | string[] | [] | unhealthyEndpoints字段。 |
|---|---|---|---|
| data.zones | string[] | ["cn-hangzhou-a"] | zones字段。 |
| data.strategyConfigs | StrategyConfigRelati on[] | [] | strategyConfigs字段。 |
| data.strategyConfigs.stra tegyConfigId | string | strategy-001 | strategyConfigId字段。 |
| data.strategyConfigs.stra tegyConfigName | string | token-limit-config | strategyConfigName字段。 |
| data.strategyConfigs.stra tegyName | string | ai-token-limit | strategyName字段。 |
| data.strategyConfigs.stat us | boolean | true | 状态。 |
| data.strategyConfigs.sco pes | string[] | ["read","write"] | OAuth2授权范围。 |
| data.strategyConfigs.sco pe | object | {} | scope字段。 |
| data.strategyConfigs.sco pe.routeInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | [] | routeInfos字段。 |
| data.strategyConfigs.sco pe.routeInfos.name | string | my-route | 名称。 |
| data.strategyConfigs.sco pe.routeInfos.id | string | route-001 | ID标识。 |
| data.strategyConfigs.sco pe.serviceInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | [] | serviceInfos字段。 |
| data.strategyConfigs.sco pe.serviceInfos.name | string | qwen-service | 名称。 |
| data.strategyConfigs.sco pe.serviceInfos.id | string | service-001 | ID标识。 |

|  |  | StrategyConfigRelati | [ |  |
|---|---|---|---|---|
|  |  |  |  | [ |
| a.strategyConfigs | on[] |  |  |  |

|  |  | StrategyConfigScopeD | [] |
|---|---|---|---|
| routeInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD |  |
|---|---|---|---|
| a.strategyConfigs.sco serviceInfos | TO$ScopeTargetDTO[] |  |  |

智能体工厂 OpenTrek

| data.strategyConfigs.sco pe.appInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | [] | appInfos字段。 |
|---|---|---|---|
| data.strategyConfigs.sco pe.appInfos.name | string | my-consumer | 名称。 |
| data.strategyConfigs.sco pe.appInfos.id | string | app-001 | ID标识。 |
| data.strategyConfigs.sco pe.domainInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | [] | domainInfos字段。 |
| data.strategyConfigs.sco pe.domainInfos.name | string | api.example.com | 名称。 |
| data.strategyConfigs.sco pe.domainInfos.id | string | domain-001 | ID标识。 |
| data.strategyConfigs.sco pe.mcpServerInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | [] | mcpServerInfos字段。 |
| data.strategyConfigs.sco pe.mcpServerInfos.name | string | mcp-server-001 | 名称。 |
| data.strategyConfigs.sco pe.mcpServerInfos.id | string | mcp-001 | ID标识。 |
| data.strategyConfigs.sco pe.scopes | string[] | ["read","write"] | OAuth2授权范围。 |
| data.strategyConfigs.cre ateTime | string | 2024-01-01 12:00:00 | 创建时间。 |
| data.strategyConfigs.upd ateTime | string | 2024-01-01 12:00:00 | 更新时间。 |
| data.proxyServerName | string | proxy-001 | 代理服务器名称。 |

|  |  | StrategyConfigScopeD | [] |
|---|---|---|---|
| appInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | [] |
|---|---|---|---|
| domainInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | [] |
|---|---|---|---|
| mcpServerInfos | TO$ScopeTargetDTO[] |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceId": "serviceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "serviceId": "serviceId_value",
        "name": "name_value",
        "serviceName": "serviceName_value",
        "description": "description_value",
        "createTime": "createTime_value",
        "updateTime": "updateTime_value",
        "creator": "creator_value",
        "updater": "updater_value",
        "protocol": "protocol_value",
        "serviceType": 0,
        "upstreamType": 0,
        "upstreamTypeName": "upstreamTypeName_value",
        "loadBalanceType": 0,
        "loadBalanceTypeName": "loadBalanceTypeName_value",
        "routeList": {
            "routeId": "routeId_value",
            "routeName": "routeName_value",
            "routePath": []
        },
        "sourceType": 0,
        "serviceSourceType": 0,
        "serviceAddress": "serviceAddress_value",
        "port": 0,
        "serviceStruct": {},
        "isOpenHealthCheck": true,
        "healthCheckStruct": {
            "type": 0,
            "healthPath": "healthPath_value",
            "httpStatuses": "httpStatuses_value",
            "timeout": 0,
            "healthInterval": 0,
            "unHealthInterval": 0,
            "httpSuccesses": 0,
            "httpFailures": 0
        },
        "activeHealthCheckStruct": {
"enable":true,
```

智能体工厂 OpenTrek

```json
            enable: true,
            "protocol": "protocol_value",
            "timeout": 0,
            "interval": 0,
            "healthyThreshold": 0,
            "unhealthyThreshold": 0,
            "httpPath": "httpPath_value",
            "httpHost": "httpHost_value",
            "expectedStatuses": []
        },
        "activeHealthCheckStatusStruct": {
            "healthStatus": "healthStatus_value",
            "unhealthyEndpoints": []
        },
        "zones": [],
        "strategyConfigs": {
            "strategyConfigId": "strategyConfigId_value",
            "strategyConfigName": "strategyConfigName_value",
            "strategyName": "strategyName_value",
            "status": true,
            "scopes": [],
            "scope": {
                "routeInfos": {
                    "name": {},
                    "id": {}
                },
                "serviceInfos": {
                    "name": {},
                    "id": {}
                },
                "appInfos": {
                    "name": {},
                    "id": {}
                },
                "domainInfos": {
                    "name": {},
                    "id": {}
                },
                "mcpServerInfos": {
                    "name": {},
                    "id": {}
                },
                "scopes": []
            },
            "createTime": "createTime_value",
            "updateTime": "updateTime_value"
        },
        "proxyServerName": "proxyServerName_value"
    }
}
```

#### listServices

**API 接口概述**

**中文名称：**查询服务列表
智能体工厂 OpenTrek
**功能概述：**服务管理 - 查询服务列表。
**请求方式：** `POST`
**区分说明**：此接口同时用于查询 AI服务和普通服务，通过参数区分：
查询**AI****服务**：传 `sourceTypeList: ["ai"]` 或 `sourceTypeList: ["9"]` 查询**普通服务**：不传此参数或传其他类型值

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |  |  |
| current | integer | body | 是 | 1 | 当前页码。 |  |  |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |  |  |
| serviceName | string | body | 否 | qwen- service | 服务名称。 |  |  |
| serviceId | string | body | 否 | service- 001 | 服务ID。 |  |  |
| sourceName | string | body | 否 | qwen- provider | 来源名称。 |  |  |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |  |  |
| sourceTypeList | string[] | body | 否 | ["ai"] | 服务来源类型列表。AI服务传 ["ai"] 或 ["9"] ；普通服务可选值： nacos ( Nacos服务发现)、 kuberne tes (K8s集群)、 static (固定地址)、 dns (D NS域名)。 |  |  |
|  |  |  |  |  |  | kuberne |  |
| provider | string | body | 否 | qwen | provider参数。 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | qwen- |
|---|---|---|
|  | service |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

|  |  | qwen- |  |
|---|---|---|---|
|  | provider |  |  |

|  | tes |
|---|---|

智能体工厂 OpenTrek

| sourceTypeLab elValue | string | body | 否 | ai | sourceTypeLab elValue参数。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 |  | 类型 |  | 示例 | 说明 |
|---|---|---|---|---|---|
| requestId |  | string |  | uuid-xxx-xxx | 请求ID。 |
| code |  | integer |  | 200 | 响应码。 |
| msg |  | string |  | success | 响应消息。 |
| message |  | string |  | success | 响应消息。 |
| data |  | object |  | {} | 响应数据。 |
| data.size |  | integer |  | 10 | 每页大小。 |
| data.total |  | integer |  | 100 | 总数。 |
| data.current |  | integer |  | 1 | 当前页码。 |
| data.records |  | GatewayServiceListBy PageResponseRecord[] |  | [] | 记录列表。 |
|  |  |  | GatewayServiceListBy |  |  |
|  | a.records | PageResponseRecord[] |  |  |  |
| data.records.serviceId |  | string |  | service-001 | 服务ID。 |
| data.records.name |  | string |  | qwen-service | 名称。 |
| data.records.upstreamTy pe |  | integer |  | 1 | 上游类型。 |
| data.records.serviceType |  | integer |  | 1 | 服务类型。 |
| data.records.upstreamTy peName |  | string |  | AI服务 | upstreamTypeName字段。 |
| data.records.serviceProt ocol |  | string |  | HTTP | serviceProtocol字段。 |

智能体工厂 OpenTrek

| data.records.sourceId | string | source-001 | 来源ID。 |
|---|---|---|---|
| data.records.sourceNam e | string | qwen-provider | 来源名称。 |
| data.records.sourceType | integer | 9 | 来源类型。 |
| data.records.sourceType Name | string | AI服务 | sourceTypeName字段。 |
| data.records.createTime | string | 2024-01-01 12:00:00 | 创建时间。 |
| data.records.updateTime | string | 2024-01-01 12:00:00 | 更新时间。 |
| data.records.creator | string | admin | 创建者。 |
| data.records.updater | string | admin | 更新者。 |
| data.records.nodes | FixedNodesDTO$Node[] | [] | 节点列表。 |
| data.records.nodes.ip | string | 192.168.1.100 | IP地址。 |
| data.records.nodes.port | integer | 8080 | 端口。 |
| data.records.nodes.weig ht | integer | 1 | 权重。 |
| data.records.nodes.enabl e | boolean | true | 是否启用。 |
| data.records.nodes.vpcId | string | vpc-xxx-xxx | VPC ID。 |
| data.records.nodes.vpcM appingIp | string | 10.0.0.1 | vpcMappingIp字段。 |
| data.records.nodes.vpcM appingPort | integer | 8080 | vpcMappingPort字段。 |
| data.records.proxyServe rName | string | proxy-001 | 代理服务器名称。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 12:00:00 |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 12:00:00 |  |

|  |  | FixedNodesDTO$Node[] |
|---|---|---|
| a.records.nodes |  |  |

智能体工厂 OpenTrek

| data.records.serviceAddr ess | string | qwen- service.example.com | 服务地址。 |
|---|---|---|---|
| data.records.activeHealt hCheckStruct | object | {} | 主动健康检查配置。 |
| data.records.activeHealt hCheckStruct.enable | boolean | false | 是否启用。 |
| data.records.activeHealt hCheckStruct.protocol | string | HTTP | 协议类型。 |
| data.records.activeHealt hCheckStruct.timeout | integer | 5 | 超时时间（秒）。 |
| data.records.activeHealt hCheckStruct.interval | integer | 10 | 检查间隔（秒）。 |
| data.records.activeHealt hCheckStruct.healthyThr eshold | integer | 3 | 健康阈值。 |
| data.records.activeHealt hCheckStruct.unhealthyT hreshold | integer | 3 | 不健康阈值。 |
| data.records.activeHealt hCheckStruct.httpPath | string | /health | HTTP路径。 |
| data.records.activeHealt hCheckStruct.httpHost | string | localhost | HTTP Host头。 |
| data.records.activeHealt hCheckStruct.expectedSt atuses | string[] | ["200"] | 期望的状态码列表。 |
| data.records.activeHealt hCheckStatusStruct | object | {} | activeHealthCheckStatus Struct字段。 |
| data.records.activeHealt hCheckStatusStruct.healt hStatus | string | healthy | healthStatus字段。 |
| data.records.activeHealt hCheckStatusStruct.unhe althyEndpoints | string[] | [] | unhealthyEndpoints字段。 |
| data.records.aiServiceCo nfig | object | {} | aiServiceConfig字段。 |

|  |  | qwen- | 服务 |
|---|---|---|---|
|  | service.example.com |  |  |

智能体工厂 OpenTrek

| data.records.aiServiceCo nfig.provider | string | qwen | provider字段。 |
|---|---|---|---|
| data.records.aiServiceCo nfig.aiProtocol | string | openai | aiProtocol字段。 |
| data.records.aiServiceCo nfig.baseUrl | string | https://dashscope.al iyuncs.com | baseUrl字段。 |
| data.records.aiServiceCo nfig.apiKeyList | string[] | ["sk-xxx"] | apiKeyList字段。 |

|  | https://dashscope.al | baseUrl字 |
|---|---|---|
| iyuncs.com |  |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value",
  "serviceName": "serviceName_value",
  "serviceId": "serviceId_value",
  "sourceName": "sourceName_value",
  "isDisasterRecovery": true,
  "sourceTypeList": [
    "ai"
```

`],`

```json
  "provider": "provider_value",
  "sourceTypeLabelValue": "sourceTypeLabelValue_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "size": 0,
        "total": 0,
        "current": 0,
        "records": {
            "serviceId": "serviceId_value",
            "name": "name_value",
            "upstreamType": 0,
"serviceType":0
```

智能体工厂 OpenTrek

```json
            serviceType: 0,
            "upstreamTypeName": "upstreamTypeName_value",
            "serviceProtocol": "serviceProtocol_value",
            "sourceId": "sourceId_value",
            "sourceName": "sourceName_value",
            "sourceType": 0,
            "sourceTypeName": "sourceTypeName_value",
            "createTime": "createTime_value",
            "updateTime": "updateTime_value",
            "creator": "creator_value",
            "updater": "updater_value",
            "nodes": {
                "ip": "ip_value",
                "port": 0,
                "weight": 0,
                "enable": true,
                "vpcId": "vpcId_value",
                "vpcMappingIp": "vpcMappingIp_value",
                "vpcMappingPort": 0
            },
            "proxyServerName": "proxyServerName_value",
            "serviceAddress": "serviceAddress_value",
            "activeHealthCheckStruct": {
                "enable": true,
                "protocol": "protocol_value",
                "timeout": 0,
                "interval": 0,
                "healthyThreshold": 0,
                "unhealthyThreshold": 0,
                "httpPath": "httpPath_value",
                "httpHost": "httpHost_value",
                "expectedStatuses": []
            },
            "activeHealthCheckStatusStruct": {
                "healthStatus": "healthStatus_value",
                "unhealthyEndpoints": []
            },
            "aiServiceConfig": {
                "provider": "provider_value",
                "aiProtocol": "aiProtocol_value",
                "baseUrl": "baseUrl_value",
                "apiKeyList": []
            }
        }
    }
}
```

#### listServicesBySource

**API 接口概述**

**中文名称：**按来源查询服务
**功能概述：**服务管理 - 根据来源查询服务。
智能体工厂 OpenTrek
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| sourceId | string | body | 是 | source- 001 | 来源ID。 |
| sourceNamesp aceId | string | body | 否 | namespace- 001 | Nacos命名空间 ID。 |
| groupName | string | body | 否 | DEFAULT GROU _ P | 服务分组名称。 |
| sourceType | integer | body | 是 | 1 | 来源类型。可选值： 1 (Naco s服务发现)、 4 (K8s 集群)、 7 (固定地址)、 8 (DNS 域名)、 9 (AI 服务)。 |
| keyword | string | body | 否 | my- service | 服务名称关键字。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | source- |
|---|---|---|
|  | 001 |  |

|  |  | namespace- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | my- |
|---|---|---|
|  | service |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |

智能体工厂 OpenTrek

| data.importServiceList | string[] | ["service-001", "service-002"] | 已导入的服务列表。 |
|---|---|---|---|
| data.notImportServiceLis t | string[] | ["service-003"] | 未导入的服务列表。 |

|  | ["service-001", |  |
|---|---|---|
| "service-002"] |  |  |

**示例**

**请求示例**

```json
POST /microservice/listServicesBySource HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "sourceId": "sourceId_value",
  "sourceNamespaceId": "sourceNamespaceId_value",
  "groupName": "groupName_value",
  "sourceType": 0,
  "keyword": "keyword_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "importServiceList": [],
        "notImportServiceList": []
    }
}
```

#### modifyMicroservice

**API 接口概述**

**中文名称：**修改服务
**功能概述：**服务管理 - 修改服务。
**请求路径：** `/microservice/modifyService`
**请求方式：** `POST`
**区分说明**：此接口同时用于修改 AI服务和普通服务，通过参数区分（同 createMicroservice）。
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 |  | 位置 |  |  |  | 是否必选 |  |  |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| serviceId | string |  | body |  |  |  | 是 |  |  |  | service- 001 |  | 服务ID，修改时必填。 |  |
| gwInstanceId | string |  | body |  |  |  | 是 |  |  |  | higress- 001 |  | 网关实例ID。 |  |
| name | string |  | body |  |  |  | 是 |  |  |  | qwen- |  | 名称。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | qwen- |  |  |
|  |  |  |  |  |  |  |  |  |  |  | service- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | updated |  |  |  |
| serviceName | string |  | body |  |  |  | 否 |  |  |  | qwen- service |  | 服务名称。 |  |
| description | string |  | body |  |  |  | 否 |  |  |  | 更新后的通义千问AI服务 |  | 描述信息。 |  |
| upstreamType | integer |  | body |  |  |  | 否 |  |  |  | 1 |  | 上游类型。 |  |
| serviceSourceT ype | integer |  | body |  |  |  | 否 |  |  |  | 9 |  | 服务来源类型。AI服务传 9 ；普通服务可选值： 1 (Naco s服务发现)、 4 (K8s 集群)、 7 (固定地址)、 8 (DNS 域名)。 |  |
| serviceType | integer |  | body |  |  |  | 否 |  |  |  | 1 |  | 服务类型。 |  |
| loadBalanceTy pe | integer |  | body |  |  |  | 否 |  |  |  | 1 |  | 负载均衡算法类型。 |  |
| serviceStruct | object |  |  |  |  |  |  |  |  |  | {"provider": |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | {"provider": |  |  |
|  |  |  |  |  |  |  |  |  |  |  | "qwen","aiPro |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | tocol":"opena |  |  |  |
|  |  |  | body |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | body |  |  | 否 |  |  |  | i"} |  |  |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | qwen- |
|---|---|---|
|  | service |  |

|  |  | 更新后的通义 | 描述信 |
|---|---|---|---|
|  | 千问AI服务 |  |  |

智能体工厂 OpenTrek

| isOpenHealthC heck | boolean | body | 否 | false | 是否开启健康检查。 |
|---|---|---|---|---|---|
| healthCheckStr uct | object | body | 否 | {"type":1,"t imeout":5} | 健康检查配置。 |
| activeHealthCh eckStruct | object | body | 否 | {"enable":fa lse} | 主动健康检查配置。 |
| protocol | string | body | 是 | HTTP | 协议类型。 |
| proxyServerNa me | string | body | 否 | proxy-001 | 代理服务器名称。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

| {"type":1,"t | 健康检查配 |
|---|---|

|  |  | {"enable":fa | 主动 |
|---|---|---|---|
|  | lse} |  |  |

**healthCheckStruct 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | integer | body | 否 | 1 | 类型。 |
| healthPath | string | body | 否 | /health | 健康检查路径。 |
| httpStatuses | string | body | 否 | 200,301,302 | HTTP状态码。 |
| timeout | integer | body | 否 | 5 | 超时时间 （秒）。 |
| healthInterval | integer | body | 否 | 10 | 健康检查间隔。 |
| unHealthInterv al | integer | body | 否 | 30 | 不健康检查间隔。 |
| httpSuccesses | integer | body | 否 | 3 | HTTP成功次数阈值。 |
| httpFailures | integer | body | 否 | 3 | HTTP失败次数阈值。 |

|  |  | 200,301,302 |
|---|---|---|

**activeHealthCheckStruct 对象结构**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | false | 是否启用。 |
| protocol | string | body | 否 | HTTP | 协议类型。 |
| timeout | integer | body | 否 | 5 | 超时时间 （秒）。 |
| interval | integer | body | 否 | 10 | 检查间隔 （秒）。 |
| healthyThresho ld | integer | body | 否 | 3 | 健康阈值。 |
| unhealthyThres hold | integer | body | 否 | 3 | 不健康阈值。 |
| httpPath | string | body | 否 | /health | HTTP路径。 |
| httpHost | string | body | 否 | localhost | HTTP Host头。 |
| expectedStatus es | string[] | body | 否 | ["200"] | 期望的状态码列表。 |

**serviceStruct 对象结构**

**说明**：serviceStruct 根据 `serviceSourceType` 参数有不同的字段结构：

**当 serviceSourceType=9（AI服务）时：**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| provider | string | body | 是 | qwen | AI提供商类型。 可选值： selfbuil d (自建)、 qwen ( 通义千问)、 deepsee k 、 openai 、 azure 、 gemini 、 bedrock 、 c laude 、 moo nshot (月之暗面)、 baichua n (百川)、 yi (零一万物)、 zhipuai (智谱)、 hunyuan (混元)、 stepfun (阶跃)、 spark ( 讯飞星火)、 doubao (豆包)、 minimax 、 vertex ( Vertex AI)。 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | azure |  |  |  |
|  |  |  |  |  |  |  | 、 、 |  |  |
|  |  |  |  |  |  |  |  | c |  |
|  |  |  |  |  |  |  | moo |  |  |
| aiProtocol | string | body | 是 | openai | AI协议类型。可选值： openai ( OpenAI/V1标准协议)、 origina l (原始协议)。 |  |  |  |  |

|  | d |
|---|---|

|  |  |  |  | k |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | bedrock |  |  |
|  |  |  |  | laude |  |  |
|  |  |  |  | nshot |  |  |

|  | n |
|---|---|

|  | l |
|---|---|

智能体工厂 OpenTrek

| baseUrl | string | body |  |  | 否 |  |  | https://api. |  |  |  | AI服务基础URL 地址。部分提供商有默认值，如 qwen 默认为 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | https://api. |  |  |  | https:/ | /dash |  |
|  |  |  |  |  |  |  |  | ope |  | nai.com |  | scope.aliyunc |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | s.com/compati |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | ble- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | mode/v1 |  |  |  |
| apiKeyList | string[] | body |  |  | 否 |  |  | ['sk- xxx'] |  |  |  | API Key列表。支持配置多个 API Key 实现负载均衡和容灾。自建 LLM时可省略。 |  |  |  |

**当 serviceSourceType 为其他值（普通服务）时：**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|
| nodes | object[] | body | 否 |  | [{"ip":"192. |  | 服务节点列表。 当 |  |
|  |  |  |  |  |  | [{"ip":"192. | serviceSourceT ype=7( |  |
|  |  |  |  |  | 168.1.1","por |  | ype=7( |  |
|  |  |  |  |  |  |  | 固址)或 |  |
|  |  |  |  |  | t":8080}] |  |  |  |
| sourceGroup | string | body | 否 |  | DEFAULT GROU _ P |  | Nacos分组名。 当 serviceSourceT ype=1(NACOS) 时使用，默认值为 DEFAULT GROU _ P 。 |  |
| sourceNamesp aceId | string | body | 否 |  | namespace- 001 |  | Nacos命名空间 ID。当 serviceSourceT ype=1(NACOS) 时使用。 |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | namespace- |  |
|---|---|---|---|
|  | 001 |  |  |

**nodes 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ip | string | body | 是 | 192.168.1.1 | 节点IP地址。 |
| port | integer | body | 是 | 8080 | 节点端口。 |

|  |  | 192.168.1.1 |
|---|---|---|

智能体工厂 OpenTrek

| weight | integer | body | 否 | 1 | 节点权重，用于负载均衡。默认值为 1。 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | true | 节点是否启用。 默认值为 true。 |
| vpcId | string | body | 否 | vpc-xxx- xxx | VPC ID（跨VPC 场景）。 |
| vpcMappingIp | string | body | 否 | 10.0.0.1 | VPC映射IP。 |
| vpcMappingPor t | integer | body | 否 | 8080 | VPC映射端口。 |

|  |  | vpc-xxx- |
|---|---|---|
|  | xxx |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | service-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /microservice/modifyService HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "serviceId": "serviceId_value",
  "gwInstanceId": "gwInstanceId_value",
  "name": "name_value",
  "serviceName": "serviceName_value",
  "description": "description_value",
  "upstreamType": 0,
  "serviceSourceType": 9,
  "serviceType": 0,
  "loadBalanceType": 0,
  "serviceStruct": {
    "provider": "qwen",
    "aiProtocol": "openai",
    "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "apiKeyList": [
      "sk-xxxxx"
```

]

```json
  },
  "isOpenHealthCheck": true,
  "healthCheckStruct": {
    "type": 0,
    "healthPath": "healthPath_value",
    "httpStatuses": "httpStatuses_value",
    "timeout": 0,
    "healthInterval": 0,
    "unHealthInterval": 0,
    "httpSuccesses": 0,
    "httpFailures": 0
  },
  "activeHealthCheckStruct": {
    "enable": true,
    "protocol": "protocol_value",
    "timeout": 0,
    "interval": 0,
    "healthyThreshold": 0,
    "unhealthyThreshold": 0,
    "httpPath": "httpPath_value",
    "httpHost": "httpHost_value",
    "expectedStatuses": []
  },
  "protocol": "protocol_value",
  "proxyServerName": "proxyServerName_value",
  "isDisasterRecovery": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### modifyNode

**API 接口概述**

**中文名称：**修改服务节点
**功能概述：**服务管理 - 修改节点。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body |  |  |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| serviceId | string | body |  |  |  | 是 |  | service- 001 |  | 服务ID。 |  |
| serviceSourceT ype | integer | body |  |  |  | 否 |  | 9 |  | 服务来源类型。 可选值： 1 (Naco s服务发现)、 4 (K8s 集群)、 7 (固定地址)、 8 (DNS 域名)、 9 (AI 服务)。 |  |
| serviceStruct | object |  |  |  |  |  |  | {"nodes": |  |  |  |
|  |  |  |  |  |  |  |  |  | {"nodes": |  |  |
|  |  |  |  |  |  |  |  | [{"ip": |  |  |  |
|  |  |  |  |  |  |  |  | "192.168.1.1" |  |  |  |
|  |  |  |  |  |  |  |  | , "port": |  |  |  |
|  |  | body |  |  |  |  |  |  |  |  |  |
|  |  |  | body |  |  | 否 |  | 8080}]} |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | service-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "serviceId": "service-001",
  "serviceSourceType": 7,
  "serviceStruct": {
    "nodes": [
      {"ip": "192.168.1.1", "port": 8080, "weight": 1, "enable": true}
```

]

```
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "service-001"
}
```

### AI网关实例管理

智能体工厂 OpenTrek

#### addInstance

**API 接口概述**

**中文名称：**创建实例
**功能概述：**创建网关实例。

```
请求路径： /gatewayInstance/createInstance
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| gwInstanceName | string | 是 | my-gateway |  | 网关实例名称，长度限制2-128字符。 |  |  |
| clusterCode | string | 是 | cluster-001 |  | 集群编码。 |  |  |
| namespace | string | 是 | default |  | K8s命名空间。 |  |  |
| deployConfigConte nt | string | 否 | {} |  | 部署配置内容（JSON 格式）。 |  |  |
| accessModeConfig Content | string | 否 | {} |  | 访问模式配置内容 （JSON格式）。 |  |  |
| vpcId | string | 否 | vpc-xxx |  | VPC ID。 |  |  |
| vswId | string | 否 | vsw-xxx |  | vSwitch ID。 |  |  |
| ingressName | string | 否 | my-ingress |  | Ingress名称。 |  |  |
| brokerEngineType | string | 否 | HIGRESS |  | 引擎类型。可选值： HIGRESS (AI 网关)、 SCG (API 网关)、 SHARED SCG _ (共享型API网关)、 CLOUD NATIV _ E GATEWAY (云原生 _ 网关)。 |  |  |
|  |  |  |  |  |  | CLOUD NATIV _ |  |
|  |  |  |  |  | E GATEWAY _ |  |  |

智能体工厂 OpenTrek

| deployMode | string | 否 | k8s | 部署模式。可选值： edas (EDAS K8s部署，SCG引擎)、 custom (自定义部署，SCG引擎)、 adp (ADP部署，SCG引擎)、 apig k8s ( _ APIG K8s部署，SCG 引擎)、 onpaas (共享PaaS部署，SHARED SCG _ 引擎)、 k8s (K8s 部署，Higress引擎)、 acs k8s (A _ CS K8s部署，Higress引擎)。 |  |  |
|---|---|---|---|---|---|---|
| instanceClass | string | 否 | standard | 实例规格类型（支持 K8s部署模式）。 |  |  |
| instanceNumber | string | 否 | 2 | 实例数量。 |  |  |
| o11y | object | 否 | {} | 可观测配置对象，详见下方二级参数表。 |  |  |
| imagePullSecretNa me | string | 否 | my-secret | 镜像拉取Secret名称，用于拉取私有镜像。 |  |  |
| gatewayServiceTyp e | string | 否 | LoadBalancer | 网关Service类型。可选值： ClusterIP ( 集群内部访问)、 NodePort ( 通过节点端口暴露)、 LoadBalance r (通过负载均衡器暴露)。 |  |  |
|  |  |  |  |  | LoadBalance |  |
| gatewayNodePort | integer | 否 | 30080 | NodePort端口，当 gatewayServiceTy pe为NodePort时使用，端口范围30000- 32767。 |  |  |
| replicas | integer | 否 | 2 | 实例副本数（发现/导入实例时填充）。 |  |  |
| higressVersion | string | 否 | 1.4.0 | Higress版本（发现/ 导入实例时填充）。 |  |  |

|  | r |
|---|---|

智能体工厂 OpenTrek

| deploymentUid | string | 否 | uid-xxx | Deployment UID（发现/导入实例时填充）。 |
|---|---|---|---|---|

**o11y 二级参数表：**

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| slsEnabled | boolean | 否 | true | 是否启用阿里云SLS 日志配置。 |
| prometheusEnable d | boolean | 否 | true | 是否启用阿里云 Prometheus监控配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | xxx-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | gw-instance-001 | 创建成功后返回的网关实例 ID。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /gatewayInstance/createInstance HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceName": "my-higress-gateway",
  "clusterCode": "k8s-cluster-001",
  "namespace": "apigateway-system",
  "brokerEngineType": "HIGRESS",
  "deployMode": "k8s",
  "instanceClass": "standard",
  "instanceNumber": "2",
  "gatewayServiceType": "LoadBalancer",
  "o11y": {
    "slsEnabled": true,
    "prometheusEnabled": true
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "msg": "success",
  "message": "success",
  "requestId": "req-xxx-xxx-xxx",
  "data": "gw-instance-001"
}
```

#### ascmCreateInstance

**API 接口概述**

**中文名称：** ASCM创建实例
**功能概述：** ASCM创建实例。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceNa me | string | body | 是 | higress- 001 | 网关实例名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| clusterCode | string | body | 否 | k8s- cluster-001 | Kubernetes集群编码。 |
|---|---|---|---|---|---|
| instanceNumbe r | string | body | 是 | 2 | 实例数量。 |
| instanceClass | string | body | 否 | 2c4g | 实例规格类型。 |
| vpcId | string | body | 否 | vpc-xxx- xxx | VPC ID。 |
| backupZoneId | string | body | 否 | cn- hangzhou-b | backupZoneId 参数。 |
| backupVSwitch Id | string | body | 否 | vsw-xxx- xxx | backupVSwitch Id参数。 |
| thirdZoneId | string | body | 否 | cn- hangzhou-c | thirdZoneId参数。 |
| thirdVSwitchId | string | body | 否 | vsw-xxx- xxx | thirdVSwitchId 参数。 |
| zoneType | string | body | 否 | multizone | zoneType参数。 |
| uid | string | body | 否 | user-001 | uid参数。 |

|  |  | k8s- | Ku |
|---|---|---|---|
|  | cluster-001 |  |  |

|  |  | vpc-xxx- |
|---|---|---|
|  | xxx |  |

|  |  | cn- |  |
|---|---|---|---|
|  | hangzhou-b |  |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

|  |  | cn- |  |
|---|---|---|---|
|  | hangzhou-c |  |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

智能体工厂 OpenTrek

| deployMode | string | body | 否 | k8s | 部署模式。可选值： edas (E DAS K8s部署，SCG引擎)、 custom (自定义部署，SCG引擎)、 adp (A DP部署，SCG引擎)、 apig k8 _ s (APIG K8s部署，SCG引擎)、 onpaas (共享PaaS部署，SHARED S _ CG引擎)、 k8s (K8 s部署，Higress 引擎)、 acs k8s _ (ACS K8s部署，Higress引擎)。 |
|---|---|---|---|---|---|
| edasAppInfos | EdasAppInfo[ ] | body | 否 | [{"appId": "app-001"}] | edasAppInfos参数。 |
| deployConfigCo ntent | string | body | 否 | yaml配置内容 | 部署配置内容。 |
| accessModeCo nfigContent | string | body | 否 | yaml配置内容 | 访问模式配置内容。 |
| namespace | string | body | 否 | apigateway- system | Kubernetes命名空间。 |

|  | s |
|---|---|

|  |  | EdasAppInfo[ |  |
|---|---|---|---|
| sAppInfos | ] |  |  |

|  |  | [{"appId": | edasAppIn |
|---|---|---|---|
|  | "app-001"}] |  |  |

|  |  | yaml配置内 |
|---|---|---|
|  | 容 |  |

|  |  | yaml配置内 |
|---|---|---|
|  | 容 |  |

|  |  | apigateway- | Kube |
|---|---|---|---|
|  | system |  |  |

智能体工厂 OpenTrek

| brokerEngineTy pe | string | body | 否 |  | HIGRESS |  | 引擎类型。可选值： HIGRESS （AI网关）、 SCG （ API网关）、 SHARED SCG （共享型 _ API网关）、 CLOUD _ |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | CLOUD _ |  |
|  |  |  |  |  |  |  | NATIVE GATEWA _ |  |  |
|  |  |  |  |  |  |  | Y |  |  |
| ingressClassNa me | string | body | 否 |  | higress |  | ingressClassNa me参数。 |  |  |
| o11y | object | body | 否 |  | {"slsEnabled ": true} |  | o11y参数。 |  |  |
| imagePullSecre tName | string | body | 否 |  | registry- secret |  | 镜像拉取Secret 名称。 |  |  |
| gatewayServic eType | string | body | 否 |  | LoadBalancer |  | 网关服务类型。 可选值： ClusterI P （集群内部服务）、 NodePo rt （NodePort 暴露）、 LoadBa lancer （负载均衡器暴露）。 |  |  |
| gatewayNodeP ort | integer | body | 否 |  | 30080 |  | 网关NodePort端口。 |  |  |
| replicas | integer | body | 否 |  | 2 |  | 副本数。 |  |  |
| higressVersion | string | body | 否 |  | 1.4.0 |  | Higress版本。 |  |  |
| deploymentUid | string | body | 否 |  | deploy-uid- 001 |  | Deployment UID。 |  |  |
| enableIpv6 | boolean | body | 否 |  | false |  | enableIpv6参数。 |  |  |

| SHARED |  |
|---|---|

| {"slsEnabled | o11y参数 |
|---|---|

| registry- | 镜 |
|---|---|

| ClusterI |  |
|---|---|

|  | P |
|---|---|

| NodePo |  |
|---|---|

|  |  |  |  | rt |
|---|---|---|---|---|
|  |  | LoadBalancer | ancer |  |

|  |  | LoadBa |  |
|---|---|---|---|
|  | lancer |  |  |

|  |  | deploy-uid- | D |
|---|---|---|---|
|  | 001 |  |  |

智能体工厂 OpenTrek

| Department | string | body | 否 | IT部门 | Department参数。 |
|---|---|---|---|---|---|
| ResourceGroup | string | body | 否 | rg-001 | ResourceGroup 参数。 |
| RegionId | string | body | 是 | cn- hangzhou | RegionId参数。 |
| ZoneId | string | body | 否 | cn- hangzhou-a | ZoneId参数。 |
| vSwitchId | string | body | 否 | vsw-xxx- xxx | vSwitchId参数。 |

|  |  | cn- |
|---|---|---|
|  | hangzhou |  |

|  |  | cn- |  |
|---|---|---|---|
|  | hangzhou-a |  |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

**edasAppInfos 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | string | body | 否 | app-001 | 应用ID。 |
| edasNamespac eId | string | body | 否 | edas-ns- 001 | edasNamespac eId参数。 |
| k8sClusterId | string | body | 否 | k8s- cluster-001 | Kubernetes集群 ID。 |
| k8sNamespace | string | body | 否 | default | k8sNamespace 参数。 |

|  |  | edas-ns- |
|---|---|---|
|  | 001 |  |

|  |  | k8s- | Ku |
|---|---|---|---|
|  | cluster-001 |  |  |

**o11y 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| slsEnabled | boolean | body | 否 | true | 是否启用SLS日志。 |
| prometheusEn abled | boolean | body | 否 | true | 是否启用 Prometheus监控。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | higress-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /gatewayInstance/ascmCreateInstance HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceName": "gwInstanceName_value",
  "clusterCode": "clusterCode_value",
  "instanceNumber": "instanceNumber_value",
  "instanceClass": "instanceClass_value",
  "vpcId": "vpcId_value",
  "backupZoneId": "backupZoneId_value",
  "backupVSwitchId": "backupVSwitchId_value",
  "thirdZoneId": "thirdZoneId_value",
  "thirdVSwitchId": "thirdVSwitchId_value",
  "zoneType": "zoneType_value",
  "uid": "uid_value",
  "deployMode": "k8s",
  "edasAppInfos": [
    {
      "appId": "appId_value",
      "edasNamespaceId": "edasNamespaceId_value",
      "k8sClusterId": "k8sClusterId_value",
      "k8sNamespace": "k8sNamespace_value"
    }
```

`],`

```json
  "deployConfigContent": "deployConfigContent_value",
  "accessModeConfigContent": "accessModeConfigContent_value",
  "namespace": "namespace_value",
  "brokerEngineType": "brokerEngineType_value",
  "ingressClassName": "ingressClassName_value",
  "o11y": {
    "slsEnabled": true,
    "prometheusEnabled": true
  },
  "imagePullSecretName": "imagePullSecretName_value",
  "gatewayServiceType": "gatewayServiceType_value",
  "gatewayNodePort": 0,
  "replicas": 0,
  "higressVersion": "higressVersion_value",
  "deploymentUid": "deploymentUid_value",
  "enableIpv6": true,
  "Department": "Department_value",
  "ResourceGroup": "ResourceGroup_value",
  "RegionId": "RegionId_value",
  "ZoneId": "ZoneId_value",
  "vSwitchId": "vSwitchId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### createDeployConfig

**API 接口概述**

**中文名称：**创建部署配置
**功能概述：**创建部署配置。

```
请求路径： /gatewayInstance/createInstanceDeployConfig
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuRequest | string | body | 否 | 500m | cpuRequest参数。 |
| cpuLimit | string | body | 否 | 1000m | cpuLimit参数。 |
| memoryReques t | string | body | 否 | 512Mi | memoryReque st参数。 |
| memoryLimit | string | body | 否 | 1024Mi | memoryLimit参数。 |
| replicas | integer | body | 否 | 2 | 副本数。 |
| jvmArgs | string | body | 否 | -Xmx512m - Xms256m | jvmArgs参数。 |
| gwInstanceNa me | string | body | 是 | higress- 001 | 网关实例名称。 |
| accessModeTy pe | string | body | 是 | LoadBalancer | accessModeTy pe参数。 |

|  |  | -Xmx512m - | jvmA |
|---|---|---|---|
|  | Xms256m |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | LoadBalancer |
|---|---|---|

智能体工厂 OpenTrek

|  |  |  | CreateInstan |  |  |  |  |  |  |  |  |  | [{"port":80, |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | CreateInstan |  |  |  |  |  |  |  |  | [{"por |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"por | t":80, |  |  |
|  |  |  | ceDeployConfi |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "targetPort": |  |  |  |  |
|  | ports |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ports参数。 |  |
|  |  |  | gRequest$Acce |  |  |  | body |  |  | 否 |  |  |  |  |  | ports参 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "80","name":" |  |  |  |  |
|  |  |  | ssModePor |  | tInf |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | http"}] |  |  |  |  |
|  |  |  | o[] |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | namespace |  | string |  |  | body |  |  |  | 否 |  |  | apigateway- system |  |  | Kubernetes命名空间。 |  |
|  | externalTraffic Policy |  | string |  |  | body |  |  |  | 否 |  |  | Local |  |  | externalTraffic Policy参数。 |  |
|  | ipType |  | string |  |  | body |  |  |  | 是 |  |  | intranet |  |  | ipType参数。 |  |
|  | vpcId |  | string |  |  | body |  |  |  | 否 |  |  | vpc-xxx- xxx |  |  | VPC ID。 |  |
|  | vswId |  | string |  |  | body |  |  |  | 否 |  |  | vsw-xxx- xxx |  |  | 交换机ID。 |  |
|  | uid |  | string |  |  | body |  |  |  | 否 |  |  | user-001 |  |  | uid参数。 |  |

| apigateway- | Kube |
|---|---|

|  |  | vpc-xxx- |
|---|---|---|
|  | xxx |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

**ports 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| port | integer | body | 是 | 80 | 端口。 |
| targetPort | string | body | 是 | 8080 | targetPort参数。 |
| nodePort | integer | body | 否 | 30080 | nodePort参数。 |
| name | string | body | 是 | http-port | 名称。 |
| protocol | string | body | 否 | TCP | 协议类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.deployConfigYamlSt r | string | yaml配置内容 | deployConfigYamlStr字段。 |
| data.accessModeConfigY amlStr | string | yaml配置内容 | accessModeConfigYamlS tr字段。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/createInstanceDeployConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "cpuRequest": "cpuRequest_value",
  "cpuLimit": "cpuLimit_value",
  "memoryRequest": "memoryRequest_value",
  "memoryLimit": "memoryLimit_value",
  "replicas": 0,
  "jvmArgs": "jvmArgs_value",
  "gwInstanceName": "gwInstanceName_value",
  "accessModeType": "accessModeType_value",
  "ports": [
    {
      "port": 0,
      "targetPort": "targetPort_value",
      "nodePort": 0,
      "name": "name_value",
      "protocol": "protocol_value"
    }
```

`],`

```json
  "namespace": "namespace_value",
  "externalTrafficPolicy": "externalTrafficPolicy_value",
  "ipType": "ipType_value",
  "vpcId": "vpcId_value",
  "vswId": "vswId_value",
  "uid": "uid_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "deployConfigYamlStr": "deployConfigYamlStr_value",
        "accessModeConfigYamlStr": "accessModeConfigYamlStr_value"
    }
}
```

#### getCapacity

**API 接口概述**

**中文名称：**查询资源容量
**功能概述：**查询资源容量。
**请求路径：** `/gatewayInstance/getResource`
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.replicas | integer | 2 | 副本数。 |

智能体工厂 OpenTrek

| data.cpuRequest | object | {} | cpuRequest 字段。 |
|---|---|---|---|
| data.cpuRequest.amount | string | 500m | amount 字段。 |
| data.cpuRequest.unit | string | m | unit 字段。 |
| data.memoryRequest | object | {} | memoryRequest 字段。 |
| data.memoryRequest.am ount | string | 512Mi | amount 字段。 |
| data.memoryRequest.uni t | string | Mi | unit 字段。 |
| data.cpuLimit | object | {} | cpuLimit 字段。 |
| data.cpuLimit.amount | string | 1000m | amount 字段。 |
| data.cpuLimit.unit | string | m | unit 字段。 |
| data.memoryLimit | object | {} | memoryLimit 字段。 |
| data.memoryLimit.amou nt | string | 1Gi | amount 字段。 |
| data.memoryLimit.unit | string | Gi | unit 字段。 |
| data.jvmArgs | string | -Xms256m -Xmx512m | jvmArgs 字段。 |
| data.instanceName | string | higress-001 | instanceName 字段。 |
| data.engineSpecification | string | standard | engineSpecification 字段。 |
| data.vpcId | string | vpc-001 | VPC ID。 |
| data.regionId | string | cn-hangzhou | regionId 字段。 |
| data.zoneId | string | cn-hangzhou-a | zoneId 字段。 |

智能体工厂 OpenTrek

| data.backupZoneId | string | cn-hangzhou-b | backupZoneId 字段。 |
|---|---|---|---|
| data.backupVSwitchId | string | vsw-002 | backupVSwitchId 字段。 |
| data.thirdZoneId | string | cn-hangzhou-c | thirdZoneId 字段。 |
| data.thirdVSwitchId | string | vsw-003 | thirdVSwitchId 字段。 |
| data.zoneType | string | MultiZone | zoneType 字段。 |
| data.vSwitchId | string | vsw-001 | vSwitchId 字段。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/getResource HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "replicas": 0,
        "cpuRequest": {
            "amount": "amount_value",
            "unit": "unit_value"
        },
        "memoryRequest": {
            "amount": "amount_value",
            "unit": "unit_value"
        },
        "cpuLimit": {
            "amount": "amount_value",
            "unit": "unit_value"
        },
        "memoryLimit": {
            "amount": "amount_value",
            "unit": "unit_value"
        },
        "jvmArgs": "jvmArgs_value",
        "instanceName": "instanceName_value",
        "engineSpecification": "engineSpecification_value",
        "vpcId": "vpcId_value",
        "regionId": "regionId_value",
        "zoneId": "zoneId_value",
        "backupZoneId": "backupZoneId_value",
        "backupVSwitchId": "backupVSwitchId_value",
        "thirdZoneId": "thirdZoneId_value",
        "thirdVSwitchId": "thirdVSwitchId_value",
        "zoneType": "zoneType_value",
        "vSwitchId": "vSwitchId_value"
    }
}
```

#### getCustomDeployConfig

**API 接口概述**

**中文名称：**查询自定义部署配置
**功能概述：**查询自定义部署配置。

```
请求路径： /gatewayInstance/getCustomDeployConfig
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
|---|---|---|---|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|
| requestId | string |  | uuid-xxx-xxx |  | 请求 ID。 |
| code | integer |  | 200 |  | 响应码。 |
| msg | string |  | success |  | 响应消息。 |
| message | string |  | success |  | 响应消息。 |
| data | object |  | {} |  | 响应数据。 |
| data.deploymentYamlStr | string |  | apiVersion: apps/v1... |  | deploymentYamlStr 字段。 |
| data.serviceYamlStr | string |  | apiVersion: v1... |  | serviceYamlStr 字段。 |
| data.jarStr | string |  | /app/gateway- admin.jar |  | jarStr 字段。 |
| data.wgetStr | string |  | wget |  | wgetStr 字段。 |
|  |  |  |  | wget |  |
|  |  |  | http://xxx/gateway- |  |  |
|  |  |  |  |  | wgetS |
|  |  |  | admin.jar |  |  |

|  |  | apiVersion: | d |
|---|---|---|---|
|  | apps/v1... |  |  |

|  |  | /app/gateway- | j |
|---|---|---|---|
|  | admin.jar |  |  |

**示例**

**请求示例**

```json
POST /gatewayInstance/getCustomDeployConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "deploymentYamlStr": "deploymentYamlStr_value",
        "serviceYamlStr": "serviceYamlStr_value",
        "jarStr": "jarStr_value",
        "wgetStr": "wgetStr_value"
    }
}
```

#### getDeployConfig

**API 接口概述**

**中文名称：**查询部署配置
**功能概述：**查询部署配置。

```
请求路径： /gatewayInstance/getInstanceDeployDeployConfig
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | {} | 响应数据。 |

**示例**

智能体工厂 OpenTrek

**请求示例**

```json
POST /gatewayInstance/getInstanceDeployDeployConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getInstanceImageUrl

**API 接口概述**

**中文名称：**查询实例镜像地址
**功能概述：**查询实例镜像地址。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

| msg | string | success | 响应消息。 |
|---|---|---|---|
| message | string | success | 响应消息。 |
| data | string | registry.example.com /higress:v1.0 | 响应数据。 |

|  | registry.example.com | 响应数据。 |
|---|---|---|
| /higress:v1.0 |  |  |

**示例**

**请求示例**

```json
POST /gatewayInstance/getInstanceImageUrl HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getInstanceInfo

**API 接口概述**

**中文名称：**查询实例详情
**功能概述：**查询指定网关实例的详细信息。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | 是 | gw-instance- 001 | 网关实例 ID。 |
|---|---|---|---|---|

|  |  | gw-instance- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | xxx-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据，实例详情对象。 |
| data.status | integer | 1 | 实例状态。 |
| data.gwInstanceId | string | gw-instance-001 | 网关实例 ID。 |
| data.name | string | my-gateway | 网关实例名称。 |
| data.instanceName | string | my-gateway | 实例名称。 |
| data.deployClusterName space | string | apigateway-system | 部署集群命名空间。 |
| data.deployClusterCode | string | cluster-001 | 部署集群编码。 |
| data.deployClusterName | string | 生产集群 | 部署集群名称。 |
| data.k8sServiceName | string | higress-gateway | K8s Service 名称。 |
| data.createTime | string | 2024-01- 01T00:00:00 | 创建时间。 |
| data.modifyTime | string | 2024-01- 01T00:00:00 | 修改时间。 |

智能体工厂 OpenTrek

| data.vpcId | string | vpc-xxx | VPC ID。 |
|---|---|---|---|
| data.vSwitchId | string | vsw-xxx | vSwitch ID。 |
| data.regionId | string | cn-hangzhou | 区域 ID。 |
| data.zoneId | string | cn-hangzhou-a | 可用区 ID。 |
| data.deployMode | string | k8s | 部署模式。可选值： edas (EDAS K8s 部署，SCG 引擎)、 custom (自定义部署，SCG 引擎)、 adp (ADP 部署，SCG 引擎)、 apig k8s (APIG _ K8s 部署，SCG 引擎)、 onpaas (共享 PaaS 部署，SHARED SCG _ 引擎)、 k8s (K8s 部署，Higress 引擎)、 acs k8s (ACS _ K8s 部署，Higress 引擎)。 |
| data.edasAppId | string | app-xxx | EDAS 应用 ID。 |
| data.edasNamespaceId | string | ns-xxx | EDAS 命名空间 ID。 |
| data.k8sClusterId | string | k8s-xxx | K8s 集群 ID。 |
| data.k8sNamespace | string | default | K8s 命名空间。 |
| data.instanceClass | string | standard | 实例规格类型。 |
| data.department | string | 研发部 | 所属部门。 |
| data.resourceGroup | string | group-001 | 资源组。 |
| data.ingressClassName | string | higress | IngressClass 名称。 |

智能体工厂 OpenTrek

| data.brokerEngineType | string | HIGRESS |  | 引擎类型。可选值： HIGRESS (AI网关)、 SCG (API 网关)、 SHARED SCG (共享 _ 型 API 网关)、 CLOUD NATIVE GAT _ _ EWAY (云原生网关)。 |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  |  | CLOUD NATIVE GAT _ _ |  |
|  |  |  |  | EWAY |  |  |
| data.brokerEngineVersio n | string | 1.4.0 |  | 当前引擎版本。 |  |  |
| data.brokerLatestEngine Version | string | 1.5.0 |  | 最新引擎版本（用于升级提示）。 |  |  |
| data.deployClusterAttrib ute | string | hub |  | 部署集群属性。 |  |  |
| data.nodeNumber | integer | 2 |  | 节点数量。 |  |  |
| data.sharedInstance | boolean | false |  | 是否为共享实例。 |  |  |
| data.sharedInstanceSour ce | string | external-sharing |  | 共享实例来源。 |  |  |
| data.higressDeployment Uid | string | uid-xxx |  | Higress Deployment 的 K8s UID。 |  |  |
| data.o11y | object | {} |  | 可观测配置对象。 |  |  |
| data.o11y.slsEnabled | boolean | true |  | 是否启用 SLS 日志。 |  |  |
| data.o11y.prometheusEn abled | boolean | true |  | 是否启用 Prometheus 监控。 |  |  |
| data.accessMode | array | [] |  | 访问模式列表，详见下方二级参数表。 |  |  |
| data.edasAppInfos | array | [] |  | EDAS 应用信息列表，详见下方二级参数表。 |  |  |

**accessMode 二级参数表：**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| accessMode[].ips | string[] | ["192.168.1.1"] | IP 地址列表。 |

智能体工厂 OpenTrek

| accessMode[].ports | string[] | ["80", "443"] | 端口列表。 |
|---|---|---|---|
| accessMode[].accessMod eType | string | LoadBalancer | 访问模式类型。 |
| accessMode[].loadBalanc erNetworkType | string | internet | 负载均衡器网络类型。 |
| accessMode[].loadBalanc erAddressType | string | external | 负载均衡器地址类型。 |
| accessMode[].serviceNa me | string | higress-gateway | K8s Service 名称。 |
| accessMode[].externalIp s | string[] | [] | 外部 IP 列表。 |
| accessMode[].clusterIp | string[] | ["10.0.0.1"] | 集群 IP 列表。 |
| accessMode[].edasAppId | string | app-xxx | EDAS 应用 ID。 |
| accessMode[].ipVersion | string | IPv4 | IP 版本。 |

**edasAppInfos 二级参数表：**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| edasAppInfos[].appId | string | app-xxx | EDAS 应用 ID。 |
| edasAppInfos[].edasNam espaceId | string | ns-xxx | EDAS 命名空间 ID。 |
| edasAppInfos[].k8sCluste rId | string | k8s-xxx | K8s 集群 ID。 |
| edasAppInfos[].k8sName space | string | default | K8s 命名空间。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gw-instance-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "msg": "success",
  "message": "success",
  "requestId": "req-xxx-xxx-xxx",
  "data": {
    "status": 1,
    "gwInstanceId": "gw-instance-001",
    "name": "my-higress-gateway",
    "instanceName": "my-higress-gateway",
    "deployClusterNamespace": "apigateway-system",
    "deployClusterCode": "cluster-001",
    "deployClusterName": "生产集群",
    "k8sServiceName": "higress-gateway",
    "createTime": "2024-01-01T10:00:00",
    "modifyTime": "2024-01-01T10:00:00",
    "vpcId": "vpc-xxx",
    "vSwitchId": "vsw-xxx",
    "regionId": "cn-hangzhou",
    "zoneId": "cn-hangzhou-a",
    "deployMode": "k8s",
    "brokerEngineType": "HIGRESS",
    "brokerEngineVersion": "1.4.0",
    "brokerLatestEngineVersion": "1.5.0",
    "nodeNumber": 2,
    "sharedInstance": false,
    "o11y": {
      "slsEnabled": true,
      "prometheusEnabled": true
    },
    "accessMode": [
      {
        "ips": ["192.168.1.1"],
        "ports": ["80", "443"],
        "accessModeType": "LoadBalancer",
        "serviceName": "higress-gateway"
      }
```

]

```
  }
}
```

#### getK8sMsg

智能体工厂 OpenTrek

**API 接口概述**

**中文名称：**查询实例部署信息
**功能概述：**查询实例部署信息。

```
请求路径： /gatewayInstance/getInstanceDeployMsg
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.deploymentName | string | higress-001- deployment | deploymentName 字段。 |
| data.resConfig | object | {} | resConfig 字段。 |
| data.resConfig.cpuReque st | string | 500m | cpuRequest 字段。 |
| data.resConfig.memoryR equest | string | 512Mi | memoryRequest 字段。 |
| data.resConfig.cpuLimit | string | 1000m | cpuLimit 字段。 |
| data.resConfig.memoryLi mit | string | 1Gi | memoryLimit 字段。 |

|  |  | higress-001- | d |
|---|---|---|---|
|  | deployment |  |  |

智能体工厂 OpenTrek

| data.resConfig.replicas |  | integer |  | 2 |  |  | 副本数。 |
|---|---|---|---|---|---|---|---|
| data.resConfig.jvmArgs |  | string |  | -Xms256m -Xmx512m |  |  | jvmArgs 字段。 |
| data.clusterConfig |  | object |  | {} |  |  | clusterConfig 字段。 |
| data.clusterConfig.cluste rName |  | string |  | my-k8s-cluster |  |  | clusterName 字段。 |
| data.clusterConfig.name space |  | string |  | apigateway-system |  |  | Kubernetes 命名空间。 |
| data.clusterConfig.cluste rCode |  | string |  | k8s-cluster-001 |  |  | Kubernetes 集群编码。 |
| data.accessModeList |  | GetGwInstanceDeployM |  |  |  |  | accessModeList 字段。 |
|  |  |  | GetGwInstanceDeployM |  |  |  |  |
|  | a.accessModeList | sgResponse$AccessModeI |  |  |  |  |  |
|  |  |  |  |  | [] |  |  |
|  |  | nfo[] |  |  |  |  |  |
| data.accessModeList.na me |  | string |  | 内网访问 |  |  | 名称。 |
| data.accessModeList.typ e |  | string |  | intranet |  |  | 类型。 |
| data.accessModeList.intr anetUrlStrList |  | string[] |  | ["http://192.168.1.1 :80"] |  |  | intranetUrlStrList 字段。 |
| data.accessModeList.net workUrlStrList |  | string[] |  | ["http://api.example .com"] |  |  | networkUrlStrList 字段。 |
| data.podInfoList |  | GetGwInstanceDeployM sgResponse$PodInfo[] |  | [] |  |  | podInfoList 字段。 |
|  |  |  | GetGwInstanceDeployM |  |  |  |  |
|  | a.podInfoList | sgResponse$PodInfo[] |  |  |  |  |  |
| data.podInfoList.name |  | string |  | higress-001-pod-1 |  |  | 名称。 |
| data.podInfoList.isReady |  | boolean |  | true |  |  | isReady 字段。 |
| data.podInfoList.ipList |  | GetGwInstanceDeployM sgResponse$IpInfo[] |  | [] |  |  | ipList 字段。 |

| ["http://192.168.1.1 | intra |
|---|---|

|  | ["http://api.example | netwo |
|---|---|---|
| .com"] |  |  |

|  |  | GetGwInstanceDeployM |  |
|---|---|---|---|
| a.podInfoList.ipList | sgResponse$IpInfo[] |  |  |

智能体工厂 OpenTrek

| data.podInfoList.ipList.ip | string | 192.168.1.1 | IP 地址。 |
|---|---|---|---|
| data.podInfoList.ipList.ip Type | string | intranet | ipType 字段。 |
| data.gwInstanceId | string | higress-001 | 网关实例 ID。 |
| data.instanceName | string | higress-gateway | instanceName 字段。 |
| data.engineSpecification | string | standard | engineSpecification 字段。 |
| data.vpcId | string | vpc-001 | VPC ID。 |
| data.regionId | string | cn-hangzhou | regionId 字段。 |
| data.zoneId | string | cn-hangzhou-a | zoneId 字段。 |
| data.vSwitchId | string | vsw-001 | vSwitchId 字段。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/getInstanceDeployMsg HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "deploymentName": "deploymentName_value",
        "resConfig": {
            "cpuRequest": "cpuRequest_value",
            "memoryRequest": "memoryRequest_value",
            "cpuLimit": "cpuLimit_value",
            "memoryLimit": "memoryLimit_value",
            "replicas": 0,
            "jvmArgs": "jvmArgs_value"
        },
        "clusterConfig": {
            "clusterName": "clusterName_value",
            "namespace": "namespace_value",
            "clusterCode": "clusterCode_value"
        },
        "accessModeList": {
            "name": "name_value",
            "type": "type_value",
            "intranetUrlStrList": [],
            "networkUrlStrList": []
        },
        "podInfoList": {
            "name": "name_value",
            "isReady": true,
            "ipList": {
                "ip": "ip_value",
                "ipType": "ipType_value"
            }
        },
        "gwInstanceId": "gwInstanceId_value",
        "instanceName": "instanceName_value",
        "engineSpecification": "engineSpecification_value",
        "vpcId": "vpcId_value",
        "regionId": "regionId_value",
        "zoneId": "zoneId_value",
        "vSwitchId": "vSwitchId_value"
    }
}
```

#### getK8sServiceConfigContent

**API 接口概述**

**中文名称：**查询实例访问配置
**功能概述：**查询实例访问配置。

```
请求路径： /gatewayInstance/getInstanceAccessModeConfig
```

**请求方式：** `POST`
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/getInstanceAccessModeConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### getPortTemplates

智能体工厂 OpenTrek

**API 接口概述**

**中文名称：**查询端口模板
**功能概述：**查询端口模板。

```
请求路径： /gatewayInstance/getInstanceDeployPortTemplates
```

**请求方式：** `POST`

**请求参数**

无请求参数。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | AccessModePortTempla teResponse[] | [{}] | 响应数据。 |
| data.port | integer | 80 | 端口。 |
| data.targetPort | string | 8080 | targetPort 字段。 |
| data.nodePort | integer | 30080 | nodePort 字段。 |
| data.name | string | http-port | 名称。 |
| data.protocol | string | TCP | 协议类型。 |

|  |  | AccessModePortTempla | [{}] |
|---|---|---|---|
| a | teResponse[] |  |  |

**示例**

**请求示例**

```
POST /gatewayInstance/getInstanceDeployPortTemplates HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "port": 0,
        "targetPort": "targetPort_value",
        "nodePort": 0,
        "name": "name_value",
        "protocol": "protocol_value"
    }
}
```

#### importHigressInstance

**API 接口概述**

**中文名称：**导入 Higress 实例
**功能概述：**导入 Higress 实例。

```
请求路径： /gatewayInstance/importHigressInstance
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| namespace | string | body | 否 | higress- system | Kubernetes 命名空间。 |
| clusterCode | string | body | 否 | k8s- cluster-001 | Kubernetes 集群编码。 |
| ingressName | string | body | 否 | higress- ingress | Ingress 名称。 |

|  |  | higress- | K |
|---|---|---|---|
|  | system |  |  |

|  |  | k8s- | Ku |
|---|---|---|---|
|  | cluster-001 |  |  |

|  |  | higress- | In |
|---|---|---|---|
|  | ingress |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | boolean | true | 响应数据。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/importHigressInstance HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "namespace": "namespace_value",
  "clusterCode": "clusterCode_value",
  "ingressName": "ingressName_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": true
}
```

#### listAllGatewayInstances

**API 接口概述**

**中文名称：**查询所有实例
**功能概述：**查询所有实例。

```
请求路径： /gatewayInstance/listAllInstances
```

**请求方式：** `POST`

**请求参数**

无请求参数。

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | ListAllGwInstanceRes ponse[] | [{}] | 响应数据。 |
| data.gwInstanceId | string | higress-001 | 网关实例 ID。 |
| data.name | string | my-higress-gateway | 名称。 |
| data.status | integer | 1 | 状态。 |
| data.accessMode | GetInstanceAccessMod eResponse[] | [{}] | accessMode 字段。 |
| data.accessMode.ips | string[] | ["192.168.1.1"] | ips 字段。 |
| data.accessMode.ports | string[] | ["80", "443"] | ports 字段。 |
| data.accessMode.access ModeType | string | LoadBalancer | accessModeType 字段。 |
| data.accessMode.loadBal ancerNetworkType | string | internet | loadBalancerNetworkTyp e 字段。 |
| data.accessMode.loadBal ancerAddressType | string | external | loadBalancerAddressTyp e 字段。 |
| data.accessMode.service Name | string | higress-gateway | 服务名称。 |
| data.accessMode.extern alIps | string[] | [] | externalIps 字段。 |
| data.accessMode.clusterI p | string[] | ["10.0.0.1"] | clusterIp 字段。 |

| ListAllGwInstanceRes | [{}] |  |
|---|---|---|
|  |  | [{}] |

|  |  | GetInstanceAccessMod | [{}] |
|---|---|---|---|
| a.accessMode | eResponse[] |  |  |

智能体工厂 OpenTrek

| data.accessMode.edasAp pId | string | app-xxx | edasAppId 字段。 |
|---|---|---|---|
| data.accessMode.ipVersi on | string | IPv4 | ipVersion 字段。 |

**示例**

**请求示例**

```
POST /gatewayInstance/listAllInstances HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": [
        {
            "gwInstanceId": "instance-001",
            "name": "demo-instance",
            "status": 1,
            "accessMode": [
                {
                    "ips": ["192.168.1.1"],
                    "ports": ["8080"],
                    "accessModeType": "LoadBalancer",
                    "loadBalancerNetworkType": "vpc",
                    "loadBalancerAddressType": "intranet",
                    "serviceName": "service-name",
                    "externalIps": ["1.2.3.4"],
                    "clusterIp": ["10.0.0.1"],
                    "edasAppId": "edas-app-001",
                    "ipVersion": "ipv4"
                }
```

]

```json
        },
        {
            "gwInstanceId": "instance-002",
            "name": "another-instance",
            "status": 2,
            "accessMode": []
        }
```

]

```
}
```

智能体工厂 OpenTrek

#### listGatewayInstances

**API 接口概述**

**中文名称：**查询实例列表
**功能概述：**分页查询网关实例列表。

```
请求路径： /gatewayInstance/listInstances
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|
| current | integer | 是 | 1 | 当前页码，最小值为 1。 |
| size | integer | 是 | 10 | 每页大小，最小值为 1。 |
| name | string | 否 | my-gateway | 按实例名称过滤（模糊匹配）。 |
| gwInstanceId | string | 否 | gw-instance- 001 | 按实例ID过滤。 |
| deployMode | string | 否 | k8s | 按部署模式过滤。可选值： edas (EDAS K8s部署，SCG引擎)、 custom (自定义部署，SCG引擎)、 adp (ADP部署，SCG引擎)、 apig k8s ( _ APIG K8s部署，SCG 引擎)、 onpaas (共享PaaS部署，SHARED SCG _ 引擎)、 k8s (K8s 部署，Higress引擎)、 acs k8s (A _ CS K8s部署，Higress引擎)。 |
| status | integer | 否 | 1 | 按实例状态过滤。 |

|  |  | gw-instance- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| brokerEngineType | string | 否 | HIGRESS |  | 按引擎类型过滤。可选值： HIGRESS (AI 网关)、 SCG (API 网关)、 SHARED SCG _ (共享型API网关)、 CLOUD NATIV _ E GATEWAY (云原生 _ 网关)。 |  |  |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | CLOUD NATIV _ |  |
|  |  |  |  |  | E GATEWAY _ |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | xxx-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据，分页结果对象。 |
| data.total | integer | 100 | 总记录数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | array | [] | 实例记录列表，详见下方二级参数表。 |

**records 二级参数表：**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| records[].status | integer | 1 | 实例状态。 |
| records[].gwInstanceId | string | gw-instance-001 | 网关实例ID。 |
| records[].name | string | my-gateway | 网关实例名称。 |

智能体工厂 OpenTrek

| records[].instanceName | string | my-gateway | 实例名称。 |
|---|---|---|---|
| records[].deployClusterN amespace | string | apigateway-system | 部署集群命名空间。 |
| records[].deployClusterC ode | string | cluster-001 | 部署集群编码。 |
| records[].deployClusterN ame | string | 生产集群 | 部署集群名称。 |
| records[].k8sServiceNam e | string | higress-gateway | K8s Service名称。 |
| records[].createTime | string | 2024-01- 01T00:00:00 | 创建时间。 |
| records[].modifyTime | string | 2024-01- 01T00:00:00 | 修改时间。 |
| records[].vpcId | string | vpc-xxx | VPC ID。 |
| records[].vSwitchId | string | vsw-xxx | vSwitch ID。 |
| records[].regionId | string | cn-hangzhou | 区域ID。 |
| records[].zoneId | string | cn-hangzhou-a | 可用区ID。 |
| records[].deployMode | string | k8s | 部署模式。 |
| records[].edasAppId | string | app-xxx | EDAS应用ID。 |
| records[].edasNamespac eId | string | ns-xxx | EDAS命名空间ID。 |
| records[].k8sClusterId | string | k8s-xxx | K8s集群ID。 |
| records[].k8sNamespace | string | default | K8s命名空间。 |
| records[].instanceClass | string | standard | 实例规格类型。 |
| records[].department | string | 研发部 | 所属部门。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| records[].resourceGroup | string | group-001 | 资源组。 |
|---|---|---|---|
| records[].ingressClassNa me | string | higress | IngressClass名称。 |
| records[].brokerEngineTy pe | string | HIGRESS | 引擎类型。 |
| records[].brokerEngineV ersion | string | 1.4.0 | 当前引擎版本。 |
| records[].brokerLatestEn gineVersion | string | 1.5.0 | 最新引擎版本。 |
| records[].deployClusterA ttribute | string | hub | 部署集群属性。 |
| records[].nodeNumber | integer | 2 | 节点数量。 |
| records[].sharedInstance | boolean | false | 是否为共享实例。 |
| records[].sharedInstance Source | string | external-sharing | 共享实例来源。 |
| records[].higressDeploy mentUid | string | uid-xxx | Higress Deployment的 K8s UID。 |
| records[].o11y | object | {} | 可观测配置对象。 |
| records[].o11y.slsEnable d | boolean | true | 是否启用SLS日志。 |
| records[].o11y.promethe usEnabled | boolean | true | 是否启用Prometheus监控。 |
| records[].accessMode | array | [] | 访问模式列表，详见下方三级参数表。 |
| records[].edasAppInfos | array | [] | EDAS应用信息列表。 |

**records[].accessMode 三级参数表：**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| accessMode[].ips | string[] | ["192.168.1.1"] | IP地址列表。 |

智能体工厂 OpenTrek

| accessMode[].ports | string[] | ["80", "443"] | 端口列表。 |
|---|---|---|---|
| accessMode[].accessMod eType | string | LoadBalancer | 访问模式类型。 |
| accessMode[].loadBalanc erNetworkType | string | internet | 负载均衡器网络类型。 |
| accessMode[].loadBalanc erAddressType | string | external | 负载均衡器地址类型。 |
| accessMode[].serviceNa me | string | higress-gateway | K8s Service名称。 |
| accessMode[].externalIp s | string[] | [] | 外部IP列表。 |
| accessMode[].clusterIp | string[] | ["10.0.0.1"] | 集群IP列表。 |
| accessMode[].edasAppId | string | app-xxx | EDAS应用ID。 |
| accessMode[].ipVersion | string | IPv4 | IP版本。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/listInstances HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "current": 1,
  "size": 10,
  "brokerEngineType": "HIGRESS",
  "deployMode": "k8s"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "msg": "success",
  "message": "success",
  "requestId": "req-xxx-xxx-xxx",
  "data": {
    "total": 2,
    "current": 1,
    "size": 10,
    "records": [
      {
        "status": 1,
        "gwInstanceId": "gw-instance-001",
        "name": "my-higress-gateway",
        "instanceName": "my-higress-gateway",
        "deployClusterNamespace": "apigateway-system",
        "deployClusterCode": "cluster-001",
        "deployClusterName": "生产集群",
        "k8sServiceName": "higress-gateway",
        "createTime": "2024-01-01T10:00:00",
        "modifyTime": "2024-01-01T10:00:00",
        "deployMode": "k8s",
        "brokerEngineType": "HIGRESS",
        "brokerEngineVersion": "1.4.0",
        "nodeNumber": 2,
        "sharedInstance": false,
        "o11y": {
          "slsEnabled": true,
          "prometheusEnabled": true
        },
        "accessMode": [
          {
            "ips": ["192.168.1.1"],
            "ports": ["80", "443"],
            "accessModeType": "LoadBalancer",
            "serviceName": "higress-gateway"
          }
```

]

```
      }
```

]

```
  }
}
```

#### modifyCapacity

**API 接口概述**

**中文名称：**修改资源容量
**功能概述：**修改资源容量。

```
请求路径： /gatewayInstance/modifyResource
```

**请求方式：** `POST`
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| replicas | integer | body | 否 | 3 | 副本数。 |
| specificationTe mplate | integer | body | 否 | 1 | specificationTe mplate 参数。 |
| source | string | body | 否 | manual | source 参数。 |
| instanceClass | string | body | 否 | 4c8g | 实例规格类型。 |
| backupZoneId | string | body | 否 | cn- hangzhou-b | backupZoneId 参数。 |
| backupVSwitch Id | string | body | 否 | vsw-xxx- xxx | backupVSwitch Id 参数。 |
| thirdZoneId | string | body | 否 | cn- hangzhou-c | thirdZoneId 参数。 |
| thirdVSwitchId | string | body | 否 | vsw-xxx- xxx | thirdVSwitchId 参数。 |
| zoneType | string | body | 否 | multizone | zoneType 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | cn- |  |
|---|---|---|---|
|  | hangzhou-b |  |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

|  |  | cn- |  |
|---|---|---|---|
|  | hangzhou-c |  |  |

|  |  | vsw-xxx- |
|---|---|---|
|  | xxx |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |

智能体工厂 OpenTrek

| data | string | higress-001 | 响应数据。 |
|---|---|---|---|

**示例**

**请求示例**

```json
POST /gatewayInstance/modifyResource HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "replicas": 0,
  "specificationTemplate": 0,
  "source": "source_value",
  "instanceClass": "instanceClass_value",
  "backupZoneId": "backupZoneId_value",
  "backupVSwitchId": "backupVSwitchId_value",
  "thirdZoneId": "thirdZoneId_value",
  "thirdVSwitchId": "thirdVSwitchId_value",
  "zoneType": "zoneType_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### modifyInstance

**API 接口概述**

**中文名称：**修改实例
**功能概述：**修改实例。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|
| instanceName | string | body | 是 | my-higress- instance | instanceName 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-higress- | instanc |
|---|---|---|---|
|  | instance |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | boolean | true | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "instanceName": "my-higress-instance"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": true
}
```

智能体工厂 OpenTrek

#### modifyInstanceImageUrl

**API 接口概述**

**中文名称：**修改实例镜像地址
**功能概述：**修改实例镜像地址。

```
请求路径： /gatewayInstance/modifyInstanceImageUrl
```

**请求方式：** `POST`

**请求参数**

| 参数名称 |  | 类型 |  | 位置 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gwInstanceId |  | string |  | body |  |  |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| imageUrl |  | string |  |  |  |  |  |  |  | higress- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | higress- |  |  |
|  |  |  |  |  |  |  |  |  |  | registry.cn- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | hangzhou.cr.a |  |  |  |
|  |  |  |  |  | body |  |  | 是 |  |  |  | imageUrl参数。 |  |
|  |  |  |  |  |  |  |  |  |  | liyuncs.com/h |  |  |  |
|  |  |  |  |  |  |  |  |  |  | igress/gatewa |  |  |  |
|  |  |  |  |  |  |  |  |  |  | y:1.4.0 |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | boolean | true | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /gatewayInstance/modifyInstanceImageUrl HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "imageUrl": "imageUrl_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": true
}
```

#### refresh

**API 接口概述**

**中文名称：**刷新实例状态
**功能概述：**刷新实例状态。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceCod e | string | body | 是 | higress- 001 | gwInstanceCod e 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

| msg |  | string |  | success | 响应消息。 |
|---|---|---|---|---|---|
| message |  | string |  | success | 响应消息。 |
| data |  | object |  | {} | 响应数据。 |
| data.status |  | integer |  | 1 | 状态。 |
| data.gwInstanceId |  | string |  | higress-001 | 网关实例 ID。 |
| data.name |  | string |  | my-higress-gateway | 名称。 |
| data.deployClusterName space |  | string |  | apigateway-system | deployClusterNamespac e 字段。 |
| data.deployClusterCode |  | string |  | cluster-001 | deployClusterCode 字段。 |
| data.accessMode |  | RefreshGwInstanceRes |  | [{}] | accessMode 字段。 |
|  |  |  | RefreshGwInstanceRes |  |  |
|  | a.accessMode | ponse$AccessModeInfo[] |  |  |  |
| data.accessMode.ips |  | string[] |  | ["192.168.1.1"] | ips 字段。 |
| data.accessMode.ports |  | string[] |  | ["80", "443"] | ports 字段。 |
| data.accessMode.access ModeType |  | string |  | LoadBalancer | accessModeType 字段。 |
| data.accessMode.extern alIps |  | string[] |  | [] | externalIps 字段。 |
| data.accessMode.clusterI p |  | string[] |  | ["10.0.0.1"] | clusterIp 字段。 |
| data.deployClusterName |  | string |  | 生产集群 | deployClusterName 字段。 |
| data.k8sServiceName |  | string |  | higress-gateway | k8sServiceName 字段。 |
| data.createTime |  | string |  | 2024-01- 01T00:00:00 | 创建时间。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| data.modifyTime | string | 2024-01- 01T00:00:00 | modifyTime 字段。 |
|---|---|---|---|
| data.tid | string | tid-xxx | tid 字段。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceCode": "gwInstanceCode_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "status": 0,
        "gwInstanceId": "gwInstanceId_value",
        "name": "name_value",
        "deployClusterNamespace": "deployClusterNamespace_value",
        "deployClusterCode": "deployClusterCode_value",
        "accessMode": {
            "ips": [],
            "ports": [],
            "accessModeType": "accessModeType_value",
            "externalIps": [],
            "clusterIp": []
        },
        "deployClusterName": "deployClusterName_value",
        "k8sServiceName": "k8sServiceName_value",
        "createTime": "createTime_value",
        "modifyTime": "modifyTime_value",
        "tid": "tid_value"
    }
}
```

#### removeGwInstance

**API 接口概述**

**中文名称：**删除实例
智能体工厂 OpenTrek
**功能概述：**删除实例。

```
请求路径： /gatewayInstance/deleteInstance
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| forcedDelete | boolean | body | 否 | false | forcedDelete 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

**请求示例**

```json
POST /gatewayInstance/deleteInstance HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "forcedDelete": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### restart

**API 接口概述**

**中文名称：**重启实例
**功能概述：**重启实例。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### stopInstance

**API 接口概述**

**中文名称：**停止实例
**功能概述：**停止实例。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | boolean | true | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": true
}
```

#### upgradeInstance

**API 接口概述**

**中文名称：**升级实例
**功能概述：**升级实例。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

### MCP管理

#### addConsumers

**API 接口概述**

**中文名称：**添加 MCP 授权消费者
**功能概述：** MCP Server 授权消费者。

```
请求路径： /mcpServer/addMcpServerConsumers
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body |  | 是 |  | higress- 001 |  | 网关实例 ID。 |  |
| mcpServerNam e | string | body |  | 是 |  | my-mcp- server |  | MCP 服务名称。 |  |
| consumers | string[] | body |  |  |  | ["consumer- |  |  |  |
|  |  |  |  |  |  |  | ["consumer- |  |  |
|  |  |  |  |  |  | 001", |  |  |  |
|  |  |  |  |  |  |  |  | consum |  |
|  |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  | "consumer- |  |  |  |
|  |  |  |  |  |  | 002"] |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | success | 响应数据。 |

**示例**

**请求示例**

```json
POST /mcpServer/addMcpServerConsumers HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "mcpServerName": "my-mcp-server",
  "consumers": ["consumer-001", "consumer-002"]
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "success"
}
```

#### createMcpServer

**API 接口概述**

**中文名称：**创建 MCP 服务
**功能概述：**创建 MCP 服务。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

|  | 参数名称 |  | 类型 |  | 位置 |  |  |  | 是否必选 |  |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | gwInstanceId |  | string |  | body |  |  |  | 是 |  |  | higress- 001 |  | 网关实例 ID。 |  |
|  | id |  | string |  | body |  |  |  | 否 |  |  | mcp-server- 001 |  | ID 标识。 |  |
|  | name |  | string |  | body |  |  |  | 否 |  |  | my-mcp- server |  | MCP 服务名称。 |  |
|  | description |  | string |  | body |  |  |  | 否 |  |  | 数据库查询服务 |  | MCP 服务描述。 |  |
|  | domains |  | string[] |  | body |  |  |  | 否 |  |  | ["api.exampl e.com"] |  | MCP 服务生效的域名列表。 |  |
|  |  |  | CreateMcpSer |  |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  | CreateMcpSer |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId | MCP 服务上游服 |  |
|  |  |  | verRequest$Hi |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | body |  |  | 是 |  |  | ": "service- |  | MCP |  |
|  | services | vices |  |  |  | body |  |  |  |  |  |  |  | 务列 |  |
|  |  |  | gressServiceT |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 001"}] |  |  |  |
|  |  |  | arget[] |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | mcp-server- | I |
|---|---|---|---|
|  | 001 |  |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

|  |  | 数据库查询服 |
|---|---|---|
|  | 务 |  |

|  |  | ["api.exampl | MCP 服 |
|---|---|---|---|
|  | e.com"] |  |  |

智能体工厂 OpenTrek

| type | string | body |  |  | 否 |  | DATABASE |  | MCP 服务类型。 可选值： OPEN API _ （OpenAPI 类型，通过 API 工具提供服务）、 DATABA SE （数据库类型，直连数据库提供服务）、 DIRECT ROUTE （直连 _ 路由类型）。 |  |
|---|---|---|---|---|---|---|---|---|---|---|
| consumerAuthI nfo | object | body |  |  |  |  | {"type": |  |  |  |
|  |  |  |  |  |  |  |  | {"type": |  |  |
|  |  |  |  |  |  |  | "consumer", |  |  |  |
|  |  |  | body |  |  |  |  |  | 消费者认证配 |  |
|  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  | "enable": |  |  |  |
|  |  |  |  |  |  |  | true} |  |  |  |
| rawConfigurati ons | string | body |  |  | 否 |  | tools:\n - name: query |  | YAML 格式的原始配置。 |  |
| dbConfig | object | body |  |  | 否 |  | 见下方示例 |  | 数据库配置（数据库类型 MCP 服务，type=DATA BASE 时需填写）。 |  |
| dbType | string | body |  |  | 否 |  | MYSQL |  | 数据库类型。可选值： MYSQL （MySQL 数据库）、 POSTGR ESQL （Postgr eSQL 数据库）、 SQLITE （SQLite 数据库）、 CLICKH OUSE （ClickH ouse 数据库）。 |  |
| directRouteCon fig | object | body |  |  | 否 |  | 见下方示例 |  | 直连路由配置。 |  |
| observabilityEn abled | boolean | body |  |  | 否 |  | true |  | MCP Server observability enabled flag。 |  |

| DATABA |  |
|---|---|

|  |  | DIRECT |  |
|---|---|---|---|
|  | ROUTE _ |  |  |

|  |  | tools:\n - | YAML 格式 |
|---|---|---|---|
|  | name: query |  |  |

| POSTGR |  |
|---|---|

|  | ESQL |
|---|---|

| CLICKH |  |
|---|---|

|  | OUSE |
|---|---|

**services 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| serviceId | string | body | 否 | service- 001 | 服务 ID。 |
|---|---|---|---|---|---|

|  |  | service- |
|---|---|---|
|  | 001 |  |

**consumerAuthInfo 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | consumer | MCP 服务类型。 |
| enable | boolean | body | 否 | true | 是否启用。 |
| allowedConsu mers | string[] | body | 否 | ["consumer- 001"] | 允许的消费者名称列表。 |

|  |  | ["consumer- | 允许 |
|---|---|---|---|
|  | 001"] |  |  |

**dbConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| host | string | body | 否 | 192.168.1.10 0 | 主机地址。 |
| port | string | body | 否 | 3306 | 端口。 |
| username | string | body | 否 | root | 用户名。 |
| password | string | body | 否 | password123 | 密码。 |
| dbname | string | body | 否 | mydb | 数据库名称。 |
| otherParams | object | body | 否 | {"charset": "utf8mb4"} | 其他数据库连接参数，详见下方说明。 |

|  |  | 192.168.1.10 |  |
|---|---|---|---|
|  | 0 |  |  |

|  |  | password123 |
|---|---|---|

|  |  | {"charset": | 其他数据库参数，详见 |
|---|---|---|---|
|  | "utf8mb4"} |  |  |

**otherParams 常用参数：**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| sslmode | string | require | SSL 连接模式 （PostgreSQL），可选值： disable 、 requ ire 、 verify- ca 、 verify-full 。 |  |  |
|---|---|---|---|---|---|
|  |  |  |  | requ |  |
| connect timeout _ | integer | 10 | 连接超时时间（秒）。 |  |  |
| charset | string | utf8mb4 | 字符集编码（MySQL）。 |  |  |
| ssl | string | true | 是否启用 SSL 连接。 |  |  |
| timeout | integer | 30 | 查询超时时间（秒）。 |  |  |

|  |  |  | disable |  |
|---|---|---|---|---|
|  |  | ire |  |  |
|  |  | ca |  |  |

**说明**： `otherParams` 为数据库连接的额外参数，以 key-value 形式传递。具体参数取决于数据库类型
（MySQL、PostgreSQL、SQLite、ClickHouse）和实际需求。

**directRouteConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| path | string | body | 否 | /api/v1 | 路径。 |
| transportType | string | body | 否 | http | 传输类型。 |
| protocolConver sion | boolean | body | 否 | true | 协议转换标志。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | mcp-server-001 | 响应数据。 |

**示例**

智能体工厂 OpenTrek

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "id": "mcp-server-001",
  "name": "my-mcp-server",
```

`"description": "`数据库查询服务`",`

```json
  "domains": ["api.example.com"],
  "services": [
    {
      "serviceId": "service-001"
    }
```

`],`

```json
  "type": "DATABASE",
  "consumerAuthInfo": {
    "type": "consumer",
    "enable": true,
    "allowedConsumers": ["consumer-001"]
  },
  "dbConfig": {
    "host": "192.168.1.100",
    "port": "3306",
    "username": "root",
    "password": "password123",
    "dbname": "mydb",
    "otherParams": {"charset": "utf8mb4"}
  },
  "dbType": "MYSQL",
  "observabilityEnabled": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "mcp-server-001"
}
```

#### deleteConsumers

**API 接口概述**

**中文名称：**删除 MCP 授权消费者
**功能概述：** MCP Server 解除授权消费者。
智能体工厂 OpenTrek
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| mcpServerNam e | string | body | 是 | my-mcp- server | MCP 服务名称。 |
| consumers | string[] | body | 是 | ["consumer- 001"] | consumers 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

|  |  | ["consumer- | con |
|---|---|---|---|
|  | 001"] |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | success | 响应数据。 |

**示例**

**请求示例**

```json
POST /mcpServer/deleteMcpServerConsumers HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "mcpServerName": "my-mcp-server",
  "consumers": ["consumer-001"]
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "success"
}
```

#### deleteMcpServer

**API 接口概述**

**中文名称：**删除 MCP 服务
**功能概述：**删除 MCP 服务。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| mcpServerNam e | string | body | 是 | my-mcp- server | MCP 服务名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | my-mcp-server | 响应数据。 |

智能体工厂 OpenTrek

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "mcpServerName": "my-mcp-server"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "my-mcp-server"
}
```

#### getMcpServer

**API 接口概述**

**中文名称：**查询 MCP 服务详情
**功能概述：**查询 MCP 服务详情。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| mcpServerNam e | string | body | 是 | my-mcp- server | MCP 服务名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求 ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | 见下方 | 响应数据。 |
| data.gwInstanceId | string | higress-001 | 网关实例 ID。 |
| data.name | string | my-mcp-server | 名称。 |
| data.description | string | 数据库查询服务 | 描述信息。 |
| data.domains | string[] | ["api.example.com"] | domains 字段。 |
| data.services | HigressServiceSimple Response[] | 见下方 | services 字段。 |
| data.services.serviceId | string | service-001 | 服务 ID。 |
| data.services.name | string | ai-service | 名称。 |
| data.consumerAuthInfo | object | 见下方 | 消费者认证配置。 |
| data.consumerAuthInfo.t ype | string | consumer | 类型。 |
| data.consumerAuthInfo.e nable | boolean | true | 是否启用。 |
| data.consumerAuthInfo.a llowedConsumers | string[] | ["consumer-001"] | 允许的消费者名称列表。 |
| data.rawConfigurations | string | tools:\n - name: query | 原始配置内容。 |
| data.type | string | DATABASE | 类型。 |

|  | ["api.example.com"] |
|---|---|

|  |  | HigressServiceSimple | 见下方 |
|---|---|---|---|
| a.services | Response[] |  |  |

|  | tools:\n - name: |  |
|---|---|---|
| query |  |  |

智能体工厂 OpenTrek

| data.dbType | string | MYSQL | 数据库类型。 |
|---|---|---|---|
| data.dbConfig | object | 见下方 | 数据库配置。 |
| data.dbConfig.host | string | 192.168.1.100 | 主机地址。 |
| data.dbConfig.port | string | 3306 | 端口。 |
| data.dbConfig.username | string | root | 用户名。 |
| data.dbConfig.password | string | password123 | 密码。 |
| data.dbConfig.dbname | string | mydb | 数据库名称。 |
| data.dbConfig.otherPara ms | object | {"charset": "utf8mb4"} | 其他参数。 |
| data.directRouteConfig | object | 见下方 | 直连路由配置。 |
| data.directRouteConfig.p ath | string | /api/v1 | 路径。 |
| data.directRouteConfig.tr ansportType | string | http | 传输类型。 |
| data.directRouteConfig.p rotocolConversion | boolean | true | 协议转换标志。 |
| data.observabilityEnable d | boolean | true | 是否启用可观测性。 |
| data.tools | McpToolInfo[] | 见下方 | tools 字段。 |
| data.tools.name | string | query | 名称。 |
| data.tools.description | string | 查询数据库 | 描述信息。 |
| data.tools.inputSchema | object | {} | inputSchema 字段。 |

|  |  | {"charset": |  |
|---|---|---|---|
|  | "utf8mb4"} |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "mcpServerName": "my-mcp-server"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": {
    "gwInstanceId": "higress-001",
    "name": "my-mcp-server",
```

`"description": "`数据库查询服务`",`

```json
    "domains": ["api.example.com"],
    "services": {
      "serviceId": "service-001",
      "name": "ai-service"
    },
    "consumerAuthInfo": {
      "type": "consumer",
      "enable": true,
      "allowedConsumers": ["consumer-001"]
    },
    "rawConfigurations": "tools:\n  - name: query",
    "type": "DATABASE",
    "dbType": "MYSQL",
    "dbConfig": {
      "host": "192.168.1.100",
      "port": "3306",
      "username": "root",
      "password": "password123",
      "dbname": "mydb",
      "otherParams": {"charset": "utf8mb4"}
    },
    "directRouteConfig": {
      "path": "/api/v1",
      "transportType": "http",
      "protocolConversion": true
    },
    "observabilityEnabled": true,
    "tools": {
      "name": "query",
```

`"description": "`查询数据库`",`

```json
      "inputSchema": {}
    }
  }
}
```

智能体工厂 OpenTrek

#### getSsePathSuffix

**API 接口概述**

**中文名称：**查询 SSE 路径后缀
**功能概述：**获取 MCP Server SSE 后缀路径。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | /sse/mcp-server- 001 | 响应数据。 |

|  | /sse/mcp-server- |
|---|---|
| 001 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001"
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "/sse/mcp-server-001"
}
```

#### listConsumers

**API 接口概述**

**中文名称：**查询 MCP 授权消费者列表
**功能概述：**查询 MCP Server 授权消费者列表。

```
请求路径： /mcpServer/listMcpServerConsumers
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |
| mcpServerNam e | string | body | 否 | my-mcp- server | MCP 服务名称。 |
| consumerNam e | string | body | 否 | my- consumer | 消费者名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

|  |  | my- |
|---|---|---|
|  | consumer |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ListMcpServerConsume rsResponse[] | - | 记录列表。 |
| data.records.gwInstanceI d | string | higress-001 | 网关实例 ID。 |
| data.records.mcpServer Name | string | my-mcp-server | MCP Server 名称。 |
| data.records.consumerN ame | string | my-consumer | 消费者名称。 |
| data.records.authType | string | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT，4=OAuth 2。 |
| data.records.enable | boolean | true | 是否启用。 |

|  |  | ListMcpServerConsume | - |
|---|---|---|---|
| a.records | rsResponse[] |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /mcpServer/listMcpServerConsumers HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value",
  "mcpServerName": "mcpServerName_value",
  "consumerName": "consumerName_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "total": 0,
        "current": 0,
        "size": 0,
        "records": {
            "gwInstanceId": "gwInstanceId_value",
            "mcpServerName": "mcpServerName_value",
            "consumerName": "consumerName_value",
            "authType": "authType_value",
            "enable": true
        }
    }
}
```

#### listMcpServers

**API 接口概述**

**中文名称：**查询 MCP 服务列表
**功能概述：**查询 MCP 服务列表。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |

智能体工厂 OpenTrek

| current | integer | body | 是 | 1 |  | 当前页码。 |  |  |
|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 |  | 网关实例 ID。 |  |  |
| name | string | body | 否 | my-mcp- server |  | 名称。 |  |  |
| type | string | body | 否 | OPEN API _ |  | MCP 服务类型。 可选值： OPEN API _ （OpenAPI 类型）、 DATABA SE （数据库类型）、 DIRECT ROUTE （直连 _ 路由类型）。 |  |  |
|  |  |  |  |  |  |  | DIRECT |  |
|  |  |  |  |  |  | ROUTE _ |  |  |
| domainId | string | body | 否 | domain- 001 |  | 域名 ID。 |  |  |
| serviceId | string | body | 否 | service- 001 |  | 服务 ID。 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

| OPEN API _ |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  | SE |

| DATABA |  |
|---|---|

|  |  | domain- |
|---|---|---|
|  | 001 |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |

智能体工厂 OpenTrek

| data.records | ListMcpServerRespons e[] | - | 记录列表。 |
|---|---|---|---|
| data.records.id | string | mcp-001 | ID 标识。 |
| data.records.gwInstanceI d | string | higress-001 | 网关实例 ID。 |
| data.records.name | string | my-mcp-server | 名称。 |
| data.records.description | string | MCP 服务描述 | 描述信息。 |
| data.records.domains | string[] | ["api.example.com"] | 域名列表。 |
| data.records.services | HigressServiceSimple Response[] | - | 服务列表。 |
| data.records.services.ser viceId | string | service-001 | 服务 ID。 |
| data.records.services.na me | string | my-service | 服务名称。 |
| data.records.consumerA uthInfo | object | - | 消费者认证配置。 |
| data.records.consumerA uthInfo.type | string | key-auth | 认证类型。 |
| data.records.consumerA uthInfo.enable | boolean | true | 是否启用。 |
| data.records.consumerA uthInfo.allowedConsume rs | string[] | ["consumer-001"] | 允许的消费者列表。 |
| data.records.rawConfigur ations | string | {...} | 原始配置内容。 |
| data.records.type | string | OPEN API _ | MCP 类型。 |
| data.records.dbType | string | mysql | 数据库类型。 |

|  |  | ListMcpServerRespons |  |  |
|---|---|---|---|---|
| a.records | e[] |  |  |  |

|  | ["api.example.com"] |
|---|---|

|  |  | HigressServiceSimple | - |
|---|---|---|---|
| a.records.services | Response[] |  |  |

智能体工厂 OpenTrek

| data.records.dbConfig | object | - | 数据库配置。 |
|---|---|---|---|
| data.records.dbConfig.ho st | string | 192.168.1.100 | 主机地址。 |
| data.records.dbConfig.po rt | string | 3306 | 端口。 |
| data.records.dbConfig.us ername | string | root | 用户名。 |
| data.records.dbConfig.pa ssword | string | password123 | 密码。 |
| data.records.dbConfig.db name | string | my database _ | 数据库名称。 |
| data.records.dbConfig.ot herParams | object | {} | 其他参数。 |
| data.records.directRoute Config | object | - | 直连路由配置。 |
| data.records.directRoute Config.path | string | /mcp/v1 | 路径。 |
| data.records.directRoute Config.transportType | string | http | 传输类型。 |
| data.records.directRoute Config.protocolConversio n | boolean | true | 是否启用协议转换。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value",
  "name": "name_value",
  "type": "type_value",
  "domainId": "domainId_value",
  "serviceId": "serviceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "total": 0,
        "current": 0,
        "size": 0,
        "records": {
            "id": "id_value",
            "gwInstanceId": "gwInstanceId_value",
            "name": "name_value",
            "description": "description_value",
            "domains": [],
            "services": {
                "serviceId": "serviceId_value",
                "name": "name_value"
            },
            "consumerAuthInfo": {
                "type": "type_value",
                "enable": true,
                "allowedConsumers": []
            },
            "rawConfigurations": "rawConfigurations_value",
            "type": "type_value",
            "dbType": "dbType_value",
            "dbConfig": {
                "host": "host_value",
                "port": "port_value",
                "username": "username_value",
                "password": "password_value",
                "dbname": "dbname_value",
                "otherParams": {}
            },
            "directRouteConfig": {
                "path": "path_value",
                "transportType": "transportType_value",
                "protocolConversion": true
            }
        }
    }
}
```

#### swaggerToMcpConfig

**API 接口概述**

**中文名称：** Swagger 转 MCP 配置
**功能概述：**将 Swagger 配置转换为 MCP 配置。
**请求方式：** `POST`
智能体工厂 OpenTrek
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| content | string | body | 是 | {"swagger":" 2.0",...} | Swagger 内容。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例 ID。 |

|  |  | {"swagger":" | Swagger |
|---|---|---|---|
|  | 2.0",...} |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求 ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.mcpConfigContent | string | {...} | MCP 配置内容。 |
| data.warnings | string[] | [] | 警告信息列表。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "content": "content_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "mcpConfigContent": "mcpConfigContent_value",
        "warnings": []
    }
}
```

#### updateMcpServer

**API 接口概述**

**中文名称：**更新 MCP 服务
**功能概述：**编辑 MCP 服务。
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress 引擎）实例。

**请求参数**

|  | 参数名称 |  | 类型 |  | 位置 |  |  |  | 是否必选 |  |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | gwInstanceId |  | string |  | body |  |  |  | 是 |  |  | higress- 001 |  | 网关实例 ID。 |  |
|  | id |  | string |  | body |  |  |  | 否 |  |  | mcp-server- 001 |  | ID 标识。 |  |
|  | name |  | string |  | body |  |  |  | 否 |  |  | my-mcp- server |  | MCP Server 名称。 |  |
|  | description |  | string |  | body |  |  |  | 否 |  |  | 数据库查询服务（已更新） |  | MCP Server 描述。 |  |
|  | domains |  | string[] |  | body |  |  |  | 否 |  |  | ["api.exampl e.com"] |  | MCP Server 适用的域名列表。 |  |
|  |  |  | CreateMcpSer |  |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  | CreateMcpSer |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId | MCP Server 上 |  |
|  |  |  | verRequest$Hi |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  | body |  |  | 是 |  |  | ": "service- |  | MCP |  |
|  | services | vices |  |  |  | body |  |  |  |  |  |  |  | 游服 |  |
|  |  |  | gressServiceT |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 001"}] |  |  |  |
|  |  |  | arget[] |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | mcp-server- | I |
|---|---|---|---|
|  | 001 |  |  |

|  |  | my-mcp- |  |
|---|---|---|---|
|  | server |  |  |

|  |  | 数据库查询服 | MCP Ser |
|---|---|---|---|
|  | 务（已更新） |  |  |

|  |  | ["api.exampl | MCP Se |
|---|---|---|---|
|  | e.com"] |  |  |

智能体工厂 OpenTrek

| type | string | body |  |  | 否 |  | DATABASE |  | MCP 服务类型。 可选值： OPEN API _ （OpenAPI 类型）、 DATABA SE （数据库类型）、 DIRECT ROUTE （直连 _ 路由类型）。 |  |
|---|---|---|---|---|---|---|---|---|---|---|
| consumerAuthI nfo | object | body |  |  |  |  | {"type": |  |  |  |
|  |  |  |  |  |  |  |  | {"type": |  |  |
|  |  |  |  |  |  |  | "consumer", |  |  |  |
|  |  |  | body |  |  |  |  |  | 消费者认证配 |  |
|  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  | "enable": |  |  |  |
|  |  |  |  |  |  |  | true} |  |  |  |
| rawConfigurati ons | string | body |  |  | 否 |  | tools:\n - name: query |  | YAML 格式的原始配置。 |  |
| dbConfig | object | body |  |  | 否 |  | 见下方示例 |  | 数据库配置 （type=DATAB ASE 时需填写）。 |  |
| dbType | string | body |  |  | 否 |  | MYSQL |  | 数据库类型。可选值： MYSQL （MySQL）、 POSTGRESQL （PostgreSQL） 、 SQLITE （ SQLite）、 CL ICKHOUSE （Cl ickHouse）。 |  |
| directRouteCon fig | object | body |  |  | 否 |  | 见下方示例 |  | 直连路由配置。 |  |
| observabilityEn abled | boolean | body |  |  | 否 |  | true |  | 是否启用 MCP Server 可观测性。 |  |

| DATABASE |  |  |  |  |
|---|---|---|---|---|
|  |  |  |  | SE |

| DATABA |  |
|---|---|

|  |  | DIRECT |  |
|---|---|---|---|
|  | ROUTE _ |  |  |

|  |  | tools:\n - | YAML 格式 |
|---|---|---|---|
|  | name: query |  |  |

|  | ICKHOUSE |  |
|---|---|---|

**services 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | string | body | 否 | service- 001 | 服务 ID。 |

|  |  | service- |
|---|---|---|
|  | 001 |  |

**consumerAuthInfo 对象结构**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | consumer | 认证类型。 |
| enable | boolean | body | 否 | true | 是否启用。 |
| allowedConsu mers | string[] | body | 否 | ["consumer- 001"] | 允许的消费者名称列表。 |

|  |  | ["consumer- | 允许 |
|---|---|---|---|
|  | 001"] |  |  |

**dbConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| host | string | body | 否 | 192.168.1.10 0 | 主机地址。 |
| port | string | body | 否 | 3306 | 端口。 |
| username | string | body | 否 | root | 用户名。 |
| password | string | body | 否 | password123 | 密码。 |
| dbname | string | body | 否 | mydb | 数据库名称。 |
| otherParams | object | body | 否 | {"charset": "utf8mb4"} | 其他参数。 |

|  |  | 192.168.1.10 |  |
|---|---|---|---|
|  | 0 |  |  |

|  |  | password123 |
|---|---|---|

|  |  | {"charset": | 其他参数。 |
|---|---|---|---|
|  | "utf8mb4"} |  |  |

**directRouteConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| path | string | body | 否 | /api/v1 | 路径。 |
| transportType | string | body | 否 | http | 传输类型。 |
| protocolConver sion | boolean | body | 否 | true | 协议转换标志。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求 ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | mcp-server-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "id": "mcp-server-001",
  "name": "my-mcp-server",
```

`"description": "`数据库查询服务（已更新）`",`

```json
  "domains": ["api.example.com"],
  "services": [
    {
      "serviceId": "service-001"
    }
```

`],`

```json
  "type": "DATABASE",
  "consumerAuthInfo": {
    "type": "consumer",
    "enable": true,
    "allowedConsumers": ["consumer-001"]
  },
  "dbConfig": {
    "host": "192.168.1.100",
    "port": "3306",
    "username": "root",
    "password": "password123",
    "dbname": "mydb",
    "otherParams": {"charset": "utf8mb4"}
  },
  "dbType": "MYSQL",
  "observabilityEnabled": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "mcp-server-001"
}
```

### 代理服务器

#### createProxyServer

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | HTTP | 代理服务器类型。目前仅支持 HTTP 。 |
| name | string | body | 否 | my-proxy- server | 代理服务器名称。 |
| version | string | body | 否 | v1 | 代理服务器版本。更新时必填。 |
| serverAddress | string | body | 否 | 192.168.1.10 0 | 代理服务器地址，可以是IP或域名。 |
| serverPort | integer | body | 否 | 8080 | 代理服务器端口。 |
| connectTimeou t | integer | body | 否 | 1200 | 连接超时时间 （毫秒），默认 1200。 |

|  |  | my-proxy- | 代 |
|---|---|---|---|
|  | server |  |  |

|  |  | 192.168.1.10 |  |
|---|---|---|---|
|  | 0 |  |  |

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | proxy-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "type": "type_value",
  "name": "name_value",
  "version": "version_value",
  "serverAddress": "serverAddress_value",
  "serverPort": 0,
  "connectTimeout": 0,
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteProxyServer

智能体工厂 OpenTrek

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| proxyServerId | string | body | 是 | proxy- server-001 | proxyServerId 参数。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | proxy- | pro |
|---|---|---|---|
|  | server-001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | proxy-server-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "proxyServerId": "proxyServerId_value"
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getProxyServer

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| proxyServerId | string | body | 是 | proxy-001 | 代理服务器ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |

智能体工厂 OpenTrek

| data.type | string | HTTP | 代理服务器类型。目前仅支持 HTTP 。 |
|---|---|---|---|
| data.name | string | my-proxy-server | 代理服务器名称。 |
| data.version | string | v1 | 代理服务器版本。 |
| data.serverAddress | string | 192.168.1.100 | 代理服务器地址。 |
| data.serverPort | integer | 8080 | 代理服务器端口。 |
| data.connectTimeout | integer | 1200 | 连接超时时间（毫秒）。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "proxyServerId": "proxyServerId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "type": "type_value",
        "name": "name_value",
        "version": "version_value",
        "serverAddress": "serverAddress_value",
        "serverPort": 0,
        "connectTimeout": 0
    }
}
```

#### ListProxyServers

**API 接口概述**

智能体工厂 OpenTrek
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.total | integer | 2 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ProxyServer[] | [] | 记录列表。 |

智能体工厂 OpenTrek

| data.records.type | string | HTTP | 代理服务器类型。目前仅支持 HTTP 。 |
|---|---|---|---|
| data.records.name | string | proxy-server-001 | Proxy server name。 |
| data.records.version | string | v1.0 | Proxy server version. Required when updating。 |
| data.records.serverAddr ess | string | 192.168.1.100 | Proxy server address, can be IP or domain name。 |
| data.records.serverPort | integer | 8080 | Proxy server port。 |
| data.records.connectTim eout | integer | 1200 | Proxy server connect timeout in milliseconds, default is 1200。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "total": 0,
        "current": 0,
        "size": 0,
        "records": {
            "type": "type_value",
            "name": "name_value",
            "version": "version_value",
            "serverAddress": "serverAddress_value",
            "serverPort": 0,
            "connectTimeout": 0
        }
    }
}
```

#### updateProxyServer

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | HTTP | 代理服务器类型。目前仅支持 HTTP 。 |
| name | string | body | 否 | my-proxy | Proxy server name。 |
| version | string | body | 否 | v1.0 | Proxy server version. Required when updating。 |

智能体工厂 OpenTrek

| serverAddress | string | body | 否 | 192.168.1.10 0 | Proxy server address, can be IP or domain name。 |
|---|---|---|---|---|---|
| serverPort | integer | body | 否 | 8080 | Proxy server port。 |
| connectTimeou t | integer | body | 否 | 1200 | Proxy server connect timeout in milliseconds, default is 1200。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | 192.168.1.10 |  |
|---|---|---|---|
|  | 0 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | my-proxy | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "type": "type_value",
  "name": "name_value",
  "version": "version_value",
  "serverAddress": "serverAddress_value",
  "serverPort": 0,
  "connectTimeout": 0,
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 服务来源

#### batchDeleteSource

**API 接口概述**

**中文名称：**批量删除来源
**功能概述：**来源管理 - 批量删除来源。
**请求方式：** `POST`
**说明**：此接口用于批量删除多个服务来源配置。

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|---|
| sourceIds | array<string > | body |  | 是 |  |  | ["source- |  |  |
|  |  |  |  |  |  |  |  | ["source- |  |
|  |  |  |  |  |  |  | 001", |  |  |
|  |  |  |  |  |  |  |  |  | 要删除 |
|  |  |  |  |  | 是 |  |  |  |  |
|  |  |  |  |  |  |  | "source- |  |  |
|  |  |  |  |  |  |  | 002"] |  |  |

|  |  | array<string |  |
|---|---|---|---|
| rceIds | > |  |  |

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
|---|---|---|---|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | 见下方。 | 批量删除结果。 |
| data.successIds | array<string> | ["source-001"] | 成功删除的 ID 列表。 |
| data.failedIds | array<string> | ["source-002"] | 删除失败的 ID 列表。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "sourceIds": ["source-001", "source-002", "source-003"],
  "gwInstanceId": "higress-001"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "successIds": ["source-001", "source-003"],
    "failedIds": ["source-002"]
  }
}
```

#### createSource

**API 接口概述**

**中文名称：**创建来源
**功能概述：**来源管理 - 创建来源。
**请求方式：** `POST`
**说明**：此接口用于注册新的服务来源（如 Nacos、EDAS、Eureka 等），支持 Higress 整合多种服务发现机制。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | string | body | 否 | source- 001 | 来源 ID，通常用于导入场景。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
| sourceName | string | body | 是 | my-nacos | 来源名称，唯一标识该来源。 |
| host | string | body | 否 | nacos.exampl e.com | 注册中心地址。 |
| port | integer | body | 否 | 8848 | 注册中心端口。 |
| username | string | body | 否 | nacos | 注册中心用户名。 |
| password | string | body | 否 | nacos123 | 注册中心密码。 |

|  |  | source- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

| nacos.exampl | 注册 |
|---|---|

智能体工厂 OpenTrek

| description | string | body | 否 | Nacos 服务发现 | 备注说明。 |
|---|---|---|---|---|---|
| sourceType | integer | body | 是 | 1 | 来源类型，见下方枚举说明。 |
| sourceStruct | object | body | 是 | 见下方示例 | 来源详细配置， 根据 sourceType 不同结构不同。 |

|  |  | Nacos 服务发 |  |
|---|---|---|---|
|  | 现 |  |  |

**sourceType 枚举值**

| 值 | 类型名称 | 说明 |
|---|---|---|
| 1 | Nacos | Nacos 服务发现，支持阿里云 MSE Nacos 和开源 Nacos。 |
| 2 | EDAS | EDAS 服务发现，支持阿里云 EDAS。 |
| 3 | Eureka | Eureka 服务发现。 |
| 4 | K8s | Kubernetes 服务发现。 |
| 7 | 固定节点 | 固定 IP 地址节点。 |

**sourceStruct 结构说明**

**Nacos 来源配置（sourceType = 1）**

| 参数名称 | 类型 |  | 是否必选 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| nacosRegistry | string |  | 是 |  | Nacos 注册中心地址，如 mse- |  |  |
|  |  |  |  |  |  | mse- |  |
|  |  |  |  |  | xxx.nacos.mse.aliyuncs |  |  |
|  |  |  |  |  | .com:8848 |  |  |
| checkType | integer |  | 是 |  | 鉴权类型：0=阿里云 AK/SK 鉴权，1=简易用户名密码鉴权。 |  |  |
| nacosAccessKey | string |  | 否 |  | 阿里云 AccessKey（checkType= 0 时必填）。 |  |  |

智能体工厂 OpenTrek

| nacosSecretKey | string | 否 | 阿里云 SecretKey（checkType= 0 时必填）。 |
|---|---|---|---|

**示例**：

```json
{
  "nacosRegistry": "mse-xxx.nacos.mse.aliyuncs.com:8848",
  "checkType": 0,
  "nacosAccessKey": "AK_xxx",
  "nacosSecretKey": "SK_xxx"
}
```

**EDAS 来源配置（sourceType = 2）**

| 参数名称 | 类型 | 是否必选 | 说明 |
|---|---|---|---|
| type | integer | 是 | 注册类型： 0=Nacos，1=ConfigServ er。 |
| edasNameSpaceId | string | 是 | EDAS 命名空间 ID。 |
| edasServerAddr | string | 否 | 服务器地址。 |
| edasEndPoint | string | 否 | 端点地址。 |
| edasEndPointPort | integer | 否 | 端点端口。 |
| edasAccessKey | string | 否 | 阿里云 AccessKey。 |
| edasSecretKey | string | 否 | 阿里云 SecretKey。 |

**示例**：

```json
{
  "type": 0,
  "edasNameSpaceId": "namespace-001",
  "edasServerAddr": "edas-server.aliyuncs.com",
  "edasAccessKey": "AK_xxx",
  "edasSecretKey": "SK_xxx"
}
```

**Eureka 来源配置（sourceType = 3）**

| 参数名称 | 类型 | 是否必选 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| eurekaRegistry | string | 是 | Eureka 注册中心地址。 |
|---|---|---|---|

**示例**：

```json
{
  "eurekaRegistry": "eureka.example.com:8761"
}
```

**K8s 来源配置（sourceType = 4）**

| 参数名称 | 类型 | 是否必选 | 说明 |
|---|---|---|---|
| k8sConfig | string | 是 | KubeConfig 内容 （Base64 编码）。 |

**示例**：

```json
{
  "k8sConfig": "base64-encoded-kubeconfig"
}
```

**固定节点配置（sourceType = 7）**

| 参数名称 | 类型 | 是否必选 | 说明 |
|---|---|---|---|
| nodes | array | 是 | 节点列表。 |
| nodes[].ip | string | 是 | IP 地址。 |
| nodes[].port | integer | 是 | 端口。 |
| nodes[].weight | integer | 否 | 权重，默认 1。 |
| nodes[].enable | boolean | 否 | 是否启用，默认 true。 |
| nodes[].vpcId | string | 否 | VPC ID（VPC 场景）。 |
| nodes[].vpcMappingIp | string | 否 | VPC 映射 IP。 |
| nodes[].vpcMappingPort | integer | 否 | VPC 映射端口。 |

**示例**：
智能体工厂 OpenTrek

```json
{
  "nodes": [
    {
      "ip": "192.168.1.1",
      "port": 8080,
      "weight": 1,
      "enable": true
    },
    {
      "ip": "192.168.1.2",
      "port": 8080,
      "weight": 1,
      "enable": true
    }
```

]

```
}
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | source-001 | 创建成功的来源 ID。 |

**示例**

**请求示例 - 创建 Nacos 来源**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "sourceName": "my-nacos",
  "sourceType": 1,
  "description": "Nacos 服务发现",
  "sourceStruct": {
    "nacosRegistry": "mse-xxx.nacos.mse.aliyuncs.com:8848",
    "checkType": 0,
    "nacosAccessKey": "AK_xxx",
    "nacosSecretKey": "SK_xxx"
  }
}
```

**请求示例 - 创建固定节点来源**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "sourceName": "fixed-backend",
  "sourceType": 7,
```

`"description": "`固定后端服务`",`

```json
  "sourceStruct": {
    "nodes": [
      {
        "ip": "192.168.1.1",
        "port": 8080,
        "weight": 1,
        "enable": true
      },
      {
        "ip": "192.168.1.2",
        "port": 8080,
        "weight": 1,
        "enable": true
      }
```

]

```
  }
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "source-001"
}
```

#### deleteSource

**API 接口概述**

**中文名称：**删除来源
**功能概述：**来源管理 - 删除来源。
**请求方式：** `POST`
**说明**：此接口用于删除指定的服务来源配置。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | string | body | 是 | source- 001 | 要删除的来源 ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |

|  |  | source- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | source-001 | 已删除的来源 ID。 |

智能体工厂 OpenTrek

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "sourceId": "source-001",
  "gwInstanceId": "higress-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "source-001"
}
```

#### getSource

**API 接口概述**

**中文名称：**查询来源详情
**功能概述：**来源管理 - 查询来源详情。
**请求方式：** `POST`
**说明**：此接口用于获取单个服务来源的详细配置信息。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | string | body | 是 | source- 001 | 来源唯一标识。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |

|  |  | source- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | 见下方。 | 来源详情。 |
| data.sourceId | string | source-001 | 来源唯一标识。 |
| data.sourceName | string | my-nacos | 来源名称。 |
| data.sourceType | integer | 1 | 来源类型代码。 |
| data.sourceTypeName | string | Nacos | 来源类型名称。 |
| data.sourceStruct | object | {} | 来源详细配置对象。 |
| data.description | string | Nacos 服务发现 | 描述信息。 |
| data.createTime | string | 2024-01- 01T00:00:00 | 创建时间。 |
| data.updateTime | string | 2024-01- 01T00:00:00 | 更新时间。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "sourceId": "source-001",
  "gwInstanceId": "higress-001"
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "sourceId": "source-001",
    "sourceName": "my-nacos",
    "sourceType": 1,
    "sourceTypeName": "Nacos",
    "sourceStruct": {
      "nacosRegistry": "mse-xxx.nacos.mse.aliyuncs.com:8848",
      "checkType": 0,
      "nacosAccessKey": "AK_xxx",
      "nacosSecretKey": "SK_xxx"
    },
    "description": "Nacos 服务发现",
    "createTime": "2024-01-01T00:00:00",
    "updateTime": "2024-01-01T00:00:00"
  }
}
```

#### listAllNamespaces

**API 接口概述**

**中文名称：**获取所有命名空间
**功能概述：**来源管理 - 查询来源下的命名空间列表。
**请求方式：** `POST`
**说明**：此接口用于查询指定服务来源（如 Nacos、EDAS）下的命名空间列表，主要用于服务发现场景。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
| sourceId | string | body | 是 | source- 001 | 来源唯一标识。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | source- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | array | [] | 命名空间列表。 |
| data[].namespaceId | string | namespace-001 | 命名空间 ID。 |
| data[].namespaceName | string | 生产环境 | 命名空间展示名称。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "sourceId": "source-001"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": [
    {
      "namespaceId": "public",
```

`"namespaceName": "`公共命名空间"

```json
    },
    {
      "namespaceId": "namespace-001",
```

`"namespaceName": "`生产环境"

```json
    },
    {
      "namespaceId": "namespace-002",
```

`"namespaceName": "`测试环境"

```
    }
```

]

```
}
```

#### listAllSources

**API 接口概述**

**中文名称：**获取所有来源
**功能概述：**来源管理 - 全量查询来源列表。
**请求方式：** `POST`
**说明**：此接口用于全量查询指定网关实例下的所有服务来源（不分页）。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
| serviceType | integer | body | 否 | 1 | 服务类型过滤。 |
| isDisasterReco very | boolean | body | 否 | false | 是否容灾来源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | array | [] | 来源列表。 |
| data[].sourceId | string | source-001 | 来源 ID。 |
| data[].sourceName | string | my-nacos | 来源名称。 |
| data[].sourceType | integer | 1 | 类型代码。 |
| data[].sourceTypeName | string | Nacos | 类型名称。 |
| data[].description | string | Nacos 服务发现 | 描述信息。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": [
    {
      "sourceId": "source-001",
      "sourceName": "my-nacos",
      "sourceType": 1,
      "sourceTypeName": "Nacos",
```

`"description": "Nacos` 服务发现"

```json
    },
    {
      "sourceId": "source-002",
      "sourceName": "my-eureka",
      "sourceType": 3,
      "sourceTypeName": "Eureka",
      "description": "Eureka 服务发现"
    }
```

]

```
}
```

#### listSources

**API 接口概述**

**中文名称：**查询来源列表
**功能概述：**来源管理 - 分页查询来源列表。
**请求方式：** `POST`
**说明**：此接口用于分页查询指定网关实例下的服务来源列表。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| size | integer | body | 是 | 10 | 每页大小。 |
| sourceId | string | body | 否 | source- 001 | 来源 ID 精确检索。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | source- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| sourceName | string | body | 否 | nacos | 来源名称模糊检索。 |
|---|---|---|---|---|---|
| orgPathId | string | body | 否 | org-001 | 组织路径 ID。 |
| resourceType | string | body | 否 | Nacos | 资源类型过滤。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | 见下方。 | 分页响应。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总记录数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | array | [] | 记录列表。 |
| data.records[].sourceId | string | source-001 | 来源 ID。 |
| data.records[].sourceNa me | string | my-nacos | 来源名称。 |
| data.records[].sourceTyp e | integer | 1 | 类型代码。 |
| data.records[].sourceTyp eName | string | Nacos | 类型名称。 |
| data.records[].descriptio n | string | Nacos 服务发现 | 描述信息。 |

智能体工厂 OpenTrek

| data.records[].createTim e | string | 2024-01- 01T00:00:00 | 创建时间。 |
|---|---|---|---|
| data.records[].updateTi me | string | 2024-01- 01T00:00:00 | 更新时间。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "current": 1,
  "size": 10,
  "sourceName": "nacos"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "size": 10,
    "total": 2,
    "current": 1,
    "records": [
      {
        "sourceId": "source-001",
        "sourceName": "my-nacos",
        "sourceType": 1,
        "sourceTypeName": "Nacos",
        "description": "Nacos 服务发现",
        "createTime": "2024-01-01T00:00:00",
        "updateTime": "2024-01-01T00:00:00"
      },
      {
        "sourceId": "source-002",
        "sourceName": "my-nacos-backup",
        "sourceType": 1,
        "sourceTypeName": "Nacos",
        "description": "备用 Nacos",
        "createTime": "2024-01-02T00:00:00",
        "updateTime": "2024-01-02T00:00:00"
      }
```

]

```
  }
}
```

#### modifySource

**API 接口概述**

**中文名称：**修改来源
**功能概述：**来源管理 - 修改来源。
**请求方式：** `POST`
**说明**：此接口用于修改现有的服务来源配置。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceId | string | body | 是 | source- 001 | 来源唯一标识。 |

|  |  | source- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例唯一标识。 |
|---|---|---|---|---|---|
| sourceName | string | body | 否 | my-nacos- updated | 来源名称。 |
| sourceStruct | object | body | 否 | 见下方示例 | 来源详细配置。 |
| description | string | body | 否 | 更新后的 Nacos 配置 | 备注说明。 |
| sourceType | integer | body | 否 | 1 | 来源类型。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-nacos- | 来源 |
|---|---|---|---|
|  | updated |  |  |

|  |  | 更新后的 | 备注 |
|---|---|---|---|
|  | Nacos 配置 |  |  |

**说明**： `sourceStruct` 的结构请参考createSource接口文档中的 `sourceStruct` 结构说明。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | source-001 | 已修改的来源 ID。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "sourceId": "source-001",
  "gwInstanceId": "higress-001",
  "sourceName": "my-nacos-updated",
```

`"description": "`更新后的 `Nacos` 配置`",`

```json
  "sourceStruct": {
    "nacosRegistry": "mse-new.nacos.mse.aliyuncs.com:8848",
    "checkType": 0,
    "nacosAccessKey": "AK_new",
    "nacosSecretKey": "SK_new"
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "source-001"
}
```

### 插件

#### createCustomWasmPlugin

**API 接口概述**

**中文名称：**创建自定义WASM插件
**功能概述：**插件管理 - 创建自定义WASM插件。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

|  | pluginName |  |  | string |  | body |  |  |  | 是 |  |  | my-custom- plugin |  | 插件名称。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | category |  |  | string |  | body |  |  |  | 否 |  |  | auth |  | 插件分类。 |  |
|  | title |  |  | string |  | body |  |  |  | 是 |  |  | 自定义认证插件 |  | 插件显示标题。 |  |
|  | description |  |  | string |  | body |  |  |  | 是 |  |  | 用于API请求认证的自定义插件 |  | 插件显示描述。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | 用于API请求认 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 证的自定义插 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 件 |  |  |  |
|  | imageRepositor y |  |  | string |  | body |  |  |  | 是 |  |  | registry.exa |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | registry.exa |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | mple.com/my- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 插件 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | plugin |  |  |  |
|  | imagePullPolicy |  |  | string |  | body |  |  |  | 是 |  |  | IfNotPresent |  | 插件镜像拉取策略。 |  |
|  | imagePullSecre t |  |  | string |  | body |  |  |  | 否 |  |  | my-secret |  | 插件镜像拉取密钥。 |  |
|  | phase |  |  | string (枚 |  | body |  |  |  | 是 |  |  | AUTH |  | 执行阶段。 |  |
|  |  |  |  |  | string (枚 |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 举: |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hase |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | PluginPhase) |  |  |  |  |  |  |  |  |  |  |  |  |
|  | priority |  |  | integer |  | body |  |  |  | 是 |  |  | 100 |  | 插件执行优先级。 |  |
|  | example |  |  | string |  | body |  |  |  | 否 |  |  | {"timeout":3 0} |  | 配置示例。 |  |
|  | document |  |  | string |  | body |  |  |  | 否 |  |  | https://docs |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | https://docs |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | .example.com/ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 插件文 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | plugin |  |  |  |

|  |  | my-custom- | 插件 |
|---|---|---|---|
|  | plugin |  |  |

|  |  | 自定义认证插 |
|---|---|---|
|  | 件 |  |

|  |  | IfNotPresent |
|---|---|---|

|  |  | {"timeout":3 | 配 |
|---|---|---|---|
|  | 0} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

| msg | string | success | 响应消息。 |
|---|---|---|---|
| message | string | success | 响应消息。 |
| data | string | my-custom-plugin | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "pluginName": "pluginName_value",
  "category": "category_value",
  "title": "title_value",
  "description": "description_value",
  "imageRepository": "imageRepository_value",
  "imagePullPolicy": "imagePullPolicy_value",
  "imagePullSecret": "imagePullSecret_value",
  "phase": "phase_value",
  "priority": 0,
  "example": "example_value",
  "document": "document_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteCustomWasmPlugin

**API 接口概述**

**中文名称：**删除自定义WASM插件
**功能概述：**插件管理 - 删除自定义WASM插件。
智能体工厂 OpenTrek
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| pluginName | string | body | 是 | my-custom- plugin | 插件名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-custom- | 插件 |
|---|---|---|---|
|  | plugin |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | my-custom-plugin | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "pluginName": "pluginName_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getCustomWasmPlugin

**API 接口概述**

**中文名称：**查询自定义WASM插件详情
**功能概述：**插件管理 - 查询自定义WASM插件详情。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| pluginName | string | body | 是 | my-custom- plugin | 插件名称。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-custom- | 插件 |
|---|---|---|---|
|  | plugin |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.pluginName | string | my-custom-plugin | 插件名称。 |

智能体工厂 OpenTrek

| data.category | string | auth | 插件分类。 |
|---|---|---|---|
| data.title | string | 自定义认证插件 | 插件显示标题。 |
| data.description | string | 用于API请求认证的自定义插件 | 插件显示描述。 |
| data.example | string | {"timeout":30} | 插件配置示例。 |
| data.document | string | https://docs.example .com/plugin | 插件文档链接。 |
| data.imageRepository | string | registry.example.com /my-plugin | 插件镜像仓库地址。 |
| data.imagePullPolicy | string | IfNotPresent | 插件镜像拉取策略。 |
| data.imagePullSecret | string | my-secret | 插件镜像拉取密钥。 |
| data.phase | string | AUTH | 插件执行阶段。 |
| data.priority | integer | 100 | 插件执行优先级。 |
| data.gwInstanceId | string | higress-001 | 网关实例ID。 |

|  | 用于API请求认证的自定义 | 插 |
|---|---|---|
| 插件 |  |  |

|  | https://docs.example | 插件文档链接 |
|---|---|---|
| .com/plugin |  |  |

| registry.example.com | 插件镜像仓 |
|---|---|

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "pluginName": "pluginName_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "pluginName": "pluginName_value",
        "category": "category_value",
        "title": "title_value",
        "description": "description_value",
        "example": "example_value",
        "document": "document_value",
        "imageRepository": "imageRepository_value",
        "imagePullPolicy": "imagePullPolicy_value",
        "imagePullSecret": "imagePullSecret_value",
        "phase": "phase_value",
        "priority": 0,
        "gwInstanceId": "gwInstanceId_value"
    }
}
```

#### modifyCustomWasmPlugin

**API 接口概述**

**中文名称：**修改自定义WASM插件
**功能概述：**插件管理 - 编辑自定义WASM插件。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| pluginName | string | body | 是 | my-custom- plugin | 插件名称。 |
| category | string | body | 否 | auth | 插件分类。 |
| title | string | body | 是 | 自定义认证插件 | 插件显示标题。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-custom- | 插件 |
|---|---|---|---|
|  | plugin |  |  |

|  |  | 自定义认证插 |
|---|---|---|
|  | 件 |  |

智能体工厂 OpenTrek

|  | description |  |  | string |  | body |  |  |  |  |  |  |  | 用于自定义认 |  | 插件显示描述。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 用于自定义认 |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | 证逻辑的WASM插 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 是 |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | 件 |  |  |  |
|  | imageRepositor y |  |  | string |  | body |  |  |  | 是 |  |  |  | registry.exa |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | registry.exa | 插件镜像仓库地 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | mple.com/plug |  | 插件镜像 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 址。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | ins/auth |  |  |  |
|  | imagePullPolicy |  |  | string |  | body |  |  |  | 是 |  |  |  | IfNotPresent |  | 插件镜像拉取策略。 |  |
|  | imagePullSecre t |  |  | string |  | body |  |  |  | 否 |  |  |  | docker- |  | 插件镜像拉取密钥。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | docker- | 插件镜像拉 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | registry- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | secret |  |  |  |
|  | phase |  |  | string (枚 |  | body |  |  |  | 是 |  |  |  | AUTHN |  | 执行阶段。 |  |
|  |  |  |  |  | string (枚 |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | 举: |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | hase |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | PluginPhase) |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | priority |  |  | integer |  | body |  |  |  | 是 |  |  |  | 100 |  | 插件在指定阶段中的执行优先级。 |  |
|  | example |  |  | string |  | body |  |  |  | 否 |  |  |  | {"rules": |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"rules": |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key": |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 配置示 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | "header"}]} |  |  |  |
|  | document |  |  | string |  | body |  |  |  | 否 |  |  |  | https://docs |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | https://docs |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | .example.com/ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 插件文 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | plugin |  |  |  |
|  | version |  |  | string |  | body |  |  |  | 否 |  |  |  | 1.0.0 |  | 版本号。 |  |

|  |  | IfNotPresent |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | string | my-custom-plugin | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "pluginName": "my-custom-plugin",
  "category": "auth",
```

`"title": "`自定义认证插件`",` `"description": "`用于自定义认证逻辑的`WASM`插件`",`

```json
  "imageRepository": "registry.example.com/plugins/auth",
  "imagePullPolicy": "IfNotPresent",
  "imagePullSecret": "docker-registry-secret",
  "phase": "AUTHN",
  "priority": 100,
  "example": "{\"rules\": [{\"key\": \"header\"}]}",
  "document": "https://docs.example.com/plugin",
  "version": "1.0.0"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "my-custom-plugin"
}
```

### 消费者

#### batchCreateAppAuthByRoute

**API 接口概述**

**中文名称：**批量创建消费者授权
**功能概述：**应用授权管理 - 批量创建应用授权与认证绑定（支持 grantType）。
智能体工厂 OpenTrek

```
请求路径： /applicationauth/batchCreateAppAuthByRoute
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body |  | 是 |  | higress- 001 |  | 网关实例ID。 |
| appId | string | body |  | 是 |  | app-001 |  | 应用ID。 |
| routeId | string[] | body |  | 否 |  | ["route- |  | 路由ID列表。 |
|  |  |  |  |  |  |  | ["route- |  |
|  |  |  |  |  |  | 001", "route- |  |  |
|  |  |  |  |  |  |  |  | 路由 |
|  |  |  |  |  |  | 002"] |  |  |
| authStatus | integer | body |  | 是 |  | 1 |  | 授权状态。 |
| isDisasterReco very | boolean | body |  | 否 |  | false |  | 是否为容灾资源。 |
| grantType | string | body |  | 否 |  | route |  | 授权类型。 |
| grantTargetIds | string[] | body |  | 否 |  | ["route- |  | 授权目标ID列表。 |
|  |  |  |  |  |  |  | ["route- | 授权目标ID列 |
|  |  |  |  |  |  | 001", "route- |  | 授权 |
|  |  |  |  |  |  |  |  | 表。 |
|  |  |  |  |  |  | 002"] |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | success | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /applicationauth/batchCreateAppAuthByRoute HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "appId": "appId_value",
  "routeId": [],
  "authStatus": 0,
  "isDisasterRecovery": true,
  "grantType": "grantType_value",
  "grantTargetIds": []
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### batchDeleteApp

**API 接口概述**

**中文名称：**批量删除消费者
**功能概述：**消费者管理 - 批量删除消费者。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appIds | string[] | body | 是 | ["app-001", "app-002"] | 应用ID列表。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | ["app-001", | 应用ID列表 |
|---|---|---|---|
|  | "app-002"] |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.successIds | string[] | ["app-001"] | 成功删除的应用ID列表。 |
| data.failedIds | string[] | ["app-002"] | 删除失败的应用ID列表。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "appIds": [],
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "successIds": [],
        "failedIds": []
    }
}
```

#### createAppAuthByRoute

**API 接口概述**

智能体工厂 OpenTrek
**中文名称：**创建消费者授权
**功能概述：**应用授权管理 - 创建应用授权与认证绑定（支持 grantType）。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| appId | string | body | 是 | app-001 | 应用ID。 |
| authId | string | body | 否 | auth-001 | 授权ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |
| authStatus | integer | body | 是 | 1 | 授权状态。 |
| isStop | boolean | body | 否 | false | 是否停止。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| grantType | string | body | 否 | route | 授权类型。 |
| grantTargetId | string | body | 否 | route-001 | 授权目标ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |

智能体工厂 OpenTrek

| data | string | auth-001 | 响应数据。 |
|---|---|---|---|

**示例**

**请求示例**

```json
POST /applicationauth/createAppAuthByRoute HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "appId": "appId_value",
  "authId": "authId_value",
  "routeId": "routeId_value",
  "authStatus": 0,
  "isStop": true,
  "isDisasterRecovery": true,
  "grantType": "grantType_value",
  "grantTargetId": "grantTargetId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### createConsumer

**API 接口概述**

**中文名称：**创建消费者
**功能概述：**消费者管理 - 创建消费者。
**请求路径：** `/application/createApp`
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| key | string |  | body |  |  |  | 是 |  | api-key- 001 |  | Key Auth认证时的Key。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| payload | object |  | body |  |  |  |  |  | {"subject": |  |  |  |
|  |  |  |  |  |  |  |  |  |  | {"subject": | JWT认证时的 |  |
|  |  |  |  |  |  |  |  |  | "user-001", |  |  |  |
|  |  |  |  | body |  |  |  |  |  |  | payload配置 |  |
|  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | "issuer": |  | （包含 |  |
|  |  |  |  |  |  |  |  |  | "my-app"} |  |  |  |
| oauth2Payload | object |  | body |  |  |  | 否 |  | {"clientId": |  | OAuth2认证时的配置。 |  |
|  |  |  |  |  |  |  |  |  |  | {"clientId": | OAuth2认证时 |  |
|  |  |  |  |  |  |  |  |  | "client- |  |  |  |
|  |  |  |  |  |  |  |  |  | 001"} |  |  |  |
| password | string |  | body |  |  |  | 否 |  | password123 |  | Basic Auth认证时的密码。 |  |
| expireTime | integer |  | body |  |  |  | 否 |  | 3600 |  | 过期时间。 |  |
| appSecret | string |  | body |  |  |  | 否 |  | secret- abc123 |  | 应用Secret。 |  |
| requestHeader | string |  | body |  |  |  | 否 |  | X-Custom- Header |  | 认证请求头名称。 |  |
| token | string |  | body |  |  |  | 否 |  | token- xyz789 |  | Token。 |  |
| useAuth | boolean |  | body |  |  |  | 否 |  | true |  | 是否启用认证。 |  |
| appId | string |  | body |  |  |  | 否 |  | app-001 |  | 应用ID。 |  |
| authType | integer |  | body |  |  |  | 是 |  | 1 |  | 认证类型。 0 =无认证， 1 =Key Auth， 2 =B asic Auth， 3 =J WT， 4 =OA uth2。 |  |
| useWhiteList | boolean |  | body |  |  |  | 否 |  | false |  | 是否启用IP白名单。 |  |
| ipWhiteList | string |  | body |  |  |  | 否 |  | 192.168.1.0/ 24,10.0.0.1 |  | IP白名单，逗号分隔。 |  |

|  |  | api-key- |
|---|---|---|
|  | 001 |  |

|  | password123 |
|---|---|

|  |  | secret- |  |
|---|---|---|---|
|  | abc123 |  |  |

|  |  | X-Custom- | 认 |
|---|---|---|---|
|  | Header |  |  |

|  |  | token- |
|---|---|---|
|  | xyz789 |  |

|  | 3 |
|---|---|
| 4 |  |

|  |  | 192.168.1.0/ | IP白名单，逗 |
|---|---|---|---|
|  | 24,10.0.0.1 |  |  |

智能体工厂 OpenTrek

| appName | string | body | 是 | my- consumer | 消费者名称。 |
|---|---|---|---|---|---|
| description | string | body | 否 | 测试消费者 | 消费者描述。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| userId | string | body | 否 | user-001 | 用户ID。 |
| userName | string | body | 否 | admin | 用户名。 |
| appKey | string | body | 否 | app-key- 001 | 应用Key。 |
| groups | string[] | body | 否 | ["group- 001"] | 消费者分组列表。 |
| appCode | string | body | 否 | APP001 | 应用Code。 |
| accessKey | string | body | 否 | AK xxx _ | AccessKey。 |
| secretKey | string | body | 否 | SK xxx _ | SecretKey。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| apiKeyLocation Type | string | body | 否 | HEADER | API Key位置类型。可选值： HEADER （放在请求头中）、 QUERY （放在查询参数中）、 BEARER （Bearer Token认证）。 |
| keyName | string | body | 否 | X-API-Key | Key名称。 |

|  |  | my- |
|---|---|---|
|  | consumer |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | app-key- |
|---|---|---|
|  | 001 |  |

|  |  | ["group- |  |
|---|---|---|---|
|  | 001"] |  |  |

**payload 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| subject | string | body | 否 | user-001 | JWT Subject标识。 |
|---|---|---|---|---|---|
| issuer | string | body | 否 | my-app | JWT Issuer签发者。 |

**oauth2Payload 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|
| scopes | string | body | 否 |  | read,write |  | OAuth2授权范围。 |
| authorizationC ode | boolean | body | 否 |  | true |  | 是否启用授权码模式。 |
| clientCredentia ls | boolean | body | 否 |  | false |  | 是否启用客户端凭证模式。 |
| implicitGrant | boolean | body | 否 |  | false |  | 是否启用隐式授权模式。 |
| passwordGrant | boolean | body | 否 |  | false |  | 是否启用密码模式。 |
| tokenExpiratio n | integer | body | 否 |  | 3600 |  | Token过期时间 （秒）。 |
| refreshTokenEx piration | integer | body | 否 |  | 86400 |  | Refresh Token 过期时间 （秒）。 |
| clientId | string | body | 否 |  | client- 001 |  | OAuth2客户端 ID。 |
| clientSecret | string | body | 否 |  | secret- abc123 |  | OAuth2客户端 Secret。 |
| redirectUris | string | body | 否 |  | https://exam |  |  |
|  |  |  |  |  |  | https://exam | OAuth2回调地 |
|  |  |  |  |  | ple.com/callb |  | O |
|  |  |  |  |  |  |  | 址 |
|  |  |  |  |  | ack |  |  |
| pkce | boolean | body | 否 |  | true |  | 是否启用PKCE。 |

|  |  | read,write |
|---|---|---|

|  |  | client- |
|---|---|---|
|  | 001 |  |

|  |  | secret- |  |
|---|---|---|---|
|  | abc123 |  |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | app-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /application/createApp HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "key": "key_value",
  "payload": {
    "subject": "subject_value",
    "issuer": "issuer_value"
  },
  "oauth2Payload": {
    "scopes": "scopes_value",
    "authorizationCode": true,
    "clientCredentials": true,
    "implicitGrant": true,
    "passwordGrant": true,
    "tokenExpiration": 0,
    "refreshTokenExpiration": 0,
    "clientId": "clientId_value",
    "clientSecret": "clientSecret_value",
    "redirectUris": "redirectUris_value",
    "pkce": true
  },
  "password": "password_value",
  "expireTime": 0,
  "appSecret": "appSecret_value",
  "requestHeader": "requestHeader_value",
  "token": "token_value",
  "useAuth": true,
  "appId": "appId_value",
  "authType": 0,
  "useWhiteList": true,
  "ipWhiteList": "ipWhiteList_value",
  "appName": "appName_value",
  "description": "description_value",
  "gwInstanceId": "gwInstanceId_value",
  "userId": "userId_value",
  "userName": "userName_value",
  "appKey": "appKey_value",
  "groups": [],
  "appCode": "appCode_value",
  "accessKey": "accessKey_value",
  "secretKey": "secretKey_value",
  "isDisasterRecovery": true,
  "apiKeyLocationType": "apiKeyLocationType_value",
  "keyName": "keyName_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteApp

**API 接口概述**

**中文名称：**删除消费者
**功能概述：**消费者管理 - 删除消费者。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | string | body | 是 | app-001 | 应用ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | app-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "appId": "appId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteAppAuth

**API 接口概述**

**中文名称：**删除消费者授权
**功能概述：**消费者管理 - 删除消费者授权。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| authId | string | body | 是 | auth-001 | 授权ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| isStop | boolean | body | 否 | false | 是否停止。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | auth-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "authId": "authId_value",
  "gwInstanceId": "gwInstanceId_value",
  "isStop": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getApp

**API 接口概述**

**中文名称：**查询消费者详情
**功能概述：**消费者管理 - 根据 AppId 获取消费者详情。
**请求方式：** `POST`

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| appId | string | body | 是 | app-001 | 应用ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.appId | string | app-001 | 应用ID。 |
| data.appName | string | my-app | 应用名称。 |
| data.useAuth | boolean | true | 是否启用认证。 |
| data.authType | integer | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT，4=OAuth 2。 |
| data.requestHeader | string | X-API-Key | 认证请求头名称。 |
| data.authTypeName | string | Key Auth | 认证类型名称。 |
| data.ipWhiteList | string | 192.168.1.0/24 | IP白名单。 |
| data.useWhiteList | boolean | false | 是否启用IP白名单。 |

智能体工厂 OpenTrek

| data.description | string | 测试应用 | 描述信息。 |
|---|---|---|---|
| data.appTags | object[] | [{"key":"env","value ":"prod"}] | 应用标签列表。 |
| data.token | string | eyJhbGciOiJIUzI1NiIs ... | Token。 |
| data.appSecret | string | secret-xxx-xxx | 应用Secret。 |
| data.isDisable | boolean | false | 是否禁用。 |
| data.payload | object | - | JWT Payload配置。 |
| data.payload.subject | string | my-subject | JWT Subject。 |
| data.payload.issuer | string | my-issuer | JWT Issuer。 |
| data.oauth2Payload | object | - | OAuth2配置。 |
| data.oauth2Payload.scop es | string | read,write | OAuth2授权范围。 |
| data.oauth2Payload.auth orizationCode | boolean | true | 是否启用授权码模式。 |
| data.oauth2Payload.clien tCredentials | boolean | false | 是否启用客户端凭证模式。 |
| data.oauth2Payload.impl icitGrant | boolean | false | 是否启用隐式授权模式。 |
| data.oauth2Payload.pass wordGrant | boolean | false | 是否启用密码模式。 |
| data.oauth2Payload.toke nExpiration | integer | 3600 | Token过期时间（秒）。 |
| data.oauth2Payload.refre shTokenExpiration | integer | 7200 | Refresh Token过期时间 （秒）。 |
| data.oauth2Payload.clien tId | string | client-001 | OAuth2客户端ID。 |

| [{"key":"env","value | 应用标签列 |
|---|---|

|  | eyJhbGciOiJIUzI1NiIs | To |
|---|---|---|
| ... |  |  |

智能体工厂 OpenTrek

| data.oauth2Payload.clien tSecret | string | secret-xxx | OAuth2客户端Secret。 |
|---|---|---|---|
| data.oauth2Payload.redir ectUris | string | https://example.com/ callback | OAuth2回调地址。 |
| data.oauth2Payload.pkce | boolean | false | 是否启用PKCE。 |
| data.enable | boolean | true | 是否启用。 |
| data.key | string | api-key-xxx | 键名。 |
| data.password | string | password123 | 密码。 |
| data.expireTime | integer | 3600 | 过期时间（秒）。 |
| data.groups | string[] | ["group-001"] | 分组列表。 |
| data.strategyConfigs | StrategyConfigRelati on[] | - | 策略配置列表。 |
| data.strategyConfigs.stra tegyConfigId | string | strategy-001 | 策略配置ID。 |
| data.strategyConfigs.stra tegyConfigName | string | my-strategy | 策略配置名称。 |
| data.strategyConfigs.stra tegyName | string | rate-limit | 策略名称。 |
| data.strategyConfigs.stat us | boolean | true | 状态。 |
| data.strategyConfigs.sco pes | string[] | ["read","write"] | OAuth2授权范围。 |
| data.strategyConfigs.sco pe | object | - | 策略作用域配置。 |
| data.strategyConfigs.sco pe.routeInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 路由信息列表。 |
| data.strategyConfigs.sco pe.routeInfos.name | string | my-route | 路由名称。 |

|  | https://example.com/ | OAuth2 |
|---|---|---|
| callback |  |  |

|  |  | StrategyConfigRelati | - |  |
|---|---|---|---|---|
|  |  |  |  | - |
| a.strategyConfigs | on[] |  |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| routeInfos | TO$ScopeTargetDTO[] |  |  |

智能体工厂 OpenTrek

| data.strategyConfigs.sco pe.routeInfos.id | string | route-001 | 路由ID。 |
|---|---|---|---|
| data.strategyConfigs.sco pe.serviceInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 服务信息列表。 |
| data.strategyConfigs.sco pe.serviceInfos.name | string | my-service | 服务名称。 |
| data.strategyConfigs.sco pe.serviceInfos.id | string | service-001 | 服务ID。 |
| data.strategyConfigs.sco pe.appInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 应用信息列表。 |
| data.strategyConfigs.sco pe.appInfos.name | string | my-app | 应用名称。 |
| data.strategyConfigs.sco pe.appInfos.id | string | app-001 | 应用ID。 |
| data.strategyConfigs.sco pe.domainInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 域名信息列表。 |
| data.strategyConfigs.sco pe.domainInfos.name | string | api.example.com | 域名名称。 |
| data.strategyConfigs.sco pe.domainInfos.id | string | domain-001 | 域名ID。 |
| data.strategyConfigs.sco pe.mcpServerInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | MCP服务器信息列表。 |
| data.strategyConfigs.sco pe.mcpServerInfos.name | string | my-mcp-server | MCP服务器名称。 |
| data.strategyConfigs.sco pe.mcpServerInfos.id | string | mcp-001 | MCP服务器ID。 |
| data.strategyConfigs.sco pe.scopes | string[] | ["read","write"] | OAuth2授权范围。 |
| data.strategyConfigs.cre ateTime | string | 2024-01-01 10:00:00 | 创建时间。 |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| serviceInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| appInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| domainInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| mcpServerInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

智能体工厂 OpenTrek

| data.strategyConfigs.upd ateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
|---|---|---|---|
| data.appCode | string | APP001 | 应用Code。 |
| data.accessKey | string | AK-xxx-xxx | AccessKey。 |
| data.secretKey | string | SK-xxx-xxx | SecretKey。 |
| data.apiKeyLocationType | string | HEADER | API Key位置类型。 |
| data.keyName | string | X-API-Key | Key名称。 |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "appId": "appId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "appId": "appId_value",
        "appName": "appName_value",
        "useAuth": true,
        "authType": 0,
        "requestHeader": "requestHeader_value",
        "authTypeName": "authTypeName_value",
        "ipWhiteList": "ipWhiteList_value",
        "useWhiteList": true,
        "description": "description_value",
        "appTags": [],
        "token": "token_value",
        "appSecret": "appSecret_value",
        "isDisable": true,
        "payload": {
            "subject": "subject_value",
"issuer":"issuervalue"
```

智能体工厂 OpenTrek

```json
            issuer: issuer_value
        },
        "oauth2Payload": {
            "scopes": "scopes_value",
            "authorizationCode": true,
            "clientCredentials": true,
            "implicitGrant": true,
            "passwordGrant": true,
            "tokenExpiration": 0,
            "refreshTokenExpiration": 0,
            "clientId": "clientId_value",
            "clientSecret": "clientSecret_value",
            "redirectUris": "redirectUris_value",
            "pkce": true
        },
        "enable": true,
        "key": "key_value",
        "password": "password_value",
        "expireTime": 0,
        "groups": [],
        "strategyConfigs": {
            "strategyConfigId": "strategyConfigId_value",
            "strategyConfigName": "strategyConfigName_value",
            "strategyName": "strategyName_value",
            "status": true,
            "scopes": [],
            "scope": {
                "routeInfos": {
                    "name": {},
                    "id": {}
                },
                "serviceInfos": {
                    "name": {},
                    "id": {}
                },
                "appInfos": {
                    "name": {},
                    "id": {}
                },
                "domainInfos": {
                    "name": {},
                    "id": {}
                },
                "mcpServerInfos": {
                    "name": {},
                    "id": {}
                },
                "scopes": []
            },
            "createTime": "createTime_value",
            "updateTime": "updateTime_value"
        },
        "appCode": "appCode_value",
        "accessKey": "accessKey_value",
        "secretKey": "secretKey_value",
        "apiKeyLocationType": "apiKeyLocationType_value",
        "keyName": "keyName_value"
    }
}
```

智能体工厂 OpenTrek

#### getAppAuth

**API 接口概述**

**中文名称：**查询消费者授权详情
**功能概述：**消费者管理 - 查询认证信息。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| authId | string | body | 是 | auth-001 | 授权ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.authId | integer | 1001 | 授权ID。 |
| data.appId | string | app-001 | 应用ID。 |
| data.routeId | string | route-001 | 路由ID。 |
| data.routePath | string | /api/v1/test | 路由路径。 |

智能体工厂 OpenTrek

| data.serviceId | integer | 2001 | 服务ID。 |
|---|---|---|---|
| data.serviceName | string | my-service | 服务名称。 |
| data.serviceProtocol | string | HTTP | 服务协议。 |
| data.authStatus | integer | 1 | 授权状态。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "authId": "authId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "authId": 0,
        "appId": "appId_value",
        "routeId": "routeId_value",
        "routePath": "routePath_value",
        "serviceId": 0,
        "serviceName": "serviceName_value",
        "serviceProtocol": "serviceProtocol_value",
        "authStatus": 0
    }
}
```

#### listApps

**API 接口概述**

**中文名称：**查询消费者列表
**功能概述：**消费者管理 - 分页查询消费者。
智能体工厂 OpenTrek
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| isShareInstanc e | boolean | body | 否 | false | 是否共享实例。 |
| regionId | string | body | 否 | cn- hangzhou | 地域ID。 |
| resourceGroupI d | integer | body | 否 | 1 | 资源组ID。 |
| orgPathId | string | body | 否 | org-001 | 组织路径ID。 |
| resourceType | string | body | 否 | gateway | 资源类型。 |
| appId | string | body | 否 | app-001 | 应用ID。 |
| appName | string | body | 否 | my-app | 应用名称。 |
| appTags | string | body | 否 | tag1,tag2 | 应用标签。 |
| authType | string | body | 否 | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT， 4=OAuth2。 |
| userId | string | body | 否 | user-001 | 用户ID。 |
| userName | string | body | 否 | admin | 用户名。 |
| email | string | body | 否 | admin@exampl e.com | 用户邮箱。 |

|  |  | cn- |
|---|---|---|
|  | hangzhou |  |

|  | e.com |
|---|---|

智能体工厂 OpenTrek

| status | integer | body | 否 | 1 | 状态。 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| appType | integer | body | 否 | 1 | 应用类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | AppResponse[] | - | 记录列表。 |
| data.records.appId | string | app-001 | 应用ID。 |
| data.records.appName | string | my-app | 应用名称。 |
| data.records.appAddress | string | 192.168.1.100:8080 | 应用地址。 |

智能体工厂 OpenTrek

| data.records.appTags | object[] | [{"key":"env","value ":"prod"}] | 应用标签列表。 |
|---|---|---|---|
| data.records.useAuth | boolean | true | 是否启用认证。 |
| data.records.authType | integer | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT，4=OAuth 2。 |
| data.records.authTypeNa me | string | Key Auth | 认证类型名称。 |
| data.records.useWhiteLis t | boolean | false | 是否启用IP白名单。 |
| data.records.ipWhiteList | string[] | ["192.168.1.0/24"] | IP白名单。 |
| data.records.description | string | 测试应用 | 描述信息。 |
| data.records.chargePers onName | string | 张三 | 负责人姓名。 |
| data.records.createBy | integer | 1001 | 创建者ID。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.records.updateBy | integer | 1001 | 更新者ID。 |
| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.records.userId | string | user-001 | 用户ID。 |
| data.records.userName | string | admin | 用户名。 |
| data.records.delFlag | string | 0 | 删除标记。 |
| data.records.isDisable | boolean | false | 是否禁用。 |

|  | [{"key":"env","value |  |
|---|---|---|
| ":"prod"}] |  |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

智能体工厂 OpenTrek

| data.records.enable | boolean | true | 是否启用。 |
|---|---|---|---|
| data.records.groups | string[] | ["group-001"] | 分组列表。 |
| data.records.credentials | array | [] | 凭证列表。 |
| data.records.timeOut | boolean | false | 是否超时。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "isShareInstance": true,
  "regionId": "regionId_value",
  "resourceGroupId": 0,
  "orgPathId": "orgPathId_value",
  "resourceType": "resourceType_value",
  "appId": "appId_value",
  "appName": "appName_value",
  "appTags": "appTags_value",
  "authType": "authType_value",
  "userId": "userId_value",
  "userName": "userName_value",
  "email": "email_value",
  "status": 0,
  "gwInstanceId": "gwInstanceId_value",
  "appType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "total": 0,
        "current": 0,
        "size": 0,
        "records": {
            "appId": "appId_value",
            "appName": "appName_value",
            "appAddress": "appAddress_value",
            "appTags": [],
            "useAuth": true,
            "authType": 0,
            "authTypeName": "authTypeName_value",
            "useWhiteList": true,
            "ipWhiteList": [],
            "description": "description_value",
            "chargePersonName": "chargePersonName_value",
            "createBy": 0,
            "createTime": "createTime_value",
            "updateBy": 0,
            "updateTime": "updateTime_value",
            "userId": "userId_value",
            "userName": "userName_value",
            "delFlag": "delFlag_value",
            "isDisable": true,
            "enable": true,
            "groups": [],
            "credentials": [],
            "timeOut": true
        }
    }
}
```

#### listAppsByGwInstanceId

**API 接口概述**

**中文名称：**按实例查询消费者
**功能概述：**消费者管理 - 根据网关实例查询消费者列表。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | AppDetailResponse[] | - | 响应数据。 |
| data.appId | string | app-001 | 应用ID。 |
| data.appName | string | my-app | 应用名称。 |
| data.useAuth | boolean | true | 是否启用认证。 |
| data.authType | integer | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT，4=OAuth 2。 |
| data.requestHeader | string | X-API-Key | 认证请求头名称。 |
| data.authTypeName | string | Key Auth | 认证类型名称。 |
| data.ipWhiteList | string | 192.168.1.0/24 | IP白名单。 |

|  |  | AppDetailResponse[] |
|---|---|---|

智能体工厂 OpenTrek

| data.useWhiteList | boolean | false | 是否启用IP白名单。 |
|---|---|---|---|
| data.description | string | 测试应用 | 描述信息。 |
| data.appTags | object[] | [{"key":"env","value ":"prod"}] | 应用标签列表。 |
| data.token | string | eyJhbGciOiJIUzI1NiIs ... | Token。 |
| data.appSecret | string | secret-xxx-xxx | 应用Secret。 |
| data.isDisable | boolean | false | 是否禁用。 |
| data.payload | object | - | JWT Payload配置。 |
| data.payload.subject | string | my-subject | JWT Subject。 |
| data.payload.issuer | string | my-issuer | JWT Issuer。 |
| data.oauth2Payload | object | - | OAuth2配置。 |
| data.oauth2Payload.scop es | string | read,write | OAuth2授权范围。 |
| data.oauth2Payload.auth orizationCode | boolean | true | 是否启用授权码模式。 |
| data.oauth2Payload.clien tCredentials | boolean | false | 是否启用客户端凭证模式。 |
| data.oauth2Payload.impl icitGrant | boolean | false | 是否启用隐式授权模式。 |
| data.oauth2Payload.pass wordGrant | boolean | false | 是否启用密码模式。 |
| data.oauth2Payload.toke nExpiration | integer | 3600 | Token过期时间（秒）。 |
| data.oauth2Payload.refre shTokenExpiration | integer | 7200 | Refresh Token过期时间 （秒）。 |

| [{"key":"env","value | 应用标签列 |
|---|---|

|  | eyJhbGciOiJIUzI1NiIs | To |
|---|---|---|
| ... |  |  |

智能体工厂 OpenTrek

| data.oauth2Payload.clien tId | string | client-001 | OAuth2客户端ID。 |
|---|---|---|---|
| data.oauth2Payload.clien tSecret | string | secret-xxx | OAuth2客户端Secret。 |
| data.oauth2Payload.redir ectUris | string | https://example.com/ callback | OAuth2回调地址。 |
| data.oauth2Payload.pkce | boolean | false | 是否启用PKCE。 |
| data.enable | boolean | true | 是否启用。 |
| data.key | string | api-key-xxx | 键名。 |
| data.password | string | password123 | 密码。 |
| data.expireTime | integer | 3600 | 过期时间（秒）。 |
| data.groups | string[] | ["group-001"] | 分组列表。 |
| data.strategyConfigs | StrategyConfigRelati on[] | - | 策略配置列表。 |
| data.strategyConfigs.stra tegyConfigId | string | strategy-001 | 策略配置ID。 |
| data.strategyConfigs.stra tegyConfigName | string | my-strategy | 策略配置名称。 |
| data.strategyConfigs.stra tegyName | string | rate-limit | 策略名称。 |
| data.strategyConfigs.stat us | boolean | true | 状态。 |
| data.strategyConfigs.sco pes | string[] | ["read","write"] | OAuth2授权范围。 |
| data.strategyConfigs.sco pe | object | - | 策略作用域配置。 |
| data.strategyConfigs.sco pe.routeInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 路由信息列表。 |

|  | https://example.com/ | OAuth2 |
|---|---|---|
| callback |  |  |

|  |  | StrategyConfigRelati | - |  |
|---|---|---|---|---|
|  |  |  |  | - |
| a.strategyConfigs | on[] |  |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| routeInfos | TO$ScopeTargetDTO[] |  |  |

智能体工厂 OpenTrek

| data.strategyConfigs.sco pe.routeInfos.name | string | my-route | 路由名称。 |
|---|---|---|---|
| data.strategyConfigs.sco pe.routeInfos.id | string | route-001 | 路由ID。 |
| data.strategyConfigs.sco pe.serviceInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 服务信息列表。 |
| data.strategyConfigs.sco pe.serviceInfos.name | string | my-service | 服务名称。 |
| data.strategyConfigs.sco pe.serviceInfos.id | string | service-001 | 服务ID。 |
| data.strategyConfigs.sco pe.appInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 应用信息列表。 |
| data.strategyConfigs.sco pe.appInfos.name | string | my-app | 应用名称。 |
| data.strategyConfigs.sco pe.appInfos.id | string | app-001 | 应用ID。 |
| data.strategyConfigs.sco pe.domainInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | 域名信息列表。 |
| data.strategyConfigs.sco pe.domainInfos.name | string | api.example.com | 域名名称。 |
| data.strategyConfigs.sco pe.domainInfos.id | string | domain-001 | 域名ID。 |
| data.strategyConfigs.sco pe.mcpServerInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | - | MCP服务器信息列表。 |
| data.strategyConfigs.sco pe.mcpServerInfos.name | string | my-mcp-server | MCP服务器名称。 |
| data.strategyConfigs.sco pe.mcpServerInfos.id | string | mcp-001 | MCP服务器ID。 |
| data.strategyConfigs.sco pe.scopes | string[] | ["read","write"] | OAuth2授权范围。 |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| serviceInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| appInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| domainInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | - |
|---|---|---|---|
| mcpServerInfos | TO$ScopeTargetDTO[] |  |  |

智能体工厂 OpenTrek

| data.strategyConfigs.cre ateTime | string | 2024-01-01 10:00:00 | 创建时间。 |
|---|---|---|---|
| data.strategyConfigs.upd ateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.appCode | string | APP001 | 应用Code。 |
| data.accessKey | string | AK-xxx-xxx | AccessKey。 |
| data.secretKey | string | SK-xxx-xxx | SecretKey。 |
| data.apiKeyLocationType | string | HEADER | API Key位置类型。 |
| data.keyName | string | X-API-Key | Key名称。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
POST /application/listAppsByGwInstanceId HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "appId": "appId_value",
        "appName": "appName_value",
        "useAuth": true,
        "authType": 0,
        "requestHeader": "requestHeader_value",
        "authTypeName": "authTypeName_value",
        "ipWhiteList": "ipWhiteList_value",
        "useWhiteList": true,
        "description": "description_value",
        "appTags": [],
"token":"tokenvalue"
```

智能体工厂 OpenTrek

```json
        token: token_value,
        "appSecret": "appSecret_value",
        "isDisable": true,
        "payload": {
            "subject": "subject_value",
            "issuer": "issuer_value"
        },
        "oauth2Payload": {
            "scopes": "scopes_value",
            "authorizationCode": true,
            "clientCredentials": true,
            "implicitGrant": true,
            "passwordGrant": true,
            "tokenExpiration": 0,
            "refreshTokenExpiration": 0,
            "clientId": "clientId_value",
            "clientSecret": "clientSecret_value",
            "redirectUris": "redirectUris_value",
            "pkce": true
        },
        "enable": true,
        "key": "key_value",
        "password": "password_value",
        "expireTime": 0,
        "groups": [],
        "strategyConfigs": {
            "strategyConfigId": "strategyConfigId_value",
            "strategyConfigName": "strategyConfigName_value",
            "strategyName": "strategyName_value",
            "status": true,
            "scopes": [],
            "scope": {
                "routeInfos": {
                    "name": {},
                    "id": {}
                },
                "serviceInfos": {
                    "name": {},
                    "id": {}
                },
                "appInfos": {
                    "name": {},
                    "id": {}
                },
                "domainInfos": {
                    "name": {},
                    "id": {}
                },
                "mcpServerInfos": {
                    "name": {},
                    "id": {}
                },
                "scopes": []
            },
            "createTime": "createTime_value",
            "updateTime": "updateTime_value"
        },
        "appCode": "appCode_value",
        "accessKey": "accessKey_value",
```

智能体工厂 OpenTrek

```json
        "secretKey": "secretKey_value",
        "apiKeyLocationType": "apiKeyLocationType_value",
        "keyName": "keyName_value"
    }
}
```

#### listMcpServersByAppId

**API 接口概述**

**中文名称：**查询消费者关联MCP服务
**功能概述：**消费者管理 - 查询 MCP 服务器列表。

```
请求路径： /applicationauth/listMcpServersByAppId
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| total | integer | body | 否 | 100 | 总数。 |
| routeName | string | body | 否 | my-mcp- server | MCP服务器名称。 |
| routeId | string | body | 否 | mcp-001 | MCP服务器ID。 |
| appId | string | body | 否 | app-001 | 应用ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| grantType | string | body | 否 | mcpServer | 授权类型。 |

| my-mcp- |  |
|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | ListRoutesByAppIdRes ponseRecord[] | - | 记录列表。 |
| data.records.routeId | string | mcp-001 | MCP服务器ID。 |
| data.records.routeName | string | my-mcp-server | MCP服务器名称。 |
| data.records.routePath | string | /mcp/v1/tools | MCP路径。 |
| data.records.serviceId | string | service-001 | 服务ID。 |
| data.records.serviceNam e | string | my-service | 服务名称。 |
| data.records.serviceProt ocol | string | HTTP | 服务协议。 |
| data.records.authId | string | auth-001 | 授权ID。 |
| data.records.authStatus | integer | 1 | 授权状态。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |

|  |  | ListRoutesByAppIdRes | - |
|---|---|---|---|
| a.records | ponseRecord[] |  |  |

智能体工厂 OpenTrek

| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
|---|---|---|---|
| data.records.targetId | string | mcp-001 | 目标ID。 |
| data.records.targetName | string | my-mcp-server | 目标名称。 |

**示例**

**请求示例**

```json
POST /applicationauth/listMcpServersByAppId HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "total": 0,
  "routeName": "routeName_value",
  "routeId": "routeId_value",
  "appId": "appId_value",
  "gwInstanceId": "gwInstanceId_value",
  "isDisasterRecovery": true,
  "grantType": "grantType_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "size": 0,
        "total": 0,
        "current": 0,
        "records": {
            "routeId": "routeId_value",
            "routeName": "routeName_value",
            "routePath": "routePath_value",
            "serviceId": "serviceId_value",
            "serviceName": "serviceName_value",
            "serviceProtocol": "serviceProtocol_value",
            "authId": "authId_value",
            "authStatus": 0,
            "createTime": "createTime_value",
            "updateTime": "updateTime_value",
            "targetId": "targetId_value",
            "targetName": "targetName_value"
        }
    }
}
```

#### listModelApisByAppId

**API 接口概述**

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| total | integer | body | 否 | 100 | 总数。 |

智能体工厂 OpenTrek

| routeName | string | body | 否 | my-model- api | 模型API名称。 |
|---|---|---|---|---|---|
| routeId | string | body | 否 | model-api- 001 | 模型API ID。 |
| appId | string | body | 否 | app-001 | 应用ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| grantType | string | body | 否 | modelApi | 授权类型。 |

|  |  | my-model- |
|---|---|---|
|  | api |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | ListRoutesByAppIdRes ponseRecord[] | - | 记录列表。 |
| data.records.routeId | string | model-api-001 | 模型API ID。 |

|  |  | ListRoutesByAppIdRes | - |
|---|---|---|---|
| a.records | ponseRecord[] |  |  |

智能体工厂 OpenTrek

| data.records.routeName | string | my-model-api | 模型API名称。 |
|---|---|---|---|
| data.records.routePath | string | /api/v1/chat | 模型API路径。 |
| data.records.serviceId | string | service-001 | 服务ID。 |
| data.records.serviceNam e | string | my-service | 服务名称。 |
| data.records.serviceProt ocol | string | HTTP | 服务协议。 |
| data.records.authId | string | auth-001 | 授权ID。 |
| data.records.authStatus | integer | 1 | 授权状态。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.records.targetId | string | model-api-001 | 目标ID。 |
| data.records.targetName | string | my-model-api | 目标名称。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
POST /applicationauth/listModelApisByAppId HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "total": 0,
  "routeName": "routeName_value",
  "routeId": "routeId_value",
  "appId": "appId_value",
  "gwInstanceId": "gwInstanceId_value",
  "isDisasterRecovery": true,
  "grantType": "grantType_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "size": 0,
        "total": 0,
        "current": 0,
        "records": {
            "routeId": "routeId_value",
            "routeName": "routeName_value",
            "routePath": "routePath_value",
            "serviceId": "serviceId_value",
            "serviceName": "serviceName_value",
            "serviceProtocol": "serviceProtocol_value",
            "authId": "authId_value",
            "authStatus": 0,
            "createTime": "createTime_value",
            "updateTime": "updateTime_value",
            "targetId": "targetId_value",
            "targetName": "targetName_value"
        }
    }
}
```

#### listRoutesByAppId

**API 接口概述**

**中文名称：**查询消费者关联路由
**功能概述：**消费者管理 - 查询路由列表。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| total | integer | body | 否 | 100 | 总数。 |
| routeName | string | body | 否 | my-route | 路由名称。 |

智能体工厂 OpenTrek

| routeId | string | body | 否 | route-001 | 路由ID。 |
|---|---|---|---|---|---|
| appId | string | body | 否 | app-001 | 应用ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| grantType | string | body | 否 | route | 授权类型。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | ListRoutesByAppIdRes ponseRecord[] | - | 记录列表。 |
| data.records.routeId | string | route-001 | 路由ID。 |
| data.records.routeName | string | my-route | 路由名称。 |
| data.records.routePath | string | /api/v1/test | 路由路径。 |

|  |  | ListRoutesByAppIdRes | - |
|---|---|---|---|
| a.records | ponseRecord[] |  |  |

智能体工厂 OpenTrek

| data.records.serviceId | string | service-001 | 服务ID。 |
|---|---|---|---|
| data.records.serviceNam e | string | my-service | 服务名称。 |
| data.records.serviceProt ocol | string | HTTP | 服务协议。 |
| data.records.authId | string | auth-001 | 授权ID。 |
| data.records.authStatus | integer | 1 | 授权状态。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.records.targetId | string | route-001 | 目标ID。 |
| data.records.targetName | string | my-route | 目标名称。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
POST /applicationauth/listRoutesByAppId HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "total": 0,
  "routeName": "routeName_value",
  "routeId": "routeId_value",
  "appId": "appId_value",
  "gwInstanceId": "gwInstanceId_value",
  "isDisasterRecovery": true,
  "grantType": "grantType_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "size": 0,
        "total": 0,
        "current": 0,
        "records": {
            "routeId": "routeId_value",
            "routeName": "routeName_value",
            "routePath": "routePath_value",
            "serviceId": "serviceId_value",
            "serviceName": "serviceName_value",
            "serviceProtocol": "serviceProtocol_value",
            "authId": "authId_value",
            "authStatus": 0,
            "createTime": "createTime_value",
            "updateTime": "updateTime_value",
            "targetId": "targetId_value",
            "targetName": "targetName_value"
        }
    }
}
```

#### listRoutesByGwInstanceId

**API 接口概述**

**中文名称：**按实例查询路由列表
**功能概述：**消费者管理 - 根据网关实例获取路由列表。

```
请求路径： /applicationauth/listRoutesByGwInstanceId
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | GetRouteListByGwInst anceIdResponse[] | - | 响应数据。 |
| data.routeId | string | route-001 | 路由ID。 |
| data.routeName | string | my-route | 路由名称。 |
| data.routePath | string | /api/v1/test | 路由路径。 |
| data.serviceId | string | service-001 | 服务ID。 |
| data.serviceName | string | my-service | 服务名称。 |
| data.serviceProtocol | string | HTTP | 服务协议。 |
| data.isDisasterRecovery | boolean | false | 是否为容灾资源。 |

|  |  | GetRouteListByGwInst | - |
|---|---|---|---|
| a | anceIdResponse[] |  |  |

**示例**

**请求示例**

```json
POST /applicationauth/listRoutesByGwInstanceId HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "routeId": "routeId_value",
        "routeName": "routeName_value",
        "routePath": "routePath_value",
        "serviceId": "serviceId_value",
        "serviceName": "serviceName_value",
        "serviceProtocol": "serviceProtocol_value",
        "isDisasterRecovery": true
    }
} }
```

#### modifyApp

**API 接口概述**

**中文名称：**修改消费者
**功能概述：**消费者管理 - 编辑消费者。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 是 | api-key- xxx | 键名。 |
| payload | object | body | 否 | - | JWT Payload配置。 |
| oauth2Payload | object | body | 否 | - | OAuth2配置。 |
| password | string | body | 否 | password123 | 密码。 |
| expireTime | integer | body | 否 | 3600 | 过期时间 （秒）。 |
| appSecret | string | body | 否 | secret-xxx- xxx | 应用Secret。 |

|  |  | api-key- |
|---|---|---|
|  | xxx |  |

|  |  | password123 |
|---|---|---|

|  |  | secret-xxx- |  |
|---|---|---|---|
|  | xxx |  |  |

智能体工厂 OpenTrek

| requestHeader | string | body | 否 | X-API-Key | 认证请求头名称。 |
|---|---|---|---|---|---|
| token | string | body | 否 | eyJhbGciOiJI UzI1NiIs... | Token。 |
| useAuth | boolean | body | 否 | true | 是否启用认证。 |
| appId | string | body | 否 | app-001 | 应用ID。 |
| authType | integer | body | 是 | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT， 4=OAuth2。 |
| useWhiteList | boolean | body | 否 | false | 是否启用IP白名单。 |
| ipWhiteList | string | body | 否 | 192.168.1.0/ 24 | IP白名单。 |
| appName | string | body | 是 | my-app | 应用名称。 |
| description | string | body | 否 | 测试应用 | 描述信息。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| userId | string | body | 否 | user-001 | 用户ID。 |
| userName | string | body | 否 | admin | 用户名。 |
| appKey | string | body | 否 | app-key- xxx | 应用Key。 |
| groups | string[] | body | 否 | ["group- 001"] | 分组列表。 |
| appCode | string | body | 否 | APP001 | 应用Code。 |
| accessKey | string | body | 否 | AK-xxx- xxx | AccessKey。 |

|  |  | eyJhbGciOiJI | Token。 |
|---|---|---|---|
|  | UzI1NiIs... |  |  |

| 192.168.1.0/ | I |
|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | app-key- |
|---|---|---|
|  | xxx |  |

| ["group- |  |
|---|---|

|  |  | AK-xxx- |
|---|---|---|
|  | xxx |  |

智能体工厂 OpenTrek

| secretKey | string | body |  | 否 |  | SK-xxx- xxx |  | SecretKey。 |
|---|---|---|---|---|---|---|---|---|
| isDisasterReco very | boolean | body |  | 否 |  | false |  | 是否为容灾资源。 |
| apiKeyLocation Type | string | body |  | 否 |  | HEADER |  | API Key位置类型。可选值： HEADER （放在请求头中）、 QUERY （放在查询参数中）、 BEARER （Bearer Token认证）。 |
| keyName | string | body |  | 否 |  | X-API-Key |  | Key名称。 |
| appAddress | string | body |  | 否 |  | 192.168.1.10 0:8080 |  | 应用地址。 |
| appTagsStr | string | body |  | 否 |  | env:prod,typ e:api |  | 应用标签字符串。 |
| chargePersonN ame | string | body |  | 否 |  | 张三 |  | 负责人姓名。 |
| openCross | boolean | body |  | 否 |  | false |  | 是否启用跨域。 |
| allowedOrigins | string | body |  | 否 |  | https://exam ple.com |  | 允许的跨域来源。 |
| allowedHeader s | string | body |  | 否 |  | Content- |  | 允许的请求头。 |
|  |  |  |  |  |  |  | Content- |  |
|  |  |  |  |  |  | Type,X-API- |  |  |
|  |  |  |  |  |  | Key |  |  |
| allowedMethod s | string | body |  | 否 |  | GET,POST,PUT ,DELETE |  | 允许的请求方法。 |
| isDisable | boolean | body |  | 否 |  | false |  | 是否禁用。 |
| appType | integer | body |  | 否 |  | 1 |  | 应用类型。 |

|  |  | SK-xxx- |
|---|---|---|
|  | xxx |  |

| 192.168.1.10 | 应用地 |
|---|---|

|  |  | env:prod,typ | 应用 |
|---|---|---|---|
|  | e:api |  |  |

|  |  | https://exam | 允许的跨 |
|---|---|---|---|
|  | ple.com |  |  |

|  |  | GET,POST,PUT | 允许的请 |
|---|---|---|---|
|  | ,DELETE |  |  |

**payload 对象结构**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| subject | string | body | 否 | my- subject | JWT Subject。 |
| issuer | string | body | 否 | my-issuer | JWT Issuer。 |

|  |  | my- |
|---|---|---|
|  | subject |  |

**oauth2Payload 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|
| scopes | string | body | 否 |  | read,write |  | OAuth2授权范围。 |
| authorizationC ode | boolean | body | 否 |  | true |  | 是否启用授权码模式。 |
| clientCredentia ls | boolean | body | 否 |  | false |  | 是否启用客户端凭证模式。 |
| implicitGrant | boolean | body | 否 |  | false |  | 是否启用隐式授权模式。 |
| passwordGrant | boolean | body | 否 |  | false |  | 是否启用密码模式。 |
| tokenExpiratio n | integer | body | 否 |  | 3600 |  | Token过期时间 （秒）。 |
| refreshTokenEx piration | integer | body | 否 |  | 7200 |  | Refresh Token 过期时间 （秒）。 |
| clientId | string | body | 否 |  | client- 001 |  | OAuth2客户端 ID。 |
| clientSecret | string | body | 否 |  | secret- xxx |  | OAuth2客户端 Secret。 |
| redirectUris | string | body | 否 |  | https://exam |  |  |
|  |  |  |  |  |  | https://exam | OAuth2回调地 |
|  |  |  |  |  | ple.com/callb |  | O |
|  |  |  |  |  |  |  | 址 |
|  |  |  |  |  | ack |  |  |
| pkce | boolean | body | 否 |  | false |  | 是否启用PKCE。 |

|  |  | read,write |
|---|---|---|

|  |  | client- |
|---|---|---|
|  | 001 |  |

|  |  | secret- |
|---|---|---|
|  | xxx |  |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | app-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "key": "key_value",
  "payload": {
    "subject": "subject_value",
    "issuer": "issuer_value"
  },
  "oauth2Payload": {
    "scopes": "scopes_value",
    "authorizationCode": true,
    "clientCredentials": true,
    "implicitGrant": true,
    "passwordGrant": true,
    "tokenExpiration": 0,
    "refreshTokenExpiration": 0,
    "clientId": "clientId_value",
    "clientSecret": "clientSecret_value",
    "redirectUris": "redirectUris_value",
    "pkce": true
  },
  "password": "password_value",
  "expireTime": 0,
  "appSecret": "appSecret_value",
  "requestHeader": "requestHeader_value",
  "token": "token_value",
  "useAuth": true,
  "appId": "appId_value",
  "authType": 0,
  "useWhiteList": true,
  "ipWhiteList": "ipWhiteList_value",
  "appName": "appName_value",
  "description": "description_value",
  "gwInstanceId": "gwInstanceId_value",
  "userId": "userId_value",
  "userName": "userName_value",
  "appKey": "appKey_value",
  "groups": [],
  "appCode": "appCode_value",
  "accessKey": "accessKey_value",
  "secretKey": "secretKey_value",
  "isDisasterRecovery": true,
  "apiKeyLocationType": "apiKeyLocationType_value",
  "keyName": "keyName_value",
  "appAddress": "appAddress_value",
  "appTagsStr": "appTagsStr_value",
  "chargePersonName": "chargePersonName_value",
  "openCross": true,
  "allowedOrigins": "allowedOrigins_value",
  "allowedHeaders": "allowedHeaders_value",
  "allowedMethods": "allowedMethods_value",
  "isDisable": true,
  "appType": 0
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### refreshToken

**API 接口概述**

**中文名称：**刷新消费者Token
**功能概述：**消费者管理 - 刷新 Token。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 是 | api-key- xxx | 键名。 |
| payload | object | body | 否 | - | JWT Payload配置。 |
| oauth2Payload | object | body | 否 | - | OAuth2配置。 |
| password | string | body | 否 | password123 | 密码。 |
| expireTime | integer | body | 否 | 3600 | 过期时间 （秒）。 |
| appSecret | string | body | 否 | secret-xxx- xxx | 应用Secret。 |
| requestHeader | string | body | 否 | X-API-Key | 认证请求头名称。 |

|  |  | api-key- |
|---|---|---|
|  | xxx |  |

|  |  | password123 |
|---|---|---|

|  |  | secret-xxx- | 应 |
|---|---|---|---|
|  | xxx |  |  |

智能体工厂 OpenTrek

| token | string | body | 否 | eyJhbGciOiJI UzI1NiIs... | Token。 |
|---|---|---|---|---|---|
| useAuth | boolean | body | 否 | true | 是否启用认证。 |
| appId | string | body | 否 | app-001 | 应用ID。 |
| authType | integer | body | 是 | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT， 4=OAuth2。 |
| useWhiteList | boolean | body | 否 | false | 是否启用IP白名单。 |
| ipWhiteList | string | body | 否 | 192.168.1.0/ 24 | IP白名单。 |
| appName | string | body | 是 | my-app | 应用名称。 |
| description | string | body | 否 | 测试应用 | 描述信息。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| userId | string | body | 否 | user-001 | 用户ID。 |
| userName | string | body | 否 | admin | 用户名。 |
| appKey | string | body | 否 | app-key- xxx | 应用Key。 |
| groups | string[] | body | 否 | ["group- 001"] | 分组列表。 |
| appCode | string | body | 否 | APP001 | 应用Code。 |
| accessKey | string | body | 否 | AK-xxx- xxx | AccessKey。 |
| secretKey | string | body | 否 | SK-xxx- xxx | SecretKey。 |

| eyJhbGciOiJI | Token。 |
|---|---|

| 192.168.1.0/ | I |
|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | app-key- |
|---|---|---|
|  | xxx |  |

| ["group- |  |
|---|---|

|  |  | AK-xxx- |
|---|---|---|
|  | xxx |  |

|  |  | SK-xxx- |
|---|---|---|
|  | xxx |  |

智能体工厂 OpenTrek

| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
|---|---|---|---|---|---|
| apiKeyLocation Type | string | body | 否 | HEADER | API Key位置类型。可选值： HEADER （放在请求头中）、 QUERY （放在查询参数中）、 BEARER （Bearer Token认证）。 |
| keyName | string | body | 否 | X-API-Key | Key名称。 |

**payload 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| subject | string | body | 否 | my- subject | JWT Subject。 |
| issuer | string | body | 否 | my-issuer | JWT Issuer。 |

|  |  | my- |
|---|---|---|
|  | subject |  |

**oauth2Payload 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| scopes | string | body | 否 | read,write | OAuth2授权范围。 |
| authorizationC ode | boolean | body | 否 | true | 是否启用授权码模式。 |
| clientCredentia ls | boolean | body | 否 | false | 是否启用客户端凭证模式。 |
| implicitGrant | boolean | body | 否 | false | 是否启用隐式授权模式。 |
| passwordGrant | boolean | body | 否 | false | 是否启用密码模式。 |
| tokenExpiratio n | integer | body | 否 | 3600 | Token过期时间 （秒）。 |

|  |  | read,write |
|---|---|---|

智能体工厂 OpenTrek

| refreshTokenEx piration | integer | body | 否 |  | 7200 |  | Refresh Token 过期时间 （秒）。 |
|---|---|---|---|---|---|---|---|
| clientId | string | body | 否 |  | client- 001 |  | OAuth2客户端 ID。 |
| clientSecret | string | body | 否 |  | secret- xxx |  | OAuth2客户端 Secret。 |
| redirectUris | string | body | 否 |  | https://exam |  |  |
|  |  |  |  |  |  | https://exam | OAuth2回调地 |
|  |  |  |  |  | ple.com/callb |  | O |
|  |  |  |  |  |  |  | 址 |
|  |  |  |  |  | ack |  |  |
| pkce | boolean | body | 否 |  | false |  | 是否启用PKCE。 |

|  |  | client- |
|---|---|---|
|  | 001 |  |

|  |  | secret- |
|---|---|---|
|  | xxx |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | eyJhbGciOiJIUzI1NiIs ... | 新Token。 |

|  | eyJhbGciOiJIUzI1NiIs | 新 |
|---|---|---|
| ... |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "key": "key_value",
  "payload": {
    "subject": "subject_value",
    "issuer": "issuer_value"
  },
  "oauth2Payload": {
    "scopes": "scopes_value",
    "authorizationCode": true,
    "clientCredentials": true,
    "implicitGrant": true,
    "passwordGrant": true,
    "tokenExpiration": 0,
    "refreshTokenExpiration": 0,
    "clientId": "clientId_value",
    "clientSecret": "clientSecret_value",
    "redirectUris": "redirectUris_value",
    "pkce": true
  },
  "password": "password_value",
  "expireTime": 0,
  "appSecret": "appSecret_value",
  "requestHeader": "requestHeader_value",
  "token": "token_value",
  "useAuth": true,
  "appId": "appId_value",
  "authType": 0,
  "useWhiteList": true,
  "ipWhiteList": "ipWhiteList_value",
  "appName": "appName_value",
  "description": "description_value",
  "gwInstanceId": "gwInstanceId_value",
  "userId": "userId_value",
  "userName": "userName_value",
  "appKey": "appKey_value",
  "groups": [],
  "appCode": "appCode_value",
  "accessKey": "accessKey_value",
  "secretKey": "secretKey_value",
  "isDisasterRecovery": true,
  "apiKeyLocationType": "apiKeyLocationType_value",
  "keyName": "keyName_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 域名

#### createDomain

**API 接口概述**

**中文名称：**创建域名
**功能概述：**创建域名。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | string | body | 否 | domain- 001 | 域名ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| protocol | string | body | 是 | HTTP | 协议类型。可选值： HTTP 、 HTTPS 。 |
| certificateId | string | body | 否 | cert-001 | HTTPS协议时需要的服务端证书 ID。HTTP协议时不需要。 |
| domain | string | body | 是 | api.example. com | 域名，长度不超过255字符。支持精确域名和通配符域名（如 *.example.com ）。 |

|  |  | domain- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  | HTTP |
|---|---|
| HTTPS |  |

|  | com |
|---|---|

智能体工厂 OpenTrek

| clientAuth | integer | body | 否 | 0 | 是否开启客户端认证。 0 =关闭， 1 =开启。仅HTTPS协议且非Higress引擎时生效。 |
|---|---|---|---|---|---|
| caCertificateId | string | body | 否 | ca-cert- 001 | 客户端认证开启时需要的CA证书 ID。 |
| subjectDn | string | body | 否 | X-Subject- Dn | Subject DN转发头。 |
| issuerDn | string | body | 否 | X-Issuer- Dn | Issuer DN转发头。 |

|  | 0 |
|---|---|
| 1 |  |

|  |  | ca-cert- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | domain-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "domainId": "domainId_value",
  "gwInstanceId": "gwInstanceId_value",
  "protocol": "protocol_value",
  "certificateId": "certificateId_value",
  "domain": "domain_value",
  "clientAuth": 0,
  "caCertificateId": "caCertificateId_value",
  "subjectDn": "subjectDn_value",
  "issuerDn": "issuerDn_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteDomain

**API 接口概述**

**中文名称：**删除域名
**功能概述：**删除域名。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| domainId | string | body | 是 | domain- 001 | 域名ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | domain- |
|---|---|---|
|  | 001 |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | domain-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "higress-001",
  "domainId": "domain-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "domain-001"
}
```

#### getDomain

**API 接口概述**

**中文名称：**查询域名详情
**功能概述：**查询域名详情。
**请求方式：** `POST`

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | string | body | 否 | domain- 001 | 域名ID。 |
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |

|  |  | domain- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.domainId | string | domain-001 | 域名ID。 |
| data.domain | string | api.example.com | 域名。 |
| data.protocol | string | HTTP | 协议类型。 |
| data.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.certificateId | string | cert-001 | 证书ID。 |
| data.clientAuth | integer | 0 | 是否开启客户端认证。 |
| data.caCertificateId | string | ca-cert-001 | CA证书ID。 |

智能体工厂 OpenTrek

| data.subjectDn | string | X-Subject-Dn | Subject DN转发头。 |
|---|---|---|---|
| data.issuerDn | string | X-Issuer-Dn | Issuer DN转发头。 |
| data.routeInfos | GetDomainResponse$Ro uteInfo[] | - | 路由信息列表。 |
| data.routeInfos.routeId | string | route-001 | 路由ID。 |
| data.routeInfos.routeNa me | string | my-route | 路由名称。 |
| data.routeInfos.serviceId | string | service-001 | 服务ID。 |
| data.routeInfos.serviceN ame | string | my-service | 服务名称。 |
| data.routeInfos.createTi me | string | 2024-01-01 10:00:00 | 创建时间。 |

|  |  | GetDomainResponse$Ro | - |
|---|---|---|---|
| a.routeInfos | uteInfo[] |  |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "domainId": "domainId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "domainId": "domainId_value",
        "domain": "domain_value",
        "protocol": "protocol_value",
        "createTime": "createTime_value",
        "updateTime": "updateTime_value",
        "certificateId": "certificateId_value",
        "clientAuth": 0,
        "caCertificateId": "caCertificateId_value",
        "subjectDn": "subjectDn_value",
        "issuerDn": "issuerDn_value",
        "routeInfos": {
            "routeId": "routeId_value",
            "routeName": "routeName_value",
            "serviceId": "serviceId_value",
            "serviceName": "serviceName_value",
            "createTime": "createTime_value"
        }
    }
}
```

#### listAllDomains

**API 接口概述**

**中文名称：**查询所有域名
**功能概述：**查询所有域名。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | ListDomainsResponseR ecord[] | - | 响应数据。 |
| data.domainId | string | domain-001 | 域名ID。 |
| data.certificateId | string | cert-001 | 证书ID。 |
| data.certificateName | string | my-cert | 证书名称。 |
| data.domain | string | api.example.com | 域名。 |
| data.protocol | string | HTTP | 协议类型。 |
| data.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.clientAuth | integer | 0 | 是否开启客户端认证。 |
| data.caCertificateId | string | ca-cert-001 | CA证书ID。 |
| data.caCertificateName | string | my-ca-cert | CA证书名称。 |

| ListDomainsResponseR | - |
|---|---|

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "domainId": "domainId_value",
        "certificateId": "certificateId_value",
        "certificateName": "certificateName_value",
        "domain": "domain_value",
        "protocol": "protocol_value",
        "createTime": "createTime_value",
        "updateTime": "updateTime_value",
        "clientAuth": 0,
        "caCertificateId": "caCertificateId_value",
        "caCertificateName": "caCertificateName_value"
    }
}
```

#### listDomains

**API 接口概述**

**中文名称：**查询域名列表
**功能概述：**查询域名列表。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |

智能体工厂 OpenTrek

| domain | string | body | 否 | api.example. com | 域名。 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | api.example. |  |
|---|---|---|---|
|  | com |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | ListDomainsResponseR ecord[] | - | 记录列表。 |
| data.records.domainId | string | domain-001 | 域名ID。 |
| data.records.certificateId | string | cert-001 | 证书ID。 |
| data.records.certificateN ame | string | my-cert | 证书名称。 |
| data.records.domain | string | api.example.com | 域名。 |
| data.records.protocol | string | HTTP | 协议类型。 |

| ListDomainsResponseR | - |
|---|---|

智能体工厂 OpenTrek

| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
|---|---|---|---|
| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.records.clientAuth | integer | 0 | 是否开启客户端认证。 |
| data.records.caCertificat eId | string | ca-cert-001 | CA证书ID。 |
| data.records.caCertificat eName | string | my-ca-cert | CA证书名称。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "domain": "domain_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": {
        "size": 0,
        "total": 0,
        "current": 0,
        "records": {
            "domainId": "domainId_value",
            "certificateId": "certificateId_value",
            "certificateName": "certificateName_value",
            "domain": "domain_value",
            "protocol": "protocol_value",
            "createTime": "createTime_value",
            "updateTime": "updateTime_value",
            "clientAuth": 0,
            "caCertificateId": "caCertificateId_value",
            "caCertificateName": "caCertificateName_value"
        }
    }
}
```

#### updateDomain

**API 接口概述**

**中文名称：**修改域名
**功能概述：**修改域名。
**请求路径：** `/domain/modifyDomain`
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainId | string | body | 否 | domain- 001 | 域名ID，修改时必填。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| protocol | string | body | 是 | HTTPS | 协议类型。可选值： HTTP 、 HTTPS 。 |

|  |  | domain- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  | HTTP |
|---|---|
| HTTPS |  |

智能体工厂 OpenTrek

| certificateId | string | body | 否 | cert-001 | HTTPS协议时需要的服务端证书 ID。 |
|---|---|---|---|---|---|
| domain | string | body | 是 | api.example. com | 域名。 |
| clientAuth | integer | body | 否 | 1 | 是否开启客户端认证。 |
| caCertificateId | string | body | 否 | ca-cert- 001 | CA证书ID。 |
| subjectDn | string | body | 否 | X-Subject- Dn | Subject DN转发头。 |
| issuerDn | string | body | 否 | X-Issuer- Dn | Issuer DN转发头。 |

|  |  | api.example. | 域 |
|---|---|---|---|
|  | com |  |  |

|  |  | ca-cert- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | domain-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /domain/modifyDomain HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "domainId": "domainId_value",
  "gwInstanceId": "gwInstanceId_value",
  "protocol": "protocol_value",
  "certificateId": "certificateId_value",
  "domain": "domain_value",
  "clientAuth": 0,
  "caCertificateId": "caCertificateId_value",
  "subjectDn": "subjectDn_value",
  "issuerDn": "issuerDn_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 模型API

#### batchGrantModelApi

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| modelApiId | string | body | 是 | model-api- 001 | 模型API ID。 |
|---|---|---|---|---|---|
| consumerIds | string[] | body | 是 | ["app-001", "app-002"] | 消费者ID列表。 |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | ["app-001", | 消费者ID列 |
|---|---|---|---|
|  | "app-002"] |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | null | 响应数据（null）。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "modelApiId": "model-api-001",
  "consumerIds": ["app-001", "app-002"]
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": null
}
```

智能体工厂 OpenTrek

#### changeModelApiAuthStatus

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| id | string | body | 是 | model-api- 001 | 模型API ID。 |
| authentication Config | object | body | 是 | - | 认证配置。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

**authenticationConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | true | 是否启用。 |
| credentialType List | string[] | body | 否 | ["apiKey","b earer"] | 凭证类型列表。 |

|  |  | ["apiKey","b | 凭证类型 |
|---|---|---|---|
|  | earer"] |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | object | - | 响应数据。 |

**示例**

**请求示例**

```json
POST /modelapi/changeModelApiAuthStatus HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value",
  "authenticationConfig": {
    "enable": true,
    "credentialTypeList": []
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### createModelApi

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId |  | string |  |  | body |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| apiName |  | string |  |  | body |  | 是 |  | my-ai-api |  | 模型API名称。 |  |
| description |  | string |  |  | body |  | 否 |  | OpenAI文本生成API |  | 描述信息。 |  |
| basePath |  | string |  |  | body |  | 否 |  | /v1/chat |  | 基础路径。 |  |
| basePathRemo ve |  | boolean |  |  | body |  | 否 |  | false |  | 是否移除基础路径前缀。 |  |
| methodPathList |  | ModelRouteMe thodPath[] |  |  | body |  |  |  | [{"path": |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [{"path": |  |  |
|  |  |  | ModelRouteMe |  | body |  |  |  | "/completions |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 路径和方法配置 |  |
|  | thodPathList | thodPath[] |  |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | ", "method": |  | 列表。 |  |
|  |  |  |  |  |  |  |  |  | "POST"}] |  |  |  |
| domainNameLi st |  | string[] |  |  | body |  | 否 |  | ["api.exampl e.com"] |  | 域名列表。 |  |
| protocol |  | string |  |  | body |  | 是 |  | openai |  | 协议类型。 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | OpenAI文本生 | 描述 |
|---|---|---|---|
|  | 成API |  |  |

|  |  | ["api.exampl | 域名列表 |
|---|---|---|---|
|  | e.com"] |  |  |

智能体工厂 OpenTrek

| sceneType | string | body | 是 | TEXT GENERAT _ ION |  | 场景类型。可选值： TEXT GEN _ ERATION （文本生成）、 IMAGE _ GENERATION （图片生成）、 VIDEO _ GENERATION （视频生成）、 SPEECH SYNTHESIS _ （语音合成）、 TEXT R _ ERANK （文本排序/Rerank）、 EMBEDDING （ 向量化）、 OTHER （其他）。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | IMAGE _ |  |  |
|  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  |  | VIDEO _ |  |  |
|  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  |  | SPEECH |  |  |
|  |  |  |  |  |  | SYNTHESIS _ |  |  |  |
| routeDispatche r | object | body | 否 | 见下方示例 |  | 路由分发配置。 |  |  |  |
| observationCon fig | object | body | 否 | {"enable": true} |  | 可观测性配置。 |  |  |  |
| fallback | object | body | 否 | {"enable": false} |  | 降级配置。 |  |  |  |

|  |  | TEXT GEN _ |  |
|---|---|---|---|
|  | ERATION |  |  |

|  |  | TEXT R _ |  |
|---|---|---|---|
|  | ERANK |  |  |

| ERAT |  |
|---|---|

|  | ION |
|---|---|

|  |  | {"enable": | 可观 |
|---|---|---|---|
|  | true} |  |  |

|  |  | {"enable": | 降级 |
|---|---|---|---|
|  | false} |  |  |

**methodPathList 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| path | string | body | 否 | /completions | 路径。 |
|---|---|---|---|---|---|
| method | string | body | 否 | POST | HTTP方法。 |

|  |  | /completions |
|---|---|---|

**observationConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | true | 是否启用。 |
| logRequestInfo | boolean | body | 否 | true | 是否记录请求信息。 |
| logResponseInf o | boolean | body | 否 | false | 是否记录响应信息。 |

**fallback 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | false | 是否启用。 |
| responseCodes | string[] | body | 否 | ["500", "503"] | 触发降级的响应码。 |
| fallbackServiceI d | string | body | 否 | fallback- service-001 | 降级服务ID。 |
| fallbackStrateg y | string | body | 否 | ratio | 降级策略。 |

|  |  | ["500", | 触 |
|---|---|---|---|
|  | "503"] |  |  |

|  |  | fallback- | 降级服务I |
|---|---|---|---|
|  | service-001 |  |  |

**routeDispatcher 对象结构**

路由分发配置，根据 `strategyType` 字段值采用不同的策略类型。

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| strategyType | string | body |  |  |  | 是 |  |  |  |  |  | 路由分发策略类型，可选值： WEIGHT （权重分发）、 HEADER （Header条件分发）、 WEIGHT |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  | WEIGHT |  |
|  |  |  |  |  |  |  |  |  |  |  |  | MODEL MAPPIN _ _ |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | G |  |  |
|  |  |  |  |  |  |  |  |  | WEIGHT | WEIGHT |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | SINGLE |  |
|  |  |  |  |  |  |  |  |  |  |  |  | MODEL MAPPIN _ _ |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | G |  |  |
| rules | array | body |  |  |  |  |  |  | [{"weight":5 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [{"weight":5 |  | 路由规则列表， 结构根据 |  |  |
|  |  |  |  |  |  |  |  |  | 0,"serviceId" |  |  |  |  |  |
|  |  |  | body |  |  |  |  |  |  |  |  | strategyTyp |  |  |
|  |  |  |  |  |  | 否 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | :"svc- |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 001"}] |  |  |  |  |  |

**WEIGHT 策略（权重分发）：**

| 参数名称 | 类型 | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|
| rules | array | 是 |  | [{"weight":50," |  |  |  |
|  |  |  |  |  | [{"weight":50," |  |  |
|  |  |  |  | serviceId":"svc- |  |  |  |
|  |  |  |  |  |  | 权重 |  |
|  |  |  |  | 001"}] |  |  |  |
| rules[].weight | integer | 是 |  | 50 |  | 权重值（百分比）。 |  |
| rules[].serviceId | string | 是 |  | svc-001 |  | 目标服务ID。 |  |
| rules[].serviceNam e | string | 否 |  | model-service |  | 目标服务名称。 |  |

**HEADER 策略（Header条件分发）：**

| 参数名称 | 类型 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|

智能体工厂 OpenTrek

| rules | array |  |  |  | [{"headerMatch" |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | [{"headerMatch" |  |  |  |  |  |
|  |  |  |  |  | :{"model":"gpt- |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | He |  |  |
|  |  |  | 是 |  |  |  |  |  |  |  |  |
|  |  |  |  |  | 4"}}] |  |  |  |  |  |  |
| rules[].headerMatc h | object |  | 是 |  | {"model": "gpt-4"} |  |  |  | Header匹配条件，key-value 形式，如 {"model": "gpt-4"} 。 |  |  |
|  |  |  |  |  |  | {"model": |  |  | 件 |  |  |
|  |  |  |  |  |  |  |  |  |  | {"model": |  |
|  |  |  |  |  |  |  |  |  | "gpt-4"} |  |  |
| rules[].weightRuleL ist | array |  | 否 |  | [{"weight":50," |  |  |  |  |  |  |
|  |  |  |  |  |  | [{"weight":50," |  |  | 权重规则列表（匹配 |  |  |
|  |  |  |  |  | serviceId":"svc- |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 成功 |  |  |
|  |  |  |  |  | 001"}] |  |  |  |  |  |  |
| rules[].serviceId | string |  | 否 |  | svc-001 |  |  |  | 目标服务ID（已废弃，建议使用 weightRuleList）。 |  |  |

**WEIGHT_MODEL_MAPPING / SINGLE_MODEL_MAPPING 策略（权重+模型映射）：**

|  | 参数名称 |  |  | 类型 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | rules |  |  |  |  |  |  |  |  | [{"weight":50," |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"weight":50," |  |  |
|  |  |  |  |  |  |  |  |  |  | serviceId":"svc- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 001","modelMappin |  | 权重+模型映射规则 |  |
|  |  |  |  | array |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | g":{"gpt- |  | 列表。 |  |
|  |  |  |  |  |  |  |  |  |  | 3.5":"gpt- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 4"}}] |  |  |  |
|  | rules[].weight |  |  | integer |  |  |  | 是 |  | 50 |  | 权重值（百分比）。 |  |
|  | rules[].serviceId |  |  | string |  |  |  | 是 |  | svc-001 |  | 目标服务ID。 |  |
|  | rules[].modelMappi ng |  |  | object |  |  |  | 否 |  | {"gpt-3.5": "gpt-4"} |  | 模型映射配置，key- value 形式，如 {"gpt-3.5": "gpt-4"} 。 |  |
|  | rules[].serviceNam e |  |  | string |  |  |  | 否 |  | model-service |  | 目标服务名称。 |  |

| {"gpt-3.5": |  |  | valu |  |
|---|---|---|---|---|
|  |  |  | "gpt-4"} |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | modelapi-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "apiName": "apiName_value",
  "description": "description_value",
  "basePath": "basePath_value",
  "basePathRemove": true,
  "methodPathList": [
    {
      "path": "path_value",
      "method": "method_value"
    }
```

`],`

```json
  "domainNameList": [],
  "protocol": "protocol_value",
  "sceneType": "sceneType_value",
  "routeDispatcher": {},
  "observationConfig": {
    "enable": true,
    "logRequestInfo": true,
    "logResponseInfo": true
  },
  "fallback": {
    "enable": true,
    "responseCodes": [],
    "fallbackServiceId": "fallbackServiceId_value",
    "fallbackStrategy": "fallbackStrategy_value"
  }
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### createModelApiStrategyConfig

**API 接口概述**

```
请求路径： /modelapi/createModelApiStrategyConfig
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 |  |  | 示例 |  |  |  |  |  |  |  | 说明 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| modelApiId | string | body | 是 |  |  | model-api- |  |  |  |  |  |  |  | 模型API ID，格式为 model- |  |  |  |  |  |  |
|  |  |  |  |  |  |  | model-api- |  |  |  |  |  |  | 式为 |  |  | model- |  |  |  |
|  |  |  |  |  |  | my-api |  |  |  |  |  |  |  | api- |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | {apiName} |  |  |  |  |  |  |
| gwInstanceId | string | body | 是 |  |  | higress- 001 |  |  |  |  |  |  |  | 网关实例ID。 |  |  |  |  |  |  |
| strategyName | string | body | 是 |  |  | ai-token- |  |  |  |  |  |  |  | 策略名称（插件名称），如 |  |  |  |  |  |  |
|  |  |  |  |  |  |  | ai-token- |  |  |  |  |  |  |  |  | ai-token- |  |  |  |  |
|  |  |  |  |  |  | limit |  |  |  |  |  |  |  | limit |  |  |  | 、 | ai- |  |
| config | object | body | 否 |  |  | 见下方示例 |  |  |  |  |  |  |  | 插件配置对象，JSON 格式， 字段根据插件类型动态变化。 |  |  |  |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| rawConfig | string | body | 否 | 见下方示例 | YAML 格式的插件配置字符串， 与 config 二选一，推荐使用此字段。 |
|---|---|---|---|---|---|

| 要： | config |
|---|---|
| config ：JS rawConfig |  |

**config/rawConfig 配置结构**

插件配置的字段结构根据 `strategyName` （插件类型）不同而变化。以下是常用插件的配置示例：

**ai-token-limit（Token 限流插件）**

限制 API 的 Token 消耗量，支持按时间窗口配置限流规则。
**config** **示例（****JSON** **格式）**：

```json
{
  "rule_items": [
    {
      "limit_by_type": "consumer",
      "limit_by_value": "",
      "limit_keys": [
        {
          "key": "default",
          "time_unit": "hour",
          "token_limit": 1000
        }
```

]

```
    }
```

]

```
}
```

**rawConfig** **示例（****YAML** **格式）**：

```
rule_items:
  - limit_by_type: consumer
    limit_by_value: ""
    limit_keys:
      - key: default
        time_unit: hour
        token_limit: 1000
```

| 字段 | 类型 | 说明 |
|---|---|---|
| rule items _ | array | 限流规则列表。 |

智能体工厂 OpenTrek

| rule items.limit by type _ _ _ | string | 限流维度，可选值： consumer （按消费者）、 api key （按 API Key）。 _ |  |  |
|---|---|---|---|---|
| rule items.limit by value _ _ _ | string | 限流维度的具体值，为空表示全部。 |  |  |
| rule items.limit keys _ _ | array | 限流配置项列表。 |  |  |
| rule items.limit keys.key _ _ | string | 限流键名， default 表示默认规则。 |  |  |
| rule items.limit keys.time unit _ _ _ | string | 时间单位，可选值： second 、 minute 、 hou r 、 day 。 |  |  |
|  |  |  | hou |  |
| rule items.limit keys.token limit _ _ _ | integer | Token 数量上限。 |  |  |

|  | r |
|---|---|

**ai-statistics（AI 统计插件）**

记录 AI 调用的统计信息，用于监控和分析。
**config** **示例（****JSON** **格式）**：

```json
{
  "enable": true,
  "statistics_type": "model"
}
```

**rawConfig** **示例（****YAML** **格式）**：

```
enable: true statistics_type: model
```

| 字段 | 类型 | 说明 |
|---|---|---|
| enable | boolean | 是否启用统计，默认 true 。 |
| statistics type _ | string | 统计维度，可选值： model （按模型）、 consumer （按消费者）。 |

**request-validation（请求验证插件）**

校验请求参数，确保请求符合预期格式。
**config** **示例（****JSON** **格式）**：
智能体工厂 OpenTrek

```json
{
  "body_schema": {
    "type": "object",
    "required": ["prompt"],
    "properties": {
      "prompt": {"type": "string"}
    }
  }
}
```

**rawConfig** **示例（****YAML** **格式）**：

```
body_schema:
  type: object
  required:
    - prompt
  properties:
    prompt:
      type: string
```

| 字段 | 类型 | 说明 |
|---|---|---|
| body schema _ | object | JSON Schema 格式的请求体校验规则。 |

**response-cache（响应缓存插件）**

缓存 AI 响应结果，减少重复调用。
**config** **示例（****JSON** **格式）**：

```json
{
  "cache_key": "request_body",
  "ttl": 3600
}
```

**rawConfig** **示例（****YAML** **格式）**：

```
cache_key: request_body ttl: 3600
```

| 字段 | 类型 | 说明 |  |  |
|---|---|---|---|---|
| cache key _ | string | 缓存键来源，可选值： request body 、 request _ _ header 等。 |  |  |
|  |  |  | request _ |  |
| ttl | integer | 缓存过期时间（秒）。 |  |  |

|  |  | request body _ |
|---|---|---|
|  | header |  |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx | 请求ID。 |
| code | integer | 200 | 响应码，200 表示成功。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | wasm-plugin-xxx | 创建成功的策略配置ID。 |

**示例**

**请求示例 - 使用 rawConfig（推荐）**

```json
POST /modelapi/createModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "modelApiId": "model-api-my-ai-api",
  "gwInstanceId": "higress-001",
  "strategyName": "ai-token-limit",
  "rawConfig": "rule_items:\n  - limit_by_type: consumer\n    limit_by_value: \"\"\n    limit_k
eys:\n - key: default\n time_unit: hour\n token_limit: 1000" }
```

**请求示例 - 使用 config**

智能体工厂 OpenTrek

```json
POST /modelapi/createModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "modelApiId": "model-api-my-ai-api",
  "gwInstanceId": "higress-001",
  "strategyName": "ai-token-limit",
  "config": {
    "rule_items": [
      {
        "limit_by_type": "consumer",
        "limit_by_value": "",
        "limit_keys": [
          {
            "key": "default",
            "time_unit": "hour",
            "token_limit": 1000
          }
```

]

```
      }
```

]

```
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "wasm-plugin-ai-token-limit-model-api-my-ai-api-xxx"
}
```

#### deleteModelApi

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| AI Gateway 开发指 | 南·API参考 |  |  | 智 | 能体工厂 OpenTre |
|---|---|---|---|---|---|

| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|
| id | string | body | 否 | model-api- 001 | ID标识。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据（null）。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": null
}
```

智能体工厂 OpenTrek

#### deleteModelApiStrategyConfig

**API 接口概述**

```
请求路径： /modelapi/deleteModelApiStrategyConfig
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| strategyConfigI d | string | body | 否 | strategy- 001 | 策略配置ID。 |
| modelApiId | string | body | 否 | model-api- 001 | 模型API ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | strategy- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | null | 响应数据（该接口无返回数据）。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /modelapi/deleteModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "strategyConfigId": "strategy-001",
  "modelApiId": "model-api-001",
  "gwInstanceId": "higress-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": null
}
```

#### getModelApiById

**API 接口概述**

**请求路径：** `/modelapi/getModelApi`
**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| id | string | body | 否 | model-api- 001 | ID标识。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.id | string | model-api-001 | ID标识。 |
| data.apiName | string | my-model-api | API名称。 |
| data.description | string | 文本生成模型API | 描述信息。 |
| data.basePath | string | /api/v1/chat | 基础路径。 |
| data.basePathRemove | boolean | false | 是否移除基础路径。 |
| data.methodPathList | ModelRouteMethodPath [] | - | 方法和路径配置列表。 |
| data.methodPathList.pat h | string | /completions | 路径。 |
| data.methodPathList.met hod | string | POST | HTTP方法。 |
| data.domainNameList | string[] | ["api.example.com"] | 域名列表。 |
| data.protocol | string | openai | 协议类型。 |
| data.sceneType | string | TEXT GENERATION _ | 场景类型。 |
| data.routeDispatcher | object | - | 路由分发配置。 |
| data.observationConfig | object | - | 可观测性配置。 |
| data.observationConfig.e nable | boolean | true | 是否启用。 |

|  |  | ModelRouteMethodPath |  |  |
|---|---|---|---|---|
| a.methodPathList | [] |  |  |  |

|  | ["api.example.com"] |
|---|---|

智能体工厂 OpenTrek

| data.observationConfig.l ogRequestInfo | boolean | true | 是否记录请求信息。 |
|---|---|---|---|
| data.observationConfig.l ogResponseInfo | boolean | false | 是否记录响应信息。 |
| data.fallback | object | - | 降级配置。 |
| data.fallback.enable | boolean | false | 是否启用。 |
| data.fallback.responseCo des | string[] | ["500","502"] | 触发降级的响应码。 |
| data.fallback.fallbackSer viceId | string | fallback-service- 001 | 降级服务ID。 |
| data.fallback.fallbackStra tegy | string | modelFallback | 降级策略。 |
| data.authenticationConfi g | object | - | 认证配置。 |
| data.authenticationConfi g.enable | boolean | true | 是否启用。 |
| data.authenticationConfi g.credentialTypeList | string[] | ["apiKey","bearer"] | 凭证类型列表。 |

|  | fallback-service- |
|---|---|
| 001 |  |

|  | ["apiKey","bearer"] |
|---|---|

**示例**

**请求示例**

```json
POST /modelapi/getModelApi HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "id": "id_value",
    "apiName": "apiName_value",
    "description": "description_value",
    "basePath": "basePath_value",
    "basePathRemove": true,
    "methodPathList": {
      "path": "path_value",
      "method": "method_value"
    },
    "domainNameList": [],
    "protocol": "protocol_value",
    "sceneType": "sceneType_value",
    "routeDispatcher": {},
    "observationConfig": {
      "enable": true,
      "logRequestInfo": true,
      "logResponseInfo": true
    },
    "fallback": {
      "enable": true,
      "responseCodes": [],
      "fallbackServiceId": "fallbackServiceId_value",
      "fallbackStrategy": "fallbackStrategy_value"
    },
    "authenticationConfig": {
      "enable": true,
      "credentialTypeList": []
    }
  }
}
```

#### getModelApiPolicies

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|
| id | string | body | 否 | model-api- 001 | ID标识。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.aiSecurityPolicyCon fig | object | {} | AI安全策略配置。 |
| data.aiSecurityPolicyCon fig.enabled | boolean | false | 是否启用。 |
| data.aiSecurityPolicyCon fig.accessUrl | string | https://security.exa mple.com | 安全检查服务访问地址。 |
| data.aiSecurityPolicyCon fig.checkRequestEnabled | boolean | true | 是否启用请求检查。 |
| data.aiSecurityPolicyCon fig.checkResponseEnable d | boolean | false | 是否启用响应检查。 |
| data.aiSecurityPolicyCon fig.streamChunkSize | integer | 1024 | 流式分块大小。 |
| data.aiSecurityPolicyCon fig.timeoutSeconds | integer | 30 | 超时时间（秒）。 |
| data.aiSecurityPolicyCon fig.denyMessage | string | 内容不符合安全规范 | 拒绝消息。 |

| https://security.exa | 安全检查 |
|---|---|

智能体工厂 OpenTrek

| data.aiSecurityPolicyCon fig.requestCheckService |  | string |  | security-service |  |  | 请求检查服务名称。 |
|---|---|---|---|---|---|---|---|
| data.aiSecurityPolicyCon fig.responseCheckServic e |  | string |  | security-service |  |  | 响应检查服务名称。 |
| data.aiSecurityPolicyCon fig.riskLevelBar |  | string |  | HIGH |  |  | 风险级别阈值。 |
| data.aiTokenLimitPolicyC onfig |  | object |  | {} |  |  | AI Token限流策略配置。 |
| data.aiTokenLimitPolicyC onfig.enabled |  | boolean |  | true |  |  | 是否启用。 |
| data.aiTokenLimitPolicyC |  | AiTokenLimitPolicyCo |  |  |  |  | 限流规则项列表。 |
|  |  |  | AiTokenLimitPolicyCo |  |  |  |  |
|  | a.aiTokenLimitPolicyC | nfig$AiTokenLimitRuleI |  |  |  |  |  |
|  |  |  |  |  | [] |  |  |
| onfig.ruleItems | ig.ruleItems |  |  |  |  |  |  |
|  |  | tem[] |  |  |  |  |  |
| data.aiTokenLimitPolicyC onfig.ruleItems.limitByTy pe |  | string |  | consumer |  |  | 限流维度类型。 |
| data.aiTokenLimitPolicyC onfig.ruleItems.limitByVa lue |  | string |  | app-001 |  |  | 限流维度值。 |
| data.aiTokenLimitPolicyC |  | AiTokenLimitPolicyCo |  | [] |  |  | 限流键列表。 |
|  |  |  | AiTokenLimitPolicyCo |  |  |  |  |
|  | a.aiTokenLimitPolicyC | nfig$AiTokenLimitKey[] |  |  |  |  |  |
| onfig.ruleItems.limitKeys | ig.ruleItems.limitKeys |  |  |  |  |  |  |
| data.aiTokenLimitPolicyC onfig.ruleItems.limitKeys .key |  | string |  | token limit _ |  |  | 键名。 |
| data.aiTokenLimitPolicyC onfig.ruleItems.limitKeys .timeUnit |  | string |  | DAY |  |  | 时间单位。 |
| data.aiTokenLimitPolicyC onfig.ruleItems.limitKeys .tokenLimit |  | integer |  | 10000 |  |  | Token限制数量。 |
| data.clusterQpsLimitPolic yConfig |  | object |  | {} |  |  | 集群QPS限流策略配置。 |
| data.clusterQpsLimitPolic yConfig.enabled |  | boolean |  | true |  |  | 是否启用。 |

智能体工厂 OpenTrek

| data.clusterQpsLimitPolic yConfig.queryPerSecond |  | integer |  | 100 |  |  | 每秒允许的请求数。 |
|---|---|---|---|---|---|---|---|
| data.clusterQpsLimitPolic yConfig.queryPerMinute |  | integer |  | 6000 |  |  | 每分钟允许的请求数。 |
| data.clusterQpsLimitPolic yConfig.queryPerHour |  | integer |  | 360000 |  |  | 每小时允许的请求数。 |
| data.clusterQpsLimitPolic yConfig.queryPerDay |  | integer |  | 8640000 |  |  | 每天允许的请求数。 |
| data.allClusterLimitPolicy Config |  | object |  | {} |  |  | 全局限流策略配置。 |
| data.allClusterLimitPolicy Config.enabled |  | boolean |  | false |  |  | 是否启用。 |
| data.allClusterLimitPolicy Config.multiRuleMode |  | boolean |  | false |  |  | 多规则模式。 |
| data.allClusterLimitPolicy Config.maxConcurrentRu les |  | integer |  | 10 |  |  | 最大并发规则数。 |
| data.allClusterLimitPolicy Config.rejectedCode |  | integer |  | 429 |  |  | 拒绝响应码。 |
| data.allClusterLimitPolicy Config.rejectedMsg |  | string |  | 请求过多，请稍后重试 |  |  | 拒绝消息。 |
| data.allClusterLimitPolicy |  | AllClusterLimitPolic |  |  |  |  | 全局阈值列表。 |
|  |  |  | AllClusterLimitPolic |  |  |  |  |
|  | a.allClusterLimitPolicy | yConfig$GlobalThreshol |  |  |  |  |  |
|  |  |  |  |  | [] |  |  |
| Config.globalThresholds | fig.globalThresholds |  |  |  |  |  |  |
|  |  | dConfig[] |  |  |  |  |  |
| data.allClusterLimitPolicy Config.globalThresholds.l imitType |  | string |  | QPS |  |  | 限制类型。 |
| data.allClusterLimitPolicy Config.globalThresholds.l imitKeys |  | object |  | {} |  |  | 限制键配置。 |
| data.allClusterLimitPolicy Config.globalThresholds.f ixedQuotaMode |  | boolean |  | false |  |  | 固定配额模式。 |

智能体工厂 OpenTrek

| data.allClusterLimitPolicy Config.globalThresholds. hitsAddend |  | object |  | {} |  |  |  | 命中加数配置。 |
|---|---|---|---|---|---|---|---|---|
| data.allClusterLimitPolicy Config.globalThresholds. hitsAddend.base |  | integer |  | 1 |  |  |  | 基础值。 |
| data.allClusterLimitPolicy Config.globalThresholds. hitsAddend.fromHeader |  | string |  | X-Request-Weight |  |  |  | 来源Header。 |
| data.allClusterLimitPolicy |  | AllClusterLimitPolic |  |  |  |  |  | 规则项列表。 |
|  |  |  | AllClusterLimitPolic |  |  |  |  |  |
|  | a.allClusterLimitPolicy | yConfig$RuleItemConfig |  |  |  |  |  |  |
|  |  |  |  |  |  | [] |  |  |
| Config.ruleItems | fig.ruleItems |  |  |  |  |  |  |  |
|  |  | [] |  |  |  |  |  |  |
| data.allClusterLimitPolicy Config.ruleItems.limitBy |  | string |  | consumer |  |  |  | 限制维度。 |
| data.allClusterLimitPolicy Config.ruleItems.limitByF rom |  | string |  | header |  |  |  | 限制来源。 |
| data.allClusterLimitPolicy Config.ruleItems.andMat |  | AllClusterLimitPolic |  |  |  |  |  | 匹配器配置列表。 |
|  |  |  | AllClusterLimitPolic |  |  |  |  |  |
|  | fig.ruleItems.andMat | yConfig$AndMatcherConf |  |  |  |  |  |  |
|  |  |  |  |  | [] |  |  |  |
| cherConfig |  |  |  |  |  |  |  |  |
|  |  | ig[] |  |  |  |  |  |  |
| data.allClusterLimitPolicy Config.ruleItems.andMat cherConfig.limitBy |  | string |  | header |  |  |  | 匹配维度。 |
| data.allClusterLimitPolicy Config.ruleItems.andMat cherConfig.limitByFrom |  | string |  | X-Consumer-ID |  |  |  | 匹配来源。 |
| data.allClusterLimitPolicy Config.ruleItems.andMat cherConfig.key |  | string |  | consumer match _ |  |  |  | 键名。 |
| data.allClusterLimitPolicy Config.ruleItems.limitKey |  | AllClusterLimitPolic |  |  |  |  |  | 限制键列表。 |
|  |  |  | AllClusterLimitPolic |  |  |  |  |  |
|  | fig.ruleItems.limitKey | yConfig$RuleItemLimitK |  |  |  |  |  |  |
|  |  |  |  |  | [] |  |  |  |
| s |  |  |  |  |  |  |  |  |
|  |  | ey[] |  |  |  |  |  |  |
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.limitType |  | string |  | QPS |  |  |  | 限制类型。 |

智能体工厂 OpenTrek

| data.allClusterLimitPolicy Config.ruleItems.limitKey s.limitKeys | object | {} | 限制键配置。 |
|---|---|---|---|
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.fixedQuotaMode | boolean | false | 固定配额模式。 |
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.hitsAddend | object | {} | 命中加数配置。 |
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.hitsAddend.base | integer | 1 | 基础值。 |
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.hitsAddend.fromHeade r | string | X-Request-Weight | 来源Header。 |
| data.allClusterLimitPolicy Config.ruleItems.limitKey s.key | string | limit key _ | 键名。 |
| data.headerControl | object | {} | Header控制配置。 |
| data.headerControl.enab led | boolean | false | 是否启用Header控制功能。 |
| data.headerControl.requ est | object | {} | 请求Header配置。 |
| data.headerControl.requ est.add | Header[] | [] | 要添加的Header列表。 |
| data.headerControl.requ est.add.key | string | X-Custom-Header | 键名。 |
| data.headerControl.requ est.add.value | string | custom-value | 键值。 |
| data.headerControl.requ est.set | Header[] | [] | 要设置的Header列表。 |
| data.headerControl.requ est.set.key | string | X-Set-Header | 键名。 |

智能体工厂 OpenTrek

| data.headerControl.requ est.set.value | string | set-value | 键值。 |
|---|---|---|---|
| data.headerControl.requ est.remove | string[] | [] | 要移除的Header列表。 |
| data.headerControl.resp onse | object | {} | 响应Header配置。 |
| data.headerControl.resp onse.add | Header[] | [] | 要添加的Header列表。 |
| data.headerControl.resp onse.add.key | string | X-Response-Header | 键名。 |
| data.headerControl.resp onse.add.value | string | response-value | 键值。 |
| data.headerControl.resp onse.set | Header[] | [] | 要设置的Header列表。 |
| data.headerControl.resp onse.set.key | string | X-Response-Set | 键名。 |
| data.headerControl.resp onse.set.value | string | response-set-value | 键值。 |
| data.headerControl.resp onse.remove | string[] | [] | 要移除的Header列表。 |
| data.timeoutConfig | object | {} | 超时配置。 |
| data.timeoutConfig.enab led | boolean | true | 是否启用。 |
| data.timeoutConfig.time out | integer | 60 | 超时时间（秒）。 |
| data.retryConfig | object | {} | 重试配置。 |
| data.retryConfig.enabled | boolean | false | 是否启用。 |
| data.retryConfig.attempt s | integer | 3 | 重试次数。 |
| data.retryConfig.timeout | integer | 5 | 超时时间（秒）。 |

智能体工厂 OpenTrek

| data.retryConfig.conditio ns | string[] | ["error", "timeout"] | 重试条件。 |
|---|---|---|---|
| data.retryConfig.httpStat usCodes | integer[] | [500, 502, 503] | HTTP状态码列表。 |

|  |  | ["error", |
|---|---|---|
|  | "timeout"] |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "aiSecurityPolicyConfig": {
      "enabled": true,
      "accessUrl": "accessUrl_value",
      "checkRequestEnabled": true,
      "checkResponseEnabled": true,
      "streamChunkSize": 0,
      "timeoutSeconds": 0,
      "denyMessage": "denyMessage_value",
      "requestCheckService": "requestCheckService_value",
      "responseCheckService": "responseCheckService_value",
      "riskLevelBar": "riskLevelBar_value"
    },
    "aiTokenLimitPolicyConfig": {
      "enabled": true,
      "ruleItems": {
        "limitByType": "limitByType_value",
        "limitByValue": "limitByValue_value",
        "limitKeys": {
          "key": {},
          "timeUnit": {},
          "tokenLimit": {}
        }
      }
    },
    "clusterQpsLimitPolicyConfig": {
      "enabled": true,
      "queryPerSecond": 0,
```

智能体工厂 OpenTrek

```json
      queryPerSecond: 0,
      "queryPerMinute": 0,
      "queryPerHour": 0,
      "queryPerDay": 0
    },
    "allClusterLimitPolicyConfig": {
      "enabled": true,
      "multiRuleMode": true,
      "maxConcurrentRules": 0,
      "rejectedCode": 0,
      "rejectedMsg": "rejectedMsg_value",
      "globalThresholds": {
        "limitType": "limitType_value",
        "limitKeys": {},
        "fixedQuotaMode": true,
        "hitsAddend": {
          "base": {},
          "fromHeader": {}
        }
      },
      "ruleItems": {
        "limitBy": "limitBy_value",
        "limitByFrom": "limitByFrom_value",
        "andMatcherConfig": {
          "limitBy": {},
          "limitByFrom": {},
          "key": {}
        },
        "limitKeys": {
          "limitType": {},
          "limitKeys": {},
          "fixedQuotaMode": {},
          "hitsAddend": {},
          "key": {}
        }
      }
    },
    "headerControl": {
      "enabled": true,
      "request": {
        "add": {
          "key": {},
          "value": {}
        },
        "set": {
          "key": {},
          "value": {}
        },
        "remove": []
      },
      "response": {
        "add": {
          "key": {},
          "value": {}
        },
        "set": {
          "key": {},
          "value": {}
        },
```

智能体工厂 OpenTrek

```json
        "remove": []
      }
    },
    "timeoutConfig": {
      "enabled": true,
      "timeout": 0
    },
    "retryConfig": {
      "enabled": true,
      "attempts": 0,
      "timeout": 0,
      "conditions": [],
      "httpStatusCodes": []
    }
  }
}
```

#### getModelApiStrategyConfig

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| strategyConfigI d | string | body | 否 | strategy- 001 | 策略配置ID。 |
| modelApiId | string | body | 否 | model-api- 001 | 模型API ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | strategy- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.strategyConfigId | string | strategy-001 | 策略配置ID。 |
| data.strategyName | string | token-limit-policy | 策略名称。 |
| data.strategyTitle | string | Token限流策略 | 策略标题。 |
| data.status | boolean | true | 状态。 |
| data.config | object | {} | 插件配置。 |
| data.rawConfig | string | {} | rawConfig字段。 |
| data.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.updateTime | string | 2024-01-01 10:00:00 | 更新时间。 |
| data.modelApiId | string | model-api-001 | 模型API ID。 |

**示例**

**请求示例**

```json
POST /modelapi/getModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "strategyConfigId": "strategyConfigId_value",
  "modelApiId": "modelApiId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "strategyConfigId": "strategyConfigId_value",
    "strategyName": "strategyName_value",
    "strategyTitle": "strategyTitle_value",
    "status": true,
    "config": {},
    "rawConfig": "rawConfig_value",
    "createTime": "createTime_value",
    "updateTime": "updateTime_value",
    "modelApiId": "modelApiId_value"
  }
}
```

#### listModelApiConsumers

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| modelApiId | string | body | 是 | model-api- 001 | 模型API ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

智能体工厂 OpenTrek

| consumerNam e | string | body | 否 | app-001 | 消费者名称（可选，支持模糊查询）。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.total | integer | 2 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ListModelApiConsumer sResponse[] | [] | 记录列表。 |
| data.records.gwInstanceI d | string | higress-001 | 网关实例ID。 |
| data.records.modelApiId | string | model-api-001 | 模型API ID。 |
| data.records.appId | string | app-001 | 消费者ID。 |
| data.records.consumerN ame | string | 消费者应用1 | 消费者名称。 |
| data.records.authType | string | apikey | 认证类型。 |
| data.records.enable | boolean | true | 是否启用。 |

|  |  | ListModelApiConsumer | [] |
|---|---|---|---|
| a.records | sResponse[] |  |  |

智能体工厂 OpenTrek

| data.records.authId | string | auth-001 | 授权ID。 |
|---|---|---|---|

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value",
  "modelApiId": "modelApiId_value",
  "consumerName": "consumerName_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "total": 0,
    "current": 0,
    "size": 0,
    "records": {
      "gwInstanceId": "gwInstanceId_value",
      "modelApiId": "modelApiId_value",
      "appId": "appId_value",
      "consumerName": "consumerName_value",
      "authType": "authType_value",
      "enable": true,
      "authId": "authId_value"
    }
  }
}
```

#### listModelApiRoutes

**API 接口概述**

**请求方式：** `POST`
智能体工厂 OpenTrek
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| id | string | body | 否 | model-api- 001 | ID标识。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

**返回数据**

|  | 参数名称 |  | 类型 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|
|  | requestId |  | string |  | uuid-xxx-xxx |  | 请求ID。 |
|  | code |  | integer |  | 200 |  | 响应码。 |
|  | msg |  | string |  | success |  | 响应消息。 |
|  | message |  | string |  | success |  | 响应消息。 |
|  | data |  | ModelApiRouteInfo[] |  | [] |  | 响应数据。 |
|  | data.routeId |  | string |  | route-001 |  | 路由ID。 |
|  | data.routeName |  | string |  | ai-route-001 |  | 路由名称。 |
|  | data.enableStatus |  | boolean |  | true |  | 启用状态。 |
|  | data.routePath |  | string[] |  | ["/api/v1/chat"] |  | 路由路径。 |
|  | data.path |  | object |  | {} |  | 路径。 |
|  | data.path.matchType |  | string (枚举: |  | EXACT |  | 匹配类型。 |
|  |  |  |  | string (枚举: |  |  |  |
|  |  | atchType | RoutePredicateTypeEnum |  |  |  |  |
|  |  |  |  |  |  | EXACT |  |
|  |  |  | ) |  |  |  |  |
|  | data.path.matchValue |  | string |  | /api/v1/chat |  | 用于匹配的值。 |

|  |  | ModelApiRouteInfo[] |
|---|---|---|

智能体工厂 OpenTrek

| data.path.caseSensitive | boolean | true | 是否区分大小写匹配。 |
|---|---|---|---|
| data.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.domains | string[] | ["api.example.com"] | 域名列表。 |
| data.routeDispatcherCon fig | object | {} | 路由分发配置。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  | ["api.example.com"] |
|---|---|

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "routeId": "routeId_value",
    "routeName": "routeName_value",
    "enableStatus": true,
    "routePath": [],
    "path": {
      "matchType": "matchType_value",
      "matchValue": "matchValue_value",
      "caseSensitive": true
    },
    "createTime": "createTime_value",
    "domains": [],
    "routeDispatcherConfig": {}
  }
}
```

#### listModelApis

智能体工厂 OpenTrek

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| size | integer | body | 是 |  | 10 |  |  | 每页大小。 |  |  |  |
| current | integer | body | 是 |  | 1 |  |  | 当前页码。 |  |  |  |
| gwInstanceId | string | body | 否 |  | higress- 001 |  |  | 网关实例ID。 |  |  |  |
| apiName | string | body | 否 |  | my-model- api |  |  | API名称。 |  |  |  |
| protocol | string | body | 否 |  | openai |  |  | 协议类型。 |  |  |  |
| sceneType | string | body | 否 |  | TEXT GENERAT _ ION |  |  | 场景类型。可选值： TEXT GEN _ ERATION （文本生成）、 IMAGE _ GENERATION （图片生成）、 VIDEO _ GENERATION （视频生成）、 SPEECH SYNTHESIS _ （语音合成）、 TEXT R _ ERANK （文本排序/Rerank）、 EMBEDDING （ 向量化）、 OTHER （其他）。 |  |  |  |
|  |  |  |  |  |  |  |  |  | IMAGE _ |  |  |
|  |  |  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  |  |  |  | VIDEO _ |  |  |
|  |  |  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  | TEXT GENERAT _ |  | （ 成 |  |  |  |
|  |  |  |  |  |  |  |  |  | SPEECH |  |  |
|  |  |  |  |  | ION |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | SYNTHESIS _ |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | my-model- |
|---|---|---|
|  | api |  |

|  |  | TEXT GEN _ |  |
|---|---|---|---|
|  | ERATION |  |  |

|  |  | TEXT R _ |  |
|---|---|---|---|
|  | ERANK |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ModelApiResponse[] | - | 记录列表。 |
| data.records.id | string | model-api-001 | ID标识。 |
| data.records.apiName | string | my-model-api | API名称。 |
| data.records.description | string | 文本生成模型API | 描述信息。 |
| data.records.basePath | string | /api/v1/chat | 基础路径。 |
| data.records.basePathRe move | boolean | false | 是否移除基础路径。 |
| data.records.methodPath List | ModelRouteMethodPath [] | - | 方法和路径配置列表。 |
| data.records.methodPath List.path | string | /completions | 路径。 |
| data.records.methodPath List.method | string | POST | HTTP方法。 |
| data.records.domainNam eList | string[] | ["api.example.com"] | 域名列表。 |

|  |  | ModelRouteMethodPath |  |  |
|---|---|---|---|---|
|  | [] |  |  |  |

|  | ["api.example.com"] |
|---|---|

智能体工厂 OpenTrek

| data.records.protocol | string | openai | 协议类型。 |
|---|---|---|---|
| data.records.sceneType | string | TEXT GENERATION _ | 场景类型。 |
| data.records.routeDispat cher | object | - | 路由分发配置。 |
| data.records.observation Config | object | - | 可观测性配置。 |
| data.records.observation Config.enable | boolean | true | 是否启用。 |
| data.records.observation Config.logRequestInfo | boolean | true | 是否记录请求信息。 |
| data.records.observation Config.logResponseInfo | boolean | false | 是否记录响应信息。 |
| data.records.fallback | object | - | 降级配置。 |
| data.records.fallback.ena ble | boolean | false | 是否启用。 |
| data.records.fallback.res ponseCodes | string[] | ["500","502"] | 触发降级的响应码。 |
| data.records.fallback.fall backServiceId | string | fallback-service- 001 | 降级服务ID。 |
| data.records.fallback.fall backStrategy | string | modelFallback | 降级策略。 |
| data.records.authenticati onConfig | object | - | 认证配置。 |
| data.records.authenticati onConfig.enable | boolean | true | 是否启用。 |
| data.records.authenticati onConfig.credentialType List | string[] | ["apiKey","bearer"] | 凭证类型列表。 |

|  | fallback-service- |
|---|---|
| 001 |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "gwInstanceId": "gwInstanceId_value",
  "apiName": "apiName_value",
  "protocol": "protocol_value",
  "sceneType": "sceneType_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "total": 0,
    "current": 0,
    "size": 0,
    "records": {
      "id": "id_value",
      "apiName": "apiName_value",
      "description": "description_value",
      "basePath": "basePath_value",
      "basePathRemove": true,
      "methodPathList": {
        "path": "path_value",
        "method": "method_value"
      },
      "domainNameList": [],
      "protocol": "protocol_value",
      "sceneType": "sceneType_value",
      "routeDispatcher": {},
      "observationConfig": {
        "enable": true,
        "logRequestInfo": true,
        "logResponseInfo": true
      },
      "fallback": {
        "enable": true,
        "responseCodes": [],
        "fallbackServiceId": "fallbackServiceId_value",
        "fallbackStrategy": "fallbackStrategy_value"
      },
      "authenticationConfig": {
        "enable": true,
        "credentialTypeList": []
      }
    }
  }
}
```

#### listModelApiStrategyConfig

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| strategyName | string | body | 否 | token- limit- policy | 策略名称。 |
| modelApiId | string | body | 否 | model-api- 001 | 模型API ID。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

| token- |  |
|---|---|

|  |  | policy |
|---|---|---|

|  |  | model-api- |  |
|---|---|---|---|
|  | 001 |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.total | integer | 2 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ListModelApiStrategy ConfigResponse[] | [] | 记录列表。 |

|  |  | ListModelApiStrategy | [] |
|---|---|---|---|
| a.records | ConfigResponse[] |  |  |

智能体工厂 OpenTrek

| data.records.strategyCon figId | string | strategy-001 | 策略配置ID。 |
|---|---|---|---|
| data.records.strategyNa me | string | token-limit-policy | 策略名称。 |
| data.records.modelApiId | string | model-api-001 | 模型API ID。 |
| data.records.status | boolean | true | 状态。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.records.updateTime | string | 2024-01-01 10:00:00 | 更新时间。 |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
POST /modelapi/listModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "size": 0,
  "current": 0,
  "strategyName": "strategyName_value",
  "modelApiId": "modelApiId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "total": 0,
    "current": 0,
    "size": 0,
    "records": {
      "strategyConfigId": "strategyConfigId_value",
      "strategyName": "strategyName_value",
      "modelApiId": "modelApiId_value",
      "status": true,
      "createTime": "createTime_value",
      "updateTime": "updateTime_value"
    }
  }
}
```

#### modifyModelApiPolicy

**API 接口概述**

**请求方式：** `POST`

**说明**

此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  |  |  | 说明 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| configTy pe | string | body | 是 |  | "aiSec |  |  |  | 策略类型，决定 configData 的结构。支持值： rewrite 、 header 、 timeout 、 r etry 、 fallback 、 aiSecurity 、 aiTo kenLimit 、 aiModelParameterOverride 、 clusterQpsLimit 、 allClusterLimit 。 详见configType 与 configData 对应关系。 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | rewrite |  |  |  |  |  | header |  |  | timeout |  |  | r |  |
|  |  |  |  |  |  | "aiSec |  |  | etry |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 、 |  |  |  |  | 、 |  |  | 、 |  |  |  |
|  |  |  |  |  | urity |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  | " |  |  |  |  |  |  |  | 、 |  |  |  |  |  |  |  |  |  |
| configDa ta | object | body | 是 |  | {...} |  |  |  | 策略配置数据，结构随 configType 变化。详见configType 与 configData 对应关系。 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

|  |  | string |
|---|---|---|

|  |  | object |
|---|---|---|

|  |  | {...} |
|---|---|---|

智能体工厂 OpenTrek

| gwInstan ceId | string | body |  | 是 |  |  | "higre |  | 网关实例ID。 |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | "higre |  |
|  |  |  |  |  |  |  | ss- |  |  |
|  |  |  |  |  |  |  |  |  | 网关 |
|  |  |  |  |  | 是 |  |  |  |  |
|  |  |  |  |  |  |  | demo- |  |  |
|  |  |  |  |  |  |  | 001" |  |  |
| targetId | string | body |  | 是 |  |  | "model |  | 模型API的唯一标识ID。 |
|  |  |  |  |  |  |  |  | "model |  |
|  |  |  |  |  |  |  | -api- |  |  |
|  |  |  |  |  |  |  | 001" |  |  |

|  |  | string |
|---|---|---|

| etId |  |
|---|---|

**configType 与 configData 对应关系**

`configType` 指定策略类型， `configData` 提供对应的配置数据。以下是所有支持的策略类型及其配置结构：
1. . aiSecurity**（**AI** **内容安全策略）**

**configData 结构：**

```json
{
  "enabled": true,
  "checkRequestEnabled": true,
  "checkResponseEnabled": true,
  "streamChunkSize": 100,
  "timeoutSeconds": 1,
  "denyMessage": "Sorry, I can't answer this question",
  "requestCheckService": "dc_llm_query_moderation",
  "responseCheckService": "dc_llm_response_moderation",
  "riskLevelBar": "low"
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| enabled | Boolean | 是 | - | 是否启用内容安全检测。 |
| checkRequestEnabl ed | Boolean | 否 | false | 是否检测请求内容。 |
| checkResponseEna bled | Boolean | 否 | false | 是否检测响应内容。 |
| streamChunkSize | Integer | 否 | 100 | 流式响应分块大小。 |
| timeoutSeconds | Integer | 否 | 1 | 检测超时时间 （秒）。 |
| denyMessage | String | 否 | - | 内容违规时的拒绝消息。 |

智能体工厂 OpenTrek

| requestCheckServi ce | String | 否 | dc llm query mod _ _ _ eration | 请求内容检测服务名称。 |
|---|---|---|---|---|
| responseCheckSer vice | String | 否 | dc llm response m _ _ _ oderation | 响应内容检测服务名称。 |
| riskLevelBar | String | 否 | low | 风险等级拦截阈值： max （仅记录不拦截）、 high （仅拦截高风险）、 medium （ 拦截中等及以上）、 low （拦截低风险及以上）。 |

2. . aiTokenLimit**（**AI Token** **限流策略）**

**configData 结构：**

```json
{
  "enabled": true,
  "ruleItems": [
    {
      "limitByType": "header",
      "limitByValue": "Authorization",
      "limitKeys": [
        {
          "key": "*",
          "timeUnit": "MINUTE",
          "tokenLimit": 1000
        }
```

]

```
    }
```

]

```
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enabled | Boolean | 是 | 是否启用 Token 限流。 |
| ruleItems | Array | 否 | 限流规则列表。 |
| ruleItems[].limitByType | String | 否 | 限流条件类型： header 、 param 、 ip 等。 |
| ruleItems[].limitByValue | String | 否 | 限流条件值，如 header 名称。 |

智能体工厂 OpenTrek

| ruleItems[].limitKeys | Array | 否 | 限流键配置列表。 |
|---|---|---|---|
| ruleItems[].limitKeys[].ke y | String | 否 | 匹配的键值， * 表示所有。 |
| ruleItems[].limitKeys[].ti meUnit | String | 否 | 时间单位： SECOND 、 MINUT E 、 HOUR 、 DAY 。 |
| ruleItems[].limitKeys[].to kenLimit | Integer | 否 | 限定时间窗口内允许的 Token 数量。 |

|  | E |
|---|---|

3. . clusterQpsLimit****（集群** **QPS** **限流策略）**

**configData 结构：**

```json
{
  "enabled": true,
  "queryPerSecond": 100,
  "queryPerMinute": 5000,
  "queryPerHour": 200000,
  "queryPerDay": 4000000
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| enabled | Boolean | 是 | - | 是否启用 QPS 限流。 |
| queryPerSecond | Integer | 否 | 0 | 每秒允许的请求数（0 表示不限制）。 |
| queryPerMinute | Integer | 否 | 0 | 每分钟允许的请求数 （0 表示不限制）。 |
| queryPerHour | Integer | 否 | 0 | 每小时允许的请求数 （0 表示不限制）。 |
| queryPerDay | Integer | 否 | 0 | 每天允许的请求数（0 表示不限制）。 |

4. . allClusterLimit****（全局限流策略）**

**configData 结构：**

智能体工厂 OpenTrek

```json
{
  "enabled": true,
  "multiRuleMode": true,
  "maxConcurrentRules": 10,
  "rejectedCode": 429,
  "rejectedMsg": "Rate limit exceeded",
  "globalThresholds": [
    {
      "limitType": "ip",
      "fixedQuotaMode": false,
      "hitsAddend": {
        "base": 1
      }
    }
```

`],`

```json
  "ruleItems": [
    {
      "limitBy": "header",
      "limitByFrom": "X-User-ID",
      "limitKeys": [
        {
          "limitType": "token",
          "fixedQuotaMode": false,
          "hitsAddend": {
            "base": 1
          },
          "key": "*"
        }
```

]

```
    }
```

]

```
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| enabled | Boolean | 是 | - | 是否启用全局限流。 |
| multiRuleMode | Boolean | 否 | false | 是否启用多规则模式。 |
| maxConcurrentRul es | Integer | 否 | 10 | 最大并发规则数。 |
| rejectedCode | Integer | 否 | 429 | 限流触发时返回的 HTTP 状态码。 |
| rejectedMsg | String | 否 | Rate limit exceeded | 限流触发时的错误消息。 |
| globalThresholds | Array | 否 | - | 全局阈值配置列表。 |

智能体工厂 OpenTrek

| globalThresholds[]. limitType | String | 否 | - | 限流类型： ip 、 user 、 api key _ 等。 |  |  |
|---|---|---|---|---|---|---|
| globalThresholds[]. fixedQuotaMode | Boolean | 否 | false | 是否使用固定配额模式。 |  |  |
| globalThresholds[]. hitsAddend | Object | 否 | - | 计数增量配置。 |  |  |
| globalThresholds[]. hitsAddend.base | Integer | 否 | 1 | 基础增量值。 |  |  |
| globalThresholds[]. hitsAddend.fromHe ader | String | 否 | - | 从请求头获取增量值。 |  |  |
| ruleItems | Array | 否 | - | 限流规则列表。 |  |  |
| ruleItems[].limitBy | String | 否 | - | 限流维度： header 、 param 、 ip 等。 |  |  |
| ruleItems[].limitBy From | String | 否 | - | 限流来源字段名。 |  |  |
| ruleItems[].andMat cherConfig | Array | 否 | - | 组合匹配条件。 |  |  |
| ruleItems[].limitKe ys | Array | 否 | - | 限流键配置。 |  |  |
| ruleItems[].limitKe ys[].limitType | String | 否 | - | 限流类型： token 、 r equest 等。 |  |  |
|  |  |  |  |  | r |  |
| ruleItems[].limitKe ys[].key | String | 否 | * | 匹配的键值。 |  |  |

|  | header |  |
|---|---|---|
| param |  |  |

|  |  | token |
|---|---|---|
|  | equest |  |

5. . timeout****（超时控制策略）**

**configData 结构：**

```json
{
  "enabled": true,
  "timeout": 30
}
```

智能体工厂 OpenTrek

**参数说明：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| enabled | Boolean | 是 | - | 是否启用超时控制。 |
| timeout | Integer | 否 | 0 | 超时时间（秒），0 表示不限制。 |

6. . retry****（重试策略）**

**configData 结构：**

```json
{
  "enabled": true,
  "attempts": 2,
  "timeout": 10,
  "conditions": ["error", "timeout", "non_idempotent"],
  "httpStatusCodes": [502, 503, 504]
}
```

**参数说明：**

| 参数名 | 类型 |  |  | 必填 |  | 默认值 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| enabled | Boolean |  |  | 是 |  | - |  | 是否启用重试。 |  |  |  |
| attempts | Integer |  |  | 否 |  | 2 |  | 最大重试次数。 |  |  |  |
| timeout | Integer |  |  | 否 |  | - |  | 每次重试的超时时间 （秒）。 |  |  |  |
| conditions | String[] |  |  |  |  | ["error", |  | 重试触发条 |  |  |  |
|  |  |  |  |  |  |  | ["error", | 件： | error |  |  |
|  |  |  |  |  |  | "timeout", |  | 接错 |  |  |  |
|  |  |  |  |  |  |  |  | 误）、 |  | tim |  |
|  |  |  |  | 否 |  |  |  |  |  |  |  |
|  |  |  |  |  |  | "non idempotent"] _ |  |  |  |  |  |
| httpStatusCodes | Integer[] |  |  | 否 |  | [502, 503, 504] |  | 需要重试的 HTTP 状态码列表。 |  |  |  |

| non idempoten _ |  |
|---|---|

|  | t |
|---|---|

|  |  | [502, 503, |
|---|---|---|
|  | 504] |  |

7. . fallback****（降级策略）**

**configData 结构：**

智能体工厂 OpenTrek

```json
{
  "enabled": true,
  "fallbackStrategy": "RANDOM",
  "responseCodes": ["500", "502", "503", "504"],
  "services": [
    {
      "name": "backup-service",
      "weight": 100
    }
```

]

```
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
|---|---|---|---|---|
| enabled | Boolean | 是 | - | 是否启用降级。 |
| fallbackStrategy | String | 否 | RANDOM | 降级策略： RANDOM （随机选择）、 SEQUENCE （顺序选择）。 |
| responseCodes | String[] | 否 | - | 触发降级的响应码列表。 |
| services | Array | 否 | - | 降级目标服务列表。 |
| services[].name | String | 否 | - | 服务名称。 |
| services[].weight | Integer | 否 | 100 | 服务权重（RANDOM 模式下生效）。 |

8. . header****（请求头控制策略）**

**configData 结构：**

智能体工厂 OpenTrek

```json
{
  "enabled": true,
  "request": {
    "add": [
      {"key": "X-Custom-Header", "value": "custom-value"}
```

`],`

```json
    "set": [
      {"key": "X-Forwarded-For", "value": "10.0.0.1"}
```

`],`

```json
    "remove": ["X-Internal-Token"]
  },
  "response": {
    "add": [
      {"key": "X-API-Version", "value": "v1.0"}
```

`],`

```json
    "set": [
      {"key": "Cache-Control", "value": "no-cache"}
```

`],`

```json
    "remove": ["X-Internal-Debug"]
  }
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| enabled | Boolean | 是 | 是否启用请求头控制。 |
| request | Object | 否 | 请求头配置。 |
| request.add | Array | 否 | 要添加的请求头列表（保留原有值）。 |
| request.set | Array | 否 | 要设置的请求头列表（覆盖原有值）。 |
| request.remove | String[] | 否 | 要删除的请求头名称列表。 |
| response | Object | 否 | 响应头配置。 |
| response.add | Array | 否 | 要添加的响应头列表。 |
| response.set | Array | 否 | 要设置的响应头列表。 |
| response.remove | String[] | 否 | 要删除的响应头名称列表。 |

9. . rewrite**（**URL** **重写策略）**

**configData 结构：**

智能体工厂 OpenTrek

```json
{
  "path": "/new-path",
  "host": "new-host.example.com"
}
```

**参数说明：**

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| path | String | 否 | 重写后的路径。 |
| host | String | 否 | 重写后的主机名。 |

**重要**

此配置来自 Higress SDK 的“RewriteConfig”，具体字段可能随版本变化。
10. . aiModelParameterOverride**（**AI** **模型参数覆盖策略）**

**重要**

此策略类型的详细配置结构请参考 Higress 官方文档或联系技术支持。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | `` | 请求ID。 |
| code | integer | `` | 响应码。 |
| msg | string | `` | 响应消息。 |
| message | string | `` | 响应消息。 |
| data | string | `` | 响应数据。 |

**示例**

**请求示例**

**示例 1：配置 AI 内容安全策略**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "configType": "aiSecurity",
  "configData": {
    "enabled": true,
    "checkRequestEnabled": true,
    "checkResponseEnabled": false,
    "streamChunkSize": 100,
    "timeoutSeconds": 1,
```

`"denyMessage": "`内容不合规，无法处理`",`

```json
    "riskLevelBar": "medium"
  },
  "gwInstanceId": "higress-demo-001",
  "targetId": "model-api-001"
}
```

**示例 2：配置 Token 限流策略**

```json
Host: localhost:80 Content-Type: application/json {
  "configType": "aiTokenLimit",
  "configData": {
    "enabled": true,
    "ruleItems": [
      {
        "limitByType": "header",
        "limitByValue": "X-User-ID",
        "limitKeys": [
          {
            "key": "*",
            "timeUnit": "MINUTE",
            "tokenLimit": 5000
          }
```

]

```
      }
```

]

```json
  },
  "gwInstanceId": "higress-demo-001",
  "targetId": "model-api-001"
}
```

**示例 3：配置超时策略**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json {
  "configType": "timeout",
  "configData": {
    "enabled": true,
    "timeout": 60
  },
  "gwInstanceId": "higress-demo-001",
  "targetId": "model-api-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "model-api-001"
}
```

#### modifyModelApiStrategyConfig

**API 接口概述**

```
请求路径： /modelapi/modifyModelApiStrategyConfig
```

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| strategyConfigI d | string | body | 否 | strategy- 001 | 策略配置ID。 |
| modelApiId | string | body | 否 | modelapi- 001 | 模型API ID。 |
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |

|  |  | strategy- |
|---|---|---|
|  | 001 |  |

|  |  | modelapi- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| strategyName | string |  | body |  | 否 |  |  | ai-token- limit |  | 策略名称（插件名称）。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| config | object |  | body |  | 否 |  |  | {"enable":tr |  |  |  |
|  |  |  |  |  |  |  |  |  | {"enable":tr | 插件配置对象， |  |
|  |  |  |  |  |  |  |  | ue,"limit":10 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 字型 |  |
|  |  |  |  |  |  |  |  | 00} |  |  |  |
| rawConfig | string |  | body |  |  |  |  | enable: |  |  |  |
|  |  |  |  |  |  |  |  |  | enable: | YAML 格式的插 |  |
|  |  |  |  |  |  |  |  | true\nlimit: |  | 件配置，与 |  |
|  |  |  |  |  |  |  |  |  |  | config 二选一， |  |
|  |  |  |  |  | 否 |  |  |  |  | config 二 |  |
|  |  |  |  |  |  |  |  | 1000\nwindowS |  | 推荐使用 |  |
|  |  |  |  |  |  |  |  | ize: 3600 |  |  |  |

|  |  | ai-token- | 策 |
|---|---|---|---|
|  | limit |  |  |

**config 对象结构**

插件配置对象，字段结构根据 `strategyName` （插件类型）不同而变化。常用插件配置字段如下：

| 插件名称 | 主要配置字段 | 说明 |
|---|---|---|
| ai-statistics | enable , statisticType | AI 统计插件，用于记录 AI 调用统计信息。 |
| ai-token-limit | limit , windowSize | Token 限流插件，限制 API Token 消耗。 |
| request-validation | rules , bodySchema | 请求验证插件，校验请求参数。 |
| response-cache | cacheKey , ttl | 响应缓存插件，缓存 AI 响应结果。 |

**说明**： `config` 和 `rawConfig` 不能同时为空。推荐使用 `rawConfig` 传递完整的 YAML 格式配置，格式更
清晰易读。例如：

```
enable: true limit: 1000 windowSize: 3600
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | string | strategy-001 | 响应数据。 |

**示例**

**请求示例**

```json
POST /modelapi/modifyModelApiStrategyConfig HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "strategyConfigId": "strategyConfigId_value",
  "modelApiId": "modelApiId_value",
  "gwInstanceId": "gwInstanceId_value",
  "strategyName": "strategyName_value",
  "config": {},
  "rawConfig": "rawConfig_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### revokeModelApiGrant

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|
| authId | string | body | 是 | auth-001 | 授权ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "authId": "authId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### updateModelApi

智能体工厂 OpenTrek

**API 接口概述**

**请求方式：** `POST`
**说明**：此接口仅适用于 AI网关（Higress引擎）实例。

**请求参数**

| 参数名称 |  | 类型 |  |  |  | 位置 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gwInstanceId |  | string |  |  |  | body |  |  |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| id |  | string |  |  |  | body |  |  |  | 是 |  | modelapi- 001 |  | ID标识。 |  |
| apiName |  | string |  |  |  | body |  |  |  | 是 |  | gpt-4-api |  | API名称。 |  |
| description |  | string |  |  |  | body |  |  |  | 否 |  | GPT-4模型API 接口 |  | 描述信息。 |  |
| basePath |  | string |  |  |  | body |  |  |  | 否 |  | /v1/chat/com pletions |  | 基础路径。 |  |
| basePathRemo ve |  | boolean |  |  |  | body |  |  |  | 否 |  | false |  | 是否移除基础路径。 |  |
| methodPathList |  | ModelRouteMe thodPath[] |  |  |  | body |  |  |  |  |  | [{"path":"/v |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | [{"path":"/v |  |  |
|  |  |  | ModelRouteMe |  |  | body |  |  |  |  |  | 1/chat/comple |  |  |  |
|  |  |  |  |  |  |  | body |  |  |  |  |  |  | 方法和路径配置 |  |
|  | thodPathList | thodPath[] |  |  |  |  |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | tions","metho |  | 列表。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  | d":"POST"}] |  |  |  |
| domainNameLi st |  | string[] |  |  |  | body |  |  |  | 否 |  | ["api.exampl e.com"] |  | 域名列表。 |  |
| protocol |  | string |  |  |  | body |  |  |  | 是 |  | openai |  | 协议类型。 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | modelapi- |
|---|---|---|
|  | 001 |  |

|  |  | GPT-4模型API | 描 |
|---|---|---|---|
|  | 接口 |  |  |

|  |  | /v1/chat/com | 基础路径 |
|---|---|---|---|
|  | pletions |  |  |

|  |  | ["api.exampl | 域名列表 |
|---|---|---|---|
|  | e.com"] |  |  |

智能体工厂 OpenTrek

| sceneType | string | body | 是 | TEXT GENERAT _ ION |  | 场景类型。可选值： TEXT GEN _ ERATION （文本生成）、 IMAGE _ GENERATION （图片生成）、 VIDEO _ GENERATION （视频生成）、 SPEECH SYNTHESIS _ （语音合成）、 TEXT R _ ERANK （文本排序/Rerank）、 EMBEDDING （ 向量化）、 OTHER （其他）。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | IMAGE _ |  |  |
|  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  |  | VIDEO _ |  |  |
|  |  |  |  |  |  | GENERATION |  |  |  |
|  |  |  |  |  |  |  | SPEECH |  |  |
|  |  |  |  |  |  | SYNTHESIS _ |  |  |  |
|  |  |  |  |  | NERAT | S _ |  |  |  |
|  |  |  |  |  |  | （ |  |  |  |
| routeDispatche r | object | body | 否 |  |  | 路由分发配置。 |  |  |  |
| observationCon fig | object | body | 否 |  |  | 可观测性配置。 |  |  |  |
| fallback | object | body | 否 |  |  | 降级配置。 |  |  |  |

|  |  | TEXT GEN _ |  |
|---|---|---|---|
|  | ERATION |  |  |

**methodPathList 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| path | string | body | 否 | /v1/chat/com pletions | 路径。 |
| method | string | body | 否 | POST | HTTP方法。 |

|  |  | /v1/chat/com | 路径。 |
|---|---|---|---|
|  | pletions |  |  |

**observationConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | true | 是否启用。 |

智能体工厂 OpenTrek

| logRequestInfo | boolean | body | 否 | true | 是否记录请求信息。 |
|---|---|---|---|---|---|
| logResponseInf o | boolean | body | 否 | false | 是否记录响应信息。 |

**fallback 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | boolean | body | 否 | false | 是否启用。 |
| responseCodes | string[] | body | 否 | ["500", "503"] | 触发降级的响应码。 |
| fallbackServiceI d | string | body | 否 | fallback- service-001 | 降级服务ID。 |
| fallbackStrateg y | string | body | 否 | ratio | 降级策略。 |

| ["500", | 触 |
|---|---|

|  |  | fallback- | 降级服务I |
|---|---|---|---|
|  | service-001 |  |  |

**routeDispatcher 对象结构**

路由分发配置，根据 `strategyType` 字段值采用不同的策略类型。

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| strategyType | string | body | 是 |  | WEIGHT |  | 路由分发策略类型，可选值： WEIGHT （权重分发）、 HEADER （Header条件分发）、 WEIGHT |  |  |
|  |  |  |  |  |  |  |  | WEIGHT |  |
|  |  |  |  |  |  |  | MODEL MAPPIN _ _ |  |  |
|  |  |  |  |  |  |  | G |  |  |
|  |  |  |  |  |  |  |  | SINGLE |  |
|  |  |  |  |  |  |  | MODEL MAPPIN _ _ |  |  |
|  |  |  |  |  |  |  | G |  |  |

智能体工厂 OpenTrek

| rules | array |  | body |  |  |  |  |  | [{"weight":5 |  | 路由规则列表， |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | [{"weight":5 | 结构根据 |  |
|  |  |  |  |  |  |  |  |  | 0,"serviceId" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | strategyType 不同而变化，详 |  |
|  |  |  |  |  |  |  |  |  |  |  | 不 |  |
|  |  |  |  | body |  |  |  |  | :"service- |  | 见 |  |
|  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 001"}] |  |  |  |

**WEIGHT 策略（权重分发）：**

| 参数名称 | 类型 | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|
| rules | array | 是 |  | [{"weight":50," |  |  |  |
|  |  |  |  |  | [{"weight":50," |  |  |
|  |  |  |  | serviceId":"svc- |  |  |  |
|  |  |  |  |  |  | 权重 |  |
|  |  |  |  | 001"}] |  |  |  |
| rules[].weight | integer | 是 |  | 50 |  | 权重值（百分比）。 |  |
| rules[].serviceId | string | 是 |  | svc-001 |  | 目标服务ID。 |  |
| rules[].serviceNam e | string | 否 |  | model-service |  | 目标服务名称。 |  |

**HEADER 策略（Header条件分发）：**

| 参数名称 | 类型 |  | 是否必选 |  | 示例 |  |  |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
| rules | array |  | 是 |  | [{"headerMatch" |  |  |  |  |  |  |
|  |  |  |  |  |  | [{"headerMatch" |  |  | Header匹配规则列 |  |  |
|  |  |  |  |  | :{"model":"gpt- |  |  |  | H |  |  |
|  |  |  |  |  |  |  |  |  | 表 |  |  |
|  |  |  |  |  | 4"}}] |  |  |  |  |  |  |
| rules[].headerMatc h | object |  | 是 |  | {"model": "gpt-4"} |  |  |  | Header匹配条件，key-value 形式，如 {"model": "gpt-4"} 。 |  |  |
|  |  |  |  |  |  | {"model": |  |  | 件 |  |  |
|  |  |  |  |  |  |  |  |  |  | {"model": |  |
|  |  |  |  |  |  |  |  |  | "gpt-4"} |  |  |
| rules[].weightRuleL ist | array |  | 否 |  | [{"weight":50," |  |  |  |  |  |  |
|  |  |  |  |  |  | [{"weight":50," |  |  | 权重规则列表（匹配 |  |  |
|  |  |  |  |  | serviceId":"svc- |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 成功 |  |  |
|  |  |  |  |  | 001"}] |  |  |  |  |  |  |
| rules[].serviceId | string |  | 否 |  | svc-001 |  |  |  | 目标服务ID（已废弃，建议使用 weightRuleList）。 |  |  |

**WEIGHT_MODEL_MAPPING / SINGLE_MODEL_MAPPING 策略（权重+模型映射）：**

智能体工厂 OpenTrek

|  | 参数名称 |  |  | 类型 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | rules |  |  |  |  |  |  |  |  | [{"weight":50," |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"weight":50," |  |  |
|  |  |  |  |  |  |  |  |  |  | serviceId":"svc- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 001","modelMappin |  | 权重+模型映射规则 |  |
|  |  |  |  | array |  |  |  | 是 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | g":{"gpt- |  | 列表。 |  |
|  |  |  |  |  |  |  |  |  |  | 3.5":"gpt- |  |  |  |
|  |  |  |  |  |  |  |  |  |  | 4"}}] |  |  |  |
|  | rules[].weight |  |  | integer |  |  |  | 是 |  | 50 |  | 权重值（百分比）。 |  |
|  | rules[].serviceId |  |  | string |  |  |  | 是 |  | svc-001 |  | 目标服务ID。 |  |
|  | rules[].modelMappi ng |  |  | object |  |  |  | 否 |  | {"gpt-3.5": "gpt-4"} |  | 模型映射配置，key- value 形式，如 {"gpt-3.5": "gpt-4"} 。 |  |
|  | rules[].serviceNam e |  |  | string |  |  |  | 否 |  | model-service |  | 目标服务名称。 |  |

| {"gpt-3.5": |  |  | valu |  |
|---|---|---|---|---|
|  |  |  | "gpt-4"} |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | modelapi-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "id": "id_value",
  "apiName": "apiName_value",
  "description": "description_value",
  "basePath": "basePath_value",
  "basePathRemove": true,
  "methodPathList": [
    {
      "path": "path_value",
      "method": "method_value"
    }
```

`],`

```json
  "domainNameList": [],
  "protocol": "protocol_value",
  "sceneType": "sceneType_value",
  "routeDispatcher": {},
  "observationConfig": {
    "enable": true,
    "logRequestInfo": true,
    "logResponseInfo": true
  },
  "fallback": {
    "enable": true,
    "responseCodes": [],
    "fallbackServiceId": "fallbackServiceId_value",
    "fallbackStrategy": "fallbackStrategy_value"
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 证书

#### createCertificate

**API 接口概述**

**中文名称：**创建证书
智能体工厂 OpenTrek
**功能概述：**创建证书。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|
| certificateId | string | body |  | 否 |  | cert-001 |  | 证书ID。 |  |
| gwInstanceId | string | body |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| certificates | string | body |  | 否 |  | -----BEGIN |  |  |  |
|  |  |  |  |  |  |  | -----BEGIN | 证书内容，PEM |  |
|  |  |  |  |  |  | CERTIFICATE-- |  |  |  |
|  |  |  |  |  |  |  |  | 格式。 证书文 |  |
|  |  |  |  |  |  | ---... |  |  |  |
| privateKey | string | body |  | 否 |  | -----BEGIN |  | 私钥内容，PEM |  |
|  |  |  |  |  |  |  | -----BEGIN | 格式。仅服务端 |  |
|  |  |  |  |  |  | PRIVATE KEY-- |  |  |  |
|  |  |  |  |  |  |  |  | 证书 (cert |  |
|  |  |  |  |  |  | ---... |  |  |  |
| certificateNam e | string | body |  | 否 |  | my-cert |  | 证书名称，长度不超过15字符。 |  |
| certType | integer | body |  | 是 |  | 0 |  | 证书类型。 0 =服务端证书（SSL证书）， 1 =CA 证书（客户端认证用）。 |  |
| isImport | boolean | body |  | 否 |  | false |  | 是否为导入。 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | string | cert-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "certificateId": "certificateId_value",
  "gwInstanceId": "gwInstanceId_value",
  "certificates": "certificates_value",
  "privateKey": "privateKey_value",
  "certificateName": "certificateName_value",
  "certType": 0,
  "isImport": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteCertificate

**API 接口概述**

**中文名称：**删除证书
**功能概述：**删除证书。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| certificateId | string | body | 是 | cert-001 | 证书ID。 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | cert-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "certificateId": "certificateId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

智能体工厂 OpenTrek

#### getCertificate

**API 接口概述**

**中文名称：**查询证书详情
**功能概述：**查询证书详情。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| certificateId | string | body | 否 | cert-001 | 证书ID。 |
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.signTime | string | 2024-01-01 00:00:00 | 签发时间。 |
| data.expireTime | string | 2025-01-01 00:00:00 | 过期时间。 |
| data.algorithm | string | RSA | 加密算法。 |
| data.privateKeyLen | integer | 2048 | 私钥长度。 |

智能体工厂 OpenTrek

| data.fingerPrint | string | A1:B2:C3:D4:E5... | 指纹。 |
|---|---|---|---|
| data.snis | string[] | ["api.example.com"] | SNI列表。 |
| data.signerCN | string | Let's Encrypt | 签发者CN。 |
| data.signerOU | string | Certificate Authority | 签发者OU。 |
| data.certificateName | string | my-cert | 证书名称。 |
| data.certificateId | string | cert-001 | 证书ID。 |
| data.domainId | string | domain-001 | 域名ID。 |
| data.certType | integer | 0 | 证书类型。0=服务端证书，1=CA证书。 |
| data.SN | string | 1234567890ABCDEF | 序列号。 |

|  | ["api.example.com"] |
|---|---|

|  |  | Certificate |  |
|---|---|---|---|
|  | Authority |  |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "certificateId": "certificateId_value",
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "signTime": "signTime_value",
    "expireTime": "expireTime_value",
    "algorithm": "algorithm_value",
    "privateKeyLen": 0,
    "fingerPrint": "fingerPrint_value",
    "snis": [],
    "signerCN": "signerCN_value",
    "signerOU": "signerOU_value",
    "certificateName": "certificateName_value",
    "certificateId": "certificateId_value",
    "domainId": "domainId_value",
    "certType": 0,
    "SN": "SN_value"
  }
}
```

#### listAllCACertificates

**API 接口概述**

**中文名称：**查询所有CA证书
**功能概述：**查询所有CA证书。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| requestId | string | uuid-xxx-xxx | 请求ID。 |
|---|---|---|---|
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | ListCertificateRespo nseRecord[] | - | 响应数据。 |
| data.snis | string[] | ["api.example.com"] | SNI列表。 |
| data.expireTime | string | 2025-01-01 00:00:00 | 过期时间。 |
| data.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.certificateName | string | my-ca-cert | 证书名称。 |
| data.certificateId | string | ca-cert-001 | 证书ID。 |
| data.certType | integer | 1 | 证书类型。0=服务端证书，1=CA证书。 |

|  |  | ListCertificateRespo | - |
|---|---|---|---|
| a | nseRecord[] |  |  |

|  | ["api.example.com"] |
|---|---|

|  |  | 2025-01-01 |
|---|---|---|
|  | 00:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
POST /certificate/listAllCACertificates HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": [
        {
            "snis": [],
            "expireTime": "expireTime_value",
            "updateTime": "updateTime_value",
            "createTime": "createTime_value",
            "certificateName": "certificateName_value",
            "certificateId": "certificateId_value",
            "certType": 0
        }
```

]

```
}
```

#### listAllServerCertificates

**API 接口概述**

**中文名称：**查询所有服务端证书
**功能概述：**查询所有服务端证书。

```
请求路径： /certificate/listAllServerCertificates
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.certificateId String | String | cert-123456 | 证书 ID。 |
| data.certificateName | String | my-server-cert | 证书名称。 |
| data.domainId | String | domain-789 | 关联域名 ID。 |
| data.snis | Array<String> | ["example.com", "*.example.com"] | SNI 域名列表。 |
| data.certType | Integer | 1 | 证书类型。 |
| data.algorithm | String | RSA | 加密算法（如 RSA、 ECDSA）。 |
| data.privateKeyLen | Int | 2048 | 私钥长度（如 2048、 4096）。 |
| data.fingerPrint | String | A1:B2:C3:D4:E5:F6... | 证书指纹。 |
| data.SN | String | 01:23:45:67:89:AB:CD :EF | 序列号。 |
| data.signerCN | String | DigiCert Global Root CA | 签发者 Common Name。 |
| data.signerOU | String | www.digicert.com | 签发者 Organization Unit。 |
| data.signTime | LocalDateTime | 2024-01- 01T00:00:00 | 签发时间。 |

|  | ["example.com", | SNI 域名列表 |
|---|---|---|
| "*.example.com"] |  |  |

|  | A1:B2:C3:D4:E5:F6... |
|---|---|

|  | 01:23:45:67:89:AB:CD | 序 |
|---|---|---|
| :EF |  |  |

|  | DigiCert Global | 签 |
|---|---|---|
| Root CA |  |  |

智能体工厂 OpenTrek

| data.expireTime | LocalDateTime | 2026-12- 31T23:59:59 | 过期时间。 |
|---|---|---|---|

|  | 2026-12- |
|---|---|
| 31T23:59:59 |  |

**示例**

**请求示例**

```json
POST /certificate/listAllServerCertificates HTTP/1.1 Host: localhost:80 Content-Type: application/json {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "certificateId": "cert-123456",
    "certificateName": "my-server-cert",
    "domainId": "domain-789",
    "snis": ["example.com", "*.example.com"],
    "certType": 1,
    "algorithm": "RSA",
    "privateKeyLen": 2048,
    "fingerPrint": "A1:B2:C3:D4:E5:F6...",
    "SN": "01:23:45:67:89:AB:CD:EF",
    "signerCN": "DigiCert Global Root CA",
    "signerOU": "www.digicert.com",
    "signTime": "2024-01-01T00:00:00",
    "expireTime": "2026-12-31T23:59:59"
  }
}
```

#### listCertificates

**API 接口概述**

**中文名称：**查询证书列表
**功能概述：**查询证书列表。
**请求方式：** `POST`
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| sni | string | body | 否 | api.example. com | SNI名称。 |
| certType | integer | body | 否 | 0 | 证书类型。0=服务端证书，1=CA证书。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | api.example. | SN |
|---|---|---|---|
|  | com |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.size | integer | 10 | 每页大小。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.records | ListCertificateRespo nseRecord[] | - | 记录列表。 |

|  |  | ListCertificateRespo | - |
|---|---|---|---|
| a.records | nseRecord[] |  |  |

智能体工厂 OpenTrek

| data.records.snis | string[] | ["api.example.com"] | SNI列表。 |
|---|---|---|---|
| data.records.expireTime | string | 2025-01-01 00:00:00 | 过期时间。 |
| data.records.updateTime | string | 2024-01-02 10:00:00 | 更新时间。 |
| data.records.createTime | string | 2024-01-01 10:00:00 | 创建时间。 |
| data.records.certificateN ame | string | my-cert | 证书名称。 |
| data.records.certificateId | string | cert-001 | 证书ID。 |
| data.records.certType | integer | 0 | 证书类型。0=服务端证书，1=CA证书。 |

|  | ["api.example.com"] |
|---|---|

|  |  | 2025-01-01 |
|---|---|---|
|  | 00:00:00 |  |

|  |  | 2024-01-02 |
|---|---|---|
|  | 10:00:00 |  |

|  |  | 2024-01-01 |
|---|---|---|
|  | 10:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "size": 0,
  "current": 0,
  "sni": "sni_value",
  "certType": 0,
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "size": 0,
    "total": 0,
    "current": 0,
    "records": {
      "snis": [],
      "expireTime": "expireTime_value",
      "updateTime": "updateTime_value",
      "createTime": "createTime_value",
      "certificateName": "certificateName_value",
      "certificateId": "certificateId_value",
      "certType": 0
    }
  }
}
```

#### updateCertificate

**API 接口概述**

**中文名称：**修改证书
**功能概述：**修改证书。

```
请求路径： /certificate/modifyCertificate
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|
| certificateId | string | body |  | 否 |  | cert-001 |  | 证书ID，修改时必填。 |  |
| gwInstanceId | string | body |  | 是 |  | higress- 001 |  | 网关实例ID。 |  |
| certificates | string | body |  | 否 |  | -----BEGIN |  |  |  |
|  |  |  |  |  |  |  | -----BEGIN | 证书内容，PEM |  |
|  |  |  |  |  |  | CERTIFICATE-- |  | 证书内 |  |
|  |  |  |  |  |  |  |  | 格式。 |  |
|  |  |  |  |  |  | ---... |  |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

| privateKey | string | body |  | 否 |  | -----BEGIN |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  | -----BEGIN | 私钥内容，PEM 格式。仅服务端 |  |
|  |  |  |  |  |  | PRIVATE KEY-- |  |  |  |
|  |  |  |  |  |  |  |  | 证书 |  |
|  |  |  |  |  |  | ---... |  |  |  |
| certificateNam e | string | body |  | 否 |  | my-cert |  | 证书名称。 |  |
| certType | integer | body |  | 是 |  | 0 |  | 证书类型。 0 =服务端证书（SSL证书）， 1 =CA 证书（客户端认证用）。 |  |
| isImport | boolean | body |  | 否 |  | false |  | 是否为导入。 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | cert-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /certificate/modifyCertificate HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "certificateId": "certificateId_value",
  "gwInstanceId": "gwInstanceId_value",
  "certificates": "certificates_value",
  "privateKey": "privateKey_value",
  "certificateName": "certificateName_value",
  "certType": 0,
  "isImport": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 路由

#### batchDeletesRoutes

**API 接口概述**

**中文名称：**批量删除路由
**功能概述：**路由管理 - 批量删除路由。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 |  | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|
| gwInstanceId | string | body |  | 否 |  | higress- 001 |  | 网关实例ID。 |
| routeIds | string[] | body |  | 否 |  | ["route- |  | 路由ID列表。 |
|  |  |  |  |  |  |  | ["route- |  |
|  |  |  |  |  |  | 001", "route- |  |  |
|  |  |  |  |  |  |  |  | 路由 |
|  |  |  |  |  |  | 002"] |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.successIds | string[] | ["route-001"] | 成功删除的路由ID列表。 |
| data.failedIds | string[] | ["route-002"] | 删除失败的路由ID列表。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "routeIds": []
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "successIds": [],
    "failedIds": []
  }
}
```

智能体工厂 OpenTrek

#### createRoute

**API 接口概述**

**中文名称：**创建路由
**功能概述：**创建路由。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 |  |  | 位置 |  |  |  | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order | integer |  |  | body |  |  |  | 否 |  | 100 |  | 路由优先级顺序。 |  |
| filters | string |  |  | body |  |  |  |  |  | [{\"name\":\ |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{\"name\":\ |  |  |
|  |  |  |  |  |  |  |  |  |  | "requestHeade |  |  |  |
|  |  | string |  |  | body |  |  |  |  |  |  | 路由过滤器配 |  |
|  |  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | rModifier\"}] |  |  |  |
| routeId | string |  |  | body |  |  |  | 否 |  | route-001 |  | 路由ID。 |  |
| routeName | string |  |  | body |  |  |  | 否 |  | my-route |  | 路由名称。 |  |
| serviceId | string |  |  | body |  |  |  | 否 |  | service- 001 |  | 目标服务ID。 |  |
| serviceType | string |  |  | body |  |  |  | 否 |  | 1 |  | 服务类型。可选值： 1 （固定节点）、 2 （服务发现）。 |  |
| gwInstanceId | string |  |  | body |  |  |  | 否 |  | higress- 001 |  | 网关实例ID。 |  |
| methods | string[] |  |  | body |  |  |  | 否 |  | ["GET", "POST"] |  | HTTP方法列表， 如 GET、 POST、PUT、 DELETE。 |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | ["GET", | 如 |
|---|---|---|---|
|  | "POST"] |  |  |

智能体工厂 OpenTrek

| header | KvPair[] |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"Con |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"Con |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | tent- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Type","value" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"application |  |  |  |
|  |  |  | air[] |  |  | body |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | KvPair[] | air[] |  |  |  | body |  |  |  |  |  | 否 |  | /json"}] |  |  |  |
| cookie | KvPair[] |  |  |  |  | body |  |  |  |  |  |  | 否 |  | [{"key":"ses |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"ses | Cookie匹配规 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | sion","value" |  | Cookie匹配 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"active"}] |  |  |  |
| queryParam | KvPair[] |  |  |  |  | body |  |  |  |  |  |  | 否 |  | [{"key":"ver |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"ver | 查询参数匹配规 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | sion","value" |  | 查询参 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"v1"}] |  |  |  |
| domainIds | string[] |  |  |  |  | body |  |  |  |  |  |  | 否 |  | ["domain- 001"] |  | 关联域名ID列表。 |  |
| routePath | string[] |  |  |  |  | body |  |  |  |  |  |  | 否 |  | ["/api/v1/*" ] |  | 路由路径。 |  |
| stripPrefix | integer |  |  |  |  | body |  |  |  |  |  |  | 否 |  | 1 |  | 去除路径前缀的层数。 |  |
| requestTimeou t | integer |  |  |  |  | body |  |  |  |  |  |  | 否 |  | 30000 |  | 请求超时时间 （毫秒）。 |  |
| openStripPrefix | boolean |  |  |  |  | body |  |  |  |  |  |  | 否 |  | true |  | 是否启用去除前缀。 |  |
| enableForceNo nceCheck | boolean |  |  |  |  | body |  |  |  |  |  |  | 否 |  | false |  | enableForceNo nceCheck参数。 |  |
| path | object |  |  |  |  | body |  |  |  |  |  |  |  |  | {"matchType" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"matchType" |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"prefix","ma |  |  |  |
|  |  | object |  |  |  |  | body |  |  |  |  |  |  |  |  |  | 路由路径匹配配 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | tchValue":"/a |  | 置 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | pi"} |  |  |  |
| serviceIds | ServiceAndWe ight[] |  |  |  |  | body |  |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ":"service- |  | 多服务负载均衡 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 配置列表（带权 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  | 配置 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 001","weight" |  | 重） |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :50}] |  |  |  |

|  |  | ["domain- | 关 |
|---|---|---|---|
|  | 001"] |  |  |

|  |  | ["/api/v1/*" |  |
|---|---|---|---|
|  | ] |  |  |

|  |  | ServiceAndWe | bod |  |
|---|---|---|---|---|
|  |  |  |  | bod |
| viceIds | ight[] |  |  |  |

智能体工厂 OpenTrek

| groupId | string |  |  |  | body |  |  |  |  |  | 否 |  | group-001 |  | 分组ID。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| enableStatus | boolean |  |  |  | body |  |  |  |  |  | 否 |  | true |  | 路由是否启用。 |  |
| isDisasterReco very | boolean |  |  |  | body |  |  |  |  |  | 否 |  | false |  | 是否为容灾资源。 |  |
| disasterRecove ryServiceId | string |  |  |  | body |  |  |  |  |  | 否 |  | dr-service- 001 |  | 容灾服务ID。 |  |
| disasterRecove ryServiceIds | ServiceAndWe ight[] |  |  |  | body |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | ":"dr- |  |  |  |
|  |  |  |  |  | bod |  |  |  |  |  |  |  |  |  | 容灾服务ID列 |  |
|  |  |  |  |  |  | bod | y |  |  |  | 否 |  |  |  | 容灾服务ID列 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | service- |  | 表。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 表。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 001","weight" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | :100}] |  |  |  |
| hsfMethodMap pingConfig | object |  |  |  | body |  |  |  |  |  |  |  | {"hsfMethod" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"hsfMethod" |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | :"com.example |  | hsfMethodMap |  |
|  |  | object |  |  |  | body |  |  |  |  |  |  |  |  | pingConfig参 |  |
|  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  | pin |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | .Service:meth |  | 数。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | od"} |  |  |  |

|  |  | dr-service- | 容 |
|---|---|---|---|
|  | 001 |  |  |

**header 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 否 | Content- Type | 键名。 |
| value | string | body | 否 | application/ json | 键值。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

|  |  | application/ | 键值 |
|---|---|---|---|
|  | json |  |  |

**cookie 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 否 | Content- Type | 键名。 |
| value | string | body | 否 | application/ json | 键值。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

|  |  | application/ | 键值 |
|---|---|---|---|
|  | json |  |  |

**queryParam 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| key | string | body | 否 | Content- Type | 键名。 |
|---|---|---|---|---|---|
| value | string | body | 否 | application/ json | 键值。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

|  |  | application/ | 键值 |
|---|---|---|---|
|  | json |  |  |

**path 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| matchType | string | body | 否 | prefix | 匹配类型。 |
| matchValue | string | body | 否 | /api/v1 | 匹配值。 |
| caseSensitive | boolean | body | 否 | true | 是否区分大小写。 |

**serviceIds 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | string | body | 否 | service- 001 | 目标服务ID。 |
| weight | integer | body | 否 | 50 | 权重。 |

**disasterRecoveryServiceIds 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | string | body | 否 | service- 001 | 目标服务ID。 |
| weight | integer | body | 否 | 50 | 权重。 |

**hsfMethodMappingConfig 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|
| hsfMethod | string | body | 否 |  | com.example. |  | HSF方法名。 |
|  |  |  |  |  |  | com.example. |  |
|  |  |  |  |  | Service:metho |  |  |
|  |  |  |  |  | d |  |  |

智能体工厂 OpenTrek

|  | parameterMap |  | HsfMethodMap |  |  |  |  |  |  | 否 |  | [{"name":"pa |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  | HsfMethodMap |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | [{"name":"pa |  |  |
|  |  | ameterMap | pingConfig$Pa |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | ram1","order" |  |  |  |
|  | pingList |  |  |  |  |  |  |  |  |  |  |  |  | 参 |  |
|  |  |  | rameterMappin |  |  |  | body |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | :1}] |  |  |  |
|  |  |  | g[] |  |  |  |  |  |  |  |  |  |  |  |  |

**hsfMethodMappingConfig.parameterMappingList 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | string | body | 是 | param1 | 名称。 |
| schema | object | body | 是 | {"type":"str ing"} | 参数Schema。 |
| location | string | body | 否 | body | 参数位置。 |
| required | boolean | body | 否 | true | 是否必填。 |
| order | integer | body | 是 | 1 | 路由优先级顺序。 |

| {"type":"str | 参数S |
|---|---|

**hsfMethodMappingConfig.parameterMappingList.schema 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | string | 类型。 |
| items | object | body | 否 | {"type":"str ing"} | 数组元素类型。 |
| array | boolean | body | 否 | false | 是否为数组。 |
| primitive | boolean | body | 否 | true | 是否为基本类型。 |
| generic | boolean | body | 否 | false | 是否为泛型类型。 |

| {"type":"str | 数组 |
|---|---|

**hsfMethodMappingConfig.parameterMappingList.schema.items 对象**

**结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| type | string | body | 否 | string | 类型。 |
|---|---|---|---|---|---|
| items | object | body | 否 | {"type":"str ing"} | 数组元素类型。 |
| array | boolean | body | 否 | false | 是否为数组。 |
| primitive | boolean | body | 否 | true | 是否为基本类型。 |
| generic | boolean | body | 否 | false | 是否为泛型类型。 |

|  |  | {"type":"str | 数组 |
|---|---|---|---|
|  | ing"} |  |  |

**hsfMethodMappingConfig.parameterMappingList.schema.items.items**

**对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | string | body | 否 | string | 类型。 |
| items | object | body | 否 | {"type":"str ing"} | 数组元素类型。 |
| array | boolean | body | 否 | false | 是否为数组。 |
| primitive | boolean | body | 否 | true | 是否为基本类型。 |
| generic | boolean | body | 否 | false | 是否为泛型类型。 |

|  |  | {"type":"str | 数组 |
|---|---|---|---|
|  | ing"} |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |

智能体工厂 OpenTrek

| message | string | success | 响应消息。 |
|---|---|---|---|
| data | string | route-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "order": 0,
  "filters": "filters_value",
  "routeId": "routeId_value",
  "routeName": "routeName_value",
  "serviceId": "serviceId_value",
  "serviceType": "serviceType_value",
  "gwInstanceId": "gwInstanceId_value",
  "methods": [],
  "header": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "cookie": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "queryParam": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "domainIds": [],
  "routePath": [],
  "stripPrefix": 0,
  "requestTimeout": 0,
  "openStripPrefix": true,
  "enableForceNonceCheck": true,
  "path": {
    "matchType": "matchType_value",
    "matchValue": "matchValue_value",
    "caseSensitive": true
  },
  "serviceIds": [
    {
      "serviceId": "serviceId_value",
      "weight": 0
```

智能体工厂 OpenTrek

```
    }
```

`],`

```json
  "groupId": "groupId_value",
  "enableStatus": true,
  "isDisasterRecovery": true,
  "disasterRecoveryServiceId": "disasterRecoveryServiceId_value",
  "disasterRecoveryServiceIds": [
    {
      "serviceId": "serviceId_value",
      "weight": 0
    }
```

`],`

```json
  "hsfMethodMappingConfig": {
    "hsfMethod": "hsfMethod_value",
    "parameterMappingList": [
      {
        "name": "name_value",
        "schema": {
          "type": "type_value",
          "items": {
            "type": {},
            "items": {},
            "array": {},
            "primitive": {},
            "generic": {}
          },
          "array": true,
          "primitive": true,
          "generic": true
        },
        "location": "location_value",
        "required": true,
        "order": 0
      }
```

]

```
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### deleteRoute

**API 接口概述**

**中文名称：**删除路由
智能体工厂 OpenTrek
**功能概述：**删除路由。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 是 | route-001 | 路由ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | route-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "routeId": "routeId_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getAll

**API 接口概述**

**中文名称：**查询所有路由
**功能概述：**查询所有路由。
**请求路径：** `/route/listAllRoutes`
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| serviceType | integer | body | 否 | 1 | 服务类型。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |

智能体工厂 OpenTrek

| data | AllRouteResponse[] | - | 响应数据。 |
|---|---|---|---|
| data.routeName | string | my-route | 路由名称。 |
| data.routeId | string | route-001 | 路由ID。 |
| data.serviceId | string | service-001 | 服务ID。 |

**示例**

**请求示例**

```json
POST /route/listAllRoutes HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "serviceType": 0,
  "isDisasterRecovery": true
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": [
        {
            "routeName": "demo-route",
            "routeId": "route-001",
            "serviceId": "service-001"
        },
        {
            "routeName": "another-route",
            "routeId": "route-002",
            "serviceId": "service-002"
        }
```

]

```
}
```

#### getProtocolByRoute

**API 接口概述**

智能体工厂 OpenTrek
**中文名称：**查询路由协议
**功能概述：**查询路由协议。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |
| type | integer | body | 否 | 1 | 类型。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | HTTP | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "routeId": "routeId_value",
  "type": 0
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getRoute

**API 接口概述**

**中文名称：**查询路由详情
**功能概述：**查询路由详情。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | 见下方 | 响应数据。 |

智能体工厂 OpenTrek

|  | data.routeId |  | string |  | route-001 |  | 路由ID。 |
|---|---|---|---|---|---|---|---|
|  | data.routeName |  | string |  | my-route |  | 路由名称。 |
|  | data.enableStatus |  | boolean |  | true |  | 启用状态。 |
|  | data.routePath |  | string[] |  | ["/api/v1"] |  | 路由路径。 |
|  | data.path |  | object |  | 见下方 |  | 路径。 |
|  | data.path.matchType |  | string (枚举: |  | EXACT |  | 匹配类型。 |
|  |  |  |  | string (枚举: |  |  |  |
|  |  | atchType | RoutePredicateTypeEnum |  |  |  |  |
|  |  |  |  |  |  | EXACT |  |
|  |  |  | ) |  |  |  |  |
|  | data.path.matchValue |  | string |  | /api/v1 |  | The value to match against. |
|  | data.path.caseSensitive |  | boolean |  | true |  | Whether to match the value case-sensitively. |
|  | data.openStripPrefix |  | boolean |  | false |  | 是否启用去除前缀。 |
|  | data.stripPrefix |  | integer |  | 0 |  | 去除路径前缀层数。 |
|  | data.order |  | integer |  | 1 |  | 顺序/优先级。 |
|  | data.methods |  | string[] |  | ["GET", "POST"] |  | HTTP方法列表。 |
|  | data.header |  | KvPair[] |  | 见下方 |  | 请求头匹配规则。 |
|  | data.header.key |  | string |  | Content-Type |  | 键名。 |
|  | data.header.value |  | string |  | application/json |  | 键值。 |
|  | data.cookie |  | KvPair[] |  | 见下方 |  | Cookie匹配规则。 |
|  | data.cookie.key |  | string |  | session |  | 键名。 |
|  | data.cookie.value |  | string |  | active |  | 键值。 |

智能体工厂 OpenTrek

| data.queryParam | KvPair[] | 见下方 | 查询参数匹配规则。 |
|---|---|---|---|
| data.queryParam.key | string | version | 键名。 |
| data.queryParam.value | string | v1 | 键值。 |
| data.routeCreateTime | string | 2024-01- 01T00:00:00 | routeCreateTime字段。 |
| data.groupId | string | group-001 | 分组ID。 |
| data.groupName | string | default | groupName字段。 |
| data.basePath | string | /api | 基础路径。 |
| data.serviceName | string | my-service | 服务名称。 |
| data.serviceId | string | service-001 | 服务ID。 |
| data.serviceDescription | string | 后端服务 | serviceDescription字段。 |
| data.upstreamType | integer | 1 | 上游类型。 |
| data.upstreamTypeNam e | string | HTTP | upstreamTypeName字段。 |
| data.loadBalanceType | integer | 1 | 负载均衡算法类型。 |
| data.loadBalanceTypeNa me | string | ROUND ROBIN _ | loadBalanceTypeName字段。 |
| data.serviceCreateTime | string | 2024-01- 01T00:00:00 | serviceCreateTime字段。 |
| data.disasterRecoveryLo adBalanceType | integer | 1 | disasterRecoveryLoadBal anceType字段。 |
| data.disasterRecoveryLo adBalanceTypeName | string | ROUND ROBIN _ | disasterRecoveryLoadBal anceTypeName字段。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| data.disasterRecoverySe rviceName | string | backup-service | disasterRecoveryService Name字段。 |
|---|---|---|---|
| data.disasterRecoverySe rviceId | string | service-backup | 容灾服务ID。 |
| data.disasterRecoverySe rviceDescription | string | 容灾备份服务 | disasterRecoveryService Description字段。 |
| data.disasterRecoveryUp streamTypeName | string | HTTP | disasterRecoveryUpstrea mTypeName字段。 |
| data.disasterRecoveryUp streamType | integer | 1 | disasterRecoveryUpstrea mType字段。 |
| data.disasterRecoverySe rviceCreateTime | string | 2024-01- 01T00:00:00 | disasterRecoveryService CreateTime字段。 |
| data.isOpenFreeCert | boolean | false | isOpenFreeCert字段。 |
| data.isOpenTraffic | boolean | false | isOpenTraffic字段。 |
| data.trafficControl | object | 见下方 | trafficControl字段。 |
| data.trafficControl.id | integer | 1 | ID标识。 |
| data.trafficControl.userId | string | user-001 | 用户ID。 |
| data.trafficControl.name space | string | default | Kubernetes命名空间。 |
| data.trafficControl.routeI d | string | route-001 | 路由ID。 |
| data.trafficControl.resour ceMode | integer | 1 | resourceMode字段。 |
| data.trafficControl.thresh oldType | integer | 1 | thresholdType字段。 |
| data.trafficControl.count | number | 100 | count字段。 |
| data.trafficControl.contro lBehavior | integer | 0 | controlBehavior字段。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| data.trafficControl.interv alSec | integer | 1 | intervalSec字段。 |
|---|---|---|---|
| data.trafficControl.burst | integer | 10 | burst字段。 |
| data.trafficControl.maxQ ueueingTimeoutMs | integer | 500 | maxQueueingTimeoutMs 字段。 |
| data.trafficControl.isReq uestAttr | boolean | false | isRequestAttr字段。 |
| data.trafficControl.attrStr | object | {} | attrStr字段。 |
| data.trafficControl.attrStr .paramAttr | integer | 0 | paramAttr字段。 |
| data.trafficControl.attrStr .paramAttrDetail | string | header | paramAttrDetail字段。 |
| data.trafficControl.attrStr .isOpenMatch | integer | 0 | isOpenMatch字段。 |
| data.trafficControl.attrStr .matchMode | integer | 0 | matchMode字段。 |
| data.trafficControl.attrStr .matchString | string | api-key | matchString字段。 |
| data.trafficControl.enabl e | boolean | true | 是否启用。 |
| data.trafficControl.gwIns tanceId | string | higress-001 | 网关实例ID。 |
| data.trafficControl.create Time | string | 2024-01- 01T00:00:00 | 创建时间。 |
| data.trafficControl.updat eTime | string | 2024-01- 01T00:00:00 | 更新时间。 |
| data.trafficControl.thresh oldByQps | object | 见下方 | thresholdByQps字段。 |
| data.trafficControl.thresh oldByQps.qpsThreshold | integer | 100 | qpsThreshold字段。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| data.trafficControl.thresh oldByQps.timeInterval | integer | 1 | timeInterval字段。 |
|---|---|---|---|
| data.trafficControl.thresh oldByQps.timeUnit | integer | 1 | timeUnit字段。 |
| data.trafficControl.thresh oldByQps.flowControlMet hod | integer | 0 | flowControlMethod字段。 |
| data.trafficControl.thresh oldByQps.flowControlInfo | integer | 0 | flowControlInfo字段。 |
| data.trafficControl.thresh oldByThreadVo | object | 见下方 | thresholdByThreadVo字段。 |
| data.trafficControl.thresh oldByThreadVo.threadNu m | integer | 10 | threadNum字段。 |
| data.isOpenMock | boolean | false | isOpenMock字段。 |
| data.routeMockConfigVo | object | 见下方 | routeMockConfigVo字段。 |
| data.routeMockConfigVo. isOpen | integer | 0 | isOpen字段。 |
| data.routeMockConfigVo. responseBody | string | {} | responseBody字段。 |
| data.routeMockConfigVo. responseHeader | string[] | [] | responseHeader字段。 |
| data.routeMockConfigVo. responseCode | integer | 200 | responseCode字段。 |
| data.isOpenTimeOut | boolean | true | isOpenTimeOut字段。 |
| data.requestTimeout | integer | 30000 | 请求超时时间（毫秒）。 |
| data.isOpenPlugin | boolean | false | isOpenPlugin字段。 |
| data.plugins | KvPair[] | 见下方 | plugins字段。 |

智能体工厂 OpenTrek

| data.plugins.key | string | ai-token-limit | 键名。 |
|---|---|---|---|
| data.plugins.value | string | {} | 键值。 |
| data.isOpenFuse | boolean | false | isOpenFuse字段。 |
| data.routeFusesConfigVo | object | 见下方 | routeFusesConfigVo字段。 |
| data.routeFusesConfigVo .resourceId | string | route-001 | resourceId字段。 |
| data.routeFusesConfigVo .combinedCondition | string | OR | combinedCondition字段。 |
| data.routeFusesConfigVo .routeFusesCondition | RouteFuseVo[] | 见下方 | routeFusesCondition字段。 |
| data.routeFusesConfigVo .routeFusesCondition.id | integer | 1 | ID标识。 |
| data.routeFusesConfigVo .routeFusesCondition.typ e | integer | 1 | 类型。 |
| data.routeFusesConfigVo .routeFusesCondition.op erator | string | >= | operator字段。 |
| data.routeFusesConfigVo .routeFusesCondition.jud gValue | string | 500 | judgValue字段。 |
| data.routeFusesConfigVo .routeFusesCondition.err orCount | number | 5 | errorCount字段。 |
| data.routeFusesConfigVo .routeFusesCondition.sta tInterval | integer | 10 | statInterval字段。 |
| data.routeFusesConfigVo .routeFusesCondition.tim eWindow | integer | 30 | timeWindow字段。 |
| data.routeFusesConfigVo .routeFusesCondition.mi nRequestAmount | integer | 10 | minRequestAmount字段。 |

智能体工厂 OpenTrek

| data.routeFusesConfigVo .routeFusesCondition.hal fOpenBaseAmountPerSte p | integer | 5 | halfOpenBaseAmountPer Step字段。 |
|---|---|---|---|
| data.routeFusesConfigVo .routeFusesCondition.hal fOpenRecoveryStepNum | integer | 3 | halfOpenRecoveryStepN um字段。 |
| data.routeFusesConfigVo .degradeStrategy | integer | 0 | degradeStrategy字段。 |
| data.routeFusesConfigVo .fuseMock | object | 见下方 | fuseMock字段。 |
| data.routeFusesConfigVo .fuseMock.isOpen | integer | 0 | isOpen字段。 |
| data.routeFusesConfigVo .fuseMock.responseBody | string | {} | responseBody字段。 |
| data.routeFusesConfigVo .fuseMock.responseHead er | string[] | [] | responseHeader字段。 |
| data.routeFusesConfigVo .fuseMock.responseCode | integer | 503 | responseCode字段。 |
| data.isOpenSig | boolean | false | isOpenSig字段。 |
| data.sigSchemeDTOList | SigSchemeRouteRelDet ail[] | 见下方 | sigSchemeDTOList字段。 |
| data.sigSchemeDTOList. sigSchemeStatus | integer | 1 | sigSchemeStatus字段。 |
| data.sigSchemeDTOList. sigSchemeName | string | default-sig | sigSchemeName字段。 |
| data.sigSchemeDTOList. sigSchemeId | string | sig-001 | sigSchemeId字段。 |
| data.sigSchemeDTOList. sigAlg | string | HMAC-SHA256 | sigAlg字段。 |
| data.sigSchemeDTOList. secretKey | string | secret-key-xxx | SecretKey. |

|  |  | SigSchemeRouteRelDet | 见下 |
|---|---|---|---|
| a.sigSchemeDTOList | ail[] |  |  |

智能体工厂 OpenTrek

| data.routeAuthVO | object | 见下方 | routeAuthVO字段。 |
|---|---|---|---|
| data.routeAuthVO.reque stHeader | string | X-API-Key | requestHeader字段。 |
| data.routeAuthVO.authT ype | integer | 1 | 认证类型。0=无认证，1=Key Auth，2=Basic Auth，3=JWT，4=OAuth 2。 |
| data.routeAuthVO.custo mAuth | object | 见下方 | customAuth字段。 |
| data.routeAuthVO.custo mAuth.authRequestHead er | string[] | [] | authRequestHeader字段。 |
| data.routeAuthVO.custo mAuth.authResponseHea der | string[] | [] | authResponseHeader字段。 |
| data.routeAuthVO.custo mAuth.authServerHost | string | auth.example.com | authServerHost字段。 |
| data.routeAuthVO.custo mAuth.authServerUri | string | /auth | authServerUri字段。 |
| data.routeAuthVO.custo mAuth.authTimeout | integer | 5000 | authTimeout字段。 |
| data.routeAuthVO.custo mAuth.keepAlive | integer | 60 | keepAlive字段。 |
| data.routeAuthVO.custo mAuth.tokenExpiration | integer | 3600 | tokenExpiration字段。 |
| data.routeAuthVO.custo mAuth.authAssertType | string | header | authAssertType字段。 |
| data.routeAuthVO.custo mAuth.authAssertValue | string | X-Auth-Token | authAssertValue字段。 |
| data.routeAuthVO.custo mAuth.openLoosePattern | boolean | false | openLoosePattern字段。 |
| data.routeAuthVO.custo mAuth.cachedClient | object | {} | cachedClient字段。 |

智能体工厂 OpenTrek

| data.routeAuthVO.apiKey | object | 见下方 | apiKey字段。 |
|---|---|---|---|
| data.routeAuthVO.apiKey .enableInHeader | boolean | true | enableInHeader字段。 |
| data.routeAuthVO.apiKey .enableInQuery | boolean | false | enableInQuery字段。 |
| data.routeAuthVO.apiKey .apiKeyName | string | X-API-Key | apiKeyName字段。 |
| data.routeAuthVO.apiKey .enableRmParam | boolean | false | enableRmParam字段。 |
| data.routeAuthVO.apiKey .enableOptionsFreeAuth | boolean | true | enableOptionsFreeAuth 字段。 |
| data.routeAuthVO.appCo deAuthType | string | HEADER | appCodeAuthType字段。 |
| data.isRewrite | boolean | false | isRewrite字段。 |
| data.isOpenCross | boolean | false | isOpenCross字段。 |
| data.isOpenResponseCac he | boolean | false | isOpenResponseCache字段。 |
| data.crossConfig | object | 见下方 | crossConfig字段。 |
| data.crossConfig.isOpen Cross | boolean | false | isOpenCross字段。 |
| data.crossConfig.crossTy pe | string | ALL | crossType字段。 |
| data.crossConfig.allowed Origins | string | * | allowedOrigins字段。 |
| data.crossConfig.allowed Methods | string[] | ["GET", "POST"] | allowedMethods字段。 |
| data.crossConfig.expose dHeaders | string | X-Custom-Header | exposedHeaders字段。 |
| data.crossConfig.allowed Headers | string | Content-Type | allowedHeaders字段。 |

智能体工厂 OpenTrek

| data.crossConfig.allowed Credentials | boolean | true | allowedCredentials字段。 |
|---|---|---|---|
| data.crossConfig.maxAg e | integer | 3600 | maxAge字段。 |
| data.crossConfig.callbac kFunc | string | corsCallback | callbackFunc字段。 |
| data.responseCacheConf ig | object | 见下方 | responseCacheConfig字段。 |
| data.responseCacheConf ig.maxAge | integer | 3600 | maxAge字段。 |
| data.responseCacheConf ig.isOpenCacheControl | boolean | true | isOpenCacheControl字段。 |
| data.responseCacheConf ig.allowedStatusCode | string | 200,301 | allowedStatusCode字段。 |
| data.responseCacheConf ig.routeInterfaceList | RouteInterface[] | 见下方 | routeInterfaceList字段。 |
| data.responseCacheConf ig.routeInterfaceList.met hod | string | GET | HTTP方法。 |
| data.responseCacheConf ig.routeInterfaceList.hea ders | string | Content-Type | headers字段。 |
| data.responseCacheConf ig.routeInterfaceList.path | string | /api/v1 | 路径。 |
| data.responseCacheConf ig.routeInterfaceList.quer yParams | string | version | queryParams字段。 |
| data.responseCacheConf ig.isOpenResponseCache | boolean | false | isOpenResponseCache字段。 |
| data.routeIpBlockConfigV O | object | 见下方 | routeIpBlockConfigVO字段。 |
| data.routeIpBlockConfigV O.ipBlockRules | IpBlockRule[] | 见下方 | ipBlockRules字段。 |

智能体工厂 OpenTrek

| data.routeIpBlockConfigV O.ipBlockRules.ip | string | 192.168.1.100 | IP地址。 |
|---|---|---|---|
| data.routeIpBlockConfigV O.ipBlockRules.policy | string | BLOCK | policy字段。 |
| data.routeIpBlockConfigV O.isOpenIpBlock | boolean | false | isOpenIpBlock字段。 |
| data.domainVO | RouteDomains[] | 见下方 | domainVO字段。 |
| data.domainVO.domainI d | string | domain-001 | 域名ID。 |
| data.domainVO.domain | string | api.example.com | 域名。 |
| data.domainVO.protocol | string | HTTPS | 协议类型。 |
| data.domainVO.createTi me | string | 2024-01- 01T00:00:00 | 创建时间。 |
| data.domainVO.defaultD omain | boolean | false | defaultDomain字段。 |
| data.groupDomainVO | RouteDomains[] | 见下方 | groupDomainVO字段。 |
| data.groupDomainVO.do mainId | string | domain-001 | 域名ID。 |
| data.groupDomainVO.do main | string | api.example.com | 域名。 |
| data.groupDomainVO.pr otocol | string | HTTPS | 协议类型。 |
| data.groupDomainVO.cre ateTime | string | 2024-01- 01T00:00:00 | 创建时间。 |
| data.groupDomainVO.de faultDomain | boolean | false | defaultDomain字段。 |
| data.routeACLConfig | object | 见下方 | routeACLConfig字段。 |
| data.routeACLConfig.acl Rules | ACLRule[] | 见下方 | aclRules字段。 |

智能体工厂 OpenTrek

| data.routeACLConfig.acl Rules.group | string | group-001 | group字段。 |
|---|---|---|---|
| data.routeACLConfig.acl Rules.policy | string | ALLOW | policy字段。 |
| data.routeACLConfig.isE nableACL | boolean | false | isEnableACL字段。 |
| data.routeTracingConfig | object | 见下方 | routeTracingConfig字段。 |
| data.routeTracingConfig. traceHeader | string | X-Trace-Id | traceHeader字段。 |
| data.routeTracingConfig. isEnableDownstream | boolean | true | isEnableDownstream字段。 |
| data.routeTracingConfig. isEnableTracing | boolean | false | isEnableTracing字段。 |
| data.strategyConfigs | StrategyConfigRelati on[] | 见下方 | strategyConfigs字段。 |
| data.strategyConfigs.stra tegyConfigId | string | strategy-001 | strategyConfigId字段。 |
| data.strategyConfigs.stra tegyConfigName | string | ai-token-limit | strategyConfigName字段。 |
| data.strategyConfigs.stra tegyName | string | ai-token-limit | strategyName字段。 |
| data.strategyConfigs.stat us | boolean | true | 状态。 |
| data.strategyConfigs.sco pes | string[] | ["route"] | OAuth2授权范围。 |
| data.strategyConfigs.sco pe | object | 见下方 | scope字段。 |
| data.strategyConfigs.sco pe.routeInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | 见下方 | routeInfos字段。 |
| data.strategyConfigs.sco pe.routeInfos.name | string | my-route | 名称。 |

|  |  | StrategyConfigRelati | 见下 |
|---|---|---|---|
| a.strategyConfigs | on[] |  |  |

|  |  | StrategyConfigScopeD | 见下方 |
|---|---|---|---|
| routeInfos | TO$ScopeTargetDTO[] |  |  |

智能体工厂 OpenTrek

| data.strategyConfigs.sco pe.routeInfos.id | string | route-001 | ID标识。 |
|---|---|---|---|
| data.strategyConfigs.sco pe.serviceInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | 见下方 | serviceInfos字段。 |
| data.strategyConfigs.sco pe.serviceInfos.name | string | my-service | 名称。 |
| data.strategyConfigs.sco pe.serviceInfos.id | string | service-001 | ID标识。 |
| data.strategyConfigs.sco pe.appInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | 见下方 | appInfos字段。 |
| data.strategyConfigs.sco pe.appInfos.name | string | my-app | 名称。 |
| data.strategyConfigs.sco pe.appInfos.id | string | app-001 | ID标识。 |
| data.strategyConfigs.sco pe.domainInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | 见下方 | domainInfos字段。 |
| data.strategyConfigs.sco pe.domainInfos.name | string | api.example.com | 名称。 |
| data.strategyConfigs.sco pe.domainInfos.id | string | domain-001 | ID标识。 |
| data.strategyConfigs.sco pe.mcpServerInfos | StrategyConfigScopeD TO$ScopeTargetDTO[] | 见下方 | mcpServerInfos字段。 |
| data.strategyConfigs.sco pe.mcpServerInfos.name | string | my-mcp-server | 名称。 |
| data.strategyConfigs.sco pe.mcpServerInfos.id | string | mcp-001 | ID标识。 |
| data.strategyConfigs.sco pe.scopes | string[] | ["route"] | OAuth2授权范围。 |
| data.strategyConfigs.cre ateTime | string | 2024-01- 01T00:00:00 | 创建时间。 |

|  |  | StrategyConfigScopeD | 见下方 |
|---|---|---|---|
| serviceInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | 见下方 |
|---|---|---|---|
| appInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | 见下方 |
|---|---|---|---|
| domainInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | StrategyConfigScopeD | 见下方 |
|---|---|---|---|
| mcpServerInfos | TO$ScopeTargetDTO[] |  |  |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

智能体工厂 OpenTrek

| data.strategyConfigs.upd ateTime | string | 2024-01- 01T00:00:00 | 更新时间。 |
|---|---|---|---|
| data.serviceType | string | HTTP | 服务类型。 |
| data.serviceIds | object[] | 见下方 | 服务ID列表（带权重）。 |
| data.disasterRecoverySe rviceIds | object[] | 见下方 | 容灾服务ID列表。 |

|  |  | 2024-01- |
|---|---|---|
|  | 01T00:00:00 |  |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "higress-001",
  "routeId": "route-001"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": {
    "routeId": "route-001",
    "routeName": "my-route",
    "enableStatus": true,
    "routePath": ["/api/v1"],
    "path": {
      "matchType": "EXACT",
      "matchValue": "/api/v1",
      "caseSensitive": true
    },
    "order": 1,
    "methods": ["GET", "POST"],
    "serviceName": "my-service",
    "serviceId": "service-001",
    "isOpenTimeOut": true,
    "requestTimeout": 30000
  }
}
```

智能体工厂 OpenTrek

#### getRoutePolicies

**API 接口概述**

**中文名称：**查询路由策略
**功能概述：**查询路由策略。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.rewrite | object | - | 重写配置。 |
| data.rewrite.enabled | boolean | true | 是否启用重写。 |
| data.rewrite.path | string | /api/v2/test | 重写路径。 |
| data.rewrite.host | string | api.example.com | 重写主机。 |
| data.headerControl | object | - | 请求头控制配置。 |

智能体工厂 OpenTrek

| data.headerControl.enab led |  |  |  | boolean |  |  |  |  |  | true |  | 是否启用请求头控制。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| data.headerControl.requ est |  |  |  | object |  |  |  |  |  | - |  | 请求头配置。 |  |
| data.headerControl.requ est.add |  |  |  | Header[] |  |  |  |  |  | [{"key":"X- |  | 添加的请求头。 |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"key":"X- |  |  |
|  |  |  |  |  |  |  |  |  |  | Custom","value":"value |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 添加 |  |
|  |  |  |  |  |  |  |  |  |  | 1"}] |  |  |  |
| data.headerControl.requ est.add.key |  |  |  | string |  |  |  |  |  | X-Custom |  | 请求头键名。 |  |
| data.headerControl.requ est.add.value |  |  |  | string |  |  |  |  |  | value1 |  | 请求头键值。 |  |
| data.headerControl.requ est.set |  |  |  | Header[] |  |  |  |  |  | [{"key":"Content- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"key":"Content- |  |  |
|  |  |  |  |  | Head | er[] |  |  |  | Type","value":"applica |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 设置的请求头。 |  |
|  |  |  |  |  |  |  |  |  |  | tion/json"}] |  |  |  |
| data.headerControl.requ est.set.key |  |  |  | string |  |  |  |  |  | Content-Type |  | 请求头键名。 |  |
| data.headerControl.requ est.set.value |  |  |  | string |  |  |  |  |  | application/json |  | 请求头键值。 |  |
| data.headerControl.requ est.remove |  |  |  | string[] |  |  |  |  |  | ["X-Remove"] |  | 移除的请求头。 |  |
| data.headerControl.resp onse |  |  |  | object |  |  |  |  |  | - |  | 响应头配置。 |  |
| data.headerControl.resp onse.add |  |  |  | Header[] |  |  |  |  |  | [{"key":"X- |  | 添加的响应头。 |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"key":"X- |  |  |
|  |  |  |  |  |  |  |  |  |  | Response","value":"val |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 添加的 |  |
|  |  |  |  |  |  |  |  |  |  | ue1"}] |  |  |  |
| data.headerControl.resp onse.add.key |  |  |  | string |  |  |  |  |  | X-Response |  | 响应头键名。 |  |
| data.headerControl.resp onse.add.value |  |  |  | string |  |  |  |  |  | value1 |  | 响应头键值。 |  |
| data.headerControl.resp onse.set |  |  |  | Header[] |  |  |  |  |  | [{"key":"Cache- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [{"key":"Cache- |  |  |
|  |  |  |  |  | Header |  | [] |  |  | Control","value":"no- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  | 设置的响 |  |
|  |  |  |  |  |  |  |  |  |  | cache"}] |  |  |  |

智能体工厂 OpenTrek

|  | data.headerControl.resp onse.set.key |  | string |  | Cache-Control |  |  | 响应头键名。 |
|---|---|---|---|---|---|---|---|---|
|  | data.headerControl.resp onse.set.value |  | string |  | no-cache |  |  | 响应头键值。 |
|  | data.headerControl.resp onse.remove |  | string[] |  | ["X-Powered-By"] |  |  | 移除的响应头。 |
|  | data.timeoutConfig |  | object |  | - |  |  | 超时配置。 |
|  | data.timeoutConfig.enab led |  | boolean |  | true |  |  | 是否启用。 |
|  | data.timeoutConfig.time out |  | integer |  | 30 |  |  | 超时时间（秒）。 |
|  | data.retryConfig |  | object |  | - |  |  | 重试配置。 |
|  | data.retryConfig.enabled |  | boolean |  | true |  |  | 是否启用。 |
|  | data.retryConfig.attempt s |  | integer |  | 3 |  |  | 重试次数。 |
|  | data.retryConfig.timeout |  | integer |  | 5 |  |  | 重试超时时间（秒）。 |
|  | data.retryConfig.conditio ns |  | string[] |  | ["error","timeout"] |  |  | 重试条件。 |
|  | data.retryConfig.httpStat usCodes |  | integer[] |  | [500,502,503] |  |  | 重试HTTP状态码。 |
|  | data.fallbackConfig |  | object |  | - |  |  | 降级配置。 |
|  | data.fallbackConfig.enab led |  | boolean |  | true |  |  | 是否启用降级。 |
|  | data.fallbackConfig.fallba |  | string (枚举: |  | modelFallback |  |  | 降级策略。 |
|  |  |  |  | string (枚举: |  |  |  |  |
|  |  | kConfig.fallba | AiRouteFallbackStrateg |  |  |  |  |  |
|  |  |  |  |  |  |  | modelFallback |  |
|  | ckStrategy |  |  |  |  |  |  |  |
|  |  |  | y) |  |  |  |  |  |
|  | data.fallbackConfig.resp onseCodes |  | string[] |  | ["500","502"] |  |  | 需要降级的响应码。 |

|  | ["error","timeout"] |
|---|---|

智能体工厂 OpenTrek

| data.fallbackConfig.servi ces | UpstreamService[] | - | 上游服务列表。 |
|---|---|---|---|
| data.fallbackConfig.servi ces.name | string | fallback-service | 服务名称。 |
| data.fallbackConfig.servi ces.port | integer | 8080 | 服务端口。 |
| data.fallbackConfig.servi ces.version | string | v1 | 服务版本。 |
| data.fallbackConfig.servi ces.weight | integer | 100 | 服务权重。 |
| data.fallbackConfig.servi ces.bizId | string | biz-001 | 业务ID。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value",
  "routeId": "routeId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "rewrite": {
      "enabled": true,
      "path": "path_value",
      "host": "host_value"
    },
    "headerControl": {
      "enabled": true,
      "request": {
        "add": {
          "key": {},
          "value": {}
```

智能体工厂 OpenTrek

```json
        },
        "set": {
          "key": {},
          "value": {}
        },
        "remove": []
      },
      "response": {
        "add": {
          "key": {},
          "value": {}
        },
        "set": {
          "key": {},
          "value": {}
        },
        "remove": []
      }
    },
    "timeoutConfig": {
      "enabled": true,
      "timeout": 0
    },
    "retryConfig": {
      "enabled": true,
      "attempts": 0,
      "timeout": 0,
      "conditions": [],
      "httpStatusCodes": []
    },
    "fallbackConfig": {
      "enabled": true,
      "fallbackStrategy": "fallbackStrategy_value",
      "responseCodes": [],
      "services": {
        "name": "name_value",
        "port": 0,
        "version": "version_value",
        "weight": 0,
        "bizId": "bizId_value"
      }
    }
  }
}
```

#### listRoutes

**API 接口概述**

**中文名称：**查询路由列表
**功能概述：**查询路由列表。
**请求方式：** `POST`
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| size | integer | body | 是 | 10 | 每页大小。 |
| current | integer | body | 是 | 1 | 当前页码。 |
| routeName | string | body | 否 | my-route | 路由名称。 |
| serviceName | string | body | 否 | my- service | 服务名称。 |
| exactServiceId | string | body | 否 | service- 001 | 精确服务ID。 |
| enableStatus | boolean | body | 否 | true | 启用状态。 |
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |
| groupName | string | body | 否 | DEFAULT GROU _ P | 分组名称。 |
| domainName | string | body | 否 | api.example. com | 域名名称。 |
| isDisasterReco very | boolean | body | 否 | false | 是否为容灾资源。 |
| routePath | string | body | 否 | /api/v1/test | 路由路径。 |

|  |  | my- |
|---|---|---|
|  | service |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | DEFAULT GROU _ |  |
|---|---|---|---|
|  | P |  |  |

|  |  | api.example. | 域 |
|---|---|---|---|
|  | com |  |  |

|  |  | /api/v1/test |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

|  | msg |  | string |  | success |  | 响应消息。 |
|---|---|---|---|---|---|---|---|
|  | message |  | string |  | success |  | 响应消息。 |
|  | data |  | object |  | - |  | 响应数据。 |
|  | data.size |  | integer |  | 10 |  | 每页大小。 |
|  | data.total |  | integer |  | 100 |  | 总数。 |
|  | data.current |  | integer |  | 1 |  | 当前页码。 |
|  | data.records |  | GetRoutesByPageRespo nseRecord[] |  | - |  | 记录列表。 |
|  | data.records.routeId |  | string |  | route-001 |  | 路由ID。 |
|  | data.records.routeName |  | string |  | my-route |  | 路由名称。 |
|  | data.records.enableStatu s |  | boolean |  | true |  | 启用状态。 |
|  | data.records.routePath |  | string[] |  | ["/api/v1/test"] |  | 路由路径。 |
|  | data.records.path |  | object |  | - |  | 路径配置。 |
|  | data.records.path.match |  | string (枚举: |  | EXACT |  | 匹配类型。 |
|  |  |  |  | string (枚举: |  |  |  |
|  |  | s.path.match | RoutePredicateTypeEnum |  |  |  |  |
|  |  |  |  |  |  | EXACT |  |
|  | Type |  |  |  |  |  |  |
|  |  |  | ) |  |  |  |  |
|  | data.records.path.match Value |  | string |  | /api/v1/test |  | 匹配值。 |
|  | data.records.path.caseS ensitive |  | boolean |  | true |  | 是否区分大小写。 |
|  | data.records.createTime |  | string |  | 2024-01-01 10:00:00 |  | 创建时间。 |
|  | data.records.serviceId |  | string |  | service-001 |  | 服务ID。 |

|  |  | GetRoutesByPageRespo | - |
|---|---|---|---|
| a.records | nseRecord[] |  |  |

智能体工厂 OpenTrek

| data.records.serviceType | string | HTTP | 服务类型。 |
|---|---|---|---|
| data.records.serviceIds | object[] | [{"id":"service- 001","weight":100}] | 服务ID列表（带权重）。 |
| data.records.disasterRec overyServiceId | string | service-dr-001 | 容灾服务ID。 |
| data.records.serviceNam e | string | my-service | 服务名称。 |
| data.records.groupId | string | group-001 | 分组ID。 |
| data.records.groupName | string | DEFAULT GROUP _ | 分组名称。 |
| data.records.domains | string[] | ["api.example.com"] | 域名列表。 |

|  | [{"id":"service- | 服务ID列表（带权 |
|---|---|---|
| 001","weight":100}] |  |  |

|  | ["api.example.com"] |
|---|---|

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "size": 0,
  "current": 0,
  "routeName": "routeName_value",
  "serviceName": "serviceName_value",
  "exactServiceId": "exactServiceId_value",
  "enableStatus": true,
  "gwInstanceId": "gwInstanceId_value",
  "routeId": "routeId_value",
  "groupName": "groupName_value",
  "domainName": "domainName_value",
  "isDisasterRecovery": true,
  "routePath": "routePath_value"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "size": 0,
    "total": 0,
    "current": 0,
    "records": {
      "routeId": "routeId_value",
      "routeName": "routeName_value",
      "enableStatus": true,
      "routePath": [],
      "path": {
        "matchType": "matchType_value",
        "matchValue": "matchValue_value",
        "caseSensitive": true
      },
      "createTime": "createTime_value",
      "serviceId": "serviceId_value",
      "serviceType": "serviceType_value",
      "serviceIds": [],
      "disasterRecoveryServiceId": "disasterRecoveryServiceId_value",
      "serviceName": "serviceName_value",
      "groupId": "groupId_value",
      "groupName": "groupName_value",
      "domains": []
    }
  }
}
```

#### modifyRoute

**API 接口概述**

**中文名称：**修改路由
**功能概述：**修改路由。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| order | integer | body | 否 | 100 | 顺序/优先级。 |

智能体工厂 OpenTrek

| filters | string |  |  |  | body |  |  |  |  |  |  |  | [{\"name\":\ |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{\"name\":\ |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | "requestHeade |  |  |  |
|  |  | string |  |  |  | body |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | rModifier\"}] |  |  |  |
| routeId | string |  |  |  | body |  |  |  |  |  | 否 |  | route-001 |  | 路由ID。 |  |
| routeName | string |  |  |  | body |  |  |  |  |  | 否 |  | my-route- updated |  | 路由名称。 |  |
| serviceId | string |  |  |  | body |  |  |  |  |  | 否 |  | service- 001 |  | 服务ID。 |  |
| serviceType | string |  |  |  | body |  |  |  |  |  | 否 |  | 1 |  | 服务类型。 |  |
| gwInstanceId | string |  |  |  | body |  |  |  |  |  | 否 |  | higress- 001 |  | 网关实例ID。 |  |
| methods | string[] |  |  |  | body |  |  |  |  |  | 否 |  | ["GET", "POST"] |  | HTTP方法列表。 |  |
| header | KvPair[] |  |  |  | body |  |  |  |  |  |  |  | [{"key":"Con |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"Con |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | tent- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  | 请求头匹配规 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | Type","value" |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | :"application |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | /json"}] |  |  |  |
| cookie | KvPair[] |  |  |  | body |  |  |  |  |  | 否 |  | [{"key":"ses |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"ses | Cookie匹配规 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | sion","value" |  | Cookie匹配 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | :"active"}] |  |  |  |
| queryParam | KvPair[] |  |  |  | body |  |  |  |  |  | 否 |  | [{"key":"ver |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"key":"ver | 查询参数匹配规 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | sion","value" |  | 查询参 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 则。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | :"v1"}] |  |  |  |
| domainIds | string[] |  |  |  | body |  |  |  |  |  | 否 |  | ["domain- 001"] |  | 域名ID列表。 |  |
| routePath | string[] |  |  |  | body |  |  |  |  |  | 否 |  | ["/api/v1/*" ] |  | 路由路径。 |  |
| stripPrefix | integer |  |  |  | body |  |  |  |  |  | 否 |  | 1 |  | 去除路径前缀层数。 |  |

|  |  | my-route- | 路由 |
|---|---|---|---|
|  | updated |  |  |

|  |  | service- |
|---|---|---|
|  | 001 |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

|  |  | ["GET", | HT |
|---|---|---|---|
|  | "POST"] |  |  |

|  |  | ["domain- | 域 |
|---|---|---|---|
|  | 001"] |  |  |

|  |  | ["/api/v1/*" |  |
|---|---|---|---|
|  | ] |  |  |

智能体工厂 OpenTrek

| requestTimeou t | integer |  |  |  |  | body |  |  |  |  |  |  | 否 |  | 30000 |  | 请求超时时间 （毫秒）。 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openStripPrefix | boolean |  |  |  |  | body |  |  |  |  |  |  | 否 |  | true |  | 是否启用去除前缀。 |  |
| enableForceNo nceCheck | boolean |  |  |  |  | body |  |  |  |  |  |  | 否 |  | false |  | enableForceNo nceCheck参数。 |  |
| path | object |  |  |  |  | body |  |  |  |  |  |  |  |  | {"matchType" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | {"matchType" |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :"prefix","ma |  |  |  |
|  |  | object |  |  |  |  | body |  |  |  |  |  |  |  |  |  | 路径。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  | 路径 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | tchValue":"/a |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | pi"} |  |  |  |
| serviceIds | ServiceAndWe ight[] |  |  |  |  | body |  |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ":"service- |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 服务ID列表（带 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | 否 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 001","weight" |  | 权重 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :50}] |  |  |  |
| disasterRecove ryServiceId | string |  |  |  |  | body |  |  |  |  |  |  | 否 |  | dr-service- 001 |  | 容灾服务ID。 |  |
| disasterRecove ryServiceIds | ServiceAndWe ight[] |  |  |  |  | body |  |  |  |  |  |  |  |  | [{"serviceId |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | [{"serviceId |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ":"dr- |  |  |  |
|  |  |  |  |  |  | bod |  |  |  |  |  |  |  |  |  |  | 容灾服务ID列 |  |
|  |  |  |  |  |  |  | bod | y |  |  |  |  | 否 |  |  |  | 容灾服务ID列 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | service- |  | 表。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 表。 |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 001","weight" |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :100}] |  |  |  |

|  |  | ServiceAndWe | bod |  |
|---|---|---|---|---|
|  |  |  |  | bod |
| viceIds | ight[] |  |  |  |

|  |  | dr-service- | 容 |
|---|---|---|---|
|  | 001 |  |  |

**header 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 否 | Content- Type | 键名。 |
| value | string | body | 否 | application/ json | 键值。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

|  |  | application/ | 键值 |
|---|---|---|---|
|  | json |  |  |

**cookie 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 否 | Content- Type | 键名。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

智能体工厂 OpenTrek

| value | string | body | 否 | application/ json | 键值。 |
|---|---|---|---|---|---|

|  |  | application/ |  |
|---|---|---|---|
|  | json |  |  |

**queryParam 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| key | string | body | 否 | Content- Type | 键名。 |
| value | string | body | 否 | application/ json | 键值。 |

|  |  | Content- |
|---|---|---|
|  | Type |  |

|  |  | application/ | 键值 |
|---|---|---|---|
|  | json |  |  |

**path 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| matchType | string | body | 否 | prefix | 匹配类型。 |
| matchValue | string | body | 否 | /api/v1 | 匹配值。 |
| caseSensitive | boolean | body | 否 | true | 是否区分大小写。 |

**serviceIds 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | string | body | 否 | service- 001 | 服务ID。 |
| weight | integer | body | 否 | 50 | 权重。 |

**disasterRecoveryServiceIds 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | string | body | 否 | service- 001 | 服务ID。 |
| weight | integer | body | 否 | 50 | 权重。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | route-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "order": 0,
  "filters": "filters_value",
  "routeId": "routeId_value",
  "routeName": "routeName_value",
  "serviceId": "serviceId_value",
  "serviceType": "serviceType_value",
  "gwInstanceId": "gwInstanceId_value",
  "methods": [],
  "header": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "cookie": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "queryParam": [
    {
      "key": "key_value",
      "value": "value_value"
    }
```

`],`

```json
  "domainIds": [],
"routePath":[],
```

智能体工厂 OpenTrek

```json
  routePath: [],
  "stripPrefix": 0,
  "requestTimeout": 0,
  "openStripPrefix": true,
  "enableForceNonceCheck": true,
  "path": {
    "matchType": "matchType_value",
    "matchValue": "matchValue_value",
    "caseSensitive": true
  },
  "serviceIds": [
    {
      "serviceId": "serviceId_value",
      "weight": 0
    }
```

`],`

```json
  "disasterRecoveryServiceId": "disasterRecoveryServiceId_value",
  "disasterRecoveryServiceIds": [
    {
      "serviceId": "serviceId_value",
      "weight": 0
    }
```

]

```
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### modifyRoutePolicy

**API 接口概述**

**中文名称：**修改路由策略
**功能概述：**修改路由策略。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configType | string | body | 否 | timeout | 配置类型。 |

智能体工厂 OpenTrek

| targetType | string | body | 否 | route | 目标类型。 |
|---|---|---|---|---|---|
| configData | object | body | 否 | {"timeout":3 0} | 配置数据。 |
| gwInstanceId | string | body | 否 | higress- 001 | 网关实例ID。 |
| routeId | string | body | 否 | route-001 | 路由ID。 |
| targetId | string | body | 否 | route-001 | 目标ID。 |

|  |  | {"timeout":3 | 配 |
|---|---|---|---|
|  | 0} |  |  |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | route-001 | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "configType": "configType_value",
  "targetType": "targetType_value",
  "configData": {},
  "gwInstanceId": "gwInstanceId_value",
  "routeId": "routeId_value",
  "targetId": "targetId_value"
}
```

智能体工厂 OpenTrek

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

### 集群管理

#### cancelImportCluster

**API 接口概述**

**中文名称：**取消导入集群
**功能概述：**取消导入k8s集群。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| k8sClusterCode | string | body | 是 | k8s- cluster-001 | Kubernetes集群编码。 |

|  |  | k8s- | Ku |
|---|---|---|---|
|  | cluster-001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |

**示例**

智能体工厂 OpenTrek

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "k8sClusterCode": "k8sClusterCode_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {}
}
```

#### checkConnect

**API 接口概述**

**中文名称：**检查集群连通性
**功能概述：**测试Kubernetes集群连接是否正常。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 |  |  | 示例 |  | 说明 |
|---|---|---|---|---|---|---|---|---|
| configContent | string | body | 是 |  |  | base64- |  | configContent 参数。 |
|  |  |  |  |  |  |  | base64- | configContent |
|  |  |  |  |  |  | encoded- |  | conf |
|  |  |  |  |  |  |  |  | 参数 |
|  |  |  |  |  |  | kubeconfig |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

| msg | string | success | 响应消息。 |
|---|---|---|---|
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.connectStatus | integer | 1 | connectStatus字段。 |
| data.connectStatusDesc | string | 连接正常 | connectStatusDesc字段。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "configContent": "configContent_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "connectStatus": 0,
    "connectStatusDesc": "connectStatusDesc_value"
  }
}
```

#### createK8s

**API 接口概述**

**中文名称：**导入Kubernetes集群
**功能概述：**导入Kubernetes集群。
**请求路径：** `/k8s/importCluster`
**请求方式：** `POST`
智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configContent | string | body | 否 | apiVersion: v1... | KubeConfig内容。 |
| k8sClusterNam e | string | body | 是 | my-k8s- cluster | Kubernetes集群名称。 |
| k8sClusterType | string | body | 否 | ACK | Kubernetes集群类型。 |
| k8sClusterAttri bute | object | body | 否 | - | 集群属性配置。 |

|  |  | apiVersion: | Kub |
|---|---|---|---|
|  | v1... |  |  |

|  |  | my-k8s- | K |
|---|---|---|---|
|  | cluster |  |  |

**k8sClusterAttribute 对象结构**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| csClusterId | string | body | 否 | cs-cluster- 001 | CS集群ID。 |

|  |  | cs-cluster- | C |
|---|---|---|---|
|  | 001 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | k8s-cluster-001 | 响应数据。 |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /k8s/importCluster HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "configContent": "configContent_value",
  "k8sClusterName": "k8sClusterName_value",
  "k8sClusterType": "k8sClusterType_value",
  "k8sClusterAttribute": {
    "csClusterId": "csClusterId_value"
  }
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getK8sClusterName

**API 接口概述**

**中文名称：**查询集群名称
**功能概述：**查询集群名称。
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |

智能体工厂 OpenTrek

| code | integer | 200 | 响应码。 |
|---|---|---|---|
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | my-k8s-cluster | 响应数据。 |

**示例**

**请求示例**

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": "data_value"
}
```

#### getK8sInfoByGwInstanceId

**API 接口概述**

**中文名称：**查询实例所属集群
**功能概述：**获取当前实例的Kubernetes集群信息。

```
请求路径： /k8s/getK8sClusterInfoByGwInstanceId
```

**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| gwInstanceId | string | body | 是 | higress- 001 | 网关实例ID。 |
|---|---|---|---|---|---|

|  |  | higress- |
|---|---|---|
|  | 001 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | {} | 响应数据。 |
| data.k8sClusterCode | string | k8s-cluster-001 | Kubernetes集群编码。 |
| data.k8sClusterName | string | my-k8s-cluster | Kubernetes集群名称。 |
| data.masterUrl | string | https://192.168.1.10 0:6443 | masterUrl字段。 |
| data.k8sClusterStatus | integer | 1 | k8sClusterStatus字段。 |
| data.k8sClusterStatusDe sc | string | 正常 | k8sClusterStatusDesc字段。 |
| data.k8sClusterImportDa teTime | string | 2024-01-01 10:00:00 | k8sClusterImportDateTi me字段。 |

|  | https://192.168.1.10 | mast |
|---|---|---|
| 0:6443 |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
POST /k8s/getK8sClusterInfoByGwInstanceId HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "gwInstanceId": "gwInstanceId_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "k8sClusterCode": "k8sClusterCode_value",
    "k8sClusterName": "k8sClusterName_value",
    "masterUrl": "masterUrl_value",
    "k8sClusterStatus": 0,
    "k8sClusterStatusDesc": "k8sClusterStatusDesc_value",
    "k8sClusterImportDateTime": "k8sClusterImportDateTime_value"
  }
}
```

#### listCluster

**API 接口概述**

**中文名称：**查询集群列表
**功能概述：**服务管理 - 获取集群列表。
**请求路径：** `/k8s/getClusterList`
**请求方式：** `POST`

**请求参数**

无请求参数。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |

智能体工厂 OpenTrek

| msg | string | success | 响应消息。 |
|---|---|---|---|
| message | string | success | 响应消息。 |
| data | BaseLVListResponse[] | [] | 响应数据。 |
| data.label | string | my-k8s-cluster | label字段。 |
| data.value | string | k8s-cluster-001 | 键值。 |

|  |  | BaseLVListResponse[] |
|---|---|---|
| a |  |  |

**示例**

**请求示例**

```
POST /k8s/getClusterList HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
    "code": 200,
    "message": "success",
    "requestId": "xxx-xxx-xxx",
    "data": [
        {
```

`"label": "`集群名称`1",` `"value": "`集群编码`1"`

```
        },
        {
```

`"label": "`集群名称`2",` `"value": "`集群编码`2"`

```
        }
```

]

```
}
```

#### pageK8s

**API 接口概述**

**中文名称：**分页查询集群
**功能概述：**获取所有的Kubernetes集群。
智能体工厂 OpenTrek
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| current | integer | body | 是 | 1 | 当前页码。 |
| size | integer | body | 是 | 10 | 每页大小。 |
| clusterName | string | body | 否 | my-k8s- cluster | 集群名称。 |

|  |  | my-k8s- | 集 |
|---|---|---|---|
|  | cluster |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | object | - | 响应数据。 |
| data.total | integer | 100 | 总数。 |
| data.current | integer | 1 | 当前页码。 |
| data.size | integer | 10 | 每页大小。 |
| data.records | ListK8sClusterRespon se[] | - | 记录列表。 |
| data.records.k8sClusterC ode | string | k8s-cluster-001 | Kubernetes集群编码。 |
| data.records.k8sClusterN ame | string | my-k8s-cluster | Kubernetes集群名称。 |

| ListK8sClusterRespon | - |  |
|---|---|---|
|  |  | - |

智能体工厂 OpenTrek

| data.records.masterUrl | string | https://192.168.1.10 0:6443 | Master节点地址。 |
|---|---|---|---|
| data.records.k8sClusterS tatus | integer | 1 | 集群状态。1=正常，0=异常。 |
| data.records.k8sClusterS tatusDesc | string | 正常 | 集群状态描述。 |
| data.records.k8sClusterI mportDateTime | string | 2024-01-01 10:00:00 | 导入时间。 |
| data.records.k8sClusterA ttribute | object | - | 集群属性配置。 |
| data.records.k8sClusterA ttribute.csClusterId | string | cs-cluster-001 | CS集群ID。 |
| data.records.k8sClusterA ttribute.csClusterName | string | my-cs-cluster | CS集群名称。 |
| data.records.k8sClusterA ttribute.slbType | string | private | SLB类型。 |
| data.records.k8sClusterA ttribute.vpcId | string | vpc-001 | VPC ID。 |
| data.records.k8sClusterA ttribute.mappingIP | string | 192.168.1.100 | 映射IP。 |
| data.records.k8sClusterA ttribute.mappingPort | integer | 6443 | 映射端口。 |
| data.records.k8sClusterA ttribute.abnormalReason | string | - | 异常原因。 |
| data.records.k8sClusterT ype | string | ACK | 集群类型。 |

|  | https://192.168.1.10 | Maste |
|---|---|---|
| 0:6443 |  |  |

**示例**

**请求示例**

智能体工厂 OpenTrek

```json
Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "current": 0,
  "size": 0,
  "clusterName": "clusterName_value"
}
```

**响应示例**

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "xxx-xxx-xxx",
  "data": {
    "total": 0,
    "current": 0,
    "size": 0,
    "records": {
      "k8sClusterCode": "k8sClusterCode_value",
      "k8sClusterName": "k8sClusterName_value",
      "masterUrl": "masterUrl_value",
      "k8sClusterStatus": 0,
      "k8sClusterStatusDesc": "k8sClusterStatusDesc_value",
      "k8sClusterImportDateTime": "k8sClusterImportDateTime_value",
      "k8sClusterAttribute": {
        "csClusterId": "csClusterId_value",
        "csClusterName": "csClusterName_value",
        "slbType": "slbType_value",
        "vpcId": "vpcId_value",
        "mappingIP": "mappingIP_value",
        "mappingPort": 0,
        "abnormalReason": "abnormalReason_value"
      },
        "k8sClusterType": "k8sClusterType_value"
     }
  }
}
```

#### updateK8s

**API 接口概述**

**中文名称：**更新Kubernetes集群
**功能概述：**更新Kubernetes集群信息。
**请求路径：** `/k8s/updateCluster`
智能体工厂 OpenTrek
**请求方式：** `POST`

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| clusterCode | string | body | 是 | k8s- cluster-001 | Kubernetes集群编码。 |
| k8sClusterAttri bute | string | body | 是 | updated- attribute | k8sClusterAttri bute参数。 |

|  |  | k8s- | Ku |
|---|---|---|---|
|  | cluster-001 |  |  |

|  |  | updated- | k8sC |
|---|---|---|---|
|  | attribute |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | string | uuid-xxx-xxx | 请求ID。 |
| code | integer | 200 | 响应码。 |
| msg | string | success | 响应消息。 |
| message | string | success | 响应消息。 |
| data | string | k8s-cluster-001 | 响应数据。 |

**示例**

**请求示例**

```json
POST /k8s/updateCluster HTTP/1.1 Host: localhost:80 Content-Type: application/json X-CSB-OPENAPI: true X-CSB-TOKEN: csb@2022 {
  "clusterCode": "k8s-cluster-001",
  "k8sClusterAttribute": "updated-attribute"
}
```

**响应示例**

智能体工厂 OpenTrek

```json
HTTP/1.1 200 OK Content-Type: application/json {
  "code": 200,
  "message": "success",
  "requestId": "uuid-xxx-xxx",
  "data": "k8s-cluster-001"
}
```
