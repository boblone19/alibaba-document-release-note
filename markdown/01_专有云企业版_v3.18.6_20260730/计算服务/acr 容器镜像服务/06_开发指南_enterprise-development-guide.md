---
title: "容器镜像服务 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 134
source_pdf: "06_开发指南_enterprise-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/acr/zh/enterprise-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 容器镜像服务 开发指南

## SDK参考

### 快速入门

#### 开发文档使用说明

本文为您介绍在使用专有云API进行开发工作时，如何查看所需要的产品文档。

**使用流程**

您可以按照以下流程图中步骤，判断自己所需要使用的开发文档。

**前提条件**

通过运维人员或运营管理员获取专有云的版本。

**操作步骤**

您可以通过阿里云专有云文档中心，获取需要的产品文档。
1. 通过浏览器打开专有云文档中心。
2. 根据专有云的版本单击**企业版**、**敏捷版**或**一体机**标签。
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

#### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云更一致的体验，自企业版V3.16.0 开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

|  | 说明调用API时，请在Header参数中增加组织ID <x-acs-organizationid> 和资源集ID <x-acs- resourcegroupid>， 指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID <x-acs-organizationid> ，则默认获取当前用户所属的组织。 不指定资源集ID <x-acs-resourcegroupid> ，则默认为空，如果指定资源集需要同时指定组织ID。 |  |  |
|---|---|---|---|
|  |  | <x-acs- |  |

4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。

### 准备工作

#### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

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

#### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

#### 获取AccessKey

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
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

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

#### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。更多STS说明请参见STS使用说明。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourRoleSessionName>，请替换为您当前实际的会话名称。 <yourRoleArn>，请替换为您实际的RAM Role。 <sts.aliyuns.com> ，请替换为实际的STS Endpoint。

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

`// "sts.aliyuns.com"` 请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`"<yourRoleSessionName>"`请您替换为实际值

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`Ram Role ARN`

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

3. 通过STS AccessKey三元组调用云产品的接口，下列代码以容器镜像服务高级版

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <accesskeyId>，请替换为您实际的STS Accesskey ID。 <accessKeySecret>，请替换为您实际的STS Accesskey Secret。 <securityToken>，请替换为您实际的STS SecurityToken。

```java
// This file is auto-generated, don't edit it. Thanks. package com.aliyun.sample; import com.aliyun.tea.*; import com.aliyun.cr20181201.*; import com.aliyun.cr20181201.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
    /**
```

* 使用`AK&SK`初始化账号`Client`

```
     * @param accessKeyId
     * @param accessKeySecret
     * @return Client
     * @throws Exception
```

`*/`

```
    public static com.aliyun.cr20181201.Client createClient(String accessKeyId, Strin
g accessKeySecret, String securityToken) throws Exception {
```

`// accessKeyId, accessKeySecret`请替换为前一步获取到的`STS`三元组中`AccessKeyID`、`AccessK`

```
eySecret和Security Token。
        Config config = new Config()
                // 您的AccessKey ID
                .setAccessKeyId(accessKeyId)
                // 您的AccessKey Secret
                .setAccessKeySecret(accessKeySecret)
                // 您的Security Token
                .setSecurityToken(securityToken);
```

`//` 访问的域名

```
        config.endpoint = "cr.cn-shanghai.aliyuncs.com";
        return new com.aliyun.cr20181201.Client(config);
    }
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.cr20181201.Client client = Sample.createClient("accessKeyId", "acc
essKeySecret", "securityToken");
        CreateNamespaceRequest createNamespaceRequest = new CreateNamespaceRequest();
```

`//` 复制代码运行请自行打印 `API` 的返回值

```
        client.createNamespace(createNamespaceRequest);
    }
}
```

#### 获取公共Header参数

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

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**弹性计算**>**容器镜像服务****ACR**。
3. 在实例列表中，单击专有云高级版实例。
4. 在**概览**页面中查看**实例****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

#### 获取容器镜像服务的SDK包

通过POP网关调用专有云API时，需使用容器镜像服务的SDK。本文为您介绍如何获取阿里云开发工具包 （SDK）。 软件开发工具包（SDK）包括代码以及示例，用户可以自行选择语言创建云应用。 目前SDK的语言支持：Java、Python、Go，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python、Go三种语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 SDK核心库推荐使用阿里云官网的SDK核心库，其内容所有云产品共用，且适用于专有云。

### 标准版SDK

#### Java SDK调用示例

##### 安装Java

**环境要求**

最低要求Java 6。 安装SDK核心库Core ，可以通过POM文件引入的方式来安装。 本文以4.5.21版本的SDK为例。

**说明**

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.21</version>
</dependency>
```

**安装容器镜像SDK**

在Maven项目文件中添加以下依赖： 本文以4.1.2版本的SDK为例。

**说明**

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-cr</artifactId>
  <version>4.1.2</version>
</dependency>
```

##### 使用CommonRequest进行调用

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile;
```

`/*`

```xml
pom.xml <dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>aliyun-java-sdk-core</artifactId>
  <version>4.5.16</version>
</dependency>
```

`*/`

```java
    public static void main(String[] args) {
        DefaultProfile profile = DefaultProfile.getProfile("cn-wl-e****", "<your-
access-key-id>", "<your-access-key-secret>");
        /** use STS Token
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",           // The region ID
            "<your-access-key-id>",       // The AccessKey ID of the RAM account
            "<your-access-key-secret>",   // The AccessKey Secret of the RAM account
            "<your-sts-token>");          // STS Token
        **/
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        //request.setProtocol(ProtocolType.HTTPS);
        request.setMethod(MethodType.GET);
        request.setDomain("cr.registry.inter.e****.shuguang.com");
        request.setVersion("2016-06-07");
        request.setUriPattern("/namespace/fc-example");
        request.putHeadParameter("Content-Type", "application/json");
        String requestBody = "" +
                "{}";
        request.setHttpContent(requestBody.getBytes(), "utf-8", FormatType.JSON);
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            e.printStackTrace();
        }
    }
}
```

#### Python SDK调用示例

**背景信息**

##### 安装Python SDK

**环境要求**

Python2.7或3.x 安装SDK核心库Core，使用pip安装包依赖:

```
pip install aliyun-python-sdk-core
```

**安装容器镜像SDK**

PyPI PIP

```
pip install aliyun-python-sdk-cr==4.1.2
```

PyPI Anaconda

```
conde install aliyun-python-sdk-cr=4.1.2
```

##### 使用CommonRequest进行调用

**前提条件**

目前专有云推荐使用CommonRequest进行调用，可以在Apsara Uni-manager运营控制台**产品** > **应用**
**服务** > **开发者门户**，选择**API****集成** > **SDK****示例**查看推荐SDK版本以及示例代码。

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**CommonRequest调用示例**

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential credentials = AccessKeyCredential('<your-access-key-id>', '<your-access-key-secret>')
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>',
'<your-sts-token>') client = AcsClient(region_id='cn-wl-e****', credential=credentials) request = CommonRequest() request.set_accept_format('json') request.set_method('GET') request.set_protocol_type('https') # https | http request.set_domain('cr.registry.inter.e****.shuguang.com') request.set_version('2016-06-07') request.add_header('Content-Type', 'application/json') request.set_uri_pattern('/namespace/fc-example') body = '''{}''' request.set_content(body.encode('utf-8')) response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding = 'utf-8'))
```

### 高级版SDK

#### Java SDK调用示例

##### 安装Java SDK

**环境要求**

最低要求Java 8 安装SDK核心库OpenAPI ，可以通过POM文件引入的方式来安装。 本文以0.0.19版本为例。

**说明**

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>tea-openapi</artifactId>
  <version>0.0.19</version>
</dependency>
```

**安装容器镜像SDK**

在Maven项目文件中添加以下依赖：

**说明**

本文以1.0.1版本为例。

```xml
<dependency>
  <groupId>com.aliyun</groupId>
  <artifactId>cr20181201</artifactId>
  <version>1.0.1</version>
</dependency>
```

##### 调用Java SDK

**操作步骤**

1. 初始化配置对象com.aliyun.teaopenapi.models.Config。
Config对象包含 `access_key_id` 、 `access_key_secret` 和 `endpoint` 等配置。

```
Config config = new Config()
```

`//` 您的`AccessKey ID`。

```
    .setAccessKeyId(accessKeyId)
    // 您的AccessKey Secret。
    .setAccessKeySecret(accessKeySecret);// 访问的域名。
config.endpoint = "cr-ee.cn-qingdao***.shuguang.com";
```

2. 实例化一个客户端，从com.aliyun.cr20181201.Client类生成对象client。
后续Request、Response从com.aliyun.cr20181201.models中获得。

```
Client client = new Client(config);
```

3. 创建对应API的Request 。
类的命名规则为API方法名加上Request。

```
GetArtifactBuildTaskRequest request = new GetArtifactBuildTaskRequest();
```

4. 设置请求类Request的参数。
通过Request类的属性设置必要的信息，即API中必须要提供的信息。 request.InstanceId = "test"; // 该参数值为假设值，请您根据实际情况进行填写。 request.BuildTaskId = "test"; // 该参数值为假设值，请您根据实际情况进行填写。
5. 通过client对象获得对应Request响应Response。

```java
GetArtifactBuildTaskResponse response = client.getArtifactBuildTask(request); System.out.println(new Gson().toJson(response.Body));
```

6. 调用Response中对应的属性获得返回的参数值。
本文以获取 `requestId` 为例。

```
String requestId = response.Body.requestId;
```

7. 使用catch()处理报错。

```
catch (Exception e) {
    e.printStackTrace();
}
```

**完整代码示例**

```java
// This file is auto-generated, don't edit it. Thanks. package com.aliyun.sample; import com.aliyun.tea.*; import com.aliyun.cr20181201.*; import com.aliyun.cr20181201.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
    /**
```

* 使用`AK&SK`初始化账号`Client`

```
     * @param accessKeyId
     * @param accessKeySecret
     * @return Client
     * @throws Exception
```

`*/`

```
    public static com.aliyun.cr20181201.Client createClient<String accessKeyId, String
accessKeySecret> throws Exception {
        Config config = new Config()
                // 您的AccessKey ID
                .setAccessKeyId<accessKeyId>
                // 您的AccessKey Secret
                .setAccessKeySecret<accessKeySecret>;
```

`//` 访问的域名

```
        config.endpoint = "cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com";
        return new com.aliyun.cr20181201.Client(config);
    }
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.cr20181201.Client client = Sample.createClient<"accessKeyId",
"accessKeySecret">;
        GetNamespaceRequest getNamespaceRequest = new GetNamespaceRequest()
                .setInstanceId("cri-pri****")
                .setNamespaceName("test12");
```

`//` 复制代码运行请自行打印 `API` 的返回值

```
        client.getNamespace(getNamespaceRequest);
    }
}
```

#### Python SDK调用示例

##### 安装Python SDK

**环境要求**

Python 3 安装SDK核心库OpenAPI ，使用pip安装包依赖：

```
pip install alibabacloud_tea_openapi>
```

**安装容器镜像SDK**

PyPI PIP

```
pip install alibabacloud_cr20181201==1.0.3
```

PyPI Anaconda

```
conde install alibabacloud_cr20181201=1.0.3
```

##### 调用Python SDK

**操作步骤**

1. 初始化配置对象alibabacloud_tea_openapi.Config。
Config对象包含 `access_key_id` 、 `access_key_secret` 和 `endpoint` 等配置。

```python
from alibabacloud_tea_openapi import models as open_api_models config = open_api_models.Config(
```

# 您的`AccessKey ID`。

```bash
    access_key_id=access_key_id,
    # 您的AccessKey Secret。
    access_key_secret=access_key_secret
```

)
# 访问的域名。

```
config.endpoint = 'cr.cn-hangzhou.aliyuncs.com'
```

2. 实例化一个客户端，从com.aliyun.cr20181201.Client类生成对象client。
后续Request、Response从com.aliyun.cr20181201.models中获得。

```python
from alibabacloud_cr20181201.client import Client as Client from alibabacloud_cr20181201 import models as models client = Client(config)
```

3. 创建对应API的Request。
方法的命名规则为Create加上API方法名再加上Request。
4. 设置请求类Request的参数。
通过设置Request类的属性设置参数，即API中必须要提供的信息。 `//` 该参数值为假设值，请您根据实际情况进行填写。

```
request.InstanceId = "test";
```

`//` 该参数值为假设值，请您根据实际情况进行填写。

```
request.BuildTaskId = "test";
```

5. 通过client对象获得对应Request响应Response。

```python
requestId = response.body.requestId print(requestId)
```

6. 调用Response中对应的属性获得返回的参数值。
本文以获取 `requestId` 为例。

```
String requestId = response.Body.requestId;
```

7. 使用try...except...处理报错。

```python
from Tea.exceptions import UnretryableException try:
    response = client.describe_images(request)
except UnretryableException as e:
    # Server Error
    print(e.inner_exception.code)
    print(e.inner_exception.message)
except Exception as e:
    print(e)
```

**完整代码示例**

