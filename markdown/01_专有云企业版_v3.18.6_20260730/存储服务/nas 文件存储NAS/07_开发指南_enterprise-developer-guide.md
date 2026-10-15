---
title: "文件存储NAS 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 120
source_pdf: "07_开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/nas/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 文件存储NAS 开发指南

文件存储NAS

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
文件存储NAS
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

本文为您介绍调用流程及可以参考的文档资料。

**流程图**

文件存储NAS

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数。具体操作，请参见获取AccessKey或获取STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取RegionID。
获取调用时所需要的RegionID参数。具体操作，请参见获取公共Header参数。
3. 获取组织ID与资源集ID。
组织ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrga nizationList章节。 资源集ID需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListRe sourceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 获取对应的API参考文档。
文件存储NAS 您需要查看目标云产品的开发指南，了解API的功能与使用方式。开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
文件存储NAS

## 准备工作

### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器。

**操作步骤**

1. 在浏览器地址栏中，输入Apsara Uni-manager运营控制台的服务域名地址，按回车键。
文件存储NAS

**说明**

单击页面右上角的当前语言可以切换其它语言。 由于浏览器证书过期或环境开启HTTPS认证等出现多次单击继续访问或无Apsara Unimanager运营控制台地址入口等现象，此时需要安装证书才能正常访问。单击页面右上角的**浏览器证书安装**，可打开浏览器证书安装指南。
2. 输入正确的用户名及密码。

**说明**

请向运营管理员获取登录控制台的用户名和密码。 首次登录Apsara Uni-manager运营控制台时，需要修改登录用户名的密码，请按照提示完成密码修改。为提高安全性，密码长度必须为10~32位，且包含英文字母大小写、阿拉伯数字和特殊符号（感叹号（!）、at（@）、井号（#）、美元符号（$）、百分号（%）等）。
3. 勾选**我已阅读并同意产品服务协议、隐私协议、用户协议**。

**说明**

登录页展示的链接文字为文档标题，单击链接文字，可查看协议的详细内容。
**产品服务协议**、**隐私协议**和**用户协议**仅在已发布时才会显示。如果三种类型协议都没有发布，
则不需要执行该操作。
4. 单击**账号登录**/**授权登录**。

**说明**

“授权登录”仅第三方认证的全局IdP设置启用时才会显示，且该显示名称可自定义，默认显示名称为“授权登录”。
5. 如果账号已激活MFA多因素认证，请根据以下两种情况进行操作：

**说明**

公网场景下，登录入口默认强制开启多因素认证。

**开启MFA后的首次登录**

a. 输入账号密码登录后，展示绑定虚拟MFA设备页面。 b. 在绑定虚拟MFA设备页面中，按页面提示步骤绑定虚拟MFA设备。 c. 登录成功，进入控制台。

**已开启并绑定MFA**

输入6位MFA码后单击**认证**。
6. 在页面上方的菜单栏，选择**产品** > **开发工具** > **开发者门户**。

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

文件存储NAS Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。本文将为您描述如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。具体操作，请 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足： 文件存储NAS 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 地域，例如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。 |
| x-acs-instanceid | 进行操作的实例ID，例如，NAS的实例ID可以从NAS文件系统列表中查询到。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。
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

### 获取STS AccessKey

本文为您介绍如何利用STS方式，调用专有云的产品API。

**背景信息**

文件存储NAS 阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以选择使用STS方式，调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。

**操作步骤**

1. 获取用户角色的 `RAM Role` 。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，选择**个人信息**。 iii. 单击**查看当前角色策略**。 在**当前选择角色策略**对话框中查看 `RAM Role` 。
2. 获取STS Accesskey三元组。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 文件存储NAS

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

`// sts.aliyuns.com`请替换为实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}。
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 业务参数，设置本次调用`Session`的别名，`<yourRoleSessionName>`请您替换为实际值。

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`Role`角色`ARN`，`<yourRoleArn>`请替换为上一步获取到的实际`R Role ARN`。

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

3. 通过STS AccessKey三元组调用云产品的接口，下列代码以NAS的 `DescribeRegions` 接口为示例。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 文件存储NAS

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为您实际的地域`ID`。 `// "<yourStsAccessKeyID>", "<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中

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
    request.setSysDomain("nas.aliyuns.com");
    request.setSysProduct("NAS");
    request.setSysAction("DescribeRegions");
    request.setSysVersion("2017-06-26");
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

`//` 非必填,请替换为您实际的资源集`ID`。

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为您实际的组织`ID`。

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

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并对调用后的一些返回值做出解释。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境Region，获取方式请参见获取Region ID。 |

文件存储NAS

| 名称 | 描述 |
|---|---|
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 进行操作的实例ID，获取方式请参见获取文件系统ID。 |

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

**获取文件系统ID**

文件系统ID可以通过Apsara Uni-manager运营控制台中的文件系统列表进行获取，获取步骤如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏中，选择**产品**>**存储**>**文件存储****NAS**。
3. 在左侧导航栏中，单击**文件系统列表**。
4. 在文件系统列表中查看**文件系统****ID**。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |

| 文件存储NAS | 开发指南·准备工作 |
|---|---|

| 名称 | 描述 |
|---|---|
| Department | 组织ID。 |

### 获取文件存储的SDK包

通过POP网关调用专有云API时，需使用相应云产品的SDK。本文为您介绍如何获取阿里云开发工具包 （SDK）。 软件开发工具包（SDK）包括代码以及示例，您可以自行选择语言创建云应用。 目前SDK的语言支持：Java、Python等，您可以前往阿里云开发工具包（SDK）中进行选择。

**说明**

推荐使用 Java、Python语言的SDK包，使用其他语言的SDK包可能发生不兼容情况。 SDK核心库推荐使用阿里云官网的SDK核心库，其内容所有云产品共用，且适用于专有云。 下表列举了文件存储常用语言的SDK的GitHub源码地址。

| SDK语言 | GitHub源码 |
|---|---|
| Java | NAS Java SDK |
| Python | NAS Python SDK |

文件存储NAS

## Java SDK调用示例

### 快速开始

本节介绍如何获取文件存储Java SDK并开始调用。

**环境准备**

使用阿里云专有云Java SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具使用NAS Java SDK前，您还需要获取文件存储的Endpoint。具体操作，请参见获取API信息及其 EndPoint。 阿里云专有云Java SDK支持1.8及以上版本的JDK。 如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。

**说明**

使用文件存储的开发工具包，必须安装阿里云Java SDK核心库以及NAS的SDK。其中，SDK核心库推荐使用4.5.17及以上版本，NAS Java SDK的版本为2.0.2。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数请替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

```java
import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsRequest; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsResponse; public class Main {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
       DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。 `//` 设置当前产品的`Endpoint`，可变参数请替换为您的实际值。

```
       profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
```

`//` 设置请求配置。

```
       HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

文件存储NAS

```
       clientConfig.setIgnoreSSLCerts(true);// 忽略证书。
```

clientConfig.setReadTimeoutMillis(<readTimeout>);// 读取超时时间（可选），单位为毫秒 （`ms`）。

```
       clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// 连接超时时间（可
```

选），单位为毫秒（`ms`）。 clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// 设置每个主机的最大请求数（可选）。 clientConfig.setMaxRequests(<maxRequests>);// 设置最大请求数（可选）。 clientConfig.setProtocolType(ProtocolType.HTTP); // 设置请求协议，默认`HTTP`（可选） 。 `/*` 设置代理（可选）,替换为代理`IP+Port`。

```
       clientConfig.setHttpProxy("http://192.168.XX.XX:33XX");
```

或

```
       clientConfig.setHttpsProxy("https://192.168.XX.XX:33XX");
```

`*/`

```
       profile.setHttpClientConfig(clientConfig);
       IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
       DescribeFileSystemsRequest request = new DescribeFileSystemsRequest();
```

`//` 业务参数。

```
       request.setPageSize(10);
       request.setPageNumber(1);
```

`//` 特殊`Header`参数，用于资源隔离，请替换为您实际的组织`ID`和资源集`ID`。

```
       request.putHeadParameter("x-acs-organizationid", "1");
       request.putHeadParameter("x-acs-resourcegroupid", "11");
```

`//` 发起请求并处理应答或异常。

```java
       DescribeFileSystemsResponse response;
       try {
           response = client.getAcsResponse(request);
fileSystem:rsp.getFileSystems()) {
               System.out.println(fileSystem.getFileSystemId());
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

本文介绍如何安装及调用文件存储Java SDK。 阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包 （SDK）的方式安装专有云Java SDK。 要使用文件存储的开发工具包，必须安装阿里云Java SDK核心库以及文件存储的Java SDK。SDK核心库推荐使用4.5.17及以上版本，Java SDK的版本为2.0.2。 文件存储NAS 以使用NAS的Java SDK为例，您需要安装阿里云Java SDK核心库和NAS Java SDK，并在pom.xml文件中添加以下依赖即可。准确的SDK版本号，请参见阿里云开发工具包（SDK）。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency> <!-- NAS Java SDK --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-nas</artifactId>
    <version>2.0.2</version>
</dependency>
```

#### 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍如何设置身份验证凭证。 目前，Java SDK支持通过AccessKey进行身份验证，获取AccessKey的具体操作，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**说明**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID` `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID` "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 文件存储NAS

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

本文介绍如何使用Java SDK发起请求。

**操作步骤**

1. 新建一个AcsClient。

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. 创建请求。
请求类的命名规范为 ${apiName}Request ，其中**${apiName}**为API名称，例在引入多个产品SDK时，有可能存在Request类同名的情况，请注意按照package区分。 文件存储NAS

```
DescribeFileSystemsRequest request = new DescribeFileSystemsRequest();
```

`//`业务参数

```
request.setFileSystemType("all"); request.setPageSize(10);
```

`//` 特殊`Header`参数，用于资源隔离，请替换为您实际的组织`ID`和资源集`ID`

