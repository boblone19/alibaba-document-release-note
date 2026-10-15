---
title: "灾备管理平台 备份管理平台ASR-BR开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 362
source_pdf: "22_备份管理平台ASR-BR开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/asr/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 灾备管理平台 备份管理平台ASR-BR开发指南

灾备管理中心说明

## API调用流程说明

**流程图**

**调用步骤**

1. 获取API信息。
2. 获取AccessKey ID和AccessKey Secret，获取方式请参见获取AccessKey。
3. 获取备份管理平台ASR-BR的Endpoint和Region ID，获取方式请参见获取API信息及其Endpoint。
4. 获取备份管理平台ASR-BR的SDK包和SDK核心库，获取方法请参见通过POP网关调用专有云API。
5. 调用备份管理平台ASR-BR的API。

**说明**

| 请参见 | 备份管理平台ASR- |
|---|---|

| BR用户指南 | 中的 |
|---|---|

|  | > |
|---|---|

灾备管理中心

## 准备工作

### 获取AccessKey

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey。推荐使用个人账号 AccessKey调用接口。

**说明**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**获取个人账号AccessKey时，请确保登录的用户具备组织备份管理员角**

**色，否则可能导致接口调用失败。**

**获取个人账号AccessKey**

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

**重要**

AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
灾备管理中心
3. 在左侧导航栏中，选择**资源管理**>**组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取API信息及其Endpoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见ASR- BR的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** **> API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择**灾备管理平台**。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取ASR-BR的POP Endpoint和RegionId等接口信息。
灾备管理中心

### 通过POP网关调用专有云API

通过POP Java SDK访问产品域名，需要了解该产品调用方式（RPC或ROA）。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！ RPC调用，示例接口信息：产品（ASR-BR）、接口（CreateAdbBackupPlan）、版本（2021-10- 15）。 调用示例如下： 灾备管理中心

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`//` 您的地域`ID` `"<your-region<YOUR-REGION-ID> //` 从环境变量获取`RAM`账号的`AccessKey ID`

```
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
```

`//` 从环境变量获取`RAM`账号的`AccessKey ID`

```
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
        CommonRequest request = new CommonRequest();
        request.setSysDomain("asrbr.aliyuncs.com");
        request.setSysVersion("2021-10-15");
        request.setSysAction("CreateAdbBackupPlan");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClientException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

ROA调用，示例接口信息：产品（ASR-BR）接口（CreateAdbBackupPlan）版本（2021-10-15）。 调用示例如下： 灾备管理中心

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`//` 您的地域`ID` `"<your-region<YOUR-REGION-ID> //` 从环境变量获取`RAM`账号的`AccessKey ID`

```
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
```

`//` 从环境变量获取`RAM`账号的`AccessKey ID`

```
                System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"));
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
        CommonRequest request = new CommonRequest();
        request.setSysDomain("asrbr.aliyuncs.com");
        request.setSysVersion("2021-10-15");
        request.setSysUriPattern("/clusters");
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (ClientException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
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

灾备管理中心用示例

## Java SDK调用示例

### 安装Java SDK

**环境准备**

阿里云专有云Java SDK需要使用1.8及后续版本的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 调用Java SDK必须安装SDK核心库以及ASR-BR的SDK包。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为1.0.0。 以下为Java pom文件设置示例。

```xml
<dependencies>
```

<!--必须要的依赖`-->`

```xml
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-asrbr</artifactId>
        <version>1.0.0</version>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>aliyun-java-sdk-core</artifactId>
        <version>4.6.0</version>
    </dependency>
</dependencies>
```

### 设置身份验证凭证

使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 Java SDK支持通过AccessKey进行身份验证，获取AccessKey ID和AccessKey Secret的方法请参见获取AccessKey，获取Endpoint的方法请参见获取Endpoint，获取Region ID的方法请参见获取Region ID。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**重要**

请确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。 灾备管理中心用示例 `//`配置请求`Endpoint`

```
DefaultProfile.addEndpoint(
```

`"<RegionId>", //`请替换为您实际的地域`ID` `"<Endpoint>" //`请替换为您实际的产品请求域名

```
);
```

`//`配置身份验证凭证

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` `"<yourAccessKeySecret>" //` 请替换为您实际的`AccessKey Secret`

```
);
```

**说明**

以上代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 均为可变参
```

数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### 发起调用请求

本文介绍如何使用Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
DefaultAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为${apiName}Request，其中**${apiName}**为API名称，例

```
CreateEcsSnapshotBackupPlanRequest request = new CreateEcsSnapshotBackupPlanRequest();
```

3. 发起调用并处理应答。
`//` 发起请求，查看结果

```
AcsResponse response = client.getAcsResponse(request);
```

**完整调用示例**

以下代码为备份管理平台ASR-BR的 `CreateEcsSnapshotBackupPlan` 接口调用示例。

```java
import com.alibaba.fastjson.JSON; import com.aliyuncs.AcsResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.asrbr.model.v20211015.*; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.profile.DefaultProfile;
```

灾备管理中心用示例

```java
import java.util.ArrayList; import java.util.HashMap; import java.util.List; import java.util.Map;
    public static void main(String[] args) throws ClientException {
```

`//`配置请求`Endpoint`

```
        DefaultProfile.addEndpoint(
```

`"<RegionId>", //`请替换为您实际的地域`ID` `"<Endpoint>" //`请替换为您实际的产品请求域名

```
        );
```

`//`配置身份验证凭证

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKeySecret`

```
        );
```

`//`构建调用`Client`

```
        DefaultAcsClient client = new DefaultAcsClient(profile);
```

`//`创建`ECS`整机备份计划 `//`构造请求参数

```
        CreateEcsSnapshotBackupPlanRequest request = new
CreateEcsSnapshotBackupPlanRequest() ;
        request.setClientToken("12asd-dfsdfest1201123123-100aa0111");
        request.setPlanName("udmecs-backup");
```

`//`构造备份实例

```
        Map<Object,Object> backupInstance = new HashMap<>();
        backupInstance.put("instanceId","i-q1f0********89b5");
        request.setBackupInstance(backupInstance);
```

`//`构造备份策略

```
        List<Integer> preferredBackupPeriodList = new ArrayList<>();
        preferredBackupPeriodList.add(2);
        Map<Object,Object> backupPolicy = new HashMap<>();
        backupPolicy.put("preferredBackupPeriod",preferredBackupPeriodList);
        backupPolicy.put("preferredBackupTime",System.currentTimeMillis());
        backupPolicy.put("vaultId","c59f9c6b-********9a686a26");
        backupPolicy.put("backupRetentionPeriod",8);
        List<Integer> preferredBackupPeriodFullList = new ArrayList<>();
        preferredBackupPeriodFullList.add(7);
        backupPolicy.put("preferredBackupPeriodFull",preferredBackupPeriodFullList);
        backupPolicy.put("preferredCycleType","BY_DAY");
        request.setBackupPolicy(backupPolicy);
```

`//`调用`API`

```
        AcsResponse response = client.getAcsResponse(request);
    }
}
```

灾备管理中心用示例

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

灾备管理中心

## API参考

### 初始化云实例信息

#### InitCloudInfo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Quer y | 否 | 2 | 组织ID。 |
| ResourceG roupId | Integ er | Quer y | 否 | 32 | 资源集ID |
| ClientToke n | Strin g | Quer y | 是 | 123e4567********554400 00 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII字符，且不能超过64个字符。 |
| AccessKey | Strin g | Body | 是 | wsdf2321df****** | 组织AccessKey。 |
| AccessSec ret | Strin g | Body | 是 | wuqyewyriuiwe***** | 组织AccessSecret |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |

灾备管理中心

| errorMessage | String | InternalFailure | 错误提示信息。 |
|---|---|---|---|
| errorCode | String | 500 | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| cloudInfo | Struct |  | 云实例信息。 |
| -cloudId | String | d202309c-0c20- 44e2-9e02- bacf****** | 云实例ID。 |

**示例**

请求示例

```
&ClientToken=123e4567********55440000 &AccessKey=wsdf2321df****** &AccessSecret=wuqyewyriuiwe*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "CloudInfo":{
  "CloudId":"d202309c-0c20-44e2-9e02-bacf******"
 },
 "ErrorCode":"500",
 "ErrorMessage":"InternalFailure",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <CloudInfo>
 <CloudId>d202309c-0c20-44e2-9e02-bacf******</CloudId>
</CloudInfo> <ErrorCode>500</ErrorCode> <ErrorMessage>InternalFailure</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

### 备份仓库

#### CreateBackupVault

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1234 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 16253egdcf | 资源集ID |
| ClientToke n | Strin g | Body | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| VaultNam e | Strin g | Body | 是 | asrbr vault _ | 备份仓库名称。 |
| InstanceT ype | Strin g | Body | 是 | OSS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |
| StorageSp ace | Long | Body | 是 | 2048 | 存储空间大小，单位： byte。 |
| StorageId | Strin g | Body | 是 | 123e4567-e89b-12d3- a456-4266********* | 存储池ID。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| UseHttps | Integ er | Body | 否 | 1 | 是否是https仓库。 |
| VaultType | Strin g | Body | 否 | OSS | 存储类型，支持 OSS/MINIOSS/CDS OSS/ _ PANGUSTOR/SDS。 默认：OSS。 |
| Descriptio n | Strin g | Body | 否 | test | 仓库描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 32 | 接口耗时，单位毫秒（ms）。 |
| backupVaultIn ner | Struct |  | 备份仓库信息。 |
| -products | String | OSS | 支持存储的备份产品。 |
| -vaultId | String | efa6d59b- 83492342399***** ****** | 仓库ID。 |
| -vaultName | String | asrbr vault _ | 备份仓库名称。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -status | String | success | 仓库状态。 creating：创建中 success：成功 failed：失败 unavailable：不可用 |
| -vaultType | String | OSS | 存储类型，支持 OSS/MINIOSS/CDS OSS/PANGUSTOR/SDS _ 。 默认：OSS。 |
| -storageId | String | efa6d59b-8288- 48c2-8ef5- 46*********** | 存储池ID。 |
| -storageName | String | storage pool | 存储池名称。 |
| -storageSpace | Long | 2048 | 存储空间，单位：byte。 |
| -ossEndpoint | String | oss-cn- hangzhou********* | 存储endpoint。 |
| -organizationId | Integer | 2 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -creator | String | ascm-org- 16678*********** | 创建人。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |

**示例**

请求示例

```
&ClientToken=123e4567********55440000 &StorageId=123e4567-e89b-12d3-a456-4266*********
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"success",
  "OrganizationName":"test",
  "Products":"OSS",
  "VaultName":"asrbr_vault",
  "OrganizationId":2,
  "Creator":"ascm-org-16678***********",
  "VaultId":"efa6d59b-83492342399***********",
  "StorageId":"efa6d59b-8288-48c2-8ef5-46***********",
  "VaultType":"OSS",
  "OssEndpoint":"oss-cn-hangzhou*********",
  "StorageName":"storage pool",
  "StorageSpace":"2048",
  "Ctime":1677825909000
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":32,
 "Success":true
}
```

`XML` 格式

```xml
 <Status>success</Status>
 <OrganizationName>test</OrganizationName>
 <Products>OSS</Products>
 <OrganizationId>2</OrganizationId>
 <Creator>ascm-org-16678***********</Creator>
 <VaultId>efa6d59b-83492342399***********</VaultId>
 <StorageId>efa6d59b-8288-48c2-8ef5-46***********</StorageId>
 <OssEndpoint>oss-cn-hangzhou*********</OssEndpoint>
 <Ctime>1677825909000</Ctime>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>32</Cost> <Success>true</Success>
```

#### DescribeVaultUseageDetail

灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Strin g | Query | 否 | 2 | 组织ID。 |
| VaultNam e | Strin g | Query | 否 | backup-vault | 仓库名称。 |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 2 | 每页返回的数据个数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  | 返回数据。 |
| -VaultName | String | backup-vault | 仓库名称。 |
| - OrganizationId | Integer | 4 | 组织ID。 |
| - OrganizationN ame | String | current-org | 组织名称。 |
| - UsedStorageC apacity | Long | 204800000 | 已使用存储。单位：byte。 |
| - AvailableStora geCapacity | Long | 102400000 | 可用存储。单位：byte。 |
| - ParentOrganiz ationId | Integer | 2 | 上级组织ID。 |
| - ParentOrganiz ationName | String | backup-test | 上级组织名称。 |
| - RootOrganizati onId | Integer | 1 | 根组织ID。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| Success | Boolean | true | 本次请求是否成功。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| Message | String | success | 错误提示信息。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页返回的数据个数。 |
| TotalSize | Integer | 1 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVaultUseageDetail
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Message":"success",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "OrganizationName":"current-org",
  "RootOrganizationId":1,
  "UsedStorageCapacity":204800000,
  "ParentOrganizationId":2,
  "VaultName":"backup-vault",
  "ParentOrganizationName":"backup-test",
  "OrganizationId":4,
 },
 "TotalSize":1,
 "Code":"200",
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Message>success</Message> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <OrganizationName>current-org</OrganizationName>
 <RootOrganizationId>1</RootOrganizationId>
 <UsedStorageCapacity>204800000</UsedStorageCapacity>
 <ParentOrganizationId>2</ParentOrganizationId>
 <ParentOrganizationName>backup-test</ParentOrganizationName>
 <OrganizationId>4</OrganizationId>
 <AvailableStorageCapacity>102400000</AvailableStorageCapacity>
</Data> <TotalSize>1</TotalSize> <Code>200</Code> <Success>true</Success>
```

#### DescribeBackupVault

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 21 | 资源集ID |
| VaultId | Strin g | Query | 是 | c59f9c6b-effd-4d5c- 841b-c14d9**** | 备份仓库ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | Not Found Backup Vault for current operate. | 错误提示信息。 |
| errorCode | String | BackupVaultNotFo und | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupVaultIn ner | Struct | - | 备份仓库信息。 |
| -products | List | ["OSS", "ECS", "VMWARE", "ADB"] | 支持备份产品。 |
| -vaultId | String | c59f9c6b-effd- 4d5c-841b- c14d9**** | 备份仓库ID。 |
| -vaultName | String | backup-vault | 备份仓库名称。 |
| -status | String | success | 仓库状态。 creating：创建中 success：成功 failed：失败 unavailable：不可用 |
| -vaultType | String | OSS | 存储类型，支持OSS/MiniOSS。 默认：OSS。 |
| -storageId | String | efa6d59b-8288- 48c2-8ef5- 46*********** | 存储池ID。 |
| -storageName | String | storage pool | 存储池名称。 |
| -storageSpace | Long | 20 | 存储空间，单位：（TB）。 |
| -ossEndpoint | String | oss-cn- hangzhou********* | 存储endpoint。 |
| -organizationId | Integer | 2 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -creator | String | ascm-org- 16678*********** | 创建人。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -usedCapacity | Long | 612 | 备份仓库使用容量 |
| - storageLocatio n | String | LOCAL | 存储池存储位置，默认：REMOTE。 LOCAL：本地 REMOTE：异地 |
| - replicationVaul tNum | Integer | 5 | 镜像仓库数量 |
| - usedCapacityP ercentage | String | 0.0000% | 仓库使用占比 |
| - storagePoolCa pacity | Long | 10 | 存储池容量 |
| - storagePoolUs edCapacity | Long | 612 | 存储池使用容量 |
| - storagePoolPer centage | String | 0.0000% | 存储池使用占比 |
| -lastModifier | String | admin | 最后一次修改用户 |
| -description | String | test | 描述 |
| -useHttps | Integer | 1 | 是否使用https |
| -mtime | Long | 1705403404000 | 修改时间 |
| -vaultTag | String | BACKUP | 备份仓库标签。 BACKUP：仅用于备份 ARCHIVE: 用于备份+归档 RESTORE: 用于归档恢复 |
| -immutable | Boolean | true | 是否开启备份锁定。true：开启备份锁定； false：未开启备份锁定。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - immutableRet ention | Integer | 10 | 备份锁定保存时长。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupVault
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
  "ossEndpoint":"oss-cn-hangzhou*********",
  "storageLocation":"LOCAL",
  "lastModifier":"admin",
  "description":"test",
  "mtime":1705403404000,
  "replicationVaultNum":5,
  "products":"[\"OSS\", \"ECS\", \"VMWARE\", \"ADB\"]",
  "storageName":"storage pool",
  "organizationId":2,
  "storagePoolCapacity":10,
  "storageSpace":20,
  "ctime":1677825909000,
  "storagePoolUsedCapacity":612,
  "vaultTag":"BACKUP",
  "storageId":"efa6d59b-8288-48c2-8ef5-46***********",
  "vaultType":"OSS",
  "creator":"ascm-org-16678***********",
  "organizationName":"test",
  "usedCapacityPercentage":"0.0000%",
  "vaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "usedCapacity":612,
  "immutableRetention":10,
  "storagePoolPercentage":"0.0000%",
  "immutable":true,
  "vaultName":"backup-vault",
  "useHttps":1,
  "status":"success"
 },
 "errorMessage":"Not Found Backup Vault for current operate.",
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success>
 <ossEndpoint>oss-cn-hangzhou*********</ossEndpoint>
 <lastModifier>admin</lastModifier>
 <description>test</description>
 <mtime>1705403404000</mtime>
 <replicationVaultNum>5</replicationVaultNum>
 <products>[&quot;OSS&quot;, &quot;ECS&quot;, &quot;VMWARE&quot;, &quot;ADB&quot;]</pro
ducts>
 <organizationId>2</organizationId>
 <storagePoolCapacity>10</storagePoolCapacity>
 <ctime>1677825909000</ctime>
 <storagePoolUsedCapacity>612</storagePoolUsedCapacity>
 <storageId>efa6d59b-8288-48c2-8ef5-46***********</storageId>
 <creator>ascm-org-16678***********</creator>
 <organizationName>test</organizationName>
 <usedCapacityPercentage>0.0000%</usedCapacityPercentage>
 <vaultId>c59f9c6b-effd-4d5c-841b-c14d9****</vaultId>
 <usedCapacity>612</usedCapacity>
 <immutableRetention>10</immutableRetention>
 <storagePoolPercentage>0.0000%</storagePoolPercentage>
 <immutable>true</immutable>
 <useHttps>1</useHttps>
 <status>success</status>
<errorMessage>Not Found Backup Vault for current operate.</errorMessage> <errorCode>BackupVaultNotFound</errorCode>
```

#### DescribeBackupVaultList

查看备份仓库列表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| InstanceT ype | Strin g | Query | 否 | OSS | 实例类型。 OSS、ECS、 NAS、ADB、RDS、 DRDS、ODPS、 ES（ElasticSearch）及 VMware。 |
| Status | Strin g | Query | 否 | success | 仓库状态。 creating：创建中。 success：成功。 failed：失败。 unavailable：不可用。 |
| StorageLo cation | Strin g | Query | 否 | REMOTE | 存储池存储位置， 默认： REMOTE LOCAL：本地 REMOTE：异地 |
| VaultType | Strin g | Query | 否 | OSS | 仓库类型： OSS MINIOSS CDS-OSS SDS PANGUSTOR |
| VaultNam e | Strin g | Query | 否 | test | 仓库名称 |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 分页数据数。 |
| VaultTag | Strin g | Query | 否 | BACKUP | 备份仓库标签。 BACKUP：仅用于备份 ARCHIVE: 用于备份+归档 RESTORE: 用于归档恢复 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | success | 返回数据。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -products | List | [ "OSS", "ECS", "VMWARE", "ADB" ] | 支持备份产品。 |
| -vaultId | String | c59f9c6b-effd- 4d5c-841b- c14d9**** | 备份仓库ID。 |
| -vaultName | String | backup-vault | 备份仓库名称。 |
| -status | String | success | 仓库状态。 creating：创建中。 success：成功。 failed：失败。 unavailable：不可用。 |
| -errorMessage | String | failed | 错误提示信息。 |
| -vaultType | String | OSS | 存储类型，支持 OSS/MINIOSS/PANGUSTOR/CDS-OSS/SDS。 默认：OSS。 |
| -storageId | String | efa6d59b-8288- 48c2-8ef5- 46*********** | 存储池ID。 |
| -storageName | String | storage pool | 存储池名称。 |
| -storageSpace | String | 200 | 存储空间，单位：（TB）。 |
| -authority | String | newratings.default. svc.cluster.local | 权限。 |
| -ossEndpoint | String | oss-cn- hangzhou********* | 存储endpont。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -creator | String | ascm-org- 16678*********** | 创建人。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -usedCapacity | String | 1024 | 使用空间，单位：byte。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - storageLocatio n | String | local | 存储位置 |
| -bucketName | String | lengjuetest | 备份仓库名称 |
| - usedCapacityP ercentage | String | 32 | 仓库使用占比 |
| - storagePoolPer centage | String | 55 | 存储池使用占比 |
| -ddrType | String | HBR | 数据转储类型： GULLTOPPR HBR DEDUPLICATION |
| - replicationVaul tNum | Integer | 56 | 镜像仓库数量 |
| -description | String | test | 存储池描述。 |
| -vaultTag | String | BACKUP | 备份仓库标签。 BACKUP：仅用于备份 ARCHIVE: 用于备份+归档 RESTORE: 用于归档恢复 |
| -immutable | Boolean | true | 是否开启备份锁定。 true：开启备份锁定 false：未开启备份锁定。 |
| - immutableRet ention | Integer | 30 | 备份锁定时长。 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found Backup Vault for current operate. | 错误提示信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | BackupVaultNotFo und | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 分页数据数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupVaultList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "totalSize":50,
 "data":[
  {
   "bucketName":"lengjuetest",
   "ossEndpoint":"oss-cn-hangzhou*********",
   "storageLocation":"local",
   "description":"test",
   "replicationVaultNum":56,
   "ddrType":"HBR",
   "products":"[            \"OSS\",            \"ECS\",            \"VMWARE\",
\"ADB\"]",
   "storageName":"storage pool",
   "organizationId":12,
   "storageSpace":"200",
   "ctime":1677825909000,
   "vaultTag":"BACKUP",
   "storageId":"efa6d59b-8288-48c2-8ef5-46***********",
   "vaultType":"OSS",
   "creator":"ascm-org-16678***********",
   "organizationName":"test",
   "usedCapacityPercentage":"32",
   "vaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
   "usedCapacity":"1024",
   "immutableRetention":30,
   "errorMessage":"failed",
   "storagePoolPercentage":"55",
   "immutable":true,
   "vaultName":"backup-vault",
   "authority":"newratings.default.svc.cluster.local",
   "status":"success"
  }
```

`],`

```json
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"Not Found Backup Vault for current operate.",
 "errorCode":"BackupVaultNotFound",
 "pageSize":10,
 "pageNum":1
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <totalSize>50</totalSize> <data>
 <bucketName>lengjuetest</bucketName>
 <ossEndpoint>oss-cn-hangzhou*********</ossEndpoint>
 <description>test</description>
 <replicationVaultNum>56</replicationVaultNum>
 <ddrType>HBR</ddrType>
 <products>[
            &quot;OSS&quot;,
            &quot;ECS&quot;,
            &quot;VMWARE&quot;,
            &quot;ADB&quot;
]</products>
  <organizationId>12</organizationId>
  <ctime>1677825909000</ctime>
  <storageId>efa6d59b-8288-48c2-8ef5-46***********</storageId>
  <creator>ascm-org-16678***********</creator>
  <organizationName>test</organizationName>
  <usedCapacityPercentage>32</usedCapacityPercentage>
  <vaultId>c59f9c6b-effd-4d5c-841b-c14d9****</vaultId>
  <usedCapacity>1024</usedCapacity>
  <immutableRetention>30</immutableRetention>
  <errorMessage>failed</errorMessage>
  <storagePoolPercentage>55</storagePoolPercentage>
  <immutable>true</immutable>
  <authority>newratings.default.svc.cluster.local</authority>
  <status>success</status>
 </data>
 <requestId>C8B26B44-0189-443E-9816-*******</requestId>
 <success>true</success>
 <errorMessage>Not Found Backup Vault for current operate.</errorMessage>
 <errorCode>BackupVaultNotFound</errorCode>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
```

### 备份计划

#### 安装ECS客户端

##### InstallEcsClient

灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| InstanceId | Strin g | Query | 是 | i-rtstedsfsd******** | 实例ID。 |
| InstallPath | Strin g | Query | 否 | /root/ | 安装路径（绝对路径），建议安装在数据盘路径。 |
| MaxCpuC ore | Integ er | Query | 否 | 1 | 最大使用CPU， 默认：1。 |
| MaxWorke r | Integ er | Query | 否 | 10 | 最大工作线程， 默认： 10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | InternalFailure | 错误提示信息。 |
| errorCode | String | 500 | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
|---|---|---|---|
| data | Struct |  | 客户端信息。 |
| -errorCode | String | 500 | 错误码 |
| -errorMessage | String | false | 接口返回错误信息 |
| -exitCode | String | 400 | 退出code |
| -invokeId | String | t-rg43883drsg8ow | 调用ID |
| -output | String | success | 测试结果输出 |
| -status | String | RUNNING | 客户端状态。 |

**示例**

请求示例

```
&ClientToken=123e4567********55440000
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "data":{
  "invokeId":"t-rg43883drsg8ow",
  "output":"success",
  "errorMessage":"false",
  "errorCode":"500",
  "exitCode":"400",
  "status":"RUNNING"
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"InternalFailure",
 "errorCode":"500"
}
```

`XML` 格式

```xml
<code>200</code> <cost>20</cost> <data>
 <invokeId>t-rg43883drsg8ow</invokeId>
 <output>success</output>
 <errorMessage>false</errorMessage>
 <errorCode>500</errorCode>
 <exitCode>400</exitCode>
 <status>RUNNING</status>
</data> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>InternalFailure</errorMessage> <errorCode>500</errorCode>
```

#### 创建备份计划

##### CreateAdbBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | ADB备份计划 | 备份计划名称。 |
| Descriptio n | Strin g | Body | 否 | ADB备份计划 | 描述 |
| BackupIns tance | Json | Body | 是 | {"instanceId": "am- c3kn4r00sh*****" } | 备份实例信息。 instanceId：备份实例ID。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ "Thursday","Sunday" ], "preferredBackupTime": "19:00Z-20:00Z", "backupRetentionPeriod ": 7, "preferredCycleType": "BY WEEK", "vaultId": _ "47c5862e-978b- *******" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值 ["Monday"：星期一,"Tuesday"：星期二，"Wednesday"：星期三，"Thursday"：星期四，"Friday"：星期五，"Saturday"：星期六，"Sunday"：星期日]。 preferredBackupTime ：备份执行时间，UTC时间段。 backupRetentionPerio d：备份保存时长，单位: 天。 preferredCycleType： 备份周期类型。 vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 32 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | adb-test | 备份计划名称。 |
| -status | String | CREATING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String | ECS FILE _ | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | ADB | 实例类型。 OSS、ECS、NAS、ADB、RDS、 PolarDB-X、MaxCompute、Elasticsearch及 VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -lastResult | String | NOT RUN _ | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |
| -creator | String | ascm-org-**** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateAdbBackupPlan &ClientToken=123e4567********55440000
```

`&PlanName=ADB`备份计划

```json
&BackupInstance={"instanceId": "am-c3kn4r00sh*****" } &BackupPolicy=[ { "preferredBackupPeriod": [ "Thursday","Sunday" ], "preferredBackupTime": "19:00Z-20:00Z", "backupRetentionPeriod": 7, "preferredCycleType": "BY_WEEK", "vaultId": "47c5862e-978b-*******" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":32,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"failed",
 "errorCode":"403",
  "creator":"ascm-org-****",
  "organizationName":"test",
  "lastResult":"NOT_RUN",
  "instanceType":"ADB",
  "regionName":"cn-hangzhou*****",
  "nextBackupTime":1677825909000,
  "creatorId":5612,
  "planName":"adb-test",
  "mtime":1677825909000,
  "backupType":"ECS_FILE",
  "organizationId":12,
  "regionId":"cn-hangzhou******",
  "ctime":1677825909000,
  "planId":"108e46be-c321-4694-9c2d-b478b*******",
  "status":"CREATING"
 }
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>32</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>failed</errorMessage> <errorCode>403</errorCode>
 <creator>ascm-org-****</creator>
 <organizationName>test</organizationName>
 <lastResult>NOT_RUN</lastResult>
 <regionName>cn-hangzhou*****</regionName>
 <nextBackupTime>1677825909000</nextBackupTime>
 <creatorId>5612</creatorId>
 <planName>adb-test</planName>
 <mtime>1677825909000</mtime>
 <organizationId>12</organizationId>
 <regionId>cn-hangzhou******</regionId>
 <ctime>1677825909000</ctime>
 <planId>108e46be-c321-4694-9c2d-b478b*******</planId>
 <status>CREATING</status>
```

##### CreateDrdsBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12233 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 34455 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | PolarDB-X备份计划 | 备份计划名称。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Descriptio n | Strin g | Body | 否 | DRDS备份计划 | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "drdsusrz38g****", } | 备份实例信息。 instanceId：备份实例ID。 |
| BackupPol icy | Json | Body | 是 | [ { "backupMode":"CONSIST ENT", "preferredBackupPeriod" : [ "Monday", "Friday" ], "preferredBackupTime": "19:00Z-20:00Z" , "backupRetentionPeriod ": 7, "preferredCycleType": "BY WEEK", "vaultId": _ "47c5862e-978b-48fc- a********" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值 ["Monday"：星期一,"Tuesday"：星期二，"Wednesday"：星期三，"Thursday"：星期四，"Friday"：星期五，"Saturday"：星期六，"Sunday"：星期日]。 preferredBackupTime ：备份执行时间，UTC时间段。 backupRetentionPerio d：备份保存时长，单位为天。 preferredCycleType： 备份周期类型。 vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | PolarDB-X备份计划 | 备份计划名称。 |
| -status | String | CREATING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | PolarDB-X | 实例类型。包含OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | NOT RUN _ | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-**** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateDrdsBackupPlan &ClientToken=123e4567********55440000
```

`&PlanName=PolarDB-X`备份计划

```json
        "instanceId": "drdsusrz38g****",
} &BackupPolicy=[ { "backupMode":"CONSISTENT", "preferredBackupPeriod": [ "Monday", "Frid ay" ], "preferredBackupTime":"19:00Z-20:00Z" , "backupRetentionPeriod": 7, "preferredCycleType": "BY_WEEK", "vaultId": "47c5862e-978b-48fc-a********" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"CREATING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-****",
  "PlanName":"PolarDB-X备份计划",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"NOT_RUN",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>CREATING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-****</Creator>
 <PlanName>PolarDB-X备份计划</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>NOT_RUN</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed </ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateEsBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanName | Strin g | Query | 是 | Elasticsearch备份 | 备份计划名称。 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "source- 6-8-*********", "userName":"admin", "passWord":"*******" } | 备份实例信息。 instanceId：备份实例 ID。 userName： Elasticsearch访问用户名称。 passWord： Elasticsearch访问密码。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 1 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a****", "preferredBackupPeriod Full": [ 3 ], vaultId:"213aawwwq"} ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 preferredBackupPerio dFull：全量备份周期。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | Elasticsearch备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | Elasticsearch | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateEsBackupPlan &ClientToken=123e4567********55440000 &PlanName=Elasticsearch备份
        "instanceId": "source-6-8-*********",
        "userName":"admin",
        "passWord":"*******"
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ 1 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a****", "preferredBackupPeriodFull": [ 3 ], vaultId:"213aawwwq"} ]
```

&公共请求参数正常返回示例灾备管理中心 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
  "Status":"RUNNING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
  "PlanName":"Elasticsearch备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <PlanName>Elasticsearch备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
 <InstanceType>Elasticsearch</InstanceType>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateEcsBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1234 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2234 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | ECS文件备份计划 | 备份计划名称。 |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | ECS备份计划 | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "i- nn901lg2s5pb*****", "prefix": "/", "excludeFileList": [ "/home" ], "speedLimit": "6:12:5120\|12:18:2560" } | 备份实例信息。 instanceId：实例ID。 prefix：备份目录。 excludeFileList：排除文件列表。 speedLimit：实例备份限速。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 1 ], "preferredBackupTime": 1666062748312, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a831***" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | ECS文件备份计划 | 备份计划名称。 |
| -status | String | CREATING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String | ECS FILE _ | 备份类型。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | ECS | 实例类型。包含OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | NOT RUN _ | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-**** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateEcsBackupPlan &ClientToken=123e4567********55440000
```

`&PlanName=ECS`文件备份计划

```json
        "instanceId": "i-nn901lg2s5pb*****",
        "prefix": "/",
        "excludeFileList": [
            "/home"
```

`],`

```json
        "speedLimit": "6:12:5120|12:18:2560"
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ 1 ], "preferredBackupTime": 1666062748312, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a831***" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"CREATING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-****",
```

`"PlanName":"ECS`文件备份计划`",`

```json
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"ECS_FILE",
  "LastResult":"NOT_RUN",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>CREATING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-****</Creator>
```

`<PlanName>ECS`文件备份计划`</PlanName>`

```xml
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>NOT_RUN</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateEcsSnapshotBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 13 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | ECS快照备份 | 备份计划名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | ECS快照备份任务 | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "i- nn901lg2uex8******", } | 备份实例信息。 instanceId：实例ID。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a****" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为3表示每三天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否立即运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | ECS快照备份 | 备份计划名称。 |
| -status | String | CREATING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String | ECS DISK _ | 备份类型。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | ECS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 3 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateEcsSnapshotBackupPlan &ClientToken=123e4567********55440000
```

`&PlanName=ECS`快照备份

```json
        "instanceId": "i-nn901lg2uex8******",
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a****" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"CREATING",
  "OrganizationName":"test",
  "ResourceGroupId":3,
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
```

`"PlanName":"ECS`快照备份`",`

```json
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"ECS_DISK",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
  "InstanceType":"ECS",
  "ResourceGroupName":"ResourceSet(test)"
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>CREATING</Status>
 <OrganizationName>test</OrganizationName>
 <ResourceGroupId>3</ResourceGroupId>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <PlanName>ECS快照备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
 <ResourceGroupName>ResourceSet(test)</ResourceGroupName>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateNasBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 23 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanName | Strin g | Query | 是 | NAS备份 | 备份计划名称。 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "171a64******", "prefix": "/" } | 备份实例信息。 instanceId：实例ID。 prefix：备份目录。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a831*****" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | NAS备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | NAS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -vaultId | String | c59f9c6b-effd- 4d5c-841b- c14d9**** | 备份仓库ID。 |
| -vaultName | String | backup-vault | 备份仓库名称。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateNasBackupPlan &ClientToken=123e4567********55440000 &PlanName=NAS备份
        "instanceId": "171a64******",
        "prefix": "/"
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a831*****" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"RUNNING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
  "PlanName":"NAS备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <PlanName>NAS备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateOdpsBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 31 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | MaxCompute备份 | 备份计划名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "bigdata****", "specifyProject":"test", "dataTypeVersion":"2.0" } | 备份实例信息。 instanceId：实例ID。 specifyProject：运行项目。 dataTypeVersion：运行项目数据类型。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a831*****" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为3表示每三天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | MaxCompute备份 | 备份计划名称。 |