```java
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys from typing import List from alibabacloud_cr20181201.client import Client as cr20181201Client from alibabacloud_tea_openapi import models as open_api_models from alibabacloud_cr20181201 import models as cr_20181201_models class Sample:
    def __init__(self):
        pass
    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> cr20181201Client:
        """
```

使用`AK&SK`初始化账号`Client`

```
        @param access_key_id:
        @param access_key_secret:
        @return: Client
```

```bash
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
```

)
# 访问的域名

```python
        config.endpoint = 'cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com'
        return cr20181201Client(config)
    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        get_namespace_request = cr_20181201_models.GetNamespaceRequest(
            instance_id='cri-pri****',
            namespace_name='test12'
```

)
# 复制代码运行请自行打印 `API` 的返回值

```
    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        get_namespace_request = cr_20181201_models.GetNamespaceRequest(
            instance_id='cri-pri****',
            namespace_name='test12'
```

)
# 复制代码运行请自行打印 `API` 的返回值

```
        await client.get_namespace_async(get_namespace_request)
if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

#### Go SDK调用示例

##### 安装Go SDK

**环境要求**

Go环境版本必须不低于1.10.x 安装SDK核心库OpenAPI 。

```
go get github.com/alibabacloud-go/darabonba-openapi/client
```

**安装容器镜像SDK**

推荐使用Go工具进行安装：

```
go get github.com/alibabacloud-go/cr-20181201
```

##### 调用Go SDK

**操作步骤**

1. 在代码中引入依赖包。

```java
import (
  cr "github.com/alibabacloud-go/cr-20181201/client"
  openapi "github.com/alibabacloud-go/darabonba-openapi/client"
```

)
2. 初始化配置对象&openapi.Config。
Config对象包含 `access_key_id` 、 `access_key_secret` 和 `endpoint` 等配置。

```
config := &openapi.Config{
```

`//` 您的`AccessKey ID`。

```
  AccessKeyId: accessKeyId,
  // 您的AccessKey Secret。
  AccessKeySecret: accessKeySecret,
}
```

`//` 访问的域名。

```
config.Endpoint = tea.String("cr.cn-hangzhou.aliyuncs.com")
```

3. 实例化一个客户端，从&cr.Client类生成对象client。

```
client, _ := cr.NewClient(config)
```

4. 创建对应API的Request。
方法的命名规则为API方法名再加上Request。
5. 设置请求Request的参数。
通过Request设置必要的信息，即API中必须要提供的信息。 `//` 该参数值为假设值，请您根据实际情况进行填写。

```
request.SetInstanceId("test")
```

`//` 该参数值为假设值，请您根据实际情况进行填写。

```
request.SetBuildTaskId("test")
```

6. 通过client对象获得对应Request响应Response。

```
response, err := client.GetArtifactBuildTask(request) fmt.Println(response)
```

7. 通过err可以处理请求报错。

```
if err != nil {
  fmt.Println(err)
  return
}
```

8. 调用Response获得返回的参数值。
本文以获取 `requestId` 为例。

```
fmt.Println(tea.StringValue(response.Body.ImageId))
```

**完整代码示例**

```java
// This file is auto-generated, don't edit it. Thanks. package main import (
  "os"
  cr20181201  "github.com/alibabacloud-go/cr-20181201/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
```

)

```
/**
```

* 使用`AK&SK`初始化账号`Client`

```
 * @param accessKeyId
 * @param accessKeySecret
 * @return Client
 * @throws Exception
```

`*/`

```
func CreateClient (accessKeyId *string, accessKeySecret *string) (_result *cr20181201.C lient, _err error) {
  config := &openapi.Config{
    // 您的AccessKey ID
    AccessKeyId: accessKeyId,
    // 您的AccessKey Secret
    AccessKeySecret: accessKeySecret,
  }
```

`//` 访问的域名

```
  config.Endpoint = tea.String("cr-ee.registry.cn-wl-en****.inter.en****.shuguang.com")
  _result = &cr20181201.Client{}
  _result, _err = cr20181201.NewClient(config)
  return _result, _err
} func _main (args []*string) (_err error) {
  client, _err := CreateClient(tea.String("accessKeyId"),
tea.String("accessKeySecret"))
  if _err != nil {
    return _err
  }
  getNamespaceRequest := &cr20181201.GetNamespaceRequest{
    InstanceId: tea.String("cri-pri****"),
```

```
    NamespaceName: tea.String("test12"),
  }
```

`//` 复制代码运行请自行打印 `API` 的返回值

```
  _, _err = client.GetNamespace(getNamespaceRequest)
  if _err != nil {
    return _err
  }
  return _err
} func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
  }
}
```

## 标准版API参考

### 容器镜像API调用方式

#### 公共请求参数

| 参数名称 | 说明 | 选项 |
|---|---|---|
| Authorization | 用于验证请求合法性的认证信息，采用 AccessKeyId:Signature 的形式。 | 必须 |
| Content-Length | RFC 2616中定义的HTTP请求内容长度。 | 必须 |
| Content-Type | RFC 2616中定义的HTTP请求内容类型。 | 必须 |
| Content-MD5 | HTTP协议消息体的128-bit MD5散列值转换成BASE64编码的结果。为了防止所有请求被篡改，建议所有请求都附加该信息。 | 必须 |
| Date | 请求的构造时间，目前只支持GMT 格式。如果与 MNS的服务器时间前后差异超过15分钟将返回本次请求非法。 | 必须 |
| Host | 访问Host值，例如： cr.cn- hangzhou.aliyuncs.com 。 | 必须 |
| Accept | 客户端需要的返回值类型，支持 application/json和 application/xml。 | 必须 |
| x-acs-version | API版本号。 | 必须 |
| x-acs-region-id | 地域（Region）指的是容器镜像所在的物理位置。 | 必须 |
| x-acs-signature-nonce | 唯一随机数，用于防止网络重放攻击。您在不同请求间要使用不同的随机数值。 | 必须 |
| x-acs-signature-method | 用户签名方式，目前只支持HMAC- SHA1。 | 必须 |

|  |  | cr.cn- | 必须 |
|---|---|---|---|
|  | hangzhou.aliyuncs.com |  |  |

**示例**

```
Authorization: acs ACSbW2iBbyX1Pk9N:mp/6Wdr18V3qAc5gbgsqMe/iB0c Content-Length: 0 Content-Type: application/json;charset=utf-8 Date: Wed, 23 May 2018 12:00:01 GMT Host: cr.cn-hangzhou.aliyuncs.com Accept: application/json x-acs-version: 2016-06-07 x-acs-region-id: cn-hangzhou x-acs-signature-nonce: f63659d4-10ac-483b-99da-ea8fde61eae3 x-acs-signature-version: 1.0 x-acs-signature-method: HMAC-SHA1 User-Agent: cr-sdk-python/3.0.0 (Darwin/15.2.0/x86_64;2.7.10)
```

**公共返回**

您发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码RequestId。

**示例**

XML示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<接口名称`+Response>` <!--返回请求标签`-->`

```xml
  <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON 示例：

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216"
```

`/*` 返回结果数据 `*/`

```
}
```

#### 请求结构

本文主要介绍发起容器镜像服务Open API请求时的结构。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求方法**

使用HTTP的PUT、 POST、 GET、 DELETE 等HTTP Method发送不同的请求。

**请求参数**

**请求编码**

请求及返回结果都使用 `UTF-8` 字符集进行编码。

#### 签名机制

为保证API的安全调用，在调用API时阿里云会对每个API请求通过签名进行身份验证。

**签名**

API签名包含两部分：公共请求头（HTTP协议Header参数和阿里云协议Header参数）和 CanonicalizedResource（规范资源），Body不计入签名。

| AccessKey ID |  | 和 | AccessKey Secret |  |
|---|---|---|---|---|
| 理），其中 |  |  |  | 用于标识访问 |

系统会对每个访问的请求进行验证，每个提交的请求都需要在请求中包含签名（Signature）信息。系统通过使用 `AccessKey ID` 和 `AccessKey Secret` 进行对称加密的方法来验证请求的发送者身份。如果计算出来的验证码和提供的一样，即认为该请求是有效的；否则请求将被拒绝处理，并返回HTTP403错误。 请求要求将签名包含在HTTP Header中，格式为 `Authorization: acs [Access Key Id]:`

```
[Signature] 。
```

**签名计算方法**

签名计算方法如下：

```
Signature = base64(hmac-sha1(VERB + "\n"
            + ACCEPT + "\n"
            + Content-MD5 + "\n"
            + Content-Type + "\n"
            + Date + "\n"
            + CanonicalizedHeaders + "\n"
            + CanonicalizedResource))
```

| VERB |  |
|---|---|
| Accept |  |
| Content-MD5 |  |
| Content-Type |  |
| Date | 表示此次 |

`GMT` 。 `CanonicalizedHeaders` 表示HTTP中以 `x-acs-` 开始的字段组合。 `CanonicalizedResource` 表示HTTP所请求资源的URI（统一资源标识符）。比如 `/namespaces` 。

**CanonicalizedHeaders**

CanonicalizedHeaders（即以 `x-acs-` 开头的Header）在签名验证前需要符合以下规范：

| x-acs- 为前缀的HTTP请求头的名转换为 x-acs-meta-name: TaoBao |  | 为前缀的HTTP请求头的名 |
|---|---|---|

2. 如果一个公共请求头的值部分过长，则需要处理其中的 \t 、 \n 、 \r 、 \f 分隔符，将其替换
为英文半角的空格。
3. 将上一步得到的所有HTTP阿里云规范头按照字典序进行升序排列。
4. 删除请求头和内容之间分隔符两端出现的任何空格。比如将 `x-acs-meta-name: TaoBao,Alipay` 转换

```
为 x-acs-meta-name:TaoBao,Alipay 。
```

5. 将所有的头和内容用 \n 分隔符分隔拼成最后的CanonicalizedHeaders。

**CanonicalizedResource**

CanonicalizedResource表示客户想要访问资源的规范描述，需要将子资源和qurey一同按照字典序，从小到大排列并以&为分隔符生成子资源字符串（ ? 后的所有参数）。

```
http://cr.cn-hangzhou.aliyuncs.com/repository?name=repository1&namespace=namespace1
```

CanonicalizedResource应该为：

```
/repository?name=repository1&namespace=namespace1
```

### 命名空间管理

#### CreateNamespace

**请求信息**

**请求行RequestLine**

```
PUT /namespace HTTP/1.1
```

**请求行参数URI Param**

无

**特有请求头RequestHead**

无

**请求体RequestBody**

Request Body:

```json
{
    "Namespace": {
        "Namespace": "String",
    }
}
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Namespace | String | 是 | 命名空间名称，长度限制 2~30，支持小写字母、 数字、中划线（-）、下划线（ ） （不能以中划线 _ 和下划线开头）。 |

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data":{
        "namespaceId":Long
    },
    "requestId":"String"
}
```

**示例**

**请求示例**

```
PUT /namespace HTTP/1.1
```

<公共请求头>

```json
{
    "Namespace": {
        "Namespace": "aliyun",
    }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "589EA3A1-9A67-4B82-95E5-11B1740178D1"
}
```

#### DeleteNamespace

调用DeleteNamespace删除一个已有命名空间，注意这个操作会将存在于该命名空间下的所有仓库以及所有仓库下的镜像一并删除。

**请求信息**

**请求行RequestLine**

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Namespace | String | 是 | 命名空间名称，长度限制 2~30，支持小写字母、 数字、中划线（-）、下划线（ ） （不能以中划线 _ 和下划线开头）。 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data":{},
    "requestId":"string"
}
```

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "CBC151B2-C9B6-4393-9A7F-712C920F1DC7"
}
```

#### UpdateNamespace

**请求信息**

**请求行RequestLine**

```
POST /namespace/[Namespace] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Namespace | String | 是 | 命名空间名称 |

**特有请求头RequestHead**

无

**请求体RequestBody**

```json
{
    "Namespace": {
        "AutoCreate": Boolean,
        "DefaultVisibility": String
    }
}
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| AutoCreate | Boolean | 是 | 是否自动创建仓库 |
| DefaultVisibility | String | 是 | 默认的仓库属性 |

**返回信息**

**返回行ResponseLin**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {},
    "requestId": "string"
}
```

**示例**

**请求示例**

```
POST /namespace/[Namespace] HTTP/1.1
```

<公共请求头>

```json
{
    "Namespace": {
        "AutoCreate": false,
        "DefaultVisibility": "PUBLIC"
    }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
  "data": {},
    "requestId": "AL103117-2140-4A69-AC1A-BE69N040D01A"
}
```

#### GetNamespace

**请求信息**

**请求行RequestLine**

**请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Namespace | String | 是 | 命名空间名称，长度限制 2~30，支持小写字母、 数字、中划线（-）、下划线（ ）（不能以中划线和 _ 下划线开头）。 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
        "namespace": {
            "namespace": "String",
            "authorizeType": "String",
            "defaultVisibility": "String",
            "autoCreate": "Boolean",
            "namespaceStatus": "String"
        }
    },
    "requestId": "String"
}
```