```
request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. 发起调用并处理应答。

```java
try {
  DescribeFileSystemsResponse response = client.getAcsResponse(request);
  System.out.println(new Gson().toJson(response));
} catch (ServerException e) {
  e.printStackTrace();
} catch (ClientException e) {
  System.out.println("ErrCode:" + e.getErrCode());
  System.out.println("ErrMsg:" + e.getErrMsg());
  System.out.println("RequestId:" + e.getRequestId());
}
```

正常情况下，应答中的所有字段，都会被反序列化到response中，您可以直接调用 `response.getXXX()` 来获得应答中的字段。

```
instanceStatus = response.getStatus();
```

如果出现了异常，或您需要原始HTTP应答的情况下，您可以通过使用 `doAction()` 来获取原始应答。

```
HttpResponse response = client.doAction(request);
```

#### 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要Java SDK对返回的错误进行处理。您只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码： 文件存储NAS

```
try {
    FooResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`

```
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

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在NAS的API文档中获取以下参数的值。 域名(domain)：NAS产品服务地址。 API版本(version)：API版本号，格式为YYYY-MM-DD。 您可以在API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 例如CreateFileSystem接口，在发起CommonRequest请求时，需要使用 `request.setSysAction("CreateFileSystem")` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为NAS的DescribeFileSystems接口，查询文件系统信息的调用示例。 文件存储NAS 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 <http://192.168.XX.XX:33XX>，请替换为您实际的代理IP+端口。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 "<yourAccessKeySecret>"); // 请替换为您实际的`AccessKey Secret`。

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
```

请根据实际情况判断是否需要设置`HTTP`代理。 设置方法如下：

```
         clientConfig.setHttpProxy("http://192.168.XX.XX:33XX");
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
        request.setSysDomain("nas.cn-hangzhou.com");
        request.setSysProduct("NAS");
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.putQueryParameter("PageNumber", "1");
requestputQueryParameter("PageSize" "10");
```

文件存储NAS

```
        request.putQueryParameter(PageSize, 10);
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

`5.0`及之前历史版本需要），请替换为您实际的地域`ID`。

```
         request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// 非必填（修改
```

、删除、查询单实例详情时需要），请替换为您实际的实例`ID`。

```
        /**
```

当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段。 调用方法如下：

```
         request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
```

请替换为实际的`Token`。 `*/`

```java
        try {
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

文件存储NAS

## Python SDK调用示例

### 快速开始

本文介绍如何获取文件存储Python SDK并开始调用。

**环境准备**

使用Python SDK前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操作， 使用Python SDK前，您需要获取文件存储的Endpoint。具体操作，请参见获取API信息及其EndPoint。
1. 安装SDK核心库。
如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库。

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装文件存储的SDK。
如果您使用的是Python 2.x，执行以下命令，安装NAS SDK。

```
pip install aliyun-python-sdk-nas
```

如果您使用的是Python 3.x，执行以下命令，安装NAS SDK。

```
pip3 install aliyun-python-sdk-nas
```

**使用Python SDK**

以下示例展示调用Python SDK的3个主要步骤：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
文件存储NAS

```python
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID`

```bash
access_key = '<yourAccessKeyID>' # 请替换为您实际的AccessKey ID acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret
# product config
```

`product_name = 'NAS' #` 填写产品名称 `endpoint = 'nas.aliyuns.com' #` 产品访问域名

```bash
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式

```python
# get response
response = clt.do_action_with_exception(request) print(response)
```

### 使用手册

#### 安装Python SDK

本文档介绍如何安装阿里云Python SDK和文件存储Python SDK。
1. 安装阿里云Python SDK。
阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装专有云 Python SDK。 使用产品的开发工具包，都必须安装阿里云Python SDK核心库。例如，如果要使用

**说明**

NAS的Python SDK，您需要安装阿里云Python SDK核心库和NAS的Python SDK。 如果您使用的是Python 2.x，执行以下命令，安装阿里云SDK核心库。

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令，安装阿里云SDK核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装文件存储的SDK。
如果您使用的是Python 2.x，执行以下命令，安装文件存储的SDK。

```
pip install aliyun-python-sdk-nas
```

如果您使用的是Python 3.x，执行以下命令，安装文件存储的SDK。

```
pip3 install aliyun-python-sdk-nas
```

文件存储NAS

#### 设置身份验证凭证

当使用阿里云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。 目前Python SDK支持通过AccessKey进行身份验证，获取AccessKey的具体操作，请参见获取 AccessKey。 使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

**重要**

确保包含AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
clt = client.AcsClient(access_key, access_secret, region_id)
```

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

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 发起调用

文件存储NAS 本节介绍如何使用文件存储Python SDK发起请求。

**操作步骤**

1. 导入相关产品的SDK。

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
```

2. 新建一个AcsClient。

```
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. 创建Request对象。

```
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回。

```python
response = clt.do_action_with_exception(request) print(response)
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

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意Open API接口的调用。 文件存储NAS

**CommonRequest调用特点**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在各产品的API文档中获取以下参数的值。 域名(domain)：NAS产品服务地址。 API版本(version)：NAS API版本号，格式为YYYY-MM-DD。 您可以在NAS API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取**Action**参数，使用 `request.set_action_name("Action")` 的方式来指定API名称。 例如CreateFileSystem接口，在发起CommonRequest请求时，需要使用 `request.set_action_name("CreateFileSystem")` 来指定API名称。

**示例：调用RPC风格的API**

以下代码为NAS的DescribeFileSystems接口，查询文件系统信息的调用示例。 以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>，请替换为您实际的地域ID。 <yourAccessKeyID>，请替换为您实际的AccessKey ID。 <yourAccessKeySecret>，请替换为您实际的AccessKey Secret。 <yourSecurityToken>，请替换为您实际的SecurityToken。 <yourResourceGroupID>，请替换为您实际的资源集ID。 <yourOrganizationID>，请替换为您实际的组织ID。 <yourInstanceID>，请替换为您实际的实例ID。 文件存储NAS

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
```

# 请替换为您实际的`AccessKey ID`、`AccessKey Secret`、地域`ID`

```bash
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('NAS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26') request.set_domain('<nas.aliyuncs.com>') #产品访问域名
# or:
# request = = CommonRequest(product='NAS',
action_name='DescribeFileSystems',version='2017-06-26',domain='nas.aliyuncs.com')
######
```

# 设置请求协议类型,支持`https`或`http,`默认为`http`
# 设置`https`方法如下：

```bash
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber','1') request.add_query_param('PageSize','30')
######
```

# 当使用`STS AccessKey`调用接口时，需要在参数中加上`SecurityToken`字段
# 调用方法如下：
# 请替换为您实际的`SecurityToken`

```bash
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
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

文件存储NAS

## API参考

### API概览

NAS提供的API接口如API接口所示。 表 1. API接口

| 类别 | API | 描述 |
|---|---|---|
| 地域 | DescribeRegions | 返回所有RegionId |
|  | DescribeZones | 查询一个地域下的所有可用区及可用区所支持的NAS类型 |
| 文件系统 | CreateFileSystem | 创建新的文件系统 |
|  | DeleteFileSystem | 删除已有文件系统 |
|  | DescribeFileSystems | 返回文件系统描述信息 |
|  | ModifyFileSystem | 修改文件系统信息 |
| 挂载点 | CreateMountTarget | 创建挂载点 |
|  | DeleteMountTarget | 删除已有挂载点 |
|  | DescribeMountTargets | 返回挂载点描述信息 |
|  | ModifyMountTarget | 修改挂载点信息 |
|  | DescribeMountedClients | 查询挂载点客户端 |
|  | CreateAccessGroup | 创建权限组 |
|  | DeleteAccessGroup | 删除已有权限组 |
|  | DescribeAccessGroups | 返回权限组描述信息 |
|  | ModifyAccessGroup | 修改权限组 |

文件存储NAS

| 权限组 |  |  |
|---|---|---|
|  | CreateAccessRule | 创建权限组规则 |
|  | DeleteAccessRule | 删除已有权限组规则 |
|  | DescribeAccessRules | 返回权限规则描述信息 |
|  | ModifyAccessRule | 修改权限规则 |
| 配额 | SetDirQuota | 设置文件系统的目录配额 |
|  | CancelDirQuota | 取消文件系统的目录配额 |
|  | DescribeDirQuotas | 查询文件系统的目录配额 |
| 统一命名空间 | CreateNamespace | 创建命名空间 |
|  | DeleteNamespace | 删除命名空间 |
|  | ModifyNamespace | 修改命名空间描述 |
|  | DescribeNamespaces | 查询命名空间信息 |
|  | AddFileSystemToNamespace | 添加文件系统到命名空间 |
|  | RemoveFileSystemFromNamespac | 删除命名空间中的一个文件系统 |
|  | RenameMappedPathInNamespace | 修改命名空间中一个文件系统的映射名 |
|  | ListFileSystemsInNamespace | 列出命名空间中映射的文件系统 |
|  | CreateNamespaceMountTarget | 创建命名空间挂载点 |
|  | DeleteNamespaceMountTarget | 删除命名空间挂载点 |
|  | ModifyNamespaceMountTarget | 修改命名空间挂载点信息 |
|  | DescribeNamespaceMountTargets | 查询命名空间挂载点信息 |

文件存储NAS

|  | AddNamespaceToGroup | 创建跨域挂载编排 |
|---|---|---|
|  | RemoveNamespaceFromGroup | 删除跨域挂载编排 |
|  | DescribeNamespaceGroup | 查询跨域编排列表页 |
| 生命周期管理 | CreateLifecyclePolicy | 创建生命周期管理策略 |
|  | DeleteLifecyclePolicy | 删除生命周期管理策略 |
|  | ModifyLifecyclePolicy | 修改生命周期管理策略 |
|  | DescribeLifecyclePolicies | 查询生命周期管理策略信息 |
|  | EnableNfsAcl | 开启NFS ACL功能 |
| NFS NAS ACL |  |  |
|  | DisableNfsAcl | 关闭NFS ACL功能 |
|  | DescribeNfsAcl | 查询指定文件系统是否启用NFS ACL功能 |

### 调用方式

#### 公共参数

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。 表 1. 公共请求参数

| 参数名称 | 类型 | 必选 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回值的类型，支持JSON与XML。默认为JSON。 |
| Version | String | 是 | API 版本号为日期形式： YYYY-MM-DD ， 本版本为2017-06-26。 |

文件存储NAS

| AccessKeyId | String | 是 |  | 用户访问服务所用的密钥 ID。更多信息，请参见获取AccessKey。 |  |  |
|---|---|---|---|---|---|---|
| Signature | String | 是 |  | 签名结果串。 |  |  |
| SignatureMethod | String | 是 |  | 签名方式，目前支持HMAC-SHA1。 |  |  |
| Timestamp | String | 是 |  | 请求的时间戳。日期格式按照 ISO8601 标准表示，使用 UTC 时间，具体为 YYYY-MM- DDThh:mm:ssZ 。例如，2017-05- 26T12:00:00Z。 |  |  |
|  |  |  |  |  | YYYY-MM- |  |
|  |  |  |  | DDThh:mm:ssZ |  |  |
| SignatureVersion | String | 是 |  | 签名算法版本，目前版本是1.0。 |  |  |
| SecurityToken | String | 否 |  | 使用STS凭证类型时，要求传入。 |  |  |
| SignatureNonce | String | 否 |  | 唯一随机数，用于防止网络重放攻击。用户在不同请求间要使用不同的随机数值。 |  |  |

**请求示例**

```
GET https://nas.regionid.example.com/?Action=<Action> &Format=xml &Version=2017-06-26 &AccessKeyId=key-test &Signature=Pc5***%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &Timestamp=2012-06-01T12:00:00Z
```

…

**公共返回参数**

用户发送的每次接口调用请求，无论成功与否，系统都会返回一个唯一识别码**RequestId**给用户。 表 2. 公共返回参数文件存储NAS

| 参数名称 | 类型 | 描述 |
|---|---|---|
| RequestId | Integer | 系统返回的唯一识别码。 |

**返回示例**

XML示例

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

<接口名称`+Response>` <!--返回请求标签`-->`