| -status | String | CREATING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | MaxCompute | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateOdpsBackupPlan &ClientToken=123e4567********55440000 &PlanName=MaxCompute备份
        "instanceId": "bigdata****",
        "specifyProject":"test",
        "dataTypeVersion":"2.0"
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ 3 ], "preferredBackupTime": 1666072782336, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a831*****" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"CREATING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
  "PlanName":"MaxCompute备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>CREATING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <PlanName>MaxCompute备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateOssBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 41 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | OSS备份 | 备份计划名称。 |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "bucket- *****", "prefix": "/test" } | 备份实例信息。 instanceId：实例ID。 prefix：备份目录。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ 1 ], "preferredBackupTime": 1666169989013, "backupRetentionPeriod ": 7, "preferredCycleType": "BY DAY", "vaultId": _ "47c5862e-978b-48fc- a831*******" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | OSS备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | OSS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateOssBackupPlan &ClientToken=123e4567********55440000 &PlanName=OSS备份
        "instanceId": "bucket-*****",
        "prefix": "/test"
    }
{ "preferredBackupPeriod": [ 1 ], "preferredBackupTime": 1666169989013, "backupRetentionPeriod": 7, "preferredCycleType": "BY_DAY", "vaultId": "47c5862e-978b-4 8fc-a831*******" }
```

] &公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"RUNNING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-********",
  "PlanName":"OSS备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-********</Creator>
 <PlanName>OSS备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateRdsBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 31 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | RDS备份 | 备份计划名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "instanceId": "rm- c3kkw34*********", } | 备份实例信息。 instanceId：实例ID。 |
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" : [ "Thursday","Sunday" ], "preferredBackupTime": "19:00Z-20:00Z", "backupRetentionPeriod ": 7, "preferredCycleType": "BY WEEK", "vaultId": _ "df4d9ba9-9a15-4c96- 981b-d2******" } ] | 备份策略。 preferredBackupPerio d：备份周期，取值 ["Monday"：星期一,"Tuesday"：星期二，"Wednesday"：星期三，"Thursday"：星期四，"Friday"：星期五，"Saturday"：星期六，"Sunday"：星期日]。 preferredBackupTime ：备份执行时间，UTC时间。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY WEEK为按周执行。 _ vaultId：备份仓库ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | RDS备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -instanceType | String | RDS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateRdsBackupPlan &ClientToken=123e4567********55440000 &PlanName=RDS备份
        "instanceId": "rm-c3kkw34*********",
    }
&BackupPolicy=[ { "preferredBackupPeriod": [ "Thursday","Sunday" ], "preferredBackupTime": "19:00Z-20:00Z", "backupRetentionPeriod": 7, "preferredCycleType": "BY_WEEK", "vaultId": "df4d9ba9-9a15-4c96-981b-d2******" } ]
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"RUNNING",
  "OrganizationName":"test",
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-********",
  "PlanName":"RDS备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-********</Creator>
 <PlanName>RDS备份</PlanName>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### 管理备份计划

##### DeleteBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| PlanId | Strin g | Query | 是 | 108e46be-c321-4694- 9c2d-b478b******* | 备份计划ID。 |
| InstanceId | Strin g | Query | 否 | rm-ss23d7fgd******** | 实例ID。 |

灾备管理中心

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| data | Struct |  | 返回结果。 |
| -result | Boolean | true | 删除备份计划结果。 true：成功 false：失败 |

**示例**

请求示例

```
&PlanId=108e46be-c321-4694-9c2d-b478b*******
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":{
  "Result":true
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <Result>true</Result>
</Data> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeBackupPlanList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 21 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 22 | 资源集ID |
| PlanId | Strin g | Query | 否 | 108e46be-c321-4694- 9c2d-b478b******* | 备份计划ID。 |
| InstanceT ype | Strin g | Query | 否 | OSS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 否 | oss-test | 实例ID |
| InstanceN ame | Strin g | Query | 否 | ASDE | 实例名称 |
| PlanName | Strin g | Query | 否 | OSS备份 | 备份计划名称。 |
| VaultId | Strin g | Query | 否 | qwrr3 | 仓库ID |
| Status | Strin g | Query | 否 | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 每页返回的数据个数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回结果。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划信息。 |
| -planName | String | OSS备份 | 备份计划名称。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | ECS备份类型，只有ECS时必填。 ECS DISK：云盘备份 _ ECS FILE：文件备份 _ |
| -instanceType | String | OSS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 4 | 资源集ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |
| -instanceId | String | 69987589-****- 437b-9013- 2391**** | 实例ID |
| - instanceName | String | oss-test | 实例名称 |
| - storageLocatio n | String | EMOTE | 存储位置： EMOTE：代表异地 PUBLIC CLOUD：阿里公共云 _ |
| - localStorageLo cation | String | LOCAL | 异地存储位置，取值LOCAL |
| -description | String | 备份计划列表详情 | 描述 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupPlanList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "Status":"RUNNING",
  "OrganizationName":"test",
  "ResourceGroupId":4,
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
  "PlanName":"OSS备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
  "InstanceType":"OSS",
  "ResourceGroupName":"ResourceSet(test)"
 },
 "ErrorCode":"BackupPlanNotFound",
 "ErrorMessage":"Not Found BackupPlan for current operate.",
 "TotalSize":50,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <ResourceGroupId>4</ResourceGroupId>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <PlanName>OSS备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
 <ResourceGroupName>ResourceSet(test)</ResourceGroupName>
</Data> <ErrorMessage>Not Found BackupPlan for current operate.</ErrorMessage> <TotalSize>50</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeBackupPlan

查看备份计划详情

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| PlanId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |

灾备管理中心

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanDe tailInner | Struct |  | 备份计划详情。 |
| - backupPolicyLi st | Array |  | 备份策略集合 |
| -- preferredBack upPeriod | String | ["2"] | 备份周期。 RDS、DRDS：["SUNDAY"、 "MONDAY"]，每周日、周三备份。 其他产品： ["2"]，2天或小时。 |
| -- preferredBack upPeriodFull | String | ["7"] | 全量备份备份周期。 |
| -- backupRetenti onPeriod | Integer | 14 | 备份保存时长。单位：天。 |
| --policyType | String | INCREMENTAL | 备份策略类型： 全量备：FULL。 增量备份：INCREMENTAL。 全量+增量：FULL INCREMENTAL。 _ |
| -- preferredBack upTime | String | 1677815157665 | 备份执行时间，UTC时间。 RDS、DRDS： 10:00Z-11:00Z(UTC时间)。 其他： 1677576600519，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- preferredBack upType | String | BY TIME _ | 备份保存类型，BY TIME：按时间。 _ |
| -- preferredCycle Type | String | BY INTERVAL _ | 备份间隔： BY HOUR：按小时。 _ BY INTERVAL：按天。 _ |
| --vaultId | String | 1231--- 231231231236 | 仓库ID |
| --vaultName | String | asd | 仓库名称 |
| --backupMode | String | normal | 备份模式 |
| -- storagePositio n | String | LOCAL | 存储位置: REMOTE：代表异地 LOCAL：代表本地 |
| -- logBackupRete ntionPeriod | Integer | 2 | 日志备份保留时长，单位：天。 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planName | String | NAS备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行。 _ CREATING：创建中。 CREATED：创建成功。 STARTING：启动中。 RUNNING：运行中 BACKING UP：备份中。 _ STOPPING：停止中 STOPPED：已停止。 DELETED： 已删除。 DELETING：删除中。 |
| -backupType | String | ECSFILE | 备份类型。 ECSFILE：ECS文件。 ECSDISK：ECS云盘。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -instanceType | String | NAS | 实例类型。 OSS、ECS、NAS、ADB、RDS、 DRDS、ODPS、ES（ElasticSearch）及 VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行。 _ BACKUPING：运行中。 SUCCESS：成功。 PART FINISHED：部分完成。 _ FAILED：失败。 MIGRATING：迁移中。 BLOCKED：已阻塞。 |
| - lastBackupTim e | Long | 1677825909000 | 最后备份时间 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 4 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

|  | 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -instance | Struct |  | 备份实例信息。 |
| --whitelist | String | "*bacup- test,*temp-table" | 白名单列表 |
| --blacklist | String | "temp-arst,black- tes" | 黑名单列表 |
| --instanceId | String | 1ase4****** | 实例ID。 |
| -- instanceName | String | 1ase4****** | 实例名称。 |
| -- instanceBacku pType | String | UDM ECS _ | ECS实例备份类型。 UDM ECSY：ECS整机备份。 _ UDM ECSY DISK：ECS云盘备份。 _ _ |
| --prefix | String | /root/ | 备份目录。 |
| --speedLimit | String | 8:10:10240\|12:18: 5120 | ECS文件备份限速配置项。 |
| --cloudDiskList | String | ["d- sddgerttr224****** "] | ECS快照备份，指定云盘列表。 |
| -- consistentLeve l | String | CRASH | ECS快照备份一致性级别。 CRASH：崩溃一致性。 |
| -- instanceResou rcesType | String | CATALOG | 默认值：["CATALOG"] ，取值范围： CATALOG：项目备份，默认会备份项目中存在的TABLE、RESOURCE、FUNCTION类型的所有数据，允许配置黑名单或者白名单来控制备份的表。 TABLE：表备份，会根据白名单进行备份，表备份必须传输白名单列表参数。 |
| -- specifyProject | String | test | 指定备份项目 |
| -- tempTablePref ix | String | awd | 临时表名前缀，表名大小写不敏感，不能有特殊字符，只能包含a~z、A~Z、数字和下划线 （ ）。建议以字母开头，名称的长度不超过64 _ 字节。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=DescribeBackupPlan &PlanId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
  "creator":"ascm-org-********",
  "resourceGroupName":"ResourceSet(test)",
  "organizationName":"test",
  "lastResult":"SUCCESS",
  "instanceType":"NAS",
  "regionName":"cn-hangzhou******",
  "nextBackupTime":1677825909000,
  "creatorId":5612,
  "planName":"NAS备份",
  "mtime":1677825909000,
  "backupType":"ECSFILE",
  "lastBackupTime":1677825909000,
  "organizationId":12,
  "regionId":"cn-hangzhou******",
   "preferredBackupPeriod":"[\"2\"]",
   "preferredBackupTime":"1677815157665",
   "vaultName":"asd",
   "logBackupRetentionPeriod":2,
   "vaultId":"1231---231231231236",
   "backupMode":"normal",
   "policyType":"INCREMENTAL",
   "storagePosition":"LOCAL",
   "backupRetentionPeriod":14,
   "preferredBackupPeriodFull":"[\"7\"]",
   "preferredCycleType":"BY_INTERVAL",
  },
  "ctime":1677825909000,
  "planId":"d202309c-0c20-44e2-9e02-bacf******",
  "resourceGroupId":4,
   "tempTablePrefix":"awd",
   "instanceId":"1ase4******",
   "consistentLevel":"CRASH",
   "instanceResourcesType":"CATALOG",
   "instanceName":"1ase4******",
   "prefix":"/root/",
   "cloudDiskList":"[\"d-sddgerttr224******\"]",
```

灾备管理中心

```json
   "blacklist":"\"temp-arst,black-tes\"",
   "whitelist":"\"*bacup-test,*temp-table\"",
   "speedLimit":"8:10:10240|12:18:5120",
   "instanceBackupType":"UDM_ECS",
   "specifyProject":"test"
  },
  "status":"RUNNING"
 },
 "errorMessage":"Not Found BackupPlan for current operate.",
}
```

`XML` 格式

```xml
<code>200</code> <cost>20</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success>
 <creator>ascm-org-********</creator>
 <resourceGroupName>ResourceSet(test)</resourceGroupName>
 <organizationName>test</organizationName>
 <lastResult>SUCCESS</lastResult>
 <regionName>cn-hangzhou******</regionName>
 <nextBackupTime>1677825909000</nextBackupTime>
 <creatorId>5612</creatorId>
 <planName>NAS备份</planName>
 <mtime>1677825909000</mtime>
 <lastBackupTime>1677825909000</lastBackupTime>
 <organizationId>12</organizationId>
 <regionId>cn-hangzhou******</regionId>
  <preferredBackupPeriod>[&quot;2&quot;]</preferredBackupPeriod>
  <preferredBackupTime>1677815157665</preferredBackupTime>
  <logBackupRetentionPeriod>2</logBackupRetentionPeriod>
  <policyType>INCREMENTAL</policyType>
  <backupRetentionPeriod>14</backupRetentionPeriod>
  <preferredBackupPeriodFull>[&quot;7&quot;]</preferredBackupPeriodFull>
  <preferredCycleType>BY_INTERVAL</preferredCycleType>
  <preferredBackupType>BY_TIME</preferredBackupType>
 <ctime>1677825909000</ctime>
 <planId>d202309c-0c20-44e2-9e02-bacf******</planId>
 <resourceGroupId>4</resourceGroupId>
  <tempTablePrefix>awd</tempTablePrefix>
```

灾备管理中心

```
staced ase
```

/

```xml
staced
  <consistentLevel>CRASH</consistentLevel>
  <instanceResourcesType>CATALOG</instanceResourcesType>
  <prefix>/root/</prefix>
  <cloudDiskList>[&quot;d-sddgerttr224******&quot;]</cloudDiskList>
  <blacklist>&quot;temp-arst,black-tes&quot;</blacklist>
  <whitelist>
&quot;*bacup-test,*temp-table&quot;</whitelist>
   <speedLimit>8:10:10240|12:18:5120</speedLimit>
   <instanceBackupType>UDM_ECS</instanceBackupType>
   <specifyProject>test</specifyProject>
  <status>RUNNING</status>
 <errorMessage>Not Found BackupPlan for current operate.</errorMessage>
```

##### DisableBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| PlanId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |

|  | 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 计划详情。 |
| -result | Boolean | true | 请求结果。 true：成功 false：失败 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -state | String | STOPPED | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |

**示例**

请求示例

```
&PlanId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "State":"STOPPED",
  "PlanId":"d202309c-0c20-44e2-9e02-bacf******",
  "Result":true
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"BackupPlanNotFound",
 "ErrorMessage":"Not Found BackupPlan for current operate.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
 <State>STOPPED</State>
 <PlanId>d202309c-0c20-44e2-9e02-bacf******</PlanId>
 <Result>true</Result>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorMessage>Not Found BackupPlan for current operate.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### EnableBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlanId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 本次请求是否成功。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| ErrorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| ErrorCode | String | BackupPlanNotFou nd | 错误码。 |
| Path | String | /asrbr/*/* | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| BackupPlanInn er | Struct |  | 备份计划详情。 |
| -Result | Boolean | true | 请求结果。 true：成功 false：失败 |
| -PlanId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -State | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |

**示例**

请求示例

```
&PlanId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例灾备管理中心 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
  "State":"RUNNING",
  "PlanId":"d202309c-0c20-44e2-9e02-bacf******",
  "Result":true
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"BackupPlanNotFound",
 "ErrorMessage":"Not Found BackupPlan for current operate.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
 <State>RUNNING</State>
 <PlanId>d202309c-0c20-44e2-9e02-bacf******</PlanId>
 <Result>true</Result>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorMessage>Not Found BackupPlan for current operate.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### ExecuteBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 21 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 322 | 资源集ID |
| PlanId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 否 | i-deriqa1******** | 备份实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划详情。 |
| -result | Boolean | true | 请求结果。 true：成功 false：失败 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -state | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |

**示例**

请求示例

```
&PlanId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"Not Found BackupPlan for current operate.",
 "errorCode":"BackupPlanNotFound",
  "result":true,
  "planId":"d202309c-0c20-44e2-9e02-bacf******",
  "state":"RUNNING"
 }
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>Not Found BackupPlan for current operate.</errorMessage>
 <result>true</result>
 <planId>d202309c-0c20-44e2-9e02-bacf******</planId>
 <state>RUNNING</state>
```

##### ModifyBackupPolicy

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| PlanId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BackupPol icy | Json | Body | 是 | [ { "preferredBackupPeriod" :[ 1 ], "preferredBackupTime": 1669918794351, "backupRetentionPeriod ":10, "preferredBackupPeriod Full":[ 8 ], "preferredCycleType":"B Y DAY","vaultId":"123as _ qwqweqw*****"} ] | 备份策略。 preferredBackupPerio d：备份周期，RDS、 PolarDB-X及ADB取值 ["Monday"：星期一,"Tuesday"：星期二，"Wednesday"：星期三，"Thursday"：星期四，"Friday"：星期五，"Saturday"：星期六，"Sunday"：星期日]；其他产品取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。RDS、 PolarDB-X及ADB取值为 UTC时间段，例如： 10:00Z-11:00Z；其他产品取值为时间戳，例如： 1669918794351。 backupRetentionPerio d：备份保留时长，单位为天。 preferredCycleType： 备份周期类型，取值 BY HOUR为按小 _ 时，BY DAY为按天。 _ preferredBackupPerio dFull：全量备份周期。 vaultId：备份仓库ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanDe tailInner | Struct |  | 备份计划详情。 |
| - backupPolicyLi st | Array |  | 备份策略集合 |
| -- preferredBack upPeriod | String | 2 | 备份周期。 RDS、PolarDB-X：["SUNDAY"、 "MONDAY"]，每周日、周三备份其他产品：["2"]，2天或小时 |
| -- preferredBack upPeriodFull | String | 7 | 全量备份备份周期。 |
| -- backupRetenti onPeriod | Integer | 14 | 备份保存时长。单位：天。 |
| --policyType | String | INCREMENTAL | 备份策略类型。 全量备份：FULL 增量备份：INCREMENTAL 全量+增量：FULL INCREMENTAL _ |
| -- preferredBack upTime | String | 1677825909000 | 备份执行时间，UTC时间。 RDS、PolarDB-X：10:00Z-11:00Z(UTC时间) 其他：1677576600519，单位毫秒（ms） |
| -- preferredBack upType | String | BY TIME _ | 备份保存类型。 BY TIME：按时间。 _ |
| -- preferredCycle Type | String | BY INTERVAL _ | 备份间隔。 BY HOUR：按小时 _ BY INTERVAL：按天 _ |
| --vaultId | String | c59f9c6b-effd- 4d5c-841b- c14d9a686a26 | 仓库ID |
| --vaultName | String | lengjuetest | 仓库名称 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- storagePositio n | String | LOCATION | 存储位置，用于判断本地/异地策略。 LOCATION：本地 REMOTE：异地 PUBLIC CLOUD：阿里公共云 _ |
| --backupMode | String | ALL | 备份模式 |
| -- logBackupRete ntionPeriod | Integer | 23 | 备份日志保留时长。 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planName | String | NAS备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED：已删除 DELETING：删除中 |
| -backupType | String |  | ECS备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
| -instanceType | String | NAS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -lastResult | Integer | 1 | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 4 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例灾备管理中心

```json
http(s)://[Endpoint]/?Action=ModifyBackupPolicy &PlanId=d202309c-0c20-44e2-9e02-bacf****** { "preferredBackupPeriod":[ 1 ], "preferredBackupTime":1669918794351, "backupRetentionPeriod":10, "preferredBackupPeriodFull":[ 8 ], "preferredCycleType":"BY_DAY","vaultId":"123asqwqweqw*****"}
```

] &公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
  "creator":"ascm-org-********",
  "resourceGroupName":"ResourceSet(test)",
  "organizationName":"test",
  "lastResult":1,
  "instanceType":"NAS",
  "regionName":"cn-hangzhou******",
  "nextBackupTime":1677825909000,
  "creatorId":5612,
  "planName":"NAS备份",
  "mtime":1677825909000,
  "backupType":"",
  "organizationId":12,
  "regionId":"cn-hangzhou******",
   "preferredBackupPeriod":"2",
   "preferredBackupTime":"1677825909000",
   "vaultName":"lengjuetest",
   "logBackupRetentionPeriod":23,
   "vaultId":"c59f9c6b-effd-4d5c-841b-c14d9a686a26",
   "backupMode":"ALL",
   "policyType":"INCREMENTAL",
   "storagePosition":"LOCATION",
   "backupRetentionPeriod":14,
   "preferredBackupPeriodFull":"7",
   "preferredCycleType":"BY_INTERVAL",
  },
  "ctime":1677825909000,
  "planId":"d202309c-0c20-44e2-9e02-bacf******",
  "resourceGroupId":4,
  "status":"RUNNING"
 },
 "errorMessage":"Not Found BackupPlan for current operate.",
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success>
 <creator>ascm-org-********</creator>
 <resourceGroupName>ResourceSet(test)</resourceGroupName>
 <organizationName>test</organizationName>
 <lastResult>1</lastResult>
 <regionName>cn-hangzhou******</regionName>
 <nextBackupTime>1677825909000</nextBackupTime>
 <creatorId>5612</creatorId>
 <planName>NAS备份</planName>
 <mtime>1677825909000</mtime>
 <organizationId>12</organizationId>
 <regionId>cn-hangzhou******</regionId>
  <preferredBackupPeriod>2</preferredBackupPeriod>
  <preferredBackupTime>1677825909000</preferredBackupTime>
  <logBackupRetentionPeriod>23</logBackupRetentionPeriod>
  <vaultId>c59f9c6b-effd-4d5c-841b-c14d9a686a26</vaultId>
  <policyType>INCREMENTAL</policyType>
  <storagePosition>LOCATION</storagePosition>
  <backupRetentionPeriod>14</backupRetentionPeriod>
  <preferredBackupPeriodFull>7</preferredBackupPeriodFull>
  <preferredCycleType>BY_INTERVAL</preferredCycleType>
  <preferredBackupType>BY_TIME</preferredBackupType>
 <ctime>1677825909000</ctime>
 <planId>d202309c-0c20-44e2-9e02-bacf******</planId>
 <resourceGroupId>4</resourceGroupId>
 <status>RUNNING</status>
<errorMessage>Not Found BackupPlan for current operate.</errorMessage>
```

### 备份记录

#### DescribeBackupInstanceRecordList

调用DescribeBackupInstanceRecordList查看备份实例记录列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 21 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 332 | 资源集ID |
| PlanId | Strin g | Query | 否 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |
| InstanceId | Strin g | Query | 否 | rm-sf234dsfellre0****** | 实例ID。 |
| InstanceT ype | Strin g | Query | 否 | RDS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |
| Result | Strin g | Query | 否 | SUCCESS | 记录结果状态 |
| MinBeginT ime | Long | Query | 否 | 170025634 | 最小开始时间 |
| MaxBegin Time | Long | Query | 否 | 192202365 | 最大开始时间 |
| PageNum | Integ er | Query | 否 | 1 | 分页页码。 |
| PageSize | Integ er | Query | 否 | 10 | 分页记录数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| -recordId | Integer | 1 | 记录ID。 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planRecordId | String | fghres26s58-0189- 4sdf-88hj-******* | 备份计划记录ID。 |
| -backupMode | String | QUICK | DRDS备份模式。 CONSISTENCY：一致性备份。 QUICK：快速备份。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -backupType | String | ECS FILE _ | ECS备份类型 ECS DISK：云盘 _ ECS FILE：文件 _ |
| - backupDataTy pe | String | string | 备份数据类型 |
| -beginTime | Long | 1677825909000 | 备份开始时间。 |
| -endTime | Long | 1677825909000 | 备份结束时间。 |
| -ctime | Long | 1677825909000 | 创建时间。 |
| -expireDate | Long | 1677825909000 | 过期时间。 |
| -expireStatus | Integer | 0 | 过期状态。 0：未过期。 1：已过期。 |
| -instanceId | String | rm- sf234dsfellre0***** * | 实例ID。 |
| - instanceName | String | rm- sf234dsfellre0***** * | 实例名称。 |
| -progress | Integer | 10000 | 备份进度。 10000代表100%。 |
| -snapshotId | String | s- 000020swb2****** **** | 快照ID。 |
| -snapshotHash | String | b0f20b06ab5****** *****322e34faa9a | 快照Hash值。 |
| -vaultId | String | 4a0b3d3d********7 9a12620b | 备份仓库ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -result | String | SUCCESS | 备份记录结果。 IN QUEUE(0)：队列中 _ BACKUPING(1)：备份中 SUCCESS(2)：备份完成 FAILED(3)：备份失败 UNABLE(4)：过期失效 PARTIAL COMPLETE(5)：备份部分完成 _ BLOCKED(6)：阻塞 DELETED(7)：已删除 DELETEDING(8)：删除中 DELETED FAILED(9)：删除失败 _ CANCELED(10)： 已取消 EXECUTE INIT(11)：立即备份初始化状态 _ |
| -size | Long | 1024 | 备份集大小。单位：byte。 |
| -replication | Boolean | true | 是否使用镜像复制： ture：是 false：否 |
| - storageLocatio n | String | REMOTE | 备份位置。 LOCAL：本地 REMOTE：异地 |
| - containSystem Disk | Integer | 0 | 是否包含系统盘。 0：否 1：是 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 100 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 20 | 数据总量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupInstanceRecordList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":100,
 "totalSize":20,
 "data":{
  "replication":"",
  "snapshotId":"s-000020swb2**********",
  "instanceName":"rm-sf234dsfellre0******",
  "vaultId":"4a0b3d3d********79a12620b",
  "snapshotHash":"b0f20b06ab5***********322e34faa9a",
  "storageLocation":"REMOTE",
  "backupType":"ECS_FILE",
  "recordId":1,
  "result":"SUCCESS",
  "planRecordId":"fghres26s58-0189-4sdf-88hj-*******",
  "backupDataType":"string",
  "instanceId":"rm-sf234dsfellre0******",
  "size":1024,
  "backupMode":"QUICK",
  "ctime":1677825909000,
  "progress":10000,
  "planId":"d202309c-0c20-44e2-9e02-bacf******",
  "expireDate":1677825909000,
  "expireStatus":0,
  "containSystemDisk":0,
  "beginTime":1677825909000,
  "endTime":1677825909000
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"failed",
 "errorCode":"403",
 "pageSize":10,
 "pageNum":1
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>100</cost> <totalSize>20</totalSize> <data>
 <replication  />
 <snapshotId>s-000020swb2**********</snapshotId>
 <instanceName>rm-sf234dsfellre0******</instanceName>
 <vaultId>4a0b3d3d********79a12620b</vaultId>
 <snapshotHash>b0f20b06ab5***********322e34faa9a</snapshotHash>
 <recordId>1</recordId>
 <result>SUCCESS</result>
 <planRecordId>fghres26s58-0189-4sdf-88hj-*******</planRecordId>
 <instanceId>rm-sf234dsfellre0******</instanceId>
 <size>1024</size>
 <ctime>1677825909000</ctime>
 <progress>10000</progress>
 <planId>d202309c-0c20-44e2-9e02-bacf******</planId>
 <expireDate>1677825909000</expireDate>
 <expireStatus>0</expireStatus>
 <beginTime>1677825909000</beginTime>
 <endTime>1677825909000</endTime>
</data> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>failed</errorMessage> <errorCode>403</errorCode> <pageSize>10</pageSize> <pageNum>1</pageNum>
```

### 恢复任务

#### 创建恢复任务

##### CreateAdbRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | adb-task | 恢复任务名称。 |
| Descriptio n | Strin g | Body | 否 | ADB恢复任务 | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "instanceId":"am- c3k97d2k8yn***", "recordId":"1", "recoveryInstanceName" :"adb-restore", "vpcId":"vpc- q1fxs39dm3***", "vSwitchId":"vsw- q1flt5ccjklh3pz****", "organizationId":2, "resourceGroupId":4, "zoneId":"azone- ********" } | 恢复任务实例信息。 instanceId：备份实例ID recordId：备份记录ID recoveryInstanceNam e：恢复实例名称 vpcId：专有网络ID vSwitchId：交换机ID organizationId：组织ID resourceGroupId：资源集ID zoneId：可用区ID |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 32 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | adb-task | 恢复任务名称。 |
| -instanceType | String | ADB | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 2 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String | ECS FILE _ | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -creator | String | ascm-org-**** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateAdbRecoveryTask &ClientToken=123e4567********55440000 &TaskName=adb-task
        "instanceId":"am-c3k97d2k8yn***",
        "recordId":"1",
        "recoveryInstanceName":"adb-restore",
        "vpcId":"vpc-q1fxs39dm3***",
        "vSwitchId":"vsw-q1flt5ccjklh3pz****",
        "organizationId":2,
        "resourceGroupId":4,
        "zoneId":"azone-********"
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":32,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"failed",
 "errorCode":"403",
 "recoveryTaskInner":{
  "creator":"ascm-org-****",
  "instanceNum":1,
  "organizationName":"test",
  "instanceType":"ADB",
  "regionName":"cn-hangzhou*****",
  "creatorId":5612,
  "mtime":1677825909000,
  "recoveryType":"ECS_FILE",
  "organizationId":2,
  "deleted":0,
  "regionId":"cn-hangzhou******",
  "ctime":1677825909000,
  "taskName":"adb-task",
  "beginTime":1677825909000,
  "endTime":1677825909000,
  "taskId":"d202309c-0c20-44e2-9e02-bacf******",
  "status":"RECOVERYING"
 }
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>32</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>failed</errorMessage> <errorCode>403</errorCode> <recoveryTaskInner>
 <creator>ascm-org-****</creator>
 <organizationName>test</organizationName>
 <regionName>cn-hangzhou*****</regionName>
 <creatorId>5612</creatorId>
 <mtime>1677825909000</mtime>
 <recoveryType>ECS_FILE</recoveryType>
 <organizationId>2</organizationId>
 <deleted>0</deleted>
 <regionId>cn-hangzhou******</regionId>
 <ctime>1677825909000</ctime>
 <taskName>adb-task</taskName>
 <beginTime>1677825909000</beginTime>
 <endTime>1677825909000</endTime>
 <taskId>d202309c-0c20-44e2-9e02-bacf******</taskId>
 <status>RECOVERYING</status>
</recoveryTaskInner>
```

##### CreateDrdsRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 123421 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 12456 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | PolarDB-X恢复 | 恢复任务名称。 |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | DRDS恢复计划 | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "instanceId":"drdsusrz30 8***", "recordId":"1", "recoveryInstanceName" :"drdsrestore-test", "vpcId":"vpc- q1fxs39dm3cc2wk6jcut0 ", "vSwitchId":"vsw- q1flt5ccjklh38qxm51pz", "organizationId":2, "resourceGroupId":4, "dbInstanceSpec":"mysq l.x4.large.2", "dbInstanceStorage":20 0, "engine":"mysql", "engineVersion":"5.7", "zoneId":"azone-atest- 0923421" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceNam e：恢复实例名称。 vpcId：专有网络ID。 vSwitchId：交换机ID。 organizationId：组织 ID。 resourceGroupId：资源集ID。 dbInstanceSpec：数据库实例规格。 dbInstanceStorage： 数据库实例存储。 engine：数据库引擎类型。 engineVersion：数据库引擎版本。 zoneId：可用区ID。 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

|  | 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 10 | 接口耗时，单位毫秒（ms）。 |
| RecoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | PolarDB-X恢复 | 恢复任务名称。 |
| -instanceType | String | PolarDB-X | 实例类型。包含OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou***** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |
| -creator | String | ascm-org-**** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateDrdsRecoveryTask &ClientToken=123e4567********55440000 &TaskName=PolarDB-X恢复 "instanceId":"drdsusrz308***", "recordId":"1", "recoveryInstanceName":"drdsrestore-test", "vpcId":"vpc-q1fxs39dm3cc2wk6jcut0", "vSwitchId":"vsw-q1flt5ccjklh38qxm51pz", "organizationId":2, "resourceGroupId":4, "dbInstanceSpec":"mysql.x4.large.2", "dbInstanceStorage":200, "engine":"mysql", "engineVersion":"5.7", "zoneId":"azone-atest-0923421" }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":10,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"failed",
 "errorCode":"403",
 "RecoveryTaskInner":{
  "creator":"ascm-org-****",
  "instanceNum":1,
  "organizationName":"test",
  "instanceType":"PolarDB-X",
  "regionName":"cn-hangzhou*****",
  "creatorId":5612,
  "mtime":1677825909000,
  "recoveryType":"",
  "organizationId":12,
  "deleted":0,
  "regionId":"cn-hangzhou*****",
  "ctime":1677825909000,
  "taskName":"PolarDB-X恢复",
  "beginTime":1677825909000,
  "endTime":1677825909000,
  "taskId":"d202309c-0c20-44e2-9e02-bacf******",
  "status":"RECOVERYING"
 }
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>10</cost> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>failed</errorMessage> <errorCode>403</errorCode> <RecoveryTaskInner>
 <creator>ascm-org-****</creator>
 <organizationName>test</organizationName>
 <regionName>cn-hangzhou*****</regionName>
 <creatorId>5612</creatorId>
 <mtime>1677825909000</mtime>
 <recoveryType  />
 <organizationId>12</organizationId>
 <deleted>0</deleted>
 <regionId>cn-hangzhou*****</regionId>
 <ctime>1677825909000</ctime>
 <taskName>PolarDB-X恢复</taskName>
 <beginTime>1677825909000</beginTime>
 <endTime>1677825909000</endTime>
 <taskId>d202309c-0c20-44e2-9e02-bacf******</taskId>
 <status>RECOVERYING</status>
</RecoveryTaskInner>
```

##### CreateEcsRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 13 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | ecs-task | 恢复任务名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| TaskType | Strin g | Query | 否 | REGULAR | 任务类型 |
| Descriptio n | Strin g | Body | 否 | ECS恢复任务 | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":"1", "instanceId":"i- q1f01emdyy9a*******", "targetPrefix":"/", "recoveryInstanceId":"i- q1f01em9an***" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 targetPrefix：目标端目录。 recoveryInstanceId： 覆盖实例ID。 |
| IsDisaster Recovery | Boole an | Query | 否 | false | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 10 | 接口耗时，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | ecs-task | 恢复任务名称。 |
| -instanceType | String | ECS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String | ECS FILE _ | 恢复类型。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou***** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |
| -creator | String | ascm-org-****** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateEcsRecoveryTask &ClientToken=123e4567********55440000 &TaskName=ecs-task
        "recordId":"1",
        "instanceId":"i-q1f01emdyy9a*******",
        "targetPrefix":"/",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"ECS_FILE",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-******",
  "InstanceNum":1,
  "TaskName":"ecs-task",
  "RegionName":"cn-hangzhou*****",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou*****",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":10,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
</Path> <RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType>ECS_FILE</RecoveryType>
 <TaskId>d202309c-0c20-44e2-9e02-bacf******
 </TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-******</Creator>
 <TaskName>ecs-task</TaskName>
 <RegionName>cn-hangzhou*****</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou*****</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>10</Cost> <Success>true</Success>
```

##### CreateEcsSnapshotRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 13 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskName | Strin g | Query | 是 | ECS快照恢复 | 恢复任务名称。 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | 快照恢复 | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":"3", "instanceId":"i- q1f01emdyy9a*******", "recoveryInstanceId":"i- q1f01gxfpx1***", "diskId":"d- q1f01emdyy9a****", "diskCategory":"cloud ef _ ficiency", "recoveryInstanceName" :"test-backup" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceId： 云盘挂载实例ID。 diskId：云盘ID。 diskCategory：云盘类型。取值 cloud efficiency为高效 _ 云盘，cloud pperf为高 _ 性能云盘，cloud ssd为 _ SSD盘，cloud sperf为 _ 普通性能云盘。 recoveryInstanceNam e：云盘挂载实例名称。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | ECS快照恢复 | 恢复任务名称。 |
| -instanceType | String | ECS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String | ECS DISK _ | 恢复类型。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org-****** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateEcsSnapshotRecoveryTask &ClientToken=123e4567********55440000
```

`&TaskName=ECS`快照恢复

```json
        "recordId":"3",
        "instanceId":"i-q1f01emdyy9a*******",
        "recoveryInstanceId":"i-q1f01gxfpx1***",
        "diskId":"d-q1f01emdyy9a****",
        "diskCategory":"cloud_efficiency",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"ECS_DISK",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-******",
  "InstanceNum":1,
```

`"TaskName":"ECS`快照恢复`",`

```json
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType>ECS_DISK</RecoveryType>
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-******</Creator>
 <TaskName>ECS快照恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateEsRecoveryTask

调用CreateEsRecoveryTask创建Elasticsearch恢复任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | Elasticsearch恢复任务 | 恢复任务名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":"1", "instanceId":"source-6- 8-*********", "recoveryInstanceId":"ta rget-6-8-*****" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceId： 覆盖实例ID。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | Elasticsearch恢复任务 | 恢复任务名称。 |
| -instanceType | String | Elasticsearch | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org- ********** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateEsRecoveryTask &ClientToken=123e4567********55440000 &TaskName=Elasticsearch恢复任务
        "recordId":"1",
        "instanceId":"source-6-8-*********",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-**********",
  "InstanceNum":1,
  "TaskName":"Elasticsearch恢复任务",
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
</Path> <RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-**********</Creator>
 <TaskName>Elasticsearch恢复任务</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
 <InstanceType>Elasticsearch</InstanceType>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateNasRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 23 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 31 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskName | Strin g | Query | 是 | NAS恢复 | 恢复任务名称。 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":"1", "instanceId":"15bf74**** ", "targetPrefix":"/", "recoveryInstanceId":"1 9d824****" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 targetPrefix：目的端目录。 recoveryInstanceId： 覆盖实例ID。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | NAS恢复 | 恢复任务名称。 |
| -instanceType | String | NAS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org-******* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateNasRecoveryTask &ClientToken=123e4567********55440000 &TaskName=NAS恢复
        "recordId":"1",
        "instanceId":"15bf74****",
        "targetPrefix":"/",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*******",
  "InstanceNum":1,
  "TaskName":"NAS恢复",
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*******</Creator>
 <TaskName>NAS恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateOdpsRecoveryTask

调用CreateOdpsRecoveryTask创建MaxCompute恢复任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 43 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | MaxCompute恢复 | 恢复任务名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":"3", "instanceId":"odps- q1f01em****", "recoveryInstanceId":"od ps-q1f01gxfp*******" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceId： 覆盖实例ID。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | MaxCompute恢复 | 恢复任务名称。 |
| -instanceType | String | MaxCompute | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org- ************** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateOdpsRecoveryTask &ClientToken=123e4567********55440000 &TaskName=MaxCompute恢复
        "recordId":"3",
        "instanceId":"odps-q1f01em****",
        "recoveryInstanceId":"odps-q1f01gxfp*******"
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-**************",
  "InstanceNum":1,
  "TaskName":"MaxCompute恢复",
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-**************</Creator>
 <TaskName>MaxCompute恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateOssRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 43 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | OSS恢复 | 恢复任务名称。 |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "instanceId":"bucket- test*****", "recordId":"1", "recoveryInstanceName" :"restore-****", "recoveryInstanceId":"re store-****", "targetPrefix":"recovery/ " } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceNam e：覆盖恢复实例名称。 recoveryInstanceId： 覆盖恢复实例ID。 targetPrefix：目的端目录。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | OSS恢复 | 恢复任务名称。 |
| -instanceType | String | OSS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org-********* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateOssRecoveryTask &ClientToken=123e4567********55440000 &TaskName=OSS恢复
        "instanceId":"bucket-test*****",
        "recordId":"1",
        "recoveryInstanceName":"restore-****",
        "recoveryInstanceId":"restore-****",
        "targetPrefix":"recovery/"
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*********",
  "InstanceNum":1,
  "TaskName":"OSS恢复",
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******
 </TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*********</Creator>
 <TaskName>OSS恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### CreateRdsRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 21 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TaskName | Strin g | Query | 是 | RDS恢复 | 恢复任务名称。 |
| TaskType | Strin g | Query | 否 | REGULAR | 恢复类型： 常规恢复：REGULAR 灾难恢复：DISASTER |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "instanceId":"rm- c3ksc7g4*******", "recordId":"1", "recoveryInstanceName" :"rds-restore", "vpcId":"vpc- q1fxs39dm3cc*****", "vSwitchId":"vsw- q1flt5ccjklh38******", "organizationId":2, "resourceGroupId":4, "zoneId":"zone-a- **********" } | 恢复任务实例信息。 instanceId：备份实例 ID。 recordId：备份记录ID。 recoveryInstanceNam e：恢复实例名称。 vpcId：专有网络ID。 vSwitchId：虚拟机ID。 organizationId：组织 ID。 resourceGroupId：资源集ID。 zoneId：可用区ID。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |
| EnableSta rt | Boole an | Body | 否 | true | 是否马上运行： true false |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | RDS恢复 | 恢复任务名称。 |
| -instanceType | String | RDS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -creator | String | ascm-org- ********** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```json
http(s)://[Endpoint]/?Action=CreateRdsRecoveryTask &ClientToken=123e4567********55440000 &TaskName=RDS恢复
        "instanceId":"rm-c3ksc7g4*******",
        "recordId":"1",
        "recoveryInstanceName":"rds-restore",
        "vpcId":"vpc-q1fxs39dm3cc*****",
        "vSwitchId":"vsw-q1flt5ccjklh38******",
        "organizationId":2,
        "resourceGroupId":4,
        "zoneId":"zone-a-**********"
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-**********",
  "InstanceNum":1,
  "TaskName":"RDS恢复",
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-**********</Creator>
 <TaskName>RDS恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### 管理恢复任务

##### DescribeRecoverableDiskList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RecordId | Strin g | Query | 是 | 3 | ECS备份记录ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Data | Array |  | 返回数据。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DiskId | String | d- asdfew134ss****** *** | 云盘ID。 |
| -DiskName | String | 系统盘 | 云盘名称。 |
| -StorageSpace | Long | 2048000000 | 云盘存储大小，单位：byte。 |
| -DiskType | String | system | 云盘类型。 system：系统盘 data：数据盘 |
| - ConsistentLev el | String | CRASH | 一致性级别。 CRASH：崩溃一致性。 |
| - BackupDataTy pe | String | FULL | 备份数据方式。 FULL：全量 INCREMENTAL：增量 |
| - StorageLocatio n | String | LOCAL | 存储位置。 LOCAL：本地 REMOTE：异地 |
| -DiskCategory | String | cloud efficiency _ | 云盘规格。 cloud efficiency：高效云盘 _ cloud pperf：高性能云盘 _ cloud ssd：SSD盘 _ cloud sperf：普通性能云盘 _ |
| RequestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| Success | Boolean | true | 本次请求是否成功。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| ErrorMessage | String | The request is missing a ecsRecordId parameter. | 错误提示信息。 |
| ErrorCode | String | MissingParam.EcsR ecordId | 错误码。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Path | String | /asrbr/*/* | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoverableDiskList &RecordId=3
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":{
  "DiskType":"system",
  "ConsistentLevel":"CRASH",
  "StorageSpace":2048000000,
  "DiskCategory":"cloud_efficiency",
