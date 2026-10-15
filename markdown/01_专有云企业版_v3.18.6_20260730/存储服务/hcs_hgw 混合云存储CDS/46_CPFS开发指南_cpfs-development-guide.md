---
title: "混合云存储CDS CPFS开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 38
source_pdf: "46_CPFS开发指南_cpfs-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/hcs_hgw/zh/cpfs-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 混合云存储CDS CPFS开发指南

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

**流程图**

| 获取API信息获取AccessKey 获取公共Header参数 |  |
|---|---|
| 获取Endpoint信息获取SDK包调用API |  |

## 准备工作

正式调用

**调用步骤**

1. 从API参考文档中获取API信息。
2. 获取AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
3. 获取公共Header参数。
RegionID：地域ID。 组织ID：需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的Get OrganizationList章节。 资源集ID：需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的Li stResourceGroup章节。

|  | 说明调用API时，请在Header参数中增加组织ID <x-acs-organizationid> 和资源集ID <x-acs- resourcegroupid>， 指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID <x-acs-organizationid> ，则默认获取当前用户所属的组织。 不指定资源集ID <x-acs-resourcegroupid> ，则默认为空，如果指定资源集需要同时指定组织ID。 |
|---|---|

4. 获取Endpoint信息。
5. 获取阿里云官网的SDK核心库。
使用CPFS功能，直接安装阿里云官网的SDK核心库即可。
6. 通过POP SDK调用API。使用POP SDK调用API时，请设置产品名称为CPFS，API版本为2017-06-26。

## 准备工作

### 获取AccessKey

AccessKey支持RAM授权模式。本文将为您描述如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，以验证某个请求发送者的身份。其中 AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串，通过RAM授权给第三方请求者。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方式，请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方式，请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。 |
| x-acs-instanceid | 进行操作的实例ID，例如，CPFS的实例ID可以从 CPFS 文件系统列表中查询到。 |

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
3. 在左侧导航栏中，选择。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

### 获取Endpoint信息

本文介绍如何获取CPFS的Endpoint信息。
1. 登录Apsara Uni-manager运维控制台。
2. 在顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在**服务注册变量大盘**页面，选择**服务**并输入**nas-yaochi**。
4. 单击**Service Registration**列
图标，单击显示的信息。
5. 在**注册变量**对话框，查看**nas.openapi.endpoint**的值即为CPFS文件系统的Endpoint。

### 获取公共Header参数

调用专有云API时需要填写多个公共请求Header参数，在返回结果中也会包含公共返回参数。

**公共请求参数**

在专有云API调用的代码中需要指定这些公共请求参数的参数值。