**返回参数**

| 名称 | 类型 | 描述 |
|---|---|---|
| namespace | String | 命名空间名称。 |
| authorizeType | String | 请求用户对该命名空间的操作权限， 仅限于控制台授权的情况。 |
| defaultVisibility | String | 在该命名空间下创建仓库的默认可见性。 |
| autoCreate | String | 是否允许推送镜像自动创建对应名称的仓库。如果关闭则需要先创建仓库，然后再推送镜像。 |
| namespaceStatus | String | 命名空间状态（NORMAL、 DELETING）。 |

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
        "namespace": {
            "namespace": "aliyun",
            "authorizeType": "ADMIN",
            "defaultVisibility": "PRIVATE",
            "autoCreate": true,
            "namespaceStatus": "NORMAL"
        }
    },
    "requestId": "19228CE5-4905-4A24-A2C1-E774F32CCC31"
}
```

#### GetNamespaceList

**请求信息**

**请求行RequestLine**

**请求行参数URI Param**

无

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
        "namespace": [
            {
                "namespace": "String",
                "authorizeType": "String",
                "namespaceStatus": "String"
            }
```

]

```json
    },
    "requestId": "string"
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| namespace | String | 命名空间名称。 |
| authorizeType | String | 请求用户对该命名空间的操作权限， 仅限于控制台授权的情况。 |
| namespaceStatus | String | 命名空间状态（NORMAL、 DELETING）。 |

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
        "namespaces": [
            {
                "namespace": "aliyun",
                "authorizeType": "ADMIN",
                "namespaceStatus": "NORMAL"
            },
            {
                "namespace": "alibaba",
                "authorizeType": "ADMIN",
                "namespaceStatus": "NORMAL"
            }
```

]

```json
    },
    "requestId": "AB034FC3-27E8-4E34-958B-0944E369270B"
}
```

### 镜像仓库管理

#### CreateRepo

**请求信息**

**请求行RequestLine**

```
PUT /repos HTTP/1.1
```

**请求行参数URI Param**

无

**特有请求头RequestHead**

无

**请求体RequestBody**

Request Body:

```json
{
       "Repo": {
           "RepoNamespace": "String" //必填 2~30,
           "RepoName": "String" //必填 2~30,
           "Summary": "String" //必填 1~100,
           "Detail": "String" //选填 *~2000 支持Markdown语法,
           "RepoType": "String" //必填枚举(PRIVATE PUBLIC),
       }
   }
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 仓库所属命名空间。长度限制2~30，支持小写字母、数字、短划线（-）、 下划线（ ）（不能以短划 _ 线和下划线开头）。 |
| RepoName | String | 是 | 仓库名称。长度限制 1~64，支持小写字母、 数字、短划线（-）、下划线（ ） （不能以短划线 _ 和下划线开头）。 |
| Summary | String | 是 | 仓库大致信息。长度限制 1~100。 |
| Detail | String | 否 | 仓库具体信息，支持 MarkDown格式，长度限制2000。 |

| RepoType | String | 是 | 枚举（PRIVATE、 PUBLIC），公有仓库支持匿名下载，私有仓库必须登录后下载。 |
|---|---|---|---|

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {},
    "requestId": "String"
}
```

**示例**

**请求示例**

```
PUT /repos HTTP/1.1
```

<公共请求头>

```json
{
    "repo": {
        "RepoNamespace": "aliyun",
        "RepoName": "Tengine",
        "Summary": "This is Aliyun Nginx",
        "RepoType": "PUBLIC"
    }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "80705201-FE46-4C08-AE30-FD50F5930993"
}
```

#### DeleteRepo

调用DeleteRepo删除一个已有仓库，注意这个操作会将存在于该仓库下的所有镜像一并删除。

**请求信息**

**请求行RequestLine**

```
DELETE /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 需要删除的仓库的命名空间名称。长度限制 2~30，支持小写字母、 数字、短划线（-）、下划线（ ） （不能以短划线 _ 和下划线开头）。 |
| RepoName | String | 是 | 需要删除的仓库的仓库名称。长度限制1~64，支持小写字母、数字、短划线（-）、下划线（ ） _ （不能以短划线和下划线开头）。 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data":{},
    "requestId":"string"
}
```

**示例**

**请求示例**

```
DELETE /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "7BF6D761-E7F8-454C-A235-983E5D183B4E"
}
```

#### UpdateRepo

**请求信息**

**请求行RequestLine**

```
POST /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |

**特有请求头RequestHead**

无

**请求体RequestBody**

```json
{
    "Repo": {
        "Summary": "String",
        "Detail": "String",
        "RepoType": "String"
    }
}
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Summary | String | 是 | 摘要信息 |
| Detail | String | 否 | 详细描述信息，支持 Markdown语法 |
| RepoType | String | 是 | 仓库性质，取值： PRIVATE、PUBLIC |

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {},
    "requestId": "String"
}
```

**示例**

**请求示例**

```
POST /repos/[RepoNamespace]/[RepoName] HTTP/1.1
```

<公共请求头>

```json
{
    "Repo": {
        "Summary": "Test repository",
        "Detail": "This is a test repository",
        "RepoType": "PRIVATE"
    }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "F3103017-5928-4A69-AC1A-BE69A840D01A"
}
```

#### GetRepoTag

**请求信息**

**请求行RequestLine**

```
GET /repos/[RepoNamespace]/[RepoName]/tag/[Tag] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |

| RepoName | String | 是 | 仓库名称 |
|---|---|---|---|
| Tag | String | 是 | 镜像标签 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**返回体ResponseBody**

```json
{
    "imageUpdate": 1578625336000,
    "imageId": "6f08feb0be92c8ed2cc5b3e563313d2c08e468c1aa40d06908634884f236****",
    "requestId": "9AFB10K1-2301-4B00-A817-93249204****",
    "digest": "110acd135b0b71c38f10a6db02b0318d6ec731ec318cbfc5dadc4cc182b54052",
    "tag": 1,
    "imageSize": 558063443,
    "imageCreate": 1577445220000,
    "status": "NORMAL"
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| imageUpdate | Long | 镜像更新时间 |
| imageCreate | Long | 镜像创建时间 |
| imageId | String | 镜像ID |
| imageSize | String | 镜像大小 |
| requestId | String | 请求ID |
| digest | String | 镜像的sha256 |
| tag | String | 镜像标签 |
| status | String | 镜像状态 |

**示例**

**请求示例**

```json
GET /repos/RepoNamespace/RepoName/tags/Tag HTTP/1.1 公共请求头 { "RepoName": "test", "RepoNamespace": "test", "Tag": "1.0" }
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "imageUpdate": 1578625336000,
    "imageId": "6f08feb0be92c8ed2cc5b3e563313d2c08e468c1aa40d06908634884f236****",
    "requestId": "",
    "digest": "110acd135b0b71c38f10a6db02b0318d6ec731ec318cbfc5dadc4cc182b54052",
    "tag": 1,
    "imageSize": 558063443,
    "imageCreate": 1577445220000,
    "status": "NORMAL"
}
```

#### GetRepo

**请求信息**

**请求行RequestLine**

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{ "data":{
    "repo": {
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
        },
        "regionId": String,
        "repoStatus": String,
        "detail": String,
        "repoAuthorizeType": String
    }
}, "requestId": string
    }
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| summary | String | 摘要信息 |
| gmtCreate | Long | 创建时间 |
| gmtModified | Long | 修改时间 |
| repoNamespace | String | 仓库所在的命名空间名称 |
| repoName | String | 仓库名称 |
| repoBuildType | String | 构建类型 |
| repoType | String | 仓库类型 |
| repoDomainList | Array | 仓库域名列表 |
| regionId | String | 区域 |
| repoStatus | String | 仓库状态 |
| detail | String | 仓库详情 |
| repoAuthorizeType | String | 仓库权限 |

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
 "data":{
     "repo": {
       "summary": "test",
       "gmtCreate": 1524663834000,
       "gmtModified": 1524663871000,
       "repoNamespace": "test",
       "repoName": "test",
       "repoBuildType": "AUTO_BUILD",
       "repoType": "PUBLIC",
       "repoDomainList": {
         "public": "registry.cn-hangzhou.aliyuncs.com",
         "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
       },
       "regionId": "cn-hangzhou",
       "repoStatus": "NORMAL",
       "detail": "",
       "repoAuthorizeType": "ADMIN"
     }
},
 "requestId": "B21BE190-08BA-41B6-B8B5-CA4029F1CC58"
}
```

#### GetRepoList

**请求信息**

**请求行RequestLine**

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Status | String | 是 | 仓库状态 |
| RepoNamePrefix | String | 是 | 仓库名称前缀 |
| Page | Integer | 否 | 当前页 |
| PageSize | Integer | 否 | 每页显示记录数 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{ "data": {
    "total": Integer,
    "repos": [{
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
        },
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }, {
        "summary": String,
        "repoId": Long,
        "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
        },
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }],
    "pageSize": Integer,
    "page": Integer
}, "requestId": String }
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| summary | String | 摘要信息 |
| repoId | Long | 仓库唯一标识ID |
| gmtCreate | Long | 创建时间 |
| gmtModified | Long | 修改时间 |

| repoNamespace | String | 仓库所在的命名空间名称 |
|---|---|---|
| repoName | String | 仓库名称 |
| repoBuildType | String | 仓库构建类型 |
| repoType | String | 仓库类型 |
| repoDomainList | Array | 仓库域名列表 |
| regionId | String | 区域 |
| repoStatus | String | 仓库状态 |
| repoAuthorizeType | String | 仓库权限 |
| page | Integer | 当前页 |
| pageSize | Integer | 每页显示记录数 |
| total | Integer | 总记录数 |

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{ "data": {
    "total": 2,
    "repos": [{
        "summary": "测试1",
        "repoId": 00001,
        "gmtModified": 1524663871000,
        "repoNamespace": "test1",
        "repoName": "test_repo_1",
        "gmtCreate": 1524663834000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PUBLIC",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
        },
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }, {
        "summary": "测试2",
        "repoId": 00002,
        "gmtModified": 1487319003000,
        "repoNamespace": "test2",
        "repoName": "测试2",
        "gmtCreate": 1487319003000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PRIVATE",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
        },
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }],
    "pageSize": 20,
    "page": 1
}, "requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E" }
```

#### GetRepoListByNamespace

**请求信息**

**请求行RequestLine**

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Status | String | 是 | 仓库状态 |
| RepoNamespace | String | 是 | 仓库所在的命名空间 |
| RepoNamePrefix | String | 是 | 仓库名称前缀 |
| Page | Integer | 否 | 当前页 |
| PageSize | Integer | 否 | 每页显示记录数 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{ "data": {
    "total": Integer,
    "repos": [{
        "summary": String,
        "repoId": Long,
    "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
        },
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }, {
    "summary": String,
        "repoId": Long,
    "gmtCreate": Long,
        "gmtModified": Long,
        "repoNamespace": String,
        "repoName": String,
        "repoBuildType": String,
        "repoType": String,
        "repoDomainList": {
            "public": String,
            "vpc": String
        },
        "regionId": String,
        "repoStatus": String,
        "repoAuthorizeType": String
    }],
    "pageSize": Integer,
    "page": Integer
}, "requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E" }
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| summary | String | 摘要信息 |
| repoId | Long | 仓库唯一标识ID |
| gmtCreate | Long | 创建时间 |
| gmtModified | Long | 修改时间 |

| repoNamespace | String | 仓库所在的命名空间名称 |
|---|---|---|
| repoName | String | 仓库名称 |
| repoBuildType | String | 仓库构建类型 |
| repoType | String | 仓库类型 |
| repoDomainList | Array | 仓库域名列表 |
| downloads | Long | 仓库下载量 |
| regionId | String | 区域 |
| logo | String | 仓库图标 |
| repoStatus | String | 仓库状态 |
| repoAuthorizeType | String | 仓库权限 |
| Page | Integer | 当前页 |
| PageSize | Integer | 每页显示记录数 |
| total | Integer | 总记录数 |

**示例**

**请求示例**

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{ "data": {
    "total": 2,
    "repos": [{
        "summary": "测试1",
        "repoId": 00001,
        "gmtModified": 1524663871000,
        "repoNamespace": "test",
        "repoName": "test_repo_1",
        "gmtCreate": 1524663834000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PUBLIC",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
        },
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }, {
        "summary": "测试2",
        "repoId": 00002,
        "gmtModified": 1487319003000,
        "repoNamespace": "test",
        "repoName": "test_repo_2",
        "gmtCreate": 1487319003000,
        "repoBuildType": "AUTO_BUILD",
        "repoType": "PRIVATE",
        "repoDomainList": {
            "public": "registry.cn-hangzhou.aliyuncs.com",
            "vpc": "registry-vpc.cn-hangzhou.aliyuncs.com"
        },
        "regionId": "cn-hangzhou",
        "repoStatus": "NORMAL",
        "repoAuthorizeType": "ADMIN"
    }],
    "pageSize": 20,
    "page": 1
}, "requestId": "F11E3C4C-LO9Q-4D11-B7C5-5EFCA8E7CA2E" }
```