```

`"DiskName":"`系统盘`",`

```json
  "StorageLocation":"LOCAL",
  "BackupDataType":"FULL",
  "DiskId":"d-asdfew134ss*********"
 },
 "ErrorCode":"MissingParam.EcsRecordId",
 "ErrorMessage":"The request is missing a ecsRecordId parameter.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <ConsistentLevel>CRASH</ConsistentLevel>
 <DiskCategory>cloud_efficiency</DiskCategory>
 <DiskName>系统盘</DiskName>
 <DiskId>d-asdfew134ss*********</DiskId>
</Data> <ErrorCode>MissingParam.EcsRecordId</ErrorCode> <ErrorMessage>The request is missing a ecsRecordId parameter.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeRecoverableDrdsDbEngine

调用DescribeRecoverableDrdsDbEngine查看可恢复PolarDB-X DB引擎。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 23 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 43 | 资源集ID |
| InstanceId | Strin g | Query | 是 | drdswesd****** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| - engineVersion s | String | 5.6 | 引擎版本，支持5.6、5.7版本。 |
| -engine | String | mysql | 引擎类型，仅支持mysql。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of instanceId is null. | 错误提示信息。 |
| errorCode | String | InstanceIdIsNull | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoverableDrdsDbEngine
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":{
  "Engine":"mysql",
  "EngineVersions":"5.6"
 },
 "ErrorCode":"InstanceIdIsNull",
 "ErrorMessage":"The parameter of instanceId is null.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <Engine>mysql</Engine>
 <EngineVersions>5.6</EngineVersions>
</Data> <ErrorMessage>The parameter of instanceId is null.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeRecoverableDrdsDbSepc

调用DescribeRecoverableDrdsDbSepc查看可恢复PolarDB-X DB规格。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 23 | 资源集ID |
| NetworkT ype | Strin g | Query | 是 | CLASSIC | 网络类型。 VPC：VPC网络 CLASSIC：经典网络 |
| Engine | Strin g | Query | 是 | mysql | 引擎类型，仅支持mysql。 |
| EngineVer sion | Strin g | Query | 是 | 5.7 | 引擎版本，支持5.6、5.7版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| - dbInstanceCla ss | String | mysql.x4.****** | db实例类型。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -category | String | HighAvailability | 规格。 HighAvailability：高可用。 |
| -engine | String | mysql | 引擎类型，仅支持mysql。 |
| -engineVersion | String | 5.7 | 引擎版本，支持5.6、5.7版本。 |
| -networkType | String | VPC | 网络类型。 VPC：VPC网络 CLASSIC：经典网络 |
| -storageType | String | local ssd _ | 存储类型 |
| -storageStep | Integer | 5 | 存储选择间距 |
| -minStorage | Integer | 5 | 最小存储 |
| -maxStorage | Integer | 2000 | 最大存储 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The request is missing a DbInstanceSpec parameter. | 错误提示信息。 |
| errorCode | String | MissingParam.DbIn stanceSpec | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=DescribeRecoverableDrdsDbSepc &NetworkType=CLASSIC &Engine=mysql &EngineVersion=5.7
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "data":{
  "engineVersion":"5.7",
  "dbInstanceClass":"mysql.x4.******",
  "engine":"mysql",
  "storageType":"local_ssd",
  "minStorage":5,
  "storageStep":5,
  "category":"HighAvailability",
  "networkType":"VPC",
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"The request is missing a DbInstanceSpec parameter.",
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <engineVersion>5.7</engineVersion>
 <availableStatus>1</availableStatus>
 <dbInstanceClass>mysql.x4.******</dbInstanceClass>
 <engine>mysql</engine>
 <category>HighAvailability</category>
 <networkType>VPC</networkType>
</Data> <ErrorCode>MissingParam.DbInstanceSpec</ErrorCode> <ErrorMessage>The request is missing a DbInstanceSpec parameter.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeRecoverableInstanceList

调用DescribeRecoverableInstanceList查看可恢复实例列表。 灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 21 | 资源集ID |
| InstanceT ype | Strin g | Query | 是 | OSS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |
| RecoveryT ype | Strin g | Query | 否 | ECS FILE _ | ECS恢复类型。当实例类型为ECS时填写。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 每页返回的数据个数。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| -formerName | String | 测试实例 | 实例曾用名。 |
| -instanceId | String | test-bucket | 实例ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -metaInfo | String | "metaInfo": { "architecture": "x86 64", _ "clusterId": "", "zoneId": "cn- qingdao-env17- amtest17001-a" } | 元数据信息，根据产品定制返回。 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The request is missing a recoveryType parameter. | 错误提示信息。 |
| errorCode | String | MissingParam.Reco veryType | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoverableInstanceList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "totalSize":50,
 "data":{
  "metaInfo":"\"metaInfo\": {                    \"architecture\": \"x86_64\",
\"clusterId\": \"\", \"zoneId\": \"cn-qingdao-env17-amtest17001-a\" }",
  "instanceId":"test-bucket",
```

`"formerName":"`测试实例"

```json
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"The request is missing a recoveryType parameter.",
 "errorCode":"MissingParam.RecoveryType",
 "pageSize":10,
 "pageNum":1
}
```

`XML` 格式

```xml
<code>200</code> <cost>20</cost> <totalSize>50</totalSize> <data>
 <metaInfo>&quot;metaInfo&quot;: {
                    &quot;architecture&quot;: &quot;x86_64&quot;,
                    &quot;clusterId&quot;: &quot;&quot;,
                    &quot;zoneId&quot;: &quot;cn-qingdao-env17-amtest17001-a&quot;
                }</metaInfo>
  <formerName>测试实例</formerName>
 </data>
 <requestId>C8B26B44-0189-443E-9816-*******</requestId>
 <success>true</success>
 <errorMessage>The request is missing a recoveryType parameter.</errorMessage>
 <errorCode>MissingParam.RecoveryType</errorCode>
 <pageSize>10</pageSize>
 <pageNum>1</pageNum>
```

##### DescribeRecoverableInstanceRecordList

调用DescribeRecoverableInstanceRecordList查看可以恢复实例记录列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| InstanceId | Strin g | Query | 是 | i-edsewr32********* | 实例ID。 |
| InstanceT ype | Strin g | Query | 是 | ECS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |
| RecoveryT ype | Strin g | Query | 否 | ECS FILE _ | ECS恢复类型。当实例类型为ECS时填写。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 每页返回的数据个数。 |
| IsDisaster Recovery | Boole an | Query | 否 | true | 是否是灾难恢复： true：是 false：否 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| - instanceResou rcesType | String | rds | 实例资源类型 |
| -recordId | String | ASD26B44-0189- 443E-9816-******* | 记录ID。 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planRecordId | String | fghres26s58-0189- 4sdf-88hj-******* | 备份计划记录ID。 |

|  | 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -backupMode | String | QUICK | PolarDB-X备份模式。 CONSISTENCY：一致性备份 QUICK：快速备份 |
| -beginTime | Long | 1677825909000 | 备份开始时间。 |
| -endTime | Long | 1677825909000 | 备份结束时间。 |
| -ctime | Long | 1677825909000 | 创建时间。 |
| -expireDate | Long | 1677825909000 | 过期时间。 |
| -expireStatus | Integer | 0 | 过期状态。 0：未过期 1：已过期 |
| -instanceId | String | rm- sf234dsfellre0***** * | 实例ID。 |
| - instanceName | String | rm- sf234dsfellre0***** * | 实例名称。 |
| -jobId | String | j- sa33ds4345******* | 备份任务ID。 |
| -prefix | String | /root/ | 备份文件目录。 |
| -progress | Integer | 10000 | 备份进度。 10000代表100%。 |
| -snapshotId | String | s- 000020swb2p***** ***** | 快照ID。 |
| -snapshotHash | String | b0f20b06ab5219** ********847a2322e 34faa9a | 快照Hash值。 |
| -vaultId | String | 4a0b3d3d- 2********79a12620 b | 备份仓库ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -result | String | SUCCESS | 备份记录结果。 INQUEUE(0)：队列中 BACKUPING(1)：备份中 SUCCESS(2)：备份完成 FAILED(3)：备份失败 UNABLE(4)：过期失效 PARTIAL COMPLETE(5)：备份部分完成 _ BLOCKED(6)：阻塞 DELETED(7)：已删除 DELETEDING(8)：删除中 DELETEDFAILED(9)：删除失败 CANCELED(10)： 已取消 EXECUTE INIT(11)：立即备份初始化状态 _ |
| -size | Long | 1024 | 备份集大小。单位：byte。 |
| - storageLocatio n | String | REMOTE | 备份位置。 LOCAL：本地 REMOTE：异地 |
| - containSystem Disk | Integer | 1 | 是否包含系统盘。 0：否 1：是 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The request is missing a recoveryType parameter. | 错误提示信息。 |
| errorCode | String | MissingParam.Reco veryType | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoverableInstanceRecordList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "Progress":10000,
  "PlanRecordId":"fghres26s58-0189-4sdf-88hj-*******",
  "EndTime":1677825909000,
  "ExpireDate":1677825909000,
  "InstanceId":"rm-sf234dsfellre0******",
  "Size":1024,
  "PlanId":"d202309c-0c20-44e2-9e02-bacf******",
  "BackupMode":"QUICK",
  "ExpireStatus":0,
  "BeginTime":1677825909000,
  "Prefix":"/root/",
  "VaultId":"4a0b3d3d-2********79a12620b",
  "SnapshotHash":"b0f20b06ab5219**********847a2322e34faa9a",
  "Result":"SUCCESS",
  "InstanceName":"rm-sf234dsfellre0******",
  "SnapshotId":"s-000020swb2p**********",
  "Ctime":1677825909000,
  "RecordId":"ASD26B44-0189-443E-9816-*******",
  "StorageLocation":"REMOTE",
  "JobId":"j-sa33ds4345*******",
 },
 "ErrorCode":"MissingParam.RecoveryType",
 "ErrorMessage":"The request is missing a recoveryType parameter.",
 "TotalSize":50,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <Progress>10000</Progress>
 <PlanRecordId>fghres26s58-0189-4sdf-88hj-*******</PlanRecordId>
 <EndTime>1677825909000</EndTime>
 <ExpireDate>1677825909000</ExpireDate>
 <InstanceId>rm-sf234dsfellre0******</InstanceId>
 <Size>1024</Size>
 <PlanId>d202309c-0c20-44e2-9e02-bacf******</PlanId>
 <ExpireStatus>0</ExpireStatus>
 <BeginTime>1677825909000</BeginTime>
 <Prefix>/root/</Prefix>
 <VaultId>4a0b3d3d-2********79a12620b</VaultId>
 <SnapshotHash>b0f20b06ab5219**********847a2322e34faa9a</SnapshotHash>
 <Result>SUCCESS</Result>
 <InstanceName>rm-sf234dsfellre0******</InstanceName>
 <SnapshotId>s-000020swb2p**********</SnapshotId>
 <Ctime>1677825909000</Ctime>
 <RecordId>ASD26B44-0189-443E-9816-*******</RecordId>
 <JobId>j-sa33ds4345*******</JobId>
</Data> <ErrorCode>MissingParam.RecoveryType</ErrorCode> <ErrorMessage>The request is missing a recoveryType parameter.</ErrorMessage> <TotalSize>50</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeRecoveryTaskList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 21 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 22 | 资源集ID |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceT ype | Strin g | Query | 否 | ECS | 实例类型。包括OSS、 ECS、NAS、ADB、RDS、 PolarDB-X、 MaxCompute、 Elasticsearch及 VMware。 |
| TaskName | Strin g | Query | 否 | ECS恢复 | 恢复任务名称。 |
| Status | Strin g | Query | 否 | SUCCESS | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分 _ 成功 |
| TaskType | Strin g | Query | 否 | REGULAR | 任务类型。 REGULAR：常规恢复 DISASTER：灾难恢复 LOCAL：VMware本地恢复 CLOUD：VMware云上恢复 |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 每页返回的数据个数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | ECS恢复 | 恢复任务名称。 |
| -instanceType | String | ECS | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -status | String | SUCCESS | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String | ECS FILE _ | ECS恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
| -regionId | String | cn-hangzhou***** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |
| -creator | String | ascm-org-****** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否 1：是 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -description | String | test | 描述 |
| -taskType | String | REGULAR | 恢复任务类型： 常规恢复：REGULAR 灾难恢复：DISASTER 本地恢复：LOCAL 云上恢复：CLOUD |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The product does not support. | 错误提示信息。 |
| errorCode | String | ProductNotSupport | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoveryTaskList
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "totalSize":50,
 "data":{
  "creator":"ascm-org-******",
  "instanceNum":1,
  "organizationName":"test",
  "instanceType":"ECS",
  "regionName":"cn-hangzhou*****",
  "creatorId":5612,
  "description":"test",
  "mtime":1677825909000,
  "recoveryType":"ECS_FILE",
  "organizationId":12,
  "taskType":"REGULAR",
  "deleted":0,
  "regionId":"cn-hangzhou*****",
  "ctime":1677825909000,
  "taskName":"ECS恢复",
  "beginTime":1677825909000,
  "endTime":1677825909000,
  "taskId":"d202309c-0c20-44e2-9e02-bacf******",
  "status":"SUCCESS"
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"The product does not support.",
 "errorCode":"ProductNotSupport",
 "pageSize":10,
 "pageNum":1
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <totalSize>50</totalSize> <data>
 <creator>ascm-org-******</creator>
 <organizationName>test</organizationName>
 <regionName>cn-hangzhou*****</regionName>
 <creatorId>5612</creatorId>
 <description>test</description>
 <mtime>1677825909000</mtime>
 <recoveryType>ECS_FILE</recoveryType>
 <organizationId>12</organizationId>
 <taskType>REGULAR</taskType>
 <deleted>0</deleted>
 <regionId>cn-hangzhou*****</regionId>
 <ctime>1677825909000</ctime>
 <taskName>ECS恢复</taskName>
 <beginTime>1677825909000</beginTime>
 <endTime>1677825909000</endTime>
 <taskId>d202309c-0c20-44e2-9e02-bacf******</taskId>
 <status>SUCCESS</status>
</data> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>The product does not support.</errorMessage> <errorCode>ProductNotSupport</errorCode> <pageSize>10</pageSize> <pageNum>1</pageNum>
```

##### DescribeRecoveryTask

查看恢复任务

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 22 | 资源集ID |
| TaskId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 恢复任务ID。 |

灾备管理中心

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The request is missing a taskId parameter. | 错误提示信息。 |
| errorCode | String | MissingParam.Task Id | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| - recoveryInstan ces | Array |  | 恢复实例集合。 |
| --instanceId | String | i- sidllewqw12******* | 原实例ID。 |
| -- instanceName | String | i- sidllewqw12******* | 原实例名称。 |
| -- recoveryInstan ceId | String | i- wdlsfgolpo9******* | 恢复实例ID。 |
| -- recoveryInstan ceName | String | i- wdlsfgolpo9******* | 恢复实例名称。 |
| -- backupPlanRe cordId | String | 2 | 备份计划记录ID。 |
| --regionId | String | cn-hangzhou***** | 区域ID。 |
| --regionName | String | cn-hangzhou***** | 区域名称。 |
| -- organizationId | Integer | 12 | 组织ID。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- organizationN ame | String | test | 组织名称。 |
| -- resourceGroup Id | Integer | 4 | 组织集ID。 |
| -- resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| --progress | Long | 10000 | 实例恢复进度,10000代表100%。 |
| --beginTime | Long | 1677825909000 | 恢复开始时间。 |
| --endTime | Long | 1677825909000 | 恢复结束时间。 |
| --result | String | SUCCESS | 恢复结果。 NOT RUN：未运行。 _ RECOVERYING：恢复中。 SUCCESS： 成功。 FAILED：失败。 PENDING：队列中。 CREATING： 创建中。 CREATED：已创建。 STOPPING：停止中。 STARTING：启动中。 DELETING：删除中。 DELETED：已删除。 STOPPED：已停止。 CANCELED：已取消。 PART FINISHED：部分成功。 _ |
| -- taskInstanceId | String | 12343asgdg*** | 任务实例ID |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | ECS恢复 | 恢复任务名称。 |
| -instanceType | String | ECS | 实例类型。 OSS、ECS、NAS、ADB、RDS、 DRDS、ODPS、ES（ElasticSearch）及 VMware。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -status | String | SUCCESS | 恢复任务状态。 NOT RUN：未运行。 _ RECOVERYING：恢复中。 FAILED：恢复失败。 SUCCESS：成功。 STOPPED： 停止。 PART FINISHED：部分成功。 _ |
| -progress | Long | 30 | 恢复进度 |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String | ECS FILE _ | ECS恢复类型。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -taskType | String | REGULAR | 任务类型： 常规恢复：REGULAR 灾难恢复：DISASTER 本地恢复：LOCAL 云上恢复：CLOUD |
| -regionId | String | cn-hangzhou***** | 区域ID。 |
| -regionName | String | cn-hangzhou***** | 区域名称。 |
| -creator | String | ascm-org-****** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |
| -description | String | test | 描述 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeRecoveryTask &TaskId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"The request is missing a taskId parameter.",
 "errorCode":"MissingParam.TaskId",
 "recoveryTaskInner":{
  "creator":"ascm-org-******",
  "instanceNum":1,
  "organizationName":"test",
  "instanceType":"ECS",
  "regionName":"cn-hangzhou*****",
  "creatorId":5612,
  "description":"test",
  "mtime":1677825909000,
  "recoveryType":"ECS_FILE",
   "backupPlanRecordId":"2",
   "resourceGroupName":"ResourceSet(test)",
   "organizationName":"test",
   "instanceName":"i-sidllewqw12*******",
   "regionName":"cn-hangzhou*****",
   "taskInstanceId":"12343asgdg***",
   "organizationId":12,
   "result":"SUCCESS",
   "instanceId":"i-sidllewqw12*******",
   "regionId":"cn-hangzhou*****",
   "recoveryInstanceId":"i-wdlsfgolpo9*******",
   "progress":10000,
   "resourceGroupId":4,
   "beginTime":1677825909000,
   "endTime":1677825909000,
   "recoveryInstanceName":"i-wdlsfgolpo9*******"
  },
  "organizationId":12,
  "taskType":"REGULAR",
  "deleted":0,
  "regionId":"cn-hangzhou*****",
  "progress":30,
  "ctime":1677825909000,
  "taskName":"ECS恢复",
  "beginTime":1677825909000,
  "endTime":1677825909000,
  "taskId":"d202309c-0c20-44e2-9e02-bacf******",
  "status":"SUCCESS"
 }
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <requestId>C8B26B44-0189-443E-9816-******* </requestId> <success>true</success> <errorMessage>The request is missing a taskId parameter.</errorMessage> <errorCode>MissingParam.TaskId</errorCode> <recoveryTaskInner>
 <creator>ascm-org-******</creator>
 <organizationName>test</organizationName>
 <regionName>cn-hangzhou*****</regionName>
 <creatorId>5612</creatorId>
 <description>test</description>
 <mtime>1677825909000</mtime>
 <recoveryType>ECS_FILE</recoveryType>
  <backupPlanRecordId>2</backupPlanRecordId>
  <resourceGroupName>ResourceSet(test)</resourceGroupName>
  <organizationName>test</organizationName>
  <instanceName>i-sidllewqw12*******</instanceName>
  <regionName>cn-hangzhou*****</regionName>
  <taskInstanceId>12343asgdg***</taskInstanceId>
  <organizationId>12</organizationId>
  <result>SUCCESS</result>
  <instanceId>i-sidllewqw12*******</instanceId>
  <regionId>cn-hangzhou*****</regionId>
  <recoveryInstanceId>i-wdlsfgolpo9*******</recoveryInstanceId>
  <progress>10000</progress>
  <resourceGroupId>4</resourceGroupId>
  <beginTime>1677825909000</beginTime>
  <endTime>1677825909000</endTime>
  <recoveryInstanceName>i-wdlsfgolpo9*******</recoveryInstanceName>
 <organizationId>12</organizationId>
 <taskType>REGULAR</taskType>
 <deleted>0</deleted>
 <regionId>cn-hangzhou*****</regionId>
 <progress>30</progress>
 <ctime>1677825909000</ctime>
 <taskName>ECS恢复</taskName>
 <beginTime>1677825909000</beginTime>
 <endTime>1677825909000</endTime>
 <taskId>d202309c-0c20-44e2-9e02-bacf******</taskId>
 <status>SUCCESS</status>
</recoveryTaskInner>
```

##### DisableRecoveryTask

灾备管理中心

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| TaskId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 恢复任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of recoveryTask is null. | 错误提示信息。 |
| errorCode | String | RecoveryTaskIsNull | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -status | String | STOPPED | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 STOPPING：停止中 PART FINISHED：部分成功 _ |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DisableRecoveryTask &TaskId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"STOPPED",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******"
 },
 "ErrorCode":"RecoveryTaskIsNull",
 "ErrorMessage":"The parameter of recoveryTask is null.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>STOPPED</Status>
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
</RecoveryTaskInner> <ErrorCode>RecoveryTaskIsNull</ErrorCode> <ErrorMessage>The parameter of recoveryTask is null.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### EnableRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 灾备管理中心

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| TaskId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 恢复任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of recoveryTask is null. | 错误提示信息。 |
| errorCode | String | RecoveryTaskIsNull | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |

**示例**

灾备管理中心请求示例

```
http(s)://[Endpoint]/?Action=EnableRecoveryTask &TaskId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******"
 },
 "ErrorCode":"RecoveryTaskIsNull",
 "ErrorMessage":"The parameter of recoveryTask is null.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
</RecoveryTaskInner> <ErrorCode>RecoveryTaskIsNull</ErrorCode> <ErrorMessage>The parameter of recoveryTask is null.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### RestartRecoveryTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Resource GroupId | Integ er | Query | 否 | 33 | 资源集ID |
| TaskId | Strin g | Query | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 恢复任务ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of recoveryTask is null. | 错误提示信息。 |
| errorCode | String | RecoveryTaskIsNull | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务详情。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=RestartRecoveryTask &TaskId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******"
 },
 "ErrorCode":"RecoveryTaskIsNull",
 "ErrorMessage":"The parameter of recoveryTask is null.",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
</RecoveryTaskInner> <ErrorCode>RecoveryTaskIsNull</ErrorCode> <ErrorMessage>The parameter of recoveryTask is null.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

##### DescribeAvailableRecoveryTime

调用DescribeAvailableRecoveryTime查看RDS可恢复时间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 12 | 资源集ID |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | 是 | rm-ad23dsflkj43******* | 实例ID。 |
| Location | Strin g | Query | 是 | REMOTE | 选取恢复位置。 LOCAL：本地 REMOTE：异地 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTimeI nner | Struct |  | 返回结果。 |
| -instanceId | String | rm- ad2343er******* | 实例ID。 |
| - recoveryBegin Time | Long | 1677825909000 | 恢复起始时间。 |
| - recoveryEndTi me | Long | 1677825909000 | 恢复截止时间。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=DescribeAvailableRecoveryTime &Location=REMOTE
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTimeInner":{
  "RecoveryEndTime":1677825909000,
  "RecoveryBeginTime":1677825909000,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTimeInner>
 <RecoveryEndTime>1677825909000</RecoveryEndTime>
 <RecoveryBeginTime>1677825909000</RecoveryBeginTime>
 <InstanceId>rm-ad2343er*******</InstanceId>
</RecoveryTimeInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

### VMware备份、恢复、迁移

#### CreateVmwareBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 31 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| PlanName | Strin g | Query | 是 | VMware备份 | 备份计划名称。 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| BackupIns tance | Json | Body | 是 | { "datacenterName":"data center", "instanceName":"smj an _ 23 x86", _ "clusterName":"asrbr cl _ uster", "vcenterId":"90c83761- 148b-4aa9-968c- 4******", "serverId":"svr- 00001xuhgg******" } | 备份实例信息。 datacenterName：虚拟机所属数据中心名称。 instanceName：虚拟机名称。 clusterName：虚拟机所属集群名称。 vcenterId：vCenter ID。 serverId：服务ID。 |
| BackupPol icy | Json | Body | 是 | { "preferredBackupPeriod" :[ 1 ], "preferredBackupTime": 1669800995050, "vaultId":"952dab58- c8a1-4868-89b4- 67*****", "backupRetentionPeriod ":7 } | 备份策略。 preferredBackupPerio d：备份周期，取值为整数，例如取值为1表示每天备份一次。 preferredBackupTime ：备份执行时间。 backupRetentionPerio d：备份保留时长，单位为天。 vaultId：备份仓库ID。 |
| Increment alPolicy | Json | Body | 否 | { "preferredBackupPeriod" :[ 1 ], "preferredBackupTime": 1669800995050, "vaultId":"952dab58- c8a1-4868-89b4- 67*****", "backupRetentionPeriod ":7 } | 增量备份策略 |

灾备管理中心

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| backupPlanInn er | Struct |  | 备份计划信息。 |
| -planId | String | 108e46be-c321- 4694-9c2d- b478b******* | 备份计划ID。 |
| -planName | String | VMware备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED：已删除 DELETING：删除中 |
| -backupType | String |  | 备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -instanceType | String | VMware | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 3 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-********* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例灾备管理中心

```json
http(s)://[Endpoint]/?Action=CreateVmwareBackupPlan &ClientToken=123e4567********55440000 &PlanName=VMware备份
        "datacenterName":"datacenter",
        "instanceName":"smj_an23_x86",
        "clusterName":"asrbr_cluster",
        "vcenterId":"90c83761-148b-4aa9-968c-4******",
        "serverId":"svr-00001xuhgg******"
    }
```

`],`

```json
        "preferredBackupTime":1669800995050,
        "vaultId":"952dab58-c8a1-4868-89b4-67*****",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
  "Status":"RUNNING",
  "OrganizationName":"test",
  "ResourceGroupId":3,
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"108e46be-c321-4694-9c2d-b478b*******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*********",
  "PlanName":"VMware备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
  "InstanceType":"VMware",
  "ResourceGroupName":"ResourceSet(test)"
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <ResourceGroupId>3</ResourceGroupId>
 <CreatorId>5612</CreatorId>
 <PlanId>108e46be-c321-4694-9c2d-b478b*******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*********</Creator>
 <PlanName>VMware备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
 <ResourceGroupName>ResourceSet(test)</ResourceGroupName>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateVmwareLocalRecovery

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 41 | 资源集ID |

灾备管理中心

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | VMware本地恢复 | 恢复任务名称。 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":2, "path":{ "computeResourceName ":"asrbrDatacenter/host/ asrbrCluster", "locationName":"asrbrD atacenter", "datacenterName":"asrb rDatacenter", "resourcePoolId":"resgro up***", "networkMoReference":" network*****", "datastoreName":"asrbr Datacenter/host/asrbrCl uster/Resources/Datasto re***", "datastoreId":"datastore -*****", "folderId":"group-******" }, "instanceId":"52e53ab8- 2f7d-0385-f662- 1e******", "instanceName":"smj an _ 23*****", "vcenterId":"90c83761- 148b-4aa9-968c- 4fb8********", "serverId":"svr- 00001xuhgga*********" } } | 恢复任务实例信息。 recordId：备份记录ID。 instanceId：备份虚拟机实例ID。 instanceName：备份虚拟机实例名称。 vcenterId：添加的 vCenter ID。 serverId：添加的 vcenter服务ID。 path：虚拟机恢复地址信息。 computeResourceNa me：计算资源（集群） 名称。 locationName：数据中心名称。 datacenterName：数据中心名称。 resourcePoolId：资源池ID。 networkMoReference ：网络模块。 datastoreName：存储名称。 datastoreId：存储ID。 folderId：目录ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | VMware本地恢复 | 恢复任务名称。 |
| -instanceType | String | VMware | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED：停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org-********* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=CreateVmwareLocalRecovery &ClientToken=123e4567********55440000
```

`&TaskName=VMware`本地恢复

```json
        "recordId":2,
        "path":{
            "computeResourceName":"asrbrDatacenter/host/asrbrCluster",
            "locationName":"asrbrDatacenter",
            "datacenterName":"asrbrDatacenter",
            "resourcePoolId":"resgroup***",
            "networkMoReference":"network*****",
            "datastoreName":"asrbrDatacenter/host/asrbrCluster/Resources/Datastore***",
            "datastoreId":"datastore-*****",
            "folderId":"group-******"
        },
        "instanceId":"52e53ab8-2f7d-0385-f662-1e******",
        "instanceName":"smj_an23*****",
        "vcenterId":"90c83761-148b-4aa9-968c-4fb8********",
        "serverId":"svr-00001xuhgga*********"
    }
}
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*********",
  "InstanceNum":1,
```

`"TaskName":"VMware`本地恢复`",`

```json
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*********</Creator>
 <TaskName>VMware本地恢复</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### CreateVmwareRestoreToCloud

调用CreateVmwareRestoreToCloud创建VMware恢复上云。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567********55440 000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| TaskName | Strin g | Query | 是 | VMware恢复上云 | 恢复任务名称。 |

| 备份管理平台开 | 发指南·A | PI参考 |  |  | 灾备管理中心 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| Descriptio n | Strin g | Body | 否 | test | 描述 |
| RecoveryI nstance | Json | Body | 是 | { "recordId":2, "securityGroupId":"sg- q1f01emdyy96*****", "organizationId":4, "instanceId":"52e53ab8- 2f7d-0385-f662- 1e9******", "classic":"ecs.sn2ne.larg e", "instanceName":"smj an _ 23***", "vSwitchId":"vsw- q1flt5ccjklh38******", "vpcId":"vpc- q1fxs39dm3*****", "restoreHostName":"rest oretoecs", "resourceGroupId":3, "diskCategory":"cloud ef _ ficiency", "recoveryInstanceName" :"restoretoecs" } | 恢复任务实例信息。 recordId：备份记录ID。 securityGroupId：安全组ID。 organizationId：组织 ID。 instanceId：备份实例 ID。 classic：ECS实例规格。 instanceName：虚拟机名称。 vSwitchId：交换机ID。 vpcId：专有网络ID。 restoreHostName：主机名称。 resourceGroupId：资源集ID。 diskCategory：云盘类型，取值 cloud efficiency为高效 _ 云盘，cloud pperf为高 _ 性能云盘，cloud ssd为 _ SSD盘，cloud sperf为 _ 普通性能云盘。 recoveryInstanceNam e：恢复实例名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| recoveryTaskI nner | Struct |  | 恢复任务信息。 |
| -taskId | String | d202309c-0c20- 44e2-9e02- bacf****** | 恢复任务ID。 |
| -taskName | String | VMware恢复上云 | 恢复任务名称。 |
| -instanceType | String | VMware | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| -status | String | RECOVERYING | 恢复任务状态。 NOT RUN：未运行 _ RECOVERYING：恢复中 FAILED：恢复失败 SUCCESS：成功 STOPPED： 停止 PART FINISHED：部分成功 _ |
| -instanceNum | Integer | 1 | 实例数量。 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -recoveryType | String |  | 恢复类型。当实例类型为ECS时显示。 ECS FILE：ECS文件。 _ ECS DISK：ECS云盘。 _ |
| -regionId | String | cn-hangzhou- ******** | 区域ID。 |
| -regionName | String | cn-hangzhou- ******** | 区域名称。 |
| -creator | String | ascm-org-********* | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -deleted | Integer | 0 | 是否删除。 0：否。 1：是。 |
| -beginTime | Long | 1677825909000 | 开始时间，单位毫秒（ms）。 |
| -endTime | Long | 1677825909000 | 结束时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateVmwareRestoreToCloud &ClientToken=123e4567********55440000
```

`&TaskName=VMware`恢复上云

```json
        "recordId":2,
        "securityGroupId":"sg-q1f01emdyy96*****",
        "organizationId":4,
        "instanceId":"52e53ab8-2f7d-0385-f662-1e9******",
        "classic":"ecs.sn2ne.large",
        "instanceName":"smj_an23***",
        "vSwitchId":"vsw-q1flt5ccjklh38******",
        "vpcId":"vpc-q1fxs39dm3*****",
        "restoreHostName":"restoretoecs",
        "resourceGroupId":3,
        "diskCategory":"cloud_efficiency",
    }
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "RecoveryTaskInner":{
  "Status":"RECOVERYING",
  "OrganizationName":"test",
  "RecoveryType":"",
  "TaskId":"d202309c-0c20-44e2-9e02-bacf******",
  "EndTime":1677825909000,
  "CreatorId":5612,
  "BeginTime":1677825909000,
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-*********",
  "InstanceNum":1,
```

`"TaskName":"VMware`恢复上云`",`

```json
  "RegionName":"cn-hangzhou-********",
  "Ctime":1677825909000,
  "RegionId":"cn-hangzhou-********",
  "Deleted":0,
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <RecoveryTaskInner>
 <Status>RECOVERYING</Status>
 <OrganizationName>test</OrganizationName>
 <RecoveryType  />
 <TaskId>d202309c-0c20-44e2-9e02-bacf******</TaskId>
 <EndTime>1677825909000</EndTime>
 <CreatorId>5612</CreatorId>
 <BeginTime>1677825909000</BeginTime>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-*********</Creator>
 <TaskName>VMware恢复上云</TaskName>
 <RegionName>cn-hangzhou-********</RegionName>
 <Ctime>1677825909000</Ctime>
 <RegionId>cn-hangzhou-********</RegionId>
 <Deleted>0</Deleted>
</RecoveryTaskInner> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVmwareBackupPlanList

调用DescribeVmwareBackupPlanList查看VMware备份计划列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| PlanName | Strin g | Query | 否 | VMware备份 | 备份计划名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planName | String | VMware备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |
| -backupType | String |  | ECS备份类型。当实例类型为ECS时显示。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
| -instanceType | String | VMware | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 4 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |
| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 10 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVmwareBackupPlanList
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "Status":"RUNNING",
  "OrganizationName":"test",
  "ResourceGroupId":4,
  "VaultName":"backup-vault",
  "CreatorId":5612,
  "PlanId":"d202309c-0c20-44e2-9e02-bacf******",
  "Mtime":1677825909000,
  "OrganizationId":12,
  "Creator":"ascm-org-********",
  "PlanName":"VMware备份",
  "VaultId":"c59f9c6b-effd-4d5c-841b-c14d9****",
  "NextBackupTime":1677825909000,
  "RegionName":"cn-hangzhou******",
  "Ctime":1677825909000,
  "BackupType":"",
  "LastResult":"SUCCESS",
  "RegionId":"cn-hangzhou******",
  "InstanceType":"VMware",
  "ResourceGroupName":"ResourceSet(test)"
 },
 "ErrorCode":"BackupPlanNotFound",
 "ErrorMessage":"Not Found BackupPlan for current operate.",
 "TotalSize":10,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <Status>RUNNING</Status>
 <OrganizationName>test</OrganizationName>
 <ResourceGroupId>4</ResourceGroupId>
 <CreatorId>5612</CreatorId>
 <PlanId>d202309c-0c20-44e2-9e02-bacf******</PlanId>
 <Mtime>1677825909000</Mtime>
 <OrganizationId>12</OrganizationId>
 <Creator>ascm-org-********</Creator>
 <PlanName>VMware备份</PlanName>
 <VaultId>c59f9c6b-effd-4d5c-841b-c14d9****</VaultId>
 <NextBackupTime>1677825909000</NextBackupTime>
 <RegionName>cn-hangzhou******</RegionName>
 <Ctime>1677825909000</Ctime>
 <LastResult>SUCCESS</LastResult>
 <RegionId>cn-hangzhou******</RegionId>
 <ResourceGroupName>ResourceSet(test)</ResourceGroupName>