| request.putHeadParameter("x-acs-resourcegroupid", " |  |  |  |
|---|---|---|---|
|  | ，需要将 | <yourResourceGroupID> | 替换为您获取到的实际的资源集ID。 |

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 实际操作的实例资源所属的地域ID，获取方式请参见获取Region ID。 |
| x-acs-organizationid | 实际操作的实例资源所属的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | 实际操作的实例资源所属的资源集ID，获取方式请参见获取资源集ID。 |

| x-acs-instanceid | 实际操作的文件系统资源的ID，获取方式请参见获取实例ID。 |
|---|---|

| 说明调用Apsara Uni-manager运营控制台的API时，可以不使用Header参数 x-acs- organizationid 、 x-acs-resourcegroupid 、 x-acs-instanceid 。 调用其他云产品的API时，需要在Header参数中增加组织ID <x-acs-organizationid> ，否则将返回调用异常，提示无权限。 调用其他云产品的API时，建议在Header参数中增加资源集ID <x-acs-resourcegroupid> 。 指定资源所属的组织和资源集，实现实例资源的隔离查询。若不指定资源集ID <x-acs- resourcegroupid> ，则获取当前用户所属组织的默认资源集。 |  |
|---|---|

| x-acs- |  |
|---|---|

**获取Region ID**

您可以在Apsara Uni-manager运营控制台中查看资源所属的RegionID。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看**Region****名称**，即为Region ID。

**获取组织ID**

组织ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取组织ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。

**获取文件系统ID**

文件系统ID可以通过Apsara Uni-manager运营控制台中的云产品资源列表进行获取。请在文件存储 CPFS 产品控制台的文件系统列表中查看文件系统ID信息。
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏，选择**产品** > **存储** > **文件存储** **CPFS**
3. 在左侧导航栏中，单击**CPFS****列表**。
4. 在列表中可查看并复制实例ID。

**公共返回参数**

在调用列表类的云产品资源实例接口时，在返回结果中默认包含以下公共返回参数。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

### 通过POP网关调用专有云API

通过POP Java SDK访问产品域名，需要了解该产品调用方式（RPC或ROA）。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，您可以从SDK中心下载V1.0版本的SDK。

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（CPFS）、接口（DescribeFileSystems）、版本（2017-06-26）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//`设置当前产品的`Endpoint`，可变参数请替换为您的实际值。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

请替换为实际代理`IP+`端口。 `*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 替换为真实的产品域名。

```
        request.setDomain("<Endpoint>");
        request.setSysProduct("CPFS");
        request.setVersion("2017-06-26");
        request.setAction("DescribeFileSystems");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非
```

必填，请替换为您实际的资源集`ID`。

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填
```

，请替换为您实际的组织`ID`。

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来
```

源说明。

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填（企业版V3.1
```

`5.0`及之前历史版本必填）,请替换为您实际的地域`ID`。

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修
```

改、删除、查询单实例详情时必填）,请替换为您实际的实例`ID`。

```
        /**
```

当使用`STS AccessKey`调用接口时需要在参数中加上`SecurityToken`字段。 调用方法如下：

```
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
```

请替换为实际的`Token` `*/`

```java
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

用示例

## Java SDK调用示例

本文介绍如何获取Java SDK并开始调用。

### 快速开始

本文介绍如何获取Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体根据所用功能获取相应产品的Endpoint。具体操作，请参见获取Endpoint信息。 阿里云专有云Java SDK需要1.8及以上的JDK。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用产品的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Java SDK

本文介绍如何安装及调用Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。要使用CPFS功能，安装阿里云Java SDK核心库即可，SDK核心库推荐使用4.5.17及以上版本。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Java SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 用示例使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请您根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请您根据自身服务的能力，配置连接超时时间，单位为毫秒 （ms）。 <maxRequestsPerHost>，请您根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请您根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 用示例 `//` 获取`HttpClientConfig`对象

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置是否忽略证书

```
clientConfig.setIgnoreSSLCerts(true);
```

`// (`可选)设置读取超时时间，单位毫秒（`ms`）

```
clientConfig.setReadTimeoutMillis(<readTimeout>);
```

`// (`可选)设置创建连接超时时间，单位毫秒（`ms`）

```
clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);
```

`// (`可选)设置每个主机的最大请求数，数据类型为`INT`

```
clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);
```

`// (`可选)设置最大请求数，数据类型为`INT`

```
clientConfig.setMaxRequests(<maxRequests>);
```

`// (`可选)设置协议类型

```
clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下：

```
clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

请替换为您实际的代理`IP+`端口 `*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 使用CommonRequest进行调用

当您要调用某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。更多信息，可参考泛化调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。 域名（domain）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。

| 如 | CreateFileSystem | 接口，在发起 | CommonRequest |  |
|---|---|---|---|---|
| request.setSysAction("CreateFileSystem") |  |  |  |  |
|  |  |  |  | 来指定 |

**示例：调用RPC风格的API**

使用CPFS的DescribeFileSystems接口获取文件系统信息的示例代码如下： 用示例

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <Endpoint>，请替换为您当前产品实际的Endpoint。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP和端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
```