#### GetRepoTags

**请求信息**

**请求行RequestLine**

```
GET /repos/[RepoNamespace]/[RepoName]/tags HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |
| Page | Integer | 否 | 当前页 |
| PageSize | Integer | 否 | 每页显示记录数 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{ "data": {
 "total": Integer,
 "pageSize": Integer,
 "page": Integer,
 "tags": [{
   "imageUpdate": Long,
    "imageCreate": Long,
   "imageId": String,
   "digest": String,
   "imageSize": Long,
   "tag": String,
   "status": String
 }, {
   "imageUpdate": Long,
   "imageCreate": Long,
   "imageId": String,
   "digest": String,
   "imageSize": Long,
   "tag": String,
   "status": String
 }]
}, "requestId": "9AFB10K1-2301-4B00-A817-932492040126" }
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| imageUpdate | Long | 镜像更新时间 |
| imageCreate | Long | 镜像创建时间 |
| imageId | String | 镜像ID |
| digest | String | 镜像的sha256 |
| imageSize | Long | 镜像大小 |
| tag | String | 镜像标签 |
| status | String | 镜像状态 |
| page | Integer | 当前页 |
| pageSize | Integer | 每页显示记录数 |
| total | Integer | 总记录数 |

**示例**

**请求示例**

```
GET /repos/[RepoNamespace]/[RepoName]/tags HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
   "total": 2,
   "pageSize": 30,
   "page": 1,
   "tags": [{
     "imageUpdate": 1514432549000,
     "imageId": "2842876c9b98f8c7607c1123ks18ff040b76a1d932c6d60c96aa3c283bd221cd",
     "digest": "83414d2c3b04e0lo1q7693e31aeca95b82c61949ea8de858579bf16bd92490c6",
     "imageSize": 715764,
     "tag": "new",
     "imageCreate": 1514432549000,
     "status": "NORMAL"
   }, {
     "imageUpdate": 1514372113000,
     "imageId": "414e6daa772a8cd5dfloqpe503e6e313c372d2e15958ab649709daf9b1065479",
     "digest": "fcf39ed78ef0fa27bcc74713b85259alop1b12e6a201e3083af50fd8eda1cbe1",
     "imageSize": 715653,
     "tag": "asdf",
     "imageCreate": 1514372044000,
     "status": "NORMAL"
   }]
 },
 "requestId": "9AFB52D3-6631-4B00-A857-932492097726"
}
```

### 镜像管理

#### DeleteImage

**请求信息**

**请求行RequestLin**

```
DELETE /repos/[RepoNamespace]/[RepoName]/tags/[Tag] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |

| RepoName | String | 是 | 仓库名称 |
|---|---|---|---|
| Tag | String | 是 | 镜像版本 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data":{},
    "requestId":"string"
}
```

**示例**

**请求示例**

```
DELETE /repos/[RepoNamespace]/[RepoName]/tags/[Tag] HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "7BF6D761-E7F8-454C-A235-983E5D183B4E"
}
```

#### GetImageManifest

**请求信息**

**请求行RequestLine**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/manifest HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |
| Tag | String | 是 | 镜像版本 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
  "data": {
    "manifest": {
      "name": "String",
      "fsLayers": "Array",
      "history": "Array",
      "signatures": "Array",
      "architecture": "String",
      "tag": "String",
      "schemaVersion": "Integer"
    }
  },
  "requestId": "String"
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| name | String | 镜像名称（命名空间或仓库名） |
| fsLayers | String | 镜像每层的sha256值 |

| history | Array | schema v1兼容的非结构化历史数据列表 |
|---|---|---|
| signatures | Array | 镜像签名数据 |
| architecture | String | 镜像架构 |
| tag | String | 镜像版本（Tag） |
| schemaVersion | Integer | schema版本（1、2 分别代表 manifest v2 schema1和 manifest v2 schema2） |

**示例**

**请求示例**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/manifest HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
  "data": {
    "manifest": {
      "name": "testNamespace/testRepo",
      "fsLayers": [{
        "blobSum": "sha256:a"
      }],
      "history": [{
        "v1Compatibility": {
          "parent": "b",
          "os": "linux",
          "created": "2018-01-01T00:00:00.000000001Z",
          "container_config": {},
          "id": "c",
          "config": {},
          "docker_version": "17.12.0-ce",
          "architecture": "amd64"
        }
      }],
      "signatures": [{
        "signature": "e",
        "header": {
          "alg": "ES256",
          "jwk": {}
        },
        "protected": "f"
      }],
      "architecture": "amd64",
      "tag": "tag1",
      "schemaVersion": 1
    }
  },
  "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
}
```

#### GetImageLayer

**请求信息**

**请求行RequestLine**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/layers HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

| RepoNamespace | String | 是 | 命名空间名称 |
|---|---|---|---|
| RepoName | String | 是 | 仓库名称 |
| Tag | String | 是 | 镜像版本 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
      "image": {
        "repoNamespace": "String",
        "repoName": "String",
        "layers": "Array",
        "tag": "String",
        "region": "String"
      }
    },
    "requestId": "String"
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| repoNamespace | String | 命名空间名称 |
| repoName | String | 镜像仓库命名称 |
| layers | Array | 镜像层信息 |
| tag | String | 镜像版本（Tag） |
| region | String | 镜像仓库地域 |

**示例**

**请求示例**

```
GET /repos/[RepoNamespace]/[RepoName]/tags/[Tag]/layers HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
      "image": {
        "repoNamespace": "testNamespace",
        "repoName": "testRepo",
        "layers": [{
          "layerCMD": "file:a in /TEMP",
          "blobDigest": "sha256:b",
          "blobSize": 1000,
          "layerInstruction": "COPY",
          "layerIndex": 2
        }, {
          "layerCMD": "[\"bash\"]",
          "blobDigest": "sha256:c",
          "blobSize": 32,
          "layerInstruction": "CMD",
          "layerIndex": 1
        }, {
          "layerCMD": "file:e in /",
          "blobDigest": "sha256:f",
          "blobSize": 52608285,
          "layerInstruction": "ADD",
          "layerIndex": 0
        }],
        "tag": "latest",
        "region": "cn-hangzhou"
      }
    },
    "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
}
```

### 触发器管理

#### CreateRepoWebhook

**请求信息**

**请求行RequestLine**

```
PUT /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 仓库所属命名空间 |
| RepoName | String | 是 | 仓库名称 |

**特有请求头RequestHead**

无

**请求体RequestBody**

```json
Request Body: {
    "Webhook": {
        "WebhookName": "String" 必填,
        "WebhookUrl": "String" 必填,
        "TriggerType": "String" 必填枚举(ALL TAG_REG_EXP TAG_LIST),
    }
}
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| WebhookName | String | 是 | 触发器名称。 |
| WebhookUrl | String | 是 | 镜像推送时触发的URL。 |
| TriggerType | String | 是 | 镜像推送时触发器的触发类型，枚举(ALL、 TAG REG EXP、 _ _ TAG LIST)，可以选择镜 _ 像版本触发，正则表达式触发，以及支持两者同时触发。 |

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
        "webhookId": "String"
    },
    "requestId": "String"
}
```

**示例**

**请求示例**

```
PUT /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

<公共请求头>

```json
{
    "Webhook": {
        "WebhookName": "MyTrigger",
        "WebhookUrl": "https://www.****.com",
        "TriggerType": "ALL"
    }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
        "webhookId": "39762"
    },
    "requestId": "3666F8EA-1468-4BEA-883B-FC60A651A609"
}
```

#### DeleteRepoWebhook

**请求信息**

**请求行RequestLine**

```
DELETE /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 仓库所属命名空间，应该从您已申请的命名空间中选取。 |
| RepoName | String | 是 | 仓库名称。 |
| WebhookId | Long | 是 | 仓库的触发器ID信息。 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**请求体解析**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {},
    "requestId": "String"
}
```

**示例**

**请求示例**

```
DELETE /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {},
    "requestId": "639F1195-56D9-49B7-BC47-B3BFCC9ED1C9"
}
```

#### GetRepoWebhook

**请求信息**

**请求行RequestLine**

```
GET /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |

**特有请求头RequestHead**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
        "webhooks":[
            {
                "webhookId": Long,
                "triggerTag": String,
                "webhookName": String,
                "triggerType": String,
                "webhookUrl": String
            }
```

]

```json
    },
    "requestId": String
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| webhookId | Long | webhook ID |
| triggerTag | String | 触发Tag |
| webhookName | String | webhook名 |
| triggerType | String | 触发方式 |
| webhookUrl | String | 触发url |
| syncTaskId | String | 同步任务ID |
| RequestId | String | 唯一请求ID |

**示例**

**请求示例**

```
GET /repos/[RepoNamespace]/[RepoName]/webhooks HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
        "webhooks":[
            {
                "webhookId": 39726,
                "triggerTag": "",
                "webhookName": "justForTest",
                "triggerType": "ALL",
                "webhookUrl": "https://www.****.com"
            }
```

]

```json
    },
    "requestId": "A86AB63A-758B-4FD9-9CB1-1421083A2EF5"
}
```

#### UpdateRepoWebhook

**请求信息**

**请求行RequestLine**

```
POST /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

**请求行参数URI Param**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| RepoNamespace | String | 是 | 命名空间名称 |
| RepoName | String | 是 | 仓库名称 |
| WebhookId | String | 是 | 触发器ID |

**特有请求头RequestHead**

无

**请求体RequestBody**

```json
{
   "Webhook": {
      "WebhookName": "String",
      "WebhookUrl": "String",
      "TriggerName": "String",
      "TriggerUrl": "String",
      "TriggerType": "String"
   }
}
```

**请求体解析**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| WebhookName | String | 是 | 仓库触发器名称。长度限制2~30，支持小写字母、数字、下划线（ ） _ (不能以下划线开头）。 |
| WebhookUrl | String | 是 | 仓库触发器 URL。长度限制1~1024，支持小写字母、数字、短划线（-）、 下划线（ ） （不能以短 _ 划线和下划线开头）。 |

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
    },
    "requestId": "String"
}
```

**返回体解析**

无

**示例**

**请求示例**

```
POST /repos/[RepoNamespace]/[RepoName]/webhooks/[WebhookId] HTTP/1.1
```

<公共请求头>

```json
{
   "Webhook": {
      "WebhookName": "justForTest",
      "WebhookUrl": "https://www.****.com",
      "TriggerName": "justForTest",
      "TriggerUrl": "https://www.****.com",
      "TriggerType": "ALL"
   }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
    },
    "requestId": "8DBD3292-A232-44F6-93DC-B30D70AF54E9"
}
```

### 访问凭证管理

#### GetAuthorizationToken

返回用于登录Registry的临时账号和临时密码，临时密码的有效时间为1小时，若使用STS方式请求时，临时密码的有效时间等同于本次请求STS Token的有效时间。

**权限说明**

| 调用方式 | 权限说明 |
|---|---|
| 主账号 | 使用临时Token登录Registry的权限等同于主账号使用用户名和密码登录 Registry的权限。 |
| 子账号 | 使用临时Token登录Registry的权限等同于子账号使用用户名和密码登录 Registry的权限。 |
| STS | 使用临时Token登录Registry的权限由角色的策略决定。 |

**请求信息**

**请求行RequestLine**

```
Get /tokens HTTP/1.1
```

**请求行参数URI Param**

无

**特有请求头RequestHeadI Param**

无

**请求体RequestBody**

无

**返回信息**

**返回行ResponseLine**

```
HTTP/1.1 200 OK
```

**特有返回头ResponseHead**

无

**返回体ResponseBody**

```json
{
    "data": {
        "authorizationToken": "String",
        "tempUserName": "String",
        "expireDate": Long
    },
    "requestId": "String"
}
```

**返回体解析**

| 名称 | 类型 | 描述 |
|---|---|---|
| authorizationToken | String | 用于登录Registry的密码 |
| tempUserName | String | 用于登录Registry的用户名 |
| expireDate | Long | 临时Token的过期时间戳，单位为 ms |

**示例**

**请求示例**

```
Get /tokens HTTP/1.1
```

<公共请求头>

**返回示例**

```
HTTP/1.1 200 OK
```

<公共响应头>

```json
{
    "data": {
        "authorizationToken": "eyJ0aW1lIjoiMTUyNjU0OTc5:0705733****",
        "tempUserName": "cr_temp_user",
        "expireDate": 1526549792000
    },
    "requestId": "94E89857-B994-44B6-9C4F-DBD200E9E272"
}
```

## 高级版API参考

### 镜像命名空间管理

#### CreateNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNamespa ce | 系统规定参数。取值：CreateNamespace。 |
| RegionId | String | 是 | cn-wl-env**** | 地域ID |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| NamespaceNam e | String | 是 | namespace1 | 命名空间名称 |
| AutoCreateRepo | Boolean | 否 | true | 是否自动创建镜像仓库 |
| DefaultRepoTyp e | String | 否 | PUBLIC | 自动创建仓库默认类型，取值： PUBLIC ：公开 PRIVATE ：私有 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否成功 |
| RequestId | String | BC648259-91A7- 4502-BED3- EDF64361FA83 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &NamespaceName=namespace1 &RegionId=cn-wl-env****
```