```xml
  <RequestId> 6D9F62C5-BF52-447C-AA34-C77F7AFCCC12</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON示例

```json
{
  "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

#### 请求结构

**服务地址**

**通信协议**

支持HTTP或HTTPS协议进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如 `DescribeRegions` ）、每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用 `UTF-8` 字符集进行编码。

### 地域

#### DescribeRegions

**请求参数**

文件存储NAS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 接口名称。 取值：DescribeRegions |
| PageSize | Integer | 否 | 10 | 分页查询时，每页包含的地域数。 取值范围：1~100 默认值：10 |
| PageNumber | Integer | 否 | 1 | 列表的分页页码。 起始值（默认值）：1 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 列表的分页页码。 |
| PageSize | Integer | 2 | 每个分页包含的地域个数。 |
| Regions | Array of Region |  | 地域信息集合。 |
| Region |  |  |  |
| LocalName | String | East China 1 | 地域名称。 |
| RegionEndpoin t | String | nas.cn- hangzhou.aliyuncs. com | 对应地域的服务入口地址。 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| RequestId | String | A70BEE5D-76D3- 49FB-B58F- 1F398211**** | 请求ID。 |
| TotalCount | Integer | 4 | 查询到的地域总个数。 |

**示例**

请求示例文件存储NAS `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>4</TotalCount> <PageSize>2</PageSize> <RequestId>A70BEE5D-76D3-49FB-B58F-1F398211****</RequestId> <PageNumber>1</PageNumber> <Regions>
    <RegionId>cn-hangzhou</RegionId>
    <RegionEndpoint>nas.cn-hangzhou.aliyuncs.com</RegionEndpoint>
    <LocalName>East China 1</LocalName>
</Regions>
```

`JSON` 格式

```json
{
    "TotalCount": 4,
    "PageSize": 2,
    "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211****",
    "PageNumber": 1,
    "Regions": {
        "RegionId": "cn-hangzhou",
        "RegionEndpoint": "nas.cn-hangzhou.aliyuncs.com",
        "LocalName": "East China 1"
    }
}
```

#### DescribeZones

调用DescribeZones查询一个地域下的所有可用区及可用区所支持的NAS类型。 只发布中国站

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeZones | 操作接口名。取值：DescribeZones |
| RegionId | String | 是 | cn-hangzhou | 地域ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |

文件存储NAS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | A70BEE5D-76D3- 49FB-B58F- 1F398211A5C3 | 请求ID。 |
| Zones | Array of Zone |  | 可用区信息。 |
| Zone |  |  |  |
| Capacity | List | 1 | 容量型NAS。 |
| Clusters | Array of Cluster |  | 集群信息集合。 |
| Cluster |  |  |  |
| ClusterId | String | StandarNasCluster | 集群ID。 |
| ClusterType | String | NAS | 集群类型。 |
| ClusterVersion | String | 3.16.0 | 集群版本。 |
| InstanceTypes | Array of InstanceType |  | 实例类型。 |
| InstanceType |  |  |  |
| ProtocolType | String | NFS | 文件传输协议类型。 取值： NFS：NFS文件传输协议。 SMB：SMB文件传输协议。 |
| StorageType | String | Performance | 存储类型。 取值： Performance：性能型 Capacity：容量型 |

文件存储NAS

| SupportedFeat ures | List | ["ACL","Quota","Lif ecycle","Namespac e"] | NAS支持的高级功能。 包括： ACL：访问控制 Quota：配额 Lifecycle：生命周期管理策略 Namespce：统一命名空间 |
|---|---|---|---|
| Performance | List | 0 | 性能型NAS。 |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A70BEE5D-76D3-49FB-B58F-1F398211A5C3</RequestId> <Zones>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <Clusters>
        <ClusterVersion>3.16.0</ClusterVersion>
        <ClusterId>StandarNasCluster</ClusterId>
        <ClusterType>NAS</ClusterType>
        <InstanceTypes>
            <StorageType>Performance</StorageType>
            <ProtocolType>NFS</ProtocolType>
            <SupportedFeatures>["ACL","Quota","Lifecycle","Namespace"]
</SupportedFeatures>
        </InstanceTypes>
    </Clusters>
    <Capacity>1</Capacity>
    <Performance>0</Performance>
</Zones>
```

`JSON` 格式文件存储NAS

```json
{
    "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211A5C3",
    "Zones": {
        "ZoneId": "cn-hangzhou-b",
        "Clusters": {
            "ClusterVersion": "3.16.0",
            "ClusterId": "StandarNasCluster",
            "ClusterType": "NAS",
            "InstanceTypes": {
                "StorageType": "Performance",
                "ProtocolType": "NFS",
                "SupportedFeatures": "[\"ACL\",\"Quota\",\"Lifecycle\",\"Namespace\"]"
            }
        },
        "Capacity": 1,
        "Performance": 0
    }
}
```

**错误码**

| HttpCod e | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | 由于未知错误造成请求失败，请稍后再试。 |
| 404 | InvalidRegionId.Not Found | The specified Region is not found. | 请求的地域不存在或暂未提供服务。 |

### 文件系统

#### CreateFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateFileSyste m | 接口名称。 取值：CreateFileSystem |

文件存储NAS

| ProtocolType | String | 是 | NFS | 文件传输协议类型。 取值： NFS：NFS文件传输协议。 SMB：SMB文件传输协议。 |
|---|---|---|---|---|
| StorageType | String | 是 | Performance | 存储类型。 取值： Performance：性能型 Capacity：容量型 |
| ZoneId | String | 否 | cn-hangzhou-b | 可用区ID。 可用区是指在同一地域内，电力和网络互相独立的物理区域。 说明同一地域不同可用区之间的文件系统与ECS云服务器互通。 建议文件系统与云服务器 ECS属于同一可用区，避免跨可用区产生的时延。 |
| EncryptType | Integer | 否 | 1 | 文件系统是否加密。 使用KMS服务托管密钥，对文件系统落盘数据进行加密存储。在读写加密数据时， 无需解密。 取值： 0：不加密 1：加密 |
| Description | String | 否 | balabala | 文件系统描述。 限制： 长度为2~128个英文或中文字符。 必须以大小写字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |
| VolumeSize | Long | 否 | 100 | 通用型NAS容量大小。 单位：Byte 取值： 容量型：0~10 PB 性能型：0~1 PB |

文件存储NAS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | 完成创建的文件系统ID。 |
| RequestId | String | 98696EF0-1607- 4E9D-B01D- F20930B6**** | 请求ID。 |

**示例**

请求示例

```
&ProtocolType=NFS &StorageType=Performance
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>98696EF0-1607-4E9D-B01D-F20930B6****</RequestId> <FileSystemId>1ca404****</FileSystemId>
```

`JSON` 格式

```json
{
    "RequestId": "98696EF0-1607-4E9D-B01D-F20930B6****",
    "FileSystemId": "1ca404****"
}
```

#### DeleteFileSystem

**接口说明**

仅当文件系统的挂载点数目为0时，支持删除文件系统实例。 文件系统实例一旦删除，数据将不可恢复，请谨慎操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteFileSyste m | 接口名称。 取值：DeleteFileSystem |
| FileSystemId | String | 是 | 1ca404**** | 待删除的文件系统ID。 |

文件存储NAS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=1ca404****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****"
}
```

#### ModifyFileSystem

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyFileSyste m | 接口名称。 取值：ModifyFileSystem |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| Description | String | 否 | 空 | 文件系统描述。 限制： 长度为2~128个英文或中文字符。 必须以大小写字母或中文开头，不能以 http://和https://开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |

文件存储NAS

| VolumeSize | Long | 否 | 1000 | 文件系统容量。 取值： 容量型：0~10 PB 性能型：0~1 PB |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=1ca404****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****"
}
```

#### DescribeFileSystems

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeFileSyst ems | 接口名称。 取值：DescribeFileSystems |
| FileSystemId | String | 否 | 109c04**** | 文件系统ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 取值：standard：通用型NAS |

文件存储NAS

| VpcId | String | 否 | vpc- bp1sevsgtqvk5g xbl**** | 专有网络ID。 必须与待挂载的云服务器ECS选择一样的 VPC网络。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 1 | 分页查询时，每个分页包含的文件系统个数。 取值范围：1~100 默认值：10 |
| PageNumber | Integer | 否 | 1 | 文件系统列表的分页页码。 起始值（默认值）：1 |
| UseUTCDateTim e | Boolean | 否 | true | 指定返回的时间是否按照UTC标准格式表示。 取值： true（默认值）：返回的时间为UTC标准格式。 false：返回的时间为非UTC标准格式。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageNumber | Integer | 1 | 文件系统列表的分页页码。 起始值（默认值）：1。 |
| PageSize | Integer | 1 | 每个分页包含的文件系统个数。 |
| RequestId | String | 035B3A3A-E514- 4B41-B906- 5D906CFB**** | 请求ID。 |
| TotalCount | Integer | 1 | 文件系统的总个数。 |
| FileSystems | Array of FileSystem |  | 文件系统的描述信息集合。 |
| FileSystem |  |  |  |
| Bandwidth | Long | 150 | 文件系统的带宽。 单位：MB/s。通用型NAS没有该字段。 |

文件存储NAS

| ChargeType | String | PayAsYouGo | 计费类型。 包括： Subscription：包年包月 PayAsYouGo：按量付费 Package：已绑定存储包 |
|---|---|---|---|
| CreateTime | String | 2017-05- 27T15:43:06CST | 文件系统的创建时间。 |
| Description | String | This can be the description of the created file system. | 文件系统的描述信息。 |
| EncryptType | Integer | 1 | 加密类型。 包括： 0：不加密 1：加密 |
| ExpiredTime | String | 1572174830000 | 文件系统到期时间。 |
| FileSystemId | String | 109c04**** | 文件系统ID。 |
| FileSystemTyp e | String | all | 文件系统类型。 |
| MeteredIASize | Long | 1000 | 低频介质存储量。 |
| MeteredSize | Long | 1611661312 | 文件系统的使用量。 非实时使用量，为上一小时最大使用量，单位： Byte。 |
| MountTargets | Array of MountTarget |  | 挂载点信息集合。 |
| MountTarget |  |  |  |
| AccessGroupN ame | String | test-001 | 挂载点使用的权限组名称。 |
| MountTargetD omain | String | 109c042666- w****.cn- hangzhou.nas.aliyu ncs.com | 挂载点域名。 |

文件存储NAS

| NetworkType | String | vpc | 网络类型。 包括： vpc：专有网络 classic：经典网络 |
|---|---|---|---|
| Status | String | active | 挂载点状态。 包括： Active：可用 Inactive：不可用 |
| VpcId | String | vpc- bp1sevsgtqvk5gxbl **** | 专有网络ID。 |
| VswId | String | vsw- bp1omfzsszekkvax n**** | 交换机ID。 |
| Packages | Array of Package |  | 存储包信息集合。 |
| Package |  |  |  |
| ExpiredTime | String | 2020-01- 05T16:00:00Z | 存储包到期时间。 |
| PackageId | String | naspackage- 0be9c4b624- 37**** | 存储包ID。 |
| PackageType | String | hybrid | 存储包类型。 |
| Size | Long | 107374182400 | 存储包容量大小。 |
| StartTime | String | 2019-12- 05T01:40:56Z | 存储包起始时间。 |
| ProtocolType | String | NFS | 文件系统协议类型。 包括： NFS：NFS文件协议 SMB：SMB文件协议 |
| QuotaSize | Long | 100 | 文件系统容量。 |
| RegionId | String | cn-hangzhou | 地域ID。 |

文件存储NAS

| Status | String | Pending | 文件系统状态。包括： Pending：当前文件系统正在处理任务中。 Running：当前文件系统可用，当状态为 Running时才可以进行后续操作（例如：创建挂载点等）。 Stopped：当前文件系统不可用。 Extending：当前文件系统扩容中。 Stopping：当前文件系统停机中。 Deleting：当前文件系统删除中。 |
|---|---|---|---|
| StorageType | String | Performance | 存储类型。包括： Capacity（容量型） Performance（性能型） |
| SupportedFeat ures | List | Lifecycle | 文件系统支持的功能。 包括： Lifecycle：生命周期管理。 Quota：配额管理。 |
| VolumeSize | Long | 1000 | 通用型NAS容量。 包括： 容量型：0~10 PB 性能型：0~1 PB |
| ZoneId | String | cn-hangzhou-b | 文件系统所在的可用区。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeFileSystems
```

`&<`公共请求参数> 正常返回示例 `XML` 格式文件存储NAS

```xml
<FileSystems>
    <Status>Pending</Status>
    <StorageType>Performance</StorageType>
    <Description>This can be the description of the created file system.</Description>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <MeteredIASize>1000</MeteredIASize>
    <CreateTime>2017-05-27T15:43:06CST</CreateTime>
    <QuotaSize>100</QuotaSize>
    <MeteredSize>1611661312</MeteredSize>
    <EncryptType>1</EncryptType>
    <ChargeType>PayAsYouGo</ChargeType>
    <ProtocolType>NFS</ProtocolType>
    <Bandwidth>150</Bandwidth>
    <FileSystemType>all</FileSystemType>
    <ExpiredTime>1572174830000</ExpiredTime>
    <FileSystemId>109c04****</FileSystemId>
    <RegionId>cn-hangzhou</RegionId>
    <VolumeSize>1000</VolumeSize>
</FileSystems> <FileSystems>
    <MountTargets>
        <Status>active</Status>
        <VswId>vsw-bp1omfzsszekkvaxn****</VswId>
        <VpcId>vpc-bp1sevsgtqvk5gxbl****</VpcId>
        <MountTargetDomain>109c042666-w****.cn-
hangzhou.nas.aliyuncs.com</MountTargetDomain>
        <NetworkType>vpc</NetworkType>
        <AccessGroupName>test-001</AccessGroupName>
    </MountTargets>
    <Packages>
        <StartTime>2019-12-05T01:40:56Z</StartTime>
        <PackageId>naspackage-0be9c4b624-37****</PackageId>
        <Size>107374182400</Size>
        <ExpiredTime>2020-01-05T16:00:00Z</ExpiredTime>
        <PackageType>hybrid</PackageType>
    </Packages>
</FileSystems> <FileSystems>
    <SupportedFeatures>Lifecycle</SupportedFeatures>
</FileSystems> <FileSystems>
    <Ldap>
        <SearchBase>dc=example</SearchBase>
        <URI>ldap://ldap.example.example</URI>
        <BindDN>cn=alibaba,dc=com</BindDN>
    </Ldap>
</FileSystems> <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>035B3A3A-E514-4B41-B906-5D906CFB****</RequestId> <PageNumber>1</PageNumber>
```

`JSON` 格式文件存储NAS

| { "FileSystems": [ { "Status": "Pending", "StorageType": "Performance", "Description": "This can be the description of the created file system.", "ZoneId": "cn-hangzhou-b", "MeteredIASize": 1000, "CreateTime": "2017-05-27T15:43:06CST", "QuotaSize": 100, "MeteredSize": 1611661312, "EncryptType": 1, "ChargeType": "PayAsYouGo", "ProtocolType": "NFS", "Bandwidth": 150, "FileSystemType": "all", "ExpiredTime": 1572174830000, "FileSystemId": "109c04****", "RegionId": "cn-hangzhou", "VolumeSize": 1000 }, { "MountTargets": { "Status": "active", "VswId": "vsw-bp1omfzsszekkvaxn****", "VpcId": "vpc-bp1sevsgtqvk5gxbl****", "MountTargetDomain": "109c042666-w****.cn-hangzhou.nas.aliyuncs.com", "NetworkType": "vpc", "AccessGroupName": "test-001" }, "Packages": { "StartTime": "2019-12-05T01:40:56Z", "PackageId": "naspackage-0be9c4b624-37****", "Size": 107374182400, "ExpiredTime": "2020-01-05T16:00:00Z", "PackageType": "hybrid" } }, { "SupportedFeatures": "Lifecycle" }, { "Ldap": { "SearchBase": "dc=example", "URI": "ldap://ldap.example.example", "BindDN": "cn=alibaba,dc=com" } } ], "TotalCount": 1, "PageSize": 1, "RequestId": "035B3A3A-E514-4B41-B906-5D906CFB****", "PageNumber": 1 } |  |
|---|---|

文件存储NAS

### 挂载点