</Data> <ErrorMessage>Not Found BackupPlan for current operate.</ErrorMessage> <TotalSize>10</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVmwareBackupPlan

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Quer y | 否 | 1 | 组织ID |
| ResourceG roupId | Integ er | Quer y | 否 | 2 | 资源集ID |

灾备管理中心

| PlanId | Strin g | Quer y | 是 | d202309c-0c20-44e2- 9e02-bacf****** | 备份计划ID。 |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | Not Found BackupPlan for current operate. | 错误提示信息。 |
| errorCode | String | BackupPlanNotFou nd | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| data | Struct |  | 返回数据。 |
| - backupPolicyLi st | Array |  | 备份策略集合 |
| -- preferredBack upPeriod | String | 2 | 备份周期。 RDS、PolarDB-X：["SUNDAY"、 "MONDAY"]，每周日、周三备份其他产品：["2"]，2天或小时 |
| -- preferredBack upPeriodFull | String | 7 | 全量备份备份周期。 |
| -- backupRetenti onPeriod | Integer | 14 | 备份保存时长。单位：天。 |

灾备管理中心

| --policyType | String | INCREMENTAL | 备份策略类型。 全量备份：FULL 增量备份：INCREMENTAL 全量+增量：FULL INCREMENTAL _ |
|---|---|---|---|
| -- preferredBack upTime | String | 1677825909000 | 备份执行时间，UTC时间。 RDS、PolarDB-X：10:00Z-11:00Z(UTC时间) 其他：1677576600519，单位毫秒（ms） |
| -- preferredBack upType | String | BY TIME _ | 备份保存类型。 BY TIME：按时间。 _ |
| -- preferredCycle Type | String | BY INTERVAL _ | 备份间隔。 BY HOUR：按小时 _ BY INTERVAL：按天 _ |
| --vaultId | String | d202309c-0c20- 44e2-9e02- | 仓库ID |
| --vaultName | String | ASRBR | 仓库名称 |
| -planId | String | d202309c-0c20- 44e2-9e02- bacf****** | 备份计划ID。 |
| -planName | String | VMware备份 | 备份计划名称。 |
| -status | String | RUNNING | 备份计划状态。 NOT RUN：没有运行 _ CREATING：创建中 CREATED：创建成功 STARTING：启动中 RUNNING：运行中 BACKING UP：备份中 _ STOPPING：停止中 STOPPED：已停止 DELETED： 已删除 DELETING：删除中 |

灾备管理中心

| -backupType | String |  | ECS备份类型。当实例类型为ECS时展示。 ECS FILE：ECS文件 _ ECS DISK：ECS云盘 _ |
|---|---|---|---|
| -instanceType | String | VMware | 实例类型。包括OSS、ECS、NAS、ADB、 RDS、PolarDB-X、MaxCompute、 Elasticsearch及VMware。 |
| - nextBackupTi me | Long | 1677825909000 | 下次备份时间，单位毫秒（ms）。 |
| -lastResult | String | SUCCESS | 最近一次备份结果。 NOT RUN：未运行 _ BACKUPING：运行中 SUCCESS：成功 PART FINISHED：部分完成 _ FAILED：失败 MIGRATING：迁移中 BLOCKED：已阻塞 |
| -organizationId | Integer | 12 | 组织ID。 |
| - organizationN ame | String | test | 组织名称。 |
| -regionId | String | cn-hangzhou****** | 区域ID。 |
| -regionName | String | cn-hangzhou****** | 区域名称。 |
| - resourceGroup Id | Integer | 4 | 资源集ID。 |
| - resourceGroup Name | String | ResourceSet(test) | 资源集名称。 |
| -creator | String | ascm-org-******** | 创建人。 |
| -creatorId | Integer | 5612 | 创建人ID。 |

灾备管理中心

| -ctime | Long | 1677825909000 | 创建时间，单位毫秒（ms）。 |
|---|---|---|---|
| -mtime | Long | 1677825909000 | 修改时间，单位毫秒（ms）。 |
| -instance | Struct |  | 备份实例。 |
| --instanceId | String | vm- as312wer1****** | 实例ID。 |
| -- instanceName | String | vm- as312wer1****** | 实例名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVmwareBackupPlan &PlanId=d202309c-0c20-44e2-9e02-bacf******
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":20,
 "data":{
  "creator":"ascm-org-********",
  "resourceGroupName":"ResourceSet(test)",
  "organizationName":"test",
  "lastResult":"SUCCESS",
  "instanceType":"VMware",
  "regionName":"cn-hangzhou******",
  "nextBackupTime":1677825909000,
  "creatorId":5612,
  "planName":"VMware备份",
  "mtime":1677825909000,
  "backupType":"",
  "organizationId":12,
  "regionId":"cn-hangzhou******",
   "preferredBackupPeriod":"2",
   "preferredBackupTime":"1677825909000",
   "vaultName":"ASRBR",
   "vaultId":"d202309c-0c20-44e2-9e02-",
   "policyType":"INCREMENTAL",
   "backupRetentionPeriod":14,
   "preferredBackupPeriodFull":"7",
   "preferredCycleType":"BY_INTERVAL",
  },
  "ctime":1677825909000,
  "planId":"d202309c-0c20-44e2-9e02-bacf******",
  "resourceGroupId":4,
   "instanceId":"vm-as312wer1******",
  },
  "status":"RUNNING"
 },
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"Not Found BackupPlan for current operate.",
}
```

`XML` 格式灾备管理中心

```xml
<code>200</code> <cost>20</cost> <data>
 <creator>ascm-org-********</creator>
 <resourceGroupName>ResourceSet(test)</resourceGroupName>
 <organizationName>test</organizationName>
 <lastResult>SUCCESS</lastResult>
 <regionName>cn-hangzhou******</regionName>
 <nextBackupTime>1677825909000</nextBackupTime>
 <creatorId>5612</creatorId>
 <planName>VMware备份</planName>
 <mtime>1677825909000</mtime>
 <organizationId>12</organizationId>
 <regionId>cn-hangzhou******</regionId>
  <preferredBackupPeriod>2</preferredBackupPeriod>
  <preferredBackupTime>1677825909000</preferredBackupTime>
  <policyType>INCREMENTAL</policyType>
  <backupRetentionPeriod>14</backupRetentionPeriod>
  <preferredBackupPeriodFull>7</preferredBackupPeriodFull>
  <preferredCycleType>BY_INTERVAL</preferredCycleType>
  <preferredBackupType>BY_TIME</preferredBackupType>
 <ctime>1677825909000</ctime>
 <planId>d202309c-0c20-44e2-9e02-bacf******</planId>
 <resourceGroupId>4</resourceGroupId>
  <instanceId>vm-as312wer1******</instanceId>
  <instanceName>vm-as312wer1******</instanceName>
 <status>RUNNING</status>
</data> <requestId>C8B26B44-0189-443E-9816-*******</requestId> <success>true</success> <errorMessage>Not Found BackupPlan for current operate.</errorMessage>
```

### vCenter管理

#### AddVCenter

添加vCenter

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 灾备管理中心

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| ClientToke n | Strin g | Query | 是 | 123e4567-e89b-12d3- a456-426655440000 | 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。 ClientToken只支持ASCII 字符，且不能超过64个字符。 |
| Host | Strin g | Query | 是 | 192.168.*.* | vCenter主机地址。 |
| Password | Strin g | Body | 是 | *********** | vCenter登录用户名。 |
| UserName | Strin g | Body | 是 | admin********* | vCenter登录密码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 32 | 接口耗时，单位毫秒（ms）。 |
| vcenterInfo | Struct |  | vCenter信息。 |
| -host | String | 192.168.*.* | vCenter主机地址。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -serverId | String | svr- 00001xuhggafmr** ****** | vCenter服务ID。 |
| -vCenterId | String | 90c83761-148b- 4aa9-968c- 4fb84***** | vCenter ID。 |
| -serverStatus | String | ACTIVE | vCenter服务状态。 |
| -userName | String | admin********* | vCenter登录用户名。 |

**示例**

请求示例

```
&ClientToken=123e4567-e89b-12d3-a456-426655440000 &Host=192.168.*.* &Password=*********** &UserName=admin*********
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "path":"/asrbr/*/*",
 "code":"200",
 "cost":32,
 "requestId":"C8B26B44-0189-443E-9816-*******",
 "success":true,
 "errorMessage":"failed",
 "errorCode":"403",
 "vcenterInfo":{
  "vCenterId":"90c83761-148b-4aa9-968c-4fb84*****",
  "serverStatus":"ACTIVE",
  "host":"192.168.*.*",
  "userName":"admin*********",
  "serverId":"svr-00001xuhggafmr********"
 }
}
```

`XML` 格式灾备管理中心

```xml
<Path>/asrbr/*/*</Path><RequestId>C8B26B44-0189-443E-9816-*******</RequestId><VcenterIn fo><-vCenterId>90c83761-148b-4aa9-968c-4fb84*****</-vCenterId><-ServerStatus>ACTIVE</-S erverStatus><-Host>192.168.*.*</-Host><-ServerId>svr-00001xuhggafmr********</-ServerId> <-UserName>admin*********</-UserName></VcenterInfo><ErrorCode>403</ErrorCode><ErrorMess age>failed</ErrorMessage><Code>200</Code><Cost>32</Cost><Success>true</Success>
```

#### ModifyvCenterInfo

修改vCenter信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 21 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 32 | 资源集ID |
| VCenterId | Strin g | Query | 是 | 98357fa5-****-4bd8- 9787-3e614cc**** | VCenterID |
| Host | Strin g | Body | 是 | 192.168.*.* | vCenter地址。 |
| Password | Strin g | Body | 是 | ************ | vCenter访问密码。 |
| UserName | Strin g | Body | 是 | admin********* | vCenter用户名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The vcenter not found. | 错误提示信息。 |
| errorCode | String | VcenterNotExists | 错误码。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| data | String | success | 返回结果。 |

**示例**

请求示例

```
&VCenterId=98357fa5-****-4bd8-9787-3e614cc**** &Host=192.168.*.* &Password=************ &UserName=admin*********
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":"success",
 "ErrorCode":"VcenterNotExists",
 "ErrorMessage":"The vcenter not found.",
 "Code":"200",
 "Cost":"20",
 "Success":"true"
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>success</Data> <ErrorCode>VcenterNotExists</ErrorCode> <ErrorMessage>The vcenter not found.</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DeleteVCenter

**请求头**

灾备管理中心该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 32 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 23 | 资源集ID |
| VCenterId | Strin g | Query | 是 | 90c83761-148b-4aa9- 968c-4fb84***** | VCenterID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | failed | 错误提示信息。 |
| errorCode | String | 403 | 错误码。 403：没有权限。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| data | Struct |  | 返回结果。 |
| -result | Boolean | true | 删除结果。 true：成功 false：失败 |

**示例**

请求示例

```
&vCenterId=90c83761-148b-4aa9-968c-4fb84*****
```

&公共请求参数灾备管理中心正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":{
  "Result":true
 },
 "ErrorCode":"403",
 "ErrorMessage":"failed",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <Result>true</Result>
</Data> <ErrorCode>403</ErrorCode> <ErrorMessage>failed</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterComputeResourceList

调用DescribeVCenterComputeResourceList查看vCenter计算资源列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 2 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 1 | 资源集ID |
| VCenterId | Strin g | Query | 是 | 98357fa5-bd33-4bd8- 9787-3e614cc1dbad | VCenterID |
| DataCent erPath | Strin g | Query | 是 | asrbrDatacenter | 数据中心地址。 |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| purpose | Strin g | Query | 否 | restore | 查询目的 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of vcenterId is empty. | 错误提示信息。 |
| errorCode | String | VcenterIdIsEmpty | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |
| data | Struct |  | 返回数据。 |
| -inventories | Array |  | 资源列表。 |
| --moId | String | domain-c8 | 模块ID。 |
| -- computeResou rceName | String | asrbr集群 | 计算资源名称。 |
| -- computeResou rcePath | String | asrbrDatacenter/ho st/asrbr集群 | 计算资源路径。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --type | String | ClusterComputeRe source | 资源类型。 |
| --properties | Struct |  | 属性信息。 |
| ---hasHost | Boolean | true | 是否有地址。 |
| --- resourcePoolId | String | resgroup-***** | 资源池ID。 |
| -totalCount | String | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVCenterComputeResourceList &VCenterId=98357fa5-bd33-4bd8-9787-3e614cc1dbad
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "TotalCount":"50",
  "-Inventories":{
   "Type":"ClusterComputeResource",
   "ComputeResourceName":"asrbr集群",
   "MoId":"domain-c8",
   "ComputeResourcePath":"asrbrDatacenter/host/asrbr集群",
   "--Properties":{
    "HasHost":true,
    "ResourcePoolId":"resgroup-*****"
   }
  }
 },
 "ErrorCode":"VcenterIdIsEmpty",
 "ErrorMessage":"The parameter of vcenterId is empty.",
 "TotalSize":50,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

灾备管理中心 `XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <TotalCount>50</TotalCount>
 <-Inventories>
  <Type>ClusterComputeResource</Type>
  <ComputeResourceName>asrbr集群</ComputeResourceName>
  <MoId>domain-c8</MoId>
  <ComputeResourcePath>asrbrDatacenter/host/asrbr集群</ComputeResourcePath>
  <--Properties>
   <HasHost>true</HasHost>
   <ResourcePoolId>resgroup-*****</ResourcePoolId>
  </--Properties>
 </-Inventories>
</Data> <ErrorCode>VcenterIdIsEmpty</ErrorCode> <ErrorMessage>The parameter of vcenterId is empty.</ErrorMessage> <TotalSize>50</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterDataCenterList

调用DescribeVCenterDataCenterList查看vCenter数据中心列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| VCenterId | Strin g | Query | 是 | v-test12s**** | VCenter ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |

|  | 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The parameter of vcenterId is empty. | 错误提示信息。 |
| errorCode | String | VcenterIdIsEmpty | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 5 | 总数据量。 |
| data | Struct |  | 返回数据。 |
| -inventories | Array |  | 资源列表。 |
| --moId | String | datacenter-3 | 模块ID。 |
| -- dataCenterPat h | String | asrbrDatacenter | 数据中心地址。 |
| -- dataCenterNa me | String | asrbrDatacenter | 数据中心名称。 |
| --type | String | Datacenter | 资源类型。 |
| --properties | Struct |  | 属性信息。 |
| ---folderId | String | group-v4 | 文件夹ID。 |
| ---hasHost | Boolean | false | 是否有地址。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -totalCount | String | 5 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVCenterDataCenterList &VCenterId=v-test12s****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "TotalCount":"5",
  "-Inventories":{
   "Type":"Datacenter",
   "DataCenterPath":"asrbrDatacenter",
   "MoId":"datacenter-3",
   "DataCenterName":"asrbrDatacenter",
   "--Properties":{
    "FolderId":"group-v4",
    "HasHost":false
   }
  }
 },
 "ErrorCode":"VcenterIdIsEmpty",
 "ErrorMessage":"The parameter of vcenterId is empty.",
 "TotalSize":5,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <TotalCount>5</TotalCount>
 <-Inventories>
  <Type>Datacenter</Type>
  <DataCenterPath>asrbrDatacenter</DataCenterPath>
  <MoId>datacenter-3</MoId>
  <DataCenterName>asrbrDatacenter</DataCenterName>
  <--Properties>
   <FolderId>group-v4</FolderId>
   <HasHost>false</HasHost>
  </--Properties>
 </-Inventories>
</Data> <ErrorCode>VcenterIdIsEmpty</ErrorCode> <ErrorMessage>The parameter of vcenterId is empty.</ErrorMessage> <TotalSize>5</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| PageNum | Integ er | Query | 否 | 1 | 分页页数。 |
| PageSize | Integ er | Query | 否 | 10 | 每页返回的数据个数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 返回数据。 |
| -host | String | 192.168.*.* | vCenter地址。 |
| -serverId | String | svr- 00001xuhggafmr** ***** | vCenter服务ID。 |
| -serverStatus | String | ACTIVE | vCenter服务状态。 UNKNOWN：未知状态 ACTIVE：活跃状态 |
| -userName | String | admin********* | vCenter登录用户名。 |
| -vCenterId | String | 90c83761********4 44daa69 | vCenter ID。 |
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The vcenter not found. | 错误提示信息。 |
| errorCode | String | VcenterNotExists | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例灾备管理中心

```
http(s)://[Endpoint]/?Action=DescribeVCenterList
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "vCenterId":"90c83761********444daa69",
  "ServerId":"svr-00001xuhggafmr*******",
  "UserName":"admin*********",
  "ServerStatus":"ACTIVE",
  "Host":"192.168.*.*"
 },
 "ErrorCode":"VcenterNotExists",
 "ErrorMessage":"The vcenter not found.",
 "TotalSize":50,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <vCenterId>90c83761********444daa69</vCenterId>
 <ServerId>svr-00001xuhggafmr*******</ServerId>
 <UserName>admin*********</UserName>
 <ServerStatus>ACTIVE</ServerStatus>
 <Host>192.168.*.*</Host>
</Data> <ErrorCode>VcenterNotExists</ErrorCode> <ErrorMessage>The vcenter not found.</ErrorMessage> <TotalSize>50</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterNetworkList

调用DescribeVCenterNetworkList查看vCenter网络列表。

**请求头**

灾备管理中心该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 1 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 2 | 资源集ID |
| VCenterId | Strin g | Query | 是 | 0ac81caa170858459101 27329e0034 | VCenterID |
| ClusterNa mePath | Strin g | Query | 是 | asrbrDatacenter/host/as rbr集群 | vCenter集群地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The vcenter not found. | 错误提示信息。 |
| errorCode | String | VcenterNotExists | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 1 | 总数据量。 |
| data | Struct |  | 返回数据。 |
| -inventories | Array |  | 资源列表。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- networkMoRef erence | String | network-16 | 网络模块。 |
| --name | String | VM Network | 网络名称。 |
| --path | String | asrbrDatacenter/ho st/asrbr集群/Resources/VM Network | 网络地址。 |
| --type | String | Network | 资源类型。 |
| --properties | Struct |  | 属性信息。 |
| ---hasHost | Boolean | true | 是否有地址。 |
| ---capacity | String | 3840506068992 | 存储规格。 |
| ---freeSpace | String | 2294717349888 | 剩余空间。 |
| -totalCount | String | 1 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVCenterNetworkList &VCenterId=0ac81caa17085845910127329e0034 &ClusterNamePath=asrbrDatacenter/host/asrbr集群
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "TotalCount":"1",
  "-Inventories":{
   "Path":"asrbrDatacenter/host/asrbr集群/Resources/VM Network",
   "Type":"Network",
   "NetworkMoReference":"network-16",
   "Name":"VM Network",
   "--Properties":{
    "Capacity":"3840506068992",
    "FreeSpace":"2294717349888",
    "HasHost":true
   }
  }
 },
 "ErrorCode":"VcenterNotExists",
 "ErrorMessage":"The vcenter not found.",
 "TotalSize":1,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <TotalCount>1</TotalCount>
 <-Inventories>
  <Path>asrbrDatacenter/host/asrbr集群/Resources/VM Network</Path>
  <Type>Network</Type>
  <NetworkMoReference>network-16</NetworkMoReference>
  <Name>VM Network</Name>
  <--Properties>
   <Capacity>3840506068992</Capacity>
   <FreeSpace>2294717349888</FreeSpace>
   <HasHost>true</HasHost>
  </--Properties>
 </-Inventories>
</Data> <ErrorCode>VcenterNotExists</ErrorCode> <ErrorMessage>The vcenter not found.</ErrorMessage> <TotalSize>1</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterRegisterCode

调用DescribeVCenterRegisterCode查看vCenter注册码。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 21 | 资源集ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |

| 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | InternalFailure | 错误提示信息。 |
| errorCode | String | 500 | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| data | Struct |  | 返回数据。 |
| -expireTime | Long | 1677825909000 | 过期时间，单位毫秒（ms）。 |
| -rabbitMqHost | String | cn-hangzhou.hbr- mq****** | 注册码获取地址。 |
| -rabbitMqPort | Long | 5628 | 注册码获取端口。 |
| -token | String | 00YN***** | 注册码。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVCenterRegisterCode
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "Data":{
  "RabbitMqHost":"cn-hangzhou.hbr-mq******",
  "Token":"00YN*****",
  "ExpireTime":1677825909000,
  "RabbitMqPort":5628
 },
 "ErrorCode":"500",
 "ErrorMessage":"InternalFailure",
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <Data>
 <RabbitMqHost>cn-hangzhou.hbr-mq******</RabbitMqHost>
 <Token>00YN*****</Token>
 <ExpireTime>1677825909000</ExpireTime>
 <RabbitMqPort>5628</RabbitMqPort>
</Data> <ErrorCode>500</ErrorCode> <ErrorMessage>InternalFailure</ErrorMessage> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

#### DescribeVCenterStorageResourceList

调用DescribeVCenterStorageResourceList查看vCenter存储资源列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Organizati onId | Integ er | Query | 否 | 12 | 组织ID |
| Resource GroupId | Integ er | Query | 否 | 13 | 资源集ID |
| VCenterId | Strin g | Query | 是 | 0ac81caa170858459101 27329e0034 | VCenterID |

| 灾备管理中心 |  |  |  | 备 | 份管理平台开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterNa mePath | Strin g | Query | 是 | asrbrDatacenter/host/as rbr集群 | vCenter集群地址。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| success | Boolean | true | 本次请求是否成功。 |
| code | String | 200 | 状态码。 200：调用正常。 |
| errorMessage | String | The vcenter not found. | 错误提示信息。 |
| errorCode | String | VcenterNotExists | 错误码。 |
| path | String | /asrbr/*/* | 请求路径。 |
| cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |
| pageNum | Integer | 1 | 分页页数。 |
| pageSize | Integer | 10 | 每页返回的数据个数。 |
| totalSize | Integer | 1 | 总数据量。 |
| data | Struct |  | 返回数据。 |
| -inventories | Array |  | 资源列表。 |
| --datastoreId | String | datastore-14 | 存储ID。 |
| --name | String | datastore | 存储名称。 |
| -- datastoreNam e | String | asrbrDatacenter/ho st/asrbr集群/Resources/datas tore | 存储路径。 |

灾备管理中心

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --type | String | Datastore | 资源类型。 |
| --properties | Struct |  | 属性信息。 |
| ---hasHost | Boolean | false | 是否有地址。 |
| ---capacity | String | 3840506068992 | 存储规格，单位：byte。 |
| ---freeSpace | String | 2294717349888 | 剩余空间，单位：byte。 |
| -totalCount | String | 1 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeVCenterStorageResourceList &VCenterId=0ac81caa17085845910127329e0034 &ClusterNamePath=asrbrDatacenter/host/asrbr集群
```

&公共请求参数正常返回示例 `JSON` 格式灾备管理中心

```json
{
 "Path":"/asrbr/*/*",
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "Data":{
  "TotalCount":"1",
  "-Inventories":{
   "Type":"Datastore",
   "DatastoreId":"datastore-14",
   "DatastoreName":"asrbrDatacenter/host/asrbr集群/Resources/datastore",
   "Name":"datastore",
   "--Properties":{
    "Capacity":"3840506068992",
    "FreeSpace":"2294717349888",
    "HasHost":false
   }
  }
 },
 "ErrorCode":"VcenterNotExists",
 "ErrorMessage":"The vcenter not found.",
 "TotalSize":1,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <Data>
 <TotalCount>1</TotalCount>
 <-Inventories>
  <Type>Datastore</Type>
  <DatastoreId>datastore-14</DatastoreId>
  <DatastoreName>asrbrDatacenter/host/asrbr集群/Resources/datastore</DatastoreName>
  <Name>datastore</Name>
  <--Properties>
   <Capacity>3840506068992</Capacity>
   <FreeSpace>2294717349888</FreeSpace>
   <HasHost>false</HasHost>
  </--Properties>
 </-Inventories>
</Data> <ErrorCode>VcenterNotExists</ErrorCode> <ErrorMessage>The vcenter not found.</ErrorMessage> <TotalSize>1</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

### 存储池管理

#### DescribeStoragePoolList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | Strin g | Query | 否 | storage pool | 存储池名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| StoragePool | Array |  | 存储池信息。 |
| -StorageId | String | efa6d59b-8288- 48c2-8ef5- 46*********** | 存储池ID。 |

|  | 灾备管理中心 |  |  | 备份管理平台开发指南·API参考 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Name | String | storage pool | 存储池名称。 |
| -Endpoint | String | oss-cn- hangzhou********* | 存储地址。 |
| -AccessKeyId | String | sdflee123******** | 访问AK。 |
| -StorageType | String | OSS | 存储类型，支持OSS/MiniOSS。 默认：OSS。 |
| -TrashBucket | String | trusn- des12fr******* | 回收站。 |
| -RegionId | String | cn-hangzhou***** | 区域ID。 |
| -Authority | String | owner | 用户权限。 owner：管理者。 |
| - StorageCapaci ty | Long | 20 | 存储空间，单位：（TB）。 |
| -UsedCapacity | Long | 8695761428 | 使用空间。单位：（byte）。 |
| -Description | String | 存储数据 | 存储池描述。 |
| RequestId | String | C8B26B44-0189- 443E-9816-******* | 请求ID。 |
| Success | Boolean | true | 本次请求是否成功。 |
| Code | String | 200 | 状态码。 200：调用正常。 |
| ErrorMessage | String | Not Found StoragePool for current operate. | 错误提示信息。 |
| ErrorCode | String | StoragePoolNotFou nd | 错误码。 |
| Path | String | /asrbr/*/* | 请求路径。 |
| Cost | Long | 20 | 接口耗时，单位毫秒（ms）。 |

| 备份管理平台开发指 | 南·API参考 |  | 灾备管理中心 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页返回的数据个数。 |
| TotalSize | Integer | 50 | 总数据量。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeStoragePoolList
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "Path":"/asrbr/*/*",
  "StorageType":"OSS",
```

`"Description":"`存储数据`",`

```json
  "Endpoint":"oss-cn-hangzhou*********",
  "StorageCapacity":20,
  "Authority":"owner",
  "AccessKeyId":"sdflee123********",
  "TrashBucket":"trusn-des12fr*******",
  "RegionId":"cn-hangzhou*****",
  "UsedCapacity":8695761428,
  "StorageId":"efa6d59b-8288-48c2-8ef5-46***********",
 },
 "RequestId":"C8B26B44-0189-443E-9816-*******",
 "PageNum":1,
 "PageSize":10,
 "ErrorCode":"StoragePoolNotFound",
 "ErrorMessage":"Not Found StoragePool for current operate.",
 "TotalSize":50,
 "Code":"200",
 "Cost":20,
 "Success":true
}
```

`XML` 格式灾备管理中心

```xml
 <Description>存储数据</Description>
 <Endpoint>oss-cn-hangzhou*********</Endpoint>
 <Authority>owner</Authority>
 <AccessKeyId>sdflee123********</AccessKeyId>
 <TrashBucket>trusn-des12fr*******</TrashBucket>
 <RegionId>cn-hangzhou*****</RegionId>
 <UsedCapacity>8695761428</UsedCapacity>
 <StorageId>efa6d59b-8288-48c2-8ef5-46***********</StorageId>
<RequestId>C8B26B44-0189-443E-9816-*******</RequestId> <PageNum>1</PageNum> <PageSize>10</PageSize> <ErrorCode>StoragePoolNotFound</ErrorCode> <ErrorMessage>Not Found StoragePool for current operate.</ErrorMessage> <TotalSize>50</TotalSize> <Code>200</Code> <Cost>20</Cost> <Success>true</Success>
```

灾备管理中心

## 错误码

### 数据面

#### Data_Execution_Layer_Error

## 错误码

**错误信息**

存储类产品在数据面执行备份任务时发生错误。

**原因分析**

存储类产品（如ECS、NAS、OSS、OTS、无影等）在执行备份任务时，数据面执行过程中发生错误。由于本版本尚未对数据面产品进行错误码适配，管控无法拿到细粒度的失败原因，只能通过透传到管控平台的错误信息或者数据面服务的日志进行确认与解决。

**置信等级**

A

**解决方案**

1. 根据产品类型确定对应的数据面服务，例如OSS、NAS产品对应hbr-agent.Agent#、ECS快照对应hbr-
2. 登录数据面服务节点，查看对应服务的日志，定位备份任务失败的具体原因。
3. 根据日志中的错误信息进行处理，处理完成后等待下一次备份周期自动重试，或在ASRBR控制台手动触
发备份。

### DBS

#### Dbaas

##### DBS-Dbaas-

**AccessInfoInvalidResourceStorageConfig**

## 错误码

##### DBS-Dbaas-AccessInfoInvalidResourceStorageConfig

**错误信息**

存储资源配置无效。

**原因分析**

首次创建存储接入信息时会检查并初始化 `DBS_REP_SAURON_SELECTOR` 资源记录时JSON处理报错。

**置信等级**

灾备管理中心 B

**排查方式**

**解决方案**

序列化异常：检查ObjectMapper配置及selector结构定义是否发生不兼容变更。

##### DBS-Dbaas-AccessInfoStorageInitFailed

## 错误码

**错误信息**

初始化存储访问信息失败。

**原因分析**

数据库写入异常：插入access_info记录时，因唯一键冲突、数据库连接异常导致错误。

**置信等级**

B

**排查方式**

1. 查看DBAAS服务日志中该异常的完整cause堆栈。
2. 检查数据库连接池状态与access_info表唯一键约束是否冲突。

**解决方案**

数据库异常：排查连接池状态、唯一键冲突记录，清理异常数据后重试。

##### DBS-Dbaas-BackupDataQueryFailed

## 错误码

**错误信息**

查询备份数据失败。

**原因分析**

describeUnifyBackupList委托具体IRestoreService实现查询备份列表时抛出的非结构化异常，被统一包装为该错误码，可能是下游存储/元数据服务查询异常。

**置信等级**

B

**排查方式**

1. 查看服务日志获取原始异常cause及涉及的dbType/kindCode/sceneType组合。
2. 结合具体IRestoreService实现（按dbType区分）进一步排查下游依赖（如备份集表、复制表）是否正
常。 灾备管理中心
3. 必要时调用相关运维工具核对底层存储/元数据服务状态。

**解决方案**

根据具体下游异常处理： 数据缺失，需检查备份任务是否正常执行。 服务异常，需等下游恢复后重试。

##### DBS-Dbaas-

**BackupDataSourceInstanceNotFound**

## 错误码

**错误信息**

备份源实例不存在。

**原因分析**

查询不到源实例信息，常见于实例不存在、已被删除或异地复制场景下数据库中缺少该实例的备份记录。

**置信等级**

B

**排查方式**

1. 确认instanceName 在该region下是否真实存在。
2. 针对异地恢复场景，检查replication_bakset表中是否存在对应源实例的复制备份集记录。
3. 核对sceneType参数是否传递正确（本地/异地场景）。

**解决方案**

实例确实不存在时，引导用户确认实例状态。如为异地场景元数据缺失，需检查复制链路是否正常完成备份集注册。

##### DBS-Dbaas-BackupJobAlreadyExists

## 错误码

**错误信息**

备份任务已存在。

**原因分析**

该实例已存在进行中的备份任务。

**置信等级**

A

**解决方案**

灾备管理中心查询该实例已存在的备份任务状态，等待其结束后再发起新任务。

##### DBS-Dbaas-BackupJobAlreadyFinished

## 错误码

**错误信息**

备份任务已完成。

**原因分析**

检测到相同missionId对应的备份任务已经处于完成状态，通常是客户端对同一missionId重复发起创建请求。

**置信等级**

A

**解决方案**

无需重复处理，可直接查询该missionId对应任务的最终状态确认结果。如需重新备份，应使用新的 missionId发起请求。

##### DBS-Dbaas-BackupJobInstanceNotFound

## 错误码

**错误信息**

备份任务对应的实例不存在。

**原因分析**

按实例标识查询不到对应的数据库实例，常见于实例名错误或实例已被释放。

**置信等级**

B

**排查方式**

核对请求中的实例标识是否正确，实例是否仍然存在。

**解决方案**

确认实例信息后重试。实例已释放的场景需引导用户重新创建实例。

##### DBS-Dbaas-BackupJobInternalError

## 错误码

**错误信息**

备份任务内部错误。 灾备管理中心

**原因分析**

请求中出现的内部异常，涉及Handler内部逻辑处理、下游依赖调用等多种可能原因。

**置信等级**

B

**排查方式**

1. 查看服务日志获取具体异常堆栈及涉及的
Handler（InstanceBakJobHandler/ClusterBakJobHandler）。
2. 结合missionId/instanceName等关键信息追踪该次请求的完整处理链路。
3. 必要时借助日志检索或链路追踪工具定位下游依赖异常点。

**解决方案**

根据具体异常原因分类处理： 若为偶发异常可重试。 持续复现需上报研发定位代码逻辑问题。

##### DBS-Dbaas-BackupJobInvalidParameters

## 错误码

**错误信息**

备份任务参数非法。

**原因分析**

请求参数错误。例如backupType不受支持、planBackupTime格式非法或forceSnapshot与其他参数组合不合法，通过查询Message获取详细的错误原因。

**置信等级**

B

**排查方式**

1. 核对backupType是否为接口支持的取值。
2. 核对planBackupTime时间格式，forceSnapshot与其他参数的组合是否符合业务约束。

**解决方案**

按接口文档修正参数取值和组合后重新提交请求。

##### DBS-Dbaas-BackupJobNotFound

## 错误码

**错误信息**

备份任务不存在。 灾备管理中心

**原因分析**

按backupJobId查询不到对应的备份任务记录，可能是任务ID错误或任务记录已被清理。

**置信等级**

B

**排查方式**

**解决方案**

确认任务ID后重试。任务记录确实已清理时，无法再查询历史状态。

##### DBS-Dbaas-BackupJobPolicyNotFound

## 错误码

**错误信息**

备份任务依赖的备份策略不存在。

**原因分析**

创建备份任务时依赖的备份策略未找到，常见于实例尚未配置备份策略，或策略与当前请求的policyLevel 不匹配。

**置信等级**

B

**排查方式**

核对该实例/集群是否已配置对应policyLevel的备份策略。

**解决方案**

先通过CreateBackupPolicy/ModifyBackupPolicy配置备份策略，再重新发起备份任务。

##### DBS-Dbaas-BackupJobStrategySyncing

## 错误码

**错误信息**

备份策略正在同步中。

**原因分析**

备份策略正在向DAG侧同步，尚未完成，此时不允许创建新的备份任务。

**置信等级**

A

**解决方案**

灾备管理中心等待策略同步完成后重新发起备份任务。如长时间未完成同步，需排查DAG侧策略同步链路是否卡住。

##### DBS-Dbaas-BackupPolicyDescribeFailed

## 错误码

**错误信息**

查询备份策略详情失败。

**原因分析**

在调用具体Handler查询策略详情时捕获到通用异常，可能是策略数据解析异常或下游查询异常。

**置信等级**

B

**排查方式**

1. 查看服务日志获取原始异常堆栈。
2. 核对该实例/集群关联的策略数据是否完整、格式是否正常。

**解决方案**

按异常原因修复对应数据或重试。如为下游依赖异常，需等下游恢复后重试。

##### DBS-Dbaas-

**BackupPolicyHandlerNotFound**

## 错误码

**错误信息**

未找到备份策略处理器。

**原因分析**

1. 该实例不支持备份。
2. 请求中的DbType大小写不规范（要求必须为小写，如mysql、polardb），导致无法命中注册的处理
器。

**置信等级**

B

**排查方式**

1. 检查请求中的DbType是否为小写，是否存在大小写混用（如MySQL、PolarDB）。
2. 该实例不支持备份，无法进行备份，通过备份产品文档查询哪些实例支持备份。

**解决方案**

1. 将DbType统一改为小写后重试。
灾备管理中心
2. 该实例不支持备份。

##### DBS-Dbaas-

**BackupPolicyInstanceNotFound**

## 错误码

**错误信息**

备份策略对应的实例/集群不存在。

**原因分析**

1. 根据instanceName（实例级策略）或clusterName（集群级策略）查询不到对应的实例/集群元信息，
可能是实例不存在、已释放，
2. policyLevel与实际实例类型不匹配（如gpdb_master场景下拼接了-master后缀仍未匹配；集群级实
例， policyLevel应为C；实例级应该为I）。

**置信等级**

B

**排查方式**

1. 核对请求中的instanceName/clusterName 拼写是否正确，实例是否真实存在于该region。
2. 检查policyLevel参数是否与实例真实类型（实例级/集群级）一致。
3. 针对GPDB场景确认master实例命名规则是否符合预期。

**解决方案**

确认实例信息无误后重试。若实例已释放，需引导用户重新创建实例后再配置备份策略。

##### DBS-Dbaas-BackupPolicyModifyFailed

## 错误码

**错误信息**

修改备份策略失败。

**原因分析**

modifyBackupPolicy在调用具体Handler执行策略修改逻辑时捕获到通用异常（如策略保存失败、DAG侧策略同步失败等下游调用异常）。

**置信等级**

B

**排查方式**

1. 查看DBAAS服务日志中modifyBackupPolicy相关的error日志，获取原始异常cause。
2. 结合message中透传的原始异常信息，定位是数据库写入失败还是下游服务（如DAG）调用失败。
灾备管理中心

**解决方案**

根据具体cause处理： 数据库异常，检查连接与数据一致性。 下游调用失败，检查下游服务状态后重试。

##### DBS-Dbaas-

**BackupPolicyRetentionModifyFailed**

## 错误码

##### DBS-Dbaas-BackupPolicyRetentionModifyFailed

**错误信息**

修改备份策略保留时长失败。

**原因分析**

常见于待修改的策略记录不存在或保留策略更新到数据库时失败。

**置信等级**

B

**排查方式**

1. 查看服务日志获取具体异常原因。
2. 核对该用户/region下是否已存在对应的额外备份策略记录。

**解决方案**

如策略记录不存在，需先确认策略初始化流程是否正常执行。 如为更新失败，检查数据库状态后重试。

##### DBS-Dbaas-BackupPolicyUserNotFound

## 错误码

**错误信息**

备份策略对应的用户不存在。

**原因分析**

查询 UserDAO 未找到对应用户记录。

**置信等级**

B

**排查方式**

1. 核对请求中的callerBid、userId、regionCode是否与实际账号信息一致。
2. 检查用户是否已在对应region完成同步/注册。
灾备管理中心

**解决方案**

确认用户账号信息正确后重试。如用户确实未同步，需先完成用户数据同步。

##### DBS-Dbaas-

**ClusterBackupClusterNotFound**

## 错误码

**错误信息**

集群备份对应的集群不存在。

**原因分析**

查询的集群在集群拓扑信息中不存在，通常发生在集群未删除但拓扑数据缺失，或集群标识传递错误的场景 （区别于集群已删除走用户校验分支的情况）。

**置信等级**

B

**排查方式**

1. 核对clusterName是否正确。
2. 检查集群拓扑服务中该集群的元数据是否完整。

**解决方案**

确认集群信息无误后重试。拓扑数据缺失需排查集群拓扑同步链路。

##### DBS-Dbaas-ClusterBackupUserNotFound

## 错误码

**错误信息**

集群备份对应的用户不存在。

**原因分析**

查询 UserDAO 未找到对应用户记录。

**置信等级**

B

**排查方式**

1. 核对请求中的callerBid、userId是否正确。
2. 确认该用户是否已在对应region完成同步。

**解决方案**

核实用户信息后重试。用户数据未同步时，需先完成用户同步流程。 灾备管理中心

##### DBS-Dbaas-

**RestoreArchiveLogUnavailable**

## 错误码

**错误信息**

恢复所需的归档日志不可用。

**原因分析**

按时间点恢复场景下，全量备份集校验通过后进行日志前置校验，查询到的归档日志列表为空或下游归档日志查询服务抛出异常。

**置信等级**

B

**排查方式**

1. 核对目标恢复时间点与全量备份集的一致性时间（consistentTime）之间是否存在完整的归档日志链。
2. 结合message中透传的下游downstreamCode/downstreamMessage定位具体下游异常原因。

**解决方案**

若归档日志确实缺失（链路断裂），需调整恢复时间点到有完整日志覆盖的范围。 若为下游异常，等待下游恢复后重试。

##### DBS-Dbaas-RestoreBackupInvalid

## 错误码

**错误信息**

恢复所用的备份集无效。

**原因分析**

按BackupId或RestoreTimePoint查询到的unifyBackupSet为空（对应结果中 RestoreTimeValid=false，ErrorMessage: Restore backupset invalid`），说明该备份集存在但状态不可用于恢复（如损坏、未完成、状态异常）。