正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml <IsSuccess>true</IsSuccess> <RequestId>BC648259-91A7-4502-BED3-EDF64361FA83</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "IsSuccess" : true,
  "RequestId" : "BC648259-91A7-4502-BED3-EDF64361FA83",
  "Code" : "success"
}
```

#### DeleteNamespace

删除镜像仓库命名空间会将存在于该命名空间下的所有仓库以及所有仓库下的镜像一并删

**说明**

除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteNamespa ce | 系统规定参数。取值： DeleteNamespace。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| NamespaceNam e | String | 是 | ns3 | 镜像命名空间名称 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RequestId | String | BA08C185-8F76- 48D7-ACB3- BA11BF2778F9 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &NamespaceName=ns3 &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>BA08C185-8F76-48D7-ACB3-BA11BF2778F9</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"BA08C185-8F76-48D7-ACB3-BA11BF2778F9",
    "Code":"success"
}
```

#### UpdateNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | UpdateNamespa ce | 系统规定参数。取值： UpdateNamespace。 |
|---|---|---|---|---|
| InstanceId | String | 是 | cri-pri**** | 实例 ID |
| NamespaceNam e | String | 是 | test | 命名空间名称 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| AutoCreateRepo | Boolean | 否 | true | 允许推送时自动创建仓库 |
| DefaultRepoTyp e | String | 否 | PRIVATE | 默认仓库类型，取值： PUBLIC ：公开仓库 PRIVATE ：私有仓库 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RequestId | String | 90B8475C-C066- 4B92-946E- 4D0DECB514E8 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &NamespaceName=test &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>90B8475C-C066-4B92-946E-4D0DECB514E8</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"90B8475C-C066-4B92-946E-4D0DECB514E8",
    "Code":"success"
}
```

#### GetNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetNamespace | 系统规定参数。取值：GetNamespace。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| NamespaceNam e | String | 否 | test | 命名空间名称 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| NamespaceId | String | 否 | crn- tiw8t3f8i5lta**** | 命名空间ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AutoCreateRe po | Boolean | true | 开启自动创建仓库 |
| Code | String | success | 返回值 |
| DefaultRepoTy pe | String | PUBLIC | 默认仓库类型，取值： PUBLIC：公开仓库 PRIVATE：私有仓库 |
| InstanceId | String | cri-pri**** | 实例ID |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |

| NamespaceId | String | crn-tiw8t3f8i5lt**** | 命名空间ID |
|---|---|---|---|
| NamespaceNa me | String | test | 命名空间名称 |
| NamespaceSta tus | String | NORMAL | 命名空间状态 |
| RequestId | String | E4BC9E21-8AA5- 4582-83C1- C1209AB8196F | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &NamespaceName=test &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<Code>success</Code> <DefaultRepoType>PUBLIC</DefaultRepoType> <InstanceId>cri-pri****</InstanceId> <IsSuccess>true</IsSuccess> <NamespaceName>test</NamespaceName> <NamespaceId>crn-tiw8t3f8i5lta4uv</NamespaceId> <NamespaceStatus>NORMAL</NamespaceStatus> <RequestId>E4BC9E21-8AA5-4582-83C1-C1209AB8196F</RequestId>
```

`JSON` 格式

```json
{
    "AutoCreateRepo": "true",
    "Code": "success",
    "DefaultRepoType": "PUBLIC",
    "InstanceId": "cri-pri****",
    "IsSuccess": "true",
    "NamespaceName": "test",
    "NamespaceId": "crn-tiw8t3f8i5lta4uv",
    "NamespaceStatus": "NORMAL",
    "RequestId": "E4BC9E21-8AA5-4582-83C1-C1209AB8196F"
}
```

**错误码**

访问错误中心查看更多错误码。 访问错误中心查看更多错误码。

#### ListNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListNamespace | 系统规定参数。取值：ListNamespace。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| NamespaceStat us | String | 否 | NORMAL | 命名空间状态，取值： NORMAL ：正常 DELETING ：删除中 |
| NamespaceNam e | String | 否 | test-namespace | 命名空间名称 |
| PageNo | Integer | 否 | 1 | 页号 |
| PageSize | Integer | 否 | 30 | 页大小 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| Namespaces | Array of Namespaces |  | 命名空间列表 |
| AutoCreateRe po | Boolean | true | 开启自动创建仓库 |
| DefaultRepoTy pe | String | PUBLIC | 默认仓库类型，取值： PUBLIC ：公开仓库 PRIVATE ：私有仓库 |

| InstanceId | String | cri-pri**** | 实例ID |
|---|---|---|---|
| NamespaceId | String | crn-tiw8t3f8i5lt**** | 命名空间ID |
| NamespaceNa me | String | test | 命名空间名称 |
| NamespaceSta tus | String | NORMAL | 命名空间状态，取值： NORMAL ：正常 DELETING ：删除中 |
| PageNo | Integer | 1 | 页号 |
| PageSize | Integer | 30 | 页大小 |
| RequestId | String | B7E5FCA5-55ED- 451C-9649- 0BB2B93387D0 | 请求ID |
| TotalCount | String | 1 | 总数量 |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <Namespaces>
    <NamespaceStatus>NORMAL</NamespaceStatus>
    <NamespaceName>test</NamespaceName>
    <DefaultRepoType>PUBLIC</DefaultRepoType>
    <InstanceId>cri-pri****</InstanceId>
    <NamespaceId>crn-tiw8t3f8i5lt****</NamespaceId>
</Namespaces> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>B7E5FCA5-55ED-451C-9649-0BB2B93387D0</RequestId> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "Namespaces": {
        "NamespaceStatus": "NORMAL",
        "NamespaceName": "test",
        "DefaultRepoType": "PUBLIC",
        "InstanceId": "cri-pri****",
        "AutoCreateRepo": true,
        "NamespaceId": "crn-tiw8t3f8i5lt****"
    },
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "B7E5FCA5-55ED-451C-9649-0BB2B93387D0",
    "PageNo": 1,
    "Code": "success"
}
```

### 镜像仓库管理

#### CreateRepository

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateRepositor y | 系统规定参数。取值： CreateRepository。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoName | String | 是 | repo1 | 镜像仓库名称 |
| RepoNamespace Name | String | 是 | namespace01 | 镜像仓库命名空间名称 |
| RepoType | String | 是 | PRIVATE | 仓库类型，取值： PUBLIC ：公开仓库 PRIVATE ：私有仓库 |
| Summary | String | 是 | repo1 | 仓库摘要 |

| Detail | String | 否 | repo1 | 仓库详细描述 |
|---|---|---|---|---|
| TagImmutability | Boolean | 否 | true | 镜像tag不可变性，取值： true ：开启 false ：关闭 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RepoId | String | crr- xwvi3osiy4ff**** | 镜像仓库 ID |
| RequestId | String | 886FB272-15C3- 44FC-AA54- F4ABD5B93A28 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoName=repo1 &RepoNamespaceName=namespace01 &RepoType=PRIVATE &Summary=repo1
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>886FB272-15C3-44FC-AA54-F4ABD5B93A28</RequestId> <RepoId>crr-xwvi3osiy4ff****</RepoId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "886FB272-15C3-44FC-AA54-F4ABD5B93A28",
    "RepoId": "crr-xwvi3osiy4ff****",
    "Code": "success"
}
```

#### DeleteRepository

这个操作会将存在于该仓库下的所有镜像一并删除。

**重要**

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRepositor y | 系统规定参数。取值： DeleteRepository。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 是 | crr- l4933wbcmun2* *** | 镜像仓库ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | 47DD9D56-09A0- 4C52-B520- C3805DBAB96B | 请求ID |

**示例**

请求示例

```
&InstanceId=cn-wl-en**** &RegionId=cri-pri**** &RepoId=crr-l4933wbcmun2****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>47DD9D56-09A0-4C52-B520-C3805DBAB96B</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "47DD9D56-09A0-4C52-B520-C3805DBAB96B",
    "Code": "success"
}
```

#### UpdateRepository

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateRepositor y | 系统规定参数。取值：UpdateRepository。 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RepoId | String | 是 | crr- tquyps22md8p* *** | 镜像仓库ID |
| RepoType | String | 是 | PUBLIC | 镜像仓库类型，取值： PUBLIC ：公开仓库 PRIVATE ：私有仓库 |
| Summary | String | 是 | test repo | 摘要信息 |

| Detail | String | 否 | repo-for-test | 镜像仓库介绍 |
|---|---|---|---|---|
| TagImmutability | Boolean | 否 | true | 镜像tag不可变性，取值： true ：开启 false ：关闭 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RequestId | String | CC43EC6B-0DD4- 40AE-8811- B0519617051A | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RepoId=crr-tquyps22md8p**** &RepoType=PUBLIC &Summary=test repo &Detail=repo-for-test &TagImmutability=true
```

正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <Code>success</Code>
    <IsSuccess>true</IsSuccess>
    <RequestId>CC43EC6B-0DD4-40AE-8811-B0519617051A</RequestId>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "Code" : "success",
  "IsSuccess" : true,
  "RequestId" : "CC43EC6B-0DD4-40AE-8811-B0519617051A"
}
```

#### ListRepository

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListRepository | 系统规定参数。取值：ListRepository。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoStatus | String | 否 | NORMAL | 仓库状态，取值： NORMAL ：正常 DELETING ：删除中 DELETED ：已删除 |
| RepoName | String | 否 | repo-test | 仓库名称 |
| RepoNamespace Name | String | 否 | repo- namespace-test | 仓库命名空间名称 |
| PageNo | Integer | 否 | 1 | 页号 |
| PageSize | Integer | 否 | 30 | 页大小 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |

| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
|---|---|---|---|
| PageNo | Integer | 1 | 页号 |
| PageSize | Integer | 30 | 页大小 |
| Repositories | Array of Repositories |  | 仓库列表 |
| CreateTime | Long | 1564153576000 | 创建时间 |
| InstanceId | String | cn-wl-en**** | 实例ID |
| ModifiedTime | Long | 1564153576000 | 最近修改时间 |
| RepoBuildType | String | MANUAL | 仓库构建类型，取值： AUTO ：自动触发构建 MANUAL ：手动触发构建 |
| RepoId | String | crr- 03cuozrsqhkw**** | 仓库ID |
| RepoName | String | test | 仓库名称 |
| RepoNamespa ceName | String | test | 仓库命名空间 |
| RepoStatus | String | NORMAL | 仓库状态 |
| RepoType | String | PRIVATE | 仓库类型，取值： PUBLIC ：公开 PRIVATE ：私有 |
| Summary | String | test OK | 摘要信息 |
| TagImmutabili ty | Boolean | true | 镜像tag不可变性 |
| RequestId | String | 5241C090-DA69- 4B0F-8E3F- 2F24FDE1110E | 请求ID |

| TotalCount | String | 1 | 总数量 |
|---|---|---|---|

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<Repositories>
    <RepoNamespaceName>test</RepoNamespaceName>
    <TagImmutability>true</TagImmutability>
    <RepoBuildType>MANUAL</RepoBuildType>
    <ModifiedTime>1564153576000</ModifiedTime>
    <RepoType>PRIVATE</RepoType>
    <RepoStatus>NORMAL</RepoStatus>
    <InstanceId>cri-pri****</InstanceId>
    <CreateTime>1564153576000</CreateTime>
    <RepoName>test</RepoName>
    <Summary>test OK</Summary>
    <RepoId>crr-03cuozrsqhkw****</RepoId>