#### CreateMountTarget

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateMountTar get | 接口名称。 取值：CreateMountTarget |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 默认权限组： DEFAULT VPC GROUP NAME（专有网 _ _ _ 络默认权限组）、 DEFAULT CLASSIC GROUP NAME（经 _ _ _ 典网络默认权限组）。 |
| FileSystemId | String | 是 | 174494**** | 文件系统ID。 |
| NetworkType | String | 是 | VPC | 挂载点网络类型。 取值： Vpc：专有网络 Classic：经典网络 |
| VpcId | String | 否 | vpc- 2zesj9afh3y518 k9o**** | 专有网络ID。 当网络类型是专有网络，此字段必填且有意义。 |
| VSwitchId | String | 否 | vsw- 2zevmwkwyztju offg**** | 交换机ID。 当网络类型是专有网络，此字段必填且有意义。 |
| SecurityGroupId | String | 否 | sg- bp1fg655nh68x yz9**** | 安全组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | 挂载点域名。 |

文件存储NAS

| RequestId | String | 70EACC9C-D07A- 4A34-ADA4- 77506C42**** | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
&AccessGroupName=classic-test &FileSystemId=174494**** &NetworkType=VPC
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>70EACC9C-D07A-4A34-ADA4-77506C42****</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
```

`JSON` 格式

```json
{
    "RequestId": "70EACC9C-D07A-4A34-ADA4-77506C42****",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
}
```

#### DeleteMountTarget

**接口说明**

删除挂载点后，无法恢复，请谨慎操作。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteMountTar get | 接口名称。 取值：DeleteMountTarget |
| FileSystemId | String | 是 | 174494**** | 文件系统ID。 |
| MountTargetDo main | String | 是 | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | 挂载点域名。 |

**返回数据**

文件存储NAS

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=174494**** &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****"
}
```

#### DescribeMountTargets

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeMountT argets | 接口名称。 取值：DescribeMountTargets |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| MountTargetDo main | String | 否 | 1ca404a666- x****.cn- hangzhou.nas.al iyuncs.com | 挂载点域名。 |
| PageSize | Integer | 否 | 1 | 每个分页包含的挂载点个数。 取值范围：1~100 默认值：10 |

文件存储NAS

| PageNumber | Integer | 否 | 1 | 列表的分页页码。 起始值（默认值）：1 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MountTargets | Array of MountTarget |  | 挂载点描述信息集合。 |
| MountTarget |  |  |  |
| AccessGroup | String | DEFAULT VPC GRO _ _ UP NAME _ | 挂载点所应用的权限组名称。 |
| MountTargetD omain | String | 1ca404a666- w****.cn- hangzhou.nas.aliyu ncs.com | 挂载点域名。 |
| NetworkType | String | Vpc | 网络类型。 |
| Status | String | Active | 当前挂载点状态。 包括： Active：可用 Inactive：不可用说明当状态为Active时才可以挂载文件系统。 |
| VpcId | String | vpc- 2zesj9afh3y518k9o **** | 专有网络ID。 |
| VswId | String | vsw- 2zevmwkwyztjuoff g**** | 交换机ID。 |
| PageNumber | Integer | 1 | 列表的分页页码。 |
| PageSize | Integer | 1 | 每个分页包含的挂载点个数。 |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | 请求ID。 |
| TotalCount | Integer | 1 | 挂载点总数。 |

**示例**

文件存储NAS 请求示例

```
http(s)://[Endpoint]/?Action=DescribeMountTargets &FileSystemId=1ca404****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>3BAB90FD-B4A0-48DA-9F09-2B963510A0EF</RequestId> <PageNumber>1</PageNumber> <MountTargets>
    <Status>Active</Status>
    <VswId>vsw-2zevmwkwyztjuoffg****</VswId>
    <VpcId>vpc-2zesj9afh3y518k9o****</VpcId>
    <MountTargetDomain>1ca404a666-w****.cn-
hangzhou.nas.aliyuncs.com</MountTargetDomain>
    <AccessGroup>DEFAULT_VPC_GROUP_NAME</AccessGroup>
    <NetworkType>Vpc</NetworkType>
</MountTargets>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "3BAB90FD-B4A0-48DA-9F09-2B963510A0EF",
    "PageNumber": 1,
    "MountTargets": {
        "Status": "Active",
        "VswId": "vsw-2zevmwkwyztjuoffg****",
        "VpcId": "vpc-2zesj9afh3y518k9o****",
        "MountTargetDomain": "1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com",
        "AccessGroup": "DEFAULT_VPC_GROUP_NAME",
        "NetworkType": "Vpc"
    }
}
```

#### ModifyMountTarget

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyMountTar get | 接口名称。 取值：ModifyMountTarget |

文件存储NAS

| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
|---|---|---|---|---|
| MountTargetDo main | String | 是 | 1ca404a666- w****.cn- hangzhou.nas.al iyuncs.com | 挂载点。 |
| AccessGroupNa me | String | 否 | classic-test | 挂载点绑定的权限组。 |
| Status | String | 否 | Inactive | 挂载点状态。 取值： Active：可用 Inactive：不可用 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | FF387D95-34C4- 4879-B65A- 99D1FA1**** | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=1ca404**** &MountTargetDomain=1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>FF387D95-34C4-4879-B65A-99D1FA1****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "FF387D95-34C4-4879-B65A-99D1FA1****"
}
```

#### DescribeMountedClients

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 文件存储NAS

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | 是 | cn-hangzhou-balbala | 地域值。 |
| FileSyste mId | Strin g | Query | 是 | 1ca404**** | 文件系统id。 |
| MountTar getDomai n | Strin g | Query | 是 | 1ca404a666-x****.cn- hangzhou.nas.aliyuncs.c om | 挂载点域名。 |
| ClientIP | Strin g | Query | 否 | 192.**.16.17 | 客户端ip。 |
| PageSize | Integ er | Query | 否 | 1 | 每个分页包含的挂载点个数。取值范围：1~100默认值：10。 |
| PageNum ber | Integ er | Query | 否 | 1 | 列表的分页页码。起始值 （默认值）：1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Clients | Array | 192.***.6.17 | 挂载客户端ip列表。 |
| -ClientIP | String | 192.***.6.17 | 客户端ip。 |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | 请求id。 |
| TotalCount | Integer | 3 | 总计条数。 |
| PageSize | Integer | 1 | 每个分页包含的挂载点个数。取值范围：1~100 默认值：10。 |
| PageNumber | Integer | 1 | 列表的分页页码。起始值（默认值）：1。 |

**示例**

请求示例文件存储NAS

```
http(s)://[Endpoint]/?Action=DescribeMountedClients &RegionId=cn-hangzhou-balbala &FileSystemId=1ca404**** &MountTargetDomain=1ca404a666-x****.cn-hangzhou.nas.aliyuncs.com
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
  "TotalCount": 10,
  "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211****",
  "PageSize": 10,
  "PageNumber": 1,
  "Clients": {
    "Client": [
      {
        "ClientIP": "10.10.10.1"
      }
```

]

```
  }
}
```

### 权限组

#### CreateAccessGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateAccessGr oup | 接口名称。 取值：CreateAccessGroup |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 限制： 长度为3~64个字符。 必须以大小写字母开头，可以包含英文字母、数字、下划线（ ）或者短划线 _ （-）。 新创建的权限组名称不能与两个默认的权限组相同。 默认权限组： DEFAULT VPC GROUP NAME（专有网 _ _ _ 络默认权限组）、 DEFAULT CLASSIC GROUP NAME（经 _ _ _ 典网络默认权限组）。 |

文件存储NAS

| AccessGroupTyp e | String | 是 | Classic | 权限组类型。 取值： Vpc：专有网络 Classic：经典网络 |
|---|---|---|---|---|
| Description | String | 否 | classictestacces sgroup | 权限组描述。 限制： 默认和名称相同，长度为2~128个英文或中文字符。 必须以大小字母或中文开头，不能以 http://和https://开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划号（-）。 _ |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessGroupN ame | String | classic-test | 权限组名称。 |
| RequestId | String | 55C5FFD6-BF99- 41BD-9C66- FFF39189**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test &AccessGroupType=Classic
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>55C5FFD6-BF99-41BD-9C66-FFF39189****</RequestId> <AccessGroupName>classic-test</AccessGroupName>
```

`JSON` 格式

```json
{
    "RequestId": "55C5FFD6-BF99-41BD-9C66-FFF39189****",
    "AccessGroupName": "classic-test"
}
```

文件存储NAS

#### DeleteAccessGroup

**接口说明**

默认权限组（DEFAULT_VPC_GROUP_NAME和DEFAULT_CLASSIC_GROUP_NAME）不支持删除。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteAccessGr oup | 接口名称。 取值：DeleteAccessGroup |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****"
}
```

#### ModifyAccessGroup

文件存储NAS

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAccessGr oup | 接口名称。 取值：ModifyAccessGroup |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 限制： 长度为3~64个字符。 必须以大小写字母开头，可以包含英文字母、数字、下划线（ ）或者短划号 _ （-）。 |
| Description | String | 否 | classic-test | 权限组描述。 限制： 默认和权限组名称相同，长度为2~128 个英文或中文字符。 必须以大小写字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划号（-）。 _ |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | ED2AE737-9D50- 4CA4-B0DA- 31BD610C**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>ED2AE737-9D50-4CA4-B0DA-31BD610C****</RequestId>
```

文件存储NAS `JSON` 格式

```json
{
    "RequestId": "ED2AE737-9D50-4CA4-B0DA-31BD610C****"
}
```

#### DescribeAccessGroups

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccess Groups | 接口名称。 取值：DescribeAccessGroups |
| AccessGroupNa me | String | 否 | classic-test | 权限组名称。 |
| PageSize | Integer | 否 | 2 | 每个分页包含的权限组个数。 取值范围：1~100 默认值：10 |
| PageNumber | Integer | 否 | 1 | 列表的分页页码。 起始值（默认值）：1 |
| UseUTCDateTim e | Boolean | 否 | true | 指定返回的时间是否按照UTC标准格式表示。 取值： true（默认值）：返回的时间为UTC标准格式。 false：返回的时间为非UTC标准格式。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessGroups | Array of AccessGroup |  | 权限组描述信息集合。 |
| AccessGroup |  |  |  |
| AccessGroupN ame | String | classic-test | 权限组名称。 |

文件存储NAS

| AccessGroupT ype | String | Classic | 权限组类型。 包括： Vpc：专有网络 Classic：经典网络 |
|---|---|---|---|
| Description | String | This is a classic test access group~ | 权限组描述信息。 |
| MountTargetC ount | Integer | 0 | 应用此权限组的挂载点数量。 |
| RuleCount | Integer | 0 | 此权限组中包含的权限组规则数量。 |
| PageNumber | Integer | 1 | 列表的分页页码。 |
| PageSize | Integer | 2 | 每个分页包含的权限组个数。 |
| RequestId | String | 2514F97E-FFF0- 4A1F-BF04- 729CEAC64B6F | 请求ID。 |
| ResourceOwne rId | String | 258456 | 资源所属ID。 |
| TotalCount | Integer | 2 | 权限组的总个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAccessGroups
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<AccessGroups>
    <RuleCount>0</RuleCount>
    <AccessGroupType>Classic</AccessGroupType>
    <Description>This is a classic test access group~</Description>
    <MountTargetCount>0</MountTargetCount>
    <AccessGroupName>classic-test</AccessGroupName>
</AccessGroups> <TotalCount>2</TotalCount> <PageSize>2</PageSize> <RequestId>2514F97E-FFF0-4A1F-BF04-729CEAC64B6F</RequestId> <PageNumber>1</PageNumber> <ResourceOwnerId>258456</ResourceOwnerId>
```

文件存储NAS `JSON` 格式

```json
{
    "AccessGroups": {
        "RuleCount": 0,
        "AccessGroupType": "Classic",
        "Description": "This is a classic test access group~",
        "MountTargetCount": 0,
        "AccessGroupName": "classic-test"
    },
    "TotalCount": 2,
    "PageSize": 2,
    "RequestId": "2514F97E-FFF0-4A1F-BF04-729CEAC64B6F",
    "PageNumber": 1,
    "ResourceOwnerId": 258456
}
```

#### CreateAccessRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateAccessRul e | 接口名称。 取值：CreateAccessRule |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 |
| SourceCidrIp | String | 是 | 10.0.*.*/** | 授权对象的IP地址或网段。 格式必须为单一的IP地址或者CIDR网段。 说明经典网络类型的权限组只支持IP地址。 |
| RWAccessType | String | 否 | RDWR | 授权对象对文件系统的读写权限。 取值： RDWR（默认值）：读写 RDONLY：只读 |

文件存储NAS

| UserAccessType | String | 否 | no squash _ | 授权对象的系统用户对文件系统的访问权限。 取值： no squash（默认值）：允许使用root _ 用户访问文件系统。 root squash：以root用户身份访问 _ 时，映射nobody用户。 all squash：无论以何种用户身份访 _ 问，均映射为nobody用户。 nobody用户是Linux系统的默认用户，只能访问服务器上的公共内容，具有低权限、高安全性的特点。 |
|---|---|---|---|---|
| Priority | Integer | 否 | 1 | 权限组规则优先级。 当同一个授权对象匹配到多条规则时，高优先级规则生效。 取值范围：1~100，1为最高优先级。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessRuleId | String | 1 | 权限组规则ID。 |
| RequestId | String | A323836B-5BC6- 45A6-8048- 60675C23**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test &SourceCidrIp=10.0.*.*/**
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>A323836B-5BC6-45A6-8048-60675C23****</RequestId> <AccessRuleId>1</AccessRuleId>
```