**置信等级**

B

**排查方式**

1. 核对该备份集在备份集表中的状态字段，确认是否为已完成且可用状态。
2. 查看该备份集对应的原始备份任务是否正常结束。

**解决方案**

如备份集状态异常，需重新触发一次全量备份，使用新生成的可用备份集进行恢复。 灾备管理中心

##### DBS-Dbaas-RestoreQueryFailed

## 错误码

**错误信息**

查询恢复信息失败。

**原因分析**

程序运行时抛出异常（对应结果中RestoreTimeValid=false，ErrorMessage透传原始异常信息）。

**置信等级**

B

**排查方式**

1. 结合结果中的ErrorMessage字段查看原始异常描述。
2. 核对该实例对应的dbType/kindCode所使用的具体IRestoreService实现是否存在已知问题。
3. 必要时借助日志检索工具定位下游依赖调用失败详情。

**解决方案**

根据原始异常信息处理： 参数问题，需修正后重试。 下游依赖异常，需等待恢复或联系下游负责人排查。

##### DBS-Dbaas-

**RestoreSourceInstanceNotFound**

## 错误码

**错误信息**

恢复源实例不存在。

**原因分析**

通常发生在异地恢复场景下源端实例元数据缺失或者备份集不存在。

**置信等级**

B

**排查方式**

1. 确认待恢复的源实例名称、region是否正确。
2. 异地恢复场景下检查复制备份集表中是否存在对应源实例记录。

**解决方案**

核实实例信息后重试。若为异地场景元数据缺失，需排查复制备份链路。 灾备管理中心

##### DBS-Dbaas-RestoreTimeQueryFailed

## 错误码

**错误信息**

查询可恢复时间范围失败

**原因分析**

查询集群可恢复时间范围时捕获到非通用异常，可能是下游可恢复时间计算服务异常或参数组合不受支持。

**置信等级**

B

**排查方式**

1. 查看服务日志获取原始异常cause。
2. 核对describeBeginDateTime/describeEndDateTime时间范围是否合理（结束时间不早于开始时
间）。
3. 必要时结合下游备份集查询工具核对该集群备份集数据完整性。

**解决方案**

修正不合理的时间范围参数后重试。如为下游服务异常，等待恢复后重试。

#### Gareth

##### DBS-Gareth-ObjectNotFound

## 错误码

**错误信息**

源备份对象不存在，无法执行读取操作。

**原因分析**

备份引擎在访问源端备份文件时，根据提供的对象路径或名称未能找到对应文件（Object）。 常见根因包括： 对象已被删除，备份文件在存储中已被手动删除或通过生命周期规则自动清理。 备份任务积压，本地备份任务完成后向异地转储的时候，由于排队时间过长，本地备份集被过期清理。

**置信等级**

A

**解决方案**

1. 确认本地备份集是否被过期删除：如果当前时间，本地备份集产生时间大于本地备份策略保存时间，则有
可能因为本地备份集已过期被系统删除。如果因为备份任务积压导致过期删除，考虑修改备份策略，降低备份频率。 灾备管理中心
2. 排查删除原因：查看存储桶生命周期规则（Lifecycle Policy），判断是否自动删除了对象。检查是否有
人为删除操作或清理脚本影响。

##### DBS-Gareth-FileTooLarge

## 错误码

**错误信息**

备份文件大小超过系统或存储服务允许的最大限制，无法写入。

**原因分析**

数据库备份在执行备份操作时，发现目标文件（备份对象）体积超出了允许的大小限制，从而导致操作失败。常见根因包括：
1. 存储服务单文件限制：某些对象存储服务（如OSS、S3等）对单个对象大小有上限（如5TB、10GB
等）。
2. 网络传输协议限制：部分存储访问方式（例如分片上传、HTTP PUT限制）存在文件大小约束。

**置信等级**

A

**解决方案**

确认存储服务限制： 查询目标存储服务的单文件大小限制（如S3最大5TB、某些归档存储最大10GB）. 查看本地备份集是否大于目标存储服务的单文件大小限制。

##### DBS-Gareth-NetworkError

## 错误码

**错误信息**

备份任务与存储服务之间的网络通信出现异常，无法正常传输数据。

**原因分析**

备份服务在访问存储服务（对象存储、文件存储等）时，发生了非超时类的网络错误，导致请求失败。与 NetworkTimeout不同，此错误更广泛，可能涵盖连接中断、DNS解析失败、协议错误等。常见根因包括：
1. 网络中断：备份服务节点与存储服务之间的链路突然断开。
2. DNS解析失败：无法解析存储服务域名，导致请求无法建立。
3. TLS/SSL握手失败：安全连接过程出现认证或协议错误。
4. 路由异常：网络数据包无法正确到达目标端点（路由表错误或链路故障）。
5. 防火墙/安全组阻断：访问被本地或云端安全规则阻止。
6. 网络配置错误：代理、VPN、VPC等网络配置导致存储服务不可访问。
7. 丢包率过高：大量数据包丢失导致连接不稳定。
灾备管理中心

**置信等级**

B

**排查方式**

1. 查看任务与系统日志：检查错误发生时的日志，确认是连接失败、握手错误还是DNS问题。
2. 网络连通性测试：使用ping/traceroute /mtr测试到存储服务端点的连通性与延迟。
3. DNS解析验证：使用nslookup/dig解析存储服务域名，确认解析结果正确。
4. TLS/SSL检查：如果使用HTTPS访问，测试是否能正常建立安全连接；检查证书是否有效。
5. 安全规则验证：检查防火墙、安全组、ACL是否允许当前访问路线和端口。
6. 网络配置确认：如果任务运行在VPC或使用VPN/代理，确认这些连接配置无误并允许访问存储端点。
7. 丢包测试：使用iperf或网络监测工具查看传输丢包率是否异常。

##### DBS-Gareth-NetworkTimeout

## 错误码

**错误信息**

备份服务与目标存储服务通信超时。

**原因分析**

备份服务在与目标存储服务进行数据传输时，网络请求在预设时间内未完成，因此被判定为超时。常见根因包括：
1. 网络链路异常：服务节点与存储服务之间出现网络中断、传输延迟或丢包。
2. 带宽不足：网络出口带宽耗尽，导致请求无法在限定时间内完成。
3. 跨区域访问延迟：备份服务所在地域与存储桶所在地域距离较远，延迟高。
4. 存储服务端响应慢：存储服务高负载或限速状态，导致响应时间变长。
5. 防火墙或安全组规则阻断：网络访问路径上存在安全规则，阻止或延迟请求。
6. 客户端超时时间配置过短：备份任务侧的请求超时阈值设置不合理，导致提前中断。

**置信等级**

B

**排查方式**

1. 查看任务与网络日志：检查备份任务日志，确认超时发生的具体阶段（连接、传输、结束）；查看系统网
络监控是否有丢包、延迟异常。
2. 验证网络连通性：使用ping或traceroute测试到存储服务端点的延迟与连通性；检查是否存在间歇性网
络中断。
3. 带宽使用情况：查看当前网络带宽占用，确认是否已接近或达到上限。
4. 区域与线路优化：确认备份服务与存储桶是否位于同一区域，尽可能减少跨区域延迟。
5. 防火墙/安全组检查：确认网络安全配置（防火墙规则、安全组）允许存储服务端口及协议访问。
6. 调整超时阈值：在DBS任务配置中增加网络/请求超时时间，在大数据传输场景下减少误判。

**解决方案**

灾备管理中心
1. 优化网络链路：采用专线或高速通道，减少跨区域网络延迟；使用CDN或边缘存储节点，缩短访问路径。
2. 调整备份策略：降低备份并发数和单次数据量，减少网络压力。
3. 检查存储服务状态：确认存储服务端没有故障或限速。
4. 增加超时设置：在备份任务中适当增加网络超时阈值，避免在大文件传输中途终止。
5. 网络故障恢复后重试：网络恢复正常后重新执行备份任务。

##### DBS-Gareth-StorageThrottled

## 错误码

**错误信息**

存储服务访问速度被限制，备份任务性能下降或中断。

**原因分析**

此错误表示数据库备份在访问存储服务（对象存储、文件存储等）时，由于触发了存储服务的限速/节流策略，导致读写请求被延迟甚至暂时拒绝。常见根因包括：
1. 存储服务限流策略：对象存储服务对单个账号、单个桶或单个API接口调用设定了速率限制（QPS、带宽
限制）。
2. 并发请求过多：短时间内产生大量备份数据上传/下载，引发存储服务限流。
3. 带宽耗尽：网络出口或存储服务流量带宽达到上限。
4. 存储服务负载过高：后台系统负载较高，主动对部分请求限速以保障整体服务稳定。
5. 跨区域访问延迟：访问存储桶所在区域的网络链路带宽不足，也可能导致限速或超时。

**置信等级**

B

**排查方式**

1. 查看DBS与存储服务日志：分析限速的具体时间点与触发场景；检查是否出现HTTP状态码如 429 Too
Many Requests、503 Slow Down等。
2. 确认限流规则：查看存储服务文档或控制台中配置的QPS限制、带宽限制、并发请求数限制等；确认是否
对备份任务的访问账户或桶进行了速率配置。
3. 监控流量与并发：使用网络监控工具或云服务监控面板，查看当前备份任务的上传/下载流量；检查并发
任务数是否超过建议值。
4. 网络排查：如果是跨区域访问，测试到存储端点的网络延迟与带宽，确认是否因线路瓶颈触发限速。
5. 联系运维或云存储支持：如果为服务端负载限速，应联系云服务或内部运维团队协助调整。

**解决方案**

1. 优化并发与速率：降低同时执行的备份任务数量或调整分批上传策略；在备份配置中设置限速（Rate
Limiting）以避免触发服务端限流。
2. 分区或分桶备份：将数据分散到多个存储桶，降低单桶访问压力。
3. 重试机制：在备份脚本或配置中加入指数退避重试，减少限速后任务终止的风险。

##### DBS-Gareth-BucketFull

## 错误码

灾备管理中心

## 错误码

**错误信息**

备份仓库存储空间不足，无法继续写入备份数据。

**原因分析**

数据库备份在将备份数据写入对象仓库时，检测到目标备份仓库容量已达到上限或配额不足，导致备份中断。常见根因包括：
1. 存储配额耗尽：备份仓库已使用空间达到分配上限。
2. 存储服务默认限额：未购买额外容量，使用的免费/默认空间已用尽。
3. 存储桶写入限制：存储服务对单个桶的最大对象数量、总大小有技术限制。

**置信等级**

A

**解决方案**

通过asrbr-backup管控控制台获取当前备份计划对应的备份仓库，通过备份仓库获取对象存储桶名称。
1. 检查存储桶容量使用情况：在对象存储管理控制台查看桶的总容量和已用容量；通过查询命令（如aws
s3 ls、ossutil du）获取桶内文件占用空间。
2. 扩容存储容量：提升存储桶容量上限。
3. 优化备份策略：调整备份周期与保留策略，减少备份次数、缩短备份时长；手动删除备份记录（针对存储
类产品删除备份记录后，需要等待备份软件完成GC后，才能释放存储空间）。
4. 重试备份：在释放或扩充空间后，重新执行备份任务。

##### DBS-Gareth-DiskFull

## 错误码

**错误信息**

备份任务执行失败，备份引擎本地磁盘空间不足，无法写入临时数据。

**原因分析**

数据库备份服务的Gareth模块在执行备份任务时，检测到运行服务器本地磁盘已达到使用上限，无法继续写入数据。常见根因包括：
1. 临时文件占用过大：备份任务产生的中间文件未及时清理。
2. 日志文件增长过快：备份任务日志增长过快。
3. 多任务并发写入：多个备份任务同时在同一磁盘写入数据，导致空间迅速耗尽。

**置信等级**

A

**解决方案**

1. 检查磁盘使用情况：使用df -h或存储管理工具查看磁盘容量；确认磁盘已满或接近满负荷。
2. 清理不必要文件：清理日志。
3. 监控磁盘容量：配置磁盘使用率告警，提前预防磁盘满导致任务失败。
灾备管理中心
4. 重试任务：清理后重新执行备份任务。

##### DBS-Gareth-StorageAccessDenied

## 错误码

**错误信息**

备份服务调用目标存储接口时，访问被拒绝。 访问的OSS接口：PutObject、InitiateMultipartUpload、UploadPart、CompleteMultipartUpload、 AbortMultipartUpload、AppendObject 。 访问的S3接口：PutObject、WaitUntilObjectExists、CreateMultipartUpload、UploadPart、 CompleteMultipartUpload、AbortMultipartUpload。

**原因分析**

数据库备份服务在尝试访问目标存储（对象存储 Bucket）时，被存储服务拒绝。常见原因包括：
1. 权限策略缺失或不足：存储池的（AccessKey/SecretKey）未被授予相应接口的读写权限。
2. 访问密钥错误或已失效：存储池的密钥(AccessKey/SecretKey)被轮转。
3. 访问策略限制：存储服务设置了白名单IP、VPC限制或资源策略，导致备份服务无法访问目标存储。
4. 跨账号访问未授权：目标存储桶属于其他账号，但没有正确的跨账号授权策略。
5. 权限更新延迟：刚刚修改了访问策略或授权，但尚未在存储服务生效。

**置信等级**

B

**排查方式**

1. 查看备份服务的访问日志：在备份服务的访问日志中，查看访问拒绝的详细原因（会标明是权限不足、策
略冲突或资源不存在）。
2. 验证访问凭证有效性：确认存储池配置的AccessKey/SecretKey有效且未过期；测试直接使用该凭证访
问存储（例如使用ossutil/aws s3 cli/SDK）。
3. 检查权限策略：确认绑定的用户/角色策略中，已包含对应存储操作的权限（如
PutObject/InitiateMultipartUpload/UploadPart）。
4. 确认资源策略与网络条件：查看存储桶策略、ACL、白名单IP、VPC绑定等设置，确保备份引擎所在的网
络环境符合访问条件。
5. 跨账号场景：如果目标存储桶属于其他账号，确认已进行跨账号授权（例如Bucket Policy allowing
external account）。
6. 同步授权变更：如果刚调整了存储权限，等待权限同步或在存储服务控制台进行手动刷新。

**解决方案**

1. 修正访问策略：在存储服务中给存储池对应的AccessKey添加所需的存储权限策略。
2. 更新访问密钥：如果密钥错误或过期，在备份存储池配置新的有效密钥。
3. 调整资源策略：在存储桶ACL或策略中加入备份引擎的访问主体，并检查网络/VPC/IP限制。
4. 配置跨账号授权：在跨账号场景下，确保正确配置Bucket Policy。
5. 重新测试：修改后使用CLI或SDK验证访问正常，再重启或重试备份任务。
灾备管理中心

##### DBS-Gareth-BucketNotFound

## 错误码

**错误信息**

备份仓库对应的存储桶不存在，无法进行备份或恢复操作。

**原因分析**

出现该错误通常意味着系统要访问的存储桶（Bucket）不存在或无法被识别，可能的原因包括： 存储桶被删除，目标存储桶已被手动或自动删除，但备份任务仍引用该桶。

**置信等级**

A

**解决方案**

确认存储桶存在性：登录存储服务管理控制台或通过API查询，确认该存储桶是否仍存在。如果不存在需要创建新的备份仓库，将备份计划指定到新的备份仓库。

#### REP

##### DBS-REP-JobTerminated

## 错误码

**错误信息**

跨地域复制任务已被终止，任务未完成。

**原因分析**

状态机在执行Physical物理备份复制或Snapshot快照复制任务时捕获到TerminatedException，将任务归类为终止类失败：
1. 用户或系统主动取消：任务被人工取消，或上层调度因策略变更、实例删除、任务冲突等原因终止任务。
2. 下游任务进入终止态：已提交到执行通道的复制/转储任务被取消或返回TERMINATED，状态机随之进入
终止流程。
3. 状态机等待终止：任务进入WAIT_TERMINATE后，Finish阶段继续清理或取消下游任务，最终以终止状
态结束。
4. 执行环境中断：容器重启、调度迁移或执行通道异常，可能被上层框架转换为终止异常。

**置信等级**

B

**排查方式**

1. 检查操作审计、任务变更记录和控制台操作日志，确认是否有人为取消或策略变更触发终止。
2. 根据taskId查询dbs-workflow/dbs-sauron/dbs-gareth侧任务状态，确认是否已返回TERMINATED或
被取消。 灾备管理中心
3. 查看Job当前状态、进入WAIT_TERMINATE的原因及errMsg中的原始错误信息，定位最早的终止触发
点。

**解决方案**

1. 确认终止是否符合预期（如用户主动取消、实例已删除），若符合预期无需处理。
2. 若终止并非预期，确认源备份集仍可用、目标地域配置正确后，重新触发跨地域复制。
3. 若为执行环境中断导致，检查相关容器/调度日志，确认环境恢复后再重试。

##### DBS-REP-InternalConfigError

## 错误码

**错误信息**

复制任务内部配置或任务上下文异常，无法继续执行。

**原因分析**

状态机捕获到内部配置类异常（FailedException或JsonProcessingException）并将错误码归类为DBS- REP-InternalConfigError：
1. 任务上下文 JSON 解析失败：Job的context、备份集slaveStatus或下游返回信息格式异常，触发
JsonProcessingException。
2. 内部处理显式失败：Handler执行过程中抛出FailedException，通常表示必要配置、上下文或内部依赖
不满足。
3. 存储配置构建失败：源端或目标端存储配置缺失、ownerId异常、region/storageType不匹配，导致无
法构造复制所需的存储参数。
4. 实例或快照上下文不完整：快照复制场景下，实例信息、ECS访问凭证、snapshotId、diskId等上下文
缺失或格式不符合预期。

**置信等级**

B

**排查方式**

1. 根据eventId/custinsId查询Job的context字段，确认JSON可解析且关键字段完整。
2. 检查bakhistory.slaveStatus、downloadUrl、archiveOwnerid、type等字段是否完整、格式是否正
确。
3. 核对源端和目标端region、storageType、storageId、ownerId是否与实际资源匹配，确认访问凭证可
用。
4. 在bak-replication-service日志中搜索“JsonProcessingException”、“FailedException”、“prepare
parse json failed"”或相关“eventId”，定位具体缺失字段。

**解决方案**

1. 修正任务上下文或备份集元数据中缺失/格式错误的字段后重新触发复制。
2. 若上下文来自上游创建逻辑，需同步排查dbs-dbaas/dbs-dag-controller的任务生成参数是否正确。
3. 若为存储配置问题，核实对应存储账号、region、storageType配置是否与实际资源一致。

##### DBS-REP-SubJobFailed

## 错误码

灾备管理中心

## 错误码

**错误信息**

集群备份复制任务中，一个或多个子任务（物理备份复制）执行失败，导致整体任务失败。

**原因分析**

集群复制任务会为每个分片节点创建独立的PhysicalBackupReplicationJob子任务并行执行。当任意子任务进入失败终态时，父任务汇总子任务错误并以此错误码标记整体失败，常见子任务失败根因：
1. 网络不稳定：跨地域数据传输过程中发生持续网络中断，超过最大重试次数（MAX_RETRY=10）后触发
终态失败。
2. 存储空间不足：目标地域存储资源配额耗尽，物理备份文件写入失败。
3. 源文件丢失：子任务执行期间，源端备份文件被提前清理或过期删除。
4. 单节点超时：特定分片节点的备份数据量远超预期，在规定时间窗口内未能完成传输。
结构化错误信息的errorMessage.subJobsError字段会列出各失败子任务的subJobId及对应错误详情，可直接定位到具体失败的分片。

**置信等级**

B

**排查方式**

1. 在任务的resultMessage JSON中读取errorMessage.subJobsError，确认失败的子任务ID及其错误原
因。
2. 针对失败子任务的具体subJobId，结合物理备份复制的DBS-REP-*错误码文档进一步定位子任务级根
因。
3. 检查两端地域网络连通性、目标地域存储配额使用情况，以及是否存在数据量异常偏大的分片。

**解决方案**

1. 针对网络问题：确认两端地域的网络连通性，必要时联系网络团队排查专线或公网带宽；网络恢复后重新
触发父任务。
2. 针对存储不足：扩容目标地域存储配额后重试，或清理历史过期数据释放空间。
3. 针对源文件丢失：确认源端备份集的保留策略，若文件已不可恢复则需重新生成源备份后再发起复制。
4. 针对超时：评估是否需要对数据量特别大的分片单独调整超时配置，或将任务拆分为更小粒度。

##### DBS-REP-ReplicationFailed

## 错误码

**错误信息**

跨地域复制任务执行失败（未归类到具体错误类型）。

**原因分析**

DBS-REP-ReplicationFailed是Physical物理备份复制和Snapshot快照复制场景下的兜底错误码。当任务失败但异常类型不属于TerminatedException、FailedException、JsonProcessingException等已知分类时，deriveErrorCode会统一归类为该错误码：
1. 未知运行时异常：网络超时、RPC调用异常、数据库访问异常等未被特殊处理的RuntimeException。
灾备管理中心
2. 重试次数超限：快照复制场景下任务重试次数超过MAX_RETRY，系统主动放弃并标记为复制失败。
3. 下游存储/转储组件异常：dbs-gareth转储、ECS/HBR快照复制等下游组件返回的错误未被识别为特定错
误码。
4. 其他未覆盖分支：状态机分支处理未穷尽所有异常场景，兜底进入该错误码。

**置信等级**

B

**排查方式**

1. 优先查看errMsg中的errorMessage字段（通常携带原始异常消息，如e.getMessage()），据此判断根
因方向。
2. 若日志显示 "retry rep job more than N times"，说明是多次重试后放弃，需要排查更早期重试失败的
具体原因（网络、存储、下游服务状态）。
3. 结合custinsId、eventId、taskId查询dbs-gareth/dbs-sauron/ECS快照复制接口的返回码和异常堆
栈，定位具体失败环节。
4. 检查网络连通性（跨地域专线/公网带宽）和下游服务健康状态。

**解决方案**

1. 根据排查得到的具体根因分别处理：网络问题联系网络团队排查，下游服务异常等待恢复或联系对应服务
负责人。
2. 确认根因修复后，可重新触发或等待任务自动重试。
3. 若该场景出现频率较高，建议在BaseHandler.deriveErrorCode() 中补充对应异常类型的显式映射，避
免持续落入兜底错误码，便于后续统计和自动化排查。

##### DBS-REP-SrcBaksetNotAvailable

## 错误码

**错误信息**

源备份集不可用，无法执行跨地域复制。

**原因分析**

在Physical物理备份复制或Snapshot快照复制的准备/校验阶段，系统发现源备份集数据存在异常，无法继续发起复制：
1. 备份集状态不可复制：源地域的备份集当前处于不可复制状态，例如正在生成中、已过期、被锁定、状态
异常，canReplicate()校验不通过。
2. 备份集无有效下载地址：备份集记录存在，但缺少下载URL；非 restorepoi类型备份集无法定位实际数
据进行传输。
3. 备份集查询结果为空：按照Job记录的备份集ID查询时返回null，说明对应备份集记录可能已删除、未写
入或元数据丢失。
4. 快照备份集不可用：Snapshot复制场景下，bakhistory为空或 isAvail不为true，系统判断源快照备份
集不可用。
5. 内部临时备份不可复制：Snapshot复制场景下，备份集taskFrom=2，属于内部临时备份，不允许作为
跨地域复制源。

**置信等级**

B 灾备管理中心

**排查方式**

1. 根据backupsetId/hisId/custinsId查询bakdb中bakhistory记录，确认记录是否存在、
canReplicate()/isAvail/taskFrom字段取值。
2. 检查downloadUrl是否为空，确认源备份任务是否正常结束、备份元数据是否完整写入。
3. 结合Job的errMsg中的原始日志信息（如 "src bakset cannot replicate, skip"、"bakhistory is not
avail, skip"）定位具体触发分支。

**解决方案**

1. 状态不可复制：等待源备份集生成完成后重试；若备份集已过期或状态持续异常，需重新触发源地域备
份。
2. 无下载地址：检查备份元数据是否完整写入；若备份数据确实缺失，重新发起备份。
3. 查询为空：确认 bakhistory 记录是否被清理或逻辑删除，必要时重新生成源备份集。
4. 快照不可用：确认源快照是否已生成完成且仍可用；若快照已删除，需要重新生成本地快照备份后再触发
复制。
5. 内部临时备份：不要使用内部临时备份作为复制源，选择正式备份集重新发起异地备份复制。

##### DBS-REP-SrcFileLost

## 错误码

**错误信息**

源备份文件或源快照已丢失，无法继续跨地域复制。

**原因分析**

系统已找到备份集元数据，但在校验实际源数据时发现文件或快照不存在，无法继续传输：
1. 物理备份源对象不存在：根据备份集下载地址调用checkExists校验，连续重试后仍无法定位源对象。
2. 备份文件已被清理：源地域备份文件可能已被保留策略、生命周期规则或人工操作删除，但bakhistory元
数据仍残留。
3. 源快照已删除：Snapshot复制调用ECS/HBR快照复制接口时返回InvalidSnapshotId.NotFound，源快
照ID已不存在于ECS。
4. 元数据与实际存储不一致：备份集中的下载地址或快照ID指向的数据已不存在，元数据未及时更新。

**置信等级**

B

**排查方式（可选）**

1. 对于物理备份：在源端存储中直接验证downloadUrl对应的对象是否存在（如OSS对象路径）；检查备
份保留策略和清理任务日志，确认文件何时被删除。
2. 对于快照备份：在源地域ECS控制台或通过DescribeSnapshots API确认快照ID是否存在；查看bak-
replication-service日志中"snapshot is already delete, skip copy"的触发时间与上游快照清理时间是否重叠。
3. 检查备份保留时长配置：确认源地域备份是否在复制任务完成前已过保留期被自动清除。

**解决方案**

1. 物理备份文件丢失：确认备份数据是否被生命周期或清理任务删除；如数据已不可恢复，重新触发备份生
成新的源备份集后再发起复制。 灾备管理中心
2. 源快照丢失：若快照已删除，需在源地域重新执行本地快照备份后，再触发跨地域复制。
3. 优化保留策略：将备份文件/快照保留时长设置为大于跨地域复制预计耗时，防止复制未完成时源数据被
清理。
4. 元数据修复：若数据实际存在但路径记录错误，修正备份集downloadUrl或快照ID后重试。

### ASRBR

#### SYSTEM

##### ASRBR-SYSTEM-LicenseQuotaExceeded

## 错误码

**错误信息**

License配额不足，无法执行请求的操作。

**原因分析**

备份能力受License授权配额约束。当已使用量达到或本次操作将超过License配额上限（如容量/实例数/产品类型额度）时，系统阻止新增。

**置信等级**

B

**解决方案**

1. 释放配额：清理不再需要的备份计划或实例以释放License配额。
2. 扩充配额：联系管理员扩充当前组织的License配额。
3. 重新操作：配额充足后重新提交请求。

##### ASRBR-SYSTEM-LicenseValidationFailed

## 错误码

**错误信息**

License校验失败。

**原因分析**

系统在执行备份计划的创建、立即备份等场景会去检查当前环境的授权（license）是否满足需求，在这个检查过程中出现验证失败。

**置信等级**

B

**解决方案**

1. 确认License有效性：检查当前环境的License是否在有效期内且与环境匹配。
灾备管理中心
2. 重新导入：若License已过期或不匹配，重新获取正确的License并导入。
3. 联系管理员：若无法解决，联系管理员协助排查License校验链路。

##### ASRBR-SYSTEM-

**LicenseConfigBelowLowerLimit**

## 错误码

**错误信息**

License配置低于下限。

**原因分析**

修改组织的License分配额度时，新值低于允许的下限。此下限由已分配给子组织的最大额度决定，以防止子组织授权被意外收回。

**置信等级**

B

**解决方案**

1. 查看子组织分配：确认各子组织当前已分配的License额度。
2. 调整至合规值：将分配值设置为不低于子组织中最大分配值。
3. 先回收再调整：若确需减小，先回收子组织的部分额度后再操作。

##### ASRBR-SYSTEM-

**LicenseConfigExceedsTotalQuota**

## 错误码

##### ASRBR-SYSTEM-LicenseConfigExceedsTotalQuota

**错误信息**

License 分配值超过总额度上限。

**原因分析**

修改组织License分配时，新值超过了可用的总额度上限。具体有两种情况：
1. 无父组织时，总分配量超过系统总License容量。
2. 有父组织时，分配量超过父组织授权给当前组织的上限。

**置信等级**

B

**解决方案**

1. 调小分配值：确保总分配量不超过可用总额度。
2. 回收其他组织额度：释放其他子组织的部分额度后再分配。
灾备管理中心
3. 扩充总License：若总额度不足，联系管理员扩充License总量。

##### ASRBR-SYSTEM-

**PhysicalMachineInfoQueryFailed**

## 错误码

##### ASRBR-SYSTEM-PhysicalMachineInfoQueryFailed

**错误信息**

物理机或节点信息查询失败。

**原因分析**

查询物理机/节点/动态VIP信息依赖底层运维服务接口。常见失败原因：
1. 目标物理机或节点不可达，处于离线、维护或重启状态。
2. 当前账号缺少查看物理机信息的权限。
3. 底层运维服务异常或网络中断，导致查询请求未成功返回。

**置信等级**

A

**解决方案**

1. 检查目标物理机或节点的状态与网络连通性。
2. 确认当前账号具备查看物理机信息所需的权限。
3. 稍后重试；若持续失败请联系管理员排查运维服务。

##### ASRBR-SYSTEM-

**CrossRegionRecoveryNeedAdvancedLicense**

## 错误码

##### ASRBR-SYSTEM-CrossRegionRecoveryNeedAdvancedLicense

**错误信息**

跨云恢复需要购买高级版授权。

**原因分析**

在执行元数据灾备恢复时，管控会将源环境备份的元数据还原到恢复库，并比对源环境与当前环境的地域。 当判定为跨地域恢复且当前环境未购买ASR-BR高级版授权，恢复流程被阻断并记录本错误码。跨地域恢复属于高级版能力，未获授权时不允许执行。

**置信等级**

B

**解决方案**

1. 确认本次恢复是否为跨地域恢复：核对源环境备份计划所属地域与当前环境地域是否一致。
灾备管理中心
2. 若确需跨地域恢复：为当前环境购买并开通 ASR-BR 高级版授权后重新发起恢复。
3. 若地域配置有误：在与源环境一致的地域执行恢复。
4. 注意，阻断发生时恢复库会被清理，处理授权后需重新触发完整恢复流程。

##### ASRBR-SYSTEM-HbrInitializeFailed

## 错误码

**错误信息**

HBR服务初始化失败。

**原因分析**

ASRBR管控调用HBR-Console接口时，若检测到HBR-Console尚未初始化，会尝试自动初始化。 当在重试次数内初始化仍未成功时，记录本错误码。常见于HBR-Console服务状态异常或初始化依赖条件不满足。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，确认HBR-Console初始化失败的返回信息。
2. 确认HBR-Console服务状态是否正常、初始化依赖（如存储、网络）是否就绪。
3. 若无法明确原因，联系产品研发协助排查。
4. 问题解决后，重新触发相关操作。

#### VAULT

##### ASRBR-VAULT-VaultCapacityExceeded

## 错误码

**错误信息**

备份仓库使用量已超过总容量。

**原因分析**

备份仓库存在总容量上限。当仓库内已存储的数据量达到或超过该上限时，系统会阻止继续写入。常见原因：
1. 该仓库关联的备份计划周期性运行，备份数据持续累积超过仓库容量上限。
2. 该仓库关联的备份计划保留时长设置过长，过期数据未及时清理，长期占用存储空间。
3. 仓库容量规划偏小，不足以支撑当前的备份数据规模。

**置信等级**

A 灾备管理中心

**解决方案**

**当前恢复操作**

1. 扩大备份仓库的总容量上限，快速恢复可用空间。
2. 联系产研同学评估是否可以执行手动GC操作，清理仓库中无效或过期数据以释放空间。

**后续优化建议**

1. 等待过期备份记录自动过期，或在产品支持的情况下手动删除不再需要的备份记录，持续释放空间。
2. 在引用该仓库的备份计划中适当缩短保留时长，减少长期空间占用。

##### ASRBR-VAULT-TrashBucketCannotBeVault

## 错误码

**错误信息**

回收站Bucket不能作为备份仓库。

**原因分析**

出于数据安全考虑，系统禁止将回收站Bucket用作备份仓库。

**置信等级**

A

**解决方案**

改选一个未配置为回收站的普通Bucket作为备份仓库。

##### ASRBR-VAULT-VaultDeletionBlocked

## 错误码

**错误信息**

删除备份仓库失败，存在关联的备份计划或者存在未过期的备份记录。

**原因分析**