</Repositories> <IsSuccess>true</IsSuccess> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>5241C090-DA69-4B0F-8E3F-2F24FDE1110E</RequestId> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` 格式

```json
{
    "Repositories": {
        "RepoNamespaceName": "test",
        "TagImmutability": true,
        "RepoBuildType": "MANUAL",
        "ModifiedTime": 1564153576000,
        "RepoType": "PRIVATE",
        "RepoStatus": "NORMAL",
        "InstanceId": "cri-pri****",
        "CreateTime": 1564153576000,
        "RepoName": "test",
        "Summary": "test OK",
        "RepoId": "crr-03cuozrsqhkw****"
    },
    "IsSuccess": true,
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "5241C090-DA69-4B0F-8E3F-2F24FDE1110E",
    "PageNo": 1,
    "Code": "success"
}
```

#### GetRepository

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRepository | 系统规定参数。取值：GetRepository。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 否 | crr- l5eoubonp0l**** | 仓库ID |
| RepoNamespace Name | String | 否 | test | 仓库命名空间名称 |
| RepoName | String | 否 | test | 仓库名称 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| Code | String | success | 返回值 |
|---|---|---|---|
| CreateTime | Long | 1570759546000 | 创建时间 |
| Detail | String | test | 细节信息 |
| InstanceId | String | cri-pri**** | 实例ID |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| ModifiedTime | Long | 1570759546100 | 最近修改时间 |
| RepoBuildType | String | MANUAL | 仓库构建类型，取值： MANUAL ：手动触发构建 AUTO ：自动触发构建 |
| RepoId | String | crr- l5eoubonp0l**** | 仓库ID |
| RepoName | String | test | 仓库名称 |
| RepoNamespa ceName | String | test | 命名空间名称 |
| RepoStatus | String | NORMAL | 仓库状态 |
| RepoType | String | PRIVATE | 仓库类型，取值： PUBLIC ：公开仓库 PRIVATE ：私有仓库 |
| RequestId | String | 915E6734-3E50- 4640-8DBA- 126D2D94DE29 | 请求ID |
| Summary | String | Automatically created repository | 摘要信息 |
| TagImmutabili ty | Boolean | true | 镜像tag不可变性，取值： true ：开启 false ：关闭 |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<RepoNamespaceName>test</RepoNamespaceName> <IsSuccess>true</IsSuccess> <RequestId>915E6734-3E50-4640-8DBA-126D2D94DE29</RequestId> <InstanceId>cri-pri****</InstanceId> <CreateTime>1570759546000</CreateTime> <RepoName>test</RepoName> <Code>success</Code> <TagImmutability>true</TagImmutability> <RepoBuildType>MANUAL</RepoBuildType> <ModifiedTime>1570759546100</ModifiedTime> <RepoType>PRIVATE</RepoType> <RepoStatus>NORMAL</RepoStatus> <Summary>Automatically created repository</Summary> <RepoId>crr-l5eoubonp0l****</RepoId> <Detail>test</Detail>
```

`JSON` 格式

```json
{
    "RepoNamespaceName": "test",
    "IsSuccess": true,
    "RequestId": "915E6734-3E50-4640-8DBA-126D2D94DE29",
    "InstanceId": "cri-pri****",
    "CreateTime": 1570759546000,
    "RepoName": "test",
    "Code": "success",
    "TagImmutability": true,
    "RepoBuildType": "MANUAL",
    "ModifiedTime": 1570759546100,
    "RepoType": "PRIVATE",
    "RepoStatus": "NORMAL",
    "Summary": "Automatically created repository",
    "RepoId": "crr-l5eoubonp0l****",
    "Detail": "test"
}
```

**错误码**

访问错误中心查看更多错误码。 访问错误中心查看更多错误码。

### 镜像管理

#### ListRepoTag

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListRepoTag | 系统规定参数。取值：ListRepoTag。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 是 | crr- tquyps22md8p* *** | 仓库ID |
| PageNo | Integer | 否 | 1 | 页号 |
| PageSize | Integer | 否 | 30 | 页大小 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| Images | Array of Images |  | 镜像列表 |
| Digest | String | 67bfbcc12b67936e c7f867927817cbb0 71832b873dbcaed 312a1930ba5f1*** * | digest值 |
| ImageCreate | String | 1572839125000 | 镜像创建时间 |
| ImageId | String | 45023655bf39c382 e26a8607d057c27 871dee163c1ecf48 cc1ebf2a1**** | 镜像ID |
| ImageSize | Long | 27107966 | 镜像大小 |

| ImageUpdate | String | 1572875608000 | 镜像更新时间 |
|---|---|---|---|
| Status | String | NORMAL | 状态 |
| Tag | String | v0.1 | 镜像TAG |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| PageNo | Integer | 1 | 页号 |
| PageSize | Integer | 30 | 页大小 |
| RequestId | String | 031572FA-7D8F- 4C05-B790- 1071E0E05DE6 | 请求ID |
| TotalCount | String | 1 | 总数量 |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <TotalCount>1</TotalCount> <PageSize>30</PageSize> <RequestId>031572FA-7D8F-4C05-B790-1071E0E05DE6</RequestId> <Images>
    <Status>NORMAL</Status>
    <ImageCreate>1572839125000</ImageCreate>
    <ImageSize>27107966</ImageSize>
    <Digest>67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****</Digest>
    <ImageId>45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****</ImageId>
    <ImageUpdate>1572875608000</ImageUpdate>
    <Tag>v0.1</Tag>
</Images> <PageNo>1</PageNo> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "TotalCount": 1,
    "PageSize": 30,
    "RequestId": "031572FA-7D8F-4C05-B790-1071E0E05DE6",
    "Images": {
        "Status": "NORMAL",
        "ImageCreate": 1572839125000,
        "ImageSize": 27107966,
        "Digest": "67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****",
        "ImageId": "45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****",
        "ImageUpdate": 1572875608000,
        "Tag": "v0.1"
    },
    "PageNo": 1,
    "Code": "success"
}
```

#### DeleteRepoTag

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRepoTag | 系统规定参数。取值：DeleteRepoTag。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 是 | crr- xwvi3osiy4ff**** | 镜像仓库ID |
| Tag | String | 是 | 1.24 | 镜像版本 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |

| RequestId | String | 96E66B3A-C81A- 48BE-ACD6- C0AB1F9313C0 | 请求ID |
|---|---|---|---|

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &Tag=1.24
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>96E66B3A-C81A-48BE-ACD6-C0AB1F9313C0</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "96E66B3A-C81A-48BE-ACD6-C0AB1F9313C0",
    "Code": "success"
}
```

#### GetRepoTag

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRepoTag | 系统规定参数。取值：GetRepoTag。 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RepoId | String | 是 | crr- tquyps22md8p* *** | 仓库ID |
| Tag | String | 是 | 1.0 | 仓库版本 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Status | String | NORMAL | 状态，取值： NORMAL ：正常镜像 DELETING ：镜像删除中 |
| ImageCreate | Long | 1572839125000 | 镜像创建时间 |
| ImageSize | Long | 27107966 | 镜像大小 |
| RequestId | String | 031572FA-7D8F- 4C05-B790- 1071E0E05DE6 | 请求ID |
| Digest | String | 67bfbcc12b67936e c7f867927817cbb0 71832b873dbcaed 312a1930ba5f1*** * | digest值 |
| Code | String | success | 返回值 |
| ImageUpdate | Long | 1572875608000 | 镜像更新时间 |
| Tag | String | 1.0 | 仓库版本 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| ImageId | String | 45023655bf39c382 e26a8607d057c27 871dee163c1ecf48 cc1ebf2a1**** | 镜像ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RepoId=crr-tquyps22md8p**** &Tag=1.0
```

正常返回示例 `XML` 格式

```xml
HTTP/1.1 200 OK Content-Type:application/xml
    <Status>NORMAL</Status>
    <ImageCreate>1572839125000</ImageCreate>
    <ImageSize>27107966</ImageSize>
    <RequestId>031572FA-7D8F-4C05-B790-1071E0E05DE6</RequestId>
    <Digest>67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****</Digest>
    <Code>success</Code>
    <ImageUpdate>1572875608000</ImageUpdate>
    <Tag>1.0</Tag>
    <IsSuccess>true</IsSuccess>
    <ImageId>45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****</ImageId>
```

`JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
  "Status" : "NORMAL",
  "ImageCreate" : 1572839125000,
  "ImageSize" : 27107966,
  "RequestId" : "031572FA-7D8F-4C05-B790-1071E0E05DE6",
  "Digest" : "67bfbcc12b67936ec7f867927817cbb071832b873dbcaed312a1930ba5f1****",
  "Code" : "success",
  "ImageUpdate" : 1572875608000,
  "Tag" : 1,
  "IsSuccess" : true,
  "ImageId" : "45023655bf39c382e26a8607d057c27871dee163c1ecf48cc1ebf2a1****"
}
```

#### GetRepoTagLayers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRepoTagLay ers | 系统规定参数。取值： GetRepoTagLayers。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |

| RepoId | String | 是 | crr- kwgb20p8wwmh **** | 仓库ID |
|---|---|---|---|---|
| Tag | String | 是 | master | 镜像版本 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| Layers | Array of Layers |  | 层数据 |
| BlobDigest | String | sha256:36fb85fcb5 e919cb60e782397 a6be04201868fe7 b38ef7669fc01cae c1c8fc4e | 块digest值 |
| BlobSize | Long | 23655489 | 块大小 |
| LayerCMD | String | /usr/bin/virtual- kubelet /usr/bin/virtual- kubelet # buildkit | 层命令 |
| LayerIndex | Integer | 0 | 层下标 |
| LayerInstructio n | String | COPY | 层指令 |
| RequestId | String | D39D7151-0299- 47E3-B948- E49E1EA8D406 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-kwgb20p8wwmh**** &Tag=master
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>D39D7151-0299-47E3-B948-E49E1EA8D406</RequestId> <Layers> <BlobDigest>sha256:36fb85fcb5e919cb60e782397a6be04201868fe7b38ef7669fc01caec1c8fc4e</Blob gest>
    <LayerInstruction>COPY</LayerInstruction>
    <BlobSize>23655489</BlobSize>
    <LayerCMD>/usr/bin/virtual-kubelet /usr/bin/virtual-kubelet # buildkit</LayerCMD>
    <LayerIndex>0</LayerIndex>
</Layers> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"D39D7151-0299-47E3-B948-E49E1EA8D406",
    "Layers":[
        {
"BlobDigest":"sha256:36fb85fcb5e919cb60e782397a6be04201868fe7b38ef7669fc01caec1c8fc4e",
            "LayerInstruction":"COPY",
            "BlobSize":23655489,
            "LayerCMD":"/usr/bin/virtual-kubelet /usr/bin/virtual-kubelet # buildkit",
            "LayerIndex":0
        }
```

`],`

```json
    "Code":"success"
}
```

#### GetRepoTagManifest

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetRepoTagMan ifest | 系统规定参数。取值： GetRepoTagManifest。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |

| RepoId | String | 是 | crr- kwgb20p8wwmh **** | 仓库ID |
|---|---|---|---|---|
| Tag | String | 是 | master | 镜像版本 |
| SchemaVersion | Integer | 否 | 2 | Schema版本，可选1和2。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| Manifest | Struct |  | Manifest信息 |
| Architecture | String | null | 架构 |
| Config | Struct |  | 配置信息 |
| Digest | String | sha256:b5b2b2c50 7a0944348e03031 14d8d93aaaa0817 32b86451d9bce1f4 32a537bc7 | digest值 |
| MediaType | String | application/vnd.doc ker.container.imag e.v1+json | 文件类型 |
| Size | Long | 7023 | 大小 |
| FsLayers | Array of FsLayers |  | 文件层信息 |
| BlobSum | String | null | 块sum值 |
| History | Array of History |  | 历史信息 |
| V1Compatibilit y | Map | null | v1兼容性 |
| Layers | Array of Layers |  | 层列表 |

| Digest | String | sha256:e692418e4 cbaf90ca69d05a66 403747baa33ee08 806650b51fab815 ad7fc331f | digest值 |
|---|---|---|---|
| MediaType | String | application/vnd.doc ker.image.rootfs.di ff.tar.gzip | 文件类型 |
| Size | Long | 32654 | 大小 |
| MediaType | String | application/vnd.doc ker.distribution.ma nifest.v2+json | 类型 |
| Name | String | null | 名称 |
| SchemaVersio n | Integer | 2 | schema版本 |
| Signatures | Array of Signatures |  | 签名列表 |
| Header | Map | null | 头信息 |
| Protected | String | null | 受保护 |
| Signature | String | null | 签名信息 |
| Tag | String | master | 镜像TAG |
| RequestId | String | D39D7151-0299- 47E3-B948- E49E1EA8D406 | 请求ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetRepoTagManifest &InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-kwgb20p8wwmh**** &Tag=master
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>D39D7151-0299-47E3-B948-E49E1EA8D406</RequestId> <Manifest>
    <Architecture>null</Architecture>
    <SchemaVersion>2</SchemaVersion>
    <MediaType>application/vnd.docker.distribution.manifest.v2+json</MediaType>
    <Tag>master</Tag>
    <Name>null</Name>
    <FsLayers>
        <BlobSum>null</BlobSum>
    </FsLayers>
    <History>
        <V1Compatibility>null</V1Compatibility>
    </History>
    <Signatures>
        <Protected>null</Protected>
        <Header>null</Header>
        <Signature>null</Signature>
    </Signatures>
    <Layers>
<Digest>sha256:e692418e4cbaf90ca69d05a66403747baa33ee08806650b51fab815ad7fc331f</Digest>
        <Size>32654</Size>
        <MediaType>application/vnd.docker.image.rootfs.diff.tar.gzip</MediaType>
    </Layers>
    <Config>
<Digest>sha256:b5b2b2c507a0944348e0303114d8d93aaaa081732b86451d9bce1f432a537bc7</Digest>
        <Size>7023</Size>
        <MediaType>application/vnd.docker.container.image.v1+json</MediaType>
    </Config>