`JSON` 格式文件存储NAS

```json
{
    "RequestId": "A323836B-5BC6-45A6-8048-60675C23****",
    "AccessRuleId": 1
}
```

#### DeleteAccessRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteAccessRul e | 接口名称。 取值：DeleteAccessRule |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 |
| AccessRuleId | String | 是 | 1 | 权限组规则ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5B4511A7-C99E- 4071-AA8C- 32E2529D**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test &AccessRuleId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5B4511A7-C99E-4071-AA8C-32E2529D****</RequestId>
```

`JSON` 格式文件存储NAS

```json
{
    "RequestId": "5B4511A7-C99E-4071-AA8C-32E2529D****"
}
```

#### ModifyAccessRule

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyAccessRul e | 接口名称。 取值：ModifyAccessRule |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 |
| AccessRuleId | String | 是 | 1 | 权限组规则ID。 |
| SourceCidrIp | String | 是 | 192.1**.*.* | IP地址或网段。 格式必须为单一的IP地址或者CIDR网段。 说明经典网络类型的权限组只支持IP地址。 |
| RWAccessType | String | 否 | RDWR | 授权对象对文件系统的读写权限。 取值： RDWR（默认值）：读写 RDONLY：只读 |
| UserAccessType | String | 否 | all squash _ | 授权对象的系统用户对文件系统的访问权限。 取值： no squash：允许使用root用户访问文 _ 件系统。 root squash：以root用户身份访问 _ 时，映射nobody用户。 all squash：无论以何种用户身份访 _ 问，均映射为nobody用户。 nobody用户是Linux系统的默认用户，只能访问服务器上的公共内容，具有低权限，高安全性的特点。 |

文件存储NAS

| Priority | Integer | 否 | 1 | 权限组规则优先级。 取值范围：1~100 默认值：1（最高优先级） |
|---|---|---|---|---|
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6299428C-3861- 435D-AE54- 9B330A00**** | 请求ID。 |

**示例**

请求示例

```
&AccessGroupName=classic-test &AccessRuleId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>6299428C-3861-435D-AE54-9B330A00****</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "6299428C-3861-435D-AE54-9B330A00****"
}
```

#### DescribeAccessRules

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeAccess Rules | 接口名称。 取值：DescribeAccessRules |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 |

文件存储NAS

| AccessRuleId | String | 否 | 1 | 规则序号。 |
|---|---|---|---|---|
| PageSize | Integer | 否 | 1 | 分页查询时，每个分页包含的文件系统个数。 取值范围：1~100 默认值：10 |
| PageNumber | Integer | 否 | 1 | 文件系统列表的分页页码。 起始值（默认值）：1 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard（通用型NAS） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| AccessRules | Array of AccessRule |  | 权限规则描述信息集合。 |
| AccessRule |  |  |  |
| AccessRuleId | String | 1 | 权限规则ID。 |
| Ipv6SourceCid rIp | String | 2001:250:6000::** * | 源端IPv6 CIDR地址段。 |
| Priority | Integer | 1 | 优先级。 当同一个授权对象匹配到多条规则时，高优先级规则生效。 取值范围：1~100，1为最高优先级。 |
| RWAccess | String | RDWR | 授权对象对文件系统的读写权限。 包括： RDWR（默认值）：读写 RDONLY：只读 |
| SourceCidrIp | String | 10.0.*.*/** | 地址或地址段。 |
| UserAccess | String | no squash _ | 用户权限类型：no squash（默认）、 _ root squash 和 all squash _ _ |
| PageNumber | Integer | 1 | 文件系统列表的分页页码。 |

文件存储NAS

| PageSize | Integer | 1 | 每个分页包含的权限规则个数。 |
|---|---|---|---|
| RequestId | String | 86D89E82-4297- 4343-8E1E- A2495B35CC70 | 请求ID。 |
| TotalCount | Integer | 1 | 权限规则的总个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeAccessRules &AccessGroupName=classic-test
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>86D89E82-4297-4343-8E1E-A2495B35CC70</RequestId> <PageNumber>1</PageNumber> <AccessRules>
    <RWAccess>RDWR</RWAccess>
    <UserAccess>no_squash</UserAccess>
    <Priority>1</Priority>
    <SourceCidrIp>10.0.*.*/**</SourceCidrIp>
    <Ipv6SourceCidrIp>2001:250:6000::***</Ipv6SourceCidrIp>
    <AccessRuleId>1</AccessRuleId>
</AccessRules>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "86D89E82-4297-4343-8E1E-A2495B35CC70",
    "PageNumber": 1,
    "AccessRules": {
        "RWAccess": "RDWR",
        "UserAccess": "no_squash",
        "Priority": 1,
        "SourceCidrIp": "10.0.*.*/**",
        "Ipv6SourceCidrIp": "2001:250:6000::***",
        "AccessRuleId": 1
    }
}
```

文件存储NAS

### 配额

#### SetDirQuota

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SetDirQuota | 接口名称。取值：SetDirQuota。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| Path | String | 是 | /data/sub1 | 目录在文件系统中的绝对路径。 |
| QuotaType | String | 是 | Accounting | 配额类型。 取值： Accounting：统计型配额，只统计使用量。 Enforcement：限制型配额，当使用量超过限制后，会导致创建文件或目录、 追加写入等操作失败。 |
| UserType | String | 是 | Uid | 用户类型。 取值： Uid：用户ID Gid：用户所属组ID AllUsers：所有用户 |
| UserId | String | 否 | 500 | 要限制的Uid或Gid。 当UserType=Uid或Gid时必填且有意义。 例如： 要限制Uid=500的用户，则UserType 填Uid，UserId填500。 要限制Gid=100的用户组，则 UserType填Gid，UserId填100。 |
| SizeLimit | Long | 否 | 1024 | 限制目录下文件总容量，单位为GB。 当QuotaType为Enforcement 时，SizeLimit和FileCountLimit至少填写其中一项。 |

文件存储NAS

| FileCountLimit | Long | 否 | 10000 | 限制目录下文件数目，包括文件、目录和特殊文件。 当QuotaType为Enforcement 时，SizeLimit和FileCountLimit至少填写其中一项。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |
| Success | Boolean | true | 请求状态。 包括： true：请求成功 false：请求失败 |

**示例**

请求示例

```
&FileSystemId=1ca404**** &Path=/data/sub1 &QuotaType=Accounting &UserType=Uid
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
}
```

#### CancelDirQuota

**请求参数**

文件存储NAS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CancelDirQuota | 系统规定参数。取值： CancelDirQuota。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| Path | String | 是 | /data/sub1 | 目录在文件系统中的绝对路径。 |
| UserType | String | 是 | Uid | 指定UserId的类型。 取值： Uid：用户ID Gid：用户所属组ID AllUsers：所有用户 |
| UserId | String | 否 | 500 | 要取消限制的uid或gid。 当UserType=Uid或Gid时必填且有意义。 例如： 要取消Uid=500的用户，则UserType 填Uid，UserId填500。 要取消Gid=100的用户组，则 UserType填Gid，UserId填100。 要取消所有用户，则UserType填 AllUsers，UserId可不填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |
| Success | Boolean | true | 请求状态。 取值： true：请求成功。 false：请求失败。 |

**示例**

请求示例

```
&FileSystemId=1ca404**** &Path=/data/sub1 &UserType=Uid
```

`&<`公共请求参数> 文件存储NAS 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
}
```

#### DescribeDirQuotas

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeDirQuot as | 接口名称。取值：DescribeDirQuotas。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| Path | String | 否 | /data/sub1 | 目录在文件系统中的绝对路径。 不填写时会返回文件系统中全部已设置了配额的目录。 |
| PageSize | Integer | 否 | 1 | 每个分页包含的目录个数。 |
| PageNumber | Integer | 否 | 1 | 分页页码。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| DirQuotaInfos | Array of DirQuotaInfo |  | 每个目录的配额信息列表。 |
| DirInode | String | 1123 | 目录的inode号。 |
| Path | String | /data/sub1 | 目录在文件系统中的绝对路径。 |

文件存储NAS

| Status | String | Normal | 目录的统计状态。 初始化时为Initializing；正常时为Normal。 |
|---|---|---|---|
| UserQuotaInfo s | Array of UserQuotaInfo |  | 每个用户的配额信息列表。 |
| FileCountLimit | Long | 10000 | 目录下用户的文件数目限制。 |
| FileCountReal | Long | 5100 | 目录下用户的实际文件数目。 |
| QuotaType | String | Accounting | 配额类型，包括统计型（Accounting）和限制型（Enforcement）。 |
| SizeLimit | Long | 1024 | 目录下用户的文件总容量限制，单位为GB。 |
| SizeReal | Long | 800 | 目录下用户的实际文件总容量，单位为GB。 |
| UserId | String | 500 | 要限制的uid或gid，取决于UserType的值。 |
| UserType | String | Uid | 指定UserId的类型，包括Uid、Gid、AllUsers 三种。 当指定为Uid或Gid时，UserId为必填。 当指定为AllUsers时，UserId为空。 |
| PageNumber | Integer | 1 | 分页页码。 |
| PageSize | Integer | 1 | 每个分页包含的目录个数。 |
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |
| TotalCount | Integer | 1 | 目录总个数。 |

**示例**

请求示例

```
&FileSystemId=1ca404****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式文件存储NAS

```xml
<TotalCount>1</TotalCount> <DirQuotaInfos>
    <Status>Normal</Status>
    <Path>/data/sub1</Path>
    <DirInode>1123</DirInode>
    <UserQuotaInfos>
        <FileCountLimit>10000</FileCountLimit>
        <UserId>500</UserId>
        <SizeLimit>1024</SizeLimit>
        <QuotaType>Accounting</QuotaType>
        <FileCountReal>5100</FileCountReal>
        <SizeReal>800</SizeReal>
        <UserType>Uid</UserType>
    </UserQuotaInfos>
</DirQuotaInfos> <PageSize>1</PageSize> <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <PageNumber>1</PageNumber>
```

`JSON` 格式

```json
{
    "TotalCount": 1,
    "DirQuotaInfos": {
        "Status": "Normal",
        "Path": "/data/sub1",
        "DirInode": 1123,
        "UserQuotaInfos": {
            "FileCountLimit": 10000,
            "UserId": 500,
            "SizeLimit": 1024,
            "QuotaType": "Accounting",
            "FileCountReal": 5100,
            "SizeReal": 800,
            "UserType": "Uid"
        }
    },
    "PageSize": 1,
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "PageNumber": 1
}
```

### 统一命名空间

#### CreateNamespace

**请求参数**

文件存储NAS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNamespa ce | 接口名称。取值：CreateNamespace。 |
| ProtocolType | String | 是 | NFS | 文件传输协议类型。 仅支持NFS文件传输协议。 |
| StorageType | String | 是 | Performance | 存储类型。 取值： Performance：性能型 Capacity：容量型 |
| ZoneId | String | 否 | cn-hangzhou-b | 可用区ID。 可用区是指在同一地域内，电力和网络互相独立的物理区域。 说明同一地域不同可用区之间的文件系统与ECS云服务器互通。 建议文件系统与云服务器 ECS属于同一可用区，避免跨可用区产生的时延。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |
| ClusterId | String | 否 | StandardNasClu ster | 集群ID。 |
| EncryptType | String | 否 | 0 | 命名空间中的文件系统是否加密。 使用KMS服务托管密钥，对文件系统落盘数据进行加密存储。在读写加密数据时， 无需解密。 取值： 0（默认值）：不加密 1：加密 |

文件存储NAS

| Description | String | 否 | balabala | 文件系统描述。 限制： 长度为2~128个英文或中文字符。 必须以大小写字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线 （ ）或者短划线（-）。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | 命名空间ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&ProtocolType=NFS &StorageType=Performance
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
}
```

#### DeleteNamespace

**请求参数**

文件存储NAS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteNamespa ce | 接口名称。取值：DeleteNamespace。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | 命名空间ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
}
```

#### ModifyNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

文件存储NAS

