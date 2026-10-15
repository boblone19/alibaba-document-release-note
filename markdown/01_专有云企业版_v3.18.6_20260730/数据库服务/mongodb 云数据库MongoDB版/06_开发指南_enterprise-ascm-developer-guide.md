---
title: "云数据库MongoDB版 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 205
source_pdf: "06_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/mongodb/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 云数据库MongoDB版 开发指南

云数据库 MongoDB 版

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
云数据库 MongoDB 版
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

为了使您拥有与公有云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文

**流程图**

云数据库 MongoDB 版

**调用步骤**

1. 获取AccessKey。

**说明**

推荐使用个人AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
云数据库 MongoDB 版您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云数据库MongoDB的Endpoint。
6. 获取云数据库MongoDB的SDK并调用云数据库MongoDB的API。
云数据库 MongoDB 版

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

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标示用户，AccessKey Secret是用户用于加密签名的字符串。 云数据库 MongoDB 版 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织 AccessKey相对权限较大，需要管理员确认操作的安全性。

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
AccessKey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
云数据库 MongoDB 版
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
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，
调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节GetOrganizationList。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 单击顶部菜单栏**产品**，选择**应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源
集ID。接口信息详见Apsara Uni-manager运营控制台开发指南中的章节ListResourceGroup。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，本文中以云数据库 MongoDB为例，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**数据库**>**云数据库****MongoDB**。
3. 根据目标实例的类型，在左侧导航栏中，单击**副本集实例列表**或**分片集群实例列表**。
云数据库 MongoDB 版
4. 在实例列表中查看**实例****ID/****名称**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

云数据库 MongoDB 版

## Java SDK调用示例

### 快速开始

本节介绍如何获取云数据库MongoDB Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。参见获取AccessKey在Apsara Uni-manager运营控制台上获取和查看您的AccessKey。 获取云数据库MongoDB的Endpoint。具体操作，请参见获取API信息及其EndPoint。 阿里云专有云Java SDK需要1.8及以上版本的JDK。

**安装阿里云专有云 Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 要使用云数据库MongoDB的开发工具包，必须安装SDK核心库以及产品的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，SDK的版本为3.6.3。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。 云数据库 MongoDB 版

```java
import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.google.gson.Gson; import java.util.*; import com.aliyuncs.dds.model.v20151201.*;
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourAccessKeyID>", "<yourAccessKeySecret>");
        IAcsClient client = new DefaultAcsClient(profile);
        DescribeAccountsRequest request = new DescribeAccountsRequest();
        request.setDBInstanceId("<yourDBInstanceId>");
        try {
            DescribeAccountsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
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

### 使用手册

#### 安装Java SDK

本文介绍如何安装及调用云数据库MongoDB Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载SDK包的方式安装专有云Java SDK。 要使用云数据库MongoDB的开发工具包，必须安装阿里云Java SDK核心库以及云数据库MongoDB的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为3.6.3。 以使用云数据库MongoDB的Java SDK为例，您需要安装阿里云Java SDK核心库和MongoDB Java SDK，并在pom.xml文件中添加以下依赖即可。更多关于SDK的内容，请参见SDK中心。 云数据库 MongoDB 版

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- dds java sdk --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-dds</artifactId>
    <version>3.6.3</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您可以通过AccessKey进行身份验证。 目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭证时，需要在初始化Client时设置凭证。

**说明**

请确保包含AccessKey的代码不会泄漏（例如提交到公开的GitHub项目），否则将会危害您的信息安全。

```xml
DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", " <yourAccessKeyID>", "<yourAccessKeySecret>")
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 云数据库 MongoDB 版

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请您根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请您根据自身服务的能力，配置连接超时时间，单位为毫秒 （ms）。 <maxRequestsPerHost>，请您根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请您根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。 `//` 获取`HttpClientConfig`对象

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

#### 发起调用

本文介绍如何使用云数据库MongoDB Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 云数据库 MongoDB 版

```
DescribeAccountsRequest request = new DescribeAccountsRequest();
      request.setDBInstanceId("dds-********");
      request.setAccountName("root");
```

3. 发起调用并处理应答。

```
DescribeAccountsResponse response = client.getAcsResponse(request);
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
AccountData := response.getData()
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息，包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

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

云数据库 MongoDB 版

## Python SDK调用示例

### 快速开始

本节介绍如何获取云数据库MongoDB Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体请参获取云数据库MongoDB的Endpoint，具体操作参见获取API信息及其EndPoint。
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
以下以安装云数据库MongoDB的SDK为例： 如果您使用的是Python 2.x，执行以下命令，安装云数据库MongoDB的SDK：

```
pip install aliyun-python-sdk-dds
```

如果您使用的是Python 3.x，执行以下命令，安装云数据库MongoDB的SDK：

```
pip3 install aliyun-python-sdk-dds
```

**使用Python SDK**

以下示例以云数据库MongoDB为例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。 云数据库 MongoDB 版

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>") response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

### 使用手册

#### 安装Python SDK

本文介绍如何安装阿里云Python SDK核心库和云数据库MongoDB Python SDK。

**背景信息**

使用产品的开发工具包，都必须安装阿里云Python SDK核心库。云数据库MongoDB的Python SDK，您需要安装阿里云Python SDK核心库和云数据库MongoDB的Python SDK。

**安装阿里云Python SDK核心库**

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库：

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库：

```
pip3 install aliyun-python-sdk-core-v3
```

**安装云数据库MongoDB Python SDK**

如果您使用的是Python 2.x，执行以下命令，安装云数据库MongoDB的SDK：

```
pip install aliyun-python-sdk-dds
```

如果您使用的是Python 3.x，执行以下命令，安装云数据库MongoDB的SDK： 云数据库 MongoDB 版

```
pip3 install aliyun-python-sdk-dds
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您可以通过AccessKey进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的方法请参见获取AccessKey。 使用AccessKey作为访问凭证时，需要在初始化Client时设置凭证。 请确保包含AccessKey的代码不会泄漏（例如提交到公开的GitHub项目），否则将会危害

**重要**

您的信息安全。

```
clt = client.AcsClient(<yourRegionID>, <yourAccessKeyID>, <yourAccessKeySecret>)
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。 产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**说明**

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No module named ssl` 的错误信息，说明已经支持OpenSSL。 若没有OpenSSL，运行以下命令安装：

```
pip install pyopenssl
```

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用：

```
request = DescribeInstancesRequest() request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议： 云数据库 MongoDB 版

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 发起调用

本文以DescribeAccounts接口为例，介绍使用云数据库MongoDB Python SDK发起请求的方法。

**操作步骤**

1. 导入云数据库MongoDB的SDK。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.acs_exception.exceptions import ClientException from aliyunsdkcore.acs_exception.exceptions import ServerException from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential from aliyunsdkdds.request.v20151201.DescribeAccountsRequest import
```

2. 新建一个AcsClient。
涉及替换的参数如下：

**说明**

<yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。

```
credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials)
```

3. 创建Request对象。
<yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。

**说明**

```
request.set_accept_format('json') request.set_DBInstanceId("<yourDBInstanceId>")
```

4. 发起调用并处理返回。

```python
response = client.do_action_with_exception(request)
# python2:  print response
print(str(response, encoding='utf-8'))
```

#### 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 云数据库 MongoDB 版 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

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

云数据库 MongoDB 版

## Go SDK调用示例

### 快速开始

本文介绍如何获取云数据库MongoDB Go SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。获取方法请参

**安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**使用Go SDK**

以下这个代码示例展示了调用阿里云Go SDK的3个主要步骤：
1. 初始化Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。 云数据库 MongoDB 版

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

)

```
func main() {
    client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>",
"<yourAccessKeySecret>")
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
    response, err := client.DescribeAccounts(request)
    if err != nil {
        fmt.Print(err.Error())
    }
    fmt.Printf("response is %#v\n", response)
}
```

4. （可选）切换HTTP或HTTPS协议。

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

当使用阿里云专有云SDK访问阿里云专有云服务时，您可以通过AccessKey进行身份验证。 目前Go SDK支持通过AccessKey进行身份验证，获取方法请参见获取AccessKey。 使用AccessKey作为访问凭证时，需要在初始化Client时设置凭证。 请确保包含AccessKey的代码不会泄漏（例如提交到公开的GitHub项目），否则将会危害

**重要**

您的阿里云账号的信息安全。

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

云数据库 MongoDB 版以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。

#### 发起调用

本文介绍如何使用云数据库MongoDB Go SDK发起调用。 使用云数据库MongoDB Go SDK发起调用。
1. 导入云数据库MongoDB SDK。

```java
package main import (
    "fmt"
      dds "github.com/aliyun/alibaba-cloud-sdk-go/services/dds"
```

)
2. 新建一个产品名Client，该Client中包含产品名的所有API。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。

```
client, err := dds.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<yo urAccessKeySecret>")
```

| xxx.CreateXXXRequest |  | 方法创建一个请求。 |
|---|---|---|
| 法的命名规范为 |  |  |

**${service}**为产品名称（小写），例如dds（代表云数据库MongoDB产品）。
<yourDBInstanceId>，请替换为您实际的云数据库MongoDB实例ID。

**说明**

```
    request.Scheme = "https"
    request.DBInstanceId = "<yourDBInstanceId>"
```

4. 发起调用。

```
response, err := client.DescribeAccounts(request)
```

云数据库 MongoDB 版

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response, err := client.DescribeAccounts(request) if err != nil {
    fmt.Print(err.Error())
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个 `ClientError` 。 通过以下代码来判断并获取 `ClientError` 中的错误信息：

| 重要使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参考： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" //dds表示云数据库MongoDB "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // 新增的错误包 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

```
response, err := Client.DescribeAccounts(request) if clientError, ok := err.(*errors.ClientError); ok{
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

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。 您可以通过以下代码来判断并获取ServerError以及Response中的错误信息： 云数据库 MongoDB 版

| github.com/aliyun/alibaba-cloud-sdk- |  |
|---|---|

**重要**

`go/sdk/errors` ，引入方法请参考：

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/dds" //dds表示云数据库MongoDB
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := Client.DescribeAccounts(request) if serverError, ok := err.(*errors.ServerError); ok{
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

云数据库 MongoDB 版

## 通过POP网关调用专有云API

### 调用前置

阿里云专有云与公共云一样，可通过POP网关的方式进行API调用。本文为您介绍调用前需要进行的准备工作。

**背景信息**

为了使专有云保持与公共云相同的使用方式，使您拥有更方便，更一致的体验，建议通过POP网关调用专有云API。

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
云数据库 MongoDB 版
2. 顶部菜单栏选择**平台运维** > **飞天基础运维平台** > **运维工具**。
3. 在左侧导航栏，选择**运维工具** > **服务注册变量大盘**。
4. 在服务注册变量大盘页面，单击**高级筛选**。
5. 在Service Registration文本框中输入 `apigateway` ，单击**搜索**。
6. 在 `apigateway` 服务的**Service Registration**列中，单击
图标。
7. 单击 `apigateway` 服务**Service Registration**列的文本信息，在弹出的**注册变量**对话框中，查看
apigateway.openapi.endpoint值，即 `Endpoint` 。

**获取公共参数**

通过POP网关调用专有云API过程中所使用的参数，如组织ID、资源集ID、RegionID和实例ID，获取方式请

### Java版

通过POP Java SDK访问产品域名，需要了解该产品调用方式(RPC或ROA)。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

RPC调用，示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

云数据库 MongoDB 版 `//` 创建`DefaultAcsClient`实例并初始化。

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
```

云数据库 MongoDB 版

```java
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

`//`必填值，调用来源说明云数据库 MongoDB 版 `//` 必填值，调用来源说明

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

### Go版

本文为您介绍POP Go SDK调用的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。
云数据库 MongoDB 版

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

RPC方式调用示例接口信息：产品（apigateway）、接口（DescribeApiGroups）、版本（2016-07- 14）。 示例代码如下： 云数据库 MongoDB 版

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

ROA调用示例接口信息：产品（CR）接口（GetNamespaceList）版本（2016-06-07）。 调用示例如下： 云数据库 MongoDB 版

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

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 云数据库 MongoDB 版

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

云数据库 MongoDB 版

### Python版

本文为您介绍POP Python SDK调用云产品API的方式。

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

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

云数据库 MongoDB 版
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

云数据库 MongoDB 版

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

) 云数据库 MongoDB 版

## API概览

云数据库 MongoDB 版提供以下相关API接口。

| API | 描述 |
|---|---|
| CreateDBInstance | 调用CreateDBInstance接口创建云数据库MongoDB副本集实例，同时也可用于克隆云数据库MongoDB副本集实例。 |
| ModifyDBInstanceSpec | 调用ModifyDBInstanceSpec接口变更云数据库MongoDB单节点或副本集实例的规格或存储空间。 |
| DeleteDBInstance | 调用DeleteDBInstance接口释放云数据库MongoDB实例。 |
| CreateShardingDBInstance | 调用CreateShardingDBInstance接口创建云数据库MongoDB分片集群实例，同时也可用于克隆云数据库MongoDB分片集群实例。 |
| CreateNode | 调用CreateNode接口为云数据库MongoDB分片集群实例添加Shard节点或 Mongos节点。 |
| DeleteNode | 调用DeleteNode接口删除云数据库MongoDB分片集群实例中的Shard节点或Mongos节点。 |
| ModifyNodeSpec | 调用ModifyNodeSpec接口变更云数据库MongoDB分片集群实例中节点的规格和存储空间。 |

### 区域管理

| API | 描述 |
|---|---|
| MigrateToOtherZone | 调用MigrateToOtherZone接口迁移云数据库MongoDB实例到其他可用区。 |
| DescribeRegions | 调用DescribeRegions接口查看云数据库MongoDB实例可用的地域和可用区。 |
| MigrateAvailableZone | 调用MigrateAvailableZone接口迁移云数据库MongoDB实例的可用区。 |

### 资源管理

| API | 描述 |
|---|---|
| DescribeAvailableResource | 调用DescribeAvailableResource查询指定可用区内可创建的云数据库 MongoDB实例。 |

### 连接管理

| API | 描述 |
|---|---|
| AllocatePublicNetworkAddress | 调用AllocatePublicNetworkAddress接口为云数据库MongoDB实例申请公网连接地址。 |
| ReleasePublicNetworkAddress | 调用ReleasePublicNetworkAddress接口释放云数据库MongoDB实例的公网连接地址。 |

云数据库 MongoDB 版

| ModifyInstanceVpcAuthMode | 调用ModifyInstanceVpcAuthMode接口开启或关闭云数据库MongoDB实例的专有网络免密访问功能。 |
|---|---|
| DescribeShardingNetworkAddre ss | 调用DescribeShardingNetworkAddress接口查询云数据库MongoDB分片集群实例的连接信息。 |
| ModifyDBInstanceConnectionSt ring | 调用ModifyDBInstanceConnectionString接口修改云数据库MongoDB实例的连接地址。 |
| ReleaseNodePrivateNetworkAd dress | 调用ReleaseNodePrivateNetworkAddress接口释放云数据库MongoDB分片集群实例的Shard节点或ConfigServer节点的内网连接地址。 |

| API | 描述 |
|---|---|
| DescribeReplicaSetRole | 调用DescribeReplicaSetRole接口查询云数据库MongoDB实例中的角色信息及连接信息。 |
| DescribeKernelReleaseNotes | 调用DescribeKernelReleaseNotes接口查询云数据库MongoDB实例的小版本发布日志。 |
| DescribeAvailableEngineVersio n | 调用DescribeAvailableEngineVersion接口查询云数据库MongoDB实例可升级的版本。 |
| DescribeDBInstances | 调用DescribeDBInstances接口查询云数据库MongoDB的实例列表。 |
| DescribeDBInstanceAttribute | 调用DescribeDBInstanceAttribute接口查询云数据库MongoDB的实例详情。 |
| DescribeRoleZoneInfo | 调用DescribeRoleZoneInfo接口查询云数据库MongoDB实例的各节点的角色和所属的可用区。 |

### 实例管理

| API | 描述 |
|---|---|
| RestartDBInstance | 调用RestartDBInstance接口重启云数据库MongoDB实例。 |
| ModifyDBInstanceMaintainTime | 调用ModifyDBInstanceMaintainTime接口修改云数据库MongoDB实例的可维护时间。 |
| ModifyDBInstanceDescription | 调用ModifyDBInstanceDescription接口修改云数据库MongoDB实例名称。 |
| SwitchDBInstanceHA | 调用SwitchDBInstanceHA接口切换云数据库MongoDB实例中的主备节点。 |
| UpgradeDBInstanceEngineVersi on | 调用UpgradeDBInstanceEngineVersion接口升级云数据库MongoDB实例的数据库版本。 |
| UpgradeDBInstanceKernelVersi on | 调用UpgradeDBInstanceKernelVersion接口升级云数据库MongoDB实例的数据库小版本。 |
| ModifyDBInstanceNetExpireTim e | 调用ModifyDBInstanceNetExpireTime接口延长云数据库MongoDB实例的经典网络保留时长。 |

### 账号管理

云数据库 MongoDB 版

| API | 描述 |
|---|---|
| DescribeAccounts | 调用DescribeAccounts接口查询云数据库MongoDB实例的数据库账号信息。 |
| ResetAccountPassword | 调用ResetAccountPassword接口重置云数据库MongoDB实例中root账号的密码。 |
| ModifyAccountDescription | 调用ModifyAccountDescription接口修改云数据库MongoDB实例中root账号的备注信息。 |

| API | 描述 |
|---|---|
| DescribeSecurityGroupConfigur ation | 调用DescribeSecurityGroupConfiguration接口查询云数据库MongoDB 实例绑定的ECS安全组信息。 |
| ModifySecurityGroupConfigurati on | 调用ModifySecurityGroupConfiguration更改云数据库MongoDB实例已绑定的ECS安全组。 |
| DescribeSecurityIps | 调用DescribeSecurityIps接口查询云数据库MongoDB实例的IP白名单。 |
| ModifySecurityIps | 调用ModifySecurityIps接口修改云数据库MongoDB实例的IP白名单。 |

### 密钥管理

| API | 描述 |
|---|---|
| DescribeDBInstanceTDEInfo | 调用DescribeDBInstanceTDEInfo接口查询云数据库MongoDB实例的透明数据加密TDE（Transparent Data Encryption）是否开启。 |
| ModifyDBInstanceTDE | 调用ModifyDBInstanceTDE接口修改云数据库MongoDB实例的透明数据加密TDE（Transparent Data Encryption）状态。 |

| API | 描述 |
|---|---|
| ModifyDBInstanceSSL | 调用ModifyDBInstanceSSL接口修改云数据库MongoDB实例的SSL配置。 |
| DescribeDBInstanceSSL | 调用DescribeDBInstanceSSL接口查询云数据库MongoDB实例的SSL设置详情。 |

### 审计日志

| API | 描述 |
|---|---|
| DescribeAuditRecords | 调用DescribeAuditRecords接口查询云数据库MongoDB实例的审计日志。 |
| DescribeAuditFiles | 调用DescribeAuditFiles接口查询云数据库MongoDB实例的审计日志文件。 |
| DescribeAuditPolicy | 调用DescribeAuditPolicy接口查询云数据库MongoDB实例的审计日志是否开启。 |
| ModifyAuditLogFilter | 调用ModifyAuditLogFilter接口修改云数据库MongoDB实例审计日志的采集类型。 |

| 云数据库 MongoDB 版 | 开发指南·API概览 |
|---|---|

| DescribeAuditLogFilter | 调用DescribeAuditLogFilter接口查询云数据库MongoDB实例审计日志采集的日志类型。 |
|---|---|
| ModifyAuditPolicy | 调用ModifyAuditPolicy接口设置云数据库MongoDB实例的审计日志开关或日志存储时长。 |

### 日志管理

| API | 描述 |
|---|---|
| DescribeSlowLogRecords | 调用DescribeSlowLogRecords接口查询云数据库MongoDB实例运行出现的慢操作日志明细。 |
| DescribeErrorLogRecords | 调用DescribeErrorLogRecords接口查询云数据库MongoDB实例的错误日志。 |
| DescribeRunningLogRecords | 调用DescribeRunningLogRecords接口查询云数据库MongoDB实例的运行日志。 |

| API | 描述 |
|---|---|
| DescribeDBInstancePerformanc e | 调用DescribeDBInstancePerformance接口查询云数据库MongoDB实例的性能数据。 |
| DescribeDBInstanceMonitor | 调用DescribeDBInstanceMonitor接口查询云数据库MongoDB实例的监控采集粒度。 |

### 参数管理

| API | 描述 |
|---|---|
| DescribeParameterModification History | 调用DescribeParameterModificationHistory接口查询云数据库MongoDB 实例参数的修改记录。 |
| DescribeParameters | 调用DescribeParameters接口查询云数据库MongoDB实例的参数配置信息。 |
| ModifyParameters | 调用ModifyParameters接口修改云数据库MongoDB实例的参数。 |

| API | 描述 |
|---|---|
| DescribeBackupPolicy | 调用DescribeBackupPolicy接口查询云数据库MongoDB实例的备份策略。 |
| ModifyBackupPolicy | 调用ModifyBackupPolicy接口修改云数据库MongoDB实例的备份策略。 |
| CreateBackup | 调用CreateBackup接口手动备份云数据库MongoDB实例。 |
| DescribeBackups | 调用DescribeBackups接口查询云数据库MongoDB实例的备份列表。 |
| RestoreDBInstance | 调用RestoreDBInstance接口恢复数据至当前云数据库MongoDB实例。 |

| DescribeBackupDBs | 在为云数据库MongoDB实例执行单库恢复前，您可以调用本接口查询指定的时间点或备份集内包含的数据库。 |
|---|---|

云数据库 MongoDB 版

## API参考

### 生命周期管理

#### CreateDBInstance

调用CreateDBInstance创建MongoDB副本集实例，同时也可用于克隆MongoDB副本集实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 是 | CreateDBInstance | 要执行的操作，取值： CreateDBInstance。 |
| RegionId | Strin g | Dom ain | 是 | cn-hangzhou | 实例所在地域。 |
| ClientToke n | Strin g | Quer y | 是 | ETnLKlblzczshOTUbOCzxx xxxxxxxx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符，且该参数值中不能包含非ASCII字符。 |
| ZoneId | Strin g | Quer y | 否 | cn-hangzhou-b | 可用区ID。 |
| Engine | Strin g | Quer y | 是 | MongoDB | 数据库引擎，取值： MongoDB。 |
| EngineVer sion | Strin g | Quer y | 是 | 4.0 | 数据库版本号。 |
| DBInstanc eClass | Strin g | Quer y | 是 | dds.mongo.standard | 实例规格。 |
| DBInstanc eStorage | Integ er | Quer y | 是 | 10 | 实例存储空间。 取值范围： 10~3000，单位为GB。 每 10GB递增。 |

云数据库 MongoDB 版

| DBInstanc eDescripti on | Strin g | Quer y | 否 | 测试数据库1 | 实例名称，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（ ）、短横线 _ （-）。 |
|---|---|---|---|---|---|
| SecurityIPL ist | Strin g | Quer y | 否 | 10.23.12.24/24 | 实例的IP白名单，以逗号隔开，不可重复，最多 1000个IP。 支持格式： %，0.0.0.0/0，10.23.12 .24（IP）或者 10.23.12.24/24（CIDR 模式，无类域间路由，/24 表示地址前缀的长度，范围为1~32）。 %和0.0.0.0/0表示任何 IP地址都可以访问实例的数据库，属于高危设置，请谨慎设置。 |
| AccountPa ssword | Strin g | Quer y | 否 | Alitest!159 | root账号的密码。 密码由大写字母、小写字母、数字、特殊字符中的至少三种组成，特殊字符为!#$%^&*() +-= _ 密码长度为8-32位。 |
| ChargeTyp e | Strin g | Quer y | 否 | PrePaid | 实例的付费类型，取值： PostPaid：后付费（按量付费）。 PrePaid：预付费（包年包月）。 默认付费类型为按量付费。当本参数值为PrePaid时，还需要传入Period参数。 |
| Period | Integ er | Quer y | 否 | 1 | 实例的购买时长，单位为月。 取值范围为：1~9，12，24，36。 当ChargeType参数值为 PrePaid时，本参数才可用且必须传入。 |

云数据库 MongoDB 版

| NetworkTy pe | Strin g | Quer y | 否 | VPC | 实例的网络类型，取值： classic：经典网络。 vpc：专有网络。 默认网络类型为经典网络。 当本参数值为vpc时，还需要传入VpcId参数和VSwitchId 参数。 |
|---|---|---|---|---|---|
| VpcId | Strin g | Quer y | 否 | vpc-bpxxxxxxxx | 专有网络（VPC）ID。 当 NetworkType参数值为VPC 时，本参数才可用。 |
| VSwitchId | Strin g | Quer y | 否 | vsw-bpxxxxxxxx | 虚拟交换机ID。 当 NetworkType参数值为VPC 时，本参数才可用。 |
| SrcDBInsta nceId | Strin g | Quer y | 否 | dds-bpxxxxxxxx | 源实例ID，只有调用本接口用于克隆实例时才能传入该参数，且必须和BackupId或 RestoreTime参数一同传入。 |
| BackupId | Strin g | Quer y | 否 | 32994xxxx | 具体的备份集ID，只有调用本接口用于克隆实例时才能传入该参数，且必须和 SrcDBInstanceId参数一同传入。 |
| RestoreTi me | Strin g | Quer y | 否 | 2019-03-13T12:11:14Z | 克隆实例时所恢复的时间点， 格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 只有调用本接口用于克隆实例时才能传入该参数， 且必须和 SrcDBInstanceId、 BackupId参数一同传入。 支持选择7天内的任一时间点进行克隆。 |
| BusinessIn fo | Strin g | Quer y | 否 | {“ActivityId":"000000000 "} | 附加参数，业务信息。 |

云数据库 MongoDB 版

| AutoRene w | Strin g | Quer y | 否 | true | 设置实例是否自动续费，取值： true：自动续费。 false：不自动续费，即手动续费。 默认为手动续费。 当 ChargeType参数值为 PrePaid时，本参数才可用。 |
|---|---|---|---|---|---|
| DatabaseN ames | Strin g | Quer y | 否 | mongodbtest | 数据库名。 调用本接口用于克隆实例操作时，可传入该参数指定需要克隆的数据库，如不传入，则克隆实例的所有数据库。 |
| StorageEn gine | Strin g | Quer y | 否 | WiredTiger | 仅支持WiredTiger。 如不填则默认为WiredTiger。 |
| Replication Factor | Strin g | Quer y | 否 | 3 | 副本集节点个数，取值： 3，5，7。 默认值为3。 |
| ReadonlyR eplicas | Strin g | Quer y | 否 | 1 | 创建只读节点的个数，取值范围为1~5。 默认不传入该参数，即默认不创建只读节点。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-axxxxxxxx | 资源组ID。 |
| CpuType | Strin g | Quer y | 否 | intel | CPU芯片类型。取值： intel、arm等。 |
| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv4 | 实例支持的网络类型，默认值 IPv4。取值范围： IPv4 IPv4v6 |
| SecurityIPv 6List | Strin g | Quer y | 否 | 2001:db8::1,2001:db8::ff, 2001:db8:1::/64 | IPv6白名单IP。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云数据库 MongoDB 版

| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9624D | 请求ID。 |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxxxxx | 订单ID。 |
| DBInstanceId | String | dds-bpxxxxxxxx | 实例ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &ClientToken=ETnLKlblzczshOTUbOCzxxxxxxxxxx &Engine=MongoDB &EngineVersion=4.0 &DBInstanceClass=dds.mongo.standard &DBInstanceStorage=10
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"D8F1D721-6439-4257-A89C-F1E8E9C9624D",
 "DBInstanceId":"dds-bpxxxxxxxx",
 "OrderId":"2033xxxxxxxxxxxx"
}
```

`XML` 格式

```xml
<RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9624D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <OrderId>2033xxxxxxxxxxxx</OrderId>
```

#### ModifyDBInstanceSpec

调用ModifyDBInstanceSpec接口变更MongoDB副本集实例的规格或存储空间。 该接口仅适用于MongoDB副本集实例。分片集群实例如需变更配置，您可以根据需求通过调用**ModifyNodeSpec**、**CreateNode**或**DeleteNode**接口来实现。 调用ModifyDBInstanceSpec接口时，您需要在调用代码的Header中设置 `x-acs-` `organizationid` 、 `x-acs-resourcegroupid` 、 `x-acs-instanceid` 等参数，用于指定资源所属的组织、资源集以及资源实例ID，否则调用接口时会指向根组织和根资源集。具体调用代码请参见云数据库云数据库 MongoDB 版 MongoDB产品简介中的SDK说明。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eSpec | 系统规定参数，取值：ModifyDBInstanceSpec。 |
| DBInstanceId | String | 是 | dds- d1n4eab47879* *** | 实例ID。 |
| RegionId | String | 否 | cn-qd- agility14**** | 实例所属的地域ID。 说明您可以通过DescribeDBInstanceAttribu te接口查询实例所属地域ID。 |
| DBInstanceClass | String | 否 | dds.mongo.stan dard | 实例规格。 说明规格信息请参见云数据库Mo ngoDB产品简介中的实例规格表。 本参数和 DBInstanceStorage 参数两者中必须配置一项。 |
| DBInstanceStora ge | String | 否 | 50 | 实例的存储空间，取值范围为10~3000 GB，步长为10 GB。 说明取值受实例规格约束，详情请参见云数据库MongoDB产品简介中的实例规格表。 本参数和 DBInstanceClass 参数两者中必须配置一项。 仅按量付费的副本集实例支持降配存储空间，且存储空间必须大于当前已使用的存储空间。 |

云数据库 MongoDB 版

| OrderType | String | 否 | UPGRADE | 变配类型，取值如下： UPGRADE：升级配置。 DOWNGRADE：降级配置。 默认为DOWNGRADE。 说明当付费类型为PostPaid时，需要配置该参数。 |
|---|---|---|---|---|
| AutoPay | Boolean | 否 | true | 是否自动付费。取值如下： true：自动付费，请确保账号有足够的余额。 false：控制台手动付费。 默认值为true。 |
| BusinessInfo | String | 否 | {“ActivityId":"00 0000000"} | 业务信息。 |
| ReplicationFacto r | String | 否 | 3 | 设置实例的节点个数。副本集实例取值为3，5，7。单节点实例取值固定为1。 |
| ReadonlyReplica s | String | 否 | 1 | 只读节点的个数，取值范围为1~5。 |
| CouponNo | String | 否 | youhuiquan pro _ motion option i _ _ d for blank _ _ | 优惠码，默认为：youhuiquan promotion optio _ _ n id for blank。 _ _ _ |
| EffectiveTime | String | 否 | Immediately | 变更配置的生效时间，取值如下： Immediately：立即生效。 MaintainTime：在实例的可运维时间段内生效。 默认为Immediately。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 20331066**** | 订单ID。 |
| RequestId | String | C5662998-62BE- 4C7F-961D- 7DFE775D**** | 请求ID。 |

**示例**

请求示例云数据库 MongoDB 版

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSpec &DBInstanceId=dds-d1n4eab47879****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>C5662998-62BE-4C7F-961D-7DFE775D****</RequestId>
  <OrderId>20331066****</OrderId>
```

`JSON` 格式

```json
{
  "RequestId": "C5662998-62BE-4C7F-961D-7DFE775D****",
  "OrderId": "20331066****"
}
```

#### DeleteDBInstance

调用该接口时，实例状态必须为运行中。实例释放后数据将无法找回，请谨慎操作。 调用DeleteDBInstance接口时，您需要在调用代码的Header中设置 `x-acs-organizationid` 、 `x-` `acs-resourcegroupid` 、 `x-acs-instanceid` 等参数，用于指定资源所属的组织、资源集以及资源实例ID，否则调用接口时会指向根组织和根资源集。具体调用代码请参见云数据库MongoDB产品简介中的 SDK说明。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteDBInstanc e | 要执行的操作，取值DeleteDBInstance。 |
| DBInstanceId | String | 是 | dds- d1n4eab47879* *** | 实例ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz**** | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库 MongoDB 版

| RequestId | String | 72651AF9-7897- 41A7-8B67- 6C15C7F2**** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DeleteDBInstance &DBInstanceId=dds-d1n4eab47879****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
  <RequestId>72651AF9-7897-41A7-8B67-6C15C7F2****</RequestId>
```

`JSON` 格式

```json
{
  "RequestId": "72651AF9-7897-41A7-8B67-6C15C7F2****"
}
```

#### CreateShardingDBInstance

调用CreateShardingDBInstance接口创建或者克隆MongoDB分片集群实例。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 是 | CreateShardingDBInstanc e | 要执行的操作，取值： CreateShardingDBInstanc e。 |
| RegionId | Strin g | Host | 是 | cn-qd-agility14**** | 实例所属的地域ID。 |
| ZoneId | Strin g | Quer y | 否 | cn-qd-agility14- amtest110**** | 实例所属的可用区ID。 |
| Engine | Strin g | Quer y | 是 | MongoDB | 数据库引擎，取值为 MongoDB。 |

云数据库 MongoDB 版

| EngineVer sion | Strin g | Quer y | 是 | 4.0 | 数据库版本号。 |
|---|---|---|---|---|---|
| Mongos | Repe atLis t | Quer y | 否 | - | Mongos结构。 |
| -Class | Strin g |  | 否 | dds.cs.mid | CongfigServer的规格。 |
| ReplicaSet | Repe atLis t | Quer y | 否 | - | ReplicaSet结构。 |
| -Class | Strin g |  | 否 | dds.cs.mid | CongfigServer的规格。 |
| -Storage | Integ er |  | 否 | 20 | CongfigServer的存储空间。 |
| ConfigServ er | Repe atLis t | Quer y | 否 | - | ConfigServer结构。 |
| -Class | Strin g |  | 否 | dds.cs.mid | CongfigServer的规格。 |
| -Storage | Integ er |  | 否 | 20 | CongfigServer的存储空间。 |
| DBInstanc eDescripti on | Strin g | Quer y | 否 | 测试数据库1 | 实例名称。命名规则如下： 以中文、英文字母开头， 可以包含数字、中文、英文、下划线（ ）、短划线 _ （-）。 长度为2~256个字符。 |

云数据库 MongoDB 版

| SecurityIPL ist | Strin g | Quer y | 否 | 10.23.12.24/24 | 实例的IP白名单，以逗号隔开，不可重复，最多 1000个IP。 支持格式： %，0.0.0.0/0，10.23.12 .24（IP）或 10.23.12.24/24（CIDR 模式，无类域间路由，/24 表示地址前缀的长度，范围为1~32）。 %和0.0.0.0/0表示任何 IP地址都可以访问实例的数据库，属于高危设置，请谨慎设置。 |
|---|---|---|---|---|---|
| AccountPa ssword | Strin g | Quer y | 否 | Alitest**** | root账号的密码。密码规则如下： 密码由大写字母、小写字母、数字、特殊字符中的至少三种组成，特殊字符为： !#$%^&*() +-= _ 密码长度为8~32位。 |
| ChargeTyp e | Strin g | Quer y | 否 | PrePaid | 实例的付费类型，取值： PostPaid：后付费（按量付费）。 PrePaid：预付费（包年包月）。 默认为 PostPaid。 当付费类型为PrePaid时， 还需要配置Period参数。 |
| Period | Integ er | Quer y | 否 | 1 | 实例的购买时长，单位为月。 取值范围为： 1~9，12，24，36。当 ChargeType参数值为 PrePaid时，需要配置该参数。 |
| NetworkTy pe | Strin g | Quer y | 否 | Classic | 实例的网络类型。 取值： Classic：经典网络。 VPC：专有网络。 默认为Classic。 当网络类型为VPC时，还需要传入VpcId 和VSwitchId参数。 |

云数据库 MongoDB 版

| VpcId | Strin g | Quer y | 否 | vpc- bp1q2qqm4vxo6e6zl**** | 专有网络（VPC）ID。 当网络类型为VPC时，需要配置该参数。 |
|---|---|---|---|---|---|
| VSwitchId | Strin g | Quer y | 否 | vsw- bp1buy0h9myt5i9e7**** | 虚拟交换机ID。 当网络类型为VPC时，需要配置该参数。 |
| SrcDBInsta nceId | Strin g | Quer y | 否 | dds-bp1b47357f21**** | 源实例ID。 当调用本接口用于克隆实例时，需要配置该参数，且必须和RestoreTime 参数一同配置。 |
| RestoreTi me | Strin g | Quer y | 否 | 2019-03-08T02:30:25Z | 克隆实例时所恢复的时间点， 格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 当调用本接口用于克隆实例时，需要配置该参数， 且必须和SrcDBInstanceId 参数一同配置。 支持选择7天内的任一时间点进行克隆。 |
| ClientToke n | Strin g | Quer y | 否 | ETnLKlblzczshOTUbOCz** ** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个 ASCII字符，且该参数值中不能包含非ASCII字符。 |
| StorageEn gine | Strin g | Quer y | 否 | WiredTiger | 数据库存储引擎，仅支持 WiredTiger。 |
| AutoRene w | Strin g | Quer y | 否 | false | 设置实例是否自动续费，取值： true：自动续费。 false：不自动续费，即手动续费。 默认为false。 当付费类型为 PrePaid时，需要配置该参数。 |
| ResourceG roupId | Strin g | Quer y | 否 | rg-acfm22cdcgc**** | 资源组ID。 |

云数据库 MongoDB 版

| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv4 | 实例支持的网络类型，默认值 IPv4。取值范围： IPv4 IPv4v6 |
|---|---|---|---|---|---|
| SecurityIPv 6List | Strin g | Quer y | 否 | 2001:db8::1,2001:db8::ff, 2001:db8:1::/64 | IPv6白名单IP。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | D8F1D721-6439- 4257-A89C- F1E8E9C9**** | 请求ID。 |
| OrderId | String | 20331066**** | 资源ID。 |
| DBInstanceId | String | dds- bp14ed961586**** | 实例ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateShardingDBInstance &RegionId=cn-qd-agility14**** &Engine=MongoDB &EngineVersion=4.0
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"D8F1D721-6439-4257-A89C-F1E8E9C9****",
 "DBInstanceId":"dds-bp14ed961586****",
 "OrderId":"20331066****"
}
```

`XML` 格式云数据库 MongoDB 版

```xml
<RequestId>D8F1D721-6439-4257-A89C-F1E8E9C9****</RequestId> <DBInstanceId>dds-bp14ed961586****</DBInstanceId> <OrderId>20331066****</OrderId>
```

#### CreateNode

调用CreateNode接口为MongoDB分片集群实例增加Shard节点或Mongos节点。 该接口仅适用于分片集群实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNode | 要执行的操作，取值：CreateNode。 |
| NodeClass | String | 是 | dds.shard.mid | Shard节点或Mongos节点的规格。 |
| NodeType | String | 是 | shard | Node的类型，取值： shard：Shrad节点。 mongos：Mongos节点。 |
| DBInstanceId | String | 是 | dds- bp11501cd7b5* *** | 分片集群实例ID。 |
| NodeStorage | Integer | 否 | 10 | Node的磁盘空间，当NodeType参数取值为Shard时该参数可用，且该参数必须传入。 取值范围：10~2000，单位为GB。 每10 GB进行递增。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。 |
| FromApp | String | 否 | OpenApi | 请求来源，取值： OpenApi：请求来源为OpenApi。 mongo buy：请求来源为控制台。 _ |
| AutoPay | Boolean | 否 | true | 是否自动付费。取值： true：自动付费，请确保账号有足够的余额。 false：控制台手动付费。 默认值：true。 |

云数据库 MongoDB 版

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NodeId | String | d- bp1b7bb3bbe1**** | 节点ID。 |
| OrderId | String | 2034**** | 订单ID。 |
| RequestId | String | 7D48FB19-20CA- 4725-A870- 3D8F5CE69F14 | 请求ID。 |

**示例**

请求示例

```
&NodeClass=dds.shard.mid &NodeType=shard &DBInstanceId=dds-bp11501cd7b5****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>7D48FB19-20CA-4725-A870-3D8F5CE69F14</RequestId> <NodeId>d-bp1b7bb3bbe1****</NodeId> <OrderId>2034****</OrderId>
```

`JSON` 格式

```json
{
    "RequestId": "7D48FB19-20CA-4725-A870-3D8F5CE69F14",
    "NodeId": "d-bp1b7bb3bbe1****",
    "OrderId": "2034****"
}
```

#### DeleteNode

调用DeleteNode接口删除MongoDB分片集群实例中的Shard节点或Mongos节点。 调用本接口时，实例必须满足以下条件： 实例状态为运行中。 实例类型为分片集群实例。 实例中Shard节点或Mongos节点的数量必须大于2。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | DeleteNode | 要执行的操作，取值：DeleteNode。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | dds- bp11501cd7b5* *** | 实例ID。 |
| NodeId | String | 是 | s- bp1713dece57* *** | 待删除的Shard节点ID或Mongos节点 ID。您可以通过 DescribeDBInstanceAttribute接口查询节点ID。 |
| ClientToken | String | 否 | ETnLKlblzczshOT UbOCz**** | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 2033**** | 订单ID。 |
| RequestId | String | 9F9BDE64-BF30- 41F3-BD29- C19CE4AB3404 | 请求ID。 |
| TaskId | Integer | 111111111 | 任务ID。 |

**示例**

请求示例

```
&DBInstanceId=dds-bp11501cd7b5**** &NodeId=s-bp1713dece57****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TaskId>111111111</TaskId> <RequestId>9F9BDE64-BF30-41F3-BD29-C19CE4AB3404</RequestId> <OrderId>2033****</OrderId>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
    "TaskId": 111111111,
    "RequestId": "9F9BDE64-BF30-41F3-BD29-C19CE4AB3404",
    "OrderId": "2033****"
}
```

#### ModifyNodeSpec

调用ModifyNodeSpec接口变更MongoDB分片集群实例中节点的规格和存储空间。 该接口仅适用于分片集群实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyNodeSpec | 要执行的操作，取值：ModifyNodeSpec。 |
| NodeId | String | 是 | d-bpxxxxxxxx | 分片集群实例中Shard节点ID或Mongos 节点ID，您可以通过调用DescribeDBInstanceAttribute接口进行查询。 说明当传入的值为Shard节点ID时，还需要传入NodeStorage参数。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| NodeClass | String | 否 | dds.shard.stand ard | Shard节点或Mongos节点的规格，规格详情请参见云数据库MongoDB版中的产品简介 > 实例规格。 说明本参数和NodeStorage参数两者必须传入一个。 |
| NodeStorage | Integer | 否 | 20 | 设置Shard节点的存储空间。 取值范围：10~2000，单位为GB。 每10GB进行递增。 说明本参数和NodeClass参数两者必须传入一个。 当NodeId传入的值为 Shard节点ID时，本参数才可用。 |

云数据库 MongoDB 版

| ClientToken | String | 否 | ETnLKlblzczshOT UbOCzxxxxxxxx xx | 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII 字符，且该参数值中不能包含非ASCII字符。 |
|---|---|---|---|---|
| AutoPay | Boolean | 否 | true | 是否自动付费。取值： true：自动付费，请确保账号有足够的余额。 false：控制台手动付费。具体操作为：登录控制台，在右上角选择费用> 进入费用中心，在订单管理找到目标订单进行支付。 默认值为：true。 |
| EffectiveTime | String | 否 | Immediately | 变更配置的生效时间，取值： Immediately：立即生效。 MaintainTime：实例可运维时间段内生效。 默认值为Immediately。 |
| FromApp | String | 否 | OpenApi | 请求来源，取值： OpenApi：请求来源为OpenApi。 mongo buy：请求来源为控制台。 _ |
| OrderType | String | 否 | UPGRADE | 订单类型。取值： UPGRADE：升配 DOWNGRADE：降配 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| OrderId | String | 2033xxxxxxxxx | 订单ID。 |
| RequestId | String | EFFC5788-8BB5- 41B5-9F15- 9CFC5A0E8FCC | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.aliyuncs.com/?Action=ModifyNodeSpec &NodeId=d-bpxxxxxxxx &DBInstanceId=dds-bpxxxxxxxx &NodeClass=dds.shard.standard &NodeStorage=20
```

`&<`公共请求参数> 云数据库 MongoDB 版正常返回示例 `XML` 格式

```xml
   <OrderId>2033xxxxxxxxx</OrderId>
   <RequestId>EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC</RequestId>
```

`JSON` 格式

```json
{
    "OrderId": "2033xxxxxxxx",
    "RequestId": "EFFC5788-8BB5-41B5-9F15-9CFC5A0E8FCC"
}
```

#### InitializeDdsPermission

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | InitializeDdsPermission | 系统规定参数，取值： InitializeDdsPermission 。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | 请求 ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=InitializeDdsPermission
```

&公共请求参数正常返回示例 `JSON` 格式云数据库 MongoDB 版

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":""
}
```

`XML` 格式

```xml
<RequestId />
```

### 区域管理

#### MigrateToOtherZone

本接口适用于副本集实例，暂不支持分片集群实例。

**说明**

如果实例申请了公网连接地址，需要先调用**ReleasePublicNetworkAddress**接口释放公网连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | MigrateToOther Zone | 要执行的操作，取值：MigrateToOtherZone。 |
| InstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明如果实例的网络类型为专有网络，您还需要传入Vswitch参数。 |
| ZoneId | String | 是 | cn-hangzhou-b | 迁移的目标可用区ID。 说明迁移的目标可用区必须和当前实例的可用区处于同一地域。 您可以通过调用DescribeRegions接口查询可用区ID。 |

云数据库 MongoDB 版

| EffectiveTime | String | 否 | Immediately | 迁移可用区的生效时间，取值： Immediately：立即生效。 MaintainTime：在实例的可运维时间段内生效。 默认为Immediately。 |
|---|---|---|---|---|
| VSwitchId | String | 否 | vsw-bpxxxxxxxx | 迁移的目标可用区虚拟交换机ID。 说明当实例的网络类型为专有网络时，本参数才可用且必须传入。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=MigrateToOtherZone &InstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

#### DescribeRegions

云数据库 MongoDB 版调用CreateDBInstance或CreateShardingDBInstance接口创建实例之前，请先用本接口查询支持的地域和可用区信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 要执行的操作，取值： DescribeRegions。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of DdsRegion |  | 地域信息列表。 |
| DdsRegion |  |  |  |
| RegionId | String | cn-qingdao | 地域ID。 |
| Zones | Array of Zone |  | 可用区信息列表。 |
| Zone |  |  |  |
| VpcEnabled | Boolean | true | 是否支持专有网络。返回值： true：支持 false：不支持 |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |
| RequestId | String | 4E46C22C-D3B7- 4DB8-9C76- 63851BE68E20 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeRegions
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <RequestId>4E46C22C-D3B7-4DB8-9C76-63851BE68E20</RequestId>
   <Regions>
      <DdsRegion>
         <RegionId>cn-hangzhou</RegionId>
         <Zones>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-i</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-b</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-d</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-f</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-MAZ5(b,e,f)</ZoneId>
            </Zone>
            <Zone>
               <VpcEnabled>true</VpcEnabled>
               <ZoneId>cn-hangzhou-g</ZoneId>
            </Zone>
         </Zones>
      </DdsRegion>
   </Regions>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
 "RequestId": "4E46C22C-D3B7-4DB8-9C76-63851BE68E20",
 "Regions": {
  "DdsRegion": [
   {
    "RegionId": "cn-hangzhou",
    "Zones": {
     "Zone": [
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-i"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-b"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-d"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-f"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-MAZ5(b,e,f)"
      },
      {
       "VpcEnabled": true,
       "ZoneId": "cn-hangzhou-g"
      }
```

]

```
    }
   }
```

]

```
 }
}
```

#### MigrateAvailableZone

本接口适用于副本集实例，暂不支持分片集群实例。 如果实例申请了公网连接地址，需要先调用**ReleasePublicNetworkAddress**接口释

**说明**

放公网连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | MigrateAvailable Zone | 要执行的操作，取值MigrateAvailableZone。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明如果实例的网络类型为专有网络，您还需要传入Vswitch参数。 |
| ZoneId | String | 是 | cn-hangzhou-b | 迁移的目标可用区ID。 说明迁移的目标可用区和当前实例的可用区处于同一地域。 您可以通过调用DescribeRegions接口查询可用区ID。 |
| Vswitch | String | 否 | vsw-bpxxxxxxxx | 迁移的目标可用区虚拟交换机ID。 说明当实例的网络类型为专有网络时，本参数才可用且必须传入。 |
| EffectiveTime | String | 否 | Immediately | 迁移可用区的生效时间，取值： Immediately：立即生效。 MaintainTime：在实例的可运维时间段内生效。 默认为Immediately。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=MigrateAvailableZone &DBInstanceId=dds-bpxxxxxxxx &ZoneId=cn-hangzhou-b &EffectiveTime=Immediately
```

`&<`公共请求参数> 正常返回示例云数据库 MongoDB 版 `XML` 格式

```xml
   <RequestId>0FDDC511-7252-4A4A-ADDA-5CB1BF63873D</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

### 资源管理

#### DescribeAvailableResource

调用DescribeAvailableResource查询指定可用区内可创建的实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAvailabl eResource | 要执行的操作。取值：DescribeAvailableResource。 |
| RegionId | String | 是 | cn-hangzhou | 地域ID，您可以通过调用DescribeRegions进行查询。 |
| ZoneId | String | 否 | cn-hangzhou-h | 可用区ID，您可以通过DescribeRegions查看可用的可用区。 |
| InstanceChargeT ype | String | 否 | PrePaid | 付费类型，取值： PrePaid（包年包月） PostPaid（按量付费） 说明默认值：PrePaid。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 344EE51D-8850- 4935-B68B- 58A8F4DCE3BD | 请求ID。 |
| SupportedDBT ypes | Array of SupportedDBT ype |  | 支持的数据库类型。 |

云数据库 MongoDB 版

| SupportedDBT ype |  |  |  |
|---|---|---|---|
| AvailableZone s | Array of AvailableZone |  | 可用区。 |
| AvailableZone |  |  |  |
| RegionId | String | cn-hangzhou | 地域ID。 |
| SupportedEngi neVersions | Array of SupportedEngi neVersion |  | 支持的存储引擎版本。 |
| SupportedEngi neVersion |  |  |  |
| SupportedEngi nes | Array of SupportedEngi ne |  | 支持的存储引擎。 |
| SupportedEngi ne |  |  |  |
| Engine | String | WiredTiger | 实例的存储引擎。 |
| SupportedNod eTypes | Array of SupportedNod eType |  | 支持的实例类型。 |
| SupportedNod eType |  |  |  |
| AvailableReso urces | Array of AvailableReso urce |  | 可用的资源详情。 |
| AvailableReso urce |  |  |  |
| InstanceClass | String | dds.mongo.2xlarge | 实例规格族。 |
| InstanceClass Remark | String | 8核32G（最大连接数 8000 IOPS 14000） | 实例规格。 |
| NetworkTypes | String | VPC | 实例的网络类型。 |
| NodeType | String | 3 | 实例的节点数。 |
| Version | String | 4.0 | 实例的版本。 |
| ZoneId | String | cn-hangzhou-h | 可用区ID。 |

云数据库 MongoDB 版

| DbType | String | sharding | 实例的数据库类型。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeAvailableResource &RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>344EE51D-8850-4935-B68B-58A8F4DCE3BD</RequestId> <SupportedDBTypes>
    <DbType>sharding</DbType>
</SupportedDBTypes> <SupportedDBTypes>
    <AvailableZones>
        <ZoneId>cn-hangzhou-h</ZoneId>
        <RegionId>cn-hangzhou</RegionId>
    </AvailableZones>
    <AvailableZones>
        <SupportedEngineVersions>
            <Version>4.0</Version>
        </SupportedEngineVersions>
        <SupportedEngineVersions>
            <SupportedEngines>
                <Engine>WiredTiger</Engine>
            </SupportedEngines>
            <SupportedEngines>
                <SupportedNodeTypes>
                    <NetworkTypes>VPC</NetworkTypes>
                    <NodeType>3</NodeType>
                </SupportedNodeTypes>
                <SupportedNodeTypes>
                    <AvailableResources>
                        <InstanceClassRemark>8核32G（最大连接数 8000 IOPS 14000）</Instance
ClassRemark>
                        <InstanceClass>dds.mongo.2xlarge</InstanceClass>
                    </AvailableResources>
                </SupportedNodeTypes>
            </SupportedEngines>
        </SupportedEngineVersions>
    </AvailableZones>
</SupportedDBTypes>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
    "RequestId":"344EE51D-8850-4935-B68B-58A8F4DCE3BD",
    "SupportedDBTypes":[
        {
            "DbType":"sharding"
        },
        {
            "AvailableZones":[
                {
                    "ZoneId":"cn-hangzhou-h",
                    "RegionId":"cn-hangzhou"
                },
                {
                    "SupportedEngineVersions":[
                        {
                            "Version":"4.0"
                        },
                        {
                            "SupportedEngines":[
                                {
                                    "Engine":"WiredTiger"
                                },
                                {
                                    "SupportedNodeTypes":[
                                        {
                                            "NetworkTypes":"VPC",
                                            "NodeType":"3"
                                        },
                                        {
                                            "AvailableResources":[
                                                {
```

`"InstanceClassRemark":"8`核`32G`（最大连接

```json
数 8000 IOPS 14000）",
                                                    "InstanceClass":"dds.mongo.2xlarge"
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

]

```
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

]

```
}
```

### 连接管理

#### AllocatePublicNetworkAddress

云数据库 MongoDB 版调用AllocatePublicNetworkAddress接口为MongoDB实例申请公网连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AllocatePublicNe tworkAddress | 要执行的操作，取值：AllocatePublicNetworkAddres s。 |
| DBInstanceId | String | 是 | dds- bp11501cd7b5* *** | 实例ID。 说明当本参数传入的是分片集群实例ID 时，还需要传入NodeId参数。 |
| NodeId | String | 否 | s- bp1713dece57* *** | 分片集群实例中Mongos节点ID、Shard节点ID或ConfigServer节点ID。 说明当DBInstanceId传入的是分片集群实例ID时，本参数才可用。 您可以调用 DescribeDBInstanceAttrib ute接口查询Mongos节点 ID、Shard节点ID或 ConfigServer节点ID。 |
| IPVersionSelecte dType | String | 否 | IPv6 | IP类型，默认为IPv4。取值范围： IPv4 IPv6 IPv4v6 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B6D17591-B48B- 4D31-9CD6- 9B9796B2270A | 请求ID。 |

**示例**

请求示例云数据库 MongoDB 版

```
http(s)://mongodb.aliyuncs.com/?Action=AllocatePublicNetworkAddress &DBInstanceId=dds-bp11501cd7b5****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>B6D17591-B48B-4D31-9CD6-9B9796B2270A</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "B6D17591-B48B-4D31-9CD6-9B9796B2270A"
}
```

#### AllocateNodePrivateNetworkAddress

调用 AllocateNodePrivateNetworkAddress 接口，为 MongoDB 分片集群实例的 Shard 节点、 ConfigServer 节点申请内网连接地址，或仅为 Mongos 节点申请 IPv6 内网连接地址。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AllocateNodePri vateNetworkAdd ress | 要执行的操作，取值：AllocateNodePrivateNetwork Address。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 分片集群实例ID。 |
| NodeId | String | 是 | d-bpxxxxxxxx | 节点ID。 Shard节点 ConfigServer节点。 Mongos节点。 |
| ZoneId | String | 否 | cn-hangzhou-b | 实例所属的可用区ID。 |

云数据库 MongoDB 版

| AccountName | String | 否 | shardcsaccount | 账户名。 说明以小写字母开头，长度为 4~16位，由小写字母、数字或下划线组成。 仅在首次申请 Shard/ConfigServer/Mong os地址时，需要设置账户名和账户密码。即所有Shard 节点和ConfigServer节点都将使用首次申请地址时设置的账户和密码。 该账户的权限固定为只读权限。 |
|---|---|---|---|---|
| AccountPasswor d | String | 否 | Test123456 | 账户密码。 密码由大写字母、小写字母、数字、特殊字符中的至少三种组成，特殊字符为!#$%^&amp;*() +-= _ 密码长度为8-32位 |
| IPVersionSelecte dType | String | 否 | IPv6 | IP类型，取值范围： IPv4 IPv6 IPv4v6 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=AllocateNodePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx &NodeId=d-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<AllocateNodePrivateNetworkAddressResponse>
   <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</AllocateNodePrivateNetworkAddressResponse>
```

`JSON` 格式

```json
{
 "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

#### ReleasePublicNetworkAddress

调用ReleasePublicNetworkAddress接口释放MongoDB实例的公网连接地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | 是 | dds-bpxxxxxxxx | 实例ID。 当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NodeId | Strin g | Quer y | 否 | s-bpxxxxxxxx | 分片集群实例中Mongos节点 ID、Shard节点ID或 ConfigServer节点ID。当 DBInstanceId传入的是分片集群实例ID时，本参数才可用。 |
| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv4 | IP类型，取值范围： IPv4 IPv6 IPv4v6 分片集的Mongos私网仅支持 IPv6。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

云数据库 MongoDB 版

| RequestId | String | 1D6AFE36-1AF5- 4DE4-A954- 672159D4CC69 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ReleasePublicNetworkAddress &DBInstanceId=dds-bpxxxxxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"1D6AFE36-1AF5-4DE4-A954-672159D4CC69"
}
```

`XML` 格式

```xml
<RequestId>1D6AFE36-1AF5-4DE4-A954-672159D4CC69</RequestId>
```

#### ModifyInstanceVpcAuthMode

调用ModifyInstanceVpcAuthMode接口开启或关闭MongoDB实例的专有网络免密访问功能。 调用本接口时，实例必须满足以下条件： 实例的类型为副本集实例或分片集群实例。 实例的数据库版本为4.0版本或4.2版本。您可以通过调用**DescribeDBInstanceAttribute**接口查看版本信息。如果版本过低请调用**UpgradeDBInstanceEngineVersion**接口升级数据库版本。 实例的网络类型为专有网络。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyInstanceV pcAuthMode | 要执行的操作，取值ModifyInstanceVpcAuthMode。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| RegionId | String | 否 | cn-hangzhou | 实例所属的地域ID，您可以通过调用DescribeDBInstanceAttribute进行查询。 |
|---|---|---|---|---|
| NodeId | String | 否 | s-bpxxxxxxxx | 分片集群实例的Mongos节点ID。 说明实例类型为分片集群实例时，本参数才可用。 |
| VpcAuthMode | String | 否 | Open | 设置专有网络免密访问功能，取值： Open：开启专有网络免密访问。 Close：关闭专有网络免密访问。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | BA51E9D9-B14A- 4542-B6E6- 7DE00BECCB8C | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyInstanceVpcAuthMode &DBInstanceId=dds-bpxxxxxxxx &VpcAuthMode=Open
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "BA51E9D9-B14A-4542-B6E6-7DE00BECCB8C"
}
```

#### DescribeShardingNetworkAddress

调用DescribeShardingNetworkAddress接口查询MongoDB分片集群实例的连接信息。 该接口仅支持分片集群实例。 云数据库 MongoDB 版

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeShardin gNetworkAddres s | 要执行的操作，取值：DescribeShardingNetworkAd dress。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID、Shard节点ID或ConfigServer节点ID。 说明您可以调用DescribeDBInstanceAttribu te接口查询Mongos、Shard、 ConfigServer节点ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CompatibleCo nnections | Array of CompatibleCo nnection |  | DynamoDB协议类型实例的连接地址信息列表。 |
| CompatibleCo nnection |  |  |  |
| ExpiredTime | String | 2591963 | 保留的经典网络地址剩余时长，单位为秒。 |
| IPAddress | String | 10.140.xxx.xx | IP地址。 |
| NetworkAddre ss | String | dds- bpxxxxxxxxxxxxxx. mongodb.rds.aliyu ncs.com | 连接地址。 |
| NetworkType | String | VPC | 网络类型。取值： VPC：专有网络。 Classic：经典网络。 Public：公网。 |

云数据库 MongoDB 版

| Port | String | 3717 | 连接端口。 |
|---|---|---|---|
| VPCId | String | vpc-bpxxxxxxxx | 专有网络ID。 说明当网络类型为VPC时返回该参数。 |
| VswitchId | String | vsw-bpxxxxxxxx | 专有网络中交换机ID。 说明当网络类型为VPC时返回该参数。 |
| NetworkAddre sses | Array of NetworkAddre ss |  | MongoDB协议类型实例的连接地址信息列表。 |
| NetworkAddre ss |  |  |  |
| ExpiredTime | String | 2591963 | 保留的经典网络地址剩余时长，单位为秒。 |
| IPAddress | String | 10.140.xxx.xx | IP地址。 |
| NetworkAddre ss | String | s- bpxxxxxxxx.mongo db.rds.aliyuncs.co m | 连接地址（字符串）。 |
| NetworkType | String | VPC | 网络类型。 VPC：专有网络。 Classic：经典网络。 Public：公网。 |
| NodeId | String | s-bpxxxxxxxx | Mongos节点ID。 |
| NodeType | String | mongos | 节点类型，返回值为 mongos：mongos节点。 shard：shard节点。 configserver：configserver节点。 |
| Port | String | 3717 | 连接端口。 |

云数据库 MongoDB 版

| Role | String | Primary | 节点角色，返回值： Primary：主节点。 Secondary：从节点。 |
|---|---|---|---|
| VPCId | String | vpc-bpxxxxxxxx | 专有网络ID。 说明当网络类型为VPC时返回该参数。 |
| VswitchId | String | vsw-bpxxxxxxxx | 专有网络中交换机ID。 说明当网络类型为VPC时返回该参数。 |
| IpVersion | String | ipv4 | IP类型，取值范围： ipv4 ipv4v6 |
| IPAddress | String | 192.168.1.xxx | IPv4地址。 |
| IPAddressV6 | String | 2001:0db8:85a3:0 000:0000:8a2e:03 70:xxxx | IPv6地址。 |
| RequestId | String | 18D8AAFD-6BEB- 420F-8164- 810CB0C0AA39 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeShardingNetworkAddress &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<DescribeDBInstanceNetInfoResponse>
    <RequestId>18D8AAFD-6BEB-420F-8164-810CB0C0AA39</RequestId>
```

<!-- DynamoDB 协议类型实例连接列表 `-->`

```xml
    <CompatibleConnections>
        <CompatibleConnection>
            <IPAddress>10.140.23.45</IPAddress>
            <NetworkAddress>dds-
bp1a2b3c4d5e6f7g.mongodb.rds.aliyuncs.com</NetworkAddress>
            <NetworkType>VPC</NetworkType>
            <Port>3717</Port>
            <ExpiredTime>2591963</ExpiredTime>
            <VPCId>vpc-bp1a2b3c4d5e6f7g</VPCId>
            <VswitchId>vsw-bp1a2b3c4d5e6f7g</VswitchId>
        </CompatibleConnection>
    </CompatibleConnections>
```

<!-- MongoDB 协议类型实例连接列表 `-->`

```xml
    <NetworkAddresses>
        <NetworkAddress>
            <NodeId>s-bp1x9y8z7w6v5u4t</NodeId>
            <NodeType>mongos</NodeType>
            <Role>Primary</Role>
            <NetworkAddress>s-
bp1x9y8z7w6v5u4t.mongodb.rds.aliyuncs.com</NetworkAddress>
            <IPAddress>192.168.1.100</IPAddress>
            <IPAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:1234</IPAddressV6>
            <IpVersion>ipv4v6</IpVersion>
            <Port>3717</Port>
            <NetworkType>VPC</NetworkType>
            <ExpiredTime>2591963</ExpiredTime>
            <VPCId>vpc-bp1x9y8z7w6v5u4t</VPCId>
            <VswitchId>vsw-bp1x9y8z7w6v5u4t</VswitchId>
        </NetworkAddress>
        <NetworkAddress>
            <NodeId>d-bp1shard12345678</NodeId>
            <NodeType>shard</NodeType>
            <Role>Secondary</Role>
            <NetworkAddress>d-
bp1shard12345678.mongodb.rds.aliyuncs.com</NetworkAddress>
            <IPAddress>192.168.1.101</IPAddress>
            <IPAddressV6></IPAddressV6>
            <IpVersion>ipv4</IpVersion>
            <Port>3717</Port>
            <NetworkType>Classic</NetworkType>
            <ExpiredTime>0</ExpiredTime>
        </NetworkAddress>
    </NetworkAddresses>
</DescribeDBInstanceNetInfoResponse>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
    "RequestId": "18D8AAFD-6BEB-420F-8164-810CB0C0AA39",
    "CompatibleConnections": {
        "CompatibleConnection": [
            {
                "IPAddress": "10.140.23.45",
                "NetworkAddress": "dds-bp1a2b3c4d5e6f7g.mongodb.rds.aliyuncs.com",
                "NetworkType": "VPC",
                "Port": "3717",
                "ExpiredTime": "2591963",
                "VPCId": "vpc-bp1a2b3c4d5e6f7g",
                "VswitchId": "vsw-bp1a2b3c4d5e6f7g"
            }
```

]

```json
    },
    "NetworkAddresses": {
        "NetworkAddress": [
            {
                "NodeId": "s-bp1x9y8z7w6v5u4t",
                "NodeType": "mongos",
                "Role": "Primary",
                "NetworkAddress": "s-bp1x9y8z7w6v5u4t.mongodb.rds.aliyuncs.com",
                "IPAddress": "192.168.1.100",
                "IPAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:1234",
                "IpVersion": "ipv4v6",
                "Port": "3717",
                "NetworkType": "VPC",
                "ExpiredTime": "2591963",
                "VPCId": "vpc-bp1x9y8z7w6v5u4t",
                "VswitchId": "vsw-bp1x9y8z7w6v5u4t"
            },
            {
                "NodeId": "d-bp1shard12345678",
                "NodeType": "shard",
                "Role": "Secondary",
                "NetworkAddress": "d-bp1shard12345678.mongodb.rds.aliyuncs.com",
                "IPAddress": "192.168.1.101",
                "IPAddressV6": "",
                "IpVersion": "ipv4",
                "Port": "3717",
                "NetworkType": "Classic",
                "ExpiredTime": "0"
            }
```

]

```
    }
}
```

#### ModifyDBInstanceConnectionString

调用ModifyDBInstanceConnectionString接口修改MongoDB实例的连接地址。

**请求参数**

云数据库 MongoDB 版

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eConnectionStri ng | 要执行的操作，取值： ModifyDBInstanceConnectionStri ng。 |
| CurrentConnecti onString | String | 是 | s- bpxxxxxxxx.mon godb.rds.aliyunc s.com | 当前连接地址，即待修改的连接地址。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NewConnectionS tring | String | 是 | aliyuntest111 | 新的连接地址，以小写字母开头，由字母、数字组成，长度为8~64个字符。 说明仅需传入连接地址的前缀部分，前缀以外的部分不可修改。 |
| NodeId | String | 否 | s-bpxxxxxxxx | 分片集群实例中的Mongos节点ID，每次调用仅能传入一个Mongos节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FF36A84C-0694- 42D0-861D- C383E8E4FAAF | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceConnectionString &CurrentConnectionString=s-bpxxxxxxxx.mongodb.rds.aliyuncs.com &NewConnectionString=aliyuntest111 &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<ModifyDBInstanceConnectionStringResponse>
   <RequestId>FF36A84C-0694-42D0-861D-C383E8E4FAAF</RequestId>
</ModifyDBInstanceConnectionStringResponse>
```

`JSON` 格式

```json
{
 "RequestId": "FF36A84C-0694-42D0-861D-C383E8E4FAAF"
}
```

#### ReleasePrivateNetworkAddress

调用ReleasePrivateNetworkAddress接口释放MongoDB副本集实例的IPv6私有网络地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | 是 | dds-bpxxxxxxxx | 实例ID。 |
| NodeId | Strin g | Quer y | 否 | s-bpxxxxxxxx | 副本集实例ID。 |
| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv6 | IP类型，取值：IPv6。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ReleasePrivateNetworkAddress &DBInstanceId=dds-bpxxxxxxxx
```

&公共请求参数云数据库 MongoDB 版正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F8CA8312-530A-413A-9129-F2BB32A8D404"
}
```

`XML` 格式

```xml
<RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
```

#### ReleaseNodePrivateNetworkAddress

调用 ReleaseNodePrivateNetworkAddress 接口，释放云数据库 MongoDB 分片集群实例中 Shard、 ConfigServer 节点的内网地址，或仅释放 Mongos 节点的 IPv6 内网地址。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DBInstanc eId | Strin g | Quer y | 是 | dds-bp1a7009eb24**** | 分片集群实例ID。 |
| NodeId | Strin g | Quer y | 是 | d-bp128a003436**** | 节点ID。 Shard节点 ConfigServer节点。 Mongos节点。 |
| NetworkTy pe | Strin g | Quer y | 是 | VPC | 节点内网连接地址所属的网络类型，取值说明： VPC：专有网络。 Classic：经典网络。 |
| IPVersionS electedTyp e | Strin g | Quer y | 否 | IPv4 | IP类型，默认值IPv4。取值范围： IPv4 IPv6 IPv4v6 分片集的mongos私网仅支持 IPv6。 |

云数据库 MongoDB 版

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 0FDDC511-7252- 4A4A-ADDA- 5CB1BF63873D | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ReleaseNodePrivateNetworkAddress &DBInstanceId=dds-bp1a7009eb24**** &NodeId=d-bp128a003436****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
    "RequestId":"0FDDC511-7252-4A4A-ADDA-5CB1BF63873D"
}
```

`XML` 格式

```xml
<ReleaseNodePrivateNetworkAddressResponse>
      <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
</ReleaseNodePrivateNetworkAddressResponse>
```

### 查询实例信息

#### DescribeReplicaSetRole

调用DescribeReplicaSetRole接口查询MongoDB实例中的角色信息及连接信息。 本接口适用于副本集实例，不适用于分片集群实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeReplica SetRole | 要执行的操作，取值：DescribeReplicaSetRole。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | DB4A0595-FCA9- 437F-B2BB- 25DBFC009D3E | 请求ID。 |
| DBInstanceId | String | dds-bpxxxxxxxx | 实例ID。 |
| ReplicaSets | Array of ReplicaSet |  | 副本集角色信息列表。 |
| ReplicaSet |  |  |  |
| ConnectionDo main | String | dds- bpxxxxxxxx.mongo db.rds.aliyuncs.co m | 节点的连接地址。 |
| ConnectionPor t | String | 3717 | 节点的连接端口。 |
| ExpiredTime | String | 1209582 | 保留的经典网络地址剩余时长，单位为秒。 |
| NetworkType | String | VPC | 网络类型。 VPC：专有网络。 Classic：经典网络。 Public：公网。 |
| ReplicaSetRole | String | Primary | 该节点在副本集中的角色。 Primary：主节点。 Secondary：从节点。 |
| RoleId | String | 651xxxxx | 节点的角色ID。 |
| NodeType | String | mongos | 节点类型。 mongos：mongos节点。 shard：shard节点。 configserver：configserver节点。 |

云数据库 MongoDB 版

| IpVersion | String | ipv4 | IP类型，取值范围： ipv4 ipv4v6 |
|---|---|---|---|
| IpAddress | String | 192.168.1.xxx | IPv4地址。 |
| IpAddressV6 | String | 2001:0db8:85a3:0 000:0000:8a2e:03 70:xxxx | IPv6地址。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeReplicaSetRole &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
    <RequestId>7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD</RequestId>
    <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId>
    <ReplicaSets>
        <ReplicaSet>
            <NetworkType>Classic</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Primary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <ExpiredTime>12xxxxx</ExpiredTime>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4</IpVersion>
            <IpAddress>192.168.1.105</IpAddress>
            <IpAddressV6></IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>Classic</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Secondary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <ExpiredTime>12xxxxx</ExpiredTime>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4</IpVersion>
            <IpAddress>192.168.1.106</IpAddress>
            <IpAddressV6></IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>VPC</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Primary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4v6</IpVersion>
            <IpAddress>10.0.0.50</IpAddress>
            <IpAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:7334</IpAddressV6>
        </ReplicaSet>
        <ReplicaSet>
            <NetworkType>VPC</NetworkType>
            <ConnectionPort>3717</ConnectionPort>
            <ReplicaSetRole>Secondary</ReplicaSetRole>
            <ConnectionDomain>dds-
bpxxxxxxxx.mongodb.rds.aliyuncs.com</ConnectionDomain>
            <RoleId>55xxxxx</RoleId>
            <IpVersion>ipv4v6</IpVersion>
            <IpAddress>10.0.0.51</IpAddress>
            <IpAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:7335</IpAddressV6>
        </ReplicaSet>
    </ReplicaSets>
```

云数据库 MongoDB 版 `JSON` 格式

```json
{
    "RequestId": "7762D0FF-F34D-4DAF-9D06-6C1C28CC98CD",
    "DBInstanceId": "dds-bpxxxxxxxx",
    "ReplicaSets": {
        "ReplicaSet": [
            {
                "NetworkType": "Classic",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Primary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "ExpiredTime": "12xxxxx",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4",
                "IpAddress": "192.168.1.105",
                "IpAddressV6": ""
            },
            {
                "NetworkType": "Classic",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Secondary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "ExpiredTime": "12xxxxx",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4",
                "IpAddress": "192.168.1.106",
                "IpAddressV6": ""
            },
            {
                "NetworkType": "VPC",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Primary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4v6",
                "IpAddress": "10.0.0.50",
                "IpAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
            },
            {
                "NetworkType": "VPC",
                "ConnectionPort": "3717",
                "ReplicaSetRole": "Secondary",
                "ConnectionDomain": "dds-bpxxxxxxxx.mongodb.rds.aliyuncs.com",
                "RoleId": "55xxxxx",
                "IpVersion": "ipv4v6",
                "IpAddress": "10.0.0.51",
                "IpAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:7335"
            }
```

]

```
    }
}
```

云数据库 MongoDB 版

#### DescribeKernelReleaseNotes

调用DescribeKernelReleaseNotes接口查询MongoDB实例的小版本发布日志。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeKernelR eleaseNotes | 要执行的操作，取值： DescribeKernelReleaseNotes。 |
| KernelVersion | String | 否 | mongodb 20180 _ 522 0.4.8 _ | 数据库小版本号，例如：mongodb 20180522 0.4.8。 _ _ 如果传入该参数，返回大于该版本的版本号列表。 如果不传入该参数，返回所有版本号列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ReleaseNotes | Array of ReleaseNote |  | 版本发布日志信息列表。 |
| ReleaseNote |  |  |  |
| KernelVersion | String | mongodb 2018061 _ 9 0.4.9 _ | 版本号。 |
| ReleaseNote | String | 放开sharding某集合开关balancer的限制 | 发布日志。 |
| RequestId | String | F01D4DDA-CB72- 4083-B399- AF4642294FE6 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeKernelReleaseNotes
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<RequestId>F01D4DDA-CB72-4083-B399-AF4642294FE6</RequestId> <ReleaseNotes>
    <ReleaseNote>
        <KernelVersion>mongodb_20180619_0.4.9</KernelVersion>
```

`<ReleaseNote>`放开`sharding`某集合开关`balancer`的限制`</ReleaseNote>`

```
    </ReleaseNote>
</ReleaseNotes>
```

`JSON` 格式

```json
{
    "RequestId":"F01D4DDA-CB72-4083-B399-AF4642294FE6",
    "ReleaseNotes":
    {
        "ReleaseNote":[
            {
                "KernelVersion":"mongodb_20180619_0.4.9",
```

`"ReleaseNote":"`放开`sharding`某集合开关`balancer`的限制"

```
            }
```

]

```
    }
}
```

#### DescribeAvailableEngineVersion

调用DescribeAvailableEngineVersion接口查询MongoDB实例可升级的版本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAvailabl eEngineVersion | 要执行的操作，取值：DescribeAvailableEngineVersi on。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 52507B6B-003B- 47A3-A0A3- 9FE992C7A243 | 请求ID。 |
| EngineVersion s | List | {"EngineVersion": ["4.0" ]} | 可升级的版本。 说明如果当前已经是最新版本，则本参数返回为空。 |

云数据库 MongoDB 版

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeAvailableEngineVersion &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <EngineVersions>
      <EngineVersion>4.0</EngineVersion>
   </EngineVersions>
   <RequestId>52507B6B-003B-47A3-A0A3-9FE992C7A243</RequestId>
```

`JSON` 格式

```json
{
 "EngineVersions": {
  "EngineVersion": [
   "4.0"
```

]

```json
 },
 "RequestId": "52507B6B-003B-47A3-A0A3-9FE992C7A243"
}
```

#### DescribeDBInstances

调用DescribeDBInstances接口时，您需要在调用代码的Header中设置 `x-acs-organizationid` 、 `x-` `acs-resourcegroupid` 、 `x-acs-instanceid` 等参数，用于指定资源所属的组织、资源集以及资源实例 ID，否则调用接口时会指向根组织和根资源集。具体调用代码请参见云数据库MongoDB产品简介中的SDK 说明。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nces | 要执行的操作，取值：DescribeDBInstances。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值为 30、50或100，默认值为30。 |

云数据库 MongoDB 版

| DBInstanceId | String | 否 | dds- d1n4eab47879* *** | 实例ID。 |
|---|---|---|---|---|
| ReplicationFacto r | String | 否 | 3 | 副本集实例的节点数量，取值为3、5或 7。 |
| DBInstanceDesc ription | String | 否 | test | 实例的描述或备注信息。 |
| ExpireTime | String | 否 | 2019-12- 26T16:00Z | 实例的到期时间。 |
| DBInstanceStatu s | String | 否 | ACTIVATION | 实例的状态信息，请参见云数据库 MongoDB开发指南中的实例状态表。 |
| DBInstanceType | String | 否 | replicate | 实例类型，取值如下： sharding：分片集群实例。 replicate：副本集实例或单节点实例。 默认值为replicate。 |
| DBInstanceClass | String | 否 | dds.mongo.mid | 实例规格。 说明规格信息请参见云数据库MongoDB产品简介中的实例规格表。 |
| Engine | String | 否 | MongoDB | 数据库引擎，取值为MongoDB。 |
| EngineVersion | String | 否 | 4.2 | 实例的数据库版本。取值为 3.0、 3.4、4.0或 4.2。 |
| NetworkType | String | 否 | Classic | 实例的网络类型，取值如下： Classic：经典网络。 VPC：VPC网络。 固定为Classic。 |
| VpcId | String | 否 | vpc- bp1q2qqm4vxo 6e6zl**** | 专有网络ID。 |
| VSwitchId | String | 否 | vsw- bp1buy0h9myt5 i9e7**** | 专有网络的交换机ID。 |

云数据库 MongoDB 版

| ChargeType | String | 否 | PostPaid | 实例的付费类型，取值如下： PrePaid：预付费，包年包月。 PostPaid：按量付费。 |
|---|---|---|---|---|
| ZoneId | String | 否 | cn-qd-agility14- amtest110**** | 可用区ID。 说明您可以通过DescribeRegions接口查询可用的可用区。 |
| Expired | String | 否 | true | 实例过期状态，取值如下： true：已过期。 false：未过期。 |
| ResourceGroupI d | String | 否 | rg- acfm22cdcgc*** * | 资源组ID。 |
| Tag.N.Key | String | 否 | testdatabase | 实例的标签键。 说明 N的取值范围为1~20，最多支持64个字符。 不能以 aliyun 、 acs: 、 http:// 或者 https:// 开头。 不允许传入空字符串。 |
| Tag.N.Value | String | 否 | apitest | 实例的标签值。 说明 N的取值范围：1~20，最多支持128个字符。 不能以 aliyun 、 acs: 、 http:// 或者 https:// 开头。 可以为空。 |

|  | aliyun |
|---|---|
| http:// |  |

|  | aliyun |
|---|---|
| http:// |  |

云数据库 MongoDB 版

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstances | Array of DBInstance |  | 实例信息列表。 |
| DBInstance |  |  |  |
| ChargeType | String | PostPaid | 实例付费类型。 PrePaid：预付费，包年包月。 PostPaid：按量付费。 |
| CreationTime | String | 2021-05- 31T12:00:52Z | 实例创建的时间，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| DBInstanceCla ss | String | dds.mongo.mid | 实例规格。 说明规格信息请参见云数据库 MongoDB产品简介中的实例规格表。 |
| DBInstanceDe scription | String | 测试数据库 | 实例的描述或备注信息。 |
| DBInstanceId | String | dds- d1n4eab47879**** | 实例ID。 |
| DBInstanceSta tus | String | Running | 实例的状态。 |
| DBInstanceSto rage | Integer | 50 | 实例的存储空间。 |
| DBInstanceTy pe | String | replicate | 实例的类型。取值： sharding：分片集群实例。 replicate：副本集实例。 |
| DestroyTime | String | 2021-12- 31T16:00:00Z | 实例数据销毁时间，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 说明包年包月实例，到期7天后会被释放，数据也会被删除且无法恢复。 按量付费实例，欠费超过24小时会被锁定，持续欠费7天会被释放， 数据也被删除且无法恢复。 |
| Engine | String | MongoDB | 数据库引擎。 |

云数据库 MongoDB 版

| EngineVersion | String | 3.0 | 数据库版本。 |
|---|---|---|---|
| ExpireTime | String | 2019-11- 25T16:00Z | 实例到期时间，格式为yyyy-MM-ddTHH:mm:ssZ（UTC时间）。 |
| KindCode | String | 1 | 表示实例的类型。取值： 0：物理机 1：ECS 2：DOCKER 18：k8s新架构实例 |
| LastDowngrad eTime | String | 20210708 | 实例最后一次降配时间。 |
| LockMode | String | unlock | 实例的锁定状态。 Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前自动锁定。 LockByDiskQuota：实例空间满自动锁定。 Released：实例已释放。此时实例无法进行解锁，只能使用备份数据重新创建新实例，重建时间较长，请耐心等待。 |
| MongosList | Array of MongosAttribu te |  | Mongos节点信息列表。 说明实例类型为分片集群实例时返回该参数。 |
| MongosAttribu te |  |  |  |
| NodeClass | String | dds.mongos.mid | Mongos节点规格。 |
| NodeDescripti on | String | 测试Mongos节点 | Mongos节点描述。 |
| NodeId | String | s- d1n849c1788f**** | Mongos节点ID。 |
| NetworkType | String | Classic | 实例的网络类型，固定为经典网络 （Classic）。 |
| RegionId | String | cn-qd-agility14**** | 实例所属地域ID。 |

云数据库 MongoDB 版

| ReplicationFac tor | String | 3 | 实例中节点的个数。 说明实例类型为副本集实例时返回该参数。 |
|---|---|---|---|
| ResourceGrou pId | String | rg- acfm22cdcgc**** | 资源组ID。 |
| ShardList | Array of ShardAttribute |  | Shard节点信息列表。 说明实例类型为分片集群实例时返回该参数。 |
| ShardAttribute |  |  |  |
| NodeClass | String | dds.shard.mid | Shard节点的实例规格。 |
| NodeDescripti on | String | 测试Shard节点 | Shard节点描述。 |
| NodeId | String | d- d1n753c91603**** | Shard节点ID。 |
| NodeStorage | Integer | 20 | Shard节点的存储空间，单位为GB。 |
| Tags | Array of Tag |  | 资源标签信息列表。 |
| Tag |  |  |  |
| Key | String | test | 资源的标签键。 |
| Value | String | api | 资源的标签值。 |
| VpcAuthMode | String | Close | 是否开启了专有网络免密访问功能，返回值： Open：开启 Close：关闭 |
| ZoneId | String | cn-qd-agility14- amtest110**** | 实例所属可用区ID。 |
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 30 | 每页记录数。 |
| RequestId | String | A10B8ECB-0BA0- 4EC6-93A5- C65FDEDA**** | 请求ID。 |

云数据库 MongoDB 版

| TotalCount | Integer | 1 | 查询结果中实例的数量。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstances
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
  <TotalCount>1</TotalCount>
  <PageSize>30</PageSize>
  <RequestId>A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****</RequestId>
  <PageNumber>1</PageNumber>
  <DBInstances>
        <EngineVersion>3.0</EngineVersion>
        <ReplicationFactor>3</ReplicationFactor>
        <DBInstanceStatus>Running</DBInstanceStatus>
        <ZoneId>cn-qd-agility14-amtest110****</ZoneId>
        <ResourceGroupId>rg-acfm22cdcgc****</ResourceGroupId>
        <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
        <DestroyTime>2021-12-31T16:00:00Z</DestroyTime>
        <DBInstanceType>replicate</DBInstanceType>
        <LockMode>unlock</LockMode>
        <DBInstanceId>dds-d1n4eab47879****</DBInstanceId>
        <VpcAuthMode>Close</VpcAuthMode>
        <NetworkType>Classic</NetworkType>
        <ChargeType>PostPaid</ChargeType>
        <LastDowngradeTime>20210708</LastDowngradeTime>
        <DBInstanceStorage>50</DBInstanceStorage>
        <CreationTime>2021-05-31T12:00:52Z</CreationTime>
        <RegionId>cn-qd-agility14****</RegionId>
        <ExpireTime>2019-11-25T16:00Z</ExpireTime>
        <KindCode>1</KindCode>
        <Engine>MongoDB</Engine>
        <DBInstanceDescription>测试数据库</DBInstanceDescription>
        <ShardList>
              <NodeClass>dds.shard.mid</NodeClass>
              <NodeDescription>测试Shard节点</NodeDescription>
              <NodeStorage>20</NodeStorage>
              <NodeId>d-d1n753c91603****</NodeId>
        </ShardList>
        <MongosList>
              <NodeClass>dds.mongos.mid</NodeClass>
              <NodeDescription>测试Mongos节点</NodeDescription>
              <NodeId>s-d1n849c1788f****</NodeId>
        </MongosList>
        <Tags>
              <Value>api</Value>
              <Key>test</Key>
        </Tags>
  </DBInstances>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
  "TotalCount": "1",
  "PageSize": "30",
  "RequestId": "A10B8ECB-0BA0-4EC6-93A5-C65FDEDA****",
  "PageNumber": "1",
  "DBInstances": [
    {
      "EngineVersion": "3.0",
      "ReplicationFactor": "3",
      "DBInstanceStatus": "Running",
      "ZoneId": "cn-qd-agility14-amtest110****",
      "ResourceGroupId": "rg-acfm22cdcgc****",
      "DBInstanceClass": "dds.mongo.mid",
      "DestroyTime": "2021-12-31T16:00:00Z",
      "DBInstanceType": "replicate",
      "LockMode": "unlock",
      "DBInstanceId": "dds-d1n4eab47879****",
      "VpcAuthMode": "Close",
      "NetworkType": "Classic",
      "ChargeType": "PostPaid",
      "LastDowngradeTime": "20210708",
      "DBInstanceStorage": "50",
      "CreationTime": "2021-05-31T12:00:52Z",
      "RegionId": "cn-qd-agility14****",
      "ExpireTime": "2019-11-25T16:00Z",
      "KindCode": "1",
      "Engine": "MongoDB",
```

`"DBInstanceDescription": "`测试数据库`",`

```json
      "ShardList": [
        {
          "NodeClass": "dds.shard.mid",
          "NodeDescription": "测试Shard节点",
          "NodeStorage": "20",
          "NodeId": "d-d1n753c91603****"
        }
```

`],`

```json
      "MongosList": [
        {
          "NodeClass": "dds.mongos.mid",
          "NodeDescription": "测试Mongos节点",
          "NodeId": "s-d1n849c1788f****"
        }
```

`],`

```json
      "Tags": [
        {
          "Value": "api",
          "Key": "test"
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

云数据库 MongoDB 版

#### DescribeDBInstanceAttribute

调用DescribeDBInstanceAttribute接口查询云数据库MongoDB的实例信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceAttribute | 系统规定参数，取值：DescribeDBInstanceAttribute 。 |
| DBInstanceId | String | 是 | dds- bp11483712c1* *** | 实例ID。 |
| Engine | String | 否 | MongoDB | 数据库引擎，取值固定为MongoDB。 |
| ResourceGroupI d | String | 否 | rg- acfmyiu4ekp**** | 资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C373EED9-5125- 4DD9-89DB- FB1ECD2C2B4F | 请求ID。 |
| DBInstances | Array of DBInstan ce |  | 实例信息列表。 |
| DBInstance |  |  |  |
| CpuType | String | intel | CPU类型。 |
| ChargeType | String | PostPaid | 实例的付费类型，取值说明： PostPaid：后付费，按量付费。 |

云数据库 MongoDB 版

| Configserver List | Array of Configser verAttrib ute |  | Configserver节点信息列表。 说明当实例类型为分片集群实例时，返回该参数。 |
|---|---|---|---|
| Configserver Attribute |  |  |  |
| ConnectStri ng | String | mongodb://root:** **@dds- bp11483712c1*** *-cs1730- pub.mongodb.rds .aliyuncs.com:371 7 | Configserver节点的连接地址。 |
| MaxConnect ions | Integer | 8000 | Configserver节点的最大连接数。 |
| MaxIOPS | Integer | 8000 | Configserver节点的最大IOPS。 |
| NodeClass | String | dds.cs.mid | Configserver节点的规格。 |
| NodeDescrip tion | String | testConfigserver | Configserver节点的名称。 |
| NodeId | String | dds- bp11483712c1*** *-cs | Configserver节点的ID。 |
| NodeStorag e | Integer | 20 | Configserver节点的存储空间，单位：GB。 |
| Port | Integer | 3717 | Configserver节点的端口。 |
| CreationTim e | String | 2022-08- 21T05:10:00Z | 实例创建的时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| CurrentKern elVersion | String | mongodb 201809 _ 14 1.1.5 _ | 实例当前数据库的内核版本号。 |
| DBInstanceC lass | String | dds.mongo.mid | 实例的规格。 |

云数据库 MongoDB 版

| DBInstance Description | String | ceshi | 实例名称。 |
|---|---|---|---|
| DBInstanceI d | String | dds- bp11483712c1*** * | 实例ID。 |
| DBInstanceR eleaseProtec tion | Boolean | false | 是否开启了实例释放保护，取值说明： true：已开启。 false：（默认值）未开启。 |
| DBInstanceS tatus | String | Running | 实例状态，取值说明： Creating：创建中。 Running：运行中。 DBInstanceClassChanging：升降级中。 DBInstanceNetTypeChanging：内外网切换中。 Deleting：删除中。 EngineVersionUpgrading：迁移版本中。 GuardSwitching：容灾切换中。 HASwitching：主备切换中。 ImportingFromOthers：数据库导入中。 LinkSwitching：链路切换中。 EngineVersionUpgrading：大版本升级中。 MinorVersionUpgrading：小版本升级中。 NET CREATING：创建网络连接中。 _ NET DELETING：删除网络连接中。 _ NodeCreating：实例节点创建中。 NodeDeleting：实例节点删除中。 Rebooting：重启中。 Restoring：备份恢复中。 SSLModifying：SSL变更中。 TempDBInstanceCreating：临时实例创建中。 Transing：实例迁移中。 TransingToOthers：数据库迁移中。 |
| DBInstanceS torage | Integer | 10 | 实例的存储空间，单位：GB。 |
| DBInstanceT ype | String | replicate | 实例类型，取值说明： replicate：副本集实例。 sharding：分片集群实例。 |

云数据库 MongoDB 版

| Engine | String | MongoDB | 数据库引擎。 |
|---|---|---|---|
| EngineVersi on | String | 3.4 | 数据库版本，取值： 4.2 4.0 3.4 3.0 说明仅副本集实例支持3.0版本。 |
| ExpireTime | String | 无 | 不涉及。 |
| KindCode | String | 0 | 实例的规格类型，取值说明： 0：物理机。 |
| LastDowngr adeTime | String | 2022-08-28 | 实例最近一次的降配时间，格式为yyyy-MM-dd（UTC时间）。 |
| LockMode | String | Unlock | 实例的锁定状态，取值说明： Unlock：正常，没有被锁定。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前自动锁定。 LockByDiskQuota：实例空间满自动锁定。 Released：实例已释放。此时实例无法进行解锁，只能使用备份数据重新创建新实例，重建时间较长，请耐心等待。 |
| MaintainEnd Time | String | 03:00Z | 实例可维护时间段的结束时间，格式为HH:mmZ（UTC时间）。 |
| MaintainStar tTime | String | 02:00Z | 实例可维护时间段的开始时间，格式为HH:mmZ（UTC时间）。 |
| MaxConnect ions | Integer | 500 | 实例的最大连接数。 |
| MaxIOPS | Integer | 1000 | 实例的最大IOPS。 |

云数据库 MongoDB 版

| MongosList | Array of MongosAt tribute |  | Mongos节点信息列表。 说明当实例类型为分片集群实例时，返回该参数。 |
|---|---|---|---|
| MongosAttri bute |  |  |  |
| ConnectStin g | String | s- bp1d8c262a158* ***.mongodb.rds. aliyuncs.com | Mongos节点的连接地址。 |
| MaxConnect ions | Integer | 1000 | Mongos节点的最大连接数。 |
| MaxIOPS | Integer | 800 | Mongos节点的最大IOPS。 |
| NodeClass | String | dds.mongos.mid | Mongos节点的规格代码。 |
| NodeDescrip tion | String | mongos1 | Mongos节点的名称。 |
| NodeId | String | s- bp1d8c262a158* *** | Mongos节点的ID。 |
| Port | Integer | 3717 | Mongos节点的连接端口。 |
| VPCId | String | vpc- bp1n3i15v90el48 nx**** | Mongos节点的专有网络ID。 |
| VSwitchId | String | vsw- bp1n3i15v90el48 nx**** | Mongos节点的交换机ID。 |
| VpcCloudIns tanceId | String | s- bp1d8c262a158* *** | Mongos节点的专有网络实例ID。 |
| NetworkTyp e | String | VPC | 实例的网络类型，取值说明： Classic：经典网络。 VPC：专有网络。 |

云数据库 MongoDB 版

| ProtocolTyp e | String | mongodb | 实例的访问协议类型，取值说明： mongodb：MongoDB协议。 |
|---|---|---|---|
| ReadonlyRe plicas | String | 0 | 实例的只读节点个数，目前不支持只读节点，取值为0。 |
| RegionId | String | cn-qingdao- env17-d01 | 实例所属地域ID。 |
| ReplacateId | String | bls-mgs**** | BLS通道ID。 |
| ReplicaSetN ame | String | test | 实例的副本集名称。 说明当实例类型为副本集实例时，返回该参数。 |
| ReplicaSets | Array of ReplicaSe t |  | 副本集实例信息。 说明当实例类型为副本集实例时，返回该参数。 |
| ReplicaSet |  |  |  |
| IPVersion | String | IPv4 | IP类型，取值范围： IPv4 IPv4v6 |
| IPAddress | String | 192.168.1.xxx | IPv4地址。 |
| IPAddressV6 | String | 2001:0db8:85a3: 0000:0000:8a2e: 0370:xxxx | IPv6地址。 |
| ConnectionD omain | String | dds- bp11483712c1*** *.mongodb.rds.ali yuncs.com | 节点的连接地址。 |
| ConnectionP ort | String | 3717 | 节点的连接端口。 |

云数据库 MongoDB 版

| NetworkTyp e | String | VPC | 节点的网络类型，取值说明： Classic：经典网络。 VPC：专有网络。 |
|---|---|---|---|
| ReplicaSetR ole | String | Primary | 节点的角色，取值说明： Primary：主节点。 Secondary：从节点。 |
| VPCCloudIns tanceId | String | vpc- bp1jk5vwkcri27q me**** | 专有网络实例ID。 |
| VPCId | String | vpc- bp1jk5vwkcri27q me**** | 专有网络ID。 |
| VSwitchId | String | vsw- bp1jk5vwkcri27q me**** | 专有网络交换机ID。 |
| ReplicationF actor | String | 3 | 实例的节点数。 |
| ResourceGro upId | String | rg-a7qme**** | 实例所属资源组ID。 |
| ShardList | Array of ShardAttr ibute |  | Shard节点信息列表。 说明当实例类型为分片集群实例时返回该参数。 |
| ShardAttribu te |  |  |  |
| ConnectStri ng | String | d- bp1af0680a9c6d 3****.mongodb.rd s.aliyuncs.com | Shard节点的连接地址。 |
| MaxConnect ions | Integer | 8000 | Shard节点的最大连接数。 |
| MaxIOPS | Integer | 8000 | Shard节点的最大IOPS。 |

云数据库 MongoDB 版

| NodeClass | String | dds.shard.mid | Shard节点的规格。 |
|---|---|---|---|
| NodeDescrip tion | String | testshard | Shard节点的名称。 |
| NodeId | String | d- bp16e09d9c5d*** * | Shard节点的ID。 |
| NodeStorag e | Integer | 10 | Shard节点的存储空间，单位：GB。 |
| Port | Integer | 3717 | Shard节点的端口。 |
| StorageEngi ne | String | WiredTiger | 实例的存储引擎类型。 |
| Tags | Array of Tag |  | 实例的标签信息列表。 |
| Tag |  |  |  |
| Key | String | test | 实例的标签键。 |
| Value | String | api | 实例的标签值。 |
| VPCId | String | vpc- bp1jk5vwkcri27q me**** | 专有网络ID。 |
| VSwitchId | String | vsw- bp1oo2a7isyrb8ig f**** | 专有网络的交换机ID。 |
| VpcAuthMod e | String | NotSupport | 内网免密访问模式，取值说明： Open：内网免密访问处于开启状态。 Close：内网免密访问处于关闭状态，需要使用密码访问。 NotSupport：不支持该功能。 |
| ZoneId | String | cn-qingdao- ft154e- amtest154001-a | 实例所属可用区ID。 |

云数据库 MongoDB 版

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceAttribute &DBInstanceId=dds-bp11483712c1****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F</RequestId>
    <DBInstances>
        <DBInstance>
```

<!-- 基础信息 `-->`

```xml
            <DBInstanceId>dds-bp11483712c1****</DBInstanceId>
            <DBInstanceDescription>ceshi</DBInstanceDescription>
            <DBInstanceClass>dds.mongo.mid</DBInstanceClass>
            <DBInstanceStorage>10</DBInstanceStorage>
            <DBInstanceType>sharding</DBInstanceType>
            <Engine>MongoDB</Engine>
            <EngineVersion>4.4</EngineVersion>
            <ChargeType>PostPaid</ChargeType>
            <DBInstanceStatus>Running</DBInstanceStatus>
            <CreationTime>2022-08-21T05:10:00Z</CreationTime>
            <ExpireTime></ExpireTime>
            <RegionId>cn-qingdao-env17-d01</RegionId>
            <ZoneId>cn-qingdao-ft154e-amtest154001-a</ZoneId>
            <NetworkType>VPC</NetworkType>
            <VPCId>vpc-bp1n3i15v90el48nx****</VPCId>
            <VSwitchId>vsw-bp1n3i15v90el48nx****</VSwitchId>
            <VPCCloudInstanceIds>s-bp1d8c262a158****</VPCCloudInstanceIds>
            <MaxConnections>500</MaxConnections>
            <MaxIOPS>1000</MaxIOPS>
            <MaintainStartTime>02:00Z</MaintainStartTime>
            <MaintainEndTime>03:00Z</MaintainEndTime>
            <LockMode>Unlock</LockMode>
            <DBInstanceReleaseProtection>false</DBInstanceReleaseProtection>
            <CurrentKernelVersion>mongodb_20180914_1.1.5</CurrentKernelVersion>
            <StorageEngine>WiredTiger</StorageEngine>
            <ProtocolType>mongodb</ProtocolType>
            <ReadonlyReplicas>0</ReadonlyReplicas>
            <ReplicationFactor>3</ReplicationFactor>
            <ResourceGroupId>rg-a7qme****</ResourceGroupId>
            <KindCode>0</KindCode>
            <LastDowngradeTime>2022-08-28</LastDowngradeTime>
            <ReplacateId>bls-mgs****</ReplacateId>
            <VpcAuthMode>Close</VpcAuthMode>
```

<!-- 新增参数 `-->`

```xml
            <CpuType>intel</CpuType>
```

<!-- 分片集群特有：`Mongos` 节点列表 `-->`

```xml
            <MongosList>
```

云数据库 MongoDB 版

```xml
                <MongosAttribute>
                    <NodeId>s-bp1d8c262a158****</NodeId>
                    <NodeDescription>mongos1</NodeDescription>
                    <NodeClass>dds.mongos.mid</NodeClass>
                    <ConnectSting>s-
bp1d8c262a158****.mongodb.rds.aliyuncs.com</ConnectSting>
                    <Port>3717</Port>
                    <MaxConnections>1000</MaxConnections>
                    <MaxIOPS>800</MaxIOPS>
                    <VPCId>vpc-bp1n3i15v90el48nx****</VPCId>
                    <VSwitchId>vsw-bp1n3i15v90el48nx****</VSwitchId>
                    <VpcCloudInstanceId>s-bp1d8c262a158****</VpcCloudInstanceId>
                </MongosAttribute>
            </MongosList>
```

<!-- 分片集群特有：`Shard` 节点列表 `-->`

```xml
            <ShardList>
                <ShardAttribute>
                    <NodeId>d-bp16e09d9c5d****</NodeId>
                    <NodeDescription>testshard</NodeDescription>
                    <NodeClass>dds.shard.mid</NodeClass>
                    <ConnectString>d-
bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com</ConnectString>
                    <Port>3717</Port>
                    <NodeStorage>10</NodeStorage>
                    <MaxConnections>8000</MaxConnections>
                    <MaxIOPS>8000</MaxIOPS>
                </ShardAttribute>
            </ShardList>
```

<!-- 分片集群特有：`ConfigServer` 节点列表 `-->`

```xml
            <ConfigserverList>
                <ConfigserverAttribute>
                    <NodeId>dds-bp11483712c1****-cs</NodeId>
                    <NodeDescription>testConfigserver</NodeDescription>
                    <NodeClass>dds.cs.mid</NodeClass>
                    <ConnectString>mongodb://root:****@dds-bp11483712c1****-cs1730-pub.m
ongodb.rds.aliyuncs.com:3717</ConnectString>
                    <Port>3717</Port>
                    <NodeStorage>20</NodeStorage>
                    <MaxConnections>8000</MaxConnections>
                    <MaxIOPS>8000</MaxIOPS>
                </ConfigserverAttribute>
            </ConfigserverList>
```

<!-- 标签列表 `-->`

```xml
            <Tags>
                <Tag>
                    <Key>test</Key>
                    <Value>api</Value>
                </Tag>
            </Tags>
        </DBInstance>
```

云数据库 MongoDB 版 <!-- 示例：副本集实例结构 (简化展示差异部分`) -->`

```xml
        <DBInstance>
            <DBInstanceId>dds-replicate-id****</DBInstanceId>
            <DBInstanceType>replicate</DBInstanceType>
            <ReplicaSetName>test</ReplicaSetName>
            <CpuType>intel</CpuType>
```

<!-- 副本集特有：`ReplicaSets` 列表 `-->`

```xml
            <ReplicaSets>
                <ReplicaSet>
                    <ReplicaSetRole>Primary</ReplicaSetRole>
                    <ConnectionDomain>dds-replicate-
id****.mongodb.rds.aliyuncs.com</ConnectionDomain>
                    <ConnectionPort>3717</ConnectionPort>
                    <IPAddress>192.168.1.xxx</IPAddress>
                    <IPAddressV6>2001:0db8:85a3:0000:0000:8a2e:0370:xxxx</IPAddressV6>
                    <IPVersion>IPv4v6</IPVersion>
                    <NetworkType>VPC</NetworkType>
                    <VPCId>vpc-bp1jk5vwkcri27qme****</VPCId>
                    <VSwitchId>vsw-bp1oo2a7isyrb8igf****</VSwitchId>
                    <VPCCloudInstanceId>vpc-bp1jk5vwkcri27qme****</VPCCloudInstanceId>
                </ReplicaSet>
            </ReplicaSets>
        </DBInstance>
    </DBInstances>
```

`JSON` 格式

```json
{
    "RequestId": "C373EED9-5125-4DD9-89DB-FB1ECD2C2B4F",
    "DBInstances": {
        "DBInstance": [
            {
                "DBInstanceId": "dds-bp11483712c1****",
                "DBInstanceDescription": "ceshi",
                "DBInstanceClass": "dds.mongo.mid",
                "DBInstanceStorage": 10,
                "DBInstanceType": "sharding",
                "Engine": "MongoDB",
                "EngineVersion": "4.4",
                "ChargeType": "PostPaid",
                "DBInstanceStatus": "Running",
                "CreationTime": "2022-08-21T05:10:00Z",
                "ExpireTime": "",
                "RegionId": "cn-qingdao-env17-d01",
                "ZoneId": "cn-qingdao-ft154e-amtest154001-a",
                "NetworkType": "VPC",
                "VPCId": "vpc-bp1n3i15v90el48nx****",
                "VSwitchId": "vsw-bp1n3i15v90el48nx****",
                "VPCCloudInstanceIds": "s-bp1d8c262a158****",
                "MaxConnections": 500,
                "MaxIOPS": 1000,
                "MaintainStartTime": "02:00Z",
                "MaintainEndTime": "03:00Z",
```

云数据库 MongoDB 版

```json
                "LockMode": "Unlock",
                "DBInstanceReleaseProtection": false,
                "CurrentKernelVersion": "mongodb_20180914_1.1.5",
                "StorageEngine": "WiredTiger",
                "ProtocolType": "mongodb",
                "ReadonlyReplicas": "0",
                "ReplicationFactor": "3",
                "ResourceGroupId": "rg-a7qme****",
                "KindCode": "0",
                "LastDowngradeTime": "2022-08-28",
                "ReplacateId": "bls-mgs****",
                "VpcAuthMode": "Close",
                "CpuType": "intel",
                "MongosList": {
                    "MongosAttribute": [
                        {
                            "NodeId": "s-bp1d8c262a158****",
                            "NodeDescription": "mongos1",
                            "NodeClass": "dds.mongos.mid",
                            "ConnectSting": "s-
bp1d8c262a158****.mongodb.rds.aliyuncs.com",
                            "Port": 3717,
                            "MaxConnections": 1000,
                            "MaxIOPS": 800,
                            "VPCId": "vpc-bp1n3i15v90el48nx****",
                            "VSwitchId": "vsw-bp1n3i15v90el48nx****",
                            "VpcCloudInstanceId": "s-bp1d8c262a158****"
                        }
```

]

```json
                },
                "ShardList": {
                    "ShardAttribute": [
                        {
                            "NodeId": "d-bp16e09d9c5d****",
                            "NodeDescription": "testshard",
                            "NodeClass": "dds.shard.mid",
                            "ConnectString": "d-
bp1af0680a9c6d3****.mongodb.rds.aliyuncs.com",
                            "Port": 3717,
                            "NodeStorage": 10,
                            "MaxConnections": 8000,
                            "MaxIOPS": 8000
                        }
```

]

```json
                },
                "ConfigserverList": {
                    "ConfigserverAttribute": [
                        {
                            "NodeId": "dds-bp11483712c1****-cs",
                            "NodeDescription": "testConfigserver",
                            "NodeClass": "dds.cs.mid",
                            "ConnectString": "mongodb://root:****@dds-bp11483712c1****-c
s1730-pub.mongodb.rds.aliyuncs.com:3717",
                            "Port": 3717,
```

云数据库 MongoDB 版

```json
                            "NodeStorage": 20,
                            "MaxConnections": 8000,
                            "MaxIOPS": 8000
                        }
```

]

```json
                },
                "Tags": {
                    "Tag": [
                        {
                            "Key": "test",
                            "Value": "api"
                        }
```

]

```json
                }
            },
            {
                "DBInstanceId": "dds-replicate-id****",
                "DBInstanceType": "replicate",
                "ReplicaSetName": "test",
                "CpuType": "intel",
                "ReplicaSets": {
                    "ReplicaSet": [
                        {
                            "ReplicaSetRole": "Primary",
                            "ConnectionDomain": "dds-replicate-
id****.mongodb.rds.aliyuncs.com",
                            "ConnectionPort": "3717",
                            "IPAddress": "192.168.1.xxx",
                            "IPAddressV6": "2001:0db8:85a3:0000:0000:8a2e:0370:xxxx",
                            "IPVersion": "IPv4v6",
                            "NetworkType": "VPC",
                            "VPCId": "vpc-bp1jk5vwkcri27qme****",
                            "VSwitchId": "vsw-bp1oo2a7isyrb8igf****",
                            "VPCCloudInstanceId": "vpc-bp1jk5vwkcri27qme****"
                        }
```

]

```
                }
            }
```

]

```
    }
}
```

#### DescribeRoleZoneInfo

调用DescribeRoleZoneInfo接口查询MongoDB实例的各节点的角色和所属的可用区

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | DescribeRoleZo neInfo | 要执行的操作，取值：DescribeRoleZoneInfo。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 728B9A96-E262- 4AE5-915E- 3A51CCE2FDA9 | 请求ID。 |
| ZoneInfos | Array of ZoneInfo |  | 节点在可用区中的分布信息列表。 |
| ZoneInfo |  |  |  |
| InsName | String | dds-bpxxxxxxxx | 节点ID。 |
| NodeType | String | normal | 节点类型，返回值为： normal：普通节点。 configServer：配置服务器节点。 shard：Shard节点。 mongos：Mongos节点。 说明当实例类型为副本集实例时， 返回值为normal；当实例类型为分片集群实例时，返回值中包含configServer、shard和mongos。 |
| RoleId | String | 83xxxxx | 角色ID。 |
| RoleType | String | Primary | 节点的角色，返回值为： Primary：主节点。 Secondary：从节点。 Hidden：隐藏节点。 |
| ZoneId | String | cn-hangzhou-e | 可用区ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeRoleZoneInfo &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 云数据库 MongoDB 版正常返回示例 `XML` 格式

```xml
   <ZoneInfos>
      <ZoneInfo>
         <RoleType>Primary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-e</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Secondary</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-f</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
      <ZoneInfo>
         <RoleType>Hidden</RoleType>
         <NodeType>normal</NodeType>
         <InsName>dds-bpxxxxxxxx</InsName>
         <ZoneId>cn-hangzhou-b</ZoneId>
         <RoleId>83xxxxx</RoleId>
      </ZoneInfo>
   </ZoneInfos>
   <RequestId>728B9A96-E262-4AE5-915E-3A51CCE2FDA9</RequestId>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
 "ZoneInfos": {
  "ZoneInfo": [
   {
    "RoleType": "Primary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-e",
    "RoleId": "83xxxxx"
   },
   {
    "RoleType": "Secondary",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-f",
    "RoleId": "83xxxxx"
   },
   {
    "RoleType": "Hidden",
    "NodeType": "normal",
    "InsName": "dds-bpxxxxxxxx",
    "ZoneId": "cn-hangzhou-b",
    "RoleId": "83xxxxx"
   }
```

]

```json
 },
 "RequestId": "728B9A96-E262-4AE5-915E-3A51CCE2FDA9"
}
```

### 实例管理

#### RestartDBInstance

调用本接口可用于重启实例，也可用于重启分片集群实例中的某个Shard节点或Mongos节点。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RestartDBInstan ce | 要执行的操作，取值：RestartDBInstance。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Shard节点ID或Mongos 节点ID。 说明当实例类型为分片集群实例时，如不传入本参数，则重启分片集群实例。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 149C517D-B586- 47BE-A107- 8673E0ED77C6 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=RestartDBInstance &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>149C517D-B586-47BE-A107-8673E0ED77C6</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "149C517D-B586-47BE-A107-8673E0ED77C6"
}
```

#### ModifyDBInstanceMaintainTime

调用ModifyDBInstanceMaintainTime接口修改MongoDB实例的可维护时间。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eMaintainTime | 要执行的操作，取值：ModifyDBInstanceMaintainTi me。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| MaintainEndTim e | String | 是 | 02:00Z | 实例可运维时间段的结束时间，格式为HH:mmZ（UTC时间）。 说明开始时间至结束时间的范围须为1小时，例如MaintainStartTime为01:00Z ，则MaintainEndTime必须为02:00Z。 |
|---|---|---|---|---|
| MaintainStartTi me | String | 是 | 01:00Z | 实例可运维时间段的开始时间，格式为HH:mmZ（UTC时间）。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A9310426-C763- 42A2-A3AD- 70A8DA204531 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceMaintainTime &MaintainStartTime=01:00Z &MaintainEndTime=02:00Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>A9310426-C763-42A2-A3AD-70A8DA204531</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "A9310426-C763-42A2-A3AD-70A8DA204531"
}
```

#### ModifyDBInstanceDescription

调用ModifyDBInstanceDescription接口修改MongoDB实例名称。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | ModifyDBInstanc eDescription | 要执行的操作，取值：ModifyDBInstanceDescription 。 |
|---|---|---|---|---|
| DBInstanceDesc ription | String | 是 | testdata | 实例名称。 说明不能 http:// 或者 https:// 开头。 以中文、英文字母开头。 可以包含中文、英文字符、 下划线（ ）、连接号（-） _ 和数字，字符长度2~256个字符。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明如需修改分片集群实例中的Shard节点或Mongos节点的名称，还需要传入NodeId参数。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Shard节点ID或Mongos 节点ID。 说明当DBInstanceId传入的是分片集群实例ID时，本参数才可用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 06F8F642-4009- 4FFC-80C4- 9D67DBF7B74E | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceDescription &DBInstanceDescription=testdata &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <RequestId>06F8F642-4009-4FFC-80C4-9D67DBF7B74E</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "06F8F642-4009-4FFC-80C4-9D67DBF7B74E"
}
```

#### SwitchDBInstanceHA

调用本接口时，实例状态要求为运行中。 副本集实例以实例单位进行切换，分片集群实例以Shard为单位进行切换。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SwitchDBInstanc eHA | 要执行的操作，取值：SwitchDBInstanceHA。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Shard节点的ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数必须传入。 |
| RoleIds | String | 否 | 972xxxx,972xxx x | 需要执行切换的角色ID。您可以调用DescribeRoleZoneInfo接口获取角色ID和节点角色信息。 说明角色ID以英文逗号（,）分隔，不传入本参数则切换主备节点。 当DBInstanceId参数传入的是分片集群实例ID时，执行切换的角色必须属于同一 Shard节点中。 |

云数据库 MongoDB 版

| SwitchMode | Integer | 否 | 0 | 切换主备节点的时间点。取值： 0：立即切换。 1：在可运维时间段内切换。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 26BD4E5F-BDB4- 47BA-B232- 413AA78CFA8F | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=SwitchDBInstanceHA &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>26BD4E5F-BDB4-47BA-B232-413AA78CFA8F</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "26BD4E5F-BDB4-47BA-B232-413AA78CFA8F"
}
```

#### UpgradeDBInstanceEngineVersion

调用UpgradeDBInstanceEngineVersion接口升级MongoDB实例的数据库版本。 调用本接口时，要求实例状态为运行中。

**说明**

实例的存储引擎对数据库版本的选择有约束性，您可以调用**DescribeAvailableEngineVersion**接口查询实例可升级的版本。 升级数据库版本后不支持降级数据库版本。 升级过程中会自动对实例进行2~3次重启，请确保在业务低峰执行。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | UpgradeDBInsta nceEngineVersio n | 要执行的操作，取值：UpgradeDBInstanceEngineVe rsion。 |
|---|---|---|---|---|
| EngineVersion | String | 是 | 4.2 | 升级的目标数据库版本，取值：3.4、4.0、4.2。 说明升级的目标数据库版本必须大于实例当前的数据库版本。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C4907B00-A208- 4E0C-A636- AA85140E406C | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=UpgradeDBInstanceEngineVersion &EngineVersion=4.0 &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>C4907B00-A208-4E0C-A636-AA85140E406C</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "C4907B00-A208-4E0C-A636-AA85140E406C"
}
```

#### UpgradeDBInstanceKernelVersion

调用UpgradeDBInstanceKernelVersion接口升级MongoDB实例的数据库小版本。 调用本接口时，要求实例状态为运行中。 升级过程中，实例会被重启一次，请在业务低峰期执行该操作。

**说明**

云数据库 MongoDB 版

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpgradeDBInsta nceKernelVersio n | 要执行的操作，取值： UpgradeDBInstanceKernelVersio n。 |
| DBInstanceId | String | 否 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 27B9A130-7C4B- 40D9-84E8- 2FC081097AAC | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=UpgradeDBInstanceKernelVersion &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>27B9A130-7C4B-40D9-84E8-2FC081097AAC</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "27B9A130-7C4B-40D9-84E8-2FC081097AAC"
}
```

#### ModifyDBInstanceNetExpireTime

调用ModifyDBInstanceNetExpireTime接口延长MongoDB实例的经典网络保留时长。 调用该接口时实例须满足以下条件： 实例状态处于运行中。 实例的网络处于混访模式。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | ModifyDBInstanc eNetExpireTime | 要执行的操作，取值：ModifyDBInstanceNetExpireTi me。 |
|---|---|---|---|---|
| ClassicExpendEx piredDays | Integer | 是 | 30 | 设置保留原经典网络地址的时长，取值：14、30、60、120，单位为天。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| ConnectionStrin g | String | 否 | dds- bpxxxxxxxx.mon godb.rds.aliyunc s.com | 实例的连接地址。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 459E7D5C-38DA- 4E14-9C82- 5B5AF693DBAB | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceNetExpireTime &ClassicExpendExpiredDays=30 &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>459E7D5C-38DA-4E14-9C82-5B5AF693DBAB</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "459E7D5C-38DA-4E14-9C82-5B5AF693DBAB"
}
```

### 账号管理

#### DescribeAccounts

查询数据库实例的账户列表信息。 云数据库 MongoDB 版

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | DescribeAccounts | 系统规定参数，取值： DescribeAccounts。 |
| DBInstanc eId | Strin g | Query | 是 | dds-bpxxxxxxxx | 实例 ID。 |
| AccountN ame | Strin g | Query | 否 | testacc | 账号名称。 |
| Database Names | Repe atList | Query | 否 | ["db1","db2"] | 数据库名列表。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Accounts | Array | - | 账户列表。 |
| -Roles | Array | myRole1 | 角色列表。 |
| -- DatabaseNam e | String | db1 | 数据库名称。 |
| --RoleName | String | role test _ | 角色名称。 |
| -DBInstanceId | String | dds-xxxxx | 实例ID。 |
| -AccountName | String | root | 账号名称。 |
| - DatabaseNam e | String | abc | 数据库名称。 |
| - AccountStatus | String | 1 | 状态。 |
| - AccountDescri ption | String | 测试数据库账号 | 账号描述。 |
| - CharacterType | String | normal | MongoDB实例的类型。 |

| 云数据库 MongoDB | 版 |  | 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -AccountType | String | SUB | 账号类型。 |
| -AccountId | Integer | 1 | 账号ID。 |
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | 请求 ID。 |

**示例**

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F8CA8312-530A-413A-9129-F2BB32A8D404",
 "Accounts":[
  {
   "AccountDescription":"",
   "Roles":[
    {
     "RoleName":"",
     "DatabaseName":""
    }
```

`],`

```json
   "AccountStatus":"",
   "AccountId":"",
   "DBInstanceId":"",
   "DatabaseName":"",
   "CharacterType":"",
   "AccountType":"",
   "AccountName":""
  }
```

]

```
}
```

`XML` 格式云数据库 MongoDB 版

```xml
<RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId> <Accounts>
 <AccountDescription  />
 <Roles>
  <RoleName  />
  <DatabaseName  />
 </Roles>
 <AccountStatus  />
 <AccountId  />
 <DBInstanceId  />
 <DatabaseName  />
 <CharacterType  />
 <AccountType  />
 <AccountName  />
</Accounts>
```

#### ResetAccountPassword

调用ResetAccountPassword接口重置MongoDB实例中root账号的密码。 本接口目前仅支持重置实例中root账号的密码。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetAccountPa ssword | 要执行的操作，取值：ResetAccountPassword。 |
| AccountName | String | 是 | root | 需要重置密码的账号，取值：root。 |
| AccountPasswor d | String | 是 | Ali!123456 | 重置后的密码，即修改后的密码。 密码由大写字母、小写字母、数字、特殊字符中的任意三种组成，特殊字符为 !#$%^&*() +-= _ 密码长度为8~32位。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 06CBD06E-ABC9- 4121-AB93- 3C3820B3E7E6 | 请求ID。 |

**示例**

云数据库 MongoDB 版请求示例

```
http(s)://mongodb.example.com/?Action=ResetAccountPassword &AccountName=root &AccountPassword=Ali!123456 &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>06CBD06E-ABC9-4121-AB93-3C3820B3E7E6</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "06CBD06E-ABC9-4121-AB93-3C3820B3E7E6"
}
```

#### ModifyAccountDescription

调用ModifyAccountDescription接口修改MongoDB实例中root账号的备注信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAccountD escription | 要执行的操作，取值：ModifyAccountDescription。 |
| AccountDescripti on | String | 是 | superadmin | 设置账号的备注信息。 不能以http:// 或者 https:// 开头。 以中文、英文字母开头。 可以包含中文、英文字符、下划线 （ ）、连接号（-）和数字，长度为 _ 2~256个字符。 |
| AccountName | String | 是 | root | 待修改备注信息的账号名。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库 MongoDB 版

| RequestId | String | 59DE9FC2-7B40- 45CF-9011- 7327A8A771A2 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyAccountDescription &AccountName=root &AccountDescription=superadmin &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>59DE9FC2-7B40-45CF-9011-7327A8A771A2</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "59DE9FC2-7B40-45CF-9011-7327A8A771A2"
}
```

#### CreateAccount

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Query | 是 | CreateAccount | 系统规定参数，取值为 CreateAccount。 |
| DBInstanc eId | Strin g | Query | 是 | dds-ir4c9c4cfe26a894 | 实例 ID。 |
| AccountN ame | Strin g | Query | 是 | testxxx | 账号名称。 |
| AccountPa ssword | Strin g | Query | 是 | Pw123xxxx | 账号密码。 |

云数据库 MongoDB 版

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| AccountD escription | Strin g | Query | 否 | test账号 | 账号描述。 |
| Database Name | Strin g | Query | 否 | db1 | 数据库名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8xxxx | 请求 ID。 |

**示例**

请求示例

```
&DBInstanceId=dds-ir4c9c4cfe26a894 &AccountName=testxxx &AccountPassword=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"F8CA8312-530A-413A-9129-F2BB32A8xxxx"
}
```

`XML` 格式

```xml
<RequestId>F8CA8312-530A-413A-9129-F2BB32A8xxxx</RequestId>
```

**错误码**

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccountNam e.Malformed | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |
| 400 | InvalidAccountPass word.Malformed | InvalidAccountPassword.Malfor med | Specified parameter AccountPassword is not valid. |

云数据库 MongoDB 版

| HttpCo de | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidAccountDesc ription.Malformed | InvalidAccountDescription.Malf ormed | Specified parameter AccountDescription is not valid. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |
| 404 | AccountLimitExcee ded | AccountLimitExceeded | AccountQuotaExceeded: Exceeding the allowed amount of account. |
| 400 | InvalidParameters. Format | InvalidParameters.Format | Specified parameter AccountName or AccountPassword not exist. |
| 403 | IncorrectAccountTy pe | IncorrectAccountType | Current account type does not support this operation. |
| 403 | InvalidDBName | InvalidDBName | The specified database name is not allowed. |
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Specified account name already exists in this instance. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.Forbid | Specified Account Name is a keyword in DDS |
| 400 | InvalidParameters. Format | InvalidParameters.Format | The specified database does not exist. |
| 403 | IncorrectDBInstanc eCharacterType | IncorrectDBInstanceCharacter Type | Current DB Instance character type does not _ support this operation. |
| 403 | IncorrectDBInstanc eState | IncorrectDBInstanceState | Current DB instance state does not support this operation. |
| 403 | IncorrectDBInstanc eLockMode | IncorrectDBInstanceLockMode | Current DB instance lock mode does not support this operation. |
| 400 | InvalidAccountPass word.Malformed | IncorrectDBInstanceLockMode | Specified parameter AccountPassword is not valid. |
| 400 | InvalidAccountNam e.Malformed | InvalidAccountName.Malforme d | Specified parameter AccountName is not valid. |

### 白名单和安全组

#### DescribeSecurityGroupConfiguration

调用DescribeSecurityGroupConfiguration接口查询MongoDB实例绑定的ECS安全组信息。

**请求参数**

云数据库 MongoDB 版

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurit yGroupConfigur ation | 要执行的操作，取值：DescribeSecurityGroupConfig uration。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of RdsEcsSecurit yGroupRel |  | ECS安全组信息。 |
| RdsEcsSecurit yGroupRel |  |  |  |
| NetType | String | vpc | ECS安全组的网络类型。返回值： vpc：专有网络。 classic：经典网络。 |
| RegionId | String | cn-hangzhou | ECS安全组所属的地域。 |
| SecurityGroupI d | String | sg-bpxxxxxxxx | ECS安全组ID。 |
| RequestId | String | 3C4A2494-85C4- 45C5-93CF- 548DB3375193 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeSecurityGroupConfiguration &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<Items>
    <RdsEcsSecurityGroupRel>
        <SecurityGroupId>sg-bpxxxxxxxx</SecurityGroupId>
        <RegionId>cn-hangzhou</RegionId>
        <NetType>classic</NetType>
    </RdsEcsSecurityGroupRel>
</Items> <RequestId>D18F5B88-ACA6-470E-9493-384412EDD902</RequestId>
```

`JSON` 格式

```json
{
 "Items": {
  "RdsEcsSecurityGroupRel": [
   {
    "SecurityGroupId": "sg-bpxxxxxxxx",
    "RegionId": "cn-hangzhou",
    "NetType": "classic"
   }
```

]

```json
 },
 "RequestId": "D18F5B88-ACA6-470E-9493-384412EDD902"
}
```

#### DescribeSecurityIps

调用DescribeSecurityIps接口查询MongoDB实例的IP白名单。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSecurit yIps | 要执行的操作，取值：DescribeSecurityIps。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| SecurityIpGrou ps | Array of SecurityIpGrou p |  | IP白名单分组列表。 |
| SecurityIpGrou p |  |  |  |

云数据库 MongoDB 版

| SecurityIpGrou pAttribute | String | hidden | IP白名单分组属性，默认为空。 |
|---|---|---|---|
| SecurityIpGrou pName | String | default | 分组名。 |
| SecurityIpList | String | 47.xxx.xxx.xx,100.x xx.xxx.0/24 | 分组中包含的IP白名单列表。 |
| SecurityIps | String | 47.xxx.xxx.xx,100.x xx.xxx.0/24 | 默认分组中包含的IP白名单。 |
| RequestId | String | FC724D23-2962- 479E-ABB1- 606C935AE7FD | 请求ID。 |
| SecurityIPType | String | ipv4 | IP类型。 ipv4地址。 ipv6地址。 |
| WhitelistNetTy pe | String | mix | 白名单网络类型。 |
| CreateTime | String | "2026-05- 06T02:49:06Z" | 创建时间。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeSecurityIps &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<Response>
    <eagleEyeTraceId>0ab07e0817791996299386818e002d</eagleEyeTraceId>
    <SecurityIps>::1</SecurityIps>
    <asapiSuccess>true</asapiSuccess>
    <asapiRequestId>24F37C1B-6D50-4541-8E62-777A8FCFBA16</asapiRequestId>
    <RequestId>24F37C1B-6D50-4541-8E62-777A8FCFBA16</RequestId>
    <SecurityIpGroups>
        <SecurityIpGroup>
            <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
            <SecurityIPType>ipv4</SecurityIPType>
            <SecurityIpList>127.0.0.1/0</SecurityIpList>
            <CreateTime>2026-05-18T06:45:48Z</CreateTime>
            <WhitelistNetType>mix</WhitelistNetType>
            <SecurityIpGroupName>default</SecurityIpGroupName>
        </SecurityIpGroup>
        <SecurityIpGroup>
            <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
            <SecurityIPType>ipv6</SecurityIPType>
            <SecurityIpList>::1</SecurityIpList>
            <CreateTime>2026-05-18T06:45:48Z</CreateTime>
            <WhitelistNetType>mix</WhitelistNetType>
            <SecurityIpGroupName>default</SecurityIpGroupName>
        </SecurityIpGroup>
    </SecurityIpGroups>
</Response>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
  "eagleEyeTraceId": "0ab07e0817791996299386818e002d",
  "SecurityIps": "::1",
  "asapiSuccess": true,
  "asapiRequestId": "24F37C1B-6D50-4541-8E62-777A8FCFBA16",
  "RequestId": "24F37C1B-6D50-4541-8E62-777A8FCFBA16",
  "SecurityIpGroups": {
    "SecurityIpGroup": [
      {
        "SecurityIpGroupAttribute": "",
        "SecurityIPType": "ipv4",
        "SecurityIpList": "127.0.0.1/0",
        "CreateTime": "2026-05-18T06:45:48Z",
        "WhitelistNetType": "mix",
        "SecurityIpGroupName": "default"
      },
      {
        "SecurityIpGroupAttribute": "",
        "SecurityIPType": "ipv6",
        "SecurityIpList": "::1",
        "CreateTime": "2026-05-18T06:45:48Z",
        "WhitelistNetType": "mix",
        "SecurityIpGroupName": "default"
      }
```

]

```
  }
}
```

#### ModifySecurityIps

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Action | Strin g | Quer y | 是 | ModifySecurityIps | 要执行的操作，取值： ModifySecurityIps。 |
| DBInstanc eId | Strin g | Quer y | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| SecurityIps | Strin g | Quer y | 是 | 10.23.12.24/24,10.22.22. 22 | IP白名单分组下的IP列表，多个IP地址请以英文逗号（,） 隔开，不可重复，最多1000 个。支持如下两种格式： IP地址形式，例如： 10.23.12.24。 CIDR形式，例如： 10.23.12.24/24（无类域间路由，24表示了地址中前缀的长度，范围为 1~32）。 |
|---|---|---|---|---|---|
| ModifyMod e | Strin g | Quer y | 否 | Append | 修改方式，取值： Cover：覆盖原白名单。 Append：追加白名单。 Delete：删除该白名单。 默认取值为Cover。 |
| SecurityIp GroupNam e | Strin g | Quer y | 否 | allowserver | 进行修改的IP白名单所属分组名称，默认为default分组。 |
| SecurityIp GroupAttri bute | Strin g | Quer y | 否 | test | 白名单分组属性。支持大写字母、小写字母、数字，长度最大为120个字符。 默认为空字符串。 |
| SecurityIP Type | Strin g | Quer y | 否 | ipv4 | IP类型，默认ipv4。取值范围： ipv4 ipv6 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 61B05CCF-EBAB- 4BF3-BA67- D77256A721E2 | 请求ID。 |

**示例**

请求示例云数据库 MongoDB 版

```
&DBInstanceId=dds-bpxxxxxxxx &SecurityIps=10.23.12.24/24,10.22.22.22
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"61B05CCF-EBAB-4BF3-BA67-D77256A721E2"
}
```

`XML` 格式

```xml
<RequestId>61B05CCF-EBAB-4BF3-BA67-D77256A721E2</RequestId>
```

### 密钥管理

#### DescribeDBInstanceTDEInfo

调用DescribeDBInstanceTDEInfo接口查询MongoDB实例的透明数据加密TDE（Transparent Data Encryption）是否开启。 调用本接口时，实例必须满足以下条件： 实例为副本集实例或分片集群实例。 实例的存储引擎为WiredTiger。 实例的数据库版本为4.0或4.2版本，如果实例数据库版本过低，您可以调用**UpgradeDBInstanceEngineVersion**接口升级数据库版本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceTDEInfo | 要执行的操作，取值：DescribeDBInstanceTDEInfo。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | F4DD0E29-361B- 42F2-9301- B0048CCCE5D6 | 请求ID。 |

云数据库 MongoDB 版

| TDEStatus | String | enabled | TDE状态，返回值为： enabled：开启状态。 disabled：关闭状态。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceTDEInfo &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TDEStatus>enabled</TDEStatus> <RequestId>F4DD0E29-361B-42F2-9301-B0048CCCE5D6</RequestId>
```

`JSON` 格式

```json
{
    "TDEStatus":"enabled",
    "RequestId":"F4DD0E29-361B-42F2-9301-B0048CCCE5D6"
}
```

#### ModifyDBInstanceTDE

调用ModifyDBInstanceTDE接口修改MongoDB实例的透明数据加密TDE（Transparent Data Encryption）状态。 透明数据加密TDE（Transparent Data Encryption）可对数据文件执行实时I/O加密和解密，数据在写入磁盘之前进行加密，从磁盘读入内存时进行解密。 TDE功能开通后无法关闭。

**说明**

调用本接口时，实例必须满足以下条件： 实例为副本集实例或分片集群实例。 实例的存储引擎为WiredTiger。 实例的数据库版本为4.0或4.2版本，如果实例数据库版本过低，您可以调用**UpgradeDBInstanceEngineVersion**接口升级数据库版本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eTDE | 要执行的操作，取值：ModifyDBInstanceTDE。 |

云数据库 MongoDB 版

| DBInstanceId | String | 是 |  | dds-bpxxxxxxxx | 实例ID。 |  |  |
|---|---|---|---|---|---|---|---|
| TDEStatus | String | 是 |  | enabled | TDE状态，取值： enabled，即开启TDE 功能。 说明 TDE功能开启后不支持关闭，请谨慎开启。 |  |  |
| EncryptorName | String | 否 |  | aes-256-cbc | 加密方式，取值：aes-256-cbc。 说明当TEDStatus参数取值为enabled时，本参数才可用。 |  |  |
| EncryptionKey | String | 否 |  | 749c1df7-xxxx- xxxx-xxxx- xxxxxxxxxxxx | 自定义密钥ID。 |  |  |
| RoleARN | String | 否 |  |  | 指定角色的ARN。格式： acs:ram::$accountID:role/$r oleName 。 说明 $accountID ：云账号ID。您可以通过登录阿里云控制台，将鼠标悬停在右上角头像的位置，单击安全设置进行查看。 $roleName ：RAM角色名称。您可以通过登录RAM控制台，单击左侧导航栏的RAM角色管理，在RAM角色名称列表下进行查看。 |  |  |
|  |  |  |  |  |  | acs:ram::$accountID:role/$r |  |
|  |  |  |  |  | oleName |  |  |
|  |  |  |  | acs:ram::12345 6789012****:rol e/adminrole |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 434D7127-6229- 4355-BA50- 7A3685A725DF | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceTDE &DBInstanceId=dds-bpxxxxxxxx &TDEStatus=enabled
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <RequestId>434D7127-6229-4355-BA50-7A3685A725DF</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "434D7127-6229-4355-BA50-7A3685A725DF"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectDBInstanc eState | Current DB instance state does not support this operation. | 实例状态不支持此操作，请您检查输入的参数是否正确。 |
| 403 | IncorrectDBInstanc eLockMode | Current DB instance lock mode does not support this operation. | 实例已经被锁定。 |

### SSL加密

#### ModifyDBInstanceSSL

调用ModifyDBInstanceSSL接口修改MongoDB实例的SSL配置。 调用该接口时，实例必须满足以下条件： 实例状态为运行中。 实例类型为副本集实例。 实例的数据库版本为3.4、4.0或4.2。

**说明**

在开通、更新和关闭SSL过程中，实例会重启一次，建议您在业务低峰期操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyDBInstanc eSSL | 要执行的操作，取值： ModifyDBInstanceSSL。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| SSLAction | String | 是 | Open | 对SSL功能执行的操作，取值： Open：开启SSL加密。 Close：关闭SSL加密。 Update：更新SSL证书。 |
|---|---|---|---|---|
| ConfigMode | String | 否 | free | 配置模式。取值： simple：简化模式。 advanced：完整模式。 说明仅MongoDB7及以上版本支持。 |
| CertSource | String | 是 | cloud | 证书来源：标识当前 SSL 证书的颁发机构或来源类型。不填默认为cloud。可选值： cloud、custom。custom模式暂不支持。 |
| ConnectionStrin g | String | 是 | "pc- xxxxx.redis.rds.a liyuncs.com:637 9" | 受保护的连接串。 说明仅MongoDB7及以上版本支持。 |
| TLSMode | String | 否 | required | TLS加密模式：定义服务器对客户端连接的加密要求策略。 prefer：优先加密。允许客户端选择是否加密，若客户端支持则强制加密，否则允许明文连接。 required：强制加密。拒绝所有非加密的连接请求，客户端必须提供有效证书。 说明仅MongoDB7及以上版本支持。 |
| MinTLSVersion | String | 否 | TLSv1.2 | 最小支持TLS版本：实例允许建立的最低 TLS协议版本，用于保障安全性。 常见取值："TLSv1.0", "TLSv1.1", "TLSv1.2", " TLSv1.3"。 说明仅MongoDB7及以上版本支持。 |

**返回数据**

云数据库 MongoDB 版

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6D806B11-078F- 4154-BF9F- 844F56D08964 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx &SSLAction=Open
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>6D806B11-078F-4154-BF9F-844F56D08964</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "6D806B11-078F-4154-BF9F-844F56D08964"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectDBInstanc eState | Current DB instance state does not support this operation. | 实例状态不支持此操作，请您检查输入的参数是否正确。 |
| 403 | IncorrectDBInstanc eLockMode | Current DB instance lock mode does not support this operation. | 实例已经被锁定。 |

#### DescribeDBInstanceSSL

调用DescribeDBInstanceSSL接口查询MongoDB实例的SSL设置详情。 调用该接口时，实例必须满足以下条件： 实例状态为运行中。 云数据库 MongoDB 版实例类型为副本集实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta nceSSL | 要执行的操作，取值：DescribeDBInstanceSSL。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| SSLExpiredTim e | String | 2020-03- 11T02:28:25Z | SSL证书的过期时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| RequestId | String | 36BB1BC2-789C- 4BBA-A519- C5B388E4B0D4 | 请求ID。 |
| SSLStatus | String | Open | SSL功能的状态。 Open：SSL功能已开启。 Closed：SSL功能已关闭。 |
| CertCommonN ame | String | dds- bpxxxxxxxx.mongo db.rds.example.co m | SSL证书名称。 |
| ConnectionStri ng | String | pc- xxxxx.redis.rds.aliy uncs.com:6379 | 受保护的连接串：启用SSL/TLS加密后的数据库连接地址。客户端需使用此地址并配置证书才能建立安全连接。 |
| SSLEnabled | Boolean | true | TLS加密开启状态：标识实例当前是否已开启 SSL加密功能。 true：已开启 false：未开启 |

云数据库 MongoDB 版

| TLSMode | String | required | TLS加密模式：定义服务器对客户端连接的加密要求策略。 prefer：优先加密。允许客户端选择是否加密，若客户端支持则强制加密，否则允许明文连接。 required：强制加密。拒绝所有非加密的连接请求，客户端必须提供有效证书。 说明仅MongoDB7及以上版本，设置了值时该参数才有值返回。 |
|---|---|---|---|
| MinTLSVersion | String | TLSv1.2 | 最小支持TLS版本：实例允许建立的最低TLS协议版本，用于保障安全性。 常见取值："TLSv1.0", "TLSv1.1", "TLSv1.2", "TLSv 1.3"。 说明仅MongoDB7及以上版本，设置了值时该参数才有值返回。 |
| CertSource | String | cloud | 证书来源：标识当前使用的SSL证书的颁发机构或来源类型。取值：cloud，custom 说明仅MongoDB7及以上版本，设置了值时该参数才有值返回。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceSSL &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
    <RequestId>36BB1BC2-789C-4BBA-A519-C5B388E4B0D4</RequestId>
    <SSLStatus>Open</SSLStatus>
    <SSLEnabled>true</SSLEnabled>
    <SSLExpiredTime>2020-03-11T02:28:25Z</SSLExpiredTime>
    <CertCommonName>dds-bpxxxxxxxx.mongodb.rds.example.com</CertCommonName>
    <ConnectionString>pc-xxxxx.redis.rds.aliyuncs.com:6379</ConnectionString>
    <TLSMode>required</TLSMode>
    <MinTLSVersion>TLSv1.2</MinTLSVersion>
    <CertSource>aliyun</CertSource>
```

`JSON` 格式

```json
{
    "RequestId": "36BB1BC2-789C-4BBA-A519-C5B388E4B0D4",
    "SSLStatus": "Open",
    "SSLEnabled": true,
    "SSLExpiredTime": "2020-03-11T02:28:25Z",
    "CertCommonName": "dds-bpxxxxxxxx.mongodb.rds.example.com",
    "ConnectionString": "pc-xxxxx.redis.rds.aliyuncs.com:6379",
    "TLSMode": "required",
    "MinTLSVersion": "TLSv1.2",
    "CertSource": "aliyun"
}
```

### 审计日志

#### DescribeAuditRecords

调用DescribeAuditRecords接口查询MongoDB实例的审计日志。 调用本接口时，实例的审计日志须处于开通状态，否则返回的审计日志内容为空。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAuditRe cords | 要执行的操作，取值：DescribeAuditRecords。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |

云数据库 MongoDB 版

| EndTime | String | 是 | 2019-03- 13T13:11:14Z | 查询结束时间，必须晚于查询开始时间， 格式为*yyyy-MM- dd*T*HH:mm:ss*Z（UTC时间）。 |
|---|---|---|---|---|
| StartTime | String | 是 | 2019-03- 13T12:11:14Z | 查询开始时间，格式为*yyyy-MM- dd*T*HH:mm:ss*Z（UTC时间）。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| Database | String | 否 | testdatabase | 数据库名，默认为所有数据库。 |
| User | String | 否 | root | 数据库账号，默认为所有账号。 |
| Form | String | 否 | Stream | 审计记录返回的展示类型，取值： File：触发审计日志文件的生成，若传入这个值，只返回公共参数，需再调用DescribeAuditFiles获取文件的下载地址。 Stream：返回数据流。 默认为Stream。 |
| QueryKeywords | String | 否 | slow | 关键字查询，多个关键字以空格分隔，不超过10个关键字。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值：30、50、100，默认值为30。 |
| PageNumber | Integer | 否 | 1 | 页码，大于0，且不超过Integer的最大值，默认值为1。 |
| OrderType | String | 否 | asc | 按时间的升降序对查询到的慢日志进行排序。取值： asc：按时间升序排序。 desc：按时间降序排序。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Items | Array of SQLRecord |  | 审计日志详情列表。 |

云数据库 MongoDB 版

| SQLRecord |  |  |  |
|---|---|---|---|
| AccountName | String | root | 数据库账号名。 |
| DBName | String | test123 | 数据库名。 |
| ExecuteTime | String | 2019-03- 11T03:30:27Z | 该语句执行的时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| HostAddress | String | 11.xxx.xxx.xxx | 客户端IP地址。 |
| ReturnRowCou nts | Long | 2 | 返回记录数。 |
| Syntax | String | { \"atype\" : \"createCollection\" , \"param\" : { \"ns\" : \"123.test1\" }, \"result\": \"OK\" } | 执行语句。 |
| TableName | String | C1 | MongoDB的集合名称。 |
| ThreadID | String | 140682188297984 | 线程ID。 |
| TotalExecution Times | Long | 700 | 消耗时间，单位为微秒。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 当前页最大记录数。 |
| RequestId | String | 3278BEB8-503B- 4E46-8F7E- D26E040C9769 | 请求ID。 |
| TotalRecordCo unt | Integer | 40 | 总记录数。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeAuditRecords &StartTime=2019-03-13T12:11:14Z &EndTime=2019-03-13T13:11:14Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例云数据库 MongoDB 版 `XML` 格式

```xml
<TotalRecordCount>40</TotalRecordCount> <PageRecordCount>30</PageRecordCount> <RequestId>3278BEB8-503B-4E46-8F7E-D26E040C9769</RequestId> <PageNumber>1</PageNumber> <Items>
    <TableName>C1</TableName>
    <ThreadID>140682188297984</ThreadID>
    <ExecuteTime>2019-03-11T03:30:27Z</ExecuteTime>
    <ReturnRowCounts>2</ReturnRowCounts>
    <DBName>test123</DBName>
    <TotalExecutionTimes>700</TotalExecutionTimes>
    <Syntax>{ \"atype\" : \"createCollection\", \"param\" : { \"ns\" : \"123.test1\" },
\"result\": \"OK\" }</Syntax>
    <HostAddress>11.xxx.xxx.xxx</HostAddress>
    <AccountName>root</AccountName>
</Items>
```

`JSON` 格式

```json
{
    "TotalRecordCount":"40",
    "PageRecordCount":"30",
    "RequestId":"3278BEB8-503B-4E46-8F7E-D26E040C9769",
    "PageNumber":"1",
    "Items":[
        {
            "TableName":"C1",
            "ThreadID":"140682188297984",
            "ExecuteTime":"2019-03-11T03:30:27Z",
            "ReturnRowCounts":"2",
            "DBName":"test123",
            "TotalExecutionTimes":"700",
            "Syntax":"{ \\\"atype\\\" : \\\"createCollection\\\", \\\"param\\\" : { \\\"
ns\\\" : \\\"123.test1\\\" }, \\\"result\\\": \\\"OK\\\" }",
            "HostAddress":"11.xxx.xxx.xxx",
            "AccountName":"root"
        }
```

]

```
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidEndTime.For mat | Specified end time is not valid. | 输入的结束时间无效，请您检查输入的时间格式是否正确。 |

#### DescribeAuditFiles

云数据库 MongoDB 版调用DescribeAuditFiles接口查询MongoDB实例的审计日志文件。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAuditFil es | 要执行的操作，取值：DescribeAuditFiles。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID。 说明如不传入则返回所有 Mongos节点和Shard节点的审计日志。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30、50、100，默认值为30。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的的最大值，默认值为1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DBInstanceId | String | dds-bpxxxxxxxx | 实例ID。 |
| Items | Array of LogFile |  | 审计文件信息列表。 |
| LogFile |  |  |  |
| FileID | Integer | 406505 | 文件ID。 |
| LogDownloadU RL | String | http://xxxxxxxx.oss -cn- hangzhou.aliyuncs. com/custinsxxxxxx /custinsxxxxxx xxx _ xxx.csv | 审计日志文件的下载链接。 说明若当前不可下载，则为空串。 |
| LogEndTime | String | 2019-03- 12T09:23:15Z | 审计日志结束时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| LogSize | Long | 98 | 审计日志文件的大小，单位为Byte。 |

云数据库 MongoDB 版

| LogStartTime | String | 2019-03- 11T08:19:29Z | 审计日志起始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
|---|---|---|---|
| LogStatus | String | Success | 审计日志文件状态。 Success：归档完成。 Failed：归档失败。 Generating：归档中。 Initializing：未开始。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 当前页记录数。 |
| RequestId | String | F8CA8312-530A- 413A-9129- F2BB32A8D404 | 请求ID。 |
| TotalRecordCo unt | Integer | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeAuditFiles &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <Items>
      <LogFile>
         <LogStartTime>2019-03-11T08:19:29Z</LogStartTime>
         <LogEndTime>2019-03-12T09:23:15Z</LogEndTime>
         <LogStatus>Success</LogStatus>
         <FileID>406505</FileID>
         <LogDownloadURL>http://xxxxxxxx.oss-cn-
hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv</LogDownloadURL>
         <LogSize>98</LogSize>
      </LogFile>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>1</TotalRecordCount>
   <RequestId>F8CA8312-530A-413A-9129-F2BB32A8D404</RequestId>
   <PageRecordCount>1</PageRecordCount>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
 "Items": {
  "LogFile": [
   {
    "LogStartTime": "2019-03-11T08:19:29Z",
    "LogEndTime": "2019-03-12T09:23:15Z",
    "LogStatus": "Success",
    "FileID": 406505,
    "LogDownloadURL": "http://xxxxxxxx.oss-cn-
hangzhou.aliyuncs.com/custinsxxxxxx/custinsxxxxxx_xxxxxx.csv",
    "LogSize": 98
   }
```

]

```json
 },
 "PageNumber": 1,
 "TotalRecordCount": 1,
 "RequestId": "F8CA8312-530A-413A-9129-F2BB32A8D404",
 "PageRecordCount": 1
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstanceC lass.NotFound | Specified DB instance class is not found. | 该实例规格不存在，请您检查输入的参数是否正确。 |
| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | 当前的实例类型不支持此操作。 |

#### DescribeAuditPolicy

调用DescribeAuditPolicy接口查询MongoDB实例的审计日志是否开启。 调用本接口时，要求实例状态为运行中。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAuditPo licy | 要执行的操作，取值： DescribeAuditPolicy。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

云数据库 MongoDB 版

| LogAuditStatu s | String | Enable | 审计日志的状态。 Enable：开启。 Disabled：关闭。 默认为关闭状态。 |
|---|---|---|---|
| RequestId | String | 111E7B16-0A87- 4CBA-B271- F34AD61E099F | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeAuditPolicy &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <LogAuditStatus>Enable</LogAuditStatus>
   <RequestId>111E7B16-0A87-4CBA-B271-F34AD61E099F</RequestId>
```

`JSON` 格式

```json
{
 "LogAuditStatus": "Enable",
 "RequestId": "111E7B16-0A87-4CBA-B271-F34AD61E099F"
}
```

#### ModifyAuditLogFilter

调用ModifyAuditLogFilter接口修改MongoDB实例审计日志的采集类型。 调用本接口时，要求实例状态为运行中。 本接口仅适用于副本集实例，暂不支持分片集群实例。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAuditLogF ilter | 要执行的操作，取值： ModifyAuditLogFilter。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

云数据库 MongoDB 版

| Filter | String | 是 | insert,query,upd ate,delete | 设置审计日志的采集类型。 admin：运维管控操作。 slow：慢日志。 query：查询操作。 insert：插入操作。 update：更新操作。 delete：删除操作。 command：协议命令。例如 aggregate聚合方法。 |
|---|---|---|---|---|
| RoleType | String | 否 | primary | 实例中节点的角色，取值： primary：主节点。 secondary：从节点。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | E209BE2B-F264- 4B9D-81F6- A5A5FB1FBF28 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyAuditLogFilter &Filter=insert,query,update,delete &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "E209BE2B-F264-4B9D-81F6-A5A5FB1FBF28"
}
```

#### DescribeAuditLogFilter

调用DescribeAuditLogFilter接口查询MongoDB实例审计日志采集的日志类型。 调用本接口时，要求实例状态为运行中。 云数据库 MongoDB 版本接口仅适用于副本集实例，暂不支持分片集群实例。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAuditLo gFilter | 要执行的操作，取值： DescribeAuditLogFilter。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| RoleType | String | 否 | primary | 实例中节点的角色，取值： primary：主节点。 secondary：从节点。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Filter | String | admin,slow,insert,q uery,update,delete ,command | 数据库操作日志类型，有以下几种类型： admin：运维管控操作。 slow：慢日志。 query：查询操作。 insert：插入操作。 update：更新操作。 delete：删除操作。 command：协议命令。例如aggregate聚合方法。 |
| RequestId | String | D7C8BA0C-9350- 487D-9B70- D69AF27FB1EB | 请求ID。 |
| RoleType | String | primary | 节点角色。 |

**示例**

请求示例

```
http(s)://mongodb.aliyuncs.com/?Action=DescribeAuditLogFilter &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <Filter>admin,slow,insert,query,update,delete,command</Filter>
   <RoleType></RoleType>
   <RequestId>D7C8BA0C-9350-487D-9B70-D69AF27FB1EB</RequestId>
```

`JSON` 格式

```json
{
 "Filter": "admin,slow,insert,query,update,delete,command",
 "RoleType": "",
 "RequestId": "D7C8BA0C-9350-487D-9B70-D69AF27FB1EB"
}
```

#### ModifyAuditPolicy

调用ModifyAuditPolicy接口设置MongoDB实例的审计日志开关或日志存储时长。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAuditPolic y | 要执行的操作，取值：ModifyAuditPolicy。 |
| AuditStatus | String | 是 | enable | 审计日志状态，取值： enable：开启审计日志。 disabled：关闭审计日志。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
| StoragePeriod | Integer | 否 | 30 | 审计日志存储的天数。取值范围为1~30，默认为30。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | DC04D812-F18D- 4568-9B88- F260D9590116 | 请求ID。 |

**示例**

请求示例云数据库 MongoDB 版

```
http(s)://mongodb.example.com/?Action=ModifyAuditPolicy &AuditStatus=enable &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>DC04D812-F18D-4568-9B88-F260D9590116</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "DC04D812-F18D-4568-9B88-F260D9590116"
}
```

### 日志管理

#### DescribeSlowLogRecords

调用DescribeSlowLogRecords接口查询某段时间内云数据库MongoDB实例的慢操作日志明细。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeSlowLo gRecords | 系统规定的参数，取值：DescribeSlowLogRecords。 |
| StartTime | String | 是 | 2022-09- 05T12:10Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 说明此时间为慢操作的执行时间，不是慢日志的采集时间。 |
| EndTime | String | 是 | 2022-09- 06T12:10Z | 查询结束时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 说明查询结束时间必须晚于查询开始时间。 查询结束时间距查询开始时间不得超过 24个小时，超过则查询失败。 |

云数据库 MongoDB 版

| DBInstanc eId | String | 是 | dds- bp1366caac83* *** | 实例ID。 说明您可以通过调用 DescribeDBInstanceAttribute接口查询实例ID。 当此参数传入的是分片集群实例ID时， 还需要传入NodeId参数。 |
|---|---|---|---|---|
| NodeId | String | 否 | d- bp18b06ebc21* *** | Shard节点ID。 说明您可以通过调用 DescribeDBInstanceAttribute接口查询Shard节点ID。 当DBInstanceId参数传入的是分片集群实例ID时，此参数才可用。 |
| DBName | String | 否 | admin | 数据库名。 说明不传入此参数时，默认查询所有数据库的慢日志明细。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值范围：30~100，默认值为30。 |
| PageNumb er | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的最大值，默认值为1。 |
| OrderType | String | 否 | asc | 按时间的升降序对查询到的慢日志进行排序，取值说明： asc：按时间升序排序。 desc：（默认值）按时间降序排序。 |
| ResourceG roupId | String | 否 | rg- acfmyiu4ekp*** * | 资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Engine | String | MongoDB | 当前数据库的引擎类型。 |
| Items | Array of LogRecords |  | 慢日志明细列表。 |
| LogRecords |  |  |  |
| AccountName | String | root | 数据库账号名。 |
| DBName | String | admin | 数据库名。 |
| DocsExamined | Long | 1000000 | 慢操作执行时扫描的文档数。 |

云数据库 MongoDB 版

| ExecutionStart Time | String | 2022-09- 06T01:41:28Z | 慢操作的开始执行时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
|---|---|---|---|
| HostAddress | String | 192.168.XX.XX | 连接数据库的客户端IP。 |
| KeysExamined | Long | 0 | 索引扫描行数。 |
| QueryTimes | String | 600 | 查询耗时，单位：毫秒。 |
| ReturnRowCou nts | Long | 0 | 慢操作返回的结果行数。 |
| SQLText | String | {\"op\":\"query\",\" ns\":\"mongodbtest .customer\",\"query \": {\"find\":\"custome r\",\"filter\": {\"name\":\"jack\"} }} | 慢操作执行的语句。 |
| TableName | String | C1 | 集合名称。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 本页慢日志的个数。 |
| RequestId | String | 414A4E5-4C36- 4461-95FC- 23757A20B5F8 | 请求ID。 |
| TotalRecordCo unt | Integer | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeSlowLogRecords &StartTime=2022-09-05T12:10Z &EndTime=2022-09-06T12:10Z &DBInstanceId=dds-bp1366caac83**** &NodeId=d-bp18b06ebc21**** &DBName=admin
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<TotalRecordCount>1</TotalRecordCount> <PageRecordCount>1</PageRecordCount> <RequestId>414A4E5-4C36-4461-95FC-23757A20B5F8</RequestId> <PageNumber>1</PageNumber> <Items>
    <LogRecords>
        <TableName>C1</TableName>
        <QueryTimes>600</QueryTimes>
        <ExecutionStartTime>2022-09-06T01:41:28Z</ExecutionStartTime>
        <ReturnRowCounts>0</ReturnRowCounts>
        <KeysExamined>0</KeysExamined>
        <DBName>mongodbtest</DBName>
        <DocsExamined>1000000</DocsExamined>
        <HostAddress>192.168.XX.XX</HostAddress>
        <AccountName>root</AccountName>
        <SQLText>{\"op\":\"query\",\"ns\":\"mongodbtest.customer\",\"query\":
{\"find\":\"customer\",\"filter\":{\"name\":\"jack\"}}}</SQLText>
    </LogRecords>
</Items> <Engine>MongoDB</Engine>
```

`JSON` 格式

```json
{
    "TotalRecordCount": "1",
    "PageRecordCount": "1",
    "RequestId": "414A4E5-4C36-4461-95FC-23757A20B5F8",
    "PageNumber": "1",
    "Items": {
        "LogRecords": [{
            "TableName": "C1",
            "QueryTimes": "600",
            "ExecutionStartTime": "2022-09-06T01:41:28Z",
            "ReturnRowCounts": "0",
            "KeysExamined": "0",
            "DBName": "mongodbtest",
            "DocsExamined": "1000000",
            "HostAddress": "192.168.XX.XX",
            "AccountName": "root",
            "SQLText": "
{\\\"op\\\":\\\"query\\\",\\\"ns\\\":\\\"mongodbtest.customer\\\",\\\"query\\\":{\\\"fi nd\\\":\\\"customer\\\",\\\"filter\\\":{\\\"name\\\":\\\"jack\\\"}}}"
        }]
    },
    "Engine": "MongoDB"
}
```

#### DescribeErrorLogRecords

调用DescribeErrorLogRecords接口查询MongoDB实例的错误日志。

**请求参数**

云数据库 MongoDB 版

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeErrorLo gRecords | 要执行的操作，取值：DescribeErrorLogRecords。 |
| StartTime | String | 是 | 2019-01- 01T12:10Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2019-01- 02T12:10Z | 查询结束时间，必须晚于查询开始时间， 格式为yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| RoleType | String | 否 | primary | 实例中节点的角色。取值： primary：主节点。 secondary：从节点。 说明当NodeId参数传入的是Mongos节点ID时，本参数取值只能为primary。 |
| DBName | String | 否 | mongodbtest | 数据库名。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值范围：30~100。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的的最大值，默认值为1。 |
| ResourceGroupI d | String | 否 | rg-axxxxxxxx | 资源组ID。 |

**返回数据**

云数据库 MongoDB 版

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Engine | String | MongoDB | 数据库引擎。 |
| Items | Array of LogRecords |  | 错误日志明细列表。 |
| LogRecords |  |  |  |
| Category | String | NETWORK | 日志类别。 |
| ConnInfo | String | conn18xxxxxx | 日志连接信息。 |
| Content | String | xxxxxxxx | 日志信息。 |
| CreateTime | String | 2019-02- 26T12:09:34Z | 日志生成时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Id | Integer | 1111111111 | 日志ID。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 1 | 每页的记录数。 |
| RequestId | String | 68BCBEC2-1E66- 471F-A1A8- E3C60C0A80B0 | 请求ID。 |
| TotalRecordCo unt | Integer | 1 | 总记录数。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeErrorLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <Items>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>xxxxxxxx</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0</RequestId>
```

`JSON` 格式

```json
{
    "TotalRecordCount":"1",
    "PageRecordCount":"1",
    "RequestId":"68BCBEC2-1E66-471F-A1A8-E3C60C0A80B0",
    "PageNumber":"1",
    "Items":{
        "LogRecords":[
            {
                "ConnInfo":"conn18xxxxxx",
                "Category":"NETWORK",
                "Id":"1111111111",
                "Content":"xxxxxxxx",
                "CreateTime":"2019-02-26T12:09:34Z"
            }
```

]

```
    },"Engine":"MongoDB"
}
```

#### DescribeRunningLogRecords

调用DescribeRunningLogRecords接口查询MongoDB实例的运行日志。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRunnin gLogRecords | 要执行的操作，取值：DescribeRunningLogRecords 。 |
| StartTime | String | 是 | 2019-01- 01T12:10Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |

云数据库 MongoDB 版

| EndTime | String | 是 | 2019-01- 02T12:10Z | 查询结束时间，必须晚于查询开始时间， 格式为yyyy-MM-ddTHH:mmZ（UTC时间）。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| DBName | String | 否 | mongodbtest | 数据库名。 |
| RoleType | String | 否 | primary | 实例中节点的角色。取值： primary：主节点。 secondary：从节点。 说明当NodeId参数传入的是Mongos节点ID时，RoleType取值只能为primary。 |
| PageSize | Integer | 否 | 30 | 每页记录数，取值范围为30~100。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的的最大值，默认值为1。 |
| OrderType | String | 否 | asc | 按时间的升降序对查询到的慢日志进行排序。取值： asc：按时间升序排序。 desc：按时间降序排序。 |
| ResourceGroupI d | String | 否 | rg-axxxxxxx | 资源组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Engine | String | MongoDB | 当前数据库的引擎类型。 |

云数据库 MongoDB 版

| Items | Array of LogRecords |  | 运行日志明细列表。 |
|---|---|---|---|
| LogRecords |  |  |  |
| Category | String | NETWORK | 日志类别。 |
| ConnInfo | String | conn18xxxxxx | 日志连接信息。 |
| Content | String | end connection 11.xxx.xxx.xx:3xxx x (0 connections now open)\n | 日志信息。 |
| CreateTime | String | 2019-02- 26T12:09:34Z | 日志生成时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| Id | Integer | 1111111111 | 日志ID。 |
| PageNumber | Integer | 1 | 页码。 |
| PageRecordCo unt | Integer | 30 | 每页的记录数。 |
| RequestId | String | 45D2B592-DEBA- 4347-BBF3- 47FF6C97DBBC | 请求ID。 |
| TotalRecordCo unt | Integer | 2 | 总记录数。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeRunningLogRecords &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <Items>
      <LogRecords>
         <Category>-</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>conn18xxxxxx</ConnInfo>
         <Content>
    end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)
   </Content>
      </LogRecords>
      <LogRecords>
         <Category>NETWORK</Category>
         <CreateTime>2019-02-26T12:09:34Z</CreateTime>
         <ConnInfo>thread1</ConnInfo>
         <Content>connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11 connections
now open)</Content>
      </LogRecords>
   </Items>
   <PageNumber>1</PageNumber>
   <TotalRecordCount>2</TotalRecordCount>
   <RequestId>45D2B592-DEBA-4347-BBF3-47FF6C97DBBC</RequestId>
```

`JSON` 格式

```json
{
    "Items": {
        "LogRecords": [
            {
                "Category": "-",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "conn18xxxxxx",
                "Content": "end connection 11.xxx.xxx.xx:3xxxx (0 connections now open)\
```

`n"`

```json
            },
            {
                "Category": "NETWORK",
                "CreateTime": "2019-02-26T12:09:34Z",
                "ConnInfo": "thread1",
                "Content": "connection accepted from 11.xxx.xxx.xx:3xxxx #1862051 (11
connections now open)"
            }
```

]

```json
    },
    "PageNumber": 1,
    "TotalRecordCount": 2,
    "RequestId": "45D2B592-DEBA-4347-BBF3-47FF6C97DBBC"
}
```

### 性能监控管理

云数据库 MongoDB 版

#### DescribeDBInstancePerformance

调用DescribeDBInstancePerformance接口查询MongoDB实例性能数据。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDBInsta ncePerformance | 要执行的操作，取值：DescribeDBInstancePerforma nce。 |
| Key | String | 是 | MongoDB Detail _ edSpaceUsage | 性能指标，取值： CpuUsage：CPU使用率。 MemoryUsage：内存使用率。 MongoDB IOPS：IOPS 使用量。 _ IOPSUsage：IOPS 使用率。 MongoDB DetailedSpaceUsage _ ：磁盘空间使用量。 DiskUsage：磁盘空间使用率。 MongoDB Opcounters： _ Opcounters。 MongoDB Connections： _ Connections。 MongoDB Cursors：Cursors。 _ MongoDB Network：Network。 _ MongoDB Global Lock Current _ _ _ Queue：GlobalLock。 _ MongoDB Wt Cache： _ _ WiredTiger。 说明如需传入多个指标使用英文逗号（,）分隔。 |
| StartTime | String | 是 | 2019-03- 11T12:30Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2019-03- 11T12:30Z | 查询结束时间，必须晚于查询开始时间， 格式为yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |

云数据库 MongoDB 版

| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID，可用于查询单个节点的性能情况。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
|---|---|---|---|---|
| ReplicaSetRole | String | 否 | Primary | 节点角色，取值： Primary：主节点。 Secondary：从节点。 说明当DBInstanceId参数传入的是单节点实例，本参数的取值仅支持Primary。 |
| RoleId | String | 否 | 60xxxxx | 实例的节点角色ID，可通过DescribeReplicaSetRole接口查询。 说明当DBInstanceId参数传入的是副本集实例ID时，本参数才可用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 267F98DC-367D- 4F20-B137- 8B5B664D1C5D | 请求ID。 |
| StartTime | String | 2019-03- 11T12:20Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 2019-03- 11T12:30Z | 查询结束时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| PerformanceK eys | Array of PerformanceK ey |  | 性能指标信息列表。 |
| PerformanceK ey |  |  |  |
| Key | String | MongoDB Detailed _ SpaceUsage | 性能指标。 |
| PerformanceV alues | Array of PerformanceV alue |  | 性能指标值列表。 |

云数据库 MongoDB 版

| PerformanceV alue |  |  |  |
|---|---|---|---|
| Date | String | 2019-03- 11T12:21:51Z | 性能指标值产生的日期。 |
| Value | String | 0.6 | 性能指标值。 |
| Unit | String | MB | 展示单位。 |
| ValueFormat | String | cpu usage _ | 性能指标值的格式。如果该性能指标包含多个字段，通常以&amp;分隔。 例如查询磁盘空间使用量，返回的ValueFormat 即为ins size&amp;data size&amp;log si _ _ _ ze。 |
| DBInstanceId | String | dds-bpxxxxxxxx | 示例ID。 |
| Engine | String | MongoDB | 数据库引擎，固定为MongoDB。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstancePerformance &Key=MongoDB_DetailedSpaceUsage &StartTime=2019-03-11T12:30Z &EndTime=2019-03-11T12:30Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<PerformanceKeys>
    <ValueFormat>cpu_usage</ValueFormat>
    <Unit>MB</Unit>
    <Key>MongoDB_DetailedSpaceUsage</Key>
</PerformanceKeys> <PerformanceKeys>
    <PerformanceValues>
        <Value>0.6</Value>
        <Date>2019-03-11T12:21:51Z</Date>
    </PerformanceValues>
</PerformanceKeys> <EndTime>2019-03-11T12:30Z</EndTime> <RequestId>267F98DC-367D-4F20-B137-8B5B664D1C5D</RequestId> <DBInstanceId>dds-bpxxxxxxxx</DBInstanceId> <StartTime>2019-03-11T12:20Z</StartTime> <Engine>MongoDB</Engine>
```

`JSON` 格式

```json
{
    "PerformanceKeys":[
        {
            "ValueFormat":"cpu_usage",
            "Unit":"MB",
            "Key":"MongoDB_DetailedSpaceUsage"
        },
        {
            "PerformanceValues":[
                {
                    "Value":"0.6",
                    "Date":"2019-03-11T12:21:51Z"
                }
```

]

```
        }
```

`],`

```json
    "EndTime":"2019-03-11T12:30Z",
    "RequestId":"267F98DC-367D-4F20-B137-8B5B664D1C5D",
    "DBInstanceId":"dds-bpxxxxxxxx",
    "StartTime":"2019-03-11T12:20Z",
    "Engine":"MongoDB"
}
```

#### DescribeDBInstanceMonitor

调用DescribeDBInstanceMonitor接口查询MongoDB实例的监控采集粒度。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | DescribeDBInsta nceMonitor | 要执行的操作，取值：DescribeDBInstanceMonitor。 |
|---|---|---|---|---|
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Granularity | String | 300 | 监控采集粒度。返回值固定为300，单位为秒。 |
| RequestId | String | EFD65226-08CC- 4C4D-B6A4- CB3C382F67B0 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeDBInstanceMonitor &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<Granularity>300</Granularity> <RequestId>EFD65226-08CC-4C4D-B6A4-CB3C382F67B0</RequestId>
```

`JSON` 格式

```json
{
 "Granularity": 300,
 "RequestId": "EFD65226-08CC-4C4D-B6A4-CB3C382F67B0"
}
```

### 参数管理

**8.14.1.**

#### DescribeParameterModificationHistory

调用DescribeParameterModificationHistory接口查询MongoDB实例参数的修改记录。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

云数据库 MongoDB 版

| Action | String | 是 | DescribeParame terModificationH istory | 要执行的操作，取值：DescribeParameterModificati onHistroy。 |
|---|---|---|---|---|
| StartTime | String | 是 | 2019-01- 01T12:10Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2019-01- 02T12:10Z | 查询结束时间，必须晚于查询开始时间， 格式为yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| CharacterType | String | 是 | db | 实例的角色类型，取值： db：shard角色 cs：config server角色 mongos：mongos角色 logic：分片集群实例 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Mongos节点ID或Shard 节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| RegionId | String | 否 | cn-hangzhou | 实例所属的地域ID，您可以调用DescribeDBInstanceAttribute接口查询。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| HistoricalPara meters | Array of HistoricalPara meter |  | 参数的修改记录列表。 |
| HistoricalPara meter |  |  |  |
| ModifyTime | String | 2019-03- 12T07:58:24Z | 参数修改的时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |

云数据库 MongoDB 版

| NewParameter Value | String | 200 | 修改后的参数值。 |
|---|---|---|---|
| OldParameter Value | String | 100 | 修改前的参数值。 |
| ParameterNa me | String | operationProfiling.s lowOpThresholdMs | 被修改参数的名称。 |
| RequestId | String | B1BB6E0E-B4EF- 4145-81FA- A07719860248 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeParameterModificationHistory &StartTime=2019-01-01T12:10Z &EndTime=2019-01-02T12:10Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<DescribeParameterModificationHistoryResponse>
   <HistoricalParameters>
      <HistoricalParameter>
         <OldParameterValue>100</OldParameterValue>
         <ModifyTime>2019-03-12T07:58:24Z</ModifyTime>
         <NewParameterValue>200</NewParameterValue>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </HistoricalParameter>
   </HistoricalParameters>
   <RequestId>B1BB6E0E-B4EF-4145-81FA-A07719860248</RequestId>
</DescribeParameterModificationHistoryResponse>
```

`JSON` 格式

```json
{
 "HistoricalParameters": {
  "HistoricalParameter": [
   {
    "OldParameterValue": "100",
    "ModifyTime": "2019-03-12T07:58:24Z",
    "NewParameterValue": "200",
    "ParameterName": "operationProfiling.slowOpThresholdMs"
   }
```

]

```json
 },
 "RequestId": "B1BB6E0E-B4EF-4145-81FA-A07719860248"
}
```

云数据库 MongoDB 版

#### DescribeParameters

调用DescribeParameters接口查询MongoDB实例的参数配置信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeParame ters | 要执行的操作，取值：DescribeParameters。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中的Mongos节点ID或 Shard节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| CharacterType | String | 否 | mongos | 账号类型，取值为： mongos：mongos节点的登录账号。 shard：shard节点的登录账号。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| ConfigParamet ers | Array of Parameter |  | 配置中的的参数配置信息列表。 |
| Parameter |  |  |  |
| CheckingCode | String | [0-65536] | 参数取值范围。 |
| ForceRestart | Boolean | true | 修改参数后是否需要重启生效。 flase：无需重启，提交后即生效。 true：需要重启生效。 |
| ModifiableStat us | Boolean | true | 参数是否处于可修改的状态。 flase：不可修改。 true：可修改。 |

云数据库 MongoDB 版

| ParameterDes cription | String | The threshold in milliseconds at which the database profiler considers a query slow, default is 100. | 参数描述。 |
|---|---|---|---|
| ParameterNa me | String | operationProfiling.s lowOpThresholdMs | 参数名。 |
| ParameterValu e | String | 200 | 参数值。 |
| RequestId | String | 3ADD0C7D-2D2A- 4F15-88FF- E7AC9B9FDCC8 | 请求ID。 |
| RunningParam eters | Array of Parameter |  | 当前运行的参数配置信息列表。 |
| Parameter |  |  |  |
| CheckingCode | String | [33554432- 268435456] | 参数取值范围。 |
| ForceRestart | String | false | 修改参数后是否需要重启生效。 flase：无需重启，提交后即生效。 true：需要重启生效。 |
| ModifiableStat us | String | true | 参数是否处于可修改的状态。 flase：不可修改。 true：可修改。 |
| ParameterDes cription | String | The maximum memory bytes that sort stage may use, default is 33554432(i.e. 32MB) | 参数描述。 |
| ParameterNa me | String | setParameter.inter nalQueryExecMaxB lockingSortBytes | 参数名。 |
| ParameterValu e | String | 33554432 | 参数值。 |
| EngineVersion | String | 4.0 | 数据库版本号。 |
| Engine | String | mongodb | 数据库引擎，默认返回mongodb。 |

**示例**

请求示例云数据库 MongoDB 版

```
http(s)://mongodb.example.com/?Action=DescribeParameters &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <ConfigParameters>
      <Parameter>
         <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100.</ParameterDescription>
         <ParameterValue>200</ParameterValue>
         <CheckingCode>[0-65536]</CheckingCode>
         <ForceRestart>false</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </Parameter>
   </ConfigParameters>
   <RequestId>3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8</RequestId>
   <RunningParameters>
      <Parameter>
         <ParameterDescription></ParameterDescription>
         <ParameterValue>zlib</ParameterValue>
         <CheckingCode>snappy|zlib|disabled</CheckingCode>
         <ForceRestart>true</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
         <ParameterName>net.compression.compressors</ParameterName>
      </Parameter>
      <Parameter>
         <ParameterDescription>The level of database profiling, which inserts
information about operation performance into the system.profile collection. 'off' for n o profiling, 'slowOp' for only includes slow operations, 'all' for includes all operati ons, default is 'slowOp'.</ParameterDescription>
         <ParameterValue>slowOp</ParameterValue>
         <CheckingCode>off|slowOp|all</CheckingCode>
         <ForceRestart>false</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
         <ParameterName>operationProfiling.mode</ParameterName>
      </Parameter>
      <Parameter>
         <ParameterDescription>The threshold in milliseconds at which the database
profiler considers a query slow, default is 100.</ParameterDescription>
         <ParameterValue>220</ParameterValue>
         <CheckingCode>[0-65536]</CheckingCode>
         <ForceRestart>false</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
         <ParameterName>operationProfiling.slowOpThresholdMs</ParameterName>
      </Parameter>
      <Parameter>
         <ParameterDescription>The expiration threshold in milliseconds for idle
cursors before MongoDB removes them; i.e. MongoDB removes cursors that have been idle f or the specified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)
```

云数据库 MongoDB 版

```xml
</ParameterDescription>
         <ParameterValue>600000</ParameterValue>
         <CheckingCode>[1-2147483647]</CheckingCode>
         <ForceRestart>false</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
         <ParameterName>setParameter.cursorTimeoutMillis</ParameterName>
      </Parameter>
      <Parameter>
         <ParameterDescription>The maximum memory bytes that sort stage may use,
default is 33554432(i.e. 32MB)</ParameterDescription>
         <ParameterValue>33554432</ParameterValue>
         <CheckingCode>[33554432-268435456]</CheckingCode>
         <ForceRestart>false</ForceRestart>
         <ModifiableStatus>true</ModifiableStatus>
<ParameterName>setParameter.internalQueryExecMaxBlockingSortBytes</ParameterName>
      </Parameter>
   </RunningParameters>
   <EngineVersion>4.0</EngineVersion>
   <Engine>mongodb</Engine>
```

`JSON` 格式

```json
{
 "ConfigParameters": {
  "Parameter": [
   {
    "ParameterDescription": "The threshold in milliseconds at which the database profil
er considers a query slow, default is 100.",
    "ParameterValue": "200",
    "CheckingCode": "[0-65536]",
    "ForceRestart": false,
    "ModifiableStatus": true,
    "ParameterName": "operationProfiling.slowOpThresholdMs"
   }
```

]

```json
 },
 "RequestId": "3ADD0C7D-2D2A-4F15-88FF-E7AC9B9FDCC8",
 "RunningParameters": {
  "Parameter": [
   {
    "ParameterDescription": "",
    "ParameterValue": "zlib",
    "CheckingCode": "snappy|zlib|disabled",
    "ForceRestart": "true",
    "ModifiableStatus": "true",
    "ParameterName": "net.compression.compressors"
   },
   {
    "ParameterDescription": "The level of database profiling, which inserts information
about operation performance into the system.profile collection. 'off' for no profiling, 'slowOp' for only includes slow operations, 'all' for includes all operations, default is 'slowOp'.",
```

云数据库 MongoDB 版 s

```json
sowOp.,
    "ParameterValue": "slowOp",
    "CheckingCode": "off|slowOp|all",
    "ForceRestart": "false",
    "ModifiableStatus": "true",
    "ParameterName": "operationProfiling.mode"
   },
   {
    "ParameterDescription": "The threshold in milliseconds at which the database profil
er considers a query slow, default is 100.",
    "ParameterValue": "220",
    "CheckingCode": "[0-65536]",
    "ForceRestart": "false",
    "ModifiableStatus": "true",
    "ParameterName": "operationProfiling.slowOpThresholdMs"
   },
   {
    "ParameterDescription": "The expiration threshold in milliseconds for idle cursors
before MongoDB removes them; i.e. MongoDB removes cursors that have been idle for the s pecified cursorTimeoutMillis. default is 600000(i.e. 10 minutes)",
    "ParameterValue": "600000",
    "CheckingCode": "[1-2147483647]",
    "ForceRestart": "false",
    "ModifiableStatus": "true",
    "ParameterName": "setParameter.cursorTimeoutMillis"
   },
   {
    "ParameterDescription": "The maximum memory bytes that sort stage may use, default
is 33554432(i.e. 32MB)",
    "ParameterValue": "33554432",
    "CheckingCode": "[33554432-268435456]",
    "ForceRestart": "false",
    "ModifiableStatus": "true",
    "ParameterName": "setParameter.internalQueryExecMaxBlockingSortBytes"
   }
```

]

```json
 },
 "EngineVersion": "4.0",
 "Engine": "mongodb"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | InvalidDBInstanceC lass.NotFound | Specified DB instance class is not found. | 该实例规格不存在，请您检查输入的参数是否正确。 |
| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | 当前的实例类型不支持此操作。 |

#### ModifyParameters

云数据库 MongoDB 版调用本接口时，要求实例状态为运行中。 如果提交的修改参数中包含需要重启才能生效的参数，则提交后实例将自动重启。您可以

**说明**

调用**DescribeParameterTemplates**接口查询哪些是修改后需要重启才能生效的参数。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyParamete rs | 要执行的操作，取值：ModifyParameters。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| Parameters | String | 是 | {"operationProfil ing.slowOpThres holdMs":"300"} | 需要修改的参数及参数的取值，格式为 JSON串，例如： {“name”:”value”,”name”:”value2”} 。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中的Mongos节点ID或 Shard节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| CharacterType | String | 否 | db | 实例的角色类型。取值： db：shard角色 cs：config server角色 mongos：mongos角色 logic：分片集群实例 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 36923CC2-DDAB- 4B48-A144- DA92C1E19537 | 请求ID。 |

**示例**

请求示例云数据库 MongoDB 版

```
http(s)://mongodb.example.com/?Action=ModifyParameters &DBInstanceId=dds-bpxxxxxxxx &Parameters={"operationProfiling.slowOpThresholdMs":"300"}
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>36923CC2-DDAB-4B48-A144-DA92C1E19537</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "36923CC2-DDAB-4B48-A144-DA92C1E19537"
}
```

### 备份与恢复

#### DescribeBackupPolicy

调用DescribeBackupPolicy接口查询MongoDB实例的备份策略。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup Policy | 要执行的操作，取值：DescribeBackupPolicy。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupRetenti onPeriod | String | 7 | 备份保留天数。 |
| PreferredBack upPeriod | String | Monday,Wednesda y,Friday,Sunday | 备份周期。 Monday：周一。 Tuesday：周二。 Thursday：周四。 Friday：周五。 Saturday：周六。 Sunday：周日。 |

云数据库 MongoDB 版

| PreferredBack upTime | String | 20:00Z-21:00Z | 备份时间，格式为HH:mmZ-HH:mmZ（UTC时间）。 |
|---|---|---|---|
| PreferredNext BackupTime | String | 2020-05- 13T22:56Z | 下一次备份时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| RequestId | String | C2C283A1-1CC4- 4DD9-B985- 3811E0244A45 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeBackupPolicy DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<PreferredBackupPeriod>Monday,Wednesday,Friday,Sunday</PreferredBackupPeriod> <RequestId>C2C283A1-1CC4-4DD9-B985-3811E0244A45</RequestId> <PreferredBackupTime>20:00Z-21:00Z</PreferredBackupTime> <PreferredNextBackupTime>2020-05-13T22:56Z</PreferredNextBackupTime> <BackupRetentionPeriod>7</BackupRetentionPeriod>
```

`JSON` 格式

```json
{
    "PreferredBackupPeriod":"Monday,Wednesday,Friday,Sunday",
    "RequestId":"C2C283A1-1CC4-4DD9-B985-3811E0244A45",
    "PreferredBackupTime":"20:00Z-21:00Z",
    "PreferredNextBackupTime":"2020-05-13T22:56Z",
    "BackupRetentionPeriod":"7"
}
```

#### ModifyBackupPolicy

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyBackupPo licy | 要执行的操作，取值：ModifyBackupPolicy。 |

云数据库 MongoDB 版

| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 |
|---|---|---|---|---|
| PreferredBackup Period | String | 是 | Monday,Wednes day,Friday,Sund ay | 备份周期，取值： Monday：周一。 Tuesday：周二。 Wednesday：周三。 Thursday：周四。 Friday：周五。 Saturday：周六。 Sunday：周日。 说明如需传入多个值，多个值用英文逗号 （,）隔开。 |
| PreferredBackup Time | String | 是 | 03:00Z-04:00Z | 执行备份的时间，格式为HH:mmZ-HH:mmZ（UTC时间）。 说明时间范围限制为1小时。 |
| BackupRetentio nPeriod | String | 是 | 7 | 备份保留周期，值范围7-730。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 644A359C-B871- 4DD3-97B5- ED91EF5809C2 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=ModifyBackupPolicy &DBInstanceId=dds-bpxxxxxxxx &PreferredBackupPeriod=Monday,Wednesday,Friday,Sunday &PreferredBackupTime=03:00Z-04:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
   <RequestId>644A359C-B871-4DD3-97B5-ED91EF5809C2</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "644A359C-B871-4DD3-97B5-ED91EF5809C2"
}
```

#### CreateBackup

调用该接口时，要求实例状态为运行中。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateBackup | 要执行的操作，取值： CreateBackup。 |
| DBInstanceId | String | 是 | d-bpxxxxxxxx | 实例ID。 |
| BackupMethod | String | 否 | Logical | 实例的备份方式，取值： Logical：逻辑备份。 Physical：物理备份，默认为物理备份。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| BackupId | String | 5664xxxx | 备份ID。 |
| RequestId | String | 7016B12F-7F64- 40A4-BAFF- 013F02AC82FC | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=CreateBackup DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例云数据库 MongoDB 版 `XML` 格式

```xml
   <RequestId>7016B12F-7F64-40A4-BAFF-013F02AC82FC</RequestId>
   <BackupId>5664xxxx</BackupId>
```

`JSON` 格式

```json
{
    "RequestId": "7016B12F-7F64-40A4-BAFF-013F02AC82FC",
    "BackupId": "5664xxxx"
}
```

#### DescribeBackups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup s | 要执行的操作，取值：DescribeBackups。 |
| StartTime | String | 是 | 2019-03- 12T12:00Z | 查询开始时间，格式为yyyy-MM- ddTHH:mmZ（UTC时间）。 |
| EndTime | String | 是 | 2019-03- 13T12:00Z | 查询结束时间，必须晚于查询开始时间， 格式为yyyy-MM-ddTHH:mmZ（UTC时间）。 |
| DBInstanceId | String | 是 | dds-bpxxxxxxxx | 实例ID。 说明当本参数传入的是分片集群实例ID时，还需要传入NodeId参数。 |
| NodeId | String | 否 | d-bpxxxxxxxx | 分片集群实例中Shard节点ID。 说明当DBInstanceId参数传入的是分片集群实例ID时，本参数才可用。 |
| BackupId | String | 否 | 12345678 | 备份ID。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的的最大值，默认值为1。 |

云数据库 MongoDB 版

| PageSize | Integer | 否 | 30 | 每页记录数，取值： 30、50、100，默认值为30。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 页码。 |
| PageSize | Integer | 30 | 每页记录数。 |
| RequestId | String | 8925E66F-1971- 4C8C-90A7- F93BF1867E25 | 请求ID。 |
| TotalCount | Integer | 1 | 备份总个数。 |
| Backups | Array of Backup |  | 备份文件详情列表。 |
| Backup |  |  |  |
| BackupDBNam es | String | mongodbtest,new,t est | 备份的数据库名。 |
| BackupDownlo adURL | String | http://xxxxx.oss- cn- hangzhou.aliyuncs. com/xxxxx/hinsxxx xx data xxxxx.tar. _ _ gz | 备份文件的外网下载地址，若当前不可下载，则为空字符串。 |
| BackupEndTim e | String | 2019-03- 13T04:34:57Z | 本次备份结束时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| BackupId | Integer | 11111111 | 备份ID。 |
| BackupIntrane tDownloadURL | String | http://xxxxx.oss- cn-hangzhou- internal.example.c om/xxxxx/xxxxx.tar .gz | 备份文件的内网下载地址。 说明您可以在和此MongoDB实例连通的ECS（二者需属于同地域的经典网络或者在同一VPC内）上使用该地址下载目标备份文件。 |
| BackupMethod | String | Physical | 备份方式。 Snapshot：快照备份。 Physical：物理备份。 Logical：逻辑备份。 |

云数据库 MongoDB 版

| BackupMode | String | Automated | 备份模式。 Automated：系统自动备份。 Manual：手动备份。 |
|---|---|---|---|
| BackupSize | Long | 335520510 | 备份文件大小，单位为Byte。 |
| BackupStartTi me | String | 2019-03- 13T04:32:42Z | 本次备份开始时间，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 |
| BackupStatus | String | Success | 备份状态。 Success：备份成功。 Failed：备份失败。 |
| BackupType | String | FullBackup | 备份类型。 FullBackup：全量备份。 IncrementalBackup：增量备份。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeBackups &StartTime=2019-03-12T12:00Z &EndTime=2019-03-13T12:00Z &DBInstanceId=dds-bpxxxxxxxx
```

`&<`公共请求参数> 正常返回示例 `XML` 格式云数据库 MongoDB 版

```xml
<TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>8925E66F-1971-4C8C-90A7-F93BF1867E25</RequestId> <PageNumber>1</PageNumber> <Backups>
    <BackupMethod>Physical</BackupMethod>
    <BackupDownloadURL>http://xxxxx.oss-cn-
hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz</BackupDownloadURL>
    <BackupIntranetDownloadURL>http://xxxxx.oss-cn-hangzhou-
internal.example.com/xxxxx/xxxxx.tar.gz</BackupIntranetDownloadURL>
    <BackupSize>335520510</BackupSize>
    <BackupMode>Automated</BackupMode>
    <BackupEndTime>2019-03-13T04:34:57Z</BackupEndTime>
    <BackupStartTime>2019-03-13T04:32:42Z</BackupStartTime>
    <BackupType>FullBackup</BackupType>
    <BackupId>11111111</BackupId>
    <BackupDBNames>mongodbtest,new,test</BackupDBNames>
    <BackupStatus>Success</BackupStatus>
</Backups>
```

`JSON` 格式

```json
{
    "TotalCount":"1",
    "PageSize":"30",
    "RequestId":"8925E66F-1971-4C8C-90A7-F93BF1867E25",
    "PageNumber":"1",
    "Backups":[
        {
            "BackupMethod":"Physical",
            "BackupDownloadURL":"http://xxxxx.oss-cn-
hangzhou.aliyuncs.com/xxxxx/hinsxxxxx_data_xxxxx.tar.gz",
            "BackupIntranetDownloadURL":"http://xxxxx.oss-cn-hangzhou-
internal.example.com/xxxxx/xxxxx.tar.gz",
            "BackupSize":"335520510",
            "BackupMode":"Automated",
            "BackupEndTime":"2019-03-13T04:34:57Z",
            "BackupStartTime":"2019-03-13T04:32:42Z",
            "BackupType":"FullBackup",
            "BackupId":"11111111",
            "BackupDBNames":"mongodbtest,new,test",
            "BackupStatus":"Success"
        }
```

]

```
}
```

#### RestoreDBInstance

本接口仅适用于副本集实例，暂不支持单节点实例和分片集群实例。单节点实例可通过从备份点新建实例克隆当前实例，分片集群实例可通过调用CreateShardingDBInstance接口克隆当前实例。 云数据库 MongoDB 版调用该接口将覆盖当前实例的原有数据且无法恢复，请谨慎操作。

**说明**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RestoreDBInstan ce | 要执行的操作，取值：RestoreDBInstance。 |
| BackupId | Integer | 是 | 11111111 | 备份ID。 说明您可以通过调用DescribeBackups接口查询备份ID。 |
| DBInstanceId | String | 是 | dds- bp11501cd7b5* *** | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 973DCB8F-56B3- 4102-8777- 3A90495927F7 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=RestoreDBInstance &BackupId=11111111 &DBInstanceId=dds-bp11501cd7b5****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
   <RequestId>973DCB8F-56B3-4102-8777-3A90495927F7</RequestId>
```

`JSON` 格式

```json
{
 "RequestId": "973DCB8F-56B3-4102-8777-3A90495927F7"
}
```

云数据库 MongoDB 版

#### DescribeBackupDBs

在为MongoDB实例执行单库恢复前，您可以调用本接口查询指定的时间点或备份集内包含的数据库。

**说明**

调用本接口时，实例必须满足以下条件： 实例类型为副本集实例。 实例版本须为**3.0**、**3.4**、**4.0**或**4.2**版本。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeBackup DBs | 要执行的操作，取值：DescribeBackupDBs。 |
| SourceDBInstan ce | String | 是 | dds-bpxxxxxxxx | 待恢复数据的源实例ID。 |
| PageNumber | Integer | 否 | 1 | 页码，取值为大于0且不超过Integer数据类型的的最大值，默认值为1。 |
| PageSize | Integer | 否 | 30 | 每页可展示的记录数，取值： 30、50、100，默认值为30。 |
| RestoreTime | String | 否 | 2019-08- 22T12:00:00Z | 实例所需恢复的时间点，格式为yyyy-MM- ddTHH:mm:ssZ（UTC时间）。 说明本参数可取值为7天内的任意时间，但是须早于当前时间，且晚于实例的创建时间。 本参数和BackupId参数两者中必须传入一项。 |
| BackupId | String | 否 | 5664xxxx | 备份ID。 说明您可以通过调用DescribeBackups接口查询备份ID。 本参数和RestoreTime参数两者中必须传入一项。 |
| ResourceGroupI d | String | 否 | rg-axxxxxxxx | 资源组ID。 |

**返回数据**

云数据库 MongoDB 版

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Databases | Array of Database |  | 数据库列表。 |
| Database |  |  |  |
| DBName | String | mongodbtest | 数据库名。 |
| PageNumber | Integer | 1 | 页码。 |
| TotalCount | Integer | 5 | 查询结果中数据库的数量。 |
| PageSize | Integer | 30 | 每页可展示的记录数。 |
| RequestId | String | 1AF0AD89-ED4F- 44AD-B65F- BFC1D5CD9455 | 请求ID。 |

**示例**

请求示例

```
http(s)://mongodb.example.com/?Action=DescribeBackupDBs &SourceDBInstance=dds-bpxxxxxxxx &RestoreTime=2019-08-22T12:00:00Z
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>5</TotalCount> <Databases>
    <DBName>mongodbtest</DBName>
</Databases> <PageSize>30</PageSize> <RequestId>1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455</RequestId> <PageNumber>1</PageNumber>
```

`JSON` 格式云数据库 MongoDB 版

```json
{
    "TotalCount":"5",
    "Databases":[
        {
            "DBName":"mongodbtest"
        }
```

`],`

```json
    "PageSize":"30",
    "RequestId":"1AF0AD89-ED4F-44AD-B65F-BFC1D5CD9455",
    "PageNumber":"1"
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 403 | IncorrectDBInstanc eType | Current DB instance type does not support this operation. | 当前的实例类型不支持此操作。 |

### 实例状态表

本文列举实例状态以及状态说明。

| 实例状态 | 状态说明 |
|---|---|
| Creating | 创建中 |
| DBInstanceClassChanging | 升降级中 |
| DBInstanceNetTypeChanging | 内外网切换中 |
| Deleting | 删除中 |
| EngineVersionUpgrading | 迁移版本中 |
| GuardSwitching | 容灾切换中 |
| HASwitching | 主备切换中 |
| Importing | 数据导入中 |
| ImportingFromOthers | 数据库导入中 |
| LinkSwitching | 链路切换中 |
| MinorVersionUpgrading | 小版本升级中 |
| NET CREATING _ | 创建网络连接中 |
| NET DELETING _ | 删除网络连接中 |
| NodeCreating | 实例节点创建中 |
| NodeDeleting | 实例节点删除中 |

云数据库 MongoDB 版

| Rebooting | 重启中 |
|---|---|
| Restoring | 备份恢复中 |
| Running | 运行中 |
| SSLModifying | SSL变更中 |
| TempDBInstanceCreating | 临时实例创建中 |
| Transing | 迁移中 |
| TransingToOthers | 迁移数据库中 |

云数据库 MongoDB 版

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

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
| RoleArn | String | 是 | acs:ram::123456 789012****:role/ adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM 角色。 |
| RoleSessionNa me | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-） 和下划线（ ）。 _ |

云数据库 MongoDB 版

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 长度为1~1024个字符。 |

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | wyLTSmsyPGP1ohv vw8xYgB29dlGI8KM iH2pK**** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495** **:alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

云数据库 MongoDB 版操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**调用API获取STS AccessKey三元组**

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
if(Sti Util
```

iE

```
t( Rl))
```

t 云数据库 MongoDB 版

```
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
```

`//` 获取到`STS`三元组

```java
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: "
+ stsToken);
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

下列代码以调用ECS的 `DescribeZones` 接口为示例。 云数据库 MongoDB 版

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
```

`// "<yourRegionID>"`替换为真实的`RegionID` `// "<yourStsAccesskey>", "<yourStsAccessKeySecret>"`替换为上面获取到的`STS`三元组中

```xml
stsAk、stsSk
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

云数据库 MongoDB 版

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64 个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号 （.）、at（@）、短划线 （-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDurati on设置的时间。 |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