</Manifest> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "D39D7151-0299-47E3-B948-E49E1EA8D406",
    "Manifest": {
        "Architecture": "null",
        "SchemaVersion": 2,
        "MediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "Tag": "master",
        "Name": "null",
        "FsLayers": {
            "BlobSum": "null"
        },
        "History": {
            "V1Compatibility": "null"
        },
        "Signatures": {
            "Protected": "null",
            "Header": "null",
            "Signature": "null"
        },
        "Layers": {
            "Digest":
"sha256:e692418e4cbaf90ca69d05a66403747baa33ee08806650b51fab815ad7fc331f",
            "Size": 32654,
            "MediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip"
        },
        "Config": {
            "Digest":
"sha256:b5b2b2c507a0944348e0303114d8d93aaaa081732b86451d9bce1f432a537bc7",
            "Size": 7023,
            "MediaType": "application/vnd.docker.container.image.v1+json"
        }
    },
    "Code": "success"
}
```

#### CreateRepoTag

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateRepoTag | 系统规定参数。取值：CreateRepoTag。 |
| FromTag | String | 是 | v1 | 源镜像版本 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |

| NamespaceNam e | String | 是 | ns | 命名空间名称 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoName | String | 是 | repo1 | 镜像仓库名称 |
| ToTag | String | 是 | v2 | 目标镜像版本 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RequestId | String | C4C7DD0C-C9D6- 437A-A7EE- 8BY***** | 请求ID |

**示例**

请求示例

```
&FromTag=v1 &InstanceId=cri-pri**** &NamespaceName=ns &RegionId=cn-wl-en**** &RepoName=repo1 &ToTag=v2
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>C4C7DD0C-C9D6-437A-A7EE-8BY*****</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "C4C7DD0C-C9D6-437A-A7EE-8BY*****",
    "Code": "success"
}
```

### 镜像触发器管理

#### UpdateRepoTrigger

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateRepoTrig ger | 系统规定参数。取值： UpdateRepoTrigger。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 是 | crr- tquyps22md8p* *** | 镜像仓库ID |
| TriggerId | String | 是 | crw- k7bdx4kt52ty*** * | 触发器ID |
| TriggerName | String | 否 | test trigger _ | 触发器名称 |
| TriggerUrl | String | 否 | https://www.test. com | 触发器地址 |
| TriggerType | String | 否 | TAG LIST _ | 触发类型，取值： ALL ：全部触发，只要镜像构建成功后，自动触发容器服务上应用拉取新的镜像。 TAG LISTTAG ：TAG触发，基于设 _ 置的Tag列表来进行触发，只有符合设置的TAG才会触发容器服务上应用拉取新的镜像。 TAG REG EXP ：表达式触发，基于 _ _ 正则表达式来进行Tag的过滤，只有当符合正则表达式的Tag才会触发容器服务上应用拉取新的镜像。。 |

| TriggerTag | String | 否 | master | 触发触发器的镜像版本 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |
| RequestId | String | 32535049-ED91- 4589-98C0- 7C88766EDF1F | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p**** &TriggerId=crw-k7bdx4kt52ty**** &TriggerName=test_trigger
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>32535049-ED91-4589-98C0-7C88766EDF1F</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"32535049-ED91-4589-98C0-7C88766EDF1F",
    "Code":"success"
}
```

#### ListRepoTrigger

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListRepoTrigger | 系统规定参数。取值： ListRepoTrigger。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |
| RepoId | String | 是 | crr- tquyps22md8p* *** | 镜像仓库ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | 2CA76D52-A8F0- 4D0B-854E- FBD9F6C99049 | 请求ID |
| Triggers | Array of Triggers |  | 触发器列表 |
| RepoEvent | String | BUILD SUCCESS _ | 触发事件类型，取值： BUILD SUCCESS ：触发成功 _ BUILD Fail ：触发失败 _ |
| TriggerId | String | crw- vriyql9eq7ep**** | 触发器ID |
| TriggerName | String | test | 触发器名称 |
| TriggerTag | String | * | 触发触发器的镜像版本 |
| TriggerType | String | ALL | 触发类型，取值： ALL ：全部触发 TAG LISTTAG ：触发 _ TAG REG EXP ：表达式触发 _ _ |

| TriggerUrl | String | https://www.test.co m | 触发器URL地址 |
|---|---|---|---|

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-tquyps22md8p****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>2CA76D52-A8F0-4D0B-854E-FBD9F6C99049</RequestId> <Triggers>
    <TriggerUrl>https://www.test.com</TriggerUrl>
    <TriggerType>ALL</TriggerType>
    <RepoEvent>BUILD_SUCCESS</RepoEvent>
    <TriggerName>test</TriggerName>
    <TriggerTag>*</TriggerTag>
    <TriggerId>crw-vriyql9eq7ep****</TriggerId>
</Triggers> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "2CA76D52-A8F0-4D0B-854E-FBD9F6C99049",
    "Triggers": {
        "TriggerUrl": "https://www.test.com",
        "TriggerType": "ALL",
        "RepoEvent": "BUILD_SUCCESS",
        "TriggerName": "test",
        "TriggerTag": "*",
        "TriggerId": "crw-vriyql9eq7ep****"
    },
    "Code": "success"
}
```

#### CreateRepoTrigger

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

| Action | String | 是 | CreateRepoTrigg er |  | 系统规定参数。取值： CreateRepoTrigger 。 |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| InstanceId | String | 是 | cri-pri**** |  | 实例ID |  |  |  |  |  |  |  |  |  |
| RegionId | String | 是 | cn-wl-en**** |  | 地域ID |  |  |  |  |  |  |  |  |  |
| RepoId | String | 是 | crr- xwvi3osiy4ff**** |  | 镜像仓库ID |  |  |  |  |  |  |  |  |  |
| TriggerName | String | 是 | trigger1 |  | 触发器名称 |  |  |  |  |  |  |  |  |  |
| TriggerTag | String | 是 | [1] |  | 触发触发器的镜像版本。 说明 TriggerType 为 ALL ， TriggerTag 可以为任意字符串，示例 * 。 TriggerType 为 TAG _ LIST ， TriggerTag 为数组，示例 [1] 。 TriggerType 为 TAG _ REG EXP ， TriggerTag _ 为字符串，示例 * 。 |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | TriggerType |  |  | 为 | TAG _ |  |  |
|  |  |  |  |  |  |  | LIST |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [1] |  |  |  |  |
|  |  |  |  |  |  |  |  | TriggerType |  |  | 为 | TAG _ |  |  |
|  |  |  |  |  |  |  | REG EXP _ |  |  |  |  |  |  |  |
| TriggerType | String | 是 | ALL |  | 触发器类型，取值： ALL ：全部触发 TAG LIST ：Tag触发 _ TAG REG EXP ：表达式触发 _ _ |  |  |  |  |  |  |  |  |  |
| TriggerUrl | String | 是 | http://www.mysit e.com |  | 触发器URL |  |  |  |  |  |  |  |  |  |

|  | TriggerType |  |
|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用成功，取值： true ：调用成功 false ：调用失败 |

| RequestId | String | B79F5E0E-8770- 407D-BCB6- ECF4BA9C**** | 请求ID |
|---|---|---|---|
| TriggerId | String | crw- 0z4pf81pgz35**** | 触发器ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &TriggerName=trigger1 &TriggerTag=[1] &TriggerType=ALL &TriggerUrl=http://www.mysite.com
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>B79F5E0E-8770-407D-BCB6-ECF4BA9C****</RequestId> <TriggerId>crw-0z4pf81pgz35****</TriggerId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "RequestId": "B79F5E0E-8770-407D-BCB6-ECF4BA9C****",
    "TriggerId": "crw-0z4pf81pgz35****",
    "Code": "success"
}
```

#### DeleteRepoTrigger

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteRepoTrigg er | 系统规定参数。取值： DeleteRepoTrigger。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |

| RegionId | String | 是 | cn-wl-en**** | 地域ID |
|---|---|---|---|---|
| RepoId | String | 是 | crr- xwvi3osiy4ff**** | 镜像仓库ID |
| TriggerId | String | 是 | crw- 0z4pf81pgz35** ** | 触发器ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | 85180AE4-9A57- 48F8-9EF9- 68ECCE54B552 | 请求ID |

**示例**

请求示例

```
&InstanceId=cri-pri**** &RegionId=cn-wl-en**** &RepoId=crr-xwvi3osiy4ff**** &TriggerId=crw-0z4pf81pgz35****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>85180AE4-9A57-48F8-9EF9-68ECCE54B552</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"85180AE4-9A57-48F8-9EF9-68ECCE54B552",
    "Code":"success"
}
```

### 访问凭证管理

#### GetAuthorizationToken

调用GetAuthorizationToken获取用于登录实例的临时账号和临时密码。 临时密码的有效时间为1小时，若使用STS方式请求时，临时密码的有效时间等同于本次请求STS Token的有效时间。关于临时Token登录实例的权限说明如下： 使用通过阿里云账号获取的临时Token登录实例的权限等同于阿里云账号使用用户名和密码登录实例的权限。 使用通过RAM用户获取的临时Token登录实例的权限等同于RAM用户使用用户名和密码登录实例的权限。 使用STS方式获取的临时Token登录实例的权限等同于STS Token的权限。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetAuthorizatio nToken | 系统规定参数。取值： GetAuthorizationToken。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AuthorizationT oken | String | shaunadadakks:uu czxnjcyeyhdjadkkaj sjd**** | 用于登录实例的密码 |
| Code | String | success | 返回值 |
| ExpireTime | Long | 1571242083000 | 临时Token的过期时间戳，单位为ms |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | E069EB86-E6AD- 4A98-ADDE- 0E993390239A | 请求ID |
| TempUsernam e | String | temp user cr _ _ | 用于登录实例的用户名 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetAuthorizationToken &InstanceId=cri-pri**** &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <AuthorizationToken>shaunadadakks:uuczxnjcyeyhdjadkkajsjd****</AuthorizationToken> <TempUsername>temp_user_cr</TempUsername> <RequestId>E069EB86-E6AD-4A98-ADDE-0E993390239A</RequestId> <ExpireTime>1571242083000</ExpireTime> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess": true,
    "AuthorizationToken": "shaunadadakks:uuczxnjcyeyhdjadkkajsjd****",
    "TempUsername": "temp_user_cr",
    "RequestId": "E069EB86-E6AD-4A98-ADDE-0E993390239A",
    "ExpireTime": 1571242083000,
    "Code": "success"
}
```

#### ResetLoginPassword

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ResetLoginPass word | 系统规定参数。取值： ResetLoginPassword。 |
| InstanceId | String | 是 | cri-pri**** | 实例ID |
| Password | String | 是 | test | 登录密码 |
| RegionId | String | 是 | cn-wl-en**** | 地域ID |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Code | String | success | 返回值 |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | EB9C5722-51E2- 4497-A573- 575B0CA5CE0C | 请求ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ResetLoginPassword &InstanceId=cri-pri**** &Password=test &RegionId=cn-wl-en****
```

正常返回示例 `XML` 格式

```xml
<IsSuccess>true</IsSuccess> <RequestId>EB9C5722-51E2-4497-A573-575B0CA5CE0C</RequestId> <Code>success</Code>
```

`JSON` 格式

```json
{
    "IsSuccess":true,
    "RequestId":"EB9C5722-51E2-4497-A573-575B0CA5CE0C",
    "Code":"success"
}
```

### 制品构建

#### CreateArtifactBuildTask