| Action | String | 是 | ModifyNamespa ce | 接口名称。取值：ModifyNamespace。 |
|---|---|---|---|---|
| Description | String | 是 | test | 命名空间描述。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | 命名空间ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
&Description=test &NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
}
```

#### DescribeNamespaces

**请求参数**

文件存储NAS

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeNames paces | 接口名称。取值： DescribeNamespaces。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |
| NasNamespaceI d | String | 否 | 1NS244**** | 命名空间ID。 |
| Description | String | 否 | test | 命名空间描述。 |
| PageSize | Integer | 否 | 10 | 每个分页包含的命名空间个数。 默认值：10。 取值范围：1~100。 |
| PageNumber | Integer | 否 | 1 | 列表的分页页码。 起始值（默认值）：1 |
| StorageType | String | 否 | Performance | 存储类型。 取值： Performance：性能型 Capacity：容量型 |
| OrderByField | String | 否 | CreateTime | 返回结果排序字段。 默认值：CreateTime，按创建时间排序。 |
| SortOrder | String | 否 | ASC | 排序顺序。 取值： ASC（默认值）：升序 DESC：降序 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NasNamespac eCreateLimit | Integer | 2 | 命名空间创建数量限制。 |
| NasNamespac es | Array of NasNamespac e |  | 命名空间信息集合。 |

文件存储NAS

| CreateTime | String | 2022-07- 20T10:08:08Z | 命名空间创建的实践。 执行ISO8601标准表示，返回格式： yyyy- MM-ddTHH:mm:ssZ 。 |  |  |
|---|---|---|---|---|---|
|  |  |  |  | yyyy- |  |
| Description | String | balabala | 文件系统描述。 限制： 长度为2~128个英文或中文字符。 必须以大小写字母或中文开头，不能以 http:// 和 https:// 开头。 可以包含数字、半角冒号（:）、下划线（ ） _ 或者短划线（-）。 |  |  |
| EncryptType | Integer | 1 | 命名空间中的文件系统是否加密。 使用KMS服务托管密钥，对文件系统落盘数据进行加密存储。在读写加密数据时，无需解密。 取值： 0：不加密 1：加密 |  |  |
| FileSystemTyp e | String | standard | 文件系统类型。 默认值：standard，通用型NAS |  |  |
| MountTargets | Array of MountTarget |  | 命名空间文件系统挂载点信息集合。 |  |  |
| AccessGroupN ame | String | classic-test | 权限组名称。 |  |  |
| MountTargetD omain | String | 1ca404a666- w****.cn- hangzhou.nas.aliyu ncs.com | 文件系统挂载点。 |  |  |
| NetworkType | String | Vpc | 网络类型。 包括： Vpc：专有网络 Classic：经典网络 |  |  |
| Status | String | Active | 当前挂载点状态。 包括： Active：可用 Inactive：不可用 Pending：任务排队中 Deleting：删除中 |  |  |

|  | MM-ddTHH:mm:ssZ |
|---|---|

文件存储NAS

| VpcId | String | vpc- 2zesj9afh3y518k9o **** | 专有网络ID。 |
|---|---|---|---|
| VswId | String | vsw- 2zevmwkwyztjuoff g**** | 交换机ID。 |
| NasNamespac eId | String | 1NS244**** | 命名空间ID。 |
| ProtocolType | String | NFS | 文件传输协议类型。 取值： NFS：NFS文件传输协议。 SMB：SMB文件传输协议。 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| Status | String | Normal | 目录的统计状态。 初始化时为Initializing；正常时为Normal。 |
| StorageType | String | Performance | 存储类型。 取值： Performance：性能型 Capacity：容量型 |
| ZoneId | String | cn-hangzhou-b | 可用区ID。 |
| PageNumber | Integer | 1 | 列表的分页页码。 起始值（默认值）：1 |
| PageSize | Integer | 1 | 每个分页包含的命名空间个数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 命名空间总个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeNamespaces
```

`&<`公共请求参数> 正常返回示例文件存储NAS `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <NasNamespaceCreateLimit>2</NasNamespaceCreateLimit> <NasNamespaces>
    <Status>Normal</Status>
    <StorageType>Performance</StorageType>
    <Description>balabala</Description>
    <EncryptType>1</EncryptType>
    <ZoneId>cn-hangzhou-b</ZoneId>
    <NasNamespaceId>1NS244****</NasNamespaceId>
    <ProtocolType>NFS</ProtocolType>
    <FileSystemType>standard</FileSystemType>
    <CreateTime>2022-07-20T10:08:08Z</CreateTime>
    <RegionId>cn-hangzhou</RegionId>
    <MountTargets>
        <Status/>
        <VswId/>
        <VpcId/>
        <MountTargetDomain/>
        <NetworkType/>
        <AccessGroupName/>
    </MountTargets>
</NasNamespaces>
```

`JSON` 格式文件存储NAS

```json
{
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "PageNumber": 1,
    "NasNamespaceCreateLimit": 2,
    "NasNamespaces": {
        "Status": "Normal",
        "StorageType": "Performance",
        "Description": "balabala",
        "EncryptType": 1,
        "ZoneId": "cn-hangzhou-b",
        "NasNamespaceId": "1NS244****",
        "ProtocolType": "NFS",
        "FileSystemType": "standard",
        "CreateTime": "2022-07-20T10:08:08Z",
        "RegionId": "cn-hangzhou",
        "MountTargets": {
            "Status": "",
            "VswId": "",
            "VpcId": "",
            "MountTargetDomain": "",
            "NetworkType": "",
            "AccessGroupName": ""
        }
    }
}
```

#### AddFileSystemToNamespace

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | AddFileSystemT oNamespace | 接口名称。取值： AddFileSystemToNamespace。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| MappedPath | String | 是 | tmp path _ | 映射路径。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 取值： standard（默认值）：通用型NAS |

文件存储NAS

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | 文件系统ID。 |
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddFileSystemToNamespace &FileSystemId=1ca404**** &MappedPath=tmp_path &NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <FileSystemId>1ca404****</FileSystemId>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "FileSystemId": "1ca404****"
}
```

#### RemoveFileSystemFromNamespace

调用RemoveFileSystemFromNamespace删除命名空间中的一个文件系统。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveFileSyst emFromNamesp ace | 接口名称。取值： RemoveFileSystemFromNamespace 。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |

文件存储NAS

| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | 文件系统ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveFileSystemFromNamespace &FileSystemId=1ca404**** &NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <FileSystemId>1ca404****</FileSystemId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "FileSystemId": "1ca404****"
}
```

#### RenameMappedPathInNamespace

调用RenameMappedPathInNamespace修改命名空间中一个文件系统的映射名。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RenameMapped PathInNamespac e | 接口名称。取值： RenameMappedPathInNamespace。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |

文件存储NAS

| MappedPath | String | 是 | tmp path _ | 映射路径。 |
|---|---|---|---|---|
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | 命名空间ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RenameMappedPathInNamespace &FileSystemId=1ca404**** &MappedPath=tmp_path &NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
}
```

#### ListFileSystemsInNamespace

调用ListFileSystemsInNamespace列出命名空间中映射的文件系统。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

文件存储NAS

| Action | String | 是 | ListFileSystemsI nNamespace | 接口名称。取值： ListFileSystemsInNamespace。 |
|---|---|---|---|---|
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |
| NasNamespaceI d | String | 否 | 1NS244**** | 命名空间ID。 |
| Description | String | 否 | test | 命名空间描述。 |
| PageSize | Integer | 否 | 10 | 每页展示的数据条数。 |
| PageNumber | Integer | 否 | 1 | 当前展示的页数。 |
| FileSystemId | String | 否 | 1ca404**** | 文件系统ID。 |
| MappedPath | String | 否 | tmp path _ | 映射路径。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| NSMembers | Array of NSMember |  | 文件系统信息集合。 |
| CreateTime | String | 2022-07- 25T15:43:06CST | 创建时间。 |
| FileSystemId | String | 1ca404**** | 文件系统ID。 |
| FileSystemTyp e | String | standard | 文件系统类型。 standard：通用型NAS。 |
| MappedPath | String | tmp path _ | 映射路径。 |

文件存储NAS

| Status | String | Running | 文件系统状态。包括： Pending：当前文件系统正在处理任务中。 Running：当前文件系统可用，当状态为 Running时才可以进行后续操作（例如：创建挂载点等）。 Stopped：当前文件系统不可用。 Extending：当前文件系统扩容中。 Stopping：当前文件系统停机中。 Deleting：当前文件系统删除中。 |
|---|---|---|---|
| StorageType | String | Performance | 存储类型。 包括： Capacity：容量型 Performance：性能型 |
| PageNumber | Integer | 1 | 当前展示的页数。 |
| PageSize | Integer | 1 | 每页展示的数据条数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 映射的文件系统总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ListFileSystemsInNamespace
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <NSMembers>
    <Status>Running</Status>
    <StorageType>Performance</StorageType>
    <FileSystemType>standard</FileSystemType>
    <CreateTime>2022-07-25T15:43:06CST</CreateTime>
    <FileSystemId>1ca404****</FileSystemId>
    <MappedPath>tmp_path</MappedPath>
</NSMembers>
```

文件存储NAS `JSON` 格式

```json
{
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "PageNumber": 1,
    "NSMembers": {
        "Status": "Running",
        "StorageType": "Performance",
        "FileSystemType": "standard",
        "CreateTime": "2022-07-25T15:43:06CST",
        "FileSystemId": "1ca404****",
        "MappedPath": "tmp_path"
    }
}
```

#### CreateNamespaceMountTarget

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateNamespa ceMountTarget | 接口名称。取值： CreateNamespaceMountTarget。 |
| AccessGroupNa me | String | 是 | classic-test | 权限组名称。 限制： 长度为3~64个字符。 必须以大小写字母开头，可以包含英文字母、数字、下划线（ ）或者短划线 _ （-）。 新创建的权限组名称不能与两个默认的权限组相同。 默认权限组： DEFAULT VPC GROUP NAME（专有网 _ _ _ 络默认权限组）、 DEFAULT CLASSIC GROUP NAME（经 _ _ _ 典网络默认权限组）。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| NetworkType | String | 是 | Vpc | 挂载点网络类型。 取值： Vpc：专有网络 Classic：经典网络 |

文件存储NAS

| FileSystemType | String | 否 | standard | 文件系统类型。 取值： standard：通用型NAS。 |
|---|---|---|---|---|
| VpcId | String | 否 | vpc- 2zesj9afh3y518 k9o**** | 专有网络ID。 当网络类型是专有网络，此字段必填且有意义。 |
| VSwitchId | String | 否 | vsw- 2zevmwkwyztju offg**** | 交换机ID。 当网络类型是专有网络，此字段必填且有意义。 |
| SecurityGroupId | String | 否 | sg- bp1fg655nh68x yz9**** | 安全组ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | 挂载点域名。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateNamespaceMountTarget &AccessGroupName=classic-test &NasNamespaceId=1NS244**** &NetworkType=Vpc
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
```

`JSON` 格式文件存储NAS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
}
```

#### DeleteNamespaceMountTarget

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteNamespa ceMountTarget | 接口名称。取值： DeleteNamespaceMountTarget。 |
| MountTargetDo main | String | 是 | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | 挂载点域名。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | 挂载点域名。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteNamespaceMountTarget &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NS244****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
```

文件存储NAS `JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
}
```

#### ModifyNamespaceMountTarget

调用ModifyNamespaceMountTarget修改命名空间挂载点状态信息。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyNamespa ceMountTarget | 接口名称。取值： ModifyNamespaceMountTarget。 |
| MountTargetDo main | String | 是 | 1ca404****- kvr2.cn- hangzhou.nas.al iyuncs.com | 文件系统命名空间挂载点域名。 |
| NasNamespaceI d | String | 是 | 1NSc24**** | 命名空间ID。 |
| AccessGroupNa me | String | 否 | DEFAULT VPC G _ _ ROUP NAME _ | 权限组名称。 限制： 长度为3~64个字符。 必须以大小写字母开头，可以包含英文字母、数字、下划线（ ）或者短划线 _ （-）。 新创建的权限组名称不能与两个默认的权限组相同。 默认权限组： DEFAULT VPC GROUP NAME（专有网 _ _ _ 络默认权限组）、 DEFAULT CLASSIC GROUP NAME（经 _ _ _ 典网络默认权限组）。 |
| Status | String | 否 | Active | 挂载点状态。 取值： Active：可用 Inactive：不可用 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

文件存储NAS

| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyNamespaceMountTarget &MountTargetDomain=1ca404****-kvr2.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NSc24****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8"
}
```

#### DescribeNamespaceMountTargets

