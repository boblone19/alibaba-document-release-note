---
title: "智能体工厂 OpenTrek AI Studio 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 931
source_pdf: "11_AI Studio 开发指南_ai-studio-development-guide-2.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/opentrek/zh/ai-studio-development-guide-2.pdf"
converter: line-classifier (PyMuPDF)
---

# 智能体工厂 OpenTrek AI Studio 开发指南

智能体工厂 OpenTrek

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
智能体工厂 OpenTrek
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

AI Studio的API调用流程如下图所示。

**调用步骤**

1. 获取AccessKey。
智能体工厂 OpenTrek

**说明**

推荐使用个人AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取Endpoint和Region ID信息。
获取调用时所需要的Endpoint和RegionID参数，请参见获取API信息及其EndPoint。
3. 获取AI Studio的SDK包和SDK核心库，获取方法请参见安装Java SDK。
4. 通过API参考章节的信息进行调用。
智能体工厂 OpenTrek

## 准备工作

### 获取AccessKey

**背景信息**

访问身份验证中通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。

**前提条件**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，将鼠标悬停在当前登录用户的头像上，单击**个人信息**。
3. 在**阿里云****AccessKey**区域，您可以查看个人账户的AccessKey信息。

**重要**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。 获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。
智能体工厂 OpenTrek

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择AI Studio。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取AI Studio的POP Endpoint和Region ID等信息。

### 通过POP网关调用专有云API

AI Studio通过绑定的POP域名来访问，当前版本支持ROA风格的接口调用。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！ ROA调用，示例接口信息：产品（aipaas）接口（CreateModel）版本（2024-06-24）。 调用示例如下： Java

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType;
```

智能体工厂 OpenTrek

```java
import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile;
```

#sts安全访问示例`demo`：

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
    /** 使用 STS Token
     DefaultProfile profile = DefaultProfile.getProfile(
     "<your-regionid>",            // 实际的地域ID
     "<your-access-key-id>",       // RAM 账户的 AccessKey ID
     "<your-access-key-secret>",   // RAM 账户的 AccessKey Secret
     "<your-sts-token>");          // STS Token
     **/
    IClientProfile profile = DefaultProfile.getProfile("<your-regionid>", "<your-access
-key-id>", "<your-access-key-secret>",
            "<your-sts-token>");
```

`// Client` 代理配置

```
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置请求协议

```
    clientConfig.setProtocolType(ProtocolType.HTTP);
```

`//` 设置读取超时，单位：`ms`

```
    clientConfig.setReadTimeoutMillis("<readTimeout>");
    /**
```

请根据实际情况判断是否需要设置`HTTP`代理设置方法如下：

```
     clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

请替换为实际代理`IP+`端口 `*/`

```
    clientConfig.setHttpProxy("http://192.168.XX.XX:33XX>");
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求

```
    CommonRequest request = new CommonRequest();
```

`//` 云产品的`Endpoint`地址，可变参数请替换为您的实际值。

```
    request.setSysDomain("<Endpoint>");
```

`//` 产品接口信息参数

```
    request.setSysProduct("aipaas");
    request.setSysVersion("2024-06-24");
    request.setSysUriPattern("/model/create");
    /**
```

阿里云核心库`SDK`发起`API`请求时，可以设置四种类型参数（`Path/Query/Body/Header`） `Path`参数用于对请求`Request`中设置的`UriPattern`进行变量替换 `Query`参数用于对请求`Request`中的`URL`参数进行设置（一般用于`GET`请求） `Body`参数用于对请求`Request`中的`HTTP Content`进行设置（一般用于`POST/PUT`请求），在设置`Body`参数时 ，需要同时设置`HTTP Content-Type`，目前支持`JSON`和`FORM`两种格式 `Header`参数用于对请求`Request`中的`HTTP Header`进行设置 `*/`

```
    /**
```

设置`Headers` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-` `id`等" i i `id` `id` i 智能体工厂 OpenTrek

```
organizationid、x-acs-resourcegroupid、x-acs-instanceid等"
     request.putHeadParameter("x-acs-caller-sdk-source","<your-sdk-source>");
```

`*/` `//` 接口业务参数设置，接口参数请替换为您的实际值。

```
    request.putBodyParameter("modelName", "test");
    request.putBodyParameter("modelDesc", "test");
    request.putBodyParameter("modelType", "1");
    request.putBodyParameter("frameWork", "1");
    request.putBodyParameter("modelVersion", "v1");
    request.putBodyParameter("modelSource", "1");
    request.putBodyParameter("modelStatus", "true");
    request.putBodyParameter("storageSource", "1");
    request.putBodyParameter("storagePath", "<your-storage-path>");
```

`//` 设置请求方式

```java
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.JSON);
    try {
        CommonResponse response = client.getCommonResponse(request);
        System.out.println("输出结果：" + response.getData());
    } catch (ServerException e) {
        e.printStackTrace();
    } catch (ClientException e) {
        e.printStackTrace();
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

智能体工厂 OpenTrek 例

## Java SDK调用示例

### 安装Java SDK

本文介绍如何安装AI Studio的Java SDK。

**环境准备**

阿里云专有云Java SDK需要使用1.8及后续版本的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 调用Java SDK必须安装SDK核心库以及AI Studio的SDK包。其中，SDK核心库推荐使用4.6.3及以上版本，SDK的版本为3.0.0。 以下为Java pom文件设置示例。

```xml
<dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-sts-internal</artifactId>
    <version>3.0.0</version>
    <scope>compile</scope>
</dependency> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.6.3</version>
</dependency>
```

### 设置身份验证凭证

使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 Java SDK支持通过AccessKey进行身份验证，获取AccessKey ID和AccessKey Secret的方法请参见获取AccessKey，获取Endpoint和Region ID的方法请参见获取API信息及其EndPoint。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**重要**

请确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret` 智能体工厂 OpenTrek 例

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留

### 发起调用请求

本文介绍如何使用Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
DefaultAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类使用CommonRequest来进行调用。

```
CommonRequest request = new CommonRequest();
```

3. 发起调用并处理应答。
`//` 发起请求，查看结果

```
CommonResponse response = client.getCommonResponse(request););
```

**完整调用示例**

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.profile.IClientProfile; public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
    /** 使用 STS Token
     DefaultProfile profile = DefaultProfile.getProfile(
     "<your-regionid>",            // 实际的地域ID
     "<your-access-key-id>",       // RAM 账户的 AccessKey ID
     "<your-access-key-secret>",   // RAM 账户的 AccessKey Secret
     "<your-sts-token>");          // STS Token
     **/
    IClientProfile profile = DefaultProfile.getProfile("<your-regionid>", "<your-access
-key-id>", "<your-access-key-secret>",
            "<your-sts-token>");
```

`// Client` 代理配置

```
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

智能体工厂 OpenTrek 例 `//` 设置请求协议

```
    clientConfig.setProtocolType(ProtocolType.HTTP);
```

`//` 设置读取超时，单位：`ms`

```
    clientConfig.setReadTimeoutMillis("<readTimeout>");
    /**
```

请根据实际情况判断是否需要设置`HTTP`代理设置方法如下：

```
     clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

请替换为实际代理`IP+`端口 `*/`

```
    clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求

```
    CommonRequest request = new CommonRequest();
```

`//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
    request.setSysDomain("<Endpoint>");
```

`//` 产品接口信息参数

```
    request.setSysProduct("aipaas");
    request.setSysVersion("2024-06-24");
    request.setSysUriPattern("/image/createCustomImage");
    /**
```

阿里云核心库`SDK`发起`API`请求时，可以设置四种类型参数（`Path/Query/Body/Header`） `Path`参数用于对请求`Request`中设置的`UriPattern`进行变量替换 `Query`参数用于对请求`Request`中的`URL`参数进行设置（一般用于`GET`请求） `Body`参数用于对请求`Request`中的`HTTP Content`进行设置（一般用于`POST/PUT`请求），在设置`Body`参数时 ，需要同时设置`HTTP Content-Type`，目前支持`JSON`和`FORM`两种格式 `Header`参数用于对请求`Request`中的`HTTP Header`进行设置 `*/`

```
    /**
```

设置`Headers` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-`

```
organizationid、x-acs-resourcegroupid、x-acs-instanceid等"
     request.putHeadParameter("x-acs-caller-sdk-source","<your-sdk-source>");
```

`*/` `//` 接口业务参数设置，接口参数请替换为您的实际值。

```
    request.putBodyParameter("imageName", "test");
    request.putBodyParameter("imageDesc", "test");
    request.putBodyParameter("imageVersion", "v1");
    request.putBodyParameter("imageNamespace", "test");
    request.putBodyParameter("imageRepo", "test");
    request.putBodyParameter("imageRepoTag", "v1");
    request.putBodyParameter("imageAddress", "<your-image-address>");
    request.putBodyParameter("imageSize", "1000");
    request.putBodyParameter("availableService", "2");
    request.putBodyParameter("frameWork", "1");
```

`//` 设置请求方式

```
    request.setSysMethod(MethodType.POST);
```

智能体工厂 OpenTrek 例

```java
    request.setHttpContentType(FormatType.JSON);
    try {
        CommonResponse response = client.getCommonResponse(request);
        System.out.println("输出结果：" + response.getData());
    } catch (ServerException e) {
        e.printStackTrace();
    } catch (ClientException e) {
        e.printStackTrace();
    }
}
```

### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要根据Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 ServerException是服务端错误信息。 ClientException是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    AcsResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`

```
    // ...
} catch (ClientException e) {
```

`//` 这里可以添加您自己的错误处理逻辑 `//` 例如，打印具体的错误信息

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    e.printStackTrace();
} catch (ServerException e) {
    e.printStackTrace();
}
```

智能体工厂 OpenTrek

## API参考

### 数据集

#### GetApfs

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| bmcpClust erId | Strin g | Query | 是 | ack-YoZjG***** | BMCP集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -mountDir | List | [ "/example/dir" ] | 挂载目录列表。 |
| -mountedFs | String | efs-****018e | 已挂载的文件系统。 |

**示例**

智能体工厂 OpenTrek 请求示例

```
&bmcpClusterId=ack-YoZjG*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "mountedFs":"efs-****018e",
  "mountDir":"[  \"/example/dir\"]"
 },
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteDataset

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /dataset/deleteDataset/[datasetId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Path | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /dataset/deleteDataset/[datasetId] HTTP/1.1 &datasetId=ds-3dc49fc087b3491cafa76b5d842****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetDataset

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Path | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |
| -dataSource | Integer | 1 | 数据集存储类型： 1：OSS 2：CPFS 4：APFS 5：S3 |
| - datasetDescri ption | String | 自动化创建 | 数据集描述。 |
| - datasetGmtCr eate | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -datasetId | String | ds- a60cbb90******46f 4 | 数据集ID。 |
| -datasetName | String | ait dataset pytorc _ _ h mnist 770b587b _ _ | 数据集名称。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtModified | String | 2026-02- 27T01:53:30Z | 修改时间。 |
| -latestVersion | String | v1 | 最新版本号。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -versionCount | Integer | 1 | 版本数量。 |

**示例**

请求示例

```
&datasetId=ds-3dc49fc087b3491cafa76b5d842****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "versionCount":"",
  "datasetDescription":"",
  "gmtModified":"",
  "aliyunUid":"",
  "latestVersion":"",
  "regionId":"",
  "datasetGmtCreate":"",
  "datasetName":"",
  "datasetId":"",
  "dataSource":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListDatasets

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |
| dataType | Integ er | Query | 否 | 0 | 数据类型，取值范围： 0：图片。 1：文本。 2：音频。 3：表格。 4：视频。 |
| dataSourc e | Integ er | Query | 否 | 1 | 数据来源存储类型，取值范围： 1：OSS存储。 2：CPFS存在。 |
| datasetTy pe | Integ er | Query | 否 | 0 | 数据集类型，取值范围： 0：训练集。 1：评测集。 2：训练集&评测集。 |
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27f36**** | 资源配额ID。 |
| sourceTyp e | Integ er | Query | 否 | 1 | 数据集来源，取值范围： 1：用户上传。 2：数据标注导出。 |
| dataProce ssTaskTyp e | Integ er | Query | 否 | 2 | 数据处理类型，取值范围： 2：标注。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据集列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |
| - dataProcessTa skType | Integer | 2 | 初始化后的目标数据处理任务类型: 2-数据标注, etc。 |
| -dataSource | Integer | 1 | 数据集存储类型： 1：OSS。 2：CPFS。 4：APFS。 5：S3。 |
| - dataSubProces sTaskType | Integer | 0 | 初始化后的数据处理任务的子任务类型。 0：文本标注。 1：图片标注。 |
| - datasetDescri ption | String | 自动化创建 | 数据集描述。 |
| - datasetGmtCr eate | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -datasetId | String | ds- a60cbb90******46f 4 | 数据集ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -datasetName | String | dataset mnist _ | 数据集名称。 |
| -gmtModified | String | 2026-02- 27T01:53:30Z | 修改时间。 |
| -latestVersion | String | v1 | 最新版本号。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -shared | Integer | 1 | 共享范围： 0：本资源集。 1：本组织及下级组织。 2：本组织。 |
| -versionCount | Integer | 1 | 版本数量。 |
| totalCount | Integer | 100 | 数据集的总数。 |
| pageSize | Integer | 10 | 数据集的页码。 |
| pageIndex | Integer | 1 | 每页行数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":[
  {
   "versionCount":"",
   "shared":"",
   "datasetDescription":"",
   "gmtModified":"",
   "aliyunUid":"",
   "datasetName":"",
   "dataSubProcessTaskType":"",
   "dataProcessTaskType":"",
   "latestVersion":"",
   "regionId":"",
   "datasetGmtCreate":"",
   "datasetId":"",
   "dataSource":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### UpdateDataset

调用UpdateDataset修改指定数据集的部分信息，包括数据集名称、描述和数据集类型。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataset/updateDataset/[datasetId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Path | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetVe rsion | Strin g | Body | 否 | v1.0 | 数据集版本。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetNa me | Strin g | Body | 是 | dataset-name | 数据集名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | dataset-description | 数据集描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| versionDe scription | Strin g | Body | 否 | description for dataset version | 数据集版本描述。 |
| datasetTy pe | Integ er | Body | 否 | 0 | 数据集类型，取值范围： 0：训练集。 1：评测集。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /dataset/updateDataset/[datasetId] HTTP/1.1 { "datasetId":"ds-3dc49fc087b3491cafa76b5d842****", "datasetName":"dataset-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateDataset

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Body | 是 | ds-rbvg5****jhc9ks92 | 数据集ID，创建新数据集版本时必填。 |
| datasetNa me | Strin g | Body | 是 | dataset-name | 数据集名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| versionDe scription | Strin g | Body | 否 | datasetVersionDescripti on | 数据集版本描述信息。 |
| datasetDe scription | Strin g | Body | 否 | dataset-description | 数据集描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetTy pe | Integ er | Body | 是 | 0 | 数据集类型，该参数必填， 取值范围： 0：训练集。 1：评测集。 2：训练集&评测集。 （废弃） |
| dataType | Integ er | Body | 是 | 0 | 数据类型，该参数必填，取值范围： 0：图片。 1：文本。 2：音频。 3：表格。 4：视频。 |
| dataSourc e | Integ er | Body | 是 | 1 | 数据来源存储类型，该参数必填，取值范围： 1：OSS对象存储。 2：CPFS文件系统。 4：APFS文件系统。 |
| dataPath | Strin g | Body | 是 | oss://****/**** | 数据路径，该参数必填。 |
| isDirector y | Integ er | Body | 是 | 0 | 数据集是否为文件夹，该参数必填，取值范围： 0：文件。 1：文件夹。 |
| sourceTyp e | Integ er | Body | 是 | 1 | 数据集来源，该参数必填， 取值范围： 1：自定义创建。 2：数据标注导出。 3：数据生成导出。 4：评测结果导出。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataProce ssOptions | Strin g | Body | 否 | { "dataProcessTaskType": 2, "initResultPath": "oss://***/***", "dataSubProcessTaskTy pe": "0" } | 可选配置。在数据集需要标注时必传。 dataProcessTaskType ：数据集待处理任务的类型。支持任务场景： 2：数据标注 dataSubProcessTaskT ype：数据集待处理任务的子类型。 数据标注场景（即 dataProcessTaskTy pe为2 时，dataSubProcess TaskType必传） 0：文本类标注 1：图片类标注 initResultPath：数据处理任务前，数据集进行初始化后的存储路径。 数据标注场景（即 dataProcessTaskTy pe为2 时，initResultPath必传） 文本类标注（即 dataSubProcessT askType为0 时），initResultP ath与数据集的存储路径（dataPath） 一致图片类标注（即 dataSubProcessT askType为1时）， 创建数据集的过程中将生成标准格式的初始化待标注数据文件，initResultPat h为该初始化文件的存放的目录 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceInfo | Json | Body | 是 | "sourceInfo":{ "sfmWorkspaceCode":"* ***", "sfmDatasetCode": "****", "sfmSubsetCode":"****" } | 数据集来源元信息。 关联百炼专属版数据集时此字段不能为空，sfmWorkspaceCo de和sfmDatasetCode 必填， 导入格式为文件夹时， 关联百炼专属版数据集，此时无需填 sfmSubsetCode。 导入格式为文件时，关联百炼专属版数据子集，此时需填 sfmSubsetCode。 字段含义： sfmWorkspaceCode： 百炼专属版工作空间 code sfmDatasetCode：百炼专属版数据集code sfmSubsetCode：百炼专属版数据子集code |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "datasetId": "ds- *****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
{ "datasetId":"ds-rbvg5****jhc9ks92", "datasetName":"dataset-name", "datasetType":"0", "dataType":"0", "dataSource":"1", "dataPath":"oss://****/****", "isDirectory":"0", "sourceType":"1", "sourceInfo":""sourceInfo":{
    "sfmWorkspaceCode":"****",
    "sfmDatasetCode": "****",
    "sfmSubsetCode":"****"
}" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{       \"datasetId\": \"ds-*****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListDataExportTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| exportTas kId | Strin g | Query | 否 | exdt- 7c687fe90b7be047ce09 e34**** | 导出任务ID。 |
| dataProce ssTaskId | Strin g | Query | 否 | at- 8870154d05c9f047b70a 5f30**** | 来源数据处理任务ID。 |

|  | 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataProce ssTaskTyp e | Integ er | Query | 否 | 2 | 来源数据处理任务类型。 |
| exportTyp e | Integ er | Query | 否 | 0 | 导出类型，取值范围： 0：只导出至存储类型。 1：导出至存储类型后， 创建数据集。 |
| exportStat us | Integ er | Query | 否 | 2 | 导出任务状态，取值范围： 0：未开始。 1：运行中。 2：已完成。 3：失败。 4：停止。 |
| exportFor matType | Integ er | Query | 否 | 1 | 导出文件格式，取值范围： 0：jsonl。 1：csv。 2：manifest。 |
| pageIndex | Integ er | Query | 否 | 1 | 导出任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliYunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - dataProcessTa skId | String | dpd-sdsafhu | 来源数据处理任务ID。 |
| - dataProcessTa skMeta | String | "" | 描述数据处理任务的元信息 |
| - dataProcessTa skType | Integer | 2 | 数据导出类型 1：用户上传 2：数据标注导出 4：评测结果反馈导出 |
| - exportDataset Config | String | { "dataType": 0, "datasetId": "ds- 16944a2100cf3042 85", "Department": 5, "datasetName": "zexi test 0209", _ _ "datasetType": 0, "ResourceGroup": 4, "datasetVersion": "v2" } | 导出数据集配置。 |
| - exportDatasetI d | String | ds-16944a2100 | 用于标识待导出数据集的唯一ID |
| - exportDataset Version | String | v1 | 表示导出数据集的版本号 |
| - exportFormatT ype | Integer | 0 | 导出文件格式，取值范围： 0：jsonl。 |
| -exportPath | String | oss://test- gq.osaa.com/ | 导出oss目标路径，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -exportStatus | Integer | 2 | 导出任务状态: 0:未开始 1:进行中 2:已完成 3:失败 4:停止 |
| - exportStorage Type | Integer | 1 | 导出存储类型，该参数必填，取值范围： 1：OSS。 |
| -exportTaskId | String | exdt- d1972aae0bd0e0 | 异步导出任务id |
| -exportType | Integer | 1 | 导出类型 0:仅导出至存储路径 1:导出至存储路径并数据集 |
| -gmtCreated | String | 2026-02- 27T06:00:18Z | 创建时间。 |
| -gmtModified | String | 2026-02- 27T06:00:18Z | 修改时间。 |
| -id | Integer | 66 | id |
| -isDeleted | Integer | 0 | 是否已删除，取值范围如下： 0 ：未删除。 1 ：已删除。 |
| - progressComp leted | Integer | 10 | 导出进度（文件数量，单位：个） |
| -progressTotal | Integer | 20 | 导出总数(文件数量，单位：个） |
| -regionId | String | cn-hangzhou | regionId |
| -totalFileSize | Integer | 2300 | 导出文件总大小（单位：字节） |
| totalCount | Integer | 100 | 导出任务数据的总数。 |
| pageSize | Integer | 10 | 每页行数。 |

| I Studio · | API |  | OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageIndex | Integer | 1 | 任务的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
                "exportTaskId": "exdt-d1972aae0bd0e04c3b",
                "gmtModified": "2026-02-27T06:00:21Z",
                "aliYunUid": "1982260514521225",
                "exportDatasetId": "ds-16944a2100cf304285",
                "gmtCreated": "2026-02-27T06:00:18Z",
                "exportPath": "oss://test-gq.oss.ops.arm.com/",
                "isDeleted": 0,
                "id": 66,
                "exportStatus": 2,
                "progressTotal": 10,
                "dataProcessTaskMeta": "{\"taskId\": \"at-a6e1e7cc0161304d4d\", \"taskNa
me\": \"zexi_test_0212\", \"datasetId\": \"ds-16944a2100cf304285\", \"datasetName\": \" zexi_test_0209\", \"taskFlowType\": 1, \"annotationType\": 4, \"datasetVersion\": \"v1\ "}",
                "dataProcessTaskType": 2,
                "dataProcessTaskId": "at-a6e1e7cc0161304d4d",
                "exportDatasetVersion": "v2",
                "regionId": "cn-neimeng-236e-d01",
                "exportType": 1,
                "exportStorageType": 1,
                "totalFileSize": 3320,
                "exportDatasetConfig": "{\"dataType\": 0, \"datasetId\": \"ds-16944a2100
cf304285\", \"Department\": 5, \"datasetName\": \"zexi_test_0209\", \"datasetType\": 0, \"ResourceGroup\": 4, \"datasetVersion\": \"v2\"}",
                "exportFormatType": 0,
                "progressCompleted": 10
            }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### CreateDataExportTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataset/exportData/create HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataProce ssTaskTyp e | Integ er | Body | 是 | 2 | 来源数据处理任务类型，该参数必填，取值范围： 2：数据标注。 3：数据生成。 4：模型评测。 |
| dataProce ssTaskId | Strin g | Body | 是 | at- 8870154d05c9f047b70a 5f3***** | 来源数据处理任务ID，该参数必填。 |
| exportFor matType | Integ er | Body | 否 | 1 | 导出文件格式，取值范围： 0：jsonl。 |
| exportTyp e | Integ er | Body | 是 | 0 | 导出方式，该参数必填，取值范围： 0：只导出至存储类型。 1：导出至存储类型后， 创建数据集。 |
| exportStor ageType | Integ er | Body | 是 | 1 | 导出存储类型，该参数必填，取值范围： 1：OSS。 |
| exportPat h | Strin g | Body | 是 | oss://******/ | 导出目标路径，该参数必填。 |
| exportDat asetConfi g | Strin g | Body | 否 | { "datasetName": "aaaa", "datasetDescription": "", "datasetType": 1, "dataType": 3 } | 导出数据集配置，当 exportType为1时，该参数不能为空。 |
| dataFilter Config | Strin g | Body | 否 | {\"minScore\":0.1,\"max Score\":4.6} | 导出数据的过滤条件。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"exportTaskId": "exdt-*****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataset/exportData/create HTTP/1.1 { "dataProcessTaskType":"2", "dataProcessTaskId":"at-8870154d05c9f047b70a5f3*****", "exportType":"0", "exportStorageType":"1", "exportPath":"oss://******/" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"exportTaskId\": \"exdt-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteDatasetVersion

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataset/delete-version HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Body | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID，该参数必填。 |
| datasetVe rsion | Json | Body | 是 | ['v1','v3'] | 数据集版本，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataset/delete-version HTTP/1.1 { "datasetId":"ds-3dc49fc087b3491cafa76b5d842****", "datasetVersion":"['v1','v3']" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### GetDatasetFileContent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Path | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetVe rsion | Strin g | Path | 是 | v1 | 数据集版本。 |
| filePath | Strin g | Path | 是 | componentUpload/ | 文件路径。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -content | String | {"data": {"source":"示例内容。"}} | 响应内容。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -datasetId | String | ds- a60cbb90******46f 4 | 数据集ID。 |
| - datasetVersion | String | v1 | 数据集版本。 |
| -filePath | String | oss://****/example. jsonl | 文件路径。 |
| -objectName | String | example.jsonl | OSS对象名称。 |
| -preSignedUrl | String | http://****/**** | 预签名URL。 |

**示例**

请求示例

```
&datasetId=ds-3dc49fc087b3491cafa76b5d842**** &datasetVersion=v1 &filePath=componentUpload/
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "datasetVersion":"v1",
  "filePath":"oss://****/example.jsonl",
  "datasetId":"ds-a60cbb90******46f4",
  "objectName":"example.jsonl",
  "preSignedUrl":"http://****/****",
  "content":"{\"data\":{\"source\":\"示例内容。\"}}"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListDatasetVersion

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Query | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetVe rsion | Strin g | Query | 否 | v1 | 数据集版本。 |
| isDirector y | Integ er | Query | 否 | 0 | 数据集是否为文件夹，取值范围： 0：文件。 1：文件夹。 |
| dataType | Integ er | Query | 否 | 0 | 数据类型，取值范围： 0：图片。 1：文本。 2：音频。 3：表格。 4：视频。 |
| dataSourc e | Integ er | Query | 否 | oss://****/**** | 数据集存储类型，取值范围： 1：OSS对象存储。 2：CPFS文件系统。 |
| datasetTy pe | Integ er | Query | 否 | 0 | 数据集类型，取值范围： 0：训练集。 1：评测集。 |
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| sourceTyp e | Integ er | Query | 否 | 1 | 源类型，取值范围： 1：自定义创建。 2：数据标注导出。 3：数据生成导出。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataProce ssTaskTyp e | Integ er | Query | 否 | 2 | 来源数据处理任务类型，取值范围： 2：数据标注。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据集版本列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | scaleTime | 排序字段。 默认值：scaleTime。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| importSta tus | Integ er | Query | 否 | 0 | 导入状态，取值范围： 0：导入完成。 1：导入中。 2：导入失败。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -taskList | List | ["at- bbadc141******47c 4"] | 关联任务的列表。 |
| -aliYunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |
| -dataAccCount | Integer | 0 | 关联的数据加速器的数量。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -dataPath | String | oss://****/**** | 数据路径。 |
| -dataSource | Integer | 1 | 数据集存储类型： 1：OSS。 2：CPFS。 4：APFS。 5：S3。 |
| -dataType | Integer | 1 | 文件模态类型（数据格式）： 0：图片。 1：文本。 2：音频。 3：表格。 4：视频。 |
| - datasetGmtCr eate | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -datasetId | String | ds- a60cbb90******46f 4 | 数据集ID。 |
| -datasetType | Integer | 0 | 数据集类型： 0：训练集。 1：评测集。 2：训练集&评测集。 |
| - datasetVersion | String | v1 | 数据集版本。 |
| -importStatus | Integer | 0 | 数据集导入状态： 0：导入完成。 1：导入中。 2：导入失败。 默认为导入完成。 |
| -isDirectory | Integer | 0 | 数据集导入格式： 0：文件。 1：文件夹。 |
| -regionId | String | cn-hangzhou | 地域ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -sourceType | Integer | 1 | 数据集来源 1：用户上传（自定义创建）。 2：数据标注导出。 3：数据生成导出。 4：评测结果导出。 |
| - versionDescrip tion | String | Example desc. | 版本描述。 |
| totalCount | Integer | 1 | 数据集版本的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 数据集版本的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&datasetId=ds-3dc49fc087b3491cafa76b5d842****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "versionDescription":"Example desc.",
   "importStatus":0,
   "aliYunUid":"127756******1314",
   "datasetVersion":"v1",
   "dataType":1,
   "taskList":"[\"at-bbadc141******47c4\"]",
   "dataPath":"oss://****/****",
   "dataAccCount":0,
   "regionId":"cn-hangzhou",
   "sourceType":1,
   "datasetGmtCreate":"2026-02-27T01:53:30Z",
   "datasetId":"ds-a60cbb90******46f4",
   "datasetType":0,
   "dataSource":1,
   "isDirectory":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":1,
 "httpCode":200
}
```

### 数据标注

#### ListAnnotationSubTaskCheck

调用ListAnnotationSubTaskCheck查询所有的验收子任务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/subTask/listCheck HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Query | 否 | at- 97d11ca204c6b0493908 63***** | 数据标注任务ID。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Query | 否 | subtask-name | 数据标注子任务名称。 |
| annotatio nSubTaskI d | Strin g | Query | 否 | ast- eaf458f4057ad04a540b 953***** | 数据标注子任务ID。 |
| subTaskSt atus | Integ er | Query | 是 | 0 | 数据标注子任务状态，取值范围： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 10：已完成。 |
| objectTyp e | Integ er | Query | 否 | 0 | 数据标注对象，取值范围： 0：图片。 1：文本。 |
| taskFlowT ype | Integ er | Query | 否 | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| taskFromT ype | Integ er | Query | 否 | 0 | 数据标注任务来源，取值范围： 0：分配。 1：转派。 2：驳回。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据标注子任务验收列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| Resource Group | Integ er | Query | 否 | 1 | 资源集。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - annotatedNum | Integer | 2 | 已标注数量。 |
| - annotationSub TaskId | String | ast- eaf458f4057ad0*** ** | 数据标注子任务ID。 |
| - annotationTas kId | String | at-97d08634***** | 数据标注任务ID。 |
| - annotationTot alNum | Integer | 10 | 标注总量。 |
| - annotationTyp e | Integer | 0 | 标注类型： 0：文本分类。 1：文本实体标注 。 2：图片描述 。 3：图片QA 。 4：图片分类 。 5：图片目标检测 。 6：文本QA。 |
| - annotatorNam e | String | zhangsan | 标注员。 |
| -annotatorUid | String | 23743437*** | 标注员ID。 |
| - checkTotalNu m | Integer | 6 | 验收总量。 |
| -checkedNum | Integer | 2 | 已验收总量。 |
| -checkerName | String | lisi | 验收员。 |
| -checkerUid | String | 23877***** | 验收员ID。 |
| -name | String | 文本标注 | 任务名称。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -objectType | Integer | 1 | 标注对象类型： 0：图片。 1：文本。 |
| -sampleRate | Float | 1.0 | 抽样比例。 |
| - subTaskStatus | Integer | 1 | 子任务状态： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 |
| -taskFlowType | Integer | 0 | 任务类型： 0：标注。 1：标注-验收。 |
| -taskFromType | Integer | 0 | 数据标注任务来源，取值范围： 0：分配。 1：转派。 2：驳回。 |
| totalCount | Integer | 100 | 数据标注子任务验收的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 数据标注子任务验收的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
GET /dataAnnotation/subTask/listCheck HTTP/1.1 &subTaskStatus=0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "taskFromType":0,
   "annotatorUid":"23743437***",
   "subTaskStatus":1,
   "annotationTotalNum":10,
   "annotationType":0,
   "annotatedNum":2,
   "sampleRate":1.0,
   "checkTotalNum":6,
   "objectType":1,
   "annotationTaskId":"at-97d08634*****",
   "annotatorName":"zhangsan",
   "annotationSubTaskId":"ast-eaf458f4057ad0*****",
   "checkerUid":"23877*****",
   "checkedNum":2,
```

`"name":"`文本标注`",`

```json
   "checkerName":"lisi",
   "taskFlowType":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### ListAnnotationTaskSubTask

调用ListAnnotationTaskSubTask查询所有的数据标注子任务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/task/subTaskList/[annotationTaskId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Path | 是 | at- 97d11ca204c6b0493908 6340c6d***** | 数据标注任务ID。 |
| annotatio nSubTaskI d | Strin g | Query | 否 | ast- 4901bf1400f21043400a 2fd9as601***** | 数据标注子任务ID。 |
| subTaskSt atus | Integ er | Query | 否 | 0 | 子任务状态，取值范围： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 10：已完成。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据标注子任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - annotatedNum | Integer | 5 | 已标注数据量 |
| - annotationSub TaskId | String | ast- eaf458f4040b9530 ***** | 数据标注子任务ID。 |
| - annotationTas kId | String | at- 97d1493908634*** ** | 数据标注任务ID。 |
| - annotationTot alNum | Integer | 10 | 标注数据总量 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - annotatorNam e | String | zhangsan | 标注员 |
| -annotatorUid | String | 22737*** | 标注员对应的阿里云子账号id |
| - checkTotalNu m | Integer | 6 | 需验收数据总量 |
| -checkedNum | Integer | 2 | 已验收数据量 |
| -checkerName | String | lisi | 验收员 |
| -checkerUid | String | 28337*** | 验收员对应阿里云子账号id |
| -sampleRate | Float | 0.6 | 验收采样率。 |
| - subTaskStatus | Integer | 1 | 数据标注子任务状态，取值范围： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 10：已完成。 |
| -taskFromType | Integer | 1 | 数据标注任务来源，取值范围： 0：分配。 1：转派。 2：驳回。 |
| totalCount | Integer | 100 | 数据标注子任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 数据标注子任务的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataAnnotation/task/subTaskList/[annotationTaskId] HTTP/1.1 &annotationTaskId=at-97d11ca204c6b04939086340c6d*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "taskFromType":1,
   "annotatorUid":"22737***",
   "subTaskStatus":1,
   "annotationTotalNum":10,
   "annotatedNum":5,
   "sampleRate":0.6,
   "checkTotalNum":6,
   "annotationTaskId":"at-97d1493908634*****",
   "annotatorName":"zhangsan",
   "annotationSubTaskId":"ast-eaf458f4040b9530*****",
   "checkerUid":"28337***",
   "checkedNum":2,
   "checkerName":"lisi"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### ListAnnotationSubTaskAnnotation

智能体工厂 OpenTrek 调用ListAnnotationSubTaskAnnotation查询所有的标注任务子任务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/subTask/listAnnotation HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Query | 否 | at- 97d11ca204c6b0493908 6340c***** | 数据标注任务ID。 |
| name | Strin g | Query | 否 | annotation-name | 数据标注任务名称。 |
| annotatio nSubTaskI d | Strin g | Query | 否 | ast- eaf458f4057ad04a540b 95308d***** | 数据标注子任务ID。 |
| subTaskSt atus | Integ er | Query | 是 | 1 | 数据标注子任务状态，取值范围： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 10：已完成。 |
| objectTyp e | Integ er | Query | 否 | 0 | 数据标注对象，取值范围： 0：图片。 1：文本。 |
| taskFlowT ype | Integ er | Query | 否 | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| taskFromT ype | Integ er | Query | 否 | 0 | 数据标注任务来源，取值范围： 0：分配。 1：转派。 2：驳回。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 10 | 子任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 1 | 分页查询时设置的每页行数。 默认值：10。 |
| Resource Group | Integ er | Query | 否 | 1 | 资源集。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - annotatedNum | Integer | 3 | 已标注数据量 |
| - annotationSub TaskId | String | ast- eaf458f4530***** | 数据标注子任务ID。 |
| - annotationTas kId | String | at- 97d11ca204c634** *** | 数据标注任务ID。 |
| - annotationTot alNum | Integer | 10 | 子任务中所有数据量 |
| - annotationTyp e | Integer | 0 | 标注类型，该参数必填，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |
| - annotatorNam e | String | zhangsan | 标注员名称 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -annotatorUid | String | 27889**** | 标注员对应的阿里云子账号id |
| - checkTotalNu m | Integer | 5 | 需验收的数据量 |
| -checkedNum | Integer | 2 | 已验收的数据量 |
| -checkerName | String | lisi | 验收员名称 |
| -checkerUid | String | 229787* | 验收员对应的阿里云子账号id |
| -name | String | 标注任务 | 名称 |
| -objectType | Integer | 1 | 标注对象类型： 0:图片 1:文本 |
| -sampleRate | Float | 1.0 | 采样率。 |
| - subTaskStatus | Integer | 1 | 数据标注子任务状态，取值范围： 0：待标注。 1：已标注。 2：待验收。 3：已验收。 10：已完成。 |
| -taskFlowType | Integer | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| -taskFromType | Integer | 0 | 任务来源： 0:分配 1:转派 2:被驳回 |
| totalCount | Integer | 10 | 标注任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageIndex | Integer | 1 | 标准任务的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataAnnotation/subTask/listAnnotation HTTP/1.1 &subTaskStatus=1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "taskFromType":0,
   "annotatorUid":"27889****",
   "subTaskStatus":1,
   "annotationTotalNum":10,
   "annotationType":0,
   "annotatedNum":3,
   "sampleRate":1.0,
   "checkTotalNum":5,
   "objectType":1,
   "annotationTaskId":"at-97d11ca204c634*****",
   "annotatorName":"zhangsan",
   "annotationSubTaskId":"ast-eaf458f4530*****",
   "checkerUid":"229787*",
   "checkedNum":2,
```

`"name":"`标注任务`",`

```json
   "checkerName":"lisi",
   "taskFlowType":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":10,
 "httpCode":200
}
```

#### GetAnnotationTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/task/get/[annotationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Path | 是 | at- 97d11ca204c6b0493908 634***** | 数据标注任务ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - annotatedSub TaskNum | Integer | 1 | 已标注完成的子任务数量。 |
| - annotationMet hodType | Integer | 0 | 标准方式： 0：人工标注。 1：自动标注。 |
| - annotationTas kId | String | at- 97d11ca204c6b04 93908634***** | 数据标注任务ID。 |
| - annotationTyp e | Integer | 1 | 标注类型，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |
| - checkedSubTa skNum | Integer | 1 | 完成验收的子任务数量。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - completedDat aNum | Integer | 10 | 已完成处理的数据条目数量。 |
| -datasetId | String | ds-7sda**** | 数据集ID。 |
| -datasetName | String | 待标注数据 | 数据集名称。 |
| - datasetVersion | String | v1 | 数据集版本。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| - isMustReadMa nual | Boolean | false | 是否必须阅读说明书，取值范围： true：是。 false：否。 默认值：false。 |
| -name | String | 数据标注QA | 名称。 |
| -objectType | Integer | 1 | 标注对象类型： 0：图片。 1：文本。 |
| - subTaskDataN um | Integer | 10 | 子任务的数据量。 |
| -subTaskNum | Integer | 5 | 子任务量。 |
| -taskFlowType | Integer | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| -taskStatus | Integer | 1 | 任务状态，取值范围： 0：初始化中。 1：标注中。 2：验收中。 3：已完成。 255：初始化失败。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -totalDataNum | Integer | 50 | 总数据量。 |
| - waitingAnnota tionSubTaskNu m | Integer | 4 | 待标注的子任务数量。 |
| - annotatorDistr ibuteStrategy | Struct | 结构体见子字段 | 标注员分配策略。 |
| --annotatorList | Array | 见子字段 | 标注员列表。 |
| --- aliyunSubUid | String | 1277043054***** | 阿里云子账号Uid。 |
| ---loginName | String | zhangsan | 阿里云子账号名称。 |
| -- distributeStrat egy | String | averageDistributio n | 分配策略。 |
| - checkerDistrib uteStrategy | Struct | 结构体见子字段 | 验收员分配策略。 |
| --checkerList | Array | 见子字段 | 验收员列表。 |
| --- aliyunSubUid | String | 1277043054***** | 阿里云子账号Uid。 |
| ---loginName | String | zhangsan | 阿里云子账号名称。 |
| -- samplingMeth od | String | dataSampling | 抽样规则。 |
| -- samplingPerce ntage | Integer | 100 | 抽样比例。 |
| - managerDistri buteStrategy | Struct | 结构体见子字段 | 管理员分配规则。 |
| --managerList | Array | 见子字段 | 管理员列表。 |
| --- aliyunSubUid | String | 1277043054***** | 阿里云子账号Uid。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---loginName | String | zhangsan | 阿里云子账号名称。 |

**示例**

请求示例

```
GET /dataAnnotation/task/get/[annotationTaskId] HTTP/1.1 &annotationTaskId=at-97d11ca204c6b0493908634*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "datasetVersion":"v1",
  "totalDataNum":50,
  "aliyunUid":"157123456789****",
  "annotatedSubTaskNum":1,
  "completedDataNum":10,
  "gmtCreated":"2017-11-27T06:51:26Z",
  "managerDistributeStrategy":{
   "managerList":[
    {
     "loginName":"zhangsan",
     "aliyunSubUid":"1277043054*****"
    }
```

]

```
  },
```

`"datasetName":"`待标注数据`",`

```json
  "annotationType":1,
  "subTaskDataNum":10,
  "isMustReadManual":false,
  "subTaskNum":5,
  "objectType":1,
  "checkerDistributeStrategy":{
   "samplingPercentage":100,
   "samplingMethod":"dataSampling",
   "checkerList":[
    {
     "loginName":"zhangsan",
     "aliyunSubUid":"2277043054*****"
    }
```

]

```json
  },
  "checkedSubTaskNum":1,
  "annotationTaskId":"at-97d11ca204c6b0493908634*****",
  "waitingAnnotationSubTaskNum":4,
  "annotationMethodType":0,
```

`"name":"`数据标注`QA",`

```json
"datasetId":"ds7sda****"
```

智能体工厂 OpenTrek

```json
  "datasetId":"ds-7sda****",
  "taskFlowType":0,
  "taskStatus":1,
  "annotatorDistributeStrategy":{
   "distributeStrategy":"averageDistribution",
   "annotatorList":[
    {
     "loginName":"zhangsan",
     "aliyunSubUid":"1277043054*****"
    }
```

]

```json
  }
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateAnnotationTask

调用UpdateAnnotationTask修改指定数据标注任务的部分信息，包括数据标注任务名称、描述以及人员配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/task/update/[annotationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Path | 是 | at- 97d11ca204c6b0493908 6340c***** | 数据标注任务ID。 |
| name | Strin g | Body | 否 | annotation-name | 数据标注任务名称，长度为 2～64个字符，必须以字母或中文开头，可包含数字、 半角句号（.）、下划线 （ ）和短划线（-）。 _ 注： 1. 更改任务名称时，该参数不能为空； 2. 更改人员配置时，该参数不做校验。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| descriptio n | Strin g | Body | 否 | annotation-description | 数据标注任务描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |
| annotator List | Strin g | Body | 否 | [{ "loginName": "admin", "aliyunSubUid": "23037432964*****" }] | 标注员列表。 |
| checkerLis t | Strin g | Body | 否 | [{ "loginName": "admin", "aliyunSubUid": "23037432964*****" }] | 验收员列表。 |
| managerL ist | Strin g | Body | 否 | [{ "loginName": "admin", "aliyunSubUid": "23037432964*****" }] | 管理员列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/task/update/[annotationTaskId] HTTP/1.1 { "annotationTaskId":"at-97d11ca204c6b04939086340c*****" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

**4.2.6.**

#### UpdateAnnotationDataAnnotationResult

调用UpdateAnnotationDataAnnotationResult修改标注数据结果。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/data/annotationUpdate/[annotationDataId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nDataId | Strin g | Path | 是 | ad- cf4b1c6900caa048bf095 ed05***** | 标注数据D。 |
| annotatio nResult | Strin g | Body | 否 | { "objects": [{ "name": "事件" }, { "name": "新闻" }] } | 标注结果。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/data/annotationUpdate/[annotationDataId] HTTP/1.1 { "annotationDataId":"ad-cf4b1c6900caa048bf095ed05*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateAnnotationTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataAnnotation/task/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Departme nt | Strin g | Body | 是 | 1 | 组织ID，该参数必填。 |
| Resource Group | Strin g | Body | 是 | 1 | 资源集ID，该参数必填。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Body | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID，该参数必填。 |
| datasetVe rsion | Strin g | Body | 否 | v1 | 数据集版本。 |
| name | Strin g | Body | 是 | annotation-name | 数据标注任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| descriptio n | Strin g | Body | 否 | annotation-description | 代码集描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| manual | Strin g | Body | 否 | 一本用户手册 | 任务说明书。 |
| isMustRea dManual | Boole an | Body | 是 | false | 是否必须阅读说明书，该参数必填，取值范围： true：是。 false：否。 默认值：false。 |
| objectTyp e | Integ er | Body | 是 | 0 | 数据标注对象，该参数必填，取值范围： 0：图片。 1：文本。 |
| annotatio nType | Integ er | Body | 是 | 1 | 标注类型，该参数必填，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskFlowT ype | Integ er | Body | 是 | 0 | 数据标注类型，该参数必填，取值范围： 0：标注。 1：标注-验收。 |
| subTaskD ataNum | Integ er | Body | 是 | 200 | 子任务的数据量，该参数必填。 |
| subTaskC anSkipDat aNum | Integ er | Body | 是 | 5 | 子任务可跳过的数据量，该参数必填。 |
| annotatio nLabelCon fig | Json | Body | 否 | { "isMultipleChoice": true, "labels": ["人名", "地名", "时间"] } | 标注标签配置。 |
| annotator Distribute Strategy | Json | Body | 是 | [{ "aliyunSubUid": "23783684****", "loginName": "李四" }] | 标注员分配策略，该参数必填。 |
| checkerDi stributeStr ategy | Json | Body | 是 | [{ "aliyunSubUid": "23783684****", "loginName": "李四" }] | 验收员分配策略，该参数必填。 |
| managerD istributeSt rategy | Json | Body | 是 | [{ "aliyunSubUid": "23783684****", "loginName": "李四" }] | 管理员分配策略，该参数必填。 |
| llmGenera tionParam Config | Json | Body | 否 | { "datasetId": "ds- f453ede15d3****", "name": "图片标注任务 12.27-1", "llmGenerationParamCo nfig":{ "temperature":0.1, "top p":0.9 } } _ | 调用LLM生成的配置参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "annotationTaskId" : "at-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataAnnotation/task/create HTTP/1.1 { "Department":"1", "ResourceGroup":"1", "datasetId":"ds-3dc49fc087b3491cafa76b5d842****", "name":"annotation-name", "isMustReadManual":"false", "objectType":"0", "annotationType":"1", "taskFlowType":"0", "subTaskDataNum":"200", "subTaskCanSkipDataNum":"5", "annotatorDistributeStrategy":"[{
 "aliyunSubUid": "23783684****",
 "loginName": "李四"
}]", "checkerDistributeStrategy":"[{
 "aliyunSubUid": "23783684****",
 "loginName": "李四"
}]", "managerDistributeStrategy":"[{
 "aliyunSubUid": "23783684****",
 "loginName": "李四"
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"annotationTaskId\": \"at-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### UpdateAnnotationSubTaskCheck

调用UpdateAnnotationSubTaskCheck修改指定数据标注子任务的状态和验收反馈信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/subTask/checkUpdate/[annotationSubTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nSubTaskI d | Strin g | Path | 是 | ast- eaf458f4057ad04a540b 9530**** | 数据标注子任务ID。 |
| taskStatus | Integ er | Body | 是 | 0 | 数据标注子任务状态，该参数必填，取值范围： 0：待标注。 3：已验收。 |
| checkMes sage | Strin g | Body | 否 | "" | 验收反馈信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
PUT /dataAnnotation/subTask/checkUpdate/[annotationSubTaskId] HTTP/1.1 { "annotationSubTaskId":"ast-eaf458f4057ad04a540b9530****", "taskStatus":"0" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

**4.2.9.**

#### UpdateAnnotationTaskAlreadyReadManual

调用UpdateAnnotationTaskAlreadyReadManual修改指定数据标注任务标注说明状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/task/updateAlreadyReadManual/[annotationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Path | 是 | at- 8870154d05c9f047b70a 5f306c9***** | 数据标注任务ID。 |
| isAlreadyR eadManua l | Boole an | Body | 是 | false | 标注说明是否已读，该参数必填，取值范围： true：是。 false：否。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/task/updateAlreadyReadManual/[annotationTaskId] HTTP/1.1 { "annotationTaskId":"at-8870154d05c9f047b70a5f306c9*****", "isAlreadyReadManual":"false" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetAnnotationConfig

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
GET /dataAnnotation/subTask/getConfig/[annotationSubTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nSubTaskI d | Strin g | Path | 是 | ast- eaf458f4057ad04a540b 9530***** | 数据标注子任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -labels | List | [ "历史", "新闻" ] | 标签信息。 |
| - annotationMet hodType | Integer | 0 | 标准方式。 0：人工标注 1：自动标注 |
| - annotationTas kId | String | at- 97d11ca204c6086 34***** | 数据标注任务ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - annotationTyp e | Integer | 0 | 标注类型，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |
| - annotatorNam e | String | zhangsan | 标注人员名称。 |
| - isAlreadyRead Manual | Boolean | true | 标注说明是否已读。 true：是。 false：否。 |
| - isMultipleChoic e | Boolean | false | 是否为多选标签。 true： 是。 false：否。 |
| - isMustReadMa nual | Boolean | false | 是否必须阅读说明书： true：是。 false：否。 |
| -name | String | 标注任务 | 名称。 |
| -objectType | Integer | 1 | 标注对象类型，取值范围： 0：图片。 1：文本。 |
| -sampleRate | Float | 1.0 | 抽检采样率。 |
| - subTaskCanSk ipDataNum | Integer | 2 | 子任务可跳过的数据量。 |
| - subTaskDataN um | Integer | 10 | 子任务的数据量。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskFlowType | Integer | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| -taskStatus | Integer | 1 | 任务状态，取值范围： 0：初始化中。 1：标注中。 2：验收中。 3：已完成。 255：初始化失败。 |

**示例**

请求示例

```
GET /dataAnnotation/subTask/getConfig/[annotationSubTaskId] HTTP/1.1 &annotationSubTaskId=ast-eaf458f4057ad04a540b9530*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "annotationType":0,
  "subTaskDataNum":10,
  "sampleRate":1.0,
  "isMultipleChoice":false,
  "isMustReadManual":false,
  "labels":"[   \"历史\",  \"新闻\"]",
  "isAlreadyReadManual":true,
  "objectType":1,
  "annotationTaskId":"at-97d11ca204c608634*****",
  "annotatorName":"zhangsan",
  "annotationMethodType":0,
```

`"name":"`标注任务`",`

```json
  "taskFlowType":0,
  "subTaskCanSkipDataNum":2,
  "taskStatus":1
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### DeleteAnnotationTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /dataAnnotation/task/delete/[annotationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Path | 是 | at- 97d11ca204c6b0493908 634***** | 数据标注任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /dataAnnotation/task/delete/[annotationTaskId] HTTP/1.1 &annotationTaskId=at-97d11ca204c6b0493908634*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateAnnotationSubTaskReassign

调用UpdateAnnotationSubTaskReassign进行转派子任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/subTask/reassign/[annotationSubTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nSubTaskI d | Strin g | Path | 是 | ast- eaf458f4057ad04a540b 9530***** | 数据标注子任务ID。 |
| assignedT oAnnotato rUid | Strin g | Body | 否 | 12770430548***** | 转派给标注员ID。 |
| assignedT oChecker Uid | Strin g | Body | 否 | 12770430548***** | 转派给验收员ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/subTask/reassign/[annotationSubTaskId] HTTP/1.1 { "annotationSubTaskId":"ast-eaf458f4057ad04a540b9530*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListAnnotationTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/task/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nTaskId | Strin g | Query | 否 | at- 97d11ca204c6b0493908 6340***** | 数据标注任务ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Query | 否 | annotation-name | 数据标注任务名称。 |
| aliyunSub Uid | Strin g | Query | 否 | 1277043054***** | 阿里云子账号Uid。 |
| taskFlowT ype | Integ er | Query | 否 | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| datasetId | Strin g | Query | 否 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |
| taskStatus | Integ er | Query | 否 | 1 | 任务状态，取值范围： 0：初始化中。 1：标注中。 2：验收中。 3：已完成。 255：初始化失败。 |
| objectTyp e | Integ er | Query | 否 | 0 | 数据标注对象，取值范围： 0：图片。 1：文本。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据标注任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - managerName List | List | ["admin"] | 任务管理员列表。 |
| - managerUidLis t | List | ["113776****"] | 任务管理员ID列表。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - annotatedSub TaskNum | Integer | 1 | 已人工标注完成的子任务数量。 |
| - annotationMet hodType | Integer | 1 | 标注方式。 0：人工标注。 1：自动标注。 |
| - annotationTas kId | String | at- 97d11ca204c6b34 ***** | 数据标注任务ID。 |
| - annotationTyp e | Integer | 1 | 标注类型，该参数必填，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |
| - checkedSubTa skNum | Integer | 1 | 已验收子任务数量。 |
| - completedDat aNum | Integer | 5 | 已完成处理的数据条目数量。 |
| -datasetId | String | ds-dfasf*** | 数据集ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -datasetName | String | 文本待标注数据 | 数据集名称。 |
| - datasetVersion | String | v1 | 数据集版本。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| - isMustReadMa nual | Boolean | false | 是否必须阅读说明书，取值范围： true：是。 false：否。 默认值：false。 |
| -name | String | 文本标注任务 | 名称。 |
| -objectType | Integer | 1 | 标注对象类型： 0：图片。 1：文本。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - subTaskDataN um | Integer | 2 | 子任务的数据量。 |
| -subTaskNum | Integer | 3 | 子任务数量。 |
| -taskFlowType | Integer | 0 | 数据标注类型，取值范围： 0：标注。 1：标注-验收。 |
| -taskStatus | Integer | 1 | 任务状态： 0：初始化中。 1：标注中。 2：验收中。 255：初始化失败。 |
| -totalDataNum | Integer | 100 | 数据总量。 |
| - waitingAnnota tionSubTaskNu m | Integer | 1 | 待标注的子任务数量。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| totalCount | Integer | 100 | 数据标注任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 数据标注任务的页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataAnnotation/task/list HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "managerNameList":"[\"admin\"]",
   "datasetVersion":"v1",
   "totalDataNum":100,
   "aliyunUid":"157123456789****",
   "annotatedSubTaskNum":1,
   "completedDataNum":5,
   "gmtCreated":"2017-11-27T06:51:26Z",
   "managerUidList":"[\"113776****\"]",
```

`"datasetName":"`文本待标注数据`",`

```json
   "annotationType":1,
   "subTaskDataNum":2,
   "isMustReadManual":false,
   "subTaskNum":3,
   "objectType":1,
   "checkedSubTaskNum":1,
   "annotationTaskId":"at-97d11ca204c6b34*****",
   "waitingAnnotationSubTaskNum":1,
   "regionId":"cn-hangzhou",
   "annotationMethodType":1,
```

`"name":"`文本标注任务`",`

```json
   "datasetId":"ds-dfasf***",
   "taskFlowType":0,
   "taskStatus":1
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### UpdateAnnotationDataCheckResult

调用UpdateAnnotationDataCheckResult修改指定标注数据验收结果。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/data/checkUpdate/[annotationDataId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nDataId | Strin g | Path | 是 | ad- cf4b1c6900caa048bf095 ***** | 标注数据ID。 |
| checkStat us | Integ er | Body | 否 | 1 | 验收状态：取值范围： 0：待验收。 1：验收通过。 2：验收不通过。 |
| checkMes sage | Strin g | Body | 否 | 命中xxx规则，请修改后重试 | 验收反馈信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/data/checkUpdate/[annotationDataId] HTTP/1.1 { "annotationDataId":"ad-cf4b1c6900caa048bf095*****" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListAnnotationData

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/data/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nSubTaskI d | Strin g | Query | 是 | ast- eaf458f4057ad04a540b 9530***** | 数据标注子任务ID。 |
| isOnlyChe ckData | Boole an | Query | 否 | false | 查询数据类型，取值范围： true：查询标注数据。 false：查询验收数据。 默认值：false。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - annotationDat aId | String | ad- cf4b1c65ed05***** | 标注数据ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - annotationStat us | Integer | 1 | 标注状态： 0:未标注 1:已标注 |
| - annotationTas kId | String | at-97d11ca24***** | 数据标注任务ID。 |
| - annotatorNam e | String | zhangsan | 标注人员名称。 |
| -annotatorUid | String | 2377788*** | 标注人员阿里云子账号id |
| -checkStatus | Integer | 1 | 审核状态： 0:未验收 1:验收通过 2:验收不通过（驳回） |
| -checkerName | String | lisi | 审核员名称 |
| -checkerUid | String | 27898*** | 验收员阿里云子账号id |
| -source | String | 待标注数据内容 | 数据内容 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataAnnotation/data/list HTTP/1.1 &annotationSubTaskId=ast-eaf458f4057ad04a540b9530*****
```

&公共请求参数智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "checkStatus":1,
   "annotationTaskId":"at-97d11ca24*****",
   "annotatorUid":"2377788***",
   "annotatorName":"zhangsan",
   "checkerUid":"27898***",
   "annotationStatus":1,
   "checkerName":"lisi",
   "annotationDataId":"ad-cf4b1c65ed05*****",
```

`"source":"`待标注数据内容"

```
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateAnnotationSubTaskAnnotation

调用UpdateAnnotationSubTaskAnnotation更新数据标注子任务状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataAnnotation/subTask/annotationUpdate/[annotationSubTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nSubTaskI d | Strin g | Path | 是 | ast- eaf458f4057ad04a540b 95***** | 数据标注子任务ID。 |
| taskStatus | Integ er | Body | 是 | 1 | 子任务状态，该参数必填， 取值范围： 1：已标注。 2：待验收。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataAnnotation/subTask/annotationUpdate/[annotationSubTaskId] HTTP/1.1 { "annotationSubTaskId":"ast-eaf458f4057ad04a540b95*****", "taskStatus":"1" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateAnnotationPromptTemplate

调用CreateAnnotationPromptTemplate创建标注任务模版。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /dataAnnotation/promptTemplate/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| usageTyp e | Integ er | Body | 是 | 0 | 使用场景，该参数必填，取值范围： 标注场景：0。 生成场景：1。 |
| sourceTyp e | Integ er | Body | 是 | 0 | 来源类型，该参数必填，取值范围： 系统内置：0。 用户录入：1。 |
| annotatio nType | Integ er | Body | 是 | 1 | 标注类型，该参数必填，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 6：文本-QA。 |
| labelConfi gType | Integ er | Body | 是 | 0 | 标签类型，该参数必填，取值范围： 无标签：0。 单标签：1。 多标签：2。 |
| name | Strin g | Body | 是 | QAprompt模版 | prompt模版名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| descriptio n | Strin g | Body | 否 | QAprompt模版生成QA使用 | prompt模版描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |
| systemCo ntent | Strin g | Body | 否 | 你是一个有用的数据标注智能助手 | 系统指令。 |

|  | 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| userConte nt | Strin g | Body | 是 | 请根据给定的内容标注1- 3QA对，返回为json格式。 | 用户指令，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "annotationPrompt TemplateId": "apt-- 575011c0045fd0** ***" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataAnnotation/promptTemplate/create HTTP/1.1 { "usageType":"0", "sourceType":"0", "annotationType":"1", "labelConfigType":"0", "name":"QAprompt模版",
```

`"userContent":"`请根据给定的内容标注`1-3QA`对，返回为`json`格式。"

```
}
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{      \"draftId\": \"draft-575011c0045fd0*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListAnnotationPromptTemplate

调用ListAnnotationPromptTemplate查询相关的标注Prompt模版列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataAnnotation/promptTemplate/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| promptTe mplateId | Strin g | Query | 否 | apt-sadfay8*** | 用于标识特定提示模板的唯一ID。 |
| name | Strin g | Query | 否 | 文本QA标注模版 | 标注模版名称。 |
| usageTyp e | Integ er | Query | 是 | 0 | 设备使用性质，该参数必填，取值范围： 标注场景：0。 生成场景：1。 |
| sourceTyp e | Integ er | Query | 是 | camera | 源类型，该参数必填，取值范围： 系统内置：0。 用户录入：1。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| annotatio nType | Integ er | Query | 是 | 1 | 标注类型，该参数必填，取值范围： 0：文本-分类。 1：文本-实体识别。 2：图片-描述。 3：图片-QA。 4：图片-分类。 5：图片-目标检测。 6：文本-QA。 |
| labelConfi gType | Integ er | Query | 是 | 0 | 标签类型，该参数必填，取值范围： 无标签：0。 单标签：1。 多标签：2。 |
| pageIndex | Integ er | Query | 否 | 10 | 标注模版列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - annotationPro mptTemplateI d | String | apt-textQA | 标注Prompt模版ID。 |
| - annotationTyp e | Integer | 0 | 模版用途类型： 0：数据标注。 |
| -description | String | 文本分类 | 模板描述。 |
| -gmtCreated | String | 2026-02- 27T06:00:18Z | 创建时间。 |
| -gmtModified | String | 2026-02- 27T06:00:18Z | 修改时间。 |
| -id | Integer | 1 | ID。 |
| -isDeleted | Boolean | 0 | 删除状态。 0：未删除。 1：已删除。 |
| - labelConfigTyp e | Integer | 0 | 标签配置类型： 0：无标签。 1：标签单选。 2：标签多选。 |
| -name | String | 文本QA标注 | 模版名称。 |
| -sourceType | Integer | 0 | 模版类型： 0：系统内置。 1：用户录入。 |
| - systemConten t | String | 你是一个根据文本可自动生成问答对的专家。 | 系统指令。 |
| -usageType | Integer | 0 | 模版用途类型： 0：数据标注。 1：数据生成。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -userContent | String | 【任务描述】 请根据 【待分析内容】生成1 到3个问答对,在生成的问答对精准的情况下越多越好，整体不要超过3对，问题和答案必须严格符合给定的【待分析内容】中描述的事实。 【待分析内容】 ${text} 【输出结果参考】 输出格式: "{"objects": [{"question": "中国的首都是？","answer": "北京"},{"question": "浙江的省会是？","answer": "杭州"}]}" 特别注意: 注意一定要遵循输出结果格式为JSON,不要输出markdown格式！ 结果不要包含任何 JSON格式之外的字符！ | 用户指令。 |
| totalCount | Integer | 1 | 总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 页码。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataAnnotation/promptTemplate/list HTTP/1.1
```

&公共请求参数正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":[
  {
   "gmtModified":"2026-02-27T06:00:18Z",
   "aliyunUid":"157123456789****",
   "annotationPromptTemplateId":"apt-textQA",
   "gmtCreated":"2026-02-27T06:00:18Z",
   "labelConfigType":0,
   "annotationType":0,
```

`"description":"`文本分类`",` `"systemContent":"`你是一个根据文本可自动生成问答对的专家。`",`

```json
   "isDeleted":false,
   "sourceType":0,
```

`"userContent":"`【任务描述】请根据【待分析内容】生成1到3个问答对,在生成的问答对精准的情况下越多越好，整体不要超过3对，问题和答案必须严格符合给定的【待分析内容】中描述的事实。【待分析内容】${text}【输出结果参考】输出格式:\"{\"objects\": [{\"question\": \"中国的首都是？\",\"answer\": \"北京 \"},{\"question\": \"浙江的省会是？\",\"answer\": \"杭州\"}]}\" 特别注意: 注意一定要遵循输出结果格式为`JSON,`不要输出`markdown`格式！结果不要包含任何`JSON`格式之外的字符！`",` `"name":"`文本`QA`标注`",`

```json
   "id":1,
   "usageType":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":1,
 "httpCode":200
}
```

### 数据生成

#### CreateDataGenerationTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataGeneration/task/create HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| datasetId | Strin g | Body | 是 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID，该参数必填。 |
| datasetVe rsion | Strin g | Body | 是 | v1 | 数据集版本，该参数必填。 |
| name | Strin g | Body | 否 | 生成任务1 | 数据标注任务名称，长度为 2～128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | 生成任务描述123 | 数据标注任务描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |
| objectTyp e | Integ er | Body | 是 | 0 | 数据标注对象，该参数必填，取值范围： 0：图片。 1：文本。 |
| generatio nType | Integ er | Body | 是 | 101 | 标注类型，该参数必填，取值范围： 101：SFT数据增强。 |
| detailConf ig | Strin g | Body | 否 | { "generationDataNum":5 0 } | 数据生成详细配置，比如生成条数等。 |
| useUserPr omptTem plate | Boole an | Body | 否 | false | 自动标注时是否使用用户编辑后的标注模版。 |
| userProm ptTemplat eContent | Strin g | Body | 否 | 请根据一些要求生成数据, 要求1：*** | 用户编辑后的标注模版内容。 |
| autoAnnot ationServi ceId | Strin g | Body | 否 | os-sd7sa7d7ds*** | 推理服务Id。 |
| llmGenera tionParam Config | Json | Body | 否 | { "temperature":0.0, "top p":0.9 } _ | 推理服务入参高级配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "generationTaskId" : "gt-6f07***" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataGeneration/task/create HTTP/1.1 { "datasetId":"ds-3dc49fc087b3491cafa76b5d842****", "datasetVersion":"v1", "objectType":"0", "generationType":"101" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"draftId\": \"draft-575011c0045fd0*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteDataGenerationTask

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /dataGeneration/task/delete/[generationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| generatio nTaskId | Strin g | Path | 是 | gt-sdysu6d*** | 数据生成任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /dataGeneration/task/delete/[generationTaskId] HTTP/1.1 &generationTaskId=gt-sdysu6d***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### DeleteGenerationData

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /dataGeneration/data/delete/[dataId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataId | Strin g | Path | 是 | gd-ddd7ysdy*** | 数据ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /dataGeneration/data/delete/[dataId] HTTP/1.1 &dataId=gd-ddd7ysdy***
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateDataGenerationTask

调用UpdateDataGenerationTask修改数据生成任务的部分信息，包括数据生成任务名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataGeneration/task/update/[generationTaskId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| generatio nTaskId | Strin g | Path | 是 | gt-fsu8fys8afs***** | 数据生成任务ID。 |
| name | Strin g | Body | 否 | name | 数据生成任务名称，长度为 2～128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | annotation-description | 数据生成任务描述，描述长度为2~256个字符，不能以 http://和https://开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataGeneration/task/update/[generationTaskId] HTTP/1.1 { "generationTaskId":"gt-fsu8fys8afs*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateGenerationData

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /dataGeneration/data/update/[dataId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| dataId | Strin g | Path | 是 | gtd-df9860cd0fc8***** | 生成数据ID。 |
| result | Strin g | Body | 否 | {\"messages\": [{\"role\":\"user\",\"cont ent\":\"一年有几个季度？ \"}, {\"role\":\"assistant\",\"c ontent\":\"4个。\"}, {\"role\":\"system\",\"co ntent\":\"You are a helpful assistant\"}]} | 更新结果，格式为转义后的 Json字符串。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /dataGeneration/data/update/[dataId] HTTP/1.1 { "dataId":"gtd-df9860cd0fc8*****" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### NoteBook建模

#### ModifyNotebookSSHAccess

调用ModifyNotebookSSHAccess修改指定NotebookSSH访问。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-ssh HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 8c16aa9502e12042930 bc750e7ec**** | Notebook建模ID，该参数必填。 |
| slbRegistr yId | Strin g | Body | 否 | lb-***** | SLB注册ID。 |
| sshPort | Integ er | Body | 否 | 22 | SSH端口号。 |
| sshClassic NetworkA ccess | Boole an | Body | 是 | false | 是否开启经典网络SSH访问，该参数必填，取值范围： true：开启。 false：禁用。 |
| sshStatus | Boole an | Body | 否 | false | SSH状态。 |
| sshPublicK ey | Strin g | Body | 否 | ssh-rsa AAAAB3NzaC1****** | SSH公钥。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
PUT /notebook/modify-ssh HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyNotebookStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-status HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 05fec54408c6d0460c08 9de038c**** | Notebook建模ID，该参数必填。 |
| notebookS tatus | Boole an | Body | 是 | true | Notebook建模状态，该参数必填，取值范围： true：启动。 false：停止。 |
| slbRegistr yId | Strin g | Body | 否 | lb-***** | SLB注册ID。 |
| sshPort | Integ er | Body | 否 | 80 | SSH端口号。 |
| notebookS erviceCon fig | Json | Body | 否 | [ { "classicNetworkAccess": true, "sortOrder": 0, "vpcAccess": false, "servicePort": "90", "slbRegistryName": "kuoyi ipv4 6", _ _ "serviceName": "demo- 01", "slbRegistryId": "lb- ****", "targetPort": "2090", "classicNetworkAccessP ort": "90", "classicNetworkAccessIp ": "10.17.82.111" } ] | Notebook服务配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
PUT /notebook/modify-status HTTP/1.1 { "notebookId":"nb-05fec54408c6d0460c089de038c****", "notebookStatus":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateNotebook

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /notebook/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebook Name | Strin g | Body | 是 | notebook-name | Notebook名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| notebook Desc | Strin g | Body | 否 | notebook-desc | Notebook描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookT ype | Integ er | Body | 否 | 1 | Notebook类型，取值范围： 1：jupyterlab。 2：vscode。 3： jupyterlab+vscode。 |
| imageId | Strin g | Body | 是 | img- e87443ff0d37904e860a 4e90b75fa**** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | CPU大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 3 | 内存大小，单位为GB，该参数必填。 |
| sharedMe mCount | Integ er | Body | 否 | 2 | 共享内存大小，单位为GB。 |
| gpuMemC ount | Integ er | Body | 否 | 0 | 显存大小，单位为GB。 |
| gpuCount | Integ er | Body | 是 | 0 | GPU大小，单位为卡，该参数必填。 |
| notebook Account | Strin g | Body | 是 | ad**** | Notebook账户，该参数必填。 |
| notebookP assword | Strin g | Body | 否 | note***** | Notebook密码。 |
| notebookP ort | Strin g | Body | 否 | 80 | Notebook端口，可不填。 |
| sshStatus | Integ er | Body | 否 | 0 | SSH状态，取值范围： 0：禁用。 1：启用。 |
| sshPublicK ey | Strin g | Body | 否 | ssh-rsa AAAAB3NzaC1****** | SSH公钥，当sshStatus值为1时，该参数不能为空。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| slbRegistr yId | Strin g | Body | 否 | lb-*** | SLB注册ID。 |
| slbRegistr yName | Strin g | Body | 否 | lb-name | SLB注册名称。 |
| sshClassic NetworkA ccess | Strin g | Body | 否 | 1 | SSH经典访问状态，取值范围： 0：禁用。 1：启用。 |
| sshPort | Integ er | Body | 否 | 2201 | SSH服务使用的端口号。 |
| datasetMo untList | Json | Body | 否 | [{ "mountPath": "/data", "datasetId": "ds- 5740734ff2cf4a00bc6da 4*****", "dataAccInstance": null }] | 数据集配置。 |
| modelMou ntList | Json | Body | 否 | [{ "mountPath": "/data", "modelId": "md- fce5c8bf03ba604a350b 9c907e3*****", "modelVersion": "v1", "modelType": 1, "dataAccInstance": null }] | 模型库配置。 |
| codeMoun tList | Json | Body | 否 | [] | 代码集配置，可不填。 |
| storageMo untList | Json | Body | 否 | [{ "quotaId": "rq- d8890a98089c2041d80 86bb0b2e27****", "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| nodeConfi gList | Json | Body | 否 | [] | 节点配置，可不填。 |
| autoShutd ownStatus | Boole an | Body | 否 | 0 | 自动停止启用状态，取值范围： 0：未启用。 1：启用。 设置后，将在指定时间强行停止该实例，请谨慎设置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| autoShutd ownTime | Strin g | Body | 否 | 2025-09- 29T16:00:00.000Z | 启用自动停止时，设置的自动停止的时间。日期时间采用 ISO 8601 格式。 |
| startCom mand | Strin g | Body | 否 | sleep 300 | 初始化命令。 执行初始化命令会导致实例启动时间变长，请谨慎在其中执行长耗时命令。 |
| notebookE nvConfig | Json | Body | 否 | [ { "code": "myenv", "value": "custom" } ] | 实例运行的环境变量信息。 |
| notebookS erviceCon fig | Json | Body | 否 | [ { "vpcAccess": true, "serviceName": "demo", "targetPort": 9000, "servicePort": 9001 } ] | 配置Notebook实例中服务的外部访问。支持VPC网络或经典网络访问。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "notebookId": "nb-****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /notebook/create HTTP/1.1 { "notebookName":"notebook-name", "imageId":"img-e87443ff0d37904e860a4e90b75fa****", "imageVersion":"v1", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "cpuCount":"1", "memCount":"3", "gpuCount":"0", "notebookAccount":"ad****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"notebookId\": \"nb-****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteNotebook

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Query | 是 | nb- 8c16aa9502e12042930 bc750e7ec**** | notebook建模ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&notebookId=nb-8c16aa9502e12042930bc750e7ec****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetNotebook

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Query | 是 | nb-6f95****0004eff | Notebook唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds- c3de****0804b03 | 数据集ID。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -- datasetFileNa me | String | data.csv | 数据集文件名。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --pvcName | String | null | PVC名称。 |
| -- dataAccInstan ce | String | da-xxxxxxxxx | 数据加速实例。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |
| --modelId | String | md-gallery- 0a89****0418b | 模型ID。 |
| --modelName | String | qwen-model | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| -- dataAccInstan ce | String | da-xxxxxxxxx | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |
| - codeMountList | Array | [] | 代码库挂载列表。 |
| --codeId | String | cd- 2e0c****0e04d24 | 代码库ID。 |
| --codeName | String | my-code-repo | 代码库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -- storageSource | Integer | 1 | 存储来源。 |
| --storagePath | String | oss://xxxxx.rm.com / | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | 2 | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --cpuCount | Integer | 1 | CPU数量。 |
| --memCount | Integer | 1 | 内存大小（GB）。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| -- gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| --gpuCount | Integer | 0 | GPU数量。 |
| -- startCommand | String | sleep 100 | 初始化命令。 |
| - imageExportLi st | Array | [] | 制作镜像信息列表。 |
| -- gpuManufactu rerList | List | [] | GPU厂商列表。 |
| -- componentList | List | [] | 组件信息列表。 |
| --gmtCreated | String | 2025-11- 13T08:10:12Z | 创建时间。 |
| --gmtModified | String | 2025-11- 13T08:10:12Z | 修改时间。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --aliyunUid | String | 198226****1225 | 阿里云账号。 |
| --regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| --exportId | String | ei- 93c7****56404421 | 镜像导出ID。 |
| --imageId | String | img- 7f2c****5040f6 | 镜像ID。 |
| --imageName | String | nvidia-pytorch- jupyter | 镜像名称。 |
| --imageDesc | String | xxxxx | 镜像描述。 |
| -- imageVersion | String | 2.2.0.1-3.2304- cu121 | 镜像版本。 |
| -- imageNamesp ace | String | acr-aipaas | ACR镜像空间。 |
| --imageRepo | String | nvidia-pytorch- jupyter | 镜像仓库。 |
| -- imageRepoTag | String | 2.2.0.1-3.2304- cu121 | 镜像仓库Tag。 |
| -- imageAddress | String | cr-ee.registry.cn- xxxxx.arm.com/acr -aipaas/nvidia- pytorch- jupyter:2.2.0.1- 3.2304-cu121 | 镜像地址。 |
| --imageSize | String | 4701329799 | 镜像大小（字节）。 |
| -- availableServi ce | Integer | 0 | 可用服务。 |
| --frameWork | Integer | 2 | 镜像框架。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型。枚举值： 0 -IMAGE(普通镜像)， 1 -ACCELERATED IMAGE(加速镜 _ 像)。 |
| --imageStatus | Integer | 1 | 镜像状态。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuDriver | String | null | GPU驱动(已废弃）。 |
| - notebookEnvC onfig | Array | [] | Notebook环境变量配置列表。 |
| --code | String | PYTHONPATH | 环境变量名。 |
| --value | String | /usr/local/lib/pytho n3.10 | 环境变量值。 |
| - notebookServi ceConfigList | Array | [] | Notebook自定义服务配置列表。 |
| --serviceName | String | vscode-14817ae4 | 服务名称。 |
| --targetPort | String | 8080 | 目标端口。 |
| --vpcAccess | Boolean | false | 是否启用VPC访问。 |
| -- classicNetwork Access | Boolean | true | 是否启用经典网络访问。 |
| --servicePort | String | 8080 | 服务端口。 |
| --vpcAccessIp | String | 172.123.123.123 | VPC访问IP。 |
| -- vpcAccessPort | String | 22 | VPC访问端口。 |
| -- classicNetwork AccessIp | String | 10.123.123.123 | 经典网络访问IP。 |
| -- classicNetwork AccessPort | String | 23 | 经典网络访问端口。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --storageId | String | ts- e42a****3204003 | 第三方存储ID。 |
| --occupantId | String | nb- ff49****22304cae | 资源ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- storageSubPat h | String | /mnt/data/ | 存储子路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -gmtCreated | String | 2025-11- 13T08:10:12Z | 创建时间。 |
| -gmtModified | String | 2025-11- 13T08:10:12Z | 修改时间。 |
| -aliyunUid | String | 198226****1225 | 阿里云账号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -failedMsg | String | null | 失败信息。 |
| -notebookId | String | nb-6f95****0004eff | Notebook唯一标识ID。 |
| - notebookNam e | String | ll | Notebook名称。 |
| -notebookDesc | String | xxxxxx | Notebook描述。 |
| -notebookType | Integer | 1 | Notebook类型。枚举值： 1 - JUPYTER， 2 -VSCODE。 |
| - notebookStatu s | Integer | 2 | Notebook状态。枚举值： 0 -启动中 (starting)， 1 -运行中(running)， 2 -已停止(stopped)， 3 -失败(failed)， 4 -等待启动(waiting for starting)， 5 -变配中 (scaling)， 6 -停止中(stopping)。 |
| -imageId | String | img- 7f2c****5040f6 | 镜像ID。 |
| -imageVersion | String | 2.2.0.1-3.2304- cu121 | 镜像版本。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageName | String | nvidia-pytorch- jupyter | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型。枚举值： 0 -PUBLIC(公共镜像)， 1 -CUSTOM(自定义镜像)。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型。枚举值： 0 -IMAGE(普通镜像)， 1 -ACCELERATED IMAGE(加速镜 _ 像)。 |
| -quotaId | String | rq- 394c****ed104499 | 配额ID。 |
| -quotaName | String | A800高网资源配额 | 配额名称。 |
| -cpuCount | Integer | 1 | CPU数量。 |
| -memCount | Integer | 1 | 内存大小（GB）。 |
| - sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| - gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| -gpuCount | Integer | 0 | GPU数量。 |
| - gpuLabelCoun t | Integer | 0 | GPU虚拟化卡数量。 |
| -gpuMemTotal | Integer | 0 | 显存总量（GB）。 |
| -gpuCountUnit | Integer | null | GPU数量单位。 |
| - gpuMemTotal Unit | Integer | null | 显存总量单位。 |
| - notebookAcco unt | String | admin | Notebook登录账户。 |
| -tensorboard | Boolean | false | 是否开启TensorBoard。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 |  |  | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| -endpoint | String |  |  | https://10.*****.10 0/nb- 93a*****e804f43/ju pyter/ | Notebook访问Endpoint。 |  |  |
| - vscodeEndpoi nt | String |  |  | https://10.*****.10 0/nb- 93a*****e804f43/c odeserver/ | VSCode访问Endpoint。 |  |  |
| - jupyterEndpoi nt | String |  |  | https://10.*****.10 0/nb- 93a*****e804f43/ju pyter/ | Jupyter访问Endpoint。 |  |  |
| -accessType | Boolean |  |  | true | 访问类型。 |  |  |
| -sshStatus | Boolean |  |  | true | SSH是否启用。 |  |  |
| -sshPublicKey | String |  |  | ssh-rsa AAAA****Ts= | SSH公钥。 |  |  |
| - sshClassicNet workAccess | Boolean |  |  | true | 是否启用SSH经典网络访问。 |  |  |
| - sshClassicNet workAccessIp | String |  |  | 10.123.123.123 | 经典网络SSH访问IP。 |  |  |
| - sshClassicNet workAccessPor t | Integer |  |  | 22 | 经典网络SSH访问端口。 |  |  |
| - sshClassicNet workAccessSta tus | Boolean |  |  | true | 经典网络SSH访问健康检查状态。 |  |  |
| -gpuType | Integer |  |  |  | GPU类型。枚举值： NO LIMIT -不限 _ 制， NVIDIA Ampere A100 80G NVLink _ _ _ _ -A100 80G， NVIDIA Ampere A800 80G NVLink _ _ _ _ -A800 80G， Hygon Kongming DCUK100 AI PCIE _ _ _ _ 64G -海光DCU K100 _ 64G， HUAWEI DaVinci Ascend910B1 - _ _ 华为昇腾 910B1， Baidu kunlun P800 OAM 96G - _ _ _ _ 百度昆仑P800 96G， PG1 A910E -PPU _ A910E， OTHER -其他。 |  |  |
|  |  |  |  |  |  | Hygon Kongming DCUK100 AI PCIE _ _ _ _ |  |
|  |  |  |  | NVIDIA Ampere A1 |  |  |  |
|  |  | ger |  | _ _ 00 80G NVLink _ _ | 64G _ |  |  |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - autoShutdown Status | Boolean | false | 是否启用定时关机。 |
| - autoShutdown Time | String | 2026-03- 05T10:00:00Z | 定时关机时间。 |
| - startCommand | String | sleep 100 | 初始化命令。 |
| -instanceCost | Struct | {} | 实例费用信息。 |
| --runningCost | Float | 0.00 | 运行中费用。 |
| --runningPod | Float | 0 | 运行中Pod数。 |
| --runningCpu | Float | 0 | 运行中CPU数。 |
| --runningMem | Float | 0 | 运行中内存数。 |
| --runningGpu | Float | 0 | 运行中GPU数。 |
| -- runningGpuMe m | Float | 0 | 运行中GPU显存数。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 0 | 总Pod数。 |
| --totalCpu | Float | 0 | 总CPU数。 |
| --totalMem | Float | 0 | 总内存数。 |
| --totalGpu | Float | 0 | 总GPU数。 |
| --totalGpuMem | Float | 0 | 总GPU显存数。 |

**示例**

请求示例智能体工厂 OpenTrek

```
&notebookId=nb-8c16aa9502e12042930bc750e7ec****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "sshPublicKey":"",
  "notebookStatus":"",
  "storageMountList":[
   {
    "mountPath":"",
    "pvcName":"",
    "storagePath":"",
    "storageSource":""
   }
```

`],`

```json
  "gmtCreated":"",
  "sshStatus":"",
  "failedMsg":"",
  "modelMountList":[
   {
    "modelName":"",
    "dataAccInstance":"",
    "weightType":"",
    "mountPath":"",
    "modelId":"",
    "pvcName":"",
    "modelVersion":"",
    "modelType":""
   }
```

`],`

```json
  "thirdpartyStorageMountList":[
   {
    "mountPath":"",
    "storageSubPath":"",
    "occupantId":"",
    "storageId":""
   }
```

`],`

```json
  "sshClassicNetworkAccessIp":"",
  "sharedMemCount":"",
  "sshClassicNetworkAccessStatus":"",
  "vscodeEndpoint":"",
  "imageType":"",
  "gpuCount":"",
  "cpuCount":"",
  "memCount":"",
  "imageId":"",
  "imageName":"",
  "nodeConfigList":[
```

智能体工厂 OpenTrek

```json
   {
    "memCount":"",
    "sharedMemCount":"",
    "gpuMemCount":"",
    "nodeCount":"",
    "startCommand":"",
    "nodeType":"",
    "gpuCount":"",
    "cpuCount":""
   }
```

`],`

```json
  "instanceCost":{
   "runningPod":"",
   "runningMem":"",
   "runningGpuMem":"",
   "totalCpu":"",
   "totalPod":"",
   "totalMem":"",
   "runningGpu":"",
   "totalGpuMem":"",
   "runningCost":"",
   "runningCpu":"",
   "totalCost":"",
   "totalGpu":""
  },
  "notebookEnvConfig":[
   {
    "code":"",
    "value":""
   }
```

`],`

```json
  "quotaId":"",
  "startCommand":"",
  "gpuLabelCount":"",
  "tensorboard":"",
  "notebookDesc":"",
  "autoShutdownStatus":"",
  "notebookName":"",
  "gmtModified":"",
  "quotaName":"",
  "aliyunUid":"",
  "accessType":"",
  "imageExportList":[
   {
    "imageVersion":"",
    "frameWork":"",
    "gmtModified":"",
    "imageId":"",
    "imageName":"",
    "imageNamespace":"",
    "gmtCreated":"",
    "aliyunUid":"",
    "componentList":"",
    "imageRepo":"",
```

智能体工厂 OpenTrek

```json
    "imageRepoTag":"",
    "imageDesc":"",
    "imageStatus":"",
    "gpuDriver":"",
    "regionId":"",
    "imageAddress":"",
    "gpuManufacturerList":"",
    "imageSize":"",
    "availableService":"",
    "imageAccelerationType":"",
    "exportId":""
   }
```

`],`

```json
  "endpoint":"",
  "gpuType":"",
  "imageVersion":"",
  "gpuMemCount":"",
  "notebookServiceConfigList":[
   {
    "vpcAccessPort":"",
    "classicNetworkAccess":"",
    "vpcAccess":"",
    "vpcAccessIp":"",
    "servicePort":"",
    "serviceName":"",
    "targetPort":"",
    "classicNetworkAccessPort":"",
    "classicNetworkAccessIp":""
   }
```

`],`

```json
  "gpuMemTotal":"",
  "autoShutdownTime":"",
  "sshClassicNetworkAccess":"",
  "notebookAccount":"",
  "jupyterEndpoint":"",
  "regionId":"",
  "notebookId":"",
  "gpuMemTotalUnit":"",
  "datasetMountList":[
   {
    "dataAccInstance":"",
    "datasetVersion":"",
    "mountPath":"",
    "pvcName":"",
    "dataType":"",
    "datasetName":"",
    "datasetId":"",
    "datasetFileName":"",
    "datasetType":""
   }
```

`],`

```json
  "codeMountList":[
   {
    "codeId":"",
```

"

```
tPth"""
```

智能体工厂 OpenTrek

```json
    "mountPath":"",
    "pvcName":"",
    "codeName":"",
    "codeRepoType":""
   }
```

`],`

```json
  "notebookType":"",
  "gpuCountUnit":"",
  "imageAccelerationType":"",
  "sshClassicNetworkAccessPort":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListNotebook

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | Notebook建模列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebook Name | Strin g | Query | 否 | ll | Notebook名称。 |
| notebookI d | Strin g | Query | 否 | nb-6f95****0004eff | Notebook唯一标识ID。 |
| notebookS tatus | Strin g | Query | 否 | 2 | Notebook状态。枚举值： 0 -启动中 (starting)， 1 -运行中 (running)， 2 -已停止 (stopped)， 3 -失败 (failed)， 4 -等待启动 (waiting for starting)， 5 -变配中 (scaling)， 6 -停止中 (stopping)。 0：启动中。 1：运行中。 2：已停止。 3：失败。 |
| quotaId | Strin g | Query | 否 | rq-394c****ed104499 | 配额ID。 |
| quotaNam e | Strin g | Query | 否 | A800高网资源配额 | 配额名称。 |
| imageId | Strin g | Query | 否 | img-7f2c****5040f6 | 镜像ID。 |
| imageNa me | Strin g | Query | 否 | nvidia-pytorch-jupyter | 镜像名称。 |

|  | 1 |
|---|---|
|  | 2 |
|  | 3 |
| 4 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds- c3de****0804b03 | 数据集ID。 |

| 37 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- datasetVersion | String | v1 | 数据集版本。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -- datasetFileNa me | String | data.csv | 数据集文件名。 |
| --pvcName | String | null | PVC名称。 |
| -- dataAccInstan ce | String | da-xxxxxxxxx | 数据加速实例。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |
| --modelId | String | md-gallery- 0a89****0418b | 模型ID。 |
| --modelName | String | qwen-model | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| -- dataAccInstan ce | String | da-xxxxxxxxx | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |

| > 文档版本：20260 | 729 |  | 13 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - codeMountList | Array | [] | 代码库挂载列表。 |
| --codeId | String | cd- 2e0c****0e04d24 | 代码库ID。 |
| --codeName | String | my-code-repo | 代码库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |
| -- storageSource | Integer | 1 | 存储来源。 |
| --storagePath | String | oss://xxxxx.rm.com / | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称。 |
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | 2 | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --cpuCount | Integer | 1 | CPU数量。 |
| --memCount | Integer | 1 | 内存大小（GB）。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| -- gpuMemCount | Integer | -1 | 显存大小（GB）。 |

| 39 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuCount | Integer | 0 | GPU数量。 |
| -- startCommand | String | sleep 100 | 初始化命令。 |
| -gmtCreated | String | 2025-11- 13T08:10:12Z | 创建时间。 |
| -gmtModified | String | 2025-11- 13T08:10:12Z | 修改时间。 |
| -aliyunUid | String | 198226****1225 | 阿里云账号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -failedMsg | String | null | 失败信息。 |
| -notebookId | String | nb-6f95****0004eff | Notebook唯一标识ID。 |
| - notebookNam e | String | ll | Notebook名称。 |
| -notebookDesc | String | xxxxxx | Notebook描述。 |
| -notebookType | Integer | 1 | Notebook类型。枚举值： 1 - JUPYTER， 2 -VSCODE。 |
| - notebookStatu s | Integer | 2 | Notebook状态。枚举值： 0 -启动中 (starting)， 1 -运行中(running)， 2 -已停止(stopped)， 3 -失败(failed)， 4 -等待启动(waiting for starting)， 5 -变配中 (scaling)， 6 -停止中(stopping)。 |
| -imageId | String | img- 7f2c****5040f6 | 镜像ID。 |
| -imageVersion | String | 2.2.0.1-3.2304- cu121 | 镜像版本。 |
| -imageName | String | nvidia-pytorch- jupyter | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型。枚举值： 0 -PUBLIC(公共镜像)， 1 -CUSTOM(自定义镜像)。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - imageAccelera tionType | Integer | 0 | 镜像加速类型。枚举值： 0 -IMAGE(普通镜像)， 1 -ACCELERATED IMAGE(加速镜 _ 像)。 |
| -quotaId | String | rq- 394c****ed104499 | 配额ID。 |
| -quotaName | String | A800高网资源配额 | 配额名称。 |
| -cpuCount | Integer | 1 | CPU数量。 |
| -memCount | Integer | 1 | 内存大小（GB）。 |
| - sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| - gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| -gpuCount | Integer | 0 | GPU数量。 |
| - gpuLabelCoun t | Integer | 0 | GPU虚拟化卡数量。 |
| -gpuMemTotal | Integer | 0 | 显存总量（GB）。 |
| -gpuCountUnit | Integer | null | GPU数量单位。 |
| - gpuMemTotal Unit | Integer | null | 显存总量单位。 |
| - notebookAcco unt | String | admin | Notebook登录账户。 |
| -tensorboard | Boolean | false | 是否开启TensorBoard。 |
| -endpoint | String | https://10.*****.10 0/nb- 93a*****e804f43/ju pyter/ | Notebook访问Endpoint。 |
| - vscodeEndpoi nt | String | https://10.*****.10 0/nb- 93a*****e804f43/c odeserver/ | VSCode访问Endpoint。 |

| 41 |  |  | > 文档版本：2026072 |
|---|---|---|---|

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 |  | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|
| - jupyterEndpoi nt | String |  | https://10.*****.10 0/nb- 93a*****e804f43/ju pyter/ | Jupyter访问Endpoint。 |  |  |
| -accessType | Boolean |  | true | 访问类型。 |  |  |
| -sshStatus | Boolean |  | true | SSH是否启用。 |  |  |
| -gpuType | Integer |  |  | GPU类型。枚举值： NO LIMIT -不限制。 _ NVIDIA Ampere A100 80G NVLink - _ _ _ _ A100 80G。 NVIDIA Ampere A800 80G NVLink - _ _ _ _ A800 80G。 Hygon Kongming DCUK100 AI PCIE 64 _ _ _ _ _ G -海光DCU K100 64G。 HUAWEI DaVinci Ascend910B1 -***昇 _ _ 腾910B1。 Baidu kunlun P800 OAM 96G -***昆 _ _ _ _ 仑P800 96G。 PG1 A910E -PPU A910E。 _ OTHER -其他。 |  |  |
|  |  |  |  |  | Hygon Kongming DCUK100 AI PCIE 64 _ _ _ _ _ |  |
|  |  | ger | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ |  |  |  |
| - autoShutdown Status | Boolean |  | false | 是否启用定时关机。 |  |  |
| - autoShutdown Time | String |  | 2026-03- 05T10:00:00Z | 定时关机时间。 |  |  |
| - startCommand | String |  | sleep 100 | 初始化命令。 |  |  |
| -instanceCost | Struct |  | {} | 实例费用信息。 |  |  |
| --runningCost | Float |  | 0.00 | 运行中费用。 |  |  |
| --runningPod | Float |  | 0 | 运行中Pod数。 |  |  |
| --runningCpu | Float |  | 0 | 运行中CPU数。 |  |  |

| > 文档版本：20260 | 729 |  | 14 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --runningMem | Float | 0 | 运行中内存数。 |
| --runningGpu | Float | 0 | 运行中GPU数。 |
| -- runningGpuMe m | Float | 0 | 运行中GPU显存数。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 0 | 总Pod数。 |
| --totalCpu | Float | 0 | 总CPU数。 |
| --totalMem | Float | 0 | 总内存数。 |
| --totalGpu | Float | 0 | 总GPU数。 |
| --totalGpuMem | Float | 0 | 总GPU显存数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | notebook建模的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | notebook建模的页码。 |

**示例**

请求示例智能体工厂 OpenTrek &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "gmtModified":"",
   "notebookStatus":"",
   "quotaName":"",
   "storageMountList":[
    {
     "mountPath":"",
     "pvcName":"",
     "storagePath":"",
     "storageSource":""
    }
```

`],`

```json
   "gmtCreated":"",
   "aliyunUid":"",
   "sshStatus":"",
   "failedMsg":"",
   "modelMountList":[
    {
     "modelName":"",
     "dataAccInstance":"",
     "weightType":"",
     "mountPath":"",
     "modelId":"",
     "pvcName":"",
     "modelVersion":"",
     "modelType":""
    }
```

`],`

```json
   "accessType":"",
   "endpoint":"",
   "sharedMemCount":"",
   "vscodeEndpoint":"",
   "imageType":"",
   "gpuCount":"",
   "cpuCount":"",
   "gpuType":"",
   "imageVersion":"",
   "memCount":"",
   "imageId":"",
   "imageName":"",
   "nodeConfigList":[
    {
     "memCount":"",
     "sharedMemCount":"",
     "gpuMemCount":"",
```

智能体工厂 OpenTrek

```json
     "nodeCount":"",
     "startCommand":"",
     "nodeType":"",
     "gpuCount":"",
     "cpuCount":""
    }
```

`],`

```json
   "gpuMemCount":"",
   "instanceCost":[
    {
     "runningPod":"",
     "runningMem":"",
     "runningGpuMem":"",
     "totalCpu":"",
     "totalPod":"",
     "totalMem":"",
     "runningGpu":"",
     "totalGpuMem":"",
     "runningCost":"",
     "runningCpu":"",
     "totalCost":"",
     "totalGpu":""
    }
```

`],`

```json
   "quotaId":"",
   "gpuMemTotal":"",
   "startCommand":"",
   "autoShutdownTime":"",
   "gpuLabelCount":"",
   "notebookAccount":"",
   "tensorboard":"",
   "jupyterEndpoint":"",
   "regionId":"",
   "notebookId":"",
   "gpuMemTotalUnit":"",
   "datasetMountList":[
    {
     "dataAccInstance":"",
     "datasetVersion":"",
     "mountPath":"",
     "pvcName":"",
     "dataType":"",
     "datasetName":"",
     "datasetId":"",
     "datasetFileName":"",
     "datasetType":""
    }
```

`],`

```json
   "notebookDesc":"",
   "autoShutdownStatus":"",
   "codeMountList":[
    {
     "codeId":"",
     "mountPath":"",
```

智能体工厂 OpenTrek

```json
     "pvcName":"",
     "codeName":"",
     "codeRepoType":""
    }
```

`],`

```json
   "notebookType":"",
   "notebookName":"",
   "gpuCountUnit":"",
   "imageAccelerationType":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ModifyNotebook

调用ModifyNotebook修改指定notebook建模的部分信息，包括notebook名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 05fec54408c6d0460c08 9de038cs2j3**** | notebook建模ID，该参数必填。 |
| notebook Name | Strin g | Body | 是 | notebook-name | notebook建模名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| notebook Desc | Strin g | Body | 否 | notebook-desc | notebook建模描述，描述长度为2~256个字符，不能以http://和https:// 开头。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/modify HTTP/1.1 { "notebookId":" nb-05fec54408c6d0460c089de038cs2j3****", "notebookName":"notebook-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyNotebookSpec

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-spec HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 05fec54408c6d0460c08 9de038cc**** | notebook建模ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| sharedMe mCount | Integ er | Body | 否 | 1 | 共享内存大小，单位为GB。 |
| gpuCount | Integ er | Body | 是 | 1 | gpu大小，单位为卡，值为- 1时代表gpu根据 gpuMemCount参数进行虚拟化分配，该参数必填。 |
| gpuMemC ount | Integ er | Body | 否 | 1280 | gpu显存份数，值为-1时代表gpu根据gpuCount参数进行整卡分配。该参数与 gpuLabelCount参数有关联，计算式为 gpuMemCount = (gpuLabelCount * maxSpace) / idealResourceStep，其中 maxSpace为单张gpu卡的显存，idealResourceStep 为资源切分的粒度，目前默认按照128Mi一份进行切分。 |
| gpuLabelC ount | Integ er | Body | 否 | 2 | gpu虚拟化卡数量，值为-1 时代表gpu根据gpuCount 参数进行按卡分配。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/modify-spec HTTP/1.1 { "notebookId":" nb-05fec54408c6d0460c089de038cc****", "cpuCount":"1", "memCount":"1", "gpuCount":"1" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyNotebookUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-user HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 7ea900eb04207041a50 90d10b7***** | notebook建模ID，该参数必填。 |
| notebook Account | Strin g | Body | 是 | ad**** | notebook建模账号，该参数必填。 |
| oldPasswo rd | Strin g | Body | 是 | ******* | notebook建模旧密码，该参数必填。 |
| notebookP assword | Strin g | Body | 是 | ******* | notebook建模新密码，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/modify-user HTTP/1.1 { "notebookId":"nb-7ea900eb04207041a5090d10b7*****", "notebookAccount":"ad****", "oldPassword":"*******", "notebookPassword":"*******" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateNotebookImageExportTask

调用CreateNotebookImageExportTask创建导出notebook镜像任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /notebook/export-image HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb- 8c16aa9502e12042930 bc750e7ec**** | notebook建模ID，该参数必填。 |
| imageId | Strin g | Body | 否 | img- 66562b610952c0441e0 ba6a***** | 镜像ID。 |
| imageNa me | Strin g | Body | 是 | image-name | 镜像名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| imageDes c | Strin g | Body | 否 | image-desc | 镜像描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| imageNa mespace | Strin g | Body | 是 | test | ACR镜像命名空间，该参数必填。 |
| imageRep o | Strin g | Body | 是 | test | 镜像仓库，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageRep oTag | Strin g | Body | 是 | v1 | 镜像仓库Tag，该参数必填。 |
| availableS ervice | Integ er | Body | 否 | 1 | 可用服务，取值范围： 1：任务建模。 2：notebook建模。 3：任务建模和 notebook建模。 4：在线服务。 5：任务建模和在线服务。 6：notebook建模和在线服务。 7：任务建模、 notebook建模和在线服务。 该参数为位运算，可以支持单选，多选。 例如多选任务建模和notebook建模时， 该值为3。 |
| frameWor k | Integ er | Body | 否 | 1 | 框架类型，取值范围： 1：Tensorflow。 2：PyTorch。 |
| clusterTyp e | Integ er | Body | 否 | 0 | 集群算力类型，取值范围： 0：裸金属。 1：EGS。 2：不限。 |
| imageAcc elerationT ype | Integ er | Body | 否 | 0 | 镜像加速类型，取值范围： 0：容器镜像。 1：加速镜像。 |
| imageStat us | Integ er | Body | 否 | 1 | 镜像状态，取值范围： 0：转换中。 1：正常。 2：转换失败。 3：未知状态。 4：等待中。 |
| gpuDriver | Strin g | Body | 否 | CUDA v1 _ | AI计算工具包。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gpuManuf acturerLis t | Json | Body | 否 | ["NVIDIA", "AMD"] | 芯片厂商。 |
| imageSize | Strin g | Body | 否 | 30 | 镜像大小。 |
| componen tList | Json | Body | 否 | ["PyTorch:2.3.1"] | 组件信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "exportId": "ei- *****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /notebook/export-image HTTP/1.1 { "notebookId":"nb-8c16aa9502e12042930bc750e7ec****", "imageName":"image-name", "imageVersion":"v1", "imageNamespace":"test", "imageRepo":"test", "imageRepoTag":"v1" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{      \"exportId\": \"ei-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyNotebookAutoShutdown

调用ModifyNotebookAutoShutdown修改Notebook实例自动停止。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-auto-shutdown HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb-596e****** | notebook建模实例ID，该参数必填。 |
| autoShutd ownStatus | Boole an | Body | 否 | true | 是否启用自动停止。 |
| autoShutd ownTime | Strin g | Body | 否 | 2025-09- 29T16:00:00.000Z | 自动停止时间，使用 ISO 8601 日期时间格式。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/modify-auto-shutdown HTTP/1.1 { "notebookId":"nb-596e******" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyNotebookServiceConfig

调用ModifyNotebookServiceConfig修改Notebook自定义服务配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/modify-service-config HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb-8c16aa97ec**** | Notebook建模ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookS erviceCon fig | Json | Body | 否 | [ { "serviceName": "service-demo1", "targetPort": 9000, "vpcAccess": true, "classicNetworkAccess": false, "servicePort": 9003 }, { "serviceName": "service- demo2", "targetPort": 9000, "vpcAccess": false, "classicNetworkAccess": true, "servicePort": 9005 } ] | 自定义服务的名称、监听端口、访问端口、网络访问类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/modify-service-config HTTP/1.1 { "notebookId":"nb-8c16aa97ec****" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ResetNotebookUserPassword

调用ResetNotebookUserPassword重置Notebook用户密码。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /notebook/reset-user-password HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| notebookI d | Strin g | Body | 是 | nb-8c16750e7ec**** | notebook建模ID，该参数必填。 |
| notebook Account | Strin g | Body | 是 | ad**** | notebook建模账号，该参数必填。 |
| notebookP assword | Strin g | Body | 是 | note***** | notebook建模新密码，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /notebook/reset-user-password HTTP/1.1 { "notebookId":"nb-8c16750e7ec****", "notebookAccount":"ad****", "notebookPassword":"note*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 任务建模

#### ModifyTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /task/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Body | 是 | tk- be1b6a1201b4004c5c0b be10c855**** | 任务ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | Strin g | Body | 是 | task-name | 任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| taskDesc | Strin g | Body | 否 | task-desc | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| startTime | Strin g | Body | 否 | 2026-05-26 18:00:00 | 开始时间。 |
| stopTime | Strin g | Body | 否 | 2026-05-27 18:00:00 | 结束时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /task/modify HTTP/1.1 { "taskId":"tk-be1b6a1201b4004c5c0bbe10c855****", "taskName":"task-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyTaskStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /task/modify-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Body | 是 | tk- 3fa6425c0534704b3609 bd80e4c9**** | 任务ID，该参数必填。 |
| taskStatus | Boole an | Body | 是 | true | 任务状态，该参数必填，取值范围： true：重启。 false：停止。 |
| restartTyp e | Strin g | Body | 否 | direct | 重启类型，若taskStatus值为true时，该参数不能为空，取值范围： direct：直接重启。 ckpt：从ckpt重启。 默认值：direct。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ckptId | Strin g | Body | 否 | ckpt-f8d48a42-3dc7- 4c57-80b6-fa74**** | 检查点ID，若taskStatus值为true时，该参数不能为空。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| startTime | Strin g | Body | 否 | 2026-05-26 18:00:00 | 开始时间。 |
| stopTime | Strin g | Body | 否 | 2026-05-27 18:00:00 | 结束时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /task/modify-status HTTP/1.1 { "taskId":"tk-3fa6425c0534704b3609bd80e4c9****", "taskStatus":"true" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

|  | { "success":true, "dynamicMessages":"-", "errorMessage":"", "errorCode":"500", "httpCode":200 } |  |
|---|---|---|

#### CreateTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /task/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | Strin g | Body | 是 | task-name | 任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| taskDesc | Strin g | Body | 否 | task-desc | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| imageId | Strin g | Body | 否 | img- cf3b10300ca7c0423b08 a3e02c547**** | 镜像ID，创建方式为自定义配置时，该参数不能为空。 |
| imageVer sion | Strin g | Body | 否 | v1 | 镜像版本，创建方式为自定义配置时，该参数不能为空。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| taskType | Integ er | Body | 是 | 0 | 任务类型，该参数必填，取值范围： 0：任务建模。 1：模型评测。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceTyp e | Integ er | Body | 否 | 0 | 创建方式，取值范围： 0：自定义配置。 1：套件配置。 |
| componen tId | Strin g | Body | 否 | cp-50dad2a5019c00**** | 训推套件ID，创建方式为套件配置时，该参数不能为空。 |
| componen tParams | Json | Body | 否 | [ { "code": "gradient accumulation _ _ steps", "defaultValue": "16", "name": "梯度累计步数", "type": "INT" } ] | 训推套件参数。 |
| componen tInputs | Json | Body | 否 | [ { "datasetId": "ds- 3fe17306002190****", "datasetVersion": "v1", "sourceType": "dataset", "code": "dataset", "dataAccInstance": "" }, { "modelId": "md- 24f43161077960****", "modelVersion": "v1", "modelType": 1, "sourceType": "model", "code": "model" } ] | 训推套件输入。 |
| componen tOutputs | Json | Body | 否 | [ { "sourceType": "oss", "storagePath": "oss://xxxxx.oss-cn- xxxxx.com/deepspeed- trl-task/code/" } ] | 训推套件输出。 |
| frameWor k | Integ er | Body | 是 | 1 | 模型框架，该参数必填，取值范围： 1：Tensorflow。 2：PyTorch。 10：DeepSpeed。 11：Megatron。 12：PaddlePaddle。 13：MindSpore。 |
| trainType | Integ er | Body | 否 | 0 | 训练类型，取值范围： 0：单机训练。 1：分布式训练。 默认值：0。 |
| startCom mand | Strin g | Body | 否 | python3 main.py | 启动命令，创建方式为套件配置时，该参数不能为空。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| rdmaEnab le | Boole an | Body | 否 | true | 是否启用高网，取值范围： true：启用。 false：禁用。 |
| autoDiagn osis | Boole an | Body | 否 | true | 是否启用自动诊断，取值范围： true：启用。 false：禁用。 |
| datasetMo untList | Json | Body | 否 | [{ "mountPath": "/root/", "datasetId": "ds- 53db9f1d7e6c466b89ce 12e7****", "datasetType": 0, "dataSource": 1, "quotaId": "rq- d8890a98089c2041d80 86bb0b2e2****", "dataAccInstance":"da- 8x9778f7s9fsfhsr8****" }] | 数据集配置。 |
| modelMou ntList | Json | Body | 否 | [{ "modelId": "md- 2af563bb00a40042c709 5d00f6a1*****", "modelVersion": "ten", "modelType": 1, "dataAccInstance": null, "mountPath": "/data" }] | 模型仓库配置。 |
| codeMoun tList | Json | Body | 否 | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046ec0bc ad0d3682****" }] | 代码集配置。 |
| storageMo untList | Json | Body | 否 | [{ "mountPath": "/root/", "storagePath": "oss://****/****", "storageSource": 1, "quotaId": "rq- d8890a98089c2041d80 86bb0b2e2****" }] | 持久化存储设置。 |
| nodeConfi gList | Json | Body | 是 | [{ "memCount": 1, "nodeCount": 1, "nodeType": 2, "gpuCount": 0, "cpuCount": 1 }] | 任务资源配置，该参数必填。 |
| thirdparty StorageLis t | Json | Body | 否 | [ { "storageId":"******", "storageSubPath":"/aistu dio/third/***", "mountPath":"/kea/traini ng/****" } ] | 第三方存储列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| elasticCon fig | Json | Body | 否 | { "enableFaultTolerant": true, "faultStrategy": "OnFailure", "maxRestarts": "3", "enableElastic": true, "minWorkers": 1, "maxWorkers": 1, "enableCkpt": false, "enableHealthCheck": true, "elasticFramework": "kea", "restartType": "direct" } | 弹性容错配置信息。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| startTime | Strin g | Body | 否 | 2024-08-02 18:09:14 | 开始时间。 |
| stopTime | Strin g | Body | 否 | 2026-05-26 17:00:00 | 结束时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "taskId": "tk-****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /task/create HTTP/1.1 { "taskName":"task-name", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "taskType":"0", "frameWork":"1", "nodeConfigList":"[{
 "memCount": 1,
 "nodeCount": 1,
 "nodeType": 2,
 "gpuCount": 0,
 "cpuCount": 1
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"taskId\": \"tk-****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | tk- 522aaaab085c004d600 85360b1c2fs9**** | 任务ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&taskId=tk-522aaaab085c004d60085360b1c2fs9****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | tk- 522aaaab085c004d600 85360b1c2fs9**** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - codeMountList | Array | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" }] | 代码集配置。 |
| --codeId | String | "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" | 唯一标识代码的编号，用于系统内区分不同代码段或配置项。 |
| --codeName | String | name | 代码集名称。 |
| -- codeRepoType | Integer | 1 | 代码仓库类型。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| - datasetMountL ist | Array | [{ "datasetId": "ds- 5740734ff2cf4a00 bc6da*****", "mountPath": "/data" }] | 数据集配置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --dataType | Integer | 0 | 数据类型。 |
| --datasetId | String | "ds- 5740734ff2cf4a00 bc6da*****" | 数据集ID。 |
| --datasetName | String | name | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| - modelMountLi st | Array | [{ "modelId": "md- 7a5c75e10a95104 e1d0bd5804e0c34 6c****", "mountPath": "/root", "modelType": 1, "modelVersion": "v1", "dataAccInstance": "da- df89s8f9sdfs99sae *****" }] | 模型库配置。 |
| --modelId | String | “md- rbvg5wzljz****ks92 ” | 模型ID。 |
| --modelName | String | name | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --mountPath | String | /tmp | 容器挂载路径。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - nodeConfigList | Array | [{ "memCount": 0, "nodeCount": 1, " id": _ "wUSP459HLrZZrD WsARAI", "gpuCount": 0, "cpuCount": 1, "quotaCount": { "task": 0, "cpu": 0, "cpuMax": 0, "mem": 0, "memMax": 0, "gpu": 0, "gpuMax": 0 } }] | 节点配置。 |
| --cpuCount | Integer | 16 | CPU总核数。 |
| --gpuCount | Integer | 1 | GPU核数。 |
| -- gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| --memCount | Integer | 1 | 内存大小，单位为GB。 |
| --nodeCount | Integer | 2 | 节点个数。 |
| --nodeType | Integer | 0 | 节点类型。 |
| -- sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| - storageMountL ist | Array | [{ "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| --storagePath | String | oss://****.oss- ****/****/ | 存储路径。 |
| -- storageSource | Integer | 1 | 存储类型，取值范围： 0：LOCAL。 1：OSS。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -autoDiagnosis | Boolean | true | 任务自动诊断功能配置。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| - elasticFramew ork | String | kea | Kea弹性框架。 |
| -frameWork | Integer | 1 | 框架类型。 |
| -gmtCreated | String | "2026-03- 04T07:55:56Z" | 资源创建时间。 |
| -gmtEnd | String | "2026-03- 04T07:55:56Z" | 结束时间。 |
| -gmtModified | String | "2026-03- 04T07:55:56Z" | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指单个GPU 设备。 |
| - gpuLabelCoun t | Integer | 1 | GPU虚拟化指示。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| -gpuMemTotal | Integer | 16384 | 显存总数。 |
| - gpuMemTotal Unit | Integer | 1 | 表示GPU总显存容量的单位。 |
| -gpuType | Integer | 1 | GPU显卡类型。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型，取值范围： 0：容器镜像。 1：加速镜像。 默认值：0。 |
| -imageId | String | img- 05cefd0be2exxxx | 镜像ID。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - imageIdAndVe rsion | String | imgv- 5cefd0be2exxx | 镜像ID版本。 |
| -imageName | String | testImageName | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型。 |
| -imageVersion | String | V3.5 | 镜像版本。 |
| -isSchedule | Boolean | false | 是否启用定时任务。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | name | 配额名称。 |
| -rdmaEnable | Boolean | true | 是否启用RDMA高网。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| -sourceType | Integer | 1 | 源数据的类型。 |
| - startCommand | String | python3 main.py | 启动命令。 |
| -taskId | String | tk-000000000001 | 任务ID。 |
| -taskName | String | name | 任务名称。 |
| -taskStatus | Integer | 0 | 任务状态。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskType | Integer | 0 | 任务类型。 |
| -tensorboard | Boolean | false | 用于指定TensorBoard读取事件文件（如训练指标、模型图等）的目录路径。 |
| -trainType | Integer | 0 | 训练类型，取值范围： 0：单机训练。 1：分布式训练。 默认值：0。 |
| -elasticConfig | Struct | { "enableFaultTolera nt": true, "faultStrategy": "OnFailure", "maxRestarts": "3", "enableElastic": true, "minWorkers": 1, "maxWorkers": 1, "enableCkpt": false, "enableHealthChec k": true, "elasticFramework" : "kea", "restartType": "direct" } | 弹性容错配置信息。 |
| -- ckptMountPath | String | /mnt/checkpoints | 指定模型检查点文件在容器内的挂载路径，用于加载或保存训练过程中的权重和优化器状态。 |
| -- elasticFramew ork | String | kea | 框架弹性。 |
| --enableCkpt | Boolean | true | 启用检查点机制，用于在任务失败时从最近的检查点恢复执行，保障数据处理的一致性和容错性。 |
| --enableElastic | Boolean | true | 启用弹性。 |
| -- enableFaultTol erant | Boolean | true | 启用容错机制，允许系统在部分组件失败时继续运行并自动恢复 |
| -- enableHealthC heck | Boolean | true | 启用健康检查功能，用于定期检测服务实例的运行状态以确保高可用性。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --faultStrategy | String | OnFailure | 容错策略。 |
| --maxRestarts | Integer | 3 | 表示任务或进程在失败后最多允许自动重启的次数，超过该次数后将不再尝试重启并标记为最终失败。 |
| --minWorkers | Integer | 2 | 指定集群或工作负载中最小可维持的工作者节点数量，用于保障服务基本可用性和弹性伸缩下限。 |
| --restartType | String | direct | 类型重启。 |
| --storagePath | String | oss://****.oss- ****/****/ | 存储路径。 |
| --storageType | Integer | 0 | 存储类型。 |
| -instanceCost | Struct | {} | 表示单个实例在指定时间段内产生的费用金额， 单位为货币（如美元），通常包含计算资源、存储及网络等成本。 |
| --runningCost | Float | 500 | 每小时运行消耗。 |
| --runningCpu | Integer | 0 | 当前系统中正在运行或等待CPU调度的进程所占用的CPU。 |
| --runningGpu | Integer | 2 | GPU使用情况。 |
| -- runningGpuMe m | Integer | 1256 | 当前GPU正在使用的显存大小，单位为字节（例如12MB）。 |
| --runningMem | Integer | 128 | 表示当前系统中正在运行的进程所占用的物理内存大小。 |
| --runningPod | Integer | 1 | 运行中Pod数。 |
| --totalCost | Float | 150.75 | 任务总消耗。 |
| --totalCpu | Float | 10 | 配额总数（CPU）。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --totalGpu | Integer | 10 | 配额总数（GPU）。 |
| --totalGpuMem | Integer | 10 | 显存使用总量。 |
| --totalMem | Integer | 10 | 内存使用总量。 |
| --totalPod | Integer | 3 | 集群中当前运行的Pod总数。 |
| -taskConfig | Struct | {} | 高级配置。 |
| --envs | List | [{"name":"x","valu e":"y"}, {"name":"x2","valu e":"y2"}] | 环境变量配置。 |

**示例**

请求示例

```
&taskId=tk-522aaaab085c004d60085360b1c2fs9****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "gmtModified":"\"2026-03-04T07:55:56Z\"",
  "quotaName":"name",
  "storageMountList":[
   {
    "mountPath":"/tmp",
    "storagePath":"oss://****.oss-****/****/",
    "storageSource":1
   }
```

`],`

```json
  "aliyunUid":"157123456789****",
  "gmtCreated":"\"2026-03-04T07:55:56Z\"",
  "trainType":0,
  "modelMountList":[
   {
    "modelName":"name",
    "mountPath":"/tmp",
    "modelId":"“md-rbvg5wzljz****ks92”",
    "modelVersion":"v1",
    "modelType":0
   }
```

智能体工厂 OpenTrek `],`

```json
  "taskType":0,
  "sharedMemCount":4,
  "gmtEnd":"\"2026-03-04T07:55:56Z\"",
  "nodeCount":2,
  "autoDiagnosis":true,
  "elasticFramework":"kea",
  "gpuCount":1,
  "imageType":0,
  "cpuCount":16,
  "taskStatus":0,
  "gpuType":1,
  "imageVersion":"V3.5",
  "memCount":1,
  "frameWork":1,
  "imageId":"img-05cefd0be2exxxx",
  "imageName":"testImageName",
  "nodeConfigList":[
   {
    "memCount":1,
    "sharedMemCount":4,
    "gpuMemCount":0,
    "nodeCount":2,
    "nodeType":0,
    "gpuCount":1,
    "cpuCount":16
   }
```

`],`

```json
  "gpuMemCount":0,
  "instanceCost":{
   "runningGpuMem":1256,
   "runningMem":128,
   "runningPod":1,
   "totalCpu":10.0,
   "totalMem":10,
   "totalPod":3,
   "runningGpu":2,
   "totalGpuMem":10,
   "runningCost":500.0,
   "runningCpu":0,
   "totalCost":150.75,
   "totalGpu":10
  },
  "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****",
  "gpuMemTotal":16384,
  "startCommand":"python3 main.py",
  "gpuLabelCount":1,
  "rdmaEnable":true,
  "imageIdAndVersion":"imgv-5cefd0be2exxx",
  "tensorboard":false,
  "gpuMemTotalUnit":1,
  "regionId":"cn-hangzhou",
  "sourceType":1,
  "datasetMountList":[
{
```

智能体工厂 OpenTrek

```json
   {
    "datasetVersion":"v1",
    "mountPath":"/tmp",
    "dataType":0,
    "datasetName":"name",
    "datasetId":"\"ds-5740734ff2cf4a00bc6da*****\"",
    "datasetType":0
   }
```

`],`

```json
  "codeMountList":[
   {
    "codeId":"\"cd-f1bb797e0cef2046ec0bcad0d3682****\"",
    "mountPath":"/tmp",
    "codeName":"name",
    "codeRepoType":1
   }
```

`],`

```json
  "gpuCountUnit":1,
  "taskName":"name",
  "elasticConfig":{
   "enableFaultTolerant":true,
   "maxRestarts":3,
   "faultStrategy":"OnFailure",
   "enableElastic":true,
   "enableHealthCheck":true,
   "storageType":0,
   "storagePath":"oss://****.oss-****/****/",
   "minWorkers":2,
   "elasticFramework":"kea",
   "ckptMountPath":"/mnt/checkpoints",
   "restartType":"direct",
   "enableCkpt":true
  },
  "taskConfig":{
   "envs":"[{\"name\":\"x\",\"value\":\"y\"},{\"name\":\"x2\",\"value\":\"y2\"}]"
  },
  "imageAccelerationType":0,
  "taskId":"tk-000000000001",
  "isSchedule":false
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | tk- c2dd02940f8b604ad308 be708be8**** | 任务ID。 |
| taskName | Strin g | Query | 否 | task-name | 任务名称。 |
| taskStatus | Integ er | Query | 否 | 0 | 任务状态，取值范围： 0：已创建。 1：启动中。 2：运行中。 3：已停止。 4：失败。 5：完成。 |
| frameWor k | Integ er | Query | 否 | 1 | 模型框架，取值范围： 1：Tensorflow。 2：PyTorch。 10：DeepSpeed。 11：Megatron。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| quotaNam e | Strin g | Query | 否 | quota-name | 资源配额名称。 |
| imageId | Strin g | Query | 否 | img- 359cc14b09a50049800b bd4sada8**** | 镜像ID。 |
| imageNa me | Strin g | Query | 否 | image-name | 镜像名称。 |
| modelId | Strin g | Query | 否 | md- 7a5c75e10a95104e1d0 bd5804e0c346c**** | 模型仓库ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型仓库名称。 |
| datasetId | Strin g | Query | 否 | ds- d8890a98089c2041d80 86bb0b2e27**** | 数据集ID。 |
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - codeMountList | Array | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" }] | 代码集配置列表。 |
| --codeId | String | "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" | 唯一标识代码的编号，用于系统内区分不同代码实体。 |
| --codeName | String | name | 代码名称。 |
| -- codeRepoType | Integer | 1 | 代码仓库类型。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --mountPath | String | /tmp | 容器挂载路径。 |
| - datasetMountL ist | Array | [{ "datasetId": "ds- 5740734ff2cf4a00 bc6da*****", "mountPath": "/data" }] | 数据集配置。 |
| --dataType | Integer | 0 | 数据类型。 |
| --datasetId | String | "ds- 5740734ff2cf4a00 bc6da*****" | 数据集ID。 |
| --datasetName | String | name | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| - modelMountLi st | Array | [{ "modelId": "md- 7a5c75e10a95104 e1d0bd5804e0c34 6c****", "mountPath": "/root", "modelType": 1, "modelVersion": "v1", "dataAccInstance": "da- df89s8f9sdfs99sae *****" }] | 模型库配置。 |
| --modelId | String | “md- rbvg5wzljz****ks92 ” | 模型ID。 |
| --modelName | String | name | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --mountPath | String | /tmp | 容器挂载路径。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - nodeConfigList | Array | [{ "memCount": 0, "nodeCount": 1, " id": _ "wUSP459HLrZZrD WsARAI", "gpuCount": 0, "cpuCount": 1, "quotaCount": { "task": 0, "cpu": 0, "cpuMax": 0, "mem": 0, "memMax": 0, "gpu": 0, "gpuMax": 0 } }] | 节点配置。 |
| --cpuCount | Integer | 16 | CPU总核数。 |
| --gpuCount | Integer | 1 | GPU核数。 |
| -- gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| --memCount | Integer | 1 | 内存大小，单位为GB。 |
| --nodeCount | Integer | 2 | 节点个数。 |
| --nodeType | Integer | 0 | 节点类型。 |
| -- sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| - storageMountL ist | Array | [{ "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| --storagePath | String | oss://****/**** | 存储路径。 |
| -- storageSource | Integer | 1 | 存储类型，取值范围： 0：LOCAL。 1：OSS。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -autoDiagnosis | Boolean | true | 网格自动诊断功能配置。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| - elasticFramew ork | String | kea | Kea弹性框架。 |
| -frameWork | Integer | 1 | 框架类型，取值范围： 1：Tensorflow。 2：PyTorch。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源创建时间。 |
| -gmtEnd | String | 2017-11- 27T06:51:26Z | 结束时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指1块物理 GPU或1个GPU实例。 |
| - gpuLabelCoun t | Integer | 1 | GPU虚拟化指示。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| -gpuMemTotal | Integer | 16384 | 显存总数。 |
| - gpuMemTotal Unit | Integer | 1 | 表示GPU显存总容量的单位。 |
| -gpuType | Integer | 1 | GPU显卡类型。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型，取值范围： 0：容器镜像。 1：加速镜像。 默认值：0。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageId | String | img- 05cefd0be2exxxx | 镜像ID。 |
| - imageIdAndVe rsion | String | imgv- 5cefd0be2exxx | 镜像ID版本。 |
| -imageName | String | testImageName | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型。 |
| -imageVersion | String | v1 | 镜像版本。 |
| -isSchedule | Boolean | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | quota-name | 配额名称。 |
| -rdmaEnable | Boolean | true | 是否启用RDMA高网。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| -sourceType | Integer | 1 | 源数据的类型。 |
| - startCommand | String | python3 main.py | 启动命令。 |
| -taskId | String | tk-000000000001 | 任务ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskName | String | name | 任务名称。 |
| -taskStatus | Integer | 0 | 任务状态。 |
| -taskType | Integer | 0 | 任务类型。 |
| -tensorboard | Boolean | false | 是否启用Tensorboard。 |
| -trainType | Integer | 0 | 训练类型，取值范围： 0：单机训练。 1：分布式训练。 默认值：0。 |
| -instanceCost | Struct | {} | 表示单个实例在指定计费周期内的实际费用金额，单位为货币（如美元），含基础资源费、附加服务费及税费等综合成本。 |
| --runningCost | Float | 500 | 运行消耗。 |
| --runningCpu | Integer | 0 | 当前系统中CPU正在执行任务的时间占总时间的百分比，反映CPU的实时负载程度。 |
| --runningGpu | Integer | 2 | GPU使用情况。 |
| -- runningGpuMe m | Integer | 1256 | 当前GPU上正在运行的进程所占用的显存大小 （单位：GB）。 |
| --runningMem | Integer | 128 | 表示当前系统中正在运行的进程所占用的物理内存大小。 |
| --runningPod | Integer | 1 | 运行中Pod数。 |
| --totalCost | Float | 150.75 | 任务总消耗。 |
| --totalCpu | Float | 10 | 配额总数（CPU）。 |
| --totalGpu | Integer | 10 | 配额总数（GPU）。 |
| --totalGpuMem | Integer | 10 | 显存使用总量。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --totalMem | Integer | 10 | 内存使用总量。 |
| --totalPod | Integer | 3 | 运行中Pod总数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 任务的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "gmtModified":"",
   "quotaName":"",
   "storageMountList":[
    {
     "mountPath":"",
     "storagePath":"",
     "storageSource":""
    }
```

`],`

```json
   "aliyunUid":"",
```

智能体工厂 OpenTrek

```json
   "gmtCreated":"",
   "trainType":"",
   "modelMountList":[
    {
     "modelName":"",
     "mountPath":"",
     "modelId":"",
     "modelVersion":"",
     "modelType":""
    }
```

`],`

```json
   "taskType":"",
   "sharedMemCount":"",
   "gmtEnd":"",
   "nodeCount":"",
   "autoDiagnosis":"",
   "elasticFramework":"",
   "gpuCount":"",
   "imageType":"",
   "cpuCount":"",
   "taskStatus":"",
   "gpuType":"",
   "imageVersion":"",
   "memCount":"",
   "frameWork":"",
   "imageId":"",
   "imageName":"",
   "nodeConfigList":[
    {
     "memCount":"",
     "sharedMemCount":"",
     "gpuMemCount":"",
     "nodeCount":"",
     "nodeType":"",
     "gpuCount":"",
     "cpuCount":""
    }
```

`],`

```json
   "gpuMemCount":"",
   "instanceCost":[
    {
     "runningGpuMem":"",
     "runningMem":"",
     "runningPod":"",
     "totalCpu":"",
     "totalMem":"",
     "totalPod":"",
     "runningGpu":"",
     "totalGpuMem":"",
     "runningCost":"",
     "runningCpu":"",
     "totalCost":"",
     "totalGpu":""
    }
```

] 智能体工厂 OpenTrek `],`

```json
   "quotaId":"",
   "gpuMemTotal":"",
   "startCommand":"",
   "gpuLabelCount":"",
   "rdmaEnable":"",
   "imageIdAndVersion":"",
   "tensorboard":"",
   "gpuMemTotalUnit":"",
   "regionId":"",
   "sourceType":"",
   "datasetMountList":[
    {
     "datasetVersion":"",
     "mountPath":"",
     "dataType":"",
     "datasetName":"",
     "datasetId":"",
     "datasetType":""
    }
```

`],`

```json
   "codeMountList":[
    {
     "codeId":"",
     "mountPath":"",
     "codeName":"",
     "codeRepoType":""
    }
```

`],`

```json
   "gpuCountUnit":"",
   "taskName":"",
   "imageAccelerationType":"",
   "taskId":"",
   "isSchedule":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ListCheckpoint

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | tk- 024db1d30738104a3d0 820105f2**** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -checkPointId | String | "ckpt-b3c2ac70- 8d95-4dfa-badf- 71d461xxxx" | 唯一标识某个Checkpoint的编号。 |
| - checkPointNa me | String | 100 | Ccheckpoint名称。 |
| - checkPointPat h | String | output/checkpoint- 100 | Checkpoint挂载路径。 |
| - checkPointSize | String | 83577373133Byte | Checkpoint大小。 |
| - checkPointStor agePath | String | efs-xxxxx | Cpfs文件系统中存储路径。 |
| - checkPointTim e | String | 2026-02-18 03:57:20 | Checkpoint保存时间。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| AI Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&taskId=tk-024db1d30738104a3d0820105f2****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "checkPointStoragePath":"",
   "checkPointId":"",
   "checkPointSize":"",
   "checkPointPath":"",
   "checkPointTime":"",
   "checkPointName":""
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### FaultTolerantLogPageList

调用FaultTolerantLogPageLis查询所有的容错记录&事件分页列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 容错列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| taskId | Strin g | Query | 是 | tk- 024db1d30738104a3d0 820105f2**** | 任务ID。 |
| eventType | Strin g | Query | 是 | FaultTolerant | 事件类型。 |
| eventTim e | Strin g | Query | 否 | 2024-11-14 00:00:00 | 事件时间。 |
| eventNam e | Strin g | Query | 否 | test | 事件名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -detailList | Array | [{}] | 明细数组。 |
| --code | String | exit code _ | 错误码。 |
| --label | String | Exit Code | 退出码。 |
| --value | String | 0 | 明细值。 |
| -aistudioRunId | String | feca8d72-3a53- 4ab3-9d25- 0dbd4f43xxxx | AI Studio运行ID。 |
| - aistudioTaskId | String | tk- 1234567890abxxx x | AI Studio任务ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -errorMsg | String | error | 错误信息。 |
| -eventCode | String | MasterStart | 事件码。 |
| -eventName | String | network worker node list | 事件名称。 |
| -eventTime | String | 2026-02- 06T16:34:22.9652 61 | 事件时间。 |
| -eventType | String | Instance Event | 事件类型。 |
| -instanceType | String | master | 实例类型。 |
| -podName | String | elasticjob-tk- 33eae7830ea0xxx x-kea-master-0 | Pod名称。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 容错记录总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 容错记录的页码。 |

**示例**

请求示例

```
&taskId=tk-024db1d30738104a3d0820105f2**** &eventType=FaultTolerant
```

&公共请求参数智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "eventCode":"MasterStart",
   "detailList":[
    {
     "code":"exit_code",
     "label":"Exit Code",
     "value":"0"
    }
```

`],`

```json
   "instanceType":"master",
   "eventTime":"2026-02-06T16:34:22.965261",
   "eventName":"network worker node list",
   "podName":"elasticjob-tk-33eae7830ea0xxxx-kea-master-0",
   "aistudioTaskId":"tk-1234567890abxxxx",
   "eventType":"Instance Event",
   "aistudioRunId":"feca8d72-3a53-4ab3-9d25-0dbd4f43xxxx",
   "errorMsg":"error"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### GetCpfs

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| bmcpClust erId | Strin g | Query | 是 | ack-YoZjG***** | bmcp集群ID。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -mountDir | List | [ "/example/dir" ] | 挂载目录列表。 |
| -mountedFs | String | bmcpfs-****018e | 已挂载的文件系统。 |

**示例**

请求示例

```
&bmcpClusterId=ack-YoZjG*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "mountedFs":"",
  "mountDir":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### 任务诊断

##### GetTaskDiagnosticsDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /diagnose/taskDiagnosticsDetail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobId | Strin g | Path | 是 | d7d***** | JobID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - diagnoseItem Detail | List | ["frr", "teeeee"] | 诊断详情 |
| - constantConfi g | String | {} | 诊断配置 |
| - diagnoseItem Description | String | pod检查 | 诊断项说明 |
| - diagnoseItem Name | String | DEPLOYMENT CHE _ CK ITEM _ | 诊断项 |
| - diagnoseItemS tate | Integer | 0 | 诊断状态 0-正常 1-异常 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - diagnoseItemS uggestions | String | "" | 诊断项建议 |
| - diagnosisStatu s | Integer | 0 | 诊断状态： 0-诊断中 1-诊断完成 2-诊断成功 3-诊断失败 |
| -gmtModified | String | 2026-02- 27T01:53:30Z | 诊断更新时间 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /diagnose/taskDiagnosticsDetail HTTP/1.1 &jobId=d7d*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":" -",
 "success":false,
 "dynamicMessages":" -",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### TaskDiagnose

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceId | Strin g | Path | 是 | bi- 46085f2a0778f0433909 623080d***** | 资源ID。 |
| resourceT ype | Strin g | Path | 是 | NOTE BOOK MODELING _ _ | 任务类型，取值范围： NOTE BOOK MODELI _ _ NG：notebook 建模。 TASK MODELING：任 _ 务建模。 ONLINE SERVICE：在 _ 线服务。 VISUAL MODELING： _ 可视化建模。 MODEL EVALUATION _ ：模型评测。 |
| diagnoseIt em | Strin g | Path | 是 | POD | 诊断类型，取值范围： OPERATOR： OPERATOR类型检测项。 QUEUE：kube-queue 类型检测项。 POD：POD类型检测项。 DEPLOYMENT： DEPLOYMENT类型检测项。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - resourceDetail s | Array | [{}] | 诊断流程结果。 |
| --logMessage | List | {} | 业务日志。 |
| -- codeErrorMsg | String | "" | 代码运行错误信息。 |
| -- constantConfi g | String | "" | 诊断配置。 |
| -- diagnoseItem Des | String | "" | 诊断描述。 |
| -- diagnoseItemS tate | String | "" | 诊断项状态。 |
| - constantConfi g | String | "" | 诊断配置。 |
| -diagnoseTime | String | 1662307202400 | 诊断任务入库的时间戳。单位：毫秒。 |
| -finalDiagnose | String | "" | 诊断流程总结。 |
| - finalDiagnoseS tate | String | "" | 诊断流程结果。 |
| -success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| -taskStatus | String | "" | 任务状态。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |

| OpenTr | ek |  | AI Studio ·API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&resourceId=bi-46085f2a0778f0433909623080d***** &resourceType=NOTE_BOOK_MODELING &diagnoseItem=POD
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "resourceDetails":[
    {
     "diagnoseItemState":"\"\"",
     "constantConfig":"\"\"",
     "logMessage":"{}",
     "diagnoseItemDes":"\"\"",
     "codeErrorMsg":"\"\""
    }
```

`],`

```json
   "constantConfig":"\"\"",
   "success":true,
   "finalDiagnose":"\"\"",
   "finalDiagnoseState":"\"\"",
   "diagnoseTime":"1662307202400",
   "taskStatus":"\"\""
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListTaskDiagnoseConfig

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceId | Strin g | Path | 是 | nb- 1051072203c8404885 | 资源ID，该参数必填。 |
| resourceT ype | Strin g | Path | 是 | NOTE BOOK MODELING _ _ | 任务类型，该参数必填，取值范围： NOTE BOOK MODELI _ _ NG：notebook 建模 TASK MODELING：任 _ 务建模 ONLINE SERVICE：在 _ 线服务 VISUAL MODELING： _ 可视化建模 MODEL EVALUATION _ ：模型评测 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - constantConfi g | String | {} | 诊断配置 |
| -diagnoseItem | String | DEPLOYMENT | 诊断项 |
| - diagnoseItem Name | String | DEPLOYMENT CHE _ CK ITEM _ | 诊断项名称 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&resourceId=nb-1051072203c8404885 &resourceType=NOTE_BOOK_MODELING
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPodDiagnosticsDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /diagnose/podDiagnosticsDetail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobId | Strin g | Path | 是 | d7d***** | 任务ID。 |
| podName | Strin g | Path | 否 | tk-1******** | pod名称。 |
| nodeNam e | Strin g | Path | 否 | i-d***** | 节点名称。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -report | Array | [{}] | 诊断报告信息 |
| --metrics | Array | [{}] | 诊断出的异常监控指标 |
| --- metricClassify | String | MemoryError | 监控项分类 CPUError CPU故障 MemoryError 内存故障 NetworkError 网络故障 StorageError 存储故障 OSError 系统故障 GPUError GPU故障 |
| ---metricDetail | String | de vmstat pgmaj _ _ | 监控项详情 |
| ---metricInfo | String | vmstat pgmajfaul _ _ t increased by | 指标对应的触发信息 |
| ---metricName | String | node vmstat pgm _ _ ajfault | 监控指标名称 |
| --- metricSource | String | node-exporter | 指标来源 node-exporter Node指标 gpu-exporter GPU指标 kube-state-metrics Kubernetes指标 _ cluster 集群指标 |
| --nodeprobes | Array | [{}] | 从bmcp捕获到的NodeProbe诊断自愈信息，包含错误信息和工单链接 |
| ---errorDetail | String | NVRM: Xid (P | 错误详情 |
| ---errorType | String | node cpu core thr _ _ _ ottles total _ | 错误码 |
| ---link | String | http://xxxxx | 工单链接 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---reportTime | String | 2025-11- 27T08:02:02Z | 报告时间 |
| --hostIp | String | 172.114.XX.XX | pod对应的host ip |
| --keaLog | String | "" | kea框架诊断日志 |
| --nodeName | String | i-dddd | 节点名称。 |
| --podName | String | tk-dddx-xxx | pod名称 |
| -errorMsg | String | error | 错误信息 |
| -gmtModified | String | 2018-12- 07T02:24:26.00Z | 更新时间 |
| -reportStatus | Integer | 0 | 诊断状态： 0-诊断中， 1-诊断完成, 2-诊断失败， 3-诊断成功 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /diagnose/podDiagnosticsDetail HTTP/1.1 &jobId=d7d*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"\t-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListDiagnostics

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /diagnose/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Path | 是 | tk-7f******* | 任务ID。 |
| startTime | Strin g | Path | 否 | 2025-12-10T09:58:42Z | 查询起始时间。 |
| endTime | Strin g | Path | 否 | 2025-12-10T09:58:42Z | 查询结束时间。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -ackClusterId | String | cef51d60a6778415 ab3a8026c24***** | ack集群id。 |
| - bmcpClusterId | String | ack-YoZjGQ**** | BMCP集群ID，该参数必填。 |
| - diagnosticTim e | String | 2018-01- 17T12:46:09Z | 诊断时间。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| -jobId | String | 72dcd26b-f12d- 4c27-b3af- 18f6aed5**** | 任务ID。 |
|---|---|---|---|
| - podDiagnosisS tatus | Integer | 0 | pod诊断状态 0-诊断中 1-完成' |
| - taskDiagnosis Status | Integer | 0 | 任务诊断状态 0-诊断中 1-完成' |
| -taskId | String | tk-cddsss******* | 任务ID。 |
| -taskStatus | Integer | 0 | 任务状态 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /diagnose/list HTTP/1.1 &taskId=tk-7f*******
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"\t-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### Tensorboard

##### DeleteTensorboard

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| tensorboa rdId | Strin g | Query | 是 | tb- 8c827f4108be104d9d0a 4dc0f7**** | tensorboardID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&tensorboardId=tb-8c827f4108be104d9d0a4dc0f7****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListTensorboard

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | tensorboard列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | tk- 024db1d30738104a3d0 820105f265**** | 任务ID。 |
| tensorboa rdId | Strin g | Query | 否 | tb- 47e1ac300108a049760 ac7f0062**** | tensorboardID。 |
| tensorboa rdName | Strin g | Query | 否 | tensorboard-name | tensorboard名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -subStatus | Integer | 0 | Tensorboard子状态 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskId | String | tk- 000000000001xxx | 任务ID。 |
| -tensorboardId | String | tb-xxxxxxxx | Tensorboard ID。 |
| - tensorboardNa me | String | tensorboard-name | tensorboard名称。 |
| - tensorboardSt atus | Integer | 0 | tensorboard状态 |
| -totalTime | String | 2340 | 总时长。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | tensorboard的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | tensorboard的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "memCount":"",
   "gmtModified":"",
   "aliyunUid":"",
   "gmtCreated":"",
   "totalTime":"",
   "quotaId":"",
   "tensorboardId":"",
   "tensorboardStatus":"",
   "subStatus":"",
   "regionId":"",
   "tensorboardName":"",
   "cpuCount":"",
   "taskId":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

##### CreateTensorboard

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| tensorboa rdName | Strin g | Body | 是 | tensorboard-name | tensorboard名称，该参数必填。 |
| taskId | Strin g | Body | 是 | tk- 83d54e96082b7043790 ad2705e4**** | 任务ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 2 | 内存大小，单位为GB，该参数必填。 |
| storageMo untList | Json | Body | 是 | [{ "logdirMountPath": "/data", "storagePath": "oss://*****/", "mountType": 0, "fileTotalSize": "2.12 MB" }] | 持久化存储设置，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "tensorboardId": "tb-****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
{ "tensorboardName":"tensorboard-name", "taskId":"tk-83d54e96082b7043790ad2705e4****", "cpuCount":"1", "memCount":"2", "storageMountList":"[{
 "logdirMountPath": "/data",
 "storagePath": "oss://*****/",
 "mountType": 0,
 "fileTotalSize": "2.12 MB"
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\t\"tensorboardId\": \"tb-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteTensorboardConfig

调用DeleteTensorboardConfig删除指定的Tensorboard配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| tensorboa rdId | Strin g | Query | 是 | tb- ae2d52190bf2e04d200b 44b0c**** | tensorboardID。 |
| logdirMou ntPath | Strin g | Query | 是 | /tmp/****/ | logdir挂载路径。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&tensorboardId=tb-ae2d52190bf2e04d200b44b0c**** &logdirMountPath=/tmp/****/
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyTensorboardStatus

调用ModifyTensorboardStatus修改指定Tensorboard的状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| tensorboa rdId | Strin g | Body | 是 | tb- f7eec3e507a0c0420d0a 27802dc***** | tensorboardID，该参数必填。 |
| tensorboa rdStatus | Boole an | Body | 是 | true | tensorboard状态，该参数必填，取值范围： true：启动。 false：停止。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "tensorboardId":"tb-f7eec3e507a0c0420d0a27802dc*****", }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetTensorboard

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| tensorboa rdId | Strin g | Query | 是 | tb- f7eec3e507a0c0420d0a 27802dce***** | tensorboardID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - storageMountL ist | Array | [{ "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| --aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| --gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间 |
| --gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -- logdirMountPa th | String | /tmp/****/ | logdir挂载路径。 |
| --mountType | Integer | 0 | 挂载类型。 |
| --regionId | String | cn-hangzhou | 地域ID。 |
| --storagePath | String | oss://****/**** | 存储路径 |
| -- tensorboardId | String | tb-xxxxxxxx | Tensorboard ID。 |
| -accessType | Boolean | 0 | 接入方式 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -endpoint | String | http://xxx | 访问Endpoint。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -subStatus | Integer | 0 | 任务子状态 |
| -taskId | String | tk- 000000000001xxx | 任务ID。 |
| -tensorboardId | String | tb-xxxxxxxx | Tensorboard ID。 |
| - tensorboardNa me | String | tensorboard-name | tensorboard名称。 |
| - tensorboardSt atus | Integer | 0 | tensorboard状态 |
| -totalTime | String | 2340 | 总时长。 |

**示例**

请求示例

```
&tensorboardId=tb-f7eec3e507a0c0420d0a27802dce*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "memCount":"",
  "gmtModified":"",
  "storageMountList":[
   {
    "gmtModified":"",
    "logdirMountPath":"",
    "aliyunUid":"",
    "gmtCreated":"",
    "regionId":"",
    "storagePath":"",
    "tensorboardId":"",
    "mountType":""
   }
```

`],`

```json
  "aliyunUid":"",
  "gmtCreated":"",
  "totalTime":"",
  "quotaId":"",
  "tensorboardId":"",
  "tensorboardStatus":"",
  "subStatus":"",
  "accessType":"",
  "endpoint":"",
  "regionId":"",
  "tensorboardName":"",
  "cpuCount":"",
  "taskId":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetTensorboardOssFileSize

调用GetTensorboardOssFileSize查询Tensorboard的OSS文件大小。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ossPath | Strin g | Body | 否 | oss://***** | OSS路径。 |
| filePrefix | Strin g | Body | 否 | events | 文件前缀。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -fileTotalNum | Integer | 15 | 表示文件总数为15个 |
| -fileTotalSize | String | 1048576 KB | 文件总大小，单位为KB |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 可视化建模

#### 工作流

##### ModifyPipelineDraft

调用ModifyPipelineDraft修改指定工作流的部分信息，包括工作流名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/draft/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Body | 是 | draft- e48bc4e6020df04a430b d***** | 工作流ID，该参数必填。 |
| draftNam e | Strin g | Body | 是 | draft-name | 工作流名称，长度为2～64 个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短 _ 划线（-），该参数必填。 |
| draftDesc | Strin g | Body | 否 | draft-desc | 工作流描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /pipeline/draft/update HTTP/1.1 { "draftId":" draft-e48bc4e6020df04a430bd*****", "draftName":"draft-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListPipelineDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 否 | draft- e48bc4e6020df04a430b df***** | 工作流ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 工作流列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -componentId | List | ["comp-111", "comp-222"] | 关联的组件ID列表。 |
| -datasetIds | List | ["ds-111", "ds- 222"] | 关联的数据集ID列表。 |
| -modelIds | List | ["md-111", "md- 222"] | 关联的模型ID列表。 |
| -aliyunUid | String | 12345678 | 阿里云用户ID。 |
| -draftId | String | draft-abc123 | 工作流ID。 |
| -draftName | String | test | 工作流名称。 |
| -gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T08:58:00Z | 修改时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gpuType | Integer | 0 | GPU类型枚举。枚举值：0-NO LIMIT、1- _ NVIDIA AMPERE A100 80G NVLINK、2- _ _ _ _ NVIDIA AMPERE A800 80G NVLINK、3- _ _ _ _ HUAWEI DAVINCI ASCEND910B1、4- _ _ HUAWEI DAVINCI ASCEND910B2、5- _ _ HUAWEI DAVINCI ASCEND910B3、6- _ _ HUAWEI DAVINCI ASCEND910B4、7- _ _ HUAWEI DaVinci Ascend910B 64G PCIE、 _ _ _ _ 8-BAIDU KUNLUN P800 OAM 96G、9- _ _ _ _ A910E、10- NVIDIA AMPERE A800 80G PCIE、11- _ _ _ _ OTHER。 |
| - ossStoragePat h | String | oss://*****/ | OSS存储路径。 |
| -quotaId | String | rq- d8890a98089c20b b0b2e27**** | 资源配额ID。 |
| -quotaName | String | test | 资源配额名称。 |
| -regionId | String | cn-hangzhou | 区域ID。 |
| -templateId | String | template- 4deda493094f804 d87 | 关联的模板ID。 |
| -templateType | String | 0 | 模板类型。枚举值：0-System template、1- Custom template、2-Clone from other draft。 |
| -versionId | Integer | 1 | 版本号。 |
| -duration | Struct | {"cpu": 10, "memory": 2048.0, "gpu": 1, "gpuMemory": 16384.0} | 工作流资源消耗统计。 |
| --cpu | Integer | 10 | CPU核数。 |
| --gpu | Integer | 1 | GPU个数。 |
| --gpuMemory | Float | 16384.0 | 显卡内存大小。 |
| --memory | Float | 2048.0 | 内存大小。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "templateType":"0",
   "draftId":"draft-abc123",
   "gmtModified":"2026-03-04T08:58:00Z",
   "componentId":"[\"comp-111\", \"comp-222\"]",
   "quotaName":"test",
   "datasetIds":"[\"ds-111\", \"ds-222\"]",
   "aliyunUid":"12345678",
   "gmtCreated":"2026-03-04T08:30:00Z",
   "quotaId":"rq-d8890a98089c20bb0b2e27****",
   "duration":[
    {
     "gpuMemory":16384.0,
     "memory":2048.0,
     "cpu":10,
     "gpu":1
    }
```

`],`

```json
   "templateId":"template-4deda493094f804d87",
   "versionId":1,
   "regionId":"cn-hangzhou",
   "modelIds":"[\"md-111\", \"md-222\"]",
   "ossStoragePath":"oss://*****/",
   "draftName":"test",
   "gpuType":0
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreatePipelineRun

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pipeline/run/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Body | 是 | draft- a8a63bc504127047a30 9279***** | 工作流ID，该参数必填。 |
| execution NodeId | Strin g | Body | 否 | node-hwejdqm9***** | 表示灵活调试中用户选定的节点。 |
| execution Type | Strin g | Body | 否 | 0 | 工作流执行类型，取值范围： 0：全量执行 1：仅执行该节点 2：从当前节点开始 3：执行到该节点 4：从根节点执行到该节点 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "runId": "run- *****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /pipeline/run/create HTTP/1.1 { "draftId":"draft-a8a63bc504127047a309279*****" }
```

智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"runId\": \"run-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyPipelineDraftContent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/draft/updatecontent HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Body | 是 | draft- a8a63bc504127047a30 9279***** | 工作流ID，该参数必填。 |
| content | Strin g | Body | 是 | "" | 工作区内容，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /pipeline/draft/updatecontent HTTP/1.1 { "draftId":"draft-a8a63bc504127047a309279*****", "content":"""" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeletePipelineDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- a8a63bc504127047a30 927**** | 工作流ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&draftId=draft-a8a63bc504127047a30927****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineNodeInputSchema

调用GetPipelineNodeInputSchema查询指定工作流组件输出的Schema。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pipeline/inputschema/get HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- 97a50b0b04fda046590a ff20***** | 工作流ID。 |
| nodeId | Strin g | Query | 是 | node-2qcgrt9ehog9**** | 节点ID。 |
| outputId | Strin g | Query | 是 | artifact- 740108480de***** | 任务结果ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -colNames | List | ["id", "name", "age", "score"] | CSV文件的列名列表，表示数据表的字段名称。 |
| -colTypes | List | ["int", "string", "int", "float"] | CSV文件的列类型列表，与列名列表一一对应， 表示每个字段的数据类型。 |

**示例**

请求示例

```
GET /pipeline/inputschema/get HTTP/1.1 &draftId=draft-97a50b0b04fda046590aff20***** &nodeId=node-2qcgrt9ehog9**** &outputId=artifact-740108480de*****
```

&公共请求参数正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":{
  "colTypes":"[\"int\", \"string\", \"int\", \"float\"] ",
  "colNames":"[\"id\", \"name\", \"age\", \"score\"]"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- 97a50b0b04fda046590a ff2***** | 工作流ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -datasetIds | List | ["ds-111", "ds- 222"] | 关联的数据集ID列表。 |
| -modelIds | List | ["md-111", "md- 222"] | 关联的模型ID列表。 |
| -aliyunUid | String | 123456 | 阿里云用户ID。 |
| -content | String | {"workflow": {...}} | 工作流内容。 |
| -draftId | String | draft-abc123 | 工作流ID。 |
| -draftName | String | test | 工作流名称。 |
| -gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T09:30:00Z | 修改时间。 |
| - ossStoragePat h | String | oss://*****/ | OSS存储路径。 |
| -quotaId | String | rq- d8890a98089b0b2 e27**** | 资源配额ID。 |
| -quotaName | String | test | 资源配额名称。 |
| -regionId | String | cn-hangzhou | 区域ID。 |
| -templateId | String | template- 4deda493094f804 d87 | 关联的模板ID。 |
| - templateName | String | test | 关联的模板名称。 |
| -templateType | String | 0 | 工作流类型。枚举值：0-System template、 1-Custom template、2-Clone from other draft。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -versionId | Integer | 1 | 版本号。 |

**示例**

请求示例

```
&draftId=draft-97a50b0b04fda046590aff2*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "templateType":"0",
  "draftId":"draft-abc123",
  "gmtModified":"2026-03-04T09:30:00Z",
  "quotaName":"test",
  "datasetIds":"[\"ds-111\", \"ds-222\"]",
  "aliyunUid":"123456",
  "gmtCreated":"2026-03-04T08:30:00Z",
  "quotaId":"rq-d8890a98089b0b2e27****",
  "templateId":"template-4deda493094f804d87",
  "content":"{\"workflow\": {...}}",
  "versionId":1,
  "regionId":"cn-hangzhou",
  "templateName":"test",
  "modelIds":"[\"md-111\", \"md-222\"]",
  "ossStoragePath":"oss://*****/",
  "draftName":"test"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ClonePipelineDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pipeline/draft/clone HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Body | 是 | draft- 97a50b0b04fda046590a ff20***** | 工作流ID，该参数必填。 |
| draftNam e | Strin g | Body | 是 | draft-name | 工作流名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| draftDesc | Strin g | Body | 否 | draft-desc | 工作流描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| ossStorag ePath | Strin g | Body | 是 | oss://*****/ | OSS存储路径，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "draftId": "draft- 575011c0045fd0** ***" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /pipeline/draft/clone HTTP/1.1 { "draftId":"draft-97a50b0b04fda046590aff20*****", "draftName":"draft-name", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "ossStoragePath":"oss://*****/" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"draftId\": \"draft-575011c0045fd0*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### TerminatePipelineRun

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/run/terminate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| runId | Strin g | Query | 是 | run- c75aa00807c78***** | 任务ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /pipeline/run/terminate HTTP/1.1 { "runId":"run-c75aa00807c78*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineDraftStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- 97a50b0b04fda046590a ff2***** | 工作流ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -nodes | Array | [{"nodeId": "node- 001", "nodeName": "训练节点", "status": "Running", "runId": "run-abc", "nodeKey": "train", "duration": {"cpu": 3600, "memory": 8192.0, "gpu": 2, "gpuMemory": 160.0}, "startedAt": "2026- 03-04T08:35:00Z", "finishedAt": "2026-03- 04T09:35:00Z"}] | 节点相关信息。 |
| --nodeId | String | node-123 | Pipeline节点ID。 |
| --nodeKey | String | train | Pipeline节点的键值，用于标识节点类型。 |
| --nodeName | String | test | 节点名称。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --runId | String | run- 13BeYuxc0fxO24u A75UppTiMRoQ | 任务运行ID。 |
| --startedAt | String | 2026-03- 04T08:00:00Z | Pipeline运行的开始时间，格式为ISO 8601标准时间。 |
| --status | String | Running | 节点状态。 |
| --duration | Struct | {"cpu": 10, "memory": 2048.0, "gpu": 1, "gpuMemory": 16384.0} | Pipeline运行的节点资源信息。 |
| ---cpu | Integer | 10 | CPU核数。 |
| ---gpu | Integer | 1 | GPU个数。 |
| ---gpuMemory | Float | 16384.0 | 显卡内存大小。 |
| ---memory | Float | 2048.0 | 内存大小。 |
| -aliyunUid | String | 12345678 | 阿里云用户ID。 |
| -draftId | String | draft- 97a50b0b04fda04 6590aff2***** | 工作流ID。 |
| -draftName | String | test | 工作流名称。 |
| -gmtCreated | String | 2026-03- 04T09:00:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T09:45:00Z | 修改时间。 |
| - ossStoragePat h | String | oss://*****/ | OSS存储路径。 |
| -quotaId | String | rq- ddfeea0e02175df0 b093**** | 资源配额ID。 |
| -regionId | String | cn-hangzhou | 区域ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -status | String | Running | 流水线状态。枚举值：0-Starting、1- Running、2-Succeeded、3-Failed、4- Error、5-Pending、6-Terminated。 |
| -templateId | String | template- 4deda493094f804 d87 | 关联的模板ID。 |
| -templateType | String | 0 | 工作流模板类型。枚举值：0-System template、1-Custom template、2-Clone from other draft。 |
| -versionId | Integer | 1 | 工作流版本号。 |

**示例**

请求示例

```
&draftId=draft-97a50b0b04fda046590aff2*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "templateType":"0",
  "draftId":"draft-97a50b0b04fda046590aff2*****",
  "gmtModified":"2026-03-04T09:45:00Z",
  "aliyunUid":"12345678",
  "gmtCreated":"2026-03-04T09:00:00Z",
  "nodes":[
   {
    "nodeName":"test",
    "duration":[
     {
      "gpuMemory":16384.0,
      "memory":2048.0,
      "cpu":10,
      "gpu":1
     }
```

`],`

```json
    "startedAt":"2026-03-04T08:00:00Z",
    "nodeKey":"train",
    "runId":"run-13BeYuxc0fxO24uA75UppTiMRoQ",
    "nodeId":"node-123",
    "status":"Running"
   }
```

`],`

```json
  "quotaId":"rq-ddfeea0e02175df0b093****",
  "templateId":"template-4deda493094f804d87",
  "versionId":1,
  "regionId":"cn-hangzhou",
  "ossStoragePath":"oss://*****/",
  "draftName":"test",
  "status":"Running"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineRun

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| runId | Strin g | Query | 是 | run- 13BeYuxc0fxO24uA***** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -nodes | Array | [{"nodeId": "node- 123", "status": "Succeeded", "nodeName": "训练节点", "runId": "run- abc123def456", "nodeKey": "train- node", "duration": {"cpu": 800, "memory": 1024.0, "gpu": 1, "gpuMemory": 16384.0}, "startedAt": "2026- 03-04T08:00:00Z", "finishedAt": "2026-03- 04T08:25:00Z"}] | Pipeline运行包含的节点列表。 |
| --finishedAt | String | 2026-03- 04T08:25:00Z | 节点的结束时间，格式为ISO 8601标准时间。 |
| --nodeId | String | node-123 | Pipeline节点ID。 |
| --nodeKey | String | train-node | Pipeline节点的键值，用于标识节点类型。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --nodeName | String | node-name | 节点名称。 |
| --runId | String | run-abc123def456 | 节点所属的Pipeline运行ID。 |
| --startedAt | String | 2026-03- 04T08:00:00Z | 节点的开始时间，格式为ISO 8601标准时间。 |
| --status | String | Succeeded | Pipeline节点的执行状态。 |
| --duration | Struct | {"cpu": 10, "memory": 2048.0, "gpu": 1, "gpuMemory": 16384.0} | Pipeline运行的节点资源信息。 |
| ---cpu | Integer | 10 | CPU核数。 |
| ---gpu | Integer | 1 | GPU个数。 |
| ---gpuMemory | Float | 16384.0 | 显卡内存大小。 |
| ---memory | Float | 2048.0 | 内存大小。 |
| -content | String | {"nodes": [], "edges": []} | Pipeline运行的内容配置，包含节点和边的信息。 |
| -finishedAt | String | 2026-03- 04T08:30:00Z | Pipeline运行的结束时间，格式为ISO 8601标准时间。 |
| -runId | String | run-abc123def456 | Pipeline运行ID。 |
| -runStatus | String | Succeeded | Pipeline运行状态。 |
| -sourceId | String | draft- xyz789ghi012 | Pipeline运行的源ID。 |
| -startedAt | String | 2026-03- 04T08:00:00Z | Pipeline运行的开始时间，格式为ISO 8601标准时间。 |
| -versionId | Integer | 1 | Pipeline运行的版本号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -duration | Struct | {"cpu": 10, "memory": 2048.0, "gpu": 1, "gpuMemory": 16384.0} | Pipeline运行的资源信息。 |
| --cpu | Integer | 10 | CPU核数。 |
| --gpu | Integer | 1 | GPU个数。 |
| --gpuMemory | Float | 16384.0 | 显卡内存大小。 |
| --memory | Float | 2048.0 | 内存大小。 |

**示例**

请求示例

```
&runId=run-13BeYuxc0fxO24uA*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "sourceId":"draft-xyz789ghi012",
  "versionId":1,
  "nodes":[
   {
    "nodeName":"node-name",
    "duration":[
     {
      "gpuMemory":16384.0,
      "memory":2048.0,
      "cpu":10,
      "gpu":1
     }
```

`],`

```json
    "startedAt":"2026-03-04T08:00:00Z",
    "nodeKey":"train-node",
    "runId":"run-abc123def456",
    "nodeId":"node-123",
    "finishedAt":"2026-03-04T08:25:00Z",
    "status":"Succeeded"
   }
```

`],`

```json
  "startedAt":"2026-03-04T08:00:00Z",
  "duration":{
   "gpuMemory":16384.0,
   "memory":2048.0,
   "cpu":10,
   "gpu":1
  },
  "runId":"run-abc123def456",
  "content":" {\"nodes\": [], \"edges\": []}",
  "runStatus":"Succeeded",
  "finishedAt":"2026-03-04T08:30:00Z"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListPipelineRun

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- 97a50b0b04fda046590a ff2***** | 工作流ID。 |
| runId | Strin g | Query | 否 | run-5a15ce3102da***** | 任务ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -finishedAt | String | 2026-03- 04T08:30:00Z | Pipeline运行的结束时间，格式为ISO 8601标准时间。 |
| -runId | String | run-abc123def456 | 任务ID。 |
| -runStatus | String | Succeeded | Pipeline运行的执行状态。 |
| -sourceId | String | draft- xyz789ghi012 | Pipeline运行的源ID。 |
| -startedAt | String | 2026-03- 04T08:00:00Z | Pipeline运行的开始时间，格式为ISO 8601标准时间。 |
| -versionId | Integer | 1 | Pipeline运行的版本号。 |
| -duration | Struct | {"cpu": 10, "memory": 2048.0, "gpu": 1, "gpuMemory": 16384.0} | Pipeline运行的资源信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --cpu | Integer | 10 | CPU核数。 |
| --gpu | Integer | 1 | GPU个数。 |
| --gpuMemory | Float | 16384.0 | 显卡内存大小。 |
| --memory | Float | 2048.0 | 内存大小。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&draftId=draft-97a50b0b04fda046590aff2*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "sourceId":"draft-xyz789ghi012",
   "versionId":1,
   "startedAt":"2026-03-04T08:00:00Z",
   "duration":[
    {
     "gpuMemory":16384.0,
     "memory":2048.0,
     "cpu":10,
     "gpu":1
    }
```

`],`

```json
   "runId":"run-abc123def456",
   "runStatus":"Succeeded",
   "finishedAt":"2026-03-04T08:30:00Z"
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineArtifactData

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pipeline/artifact/get HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| artifactId | Strin g | Query | 是 | artifact-f2ebc8e20***** | 制品ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /pipeline/artifact/get HTTP/1.1 &artifactId=artifact-f2ebc8e20*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListPipelineArtifact

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /pipeline/artifact/list HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| runId | Strin g | Query | 是 | run-13BeYuxc0fxO2***** | 任务ID。 |
| nodeId | Strin g | Query | 否 | node-tqrkojdnzd***** | 节点ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 制品列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| artifactId | Strin g | Query | 否 | artifact- 9c5e7e1a02***** | 制品ID。 |
| artifactNa me | Strin g | Query | 否 | artifact-name | 制品名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - artifactCreate dTime | String | 2026-03- 04T08:30:00Z | 制品的创建时间。 |
| -artifactId | String | artifact- 21ca53ac16a6**** * | 制品ID。 |
| -artifactKey | String | artifacts/*****/mod el output _ | 制品在存储系统中的键路径。 |
| -artifactName | String | artifact-name | 制品名称。 |
| -dataType | String | Table | 制品的数据类型，表示数据的存储格式。 |
| -nodeId | String | node- tqrkojdnzd***** | 节点ID。 |
| -nodeName | String | node-name | 节点名称。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -runId | String | run- 13BeYuxc0fxO2*** ** | 任务ID。 |
| -storagePath | String | oss://*****/model o _ utput | 制品的存储路径。 |
| -subType | String | pytorch | 制品的子类型。 |
| -type | String | model | 制品类型。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /pipeline/artifact/list HTTP/1.1 &runId=run-13BeYuxc0fxO2*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "nodeName":"node-name",
   "artifactName":"artifact-name",
   "dataType":"Table",
   "artifactKey":"artifacts/*****/model_output",
   "artifactId":"artifact-21ca53ac16a6*****",
   "storagePath":"oss://*****/model_output",
   "subType":"pytorch",
   "artifactCreatedTime":"2026-03-04T08:30:00Z",
   "runId":"run-13BeYuxc0fxO2*****",
   "type":"model",
   "nodeId":"node-tqrkojdnzd*****"
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreatePipelineDraft

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pipeline/draft/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftNam e | Strin g | Body | 是 | draft-name | 工作流名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| draftDesc | Strin g | Body | 否 | draft-desc | 工作流描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |

| A | I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| templateI d | Strin g | Body | 否 | template-**** | 模板ID。 |
| ossStorag ePath | Strin g | Body | 是 | oss://*****/ | 持久化存储设置，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "draftId": "draft- ***** } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /pipeline/draft/create HTTP/1.1 { "draftName":"draft-name", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "ossStoragePath":"oss://*****/" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{      \"draftId\": \"draft-*****}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyPipelineDraftContentByRollback

调用ModifyPipelineDraftContentByRollback修改工作流的内容回滚到指定的版本。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/draft/versionRollback HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| runId | Strin g | Query | 是 | run- 13BeYuxc0fxO24uA***** | 需要回滚的任务ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /pipeline/draft/versionRollback HTTP/1.1 { "runId":"run-13BeYuxc0fxO24uA*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineDraftSchedule

调用GetPipelineDraftSchedule查询指定工作流的周期调度信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Query | 是 | draft- 97a50b0b04fda046590a ff2***** | 工作流ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - scheduleConfi g | List | [1, 3, 5] | 调度配置列表，按周调度时表示星期几（1-7，1 表示周一），按月调度时表示每月的几号（1- 31）。 |
| -draftId | String | draft- 97a50b0b04fda04 6590aff2***** | 工作流ID。 |
| -executeTime | String | 14:30:00 | 每日执行的具体时间，格式为HH:mm:ss。 |
| - scheduleStatu s | Boolean | true | 调度任务的启用状态，true表示已启用，false表示已禁用。 |
| -scheduleType | Integer | 1 | 调度类型，0表示按天调度，1表示按周调度，2 表示按月调度。 |
| -timeZone | String | Asia/Shanghai | 调度任务使用的时区，用于确定执行时间的时区上下文。 |

**示例**

请求示例

```
&draftId=draft-97a50b0b04fda046590aff2*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### ModifyPipelineDraftSchedule

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/run/modifyPipelineDraftSchedule HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| scheduleT ype | Strin g | Body | 是 | 1 | 调度类型，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /pipeline/run/modifyPipelineDraftSchedule HTTP/1.1 { "scheduleType":"1", "scheduleStatus":"0", "timeZone":"Asia/Shanghai" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 模板

##### ListPipelineDraftTemplate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 工作流模板列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| templateT ype | Integ er | Query | 否 | 0 | 模板类型，取值范围： 系统模版：0 自定义模版：1 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -componentId | List | ["comp-111", "comp-222"] | 关联的组件ID列表。 |
| -aliyunUid | String | 123456 | 阿里云用户ID。 |
| -gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T09:30:00Z | 修改时间。 |
| -regionId | String | cn-hangzhou | 区域ID。 |
| - templateConte nt | String | {"workflow": {...}} | 工作流模板的内容。 |
| -templateDesc | String | desc | 工作流模板的描述信息。 |
| -templateId | String | template- 4deda493094f804 d87 | 工作流模板ID。 |
| - templateName | String | test-template | 工作流模板名称。 |
| -templateType | Integer | 0 | 工作流模板类型枚举。枚举值：0-System template（系统模板）、1-Custom template（自定义模板）、2-Clone from other draft（从其他草稿克隆）。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "templateType":0,
   "gmtModified":"2026-03-04T09:30:00Z",
   "componentId":"[\"comp-111\", \"comp-222\"]",
   "aliyunUid":"123456",
   "gmtCreated":"2026-03-04T08:30:00Z",
   "regionId":"cn-hangzhou",
   "templateName":"test-template",
   "templateDesc":"desc",
   "templateContent":"{\"workflow\": {...}}",
   "templateId":"template-4deda493094f804d87"
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateDraftTemplate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /pipeline/draft/saveTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| draftId | Strin g | Body | 是 | draft- 97a50b0b04fda046590a ff2***** | 工作流ID，该参数必填。 |
| templateN ame | Strin g | Body | 是 | template-name | 模板名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| descriptio n | Strin g | Body | 否 | template-desc | 模版描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| content | Strin g | Body | 是 | "" | 工作区内容，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "draftId": "draft- 575011c0045fd0** ***" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /pipeline/draft/saveTemplate HTTP/1.1 { "draftId":"draft-97a50b0b04fda046590aff2*****", "templateName":"template-name", "content":"""" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{      \"draftId\": \"draft-575011c0045fd0*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteDraftTemplate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| templateI d | Strin g | Query | 是 | draft-586602cf0c1***** | 模板ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&templateId=draft-586602cf0c1*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 组件

##### ListPipelineComponent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Body | 否 | comp- 1c2d7a2f0cd67049eb0a ac90**** | 组件ID。 |
| pageIndex | Integ er | Body | 否 | 1 | 组件列表的页码。 默认值：1。 |
| pageSize | Integ er | Body | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| templateT ype | Integ er | Body | 是 | 0 | 组件类型，该参数必填。 |
| imageId | Strin g | Body | 否 | img- 66562b610952c0441e0 ba6a***** | 镜像ID。 |
| imageVer sion | Strin g | Body | 否 | v1 | 镜像版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -codeId | List | ["code-111", "code-222"] | 关联的代码集ID列表。 |
| -parameters | Array | [{"name": "learning rate", _ "default": "0.001", "component": "InputNumber", "title": "学习率", "tooltip": "模型训练的学习率", "rules": [{"required": true, "min": "0.0001", "max": "1.0"}], "dataSource": [{"label": "默认值", "value": "0.001"}], "props": {"step": "0.0001"}, "reactions": {"onChange": "updateModel"}, "pathType": "relative", "anchor": "param1"}] | 组件参数列表。 |
| --rules | Array | [{"required": true, "min": "0.0001", "max": "1.0"}] | 参数验证规则列表。 |
| ---required | Boolean | true | 是否必填。 |
| --component | String | InputNumber | 参数组件类型。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --default | String | 0 | 参数默认值。 |
| --name | String | test | 输入名称。 |
| --title | String | 学习率 | 参数标题。 |
| -componentId | String | comp-abc123 | 工作流组件的唯一标识符。 |
| -description | String | desc | 组件描述信息。 |
| -gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T09:30:00Z | 修改时间。 |
| -identifier | String | pytorch-train | 组件标识符。 |
| -imageId | String | img-xyz789 | 镜像ID。 |
| -imageVersion | String | v1 | 镜像版本。 |
| -name | String | test | 组件名称。 |
| - relatedTaskCo unt | Integer | 5 | 组件关联的任务数量。 |
| -shared | Integer | 1 | 共享范围： 0：本资源集。 1：本组织及下级组织。 2：本组织。 |
| -type | String | 1 | 组件类型。 |
| -version | String | v1 | 组件版本号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -io | Struct | {"outputs": [{"dataType": "model", "subType": "pytorch", "id": "output-model", "type": "artifact", "required": true, "properties": ["accuracy", "loss"], "name": "模型输出"}], "inputs": [{"dataType": "dataset", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}]} | 组件输入输出定义，包含输入和输出列表。 |
| --inputs | Array | [{"dataType": "model", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}] | 输入列表。 |
| ---dataType | String | model | 输出数据类型。 |
| ---id | String | output-model | 输出ID。 |
| ---name | String | test模型输出 | 输出名称。 |
| ---required | Boolean | true | 是否必填。 |
| ---type | String | artifact | 输出类型。 |
| --outputs | Array | [{"dataType": "model", "subType": "pytorch", "id": "output-model", "type": "artifact", "required": true, "properties": ["accuracy", "loss"], "name": "模型输出"}] | 输出列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---dataType | String | model | 输出数据类型。 |
| ---id | String | output-model | 输出ID。 |
| ---name | String | test模型输出 | 输出名称。 |
| ---required | Boolean | true | 是否必填。 |
| ---type | String | artifact | 输出类型。 |
| -metaData | Struct | {"visual": true, "identifier": "pytorch-train", "version": "1.0.0", "dispalyName": "PyTorch训练"} | 组件元数据，包含可视化标识、标识符、版本、 显示名称等信息。 |
| --visual | Boolean | true | 是否可视化。 |
| --identifier | String | pytorch-train | 组件标识符。 |
| --version | String | 1.0.0 | 组件版本号。 |
| --dispalyName | String | PyTorch训练 | 组件显示名称。 |
| -resources | Struct | {"cpu": 4, "memory": 8192, "gpu": 1} | 组件资源配置，包含CPU核数、内存（MB）、 GPU数量。 |
| --cpu | Integer | 4 | CPU核数。 |
| --gpu | Integer | 1 | GPU个数。 |
| --memory | Integer | 8192 | 内存大小。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 组件的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 标准任务的页码。 |

**示例**

请求示例

```
&templateType=0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "imageVersion":"v1",
   "identifier":"pytorch-train",
   "shared":1,
   "gmtModified":"2026-03-04T09:30:00Z",
   "componentId":"comp-abc123",
   "imageId":"img-xyz789",
   "gmtCreated":"2026-03-04T08:30:00Z",
   "description":"desc",
   "relatedTaskCount":5,
   "type":"1",
   "version":"v1",
   "resources":[
    {
     "memory":8192,
     "cpu":4,
     "gpu":1
    }
```

`],`

```json
   "codeId":"[\"code-111\", \"code-222\"]",
   "io":[
    {
     "inputs":[
      {
"dataTpe""model"
```

智能体工厂 OpenTrek

```json
       "dataType":"model",
```

`"name":"test`模型输出`",`

```json
       "id":"output-model",
       "type":"artifact",
       "required":true
      }
```

`],`

```json
     "outputs":[
      {
       "dataType":"model",
```

`"name":"test`模型输出`",`

```json
       "id":"output-model",
       "type":"artifact",
       "required":true
      }
```

]

```
    }
```

`],`

```json
   "name":"test",
   "metaData":[
    {
     "identifier":"pytorch-train",
     "visual":true,
     "dispalyName":"PyTorch训练",
     "version":"1.0.0"
    }
```

`],`

```json
   "parameters":[
    {
     "component":"InputNumber",
     "default":"0",
     "rules":[
      {
       "required":true
      }
```

`],`

```json
     "name":"test",
```

`"title":"`学习率"

```
    }
```

]

```
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

智能体工厂 OpenTrek

##### GetPipelineComponentTree

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
|  |  | [{"treeNodeid": "pytorch", "treeNodeName": "PyTorch训练", "treeNodeType": "subcategory", "sortKey": 1, "children": [], "components": [{"componentId": "comp-abc123", "identifier": "pytorch-train", "name": "PyTorch 训练组件", "description": "用于 PyTorch模型训练的组件", "componentPath": "/train/pytorch", "metaData": {"visual": true, "identifier": "pytorch-train", "version": "1.0.0", "dispalyName": "PyTorch训练"}, "type": 1, "version": "1.0.0", "path": "/path/to/compone nt", "io": {"outputs": [{"dataType": "model", "subType": "pytorch", "id": "output-model", |  |

智能体工厂 OpenTrek

| 参数名称 | 类型 | "type": "artifact", 示例 "required": true, | 说明 |
|---|---|---|---|
| -children | List | "properties": ["accuracy", "loss"], "name": "模型输出"}], "inputs": [{"dataType": "dataset", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}]}, "resources": {"cpu": 4, "memory": 8192, "gpu": 1}, "parameters": [{"name": "learning rate", _ "default": "0.001", | 子节点列表，用于构建组件树的层级结构。 |
|  |  | "component": "InputNumber", "title": "学习率", "tooltip": "模型训练的学习率", "rules": [{"required": true, "min": "0.0001", "max": "1.0"}], "dataSource": [{"label": "默认值", "value": "0.001"}], "props": {"step": "0.0001"}, "reactions": {"onChange": "updateModel"}, "pathType": "relative", "anchor": "param1"}], "codeId": ["code- 111", "code-222"], "imageId": "img- xyz789", "imageVersion": "v1.2.3", "gmtCreated": "2026-03- 04T08:30:00Z", "gmtModified": "2026-03- 04T09:45:00Z", "relatedTaskCount" : 5}]}] |  |
|  |  | [{"componentId": "comp-abc123", "identifier": "pytorch-train", "name": "PyTorch 训练组件", "description": "用于 PyTorch模型训练的组件", |  |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | "componentPath": 示例 "/train/pytorch", | 说明 |
| -components | Array | "metaData": {"visual": true, "identifier": "pytorch-train", "version": "1.0.0", "dispalyName": "PyTorch训练"}, "type": 1, "version": "1.0.0", "path": "/path/to/compone nt", "io": {"outputs": [{"dataType": "model", "subType": "pytorch", "id": "output-model", "type": "artifact", "required": true, "properties": ["accuracy", "loss"], "name": "模型输出"}], "inputs": [{"dataType": "dataset", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}]}, "resources": {"cpu": 4, "memory": 8192, "gpu": 1}, "parameters": [{"name": "learning rate", _ "default": "0.001", "component": "InputNumber", "title": "学习率", "tooltip": "模型训练的学习率", "rules": [{"required": true, "min": "0.0001", "max": "1.0"}], "dataSource": [{"label": "默认值", "value": "0.001"}], "props": {"step": "0.0001"}, "reactions": {"onChange": "updateModel"}, "pathType": "relative", "anchor": "param1"}], "codeId": ["code- 111", "code-222"], "imageId": "img- | 组件列表，包含该节点下的所有组件详情。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | xyz789", 示例 "imageVersion": | 说明 |
|---|---|---|---|
|  |  | "v1.2.3", "gmtCreated": "2026-03- 04T08:30:00Z", "gmtModified": "2026-03- 04T09:45:00Z", "relatedTaskCount" : 5}] |  |
| --parameters | Array | [{"name": "learning rate", _ "default": "0.001", "component": "InputNumber", "title": "学习率", "tooltip": "模型训练的学习率", "rules": [{"required": true, "min": "0.0001", "max": "1.0"}], "dataSource": [{"label": "默认值", "value": "0.001"}], "props": {"step": "0.0001"}, "reactions": {"onChange": "updateModel"}, "pathType": "relative", "anchor": "param1"}] | 组件参数列表。 |
| ---dataSource | Array | [{"label": "默认值", "value": "0.001"}] | 数据来源。 |
| ----label | String | 默认值 | 标签。 |
| ----value | String | 0.001 | 指标值。 |
| ---rules | Array | [{"required": true, "min": "0.0001", "max": "1.0"}] | 参数验证规则列表。 |
| ----required | Boolean | true | 是否必填。 |
| ---component | String | InputNumber | 参数组件类型。 |
| ---default | String | 0 | 参数默认值。 |
| ---name | String | test | 输入名称。 |
| ---pathType | String | relative | 地址类型。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---title | String | 学习率 | 参数标题。 |
| ---tooltip | String | 模型训练的学习率 | 提示信息。 |
| ---reactions | Struct | {"onChange": "updateModel"} | 依赖关系。 |
| ---- dependencies | List | ["react": "^18.2.0", "axios": "^1.4.0"] | 依赖列表。 |
| ----fulfill | Struct | {} | 指定信息 |
| -----state | Struct | {} | 状态 |
| ------display | String | 0 | 显示名称。 |
| --componentId | String | comp-abc123 | 工作流组件的唯一标识符。 |
| --description | String | desc | 组件描述信息。 |
| --gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| --gmtModified | String | 2026-03- 04T09:30:00Z | 修改时间。 |
| --identifier | String | pytorch-train | 组件标识符。 |
| --name | String | test | 组件名称。 |
| -- relatedTaskCo unt | Integer | 5 | 组件关联的任务数量。 |
| --type | String | 1 | 组件类型。 |
| --version | String | v1 | 组件版本号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --io | Struct | {"outputs": [{"dataType": "model", "subType": "pytorch", "id": "output-model", "type": "artifact", "required": true, "properties": ["accuracy", "loss"], "name": "模型输出"}], "inputs": [{"dataType": "dataset", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}]} | 组件输入输出定义，包含输入和输出列表。 |
| ---inputs | Array | [{"dataType": "dataset", "subType": "csv", "id": "input- dataset", "type": "artifact", "required": true, "name": "数据集输入"}] | 输入列表。 |
| ----dataType | String | model | 输出数据类型。 |
| ----id | String | output-model | 输出ID。 |
| ----name | String | 模型输出 | 输出名称。 |
| ----required | Boolean | true | 是否必填。 |
| ----type | String | artifact | 输出类型。 |
| ---outputs | Array | [{"dataType": "model", "subType": "pytorch", "id": "output-model", "type": "artifact", "required": true, "properties": ["accuracy", "loss"], "name": "模型输出"}] | 输出列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----dataType | String | model | 输出数据类型。 |
| ----id | String | output-model | 输出ID。 |
| ----name | String | 模型输出 | 输出名称。 |
| ----required | Boolean | true | 是否必填。 |
| ----type | String | artifact | 输出类型。 |
| --metaData | Struct | {"visual": true, "identifier": "pytorch-train", "version": "1.0.0", "dispalyName": "PyTorch训练"} | 组件元数据，包含可视化标识、标识符、版本、 显示名称等信息。 |
| ---visual | Boolean | true | 是否可视化。 |
| ---identifier | String | pytorch-train | 组件标识符。 |
| ---version | String | 1.0.0 | 组件版本号。 |
| --- dispalyName | String | PyTorch训练 | 组件显示名称。 |
| --resources | Struct | {"cpu": 4, "memory": 8192} | 组件资源配置，包含CPU核数、内存（MB）。 |
| ---cpu | Integer | 4 | CPU核数。 |
| ---memory | Integer | 8192 | 内存大小。 |
| - treeNodeNam e | String | 训练组件 | 组件名称，表示组件分类的显示名称。 |
| -treeNodeid | String | pytorch-train | 组件ID，组件唯一标识。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
```

`"treeNodeName":"`训练组件`",`

```json
   "components":[
    {
     "metaData":[
      {
       "identifier":"pytorch-train",
       "visual":true,
       "dispalyName":"PyTorch训练",
       "version":"1.0.0"
      }
```

`],`

```json
     "identifier":"\tpytorch-train",
     "gmtModified":"2026-03-04T09:30:00Z",
     "componentId":"comp-abc123",
     "gmtCreated":"2026-03-04T08:30:00Z",
     "description":"desc",
     "relatedTaskCount":5,
     "type":"1",
     "resources":[
      {
       "memory":8192,
       "cpu":4
      }
```

`],`

```json
     "version":"v1",
     "parameters":[
      {
       "component":"InputNumber",
       "default":"0",
       "name":"test",
```

`"tooltip":"`模型训练的学习率`",`

```
"reactions"[
```

智能体工厂 OpenTrek

```json
       "reactions":[
        {
         "fulfill":[
          {
           "state":[
            {
             "display":"0"
            }
```

]

```
          }
```

`],`

```json
         "dependencies":"[\"react\": \"^18.2.0\", \"axios\": \"^1.4.0\"]"
        }
```

`],`

```json
       "pathType":"relative",
```

`"title":"`学习率`",`

```json
       "rules":[
        {
         "required":true
        }
```

`],`

```json
       "dataSource":[
        {
```

`"label":"`默认值`",`

```json
         "value":"0.001"
        }
```

]

```
      }
```

`],`

```json
     "io":[
      {
       "inputs":[
        {
         "dataType":"model",
```

`"name":"`模型输出`",`

```json
         "id":"output-model",
         "type":"artifact",
         "required":true
        }
```

`],`

```json
       "outputs":[
        {
         "dataType":"model",
```

`"name":"`模型输出`",`

```json
         "id":"output-model",
         "type":"artifact",
         "required":true
        }
```

]

```
      }
```

`],`

```json
     "name":"test"
    }
```

`],`

```json
"children":"[{\"treeNodeid\":\"pytorch\",\"treeNodeName\":\"PyTorch训练\",\"treeN
```

智能体工厂 OpenTrek

```
   children:[{\treeNodeid\: \pytorch\, \treeNodeName\: \PyTorch训练\, \treeN
odeType\": \"subcategory\", \"sortKey\": 1, \"children\": [], \"components\": [{\"compo nentId\": \"comp-abc123\", \"identifier\": \"pytorch-train\", \"name\": \"PyTorch训练组
```

件\", \"description\": \"用于`PyTorch`模型训练的组件\", \"componentPath\":

```json
\"/train/pytorch\", \"metaData\": {\"visual\": true, \"identifier\": \"pytorch-train\", \"version\": \"1.0.0\", \"dispalyName\": \"PyTorch训练\"}, \"type\": 1, \"version\": \"1.0.0\", \"path\": \"/path/to/component\", \"io\": {\"outputs\": [{\"dataType\": \"mo del\", \"subType\": \"pytorch\", \"id\": \"output-model\", \"type\": \"artifact\", \"re quired\": true, \"properties\": [\"accuracy\", \"loss\"], \"name\": \"模型输出\"}], \"inputs\": [{\"dataType\": \"dataset\", \"subType\": \"csv\", \"id\": \"input-dataset\ ", \"type\": \"artifact\", \"required\": true, \"name\": \"数据集输入\"}]}, \"resources\" : {\"cpu\": 4, \"memory\": 8192, \"gpu\": 1}, \"parameters\": [{\"name\": \"learning_rate\", \"default\": \"0.001\", \"component\": \"InputNumber\", \"title\": \ "学习率\", \"tooltip\": \"模型训练的学习率\", \"rules\": [{\"required\": true, \"min\": \"0 .0001\", \"max\": \"1.0\"}], \"dataSource\": [{\"label\": \"默认值\", \"value\": \"0.001 \"}], \"props\": {\"step\": \"0.0001\"}, \"reactions\": {\"onChange\": \"updateModel\"}, \"pathType\": \"relative\", \"anchor\": \"param1\"}], \"codeId\": [\" code-111\", \"code-222\"], \"imageId\": \"img-xyz789\", \"imageVersion\": \"v1.2.3\", \ "gmtCreated\": \"2026-03-04T08:30:00Z\", \"gmtModified\": \"2026-03-04T09:45:00Z\", \"r elatedTaskCount\": 5}]}]",
   "treeNodeid":"pytorch-train"
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetPipelineComponent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Query | 是 | comp- 1c2d7a2f0cd67049eb0a ac90**** | 组件ID，该参数必填。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - codeMountList | Array | [{"codeId": "cd- 111", "codeRepoType": "GIT", "sourcePath": "/repo/path", "storageType": 1, "mountPath": "/workspace/code", "pvcName": "pvc- code", "dataAccInstance": "da-001"}] | 代码集挂载列表。 |
| --codeId | String | cd-111 | 代码集ID。 |
| -- codeRepoType | String | GIT | 代码集类型。 |
| --mountPath | String | /workspace/code | 代码集挂载路径。 |
| -componentId | String | comp-abc123 | 自定义组件ID。 |
| - customCompo nentDesc | String | 用于自定义模型训练的组件 | 自定义组件描述信息。 |
| - customCompo nentName | String | test | 自定义组件名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtCreated | String | 2026-03- 04T08:30:00Z | 创建时间。 |
| -gmtModified | String | 2026-03- 04T09:30:00Z | 修改时间。 |
| -imageId | String | img-xyz789 | 镜像ID。 |
| -imageType | Integer | 1 | 镜像类型。 |
| -imageVersion | String | v1 | 镜像版本。 |
| -parameters | Map | {"learning rate": _ {"name": "learning rate", _ "type": "float", "defaultValue": "0.001", "required": true}} | 组件参数映射，包含参数名称、类型、默认值、 是否必填等信息。 |
| - relatedTaskCo unt | Integer | 5 | 组件关联任务数量。 |
| - startCommand | String | python train.py -- epochs 100 | 启动命令。 |
| -type | Integer | 1 | 组件类型枚举。枚举值：0- SYSTEM COMPONENT（系统组件）、1- _ CUSTOM COMPONENT（自定义组件）。 _ |
| -inputs | Struct | {"artifacts": {"input-dataset": {"name": "数据集输入", "type": "artifact", "dataType": "dataset", "required": true}}} | 组件自定义输入。 |
| --artifacts | Map | {"input-dataset": {"name": "数据集输入", "type": "artifact", "dataType": "dataset", "required": true}} | 输入制品映射。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -outputs | Struct | {"artifacts": {"output-model": {"name": "模型输出", "type": "artifact", "dataType": "model", "required": true}}} | 组件自定义输出。 |
| --artifacts | Map | {"output-model": {"name": "模型输出", "type": "artifact", "dataType": "model", "required": true}} | 输出制品映射。 |
| -resource | Struct | {"cpu": "4", "memory": "8192", "gpu": "1"} | 组件所需资源默认配置，包含CPU核数、内存 （MB）、GPU数量。 |
| --cpu | String | 4 | CPU核数。 |
| --gpu | String | 1 | GPU个数。 |
| --memory | String | 8192 | 内存大小。 |

**示例**

请求示例

```
&componentId=comp-1c2d7a2f0cd67049eb0aac90****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "imageVersion":"v1",
  "gmtModified":"2026-03-04T09:30:00Z",
  "componentId":"comp-abc123",
  "imageId":"img-xyz789",
  "outputs":{
   "artifacts":{
    "outputmodel":{
     "dataType":"model",
```

`"name":"`模型输出`",`

```json
     "type":"artifact",
     "required":true
    }
```

智能体工厂 OpenTrek

```json
   }
  },
  "gmtCreated":"2026-03-04T08:30:00Z",
  "resource":{
   "memory":"8192",
   "cpu":"4",
   "gpu":"1"
  },
```

`"customComponentDesc":"`用于自定义模型训练的组件`",`

```json
  "startCommand":"python train.py --epochs 100",
  "customComponentName":"test",
  "relatedTaskCount":5,
  "type":1,
  "codeMountList":[
   {
    "codeId":"cd-111",
    "mountPath":"/workspace/code",
    "codeRepoType":"GIT"
   }
```

`],`

```json
  "imageType":1,
  "parameters":{
   "learning_rate":{
    "defaultValue":"0.001",
    "name":"learning_rate",
    "type":"float",
    "required":true
   }
  },
  "inputs":{
   "artifacts":{
    "inputdataset":{
     "dataType":"dataset",
```

`"name":"`数据集输入`",`

```json
     "type":"artifact",
     "required":true
    }
   }
  }
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreatePipelineCustomComponent

调用CreatePipelineCustomComponent创建工作流自定义组件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /pipeline/component/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| customCo mponentN ame | Strin g | Body | 是 | component-name | 组件名称，该参数必填。 |
| customCo mponentD esc | Strin g | Body | 否 | omponent-desc | 组件描述。 |
| imageId | Strin g | Body | 是 | img- 66562b610952c0441e0 ba6a***** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| startCom mand | Strin g | Body | 是 | python3 main.py | 启动命令，该参数必填。 |
| codeMoun tList | Json | Body | 是 | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046ec0bc ad0d3682****" }] | 代码集配置，该参数必填。 |
| componen tDefaultR esource | Json | Body | 是 | {"cpu": "500", "memory": "1G"} | 表示组件的默认资源值，用于在未指定具体资源配置时的后备选项，该参数必填。 |
| inputs | Json | Body | 否 | {"artifacts":{"input1": {"type":"DataSet","data Type":"Table","required" :true,"name":"input"}}} | 组件输入列表。 |
| outputs | Json | Body | 否 | {"artifacts":{"output1": {"type":"Model","dataTy pe":"File","required":fals e,"name":"output"}}} | 组件的输出列表。 |
| parameter s | Json | Body | 否 | {"parameter1": {"type":"TextArea","na me":"featureColName"}, "parameter2": {"type":"TextArea","na me":"labelColName"},"p arameter3": {"type":"NumberPicker", "name":"maxIter","defau ltValue":"100"},"parame ter4": {"type":"NumberPicker", "name":"regularizedLev el","defaultValue":"1"}} | 组件的参数列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| isUseGpu | Boole an | Body | 是 | false | 是否使用GPU，该参数必填，取值范围： true：使用。 false：禁用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "componentId": "comp-****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /pipeline/component/create HTTP/1.1 { "customComponentName":"component-name", "imageId":"img-66562b610952c0441e0ba6a*****", "imageVersion":"v1", "startCommand":"python3 main.py", "codeMountList":"[{
 "mountPath": "/root/",
 "codeId": "cd-f1bb797e0cef2046ec0bcad0d3682****"
}]", "componentDefaultResource":"{"cpu": "500", "memory": "1G"}", "isUseGpu":"false" }
```

正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":"{      \"componentId\": \"comp-****\"}",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyPipelineCustomComponent

调用ModifyPipelineCustomComponent修改指定自定义组件部分信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /pipeline/component/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Body | 是 | comp- 1c2d7a2f0cd67049eb0a ac90**** | 组件ID，该参数必填。 |
| componen tName | Strin g | Body | 是 | python组件 | 组件名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | annotation-description | 自定义组件描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /pipeline/component/modify HTTP/1.1 { "componentId":"comp-1c2d7a2f0cd67049eb0aac90****", "componentName":"python组件" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeletePipelineCustomComponent

调用DeletePipelineCustomComponent删除指定自定义组件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /pipeline/component/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Query | 是 | comp- 1c2d7a2f0cd67049eb0a ac90**** | 组件ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /pipeline/component/delete HTTP/1.1 &componentId=comp-1c2d7a2f0cd67049eb0aac90****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 在线服务

#### 在线服务

##### ModifyOnlineServiceLoraAdapter

调用ModifyOnlineServiceLoraAdapter动态加卸载LoRA模型。 智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-lora-adapter HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 否 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |
| loraLoadIn fo | Json | Body | 否 | {} | LoRA加载配置信息。 |
| regionId | Strin g | Body | 否 | cn-hangzhou | 地域ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
PUT /online-service/modify-lora-adapter HTTP/1.1 { }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

| { "success":false, "dynamicMessages":"-", "errorMessage":"", "errorCode":"500", "httpCode":200 } |  |
|---|---|

##### ListOnlineService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 在线服务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| serviceNa me | Strin g | Query | 否 | service-name | 在线服务名称。 |
| serviceId | Strin g | Query | 否 | os- 5be13385078c904e750 91aa0606**** | 在线服务ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceSta tus | Integ er | Query | 否 | 0 | 在线服务状态，取值范围： 0：启动中。 1：运行中。 2：已停止。 3：失败。 |
| quotaId | Strin g | Query | 否 | rq- ddfeea0e0217604a5b0a 5df0b093**** | 资源配额ID。 |
| quotaNam e | Strin g | Query | 否 | quota-name | 资源配额名称。 |
| imageId | Strin g | Query | 否 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |
| imageNa me | Strin g | Query | 否 | image-name | 镜像名称。 |
| modelId | Strin g | Query | 否 | md- e97c65da0d70b04f2b0b bcb05740**** | 模型仓库ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型仓库名称。 |
| storagePa th | Strin g | Query | 否 | oss://****/**** | 在线服务存储路径。 |
| resourceP oolId | Strin g | Query | 否 | rp-123456 | 资源池ID。 |
| modelCat egoryIdLis t | Json | Query | 否 | [1001,1002,1003] | 模型分类ID列表，用于指定一组模型分类的唯一标识符，常用于筛选或关联多个模型分类场景。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -clusterVpcList | List | null | 集群VPC列表。 |
| - modelCategor yIds | List | -1 | 模型分类ID列表，[-1]表示无分类。 |
| - modelMountLi st | Array | [] | 在线服务挂载的模型库列表。 |
| --modelId | String | md-xxxx | 模型ID。 |
| --modelName | String | Qwen2.5-0.5B | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /models | 模型挂载路径。 |
| --pvcName | String | pvc-storage-xxxx | PVC名称。 |
| -- dataAccInstan ce | String | da-**** | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |
| - storageMountL ist | Array | [] | 在线服务挂载的持久化存储列表。 |
| -- storageSource | Integer | 1 | 存储来源类型。 |
| --storagePath | String | /data/storage | 存储路径。 |
| --mountPath | String | /models | 模型挂载路径。 |
| --pvcName | String | pvc-storage-xxxx | PVC名称。 |
| - aspeedCRDCo nfigList | Array | [] | Aspeed CRD配置信息列表。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --serviceId | String | os-0573****04b94 | 服务ID。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |
| --instanceType | String | prefill-decode | 实例类型（如prefill-decode/ep-common）。 |
| --modelRole | String | PrefillNode | 模型角色。枚举值：PrefillNode、 DecodeNode、EPNode。 |
| --cpuCount | Integer | 8 | CPU核心数。 |
| --memCount | Integer | 16 | 内存大小，单位GB。 |
| --gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -- gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| --imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| --imageName | String | vllm-inference | 镜像名称（扩展字段）。 |
| -- imageIdAndVe rsion | String | img-public- b003****905b7a, 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像ID和版本（扩展字段）。 |
| --imageType | Integer | 1 | 镜像类型（扩展字段）。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型（扩展字段）。 |
| -- sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |
| -- instanceCount | Integer | 1 | 该类型实例数量。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- replicasCount | Integer | 1 | 推理子节点副本数。 |
| --quotaId | String | rq-394c****04499 | 配额ID。 |
| --quotaName | String | 默认资源组 | 配额名称（扩展字段）。 |
| -- startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| --apiPort | String | 8080 | 容器端口。 |
| -- featureConfig | String | null | 特性配置JSON字符串。 |
| -- gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -- gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| -- gpuCountUnit | Integer | 1 | GPU数量单位。 |
| -- gpuMemTotal Unit | Integer | 10 | GPU显存总量单位。 |
| -- serviceRoleTy pe | String | engine | 服务角色类型。枚举值： - engine ：引擎节点 - proxy ：路由节点 - prefiller ：预填充节点 - decoder ：解码节点。 |
| --command | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 主节点启动命令。 |
| -- workerComma nd | String | null | Worker节点启动命令，开启条件：1、 serviceDeployMode为分布式/PD分离；2、 instanceCount>=2。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| --enableEP | Boolean | false | 是否开启EP（Expert Parallelism）。 |
|---|---|---|---|
| -- enableKVCach e | Boolean | false | 是否开启KVCache。 |
| - ddpRoleInstan ceConfig | Array | [] | DDP角色实例配置列表。 |
| --serviceId | String | os-0573****04b94 | 服务ID。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |
| --instanceType | String | prefill-decode | 实例类型（如prefill-decode/ep-common）。 |
| --modelRole | String | PrefillNode | 模型角色。枚举值：PrefillNode、 DecodeNode、EPNode。 |
| --cpuCount | Integer | 8 | CPU核心数。 |
| --memCount | Integer | 16 | 内存大小，单位GB。 |
| --gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -- gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| --imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| --imageName | String | vllm-inference | 镜像名称（扩展字段）。 |
| -- imageIdAndVe rsion | String | img-public- b003****905b7a, 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像ID和版本（扩展字段）。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --imageType | Integer | 1 | 镜像类型（扩展字段）。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型（扩展字段）。 |
| -- sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |
| -- instanceCount | Integer | 1 | 该类型实例数量。 |
| -- replicasCount | Integer | 1 | 推理子节点副本数。 |
| --quotaId | String | rq-394c****04499 | 配额ID。 |
| --quotaName | String | 默认资源组 | 配额名称（扩展字段）。 |
| -- startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| --apiPort | String | 8080 | 容器端口。 |
| -- featureConfig | String | null | 特性配置JSON字符串。 |
| -- gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -- gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| -- gpuCountUnit | Integer | 1 | GPU数量单位。 |
| -- gpuMemTotal Unit | Integer | 10 | GPU显存总量单位。 |
| - inferenceRunti meConfigList | Array | [] | M-LoRA推理运行时配置列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- hyperparamet erConfig | Array | [] | 超参数配置列表。 |
| ---code | String | temperature | 超参数编码。 |
| ---name | String | 温度 | 超参数名称。 |
| ---type | String | float | 超参数类型。 |
| ---value | String | 0.7 | 超参数当前值。 |
| ---custom | Boolean | false | 是否为自定义超参数。 |
| ---description | String | 控制生成文本的随机性 | 超参数描述。 |
| ---defaultValue | String | 1.0 | 超参数默认值。 |
| --loraConfig | Array | [] | LoRA配置列表。 |
| --- modelVersion | String | v1.0 | LoRA模型版本。 |
| ---modelId | String | md-xxxx****xxxx | LoRA模型ID。 |
| ---modelType | String | lora | 模型类型。 |
| ---mountPath | String | /models/lora | LoRA模型挂载路径。 |
| --- loraModuleNa me | String | lora-adapter-1 | LoRA模块名称。 |
| --- loraDescriptio n | String | 中文对话微调适配器 | LoRA描述信息。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |
| -gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| -aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -failedMsg | String | Pod启动失败：镜像拉取超时 | 在线服务失败时的错误信息。 |
| -serviceId | String | os-0573****04b94 | 服务ID。 |
| -haType | Integer | 0 | 高可用类型。 |
| -serviceName | String | test-H100-vllm | 在线服务名称。 |
| - servedModelN ame | String | Qwen2.5-0.5B | 对外提供服务的模型名称。 |
| - serviceDeploy Mode | String | customer | 服务部署模式。枚举值： - customer ：Custom deployment（自定义部署） - aspeed ：High-performance deployment（高性能部署） - DisaggregatingEP ：aistudio High performance DisaggregatingEP（分离式EP 高性能部署） - Disaggregating ：aistudio DDP Disaggregating（DDP分离式部署） - ExpertParallelism ：Expert Parallelism mode（专家并行模式） - json ：Standalone deployment（单机部署）。 |
| -serviceDesc | String | test | 在线服务描述信息。 |
| -serviceStatus | Integer | 2 | 在线服务状态。枚举值： - 0 ：STARTING（启动中） - 1 ：RUNNING（运行中） - 2 ：STOP（已停止） - 3 ：FAILED（失败） - 4 ：WAITING FOR STARTING（待启 _ _ 动） - 5 ：SCALING（变配中） - 6 ：STOPPING（停止中）。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -imageName | String | vllm-inference | 镜像名称。 |
| -imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| -imageType | Integer | 1 | 镜像类型。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| -quotaId | String | rq-394c****04499 | 配额ID。 |
| -quotaName | String | 默认资源组 | 配额名称。 |
| - startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| -cpuCount | Integer | 8 | CPU核心数。 |
| -memCount | Integer | 16 | 内存大小，单位GB。 |
| - sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |
| - gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| - gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| -gpuCountUnit | Integer | 1 | GPU数量单位。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - gpuMemTotal Unit | Integer | 10 | GPU显存总量单位。 |
| - instanceCount | Integer | 1 | 该类型实例数量。 |
| -replicasCount | Integer | 1 | 推理子节点副本数。 |
| -totalCount | Integer | 10 | 总实例数量。 |
| - serviceAddres s | String | null | 在线服务的访问地址。 |
| -servicePort | String | 80 | 在线服务对外暴露的端口。 |
| -apiPort | String | 8080 | 容器端口。 |
| -accessType | Boolean | inference sync vpc _ _ | 推理服务访问类型。枚举值： - inference sync vpc ：同步VPC网络 _ _ - inference sync classic ：同步经典 _ _ 网络 - inference sync nodeport ：同步 _ _ NodePort网络 - inference async vpc req ：异步VPC _ _ _ 请求 - inference async vpc resp ：异步 _ _ _ VPC查询 - inference async classic req ：异 _ _ _ 步经典网络请求 - inference async classic resp ：异 _ _ _ 步经典网络查询 - inference async nodeport req ：异 _ _ _ 步NodePort请求 - inference async nodeport resp ： _ _ _ 异步NodePort查询。 |
| -rdmaSwitch | Boolean | false | RDMA开关是否开启（已废弃，仅兼容老数据）。 |
| -docId | String | doc-**** | 关联的文档ID。 |
| -gpuType | Integer | 1 | GPU型号类型（由业务逻辑填充）。 |
| -aliyunSubUid | String | 261080****688733 | 阿里云子账号UID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - serviceGroupU id | String | sg-**** | 在线服务所属服务组ID。 |
| - serviceGroupN ame | String | test | 在线服务所属服务组名称。 |
| - resourcePoolId | String | rp-***** | 资源池ID。 |
| -clusterIp | String | 104.23.xx.xx | 集群内部IP地址。 |
| -clusterId | String | sfi9s8fsnvsa98r2 | 集群ID。 |
| - apikeyPermissi on | Boolean | false | 是否具有API Key权限，默认为false。 |
| -instanceCost | Struct | {} | 在线服务的实例资源消耗统计信息。 |
| --runningCost | Float | 0.00 | 运行中实例的费用。 |
| --runningPod | Float | 1 | 运行中的Pod数量。 |
| --runningCpu | Float | 8 | 运行中实例的CPU核心数。 |
| --runningMem | Float | 16 | 运行中实例的内存大小，单位GB。 |
| --runningGpu | Float | 1 | 运行中实例的GPU卡数。 |
| -- runningGpuMe m | Float | 0 | 运行中实例的GPU显存大小，单位GB。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 1 | 总Pod数量。 |
| --totalCpu | Float | 8 | 总CPU核心数。 |
| --totalMem | Float | 16 | 总内存大小，单位GB。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --totalGpu | Float | 1 | 总GPU卡数。 |
| --totalGpuMem | Float | 0 | 总GPU显存大小，单位GB。 |
| -deployType | Struct | {} | 部署类型配置信息。 |
| --framework | String | deployment | 框架类型，默认为deployment。 |
| --open | Boolean | false | 是否开启网关，默认为false。 |
| --rdmaSwitch | Boolean | false | RDMA开关是否开启（已废弃，仅兼容老数据）。 |
| --serviceConfig | Struct | {} | 服务任务配置，包含环境等配置。 |
| ---envs | Array | [] | 环境变量列表。 |
| ----code | String | temperature | 超参数编码。 |
| ----value | String | 0.7 | 超参数当前值。 |
| --- componentEnv s | Array | null | 套件使用的环境变量列表。 |
| ----code | String | temperature | 超参数编码。 |
| ----value | String | 0.7 | 超参数当前值。 |
| - aiGatewayInfo | Struct | {} | AI网关调用信息。 |
| --sourceType | Integer | 1 | 数据来源。枚举值： - 1 ：在线服务 - 2 ：在线服务组。 |
| --open | Boolean | false | 是否开启网关，默认为false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 10 | 总实例数量（由业务逻辑计算填充）。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 在线服务的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "storageMountList":[
    {
     "mountPath":"/models",
     "pvcName":"pvc-storage-xxxx",
     "storagePath":"/data/storage",
     "storageSource":1
    }
```

`],`

```json
   "gmtCreated":"2026-02-02T03:53:49Z",
```

`"failedMsg":"Pod`启动失败：镜像拉取超时`",`

```json
   "modelMountList":[
    {
     "modelName":"Qwen2.5-0.5B",
     "dataAccInstance":"da-****",
     "weightType":0,
     "mountPath":"/models",
```

智能体工厂 OpenTrek

```json
     "modelId":"md-xxxx",
     "pvcName":"pvc-storage-xxxx",
     "modelVersion":"v1.0",
     "modelType":0
    }
```

`],`

```json
   "apikeyPermission":false,
   "ddpRoleInstanceConfig":[
    {
```

`"quotaName":"`默认资源组`",`

```json
     "sharedMemCount":1,
     "modelRole":"PrefillNode",
     "featureConfig":"null",
     "serviceId":"os-0573****04b94",
     "gpuCount":1,
     "imageType":1,
     "cpuCount":8,
     "memCount":16,
     "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
     "imageId":"img-public-b003****905b7a",
     "imageName":"vllm-inference",
     "gpuMemCount":0,
     "instanceType":"prefill-decode",
     "serviceInstanceId":"osi-xxxx****xxxx",
     "replicasCount":1,
     "quotaId":"rq-394c****04499",
     "gpuMemTotal":80,
     "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --por
t 8080 --model /model/ --served_model_name Qwen2.5-0.5B",
     "gpuLabelCount":0,
     "imageIdAndVersion":"img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ub
untu22.04-lws",
     "apiPort":"8080",
     "gpuMemTotalUnit":10,
     "instanceCount":1,
     "gpuCountUnit":1,
     "imageAccelerationType":0
    }
```

`],`

```json
   "sharedMemCount":1,
   "imageType":1,
   "gpuCount":1,
   "cpuCount":8,
   "memCount":16,
   "imageId":"img-public-b003****905b7a",
   "imageName":"vllm-inference",
   "haType":0,
   "instanceCost":[
    {
     "runningPod":1.0,
     "runningMem":16.0,
     "runningGpuMem":0.0,
     "totalCpu":8.0,
     "totalPod":1.0,
"ttlM "160
```

智能体工厂 OpenTrek

```json
     "totalMem":16.0,
     "runningGpu":1.0,
     "totalGpuMem":0.0,
     "runningCost":0.0,
     "runningCpu":8.0,
     "totalCost":0.0,
     "totalGpu":1.0
    }
```

`],`

```json
   "quotaId":"rq-394c****04499",
   "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port
8080 --model /model/ --served_model_name Qwen2.5-0.5B",
   "gpuLabelCount":0,
   "serviceGroupUid":"sg-****",
   "resourcePoolId":"rp-*****",
   "clusterIp":"104.23.xx.xx",
   "gmtModified":"2026-02-02T23:47:38Z",
```

`"quotaName":"`默认资源组`",`

```json
   "aliyunUid":"198226****521225",
   "inferenceRuntimeConfigList":[
    {
     "loraConfig":[
      {
       "mountPath":"/models/lora",
       "modelId":"md-xxxx****xxxx",
       "modelVersion":"v1.0",
```

`"loraDescription":"`中文对话微调适配器`",`

```json
       "modelType":"lora",
       "loraModuleName":"lora-adapter-1"
      }
```

`],`

```json
     "hyperparameterConfig":[
      {
       "code":"temperature",
       "defaultValue":"1.0",
       "custom":false,
```

`"name":"`温度`",` `"description":"`控制生成文本的随机性`",`

```json
       "type":"float",
       "value":"0.7"
      }
```

`],`

```json
     "serviceInstanceId":"osi-xxxx****xxxx"
    }
```

`],`

```json
   "docId":"doc-****",
   "clusterId":"sfi9s8fsnvsa98r2",
   "totalCount":10,
   "aiGatewayInfo":[
    {
     "sourceType":1,
     "open":false
    }
```

`],`

```json
"accessType":false
```

智能体工厂 OpenTrek

```json
   accessType:false,
   "servedModelName":"Qwen2.5-0.5B",
   "serviceStatus":2,
   "servicePort":"80",
   "serviceId":"os-0573****04b94",
   "clusterVpcList":"null",
   "aliyunSubUid":"261080****688733",
   "gpuType":1,
   "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
   "serviceDesc":"test",
   "gpuMemCount":0,
   "modelCategoryIds":-1,
   "serviceGroupName":"test",
   "aspeedCRDConfigList":[
    {
```

`"quotaName":"`默认资源组`",`

```json
     "enableEP":false,
     "sharedMemCount":1,
     "serviceRoleType":"engine",
     "modelRole":"PrefillNode",
     "featureConfig":"null",
     "serviceId":"os-0573****04b94",
     "gpuCount":1,
     "imageType":1,
     "cpuCount":8,
     "memCount":16,
     "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
     "imageId":"img-public-b003****905b7a",
     "imageName":"vllm-inference",
     "gpuMemCount":0,
     "instanceType":"prefill-decode",
     "enableKVCache":false,
     "serviceInstanceId":"osi-xxxx****xxxx",
     "replicasCount":1,
     "quotaId":"rq-394c****04499",
     "gpuMemTotal":80,
     "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --por
t 8080 --model /model/ --served_model_name Qwen2.5-0.5B",
     "gpuLabelCount":0,
     "command":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 808
0 --model /model/ --served_model_name Qwen2.5-0.5B",
     "imageIdAndVersion":"img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ub
untu22.04-lws",
     "workerCommand":"null",
     "apiPort":"8080",
     "gpuMemTotalUnit":10,
     "instanceCount":1,
     "gpuCountUnit":1,
     "imageAccelerationType":0
    }
```

`],`

```json
   "replicasCount":1,
   "serviceAddress":"null",
   "serviceDeployMode":"customer",
   "gpuMemTotal":80,
```

智能体工厂 OpenTrek

```json
gpue ota :80,
   "serviceName":"test-H100-vllm",
   "deployType":[
    {
     "framework":"deployment",
     "rdmaSwitch":false,
     "serviceConfig":[
      {
       "componentEnvs":[
        {
         "code":"temperature",
         "value":"0.7"
        }
```

`],`

```json
       "envs":[
        {
         "code":"temperature",
         "value":"0.7"
        }
```

]

```
      }
```

`],`

```json
     "open":false
    }
```

`],`

```json
   "apiPort":"8080",
   "regionId":"cn-neimeng-236e-d01",
   "gpuMemTotalUnit":10,
   "instanceCount":1,
   "rdmaSwitch":false,
   "gpuCountUnit":1,
   "imageAccelerationType":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":10
}
```

`XML` 格式

```xml
<data>
 <storageMountList>
  <mountPath>/models</mountPath>
  <pvcName>pvc-storage-xxxx</pvcName>
  <storagePath>/data/storage</storagePath>
  <storageSource>1</storageSource>
 </storageMountList>
 <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
```

`<failedMsg>Pod`启动失败：镜像拉取超时`</failedMsg>` 智能体工厂 OpenTrek `<failedMsg>Pod`启动失败：镜像拉取超时`</failedMsg>`

```xml
 <modelMountList>
  <modelName>Qwen2.5-0.5B</modelName>
  <dataAccInstance>da-****</dataAccInstance>
  <weightType>0</weightType>
  <mountPath>/models</mountPath>
  <modelId>md-xxxx</modelId>
  <pvcName>pvc-storage-xxxx</pvcName>
  <modelVersion>v1.0</modelVersion>
  <modelType>0</modelType>
 </modelMountList>
 <apikeyPermission>false</apikeyPermission>
 <ddpRoleInstanceConfig>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
  <sharedMemCount>1</sharedMemCount>
  <modelRole>PrefillNode</modelRole>
  <featureConfig>null</featureConfig>
  <serviceId>os-0573****04b94</serviceId>
  <gpuCount>1</gpuCount>
  <imageType>1</imageType>
  <cpuCount>8</cpuCount>
  <memCount>16</memCount>
  <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
  <imageId>img-public-b003****905b7a</imageId>
  <imageName>vllm-inference</imageName>
  <gpuMemCount>0</gpuMemCount>
  <instanceType>prefill-decode</instanceType>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
  <replicasCount>1</replicasCount>
  <quotaId>rq-394c****04499</quotaId>
  <gpuMemTotal>80</gpuMemTotal>
  <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 808
0 --model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
  <gpuLabelCount>0</gpuLabelCount>
  <imageIdAndVersion>img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubuntu2
2.04-lws</imageIdAndVersion>
  <apiPort>8080</apiPort>
  <gpuMemTotalUnit>10</gpuMemTotalUnit>
  <instanceCount>1</instanceCount>
  <gpuCountUnit>1</gpuCountUnit>
  <imageAccelerationType>0</imageAccelerationType>
 </ddpRoleInstanceConfig>
 <sharedMemCount>1</sharedMemCount>
 <imageType>1</imageType>
 <gpuCount>1</gpuCount>
 <cpuCount>8</cpuCount>
 <memCount>16</memCount>
 <imageId>img-public-b003****905b7a</imageId>
 <imageName>vllm-inference</imageName>
 <haType>0</haType>
 <instanceCost>
  <runningPod>1</runningPod>
  <runningMem>16</runningMem>
  <runningGpuMem>0</runningGpuMem>
<totalCpu>8</totalCpu>
```

智能体工厂 OpenTrek

```xml
  <totalCpu>8</totalCpu>
  <totalPod>1</totalPod>
  <totalMem>16</totalMem>
  <runningGpu>1</runningGpu>
  <totalGpuMem>0</totalGpuMem>
  <runningCost>0</runningCost>
  <runningCpu>8</runningCpu>
  <totalCost>0</totalCost>
  <totalGpu>1</totalGpu>
 </instanceCost>
 <quotaId>rq-394c****04499</quotaId>
 <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080
--model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
 <gpuLabelCount>0</gpuLabelCount>
 <serviceGroupUid>sg-****</serviceGroupUid>
 <resourcePoolId>rp-*****</resourcePoolId>
 <clusterIp>104.23.xx.xx</clusterIp>
 <gmtModified>2026-02-02T23:47:38Z</gmtModified>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
 <aliyunUid>198226****521225</aliyunUid>
 <inferenceRuntimeConfigList>
  <loraConfig>
   <mountPath>/models/lora</mountPath>
   <modelId>md-xxxx****xxxx</modelId>
   <modelVersion>v1.0</modelVersion>
```

`<loraDescription>`中文对话微调适配器`</loraDescription>`

```xml
   <modelType>lora</modelType>
   <loraModuleName>lora-adapter-1</loraModuleName>
  </loraConfig>
  <hyperparameterConfig>
   <code>temperature</code>
   <defaultValue>1.0</defaultValue>
   <custom>false</custom>
   <name>温度</name>
```

`<description>`控制生成文本的随机性`</description>`

```xml
   <type>float</type>
   <value>0.7</value>
  </hyperparameterConfig>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
 </inferenceRuntimeConfigList>
 <docId>doc-****</docId>
 <clusterId>sfi9s8fsnvsa98r2</clusterId>
 <totalCount>10</totalCount>
 <aiGatewayInfo>
  <sourceType>1</sourceType>
  <open>false</open>
 </aiGatewayInfo>
 <accessType>false</accessType>
 <servedModelName>Qwen2.5-0.5B</servedModelName>
 <serviceStatus>2</serviceStatus>
 <servicePort>80</servicePort>
 <serviceId>os-0573****04b94</serviceId>
 <clusterVpcList>null</clusterVpcList>
 <aliyunSubUid>261080****688733</aliyunSubUid>
 <gpuType>1</gpuType>
```

智能体工厂 OpenTrek `gp` `yp` `gp` `yp`

```xml
 <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
 <serviceDesc>test</serviceDesc>
 <gpuMemCount>0</gpuMemCount>
 <modelCategoryIds>-1</modelCategoryIds>
 <serviceGroupName>test</serviceGroupName>
 <aspeedCRDConfigList>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
  <enableEP>false</enableEP>
  <sharedMemCount>1</sharedMemCount>
  <serviceRoleType>engine</serviceRoleType>
  <modelRole>PrefillNode</modelRole>
  <featureConfig>null</featureConfig>
  <serviceId>os-0573****04b94</serviceId>
  <gpuCount>1</gpuCount>
  <imageType>1</imageType>
  <cpuCount>8</cpuCount>
  <memCount>16</memCount>
  <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
  <imageId>img-public-b003****905b7a</imageId>
  <imageName>vllm-inference</imageName>
  <gpuMemCount>0</gpuMemCount>
  <instanceType>prefill-decode</instanceType>
  <enableKVCache>false</enableKVCache>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
  <replicasCount>1</replicasCount>
  <quotaId>rq-394c****04499</quotaId>
  <gpuMemTotal>80</gpuMemTotal>
  <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 808
0 --model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
  <gpuLabelCount>0</gpuLabelCount>
  <command>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --m
odel /model/ --served_model_name Qwen2.5-0.5B</command>
  <imageIdAndVersion>img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubuntu2
2.04-lws</imageIdAndVersion>
  <workerCommand>null</workerCommand>
  <apiPort>8080</apiPort>
  <gpuMemTotalUnit>10</gpuMemTotalUnit>
  <instanceCount>1</instanceCount>
  <gpuCountUnit>1</gpuCountUnit>
  <imageAccelerationType>0</imageAccelerationType>
 </aspeedCRDConfigList>
 <replicasCount>1</replicasCount>
 <serviceAddress>null</serviceAddress>
 <serviceDeployMode>customer</serviceDeployMode>
 <gpuMemTotal>80</gpuMemTotal>
 <serviceName>test-H100-vllm</serviceName>
 <deployType>
  <framework>deployment</framework>
  <rdmaSwitch>false</rdmaSwitch>
  <serviceConfig>
   <componentEnvs>
    <code>temperature</code>
    <value>0.7</value>
   </componentEnvs>
```

智能体工厂 OpenTrek

```xml
   <envs>
    <code>temperature</code>
    <value>0.7</value>
   </envs>
  </serviceConfig>
  <open>false</open>
 </deployType>
 <apiPort>8080</apiPort>
 <regionId>cn-neimeng-236e-d01</regionId>
 <gpuMemTotalUnit>10</gpuMemTotalUnit>
 <instanceCount>1</instanceCount>
 <rdmaSwitch>false</rdmaSwitch>
 <gpuCountUnit>1</gpuCountUnit>
 <imageAccelerationType>0</imageAccelerationType>
</data> <pageIndex>1</pageIndex> <success>true</success> <dynamicMessages>[]</dynamicMessages> <errorMessage /> <errorCode>500</errorCode> <pageSize>10</pageSize> <httpCode>200</httpCode> <totalCount>10</totalCount>
```

##### GetOnlineService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -clusterVpcList | List | ["vpc-****"] | 集群VPC列表。 |
| - modelCategor yIds | List | 1 | 模型分类ID列表，[-1]表示无分类。 |
| - modelMountLi st | Array | [] | 在线服务挂载的模型库列表。 |
| --modelId | String | md-xxxx****xxxx | 模型ID。 |
| --modelName | String | Qwen2.5-0.5B | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /models | 挂载路径。 |
| --pvcName | String | pvc-storage-xxxx | PVC名称。 |
| -- dataAccInstan ce | String | da-****** | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - storageMountL ist | Array | [] | 在线服务挂载的持久化存储列表。 |
| -- storageSource | Integer | 1 | 存储来源类型。 |
| --storagePath | String | /data/storage | 存储路径。 |
| --mountPath | String | /models | 挂载路径。 |
| --pvcName | String | pvc-storage-xxxx | PVC名称。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| --gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| --aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| --regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| --storageId | String | ts-xxxx****xxxx | 第三方存储ID。 |
| --occupantId | String | os-0573****04b94 | 关联的资源ID（在线服务、notebook等）。 |
| -- storageSubPat h | String | /data/models | 存储子路径。 |
| --mountPath | String | /models | 挂载路径。 |
| - aspeedCRDCo nfigList | Array | [] | Aspeed CRD配置信息列表。 |
| --serviceId | String | os-0573****04b94 | 服务ID。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --instanceType | String | prefill-decode | 实例类型（如prefill-decode/ep-common）。 |
| --modelRole | String | PrefillNode | 模型角色。枚举值：PrefillNode、 DecodeNode、EPNode。 |
| --cpuCount | Integer | 8 | CPU核心数。 |
| --memCount | Integer | 16 | 内存大小，单位GB。 |
| --gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -- gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| --imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| --imageName | String | vllm-inference | 镜像名称。 |
| -- imageIdAndVe rsion | String | img-public- b003****905b7a, 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像ID和版本。 |
| --imageType | Integer | 1 | 镜像类型。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| -- sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |
| -- instanceCount | Integer | 1 | 该类型实例数量。 |
| -- replicasCount | Integer | 1 | 推理子节点副本数。 |
| --quotaId | String | rq-394c****04499 | 配额ID。 |
| --quotaName | String | 默认资源组 | 配额名称。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -- startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| --apiPort | String | 8080 | 容器端口。 |
| -- featureConfig | String | "" | 特性配置JSON字符串。 |
| -- gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -- gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| -- gpuCountUnit | Integer | 1 | GPU数量单位。 |
| -- gpuMemTotal Unit | Integer | 10 | GPU显存总量单位。 |
| -- serviceRoleTy pe | String | engine | 服务角色类型。枚举值： - engine ：引擎节点 - proxy ：路由节点 - prefiller ：预填充节点 - decoder ：解码节点。 |
| --command | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 主节点启动命令。 |
| -- workerComma nd | String | "" | Worker节点启动命令，开启条件：1、 serviceDeployMode为分布式/PD分离；2、 instanceCount>=2。 |
| --enableEP | Boolean | false | 是否开启EP（Expert Parallelism）。 |
| -- enableKVCach e | Boolean | false | 是否开启KVCache。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ddpRoleInstan ceConfig | Array | [] | DDP角色实例配置列表。 |
| --serviceId | String | os-0573****04b94 | 服务ID。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |
| --instanceType | String | prefill-decode | 实例类型（如prefill-decode/ep-common）。 |
| --modelRole | String | PrefillNode | 模型角色。枚举值：PrefillNode、 DecodeNode、EPNode。 |
| --cpuCount | Integer | 8 | CPU核心数。 |
| --memCount | Integer | 16 | 内存大小，单位GB。 |
| --gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -- gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| --imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| --imageName | String | vllm-inference | 镜像名称。 |
| -- imageIdAndVe rsion | String | img-public- b003****905b7a, 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像ID和版本。 |
| --imageType | Integer | 1 | 镜像类型。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| -- sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- instanceCount | Integer | 1 | 该类型实例数量。 |
| -- replicasCount | Integer | 1 | 推理子节点副本数。 |
| --quotaId | String | rq-394c****04499 | 配额ID。 |
| --quotaName | String | 默认资源组 | 配额名称。 |
| -- startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| --apiPort | String | 8080 | 容器端口。 |
| -- featureConfig | String | "" | 特性配置JSON字符串。 |
| -- gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -- gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| -- gpuCountUnit | Integer | 1 | GPU数量单位。 |
| -- gpuMemTotal Unit | Integer | 10 | GPU显存总量单位。 |
| - inferenceRunti meConfigList | Array | [] | 推理运行时配置列表。 |
| -- hyperparamet erConfig | Array | [] | 超参数配置列表。 |
| ---code | String | max-context-len | 超参数Code。 |
| ---name | String | 最大上下文长度 | 超参数名称。 |
| ---type | String | float | 超参数类型。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---value | String | 0.7 | 超参数当前值。 |
| ---custom | Boolean | false | 是否为自定义超参数。 |
| ---description | String | test | 代码集描述。 |
| ---defaultValue | String | 1.0 | 超参数默认值。 |
| --loraConfig | Array | [] | LoRA配置列表。 |
| --- loraModuleSou rceType | Integer | 0 | LoRA模型来源： 0：模型库 1：持久化存储 |
| --- modelVersion | String | v1.0 | LoRA模型版本。 |
| ---modelId | String | md-lora- xxxx****xxxx | LoRA模型ID。 |
| ---modelType | String | lora | 模型类型。 |
| ---mountPath | String | /models/lora | LoRA模型挂载路径。 |
| --- loraModuleNa me | String | lora-adapter-1 | LoRA模块名称。 |
| --- loraDescriptio n | String | 中文对话微调适配器 | LoRA描述信息。 |
| --- storageSource | String | 1 | LoRA模型存储类型，取值范围： 0：LOCAL。 1：OSS。 |
| ---storagePath | String | oss://******/ | LoRA模型存储路径。 |
| --loraLoadInfo | Array | [] | LoRA动态配置信息。 |
| ---loraConfigId | String | osla-12345 | LoRA配置ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- loraModuleSou rce | Integer | 0 | LoRA配置来源： 0：模型库。 1：持久化存储。 |
| --- loraModuleNa me | String | lora-adapter-1 | LoRA模块名称。 |
| ---mountPath | String | /models/lora | LoRA模型挂载路径。 |
| --- loraModuleCur rentStatus | String | ENABLE | LoRA模型当前状态。 |
| --- loraModuleTar getStatus | String | DISABEL | LoRA模型目标状态。 |
| --- statusMessage | String | null | 网关状态处于异常状态下的错误信息。 |
| ---sourceInfo | Struct | {} | LoRA模型来源信息。 |
| ---- modelVersion | String | v1 | 模型仓库版本号。 |
| ----modelId | String | md-123 | 模型ID。 |
| ---- storageSource | String | 1 | 存储类型，取值范围： 0：LOCAL。 1：OSS。 |
| ----storagePath | String | oss://******/ | 存储路径。 |
| -- serviceInstanc eId | String | osi-xxxx****xxxx | 服务实例ID。 |
| -gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| -gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| -aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -failedMsg | String | Pod启动失败：镜像拉取超时 | 在线服务失败时的错误信息。 |
| -serviceId | String | os-0573****04b94 | 服务ID。 |
| -haType | Integer | 0 | 高可用类型。 |
| -serviceName | String | test-H100-vllm | 在线服务名称。 |
| - servedModelN ame | String | Qwen2.5-0.5B | 对外提供服务的模型名称。 |
| - serviceDeploy Mode | String | customer | 服务部署模式。枚举值： - customer ：Custom deployment（自定义部署） - aspeed ：High-performance deployment（高性能部署） - DisaggregatingEP ：aistudio High performance DisaggregatingEP（分离式EP 高性能部署） - Disaggregating ：aistudio DDP Disaggregating（DDP分离式部署） - ExpertParallelism ：Expert Parallelism mode（专家并行模式） - json ：Standalone deployment（单机部署）。 |
| -serviceDesc | String | test | 在线服务描述信息。 |
| -serviceStatus | Integer | 2 | 在线服务状态。枚举值： - 0 ：STARTING（启动中） - 1 ：RUNNING（运行中） - 2 ：STOP（已停止） - 3 ：FAILED（失败） - 4 ：WAITING FOR STARTING（待启 _ _ 动） - 5 ：SCALING（变配中） - 6 ：STOPPING（停止中）。 |
| -imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -imageName | String | vllm-inference | 镜像名称。 |
| -imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageType | Integer | 1 | 镜像类型。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| -quotaId | String | rq-394c****04499 | 配额ID。 |
| -quotaName | String | 默认资源组 | 配额名称。 |
| - startCommand | String | python3 -m vllm.entrypoints.op enai.api server -- _ host 0.0.0.0 --port 8080 --model /model/ -- served model nam _ _ e Qwen2.5-0.5B | 启动命令。 |
| -cpuCount | Integer | 8 | CPU核心数。 |
| -memCount | Integer | 16 | 内存大小，单位GB。 |
| - sharedMemCo unt | Integer | 1 | 共享内存大小，单位GB。 |
| - gpuMemCount | Integer | 0 | GPU显存数量，默认为0。 |
| - gpuLabelCoun t | Integer | 0 | 显存标签数量，默认为0。 |
| -gpuCount | Integer | 1 | 显卡数量，默认为0。 |
| -gpuMemTotal | Integer | 80 | 显存大小，单位GB，默认为0。 |
| -gpuCountUnit | Integer | 1 | GPU数量单位。 |
| - gpuMemTotal Unit | Integer | 1 | GPU显存总量单位。 |
| - instanceCount | Integer | 1 | 该类型实例数量。 |
| -replicasCount | Integer | 1 | 推理子节点副本数。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -totalCount | Integer | 10 | 总实例数量（由业务逻辑计算填充）。 |
| - serviceAddres s | String | "" | 在线服务的地址。 |
| -servicePort | String | 80 | 在线服务对外暴露的端口。 |
| -apiPort | String | 8080 | 容器端口。 |
| -accessType | Boolean | inference sync vpc _ _ | 推理服务访问类型。枚举值： - inference sync vpc ：同步VPC网络 _ _ - inference sync classic ：同步经典 _ _ 网络 - inference sync nodeport ：同步 _ _ NodePort网络 - inference async vpc req ：异步VPC _ _ _ 请求 - inference async vpc resp ：异步 _ _ _ VPC查询 - inference async classic req ：异 _ _ _ 步经典网络请求 - inference async classic resp ：异 _ _ _ 步经典网络查询 - inference async nodeport req ：异 _ _ _ 步NodePort请求 - inference async nodeport resp ： _ _ _ 异步NodePort查询。 |
| -rdmaSwitch | Boolean | false | RDMA开关是否开启（已废弃，仅兼容老数据）。 |
| -endpoint | String | http:://***** | 在线服务的访问地址。 |
| -docId | String | doc-***** | 关联的文档ID。 |
| -gpuType | Integer | 1 | GPU型号类型（由业务逻辑填充）。 |
| -aliyunSubUid | String | 261080****688733 | 阿里云子账号UID。 |
| -aiProxyApikey | String | sk-******* | 模型API Key。 |
| - serviceGroupU id | String | osg-******** | 在线服务所属服务组ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - serviceGroupN ame | String | test | 在线服务所属服务组名称。 |
| - resourcePoolId | String | rp-******* | 资源池ID。 |
| -clusterIp | String | c3283**********sa hd | 集群ID。 |
| -clusterId | String | c3283**********sa hd | 集群ID。 |
| - apikeyPermissi on | Boolean | false | 是否具有API Key权限，默认为false。 |
| -instanceCost | Struct | [] | 在线服务的实例资源消耗统计信息。 |
| --runningCost | Float | 0.00 | 运行中实例的费用。 |
| --runningPod | Float | 1 | 运行中的Pod数量。 |
| --runningCpu | Float | 8 | 运行中实例的CPU核心数。 |
| --runningMem | Float | 16 | 运行中实例的内存大小，单位GB。 |
| --runningGpu | Float | 1 | 运行中实例的GPU卡数。 |
| -- runningGpuMe m | Float | 0 | 运行中实例的GPU显存大小，单位GB。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 1 | 总Pod数量。 |
| --totalCpu | Float | 8 | 总CPU核心数。 |
| --totalMem | Float | 16 | 总内存大小，单位GB。 |
| --totalGpu | Float | 1 | 总GPU卡数。 |
| --totalGpuMem | Float | 0 | 总GPU显存大小，单位GB。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -deployType | Struct | [] | 部署类型配置信息。 |
| --framework | String | deployment | 框架类型，默认为deployment。 |
| --open | Boolean | false | 是否开启网关，默认为false。 |
| --rdmaSwitch | Boolean | false | RDMA开关是否开启（已废弃，仅兼容老数据）。 |
| --serviceConfig | Struct | {} | 服务任务配置，包含环境等配置。 |
| ---envs | Array | [] | 环境变量列表。 |
| ----code | String | test | 参数Code。 |
| ----value | String | 0.7 | 超参数当前值。 |
| --- componentEnv s | Array | {} | 套件使用的环境变量列表。 |
| ----code | String | test | 参数Code。 |
| ----value | String | 0.7 | 超参数当前值。 |
| -asyncService | Struct | [] | 异步推理服务信息。 |
| --gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| --gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| --aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| --regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| --imageId | String | img-public- b003****905b7a | 镜像ID。 |
| -- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- asyncServiceId | String | as-xxxx****xxxx | 异步服务唯一标识ID。 |
| -- asyncServiceN ame | String | async-inference- service | 异步服务名称。 |
| --occupantId | String | os-0573****04b94 | 关联的资源ID（在线服务、notebook等）。 |
| --middlewareId | String | mw-xxxx****xxxx | 中间件唯一标识ID。 |
| --cpuCount | Integer | 8 | CPU核心数。 |
| --memCount | Integer | 16 | 内存大小，单位GB。 |
| -- instanceCount | Integer | 1 | 该类型实例数量。 |
| --storageUrl | String | /mnt/data/async | 持久化存储地址。 |
| -- middlewareMe taInfo | Struct | {} | 中间件元信息。 |
| ---gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| ---gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| ---aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| ---regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| --- middlewareId | String | mw-xxxx****xxxx | 中间件唯一标识ID。 |
| --- middlewareTy pe | String | kafka | 中间件类型。 |
| --- middlewareIns tanceId | String | kafka-xxxx****xxxx | Kafka实例ID。 |
| ---inputTopic | String | async-input-topic | Kafka输入Topic。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---outputTopic | String | async-output-topic | Kafka输出Topic。 |
| ---authUser | String | admin | Kafka用户名。 |
| ---servers | String | 10.0.0.1:9092 | Kafka Broker地址。 |
| - aiGatewayInfo | Struct | [] | AI网关调用信息。 |
| -- aiGatewayList | Array | [] | 调用信息列表。 |
| ---gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| ---gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| ---aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| ---regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| ---gatewayUid | String | gw-xxxx****xxxx | 网关唯一标识ID。 |
| --- gwInstanceId | String | gw-inst- xxxx****xxxx | 网关实例ID。 |
| --- resourcePoolUi d | String | rp-xxxx****xxxx | 资源池ID。 |
| --- domainName | String | inference.example. com | 网关域名。 |
| ---slbIp | String | 10.0.0.1 | SLB地址，higress网关服务关联的SLB地址。 |
| ---slbIpType | String | vpc | SLB地址类型。枚举值： - vpc ：VPC类型 - classic ：经典网络类型。 |
| --- ingressClassN ame | String | higress | Ingress类型。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- gatewayStatus | String | DEPLOY SUCCEED _ ED | 网关状态。枚举值： - PENDING ：Pending - DEPLOYING ：Deploying - DEPLOY SUCCEEDED ：Deployment _ succeeded - DEPLOY FAILED ：Deployment failed _ - WAIT UPDATE ：Wait update _ - UPDATEING ：Updating - UPDATE SUCCEEDED ：Update _ succeeded - UPDATE FAILED ：Update failed _ - WAIT UNDEPLOY ：Wait undeploy _ - UNDEPLOYING ：Undeploying - UNDEPLOY SUCCEEDED ： _ Undeployment succeeded - UNDEPLOY FAILED ：Undeployment _ failed。 |
| --- statusMessage | String | "" | 网关状态处于异常状态下的错误信息。 |
| --- occupantReso urceId | String | os-0573****04b94 | 网关绑定的资源实体ID（推理服务等）。 |
| ---accessType | String | inference sync vpc _ _ | 推理服务访问类型。枚举值： - inference sync vpc ：同步VPC网络 _ _ - inference sync classic ：同步经典 _ _ 网络 - inference sync nodeport ：同步 _ _ NodePort网络 - inference async vpc req ：异步VPC _ _ _ 请求 - inference async vpc resp ：异步 _ _ _ VPC查询 - inference async classic req ：异 _ _ _ 步经典网络请求 - inference async classic resp ：异 _ _ _ 步经典网络查询 - inference async nodeport req ：异 _ _ _ 步NodePort请求 - inference async nodeport resp ： _ _ _ 异步NodePort查询。 |
| ---description | String | test | 代码集描述。 |
| --gwInstanceId | String | gw-inst- xxxx****xxxx | 网关实例ID。 |
| --gwName | String | null | 网关实例名称。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --sourceType | Integer | 1 | 数据来源。枚举值： - 1 ：在线服务 - 2 ：在线服务组。 |
| --open | Boolean | false | 是否开启网关，默认为false。 |
| - componentDet ail | Struct | {} | 关联的套件详情（可选）。 |
| -- componentDat asetFormats | List | null | 套件数据集格式列表。 |
| -- componentPar ams | Array | [] | 套件参数列表。 |
| ---code | String | max-context-len | 超参数Code。 |
| ---name | String | 最大上下文长度 | 超参数名称。 |
| ---type | String | float | 超参数类型。 |
| ---description | String | test | 代码集描述。 |
| ---value | String | 0.7 | 超参数当前值。 |
| ---defaultValue | String | 1.0 | 超参数默认值。 |
| ---unit | String | K | 超参数单位。 |
| ---custom | Boolean | false | 是否为自定义超参数。 |
| -- componentRes ourceSpecs | Array | [] | 套件资源规格列表。 |
| ---code | String | max-context-len | 超参数Code。 |
| --- resourceType | String | spec | 资源类型。 |
| ---name | String | 最大上下文长度 | 超参数名称。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---memory | String | 16Gi | 内存大小。 |
| ---cpu | Float | 4 | CPU核数。 |
| ---instance | Integer | 1 | 实例数量。 |
| ---gpu | Float | 1 | GPU个数。 |
| ---gpuType | String | NVIDIA Ampere ** _ _ *** | GPU型号类型。 |
| ---shmSize | String | 64 | 共享内存大小。 |
| ---shmSizeUnit | String | GB | 共享内存大小单位。 |
| ---vGPU | Boolean | false | 是否开启GPU虚拟化。 |
| ---gpuMemory | String | 8192 | 显卡内存大小，单位为MB。 |
| -- componentApi s | Array | [] | 套件API列表。 |
| --- componentApi | String | {} | 套件Api信息。 |
| -- componentMet as | Array | [] | 套件元数据列表。 |
| ---code | String | max-context-len | 超参数Code。 |
| ---name | String | 最大上下文长度 | 超参数名称。 |
| ---type | String | float | 超参数类型。 |
| ---defaultValue | String | 1.0 | 超参数默认值。 |
| ---unit | String | K | 超参数单位。 |
| --regionId | String | cn-neimeng-**** | 地域ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --componentId | String | comp- xxxx****xxxx | 套件ID。 |
| -- componentNa me | String | vllm-component | 套件名称。 |
| -- componentDe scription | String | vLLM推理套件 | 套件描述。 |
| -- componentTyp e | String | inference | 套件类型。 |
| -- componentSu bType | String | llm | 套件子类型。 |
| -- componentCat egoryId | String | cat-xxxx****xxxx | 套件分类ID。 |
| -- componentEnt ry | String | main.py | 套件入口。 |
| -- componentLab els | Map | {} | 套件标签。 |
| -- componentCus tomService | Map | {} | 套件自定义服务配置。 |
| --image | Struct | [] | 套件使用的镜像版本信息。 |
| ---id | Integer | 1 | id。 |
| ---gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| ---gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| ---isDeleted | Boolean | 0 | 是否删除。 |
| ---aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| ---regionId | String | cn-neimeng-236e- d01 | 地域ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- imageVersionI d | String | v1.0 | 镜像版本ID。 |
| ---imageId | String | img-public- b003****905b7a | 镜像ID。 |
| --- imageVersion | String | 0.11.0-torch2.8- ***12.8.1-py312- ubuntu22.04-lws | 镜像版本。 |
| --- imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| --- imageNamesp ace | String | test | ACR镜像命名空间。 |
| ---imageRepo | String | test | 镜像仓库。 |
| --- imageRepoTag | String | v1 | 镜像仓库标签。 |
| --- imageAddress | String | cr- ee.registry.${regio n}.& {domain}/****/**** | 镜像地址。 |
| ---imageSize | String | 27107966 | 镜像大小。 |
| ---versionDesc | String | test | 描述信息。 |
| ---imageStatus | Integer | 1 | 镜像状态。 |
| --- imageSource | Integer | 0 | 镜像来源。 |
| ---quotaId | String | rq-394c****04499 | 配额ID。 |
| ---imageDigest | String | 5b046e2de8c4908 19125193ee2eb71 a66f2cc16c032dcd 8b69ead4be1024* *** | 镜像摘要。 |
| --codeRepo | Struct | {} | 套件关联的代码仓库信息。 |
| ---id | Integer | 1 | id。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---gmtCreated | String | 2026-02- 02T03:53:49Z | 创建时间。 |
| ---gmtModified | String | 2026-02- 02T23:47:38Z | 修改时间。 |
| ---isDeleted | Boolean | 0 | 是否删除。 |
| ---aliyunUid | String | 198226****521225 | 阿里云主账号UID。 |
| ---regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| ---codeRepoId | String | cd- 96a5060c0a95704 04f09a8f0747**** | 代码集ID。 |
| --- codeRepoNam e | String | repo | 代码集名称。 |
| ---description | String | test | 代码集描述。 |
| --- codeRepoPath | String | oss://****/**** | 代码集路径。 |
| --- codeRepoSize | String | 1000 | 代码集大小。 |
| --- codeRepoType | Integer | 1 | 代码仓库类型。 |
| -- componentMul tiEntry | Struct | {} | 套件多入口配置。 |
| ---proxyEntry | String | python3 | Proxy 服务入口命令。 |
| ---prefillEntry | String | python3 | Prefill 阶段服务入口命令。 |
| ---decodeEntry | String | python3 | Decode 阶段服务入口命令。 |
| -- componentInp uts | Struct | {} | 套件输入配置。 |
| ---artifacts | Array | [] | 制品列表。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----code | String | test | 参数Code。 |
| ----name | String | test | 参数名称。 |
| ----type | String | float | 参数类型。 |
| ----mountPath | String | /models | 挂载路径。 |
| -- componentOut puts | Struct | {} | 套件输出配置。 |
| ---artifacts | Array | [] | 制品列表。 |
| ----code | String | test | 参数Code。 |
| ----name | String | test | 参数名称。 |
| ----type | String | float | 参数类型。 |
| ----mountPath | String | /models | 挂载路径。 |

**示例**

请求示例

```
&serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "asyncService":{
   "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
   "middlewareId":"mw-xxxx****xxxx",
   "memCount":16,
   "gmtModified":"2026-02-02T23:47:38Z",
   "imageId":"img-public-b003****905b7a",
   "gmtCreated":"2026-02-02T03:53:49Z",
   "aliyunUid":"198226****521225",
   "middlewareMetaInfo":{
    "middlewareId":"mw-xxxx****xxxx",
```

智能体工厂 OpenTrek

```json
    "outputTopic":"async-output-topic",
    "gmtModified":"2026-02-02T23:47:38Z",
    "servers":"10.0.0.1:9092",
    "gmtCreated":"2026-02-02T03:53:49Z",
    "aliyunUid":"198226****521225",
    "regionId":"cn-neimeng-236e-d01",
    "middlewareType":"kafka",
    "middlewareInstanceId":"kafka-xxxx****xxxx",
    "inputTopic":"async-input-topic",
    "authUser":"admin"
   },
   "asyncServiceId":"as-xxxx****xxxx",
   "regionId":"cn-neimeng-236e-d01",
   "instanceCount":1,
   "asyncServiceName":"async-inference-service",
   "occupantId":"os-0573****04b94",
   "storageUrl":"/mnt/data/async",
   "cpuCount":8
  },
  "storageMountList":[
   {
    "mountPath":"/models",
    "pvcName":"pvc-storage-xxxx",
    "storagePath":"/data/storage",
    "storageSource":1
   }
```

`],`

```json
  "gmtCreated":"2026-02-02T03:53:49Z",
```

`"failedMsg":"Pod`启动失败：镜像拉取超时`",`

```json
  "modelMountList":[
   {
    "modelName":"Qwen2.5-0.5B",
    "dataAccInstance":"da-******",
    "weightType":0,
    "mountPath":"/models",
    "modelId":"md-xxxx****xxxx",
    "pvcName":"pvc-storage-xxxx",
    "modelVersion":"v1.0",
    "modelType":0
   }
```

`],`

```json
  "thirdpartyStorageMountList":[
   {
    "gmtModified":"2026-02-02T23:47:38Z",
    "mountPath":"/models",
    "storageSubPath":"/data/models",
    "gmtCreated":"2026-02-02T03:53:49Z",
    "aliyunUid":"198226****521225",
    "regionId":"cn-neimeng-236e-d01",
    "occupantId":"os-0573****04b94",
    "storageId":"ts-xxxx****xxxx"
   }
```

`],`

```json
  "apikeyPermission":false,
```

智能体工厂 OpenTrek

```json
  "ddpRoleInstanceConfig":[
   {
```

`"quotaName":"`默认资源组`",`

```json
    "sharedMemCount":1,
    "modelRole":"PrefillNode",
    "featureConfig":"\"\"",
    "serviceId":"os-0573****04b94",
    "gpuCount":1,
    "imageType":1,
    "cpuCount":8,
    "memCount":16,
    "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
    "imageId":"img-public-b003****905b7a",
    "imageName":"vllm-inference",
    "gpuMemCount":0,
    "instanceType":"prefill-decode",
    "serviceInstanceId":"osi-xxxx****xxxx",
    "replicasCount":1,
    "quotaId":"rq-394c****04499",
    "gpuMemTotal":80,
    "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port
8080 --model /model/ --served_model_name Qwen2.5-0.5B",
    "gpuLabelCount":0,
    "imageIdAndVersion":"img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubu
ntu22.04-lws",
    "apiPort":"8080",
    "gpuMemTotalUnit":10,
    "instanceCount":1,
    "gpuCountUnit":1,
    "imageAccelerationType":0
   }
```

`],`

```json
  "sharedMemCount":1,
  "imageType":1,
  "gpuCount":1,
  "cpuCount":8,
  "memCount":16,
  "imageId":"img-public-b003****905b7a",
  "imageName":"vllm-inference",
  "componentDetail":{
   "componentParams":[
    {
     "unit":"K",
     "code":"max-context-len",
     "defaultValue":"1.0",
     "custom":false,
```

`"name":"`最大上下文长度`",`

```json
     "description":"test",
     "type":"float",
     "value":"0.7"
    }
```

`],`

```json
   "componentType":"inference",
   "componentInputs":{
```

"

```
tif t"[
```

智能体工厂 OpenTrek

```json
    "artifacts":[
     {
      "mountPath":"/models",
      "code":"test",
      "name":"test",
      "type":"float"
     }
```

]

```json
   },
   "componentId":"comp-xxxx****xxxx",
   "componentMultiEntry":{
    "decodeEntry":"python3",
    "proxyEntry":"python3",
    "prefillEntry":"python3"
   },
   "componentSubType":"llm",
   "image":{
    "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
    "gmtModified":"2026-02-02T23:47:38Z",
    "versionDesc":"test",
    "imageId":"img-public-b003****905b7a",
    "imageNamespace":"test",
    "gmtCreated":"2026-02-02T03:53:49Z",
    "aliyunUid":"198226****521225",
    "imageRepo":"test",
    "quotaId":"rq-394c****04499",
    "imageRepoTag":"v1",
    "imageStatus":1,
    "imageDigest":"5b046e2de8c490819125193ee2eb71a66f2cc16c032dcd8b69ead4be1024****",
    "imageSource":0,
    "isDeleted":false,
    "regionId":"cn-neimeng-236e-d01",
    "imageAddress":"cr-ee.registry.${region}.&{domain}/****/****",
    "imageVersionId":"v1.0",
    "id":1,
    "imageSize":"27107966",
    "imageAccelerationType":0
   },
   "componentResourceSpecs":[
    {
     "vGPU":false,
     "gpuMemory":"8192",
     "shmSizeUnit":"GB",
     "shmSize":"64",
     "code":"max-context-len",
     "memory":"16Gi",
     "instance":1,
```

`"name":"`最大上下文长度`",`

```json
     "cpu":4.0,
     "gpu":1.0,
     "resourceType":"spec",
     "gpuType":"NVIDIA_Ampere_*****"
    }
```

`],`

```json
"componentDescription":"vLLM推理套件"
```

智能体工厂 OpenTrek

```json
   componentDescription:vLLM推理套件,
   "componentEntry":"main.py",
   "componentCategoryId":"cat-xxxx****xxxx",
   "codeRepo":{
    "gmtModified":"2026-02-02T23:47:38Z",
    "isDeleted":false,
    "codeRepoSize":"1000",
    "gmtCreated":"2026-02-02T03:53:49Z",
    "aliyunUid":"198226****521225",
    "regionId":"cn-neimeng-236e-d01",
    "codeRepoId":"cd-96a5060c0a9570404f09a8f0747****",
    "codeRepoPath":"oss://****/****",
    "codeRepoName":"repo",
    "description":"test",
    "id":1,
    "codeRepoType":1
   },
   "componentApis":[
    {
     "componentApi":"{}"
    }
```

`],`

```json
   "componentMetas":[
    {
     "unit":"K",
     "code":"max-context-len",
     "defaultValue":"1.0",
```

`"name":"`最大上下文长度`",`

```json
     "type":"float"
    }
```

`],`

```json
   "componentCustomService":{},
   "regionId":"cn-neimeng-****",
   "componentDatasetFormats":null,
   "componentName":"vllm-component",
   "componentLabels":{},
   "componentOutputs":{
    "artifacts":[
     {
      "mountPath":"/models",
      "code":"test",
      "name":"test",
      "type":"float"
     }
```

]

```json
   }
  },
  "haType":0,
  "instanceCost":{
   "runningPod":1.0,
   "runningMem":16.0,
   "runningGpuMem":0.0,
   "totalCpu":8.0,
   "totalPod":1.0,
   "totalMem":16.0,
```

智能体工厂 OpenTrek

```
tota
```

e

```json
:6.0,
   "runningGpu":1.0,
   "totalGpuMem":0.0,
   "runningCost":0.0,
   "runningCpu":8.0,
   "totalCost":0.0,
   "totalGpu":1.0
  },
  "quotaId":"rq-394c****04499",
  "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8
080 --model /model/ --served_model_name Qwen2.5-0.5B",
  "gpuLabelCount":0,
  "serviceGroupUid":"osg-********",
  "resourcePoolId":"rp-*******",
  "clusterIp":"c3283**********sahd",
  "gmtModified":"2026-02-02T23:47:38Z",
```

`"quotaName":"`默认资源组`",`

```json
  "aliyunUid":"198226****521225",
  "inferenceRuntimeConfigList":[
   {
    "loraConfig":[
     {
      "loraModuleSourceType":0,
      "mountPath":"/models/lora",
      "modelId":"md-lora-xxxx****xxxx",
      "modelVersion":"v1.0",
```

`"loraDescription":"`中文对话微调适配器`",`

```json
      "storagePath":"oss://******/",
      "modelType":"lora",
      "loraModuleName":"lora-adapter-1",
      "storageSource":"1"
     }
```

`],`

```json
    "hyperparameterConfig":[
     {
      "code":"max-context-len",
      "defaultValue":"1.0",
      "custom":false,
```

`"name":"`最大上下文长度`",`

```json
      "description":"test",
      "type":"float",
      "value":"0.7"
     }
```

`],`

```json
    "serviceInstanceId":"osi-xxxx****xxxx",
    "loraLoadInfo":[
     {
      "loraModuleCurrentStatus":"ENABLE",
      "mountPath":"/models/lora",
      "loraModuleSource":0,
      "loraModuleTargetStatus":"DISABEL",
      "sourceInfo":[
       {
        "modelId":"md-123",
        "modelVersion":"v1",
```

智能体工厂 OpenTrek

```json
        "storagePath":"oss://******/",
        "storageSource":"1"
       }
```

`],`

```json
      "loraConfigId":"osla-12345",
      "loraModuleName":"lora-adapter-1",
      "statusMessage":"null"
     }
```

]

```
   }
```

`],`

```json
  "docId":"doc-*****",
  "aiProxyApikey":"sk-*******",
  "clusterId":"c3283**********sahd",
  "totalCount":10,
  "aiGatewayInfo":{
   "sourceType":1,
   "aiGatewayList":[
    {
     "gmtModified":"2026-02-02T23:47:38Z",
     "occupantResourceId":"os-0573****04b94",
     "gmtCreated":"2026-02-02T03:53:49Z",
     "aliyunUid":"198226****521225",
     "slbIpType":"vpc",
     "description":"test",
     "resourcePoolUid":"rp-xxxx****xxxx",
     "statusMessage":"\"\"",
     "accessType":"inference_sync_vpc",
     "ingressClassName":"higress",
     "gatewayUid":"gw-xxxx****xxxx",
     "regionId":"cn-neimeng-236e-d01",
     "domainName":"inference.example.com",
     "slbIp":"10.0.0.1",
     "gwInstanceId":"gw-inst-xxxx****xxxx",
     "gatewayStatus":"DEPLOY_SUCCEEDED"
    }
```

`],`

```json
   "gwInstanceId":"gw-inst-xxxx****xxxx",
   "gwName":"",
   "open":false
  },
  "accessType":false,
  "servedModelName":"Qwen2.5-0.5B",
  "endpoint":"http:://*****",
  "serviceStatus":2,
  "servicePort":"80",
  "serviceId":"os-0573****04b94",
  "clusterVpcList":"[\"vpc-****\"]",
  "aliyunSubUid":"261080****688733",
  "gpuType":1,
  "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
  "serviceDesc":"test",
  "gpuMemCount":0,
  "modelCategoryIds":1,
```

智能体工厂 OpenTrek

```json
  "serviceGroupName":"test",
  "aspeedCRDConfigList":[
   {
```

`"quotaName":"`默认资源组`",`

```json
    "enableEP":false,
    "sharedMemCount":1,
    "serviceRoleType":"engine",
    "modelRole":"PrefillNode",
    "featureConfig":"\"\"",
    "serviceId":"os-0573****04b94",
    "gpuCount":1,
    "imageType":1,
    "cpuCount":8,
    "memCount":16,
    "imageVersion":"0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws",
    "imageId":"img-public-b003****905b7a",
    "imageName":"vllm-inference",
    "gpuMemCount":0,
    "instanceType":"prefill-decode",
    "enableKVCache":false,
    "serviceInstanceId":"osi-xxxx****xxxx",
    "replicasCount":1,
    "quotaId":"rq-394c****04499",
    "gpuMemTotal":80,
    "startCommand":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port
8080 --model /model/ --served_model_name Qwen2.5-0.5B",
    "gpuLabelCount":0,
    "command":"python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080
--model /model/ --served_model_name Qwen2.5-0.5B",
    "imageIdAndVersion":"img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubu
ntu22.04-lws",
    "workerCommand":"\"\"",
    "apiPort":"8080",
    "gpuMemTotalUnit":10,
    "instanceCount":1,
    "gpuCountUnit":1,
    "imageAccelerationType":0
   }
```

`],`

```json
  "replicasCount":1,
  "serviceAddress":"",
  "serviceDeployMode":"customer",
  "gpuMemTotal":80,
  "serviceName":"test-H100-vllm",
  "deployType":{
   "framework":"deployment",
   "rdmaSwitch":false,
   "serviceConfig":{
    "componentEnvs":[
     {
      "code":"test",
      "value":"0.7"
     }
```

`],` 智能体工厂 OpenTrek

```json
    "envs":[
     {
      "code":"test",
      "value":"0.7"
     }
```

]

```json
   },
   "open":false
  },
  "apiPort":"8080",
  "regionId":"cn-neimeng-236e-d01",
  "gpuMemTotalUnit":1,
  "instanceCount":1,
  "rdmaSwitch":false,
  "gpuCountUnit":1,
  "imageAccelerationType":0
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

`XML` 格式

```xml
<data>
 <asyncService>
  <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
  <middlewareId>mw-xxxx****xxxx</middlewareId>
  <memCount>16</memCount>
  <gmtModified>2026-02-02T23:47:38Z</gmtModified>
  <imageId>img-public-b003****905b7a</imageId>
  <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
  <aliyunUid>198226****521225</aliyunUid>
  <middlewareMetaInfo>
   <middlewareId>mw-xxxx****xxxx</middlewareId>
   <outputTopic>async-output-topic</outputTopic>
   <gmtModified>2026-02-02T23:47:38Z</gmtModified>
   <servers>10.0.0.1:9092</servers>
   <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
   <aliyunUid>198226****521225</aliyunUid>
   <regionId>cn-neimeng-236e-d01</regionId>
   <middlewareType>kafka</middlewareType>
   <middlewareInstanceId>kafka-xxxx****xxxx</middlewareInstanceId>
   <inputTopic>async-input-topic</inputTopic>
   <authUser>admin</authUser>
  </middlewareMetaInfo>
  <asyncServiceId>as-xxxx****xxxx</asyncServiceId>
  <regionId>cn-neimeng-236e-d01</regionId>
  <instanceCount>1</instanceCount>
  <asyncServiceName>async-inference-service</asyncServiceName>
  <occupantId>os-0573****04b94</occupantId>
  <storageUrl>/mnt/data/async</storageUrl>
```

智能体工厂 OpenTrek

```xml
  <cpuCount>8</cpuCount>
 </asyncService>
 <storageMountList>
  <mountPath>/models</mountPath>
  <pvcName>pvc-storage-xxxx</pvcName>
  <storagePath>/data/storage</storagePath>
  <storageSource>1</storageSource>
 </storageMountList>
 <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
```

`<failedMsg>Pod`启动失败：镜像拉取超时`</failedMsg>`

```xml
 <modelMountList>
  <modelName>Qwen2.5-0.5B</modelName>
  <dataAccInstance>da-******</dataAccInstance>
  <weightType>0</weightType>
  <mountPath>/models</mountPath>
  <modelId>md-xxxx****xxxx</modelId>
  <pvcName>pvc-storage-xxxx</pvcName>
  <modelVersion>v1.0</modelVersion>
  <modelType>0</modelType>
 </modelMountList>
 <thirdpartyStorageMountList>
  <gmtModified>2026-02-02T23:47:38Z</gmtModified>
  <mountPath>/models</mountPath>
  <storageSubPath>/data/models</storageSubPath>
  <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
  <aliyunUid>198226****521225</aliyunUid>
  <regionId>cn-neimeng-236e-d01</regionId>
  <occupantId>os-0573****04b94</occupantId>
  <storageId>ts-xxxx****xxxx</storageId>
 </thirdpartyStorageMountList>
 <apikeyPermission>false</apikeyPermission>
 <ddpRoleInstanceConfig>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
  <sharedMemCount>1</sharedMemCount>
  <modelRole>PrefillNode</modelRole>
  <featureConfig>&quot;&quot;</featureConfig>
  <serviceId>os-0573****04b94</serviceId>
  <gpuCount>1</gpuCount>
  <imageType>1</imageType>
  <cpuCount>8</cpuCount>
  <memCount>16</memCount>
  <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
  <imageId>img-public-b003****905b7a</imageId>
  <imageName>vllm-inference</imageName>
  <gpuMemCount>0</gpuMemCount>
  <instanceType>prefill-decode</instanceType>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
  <replicasCount>1</replicasCount>
  <quotaId>rq-394c****04499</quotaId>
  <gpuMemTotal>80</gpuMemTotal>
  <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 808
0 --model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
  <gpuLabelCount>0</gpuLabelCount>
  <imageIdAndVersion>img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubuntu2
```

智能体工厂 OpenTrek

```xml
2.04-lws</imageIdAndVersion>
  <apiPort>8080</apiPort>
  <gpuMemTotalUnit>10</gpuMemTotalUnit>
  <instanceCount>1</instanceCount>
  <gpuCountUnit>1</gpuCountUnit>
  <imageAccelerationType>0</imageAccelerationType>
 </ddpRoleInstanceConfig>
 <sharedMemCount>1</sharedMemCount>
 <imageType>1</imageType>
 <gpuCount>1</gpuCount>
 <cpuCount>8</cpuCount>
 <memCount>16</memCount>
 <imageId>img-public-b003****905b7a</imageId>
 <imageName>vllm-inference</imageName>
 <componentDetail>
  <componentParams>
   <unit>K</unit>
   <code>max-context-len</code>
   <defaultValue>1.0</defaultValue>
   <custom>false</custom>
```

`<name>`最大上下文长度`</name>`

```xml
   <description>test</description>
   <type>float</type>
   <value>0.7</value>
  </componentParams>
  <componentType>inference</componentType>
  <componentInputs>
   <artifacts>
    <mountPath>/models</mountPath>
    <code>test</code>
    <name>test</name>
    <type>float</type>
   </artifacts>
  </componentInputs>
  <componentId>comp-xxxx****xxxx</componentId>
  <componentMultiEntry>
   <decodeEntry>python3</decodeEntry>
   <proxyEntry>python3</proxyEntry>
   <prefillEntry>python3</prefillEntry>
  </componentMultiEntry>
  <componentSubType>llm</componentSubType>
  <image>
   <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
   <gmtModified>2026-02-02T23:47:38Z</gmtModified>
   <versionDesc>test</versionDesc>
   <imageId>img-public-b003****905b7a</imageId>
   <imageNamespace>test</imageNamespace>
   <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
   <aliyunUid>198226****521225</aliyunUid>
   <imageRepo>test</imageRepo>
   <quotaId>rq-394c****04499</quotaId>
   <imageRepoTag>v1</imageRepoTag>
   <imageStatus>1</imageStatus>
   <imageDigest>5b046e2de8c490819125193ee2eb71a66f2cc16c032dcd8b69ead4be1024****</image
```

`Di` `t>` 智能体工厂 OpenTrek

```xml
Digest>
   <imageSource>0</imageSource>
   <isDeleted>false</isDeleted>
   <regionId>cn-neimeng-236e-d01</regionId>
   <imageAddress>cr-ee.registry.${region}.&amp;{domain}/****/****</imageAddress>
   <imageVersionId>v1.0</imageVersionId>
   <id>1</id>
   <imageSize>27107966</imageSize>
   <imageAccelerationType>0</imageAccelerationType>
  </image>
  <componentResourceSpecs>
   <vGPU>false</vGPU>
   <gpuMemory>8192</gpuMemory>
   <shmSizeUnit>GB</shmSizeUnit>
   <shmSize>64</shmSize>
   <code>max-context-len</code>
   <memory>16Gi</memory>
   <instance>1</instance>
```

`<name>`最大上下文长度`</name>`

```xml
   <cpu>4</cpu>
   <gpu>1</gpu>
   <resourceType>spec</resourceType>
   <gpuType>NVIDIA_Ampere_*****</gpuType>
  </componentResourceSpecs>
  <componentDescription>vLLM推理套件</componentDescription>
  <componentEntry>main.py</componentEntry>
  <componentCategoryId>cat-xxxx****xxxx</componentCategoryId>
  <codeRepo>
   <gmtModified>2026-02-02T23:47:38Z</gmtModified>
   <isDeleted>false</isDeleted>
   <codeRepoSize>1000</codeRepoSize>
   <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
   <aliyunUid>198226****521225</aliyunUid>
   <regionId>cn-neimeng-236e-d01</regionId>
   <codeRepoId>cd-96a5060c0a9570404f09a8f0747****</codeRepoId>
   <codeRepoPath>oss://****/****</codeRepoPath>
   <codeRepoName>repo</codeRepoName>
   <description>test</description>
   <id>1</id>
   <codeRepoType>1</codeRepoType>
  </codeRepo>
  <componentApis>
   <componentApi>{}</componentApi>
  </componentApis>
  <componentMetas>
   <unit>K</unit>
   <code>max-context-len</code>
   <defaultValue>1.0</defaultValue>
```

`<name>`最大上下文长度`</name>`

```xml
   <type>float</type>
  </componentMetas>
  <componentCustomService  />
  <regionId>cn-neimeng-****</regionId>
  <componentDatasetFormats  />
<componentName>vllm-component</componentName>
```

智能体工厂 OpenTrek

```xml
  <componentName>vllmcomponent</componentName>
  <componentLabels  />
  <componentOutputs>
   <artifacts>
    <mountPath>/models</mountPath>
    <code>test</code>
    <name>test</name>
    <type>float</type>
   </artifacts>
  </componentOutputs>
 </componentDetail>
 <haType>0</haType>
 <instanceCost>
  <runningPod>1</runningPod>
  <runningMem>16</runningMem>
  <runningGpuMem>0</runningGpuMem>
  <totalCpu>8</totalCpu>
  <totalPod>1</totalPod>
  <totalMem>16</totalMem>
  <runningGpu>1</runningGpu>
  <totalGpuMem>0</totalGpuMem>
  <runningCost>0</runningCost>
  <runningCpu>8</runningCpu>
  <totalCost>0</totalCost>
  <totalGpu>1</totalGpu>
 </instanceCost>
 <quotaId>rq-394c****04499</quotaId>
 <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080
--model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
 <gpuLabelCount>0</gpuLabelCount>
 <serviceGroupUid>osg-********</serviceGroupUid>
 <resourcePoolId>rp-*******</resourcePoolId>
 <clusterIp>c3283**********sahd</clusterIp>
 <gmtModified>2026-02-02T23:47:38Z</gmtModified>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
 <aliyunUid>198226****521225</aliyunUid>
 <inferenceRuntimeConfigList>
  <loraConfig>
   <loraModuleSourceType>0</loraModuleSourceType>
   <mountPath>/models/lora</mountPath>
   <modelId>md-lora-xxxx****xxxx</modelId>
   <modelVersion>v1.0</modelVersion>
```

`<loraDescription>`中文对话微调适配器`</loraDescription>`

```xml
   <storagePath>oss://******/</storagePath>
   <modelType>lora</modelType>
   <loraModuleName>lora-adapter-1</loraModuleName>
   <storageSource>1</storageSource>
  </loraConfig>
  <hyperparameterConfig>
   <code>max-context-len</code>
   <defaultValue>1.0</defaultValue>
   <custom>false</custom>
```

`<name>`最大上下文长度`</name>`

```xml
   <description>test</description>
   <type>float</type>
```

智能体工厂 OpenTrek `yp`

```xml
/yp
   <value>0.7</value>
  </hyperparameterConfig>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
  <loraLoadInfo>
   <loraModuleCurrentStatus>ENABLE</loraModuleCurrentStatus>
   <mountPath>/models/lora</mountPath>
   <loraModuleSource>0</loraModuleSource>
   <loraModuleTargetStatus>DISABEL</loraModuleTargetStatus>
   <sourceInfo>
    <modelId>md-123</modelId>
    <modelVersion>v1</modelVersion>
    <storagePath>oss://******/</storagePath>
    <storageSource>1</storageSource>
   </sourceInfo>
   <loraConfigId>osla-12345</loraConfigId>
   <loraModuleName>lora-adapter-1</loraModuleName>
   <statusMessage>null</statusMessage>
  </loraLoadInfo>
 </inferenceRuntimeConfigList>
 <docId>doc-*****</docId>
 <aiProxyApikey>sk-*******</aiProxyApikey>
 <clusterId>c3283**********sahd</clusterId>
 <totalCount>10</totalCount>
 <aiGatewayInfo>
  <sourceType>1</sourceType>
  <aiGatewayList>
   <gmtModified>2026-02-02T23:47:38Z</gmtModified>
   <occupantResourceId>os-0573****04b94</occupantResourceId>
   <gmtCreated>2026-02-02T03:53:49Z</gmtCreated>
   <aliyunUid>198226****521225</aliyunUid>
   <slbIpType>vpc</slbIpType>
   <description>test</description>
   <resourcePoolUid>rp-xxxx****xxxx</resourcePoolUid>
   <statusMessage>&quot;&quot;</statusMessage>
   <accessType>inference_sync_vpc</accessType>
   <ingressClassName>higress</ingressClassName>
   <gatewayUid>gw-xxxx****xxxx</gatewayUid>
   <regionId>cn-neimeng-236e-d01</regionId>
   <domainName>inference.example.com</domainName>
   <slbIp>10.0.0.1</slbIp>
   <gwInstanceId>gw-inst-xxxx****xxxx</gwInstanceId>
   <gatewayStatus>DEPLOY_SUCCEEDED</gatewayStatus>
  </aiGatewayList>
  <gwInstanceId>gw-inst-xxxx****xxxx</gwInstanceId>
  <gwName  />
  <open>false</open>
 </aiGatewayInfo>
 <accessType>false</accessType>
 <servedModelName>Qwen2.5-0.5B</servedModelName>
 <endpoint>http:://*****</endpoint>
 <serviceStatus>2</serviceStatus>
 <servicePort>80</servicePort>
 <serviceId>os-0573****04b94</serviceId>
 <clusterVpcList>[&quot;vpc-****&quot;]</clusterVpcList>
```

智能体工厂 OpenTrek

```xml
 <aliyunSubUid>261080****688733</aliyunSubUid>
 <gpuType>1</gpuType>
 <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
 <serviceDesc>test</serviceDesc>
 <gpuMemCount>0</gpuMemCount>
 <modelCategoryIds>1</modelCategoryIds>
 <serviceGroupName>test</serviceGroupName>
 <aspeedCRDConfigList>
```

`<quotaName>`默认资源组`</quotaName>`

```xml
  <enableEP>false</enableEP>
  <sharedMemCount>1</sharedMemCount>
  <serviceRoleType>engine</serviceRoleType>
  <modelRole>PrefillNode</modelRole>
  <featureConfig>&quot;&quot;</featureConfig>
  <serviceId>os-0573****04b94</serviceId>
  <gpuCount>1</gpuCount>
  <imageType>1</imageType>
  <cpuCount>8</cpuCount>
  <memCount>16</memCount>
  <imageVersion>0.11.0-torch2.8-***12.8.1-py312-ubuntu22.04-lws</imageVersion>
  <imageId>img-public-b003****905b7a</imageId>
  <imageName>vllm-inference</imageName>
  <gpuMemCount>0</gpuMemCount>
  <instanceType>prefill-decode</instanceType>
  <enableKVCache>false</enableKVCache>
  <serviceInstanceId>osi-xxxx****xxxx</serviceInstanceId>
  <replicasCount>1</replicasCount>
  <quotaId>rq-394c****04499</quotaId>
  <gpuMemTotal>80</gpuMemTotal>
  <startCommand>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 808
0 --model /model/ --served_model_name Qwen2.5-0.5B</startCommand>
  <gpuLabelCount>0</gpuLabelCount>
  <command>python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 --m
odel /model/ --served_model_name Qwen2.5-0.5B</command>
  <imageIdAndVersion>img-public-b003****905b7a, 0.11.0-torch2.8-***12.8.1-py312-ubuntu2
2.04-lws</imageIdAndVersion>
  <workerCommand>&quot;&quot;</workerCommand>
  <apiPort>8080</apiPort>
  <gpuMemTotalUnit>10</gpuMemTotalUnit>
  <instanceCount>1</instanceCount>
  <gpuCountUnit>1</gpuCountUnit>
  <imageAccelerationType>0</imageAccelerationType>
 </aspeedCRDConfigList>
 <replicasCount>1</replicasCount>
 <serviceAddress  />
 <serviceDeployMode>customer</serviceDeployMode>
 <gpuMemTotal>80</gpuMemTotal>
 <serviceName>test-H100-vllm</serviceName>
 <deployType>
  <framework>deployment</framework>
  <rdmaSwitch>false</rdmaSwitch>
  <serviceConfig>
   <componentEnvs>
    <code>test</code>
```

智能体工厂 OpenTrek

```xml
    <value>0.7</value>
   </componentEnvs>
   <envs>
    <code>test</code>
    <value>0.7</value>
   </envs>
  </serviceConfig>
  <open>false</open>
 </deployType>
 <apiPort>8080</apiPort>
 <regionId>cn-neimeng-236e-d01</regionId>
 <gpuMemTotalUnit>1</gpuMemTotalUnit>
 <instanceCount>1</instanceCount>
 <rdmaSwitch>false</rdmaSwitch>
 <gpuCountUnit>1</gpuCountUnit>
 <imageAccelerationType>0</imageAccelerationType>
</data> <success>true</success> <dynamicMessages>[]</dynamicMessages> <errorMessage /> <errorCode>500</errorCode> <httpCode>200</httpCode>
```

##### ModifyOnlineServiceSpec

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-spec HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- 5bceba1c05979043de08 1400ds9s9**** | 在线服务ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | CPU大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| gpuCount | Integ er | Body | 是 | 1 | GPU大小，单位为卡，该参数必填。 |

| A | I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gpuMemC ount | Integ er | Body | 否 | 0 | 显存大小，单位为GB。 |
| gpuLabelC ount | Integ er | Body | 否 | 1 | GPU虚拟化下GPU的数量。 |
| sharedMe mCount | Integ er | Body | 否 | 4 | 共享内存大小，单位为GB。 |
| instanceC ount | Integ er | Body | 是 | 1 | 实例数量，该参数必填。 |
| replicasCo unt | Integ er | Body | 否 | 1 | 在线服务副本数量。 |
| instanceS pecList | Json | Body | 否 | {} | 在线服务角色配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify-spec HTTP/1.1 { "serviceId":"os-5bceba1c05979043de081400ds9s9****", "cpuCount":"1", "memCount":"1", "gpuCount":"1", "instanceCount":"1" }
```

智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineServiceConfig

调用ModifyOnlineServiceConfig修改指定在线服务配置并重启服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/modify-online-service-config HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os-d20bd4**** | 在线服务ID，该参数必填。 |
| servedMo delName | Strin g | Body | 否 | Qwen3 | 模型服务名称。 |
| instanceC ount | Integ er | Body | 否 | 1 | 在线服务单节点实例数量。 |
| replicasCo unt | Integ er | Body | 否 | 1 | 在线服务副本数量。 |
| cpuCount | Integ er | Body | 否 | 4 | cpu大小，单位为核。 |
| memCoun t | Integ er | Body | 否 | 8 | 内存大小，单位为GB。 |
| sharedMe mCount | Integ er | Body | 否 | 4 | 共享内存大小，单位为GB。 |
| gpuMemC ount | Integ er | Query | 否 | 8 | GPU显存份数，按照切分粒度来统计，开启GPU虚拟化时需填写；例如切分粒度为 128MB, 申请显存份数为 8，即可申请1GB显存。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| gpuCount | Integ er | Body | 否 | 1 | gpu大小，单位为卡。 |
| gpuLabelC ount | Integ er | Body | 否 | 1 | 申请到的gpuMemCount显存，平均分配GPU卡数，GPU虚拟化时开启。例如申请显存为 gpuMemCount=8 ， 申请卡数为 gpuLabelCount=2 ，表示申请2张GPU卡，每张卡分配4份显存。 |
| apiPort | Strin g | Body | 是 | 8000 | API访问端口，该参数必填。 配置模型服务所在POD的 API访问端口，可通过API 访问该模型在线服务。 端口可配置范围建议在： 1000-9000。 |
| startCom mand | Strin g | Body | 是 | python3 main.py | 启动命令，该参数必填。 |
| envs | Json | Body | 否 | [ { "code": "key1", "value": "value1" }, { "code": "key2", "value": "value2" } ] | 环境变量配置。 |
| imageId | Strin g | Body | 是 | img- 66562b610952c0441e0 ba6a***** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| modelMou ntList | Json | Body | 否 | { "modelId": "md- system-f384af80******", "modelVersion": "v1.0", "mountPath": "/models/", "dataAccInstance": null } | 模型库配置。 |
| storageMo untList | Json | Body | 否 | { "mountPath": "/datas/utils/test", "storagePath": "oss://******", "storageSource": 1 } | 持久化存储设置。 |
| aspeedCR DConfigLi st | Json | Body | 否 | {} | aspeed配置。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| dynamicMessa ges | String | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

**示例**

请求示例

```json
POST /online-service/modify-online-service-config HTTP/1.1 { "serviceId":"os-d20bd4****", "apiPort":"8000", "startCommand":"python3 main.py", "imageId":"img-66562b610952c0441e0ba6a*****", "imageVersion":"v1" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateOnlineService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
POST /online-service/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| haType | Integ er | Body | 否 | 0 | 高可用类型，取值范围： 0：单可用区。 默认值：0。 |
| serviceNa me | Strin g | Body | 是 | service-name | 在线服务名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| serviceDe sc | Strin g | Body | 否 | service-desc | 在线服务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| serviceDe ployMode | Strin g | Body | 否 | customer | 服务部署模式： customer（默认），Custom deployment aspeed，High- performance deployment DisaggregatingEP，ai studio High performance DisaggregatingEP Disaggregating，aistu dio DDP Disaggregating ExpertParallelism，Ex pert Parallelism mode json，Standalone deployment |
| rdmaSwitc h | Boole an | Body | 否 | false | 是否开启rdma，取值范围： true：开启。 false：禁用。 |
| imageId | Strin g | Body | 是 | img- cf3b10300ca7c0423b08 a3e02c54**** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27f**** | 资源配额ID，该参数必填。 |
| startCom mand | Strin g | Body | 是 | python3 main.py | 启动命令，该参数必填。 1、启动的服务需要监听外部访问源的地址。比如 --host=0.0.0.0 接受任意IP请求，-- host=192.168.1.0/24 该网段的请求。 2、API访问端口需要和启动命令中端口保持一致。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| sharedMe mCount | Integ er | Body | 否 | 20 | 共享内存大小，单位为GB。 |
| gpuMemC ount | Integ er | Body | 否 | 0 | 显存大小，单位为GB。 |
| gpuCount | Integ er | Body | 是 | 0 | gpu大小，单位为卡，该参数必填。 |
| instanceC ount | Integ er | Body | 是 | 1 | 实例数量，该参数必填。 |
| replicasCo unt | Integ er | Body | 否 | 1 | 分布式部署的副本数量。 |
| servicePor t | Strin g | Body | 否 | 80 | Service端口，配置模型服务Service的访问端口，端口可配置范围：80-9000。 默认值：80。 |
| apiPort | Strin g | Body | 是 | 8080 | API访问端口，该参数必填。 配置模型服务所在POD的 API访问端口，可通过API 访问该模型在线服务。 端口可配置范围建议在： 1000-9000。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| accessTyp e | Boole an | Body | 否 | false | 是否开启经典网络访问，取值范围： true：开启。 false：关闭。 默认值：false。 |
| openStatis tic | Boole an | Body | 否 | true | 性能监控配置，取值范围： true：开启。 false：关闭。 |
| scaleConfi g | Json | Body | 否 | { "autoScale": true, "serviceId": "os- 3d8f****d04381", "scaleConfig":[], "minInstanceCount": 1, "maxInstanceCount": 2 } | 自动变配配置，可不填。 |
| aiGateway | Json | Body | 否 | { "open": true, "instanceId": "i- 08ea24a0b***" } | 网关配置。 |
| rateLimitR ule | Json | Body | 否 | { "open": true, "limitType": "query per second", _ _ "limitValue": 3 } | 限流配置。 |
| routerPoli cy | Strin g | Body | 否 | "prefix cache" _ | 网关智能路由策略名称。 |
| asyncServ ice | Json | Body | 否 | { "open": true, "middlewareType": "kafka", "middlewareMetaInfo": { "middlewareInstanceId": "clust***", "inputTopic": "kafk**", "authUser": "aistudio", "servers": "192.16**" }, "cpuCount": 2, "memCount": 4, "instanceCount": 2, "storageMountList": [ { "storagePath": "oss://pe**/code/", "mountPath": null, "pvcName": "", "storageSource": 1 } ] } | 异步配置。 |
| deployTyp e | Json | Body | 否 | { "open":true, "framework":"deployme nt", "serviceConfig":{ "rdmaEnable": true, "envs": [ "code":"code- name", "value":"code- value" ] } } | 部署类型。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loadBalan ce | Json | Body | 否 | { "type":"sessionAffinity" } | 负载均衡，取值范围： sessionAffinity： session保持。 default：轮训。 |
| contentSe curity | Json | Body | 否 | { "open": true, "occupantId": "os- fd2***", "securityServiceType": "openai proxy", _ "securityConfig": { { "checkRuleList": ["inputContent","outputC ontent"] } } } | 内容安全配置。 |
| aspeedSer vice | Json | Body | 否 | { "aspeedPerformance": { "mode": "Standard", "dryRun": false, "instanceType": "standard", "resource": [ { "role": "CommonNode", "count": 1, "gpus": 1, "cpus": 8, "memory": 16, "sharedMemory": 8 } ] } } } | 高性能服务部署。 |
| datasetMo untList | Json | Body | 否 | [{}] | 数据集配置，可不填。已删除 |
| modelMou ntList | Json | Body | 否 | [{ "modelId": "md- 7a5c75e10a95104e1d0 bd5804e0****", "mountPath": "/root/", "modelType": 1, "modelVersion": "v1", "dataAccInstance": "da- 9dsfs87s6f7s6f****" }] | 模型库配置。 |
| codeMoun tList | Json | Body | 否 | [{}] | 代码集配置，可不填。已删除 |
| storageMo untList | Json | Body | 否 | [{ "quotaId": "rq- d8890a98089c2041d80 86bb0b2e****", "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| nodeConfi gList | Json | Body | 否 | [{}] | 节点配置，可不填。已删除 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| hyperpara meterConf ig | Json | Body | 否 | [ { "code": "tensor- parallel-size", "defaultValue": "2", "name": "张量并行", "description": "张量并行, 单机多卡状态采用的卡数", "type": "INT" }, { "code": "max-model- len", "defaultValue": "32768", "name": "最大长度", "description": "模型处理的上下文长度", "type": "INT" } ] | 推理引擎配置的超参数。 推理服务中，hyperParams（超参数） 是控制大模型文本生成行为的一组可配置参数，它们不改变模型结构，但直接影响输出结果的质量、多样性、长度和风格。比如： temperature 控制输出随机性，值越高越随机，越低越确定。 |
| componen tInputs | Json | Body | 否 | [ { "mountPath": "$INPUT DIR/model", _ "code": "model", "name": "模型", "type": "model", "sourceType": "model", "modelId": "md-system-56b1f****", "modelVersion": "v1.0", "dataAccInstance": "" } ] | 推理套件输入参数，示例是输入参数中的模型定义。 包含：使用的模型、模型版本、模型挂载路径、模型关联数据加速器等。 |
| componen tOutputs | Json | Body | 否 | [ { "sourceType": "oss", "storagePath": "oss://****/****/" } ] | 推理套件输出参数，示例是输入参数中的持久化存储定义。 包含：使用的存储类型、存储地址。 |
| inference RuntimeC onfig | Json | Body | 否 | { "resource": [ { "role": "prefiller", "replicates": 1, "quotaId": "rq- 5ae8d4200*****", "instanceCount": 1, "nodeCount": 1, "cpuCount": 16, "memCount": 32, "sharedMemCount": 20, "gpuCount": 1, "vGPU": false, "gpuType": "NVIDIA ****", _ "sharedMemory": 16 }, { "role": "decoder", "replicates": 1, "quotaId": "rq- 5ae8d420*****", "instanceCount": 1, "nodeCount": 1, "cpuCount": 16, "memCount": 32, "sharedMemCount": 20, "gpuCount": 1, "vGPU": false, "gpuType": "NVIDIA ****", _ "sharedMemory": 16 }, "multiLoraData": [ { "modelVersion": "v1.0", "modelId": "md-system- f63****" } ] ] } | 推理服务运行时参数。 包含multi-lora运行时配置和 PD分离 prefill decoder 运行时参数。 PD分离调度："role"为： "prefiller"、"decoder"、 "proxy"。并分别定义了每个role使用的资源规格和资源配额。 多Lora部署：定义了多个 lora模型的Id和版本号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Body | 否 | "cp-system-qwen3- *****" | 部署推理服务使用的套件 ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "serviceId": "os- ****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service/create HTTP/1.1 { "serviceName":"service-name", "imageId":"img-cf3b10300ca7c0423b08a3e02c54****", "imageVersion":"v1", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27f****", "startCommand":"python3 main.py", "cpuCount":"1", "memCount":"1", "gpuCount":"0", "instanceCount":"1", "apiPort":"8080" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{     \"serviceId\": \"os-****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteOnlineService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
&serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineServiceStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- 5bceba1c05979043de08 1400df54**** | 在线服务ID，该参数必填。 |
| serviceSta tus | Boole an | Body | 是 | true | 在线服务状态，该参数必填，取值范围： true：重启。 false：停止。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify-status HTTP/1.1 { "serviceId":"os-5bceba1c05979043de081400df54****", "serviceStatus":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineService

调用ModifyOnlineService修改指定在线服务的部分信息，包括服务名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- 5bceba1c05979043de08 1400df546**** | 在线服务ID，该参数必填。 |
| serviceNa me | Strin g | Body | 是 | service-name | 在线服务名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| serviceDe sc | Strin g | Body | 否 | service-desc | 在线服务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify HTTP/1.1 { "serviceId":"os-5bceba1c05979043de081400df546****", "serviceName":"service-name" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineServicePortSpec

调用ModifyOnlineServicePortSpec修改指定在线服务的端口配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-port-spec HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- 123f3c61074d3046b408 be70c81**** | 在线服务ID，该参数必填。 |
| servicePor t | Strin g | Body | 否 | 80 | Service端口，配置模型服务Service的访问端口，端口可配置范围：80-9000。 |
| accessTyp e | Boole an | Body | 否 | false | 是否开启经典网络访问，取值范围： true：开启。 false：关闭。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify-port-spec HTTP/1.1 { "serviceId":"os-123f3c61074d3046b408be70c81****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetServiceHealthStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /inference-access/check-service-health HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceS erviceId | Strin g | Query | 是 | example123 | 资源服务唯一标识符，用于区分不同的资源服务类型或实例。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| engineTyp e | Strin g | Query | 否 | MySQL | 数据库类型，取值范围： MySQL ，SQLServe r ，Oracle ，Postgr eSQL ，MongoDB 等 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -fullMessage | String | error | 完整错误信息。 |
| -message | String | error | 错误信息。 |
| -result | Boolean | false | 调用结果。 |

**示例**

请求示例

```
GET /inference-access/check-service-health HTTP/1.1 &resourceServiceId=example123
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "result":false,
  "fullMessage":"error",
  "message":"error"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateSecurityScanTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /sec-scan/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Body | 是 | rq- d8890a98088086bb0b2 e27**** | 资源配额ID，该参数必填。 |
| regionId | Strin g | Body | 是 | cn-hangzhou | 地域ID，该参数必填。 |
| usePredefi nedRule | Strin g | Body | 是 | true | 表示是否使用预定义安全评测规则，该参数必填，取值范围： true：启用预定义规则。 false：不启用预定义规则。 |
| isBypass | Strin g | Body | 是 | false | 是否开启对抗攻击模式，该参数必填，取值范围： true：开启。 false：不开启。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| isScanHigr ess | Strin g | Body | 否 | true | 表示被扫描的在线服务是否启用Higress网关，取值范围： true：已启用。 false：未启用。 |
| isRiskHigr ess | Strin g | Body | 否 | true | 表示负责检测的在线服务是否启用Higress网关，取值范围： true：已启用。 false：未启用。 |
| datasetMo untList | Json | Body | 否 | [{ "datasetId": "ds- f00fef1f0ec*****", "datasetVersion": "v1" }] | 安全评测数据集挂载信息。 |
| storageMo untList | Json | Body | 是 | [{ "storageSource": 1, "storagePath": "oss://yx- test.oss-cn-wulan- env17*****e.shuguang.c om/ai-scanner/reports/" }] | 安全评测结果的持久化存储设置，该参数必填。 |
| scanModel Configs | Json | Body | 是 | [{ "serviceId": "os- 906479350*****" }] | 待扫描模型配置，传入待扫描模型在线服务的ID，该参数必填。 |
| riskCheck ModelConf igs | Json | Body | 是 | [{ "serviceId": "os- 906479350d****" }] | 安全评测模型配置，传入裁判模型在线服务的ID，该参数必填。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| scheduleT ime | Strin g | Body | 否 | 2025-04-16 00:00:00 | 定时启动时间，格式为 yyyy-MM-dd HH:mm:ss。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /sec-scan/create HTTP/1.1 { "quotaId":"rq-d8890a98088086bb0b2e27****", "regionId":"cn-hangzhou", "usePredefinedRule":"true", "isBypass":"false", "storageMountList":"[{
    "storageSource": 1,
    "storagePath": "oss://yx-test.oss-cn-wulan-env17*****e.shuguang.com/ai-
scanner/reports/" }]", "scanModelConfigs":"[{
    "serviceId": "os-906479350*****"
}]", "riskCheckModelConfigs":"[{
    "serviceId": "os-906479350d****"
}]" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListSecScanTaskByServiceId

调用ListSecScanTaskByServiceId查询目标在线服务的安全评测任务信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /sec-scan/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 10 | 安全评测任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | scaleTime | 排序字段。 默认值：scaleTime。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | ss- 5103add0062e20452c8 0383***** | 任务ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskStatus | Integ er | Query | 否 | 0 | 安全评测状态，取值范围： 0：已创建。 1：启动中。 2：运行中。 3：已停止。 4：失败。 5：完成。 |
| datasetId | Strin g | Query | 否 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |
| serviceId | Strin g | Query | 否 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | null | 动态错误消息列表；成功时通常为 null。 |
| data | Array | {} | 安全扫描任务列表。 |
| - codeMountList | Array | null | 代码挂载列表（当前接口多数场景可能为 null/[]）。 |
| --codeId | String | code-8b13fd2e | 代码仓库 ID。 |
| --codeName | String | sec-scan-rules | 代码仓库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 名称。 |
| - datasetMountL ist | Array | - | 数据集挂载列表。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- dataAccInstan ce | String | dataacc-i-011 | 数据加速实例标识。 |
| --dataType | Integer | 0 | 数据类型。 |
| -- datasetFileNa me | String | custom rules.xlsx _ | 数据文件名。 |
| --datasetId | String | ds- 11aa22bb33cc44 | 数据集 ID。 |
| --datasetName | String | security scan inpu _ _ t | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 名称。 |
| - modelMountLi st | Array | null | 模型挂载列表（当前接口多数场景可能为 null/[]）。 |
| -- dataAccInstan ce | String | dataacc-i-011 | 数据加速实例标识。 |
| --modelId | String | md-system- 7ed6f4208a44e87 8ce | 模型 ID。 |
| --modelName | String | Qwen3-4B | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 名称。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --weightType | Integer | 0 | 权重类型。 |
| - nodeConfigList | Array | null | 节点配置列表（当前接口多数场景可能为 null/[]）。 |
| --cpuCount | Integer | 1 | CPU 核数。 |
| --gpuCount | Integer | 0 | GPU 卡数。 |
| -- gpuMemCount | Integer | 0 | GPU 显存规格。 |
| --memCount | Integer | 2 | 内存规格。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --nodeType | Integer | 0 | 节点类型。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存规格。 |
| -- startCommand | String | python3 main.py | 启动命令。 |
| - storageMountL ist | Array | null | 存储挂载列表（当前接口多数场景可能为 null/[]）。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 名称。 |
| --storagePath | String | oss://aipaas- bucket/security- scan/output/ | OSS 存储路径。 |
| -- storageSource | Integer | 1 | 存储来源类型。 |
| -aliyunUid | String | 1277********1314 | 阿里云账号 UID。 |
| -failedMsg | String | null | 失败信息；失败态可能有值。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtCreated | String | 2026-03- 05T07:20:15Z | 任务创建时间（UTC）。 |
| -gmtEnd | String | 2026-03- 05T09:12:30Z | 任务结束时间（UTC）；未结束时可能为 null。 |
| -gmtModified | String | 2026-03- 05T09:10:11Z | 任务修改时间（UTC）。 |
| -isBypass | Boolean | false | 是否开启绕过模式。 |
| -isSchedule | Boolean | true | 是否定时任务；非定时任务可能为 null/false。 |
| -regionId | String | cn-wulan-env38- d01 | 地域 ID。 |
| -reportPath | String | oss://aipaas- bucket/security- scan/output/securit y report sc- _ _ 20260305- 0001.xlsx | 扫描报告路径；仅完成态且存在报告时有值。 |
| -riskServiceId | String | os-risk-001 | 风险服务 ID。 |
| -scheduleTime | String | 2026-03- 06T01:00:00Z | 调度执行时间（UTC）；非定时任务可能为 null。 |
| -subStatus | Integer | 5 | 任务子状态（ModelTaskDetailStatus）。 |
| -taskId | String | sc-20260305-0001 | 安全扫描任务 ID。 |
| -taskStatus | Integer | 5 | 任务主状态（ModelTaskStatus）。 |
| - usePredefined Rule | Boolean | true | 是否使用预置规则。 |
| -instanceCost | Struct | null | 实例成本信息（当前接口多数场景可能为 null）。 |
| --runningCost | Float | 0.00 | 运行中成本。 |
| --runningCpu | Integer | 0 | 运行中 CPU。 |
| --runningGpu | Integer | 0 | 运行中 GPU。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -- runningGpuMe m | Integer | 0 | 运行中 GPU 显存。 |
| --runningMem | Integer | 0 | 运行中内存。 |
| --runningPod | Integer | 0 | 运行中 Pod 数。 |
| --totalCost | Float | 0.00 | 累计成本。 |
| --totalCpu | Integer | 0 | 累计 CPU。 |
| --totalGpu | Integer | 0 | 累计 GPU。 |
| --totalGpuMem | Integer | 0 | 累计 GPU 显存。 |
| --totalMem | Integer | 0 | 累计内存。 |
| --totalPod | Integer | 0 | 累计 Pod 数。 |
| success | Boolean | true | 请求是否成功。 成功：true。 失败：false。 |
| errorCode | String | null | 错误码；成功时为 null。 |
| errorMessage | String | null | 错误信息；成功时为 null。 |
| httpCode | Integer | 200 | HTTP 状态码。 |
| totalCount | Integer | 12 | 总记录数。 |
| pageSize | Integer | 10 | 每页条数。 |
| pageIndex | Integer | 1 | 当前页码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
GET /sec-scan/list HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### GetASpeedTemplate

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Body | 是 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID，该参数必填。 |
| runtimeTy pe | Strin g | Body | 否 | infer-singlenode | 查询运行时模板类型。 |
| modelRep oCode | Strin g | Body | 否 | Qwen3-32B | 模型编号。 |
| modelArc hitecture | Strin g | Body | 否 | Qwen3ForCausalLM | 模型架构。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - runnerTemplat eList | Array | [{}] | 模板配置角色列表。 |
| --command | String | sleep 300 | 启动脚本。 |
| --cpu | Integer | 8 | CPU核数。 |
| --enableEP | Boolean | true | 是否开启EP部署。 |
| -- enableKVCach e | Boolean | true | 是否开启KVCache。 |
| --imageType | Integer | 0 | 镜像类型。 0：public。 1：custom。 |
| -- resourceAvaila ble | Boolean | true | 资源是否可用。 |
| --roleType | String | leader-runner | 角色类型。 |
| -- sharedMemory | String | 4 | 共享内存大小，单位GB。 |
| -- workerComma nd | String | sleep 300 | worker节点命令行。 |
| - runtimeDisabl ed | Boolean | false | 表示运行时模板是否已禁用。 |
| -runtimeName | String | infer-singlenode | 模板类型名称。 |
| -runtimeType | String | infer-singlenode | 运行时模板类型。 |
| - templateName | String | Qwen3-32B | 运行时模板名称。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -templateType | String | base | 模板类型。 base：基础模板。 special：特调模板。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "resourcePoolId":"rp-bc47fd6f0af720435c0a4d60eeba63****" }
```

正常返回示例 `JSON` 格式

```
{}
```

##### ListAPIs

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Query | 是 | os- 7dawe99aw23jnfa**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | null | 动态错误消息列表；成功时通常为 null。 |
| success | Boolean | true | 请求是否成功。 成功：true。 失败：false。 |
| errorCode | String | null | 错误码；成功时为 null。 |
| errorMessage | String | null | 错误信息；成功时为 null。 |
| httpCode | Integer | 200 | HTTP 状态码。 |
| data | Struct | - | 在线服务 API 信息。 |
| -apis | String | [{"name":"chat.co mpletions","metho d":"POST","path":"/ v1/chat/completion s"}] | API 清单字符串（JSON 字符串形式）。 |
| -domainUrl | String | https://gateway.ex ample.internal | 服务访问域名。 |
| - hasComponen t | Boolean | true | 是否关联组件（代码中可能为 true/false/null）。 |
| -headers | Struct | Content-Type: application/json | 调用示例请求头。 |
| --Accept | String | */* | 默认 Accept。 |
| --Authorization | String | ****** | 鉴权头；代码里会脱敏为 ****** 。 |
| --User-Agent | String | GenericHttpProxy/ 1.0 | 默认 User-Agent。 |

**示例**

请求示例智能体工厂 OpenTrek

```
&entityId=os-7dawe99aw23jnfa****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"-",
 "errorCode":"500",
 "httpCode":200
}
```

##### OnlineDebugging

调用OnlineDebugging实现在线调试，指在在线服务运行过程中，通过远程连接对服务进行实时请求并获取模型响应。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/debug HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| domainUrl | Strin g | Body | 是 | http://example.com | 域名，该参数必填。 |
| apiPath | Strin g | Body | 是 | /test/1 | API的请求Path，该参数必填。 |
| httpMetho d | Strin g | Body | 是 | POST | http请求方法GET,POST， 该参数必填。 |
| serviceId | Strin g | Body | 是 | os-xxx | 在线服务ID，该参数必填。 |
| headers | Json | Body | 否 | { "Authorization": "*****", "Accept": "*/*", "User-Agent": "GenericHttpProxy/1.0" } | 请求头。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| requestBo dy | Strin g | Body | 是 | { \"input\": { \"query\": \"What is a text ranking model?\", \"documents\": [ \"Text ranking models are widely used in search engines and recommendation systems, where they rank candidate texts based on text relevance.\", \"Quantum computing is a cutting-edge field in computing science.\", \"The development of pre-trained language models has brought new progress to text ranking models.\" ] }, \"parameters\": { \"top n\": 5, _ \"return documents\": _ true } }", "RegionId": "cn- wulan-env119-d01 | HTTP请求体，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
POST /online-service/debug HTTP/1.1 { "domainUrl":"http://example.com", "apiPath":"/test/1", "httpMethod":"POST", "serviceId":"os-xxx", "requestBody":"{ \"input\": { \"query\": \"What is a text ranking model?\", \"documents\": [ \"Text ranking models are widely used in search engines and recom mendation systems, where they rank candidate texts based on text relevance.\", \"Q uantum computing is a cutting-edge field in computing science.\", \"The development of pre-trained language models has brought new progress to text ranking mod els.\" ] }, \"parameters\": { \"top_n\": 5, \"return_documents\": true }}",
    "RegionId": "cn-wulan-env119-d01"
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteSecurityScanTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /sec-scan/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | ss- 5103add0062e20452c8 0383***** | 任务ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /sec-scan/delete HTTP/1.1 &taskId=ss-5103add0062e20452c80383*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### 弹性伸缩

###### ListAutoScalerRecord

调用ListAutoScalerRecord查询所有的在线服务详情-获取弹性伸缩配置记录列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /inference-service/list-autoscaler-record HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 弹性伸缩配置列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | scaleTime | 排序字段。 默认值：scaleTime。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| startTime | Strin g | Query | 否 | 2025-07- 12T07:16:48.000Z | 开始时间。 |
| endTime | Strin g | Query | 否 | 2025-07- 12T07:16:48.000Z | 结束时间。 |
| formatted Status | Integ er | Query | 否 | 0 | 伸缩状态，取值范围： 0：成功。 1：扩容中。 2：缩容中。 3：失败。 |
| scaleType | Integ er | Query | 否 | 0 | 伸缩类型，取值范围： 0：扩容。 1：缩容。 |
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -serviceId | String | os-06**********369 | 服务ID。 |
| - scaleStartTime | String | 2025-11- 18T13:31:58Z | 弹性伸缩操作开始的时间，采用UTC时区格式。 |
| -scaleEndTime | String | 2025-11- 18T13:31:59Z | 弹性伸缩操作结束的时间，采用UTC时区格式。 |
| -scaleStatus | String | SuccessfulRescale | 弹性伸缩操作的原始状态描述，来自K8s HPA的状态信息。 |
| - formattedStat us | Integer | 0 | 弹性伸缩操作的格式化状态码。枚举值如下： 0: 成功 1: 扩容中 2: 缩容中 3: 失败 |
| -scaleType | Integer | 1 | 弹性伸缩的类型码。枚举值如下： 0: 扩容（Scale Up） 1: 缩容（Scale Down） |
| - instanceCount BeforeScaling | Integer | 5 | 弹性伸缩操作前的实例数量。 |
| - instanceCount AfterScaling | Integer | 4 | 弹性伸缩操作后的实例数量。 |
| -triggerRule | String | All metrics below target | 触发弹性伸缩的规则描述，说明具体的触发条件。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| totalCount | Integer | 100 | 弹性伸缩记录的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 弹性伸缩记录的页码。 |

**示例**

请求示例

```
GET /inference-service/list-autoscaler-record HTTP/1.1 &serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

###### CreateInferenceServiceAutoScaler

调用CreateInferenceServiceAutoScaler创建推理服务弹性伸缩配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /inference-service/create-autoscale HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID，该参数必填。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| minInstan ceCount | Integ er | Body | 是 | 1 | 最小实例数，该参数必填。 |
| maxInstan ceCount | Integ er | Body | 是 | 3 | 最大实例数，该参数必填。 |
| scaleStrat egies | Json | Body | 是 | [{ "metricName": "cpu:Utilization", "threshold": 2 }] | 伸缩策略列表，该参数必填。 |
| scaleUpBe havior | Json | Body | 否 | { "upStabilizationWindowS econds": 0 } | 弹性扩容参数配置，指定从扩容指令下达开始到扩容实际生效所需的时长，如果在此期间系统检测到请求量恢复了，将会取消扩容指令。 单位为秒，默认值为0秒。 |
| scaleDow nBehavior | Json | Body | 否 | { "downStabilizationWindo wSeconds": 300 } | 弹性缩容参数配置，指定从缩容指令下达开始到缩容实际生效所需的时长，如果在此期间系统检测到请求量增加了，将会取消缩容指令。 单位为秒，默认值为300 秒。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "scaleConfigId": "isa-cfg-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /inference-service/create-autoscale HTTP/1.1 { "serviceId":"os-d20bd45d0683a047a60b5f50f8b52****", "minInstanceCount":"1", "maxInstanceCount":"3", "scaleStrategies":"[{
 "metricName": "cpu:Utilization",
 "threshold": 2
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"scaleConfigId\": \"isa-cfg-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### DeleteInferenceServiceAutoScaler

调用DeleteInferenceServiceAutoScaler删除指定的推理服务弹性伸缩。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /inference-service/delete-autoscale HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID，该参数必填 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /inference-service/delete-autoscale HTTP/1.1 &serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### GetInferenceServiceAutoScaler

调用GetInferenceServiceAutoScaler查询指定推理服务弹性伸缩配置详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /inference-service/get-autoscale HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - scaleStrategie s | Array | [] | 伸缩策略列表。 |
| --metricName | String | cpu | 具体的性能指标度量名称。 |
| --threshold | Integer | 1 | 阈值。 |
| -- averageValue | Float | 0.5 | 阈值（以平均方式）。 |
| --metricType | String | Resource | 监控项类型。 |
| -gmtCreated | String | 2025-11- 17T12:37:59Z | 自动伸缩配置的创建时间。 |
| -gmtModified | String | 2025-12- 03T12:52:47Z | 自动伸缩配置的最后修改时间。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -aliyunUid | String | 198226051452122 5 | 阿里云账号ID，标识配置所属的阿里云用户。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID，标识配置所属的阿里云地域。 |
| -serviceId | String | os- 6d8f5*********c66 | 推理服务的唯一标识符。 |
| -scaleConfigId | String | isa-cfg- 81f661c*********** **8d8a7e | 自动伸缩配置的唯一标识符。 |
| - enableAutosca le | Boolean | true | 是否启用自动伸缩功能。 |
| - minInstanceCo unt | Integer | 1 | 自动伸缩的最小实例数量。 |
| - maxInstanceC ount | Integer | 5 | 自动伸缩的最大实例数量。 |
| - currentMetric Map | Map | [] | 当前监控的指标信息。 |
| - scaleUpBehavi or | Struct | { "upStabilizationWin dowSeconds": 0 } | 弹性扩容参数配置，指定从扩容指令下达开始到扩容实际生效所需的时长，如果在此期间系统检测到请求量恢复了，将会取消扩容指令。单位为秒，默认值为0秒。 |
| -- upStabilization WindowSecon ds | Integer | 0 | 扩容指令下达开始到扩容实际生效所需的时长。 |
| - scaleDownBeh avior | Struct | { "downStabilization WindowSeconds": 300 } | 弹性缩容参数配置，指定从缩容指令下达开始到缩容实际生效所需的时长，如果在此期间系统检测到请求量增加了，将会取消缩容指令。单位为秒，默认值为300秒。 |
| -- downStabilizat ionWindowSec onds | Integer | 300 | 从缩容指令下达开始到缩容实际生效所需的时长。 |
| - onZeroBehavi or | Struct | {} | 弹性扩缩容参数配置，指定缩容为0时的策略。 |
| -- scaleDownGra cePeriodSecon ds | Integer | 600 | 缩容到0之前的等待期。 当指标满足缩容到0的条件时，需要经过等待期的时间，才会执行缩容到0。默认值为600。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -- scaleUpActivat ionReplicas | Integer | 1 | 当从0开始扩容时，一次性创建的实例数。默认值为1。 |

**示例**

请求示例

```
GET /inference-service/get-autoscale HTTP/1.1 &serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ModifyInferenceServiceAutoScaler

调用ModifyInferenceServiceAutoScaler修改推理服务弹性伸缩配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /inference-service/modify-autoscale HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID，该参数必填。 |
| minInstan ceCount | Integ er | Body | 是 | 1 | 最小实例数，该参数必填。 |
| maxInstan ceCount | Integ er | Body | 是 | 3 | 最大实例数，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| scaleStrat egies | Json | Body | 是 | [{ "metricName": "cpu:Utilization", "threshold": 2 }] | 伸缩策略列表，该参数必填。 |
| scaleUpBe havior | Json | Body | 否 | { "upStabilizationWindowS econds": 0 } | 弹性扩容参数配置，指定从扩容指令下达开始到扩容实际生效所需的时长，如果在此期间系统检测到请求量恢复了，将会取消扩容指令。 单位为秒，默认值为0秒。 |
| scaleDow nBehavior | Json | Body | 否 | { "downStabilizationWindo wSeconds": 300 } | 弹性缩容参数配置，指定从缩容指令下达开始到缩容实际生效所需的时长，如果在此期间系统检测到请求量增加了，将会取消缩容指令。 单位为秒，默认值为300 秒。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /inference-service/modify-autoscale HTTP/1.1 { "serviceId":"os-d20bd45d0683a047a60b5f50f8b52****", "minInstanceCount":"1", "maxInstanceCount":"3", "scaleStrategies":"[{
 "metricName": "cpu:Utilization",
 "threshold": 2
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### AI网关

###### CreateAIGateway

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| open | Boole an | Body | 是 | true | 是否开启权重配置，该参数必填。取值： true ：开启 |
| instanceId | Strin g | Body | 是 | i-08ea***77a98866 | 网关实例id，该参数必填。 |
| occupantI d | Strin g | Body | 是 | os-12345** | 在线服务id或者灰度组id， 该参数必填。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "open":"true", "instanceId":"i-08ea***77a98866", "occupantId":"os-12345**" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### CreateGatewayAccessLink

调用CreateGatewayAccessLink创建网关外部调用链接、开通按钮。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
POST /online-service/create-gateway-access-link HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os- 740042f20b89a033b**** | 在线服务或者服务组ID，该参数必填。 |
| accessTyp e | Strin g | Body | 是 | inference sync vpc _ _ | 网关类型，该参数必填。 同步推理: inference sync vpc _ _ inference sync clas _ _ sic 异步推理： inference asyc vpc _ _ req _ inference async vp _ _ c resp _ inference async cl _ _ assic req _ inference async cl _ _ assic resp _ |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /online-service/create-gateway-access-link HTTP/1.1 { "entityId":"os-740042f20b89a033b****", "accessType":"inference_sync_vpc" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### DeleteAIGateway

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| occupantI d | Strin g | Query | 是 | os-1234*** | 在线服务ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&occupantId=os-1234***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### GetGatewayAPIKeyLatestCallLog

调用GetGatewayAPIKeyLatestCallLog获取指定在线服务的APIKey使用信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service/get-gateway-apikey-latest-call-log HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| occupantR esourceId | Strin g | Query | 是 | os-123456 | 在线服务ID。 |
| apikeyUid | Strin g | Query | 是 | aigk-e02e****049ec | API密钥唯一标识。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 198226****1225 | 阿里云账号ID。 |
| -apikey | String | sk- xxxxxxxxxxxxxxxx | API密钥值。 |
| - apikeyLatestU seTime | String | 2025-11- 07T09:43:17Z | 最新使用时间。 |
| -apikeyType | String | internet | API密钥类型。枚举值： intranet：用作内部的模型广场等内部调用 internet：用户外部互联网调用 aiproxy：模型服务Key |
| -apikeyUid | String | aigk- e02e****049ec | API密钥唯一标识。 |
| -description | String | 这是一个测试API密钥 | 备注信息。 |
| -gmtCreate | String | 2025-10- 23T07:41:53Z | 创建时间。 |
| -gmtModified | String | 2025-10- 23T07:41:53Z | 修改时间，格式为UTC时间。 |
| -occupantId | String | os-8691****04e80 | 关联业务UID，如灰度组或在线服务。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -status | Integer | 1 | 状态。枚举值： 1：启用 0：禁用 |

**示例**

请求示例

```
GET /online-service/get-gateway-apikey-latest-call-log HTTP/1.1 &occupantResourceId=user123 &apikeyUid=1234567890abcdef
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ListGatewayAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 10 | API Key列表的页码。 默认值：1。 |

| Ope | nTrek |  |  |  | AI Studio ·API |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| occupantI d | Strin g | Query | 否 | os-123456 | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gmtCreated | String | 2024-01- 15T08:30:45Z | 创建时间，表示该APIKey记录首次创建的UTC时间戳。 |
| -gmtModified | String | 2024-01- 20T14:22:33Z | 修改时间，表示该APIKey记录最后更新的UTC时间戳。 |
| -aliyunUid | String | 123456789012345 6 | 阿里云账号ID，表示该APIKey所属的阿里云主账号唯一标识。 |
| -regionId | String | cn-beijing | 地域ID，表示该APIKey所在的地域标识，如cn- beijing、cn-hangzhou等。 |
| -apikeyUid | String | aigk- 1234567890abcdef | APIKey唯一标识符，表示该网关APIKey的全局唯一ID，用于区分不同的APIKey记录。 |
| -apikeyName | String | 我的模型APIKey | APIKey名称，表示用户为该APIKey设置的显示名称，便于识别和管理。 |
| -apikey | String | sk- xxxxxxxxxxxxxxxxx xxxxxxx | APIKey值，表示用于身份验证的密钥字符串，实际调用时需要在请求头中携带此值。 |
| -apikeyType | String | internet | APIKey类型，表示该APIKey的调用范围和用途。枚举值包括：intranet(用作内部的模型广场等内部调用，SystemKey类型)、internet(用户外部互联网调用，用户创建的APIKey)、 aiproxy(AI代理类型，用于AI代理场景)。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -occupantId | String | os-xxxxxxxx | 关联业务资源ID，表示该APIKey绑定的在线服务或在线服务组的唯一标识。 |
| -status | Integer | 1 | APIKey状态，表示该APIKey当前的启用状态。 枚举值包括：1(启用状态，APIKey可以正常使用)、0(禁用状态，APIKey暂停使用)。 |
| -description | String | 用于测试环境的 APIKey | 备注信息，表示用户为该APIKey添加的额外说明或描述信息。 |
| - totalRequestC ount | String | 1500 | 总调用次数，表示该APIKey在指定时间范围内的总请求数量。 |
| - successReque stCount | String | 1450 | 成功调用次数，表示该APIKey在指定时间范围内调用成功的请求数量。 |
| - failedRequest Count | String | 50 | 失败调用次数，表示该APIKey在指定时间范围内调用失败的请求数量。 |
| - inputTokenCo unt | String | 300000 | 输入Token数量，表示该APIKey在指定时间范围内消耗的输入Token总数。 |
| - outputTokenC ount | String | 250000 | 输出Token数量，表示该APIKey在指定时间范围内消耗的输出Token总数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 镜像版本的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 镜像版本的页码。 |

智能体工厂 OpenTrek

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "inputTokenCount":"300000",
   "gmtModified":"2024-01-20T14:22:33Z",
   "failedRequestCount":"50",
   "apikey":"sk-xxxxxxxxxxxxxxxxxxxxxxxx",
   "gmtCreated":"2024-01-15T08:30:45Z",
   "aliyunUid":"1234567890123456",
   "totalRequestCount":"1500",
   "successRequestCount":"1450",
```

`"description":"`用于测试环境的`APIKey",`

```json
   "outputTokenCount":"250000",
```

`"apikeyName":"`我的模型`APIKey",`

```json
   "regionId":"cn-beijing",
   "apikeyUid":"aigk-1234567890abcdef",
   "apikeyType":"internet",
   "occupantId":"os-xxxxxxxx",
   "status":1
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

###### ListGatewayAPIKeyStatisticDetail

调用ListGatewayAPIKeyStatisticDetail查询指定在线服务的API Key调用统计量详情信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service/list-gateway-apikey-statistic-detail HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apiKeyUid | Strin g | Query | 否 | aigk-4fb8b2*** | API Key唯一标识ID，不填返回在线服务所有API Key 在该时段内的调用统计。 |
| occupantI d | Strin g | Query | 否 | os-4821934902*** | 在线服务唯一标识ID，不填返回空数组。 |
| startTime | Strin g | Query | 否 | 1765184400 | 统计开始时间，Unix时间戳。 同时不填startTime和 endTime，endTime默认值为当前时间，startTime默认值为 endTime 30*24 小时前， endTime填了，startTime不填，startTime默认值为 endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为 startTime 30*24 小时后， 同时填了startTime和 endTime，startTime 和 endTime 间隔不超过 31 天。 |
| endTime | Strin g | Query | 否 | 1765188000 | 统计结束时间，Unix时间戳。 同时不填startTime和 endTime，endTime默认值为当前时间，startTime默认值为 endTime 30*24 小时前， endTime填了，startTime不填，startTime默认值为 endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为 startTime 30*24 小时后， 同时填了startTime和 endTime，startTime 和 endTime 间隔不超过 31 天。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | 否 | 10 | 每页条数，取值范围：1- 100。 默认值为10。 |
| nextToken | Strin g | Query | 否 | 087:00*******5600: | 数据分页标记，从标记位开始取一页数据，若不传则从头开始查询。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -apikeyUid | String | aigk-73a1a0550*** | API密钥UID。 |
| -endTime | Integer | 1765188000 | 统计结束时间，Unix时间戳。 |
| - failedRequest Count | String | 0 | 失败请求数。 |
| - inputTokenCo unt | String | 96 | 输入Token数。 |
| - outputTokenC ount | String | 14000 | 输出Token数。 |
| -requestCount | String | 8 | 请求总数。 |
| -serviceId | String | os-f6d2e***c82 | 服务ID。 |
| -startTime | Integer | 1765184400 | 统计开始时间，Unix时间戳。 |
| - successReque stCount | String | 8 | 成功请求数。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| nextToken | String | 087:0000000***88 000: | 是否拥有下一次查询的令牌（Token）。取值： 如果NextToken 为空表示没有下一次查询。 如果NextToken 有返回值，该取值表示下一次查询开始的令牌。 |

**示例**

请求示例

```
GET /online-service/list-gateway-apikey-statistic-detail HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{[]}",
 "success":"",
 "dynamicMessages":"\t[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### GetGatewayAPIKeyStatisticTotal

调用GetGatewayAPIKeyStatisticTotal查询指定在线服务API Key的调用统计量信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service/get-gateway-apikey-statistic-total HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apiKeyUid | Strin g | Query | 是 | aigk-4fb8b2*** | API Key唯一标识ID。 |
| occupantI d | Strin g | Query | 是 | os-8691****04e80 | 关联业务UID，如在线服务组或在线服务。 |
| startTime | Strin g | Query | 否 | 2025-10-12T01:14:54Z | 统计开始时间，格式为UTC 时间。 同时不填startTime 和endTime，则默认获取总的调用量，填了start time和 _ endTime，则获取指定时间段调用量， endTime填了，startTime不填，startTime默认值为endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为startTime 30*24 小时后， 同时填了startTime 和 endTime，startTi me 和 endTime 间隔不超过 31 天。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| endTime | Strin g | Query | 否 | 2025-11-07T09:43:17Z | 统计结束时间，格式为UTC 时间。 同时不填startTime 和endTime，则默认获取总的调用量，填了start time和 _ endTime，则获取指定时间段调用量， endTime填了，startTime不填，startTime默认值为endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为startTime 30*24 小时后， 同时填了startTime 和 endTime，startTi me 和 endTime 间隔不超过 31 天。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -apikeyUid | String | aigk- e02e****049ec | API密钥唯一标识。 |
| -endTime | String | 2025-11- 07T09:43:17Z | 统计结束时间，格式为UTC时间。 |
| - failedRequest Count | String | 320 | 失败调用数（startTime-endTime 内，startTime、endTime为空时表示总量）。 |
| - inputTokenCo unt | String | 143157 | 输入Token数（startTime-endTime 内，startTime、endTime为空时表示总量）。 |
| -occupantId | String | os-8691****04e80 | 关联业务UID，如在线服务组或在线服务。 |
| - outputTokenC ount | String | 144655 | 输出Token数（startTime-endTime 内，startTime、endTime为空时表示总量）。 |
| -startTime | String | 2025-10- 12T01:14:54Z | 统计开始时间，格式为UTC时间。 |
| - successReque stCount | String | 141915 | 成功调用数（startTime-endTime 内，startTime、endTime为空时表示总量）。 |
| - totalRequestC ount | String | 142235 | 调用总数（startTime-endTime 内，startTime、endTime为空时表示总量）。 |

**示例**

请求示例

```
GET /online-service/get-gateway-apikey-statistic-total HTTP/1.1 &apiKeyUid=aigk-4fb8b2*** &occupantId=os-4821934902***
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ListGatewayAPIKeyDetailCalls

调用ListGatewayAPIKeyDetailCalls查询指定在线服务API Key调用明细列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service/list-gateway-apikey-detail-calls HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 每页条数，取值范围：1- 100。 默认值为10。 |
| sortOrder | Strin g | Query | 否 | desc | 排序顺序，取值范围： desc：降序。 asc：升序。 默认值：desc。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| startTime | Strin g | Query | 否 | 2025-12- 01T03:20:13.000Z | 查询起始时间（utc时间），注： 同时不填startTime 和 endTime，endTime 默认值为当前时间，startTime默认值为endTime 30*24 小时前， endTime填了，startTime不填，startTime默认值为endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为startTime 30*24 小时后， 同时填了startTime 和 endTime，startTi me和endTime间隔不超过 31 天。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| endTime | Strin g | Query | 否 | 2025-12- 01T03:20:13.000Z | 查询结束时间（utc时间），注： 同时不填startTime 和 endTime，endTime 默认值为当前时间，startTime默认值为endTime 30*24 小时前， endTime填了，startTime不填，startTime默认值为endTime 30*24 小时前， endTime不填， startTime填了，endTime默认值为startTime 30*24 小时后， 同时填了startTime 和 endTime，startTi me和endTime间隔不超过 31 天。 |
| type | Strin g | Query | 是 | SUCCESS | 明细类型，取值范围： SUCCESS：成功明细。 FAILED：失败明细。 |
| apiKeyUid | Strin g | Query | 否 | aigk-4fb8b2*** | API Key唯一标识ID。 |
| occupantI d | Strin g | Query | 是 | os-4821934902*** | 在线服务唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -aliyunUid | String | 127756****314 | 阿里云账号UID。 |
| -curl | String | https://example.co m/api/v1/chat | 调用URL。 |
| -ftTimeCost | Integer | 245 | 首字耗时（First Token Time），单位毫秒。 |
| -inputToken | Integer | 96 | 输入Token数量。 |
| -ip | String | 192.168.1.100 | 客户端IP地址。 |
| -method | String | POST | HTTP请求方法。 |
| -outputToken | Integer | 14000 | 输出Token数量。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -request | String | {"model":"qwen- turbo","messages": [{"role":"user","co ntent":"你好"}]} | 请求体内容。 |
| - requestConten tType | String | application/json | 请求内容类型。 |
| -response | String | {"id":"chat- 123","choices": [{"message": {"content":"你好！"}}]} | 响应体内容。 |
| -responseCode | String | 200 | 响应状态码。 |
| -serviceId | String | os-f6d2e36e0c**2 | 服务ID。 |
| -time | String | 2025-01- 15T08:30:00Z | 调用时间。 |
| -totalTimeCost | Integer | 1523 | 总耗时，单位毫秒。 |
| -totalToken | Integer | 14096 | 总Token数量。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 调用明细的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 标准任务的页码。 |

**示例**

请求示例

```
GET /online-service/list-gateway-apikey-detail-calls HTTP/1.1 &type=SUCCESS &occupantId=os-4821934902***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "pageIndex":1,
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### 智能路由

智能体工厂 OpenTrek

###### GetGatewayRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Query | 是 | os-12345678 | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| -gmtModified | String | 2017-11- 27T06:51:26Z | 修改时间。 |
| -aliyunUid | String | 157123456789**** | 阿里云账号ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionId | String | cn-hangzhou | 地域ID。 |
| -routerId | String | aigr-1bsai******ahs | 路由条目ID。 |
| -occupantId | String | os-4821934902*** | 在线服务ID。 |
| -routerPolicy | String | prefix cache _ | 路由策略，支持 global least request，最小请求数。 _ _ prefix cache，前缀匹配。 _ |
| -valid | Boolean | true | 是否生效。 |

**示例**

请求示例

```
&entityId=os-12345678
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ModifyGatewayRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/modify-gateway-router HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| routerId | Strin g | Body | 否 | aigr-123456 | 路由策略ID。 |
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |
| routerPoli cy | Strin g | Body | 否 | prefix cache _ | 路由策略名称，取值范围： global least request _ _ ：队列及等待时长。 prefix cache：请求亲 _ 和性。 least busy：Pod负载调 _ 度。 |
| deleteOpe rator | Boole an | Body | 否 | false | 表示是否启用删除操作符， 用于标识当前上下文或配置中允许执行删除动作，取值范围： 启用：true 关闭：false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /online-service/modify-gateway-router HTTP/1.1 { "entityId":"os-123456" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### CreateGatewayRouter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/create-gateway-router HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |
| routerPoli cy | Strin g | Body | 否 | prefix cache _ | 路由策略名称，取值范围： global least request _ _ ：队列及等待时长。 prefix cache：请求亲 _ 和性。 least busy：Pod负载调 _ 度。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service/create-gateway-router HTTP/1.1 { "entityId":"os-123456" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### 限流设置

###### CreateAPIkeyTrafficLimit

调用CreateAPIkeyTrafficLimit创建在线服务指定API Key的网关限流配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
POST /online-service-group/create-apikey-traffic-limit HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |
| limitValue | Strin g | Body | 是 | 100 | 表示限流值，该参数必填。 |
| limitKey | Strin g | Body | 是 | aigk-9fcabc | 限流APIKey UID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
POST /online-service-group/create-apikey-traffic-limit HTTP/1.1 { }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ModifyAPIkeyTrafficLimit

调用ModifyAPIkeyTrafficLimit修改在线服务指定API Key的限流配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/modify-apikey-traffic-limit HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |
| limitUid | Strin g | Body | 是 | aigl-123456 | 限流配置ID，该参数必填。 |
| limitValue | Strin g | Body | 是 | 100 | 限流值，该参数必填。 |
| deleteOpe rator | Boole an | Body | 否 | true | 用于表示删除操作的标识符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
POST /online-service-group/modify-apikey-traffic-limit HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":false,
 "dynamicMessages":"\t[]",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

###### CreateGatewayTrafficLimit

调用CreateGatewayTrafficLimit创建指定在线服务的网关限流配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/create-gateway-traffic-limit HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |

|  | 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| limitValue | Long | Body | 是 | 100 | 表示限流值，该参数必填。 |
| limitType | Strin g | Body | 是 | "qps" | 限流类型，该参数必填，取值范围： qps ：按每秒请求数。 tpm ：按每分钟 Token数。 |
| limitPerTi me | Strin g | Body | 是 | "query per second" _ _ | 限流类型，该参数必填，取值范围： query per second _ _ ：按每秒请求数。 token per minute _ _ ：按每分钟Token数。 |
| descriptio n | Strin g | Body | 否 | "test" | 限流配置描述信息。 |
| deleteOpe rator | Boole an | Body | 否 | false | 表示是否执行删除操作的标识，当值为true时，表示执行删除操作；当值为false 时，表示不执行删除操作。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
POST /online-service-group/create-gateway-traffic-limit HTTP/1.1 { "entityId":"os-123456", "limitValue":"100", "limitType":""qps"", "limitPerTime":""query_per_second"" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ListGatewayTrafficLimit

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service-group/list-gateway-traffic-limit HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Query | 是 | os-123456 | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gmtCreated | String | 2025-11- 19T02:46:02Z | 创建时间。 |
| -gmtModified | String | 2025-11- 19T03:15:10Z | 修改时间。 |
| -aliyunUid | String | 198226****1225 | 阿里云账号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -limitUid | String | aigl-d7a79c8*** | 限流业务ID。 |
| -occupantId | String | os-0622f0***4369 | 关联资源ID，OS Service ID或Service Group ID。 |
| -limitLatitude | Integer | 0 | 限流策略。枚举值：0表示整体限流，1表示策略限流。 |
| -limitType | String | tpm | 限流类型。枚举值：tpm表示每分钟Token数限流，qps表示每秒请求数限流。 |
| -description | String | 服务限流配置 | 备注。 |
| -limitKey | String | * | 限流匹配的键值，支持定制化。 |
| -limitPerTime | String | token per minute _ _ | 限流时间类型键。枚举值：token per minute _ _ 表示Token限流，query per second表示QPS _ _ 限流。 |
| -limitValue | Integer | 1000 | 限流具体的数值。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /online-service-group/list-gateway-traffic-limit HTTP/1.1 &entityId=nb-ad56b7f600740042f20b89a033b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ModifyGatewayTrafficLimit

调用ModifyGatewayTrafficLimit修改指定在线服务的限流配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/modify-gateway-traffic-limit HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| limitUid | Strin g | Body | 是 | aigl-123456 | 限流配置ID，该参数必填。 |
| entityId | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |
| limitValue | Long | Body | 是 | 100 | 限流值，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| limitType | Strin g | Body | 是 | "qps" | 限流类型，该参数必填，取值范围： qps ：按每秒请求数。 tpm ：按每分钟 Token数。 |
| limitPerTi me | Strin g | Body | 是 | "query per second" _ _ | 限流类型，该参数必填，取值范围： query per second _ _ ：按每秒请求数。 token per minute _ _ ：按每分钟Token数。 |
| descriptio n | Strin g | Body | 否 | "test" | 限流描述。 |
| deleteOpe rator | Boole an | Body | 否 | true | 用于表示删除操作的标识符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /online-service-group/modify-gateway-traffic-limit HTTP/1.1 { "limitUid":"aigl-123456", "entityId":"os-123456", "limitValue":"100", "limitType":""qps"", "limitPerTime":""query_per_second"" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### 异步推理

###### CreateAsyncInferenceService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/create-async-inference-service HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| middlewar eType | Strin g | Body | 是 | "kafka" | 异步推理消息队列中间件类型，该参数必填。 |
| occupantI d | Strin g | Body | 是 | os-123456 | 在线服务ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| middlewar eMetaInfo | Json | Body | 是 | { "middlewareInstanceId": "cluster-private-paas- default", "inputTopic": "kafka-0530", "authUser": "aistudio", "servers": "192.168.1.25:8088,192. 168.1.24:8088,192.168. 1.11:8088" } | 异步推理中间件信息，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 2 | 队列服务cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 4 | 队列服务内存大小，单位为 GB，该参数必填。 |
| instanceC ount | Integ er | Body | 是 | 2 | 实例数量，该参数必填。 |
| storageMo untList | Json | Body | 是 | [ { "storagePath": "oss://****/code/", "mountPath": null, "pvcName": "", "storageSource": 1 } ] | 推理结果存储路径，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /online-service/create-async-inference-service HTTP/1.1 { "middlewareType":""kafka"", "occupantId":"os-123456", "middlewareMetaInfo":"{
  "middlewareInstanceId": "cluster-private-paas-default",
  "inputTopic": "kafka-0530",
  "authUser": "aistudio",
  "servers": "192.168.1.25:8088,192.168.1.24:8088,192.168.1.11:8088"
 }",
"cpuCount":"2", "memCount":"4", "instanceCount":"2", "storageMountList":"[
  {
   "storagePath": "oss://****/code/",
   "mountPath": null,
   "pvcName": "",
   "storageSource": 1
  }
```

`]"`

```
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### DeleteAsyncInferenceService

调用DeleteAsyncInferenceService删除指定的异步推理服务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /online-service/delete-async-inference-service HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| asyncServ iceId | Strin g | Query | 否 | osa-180**** | 异步服务标识符，用于唯一标识一个异步服务请求。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /online-service/delete-async-inference-service HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### GetAsyncInferenceService

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
GET /online-service/get-async-inference-service HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| occupantI d | Strin g | Query | 否 | os-1234**** | 在线服务或服务组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gmtCreated | String | 2025-12- 30T07:11:25Z | 中间件记录的创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z' ，时区UTC。 |
| -gmtModified | String | 2025-12- 30T07:11:25Z | 中间件记录的最后修改时间，格式为 yyyy- MM-dd'T'HH:mm:ss'Z' ，时区UTC。 |
| -aliyunUid | String | 1982********1225 | 阿里云主账号ID。 |
| -regionId | String | cn-neimeng-236e- d01 | 中间件所在的地域ID。 |
| -imageId | String | null | 创建异步服务使用的预置镜像ID。 |

| yyyy-MM- |  |
|---|---|

| 5Z | dd'T'HH:mm:ss'Z' |
|---|---|

|  | MM-dd'T'HH:mm:ss'Z' |
|---|---|

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageVersion | String | null | 异步服务镜像版本。 |
| - asyncServiceId | String | osa- 372e********d3f04 ee4 | 异步服务唯一标识ID。 |
| - asyncServiceN ame | String | osa- 372e********d3f04 ee4 | 异步服务名称。 |
| -occupantId | String | os- 120e********85e04 25c | 关联资源实体ID，可以是在线服务ID或在线服务组ID。 |
| -middlewareId | String | am- 0c65********ce304 064 | 异步中间件唯一标识ID。 |
| -cpuCount | Integer | 2 | 异步服务分配的CPU核数。 |
| -memCount | Integer | 4 | 异步服务分配的内存大小，单位GB。 |
| - instanceCount | Integer | 2 | 异步服务的实例副本数量。 |
| -storageUrl | String | oss://mm-aistudio- test.oss-cn- ****.intra.****.com/ images/ | 异步服务结果的持久化存储地址。 |
| - middlewareMe taInfo | Struct | [] | 异步中间件的详细配置信息，包含Kafka连接参数等。 |
| --gmtCreated | String | 2025-12- 30T07:11:25Z | 中间件记录的创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z' ，时区UTC。 |
| --gmtModified | String | 2025-12- 30T07:11:25Z | 中间件记录的最后修改时间，格式为 yyyy- MM-dd'T'HH:mm:ss'Z' ，时区UTC。 |
| --aliyunUid | String | 1982********1225 | 阿里云主账号ID。 |
| --regionId | String | cn-neimeng-236e- d01 | 中间件所在的地域ID。 |
| --middlewareId | String | am- 0c65********ce304 064 | 异步中间件唯一标识ID。 |

| yyyy-MM- |  |
|---|---|

| 5Z | dd'T'HH:mm:ss'Z' |
|---|---|

|  | MM-dd'T'HH:mm:ss'Z' |
|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- middlewareTy pe | String | kafka | 中间件类型，当前支持kafka。 |
| -- middlewareIns tanceId | String | cluster-t3**uo | Kafka实例ID。 |
| --inputTopic | String | hk monitor topic 1 _ _ _ 002 | Kafka输入Topic名称，用于接收异步推理请求。 |
| --outputTopic | String | null | Kafka输出Topic名称，用于发送异步推理结果。 |
| --authUser | String | ai****io | Kafka连接的认证用户名。 |
| --servers | String | 192.168.***.***:80 88,192.168.***.***: 8088,192.168.***.* **:8088 | Kafka Broker服务器地址列表，多个地址以逗号分隔。 |

**示例**

请求示例

```
GET /online-service/get-async-inference-service HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### 内容安全

###### GetContentSecurity

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| occupantI d | Strin g | Query | 否 | os- f5d5a5d2049b6047b9 | 在线服务或灰度组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -description | String | 描述 | 描述。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间 |
| -gmtModified | String | 2018-12- 07T02:24:26.000Z | 修改时间。 |
| -occupantId | String | os-4821934902*** | 所属资源ID，在线服务或者灰度组ID。 |
| - openaiProxyUi d | String | osop-a3356575** | 代理UID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionId | String | cn-hangzhou | 地域ID。 |
| - securityServic eType | String | ai gateway _ | 内容安全类型。枚举值：openai proxy、 _ ai gateway。 _ |
| -securityUid | String | oscs-42282f8e0*** | 安全UID。 |
| - specificationC onfig | String | 2c-2g-2r | 代理服务规格。 |
| - securityConfig | Struct | {} | 内容安全配置。 |
| -- checkRuleList | List | ["inputContent", "outputContent"] | 规则类型列表。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### DeleteContentSecurity

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /online-service/delete-content-security HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| securityUi d | Strin g | Query | 是 | oscs- ed873eb50857***** | 内容安全配置的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /online-service/delete-content-security HTTP/1.1 &securityUid=oscs-ed873eb50857*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### GetContentSecurityAccess

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /online-service/get-content-security-access HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| getAiGate wayAcces s | Boole an | Body | 否 | false | 是否检测AI网关，取值范围： 开启：true。 关闭：false。 默认值：false。 |
| quotaId | Strin g | Body | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| resourceP oolId | Strin g | Body | 否 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |
| instanceId | Strin g | Body | 否 | i- 08ea24a0b64a77a9886 6 | AI网关实例ID，当 GetAiGatewayAccess为 true时，该参数不能为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - aiGatewayAcc ess | Boolean | true | 表示用户已启用AI网关访问权限，允许通过AI网关调用后端AI服务。 |
| - resourcePoolA ccess | Boolean | true | 表示用户具有访问资源池的权限，可查看、使用或管理该资源池中的计算、存储等资源。 |

**示例**

请求示例

```
POST /online-service/get-content-security-access HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "data":{
  "resourcePoolAccess":true,
  "aiGatewayAccess":true
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

###### ModifyContentSecurity

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-content-security HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| securityUi d | Strin g | Body | 是 | oscs- ed873eb50857a04e7b | 内容安全配置ID，该参数必填。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| securityCo nfig | Strin g | Body | 否 | { "checkRuleList": ["inputContent","outputC ontent"] } | 选择安全配置的类型，取值范围： inputContent：输入内容。 outputContent：输出内容。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify-content-security HTTP/1.1 { "securityUid":"oscs-ed873eb50857a04e7b" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

###### CreateContentSecurity

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/create-content-security HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| open | Boole an | Body | 是 | true | 是否开启内容安全，该参数必填，取值范围： 开启：true 关闭：false |
| occupantI d | Strin g | Body | 是 | os- f5d5a5d2049b6047b9 | 在线服务ID或者灰度组ID， 该参数必填。 |
| securitySe rviceType | Strin g | Body | 是 | openai proxy _ | 安全服务类型，该参数必填，取值范围： openai proxy：使用经 _ 典网络网关。 ai gateway：使用 _ Higress网关。 |
| securityCo nfig | Json | Body | 否 | { "checkRuleList": ["inputContent"] } | 选择内容安全检测规则，取值范围： inputContent：输入内容。 outputContent：输出内容。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service/create-content-security HTTP/1.1 { "open":"true", "occupantId":"os-f5d5a5d2049b6047b9", "securityServiceType":"openai_proxy" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 灰度群组

##### CreateGatewayGrayscale

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/create-gateway-grayscale HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os- 00740042f20b89a033b* *** | 服务或者服务组ID，该参数必填。 |
| canaryTyp e | Strin g | Body | 否 | canary-weight | 灰度类型。 canary-weight. 按照权重灰度，默认值 |
| descriptio n | Strin g | Body | 否 | description | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| canaryCo nfig | Json | Body | 是 | {"serviceId": "os- 1234***", "value": 10, "servicePort": 80 } | 灰度发布配置，该参数必填。 |
| scheduleT ime | Strin g | Body | 否 | 2025-04-16 00:00:00 | 定时启动时间，格式为 yyyy-MM-dd HH:mm:ss。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /online-service-group/create-gateway-grayscale HTTP/1.1 { "entityId":"os-00740042f20b89a033b****", "canaryConfig":"{"serviceId": "os-1234***",
 "value": 10,
"servicePort": 80 }" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateOnlineServiceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os-d20bd**** | 在线服务ID，该参数必填。 |
| serviceGr oupName | Strin g | Body | 是 | 我的灰度群组 | 灰度群组名称，该参数必填，长度为2～128个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-) |
| serviceGr oupDesc | Strin g | Body | 否 | 用户管理组 | 灰度组描述，描述长度为 2~256个字符，不能以 http://和https://开头 |

|  | 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| aiGateway | Json | Body | 否 | { "open": true, "instanceId": "i- 08ea24a0b***" } | 网关配置。 |
| rateLimitR ule | Json | Body | 否 | { "open": true, "limitType": "query per second", _ _ "limitValue": 3 } | 限流配置。 |
| monitored Rule | Json | Body | 否 | { "open": true } | 网关性能监控配置。 |
| asyncServ ice | Json | Body | 否 | { "open": true, "middlewareType": "kafka", "middlewareMetaInfo": { "middlewareInstanceId": "clust***", "inputTopic": "kafk**", "authUser": "aistudio", "servers": "192.16**" }, "cpuCount": 2, "memCount": 4, "instanceCount": 2, "storageMountList": [ { "storagePath": "oss://pe**/code/", "mountPath": null, "pvcName": "", "storageSource": 1 } ] } | 异步配置。 |
| contentSe curity | Json | Body | 否 | { "open": true, "occupantId": "os- fd2***", "securityServiceType": "openai proxy", _ "securityConfig": { } } | 内容安全配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"serviceGroupUid ": "osg-977f0***"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service-group/create HTTP/1.1 { "serviceId":"os-d20bd****",
```

`"serviceGroupName":"`我的灰度群组"

```
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"serviceGroupUid\": \"osg-977f0***\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteOnlineServiceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceGr oupId | Strin g | Query | 是 | osg-12345** | 灰度组ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&serviceGroupId=1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetOnlineServiceGroupDetail

调用GetOnlineServiceGroupDetail查询指定灰度组详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceGr oupUid | Strin g | Query | 是 | osg-8a3f****074 | 服务组的唯一标识符，用于在系统中唯一标识一个服务组。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aiGatewayList | Array | [] | AI网关配置。 |
| --accessType | String | inference sync vpc _ _ | 推理服务访问类型，标识服务的网络访问方式。 枚举值： inference sync vpc (同步VPC _ _ 网络访问)、 inference sync classic (同步经 _ _ 典网络访问)、 inference async vpc req (异步 _ _ _ VPC请求访问)、 inference async vpc resp (异步 _ _ _ VPC查询访问)、 inference async classic req ( _ _ _ 异步经典网络请求访问)、 inference async classic resp ( _ _ _ 异步经典网络查询访问)。 |
| --aliyunUid | String | 127756****314 | 阿里云账号ID，标识服务组所属的阿里云主账号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --description | String | EffectGateway Success. | 网关配置的备注说明。 |
| --domainName | String | 9094b5a7.vpc.inter .env38.shuguang.c om | 网关访问域名，用于访问推理服务。 |
| -- gatewayStatus | String | DEPLOY SUCCEED _ ED | 网关状态，表示网关的部署和运行状态。枚举值： PENDING (等待部署)、 DEPLOYING (部署中)、 DEPLOY SUCCEEDED (部署成 _ 功)、 DEPLOY FAILED (部署失 _ 败)、 WAIT UPDATE (等待更 _ 新)、 UPDATEING (更新中)、 UPDATE SUCCEEDED (更新成 _ 功)、 UPDATE FAILED (更新失 _ 败)、 WAIT UNDEPLOY (等待下 _ 线)、 UNDEPLOYING (下线中)、 UNDEPLOY SUCCEEDED (下线成 _ 功)、 UNDEPLOY FAILED (下线失败)。 _ |
| --gatewayUid | String | 1f999f0b-3547- 4948-aadb- d213e78578bb | 网关的唯一标识符。 |
| --gmtCreated | String | 2026-02- 25T01:40:46Z | 创建时间。 |
| --gmtModified | String | 2026-02- 25T01:40:46Z | 修改时间。 |
| --gwInstanceId | String | i- nmrlc6ip2riyzjweco 1i | 网关实例ID，标识Higress网关的具体实例。 |
| -- ingressClassN ame | String | higress | Ingress类型，标识使用的Ingress控制器类型。 |
| -- occupantReso urceId | String | osg-8a3f****074 | 网关绑定的资源实体ID，如RAG实例、推理服务等。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --regionId | String | cn-wulan-env38- d01 | 地域ID，标识服务组所在的阿里云地域。 |
| -- resourcePoolUi d | String | rp-a664****23 | 资源池ID，标识网关所在的资源池。 |
| --slbIp | String | 172.16.1.158 | SLB地址，即Higress网关服务关联的负载均衡器IP地址。 |
| --slbIpType | String | vpc | SLB地址类型，标识网络类型。枚举值： vpc (VPC类型网络)、 classic (经典网络类型)。 |
| - aiGatewayTraf ficLimitList | Array | [] | AI网关限流配置。 |
| --aliyunUid | String | 127756****314 | 阿里云账号ID，标识服务组所属的阿里云主账号。 |
| --gmtCreated | String | 2026-02- 25T01:40:46Z | 创建时间。 |
| --gmtModified | String | 2026-02- 25T01:40:46Z | 修改时间。 |
| --limitKey | String | apikey-xxx-*** | 限流匹配的键值，支持定制化，如API Key、IP 等。 |
| --limitLatitude | Integer | 0 | 限流策略维度，0表示整体限流，1表示策略限流。 |
| --limitPerTime | String | second | 限流时间类型，如second(秒)、minute(分钟) 等。 |
| --limitType | String | qps | 限流类型，支持tpm(每分钟Token数)或qps(每秒请求数)。 |
| --limitUid | String | limit-a1b2****h8 | 限流业务ID，用于唯一标识一条限流规则。 |
| --limitValue | Integer | 100 | 限流具体的数值，表示在限定时间内的最大请求数。 |
| --occupantId | String | osg-8a3f****074 | 关联资源ID，通常为服务组ID或服务ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --regionId | String | cn-wulan-env38- d01 | 地域ID，标识服务组所在的阿里云地域。 |
| -aliyunUid | String | 127756****314 | 阿里云账号ID，标识服务组所属的阿里云主账号。 |
| - apikeyPermissi on | Boolean | true | 当前用户是否有API Key管理权限，用于控制用户是否可以管理服务组的API Key。 |
| -description | String | EffectGateway Success. | 网关配置的备注说明。 |
| -gmtCreated | String | 2026-02- 25T01:40:46Z | 服务组的创建时间，采用UTC时区，格式为ISO 8601标准。 |
| -gmtModified | String | 2026-02- 25T01:40:46Z | 服务组的最后修改时间，采用UTC时区，格式为 ISO 8601标准。 |
| -regionId | String | cn-wulan-env38- d01 | 地域ID，标识服务组所在的阿里云地域。 |
| - servedModelN ame | String | qwen-turbo | 服务组关联的模型名称，标识服务组使用的推理模型。 |
| - serviceGroupN ame | String | test1 | 服务组的名称，由用户自定义，用于标识和展示服务组。 |
| - serviceGroupU id | String | osg-8a3f****074 | 服务组的唯一标识符，用于在系统中唯一标识一个服务组。 |
| -asyncService | Struct | {} | AI网关异步配置。 |
| --aliyunUid | String | 127756****314 | 阿里云账号ID，标识服务组所属的阿里云主账号。 |
| -- asyncServiceId | String | asvc-9i0j****p2 | 异步服务的唯一标识符。 |
| -- asyncServiceN ame | String | async-inference- service | 异步服务的名称。 |
| --cpuCount | Integer | 4 | 异步服务实例的CPU核数配置。 |
| --gmtCreated | String | 2026-02- 25T01:40:46Z | 创建时间。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gmtModified | String | 2026-02- 25T01:40:46Z | 修改时间。 |
| --imageId | String | img-a1b2****h8 | 创建异步服务使用的预置镜像ID。 |
| -- imageVersion | String | v1.0.0 | 异步服务镜像版本号。 |
| -- instanceCount | Integer | 2 | 异步服务实例的副本数量。 |
| --memCount | Integer | 8 | 异步服务实例的内存配置，单位为GB。 |
| --middlewareId | String | mw-q1w2****i8 | 中间件的唯一标识符。 |
| --occupantId | String | osg-8a3f****074 | 关联资源ID，通常为服务组ID或服务ID。 |
| --regionId | String | cn-wulan-env38- d01 | 地域ID，标识服务组所在的阿里云地域。 |
| --storageUrl | String | oss://bucket- name/path/to/stora ge | 持久化存储地址，通常为OSS路径，用于存储模型和数据。 |
| -- middlewareMe taInfo | Struct | {} | 中间件信息。 |
| ---aliyunUid | String | 127756****314 | 阿里云账号ID，标识服务组所属的阿里云主账号。 |
| ---authUser | String | kafka-user-*** | 中间件USER。 |
| ---gmtCreated | String | 2026-02- 25T01:40:46Z | 创建时间。 |
| ---gmtModified | String | 2026-02- 25T01:40:46Z | 修改时间,。 |
| ---inputTopic | String | async-input-topic | Kafka输入Topic名称，用于接收异步推理请求。 |
| --- middlewareId | String | mw-q1w2****i8 | 中间件的唯一标识符。 |
| --- middlewareIns tanceId | String | kafka-inst- 1a2b****8h | 中间件实例ID，标识具体的中间件实例。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --- middlewareTy pe | String | KAFKA | 中间件类型，如KAFKA、ROCKETMQ等。 |
| ---outputTopic | String | async-output-topic | Kafka输出Topic名称，用于返回异步推理结果。 |
| ---regionId | String | cn-wulan-env38- d01 | 地域ID，标识服务组所在的阿里云地域。 |
| ---servers | String | 172.16.1.100:9092 ,172.16.1.101:909 2 | Kafka服务器地址列表，多个地址用逗号分隔。 |
| -instanceCost | Struct | InstanceCostVO | 实例成本信息。 |
| --runningCost | Float | 0.00 | 当前运行中的实例产生的费用，单位为元，保留两位小数。 |
| --runningCpu | Integer | 0 | 当前运行中的CPU资源使用量，单位为核。 |
| --runningGpu | Integer | 0 | 当前运行中的GPU卡数量。 |
| -- runningGpuMe m | Integer | 0 | 当前运行中的GPU显存使用量，单位为GB。 |
| --runningMem | Integer | 0 | 当前运行中的内存资源使用量，单位为GB。 |
| --runningPod | Integer | 0 | 当前运行中的Pod实例数量。 |
| --totalCost | Float | 0.00 | 服务组总消耗，保留两位小数。 |
| --totalCpu | Integer | 0 | 服务组CPU资源总量，单位为核。 |
| --totalGpu | Integer | 0 | 服务组GPU卡总数。 |
| --totalGpuMem | Integer | 0 | 服务组GPU显存总量，单位为GB。 |
| --totalMem | Integer | 0 | 服务组内存资源总量，单位为GB。 |
| --totalPod | Integer | 0 | 服务组Pod实例总数。 |

**示例**

智能体工厂 OpenTrek 请求示例

```
&serviceGroupUid=osg-12345**
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "gmtModified":"2026-02-25T01:40:46Z",
  "asyncService":{
   "imageVersion":"v1.0.0",
   "memCount":8,
   "middlewareId":"mw-q1w2****i8",
   "gmtModified":"2026-02-25T01:40:46Z",
   "imageId":"img-a1b2****h8",
   "aliyunUid":"127756****314",
   "gmtCreated":"2026-02-25T01:40:46Z",
   "middlewareMetaInfo":{
    "middlewareId":"mw-q1w2****i8",
    "outputTopic":"async-output-topic",
    "gmtModified":"2026-02-25T01:40:46Z",
    "servers":"172.16.1.100:9092,172.16.1.101:9092",
    "aliyunUid":"127756****314",
    "gmtCreated":"2026-02-25T01:40:46Z",
    "regionId":"cn-wulan-env38-d01",
    "middlewareType":"KAFKA",
    "middlewareInstanceId":"kafka-inst-1a2b****8h",
    "authUser":"kafka-user-***",
    "inputTopic":"async-input-topic"
   },
   "asyncServiceId":"asvc-9i0j****p2",
   "regionId":"cn-wulan-env38-d01",
   "instanceCount":2,
   "asyncServiceName":"async-inference-service",
   "occupantId":"osg-8a3f****074",
   "storageUrl":"oss://bucket-name/path/to/storage",
   "cpuCount":4
  },
  "aliyunUid":"127756****314",
  "gmtCreated":"2026-02-25T01:40:46Z",
  "serviceGroupName":"test1",
  "instanceCost":{
   "runningGpuMem":0,
   "runningMem":0,
   "runningPod":0,
   "totalCpu":0,
   "totalMem":0,
   "totalPod":0,
   "runningGpu":0,
   "totalGpuMem":0,
"runningCost":00,
```

智能体工厂 OpenTrek

```json
   runningCost:0.0,
   "runningCpu":0,
   "totalCost":0.0,
   "totalGpu":0
  },
  "description":"EffectGateway Success.",
  "serviceGroupUid":"osg-8a3f****074",
  "apikeyPermission":true,
  "servedModelName":"qwen-turbo",
  "regionId":"cn-wulan-env38-d01",
  "aiGatewayTrafficLimitList":[
   {
    "limitValue":100,
    "gmtModified":"2026-02-25T01:40:46Z",
    "aliyunUid":"127756****314",
    "gmtCreated":"2026-02-25T01:40:46Z",
    "regionId":"cn-wulan-env38-d01",
    "limitPerTime":"second",
    "limitLatitude":0,
    "limitType":"qps",
    "occupantId":"osg-8a3f****074",
    "limitKey":"apikey-xxx-***",
    "limitUid":"limit-a1b2****h8"
   }
```

`],`

```json
  "aiGatewayList":[
   {
    "gmtModified":"2026-02-25T01:40:46Z",
    "occupantResourceId":"osg-8a3f****074",
    "aliyunUid":"127756****314",
    "gmtCreated":"2026-02-25T01:40:46Z",
    "description":"EffectGateway Success.",
    "slbIpType":"vpc",
    "resourcePoolUid":"rp-a664****23",
    "accessType":"inference_sync_vpc",
    "ingressClassName":"higress",
    "gatewayUid":"1f999f0b-3547-4948-aadb-d213e78578bb",
    "regionId":"cn-wulan-env38-d01",
    "domainName":"9094b5a7.vpc.inter.env38.shuguang.com",
    "slbIp":"172.16.1.158",
    "gatewayStatus":"DEPLOY_SUCCEEDED",
    "gwInstanceId":"i-nmrlc6ip2riyzjweco1i"
   }
```

]

```json
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### ListGatewayGrayscale

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service-group/list-gateway-grayscale HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Query | 是 | osg- 00740042f20b89a033b* *** | 灰度组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {[]} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -canaryConfig | Array | {} | 灰度配置。 |
| --serviceId | String | os-****04369 | 服务id。 |
| --value | Integer | 100 | 灰度值。 |
| -canaryType | String | canary-weight | 灰度类型。枚举值包括：canary-by-header、 canary-by-cookie、canary-weight。 |
| -canaryUid | String | aigc-****0461e | 灰度业务ID。 |
| -description | String | NULL | 备注。 |
| -occupantId | String | osg-****04b19 | os service ID或者os service group ID。 |
| -scheduleTime | String | 2026-03- 03T16:55:30Z | 定时执行时间。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /online-service-group/list-gateway-grayscale HTTP/1.1 &entityId=osg-00740042f20b89a033b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{[]}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListOnlineServiceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 10 | 灰度组列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| serviceGr oupName | Strin g | Query | 否 | 我的灰度组 | 灰度组名字。 |
| serviceGr oupUid | Strin g | Query | 否 | osg-123456** | 灰度组的唯一标识符，用于区分不同的灰度组。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {[]} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - aiGatewayTraf ficLimitList | Array | [] | AI网关限流配置。 |
| --aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| --description | String | 描述 | 指标描述。 |
| --gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| --gmtModified | String | 2020-04- 23T06:08:48.000Z | 修改时间。 |
| --limitKey | String | * | 限流Key。 |
| --limitLatitude | Integer | 0 | 限流策略 |
| --limitPerTime | String | query per second _ _ | 限流key的单位值。 |
| --limitType | String | qps | 限速类型。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| --limitUid | String | aigl-957d2** | 限流Uid。 |
|---|---|---|---|
| --limitValue | Integer | 100 | 限流值 |
| --occupantId | String | osg-ee197*** | 服务或灰度组唯一标识ID。 |
| --regionId | String | cn-hangzhou | 地域ID。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -clusterIp | String | c039fc341283***4 42e794d | 集群IP。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间 |
| -gmtModified | String | 2018-12- 07T02:24:26.000Z | 修改时间。 |
| -instanceId | String | i- bp67acfmxazb4p** ** | AI网关实例ID。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - resourcePoolId | String | rp- bc47fd6f0af72043 5c0a4d60eeba63** ** | 资源池ID。 |
| - serviceGroupN ame | String | 服务组A | 灰度组名称。 |
| - serviceGroupU id | String | osg-ee197*** | 灰度组Uid |
| - serviceGroupD esc | String | 描述 | 灰度组描述。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 灰度组的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 灰度组的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{[]}",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### ListServiceGroupRelatedService

调用ListServiceGroupRelatedService查询所有的灰度组关联服务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /online-service-group/list-related-service HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 10 | 列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| serviceGr oupId | Strin g | Query | 是 | osg-12345** | 灰度组ID。 |
| serviceId | Strin g | Query | 否 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |
| serviceNa me | Strin g | Query | 否 | service-name | 在线服务名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {[]} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -canaryConfig | Array | [] | 灰度配置。 |
| --serviceId | String | os-46346* | 服务ID。 |
| --servicePort | Integer | 80 | 服务端口。 |
| --value | Integer | 20 | 服务灰度值。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 8 | CPU总数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtModified | String | 2018-12- 07T02:24:26.000Z | 修改时间。 |
| -gpuCount | Integer | 0 | GPU总数。 |
| -gpuCountUnit | Integer | -1 | 表示GPU数量的最小计量单位，为1表示单位是个数，为-1表示gpu虚拟化，单位为显存数。 |
| -gpuMemTotal | Integer | 40 | 显卡总显存量，单位为MB |
| - gpuMemTotal Unit | Integer | 1 | 表示GPU数量的最小计量单位，为-1表示单位是个数，为1表示gpu虚拟化，单位为显存数。 |
| -imageId | String | image- 05cefd0be2exxxx | 镜像ID。 |
| -imageName | String | testImageName | 镜像名称。 |
| - instanceCount | Integer | 1 | 实例数量。 |
| -memCount | Integer | 8 | 内存大小，单位为GB。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | 配额名称 | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -serviceId | String | os-2256436* | 服务ID。 |
| -serviceName | String | 服务 | 服务名称。 |
| -serviceStatus | Integer | 0 | 服务状态。 |
| -serviceType | Integer | 1 | 绑定的服务类型 1-在线服务 2-异步服务 |
| -modelId | String | model- rbvg5wzljz****ks92 | 模型ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -modelName | String | 模型一 | 模型名称 |
| -storageUrl | String | oss://oss-cn- shanghai.aliyuncs. com/emr-test | 三方存储URL。 |
| -description | String | 描述 | 描述。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 关联在线服务总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 页码。 |

**示例**

请求示例

```
GET /online-service-group/list-related-service HTTP/1.1 &serviceGroupId=osg-12345**
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{[]}",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### ModifyGatewayGrayscale

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service-group/modify-gateway-grayscale HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Body | 是 | os- 00740042f20b89a033b* *** | 服务或者服务组ID，该参数必填。 |
| canaryUid | Strin g | Body | 否 | aigc-12345** | 灰度uid。 |
| canaryTyp e | Strin g | Body | 否 | canary-weight | 灰度类型。 canary-weight 按照权重灰度，默认值 |
| descriptio n | Strin g | Body | 否 | description | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| canaryCo nfig | Json | Body | 是 | {"serviceId": "os- 1234***", "value": 10, "servicePort": 80 } | 灰度发布配置，该参数必填。 |
| scheduleT ime | Strin g | Body | 否 | 2025-04-16 00:00:00 | 定时启动时间，格式为 yyyy-MM-dd HH:mm:ss。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service-group/modify-gateway-grayscale HTTP/1.1 { "entityId":"os-00740042f20b89a033b****", "canaryConfig":"{"serviceId": "os-1234***",
 "value": 10,
"servicePort": 80 }" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineServiceGroup

调用ModifyOnlineServiceGroup修改灰度组部分信息，包括灰度组名称和描述。 智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service-group/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceGr oupId | Strin g | Body | 是 | osg-123456** | 灰度组ID，该参数必填。 |
| serviceGr oupName | Strin g | Body | 是 | 我的灰度组 | 灰度组名字，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| serviceGr oupDesc | Strin g | Body | 否 | 用户管理组 | 灰度组描述，描述长度为 2~256个字符，不能以 http://和https://开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /online-service-group/modify HTTP/1.1 { "serviceGroupId":"osg-123456**",
```

`"serviceGroupName":"`我的灰度组"

```
}
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ModifyOnlineServiceToGroup

调用ModifyOnlineServiceToGroup修改灰度组（添加/删除服务）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service-group/modify-online-service-to-group HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceGr oupId | Strin g | Body | 是 | osg-12345** | 灰度组ID，该参数必填。 |
| operation Type | Strin g | Body | 是 | remove | 操作类型，该参数必填，取值范围： remove add |
| serviceId | Strin g | Body | 是 | os-d20bd45d**** | 在线服务ID，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service-group/modify-online-service-to-group HTTP/1.1 { "serviceGroupId":"osg-12345**", "operationType":"remove", "serviceId":"os-d20bd45d****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 一键压测

##### CreateStressTestTaskConfig

调用CreateStressTestTaskConfig创建性能压测任务以及配置信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | Strin g | Body | 是 | task-name | 任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| taskDesc | Strin g | Body | 否 | task-desc | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| onlineServ iceId | Strin g | Body | 否 | os-***** | 在线服务ID。 |
| parentPla nId | Strin g | Body | 否 | stp-**** | 归属压测计划ID。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 当数据加速器实例在运行状态时，不允许修改 memCount。 |
| quotaId | Strin g | Body | 是 | rq-**** | 资源配额ID，该参数必填。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| scheduleT ime | Strin g | Body | 否 | 2025-04-16 00:00:00 | 定时启动时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| configNa me | Strin g | Body | 否 | config-sample | 配置名称。 |
| configDes c | Strin g | Body | 否 | config-desc | 配置描述。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelTyp e | Integ er | Body | 是 | 0 | 模型类型，该参数必填，取值范围： 0：LLM。 |
| durationC onfig | Json | Body | 是 | { "sampleCount": 10 } | 压测时长配置，该参数必填。 |
| datasetCo nfig | Json | Body | 是 | { "datasetType": "RANDOM", "randomInputLen": 100, "randomOutputLen": 100, "randomRangeRatio": 0.0, "randomPrefixLen": 20 } | 数据集配置，该参数必填。 |
| modeConf ig | Json | Body | 是 | { "stressMode": "FIXED REQUEST RATE", _ _ "requestRate": 10, "maxConcurrency": 100 } | 压测模式配置，该参数必填。 |
| extraConfi g | Json | Body | 否 | { "seed": 0 } | 额外配置。 |
| customOp tions | Strin g | Body | 否 | “--no-stream True” | 自定义压测参数。 |
| storageMo untList | Json | Body | 否 | [{ "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { ”sressTestTaskId“: "stt-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "taskName":"task-name", "cpuCount":"1", "memCount":"1", "quotaId":"rq-xxx", "modelType":"0", "durationConfig":"{
        "sampleCount": 10
    }",
"datasetConfig":"{
        "datasetType": "RANDOM",
        "randomInputLen": 100,
        "randomOutputLen": 100,
        "randomRangeRatio": 0.0,
        "randomPrefixLen": 20
    }",
"modeConfig":"{
        "stressMode": "FIXED_REQUEST_RATE",
        "requestRate": 10,
        "maxConcurrency": 100
    }"
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{    ”sressTestTaskId“: \"stt-*****\"  }",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListStressTestTask

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 压测任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | scaleTime | 排序字段。 默认值：scaleTime。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | stt-**** | 任务ID。 |
| taskName | Strin g | Query | 否 | task-name | 任务名称。 |
| taskStatus | Integ er | Query | 否 | 0 | 任务状态。 |
| quotaId | Strin g | Query | 否 | rq-**** | 资源配额ID。 |
| quotaNam e | Strin g | Query | 否 | quota-name | 资源配额名称。 |
| modelId | Strin g | Query | 否 | md-xxx | 模型ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型名称。 |
| datasetId | Strin g | Query | 否 | ds-**** | 数据集ID。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| onlineServ iceId | Strin g | Query | 否 | os-**** | 在线服务ID。 |
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | null | 动态错误消息列表；成功时通常为 null。 |
| data | Array | - | 压测任务列表。 |
| - codeMountList | Array | null | 代码挂载列表；当前代码路径未填充，通常为 null。 |
| --codeId | String | null | 代码集id。 |
| --codeName | String | null | 代码集名称。 |
| -- codeRepoType | Integer | null | 源代码平台类型，取值： GITHUB 、 GITLAB 、 GITEE 、 CODE 、 CODEUP |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | PVC 名称。 |
| - datasetMountL ist | Array | [{ "mountPath": "/root", "datasetId": "ds- 78b1242ffed14878 88af363a24***", "datasetType": 0, "dataSource": 1, "quotaId": "rq- d8890a98089c204 1d8086bb0b2e27f* **", "dataAccInstance": "da- df89s8f9sdfs99sae *****" }] | 数据集挂载列表（默认 []）。 |
| -- dataAccInstan ce | String | dataacc-i-011 | 数据加速实例标识。 |

|  | GITHUB |  |
|---|---|---|
| CODE |  |  |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --dataType | Integer | 0 | 数据类型。 |
| -- datasetFileNa me | String | prompt- benchmark.jsonl | 文件名。 |
| --datasetId | String | ds-20260305001 | 数据集 ID。 |
| --datasetName | String | prompt-benchmark | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v2 | 数据集版本。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | 数据类型。 |
| - modelMountLi st | Array | null | 文件名。 |
| -- dataAccInstan ce | String | dataacc-i-011 | 数据集 ID。 |
| --modelId | String | md-system- 7ed6f4208a44e87 8ce | 数据集名称。 |
| --modelName | String | Qwen3-4B | 数据集类型。 |
| --modelType | Integer | 0 | 数据集版本。 |
| -- modelVersion | String | v1.0 | 容器内挂载路径。 |
| --mountPath | String | /mnt/output/ | PVC 名称。 |
| --pvcName | String | pvc-storage-st-001 | 模型挂载列表（默认 []）。 |
| --weightType | Integer | 0 | 数据加速实例标识。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - nodeConfigList | Array | null | 模型 ID。 |
| --cpuCount | Integer | 8 | 模型名称。 |
| --gpuCount | Integer | 1 | 模型类型。 |
| -- gpuMemCount | Integer | 24 | 模型版本。 |
| --memCount | Integer | 32 | 容器内挂载路径。 |
| --nodeCount | Integer | 1 | PVC 名称。 |
| --nodeType | Integer | 0 | 权重类型。 |
| -- sharedMemCo unt | Integer | 4 | 节点配置列表（默认 []）。 |
| -- startCommand | String | python benchmark.py | CPU 核数。 |
| - storageMountL ist | Array | null | GPU 卡数。 |
| --mountPath | String | /mnt/output/ | GPU 显存规格。 |
| --pvcName | String | pvc-storage-st-001 | 内存规格。 |
| --storagePath | String | oss://aipaas- bucket/stress- test/output/ | 节点数量。 |
| -- storageSource | Integer | 1 | 节点类型。 |
| -aliyunUid | String | 1277********1314 | 共享内存规格。 |
| -cpuCount | Integer | 8 | 启动命令。 |
| -failedMsg | String | null | 存储挂载列表（默认 []）。 |
| -gmtCreated | String | 2026-03- 05T03:00:00Z | 容器内挂载路径。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| -gmtEnd | String | 2026-03- 05T06:35:20Z | PVC 名称。 |  |  |
| -gmtModified | String | 2026-03- 05T03:05:00Z | OSS 存储路径。 |  |  |
| -imageId | String | img-llm-stress | 存储来源类型。 |  |  |
| - imageIdAndVe rsion | String | img-llm-stress, v1.2.3 | 阿里云账号 UID。 |  |  |
| -imageVersion | String | v1.2.3 | CPU 核数。 |  |  |
| -memCount | Integer | 32 | 失败信息；当前代码中列表接口未主动填充。 |  |  |
| - onlineServiceI d | String | os- 698b8e19000da04 699 | 配置创建时间（UTC）。 |  |  |
| -parentPlanId | String | plan-202603 | 任务结束时间（仅结束态可见）。 |  |  |
| -quotaId | String | rq- 0635cf690bb0704b 1c | 配置修改时间（UTC）。 |  |  |
| -quotaName | String | A100 high net pool | 镜像 ID。 |  |  |
| -regionId | String | cn-wulan-env38- d01 | getter 计算字段（ imageId + ", " + imageVersion ）。 |  |  |
|  |  |  |  | imageId + ", " + |  |
| -remark | String | auto schedule | 镜像版本。 |  |  |
| -taskConfigId | String | cfg-st-001 | 内存规格。 |  |  |
| -taskDesc | String | nightly stress test | 在线服务 ID。 |  |  |
| -taskId | String | st-20260305-0003 | 父计划 ID。 |  |  |
| -taskName | String | nightly-qwen3-4b | 资源配额 ID。 |  |  |
| -taskStatus | Integer | 2 | 资源配额名称（由 fillVO 填充）。 |  |  |

| 01 | imageVersion |
|---|---|

| OpenTr | ek |  | AI Studio ·API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - taskSubStatus | Integer | null | 地域 ID。 |
| -instanceCost | Struct | 0 | 备注。 |
| --runningCost | Float | 0.00 | 任务配置 ID。 |
| --runningCpu | Integer | 0 | 任务描述。 |
| --runningGpu | Integer | 0 | 压测任务 ID。 |
| -- runningGpuMe m | Integer | 0 | 任务名称。 |
| --runningMem | Integer | 0 | 任务主状态（ModelTaskStatus）。 |
| --runningPod | Integer | 0 | 注意：VO 字段名为 taskSubStatus，DO 字段为 subStatus，当前 BeanUtils 不会自动映射，通常为 null。 |
| --totalCost | Float | 0.00 | 实例成本信息（默认会给 0 值对象）。 |
| --totalCpu | Integer | 0 | 运行中成本。 |
| --totalGpu | Integer | 0 | 运行中 CPU。 |
| --totalGpuMem | Integer | 0 | 运行中 GPU。 |
| --totalMem | Integer | 0 | 运行中 GPU 显存。 |
| --totalPod | Integer | 0 | 运行中内存。 |
| - stressTestConf ig | Struct | - | 运行中 Pod 数。 |
| --aliyunUid | String | 1277********1314 | 累计成本。 |
| --configDesc | String | null | 累计 CPU。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --configId | String | null | 累计 GPU。 |
| --configName | String | null | 累计 GPU 显存。 |
| --configType | Integer | null | 累计内存。 |
| -- datasetConfig | String | {"datasetType":"R ANDOM","randomI nputLen":512,"ran domOutputLen":25 6,"randomRangeRa tio":0.0,"randomPr efixLen":0} | 累计 Pod 数。 |
| -- durationConfig | String | {"sampleCount":10 00} | 压测配置详情（部分字段当前实现可能为 null）。 |
| --extraConfig | String | {"burstiness":1.0,"r andomSeed":42} | 阿里云账号 UID。 |
| --gmtCreated | String | 2026-03- 05T03:00:00Z | 注意：当前实现未填充，通常为 null。 |
| --gmtModified | String | 2026-03- 05T03:05:00Z | 注意：当前 StressTestConfigVO.valueOf 未填充该字段，通常为 null。 |
| --modeConfig | String | {"stressMode":"FIX ED CONCURRENCY _ ","concurrencyNum ":32} | 注意：当前实现未填充，通常为 null。 |
| --regionId | String | cn-wulan-env38- d01 | 注意：当前实现未填充，通常为 null。 |
| success | Boolean | true | 数据集配置字符串；对应 StressBaseDatasetConfig 子类之一 （此处为 StressRandomDatasetConfig ）。 成功：true。 失败：false。 |
| errorCode | String | null | 压测时长配置字符串；对应 StressDurationConfig.sampleCount 。 |
| errorMessage | String | null | 额外配置字符串；对应 StressExtraConfig 。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| httpCode | Integer | 200 | 配置创建时间（UTC）。 |
| totalCount | Integer | 25 | 配置修改时间（UTC）。 |
| pageSize | Integer | 10 | 压测模式配置字符串；对应 StressBaseModeConfig 子类之一（此处为 StressFixedConcurrencyModeConfig ）。 |
| pageIndex | Integer | 1 | 地域 ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "pageIndex":1,
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"-",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### DeleteStressTestTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 否 | stt-**** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetStressTestTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | stt-**** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | null | 动态错误消息列表；成功时通常为 null。 |
| success | Boolean | true | 请求是否成功。 成功：true。 失败：false。 |
| errorCode | String | null | 错误码；成功时为 null。 |
| errorMessage | String | null | 错误信息；成功时为 null。 |
| httpCode | Integer | 200 | HTTP 状态码。 |
| data | Struct | - | 压测任务详情。 |
| - codeMountList | Array | null | 代码挂载列表；当前代码路径未填充，通常为 null。 |
| --codeId | String | null | 代码集id。 |
| --codeName | String | null | 代码集名称。 |
| -- codeRepoType | Integer | null | 源代码平台类型，取值： GITHUB 、 GITLAB 、 GITEE 、 CODE 、 CODEUP |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | PVC 名称。 |

|  | GITHUB |  |
|---|---|---|
| CODE |  |  |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - datasetMountL ist | Array | [{ "mountPath": "/root", "datasetId": "ds- 78b1242ffed14878 88af363a24***", "datasetType": 0, "dataSource": 1, "quotaId": "rq- d8890a98089c204 1d8086bb0b2e27f* **", "dataAccInstance": "da- df89s8f9sdfs99sae *****" }] | 数据集挂载列表。 |
| -- dataAccInstan ce | String | dataacc-i-011 | 数据加速实例标识。 |
| --dataType | Integer | 0 | 数据类型。 |
| -- datasetFileNa me | String | prompt- benchmark.jsonl | 文件名。 |
| --datasetId | String | ds-20260305001 | 数据集 ID。 |
| --datasetName | String | prompt-benchmark | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v2 | 数据集版本。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | PVC 名称。 |
| -metrics | Array | - | 指标列表（无指标时可能为 null）。 |
| --name | String | qps | 指标名称。 |
| --value | String | 123.45 | 指标值（字符串）。 |
| - modelMountLi st | Array | null | 模型挂载列表。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- dataAccInstan ce | String | dataacc-i-011 | 数据加速实例标识。 |
| --modelId | String | md-system- 7ed6f4208a44e87 8ce | 模型 ID。 |
| --modelName | String | Qwen3-4B | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | PVC 名称。 |
| --weightType | Integer | 0 | 权重类型。 |
| - nodeConfigList | Array | - | 节点配置列表。 |
| --cpuCount | Integer | 8 | CPU 核数。 |
| --gpuCount | Integer | 1 | GPU 卡数。 |
| -- gpuMemCount | Integer | 24 | GPU 显存规格。 |
| --memCount | Integer | 32 | 内存规格。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --nodeType | Integer | 0 | 节点类型。 |
| -- sharedMemCo unt | Integer | 4 | 共享内存规格。 |
| -- startCommand | String | python benchmark.py | 启动命令。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - storageMountL ist | Array | [{ "quotaId": "rq- d8890a98089c204 1d8086bb0b2e**** ", "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 存储挂载列表。 |
| --mountPath | String | /mnt/output/ | 容器内挂载路径。 |
| --pvcName | String | pvc-storage-st-001 | PVC 名称。 |
| --storagePath | String | oss://aipaas- bucket/stress- test/output/ | OSS 存储路径。 |
| -- storageSource | Integer | 1 | 存储来源类型。 |
| -aliyunUid | String | 1277********1314 | 阿里云账号 UID。 |
| -cpuCount | Integer | 8 | CPU 核数。 |
| -failedMsg | String | null | 失败信息；失败时可能有值。 |
| -gmtCreated | String | 2026-03- 05T03:00:00Z | 配置创建时间（UTC）。 |
| -gmtEnd | String | 2026-03- 05T06:35:20Z | 任务结束时间（UTC）。 |
| -gmtModified | String | 2026-03- 05T03:05:00Z | 配置修改时间（UTC）。 |
| -imageId | String | img-llm-stress | 镜像 ID。 |
| - imageIdAndVe rsion | String | img-llm-stress, v1.2.3 | getter 计算字段。 |
| -imageVersion | String | v1.2.3 | 镜像版本。 |
| -memCount | Integer | 32 | 内存规格。 |
| - onlineServiceI d | String | os- 698b8e19000da04 699 | 在线服务 ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -parentPlanId | String | plan-202603 | 父计划 ID。 |
| -quotaId | String | rq- 0635cf690bb0704b 1c | 资源配额 ID。 |
| -quotaName | String | A100 high net pool | 资源配额名称。 |
| -regionId | String | cn-wulan-env38- d01 | 地域 ID。 |
| -remark | String | auto schedule | 备注。 |
| -taskConfigId | String | cfg-st-001 | 任务配置 ID。 |
| -taskDesc | String | nightly stress test | 任务描述。 |
| -taskId | String | st-20260305-0003 | 压测任务 ID。 |
| -taskName | String | nightly-qwen3-4b | 任务名称。 |
| -taskStatus | Integer | 5 | 任务主状态（ModelTaskStatus）。 |
| - taskSubStatus | Integer | null | 注意：当前 VO/DO 字段名不一致，通常为 null。 |
| -instanceCost | Struct | 0 | 实例成本信息。 |
| --runningCost | Float | 0.00 | 运行中成本。 |
| --runningCpu | Integer | 0 | 运行中 CPU。 |
| --runningGpu | Integer | 0 | 运行中 GPU。 |
| -- runningGpuMe m | Integer | 0 | 运行中 GPU 显存。 |
| --runningMem | Integer | 0 | 运行中内存。 |
| --runningPod | Integer | 0 | 运行中 Pod 数。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --totalCost | Float | 0.00 | 累计成本。 |
| --totalCpu | Integer | 0 | 累计 CPU。 |
| --totalGpu | Integer | 0 | 累计 GPU。 |
| --totalGpuMem | Integer | 0 | 累计 GPU 显存。 |
| --totalMem | Integer | 0 | 累计内存。 |
| --totalPod | Integer | 0 | 累计 Pod 数。 |
| - stressTestConf ig | Struct | - | 压测配置详情。 |
| --aliyunUid | String | 1277********1314 | 阿里云账号 UID。 |
| --configDesc | String | null | 注意：当前实现未填充，通常为 null。 |
| --configId | String | null | 注意：当前 StressTestConfigVO.valueOf 未填充该字段，通常为 null。 |
| --configName | String | null | 注意：当前实现未填充，通常为 null。 |
| --configType | Integer | null | 注意：当前实现未填充，通常为 null。 |
| -- datasetConfig | String | {"datasetType":"R ANDOM","randomI nputLen":512,"ran domOutputLen":25 6,"randomRangeRa tio":0.0,"randomPr efixLen":0} | 数据集配置字符串；对应 StressBaseDatasetConfig 子类之一 （此处为 StressRandomDatasetConfig ）。 |
| -- durationConfig | String | {"sampleCount":10 00} | 压测时长配置字符串；对应 StressDurationConfig.sampleCount 。 |
| --extraConfig | String | {"burstiness":1.0,"r andomSeed":42} | 额外配置字符串；对应 StressExtraConfig 。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gmtCreated | String | 2026-03- 05T03:00:00Z | 配置创建时间（UTC）。 |
| --gmtModified | String | 2026-03- 05T03:05:00Z | 配置修改时间（UTC）。 |
| --modeConfig | String | {"stressMode":"FIX ED CONCURRENCY _ ","concurrencyNum ":32} | 压测模式配置字符串；对应 StressBaseModeConfig 子类之一（此处为 StressFixedConcurrencyModeConfig ）。 |
| --regionId | String | cn-wulan-env38- d01 | 地域 ID。 |

**示例**

请求示例

```
&taskId=stt-xxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 批量推理

#### CreateBatchInferenceJob

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /batch-inference-job/create HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobName | Strin g | Body | 是 | job-name | 任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | job-description | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| imageId | Strin g | Body | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| jobType | Integ er | Body | 否 | 0 | 任务类型，取值范围： 0：原生的job类型。 1：支持数据分片的 elasticBatch类型。 |
| startCom mand | Strin g | Body | 是 | python3 main.py | 启动命令，该参数必填。 |
| isSchedul ed | Boole an | Body | 否 | false | 是否定时运行，取值范围： true：是。 false：否。 默认值：false。 |
| scheduleT ime | Strin g | Body | 否 | 2025-04-16 00:00:00 | 定时启动时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| datasetMo untList | Json | Body | 否 | [{ "mountPath": "/root", "datasetId": "ds- 78b1242ffed1487888af3 63a24***", "dataAccInstance":"da- df89s8f9sdfs99sae*****" }] | 数据集配置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelMou ntList | Json | Body | 否 | [{ "modelId": "md- 7a5c75e10a95104e1d0 bd5804e0c346c****", "mountPath": "/root", "modelType": 1, "modelVersion": "v1", "dataAccInstance":"da- df89s8f9sdfs99sae*****" }] | 模型库配置。 |
| codeMoun tList | Json | Body | 否 | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046ec0bc ad0d3682****" }] | 代码集配置，可不填。 |
| storageMo untList | Json | Body | 否 | [{ "mountPath": "/root/", "storageSource": 1, "storagePath": "oss://****/****/" }] | 持久化存储设置。 |
| nodeConfi gList | Json | Body | 否 | [{ "memCount": 0, "nodeCount": 1, "gpuCount": 0, "cpuCount": 1 }] | 节点配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "jobId": "bi-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /batch-inference-job/create HTTP/1.1 { "jobName":"job-name", "imageId":"img-91fa01150ee51045190baa305e****", "imageVersion":"v1", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "startCommand":"python3 main.py" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"jobId\": \"bi-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetBatchInferenceJob

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchInfer enceJobId | Strin g | Query | 是 | bi- 2d4cd47b02c3c04f080a b5b0b***** | 批量推理任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds- 459f7a****c704db 1 | 数据集 ID。 |
| -- datasetVersion | String | v1 | 数据集版本号。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -- datasetFileNa me | String | data.csv | 数据集文件名称。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| -- dataAccInstan ce | String | acc-instance-001 | 数据加速实例标识。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --modelId | String | md-system- 56b1****44b04cb7 | 模型 ID。 |
| --modelName | String | llama2-7b | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本号。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| -- dataAccInstan ce | String | acc-instance-001 | 数据加速实例标识。 |
| --weightType | Integer | 0 | 权重类型。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |
| -- storageSource | Integer | 1 | 存储来源，枚举值：0-Local Import，1- OSS，2-CPFS，3-NAS，4-APFS。 |
| --storagePath | String | oss://shaobing- test.oss-cn- neimeng-****.com/ | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | 0 | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --cpuCount | Integer | 1 | CPU 核数。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --memCount | Integer | 1 | 内存大小，单位为 GB。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小，单位为 GB。 |
| -- gpuMemCount | Integer | -1 | GPU 显存大小，-1 表示不使用 GPU 显存。 |
| --gpuCount | Integer | 0 | GPU 卡数量。 |
| -- startCommand | String | echo "hello" | 启动命令。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --gmtCreated | String | 2025-12- 24T06:02:27Z | 创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| --gmtModified | String | 2026-02- 02T15:28:16Z | 修改时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| --aliyunUid | String | 198226****521225 | 阿里云账号 UID。 |
| --regionId | String | cn-neimeng-236e- d01 | 地域 ID。 |
| --storageId | String | ts- e42a68****b32040 03 | 第三方存储 ID。 |
| --occupantId | String | bi- 4517fb****304cdb | 资源 ID（在线服务、Notebook、任务建模、批量推理等）。 |
| -- storageSubPat h | String | /mnt/data/ | 存储子路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -gmtCreated | String | 2025-12- 24T06:02:27Z | 创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -gmtModified | String | 2026-02- 02T15:28:16Z | 修改时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -aliyunUid | String | 198226****521225 | 阿里云账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID。 |
| -failedMsg | String | task failed due to OOM | 任务失败原因信息。 |
| -jobId | String | bi- 4517fb****304cdb | 批量推理任务 ID。 |
| -jobName | String | shaobing-test | 批量推理任务名称。 |
| -description | String | 批量推理测试任务 | 批量推理任务描述信息。 |
| -jobStatus | Integer | 4 | 批量推理任务状态，枚举值：0-Waiting For Starting，1-Starting，2-Running，3- Stopped，4-Failed，5-Completed，6-In Queue，7-Stopping，8-Scheduled Waiting，9-Scaling。 |
| -imageId | String | img- 8cea87****50497f | 镜像 ID。 |
| -imageVersion | String | v3 arm _ | 镜像版本号。 |
| -imageName | String | pytorch-1.12 | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型，枚举值：0-PUBLIC（公共镜像），1-CUSTOM（自定义镜像）。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型，枚举值：0-IMAGE（普通镜像），1-ACCELERATED IMAGE（加速镜 _ 像）。 |
| -quotaId | String | rq- 40c8be****aa040a 9 | 资源配额 ID。 |
| -quotaName | String | default-quota | 资源配额名称。 |
| -jobType | Integer | 0 | 批量推理任务类型，枚举值：0-ORIGINAL（原生 job 类型），1- DATA SLICE ELASTIC BATCH（支持数据分 _ _ _ 片的 elasticBatch 类型）。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - jobNodesCoun t | Integer | 1 | 任务节点总数。 |
| - startCommand | String | echo "hello" | 启动命令。 |
| -nodeCount | Integer | 1 | 节点数量。 |
| -cpuCount | Integer | 1 | CPU 核数。 |
| -memCount | Integer | 1 | 内存大小，单位为 GB。 |
| - gpuMemCount | Integer | -1 | GPU 显存大小，-1 表示不使用 GPU 显存。 |
| - gpuLabelCoun t | Integer | 0 | GPU 虚拟化卡数量。 |
| -gpuCount | Integer | 0 | GPU 卡数量。 |
| -gpuMemTotal | Integer | 0 | GPU 显存总量，默认值为 0。 |
| -gpuCountUnit | Integer | 1 | GPU 数量单位。 |
| - gpuMemTotal Unit | Integer | 1 | GPU 显存总量单位。 |
| -gpuType | Integer | 0 | GPU 类型，枚举值：0-无 GPU，1-NVIDIA 或其他，2-K100（海光 DCU），3-910B（华为昇腾）。 |
| -gmtEnd | String | 2025-12- 24T06:10:00Z | 任务结束时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -isSchedule | Boolean | false | 是否为定时启动任务，默认值为 false。 |
| -scheduleTime | String | 2025-12- 25T00:00:00Z | 定时启动时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -instanceCost | Struct | [] | 实例费用统计信息。 |
| --runningCost | Float | 0.00 | 运行中实例的费用，保留两位小数。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --runningPod | Float | 0 | 运行中的 Pod 数量。 |
| --runningCpu | Float | 0 | 运行中的 CPU 使用量。 |
| --runningMem | Float | 0 | 运行中的内存使用量。 |
| --runningGpu | Float | 0 | 运行中的 GPU 使用量。 |
| -- runningGpuMe m | Float | 0 | 运行中的 GPU 显存使用量。 |
| --totalCost | Float | 0.00 | 总费用，保留两位小数。 |
| --totalPod | Float | 0 | 总 Pod 数量。 |
| --totalCpu | Float | 0 | 总 CPU 使用量。 |
| --totalMem | Float | 0 | 总内存使用量。 |
| --totalGpu | Float | 0 | 总 GPU 使用量。 |
| --totalGpuMem | Float | 0 | 总 GPU 显存使用量。 |

**示例**

请求示例

```
&batchInferenceJobId=bi-2d4cd47b02c3c04f080ab5b0b*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "scheduleTime":"",
  "gmtModified":"",
  "jobStatus":"",
  "quotaName":"",
  "storageMountList":[
   {
    "mountPath":"",
```

智能体工厂 OpenTrek

```json
    "pvcName":"",
    "storagePath":"",
    "storageSource":""
   }
```

`],`

```json
  "gmtCreated":"",
  "aliyunUid":"",
  "failedMsg":"",
  "description":"",
  "modelMountList":[
   {
    "modelName":"",
    "dataAccInstance":"",
    "weightType":"",
    "mountPath":"",
    "modelId":"",
    "pvcName":"",
    "modelVersion":"",
    "modelType":""
   }
```

`],`

```json
  "thirdpartyStorageMountList":[
   {
    "gmtModified":"",
    "mountPath":"",
    "storageSubPath":"",
    "gmtCreated":"",
    "aliyunUid":"",
    "regionId":"",
    "occupantId":"",
    "storageId":""
   }
```

`],`

```json
  "gmtEnd":"",
  "nodeCount":"",
  "jobType":"",
  "imageType":"",
  "gpuCount":"",
  "cpuCount":"",
  "gpuType":"",
  "jobName":"",
  "imageVersion":"",
  "memCount":"",
  "imageId":"",
  "imageName":"",
  "nodeConfigList":[
   {
    "memCount":"",
    "sharedMemCount":"",
    "gpuMemCount":"",
    "nodeCount":"",
    "startCommand":"",
    "nodeType":"",
    "gpuCount":"",
```

"

```
t"""
```

智能体工厂 OpenTrek

```json
    "cpuCount":""
   }
```

`],`

```json
  "gpuMemCount":"",
  "instanceCost":{
   "runningPod":"",
   "runningMem":"",
   "runningGpuMem":"",
   "totalCpu":"",
   "totalPod":"",
   "totalMem":"",
   "runningGpu":"",
   "totalGpuMem":"",
   "runningCost":"",
   "runningCpu":"",
   "totalCost":"",
   "totalGpu":""
  },
  "quotaId":"",
  "startCommand":"",
  "gpuMemTotal":"",
  "gpuLabelCount":"",
  "jobId":"",
  "regionId":"",
  "gpuMemTotalUnit":"",
  "datasetMountList":[
   {
    "dataAccInstance":"",
    "datasetVersion":"",
    "mountPath":"",
    "pvcName":"",
    "dataType":"",
    "datasetName":"",
    "datasetId":"",
    "datasetFileName":"",
    "datasetType":""
   }
```

`],`

```json
  "jobNodesCount":"",
  "gpuCountUnit":"",
  "imageAccelerationType":"",
  "isSchedule":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteBatchInferenceJob

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchInfer enceJobId | Strin g | Query | 是 | bi- 2d4cd47b02c3c04f080a b5b0b***** | 批量推理任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&batchInferenceJobId=bi-2d4cd47b02c3c04f080ab5b0b*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateBatchInferenceJob

调用UpdateBatchInferenceJob修改指定批量推理任务的部分信息，包括推理任务名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /batch-inference-job/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchInfer enceJobId | Strin g | Body | 是 | bi- 2d4cd47b02c3c04f080a b5b0***** | 批量推理任务ID，该参数必填。 |
| jobName | Strin g | Body | 是 | batchInference-name | 批量推理任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| descriptio n | Strin g | Body | 否 | batchInference-desc | 批量推理描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| scheduleT ime | Strin g | Body | 否 | 2024-11-21 00:00:00 | 定时启动时间。 |
| isSchedul ed | Boole an | Body | 否 | false | 是否开启定时任务，取值范围： true：是。 false：否。 默认值：false。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /batch-inference-job/update HTTP/1.1 { "batchInferenceJobId":"bi-2d4cd47b02c3c04f080ab5b0*****", "jobName":"batchInference-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListBatchInferenceJob

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 批量推理任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| jobId | Strin g | Query | 否 | job-6538214103685**** | 任务ID。 |
| jobName | Strin g | Query | 否 | job-name | 任务名称。 |
| jobStatus | Integ er | Query | 否 | 0 | 任务状态，取值范围： 0：待启动。 1：启动中。 2：运行中。 3：已停止。 4：失败。 5：完成。 6：排队中。 7：停止中。 8：定时等待。 9：变配中。 |
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| quotaNam e | Strin g | Query | 否 | quota-name | 资源配额名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Query | 否 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |
| imageNa me | Strin g | Query | 否 | image-name | 镜像名称。 |
| modelId | Strin g | Query | 否 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型仓库名称。 |
| datasetId | Strin g | Query | 否 | ds- 3dc49fc087b3491cafa76 b5d842**** | 数据集ID。 |
| datasetNa me | Strin g | Query | 否 | dataset-name | 数据集名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds- 459f7a****c704db 1 | 数据集 ID。 |
| -- datasetVersion | String | v1 | 数据集版本号。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- datasetFileNa me | String | data.csv | 数据集文件名称。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| -- dataAccInstan ce | String | acc-instance-001 | 数据加速实例标识。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |
| --modelId | String | md-system- 56b1****44b04cb7 | 模型 ID。 |
| --modelName | String | llama2-7b | 模型名称。 |
| --modelType | Integer | 0 | 模型类型。 |
| -- modelVersion | String | v1.0 | 模型版本号。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| -- dataAccInstan ce | String | acc-instance-001 | 数据加速实例标识。 |
| --weightType | Integer | 0 | 权重类型。 |
| - codeMountList | Array | [] | 代码库挂载列表。 |
| --codeId | String | cd- 2e0ceb****60e04d 24 | 代码库 ID。 |
| --codeName | String | inference-code | 代码库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |

| OpenTr | ek |  | AI Studio ·API |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |
| -- storageSource | Integer | 1 | 存储来源，枚举值：0-Local Import，1- OSS，2-CPFS，3-NAS，4-APFS。 |
| --storagePath | String | oss://shaobing- test.oss-cn- neimeng-****.com/ | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | pvc-storage-001 | PVC 持久卷声明名称。 |
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | 0 | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数量。 |
| --cpuCount | Integer | 1 | CPU 核数。 |
| --memCount | Integer | 1 | 内存大小，单位为 GB。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小，单位为 GB。 |
| -- gpuMemCount | Integer | -1 | GPU 显存大小，-1 表示不使用 GPU 显存。 |
| --gpuCount | Integer | 0 | GPU 卡数量。 |
| -- startCommand | String | echo "hello" | 启动命令。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --gmtCreated | String | 2025-12- 24T06:02:27Z | 创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gmtModified | String | 2026-02- 02T15:28:16Z | 修改时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| --aliyunUid | String | 198226****521225 | 阿里云账号 UID。 |
| --regionId | String | cn-neimeng-236e- d01 | 地域 ID。 |
| --storageId | String | ts- e42a68****b32040 03 | 第三方存储 ID。 |
| --occupantId | String | bi- 4517fb****304cdb | 资源 ID（在线服务、Notebook、任务建模、批量推理等）。 |
| -- storageSubPat h | String | /mnt/data/ | 存储子路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -gmtCreated | String | 2025-12- 24T06:02:27Z | 创建时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -gmtModified | String | 2026-02- 02T15:28:16Z | 修改时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -aliyunUid | String | 198226****521225 | 阿里云账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID。 |
| -failedMsg | String | task failed due to OOM | 任务失败原因信息。 |
| -jobId | String | bi- 4517fb****304cdb | 批量推理任务 ID。 |
| -jobName | String | shaobing-test | 批量推理任务名称。 |
| -description | String | 批量推理测试任务 | 批量推理任务描述信息。 |
| -jobStatus | Integer | 4 | 批量推理任务状态，枚举值：0-Waiting For Starting，1-Starting，2-Running，3- Stopped，4-Failed，5-Completed，6-In Queue，7-Stopping，8-Scheduled Waiting，9-Scaling。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageId | String | img- 8cea87****50497f | 镜像 ID。 |
| -imageVersion | String | v3 arm _ | 镜像版本号。 |
| -imageName | String | pytorch-1.12 | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型，枚举值：0-PUBLIC（公共镜像），1-CUSTOM（自定义镜像）。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型，枚举值：0-IMAGE（普通镜像），1-ACCELERATED IMAGE（加速镜 _ 像）。 |
| -quotaId | String | rq- 40c8be****aa040a 9 | 资源配额 ID。 |
| -quotaName | String | default-quota | 资源配额名称。 |
| -jobType | Integer | 0 | 批量推理任务类型，枚举值：0-ORIGINAL（原生 job 类型），1- DATA SLICE ELASTIC BATCH（支持数据分 _ _ _ 片的 elasticBatch 类型）。 |
| - jobNodesCoun t | Integer | 1 | 任务节点总数。 |
| - startCommand | String | echo "hello" | 启动命令。 |
| -nodeCount | Integer | 1 | 节点数量。 |
| -cpuCount | Integer | 1 | CPU 核数。 |
| -memCount | Integer | 1 | 内存大小，单位为 GB。 |
| - gpuMemCount | Integer | -1 | GPU 显存大小，-1 表示不使用 GPU 显存。 |
| - gpuLabelCoun t | Integer | 0 | GPU 虚拟化卡数量。 |
| -gpuCount | Integer | 0 | GPU 卡数量。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gpuMemTotal | Integer | 0 | GPU 显存总量，默认值为 0。 |
| -gpuCountUnit | Integer | 1 | GPU 数量单位。 |
| - gpuMemTotal Unit | Integer | 1 | GPU 显存总量单位。 |
| -gpuType | Integer | 0 | GPU 类型，枚举值：0-无 GPU，1-NVIDIA 或其他，2-K100（海光 DCU），3-910B（华为昇腾）。 |
| -gmtEnd | String | 2025-12- 24T06:10:00Z | 任务结束时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -isSchedule | Boolean | false | 是否为定时启动任务，默认值为 false。 |
| -scheduleTime | String | 2025-12- 25T00:00:00Z | 定时启动时间，格式为 yyyy-MM- dd'T'HH:mm:ss'Z'，时区为 UTC。 |
| -instanceCost | Struct | [] | 实例费用统计信息。 |
| --runningCost | Float | 0.00 | 运行中实例的费用，保留两位小数。 |
| --runningPod | Float | 0 | 运行中的 Pod 数量。 |
| --runningCpu | Float | 0 | 运行中的 CPU 使用量。 |
| --runningMem | Float | 0 | 运行中的内存使用量。 |
| --runningGpu | Float | 0 | 运行中的 GPU 使用量。 |
| -- runningGpuMe m | Float | 0 | 运行中的 GPU 显存使用量。 |
| --totalCost | Float | 0.00 | 总费用，保留两位小数。 |
| --totalPod | Float | 0 | 总 Pod 数量。 |
| --totalCpu | Float | 0 | 总 CPU 使用量。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --totalMem | Float | 0 | 总内存使用量。 |
| --totalGpu | Float | 0 | 总 GPU 使用量。 |
| --totalGpuMem | Float | 0 | 总 GPU 显存使用量。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 批量推理任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 任务的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### CreateInferenceResultStorageTask

调用CreateInferenceResultStorageTask创建批量推理结果任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /batch-inference-job/result-storage/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | Strin g | Body | 是 | task-name | 任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | desc | 任务描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| resourceId | Strin g | Body | 否 | bi- 46085f2a0778f0433909 623080d***** | 资源ID。 |
| sourceBuc ket | Strin g | Body | 否 | oss://******/ | 源bucket。 |
| importFile sJson | Strin g | Body | 否 | oss://*****/test.jsonl | 导入文件。 |
| targetBuc ket | Strin g | Body | 否 | oss://******/ | 目标bucket。 |
| storagePa th | Strin g | Body | 否 | oss://******/ | 存储路径。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "taskId": "*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /batch-inference-job/result-storage/create HTTP/1.1 { "taskName":"task-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"taskId\": \"*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetInferenceResultStorageTask

调用GetInferenceResultStorageTask查询指定保存批量推理结果任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
GET /batch-inference-job/result-storage/get HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | f131977106bd7049840a 3bf0***** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -completedList | Array | [] | 已完成的文件记录列表，包含每个已导入文件的详细信息。 |
| --importFile | String | oss://shaobing- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/router-test- report/stt- **************** re _ sult.json | 已导入的文件完整 OSS 路径。 |
| --fileSize | String | 1007 | 文件大小，单位为字节。 |
| -gmtCreated | String | 2025-12- 25T03:39:14Z | 任务创建时间，格式为 UTC 时间。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtModified | String | 2025-12- 25T03:39:14Z | 任务最后修改时间，格式为 UTC 时间。 |
| -aliyunUid | String | 1982**********521 225 | 阿里云账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，标识任务所在的区域。 |
| -taskId | String | ab6e3ac7********* *********553c12a | 推理结果存储任务的唯一标识 ID。 |
| -taskStatus | Integer | 4 | 任务状态枚举值。枚举值如下： - 0 - CREATED：已创建 - 1 - RUNNING：运行中 - 2 - STOP：已停止 - 3 - FAILED：失败 - 4 - COMPLETE：已完成。 |
| -taskName | String | ffff | 任务名称。 |
| -description | String | null | 任务描述信息。 |
| -resourceId | String | bi- 4517fb********04c db | 关联的批量推理任务资源 ID。 |
| -sourceBucket | String | shaobing-test | 源 OSS Bucket 名称，即推理结果文件所在的存储桶。 |
| - importFilesJso n | String | ["oss://shaobing- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/router-test- report/stt- **************** re _ sult.json"] | 需要导入的文件列表，JSON 数组格式，每个元素为 OSS 文件完整路径。 |
| -targetBucket | String | jieran-test | 目标 OSS Bucket 名称，即存储结果的目标存储桶。 |
| -storagePath | String | oss://jieran- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/ | 目标存储路径，即文件存储到目标 Bucket 的完整 OSS 路径。 |
| -totalFilesNum | Integer | 1 | 需要存储的文件总数。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - currentFileNu m | Integer | 1 | 当前已完成存储的文件数量。 |
| -gmtEnd | String | 2025-12- 25T03:39:15Z | 任务结束时间，格式为 UTC 时间。 |
| -errorMsg | String | null | 任务执行错误信息，任务成功时为 null。 |

**示例**

请求示例

```
GET /batch-inference-job/result-storage/get HTTP/1.1 &taskId=f131977106bd7049840a3bf0*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyBatchInferenceJobStatus

调用ModifyBatchInferenceJobStatus修改指定批量推理任务的状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /batch-inference-job/modify-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchInfer enceJobId | Strin g | Body | 是 | bi- 46085f2a0778f0433909 6230***** | 批量推理任务ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobStatus | Boole an | Body | 否 | false | 批量推理任务状态，取值范围： true：启用。 false：禁用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /batch-inference-job/modify-status HTTP/1.1 { "batchInferenceJobId":"bi-46085f2a0778f04339096230*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyBatchInferenceJobSpec

智能体工厂 OpenTrek 调用ModifyBatchInferenceJobSpec修改指定批量推理任务的配额信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /batch-inference-job/modify-spec HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| batchInfer enceJobId | Strin g | Body | 是 | bi- 46085f2a0778f0433909 623***** | 批量推理任务ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| gpuMemC ount | Integ er | Body | 否 | 0 | 显存大小，单位为GB。 |
| gpuCount | Integ er | Body | 是 | 1 | gpu大小，单位为卡，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
PUT /batch-inference-job/modify-spec HTTP/1.1 { "batchInferenceJobId":"bi-46085f2a0778f0433909623*****", "cpuCount":"1", "memCount":"1", "gpuCount":"1" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListInferenceResultStorageTask

调用ListInferenceResultStorageTask查询批量推理结果保存任务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /batch-inference-job/result-storage/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 批量推理保存任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | 2aaaab085c004d60085 360b1c2fs9***** | 任务ID。 |
| resourceId | Strin g | Query | 是 | bi- 46085f2a0778f0433909 62308***** | 资源ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -completedList | Array | [] | 已完成的文件记录列表，包含每个已导入文件的详细信息。 |
| --importFile | String | oss://shaobing- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/router-test- report/stt- **************** re _ sult.json | 已导入的文件完整 OSS 路径。 |
| --fileSize | String | 1007 | 文件大小，单位为字节。 |
| -gmtCreated | String | 2025-12- 25T03:39:14Z | 任务创建时间，格式为 UTC 时间。 |
| -gmtModified | String | 2025-12- 25T03:39:14Z | 任务最后修改时间，格式为 UTC 时间。 |
| -aliyunUid | String | 1982**********521 225 | 阿里云账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，标识任务所在的区域。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskId | String | ab6e3ac7********* *********553c12a | 推理结果存储任务的唯一标识 ID。 |
| -taskStatus | Integer | 4 | 任务状态枚举值。枚举值如下： - 0 - CREATED：已创建 - 1 - RUNNING：运行中 - 2 - STOP：已停止 - 3 - FAILED：失败 - 4 - COMPLETE：已完成。 |
| -taskName | String | ffff | 任务名称。 |
| -description | String | null | 任务描述信息。 |
| -resourceId | String | bi- 4517fb********04c db | 关联的批量推理任务资源 ID。 |
| -sourceBucket | String | shaobing-test | 源 OSS Bucket 名称，即推理结果文件所在的存储桶。 |
| - importFilesJso n | String | ["oss://shaobing- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/router-test- report/stt- **************** re _ sult.json"] | 需要导入的文件列表，JSON 数组格式，每个元素为 OSS 文件完整路径。 |
| -targetBucket | String | jieran-test | 目标 OSS Bucket 名称，即存储结果的目标存储桶。 |
| -storagePath | String | oss://jieran- test.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/ | 目标存储路径，即文件存储到目标 Bucket 的完整 OSS 路径。 |
| -totalFilesNum | Integer | 1 | 需要存储的文件总数。 |
| - currentFileNu m | Integer | 1 | 当前已完成存储的文件数量。 |
| -gmtEnd | String | 2025-12- 25T03:39:15Z | 任务结束时间，格式为 UTC 时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -errorMsg | String | null | 任务执行错误信息，任务成功时为 null。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 批量推理保存任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 批量推理保存任务的页码。 |

**示例**

请求示例

```
GET /batch-inference-job/result-storage/list HTTP/1.1 &resourceId=bi-46085f2a0778f043390962308*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

### 模型广场

智能体工厂 OpenTrek

#### CreateModel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /model/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 否 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |
| modelNa me | Strin g | Body | 是 | model-name | 模型名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| modelDes c | Strin g | Body | 否 | model-desc | 模型描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| modelTyp e | Integ er | Body | 否 | 1 | 模型类型，取值范围： 0：公共模型。 1：自定义模型。 默认值：1。 |
| frameWor k | Integ er | Body | 是 | 1 | 框架类型，该参数必填，取值范围： 1：Tensorflow。 2：PyTorch。 |
| modelVer sion | Strin g | Body | 是 | v1 | 模型版本号，该参数必填。 |
| modelSou rce | Integ er | Body | 是 | 1 | 导入方式，该参数必填，取值范围： 0：训练任务导入。 1：云存储。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelStat us | Boole an | Body | 否 | false | 模型启用状态，取值范围： false：禁用。 true：启用。 默认值：false。 |
| taskType | Integ er | Body | 否 | 1 | 训练类型，取值范围： 0：notebook建模。 1：任务建模。 2：可视化建模。 |
| taskId | Strin g | Body | 否 | tk- d74ab7fb043a5041d509 36e050ef5*** | 任务建模ID。 |
| taskJobId | Strin g | Body | 否 | c1638f85-eb22-4670- a7e7-c42bf***** | 训练任务JobID。 |
| storageSo urce | Integ er | Body | 是 | 1 | 存储类型，该参数必填，取值范围： 0：LOCAL。 1：OSS。 |
| storagePa th | Strin g | Body | 是 | oss://****/**** | 存储路径，该参数必填。 |
| modelCat egoryIds | Json | Body | 否 | [1002,2002,3003] | 模型类型、模型用途、模型厂商ID列表。 当id为“1XXX”时，表示模型类型（可多传），取值范围：[1002,1017]; 当id为“2XXX”时，表示模型用途（可多传），取值范围：[2002,2016]; 当id为“3XXX”时，表示模型厂商，取值范围： [3002,3008]; |
| weightTyp e | Integ er | Body | 否 | 0 | 是否为Lora权重模型，取值范围： 0：否 1：是 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelFeat ureMetaC onfigs | Json | Body | 否 | [ { "title": "基础模型", "code": "base model", _ "content": "Qwen3-32B", "placeholder": "" }, { "title": "function call", "code": "support function call", _ _ "content": "Enable", "placeholder": "" }, { "code": "support structured out _ _ put", "title": "结构化输出", "content": "Enable", "placeholder": "" } | 模型特性信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "modleId": "md- ****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /model/create HTTP/1.1 { "modelName":"model-name", "frameWork":"1", "modelVersion":"v1", "modelSource":"1", "storageSource":"1", "storagePath":"oss://****/****" }
```

智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":"{     \"modleId\": \"md-****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteModel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Query | 是 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&modelId=md-e97c65da0d70b04f2b0bbcb057d9s****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetModel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Query | 是 | md-4cd57e****3042c1 | 模型唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -gmtCreated | String | 2025-11- 07T03:16:38Z | 模型创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-11- 07T03:16:38Z | 模型最后修改时间，格式为UTC时间。 |
| -modelId | String | md- 4cd57e****3042c1 | 模型唯一标识ID。 |
| -modelName | String | Qwen3-VL-8B- Instruct | 模型名称。 |
| -modelType | Integer | 1 | 模型类型，枚举值如下： - 0 ：SYSTEM（系统模型） - 1 ：CUSTOM（自定义模型） - 2 ：MODEL GALLERY（模型广场模型）。 _ |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| - systemModelA lreadyInstall | Boolean | 0 | 系统模型已否安装。 |
| -versionCount | Integer | 1 | 模型版本总数。 |

**示例**

请求示例

```
&modelId=md-e97c65da0d70b04f2b0bbcb057d9s****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "versionCount":1,
  "modelName":"Qwen3-VL-8B-Instruct",
  "gmtModified":"2025-11-07T03:16:38Z",
  "aliyunUid":"19822605****1225",
  "gmtCreated":"2025-11-07T03:16:38Z",
  "modelId":"md-4cd57e****3042c1",
  "regionId":"cn-neimeng-236e-d01",
  "systemModelAlreadyInstall":false,
  "modelType":1
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListModel

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型仓库列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| modelTyp e | Integ er | Query | 否 | 1 | 模型类型，枚举值如下： - 0 ：SYSTEM（系统模型） - 1 ：CUSTOM（自定义模型） - 2 ： MODEL GALLERY（模型 _ 广场模型）。 0：公共模型。 1：自定义模型。 |
| modelId | Strin g | Query | 否 | md-4cd57e****3042c1 | 模型唯一标识ID。 |
| modelNa me | Strin g | Query | 否 | Qwen3-VL-8B-Instruct | 模型名称。 |
| frameWor k | Integ er | Query | 否 | 1 | 框架类型，取值范围： 1：Tensorflow。 2：PyTorch。 |
| modelStat us | Boole an | Query | 否 | true | 模型启用状态，取值范围： true：启用。 false：停止。 |
| taskType | Strin g | Query | 否 | image-text-to-text | modelType为2时，用于筛选模型的任务分类。 |
| subTaskTy pe | Strin g | Query | 否 | action-detection | modelType为2时，用于筛选模型的子任务分类。 |
| libraries | Json | Query | 否 | gguf,llamafile | modelType为2时，用于筛选模型的框架。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - SecurityLevelT ag | String | 公开 | 表示密级。 |
| - SecurityLevelT agBackground Coler | String | #46d72e | 表示密级的标签背景色。 |
| - SecurityLevelT agTextColer | String | #46d72e | 密级标签文字颜色。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -docId | String | doc-xxxx****xxxx | 模型关联的文档ID。 |
| -gmtCreated | String | 2025-11- 07T03:16:38Z | 模型创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-11- 07T03:16:38Z | 模型最后修改时间，格式为UTC时间。 |
| -latestVersion | String | v1.0 | 模型最新版本号。 |
| -modelId | String | md- 4cd57e****3042c1 | 模型唯一标识ID。 |
| -modelName | String | Qwen3-VL-8B- Instruct | 模型名称。 |
| -modelType | Integer | 1 | 模型类型，枚举值如下： - 0 ：SYSTEM（系统模型） - 1 ：CUSTOM（自定义模型） - 2 ：MODEL GALLERY（模型广场模型）。 _ |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -metadata | String | {"Name":"Qwen3- VL-8B-Instruct"} | 模型元数据信息，JSON格式字符串。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -serviceStatus | Integer | 0 | 模型部署状态，枚举值如下： - 0 ：NO DEPLOYMENT（未部署） _ - 1 ：DEPLOYING（部署中） - 2 ：DEPLOYED（部署成功） - 3 ：FAILED（部署失败）。 |
| -shared | Integer | 1 | 模型共享范围。 |
| - systemModelA lreadyInstall | Boolean | 1 | 系统模型在当前环境中是否安装。 已安装：1。 未安装：0。 |
| -versionCount | Integer | 3 | 模型版本总数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 模型仓库的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 模型仓库的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "versionCount":3,
   "SecurityLevelTag":"公开",
   "shared":1,
   "gmtModified":"2025-11-07T03:16:38Z",
   "metadata":"{\"Name\":\"Qwen3-VL-8B-Instruct\"}",
   "SecurityLevelTagTextColer":"#46d72e",
   "aliyunUid":"19822605****1225",
   "gmtCreated":"2025-11-07T03:16:38Z",
   "modelId":"md-4cd57e****3042c1",
   "docId":"doc-xxxx****xxxx",
   "systemModelAlreadyInstall":false,
   "modelType":1,
   "modelName":"Qwen3-VL-8B-Instruct",
   "latestVersion":"v1.0",
   "regionId":"cn-neimeng-236e-d01",
   "serviceStatus":0,
   "SecurityLevelTagBackgroundColer":"#46d72e"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ListModelSelection

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型选择列表的页码。 默认值：1。 |

| A | I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| modelId | Strin g | Query | 否 | md-55a2ab****fd04ca0 | 模型版本关联的模型ID。 |
| modelVer sion | Strin g | Query | 否 | v1.0 | 模型版本号。 |
| frameWor k | Integ er | Query | 否 | 2 | 模型框架类型，枚举值如下： - 1 ：TENSOR FLOW _ - 2 ：PY TORCH _ - 3 ：ELASTIC BATCH _ - 4 ：XG BOOST _ - 5 ：ONE FLOW _ - 6 ：MPI JOB _ - 7 ：JOB - 8 ：MODEL CONVERT _ - 10 ：DEEPSPEED - 11 ：MEGATRON - 12 ： PADDLE PADDLE _ - 13 ：MIND SPORE。 _ 1：TENSOR FLOW。 _ 2：PY TORCH。 _ 3：ELASTIC BATCH。 _ 4：XG BOOST。 _ 5：ONE FLOW。 _ 6：MPI JOB。 _ 7：JOB。 8： MODEL CONVERT。 _ 10：DEEPSPEED。 11：MEGATRON。 12： PADDLE PADDLE。 _ 13：MIND SPORE。 _ |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelStat us | Boole an | Query | 否 | true | 模型版本状态，true为启用，false为禁用。 false：禁用。 true：启用。 默认值：false。 |
| modelTyp e | Integ er | Query | 是 | 1 | 模型类型，取值范围： 0：公共模型。 1：自定义模型。 |
| modelCat egoryIds | Json | Query | 否 | [1] | 模型类别ID列表。 当id为“1XXX”时，表示模型类型（可多传），取值范围：[1002,1017]; 当id为“2XXX”时，表示模型用途（可多传），取值范围：[2002,2016]; 当id为“3XXX”时，表示模型厂商，取值范围： [3002,3008]; |
| weightTyp e | Integ er | Query | 否 | 0 | 模型权重类型，枚举值如下： - 0 ：Basic（基础模型， 可直接用于训练/推理/微调） - 1 ：Lora（Lora微调后模型，用于多Lora部署）。 0：否 1：是 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - modelCategor yIds | List | 1 | 模型类别ID列表。 |

| I Studio · | API |  | OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - modelManufac turer | List | 0 | 模型厂商ID列表。 |
| -modelUsage | List | 0 | 模型用途ID列表。 |
| - modelFeature MetaConfigs | Array | [ModelFeatureMeta Config] | 模型特性元数据配置列表，元素为 ModelFeatureMetaConfig对象。 |
| --code | String | base model _ | 模型类型代码。 |
| --content | String | Qwen3-30B-A3B | 模型名称。 |
| --placeholder | String | **** | 占位符信息。 |
| --title | String | 基础模型 | 模型大类。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -dataAccCount | Integer | 0 | 数据加速计数。 |
| -frameWork | Integer | 2 | 模型框架类型，枚举值如下： - 1 ：TENSOR FLOW _ - 2 ：PY TORCH _ - 3 ：ELASTIC BATCH _ - 4 ：XG BOOST _ - 5 ：ONE FLOW _ - 6 ：MPI JOB _ - 7 ：JOB - 8 ：MODEL CONVERT _ - 10 ：DEEPSPEED - 11 ：MEGATRON - 12 ：PADDLE PADDLE _ - 13 ：MIND SPORE。 _ |
| -gmtCreated | String | 2025-11- 18T07:27:22Z | 模型版本创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-11- 18T07:27:22Z | 模型版本最后修改时间，格式为UTC时间。 |
| -modelId | String | md- 55a2ab****fd04ca 0 | 模型版本关联的模型ID。 |
| -modelSize | Float | 0.0 | 模型文件大小，单位为GB。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -modelSource | Integer | 1 | 模型来源类型，枚举值如下： - 0 ：TASK IMPORT（任务导入） _ - 1 ：CLOUD IMPORT（云端导入） _ - 2 ：LOCAL UPLOAD（本地上传）。 _ |
| -modelStatus | Boolean | true | 模型版本状态，true为启用，false为禁用。 |
| -modelVersion | String | v1.0 | 模型版本号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -storagePath | String | oss://zhic.oss-cn- neimeng-****-d01- a.env236.ops.arm. com/model/Qwen3- VL-8B-Instruct/ | 模型文件存储路径。 |
| - storageSource | Integer | 1 | 存储来源类型，枚举值如下： - 0 ：LOCAL - 1 ：OSS - 2 ：CPFS - 3 ：NAS - 4 ：APFS - 5 ：S3 - 10 ：THIRD PARTY。 _ |
| -weightType | Integer | 0 | 模型权重类型，枚举值如下： - 0 ：Basic（基础模型，可直接用于训练/推理/微调） - 1 ：Lora（Lora微调后模型，用于多Lora部署）。 |
| -importStatus | Integer | 4 | 模型导入状态，枚举值如下： - 0 ：CREATED（已创建） - 1 ：RUNNING（运行中） - 2 ：STOP（已停止） - 3 ：FAILED（失败） - 4 ：COMPLETE（完成）。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&modelType=1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "frameWork":2,
   "importStatus":4,
   "modelManufacturer":0,
   "gmtModified":"2025-11-18T07:27:22Z",
   "modelSource":1,
   "aliyunUid":"19822605****1225",
   "gmtCreated":"2025-11-18T07:27:22Z",
   "modelId":"md-55a2ab****fd04ca0",
   "modelStatus":true,
   "modelVersion":"v1.0",
   "modelCategoryIds":1,
   "storagePath":"oss://zhic.oss-cn-neimeng-****-d01-a.env236.ops.arm.com/model/Qwen3-V
L-8B-Instruct/",
   "modelSize":0.0,
   "modelFeatureMetaConfigs":[
    {
     "code":"base_model",
     "placeholder":"****",
```

`"title":"`基础模型`",`

```json
     "content":"Qwen3-30B-A3B"
    }
```

`],`

```json
   "weightType":0,
   "modelUsage":0,
   "dataAccCount":0,
   "regionId":"cn-neimeng-236e-d01",
   "storageSource":1
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyModel

调用ModifyModel修改指定模型仓库的部分信息，包括模型仓库名称、描述和版本号。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /model/modify HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 是 | md- e97c65da0d70b04f2b0b bcb0574**** | 模型仓库ID，该参数必填。 |
| modelNa me | Strin g | Body | 是 | model-name | 模型仓库名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| modelDes c | Strin g | Body | 否 | model-desc | 模型仓库描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| sourceMo delVersion | Strin g | Body | 否 | v2 | 源模型仓库版本号。 |
| modelVer sion | Strin g | Body | 否 | v1 | 模型仓库版本号。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /model/modify HTTP/1.1 { "modelId":" md-e97c65da0d70b04f2b0bbcb0574****", "modelName":"model-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyModelStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /model/modify-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 是 | md- e97c65da0d70b04f2b0b bcb0574**** | 模型仓库ID，该参数必填。 |
| modelVer sion | Strin g | Body | 是 | v1 | 模型仓库版本，该参数必填。 |
| modelStat us | Boole an | Body | 是 | true | 模型仓库状态，该参数必填，取值范围： true：启用。 false：禁用。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /model/modify-status HTTP/1.1 { "modelId":"md-e97c65da0d70b04f2b0bbcb0574****", "modelVersion":"v1", "modelStatus":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteModelVersion

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Query | 是 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |
| modelVer sion | Strin g | Query | 是 | v1 | 模型仓库版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&modelId=md-e97c65da0d70b04f2b0bbcb057d9s**** &modelVersion=v1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### ListModelFiles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizati on | Strin g | Query | 是 | 1 | 组织ID。 |
| modelNa me | Strin g | Query | 是 | model-name | 模型仓库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
&organization=1 &modelName=model-name
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetModelLineage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Query | 是 | md-sd9au8safusd***** | 模型仓库ID。 |
| modelVer sion | Strin g | Query | 是 | v1 | 模型仓库版本号。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - modelMountLi st | Array | [ModelMountVO] | 模型挂载列表，元素为ModelMountVO对象。 |
| --modelType | Integer | 0 | 模型类型，取值范围： 0：系统模型。 1：自定义模型。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -gmtCreated | String | 2026-02- 09T11:14:37Z | 创建时间，格式为UTC时间。 |
| -gmtModified | String | 2026-03- 02T15:55:03Z | 最后修改时间，格式为UTC时间。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -resourceType | Integer | 32 | 资源类型，枚举值如下： 31：TASK NOTEBOOK（交互式建模） _ 32：TASK JOB（任务建模） _ 38：FINETUNE（模型调优） 22：ASSET MODEL（模型库）。 _ |

**示例**

请求示例

```
&modelId=md-sd9au8safusd***** &modelVersion=v1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "gmtModified":"2026-03-02T15:55:03Z",
  "aliyunUid":"19822605****1225",
  "gmtCreated":"2026-02-09T11:14:37Z",
  "regionId":"cn-neimeng-236e-d01",
  "modelMountList":[
   {
    "modelType":0
   }
```

`],`

```json
  "resourceType":32
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyModelCategory

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /model/category/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 是 | md-sd9au8safusd***** | 模型仓库ID，该参数必填。 |
| modelVer sion | Strin g | Body | 否 | v1 | 模型仓库版本号。 |
| categoryI dList | Json | Body | 否 | ["1001", "1002", "1003"] | 模型仓库分类ID集合。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /model/category/modify HTTP/1.1 { "modelId":"md-sd9au8safusd*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyModelVersionComponent

调用ModifyModelVersionComponent修改指定模型版本关联的组件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 是 | md- e97c65da0d70b0457d9s **** | 模型ID，该参数必填。 |
| modelVer sion | Strin g | Body | 是 | v1.0 | 模型版本，该参数必填。 |
| inference Compone ntIdList | Json | Body | 否 | [ "cp-sdfafhygg", "cp- d21bec77ef324" ] | 推理套件列表，最多50个。 |
| trainComp onentIdLis t | Json | Body | 否 | [ "cp-sdfafhygg", "cp- d21bec77ef324" ] | 训练套件列表，最多50个。 |
| quantCom ponentIdLi st | Json | Body | 否 | [ "cp-sdfafhygg", "cp- d21bec77ef324" ] | 量化套件列表，最多50个。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
{ "modelId":"md-e97c65da0d70b0457d9s****
```

`",`

```json
"modelVersion":"v1.0" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetModelAccessInfo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Query | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - agentModelApi key | String | sk-**** | 访问模型服务的Api-Key。 |
| - agentModelEn dpoint | String | https://api.example .com/v1/agents | 用于调用智能体模型服务的HTTP REST API端点地址，支持创建、查询、调用和管理AI智能体实例。 |
| - agentModelNa me | String | Qwen2.5 | 访问模型的名称。 |
| -serviceId | String | os-xxxxx | 模型关联的在线服务ID。 |

**示例**

请求示例

```
&serviceId=os-d20bd45d0683a047a60b5f50f8b52****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "agentModelName":"Qwen2.5",
  "agentModelEndpoint":"https://api.example.com/v1/agents",
  "serviceId":"os-xxxxx",
  "agentModelApikey":"sk-****"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### 模型导出

##### ListModelImportTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型任务列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | 6836****bfee | 导入任务的唯一标识符，用于查询和管理任务。 |
| resourceId | Strin g | Query | 是 | ft-c****43ad | 资源ID，关联的模型资源标识。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -completedList | Array | ["task1", "task2", "task3"] | 表示已成功完成的任务列表，通常为字符串数组，每个元素代表一个已完成的具体任务项。 |
| --fileSize | String | 2782602 | 文件大小。 |
| --importFile | String | example.xlsx | 指定要导入的文件名。 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |
| - currentFileNu m | Integer | 3 | 当前正在处理的文件序号。 |
| -frameWork | Integer | 1 | 模型框架。 |
| -gmtCreated | String | 1606791494471 | 创建时间。 |
| -gmtEnd | String | 1667205617089 | 结束时间。 |
| -gmtModified | String | 1703575553000 | 修改时间。 |
| - importFilesJso n | String | ["oss://*****.oss- ****/*****.pdf"] | 导入文件。 |
| -modelId | String | model- rbvg5wzljz****ks92 | 模型ID。 |
| -modelName | String | test | 模型名称。 |
| -modelStatus | Boolean | 1 | 模型状态。 |
| -modelVersion | String | v1 | 模型版本号。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -resourceId | String | 1 | 资源ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -saveModel | Boolean | true | 指示是否将训练好的模型保存到指定路径。 |
| -sourceBucket | String | ***-bucket | 源bucket。 |
| -storagePath | String | http://xxxxx.jpg | 存储路径。 |
| -targetBucket | String | target-bucket | 目标bucket。 |
| -taskId | String | t-000000000001 | 任务ID。 |
| -taskStatus | Integer | 1 | 任务状态。 |
| -totalFilesNum | Integer | 5 | 表示当前目录或任务中总共包含的文件数量。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 标准任务的页码。 |

**示例**

请求示例

```
&resourceId=nb-73e3ed200e9fe048d208f3e086****
```

&公共请求参数正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":[
  {
   "frameWork":1,
   "gmtModified":"1703575553000",
   "resourceId":"1",
   "aliyunUid":"127756******1314",
   "gmtCreated":"1606791494471",
   "modelId":"model-rbvg5wzljz****ks92",
   "modelStatus":false,
   "modelVersion":"v1",
   "storagePath":"http://xxxxx.jpg",
   "completedList":[
    {
     "fileSize":"2782602",
     "importFile":"example.xlsx"
    }
```

`],`

```json
   "sourceBucket":"***-bucket",
   "modelName":"test",
   "importFilesJson":"[\"oss://*****.oss-****/*****.pdf\"]",
   "currentFileNum":3,
   "gmtEnd":"1667205617089",
   "regionId":"cn-hangzhou",
   "saveModel":true,
   "targetBucket":"target-bucket",
   "totalFilesNum":5,
   "taskId":"t-000000000001",
   "taskStatus":1
  }
```

`],`

```json
 "pageIndex":1,
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

`XML` 格式智能体工厂 OpenTrek

```xml
<data>
 <frameWork  />
 <gmtModified  />
 <resourceId  />
 <aliyunUid  />
 <gmtCreated  />
 <modelId  />
 <modelStatus  />
 <modelVersion  />
 <storagePath  />
 <completedList>
  <fileSize  />
  <importFile  />
 </completedList>
 <sourceBucket  />
 <modelName  />
 <importFilesJson  />
 <currentFileNum  />
 <gmtEnd  />
 <regionId  />
 <saveModel  />
 <targetBucket  />
 <totalFilesNum  />
 <taskId  />
 <taskStatus  />
</data> <pageIndex>1</pageIndex> <success>true</success> <dynamicMessages>[]</dynamicMessages> <errorMessage>&quot;&quot;</errorMessage> <errorCode>500</errorCode> <pageSize>10</pageSize> <httpCode>200</httpCode> <totalCount>100</totalCount>
```

##### CreateModelImportTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /model/import/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceId | Strin g | Body | 是 | tk- cf3df8ea09acf0410008c e10d00***** | 资源ID，该参数必填。 |
| sourceBuc ket | Strin g | Body | 是 | ***-bucket | 源bucket，该参数必填。 |
| importFile sJson | Strin g | Body | 是 | ["oss://*****.oss- ****/*****.pdf"] | 导入文件，该参数必填。 |
| modelId | Strin g | Body | 否 | md-sd9au8safusd***** | 模型仓库ID。 |
| modelNa me | Strin g | Body | 是 | model-name | 模型名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| modelDes c | Strin g | Body | 否 | model-desc | 模型描述，描述长度为 2~256个字符，不能以 http://和https://开头。 |
| frameWor k | Integ er | Body | 是 | 1 | 模型框架，该参数必填，取值范围： 1：Tensorflow。 2：PyTorch。 |
| modelStat us | Boole an | Body | 否 | false | 模型启用状态，取值范围： true：启用。 false：禁用。 默认值：false。 |
| modelVer sion | Strin g | Body | 是 | v1.0 | 模型版本号，该参数必填， 版本号支持：vx.x格式(例如 v1.0)。 |
| targetBuc ket | Strin g | Body | 是 | ****-bucket | 目标bucket，该参数必填。 |
| storagePa th | Strin g | Body | 是 | oss://****.oss-****/****/ | 存储路径，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| docName | Strin g | Body | 否 | doc-name | 文档名称，Readme文档若选择立即配置，该参数不能为空，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| docVersio n | Strin g | Body | 否 | v1.0 | 文档版本，Readme文档若选择立即配置，该参数不能为空，版本号支持：vx.x格式(例如v1.0)。 |
| docUrl | Strin g | Body | 否 | https://****.oss- ****/****.pdf | 文档保存路径，Readme文档若选择立即配置，该参数不能为空。 |
| weightTyp e | Integ er | Body | 否 | 0 | 是否为Lora权重模型，取值范围： 0：否 1：是 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "modelId": "md- ****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /model/import/create HTTP/1.1 { "resourceId":"tk-cf3df8ea09acf0410008ce10d00*****", "sourceBucket":"***-bucket", "importFilesJson":"["oss://*****.oss-****/*****.pdf"]", "modelName":"model-name", "frameWork":"1", "modelVersion":"v1.0", "targetBucket":"****-bucket", "storagePath":"oss://****.oss-****/****/" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\t\"modelId\": \"md-****\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetModelImportTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | tk- 5103add0062e20452c8 0383***** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -completedList | Array | [{""importFile"":""/ path/to/file"" | fileSize"":""100MB""}],已完成文件的记录列表，包含文件路径和文件大小。 |
| --fileSize | String | 2048MB | 已完成导入的文件大小。 |
| --importFile | String | /path/to/model.bin | 已完成导入的文件路径。 |
| -aliyunUid | String | 1982****1225 | 阿里云主账号 ID，用于标识任务的所有者。 |
| - currentFileNu m | Integer | 5 | 当前已完成导入的文件数量。 |
| -frameWork | Integer | 2 | 模型框架类型，取值范围：1-TensorFlow、2- PyTorch、3-ElasticBatch、4-XGBoost、5- OneFlow、6-MPI Job、7-Job、8-Model Convert、10-DeepSpeed、11-Megatron、 12-PaddlePaddle、13-MindSpore。 |
| -gmtCreated | String | 2025-11-19 02:58:32.0 | 任务创建时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| -gmtEnd | String | 2025-11-19 02:58:34.0 | 任务结束时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| -gmtModified | String | 2025-11-19 02:58:34.0 | 任务最后修改时间，格式为 yyyy-MM-dd HH:mm:ss。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - importFilesJso n | String | ["oss://yhtest.oss- cn-neimeng-236e- d01- a.env236.ops.arm. com/images/added tokens.json","oss:/ _ /yhtest.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/images/args.js on","oss://yhtest.os s-cn-neimeng- 236e-d01- a.env236.ops.arm. com/images/gener ation config.json"," _ oss://yhtest.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/images/chat t _ emplate.jinja","oss: //yhtest.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/images/config. json"] | 导入文件列表的 JSON 字符串，包含文件名和大小等信息。 |
| -modelId | String | md-e****445b | 模型 ID，导入完成后生成的模型唯一标识。 |
| -modelName | String | Qwen3-VL-8B- Instruct | 模型名称，用户自定义的模型标识。 |
| -modelStatus | Boolean | true | 模型状态，true 表示启用，false 表示停止。 |
| -modelVersion | String | v2.0 | 模型版本号，标识模型的版本信息。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，表示任务所属的地域。 |
| -resourceId | String | ft-c****43ad | 资源 ID，关联的模型资源标识。 |
| -saveModel | Boolean | true | 是否保存模型，true 表示保存，false 表示不保存。 |
| -sourceBucket | String | yhtest | 源 OSS Bucket 名称，存储待导入模型的存储空间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -storagePath | String | oss://zhic.oss-cn- neimeng-236e- d01- a.env236.ops.arm. com/ | 模型在 OSS 中的存储路径。 |
| -targetBucket | String | zhic | 目标 OSS Bucket 名称，导入完成后模型存储的存储空间。 |
| -taskId | String | 6836****bfee | 导入任务的唯一标识符，用于查询和管理任务。 |
| -taskStatus | Integer | 4 | 任务状态，取值范围：0-已创建、1-运行中、2- 已停止、3-失败、4-完成。 |
| -totalFilesNum | Integer | 5 | 需要导入的文件总数。 |

**示例**

请求示例

```
&taskId=tk-5103add0062e20452c80383*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "frameWork":"",
  "gmtModified":"",
  "resourceId":"",
  "aliyunUid":"",
  "gmtCreated":"",
  "modelId":"",
  "modelStatus":"",
  "modelVersion":"",
  "storagePath":"",
  "completedList":[
   {
    "fileSize":"",
    "importFile":""
   }
```

`],`

```json
  "sourceBucket":"",
  "modelName":"",
  "importFilesJson":"",
  "currentFileNum":"",
  "gmtEnd":"",
  "regionId":"",
  "saveModel":"",
  "targetBucket":"",
  "totalFilesNum":"",
  "taskId":"",
  "taskStatus":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### MaaS市场

##### ListModelGallery

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/model-gallery/listModelGallery HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jsonParam | Strin g | Query | 是 | { "pageSize": 30, "pageNumber": 1, "sortBy": "Default", "target": "", "criterion": [], "singleCriterion": [] } | json参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
GET /model/model-gallery/listModelGallery HTTP/1.1 &jsonParam={
 "pageSize": 30,
 "pageNumber": 1,
 "sortBy": "Default",
 "target": "",
 "criterion": [],
 "singleCriterion": []
}
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"[{}]",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetModelGalleryDetails

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/model-gallery/[organization]/[modelName] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizati on | Strin g | Path | 是 | 1 | 组织ID。 |
| modelNa me | Strin g | Path | 是 | model-name | 模型仓库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /model/model-gallery/[organization]/[modelName] HTTP/1.1 &organization=1 &modelName=model-name
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListModelGalleryCategory

调用ListModelGalleryCategory查询MaaS市场模型类型列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/model-gallery/listModelGalleryCategory HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | Integ er | Query | 否 | 1 | 模型任务分类的范围，取值范围： 1 ：获取ModelScope上的原始模型任务分类数据列表 2 ：基于本地已同步模型的元数据获取的任务分类数据列表 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /model/model-gallery/listModelGalleryCategory HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DownloadModelGallery

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /model/model-gallery/download HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 否 | annotation-name | 数据标注任务名称。 |
| path | Strin g | Body | 否 | /test | 文件夹路径。 |
| metadata | Json | Body | 否 | ** | 节点元数据。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
POST /model/model-gallery/download HTTP/1.1 { }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetModelGalleryConnectionStatus

调用GetModelGalleryConnectionStatus查询模型广场常驻连接状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/model-gallery/getConnectionStatus HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - networkStatus | Integer | 0 | 网络访问状态，取值范围：0-不通外网、1-通外网。 |
| -podId | String | mg-p****4fdb | Pod 的唯一标识符。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -podStatus | Integer | 1 | Pod 的运行状态。 |

**示例**

请求示例

```
GET /model/model-gallery/getConnectionStatus HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
 "data":{
  "podStatus":1,
  "networkStatus":0,
  "podId":"mg-p****4fdb"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### UpdateModelGalleryConnectionStatus

调用UpdateModelGalleryConnectionStatus修改模型广场连接状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/model-gallery/updateConnectionStatus HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| status | Strin g | Query | 是 | open | 集群状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /model/model-gallery/updateConnectionStatus HTTP/1.1 &status=open
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 模型体验

##### StreamChat

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os- d20bd45d0683a047a60 b5f50f8b52**** | 在线服务ID，该参数必填。 |
| model | Strin g | Body | 是 | gpt-4 | 模型型号，该参数必填。 |
| messages | Json | Body | 是 | ["Hello", "How are you?", "See you later"] | 消息，该参数必填。 |
| temperatu re | Float | Body | 否 | 0.7 | 随机性控制。 默认值：0.7。 |
| maxToken s | Integ er | Body | 否 | 100 | 生成文本的最大长度。 |
| top p _ | Float | Body | 否 | 0.3 | top p，取值范围为 _ （0,1.0]。 生成过程中的采样方法概率阈值，取值越大，生成的随机性越高。 |
| presence _ penalty | Float | Body | 否 | 0 | 重复度，取值范围 [-2.0, 2.0]。 用户控制模型生成时整个序列中的重复度，提高 presence penalty时可以 _ 降低模型生成的重复度。 |
| enable thi _ nking | Boole an | Body | 否 | false | 深度思考。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "serviceId":"os-d20bd45d0683a047a60b5f50f8b52****", "model":"gpt-4", "messages":"["Hello", "How are you?", "See you later"]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"draftId\": \"draft-575011c0045fd0*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetAigcGenerationResult

调用GetAigcGenerationResult查询指定任务多模态生成结果信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /model/aigcGeneration/getTaskResult HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 否 | 0385dc79-5ff8-4d82- ***** | 多模态生成任务ID。 |
| serviceId | Strin g | Query | 否 | os-edbe708a0b5f**** | 在线服务ID。 |
| model | Strin g | Query | 否 | wan2.2-t2i-flash | served-model-name。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 200 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -output | Struct | {} | 返回信息。 |
| --code | String | InvalidParameter | 响应码。 |
| --message | String | The size is not match xxxxxx | 错误信息。 |
| --task id _ | String | 0385dc79-5ff8- 4d82-bcb6-xxxxxx | 任务ID。 |
| --task status _ | String | FAILED | 任务状态。 |

**示例**

请求示例智能体工厂 OpenTrek

```
GET /model/aigcGeneration/getTaskResult HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"200",
 "httpCode":200
}
```

##### CreateAigcGenerationTask

调用CreateAigcGenerationTask创建多模态生成请求，目前支持文生图|文生视频|图生图|图生视频。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceId | Strin g | Body | 是 | os-edbe708a0b5f5**** | 在线服务ID，该参数必填。 |
| modelCat egoryId | Integ er | Body | 是 | 1014 | 模型类型ID，该参数必填。 |
| model | Strin g | Body | 是 | wan2.2-t2i-flash | served-model-Name，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| input | Json | Body | 是 | 文生图 \| 文生视频： { "prompt": "雪地，白色小教堂，极光，冬日场景，柔和的光线。", "negative prompt": "人 _ 物" } 图生图： { "prompt": "雪地，白色小教堂，极光，冬日场景，柔和的光线。", "negative prompt": "人 _ 物", "images": "http://xxx/6000000001 295-2-tps-1104- 1472.png", "http://xxx/6000000003 082-2-tps-1696- 960.png" } 图生视频： { "prompt": "雪地，白色小教堂，极光，冬日场景，柔和的光线。", "negative prompt": "人 _ 物", "img url": _ "https://xxx/wanx-demo- 1.png" } | 输入的基本信息，如提示词等，该参数必填。 |
| parameter s | Json | Body | 是 | 图生图 \| 文生图 { "size": "1024*1024", "n": 1 } 文生视频 \| 图生视频： { "size": "1024*1024", "duration": 10 } | 处理参数。如设置图像分辨率、生成图片数量、视频时长等，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "output": { "taskstatus": "PENDING", "taskid": "0385d82-****" } } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 200 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
{ "serviceId":"os-edbe708a0b5f5****", "modelCategoryId":"1014", "model":"wan2.2-t2i-flash",
```

`"input":"`文生图 | 文生视频： `{ "prompt": "`雪地，白色小教堂，极光，冬日场景，柔和的光线。`", "negat`

```
ive_prompt": "人物" }
```

图生图： `{ "prompt": "`雪地，白色小教堂，极光，冬日场景，柔和的光线。`", "negative_prompt": "`人

```
物", "images": "http://xxx/6000000001295-2-tps-1104-1472.png", "http://xxx/6000000003082-2-tps-1696-960.png" }
```

图生视频： `{ "prompt": "`雪地，白色小教堂，极光，冬日场景，柔和的光线。`", "negative_prompt": "`人物

```json
", "img_url": "https://xxx/wanx-demo-1.png" }", "parameters":"图生图 | 文生图 { "size": "1024*1024", "n": 1 }
```

文生视频 | 图生视频： `{ "size": "1024*1024", "duration": 10 }"`

```
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{       \"output\": {              \"taskstatus\": \"PENDING\",
\"taskid\": \"0385d82-****\" } }",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"200",
 "httpCode":200
}
```

### 模型调优

#### CreateFinetune

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /finetune/create HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneN ame | Strin g | Body | 是 | finetune-name | 模型调优名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| finetuneD esc | Strin g | Body | 否 | finetune-desc | 模型调优描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| gpuCount | Integ er | Body | 是 | 1 | gpu大小，单位为卡，该参数必填。 资源池开启GPU虚拟化特性时，gpuCount取值为- 1，GPU资源由 gpuMemCount和 gpuLabelCount决定。 |
| gpuMemC ount | Integ er | Body | 否 | 10 | 资源池开启GPU虚拟化特性情况下的显存数。 未开启GPU虚拟化时填- 1，GPU卡数将取 gpuCount参数。 |
| gpuLabelC ount | Integ er | Body | 否 | 2 | 资源池开启GPU虚拟化特性情况下的显存卡数。未开启 GPU虚拟化时填-1，GPU卡数将取gpuCount参数。 |
| modelSou rce | Integ er | Body | 是 | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelId | Strin g | Body | 是 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID，该参数必填。 |
| modelVer sion | Strin g | Body | 是 | v1 | 模型仓库版本，该参数必填。 |
| modelTyp e | Strin g | Body | 否 | 1 | 模型仓库类型，当 modelSource为1时，该参数不能为空。 |
| modelMou nt | Strin g | Body | 否 | /mnt/model | 模型挂载点，当 modelSource=为时默认/mnt/model，modelSo urce为0或2时拼接模型名称。 |
| dataAccIn stance | Strin g | Body | 否 | "" | 数据加速器。 |
| storagePa th | Strin g | Body | 是 | oss://****/**** | 存储路径，该参数必填。 |
| storageMo unt | Strin g | Body | 是 | /mnt/output | 持久化挂载点，该参数必填。 |
| finetuneM ethod | Integ er | Body | 否 | 0 | 模型调优方法，取值范围： 0：监督微调。 1：dpo直接偏好优化。 2：ppo近端策略优化。 3：DeepSeek GRPO 组间策略优化。 4：ByteDance DAPO 解耦裁剪和动态采样策略优化。 |
| parameter Range | Integ er | Body | 否 | 1 | 模型调优参数范围，取值范围： 0：全参微调。 1：ora部分参数微调。 2：qlora部分参数微调。 |
| learningR ate | Float | Body | 是 | 5e-6 | 学习率，该参数必填。 默认值：5e-6。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| numEpoch | Integ er | Body | 是 | 2 | 训练轮数，该参数必填。 默认值：2。 |
| maxLengt h | Integ er | Body | 是 | 1024 | 序列最大长度，该参数必填。 默认值：1024。 |
| perDevice TrainBatc hSize | Integ er | Body | 是 | 2 | 单设备训练批大小，该参数必填。 默认值：2。 |
| gradientA ccumulati onStep | Integ er | Body | 是 | 2 | 梯度累加步数，该参数必填。 默认值：2。 |
| loraRank | Integ er | Body | 否 | 8 | lora秩值。 默认值：8。 |
| loraAlpha | Integ er | Body | 否 | 16 | lora缩放系数。 默认值：16。 |
| loraDropo ut | Float | Body | 否 | 0 | lora丢弃率，取值范围0-1 之间。 默认值：0。 |
| lorapLrRat io | Integ er | Body | 否 | 16 | lora+学习率。 默认值：16。 |
| temperatu re | Float | Body | 否 | 0.9 | 温度参数，取值范围0.1- 2.0之间。 默认值：0.9。 |
| datasetMo untList | Json | Body | 是 | [{ "mountPath": "/mnt/****" }] | 数据集挂载信息，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | { "finetuneId": "ft- ******" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /finetune/create HTTP/1.1 { "finetuneName":"finetune-name", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "cpuCount":"1", "memCount":"1", "gpuCount":"1", "modelSource":"1", "modelId":"md-e97c65da0d70b04f2b0bbcb057d9s****", "modelVersion":"v1", "storagePath":"oss://****/****", "storageMount":"/mnt/output", "learningRate":"5e-6", "numEpoch":"2", "maxLength":"1024", "perDeviceTrainBatchSize":"2", "gradientAccumulationStep":"2", "datasetMountList":" [{
 "mountPath": "/mnt/****"
}]" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{      \"finetuneId\": \"ft-******\"}",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListFinetune

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型调优列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| finetuneId | Strin g | Query | 否 | ft- 729c6c1e030cc04d970a 10f097***** | 模型调优ID。 |
| finetuneN ame | Strin g | Query | 否 | finetune-name | 模型调优名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneSt atus | Integ er | Query | 否 | 0 | 模型调优状态，取值范围： 0：待启动。 1：启动中。 2：调优中。 3：已停止。 4：调优失败。 5：调优成功。 6：排队中。 7：停止中。 |
| finetuneM ethod | Integ er | Query | 否 | 1 | 模型调优方法，取值范围： 0：监督微调。 1：dpo直接偏好优化。 2：ppo近端策略优化。 3：DeepSeek GRPO 组间策略优化。 4：ByteDance DAPO 解耦裁剪和动态采样策略优化。 |
| parameter Range | Integ er | Query | 否 | 0 | 模型调优参数范围，取值范围： 0：全参微调。 1：ora部分参数微调。 2：qlora部分参数微调。 |
| modelId | Strin g | Query | 否 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型仓库名称。 |
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| quotaNam e | Strin g | Query | 否 | quota-name | 资源配额名称。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - codeMountList | Array | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" }] | 代码集配置。 |
| --codeId | String | cd- f1bb797e0cef2046 ec0bcad0d3682*** * | 代码集ID |
| --codeName | String | name | 代码集名称 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| - datasetMountL ist | Array | [{ "datasetId": "ds- 5740734ff2cf4a00 bc6da*****", "mountPath": "/data" }] | 数据集配置。 |
| --dataType | Integer | 0 | 数据类型 。 |
| --datasetId | String | ds- 8aefd872048140xx xx | 数据集ID。 |
| --datasetName | String | DatasetName | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 16 | CPU总核数。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -finetuneId | String | ft- 729c6c1e030cc04d 970a10f097***** | 模型调优ID。 |
| - finetuneMetho d | Integer | 0 | 模型调优方法，取值范围： 0：监督微调。 1：dpo直接偏好优化。 2：ppo近端策略优化。 3：DeepSeek GRPO 组间策略优化。 4：ByteDance DAPO 解耦裁剪和动态采样策略优化。 |
| -finetuneName | String | finetune-name | 模型调优名称， |
| - finetuneStatus | Integer | 0 | 模型调优状态，取值范围： 0：待启动。 1：启动中。 2：调优中。 3：已停止。 4：调优失败。 5：调优成功。 6：排队中。 7：停止中。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指1块物理 GPU或1个GPU实例 |
| - gpuLabelCoun t | Integer | 1 | 申请到的gpuMemCount显存，平均分配GPU卡数，GPU虚拟化时开启。例如申请显存为 gpuMemCount=8 ，申请卡数为 gpuLabelCount=2 ，表示申请2张GPU 卡，每张卡分配4份显存。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gpuMemTotal | Integer | 16384 | Maximum GPU memory capacity in MB |
| - gpuMemTotal Unit | Integer | 1 | 表示GPU显存总容量的单位，通常以 GB（Gigabytes）为单位显示 |
| -gpuType | Integer | 0 | GPU显卡类型。 |
| -imageId | String | img- 05cefd0be2exxxx | 镜像ID。 |
| -imageVersion | String | V1 | 镜像版本。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| -modelMount | String | /mnt/model | 模型挂载点 |
| -modelName | String | model-name | 模型名称 |
| -modelSource | Integer | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |
| -modelVersion | String | v1 | 模型仓库版本号。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| - parameterRan ge | Integer | 1 | 模型调优参数范围，取值范围： 0：全参微调。 1：ora部分参数微调。 2：qlora部分参数微调。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | quota-name | 配额名称。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| -storageMount | String | /mnt/output | 持久化挂载点 |
| -storagePath | String | oss://****/**** | 存储路径 |
| -subStatus | Integer | 0 | 子状态 |
| - instanceCostV O | Struct | {} | 实例消耗 |
| --runningCost | Float | 500 | 运行总消耗 |
| --runningCpu | Integer | 100 | 运行消耗的CPU总量 |
| --runningGpu | Integer | 2 | 运行消耗的GPU总量 |
| -- runningGpuMe m | Integer | 12582912 | 当前GPU正在被进程占用的显存大小（单位： MB） |
| --runningMem | Integer | 128 | 表示当前应用程序或进程正在使用的物理内存大小 |
| --runningPod | Integer | 2 | 运行中的pod数量 |
| --totalCost | Float | 129.99 | 任务运行总消耗 |
| --totalCpu | Float | 10 | 运行消耗的总cpu数 |
| --totalGpu | Integer | 10 | 运行消耗的总GPU数 |
| --totalGpuMem | Integer | 16106127360 | 运行消耗的总显存数 |
| --totalMem | Float | 10 | 总内存 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --totalPod | Integer | 3 | 总Pod |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 模型调优的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 模型调优的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### UpdateFinetuneStatus

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /finetune/update-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneId | Strin g | Body | 是 | ft- 729c6c1e030cc04d970a ***** | 模型调优ID，该参数必填。 |
| finetuneSt atus | Boole an | Body | 是 | false | 是否启用模型调优状态，该参数必填，取值范围： true：是。 false：否。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /finetune/update-status HTTP/1.1 { "finetuneId":"ft-729c6c1e030cc04d970a*****", "finetuneStatus":"false" }
```

正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteFinetune

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneId | Strin g | Query | 是 | ft- 729c6c1e030cc04d970a 10f097***** | 模型调优ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```
&finetuneId=ft-729c6c1e030cc04d970a10f097*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyFinetune

调用ModifyFinetune修改指定模型调优的部分信息，包括模型调优名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /finetune/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneId | Strin g | Body | 是 | ft- 729c6c1e030cc04d970a 10f09***** | 模型调优ID，该参数必填。 |
| finetuneN ame | Strin g | Body | 是 | finetune-name | 模型调优名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| finetuneD esc | Strin g | Body | 否 | finetune-desc | 模型调优描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /finetune/modify HTTP/1.1 { "finetuneId":"ft-729c6c1e030cc04d970a10f09*****", "finetuneName":"finetune-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetFinetune

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| finetuneId | Strin g | Query | 是 | ft- 729c6c1e030cc04d970a 10f***** | 模型调优ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - codeMountList | Array | [{ "mountPath": "/root/", "codeId": "cd- f1bb797e0cef2046 ec0bcad0d3682*** *" }] | 代码集配置。 |
| --codeId | String | cd- f1bb797e0cef2046 ec0bcad0d3682*** * | 代码集ID。 |
| --codeName | String | name | 代码集名称。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| - componentInp uts | Array | {} | 套件入参。 |
| --code | String | code | 套件Code。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| --datasetId | String | ds- rbvg5*****jhc9ks9 2 | 数据集ID。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --sourceType | String | 1 | 源数据的类型。 |
| - componentOut puts | Array | {} | 套件输出。 |
| --sourceType | String | 1 | 源数据的类型。 |
| --storagePath | String | oss://****/**** | 存储路径。 |
| - componentPar ams | Array | {} | 套件参数。 |
| --code | String | code | 套件Code。 |
| --defaultValue | String | default1 | 默认值。 |
| --description | String | testDescription | 指标描述。 |
| --name | String | nametest | 指标名称。 |
| --type | String | 1 | 指标类型 |
| --value | String | 0.5 | 指标值。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - datasetMountL ist | Array | [{ "mountPath": "/root", "datasetId": "ds- 78b1242ffed14878 88af363a24***", "datasetType": 0, "dataSource": 1, "quotaId": "rq- d8890a98089c204 1d8086bb0b2e27f* **", "dataAccInstance": "da- df89s8f9sdfs99sae *****" }] | 数据集配置。 |
| --dataType | Integer | 0 | 数据类型 。 |
| --datasetId | String | ds- rbvg5*****jhc9ks9 2 | 数据集ID。 |
| --datasetName | String | DatasetName | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --mountPath | String | /tmp | 容器挂载路径。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -componentId | String | cp-0696083a*** | 组件ID。 |
| - componentNa me | String | component name _ | 组件名称。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -finetuneId | String | ft- 729c6c1e030cc04d 970a10f097***** | 模型调优ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - finetuneMetho d | Integer | 0 | 模型调优方法，取值范围： 0：监督微调。 1：dpo直接偏好优化。 2：ppo近端策略优化。 3：DeepSeek GRPO 组间策略优化。 4：ByteDance DAPO 解耦裁剪和动态采样策略优化。 |
| -finetuneName | String | finetune-name | 模型调优名称。 |
| - finetuneStatus | Integer | 0 | 模型调优状态，取值范围： 0：待启动。 1：启动中。 2：调优中。 3：已停止。 4：调优失败。 5：调优成功。 6：排队中。 7：停止中。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| -gmtModified | String | 2017-11- 27T08:51:26Z | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指单个GPU 设备。 |
| - gpuLabelCoun t | Integer | 1 | 申请到的GpuMemCount显存，平均分配GPU 卡数，GPU虚拟化时开启。例如申请显存为 GpuMemCount=8 ，申请卡数为 GpuLabelCount=2 ，表示申请2张GPU 卡，每张卡分配4份显存。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| -gpuMemTotal | Integer | 16384 | 运行消耗的GPU总量。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - gpuMemTotal Unit | Integer | 1 | 表示GPU总显存容量的计量单位，通常以 GB（吉字节）为单位显示。 |
| -gpuType | Integer | 0 | GPU显卡类型。 |
| -imageId | String | img- 05cefd0be2exxxx | 镜像ID。 |
| -imageVersion | String | v1 | 镜像版本。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| -modelMount | String | /mnt/model | 模型挂载点。 |
| -modelName | String | name | 模型名称。 |
| -modelSource | Integer | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |
| -modelVersion | String | v1 | 模型仓库版本号。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| - parameterRan ge | Integer | 1 | 模型调优参数范围，取值范围： 0：全参微调。 1：ora部分参数微调。 2：qlora部分参数微调。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | quota-name | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| -sourceType | Integer | 1 | 源数据的类型。 |
| - startCommand | String | python3 main.py | 启动命令。 |
| -storageMount | String | /mnt/output | 持久化挂载点。 |
| -storagePath | String | oss://****/**** | 存储路径。 |
| -subStatus | Integer | 0 | 任务子状态。 |
| - instanceCostV O | Struct | {} | 任务实例消耗。 |
| --runningCost | Float | 500 | 任务运行消耗。 |
| --runningCpu | Integer | 1 | 任务消耗的Cpu数。 |
| --runningGpu | Integer | 1 | 运行中任务占用的GPU核数。 |
| -- runningGpuMe m | Integer | 12582912 | 当前GPU显存中正在被运行中的进程实际占用的显存大小（单位：字节）。 |
| --runningMem | Integer | 128 | 表示当前系统中正在运行的进程所占用的物理内存大小。 |
| --runningPod | Integer | 0 | 运行中任务的Pod数目。 |
| --totalCost | Float | 150.75 | 任务总消耗。 |
| --totalCpu | Float | 10 | 任务消耗的总Cpu。 |
| --totalGpu | Integer | 10 | 任务消耗的总Gpu。 |
| --totalGpuMem | Integer | 8589934592 | 任务消耗的总GPU显存。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --totalMem | Float | 10 | 任务消耗的总内存。 |
| --totalPod | Integer | 3 | 任务消耗的总Pod数。 |

**示例**

请求示例

```
&finetuneId=ft-729c6c1e030cc04d970a10f*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 模型工坊

#### 模型量化

##### GetQuantize

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quantizeId | Strin g | Query | 是 | qt- 729c6c1e030cc04d970a 10f***** | 模型量化ID。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| -gmtModified | String | 2017-11- 27T08:51:26Z | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指1块物理 GPU卡。 |
| - gpuLabelCoun t | Integer | 1 | 申请到的GpuMemCount显存，平均分配GPU 卡数，GPU虚拟化时开启。例如申请显存为 GpuMemCount=8 ，申请卡数为 GpuLabelCount=2 ，表示申请2张GPU 卡，每张卡分配4份显存。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| -gpuMemTotal | Integer | 16384 | 显卡总显存容量。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - gpuMemTotal Unit | Integer | 1 | 表示GPU显存总容量的单位，通常以GB（吉字节）为单位显示。 |
| -gpuType | Integer | 0 | GPU显卡类型。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| -modelSource | Integer | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| -quantizeId | String | qt-12345xxxxxx | 用于标识量化模型或量化配置的唯一整数ID，便于在训练、推理或模型管理中追踪特定量化策略。 |
| - quantizeMetho d | Integer | 0 | 量化方法。 |
| - quantizeStatus | Integer | 0 | 量化状态。 |
| - quantizeStrate gy | Integer | 0 | 量化策略。 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额组ID。 |
| -quotaName | String | quota-name | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| - sourceModelSi ze | Float | 1.2 | 表示源模型文件的大小，通常用于描述预训练模型或基础模型所占用的磁盘空间容量。 |
| -storageMount | String | /mnt/output | 持久化挂载点。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -storagePath | String | oss://****/**** | 存储路径。 |
| - targetModelSiz e | Float | 10 | 模型文件的大小，单位为MB，用于评估模型部署所需的存储空间。 |
| - instanceCostV O | Struct | {} | 任务实例消耗。 |
| --runningCost | Float | 500 | 运行中任务消耗 |
| --runningCpu | Integer | 1 | 运行中消耗的cpu数 |
| --runningGpu | Integer | 1 | 运行中消耗的gpu数 |
| -- runningGpuMe m | Integer | 12582912 | 运行中消耗的gpu显存 |
| --runningMem | Integer | 128 | 表示当前系统中正在运行的进程所占用的物理内存大小 |
| --runningPod | Integer | 1 | 运行中的pod数 |
| --totalCost | Float | 150.75 | 任务的总消耗 |
| --totalCpu | Float | 10 | 任务的cpu总消耗 |
| --totalGpu | Float | 10 | 任务的gpu总消耗 |
| --totalGpuMem | Integer | 1000 | 任务的显存总消耗 |
| --totalMem | Float | 10 | 任务的内存总消耗 |
| --totalPod | Integer | 1 | 任务的pod总消耗 |
| - modelMountV O | Struct | {} | 模型挂载。 |
| --modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --modelName | String | name | 模型名称 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --mountPath | String | /tmp | 容器挂载路径。 |

**示例**

请求示例

```
&quantizeId=qt-729c6c1e030cc04d970a10f*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateQuantize

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /quantize/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | Cpu大小，单位为核，该参数必填。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
|---|---|---|---|---|---|
| gpuCount | Integ er | Body | 是 | 1 | Gpu大小，单位为卡，该参数必填。 |
| gpuMemC ount | Integ er | Body | 否 | 0 | 显存大小，单位为GB。 |
| gpuLabelC ount | Integ er | Body | 否 | 0 | 开启GPU虚拟化之后的GPU 卡数。 |
| modelSou rce | Integ er | Body | 是 | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |
| modelTyp e | Strin g | Body | 否 | qwen3 | 模型类型，当 modelSource为1时，该参数不能为空，表示当前自定义模型对应的模型类型。 |
| quantizeS trategy | Integ er | Body | 是 | 0 | 量化策略，该参数必填，取值范围： 0：Int4-W4A16。 1：Int8-W8A16。 2：FP8-Wfp8Afp8。 |
| quantizeM ethod | Integ er | Body | 否 | 0 | 量化策略，取值范围： 0：GPTQ。 1：AWQ。 |
| storagePa th | Strin g | Body | 是 | oss://******/ | 存储路径，该参数必填。 |
| storageMo unt | Strin g | Body | 是 | /mnt/output | 持久化挂载点，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelMou nt | Json | Body | 是 | { "modelId":"md- 362495ef0fba10****", "modelVersion":"v1", "mountPath":"/mnt/mod el", "dataAccInstance":"da- 29eac3c8861d4e3d9b14 78f17d18****" } | 模型挂载信息，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "quantizeId": "qt- ****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /quantize/create HTTP/1.1 { "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "cpuCount":"1", "memCount":"1", "gpuCount":"1", "modelSource":"1", "quantizeStrategy":"0", "storagePath":"oss://******/", "storageMount":"/mnt/output", "modelMount":"{
      "modelId":"md-362495ef0fba10****",
      "modelVersion":"v1",
      "mountPath":"/mnt/model",
      "dataAccInstance":"da-29eac3c8861d4e3d9b1478f17d18****"
    }"
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\t\"quantizeId\": \"qt-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteQuantize

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quantizeId | Strin g | Query | 是 | ft- 729c6c1e030cc04d970a 10f097***** | 模型量化ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&quantizeId=ft-729c6c1e030cc04d970a10f097*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListQuantize

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 量化模型调列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtrCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| quantizeId | Strin g | Query | 否 | ft- 729c6c1e030cc04d970a 10f097***** | 模型量化ID。 |
| quotaId | Strin g | Query | 否 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |
| modelNa me | Strin g | Query | 否 | model-name | 模型仓库名称。 |
| quantizeS tatus | Integ er | Query | 否 | 0 | 模型量化状态，取值范围： 0：待启动。 1：启动中。 2：量化中。 3：量化失败。 4：量化成功。 5：排队中。 |
| quantizeS trategy | Integ er | Query | 否 | 0 | 模型量化策略，取值范围： 0：Int4-W4A16。 1：Int8-W8A16。 2：FP8-Wfp8Afp8。 |
| quantizeM ethod | Integ er | Query | 否 | 0 | 模型量化方法，取值范围： 0：GPTQ。 1：AWQ。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -gpuCount | Integer | 1 | GPU核数。 |
| -gpuCountUnit | Integer | 1 | 表示GPU数量的最小计量单位，通常指单个GPU 设备 |
| - gpuLabelCoun t | Integer | 1 | 申请到的gpuMemCount显存，平均分配GPU卡数，GPU虚拟化时开启。例如申请显存为 gpuMemCount=8 ，申请卡数为 gpuLabelCount=2 ，表示申请2张GPU 卡，每张卡分配4份显存。 |
| - gpuMemCount | Integer | 0 | 显存大小，单位为GB。 |
| -gpuMemTotal | Integer | 16384 | Maximum GPU memory capacity in MB |
| - gpuMemTotal Unit | Integer | 1 | 表示GPU总显存容量的单位，通常以GB（吉字节）为单位显示 |
| -gpuType | Integer | 0 | GPU显卡类型。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -modelSource | Integer | 1 | 模型来源，该参数必填，取值范围： 0：系统模型。 1：自定义模型。 2：MaaS市场模型。 |
| -nodeCount | Integer | 5 | 节点个数。 |
| -quantizeId | String | qt-12345xxxxxx | 用于标识量化模型或量化配置的唯一整数ID，便于在训练、推理或模型管理中追踪特定量化方案 |
| - quantizeMetho d | Integer | 0 | 量化方法 |
| - quantizeStatus | Integer | 0 | 量化状态 |
| - quantizeStrate gy | Integer | 0 | 量化策略 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | quota-name | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - sharedMemCo unt | Integer | 4 | 共享内存大小，单位为GB。 |
| - sourceModelSi ze | Float | 1.2 | 表示源模型文件的大小，通常用于描述预训练模型或基础模型所占用的磁盘空间容量，单位GB |
| -storageMount | String | /mnt/output | 持久化挂载点 |
| -storagePath | String | oss://****/**** | 存储路径 |
| - targetModelSiz e | Float | 512 | 模型文件的大小，单位为GB，用于评估模型部署所需的存储空间 |
| - instanceCostV O | Struct | {} | 实例消耗资源 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --runningCost | Float | 500 | 任务运行消耗 |
| --runningCpu | Integer | 45 | 运行中cpu数 |
| --runningGpu | Integer | 1 | 运行中gpu数 |
| -- runningGpuMe m | Integer | 2.4 | 运行中消耗的gpu显存量 |
| --runningMem | Integer | 128 | 系统当前正在运行的进程所占用的内存大小 |
| --runningPod | Integer | 1 | 运行中pod总数 |
| --totalCost | Float | 150.75 | 任务总消耗 |
| --totalCpu | Float | 10 | 任务消耗的cpu总数 |
| --totalGpu | Float | 10 | 任务消耗的gpu总数 |
| --totalGpuMem | Integer | 1000 | 任务消耗的gpu显存总数 |
| --totalMem | Float | 10 | 任务消耗的内存总数 |
| --totalPod | Integer | 3 | 任务消耗的pod总数 |
| - modelMountV O | Struct | {} | 模型挂载 |
| --modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| --modelName | String | name | 模型名称 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --mountPath | String | /tmp | 容器挂载路径。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 模型量化的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 模型量化的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### 模型转换

##### CreateModelConvertTask

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /model/convert/task/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelCon vertId | Strin g | Body | 是 | mc- 12c6efa90cc75040c908 9ce03***** | 模型转换ID，该参数必填。 |
| convertTy pe | Integ er | Body | 是 | 1 | 模型转换类型，该参数必填，取值范围： 0：HuggingFace to Megatron。 1：Megatron to HuggingFace。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| cpuCount | Integ er | Body | 是 | 1 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| tensorPar allelism | Integ er | Body | 是 | 1 | tensor并行数，该参数必填。 |
| pipelinePa rallelism | Integ er | Body | 是 | 1 | pipeline并行数，该参数必填。 |
| targetStor agePath | Strin g | Body | 是 | oss://***** | 目标存储路径，该参数必填。 |
| targetMou ntPath | Strin g | Body | 是 | /mnt/model/***** | 目标挂载路径，该参数必填。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "modelConvertId": "mc-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /model/convert/task/create HTTP/1.1 { "modelConvertId":"mc-12c6efa90cc75040c9089ce03*****", "convertType":"1", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "cpuCount":"1", "memCount":"1", "tensorParallelism":"1", "pipelineParallelism":"1", "targetStoragePath":"oss://*****", "targetMountPath":"/mnt/model/*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{       \"modelConvertId\": \"mc-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### GetModelConvertProgress

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelCon vertId | Strin g | Query | 是 | mc- 48fca8d2020f604b4709 69b0***** | 模型转换ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -convertType | Integer | 1 | 模型转换类型，该参数必填，取值范围： 0：HuggingFace to Megatron。 1：Megatron to HuggingFace。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -cpuCount | Integer | 16 | CPU总核数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| - modelConvertI d | String | mc- 12c6efa90cc75040 c9089ce03***** | 模型转换ID。 |
| - modelConvert Status | Integer | 0 | 模型转换状态，取值范围： 0：待启动。 1：启动中。 2：转换中。 3：转换失败。 4：转换成功。 5：排队中。 |
| - pipelineParalle lism | Integer | 1 | pipeline并行数 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -resultInfo | String | "" | 执行结果信息。 |
| -subStatus | Integer | 0 | 子状态。 |
| - targetModelSiz e | Float | 10 | 表示目标模型的预大小，单位为GB |
| - targetMountPa th | String | /mnt/model/***** | 目标挂载路径 |
| - targetStorage Path | String | oss://***** | 目标存储路径，该参数必填。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - tensorParalleli sm | Integer | 1 | tensor并行数 |
| - modelConvert Configvo | Struct | {} | 用于配置模型转换规则的VO对象，包含源模型类名、目标模型类名、字段映射关系（源字段→目标字段）、需忽略的字段列表，以及是否启用深度嵌套对象转换的开关 |
| --aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| --gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| --gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -- modelCategor y | Integer | 1 | 模型转换种类，取值范围： 1：llama-7b。 2：llama2-7b。 3：llama3-8b。 4：qwen-7b。 5：qwen1.5-7b。 |
| -- modelConvertI d | String | mc- 12c6efa90cc75040 c9089ce03***** | 模型转换ID。 |
| --modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --regionId | String | cn-hangzhou | 地域ID。 |
| -- sourceModelSi ze | Float | 1.2 | 表示源模型文件的大小，通常用于描述预训练模型或基础模型的磁盘占用空间 |
| -- sourceMountP ath | String | /mnt/model/***** | 源模型挂载路径 |
| -- sourceStorage Path | String | oss://*****/ | 源模型存储路径。 |
| --sourceType | Integer | 1 | 源数据的类型。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&modelConvertId=mc-48fca8d2020f604b470969b0*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListModelConvertTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型转换列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| modelCat egory | Integ er | Query | 否 | 1 | 模型转换种类，取值范围： 1：llama-7b。 2：llama2-7b。 3：llama3-8b。 4：qwen-7b。 5：qwen1.5-7b。 |
| modelCon vertStatus | Integ er | Query | 否 | 0 | 模型转换状态，取值范围： 0：待启动。 1：启动中。 2：转换中。 3：转换失败。 4：转换成功。 5：排队中。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| -convertType | Integer | 1 | 模型转换类型，该参数必填，取值范围： 0：HuggingFace to Megatron。 1：Megatron to HuggingFace。 |
| -cpuCount | Integer | 16 | CPU总核数。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -memCount | Integer | 1 | 内存大小，单位为GB。 |
| - modelConvertI d | String | mc- 12c6efa90cc75040 c9089ce03***** | 模型转换ID。 |
| - modelConvert Status | Integer | 0 | 模型转换状态，取值范围： 0：待启动。 1：启动中。 2：转换中。 3：转换失败。 4：转换成功。 5：排队中。 |
| - pipelineParalle lism | Integer | 1 | pipeline并行数 |
| -quotaId | String | rq- d8890a98089c204 1d8086bb0b2e27* *** | 配额ID。 |
| -quotaName | String | quota-name | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -subStatus | Integer | 0 | 任务子状态 |
| - targetModelSiz e | Float | 128 | 表示目标模型的预期大小，单位为GB |
| - targetMountPa th | String | /mnt/model/***** | 目标挂载路径 |
| - targetStorage Path | String | oss://***** | 目标存储路径，该参数必填。 |
| - tensorParalleli sm | Integer | 1 | tensor并行数 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - modelConvert Configvo | Struct | {} | 用于配置模型转换规则的VO对象，包含源模型类名、目标模型类名、字段映射关系、需忽略的字段列表以及是否启用校验等转换策略信息 |
| --aliyunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| --gmtCreated | String | 2017-11- 27T06:51:26Z | 资源集创建时间。 |
| --gmtModified | String | 2022-01- 07T10:07:57.000+ 0000 | 修改时间。 |
| -- modelCategor y | Integer | 1 | 模型转换种类，取值范围： 1：llama-7b。 2：llama2-7b。 3：llama3-8b。 4：qwen-7b。 5：qwen1.5-7b。 |
| -- modelConvertI d | String | mc- 12c6efa90cc75040 c9089ce03***** | 模型转换ID。 |
| --modelId | String | md- rbvg5wzljz****ks92 | 模型ID。 |
| --modelName | String | name | 模型名称 |
| -- modelVersion | String | v1 | 模型仓库版本号。 |
| --regionId | String | cn-hangzhou | 地域ID。 |
| -- sourceModelSi ze | Float | 1.2 | 表示源模型文件的大小，通常用于描述预训练模型或基础模型所占用的磁盘空间容量 |
| -- sourceMountP ath | String | /mnt/model/***** | 源模型挂载路径 |
| -- sourceStorage Path | String | oss://*****/ | 源端存储Bucket内的访问路径。 |
| --sourceType | Integer | 1 | 源数据的类型。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 模型转换任务的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 任务的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

##### DeleteModelConvert

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modelCon vertId | Strin g | Query | 是 | mc- 48fca8d2020f604b4709 69b***** | 模型转换ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&modelConvertId=mc-48fca8d2020f604b470969b*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### CreateModelConvertSource

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /model/convert/source/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceTyp e | Integ er | Body | 是 | 1 | 源类型，该参数必填，取值范围： 0：模型仓库。 1：云存储OSS。 |
| modelId | Strin g | Body | 否 | md- e97c65da0d70b04f2b0b bcb057d9s**** | 模型仓库ID。 |
| modelVer sion | Strin g | Body | 否 | v1 | 模型仓库版本。 |
| modelCat egory | Integ er | Body | 是 | 1 | 模型类型，该参数必填，取值范围： 1：llama-7b。 2：llama2-7b。 3：llama3-8b。 4：qwen-7b。 5：qwen1.5-7b。 |
| sourceSto ragePath | Strin g | Body | 否 | oss://*****/ | 源模型存储路径。 |
| sourceMo untPath | Strin g | Body | 是 | /mnt/model/***** | 源模型挂载路径，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | { "modelConvertId": "mc-*****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /model/convert/source/create HTTP/1.1 { "sourceType":"1", "modelCategory":"1", "sourceMountPath":"/mnt/model/*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{      \"modelConvertId\": \"mc-*****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 模型评测

#### CreateEvaluateTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /evaluate/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | Strin g | Body | 是 | evaluateTask-name | 模型评测任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| taskDesc | Strin g | Body | 否 | evaluateTask-desc | 模型评测任务描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |
| imageId | Strin g | Body | 是 | img- 359cc14b09a50049800b bd4sada8s*** | 镜像ID，该参数非必填，评测方法为自定义评测时必传。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数非必填， 评测方法为自定义评测时需传。 |
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27f*** | 资源配额ID，该参数必填。 |
| taskType | Integ er | Body | 是 | 1 | 任务类型，该参数非必填， 评测方法为自定义评测时需传1。 默认值：1 |
| frameWor k | Integ er | Body | 是 | 1 | 模型框架，该参数非必填 （评测方法为自定义评测时需传），取值范围： 1：Tensorflow。 2：PyTorch。 |
| trainType | Integ er | Body | 否 | 0 | （废弃参数） 训练类型，取值范围： 0：单机训练。 1：分布式训练。 默认值：0。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| startCom mand | Strin g | Body | 否 | python3 main.py | 启动命令，评测方法为自定义评测时，该参数不能为空。 |
| isSchedul e | Boole an | Body | 否 | false | 是否启用定时任务，取值范围： true：启用。 false：禁用。 默认值：false。 |
| scheduleT ime | Strin g | Body | 否 | 2024-11-21 00:00:00 | 运行时间，当isSchedule值为true时，该参数不能为空。 |
| datasetMo untList | Json | Body | 是 | [{ "datasetId": "ds- 5740734ff2cf4a00bc6da *****", "mountPath": "/data" }] | 数据集配置，评测方法为自动评测时该参数必填。 |
| modelMou ntList | Json | Body | 否 | [{ "modelId": "md- 7a5c75e10a95104e1d0 bd5804e0c346c****", "mountPath": "/root", "modelType": 1, "modelVersion": "v1", "dataAccInstance":"da- df89s8f9sdfs99sae*****" }] | 模型仓库配置，评测方法为自定义评测时该参数不能为空。 |
| codeMoun tList | Json | Body | 否 | [{ "codeId": "cd- a4a60fa1000d304cb609 79f0f1*****", "mountPath": "/data" }] | 代码集配置。 |
| storageMo untList | Json | Body | 否 | [{ "mountPath": "/root", "storagePath": "oss://****/", "storageSource": 1, "quotaId": "rq- d8890a98089c2041d80 86bb0b2e27f****" }] | 持久化存储设置。评测方法为自动评测、基准评测时该参数不能为空。 |
| nodeConfi gList | Json | Body | 是 | [{ "nodeType": 2, "nodeCount": 1, "cpuCount": 1, "memCount": 1, "gpuCount": 0 }] | 任务资源配置，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| evalMode | Integ er | Body | 否 | 0 | 评测方法，取值范围： 0：基准评测 1：自定义评测 2：自动评测默认值：1 |
| evaluateO bjectConfi gs | Json | Body | 否 | [ { "serviceId": "os- b8ab165b056f804f1c" } ] | 待评测模型服务信息配置。 |
| benchmar kType | Json | Body | 否 | [0,1,2] | 基准评测领域类型（可多选），评测方法为基准评测时该参数不能为空，取值范围： 0：知识问答 1：逻辑推理 2：指令遵循 |
| judgeStrat egy | Json | Body | 否 | [0] | 评分方式，评测方法为自动评测时该参数不能为空，取值范围： 基于规则打分：0 裁判员模型打分：1 |
| judgeMod elConfigs | Json | Body | 否 | { "serviceId": "os- b8ab165b056f804f1c" } | 裁判员模型服务配置，自动评测且评分方式为基于裁判员模型打分时该参数不能为空。 |
| scorerCon figs | Json | Body | 否 | [ { "scorerType": 3, "promptConfig": { "scoring type": _ "binary judgment", _ "system prompt": "你是 _ 一个数学题评判专家...", "judgment criteria": "判 _ 断最终数值答案是否与参考答案一致，允许等价表达。 ", "evaluation guidelines": _ "忽略中间步骤，只看最终答案" } } ] | 评分器配置，scorerType 取值范围： 0：规则评分-精准匹配。 1：规则评分-文本相似度。 2：裁判员评分-数值评分。 3：裁判员评分-二元分类。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | { "taskId": "ev- ****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /evaluate/create HTTP/1.1 { "taskName":"evaluateTask-name", "imageId":"img-359cc14b09a50049800bbd4sada8s***", "imageVersion":"v1", "quotaId":"rq-d8890a98089c2041d8086bb0b2e27f***", "taskType":"1", "frameWork":"1", "startCommand":"python3 main.py", "datasetMountList":"[{
 "datasetId": "ds-5740734ff2cf4a00bc6da*****",
 "mountPath": "/data"
}]", "nodeConfigList":"[{
 "nodeType": 2,
 "nodeCount": 1,
 "cpuCount": 1,
 "memCount": 1,
 "gpuCount": 0
}]" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{ \"taskId\": \"ev-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteEvaluateTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /evaluate/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | ev- ec00ccee0b8c904e210b ad10fb60**** | 模型评测任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
DELETE /evaluate/delete HTTP/1.1 &taskId=ev-ec00ccee0b8c904e210bad10fb60****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetEvaluateTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /evaluate/get HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 是 | ev-dfd2****9404e49 | 评测任务唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -judgeStrategy | List | [0] | 评分策略列表。枚举值： 0 -规则打分， 1 -裁判员打分(llm-as-a-judge)。 |
| - benchmarkTyp e | List | [0] | 预置基准评测类型列表。枚举值： 0 -知识问答， 1 -逻辑推理， 2 -指令遵循。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds-fcfa****9904cf7 | 数据集ID。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -- datasetFileNa me | String | null | 数据集文件名。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| -- dataAccInstan ce | String | null | 数据加速实例。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| -- dataAccInstan ce | String | null | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |
| - codeMountList | Array | [] | 代码库挂载列表。 |
| --codeId | String | cd- 2e0c****0e04d24 | 代码库ID。 |
| --codeName | String | my-code-repo | 代码库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |
| -- storageSource | Integer | 1 | 存储来源。 |
| --storagePath | String | oss://xxxxx.rm.com /secscan-output/ | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称(已废弃）。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | null | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数。 |
| --cpuCount | Integer | 2 | CPU数量。 |
| --memCount | Integer | 2 | 内存大小（GB）。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| -- gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| --gpuCount | Integer | 0 | GPU数量。 |
| -- startCommand | String | null | 启动命令。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --storageId | String | ts- e42a****3204003 | 第三方存储ID。 |
| --occupantId | String | ev- dfd2****9404e49 | 资源ID。 |
| -- storageSubPat h | String | /mnt/data/ | 存储子路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| - evaluateObjec tInfo | Array | [] | 参评对象基础信息列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --serviceId | String | os- be55****e4d04dc5 | 裁判员在线服务ID。 |
| --serviceName | String | 在线服务名称xxx | 裁判员模型在线服务名称。 |
| -- modelGenerati onConfig | Struct | {} | 模型生成参数配置。 |
| ---temperature | Float | 0.7 | 采样温度。 |
| ---topP | Float | 0.9 | Top-P采样参数。 |
| ---maxTokens | Integer | 2048 | 最大生成Token数。 |
| --- customParame ters | Struct | {} | 自定义参数。 |
| ----key | String | stop | 自定义参评模型服务推理参数的键 |
| ----value | Struct | N | 自定义参评模型服务推理参数的值 |
| - judgeModelInf o | Array | [] | 裁判员模型信息列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --serviceId | String | os- be55****e4d04dc5 | 裁判员在线服务ID。 |
| --serviceName | String | 在线服务名称xxx | 裁判员模型在线服务名称。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gmtCreated | String | 2025-11- 13T08:10:12Z | 创建时间。 |
| -gmtModified | String | 2025-11- 13T08:10:12Z | 修改时间。 |
| -aliyunUid | String | 198226****1225 | 阿里云主账号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| -failedMsg | String | null | 失败信息。 |
| -taskId | String | ev- dfd2****9404e49 | 评测任务唯一标识ID。 |
| -taskName | String | test | 评测任务名称。 |
| -taskDesc | String | task-desc | 评测任务描述。 |
| -taskStatus | Integer | 1 | 评测任务状态。枚举值： 0 -待启动， 1 - 启动中， 2 -运行中， 3 -已停止， 4 -失败， 5 -已完成， 6 -排队中， 7 -停止中， 8 -定时等待。 |
| -quotaId | String | rq-bd1d****4040fb | 配额ID。 |
| -quotaName | String | A100资源配额-3 | 配额名称。 |
| - startCommand | String | null | 启动命令。 |
| -nodeCount | Integer | 1 | 节点数。 |
| -cpuCount | Integer | 2 | CPU数量。 |
| -memCount | Integer | 2 | 内存大小（GB）。 |
| - gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| -gpuMemTotal | Integer | 0 | 显存总量（GB）。 |

|  | 2 |
|---|---|
| 5 |  |
| 8 |  |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -gpuCount | Integer | 0 | GPU数量。 |
| - gpuLabelCoun t | Integer | 0 | GPU虚拟化卡数量。 |
| -gpuCountUnit | Integer | -1 | GPU数量单位。 |
| - gpuMemTotal Unit | Integer | -1 | 显存总量单位。 |
| -imageId | String | null | 镜像ID。 |
| -imageVersion | String | v1.0 | 镜像版本。 |
| -imageName | String | null | 镜像名称。 |
| -imageType | Integer | null | 镜像类型。枚举值： 0 -公共镜像， 1 -自定义镜像。 |
| - imageAccelera tionType | Integer | null | 镜像加速类型。枚举值： 0 -普通镜像， 1 -加速镜像。 |
| -gpuType | Integer | 0 | GPU类型。枚举值： 0 -无GPU， 1 - nvidia或其他， 2 -k100， 3 -910b。 |
| -gmtEnd | String | null | 任务结束时间。 |
| -isSchedule | Boolean | false | 是否启用定时调度。 |
| -scheduleTime | String | null | 定时调度时间。 |
| -evalMode | Integer | 2 | 评测方法。枚举值： 0 -基准评测， 1 -自定义评测， 2 -自动。 |
| -instanceCost | Struct | {} | 实例消耗信息。 |
| --runningCost | Float | 0.00 | 运行中消耗。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --runningPod | Float | 0 | 运行中Pod数。 |
| --runningCpu | Float | 0 | 运行中CPU数。 |
| --runningMem | Float | 0 | 运行中内存数。 |
| --runningGpu | Float | 0 | 运行中GPU数。 |
| -- runningGpuMe m | Float | 0 | 运行中GPU显存数。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 0 | 总Pod数。 |
| --totalCpu | Float | 0 | 总CPU数。 |
| --totalMem | Float | 0 | 总内存数。 |
| --totalGpu | Float | 0 | 总GPU数。 |
| --totalGpuMem | Float | 0 | 总GPU显存数。 |

**示例**

请求示例

```
GET /evaluate/get HTTP/1.1 &taskId=ev-ec00ccee0b8c904e210bad10fb6dso****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "scheduleTime":"",
  "gmtModified":"",
  "quotaName":"",
  "storageMountList":[
   {
    "mountPath":"",
    "pvcName":"",
```

智能体工厂 OpenTrek

```json
    "storagePath":"",
    "storageSource":""
   }
```

`],`

```json
  "gmtCreated":"",
  "aliyunUid":"",
  "failedMsg":"",
  "modelMountList":[
   {
    "modelName":"",
    "dataAccInstance":"",
    "weightType":"",
    "mountPath":"",
    "modelId":"",
    "pvcName":"",
    "modelVersion":"",
    "modelType":""
   }
```

`],`

```json
  "thirdpartyStorageMountList":[
   {
    "mountPath":"",
    "storageSubPath":"",
    "occupantId":"",
    "storageId":""
   }
```

`],`

```json
  "judgeModelInfo":[
   {
    "modelName":"",
    "modelId":"",
    "modelVersion":"",
    "modelType":"",
    "serviceId":"",
    "serviceName":""
   }
```

`],`

```json
  "evalMode":"",
  "gmtEnd":"",
  "judgeStrategy":"",
  "nodeCount":"",
  "gpuCount":"",
  "imageType":"",
  "taskStatus":"",
  "cpuCount":"",
  "gpuType":"",
  "memCount":"",
  "imageVersion":"",
  "imageId":"",
  "imageName":"",
  "nodeConfigList":[
   {
    "memCount":"",
    "sharedMemCount":"",
```

" M

```
t"""
```

智能体工厂 OpenTrek

```json
    "gpuMemCount":"",
    "nodeCount":"",
    "startCommand":"",
    "nodeType":"",
    "gpuCount":"",
    "cpuCount":""
   }
```

`],`

```json
  "gpuMemCount":"",
  "instanceCost":{
   "runningPod":"",
   "runningMem":"",
   "runningGpuMem":"",
   "totalCpu":"",
   "totalPod":"",
   "totalMem":"",
   "runningGpu":"",
   "totalGpuMem":"",
   "runningCost":"",
   "runningCpu":"",
   "totalCost":"",
   "totalGpu":""
  },
  "quotaId":"",
  "startCommand":"",
  "gpuMemTotal":"",
  "gpuLabelCount":"",
  "evaluateObjectInfo":[
   {
    "modelName":"",
    "modelGenerationConfig":[
     {
      "temperature":"",
      "maxTokens":"",
      "topP":"",
      "customParameters":[
       {
        "value":"",
        "key":""
       }
```

]

```
     }
```

`],`

```json
    "modelId":"",
    "modelVersion":"",
    "modelType":"",
    "serviceId":"",
    "serviceName":""
   }
```

`],`

```json
  "taskDesc":"",
  "regionId":"",
  "gpuMemTotalUnit":"",
  "datasetMountList":[
{
```

智能体工厂 OpenTrek

```json
   {
    "dataAccInstance":"",
    "datasetVersion":"",
    "mountPath":"",
    "pvcName":"",
    "dataType":"",
    "datasetName":"",
    "datasetId":"",
    "datasetFileName":"",
    "datasetType":""
   }
```

`],`

```json
  "codeMountList":[
   {
    "codeId":"",
    "mountPath":"",
    "pvcName":"",
    "codeName":"",
    "codeRepoType":""
   }
```

`],`

```json
  "taskName":"",
  "gpuCountUnit":"",
  "imageAccelerationType":"",
  "taskId":"",
  "benchmarkType":"",
  "isSchedule":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListEvaluateTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /evaluate/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 模型评测列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| taskId | Strin g | Query | 否 | ev-dfd2****9404e49 | 评测任务唯一标识ID。 |
| taskName | Strin g | Query | 否 | test | 评测任务名称。 |
| taskStatus | Integ er | Query | 否 | 1 | 评测任务状态。枚举值： 0 -待启动， 1 - 启动中， 2 -运行中， 3 -已停止， 4 - 失败， 5 -已完成， 6 -排队中， 7 - 停止中， 8 -定时等待。 0：已创建。 1：启动中。 2：运行中。 3：已停止。 4：失败。 5：完成。 |
| frameWor k | Integ er | Query | 否 | 1 | 模型框架，取值范围： 1：Tensorflow。 2：PyTorch。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 否 | rq-bd1d****4040fb | 配额ID。 |
| quotaNam e | Strin g | Query | 否 | A100资源配额-3 | 配额名称。 |
| imageId | Strin g | Query | 否 | img-xxxxxxx | 镜像ID。 |
| imageNa me | Strin g | Query | 否 | 镜像名称xxx | 镜像名称。 |
| modelId | Strin g | Query | 否 | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| modelNa me | Strin g | Query | 否 | Qwen3-4B | 裁判员模型名称。 |
| datasetId | Strin g | Query | 否 | ds-fcfa****9904cf7 | 数据集ID。 |
| datasetNa me | Strin g | Query | 否 | test-dataset | 数据集名称。 |
| evalMode | Strin g | Query | 否 | 2 | 评测方法。枚举值： 0：基准评测。 1：自定义评测。 2：自动评测。 |
| judgeStrat egy | Strin g | Query | 否 | [0] | 评分策略列表。枚举值： 0 -规则打分， 1 -裁判员打分(llm- as-a-judge)。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -judgeStrategy | List | [0] | 评分策略列表。枚举值： 0 -规则打分， 1 -裁判员打分(llm-as-a-judge)。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - benchmarkTyp e | List | [0] | 预置基准评测类型列表。枚举值： 0 -知识问答， 1 -逻辑推理， 2 -指令遵循。 |
| - datasetMountL ist | Array | [] | 数据集挂载列表。 |
| --datasetId | String | ds-fcfa****9904cf7 | 数据集ID。 |
| -- datasetVersion | String | v1 | 数据集版本。 |
| --datasetName | String | test-dataset | 数据集名称。 |
| --datasetType | Integer | 0 | 数据集类型。 |
| --dataType | Integer | 0 | 数据类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| -- datasetFileNa me | String | null | 数据集文件名。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| -- dataAccInstan ce | String | null | 数据加速实例。 |
| - modelMountLi st | Array | [] | 模型库挂载列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --mountPath | String | /testdata/ | 挂载路径。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --pvcName | String | null | PVC名称(已废弃）。 |
| -- dataAccInstan ce | String | null | 数据加速实例。 |
| --weightType | Integer | 0 | 权重类型。 |
| - codeMountList | Array | [] | 代码库挂载列表。 |
| --codeId | String | cd- 2e0c****0e04d24 | 代码库ID。 |
| --codeName | String | my-code-repo | 代码库名称。 |
| -- codeRepoType | Integer | 0 | 代码仓库类型。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| - storageMountL ist | Array | [] | 持久化存储挂载列表。 |
| -- storageSource | Integer | 1 | 存储来源。 |
| --storagePath | String | oss://xxxxx.rm.com /secscan-output/ | 存储路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| --pvcName | String | null | PVC名称(已废弃）。 |
| - nodeConfigList | Array | [] | 节点配置列表。 |
| --nodeType | Integer | null | 节点类型。 |
| --nodeCount | Integer | 1 | 节点数。 |
| --cpuCount | Integer | 2 | CPU数量。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --memCount | Integer | 2 | 内存大小（GB）。 |
| -- sharedMemCo unt | Integer | 0 | 共享内存大小（GB）。 |
| -- gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| --gpuCount | Integer | 0 | GPU数量。 |
| -- startCommand | String | null | 启动命令。 |
| - thirdpartyStor ageMountList | Array | [] | 三方存储挂载列表。 |
| --storageId | String | ts- e42a****3204003 | 第三方存储ID。 |
| --occupantId | String | ev- dfd2****9404e49 | 资源ID。 |
| -- storageSubPat h | String | /mnt/data/ | 存储子路径。 |
| --mountPath | String | /testdata/ | 挂载路径。 |
| - evaluateObjec tInfo | Array | [] | 参评对象基础信息列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --serviceId | String | os- be55****e4d04dc5 | 裁判员在线服务ID。 |
| --serviceName | String | 在线服务名称xxx | 裁判员模型在线服务名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- modelGenerati onConfig | Struct | {} | 模型生成参数配置。 |
| ---temperature | Float | 0.7 | 采样温度。 |
| ---topP | Float | 0.9 | Top-P采样参数。 |
| ---maxTokens | Integer | 2048 | 最大生成Token数。 |
| --- customParame ters | Struct | {} | 自定义参数。 |
| ----key | String | stop | 参评对象模型服务推理参数的键 |
| ----value | Struct | N | 参评对象模型服务推理参数的值 |
| - judgeModelInf o | Array | [] | 裁判员模型信息列表。 |
| --modelId | String | md-system- fa0c****3596b3 | 裁判员模型ID。 |
| --modelType | Integer | 0 | 裁判员模型类型。 |
| --modelName | String | Qwen3-4B | 裁判员模型名称。 |
| -- modelVersion | String | v1.0 | 裁判员模型版本。 |
| --serviceId | String | os- be55****e4d04dc5 | 裁判员在线服务ID。 |
| --serviceName | String | 在线服务名称xxx | 裁判员模型在线服务名称。 |
| -gmtCreated | String | 2025-11- 13T08:10:12Z | 创建时间。 |
| -gmtModified | String | 2025-11- 13T08:10:12Z | 修改时间。 |
| -aliyunUid | String | 198226****1225 | 阿里云主账号。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -failedMsg | String | null | 失败信息。 |
| -taskId | String | ev- dfd2****9404e49 | 评测任务唯一标识ID。 |
| -taskName | String | test | 评测任务名称。 |
| -taskDesc | String | null | 评测任务描述。 |
| -taskStatus | Integer | 1 | 评测任务状态。枚举值： 0 -待启动， 1 - 启动中， 2 -运行中， 3 -已停止， 4 -失败， 5 -已完成， 6 -排队中， 7 -停止中， 8 -定时等待。 |
| -quotaId | String | rq-bd1d****4040fb | 配额ID。 |
| -quotaName | String | A100资源配额-3 | 配额名称。 |
| - startCommand | String | null | 启动命令。 |
| -nodeCount | Integer | 1 | 节点数。 |
| -cpuCount | Integer | 2 | CPU数量。 |
| -memCount | Integer | 2 | 内存大小（GB）。 |
| - gpuMemCount | Integer | -1 | 显存大小（GB）。 |
| -gpuMemTotal | Integer | 0 | 显存总量（GB）。 |
| -gpuCount | Integer | 0 | GPU数量。 |
| - gpuLabelCoun t | Integer | 0 | GPU虚拟化卡数量。 |
| -gpuCountUnit | Integer | -1 | GPU数量单位。 |
| - gpuMemTotal Unit | Integer | -1 | 显存总量单位。 |

|  | 2 |
|---|---|
| 5 |  |
| 8 |  |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageId | String | img-xxxxxxx | 镜像ID。 |
| -imageVersion | String | v1.0 | 镜像版本。 |
| -imageName | String | 镜像名称xxx | 镜像名称。 |
| -imageType | Integer | 0 | 镜像类型。枚举值： 0 -公共镜像， 1 -自定义镜像。 |
| - imageAccelera tionType | Integer | null | 镜像加速类型。枚举值： 0 -普通镜像， 1 -加速镜像。 |
| -gpuType | Integer | 0 | GPU类型。枚举值： 0 -无GPU， 1 - nvidia或其他， 2 -k100， 3 -910b。 |
| -gmtEnd | String | null | 任务结束时间。 |
| -isSchedule | Boolean | false | 是否启用定时调度。 |
| -scheduleTime | String | null | 定时调度时间。 |
| -evalMode | Integer | 2 | 评测方法。枚举值： 0 -基准评测， 1 -自定义评测， 2 -自动。 |
| -instanceCost | Struct | {} | 实例消耗信息。 |
| --runningCost | Float | 0.00 | 运行中消耗。 |
| --runningPod | Float | 0 | 运行中Pod数。 |
| --runningCpu | Float | 0 | 运行中CPU数。 |
| --runningMem | Float | 0 | 运行中内存数。 |
| --runningGpu | Float | 0 | 运行中GPU数。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- runningGpuMe m | Float | 0 | 运行中GPU显存数。 |
| --totalCost | Float | 0.00 | 总费用。 |
| --totalPod | Float | 0 | 总Pod数。 |
| --totalCpu | Float | 0 | 总CPU数。 |
| --totalMem | Float | 0 | 总内存数。 |
| --totalGpu | Float | 0 | 总GPU数。 |
| --totalGpuMem | Float | 0 | 总GPU显存数。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 模型评测的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 模型评测的页码。 |

**示例**

请求示例

```
GET /evaluate/list HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

|  | { "data":[ { "scheduleTime":"", "gmtModified":"", "quotaName":"", "storageMountList":[ { "mountPath":"", "pvcName":"", "storagePath":"", "storageSource":"" } ], "gmtCreated":"", "aliyunUid":"", "failedMsg":"", "modelMountList":[ { "modelName":"", "dataAccInstance":"", "weightType":"", "mountPath":"", "modelId":"", "pvcName":"", "modelVersion":"", "modelType":"" } ], "thirdpartyStorageMountList":[ { "mountPath":"", "storageSubPath":"", "occupantId":"", "storageId":"" } ], "judgeModelInfo":[ { "modelName":"", "modelId":"", "modelVersion":"", "modelType":"", "serviceId":"", "serviceName":"" } ], "evalMode":"", "gmtEnd":"", "judgeStrategy":"", "nodeCount":"", "gpuCount":"", "imageType":"", "taskStatus":"", |  |
|---|---|---|

智能体工厂 OpenTrek

```json
   "cpuCount":"",
   "gpuType":"",
   "memCount":"",
   "imageVersion":"",
   "imageId":"",
   "imageName":"",
   "nodeConfigList":[
    {
     "memCount":"",
     "sharedMemCount":"",
     "gpuMemCount":"",
     "nodeCount":"",
     "startCommand":"",
     "nodeType":"",
     "gpuCount":"",
     "cpuCount":""
    }
```

`],`

```json
   "gpuMemCount":"",
   "instanceCost":[
    {
     "runningPod":"",
     "runningMem":"",
     "runningGpuMem":"",
     "totalCpu":"",
     "totalPod":"",
     "totalMem":"",
     "runningGpu":"",
     "totalGpuMem":"",
     "runningCost":"",
     "runningCpu":"",
     "totalCost":"",
     "totalGpu":""
    }
```

`],`

```json
   "quotaId":"",
   "startCommand":"",
   "gpuMemTotal":"",
   "gpuLabelCount":"",
   "evaluateObjectInfo":[
    {
     "modelName":"",
     "modelGenerationConfig":[
      {
       "temperature":"",
       "maxTokens":"",
       "topP":"",
       "customParameters":[
        {
         "value":"",
         "key":""
        }
```

]

```
      }
```

智能体工厂 OpenTrek `],`

```json
     "modelId":"",
     "modelVersion":"",
     "modelType":"",
     "serviceId":"",
     "serviceName":""
    }
```

`],`

```json
   "taskDesc":"",
   "regionId":"",
   "gpuMemTotalUnit":"",
   "datasetMountList":[
    {
     "dataAccInstance":"",
     "datasetVersion":"",
     "mountPath":"",
     "pvcName":"",
     "dataType":"",
     "datasetName":"",
     "datasetId":"",
     "datasetFileName":"",
     "datasetType":""
    }
```

`],`

```json
   "codeMountList":[
    {
     "codeId":"",
     "mountPath":"",
     "pvcName":"",
     "codeName":"",
     "codeRepoType":""
    }
```

`],`

```json
   "taskName":"",
   "gpuCountUnit":"",
   "imageAccelerationType":"",
   "taskId":"",
   "benchmarkType":"",
   "isSchedule":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ModifyEvaluateTask

智能体工厂 OpenTrek 调用ModifyEvaluateTask修改指定模型评测任务的部分信息，包括模型评测任务名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /evaluate/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Body | 是 | ev- c5566dc90a718042e40a cfa07e29e**** | 模型评测任务ID，该参数必填。 |
| taskName | Strin g | Body | 是 | task-name | 模型评测任务名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| taskDesc | Strin g | Body | 否 | task-desc | 模型评测任务描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /evaluate/modify HTTP/1.1 { "taskId":"ev-c5566dc90a718042e40acfa07e29e****", "taskName":"task-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyEvaluateTaskStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /evaluate/modify-status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Body | 是 | ev- c5566dc90a718042e40a cfa07e29e**** | 模型评测任务ID，该参数必填。 |
| taskStatus | Boole an | Body | 是 | true | 模型评测任务状态，该参数必填，取值范围： true：重启。 false：停止。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /evaluate/modify-status HTTP/1.1 { "taskId":"ev-c5566dc90a718042e40acfa07e29e****", "taskStatus":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListEvaluateResult

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /evaluate/list-result HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskIdList | Json | Body | 是 | ["task001", "task042", "task113"] | 任务ID的集合，用于标识多个任务的唯一编号，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -modelMetrics | Array | [] | 评测结果列表。 |
| --costTimeList | List | [] | 耗时统计（基准评测时返回）。 |
| -- categoryScore List | Array | [] | 分类得分列表（基准评测时返回）。 |
| --- datasetScoreLi st | Array | [] | 数据集得分列表。 |
| ---- datasetName | String | GPQA Diamond | 数据集名称。 |
| ----score | Float | 0.75 | 数据集得分。 |
| ---category | String | 知识问答 | 评测类别名称。 |
| ---score | Float | 0.75 | 指标得分。 |
| --metrics | Array | [] | 评测指标列表。 |
| ---name | String | Rouge-1-F | 指标名称。 |
| ---num | Integer | 100 | 评测样本数量。 |
| ---score | Float | 0.75 | 指标得分。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --finalScore | Float | 0.85 | 最终评测得分。 |
| --modelId | String | md-system- 7ed6****e878ce | 模型ID。 |
| --modelName | String | Qwen3-4B | 模型名称。 |
| -- modelVersion | String | v1.0 | 模型版本。 |
| --serviceId | String | os- e2df****9d404e04 | 在线服务ID。 |
| --serviceName | String | 开发-LLM | 在线服务名称。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /evaluate/list-result HTTP/1.1 { "taskIdList":"["task001", "task042", "task113"]" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "modelMetrics":[
    {
     "modelName":"Qwen3-4B",
     "finalScore":0.85,
     "modelId":"md-system-7ed6****e878ce",
     "metrics":[
      {
       "score":0.75,
       "num":100,
       "name":"Rouge-1-F"
      }
```

`],`

```json
     "modelVersion":"v1.0",
     "categoryScoreList":[
      {
       "score":0.75,
       "datasetScoreList":[
        {
         "score":0.75,
         "datasetName":"GPQA Diamond"
        }
```

`],` `"category":"`知识问答"

```
      }
```

`],`

```json
     "costTimeList":"[]",
     "serviceId":"os-e2df****9d404e04",
     "serviceName":"开发-LLM"
    }
```

]

```
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListEvaluateReviewResult

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /evaluate/review/list HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 评测结果列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| taskId | Strin g | Query | 否 | ev- c5566dc90a718042e40a cfa07e29e**** | 任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - questionChoic eList | Array | [] | 选择题选项列表。 |
| --name | String | A | 可选项。 |
| --value | String | 北京 | 选项值。 |
| -metricList | Array | [] | 评测指标列表。 |
| --name | String | Rouge-1-F | 指标名称。 |
| --score | Float | 0.85 | 指标得分。 |
| -reviewId | String | null | 评测明细ID。 |
| - evalParticipant Id | String | evp- d5c8****7045a9 | 参评对象ID。 |
| -question | String | 中国的首都是哪里？ | 评测问题。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - standardAnsw er | String | 北京 | 标准答案。 |
| - candidateAns wer | String | 中国的首都是北京。 | 参评对象的回答。 |
| -judgeReason | String | 回答正确且完整。 | 裁判员评分理由。 |
| -score | Float | 0.85 | 指标得分。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 数据总条数 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 页码 |

**示例**

请求示例

```
GET /evaluate/review/list HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ExportEvaluateReviewResult

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /evaluate/review/export HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Strin g | Query | 否 | ev- ec00ccee0b8c904e210b ad10fb6dso**** | 模型评测任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"downloadUrl": "http://sttest- 0610.oss***"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /evaluate/review/export HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{\"downloadUrl\": \"http://sttest-0610.oss***\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyEvaluateReview

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /evaluate/review/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| evalTaskI d | Strin g | Body | 是 | ev-ady8sdysdf*** | 评测任务ID，该参数必填。 |
| evalPartici pantId | Strin g | Body | 是 | evp-sdydusdf6*** | 评测任务与参评对象关联唯一ID，该参数必填。 |
| reviewId | Strin g | Body | 是 | review-u7sdfa7*** | 评测ID，该参数必填。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| feedback | Json | Body | 否 | { "candidateAnswer": "天空是蓝色的" } | 反馈结果。 |
| feedbackS core | Float | Body | 否 | 2.5 | 人工修正后的评分。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /evaluate/review/modify HTTP/1.1 { "evalTaskId":"ev-ady8sdysdf***", "evalParticipantId":"evp-sdydusdf6***", "reviewId":"review-u7sdfa7***" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### AI资源池

#### EnableResourcePoolSLS

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/enable-sls/[resourcePoolId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |
| logProject | Strin g | Query | 是 | test | 日志项目名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/enable-sls/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-bc47fd6f0af720435c0a4d60eeba63****", "logProject":"test" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateResourcePool

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolName | Strin g | Body | 是 | resourcePool-name | 资源池名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| resourceP oolDescrip tion | Strin g | Body | 否 | resourcePool-desc | 资源池描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

|  | 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceT ype | Integ er | Body | 是 | 0 | 资源池类型，该参数必填， 取值范围： 0：裸金属。 1：EGS。 |
| clusterId | Strin g | Body | 是 | c2ce98d5a1dff4fb7b08e 7385cb83**** | ACK集群ID，该参数必填。 |
| bmcpClust erId | Strin g | Body | 否 | ack-YoZjGQ**** | BMCP集群 ID，resourceType为0 时，该参数不能为空。 |
| logProject | Strin g | Body | 否 | test | 日志项目名称。 |
| logFlag | Integ er | Body | 否 | 0 | 是否使用日志服务，取值范围： 0：否。 1：是。 |
| accessTyp e | Boole an | Body | 否 | false | 是否开通经典网络，取值范围： true：开通。 false：关闭。 默认值：false。 |
| thirdParty StorageLis t | Json | Body | 否 | [ { "storageId":"a12****", "storageSubPath":"/aistu dio/third/****", "mountPath":"/kea/traini ng/****" } ] | 三方存储列表。 |
| featureIdL ist | Json | Body | 否 | [1, 2, 3] | 选择启用的组件id列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"resourcePoolId": "rp-****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/create HTTP/1.1 { "resourcePoolName":"resourcePool-name", "resourceType":"0", "clusterId":"c2ce98d5a1dff4fb7b08e7385cb83****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"resourcePoolId\": \"rp-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteResourcePool

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /resource/pool/delete/[resourcePoolId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /resource/pool/delete/[resourcePoolId] HTTP/1.1 &resourcePoolId=rp-bc47fd6f0af720435c0a4d60eeba63****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### GetResourcePoolDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/pool/detail/[resourcePoolId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuTypeList | List | NVIDIA Ampere ** _ _ *** | GPU类型。 |
| -featureVOList | Array | [] | 资源池关联特性列表。 |
| --ackClusterId | String | cef51d60a65ab3a8 026c24***** | ACK集群ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- bmcpClusterId | String | ack-YoZjGQ**** | BMCP集群ID。 |
| --canClose | Integer | 1 | 是否可关闭。 0: 不可关闭。 1: 可关闭。 |
| --canOpen | Integer | 1 | 是否可开启。 0: 不可开启。 1: 可开启。 |
| -- featureDescrip tion | String | 用于训推任务运行日志的采集存储 | 特性描述。 |
| --featureName | String | LogstoreFeature | 特性名称。 |
| -- featureNameC n | String | 日志存储 | 特性中文名称。 |
| -- featureNameT W | String | 日誌存儲 | 特性繁体名称。 |
| -- featureOriginN ame | String | ResourcePoolFeatu re-LogstoreFeature | 特性原始名称。 |
| -- featureRunnin gDetails | String | "" | 特性运行详情。 |
| --featureStatus | String | DONE | 特性当前状态。 INIT: 初始化。 DOING: 正在执行。 DONE: 已完成。 UNDOING: 正在卸载。 NONE: 未开启。 |
| --featureStep | String | "" | 特性步骤。 |
| -- featureTarget Status | Integer | 1 | 特性目标状态。 |
| --gmtCreated | String | 2025-11-30 07:23:23 | 创建时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gmtModified | String | 2025-11-30 07:23:23 | 修改时间。 |
| --id | Integer | 1 | 特性ID。 |
| --resourceId | String | rp-xxxxx | 关联资源ID。 |
| --visible | Integer | 1 | 是否可见。 0: 不可见。 1: 可见。 |
| -accessIp | String | 100.104.***.*** | 集群上AIStudio经典网络SLB的IP。 |
| -accessType | Boolean | true | 经典网络是否开启。 true: 开启。 false: 关闭。 |
| -ackClusterId | String | cef51d60a677ab3a 8026c24***** | ACK集群ID。 |
| - ackClusterNa me | String | ack-cluster-name | ACK集群名称。 |
| - assignedNode Count | Integer | 3 | 分配节点数量。 |
| - availableStatu s | Integer | 1 | 资源池状态。 0: 创建中。 1: 可用。 2: 创建失败。 3: 不可用。 |
| - bmcpClusterId | String | ack-YoZjGQ**** | BMCP集群ID。 |
| - bmcpClusterN ame | String | bmcp-cluster-name | BMCP集群名称。 |
| -certStatus | Boolean | true | 证书状态。 |
| -createUser | String | 17366294xxxxxxx | 创建人。 |
| -logProject | String | k8s-log-xxxxxx | 日志服务LogProject的名称。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| - ramRoleStatus | Boolean | true | RAM角色是否可用。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - resourcePoolC PU | Integer | 128 | 资源池CPU核数。 |
| - resourcePoolD escription | String | resourcePool-desc | 资源池描述。 |
| - resourcePoolG PU | Integer | 24 | 资源池GPU卡数。 |
| - resourcePoolG mtCreate | String | 2025-11-30 07:23:23 | 资源池创建时间。 |
| - resourcePoolId | String | rp-123xxxxxxxx | 资源池ID。 |
| - resourcePoolM em | Integer | 2048 | 资源池内存（GB）。 |
| - resourcePoolN ame | String | test pool _ | 资源池名称。 |
| - resourcePoolSt atus | Integer | 1 | 关联集群状态。 |
| - resourcePoolT ag | String | tag | 资源池标签。 |
| -resourceType | Integer | 0 | 资源类型。 0: BMCP高网。 1: BMCP基础。 2: BMCP纳管。 3: EGS。 5: Aspeed。 |
| -rrsaEnable | Boolean | true | RRSA状态。 |
| - thirdPartyRdm a | Boolean | false | 三方高网状态。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - totalNodeCoun t | Integer | 3 | 总节点数。 |
| -gpuInfo | Struct | {} | 资源池GPU信息。 |
| --gpu | String | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ | 芯片名称。 |
| -- manufacturer | String | NVIDA | 芯片厂商。 |
| -- manufacturerC N | String | 英伟达 | 芯片厂商中文名。 |

**示例**

请求示例

```
GET /resource/pool/detail/[resourcePoolId] HTTP/1.1 &resourcePoolId=rp-bc47fd6f0af720435c0a4d60eeba63****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "resourcePoolStatus":"",
  "certStatus":"",
  "ramRoleStatus":"",
  "gpuInfo":{
   "manufacturerCN":"",
   "gpu":"",
   "manufacturer":""
  },
  "resourcePoolGPU":"",
  "resourcePoolGmtCreate":"",
  "ackClusterName":"",
  "ackClusterId":"",
  "accessType":"",
  "bmcpClusterId":"",
  "totalNodeCount":"",
  "bmcpClusterName":"",
  "resourcePoolMem":"",
  "accessIp":"",
  "resourcePoolName":"",
  "availableStatus":"",
  "assignedNodeCount":"",
  "resourcePoolCPU":"",
  "regionId":"",
```

智能体工厂 OpenTrek

```json
  "featureVOList":[
   {
    "canClose":"",
    "gmtModified":"",
    "resourceId":"",
    "visible":"",
    "featureName":"",
    "featureStep":"",
    "gmtCreated":"",
    "featureStatus":"",
    "featureDescription":"",
    "featureRunningDetails":"",
    "ackClusterId":"",
    "featureOriginName":"",
    "bmcpClusterId":"",
    "featureNameCn":"",
    "featureTargetStatus":"",
    "canOpen":"",
    "featureNameTW":"",
    "id":""
   }
```

`],`

```json
  "resourcePoolId":"",
  "gpuTypeList":"",
  "resourcePoolDescription":"",
  "createUser":"",
  "rrsaEnable":"",
  "resourcePoolTag":"",
  "logProject":"",
  "thirdPartyRdma":"",
  "resourceType":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetResourcePoolList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Query | 否 | rp- bc47fd6f0af720435c0a4 d60eeba6**** | 资源池ID。 |
| resourceP oolName | Strin g | Query | 否 | resourcePool-name | 资源池名称。 |
| resourceT ype | Integ er | Query | 否 | 0 | 资源池类型，取值范围： 0：裸金属。 1：EGS。 |
| gpuType | Strin g | Query | 否 | Hygon Kongming DCUK _ _ 100 **** _ | GPU类型。 |
| availableS tatus | Integ er | Query | 否 | 1 | 资源池状态，取值范围： 0：创建中。 1：可用。 2：创建失败。 3：不可用。 |
| hasShared Pool | Boole an | Query | 否 | false | 是否是共享资源池。取值范围： true：是 false：否默认值：false。 |
| pageIndex | Integ er | Query | 否 | 1 | 资源池列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | ["PG1 A910E"] _ | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuTypeList | List | PG1 A910E _ | GPU类型。 |
| -gpuInfo | Array | [{"gpu": "PG1 A910E", _ "manufacturer": "APG", "manufacturerCN": "APG", "manufacturerTW": "APG"}] | gpu信息 |
| --gpu | String | PG1 A910E _ | gpu芯片名称 |
| -- manufacturer | String | APG | 厂商 |
| -- manufacturerC N | String | APG | 厂商中文名 |
| -- manufacturerT W | String | APG | 厂商繁体名 |
| - relatedResour ceQuotaList | Array | [{"quotaName":"te st","resourcePoolId ":"rp- xxx","resourceQuot aId":"rq-xxxx"}] | 关联资源配额列表 |
| --quotaName | String | test | 配额名称。 |
| -- resourcePoolId | String | rp-xxxxxx | 资源池ID。 |
| -- resourceQuota Id | String | rq-xxxxxx | 资源配额ID。 |
| - sourceConnect ionList | Array | rp- bc47fd6f0af72043 5ceba**** | 资源池连接信息。 |
| --app | String | software-source | 名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --mappingIp | String | 192.xxx.xxx.xxx | 映射IP地址。 |
| --mappingPort | String | 8000 | 映射端口。 |
| --type | String | pypi | 类型。 |
| -accessType | Boolean | 1 | 经典网络状态。 0: 未开启经典网络。 1: 已开启经典网络。 |
| -ackClusterId | String | cef51d60a6778415 ab3a8026c24***** | ack集群ID。 |
| - assignedNode Count | Integer | 0 | 已分配节点数量。 |
| - availableStatu s | Integer | 1 | 资源池状态。 0: 创建中。 1: 可用。 2: 创建失败。 3: 不可用。 |
| - bmcpClusterId | String | ack-YoZjGQ**** | bmcp集群ID。 |
| -certStatus | Boolean | false | 证书状态。 |
| -createUser | String | 198xxxxxxxxx | 创建人。 |
| - hasSharedPool | Boolean | false | 含有共享资源池。 |
| -regionId | String | cn-hangzhou | 区域ID。 |
| - relatedResour ceQuota | String | test rq 1, test rq2 _ _ _ | 关联资源配额，多个配额之间通过','进行分隔。 |
| - resourcePoolD escription | String | resourcePool-desc | 资源池描述。 |
| - resourcePoolG mtCreate | String | 2026-02- 09T08:20:20Z | 资源池创建时间。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - resourcePoolId | String | rp-bc47ba63**** | 资源池ID。 |
| - resourcePoolN ame | String | test | 资源池名称。 |
| - resourcePoolT ag | String | tag | 资源池标签。 |
| -resourceType | Integer | 0 | 资源池类型。 0: BMCP高网集群。 1: BMCP基础集群。 2: BMCP纳管集群。 3: EGS集群。 5: Aspeed集群。 |
| -shared | Integer | 1 | 共享状态。 0: 本资源集共享。 1: 本组织及下级组织共享。 2: 本组织共享。 |
| - thirdPartyRdm a | Boolean | 1 | 三方高网。 0: 关闭。 1: 开启。 |
| - totalNodeCoun t | Integer | 10 | 总节点数量。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 资源集的总数。 |
| pageSize | Integer | 10 | 每页行数。 |

|  | AI Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageIndex | Integer | 1 | 资源集的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "shared":"",
   "relatedResourceQuota":"",
   "gpuInfo":[
    {
     "manufacturerTW":"",
     "manufacturerCN":"",
     "gpu":"",
     "manufacturer":""
    }
```

`],`

```json
   "certStatus":"",
   "hasSharedPool":"",
   "resourcePoolGmtCreate":"",
   "resourcePoolName":"",
   "ackClusterId":"",
   "accessType":"",
   "availableStatus":"",
   "bmcpClusterId":"",
   "assignedNodeCount":"",
   "totalNodeCount":"",
   "regionId":"",
   "resourcePoolId":"",
   "gpuTypeList":"",
   "resourcePoolDescription":"",
   "createUser":"",
   "resourcePoolTag":"",
   "sourceConnectionList":[
    {
     "app":"",
     "mappingPort":"",
     "mappingIp":"",
     "type":""
    }
```

`],`

```json
   "thirdPartyRdma":"",
"relatedResourceQuotaList":[
```

智能体工厂 OpenTrek

```json
   "relatedResourceQuotaList":[
    {
     "quotaName":"",
     "resourcePoolId":"",
     "resourceQuotaId":""
    }
```

`],`

```json
   "resourceType":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### GetResourcePoolNode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/pool/getNodeList HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Strin g | Query | 否 | ack-AXRu**** | ack集群ID或bmcp集群 ID。 |
| sceneCod e | Integ er | Query | 否 | 0 | 场景标识，取值范围： 0：资源池详情场景 1：资源配额详情场景 2：创建、变更资源配额场景 |
| nodeType | Strin g | Query | 否 | ecs.gn6v-c8g1.2xlarge | 节点规格，对应ECS实例的规格类型。 shareNode：出让节点 recycleNode：借入节点 myNode：我的节点 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| nodeId | Strin g | Query | 否 | i-7kk01vm****52s8hz0s | 节点实例ID，对应ACK集群中的ECS实例ID。 |
| nodeNam e | Strin g | Query | 否 | cn-neimeng-236e- d01.172.16.1.138 | 节点名称，通常为节点的主机名或IP地址标识。 |
| nodeSpec | Strin g | Query | 否 | "" | 节点配置。 |
| pageIndex | Integ er | Query | 否 | 1 | 节点列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -allocationId | String | rq- 394cb9****ed1044 99 | 节点被分配到的目标ID，对于独占配额输出为 quota-id，对于共享节点池当前不展示。 |
| - allocationType | Integer | 2 | 节点的分配类型 0-unallocated表示没被分配 1-shared表示分配到共享节点池 2-quota表示被分配到独占类型的配额里 3-master表示是Master节点 |
| -available | Boolean | true | 节点是否可用，true表示节点状态为 Ready，false表示不可用。 |
| -belongsTo | String | myNode | myNode: 当前配额节点。 shareNode: 共享节点。 recycleNode: 潮汐调度节点。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -cpuCount | Integer | 32 | 节点CPU核数。 |
| -createTime | String | 2025-10- 31T08:51:03Z | 节点创建时间，格式为yyyy-MM- dd'T'HH:mm:ss'Z'，时区为UTC。 |
| -gpuCount | Integer | 1 | 节点GPU卡数。 |
| - gpuMemCount | Integer | 80 | 节点GPU显存大小，单位为GB。 |
| -gpuType | String | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ | 节点GPU类型，对应resource config表中的 _ GPU型号编码。 |
| -isCgpu | Integer | 0 | 0: 不开启虚拟化。 1: 开启虚拟化。 2: 未知。 |
| -memCount | Integer | 128 | 节点内存大小，单位为GB。 |
| -nodeId | String | i- 7kk01vm****52s8h z0s | 节点实例ID，对应ACK集群中的ECS实例ID。 |
| -nodeName | String | cn-neimeng-xxxxx | 节点名称，通常为节点的主机名或IP地址标识。 |
| -nodeStatus | String | Ready | Ready：就绪。 NotReady：未就绪。 Unknown：未知。 |
| -nodeType | String | ecs.gn6v- c8g1.2xlarge | 节点规格，对应ECS实例的规格类型。 |
| - supportVirtStg | String | 0,1,2 | 节点支持的虚拟化策略列表，多个值以逗号分隔。 |
| - virtualStrategy | String | 0 | UNKNOWN(4): 未知。 |
| -gpuInfo | Struct | {} | GPU信息。 |
| --gpu | String | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ | GPU芯片名称。 |
| -- manufacturer | String | NVIDIA | GPU厂商。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- manufacturerC N | String | 英伟达 | GPU厂商中文名。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /resource/pool/getNodeList HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "memCount":"",
   "nodeName":"",
   "gpuInfo":[
    {
     "manufacturerCN":"",
     "gpu":"",
     "manufacturer":""
    }
```

`],`

```json
   "gpuMemCount":"",
   "supportVirtStg":"",
   "available":"",
   "allocationId":"",
   "virtualStrategy":"",
   "allocationType":"",
   "nodeStatus":"",
   "nodeType":"",
   "isCgpu":"",
   "createTime":"",
   "belongsTo":"",
   "gpuCount":"",
   "nodeId":"",
   "cpuCount":"",
   "gpuType":""
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateResourcePool

调用UpdateResourcePool修改指定资源池的部分信息，包括资源池名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/update/[resourcePoolId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeb**** | 资源池ID。 |
| resourceP oolName | Strin g | Body | 是 | resourcePool-name | 资源池名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| resourceP oolDescrip tion | Strin g | Body | 否 | resourcePool-desc | 资源池描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/update/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-bc47fd6f0af720435c0a4d60eeb****", "resourcePoolName":"resourcePool-name" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateResourcePoolAccessType

调用UpdateResourcePoolAccessType修改是否开启经典网络访问。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/update/accessType/[resourcePoolId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- b985876a0e0ff04c950af fc05ba74***** | 资源池ID。 |
| accessTyp e | Boole an | Body | 是 | true | 是否开启经典网络，该参数必填，取值范围： true：开启。 false：关闭。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/update/accessType/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-b985876a0e0ff04c950affc05ba74*****", "accessType":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetGPUConfig

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -EGS | Array | [] | EGS集群芯片。 |
| --GPUs | List | ["NVIDIA Ampere _ _ A100 80G NVLink" _ _ ] | GPU列表。 |
| -- manufacturer | String | NVIDIA | 厂商。 |
| -- manufacturerC N | String | 英伟达 | 厂商中文名。 |
| -- manufacturerT W | String | 英偉達 | 厂商繁体名。 |
| -裸金属 | Array | [] | 裸金属芯片列表。 |
| --GPUs | List | ["NVIDIA Ampere _ _ A100 80G NVLink" _ _ ] | GPU列表。 |
| -- manufacturer | String | NVIDIA | 厂商。 |
| -- manufacturerC N | String | 英伟达 | 厂商中文名。 |
| -- manufacturerT W | String | 英偉達 | 厂商繁体名。 |

**示例**

请求示例正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":{
```

`"-`裸金属`":[`

```json
   {
    "manufacturerTW":"",
    "GPUs":"",
    "manufacturerCN":"",
    "manufacturer":""
   }
```

`],`

```json
  "EGS":[
   {
    "manufacturerTW":"",
    "GPUs":"",
    "manufacturerCN":"",
    "manufacturer":""
   }
```

]

```json
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListFeature

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceT ype | Strin g | Query | 是 | 0 | 资源类型，取值范围： 0：ResourcePool。 1：ResourceQuota。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| clusterTyp e | Strin g | Query | 是 | 1 | 集群类型，取值范围： 0：智算高网型实例。 1：智算基础型实例。 2：智算纳管型实例。 3：EGS实例。 4：NO LIMIT。 _ |
| gpuTypes | Json | Query | 是 | METAX C550-B**** _ | GPU类型。 |
| resourceP oolId | Strin g | Query | 否 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -canClose | Integer | 0 | 特性是否可关闭，枚举值如下：1：可关闭；0： 不可关闭。 |
| -canOpen | Integer | 1 | 特性是否可开启，枚举值如下：1：可开启；0： 不可开启。 |
| - featureDescrip tion | String | 提供基于CPU/GPU实时监控指标的弹性扩缩容能力 | 特性的功能描述信息。 |
| -featureName | String | InferenceAutoScale GPUFeature | 特性名称，从原始特性名称中分割'-'后取第二部分。 |
| - featureNameC n | String | 弹性伸缩GPU指标 | 特性的中文名称。 |
| - featureNameT W | String | 彈性伸縮GPU指標 | 特性的繁体中文名称，通过国际化翻译获取。 |
| - featureOriginN ame | String | ResourceQuotaFea ture- InferenceAutoScale GPUFeature | 特性原始名称，包含特性类型前缀和特性名称， 格式为{特性类型前缀}-{特性名称}。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -featureStatus | String | NONE | 特性的动态运行状态，枚举值如下： UNSUPPORTED：不支持；INIT：初始化； NONE：未启用；DOING：安装/升级中； UNDOING：卸载中；DONE：服务中，所有步骤已完成。 |
| -featureStep | String | {"additionalConfigs ": {},"singleStepConf igList": [{"canSkip":false," stepClass":"com.ali yun.aistudio.asset.f eatures.step.concr ete.EmptyStep","p arameterClass":""} ]} | 特性执行步骤配置，JSON格式字符串，包含 additionalConfigs（附加配置）和 singleStepConfigList（单步骤配置列表，每项含canSkip、stepClass、 parameterClass）。 |
| - featureTarget Status | Integer | -1 | 特性的目标状态，枚举值如下：- 1（UNSUPPORTED）：不支持； 0（SUPPORTED AND DISABLED）：支持但 _ _ 禁用；1（SUPPORTED AND ENABLED）： _ _ 支持且启用。 |
| -id | Integer | 2** | 特性记录的唯一标识ID，自增主键。 |
| -visible | Integer | 1 | 特性是否可见，枚举值如下：1：可见；0：不可见。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&resourceType=0 &clusterType=1 &gpuTypes=METAX_C550-B****
```

&公共请求参数智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "canClose":"",
   "featureOriginName":"",
   "featureNameCn":"",
   "visible":"",
   "featureName":"",
   "featureStep":"",
   "featureStatus":"",
   "featureTargetStatus":"",
   "featureDescription":"",
   "canOpen":"",
   "featureNameTW":"",
   "id":""
  }
```

`],`

```json
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateFeatureStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Query | 是 | 1 | 特性ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| featureTar getStatus | Integ er | Query | 是 | 0 | 特性状态，取值范围： -1：UNSUPPORTED。 0： SUPPORTED AND DIS _ _ ABLED。 1： SUPPORTED AND EN _ _ ABLED。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&id=1 &featureTargetStatus=0
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteStorageCheck

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/delete/deleteStorageCheck/[storageId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| storageId | Strin g | Path | 是 | 1ed0670a-ca76- 4630****** | 存储池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /resource/pool/delete/deleteStorageCheck/[storageId] HTTP/1.1 { "storageId":"1ed0670a-ca76-4630******" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListAvailableCluster

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/pool/listAvailableCluster HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceT ype | Integ er | Query | 是 | 0 | 资源类型，取值范围： 0：裸金属算力集群。 1：EGS算力集群。 |
| ackCluster Ids | Json | Query | 否 | cluster123,cluster456 | ack集群ID。 |
| gpuType | Strin g | Query | 否 | NVIDIA Ampere ***** _ _ | GPU类型。 |
| clusterId | Strin g | Query | 否 | c2ce98d5a1dff4fb7bcb8 3**** | 集群ID。 |
| clusterNa me | Strin g | Query | 否 | cluster-name | 集群名称。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -EcsGpu | List | [] | ECS上GPU列表。 |
| -Gpu | Array | [] | GPU信息。 |
| --GpuModel | String | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ | GPU名称。 |
| --GpuNum | Integer | 8 | GPU数量。 |
| -- manufacturer | String | NVIDIA | 厂商。 |
| -- manufacturerC N | String | 英伟达 | 厂商中文名。 |
| -- manufacturerT W | String | 英偉達 | 厂商繁体名。 |
| -Specification | Array | [] | 规格配置。 |
| --Count | Integer | 1 | 数量。 |
| --Name | String | gBMC-Ci8bfxxxx | 名称。 |
| -AckClusterId | String | cef51d60a67784a8 026c24***** | ACK集群ID。 |
| - AckClusterNa me | String | ack-cluster-name | ACK集群名称。 |
| -AiStatus | String | notInstall | AI状态。 |
| - BmsActiveNod eCount | Integer | 2 | Bms可用节点数量。 |
| - BmsNodeCoun t | Integer | 2 | Bms节点数量。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ClusterArchTy pe | String | aspeed | 集群架构类型。 aspeed：训推优化集群。 standard：标准集群。 |
| -ClusterId | String | ack-xxxxx | BMCP集群ID。 |
| -ClusterName | String | bmcp-cluster-name | BMCP集群名称。 |
| - ClusterResour ceType | String | bmcp | BMCP集群类型。 |
| - CpfsClusterSta te | String | "" | CPFS集群状态。 |
| - CpfsClusterTy pe | String | "" | CPFS集群类型。 |
| -CpfsMountFs | String | "" | CPFS挂载文件系统。 |
| -CpuCount | Integer | 128 | CPU数量。 |
| -CreateTime | String | 2025-11-30 07:23:23 | 创建时间。 |
| -Description | String | description | 描述。 |
| -EcsCpuCount | Integer | 128 | ECS CPU数量。 |
| -EcsMemCount | Integer | 1024 | ECS 内存大小。 |
| - EcsNodeCount | Integer | 3 | ECS节点数量。 |
| - EcsVideoMem ory | Integer | 0 | ECS Video内存。 |
| - EdaClusterStat e | String | RUNNING | Eda集群状态。 |
| -EnableIpv6 | Boolean | false | 是否启用IPv6。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -EvpcId | String | evpc- t5gwwnlmkokxxxxx | Evpc的唯一标识符。 |
| -FlopsCount | Integer | 3367 | Flops。 |
| - IsSetPassword | Boolean | true | 是否设置密码。 |
| -MemCount | Integer | 2048 | 内存大小，单位为GB。 |
| -NodeCount | Integer | 5 | 节点个数。 |
| -Organization | String | 5 | 组织信息。 |
| -Region | String | cn-hangzhou | 地域。 |
| -Runtime | String | containerd 1.6.39 | 运行时。 |
| -SlbIp | String | 192.168.XX.XX | SLB IP。 |
| -SpId | String | sp- 1037871bf6060xxx xxx | SP ID信息。 |
| -Status | String | active | 状态。 active: 可用。 |
| -SwitchMethod | String | CHSW | 接入交换机类型。 |
| -UpdateTime | String | 2025-11-30 07:23:23 | 更新时间。 |
| -Version | String | 1.32.7-aliyun.1 | ACK版本。 |
| -VideoMemory | Integer | 3096 | 显存。 |
| -VpcId | String | vpc- 7kkfefbi939bmjb0z 3hoc | VPC ID。 |
| -Zone | String | cn-hangzhou-i | 可用区。 |
| -disabledTag | Boolean | true | 集群可用标识。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /resource/pool/listAvailableCluster HTTP/1.1 &resourceType=0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateResourcePoolCertificate

调用UpdateResourcePoolCertificate修改访问资源池经典网络地址的HTTPS证书信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/update/certificate/[resourcePoolId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp-40c8be62091a****** | 资源池ID。 |
| tlsCert | Strin g | Body | 是 | -----BEGIN CERTIFICATE-- --- MIICxDCCAaygAwIBAgIJA J0w2Yt9x4QSMA0GCSqG SIb3DQEBCwUAMBcxFT ATBgNV ...... ...... vH6Iie++0txwVhIuqR8b Z7tTu3sjDSEiPjXWygdP4 45laQOdPmA8CA== ----- END CERTIFICATE----- | 用于安全通信的TLS证书， 通常以Base64编码格式表示，包含公钥和身份信息， 用以验证服务器或客户端的身份，该参数必填。 |
| tlsKey | Strin g | Body | 是 | -----BEGIN PRIVATE KEY-- --- MIIEvwIBADANBgkqhkiG 9w0BAQEFAASCBKkwgg SlAgEAAoIBAQDh0EHZz Sp5reSv ...... ...... /QT+ZB+mRfGzMd2cIMz PRJMAEA== -----END PRIVATE KEY----- | 用于加密TLS通信的私钥， 与证书配对使用以验证服务器身份，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /resource/pool/update/certificate/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-40c8be62091a******", "tlsCert":"-----BEGIN CERTIFICATE----- MIICxDCCAaygAwIBAgIJAJ0w2Yt9x4QSMA0GCSqGSIb3DQEBCwUAMBcxFTATBgNV ...... ...... vH6Iie++0txwVhIuqR8bZ7tTu3sjDSEiPjXWygdP445laQOdPmA8CA== -----END CERTIFICATE-----", "tlsKey":"-----BEGIN PRIVATE KEY----- MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDh0EHZzSp5reSv ...... ...... /QT+ZB+mRfGzMd2cIMzPRJMAEA== -----END PRIVATE KEY-----" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 资源统计

##### GetPoolTaskResourceConsumption

调用GetPoolTaskResourceConsumption查询指定资源池的资源概览详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/poolTaskResourceConsumption HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| poolId | Strin g | Query | 是 | rp-wexxcd3***** | 资源池ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuShare | Boolean | true | 是否GPU共享。 |
| - batchInferenc eJob | Struct | {} | 批量推理信息。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |
| -notebook | Struct | {} | Notebook信息。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |
| -onlineService | Struct | {} | OnlineService信息。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |
| -other | Struct | {} | Other。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |
| -pipelineDraft | Struct | {} | PipelineDraft信息。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |
| -task | Struct | {} | 任务建模信息。 |
| --cpuUsed | Float | 2.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 2.0 | 显存使用。 |
| --gpuUsed | Float | 22.0 | GPU使用。 |
| --memoryUsed | Float | 2.0 | 内存使用。 |
| --taskCount | Integer | 2 | 任务数。 |

**示例**

请求示例

```
GET /resource/statics/poolTaskResourceConsumption HTTP/1.1 &poolId=rp-wexxcd3*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "task":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  },
  "onlineService":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  },
  "notebook":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  },
  "pipelineDraft":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  },
  "gpuShare":true,
  "batchInferenceJob":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  },
  "other":{
   "gpuMemoryUsed":2.0,
   "gpuUsed":22.0,
   "taskCount":2,
   "cpuUsed":2.0,
   "memoryUsed":2.0
  }
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### ListPoolResourceUtilization

调用ListPoolResourceUtilization查询资源池概览中的资源利用率信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/poolResourceUtilization HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| poolId | Strin g | Query | 是 | rp- d8890a98089c2041d80 86bb0b2e27**** | 资源池ID。 |
| specific | Strin g | Query | 否 | 1 | 查询类型，取值范围： 1： 独享资源池。 2：共享资源池。 |
| pageIndex | Integ er | Query | 否 | 1 | 列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -cpuCount | Float | 16.0 | CPU总数。 |
| -cpuUtilization | Float | 0.3 | CPU利用率。 |
| -gpuCount | Float | 1.0 | GPU总数。 |
| -gpuMemory | Float | 8192.0 | 显卡内存大小。 |
| -gpuType | String | NVIDIA Ampere ** _ _ *** | GPU类型。 |
| -gpuUtilization | Float | 0.36 | GPU利用率。 |
| -id | String | 1 | ID。 |
| -memoryCount | Float | 1024.0 | 总内存。 |
| - memoryUtiliza tion | Float | 0.3 | 内存利用率。 |
| -name | String | rq-dd | 名称。 |
| -sharedPool | Boolean | true | 是否使用共享池。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 资源池概览总数。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 资源池概览的页码。 |

**示例**

请求示例

```
GET /resource/statics/poolResourceUtilization HTTP/1.1 &poolId=rp-d8890a98089c2041d8086bb0b2e27****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "cpuUtilization":0.3,
   "gpuMemory":8192.0,
   "sharedPool":true,
   "gpuUtilization":0.36,
   "name":"rq-dd",
   "memoryUtilization":0.3,
   "memoryCount":1024.0,
   "id":"1",
   "gpuCount":1.0,
   "cpuCount":16.0,
   "gpuType":"NVIDIA_Ampere_*****"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

##### GetPoolResourceOverview

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
GET /resource/statics/poolSystemResourceOverview HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| poolId | Strin g | Query | 是 | rp-xc8x89sva***** | 资源池ID。 |
| gpuType | Strin g | Query | 否 | all | GPU类型。 默认值为：all。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuTypes | List | [NVIDIA Ampere A _ _ 100 80G NVLink] _ _ | GPU类型。 |
| -nodeCount | Integer | 2 | 节点个数。 |
| - shareNodeCou nt | Integer | 1 | 共享节点数。 |
| - sharedPoolTot alCpu | Float | 16.0 | 共享资源池的Cpu总数。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - sharedPoolTot alGpu | Float | 8.0 | 共享资源池的Gpu总数。 |
| - sharedPoolTot alGpuMemory | Float | 255.0 | 共享资源池的显存总数。 |
| - sharedPoolTot alMemory | Float | 474.0 | 共享资源池的内存总数。 |
| - totalCpuCount | Float | 4.0 | 资源池的Cpu总数。 |
| - totalGpuCount | Float | 4.0 | 资源池的Gpu总数。 |
| - totalGpuMemo ry | Float | 4444.0 | 资源池的显存总数。 |
| -totalMemory | Float | 47777.0 | 资源池的内存总数。 |
| -cpuDetails | Struct | {} | Cpu详情。 |
| --available | Float | 22.0 | 配额内存剩余数量。 |
| -- dedicatedQuot aUsage | Float | 0.3 | 独占配额内存利用率。 |
| -- dedicatedQuot aUsed | Float | 14.0 | 独占配额内存使用。 |
| -- sharedPoolUsa ge | Float | 0.6 | 共享配额内存利用率。 |
| -- sharedPoolUse d | Float | 4.0 | 共享配额内存使用。 |
| --total | Float | 1.0 | 配额内存总数。 |
| --usage | Float | 1.0 | 配额内存利用率。 |
| --used | Float | 1.0 | 配额内存使用。 |
| -gpuDetails | Struct | {} | Gpu信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| --available | Float | 22.0 | 配额内存剩余数量。 |
|---|---|---|---|
| -- dedicatedQuot aUsage | Float | 0.3 | 独占配额内存利用率。 |
| -- dedicatedQuot aUsed | Float | 14.0 | 独占配额内存使用。 |
| -- sharedPoolUsa ge | Float | 0.6 | 共享配额内存利用率。 |
| -- sharedPoolUse d | Float | 4.0 | 共享配额内存使用。 |
| --total | Float | 1.0 | 配额内存总数。 |
| --usage | Float | 1.0 | 配额内存利用率。 |
| --used | Float | 1.0 | 配额内存使用数量。 |
| - gpumemoryDe tails | Struct | {} | 显存信息。 |
| --available | Float | 22.0 | 配额内存剩余数量。 |
| -- dedicatedQuot aUsage | Float | 0.3 | 独占配额内存利用率。 |
| -- dedicatedQuot aUsed | Float | 14.0 | 独占配额内存使用数量。 |
| -- sharedPoolUsa ge | Float | 0.6 | 共享配额内存利用率。 |
| -- sharedPoolUse d | Float | 4.0 | 共享配额内存使用数量。 |
| --total | Float | 1.0 | 配额内存总数。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --usage | Float | 1.0 | 配额内存利用率。 |
| --used | Float | 1.0 | 配额内存使用数量。 |
| - memoryDetail s | Struct | {} | 内存信息。 |
| --available | Float | 22.0 | 配额内存剩余数量。 |
| -- dedicatedQuot aUsage | Float | 0.3 | 独占配额内存利用率。 |
| -- dedicatedQuot aUsed | Float | 14.0 | 独占配额内存使用数量。 |
| -- sharedPoolUsa ge | Float | 0.6 | 共享配额内存利用率。 |
| -- sharedPoolUse d | Float | 4.0 | 共享配额内存使用数量。 |
| --total | Float | 1.0 | 配额内存总数。 |
| --usage | Float | 1.0 | 配额内存利用率。 |
| --used | Float | 1.0 | 配额内存使用数量。 |

**示例**

请求示例

```
GET /resource/statics/poolSystemResourceOverview HTTP/1.1 &poolId=rp-xc8x89sva*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "sharedPoolTotalGpu":8.0,
  "cpuDetails":{
   "sharedPoolUsed":4.0,
   "dedicatedQuotaUsed":14.0,
"total":10
```

智能体工厂 OpenTrek

```json
   total:1.0,
   "dedicatedQuotaUsage":0.3,
   "usage":1.0,
   "available":22.0,
   "used":1.0,
   "sharedPoolUsage":0.6
  },
  "sharedPoolTotalGpuMemory":255.0,
  "totalCpuCount":4.0,
  "shareNodeCount":1,
  "gpuDetails":{
   "sharedPoolUsed":4.0,
   "dedicatedQuotaUsed":14.0,
   "total":1.0,
   "dedicatedQuotaUsage":0.3,
   "usage":1.0,
   "available":22.0,
   "used":1.0,
   "sharedPoolUsage":0.6
  },
  "sharedPoolTotalCpu":16.0,
  "sharedPoolTotalMemory":474.0,
  "totalMemory":47777.0,
  "totalGpuCount":4.0,
  "totalGpuMemory":4444.0,
  "memoryDetails":{
   "sharedPoolUsed":4.0,
   "dedicatedQuotaUsed":14.0,
   "total":1.0,
   "dedicatedQuotaUsage":0.3,
   "usage":1.0,
   "available":22.0,
   "used":1.0,
   "sharedPoolUsage":0.6
  },
  "nodeCount":2,
  "gpumemoryDetails":{
   "sharedPoolUsed":4.0,
   "dedicatedQuotaUsed":14.0,
   "total":1.0,
   "dedicatedQuotaUsage":0.3,
   "usage":1.0,
   "available":22.0,
   "used":1.0,
   "sharedPoolUsage":0.6
  },
  "gpuTypes":"[NVIDIA_Ampere_A100_80G_NVLink]"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### GetPoolGPUUtilization

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET|POST /resource/statics/quotaFragment HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| poolId | Strin g | Query | 是 | rp-**** | 资源池ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -nodeList | Array | [{}] | 节点信息。 |
| -- gpuMemTotal | Float | 56 | 总显存。 |
| --gpuTotal | Integer | 658 | GPU总数。 |
| --nodeName | String | i-nnnn**** | 节点的名称。 |
| -- gpuMemUsed | Struct | 58 | 已使用显存。 |
| --gpuUsed | Struct | 59 | 已使用GPU。 |
| -quotaId | String | rq-d8890a927**** | 配额ID。 |
| -timestamp | Integer | 2017-12- 10T20:00:00Z | 时间。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET|POST /resource/statics/quotaFragment HTTP/1.1 &poolId=rp-****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 共享节点池

##### AddSharedResourcePoolNodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/shared-pool/[resourcePoolId]/nodes/add HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0d60eeba**** | 资源池ID。 |
| nodeList | Json | Body | 是 | [ { "nodeName": "i- cupea****", "nodeId": "i- ***" } ] | 节点列表, 该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/shared-pool/[resourcePoolId]/nodes/add HTTP/1.1 { "resourcePoolId":"rp-bc47fd6f0d60eeba****", "nodeList":"[
  {
    "nodeName": "i-cupea****",
    "nodeId": "i-***"
  }
```

`]"`

```
}
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### RemoveSharedResourcePoolNodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/shared-pool/[resourcePoolId]/nodes/remove HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp-**** | 资源池ID，该参数必填。 |
| nodeList | Json | Body | 是 | [ { "nodeName": "i- cupea****", "nodeId": "i- ***" } ] | 节点列表，该参数必填。 |
| dryRun | Boole an | Body | 否 | false | 如果dryRun为false，如果校验失败，直接抛出参数非法如果dryRun为true，如果校验失败，则返回 data数据 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| errorCode | String | 500 | 错误码。 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/shared-pool/[resourcePoolId]/nodes/remove HTTP/1.1 { "resourcePoolId":"rp-****", "nodeList":"[
  {
    "nodeName": "i-cupea****",
    "nodeId": "i-***"
  }
```

`]"`

```
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 三方资源配置

##### UpdateThirdPartyStorage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /resource/pool/update/thirdPartyStorage/[resourcePoolId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeba63**** | 资源池ID。 |
| thirdParty StorageLis t | Json | Body | 否 | [ { "storageId":"a12****", "storageSubPath":"/aistu dio/third/****", "mountPath":"/kea/traini ng/****" } ] | 三方存储列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/pool/update/thirdPartyStorage/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-bc47fd6f0af720435c0a4d60eeba63****" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### UpdateResourcePoolThirdPartyRdma

调用UpdateResourcePoolThirdPartyRdma修改指定资源池第三方RDMA配置信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/pool/update/thirdPartyRdma/[resourcePoolId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceP oolId | Strin g | Path | 是 | rp- bc47fd6f0af720435c0a4 d60eeb**** | 资源池ID。 |
| thirdParty Rdma | Boole an | Body | 是 | true | 表示是否启用第三方 RDMA，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
POST /resource/pool/update/thirdPartyRdma/[resourcePoolId] HTTP/1.1 { "resourcePoolId":"rp-bc47fd6f0af720435c0a4d60eeb****", "thirdPartyRdma":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 资源组

#### GetResourceQuotaList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Query | 否 | rq-394cb9****04499 | 资源配额ID，资源配额的唯一标识符。 |
| resourceQ uotaName | Strin g | Query | 否 | test-A100测试配额-0202 | 资源配额名称。 |
| resourceP oolId | Strin g | Query | 否 | rp-ddf453****049f4 | 资源池ID，资源配额所属资源池的唯一标识符。 |
| resourceP oolName | Strin g | Query | 否 | A100资源池-新 | 资源池名称。 |
| tag | Strin g | Query | 否 | "" | 资源配额标签。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 资源池列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| scheduleS trategy | Integ er | Query | 否 | 0 | 2：优先级排序。 0：严格时序。 1：遍历轮询。 2：优先级排序。 |
| quantizeS trategy | Integ er | Query | 否 | [0,1,2] | 量化策略列表，JSON数组格式字符串。 0: Int4-W4A16 1: Int8-W8A16 2: FP8-Wfp8Afp8 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| isUseShar edPool | Integ er | Query | 否 | 0 | 1：共享。 0：否 1：是默认值：0。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| vpcId | Strin g | Query | 否 | vpc-******** | VPC ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - quantizeMetho dList | List | [1] | 支持的量化方法列表。 |
| - quantizeStrate gyList | List | [0] | 支持的量化策略列表。 |
| - thirdPartyStor ageList | Array | [] | 三方存储列表。 |
| -- occupantIdList | List | ["os-xxxxx"] | 存储挂载信息列表。 |
| -- storageCluster | String | H3C | 存储集群。 |
| --storageId | String | 1 | 存储ID。 |
| --storagePath | String | /data | 存储路径。 |
| -- storageProvid er | String | H3C | 存储提供方。 |
| - bmcpClusterId | String | ack-r6vw****h4ab | BMCP集群ID。 |
| -clusterId | String | c7ad28ca****e501 3 | ACK集群ID。 |
| -dataAccCount | Integer | 0 | 该资源配额上的数据加速任务数量。 |
| -gpuCount | Integer | 8 | 资源配额的GPU显卡数量。 |
| -gpuType | String | NVIDIA Hopper H1 _ _ 00 NVLink _ | GPU型号名称。 |
| -isStained | Boolean | false | 资源配额节点是否已打污点标记。 |
| - isUseSharedPo ol | Integer | 0 | 是否为共享配额。 0: 独占。 1: 共享。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -nodeCount | Integer | 1 | 资源配额关联的节点数量。 |
| - quotaCpuCoun t | Integer | 192 | 资源配额的CPU核心数。 |
| - quotaMemCou nt | Integer | 2048 | 资源配额的内存大小，单位为GB。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域ID，资源所在的地域标识。 |
| - resourcePoolId | String | rp- ddf453****049f4 | 资源池ID，资源配额所属资源池的唯一标识符。 |
| - resourcePoolN ame | String | A100资源池-新 | 资源池名称。 |
| - resourceQuota Description | String | resourceQuota- desc | 资源配额描述信息。 |
| - resourceQuota GmtCreate | String | 2026-02- 02T11:40:26Z | 资源配额的创建时间，格式为 UTC 时间。 |
| - resourceQuota GpuMem | Integer | 640 | 资源配额的显存大小，单位为GB。 |
| - resourceQuota Id | String | rq- 394cb9****04499 | 资源配额ID，资源配额的唯一标识符。 |
| - resourceQuota Name | String | test-A100测试配额- 0202 | 资源配额名称。 |
| - resourceQuota Status | String | Running | 资源配额的运行状态。 |
| - resourceQuota Type | Integer | 0 | 资源配额类型。 0: 模型训练。 1: 模型推理。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -resourceType | Integer | 0 | 资源类型。 0: BMCP高网。 1: BMCP基础。 2: BMCP纳管。 3: EGS。 5: Aspeed。 |
| - scheduleStrate gy | Integer | 0 | 调度策略，取值范围： 0：严格时序。 1：遍历轮询。 2：优先级排序。 |
| -shared | Integer | 0 | 共享状态。 0: 独占。 1: 共享。 |
| -taskCount | Integer | 1 | 该资源配额上正在运行的任务数量。 |
| - usageCpuCou nt | Float | 11.5 | 当前已使用的CPU核数。 |
| - usageGpuCou nt | Float | 2.0 | 当前已使用的GPU数量。 |
| - usageGpuMem Count | Float | 160.0 | 当前已使用的GPU显存大小，单位为GB。 |
| - usageMemCou nt | Float | 248.0 | 当前已使用的内存大小，单位为GB。 |
| -vpcId | String | vpc-2ze****kz | VPC网络ID。 |
| -gpuInfo | Struct | {} | GPU信息。 |
| --gpu | String | NVIDIA Ampere A1 _ _ 00 80G NVLink _ _ | GPU芯片名称。 |
| -- manufacturer | String | NVIDIA | 厂商。 |
| -- manufacturerC N | String | 英伟达 | 厂商中文名。 |
| -- manufacturerT W | String | 英偉達 | 厂商英文名。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 资源配额的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 资源配额的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例

#### GetQuotaNodeAllocatables

调用GetQuotaNodeAllocatables查询配额下各节点的可分配资源量信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Query | 是 | rq- f9b8861009a3504ad908 9d30ed78**** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | { "cpuAllocatableMa x": 8.0, "memoryAllocatabl eMax": 32.0, "gpuAllocatableMa x": 8 } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - cpuAllocatable Max | Float | 1.0 | 单节点CPU可分配最大值。 |
| - memoryAlloca tableMax | Float | 1.0 | 单节点内存可分配最大值。 |
| - gpuAllocatable Max | Integer | 8 | 单节点GPU可分配最大值。 |

**示例**

请求示例

```
GET /resource/quota/nodeAllocatables HTTP/1.1 &resourceQuotaId=rq-f9b8861009a3504ad9089d30ed78****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "memoryAllocatableMax":1.0,
  "gpuAllocatableMax":8,
  "cpuAllocatableMax":1.0
 },
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListQuotaNodeResources

调用ListQuotaNodeResources查询配额下所有节点的资源使用信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Query | 是 | rq- b6d3a3ee01b8a049690 a62e07ab**** | 资源配额ID。 |
| orderByFi eld | Strin g | Query | 否 | cpu | 排序字段。 默认值：cpu。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [ { "nodeName": "cn-wulan- env38g1- d02.192.168.11.16 8", "nodeStatus": "Ready", "cpuAllocatable": 24.5, "memoryAllocatabl e": 96.0, "gpuAllocatable": 6, "gpuMemoryAlloca table": 6.0 } ] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -nodeName | String | i-fhsdfu832***** | 节点名称。 |
| -nodeStatus | String | Ready | 节点运行状态。 |
| - cpuAllocatable | Float | 2.0 | 节点CPU可分配值。 |
| - memoryAlloca table | Float | 23.0 | 节点内存可分配值。 |
| - gpuAllocatable | Integer | 6 | 节点GPU可分配值。 |
| - gpuMemoryAll ocatable | Float | 3.0 | 节点显存可分配值。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /resource/quota/nodeResourceList HTTP/1.1 &resourceQuotaId=rq-b6d3a3ee01b8a049690a62e07ab****
```

&公共请求参数智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "nodeName":"i-fhsdfu832*****",
   "memoryAllocatable":23.0,
   "gpuMemoryAllocatable":3.0,
   "gpuAllocatable":6,
   "nodeStatus":"Ready",
   "cpuAllocatable":2.0
  }
```

`],`

```json
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ChangeResourceQuotaConfiguration

调用ChangeResourceQuotaConfiguration修改指定资源配额的变更配置信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/quota/change/configuration HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Body | 是 | rq- b6d3a3ee01b8a049690 a62e07ab**** | 资源配额ID，该参数必填。 |
| nodeSelec tMode | Integ er | Body | 是 | 0 | 节点类型，该参数必填，取值范围： 0：手动选择。 1：自动选择。 当节点类型为0 时，nodeList不能为空。 |
| gpuCount | Integ er | Body | 是 | 4 | gpu大小，单位为卡，该参数必填。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuCount | Integ er | Body | 是 | 4 | cpu大小，单位为核，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 8 | 内存大小，单位为GB，该参数必填。 |
| nodeList | Json | Body | 否 | [{ "nodeName": "i- cupeam6heob****", "memCount": 2048, "gpuMemCount": 1536, "available": false, "nodeType": "", "nodeStatus": "READY", "gpuInfo": { "manufacturerCN": "APG", "gpu": "PG1 A910E", _ "resourcePoolType": "裸金属", "manufacturer": "APG" }, "createTime": "2025-03-12T12:36:00", "nodeId": "i- cupeam6heob2*****", "gpuCount": 16, "cpuCount": 192, "gpuType": "PG1 A910E", "value": _ "i-cupeam6heob*****", "label": "i- cupeam6heob*****", "disabled": false }] | 节点列表。 |
| cpuRange Min | Integ er | Body | 否 | 1 | CPU配额的最小范围。 |
| cpuRange Max | Integ er | Body | 否 | 1 | CPU配额的最大范围。 |
| memoryR angeMin | Integ er | Body | 否 | 1 | 内存配额的最小范围。 |
| memoryR angeMax | Integ er | Body | 否 | 1 | 内存配额的最大范围。 |
| gpuRange Min | Integ er | Body | 否 | 1 | GPU配额的最小范围。 |
| gpuRange Max | Integ er | Body | 否 | 1 | GPU配额的最大范围。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/quota/change/configuration HTTP/1.1 { "resourceQuotaId":"rq-b6d3a3ee01b8a049690a62e07ab****", "nodeSelectMode":"0", "gpuCount":"4", "cpuCount":"4", "memCount":"8" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateResourceQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
POST /resource/quota/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaName | Strin g | Body | 是 | resourceQuota-name | 资源配额名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| resourceQ uotaDescr iption | Strin g | Body | 否 | resourceQuota-desc | 资源配额描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| resourceQ uotaType | Integ er | Body | 是 | 0 | 资源配额类型，该参数必填，取值范围： 0：模型训练。 1：模型推理。 |
| resourceT ype | Integ er | Body | 是 | 0 | 资源池类型，该参数必填， 取值范围： 0：裸金属。 1：EGS。 |
| scheduleS trategy | Integ er | Body | 是 | 0 | 调度策略，该参数必填，取值范围： 0：FIFO。 1：round robin。 2：priority。 |
| resourceP oolId | Strin g | Body | 是 | rp- 3b1b89140391204e050 984f0b524**** | 资源池ID，该参数必填。 |
| nodeSelec tMode | Integ er | Body | 是 | 0 | 节点类型，该参数必填，取值范围： 0：手动选择。 当节点类型为0 时，nodeList不能为空。 |
| quotaCPU Count | Integ er | Body | 是 | 4 | cpu大小，单位为核，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaMe mCount | Integ er | Body | 是 | 4 | 内存大小，单位为GB，该参数必填。 |
| gpuCount | Integ er | Body | 是 | 2 | gpu大小，单位为卡，该参数必填。 |
| nodeList | Json | Body | 否 | [{ "nodeName": "i- coev0ueb****", "memCount": 1007, "createTime": "2024-07- 19T12:21:25", "gpuMemCount": 0, "available": false, "nodeType": "", "nodeStatus": "READY", "nodeId": "i- coev0ueheob7****", "gpuCount": 8, "cpuCount": 128, "gpuType": "NVIDIA A100-*****" }] | 节点列表。 |
| featureIdL ist | Json | Body | 否 | [1, 2, 3] | 手动选择启动的特性时，该字段不能为空，默认不填。 |
| useShared Pool | Boole an | Body | 否 | true | 是否使用共享节点池节点， 取值范围： true: 是代表共享资源配额，不需要指定具体的节点，只需要设置CPU、Memory、GPU的范围，一下 cpuRangeMin、 cpuRangeMax、 memoryRangeMin、 memoryRangeMax、 gpuRangeMin、 gpuRangeMax字段生效。 false: 否代表独占资源配额，需要指定具体节点，以下 quotaCPUCount、 quotaMemCount、 gpuCount、nodeList字段生效。 |
| cpuRange Min | Integ er | Body | 否 | 1 | CPU配额的最小范围。 |

| A | I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cpuRange Max | Integ er | Body | 否 | 1 | CPU配额的最大范围。 |
| memoryR angeMin | Integ er | Body | 否 | 1 | 内存配额的最小范围。 |
| memoryR angeMax | Integ er | Body | 否 | 1 | 内存配额的最大范围。 |
| gpuRange Min | Integ er | Body | 否 | 1 | GPU配额的最小范围。 |
| gpuRange Max | Integ er | Body | 否 | 1 | GPU配额的最大范围。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"resourceQuotaId ": "rq-****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /resource/quota/create HTTP/1.1 { "resourceQuotaName":"resourceQuota-name", "resourceQuotaType":"0", "resourceType":"0", "scheduleStrategy":"0", "resourcePoolId":"rp-3b1b89140391204e050984f0b524****", "nodeSelectMode":"0", "quotaCPUCount":"4", "quotaMemCount":"4", "gpuCount":"2" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"resourceQuotaId\": \"rq-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteResourceQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /resource/quota/delete/[resourceQuotaId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Path | 是 | rq- f9b8861009a3504ad908 9d30ed**** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /resource/quota/delete/[resourceQuotaId] HTTP/1.1 &resourceQuotaId=rq-f9b8861009a3504ad9089d30ed****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetResourceQuotaDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/quota/detail/[resourceQuotaId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Path | 是 | rq-394cb9****04499 | 资源配额ID，资源配额的唯一标识符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -featureVOList | Array | [] | 资源配额关联特性列表。 |
| --ackClusterId | String | cef51d60a4***** | ACK集群ID。 |
| -- bmcpClusterId | String | ack-r6vw****h4ab | BMCP集群ID。 |
| --canClose | Integer | 1 | 是否可关闭。 0: 不可关闭。 1: 可关闭。 |
| --canOpen | Integer | 1 | 是否可打开。 0: 不可打开。 1: 可打开。 |
| -- featureDescrip tion | String | GPU共享使用，为任务按照显存大小分配。 | 特性描述。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --featureName | String | GpuShare | 特性名称。 |
| -- featureNameC n | String | GPU共享（物理切分 &软件虚拟） | 特性中文名。 |
| -- featureNameT W | String | GPU共享（物理切分 &軟件虛擬） | 特性繁体名称。 |
| -- featureOriginN ame | String | ResourceQuotaFea ture-GpuShare | 特性原始名称。 |
| -- featureRunnin gDetails | String | "" | 特性执行详情。 |
| --featureStatus | String | DONE | 特性当前状态。 INIT: 初始化。 NONE: 关闭。 DOING: 正在执行。 UNDOING: 正在卸载。 DONE: 执行完成。 |
| --featureStep | String | "" | 特性运行步骤。 |
| -- featureTarget Status | Integer | 1 | 特性目标状态。 -1: 特性不支持。 0: 特性关闭。 1: 特性开启。 |
| --gmtCreated | String | 2025-10-20 06:44:51 | 创建时间。 |
| --gmtModified | String | 2025-11-03 01:54:05 | 修改时间。 |
| --id | Integer | 1 | 特性实例ID。 |
| --resourceId | String | rq-xxxxxx | 关联资源ID。 |
| --visible | Integer | 0 | 是否可见。 0: 不可见。 1: 可见。 |
| - bmcpClusterId | String | ack-r6vw****h4ab | BMCP集群ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| -clusterId | String | c7ad28ca****e501 3 | ACK集群ID。 |
|---|---|---|---|
| -createUser | String | 198226****1225 | 创建用户的账号ID。 |
| -gpuCount | Integer | 8 | 资源配额的GPU显卡数量。 |
| -gpuType | String | NVIDIA Hopper H1 _ _ 00 NVLink _ | GPU型号名称。 |
| - isUseSharedPo ol | Integer | 0 | 共享状态 0: 独占。 1: 共享。 |
| -nodeCount | Integer | 1 | 资源配额关联的节点数量。 |
| - quantizeMetho d | String | [0,1] | 量化方法列表，JSON数组格式字符串。 |
| - quantizeStrate gy | String | [0,1,2] | 量化策略列表，JSON数组格式字符串。 |
| - quotaCpuCoun t | Integer | 192 | 资源配额的CPU核心数。 |
| - quotaMemCou nt | Integer | 2048 | 资源配额的内存大小，单位为GB。 |
| -regionId | String | cn-hangzhou | 地域ID，资源所在的地域标识。 |
| - resourcePoolId | String | rp- ddf453****049f4 | 资源池ID，资源配额所属资源池的唯一标识符。 |
| - resourcePoolN ame | String | 资源配额名称 | 资源池名称。 |
| - resourceQuota Description | String | 资源配额描述。 | 资源配额描述信息。 |
| - resourceQuota GmtCreate | String | 2026-02- 02T11:40:26Z | 资源配额的创建时间，格式为 UTC 时间。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - resourceQuota GpuMem | Integer | 640 | 资源配额的显存大小，单位为GB。 |
| - resourceQuota Id | String | rq- 394cb9****04499 | 资源配额ID，资源配额的唯一标识符。 |
| - resourceQuota Name | String | test-A100测试配额- 0202 | 资源配额名称。 |
| - resourceQuota Type | Integer | 0 | 资源配额类型。 0：模型推理。 1：模型推理。 |
| -resourceType | Integer | 0 | 资源类型。 0: BMCP高网。 1: BMCP基础。 2: BMCP纳管。 3: EGS。 5: Aspeed。 |
| - scheduleStrate gy | Integer | 0 | 调度策略，取值范围： 0：严格时序。 1：遍历轮询。 2：优先级排序。 |
| -vpcId | String | vpc-2ze****kz | VPC网络ID。 |
| -quotaStatus | Struct | {} | 配额状态信息。 |
| --cpuCount | Float | 128 | CPU总核数。 |
| --cpuUnUsed | Float | 30 | CPU未使用数。 |
| --gpuCount | Integer | 8 | 资源配额的GPU显卡数量。 |
| --gpuUnUsed | Integer | 2 | 表示当前GPU未被使用的数量。未虚拟化显示卡数，虚拟化后显示显存数（GiB）。 |
| --memCount | Float | 200 | 内存总数（GiB）。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --memUnUsed | Float | 100 | 内存未使用数（GiB）。 |
| -- resourceQuota Id | String | rq- 394cb9****04499 | 资源配额ID，资源配额的唯一标识符。 |

**示例**

请求示例

```
GET /resource/quota/detail/[resourceQuotaId] HTTP/1.1 &resourceQuotaId=rq-f9b8861009a3504ad9089d30ed78****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "quotaCpuCount":"",
  "resourceQuotaDescription":"",
  "resourceQuotaGmtCreate":"",
  "clusterId":"",
  "quotaMemCount":"",
  "resourceQuotaType":"",
  "bmcpClusterId":"",
  "resourceQuotaName":"",
  "scheduleStrategy":"",
  "vpcId":"",
  "nodeCount":"",
  "resourceQuotaGpuMem":"",
  "quotaStatus":{
   "memCount":"",
   "gpuUnUsed":"",
   "resourceQuotaId":"",
   "cpuUnUsed":"",
   "memUnUsed":"",
   "gpuCount":"",
   "cpuCount":""
  },
  "gpuCount":"",
  "gpuType":"",
  "isUseSharedPool":"",
  "resourcePoolName":"",
  "quantizeStrategy":"",
  "regionId":"",
  "featureVOList":[
   {
    "canClose":"",
    "gmtModified":"",
    "resourceId":"",
```

智能体工厂 OpenTrek

```json
    "visible":"",
    "featureName":"",
    "featureStep":"",
    "gmtCreated":"",
    "featureStatus":"",
    "featureDescription":"",
    "featureRunningDetails":"",
    "ackClusterId":"",
    "featureOriginName":"",
    "bmcpClusterId":"",
    "featureNameCn":"",
    "featureTargetStatus":"",
    "canOpen":"",
    "featureNameTW":"",
    "id":""
   }
```

`],`

```json
  "quantizeMethod":"",
  "resourcePoolId":"",
  "resourceQuotaId":"",
  "createUser":"",
  "resourceType":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateResourceQuota

调用UpdateResourceQuota修改指定资源配额的部分信息，包括资源配额名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/quota/update/[resourceQuotaId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaId | Strin g | Path | 是 | rq- a102a9700ae6a040d70 84f20e336**** | 资源配额ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceQ uotaName | Strin g | Body | 是 | resourceQuota-name | 资源配额名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| resourceQ uotaDescr iption | Strin g | Body | 否 | resourceQuota-desc | 资源配额描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/quota/update/[resourceQuotaId] HTTP/1.1 { "resourceQuotaId":"rq-a102a9700ae6a040d7084f20e336****", "resourceQuotaName":"resourceQuota-name" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetQuotaGPUType

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| - canSupportGp uShare | Boolean | true | 是否支持虚拟化。 |
| -frontStep | String | 1 | 前端滑块步长。 |
| -frontStepUnit | String | GiB | 前端滑块步长单位。 |
| - gpuShareType | String | CGPU VIRTUALIZA _ TION SHARE _ | GPU共享类型。 |
| - idealResource Name | String | aliyun.com/gpu- mem | 目标资源名称。 |
| - idealResource Step | String | 128 | 目标资源步长。 |
| - idealResource Unit | String | MiB | 目标资源单位。 |
| -maxSpace | String | 80 | 最大分配。 |
| -minSpace | String | 1 | 最小分配。 |
| - quotaGpuStat us | Integer | 1 | GPU切分状态。 0: 未切分。 1: 已切分。 2: 切分中。 |
| - rawResourceN ame | String | nvidia.com/gpu | 原始资源名称。 |
| - rawResourceU nit | String | "" | 原始资源单位，默认为空，表示卡。 |

**示例**

请求示例

```
&quotaId=rq-d8890a98089c2041d8086bb0b2e27****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 资源组统计

##### GetQuotaTaskResourceConsumption

调用GetQuotaTaskResourceConsumption查询指定资源配额任务资源消耗统计。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/quotaTaskResourceConsumption HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 是 | rq-d8890a98089***** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuShare | Boolean | true | GPU共享是否开启。 |
| - batchInferenc eJob | Struct | {} | 批量推理信息。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |
| -notebook | Struct | {} | Notebook信息。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |
| -onlineService | Struct | {} | OnlineService信息。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |
| -other | Struct | {} | Other。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |
| -pipelineDraft | Struct | {} | PipelineDraft信息。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |
| -task | Struct | {} | 任务建模信息。 |
| --cpuUsed | Float | 3.0 | CPU使用。 |
| -- gpuMemoryUs ed | Float | 3.0 | 显存使用。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --gpuUsed | Float | 3.0 | GPU使用。 |
| --memoryUsed | Float | 3.0 | 内存使用。 |
| --taskCount | Integer | 3 | 任务数。 |

**示例**

请求示例

```
GET /resource/statics/quotaTaskResourceConsumption HTTP/1.1 &quotaId=rq-d8890a98089*****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "task":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  },
  "onlineService":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  },
  "notebook":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  },
  "pipelineDraft":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  },
  "gpuShare":true,
  "batchInferenceJob":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  },
  "other":{
   "gpuMemoryUsed":3.0,
   "gpuUsed":3.0,
   "taskCount":3,
   "cpuUsed":3.0,
   "memoryUsed":3.0
  }
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### GetQuotaResourceOverview

调用GetQuotaResourceOverview查询指定资源配额资源概览详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/quotaResourceOverview HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 是 | rq-ddfeea0e021760***** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gpuShare | Boolean | true | 是否GPU共享。 |
| -id | String | rq-d6cfb4*** | 配额ID。 |
| - isUseSharedPo ol | Boolean | true | 是否是共享资源池。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -name | String | test | 配额名称。 |
| -nodeCount | Integer | 5 | 节点个数。 |
| -cpuDetails | Struct | {} | CPU详情。 |
| --available | Float | 32.0 | 剩余量。 |
| -- availableCapa city | Float | 32.0 | 可用余量-共享配额参数。 |
| -- guaranteedCa pacity | Float | 32.0 | 强保证可用余量-共享配额参数。 |
| --max | Float | 32.0 | 最大值-共享配额参数。 |
| --min | Float | 32.0 | 最小值-共享配额参数。 |
| --pending | Float | 32.0 | Pending量-共享配额参数。 |
| --poolTotal | Float | 32.0 | 共享资源池总量。 |
| --total | Float | 32.0 | 配额总量。 |
| --usage | Float | 0.69 | 使用率。 |
| --used | Float | 32.0 | 使用量。 |
| -gpuDetails | Struct | {} | GPU信息。 |
| --available | Float | 32.0 | 剩余量。 |
| -- availableCapa city | Float | 32.0 | 可用余量-共享配额参数。 |
| -- guaranteedCa pacity | Float | 32.0 | 强保证可用余量-共享配额参数。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --max | Float | 32.0 | 最大值-共享配额参数。 |
| --min | Float | 32.0 | 最小值-共享配额参数。 |
| --pending | Float | 32.0 | Pending量-共享配额参数。 |
| --poolTotal | Float | 32.0 | 共享资源池总量。 |
| --total | Float | 32.0 | 配额总量。 |
| --usage | Float | 0.69 | 使用率。 |
| --used | Float | 32.0 | 使用量。 |
| - gpumemoryDe tails | Struct | {} | 显存信息。 |
| --available | Float | 32.0 | 剩余量。 |
| -- availableCapa city | Float | 32.0 | 可用余量-共享配额参数。 |
| -- guaranteedCa pacity | Float | 32.0 | 强保证可用余量-共享配额参数。 |
| --max | Float | 32.0 | 最大值-共享配额参数。 |
| --min | Float | 32.0 | 最小值-共享配额参数。 |
| --pending | Float | 32.0 | Pending量-共享配额参数。 |
| --poolTotal | Float | 32.0 | 共享资源池总量。 |
| --total | Float | 32.0 | 配额总量。 |
| --usage | Float | 0.69 | 使用率。 |
| --used | Float | 32.0 | 使用量。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - memoryDetail s | Struct | {} | 内存信息。 |
| --available | Float | 32.0 | 剩余量。 |
| -- availableCapa city | Float | 32.0 | 可用余量-共享配额参数。 |
| -- guaranteedCa pacity | Float | 32.0 | 强保证可用余量-共享配额参数。 |
| --max | Float | 32.0 | 最大值-共享配额参数。 |
| --min | Float | 32.0 | 最小值-共享配额参数。 |
| --pending | Float | 32.0 | Pending量-共享配额参数。 |
| --poolTotal | Float | 32.0 | 共享资源池总量。 |
| --total | Float | 32.0 | 配额总量。 |
| --usage | Float | 0.69 | 使用率。 |
| --used | Float | 32.0 | 使用量。 |

**示例**

请求示例

```
GET /resource/statics/quotaResourceOverview HTTP/1.1 &quotaId=rq-ddfeea0e021760*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "isUseSharedPool":true,
  "cpuDetails":{
   "availableCapacity":32.0,
   "total":32.0,
   "min":32.0,
   "guaranteedCapacity":32.0,
```

智能体工厂 OpenTrek

```json
   "max":32.0,
   "pending":32.0,
   "usage":0.69,
   "available":32.0,
   "used":32.0,
   "poolTotal":32.0
  },
  "name":"test",
  "gpuDetails":{
   "availableCapacity":32.0,
   "total":32.0,
   "min":32.0,
   "guaranteedCapacity":32.0,
   "max":32.0,
   "pending":32.0,
   "usage":0.69,
   "available":32.0,
   "used":32.0,
   "poolTotal":32.0
  },
  "memoryDetails":{
   "availableCapacity":32.0,
   "total":32.0,
   "min":32.0,
   "guaranteedCapacity":32.0,
   "max":32.0,
   "pending":32.0,
   "usage":0.69,
   "available":32.0,
   "used":32.0,
   "poolTotal":32.0
  },
  "nodeCount":5,
  "id":"rq-d6cfb4***",
  "gpumemoryDetails":{
   "availableCapacity":32.0,
   "total":32.0,
   "min":32.0,
   "guaranteedCapacity":32.0,
   "max":32.0,
   "pending":32.0,
   "usage":0.69,
   "available":32.0,
   "used":32.0,
   "poolTotal":32.0
  },
  "gpuShare":true
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

##### ListQuotaTaskResource

调用ListQuotaTaskResource查询资源配额概览信息中的所有任务消耗列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/quotaTaskResourceList HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 是 | rq-d8890a98089c20 | 资源配额ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| queryTyp e | Integ er | Query | 否 | CPU | 查询类型，取值范围： CPU。 MEMORY。 GPU。 GPUMEMORY。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 页码。 |
| data | Struct | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -taskList | Array | [{}] | 任务列表。 |
| --cpu | Float | 3.0 | CPU使用。 |
| --department | String | "" | 所属组织。 |
| --gpu | Float | 3.6 | GPU使用。 |
| --gpuMemory | Float | 0.0 | 显存使用。 |
| --memory | Float | 100.3 | 内存使用。 |
| -- resourceGroup | String | "" | 所属资源集。 |
| --status | Integer | 1 | 任务状态。 |
| --taskId | String | os- 18b787be055*** | 任务ID。 |
| --taskName | String | test | 任务名称。 |
| --taskType | Integer | 0 | 任务类型。 |
| -gpuShare | Boolean | true | GPU共享是否开启。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
GET /resource/statics/quotaTaskResourceList HTTP/1.1 &quotaId=rq-d8890a98089c20
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "taskList":[
   {
    "gpuMemory":0.0,
    "resourceGroup":"\"\"",
    "taskType":0,
    "memory":100.3,
    "cpu":3.0,
    "taskName":"test",
    "department":"\"\"",
    "gpu":3.6,
    "taskId":"os-18b787be055***",
    "status":1
   }
```

`],`

```json
  "gpuShare":true
 },
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### 潮汐调度

##### UpdateMoveResourceQuotaStatus

调用UpdateMoveResourceQuotaStatus启用/禁用潮汐调度任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/quota/move/status HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configId | Strin g | Body | 是 | d207a07c | 策略ID，该参数必填。 |
| enable | Boole an | Body | 是 | true | 潮汐调度任务状态，该参数必填，取值范围： true：启用。 false：禁用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/quota/move/status HTTP/1.1 { "configId":"d207a07c", "enable":"true" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### CreateMoveResourceQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/quota/move HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceRes ourceQuot aId | Strin g | Body | 是 | rq-2d6a96e4037***** | 源资源配额ID，该参数必填。 |
| targetRes ourceQuot aId | Strin g | Body | 是 | rq-890195ff095***** | 目标资源配额ID，该参数必填。 |
| sourceNo deList | Json | Body | 是 | [ { "nodeId": "i- j1p01eoza3*****", "nodeName": "cn- neimeng*****1.192.168. 2.122", "nodeType": "ecs.g6x-ft-k*****", "cpuCount": 2, "memCount": 16, "nodeStatus": "READY", "createTime": "2025-07- 14T01:37:11Z" } ] | 移动的节点信息，该参数必填。 |
| deletePod List | Json | Body | 否 | ["pod1", "pod2", "pod3"] | 删除的 Pod 列表。 |
| deleteJobL ist | Json | Body | 否 | ["job001", "job002", "job003"] | 删除的 Job 列表, 移动过程中要删除的任务。 |
| deleteJobT ype | Json | Body | 否 | ["evaluate","finetune"] | 删除的 Job 类型。 |
| sourceTim e | Strin g | Body | 是 | 16:00:00 | 每天正向移动的时间，该参数必填。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| targetTim e | Strin g | Body | 是 | 16:00:00 | 每天反向移动的时间，该参数必填。 |
| name | Strin g | Body | 是 | name | 移动操作名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| descriptio n | Strin g | Body | 否 | "" | 移动操作描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| sourceOut ProtectTi me | Strin g | Body | 是 | 15 | 出让前保护时间，单位分钟，该参数必填。 |
| sourceInPr otectTime | Strin g | Body | 是 | 15 | 回收前保护时间，单位分钟，该参数必填。 |
| sourceJob TypeOutM ap | Json | Body | 是 | { "notebook": 1 } | 从源资源配额到目标资源配额借出时每个任务类型对应的策略，该参数必填。 |
| sourceJob TypeInMa p | Json | Body | 是 | { "notebook": 1 } | 从目标资源配额到源资源配额回收时每个任务类型对应的策略，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```json
POST /resource/quota/move HTTP/1.1 { "sourceResourceQuotaId":"rq-2d6a96e4037*****", "targetResourceQuotaId":"rq-890195ff095*****", "sourceNodeList":"[
    {
      "nodeId": "i-j1p01eoza3*****",
      "nodeName": "cn-neimeng*****1.192.168.2.122",
      "nodeType": "ecs.g6x-ft-k*****",
      "cpuCount": 2,
      "memCount": 16,
      "nodeStatus": "READY",
      "createTime": "2025-07-14T01:37:11Z"
    }
  ]",
"sourceTime":"16:00:00", "targetTime":"16:00:00", "name":"name", "sourceOutProtectTime":"15", "sourceInProtectTime":"15", "sourceJobTypeOutMap":"{
    "notebook": 1
  }",
"sourceJobTypeInMap":"{
    "notebook": 1
  }"
}
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### DeleteMoveResourceQuotaConfig

调用DeleteMoveResourceQuotaConfig删除指定资源配额策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
DELETE /resource/quota/move/status/[configId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configId | Strin g | Path | 是 | 5950d4dc | 策略ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /resource/quota/move/status/[configId] HTTP/1.1 &configId=5950d4dc
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### GetMoveResourceQuotaStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/quota/move/status/[configId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configId | Strin g | Path | 是 | 5950d4dc | 策略ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - moveQuotaSta tusVO | Array | [{}] | 潮汐调度任务列表。 |
| --deadlineTime | String | 2025-01- 02T09:01:02Z | 有效期。 |
| --direction | Integer | 0 | 移动方向：0-借出，1-回收。 |
| --endTime | String | 2017-12- 10T21:00:00Z | 结束时间。 |
| --jobId | String | MOVE QUOTA:ea3 _ a***** | 任务ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| -- schedulerTime | String | 2017-12- 10T21:00:00Z | 调度时间。 |
|---|---|---|---|
| -- sourceQuotaId | String | rq-123**** | 源资源配额ID。 |
| --startTime | String | 2017-12- 10T21:00:00Z | 任务开始时间。 |
| --status | Integer | 0 | 任务状态。 |
| -- targetQuotaId | String | rq-123**** | 目标资源配额ID。 |
| -- ackClusterNod e | Struct | {} | 节点信息。 |
| ---available | Boolean | true | 是否可用。 |
| ---belongsTo | String | myNode | 节点属于哪方。 |
| ---cpuCount | Integer | 16 | CPU总核数。 |
| ---createTime | String | 2024-10- 14T08:00:00Z | 创建时间。 |
| ---gpuCount | Integer | 1 | GPU核数。 |
| --- gpuMemCount | Integer | 8 | 显存大小，单位为GB。 |
| ---gpuType | String | NVIDIA Ampere ** _ _ *** | GPU显卡类型。 |
| ---memCount | Integer | 8 | 内存大小，单位为GB。 |
| ---nodeId | String | i-x****** | 节点ID。 |
| ---nodeName | String | test | 节点的名称。 |
| ---nodeStatus | String | Ready | 节点运行状态。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---nodeType | String | normal | 节点类型。 |
| --- supportVirtStg | String | true | GPU虚拟化。 |
| --- virtualStrategy | String | None | GPU虚拟化策略。 |
| -endTime | String | 2017-12- 10T21:00:00Z | 任务完成时间。 |
| -jobId | String | MOVE QUOTA:ea3 _ a0c6**** | 任务ID。 |
| - sourceQuotaId | String | rq-1234**** | 源资源配额ID。 |
| - sourceQuotaN ame | String | test1 | 源资源配额名称。 |
| -startTime | String | 2017-12- 10T20:00:00Z | 开始时间。 |
| -status | Boolean | true | 状态。 |
| -targetQuotaId | String | rq-123***** | 目标资源配额ID。 |
| - targetQuotaNa me | String | test2 | 目标资源配额名称。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
GET /resource/quota/move/status/[configId] HTTP/1.1 &configId=5950d4dc
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListMoveResourceQuotaConfig

调用ListMoveResourceQuotaConfig查询所有的资源调度策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/quota/move/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sourceRes ourceQuot aId | Strin g | Query | 否 | rq-890195ff095d***** | 源配额ID。 |
| targetRes ourceQuot aId | Strin g | Query | 否 | rq-890195ff095da***** | 目标配额ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

| A | I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - scheduleNode s | Array | [{}] | 调度的节点列表。 |
| --available | Boolean | true | 是否可用。 |
| --belongsTo | String | myNode | 表示节点属于哪方。 |
| --cpuCount | Integer | 16 | CPU总核数。 |
| --createTime | String | 2024-10- 14T08:00:00Z | 创建时间。 |
| --gpuCount | Integer | 4 | GPU个数。 |
| -- gpuMemCount | Integer | 8 | 显存大小，单位为GB。 |
| --gpuType | String | NVIDIA Ampere ** _ _ *** | GPU显卡类型。 |
| --memCount | Integer | 8 | 内存大小，单位为GB。 |
| --nodeId | String | r-x****-db-0 | 节点ID。 |
| --nodeName | String | test | 节点的名称。 |
| --nodeStatus | String | Running | 节点运行状态，取值如下。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --nodeType | String | normal | 节点类型。 |
| -- supportVirtStg | String | true | GPU虚拟化支持。 |
| -- virtualStrategy | String | None | GPU虚拟化策略。 |
| -aliyunUid | String | 157123456789**** | 阿里云用户ID。 |
| -configId | String | 6295 | 配置ID。 |
| -currentStatus | Integer | 1 | 当前状态。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| -gmtModified | String | 2017-11- 27T06:51:26Z | 修改时间。 |
| -name | String | test | 名称。 |
| - scheduleNode Count | Integer | 2 | 调度的节点数。 |
| -scheduleType | String | MOVE QUOTA _ | 调度配置类型。 |
| - sourceInProtec tTime | Integer | 15 | 回收前保护时间，单位分钟。 |
| - sourceOutProt ectTime | Integer | 15 | 出让保护时间，单位分钟。 |
| - sourceResourc eId | String | rq-123*** | 源资源配额ID。 |
| - sourceResourc eName | String | test1 | 源资源配额名称。 |
| -sourceTime | String | 22:00:00 | 出让时间。 |
| - targetResourc eId | String | rq-abc*** | 目标资源配额ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - targetResourc eName | String | test1 | 目标资源配额名称。 |
| -targetStatus | Integer | 1 | 状态：0 表示禁用 1 表示启用。 |
| -targetTime | String | 02:03:00 | 回收时间。 |
| - recycleStrateg y | Struct | {} | 回收策略。 |
| --model- convert | Integer | 2 | 模型转换策略。 |
| - scheduleStrate gy | Struct | {} | 借出策略。 |
| --notebook | Integer | 1 | Notebook建模策略。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 资源调度策略的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 资源调度策略的页码。 |

**示例**

请求示例

```
GET /resource/quota/move/list HTTP/1.1
```

&公共请求参数正常返回示例智能体工厂 OpenTrek `JSON` 格式

```json
{
 "data":"[{}]",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

##### UpdateMoveResourceQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/quota/move/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| configId | Strin g | Body | 是 | 5950d4dc | 配置ID，该参数必填。 |
| sourceNo deList | Json | Body | 是 | [ { "nodeId": "i- j1p01eoza339h*****", "nodeName": "cn- neimeng-2****, "nodeType": "ecs.g6x-ft- k*****", "cpuCount": 2, "memCount": 16, "nodeStatus": "READY", "createTime": "2025-07- 14T01:37:11Z" } ] | 从源资源配额出让给目标资源配额的节点列表，该参数必填。 |
| targetNod eList | Json | Body | 否 | [ { "nodeId": "i- xypg1eady121a*****", "nodeName": "cn- neimeng-2****, "nodeType": "ecs.g6x-ft- k*****", "cpuCount": 2, "memCount": 16, "nodeStatus": "READY", "createTime": "2025-07- 14T01:41:12Z" } ] | 从目标资源配额借用给源资源配额的节点列表。 |
| deletePod List | Json | Body | 否 | ["pod-fooadf1*", "pod- xyai3jnd*"] | 要删除的 Pod 列表。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deleteJobL ist | Json | Body | 否 | ["job-anyqesf1c*", "pod- helafa*"] | 要删除的 Job 列表, 移动过程中要删除的任务。 |
| deleteJobT ypeList | Json | Body | 否 | ["tfjob", "job"] | 要删除的 Job 类型。 |
| sourceTim e | Strin g | Body | 是 | 22:00:00 | 每天正向移动的时间，该参数必填。 |
| targetTim e | Strin g | Body | 是 | 22:00:00 | 每天反向移动的时间，该参数必填。 |
| name | Strin g | Body | 是 | name | 策略名，该参数必填。 |
| descriptio n | Strin g | Body | 否 | "" | 策略描述。 |
| sourceOut ProtectTi me | Strin g | Body | 是 | 15 | 出让前保护时间，单位分钟，该参数必填。 |
| sourceInPr otectTime | Strin g | Body | 是 | 15 | 回收前保护时间，单位分钟，该参数必填。 |
| sourceJob TypeOutM ap | Json | Body | 是 | { "notebook": 1 } | 从源资源配额到目标资源配额借出时每个任务类型对应的策略，该参数必填。 |
| sourceJob TypeInMa p | Json | Body | 是 | { "notebook": 1 } | 从目标资源配额到源资源配额回收时每个任务类型对应的策略，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /resource/quota/move/update HTTP/1.1 { "configId":"5950d4dc", "sourceNodeList":"[
    {
      "nodeId": "i-j1p01eoza339h*****",
      "nodeName": "cn-neimeng-2****,
      "nodeType": "ecs.g6x-ft-k*****",
      "cpuCount": 2,
      "memCount": 16,
      "nodeStatus": "READY",
      "createTime": "2025-07-14T01:37:11Z"
    }
  ]",
"sourceTime":"22:00:00", "targetTime":"22:00:00", "name":"name", "sourceOutProtectTime":"15", "sourceInProtectTime":"15", "sourceJobTypeOutMap":" {
    "notebook": 1
  }",
"sourceJobTypeInMap":" {
    "notebook": 1
  }"
}
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### 优先级调度

智能体工厂 OpenTrek

##### ModifyPriorityQueue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /task/priority/queue/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Body | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID，该参数必填。 |
| taskList | Json | Body | 是 | [{ "taskId": "tk- s01e868a0e7c8****", "queueUnitName": "name", "queueUnitNamespace": "ai-studio", "queueUnitPriority": 0 }] | 任务优先级列表，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /task/priority/queue/update HTTP/1.1 { "quotaId":"rq-d8890a98089c2041d8086bb0b2e27****", "taskList":"[{
 "taskId": "tk-s01e868a0e7c8****",
 "queueUnitName": "name",
 "queueUnitNamespace": "ai-studio",
 "queueUnitPriority": 0
}]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

##### ListPriorityQueue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| quotaId | Strin g | Query | 是 | rq- d8890a98089c2041d80 86bb0b2e27**** | 资源配额ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -taskList | Array | [{}] | 任务列表。 |
| -- autoDiagnosis | Boolean | true | 自动诊断。 |
| -- componentCat egoryId | String | 1001 | AI套件的分类。 |
| --componentId | String | 8 | AI套件的ID。 |
| -- componentNa me | String | test | AI套件的名称。 |
| --cpuCount | Integer | 16 | CPU总核数。 |
| -- elasticFramew ork | String | kea | 弹性框架信息。 |
| --frameWork | Integer | 1 | 框架类型。 |
| --gmtEnd | String | 2024-03- 02T12:12:10Z | 结束时间。 |
| --gpuCount | Integer | 1 | GPU核数。 |
| -- gpuCountUnit | Integer | 1 | 表示GPU数量的计量单位。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- gpuLabelCoun t | Integer | 1 | GPU虚拟化卡数量。 |
| -- gpuMemCount | Integer | 8 | GPU显存大小，单位为GB。 |
| -- gpuMemTotal | Integer | 16 | 显卡总显存容量，单位为GB。 |
| -- gpuMemTotal Unit | Integer | 1 | 表示GPU显存容量的单位。 |
| --gpuType | Integer | 1 | GPU显卡类型。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型。 |
| --imageId | String | image- 05cefd0be2exxxx | 镜像ID。 |
| --imageName | String | vllm | 镜像名称。 |
| --imageType | Integer | 2 | 镜像类型。 |
| -- imageVersion | String | 3.2.41 | 镜像版本。 |
| --isSchedule | Boolean | false | 是否启用定时任务。 |
| --memCount | Integer | 100 | 内存大小，单位为GB。 |
| --nodeCount | Integer | 5 | 节点个数。 |
| --priority | Integer | 5 | 优先级。 |
| --queueStatus | String | active | 队列状态：active、backoff。 |
| -- queueUnitNam e | String | test | 队列名称。 |
| -- queueUnitNam espace | String | ai | 队列命名空间。 |

| I Studio · | API |  | OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- queueUnitPosi tion | Integer | 2 | 表示队列中某个单元在队列中的序号位置。 |
| -- queueUnitPrior ity | Integer | 2 | 任务优先级，1-10。 |
| --quotaId | String | rq-123**** | 配额ID。 |
| --quotaName | String | test-bktest | 配额名称。 |
| --rdmaEnable | Boolean | true | RDMA网络开关。 |
| -- scheduleTime | String | 2023-01- 03T18:00:00Z | 调度时间。 |
| -- sharedMemCo unt | Integer | 20 | 共享内存大小，单位为GB。 |
| --sourceType | Integer | 1 | 任务来源: 0-自定义创建。 1-AI套件。 |
| -- startCommand | String | python3 main.py | 启动命令。 |
| --taskDesc | String | report version is not conform | 任务描述。 |
| --taskId | String | 1002 | 任务ID。 |
| --taskName | String | task1 | 任务名称。 |
| -- taskNodesCou nt | Integer | 3 | 任务占用的节点数量。 |
| --taskStatus | Integer | 1 | 状态： 0 已创建。 1 启动中。 2 运行中。 3 已停止。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --taskType | Integer | 1 | 计划任务类型。取值范围如下： 0 建模任务 。 1 评测任务。 2 离线推理任务。 |
| --tensorboard | Boolean | true | Tensorboard开关。 |
| --trainType | Integer | 0 | 训练类型，取值范围： 0：单机训练。 1：分布式训练。 |
| -quotaId | String | rq-123**** | 资源配额ID。 |

**示例**

请求示例

```
&quotaId=rq-d8890a98089c2041d8086bb0b2e27****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "taskList":[
   {
    "scheduleTime":"2023-01-03T18:00:00Z",
    "taskNodesCount":3,
    "componentId":"8",
    "quotaName":"test-bktest",
    "trainType":0,
    "taskType":1,
    "sharedMemCount":20,
    "gmtEnd":"2024-03-02T12:12:10Z",
    "queueStatus":"active",
    "queueUnitName":"test",
    "nodeCount":5,
    "autoDiagnosis":true,
    "componentName":"test",
    "elasticFramework":"kea",
    "gpuCount":1,
    "imageType":2,
    "cpuCount":16,
    "taskStatus":1,
    "gpuType":1,
```

`"i` i

```
""3241"
```

智能体工厂 OpenTrek

```json
    "imageVersion":"3.2.41",
    "memCount":100,
    "frameWork":1,
    "imageId":"image-05cefd0be2exxxx",
    "imageName":"vllm",
    "gpuMemCount":8,
    "queueUnitPosition":2,
    "quotaId":"rq-123****",
    "gpuMemTotal":16,
    "startCommand":"python3 main.py",
    "componentCategoryId":"1001",
    "priority":5,
    "gpuLabelCount":1,
    "rdmaEnable":true,
    "taskDesc":"report version is not conform",
    "queueUnitPriority":2,
    "tensorboard":true,
    "gpuMemTotalUnit":1,
    "sourceType":1,
    "gpuCountUnit":1,
    "queueUnitNamespace":"ai",
    "taskName":"task1",
    "imageAccelerationType":0,
    "taskId":"1002",
    "isSchedule":false
   }
```

`],`

```json
  "quotaId":"rq-123****"
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 镜像库

#### VerifyImageSig

调用VerifyImageSig验证公共镜像的签名，用于确认镜像文件的完整性和来源可信性。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Query | 是 | img-public- 610952c0441e0ba6a*** ** | 镜像ID。 |
| imageVer sion | Strin g | Query | 是 | 3.2.** | 镜像版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | [{"critical": {"identity": {"docker- reference":"cr- ee.registry.****.en v236.cloud.arm.co m/acr- aipaas/****"},"ima ge":{"docker- manifest- digest":"sha256:2d f822801a13c58a19 22235a624849283 d05ab56c0d7c771f ec********"},"type" :"cosign container image signature"},"option al": {"signer":"aistudio "}}]" | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```
&imageId=img-public-610952c0441e0ba6a***** &imageVersion=3.2.**
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"[{\"critical\":{\"identity\":{\"docker-reference\":\"cr-
ee.registry.****.env236.cloud.arm.com/acr-aipaas/****\"},\"image\":{\"docker-manifest-d igest\":\"sha256:2df822801a13c58a1922235a624849283d05ab56c0d7c771fec********\"},\"type\": cosign container image signature\"},\"optional\":{\"signer\":\"aistudio\"}}]\"",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListImageVersions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| imageId | Strin g | Query | 否 | img-public-437f****48f3 |  | 镜像id。 |  |  |
| imageVer sion | Strin g | Query | 否 | 0.4.7.post1-pytorch2.7- cu128-20250617 |  | 镜像版本。 |  |  |
| imageAcc elerationT ype | Integ er | Query | 否 | 0 |  | 镜像加速类型，枚举值： IMAGE(0) ACCELERATED IMAGE(1) _ 。 0：容器镜像。 1：加速镜像。 默认值：0。 |  |  |
|  |  |  |  |  |  |  | ACCELERATED IMAGE(1) _ |  |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageStat us | Integ er | Query | 否 | 1 | 镜像版本状态，枚举值： CONVERTING(0) NORMAL(1) FAILED(2) UNKNOWN(3) WAITING(4) EXPORTING(5) EXPORT FAILED(6) _ BUILDING(7) 。 0：转换中。 1：正常。 2：转换失败。 3：未知状态。 4：等待中。 |
| hashrateT ype | Integ er | Query | 否 | 1 | 算力类型，枚举值： NPU(0) GPU(1) DCU(2) 。 0：NPU。 1：GPU。 2：DCU。 |
| gpuDriver | Strin g | Query | 否 | "" | AI计算工具包。 |
| pageIndex | Integ er | Query | 否 | 1 | 镜像版本列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

|  | CONVERTING(0) |
|---|---|
| NORMAL(1) |  |
| FAILED(2) |  |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - componentList | List | ["PyTorch:2.7","***: 12.8.1","Python:3.1 2.7","BaseOS:Ubun tu 24.04"] | 组件信息列表。 |
| -accSupport | Boolean | 1 | 是否支持加速。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -gmtCreated | String | 2025-12- 18T04:09:14Z | 创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-12- 18T04:09:14Z | 修改时间，格式为UTC时间。 |
| -hasKea | Boolean | false | 是否包含KEA组件。 |
| - imageAccelera tionType | Integer | 0 | 镜像加速类型，枚举值： IMAGE(0) ACCELERATED IMAGE(1) 。 _ |
| -imageAddress | String | cr-ee.registry.cn- neimeng-236e- d01.env236.cloud. arm.com/bmcp- private/sglang:0.4. 7.post1- pytorch2.7-cu128- 20250617 | 镜像地址。 |
| -imageDigest | String | sha256:a3b1c2**** d4e5f6 | 镜像sha256摘要值。 |

|  | IMAGE(0) |
|---|---|
| ACCELERATED IMAGE(1) _ |  |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -imageId | String | img-public- 437f****48f3 | 镜像id。 |
| - imageNamesp ace | String | bmcp-private | ACR镜像空间。 |
| -imageRepo | String | sglang | 镜像仓库。 |
| - imageRepoTag | String | 0.4.7.post1- pytorch2.7-cu128- 20250617 | 镜像仓库tag。 |
| -imageSize | String | 31675383808 | 镜像大小，单位为字节。 |
| -imageSource | Integer | 0 | 镜像来源，0表示ACR，1表示镜像导入，2表示在线构建。 |
| -imageStatus | Integer | 1 | 镜像版本状态，枚举值： CONVERTING(0) NORMAL(1) FAILED(2) UNKNOWN(3) WAITING(4) EXPORTING(5) EXPORT FAILED(6) _ BUILDING(7) 。 |
| -imageVersion | String | 0.4.7.post1- pytorch2.7-cu128- 20250617 | 镜像版本。 |
| - imageVersionI d | String | imgv- f208****04d67 | 镜像版本id。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域id。 |
| - relatedCompo nent | Integer | 0 | 关联套件数量。 |
| - relatedPipeLin eComponent | Integer | 0 | 关联自定义组件数量。 |
| -relatedTask | Integer | 0 | 关联任务数量。 |
| -gpuDriver | Struct | [{"tagCode":"*** 12.4","tagName":"* ** 12.4"}] | GPU驱动。 |
| --tagCode | String | NVIDIA 550.127.08 | GPU硬件驱动程序的代码。 |

|  | CONVERTING(0) |
|---|---|
| FAILED(2) |  |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --tagName | String | NVIDIA 550.127.08 | GPU硬件驱动程序的名称。 |
| - gpuHardwareD river | Struct | [{"tagCode":"NVIDI A 550.127.08","tagN ame":"NVIDIA 550.127.08"}] | GPU驱动程序版本，用于支持计算、图形渲染和硬件加速功能。 |
| --tagCode | String | NVIDIA 550.127.08 | GPU硬件驱动程序的代码。 |
| --tagName | String | NVIDIA 550.127.08 | GPU硬件驱动程序的名称。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 镜像版本的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 镜像版本的页码。 |

**示例**

请求示例

```
&imageId=img-91fa01150ee51045190baa305e****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "imageVersion":"0.4.7.post1-pytorch2.7-cu128-20250617",
   "gmtModified":"2025-12-18T04:09:14Z",
   "imageId":"img-public-437f****48f3",
   "accSupport":false,
   "imageNamespace":"bmcp-private",
   "aliyunUid":"19822605****1225",
   "gmtCreated":"2025-12-18T04:09:14Z",
   "relatedPipeLineComponent":0,
   "relatedTask":0,
   "gpuDriver":[
    {
     "tagCode":"*** 12.4",
     "tagName":"*** 12.4"
    }
```

`],`

```json
   "componentList":"[\"PyTorch:2.7\",\"***:12.8.1\",\"Python:3.12.7\",\"BaseOS:Ubuntu 2
4.04\"]",
   "hasKea":false,
   "imageRepo":"sglang",
   "imageRepoTag":"0.4.7.post1-pytorch2.7-cu128-20250617",
   "imageStatus":1,
   "imageDigest":"sha256:a3b1c2****d4e5f6",
   "imageSource":0,
   "gpuHardwareDriver":[
    {
     "tagCode":"NVIDIA 550.127.08",
     "tagName":"NVIDIA 550.127.08"
    }
```

`],`

```json
   "regionId":"cn-neimeng-236e-d01",
   "relatedComponent":0,
   "imageAddress":"cr-ee.registry.cn-neimeng-236e-d01.env236.cloud.arm.com/bmcp-private
/sglang:0.4.7.post1-pytorch2.7-cu128-20250617",
   "imageVersionId":"imgv-f208****04d67",
   "imageSize":"31675383808",
   "imageAccelerationType":0
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

`XML` 格式智能体工厂 OpenTrek

```xml
<data>
 <imageVersion>0.4.7.post1-pytorch2.7-cu128-20250617</imageVersion>
 <gmtModified>2025-12-18T04:09:14Z</gmtModified>
 <imageId>img-public-437f****48f3</imageId>
 <accSupport>false</accSupport>
 <imageNamespace>bmcp-private</imageNamespace>
 <aliyunUid>19822605****1225</aliyunUid>
 <gmtCreated>2025-12-18T04:09:14Z</gmtCreated>
 <relatedPipeLineComponent>0</relatedPipeLineComponent>
 <relatedTask>0</relatedTask>
 <gpuDriver>
  <tagCode>*** 12.4</tagCode>
  <tagName>*** 12.4</tagName>
 </gpuDriver>
 <componentList>
[&quot;PyTorch:2.7&quot;,&quot;***:12.8.1&quot;,&quot;Python:3.12.7&quot;,&quot;BaseOS:Ub tu 24.04&quot;]</componentList>
 <hasKea>false</hasKea>
 <imageRepo>sglang</imageRepo>
 <imageRepoTag>0.4.7.post1-pytorch2.7-cu128-20250617</imageRepoTag>
 <imageStatus>1</imageStatus>
 <imageDigest>sha256:a3b1c2****d4e5f6</imageDigest>
 <imageSource>0</imageSource>
 <gpuHardwareDriver>
  <tagCode>NVIDIA 550.127.08</tagCode>
  <tagName>NVIDIA 550.127.08</tagName>
 </gpuHardwareDriver>
 <regionId>cn-neimeng-236e-d01</regionId>
 <relatedComponent>0</relatedComponent>
 <imageAddress>cr-ee.registry.cn-neimeng-236e-d01.env236.cloud.arm.com/bmcp-private/sgl
ang:0.4.7.post1-pytorch2.7-cu128-20250617</imageAddress>
 <imageVersionId>imgv-f208****04d67</imageVersionId>
 <imageSize>31675383808</imageSize>
 <imageAccelerationType>0</imageAccelerationType>
</data> <pageIndex>1</pageIndex> <success>true</success> <dynamicMessages>[]</dynamicMessages> <errorMessage>&quot;&quot;</errorMessage> <errorCode>500</errorCode> <pageSize>10</pageSize> <httpCode>200</httpCode> <totalCount>100</totalCount>
```

#### GetImageVersionDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Query | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - frameWorkTag List | List | ["Spring", "React", "Django"] | 镜像的框架列表。 |
| -imageUsage | List | ["training"] | 镜像用途。 |
| - imageUsageLa bel | List | ["KEA"] | 镜像用途标签。 |
| -useCaseList | List | [] | 镜像使用标签。 |
| -archs | Array | ["ARM64"] | 镜像架构。 |
| --tagCode | String | 标签code | 标签。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --tagName | String | 测试标签 | 标签名称。 |
| - gpuManufactu rerList | Array | ["NVI***", "HY***"] | 芯片厂商。 |
| --tagCode | String | 标签code | 标签。 |
| --tagName | String | 测试标签 | 标签名称。 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |
| - availableServi ce | Integer | 3 | 可用服务，取值范围： 1：任务建模。 2：notebook建模。 3：任务建模和notebook建模。 4：在线服务。 该参数为位运算，可以支持单选，多选。 例如多选任务建模和notebook建模时，该值为3。 |
| -frameWork | Integer | 1 | 框架类型，取值范围： 1：Tensorflow。 2：PyTorch。 |
| -gmtCreated | String | 1606791494471 | 资源创建时间。 |
| -gmtModified | String | 1703575553000 | 修改时间。 |
| -imageDesc | String | image-desc | 镜像描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |
| -imageId | String | image- 05cefd0be2exxxx | 镜像ID。 |
| -imageName | String | py36 cpu tf1.12 u _ _ _ buntu | 镜像名称。 |
| - imageVersion Count | Integer | 5 | 表示当前镜像版本的数量，即该镜像已发布的不同版本总数。 |
| -regionId | String | cn-hangzhou | 地域ID。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&imageId=img-91fa01150ee51045190baa305e****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "frameWork":1,
  "gmtModified":"1703575553000",
  "imageId":"image-05cefd0be2exxxx",
  "imageName":"py36_cpu_tf1.12_ubuntu",
  "aliyunUid":"127756******1314",
  "gmtCreated":"1606791494471",
  "archs":[
   {
    "tagCode":"标签code",
```

`"tagName":"`测试标签"

```
   }
```

`],`

```json
  "imageVersionCount":5,
  "useCaseList":"[]",
  "imageDesc":"image-desc",
  "imageUsage":"[\"training\"]",
  "regionId":"cn-hangzhou",
  "availableService":3,
  "frameWorkTagList":"[\"Spring\", \"React\", \"Django\"]",
  "gpuManufacturerList":[
   {
    "tagCode":"标签code",
```

`"tagName":"`测试标签"

```
   }
```

`],`

```json
  "imageUsageLabel":"[\"KEA\"]"
 },
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateCustomImage

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Body | 否 | img- 7e4d89510d0bb04bf00b eb70**** | 镜像ID，可不填。 |
| imageNa me | Strin g | Body | 是 | image-name | 镜像名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| imageDes c | Strin g | Body | 否 | image-desc | 镜像描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| imageNa mespace | Strin g | Body | 是 | test | ACR镜像命名空间，该参数必填。 |
| imageRep o | Strin g | Body | 是 | test | 镜像仓库，该参数必填。 |
| imageRep oTag | Strin g | Body | 是 | v1 | 镜像仓库Tag，该参数必填。 |
| imageAdd ress | Strin g | Body | 是 | cr- ee.registry.${region}.& {domain}/****/**** | 镜像地址，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| availableS ervice | Integ er | Body | 是 | 3 | 可应用的服务类型，该参数必填，取值范围： 1：任务建模。 2：notebook建模。 3：任务建模和 notebook建模。 4：在线服务。 5：任务建模和在线服务。 6：notebook建模和在线服务。 7：任务建模、 notebook建模和在线服务。 该参数为位运算，可以支持单选，多选。 例如多选任务建模和notebook建模时， 该值为3。 |
| frameWor k | Integ er | Body | 是 | 1 | 镜像框架，该参数必填，取值范围： 1：Tensorflow。 2：PyTorch。 |
| clusterTyp e | Integ er | Body | 否 | 0 | 集群算力类型，取值范围： 0：裸金属。 1：EGS。 2：不限。 |
| gpuDriver | Strin g | Body | 否 | [{ "type": "CU***", "version": "v1" }] | AI计算工具包。 |
| gpuManuf acturerLis t | Json | Body | 否 | ["NVI***", "HY***"] | 芯片厂商。 |
| useCaseLi st | Json | Body | 否 | ["1000", "2000"] | 镜像的适用场景。 0000 - 不限 1000 - 训练镜像 2000 - 推理镜像 2001 - A-Speed推理镜像 9000 - 其他该字段目前未启用。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageSize | Strin g | Body | 否 | 1000 | 镜像大小。 |
| componen tList | Json | Body | 否 | [{ "name": "***", "version": "***" }, { "name": "***", "version": "***" }] | 组件信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"imageId": "img- ****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误信息。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "imageName":"image-name", "imageVersion":"v1", "imageNamespace":"test", "imageRepo":"test", "imageRepoTag":"v1", "imageAddress":"cr-ee.registry.${region}.&{domain}/****/****", "availableService":"3", "frameWork":"1" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{\"imageId\": \"img-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteImageVersion

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Query | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |
| imageVer sion | Strin g | Query | 是 | v1 | 镜像版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
&imageId=img-91fa01150ee51045190baa305e**** &imageVersion=v1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteCustomImage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Query | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&imageId=img-91fa01150ee51045190baa305e****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateCustomImage

调用UpdateCustomImage修改指定镜像库的部分信息，包括镜像名称、描述和镜像版本。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Body | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 否 | v1 | 镜像版本。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageNa me | Strin g | Body | 否 | image-name | 镜像名称，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号 （.）、下划线（ ）和短划 _ 线（-）。 |
| imageDes c | Strin g | Body | 否 | image-desc | 镜像描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| targetVers ion | Strin g | Body | 否 | v1 | 目标版本。 |
| useCaseLi st | Json | Body | 否 | ["1000", "2000"] | 镜像的适用场景。 0000 - 不限 1000 - 训练镜像 2000 - 推理镜像 2001 - A-Speed推理镜像 9000 - 其他该字段目前未启用。 |
| imageVer sionId | Strin g | Body | 否 | imgv- 024ffe77087eb04eac09 6aa0**** | 镜像版本ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
{ "imageId":"img-91fa01150ee51045190baa305e****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ConvertAcceleratedImage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageId | Strin g | Body | 是 | img- 91fa01150ee51045190b aa305e**** | 镜像ID，该参数必填。 |
| imageVer sion | Strin g | Body | 是 | v1 | 镜像版本，该参数必填。 |
| imageVer sionId | Strin g | Body | 否 | imgv- 024ffe77087eb04eac09 6aa0**** | 镜像版本ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "imageId":"img-91fa01150ee51045190baa305e****", "imageVersion":"v1" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListImages

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageTyp e | Integ er | Query | 否 | 1 | 镜像类型，取值范围： 0：公共镜像。 1：自定义镜像。 默认值：1。 |
| imageAcc elerationT ype | Integ er | Query | 否 | 0 | 镜像加速类型，取值范围： 0：容器镜像。 1：加速镜像。 默认值：0。 |
| imageStat us | Integ er | Query | 否 | 1 | 镜像状态，取值范围： 0：转换中。 1：正常。 2：转换失败。 3：未知状态。 4：等待中。 |
| imageVer sionId | Strin g | Query | 否 | imgv-f208****04d67 | 镜像版本id，从SP01升级到 v3.18.6及以上版本时为兼容性保留的字段。 |
| imageId | Strin g | Query | 否 | img-public-437f****48f3 | 镜像id。 |
| imageNa me | Strin g | Query | 否 | sglang-nvidia | 镜像名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| frameWor k | Integ er | Query | 否 | 2 | 算法框架，枚举值： CUSTOM(0) TENSOR FLOW(1) _ PY TORCH(2) _ ELASTIC BATCH(3) _ XG BOOST(4) _ ONE FLOW(5) _ MPI JOB(6) _ DEEPSPEED(10) MEGATRON(11) PADDLE PADDLE(12) _ MIND SPORE(13) _ VLLM(14) OPEN TREK LLM(15) _ _ SG LANG(16) _ OLLAMA(17) 。 1：Tensorflow。 2：PyTorch。 |
| hashrateT ype | Integ er | Query | 否 | 1 | 算力类型，枚举值： NPU(0) GPU(1) DCU(2) 。 |
| clusterTyp e | Integ er | Query | 否 | 1 | 资源类型。 |
| gpuType | Strin g | Query | 否 | NVIDIA Ampere ***** _ _ | GPU类型。 |
| gpuDriver | Strin g | Query | 否 | "" | AI计算工具包。 |
| gpuManuf acturer | Strin g | Query | 否 | /NVIDIA | GPU厂商。 |
| useCase | Strin g | Query | 否 | 2000 | 镜像的适用场景，取值范围： 0000：不限 1000：训练镜像 2000：推理镜像 2001：A-Speed推理镜像 9000：其他该字段目前未启用。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| availableS ervice | Integ er | Query | 否 | 0 | 可用服务。 1：任务建模。 2：notebook建模。 3：任务建模和 notebook建模。 4：在线服务。 5：任务建模和在线服务。 6：notebook建模和在线服务。 7：任务建模、 notebook建模和在线服务。 该参数为位运算，可以支持单选，多选。 例如多选任务建模和notebook建模时， 该值为3。 |
| showAVer sion | Boole an | Query | 否 | false | 是否展示一个版本ID，取值范围： true：是。 false：否。 |
| pageIndex | Integ er | Query | 否 | 1 | 镜像列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - frameWorkTag List | List | [{"tagCode":"PT 2 _ _ 7","tagName":"PyT orch 2.7"}] | 算法框架标签列表，元素包含tagCode（标签编码）和tagName（标签名称）。 |
| -imageUsage | List | ["inference"] | 应用场景列表，可选值为training、 inference。 |
| - imageUsageLa bel | List | [“KEA”] | 功能标签列表，可选值为A-Speed、KEA等。 |
| -useCaseList | List | [{"tagCode":"infer ence","tagName":"I NFERENCE"}] | 使用场景标签列表，元素包含tagCode（标签编码）和tagName（标签名称），tagCode枚举值： no limit train inference _ quant unclassified 。 |
| -archs | Array | [{"tagCode":"AMD 64","tagName":"A MD64"}] | CPU架构标签列表，元素包含tagCode（标签编码）和tagName（标签名称）。 |
| --tagCode | String | “AMD64” | 分类或者标签的Code。 |
| --tagName | String | “AMD64” | 分类或者标签的名称。 |
| - gpuManufactu rerList | Array | [{"tagCode":"NVIDI A","tagName":"NVI DIA"}] | 芯片厂商标签列表，元素包含tagCode（标签编码）和tagName（标签名称），tagCode枚举值： HUAWEI Ascend HYGON _ NVIDIA APG KUN LUN XIN _ _ OTHER 。 |
| --tagCode | String | “NVIDIA” | 显卡的代码。 |
| --tagName | String | “NVIDIA” | 显卡的名称。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| - availableServi ce | Integer | 0 | 可用服务。 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -frameWork | Integer | 2 | 算法框架，枚举值： CUSTOM(0) TENSOR FLOW(1) PY TORCH(2) _ _ ELASTIC BATCH(3) XG BOOST(4) _ _ ONE FLOW(5) MPI JOB(6) _ _ DEEPSPEED(10) MEGATRON(11) PADDLE PADDLE(12) _ MIND SPORE(13) VLLM(14) _ OPEN TREK LLM(15) SG LANG(16) _ _ _ OLLAMA(17) 。 |
| -gmtCreated | String | 2025-12- 18T04:09:14Z | 创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-12- 18T04:09:14Z | 修改时间，格式为UTC时间。 |
| - hasAccVersion | Boolean | false | 是否存在加速版本。 |
| -imageDesc | String | image-desc | 镜像描述。 |
| -imageId | String | img-public- 437f****48f3 | 镜像id。 |
| -imageName | String | sglang-nvidia | 镜像名称。 |
| - imageVersion Count | Integer | 1 | 镜像版本数。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域id。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| PADDLE PADDLE(12) _ |  |
|---|---|
| MIND SPORE(13) _ |  |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 镜像的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 镜像的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "frameWork":2,
   "gmtModified":"2025-12-18T04:09:14Z",
   "imageId":"img-public-437f****48f3",
   "imageName":"sglang-nvidia",
   "aliyunUid":"19822605****1225",
   "gmtCreated":"2025-12-18T04:09:14Z",
   "archs":[
    {
     "tagCode":"“AMD64”",
     "tagName":"“AMD64”"
    }
```

`],`

```json
   "imageVersionCount":1,
   "useCaseList":"[{\"tagCode\":\"inference\",\"tagName\":\"INFERENCE\"}]",
   "imageDesc":"image-desc",
   "hasAccVersion":false,
   "imageUsage":"[\"inference\"]",
   "regionId":"cn-neimeng-236e-d01",
   "availableService":0,
   "frameWorkTagList":"[{\"tagCode\":\"PT_2_7\",\"tagName\":\"PyTorch 2.7\"}]",
   "gpuManufacturerList":[
    {
     "tagCode":"“NVIDIA”",
     "tagName":"“NVIDIA”"
    }
```

`],`

```json
   "imageUsageLabel":"[“KEA”]"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

### 代码集

#### CreateCodeRepo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| codeRepo Name | Strin g | Body | 是 | codeRepo-name | 代码集名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | codeRepo-desc | 代码集描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |
| codeRepo Path | Strin g | Body | 是 | oss://****/**** | 代码集路径，该参数必填。 |
| codeRepo Size | Strin g | Body | 否 | 1000 | 代码集大小。 |
| codeRepo Source | Strin g | Body | 否 | 1 | 代码集来源，取值范围： 1：云存储。 2：Github。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {"codeRepoId": "cd-****"} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "codeRepoName":"codeRepo-name", "codeRepoPath":"oss://****/****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\"codeRepoId\": \"cd-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteCodeRepo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| codeRepoI d | Strin g | Query | 是 | cd- 96a5060c0a9570404f09 a8f0747**** | 代码集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&codeRepoId=cd-96a5060c0a9570404f09a8f0747****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetCodeRepoDetail

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| codeRepoI d | Strin g | Query | 是 | cd- 96a5060c0a9570404f09 a8f0747**** | 代码集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -useCaseList | Array | [ { "tagCode": "no limit", _ "tagName": "NO LIMIT" } ] | 使用场景列表。 |
| --tagCode | String | no limit _ | 标签编码，与标签名称一一对应： no limit：不限 _ train：训练 inference：推理 quant：量化 unclassified：未分类 |
| --tagName | String | NO LIMIT | 标签名称，与标签编码一一对应： NO LIMIT：未分类 _ TRAINING：训练 INFERENCE：推理 QUANTIZATION：量化 OTHERS：未分类 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -codeRepoId | String | cd- 2cecf058******44e 1 | 代码集ID。 |
| - codeRepoNam e | String | exampleName | 代码集名称。 |
| - codeRepoPath | String | oss://****/**** | 代码集路径。 |
| -codeRepoSize | String | 1000 | 代码集大小。 |
| - codeRepoType | Integer | 1 | 代码集类型 0：公共代码集 1：自定义代码集 |
| -description | String | 示例描述。 | 代码集描述。 |
| -gmtCreated | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -gmtModified | String | 2026-02- 27T01:53:30Z | 修改时间。 |
| -regionId | String | cn-hangzhou | 地域ID。 |

**示例**

请求示例

```
&codeRepoId=cd-96a5060c0a9570404f09a8f0747****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "useCaseList":[
   {
    "tagCode":"",
    "tagName":""
   }
```

`],`

```json
  "gmtModified":"",
  "codeRepoSize":"",
  "aliyunUid":"",
  "codeRepoId":"",
  "gmtCreated":"",
  "regionId":"",
  "codeRepoPath":"",
  "codeRepoName":"",
  "description":"",
  "codeRepoType":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListCodeRepo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| codeRepoI d | Strin g | Query | 否 | cd- 96a5060c0a9570404f09 a8f0747**** | 代码集ID。 |
| codeRepo Name | Strin g | Query | 否 | codeRepo-name | 代码集名称。 |
| pageIndex | Integ er | Query | 否 | 1 | 代码集列表的页码。 默认值：1。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -useCaseList | Array | [ { "tagCode": "no limit", _ "tagName": "NO LIMIT" } ] | 使用场景列表。 |
| --tagCode | String | no limit _ | 标签编码，与标签名称一一对应： no limit：不限 _ train：训练 inference：推理 quant：量化 unclassified：未分类 |
| --tagName | String | NO LIMIT | 标签名称，与标签编码一一对应： NO LIMIT：未分类 _ TRAINING：训练 INFERENCE：推理 QUANTIZATION：量化 OTHERS：未分类 |
| -aliyunUid | String | 127756******1314 | 实例所属的阿里云账户ID。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -codeRepoId | String | cd- 2cecf058******44e 1 | 代码集ID。 |
| - codeRepoNam e | String | exampleName | 代码集名称。 |
| - codeRepoPath | String | oss://****/**** | 代码集路径。 |
| -codeRepoSize | String | 1000 | 代码集大小。 |
| - codeRepoType | Integer | 1 | 代码集类型 0：公共代码集 1：自定义代码集 |
| -description | String | 示例描述 | 代码集描述。 |
| -gmtCreated | String | 2026-02- 27T01:53:30Z | 创建时间. |
| -gmtModified | String | 2026-02- 27T01:53:30Z | 修改时间。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - relatedCompo nent | Integer | 1 | 关联套件数目。 |
| - relatedPipeline Component | Integer | 2 | 关联可视化建模组件数目。 |
| -relatedTask | Integer | 5 | 关联任务数目。 |
| -shared | Integer | 1 | 共享范围： 0：本资源集 1：本组织及下级组织 2：本组织 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 代码集的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 代码集的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "shared":"",
   "gmtModified":"",
   "codeRepoSize":"",
   "aliyunUid":"",
   "gmtCreated":"",
   "codeRepoPath":"",
   "relatedTask":"",
   "codeRepoName":"",
   "relatedPipelineComponent":"",
   "description":"",
   "useCaseList":[
    {
     "tagCode":"",
     "tagName":""
    }
```

`],`

```json
   "codeRepoId":"",
   "regionId":"",
   "relatedComponent":"",
   "codeRepoType":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### UpdateCodeRepo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| codeRepoI d | Strin g | Body | 是 | cd- 96a5060c0a9570404f09 a8f074**** | 代码集ID，该参数必填。 |
| codeRepo Name | Strin g | Body | 是 | codeRepo-name | 代码集名称，该参数必填， 长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（ ）和短划线（-）。 _ |
| descriptio n | Strin g | Body | 否 | codeRepo-desc | 代码集描述，描述长度为 2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "codeRepoId":"cd-96a5060c0a9570404f09a8f074****", "codeRepoName":"codeRepo-name" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 数据加速器

#### UpdateDataAccInstance

调用UpdateDataAccInstance修改指定数据加速器的部分信息，包括数据加速器名称和描述。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/updateDataAcc/[instanceId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- f26ee62248a34dd796dc b602b2**** | 实例ID。 |
| name | Strin g | Body | 是 | dataacc-name | 数据加速器名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线 _ （-）。 |
| descriptio n | Strin g | Body | 否 | dataacc-description | 数据加速器描述，描述长度为2~256个字符，不能以 http://和https:// 开头。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataacc/updateDataAcc/[instanceId] HTTP/1.1 { "instanceId":"da-f26ee62248a34dd796dcb602b2****", "name":"dataacc-name" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteDataAccInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /dataacc/deleteDataAcc/[instanceId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 41252a571fd9431f884a ce51fb**** | 数据加速器实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /dataacc/deleteDataAcc/[instanceId] HTTP/1.1 &instanceId=da-41252a571fd9431f884ace51fb****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### BindDataAccInstance

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/bindDataAccInstance/[instanceId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 41252a571fd9431f884a ce51fbb***** | 数据加速器实例ID。 |
| sourceId | Strin g | Body | 是 | ds- 0e54d82ee7794547a27 363988***** | 资源ID，该参数必填，绑定数据集ID或模型ID。 |
| sourceVer sion | Strin g | Body | 否 | v1 | 关联资源对象版本，关联对象是模型时，该参数不能为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /dataacc/bindDataAccInstance/[instanceId] HTTP/1.1 { "instanceId":"da-41252a571fd9431f884ace51fbb*****", "sourceId":"ds-0e54d82ee7794547a27363988*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListDataAccInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataacc/listDataAcc HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Query | 否 | da- 41252a571fd9431f884a ce51fbb***** | 数据加速器实例ID。 |
| sourceId | Strin g | Query | 否 | ds- f6e31f22336d43bb9498 2391dfa5**** | 资源ID，该资源为数据集ID 或模型ID。 |
| pageIndex | Integ er | Query | 否 | 1 | 数据加速器列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliYunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - cacheCapacity | String | 1.00GiB | 总缓存大小。 |
| -cached | String | 512.00KiB | 已使用缓存容量。 |
| -gmtCreated | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -gmtModified | String | 2026-02- 27T01:53:30Z | 修改时间。 |
| -id | Integer | 1 | 自增ID。 |
| -instanceId | String | da- 14cd8ff5******495 9 | 实例ID。 |
| - instanceName | String | exampleName | 实例名称。 |
| -isDeleted | Integer | 0 | 逻辑删除： 0：未删除 1：已删除 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -memCount | Integer | 1 | 内存大小（GB）。 |
| -quotaId | String | rq- 081ca4dc******486 d | 配额ID。 |
| -quotaName | String | quotaName | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -replica | Integer | 1 | 副本数。 |
| -resourceId | String | da- 14cd8ff5******495 9 | 该资源的ID。 |
| - resourceQuota Id | String | rq- 081ca4dc******486 d | 该资源绑定的资源配额ID。 |
| - resourceRegio nId | String | cn-hangzhou | 该资源所属地域ID。 |
| -sourceId | String | ds- 07551d6f******460 6 | 绑定数据ID。 |
| -sourceName | String | sourceName | 绑定数据名称。 |
| -sourceVersion | String | v1 | 绑定数据版本。 |
| -status | Integer | 2 | 实例状态： 0：启动中 1：运行中 2：停止 |
| totalCount | Integer | 100 | 数据加速器的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 数据加速器的页码。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /dataacc/listDataAcc HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "memCount":"",
   "sourceId":"",
   "aliYunUid":"",
   "gmtModified":"",
   "resourceId":"",
   "quotaName":"",
   "replica":"",
   "gmtCreated":"",
   "instanceName":"",
   "sourceVersion":"",
   "resourceRegionId":"",
   "quotaId":"",
   "cacheCapacity":"",
   "instanceId":"",
   "isDeleted":"",
   "regionId":"",
   "cached":"",
   "resourceQuotaId":"",
   "id":"",
   "sourceName":"",
   "status":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "pageSize":10,
 "errorCode":"500",
 "totalCount":100,
 "httpCode":200
}
```

#### UpdateDataAccInstanceStatus

调用UpdateDataAccInstanceStatus修改指定数据加速器的状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/updateDataAccStatus/[instanceId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 4cf366a718774856ba05 74da5d7**** | 数据加速器实例ID。 |
| status | Boole an | Body | 是 | true | 加速器状态，该参数必填， 取值范围： true：启动。 false：停止。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataacc/updateDataAccStatus/[instanceId] HTTP/1.1 { "instanceId":"da-4cf366a718774856ba0574da5d7****", "status":"true" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateDataAccInstanceSpec

调用UpdateDataAccInstanceSpec修改指定数据加速器规格的部分信息，包括内存大小和副本个数。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/updateDataAccSpec/[instanceId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 41252a571fd9431f884a ce51**** | 数据加速器实例ID。 |
| memCoun t | Integ er | Body | 是 | 2 | 内存大小，单位为GB，该参数必填。 当数据加速器实例在运行状态时，不允许修改 memCount。 |
| replica | Integ er | Body | 是 | 1 | 副本个数，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataacc/updateDataAccSpec/[instanceId] HTTP/1.1 { "instanceId":"da-41252a571fd9431f884ace51****", "memCount":"2", "replica":"1" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetDataAccInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /dataacc/getDataAccStatus/[instanceId] HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 41252a571fd9431f884a ce51fbb***** | 数据加速器实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -taskList | Array | [ { "gmtCreated": "2026-02- 26T13:00:41.000+ 00:00", "name": "nameExample", "id": "nb- e8a4720f******41f b", "status": 0 } ] | 关联任务列表。 |
| --gmtCreated | String | 2026-02- 26T13:00:41.000+ 00:00 | 创建时间。 |
| --id | String | nb- e8a4720f******41f b | 训推任务实例ID。 |
| --name | String | nameExample | 实例名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --status | Integer | 0 | Notebook状态。枚举值： 0 -启动中 (starting)， 1 -运行中(running)， 2 -已停止(stopped)， 3 -失败(failed)， 4 -等待启动(waiting for starting)， 5 -变配中 (scaling)， 6 -停止中(stopping)。 |
| -aliYunUid | String | 157123456789**** | 实例所属的阿里云账户ID。 |
| - cacheCapacity | String | 1.00GiB | 总缓存大小。 |
| -cached | String | 512.00KiB | 已使用缓存容量。 |
| -gmtCreated | String | 2026-02- 27T01:53:30Z | 创建时间。 |
| -instanceId | String | 2026-02- 27T01:53:30Z | 实例ID。 |
| - instanceName | String | exampleName | 实例名称。 |
| -memCount | Integer | 1 | 内存大小（GB）。 |
| -quotaId | String | rq- 081ca4dc******486 d | 配额ID。 |
| -quotaName | String | quotaName | 配额名称。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| -replica | Integer | 2 | 副本数。 |
| -sourceId | String | ds- 07551d6f******460 6 | 绑定数据ID。 |
| -sourceVersion | String | v1 | 绑定数据版本。 |
| -status | Integer | 2 | 实例状态： 0：启动中 1：运行中 2：停止 |

**示例**

智能体工厂 OpenTrek 请求示例

```
GET /dataacc/getDataAccStatus/[instanceId] HTTP/1.1 &instanceId=da-41252a571fd9431f884ace51fbb*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "memCount":"",
  "sourceId":"",
  "taskList":[
   {
    "gmtCreated":"",
    "name":"",
    "id":"",
    "status":""
   }
```

`],`

```json
  "aliYunUid":"",
  "quotaName":"",
  "replica":"",
  "gmtCreated":"",
  "instanceName":"",
  "sourceVersion":"",
  "quotaId":"",
  "cacheCapacity":"",
  "instanceId":"",
  "regionId":"",
  "cached":"",
  "status":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateDataAccInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/createDataAcc HTTP/1.1
```

智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | Strin g | Body | 是 | dataacc-name | 数据加速器名称，该参数必填，长度为2～64个字符， 必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（ ）和短划线（-)。 _ |
| descriptio n | Strin g | Body | 否 | dataacc-desc | 数据加速器描述，描述长度为2~256个字符，不能以 http://和https://开头。 |
| quotaId | Strin g | Body | 是 | rq- 6812fbe20dff7048fd0a1f b0127***** | 资源配额ID，该参数必填。 |
| memCoun t | Integ er | Body | 是 | 1 | 内存大小，单位为GB，该参数必填。 |
| replica | Integ er | Body | 是 | 1 | 副本个数，该参数必填。 |
| sourceId | Strin g | Body | 是 | ds- 55505e6bc47f4a86a455 014e***** | 关联资源对象ID，该参数必填。 |
| sourceVer sion | Strin g | Body | 否 | v1 | 关联资源对象版本，关联对象是模型时，该参数不能为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "instanceId": "da- ****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataacc/createDataAcc HTTP/1.1 { "name":"dataacc-name", "quotaId":"rq-6812fbe20dff7048fd0a1fb0127*****", "memCount":"1", "replica":"1", "sourceId":"ds-55505e6bc47f4a86a455014e*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\t\"instanceId\": \"da-****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UnbindDataAccInstance

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /dataacc/unbindDataAccInstance/[instanceId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| instanceId | Strin g | Path | 是 | da- 41252a571fd9431f884a ce51fb***** | 数据加速器实例ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /dataacc/unbindDataAccInstance/[instanceId] HTTP/1.1 { "instanceId":"da-41252a571fd9431f884ace51fb*****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 套件

#### GetComponent

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Query | 是 | cp-system-llm- H2****2gpu | 组件唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态消息列表。 |
| success | Boolean | true | 业务是否成功。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | - | 返回数据。 |
| - componentDat asetFormats | List | [dataset] | 组件支持的数据集格式列表。 |
| - componentMet as | List | [Meta] | 组件元数据列表。 |
| - componentPar ams | List | [Params] | 组件参数列表。 |
| - componentApi s | Array | [{}] | 组件对外暴露的API列表。 |
| --id | String | 17 | 数据库主键ID。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --method | String | POST | 请求方法。 |
| --name | String | OpenAI Stream | API名称。 |
| --path | String | /v1/chat/completio ns | 请求路径。 |
| -- requestSchem a | Struct | {[]} | 请求体JSON Schema定义。 |
| ---examples | Array | [] | 任务状态字段的数据类型。 |
| ----model | String | qwen | 示例中使用的模型名称。 |
| ----input | Struct | {} | 请求输入字段定义。 |
| -----img url _ | String | https://example.co m/img.jpg | 示例请求中的图片URL。 |
| ----- negative prom _ pt | String | ugly, deformed | 示例请求中的负向提示词。 |
| -----prompt | String | 一只可爱的猫咪 | 示例请求中的提示词。 |
| ----parameters | Struct | {} | 请求参数字段定义。 |
| -----duration | Integer | 5 | 示例请求中的时长参数。 |
| -----size | String | 1280x720 | 示例请求中的尺寸参数。 |
| ---$schema | String | http://json- schema.org/draft- 05/schema# | JSON Schema版本声明。 |
| ---type | String | string | 任务状态字段的数据类型。 |
| ---properties | Struct | {} | output内部属性定义。 |
| ----input | Struct | {} | 请求输入字段定义。 |
| -----type | String | string | 任务状态字段的数据类型。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----- PropertiesJson | Struct | {} | output内部属性定义。 |
| ------img url _ | Struct | https://example.co m/img.jpg | 示例请求中的图片URL。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| ------ negative prom _ pt | Struct | ugly, deformed | 示例请求中的负向提示词。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| ------prompt | Struct | 一只可爱的猫咪 | 示例请求中的提示词。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| ----model | Struct | qwen | 示例中使用的模型名称。 |
| -----type | String | string | 任务状态字段的数据类型。 |
| ----parameters | Struct | {} | 请求参数字段定义。 |
| -----type | String | string | 任务状态字段的数据类型。 |
| -----properties | Struct | {} | output内部属性定义。 |
| ------duration | Struct | 5 | 示例请求中的时长参数。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| ------size | Struct | 1280x720 | 示例请求中的尺寸参数。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| -- responseSche ma | Struct | {} | 响应体JSON Schema定义。 |
| ---examples | Array | [] | 任务状态字段的数据类型。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----output | Struct | {} | 响应输出字段定义。 |
| -----task id _ | String | task-****abcd**** | 示例响应中的任务ID。 |
| -----task status _ | String | PENDING | 示例响应中的任务状态。 |
| ---$schema | String | http://json- schema.org/draft- 05/schema# | JSON Schema版本声明。 |
| ---type | String | string | 任务状态字段的数据类型。 |
| ---properties | Struct | {} | output内部属性定义。 |
| ----outputJson | Struct | {} | 响应输出字段定义。 |
| -----type | String | string | 任务状态字段的数据类型。 |
| ----- PropertiesJson | Struct | {} | output内部属性定义。 |
| ------task id _ | Struct | task-****abcd**** | 示例响应中的任务ID。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| ------ task status _ | Struct | PENDING | 示例响应中的任务状态。 |
| -------type | String | string | 任务状态字段的数据类型。 |
| - componentRes ourceSpecs | Array | [] | 资源规格定义列表。 |
| --cpu | Integer | 16 | CPU核数。 |
| --gpu | Integer | 2 | GPU卡数。 |
| --gpuType | String | NVIDIA H20 SXM5 _ _ _ 96G | GPU型号。 |
| --instance | Integer | 1 | 实例数量。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --memory | String | 300Gi | 内存大小。 |
| --shmSize | String | 5 | 共享内存大小。 |
| --shmSizeUnit | String | Gi | 共享内存单位。 |
| --vGPU | Boolean | false | 是否为虚拟GPU。 |
| - componentCat egoryId | String | inferenceServer | 组件分类ID。 |
| - componentDe scription | String | 训练套件 | 组件描述信息。 |
| - componentEnt ry | String | python3 -m vllm.entrypoints.op enai.api server -- _ model $COMPONENT INP _ UT MODEL ... _ | 组件启动入口命令。 |
| -componentId | String | cp-system-llm- H2****2gpu | 组件唯一标识ID。 |
| - componentNa me | String | LLM Universal-H20- 2GPU | 组件名称。 |
| - componentSu bType | String | inferenceServer | 组件子类型。 |
| - componentTyp e | String | inference | 组件类型，如 train（训练）、inference（推理）。 |
| -codeRepo | Struct | {} | 组件关联的代码仓库信息。 |
| --aliyunUid | String | admin**** | 所属阿里云用户ID。 |
| --codeRepoId | String | cd-public- ****7196**** | 代码仓库唯一标识ID。 |
| -- codeRepoNam e | String | aistudio-hopper- cu12.8-vllm0.11.2- general-v1.0 | 代码仓库名称。 |
| -- codeRepoPath | String | oss://oss-aipaas- code-repo-****/ | 代码仓库OSS存储路径。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- codeRepoType | Integer | 0 | 代码仓库类型，0表示OSS类型。 |
| --description | String | 用于NVIDIA Hopper 架构GPU上的LLM推理 | 代码仓库描述信息。 |
| --gmtCreated | String | 2026-02- 06T15:53:00 | 创建时间。 |
| --gmtModified | String | 2026-02- 06T15:53:00 | 最后修改时间。 |
| --id | Integer | 17 | 数据库主键ID。 |
| --isDeleted | Boolean | false | 是否已删除。 |
| --regionId | String | cn-****-d01 | 所在地域ID。 |
| - componentCus tomService | Struct | {} | 自定义服务配置。 |
| -- enableFaultTol erant | Boolean | false | 是否开启容错机制。 |
| --servicePort | Integer | 8000 | 服务端口号。 |
| - componentInp uts | Struct | {} | 组件输入定义。 |
| --artifacts | Array | [] | 组件输出artifact列表。 |
| ---code | String | max-context-len | 元数据编码。 |
| ---mountPath | String | $OUTPUT DIR/infer _ ence persistence _ | 输出artifact挂载路径。 |
| ---name | String | OpenAI Stream | API名称。 |
| ---type | String | string | 任务状态字段的数据类型。 |
| - componentLab els | Struct | {} | 组件标签信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --ability | List | [] | 能力标签列表。 |
| -- disaggInfernen ceMode | List | [] | 分离推理模式标签列表。 |
| -- kvCacheOffloa d | List | [] | KV Cache卸载标签列表。 |
| -- modelDomain | List | LLM | 模型领域标签列表。 |
| - componentOut puts | Struct | {} | 组件输出定义。 |
| --artifacts | Array | [] | 组件输出artifact列表。 |
| ---code | String | max-context-len | 元数据编码。 |
| ---mountPath | String | $OUTPUT DIR/infer _ ence persistence _ | 输出artifact挂载路径。 |
| ---name | String | OpenAI Stream | API名称。 |
| ---type | String | string | 任务状态字段的数据类型。 |
| -image | Struct | {} | 组件使用的镜像信息。 |
| --aliyunUid | String | admin**** | 所属阿里云用户ID。 |
| --gmtCreated | String | 2026-02- 06T15:53:00 | 创建时间。 |
| --gmtModified | String | 2026-02- 06T15:53:00 | 最后修改时间。 |
| --id | Integer | 17 | 数据库主键ID。 |
| -- imageAccelera tionType | Integer | 0 | 镜像加速类型。 0：容器镜像。 1：加速镜像。 默认值：0。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- imageAddress | String | cr-ee.registry.cn- ****-d01.***/acr- aipaas/nvidia- hopper-vllm- general:0.11.2-... | 镜像完整地址。 |
| --imageDigest | String | 7e59fb6c****a7baa c8a****e31f1118** ** | 镜像摘要，用于唯一校验镜像内容。 |
| --imageId | String | img-public- ****d875**** | 镜像ID。 |
| -- imageIdAndVe rsion | String | img-public- ****d875**** 0.11.2-***12.8- ubuntu24.04- py3.12-v1.0 | 镜像ID与版本的组合标识。 |
| -- imageNamesp ace | String | acr-aipaas | 镜像所属命名空间。 |
| --imageRepo | String | nvidia-hopper-vllm- general | 镜像仓库名称。 |
| -- imageRepoTag | String | 0.11.2-***12.8- ubuntu24.04- py3.12-v1.0 | 镜像Tag。 |
| --imageSize | String | 10524283571 | 镜像大小，单位字节。 |
| --imageSource | Integer | 0 | 镜像来源，0表示公共镜像。 镜像摘要，用于唯一校验镜像内容。镜像。镜像。 1：本地上传。 2：Dockerfile构建。 |
| --imageStatus | Integer | 1 | 镜像状态，1表示可用。 0：转换中。 1：正常。 2：转换失败。 3：未知状态。 4：等待中。 |
| --imageType | Integer | 0 | 镜像类型。 镜像ID与版本的组合标识。 1：自定义镜像。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- imageVersion | String | 0.11.2-***12.8- ubuntu24.04- py3.12-v1.0 | 镜像版本号。 |
| -- imageVersionI d | String | imgv-****8fcd**** | 镜像版本ID。 |
| --isDeleted | Boolean | false | 是否已删除。 |
| --regionId | String | cn-****-d01 | 所在地域ID。 |
| --versionDesc | String | xxx | 镜像版本描述。 |

**示例**

请求示例

```
&componentId=cp-1c2d7a2f0cd67049eb0aac90****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "componentParams":"[Params]",
  "componentType":"inference",
  "componentApis":[
   {
    "requestSchema":[
     {
      "properties":[
       {
        "input":[
         {
          "properties":[
           {
            "prompt":[
             {
              "type":"string"
             }
```

`],`

```json
            "img_url":[
             {
              "type":"string"
             }
```

`],`

```json
            "negative_prompt":[
```

智能体工厂 OpenTrek

```json
             {
              "type":"string"
             }
```

]

```
           }
```

`],`

```json
          "type":"string"
         }
```

`],`

```json
        "parameters":[
         {
          "properties":[
           {
            "duration":[
             {
              "type":"string"
             }
```

`],`

```json
            "size":[
             {
              "type":"string"
             }
```

]

```
           }
```

`],`

```json
          "type":"string"
         }
```

`],`

```json
        "model":[
         {
          "type":"string"
         }
```

]

```
       }
```

`],`

```json
      "$schema":"http://json-schema.org/draft-05/schema#",
      "examples":[
       {
        "input":[
         {
          "img_url":"https://example.com/img.jpg",
          "negative_prompt":"ugly, deformed",
```

`"prompt":"`一只可爱的猫咪"

```
         }
```

`],`

```json
        "parameters":[
         {
          "duration":5,
          "size":"1280x720"
         }
```

`],`

```json
        "model":"qwen"
       }
```

`],` 智能体工厂 OpenTrek

```json
      "type":"string"
     }
```

`],`

```json
    "path":"/v1/chat/completions",
    "method":"POST",
    "name":"OpenAI Stream",
    "responseSchema":[
     {
      "properties":[
       {
        "output":[
         {
          "properties":[
           {
            "task_status":[
             {
              "type":"string"
             }
```

`],`

```json
            "task_id":[
             {
              "type":"string"
             }
```

]

```
           }
```

`],`

```json
          "type":"string"
         }
```

]

```
       }
```

`],`

```json
      "$schema":"http://json-schema.org/draft-05/schema#",
      "examples":[
       {
        "output":[
         {
          "task_status":"PENDING",
          "task_id":"task-****abcd****"
         }
```

]

```
       }
```

`],`

```json
      "type":"string"
     }
```

`],`

```json
    "id":"17"
   }
```

`],`

```json
  "componentId":"cp-system-llm-H2****2gpu",
  "componentResourceSpecs":[
   {
    "vGPU":false,
    "shmSizeUnit":"Gi",
    "shmSize":"5",
"instance":1
```

智能体工厂 OpenTrek

```json
    "instance":1,
    "memory":"300Gi",
    "cpu":16,
    "gpu":2,
    "gpuType":"NVIDIA_H20_SXM5_96G"
   }
```

`],`

```json
  "componentLabels":{
   "disaggInfernenceMode":"[]",
   "ability":"[]",
   "kvCacheOffload":"[]",
   "modelDomain":"LLM"
  },
  "componentSubType":"inferenceServer",
  "codeRepo":{
   "gmtModified":"2026-02-06T15:53:00",
   "isDeleted":false,
   "aliyunUid":"admin****",
   "codeRepoId":"cd-public-****7196****",
   "gmtCreated":"2026-02-06T15:53:00",
   "regionId":"cn-****-d01",
   "codeRepoPath":"oss://oss-aipaas-code-repo-****/",
   "codeRepoName":"aistudio-hopper-cu12.8-vllm0.11.2-general-v1.0",
```

`"description":"`用于`NVIDIA Hopper`架构`GPU`上的`LLM`推理`",`

```json
   "id":17,
   "codeRepoType":0
  },
  "componentDescription":"训练套件",
  "componentEntry":"python3 -m vllm.entrypoints.openai.api_server --model
$COMPONENT_INPUT_MODEL ...",
  "image":{
   "imageVersion":"0.11.2-***12.8-ubuntu24.04-py3.12-v1.0",
   "gmtModified":"2026-02-06T15:53:00",
   "versionDesc":"xxx",
   "imageId":"img-public-****d875****",
   "imageNamespace":"acr-aipaas",
   "aliyunUid":"admin****",
   "gmtCreated":"2026-02-06T15:53:00",
   "imageRepo":"nvidia-hopper-vllm-general",
   "imageRepoTag":"0.11.2-***12.8-ubuntu24.04-py3.12-v1.0",
   "imageStatus":1,
   "imageDigest":"7e59fb6c****a7baac8a****e31f1118****",
   "imageIdAndVersion":"img-public-****d875****  0.11.2-***12.8-ubuntu24.04-py3.12-v1.0
```

`",`

```json
   "imageSource":0,
   "isDeleted":false,
   "regionId":"cn-****-d01",
   "imageAddress":"cr-ee.registry.cn-****-d01.***/acr-aipaas/nvidia-hopper-vllm-general
:0.11.2-...",
   "imageVersionId":"imgv-****8fcd****",
   "id":17,
   "imageSize":"10524283571",
   "imageAccelerationType":0,
   "imageType":0
},
```

智能体工厂 OpenTrek

```json
  },
  "componentOutputs":{
   "artifacts":[
    {
     "mountPath":"$OUTPUT_DIR/inference_persistence",
     "code":"max-context-len",
     "name":"OpenAI Stream",
     "type":"string"
    }
```

]

```json
  },
  "componentCategoryId":"inferenceServer",
  "componentInputs":{
   "artifacts":[
    {
     "mountPath":"$OUTPUT_DIR/inference_persistence",
     "code":"max-context-len",
     "name":"OpenAI Stream",
     "type":"string"
    }
```

]

```json
  },
  "componentDatasetFormats":"[dataset]",
  "componentMetas":"[Meta]",
  "componentCustomService":{
   "enableFaultTolerant":false,
   "servicePort":8000
  },
  "componentName":"LLM Universal-H20-2GPU"
 },
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyComponent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /component/modify HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Body | 是 | cp- 1c2d7a2f0cd67049eb0a ac90**** | 套件ID，该参数必填。 |
| componen tName | Strin g | Body | 是 | component-name | 套件名称，该参数必填。 |
| componen tDescripti on | Strin g | Body | 是 | component-desc | 套件描述，该参数必填。 |
| image | Json | Body | 是 | { "imageId": "img- public-21a8c4ac3***", "imageVersion": "v1.0" } | 镜像版本信息，该参数必填。 |
| codeRepo | Json | Body | 否 | { "codeRepoId": "cd- public- ae719558c220fb****" } | 代码集信息。 |
| componen tEntry | Strin g | Body | 否 | bash run model.sh _ | 启动命令，当 categoryId=inferencePr efillDecode时该参数为空。 |
| componen tMultiEntr y | Json | Body | 否 | {"proxyEntry":"proxy命令","prefillEntry":"prefill 命令","decodeEntry":"deco de命令"} | 启动命令，当 categoryId!=inferencePr efillDecode时该参数为空。 |
| componen tResource Specs | Json | Body | 是 | [ { "cpu":64, "gpu":16, "gpuType":"PG1 A910E" _ , "instance":1, "memory":"1000Gi", "shmSize":"10", "shmSizeUnit":"Gi" } ] | 资源规格，该参数必填。 |
| componen tParams | Json | Body | 否 | [ { "code":"tensor- parallel-size", "defaultValue":"2", "description":"并行数", "name":"并行数", "type":"INT", "value":"" }, { "code":"max-model- len", "defaultValue":"32768", "description":"最大长度", "name":"最大长度", "type":"INT", "value":"" } ] | 超参。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tInputs | Json | Body | 否 | { "artifacts":[ { "mountPath":"mnt/mode l", "code":"model", "name":"模型", "type":"model" }, { "mountPath":"mnt/code" , "code":"code", "name":"代码", "type":"code" } ] } | 输入，当 categoryId!=trainCusto m时，该参数可以为空。 |
| componen tOutputs | Json | Body | 否 | { "artifacts":[ { "mountPath":"$OUTPUT _ DIR/checkpoint-best", "code":"model", "name":"输出模型", "type":"model" }, { "mountPath":"$OUTPUT _ DIR/checkpoints", "code":"checkpoint", "name":"输出 checkpoint", "type":"checkpoint" }, { "mountPath":"$OUTPUT _ DIR/runs", "code":"logs", "name":"输出日志", "type":"logs" } ] } | 输出，当 categoryId!=trainCusto m时，该参数可以为空。 |
| componen tApis | Strin g | Body | 否 | [ { "path":"/v1/chat/complet ions", "responseSchema":{}, "requestSchema":{}, "method":"POST", "name":"OpenAI", } ] | API配置列表，推理类套件专属字段。 |
| componen tLabels | Json | Body | 否 | {"ability": ["DEEP THINK"], _ "modelDomain": ["llm"]} | 套件标签，记录适用的模型类型（modelDomian）和能力（ability）。 |
| componen tCustomS ervice | Json | Body | 是 | 推理类套件： {"servicePort": 9080} 训练类套件： {"checkpointPath": "$COMPONENT OUTPUT _ HOME", _ "tensorboardPath": "$COMPONENT OUTPUT _ HOME/runs"} _ | 自定义参数，该参数必填。 |
| componen tDatasetF ormats | Json | Body | 否 | [{"code": "llm-dpo", "name": "llm-dpo", "exampleList": [{"name": "llm- dpo.json", "path": "preset/datasets/llm dpo _ .json"}]}] | 数据集示例，训练类套件专属字段。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tMetas | Json | Body | 否 | [ { "name": "最大上下文长度", "code": "max- context-len", "type": "FLOAT", "unit": "K", "defaultValue": 32 } ] | 套件原信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /component/modify HTTP/1.1 { "componentId":"cp-1c2d7a2f0cd67049eb0aac90****", "componentName":"component-name", "componentDescription":"component-desc", "image":"{
        "imageId": "img-public-21a8c4ac3***",
        "imageVersion": "v1.0"
}", "componentResourceSpecs":"[
    {
 "cpu":64,
 "gpu":16,
 "gpuType":"PG1_A910E",
 "instance":1,
 "memory":"1000Gi",
 "shmSize":"10",
 "shmSizeUnit":"Gi"
    }
]", "componentCustomService":"推理类套件：{"servicePort": 9080} 训练类套件：{"checkpointPath": "$COMPONENT_OUTPUT_HOME", "tensorboardPath": "$COMPONENT_OUTPUT_HOME/runs"}" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteComponent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tId | Strin g | Query | 是 | cp- 1c2d7a2f0cd67049eb0a ac90**** | 套件ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&componentId=cp-1c2d7a2f0cd67049eb0aac90****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetComponentMetaInfo

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| typeCode | Strin g | Query | 否 | ability | 元数据类型编码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 返回数据。 |
| -metaInfoList | Array | [MetaInfoDO] | 元数据信息列表，元素为MetaInfoDO对象。 |
| --id | Integer | 1 | ID。 |
| --key | String | KUN LUN _ | 标签键。 |
| --sort | Integer | 1 | 排序字段。 |
| --typeCode | String | ability | 元数据类型编码。 |
| --typeName | String | 组件能力标签 | 元数据类型名称。 |
| --value | String | KUN LUN _ | 标签值。 |
| -typeCode | String | ability | 元数据类型编码。 |
| -typeName | String | 组件能力标签 | 元数据类型名称。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

| A | I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre | k |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":[
  {
   "metaInfoList":[
    {
```

`"typeName":"`组件能力标签`",`

```json
     "id":1,
     "sort":1,
     "value":"KUN_LUN",
     "key":"KUN_LUN",
     "typeCode":"ability"
    }
```

`],` `"typeName":"`组件能力标签`",`

```json
   "typeCode":"ability"
  }
```

`],`

```json
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GenComponentJsonSchema

调用GenComponentJsonSchema创建推理套件的API信息过程中，将Json转为Json Schema。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求语法**

```
POST /component/genJSONSchema HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| json | Strin g | Body | 是 | {"json":"{ \"model\": \"qwen\", \"messages\": [ { \"role\": \"user\", \"content\": \"hellow111\" } ], \"stream\": true, \"presence penalty\": _ 1.03, \"temperature\": 0.5, \"top p\": 0.95, _ \"max tokens\": 200 _ }"} | 需要转化的Json，该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /component/genJSONSchema HTTP/1.1 { "json":"{"json":"{ \"model\": \"qwen\", \"messages\": [ { \"role\": \"user\", \"content\": \"hellow111\" } ], \"stream\": true, \"presence_penalty\": 1.03, \" temperature\": 0.5, \"top_p\": 0.95, \"max_tokens\": 200}"}" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### CreateComponent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /component/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tName | Strin g | Body | 是 | component-name | 套件名称，该参数必填。 |
| componen tCategoryI d | Strin g | Body | 是 | inferenceServer | 套件子类型，该参数必填。 |
| componen tDescripti on | Strin g | Body | 是 | component-desc | 套件描述，该参数必填。 |
| image | Json | Body | 是 | { "imageId": "img- public-21a8c4ac3***", "imageVersion": "v1.0" } | 镜像版本信息，该参数必填。 |
| codeRepo | Json | Body | 否 | { "codeRepoId": "cd- public- ae719558c220fb****" } | 代码集信息。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tEntry | Strin g | Body | 否 | bash run model.sh _ | 启动命令，当 categoryId=inferencePr efillDecode时该参数为空。 |
| componen tMultiEntr y | Json | Body | 否 | {"proxyEntry":"proxy命令","prefillEntry":"prefill 命令","decodeEntry":"deco de命令"} | 启动命令，当 categoryId!=inferencePr efillDecode时该参数为空。 |
| componen tResource Specs | Json | Body | 是 | [ { "cpu":64, "gpu":16, "gpuType":"PG1 A910E" _ , "instance":1, "memory":"1000Gi", "shmSize":"10", "shmSizeUnit":"Gi" } ] | 资源规格，该参数必填。 |
| componen tParams | Json | Body | 否 | [ { "code":"tensor- parallel-size", "defaultValue":"2", "description":"并行数", "name":"并行数", "type":"INT", "value":"" }, { "code":"max-model- len", "defaultValue":"32768", "description":"最大长度", "name":"最大长度", "type":"INT", "value":"" } ] | 超参。 |
| componen tInputs | Json | Body | 否 | { "artifacts":[ { "mountPath":"mnt/mode l", "code":"model", "name":"模型", "type":"model" }, { "mountPath":"mnt/code" , "code":"code", "name":"代码", "type":"code" } ] } | 输入，当 categoryId!=trainCusto m时，该参数可以为空。 |
| componen tOutputs | Json | Body | 否 | { "artifacts":[ { "mountPath":"$OUTPUT _ DIR/checkpoint-best", "code":"model", "name":"输出模型", "type":"model" }, { "mountPath":"$OUTPUT _ DIR/checkpoints", "code":"checkpoint", "name":"输出 checkpoint", "type":"checkpoint" }, { "mountPath":"$OUTPUT _ DIR/runs", "code":"logs", "name":"输出日志", "type":"logs" } ] } | 输出，当 categoryId!=trainCusto m时，该参数可以为空。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tApis | Strin g | Body | 否 | [ { "path":"/v1/chat/complet ions", "responseSchema":{}, "requestSchema":{}, "method":"POST", "name":"OpenAI", } ] | API配置列表，推理类套件专属字段。 |
| componen tLabels | Json | Body | 否 | {"ability": ["DEEP THINK"], _ "modelDomain": ["llm"]} | 套件标签，记录适用的模型类型（modelDomian）和能力（ability）。 |
| componen tCustomS ervice | Json | Body | 是 | 推理类套件： {"servicePort": 9080} 训练类套件： {"checkpointPath": "$COMPONENT OUTPUT _ HOME", _ "tensorboardPath": "$COMPONENT OUTPUT _ HOME/runs"} _ | 自定义参数，该参数必填。 |
| componen tDatasetF ormats | Json | Body | 否 | [{"code": "llm-dpo", "name": "llm-dpo", "exampleList": [{"name": "llm- dpo.json", "path": "preset/datasets/llm dpo _ .json"}]}] | 数据集示例，训练类套件专属字段。 |
| componen tMetas | Json | Body | 否 | [ { "name": "最大上下文长度", "code": "max- context-len", "type": "FLOAT", "unit": "K", "defaultValue": 32 } ] | 套件原信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "cp-****" } | 返回数据。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /component/create HTTP/1.1 { "componentName":"component-name", "componentCategoryId":"inferenceServer", "componentDescription":"component-desc", "image":"{
        "imageId": "img-public-21a8c4ac3***",
        "imageVersion": "v1.0"
}", "componentResourceSpecs":"[
    {
 "cpu":64,
 "gpu":16,
 "gpuType":"PG1_A910E",
 "instance":1,
 "memory":"1000Gi",
 "shmSize":"10",
 "shmSizeUnit":"Gi"
    }
]", "componentCustomService":"推理类套件：{"servicePort": 9080} 训练类套件：{"checkpointPath": "$COMPONENT_OUTPUT_HOME", "tensorboardPath": "$COMPONENT_OUTPUT_HOME/runs"}" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{    \"cp-****\"}",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListComponent

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /component/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| xpu | Strin g | Body | 否 | NVIDIA | 套件绑定的镜像GPU类型。 |
| modelDo main | Strin g | Body | 否 | llm | 套件适用的模型类型。 |
| componen tNameLik e | Strin g | Body | 否 | component-name | 套件名称模糊查询。 |
| componen tSource | Strin g | Body | 否 | custom | 套件来源，custom为用户自定义，admin为系统内置。 |
| componen tType | Strin g | Body | 否 | inference | 套件类型，由 componentCategoryId自动推导，枚举值如下： - inference ：推理 - train ：训练 - quant ：量化。 |
| modelId | Strin g | Body | 否 | md-sd9au8safusd***** | 模型仓库ID。 |
| modelVer sion | Strin g | Body | 否 | v1 | 模型仓库版本号。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| componen tCategoryI d | Strin g | Body | 否 | inferenceServer | 套件类别ID，枚举值如下： - inferenceServer ： 推理服务 - inferencePrefillDecod e ：推理预填充解码 - inferenceMultiLora ：推理Multi-Lora - inferenceServerDistri bute ：分布式推理 - inferenceDiffusion ：扩散模型推理 - PT ：预训练 - CPT ：持续预训练 - SFT LoRA ：SFT _ LoRA微调 - SFT full ：SFT全参微 _ 调 - DPO LoRA ：DPO _ LoRA微调 - DPO full ：DPO全参 _ 微调 - GRPO LoRA ：GRPO _ LoRA微调 - GRPO full ：GRPO全 _ 参微调 - RL LoRA ：RL LoRA _ 微调 - RL full ：RL全参微调 _ - trainCustom ：自定义训练 - quant ：量化。 |
| imageId | Strin g | Body | 否 | img- 91fa01150ee51045190b aa305e**** | 镜像ID。 |
| imageVer sion | Strin g | Body | 否 | ImagVersion | 套件关联的镜像版本信息对象。 |
| codeRepoI d | Strin g | Body | 否 | cd- 96a5060c0a9570404f09 a8f0747**** | 套件关联的代码仓库ID。 |
| pageIndex | Integ er | Body | 否 | 10 | 套件列表的页码。 |
| pageSize | Integ er | Body | 否 | 1 | 套件列表每页条数。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -frameworks | List | 2 | 适配框架类型列表。 |
| -xpus | List | [APG] | 适配硬件类型列表。 |
| -models | Array | [Model] | 套件关联的模型列表，元素为Model对象。 |
| --modelId | String | model- rbvg5wzljz****ks92 | 模型ID。 |
| -- modelVersion | String | V1.0.0 | 模型版本号。 |
| -aliyunUid | String | 19822605****1225 | 阿里云账号。 |
| -codeRepoId | String | cd- 96a5060c0a95704 04f09a8f0747**** | 套件关联的代码仓库ID。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - componentCat egoryId | String | inferenceServer | 套件类别ID，枚举值如下： inferenceServer：推理服务 inferencePrefillDecode：推理预填充解码 inferenceMultiLora：推理Multi-Lora inferenceServerDistribute：分布式推理 inferenceDiffusion：扩散模型推理 PT：预训练 CPT：持续预训练 SFT LoRA：SFTLoRA微调 _ SFT full：SFT全参微调 _ DPO LoRA：DPOLoRA微调 _ DPO full：DPO全参微调 _ GRPO LoRA：GRPO LoRA微调 _ GRPO full：GRPO全参微调 _ RL LoRA：RL LoRA微调 _ RL full：RL全参微调 _ trainCustom：自定义训练 quant：量化。 |
| - componentDe scription | String | 222 | 套件描述信息。 |
| -componentId | String | cp- 42942e39****49c6 83ae**** | 套件唯一标识ID。 |
| - componentNa me | String | 本地新建套件2 | 套件名称。 |
| - componentSou rce | String | custom | 套件来源，custom为用户自定义，admin为系统内置。 |
| - componentTyp e | String | inference | 套件类型，由componentCategoryId自动推导，枚举值如下： - inference ：推理 - train ：训练 - quant ：量化。 |
| -gmtCreated | String | 2025-11- 10T12:09:22Z | 套件创建时间，格式为UTC时间。 |
| -gmtModified | String | 2025-11- 12T14:10:48Z | 套件最后修改时间，格式为UTC时间。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionId | String | cn-neimeng-236e- d01 | 地域ID。 |
| - componentLab els | Struct | {"ability": ["InferAccel"]} | 套件标签信息，键值对形式，key为标签类型，value为标签值列表。 |
| --ability | List | MemAccSep | 套件能力。 |
| -- disaggInfernen ceMode | List | true | 分布式推理能力。 |
| -- kvCacheOffloa d | List | true | 多级缓存能力。 |
| -- modelDomain | List | MM-Understand | 模型领域。 |
| -imageVersion | Struct | ImagVersion | 套件关联的镜像版本信息对象。 |
| --imageId | String | img- 05cefd0be2exxxx | 镜像ID。 |
| -- imageVersion | String | 3.2.41 | 套件关联的镜像版本信息对象。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 查询总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 页码。 |

**示例**

智能体工厂 OpenTrek 请求示例

```json
POST /component/list HTTP/1.1 { "componentSource":"admin" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "componentType":"inference",
   "gmtModified":"2025-11-12T14:10:48Z",
   "componentId":"cp-42942e39****49c683ae****",
   "componentLabels":[
    {
     "disaggInfernenceMode":"true",
     "ability":"MemAccSep",
     "kvCacheOffload":"true",
     "modelDomain":"MM-Understand"
    }
```

`],`

```json
   "frameworks":2,
   "aliyunUid":"19822605****1225",
   "gmtCreated":"2025-11-10T12:09:22Z",
   "componentDescription":"222",
   "componentCategoryId":"inferenceServer",
   "imageVersion":[
    {
     "imageVersion":"3.2.41",
     "imageId":"img-05cefd0be2exxxx"
    }
```

`],`

```json
   "xpus":"[APG]",
   "models":[
    {
     "modelId":"model-rbvg5wzljz****ks92",
     "modelVersion":"V1.0.0"
    }
```

`],`

```json
   "codeRepoId":"cd-96a5060c0a9570404f09a8f0747****",
   "regionId":"cn-neimeng-236e-d01",
```

`"componentName":"`本地新建套件`2",`

```json
   "componentSource":"custom"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

### 软件源

#### UpdateSoftwareSourceConfig

智能体工厂 OpenTrek

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /softwareSourceConfig/updateSoftwareSourceConfig HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| yumAddre ss | Strin g | Body | 否 | https://mirrors.***** | yum源地址。 |
| debianAd dress | Strin g | Body | 否 | https://mirrors.***** | debian源地址。 |
| pipAddres s | Strin g | Body | 否 | https://mirrors.***** | pip源地址。 |
| condaAdd ress | Strin g | Body | 否 | https://repo.ana***** | conda源地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
PUT /softwareSourceConfig/updateSoftwareSourceConfig HTTP/1.1 { }
```

智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListSoftwareSource

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /softwareSource/list HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - cacheExpireTi me | Integer | 2592000 | 缓存过期时间，单位：秒。 |
| -cacheSize | Integer | 10240 | 已缓存的大小，单位为字节。 |
| -proxyAddr | String | https://mirrors.aliy un.com/ | 代理地址。 |
| - proxyAddrCon nectivity | Boolean | true | 代理地址连通性： 1：连通 0：不连通 |
| -status | Boolean | true | 软件源状态： 1：启用 0：停用 |

|  | 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -type | String | pypi | 软件源类别。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
GET /softwareSource/list HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UpdateSoftwareSource

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /softwareSource/update HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | Strin g | Body | 是 | pypi | 软件源类型，该参数必填， 取值范围： pypi yum deb conda |
| status | Boole an | Body | 是 | true | 软件源的启用状态，该参数必填。 |
| proxyAddr | Strin g | Body | 否 | http://mirrors.aliyun.com / | 公网软件源转发地址。 |
| cacheExpi reTime | Strin g | Body | 否 | 3600 | 表示缓存过期时间设置为 3600秒（即1小时），超过该时间后缓存数据将被视为过期并被清除或重新加载。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /softwareSource/update HTTP/1.1 { "type":"pypi", "status":"true" }
```

智能体工厂 OpenTrek 正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 资源同步

#### ListBmcpImageSyncHistory

调用ListBmcpImageSyncHistory查询所有的BMCP镜像同步记录列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /systemConfig/listBmcpImageSyncHistory HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| imageNa me | Strin g | Query | 否 | image-name | 镜像名称。 |
| imageVer sion | Strin g | Query | 否 | v1 | 镜像版本。 |
| pageIndex | Integ er | Query | 否 | 1 | 同步记录列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -failImageInfo | List | [] | 失败镜像信息列表，元素包含imageName（镜像名称）和imageVersion（镜像版本）。 |
| - successImageI nfo | Array | [{"imageName":"s glang","imageVersi on":"0.4.7- ubuntu24.04- sail1.5.3-cuda12.6- py312"}, {"imageName":"vll m","imageVersion" :"0.9.1- ubuntu24.04- sail1.5.3-cuda12.6- py312"}] | 成功镜像信息列表，元素包含imageName（镜像名称）和imageVersion（镜像版本）。 |
| --imageName | String | sglang | 镜像名称。 |
| -- imageVersion | String | 0.4.7-ubuntu24.04- sail1.5.3-cuda12.6- py312 | 镜像版本。 |
| - failImageCoun t | Integer | 0 | 同步失败镜像数量。 |
| -gmtCreated | String | 2026-03- 03T03:34:56Z | 同步时间，格式为UTC时间。 |
| -imageCount | Integer | 4 | 同步镜像数量。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -result | Integer | 1 | 同步状态，聚合值： 1 （全部成功） 0 （全部失败） 2 （部分成功）。 |
| - successImage Count | Integer | 4 | 同步成功镜像数量。 |
| -syncId | String | aa9018b7****dede f79 | 同步操作id。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 同步记录的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 同步记录的页码。 |

**示例**

请求示例

```
GET /systemConfig/listBmcpImageSyncHistory HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "failImageCount":0,
   "imageCount":4,
   "result":1,
   "successImageInfo":[
    {
     "imageVersion":"0.4.7-ubuntu24.04-sail1.5.3-cuda12.6-py312",
     "imageName":"sglang"
    }
```

`],`

```json
   "gmtCreated":"2026-03-03T03:34:56Z",
   "failImageInfo":"[]",
   "successImageCount":4,
   "syncId":"aa9018b7****dedef79"
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### SyncBmcpImage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| category | Strin g | Body | 否 | Inference | 镜像类别。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Integer | 1 | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
{ }
```

正常返回示例 `JSON` 格式

```json
{
 "data":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 用户APIKey

#### CreateGatewayAPIKey

**请求头**

智能体工厂 OpenTrek 该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/create-gateway-apikey HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyNa me | Strin g | Body | 是 | Test | API Key的自定义名称，该参数必填。 |
| status | Integ er | Body | 是 | 1 | 加速器状态，该参数必填， 取值范围： 1：启用。 0：禁用。 |
| organizati onUid | Strin g | Body | 是 | org-1234567890abcdefg | 组织的UID，该参数必填。 |
| organizati onId | Strin g | Body | 是 | 2 | 组织ID，该参数必填。 |
| organizati onName | Strin g | Body | 是 | MyOrganization | 组织名称，该参数必填。 |
| resourceG roupUid | Strin g | Body | 是 | rs-1234567890abcefg | 资源集的UID，该参数必填。 |
| resourceG roupId | Strin g | Body | 是 | 3 | 资源集ID。该参数必填。 |
| resourceG roupName | Strin g | Body | 是 | resourceGroupName | 资源集名称，该参数必填。 |
| aliyunSub Uid | Strin g | Body | 是 | 2277043054***** | 阿里云子账号Uid，该参数必填。 |
| aliyunSubI d | Strin g | Body | 是 | 5001 | 阿里云子账号ID，该参数必填。 |
| aliyunSub Name | Strin g | Body | 是 | user | 阿里云子账号登录名称，该参数必填。 |
| enableExp ireTime | Boole an | Body | 是 | true | 表示启用过期时间功能，APIKey将在指定的过期时间后自动失效，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| expireTim e | Strin g | Body | 否 | 2021-01-20T09:25:56Z | APIKey失效的UTC时间。 当enableExpireTime为 true时，该参数不能为空。 |
| occupantI d | Strin g | Body | 否 | os-4821934902*** | APIKey绑定的在线服务ID/ 灰度组ID。 说明：2512版本该参数已废弃。 |
| apikeyTyp e | Strin g | Body | 否 | internet | APIKey类型，取值范围： intranet：系统APIKey internet：用户APIKey 说明：2512版本该参数已废弃。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /online-service/create-gateway-apikey HTTP/1.1 { "apikeyName":"Test", "status":"1", "organizationUid":"org-1234567890abcdefg", "organizationId":"2", "organizationName":"MyOrganization", "resourceGroupUid":"rs-1234567890abcefg", "resourceGroupId":"3", "resourceGroupName":"resourceGroupName", "aliyunSubUid":"2277043054*****", "aliyunSubId":"5001", "aliyunSubName":"user", "enableExpireTime":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### DeleteGatewayAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /online-service/delete-gateway-apikey HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Query | 是 | aigk-123456 | APIKey的ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
DELETE /online-service/delete-gateway-apikey HTTP/1.1 &apikeyUid=1234567890abcdef
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyGatewayAPIKeyStatus

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-gateway-apikey-status HTTP/1.1
```

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Body | 是 | aigk-123456 | APIKey的ID，该参数必填。 |
| status | Integ er | Body | 是 | 1 | APIKey状态，该参数必填， 取值范围： 0：禁用 1：启用 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误码。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /online-service/modify-gateway-apikey-status HTTP/1.1 { "apikeyUid":"aigk-123456", "status":"1" }
```

正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### UnbindGatewayAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /online-service/unbind-gateway-apikey HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Body | 是 | aigk-4fb8b2*** | ApiKey唯一标识ID，该参数必填。 |
| onlineServ iceIds | Json | Body | 是 | [os-1hd***, os-743***, os-hbf***] | 需要解绑的在线服务列表， 该参数必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /online-service/unbind-gateway-apikey HTTP/1.1 { "apikeyUid":"aigk-4fb8b2***", "onlineServiceIds":"[os-1hd***, os-743***, os-hbf***]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### BindGatewayAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Body | 是 | aigk-4fb8b2*** | ApiKey唯一标识ID，该参数必填。 |
| onlineServ iceIds | Json | Body | 是 | [os-1hd***, os-743***, os-hbf***] | 需要绑定的在线服务ID列表，该参数必填。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
{ "apikeyUid":"aigk-4fb8b2***", "onlineServiceIds":"[os-1hd***, os-743***, os-hbf***]" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyGatewayAPIKeyAutoBinding

调用ModifyGatewayAPIKeyAutoBinding修改指定APIKey的自动绑定状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Body | 是 | aigk-4fb8b2*** | ApiKey唯一标识ID，该参数必填。 |
| enableAut oBinding | Boole an | Body | 是 | true | 是否启用自动绑定功能，该参数必填，取值范围： true：启用。 false：禁用。 |
| userRamr ole | Strin g | Body | 否 | acs:ram::198****:role/as cm-role-*-*-*** | 用户被授予角色的ARN。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

#### ListUserAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 用户APIKey列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| apikeyUid | Strin g | Query | 否 | aigk-4fb8b2*** | ApiKey唯一标识ID。 |
| apiKeyNa me | Strin g | Query | 否 | key | API密钥名称。 |
| organizati onUid | Strin g | Query | 否 | org-1234567890abcdefg | 组织的UID。 |
| organizati onName | Strin g | Query | 否 | MyOrganization | 组织名称。 |
| resourceG roupUid | Strin g | Query | 否 | rs-1234567890abcefg | 资源集的UID。 |
| resourceG roupName | Strin g | Query | 否 | resourceGroupName | 资源集名称。 |
| status | Strin g | Query | 否 | ENABLE | APIKey状态，取值范围： ENABLE：启用。 DISABLE：禁用。 EXPIRED：过期。 |
| autoBindi ng | Integ er | Query | 否 | 1 | 自动绑定的状态，取值范围： 1：启用。 0：禁用。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -gmtCreated | String | 2025-12-23 07:02:18 | 创建时间，格式：yyyy-MM-dd HH:mm:ss。 |
| -gmtModified | String | 2025-12-23 07:02:18 | 修改时间，格式：yyyy-MM-dd HH:mm:ss。 |
| -aliyunUid | String | 1982****21225 | 阿里云主账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，标识资源所在的区域。 |
| -apikeyUid | String | aigk- 50aca7****ec4048 b4 | 用户 API Key 的唯一标识 ID，前缀为 aigk-。 |
| -apikeyName | String | suihuai-apikey | 用户 API Key 的名称，由用户创建时指定。 |
| - organizationUi d | String | org- 1034b60b****0aec 1029000v | 组织 UID，组织的唯一标识。 |
| - organizationN ame | String | iaas test _ | 组织名称。 |
| - resourceGroup Uid | String | rs- 1034b60b****0aec 1029000c | 资源集 UID，资源集的唯一标识。 |
| - resourceGroup Name | String | ResourceSet(iaas t _ est) | 资源集名称。 |
| -aliyunSubUid | String | 2428119****97941 46 | 阿里云子账号 UID，创建该 API Key 的子账号标识。 |
| - aliyunSubNam e | String | suihuai | 阿里云子账号名称。 |
| -apikey | String | sk-************ | API Key 密钥值（已解密后返回），用于接口调用鉴权。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -status | String | ENABLE | API Key 状态，枚举类型 UserApiKeyStatusEnum。枚举值如下： ENABLE：启用 DISABLE：禁用 EXPIRED：已过期 |
| -autoBinding | Integer | 0 | 自动绑定开关，枚举类型 OperateStatusEnum。枚举值如下： 1（ENABLE）：启用自动绑定 0（DISABLE）：禁用自动绑定 |
| - enableExpireTi me | Boolean | false | 是否启用过期时间。 |
| -expireTime | String | 9999-12- 31T23:59:59Z | 过期时间，UTC 时区，格式：yyyy-MM- dd'T'HH:mm:ss'Z'。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 1 | 用户APIKey的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 用户APIKey的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"-",
 "pageIndex":1,
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":1
}
```

#### GetUserAPIKey

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apiKeyUid | Strin g | Query | 否 | aigk-4fb8b2*** | ApiKey唯一标识ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - boundRamrole s | List | ["acs:ram:19****** 787::role"] | 绑定的 RAM 角色列表。 |
| - boundOnlineS erviceList | Array | [{"onlineServiceId" : "os-****", "onlineServiceNam e": "my-service"}] | 绑定的在线服务列表。每个元素包含： onlineServiceId：在线服务/服务组 ID onlineServiceName：在线服务/服务组名称 |
| -- onlineServiceI d | String | os-**** | 在线服务/服务组 ID。 |
| -- onlineServiceN ame | String | my-service | 在线服务/服务组名称。 |
| -gmtCreated | String | 2025-12-23 07:02:18 | 创建时间，格式：yyyy-MM-dd HH:mm:ss。 |
| -gmtModified | String | 2025-12-23 07:02:18 | 修改时间，格式：yyyy-MM-dd HH:mm:ss。 |
| -aliyunUid | String | 1982****21225 | 阿里云主账号 UID。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，标识资源所在的区域。 |
| -apikeyUid | String | aigk- 50aca7****ec4048 b4 | 用户 API Key 的唯一标识 ID，前缀为 aigk-。 |
| -apikeyName | String | suihuai-apikey | 用户 API Key 的名称，由用户创建时指定。 |
| - organizationUi d | String | org- 1034b60b****0aec 1029000v | 组织 UID，组织的唯一标识。 |
| - organizationN ame | String | iaas test _ | 组织名称。 |
| - resourceGroup Uid | String | rs- 1034b60b****0aec 1029000c | 资源集 UID，资源集的唯一标识。 |
| - resourceGroup Name | String | ResourceSet(iaas t _ est) | 资源集名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -aliyunSubUid | String | 2428119****97941 46 | 阿里云子账号 UID，创建该 API Key 的子账号标识。 |
| - aliyunSubNam e | String | suihuai | 阿里云子账号名称。 |
| -apikey | String | sk-************ | API Key 密钥值（已解密后返回），用于接口调用鉴权。 |
| -status | String | ENABLE | API Key 状态，枚举类型 UserApiKeyStatusEnum。枚举值如下： ENABLE：启用 DISABLE：禁用 EXPIRED：已过期 |
| -autoBinding | Integer | 0 | 自动绑定开关，枚举类型 OperateStatusEnum。枚举值如下： 1（ENABLE）：启用自动绑定 0（DISABLE）：禁用自动绑定 |
| - enableExpireTi me | Boolean | false | 是否启用过期时间。 |
| -expireTime | String | 9999-12- 31T23:59:59Z | 过期时间，UTC 时区，格式：yyyy-MM- dd'T'HH:mm:ss'Z'。当 enableExpireTime 为 false 时，值为 9999-12-31T23:59:59Z（表示永不过期） |

**示例**

请求示例

```
&apiKeyUid=aigk-4fb8b2***
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### ModifyGatewayAPIKeyExpireTime

调用ModifyGatewayAPIKeyExpireTime修改指定APIKey的过期时间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /online-service/modify-gateway-apikey-expire-time HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| apikeyUid | Strin g | Body | 是 | aigk-4fb8b2*** | ApiKey唯一标识ID。该参数必填。 |
| enableExp ireTime | Boole an | Body | 是 | true | 表示启用过期时间功能，APIKey将在指定的过期时间后自动失效，该参数必填。 |
| expireTim e | Strin g | Body | 否 | 2021-01-20T09:25:56Z | APIKey失效的UTC时间。 当enableExpireTime为 true时，该参数不能为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
PUT /online-service/modify-gateway-apikey-expire-time HTTP/1.1 { "apikeyUid":"aigk-4fb8b2***", "enableExpireTime":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 用户优先级

#### DeleteUserPriority

调用DeleteUserPriority删除用户优先级，删除后用户在组织资源集下的优先级重置为默认用户优先级。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /user/priority/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| userPriorit yId | Strin g | Query | 是 | user-priority- 1234567890abcd | 用户优先级ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态提示信息。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /user/priority/delete HTTP/1.1 { "userPriorityId":"user-priority-1234567890abcd" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListUserPriority

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /user/priority/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 页码。 默认值：1。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integ er | Query | 否 | 10 | 每页数据条数。 默认值：10。 |
| userPriorit yId | Strin g | Query | 否 | user-priority- 1234567890abcd | 用户优先级实例ID。 |
| organizati onUid | Strin g | Query | 否 | org-1234567890abcdefg | 组织的唯一标识符，用于在系统中唯一识别一个组织实体。精确匹配。 |
| organizati onName | Strin g | Query | 否 | organizationName | 组织名称， 如"MyOrganization"。模糊匹配。 |
| resourceG roupUid | Strin g | Query | 否 | rs-1234567890abcefg | 资源集的唯一标识符，用于在系统中唯一识别一个资源集实体。精确匹配。 |
| resourceG roupName | Strin g | Query | 否 | resourceGroupName | 资源集名称。 |
| aliyunSub Uid | Strin g | Query | 否 | 123456789000000 | 阿里云子账号Uid。 |
| aliyunSub LoginNam e | Strin g | Query | 否 | aliyunSubLoginName | 阿里云子账号的登录名称。 |
| aliyunSub DisplayNa me | Strin g | Query | 否 | aliyunSubDisplayName | 阿里云子账号的显示名称。 |
| userPriorit y | Strin g | Query | 否 | 1 | 用户优先级。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 支持：userPriority。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序，取值范围： DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - aliyunSubDispl ayName | String | testaccount | 阿里云子账号的显示名称。 |
| -aliyunSubId | Integer | 1 | 子账号ID。 |
| - aliyunSubLogi nName | String | test account | 阿里云子账号的登录名称。 |
| -aliyunSubUid | String | 1277043054***** | 阿里云子账号Uid。 |
| -aliyunUid | String | 157123456789**** | 阿里云主账号ID。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| -gmtModified | String | 2022-01- 07T10:07:57Z | 修改时间。 |
| -id | Integer | 1 | 此优先级的ID。 |
| -organizationId | Integer | 22 | 组织ID。 |
| - organizationN ame | String | orgTest | 组织名称。 |
| - organizationUi d | String | org-12345****** | 组织的唯一标识符。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - resourceGroup Id | Integer | 1002 | 资源集ID。 |
| - resourceGroup Name | String | res test _ | 资源集名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - resourceGroup Uid | String | rs-123456789*** | 资源集的唯一标识符。 |
| -status | Integer | 1 | 状态，0: 禁用，1: 启用。 |
| -userPriority | Integer | 5 | 用户优先级，1-10。 |
| -userPriorityId | String | user-priority- 12345678**** | 用户优先级实例ID。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 查询记录总数。 |
| pageSize | Integer | 10 | 每页条数。 |
| pageIndex | Integer | 1 | 页码。 |

**示例**

请求示例

```
GET /user/priority/list HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"-",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### CreateUserPriority

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /user/priority/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizati onId | Long | Body | 是 | 1 | 组织ID，该参数必填。 |
| organizati onUid | Strin g | Body | 是 | org- 1234567890abcdefghijkl mn | 组织的唯一标识符，用于在系统中唯一识别一个组织实体，该参数必填。 |
| organizati onName | Strin g | Body | 否 | organizationName | 组织名称， 如"MyOrganization"。 |
| resourceG roupId | Long | Body | 是 | 1 | 资源集ID，该参数必填。 |
| resourceG roupUid | Strin g | Body | 是 | rs- 1234567890abcdefghijkl mn | 资源集的唯一标识符，用于在系统中唯一识别一个资源集实体，该参数必填。 |
| resourceG roupName | Strin g | Body | 否 | resourceGroupName | 资源集名称。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| aliyunSubI d | Long | Body | 是 | 1 | aliyun子账号ID，该参数必填。 |
| aliyunSub Uid | Strin g | Body | 是 | 123456789000000000 | 阿里云子账号Uid，该参数必填。 |
| aliyunSub LoginNam e | Strin g | Body | 否 | aliyunSubLoginName | 阿里云子账号登录名称，用于子用户登录阿里云平台的身份标识。 |
| aliyunSub DisplayNa me | Strin g | Body | 否 | aliyunSubDisplayName | 该字段表示阿里云子账号的显示名称，用于标识子用户在控制台中展示的名称。 |
| userPriorit y | Integ er | Body | 是 | 1 | 用户优先级，用于标识用户在指定组织资源集下能下发任务的最高优先级，该参数必填，取值范围为整数1- 10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例智能体工厂 OpenTrek

```json
POST /user/priority/create HTTP/1.1 { "organizationId":"1", "organizationUid":"org-1234567890abcdefghijklmn", "resourceGroupId":"1", "resourceGroupUid":"rs-1234567890abcdefghijklmn", "aliyunSubId":"1", "aliyunSubUid":"123456789000000000", "userPriority":"1" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyUserPriority

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /user/priority/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| userPriorit yId | Strin g | Body | 是 | user-priority- 1234567890abcd | 用户优先级ID，该参数必填。 |
| userPriorit y | Integ er | Body | 是 | 2 | 修改后的用户优先级，该参数必填，取值范围整数1- 10。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态提示信息。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /user/priority/modify HTTP/1.1 { "userPriorityId":"user-priority-1234567890abcd", "userPriority":"2" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetUserPriorityDetail

调用GetUserPriorityDetail查询用户在组织资源集下优先级详情信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizati onId | Long | Query | 否 | 1 | 组织ID。 |
| resourceG roupId | Long | Query | 否 | 2 | 资源集ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态提示信息。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - aliyunSubDispl ayName | String | 测试账号1 | 子账号显示名称。 |
| -aliyunSubId | Integer | 1002 | 子账号数据ID。 |
| - aliyunSubLogi nName | String | testaccount1 | 阿里云子账号的登录名称。 |
| -aliyunSubUid | String | 20000****** | 子账号唯一标识符。 |
| -aliyunUid | String | 1000000***** | 主账号阿里云唯一标识符。 |
| -gmtCreated | String | 2022-02- 25T06:57:41Z | 创建时间。 |
| -gmtModified | String | 2025-02- 25T06:57:41Z | 修改时间。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -id | Integer | 1 | 用户数据ID。 |
| -organizationId | Integer | 2 | 组织ID。 |
| - organizationN ame | String | orgTesttest | 组织名称。 |
| - organizationUi d | String | org-1034b******* | 组织的唯一标识符。 |
| -regionId | String | cn-hangzhou | 地域ID。 |
| - resourceGroup Id | Integer | 1 | 资源集ID。 |
| - resourceGroup Name | String | res testtest _ | 资源集名称。 |
| - resourceGroup Uid | String | rs-1234****** | 资源集的唯一标识符。 |
| -status | Integer | 1 | 状态，0: 禁用，1: 启用。 |
| -userPriority | Integer | 5 | 用户优先级，1-10。 |
| -userPriorityId | String | user-priority- 123456***** | 用户优先级ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### Readme文档

#### DeleteDocument

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
DELETE /doc/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| docId | Strin g | Query | 是 | 14e52afc0ecec046fd0a9 320be23a**** | 文档ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

智能体工厂 OpenTrek

**示例**

请求示例

```
DELETE /doc/delete HTTP/1.1 &docId=14e52afc0ecec046fd0a9320be23a****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ModifyDocument

调用ModifyDocument修改指定文档的部分信息，包括文档标题、版本和存储路径。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /doc/modify HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| docId | Strin g | Body | 是 | 89a5a8d30dbb9042650 988d07b**** | 文档ID，该参数必填。 |
| docName | Strin g | Body | 是 | doc-name | 文档名称，该参数必填。 |
| docVersio n | Strin g | Body | 是 | v1.0 | 文档版本号，该参数必填， 版本号支持：vx.x格式(例如 v1.0)。 |
| docUrl | Strin g | Body | 是 | https://****.oss- ****/****.pdf" | 存储路径，该参数必填。 |
| resourceId | Strin g | Body | 是 | os- 123f3c61074d3046b408 be70c81**** | 资源ID，该参数必填。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceV ersion | Strin g | Body | 否 | v1 | 资源版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
PUT /doc/modify HTTP/1.1 { "docId":"89a5a8d30dbb9042650988d07b****", "docName":"doc-name", "docVersion":"v1.0", "docUrl":"https://****.oss-****/****.pdf"", "resourceId":"os-123f3c61074d3046b408be70c81****" }
```

正常返回示例 `JSON` 格式

```json
{
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### CreateDocument

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /doc/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| docName | Strin g | Body | 是 | doc-name | 文档名称，该参数必填，长度为2～64个字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线 （ ）和短划线（-）。 _ |
| docVersio n | Strin g | Body | 是 | v1.0 | 文档版本号，该参数必填， 版本号支持：vx.x格式(例如 v1.0)。 |
| docUrl | Strin g | Body | 是 | https://****.oss- ****/****.pdf | 文档存储路径，该参数必填。 |
| resourceId | Strin g | Body | 是 | os- 123f3c61074d3046b408 be70c81**** | 资源ID，该参数必填。 |
| resourceV ersion | Strin g | Body | 否 | v1 | 资源版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | { "docId": "****" } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```json
POST /doc/create HTTP/1.1 { "docName":"doc-name", "docVersion":"v1.0", "docUrl":"https://****.oss-****/****.pdf", "resourceId":"os-123f3c61074d3046b408be70c81****" }
```

正常返回示例 `JSON` 格式

```json
{
 "data":"{\t\"docId\": \"****\"}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

#### GetDocument

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /doc/get HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| docId | Strin g | Query | 是 | bedd****d636 | 文档的唯一标识符。 |

智能体工厂 OpenTrek

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -aliyunUid | String | 1982****1225 | 阿里云主账号 ID，用于标识文档的所有者。 |
| -docId | String | bedd****d636 | 文档的唯一标识符。 |
| -docName | String | jieyoutest | 文档的名称。 |
| -docUrl | String | https://zytest.oss- cn-neimeng-236e- d01- a.env236.ops.arm. com/configXEOS 6.4.200 对象存储 S3 API.docx | 文档的访问 URL 地址。 |
| -docVersion | String | v1.0 | 文档的版本号。 |
| -gmtCreated | String | 2026-01-13 06:55:54.0 | 文档创建时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| -gmtModified | String | 2026-01-13 06:56:28.0 | 文档最后修改时间，格式为 yyyy-MM-dd HH:mm:ss。 |
| -regionId | String | cn-neimeng-236e- d01 | 地域 ID，表示文档所属的地域。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -resourceId | String | md-3****4693 | 关联资源的 ID，如模型 ID 或任务 ID。 |
| - resourceVersio n | String | v1.0 | 关联资源的版本号。 |

**示例**

请求示例

```
GET /doc/get HTTP/1.1 &docId=f16bea0f0669404e110b15213901a588****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "docName":"",
  "gmtModified":"",
  "resourceId":"",
  "aliyunUid":"",
  "gmtCreated":"",
  "regionId":"",
  "docId":"",
  "resourceVersion":"",
  "docUrl":"",
  "docVersion":""
 },
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

### 可观测

#### PodLogExport

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

智能体工厂 OpenTrek

```
GET /k8s-resource/export-pod-log HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 分页查询时设置的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | time | 排序字段。 默认值：time。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| startTime | Strin g | Query | 否 | 2024-08-02 18:09:14 | 开始时间。 |
| endTime | Strin g | Query | 否 | 2024-08-03 11:19:23 | 结束时间。 |
| container Name | Strin g | Query | 否 | test-container | 容器名称。 |
| podName | Strin g | Query | 否 | tk- ca57b1400f2e7045f408 01a0*****-keajob- worker-0 | POD名称。 |
| entityId | Strin g | Query | 是 | nb- ad56b7f600740042f20b 89a033b**** | 服务日志ID。 |
| content | Strin g | Query | 否 | "" | 日志内容筛选。 |
| nodeId | Strin g | Query | 否 | i-coev0ueheob771**** | 节点ID。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | { "downloadUrl": "hangzhou- 1.aliyuncs.com/xxx xx/xxxxxxxxxxxxxx ? Expires=16714481 25&OSSAccessKeyI d=xxx", "fileName": "aa.log", "lineCount": 50, "truncated": false } | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -downloadUrl | String | https://xxxxxxxx.os s-cn-hangzhou- 1.aliyuncs.com/xxx xx/xxxxxxxxxxxxxx ? Expires=16714481 25&OSSAccessKeyI d=xxx | 日志文件下载链接。 |
| -fileName | String | music.log | 日志文件名称。 |
| -lineCount | Integer | 50 | 日志文件行数。 |
| -truncated | Boolean | true | 是否因行上限被截断。 true：实际行数 < PageSize的时候 。 |

**示例**

请求示例智能体工厂 OpenTrek

```
GET /k8s-resource/export-pod-log HTTP/1.1 &entityId=nb-ad56b7f600740042f20b89a033b****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "fileName":"music.log",
  "downloadUrl":"https://xxxxxxxx.oss-cn-hangzhou-1.aliyuncs.com/xxxxx/xxxxxxxxxxxxxx?E
xpires=1671448125&OSSAccessKeyId=xxx",
  "truncated":true,
  "lineCount":50
 },
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListEvent

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 事件列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |

| 智能体工厂 Ope | nTrek |  |  |  | AI Studio 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序，取值范围： DESC：降序。 ASC：升序。 默认值：DESC。 |
| startTime | Strin g | Query | 否 | 2025-11- 01T03:20:13.000Z | 开始时间。 |
| endTime | Strin g | Query | 否 | 2025-11- 02T03:20:13.000Z | 结束时间。 |
| eventNam e | Strin g | Query | 否 | event-name | 事件名称。 |
| eventType | Strin g | Query | 否 | Pod | 触发事件实例类型。 |
| eventLeve l | Strin g | Query | 否 | Normal | 事件等级，取值范围： Normal Warning Error |
| eventDesc | Strin g | Query | 否 | System error | 事件描述信息。 |
| entityId | Strin g | Query | 是 | nb- ad56b7f600740042f20b 89a033b**** | 服务事件ID。 |
| subEntityI d | Strin g | Query | 否 | nb- ad56b7f600740042f20b 89a033b**** | 子服务事件ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -eventDesc | String | Readiness probe failed: dial tcp 172. | 事件描述 |
| -eventLevel | String | Warning | 事件等级 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -eventName | String | Unhealthy | 事件名称。 |
| -eventType | String | Pod | 事件类型。 |
| -gmtCreated | String | 2026-03- 06T03:37:30Z | 事件事件 |
| -instanceId | String | os- 9e61451b0333804 f00- 555c9b9d5***** | 实例ID。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 事件的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 事件的页码。 |

**示例**

请求示例

```
&entityId=nb-ad56b7f600740042f20b89a033b****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "eventDesc":"",
   "eventLevel":"",
   "instanceId":"",
   "gmtCreated":"",
   "eventName":"",
   "eventType":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ListPodLog

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | 日志列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | time | 排序字段。 默认值：time。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| startTime | Strin g | Query | 否 | 2024-08-02 18:09:14 | 开始时间。 |
| endTime | Strin g | Query | 否 | 2024-08-03 11:19:23 | 结束时间。 |
| container Name | Strin g | Query | 否 | master | 容器名称。 |
| podName | Strin g | Query | 否 | tk- ca57b1400f2e7045f408 01a0*****-keajob- worker-0 | pod名称。 |
| entityId | Strin g | Query | 是 | nb- ad56b7f600740042f20b 89a033b**** | 服务日志ID。 |
| content | Strin g | Query | 否 | "" | 日志内容筛选。 |
| nodeId | Strin g | Query | 否 | i-coev0ueheob771**** | 节点ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - containerNam e | String | main | 容器名称。 |
| -content | String | 2026-03- 06T05:12:01.0195 71816Z [1;36m(A | 响应内容 |
| -podName | String | os- 4303ffc905d1b04c c2-***** | pod名称 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -time | String | 2016-09- 13T16:04:00Z | 查询时间 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 日志的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 日志的页码。 |

**示例**

请求示例

```
&entityId=nb-ad56b7f600740042f20b89a033b****
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":[
  {
   "containerName":"",
   "podName":"",
   "time":"",
   "content":""
  }
```

`],`

```json
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### ListNode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceId | Strin g | Query | 是 | os- 123f3c61074d300c81*** * | 资源ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | - | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| - bmcpNodeIdLi st | List | ["ack-xxxxxxx", "ack-xxxxxxx", "ack-xxxxxxx"] | BMCP节点ID集合。 |
| -ecsNodeIdList | List | ["c1a4096860f0f48 6*****1", "c1a4096860f0f48 6*****"] | ECS ID集合。 |
| -bmcp | String | ack-xxxxxxx | BMCP集群ID。 |
| -clusterType | String | egs | 集群类型。 egs。 bmcp。 |
| -egs | String | c1a4096860f0f486 *****1 | EGS集群ID。 |

**示例**

请求示例

```
&resourceId=os-123f3c61074d300c81****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"-",
 "success":false,
 "dynamicMessages":"\t[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```

智能体工厂 OpenTrek

#### GetTenantObservability

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| entityId | Strin g | Query | 否 | rp-60a79b670c***** | 实体ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | {\"logQueryModel\" : \"page\", \"rdma\": false, \"dashboardModel\ ": \"Grafana\"} | 租户可观测特性配置信息。 |
| - logQueryMode l | String | page | 日志展示方式，取值范围： page：分页展示。 cursor：游标展示。 |
| - dashboardMod el | String | Grafana | 监控面板模式，取值范围： PAI。 Grafana。 tianyan。 dashboard。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -rdma | Boolean | false | 是否展示GPU网络拓扑大盘，取值范围： true：展示。 false：不展示。 |

**示例**

请求示例

```
GET /monitoring/GetTenantObservability HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":{
  "dashboardModel":"Grafana",
  "rdma":false,
  "logQueryModel":"page"
 },
 "success":true,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

### 基础服务

#### GetManagedGpuCount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resource/statics/managedGpuCount HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

智能体工厂 OpenTrek

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| poolId | Strin g | Query | 否 | rp-xxxx | 资源池ID。为空表示查询当前Region下所有可用纳管 GPU芯片数量的总值。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| data | Struct | { "totalGpuCount": 8 } | 返回数据。 |
| - totalGpuCount | Integer | 8 | 已纳管GPU芯片数量。 |

**示例**

请求示例

```
GET /resource/statics/managedGpuCount HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式智能体工厂 OpenTrek

```json
{
 "data":{
  "totalGpuCount":8
 },
 "success":false,
 "dynamicMessages":"-",
 "errorMessage":"",
 "errorCode":"500",
 "httpCode":200
}
```

#### ListPod

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageIndex | Integ er | Query | 否 | 1 | Pod列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |
| podName | Strin g | Query | 否 | pod-name | Pod名称。 |
| podType | Strin g | Query | 否 | worker | Pod类型。 |

| I Studio 开发 | 指南·API参 | 考 |  |  | 智能体工厂 OpenTre |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| jobKind | Strin g | Query | 否 | notebook | 任务类型。 |
| startTime | Strin g | Query | 否 | 2024-08-02 18:09:14 | 开始时间。 |
| endTime | Strin g | Query | 否 | 2024-08-03 11:19:23 | 结束时间。 |
| entityId | Strin g | Query | 是 | nb- ad56b7f600740042f20b 89a033b**** | 服务POD ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | - | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | [{}] | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -terminals | List | [ "main" ] | 容器名集合。 |
| - containerStatu ses | Array | [{}] | 容器状态信息。 |
| -- volumeMounts | Array | {} | 卷挂载信息列表。 |
| ---mountPath | String | main | 挂载到容器内的路径。 |
| ---name | String | main | 卷名称。 |
| ---readOnly | Boolean | false | 是否只读。 |
| --- recursiveRead Only | String | main | 递归只读设置。 |
| --containerID | String | ontainerd://6c090b 2f69fc*** | 容器ID。 |
| --image | String | cr-ee.registry.cn- wulan-env38- d01.inter.env3*** | 容器镜像。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --imageID | String | cr-ee.registry.cn- wulan-env38- d01.inter.env3*** | 镜像ID。 |
| --name | String | tensorflow | 容器的名称。 |
| --ready | Boolean | true | 容器是否Ready。 |
| --restartCount | Integer | 0 | 重启次数。 |
| --started | Boolean | true | 容器是否启动。 |
| -- allocatedReso urces | Struct | {} | 动态资源分配。 |
| --lastState | Struct | {} | 容器上一次的状态。 |
| ---running | Struct | {} | Running。 |
| ----startedAt | String | 2021-01- 30T12:51:33.028Z | 当前启动时间。 |
| ---terminated | Struct | {} | Terminated信息。 |
| ----containerID | String | containe | 当前容器 ID。 |
| ----exitCode | Integer | ０ | 当前退出码。 |
| ----finishedAt | String | 2021-01- 30T12:52:33.028Z | 当前终止时间。 |
| ----message | String | message | 当前等待消息。 |
| ----reason | String | reason | 当前等待原因。 |
| ----signal | Integer | 20 | 当前接收的信号。 |
| ----startedAt | String | 2021-01- 30T12:51:33.028Z | 当前启动时间。 |
| ---waiting | Struct | {} | 等待信息。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----message | String | message | 当前等待消息。 |
| ----reason | String | reason | 当前等待原因。 |
| --resources | Struct | {} | 资源声明。 |
| ---claims | Array | {} | 资源声明claims |
| ----name | String | test | 资源声明名称。 |
| ---limits | Struct | {} | 资源上限。 |
| ---requests | Struct | {} | 资源请求。 |
| --state | Struct | {} | 容器当前状态。 |
| ---running | Struct | {} | Running。 |
| ----startedAt | String | 2021-01- 30T12:51:33.028Z | 当前启动时间。 |
| ---terminated | Struct | {} | Terminated信息。 |
| ----containerID | String | containe | 当前容器 ID。 |
| ----exitCode | Integer | ０ | 当前退出码。 |
| ----finishedAt | String | 2021-01- 30T12:52:33.028Z | 当前终止时间。 |
| ----message | String | message | 当前等待消息。 |
| ----reason | String | reason | 当前等待原因。 |
| ----signal | Integer | 20 | 当前接收的信号。 |
| ----startedAt | String | 2021-01- 30T12:51:33.028Z | 当前启动时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---waiting | Struct | {} | 等待信息。 |
| ----message | String | message | 当前等待消息。 |
| ----reason | String | reason | 当前等待原因。 |
| -clusterId | String | c039fc341283d426 98d1b9149442e79 4**** | 集群ID。 |
| -gmtCreated | String | 2026-03- 06T03:37:15Z | 创建时间。 |
| - gmtLastCreate d | String | 2026-03- 06T03:37:15Z | 最近一次启动时间。 |
| - gmtLastShutd own | String | 2026-03- 06T03:37:15Z | 最近一次关闭时间。 |
| -hostIp | String | 172.16.101.1**** | HostIP。 |
| -jobId | String | 96fa138a-4b45- 4d6a-b1e9- d10ff676**** | JobID。 |
| -nodeId | String | i- d5s1oveheob0mvli 1**** | 节点ID。 |
| -nodeName | String | i- d5s1oveheob0mvli 1**** | 节点的名称。 |
| -podId | String | os- 9e61451b0333804 f00-555c9b9d58- 2n***** | Pod ID。 |
| -podName | String | os- 9e61451b0333804 f00-555c9b9d58- 2n***** | Pod名称。 |
| -podSpec | String | {\"cpu\":\"16\",\"gp u\":\"- 1\",\"gpuMem\":\"0\ ",\"memory\":\"64\" } | Pod的资源。 |
| -podStatus | String | Running | Pod状态。 |

| I Studio 开发指南· | API参考 |  | 智能体工厂 OpenTre |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -podType | String | online-service- worke | Pod类型。 |
| -podUid | String | 31758df7-13cc- 41d8-afcf- 4cca74d65b6*** | Pod UID。 |
| -resourceId | String | os-9e61451b0*** | 资源ID。 |
| -totalTime | String | 3427 | 总时长。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 资源实例的总数。 |
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 资源实例的页码。 |

**示例**

请求示例

```
&entityId=nb-ad56b7f600740042f20b89a033b****
```

&公共请求参数正常返回示例

#### ListPodsOnNode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 智能体工厂 OpenTrek

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| nodeList | Json | Query | 否 | [{ "nodeName": "i- cupeam6heob*** }] | 节点列表。 |
| pageIndex | Integ er | Query | 否 | 1 | 节点列表的页码。 默认值：1。 |
| pageSize | Integ er | Query | 否 | 10 | 分页查询时设置的每页行数。 默认值：10。 |
| orderByFi eld | Strin g | Query | 否 | gmtCreated | 排序字段。 默认值：gmtCreated。 |
| sortOrder | Strin g | Query | 否 | DESC | 排序顺序。 DESC：降序。 ASC：升序。 默认值：DESC。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | Array | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| -terminals | List | [ "main" ] | 集合名容器。 |
| -clusterId | String | cb09fda0dc2f94a8 397c76638c7ec*** * | 集群ID。 |
| -gmtCreated | String | 2017-11- 27T06:51:26Z | 创建时间。 |
| - gmtLastCreate d | String | 2017-11- 27T06:51:26Z | 最近一次启动时间。 |

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - gmtLastShutd own | String | 2017-11- 27T06:51:26Z | 最近一次停止时间。 |
| -jobId | String | 72dcd26b-f12d- 4c27-b3af- 18f6aed5**** | JobID。 |
| -podId | String | os- 9e61451b0333804 f00-555c9b9d58- 2n*** | PodID。 |
| -podName | String | os- 9e61451b0333804 f00-555c9b9d58- 2n*** | Pod名称。 |
| -podSpec | String | {\"cpu\":\"16\",\"gp u\":\"- 1\",\"gpuMem\":\"0\ ",\"memory\":\"64\" } | Pod的资源。 |
| -podStatus | String | Running | Pod状态。 |
| -podType | String | online-service- worker | Pod类型。 |
| -podUid | String | 31758df7-13cc- 41d8-afcf- 4cca74d6**** | Pod UID。 |
| -resourceId | String | os- 9e61451b033380* ** | 资源ID。 |
| -totalTime | String | 2340 | 总时长。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |
| totalCount | Integer | 100 | 节点的总数。 |

| 智能体工厂 OpenTr | ek |  | AI Studio 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageSize | Integer | 10 | 每页行数。 |
| pageIndex | Integer | 1 | 节点的页码。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "pageIndex":1,
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "pageSize":10,
 "httpCode":200,
 "totalCount":100
}
```

#### GetSysParamValue

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| paramKey | Strin g | Query | 是 | name | 参数名key。 |

**返回数据**

智能体工厂 OpenTrek

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessa ges | List | [] | 动态错误码，按顺序填充到错误码的占位符位置。 |
| data | String | {} | 这是一个数据对象，通常包含API响应中的信息或结果。 |
| success | Boolean | true | 返回状态。 成功：true。 失败：false。 |
| errorCode | String | 500 | 错误码。 |
| errorMessage | String | "" | 错误信息。 |
| httpCode | Integer | 200 | HTTP状态码。 |

**示例**

请求示例

```
&paramKey=name
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "data":"{}",
 "success":true,
 "dynamicMessages":"[]",
 "errorMessage":"\"\"",
 "errorCode":"500",
 "httpCode":200
}
```