`/**` 设置代理(可选`),`替换为代理`IP+Port`

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

或

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

请替换为实际代理`IP+`端口。 `*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 替换为真实的产品域名。

```
        request.setDomain("<Endpoint>");
        request.setSysProduct("CPFS");
        request.setVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
```

t `tQ` P t

```
("FilS
```

t T " `"b`

```
f")
```

用示例

```
        request.putQueryParameter("FileSystemType", "bmcpfs");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// 非
```

必填，请替换为您实际的资源集`ID`。

```
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// 必填
```

，请替换为您实际的组织`ID`。

```
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// 必填，调用来
```

源说明。

```
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// 非必填（企业版V3.1
```

`5.0`及之前历史版本必填）,请替换为您实际的地域`ID`。

```
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修
```

改、删除、查询单实例详情时必填）,请替换为您实际的实例`ID`。

```java
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

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 用示例

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

## Python SDK调用示例

### 快速开始

本文介绍如何获取SDK并开始调用。

**环境准备**

使用阿里云专有云Python SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。 根据所用功能获取相应产品的Endpoint。具体操作，请参见获取Endpoint信息。 要使用CPFS功能，您必须安装阿里云Python SDK核心库。 具体安装步骤如下： 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

**使用Python SDK**

调用Python SDK的3个主要步骤如下：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Python SDK

本文介绍如何安装及调用Python SDK。

**背景信息**

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。

**说明**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。 要使用CPFS功能，您必须安装阿里云Java SDK核心库。 具体安装步骤如下： 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Python SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```python
from aliyunsdkcore import client clt = client.AcsClient(access_key, acces_secret, region_id)
```

#### 使用CommonRequest进行调用

当您要调用的CPFS的某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。详细信息可参考泛化调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名（domain）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.set_action_name('Action')` 的方式来指定API名称。

| 如 | DescribeFileSystems | 接口，在发起 | CommonRequest |  |
|---|---|---|---|---|
| request.set action name('DescribeFileSystems') _ _ |  |  |  |  |
|  |  |  |  | 来 |

**示例：调用RPC风格的API**

使用文件系统的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <Endpoint>，请替换为您当前产品实际的Endpoint。

```bash
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`。

```
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CPFS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26')
```

`request.set_domain('<Endpoint>') #`产品访问域名，当前为示例值，请替换为您实际的产品访问地址。

```bash
# or:
# request = = CommonRequest(product='CPFS',
action_name='DescribeFileSystems',version='2017-06-26',domain='<Endpoint>')
######
```

# 设置请求协议类型，支持`https`或`http`，默认为`http`。
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('FileSystemType', 'bmcpfs') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段。
# 调用方法如下：

```bash
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
```

# 请替换为您实际的`SecurityToken`。

```
######
```

# 非必填，请替换为您实际的资源集`ID`。

```
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
```

# 必填，请替换为您实际的组织`ID`。

```
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
```

# 必填，调用来源说明。

```
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
```

# 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`。

```
request.add_header("x-acs-regionid", "<yourRegionID>")
```

# 非必填（修改、删除、查询单实例详情时必填），请替换为您实际的实例`ID`。

```python
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
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

用示例

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问云产品。本操作介绍如何获取阿里云Go SDK并开始调用。

**环境准备**

使用Go SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作，请参根据所用功能获取相应产品的Endpoint。具体操作，请参见获取Endpoint信息。

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及更高版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

使用Go SDK的主要步骤如下：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

### 使用手册

#### 安装Go SDK核心包

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何目前，Go SDK支持通过AccessKey进行身份验证，具体获取AccessKey的方法，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 用示例

**初始化Client实例**

```
   client, err := sdk.NewClientWithAccessKey(
```

`"<yourRegionID>", //`请替换为您实际的地域`ID`， `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID`， `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`，

#### 使用CommonRequest进行调用

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在API文档中获取以下参数的值。 域名（domain）：该产品的服务地址。 API版本（version）：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.ApiName("<Action>")` 的方式来指定API名称。

| DescribeFileSystem |  |
|---|---|
|  | 来 |

**示例：调用RPC风格的API**

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <Endpoint>，请替换为您当前产品实际的Endpoint。 用示例

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

`"<yourRegionID>", //`请替换为您实际的地域`ID`， `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID`， `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`，

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<endpoint>" //` 请求访问地址，当前为示例值，请根据实际请求地址替换，

```
    request.Product = "CPFS"
    request.Version = "2017-06-26"
```

`//` 因为是`RPC`接口，因此需指定`APIName(Action)`， `//` 业务参数

```
    request.QueryParams["FileSystemType"] = "bmcpfs"
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*` 当使用`STS AccessKey`调用`RPC`接口时，需要在参数中加上`SecurityToken`字段。 调用方式如下：

```
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
```

请替换为您实际的`SecurityToken`。 `*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // 必填，调用来源说明。
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //` 非必填（企业版`V3.15.0`及之前历史版本必填），请替换为您实际的地域`ID`。

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填，请替换为
```

您实际的资源集`ID`。

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // 必填，请替换为您实
```

际的组织`ID`。 `// request.Headers["x-acs-instanceid"] = "<yourInstanceID>" //` 非必填（修改、删除、查看单实例详情时必填），请替换为您实际的实例`ID`

```
。 response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。 用示例

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response, err := client.ProcessCommonRequest(request) if err != nil {
    panic(err)
}
```

## API参考

### 调用API

#### 概述

API接口调用是向产品的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数。调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集编码。

#### 请求结构

**服务地址**

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如CreateFileSystem），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

#### API授权

为了确保您的账号安全，建议您使用RAM用户的身份凭证调用API。如果使用RAM用户调用CPFS 文件存储的API，则您需要为该RAM用户创建并附加相应的授权策略。 在RAM中，可以对一个CPFS资源进行以下Action的授权。

| 分类 | Action名称列表 |
|---|---|
| 文件系统 | CreateFileSystem DeleteFileSystem DescribeFileSystems ModifyFileSystem |

#### 返回结果

调用API服务后返回数据采用统一格式，返回的HTTP状态码为2xx，代表调用成功；返回4xx或5xx的HTTP 状态码代表调用失败。

### RAM鉴权

当RAM用户通过OpenAPI对阿里云账号的资源进行访问时，系统会向RAM进行权限检查，以确保资源拥有者的确将相关资源的相关权限授予了调用者。

**背景信息**

默认情况下，阿里云账号或者RAM用户均能使用CPFS控制台或CPFS API操作自己创建的资源。在以下场景中，会涉及到操作授权问题： RAM用户刚创建时没有权限操作阿里云账号的资源时。 从其他阿里云服务访问CPFS资源，或者CPFS访问其他阿里云服务时。 操作具有权限控制的CPFS资源前，需要资源拥有者授权目标资源和目标API行为权限。 当其他账号通过CPFS API访问阿里云账号资源时，阿里云CPFS首先向RAM发起权限检查，以确保资源拥有者已经将相关权限授予调用者。不同的CPFS API会根据涉及的资源以及API语义确定需要检查哪些资源的权限。

**规则详情**

每个不同的CPFS API，会根据涉及到的资源以及API的语义，确定需要检查的资源的权限。

### 公共参数

公共参数分为公共请求参数、公共Header参数和公共返回参数。

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。 表 1. 公共请求参数表

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回值的类型，仅支持JSON。 |
| Version | String | 是 | API版本号，以日期形式YYYY-MM-DD输入。取值为2017-06-26。 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| AccessKeySecre t | String | 是 | 访问服务使用的密钥值。 |
| RegionId | String | 是 | 访问服务所使用的地域ID。 |
| Product | String | 是 | 接口对应的产品名称，产品名称取值为CPFS。 |

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID。具体获取方式，请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID。具体获取方式，请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID。具体获取方式，请参见获取实例ID。 |

**说明**

在调用各云产品接口时，您需要在调用代码的请求头Header中添加**x-acs-instanceid**、**x-acs-**
**organizationid**、**x-acs-resourcegroupid**等参数的实际值，用于指定当前实例的实例ID（在创
建实例和查询实例列表的场景下，实例ID不存在），及其所属的组织和资源集。若未添加相关Header 参数实际值，调用时则会默认指向root组织和root资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态： 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码 RequestId。

**获取Region ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **地域管理**。
4. 单击目标组织名称。
5. 在右侧**Region****列表**中查看Region ID。

**获取组织ID**

组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。

**获取资源集ID**

资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**获取实例ID**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**产品** > **存储** > **文件存储** **CPFS**。
3. 在左侧导航栏中，单击**CPFS****列表**。
4. 在列表中可查看并复制实例ID。

### 文件系统

#### CreateFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateFileSystem | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值：CreateFileSystem。 |
| RegionId | String | 是 | cn-qingdao-exxx- d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 是 | cn-qingdao-exxx- axxx-a | 可用区ID。必填参数。 |
| FileSystemType | String | 是 | bmcpfs | 文件系统类型, 目前仅支持bmcpfs。 |
| Capacity | Long | 是 | 20480 | 容量(GiB)，20480以上10240的倍数，performance规格下可填入最大容量 10240000。 |
| StorageType | String | 是 | bm advance 300 _ _ _ private | 文件系统规格，对应fscd的 fsSpec，bmcpfs场景目前仅支持 bm advance 300 private（性能型）。 _ _ _ |
| ZoneId | String | 是 | cn-wulan-exxx- axxx-a | ZoneId。 |
| ClusterId | String | 是 | a20231214-02cc | 天基集群ID，调用DescribeZones接口即可获取。 |
| ProtocolType | String | 是 | CPFS | 文件传输协议类型，bmcpfs场景目前仅支持CPFS。 |
| EncryptType | String | 是 | 0 | 0表示不加密，1表示加密，专有云场景不支持加密。 |

| Description | String | 否 | - | 描述信息, 传入字符串信息, 要求: 1. 长度为2~128个英文或中文字符。 2. 必须以大小写字母或中文开头，不能以 http:// 和 https:// 开头。 3. 可以包含数字、半角冒号（:）、下划线 （ ）或者连字符（-）。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```

#### DeleteFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteFileSyste m | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值：DeleteFileSystem。 |
| RegionId | String | 是 | cn-qingdao- exxx-d01 | 所属的地域ID。您可以调用 DescribeRegions查看最新的阿里云地域列表。 |
| ZoneId | String | 否 | cn-qingdao- exxx-axxx-a | 可用区ID。必填参数。 |
| FileSystemId | String | 是 | bmcpfs- 0156ec1d | 文件系统id |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```

#### DescribeFileSystems

本文介绍如何调用DescribeFileSystems接口查询已创建的CPFS文件系统。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFileSyst ems | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值：DescribeFileSystems。 |
| RegionId | String | 是 | cn-qingdao- exxx-d01 | 所属的地域ID。您可以调用 DescribeRegions接口查看地域列表。 |
| ZoneId | String | 否 | cn-qingdao- exxx-axxx-a | 可用区ID。 |
| FileSystemId | String | 否 | bmcpfs- 0156ec1d | 文件系统id。 |
| Description | String | 否 | - | 描述。 |
| FileSystemType | String | 是 | bmcpfs | 文件系统类型。 |
| PageSize | Integer | 否 | 10(默认值) | 每页的数据量。 |
| PageNumber | Integer | 否 | 1(默认值) | 页数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileSystemId | String | bmcpfs-0156ec1d | 文件系统id。 |
| Status | String | Running | 文件系统状态，所有状态如下： Pending 初始化中 Running 运行中 Deleting 删除中 Extending 扩容中 Shrinking 缩容中 Starting 启动中 Stopping 停止中 Stopped 已停止 |
| MeteredSize | Integer | 1000 | 已使用容量，单位GiB。 |
| Capacity | Integer | 1000 | 总容量，单位GiB。 |
| MountTarget | String | - | 挂载点信息。 |
| MountTargetDomain | String | - | 挂载点名称。 |

**示例**

正常返回示例

```json
{
    "FileSystems": {
        "FileSystem": [
            {
                "Status": "Running",
                "Description": "cpfs",
                "StorageType": "performance",
                "MountTargetCountLimit": 100,
                "ZoneId": "cn-wulan-exxx-axxx-a",
                "NasNamespaceId": "",
                "CreateTime": "2024-03-26T19:22:47CST",
                "MeteredIASize": 0,
                "SupportedFeatures": {
                    "SupportedFeature": [
```

]

```json
                },
                "MountTargets": {
                    "MountTarget": [
```

]

```json
                },
                "MeteredSize": 0,
                "QuotaSize": 40960,
                "EncryptType": 0,
                "ProtocolType": "CPFS",
                "Packages": {
                    "Package": [
```

]

```json
                },
                "FileSystemType": "bmcpfs",
                "FileSystemId": "bmcpfs-0156ec1d",
                "RegionId": "cn-wulan-***-d01",
                "VolumeSize": 40960
            }
```

]

```json
    },
    "TotalCount": 1,
    "RequestId": "4306B744-C87D-45C7-8083-64C4E153F46C",
    "PageSize": 10,
    "PageNumber": 1
}
```

#### ModifyFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | ModifyFileSyste m | 系统规定参数，对于您自行拼凑 HTTP/HTTPS URL发起的API请求， Action 为必选参数。取值：ModifyFileSystem。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-qingdao- exxx-d01 | 所属的地域ID。您可以调用 DescribeRegions查看地域列表。 |
| ZoneId | String | 否 | cn-qingdao- exxx-axxx-a | 可用区ID。 |
| FileSystemId | String | 是 | bmcpfs- 0156ec1d | 文件系统id。 |
| Description | String | 否 | - | 文件系统的描述信息。 |
| Capacity | Long | 否 | 20480 | 文件系统的容量，取值为20480以上且为 10240的倍数，目前仅支持扩容。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

正常返回示例

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```
