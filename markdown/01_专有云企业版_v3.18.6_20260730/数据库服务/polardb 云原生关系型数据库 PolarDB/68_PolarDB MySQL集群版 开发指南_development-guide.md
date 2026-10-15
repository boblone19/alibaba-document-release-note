---
title: "云原生关系型数据库 PolarDB PolarDB MySQL集群版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 333
source_pdf: "68_PolarDB MySQL集群版 开发指南_development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/polardb/zh/development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云原生关系型数据库 PolarDB PolarDB MySQL集群版 开发指南

云原生数据库速入门

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
云原生数据库速入门
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 获取AccessKey。
云原生数据库速入门获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizati onList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourc eGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织 ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参见开发文档使用说明。
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
云原生数据库备工作

## 准备工作

### 登录开发者门户

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
2. 输入正确的用户名及密码。
请向运营管理员获取登录控制台的用户名和密码。

**说明**

首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且至少包含以下两种类型： 英文大写或小写字母（A~Z、a~z） 阿拉伯数字（0~9） 特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）
3. 单击**账号登录**。
4. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：
管理员强制开启MFA后的首次登录： a. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定MFA设备。 b. 按照步骤2重新输入账号和密码，单击**账号登录**。 c. 输入6位MFA码后单击**认证**。 您已开启并绑定MFA： 输入6位MFA码后单击**认证**。
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者门户**。

### 查看API信息及其EndPoint

您在使用SDK时，需要获取产品名称、API名称和API版本。本文介绍如何查看API信息。

**背景信息**

API审计中的API仅供调用参考，具体API的使用方式需要参见各云产品的API文档。如果发生不一致情况，以API支持情况为准。

**操作步骤**

1. 登录开发者门户。
2. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
3. 在左侧导航栏中选择目标云产品。
云原生数据库备工作
4. 在**版本**下拉列表中，选择目标API版本。
5. 在下方API列表中，您可浏览当前版本的所有API接口。
6. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您介绍如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中 AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参见获取 STS AccessKey。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |

云原生数据库备工作

| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |
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

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 云原生数据库备工作 ii. 单击页面右上角的用户头像，单击**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com>，请替换为实际的STS Endpoint。 云原生数据库备工作

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
云原生数据库备工作

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourStsAccesskeyID>，请替换为您实际的STS Accesskey ID。 <yourStsAccessKeySecret>，请替换为您实际的STS Accesskey Secret。 <yourStsToken>，请替换为实际STS三元组中的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`// <yourRegionID>`请替换为您实际的地域`ID` `// <yourStsAccessKeyID>, <yourStsAccessKeySecret>`请替换为前一步获取到的`STS`三元组中`AccessKeyID`

```xml
、AccessKeySecret
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

### 获取公共Header参数

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。 云原生数据库备工作

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，获取方式请参见获取Region ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取集群ID。 |

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

**获取集群ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**数据库**>**云原生关系型数据库****PolarDB**。
3. 在集群列表中查看**集群****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |

云原生数据库备工作

| Department | 组织ID。 |
|---|---|

云原生数据库

## Java SDK调用

### 快速开始

本节介绍如何获取PolarDB Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。在Apsara Stack控制台上获取和查看您的AccessKey。 获取产品的endpoint。 阿里云专有云Java SDK需要1.6以上的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用产品的开发工具包，必须安装SDK核心库以及产品的SDK。 其中，SDK核心库的版本为3.7.1，PolarDB SDK的版本为1.8.27。

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>3.7.1</version>
            <scope>system</scope>
            <systemPath>${project.basedir}/lib/aliyun-java-sdk-core-3.7.1.jar</systemPath>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-ecs</artifactId>
            <version>3.5.0</version>
            <scope>system</scope>
            <systemPath>${project.basedir}/lib/aliyun-java-sdk-polardb-1.8.27.jar</systemPath>
        </dependency>
    </dependencies>
```

**使用Java SDK**

以下这个代码示例展示了调用阿里云专有云Java SDK的3个主要步骤：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
云原生数据库

```java
package com.testprogram;
 import com.aliyuncs.profile.DefaultProfile;
 import com.aliyuncs.DefaultAcsClient;
 import com.aliyuncs.IAcsClient;
 import com.aliyuncs.exceptions.ClientException;
 import com.aliyuncs.exceptions.ServerException;
 import com.aliyuncs.ecs.model.v20140526.*;
 public class Main {
     public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
         DefaultProfile profile = DefaultProfile.getProfile(
             "<your-region-id>",          // 区域名
             "<your-access-key-id>",      // 授权账号的AccessKey ID
             "<your-access-key-secret>"); // 授权账号Access Key Secret
```

`//` 设置当前产品的`endpoint`

```
        profile.addEndpoint("your-region-id", "your-region-id", "product", "endpoint");
         IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```
         DescribeInstancesRequest request = new DescribeInstancesRequest();
         request.setPageSize(10);
```

`//` 发起请求并处理应答或异常

```java
         DescribeInstancesResponse response;
         try {
             response = client.getAcsResponse(request);
             for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
                 System.out.println(instance.getPublicIpAddress());
             }
         } catch (ServerException e) {
             e.printStackTrace();
         } catch (ClientException e) {
             e.printStackTrace();
         }
     }
 }
```

### 使用手册

#### 安装Java SDK

本文档介绍如何安装及调用PolarDB Java SDK。 阿里云专有云Java SDK支持1.6及以上版本的JDK，可以通过导入JAR文件的方式进行安装。 您可以点击SDK下载下载PolarDB JAR文件。 无论您使用Eclipse还是IntelliJ作为集成开发环境，都可以通过导入JAR文件的方式安装 PolarDB Java SDK。 安装方法如下： 使用Eclipse安装完成以下操作，在Eclipse的项目中安装ECS Java SDK： i. 将下载的 `aliyun-java-sdk-polardb.jar` 文件复制到您的项目文件夹中。 ii. 在Eclipse中打开您的项目，右键单击该项目，单击**Properties**。 iii. 在弹出的对话框中，单击**Java Build Path > Libraries > Add JARs**添加下载的JAR文件。 iv. 单击**Apply and Close**。 使用IntelliJ安装云原生数据库完成以下操作，在IntelliJ的项目中安装阿里云专有云Java SDK： i. 将下载的 `aliyun-java-sdk-polardb.jar` 文件复制到您的项目文件夹中。 ii. 在IntelliJ中打开您的项目，在菜单栏中单击**File > Project Structure**。 iii. 单击**Apply**，然后单击**OK**。

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的

**重要**

信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<your-region-id>",          // 区域名
    "<your-access-key-id>",      // 授权账号的AccessKey ID
    "<your-access-key-secret>"); // 授权账号AccessKey Secret
```

#### 发起调用

本节介绍如何使用 PolarDB Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例如DescribeDBCluster。 在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。

```
DescribeInstancesRequest request = new DescribeInstancesRequest(); request.setPageSize(10);
```

3. 发起调用并处理应答。

```java
DescribeInstancesResponse response; try {
    response = client.getAcsResponse(request);
    for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.getPublicIpAddress());
    }
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
instanceStatus := response.getStatus()
```

云原生数据库如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过以使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    FooResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`

```
    // ...
}catch (ServerException e){
```

`//` 这里可以添加您自己的错误处理逻辑 `//` 例如，打印具体的错误信息

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`//` 如果遇上棘手问题，可以提交工单，并将`RequestId`提供给我们

```java
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
```

`//` 这里可以添加您自己的错误处理逻辑 `//` 例如，打印具体的错误信息

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，可以采用泛用型的API调用方式（CommonRequest）。使用 CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 云原生数据库接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.ApiName = "<Action>"` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.ApiName =` `"RunInstances"` 来指定API名称。 您需要获取**PathPattern**参数，使用 `request.PathPattern = "<PathPattern>"` 的方式来指定RESTful路径。 例如查看所有集群实例的API的**PathPattern**为 `/clusters` ，在发起CommonRequest请求时，要使用 `request.PathPattern = "/clusters"` 指定RESTful路径。

**示例：调用RPC风格的API**

以下代码展示了如何使用CommonRequest的方式调用DescribeInstanceStatus接口：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<your-access-key-id>",      // 您的AccessKey ID
            "<your-access-key-secret>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
        CommonRequest request = new CommonRequest();
        request.setDomain("ecs.aliyuncs.com");
        request.setVersion("2014-05-26");
        request.setAction("DescribeInstanceStatus");
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

**示例：调用RESTful风格的API**

以下代码展示了如何使用CommonRequest的方式调用查看所有集群实例接口： 云原生数据库

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化

```
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // 您的地域ID
            "<your-access-key-id>",      // 您的AccessKey ID
            "<your-access-key-secret>"); // 您的AccessKey Secret
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数

```java
        CommonRequest request = new CommonRequest();
        request.setDomain("cs.aliyuncs.com");
        request.setVersion("2015-12-15");
        request.setUriPattern("/clusters");
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

#### 常见错误

您可以参考本文档中提供的常见问题排查SDK使用中的问题。

|  |  | 错误码 |  |  |  |  |  | 错误信息 |  |  |  | 原因 | 解决方法 |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | SDK.CanNotResol |  |  |  |  |  | Can not |  |  |  |  | 检查提供的区域ID和endpoint是否正确。获取 endpoint后，可以通过以下代码设定 endpoint： DefaultProfile.addEndpoint("your- region-id", "your-region-id", "product", "endpoint""); |  |
|  |  |  |  |  |  |  |  |  | Can not |  |  |  | endpoint后，可以通 endpoint： |  |
|  |  |  | SDK.CanN |  |  |  |  | resolve |  |  |  | SDK无法自动获取调 |  | Defau |
|  |  |  |  | SDK.CanN |  | otResol |  |  |  |  |  | 用的产品在特定 |  |  |
|  |  |  |  |  |  |  |  | endpoint, |  |  | please | region的 |  |  |
|  |  | veEndpoint |  | Endpoint |  |  |  |  |  |  |  | re |  |  |
|  |  |  |  |  |  |  |  | check the user |  |  |  | en |  |  |
|  |  |  |  |  |  |  |  | guide |  |  |  |  |  |  |
|  |  | SDK.JsonUnmarsh |  |  |  |  |  | Failed to |  |  |  | SDK反序列化应答失败，大部分情况下是由于SDK实际收到的应答结构与ApiMeta 不符（例如字段不匹配，格式不正确等原因）导致的。 | 您可以通过使用 client.doAction(request) 方法，获取原始的HTTP应答。 |  |
|  |  |  |  |  |  |  |  |  | Failed to |  |  | 败，大部分情况由于SDK实际收 |  |  |
|  |  |  |  |  |  |  |  |  | Fail |  |  |  |  |  |
|  |  |  |  |  | nUnmarsh |  |  | unmars |  |  |  |  |  |  |
|  |  | alError |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | response |  |  |  |  |  |  |

云原生数据库

|  |  |  |  |  |  |  |  |  | The request |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  | The request |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | timed out 4 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | times(3 for |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | retry), perhaps |  |  |  |  | 如果存在其他低质量网络场景，建议考虑适 |  |  |  |
|  |  |  |  | SDK.TimeoutErro |  |  |  |  |  |  |  |  | 请求超时，并且所有 |  | 如果存在其他低质量 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | we should have |  |  |  |  | 长超时时间或最大重 |  |  |  |
|  |  |  | r |  |  |  |  |  |  |  |  |  | 重试均失败。 |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | the |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | threshold raised |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | a little? |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | Your request |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | Your request |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | is denied as |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | lack of ssl |  |  |  |  |  |  |  |  |  |
|  |  |  |  | SDK.ServerError |  |  |  |  |  |  |  |  |  |  | 在发送request前，添加以下代码： |  |  |  |
|  |  |  |  |  |  |  |  |  | protect.Recommend |  |  |  | API只 | 接受HTTPS请 |  |  |  |  |
|  |  |  | ： |  |  |  |  |  |  |  |  |  |  |  |  | request.setProtocol(ProtocolType.H |  |  |
|  |  |  |  |  |  |  |  |  | :http |  | s: | //error- | 求，不接受HTTP请 |  |  |  |  |  |
|  |  |  | InvalidProtocol.N |  |  |  |  |  |  |  |  |  |  |  |  | TTPS) |  |  |
|  |  |  |  |  |  |  |  |  | cente |  | r.aliyun.com |  | 求。 |  |  |  |  |  |
|  |  |  | eedSsl |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | /status/search? |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | Keyword=InvalidPr |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | otocol.NeedSsl&so |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  | urce=PopGw |  |  |  |  |  |  |  |  |  |

云原生数据库

## Python SDK调用示例

### 快速开始

本节介绍如何获取PolarDB Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体请参见获取 AccessKey。 获取Endpoint，具体操作参见获取Endpoint。
1. 安装SDK核心库。
如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装SDK。
以下以安装云服务器ECS的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装云服务器ECS的SDK：

```
pip install aliyun-python-sdk-ecs
```

如果您使用的是Python 3.x，执行以下命令，安装云服务器ECS的SDK：

```
pip3 install aliyun-python-sdk-ecs
```

**使用Python SDK**

以下示例以ECS为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuns.com>，请替换为您实际的产品访问地址。 云原生数据库

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID` `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`

```bash
acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret
# product config
```

`product_name = 'ECS' #` 填写产品名称 `endpoint = '<ecs.aliyuns.com>' #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeInstancesRequest.DescribeInstancesRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```bash
# get response
response = clt.do_action_with_exception(request) print response
```

### 使用手册

#### 安装Python SDK

本文档介绍如何安装及调用PolarDB Python SDK。 阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用ECS的Python SDK，您需要安装阿里云Python SDK核心库和ECS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

安装云产品的SDK，以下以安装ECS的SDK为例。 如果您使用的是Python 2.x，执行以下命令，安装ECS的SDK：

```
pip install aliyun-python-sdk-ecs
```

如果您使用的是Python 3.x，执行以下命令，安装ECS的SDK：

```
pip3 install aliyun-python-sdk-ecs
```

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。 云原生数据库

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在 Python中添加OpenSSL 支持。OpenSSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No` `module named ssl` 的错误信息，说明已经支持OpenSSL。 若没有OpenSSL，运行以下命令安装： `pip install pyopenssl #Python2`使用此命令。

**说明**

若本地环境为Python3，则运行 `pip3 install pyopenssl` 命令。

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用：

```
request = DescribeInstancesRequest() request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 发起调用

本节介绍如何使用PolarDB Python SDK发起请求。

**操作步骤**

1. 导入相关产品的SDK。
云原生数据库

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

2. 新建一个AcsClient。

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。

```
response = clt.do_action_with_exception(request) print response
```

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
```

# 这里可以添加您自己的错误处理逻辑
# 例如，打印具体的错误信息

```
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下：
1. 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。
2. 简便：无需更新SDK即可调用最新发布的API。
3. 快速迭代。
云原生数据库发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 RPC风格的API： 您需要获取**Action**参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。 例如RunInstances接口，在发起CommonRequest请求时，需要使用 `request.set_action_name('RunInstances')` 来指定API名称。 RESTful风格的API： 您需要获取**PathPattern**参数，使用 `request.set_uri_pattern('Pattern')` 的方式来指定RESTful。 例如查看所有集群实例的API的**PathPattern**为 `/api/v1/clusters` ，在发起CommonRequest请求时， 要使用 `request.set_uri_pattern ('/api/v1/clusters')` 指定RESTful路径。

**示例：调用RPC风格的API**

以下代码为云服务器（ECS）的DescribeInstanceStatus接口，获取实例状态列表的调用示例：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <ecs.aliyuncs.com>，请替换为您实际的产品访问地址。 云原生数据库

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Ecs') request.set_action_name('DescribeInstanceStatus') request.set_version('2014-05-26')
```

`request.set_domain('<ecs.aliyuncs.com>') #`产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = = CommonRequest(product='Ecs', action_name='DescribeInstanceStatus',version='2014-
05-26',domain='ecs.aliyuncs.com')
######
```

# 设置请求协议类型,支持`https`或`http,`默认为`http`
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段
# 调用方法如下：

```bash
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
```

# 请替换为您实际的`SecurityToken`

```
######
```

# 非必填，请替换为您实际的资源集`ID`

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
```

# 必填，请替换为您实际的组织`ID`

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 必填，调用来源说明

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
```

# 非必填（企业版`V3.15.0`及之前历史版本需要），请替换为您实际的地域`ID`

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时需要），请替换为您实际的实例`ID`

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

**示例：调用RESTful风格的API**

当调用RESTful风格的API时，业务参数传参方式根据接口请求方式和ContentType分为两种： 接口请求方式为 `GET` 或 `DELETE` ，或ContentType为 `application/x-www-form-urlencoded` ，使用以下方式传参：

| 例如 request.add query param("page number", "1") _ _ _ |  |  |  |
|---|---|---|---|
| PUT | ，且ContentType为 | application/json | ，使用以 |

将请求参数放在Body中，例如：

```
body = '{"page_number":"1",page_size"5":"SecurityToken","":"<yourSecurityToken>"}' request.set_content(body.encode('utf-8'))
```

以下代码为容器服务（CS）的DescribeClusterV1接口，获取集群列表的调用示例： 云原生数据库

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <cs.aliyuncs.com>，请替换为您实际的产品访问地址。 云原生数据库

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
######
# API:CS-DescribeClusterV1
######
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CS') request.set_version('2015-12-15') request.set_uri_pattern('/api/v1/clusters') # Pattern
```

`request.set_domain('<cs.aliyuncs.com>') #` 产品访问域名,当前为示例值,请替换为您实际的产品访问地址

```bash
# or:
# request = CommonRequest(product='CS', version='2015-12-15', uri_pattern='/api/v1/clusters',
domain='cs.aliyuns.com')
######
```

# 设置请求协议类型,支持 `HTTP` 或 `HTTPS,`默认为`HTTP`
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('GET') request.add_header('Content-Type', 'application/json')
```

# 非必填，请替换为您实际的资源集`ID`

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID")
```

# 必填，请替换为您实际的组织`ID`

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 必填，调用来源说明

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
```

# 非必填（企业版`V3.15.0`及之前历史版本需要）,请替换为您实际的地域`ID`

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时需要）,请替换为您实际的实例`ID`

```bash
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
```

# 业务参数,请求方式为`GET`、`DELETE` 或`ContentType`为`application/x-www-form-urlencoded,`则使用以下方式传数据

```
request.add_query_param("page_number", "1") request.add_query_param("page_size", "5")
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段
# 调用方法如下：

```bash
# body = '''{\"SecurityToken\", \"<yourSecurityToken>\"}'''
```

# 请替换为您实际的`SecurityToken`

```
######
######
```

# 若接口请求方式是`POST`、`PUT` 且`ContentType`为`application/json,`则以下方式传数据

```python
# body = '{"page_number":"1",page_size"5":"SecurityToken","":"<your-SecurityToken>"}'
# request.set_content(body.encode('utf-8'))
######
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

云原生数据库

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问。本操作介绍如何获取阿里云PolarDB Go SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。在Apsara Unimanager运营控制台上获取和查看您的AccessKey。 获取PolarDB的Endpoint，具体操作参见获取Endpoint。

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

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您实际的Endpoint。 云原生数据库

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

)

```
func main() {
```

`//` 创建`ecsClient`实例

```
    ecsClient, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
    if err != nil {
```

`//` 异常处理

```
        panic(err)
    }
```

`//` 创建`API`请求并设置参数

```
    request := ecs.CreateDescribeInstancesRequest()
```

`//` 设置当前产品的`Endpoint`

```
    request.Domain = "<Endpoint>"
    // 等价于 request.PageSize = "10"
    request.PageSize = requests.NewInteger(10)
```

`//` 发起请求并处理异常

```
    response, err := ecsClient.DescribeInstances(request)
    if err != nil {
```

`//` 异常处理

```
        panic(err)
    }
    fmt.Println(response)
}
```

4. （可选）切换HTTP/HTTPS协议。

```
request.Scheme = "HTTPS"
```

### 使用手册

#### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭据，需要在初始化Client时设置凭证。

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的阿里云账号的信息安全。 云原生数据库以下代码以ECS为例，展示初始化ecsClient实例。 `//` 初始化`ecsClient`实例

```
ecsClient, err := ecs.NewClientWithAccessKey(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的的`AccessKey ID`

```
        "<yourAccessKeySecret>")        // 请替换为您实际的AccessKey Secret
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 发起调用

本文介绍如何使用PolarDB Go SDK发起调用。 以下步骤以ECS为例，展示使用ECS Go SDK发起调用。
1. 导入云产品SDK。

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. 新建一个产品名Client，该client中包含产品名的所有API。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 `ecsClient,err := <ecs>.NewClientWithAccessKey( //`请替换为您实际的产品名称 `"<yourRegionID>", //` 请替换为您实际的`RegionID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID` `"<yourAccessKeySecret>") //` 请替换为您实际的`AccessKeySecret` `ecsClient.Domain = "ecs.aliyuns.com" //`设置请求域名地址，当前为示例值，请求根据实际请求地址替换。
3. 使用 `xxx.CreateXXXRequest` 方法创建一个请求。
该方法的命名规范为 ${service}.Create${apiName}Request ，其中：
**${service}**为产品名称(小写)。例如ecs。
**${apiName}**为API名称，例如DescribeInstances。

```
request := ecs.CreateDescribeInstanceAttributeRequest() request.InstanceId = ""
```

4. 发起调用。

```
response, err := ecsClient.DescribeInstanceAttribute(request)
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。 云原生数据库

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 以下以ECS为例，您可以通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
```

`//` 获取错误码

```
    clientError.ErrorCode()
```

`//` 获取错误描述

```
    clientError.Message()
```

`//` 获取原始错误(可能为`nil)`

```
    clientError.OriginError()
}
```

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 以下以ECS为例，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" //ecs请替换为您实际的产品名称 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

云原生数据库

```
response, err := ecsClient.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
```

`//` 获取错误码

```
    serverError.ErrorCode()
```

`//` 获取错误描述

```
    serverError.Message()
```

`//` 获取原始`http`应答

```
    response.GetOriginHttpResponse()
}
```

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**示例：调用RPC风格的API**

以下代码为云产品 ECS（云服务器）的DescribeInstanceStatus接口，获取实例状态列表的调用示例（ECS产品属于RPC的调用风格）： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <ecs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 云原生数据库

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID` `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID` `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<ecs.aliyuncs.com>" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "Ecs"
    request.Version = "2014-05-26"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)`

```
    request.ApiName = "DescribeInstanceStatus"
```

`//` 业务参数

```
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*` 当使用`STS AccessKey`调用`RPC`接口时，需要在参数中加上`SecurityToken`字段调用方式如下：

```
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
```

请替换为您实际的`SecurityToken` `*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // 必填，调用来源说明
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本需要 ），请替换为您实际的地域`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填，请替换为您实际的
```

资源集`ID` `request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" //` 必填，请替换为您实际的组织I D `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时需要），请替换为您实际的实例`ID`

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

**示例：调用RESTful风格的API**

当调用RESTful风格的API时，业务参数传参方式根据接口请求方式和ContentType分为两种： 接口请求方式为 `GET` 或 `DELETE` ，或ContentType为 `application/x-www-form-urlencoded` ，使用以下方式传参：

| 例如 request.QueryParams["page number"] = "1" _ |  |  |  |
|---|---|---|---|
| PUT | ，且ContentType为 | application/json | ，使 |

云原生数据库

```
body := "{\"page_number\":\"1\",page_size:\"5\"}" request.SetContent([]byte(body)) request.SetContentType("application/json")
```

以下代码为云产品 CS(容器服务) 的DescribeClusterV1接口，获取集群列表的调用示例（CS产品属于RESTful的调用风格）： 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

**说明**

涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <cs.aliyuncs.com>，请替换为您实际的产品访问请求地址。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 云原生数据库

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

)

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID` `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID` `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "GET"
```

`request.Domain = "cs.aliyuncs.com" //` 请求访问地址,当前为示例值,请根据实际请求地址替换

```
    request.Product = "CS"
    request.Version = "2015-12-15"
```

`//` 因为是`Restful`接口，因此需指定`PathPattern`

```
    request.PathPattern = "/api/v1/clusters"
```

`//` 当使用`STS AccesssKey`调用`ROA`接口时需要在`header`中加上`x-acs-security-token`字段

```
    // request.Headers["x-acs-security-token"] = "<yourSecurityToken>"
```

`//` 必填值，调用来源说明

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
```

`//` 非必填，企业版`V3.15.0`及之前历史版本需要

```
    request.Headers["x-acs-regionid"] = "<yourRegionID>"
```

`//` 非必填，请替换为您实际的资源集`ID`

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>"
```

`//` 必填，请替换为您实际的组织`ID`

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"
```

`//` 非必填，修改、删除、查看单实例详情时需要，请替换为您实际的实例`ID`

```
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>"
```

`//` 业务参数,当请求方式为`GET`、`DELETE` 或 `ContentType`为`application/x-www-form-urlencoded`时，使用以下方式传数据

```
    // request.QueryParams["page_number"] =  "1"
    // request.QueryParams["page_size"] = "5"
```

`//` 当接口请求方式是`POST`、`PUT` 且`ContentType`为`application/json`时，则使用以下方式传数据

```
    // body := "{\"page_number\":\"1\",page_size:\"5\"}"
    // request.SetContent([]byte(body))
    // request.SetContentType("application/json")
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

云原生数据库 I参考

## API参考

### DescribeSQLListV4

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | System | 是 | DescribeSQLListV4 | 系统规定参数。取值： DescribeSQLListV4 |
| InstanceID | String | Query | 是 | rm-my6ypxhaff547**** | 实例ID。 |
| StartTime | String | Query | 是 | 2025-08-07T06:47:00Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2025-08-07T07:02:00Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数。取值： 30 50 100 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |
| Engine | String | Query | 否 | PolarDBMySQLLocalDisk | 数据库引擎。 |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SQLTemplateIte ms | Array | SQL List | 慢日志明细列表。 |
| -SQLHash | String | 455294895%**** _ | 慢日志统计里的SQL语句唯一标识符，可用于获取该 SQL语句的慢日志明细。 |

| olarDB MySQL集 | 群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -InstanceId | String | rm- my6ypxhaff547**** | 实例ID。 |
| -SQLContent | String | /* Query from DMS- WEBSQL-0- Qid 1754550112435 _ by user 142195380638**** */ select sleep(1) from dual | SQL命令详情。 |
| -QueryTime | Long | 1 | SQL执行时长（s）。 |
| -RowsExam | Long | 0 | 扫描行数。 |
| -SourceIP | Long | 10.XXX.XX.165 | 源端IP。 |
| -StartTime | String | 2025-08-07 15:01:52.488 | 后台执行该任务的时间。 |
| -RowsSent | Long | 1 | 返回行数。 |
| -DBName | String | testdb | 数据库名称。 |
| -UserHost | Long | testadmin@10.XXX.X X.165 | 用户的主机IP地址，用于标识网络中的客户端设备。 |
| RequestId | String | 5B2E3D79-21A0- 4471-8055- ED2AF71F**** | 请求ID。 |
| success | String | true | 请求结果。取值： true ：请求成功。 false ：请求失败。 |
| code | String | 200 | 接口状态或POP错误码。 |
| message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful；请求失败时会返回请求异常信息（如错误码等）。 |
| TotalRecordCou nt | Integer | 3 | 总记录数。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCou nt | Integer | 3 | 本页记录数量。 |

云原生数据库 I参考

**示例**

请求示例

```
&InstanceID=rm-my6ypxhaff547**** &StartTime=2025-08-07T06:47:00Z &EndTime=2025-08-07T07:02:00Z
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":3,
 "code":"200",
 "PageRecordCount":3,
 "RequestId":"5B2E3D79-21A0-4471-8055-ED2AF71F****",
 "SQLTemplateItems":[
  {
   "RowsSent":1,
   "UserHost":testadmin@10.XXX.XX.165,
   "SQLHash":"_455294895%****",
   "RowsExam":0,
   "SourceIP":10.XXX.XX.165,
   "SQLContent":"/* Query from DMS-WEBSQL-0-Qid_1754550112435 by user 142195380638**** */ sele
ct sleep(1) from dual",
   "InstanceId":"rm-my6ypxhaff547****",
   "StartTime":"2025-08-07 15:01:52.488",
   "DBName":"testdb",
   "QueryTime":1
  }
```

`],`

```json
 "PageNumber":1,
 "success":"true",
 "message":"Successful"
}
```

`XML` 格式云原生数据库 I参考

```xml
<TotalRecordCount>3</TotalRecordCount> <code>200</code> <PageRecordCount>3</PageRecordCount> <RequestId>5B2E3D79-21A0-4471-8055-ED2AF71F****</RequestId> <SQLTemplateItems>
 <RowsSent>1</RowsSent>
 <UserHost>testadmin@10.XXX.XX.165</UserHost>
 <SQLHash>_455294895%****</SQLHash>
 <RowsExam>0</RowsExam>
 <SourceIP>10.XXX.XX.165</SourceIP>
 <SQLContent>/* Query from DMS-WEBSQL-0-Qid_1754550112435 by user 142195380638**** */ select s
leep(1) from dual</SQLContent>
 <InstanceId>rm-my6ypxhaff547****</InstanceId>
 <StartTime>2025-08-07 15:01:52.488</StartTime>
 <DBName>testdb</DBName>
 <QueryTime>1</QueryTime>
</SQLTemplateItems> <PageNumber>1</PageNumber> <success>true</success> <message>Successful</message>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |
| 404 | InvalidDB.NotFound | InvalidDB.NotFound | Specified db does not exist or DB status does not support this operation. |
| 404 | InvalidEngine.NotFou nd | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
| 400 | InvalidTask.NotFoun d | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatus | OperationDenied.IncorrectTaskSt atus | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationSt atus | OperationDenied.IncorrectMigrati onStatus | Migration status does not support this operation. |
| 404 | InvalidMigrationID.N otFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.Pay Type | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotAcce ss | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAcces s | No availble cluster. |
| 403 | IncorrectSQLLogActiv eStatus | OperationDenied.SQLLogActiveSt atus | The operation is not permitted due to SQLLogActive status. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidClassicNetwor k.ValueNotSupported | OperationDenied.ClassicNetwork NotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceSy ncMode | OperationDenied.DBInstanceSync Mode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.Res ource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvalid | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.AccountN oFound | OperationDenied.AccountNoFoun d | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUseTy pe.NotSupport | OperationDenied.DBInstanceUseT ypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ _ LIMIT | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.AUDIT | TIME RANGE OVER LIMIT.AUDIT _ _ _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.AUDIT DOWNL _ OAD | TIME RANGE OVER LIMIT.AUDIT _ _ _ _ DOWNLOAD | search time range cannot be longer than 7 days for exporting files. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.SLOW LOG _ | TIME RANGE OVER LIMIT.SLOW _ _ _ _ LOG | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.ERROR LOG _ | TIME RANGE OVER LIMIT.ERROR _ _ _ LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWNLO _ _ AD REQUEST TO OS _ _ _ S | TOO MANY DOWNLOAD REQUES _ _ _ T TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUSTE _ _ R DEACTIVATED _ | IGNITE LOG CLUSTER DEACTIVA _ _ _ TED | backend app is upgrading, please try again later. |
| 400 | IdempotenceParamN otMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSuppo rt | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionNot Found | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkType. NotSupport | ClassicNetworkType.NotSupport | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswitc hId.NotSupported | InvalidVpcIdOrVswitchId.NotSupp orted | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion.N otSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidVSwitchId.Not Supported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.Not Supported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Malfo rmed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotClo udInstanceIp | InvalidCloudInstanceIp.NotFound | The specified cloud instance ip is not exist. |
| 400 | InvalidRetainInstanc e.Format | InvalidRestoreTime.Malformed | The specified retain instance is not valid. |
| 400 | InvalidRestoreTime.F ormat | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 404 | InvalidBackupSetID. NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotFo und | OperationDenied.NotFoundBacku p | The operation is not permitted due to no backup. |
| 403 | InvalidBackupSetIdO rRestoreTime.NotFou nd | OperationDenied.NotFoundBacku pSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
| 403 | IncorrectBackupSetM ethod | OperationDenied.BackupMethod | The operation is not permitted method of backup. |
| 403 | InvalidBackupLogSta tus | OperationDenied.BackupLogStatu s | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Duplic ate | OperationDenied.SecurityIPListDu plicate | The Specified same security IP already exists. |
| 403 | BackupSetDeleteNot Support | OperationDenied.BackupSetDelet eNotSupport | The Specified backup does not support this operation. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 256 _ _ _ 59 | InvalidRegion.ValueNotSupported | The specified parameter "Region" is not valid. |
| 403 | ReadDBInstanceExce eded | QuotaExceeded.ReadonlyDBInsta nceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAIN _ _ _ RDS QUOTA ERROR _ _ | QuotaExceeded.ReadonlyDBInsta nceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAIN _ _ _ RDS TYPE ERROR _ _ | OperationDenied.PrimaryDBInsta nceType | The operation is not permitted due to type of primary instance. |
| 403 | LX RDS BIZ QUERY _ _ _ _ INSTANCE ERROR _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInstanc eId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidLogRetention | InvalidLogRetention.NotSupport | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceede d | QuotaExceeded.Upload | The quota of file exceeds. |
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.Malf ormed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Malfo rmed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malforme d | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinstanc eNetType.ValueNotS upported | InvalidDBinstanceNetType.ValueN otSupport | The specified parameter "DBinstanceNetType" is not valid. |
| 400 | Abs.InstanceUsedTyp e.ValueNotSupported | InvalidDBInstanceType.ValueNotS upport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod. Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersion .Malformed | InvalidEngineVersion.ValueNotSu pport | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfor med | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupRet entionPeriod.Malform ed | InvalidLogBackupRetentionPeriod .Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.DBI nstanceType | IncorrectDBInstanceType.ChildDB InstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSetS tate | OperationDenied.BackupStatus | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupSe tID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | OASBackupSetExtrac tFinished | QuotaExceeded.BackupExtractFin ished | The Specified OAS backup set had extracted finish. |
| 400 | OASExtractTimesExc eeded | QuotaExceeded.OASExtractTimes Exceeded | The Current DB Instance backup set had extracted too many times from OAS today. |
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceStora ge | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Format | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInsta nceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.For mat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |
| 404 | InvalidFileName.NotF ound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotCompleted | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Malf ormed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceNa me.Format | InvalidDBInstanceId.MalFormed | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAsso ciate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintainTi me | InvalidMaintainTime.MalFormed | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfor med | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST N _ _ OT NULL _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERROR _ | PARAMETER ERROR _ | The parameter must not be null. |
| 404 | IntranetNetTypeNotE xists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mis match | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidVPCId.NotFou nd | InvalidVPCId.NotFound | Specified VPC ID is not found. |
| 400 | InvalidVSwitchId.Not Found | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsRd sMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | VPC SYSTEM ERROR _ _ | OperationDenied | VPC system error, please check params. |
| 400 | VPC CLOUD INSTAN _ _ CEIP USED _ | InvalidPrivateIpAddress.Duplicate d | Specified private IP address is duplicated. |
| 400 | Invalid.TargetCloudIn stanceIp | InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceNet workType | InvalidInstanceNetworkType.Valu eNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanceI d.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |
| 400 | InvalidIzNo.NotSuppo rted | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.Swi tchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstance. ID | InvalidDBInstanceName.NotFoun d | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExceed ed | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.Not Found | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | INST NOT BELONG T _ _ _ O USER _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 269 _ _ _ 15 | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | MissingParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LX RDS BIZ INSTAN _ _ _ CE UPGRADE ERROR _ _ | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClass OrdbInstanceStorage .MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | LX BARDS BIZ UPGR _ _ _ ADE INSTANCE ERR _ _ OR | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedTyp e.ValueNotSupported | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UPGR _ _ _ ADE STORAG _ | OperationDenied.DBInstanceStor ageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UPGR _ _ _ ADE STORAGE ERRO _ _ R | OperationDenied.DBInstanceStor ageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 269 _ _ _ 14 | InvaildDBInstanceClassInRegion.N otAvailable | The DBInstanceClass in the Region is not available. |
| 403 | LX RDS BIZ STATUS _ _ _ ERROR _ | OperationDenied.DBInstanceStat us | The operation is not permitted due to instance status. |
| 400 | ILLEGAL ARGUMENT _ | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDataba seUserName.Malfor med | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.For mat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |
| 400 | Abs.SourceDatabase Port.Malformed | InvalidSourceDatabasePort.Malfor med | The specified parameter 'SourceDatabasePort' is not valid. |
| 400 | Abs.ImportDataType. Malformed | InvalidImportDataType.Malforme d | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSupoo rt | OperationDenied.DBInstnceInRegi on | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge. NotSupport | InvalidOrderCharge.NotSupport | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceUse Type | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationID | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | HaStatusNotSupport | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Tag OnDBInstance | QuotaExceeded.TagOnDBInstanc e | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFoun dag-Value is mismatch. |
| 400 | InvalidTag.1.key.Malf ormed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.Malf ormed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.Malf ormed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.Malf ormed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.Malf ormed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value.M alformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |
| 400 | InvalidTag.2.value.M alformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value.M alformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |
| 400 | InvalidTag.4.value.M alformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value.M alformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |
| 400 | TAG KEY ILLEGAL _ _ | Tag.Malformed | The specified parameter Tag is not valid. |
| 400 | TAG VALUE ILLEGAL _ _ | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExist | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNotB eAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |
| 400 | Tag.NoDBInstanceId Exist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBInsta nceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Tag.TooManyTagsFor OneInstance | Tag.TooManyTagsForOneInstance | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtTwo Paramters | Tag.SetTagInfoAtTwoParamters | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWith .aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLong | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLon g | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPara mter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePerio d | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |
| 400 | Abs.InvalidStartTime | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | Abs.InvalidEndTime | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSupp ort | OperationDenied.EnabledSSLNotS upport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.NotFi nished | OperationDenied.RequestNotFinis hed | The specified request not finished. |
| 403 | InvalidRequest.Exists | OperationDenied.RequestExists | The specified request already exists. |
| 400 | Abs.instanceNames. Malformed | InvalidDBInstanceId.QuotaExceed ed | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.Not Support | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |
| 400 | RenewChange.Exist | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |
| 400 | INVITATION CODE BI _ _ Z FAIL _ | InvalidEActionCode.CodeBizNotSu pported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 80 | InvalidEngine.VauleNotSupported | The specified parameter "Engine" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 63 | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 35 | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 36 | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersion .ValueNotSupported | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 62 | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClass. NotFound | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL Miss _ _ _ ingParameter | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 37 | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | InvalidDBInstanceSto rage.ValueNotSuppor ted | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.dbInstanceNetTy pe.ValueNotSupporte d | InvalidDBInstanceNetType.Value NotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIFY F _ _ _ _ AIL | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |
| 400 | QUERY PRICE RESPO _ _ NSE ERROR _ | QueryPriceResonse.Failed | query price response error. |
| 400 | LX CREATE ORDER _ _ _ FAILED | CreateOrder.Failed | Create order failed. |
| 404 | InvalidRegion.NotFou nd | InvalidRegionId.NotFound | The provided RegionId does not exist. |
| 404 | INQUERY ORDER FE _ _ E FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.NotF ound | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ _ NotFound | InvalidRegionId.NotFound | The provided RegionId is not found. |

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 38 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | Abs.dbInstanceDescr iption.Malformed | InvalidDBInstanceDescription.Mal formed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 44 | InvalidEngineVersionInRegion.Not Available | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 45 | InvalidEngineVersionInRegion.Not Available | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 261 _ _ _ 75 | InvaildEngineInRegion.NotAvailab le | The engine type in this region is not available. |
| 403 | InvalidUserRegionPri vilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COMM _ _ _ ODITY COUNT EXCE _ _ EDED LIMIT _ | QuotaExceeded.CreateInstance | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID O _ _ _ RDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |
| 403 | GET COMMODITY FA _ _ ILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN 1 _ _ 00 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge. NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |
| 400 | Abs.MissingOwnerId OrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParamet er | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceCo nnType.Format | InvalidDBInstanceConnType.Form at | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPList. Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLoc ation | InvalidBackupLocation.Malformed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.ValueN otSupported | The specified SQLCollectorStatus value not support. |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSqlLog.Malfor med | InvalidSQLCollectorStatus.Malfor med | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Start Diagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 400 | InvalidDBInstanceDe scription.Format | InvalidDBInstanceDescription.Mal formed | The specified parameter "DBInstanceDescription" is not valid. |
| 400 | InvalidConnectionStri ng.Format | InvalidConnectionString.Malforme d | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName.F ormat | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStatus .ValueNotSupported | InvalidBackupStatus.ValueNotSup port | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.ValueN otSupported | InvalidBackupMode.ValueNotSup port | The specified parameter "BackupMode" is not valid. |
| 400 | Abs.InvalidDescriptio n.Malformed | InvalidDBDescription.Malformed | The specified parameter "DBDescription" is not valid. |
| 400 | Abs.backupTime.Val ueNotSupported | InvalidPreferredBackupTime.Malf ormed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod.Ma lformed | InvalidPreferredBackupPeriod.Mal formed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountName. Format | InvalidAccountName.Malformed | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountName. Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountName. Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPassw ord.Format | InvalidAccountPassword.Malform ed | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExceed ed | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitExc eeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.For mat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionMo de | InvalidConnectionMode.ValueNot Supported | The specified parameter "ConnectionMode" is not valid. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccountPrivile ge.Malformed | InvalidAccountPrivilege.ValueNot Support | The specified "AccountPrivilege" is not valid. |
| 400 | IncorrectEngineVersi on | InvaildEngineInRegion.ValueNotS upported | The engine is not supported in the region. |
| 400 | InvalidDBName.Form at | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Dupli cate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSetN ame.Format | InvalidCharsetName.ValueNotSup port | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescription .Format | InvalidDBDescription.Malformed | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.Forbi d | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |
| 400 | InvalidUserType.NotS upport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime.F ormat | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |
| 400 | InvalidBackupMetho d.Format | InvalidBackupMethod.ValueNotSu pport | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog.Ma lformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.For mat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.Form at | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecordsPe rPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malfor med | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod.M alformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malforme d | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malforme d | InvalidPerformanceKey.Malforme d | The specified parameter "Key" is not valid. |
| 400 | InvalidQueryKeyword .NotSupport | InvalidQueryKeyword.Malformed | the query key contains exception character. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime.Malf ormed | The end time must be greater than the start time. |
| 400 | InvalidParameter.Res ourceOwnerAccount | InvalidParameter.ResourceOwner Account | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.Forma t | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenByS ubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |
| 403 | RAM.ApiNotSupporte d | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |
| 403 | RISK CONTROL RES _ _ ULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotSu pport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanceL ockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |
| 403 | IncorrectDBInstance State | OperationDenied.DBInstanceStat us | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstance Type | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNotS upport | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceNot Support | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNotS upport | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstance Engine | OperationDenied.DBInstanceEngi ne | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstance NetType | OperationDenied.DBInstanceNetT ype | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstance ConnType | OperationDenied.PublicConnectio nExists | The specified public connection already existed. |
| 403 | InsufficientResource Capacity | OperationDenied | The resource is out of usage. |
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSupp ort | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstance | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |

| P I | olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectGuardDBIns tanceVersion | OperationDenied.GuardDBInstanc eLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBIn stanceState | OperationDenied.MasterDBInstan ceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountStat us | OperationDenied.AccountStatus | The operation is not permitted due to status of account. |
| 403 | IncorrectAccountTyp e | OperationDenied.AccountType | The operation is not permitted due to type of account. |
| 403 | ConcurrentTaskExce eded | OperationDenied.TaskExceeded | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstance AccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccount PrivilegeCount | OperationDenied.DBNameAndAcc ountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWrong | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod.V alueNotSupported | InvalidBackupMethod.ValueNotSu pport | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Val ueNotSupported | InvalidBackupType.ValueNotSupp ort | The specified parameter "BackupType" is not valid. |
| 404 | INSUFFICIENT BALAN _ CE | InsufficientBalance | Your account does not have enough balance. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL INSU _ _ _ FFICIENT BALANCE _ | InsufficientBalance | Your account does not have enough balance. |
| 400 | INSTANCE PRODUCE _ FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceNa me.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFound | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance.No tFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | RAM.InstanceNotFou nd | Forbidden.InstanceNotFound | The specified instance is not found. |
| 404 | InvalidConnectionStri ng.Duplicate | InvalidConnectionStringPrefix.Du plicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTypeE xists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionStri ngOrPort.Duplicate | InvalidConnectionString.Duplicate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionStri ng.NotFound | InvalidConnectionString.NotFound | The specified connection string or network type is not found. |
| 404 | ConnectionStringLen gthExceeded | ConnectionStringLengthExceeded | The specified connection string is too long. |
| 404 | InvalidSecurityIPList. QuotaExceeded | InvalidSecurityIPListLength.Malfor med | The security IP address is not in the available range or occupied. |
| 404 | InvalidSecurityIPList. NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPList. Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceNe tType.NotFound | InvalidDBInstanceNetType.NotFo und | The specified instance network type is not found. |
| 403 | ChildDBInstanceExist s | OperationDenied.ChildDBInstance Exists | The specified instance had child instance. |
| 404 | GuardInstance.Exist | InvalidGuardInstanceId.Exist | The guard instance has exist. |
| 404 | InvalidDBInstanceCla ss.NotFound | InvalidDBInstanceClass.NotFound | The specified instance class is not found. |
| 404 | InvalidUser.NotFoun d | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPermi ssion.NotFound | InvalidOperatorPermission.NotFo und | The permission provided does not exist. |
| 404 | InvalidDBName.NotF ound | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |
| 404 | InvalidAccountName. NotFound | InvalidAccountName.NotFound | The specified account is not found. |
| 500 | Invalid.Request | InternalError | The request processing has failed due to some unknown error, exception or failure. |

| P I | olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
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

### DescribeSQLLogRecordsV4

调用DescribeSQLLogRecordsV4接口查询PolarDB集群的审计日志明细。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | String | System | 是 | DescribeSQLLogRecordsV4 | 系统规定参数。取值： DescribeSQLLogRecordsV4 |
| InstanceID | String | Query | 是 | pc-nj2s8v32e6hrb**** | 实例ID。 |
| StartTime | String | Query | 是 | 2025-06-21T15:00:00Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2025-06-21T16:00:00Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EngineNam e | String | Query | 否 | PolarDB MySQL _ | 实例名称。 |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SQLRecordItem s | Array | SQL | 审计日志明细列表。 |
| -DBName | String | test db _ | 数据库名称。 |
| -AccountName | String | test acc _ | 账号名称。 |
| -SourceIP | String | 47.100.XX.XX | 源端IP。 |
| -SourcePort | String | 5432 | 源端口号。 |
| -DBNodeRole | String | master | 实例角色。 |
| -SQLText | String | select id,name from tb table; _ | SQL语句。 |
| - ExecuteProcessI D | String | 12345 | 进程号。 |
| - SqlTotalCostTim eFloat | Long | 10 | SQL执行的绝对时间（ms）。 |
| -ScanRows | Long | 1 | 扫描行数。 |
| -ReturnRows | Long | 1 | 返回行数。 |

| olarDB MySQL集 | 群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -UpdateRows | Long | 1 | 更新行数。 |
| -ExecuteTime | String | 2025-06- 21T15:00:00Z | 执行时间，格式为UTC时间： yyyy-MM- ddTHH:mm:ssZ 。 |
| - ExecuteThreadI d | String | 123456 | 线程号。 |
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| PageNumber | Integer | 1 | 页码。 |

| yyyy-MM- |  |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSQLLogRecordsV4 &InstanceID=pc-nj2s8v32e6hrb**** &StartTime=2025-06-21T15:00:00Z &EndTime=2025-06-21T16:00:00Z
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":"",
 "PageRecordCount":"",
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "SQLRecordItems":[
  {
   "SqlTotalCostTimeFloat":10,
   "ExecuteThreadId":"123456",
   "ExecuteTime":"2025-06-21T15:00:00Z",
   "DBNodeRole":"master",
   "ExecuteProcessID":"12345",
   "SourcePort":"5432",
   "ReturnRows":1,
   "SQLText":"select id,name from tb_table;",
   "UpdateRows":1,
   "SourceIP":"47.100.XX.XX",
   "ScanRows":1,
   "DBName":"test_db",
   "AccountName":"test_acc"
  }
```

`],`

```json
 "PageNumber":1
}
```

`XML` 格式

```xml
<TotalRecordCount /> <PageRecordCount /> <RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <SQLRecordItems>
 <SqlTotalCostTimeFloat>10</SqlTotalCostTimeFloat>
 <ExecuteThreadId>123456</ExecuteThreadId>
 <ExecuteTime>2025-06-21T15:00:00Z</ExecuteTime>
 <DBNodeRole>master</DBNodeRole>
 <ExecuteProcessID>12345</ExecuteProcessID>
 <SourcePort>5432</SourcePort>
 <ReturnRows>1</ReturnRows>
 <SQLText>select id,name from tb_table;</SQLText>
 <UpdateRows>1</UpdateRows>
 <SourceIP>47.100.XX.XX</SourceIP>
 <ScanRows>1</ScanRows>
 <DBName>test_db</DBName>
 <AccountName>test_acc</AccountName>
</SQLRecordItems> <PageNumber>1</PageNumber>
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | CallEcsApi.Failure | CallEcsApi.Failure | call ecs api failure. |
| 404 | InvalidDB.NotFound | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |

| 参考 | 集群版开发指南 |  | 云原生数据库 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |

| 404 | InvalidEngine.NotFou nd | InvalidEngine.NotFound | Specified engine does not exist or engine version does not support this operation. |
|---|---|---|---|
| 400 | InvalidTask.NotFoun d | InvalidTaskId.NotFound | The "ImportId" is not found. |
| 403 | IncorrectTaskStatus | OperationDenied.IncorrectTaskSt atus | The operation is not permitted due to status of import. |
| 403 | IncorrectMigrationSt atus | OperationDenied.IncorrectMigrati onStatus | Migration status does not support this operation. |
| 404 | InvalidMigrationID.N otFound | InvalidMigrationID.NotFound | The specified migration record does not exist. |
| 403 | OperationDenied.Pay Type | OperationDenied.PayType | The operation is not permitted due to pay type of instance. |
| 403 | GetvSwitch.Failure | OperationDenied.VSwitchNotAcce ss | No availble vSwitch. |
| 403 | GetCluster.Failure | OperationDenied.ClusterNotAcces s | No availble cluster. |
| 403 | IncorrectSQLLogActiv eStatus | OperationDenied.SQLLogActiveSt atus | The operation is not permitted due to SQLLogActive status. |
| 403 | InvalidClassicNetwor k.ValueNotSupported | OperationDenied.ClassicNetwork NotSupported | The operation is not permitted due to create classicNetwork instance. |
| 403 | InvalidDBInstanceSy ncMode | OperationDenied.DBInstanceSync Mode | The operation is not permitted due to instance sync mode. |
| 403 | OperationDenied.Res ource | OperationDenied.Resource | The resource is out of usage. |
| 403 | Forbidden.BidInvalid | OperationDenied.BidInvalid | The operation is not permitted due to ownerId or resourceOwnerId. |
| 403 | Forbidden.AccountN oFound | OperationDenied.AccountNoFoun d | The specified ownerId or resourceOwnerId is not found. |
| 403 | InvalidInstanceUseTy pe.NotSupport | OperationDenied.DBInstanceUseT ypeNotSupport | The specified dbinstance use type is not found. |
| 400 | TIME RANGE OVER _ _ _ LIMIT | TIME RANGE OVER LIMIT _ _ _ | search time range cannot be longer than three days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.AUDIT | TIME RANGE OVER LIMIT.AUDIT _ _ _ | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.AUDIT DOWNL _ OAD | TIME RANGE OVER LIMIT.AUDIT _ _ _ _ DOWNLOAD | search time range cannot be longer than 7 days for exporting files. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TIME RANGE OVER _ _ _ LIMIT.SLOW LOG _ | TIME RANGE OVER LIMIT.SLOW _ _ _ _ LOG | search time range cannot be longer than 7 days. |
| 400 | TIME RANGE OVER _ _ _ LIMIT.ERROR LOG _ | TIME RANGE OVER LIMIT.ERROR _ _ _ LOG _ | search time range cannot be longer than 7 days. |
| 400 | TOO MANY DOWNLO _ _ AD REQUEST TO OS _ _ _ S | TOO MANY DOWNLOAD REQUES _ _ _ T TO OSS _ _ | too many download request is made in 30 minutes, please wait pre request complete. |
| 400 | IGNITE LOG CLUSTE _ _ R DEACTIVATED _ | IGNITE LOG CLUSTER DEACTIVA _ _ _ TED | backend app is upgrading, please try again later. |
| 400 | IdempotenceParamN otMatch | IdempotenceParamNotMatch | The specified parameter not match. |
| 400 | DefaultVpc.NotSuppo rt | DefaultVpc.NotSupport | The default VPC create is not supported. |
| 400 | Forbidden.RegionNot Found | Forbidden.RegionNotFound | The provided RegionId does not exist. |
| 400 | ClassicNetworkType. NotSupport | ClassicNetworkType.NotSupport | The Classic instance network create is not supported. |
| 400 | InvalidVpcIdOrVswitc hId.NotSupported | InvalidVpcIdOrVswitchId.NotSupp orted | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVpcIdRegion.N otSupported | InvalidVpcId.NotSupported | The specified vpcId or vSwitchId is not supported. |
| 400 | InvalidVSwitchId.Not Supported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidVSwitchId.Not Supported | InvalidVSwitchId.NotSupported | The specified VPC zone is not supported. |
| 400 | InvalidQuantity.Malfo rmed | InvalidQuantity.NotSupported | The specified instance quantity is not supported. |
| 400 | TargetSubnet.NotClo udInstanceIp | InvalidCloudInstanceIp.NotFound | The specified cloud instance ip is not exist. |
| 400 | InvalidRestoreTime.F ormat | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 400 | InvalidRestoreTime.F ormat | InvalidRestoreTime.Malformed | The specified parameter "RestoreTime" is not valid. |
| 404 | InvalidBackupSetID. NotFound | InvalidBackupId.NotFound | The BackupId provided does not exist. |
| 403 | InvalidBackup.NotFo und | OperationDenied.NotFoundBacku p | The operation is not permitted due to no backup. |
| 403 | InvalidBackupSetIdO rRestoreTime.NotFou nd | OperationDenied.NotFoundBacku pSetIdOrRestoreTime | The operation is not permitted due to no backupSetId or restoreTime. |
| 403 | IncorrectBackupSetM ethod | OperationDenied.BackupMethod | The operation is not permitted method of backup. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | InvalidBackupLogSta tus | OperationDenied.BackupLogStatu s | The Current backup log enable status does not support this operation. |
| 403 | SecurityIPList.Duplic ate | OperationDenied.SecurityIPListDu plicate | The Specified same security IP already exists. |
| 403 | BackupSetDeleteNot Support | OperationDenied.BackupSetDelet eNotSupport | The Specified backup does not support this operation. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 256 _ _ _ 59 | InvalidRegion.ValueNotSupported | The specified parameter "Region" is not valid. |
| 403 | LX RORDS BIZ MAIN _ _ _ RDS QUOTA ERROR _ _ | QuotaExceeded.ReadonlyDBInsta nceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAIN _ _ _ RDS QUOTA ERROR _ _ | QuotaExceeded.ReadonlyDBInsta nceCount | The quota of primary instance mounted read only instance. |
| 403 | LX RORDS BIZ MAIN _ _ _ RDS TYPE ERROR _ _ | OperationDenied.PrimaryDBInsta nceType | The operation is not permitted due to type of primary instance. |
| 404 | InvalidDBInstance.No tFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | IZ INVALID _ | InvalidZoneId.NotFound | The provided ZoneId does not exist. |
| 404 | Abs.InvalidDBInstanc eId.Malformed | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | InvalidLogRetention | InvalidLogRetention.NotSupport | The specified log retention is not valid,The current instance type does not support this operation. |
| 403 | UploadLimitExceede d | QuotaExceeded.Upload | The quota of file exceeds. |
| 403 | -113 | ChargeTypeViolation | The operation is not permitted due to charge type of the instance. |
| 403 | LX SYSTEM _ | System.Error | The operation is error for current isntance. |
| 403 | InvalidStartTime.Malf ormed | InvalidStartTime.Format | The specified parameter "StartTime" is not valid. |
| 403 | InvalidEndTime.Malfo rmed | InvalidEndTime.Format | The specified parameter "EndTime" is not valid. |
| 400 | Abs.Engine.Malforme d | InvalidEngine.Malformed | The specified parameter "Engine" is not valid. |
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 400 | Abs.InvalidDBinstanc eNetType.ValueNotS upported | InvalidDBinstanceNetType.ValueN otSupport | The specified parameter "DBinstanceNetType" is not valid. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InstanceUsedTyp e.ValueNotSupported | InvalidDBInstanceType.ValueNotS upport | The specified parameter"DBInstanceType" is not valid. |
| 400 | InvalidPageSize | InvalidPageSize | Specified parameter pageSize is not valid. |
| 400 | InvalidMaxRecordsPe rPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidExpirePeriod. Malformed | InvalidExpirePeriod.Malformed | The specified parameter "ExpirePeriod" is not valid. |
| 400 | InvalidEngineVersion .Malformed | InvalidEngineVersion.ValueNotSu pport | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngine.Malfor med | InvalidEngine.ValueNotSupport | The specified parameter "Engine" is not valid. |
| 400 | InvalidLogBackupRet entionPeriod.Malform ed | InvalidLogBackupRetentionPeriod .Malformed | The Specified LogBackupRetentionPeriod is not valid. |
| 400 | OperationDenied.DBI nstanceType | IncorrectDBInstanceType.ChildDB InstanceNotSupport | The operation is not permitted due to instance type. |
| 403 | IncorrectBackupSetS tate | OperationDenied.BackupStatus | The operation is not permitted due to status of instancebackup. |
| 404 | InvalidOASBackupSe tID.NotFound | InvalidBackupID.NotFound | The BackupID provided does not exist. |
| 404 | OASBackupSetExtrac tFinished | QuotaExceeded.BackupExtractFin ished | The Specified OAS backup set had extracted finish. |
| 400 | OASExtractTimesExc eeded | QuotaExceeded.OASExtractTimes Exceeded | The Current DB Instance backup set had extracted too many times from OAS today. |
| 403 | DBSizeExceeded | QuotaExceeded.DBInstanceStora ge | The quota of instance storage exceeds. |
| 400 | InvalidDBInfo.Format | InvalidDBInfo.Malformed | The specified parameter "DBInfo" is not valid or db not exist. |
| 403 | NotValidRegion. | OperationDenied.Region | The operation is not permitted due to different region. |
| 403 | InvalidTargetDBInsta nceName.Format | OperationDenied.DBInstanceId | The operation is not permitted due to DBInstanceId and SourceDBInstanceId is same. |
| 400 | InvalidFileName.For mat | InvalidFileName.Malformed | The specified parameter "FileName" is not valid. |
| 404 | InvalidFileName.NotF ound | InvalidFileName.NotFound | The FileName provided does not exist. |
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | FileNotUploaded | InvalidFileName.NotCompleted | The specified "FileName" is not completed . |
| 400 | FileNotAvailable | InvalidFileName.NotAvailable | The specified "FileName" is not Available . |
| 403 | FileSizeExceeded | QuotaExceeded.FileSize | The quota of file size exceeds. |
| 403 | Abs.IsLockTable.Malf ormed | InvalidIsLockTable.Malformed | The specified parameter "IsLockTable" is not valid. |
| 400 | InvalidDBInstanceNa me.Format | InvalidDBInstanceId.MalFormed | The specified parameter "DBInstanceId" is not valid. |
| 400 | ParameterLeastAsso ciate | ParameterLeastAssociate | Must input at least one optional parameter. |
| 400 | Abs.InvalidMaintainTi me | InvalidMaintainTime.MalFormed | The specified parameter "MaintainTime" is not valid. |
| 400 | InvalidPeriod.Malfor med | InvalidPeriod.Malformed | The Specified parameter "Period" is not valid. |
| 400 | PARAMETER MUST N _ _ OT NULL _ | PARAMETER MUST NOT NULL _ _ _ | The parameter must not be null. |
| 400 | PARAMETER ERROR _ | PARAMETER ERROR _ | The parameter must not be null. |
| 404 | IntranetNetTypeNotE xists | IntranetNetTypeNotExists | Current DB instance network type does not support this operation. |
| 400 | InvalidVSwitchId.Mis match | InvalidVSwitchId.Mismatch | Specified instance and vSwitch are not in the same zone. |
| 404 | InvalidVPCId.NotFou nd | InvalidVPCId.NotFound | Specified VPC ID is not found. |
| 400 | InvalidVSwitchId.Not Found | InvalidVSwitchId.NotFound | Specified vSwitch is not found in specified VPC. |
| 400 | VpcIzNoNotEqualsRd sMultIzNo | VpcIzNoNotEqualsRdsMultIzNo | Specified VPC IzNo does not equal to RDS IzNo. |
| 403 | InsufficientResource Capacity | OperationDenied | The resource is out of usage. |
| 400 | VPC CLOUD INSTAN _ _ CEIP USED _ | InvalidPrivateIpAddress.Duplicate d | Specified private IP address is duplicated. |
| 400 | Invalid.TargetCloudIn stanceIp | InvalidPrivateIpAddress.Mismatch | Specified private IP address is not in the CIDR block of virtual switch. |
| 400 | IncorrecttVpcId | IncorrectVpcId.Mismatch | The specified parameter "VpcId " is not valid. |
| 400 | IncorrectInstanceNet workType | InvalidInstanceNetworkType.Valu eNotSupported | The specified parameter "InstanceNetworkType" is not valid. |
| 403 | InvalidCloudInstanceI d.Duplicated | OperationDenied.SwitchToVPC | Specified instance cannot be switched to VPC. |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidIzNo.NotSuppo rted | InvalidIzNo.NotSupported | Specified VCP zone is not supported. |
| 403 | OperationDenied.Swi tchToVPC | OperationDenied.Switch | Specified instance cannot be switched to VPC. |
| 404 | InvalidCloudInstance. ID | InvalidDBInstanceName.NotFoun d | The DBInstanceId provided does not exist. |
| 403 | SlaveLagExceeded | Exceeded.SlaveLag | The slave lag exceeds. |
| 403 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 403 | BackupTimesExceed ed | Exceeded.BackupTimes | The backup times exceeds. |
| 404 | Abs.dbInstanceId.Not Found | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 404 | INST NOT BELONG T _ _ _ O USER _ | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist. |
| 400 | InvalidDBInstanceSto rage.ValueNotSuppor ted | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | Abs.MissingOwnerId OrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | LX RDS BIZ INSTAN _ _ _ CE UPGRADE ERROR _ _ | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | Abs.dbInstanceClass OrdbInstanceStorage .MissParameter | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 403 | ReadDBInstanceNotS upport | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 400 | Abs.InstanceUsedTyp e.ValueNotSupported | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | LX BARDS BIZ UPGR _ _ _ ADE STORAGE ERRO _ _ R | OperationDenied.DBInstanceStor ageReduce | The operation is not permitted due to reduce storage. |
| 403 | LX BARDS BIZ UPGR _ _ _ ADE STORAGE ERRO _ _ R | OperationDenied.DBInstanceStor ageReduce | The operation is not permitted due to reduce storage. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 269 _ _ _ 14 | InvaildDBInstanceClassInRegion.N otAvailable | The DBInstanceClass in the Region is not available. |
| 403 | IncorrectDBInstance State | OperationDenied.DBInstanceStat us | The operation is not permitted due to status of instance. |

| P I | olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ILLEGAL ARGUMENT _ | MissingParameter | The input parameters "DBInstanceClass" and "DBInstanceStorage" all blank or no change. |
| 400 | InvalidSourceDataba seUserName.Malfor med | InvalidDBInfo.Format | The specified parameter "SourceDatabaseUserName" is not valid. |
| 400 | InvalidQueryTime.For mat | InvalidQueryTime.Format | he specified parameter "QueryTime" is not valid. |
| 400 | Abs.SourceDatabase Port.Malformed | InvalidSourceDatabasePort.Malfor med | The specified parameter 'SourceDatabasePort' is not valid. |
| 400 | Abs.ImportDataType. Malformed | InvalidImportDataType.Malforme d | The specified parameter 'ImportDataType' is not valid. |
| 400 | ClusterDRCNotSupoo rt | OperationDenied.DBInstnceInRegi on | The operation is not permitted due to DBInstance in the region. |
| 404 | InvalidOrderCharge. NotSupport | InvalidOrderCharge.NotSupport | The specified order charge does not support in RDS. |
| 404 | IncorrectInstanceUse Type | InvalidDBInstanceIdUseType | InvalidDBInstanceIdUseType. |
| 403 | IncorrectMigrationID | InvalidImportId.ImportIdvalue | The operation is not permitted due to ImportId value. |
| 403 | InvalidSwitchType | InvalidSwitchType.Malformed | The specified parameter InvalidSwitchType is not valid. |
| 403 | HaStatusNotSupport | OperationDenied.HaStatus | The operation is not permitted due to hastatus no supported. |
| 404 | QuotaExceeded.Tag OnDBInstance | QuotaExceeded.TagOnDBInstanc e | The quota of tag on DBInstance exceeds. |
| 400 | Tag.Mismatch | Tag.Mismatch | Tag-Key and InvalidDBInstanceName.NotFoun dag-Value is mismatch. |
| 400 | InvalidTag.1.key.Malf ormed | InvalidTag.1.key.Malformed | The specified parameter 'Tag.1.key' is not valid. |
| 400 | InvalidTag.2.key.Malf ormed | InvalidTag.2.key.Malformed | The specified parameter 'Tag.2.key' is not valid. |
| 400 | InvalidTag.3.key.Malf ormed | InvalidTag.3.key.Malformed | The specified parameter 'Tag.3.key' is not valid. |
| 400 | InvalidTag.4.key.Malf ormed | InvalidTag.4.key.Malformed | The specified parameter 'Tag.4.key' is not valid. |
| 400 | InvalidTag.5.key.Malf ormed | InvalidTag.5.key.Malformed | The specified parameter 'Tag.5.key' is not valid. |
| 400 | InvalidTag.1.value.M alformed | InvalidTag.1.value.Malformed | The specified parameter 'Tag.1.value' is not valid. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTag.2.value.M alformed | InvalidTag.2.value.Malformed | The specified parameter 'Tag.2.value' is not valid. |
| 400 | InvalidTag.3.value.M alformed | InvalidTag.3.value.Malformed | The specified parameter 'Tag.3.value' is not valid. |
| 400 | InvalidTag.4.value.M alformed | InvalidTag.4.value.Malformed | The specified parameter 'Tag.4.value' is not valid. |
| 400 | InvalidTag.5.value.M alformed | InvalidTag.5.value.Malformed | The specified parameter 'Tag.5.value' is not valid. |
| 400 | TAG VALUE ILLEGAL _ _ | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | TAG VALUE ILLEGAL _ _ | Tag.Malformed | The specified parameter Value is not valid. |
| 400 | Tag.NoRegionIdExist | Tag.NoRegionIdExist | the region Id can not be blank. |
| 400 | Tag.NoTagInfoExist | Tag.NoTagInfoExist | all the tags and tagN parameters is null. |
| 400 | Tag.TagKeyCanNotB eAll | Tag.TagKeyCanNotBeAll | tag key can not be all. |
| 400 | Tag.TagKeyDuplex | Tag.TagKeyDuplex | tag key must be sole in one operation. |
| 400 | Tag.NoDBInstanceId Exist | Tag.NoDBInstanceIdExist | the dbinstance Id can not be blank. |
| 400 | Tag.TooManyDBInsta nceIds | Tag.TooManyDBInstanceIds | the dbinstance Ids is more than 30. |
| 400 | Tag.TooManyTagsFor OneInstance | Tag.TooManyTagsForOneInstance | total 10 tags can be added to one resource. |
| 400 | Tag.SetTagInfoAtTwo Paramters | Tag.SetTagInfoAtTwoParamters | only tags or tagN parameter could be setted. |
| 400 | Tag.Allow5TagInfos | Tag.Allow5TagInfos | only 5 tags allowed in one operation. |
| 400 | Tag.TagKeyIsBlank | Tag.TagKeyIsBlank | tag key can not be blank. |
| 400 | Tag.TagKeyStartWith .aliyun | Tag.TagKeyStartWith.aliyun | tag key and value can not be started with aliyun. |
| 400 | Tag.TagKeyTooLong | Tag.TagKeyTooLong | the max tag key's length is 64. |
| 400 | Tag.TagValueTooLon g | Tag.TagValueTooLong | the max tag value's length is 128. |
| 400 | Tag.InvalidTagsPara mter | Tag.InvalidTagsParamter | tags paramter is invalid. |
| 400 | Abs.InvalidTimePerio d | OperationDenied.TimePeriod | The specified parameter "TimePeriod" is not valid. |
| 400 | InvalidStartTime.For mat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidEndTime.Form at | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 403 | EnabledSSLNotSupp ort | OperationDenied.EnabledSSLNotS upport | The specified parameter "EnabledSSL" is not valid. |
| 403 | InvalidRequest.NotFi nished | OperationDenied.RequestNotFinis hed | The specified request not finished. |
| 403 | InvalidRequest.Exists | OperationDenied.RequestExists | The specified request already exists. |
| 400 | Abs.instanceNames. Malformed | InvalidDBInstanceId.QuotaExceed ed | The quota of instance ID exceeded. |
| 400 | InvalidOrderTask.Not Support | InvalidOrderTask.NotSupport | The Current InstanceId exist Order Task in RDS. |
| 400 | RenewChange.Exist | RenewChange.Exist | The Current InstanceId exist renewChange order in RDS. |
| 400 | INVITATION CODE BI _ _ Z FAIL _ | InvalidEActionCode.CodeBizNotSu pported | The specified action code biz is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 80 | InvalidEngine.VauleNotSupported | The specified parameter "Engine" is not valid. |
| 400 | InvalidEngineVersion .ValueNotSupported | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 35 | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 36 | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | InvalidEngineVersion .ValueNotSupported | InvalidEngineVersion.ValueNotSu pported | The specified parameter "EngineVersion" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL Miss _ _ _ ingParameter | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | Abs.dbInstanceClass. NotFound | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL Miss _ _ _ ingParameter | InvalidDBInstanceClass.ValueNot Supported | The specified parameter "DBInstanceClass" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 37 | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |
| 400 | InvalidDBInstanceSto rage.ValueNotSuppor ted | InvalidDBInstanceStorage.ValueN otSupported | The specified parameter "DBInstanceStorage" is not valid. |

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.dbInstanceNetTy pe.ValueNotSupporte d | InvalidDBInstanceNetType.Value NotSupported | The specified parameter "InvalidDBInstanceNetType" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL _ _ | FUWU BIZ COMMODITY VERIFY F _ _ _ _ AIL | Oops, unable to complete your payment. The reason for this error may be due to one of the following: 1. Your bank account funds are insufficient. 2. Your account is not yet verified. 3. You have already exceeded the maximum limit of RDS instances. |
| 400 | QUERY PRICE RESPO _ _ NSE ERROR _ | QueryPriceResonse.Failed | query price response error. |
| 400 | INSTANCE PRODUCE _ FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 38 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 404 | INQUERY ORDER FE _ _ E FAILED _ | QueryPrice.Failed | QueryPrice Failed. |
| 404 | InvalidRegionId.NotF ound | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | InvalidRegion Zone _ _ NotFound | InvalidRegionId.NotFound | The provided RegionId is not found. |
| 404 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 38 | InvalidRegionId.NotFound | The RegionId provided does not exist. |
| 400 | InvalidDBInstanceDe scription.Format | InvalidDBInstanceDescription.Mal formed | The specified parameter "DBInstanceDescription" is not valid. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 45 | InvalidEngineVersionInRegion.Not Available | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 260 _ _ _ 45 | InvalidEngineVersionInRegion.Not Available | The EngineVersion in the Region is not available. |
| 403 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL 261 _ _ _ 75 | InvaildEngineInRegion.NotAvailab le | The engine type in this region is not available. |
| 403 | InvalidUserRegionPri vilege.Malformed | RegionUnauthorized | There is no authority to create instance in the specified region. |
| 403 | LX USER BUY COMM _ _ _ ODITY COUNT EXCE _ _ EDED LIMIT _ | QuotaExceeded.CreateInstance | The quota of create instance exceeds. |
| 403 | INST HAS UNPAID O _ _ _ RDER | INST HAS UNPAID ORDER _ _ _ | The instanceId has unpaid order. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | GET COMMODITY FA _ _ ILED | COMMODITY.FAILED | The commodity is error. |
| 403 | MONEY LESSTHAN 1 _ _ 00 | MoneyLessThan100 | The Account Monet less Than 100. |
| 403 | InvalidOrderCharge. NotPay | InvalidOrderCharge.NotPay | The specified parameter OrderCharge is not pay. |
| 400 | Abs.MissingOwnerId OrOwnerAccount | MissingParameter | The input parameter "OwnerId" or "OwnerAccount" that is mandatory for processing this request is not supplied. |
| 400 | UnsupportedParamet er | UnsupportedParameter | Unsupported parameter. |
| 400 | InvalidDBInstanceCo nnType.Format | InvalidDBInstanceConnType.Form at | The specified instance connection type is not valid. |
| 400 | InvalidSecurityIPList. Format | InvalidSecurityIps.MalFormed | The specified parameter "SecurityIps" is not valid. |
| 400 | InvalidBackupSetLoc ation | InvalidBackupLocation.Malformed | The specified parameter "BackupLocation" is not valid. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Malformed | The specified parameter "Parameters" is not valid. |
| 400 | InvalidConfigValue | InvalidSQLCollectorStatus.ValueN otSupported | The specified SQLCollectorStatus value not support. |
| 400 | InvalidSqlLog.Malfor med | InvalidSQLCollectorStatus.Malfor med | The specified parameter "SQLCollectorStatus" is not valid. |
| 400 | QuotaExceeded.Start Diagnose | QuotaExceeded.StartDiagnose | The quota of start diagnose exceeds now,try again later. |
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 400 | InvalidDBInstanceDe scription.Format | InvalidDBInstanceDescription.Mal formed | The specified parameter "DBInstanceDescription" is not valid. |
| 400 | InvalidConnectionStri ng.Format | InvalidConnectionString.Malforme d | The specified parameter "ConnectionStringPrefix" is not valid. |
| 400 | InvalidGroupName.F ormat | InvalidGroupName.Malformed | The specified parameter "DBInstanceIPArrayName" is not valid. |
| 400 | Abs.backupSetStatus .ValueNotSupported | InvalidBackupStatus.ValueNotSup port | The specified parameter "BackupStatus" is not valid. |
| 400 | Abs.jobMode.ValueN otSupported | InvalidBackupMode.ValueNotSup port | The specified parameter "BackupMode" is not valid. |
| 400 | InvalidDBDescription .Format | InvalidDBDescription.Malformed | The specified parameter "DBDescription" is not valid. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.backupTime.Val ueNotSupported | InvalidPreferredBackupTime.Malf ormed | The specified parameter "PreferredBackupTime" is not valid. |
| 400 | Abs.backupPeriod.Ma lformed | InvalidPreferredBackupPeriod.Mal formed | The specified parameter "PreferredBackupPeriod" is not valid. |
| 400 | InvalidAccountName. Format | InvalidAccountName.Malformed | The specified parameter "AccountName" is not valid. |
| 400 | InvalidAccountName. Forbid | InvalidAccountName.keyword | The specified parameter "AccountName" is a keyword. |
| 400 | InvalidAccountName. Duplicate | InvalidAccountName.Duplicate | Invalid "AccountName" specified, duplicated. |
| 400 | InvalidAccountPassw ord.Format | InvalidAccountPassword.Malform ed | The specified parameter "AccountPassword" is not valid. |
| 400 | AccountLimitExceed ed | QuotaExceeded.AccountName | Account limit exceeded. |
| 400 | SwitchTimesLimitExc eeded | QuotaExceeded.SwitchTime | SwitchTimes limit exceeded. |
| 400 | InvalidTDEstatus.For mat | InvalidTDEstatus.Format | The specified TDEStatus is not valid. |
| 400 | InvalidConnectionMo de | InvalidConnectionMode.ValueNot Supported | The specified parameter "ConnectionMode" is not valid. |
| 400 | InvalidAccountPrivile ge.Malformed | InvalidAccountPrivilege.ValueNot Support | The specified "AccountPrivilege" is not valid. |
| 400 | IncorrectEngineVersi on | InvaildEngineInRegion.ValueNotS upported | The engine is not supported in the region. |
| 400 | InvalidDBName.Form at | InvalidDBName.Malformed | The specified parameter "DBName" is not valid. |
| 400 | DBLimitExceeded | QuotaExceeded.DBName | The database operation execeed. |
| 400 | InvalidDBName.Dupli cate | InvalidDBName.Duplicate | The Security db Name is not in the available range or occupied. |
| 400 | InvalidCharacterSetN ame.Format | InvalidCharsetName.ValueNotSup port | The specified parameter "CharsetName" is not valid. |
| 400 | InvalidDBDescription .Format | InvalidDBDescription.Malformed | The specified parameter "DBDescription" is not valid. |
| 400 | InvalidDBName.Forbi d | InvalidParameter.Keyword | The specified parameter "DBName" is keyword. |
| 400 | InvalidUserType.NotS upport | InvalidUserType.NotSupport | The operation is not permitted due to type of account. |
| 400 | InvalidExpiredTime.F ormat | InvalidExpiredTime.Malformed | The specified "ExpiredTime" is not valid. |