为保护备份数据，系统在以下情况下禁止删除备份仓库：
1. 该仓库当前仍被一个或多个备份计划引用，直接删除会导致相关备份任务异常。
2. 仓库内存在未过期的备份数据，直接删除会导致已存数据丢失。

**置信等级**

A

**解决方案**

1. 若存在关联的备份计划：进入【备份计划】列表，查找并删除所有引用该仓库的备份计划。
2. 若仓库内存在未过期的备份数据：等待数据自动过期或在产品支持的情况下手动删除未过期的备份记录。
3. 确认无任何依赖与未过期数据后，重新执行删除备份仓库操作。
灾备管理中心

##### ASRBR-VAULT-KmsServiceUnavailable

## 错误码

**错误信息**

KMS服务不可用。

**原因分析**

加密仓库依赖密钥管理服务（KMS）提供加密密钥。当KMS服务异常、未开通或网络不可达时，加密相关操作无法完成。 常见原因包括：KMS服务未开通、服务实例异常、网络或授权链路中断等。

**置信等级**

A

**解决方案**

1. 确认服务状态：检查KMS服务是否已开通且运行正常。
2. 检查连通与授权：确认与KMS的网络连通性以及访问授权配置正确。
3. 重新执行：待KMS恢复正常后重新创建加密仓库或重试操作。如长期不可用，请联系管理员排查KMS服
务。

##### ASRBR-VAULT-KmsKeyNotEnabled

## 错误码

**错误信息**

KMS密钥状态未启用。

**原因分析**

所选KMS密钥当前处于禁用（Disabled）、待删除或其他非启用状态，无法用于数据加密，导致加密仓库创建失败。

**置信等级**

A

**解决方案**

1. 启用密钥：进入KMS控制台，将目标密钥状态切换为「启用（Enabled）」。
2. 更换密钥：或改选一个处于启用状态的可用密钥。
3. 重新执行：确认密钥可用后，重新创建加密备份仓库。

##### ASRBR-VAULT-KmsKeySpecNotMatch

## 错误码

灾备管理中心

**错误信息**

KeySpec与加密算法不匹配。

**原因分析**

所选KMS密钥的规格（KeySpec）与备份加密所要求的加密算法不一致。密钥规格决定了其可支持的加密算法，规格不匹配时密钥无法用于该加密场景。

**置信等级**

A

**解决方案**

1. 匹配密钥规格：选择与所需加密算法相匹配规格（KeySpec）的KMS密钥。
2. 调整加密配置：或按密钥实际规格调整备份加密的算法配置。
3. 重新执行：确认KeySpec与算法匹配后，重新创建加密备份仓库。

##### ASRBR-VAULT-KmsKeyUsageNotMatch

## 错误码

**错误信息**

密钥用途不是加密/解密。

**原因分析**

所选KMS密钥的用途（KeyUsage）不是「加密/解密（ENCRYPT_DECRYPT）」，例如被设置为签名验签 （SIGN_VERIFY）等其他用途，因此无法用于备份数据的加密。

**置信等级**

A

**解决方案**

1. 选择正确用途：选择KeyUsage为「加密 / 解密」的KMS密钥。
2. 新建密钥：或新建一个用途为加密/解密的密钥。
3. 重新执行：确认密钥用途正确后，重新创建加密备份仓库。

##### ASRBR-VAULT-TrashBucketImmutable

## 错误码

**错误信息**

回收站Bucket配置一经设置不可修改。

**原因分析**

修改存储池配置时，系统发现该存储池已设置回收站Bucket，而本次请求试图改动它（置空或改为不同值）。回收站Bucket一经设置不可修改，因此拒绝本次修改并记录本错误码。 灾备管理中心

**置信等级**

A

**解决方案**

1. 修改存储池时，保持回收站Bucket配置与已设置的值一致，不要改动。
2. 若确需变更回收站Bucket，请评估影响后通过重建存储池等方式处理。

##### ASRBR-VAULT-BucketAlreadyUsed

## 错误码

**错误信息**

备份仓库使用的Bucket已被其他备份仓库占用。

**原因分析**

为避免多个备份仓库写入同一Bucket造成数据混乱，系统不允许两个备份仓库共用一个Bucket。当前所选 Bucket已被其他备份仓库使用，因此创建失败。

**置信等级**

A

**解决方案**

1. 更换一个未被任何备份仓库使用的Bucket重新创建备份仓库。
2. 若需要复用该Bucket，请先删除占用该Bucket的备份仓库。

##### ASRBR-VAULT-ExistingBucketRequired

## 错误码

**错误信息**

该存储池必须配置已存在的Bucket作为回收站Bucket。

**原因分析**

当存储池权限为读写（RW）时，系统不会自动创建Bucket，因此要求配置或选择的Bucket在底层对象存储中必须已经存在。常见触发场景：
1. 创建备份仓库时未指定Bucket名称，或指定的Bucket在底层对象存储中不存在。
2. 创建或修改存储池的回收站Bucket时，所配置的回收站Bucket在底层对象存储中不存在。

**置信等级**

A

**解决方案**

1. 创建备份仓库前，确认所选Bucket已存在于底层对象存储，并填写正确的Bucket名称。
2. 配置回收站Bucket时，确认对应Bucket已存在于底层对象存储。
灾备管理中心
3. 如确需使用新Bucket，请先在底层对象存储中创建后再返回配置。

##### ASRBR-VAULT-BucketCreationFailed

## 错误码

**错误信息**

为备份仓库创建Bucket失败。

**原因分析**

创建备份仓库时，ASRBR管控需要在底层存储创建对应的Bucket。当创建Bucket接口返回失败或抛出存储异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位创建Bucket失败的具体错误信息。
2. 常见原因包括：存储凭证权限不足、Bucket数量或容量达到上限、底层存储服务不可用。
3. 若无法明确原因，提取请求参数与响应内容，联系存储管理员协助排查。
4. 问题解决后，重新发起备份仓库创建。

##### ASRBR-VAULT-HbrVaultCreationFailed

## 错误码

**错误信息**

在HBR中创建备份仓库失败。

**原因分析**

创建备份仓库时，ASRBR管控需要在HBR-Console中创建对应的Vault。当HBR-Console未返回

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位调用HBR-Console创建Vault时的请求参数与返回内容。
2. 常见原因包括：HBR-Console服务不可用、Bucket配额不足、仓库配置异常。
3. 若无法明确原因，提取请求参数与响应内容，联系产品研发协助排查。
4. 问题解决后，重新发起备份仓库创建。
灾备管理中心

##### ASRBR-VAULT-

**ReplicationVaultCapacityTooSmall**

## 错误码

##### ASRBR-VAULT-ReplicationVaultCapacityTooSmall

**错误信息**

镜像仓库容量必须大于源仓库容量。

**原因分析**

创建镜像仓库时，系统会校验容量配置。当指定的镜像仓库容量小于源仓库容量时，记录本错误码。

**置信等级**

A

**解决方案**

1. 将镜像仓库容量设置为大于源仓库容量。
2. 调整容量后重新发起镜像仓库创建。

##### ASRBR-VAULT-

**StorageMediumLockUnsupported**

## 错误码

**错误信息**

当前存储介质不支持备份锁定。

**原因分析**

开启或延长备份仓库的备份锁定（WORM 锁定）时，系统会校验底层存储介质是否支持。当存储类型本身不支持WORM，或底层存储返回不支持时，记录本错误码。

**置信等级**

B

**解决方案**

1. 确认当前备份仓库使用的存储介质是否支持不可变备份（WORM）。
2. 如需使用备份锁定，改用支持WORM的存储介质创建备份仓库。

##### ASRBR-VAULT-TrashBucketRequired

## 错误码

灾备管理中心

**错误信息**

该仓库必须配置回收站Bucket。

**原因分析**

当存储池权限为读写（RW）且备份仓库类型为重删（DEDUPLICATION）时，系统要求存储池必须配置回收站Bucket，以保证重删仓库的清理与回收逻辑能够正常工作。当前未配置回收站Bucket，因此创建失败。

**置信等级**

A

**解决方案**

1. 在创建重删备份仓库前，先在对应存储池中配置回收站Bucket。
2. 回收站Bucket配置完成后，重新创建重删备份仓库。

#### BACKUP

##### ASRBR-BACKUP-UserCancelledBackupJob

## 错误码

**错误信息**

**原因分析**

该错误并非系统异常，而是用户在ASRBR管控平台对正在备份中的任务执行了"取消"操作，备份管控接收到取消指令后将任务终止，并以此错误码标记任务的最终状态。常见触发场景包括：
1. 用户主动取消：实例信息有误、备份策略需要调整、希望避开业务高峰，由用户在控制台手动停止当前备
份任务。
2. 误操作取消：用户在操作其他任务时点错按钮，误将备份中的任务取消。

**置信等级**

A

**解决方案**

1. 若取消属预期行为，无需处理；下次按计划周期触发时会自动执行备份任务。
2. 若取消属误操作，请前往ASRBR管控平台对应实例的备份计划页面，单击“手工备份”，手动重新触发一
次备份任务。

##### ASRBR-BACKUP-

**SyncBackupJobResultTimeout**

## 错误码

灾备管理中心

**错误信息**

备份任务已发起，但在规定时间内未收到备份服务的执行结果反馈，系统判定为超时失败。

**原因分析**

备份管控对每个备份任务设有等待时限：手动触发的备份等待24小时，周期性计划备份等待至下一次计划执行时间。超过该时限仍未获取到执行结果，即触发此错误。具体原因包括：
1. 备份管控服务与备份执行服务之间存在时区配置差异，导致任务调度时间计算偏差，执行服务未在预期时
间内启动任务。
2. 备份执行服务关联的执行节点（Worker）不可用，无法接收和执行备份任务。
3. 备份管控节点无法访问备份执行服务接口，导致任务创建请求未送达，或已创建任务的执行结果无法回传
至管控。

**置信等级**

A

**解决方案**

1. 确认备份管控节点与备份执行服务的系统时区一致；若存在偏差，统一时区配置后重新触发备份任务。
2. 确认备份执行节点处于在线状态；若异常或离线，恢复后重新触发备份。
3. 检查管控节点到备份执行服务之间的网络连通性，确认未被防火墙或安全组阻断；网络修复后重新触发备
份任务。

##### ASRBR-BACKUP-CurrentJobIsBlocked

## 错误码

**错误信息**

当前备份任务被该备份计划中的其他任务阻塞。

**原因分析**

同一备份计划中存在正在执行的其他备份任务，由于同一计划内任务不支持并行执行，因此当前任务被阻塞等待。

**置信等级**

A

**解决方案**

1. 等待当前任务执行完成后，下次周期备份可正常进行。
2. 如需立即执行，可先停止当前任务（前提是对应产品类型支持停止操作），然后手动发起备份。

##### ASRBR-BACKUP-InvalidFullBackupCycle

## 错误码

**错误信息**

备份策略的全量备份周期配置无效。 灾备管理中心

**原因分析**

1. 目前仅ECS快照备份的异地备份支持配置全量备份周期，其他场景配置该参数会被判定为无效。
2. 按天备份场景下，备份周期和全量备份周期均只能配置一个值（均表示每隔N天）。
3. 全量备份周期必须大于备份周期，且是备份周期的整数倍。
4. 全量备份周期必须小于备份保存时长。

**置信等级**

B

**解决方案**

1. 确认当前备份类型是否为ECS快照备份的异地备份，仅该场景支持配置全量备份周期；其他备份类型或本
地备份请勿配置该参数。
2. 按天备份场景下，备份周期和全量备份周期都只能配置一个值，请检查并确保每项仅填写一个有效值。
3. 调整全量备份周期，使其大于备份周期且为备份周期的整数倍
4. 调整全量备份周期，使其不超过备份保存时长。

##### ASRBR-BACKUP-InvalidLogRetentionPeriod

## 错误码

**错误信息**

备份策略的日志保留时长无效。

**原因分析**

1. 本地备份场景下：日志保留时长须在 [7, 730] 天范围内。
2. 异地备份场景下：日志保留时长须在 [7, 36500] 天范围内。
3. 日志保留时长不得超过数据备份保留时长。

**置信等级**

A

**解决方案**

1. 根据本地或异地场景，将日志保留时长调整到合法范围内。
2. 确认日志保留时长不超过数据备份保留时长。
3. 调整后重新配置备份策略。

##### ASRBR-BACKUP-

**InvalidBackupRetentionPeriod**

## 错误码

**错误信息**

灾备管理中心备份策略的备份保留时长无效。

**原因分析**

1. 数据库类（RDS/MongoDB等）产品，本地备份保留时长须在 [7, 730] 天范围内；异地备份保留时长须
在 [7, 36500] 天范围内。
2. 其他产品，本地备份保留时长须在 [7, 36500] 天范围内；异地备份保留时长须在 [7, 36500] 天范围
内。
3. 按月备份场景下：保留时长不得小于30天。

**置信等级**

A

**解决方案**

按照原因分析逐项排查并修正备份策略。

##### ASRBR-BACKUP-InvalidBackupCycle

## 错误码

**错误信息**

备份策略的备份周期配置无效。

**原因分析**

1. 按小时备份：备份间隔必须小于24小时。
2. 按天备份：周期数组只能包含1个元素，备份间隔天数必须大于0且不大于备份保留时长。
3. 按周备份：周期数组为空或元素数不在 [星期一～星期日] 范围。
4. 周期参数无法解析为合法整数。

**置信等级**

A

**解决方案**

按照原因分析逐项排查并修正备份策略。

##### ASRBR-BACKUP-InstanceCountExceeded

## 错误码

**错误信息**

一个备份计划内的实例个数超过最大限制。

**原因分析**

一个备份计划默认最多可绑定10个实例。当前计划内实例总数将超过该上限，因此系统将该操作拦截。

**置信等级**

灾备管理中心 A

**解决方案**

1. 按照现有限制调整实例数量，确保单个备份计划内的实例总数不超过上限。
2. 如确有提升上限的需求，可联系研发同学通过修改数据库方式进行调整。

##### ASRBR-BACKUP-NoAvailableLogBackup

## 错误码

**错误信息**

无可用的日志备份。

**原因分析**

1. 当前实例尚未产生可用于恢复的日志备份记录。
2. 选择的恢复时间点不在可恢复的日志备份时间窗口内。
3. 日志备份链路异常，导致最新的日志备份记录未能及时入库。

**置信等级**

A

**解决方案**

1. 若在备份记录详情页面单击「日志」按键后未看到「成功」状态的日志备份，则说明该实例尚未产生可用
日志备份，需等待日志备份成功后再发起恢复。
2. 若所选恢复时间点不在日志保留周期范围内或早于首个可用日志备份时间，则将恢复时间点调整到日志保
留周期范围内，且晚于首个可用日志备份时间后重试。
3. 若该错误反复出现且确认上述两项均已满足，则说明日志备份链路存在异常，请联系产品技术支持协助排
查日志备份链路状态。

##### ASRBR-BACKUP-LocalFailRemoteMarkFail

## 错误码

**错误信息**

由于本地备份失败，对应的异地备份结果被标记为失败。

**原因分析**

在备份管控中，部分类型产品的本地备份依赖产品自身的备份能力。本地备份成功后，备份管控通过异地备份引擎将本地备份集转储至异地。该错误表示本地备份任务已失败，由于异地备份的前置条件（本地备份集）不存在，因此异地备份结果也被标记为失败。

**置信等级**

B

**解决方案**

1. 查看同一备份计划中对应的本地备份记录，确认本地备份失败的具体原因。
灾备管理中心
2. 可通过本地备份记录的错误码、错误信息及TraceId查询日志，进一步定位问题。
3. 解决本地备份失败原因后，重新触发备份任务，异地备份将自动随本地备份成功而恢复。

##### ASRBR-BACKUP-

**DbProductItselfBackupFailed**

## 错误码

**错误信息**

数据库产品自身的备份任务执行失败。

**原因分析**

数据库产品的本地备份是产品自身的能力，由产品侧引擎负责执行。备份管控通过产品侧的查询接口同步备份状态时，发现备份任务状态为失败。该失败发生在产品侧，备份管控无法获取具体的失败细节。

**置信等级**

A

**解决方案**

1. 前往对应数据库产品的控制台，查看备份任务的执行详情，确认具体失败原因。
2. 如无法自行定位，可联系对应数据库产品的技术支持人员协助排查。
3. 问题解决后，等待下一次备份周期自动重试，或手动触发备份。

##### ASRBR-BACKUP-

**DbProductLogicBackupFail**

## 错误码

**错误信息**

数据库产品的逻辑备份任务执行失败。

**原因分析**

逻辑备份是数据库备份的另一种形式，通过DBS（数据库备份服务）引擎执行。备份管控通过DBS接口同步逻辑备份集状态时，发现备份任务状态为失败。本版本未适配确切的错误码，无法提供更细粒度的失败原因。

**置信等级**

B

**解决方案**

1. 通过备份记录的TraceId查询系统日志，定位DBS逻辑备份引擎的具体错误详情。
2. 也可前往DBS产品侧控制台，查看对应逻辑备份计划的执行情况。
3. 问题解决后，等待下一次备份周期自动重试，或手动触发备份。
灾备管理中心

##### ASRBR-BACKUP-ModifyPolicyFailed

## 错误码

**错误信息**

调用下游接口修改备份策略失败。

**原因分析**

ASRBR管控在下发备份策略变更时，会调用下游产品或下游备份引擎的策略修改、策略启动、或策略停止接口。当下游接口返回失败，或响应体为空时，会记录此错误码。

**置信等级**

B

**解决方案**

1. 通过 traceId 查询系统日志，定位实际调用的下游产品接口及其返回的errorCode、errorMessage。
2. 根据下游返回的错误信息，结合实际的下游产品或备份引擎进行排查。常见原因包括策略参数超限、下游
产品版本不兼容等。
3. 问题解决后，在ASRBR控制台重新提交策略变更；若为删除实例连带的停止策略失败，可重新触发删除
操作。

##### ASRBR-BACKUP-

**HbrBackupJobUnavailable**

## 错误码

**错误信息**

无法从HBR-Console服务获取正在执行的备份任务。

**原因分析**

所有走HBR路径的产品（OSS、NAS、ECS、ECS云盘、OTS、VMware、GWS等）在同步单次备份进度时，ASRBR管控会按hbrPlanId（或hbrJobId）+ 同步时间窗分页调HBR-Console的 DescribeBackupJobs接口。当翻完所有分页后仍未找到落在时间窗内的BackupJob时，记录本错误码。 常见根因：
1. HBR-Console 侧尚未创建对应Job，或hbrPlanId与实际不匹配、plan已被删除。
2. 备份Job被人工删除，导致查询时已不存在对应记录。
3. 备份Job的CreatedTime落在同步时间窗之外，常见于管控与HBR服务时钟漂移、或策略触发点偏差。
4. HBR接口本身抛异常导致查询返回空结果。

**置信等级**

B

**解决方案**

灾备管理中心
1. 通过备份实例日志中的traceId 检索管控日志，确认调用DescribeBackupJobs时使用的 hbrPlanId、时
间窗与HBR返回内容。
2. 前往HBR-Console侧核对对应hbrPlanId的Job是否存在，以及其CreatedTime是否落在同步时间窗内。
3. 按具体原因分别处理：
时钟漂移：统一管控节点与HBR节点的时区或时间。 plan缺失或策略下发失败：检查策略下发链路是否成功。 Job被人工删除：确认是否需要重新触发备份。
4. 处理后等待下一次备份周期自动恢复，或手动重新触发备份。

##### ASRBR-BACKUP-ExecuteBackupJobFailed

## 错误码

**错误信息**

执行备份任务失败。

**原因分析**

当用户手动发起备份或周期调度触发备份时，ASRBR管控会调用产品侧/备份引擎侧的手动备份接口。若下产品侧/备份引擎侧明确返回执行失败，则记录此错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询日志，定位下游产品侧或备份引擎返回的errorCode、errorMessage以及请求参数。
2. 根据下游返回的错误信息排查具体失败原因。
3. 处理后在ASRBR控制台重新发起手工备份或等待下一次计划周期自动重试。

##### ASRBR-BACKUP-

**BackupSetInfoUnavailable**

## 错误码

**错误信息**

无法从产品侧或备份引擎侧获取到备份集信息。

**原因分析**

ASRBR管控在同步备份记录时，会调用产品侧或备份引擎的查询接口获取备份集列表。当接口返回结果为空、数据结构不完整或在同步时间窗内尚未产生对应的备份集记录时，记录本错误码。常见根因：
1. 备份任务仍在执行中，产品侧尚未生成备份集记录，管控在同步窗口内暂时无法获取，后续轮询可能恢
复。
2. 备份策略配置异常（如计划已被产品侧删除或暂停），导致预期的备份集未被产生。
3. 产品侧接口调用成功但返回空数据，可能是查询条件不匹配（如时间窗偏差）。
灾备管理中心

**置信等级**

B

**解决方案**

1. 可能为暂时性问题，等待下一轮同步即可自动恢复。
2. 若持续出现，通过备份实例日志的traceId查询系统日志，确认调用的产品接口名称、查询参数与返回内
容。
3. 前往产品侧控制台确认备份计划是否正常运行、是否有对应时间段的备份集产生。
4. 若为查询条件不匹配（如时间窗偏差），检查管控与产品侧的时钟是否一致。

##### ASRBR-BACKUP-

**BackupJobStatusUnmapped**

## 错误码

**错误信息**

**原因分析**

ASRBR管控在同步各产品的备份任务状态时，会将产品侧返回的原始状态字符串通过映射方法转为ASRBR 内部状态枚举。当映射结果为空时，说明产品侧返回了一个ASRBR当前版本未处理的新状态值，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过备份实例日志的traceId查询系统日志，定位产品侧返回的原始状态值。
2. 确认该状态值是否为产品侧新增的状态（如产品版本升级新增了任务状态），若是，则需要ASRBR管控
侧升级适配。
3. 临时处理：该备份记录会被跳过不做状态更新，等待下一轮同步重试。若产品侧状态后续变为已知值则自
动恢复。
4. 若持续复现，请将产品名称、返回的原始状态值、traceId提供给研发，推动版本适配。

##### ASRBR-BACKUP-BackupSetStatusFailed

## 错误码

**错误信息**

从产品侧或备份引擎获取到的备份集状态为失败。

**原因分析**

灾备管理中心 ASRBR管控在同步备份集记录时，解析产品侧返回的备份集状态字段，发现该备份集已被产品侧标记为失败。这是产品侧/备份引擎明确反馈“该备份任务执行失败”的兆底错误码，具体失败原因由产品侧决定。涉及的场景包括：
1. Heimdallr 异地备份引擎返回备份集状态为FAILED或LOST（备份集丢失）。
2. DBS统一备份接口返回备份集backupStatus为ERROR。
3. DRDS跨区域备份集BackupSetStatus为FAILED。
4. PolarDB-X集群备份集状态为ERROR或WARNING。

**置信等级**

B

**解决方案**

1. 前往对应产品的控制台或备份引擎管理界面，查看该备份集的执行详情，确认产品侧给出的具体失败原
因。
2. 若备份记录中有更详细的errorCode/errorMessage（来自产品侧返回的resultMessage），可据此进
一步定位。
3. 根据产品侧的错误信息进行处理，处理完成后等待下一次备份周期自动重试或在ASRBR控制台手动触发
备份。

##### ASRBR-BACKUP-

**BackupInstanceCheckFailed**

## 错误码

**错误信息**

备份实例校验失败。

**原因分析**

创建或修改备份计划时，管控会对目标实例进行入口预检，预检不通过即记录本错误码。这是一个聚合错误码，本身不区分具体原因，真正原因需结合日志中的message关键字（如 InstanceStatusNotSupported、InstanceResourceNotFound等）判断。常见的失败原因分为以下几类：
1. 通用前置校验失败：主云信息缺失（MainCloudNotExist）、请求区域与系统区域不一致
（RegionNotMatched）、实例ID或实例类型为空。
2. 实例不存在（InstanceResourceNotFound）：按实例ID在对应产品侧查询不到实例，常见于实例ID错
误、实例已释放或OSS Bucket不存在（NoSuchBucket）。
3. 实例状态不支持（InstanceStatusNotSupported）：实例未处于可备份状态。例如数据库类要求
Running/Normal、ECS云盘备份要求Running或 Stopped、ECS文件备份要求Running、OTS要求 Normal、云桌面关联的ECS状态异常等。
4. 实例类型不支持（InstanceTypeNotSupported）：如只读/灾备/临时实例、PolarDB AI版等不支持备
份。
5. 实例规格不支持（InstanceCategoryNotSupported）：如RDS非高可用/金融版、Redis非Tair实例、
GPDB存储模式不符、ADB节点规格不在白名单等。
6. 引擎或版本不支持（InstanceVersionNotSupported）：目标引擎/版本不在支持列表或该引擎不支持所
选的逻辑备份方式（如SQLServer、PostgreSQL的逻辑备份）。
7. ECS文件备份未安装备份客户端：ECS实例未安装HBR备份客户端（Agent）或客户端不在线。
灾备管理中心
8. 云桌面存储卷已加密（VolumeEncryptionEnabled）：无影云桌面存储卷开启了加密，不支持备份。
9. 实例已被占用：DRDS的RDS子实例已被其他备份计划绑定（DrdsRdsSubInstanceAlreadyBound）
或该RDS已存在DRDS备份计划（RdsHasExistingDrdsPlan）。
0. 实例内数据异常：DRDS实例下无数据库（InstanceNotContainDatabase）、数据库状态非正常
（DatabaseStateIncorrect）、查不到DB挂载的RDS实例等。
1. 下游产品接口调用失败：调用产品侧查询接口返回错误（透传下游errorMessage）或查询实例拓扑失败
（如PolarDB-X拓扑查询失败）。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，先定位是哪个产品、命中了上述哪一类失败原因（日志中的message关键字
或预检返回内容）。
2. 若为实例不存在：核对实例ID是否正确、实例是否已释放。
3. 若为状态不支持：前往对应产品侧确认实例状态，等待实例恢复到可备份状态（如Running）后重试。
4. 若为类型/规格/版本不支持：对照产品能力边界确认该实例是否在支持范围内，改用受支持的实例、规格
或备份方式。
5. 若为ECS文件备份未安装客户端：在目标ECS上安装并启动HBR备份客户端，确认客户端在线后重试。
6. 若为云桌面存储卷加密：该场景暂不支持备份，需改用未加密存储卷的云桌面。
7. 若为实例已被占用：DRDS/RDS场景确认该实例或其子实例是否已被其他备份计划绑定，解除已有绑定
或复用现有计划。
8. 若为下游接口调用失败：结合日志中透传的下游errorMessage判断，必要时联系对应产品负责人协助排
查。
9. 修正后重新提交备份计划创建/修改请求。

##### ASRBR-BACKUP-DeleteBackupPlanFailed

## 错误码

**错误信息**

删除备份计划失败。

**原因分析**

删除备份实例/备份计划时，管控调用下游产品的删除接口失败。当接口返回为空、返回失败状态或调用过程抛出异常时记录本错误码。涉及NAS、GWS、ECS云盘、ODPS等产品。

**置信等级**

B

**解决方案**

1. 通过备份实例日志的traceId查询系统日志，定位调用的下游删除接口与返回的错误信息。
2. 确认目标实例状态是否正常、是否存在阻止删除的关联资源。
3. 问题解决后，重新发起删除操作。
灾备管理中心

##### ASRBR-BACKUP-

**HbrBackupPlanCreationFailed**

## 错误码

**错误信息**

**原因分析**

为备份实例创建备份计划时，管控需要调用HBR-Console的创建备份计划接口。当HBR-Console接口返回为空、返回失败或调用抛出异常时记录本错误码。这是一个通用的「HBR-Console 侧创建备份计划失败」 错误，涉及所有由HBR-Console承载备份的产品（ECS文件、ECS云盘、无影云桌面、OSS、NAS、 OTS、ODPS、ES、ADB、VMware等）。常见原因包括：
1. HBR-Console服务不可用或网络异常，导致创建接口调用失败。
2. HBR-Console侧参数校验不通过、Bucket/Vault配额不足或仓库配置异常。
3. 实例信息异常或与备份计划关联的资源状态不满足要求。
4. 仅针对ECS文件备份：该备份方式依赖在被保护ECS主机上安装的HBR备份客户端（Agent），当 Agent
未安装、未在线（心跳超时）或云助手未激活时，无法创建或关联备份计划。

**说明**

此原因仅适用于ECS文件备份。 ECS云盘、无影云桌面走云盘快照，OSS/NAS/OTS/ODPS/ES/ADB走云产品接口或快照，VMware走无代理备份网关，这些产品在被保护主机/实例上均不需要安装Agent。

**置信等级**

B

**解决方案**

1. 通过备份实例日志的traceId查询系统日志，定位调用HBR-Console创建备份计划时的请求参数与返回内
容，确认失败发生在哪个产品的备份流程。
2. 若日志显示HBR-Console服务调用失败或超时：确认HBR-Console服务状态与网络连通性正常后重试。
3. 若日志提示配额或仓库问题：确认备份仓库（Vault）/ Bucket配额是否充足、仓库配置是否正常。
4. 仅当为ECS文件备份且日志出现Agent未安装/未在线（如ECS Agent Uninstall/Please Install The
ECS Agent）或云助手未激活等信息时，在目标ECS上安装并启动HBR备份客户端，确认客户端在线后重试。
5. 若无法明确原因，提取请求参数与响应内容，联系产品研发协助排查。
6. 问题解决后，重新触发备份计划创建。

##### ASRBR-BACKUP-InstanceStillBound

## 错误码

灾备管理中心

**错误信息**

备份计划下仍存在未解绑的实例。

**原因分析**

删除备份计划前，会校验该计划下是否仍存在绑定的实例。当仍有实例未解绑时，为避免误删导致实例失去保护，拒绝删除并记录本错误码。

**置信等级**

B

**解决方案**

1. 前往备份计划管理页面，确认该计划下仍关联的实例。
2. 先将计划下的实例逐个解绑。
3. 确认计划下已无绑定实例后，重新发起删除操作。

##### ASRBR-BACKUP-

**InvalidAdvancedRetentionPolicy**

## 错误码

##### ASRBR-BACKUP-InvalidAdvancedRetentionPolicy

**错误信息**

特殊保留策略配置无效。

**原因分析**

创建或修改备份计划时，管控会校验备份策略中的特殊保留规则（按年保留时长/按月保留时长/按周保留时长）。当配置不合法时记录本错误码。常见原因包括：
1. 存在重复的保留规则类型。
2. 某规则的保留时长为空或不是正整数。
3. 保留时长未满足从长到短的递减约束（按年 > 按月 > 按周 > 基础保留时长）。

**置信等级**

B

**解决方案**

1. 检查高级保留策略配置，确保每种保留类型（年/月/周）不重复。
2. 确保每个保留时长均为正整数。
3. 确保保留时长满足递减关系：按年保留时长 > 按月保留时长 > 按周保留时长 > 基础保留时长。
4. 调整后重新提交备份计划。

##### ASRBR-BACKUP-

**DbsLogicalStorageNotFound**

## 错误码

灾备管理中心

**错误信息**

DBS逻辑备份存储实体未找到。

**原因分析**

修改逻辑备份策略（如备份周期、保留天数等）时，管控需要从DBS查询并关联有效的存储实体。 当DBS返回的存储实体列表为空或无法匹配到与管控存储池对应的主存储/异地存储实体时，记录本错误码。常见根因：
1. DBS侧存储实体尚未初始化或已被清理。
2. 管控存储池ID与DBS侧存储实体的关联关系缺失或不匹配。
3. 配置了异地复制存储池，但DBS侧尚未注册对应的异地存储实体。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，确认查询存储实体时使用的参数与DBS返回内容。
2. 核对管控存储池配置是否与DBS侧存储实体正确关联。
3. 若为异地存储实体缺失，确认DBS侧是否已完成异地存储注册。
4. 问题解决后，重新发起备份策略修改。

##### ASRBR-BACKUP-DbsLogicalPlanNotReady

## 错误码

**错误信息**

DBS逻辑备份计划状态未就绪。

**原因分析**

创建并启动DBS逻辑备份计划时，管控会先查询DBS侧该备份计划的当前状态。 当计划已存在但状态仍为wait（等待中）或checking（校验中）而非running（运行中）时，记录本错误码。常见根因：
1. DBS侧计划刚创建完成，正在进行初始化或连通性校验，尚未转为running状态。
2. DBS侧计划启动后，由于源端连接异常或配置校验不通过，长时间停留在非running状态。

**置信等级**

B

**解决方案**

1. 可能为暂时性问题（DBS初始化中），等待下一轮同步即可自动恢复。
2. 若持续出现，通过traceId查询系统日志，确认DBS侧计划的实际状态与失败原因。
3. 前往DBS产品侧确认该逻辑备份计划的状态，排查源端连接或配置问题后，等待计划状态恢复为
running。 灾备管理中心

##### ASRBR-BACKUP-DbsLogicalJobNotFound

## 错误码

**错误信息**

DBS逻辑备份任务未找到。

**原因分析**

停止逻辑备份计划时，管控需要先从 DBS 查询对应的备份计划/任务是否存在。 当DBS describeBackupPlanList接口返回为空或查询失败时，表示DBS侧不存在该备份任务，记录本错误码。常见根因：
1. 该逻辑备份计划在DBS侧已被清理或删除。
2. DBS侧与管控侧的计划关联信息不一致（如planId已变更）。
3. DBS接口查询异常导致未返回有效结果。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，确认管控查询DBS时使用的planId与DBS返回内容。
2. 前往DBS产品侧确认该逻辑备份计划是否仍然存在。
3. 若计划确实已被删除，管控侧需同步清理该计划的关联状态。
4. 若为查询异常，确认DBS服务状态正常后重试。

##### ASRBR-BACKUP-BackupTimesExceeded

## 错误码

**错误信息**

备份次数超过产品侧限制。

**原因分析**

该错误发生在PolarDB实例备份场景下。 ASRBR管控向PolarDB产品侧发起创建备份请求时，PolarDB产品侧返回「备份次数超限」，表示该实例在产品侧允许的备份次数已经用尽，管控随即将本次备份记录标记为失败。 PolarDB产品侧对单个实例在一定周期内可创建的备份次数存在上限。当针对同一实例的备份请求（包括按策略自动备份、手动备份等）在短时间内过于频繁，累计次数超过该上限时，产品侧会拒绝新的备份请求， 从而触发本错误。

**置信等级**

B

**解决方案**

灾备管理中心
1. 检查该PolarDB实例近期的备份触发情况，确认是否存在过于频繁的手动备份或备份策略配置的周期过
密。
2. 适当降低备份频率或等待一段时间后再重新触发备份。
3. 如需了解该实例在产品侧的具体备份次数限制，可咨询PolarDB产品侧。确认次数恢复后，等待下一次备
份周期自动重试或在控制台手动重试。

#### RESTORE

##### ASRBR-RESTORE-InstanceCountExceeded

## 错误码

**错误信息**

实例数量超出最大限制。

**原因分析**

单次恢复任务 / 恢复计划可包含的实例数量存在上限。本次操作后实例总数将超过该上限，系统予以拦截以保证恢复调度稳定。

**置信等级**

A

**解决方案**

1. 减少本次选择的恢复实例数量，使总数不超过上限。
2. 或分批创建多个恢复任务。
3. 调整后重新提交。

##### ASRBR-RESTORE-

**RestoreToExistingInstanceFailed**

## 错误码

##### ASRBR-RESTORE-RestoreToExistingInstanceFailed

**错误信息**

恢复到已有实例校验不通过。

**原因分析**

恢复至已有实例需满足目标实例与备份源的兼容性要求。 校验不通过常见原因：目标实例类型/版本/规格与备份源不匹配、目标实例状态异常、目标实例容量不足以容纳恢复数据。

**置信等级**

B

**解决方案**

灾备管理中心
1. 核对目标实例的类型、版本、规格是否与备份源兼容。
2. 确认目标实例状态正常且容量足够。
3. 修正目标实例配置后重新提交或改为恢复至新实例。

##### ASRBR-RESTORE-RecoveryPlanInUse

## 错误码

**错误信息**

当前恢复计划存在已绑定的恢复资源，无法删除。

**原因分析**

该恢复计划仍绑定有恢复资源，系统要求先解除资源绑定后才能删除。

**置信等级**

A

**解决方案**

1. 进入恢复计划详情，解除该计划下所有已绑定的恢复资源。
2. 确认无绑定资源后重新执行删除恢复计划操作。

##### ASRBR-RESTORE-

**TargetInstanceAlreadyExists**

## 错误码

**错误信息**

恢复方式为“恢复至新实例”，但同名实例已存在。

**原因分析**

1. 用户手动指定的实例名（如OSS Bucket 名称）在目标系统中已存在。
2. 系统采用自动命名生成实例名时，连续多次尝试后仍与现有实例冲突。

**置信等级**

A

**解决方案**

1. 修改新实例的名称，确保在目标系统中唯一后重新提交。
2. 若采用自动命名仍持续冲突，请稍后重试或人工指定实例名称。
3. 若希望恢复到已有实例，请将恢复方式改为"恢复至已有实例"。

##### ASRBR-RESTORE-TargetInstanceNotFound

## 错误码

灾备管理中心

## 错误码

**错误信息**

恢复方式为"恢复至已有实例"，但目标实例不存在。

**原因分析**