用于创建容器镜像服务中的制品构建任务。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |
|---|---|---|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** |  | 区域ID |  |  |
| InstanceId | Strin g | Query | 是 | cri-pri**** |  | 实例 ID。 |  |  |
| ArtifactBui ldType | Strin g | Query | 是 | IMAGE TO ACCELERATE _ _ D IMAGE _ |  | 制品构建类型，目前支持： IMAGE TO ACCELERAT _ _ ED IMAGE ：ACK场景 _ 优化的加速镜像制作 |  |  |
|  |  |  |  |  |  |  | IMAGE TO ACCELERAT _ _ |  |
|  |  |  |  |  | E | ED IMAGE _ |  |  |
| SourceArti fact | Json | Query | 是 | { \"repoId\" : \"crr- 1rgqu9n2e****\", \"version\": \"test\", \"artifactType\": \"IMAGE\" } |  | 源制品 |  |  |
| TargetArti fact | Json | Query | 是 | { \"repoId\" : \"crr- 1rgqu9n2e****\", \"version\": \"test accelerated\", _ \"artifactType\": \"ACCELERATED IMAGE\ _ " } |  | 目的制品 |  |  |
| Instructio ns | Repe atList | Query | 否 | [] |  | 附加构建指令 |  |  |
| Parameter s | Map | Query | 否 | {} |  | 附加参数。 |  |  |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否成功 |
| RequestId | String | RQ1234567890abc def | 1234567890 |
| BuildTaskId | String | i2ai-1yu**** | 制品构建任务ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateArtifactBuildTask &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &ArtifactBuildType=IMAGE_TO_ACCELERATED_IMAGE &SourceArtifact={ \"repoId\" : \"crr-1rgqu9n2e****\", \"version\": \"test\", \"artifactType\": \"IMAGE\"} &TargetArtifact={ \"repoId\" : \"crr-1rgqu9n2e****\", \"version\": \"test_accelerated\", \"artifactType\": \"ACCELERATED_IMAGE\"}
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "IsSuccess":true,
 "RequestId":"RQ1234567890abcdef",
 "BuildTaskId":"i2a-1yu****",
 "Code":"0"
}
```

#### CreateArtifactBuildRule

创建镜像仓库加速镜像构建规则。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** | 区域ID |
| InstanceId | Strin g | Query | 是 | cri-pri**** | 实例 ID。 |
| ScopeTyp e | Strin g | Query | 是 | REPOSITORY | 规则生效范围，取值： REPOSITORY ：表示生效范围仓库级别。 |
| ScopeId | Strin g | Query | 是 | crr-pmajihou6cg0**** | 规则生效范围的 ID，取值： ScopeId 配置为镜像仓库 ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ArtifactTy pe | Strin g | Query | 是 | ACCELERATED IMAGE _ | 加速镜像类型，取值： ACCELERATED IMAGE _ ：表示生成加速镜像 |
| Parameter s | Map | Query | 否 | {} | 附加参数。 |

|  |  | ACCELERATED IMAGE _ |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否成功 |
| RequestId | String | RQ1234567890abc def | 1234567890 |
| BuildRuleId | String | crabr- ly77w5i3t31f**** | 构建规则ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &ScopeType=REPOSITORY &ScopeId=crr-pmajihou6cg0**** &ArtifactType=ACCELERATED_IMAGE
```

正常返回示例 `JSON` 格式

```json
{
 "IsSuccess":true,
 "BuildRuleId":"crbr-ly77w5i3t31f****",
 "RequestId":"RQ1234567890abcdef",
 "Code":"0"
}
```

#### GetArtifactBuildTask

获取创建容器镜像服务中的制品构建任务。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** | 区域ID |
| InstanceId | Strin g | Query | 是 | cri-pri**** | 实例 ID。 |
| BuildTaskI d | Strin g | Query | 是 | i2ai-1yu**** | 制品构建任务ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Instructions | String | [] | 构建附加指令 |
| EndTime | Integer | 2019-11- 30T05:40:00Z | 结束时间。 |
| StartTime | Integer | 2019-11- 30T04:00:00Z | 开始时间。 |
| EstimateTime | Integer | 5000 | 预计结束时间。单位：毫秒。 |
| ArtifactBuildTy pe | String | IMAGE TO ACCELE _ _ RATED IMAGE _ | 制品构建类型，目前支持： IMAGE TO ACCELERATED IMAGE ： _ _ _ ACK场景优化的加速镜像制作 |
| RequestId | String | RQ1234567890abc def | 请求ID |
| TaskStatus | String | PENDING | 表示任务的状态，例如"PENDING"代表任务等待执行，"RUNNING"代表任务正在运行，"COMPLETED"代表任务已完成，"FAILED"则表示任务失败。 |
| BuildTaskId | String | i2a-1yu**** | 制品构建任务ID |
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否成功 |
| SourceArtifact | Struct | exampleValue | 源制品 |

| 容器镜像服务 |  |  | 开发指南·高级版API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -RepoId | String | 1234567890 | 仓库ID |
| -Version | String | 1 | 版本号。 |
| -ArtifactType | String | EcsImage | 制品类型 |
| TargetArtifact | Struct | example.jar | 目的制品 |
| -RepoId | String | 1234567890 | 仓库ID |
| -Version | String | 1 | 版本号。 |
| -ArtifactType | String | EcsImage | 制品类型 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetArtifactBuildTask &RegionId=cn-wl-en**** &InstanceId=cri-pri**** &BuildTaskId=i2a-1yu****
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TargetArtifact":{
  "Version":"1",
  "ArtifactType":"EcsImage",
  "RepoId":"1234567890"
 },
 "ArtifactBuildType":"IMAGE_TO_ACCELERATED_IMAGE",
 "IsSuccess":true,
 "EndTime":2022,
 "RequestId":"RQ1234567890abcdef",
 "BuildTaskId":"i2a-1yu****",
 "StartTime":2022,
 "EstimateTime":5000,
 "Instructions":"",
 "TaskStatus":"PENDING",
 "Code":"0",
 "SourceArtifact":{
  "Version":"1",
  "ArtifactType":"EcsImage",
  "RepoId":"1234567890"
 }
}
```

#### ListArtifactBuildTask

获取制品构建任务列表。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** | 区域ID |
| InstanceId | Strin g | Query | 是 | cri-pri**** | 实例 ID。 |
| PageNo | Integ er | Query | 否 | 1 | 页号 |
| PageSize | Integ er | Query | 否 | 10 | 每页展示的列表数。上限为 100。如果传入的值超过 100，系统将报参数错误或以 100 作为实际返回的列表数上限。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ArtifactBui ldType | Strin g | Query | 否 | ACCELERATED IMAGE _ | 加速镜像类型，取值： ACCELERATED IMAGE _ ：表示生成加速镜像 |
| SourceArti factRepoI d | Strin g | Query | 否 | crr-1rgqu9n2e**** | 源制品仓库ID |
| DestArtifa ctRepoId | Strin g | Query | 否 | crr-1rgqu9n2e**** | 目的制品仓库ID |

|  |  | ACCELERATED IMAGE _ |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ArtifactBuildTa sk | Array | [] | 制品构建任务列表 |
| -Instructions | String | [] | 构建附加指令 |
| -SourceArtifact | Array | [] | 源制品 |
| --RepoId | String | crr- gzsrlevmvoaq**** | 仓库ID |
| --Version | String | 1 | 版本号。 |
| --ArtifactType | String | IMAGE | 制品类型 |
| -EndTime | Integer | 2209702074010 | 结束时间。 |
| -StartTime | Integer | 2209702074000 | 开始时间。 |
| -EstimateTime | Integer | 5000 | 预估构建耗时 |
| - ArtifactBuildTy pe | String | IMAGE TO ACCELE _ _ RATED IMAGE _ | 制品构建类型，目前支持： IMAGE TO ACCELERATED IMAGE ： _ _ _ ACK场景优化的加速镜像制作 |
| -TaskStatus | String | SUCCESS | 表示任务的状态，例如"PENDING"代表任务等待执行，"RUNNING"代表任务正在运行，"COMPLETED"代表任务已完成，"FAILED"则表示任务失败。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -BuildTaskId | String | i2ai--1yu**** | 制品构建任务ID |
| -TargetArtifact | Struct | {} | 目的制品 |
| --RepoId | String | crr- gzsrlevmvoaq**** | 仓库ID |
| --Version | String | 1 accelerated _ | 版本号。 |
| --ArtifactType | String | ACCELERATED IMA _ GE | 制品类型 |
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否调用API成功，取值： true ：调用API成功 false ：调用API失败 |
| RequestId | String | C4C7DD0C-C9D6- 437A-A7EE- 121EFD70D002 | 请求 ID |
| TotalCount | Integer | 200 | 列表条目数。 |
| PageNo | Integer | 1 | 页号 |
| PageSize | Integer | 10 | 分页数据条数。 |

#### GetArtifactBuildRule

查询镜像仓库加速镜像构建规则。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** | 区域ID |
| InstanceId | Strin g | Query | 是 | cri-pri**** | 实例 ID。 |

|  | 容器镜像服务 |  |  |  |  | 开发指南·高级版API参考 |  |
|---|---|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ScopeTyp e | Strin g | Query | 否 | REPOSITORY | 规则生效范围，取值： REPOSITORY ，表示生效范围仓库级别。 |
| ScopeId | Strin g | Query | 否 | crr-pmajihou6cg0**** | 规则生效范围的 ID，取值： ScopeId 配置为镜像仓库 ID。 |
| ArtifactTy pe | Strin g | Query | 否 | ACCELERATED IMAGE _ | 加速镜像类型，取值： ACCELERATED IMAGE _ ：表示生成加速镜像 |
| BuildRuleI d | Strin g | Query | 否 | crabr-ly77w5i3t31f**** | 构建规则ID |

|  |  | ACCELERATED IMAGE _ |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | RQ1234567890abc def | 请求ID |
| ScopeId | String | crr- nyrh2oko32xb**** | 规则生效范围的 ID |
| BuildRuleId | String | crabr- ly77w5i3t31f**** | 构建规则ID |
| ArtifactType | String | ACCELERATED IMA _ GE | 制品类型 |
| ScopeType | String | REPOSITORY | 规则生效范围 |
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否成功 |
| Parameters | Struct | { "Status": { "Description": " (Required) The status of the Ecs instance.", "Type": "String" } } | 参数信息 |
| - ImageIndexOn ly | Boolean | false | 表示仅通过索引访问图像数据，不包含其他元信息或处理逻辑 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri****
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "ScopeType":"REPOSITORY",
 "IsSuccess":true,
 "BuildRuleId":"crbr-ly77w5i3t31f****",
 "Parameters":{
  "ImageIndexOnly":""
 },
 "RequestId":"RQ1234567890abcdef",
 "ArtifactType":"EcsImage",
 "ScopeId":"crr-nyrh2oko32xb****",
 "Code":"0"
}
```

#### DeleteArtifactBuildRule

删除镜像仓库加速镜像构建规则。

**请求头**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Host | 是 | cn-wl-en**** | 区域ID |
| InstanceId | Strin g | Query | 是 | cri-pri**** | 实例 ID。 |
| BuildRuleI d | Strin g | Query | 否 | crabr-ly77w5i3t31f**** | 构建规则ID |
| ScopeTyp e | Strin g | Query | 否 | REPOSITORY | 规则生效范围，取值： REPOSITORY ，表示生效范围仓库级别。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ScopeId | Strin g | Query | 否 | crr-pmajihou6cg0**** | 规则生效范围的 ID，取值： ScopeId 配置为镜像仓库 ID。 |
| ArtifactTy pe | Strin g | Query | 否 | ACCELERATED IMAGE _ | 加速镜像类型，取值： ACCELERATED IMAGE _ ：表示生成加速镜像 |

|  |  | ACCELERATED IMAGE _ |
|---|---|---|

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | success | 返回码 |
| IsSuccess | Boolean | true | 是否成功 |
| RequestId | String | RQ1234567890abc def | 请求ID |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteArtifactBuildRule &RegionId=cn-wl-en**** &InstanceId=cri-pri****
```

正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "IsSuccess":true,
 "RequestId":"RQ1234567890abcdef",
 "Code":"0"
}
```

## 附录

### STS概要

#### 什么是STS

阿里云STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。RAM提供RAM用户和RAM角色两种身份。其中，RAM角色不具备永久身份凭证，而只能通过STS获取可以自定义时效和访问权限的临时身份凭证，即安全令牌（STS Token）。

**使用RAM用户扮演角色时获取STS Token**

有权限的RAM用户可以使用其访问密钥调用AssumeRole接口，以获取某个RAM角色的STS Token，从而使用STS Token访问阿里云资源。

**产品优势**

使用STS Token，减少长期访问密钥（Accesskey）泄露的风险。 STS Token具有时效性，可以自定义有效期，到期后将自动失效，无需定期轮换。 可以为STS Token绑定自定义权限策略，提供更加灵活和精细的云资源授权。

#### AssumeRole

RAM用户调用AssumeRole接口获取一个扮演RAM角色的临时身份凭证（STS Token）。该接口中RAM用户扮演的是可信实体为阿里云账号类型的RAM角色。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AssumeRole | 要执行的操作。取值：AssumeRole |
| RoleArn | String | 是 | acs:ram::123456 789012****:role/ adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM 角色。 |
| RoleSessionNa me | String | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API的用户身份，例如：用户名。在操作审计日志中，即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字、半角句号（.）、at（@）、短划线（-） 和下划线（ ）。 _ |

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

操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

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
if(Sti Util
```

iE

```
t( Rl))
```

t

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

下列代码以调用ECS的 `DescribeZones` 接口为示例。

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

**错误码**

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | 角色ARN格式错误。 |
| 400 | InvalidParameter.Role Arn | The parameter RoleArn is wrongly formed. | 角色ARN格式错误 |
| 400 | InvalidParameter.Role SessionName | The parameter RoleSessionName is wrongly formed. | RoleSessionName格式错误，支持输入2~64 个字符，请输入至少2个字符，允许输入英文字母、数字、半角句号 （.）、at（@）、短划线 （-）和下划线（ ）。 _ |
| 400 | InvalidParameter.Dura tionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | DurationSeconds参数设置错误，过期时间最小值为900秒，最大值为MaxSessionDurati on设置的时间。 |
| 400 | InvalidParameter.Polic yGrammar | The parameter Policy has not passed grammar check. | 权限策略语法错误。 |
| 400 | InvalidParameter.Polic ySize | The size of Policy must be smaller than 1024 bytes. | 权限策略长度超限，最大不超过1024字符。 |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | STS Token没有权限。 |
| 404 | EntityNotExist.Role | The specified Role not exists. | 指定的RAM角色不存在。 |
| 500 | InternalError | STS Server Internal Error happened. | 服务器内部错误。 |