调用DescribeNamespaceMountTargets接口查询命名空间挂载点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| NasName spaceId | Strin g | Query | 是 | ns1ca404**** | 命名空间ID。 |
| MountTar getDomai n | Strin g | Query | 否 | ns-1NS724****-0****.cn- wulan-en****- d01.nas.inter.en****.sh* ***ng.com | 挂载点域名。 |
| PageSize | Integ er | Query | 否 | 1 | 每个分页包含的挂载点个数。 取值范围：1~100。 默认值：10。 |
| PageNum ber | Integ er | Query | 否 | 1 | 列表的分页页码。起始值 （默认值）：1。 |

文件存储NAS

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| MountTargets | Array | - | 挂载点信息。 |
| - MountTargetD omain | String | ns-1NS724****- 0****.cn-wulan- en****- d01.nas.inter.en*** *.sh****ng.com | 挂载点域名。 |
| -NetworkType | String | Classic | 挂载点网络类型。 包括： Classic：经典网络。 Vpc：专有网络。 |
| -VpcId | String | vpc- gxxxxxlzw21fj9k | 专有网络 ID。 |
| -VswId | String | vsw- g4xxxxxxpf4mb6o m6j | 交换机ID。 |
| -AccessGroup | String | pri | 挂载点所应用的权限组名称。 |
| -Status | String | Active | 当前挂载点状态。 包括： Active：可用 Inactive：不可用当状态为Active时才可以挂载文件系统。 |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | 请求ID。 |
| TotalCount | Integer | 3 | 挂载点总数。 |
| PageSize | Integer | 1 | 每个分页包含的挂载点个数。 取值范围：1~100。默认值：10。 |
| PageNumber | Integer | 1 | 列表的分页页码。起始值（默认值）：1。 |

**示例**

请求示例文件存储NAS

```
http(s)://[Endpoint]/?Action=DescribeNamespaceMountTargets &NasNamespaceId=ns1ca404****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":3,
 "RequestId":"3BAB90FD-B4A0-48DA-9F09-2B963510A0EF",
 "PageSize":1,
 "PageNumber":1,
 "MountTargets":[
  {
   "Status":"Active",
   "VpcId":"vpc-gxxxxxlzw21fj9k",
   "VswId":"vsw-g4xxxxxxpf4mb6om6j",
   "MountTargetDomain":"ns-1NS724****-0****.cn-wulan-en****-
d01.nas.inter.en****.sh****ng.com",
   "NetworkType":"Classic",
   "AccessGroup":"pri"
  }
```

]

```
}
```

`XML` 格式

```xml
<TotalCount>3</TotalCount> <RequestId>3BAB90FD-B4A0-48DA-9F09-2B963510A0EF</RequestId> <PageSize>1</PageSize> <PageNumber>1</PageNumber> <MountTargets>
 <Status>Active</Status>
 <VpcId>vpc-gxxxxxlzw21fj9k</VpcId>
 <VswId>vsw-g4xxxxxxpf4mb6om6j</VswId>
 <MountTargetDomain>ns-1NS724****-0****.cn-wulan-en****-
d01.nas.inter.en****.sh****ng.com</MountTargetDomain>
 <NetworkType>Classic</NetworkType>
 <AccessGroup>pri</AccessGroup>
</MountTargets>
```

#### AddNamespaceToGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

文件存储NAS

| Action | String | 是 | AddNamespaceT oGroup | 接口名称。取值： AddNamespaceToGroup。 |
|---|---|---|---|---|
| MappedPath | String | 是 | data | 跨域挂载编排映射路径。 |
| MountTargetDo main | String | 是 | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | 命名空间挂载点。 |
| NasNamespaceI d | String | 是 | 1NS244**** | 命名空间ID。 |
| NasNamespaceR egion | String | 是 | cn-hangzhou | 命名空间所在地域。 |
| NetworkType | String | 是 | Vpc | 网络类型。 取值： Vpc：专有网络 Classic：经典网络 |
| FileSystemType | String | 否 | standard | 文件系统类型。 默认值：standard，通用型NAS |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E |  |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AddNamespaceToGroup &MappedPath=data &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NS244**** &NasNamespaceRegion=cn-hangzhou &NetworkType=Vpc
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式文件存储NAS

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

#### RemoveNamespaceFromGroup

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RemoveNamesp aceFromGroup | 接口名称。取值： RemoveNamespaceFromGroup |
| MemberId | String | 是 | 1 | 跨域挂载编排ID。 |
| FileSystemType | String | 否 | 1ca404**** | 文件系统ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| MemberId | String | 1 | 跨域挂载编排ID。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveNamespaceFromGroup &MemberId=1
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<MemberId>1</MemberId> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
```

`JSON` 格式文件存储NAS

```json
{
    "MemberId": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
}
```

#### DescribeNamespaceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSyste mType | Strin g | Query | 否 | standard | 文件系统类型。 默认值：standard，通用型 NAS |
| PageSize | Integ er | Query | 否 | 1 | 每个分页包含的挂载点个数。 取值范围：1~100。默认值：10。 |
| PageNum ber | Integ er | Query | 否 | 1 | 列表的分页页码。起始值 （默认值）：1。 |
| MountTar getDomai n | Strin g | Query | 否 | ns-1Nxxxx-9cb81.cn- wulan-envxx- d01.nas.intra.envxx.shxx xang.com. | 命名空间挂载点。 |
| NasName spaceRegi on | Strin g | Query | 否 | cn-xxxn-envxxx-d01 | 命名空间所在地域。 |
| Status | Strin g | Query | 否 | Enabled | 命名空间状态。 包括： All：全部 Enabled：启用 Disable：未启用 |
| MappedPa th | Strin g | Query | 否 | nas | 跨域挂载编排映射路径。 |

**返回数据**

文件存储NAS

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| NasNamespac es | Array | - | 命名空间信息集合。 |
| - ResourceOwne rId | String | 12xxxxx8974995 | 用户组织uid。 |
| -MemberId | String | 6 | 序列id。 |
| -NetworkType | String | Vpc | 网络类型。 包括： Vpc：专有网络 Classic：经典网络 |
| - NasNamespac eRegion | String | cn-xxxn-envxxx- d01 | 域名。 |
| - NasNamespac eId | String | 1NSxxx26 | 命名空间ID。 |
| - MountTargetD omain | String | ns-1Nxxxx- 9cb81.cn-wulan- envxx- d01.nas.intra.envx x.shxxxang.com. | 命名空间挂载点。 |
| -MappedPath | String | nas | 跨域挂载编排映射路径。 |
| -CreateTime | String | 2023-12- 29T09:18:10Z | 创建时间。 |
| -Status | String | Enabled | 命名空间状态。 包括： All：全部 Enabled：启用 Disable：未启用 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 1 | 总计条数。 |
| PageSize | Integer | 1 | 每个分页包含的挂载点个数。 取值范围：1~100。默认值：10。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNumber | Integer | 1 | 列表的分页页码。起始值（默认值）：1。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeNamespaceGroup
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "TotalCount":1,
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
 "PageSize":1,
 "PageNumber":1,
 "NasNamespaces":[
  {
   "Status":"Enabled",
   "MemberId":"6",
   "NasNamespaceRegion":"cn-xxxn-envxxx-d01",
   "NasNamespaceId":"1NSxxx26",
   "MountTargetDomain":"ns-1Nxxxx-9cb81.cn-wulan-envxx-
d01.nas.intra.envxx.shxxxang.com.",
   "NetworkType":"Vpc",
   "CreateTime":"2023-12-29T09:18:10Z",
   "MappedPath":"nas",
   "ResourceOwnerId":"12xxxxx8974995"
  }
```

]

```
}
```

`XML` 格式文件存储NAS

```xml
<TotalCount>1</TotalCount> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageSize>1</PageSize> <PageNumber>1</PageNumber> <NasNamespaces>
 <Status>Enabled</Status>
 <MemberId>6</MemberId>
 <NasNamespaceRegion>cn-xxxn-envxxx-d01</NasNamespaceRegion>
 <NasNamespaceId>1NSxxx26</NasNamespaceId>
 <MountTargetDomain>ns-1Nxxxx-9cb81.cn-wulan-envxx-d01.nas.intra.envxx.shxxxang.com.</M
ountTargetDomain>
 <NetworkType>Vpc</NetworkType>
 <CreateTime>2023-12-29T09:18:10Z</CreateTime>
 <MappedPath>nas</MappedPath>
 <ResourceOwnerId>12xxxxx8974995</ResourceOwnerId>
</NasNamespaces>
```

### 生命周期管理

#### CreateLifecyclePolicy

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateLifecycleP olicy | 系统规定参数。取值： CreateLifecyclePolicy。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| LifecyclePolicyN ame | String | 是 | lifecyclepolicy 0 _ 1 | 生命周期管理策略名称。 长度为3~64个字符，必须以大写字母或小写字母开头，可以包含英文字母、数字、 下划线（ ）或者短划线（-）。 _ |
| LifecycleRuleNa me | String | 是 | DEFAULT ATIME _ 14 _ | 生命周期管理策略关联的管理规则。 取值： DEFAULT ATIME 14：距今14天未访 _ _ 问的文件 DEFAULT ATIME 30：距今30天未访 _ _ 问的文件 DEFAULT ATIME 60：距今60天未访 _ _ 问的文件 DEFAULT ATIME 90：距今90天未访 _ _ 问的文件 |

文件存储NAS

| OssBucket | String | 是 | rick-test-005 | 冷数据转储的OSS Bucket。 |
|---|---|---|---|---|
| Path | String | 是 | /pathway/to/fold er | 生命周期管理策略关联目录的绝对路径。 仅支持关联单个目录。必须以正斜线（/） 开头，并且是挂载点中真实存在的路径。 |
| StorageType | String | 是 | InfrequentAcces s | 数据转储后的存储类型。 默认值：InfrequentAccess（低频型） |
| Recursive | Boolean | 否 | true | 是否对目录进行递归。 当值为true时，会递归该路径下的所有子目录。 取值： true：是 false（默认值）：否 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | 请求ID。 |
| Success | Boolean | true | 请求状态。 取值： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateLifecyclePolicy &FileSystemId=1ca404**** &LifecyclePolicyName=lifecyclepolicy_01 &LifecycleRuleName=DEFAULT_ATIME_14 &OssBucket=rick-test-005 &Path=/pathway/to/folder &StorageType=InfrequentAccess
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
```

文件存储NAS `JSON` 格式

```json
{
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
}
```

#### DeleteLifecyclePolicy

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteLifecycleP olicy | 接口名称。取值： DeleteLifecyclePolicy。 |
| FileSystemId | String | 是 | 106174**** | 文件系统ID。 |
| LifecyclePolicyN ame | String | 是 | lifecycle | 生命周期管理策略名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| Success | Boolean | true | 请求状态。包括： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteLifecyclePolicy &FileSystemId=106174**** &LifecyclePolicyName=lifecycle
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <Success>true</Success>
```

文件存储NAS `JSON` 格式

```json
{"RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E","Success":"true"}
```

#### ModifyLifecyclePolicy

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ModifyLifecycleP olicy | 接口名称。取值： ModifyLifecyclePolicy。 |
| FileSystemId | String | 是 | 1ca404**** | 文件系统ID。 |
| LifecyclePolicyN ame | String | 是 | ifecyclepolicy 0 _ 1 | 生命周期管理策略名称。 |
| LifecycleRuleNa me | String | 是 | DEFAULT ATIME _ 14 _ | 生命周期管理策略关联的管理规则。 包括： DEFAULT ATIME 14：距今14天未访 _ _ 问的文件 DEFAULT ATIME 30：距今30天未访 _ _ 问的文件 DEFAULT ATIME 60：距今60天未访 _ _ 问的文件 DEFAULT ATIME 90：距今90天未访 _ _ 问的文件 |
| Path | String | 是 | /pathway/to/fold er | 生命周期管理策略配置的单个目录的绝对路径。 |
| Recursive | Boolean | 是 | true | 是否对目录进行递归。 当值为true时，会递归该路径下的所有子目录。 取值： true：是 false（默认值）：否 |
| StorageType | String | 否 | InfrequentAcces s | 数据转储后的存储类型。 默认值：InfrequentAccess（低频型） |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