| olarDB MySQ | L集群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.backupMethod.V alueNotSupported | InvalidBackupMethod.ValueNotSu pport | The specified parameter "BackupMethod" is not valid. |
| 400 | InvalidBackupLog.Ma lformed | InvalidBackupLog.Malformed | The specified parameter "backupPeriod" is not valid. |
| 400 | InvalidStartTime.For mat | InvalidStartTime.Malformed | The specified parameter "StartTime" is not valid. |
| 400 | InvalidEndTime.Form at | InvalidEndTime.Malformed | The specified parameter "EndTime" is not valid. |
| 400 | InvalidMaxRecordsPe rPage.Malformed | InvalidPageSize.Malformed | The specified parameter "PageSize" is not valid. |
| 400 | InvalidSortKey.Malfor med | InvalidSortKey.Malformed | The specified parameter "SortKey" is not valid. |
| 400 | InvalidSortMethod.M alformed | InvalidSortMethod.Malformed | The specified parameter "SortMethod" is not valid. |
| 400 | InvalidParameter | InvalidParameter | Invalid parameter. |
| 400 | InvalidPort.Malforme d | InvalidPort.Malformed | The specified parameter "Port" is not valid. |
| 400 | InvalidKey.Malforme d | InvalidPerformanceKey.Malforme d | The specified parameter "Key" is not valid. |
| 400 | InvalidQueryKeyword .NotSupport | InvalidQueryKeyword.Malformed | the query key contains exception character. |
| 400 | InvalidParameterCo mbination | InvalidStartTimeAndEndTime.Malf ormed | The end time must be greater than the start time. |
| 400 | InvalidParameter.Res ourceOwnerAccount | InvalidParameter.ResourceOwner Account | The specified parameter "resourceOwnerAccount" is not valid. |
| 400 | InvalidStorage.Forma t | InvalidStorage.Format | The specified "storage" is not valid. |
| 403 | Abs.ApiForbiddenByS ubBid | ActionUnauthorized | The specified action is not available for you. |
| 403 | Forbidden | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. |
| 403 | RAM.ApiNotSupporte d | Forbidden.NotSupportRAM | This action does not support accessed by RAM mode. |
| 403 | RISK CONTROL RES _ _ ULT FAIL _ | Forbidden.RiskControl | This operation is forbidden by aliyun risk control system. |
| 403 | InvalidRegion.NotSu pport | OperationDenied.NotSupport | the specified instance region does not support this operation. |
| 403 | IncorrectDBInstanceL ockMode | OperationDenied.LockMode | The operation is not permitted due to instance being locked. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectDBInstance State | OperationDenied.DBInstanceStat us | The operation is not permitted due to status of instance. |
| 403 | IncorrectDBInstance Type | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | ChildDBInstanceNotS upport | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | GuardDBInstanceNot Support | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | ReadDBInstanceNotS upport | OperationDenied.DBInstanceType | The operation is not permitted due to type of the instance. |
| 403 | IncorrectDBInstance Engine | OperationDenied.DBInstanceEngi ne | The operation is not permitted due to engine of instance. |
| 403 | IncorrectDBInstance NetType | OperationDenied.DBInstanceNetT ype | The operation is not permitted due to network type of the instance. |
| 403 | IncorrectDBInstance ConnType | OperationDenied.PublicConnectio nExists | The specified public connection already existed. |
| 403 | InsufficientResource Capacity | OperationDenied | The resource is out of usage. |
| 403 | ClusterNotSupport | OperationDenied.ClusterNotSupp ort | The instance cluster does not support this operation. |
| 403 | IncorrectDBInstance | OperationDenied.DBInstance | The operation is not permitted due to type of the instance. |
| 403 | IncorrectGuardDBIns tanceVersion | OperationDenied.GuardDBInstanc eLower | The operation is not permitted due to higher guard instance version. |
| 403 | IncorrectMasterDBIn stanceState | OperationDenied.MasterDBInstan ceState | The operation is not permitted due to status of master instance. |
| 403 | IncorrectAccountStat us | OperationDenied.AccountStatus | The operation is not permitted due to status of account. |
| 403 | IncorrectAccountTyp e | OperationDenied.AccountType | The operation is not permitted due to type of account. |
| 403 | ConcurrentTaskExce eded | OperationDenied.TaskExceeded | The concurrent tasks exceeded allowed amount. |
| 403 | IncorrectDBInstance AccountMode | OperationDenied.AccountMode | The operation is not permitted due to account mode of instance. |
| 403 | DBNameAndAccount PrivilegeCount | OperationDenied.DBNameAndAcc ountPrivilegeCount | The operation is not permitted due to count of database or account privilege. |
| 403 | OldPasswordWrong | OperationDenied.PasswordWrong | The operation is not permitted due to wrong of password. |
| 403 | IncorrectDBType | OperationDenied.DBType | The operation is not permitted due to type of the database. |

| P I | olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |  |
|---|---|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectDBState | OperationDenied.DBStatus | The operation is not permitted due to status of the database. |
| 403 | BackupJobExists | OperationDenied.BackupJobExists | The operation is not permitted due to backup job exist. |
| 400 | Abs.backupMethod.V alueNotSupported | InvalidBackupMethod.ValueNotSu pport | The specified parameter "BackupMethod" is not valid. |
| 400 | Abs.backupType.Val ueNotSupported | InvalidBackupType.ValueNotSupp ort | The specified parameter "BackupType" is not valid. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL INSU _ _ _ FFICIENT BALANCE _ | InsufficientBalance | Your account does not have enough balance. |
| 400 | FUWU BIZ COMMODI _ _ TY VERIFY FAIL INSU _ _ _ FFICIENT BALANCE _ | InsufficientBalance | Your account does not have enough balance. |
| 400 | INSTANCE PRODUCE _ FAILED _ | CreateOrder.Failed | The instance order is error. |
| 404 | InvalidDBInstanceNa me.NotFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidInstanceId | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | InvalidDB.NotFound | InvalidDB.NotFound | The Specified db does not exist or DB status does not support. |
| 404 | InvalidDBInstance.No tFound | InvalidDBInstanceId.NotFound | The specified instance is not found. |
| 404 | RAM.InstanceNotFou nd | Forbidden.InstanceNotFound | The specified instance is not found. |
| 404 | InvalidConnectionStri ng.Duplicate | InvalidConnectionStringPrefix.Du plicated | Specified connection string needs to be same as current network type. |
| 404 | AtLeastOneNetTypeE xists | AtLeastOneNetTypeExists | The specified network type at least one. |
| 404 | NetTypeExists | NetTypeExists | The specified public network type already exists. |
| 404 | InvalidConnectionStri ngOrPort.Duplicate | InvalidConnectionString.Duplicate | Specified connection string or port needs to be same as current network type. |
| 404 | InvalidConnectionStri ng.NotFound | InvalidConnectionString.NotFound | The specified connection string or network type is not found. |
| 404 | ConnectionStringLen gthExceeded | ConnectionStringLengthExceeded | The specified connection string is too long. |
| 404 | InvalidSecurityIPList. QuotaExceeded | InvalidSecurityIPListLength.Malfor med | The security IP address is not in the available range or occupied. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidSecurityIPList. NotFound | InvalidSecurityIPs.NotFound | The specified security ip list has no matching value or at least one security IP is needed. |
| 404 | InvalidSecurityIPList. Duplicate | InvalidInstanceIp.Duplicate | Invalid security IP list specified, duplicated. |
| 404 | InvalidDBInstanceNe tType.NotFound | InvalidDBInstanceNetType.NotFo und | The specified instance network type is not found. |
| 403 | ChildDBInstanceExist s | OperationDenied.ChildDBInstance Exists | The specified instance had child instance. |
| 404 | GuardInstance.Exist | InvalidGuardInstanceId.Exist | The guard instance has exist. |
| 404 | InvalidDBInstanceCla ss.NotFound | InvalidDBInstanceClass.NotFound | The specified instance class is not found. |
| 404 | InvalidUser.NotFoun d | InvalidUser.NotFound | The specified user does not exist. |
| 404 | InvalidOperatorPermi ssion.NotFound | InvalidOperatorPermission.NotFo und | The permission provided does not exist. |
| 404 | InvalidDBName.NotF ound | InvalidDBName.NotFound | The specified database is not found. |
| 404 | ParamNotFound | Param.NotFound | The specified params is not found. |
| 404 | InvalidAccountName. NotFound | InvalidAccountName.NotFound | The specified account is not found. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unkown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | Unknown.Exception | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -101 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -130 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -100 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | -40 | InternalError | The request processing has failed due to some unknown error, exception or failure. |

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | 200 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 400 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 403 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 500 | 500 | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |
| 500 |  | InternalError | The request processing has failed due to some unknown error, exception or failure. |

### RestartDBNode

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBNodeId | String | Query | 是 | pi-************* |  | 集群节点ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括节点ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | *** |  | rs |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |  |  |

|  |  |  |  | PolarD | B MySQL集群版开发指南·A |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBNodeId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

### 查询参数模版列表

查询数据库集群默认参数的列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBType | String | Query | 是 | MySQL | 数据库引擎类型，当前仅支持MySQL 。 |
| DBVersion | String | Query | 是 | 5.7 | 数据库版本，取值范围如下： 5.6 5.7 8.0 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看当前账号下的所有可用地域信息，包括地域ID。 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ParameterCount | String | 183 | 参数数量。 |
| DBVersion | String | 5.7 | 数据库引擎版本。 |
| Parameters | Array |  | 参数列表。 |
| -CheckingCode | String | [ROW\|STATEMENT\|MI XED] | 参数取值范围。 |
| - ParameterName | String | binlog format _ | 参数名称。 |
| - ParameterValue | String | ROW | 参数默认值。 |
| -ForceModify | String | true | 参数是否可修改，取值范围如下： true ：可修改 false ：不可修改 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ForceRestart | String | false | 参数修改后，是否需要重启新参数值才生效。取值范围如下： true ：需要重启 false ：不需要重启 |
| - ParameterDescr iption | String | What form of binary logging the master will use. | 参数描述。 |
| - IsNodeAvailable | String | 1 | 是否是全局参数。取值： 0 ：是全局参数。修改后的参数值会默认同步到其他节点； 1 ：不是全局参数。修改后的参数值可自定义需要同步的节点。 |
| -ParamRelyRule | String | utf8 | 参数依赖。 |
| RequestId | String | D963934D-8605- 4473-8EAC- 54C719****** | 请求ID。 |
| DBType | String | MySQL | 数据库引擎类型。 |
| Engine | String | POLARDB | 数据库引擎。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ParameterCount":"183",
 "DBVersion":"5.7",
 "Parameters":{
  "ForceModify":"true",
  "CheckingCode":"[ROW|STATEMENT|MIXED]",
  "ParameterValue":"ROW",
  "ForceRestart":"false",
  "IsNodeAvailable":"1",
  "ParamRelyRule":"utf8",
  "ParameterName":"binlog_format",
  "ParameterDescription":"What form of binary logging the master will use."
 },
 "RequestId":"D963934D-8605-4473-8EAC-54C719******",
 "DBType":"MySQL",
 "Engine":"POLARDB"
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBType.NotFo und | InvalidDBType.NotFound | The Specified DBType does not found. |
| 400 | InvalidDBVersion.Mal formed | InvalidDBVersion.Malformed | The Specified DBVersion is not valid. |

### DescribeTasks

调用DescribeTasks接口查看通过API生成的任务（如创建集群）进度详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 否 | pc-*************** | 集群ID。 DBNodeId 和 DBCl usterId 必选其一填入。您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |
|  |  |  |  |  |  | DBCl |  |
| DBNodeId | String | Query | 否 | pi-*************** | 节点ID。 DBNodeId 和 DBCl usterId 必选其一填入。您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括节点ID。 |  |  |
|  |  |  |  |  |  | DBCl |  |
| StartTime | String | Query | 是 | 2020-11-30T00:00Z | 查询开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |  |  |
| EndTime | String | Query | 是 | 2020-12-02T03:00Z | 查询结束时间，查询结束时间需晚于开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |  |  |

|  |  |  | usterId |  |  |
|---|---|---|---|---|---|
|  |  |  |  | DescribeDBCluste |  |
|  |  |  | rs |  |  |

|  |  |  | usterId |  |  |
|---|---|---|---|---|---|
|  |  |  |  | DescribeDBCluste |  |
|  |  |  | rs |  |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Status | String | Query | 否 | Running | 任务状态，取值范围如下： Waiting ：任务等待执行中 Running ：任务正在执行中 Finished ：任务已完成 Closed ：任务已关闭 Pause ：任务已暂停 Stop ：任务已中断若该参数留空，仅返回当前集群或节点下所有状态为Waiting 或Run ning 的任务详情。 支持输入多个任务状态，各状态之间用逗号分割查询。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值为30 、50 或100 。 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值为大于0且不超过 Integer数据类型的最大值。 默认值为1 。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | Integer | 1 | 总记录数。 |
| PageRecordCou nt | Integer | 30 | 本页记录数。 |
| Tasks | Array |  | 任务详情。 |
| -TaskId | String | 111111111 | 目标任务ID。 |
| -BeginTime | String | 2020-12- 02T02:39:15Z | 任务开始时间，格式为 YYYY-MM- DDThh:mm:ssZ （UTC时间）。 |