1. 目标实例名称或ID填写错误。
2. 目标实例已被删除或不在当前组织可访问范围内。
3. 目标产品侧实际查询不到该实例。

**置信等级**

A

**解决方案**

1. 核对目标实例名称是否正确，并确认实例存在且处于可访问状态。
2. 若实例已删除，请先创建对应实例或将恢复方式改为"恢复至新实例"。

##### ASRBR-RESTORE-

**InvalidRecoveryTimestampFormat**

## 错误码

##### ASRBR-RESTORE-InvalidRecoveryTimestampFormat

**错误信息**

恢复时间点格式非法，无法解析。

**原因分析**

创建按时间点恢复任务时，管控需要解析用户传入的时间戳。当传入的时间戳字符串无法被正确解析时，记录本错误码。

**置信等级**

A

**解决方案**

1. 核对传入的恢复时间点格式是否正确（应为符合要求的UTC时间格式）。
2. 参照接口文档修正时间点格式后重新提交恢复任务。

##### ASRBR-RESTORE-RecoveryPolicyInUse

## 错误码

**错误信息**

恢复策略仍被恢复计划关联，无法删除。 灾备管理中心

**原因分析**

删除恢复策略前，系统会校验该策略是否仍关联恢复计划。当仍存在关联的恢复计划时，为避免影响正在使用的计划，拒绝删除并记录本错误码。

**置信等级**

A

**解决方案**

1. 前往恢复策略页面，确认仍关联该策略的恢复计划。
2. 先解除关联或删除相关恢复计划。
3. 确认无关联后，重新发起删除操作。

#### INSTANCE

##### ASRBR-INSTANCE-

**ProductInstanceInfoQueryFail**

## 错误码

##### ASRBR-INSTANCE-ProductInstanceInfoQueryFail

**错误信息**

从产品侧查询实例信息失败。

**原因分析**

ASRBR管控在备份时会调用下游产品接口拉取实例元信息或拓扑，用于策略生成、元数据获取或者页面展示。当接口返回但内容为空、或标记为失败时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过管控日志中的traceId检索该次查询的完整调用信息，确认下游接口名称、请求参数（instanceId、
primaryKey等）与返回内容。
2. 核对查询条件是否正确：如实例ID是否真实存在、目标账号是否与实例归属账号一致。
3. 确认管控使用的AK/角色是否具备调用该产品对应接口的权限。
4. 问题解决后，等待下一次同步周期自动重试或在ASRBR控制台重新触发相关操作。

##### ASRBR-INSTANCE-

**OdpsMmaSourceNotReady**

## 错误码

**错误信息**

灾备管理中心 MMA数据源未就绪。

**原因分析**

MMA数据源已存在但尚未完成初始化加载。MMA在首次注册数据源后需要加载元数据信息（如表结构、分区信息等），此过程可能耗时较长，期间数据源处于未就绪状态，无法执行备份操作。

**置信等级**

B

**解决方案**

1. 等待MMA数据源完成加载（可通过MMA控制台查看数据源状态）。
2. 如长时间未就绪，检查MMA服务是否正常运行、ODPS项目访问权限是否正确。
3. 数据源加载完成后重新触发备份任务。

##### ASRBR-INSTANCE-

**OdpsMmaSourceNotFound**

## 错误码

**错误信息**

MMA数据源不存在。

**原因分析**

系统在执行MaxCompute（ODPS）备份时，通过MMA（MaxCompute Migration Assist）组件查找数据源配置，但未找到对应的数据源记录。 可能原因：数据源尚未注册到MMA、数据源配置被意外删除或配置的数据源标识与实际不匹配。

**置信等级**

A

**解决方案**

1. 确认MMA数据源已正确注册且数据源名称与备份计划配置一致。
2. 如数据源被误删，需重新创建MMA数据源配置。
3. 核对ODPS项目和Endpoint信息是否与MMA数据源注册时一致。

##### ASRBR-INSTANCE-

**MmaBackupJobQueryFailed**

## 错误码

**错误信息**

MMA备份任务查询失败。 灾备管理中心

**原因分析**

系统在查询MMA备份任务执行状态时失败。 可能原因：MMA服务暂时不可用、网络连接中断或任务ID对应的记录已过期被清理。

**置信等级**

B

**解决方案**

1. 确认MMA服务运行状态正常。
2. 检查备份系统与MMA服务之间的网络连通性。
3. 如任务记录已不存在，可重新触发备份任务。
4. 如问题反复出现，建议排查MMA服务端的稳定性。

##### ASRBR-INSTANCE-MmaBackupJobFailed

## 错误码

**错误信息**

MMA备份任务执行失败。

**原因分析**

MMA备份任务已成功创建并开始执行，但在执行过程中失败。 可能原因：ODPS表数据导出异常、存储空间不足、网络中断导致数据传输失败或单个表/分区的数据量超出 MMA处理能力。

**置信等级**

B

**解决方案**

1. 查看MMA任务详情，确认具体失败的表或分区信息。
2. 检查目标存储空间是否充足。
3. 验证ODPS项目访问权限和网络连通性。
4. 如个别表失败，可尝试重新触发备份或排查该表的数据异常。

##### ASRBR-INSTANCE-

**MmaBackupJobCreateFailed**

## 错误码

**错误信息**

MMA备份任务创建失败。

**原因分析**

灾备管理中心系统通过MMA组件创建MaxCompute备份任务时失败。 可能原因：MMA服务异常、数据源配置不正确、ODPS 项目权限不足或MMA任务队列已满。

**置信等级**

B

**解决方案**

1. 确认MMA服务运行正常且可访问。
2. 检查ODPS项目的AccessKey和Secret是否具备足够权限。
3. 查看MMA服务端日志，确认具体失败原因。
4. 如因任务队列满导致失败，等待现有任务完成后重试。

##### ASRBR-INSTANCE-EsSnapshotQueryFailed

## 错误码

**错误信息**

ES快照查询失败。

**原因分析**

系统在查询Elasticsearch快照状态时失败。 可能原因：ES实例连接异常、快照仓库（repository）未正确配置或已被删除、ES集群健康状态异常或网络中断导致API调用超时。

**置信等级**

A

**解决方案**

1. 确认ES实例运行状态正常，集群健康状态为green或yellow。
2. 检查快照仓库（snapshot repository）配置是否完整且可访问。
3. 验证备份系统与ES实例之间的网络连通性。
4. 如问题持续，可尝试在ES端手动执行快照状态查询（GET _snapshot//_all）以排查根因。

##### ASRBR-INSTANCE-EsAuthenticationFailed

## 错误码

**错误信息**

ES认证失败。

**原因分析**

系统在连接Elasticsearch实例时，使用配置的用户名和密码进行认证失败。 可能原因：用户名或密码错误、ES实例开启了安全认证但未正确配置凭据或ES实例的认证策略发生变更。 灾备管理中心

**置信等级**

A

**解决方案**

1. 核实备份计划中配置的Elasticsearch用户名和密码是否正确。
2. 确认目标ES实例的安全认证已正确开启且所用账号具备快照相关权限。
3. 如密码已变更，请更新备份计划中的凭据配置后重试。

##### ASRBR-INSTANCE-OdpsProjectEmpty

## 错误码

**错误信息**

ODPS项目内无可备份对象（表/函数/资源全为空）。

**原因分析**

1. 备份计划中未正确指定项目名称。
2. 所指定的项目已被删除或不存在。
3. 配置信息传递过程中项目字段丢失。

**置信等级**

A

**解决方案**

1. 核对备份计划中指定的MaxCompute项目名称是否正确。
2. 确认项目配置完整，未遗漏必填字段。
3. 修正项目配置后重新创建备份计划。

##### ASRBR-INSTANCE-OdpsConfigInvalid

## 错误码

**错误信息**

ODPS配置信息无效。

**原因分析**

ODPS接入所需的配置信息不正确，例如AccessKey/SecretKey错误、Endpoint填写有误或项目名不存在，导致系统无法成功连接并访问ODPS项目。

**置信等级**

B

**解决方案**

1. 核对ODPS的AccessKey、SecretKey是否正确且有效。
灾备管理中心
2. 检查Endpoint与项目名是否填写正确。
3. 确认该AK/SK具备访问目标项目的权限后重新提交。

##### ASRBR-INSTANCE-

**OdpsDataTypeVersionUnsupported**

## 错误码

##### ASRBR-INSTANCE-OdpsDataTypeVersionUnsupported

**错误信息**

ODPS项目数据类型版本不是2.0。

**原因分析**

ODPS备份要求项目采用2.0数据类型版本。当前项目的数据类型版本低于2.0，不满足备份兼容性要求，因此无法备份。

**置信等级**

A

**解决方案**

1. 在ODPS侧将项目数据类型版本升级至2.0。
2. 升级前请评估对现有业务的影响，必要时咨询ODPS管理员。
3. 升级完成后重新创建备份计划。

##### ASRBR-INSTANCE-

**OdpsExternalTableCreateFailed**

## 错误码

##### ASRBR-INSTANCE-OdpsExternalTableCreateFailed

**错误信息**

ODPS外部表创建失败。

**原因分析**

ODPS备份/恢复过程依赖创建外部表（External Table）作为数据中转。 创建外部表失败常见原因：外部存储（如OSS）路径/权限配置错误、AK/SK 无访问权限、外部表所需插件/ 权限未开通、网络不可达。

**置信等级**

B

**解决方案**

1. 检查外部存储（OSS）的路径、AK/SK与访问权限是否正确。
2. 确认ODPS项目已开通创建外部表所需的权限/插件。
灾备管理中心
3. 确认网络连通后重新执行，若仍失败请联系管理员排查。

##### ASRBR-INSTANCE-

**OdpsRestoreTaskStopUnsupported**

## 错误码

##### ASRBR-INSTANCE-OdpsRestoreTaskStopUnsupported

**错误信息**

ODPS恢复任务不支持停止。

**原因分析**

ODPS恢复任务一旦启动即不支持中途停止，以保证恢复数据的完整性与一致性。强行中断可能导致数据不完整。

**置信等级**

A

**解决方案**

1. 等待ODPS恢复任务自然执行完成。
2. 如需重新恢复，请在任务完成后重新发起。
3. 若任务长时间异常挂起，请联系管理员排查。

##### ASRBR-INSTANCE-InstanceNotFound

## 错误码

**错误信息**

找不到实例。

**原因分析**

1. 实例已被删除或释放，不再存在于管控侧。
2. 实例ID或名称填写错误。
3. 实例不在当前组织的可见范围内。
4. 目标产品侧查询不到该实例。

**置信等级**

B

**解决方案**

1. 核对实例ID或名称是否正确。
2. 确认实例未被删除且在当前组织内可见。
3. 若为同步延迟，请稍后重试。
灾备管理中心

##### ASRBR-INSTANCE-OtsBackupTimeConflict

## 错误码

**错误信息**

OTS备份策略中增量与全量备份的执行时间分秒不能相同。

**原因分析**

OTS备份要求增量备份与全量备份的执行时间在分、秒上不能完全一致，以避免两类任务同时触发产生调度冲突。

**置信等级**

A

**解决方案**

1. 调整增量备份或全量备份的执行时间，使二者在分或秒上至少有一个不同。
2. 调整后重新提交备份策略。

##### ASRBR-INSTANCE-

**RdsHasExistingDrdsPlan**

## 错误码

**错误信息**

RDS实例已存在DRDS备份计划。

**原因分析**

该RDS实例已被某个DRDS备份计划包含，不允许再创建独立的RDS备份计划，以避免重复备份与策略冲突。

**置信等级**

A

**解决方案**

1. 查看该RDS所属的DRDS备份计划，复用或调整其策略以覆盖该实例的备份需求。
2. 如确需为该RDS单独创建备份计划，请先从对应的DRDS备份计划中移除该实例。

##### ASRBR-INSTANCE-

**DrdsRdsSubInstanceAlreadyBound**

## 错误码

##### ASRBR-INSTANCE-DrdsRdsSubInstanceAlreadyBound

灾备管理中心

**错误信息**

DRDS备份冲突，下挂的RDS已存在备份计划。

**原因分析**

DRDS备份会作用到下挂的所有RDS实例。当某个下挂的RDS已经单独创建了备份计划时，再为该DRDS创建备份会出现重复备份与数据冲突，系统予以拦截。

**置信等级**

A

**解决方案**

1. 查找该DRDS下挂的RDS实例，确认是否已存在RDS级别的备份计划。
2. 如需保留DRDS备份计划，请先删除冲突的RDS备份计划后再创建。

##### ASRBR-INSTANCE-

**DiskNotBelongToInstance**

## 错误码

**错误信息**

指定的云盘不属于目标实例。

**原因分析**

创建或校验ECS云盘备份时，管控会查询目标ECS实例的云盘列表并校验传入的云盘归属。当传入的云盘不在该实例的云盘集合中或实例查询不到任何云盘时，记录本错误码。

**置信等级**

B

**解决方案**

1. 核对传入的云盘ID是否确实挂载在目标ECS实例上。
2. 前往ECS产品侧确认实例的云盘挂载情况。
3. 修正云盘选择后重新提交。

##### ASRBR-INSTANCE-

**EcsImageSizeExceedsSystemDisk**

## 错误码

##### ASRBR-INSTANCE-EcsImageSizeExceedsSystemDisk

**错误信息**

恢复镜像大小超过系统盘容量。

**原因分析**

灾备管理中心创建ECS整机恢复任务时，系统会校验恢复镜像大小与目标系统盘容量。当镜像大小超过系统盘容量时，无法完成恢复，记录本错误码。

**置信等级**

A

**解决方案**

1. 确认目标实例的系统盘容量，使其不小于恢复镜像大小。
2. 调大目标系统盘容量或选择系统盘容量满足要求的目标实例后，重新发起恢复。

##### ASRBR-INSTANCE-

**OdpsDeleteBlockedByRunningJob**

## 错误码

##### ASRBR-INSTANCE-OdpsDeleteBlockedByRunningJob

**错误信息**

存在正在执行的备份任务，无法删除ODPS实例。

**原因分析**

删除ODPS备份计划或解绑ODPS实例前，系统会校验是否存在处于排队中、备份中或初始化中的备份任务。当存在正在进行的任务时，为避免中断，拒绝删除并记录本错误码。

**置信等级**

B

**解决方案**

1. 前往备份计划详情页面，确认该实例正在进行的备份任务。
2. 等待相关备份任务执行完成或先停止对应任务。
3. 确认无进行中的任务后，重新发起删除操作。

##### ASRBR-INSTANCE-

**OdpsDeletedMetaCleanupFailed**

## 错误码

##### ASRBR-INSTANCE-OdpsDeletedMetaCleanupFailed

**错误信息**

清理ODPS已删除表/分区的元数据失败。

**原因分析**

ODPS备份清理阶段，系统需要将本次已删除的表/分区元数据记录并入库。 当写入已删除表/分区的中间文件失败，或将已删除分区入库失败时，记录本错误码。该错误不阻断主流程， 但会导致对应清理动作未完成。 灾备管理中心

**置信等级**

B

**解决方案**

1. 通过备份实例日志的traceId查询系统日志，定位清理失败的具体阶段（写文件或入库）与错误信息。
2. 常见原因包括：本地临时文件写入异常、数据库写入异常。
3. 若无法明确原因，提取日志内容联系ODPS备份负责人协助排查。
4. 问题解决后，等待下一次备份周期自动重试。

##### ASRBR-INSTANCE-

**OdpsTempTableDeleteFailed**

## 错误码

**错误信息**

删除ODPS临时表失败。

**原因分析**

ODPS增量备份收尾阶段，系统会调用MMA接口删除备份过程中产生的临时表。 当删除接口返回失败时，记录本错误码。该错误不阻断备份记录到达终态，但临时表可能残留。

**置信等级**

B

**解决方案**

1. 通过备份实例日志的traceId查询系统日志，定位删除临时表失败的返回信息。
2. 前往MaxCompute侧确认临时表是否残留，必要时手动清理。
3. 若无法明确原因，提取日志内容联系产品研发协助排查。

##### ASRBR-INSTANCE-

**OtsClusterNameFormatInvalid**

## 错误码

**错误信息**

OTS集群名称格式非法。

**原因分析**

OTS备份时，管控需要根据集群名称拼接集群域名或从TianJi查询集群可用区。 当集群名称为空、按分隔符拆分后段数不足或遍历相关产品仍无法从TianJi获取到可用区时，记录本错误码。 灾备管理中心

**置信等级**

B

**解决方案**

1. 核对传入的OTS集群名称是否正确、格式是否符合规范。
2. 通过traceId查询日志，确认从天基获取集群信息的返回内容。
3. 若无法明确原因，提取集群名称与日志内容联系OTS产品负责人协助排查。

##### ASRBR-INSTANCE-

**OtsTiangongCnameSetupFailed**

## 错误码

**错误信息**

为OTS设置天宫CNAME解析失败。

**原因分析**

天宫部署环境下，管控需要为OTS实例域名在PrivateZone设置CNAME解析。 当源域名或集群域名为空或调用DNS解析设置过程中发生异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位CNAME设置失败的具体原因与相关域名信息。
2. 常见原因包括：域名信息缺失、PrivateZone配置异常、DNS解析服务不可用。
3. 若无法明确原因，提取请求参数与响应内容，联系OTS/DNS相关负责人协助排查。

##### ASRBR-INSTANCE-

**OtsTiangongVpcQueryFailed**

## 错误码

**错误信息**

查询天宫VPC信息失败。

**原因分析**

天宫部署环境下，管控需要查询asrbr-backup所在VPC的VpcId（用于OTS CNAME绑定）。 当查询接口异常、返回为空、返回失败、VPC名称与预期不一致、VpcId为空或VPC下无交换机时，记录本错误码。

**置信等级**

灾备管理中心 B

**解决方案**

1. 通过traceId查询系统日志，定位VPC查询失败的具体原因。
2. 确认asrbr-backup所在VPC的配置是否正确（VPC名称、VpcId、交换机）。
3. 若无法明确原因，提取请求参数与响应内容，联系VPC/网络负责人协助排查。

##### ASRBR-INSTANCE-

**SingleDiskRequiredForRestore**

## 错误码

##### ASRBR-INSTANCE-SingleDiskRequiredForRestore

**错误信息**

云盘恢复仅支持单盘。

**原因分析**

创建ECS云盘恢复任务时，云盘级恢复仅支持单块云盘。当一次请求中指定了多块云盘时，记录本错误码。

**置信等级**

A

**解决方案**

1. 每个云盘恢复任务仅指定一块云盘。
2. 如需恢复多块云盘，分别创建多个单盘恢复任务。

##### ASRBR-INSTANCE-

**OtsTableBackupJobNotExecuted**

## 错误码

##### ASRBR-INSTANCE-OtsTableBackupJobNotExecuted

**错误信息**

OTS实例备份任务已结束，但其中某张表的备份任务始终未被执行。

**原因分析**

该错误发生在 OTS（表格存储）实例级备份场景下。 OTS实例备份会为实例内的每张表创建表级备份子任务。正常情况下，每张表的备份子任务都应在实例级备份结束前被调度执行。当实例级备份任务已经到达最终状态，而某张表的备份子任务却始终没有被执行时， 管控会把该表的备份子任务判定为失败并写入本错误码，同时将实例级备份结果由成功降级为部分成功。 这类情况通常意味着该表的备份子任务在调度或下发环节未能正常触发。例如子任务未成功创建、未被正确关联到本次实例备份或调度过程中出现异常。

**置信等级**

B 灾备管理中心

**解决方案**

1. 在该OTS实例的备份记录中定位始终未执行的表，查看对应表级备份记录的状态与traceId。
2. 结合traceId排查该表备份子任务为何未被下发或执行，确认该表是否在本次备份范围内、子任务是否正
常创建与关联。
3. 问题处理完成后，等待下一次备份周期自动重试或在ASRBR控制台重新触发该OTS实例的备份，确认该
表能够被正常备份。

##### ASRBR-INSTANCE-

**OtsAllTableBackupFailed**

## 错误码

**错误信息**

OTS实例备份下所有表级备份任务均失败，请查看各表的备份记录了解详情。

**原因分析**

该错误发生在 OTS（表格存储）实例级备份场景下。 OTS实例备份会为实例内的每张表分别创建一个表级备份子任务，实例级备份的最终结果由这些表级子任务聚合得出。当实例内所有表级备份子任务都已结束、且无一成功（全部失败）时，管控将该实例级备份记录判定为失败，并写入本错误码。 本错误是实例级的汇总结论，真正的失败原因在各张表的表级备份记录中。所有表都失败通常意味着存在影响整个实例的共性问题，例如实例整体不可访问、账号或权限异常、网络不通，导致每张表的备份都无法完成。

**置信等级**

B

**解决方案**

1. 查看该OTS实例下各表级备份记录的错误码与错误信息，确认各表失败是否指向同一类共性原因。
2. 针对共性原因排查：确认OTS实例本身是否正常可访问、备份所用账号与角色是否具备访问该实例及其表
的权限、网络链路是否正常。
3. 共性问题处理完成后，等待下一次备份周期自动重试或在ASRBR控制台重新触发该OTS实例的备份。

#### STORAGE

##### ASRBR-STORAGE-

**StoragePoolExceedsGroupCapacity**

## 错误码

##### ASRBR-STORAGE-StoragePoolExceedsGroupCapacity

**错误信息**

存储池容量超过所属存储池组的可用容量上限。 灾备管理中心

**原因分析**

存储池隶属于存储池组，组内所有存储池的容量之和不能超过组的容量上限。本次配置的存储池容量将导致组总容量超限。

**置信等级**

A

**解决方案**

1. 调小存储池容量：将存储池容量调整为不超过存储池组的剩余可用容量。
2. 扩大组容量：若业务确需更大容量，先扩大存储池组的总容量上限。
3. 重新提交：调整完成后重新提交配置。

##### ASRBR-STORAGE-UrlResolutionFailed

## 错误码

**错误信息**

无法解析提供的URL，请检查地址格式。

**原因分析**

创建或修改存储池组时，用户提供的Endpoint既非合法IP格式也无法作为URL正常解析。可能原因包括：
1. URL格式错误，如包含非法字符、缺少协议前缀、路径结构异常等。
2. 域名不存在或DNS服务器无法解析该主机名。
3. 网络环境问题导致DNS查询超时或失败。

**置信等级**

A

**解决方案**

1. 检查格式：确认Endpoint地址格式正确，支持纯IP地址或http(s):// 开头的URL。
2. 验证域名：如使用域名，确认该域名已在DNS中正确注册且可解析。
3. 检查网络：确认ASR-BR服务所在节点能够正常访问DNS服务器进行域名解析。
4. 重试操作：如为临时性DNS故障，等待网络恢复后重新提交

##### ASRBR-STORAGE-

**UrlIpAddressInRestrictedRange**

## 错误码

##### ASRBR-STORAGE-UrlIpAddressInRestrictedRange

**错误信息**

URL解析后的IP地址属于受限内网网段，禁止访问。

**原因分析**

灾备管理中心创建或修改存储池组时，用户提供的Endpoint为URL/域名格式，系统对用户提供的URL进行DNS解析以获取真实IP地址（防止进制绕过等攻击方式），然后校验该IP是否在内网管理网段黑名单中。当解析后的IP命中受限网段时，出于SSRF安全策略拦截本次请求。

**置信等级**

A

**解决方案**

（1）检查域名解析：使用nslookup或dig命令确认该URL/域名解析到的真实IP地址。 （2）更换Endpoint：将Endpoint更换为DNS解析后不在受限内网网段范围内的合法地址。 （3）排查DNS劫持：如果域名解析到非预期的内网IP，请检查DNS配置是否存在异常或被劫持。 （4）联系管理员：如确认为误拦截，请联系安全工程师核查Skyline黑名单配置或添加白名单。

##### ASRBR-STORAGE-

**IpAddressInRestrictedRange**

## 错误码

**错误信息**

提供的IP地址属于受限内网网段，禁止访问。

**原因分析**

创建或修改存储池组时，用户提供的Endpoint为直接IP地址格式且该IP落在Skyline内网黑名单CIDR范围内。系统通过Skyline动态获取内网管理网段黑名单（包括serverIB、opsvm、privatevip_cloudmgmt、 privatevip_cloudops、rama_network等网段），对用户提供的Endpoint IP进行SSRF安全检查。当IP地址命中上述受限网段时，出于安全策略拦截本次请求。

**置信等级**

A

**解决方案**

1. 检查Endpoint：确认填写的IP地址是否正确，避免使用内网管理网段的IP。
2. 更换地址：将该Endpoint更换为不在受限内网网段范围内的合法地址。
3. 联系管理员：如确认为误拦截，请联系安全工程师核查Skyline黑名单配置或添加白名单。

##### ASRBR-STORAGE-

**StoragePoolAccessDenied**

## 错误码

**错误信息**

存储池操作失败，提供的AccessKey无权限访问目标存储。 灾备管理中心

**原因分析**

系统在创建或修改存储池时尝试访问底层OSS存储（canCreateBucket），目标存储返回 ACCESS_DENIED。可能原因包括：
1. AK/SK错误或已失效。
2. AK/SK未被授予目标Bucket的读写权限。
3. Bucket存在访问策略限制。

**置信等级**

A

**解决方案**

1. 核对凭据：确认AccessKey/SecretKey正确且未过期。
2. 授予权限：为该AK/SK授予对目标Bucket的完全读写权限。
3. 重新提交：权限配置正确后重新提交操作。

##### ASRBR-STORAGE-

**TrashBucketCreationForbidden**

## 错误码

**错误信息**

无法自动创建回收站Bucket，当前凭据权限不足。

**原因分析**

创建备份仓库时系统会尝试自动创建回收站存储桶（trash bucket）。如果当前凭据仅具备读写权限，不具备创建Bucket的权限，且用户未填写trash bucket，或者填写了一个不存在的Bucket名称，就会导致自动创建失败并被系统拒绝。

**置信等级**

A

**解决方案**

根据实际情况选择以下任一方案：
1. 提升权限：修改存储池的AK、SK，使用权限更完整（包括创建Bucket权限）的凭据。
2. 指定已有Bucket：在trash bucket中填写一个已存在的Bucket名称。

##### ASRBR-STORAGE-

**OrganizationIdCountExceeded**

## 错误码

**错误信息**

灾备管理中心组织ID数量超过限制。

**原因分析**

创建或修改存储池时提供的组织ID列表长度超过了系统允许的最大值（字符串长度5000），请求失败。

**置信等级**

A

**解决方案**

1. 精简请求中的组织ID列表，使其不超过系统限制。
2. 若确需关联多个组织，可分批调用接口逐步添加。

##### ASRBR-STORAGE-TrashBucketRequired

## 错误码

**错误信息**

当前系统配置下，必须配置回收站Bucket。

**原因分析**

系统在创建或修改存储池时，校验到当前环境要求必须配置trashBucket。 触发条件为：在运维管理 > 参数配置中，HBR-Backend过期碎片清理的过期数据碎片回收方式或 HBR- Storage过期碎片清理的过期数据碎片回收方式，至少有一项被设置为回收至Trash Bucket。此时在配置存储池时必须指定trash bucket，否则操作会被拒绝。

**置信等级**

A

**解决方案**

以下两种方案任选其一即可：
1. 调整回收方式：在运维管理 > 参数配置中，将HBR-Backend过期碎片清理的过期数据碎片回收方式与
HBR-Storage过期碎片清理的过期数据碎片回收方式，均设置为非回收至Trash Bucket的选项。
2. 配置Trash Bucket：为当前存储池指定一个可用的trash bucket后重新提交操作。

##### ASRBR-STORAGE-

**StorageAccessTripleAlreadyExists**

## 错误码

##### ASRBR-STORAGE-StorageAccessTripleAlreadyExists

**错误信息**

存储池访问信息（AK/SK/Endpoint 组合）已被其他存储池占用。

**原因分析**

灾备管理中心创建存储池时，系统通过唯一性校验（checkUniqueness）发现当前 AccessKey + SecretKey + Endpoint三元组已被另一个存储池使用。同一三元组不允许重复注册。

**置信等级**

A

**解决方案**

1. 检查已有存储池：确认是否已存在使用相同AK/SK/Endpoint的存储池，避免重复创建。
2. 更换凭据：若确需新建，请使用不同的AccessKey或Endpoint进行注册。

##### ASRBR-STORAGE-

**IpAddressConflictWithOtherGroup**

## 错误码

##### ASRBR-STORAGE-IpAddressConflictWithOtherGroup

**错误信息**

存储池IP地址与其它存储池组冲突。

**原因分析**

为避免多个存储池组共用同一存储节点造成数据写入冲突，系统在创建或修改存储池组时要求其Endpoint 解析出的IP地址不得与已有存储池组的IP重叠。当前提交的IP已被其他存储池组使用，因此被拦截。

**置信等级**

A

**解决方案**

1. 核对当前存储池组的Endpoint 配置，确认其解析到的IP是否预期所属。
2. 调整Endpoint或IP，使其与现有存储池组的IP列表不重叠后重新提交。

##### ASRBR-STORAGE-

**StoragePoolDeleteFailed**

## 错误码

**错误信息**

删除存储池失败。

**原因分析**

ASRBR管控在删除存储池前会校验该存储池是否仍被其他资源占用。当存在以下任一依赖关系时，为避免数据不一致，拒绝删除并记录本错误码：
1. 该存储池下仍存在未删除的备份仓库。
2. 该存储池仍被元数据自备份策略引用。
3. 该存储池仍存在未过期的元数据自备份记录。
灾备管理中心

**置信等级**

B

**解决方案**

1. 通过操作日志的traceId查询系统日志，确认拦截删除的具体依赖类型（备份仓库、自备份策略或未过期
的自备份记录）与对应的资源标识。
2. 若为备份仓库占用：前往备份仓库管理页面，删除该存储池下关联的备份仓库。
3. 若为元数据自备份策略占用：解除或删除引用该存储池的自备份策略。
4. 若为未过期的自备份记录占用：等待相关自备份记录过期或按策略清理后再重试。
5. 确认存储池已无任何依赖后，重新发起删除操作。

##### ASRBR-STORAGE-

**StoragePoolGroupUpdateFailed**

## 错误码

**错误信息**

修改存储池组失败。

**原因分析**

ASRBR管控在修改存储池组时，若本次修改涉及变更接入地址（Endpoint），会校验该存储池组下是否仍包含存储池。 由于Endpoint是组内所有存储池的接入基础，变更后会破坏既有存储池的一致性，因此当存储池组下仍存在存储池时，拒绝修改Endpoint并记录本错误码。修改名称、存储空间、带宽、存储介质等其他属性不受此限制。

**置信等级**

B

**解决方案**

1. 通过操作日志的traceId查询系统日志，确认本次修改是否变更了存储池组的Endpoint，以及该存储池组
下仍存在的存储池情况。
2. 若确需变更Endpoint：先将该存储池组下的存储池清空或迁移，确认组内已无存储池后再修改
Endpoint。
3. 若无需变更Endpoint：保持Endpoint不变，仅修改名称、存储空间、带宽、存储介质等属性后重新提
交。

##### ASRBR-STORAGE-

**StoragePoolCannotUnauthorize**

## 错误码

**错误信息**

灾备管理中心无法取消存储池对组织的授权。

**原因分析**

ASRBR管控在修改存储池的授权组织范围时，若本次修改收窄了授权范围（将某组织从授权列表移除，或从全部组织改为部分组织导致某些组织不再被授权），会校验被取消授权的组织下是否仍存在备份仓库。 当被取消授权的组织下仍有备份仓库时，为避免仓库失去存储池授权，拒绝取消授权并记录本错误码。

**置信等级**

A

**解决方案**

1. 通过操作日志的traceId查询系统日志，确认阻止取消授权的组织与其下的备份仓库信息。
2. 迁移或删除该组织下关联到本存储池的备份仓库。
3. 或在授权列表中保留该组织的授权，不将其移除。
4. 处理后重新提交存储池授权修改。

##### ASRBR-STORAGE-

**StoragePoolGroupNotEmpty**

## 错误码

**错误信息**

存储池组下仍存在存储池，无法删除。

**原因分析**

删除存储池组前，系统会校验该组下是否仍包含存储池。当组内仍存在存储池时，拒绝删除并记录本错误码。

**置信等级**

B

**解决方案**

1. 前往存储池组管理页面，确认该存储池组下仍存在的存储池。
2. 先将存储池组内的存储池移除。
3. 确认存储池组内已无存储池后，重新发起删除操作。

##### ASRBR-STORAGE-

**SourcePoolGroupReplicationUnsupported**

## 错误码

##### ASRBR-STORAGE-SourcePoolGroupReplicationUnsupported

**错误信息**

灾备管理中心源端存储池组不支持创建镜像仓库。

**原因分析**

为某个备份仓库配置镜像仓库时，系统会先查询该源端仓库所在存储池组是否具备跨域/云复制能力。 当该存储池组存在，但未完成复制授权（即数据库中缺少复制云ID、复制OSS Region、复制OSS Location三要素之一）时，判定源端存储池组不支持创建镜像仓库，记录本错误码。常见根因：
1. 源端仓库所在的存储池组从未执行过跨域/云复制授权，数据库中复制三要素为空。
2. 该存储池组的复制授权信息被清空或未配置完整。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位源端存储池组名称/ID，以及缺失的复制配置项（复制云ID、复制OSS
Region、复制OSS Location）。
2. 使用root组织前往存储池组管理页面，对源端仓库所在的存储池组执行跨域/云复制授权。
3. 授权配置完成后，重新发起镜像仓库创建请求。

#### COMMON

##### ASRBR-COMMON-

**PermissionUserRoleUnauthorized**

## 错误码

##### ASRBR-COMMON-PermissionUserRoleUnauthorized

**错误信息**

用户角色未授权。

**原因分析**

1. 当前用户未被授予执行该操作所需的角色。
2. 当前用户尝试访问不属于其管辖范围的组织或资源。
3. 当前用户角色对该API不在允许的白名单内。
4. RAM鉴权或STS Token校验异常。

**置信等级**

B

**解决方案**

1. 为当前用户授予执行该操作所需的角色权限。
2. 确认当前账号操作的是自己管辖范围内的组织或资源。
3. 使用具备相应权限的角色账号重新登录后再执行操作。
4. 若鉴权链路异常，刷新登录态后重试。
灾备管理中心

##### ASRBR-COMMON-EndpointUnreachable

## 错误码

**错误信息**

目标对象的Endpoint不可达。

**原因分析**

ASRBR系统需要通过Endpoint访问目标对象（如对象存储Bucket、产品实例、对端服务）。 Endpoint不可达常见原因包括：
1. Endpoint地址或域名填写错误，DNS解析失败。
2. 网络中断、防火墙或安全组规则阻断了管控到目标对象的访问链路。
3. 目标对象处于异常状态（如Bucket不存在、对端服务不可用）或鉴权信息失效。

**置信等级**

B

**解决方案**

1. 核对Endpoint地址，确认目标对象存在且地址正确。
2. 检查网络连通性与DNS解析，确认防火墙或安全组放行管控到Endpoint的访问。
3. 确认目标对象服务运行正常、鉴权信息有效后重新执行操作。

#### GENERIC

##### ASRBR-GENERIC-MissingParam

## 错误码

**错误信息**

请求或调用缺少必填参数。错误消息会携带缺失的参数列表。

**原因分析**

1. 控制台/OpenAPI调用报错：用户在控制台或通过OpenAPI发起请求（如创建备份计划、修改策略、执行
恢复）时，请求体未提供必填字段。
2. 系统任务报错：备份或恢复事件的内部流转过程中存在传参异常，某个必填字段为空导致后续流程无法继
续。

**置信等级**

B

**解决方案**

灾备管理中心
1. 若为控制台/OpenAPI调用：查看错误消息中列出的参数名，检查请求体是否遗漏对应参数，补齐后重新
发起请求。
2. 若为系统任务：通过备份/恢复事件的traceId检索日志，结合errorCode和errorMessage定位参数缺失
的调用链。

##### ASRBR-GENERIC-InvalidParam

## 错误码

**错误信息**

请求或调用参数不合法。错误消息会携带不合法的参数列表。

**原因分析**

ASRBR管控在参数校验阶段发现字段值不符合规则，例如格式错误、越界、枚举值不匹配等。触发场景分两类：
1. 控制台/OpenAPI调用报错：用户输入的参数不符合业务规则，如备份周期超出允许范围、保留天数为负
数、实例ID格式错误等。
2. 系统任务报错：内部流程中传入的字段值不合法，导致后续处理无法继续执行。

**置信等级**

B

**解决方案**

1. 若为控制台/OpenAPI调用：根据错误消息中提示的参数名，参照接口文档校准取值范围与格式后重新提
交。
2. 若为系统任务：通过traceId查询日志，结合errorCode和errorMessage定位具体不合法的字段及其来
源调用链。

##### ASRBR-GENERIC-NotFoundResource

## 错误码

**错误信息**

请求的资源不存在。错误消息中会返回未找到的资源标识，例如资源类型、ID或名称。

**原因分析**

ASRBR管控按照传入的ID或名称查询资源（备份计划、备份仓库、实例、备份集、恢复计划等）时未找到匹配记录。触发场景分两类：
1. 控制台/OpenAPI调用报错：用户传入的资源ID拼写错误、资源已被删除等。
2. 系统任务报错：后台任务查询依赖的资源时，资源被并发删除或未初始化。

**置信等级**

B