文件存储NAS

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
|---|---|---|---|
| Success | Boolean | true | 请求状态。 取值： true：请求成功 false：请求失败 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifyLifecyclePolicy &FileSystemId=1ca404**** &LifecyclePolicyName=ifecyclepolicy_01 &LifecycleRuleName=DEFAULT_ATIME_14 &Path=/pathway/to/folder &Recursive=true
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <Success>true</Success>
```

`JSON` 格式

```json
{
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "Success": true
}
```

#### DescribeLifecyclePolicies

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeLifecycl ePolicies | 系统规定参数。取值： DescribeLifecyclePolicies。 |
| FileSystemId | String | 否 | 1ca404**** | 文件系统ID。 |

文件存储NAS

| PageSize | Integer | 否 | 10 | 每个分页包含的生命周期管理策略个数。 取值范围：1~100 默认值：10 |
|---|---|---|---|---|
| PageNumber | Integer | 否 | 1 | 列表的分页页码。 起始值（默认值）：1 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |  |  |
|---|---|---|---|---|---|
| LifecyclePolici es | Array of LifecyclePolicy |  | 生命周期管理策略信息集合。 |  |  |
| CreateTime | String | 2019-10- 30T10:08:08Z | 生命周期管理策略创建的时间。 执行ISO8601标准表示，返回格式： yyyy- MM-ddTHH:mm:ssZ 。 |  |  |
|  |  |  |  | yyyy- |  |
| FileSystemId | String | 1ca404**** | 文件系统ID。 |  |  |
| LifecyclePolicy Name | String | lifecyclepolicy 01 _ | 生命周期管理策略名称。 |  |  |
| LifecycleRuleN ame | String | DEFAULT ATIME 1 _ _ 4 | 生命周期管理策略关联的管理规则。 包括： DEFAULT ATIME 14：距今14天未访问的文 _ _ 件 DEFAULT ATIME 30：距今30天未访问的文 _ _ 件 DEFAULT ATIME 60：距今60天未访问的文 _ _ 件 DEFAULT ATIME 90：距今90天未访问的文 _ _ 件 |  |  |
| OssBucket | String | rick-test-005 | 需要归档到的OSS Bucket。 |  |  |
| Path | String | /pathway/to/folder | 生命周期管理策略配置的单个目录的绝对路径。 |  |  |
| Recursive | Boolean | true | 是否对目录进行递归。 当值为true时，会递归该路径下的所有子目录。 取值： true：是 false（默认值）：否 |  |  |

|  | MM-ddTHH:mm:ssZ |
|---|---|

文件存储NAS

| StorageType | String | InfrequentAccess | 数据转储后的存储类型。 默认值：InfrequentAccess（低频型） |
|---|---|---|---|
| PageNumber | Integer | 1 | 列表的分页页码。 |
| PageSize | Integer | 10 | 每个分页包含的生命周期管理策略个数。 |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | 请求ID。 |
| TotalCount | Integer | 10 | 生命周期管理策略总数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeLifecyclePolicies
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<TotalCount>10</TotalCount> <PageSize>10</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <LifecyclePolicies>
    <Path>/pathway/to/folder</Path>
    <LifecyclePolicyName>lifecyclepolicy_01</LifecyclePolicyName>
    <StorageType>InfrequentAccess</StorageType>
    <LifecycleRuleName>DEFAULT_ATIME_14</LifecycleRuleName>
    <CreateTime>2019-10-30T10:08:08Z</CreateTime>
    <OssBucket>rick-test-005</OssBucket>
    <FileSystemId>1ca404****</FileSystemId>
    <Recursive>true</Recursive>
</LifecyclePolicies>
```

`JSON` 格式文件存储NAS

```json
{
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "PageNumber": 1,
    "LifecyclePolicies": {
        "Path": "/pathway/to/folder",
        "LifecyclePolicyName": "lifecyclepolicy_01",
        "StorageType": "InfrequentAccess",
        "LifecycleRuleName": "DEFAULT_ATIME_14",
        "CreateTime": "2019-10-30T10:08:08Z",
        "OssBucket": "rick-test-005",
        "FileSystemId": "1ca404****",
        "Recursive": true
    }
}
```

### NFS NAS ACL

#### EnableNfsAcl

开启NFS ACL功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | 是 | 43f264xxxx | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 29F4F360-A6A8- 561A-A45B- A0F6882969BA | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=43f264xxxx
```

&公共请求参数正常返回示例 `JSON` 格式文件存储NAS

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"29F4F360-A6A8-561A-A45B-A0F6882969BA"
}
```

`XML` 格式

```xml
<RequestId>29F4F360-A6A8-561A-A45B-A0F6882969BA</RequestId>
```

#### DisableNfsAcl

关闭NFS ACL功能。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | 是 | 91fcdxxxx | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 24487C24-AE54- 57EC-B4E4- 4EDEEEB83B01 | 请求ID。 |

**示例**

请求示例

```
&FileSystemId=91fcdxxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"24487C24-AE54-57EC-B4E4-4EDEEEB83B01"
}
```

`XML` 格式文件存储NAS

```xml
<RequestId>24487C24-AE54-57EC-B4E4-4EDEEEB83B01</RequestId>
```

#### DescribeNfsAcl

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | 是 | 206614xxxx | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | A1098673-1746- 505E-A5F1- 08527B7EDBDF | 请求ID。 |
| Acl | Struct | - | ACL信息。 |
| -Enabled | Boolean | True | 是否启用了 NFS ACL 功能。 true：启用了 NFS ACL 功能。 false：未启用 NFS ACL 功能。 |

**示例**

请求示例

```
&FileSystemId=206614xxxx
```

&公共请求参数正常返回示例 `JSON` 格式

```json
HTTP/1.1 200 OK Content-Type:application/json {
 "RequestId":"A1098673-1746-505E-A5F1-08527B7EDBDF",
 "Acl":{
  "Enabled":true
 }
}
```

文件存储NAS `XML` 格式

```xml
<RequestId>A1098673-1746-505E-A5F1-08527B7EDBDF</RequestId> <Acl>
 <Enabled>true</Enabled>
</Acl>
```

### 附录：错误代码表

错误码由 4 部分组成，如错误码所示。 表 1. 错误码

| 组成部分 | 描述 |
|---|---|
| HttpCode | HTTP 响应码，符合 HTTP 协议语义 |
| Code | 错误标识 |
| Message | 错误消息 |
| Advice | 建议处理方式 |

**错误码列表**

| HttpCode | Code | Message | Advice |
|---|---|---|---|
| 500 | InternalError | 系统内部错误 | 给您带来的不便，深感抱歉，请稍后再试。 |
| 503 | ServiceUnavailable | 服务暂不可用 | 给您带来的不便，深感抱歉，请稍后再试。 |
| 504 | ServiceTimeout | 服务请求超时 | 请稍后再试。 |
| 503 | SubRam.CheckFailed | The sub user ram check has failed due to some internal error. | 主子账号权限检查过程中，由于内部调用失败导致检查失败，请稍后再试。 |
| 503 | VpcRam.CheckFailed | The Vpc ram check has failed due to some internal error. | Vpc 权限检查过程中，由于内部调用失败导致检查失败，请稍后再试。 |
| 503 | VpcSubRam.CheckFail ed | The Vpc sub user ram check has failed due to some internal error. | Vpc 主子账号检查过程中，由于内部调用失败导致检查失败，请稍后再试。 |
| 400 | MissingParameter.call erUid | 请求参数缺失：callerUid未指定 | 请加入 callerUid 请求参数。 |
| 400 | MissingParameter.Regi onId | 请求参数缺失：域名中RegionId未指定 | 请在域名中加入 RegionId 字段信息。 |
| 400 | MissingParameter.VSw itchId | 请求参数缺失：VSwitchId未指定 | 请加入 VSwitchId 请求参数。 |

文件存储NAS

| 400 | MissingParameter.VpcI d | 请求参数缺失：VpcId未指定 | 请加入 VpcId 请求参数。 |
|---|---|---|---|
| 400 | InvalidParameter.Stora geType | 请求参数非法：StorageType不合法 | 合法的 StorageType 请求参数有 Performance 和 Capacity。 |
| 400 | InvalidParameter.Proto calType | 请求参数非法：ProtocalType不合法 | 合法的 ProtocalType 请求参数为 NFS。 |
| 400 | InvalidParameter.Desc ription | 请求参数非法：Description包含非法字符 | Description 的合法字符包括中英文和 @#$ +-。 _ |
| 404 | InvalidFileSystem.NotF ound | 指定文件系统不存在 | 您指定的文件系统不存在或已删除。 |
| 403 | InvalidFileSystem.Alre adyExisted | 指定文件系统已存在 | 您指定的文件系统已存在，您可以通过调用 DescribeFileSystem s 并指定该文件系统id查看相关信息。 |
| 404 | InvalidMountTarget.No tFound | 指定挂载点不存在 | 您指定的挂载点不存在或已删除。 |
| 404 | InvalidAccessGroup.No tFound | 指定权限组不存在 | 您指定的权限组不存在或已删除。 |
| 403 | InvalidAccessGroup.Alr eadyExisted | 指定权限组已存在 | 您指定的权限组已存在， 您可以通过调用 DescribeMountTarg ets 并指定该权限组查看相关信息。 |
| 403 | InvalidAccessGroup.Alr eadyAttached | 指定权限组已经绑定指定挂载点 | 指定权限组还绑有相关挂载点，请先解绑相关挂载点再删除该权限组。 |
| 404 | InvalidAccessRule.Not Found | 指定权限规则不存在 | 您指定的权限规则不存在或已删除。 |
| 404 | InvalidLocatin.NotFoun d | 指定Location不存在 | 请求的 Location 不存在或暂未提供服务。 |
| 404 | InvalidRegionId.NotFou nd | 指定Region不存在 | 请求的 Region 不存在或暂未提供服务。 |
| 404 | InvalidAZone.NotFoun d | 指定Azone不存在 | 请求的 Zone 不存在或暂未提供服务。 |
| 404 | InvalidVpc.NotFound | 指定Vpc不存在 | 您指定的 Vpc 不存在，请先创建专有网络 VPC。 |
| 404 | InvalidVip.NotFound | 指定Vip不存在 | 您指定的Vpc创建Vip失败，请检查你Vpc网络中有可用ip可供创建 |

文件存储NAS

| 404 | InvalidLBid.NotFound | 指定LBid不存在 | 系统创建 LBid 失败，请稍后重试。 |
|---|---|---|---|
| 404 | InvalidVpcTunnelId.Not Found | The specified vpc tunnelId is not found. | 指定的 Vpc tunnelId 不存在，请先检查 Vpc 信息。 |
| 404 | InvalidVpc.CreationFail ed | The specified vpc instance creation failed. | 指定的 Vpc 实例创建失败，请检查您的 Vpc 信息正确有效且有可用 IP 空间可供创建，并再次重试。 |
| 403 | OperationDenied.Defa ultAccessGroupCannot Delete | 操作不被允许：默认权限组不允许删除 | 您可以编辑操作自定义的权限组。 |
| 403 | OperationDenied.Defa ultAccessGroupCannot Modify | 操作不被允许：默认权限组不允许修改 | 您可以编辑操作自定义的权限组。 |
| 403 | OperationDenied.Netw orkTypeNotMatched | 操作不被允许：挂载点网络类型与AccessGroup不匹配 | 请确保挂载点的 NetworkType 与权限组的 AccessGroupType 保持一致。 |
| 403 | OperationDenied.Moun tTargetNotEmpty | 操作不被允许：指定文件系统仍存在挂载点，请先删除挂载点 | 指定文件系统仍存在挂载点，请先删除挂载点。 |
| 403 | OperationDenied.FileS ystemCountsExceeded | 文件系统数目已达上限 （一个用户最多创建10个文件系统） | 如需提高上限，请联系技术支持。 |
| 403 | OperationDenied.Moun tTargetCountsExceede d | 挂载点数目已达上限（一个文件系统最多创建2个挂载点） | 如需提高上限，请联系技术支持。 |
| 403 | OperationDenied.Acce ssGroupCountsExceed ed | 权限组数目已达上限 | 如需提高上限，请联系技术支持。 |
| 403 | OperationDenied.Acce ssRuleCountsExceede d | 权限规则数目已达上限 | 如需提高上限，请联系技术支持。 |
| 403 | Forbidden.InvalidUserT ype | 没有权限：用户类型不合法 | NAS API 暂不支持您的账户类型，请见谅。 |
| 403 | Forbbiden.Ram | User not authorized to operate on the specified resource, or this API doesn’t support RAM. | 您的账户 RAM 权限校验失败，请前往 RAM 确保授权 NAS 相关权限。 |
| 403 | NotQualified | 未获得公测资格 | 请您先发起相关新特性的试用申请，若长时间未审批通过，请联系技术支持。 |

**错误码返回示例**

文件存储NAS XML格式

```xml
<?xml version="1.0" encoding="UTF-8"?> <Error>
  <RequestId>B71B4C68-6C6B-4D4B-AD70-8951BD7D188E</RequestId>
  <HostId>nas.regionid.example.com</HostId>
  <Code>InvalidFileSystem.NotFound</Code>
```

`<Message>`指定文件系统不存在`</Message>`

```
</Error>
```

JSON格式

```json
{
  "RequestId": "B71B4C68-6C6B-4D4B-AD70-8951BD7D188E",
  "HostId": " nas.regionid.example.com ",
  "Code": "InvalidFileSystem.NotFound",
```

`"Message": "`指定文件系统不存在"

```
}
```