|  | DDThh:mm:ssZ |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -FinishTime | String | 2020-12- 02T02:40:15Z | 任务完成时间，格式为 YYYY-MM- DDThh:mm:ssZ （UTC时间）。 |
| - ExpectedFinishT ime | String | null | 预计结束时间。若无特殊情况，该参数为空。 |
| -TaskAction | String | CreateDBInstance | 目标任务所使用的API接口，例如 CreateDBInstance 。 |
| -Progress | Integer | 100 | 任务进度百分比。 |
| -DBName | String | test | 数据库名称。 仅涉及数据库相关操作的任务会返回该参数。 |
| -ProgressInfo | String | null | 任务进度的描述信息。若目标任务无进度描述信息， 该参数为空。 |
| -TaskErrorCode | String | null | 任务出错时的错误码。 仅当任务状态为Stop 时返回该参数。 |
| - TaskErrorMessa ge | String | null | 任务出错时的错误信息。 仅当任务状态为Stop 时返回该参数。 |
| -StepsInfo | String | [{\"remain\":0,\"nam e\":\"init task\",\"pro _ gress\":100}, {\"remain\":1764,\"n ame\":\"create insta _ nce\",\"progress\":0}, {\"remain\":1,\"name \":\"init cluster\",\"pr _ ogress\":0}, {\"remain\":2,\"name \":\"create backup\",\ _ "progress\":0}] | 任务子步骤详情。 |
| -Remain | Integer | 1767 | 任务预计剩余时间，单位为秒。 |
| - StepProgressInf o | String | 1/4 | 任务子步骤进度。例如 1/4 表示该任务共包含4个子步骤，当前正在执行第一步。 |
| - CurrentStepNa me | String | create instance _ | 当前任务的子步骤名称。 |
| EndTime | String | 2020-12-02T03:00Z | 查询结束时间。 |

|  | DDThh:mm:ssZ |
|---|---|

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4352AD99-9FF5- 41A6-A319- 068089****** | 请求ID。 |
| PageNumber | Integer | 1 | 页码。 |
| StartTime | String | 2020-11-30T00:00Z | 查询开始时间。 |
| DBClusterId | String | pc-*************** | 任务所对应的集群ID。 |

**示例**

请求示例

```
&StartTime=2020-11-30T00:00Z &EndTime=2020-12-02T03:00Z
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":1,
 "PageRecordCount":30,
 "Tasks":{
  "ExpectedFinishTime":"null",
  "Progress":100,
  "TaskId":"111111111",
  "Remain":1767,
  "TaskAction":"CreateDBInstance",
  "BeginTime":"2020-12-02T02:39:15Z",
  "TaskErrorMessage":"null",
  "StepProgressInfo":"1/4",
  "FinishTime":"2020-12-02T02:40:15Z",
  "StepsInfo":"[{\\\"remain\\\":0,\\\"name\\\":\\\"init_task\\\",\\\"progress\\\":100},
{\\\"remain\\\":1764,\\\"name\\\":\\\"create_instance\\\",\\\"progress\\\":0}, {\\\"remain\\\":1,\\\"name\\\":\\\"init_cluster\\\",\\\"progress\\\":0}, {\\\"remain\\\":2,\\\"name\\\":\\\"create_backup\\\",\\\"progress\\\":0}]",
  "CurrentStepName":"create_instance",
  "ProgressInfo":"null",
  "DBName":"test",
  "TaskErrorCode":"null"
 },
 "EndTime":"2020-12-02T03:00Z",
 "RequestId":"4352AD99-9FF5-41A6-A319-068089******",
 "PageNumber":1,
 "StartTime":"2020-11-30T00:00Z",
 "DBClusterId":"pc-***************"
}
```

云原生数据库 I参考

### DescribeMetaList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |  |  |
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 您可以通过 DescribeDBCluste rs 接口查询账号下所有集群的信息详情。 |  |  |
| BackupId | String | Query | 否 | 111111 | 备份集ID。 查询时， BackupId 和 RestoreTime 参数必选其一传入。 您可以通过 DescribeBackups 接口查看备份集ID。 |  |  |
| RestoreTim e | String | Query | 否 | 2020-10-04T01:40:00Z | 还原时间点，格式为YYYY- MM-DDThh:mmZ（UTC时间）。 查询时， BackupId 和 R estoreTime 参数必选其一传入。您可以通过 DescribeBackups 接口查看还原时间点。 |  |  |
|  |  |  |  |  |  | R |  |
| GetDbNam e | String | Query | 否 | test db _ | 传入具体的数据库名称 （如 test db ）以获取目 _ 标数据库所有支持恢复的数据表名称。 每次仅支持传入一个数据库名称。 若该参数留空，您可以查看当前备份集下所有支持恢复的数据库名称，但无法查看各数据库下对应的数据表名称。 |  |  |

|  |  |  | DescribeDBCluste |  |
|---|---|---|---|---|
|  |  | rs |  |  |

|  | BackupId |
|---|---|
| estoreTime |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 50 100 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalPageCount | String | 1 | 总页数。 |
| TotalRecordCou nt | String | 2 | 总记录数。 |
| PageSize | String | 30 | 本页记录数。 |
| RequestId | String | AA815DE7-B576- 4B22-B33C- 3FB31A****** | 请求ID。 |
| PageNumber | String | 1 | 页码。 |
| DBClusterId | String | pc- bp1s826a1up****** | 集群ID。 |
| Items | Array |  | 支持恢复的库表信息详情。 |
| -Tables | String |  |  |
| -Database | String | test db _ | 支持恢复的数据库名称。 |

**示例**

请求示例

```
&DBClusterId=pc-**************
```

&公共请求参数云原生数据库 I参考正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalPageCount":"1",
 "TotalRecordCount":"2",
 "PageSize":"30",
 "RequestId":"AA815DE7-B576-4B22-B33C-3FB31A******",
 "PageNumber":"1",
 "DBClusterId":"pc-bp1s826a1up******",
 "Items":{
  "Database":"test_db",
  "Tables":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRestoreType.F ormat | InvalidRestoreType.Format | Specified restore type is not valid. |
| 400 | InvalidRestoreTime.F ormat | InvalidRestoreTime.Format | Specified restore time is not valid. |
| 400 | InvalidBackupSetID. NotFound | InvalidBackupSetID.NotFound | Specified backup set ID does not exist. |
| 400 | IncorrectBackupSetS tate | IncorrectBackupSetState | Current backup set state does not support operations. |
| 400 | InvalidDBName.Dupli cate | InvalidDBName.Duplicate | Specified DB name already exists in the This instance. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | InsufficientResource Capacity | InsufficientResourceCapacity | There is insufficient capacity available for the requested instance. |
| 400 | InvalidRestoreType.N otFound | InvalidRestoreType.NotFound | At least one of BackupId and RestoreTime is malformed. |
| 400 | MissingUserID | MissingUserID | The request is missing a user id _ parameter. |
| 400 | MissingUID | MissingUID | The request is missing a uid parameter. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidBackup.NotFo und | InvalidBackup.NotFound | The available backup does not exist in recovery time. |

云原生数据库 I参考

### DescribeDBClusterPerformance

调用DescribeDBClusterPerformance接口查询PolarDB集群的性能数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| Key | String | Query | 是 | PolarDBDiskUsage | 查询的性能指标，多个值间用英文逗号（,）分隔。 最多可传入5个查询的性能指标。 |
| StartTime | String | Query | 是 | 2020-09-23T01:01Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2020-09-23T01:00Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PerformanceKey s | Array |  | 集群性能数据列表。 |
| -Points | Array |  | 性能数据数组。 |
| --Value | String |  |  |
| --Timestamp | Long |  |  |
| -MetricName | String | mean data size _ _ | 具体的性能指标度量名称。 |
| -Measurement | String | PolarDBDiskUsage | 性能指标。 |
| -DBNodeId | String | pi-************* | 数据库集群节点ID。 当请求参数中 Key 的值设置为 PolarDBDiskUsage 时，不会返回该参数。 |
| DBVersion | String | 8.0 | 兼容数据库版本。 |

| olarDB MySQL集参考 | 群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| EndTime | String | 2020-09- 23T01:01:00Z | 查询结束时间。格式： yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
|---|---|---|---|
| RequestId | String | 35D3E3DA-4650- 407A-BFF5- 59BFF1****** | 请求ID。 |
| StartTime | String | 2020-09- 23T01:00:00Z | 查询开始时间。格式： yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| DBClusterId | String | pc-***************** | 数据库集群ID。 |
| DBType | String | MySQL | 兼容数据库类型。 |
| Engine | String |  |  |

|  | ddTHH:mm:ssZ |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterPerformance &DBClusterId=pc-**************** &Key=PolarDBDiskUsage &StartTime=2020-09-23T01:01Z &EndTime=2020-09-23T01:00Z
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "PerformanceKeys":{
  "Measurement":"PolarDBDiskUsage",
  "MetricName":"mean_data_size",
  "-Points":{
   "Value":"",
   "Timestamp":""
  },
  "DBNodeId":"pi-*************"
 },
 "DBVersion":"8.0",
 "EndTime":"2020-09-23T01:01:00Z",
 "RequestId":"35D3E3DA-4650-407A-BFF5-59BFF1******",
 "StartTime":"2020-09-23T01:00:00Z",
 "DBClusterId":"pc-*****************",
 "DBType":"MySQL",
 "Engine":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidKey.Malforme d | InvalidKey.Malformed | The specified parameter Key is not valid. |
| 400 | InvalidEndTime.Malfo rmed | InvalidEndTime.Malformed | The specified parameter EndTime is not valid. |
| 400 | InvalidStartTime.Malf ormed | InvalidStartTime.Malformed | The specified parameter StartTime is not valid. |
| 400 | InvalidParameterCo mbination | InvalidParameterCombination | The end time must be greater than the start time. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeDBClusters

查询PolarDB集群列表或被RAM授权的集群列表详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过接口 DescribeRegions 查看可用的地域。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI ds | String | Query | 否 | pc-**************** | 集群ID。多个集群ID间用英文逗号（,）隔开。 |
| DBClusterD escription | String | Query | 否 | pc-**************** | 集群描述，可模糊查询。 |
| Connection String | String | Query | 否 | ********.rwlb.polardb-pg- public.rds.aliyuncs.com | 数据库连接地址。 |
| DBClusterS tatus | String | Query | 否 | Running | 集群状态。 |
| DBType | String | Query | 否 | MySQL | 数据库类型，取值范围如下： MySQL PostgreSQL Oracle |
| DBVersion | String | Query | 否 | 5.6 | 数据库版本。 |
| RecentCrea tionInterval | Intege r | Query | 否 | 7 | 筛选最近N天创建的集群。取值范围：0~15。 |
| RecentExpi rationInterv al | Intege r | Query | 否 | 6 | 筛选N天后过期的集群。取值范围：0~15。 |
| Expired | Boole an | Query | 否 | true | 是否集群已过期。取值范围： true false |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值为30 、50 或100 。 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 10 | 页码，取值为大于0且不超过 Integer数据类型的最大值，默认值为1 。 |
| ResourceGr oupId | String | Query | 否 | rg-********** | 资源组ID。 |
| Tag | Repea tList | Query | 否 |  | 1 |
| PayType | String | Query | 否 | Postpaid | 付费类型，取值范围如下： Postpaid ：按量付费 Prepaid ：预付费（包年包月） |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBNodeIds | String | Query | 否 | pi-*************** | 节点ID。支持传入多个节点 ID，多个ID间用英文逗号（,） 分隔。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | Integer | 16 | 总记录数。 |
| PageRecordCou nt | Integer | 5 | 本页集群数量。 |
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| PageNumber | Integer | 12 | 页数。 |
| Items | Array |  | 集群列表。 |
| -Tags | Array |  | 标签列表。 |
| --Key | String |  |  |
| --Value | String |  |  |
| -DBNodes | Array |  | 节点列表。 |
| --DBNodeClass | String |  |  |
| --ZoneId | String |  |  |
| --DBNodeRole | String |  |  |
| --DBNodeId | String |  |  |
| --RegionId | String |  |  |
| -VpcId | String | vpc-**************** | 专有网络ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -ExpireTime | String | 2020-11- 14T16:00:00Z | 集群到期时间。 仅付费方式为Prepaid （包年包月）的集群会返回具体参数值，Postpaid （按量付费）集群则返回空值。 |
| -Expired | String | false | 集群是否到期。取值范围： true false 仅付费方式为Prepaid （包年包月）的集群支持返该参数。 |
| - DBNodeNumber | Integer | 2 | 节点数量。 |
| -CreateTime | String | 2020-08- 14T05:58:42Z | 创建时间。 |
| -PayType | String | Prepaid | 付费类型。取值范围： Postpaid ：按量付费。 Prepaid ：包年包月（预付费）。 |
| - StoragePayType | String | Prepaid | 存储计费类型。取值范围： Postpaid ：按容量计费（按量计费）。 Prepaid ：按空间计费（包年包月）。 |
| -ServerlessType | String | AgileServerless | Serverless类型。当前取值固定为AgileServerless （敏态）。 |
| - DBProxyCluster Class | String |  |  |
| - HotStandbyClus ter | String |  |  |
| -DBNodeClass | String | polar.mysql.x4.large | 节点规格。 |
| -DBType | String | MySQL | 数据库类型。 |
| -LockMode | String | Unlock | 集群的锁定状态，取值范围如下： Unlock ：正常。 ManualLock ：手动触发锁定。 LockByExpiration ：集群过期自动锁定。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DeletionLock | Integer | 0 | 集群删除的保护状态，取值范围如下： 0 ：未锁定。 1 ：锁定。 锁定状态时，不可以删除集群。 |
| -DBVersion | String | 5.6 | 数据库版本。 |
| -DBClusterId | String | pc-**************** | 集群ID。 |
| - DBClusterStatus | String | Running | 集群状态。 |
| - ResourceGroupI d | String | rg-************ | 资源组ID。 |
| -StorageUsed | Long | 3009413120 | 集群已经使用的存储用量，单位为Byte。 |
| -StorageSpace | Long | 50 | 按空间计费（包年包月）的存储空间。单位：Byte。 |
| - DBClusterNetwo rkType | String | VPC | 集群的网络类型。 |
| - DBClusterDescri ption | String | GDN-1 | 集群描述。 |
| -ZoneId | String | cn-hangzhou-i | 可用区ID。 |
| -Engine | String | POLARDB | 集群引擎。 |
| -Category | String | Normal | 集群系列，目前支持如下系列： Normal ：集群版 Basic ：单节点 Archive ：高压缩引擎（X-Engine） NormalMultimaster ：多主集群（库表） |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusters &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":16,
 "PageRecordCount":5,
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "PageNumber":12,
 "Items":{
  "DeletionLock":0,
  "Category":"Normal",
  "ResourceGroupId":"rg-************",
  "StoragePayType":"Prepaid",
  "-Tags":{
   "Value":"",
   "Key":""
  },
  "HotStandbyCluster":"",
  "DBClusterId":"pc-****************",
  "DBType":"MySQL",
  "DBClusterNetworkType":"VPC",
  "DBProxyClusterClass":"",
  "DBVersion":"5.6",
  "-DBNodes":{
   "ZoneId":"",
   "DBNodeRole":"",
   "DBNodeId":"",
   "RegionId":"",
   "DBNodeClass":""
  },
  "Engine":"POLARDB",
  "ZoneId":"cn-hangzhou-i",
  "DBClusterStatus":"Running",
  "CreateTime":"2020-08-14T05:58:42Z",
  "DBClusterDescription":"GDN-1",
  "Expired":"false",
  "PayType":"Prepaid",
  "LockMode":"Unlock",
  "DBNodeClass":"polar.mysql.x4.large",
  "StorageUsed":3009413120,
  "DBNodeNumber":2,
  "VpcId":"vpc-****************",
  "StorageSpace":50,
  "ServerlessType":"AgileServerless",
  "RegionId":"cn-hangzhou",
  "ExpireTime":"2020-11-14T16:00:00Z"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NumberExceed.Tags | NumberExceed.Tags | The Tags parameter's number is exceed. |
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter PageSize is not valid. |
| 400 | InvalidPageNumber. Malformed | InvalidPageNumber.Malformed | The specified parameter PageNumber is not valid. |
| 500 | InternalError | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |

### DescribeLogBackupPolicy

调用DescribeLogBackupPolicy接口查询PolarDB集群日志备份的保留策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-***************** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ******* |  | rs |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LogBackupAnot herRegionRegio n | String |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| LogBackupRete ntionPeriod | Integer | 7 | 日志保留周期，取值范围如下： 3～7300：日志保留周期，单位天。 -1：永久保留。 |
| LogBackupAnot herRegionReten tionPeriod | String |  |  |
| RequestId | String | 62EE0051-102B- 488D-9C79- D607B8****** | 请求ID。 |
| EnableBackupL og | Integer | 1 | 是否开启日志备份，取值范围如下： 0：未开启。 1：开启（默认全部开启且不支持关闭）。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "LogBackupAnotherRegionRegion":"",
 "LogBackupRetentionPeriod":"",
 "LogBackupAnotherRegionRetentionPeriod":"",
 "RequestId":"",
 "EnableBackupLog":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### EvaluateRegionResource

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 云原生数据库 I参考

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBType | String | Query | 是 | MySQL | 数据库引擎类型，取值范围如下： MySQL PostgreSQL Oracle |
| DBVersion | String | Query | 是 | 8.0 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 5.7 8.0 PostgreSQL版本号取值范围如下： 11 14 Oracle版本号取值为11 。 |
| SubDomain | String | Query | 否 | cn-beijing-i-aliyun | 子域。即顶级域名（一级域名或父域名）的下一级。例如： 父域名为：cn-beijing，则它的子域可以为cn-beijing-i- aliyun。 |
| DBNodeCla ss | String | Query | 是 | polar.mysql.x4.large | 节点规格。 |
| DBInstance ConnType | String | Query | 否 | lvs | 指定集群链路类型，后端随机选择默认值，取值范围如下： lvs ：Linux虚拟服务器。 proxy ：代理服务器。 dns ：域名系统。 |
| DispenseM ode | String | Query | 否 | 1 | 是否返回支持单可用区部署功能的可用区列表。取值范围如下： 0 （默认）：不返回。 1 ：返回。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NeedMaxSc aleLink | String | Query | 是 | true | 是否创建Maxscale，取值范围如下： true （默认）：创建 Maxscale。 false ：不创建 Maxscale。 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看可用地域。 |
| ZoneId | String | Query | 是 | cn-hangzhou-g | 可用区ID。 您可以通过 DescribeRegions 接口查看可选的可用区。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBInstanceAvail able | String | true | 是否有足够的资源。 true ：有足够的资源。 false ：资源不足。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBVersion | String | 8.0 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 5.7 8.0 PostgreSQL版本号取值范围如下： 11 14 Oracle版本号取值为11 。 |
| RequestId | String | 69A85BAF-1089- 4CDF-A82F- 0A140F****** | 请求ID。 |
| DBType | String | MySQL | 数据库引擎类型，取值范围如下： MySQL PostgreSQL Oracle |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBType":"null", "DBVersion":"null", "DBNodeClass":"null", "NeedMaxScaleLink":"null", "RegionId":"null", "ZoneId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "DBInstanceAvailable":"",
 "DBVersion":"",
 "RequestId":"",
 "DBType":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBType.Malfor med | InvalidDBType.Malformed | The Specified DBType is not valid. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBVersion.Mal formed | InvalidDBVersion.Malformed | The Specified DBVersion is not valid. |
| 404 | SubDomain.Malform ed | SubDomain.Malformed | The specified SubDomain does not exist or ZoneId is not valid. |

### ModifyDBClusterDeletion

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-bp1313h70cd5m**** |  | 目标集群ID。 您可以通过 DescribeDBCluste rs 接口查看集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  |  |  | rs |  |  |
| Protection | Boole an | Query | 否 | true |  | 开启或者关闭集群保护锁，默认值为false，取值： true ：开启集群保护锁，开启后不能直接释放该集群，需要关闭集群保护锁后重新释放。 false ：关闭集群保护锁。 |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

云原生数据库 I参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 24C80BD8-C710- 4138-893A- D2AFED4FC13D | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyBackupPolicy

调用ModifyBackupPolicy接口修改PolarDB集群的自动备份策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-bp13wz9586voc**** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | 86voc**** |  | rs |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PreferredB ackupTime | String | Query | 否 | 15:00Z-16:00Z | 执行自动备份的时间段，格式为 hh:mmZ- hh:mmZ （UTC时间），且输入的数值必须为间隔1个小时的整点，如 14:00Z- 15:00Z 。 |
| PreferredB ackupPerio d | String | Query | 否 | Monday,Tuesday | 备份周期，取值范围如下： Monday ：周一 Tuesday ：周二 Wednesday ：周三 Thursday ：周四 Friday ：周五 Saturday ：周六 Sunday ：周日至少需要选择2天，多个值之间用英文逗号 （,）隔开。 如果您的PolarDB MySQL 版所在的地域支持跨地域备份功能，将不支持该参数。 |
| DataLevel1 BackupRet entionPerio d | String | Query | 否 | 3 | 一级备份保留周期，取值范围为3~14，单位为天。 |
| DataLevel2 BackupRet entionPerio d | String | Query | 否 | 0 | 二级备份保留周期，取值范围如下： 0 ：关闭二级备份功能。 30～7300 ：二级备份保留周期，单位为天。 1 ：二级备份永久保留。 创建集群时，默认取值为0 ，即关闭二级备份功能。 |
| BackupRet entionPolic yOnCluster Deletion | String | Query | 否 | NONE | 删除集群时是否保留备份： ALL ：永久保留全部备份。 LATEST ：永久保留最后一个备份。 NONE ：不保留备份集。 默认取值为NONE。 |

|  |  | hh:mmZ- |
|---|---|---|
|  | hh:mmZ |  |

|  | 15:00Z |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BackupFre quency | String | Query | 否 | Normal | 备份频率，取值如下： Normal （默认）：常规备份，每天定时备份一次。 2/24H ：高频备份，每2 小时备份一次。 3/24H ：高频备份，每3 小时备份一次。 4/24H ：高频备份，每4 小时备份一次。 开启高频备份后，备份完成时间在24小时内的备份会全部保留。超过24小时的， 系统将仅保留每日 00:00点后完成的第一个备份，其他均被删除。 开启高频备份后，备份周期PreferredBackupPe riod 参数会默认选择一周内的所有天数（即从周一至周日）。 如果您的PolarDB MySQL 版所在的地域支持跨地域备份功能，将不支持该参数。 |
| DataLevel1 BackupFre quency | String | Query | 否 | Normal | 备份频率，取值如下： Normal （默认）：常规备份，每天定时备份一次。 2/24H ：高频备份，每2 小时备份一次。 3/24H ：高频备份，每3 小时备份一次。 4/24H ：高频备份，每4 小时备份一次。 PolarDB PostgreSQL版（兼容 Oracle）、PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL 版所在的地域不支持跨地域备份功能，将不支持该参数。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataLevel1 BackupTim e | String | Query | 否 | 15:00Z-16:00Z | 执行自动备份的时间段，格式为 hh:mmZ- hh:mmZ （UTC时间），且输入的数值必须为间隔1个小时的整点，如 14:00Z- 15:00Z 。 PolarDB PostgreSQL版（兼容 Oracle）、PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL 版所在的地域不支持跨地域备份功能，将不支持该参数。 |
| DataLevel1 BackupPeri od | String | Query | 否 | Monday,Tuesday | 一级备份周期，取值范围如下： Monday ：周一 Tuesday ：周二 Wednesday ：周三 Thursday ：周四 Friday ：周五 Saturday ：周六 Sunday ：周日至少需要选择2天，多个值之间用英文逗号 （,）隔开。 PolarDB PostgreSQL版 （兼容Oracle）、PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL 版所在的地域不支持跨地域备份功能，将不支持该参数。 |

|  |  | hh:mmZ- |
|---|---|---|
|  | hh:mmZ |  |

|  | 15:00Z |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DataLevel2 BackupPeri od | String | Query | 否 | Monday,Tuesday | 二级备份周期，取值范围如下： Monday ：周一 Tuesday ：周二 Wednesday ：周三 Thursday ：周四 Friday ：周五 Saturday ：周六 Sunday ：周日至少需要选择2天，多个值之间用英文逗号 （,）隔开。 PolarDB PostgreSQL版 （兼容Oracle）、PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL 版所在的地域不支持跨地域备份功能，将不支持该参数。 |
| DataLevel2 BackupAno therRegion Region | String | Query | 否 | cn-hangzhou | 二级备份跨地域备份区域。 |
| DataLevel2 BackupAno therRegion RetentionP eriod | String | Query | 否 | 30 | 二级备份跨地域备份保留周期。取值范围如下： 0 ：关闭二级备份功能。 30～7300 ：二级备份保留周期，单位为天。 1 ：二级备份永久保留。 创建集群时，默认取值为0 ，即关闭二级备份跨地域备份功能。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C5A5DF0E-5968- 4DC1-882E- AC2FE7****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDataLevel1Ba ckupRetentionPeriod. Malformed | InvalidDataLevel1BackupRetentio nPeriod.Malformed | The specified parameter DataLevel1BackupRetentionPerio d is not valid. |
| 400 | InvalidDataLevel2Ba ckupRetentionPeriod. Malformed | InvalidDataLevel2BackupRetentio nPeriod.Malformed | The specified parameter DataLevel2BackupRetentionPerio d is not valid. |
| 400 | InvalidBackupRetenti onPeriod.Malformed | InvalidBackupRetentionPeriod.Mal formed | The specified parameter BackupRetentionPeriod is not valid. |
| 400 | InvalidBackupFreque ncy.Malformed | InvalidBackupFrequency.Malform ed | The specified parameter BackupFrequency is not valid. |
| 400 | InvalidPreferredBack upPeriod.Malformed | InvalidPreferredBackupPeriod.Mal formed | The specified parameter PreferredBackupPeriod is not valid. |
| 400 | InvalidDataLevel2Ba ckupPeriod.Malforme d | InvalidDataLevel2BackupPeriod.M alformed | The specified parameter DataLevel2BackupPeriod is not valid. |
| 400 | InvalidDataLevel1Ba ckupPeriod.Malforme d | InvalidDataLevel1BackupPeriod.M alformed | The specified parameter DataLevel1BackupPeriod is not valid. |
| 403 | IncorrectBackupPolic y | IncorrectBackupPolicy | Current DB type does not support low frequency backupPolicy operation. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidParam | InvalidParam | new archiveBackup policy already exists. dumpretention parameter cannot used alone |

### DescribeDBClusterAttribute

调用DescribeDBClusterAttribute接口查看PolarDB集群的详细属性。 云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-***************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ******* |  | rs |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DeletionLock | Integer | 0 | 集群删除的锁定状态，取值范围如下： 0 ：未锁定，可删除集群。 1 ：锁定，不可删除集群。 |
| Category | String | Normal | 产品系列。取值范围如下： Normal ：集群版 Basic ：单节点 Archive ：高压缩引擎（X-Engine） NormalMultimaster ：多主架构集群版 SENormal ：标准版仅PolarDB MySQL版支持单节点产品系列。 仅PolarDB MySQL版8.0.1版本的集群，支持标准版产品系列。 仅PolarDB MySQL版8.0版本的集群，支持高压缩引擎（X-Engine）和多主架构集群版产品系列。 |
| ResourceGroupI d | String | rg-*************** | 资源组ID。 |
| StoragePayType | String | Prepaid | 存储计费类型。取值范围如下： Postpaid ：按容量计费（按量付费）。 Prepaid ：按空间计费（包年包月）。 |
| DataLevel1Back upChainSize | Long | 74448896 | 一级备份（快照）总大小，单位为Byte。 |

| olarDB MySQL集 | 群版开发指南·AP |  |  |
|---|---|---|---|

I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBClusterId | String | pc-***************** | 集群ID。 |
| ProxyStatus | String | Running | 数据库代理的状态。取值范围： Creating ：创建中 Running ：运行中 Deleting ：释放中 Rebooting ：重启中 DBNodeCreating ：正在增加节点 DBNodeDeleting ：正在删除节点 ClassChanging ：正在变更节点规格 NetAddressCreating ：正在创建网络连接 NetAddressDeleting ：正在删除网络连接 NetAddressModifying ：正在修改网络连接 Deleted ：已释放 |
| DBType | String | MySQL | 数据库引擎类型。 |
| DBClusterNetwo rkType | String | VPC | 集群的网络类型。 |
| BlktagUsed | Long | 5,242,880 | 当前blktag使用量。 |
| ProxyStandardC puCores | String | 2 | 数据库代理标准配置CPU核数。 |
| IsLatestVersion | Boolean | false | 是否为最新内核版本。取值范围如下： true ：是 false ：否 |
| StorageMax | Long | 10995116277760 | 当前集群规格的最大存储容量，单位为Byte。 |
| DBVersion | String | 8.0 | 数据库引擎版本。 |
| DBNodes | Array |  | 节点信息详情。 |
| -CreationTime | String | 2020-03- 23T21:35:43Z | 节点创建时间。 |
| -FailoverPriority | Integer | 1 | Failover优先级。每个节点都有一个Failover优先级，决定了当故障切换时，该节点被选举为主节点的概率高低。数值越大，优先级越高，取值范围为 1~15。 |
| -MaxIOPS | Integer | 32000 | 最大I/O请求次数，即IOPS。 |

I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DBNodeClass | String | polar.mysql.x4.large | 节点规格。 |
| -DBNodeRole | String | Reader | 节点角色，取值范围如下： Writer ：主节点。 Reader ：只读节点。 |
| -ZoneId | String | cn-hangzhou-i | 可用区ID。 |
| - MaxConnections | Integer | 8000 | 最大集群并发连接数。 |
| -DBNodeStatus | String | Running | 节点状态，取值范围如下： Creating ：创建中 Running ：运行中 Deleting ：删除中 Rebooting ：重启中 DBNodeCreating ：正在增加节点 DBNodeDeleting ：正在删除节点 ClassChanging ：正在变更节点规格 NetAddressCreating ：正在创建网络连接 NetAddressDeleting ：正在删除网络连接 NetAddressModifying ：正在修改网络连接 MinorVersionUpgrading ：小版本升级中 Maintaining ：实例维护中 Switching ：切换中 |
| -DBNodeId | String | pi-**************** | 节点ID。 |
| -ImciSwitch | String | ON | 是否开启列存索引。取值范围： ON ：开启 OFF ：关闭 |
| - HotReplicaMode | String | ON | 是否开启热备。取值范围： ON ：开启 OFF ：关闭 |
| - AddedCpuCores | String | 6 | 秒级弹性扩核的CPU核数。 |
| -MasterId | String | pi- bp18z52akld3***** | 多主架构集群版的主节点ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -SccMode | String | ON | 节点是否开启全局一致性（高性能模式）功能。取值范围： ON ：开启全局一致性（高性能模式）功能。 OFF ：关闭全局一致性（高性能模式）功能。 |
| -ServerWeight | String |  |  |
| ZoneIds | String | cn-hangzhou-i,cn- hangzhou-g | 可用区ID。 |
| InodeUsed | Long | 4,194,304 | 当前inode使用量。 |
| MaintainTime | String | 18:00Z-19:00Z | 集群的可维护时间段，格式为 HH:mmZ- HH:mmZ （UTC时间）。例如 16:00Z- 17:00Z 表示，0点到1点（UTC+08:00）可以进行例行维护。 |
| Engine | String | POLARDB | 集群引擎。 |
| Tags | Array |  | 标签信息详情。 |
| -Key | String | test | 标签键。 |
| -Value | String | MySQL | 标签值。 |
| BlktagTotal | Long | 7,864,320 | 文件系统最大blktag数。 |
| StorageType | String | HighPerformance | 存储类型，取值固定为HighPerformance 。 |
| RequestId | String | 074467EF-86B9- 4C23-ACBF- E9B81A****** | 请求ID。 |
| VPCId | String | vpc- ******************* | 专有网络ID。 |
| DBClusterStatus | String | Running | 集群状态。 |
| VSwitchId | String | vsw- ********************* | 虚拟交换机ID。 |
| DBClusterDescri ption | String | test | 集群描述。 |
| Expired | String | false | 集群是否到期。 仅付费方式为Prepaid （包年包月）的集群支持返回该参数。 |

|  | HH:mmZ |
|---|---|
|  | 17:00Z |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ProxyCpuCores | String | 4 | 数据库代理CPU核数。 |
| PayType | String | Prepaid | 付费类型。取值范围： Postpaid ：按量付费。 Prepaid ：预付费（包年包月）。 |
| LockMode | String | Unlock | 锁定模式，取值范围： Unlock ：未锁定。 ManualLock ：手动触发锁定。 LockByExpiration ：集群过期自动锁定。 |
| StorageUsed | Long | 3012558848 | 存储空间的使用量，单位为Byte。 |
| InodeTotal | Long | 6,291,456 | 文件系统最大inode数。 |
| IsProxyLatestVe rsion | Boolean | false | 是否为数据库代理最新版本，取值范围如下： true ：是 false ：否 |
| StorageSpace | Long | 50 | 按空间计费（包年包月）的存储空间。单位：GB。 |
| DBVersionStatu s | String | Stable | 当前数据库小版本状态，取值范围如下： Stable ：当前版本状态稳定。 Old ：当前版本过旧，建议升级到最新版本。 HighRisk ：当前版本有严重缺陷，请立即升级到最新的版本。 |
| ServerlessType | String | AgileServerless | Serverless类型。当前取值固定为AgileServerless （敏态）。 |
| CreationTime | String | 2020-08- 14T05:58:42Z | 集群创建时间。 |
| SubCategory | String | Exclusive | 计算节点的规格类型，取值范围如下： Exclusive ：独享规格 General ：通用规格仅PolarDB MySQL版且产品系列为集群版时， 支持返回该参数。 |
| SQLSize | Long | 0 | SQL的存储量，单位为Byte。若数值为-1，则表示没有数据。 |
| RegionId | String | cn-hangzhou | 地域ID。 |

| P I | olarDB MySQL集参考 | 群版开发指南·AP |  | 云原生数据库 |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ProxyType | String | Exclusive | 数据库代理类型，取值范围： Exclusive ：企业独享版 General ：企业通用版 |
| ExpireTime | String | 2020-11- 14T16:00:00Z | 集群到期时间。 仅付费方式为Prepaid （包年包月）的集群会返回具体参数值，Postpaid （按量付费）集群则返回空值。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterAttribute &DBClusterId=pc-*****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "DeletionLock":0,
 "Category":"Normal",
 "ResourceGroupId":"rg-***************",
 "StoragePayType":"Prepaid",
 "DataLevel1BackupChainSize":74448896,
 "DBClusterId":"pc-*****************",
 "ProxyStatus":"Running",
 "DBType":"MySQL",
 "DBClusterNetworkType":"VPC",
 "BlktagUsed":5242880,
 "ProxyStandardCpuCores":"2",
 "IsLatestVersion":false,
 "StorageMax":10995116277760,
 "DBVersion":"8.0",
 "DBNodes":{
  "DBNodeStatus":"Running",
  "ZoneId":"cn-hangzhou-i",
  "MaxConnections":8000,
  "AddedCpuCores":"6",
  "DBNodeRole":"Reader",
  "ImciSwitch":"ON",
  "DBNodeId":"pi-****************",
  "MaxIOPS":32000,
  "DBNodeClass":"polar.mysql.x4.large",
  "CreationTime":"2020-03-23T21:35:43Z",
  "SccMode":"ON",
  "MasterId":"pi-bp18z52akld3*****",
  "FailoverPriority":1,
  "HotReplicaMode":"ON",
  "ServerWeight":""
```

云原生数据库 I参考

```json
 },
 "ZoneIds":"cn-hangzhou-i,cn-hangzhou-g",
 "InodeUsed":4194304,
 "MaintainTime":"18:00Z-19:00Z",
 "Engine":"POLARDB",
 "Tags":{
  "Value":"MySQL",
  "Key":"test"
 },
 "BlktagTotal":7864320,
 "StorageType":"HighPerformance",
 "RequestId":"074467EF-86B9-4C23-ACBF-E9B81A******",
 "VPCId":"vpc-*******************",
 "DBClusterStatus":"Running",
 "VSwitchId":"vsw-*********************",
 "DBClusterDescription":"test",
 "Expired":"false",
 "ProxyCpuCores":"4",
 "PayType":"Prepaid",
 "LockMode":"Unlock",
 "StorageUsed":3012558848,
 "InodeTotal":6291456,
 "IsProxyLatestVersion":false,
 "StorageSpace":50,
 "DBVersionStatus":"Stable",
 "ServerlessType":"AgileServerless",
 "CreationTime":"2020-08-14T05:58:42Z",
 "SubCategory":"Exclusive",
 "SQLSize":0,
 "RegionId":"cn-hangzhou",
 "ProxyType":"Exclusive",
 "ExpireTime":"2020-11-14T16:00:00Z"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterParameters

调用ModifyDBClusterParameters接口修改PolarDB集群的参数或将已有的参数模板应用到目标集群上。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 |  | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query |  | 是 | pc-************** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |
| Parameters | String | Query |  |  |  |  | 参数及其值的JSON串，参数的值都是字符串类型，例如 {"wait timeout":"86" _ |  |  |
|  |  |  |  |  |  |  |  | {"wait timeout":"86" _ |  |
|  |  |  |  |  |  |  | ,"innodb old blocks tim _ _ _ |  |  |
|  |  |  |  |  |  |  | e":"10"} |  |  |
|  |  |  |  | 否 | {"wait timeout":"86","inno _ db old blocks time":"10"} _ _ _ |  |  |  |  |
| Parameter GroupId | String | Query |  | 否 | pcpg-************** |  | 参数模板ID。 您可以通过 DescribeParame terGroups 接口查看参数模板ID。 您需在该参数或 Parameters 参数中选择一个传入。 仅PolarDB MySQL版支持该参数。 |  |  |

|  |  |  | DescribeDBCluste |  |
|---|---|---|---|---|
| **** |  | rs |  |  |

|  |  |  | DescribeDBClus |  |
|---|---|---|---|---|
|  |  | terParameters |  |  |

|  |  |  | DescribeParame |  |
|---|---|---|---|---|
|  |  | terGroups |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlannedSta rtTime | String | Query | 否 | 2022-04-28T14:00:00Z | 开始执行定时（即在目标时间段内执行）任务的最早时间。 格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行任务。 |
| PlannedEn dTime | String | Query | 否 | 2022-04-28T14:30:00Z | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |
| FromTimeS ervice | Boole an | Query | 否 | false | 立即执行或定时执行修改参数并重启集群。取值： false（默认值）：定时执行 true：立即执行 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

| 14:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

| 参考 |  |  |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | C5D526E5-91B5- 48B8-B980- FE07FF****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | The specified parameters are invalid. |
| 400 | MinorVersionNotSup port | MinorVersionNotSupport | Custins minor version does not support current action. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterSSL

调用ModifyDBClusterSSL接口开通、关闭PolarDB集群的SSL加密或更新PolarDB集群的CA证书。

**请求头**

云原生数据库 I参考该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 |
| SSLEnabled | String | Query | 否 | Enable | 修改SSL状态，取值： Disable ：关闭SSL加密。 Enable ：开启SSL加密。 Update ：更新CA证书。 开启SSL加密或更新CA 证书后，需要下载和配置证书。 |
| DBEndpoin tId | String | Query | 否 | pe-****************** | 连接地址ID。 若目标集群为 PolarDB MySQL版， 该参数必填。 若目标集群为PolarDB PostgreSQL版或PolarDB PostgreSQL版（兼容 Oracle），无需传入该参数，默认所有地址开启SSL 加密。 |
| NetType | String | Query | 否 | Public | 连接地址的网络类型，需要与DBEndpointId 参数传入的连接地址的网络类型保持一致，取值： Public ：公网 Private ：私网 Inner ：私网（经典网络） 若目标集群为 PolarDB MySQL版， 该参数必填。 若目标集群为PolarDB PostgreSQL版或PolarDB PostgreSQL版（兼容 Oracle），无需传入该参数，默认所有地址开启SSL 加密。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SSLAutoRot ate | String | Query | 否 | Enable | 是否开启SSL证书自动轮转， 取值： Enable ：开启 Disable ：关闭 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A94B1755-6D8B- 4E27-BF3C- 8562BC****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterTDE

调用ModifyDBClusterTDE接口开启PolarDB MySQL版集群的TDE功能或修改加密方式。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

云原生数据库 I参考

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 |
| TDEStatus | String | Query | 是 | Enable | 修改TDE状态。取值固定为Enable 。 |
| RoleArn | String | Query | 否 | acs:ram::1406926*****:rol e/aliyunrdsinstanceencrypt iondefaultrole | 角色的全局资源描述符，用来指定具体角色。 |
| Encryption Key | String | Query | 否 | 749c1df7-****-****-****- ********* | 自定义密钥ID。 |
| EncryptNe wTables | String | Query | 否 | ON | 是否开启自动加密所有新建的表。取值： ON ：开启 OFF ：关闭 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5F859238-2A36- 4A8D-BD0F- 732112****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "TDEStatus":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidTDEstatus | InvalidTDEStatus.AlreadyEnabled | TDE has already enabled in the this cluster. |
| 400 | InvalidDBType.Malfor med | InvalidDBType.Malformed | The Specified DBType is not valid. |
| 403 | UnsupportedKmsSer vice.NotEnabled | UnsupportedKmsService.NotEnab led | KMS service is not enabled. |
| 403 | OperationDenied.DB NodeType | OperationDenied.DBNodeType | The operation is not permitted due to type of node. |
| 403 | IncorrectGdnState | IncorrectGdnState | db instance %s status is not available:%s. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBEndpointAddress

调用ModifyDBEndpointAddress接口修改PolarDB集群的连接地址，包括主地址、默认集群地址、自定义集群地址和私有域名。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
| DBEndpoin tId | String | Query | 是 | pe-**************** |  | 连接地址ID。 您可以通过接口 DescribeDBCluste rEndpoints 查询连接地址ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  |  |  | rEndpoints |  |  |

|  |  |  | DescribeDBCluste |  |
|---|---|---|---|---|
| ***** |  | rs |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NetType | String | Query | 是 | Public | 连接地址的网络类型，取值范围如下： Public ：公网 Private ：私网 <props="china">- Inner ：经典网络 <props="china">仅 PolarDB MySQL版集群支持经典网络类型。 |
| Connection StringPrefix | String | Query | 否 | example | 新的连接地址前缀，需满足如下条件： 由小写字母、数字、中划线 （-）组成。 以字母开头，以数字或字母结尾。 长度为6~30个字符。 |
| PrivateZon eAddressPr efix | String | Query | 否 | aliyundoc | 私有域名前缀。需满足如下条件： 由小写字母、数字、中划线 （-）组成。 以字母开头，以数字或字母结尾。 长度为6~30个字符。 对于PolarDB的每一个私网地址，均可以绑定一个用户的私有域名，该域名仅在当前地域内指定的VPC 中生效。私有域名实际上是通过 PrivateZone管理的，通过CNAME映射到PolarDB自带的私网地址上，该功能 PrivateZone会收取少量费用。 仅NetType=Private 时该参数有意义。 |
| PrivateZon eName | String | Query | 否 | aliyundoc.com | 私有域名Zone名称。 仅NetType=Privat e 时该参数有意义。 |
| Port | String | Query | 否 | 3306 | 端口号，取值范围为3000～ 5999。 仅PolarDB MySQL版集群支持该参数，若该参数留空，则默认端口号为3306。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBEndpointId":"null", "NetType":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBNodeClass

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| ModifyType | String | Query | 是 | Upgrade | 变更类型，取值范围如下： Upgrade ：升级规格 Downgrade ：降级规格 |
| DBNodeTar getClass | String | Query | 是 | polar.mysql.x4.large | 所有节点的目标规格。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）升级配置任务的最早时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 仅当 ModifyType 取值为 Upgrade 时， 该参数生效。 开始时间的取值范围为未来 24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ，此处允许填入的开始时间范围为 2021-01- 14T09:00:00Z ~ 2021 -01-15T09:00:00Z 。 若该参数留空，默认立即执行升级配置任务。 |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:00:00Z |  |  |

|  |  |  | 2021-01- |  |  |  |
|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |
|  |  |  |  | ~ | 2021 |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z |  | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |  |  |
|  |  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  |  | DDThh:mm:ssZ |  |  |
| SubCategor y | String | Query | 否 | normal general _ |  | 集群子系列。取值范围如下： normal exclusive ： _ 独享规格 normal general ：通 _ 用规格 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |
| StorageSpa ce | Long | Query | 否 |  |  |  |  |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 685F028C-4FCD- 407D-A559- 072D63****** | 请求ID。 |
| DBClusterId | String | pc-************* | 数据库集群ID。 |
| OrderId | String | 2035629****** | 订单ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null", "ModifyType":"null", "DBNodeTargetClass":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | OperationDenied.Ro EqualSpec | OperationDenied.RoEqualSpec | must exist at least ro class equal with rw |

### ModifyLogBackupPolicy

调用ModifyLogBackupPolicy接口修改PolarDB集群的日志备份保留策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ****** |  | rs |  |  |
| LogBackup RetentionP eriod | String | Query | 否 | 3 |  | 日志保留周期，取值范围如下： 3～7300：日志保留周期， 单位为天。 -1：永久保留。 |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| LogBackup AnotherRe gionRegion | String | Query | 否 | cn-hangzhou | 日志备份跨地域备份区域。 |
| LogBackup AnotherRe gionRetenti onPeriod | String | Query | 否 | 30 | 日志备份跨地域备份保留周期。取值范围如下： 0 ：关闭日志备份跨地域备份功能。 30～7300 ：日志备份跨地域备份保留周期，单位为天。 -1 ：永久保留。 创建集群时，默认取值为0 ，即关闭日志备份跨地域备份功能。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 345174B4-FAB3- 412E-A326- BEDDA9****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

云原生数据库 I参考

### ModifyMaskingRules

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 |  | 位置 | 是否必选 |  | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String |  | Query | 是 |  | pc-***************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |
| RuleName | String |  | Query | 否 |  | testrule |  | 脱敏规则名称。一次仅支持输入一个规则名称。 您可以通过接口 DescribeMaskin gRules 查看目标集群下的所有脱敏规则详情，包括规则名称。 若输入的规则名称不存在于当前集群中，系统会自动根据该名称和 RuleConfig 值创建一个新的脱敏规则。 |  |  |
|  |  |  |  |  |  |  |  | 需要修改的脱敏规则的配置参数及其值的JSON串，参数的值都是字符串类型，例如： {"auto": |  |  |
|  |  |  |  |  |  |  |  |  |  | {"auto": |
|  |  |  |  |  |  |  |  | {"databases": ["db1"], |  |  |
|  |  |  |  |  |  |  |  | "tables": ["tb1"], |  |  |
|  |  |  |  |  |  |  |  | "columns": ["c1,c2"] |  |  |
|  |  |  |  |  |  |  |  | }, "description": |  |  |
|  |  |  |  |  |  |  |  | "This rule will be |  |  |
|  |  |  |  |  |  |  |  | applied to the columns |  |  |
|  |  |  |  |  |  |  |  | c1 and c2 in table |  |  |
|  |  |  |  |  |  |  |  | t1", "enabled": true, |  |  |
|  |  |  |  |  |  |  |  | "applies to": _ |  |  |
|  |  |  |  |  |  |  |  | ["user"]} |  |  |
|  |  |  |  |  |  |  |  |  | "auto" |  |

|  |  |  | DescribeDBCluste |
|---|---|---|---|
| ******* |  | rs |  |

|  |  |  | DescribeMaskin |  |
|---|---|---|---|---|
|  |  | gRules |  |  |

云原生数据库 I参考

|  | 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 据库名称，多个名称间用英说明文逗号（,）分隔。若该参数 |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | 留空，表示该规则将应用到当前集群中的所有数据库。 "tables" ：选填。需要应用当前规则的表名称， 支持输入多个表库名称，多 |  |  |
|  | RuleConfig | String | Query | 否 | {"auto": {"databases": ["db1"], "tables": ["tb1"], "columns": ["c1,c2"] }, "description": "This rule will be applied to the columns c1 and c2 in table t1", "enabled": true, "applies to": ["user"]} _ | 个名称间用英文逗号（,）分隔。若该参数留空，表示该规则将应用到当前集群中的所有表。 "columns" ：必填。需要应用当前规则的字段名称，支持输入多个字段名称，多个名称间用英文逗号 （,）分隔。 "description" ：选填。脱敏规则的描述，选填。字符长度不能超过64个字符。 "enabled" ：必填。启用或禁用目标脱敏规则。取值为true （启用） 或false （禁用）。 "applies to" ：需要 _ 应用当前规则的数据库账号名称，支持输入多个数据库账号名，多个账号间用英文逗号（,）分隔。 "exempted" ：不需要应用当前规则的数据库账号名称，支持输入多个数据库账号名，多个账号间用英文逗号（,）分隔。 若输入了 RuleName 参数， RuleConfig 参数必传。 "applies to" 和 "e _ xempted" ，需要选择其中的一个进行输入。 |  |  |
|  |  |  |  |  |  |  | "e |  |
|  | RuleNameL ist | String | Query | 否 | testrule | 脱敏规则名称列表。支持一次输入一个或多个规则名称，多个名称间用英文逗号（,）分隔。 RuleName 和 Rule NameList 参数，需要选择其中的一个进行输入。 |  |  |

|  | "applies to" _ |
|---|---|
| xempted" |  |

|  |  |  | RuleName |
|---|---|---|---|
|  |  | NameList |  |

| Rule |  |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Enable | String | Query | 否 | true | 启用或禁用目标脱敏规则。取值范围如下： true ：启用。 false ：禁用。 仅当 RuleNameList 有参数值输入时，该参数生效。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 99B355CE-526C- 478B-B730- AD9D7C****** | 请求ID。 |
| Message | String | Message | 请求返回消息。 请求成功时该参数返回Successful，请求失败时会返回请求异常信息（如错误码等）。 |
| Success | Boolean | true | 请求结果。取值： true ：请求成功。 false ：请求失败。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "Message":"",
 "Success":""
}
```

### RestoreTable

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 云原生数据库 I参考

**请求语法**

```
  HTTP/1.1
```

**请求参数**

|  |  | 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  | SecurityTo ken | String | Query | 否 |  |  |  |  |  |  |  |
|  |  | DBClusterI d | String | Query | 是 |  | pc-bp*************** |  |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查询账号下所有集群的信息详情。 |  |  |
|  |  |  |  |  |  |  |  |  |  | 需要还原的目标库表信息的 JSON串，库表信息的值都是字符串类型。 例如， [ { |  |  |
|  |  |  |  |  |  |  |  |  |  |  | [ { |  |
|  |  |  |  |  |  |  |  |  |  | "tables":[ { |  |  |
|  |  |  |  |  |  |  |  |  |  | "name":"testtb", |  |  |
|  |  |  |  |  |  |  |  |  |  | "type":"table", |  |  |
|  |  |  |  |  |  |  |  |  |  | "newname":"testtb resto _ |  |  |
|  |  |  |  |  |  |  |  |  |  | re" } ], |  |  |
|  |  |  |  |  |  |  |  |  |  | "name":"testdb", |  |  |
|  |  |  |  |  |  |  | [ { "tables":[ { |  |  |  |  |  |
|  |  |  |  |  |  |  | "name":"testtb", |  |  | "type":"db", |  |  |
|  |  |  |  |  |  |  | "type":"table", |  |  | "newname":"testdb resto _ |  |  |
|  |  | TableMeta | String | Query | 是 |  | "newname":"testtb restore _ |  |  | re" } ] |  |  |
|  |  |  |  |  |  |  | " } ], "name":"testdb", "type":"db", "newname":"testdb restor _ e" } ] |  |  |  |  |  |
|  |  | BackupId | String | Query | 否 |  | 111111 |  |  | 备份集ID。 若需要按备份集还原目标库表，该参数必传。您可以通过 DescribeBackups 接口查看备份集ID。 |  |  |

|  |  |  | DescribeDBCluste |  |
|---|---|---|---|---|
|  |  | rs |  |  |

| _ |  |  |
|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RestoreTim e | String | Query | 否 | 2020-10-04T01:40:00Z | 还原时间点，格式为YYYY- MM-DDThh:mmZ（UTC时间）。 若需要按时间点还原，该参数必填。 仅支持恢复到7天内的任意时间点。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0C47508C-9DC8- 455B-985E- 2F2FA8****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "TableMeta":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRestoreType.F ormat | InvalidRestoreType.Format | Specified restore type is not valid. |
| 400 | InvalidRestoreTime.F ormat | InvalidRestoreTime.Format | Specified restore time is not valid. |
| 400 | InvalidBackupSetID. NotFound | InvalidBackupSetID.NotFound | Specified backup set ID does not exist. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | IncorrectBackupSetS tate | IncorrectBackupSetState | Current backup set state does not support operations. |
| 400 | InvalidDBName.Dupli cate | InvalidDBName.Duplicate | Specified DB name already exists in the This instance. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | InsufficientResource Capacity | InsufficientResourceCapacity | There is insufficient capacity available for the requested instance. |
| 400 | InvalidRestoreType.N otFound | InvalidRestoreType.NotFound | At least one of BackupId and RestoreTime is malformed. |
| 400 | MissingUserID | MissingUserID | The request is missing a user id _ parameter. |
| 400 | MissingUID | MissingUID | The request is missing a uid parameter. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidBackup.NotFo und | InvalidBackup.NotFound | The available backup does not exist in recovery time. |

### DescribeCharacterSetName

调用DescribeCharacterSetName接口查看PolarDB MySQL版数据库支持的字符集列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看可用地域。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 否 | pc-**************** |  | 集群ID。 当前仅支持查看PolarDB MySQL版集群数据库支持的字符集列表。若输入 PolarDB PostgreSQL版集群或PolarDB PostgreSQL版（兼容 Oracle）集群的集群 ID， CharacterSetNa meItems 会返回空值。 |  |  |  |
|  |  |  |  |  |  |  |  | CharacterSetNa |  |
|  |  |  |  |  |  |  | meItems |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 34458CD3-33E0- 4624-BFEF- 840C15****** | 请求ID。 |
| Engine | String | POLARDB | 集群引擎。 |
| CharacterSetNa meItems | String |  |  |

**示例**

请求示例

```json
  HTTP/1.1
{ "RegionId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "Engine":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |

### DescribeBackupPolicy

调用DescribeBackupPolicy接口查看PolarDB集群的自动备份策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | *** |  | rs |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DataLevel2Back upAnotherRegio nRegion | String | cn-hangzhou | 二级备份跨地域备份区域。 |
| DataLevel1Back upRetentionPeri od | String | 7 | 一级备份保留周期，取值范围为3~14，单位为天。 |
| DataLevel2Back upAnotherRegio nRetentionPerio d | String | 30 | 二级备份跨地域备份保留周期。取值范围如下： 0 ：关闭二级备份功能。 30～7300 ：二级备份保留周期，单位为天。 1 ：二级备份永久保留。 创建集群时，默认取值为0 ，即关闭二级备份跨地域备份功能。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | EADFCE0F-9FB5- 4685-B395- 1440B****** | 请求ID。 |
| PreferredBacku pTime | String | 07:00Z-08:00Z | 执行自动备份的时间段，格式为 HH:mmZ- HH:mmZ （UTC时间）。 |
| BackupRetentio nPolicyOnCluste rDeletion | String | NONE | 删除集群时是否保留备份： ALL ：永久保留全部备份。 LATEST ：永久保留最后一个备份。 NONE （默认）：不保留备份集。 |
| BackupFrequen cy | String | Normal | 备份频率，取值如下： Normal （默认）：常规备份，每天定时备份一次。 2/24H ：增强备份，每2小时备份一次。 3/24H ：增强备份，每3小时备份一次。 4/24H ：增强备份，每4小时备份一次。 开启增强备份后，备份完成时间在24小时内的备份会全部保留。超过24小时的，系统将仅保留每日00:00点后完成的第一个备份， 其他均被删除。 开启增强备份后，备份周期PreferredBackupPeriod 参数会默认选择一周内的所有天数（即从周一至周日）。 |
| DataLevel1Back upTime | String | 15:00Z-16:00Z | 执行自动备份的时间段，格式为 hh:mmZ- hh:mmZ （UTC时间），且输入的数值必须为间隔1 个小时的整点，如 14:00Z-15:00Z 。 PolarDB PostgreSQL版（兼容Oracle）、 PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL版所在的地域不支持跨地域备份功能，将不支持该参数。 |
| PreferredNextB ackupTime | String | 2020-11-16T07:30Z | 下一次备份的时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |
| DataLevel2Back upRetentionPeri od | String | 0 | 二级备份保留周期，取值范围如下： 0：关闭二级备份功能。 30～7300：二级备份保留周期，单位为天。 -1：二级备份永久保留。 创建集群时，默认取值为0 ，即关闭二级备份功能。 |

|  | HH:mmZ |
|---|---|

|  | hh:mmZ |
|---|---|

| 7:30Z | DDThh:mmZ |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PreferredBacku pPeriod | String | Monday,Tuesday,We dnesday,Thursday,Fri day,Saturday,Sunday | 数据备份周期，取值范围如下： Monday：周一 Tuesday：周二 Wednesday：周三 Thursday：周四 Friday：周五 Saturday：周六 Sunday：周日 |
| DataLevel1Back upFrequency | String | Normal | 备份频率，取值如下： Normal （默认）：常规备份，每天定时备份一次。 2/24H ：高频备份，每2小时备份一次。 3/24H ：高频备份，每3小时备份一次。 4/24H ：高频备份，每4小时备份一次。 PolarDB PostgreSQL版（兼容Oracle）、 PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL版所在的地域不支持跨地域备份功能，将不支持该参数。 |
| DataLevel2Back upPeriod | String | Monday,Tuesday | 二级备份周期，取值范围如下： Monday ：周一 Tuesday ：周二 Wednesday ：周三 Thursday ：周四 Friday ：周五 Saturday ：周六 Sunday ：周日至少需要选择2天，多个值之间用英文逗号 （,）隔开。 PolarDB PostgreSQL版（兼容Oracle）、 PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL版所在的地域不支持跨地域备份功能，将不支持该参数。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DataLevel1Back upPeriod | String | Monday,Tuesday | 一级备份周期，取值范围如下： Monday ：周一 Tuesday ：周二 Wednesday ：周三 Thursday ：周四 Friday ：周五 Saturday ：周六 Sunday ：周日至少需要选择2天，多个值之间用英文逗号 （,）隔开。 PolarDB PostgreSQL版（兼容Oracle）、 PolarDB PostgreSQL版不支持该参数。 如果您的PolarDB MySQL版所在的地域不支持跨地域备份功能，将不支持该参数。 |
| BackupRetentio nPeriod | Integer |  |  |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "DataLevel2BackupAnotherRegionRegion":"",
 "DataLevel1BackupRetentionPeriod":"",
 "DataLevel2BackupAnotherRegionRetentionPeriod":"",
 "RequestId":"",
 "PreferredBackupTime":"",
 "BackupRetentionPolicyOnClusterDeletion":"",
 "BackupFrequency":"",
 "DataLevel1BackupTime":"",
 "PreferredNextBackupTime":"",
 "DataLevel2BackupRetentionPeriod":"",
 "PreferredBackupPeriod":"",
 "DataLevel1BackupFrequency":"",
 "DataLevel2BackupPeriod":"",
 "DataLevel1BackupPeriod":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### DeleteParameterGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou |  | 地域ID。 您可以通过接口 DescribeRegions 查看可用地域。 |  |  |  |
| Parameter GroupId | String | Query | 是 | pcpg-************** |  | 参数模板ID。 您可以通过接口 DescribeParamete rGroups 查看参数模板 ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeParamete |  |
|  |  |  |  |  |  |  | rGroups |  |  |
| ResourceGr oupId | String | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4F7195E7-5F74- 479D-AF59- 1B4BF9****** | 请求ID。 |

**示例**

云原生数据库 I参考请求示例

```json
  HTTP/1.1
{ "RegionId":"null", "ParameterGroupId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |
| 400 | InvalidParameterGro upId.Malformed | InvalidParameterGroupId.Malform ed | The Specified parameter ParameterGroupId is not valid. |

### DeleteMaskingRules

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| RuleNameL ist | String | Query | 是 | testrule |  | 需要删除的脱敏规则名称。支持输入多个规则名称进行批量删除，多个名称间用英文逗号 （,）分隔。 您可以通过 DescribeMaskingR ules 接口查看目标集群下所有脱敏规则的详情，包括规则名称。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeMaskingR |  |
|  |  |  |  |  |  |  | ules |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-***************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  |  |  | rs |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2BCEE25B-797C- 426B-BA7B- D28CCF****** | 请求ID。 |
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回 Successful ，请求失败时会返回请求异常信息（如错误码等）。 |
| Success | Boolean | true | 请求结果。取值： true ：请求成功。 false ：请求失败。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "RuleNameList":"null", "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "Message":"",
 "Success":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |

### DeleteDBEndpointAddress

调用DeleteDBEndpointAddress接口释放PolarDB集群的公网或经典网络连接地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
| DBEndpoin tId | String | Query | 是 | pe-*************** |  | 连接地址ID。 您可以通过接口 DescribeDBCluste rEndpoints 查询 DBEndpointId。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  |  |  | rEndpoints |  |  |
| NetType | String | Query | 是 | Public |  | <props="intl">连接地址的网络类型，仅支持Public （公网）类型。 <props="china">连接地址的网络类型，取值范围如下： <props="china">Publi c ：公网。 <props="china">Inne r ：经典网络。 |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |  |  |

|  |  |  | DescribeDBCluste |  |
|---|---|---|---|---|
| ** |  | rs |  |  |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBEndpointId":"null", "NetType":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBEndpointId. Malformed | InvalidDBEndpointId.Malformed | The specified parameter DBEndpointId is not valid. |
| 400 | NetTypeUsed.Gdn | NetTypeUsed.Gdn | Specified endpoint?s net type is used by global database. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | EndpointStatus.NotS upport | EndpointStatus.NotSupport | Current endpoint status does not support this operation. |

云原生数据库 I参考

### DeleteBackup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| BackupId | String | Query | 是 | 11111111 | 备份ID，多个备份之间用英文逗号（,）分隔。 您可以通过 DescribeBackups 接口查询BackupId。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3CF4F9FE-BF77- 4739-8D68- B8DF5D****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null", "BackupId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidBackupSetID. NotFound | InvalidBackupSetID.NotFound | The specified parameter BackupId is not valid. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### CreateDBNodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| EndpointBi ndList | String | Query | 否 | pe-****************,pe- **************** | 指定新增节点需要加入的集群连接地址的地址ID。若需要同时加入多个连接地址，多个连接地址ID间用英文逗号（,）分隔。 您可以通过调用 DescribeDBClus terEndpoints 接口查看集群连接地址的详情，包括连接地址ID。 支持填入默认集群连接地址和自定义集群连接地址的地址ID。 若该参数留空，默认将新增节点加入所有开启了新节点自动加入功能 （即 AutoAddNewNodes 取值为 Enable ）的集群连接地址。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）新增节点任务的最早时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行新增节点任务。 |

|  |  | terEndpoints |
|---|---|---|

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z |  | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |  |  |
|  |  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  |  | DDThh:mm:ssZ |  |  |
| DBNode | Repea tList | Query | 是 |  |  | 新增节点的信息。 |  |  |
| ImciSwitch | String | Query | 否 | ON |  | 是否开启列存索引。取值范围： ON ：开启 OFF ：关闭（默认值） PolarDB PostgreSQL版 （兼容Oracle）和 PolarDB PostgreSQL版不支持该参数。 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |
| NodeType | String | Query | 否 |  |  |  |  |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E053E730-5755- 4AA9-AA9D- A47867****** | 请求ID。 |
| DBClusterId | String | pc-*************** | 数据库集群ID。 |
| OrderId | String | 2148126708***** | 订单ID。 |

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBNodeIds | String |  |  |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBNode":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ORDER.ARREARAGE | ORDER.ARREARAGE | ????????????????????????? |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### CreateDBEndpointAddress

调用CreateDBEndpointAddress接口创建PolarDB集群的公网或经典网络连接地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBEndpoin tId | String | Query | 是 | pe-************** |  | 连接地址ID。 可通过接口 DescribeDBCluste rEndpoints 查询连接地址详情。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  |  |  | rEndpoints |  |  |
| Connection StringPrefix | String | Query | 否 | test-1 |  | 新的连接地址前缀。连接地址前缀需满足如下条件： 由小写字母、数字、中划线 （-）组成。 以字母开头，以数字或字母结尾。 长度为6~40个字符。 |  |  |  |
| NetType | String | Query | 是 | Public |  | 新增连接地址的网络类型，取值范围如下： Public ：公网。 Inner ：经典网络。 对于PolarDB MySQL版集群，允许传入Public 和Inner ；对于PolarDB PostgreSQL版和 PolarDB PostgreSQL版 （兼容Oracle）集群， 只允许传入Public 。 |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6BD9CDE4-5E7B- 4BF3-9BB8- 83C73E****** | 请求ID。 |

**示例**

云原生数据库 I参考请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBEndpointId":"null", "NetType":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | EndpointStatus.NotS upport | EndpointStatus.NotSupport | Current endpoint status does not support this operation. |
| 400 | NetTypeExists | NetTypeExists | Specified net type already existed. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### CreateDBCluster

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看可用地域。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| ZoneId | String | Query | 否 | cn-hangzhou-g | 可用区ID。 您可以通过 DescribeRegions 接口查看可选的可用区。 |  |  |
| DBType | String | Query | 是 | MySQL | 数据库引擎类型，取值范围如下： MySQL PostgreSQL Oracle |  |  |
| DBVersion | String | Query | 是 | 5.6 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 5.7 8.0 PostgreSQL版本号取值范围如下： 11 14 Oracle版本号取值为11 。 |  |  |
| DBNodeCla ss | String | Query | 是 | polar.mysql.x2.medium | 节点规格。 如需创建Serverless集群，请传入polar.mysql.sl.sm all 。 |  |  |
| ClusterNet workType | String | Query | 否 | VPC | 集群网络类型，当前仅支持专有网络，取值固定为VPC 。 |  |  |
| DBClusterD escription | String | Query | 否 | test | 集群名称，集群名称需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 |  |  |
|  |  |  |  |  |  | https |  |
| PayType | String | Query | 是 | Postpaid | 付费类型，取值范围如下： Postpaid ：按量付费 Prepaid ：预付费（包年包月） |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| AutoRenew | Boole an | Query | 否 | true | 是否自动续费，取值范围如下： true ：自动续费。 false ：不自动续费。 默认为false 。 当参数PayType 取值为Prepaid 时，该参数才生效。 |  |  |
| Period | String | Query | 否 | Month | 若付费类型为Prepaid 时， 该参数为必传参数。指定预付费集群为包年或包月类型。 Year ：包年。即选择包年包月时，单位为年。 Month ：包月。即选择包年包月时，单位为月。 |  |  |
| UsedTime | String | Query | 否 | 1 | 当Period 为Month 时 ，UsedTime 取值为整数类型，取值范围为 [1- 9] 。 当Period 为Year 时， UsedTime 取值为整数类型，取值范围为 [1- 3] 。 |  |  |
|  |  |  |  |  |  | [1- |  |
| VPCId | String | Query | 否 | vpc-********** | 专有网络ID。 |  |  |
| VSwitchId | String | Query | 否 | vsw-********** | 虚拟交换机ID。 如果已选择VPCId，则 VSwitchId必选。 |  |  |

|  | 9] |
|---|---|

|  | 3] |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CreationOp tion | String | Query | 否 | Normal | 创建方式，取值范围如下： Normal ：创建一个全新的PolarDB集群。 CloneFromPolarDB ：从现有PolarDB集群克隆数据到新的PolarDB集群。 CloneFromRDS ：从现有RDS实例克隆数据到新的PolarDB集群。 MigrationFromRDS ：从现有RDS实例迁移数据到新的PolarDB集群。创建的PolarDB集群是只读模式，且默认开启Binlog。 CreateGdnStandby ：创建一个从集群。 <props="china">* UpgradeFromPolarDB ：从PolarDB升级迁移。 默认为Normal 。 当DBType 为MySQ L 且DBVersion 为 8.0 时，本参数取值可以为CreateGdnStandb y 。 |
| SourceRes ourceId | String | Query | 否 | rm-************* | 源RDS实例ID或源PolarDB集群ID。仅当CreationOption 为Mi grationFromRDS 、Clo neFromRDS 或CloneFr omPolarDB 时，该参数必填。 若CreationOption 为 MigrationFromRDS 或CloneFromRDS ， 您需要为本参数传入源RDS 实例ID。源RDS实例版本需为RDS MySQL 5.6 、5.7 或8.0高可用版。 若CreationOption 为C loneFromPolarDB ， 您需要为本参数传入源 PolarDB集群ID。克隆集群和源集群的DBType默认保持一致。例如源集群为 MySQL 8.0，则克隆集群也需设置DBType 为MySQL 且DBVersion 为8.0 。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| CloneDataP oint | String | Query | 否 | LATEST |  | 克隆数据的时间节点，取值： LATEST ：最新时间点的数据。 BackupID ：历史备份集 ID，请传入具体的备份集 ID。 Timestamp ：历史时间点，请传入具体的时间，格式： YYYY-MM- DDThh:mm:ssZ （UTC时间）。 默认为LATEST 。 若CreationOption 为CloneFromRDS ，则本参数取值只能为LATEST 。 |  |  |
|  |  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  |  | DDThh:mm:ssZ |  |  |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 5******************** |  | 用于保证请求的幂等性。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、 不超过64个ASCII 字符。 |  |  |
| ResourceGr oupId | String | Query | 否 | rg-************ |  | 资源组ID。 |  |  |
| SecurityIPLi st | String | Query | 否 | 10.***.***.*** |  | PolarDB集群白名单IP地址。 支持配置多个白名单IP地址，多个IP地址之间使用英文逗号分隔。 |  |  |
| TDEStatus | Boole an | Query | 否 | true |  | 开启TDE加密。取值范围如下： true ：开启。 false ：关闭（默认值）。 仅当DBType 为Post greSQL 或Oracl e 时，本参数生效。 您可以调用 ModifyDBClusterTDE 接口为PolarDB MySQL 集群开启TDE加密。 TDE功能开启后不可关闭。 |  |  |
| GDNId | String | Query | 否 | gdn-*********** |  | 全球数据库网络ID。 当CreationOption 为CreateGdnStandb y 时，本参数必填。 |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| CreationCa tegory | String | Query | 否 | Normal | 产品系列，取值范围如下： Normal ：集群版（默认值） Basic ：单节点 ArchiveNormal ：高压缩引擎（X-Engine） NormalMultimaster ：多主架构集群版 SENormal ：标准版仅当DBType 为MyS QL ， 且DBVersion 为5 .6 、5.7 或8.0 时，支持设置产品系列为Basic 。 仅当DBType 为MySQL ， 且DBVersion 为8.0 时，支持设置产品系列为ArchiveNormal 和N ormalMultimaster 。 仅当DBType 为MySQL ， 且DBMinorVersion 为 8.0.1 时，支持设置产品系列SENormal 。 |
| DefaultTim eZone | String | Query | 否 | SYSTEM | 集群时区（UTC），可选取值范围为**-12:00~+13:00内的所有整点时间， 如 00:00**。默认取值为SYSTEM ，默认时区与 Region所在时区一致。 仅当DBType 为MySQ L 时，该参数生效。 |
| LowerCase TableName s | String | Query | 否 | 1 | 表名是否区分大小写，取值范围如下： 1 ：不区分大小写 0 ：区分大小写默认取值为1 。 仅当DBType 为MySQ L 时，该参数生效。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| BackupRet entionPolic yOnCluster Deletion | String | Query | 否 | NONE |  | 删除集群时备份集保留策略， 取值范围如下： ALL ：永久保留全部备份。 LATEST ：永久保留最后一个备份（删除前自动备份）。 NONE ：集群删除时不保留备份集。 创建集群时，默认取值为NONE ，即集群删除时不保留备份集。 仅当DBType 为MyS QL 时，该参数生效。 Serverless集群不支持该参数。 |  |  |  |
| StorageSpa ce | Intege r | Query | 否 | 50 |  | 按空间计费（包年包月）的存储空间。单位：GB。 PolarDB MySQL标准版存储空间的取值范围： 20~32000。 |  |  |  |
| DBMinorVe rsion | String | Query | 否 | 8.0.1 |  | 数据库引擎小版本号。取值范围如下： 8.0.2 8.0.1 当参数DBType 为MySQ L 且DBVersion 为 8.0 时，该参数才生效。 |  |  |  |
| Parameter GroupId | String | Query | 否 | pcpg-************** |  | 参数模板ID。 您可以通过 DescribeParamete rGroups 接口查看目标地域的参数模板列表，包括参数模板ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeParamete |  |
|  |  |  |  |  | ******* |  | rGroups |  |  |
| Tag | Repea tList | Query | 否 |  |  | 1 |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| StorageTyp e | String | Query | 否 | PSL4 | 企业版存储类型取值如下： PSL5 PSL4 标准版存储类型取值如下： ESSDPL1 ESSDPL2 ESSDPL3 Serverless集群不支持该参数。 |
| DBNodeNu m | Intege r | Query | 否 | 1 | 标准版节点个数。取值如下： 1 （默认）：表示只有1 个读写节点。 2 ：表示有1个只读节点和一个读写节点。 |
| HotStandby Cluster | String | Query | 否 | ON | 是否开启热备集群。取值范围如下： ON （默认）：开启热备集群。 OFF ：关闭热备集群。 STANDBY ：标准版开启热备集群。 标准版集群的默认值为OFF 。 |
| ProxyType | String | Query | 否 | Exclusive | 数据库代理类型，取值范围如下： OFF （默认）：关闭数据库代理。 EXCLUSIVE ：企业独享版 GENERAL ：企业通用版 |
| ProxyClass | String | Query | 否 | polar.maxscale.g2.medium .c | 标准版数据库代理规格。取值如下： polar.maxscale.g2.m edium.c ：2核。 polar.maxscale.g2.lar ge.c ：4核。 polar.maxscale.g2.xla rge.c ：8核。 polar.maxscale.g2.2xl arge.c ：16核。 polar.maxscale.g2.3xl arge.c ：24核。 polar.maxscale.g2.4xl arge.c ：32核。 polar.maxscale.g2.8xl arge.c ：64核。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E56531A4-E552- 40BA-9C58- 137B80****** | 请求ID。 |
| ResourceGroupI d | String | rg-*************** | 资源组ID。 |
| DBClusterId | String | pc- bp1s826a1up****** | 集群ID。 |
| OrderId | String | 211454967****** | 订单ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "RegionId":"null", "DBType":"null", "DBVersion":"null", "DBNodeClass":"null", "PayType":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "ResourceGroupId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidBackupRetenti onPolicyOnClusterDe letion.Malformed | InvalidBackupRetentionPolicyOnC lusterDeletion.Malformed | The specified BackupRetentionPolicyOnCluster Deletion is invalid. |

| olarDB MySQ | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidLowerCaseTab leNames.Malformed | InvalidLowerCaseTableNames.Mal formed | The specified LowerCaseTableNames is invalid. |
| 400 | InvalidLowerCaseTab leNames.Malformed | InvalidLowerCaseTableNames.Mal formed | The specified LowerCaseTableNames value is invalid. |
| 400 | InvalidDefaultTimeZo ne.Malformed | InvalidDefaultTimeZone.Malforme d | The specified DefaultTimeZone is invalid. |
| 400 | Location.FailedGetSu bDomain | Location.FailedGetSubDomain | The specified regionId does not match the zoneId or the zoneId does not exist. |
| 400 | MissParameter.GDNI d | MissParameter.GDNId | The GDNId parameter is required. |
| 400 | EntityNotExist.Resou rceGroup | EntityNotExist.ResourceGroup | The resource group does not exist.. |

### CreateDatabase

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| DBName | String | Query | 是 | testDB | 数据库名称，名称需满足如下要求： 由小写字母、数字、中划线 （-）、下划线（ ）组成。 _ 以字母开头，以字母或数字结尾，最长64个字符。 请勿使用保留关键字作为数据库名称， 如 test 、 mysql 等。 |
| CharacterS etName | String | Query | 是 | utf8 | 字符集。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBDescript ion | String | Query | 否 | testdesc | 数据库备注信息，备注信息需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填；当集群为 PolarDB MySQL版时， 该参数非必填。 |  |  |
|  |  |  |  |  |  | https |  |
| AccountNa me | String | Query | 否 | testacc | 授权访问该数据库的账号名。 可通过接口 DescribeAccounts 查询账号信息。 只支持输入普通账号，高权限账号默认拥有数据库全部权限无需授权。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填；当集群为PolarDB MySQL版时，该参数非必填。 |  |  |
| AccountPri vilege | String | Query | 否 | ReadWrite | 账号权限，取值范围如下： ReadWrite ：读写。 ReadOnly ：只读。 DMLOnly ：只允许 DML。 DDLOnly ：只允许 DDL。 ReadIndex ：只读+索引。 若该参数不填，则默认为ReadWrite 。 该参数仅当AccountName 为非空值时生效。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填； 当集群为PolarDB MySQL 版时，该参数非必填。 |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Collate | String | Query | 否 | C | 语言环境设置，用于指定新建数据库的排序规则。 语言环境必须与CharacterSetNa me 参数设置的字符集兼容。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填；当集群为PolarDB MySQL版时，不支持该参数。 关于该参数的取值范围，请登录PolarDB控制台，在配置与管理 > 数据库管理页签，单击创建数据库进行查看。 |
| Ctype | String | Query | 否 | C | 语言环境设置，用于指定数据库的字符分类。 语言环境必须与CharacterSetNa me 参数设置的字符集兼容。 与Collate 传入信息一致。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填；当集群为PolarDB MySQL版时，该参数非必填。 关于该参数的取值范围，请登录PolarDB控制台，在配置与管理 > 数据库管理页签，单击创建数据库进行查看。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 93E98F25-BE02- 40DA-83E3- F77F8D****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBName":"null", "CharacterSetName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBName.Malf ormed | InvalidDBName.Malformed | The specified parameter DBName is not valid. |
| 400 | Database.AddError | Database.AddError | Instance %s add database minidoc error |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### CreateAccount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |

| olarDB MySQ | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| AccountNa me | String | Query | 是 | testacc | 账号名称，需符合如下要求： 以小写字母开头，以字母或数字结尾。 由小写字母、数字或下划线组成。 长度为2~16个字符。 不能使用某些预留的用户名，如root、admin等。 |  |  |
| AccountPas sword | String | Query | 是 | Test1111 | 账号密码，需符合如下要求： 至少包含大写字母、小写字母、数字或特殊字符中的任意三种。 长度为8~32个字符。 特殊字符为 !@#$%^&* () +-= 。 _ |  |  |
|  |  |  |  |  |  | !@#$%^&* |  |
| AccountTyp e | String | Query | 否 | Normal | 账号类型，取值范围如下： Normal ：普通账号。 Super ：高权限账号。 若该参数留空，则默认创建Super 账号。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，每个集群允许创建多个高权限账号，高权限账号相比普通账号拥有更多权限。 当集群为PolarDB MySQL 版时，每个集群最多只允许创建1个高权限账号，高权限账号相比普通账号拥有更多权限。 |  |  |
| AccountDe scription | String | Query | 否 | testdes | 账号备注说明，需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 |  |  |
| DBName | String | Query | 否 | testdb | 允许目标账号访问的数据库名称，支持传入多个数据库名称，多个数据库名称间用英文逗号（,）分隔。 仅PolarDB MySQL版集群的普通账号支持该参数。 |  |  |

|  | () +-= _ |
|---|---|

|  |  | http:// |
|---|---|---|
|  | :// |  |

| https |  |
|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |
|---|---|---|---|---|---|---|
| AccountPri vilege | String | Query | 否 | ReadWrite | 账号权限，取值范围如下： ReadWrite ：读写 ReadOnly ：只读 DMLOnly ：只允许DML DDLOnly ：只允许DDL ReadIndex ：只读+索引必须要传入 DBName 参数， AccountPrivi lege 才能生效。 若为 DBName 参数传入了多个数据库名称，您需要为目标数据库分别授予相应的权限，多个账号权限间用英文逗号（,）分隔。例如， 需要授权数据库DB1读写权限，授权数据库DB2只读权限，您需要设置 DBName 为 DB1,DB2 ，并设置 AccountPrivilege 为 ReadWrite,ReadOn ly 。 仅PolarDB MySQL版集群的普通账号支持设置该参数。 |  |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |

|  |  | lege |  |
|---|---|---|---|

|  |  |  | AccountPrivilege |  |
|---|---|---|---|---|
|  |  | 置 |  |  |
|  |  |  | 为 |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CED079B7-A408- 41A1-BFF1- EC608E****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null", "AccountPassword":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 400 | EngineMigration.Acti onDisabled | EngineMigration.ActionDisabled | Specified action is disabled while custins is in engine migration. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterPrimaryZone

调用ModifyDBClusterPrimaryZone修改PolarDB集群的主可用区。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | **** |  | rs |  |  |
| ZoneId | String | Query | 是 | cn-hangzhou-g |  | 新的主可用区ID。 可通过接口 DescribeRegions 查看可用的可用区。 |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| VSwitchId | String | Query | 否 | vsw-************** | 目标可用区的虚拟交换机 （VSwitch）ID。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填。 当集群为PolarDB MySQL 版时： 如果目标可用区没有创建过Vswitch，则使用默认的Vswitch，该参数非必填。 如果目标可用区已创建过 Vswitch，该参数必填。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）变更主可用区任务的最早时间。格式为 YYYY- MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行变更主可用区任务。 |

|  |  |  | YYYY- |  |
|---|---|---|---|---|
|  |  | MM- |  |  |
|  |  | DDThh:mm:ssZ |  |  |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z |  | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |  |  |
|  |  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  |  | DDThh:mm:ssZ |  |  |
| FromTimeS ervice | Boole an | Query | 否 | false |  | 立即执行或定时执行更换主可用区。取值： false（默认值）：定时执行 true：立即执行 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | ED12C6FF-3261- 4571-AB57- 3570F6****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyDBClusterPrimaryZone &DBClusterId=pc-************** &ZoneId=cn-hangzhou-g
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"ED12C6FF-3261-4571-AB57-3570F6******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ScheduleTaskExist | ScheduleTaskExist | The specified cluster already has a scheduled task. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### CheckAccountName

调用CheckAccountName接口校验账号名称是否合法或当前集群中是否已存在重名的账号。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ****** |  | rs |  |  |
| AccountNa me | String | Query | 是 | test acc _ |  | 账号名称。 |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 925B84D9-CA72- 432C-95CF- 738C22****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccountName. Duplicate | InvalidAccountName.Duplicate | The specified account name already exists. |

### 查看PolarDB MySQL集群内核版本信

**息**

查看PolarDB MySQL集群当前内核版本的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息（如集群 ID）。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ****** |  | rs |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| DBRevisionVersi on | String | 8.0.1.1.7 | 数据库引擎的修订版本号。 针对PolarDB MySQL版5.6版本的集群，仅发布日期在20200831之后的 Revision Version 信息会被返回，否则该参数为空。 |  |  |
|  |  |  |  | Revision |  |
| RequestId | String | 47921222-0D37- 4133-8C0D- 017DC3****** | 请求ID。 |  |  |
| DBClusterId | String | pc-**************** | 集群ID。 |  |  |
| ProxyRevisionV ersion | String | 2.4.15 | 数据库代理的版本。 |  |  |
| DBLatestVersio n | String | 8.0.1.1.16 | 数据库内核引擎的最新版本。 |  |  |
| ProxyLatestVers ion | String | 2.4.17 | 数据库代理的最新版本。 |  |  |
| ProxyVersionSta tus | String | Stable | 数据库代理的版本状态。取值范围如下： Stable ：当前版本状态稳定。 Old ：当前版本过旧，建议升级到最新版本。 HighRisk ：当前版本有严重缺陷，请立即升级到最新的版本。 |  |  |
| IsLatestVersion | String | true | 当前数据库内核引擎版本是否为最新版本，取值范围如下： true false |  |  |
| IsProxyLatestVe rsion | String | true | 当前数据库代理版本是否为最新版本，取值范围如下： true false |  |  |
| DBVersion | String | 8.0 | 数据库引擎的大版本号，取值范围如下： 8.0 5.7 5.6 |  |  |
| DBVersionStatu s | String | Stable | 当前数据库小版本状态，取值范围如下： Stable ：当前版本状态稳定。 Old ：当前版本过旧，建议升级到最新版本。 HighRisk ：当前版本有严重缺陷，请立即升级到最新的版本。 |  |  |

|  |  | Version |
|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBMinorVersion | String | 8.0.1 | 数据库引擎小版本号。 当 DBVersion 为8.0 时，取值范围如下： 8.0.2 8.0.1 当 DBVersion 为5.7 时，取值为5.7.28 。 当 DBVersion 为5.6 时，取值为5.6.16 。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterVersion &DBClusterId=pc-****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ProxyVersionStatus":"Stable",
 "IsLatestVersion":"true",
 "IsProxyLatestVersion":"true",
 "DBVersion":"8.0",
 "DBRevisionVersion":"8.0.1.1.7",
 "RequestId":"47921222-0D37-4133-8C0D-017DC3******",
 "DBVersionStatus":"Stable",
 "DBClusterId":"pc-****************",
 "ProxyRevisionVersion":"2.4.15",
 "DBLatestVersion":"8.0.1.1.16",
 "DBMinorVersion":"8.0.1",
 "ProxyLatestVersion":"2.4.17"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### 将标签从集群上解绑

将标签从PolarDB集群上解绑。 云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 可通过接口 DescribeRegions 查看可用的地域。 |
| ResourceTy pe | String | Query | 是 | cluster | 资源类型，取值固定为cluster 。 |
| All | Boole an | Query | 否 | true | 是否解绑全部标签，取值为true 或false ，默认值为false 。 仅当 TagKey.n 取值为空时该参数生效。 |
| ResourceId | Repea tList | Query | 是 | pc-*************** | 目标集群ID。 |
| TagKey | Repea tList | Query | 否 | type | 标签键。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2D69A58F-345C- 4FDE-88E4- BF5189****** | 请求ID。 |

**示例**

云原生数据库 I参考 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"2D69A58F-345C-4FDE-88E4-BF5189******"
}
```

### 开启或关闭集群热备节点

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-***************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ******* |  | rs |  |  |
| DBNodeId | String | Query | 是 | pi-***************** |  | 数据库集群节点ID。 |  |  |  |
| HotReplica Mode | String | Query | 是 | ON |  | 是否开启热备。取值范围： ON ：开启 OFF ：关闭 |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9F4DDFBF-205C- 5A3E-8DC2- C6********** | 请求ID。 |
| DBClusterId | String | pc-***************** | 集群ID。 您可以调用 DescribeDBClusters 接口查看目标地域下所有的集群信息，包括集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| OrderId | String | 2148126708***** | 生成的订单ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9F4DDFBF-205C-5A3E-8DC2-C6**********",
 "DBClusterId":"pc-*****************",
 "OrderId":"2148126708*****"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstanceCla ss.NotFound | InvalidDBInstanceClass.NotFound | rw class code must be equal with hot replica |

### 对集群进行手动主备切换

对PolarDB集群进行手动主备切换，可以指定一个只读节点为新的主节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 数据库集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| TargetDBN odeId | String | Query | 否 | pi-*********** | 将要切换为主节点的节点ID， 如果不填，则系统自动选举。 您可以通过接口 DescribeDBClusters 查询节点ID等信息。 自动选举主节点： 系统找出当前可以被选举的所有只读节点。 选择优先级最高的一个或多个只读节点。 如果切换第一个节点失败（例如，网络原因、复制状态异常等），则会尝试切换下一个，直至成功。 当集群为PolarDB PostgreSQL版（兼容 Oracle）或PolarDB PostgreSQL版时，该参数必填；当集群为 PolarDB MySQL版时，该参数非必填。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5* ***** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"D0CEC6AC-7760-409A-A0D5-E6CD86******"
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | HaStatusNotSupport | HaStatusNotSupport | Current DB instance HA status does not support this operation. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### 查看慢日志明细

查看PolarDB集群的慢日志明细。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou |  | 地域ID。 您可以调用 DescribeRegions 接口查看目标账号下的可用地域信息，包括地域 ID。 |  |  |  |
| DBClusterI d | String | Query | 是 | pc-************ |  | 集群ID。 您可以调用 DescribeDBCluste rs 接口查看目标地域下所有的集群信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ** |  | rs |  |  |
| StartTime | String | Query | 是 | 2022-11-15T16:00Z |  | 查询开始时间。格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 支持查看最多30天内的慢日志信息。 该参数输入的是UTC 时间（即0时区），如果您的服务当前处于其他时区，请您进行时间转换。例如，当前您的服务所在时区的时间是北京时间 （UTC+8时间）12:00点，如果您需要查询北京时间 08:00点-12:00点的慢日志信息，那么应该输入的时间是00:00 点-04:00点。 |  |  |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| EndTime | String | Query | 是 | 2022-11-16T04:00Z | 查询结束时间，需要晚于查询开始时间，且查询开始时间与结束时间的时间间隔需在24小时之内。格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 该参数输入的是UTC时间 （即0时区），如果您的服务当前处于其他时区， 请您进行时间转换。例如，当前您的服务所在时区的时间是北京时间 （UTC+8时间）12:00 点，如果您需要查询北京时间08:00点-12:00点的慢日志信息，那么应该输入的时间是00:00点- 04:00点。 |  |  |
|  |  |  |  |  |  | YYYY-MM- |  |
| DBName | String | Query | 否 | testdb | 数据库名称。 |  |  |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 50 100 默认值为30 。 |  |  |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0且不超过Integer的最大值。 默认值为1 。 |  |  |
| SQLHASH | String | Query | 否 | U2FsdGVk**** | 慢日志统计里的SQL语句唯一标识符，可用于获取该SQL语句的慢日志明细。 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |

|  | DDThh:mmZ |
|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | Integer | 1 | 总SQL语句个数。 |
| PageRecordCou nt | Integer | 1 | 本页记录数。 |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| RequestId | String | A7E6A8FD-C50B- 46B2-BA85- D8B8D3****** | 请求ID。 |  |  |
| PageNumber | Integer | 1 | 页码。 |  |  |
| DBClusterId | String | pc-***************** | 集群ID。 |  |  |
| Items | Array |  | 慢日志明细列表。 |  |  |
| - ExecutionStartT ime | String | 2021-04-07T03:47Z | SQL开始执行的时间。格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |  |  |
|  |  |  |  | YYYY-MM- |  |
| -HostAddress | String | testdb[testdb] @ [100.**.**.242] | 连接数据库的客户端地址。 |  |  |
| -QueryTimes | Long | 20 | SQL执行时长，单位为秒。 |  |  |
| -SQLText | String | /* Query from *** by user 111 */ SELECT sleep(20) | 查询语句。 |  |  |
| - ReturnRowCoun ts | Long | 0 | 返回行数。 |  |  |
| - ParseRowCount s | Long | 0 | 解析行数。 |  |  |
| -DBName | String | testdb | 数据库名称。 |  |  |
| -LockTimes | Long | 0 | SQL锁定时长，单位为秒。 |  |  |
| -DBNodeId | String | pi-***************** | 节点ID。 |  |  |
| -QueryTimeMS | Long | 100 | 查询时间。单位毫秒。 |  |  |
| Engine | String | polardb mysql _ | 数据库引擎。 |  |  |

| 3:47Z | DDThh:mmZ |
|---|---|

**示例**

`JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":1,
 "PageRecordCount":1,
 "RequestId":"A7E6A8FD-C50B-46B2-BA85-D8B8D3******",
 "PageNumber":1,
 "DBClusterId":"pc-*****************",
 "Items":{
  "QueryTimes":20,
  "ExecutionStartTime":"2021-04-07T03:47Z",
  "ReturnRowCounts":0,
  "LockTimes":0,
  "DBName":"testdb",
  "ParseRowCounts":0,
  "DBNodeId":"pi-*****************",
  "HostAddress":"testdb[testdb] @  [100.**.**.242]",
  "QueryTimeMS":100,
  "SQLText":"/* Query from *** by user 111 */ SELECT sleep(20)"
 },
 "Engine":"polardb_mysql"
}
```

### 查询集群SQL洞察功能

查看目标集群的SQL洞察功能是否已开启。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息（如集群 ID）。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | ****** |  | rs |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |  |  |

| 云原生数据库 |  |  |  |  | 集群版开发指南 I参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| OwnerAcco unt | String | Query | 否 |  |  |
|---|---|---|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3655211B-4D74- 4E13-91E6- FF2AFE****** | 请求ID。 |
| DBClusterId | String | pc- bp1s826a1up****** | 集群ID。 |
| SQLCollectorSta tus | String | Enable | SQL洞察功能是否开启，取值范围如下： Enable ：已开启 Disabled ：未开启 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"3655211B-4D74-4E13-91E6-FF2AFE******",
 "DBClusterId":"pc-bp1s826a1up******",
 "SQLCollectorStatus":"Enable"
}
```

### 查询待处理事件的详情

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Region | String | Query | 是 | all | 待处理事件所在地域的地域 ID，您可以调用 DescribeRegions 接口查看PolarDB支持的地域和可用区。 您可以输入all 查看您账户下所有的待处理事件。 当 Region 设置为all 时， TaskTy pe 也必须设置为all 。 |
| TaskType | String | Query | 是 | all | 待处理事件的任务类型，取值范围如下： DatabaseSoftwareUp grading ：数据库软件升级 DatabaseHardwareM aintenance ：硬件维护与升级 DatabaseStorageUpg rading ：数据库存储升级 DatabaseProxyUpgra ding ：代理小版本升级 all ：表示查询上述所有类型的待处理事件详情当 Region 设置为all 时， TaskType 也必须设置为all 。 |
| IsHistory | Intege r | Query | 否 | 0 | 是否返回历史任务，取值范围如下： 0 ：返回当前任务 1 ：返回历史任务默认取值为0 。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值为30 、50 或100 。 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值为大于0且不超过 Integer数据类型的最大值，默认值为1 。 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |

|  |  | pe |
|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | Integer | 1 | 总记录数。 |
| RequestId | String | 2F029645-FED9- 4FE8-A6D3- 488954****** | 请求ID。 |
| PageSize | Integer | 30 | 每页记录数。 |
| PageNumber | Integer | 1 | 页码。 |
| Items | Array |  | 任务列表。 |
| -Status | Integer | 3 | 任务状态。 若您设置 IsHistory 为0 ，则返回待处理任务状态的详情，取值范围如下： 2 ：等待用户设置任务开始时间 3 ：等待处理 4 ：任务正在处理中（不支持在该状态下修改任务执行时间） 若您设置 IsHistory 为1 ，则返回历史任务状态的详情，取值范围如下： 5 ：任务结束且执行成功 6 ：任务结束但执行失败 7 ：任务已取消 |
| -PrepareInterval | String | 04:00:00 | 待处理事件切换之前所需的准备时间，格式为 HH:mm:ss 。 |
| -Deadline | String | 2020-06- 11T15:59:59Z | 任务执行时间可调整范围的最晚期限，格式为 yyyy-MM-ddTHH:mm:ssZ （UTC时间）。 |
| -DBType | String | MySQL | 数据库引擎类型，取值范围如下： MySQL PostgreSQL Oracle |

| olarDB MySQL集参考 | 群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| -TaskType | String | DatabaseSoftwareUp grading | 待处理事件的任务类型。 |  |  |
| -StartTime | String | 2020-06- 09T18:00:00Z | 后台执行该任务的时间点，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
| -DBVersion | String | 8.0 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 5.7 8.0 PostgreSQL版本号取值范围如下： 11 14 Oracle版本号取值为11 。 |  |  |
| -ModifiedTime | String | 2020-06- 09T22:00:42Z | 修改时间，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
| -DBClusterId | String | pc-************ | 集群ID。 |  |  |
| -Region | String | cn-hangzhou | 任务所在地域的地域ID。 |  |  |
| -ResultInfo | String | manualCancel | 任务执行结果，取值范围如下： manualCancel ：手动取消任务 paramCheckNotPass ：参数检查未通过仅当 Status （任务状态）取值为6 （任务结束但执行失败）或7 （任务已取消）时， 返回该参数。 |  |  |
| -CreatedTime | String | 2020-06- 09T22:00:42Z | 创建任务的时间点，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
| -Id | Integer | 111111 | 目标任务ID。 |  |  |
| -SwitchTime | String | 2020-06- 09T22:00:00Z | 待处理事件预计的切换时间，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | yyyy-MM- |  |

| yyyy-MM- |  |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

| yyyy-MM- |  |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

`JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":1,
 "RequestId":"2F029645-FED9-4FE8-A6D3-488954******",
 "PageSize":30,
 "PageNumber":1,
 "Items":{
  "Status":3,
  "CreatedTime":"2020-06-09T22:00:42Z",
  "Deadline":"2020-06-11T15:59:59Z",
  "StartTime":"2020-06-09T18:00:00Z",
  "DBClusterId":"pc-************",
  "DBType":"MySQL",
  "DBVersion":"8.0",
  "ModifiedTime":"2020-06-09T22:00:42Z",
  "TaskType":"DatabaseSoftwareUpgrading",
  "PrepareInterval":"04:00:00",
  "Region":"cn-hangzhou",
  "Id":111111,
  "ResultInfo":"manualCancel",
  "SwitchTime":"2020-06-09T22:00:00Z"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

### 查询参数模板列表

查看目标地域的参数模板列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看当前账号下的所有可用地域信息，包括地域ID。 |
| DBType | String | Query | 否 | MySQL | 数据库引擎类型，当前仅支持MySQL 类型。 |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBVersion | String | Query | 否 | 8.0 | 数据库引擎版本号，取值范围如下： 5.6 5.7 8.0 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| ParameterGrou ps | Array |  | 参数模板列表。 |  |  |
| -DBType | String | MySQL | 数据库引擎类型。 |  |  |
| -DBVersion | String | 8.0 | 数据库引擎版本号。 |  |  |
| - ParameterGrou pName | String | test | 参数模板名称。 |  |  |
| -ForceRestart | String | 1 | 应用该参数模板是否需要重启集群，取直范围如下： 0 ：不需要重启 1 ：需要重启 |  |  |
| - ParameterGrou pType | String | 1 | 参数模板类型，取值范围如下： 0 ：系统默认模板 1 ：用户自定义模板 2 ：系统自动备份模板（应用模板后系统会自动备份之前的参数设置为模板） |  |  |
| - ParameterCount s | Long | 2 | 参数模板内的参数数量。 |  |  |
| - ParameterGrou pDesc | String | testgroup | 参数模板描述。 |  |  |
| -CreateTime | String | 2023-03- 10T08:40:39Z | 参数模板创建时间，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | yyyy-MM- |  |

|  | ddTHH:mm:ssZ |
|---|---|

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - ParameterGrou pId | String | pcpg-************** | 参数模板ID。 |
| RequestId | String | 944CED46-A6F7- 40C6-B6DC- C6E5CC****** | 请求ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ParameterGroups":{
  "DBVersion":"8.0",
  "ParameterGroupId":"pcpg-**************",
  "ParameterGroupName":"test",
  "ForceRestart":"1",
  "ParameterGroupType":"1",
  "ParameterGroupDesc":"testgroup",
  "CreateTime":"2023-03-10T08:40:39Z",
  "ParameterCounts":2,
  "DBType":"MySQL"
 },
 "RequestId":"944CED46-A6F7-40C6-B6DC-C6E5CC******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |

### 查询指定的参数模板信息

查询目标参数模板详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 您可以通过 DescribeRegions 接口查看当前账号下的所有可用地域信息，包括地域ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Parameter GroupId | String | Query | 是 | pcpg-************** |  | 参数模板ID。 您可以通过 DescribeParamete rGroups 接口查询目标地域下所有参数模板的详细信息，包括参数模板 ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeParamete |  |
|  |  |  |  |  | ******* |  | rGroups |  |  |
| ResourceGr oupId | String | Query | 否 | rg-************ |  | 资源组ID。 |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F1F16757-D31B- 49CA-9BF4- 305BAF****** | 请求ID。 |
| ParameterGrou p | Array |  | 参数模板信息列表。 |
| - ParameterDetail | Array |  | 参数列表。 |
| --ParamValue | String |  |  |
| --ParamName | String |  |  |
| -DBType | String | MySQL | 数据库引擎类型。 |
| -DBVersion | String | 8.0 | 数据库引擎版本号。 |
| - ParameterGrou pName | String | test | 参数模板名称。 |
| -ForceRestart | String | 1 | 应用该参数模板是否需要重启集群，取直范围如下： 0 ：不需要重启 1 ：需要重启 |
| - ParameterGrou pType | String | 1 | 参数模板类型，取值范围如下： 0 ：系统默认模板 1 ：用户自定义模板 2 ：系统自动备份模板（应用模板后系统会自动备份之前的参数设置为模板） |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| - ParameterCount s | Integer | 2 | 参数模板内的参数数量。 |  |  |
| - ParameterGrou pDesc | String | testgroup | 参数模板描述。 |  |  |
| -CreateTime | String | 2023-03- 10T08:40:39Z | 参数模板创建时间，格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | yyyy-MM- |  |
| - ParameterGrou pId | String | pcpg-************** | 参数模板ID。 |  |  |

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F1F16757-D31B-49CA-9BF4-305BAF******",
 "ParameterGroup":{
  "-ParameterDetail":{
   "ParamValue":"",
   "ParamName":""
  },
  "DBVersion":"8.0",
  "ParameterGroupId":"pcpg-**************",
  "ParameterGroupName":"test",
  "ForceRestart":"1",
  "ParameterGroupType":"1",
  "ParameterGroupDesc":"testgroup",
  "CreateTime":"2023-03-10T08:40:39Z",
  "ParameterCounts":2,
  "DBType":"MySQL"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |
| 400 | InvalidParameterGro upId.Malformed | InvalidParameterGroupId.Malform ed | The Specified parameter ParameterGroupId is not valid. |

### 查询 PolarDB 集群的地址信息

**请求头**

云原生数据库 I参考该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* |  | 集群ID。 您可以通过 DescribeDBCluste rs 接口查看账号下所有集群的详细信息，包括集群ID。 |  |  |  |
|  |  |  |  |  |  |  |  | DescribeDBCluste |  |
|  |  |  |  |  | *** |  | rs |  |  |
| DBEndpoin tId | String | Query | 否 | pe-************* |  | 集群地址ID。 |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2DC120BF-6EBA- 4C63-BE99- B09F9E****** | 请求ID。 |
| Items | Array |  | 集群地址详情。 |
| -AddressItems | Array |  | 连接串信息。 |
| --VSwitchId | String |  |  |
| -- PrivateZoneCon nectionString | String |  |  |
| -- ConnectionStrin g | String |  |  |
| --NetType | String |  |  |
| --Port | String |  |  |
| --VpcInstanceId | String |  |  |
| --VPCId | String |  |  |
| --IPAddress | String |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -NodeWithRoles | String | Reader1 | 目标连接地址下各节点的角色名称，其中主节点为Writer ；由于一个连接地址下可加入多个只读节点，因此每个只读节点的角色名称后会加上数字作为区分，如Reader1 、Reader2 ，以此类推。 仅PolarDB PostgreSQL版集群和PolarDB PostgreSQL版（兼容Oracle）集群支持该参数。 |
| -Nodes | String | pi-***************,pi- *************** | 连接地址配置的节点列表。 |
| - ReadWriteMode | String | ReadOnly | 读写模式： ReadWrite ：可读可写（自动读写分离）。 ReadOnly ：只读。 |
| -DBEndpointId | String | pe-************* | 连接地址ID。 |
| -EndpointConfig | String | {\"DistributedTransa ction\":\"off\",\"Consi stLevel\":\"0\",\"Load BalanceStrategy\":\"l oad\",\"MasterAccept Reads\":\"on\"} | 集群地址的高级配置。 DistributedTransaction ：事务拆分状态， 取值范围如下： on ：事务拆分已开启 off ：事务拆分已关闭 ConsistLevel ：会话一致性级别，取值范围如下： 0 ：最终一致性 1 ：会话一致性。 2 ：全局一致性 LoadBalanceStrategy ：负载均衡策略，基于负载的自动调度，取值固定为load 。 MasterAcceptReads ：主库是否接受读， 取值范围如下： on ：主库接受读 off ：主库不接受读 |
| - DBEndpointDes cription | String | test | 地址名称。 |
| -EndpointType | String | Custom | 集群地址类型： Cluster ：默认集群地址。 Primary ：主地址。 Custom ：自定义集群地址。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - AutoAddNewNo des | String | Enable | 新节点是否自动加入默认集群地址： Enable 。 Disable 。 |
| -DBClusterId | String | pc- bp1s826a1up****** | 集群ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"2DC120BF-6EBA-4C63-BE99-B09F9E******",
 "Items":{
  "DBEndpointId":"pe-*************",
  "NodeWithRoles":"Reader1",
  "AutoAddNewNodes":"Enable",
  "-AddressItems":{
   "PrivateZoneConnectionString":"",
   "VPCId":"",
   "VSwitchId":"",
   "Port":"",
   "VpcInstanceId":"",
   "ConnectionString":"",
   "IPAddress":"",
   "NetType":""
  },
  "EndpointType":"Custom",
  "DBClusterId":"pc-bp1s826a1up******",
  "Nodes":"pi-***************,pi-***************",
  "ReadWriteMode":"ReadOnly",
  "EndpointConfig":"
{\\\"DistributedTransaction\\\":\\\"off\\\",\\\"ConsistLevel\\\":\\\"0\\\",\\\"LoadBalanceStrate \\":\\\"load\\\",\\\"MasterAcceptReads\\\":\\\"on\\\"}",
  "DBEndpointDescription":"test"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### CheckKMSAuthorized

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 否 | cn-hangzhou | 地域ID。 您可以调用 DescribeRegions 接口查看目标账号下的可用地域信息，包括地域 ID。 |
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 您可以调用 DescribeDBClusters 接口查看目标地域下所有的集群信息，包括集群 ID。 |
| TDERegion | String | Query | 否 | cn-beijing | TDE密钥所在地域。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| AuthorizationSt ate | Integer | 0 | 授权状态。取值范围如下： 0 ：未授权。 1 ：已授权。 |
| RequestId | String | A7E6A8FD-C50B- 46B2-BA85- D8B8D3****** | 请求ID。 |
| RoleArn | String | acs:ram::1406926*** **:role/aliyunrdsinsta nceencryptiondefault role | 角色的全局资源描述符，用来指定具体角色。详情请参见RAM角色概览。 |
| DBClusterId | String | pc-************ | 集群ID。 |

**示例**

云原生数据库 I参考请求示例

```
http(s)://[Endpoint]/?Action=CheckKMSAuthorized &DBClusterId=pc-************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "AuthorizationState":0,
 "RequestId":"A7E6A8FD-C50B-46B2-BA85-D8B8D3******",
 "DBClusterId":"pc-************",
 "RoleArn":"acs:ram::1406926*****:role/aliyunrdsinstanceencryptiondefaultrole"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | UnsupportedKmsSer vice.NotEnabled | UnsupportedKmsService.NotEnab led | KMS service is not enabled. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### 创建全局白名单

创建全局IP白名单模板。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| GlobalIgNa me | String | Query | 是 | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线 （ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| GIpList | String | Query | 是 | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| GlobalSecurityIP Group | Array |  | 全局IP白名单模板信息。 |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| -SecurityIPType | String |  |  |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - WhitelistNetTyp e | String |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "GlobalSecurityIPGroup":{
  "SecurityIPType":"",
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |
| 400 | InvalidSecurityIPList. QuotaExceeded | InvalidSecurityIPList.QuotaExceed ed | Specified security IP list is not valid: Exceeding the allowed amount of IP address in the list. |
| 400 | InvalidSecurityIPList. Format | InvalidSecurityIPList.Format | Specified security IP list format is not valid. |
| 400 | InvalidSecurityIPList. Duplicate | InvalidSecurityIPList.Duplicate | Specified security IP list is not valid: Duplicate IP address in the list |
| 404 | InvalidUser.NotFoun d | InvalidUser.NotFound | Specified user does not exist. |

### 删除全局白名单

删除全局IP白名单模板。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| GlobalIgNa me | String | Query | 否 | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线 （ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| GlobalSecu rityGroupId | String | Query | 是 | g-zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| ResourceGr oupId | String | Query | 否 | rg-********** | 资源组ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| GlobalSecurityIP Group | Array |  | 全局IP白名单模板信息。 |
| -DBInstances | String |  |  |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| -SecurityIPType | String |  |  |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| - WhitelistNetTyp e | String |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "GlobalSecurityIPGroup":{
  "SecurityIPType":"",
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "DBInstances":"",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

### 查询备份日志列表

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 云原生数据库 I参考

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |  |  |
| StartTime | String | Query | 是 | 2020-02-01T15:00Z | 查询开始时间。格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |  |  |
| EndTime | String | Query | 是 | 2020-02-12T15:00Z | 查询结束时间，需晚于查询开始时间。格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |  |  |
|  |  |  |  |  |  | YYYY-MM- |  |
| BackupReg ion | String | Query | 否 | cn-hangzhou | 备份地域。 |  |  |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 50 100 默认值为30 。 |  |  |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0且不超过Integer的最大值的整数， 默认值为1 。 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

|  | DDThh:mmZ |
|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | String | 2 | 总记录数。 |
| PageRecordCou nt | String | 2 | 本页记录数。 |
| RequestId | String | ADAC63DB-0691- 4ECE-949A- FAEA68****** | 请求ID。 |
| PageNumber | String | 1 | 页码。 |
| Items | Array |  | 备份日志详情。 |
| -BackupLogId | String | 1111111111 | 备份日志ID。 |

| olarDB MySQL集参考 | 群版开发指南·AP |  | 云原生数据库 |  |  |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |  |  |
| - IntranetDownlo adLink | String | http://***********.oss -cn-hangzhou- internal.aliyuncs.com | 备份日志的内网下载链接。 |  |  |
| - LinkExpiredTim e | String | 2020-02- 14T08:40:50Z | 下载链接的过期时间。 |  |  |
| - BackupLogStart Time | String | 2020-02- 12T03:54:43Z | 本次备份日志开始时间，格式为 YYYY-MM- DD'T'HH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | YYYY-MM- |  |
| - BackupLogEndT ime | String | 2020-02- 12T03:55:31Z | 本次备份日志结束时间，格式为 YYYY-MM- DD'T'HH:mm:ssZ （UTC时间）。 |  |  |
|  |  |  |  | YYYY-MM- |  |
| -DownloadLink | String | http://***********.oss -cn- hangzhou.aliyuncs.co m | 备份日志的公网下载链接。 |  |  |
| -BackupLogSize | String | 1073741824 | 备份日志大小，单位为Byte。 |  |  |
| - BackupLogNam e | String | ib logfile1 _ | 备份日志文件名。 |  |  |

|  | DD'T'HH:mm:ssZ |
|---|---|

|  | DD'T'HH:mm:ssZ |
|---|---|

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":"2",
 "PageRecordCount":"2",
 "RequestId":"ADAC63DB-0691-4ECE-949A-FAEA68******",
 "PageNumber":"1",
 "Items":{
  "DownloadLink":"http://***********.oss-cn-hangzhou.aliyuncs.com",
  "BackupLogEndTime":"2020-02-12T03:55:31Z",
  "BackupLogId":"1111111111",
  "BackupLogName":"ib_logfile1",
  "LinkExpiredTime":"2020-02-14T08:40:50Z",
  "BackupLogSize":"1073741824",
  "IntranetDownloadLink":"http://***********.oss-cn-hangzhou-internal.aliyuncs.com",
  "BackupLogStartTime":"2020-02-12T03:54:43Z"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidStartTime.Malf ormed | InvalidStartTime.Malformed | The specified parameter StartTime is not valid. |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 400 | InvalidEndTime.Malfo rmed | InvalidEndTime.Malformed | The specified parameter EndTime is not valid. |
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter PageSize is not valid. |
| 400 | InvalidPageNumber. Malformed | InvalidPageNumber.Malformed | The specified parameter PageNumber is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |

### 查询备份可恢复时间范围

调用DescribeLocalAvailableRecoveryTime接口查询备份可恢复时间范围，即实例支持按时间点恢复的最早可恢复时间点（RPO）信息。

**适用引擎**

PolarDB MySQL集群版 PolarDB PostgreSQL主备版

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanceI d | Strin g | Quer y | 是 | rm-wq64n542y9j****** | 实例ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful，请求失败时会返回请求异常信息（如错误码等）。 |
| Success | Boolean | true | 请求结果。取值： true：请求成功。 false：请求失败。 |

云原生数据库 I参考

| Data | Struct | {} | 返回数据。 |
|---|---|---|---|
| - RecoveryEndTi me | String | 2026-01- 26T13:01:15Z | 恢复截止时间。 |
| - RecoveryBeginT ime | String | 2026-01- 21T04:30:32Z | 备份可恢复的起始时间。 |
| - DBInstanceNam e | String | rm- wq64n542y9j****** | 实例名称。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLocalAvailableRecoveryTime &DBInstanceId=rm-wq64n542y9j******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "Message":"Successful",
 "Data":{
  "RecoveryEndTime":"2026-01-26T13:01:15Z",
  "RecoveryBeginTime":"2026-01-21T04:30:32Z",
  "DBInstanceName":"rm-wq64n542y9j******"
 },
 "Success":true
}
```

`XML` 格式

```xml
<RequestId>9B7BFB11-C077-4FE3-B051-F69CEB******</RequestId> <Message>Successful</Message> <Data>
 <RecoveryEndTime>2026-01-26T13:01:15Z</RecoveryEndTime>
 <RecoveryBeginTime>2026-01-21T04:30:32Z</RecoveryBeginTime>
 <DBInstanceName>rm-wq64n542y9j******</DBInstanceName>
</Data> <Success>true</Success>
```

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| 400 | IInvalidDBInstanceNa me.NotFound | IInvalidDBInstanceName.NotFoun d | The specified DB instance name does not exist. |
|---|---|---|---|
| 400 | MissingUserID | MissingUserID | The request is missing a user id _ parameter. |
| 400 | MissingUID | MissingUID | The request is missing a uid parameter. |

### 查询 PolarDB 集群的规格列表

查看集群规格列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| Commodity Code | String | Query | 是 | polardb sub _ | 商品Code。取值范围如下： polardb sub：中国内地包 _ 年包月。 polardb sub intl：中国 _ _ 香港及海外包年包月。 polardb payg：中国内地 _ 按量付费。 polardb payg intl：中国 _ _ 香港及海外按量付费。 polardb sub jushita：聚 _ _ 石塔包年包月。 polardb payg jushita： _ _ 聚石塔按量付费。 polardb sub cainiao：菜 _ _ 鸟包年包月。 polardb payg cainiao： _ _ 菜鸟按量付费。 |
| OrderType | String | Query | 否 | BUY | 订单类型，取值范围如下： BUY：新购。 UPGRADE：变更配置。 RENEW：续费。 CONVERT：转换付费类型。 |
| RegionId | String | Query | 否 | cn-hangzhou | 地域ID。 如果您使用的是阿里云国际站账号，该参数必填。 |

| P I | olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 69A85BAF-1089- 4CDF-A82F- 0A140F****** | 请求ID。 |
| Items | Array |  | 集群规格列表。 |
| -Psl4MaxIOPS | String | 48000 | PSL4最大I/O请求次数，即IOPS。单位：次/秒。 |
| -ClassTypeLevel | String | enterprise | 规格类型。 |
| -Cpu | String | 8 | CPU核数。单位：个。 |
| -ReferencePrice | String | 200000 | 价格。 <props="china">单位：分（人民币）。 <props="intl">单位：美分（美元）。 CommodityCode参数中传入按量付费的商品Code时，显示为每小时的价格。 CommodityCode参数中传入包年包月的商品Code时，显示为每月的价格。 |
| - MaxConnections | String | 8000 | 最大集群并发连接数。 |
| -MemoryClass | String | 32 | 内存容量。单位：GB。 |
| -ClassCode | String | polar.mysql.x4.medi um | 集群规格。 |
| -ClassGroup | String | Exclusive package | 集群规格族。取值范围： Exclusive package：独享套餐。 Exclusive physical machine：独占物理机。 Beginner：入门级。 Historical specifications：历史规格。 |
| -Psl5MaxIOPS | String | 96000 | PSL5最大I/O请求次数，即IOPS。单位：次/秒。 |
| -MaxIOPS | String | 32000 | 最大I/O请求次数，即IOPS。单位：次/秒。 |

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - MaxStorageCap acity | String | 20 | 最大存储容量。单位：TB。 |
| RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"69A85BAF-1089-4CDF-A82F-0A140F******",
 "Items":{
  "ClassTypeLevel":"enterprise",
  "ClassCode":"polar.mysql.x4.medium",
  "MaxConnections":"8000",
  "Psl4MaxIOPS":"48000",
  "ClassGroup":"Exclusive package",
  "Psl5MaxIOPS":"96000",
  "Cpu":"8",
  "MemoryClass":"32",
  "ReferencePrice":"200000",
  "MaxIOPS":"32000",
  "MaxStorageCapacity":"20"
 },
 "RegionId":"cn-hangzhou"
}
```

### 查看集群的 IP 白名单

查看允许访问数据库集群的 IP 白名单和安全组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 559E91A2-CDA3- 4E9F-808B- 29D738****** | 请求ID。 |
| Items | Array |  | 集群的IP白名单分组列表。 |
| - DBClusterIPArra yAttribute | String | hidden | IP白名单分组属性。 |
| - DBClusterIPArra yName | String | default | IP白名单分组名称。 |
| -SecurityIps | String | 11.***.***.***,11.***.* **.*** | IP白名单分组下的IP列表，最多1000个，多个IP间用英文逗号（,）隔开，支持如下两种格式： IP地址形式，例如：10.xx.xx.24。 CIDR形式，例如：10.xx.xx.24/24（无类域间路由，24表示了地址中前缀的长度，范围为 1~32）。 |
| DBClusterSecuri tyGroups | Array |  | 集群关联的ECS安全组列表。 |
| - SecurityGroupId | String | sg-bp************** | ECS安全组ID。 |
| - SecurityGroupN ame | String | vpc- ******************** | ECS安全组名称。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"559E91A2-CDA3-4E9F-808B-29D738******",
 "Items":{
  "SecurityIps":"11.***.***.***,11.***.***.***",
  "DBClusterIPArrayName":"default",
  "DBClusterIPArrayAttribute":"hidden"
 },
 "DBClusterSecurityGroups":{
  "SecurityGroupName":"vpc-********************",
  "SecurityGroupId":"sg-bp**************"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

| 云原生数据库 |  |  | 集群版开发指南 I参考 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |

### 查询源 IP 地址能否正常访问数据库

调用接口DescribeDBClusterConnectivity查询源IP地址能否正常访问数据库。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| DBClusterI d | String | Query | 是 | pc-xxxxxxxxxxxxx | 集群ID。 |
| SourceIpAd dress | String | Query | 是 | 192.***.***.1 | 用户源IP地址。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ConnCheckError Code | String | SRC IP NOT IN USER _ _ _ _ WHITELIST _ | 连接诊断错误码。取值范围如下： SRC IP NOT IN USER WHITELIST ：源 _ _ _ _ _ IP地址没有加入白名单。 CONNECTION ABNORMAL ：连接正常。 _ |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ConnCheckResu lt | String | Failed | 连接诊断结果。取值范围如下： Success Failed |
| RequestId | String | 73A85BAF-1039- 4CDE-A83F- 1A140F****** | 请求ID。 |
| ConnCheckError Message | String | Src ip:192.***.***.1 not in user whitelist | 连接诊断错误信息。 |
| DBClusterId | String | pc-xxxxxxxxxxxxx | 集群ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ConnCheckErrorCode":"SRC_IP_NOT_IN_USER_WHITELIST",
 "ConnCheckResult":"Failed",
 "RequestId":"73A85BAF-1039-4CDE-A83F-1A140F******",
 "ConnCheckErrorMessage":"Src ip:192.***.***.1 not in user whitelist",
 "DBClusterId":"pc-xxxxxxxxxxxxx"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |

### 查询 PolarDB 集群的迁移状态

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

| 云原生数据库 |  |  |  | PolarD | B MySQL集群版开发指南·A I参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Comment | String | test | 迁移异常的注释信息，若迁移无异常则返回空值。 |
| RequestId | String | F2A9EFA7-915F- 4572-8299- 85A307****** | 请求ID。 |
| DBClusterId | String | pc-**************** | 集群ID。 |
| SrcDbType | String | PolarDBMySQL | 源数据库类型。取值如下： PolarDBMySQL ：PolarDB大版本升级迁移时的源数据库类型。 RDS ：将数据从RDS迁移至PolarDB MySQL时的源数据类型。 |
| SourceRDSDBIn stanceId | String | rm-************ | 源RDS实例ID。 |
| DBClusterRead WriteMode | String | ro | 集群读写模式，取值范围如下： rw ：读写。 ro ：只读。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MigrationStatus | String | RDS2POLARDB SYNC _ ING | PolarDB集群的迁移状态，取值范围如下： NO MIGRATION ：没有迁移任务。 _ RDS2POLARDB CLONING ：数据克隆中。 _ RDS2POLARDB SYNCING ：数据同步中， _ 此时PolarDB的读写状态为只读，RDS的读写状态为可读可写。 SWITCHING ：数据库切换中。 POLARDB2RDS SYNCING ：数据库切换完 _ 成，此时PolarDB的读写状态为可读可写，RDS的读写状态为只读。您可以修改应用内的连接地址。 ROLLBACK ：迁移回滚中，回滚完成后，状态变更为RDS2POLARDB SYNCING 。 _ CLOSING MIGRATION ：关闭迁移任务中。 _ |
| DtsInstanceId | String | dts**********618bs | 同步任务ID。 |
| RdsEndpointList | Array |  | RDS连接地址详情。 |
| -AddressItems | Array |  | 连接串详情。 |
| --VSwitchId | String |  |  |
| -- ConnectionStrin g | String |  |  |
| --NetType | String |  |  |
| --Port | String |  |  |
| --VPCId | String |  |  |
| --IPAddress | String |  |  |
| --SSLEnabled | String |  |  |
| -DBEndpointId | String | rm-************- normal | 连接地址ID。 |
| -EndpointType | String | Normal | 连接地址类型，取值范围如下： Normal ：普通地址 ReadWriteSplitting ：读写分离地址 |
| DBClusterEndpo intList | Array |  | PolarDB连接地址详情。 |
| -AddressItems | Array |  | 连接串详情。 |
| --VSwitchId | String |  |  |
| -- ConnectionStrin g | String |  |  |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --NetType | String |  |  |
| --Port | String |  |  |
| --VPCId | String |  |  |
| --IPAddress | String |  |  |
| --SSLEnabled | String |  |  |
| -DBEndpointId | String | pe-*********** | 连接地址ID。 |
| -EndpointType | String | Cluster | 连接地址类型，取值范围如下： Cluster ：默认集群地址 Primary ：主地址 Custom ：自定义集群地址 |
| ExpiredTime | String | 2020-06- 17T01:56:36Z | RDS与PolarDB之间的复制关系到期时间，格式为 YYYY-MM-DDThh:mm:ssZ （UTC时间）。 |
| Topologies | String | RDS2POLARDB | 同步关系，取值范围如下： RDS2POLARDB ：从RDS到PolarDB同步 POLARDB2RDS ：从PolarDB到RDS同步 |
| RdsReadWriteM ode | String | rw | 源RDS实例读写模式，取值范围如下： rw ：读写 ro ：只读 |
| DelayedSecond s | Integer | 0 | RDS与PolarDB之间的复制延迟时间，单位为秒。 |

**示例**

`JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "Comment":"test",
 "RequestId":"F2A9EFA7-915F-4572-8299-85A307******",
 "DBClusterId":"pc-****************",
 "SrcDbType":"PolarDBMySQL",
 "SourceRDSDBInstanceId":"rm-************",
 "DBClusterReadWriteMode":"ro",
 "MigrationStatus":"RDS2POLARDB_SYNCING",
 "DtsInstanceId":"dts**********618bs",
 "RdsEndpointList":{
  "DBEndpointId":"rm-************-normal",
  "-AddressItems":{
   "SSLEnabled":"",
   "VPCId":"",
   "VSwitchId":"",
   "Port":"",
   "ConnectionString":"",
   "IPAddress":"",
   "NetType":""
  },
  "EndpointType":"Normal"
 },
 "DBClusterEndpointList":{
  "DBEndpointId":"pe-***********",
  "-AddressItems":{
   "SSLEnabled":"",
   "VPCId":"",
   "VSwitchId":"",
   "Port":"",
   "ConnectionString":"",
   "IPAddress":"",
   "NetType":""
  },
  "EndpointType":"Cluster"
 },
 "ExpiredTime":"2020-06-17T01:56:36Z",
 "Topologies":"RDS2POLARDB",
 "RdsReadWriteMode":"rw",
 "DelayedSeconds":0
}
```

### DescribeDBClusterMonitor

调用DescribeDBClusterMonitor接口查询PolarDB集群的监控数据采集频率。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |

云原生数据库 I参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 593AE1C5-B70C- 463F-9207- 074639****** | 请求ID。 |
| Period | String | 60 | 监控数据的采集间隔，单位为秒。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterMonitor &DBClusterId=pc-****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"593AE1C5-B70C-463F-9207-074639******",
 "Period":"60"
}
```

### DescribeDBClusterParameters

调用DescribeDBClusterParameters接口查看PolarDB集群当前参数运行列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-********** | 集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RunningParame ters | Array |  |  |
| -CheckingCode | String | [utf8\|latin1\|gbk\|utf8 mb4] | 目标参数的取值范围。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DataType | String | INT | 参数值类型。取值： INT ：整数类型。 STRING ：字符串类型。 B ：字节类型。 |
| - ParameterName | String | character set server _ _ | 参数名。 |
| - ParameterValue | String | utf8 | 参数值。 |
| -ForceRestart | Boolean | true | 是否需要重启生效。取值： false ：否。 true ：是。 |
| - ParameterDescr iption | String | The server's default character set. | 参数描述。 |
| - ParameterStatu s | String | Normal | 参数状态。取值： Normal ：正常。 Modifying ：修改中。 |
| - DefaultParamet erValue | String | utf8 | 参数默认值。 |
| -IsModifiable | Boolean | true | 是否可修改。取值： false ：不可修改。 true ：可修改。 |
| - IsNodeAvailable | String | 0 | 是否是全局参数。取值如下： 0 ：是全局参数。修改后的参数值会默认同步到其它节点。 1 ：不是全局参数。修改后的参数值可自定义需要同步的节点。 |
| -ParamRelyRule | String | utf8 | 参数依赖。 |
| -Factor | String | 20 | 整除因子。对于整数和字节类型的参数，参数值除了必须满足参数的可选范围，还须是Factor（不等于 0）的倍数。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBVersion | String | 5.6 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 5.7 8.0 PostgreSQL版本号取值范围如下： 11 14 Oracle版本号取值为11 。 |
| RequestId | String | EBEAA83D-1734- 42E3-85E3- E25F6E****** | 请求ID。 |
| DBType | String | MySQL | 数据库类型，取值： MySQL 。 PostgreSQL 。 Oracle 。 |
| Engine | String | POLARDB | 引擎。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterParameters &DBClusterId=pc-**********
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RunningParameters":{
  "DefaultParameterValue":"utf8",
  "IsModifiable":true,
  "CheckingCode":"[utf8|latin1|gbk|utf8mb4]",
  "ParameterValue":"utf8",
  "ParameterStatus":"Normal",
  "ForceRestart":true,
  "IsNodeAvailable":"0",
  "Factor":"20",
  "ParamRelyRule":"utf8",
  "DataType":"INT",
  "ParameterName":"character_set_server",
  "ParameterDescription":"The server's default character set."
 },
 "DBVersion":"5.6",
 "RequestId":"EBEAA83D-1734-42E3-85E3-E25F6E******",
 "DBType":"MySQL",
 "Engine":"POLARDB"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |

### DescribeDBClusterSSL

调用DescribeDBClusterSSL接口查询PolarDB集群SSL设置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 您可以通过 DescribeDBClusters接口查看账号下所有集群的详细信息，包括集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Items | Array |  |  |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -SSLExpireTime | String | 2021-11- 13T07:14:22Z | SSL证书有效期。格式： yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| -SSLEnabled | String | Enabled | 是否开启SSL加密。取值： Enabled ：开启。 Disabled ：关闭。 |
| - SSLConnectionS tring | String | pc- ************.mysql.p olardb.rds.aliyuncs.c om | SSL链路地址。 |
| -DBEndpointId | String | pe-************ | 集群地址ID。 |
| RequestId | String | C890995A-CF06- 4F4D-8DB8- DD26C2****** | 请求ID。 |
| SSLAutoRotate | String | Enable | 是否开启SSL证书自动轮转。取值： Enable ：开启。 Disable ：关闭。 该参数仅PolarDB MySQL版支持。 |

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterSSL &DBClusterId=pc-************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"C890995A-CF06-4F4D-8DB8-DD26C2******",
 "SSLAutoRotate":"Enable",
 "Items":{
  "SSLConnectionString":"pc-************.mysql.polardb.rds.aliyuncs.com",
  "SSLExpireTime":"2021-11-13T07:14:22Z",
  "DBEndpointId":"pe-************",
  "SSLEnabled":"Enabled"
 }
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeDBClusterTDE

调用DescribeDBClusterTDE接口查询PolarDB MySQL引擎集群的TDE设置详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TDEStatus | String | Enabled | 是否开通TDE加密，取值： Enabled ：开通。 Disabled ：关闭。 |
| RequestId | String | E37D1508-EC3B- 4E06-A24A- C7AC31****** | 请求ID。 |
| DBClusterId | String | pc-*************** | 集群ID。 |
| EncryptionKey | String | 2a4f4ac2-****-****- ****-************ | 自定义密钥ID。 |
| EncryptNewTabl es | String | ON | 是否开启自动加密所有新建的表。取值： ON ：开启。 OFF ：关闭。 |
| TDERegion | String | cn-beijing | TDE密钥所在的地域。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterTDE &DBClusterId=pc-***************
```

&公共请求参数云原生数据库 I参考正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TDEStatus":"Enabled",
 "RequestId":"E37D1508-EC3B-4E06-A24A-C7AC31******",
 "EncryptNewTables":"ON",
 "TDERegion":"cn-beijing",
 "DBClusterId":"pc-***************",
 "EncryptionKey":"2a4f4ac2-****-****-****-************"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeDBNodePerformance

调用DescribeDBNodePerformance接口查询PolarDB集群节点的性能数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBNodeId | String | Query | 是 | pi-************* | 数据库集群节点ID。 |
| Key | String | Query | 是 | PolarDBDiskUsage | 查询的性能指标，多个值间用英文逗号（,）分隔，详细参数请参见性能参数表。 最多可传入5个查询的性能指标。 |
| StartTime | String | Query | 是 | 2020-09-23T01:00Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2020-09-23T01:01Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 否 | pc-**************** | 集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PerformanceKey s | Array |  | 集群性能数据列表。 |
| -Points | Array |  | 性能数据数组。 |
| --Value | String | 9.33 | 监控指标数据值。 |
| --Timestamp | Long | 1600822800000 | 监控指标的具体时间点，格式为Unix时间戳，单位为毫秒（ms）。 |
| -MetricName | String | mean sys dir size _ _ _ | 具体的性能指标度量名称。 |
| -Measurement | String | PolarDBDiskUsage | 性能指标。 |
| DBVersion | String | 8.0 | 兼容数据库版本。 |
| EndTime | String | 2020-09- 23T01:01:00Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| RequestId | String | E2FDB684-751D- 424D-98B9- 704BEA****** | 请求ID。 |
| StartTime | String | 2020-09- 23T01:00:00Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| DBType | String | MySQL | 兼容数据库类型。 |
| DBNodeId | String | pi-***************** | 数据库集群节点ID。 |
| Engine | String | POLARDB | 数据库引擎。 |

|  | ddTHH:mm:ssZ |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

请求示例云原生数据库 I参考

```
http(s)://[Endpoint]/?Action=DescribeDBNodePerformance &DBNodeId=pi-************* &Key=PolarDBDiskUsage &StartTime=2020-09-23T01:00Z &EndTime=2020-09-23T01:01Z
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "PerformanceKeys":{
  "Measurement":"PolarDBDiskUsage",
  "MetricName":"mean_sys_dir_size",
  "-Points":{
   "Value":"",
   "Timestamp":""
  }
 },
 "DBVersion":"8.0",
 "EndTime":"2020-09-23T01:01:00Z",
 "RequestId":"E2FDB684-751D-424D-98B9-704BEA******",
 "StartTime":"2020-09-23T01:00:00Z",
 "DBType":"MySQL",
 "DBNodeId":"pi-*****************",
 "Engine":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBNodeId.Not Found | InvalidDBNodeId.NotFound | The DBNodeId provided does not exist in our records. |

### 查询集群中指定节点的参数

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| DBNodeIds | String | Query | 是 | pi-****************,pi- **************** | 节点ID。支持传入多个节点 ID，多个节点ID间用英文逗号 （,）分隔。 |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| DBVersion | String | 5.6 | MySQL版本号。取值范围： 5.6 5.7 8.0 |
| DBNodeIds | Array |  | 节点ID列表。 |
| - RunningParame ters | Array |  | 当前节点运行的参数列表。 |
| --CheckingCode | String |  |  |
| --DataType | String |  |  |
| -- DefaultParamet erValue | String |  |  |
| --ForceRestart | Boolean |  |  |
| --IsModifiable | Boolean |  |  |
| -- ParameterDescr iption | String |  |  |
| -- ParameterName | String |  |  |
| -- ParameterStatu s | String |  |  |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- ParameterValue | String |  |  |
| -- IsNodeAvailable | String |  |  |
| -- ParamRelyRule | String |  |  |
| --Factor | String |  |  |
| -DBNodeId | String | pi- bp1r4qe3s534***** | 节点ID。 |
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| DBType | String | MySQL | 数据库类型。取值固定为MySQL 。 |
| Engine | String | POLARDB | 集群引擎。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "DBVersion":"5.6",
 "DBNodeIds":{
  "-RunningParameters":{
   "DefaultParameterValue":"",
   "IsModifiable":"",
   "CheckingCode":"",
   "ParameterStatus":"",
   "ParameterValue":"",
   "ForceRestart":"",
   "IsNodeAvailable":"",
   "Factor":"",
   "ParamRelyRule":"",
   "DataType":"",
   "ParameterName":"",
   "ParameterDescription":""
  },
  "DBNodeId":"pi-bp1r4qe3s534*****"
 },
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "DBType":"MySQL",
 "Engine":"POLARDB"
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBCluster.Not Found | InvalidDBCluster.NotFound | The specified DBClusterId is not found. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### 修改白名单名称

查询全局IP白名单模板列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| GlobalSecu rityGroupId | String | Query | 否 | g-zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| GlobalSecurityIP Group | Array |  | 全局IP白名单模板信息。 |
| -DBInstances | String |  |  |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| -SecurityIPType | String |  |  |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| - WhitelistNetTyp e | String |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "GlobalSecurityIPGroup":{
  "SecurityIPType":"",
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "DBInstances":"",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAction | InvalidAction | Specified action is not valid. |
| 404 | InvalidUser.NotFoun d | InvalidUser.NotFound | Specified user does not exist. |

### 修改关联关系

查询集群与全局IP白名单模板的关联关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| DBClusterI d | String | Query | 是 | pc-***************** | 集群ID。 |
| ResourceGr oupId | String | Query | 否 | rg-********** | 资源组ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| DBClusterId | String | pc-***************** | 集群ID。 |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| GlobalSecurityIP GroupRel | Array |  | 全局IP白名单模板信息。 |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| - WhitelistNetTyp e | String |  |  |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "DBClusterId":"pc-*****************",
 "GlobalSecurityIPGroupRel":{
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

### DescribeMaskingRules

调用DescribeMaskingRules接口查询PolarDB集群下所有的脱敏规则或目标脱敏规则的详情。 云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-***************** | 集群ID。 您可以通过 DescribeDBClusters接口查看账号下所有集群的详细信息，包括集群ID。 |
| RuleNameL ist | String | Query | 否 | testrule | 脱敏规则名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2F83D131-1C18- 4599-889D- 729A9D****** | 请求ID。 |
| Message | String | Successful | 请求返回消息。 请求成功时该参数返回Successful，请求失败时会返回请求异常信息（如错误码等）。 |
| Success | Boolean | true | 请求结果。取值： true ：请求成功。 false ：请求失败。 |
| DBClusterId | String | pc- bp1s826a1up****** | 集群ID。 |
| Data | Struct |  |  |
| -RuleList | String | "{\"testrule\": {\"auto\": {\"databases\": [],\"tables\": [\"t1\"],\"columns\": [\"c1\"]},\"applies to\ _ ": [],\"description\":\"Th is rule will be applied to the columns c1 in table t1\",\"enabled\":\"tru e\"}}" | 脱敏规则详细配置。 关于各参数的详细介绍，详情请参见 ModifyMaskingRules中RuleConfig的参数描述。 |

**示例**

请求示例云原生数据库 I参考

```
http(s)://[Endpoint]/?Action=DescribeMaskingRules &DBClusterId=pc-*****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"2F83D131-1C18-4599-889D-729A9D******",
 "Message":"Successful",
 "DBClusterId":"pc-bp1s826a1up******",
 "Data":{
  "RuleList":""
 },
 "Success":true
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Abs.InvalidAccount.N otFound | Abs.InvalidAccount.NotFound | account is not found. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### 查看不同任务类型下待处理事件的数量

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| IsHistory | Intege r | Query | 否 | 1 | 是否返回历史任务，取值范围如下： 0 ：返回当前任务 1 ：返回历史任务默认取值为0 。 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |

| P I | olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 314127C2-B6C1- 4F58-B1F6- E6B645****** | 请求ID。 |
| TypeList | Array |  | 待处理事件的详情。 |
| -TaskType | String | DatabaseSoftwareUp grading | 待处理事件的任务类型，取值范围如下： DatabaseSoftwareUpgrading ：数据库软件升级 DatabaseHardwareMaintenance ：硬件维护与升级 DatabaseStorageUpgrading ：数据库存储升级 DatabaseProxyUpgrading ：代理小版本升级 |
| -Count | Integer | 1 | 待处理事件的数量。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"314127C2-B6C1-4F58-B1F6-E6B645******",
 "TypeList":{
  "TaskType":"DatabaseSoftwareUpgrading",
  "Count":1
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

### 修改全局白名单

修改IP白名单模板。 云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| ResourceGr oupId | String | Query | 否 | rg-********** | 资源组ID。 |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| GlobalIgNa me | String | Query | 是 | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线 （ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| GlobalSecu rityGroupId | String | Query | 是 | g-zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| GIpList | String | Query | 是 | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| GlobalSecurityIP Group | Array |  | 全局IP白名单模板信息。 |
| -DBInstances | String |  |  |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| -SecurityIPType | String |  |  |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| - WhitelistNetTyp e | String |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "GlobalSecurityIPGroup":{
  "SecurityIPType":"",
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "DBInstances":"",
  "WhitelistNetType":""
 }
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |
| 400 | InvalidSecurityIPList. QuotaExceeded | InvalidSecurityIPList.QuotaExceed ed | Specified security IP list is not valid: Exceeding the allowed amount of IP address in the list. |
| 400 | InvalidSecurityIPList. Format | InvalidSecurityIPList.Format | Specified security IP list format is not valid. |
| 400 | InvalidSecurityIPList. Duplicate | InvalidSecurityIPList.Duplicate | Specified security IP list is not valid: Duplicate IP address in the list |

### 修改全局白名单名称

修改全局IP白名单模板名称。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| GlobalIgNa me | String | Query | 是 | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线 （ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| GlobalSecu rityGroupId | String | Query | 是 | g-zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |

| olarDB MySQ | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| GlobalSecurityIP Group | Array |  | 全局IP白名单模板信息。 |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |
| -SecurityIPType | String |  |  |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| - WhitelistNetTyp e | String |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

`JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "GlobalSecurityIPGroup":{
  "SecurityIPType":"",
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |

### 修改全局白名单关联关系

修改集群与全局IP白名单模板的关联关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| DBClusterI d | String | Query | 是 | pc-***************** | 集群ID。 |
| GlobalSecu rityGroupId | String | Query | 是 | g-zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| ResourceGr oupId | String | Query | 否 | rg-********** | 资源组ID。 |
| Action | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |

| P I | olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |
| DBClusterId | String | pc-***************** | 集群ID。 |
| GlobalSecurityIP GroupRel | Array |  | 全局IP白名单模板信息。 |
| - GlobalSecurityG roupId | String | g- zsldxfiwjmti0kcm**** | IP白名单模板ID。 |
| -GIpList | String | 192.168.0.1 | 白名单模板内的IP地址。 多个IP地址需要用英文逗号隔开，所有IP白名单累积支持添加1000个IP地址或地址段。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| - WhitelistNetTyp e | String |  |  |
| -GlobalIgName | String | test 123 _ | IP白名单模板名称。IP白名单模板名称需满足如下要求： 由小写字母、数字、下划线（ ）组成。 _ 由字母开头、字母或数字结尾。 长度为2~120个字符。 |

**示例**

`JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"9B7BFB11-C077-4FE3-B051-F69CEB******",
 "DBClusterId":"pc-*****************",
 "GlobalSecurityIPGroupRel":{
  "GlobalIgName":"test_123",
  "GIpList":"192.168.0.1",
  "GlobalSecurityGroupId":"g-zsldxfiwjmti0kcm****",
  "RegionId":"cn-hangzhou",
  "WhitelistNetType":""
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | RequiredParam.NotF ound | RequiredParam.NotFound | Required input param is not found. |
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | The specified parameters are invalid. |

### 为PolarDB集群添加标签

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 |
| ResourceTy pe | String | Query | 是 | cluster | 资源类型，取值固定为cluster 。 |
| ResourceId | Repea tList | Query | 是 | pc-***************** | 目标集群ID。 |
| Tag | Repea tList | Query | 是 |  | 标签列表。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 1CB5286F-AF5A- 4E09-BFE9- 588D4C****** | 请求ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1CB5286F-AF5A-4E09-BFE9-588D4C******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NumberExceed.Cust omTags | NumberExceed.Tags | The number of tags is exceed , Valid : 20 |

### CheckDBName

调用CheckDBName接口校验数据库名称是否合法或当前集群中是否已存在重名的数据库。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 您可以调用 DescribeDBClusters接口查看目标地域下所有的集群信息，包括集群ID。 |
| DBName | String | Query | 是 | test db _ | 数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CDB3258F-B5DE- 43C4-8935- CBA0CA****** | 请求ID。 |
| DBName | String | test db _ | 数据库名称。 |

**示例**

云原生数据库 I参考请求示例

```
&DBClusterId=pc-**************** &DBName=test_db
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"CDB3258F-B5DE-43C4-8935-CBA0CA******",
 "DBName":"test_db"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBName.Dupli cate | InvalidDBName.Duplicate | The specified DB name already exists. |

### DeleteDBCluster

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群 ID。 |
| BackupRet entionPolic yOnCluster Deletion | String | Query | 否 | NONE | 删除集群时备份集保留策略， 取值范围如下： ALL ：长期保留全部备份。 LATEST ：长期保留最后一个备份（删除前自动备份）。 NONE ：集群删除时不保留备份集。 |

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求 ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | OperationDenied.DB ClusterDeletionLock | OperationDenied.DBClusterDeleti onLock | The operation is not permitted due to the deletion lock of cluster. |
| 403 | OperationDenied.Op erateStatus | OperationDenied.OperateStatus | Specified action is denied by operate status. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### CancelScheduleTasks

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 |  |  |
| TaskId | String | Query | 是 |  |  |
| ResourceGr oupId | String | Query | 否 |  |  |

|  | 云原生数据库 |  |  |  | PolarD | B MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| callerBid | String | System | 否 |  |  |
| callerUid | Long | System | 否 |  |  |
| callerType | String | System | 否 |  |  |
| callerParen tId | Long | System | 否 |  |  |
| SecurityTo ken | String | System | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| app ip _ | String | System | 否 |  |  |
| security tr _ ansport | Boole an | System | 否 |  |  |
| proxy trust _ transport _ _ info | Boole an | System | 否 |  |  |
| proxy origi _ nal securit _ y transport _ | Boole an | System | 否 |  |  |
| proxy origi _ nal source _ _ ip | String | System | 否 |  |  |
| ak mfa pre _ _ sent | Boole an | System | 否 |  |  |
| RequestId | String | System | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| app ip _ | String | System | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| callerUidE mail | String | System | 否 |  |  |
| callerBidE mail | String | System | 否 |  |  |
| ownerIdLog inEmail | String | System | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |

| olarDB MySQ | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| enable | Boole an | System | 否 |  |  |
| requestCon tent | String | System | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| Product | String | System | 否 |  |  |
| Category | String | System | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String |  |  |
| Success | Boolean |  |  |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "TaskId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "Success":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBNodeId.Malf ormed | InvalidDBNodeId.Malformed | The specified parameter DBNodeId is not valid. |

### CloseDBClusterMigration

调用CloseDBClusterMigration接口取消或完成RDS一键升级到PolarDB的迁移任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

云原生数据库 I参考

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| ContinueEn ableBinlog | Boole an | Query | 否 | true | 是否继续打开Binlog，取值范围如下： true ：继续打开Binlog false ：关闭Binlog 默认取值为true 。 关闭Binlog将会重启您的 PolarDB集群。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3AA69096-757C- 4647-B36C- 29EBC2****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

### CreateBackup

**请求头**

云原生数据库 I参考该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F3322AFE-083E- 4D77-A074- 421301****** | 请求ID。 |
| BackupJobId | String | 11111111 | 备份集ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "BackupJobId":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | BackupTimesExceed ed | BackupTimesExceeded | The maximum number of backups per day is exceeded. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### CreateDBClusterEndpoint

调用CreateDBClusterEndpoint接口创建PolarDB自定义集群地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| EndpointTy pe | String | Query | 是 | Custom | 自定义集群地址类型，取值固定为Custom 。 |

云原生数据库 I参考

|  | 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  | Nodes | String | Query | 否 | pi-**********,pi-********* |  | 加入目标地址的读负载节点， 多个节点间用英文逗号（,）分隔。 默认为全部节点。 PolarDB MySQL版需要传入节点ID。 PolarDB PostgreSQL版和 PolarDB PostgreSQL版 （兼容Oracle）需要传入节点角色名称，例如 Writer,Reader1,Rea der2 。 ReadWriteMode 取值为ReadOnly 时，支持只挂载一个节点。但当此节点故障时，该地址可能会有最多1小时的不可用，请勿用于生产环境。因此，推荐至少选择2个节点，以提升可用性。 ReadWriteMode 取值为ReadWrite 时，至少要选择2个节点。 PolarDB MySQL版支持选择任意两个节点。当两个节点都是只读节点时， 写请求都会发往主节点。 PolarDB PostgreSQL版和PolarDB PostgreSQL 版（兼容Oracle）必须包含主节点。 |  |  |
|  |  |  |  |  |  |  |  | Writer,Reader1,Rea |  |
|  |  |  |  |  |  |  | der2 |  |  |
|  | ReadWrite Mode | String | Query | 否 | ReadOnly |  | 读写模式，取值范围如下： ReadWrite ：可读可写 （自动读写分离）。 ReadOnly ：只读。 默认为ReadOnly 。 |  |  |
|  | AutoAddNe wNodes | String | Query | 否 | Disable |  | 新节点是否自动加入本地址， 取值范围如下： Enable ：新节点自动加入本地址。 Disable ：新节点不自动加入本地址。 默认取值为Disable 。 |  |  |
|  |  |  |  |  |  |  | 集群地址的高级配置，格式为 JSON，目前支持设置一致性级别、事务拆分、主库不接受读和连接池。 |  |  |

|  | 云原生数据库 |  |  |  |  |  | PolarD |  |  | B MySQL集群版开发指南·A I参考 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 参数名称 | 类型 | 位置 | 是否必选 |  |  | 示例 |  |  | 设置一致性级别，格式说明为 {"ConsistLevel":" |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"ConsistLevel":" |  |
|  | EndpointCo nfig | String | Query | 否 |  |  |  |  |  | 一致性级别"} ，取值范围如下： 0 ：最终一致性 1 ：会话一致性（默认值） 2 ：全局一致性设置事务拆分，格式为 {"DistributedTrans action":"事务拆分"} ，取值范围如下： on ：开启事务拆分 （默认值） off ：关闭事务拆分设置主库不接受读，格式为 {"MasterAcceptRead s":"主库不接受读"} ， 取值范围如下： on ：表示主库接受读 off ：表示主库不接受读（默认值） 设置连接池，格式为 {"ConnectionPersis t":"连接池"} ，取值范围如下： off ：关闭连接池（默认值） Session ：开启会话级连接池 Transaction ：开启事务级连接池仅当PolarDB MySQL 版集群地址的读写模式为**可读可写（自动读写分离）**时， 支持设置事务拆分、 主库不接受读和连接池。 仅PolarDB MySQL版支持将一致性级别设置为全局一致性。 如果参数ReadWriteMode 取值为ReadOnly ，一致性级别取值只能为0 。 您可以同时设置一致性级别、事务拆分、主库不接受读和连接池，例如 {"ConsistLevel":"1 |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"DistributedTrans |  |
|  |  |  |  |  |  |  |  |  |  | action":"事务拆 |  |  |
|  |  |  |  |  |  |  |  |  |  | 分"} |  |  |
|  |  |  |  |  |  |  | {"ConsistLevel": "1","DistributedTransactio n": "on"} |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  | {"ConsistLevel":"1 |  |
|  |  |  |  |  |  |  |  |  |  | ","DistributedTransac |  |  |
|  |  |  |  |  |  |  |  |  |  | tion":"on","Connectio |  |  |
|  |  |  |  |  |  |  |  |  |  | nPersist":"Session"," |  |  |
|  |  |  |  |  |  |  |  |  |  | MasterAcceptReads":"o |  |  |
|  |  |  |  |  |  |  |  |  |  | n"} |  |  |

|  |  | {"MasterAcceptRead |
|---|---|---|
|  | s":"主库不接受读"} |  |

|  |  | {"ConnectionPersis |  |
|---|---|---|---|
|  | t":"连接池"} |  |  |

云原生数据库 I参考

|  |  |  |  |  | 开启事务拆分；一致性级别 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明取值为1 或2 时，支持 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f ****************** | 用于开保启证事请务求拆的分幂。等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| DBEndpoin tDescriptio n | String | Query | 否 | test | 自定义集群地址名称。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CD35F3-F3-44CA- AFFF-BAF869****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "EndpointType":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ClusterEndpoint.Stat usNotValid | ClusterEndpoint.StatusNotValid | Cluster endpoint status is not valid. |
| 400 | EndpointNum.Error | EndpointNum.Error | Endpoint number error. |
| 400 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 404 | EndpointConfig.Invali d | EndpointConfig.Invalid | Endpoint config is invalid. |

|  |  |  | PolarDB MySQL集群版开发指南·A |
|---|---|---|---|

I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | EndpointConfig.Confl ict | EndpointConfig.Conflict | Endpoint config is invalid, CausalConsistRead should be session since node SCC mode enabled. |

### CreateParameterGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 是 | cn-hangzhou | 参数模板所在地域的地域ID。 您可以通过接口 DescribeRegions查看地域ID。 |
| DBType | String | Query | 是 | MySQL | 数据库引擎类型，当前仅支持MySQL 。 |
| DBVersion | String | Query | 是 | 8.0 | 数据库引擎版本号，取值范围如下： 5.6 5.7 8.0 |
| Parameter GroupNam e | String | Query | 是 | test group _ | 参数模板的名称，需满足如下要求： 由英文、数字、和下划线 （）组成，以字母开头，不能包含中文，不能以下划线 （）结尾。 长度为8~64个字符。 |
| Parameter GroupDesc | String | Query | 否 | test group _ | 参数模板的描述，长度为 0~199个字符。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 |  | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Parameters | String | Query |  |  |  |  | 参数及其值的JSON串，参数的值都是字符串类型，例如 {"wait timeout":"864 _ |  |  |
|  |  |  |  |  |  |  |  | {"wait timeout":"864 _ |  |
|  |  |  |  |  |  |  | 00","innodb old blocks _ _ _ |  |  |
|  |  |  |  |  |  |  | time":"1000"} |  |  |
|  |  |  |  | 是 | {"wait timeout":"86400","i _ nnodb old blocks time":"1 _ _ _ 000"} |  |  |  |  |
| ResourceGr oupId | String | Query |  | 否 | rg-********** |  | 资源组ID。 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 514D1D87-E243- 4A5F-A87D- 2785C3****** | 请求ID。 |
| ParameterGrou pId | String | pcpg-************** | 参数模板ID。 您可以通过DescribeParameterGroups接口查看目标地域的参数模板列表，包括参数模板 ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "RegionId":"null", "DBType":"null", "DBVersion":"null", "ParameterGroupName":"null", "Parameters":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "ParameterGroupId":"",
 "RequestId":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | he specified parameter RegionId is not valid. |
| 400 | InvalidDBVersion.Mal formed | InvalidDBVersion.Malformed | The Specified DBVersion is not valid. |
| 400 | InvalidParameterGro upName.Malformed | InvalidParameterGroupName.Malf ormed | The Specified parameter ParameterGroupName is not valid. |
| 400 | NumberExceed.para meterGroupDesc | NumberExceed.parameterGroupD esc | The ParameterGroupDesc parameter`s number is exceed. |
| 400 | InvalidEngine.Unsup ported | InvalidEngine.Unsupported | The specified Engine does not support this feature. |
| 400 | ParamGroupsNameIn valid | ParamGroupsNameInvalid | The Specified parameter ParameterGroupName is not valid. |
| 404 | InvalidDBType.NotFo und | InvalidDBType.NotFound | The Specified DBType does not found. |

### DeleteAccount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| AccountNa me | String | Query | 是 | testacc | 账号名称。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | GdnRole.NotSupport | GdnRole.NotSupport | Specified gdn role is not support. |
| 400 | ConcurrentTaskExce eded | ConcurrentTaskExceeded | Concurrent task exceeding the allowed amount. |
| 400 | Account.DelError | Account.DelError | Instance %s remove Account crawl r error _ |
| 400 | Connect.Timeout | Connect.Timeout | Service can not connect to instance temporarily. |
| 401 | AccountActionForbid den | AccountActionForbidden | Some objects depend on the special account. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DeleteDatabase

云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| DBName | String | Query | 是 | testdb | 数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DeleteDBClusterEndpoint

调用DeleteDBClusterEndpoint接口释放PolarDB自定义集群地址。 云原生数据库 I参考

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-****************** | 集群ID。 |
| DBEndpoin tId | String | Query | 是 | pe-****************** | 自定义集群地址ID。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CD3FA5F3-FAF3- 44CA-AFFF- BAF869****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBEndpointId":"null" }
```

正常返回示例 `JSON` 格式云原生数据库 I参考

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DeleteDBNodes

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a42*********** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| DBNodeId | Repea tList | Query | 是 | pi-************ |  |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

云原生数据库 I参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6566B2E6-3157- 4B57-A693- AFB751****** | 请求ID。 |
| DBClusterId | String | pc-************** | 数据库集群ID。 |
| OrderId | String | 2035638******* | 订单ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBNodeId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBNodeNum. Malformed | InvalidDBNodeNum.Malformed | The number of parameter DBNode.N is not valid. |
| 403 | OperationDenied.DB NodeRole | OperationDenied.DBNodeRole | The operation is not permitted due to the role of node. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

**6.79.**

### DescribeDBClusterAuditLogCollector

调用DescribeDBClusterAuditLogCollector接口查看PolarDB集群的SQL采集功能（例如审计日志、SQL洞察等）是否开启。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

云原生数据库 I参考

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| CollectorStatus | String | Disabled | SQL采集功能的状态，取值范围如下： Enable：开启。 Disabled：关闭。 |
| RequestId | String | 59011D2B-2A38- 4207-A86C- 72BC1F882D19 | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "CollectorStatus":"",
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The DBClusterId provided does not exist in our records. |

### UpgradeDBClusterVersion

调用UpgradeDBClusterVersion接口升级PolarDB MySQL版集群的内核版本。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

云原生数据库 I参考

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 您可以通过 DescribeDBClusters接口查看账号下所有集群的详细信息（如集群ID）。 |
| UpgradePol icy | String | Query | 否 | HOT | 内核版本升级策略。取值： HOT ：热升级。 COLD ：冷升级。目前仅 PolarDB MySQL版8.0集群版支持该升级方式。 |
| UpgradeLa bel | String | Query | 否 | INNOVATE | 内核版本升级标签。取值固定为INNOVATE 。 当传入该参数时， UpgradePolicy 必须传入COLD 。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）内核版本升级任务的最早时间。格式为 YYYY- MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行内核版本升级任务。 |

|  |  |  | YYYY- |  |
|---|---|---|---|---|
|  |  | MM- |  |  |
|  |  | DDThh:mm:ssZ |  |  |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z |  | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |  |  |
|  |  |  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  |  |  | DDThh:mm:ssZ |  |  |
| FromTimeS ervice | Boole an | Query | 否 | false |  | 立即执行或定时执行内核版本升级。取值： false （默认值）：定时执行。 true ：立即执行。 调用该接口时无需使用该参数。 |  |  |
| UpgradeTy pe | String | Query | 否 | PROXY |  | 升级类型。取值： PROXY ：仅升级数据库代理（Proxy）。 DB ：仅升级内核引擎。 ALL （默认值）：同时升级数据库代理（Proxy）和内核引擎。 |  |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CAE6755F-B79A- 4861-B227- 801FE8****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ScheduleTaskExist | ScheduleTaskExist | The specified dbCluster already has a scheduled task. |
| 400 | InvalidUpgradeLabel. Malformed | InvalidUpgradeLabel.Malformed | The specified parameter UpgradeLabel is not valid. |
| 403 | OperationDenied.Up gradeType | OperationDenied.UpgradeType | The operation is not permitted due to gdn limit |
| 403 | IncorrectGdnStandby DBVersion | IncorrectGdnStandbyDBVersion | Current gdn standby cluster is not the latest db version. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### RevokeAccountPrivilege

调用RevokeAccountPrivilege接口移除PolarDB普通账号对数据库的访问权限。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| AccountNa me | String | Query | 是 | testacc | 账号名称。 仅支持普通账号，不支持高权限账号。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBName | String | Query | 是 | testdb | 数据库名称。支持同时传入多个数据库，多个数据库名称之间用英文逗号（,）分隔。 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null", "DBName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ResetAccount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |  |  |
| AccountNa me | String | Query | 是 | testacc | 账号名称。 仅支持重置高权限账号。 |  |  |
| AccountPas sword | String | Query | 否 | Pw123456 | 账号密码，密码需满足如下要求： 大写字母、小写字母、数字、特殊字符至少占三种。 长度为8~32位。 特殊字符为 !@#$%^&* () +-= 。 _ |  |  |
|  |  |  |  |  |  | !@#$%^&* |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |

|  | () +-= _ |
|---|---|

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | ConcurrentTaskExce eded | ConcurrentTaskExceeded | The number of concurrent tasks exceeds the quota. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBNodesClass

调用ModifyDBNodesClass接口变更PolarDB集群单个节点的规格。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ModifyType | String | Query | 是 | Upgrade | 变更类型，取值范围如下： Upgrade ：升级规格。 Downgrade ：降级规格。 |
| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、不超过64 个ASCII字符。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）升级配置任务的最早时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 仅当 ModifyType 取值为 Upgrade 时， 该参数生效。 开始时间的取值范围为未来 24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ，此处允许填入的开始时间范围为 2021-01- 14T09:00:00Z ~ 2021 -01-15T09:00:00Z 。 若该参数留空，默认立即执行升级配置任务。 |
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:00:00Z |  |  |

|  |  |  | 2021-01- |  |  |  |
|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |
|  |  |  |  | ~ | 2021 |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SubCategor y | String | Query | 否 | normal general _ | 集群子系列。取值范围如下： normal exclusive ： _ 独享规格。 normal general ：通 _ 用规格。 |
| DBNode | Repea tList | Query | 是 | pi-************* | 集群节点列表。 |
| -DBNodeId | String |  | 否 | pi-************* | 集群节点ID。 如果该参数传入后，DBNode.N.Target Class必填。N为从1开始的整数，最大值=16-当前节点数。 |
| - TargetClas s | String |  | 否 | polar.mysql.x4.medium | 变配节点的规格。 如果该参数传入后，DBNode.N.DBNod eId必填。N为从1开始的整数，最大值=16-当前节点数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 685F028C-4FCD- 407D-A559- 072D63****** | 请求ID。 |
| DBClusterId | String | pc-************* | 数据库集群ID。 |
| OrderId | String | 2035629****** | 订单ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "ModifyType":"null", "DBNode":"null" }
```

正常返回示例 `JSON` 格式云原生数据库 I参考

```json
{
 "RequestId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

### ModifyDBDescription

调用ModifyDBDescription接口修改PolarDB MySQL版数据库的备注说明。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |  |  |
| DBName | String | Query | 是 | testDB | 数据库名称。 |  |  |
| DBDescript ion | String | Query | 是 | DBDesc | 数据库备注说明，备注说明需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 |  |  |
|  |  |  |  |  |  | https |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

**返回数据**

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 5F295AAB-B599- 4F0E-96D0- DBFAB3****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBName":"null", "DBDescription":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterStorageSpace

调用ModifyDBClusterStorageSpace接口变更企业版按空间计费集群和标准版集群的存储空间。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| StorageSpa ce | Long | Query | 是 | 50 | 变更后的存储空间。单位： GB。 PolarDB MySQL标准版的存储空间取值范围： 20~32000。 |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| ClientToke n | String | Query | 否 | 6000170000591aed949d0f 54a343f1a4233c1e7d1c5c ****** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，保证在不同请求间唯一，大小写敏感、长度不超过64个ASCII字符。 |
|---|---|---|---|---|---|
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）升级配置任务的最早时间。格式为 YYYY-MM- DDThh:mm:ssZ（UTC） 。 仅当 ModifyType 取值为 Upgrade 时，该参数生效。 开始时间的取值范围为未来 24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ，此处允许填入的开始时间范围为 2021-01- 14T09:00:00Z ~ 2021 -01-15T09:00:00Z 。 若该参数留空，默认立即执行升级配置任务。 |
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ（UTC） 。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mm:ssZ（UTC） |  |

|  | ModifyType |
|---|---|
| Upgrade |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:00:00Z |  |  |

|  |  |  | 2021-01- |  |  |  |
|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |
|  |  |  |  | ~ | 2021 |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mm:ssZ（UTC） |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SubCategor y | String | Query | 否 | normal general _ | 集群子系列。取值范围如下： normal exclusive ： _ 独享规格 normal general ：通 _ 用规格 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 685F028C-4FCD- 407D-A559- 072D63****** | 请求ID。 |
| DBClusterId | String | pc-************* | 数据库集群ID。 |
| OrderId | String | 2035629****** | 订单ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "StorageSpace":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":"",
 "DBClusterId":"",
 "OrderId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | OperationDenied.Ro EqualSpec | OperationDenied.RoEqualSpec | must exist at least ro class equal with rw |

云原生数据库 I参考

### ModifyAccountPassword

调用ModifyAccountPassword接口修改PolarDB数据库的账号密码。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 |  |  |
| AccountNa me | String | Query | 是 | testacc | 账号名称。 |  |  |
| NewAccoun tPassword | String | Query | 是 | Pw123456 | 账号的新密码，需符合如下要求： 至少包含大写字母、小写字母、数字或特殊字符中的任意三种。 长度为8~32个字符。 特殊字符为 !@#$%^&* () +-= 。 _ |  |  |
|  |  |  |  |  |  | !@#$%^&* |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |  |  |

|  | () +-= _ |
|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

云原生数据库 I参考请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null", "NewAccountPassword":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | EngineMigration.Acti onDisabled | EngineMigration.ActionDisabled | Specified action is disabled while custins is in engine migration. |
| 400 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.87.**

### ModifyDBClusterAccessWhitelist

调用ModifyDBClusterAccessWhitelist接口创建或修改PolarDB集群的白名单（包括IP白名单和安全组）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityIps | String | Query | 否 | 10.23.12.24 | IP白名单分组中的IP地址或地址段。所有IP白名单分组累积支持1000个IP地址或地址段， 多个IP间用英文逗号（,）隔开，支持如下两种格式： IP地址形式，例如： 10.23.12.24。 CIDR形式，例如： 10.23.12.24/24（无类域间路由，24表示地址中前缀的长度，长度范围为 1~32）。 当WhiteListType 取值为IP 时该参数才支持配置。 |
| DBClusterI PArrayNam e | String | Query | 否 | default | IP白名单分组的名称。分组名称长度需为2~120个字符；由小写字母和数字组成；以字母开头，以字母或数字结尾。 如果传入的白名单分组名称不存在，则会创建该白名单分组。 如果传入的白名单分组名称已存在，则会修改该白名单分组。 不传入则修改default分组。 1个集群最多支持50个 IP白名单分组。 当WhiteListType 取值为IP 时该参数才支持配置。 |
| DBClusterI PArrayAttri bute | String | Query | 否 | hidden | IP白名单分组属性。设置为hidden 后控制台不可见。 已在控制台显示的IP白名单分组不支持隐藏。 当WhiteListType 取值为IP 时该参数才支持配置。 |
| WhiteListTy pe | String | Query | 否 | IP | 白名单类型。取值范围如下： IP ：IP白名单分组。 SecurityGroup ：安全组。 默认值为IP 。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityGr oupIds | String | Query | 否 | sg-********* | 安全组ID，多个安全组间用英文逗号（,）隔开。 1个集群最多支持3个安全组。 当WhiteListType 取值为SecurityGroup 时该参数才支持配置。 |
| ModifyMod e | String | Query | 否 | Cover | IP白名单的修改方式，取值范围如下： Cover ：覆盖原IP白名单 （默认值）。 Append ：追加IP。 Delete ：删除IP。 当WhiteListType 取值为IP 时该参数才支持配置。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | NumberExceed.secur ityGroupIds | NumberExceed.securityGroupIds | The number of SecurityGroupIds exceeds 10. |
| 403 | SecurityIPList.Duplic ate | SecurityIPList.Duplicate | Specified same security IP already exists. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.88.**

### ModifyDBClusterAndNodesParameters

调用ModifyDBClusterAndNodesParameters接口修改集群参数并应用到指定节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| DBNodeIds | String | Query | 否 | pi-****************,pi- **********, | 节点ID。通过设置该参数可以修改集群参数和指定节点的参数。多个节点ID间用英文逗号 （,）分隔。 当该参数为空时，则表示只修改集群参数。 |
| Parameters | String | Query | 否 | {"wait timeout":"86","inno _ db old blocks time":"10"} _ _ _ | 参数及参数值的JSON串。 |
| Parameter GroupId | String | Query | 否 | pcpg-************** | 参数模板ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）任务的最早时间。 格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行任务。 |
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTime 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。 例如当设置 PlannedStartTime 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021-01- 14T09:30:00Z 开始执行。 |
| FromTimeS ervice | Boole an | Query | 否 | false | 立即执行或定时执行修改参数并重启集群。取值： false （默认值）：定时执行 true ：立即执行 |
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

|  |  | YYYY-MM- |  |
|---|---|---|---|
|  | DDThh:mm:ssZ |  |  |

| 09:30:00Z |  |
|---|---|

|  |  |  | PlannedStartTime |  |
|---|---|---|---|---|
|  |  |  | 为 |  |

|  |  | 2021-01- |  |
|---|---|---|---|
|  | 14T09:30:00Z |  |  |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 9B7BFB11-C077- 4FE3-B051- F69CEB****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | InvalidDBType.Malfor med | InvalidDBType.Malformed | The Specified DBType is not valid. |
| 400 | ParamCollationServe rNotValid | ParamCollationServerNotValid | This param collation server is not _ valid. |
| 400 | MinorVersionNotSup port | MinorVersionNotSupport | Custins minor version does not support current action. |
| 400 | ScheduleTaskExist | ScheduleTaskExist | The specified dbCluster already has a scheduled task. |
| 400 | ParamTypeException | ParamTypeException | Param is isClusterAvailable, not allow to change alone |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBCluster.Not Found | InvalidDBCluster.NotFound | The specified DBClusterId is not found. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBNodeId.Not Found | InvalidDBNodeId.NotFound | The DBNodeId provided does not exist in our records. |

**6.89.**

### ModifyDBClusterAuditLogCollector

调用DescribeDBClusterAuditLogCollector接口开启或关闭PolarDB集群的SQL采集功能（例如审计日志、SQL 洞察等）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |
| CollectorSt atus | String | Query | 是 | Enable | 开启或关闭SQL采集功能，取值范围如下： Enable ：开启。 Disabled ：关闭。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 22C0ACF0-DD29- 4B67-9190- B7A48C****** | 请求ID。 |

**示例**

请求示例云原生数据库 I参考

```json
  HTTP/1.1
{ "DBClusterId":"null", "CollectorStatus":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

### ModifyDBClusterDescription

调用ModifyDBClusterDescription接口修改PolarDB集群名称。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |  |  |
| DBClusterD escription | String | Query | 是 | ClusterDescriptionTest | 集群名称，集群名称需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 |  |  |
|  |  |  |  |  |  | https |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

|  |  |  |  | PolarD | B MySQL集群版开发指南·A |
|---|---|---|---|---|---|

I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D0CEC6AC-7760- 409A-A0D5- E6CD86****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBClusterDescription":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterEndpoint

调用ModifyDBClusterEndpoint接口修改PolarDB的集群地址属性，包括读写模式、新节点是否自动加入本地址、 一致性级别、事务拆分、主库是否接受读、连接池等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

|  | 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|---|---|
|  | DBEndpoin tId | String | Query | 是 |  | pe-************** |  | 集群地址ID。 |  |
|  | Nodes | String | Query | 否 |  | pi-**************,pi- ************* |  | 加入目标地址的读负载节点， 多个节点间用英文逗号（,）分隔。 默认为原有节点。 PolarDB MySQL版需要传入节点ID。 PolarDB PostgreSQL版和 PolarDB PostgreSQL版 （兼容Oracle）需要传入节点角色名称，例如 Writer,Reader1,Rea der2 。 ReadWriteMode 取值为ReadOnly 时，支持只挂载一个节点。但当此节点故障时，该地址可能会有最多1小时的不可用，请勿用于生产环境。因此，推荐至少选择2个节点，以提升可用性。 ReadWriteMode 取值为ReadWrite 时，至少要选择2个节点。 PolarDB MySQL版支持选择任意两个节点。当两个节点都是只读节点时， 写请求都会发往主节点。 PolarDB PostgreSQL版和PolarDB PostgreSQL 版（兼容Oracle）必须包含主节点。 |  |
|  | ReadWrite Mode | String | Query | 否 |  | ReadWrite |  | 读写模式，取值范围如下： ReadWrite ：可读可写 （自动读写分离） ReadOnly ：只读 |  |
|  | AutoAddNe wNodes | String | Query | 否 |  | Enable |  | 新节点是否自动加入本地址， 取值范围如下： Enable ：是 Disable ：否（默认值） |  |
|  |  |  |  |  |  |  |  | 集群地址的高级配置，格式为 JSON，目前支持设置一致性级别、事务拆分、主库是否接受读和连接池等。 设置负载均衡策略，格式为 {\"LoadBalancePoli |  |
|  |  |  |  |  |  |  |  |  | {\"LoadBalancePoli |
|  |  |  |  |  |  |  |  | cy\":\"负载均衡策略 |  |
|  |  |  |  |  |  |  |  | \"} |  |

|  |  | Writer,Reader1,Rea |  |
|---|---|---|---|
|  | der2 |  |  |

云原生数据库

|  | 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 1 ：基于活跃请求数负说明载均衡 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | EndpointCo nfig | String | Query | 否 |  |  |  | 设置主库是否接受读，格式为 {\"MasterAcceptRea |  |  |
|  |  |  |  |  |  |  |  |  | {\"MasterAcceptRea |  |
|  |  |  |  |  |  |  |  | ds\":\"主库是否接受读 |  |  |
|  |  |  |  |  |  |  |  | \"} |  |  |
|  |  |  |  |  |  |  |  |  | {\"DistributedTran |  |
|  |  |  |  |  |  |  |  | saction\":\"事务拆分 |  |  |
|  |  |  |  |  |  |  |  | \"} |  |  |
|  |  |  |  |  |  | {"ConsistLevel":"1","Distri butedTransaction":"on","M asterAcceptReads":"off","C |  |  |  |  |
|  |  |  |  |  |  |  |  |  | {\"EnableHtapImci\ |  |
|  |  |  |  |  |  |  | ptReads":"off","C | ":\"行存/列存自动引流 |  |  |
|  |  |  |  |  |  | onnectionPersist": "on"} |  |  |  |  |
|  |  |  |  |  |  |  |  | \"} |  |  |

|  |  | {\"ConsistLevel\": |  |
|---|---|---|---|
|  | \"一致性级别\"} |  |  |

|  |  | {\"ConnectionPersi |
|---|---|---|
|  | st\":\"连接池\"} |  |

|  |  | {\"MaxParallelDegr |
|---|---|---|
|  | ee\":\"并行查询\"} |  |

云原生数据库 I参考

|  | 参数名称 | 类型 | 位置 | 是否必选 |  | 示例 |  | 设置是否开启过载保护，格说明式 |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  | 为 | {\"EnableOverloadT |  |
|  |  |  |  |  |  |  |  | hrottle\":\"是否开启过 |  |  |
|  |  |  |  |  |  |  |  | 载保护\"} |  |  |
|  |  |  |  |  |  |  |  |  | {\"ConsistLevel\": |  |
|  |  |  |  |  |  |  |  | \"1\",\"DistributedTr |  |  |
|  |  |  |  |  |  |  |  | ansaction\":\"on\",\" |  |  |
|  |  |  |  |  |  |  |  | ConnectionPersist\":\ |  |  |
|  |  |  |  |  |  |  |  | "Session\",\"MasterAc |  |  |
|  |  |  |  |  |  |  |  | ceptReads\":\"on\"} |  |  |
|  | DBEndpoin tDescriptio n | String | Query | 否 |  | test |  | 开启事务拆分；一致性级别取值为1 或2 时，支持地址名称。 开启事务拆分。 |  |  |
|  | ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |  |  |

|  |  |  |  | PolarD | B MySQL集群版开发指南·A |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| OwnerAcco unt | String | Query | 否 |  |  |
| EndpointTy pe | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | CD3FA5F3-FAF3- 44CA-AFFF- BAF869****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "DBEndpointId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidEndpointConfi g.Malformed | InvalidEndpointConfig.Malformed | The specified parameter EndpointConfig is not valid. |
| 400 | InvalidDBEndpointId. Malformed | InvalidDBEndpointId.Malformed | The specified parameter DBEndpointId is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | EndpointStatus.NotS upport | EndpointStatus.NotSupport | Current endpoint status does not support this operation. |

### ModifyDBClusterMigration

调用ModifyDBClusterMigration接口切换或回滚RDS一键升级到PolarDB的迁移任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

云原生数据库 I参考

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SecurityTo ken | String | Query | 否 |  |  |
| DBClusterI d | String | Query | 是 | pc-************** | PolarDB集群ID。 |
| SourceRDS DBInstance Id | String | Query | 是 | rm-************ | 源RDS实例ID。 |
| NewMasterI nstanceId | String | Query | 是 | pc-************** | 新的实例ID或集群ID，取值范围如下： 切换前，填写PolarDB集群 ID进行切换。 切换后，填写RDS实例ID进行回滚。 |
| SwapConne ctionString | String | Query | 否 | false | 是否需要切换连接地址，取值： true ：带地址切换（应用程序不用改连接配置）。 false ：不带地址切换 （应用程序需要改为新的 PolarDB连接配置）。 默认为false 。 |
| Connection Strings | String | Query | 否 | {"rm- 2ze73el581cs*****.mysql. pre.rds.aliyuncs.com":"pc- 2ze8200s298e*****.mysql. polardb.pre.rds.aliyuncs.co m","rm- 2ze73el581cs86*****.mys ql.pre.rds.aliyuncs.com":"t est- p*****.mysql.polardb.pre.r ds.aliyuncs.com"} | 需要切换的具体连接地址。取值为需要两两交换的地址对应的JSON串。 当 SwapConnectionStrin g取值为true时生效。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |
| RegionId | String | Host | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A1B303A5-653F- 4AEE-A598- 023FF9****** | 请求ID。 |

云原生数据库 I参考

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "SourceRDSDBInstanceId":"null", "NewMasterInstanceId":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyDBClusterMonitor

调用ModifyDBClusterMonitor接口修改PolarDB集群的监控数据采集频率。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| Period | String | Query | 是 | 5 | 监控的采集间隔，取值为5 或60 ，单位为秒。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 75B92353-73B4- 447B-8477- C85F3C****** | 请求ID。 |

云原生数据库 I参考

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "Period":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectPerfFrequen cyType | OperationDenied.DBInstanceMoni torPeriod | Current DB instance does not support this monitor period. |
| 404 | InvalidDBInstanceNa me.NotFound | InvalidDBInstanceId.NotFound | The DBInstanceId provided does not exist in our records. |

### GrantAccountPrivilege

调用GrantAccountPrivilege接口授权普通账号访问PolarDB集群的某个数据库。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| AccountNa me | String | Query | 是 | testacc | 账号名。 |
| DBName | String | Query | 是 | testdb 1,testdb 2 _ _ | 需要授权的数据库名称。支持同时对一个或多个数据库授权，多个数据库名称之间用英文逗号（,）隔开。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccountPri vilege | String | Query | 是 | ReadWrite,ReadOnly | 账号权限，取值范围如下： ReadWrite ：读写。 ReadOnly ：只读。 DMLOnly ：只允许DML 。 DDLOnly ：只允许 DDL。 ReadIndex ：只读+索引。 AccountPrivilege 需与DBName 输入的参数数量保持一致，且顺序对应。例如，输入DBName 为 test db 1,testdb 2 ，Ac _ _ countPrivilege 为 ReadWrite,ReadOnly ，则表示授予目标账号对数据库testdb1 的读 _ 写权限，对数据库testdb2 的只 _ 读权限。 |

|  |  |  |  | test |  |  |
|---|---|---|---|---|---|---|
|  |  |  | db 1,testdb 2 _ _ |  |  |  |
|  |  |  | ReadWrite,ReadOnly |  |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627***** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null", "DBName":"null", "AccountPrivilege":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | EngineMigration.Acti onDisabled | EngineMigration.ActionDisabled | Specified action is disabled while custins is in engine migration. |
| 400 | LockTimeout | LockTimeout | The request processing has failed due to lock timeout. |
| 400 | Account.UpdateError | Account.UpdateError | Instance %s update Account %s error |
| 403 | IncorrectAccountPrivi legeType | IncorrectAccountPrivilegeType | Current account privilege type does not support this operation. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### ModifyAccountDescription

调用ModifyAccountDescription接口修改PolarDB数据库账号的备注信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
  HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |  |  |
| AccountNa me | String | Query | 是 | testacc | 账号名。 |  |  |
| AccountDe scription | String | Query | 是 | AccDesc | 账号备注信息，备注信息如满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2-256个字符。 |  |  |
|  |  |  |  |  |  | https |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| AccessKeyI d | String | Query | 否 |  |  |  |  |
| Action | String | Query | 否 |  |  |  |  |
| OwnerId | Long | Query | 否 |  |  |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

| 云原生数据库 |  |  |  | PolarD | B MySQL集群版开发指南·A I参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2FED790E-FB61- 4721-8C1C- 07C627****** | 请求ID。 |

**示例**

请求示例

```json
  HTTP/1.1
{ "DBClusterId":"null", "AccountName":"null", "AccountDescription":"null" }
```

正常返回示例 `JSON` 格式

```json
{
 "RequestId":""
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeAccounts

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |

| olarDB MySQ | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccountNa me | String | Query | 否 | test acc _ | 账号名称。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数。默认值为1 。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围： 30 50 100 默认值为30 。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageRecordCou nt | Integer | 1 | 本页记录数。 |
| RequestId | String | 155462B9-205F- 4FFC-BB43- 4855FE****** | 请求ID。 |
| PageNumber | Integer | 1 | 页码。 |
| Accounts | Array |  | 账号信息详情。 |
| - DatabasePrivile ges | Array |  | 目标账号拥有的数据库权限详情。 |
| --DBName | String |  |  |
| -- AccountPrivileg e | String |  |  |
| -AccountStatus | String | Available | 账号状态。取值范围： Creating ：创建中。 Available ：可用。 Deleting ：删除中。 |
| - AccountDescript ion | String | test | 账号备注。 |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - PrivilegeExceed ed | String |  |  |
| - AccountPasswor dValidTime | String | undefined | 密码过期时间。 |
| -AccountType | String | Normal | 账户类型。取值范围： Normal ：普通账号。 Super ：高权限账号。 |
| - AccountLockSta te | String | UnLock | 账号锁定状态。取值范围： UnLock ：未锁定。 Lock ：锁定。 |
| -AccountName | String | test acc _ | 账号名。 |
| - AccountPasswor d | String | Test1111 | 账号密码。 |

**示例**

请求示例

```
&DBClusterId=pc-***************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "PageRecordCount":1,
 "RequestId":"155462B9-205F-4FFC-BB43-4855FE******",
 "PageNumber":1,
 "Accounts":{
  "AccountDescription":"test",
  "AccountStatus":"Available",
  "PrivilegeExceeded":"",
  "AccountLockState":"UnLock",
  "-DatabasePrivileges":{
   "AccountPrivilege":"",
   "DBName":""
  },
  "AccountPasswordValidTime":"undefined",
  "AccountType":"Normal",
  "AccountName":"test_acc",
  "AccountPassword":"Test1111"
 }
}
```

云原生数据库 I参考

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter PageSize is not valid. |
| 400 | InvalidPageNumber. Malformed | InvalidPageNumber.Malformed | The specified parameter PageNumber is not valid. |
| 400 | Database.ConnectErr or | Database.ConnectError | db instance %s connect failed, please check instance status and database processlist |
| 400 | Account.QueryError | Account.QueryError | Instance %s query account error |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |

### DescribeBackupTasks

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-*************** | 集群ID。 |
| BackupJobI d | String | Query | 否 | 11111111 | 备份任务ID。 |
| BackupMod e | String | Query | 否 | Manual | 备份模式，取值范围如下： Automated ：系统自动备份 Manual ：手动备份 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | FA8C1EF1-E3D4- 44D7-B809- 823187****** | 请求ID。 |

|  | 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 | P |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| Items | Array |  | 备份任务详情。 |  |  |
| -StartTime | String | 2020-08- 08T07:24:01Z | 备份任务开始时间（UTC），格式为 YYYY-MM- DDThh:mm:ssZ 。 |  |  |
|  |  |  |  | YYYY-MM- |  |
| -Process | String | 0 | 备份任务进度百分比。 |  |  |
| -BackupJobId | String | 11111111 | 备份任务ID。 |  |  |
| -JobMode | String | Automated | 备份模式，取值范围如下： Automated ：系统自动备份 Manual ：手动备份 |  |  |
| - BackupProgress Status | String | NoStart | 备份任务状态，取值范围如下： NoStart ：未开始 Preparing ：准备中 Waiting ：等待中 Uploading ：上传中 Checking ：检查中 Finished ：已完成 |  |  |
| -TaskAction | String | NormalBackupTask | 备份任务类型，取值范围如下： TempBackupTask ：临时备份任务 NormalBackupTask ：普通备份任务 |  |  |

|  | DDThh:mm:ssZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeBackupTasks &DBClusterId=pc-***************
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"FA8C1EF1-E3D4-44D7-B809-823187******",
 "Items":{
  "JobMode":"Automated",
  "TaskAction":"NormalBackupTask",
  "StartTime":"2020-08-08T07:24:01Z",
  "BackupProgressStatus":"NoStart",
  "Process":"0",
  "BackupJobId":"11111111"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |
| 400 | InvalidBackupMode. Malformed | InvalidBackupMode.Malformed | The specified parameter BackupMode is not valid. |

### DescribeDatabases

调用DescribeDatabases接口查询PolarDB指定集群的数据库详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| DBName | String | Query | 否 | test db _ | 数据库名。 不支持填入多个数据库名称。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 50 100 默认值为30 。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageRecordCou nt | Integer | 1 | 本页记录数。 |
| Databases | Array |  | 数据库信息详情。 |
| -Accounts | Array |  | 数据库账号信息详情。 当集群为PolarDB MySQL版时，不含高权限账号。 |
| --PrivilegeStatus | String |  |  |
| --AccountStatus | String |  |  |
| -- AccountPrivileg e | String |  |  |
| --AccountName | String |  |  |
| -DBDescription | String | test des _ | 数据库备注。 |
| -DBStatus | String | Running | 数据库状态，取值范围如下： Creating ：创建中 Running ：使用中 Deleting ：删除中 |
| -DBName | String | test db _ | 数据库名称。 |
| -Engine | String | MySQL | 数据库引擎类型，取值范围如下： MySQL Oracle PostgreSQL |
| -MasterID | String | 2 | 多主集群（库表）版的数据库所对应的主节点ID。 |
| - CharacterSetNa me | String | utf8mb4 | 字符集，详情请参见字符集表。 |

| olarDB MySQL集 | 群版开发指南·AP |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | E1DF8CA6-2300- 448B-9ABF- 760C4B****** | 请求ID。 |
| PageNumber | Integer | 1 | 页码。 |

**示例**

请求示例

```
&DBClusterId=pc-**************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "PageRecordCount":1,
 "Databases":{
  "CharacterSetName":"utf8mb4",
  "DBDescription":"test_des",
  "DBName":"test_db",
  "MasterID":"2",
  "-Accounts":{
   "AccountStatus":"",
   "AccountPrivilege":"",
   "PrivilegeStatus":"",
   "AccountName":""
  },
  "DBStatus":"Running",
  "Engine":"MySQL"
 },
 "RequestId":"E1DF8CA6-2300-448B-9ABF-760C4B******",
 "PageNumber":1
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter PageSize is not valid. |
| 400 | InvalidPageNumber. Malformed | InvalidPageNumber.Malformed | The specified parameter PageNumber is not valid. |

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | Database.ConnectErr or | Database.ConnectError | db instance %s connect failed, please check instance status and database processlist |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.99.**

### DescribeDBClusterAvailableResources

调用DescribeDBClusterAvailableResources接口查询PolarDB集群可售卖资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| PayType | String | Query | 是 | Postpaid | 付费类型，取值范围如下： Postpaid ：按量付费 （也称后付费或按小时付费）。 Prepaid ：包年包月 （也称预付费）。 |
| DBType | String | Query | 否 | MySQL | 数据库引擎类型，取值范围如下： MySQL 。 PostgreSQL 。 Oracle 。 |
| DBVersion | String | Query | 否 | 5.6 | 数据库引擎版本号。 MySQL 版本号取值范围如下： 5.6 。 5.7 。 8.0 。 PostgreSQL版本号取值范围如下： 11 。 14 。 Oracle版本号取值为11 。 当传入DBType 参数时，该参数必填。 |
| DBNodeCla ss | String | Query | 否 | polar.mysql.x4.large | 节点规格，详情请参见计算节点规格。 |

| olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 否 | cn-hangzhou | 地域ID。默认为cn- hangzhou 。 可通过接口 DescribeRegions查看可用的地域。 |
| ZoneId | String | Query | 否 | cn-hangzhou-i | 可用区ID。 可通过 DescribeRegions查看可用区。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| AvailableZones | Array |  | 可售卖的资源信息列表。 |
| - SupportedEngin es | Array |  | 可售卖引擎列表。 |
| -- AvailableResour ces | Array |  | 可售卖的资源列表。 |
| ---DBNodeClass | String | polar.mysql.x4.large | 节点规格。 |
| ---Category | String | Normal | 集群系列，取值范围如下： Normal ：集群版。 Basic ：单节点。 ArchiveNormal ：高压缩引擎（X- Engine）。 NormalMultimaster ：多主集群（库表）。 SENormal ：标准版。 仅 PolarDB MySQL 版支持单节点产品系列。 仅 PolarDB MySQL 版 8.0 版本的集群，支持高压缩引擎（X-Engine）和多主集群（库表）系列。 |
| --Engine | String | mysql57 | 数据库引擎版本。 |
| -ZoneId | String | cn-hangzhou-i | 可用区ID。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 2B19F698-8FFC- 4918-B9E2- 58D878****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClusterAvailableResources &PayType=Postpaid
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"2B19F698-8FFC-4918-B9E2-58D878******",
 "AvailableZones":{
  "-SupportedEngines":{
   "--AvailableResources":{
    "Category":"",
    "DBNodeClass":""
   },
   "Engine":""
  },
  "ZoneId":"cn-hangzhou-i",
  "RegionId":"cn-hangzhou"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBVersion.Mal formed | InvalidDBVersion.Malformed | The Specified DBVersion is not valid. |

**6.100.**

### DescribeDBClustersWithBackups

调用DescribeDBClustersWithBackups查询某地域下包含备份集的PolarDB集群详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|---|---|
| ResourceGr oupId | String | Query | 否 | rg-************ | 资源组ID。 |  |  |
| RegionId | String | Query | 是 | cn-hangzhou | 地域ID。 可通过接口 DescribeRegions查看地域信息详情。 |  |  |
| DBClusterI ds | String | Query | 否 | pc-************** | 集群ID，支持传入多个集群 ID，集群ID之间用英文逗号 （,）分隔。 |  |  |
| DBClusterD escription | String | Query | 否 | test | 集群名称，集群名称需满足如下要求： 不能以 http:// 或 https :// 开头。 长度为2~256个字符。 |  |  |
|  |  |  |  |  |  | https |  |
| DBType | String | Query | 否 | MySQL | 数据库引擎类型，取值范围如下： MySQL 。 PostgreSQL 。 Oracle 。 |  |  |
| IsDeleted | Intege r | Query | 否 | 0 | 集群是否已删除，取值范围如下： 0 ：未删除。 1 ：已删除。 |  |  |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 。 50 。 100 。 默认值为30。 |  |  |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |  |  |

|  |  | http:// |
|---|---|---|
|  | :// |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBVersion | String | Query | 否 | 8.0 | 数据库引擎版本号。 MySQL版本号取值范围如下： 5.6 。 5.7 。 8.0 。 PostgreSQL版本号取值范围如下： 11 。 14 。 Oracle版本号取值为11 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Items | Array |  |  |
| -DeletedTime | String | 2022-05- 12T03:25:37Z | 集群删除时间。 |
| -VpcId | String | vpc- ****************** | 专有网络ID。 |
| -ExpireTime | String | 2022-09- 14T16:00:00Z | 到期时间。 仅付费方式为Prepaid（包年包月）的集群会返回具体参数值，Postpaid（按量付费）集群则返回空值。 |
| -Expired | String | false | 集群是否过期。 仅付费方式为Prepaid（包年包月）的集群支持返该参数。 |
| -CreateTime | String | 2022-05- 09T09:33:51Z | 集群创建时间。 |
| -DBNodeClass | String | polar.mysql.x4.medi um | 节点规格。 |
| -PayType | String | Postpaid | 付费类型，取值范围如下： Postpaid ：按量付费。 Prepaid ：预付费（包年包月）。 |
| -DBType | String | MySQL | 数据库引擎类型。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -LockMode | String | Unlock | 集群的锁定状态，取值范围如下： Unlock ：正常。 ManualLock ：手动触发锁定。 LockByExpiration ：集群过期自动锁定。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| -DeletionLock | Integer | 0 | 集群删除的锁定状态，取值范围如下： 0 ：未锁定，可删除集群。 1 ：锁定，不可删除集群。 |
| -DBVersion | String | 8.0 | 数据库引擎版本。 |
| -DBClusterId | String | pc-**************** | 集群ID。 |
| - DBClusterStatus | String | Running | 集群状态，取值范围如下： Creating：创建中。 Running：运行中。 Deleting：释放中。 Rebooting：重启中。 DBNodeCreating：正在增加节点。 DBNodeDeleting：正在删除节点。 ClassChanging：正在变更节点规格。 NetAddressCreating：正在创建网络连接。 NetAddressDeleting：正在删除网络连接。 NetAddressModifying：正在修改网络连接 。 Deleted：已释放。 |
| -IsDeleted | Integer | 1 | 集群是否已释放，取值范围如下： 1：已释放。 0：未释放。 |
| - DBClusterNetwo rkType | String | VPC | 集群的网络类型。 |
| - DBClusterDescri ption | String | test | 集群名称。 |
| -ZoneId | String | cn-hangzhou-h | 可用区ID。 |
| -Engine | String | POLARDB | 集群引擎。 |
| RequestId | String | F8529AA2-522F- 4B30-B80B- 8F7D39****** | 请求ID。 |

| 云原生数据库 |  |  | PolarDB MySQL集群版开发指南·A I参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页数。 |
| PageRecordCou nt | Integer | 1 | 本页集群数量。 |
| TotalRecordCou nt | Integer | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBClustersWithBackups &RegionId=cn-hangzhou
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":1,
 "PageRecordCount":1,
 "RequestId":"F8529AA2-522F-4B30-B80B-8F7D39******",
 "PageNumber":1,
 "Items":{
  "DeletionLock":0,
  "IsDeleted":1,
  "ZoneId":"cn-hangzhou-h",
  "DeletedTime":"2022-05-12T03:25:37Z",
  "DBClusterStatus":"Running",
  "CreateTime":"2022-05-09T09:33:51Z",
  "DBClusterId":"pc-****************",
  "DBClusterDescription":"test",
  "Expired":"false",
  "PayType":"Postpaid",
  "DBType":"MySQL",
  "LockMode":"Unlock",
  "DBClusterNetworkType":"VPC",
  "DBNodeClass":"polar.mysql.x4.medium",
  "DBVersion":"8.0",
  "VpcId":"vpc-******************",
  "RegionId":"cn-hangzhou",
  "ExpireTime":"2022-09-14T16:00:00Z",
  "Engine":"POLARDB"
 }
}
```

**错误码**

云原生数据库 I参考

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidRegionId.Malfo rmed | InvalidRegionId.Malformed | The specified parameter RegionId is not valid. |
| 400 | InvalidPageSize.Malf ormed | InvalidPageSize.Malformed | The specified parameter PageSize is not valid. |
| 400 | InvalidPageNumber. Malformed | InvalidPageNumber.Malformed | The specified parameter PageNumber is not valid. |
| 500 | InternalError | InternalError | The request processing has failed due to some unknown error, exception or failure. |
| 503 | ServiceUnavailable | ServiceUnavailable | The request has failed due to a temporary failure of the server. |

### DescribeDetachedBackups

查询已被释放的PolarDB集群中备份集详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| BackupId | String | Query | 否 | 111111111 | 备份ID。 |
| BackupStat us | String | Query | 否 | Success | 备份状态，取值范围如下： Success ：备份完成 Failed ：备份失败 |
| BackupMod e | String | Query | 否 | Manual | 备份模式，取值范围如下： Automated ：系统自动备份 Manual ：手动备份 |
| BackupReg ion | String | Query | 否 | cn-hangzhou | 跨地域备份的目的地域。 当前仅PolarDB MySQL 版支持该参数。 |
| StartTime | String | Query | 是 | 2020-05-01T00:00Z | 查询开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| EndTime | String | Query | 是 | 2020-05-14T00:00Z | 查询结束时间，查询结束时间需晚于开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 50 100 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalRecordCou nt | String | 50 | 总记录数。 |
| PageRecordCou nt | String | 15 | 本页记录数。 |
| RequestId | String | 717B2382-BB14- 4DCB-BBC2- 32DBE0****** | 请求ID。 |
| PageNumber | String | 1 | 页码。 |
| Items | Array |  | 备份集详情。 |
| -BackupSetSize | String | 7251056 | 备份文件大小，单位为Byte。 因为快照之间存在共享数据块，因此删除目标快照备份后释放的空间会远小于该备份文件的大小。 |
| -ConsistentTime | String | 1589253947 | 一致性快照的时间点，格式为Unix时间戳，单位为秒。 |

云原生数据库 I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -StoreStatus | String | Disabled | 是否允许删除备份集，取值范围如下： Enabled ：允许删除 Disabled ：不允许删除 |
| -BackupStatus | String | Success | 备份状态，取值范围如下： Success ：备份完成 Failed ：备份失败 |
| -BackupType | String | FullBackup | 备份类型，仅支持全量备份，取值固定为FullBackup 。 |
| - BackupStartTim e | String | 2020-05- 12T03:25:44Z | 本次备份开始时间（UTC时间）。 |
| -IsAvail | String | 1 | 备份集是否可用，取值范围如下： 0 ：不可用 1 ：可用 |
| - BackupEndTime | String | 2020-05- 12T03:25:55Z | 本次备份结束时间（UTC时间）。 |
| -BackupId | String | 111111111 | 备份ID。 |
| -DBClusterId | String | pc-************** | 集群ID。 |
| -BackupsLevel | String | Level-2 | 备份集级别，取值范围如下： Level-1 ：一级备份 Level-2 ：二级备份 |
| -BackupMode | String | Manual | 备份模式，取值范围如下： Automated ：系统自动备份 Manual ：手动备份 |
| -BackupMethod | String | Snapshot | 数据备份方法，仅支持快照备份，取值固定为Snapshot 。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDetachedBackups &DBClusterId=pc-**************** &StartTime=2020-05-01T00:00Z &EndTime=2020-05-14T00:00Z
```

&公共请求参数正常返回示例云原生数据库 I参考 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":"50",
 "PageRecordCount":"15",
 "RequestId":"717B2382-BB14-4DCB-BBC2-32DBE0******",
 "PageNumber":"1",
 "Items":{
  "BackupMethod":"Snapshot",
  "BackupsLevel":"Level-2",
  "BackupMode":"Manual",
  "DBClusterId":"pc-**************",
  "BackupId":"111111111",
  "IsAvail":"1",
  "BackupSetSize":"7251056",
  "StoreStatus":"Disabled",
  "BackupEndTime":"2020-05-12T03:25:55Z",
  "ConsistentTime":"1589253947",
  "BackupStartTime":"2020-05-12T03:25:44Z",
  "BackupType":"FullBackup",
  "BackupStatus":"Success"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 404 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 400 | InvalidBackupStatus. Malformed | InvalidBackupStatus.Malformed | The specified parameter BackupStatus is not valid. |
| 400 | InvalidBackupMode. Malformed | InvalidBackupMode.Malformed | The specified parameter BackupMode is not valid. |
| 400 | InvalidStartTime.Malf ormed | InvalidStartTime.Malformed | The specified parameter StartTime is not valid. |
| 400 | InvalidEndTime.Malfo rmed | InvalidEndTime.Malformed | The specified parameter EndTime is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeRegions

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 云原生数据库 I参考

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyI d | String | Query | 否 |  |  |
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3F9E6A3B-C13E- 4064-A010- 18582A****** | 请求ID。 |
| Regions | Array |  | 地域信息列表。 |
| -Zones | Array |  | 可用区列表。 |
| --ZoneId | String |  |  |
| --VpcEnabled | Boolean |  |  |
| -RegionId | String | cn-hangzhou | 地域ID。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"3F9E6A3B-C13E-4064-A010-18582A******",
 "Regions":{
  "-Zones":{
   "VpcEnabled":"",
   "ZoneId":""
  },
  "RegionId":"cn-hangzhou"
 }
}
```

### ModifyDBNodesParameters

调用ModifyDBNodesParameters接口修改单个节点的参数并应用到指定节点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************** | 集群ID。 |
| DBNodeIds | String | Query | 是 | pi-****************， pi- **************** | 节点ID。支持传入多个节点 ID，多个节点ID间用英文逗号 （,）分隔。 |
| Parameters | String | Query | 否 | {"wait timeout":"86","inno _ db old blocks time":"10"} _ _ _ | 参数及参数值的JSON串。 |
| Parameter GroupId | String | Query | 否 | pcpg-************** | 参数模板ID。 |
| PlannedSta rtTime | String | Query | 否 | 2022-04-28T14:00:00Z | 开始执行定时（即在目标时间段内执行）内核版本升级任务的最早时间。格式为YYYY- MM- DDThh:mm:ssZ（UTC）。 |
| PlannedEn dTime | String | Query | 否 | 2022-04-28T14:30:00Z | 开始执行目标定时任务的最晚时间。格式为YYYY-MM- DDThh:mm:ssZ（UTC）。 |
| FromTimeS ervice | Boole an | Query | 否 | false | 立即执行或定时执行修改参数并重启取值： false（默认值）：定时执行 true：立即执行 |
| AccessKeyI d | String | Query | 否 |  |  |

| P I | olarDB MySQ 参考 | L集群版开 | 发指南·AP |  |  | 云原生数据库 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccessKeyI d | String | Query | 否 |  |  |
| Action | String | Query | 否 |  |  |
| OwnerId | Long | Query | 否 |  |  |
| ResourceO wnerAccou nt | String | Query | 否 |  |  |
| ResourceO wnerId | Long | Query | 否 |  |  |
| OwnerAcco unt | String | Query | 否 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | EBEAA83D-1734- 42E3-85E3- E25F6E****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyDBNodesParameters &DBClusterId=pc-************** &DBNodeIds=pi-****************， pi-****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"EBEAA83D-1734-42E3-85E3-E25F6E******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameters.Fo rmat | InvalidParameters.Format | Specified parameters is not valid. |
| 400 | InvalidDBType.Malfor med | InvalidDBType.Malformed | The Specified DBType is not valid. |
| 404 | InvalidDBCluster.Not Found | InvalidDBCluster.NotFound | The specified DBClusterId is not found. |

云原生数据库 I参考

### CheckServiceLinkedRole

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3F9E6A3B-C13E- 4064-A010- 18582A****** | 请求 ID。 |
| HasServiceLinke dRole | Boolean | true | 是否已创建服务关联角色。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CheckServiceLinkedRole
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"3F9E6A3B-C13E-4064-A010-18582A******",
 "HasServiceLinkedRole":true
}
```

### CreateServiceLinkedRole

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 3F9E6A3B-C13E- 4064-A010- 18582A****** | 请求 ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateServiceLinkedRole
```

&公共请求参数云原生数据库 I参考正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"3F9E6A3B-C13E-4064-A010-18582A******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | Unknown.Exception | Unknown.Exception | The Request Server Is Error Or The Response Can Not Be Null. |

### DescribeBackups

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| BackupId | String | Query | 否 | 11111111 | 备份ID。 |
| BackupStat us | String | Query | 否 | Success | 备份状态，取值范围如下： Success ：备份完成。 Failed ：备份失败。 |
| BackupMod e | String | Query | 否 | Automated | 备份模式，取值范围如下： Automated ：系统自动备份。 Manual ：手动备份。 |
| StartTime | String | Query | 是 | 2020-11-14T00:00Z | 查询开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2020-11-16T00:00Z | 查询结束时间，查询结束时间需晚于开始时间，格式为 YYYY-MM- DDThh:mmZ （UTC时间）。 |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

|  |  | YYYY-MM- |
|---|---|---|
|  | DDThh:mmZ |  |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| BackupReg ion | String | Query | 否 | cn-hangzhou | 跨地域备份的目的地域。 当前仅PolarDB MySQL 版支持该参数。 |
| PageSize | Intege r | Query | 否 | 30 | 每页记录数，取值范围如下： 30 。 50 。 100 。 默认值为30 。 |
| PageNumb er | Intege r | Query | 否 | 1 | 页码，取值范围为大于0但不超过Integer最大值的整数，默认值为1 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Items | Array |  |  |
| -BackupSetSize | String | 4639948800 | 备份文件大小，单位为Byte。 因为快照之间存在共享数据块，因此删除目标快照备份后释放的空间会远小于该备份文件的大小。更多详情，请参见备份功能FAQ。 |
| -ConsistentTime | String | 1605425407 | 一致性快照的时间点，格式为Unix时间戳，单位为秒。 |
| -BackupStatus | String | Success | 备份状态，取值范围如下： Success ：备份完成。 Failed ：备份失败。 |
| -BackupType | String | FullBackup | 备份类型，仅支持全量备份，取值固定为FullBackup 。 |
| - BackupStartTim e | String | 2020-11- 15T07:30:05Z | 本次备份开始时间（UTC时间）。 |
| -IsAvail | String | 0 | 备份集是否可用，取值范围如下： 0 ：不可用。 1 ：可用。 |
| - BackupEndTime | String | 2020-11- 15T07:30:20Z | 本次备份结束时间（UTC时间）。 |
| -BackupId | String | 61******* | 备份ID。 |

| olarDB MySQL集参考 | 群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -DBClusterId | String | pc-**************** | 集群ID。 |
| -BackupsLevel | String | Level-1 | 备份集级别，取值范围如下： Level-1 ：一级备份。 Level-2 ：二级备份。 |
| -BackupMode | String | Automated | 备份模式，取值范围如下： Automated ：系统自动备份。 Manual ：手动备份。 |
| -BackupMethod | String | Snapshot | 数据备份方法，仅支持快照备份，取值固定为Snapshot 。 |
| TotalRecordCou nt | String | 1 | 总记录数。 |
| PageRecordCou nt | String | 1 | 本页记录数。 |
| RequestId | String | 24A1990B-4F6E- 482B-B8CB- 75C612****** | 请求ID。 |
| PageNumber | String | 1 | 页码。 |

**示例**

请求示例

```
&DBClusterId=pc-**************** &StartTime=2020-11-14T00:00Z &EndTime=2020-11-16T00:00Z
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalRecordCount":"1",
 "PageRecordCount":"1",
 "RequestId":"24A1990B-4F6E-482B-B8CB-75C612******",
 "PageNumber":"1",
 "Items":{
  "BackupMethod":"Snapshot",
  "BackupsLevel":"Level-1",
  "BackupMode":"Automated",
  "DBClusterId":"pc-****************",
  "BackupId":"61*******",
  "IsAvail":"0",
  "BackupSetSize":"4639948800",
  "StoreStatus":"",
  "BackupEndTime":"2020-11-15T07:30:20Z",
  "ConsistentTime":"1605425407",
  "BackupStartTime":"2020-11-15T07:30:05Z",
  "BackupType":"FullBackup",
  "BackupStatus":"Success"
 }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidDBClusterId.M alformed | InvalidDBClusterId.Malformed | The specified parameter DBClusterId is not valid. |
| 400 | InvalidBackupStatus. Malformed | InvalidBackupStatus.Malformed | The specified parameter BackupStatus is not valid. |
| 400 | InvalidBackupMode. Malformed | InvalidBackupMode.Malformed | The specified parameter BackupMode is not valid. |
| 400 | InvalidStartTime.Malf ormed | InvalidStartTime.Malformed | The specified parameter StartTime is not valid. |
| 400 | InvalidEndTime.Malfo rmed | InvalidEndTime.Malformed | The specified parameter EndTime is not valid. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.107.**

### UpgradeDBClusterMinorVersion

调用UpgradeDBClusterMinorVersion接口更新PolarDB MySQL集群的内核小版本。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 您可以通过 DescribeDBClusters接口查看账号下所有集群的详细信息（如集群ID）。 |
| PlannedSta rtTime | String | Query | 否 | 2021-01-14T09:00:00Z | 开始执行定时（即在目标时间段内执行）内核版本升级任务的最早时间。格式为 YYYY- MM- DDThh:mm:ssZ （UTC）。 开始时间的取值范围为未来24小时内的任意时间点。例如当前时间为 2021-01- 14T09:00:00Z ， 此处允许填入的开始时间范围为 2021- 01- 14T09:00:00Z ~ 2021-01- 15T09:00:00Z 。 若该参数留空，默认立即执行内核版本升级任务。 |
| PlannedEn dTime | String | Query | 否 | 2021-01-14T09:30:00Z | 开始执行目标定时任务的最晚时间。格式为 YYYY-MM- DDThh:mm:ssZ （UTC）。 最晚时间需晚于开始时间的30分钟或以上。 若设置了 PlannedStartTi me 但未指定该参数，执行目标任务的最晚时间默认为开始时间+30分钟 。例如当设置 PlannedStartTi me 为 2021-01- 14T09:00:00Z 且该参数留空时，目标任务最晚将于 2021- 01- 14T09:30:00Z 开始执行。 |
| FromTimeS ervice | Boole an | Query | 否 | false | 调用该接口时无需使用该参数。 |

| YYYY- |  |
|---|---|

|  |  | MM- |
|---|---|---|
|  |  | DDThh:mm:ssZ |

|  |  |  |  | 2021-01- |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  | 14T09:00:00Z |  |  |  |  |  |  |  |
|  |  |  |  |  | 2021- |  |  |  |  |
|  |  | 01- |  |  |  |  |  |  |  |
|  |  | 14T09:00:00Z |  |  |  | ~ |  |  |  |
|  |  | 15T09:00:00Z |  |  |  |  |  |  |  |

|  | DDThh:mm:ssZ |
|---|---|

|  |  |  |  | PlannedStartTi |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
|  |  |  | me |  |  |  |  |  |
|  |  |  |  | PlannedStartTi |  |  |  |  |
|  |  |  | me |  |  |  |  |  |
|  |  |  |  |  | 为 | 2021-01- |  |  |
|  |  |  |  |  |  |  | 2021- |  |
|  |  |  | 01- |  |  |  |  |  |
|  |  |  | 14T09:30:00Z |  |  |  |  |  |

| 开始 |  |
|---|---|

|  | 时间+30分钟 |
|---|---|

云原生数据库 I参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 69FFDDF1-44C3- 4ECA-A99E- 445B493****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpgradeDBClusterMinorVersion &DBClusterId=pc-****************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"69FFDDF1-44C3-4ECA-A99E-445B493******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | TaskExists | TaskExists | Specified task have existed. |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.108.**

### ModifyDBClusterResourceGroup

调用ModifyDBClusterResourceGroup接口修改数据库群集资源组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceGr oupId | String | Query | 否 | rg-********** | 原资源组ID。 |
| DBClusterI d | String | Query | 是 | pc-************* | 集群ID。 |
| NewResour ceGroupId | String | Query | 是 | rg-********** | 变更后的资源组ID。 |

云原生数据库 I参考

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 70656639-1416- 479F-AF13- D08197****** | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyDBClusterResourceGroup &DBClusterId=pc-************* &NewResourceGroupId=rg-**********
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"70656639-1416-479F-AF13-D08197******"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |

**6.109.**

### DescribeUserEncryptionKeyList

调用DescribeUserEncryptionKeyList接口查看KMS密钥列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-************ | 集群ID。 您可以调用 DescribeDBClusters接口查看目标地域下所有的集群信息，包括集群ID。 |

云原生数据库 I参考

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | String | Query | 否 | cn-hangzhou | 地域ID。 您可以调用 DescribeRegions接口查看目标账号下的可用地域信息，包括地域ID。 |
| TDERegion | String | Query | 否 | cn-beijing | TDE密钥所在地域。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| KeyList | String | 0275bd3f-fdbb-4d8c- 846b-71b211****** | 密钥列表。 |
| RequestId | String | A7E6A8FD-C50B- 46B2-BA85- D8B8D3****** | 请求ID。 |
| DBClusterId | String | pc-************ | 集群ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeUserEncryptionKeyList &DBClusterId=pc-************
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"A7E6A8FD-C50B-46B2-BA85-D8B8D3******",
 "KeyList":"",
 "DBClusterId":"pc-************"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | ByokRoleArnNotFoun d | ByokRoleArnNotFound | The roleArn can't be null. |
| 401 | ByokNotAuthorizedT oRds | ByokNotAuthorizedToRds | This user is not Authorized Rds. |
| 403 | UnsupportedKmsSer vice.NotEnabled | UnsupportedKmsService.NotEnab led | KMS service is not enabled. |

| olarDB MySQ 参考 | L集群版开发指南·AP |  | 云原生数据库 |
|---|---|---|---|
| HttpCod e | 错误码 | 错误信息 | 描述 |
| 404 | InvalidDBInstance.No tFound | InvalidDBCluster.NotFound | The DBClusterId provided does not exist in our records. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

### DescribeDBProxyPerformance

调用DescribeDBProxyPerformance接口查询PolarDB代理层（PolarProxy）的性能数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBClusterI d | String | Query | 是 | pc-**************** | 集群ID。 |
| Key | String | Query | 是 | PolarProxy CpuUsage _ | 查询的性能指标，多个值间用英文逗号（,）分隔，详细参数请参见性能参数表。 |
| StartTime | String | Query | 是 | 2020-09-23T01:01Z | 查询开始时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |
| EndTime | String | Query | 是 | 2020-09-24T02:08Z | 查询结束时间。格式为 yyyy-MM- ddTHH:mmZ （UTC时间）。 |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

|  |  | yyyy-MM- |
|---|---|---|
|  | ddTHH:mmZ |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PerformanceKey s | Array |  | 集群性能数据列表。 |
| -Points | Array |  | 性能数据数组。 |
| --Value | String | 10 | 监控指标数据值。 |
| --Timestamp | Long | 1600822800000 | 监控指标的具体时间点，格式为时间戳，单位为毫秒。 |
| -MetricName | String | service connections _ _ ps | 具体的性能指标度量名称。 |

I参考

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Measurement | String | PolarProxy CpuUsag _ e | 性能指标。 |
| -DBNodeId | String | pi-************* | 数据库集群节点ID。 |
| DBVersion | String | 8.0 | 兼容数据库版本。 |
| EndTime | String | 2020-09- 23T01:01:00Z | 查询结束时间。格式： yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| RequestId | String | 35D3E3DA-4650- 407A-BFF5- 59BFF1****** | 请求ID。 |
| StartTime | String | 2020-09- 23T01:00:00Z | 查询开始时间。格式： yyyy-MM- ddTHH:mm:ssZ （UTC时间）。 |
| DBClusterId | String | pc-***************** | 数据库集群ID。 |
| DBType | String | MySQL | 兼容数据库类型。 |
| Engine | String | POLARDB | 数据库引擎。 |

|  | ddTHH:mm:ssZ |
|---|---|

|  | ddTHH:mm:ssZ |
|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeDBProxyPerformance &DBClusterId=pc-**************** &Key=PolarProxy_CpuUsage &StartTime=2020-09-23T01:01Z &EndTime=2020-09-24T02:08Z
```

&公共请求参数正常返回示例 `JSON` 格式云原生数据库 I参考

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "PerformanceKeys":{
  "Measurement":"PolarProxy_CpuUsage",
  "MetricName":"service_connections_ps",
  "-Points":{
   "Value":"10",
   "Timestamp":1600822800000
  },
  "DBNodeId":"pi-*************"
 },
 "DBVersion":"8.0",
 "EndTime":"2020-09-23T01:01:00Z",
 "RequestId":"35D3E3DA-4650-407A-BFF5-59BFF1******",
 "StartTime":"2020-09-23T01:00:00Z",
 "DBClusterId":"pc-*****************",
 "DBType":"MySQL",
 "Engine":"POLARDB"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameterCo mbination | InvalidParameterCombination | The end time must be greater than the start time. |
| 400 | InvalidStartTime.Malf ormed | InvalidStartTime.Malformed | The specified parameter StartTime is not valid. |
| 400 | InvalidEndTime.Malfo rmed | InvalidEndTime.Malformed | The specified parameter EndTime is not valid. |
| 400 | InvalidKey.Malforme d | InvalidKey.Malformed | The specified parameter Key is not valid. |
| 404 | InvalidDBClusterId.N otFound | InvalidDBClusterId.NotFound | The DBClusterId provided does not exist in our records. |

云原生数据库录

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM 角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证STS Token。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::1234567 89012****:role/ad minrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM角色。 |
| RoleSessionNam e | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该 API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、 半角句号（.）、at（@）、短划线（-）和下划线（ ）。 _ |

云原生数据库录

| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource" : ["*"]}],"Version":"1 "} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |
|---|---|---|---|---|

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuKg 5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | ****************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::123456789 012****:role/adminrol e/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495**** :alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下： 云原生数据库录

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

以下代码示例为通过调用 `Sts::AssumeRole::2015-04-01` 获取STS AccessKey三元组信息。

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```xml
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
```

`// "sts.aliyuns.com"`要替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`"<yourRoleSessionName>"`请替换为实际值

```
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`Ram Role ARN`

```
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
```

云原生数据库录

```java
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " +
stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        }
    }
}
```

**调用示例**

下列代码以调用ECS的 `DescribeZones` 接口为示例。 云原生数据库录

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
```

`// "<yourRegionID>"`替换为真实的`RegionID` `// "<yourStsAccesskey>", "<yourStsAccessKeySecret>"`替换为上面获取到的`STS`三元组中`stsAk`、`stsS` k

```xml
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccessKey>", "<yourStsAccessKeySecret>");
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

`//"<yourRegionID>"`替换为真实的`RegionId`

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"`替换为上面获取到的`STS`三元组中`stsToken`

```
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,资源集`id`

```
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,组织`id`

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
}
```

**错误码**

云原生数据库录

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleAr n | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.RoleSe ssionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号（.）、at（@）、短划线（-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Duratio nSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为 900秒，最大值为MaxSessionDuration 设置的时间。 |
| 400 | InvalidParameter.PolicyG rammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.PolicyS ize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