**解决方案**

灾备管理中心
1. 若为控制台/OpenAPI调用：核对错误消息中提示的资源标识，前往对应管理页面确认资源是否存在、是
否已被删除。
2. 若为系统任务：通过traceId检索日志，进一步通过errorCode、errorMessage定位缺失的具体资源及
所在业务流程。

##### ASRBR-GENERIC-InvalidStateForOperation

## 错误码

**错误信息**

资源当前状态不支持该操作。错误消息中会返回处于冲突状态的资源标识。

**原因分析**

ASRBR管控在执行操作前会做状态机校验，发现资源当前状态与目标操作不兼容。常见于：
1. 控制台/OpenAPI发起不符合当前状态的操作：例如对已过期的备份集发起恢复、对已停用的备份策略进
行修改等。
2. 系统任务报错：后台流程执行时资源状态发生变化，导致后续动作被拒绝。

**置信等级**

B

**解决方案**

1. 若为控制台/OpenAPI调用：查看错误消息中提示的资源标识，前往对应管理页面确认当前状态，等待资
源转入允许该操作的状态后再重试。
2. 若为系统任务：通过traceId查询日志，结合errorCode和errorMessage定位状态冲突发生的具体环
节。

##### ASRBR-GENERIC-ResourceAlreadyExists

## 错误码

**错误信息**

创建的资源已存在，存在名称或唯一键冲突。错误消息中会返回发生冲突的资源标识。

**原因分析**

ASRBR管控在创建资源（备份计划、备份仓库、恢复计划、存储池等）时，检测到该资源名称或唯一标识已被占用。通常分为两类场景：
1. 控制台/OpenAPI调用报错：用户重复提交表单，或创建时使用了与已有资源相同的名称。
2. 系统任务报错：后台任务重复触发创建流程，导致资源重复创建。

**置信等级**

B

**解决方案**

1. 若为控制台/OpenAPI调用：根据错误消息中返回的资源名称，前往对应管理页面确认是否已存在同名资
源；如有必要，调整命名后重新提交或直接复用现有资源。 灾备管理中心
2. 若为系统任务：通过traceId检索日志，结合errorCode和errorMessage确认是否为重复触发或幂等控
制问题。

##### ASRBR-GENERIC-PermissionDenied

## 错误码

**错误信息**

当前用户或角色没有权限执行该操作。错误消息会携带被拒绝的主体标识。

**原因分析**

1. 控制台/OpenAPI调用报错：用户使用的账号未被授权对应功能或授权范围不覆盖该资源（如跨组织操
作、只读账号发起写操作）。
2. 系统任务报错：后台服务使用的AK/角色没有下游产品的调用权限。

**置信等级**

B

**解决方案**

1. 若为控制台/OpenAPI调用：向管理员申请对应权限或授权范围，确认所用账号具备目标操作的权限后重
试。
2. 若为系统任务：通过traceId查询日志，进一步通过errorCode、errorMessage定位被拒绝鉴权的具体
接口与主体，检查后台账号/角色配置。

##### ASRBR-GENERIC-OperationNotSupported

## 错误码

**错误信息**

目标资源不支持当前操作。错误消息会携带不支持该操作的资源标识。

**原因分析**

ASRBR管控发现目标资源的类型、规格、版本或部署形态与请求的操作不兼容。常见于：
1. 控制台/OpenAPI调用报错：对不支持该能力的资源发起操作。
2. 系统任务报错：后台流程执行时发现资源不满足后续步骤所需能力。

**置信等级**

B

**解决方案**

1. 若为控制台/OpenAPI调用：查看错误消息中携带的资源标识，参照产品能力边界文档确认是否支持该操
作，改用受支持的操作方式或更换资源。
2. 若为系统任务：通过traceId查询日志，进一步通过errorCode、errorMessage分析被拒绝的具体动作
与资源能力差异。 灾备管理中心

##### ASRBR-GENERIC-SystemError

## 错误码

**错误信息**

系统发生未预期错误。

**原因分析**

SystemError是所有未预期错误的统称。当代码中未匹配到任何具体业务错误码或捕获到未分类的异常时， 此错误码不表示具体业务原因，必须结合日志分析。常见来源包括：依赖服务不可用、数据库访问失败、序列化异常、空指针等运行时异常。

**置信等级**

B

**解决方案**

1. 通过备份记录/事件/请求的traceId检索管控日志，定位抛出SystemError时的完整调用栈。
2. 根据日志中的异常类名、message与堆栈判断真实根因（如SQLException、TimeoutException、
NPE等），针对具体原因处理。
3. 若为偶发问题，可先重试。若持续复现，请将traceId与日志片段提供给运维/研发进一步排查。

#### API

##### ASRBR-API-ApiTaskQueryTimeout

## 错误码

**错误信息**

下游API异步任务轮询超时。

**原因分析**

ASRBR管控在调用HBR服务执行VMware/vCenter资源探索等异步任务后，会循环轮询任务状态 （progress）。当轮询次数达到上限后任务仍未完成（progress未到 100），记录本错误码。常见于HBR 侧任务执行耗时过长、任务卡住、或网络抖动导致轮询请求超时。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，确认轮询的任务ID与最后一次获取到的progress值。
2. 前往HBR服务侧确认该任务的实际执行状态，是否处于卡住或排队中。
3. 若为临时性网络抖动，等待后重新触发操作即可。若任务持续未完成，联系HBR产品负责人协助排查。
灾备管理中心

##### ASRBR-API-CallAdbApiFailed

## 错误码

**错误信息**

调用ADB接口失败。

**原因分析**

ASRBR管控在执行ADB（分析型数据库）相关操作时，调用ADB产品侧OpenAPI失败。 涉及的业务动作包括：查询ADB集群列表与属性、修改备份策略（全量/日志）、创建恢复实例、查询备份记录、查询物理实例信息等。 当ADB接口返回服务端错误、鉴权失败、网络异常或SDK客户端异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的ADB接口名称与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如权限不足、参数错误、实例不存在、ADB服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系ADB产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallOssApiFailed

## 错误码

**错误信息**

调用OSS接口失败。

**原因分析**

涉及的业务动作包括：存储桶的创建/删除/容量设置/ACL 查询、对象上传/下载/删除/存在检查、桶策略/生命周期/合规保留/跨区域复制规则管理等。 当OSS返回服务端异常（ServiceException）、客户端异常（ClientException）或STS临时凭证获取失败时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的OSS操作与返回的errorCode、errorMessage。
2. 常见原因包括：Bucket不存在或已删除、AccessKey/STS凭证无效或权限不足、网络连通性异常、
Bucket容量达到上限。
3. 若无法明确原因，提取请求参数与响应内容，联系OSS产品负责人或存储管理员协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallEcsApiFailed

## 错误码

**错误信息**

调用ECS接口失败。

**原因分析**

ASRBR管控在执行ECS（云服务器）相关操作时，调用ECS产品侧OpenAPI失败。 涉及的业务动作包括：实例查询/创建/启动、磁盘查询/删除、快照创建/查询/删除、安全组管理、规格与可用区查询、云助手命令执行与查询等。 当ECS接口返回服务端错误、鉴权失败、网络异常或SDK客户端异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的ECS接口名称与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如快照配额不足、磁盘状态异常、实例不存在、权限不足等）。
3. 若无法明确原因，提取请求参数与响应内容，联系ECS产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallRdsApiFailed

## 错误码

**错误信息**

调用RDS接口失败。

**原因分析**

ASRBR管控在执行RDS（关系型数据库）相关操作时，调用RDS产品侧OpenAPI失败。 涉及的业务动作包括：查询实例信息/备份策略/备份记录、创建备份、修改备份策略、白名单管理、参数与 SSL/TDE查询、克隆恢复/跨地域恢复/Binlog文件查询等。 当RDS接口返回服务端错误、鉴权失败、实例属性查询为空或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的RDS接口名称与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、权限不足、策略参数超限、RDS服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系RDS产品负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallNasApiFailed

## 错误码

**错误信息**

调用NAS接口失败。

**原因分析**

ASRBR管控在执行文件备份相关操作时，调用NAS（文件存储）产品侧OpenAPI失败。 涉及的业务动作包括：查询NAS文件系统列表、创建NAS文件系统。 当NAS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的NAS接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如权限不足、文件系统配额超限、NAS服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系NAS产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallVpcApiFailed

## 错误码

**错误信息**

调用VPC接口失败。

**原因分析**

ASRBR管控在执行网络相关操作时，调用VPC（专有网络）产品侧OpenAPI失败。 涉及的业务动作包括：查询VPC/VSwitch列表、检查私网IP可分配性、创建VPC/VSwitch、查询动态VIP 等。 当VPC接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的VPC接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如VPC/VSwitch不存在、可用IP不足、权限不足等）。
3. 若无法明确原因，提取请求参数与响应内容，联系VPC/网络产品负责人协助排查。
4. 问题解决后，重新触发相关操作。
灾备管理中心

##### ASRBR-API-CallPolardbApiFailed

## 错误码

**错误信息**

调用PolarDB接口失败。

**原因分析**

ASRBR管控在执行PolarDB相关操作时，调用PolarDB产品侧OpenAPI失败。 涉及的业务动作包括：查询集群列表/属性/备份日志、创建备份、修改备份策略、白名单管理、查询备份任务/备份记录、SSL/TDE查询、恢复/创建集群等。 当PolarDB接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的PolarDB接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如集群不存在、权限不足、策略参数错误、PolarDB服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系PolarDB产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallPolardbxApiFailed

## 错误码

**错误信息**

调用PolarDB-X接口失败。

**原因分析**

ASRBR管控在执行PolarDB-X相关操作时，调用PolarDB-X产品侧OpenAPI失败。 涉及的业务动作包括：查询实例列表/属性/拓扑/HA信息、查询区域与规格、修改实例描述、恢复实例/创建容灾恢复实例、查询资源组等。 当PolarDB-X接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的PolarDB-X接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、拓扑信息异常、权限不足等）。
3. 若无法明确原因，提取请求参数与响应内容，联系PolarDB-X产品负责人协助排查。
4. 问题解决后，重新触发相关操作。
灾备管理中心

##### ASRBR-API-CallPolardbLocalApiFailed

## 错误码

**错误信息**

调用PolarDB Local接口失败。

**原因分析**

ASRBR管控在执行PolarDB Local（本地盘版）相关操作时，调用PolarDB Local产品侧OpenAPI失败。 涉及的业务动作包括：查询实例信息、创建备份、修改备份策略、查询备份策略与记录、白名单管理、参数/SSL/TDE/网络信息查询、克隆恢复/异地恢复、Binlog文件查询等。 当接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、权限不足、参数错误等）。
3. 若无法明确原因，提取请求参数与响应内容，联系PolarDB Local产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallMongodbApiFailed

## 错误码

**错误信息**

调用MongoDB接口失败。

**原因分析**

ASRBR管控在执行MongoDB相关操作时，调用MongoDB产品侧OpenAPI失败。 涉及的业务动作包括：查询实例信息/备份策略/备份记录、创建备份、修改备份策略、SSL查询/白名单管理、修改实例描述、恢复（克隆/异地恢复/分片克隆/分片异地恢复）等。 当MongoDB接口返回服务端错误、实例属性查询为空、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的MongoDB接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在或已释放、权限不足、MongoDB服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系MongoDB产品负责人协助排查。
4. 问题解决后，重新触发相关操作。
灾备管理中心

##### ASRBR-API-CallRedisApiFailed

## 错误码

**错误信息**

调用Redis接口失败。

**原因分析**

ASRBR管控在执行Redis相关操作时，调用Redis产品侧OpenAPI失败。 涉及的业务动作包括：查询实例信息/备份策略/备份记录、创建备份、修改备份策略、实例属性与SSL查询、白名单管理、创建实例/容灾恢复、修改实例属性、查询区域与规格等。 当Redis接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的Redis接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、权限不足、Redis服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系Redis产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallDrdsApiFailed

## 错误码

**错误信息**

调用DRDS接口失败。

**原因分析**

ASRBR管控在执行DRDS（分布式关系型数据库）相关操作时，调用DRDS产品侧OpenAPI失败。 涉及的业务动作包括：查询实例详情、修改备份策略（云内/跨域）、查询备份策略/本地备份集/跨域备份集、创建容灾恢复实例、启动即时备份、查询实例下DB列表与RDS子实例列表、查询任务状态、恢复预检查、修改实例描述等。 当DRDS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的DRDS接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、策略参数错误、权限不足、DRDS服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系DRDS产品负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallGpdbApiFailed

## 错误码

**错误信息**

调用GPDB接口失败。

**原因分析**

ASRBR管控在执行GPDB（AnalyticDB PostgreSQL）相关操作时，调用GPDB产品侧OpenAPI失败。涉及的业务动作包括：创建/查询/删除/重启实例、查询/修改备份策略、查询数据与日志备份列表、创建临时备份、IP白名单管理、网络/SSL/参数查询、创建账号/重置密码、恢复实例等。 当GPDB接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的GPDB接口与返回的errorCode、errorMessage。
2. 根据错误信息初步判断原因（如实例不存在、权限不足、GPDB服务不可用等）。
3. 若无法明确原因，提取请求参数与响应内容，联系GPDB产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallOdpsApiFailed

## 错误码

**错误信息**

调用MaxCompute/ODPS接口失败。

**原因分析**

ASRBR管控在执行大数据备份相关操作时，调用MaxCompute/ODPS/MMA接口失败。 涉及的业务动作包括：创建ODPS备份计划与恢复任务、查询任务详情/列表、获取ABM Token与存储信息、MMA数据源查询与进度检查、MaxCompute外部表创建检查等。 当接口响应code非 200、JSON解析失败（返回 null）、MMA Token过期（返回408）或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的接口与返回的errorCode、errorMessage。
2. 常见原因：MMA Token过期需刷新、ABM服务不可用、ODPS项目配置异常、网络连通性问题。
3. 若无法明确原因，提取请求参数与响应内容，联系MaxCompute/MMA产品负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallOtsApiFailed

## 错误码

**错误信息**

调用OTS接口失败。

**原因分析**

ASRBR管控在执行OTS（表格存储）相关操作时，调用OTS SDK（SyncClient）失败。 涉及的业务动作为查询OTS实例下的表列表，用于备份计划创建时验证实例信息。 当OTS SDK抛出TableStoreException（如实例不存在、权限不足、网络错误）时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位OTS调用返回的errorCode、errorMessage。
2. 常见原因：OTS实例名称错误或不存在、访问凭证权限不足、OTS服务Endpoint不可达。
3. 若无法明确原因，提取请求参数与响应内容，联系OTS产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallEsApiFailed

## 错误码

**错误信息**

调用Elasticsearch接口失败。

**原因分析**

ASRBR管控在执行Elasticsearch备份/恢复相关操作时，调用ES产品侧接口失败。 涉及的业务动作包括：查询ES实例详情、查询索引列表与恢复状态、创建/删除快照仓库、触发备份与恢复等。 当ES OpenAPI调用抛出异常、ES REST响应包含Unauthorized（用户名密码不匹配）或响应JSON中包含 error字段时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的ES接口与返回的错误内容。
2. 常见原因：ES实例用户名/密码错误（Unauthorized）、快照仓库不存在或配置异常、ES实例状态不正
常、网络异常。 灾备管理中心
3. 若无法明确原因，提取请求参数与响应内容，联系ES产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallAscmApiFailed

## 错误码

**错误信息**

调用ASCM接口失败。

**原因分析**

ASRBR管控在执行账号、权限或组织管理相关操作时，调用ASCM（飞天管控平台）ASAPI接口失败。涉及的业务动作包括：查询Region/Cloud列表、获取组织树/组织信息、获取账户列表/用户信息、通过Ticket登录、判断管理员权限、查询角色列表、获取STS用户画像等。 当ASCM接口返回错误或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的ASCM接口与返回的errorCode、errorMessage。
2. 常见原因：ASCM服务不可用、Ticket已过期或无效、账号权限不足、网络连通性问题。
3. 若无法明确原因，提取请求参数与响应内容，联系ASCM/飞天平台负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallS3ApiFailed

## 错误码

**错误信息**

调用S3兼容存储接口失败。

**原因分析**

涉及的业务动作包括：列出/创建/删除Bucket、检查Bucket是否存在、获取Bucket ACL、上传/下载/删除/ 列出对象、获取对象元信息等。 当S3 SDK抛出S3Exception（服务端错误，如权限拒绝、Bucket不存在）或通用客户端异常（网络错误） 时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的S3操作与返回的errorCode、errorMessage。
2. 常见原因：S3凭证无效或权限不足、Bucket名称不存在、网络连通性异常、S3兼容存储服务不可用。
灾备管理中心
3. 若无法明确原因，提取请求参数与响应内容，联系存储管理员协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallKmsApiFailed

## 错误码

**错误信息**

调用KMS接口失败。

**原因分析**

ASRBR管控在执行加密相关操作时，调用KMS（密钥管理服务）OpenAPI失败。 涉及的业务动作包括：查询密钥列表、查询别名列表、查询密钥详情（用于备份加密功能的密钥选择与有效性验证）。 当KMS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的KMS接口与返回的errorCode、errorMessage。
2. 常见原因：密钥不存在或已禁用、KMS服务不可用、访问凭证权限不足。
3. 若无法明确原因，提取请求参数与响应内容，联系KMS产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallBackendStorageApiFailed

## 错误码

**错误信息**

调用后端存储服务接口失败。

**原因分析**

后端存储层封装了OSS和S3两种实现，涉及的业务动作包括：存储桶的创建/删除/ACL查询/容量管理、对象上传/下载/删除/列出、桶策略/统计信息管理，以及存储池连通性校验与备份仓库初始化。 当底层OSS或S3调用失败后，异常被统一封装为本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的存储操作与底层返回的errorCode、errorMessage。
2. 常见原因：存储凭证无效或权限不足、Bucket不存在、网络连通性异常、存储服务不可用。
灾备管理中心
3. 若无法明确原因，提取请求参数与响应内容，联系存储管理员协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallTianjiApiFailed

## 错误码

**错误信息**

调用天基接口失败。

**原因分析**

涉及的业务动作包括：获取服务注册变量（如cluLocation）、获取指定集群下机器列表、获取ASRBR项目集群列表、获取OSS集群信息（判断是否为CDS集群）等。 当TianJi HTTP接口响应状态码非200、请求超时或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的TianJi接口URL与返回内容。
2. 常见原因：TianJi服务不可用、集群名称不匹配、网络连通性问题。
3. 若无法明确原因，提取请求参数与响应内容，联系TianJi平台负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallOmsApiFailed

## 错误码

**错误信息**

调用OMS接口失败。

**原因分析**

ASRBR 管控在执行计量数据上报时，调用OMS（运维管理服务）OpenAPI失败。涉及的业务动作包括：推送计量数据就绪标记（标记某周期数据是否推送完毕）、推送计量数据（按代理方式上报产品计量数据）。 当OMS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的OMS接口与返回的errorCode、errorMessage。
2. 常见原因：OMS服务不可用、计量数据格式异常、鉴权失败。
3. 若无法明确原因，提取请求参数与响应内容，联系OMS产品负责人协助排查。
灾备管理中心
4. 问题解决后，等待下一次计量上报周期自动重试。

##### ASRBR-API-CallTianjiMonApiFailed

## 错误码

**错误信息**

调用TianJi监控接口失败。

**原因分析**

ASRBR管控在查询物理机流量监控数据时，调用TianJi监控（TianjiMon/CMS）的QueryMetricList接口失败。该接口用于获取备份服务器的网络流量等监控指标。 当CMS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位QueryMetricList调用返回的errorCode、errorMessage。
2. 常见原因：CMS服务不可用、监控指标名称配置错误、鉴权失败。
3. 若无法明确原因，提取请求参数与响应内容，联系TianJi监控/CMS负责人协助排查。
4. 问题解决后，等待下一次监控采集周期自动重试。

##### ASRBR-API-CallHbrApiFailed

## 错误码

**错误信息**

调用HBR接口失败。

**原因分析**

ASRBR管控在执行备份任务管理或Agent配置时，调用HBR（混合云备份）产品侧接口失败。 涉及的业务动作为：创建ECS文件备份计划后，调用HBR的UpdateClientSettings接口更新Agent的并发数和CPU核心数配置。 当HBR接口返回success=false时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位调用HBR UpdateClientSettings时的请求参数与返回内容。
2. 常见原因：HBR Agent不在线或版本不兼容、Client ID不存在、HBR服务不可用。
3. 若无法明确原因，提取请求参数与响应内容，联系HBR产品负责人协助排查。
4. 问题解决后，重新触发相关操作。
灾备管理中心

##### ASRBR-API-CallCloudDnsApiFailed

## 错误码

**错误信息**

调用CloudDns接口失败。

**原因分析**

ASRBR管控在管理PrivateZone DNS解析时，调用CloudDns（天宫 PrivateZone）OpenAPI失败。 涉及的业务动作包括：查询私有域、创建私有域、新增/更新CNAME记录、绑定VPC。 当CloudDns接口返回ClientException（如网络错误、鉴权失败、参数非法）时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的CloudDns接口与返回的errorCode、errorMessage。
2. 常见原因：PrivateZone不存在、VPC绑定冲突、权限不足、CloudDns服务不可用。
3. 若无法明确原因，提取请求参数与响应内容，联系CloudDns/PrivateZone负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallCmsApiFailed

## 错误码

**错误信息**

调用CMS接口失败。

**原因分析**

涉及的业务动作包括：上报备份监控数据到CMS、查询CMS监控指标列表。 当CMS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的CMS接口与返回的errorCode、errorMessage。
2. 常见原因：CMS服务不可用、监控命名空间或指标名称配置错误、鉴权失败。
3. 若无法明确原因，提取请求参数与响应内容，联系CMS/云监控负责人协助排查。
4. 问题解决后，等待下一次上报/采集周期自动重试。
灾备管理中心

##### ASRBR-API-CallAasApiFailed

## 错误码

**错误信息**

调用AAS接口失败。

**原因分析**

ASRBR管控在执行账号认证相关操作时，调用AAS（账号认证服务）OpenAPI失败。 涉及的业务动作包括：创建阿里云账号、修改账号密码、查询账号AccessKey列表、获取账号基本信息、通过Ticket获取登录会话信息（用于控制台/OpenAPI 用户身份认证）。 当AAS接口返回服务端错误（如 InvalidTicket）、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的AAS接口与返回的errorCode、errorMessage。
2. 常见原因：Ticket已过期或无效、账号不存在、AAS服务不可用、网络连通性问题。
3. 若无法明确原因，提取请求参数与响应内容，联系AAS/账号认证服务负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallAnyBackupApiFailed

## 错误码

**错误信息**

**原因分析**

ASRBR管控在执行归档备份相关操作时，调用第三方AnyBackup（爱数）API失败。 涉及的业务动作包括：获取/同步OEM客户端列表、创建/修改/执行备份任务、创建/执行归档任务、查询归档恢复任务、管理云存储、查询磁带介质集等。 当HTTPS响应JSON解析失败、响应中error不为空且Code非Success或HTTPS 请求本身异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的AnyBackup接口与返回的error内容。
2. 常见原因：AnyBackup服务不可达（URL不可用）、接口返回业务错误、认证信息异常。
3. 若无法明确原因，提取请求参数与响应内容，联系AnyBackup/爱数产品负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallGwsApiFailed

## 错误码

**错误信息**

调用GWS接口失败。

**原因分析**

ASRBR管控在执行无影云桌面备份相关操作时，调用GWS（无影云桌面/EDS）产品侧OpenAPI失败。涉及的业务动作包括：查询桌面列表/办公网络/子网/策略组/桌面规格、运维查询桌面、创建迁移任务、查询用户UID等。 当GWS接口返回服务端错误、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的GWS接口与返回的errorCode、errorMessage。
2. 常见原因：桌面实例不存在、权限不足、GWS服务不可用、网络异常。
3. 若无法明确原因，提取请求参数与响应内容，联系GWS/无影云桌面产品负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallOssChijiApiFailed

## 错误码

**错误信息**

调用OSS赤骥接口失败。

**原因分析**

ASRBR管控在查询存储池容量配额信息时，调用OSS赤骥（chiji_inner）内部接口失败。 涉及的业务动作为：批量查询OSS Bucket配额范围（GetBucketQuotaRangeBatch），用于获取存储池的容量配额信息。 当OSS赤骥内部接口返回服务端错误或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位调用GetBucketQuotaRangeBatch时的请求参数与返回内容。
2. 常见原因：OSS赤骥内部服务不可用、Bucket名称不存在、网络连通性问题。
3. 若无法明确原因，提取请求参数与响应内容，联系OSS赤骥/存储平台负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallRamApiFailed

## 错误码

**错误信息**

调用RAM接口失败。

**原因分析**

涉及的业务动作包括：列出/获取/创建角色、创建策略、绑定/解绑策略、查询角色策略列表。 典型场景为创建备份计划或备份仓库时，需要初始化STS服务角色（如ADB/PolarDB备份角色）。 当RAM接口返回服务端错误（如角色不存在、策略已绑定）、鉴权失败或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位具体调用的RAM接口与返回的errorCode、errorMessage。
2. 常见原因：角色不存在需手动创建、策略已绑定或不兼容、RAM服务不可用、权限不足。
3. 若无法明确原因，提取请求参数与响应内容，联系RAM/权限管理负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallStsApiFailed

## 错误码

**错误信息**

调用STS接口失败。

**原因分析**

ASRBR管控在获取临时凭证时，调用STS（安全令牌服务）AssumeRoleWithServiceIdentity接口失败。 该凭证用于后续调用各产品OpenAPI（尤其是OSS）时的身份鉴权。 当STS接口返回错误（如角色不存在、权限不足）或网络异常时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过 traceId 查询系统日志，定位STS AssumeRole调用返回的errorCode、errorMessage。
2. 常见原因：服务角色不存在或未配置信任策略、权限策略不足、STS服务不可用。
3. 若无法明确原因，提取请求参数与响应内容，联系STS/RAM负责人协助排查。
灾备管理中心
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-CallDeDuplicationApiFailed

## 错误码

**错误信息**

调用重删服务接口失败。

**原因分析**

ASRBR管控在管理HBR重删存储（Deduplication Vault）时，调用重删服务HTTP接口失败。 涉及的业务动作包括：查询重删仓库列表、配置重删仓库。 当HTTP请求失败（响应为null、状态码非200）或响应JSON解析失败时，记录本错误码。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位调用重删服务时的HTTP请求URL与响应内容。
2. 常见原因：重删服务不可达、网络连通性异常、返回数据格式不合预期。
3. 若无法明确原因，提取请求参数与响应内容，联系HBR重删服务负责人协助排查。
4. 问题解决后，重新触发相关操作。

##### ASRBR-API-ApiQueryResultEmpty

## 错误码

**错误信息**

下游接口查询结果为空。

**原因分析**

ASRBR管控在调用下游产品或服务接口查询数据（如实例信息、快照、客户端信息、备份计划ID等）时， 接口返回为null、空列表，或返回成功但关键字段缺失。 常见于目标资源不存在、已被删除、查询条件不匹配或下游服务未正确返回数据。

**置信等级**

B

**解决方案**

（1）通过traceId查询系统日志，定位具体调用的接口与查询参数。 （2）确认查询的目标资源是否存在、查询条件（实例ID、账号等）是否正确。 （3）若无法明确原因，提取请求参数与响应内容，联系对应产品负责人协助排查。 （4）问题解决后，重新触发相关操作。 灾备管理中心

##### ASRBR-API-CallDownstreamApiFailed

## 错误码

**错误信息**

下游接口调用异常。

**原因分析**

ASRBR管控通过统一HTTP/REST调用封装访问下游服务时发生异常。触发场景包括：
1. 响应体无法解析为预期的JSON结构。
2. 响应状态码既非成功码，下游又未返回明确的业务错误码。
3. 调用过程中抛出网络等未预期异常。

**置信等级**

B

**解决方案**

1. 通过traceId查询系统日志，定位调用的下游接口地址与响应内容。
2. 常见原因包括：下游服务不可用、网络连通性异常、返回数据格式不合预期、鉴权失败。
3. 若无法明确原因，提取请求参数与响应内容，联系对应下游服务负责人协助排查。
4. 问题解决后，重新触发相关操作。

### HBRC

#### HBRC-COM-InternalError

## 错误码

**错误信息**

HBR-Console服务内部错误。

**原因分析**

该错误表示HBR-Console服务遇到了未预期的内部异常，可能发生在以下任一环节：
1. 权限校验异常：调用RAM（资源访问管理）服务进行权限验证时失败，可能是RAM服务不可用、授权策
略配置异常或STS临时凭证已过期。
2. 消息队列通信异常：与消息中间件（RabbitMQ）交互时失败，可能是消息队列服务不可用、连接超时或
消息发送/接收异常，导致备份或恢复任务无法正常下发。
3. 数据加解密异常：在加解密敏感信息（如访问密钥、连接凭证）时失败，可能是密钥配置缺失或数据格式
损坏。
4. 数据源配置异常：系统数据库连接初始化失败，可能是数据库配置缺失或数据库实例不可达。
5. 系统配置缺失：读取系统级配置项时未找到必要的数据，可能是部署环境配置不完整。
6. 备份任务执行异常：备份任务在下发执行阶段遇到了未预期的异常，导致任务状态无法正常更新。
灾备管理中心
7. 未预期的系统异常：请求处理过程中发生了未被特定错误码覆盖的异常，由全局异常处理器统一捕获并返
回此错误码。

**置信等级**

B

**解决方案**

根据RequestId/traceId在服务端日志中检索对应的调用链路，从异常堆栈和触发上下文中确定具体的失败原因。
1. 若操作涉及权限相关，则检查RAM角色授权是否正常，STS凭证是否有效，必要时重新授权后重试。
2. 若操作涉及备份/恢复任务下发，则检查消息队列服务是否正常运行，确认网络连通性后重试操作。
3. 若操作涉及系统配置（如首次部署、环境迁移），则检查数据库连接配置、系统参数配置是否完整且正
确。
4. 若以上排查均未发现问题，或错误无明确触发场景，则联系技术支持，提供服务端日志中的
RequestId/traceId以便进一步定位。

#### HBRC-COM-SendMqMessageError

## 错误码

**错误信息**

向消息队列发送消息失败。

**原因分析**

备份任务创建完成后，HBR-Console需要将任务消息投递到消息队列（MQ），由后端执行器接收并执行。 当消息投递到MQ失败时，任务无法进入执行队列，被标记为失败并记录本错误码。常见于消息队列服务不可用、连接异常或网络问题。

**置信等级**

B

**解决方案**

1. 通过任务的errorMessage与traceId检索日志，确认消息投递失败的具体原因。
2. 检查消息队列服务是否正常运行、连接配置与网络连通性是否正常。
3. 确认目标队列是否存在、是否可正常收发消息。
4. 消息队列恢复后，重新触发备份任务。

#### HBRC-SNAP-

**CannotDeleteLatestSnapshot**

## 错误码

**错误信息**

无法删除最新的快照。 灾备管理中心

**原因分析**

用户请求删除的快照是当前备份仓库/客户端维度下最新的一个可恢复备份点。为防止误删最近的可恢复点导致无可用恢复数据，系统禁止删除最新快照并记录本错误码。

**置信等级**

B

**解决方案**

该最新快照为最近的可恢复点，不支持删除。如需清理历史快照，请选择非最新的快照进行删除。

#### HBRC-SNAP-SnapshotNotExist

## 错误码

**错误信息**

指定的快照不存在，请修改参数。

**原因分析**

在执行恢复、浏览快照文件、删除快照、快照拷贝等操作时，系统按快照ID查询对应的快照记录但未找到。 常见根因：
1. 传入的快照ID有误或与操作对应的资源类型不匹配。
2. 该快照已被删除。
3. 该快照已超过保留期被自动清理（过期快照同样视为不存在）。

**置信等级**

B

**解决方案**

1. 核对传入的快照ID是否正确，以及是否与操作对应的资源类型匹配。
2. 前往ECS产品侧查看对应的快照信息，确认该快照是否仍然存在、是否已被删除或过期清理。
3. 若快照已不存在，改用其他有效的快照重新发起操作。

#### HBRC-UDM-

**CreateConsistentSnapshotGroupFailed**

## 错误码

#### HBRC-UDM-CreateConsistentSnapshotGroupFailed

**错误信息**

创建一致性快照组失败。

**原因分析**

当备份计划要求创建一致性快照组（应用一致或文件系统一致）时，系统会为实例的多块磁盘创建一致性快照组。 灾备管理中心专有云场景下，若一致性快照组创建失败，任务不降级为普通快照而直接判为失败并记录本错误码。常见于磁盘不支持快照组、实例磁盘数量或类型不满足要求、应用一致所需的权限（RAM角色）未绑定，或云平台创建快照组接口调用失败。

**置信等级**

B

**解决方案**

1. 通过任务的errorMessage（可能含降级原因，如磁盘不支持快照组）与traceId检索日志，确认创建一
致性快照组失败的具体原因。
2. 前往ECS产品侧查看对应实例与磁盘的信息，确认磁盘是否支持一致性快照组、磁盘数量与类型是否满足
要求。
3. 若为应用一致性备份，确认实例已绑定所需的RAM角色。
4. 若无需一致性快照，调整备份计划取消一致性快照组要求后重试，否则修复上述条件后重新触发备份。

#### HBRC-UDM-

**CreateNativeEbsSnapshotError**

## 错误码

**错误信息**

创建EBS快照失败。

**原因分析**

在ECS云盘备份流程中，系统需要调用云平台接口为磁盘创建底层EBS快照。 当创建接口调用失败、未返回有效快照ID或创建后回查不到该快照时，任务被标记为失败并记录本错误码。 常见于快照配额不足、账号权限不足、磁盘状态异常或底层快照已丢失。

**置信等级**

B

**解决方案**

1. 通过任务的errorMessage与traceId检索日志，确认底层创建快照失败的具体原因。
2. 前往ECS产品侧查看对应磁盘的快照信息与快照配额，确认磁盘状态是否正常、快照配额是否充足。
3. 确认备份所用凭证是否具备创建快照的权限。
4. 问题解决后，重新触发备份任务。

#### HBRC-UDM-NoRunningDiskBackupJobs

## 错误码

**错误信息**

整机备份执行失败，所有云盘备份任务均未能正常启动。 灾备管理中心

**原因分析**

在执行整机备份时，系统会为每台云盘创建独立的备份子任务并下发执行。当所有云盘子任务均执行失败时，整机备份任务将被标记为失败。常见原因包括：
1. 云盘快照不存在或已被删除，导致备份无法获取有效的数据快照。
2. 访问云服务所需的凭证已过期或失效，导致无法调用云资源。
3. 备份执行过程中云盘被释放或卸载，导致快照创建失败。
4. 备份消息下发异常，导致备份任务无法正常分发到执行端。

**置信等级**

B

**解决方案**

根据RequestId/traceId在服务端日志中检索对应的调用链路，从异常堆栈和触发上下文中确定具体的失败原因。
1. 若提示快照相关错误，则检查ECS实例的云盘快照是否正常，确认快照未被手动删除或清理；
2. 若提示权限或凭证相关错误，则检查RAM角色授权是否有效，必要时重新进行授权操作；
3. 若提示云盘不存在或不可用，请检查ECS实例的云盘状态，确认没有云盘在备份期间被释放或卸载。
4. 若提示系统内部错误，则稍后重试备份任务或者联系技术支持，提供服务端日志中的RequestId/traceId
以便进一步定位。

#### HBRC-JOB-AgentReportTimeout

## 错误码

**错误信息**

Agent failed to report backup job progress within the expected time, job expired.

**原因分析**

备份任务由部署在物理机上的备份Agent负责实际执行，Agent在执行过程中会通过消息队列持续向HBR- Console上报任务进度与状态。任务在创建时会被分配一个初始的预期完成时间，Agent每次上报进度时可以携带一个新的、更晚的预期完成时间，通过这种“心跳续命”的方式把过期时间不断向后推移。HBR- Console会周期性扫描仍未推进到终态的备份任务，一旦发现某个任务已经超过其当前预期完成时间但仍未到达终态，就会将其判定为过期并抛出该错误码。 从业务侧看，触发该错误的可能原因包括：
1. 备份Agent未正常运行：物理机上的备份Agent由于进程异常退出、未启动等原因，导致任务创建后
Agent从未回报过进度，任务始终停留在初始预期完成时间上，直至被判定过期。
2. Agent与HBR-Console之间的上报通道不通：物理机与消息队列之间的网络中断、消息队列服务不可用
或鉴权失效，导致Agent上报的心跳消息无法送达HBR-Console，“心跳续命”链路中断。

**置信等级**

A

**解决方案**

根据jobId在HBR-Console服务端日志中检索该任务的Agent 上报记录，判断任务生命周期内是否收到过 Agent 的进度上报，以此区分故障方向。 灾备管理中心
1. 若整个任务生命周期内从未收到Agent上报，则检查物理机上备份Agent是否在运行、日志中是否有异常
退出记录，同时检查物理机到消息队列的网络连通性与鉴权配置，恢复后重新触发备份计划。
2. 若Agent有上报但任务停留在执行中状态未能续命至终态，则结合Agent端的执行日志排查问题，处理完
成后重新触发备份。
3. 若以上排查均未定位到具体原因，则联系技术支持，提供jobId与相关时间段的HBR-Console日志以便进
一步定位。
