---
title: "资源编排 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 151
source_pdf: "06_开发指南_enterprise-ascm-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/ros/zh/enterprise-ascm-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 资源编排 开发指南

资源编排

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
资源编排
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公共云一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 获取AccessKey。
获取调用时所需要的AccessKey参数，请参见获取AccessKey或获取STS AccessKey。 资源编排

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
2. 获取地域ID。
3. 获取组织ID与资源集ID。
组织ID需要通过API获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganiza tionList章节。 资源集ID需要通过API获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResour ceGroup章节。

**说明**

| <x-acs- |  |
|---|---|

`resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空。如果指定资源集，需要同时指定组织ID。
4. 获取对应的API参考文档。
您需要查看目标云产品的开发指南，了解API的功能与使用方式，开发指南的使用流程及获取方法请参
5. 获取云产品Endpoint。
6. 获取云产品SDK并调用云产品API。
资源编排

## 准备工作

### 登录开发者门户

**前提条件**

登录Apsara Uni-manager运营控制台前，确认您已从部署人员处获取Apsara Uni-manager运营控制台的服务域名地址。 推荐使用Chrome浏览器

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
5. 在页面顶部的菜单栏中，选择**产品** > **应用服务** > **开发者服务**。

### 获取API信息及其EndPoint

首先，您需要了解产品开放API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

资源编排 Apsara Uni-manager运营控制台API目录中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **应用服务** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey

AccessKey支持RAM和STS两种授权模式，调用时选择其中一种授权模式即可。本文将为您描述如何获取通过RAM授权的AccessKey。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，验证某个请求发送者的身份。其中 AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。获取方式请参资源编排 Apsara Uni-manager运营控制台提供了个人账号AccessKey和组织AccessKey（只有运营管理员和一级组织管理员可以获取组织AccessKey），推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。如果使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足。 个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限

**警告**

AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 环境地域ID。例如：cn-hangzhou-*。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台中对应的组织ID。获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《GetOrganizationList》文档。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台中对应的资源集ID。 获取方法可参见《Apsara Uni-manager运营控制台开发指南》中的《ListResourceGroup》文档。 |

**获取个人账号AccessKey**

获取个人账号AccessKey的方法如下：
1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，然后单击**个人信息**。
3. 在**AccessKey**区域，查看个人账号的AccessKey信息。
Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权

**说明**

限，请您妥善保管。

**获取组织AccessKey**

获取组织AccessKey的方法如下：
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****AccessKey**。
6. 在**管理****AccessKey**对话框，查看组织AccessKey信息。

### 获取STS AccessKey

本文为您介绍如何通过STS方式调用专有云的产品API。

**背景信息**

资源编排阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。您可以通过STS方式调用专有云的产品API。 STS AccessKey由AccessKey ID、AccessKey Secret及Security Token组成。通过STS方式调用专有

**操作步骤**

1. 获取用户角色的**RAM Role**。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，然后单击**个人信息**。 iii. 单击**查看当前角色策略**。 iv. 在**当前选择角色策略**对话框，选择组织，然后查看**RAM Role**。
2. 获取STS AccessKey参数。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <yourRoleSessionName>：请替换为您实际的会话名称。 <yourRoleArn>：请替换为您实际的RAM Role。 <sts.aliyuncs.com> ：请替换为您实际的STS Endpoint。 资源编排

```
public static void main(String[] args) {
```

`//`创建`DefaultAcsClient`实例并初始化。 `//`请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`。

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

`//STS AccessKey`参数。

```java
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
} private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
```

`//<sts.aliyuncs.com>`请替换为您实际的`STS Endpoint`，一般格式为`sts-`

```
vpc.${global:region}.${global:internet-domain}。
    request.setSysDomain("<sts.aliyuncs.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//`业务参数，用于设置本次调用会话的别名，`"<yourRoleSessionName>"`请您替换为实际值。

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//`扮演的角色`ARN`，`"<yourRoleArn>"`请替换为上一步获取到的实际`RAM`角色`ARN`。

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

3. 通过STS AccessKey调用云产品的接口，下列代码以ROS的DescribeRegions接口为例。
资源编排

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourStsAccesskeyID>：请替换为您实际的STS AccessKey ID。 <yourStsAccessKeySecret>：请替换为您实际的STS AccessKey Secret。 <yourStsToken>：请替换为您实际STS三元组中的Security Token。 <yourResourceGroupID>：请替换为您实际的资源集ID。 <yourOrganizationID>：请替换为您实际的组织ID。

```
public static void main(String[] args) {
```

`//"<yourRegionID>"`请替换为您实际的地域`ID`。

```xml
    //"<yourStsAccessKeyID>","<yourStsAccessKeySecret>"请替换为上一步获取到的STS AccessKe
y ID和AccessKey Secret。
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("ros.aliyuncs.com");
    request.setSysProduct("ROS");
    request.setSysAction("DescribeRegions");
    request.setSysVersion("2019-09-10");
    request.setSysMethod(MethodType.GET);
    request.setHttpContentType(FormatType.FORM);
```

`//"<yourRegionID>"` 请替换为您实际的地域`ID`。

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`//"<yourStsToken>"` 请替换为您上一步获取到的`STS Security Token`。

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//`非必填，请替换为您实际的资源集`ID`。

```
    //request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//`必填，请替换为您实际的组织`ID`。

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

资源编排

### 获取公共Header参数

调用专有云API时需要提供多个Header参数。本文为您介绍这些参数的含义及其获取方式，并解释调用后的返回值。

**Header参数描述**

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 环境地域ID，获取方式请参见获取地域ID。 |
| x-acs-organizationid | Apsara Uni-manager运营控制台上的组织ID，获取方式请参见获取组织ID。 |
| x-acs-resourcegroupid | Apsara Uni-manager运营控制台上的资源集ID，获取方式请参见获取资源集ID。 |

**获取地域ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏，选择**资源管理** > **地域管理**。
4. 单击目标组织名称。
5. 在**Region****列表**区域，查看地域ID。

**获取组织ID**

组织ID需要通过API获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。

**获取资源集ID**

资源集ID需要通过API获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**返回参数**

对于列表类的云产品资源实例接口，调用后会默认增加如下返回值。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |

| 名称 | 描述 |
|---|---|
| Department | 组织ID。 |

### 获取ROS的SDK

通过POP网关调用专有云API时，需使用ROS的阿里云开发工具包（SDK）。本文为您介绍如何获取ROS的 SDK。

| Alibaba Cloud SDK | ROS SDK |
|---|---|
| Alibaba Cloud SDK for Java | ROS SDK for Java |
| Alibaba Cloud SDK for Python | ROS SDK for Python |
| Alibaba Cloud SDK for Go | ROS SDK for Go |

资源编排例

## ROS SDK for Java调用示例

### 快速开始

**环境准备**

使用ROS SDK for Java前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操阿里云专有云Java SDK仅支持1.8及以上的JDK版本。

**安装阿里云专有云Java SDK**

如果您使用Apache Maven来管理Java项目，只需在项目的pom.xml中导入JAR文件。 如果您需要使用ROS SDK for Java，必须安装阿里云Java SDK核心库以及ROS SDK for Java。其中，阿里云Java SDK核心库推荐使用4.5.17及以上版本，ROS SDK for Java推荐使用1.0.1及以上版本。

**使用ROS SDK for Java**

1. 创建并初始化com.aliyun.ros20190910.Client实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。

**说明**

以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <yourRegionId>：请替换为您实际的地域ID。 <yourAccessKeyId>：请替换为您实际的AccessKey ID。 <yourAccessKeySecrect>：请替换为您实际的AccessKey Secret。 <Endpoint>：请替换为ROS Endpoint。

```java
package com.aliyun.sample; import com.aliyun.ros20190910.Client; import com.aliyun.tea.*; import com.aliyun.ros20190910.*; import com.aliyun.ros20190910.models.*; import com.aliyun.teaopenapi.*; import com.aliyun.teaopenapi.models.*; public class Sample {
    /**
```

* 使用`AK`和`SK`初始化账号`Client`。
*

```
     * @param accessKeyId
     * @param accessKeySecret
*@returnClient
```

资源编排例

```
      @return Client
     * @throws Exception
```

`*/`

```java
    private static String ACCESSKEYID = "<yourAccessKeyId>";
    private static String SECRET = "<yourAccessKeySecrect>";
    private static String REGIONID = "<yourRegionId>";
    public static com.aliyun.ros20190910.Client createClient() throws Exception {
        Config config = new Config()
```

`//`您的`AccessKey ID`。

```
                .setAccessKeyId(ACCESSKEYID)
                //您的AccessKey Secret。
                .setAccessKeySecret(SECRET);
```

`//`访问的域名。

```
        config.endpoint = "<Endpoint>";
        return new com.aliyun.ros20190910.Client(config);
    }
    public static void describeRegions(Client client) throws Exception {
        DescribeRegionsRequest describeRegionsRequest = new DescribeRegionsRequest();
```

`//`复制代码运行后，请自行打印`API`的返回值。

```
client.describeRegions(describeRegionsRequest);
    }
    public static void getStack(Client client, String stackId, String regionId) throw
s Exception {
        GetStackRequest getStackRequest = new GetStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
```

`//`复制代码运行后，请自行打印`API`的返回值。

```
        GetStackResponse resp = client.getStack(getStackRequest);
com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
    }
    public static void deleteStack(Client client, String stackId, String regionId) th
rows Exception {
        DeleteStackRequest deleteStackRequest = new DeleteStackRequest()
                .setStackId(stackId)
                .setRegionId(regionId);
```

`//`复制代码运行后，请自行打印`API`的返回值。

```
        DeleteStackResponse resp = client.deleteStack(deleteStackRequest);
com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
    }
    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.ros20190910.Client client = Sample.createClient();
        CreateStackRequest.CreateStackRequestParameters parameters0 = new
CreateStackRequest.CreateStackRequestParameters()
                .setParameterKey("VpcName")
```

资源编排例

```
                .setParameterValue("TestVpc");
        CreateStackRequest.CreateStackRequestParameters parameters1 = new
CreateStackRequest.CreateStackRequestParameters()
                .setParameterKey("CidrBlock")
                .setParameterValue("192.168.0.0/16");
        CreateStackRequest createStackRequest = new CreateStackRequest()
                .setTemplateBody("{\n" +
                        "  \"ROSTemplateFormatVersion\": \"2015-09-01\",\n" +
                        "  \"Parameters\": {\n" +
                        "    \"VpcName\": {\n" +
                        "      \"Type\": \"String\",\n" +
                        "      \"Description\": \"Vpc Name\",\n" +
                        "      \"Label\": \"Vpc Name\"\n" +
                        "    },\n" +
                        "    \"CidrBlock\": {\n" +
                        "      \"Type\": \"String\",\n" +
                        "      \"Description\": \"Vpc CidrBlock\",\n" +
                        "      \"Label\": \"Vpc CidrBlock\"\n" +
                        "    }\n" +
                        "  },\n" +
                        "  \"Resources\": {\n" +
                        "    \"Vpc\": {\n" +
                        "      \"Type\": \"ALIYUN::ECS::VPC\",\n" +
                        "      \"Properties\": {\n" +
                        "        \"CidrBlock\": {\n" +
                        "          \"Ref\": \"CidrBlock\"\n" +
                        "        },\n" +
                        "        \"VpcName\": {\n" +
                        "          \"Ref\": \"VpcName\"\n" +
                        "        }\n" +
                        "      }\n" +
                        "    }\n" +
                        "  }\n" +
                        "}")
                .setStackName("stackName")
                .setRegionId("cn-hangzhou")
                .setTimeoutInMinutes(40L)
                .setParameters(java.util.Arrays.asList(
                        parameters0,
                        parameters1
                ));
```

`//`复制代码运行后，请自行打印`API`的返回值。

```
        client.createStack(createStackRequest);
        Sample.describeRegions(client);
        Sample.getStack(client, "yourStackId", REGIONID);
        Sample.deleteStack(client, "yourStackId", REGIONID);
    }
}
```

### 使用手册

资源编排例

#### 安装ROS SDK for Java

安装ROS SDK for Java时，您需要先获取ROS SDK for Java，然后添加Maven依赖。

**步骤一：获取ROS SDK for Java**

阿里云专有云Java SDK支持1.8及以上版本的JDK。如果要使用ROS SDK for Java，您需要安装阿里云 Java SDK核心库（4.5.17及以上版本）和ROS SDK for Java（1.0.1及以上版本）。 更多信息，请参见ROS SDK for Java。

**步骤二：添加Maven依赖**

安装SDK时，您需要在pom.xml文件中添加以下依赖。

```xml
<dependencies>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>tea-openapi</artifactId>
        <version>0.0.19</version>
    </dependency>
    <dependency>
        <groupId>com.aliyun</groupId>
        <artifactId>ros20190910</artifactId>
        <version>1.0.1</version>
    </dependency>
</dependencies>
```

#### 设置身份验证凭证

当您使用阿里云专有云SDK访问阿里云专有云服务时，需要提供授权的账号进行身份验证。本文为您介绍如目前，Java SDK支持通过AccessKey进行身份验证。具体操作，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化客户端时设置凭据。

**警告**

请确保包含AccessKey的代码不会泄露（例如：不要将代码提交到外部公开的GitHub项目），否则将会危及您的信息安全。

```java
private static String ACCESSKEYID = "<yourAccessKeyId>"; //请替换为您实际的AccessKey ID
```

。

```java
private static String SECRET = "<yourAccessKeySecrect>"; //请替换为您实际的AccessKey Se
```

`cret`。

```java
private static String REGIONID = "<yourRegionId>"; //请替换为您实际的RegionId。
```

**说明**

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。 资源编排例

#### 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 您可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

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

#### 调用ROS SDK for Java

**操作步骤**

1. 创建AcsClient。

```
new com.aliyun.ros20190910.Client(config)
```

2. 创建请求。
资源编排例请求类的命名规范为 ${apiName}Request 。其中，**${apiName}**为API名称，例如：GetStack。 在引入多个ROS SDK for Java时，有可能存在Request类同名的情况，请注意按照package区分。

```
GetStackRequest getStackRequest = new GetStackRequest()
        .setStackId(stackId)
        .setRegionId(regionId);
```

3. 发起调用并处理返回数据。

```
GetStackResponse resp = client.getStack(getStackRequest); com.aliyun.teaconsole.Client.log(com.aliyun.teautil.Common.toJSONString(TeaModel.buildM (resp)));
```

#### 错误处理

在使用ROS SDK for Java时，如果服务端或者SDK出错，SDK会返回服务端异常信息 （ `ServerException` ）或SDK异常信息（ `ClientException` ）。这些异常信息中包含错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要处理SDK异常信息，只需要处理服务端异常信息。 如果您需要处理SDK异常信息，可以参考如下示例编写代码：

```
try {
    FooResponse response = client.getAcsResponse(request);
```

`//`处理`Response`。

```
}catch (ServerException e){
```

`//`添加您自己的异常处理逻辑。 `//`例如：打印具体的异常信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`//`如果遇到棘手问题，可以提交工单，并提供`RequestId`。

```java
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
```

/添加您自己的异常处理逻辑。 `//`例如：打印具体的异常信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

资源编排示例

## ROS SDK for Python调用示例

### 快速开始

**环境准备**

使用ROS SDK for Python前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具获取ROS的Endpoint。具体操作，请参见获取ROS的Endpoint。
1. 安装阿里云Python SDK核心库。
如果您使用的是Python 2.x，执行以下命令。

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令。

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装ROS SDK for Python。
如果您使用的是Python 2.x，执行以下命令。

```
pip install aliyun-python-sdk-ros
```

如果您使用的是Python 3.x，执行以下命令。

```
pip3 install aliyun-python-sdk-ros
```

**步骤二：使用ROS SDK for Python**

1. 创建客户端实例。在创建客户端实例时，您需要获取Region ID、AccessKey ID和AccessKey
Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <ros.aliyuncs.com>：请替换为您实际的产品访问地址。 资源编排示例

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRequest
# global config
```

`region_id = '<yourRegionID>' #` 请替换为您实际的地域`ID`。 `access_key = '<yourAccessKeyID>' #` 请替换为您实际的的`AccessKey ID`。

```
acces_secret = '<yourAccessKeySecret>' # 请替换为您实际的AccessKey Secret。
```

`endpoint = '<ros.aliyuncs.com>' #` 产品访问域名，当前为示例值，请替换为您实际的产品访问地址。

```bash
# create client
clt = client.AcsClient(access_key, acces_secret, region_id, endpoint=endpoint)
# setup request
request = ListResourceTypesRequest()
```

`request.set_accept_format('json') #` 设置返回数据格式。

```bash
# get response
response = clt.do_action_with_exception(request) print response
```

### 使用手册

#### 安装ROS SDK for Python

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上版本，您可以通过pip安装专有云Python SDK。
1. 安装阿里云Python SDK核心库。
如果您使用的是Python 2.x，执行以下命令。

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令。

```
pip3 install aliyun-python-sdk-core-v3
```

2. 安装ROS SDK for Python。
如果您使用的是Python 2.x，执行以下命令。

```
pip install aliyun-python-sdk-ros
```

如果您使用的是Python 3.x，执行以下命令。

```
pip3 install aliyun-python-sdk-ros
```

#### 设置身份验证凭证

当您使用阿里云专有云SDK访问阿里云专有云服务时，需要提供授权的账号进行身份验证。本文为您介绍如目前，ROS SDK for Python支持通过AccessKey进行身份验证。具体操作，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化客户端时设置凭据。 资源编排示例请确保包含AccessKey的代码不会泄露（例如：不要将代码提交到外部公开的GitHub项

**警告**

目），否则将会危及您的信息安全。

```python
from aliyunsdkcore import client clt = client.AcsClient(secret_id, secret_key, region_id, endpoint=endpoint)
```

#### 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。

| 行 | python -c "import ssl" | 检查Pyth |
|---|---|---|
| ImportError: No module named ssl |  |  |

若没有OpenSSL，运行以下命令安装： `pip install pyopenssl # Python 2`使用此命令。

**说明**

若本地环境为Python 3，则运行 `pip3 install pyopenssl` 命令。

**设置单个请求的HTTP/HTTPS协议**

参考以下代码示例为一个接口设置HTTPS调用：

```java
import DescribeInstancesRequest request = DescribeInstancesRequest() request.set_protocol_type("https")
```

# 取值：`"https"` 或 `"http"`

**设置全局默认协议**

参考以下代码示例设置全局默认协议：

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
```

# 创建请求并调用 `client.do_action_with_exception()` 来发送请求

#### 调用ROS SDK for Python

资源编排示例

**操作步骤**

1. 导入ROS SDK for Python。

```python
from aliyunsdkcore import client from aliyunsdkros.request.v20190910.ListResourceTypesRequest import ListResourceTypesRequest
```

2. 创建AcsClient。

```
clt = client.AcsClient(access_key, access_secret, region_id, endpoint=endpoint)
```

3. 创建Request对象。

```
request = ListResourceTypesRequest() request.set_accept_format('json')
```

4. 发起调用并处理返回数据。

```
response = clt.do_action_with_exception(request) print response
```

#### 错误处理

在使用ROS SDK for Python时，如果服务端或者SDK出错，SDK会返回服务端异常信息 （ `ServerException` ）或SDK异常信息（ `ClientException` ）。这些异常信息中包含错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要处理SDK异常信息，只需要处理服务端异常信息。 如果您需要处理SDK异常信息，可以参考如下示例编写代码：

```
#coding=utf-8
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
```

# 添加您自己的异常处理逻辑。
# 例如：打印具体的异常信息。

```
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

资源编排

## ROS SDK for Go调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可使用。本文为您介绍如何获取并调用ROS SDK for Go。

**环境准备**

使用ROS SDK for Go前，您需要一个授权账号以及一对AccessKey ID和AccessKey Secret。具体操获取ROS的Endpoint。具体操作，请参见获取ROS的Endpoint。

**步骤一：安装阿里云Go SDK核心包**

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令安装阿里云Go SDK核心包。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**步骤二：使用ROS SDK for Go**

1. 初始化客户端实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不

**说明**

保留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <Endpoint>：请替换为ROS Endpoint。 资源编排

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

)

```
func main() {
```

`//`创建客户端实例。

```
    client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>",
"<yourAccessKeySecret>")
    if err != nil {
```

`//`异常处理。

```
        panic(err)
    }
```

`//`创建`API`请求并设置参数。

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Scheme = "https" // https | http
    request.Domain = "ros.aliyuncs.com"
    request.Version = "2019-09-10"
    request.QueryParams["RegionId"] = "<yourRegionID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
     }
    fmt.Print(response.GetHttpContentString())
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

当您使用阿里云专有云SDK访问阿里云专有云服务时，需要提供授权的账号进行身份验证。本文为您介绍如目前，ROS SDK for Go支持通过AccessKey进行身份验证。具体操作，请参见获取AccessKey。 使用AccessKey作为访问凭据时，需要在初始化客户端时设置凭据。 资源编排请确保包含AccessKey的代码不会泄露（例如：不要将代码提交到外部公开的GitHub项

**警告**

目），否则将会危及您的信息安全。 `//` 初始化客户端实例。

```
client, err := sdk.NewClientWithAccessKey("<yourRegionID>", "<yourAccessKeyID>", "<your AccessKeySecret>")
```

以上代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。

#### 错误处理

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即 `sdk.errors` 包下的 `ClientError` 和 `ServerError` 。这些错误是基于Go的标准错误接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理异常。

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
```

`//`获取异常信息。

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现错误，并无法自动化处理时，SDK会返回一个 `ClientError` 。

| 您可以通过以下代码来获取并判断ROS | ClientError | 中的错误信息： |
|---|---|---|
| client, err := sdk.NewClientWithAccessKey("cn-hangzhou-ste4-d01", "<accessKeyId>", "<ac cessSecret>") if clientError, ok := err.(*errors.ClientError); ok{ //获取错误码。 clientError.ErrorCode() //获取错误描述。 clientError.Message() //获取原始错误。 clientError.OriginError() } |  |  |

资源编排

| 说明使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参见以下代码： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" //新增错误包。 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成 `ServerError` 返回。在这种情况下，您依然可以从 Response中获得原始的HTTP应答。

| 您可以通过以下代码来获取并判断ROS | ServerError | 以及Response中的错误信息： |
|---|---|---|
| response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{ //获取错误码。 serverError.ErrorCode() //获取错误描述。 serverError.Message() //获取原始HTTP应答。 response.GetOriginHttpResponse() } |  |  |

| 说明使用具体异常结构时需要引入异常结构包 github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors ，引入方法请参见以下代码： package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" //新增错误包。 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |  |  |
|---|---|---|
|  | github.com/aliyun/alibaba-cloud-sdk- |  |

#### 使用CommonRequest调用OpenAPI接口

当您要调用的某个产品的API没有提供SDK时，或者提供的SDK中的请求参数和返回值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI 接口的调用。 资源编排以下代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保

**说明**

留。 涉及替换的可变参数如下： <yourRegionID>：请替换为您实际的地域ID。 <yourAccessKeyID>：请替换为您实际的AccessKey ID。 <yourAccessKeySecret>：请替换为您实际的AccessKey Secret。 <ros.aliyuncs.com>：请替换为您实际的产品访问地址。 <yourSecurityToken>：请替换为您实际的SecurityToken。 <yourResourceGroupID>：请替换为您实际的资源集ID。 <yourOrganizationID>：请替换为您实际的组织ID。 资源编排

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

`"<yourRegionID>", //`请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //`请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>") //`请替换为您实际的`AccessKey Secret`。

```
    if err != nil {
        panic(err)
    }
    request := requests.NewCommonRequest()
    request.Method = "POST"
```

`request.Domain = "<ros.aliyuncs.com>" //`产品访问域名，当前为示例值，请替换为您实际的产品访问地址。

```
    request.Version = "2019-09-10"
```

`//`因为是`RPC`接口，所以需指定`API`名称。 `//`业务参数。

```
    request.QueryParams["RegionId"] = "<yourRegionID>"
```

`/*` 当使用`STS AccessKey`调用`RPC`接口时，需要在参数中加上`SecurityToken`字段。 调用方式如下：

```
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
```

请替换为您实际的`SecurityToken`。 `*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" //必填，调用来源说明。
```

`request.Headers["x-acs-regionid"] = "<yourRegionID>" //`非必填，请替换为您实际的地域`ID`。

```
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" //非必填，请替换为
```

您实际的资源集`ID`。

```
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" //必填，请替换为您实
```

际的组织`ID`。

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
    fmt.Print(response.GetHttpContentString())
}
```

资源编排

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
资源编排
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

调用示例接口信息：产品（ROS）、接口（ListStacks）、版本（2019-09-10）。 调用示例如下：

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 资源编排

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
        request.setSysDomain("<ROSEndpoint>");
```

`//` 设置访问接口版本

```
        request.setSysVersion("2019-09-10");
        // 设置LocationProduct
        request.setSysProduct("ROS");
```

`//` 设置访问接口的名称

```
        request.setSysAction("ListStacks");
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
            System.out.println("RequestId:" + e.getRequestId());
```

资源编排

```
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

**重要**

不建议直接从SDK中心下载SDK到专有云场景下使用，公有云的SDK不一定支持专有云的API，可能存在兼容性问题，请谨慎使用！

**背景信息**

当前支持RPC和ROA的方式调用API。

**CommonRequest调用示例**

调用示例接口信息：产品（ROS）、接口（ListStacks）、版本（2019-09-10）。 示例代码如下： 资源编排

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
```

`//` 产品接口信息参数

```
    request.Product = "ROS"
    request.Version = "2019-09-10"
```

`//` 云产品的`Endpoint`地址

```
    request.Domain = "ros.inter.env230.shuguang.com"
```

`//` 设置请求方式

```
    request.Method = "POST"
    request.Domain = "<ROSEndpoint>"
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

**设置代理**

当您在调用实例时，或许会需要设置代理，您可以通过以下两种方式设置代理。 通过环境变量设置。 环境变量HTTP_PROXY、HTTPS_PROXY或者NO_PROXY。 设置代码如下： 资源编排

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

资源编排

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

调用示例接口信息：产品（ROS）、接口（ListStacks）、版本（2019-09-10）。 示例代码如下：

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

# client和`https`或`http`一起使用

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

# 非必填，资源集`ID`
资源编排

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
    request.set_version("2019-09-10")
    request.set_endpoint("<ROSEndpoint>")   //ROSEndpoint请替换为真实地址
    request.set_product("ROS")
    request.set_method("POST")
```

# 设置请求协议类型

```
    request.set_protocol_type('http')
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
from aliyunsdkros.request.v20190910.ListStacksRequest import ListStacksRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # 地域ID
```

)

```
request.set_protocol_type('https') # 使用https client.do_action_with_exception(request)
```

资源编排

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

) 资源编排

## API参考

### API概览

资源编排服务ROS（Resource Orchestration Service）提供以下API接口。

| API | 描述 |
|---|---|
| CreateStack | 调用CreateStack接口创建资源栈。 |
| ContinueCreateStack | 资源栈创建失败后，调用ContinueCreateStack接口重新创建资源栈。 |
| UpdateStack | 调用UpdateStack接口更新资源栈。 |
| CancelUpdateStack | 调用CancelUpdateStack接口取消更新资源栈。 |
| GetStack | 调用GetStack接口查询资源栈信息。 |
| DeleteStack | 调用DeleteStack接口删除资源栈。 |
| ListStacks | 调用ListStacks接口查询资源栈列表。 |
| PreviewStack | 调用PreviewStack接口预览指定模板将要创建的资源栈信息。 |
| ListStackEvents | 调用ListStackEvents接口查询资源栈及栈内资源的事件。 |

| API | 描述 |
|---|---|
| GetResourceTypeTemplate | 调用GetResourceTypeTemplate接口根据资源类型查询该资源的模板。 |
| ListStackResources | 调用ListStackResources接口查询某个资源栈的资源列表。 |
| GetStackResource | 调用GetStackResource接口查询某个资源栈的资源。 |
| GetResourceType | 调用GetResourceType接口查询资源类型的详细信息。 |

| API | 描述 |
|---|---|
| ValidateTemplate | 调用ValidateTemplate接口验证将要创建资源栈的模板。 |
| GetTemplate | 调用GetTemplate接口查询资源栈、自定义模板的模板详情。 |
| DeleteTemplate | 调用DeleteTemplate接口删除模板。 |
| ListTemplates | 调用ListTemplates接口查询模板列表。 |
| CreateTemplate | 调用CreateTemplate接口创建自定义模板。 |
| UpdateTemplate | 调用UpdateTemplate接口更新模板。 |

资源编排

| GetTemplateSummary | 调用GetTemplateSummary接口获取新模板或者现有模板的信息。 |
|---|---|

### 其他接口

| API | 描述 |
|---|---|
| DescribeRegions | 调用DescribeRegions接口查询地域列表。 |
| SignalResource | 调用SignalResource接口发送信号。 |
| ListStackOperationRisks | 调用ListStackOperationRisks接口检测删除资源栈操作可能涉及的高风险资源，并返回每个资源对应的风险原因。 |

### 调用方式

资源编排服务ROS（Resource Orchestration Service）接口调用是向ROS API的服务端地址发送HTTPS GET或POST请求。您需要按照接口说明在请求中加入相应请求参数，调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集进行编码。

**请求结构**

ROS的API是RPC风格，您可以通过发送HTTPS GET或POST请求调用ROS API。 其请求结构如下：

```
https://Endpoint/?Action=xx&Parameters
```

请求结构中参数说明如下表所示。

| 参数 | 描述 |
|---|---|
| Endpoint | 资源编排API的服务接入地址为ros.aliyuncs.com。 |
| Action | 要执行的操作。例如：调用ListStacks查询资源栈列表。 |
| Parameter s | 请求参数，每个参数之间用and（&）分隔。 请求参数由公共请求参数和API自定义参数组成。公共参数中包含API版本号、身份验证等信息。更多信息，请参见公共参数。 |

**请求示例**

```
&RegionId=cn-hangzhou-180e-d01 &Format=JSON &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dg**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &Timestamp=2020-06-01T12:00:00Z
```

… 资源编排

### 签名机制

为保证API的安全调用，在调用API时阿里云会对每个API请求通过签名（Signature）进行身份验证。无论使用HTTP还是HTTPS协议提交请求，都需要在请求中包含签名信息。

**概述**

RPC API要按以下格式在API请求的Query中增加签名（Signature）。

```
https://Endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC- SHA1&Signature=CT9X0VtwR86fNWSnsc6v8YGOjuE%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e 0ad82fd6cf
```

其中：
**SignatureMethod**：签名方式，目前支持HMAC-SHA1。
**SignatureVersion**：签名算法版本，目前版本是1.0。
**SignatureNonce**：唯一随机数，用于防止网络重放攻击。用户在不同请求间要使用不同的随机数值，
建议使用通用唯一识别码UUID（Universally Unique Identifier）。
*************：使用AccessKey Secret对请求进行对称加密后生成的签名。
签名算法遵循RFC 2104 HMAC-SHA1规范，使用AccessKey Secret对编码、排序后的整个请求串计算 HMAC值作为签名。签名的元素是请求自身的一些参数，由于每个API请求内容不同，所以签名的结果也不尽相同。可参考本文的操作步骤，计算签名值。

```
Signature = Base64( HMAC-SHA1( AccessKey Secret, UTF-8-Encoding-Of(StringToSign)) )
```

**步骤一：构造待签名字符串**

1. 使用请求参数构造规范化的请求字符串（Canonicalized Query String）。
i. 按照参数名称的字典顺序对请求中所有的请求参数（包括公共请求参数和接口的自定义参数，但不包括公共请求参数中的Signature参数）进行排序。 当使用GET方法提交请求时，这些参数就是请求URI中的参数部分，即URI中“?”之后

**说明**

由“&”连接的部分。 资源编排 ii. 对排序之后的请求参数的名称和值分别用UTF-8字符集进行URL编码。编码规则请参考下表。

| 字符 | 编码方式 |
|---|---|
| A~Z、a~z和0~9以及“-”、“ ”、 _ “.”和“~” | 不编码。 |
| 其它字符 | 编码成 %XY 的格式，其中 XY 是字符对应ASCII码的16进制表示。例如英文的双引号（"）对应的编码为 %22 。 |
| 扩展的UTF-8字符 | 编码成 %XY%ZA… 的格式。 |
| 英文空格 | 编码成 %20 ，而不是加号（+）。 该编码方式和一般采用的 application/x-www-form- urlencoded MIME格式编码算法（例如Java标准库中的 java.net.URLEncoder 的实现）存在区别。编码时可以先用标准库的方式进行编码，然后把编码后的字符串中的加号（+）替换成 %20 ，星号（*）替换成 %2A ， %7E 替换回波浪号（~），即可得到上述规则描述的编码字符串。本算法可以用下面的 percentEncode 方法来实现： private static final String ENCODING = "UTF-8"; private static String percentEncode(String value) throws UnsupportedEncodingException { return value != null ? URLEncoder.encode(value, ENCODING).replace("+", "%20").replace("*", "%2A").replace("%7E", "~") : null; } |

|  | urlencoded |  |
|---|---|---|

iii. 将编码后的参数名称和值用英文等号（=）进行连接。 iv. 将等号连接得到的参数组合按步骤i排好的顺序依次使用“&”符号连接，即得到规范化请求字符串。
2. 将构造的规范化字符串按照下面的规则构造成待签名的字符串。

```
StringToSign=
      HTTPMethod + “&” +
      percentEncode(“/”) + ”&” +
       percentEncode(CanonicalizedQueryString)
```

其中：
**HTTPMethod** 是提交请求用的HTTP方法，例如GET。
**percentEncode(“/”)** 是按照URL编码规则对字符“/”进行编码得到的值，即%2F。
**percentEncode(CanonicalizedQueryString)** 是对构造的规范化请求字符串按URL编码规则
编码后得到的字符串。

**步骤二：计算签名值**

1. 按照RFC2104的定义，计算待签名字符串（StringToSign）的HMAC值。
计算签名时使用的Key就是您持有的AccessKey Secret并加上一个“&”字符

**说明**

（ASCII:38）, 使用的哈希算法是SHA1。
2. 按照Base64编码规则把上面的HMAC值编码成字符串，即得到签名值（Signature）。
3. 将得到的签名值作为**Signature**参数添加到请求参数中。
资源编排得到的签名值在作为最后的请求参数值提交时要和其它参数一样，按照RFC3986的规则

**说明**

进行URL编码。

**示例**

以调用 `DescribeRegions` 接口查询地域为例。假设您获得了 `AccessKeyID=testid` 以及 `AccessKeySecret=testsecret` ，签名流程如下所示：
1. 构造规范化请求字符串。

```
http://ros.aliyuncs.com/?Timestamp=2019-08- 23T12%3A46%3A24Z&Format=XML&AccessKeyId=testid&Action=DescribeRegions&SignatureMethod=H C-SHA1&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&Version=2019-09-10&Signatu reVersion=1.0
```

2. 构造待签名字符串。

```
GET&%2F&AccessKeyId%3Dtestid%26Action%3DDescribeRegions%26Format%3DXML%26SignatureMetho 3DHMAC-SHA1%26SignatureNonce%3D3ee8c1b8-83d3-44af-a94f- 4e0ad82fd6cf%26SignatureVersion%3D1.0%26Timestamp%3D2019-08- 23T12%253A46%253A24Z%26Version%3D2019-09-10
```

| 值。因为 | AccessKeySecret=testsecret |  |
|---|---|---|
| OLeaidS1JvxuMvnyHOwuJ+uX5qY= |  |  |
|  |  | 。示例 |

```
Signature = Base64( HMAC-SHA1( AccessSecret, UTF-8-Encoding-Of(StringToSign) ) )
```

4. 添加RFC3986规则编码后的 Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D 到步骤1的URL中。

```
http://ros.aliyuncs.com/? SignatureVersion=1.0&Action=DescribeRegions&Format=XML&SignatureNonce=3ee8c1b8-83d3-4 4af-a94f-4e0ad82fd6cf&Version=2019-09- 10&AccessKeyId=testid&Signature=OLeaidS1JvxuMvnyHOwuJ%2BuX5qY%3D&SignatureMethod=HMAC- SHA1&Timestamp=2019-08-23T12%253A46%253A24Z
```

通过以上URL，您可以使用浏览器、curl或者wget等工具发起HTTP请求调用 `DescribeRegions` ，查看阿里云的地域列表。

### 公共参数

公共参数分为公共请求参数和公共返回参数。

**公共请求参数**

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|
| Format | String | 否 | 返回消息的格式。取值： JSON（默认值） XML |
| Version | String | 是 | API版本号，使用YYYY- MM-DD日期格式。取值：2019-09-10。 |

资源编排

| AccessKeyId | String | 是 | 访问密钥ID。由阿里云颁发给用户，用于API调用时的身份验证。 |
|---|---|---|---|
| Signature | String | 是 | 消息签名。关于签名的计算方法，请参见签名机制。 |
| SignatureMethod | String | 是 | 签名方式。取值：HMAC- SHA1。 |
| Timestamp | String | 是 | 请求的时间戳，为日期格式。使用UTC时间并按照 ISO8601标准，格式为： YYYY-MM- DDThh:mm:ssZ。 例如：北京时间2020年 01月10日20点00分00 秒，表示为2020-01- 10T12:00:00Z。 |
| SignatureVersion | String | 是 | 签名算法版本。取值： 1.0。 |
| SignatureNonce | String | 是 | 唯一随机数。用于防止网络重放攻击。在不同请求间要使用不同的随机数值。 |

公共请求参数示例如下：

```
https://ros.aliyuncs.com/?Action=XXXXXX &Format=xml &Version=2019-09-10 &Signature=Pc5WB8gokVn0xfeu%2FZV%2BiNM1dg**** &SignatureMethod=HMAC-SHA1 &SignatureNonce=1521552885**** &SignatureVersion=1.0 &AccessKeyId=LTAI******************** &Timestamp=2020-06-01T12:00:00Z
```

**公共返回参数**

API返回结果采用统一格式，调用成功返回的数据格式有XML和JSON两种，可以在发送请求时指定返回的数据格式，默认为JSON格式。每次接口调用，无论成功与否，系统都会返回一个唯一识别码**RequestId**。 返回 `2xx` HTTP状态码表示调用成功。 返回 `4xx` 或 `5xx` HTTP状态码表示调用失败。 公共返回参数示例如下： XML格式资源编排

```xml
<?xml version="1.0" encoding="utf-8"?>
```

<!--结果的根结点`-->` <接口名称`+Response>` <!--返回请求标签`-->`

```xml
        <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
```

<!--返回结果数据`-->` `</`接口名称`+Response>` JSON格式

```json
{
    "RequestId":"4C467B38-3910-447D-87BC-AC049166F216"
```

`/*`返回结果数据`*/`

```
}
```

### 公共错误码

**客户端错误码**

| 错误码 | 错误信息 | HTTP状态码 | 描述 |
|---|---|---|---|
| UnknownError | The request processing has failed due to some unknown error. | 400 | 客户端出现非服务端原因的未知错误。 |
| MissingParameter | The input parameter {name} should be specified. | 400 | 缺少参数，name为参数名。 |
|  | One of the input parameters {names} should be specified. | 400 | 缺少参数，必须指定多个参数中的一个。names为相关的参数的列表。 |
|  | The input parameter {name} should be specified, {reason}. | 400 | 缺少参数，name为参数名，reason为原因。 |
| InvalidParameter | The specified parameter {name} is invalid. | 400 | 无效参数，name为参数名。 |
|  | The specified parameter {name} is invalid, {reason}. | 400 | 无效参数，name为参数名，reason为原因。 |
| MultipleParameter | Only one of the input parameters {names} can be specified. | 400 | 指定参数过多，只能指定多个参数中的一个。names为相关的参数的列表。 |
| InvalidIdempotence Parameter | The specified parameters are different from before. | 400 | 幂等token相同但是参数不同。 |
| LastTokenProcessin g | The last token request is processing. | 400 | 正在处理上一条令牌请求，请您稍后再试。 |
| Invalid | Data supplied was not valid: {reason}. | 400 | 无效值，reason为原因。 |
| InvalidValue | {reason}. | 400 | 无效值，reason为原因。 |

资源编排

| RequestLimitExcee ded | Request limit exceeded: {reason}. | 400 | 请求包含超过限制的内容，reason为原因。部分限制可通过调整配额改变。 |
|---|---|---|---|
| NotSupported | {feature} is not supported. | 400 | 不支持feature，feature为特性或操作。 |
| MismatchNextToke n | {name} mismatches next token. | 400 | NextToken不匹配，name为不匹配项。 |
| AssumeRoleFailure | Fail to assume role {name}: {reason} | 400 | ROS获取一个扮演该角色的临时身份失败。name为RAM角色名，reason为原因。 |
| Forbidden | You are not authorized to complete this action. | 403 | 您无权完成此操作。 |
|  | A required authorization for the specified action {api} is not supplied. Code: {code} RequestId: {request id} _ | 403 | 用户没有授权ROS调用接口。api 为接口名，code为错误码，request id为请求ID。 _ |
| AccountTypeNotSu pported | Account type not supported. | 403 | 账号类型不支持。 |
| NotFound | {reason}. | 404 | 请求包含不存在的内容，reason 为原因。 |

**服务端错误码**

| 错误码 | 错误信息 | HTTP状态码 | 描述 |
|---|---|---|---|
| InternalError | Server error. | 500 | 内部错误。 |
| ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 | 服务器故障，请重试。如果多次尝试失败，请提交工单。 |

### 资源栈相关接口

#### CreateStack

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateStack | 要执行的操作，取值：CreateStack。 |

资源编排

| Parameters.N.Pa rameterKey | String | 是 | InstanceId | 参数名称。 如果未指定参数的名称和取值，ROS将使用模板中指定的默认值。 N最大值为：200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |
|---|---|---|---|---|
| Parameters.N.Pa rameterValue | String | 是 | i-xxxxxx | 参数值。 N最大值为：200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackName | String | 是 | MyStack | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| DisableRollback | Boolean | 否 | false | 当创建资源栈失败时，是否禁用回滚策略。 取值： true：禁用回滚，即在创建资源栈失败时不进行回滚。 false（默认值）：不禁用回滚，即在创建资源栈失败时进行回滚。 |
| TemplateBody | String | 否 | { "ROSTemplateF ormatVersion": "2015-09-01" } | 模板主体的结构。长度为1~524,288个字节。如果长度较大，则建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免因URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |

资源编排

| StackPolicyURL | String | 否 | oss://ros-stack- policy/demo | 包含资源栈策略的文件的位置。 URL必须指向位于Web服务器（HTTP或HTTPS） 或阿里云OSS存储桶（例如： oss://ros/stack-policy/demo、 oss://ros/stack-policy/demo? RegionId=cn-hangzhou）中的策略，策略文件最大长度为16,384个字节。 如未指定OSS地域，默认与接口参数RegionId相同。 说明您必须指定参数 StackPolicyBody或 StackPolicyURL，但不能同时指定。 URL最大长度为1350个字节。 |
|---|---|---|---|---|
| TimeoutInMinute s | Long | 否 | 10 | 创建资源栈的超时时间。 默认值：60。 单位：分钟。 |
| StackPolicyBody | String | 否 | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | 包含资源栈策略主体的结构，长度为 1~16,384个字节。 说明您必须指定 StackPolicyBody或 StackPolicyURL参数，但不能同时指定。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。该值由客户端生成， 并且必须是全局唯一的。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |
| TemplateURL | String | 否 | oss://ros- template/demo | 包含模板主体的文件的位置。URL必须指向位于HTTP Web服务器（HTTP或 HTTPS）或阿里云OSS存储桶中的模板 （1~524,288个字节）。OSS存储桶的 URL例如oss://ros/template/demo或 oss://ros/template/demo? RegionId=cn-hangzhou。如未指定OSS 地域，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 |

资源编排

| NotificationURLs .N | RepeatL ist | 否 | http://my- site.com/ros- event | 接收资源栈事件的URL回调地址。目前仅支持HTTP POST。 N最大值：5。 每个URL的最大长度：1024个字节。 资源栈的状态发生变化时，会进行通知。 当资源栈启用回滚时，CREATE FAILED（创建失败）和 _ UPDATE FAILED（更新失败）不会通 _ 知，而CREATE ROLLBACK（创建失败回 _ 滚）和ROLLBACK（更新失败回滚）会进行通知。 说明 IN PROGRESS状态不 _ 会通知。 无论资源栈是否定义了Outputs都会进行通知。通知内容示例如下： { "Outputs": [ { "Description": "No description given", "OutputKey": "InstanceId", "OutputValue": "i-xxx" } ], "StackId": "80bd6b6c- e888-4573-ae3b- 93d29113****", "StackName": "test- notification-url", "Status": "CREATE COMPLETE" _ } |
|---|---|---|---|---|

资源编排

| RamRoleName | String | 否 | test-role | RAM角色名称。ROS会扮演该角色创建资源栈，使用角色的凭证代表用户进行接口调用。 ROS始终将此角色用于资源栈上将进行的操作。只要用户有权在资源栈上进行操作，即使用户无权使用角色，ROS也会使用此角色，确保角色授予最少的权限。 如果用户未指定该值，ROS将使用以前与资源栈关联的角色。如果没有可用角色，ROS将使用从您的用户凭证中生成的临时凭证。 RAM角色名称最大长度为64个字符。 |
|---|---|---|---|---|
| DeletionProtecti on | String | 否 | Enabled | 是否开启资源栈删除保护。取值： Enabled：开启资源栈删除保护。 Disabled（默认）：关闭资源栈删除保护。此时支持通过控制台或 API（DeleteStack）释放资源栈。 说明嵌套资源栈删除保护与根资源栈一致。 |
| CreateOption | String | 否 | KeepStackOnCre ationComplete | 用于控制创建资源栈的行为，取值： KeepStackOnCreationComplete（ 默认值）：创建资源栈成功后保留资源栈及资源栈中的资源，占用ROS允许创建的资源栈数量限额。 AbandonStackOnCreationComplet e：创建资源栈成功后删除资源栈，但保留所有资源，不占用ROS允许创建的资源栈数量限额。如果创建资源栈失败，资源栈会保留。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |

**示例**

请求示例资源编排

```
&RegionId=cn-hangzhou &StackName=MyStack &Parameters.1.ParameterKey=InstanceId &Parameters.1.ParameterValue=i-xxxxxx &TimeoutInMinutes=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
          <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
          <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| 错误代码 | 错误信息 | Http状态码 | 描述 |
|---|---|---|---|
| CircularDependency | Circular Dependency Found: {reason}. | 400 | 模板包含循环引用，reason为具体原因。 |
| InvalidSchema | {reason}. | 400 | 模板格式不正确，reason 为具体原因。 |
| InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | 模板包含不正确的资源属性（输出）引用，resource为资源名，name为属性名。 |
| InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 400 | 模板资源定义中，字段类型不正确，resource为资源名，section为字段名。 |
| InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | 模板包含不正确的引用，name为引用名，referencer为引用者。 |
| InvalidTemplateSectio n | The template section is invalid: {section}. | 400 | 模板包含无效的字段，section为字段名。 |

资源编排

| InvalidTemplateVersio n | The template version is invalid: {reason}. | 400 | 模板版本不正确，reason 为具体原因。 |
|---|---|---|---|
| StackValidationFailed | {reason}. | 400 | 资源栈校验失败，reason 为具体原因。 |
| UnknownUserParamet er | The Parameter ({name}) was not defined in template. | 400 | 传递的参数在模板中未定义，name为参数名。 |
| UserParameterMissing | The Parameter {name} was not provided. | 400 | 参数在模板中已定义，但未传递值，name为参数名。 |
| ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | 资源栈在变更中，name 为资源栈名称或 ID，action为变更操作。 |
| StackExists | The Stack ({name}) already exists. | 409 | 同名资源栈已存在，name为资源栈名称。 |

#### ContinueCreateStack

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ContinueCreate Stack | 要执行的操作，取值： ContinueCreateStack。 |
| Parameters.N.Pa rameterKey | String | 是 | Amount | 覆盖的模板参数的名称。如果未指定特定参数的名称和值，ROS将使用上一次创建时的取值。N的最大值为200。 说明仅在Mode为Recreate 时生效。 |
| Parameters.N.Pa rameterValue | String | 是 | 12 | 覆盖的模板参数的值。N的最大值为200。 仅在Mode为Recreate时生效，覆盖的模板参数限制如下： 不能引发模板Conditions部分中任何 Condition的值的变化，由true变 false，或由false变true。 覆盖参数不能被不重新创建的资源引用。 |

资源编排

| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
|---|---|---|---|---|
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| RecreatingResou rces.N | RepeatL ist | 否 | WebServer | 创建失败的资源将会被重新创建。您可以指定额外需要重新创建的资源列表，ROS 会重新创建所有依赖于其的资源。 |
| RamRoleName | String | 否 | test-role | RAM角色名称。ROS会扮演该角色创建资源栈，使用角色的凭证代表用户进行接口调用。 ROS始终将此角色用于资源栈上将进行的操作。只要用户有权在资源栈上进行操作，即使用户无权使用角色，ROS也会使用此角色，确保角色授予最少的权限。 如果用户未指定该值，ROS将使用以前与资源栈关联的角色。如果没有可用角色，ROS将使用从您的用户凭证中生成的临时凭证。 RAM角色名称最大长度为64个字节。 |

资源编排

| Mode | String | 否 | Recreate | 继续创建模式，取值： Recreate（默认值）： 重新创建如下4类资源，其它为不重新创建的资源： 创建失败的资源。 指定重新创建的资源 （RecreatingResources.N）。 依赖于指定重新创建的资源 （RecreatingResources.N）的资源。 未创建的资源。 RecreatingResources.N、 TemplateBody、TemplateURL、 Parameters参数仅在此模式下生效。 Ignore： 忽略并丢弃所有创建失败的资源、未创建的资源，直接把资源栈标记为成功。 模板内容会发生变化。 |
|---|---|---|---|---|

资源编排

| TemplateBody | String | 否 | { "ROSTemplateF ormatVersion": "2015-09-01" } | 模板主体的结构。长度为1~524,288个字节。 如果长度较大，则建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 仅在Mode为Recreate时生效，模板限制如下： 只能修改模板的Description、 Metadata、Resources、Outputs部分。 不能增加或删除Section（模板内容的第一层）。 模板的Resources部分限制如下： 对于不重新创建的资源，既不能删除，也不能修改其模板内容。 对于重新创建的资源，既可以删除， 也可以修改其模板内容。 可以增加新资源。 |
|---|---|---|---|---|
| TemplateURL | String | 否 | oss://ros- template/demo | 包含模板主体的文件的位置。 URL必须指向位于Web服务器（HTTP或HTTPS）或阿里云OSS存储桶（例如： oss://ros/template/demo、 oss://ros/template/demo? RegionId=cn-hangzhou）中的模板，模板最大为524,288个字节。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 仅在Mode为Recreate时生效，模板限制与TemplateBody相同。 |
| DryRun | Boolean | 否 | false | 此次请求是否只进行检验。取值： true：只做校验，不会实际执行。 false（默认）：会实际执行，继续创建资源栈。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |

资源编排

| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
|---|---|---|---|

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=ContinueCreateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <StackId type="string">0a7c379a-566f-4bc0-b3fb-a301df51****</StackId>
```

`JSON` 格式

```json
{
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "0a7c379a-566f-4bc0-b3fb-a301df51****"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | 模板包含循环引用，reason为具体原因。 |
| 400 | InvalidSchema | {reason}. | 模板格式不正确，reason 为具体原因。 |
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 模板包含不正确的资源属性（输出）引用，resource为资源名，name为属性名。 |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 模板资源定义中，字段类型不正确，resource为资源名，section为字段名。 |

资源编排

| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 模板包含不正确的引用，name为引用名，referencer为引用者。 |
|---|---|---|---|
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | 模板包含无效的字段，section为字段名。 |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | 模板版本不正确，reason 为具体原因。 |
| 400 | StackValidationFailed | {reason}. | 资源栈校验失败，reason 为具体原因。 |
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | 传递的参数在模板中未定义，name为参数名。 |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | 参数在模板中已定义，但未传递值，name为参数名。 |
| 400 | ContinueCreateStackV alidationFailed | {reason}. | 继续创建资源栈校验失败，reason为具体原因。 |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | 资源栈中不存某资源。 name为资源名，stack为资源栈名称或ID。 |
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 资源栈在变更中。name 为资源栈名称或 ID，action为变更操作。 |

#### UpdateStack

请求中Parameters和UsePreviousParameters取值相关。若Parameters中未指定模板中定义的参数： 当UsePreviousParameters取值为false时：如果模板中参数有默认值，则使用默认值；如果模板中参数没有默认值，则需要在Parameters中指定该参数。 当UsePreviousParameters取值为true时：如果创建资源栈时指定了该参数，则使用指定值；如果创建资源栈时未指定该参数，参数在模板中有默认值，则使用默认值。

**请求参数**

资源编排

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateStack | 要执行的操作，取值：UpdateStack。 |
| Parameters.N.Pa rameterKey | String | 是 | Amount | 参数的名称。如果未指定参数的名称和取值，ROS将使用模板中指定的默认值。 N的最大值为200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |
| Parameters.N.Pa rameterValue | String | 是 | 12 | 参数值。N的最大值为200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |
| RegionId | String | 是 | cn-beijing | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。此参数值由客户端生成，并且必须全局唯一。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |

资源编排

| StackPolicyDurin gUpdateBody | String | 否 | {"Statement": [{"Effect": "Allow", "Action": "Update:*", "Principal": "*", "Resource": "*"}]} | 临时覆盖资源栈策略主体的结构。长度为 1~16,384个字节。 如果要更新受保护的资源，请在更新期间指定临时覆盖资源栈策略。如果未指定资源栈策略，将使用与资源栈关联的当前策略。 此参数仅在更改集类型为UPDATE时生效。 您只能指定以下参数之一： StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
|---|---|---|---|---|
| TimeoutInMinute s | Long | 否 | 10 | 更新资源栈的超时时间。 默认值：60。 单位：分钟。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01"} | 模板主体的结构。长度为1~524,288个字节。 如果长度较大，则建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |
| StackPolicyURL | String | 否 | oss://ros-stack- policy/demo | 包含资源栈策略的文件的位置。 URL必须指向位于Web服务器（HTTP或HTTPS） 或阿里云OSS存储桶（例如： oss://ros/stack-policy/demo、 oss://ros/stack-policy/demo? RegionId=cn-hangzhou）的策略，策略的文件最大值为16,384个字节。如未指定 OSS地域，默认与接口参数RegionId相同。 说明您必须指定参数 StackPolicyBody或 StackPolicyURL，但不能同时指定。 URL最大长度为1350个字节。 |

资源编排

| StackPolicyDurin gUpdateURL | String | 否 | oss://ros-stack- policy/demo | 更新资源栈策略的文件的位置。URL必须指向位于Web服务器（HTTP或HTTPS） 或阿里云OSS存储空间（例如： oss://ros/stack-policy/demo、 oss://ros/stack-policy/demo? RegionId=cn-hangzhou）中的策略，策略的文件最大值为16,384个字节。 如未指定OSS地域，默认与接口参数RegionId相同。 说明您必须指定参数 StackPolicyBody或 StackPolicyURL，但不能同时指定。 URL最大长度为1350个字节。 如果要更新受保护的资源，请在更新期间指定临时覆盖资源栈策略。如果未指定资源栈策略，则将使用与资源栈关联的当前策略。此参数仅在更改集类型为UPDATE 时生效。您只能指定以下参数之一： StackPolicyBody StackPolicyURL StackPolicyDuringUpdateBody StackPolicyDuringUpdateURL |
|---|---|---|---|---|
| StackPolicyBody | String | 否 | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | 资源栈策略主体的结构，长度为 1~16,384个字节。 说明您必须指定参数 StackPolicyBody或 StackPolicyURL，但不能同时指定。 |
| UsePreviousPara meters | Boolean | 否 | true | 未传递的参数是否使用上次传递的值。取值： true：未传递的参数使用上次传递的值。 false：未传递的参数不使用上次传递的值。 |
| DisableRollback | Boolean | 否 | false | 当更新资源栈时，此参数无效。如果更新失败，则强制回滚。 |

资源编排

| TemplateURL | String | 否 | oss://ros- template/demo | 包含模板主体的文件的位置。URL必须指向位于HTTP Web服务器（HTTP或 HTTPS）或阿里云OSS存储桶中的模板 （1~524,288个字节）。OSS存储桶的 URL，例如oss://ros/template/demo或 oss://ros/template/demo? RegionId=cn-hangzhou。如未指定OSS 地域，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 |
|---|---|---|---|---|
| RamRoleName | String | 否 | test-role | RAM角色名称。ROS会扮演该角色创建资源栈，使用角色的凭证代表用户进行接口调用。 ROS始终将此角色用于资源栈上将进行的操作。只要用户有权在资源栈上进行操作，即使用户无权使用角色，ROS也会使用此角色，确保角色授予最少的权限。 如果用户未指定该值，ROS将使用以前与资源栈关联的角色。如果没有可用角色，ROS将使用从您的用户凭证中生成的临时凭证。 RAM角色名称最大长度为64个字节。 |
| ReplacementOpt ion | String | 否 | Disabled | 如果资源的属性发生了变化，且变化的属性不支持修改更新（资源物理ID不变）， 是否使用替换更新（删除资源后重新创建，资源物理ID会发生变化）。 取值： Enabled：允许替换更新。 Disabled（默认）：不允许替换更新。 说明修改更新的优先级高于替换更新。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |

**示例**

资源编排请求示例

```
&RegionId=cn-beijing &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &Parameters.1.ParameterKey=Amount &Parameters.1.ParameterValue=12
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | 模板包含循环引用。 reason为具体原因。 |
| 400 | InvalidSchema | {reason}. | 模板格式不正确。reason 为具体原因。 |
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 模板包含不正确的资源属性（输出）引用。 resource为资源名，name为属性名。 |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 模板资源定义的字段类型不正确。resource为资源名，section为字段名。 |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 模板包含不正确的引用。 name为引用名，referencer为引用者。 |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | 模板包含无效的字段。 section为字段名。 |

资源编排

| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | 模板版本不正确。reason 为具体原因。 |
|---|---|---|---|
| 400 | StackPolicyValidationF ailed | Action denied by stack policy: {reason}. | 未通过资源栈策略校验。 reason为具体原因。 |
| 400 | StackValidationFailed | {reason}. | 资源栈校验失败。reason 为具体原因。 |
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | 传递的参数在模板中未定义。name为参数名。 |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | 参数在模板中已定义，但未传递值。name为参数名。 |
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 资源栈在变更中。name 为资源栈名称或 ID，action为具体的变更操作。 |

#### CancelUpdateStack

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CancelUpdateSt ack | 要执行的操作，取值： CancelUpdateStack。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| CancelType | String | 否 | Safe | 取消更新资源栈类型。取值： Quick：尽快取消更新资源栈。 Safe：尽可能安全地取消更新资源栈。 |

**返回数据**

资源编排

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=CancelUpdateStack &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
         <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
         <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
```

`JSON` 格式

```json
{
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 资源栈在变更中。name 为资源栈名称或 ID，action为具体的变更操作。 |

#### GetStack

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

资源编排

| Action | String | 是 | GetStack | 要执行的操作，取值：GetStack。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。 该值由客户端生成， 并且必须全局唯一。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| CreateTime | String | 2019-08- 01T04:07:39 | 资源栈创建时间。按照ISO8601标准表示，需使用UTC时间，格式：YYYY-MM- DDThh:mm:ss。 |
| Description | String | my stack description | 资源栈的描述信息。 |
| DisableRollbac k | Boolean | false | 当创建资源栈失败时，是否禁用回滚策略。取值： true：禁用回滚，即当创建资源栈失败时不进行回滚。 false（默认值）：不禁用回滚，即当创建资源栈失败时进行回滚。 |
| NotificationUR Ls | List | ["http://127.XX.XX. 1:8080/x", "http://127.0.XX.XX :8080/y"] | 接收资源栈事件的URL回调地址。 |
| Outputs | List | [{"Description": "Instance ID","OutputKey": "InstanceId","Outp utValue": "i- a****"}] | 资源栈输出列表。 |
| Parameters | Array of Parameter |  | 资源栈入参。 |
| ParameterKey | String | InstanceType | 参数名称。 |
| ParameterValu e | String | ecs.cm4.6xlarge | 参数值。 |

资源编排

| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | 父资源栈ID。 |
|---|---|---|---|
| RegionId | String | cn-beijing | 要创建的资源栈所属的地域ID。 |
| Status | String | CREATE COMPLET _ E | 资源栈状态，取值： CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |

资源编排

| StackName | String | MyStack | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
|---|---|---|---|
| UpdateTime | String | 2019-08- 01T04:07:39 | 资源栈更新时间。按照ISO8601标准表示，需使用UTC时间，格式：YYYY-MM- DDThh:mm:ss。 |
| StatusReason | String | Stack successfully created | 资源栈状态原因。 |
| TemplateDesc ription | String | Some description | 资源栈描述。 |
| TimeoutInMinu tes | Integer | 10 | 创建资源栈的超时时间。单位：分钟。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |
| DeletionProtec tion | String | Enabled | 是否开启资源栈删除保护，取值： Enabled：开启资源栈删除保护。 Disabled：关闭资源栈删除保护。此时支持通过控制台或API（DeleteStack）释放资源栈。 说明嵌套资源栈删除保护与根资源栈一致。 |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | 资源栈最近一次成功的偏差检测的时间。 |
| RamRoleName | String | test-role | RAM角色名称。ROS会扮演该角色创建资源栈， 使用角色的凭证代表用户进行接口调用。 ROS始终将此角色用于资源栈上将进行的操作。 只要用户有权在资源栈上进行操作，即使用户无权使用角色，ROS也会使用此角色，确保角色授予最少的权限。 如果用户未指定该值，ROS将使用以前与资源栈关联的角色。如果没有可用角色，ROS将使用从您的用户凭证中生成的临时凭证。 RAM角色名称最大长度为64个字节。 |
| RootStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | 最顶层的资源栈的ID。当资源栈为嵌套资源栈时，会返回该属性。 |

资源编排

| StackDriftStat us | String | IN SYNC _ | 资源栈最近一次成功的偏差检测中的资源栈的状态，取值： DRIFTED：资源栈处于偏差状态。 NOT CHECKED：资源栈未进行过成功的偏 _ 差检测。 IN SYNC：资源栈处于同步状态。 _ |
|---|---|---|---|
| StackType | String | ROS | 资源栈类型，取值： ROS：使用ROS模板的资源栈。 Terraform：使用Terraform模板的资源栈。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式资源编排

```xml
    <CreationTime>2019-08-01T04:07:39</CreationTime>
    <Description>No description</Description>
    <DisableRollback>false</DisableRollback>
    <NotificationURLs>http://127.0.XX.XX:8080/x</NotificationURLs>
    <NotificationURLs>http://127.0.XX.XX:8080/y</NotificationURLs>
    <Outputs>
       <Description>Instance ID</Description>
       <OutputKey>InstanceId</OutputKey>
       <OutputValue>i-a****</OutputValue>
    </Outputs>
    <Parameters>
       <ParameterKey>InstanceType</ParameterKey>
       <ParameterValue>ecs.cm4.6xlarge</ParameterValue>
    </Parameters>
    <RegionId>cn-hangzhou</RegionId>
    <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
    <StackName>MyStack</StackName>
    <Status>CREATE_COMPLETE</Status>
    <StatusReason>Stack successfully created</StatusReason>
    <TemplateDescription>Some description</TemplateDescription>
    <TimeoutInMinutes>10</TimeoutInMinutes>
    <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
    <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
    <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
    <StackDriftStatus>IN_SYNC</StackDriftStatus>
    <RamRoleName>test-role</RamRoleName>
    <DeletionProtection>Enabled</DeletionProtection>
    <RootStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</RootStackId>
    <StackType>ROS</StackType>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式资源编排

```json
{
    "CreationTime": "2019-08-01T04:07:39",
    "Description": "No description",
    "DisableRollback": false,
    "NotificationURLs": [
        "http://127.0.XX.XX:8080/x",
        "http://127.0.XX.XX:8080/y"
```

`],`

```json
    "Outputs": [
        {
            "Description": "Instance ID",
            "OutputKey": "InstanceId",
            "OutputValue": "i-a****"
        }
```

`],`

```json
    "Parameters": [
        {
            "ParameterKey": "InstanceType",
            "ParameterValue": "ecs.cm4.6xlarge"
        }
```

`],`

```json
    "RegionId": "cn-hangzhou",
    "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
    "StackName": "MyStack",
    "Status": "CREATE_COMPLETE",
    "StatusReason": "Stack successfully created",
    "TemplateDescription": "Some description",
    "TimeoutInMinutes": 10,
    "UpdatedTime": "2019-08-01T04:07:39",
    "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "DriftDetectionTime": "2020-02-27T07:47:47",
 "StackDriftStatus": "IN_SYNC",
    "RamRoleName": "test-role",
    "DeletionProtection": "Enabled",
    "RootStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
    "StackType": "ROS",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |

#### DeleteStack

**请求参数**

资源编排

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteStack | 要执行的操作，取值：DeleteStack。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| RetainAllResourc es | Boolean | 否 | false | 是否保留该资源栈下的所有资源。 |
| RetainResources .N | RepeatL ist | 否 | WebServer | 需要保留资源的列表。 |
| RamRoleName | String | 否 | test-role | RAM角色名称。ROS会扮演该角色创建资源栈，使用角色的凭证代表用户进行接口调用。 ROS始终将此角色用于资源栈上将进行的操作。只要用户有权在资源栈上进行操作，即使用户无权使用角色，ROS也会使用此角色，确保角色授予最少的权限。 该接口与其他接口不同，如果用户未指定该值，ROS不会使用以前与资源栈关联的角色。如果需要使用角色，请显式指定。 如果没有可用角色，ROS将使用从您的用户凭证中生成的临时凭证。 RAM角色名称最大长度为64个字节。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式资源编排

```xml
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
  "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidOperation.Deleti onProtection | Fail to delete stack {ID}, as deletion protection is enabled. | 资源栈开启了删除保护， 无法被删除。ID为资源栈 ID。 |
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 409 | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 资源栈在变更中。name 为资源栈名称或 ID，action为具体的变更操作。 |

#### ListStacks

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListStacks | 要执行的操作，取值：ListStacks。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |

资源编排

| Status.N | RepeatL ist | 否 | CREATE COMPL _ ETE | 资源栈状态，取值： CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PR _ _ _ _ OGRESS IMPORT CREATE ROLLBACK FAILE _ _ _ D IMPORT CREATE ROLLBACK COMP _ _ _ LETE IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PR _ _ _ _ OGRESS IMPORT UPDATE ROLLBACK FAILE _ _ _ D IMPORT UPDATE ROLLBACK COM _ _ _ PLETE N的取值范围为：1~5。 |
|---|---|---|---|---|
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |
| ParentStackId | String | 否 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 父资源栈ID。 |

资源编排

| StackName.N | RepeatL ist | 否 | MyStack | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。支持使用星号 _ （*）进行模糊搜索。 N的取值范围为：1~5。 |
|---|---|---|---|---|
| PageNumber | Long | 否 | 1 | 资源栈列表的页码。 起始值：1。 默认值：1。 |
| ShowNestedStac k | Boolean | 否 | true | 是否列出嵌套资源栈。取值： true false（默认值） 说明如果指定了 ParentStackId，则该值为true。 |
| Tag.N.Key | String | 否 | usage | 资源栈的标签键。 N的取值范围为：1~20。 |
| Tag.N.Value | String | 否 | test | 资源栈的标签值。 N的取值范围为：1~20。 |
| StackId | String | 否 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。如果不需要资源栈详细信息， 可以指定此参数，代替GetStack接口。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Stacks | Array of Stack |  | 资源栈列表。 |
| CreateTime | String | 2019-08- 01T04:07:39 | 创建时间。按照ISO8601标准表示，需使用UTC 时间，格式：YYYY-MM-DDThh:mm:ss。 |

资源编排

| DisableRollbac k | Boolean | false | 当创建资源栈失败时，是否禁用回滚策略。取值： true：禁用回滚，即当创建资源栈失败时不进行回滚。 false（默认值）：不禁用回滚，即当创建资源栈失败时进行回滚。 |
|---|---|---|---|
| DriftDetection Time | String | 2020-02- 27T07:47:47 | 资源栈最近一次成功的偏差检测的时间。 |
| ParentStackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf692**** | 父资源栈ID。 |
| RegionId | String | cn-hangzhou | 资源栈所属的地域ID。 |
| StackDriftStat us | String | IN SYNC _ | 资源栈最近一次成功的偏差检测中的资源栈状态，取值： DRIFTED：资源栈处于检测状态。 NOT CHECKED：资源栈未进行过成功的偏 _ 差检测。 IN SYNC：资源栈处于同步状态。 _ |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| StackName | String | MyStack | 资源栈名称。 |
| StackType | String | ROS | 资源栈类型。取值为ROS，表示使用ROS模板的资源栈。 |

资源编排

| Status | String | CREATE COMPLET _ E | 资源栈状态，取值： CREATE IN PROGRESS _ _ CREATE FAILED _ CREATE COMPLETE _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CREATE ROLLBACK IN PROGRESS _ _ _ CREATE ROLLBACK FAILED _ _ CREATE ROLLBACK COMPLETE _ _ ROLLBACK IN PROGRESS _ _ ROLLBACK FAILED _ ROLLBACK COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ REVIEW IN PROGRESS _ _ IMPORT CREATE IN PROGRESS _ _ _ IMPORT CREATE FAILED _ _ IMPORT CREATE COMPLETE _ _ IMPORT CREATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT CREATE ROLLBACK FAILED _ _ _ IMPORT CREATE ROLLBACK COMPLETE _ _ _ IMPORT UPDATE IN PROGRESS _ _ _ IMPORT UPDATE FAILED _ _ IMPORT UPDATE COMPLETE _ _ IMPORT UPDATE ROLLBACK IN PROGR _ _ _ _ ESS IMPORT UPDATE ROLLBACK FAILED _ _ _ IMPORT UPDATE ROLLBACK COMPLETE _ _ _ |
|---|---|---|---|
| StatusReason | String | Stack successfully created | 资源栈状态原因。 |
| TimeoutInMinu tes | Integer | 10 | 创建资源栈的超时时间。单位：分钟。 |
| UpdateTime | String | 2019-08- 01T04:07:39 | 资源栈更新时间。按照ISO8601标准表示，需使用UTC时间，格式：YYYY-MM- DDThh:mm:ss。 |
| PageSize | Integer | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |

| 资源编排 |  |  | 开发指南·API参考 |
|---|---|---|---|

| PageNumber | Integer | 1 | 资源栈列表的页码。 |
|---|---|---|---|
| TotalCount | Integer | 1 | 资源栈总个数。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <Stacks>
        <Stack>
            <StackId>4a6c9851-3b0f-4f5f-b4ca-a14bf691****</StackId>
            <ParentStackId>4a6c9851-3b0f-4f5f-b4ca-a14bf692****</ParentStackId>
            <StackName>StackName</StackName>
            <RegionId>cn-hangzhou</RegionId>
            <DisableRollback>false</DisableRollback>
            <CreateTime>2019-08-01T04:07:39</CreationTime>
            <Status>CREATE_COMPLETE</Status>
            <StatusReason>Stack successfully created</StatusReason>
            <TimeoutInMinutes>10</TimeoutInMinutes>
            <UpdatedTime>2019-08-01T04:07:39</UpdatedTime>
            <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
            <StackDriftStatus>IN_SYNC</StackDriftStatus>
            <StackType>ROS</StackType>
        </Stack>
    </Stacks>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式资源编排

```json
{
    "Stacks": [
        {
            "StackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf691****",
            "ParentStackId": "4a6c9851-3b0f-4f5f-b4ca-a14bf692****",
            "StackName": "MyStack",
            "RegionId": "cn-hangzhou",
            "DisableRollback": false,
            "CreateTime": "2019-08-01T04:07:39",
            "Status": "CREATE_COMPLETE",
            "StatusReason": "Stack successfully created",
            "TimeoutInMinutes": 10,
            "UpdatedTime": "2019-08-01T04:07:39",
            "DriftDetectionTime": "2020-02-27T07:47:47",
      "StackDriftStatus": "IN_SYNC",
            "StackType": "ROS"
        }
```

`],`

```json
    "PageNumber": 1,
    "PageSize": 10,
    "TotalCount": 1,
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

#### PreviewStack

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | PreviewStack | 要执行的操作，取值：PreviewStack。 |
| Parameters.N.Pa rameterKey | String | 是 | InstanceType | 参数的名称。如果未指定参数的名称和值，则ROS将使用模板中指定的默认值。 N的最大值为200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |

资源编排

| Parameters.N.Pa rameterValue | String | 是 | ecs.cm4.6xlarge | 参数值。N的最大值为200。 说明 Parameters为可选参数。 如果需要指定Parameters， 则 Parameters.N.Parameter Key和 Parameters.N.Parameter Value必须同时指定。 |
|---|---|---|---|---|
| RegionId | String | 是 | cn-beijing | 资源栈所属的地域ID。 |
| StackName | String | 是 | MyStack | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| DisableRollback | Boolean | 否 | false | 当创建资源栈失败时，是否禁用回滚策略。取值： true：禁用回滚，即当创建资源栈失败时不进行回滚。 false（默认值）：不禁用回滚，即当创建资源栈失败时进行回滚。 |
| TimeoutInMinute s | Long | 否 | 10 | 创建资源栈的超时时间。 单位：分钟。 默认值：60。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01" } | 模板主体的结构。长度为1~524,288个字节。如果长度较大，则建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免因URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |

资源编排

| StackPolicyURL | String | 否 | oss://ros-stack- policy/demo | 包含资源栈策略的文件的位置。 URL必须指向位于Web服务器（HTTP或HTTPS） 或阿里云OSS存储桶（例如： oss://ros/stack-policy/demo、 oss://ros/stack-policy/demo? RegionId=cn-hangzhou）中的策略，策略文件最大长度为16,384个字节。 如未指定OSS地域，默认与接口参数RegionId相同。 说明您必须指定参数 StackPolicyBody或 StackPolicyURL，但不能同时指定。 URL最大长度为1350个字节。 |
|---|---|---|---|---|
| StackPolicyBody | String | 否 | {"Statement": [{"Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*"}]} | 包含资源栈策略主体的结构，长度为 1~16,384个字节。 说明您必须指定 StackPolicyBody或 StackPolicyURL参数，但不能同时指定。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。该值由客户端生成， 并且必须是全局唯一的。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |
| TemplateURL | String | 否 | oss://ros- template/demo | 包含模板主体的文件的位置。URL必须指向位于HTTP Web服务器（HTTP或 HTTPS）或阿里云OSS存储桶中的模板 （1~524,288个字节）。OSS存储桶的 URL例如oss://ros/template/demo或 oss://ros/template/demo? RegionId=cn-hangzhou。如未指定OSS 地域，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

资源编排

| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6F | 请求ID。 |
|---|---|---|---|
| Stack | Struct |  | 资源栈预览数据。 |
| Description | String | One ECS instance. | 资源栈描述。 |
| DisableRollbac k | Boolean | false | 是否禁用回滚。 |
| Parameters | Array of Parameter |  | 资源栈参数。 |
| ParameterKey | String | SystemDiskCatego ry | 参数的键。 |
| ParameterValu e | String | cloud ssd _ | 参数的值。 |
| RegionId | String | cn-beijing | 资源栈所在地域。 |
| Resources | Array of Resource |  | 资源栈中的资源列表。 |
| Description | String | ECS instance. | 资源描述。 |
| LogicalResour ceId | String | WebServer | 资源逻辑ID。 |

资源编排

| Properties | Map | { "DiskMappings": [ { "Category": "cloud ssd", "Size": _ "20" } ], "SystemDisk Categ _ ory": "cloud ssd", _ "InstanceChargeTy pe": "PostPaid", "AutoRenew": "False", "WillReplace": true, "ImageId": "centos 7", _ "InstanceType": "ecs.g6.large", "AllocatePublicIP": true, "AutoRenewPeriod" : 1, "IoOptimized": "optimized", "ZoneId": "cn- beijing-g", "VSwitchId": "", "SecurityGroupId": "", "Period": 1, "InternetChargeTy pe": "PayByTraffic", "SystemDiskCateg ory": "cloud efficiency", _ "InternetMaxBand widthOut": 1, "VpcId": "", "InternetMaxBand widthIn": 200, "PeriodUnit": "Month" } | 资源属性。 |
|---|---|---|---|
| RequiredBy | List | ["Resource1", "Resource2"] | 被哪些资源依赖。 |
| ResourceType | String | ALIYUN::ECS::Insta nce | 资源类型。 |
| Stack | Map | {} | 子资源栈信息。数据结构同整个返回值。 |
| StackName | String | MyStack | 资源栈名称。 |

资源编排

| StackPolicyBo dy | Map | { "Statement": [ { "Action": "Update:*", "Resource": "*", "Effect": "Allow", "Principal": "*" }, { "Action": "Update:*", "Resource": "LogicalResourceId /apple1", "Effect": "Deny", "Principal": "*" } ] } | 资源栈策略内容。 |
|---|---|---|---|
| TemplateDesc ription | String | One ECS instance. | 模板描述。 |
| TimeoutInMinu tes | Integer | 10 | 超时时间。 单位：分钟。 |

**示例**

请求示例

```
&RegionId=cn-beijing &Parameters.1.ParameterValue=ecs.cm4.6xlarge &Parameters.1.ParameterKey=InstanceType &StackName=MyStack &TimeoutInMinutes=10
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <Stack>
       <Description>No description</Description>
       <DisableRollback>true</DisableRollback>
       <Parameters>
          <ParameterKey>UpdateVersion</ParameterKey>
          <ParameterValue>1</ParameterValue>
       </Parameters>
       <RegionId>cn-beijing</RegionId>
       <Resources>
          <Description></Description>
          <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
          <Properties>
             <Count>-1</Count>
             <Mode>Full</Mode>
             <UpdateVersion>1</UpdateVersion>
          </Properties>
          <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
       </Resources>
       <Resources>
```

资源编排

```xml
          <Description></Description>
          <LogicalResourceId>nested</LogicalResourceId>
          <Properties>
             <Parameters></Parameters>
             <TemplateURL>oss://nested-stack/test/demo</TemplateURL>
             <TimeoutMins>16</TimeoutMins>
          </Properties>
          <ResourceType>ALIYUN::ROS::Stack</ResourceType>
          <Stack>
             <Description>No description</Description>
             <DisableRollback>true</DisableRollback>
             <Parameters>
                <ParameterKey>ALIYUN::AccountId</ParameterKey>
                <ParameterValue>1666666****</ParameterValue>
             </Parameters>
             <Parameters>
                <ParameterKey>ALIYUN::NoValue</ParameterKey>
                <ParameterValue>None</ParameterValue>
             </Parameters>
             <Parameters>
                <ParameterKey>ALIYUN::Region</ParameterKey>
                <ParameterValue>cn-beijing</ParameterValue>
             </Parameters>
             <Parameters>
                <ParameterKey>ALIYUN::StackId</ParameterKey>
                <ParameterValue>None</ParameterValue>
             </Parameters>
             <Parameters>
                <ParameterKey>ALIYUN::StackName</ParameterKey>
                <ParameterValue>test-preview-stack-complex-nested</ParameterValue>
             </Parameters>
             <RegionId>cn-beijing</RegionId>
             <Resources>
                <Description></Description>
                <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
                <Properties>
                   <Count>-1</Count>
                   <Mode>Full</Mode>
                   <UpdateVersion>1</UpdateVersion>
                </Properties>
                <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
             </Resources>
             <StackName>test-preview-stack-complex-nested</StackName>
             <StackPolicyBody>
                <Statement>
                   <Action>Update:*</Action>
                   <Effect>Allow</Effect>
                   <Principal>*</Principal>
                   <Resource>*</Resource>
                </Statement>
                <Statement>
                   <Action>Update:*</Action>
                   <Effect>Deny</Effect>
                   <Principal>*</Principal>
```

资源编排

```xml
                   <Resource>LogicalResourceId/apple1</Resource>
                </Statement>
             </StackPolicyBody>
             <TemplateDescription>No description</TemplateDescription>
             <TimeoutInMinutes>12</TimeoutInMinutes>
          </Stack>
       </Resources>
       <StackName>test-preview-stack-complex</StackName>
       <StackPolicyBody>
          <Statement>
             <Action>Update:*</Action>
             <Effect>Allow</Effect>
             <Principal>*</Principal>
             <Resource>*</Resource>
          </Statement>
          <Statement>
             <Action>Update:*</Action>
             <Effect>Deny</Effect>
             <Principal>*</Principal>
             <Resource>LogicalResourceId/apple1</Resource>
          </Statement>
       </StackPolicyBody>
       <TemplateDescription>No description</TemplateDescription>
       <TimeoutInMinutes>10</TimeoutInMinutes>
    </Stack>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
    "Stack": {
        "Description": "No description",
        "DisableRollback": true,
        "Parameters": [
            {
                "ParameterKey": "UpdateVersion",
                "ParameterValue": "1"
            }
```

`],`

```json
        "RegionId": "cn-beijing",
        "Resources": [
            {
                "Description": "",
                "LogicalResourceId": "WaitConditionHandle",
                "Properties": {
                    "Count": -1,
                    "Mode": "Full",
                    "UpdateVersion": 1
                },
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
            },
            {
```

资源编排

```json
{
                "Description": "",
                "LogicalResourceId": "nested",
                "Properties": {
                    "Parameters": null,
                    "TemplateURL": "oss://nested-stack/test/demo",
                    "TimeoutMins": 16
                },
                "RequiredBy": [],
                "ResourceType": "ALIYUN::ROS::Stack",
                "Stack": {
                    "Description": "No description",
                    "DisableRollback": true,
                    "Parameters": [
                        {
                            "ParameterKey": "ALIYUN::AccountId",
                            "ParameterValue": "1666666****"
                        },
                        {
                            "ParameterKey": "ALIYUN::NoValue",
                            "ParameterValue": "None"
                        },
                        {
                            "ParameterKey": "ALIYUN::Region",
                            "ParameterValue": "cn-beijing"
                        },
                        {
                            "ParameterKey": "ALIYUN::StackId",
                            "ParameterValue": "None"
                        },
                        {
                            "ParameterKey": "ALIYUN::StackName",
                            "ParameterValue": "test-preview-stack-complex-nested"
                        }
```

`],`

```json
                    "RegionId": "cn-beijing",
                    "Resources": [
                        {
                            "Description": "",
                            "LogicalResourceId": "WaitConditionHandle",
                            "Properties": {
                                "Count": -1,
                                "Mode": "Full",
                                "UpdateVersion": 1
                            },
                            "RequiredBy": [],
                            "ResourceType": "ALIYUN::ROS::WaitConditionHandle"
                        }
```

`],`

```json
                    "StackName": "test-preview-stack-complex-nested",
                    "StackPolicyBody": {
                        "Statement": [
                            {
                                "Action": "Update:*",
                                "Effect": "Allow",
```

资源编排

```json
                                "Principal": "*",
                                "Resource": "*"
                            },
                            {
                                "Action": "Update:*",
                                "Effect": "Deny",
                                "Principal": "*",
                                "Resource": "LogicalResourceId/apple1"
                            }
```

]

```json
                    },
                    "TemplateDescription": "No description",
                    "TimeoutInMinutes": 12
                }
            }
```

`],`

```json
        "StackName": "test-preview-stack-complex",
        "StackPolicyBody": {
            "Statement": [
                {
                    "Action": "Update:*",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Resource": "*"
                },
                {
                    "Action": "Update:*",
                    "Effect": "Deny",
                    "Principal": "*",
                    "Resource": "LogicalResourceId/apple1"
                }
```

]

```json
        },
        "TemplateDescription": "No description",
        "TimeoutInMinutes": 10
    },
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | CircularDependency | Circular Dependency Found: {reason}. | 模板包含循环引用。 reason为具体原因。 |
| 400 | InvalidSchema | {reason}. | 模板格式不正确。reason 为具体原因。 |

资源编排

| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 模板包含不正确的资源属性（输出）引用。 resource为资源名，name为属性名。 |
|---|---|---|---|
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 模板资源定义中的字段类型不正确。resource为资源名，section为字段名。 |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 模板包含不正确的引用。 name为引用名，referencer为引用者。 |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | 模板包含无效的字段。 section为字段名。 |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | 模板版本不正确。reason 为具体原因。 |
| 400 | StackValidationFailed | {reason}. | 资源栈校验失败。reason 为具体原因。 |
| 400 | UnknownUserParamet er | The Parameter ({name}) was not defined in template. | 传递的参数在模板中未定义。name为参数名。 |
| 400 | UserParameterMissing | The Parameter {name} was not provided. | 参数在模板中已定义，但未传递值。name为参数名。 |
| 409 | StackExists | The Stack ({name}) already exists. | 同名资源栈已存在。 name为资源栈名称。 |

#### ListStackEvents

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListStackEvents | 要执行的操作，取值： ListStackEvents。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |

资源编排

| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
|---|---|---|---|---|
| Status.N | RepeatL ist | 否 | CREATE IN PRO _ _ GRESS | 资源状态。取值： CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ UPDATE SKIPPED _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| ResourceType.N | RepeatL ist | 否 | ALIYUN::ECS::Ins tance | 资源类型列表。N的最大值为200。 |
| LogicalResourceI d.N | RepeatL ist | 否 | WebServer | 资源逻辑ID，即模板中资源的名称。 |
| PageNumber | Long | 否 | 1 | 事件列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Long | 否 | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Events | Array of Event |  | 事件对象列表。 |
| CreateTime | String | 2019-08- 01T04:07:39 | 创建时间。按照ISO8601标准表示，需使用UTC 时间，格式：YYYY-MM-DDThh:mm:ss。 |
| EventId | String | 0086612d-77cf- 4056-b0b5- ff8e94ad**** | 事件ID。 |

资源编排

| LogicalResour ceId | String | WebServer | 资源逻辑ID，即模板中资源的名称。 |
|---|---|---|---|
| PhysicalResou rceId | String | i- m5e3tfdbinchnexh **** | 实际资源的物理ID。 |
| ResourceType | String | ALIYUN::ECS::Insta nce | 资源类型。 |
| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| StackName | String | StackName | 资源栈名称。 |
| Status | String | CREATE COMPLET _ E | 资源的状态。 |
| StatusReason | String | state changed | 状态原因。 |
| PageNumber | Integer | 1 | 事件列表的页码。 起始值：1。 默认值：1。 |
| PageSize | Integer | 10 | 分页查询时设置的每页行数。 最大值：50。 默认值：10。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
| TotalCount | Integer | 20 | 查询到的事件总数。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=ListStackEvents &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <Events class="array">
              <Event class="object">
<CreationTimetype="string">2019-08-01T05:57:56</CreationTime>
```

资源编排

```xml
                     <CreationTime type
string>20190801T05:57:56</CreationTime>
                     <EventId type="string">0086612d-77cf-4056-b0b5-ff8e94ad****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">test-describe-
events</LogicalResourceId>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">Stack successfully
updated</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">2b900d01-959b-49a8-8cfe-f7de87aa****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:55</CreationTime>
                     <EventId type="string">30f721d4-8124-4fd4-8afd-7b21471f****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:54</CreationTime>
                     <EventId type="string">b5ecc0ac-f855-4503-945c-82d398a2****</EventI
```

`d>`

```xml
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
```

资源编排

```xml
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a01e5730-7244-414e-b9ff-f97e3885****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">CREATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">262b2f54-7ae7-4cf6-9c8a-eb4d0801****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">163c3965-1617-4787-ba08-1eed0e3a****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">71f7c25c-2ac7-4336-9934-85482111****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">4ed7ab13-c912-4239-b064-8cea7caa*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
```

资源编排

```xml
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">a5a0eb9e-7abe-44a1-a376-70955211****</EventI
```

`d>`

```xml
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">state changed</StatusReason>
              </Event>
              <Event class="object">
                     <CreationTime type="string">2019-08-01T05:57:53</CreationTime>
                     <EventId type="string">250f5003-f59d-46f9-8471-65d0c630****</EventI
```

`d>`

```xml
                     <LogicalResourceId type="string">test-describe-
events</LogicalResourceId>
                     <PhysicalResourceId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">57d0946e-c7f4-4f4e-89ae-0d4301a2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-events</StackName>
                     <Status type="string">UPDATE_IN_PROGRESS</Status>
                     <StatusReason type="string">Stack UPDATE started</StatusReason>
              </Event>
       </Events>
       <PageNumber type="number">1</PageNumber>
       <PageSize type="number">10</PageSize>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <TotalCount type="number">20</TotalCount>
```

`JSON` 格式

```json
{
   "Events": [
       {
           "CreationTime": "2019-08-01T05:57:56",
           "EventId": "0086612d-77cf-4056-b0b5-ff8e94ad****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "Stack successfully updated"
       },
       {
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "2b900d01-959b-49a8-8cfe-f7de87aa****",
           "LogicalResourceId": "dummy",
```

资源编排

```
ogca esouced:
```

`du` y,

```json
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:55",
           "EventId": "30f721d4-8124-4fd4-8afd-7b21471f****",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:54",
           "EventId": "b5ecc0ac-f855-4503-945c-82d398a2****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a01e5730-7244-414e-b9ff-f97e3885****",
           "LogicalResourceId": "dummy3",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "CREATE_IN_PROGRESS",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "262b2f54-7ae7-4cf6-9c8a-eb4d0801****",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "163c3965-1617-4787-ba08-1eed0e3a****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
```

资源编排

```json
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "71f7c25c-2ac7-4336-9934-85482111****",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "4ed7ab13-c912-4239-b064-8cea7caa****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "a5a0eb9e-7abe-44a1-a376-70955211****",
           "LogicalResourceId": "WaitConditionHandle",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "state changed"
       },
       {
           "CreationTime": "2019-08-01T05:57:53",
           "EventId": "250f5003-f59d-46f9-8471-65d0c630****",
           "LogicalResourceId": "test-describe-events",
           "PhysicalResourceId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "ResourceType": "ALIYUN::ROS::Stack",
           "StackId": "57d0946e-c7f4-4f4e-89ae-0d4301a2****",
           "StackName": "test-describe-events",
           "Status": "UPDATE_IN_PROGRESS",
           "StatusReason": "Stack UPDATE started"
       }
```

`],`

```json
   "PageNumber": 1,
   "PageSize": 10,
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TotalCount": 20
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |

资源编排

### 资源相关接口

#### GetResourceTypeTemplate

调用GetResourceTypeTemplate接口根据资源类型查询该资源的模板。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetResourceTyp eTemplate | 要执行的操作，取值： GetResourceTypeTemplate。 |
| ResourceType | String | 是 | ALIYUN::ECS::VP C | 资源类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 87F54B2B-AEF0- 4C33-A72A- 3F8856A575E9 | 请求ID。 |
| TemplateBody | Map | {"ROSTemplateFor matVersion": "2015-09-01"} | 模板主体的结构。 长度为1~51,200个字节。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=GetResourceTypeTemplate &ResourceType=ALIYUN::ECS::VPC
```

`&<`公共请求参数> 正常返回示例 `XML` 格式资源编排

```xml
       <RequestId type="string">87F54B2B-AEF0-4C33-A72A-3F8856A575E9</RequestId>
       <TemplateBody class="object">
              <Parameters class="object">
                     <CidrBlock class="object">
                            <Type type="string">String</Type>
                     </CidrBlock>
                     <Description class="object">
                            <Type type="string">String</Type>
                     </Description>
                     <ResourceGroupId class="object">
                            <Type type="string">String</Type>
                     </ResourceGroupId>
                     <VpcName class="object">
                            <Type type="string">String</Type>
                     </VpcName>
              </Parameters>
              <ROSTemplateFormatVersion type="string">2015-09-
01</ROSTemplateFormatVersion>
              <Resources class="object">
                     <Vpc class="object">
                            <Properties class="object">
                                   <CidrBlock class="object">
                                          <Ref type="string">CidrBlock</Ref>
                                   </CidrBlock>
                                   <Description class="object">
                                          <Ref type="string">Description</Ref>
                                   </Description>
                                   <ResourceGroupId class="object">
                                          <Ref type="string">ResourceGroupId</Ref>
                                   </ResourceGroupId>
                                   <VpcName class="object">
                                          <Ref type="string">VpcName</Ref>
                                   </VpcName>
                            </Properties>
                            <Type type="string">ALIYUN::ECS::VPC</Type>
                     </Vpc>
              </Resources>
       </TemplateBody>
```

`JSON` 格式资源编排

```json
{
  "RequestId": "87F54B2B-AEF0-4C33-A72A-3F8856A575E9",
  "TemplateBody": {
    "Parameters": {
      "CidrBlock": {
        "Type": "String"
      },
      "Description": {
        "Type": "String"
      },
      "ResourceGroupId": {
        "Type": "String"
      },
      "VpcName": {
        "Type": "String"
      }
    },
    "ROSTemplateFormatVersion": "2015-09-01",
    "Resources": {
      "Vpc": {
        "Properties": {
          "CidrBlock": {
            "Ref": "CidrBlock"
          },
          "Description": {
            "Ref": "Description"
          },
          "ResourceGroupId": {
            "Ref": "ResourceGroupId"
          },
          "VpcName": {
            "Ref": "VpcName"
          }
        },
        "Type": "ALIYUN::ECS::VPC"
      }
    }
  }
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ResourceTypeNotFoun d | The Resource Type ({name}) could not be found. | 资源类型不存在。name 为资源类型名。 |

#### ListStackResources

资源编排

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListStackResour ces | 要执行的操作，取值： ListStackResources。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
| Resources | Array of Resource |  | 资源对象的列表。 |
| CreateTime | String | 2019-08- 01T06:01:23 | 创建时间，按照ISO8601标准表示，并需要使用 UTC时间。格式为：YYYY-MM- DDThh:mm:ssZ。 |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | 资源栈最近一次成功的偏差检测中资源偏差检测的时间。 |
| LogicalResour ceId | String | dummy | 资源逻辑ID，即模板定义的名称。 |
| PhysicalResou rceId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | 资源的物理ID，即实际资源ID。 |
| ResourceDriftS tatus | String | IN SYNC _ | 资源栈最近一次成功的偏差检测中的资源的偏差状态。取值： DELETED：资源与预期的模板配置不同，因为资源已被删除。 MODIFIED：资源与预期的模板配置不同。 NOT CHECKED：ROS没有检测资源是否与 _ 预期的模板配置不同。 IN SYNC：资源的当前配置与其预期的模板配 _ 置相匹配。 |
| ResourceType | String | ALIYUN::ROS::Stac k | 资源类型。 |

资源编排

| StackId | String | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
|---|---|---|---|
| StackName | String | test-describe- resource | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| Status | String | UPDATE COMPLET _ E | 资源状态。取值： CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ DELETE COMPLETE _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| StatusReason | String | state changed | 资源状态的原因。 |
| UpdateTime | String | 2019-08- 01T06:01:29 | 更新时间，按照ISO8601标准表示，并需要使用 UTC时间。格式为：YYYY-MM- DDThh:mm:ssZ。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=ListStackResources &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
       <Resources class="array">
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">dummy</LogicalResourceId>
```

资源编排

```
ogca esoucedtype
```

`st` g `du`

```xml
y/ogca esouced
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:28</CreationTime>
                     <LogicalResourceId type="string">dummy3</LogicalResourceId>
                     <PhysicalResourceId type="string">a</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::DEBUG::Dummy</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">CREATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId
type="string">WaitConditionHandle</LogicalResourceId>
                     <PhysicalResourceId type="string"></PhysicalResourceId>
                     <ResourceType
type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:29</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
              <Resource class="object">
                     <CreationTime type="string">2019-08-01T06:01:23</CreationTime>
                     <LogicalResourceId type="string">nested</LogicalResourceId>
                     <PhysicalResourceId type="string">d04af923-e6b7-4272-aeaa-47ec9777*
***</PhysicalResourceId>
                     <ResourceType type="string">ALIYUN::ROS::Stack</ResourceType>
                     <StackId type="string">efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackI
```

`d>`

```xml
                     <StackName type="string">test-describe-resource</StackName>
                     <Status type="string">UPDATE_COMPLETE</Status>
                     <StatusReason type="string">state changed</StatusReason>
                     <UpdatedTime type="string">2019-08-01T06:01:28</UpdatedTime>
                     <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
```

资源编排

```xml
                     <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
              </Resource>
       </Resources>
```

`JSON` 格式

```json
{
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "Resources": [
       {
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "dummy",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
       },
       {
           "CreationTime": "2019-08-01T06:01:28",
           "LogicalResourceId": "dummy3",
           "PhysicalResourceId": "a",
           "ResourceType": "ALIYUN::DEBUG::Dummy",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "CREATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
       },
       {
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "WaitConditionHandle",
           "PhysicalResourceId": "",
           "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:29",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
       },
       {
           "CreationTime": "2019-08-01T06:01:23",
           "LogicalResourceId": "nested",
           "PhysicalResourceId": "d04af923-e6b7-4272-aeaa-47ec9777****",
"ResourceType":"ALIYUN::ROS::Stack",
```

资源编排

```json
           ResourceType: ALIYUN::ROS::Stack,
           "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2e0d5",
           "StackName": "test-describe-resource",
           "Status": "UPDATE_COMPLETE",
           "StatusReason": "state changed",
           "UpdatedTime": "2019-08-01T06:01:28",
           "DriftDetectionTime": "2020-02-27T07:47:47",
        "ResourceDriftStatus": "IN_SYNC"
       }
```

]

```
}
```

| 错误代码 | 错误信息 | Http状态码 | 描述 |
|---|---|---|---|
| StackNotFound | The Stack ({name}) could not be found. | 404 | 资源栈不存在，name为资源栈名称或ID。 |

#### GetStackResource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetStackResour ce | 要执行的操作，取值： GetStackResource。 |
| LogicalResourceI d | String | 是 | WebServer | 资源逻辑ID，即模板中资源的名称。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。该值由客户端生成， 并且必须是全局唯一的。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |
| ShowResourceAt tributes | Boolean | 否 | true | 是否查询资源属性。取值： true：查询资源属性。 false：不查询资源属性。 |

**返回数据**

资源编排

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Status | String | CREATE COMPLET _ E | 资源状态。取值： CREATE COMPLETE _ CREATE FAILED _ CREATE IN PROGRESS _ _ UPDATE IN PROGRESS _ _ UPDATE FAILED _ UPDATE COMPLETE _ DELETE IN PROGRESS _ _ DELETE FAILED _ CHECK IN PROGRESS _ _ CHECK FAILED _ CHECK COMPLETE _ IMPORT IN PROGRESS _ _ IMPORT FAILED _ IMPORT COMPLETE _ |
| Description | String | no description | 资源描述。 |
| LogicalResour ceId | String | WebServer | 资源逻辑ID，即模板中资源的名称。 |
| StackId | String | efdf5c10-96a5- 4fd7-ab89- 68e7baa2**** | 资源栈ID。 |
| StackName | String | test-describe- resource | 资源栈名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| StatusReason | String | state changed | 资源状态原因。 |
| PhysicalResou rceId | String | d04af923-e6b7- 4272-aeaa- 47ec9777**** | 资源物理ID，即实际资源ID。 |
| ResourceType | String | ALIYUN::ROS::Wait ConditionHandle | 资源类型。 |
| CreateTime | String | 2019-08- 01T06:01:23 | 创建时间。 按照ISO8601标准表示，需使用UTC时间，格式：YYYY-MM-DDThh:mm:ss。 |
| Metadata | Map | {"key": "value"} | 元数据。 |

资源编排

| UpdateTime | String | 2019-08- 01T06:01:29 | 更新时间。 按照ISO8601标准表示，需使用UTC时间，格式：YYYY-MM-DDThh:mm:ss。 |
|---|---|---|---|
| ResourceAttrib utes | List | [ { "ResourceAttribute Value":"curl -Uri \"http://100.100.XX .XX/waitcondition? stackname=test- describe- resource&stackid= efdf5c10-96a5- 4fd7-ab89- 68e7baa2****&res ource=WaitConditi onHandle&expire= 156468****&signat ure=991d910a901 a89db6580d74233 119960c004****\" - Method Post - Headers @{\"Content- Type\"=\"applicatio n/json\"; \"Accept\"=\"applic ation/json\"; \"x- acs-region- id\"=\"cn- beijing\"}", "ResourceAttribute Key":"PowerShellC urlCli" } ] | 资源属性列表。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
| DriftDetection Time | String | 2020-02- 27T07:47:47 | 资源栈最近一次成功的偏差检测中资源检测的时间。 |
| ResourceDriftS tatus | String | IN SYNC _ | 资源栈最近一次成功的偏差检测中的资源的偏差状态。取值： DELETED：资源与预期的模板配置不同，因为资源已被删除。 MODIFIED：资源与预期的模板配置不同。 NOT CHECKED：ROS没有检测资源是否与 _ 预期的模板配置不同。 IN SYNC：资源的当前配置与其预期的模板配 _ 置相匹配。 |

**示例**

请求示例资源编排

```
http(s)://ros.aliyuncs.com/?Action=GetStackResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <CreateTime>2019-08-01T06:01:23</CreateTime>
    <Description></Description>
    <LogicalResourceId>WaitConditionHandle</LogicalResourceId>
    <Metadata></Metadata>
    <PhysicalResourceId></PhysicalResourceId>
    <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
    <ResourceAttributes>
       <ResourceAttributeKey>CurlCli</ResourceAttributeKey>
       <ResourceAttributeValue>curl -i -X POST -H 'Content-Type: application/json' -H '
Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcondition?stackname=test-describeresource\&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****\&amp;resource=WaitConditionHandle\&amp;expire=156468****\&amp;signature=991d 0a901a89db6580d74233119960c004****</ResourceAttributeValue>
    </ResourceAttributes>
    <ResourceAttributes>
       <ResourceAttributeKey>WindowsCurlCli</ResourceAttributeKey>
       <ResourceAttributeValue>curl -i -X POST -H "Content-Type: application/json" -H "
Accept: application/json" -H "x-acs-region-id: cn-beijing" "http://100.100.XX.XX/waitcondition?stackname=test-describeresource&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&amp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910 01a89db6580d74233119960c004****"</ResourceAttributeValue>
    </ResourceAttributes>
    <ResourceAttributes>
       <ResourceAttributeKey>PowerShellCurlCli</ResourceAttributeKey>
       <ResourceAttributeValue>curl -Uri "http://100.100.XX.XX/waitcondition?
stackname=test-describe-resource&amp;stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&amp;resource=WaitConditionHandle&amp;expire=156468****&amp;signature=991d910 01a89db6580d74233119960c004****" -Method Post -Headers @{"Content- Type"="application/json"; "Accept"="application/json"; "x-acs-region-id"="cn-beijing"}< /ResourceAttributeValue>
    </ResourceAttributes>
    <ResourceType>ALIYUN::ROS::WaitConditionHandle</ResourceType>
    <StackId>efdf5c10-96a5-4fd7-ab89-68e7baa2****</StackId>
    <StackName>test-describe-resource</StackName>
    <Status>UPDATE_COMPLETE</Status>
    <StatusReason>state changed</StatusReason>
    <UpdateTime>2019-08-01T06:01:29</UpdateTime>
    <DriftDetectionTime>2020-02-27T07:47:47</DriftDetectionTime>
    <ResourceDriftStatus>IN_SYNC</ResourceDriftStatus>
```

资源编排 `JSON` 格式

```json
{
    "CreateTime": "2019-08-01T06:01:23",
    "Description": "",
    "LogicalResourceId": "WaitConditionHandle",
    "Metadata": {},
    "PhysicalResourceId": "",
    "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
    "ResourceAttributes": [
        {
            "ResourceAttributeKey": "CurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H 'Content-Type: application/jso
n' -H 'Accept: application/json' -H 'x-acs-region-id: cn-beijing' http://100.100.XX.XX/waitcondition?stackname=test-describe-resource\\&stackid=efdf5c10- 96a5-4fd7-ab89- 68e7baa2****\\&resource=WaitConditionHandle\\&expire=156468****\\&signature=991d910a901a8 b6580d74233119960c004****"
        },
        {
            "ResourceAttributeKey": "WindowsCurlCli",
            "ResourceAttributeValue": "curl -i -X POST -H \"Content-Type: application/js
on\" -H \"Accept: application/json\" -H \"x-acs-region-id: cn-beijing\" \"http://100.100.XX.XX/waitcondition?stackname=test-describe-resource&stackid=efdf5c10- 96a5-4fd7-ab89- 68e7baa2****&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db658 74233119960c004****\""
        },
        {
            "ResourceAttributeKey": "PowerShellCurlCli",
            "ResourceAttributeValue": "curl -Uri \"http://100.100.XX.XX/waitcondition?
stackname=test-describe-resource&stackid=efdf5c10-96a5-4fd7-ab89- 68e7baa2****&resource=WaitConditionHandle&expire=156468****&signature=991d910a901a89db658 74233119960c004****\" -Method Post -Headers @{\"Content-Type\"=\"application/json\"; \" Accept\"=\"application/json\"; \"x-acs-region-id\"=\"cn-beijing\"}"
        }
```

`],`

```json
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "StackId": "efdf5c10-96a5-4fd7-ab89-68e7baa2****",
    "StackName": "test-describe-resource",
    "Status": "UPDATE_COMPLETE",
    "StatusReason": "state changed",
    "UpdateTime": "2019-08-01T06:01:29",
    "DriftDetectionTime": "2020-02-27T07:47:47",
 "ResourceDriftStatus": "IN_SYNC"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|

资源编排

| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | 资源栈中不存某资源。 name为资源名，stack为资源栈名称或ID。 |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |

#### GetResourceType

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetResourceTyp e | 要执行的操作，取值： GetResourceType。 |
| ResourceType | String | 是 | ALIYUN::ROS::W aitConditionHan dle | 资源类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Attributes | Map | {"CurlCli": {},"PowerShellCurl Cli": {},"WindowsCurlCli ": {}} | 资源的返回值。 |
| Properties | Map | {"Count": {},"Mode": {"Constraints": []}} | 资源的属性。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
| ResourceType | String | ALIYUN::ROS::Wait ConditionHandle | 资源类型。 |
| SupportDriftDe tection | Boolean | false | 该资源是否支持偏差检测。取值： true：支持。 false：不支持。 |

**示例**

请求示例资源编排

```
http(s)://ros.aliyuncs.com/?Action=GetResourceType &ResourceType=ALIYUN::SLB::LoadBalancer
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <Attributes class="object">
              <CurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix, which can be used for signalling handle completion or failure. You can signal success by adding --data-binary '{"status": "SUCCESS"}' , or signal failure by a dding --data-binary '{"status": "FAILURE"}'</Description>
              </CurlCli>
              <PowerShellCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix for PowerShell, which can be used for signalling handle completion or fa ilure. As this cmdlet was introduced in PowerShell 3.0, ensure the version of PowerShel l satisfies the constraint. (Show the version via $PSVersionTable.PSVersion.) You can s ignal success by adding -Body '{"status": "SUCCESS"}' , or signal failure by adding -Bo dy '{"status": "FAILURE"}' </Description>
              </PowerShellCurlCli>
              <WindowsCurlCli class="object">
                     <Description type="string">Convenience attribute, provides curl CLI
command prefix for Windows, which can be used for signalling handle completion or failu re. As Windows does not support curl command, you need to install curl.exe and add it t o PATH first. You can signal success by adding --data-binary "{\"status\": \"SUCCESS\"} " , or signal failure by adding --data-binary "{\"status\": \"FAILURE\"}" </Description>
              </WindowsCurlCli>
       </Attributes>
       <Properties class="object">
              <Count class="object">
                     <Default type="number">-1</Default>
                     <Description type="string">There are 3 preconditions that make Coun
t taking effect: 1.Mode is set to Full. 2.Count &gt;= 0. 3.The id of signal is not specified. If so, it will be a self-increasing integer starte d from 1. For example, the id of the first signal is 1, the id of the second signal is 2, and so on. If Count takes effect, signals with id &gt; Count will be deleted before update. The default value is -1, which means no effect. It is recommended to quote the same value with WaitCondition.Count.</Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">integer</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Count>
              <Mode class="object">
                     <Constraints class="array">
```

资源编排

```xml
                            <e class="object">
                                   <AllowedValues class="array">
                                          <e type="string">Increment</e>
                                          <e type="string">Full</e>
                                   </AllowedValues>
                            </e>
                     </Constraints>
                     <Default type="string">Full</Default>
                     <Description type="string">If set to Increment, all old signals wil
l be deleted before update. In this mode, WaitCondition.Count should reference an incre mental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances. If set to Full, no old signal will be deleted unless Count is set. In this mode, WaitCo ndition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Count. Default to Full.</Description>
                     <Immutable type="boolean">false</Immutable>
                     <Required type="boolean">false</Required>
                     <Type type="string">string</Type>
                     <UpdateAllowed type="boolean">true</UpdateAllowed>
              </Mode>
       </Properties>
       <RequestId type="string">BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0</RequestId>
       <ResourceType type="string">ALIYUN::ROS::WaitConditionHandle</ResourceType>
       <SupportDriftDetection type="boolean">false</SupportDriftDetection>
```

`JSON` 格式

```json
{
    "Attributes": {
        "CurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix,
which can be used for signalling handle completion or failure. You can signal success by adding --data-binary '{\"status\": \"SUCCESS\"}' , or signal failure by adding --dat a-binary '{\"status\": \"FAILURE\"}'"
        },
        "PowerShellCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for
PowerShell, which can be used for signalling handle completion or failure. As this cmdl et was introduced in PowerShell 3.0, ensure the version of PowerShell satisfies the con straint. (Show the version via $PSVersionTable.PSVersion.) You can signal success by ad ding -Body '{\"status\": \"SUCCESS\"}' , or signal failure by adding -Body '{\"status\" : \"FAILURE\"}' "
        },
        "WindowsCurlCli": {
            "Description": "Convenience attribute, provides curl CLI command prefix for
Windows, which can be used for signalling handle completion or failure. As Windows does not support curl command, you need to install curl.exe and add it to PATH first. You ca n signal success by adding --data-binary \"{\\\"status\\\": \\\"SUCCESS\\\"}\" , or sig nal failure by adding --data-binary \"{\\\"status\\\": \\\"FAILURE\\\"}\" "
        }
```

资源编排

```json
}
    },
    "Properties": {
        "Count": {
            "Default": -1,
            "Description": "There are 3 preconditions that make Count taking
effect:\n1.Mode is set to Full.\n2.Count >= 0.\n3.The id of signal is not specified. If so, it will be a self-increasing integer started from 1. For example, the id of the fir st signal is 1, the id of the second signal is 2, and so on.\n\nIf Count takes effect, signals with id > Count will be deleted before update.\nThe default value is -1, which means no effect.\nIt is recommended to quote the same value with WaitCondition.Count.",
            "Immutable": false,
            "Required": false,
            "Type": "integer",
            "UpdateAllowed": true
        },
        "Mode": {
            "Constraints": [
                {
                    "AllowedValues": [
                        "Increment",
                        "Full"
```

]

```
                }
```

`],`

```json
            "Default": "Full",
            "Description": "If set to Increment, all old signals will be deleted before
update. In this mode, WaitCondition.Count should reference an incremental value instead of a full value, such as ScalingGroupEnable.ScalingRuleArisExecuteResultNumberOfAddedInstances.\n\nIf set to Ful l, no old signal will be deleted unless Count is set. In this mode, WaitCondition.Count should reference a full value, such as the same value with InstanceGroup.MaxAmount. It is recommended to use this mode with Count.\n\nDefault to Full.",
            "Immutable": false,
            "Required": false,
            "Type": "string",
            "UpdateAllowed": true
        }
    },
    "RequestId": "BA4C8BF3-482E-4B03-A1E3-C60DB7A95DE0",
    "ResourceType": "ALIYUN::ROS::WaitConditionHandle",
    "SupportDriftDetection": false
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ResourceTypeNotFoun d | The Resource Type ({name}) could not be found. | 资源类型不存在。name 为资源类型名。 |

资源编排

### 模板相关接口

#### ValidateTemplate

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ValidateTemplat e | 要执行的操作，取值： ValidateTemplate。 |
| TemplateURL | String | 否 | oss://ros/templat e/demo | 包含模板主体的文件的位置。URL必须指向位于Web服务器（HTTP或HTTPS）或阿里云OSS存储桶（例如： oss://ros/template/demo、 oss://ros/template/demo? RegionId=cn-hangzhou）中的模板，模板最大为524,288个字节。如果OSS地域未指定，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 URL的最大长度为：1024个字节。 |
| RegionId | String | 否 | cn-hangzhou | 资源栈模板所属的地域ID。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01"} | 模板的结构。长度为1~524,288个字节。 如果长度较大，建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Description | String | No description | 描述此资源栈模板的相关信息。 |

资源编排

| Parameters | List | [{"Description": "", "Label": "param integer", _ "NoEcho": "false", "ParameterKey": "param integer", _ "Type": "Number"},{ "Description": "", "Label": "param float", _ "NoEcho": "false", "ParameterKey": "param float", _ "Type": "Number"}] | 输入参数。 输入参数中，定义了通过此模板创建资源栈时需要指定的参数，这些参数用来定制每次资源栈创建的细节，例如：用户名、密码、环境相关的 ECS规格等。 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=ValidateTemplate &TemplateURL=oss://ros/template/demo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
       <Description type="string">No description</Description>
       <Parameters class="array">
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_integer</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_integer</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_float</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_float</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_bool</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_bool</ParameterKey>
                     <Type type="string">Boolean</Type>
              </Parameter>
              <Parameter class="object">
```

资源编排 j

```xml
                     <Description type="string"></Description>
                     <Label type="string">param_json_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_list</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Default class="object">
                            <c class="array"></c>
                     </Default>
                     <Description type="string"></Description>
                     <Label type="string">param_has_default</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_has_default</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">UpdateVersion</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">UpdateVersion</ParameterKey>
                     <Type type="string">Number</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_str</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_str</ParameterKey>
                     <Type type="string">String</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_list</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_list</ParameterKey>
                     <Type type="string">CommaDelimitedList</Type>
              </Parameter>
              <Parameter class="object">
                     <Description type="string"></Description>
                     <Label type="string">param_json_dict</Label>
                     <NoEcho type="string">false</NoEcho>
                     <ParameterKey type="string">param_json_dict</ParameterKey>
                     <Type type="string">Json</Type>
              </Parameter>
       </Parameters>
       <RequestId type="string">B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
   "Description": "No description",
   "Parameters": [
{
```

资源编排

```json
       {
           "Description": "",
           "Label": "param_integer",
           "NoEcho": "false",
           "ParameterKey": "param_integer",
           "Type": "Number"
       },
       {
           "Description": "",
           "Label": "param_float",
           "NoEcho": "false",
           "ParameterKey": "param_float",
           "Type": "Number"
       },
       {
           "Description": "",
           "Label": "param_bool",
           "NoEcho": "false",
           "ParameterKey": "param_bool",
           "Type": "Boolean"
       },
       {
           "Description": "",
           "Label": "param_json_list",
           "NoEcho": "false",
           "ParameterKey": "param_json_list",
           "Type": "Json"
       },
       {
           "Default": {
               "c": []
           },
           "Description": "",
           "Label": "param_has_default",
           "NoEcho": "false",
           "ParameterKey": "param_has_default",
           "Type": "Json"
       },
       {
           "Description": "",
           "Label": "UpdateVersion",
           "NoEcho": "false",
           "ParameterKey": "UpdateVersion",
           "Type": "Number"
       },
       {
           "Description": "",
           "Label": "param_str",
           "NoEcho": "false",
           "ParameterKey": "param_str",
           "Type": "String"
       },
       {
           "Description": "",
"Label":"paramlist",
```

资源编排

```json
           Label: param_list,
           "NoEcho": "false",
           "ParameterKey": "param_list",
           "Type": "CommaDelimitedList"
       },
       {
           "Description": "",
           "Label": "param_json_dict",
           "NoEcho": "false",
           "ParameterKey": "param_json_dict",
           "Type": "Json"
       }
```

`],`

```json
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| 错误代码 | 错误信息 | Http状态码 | 描述 |
|---|---|---|---|
| InvalidTemplate | {reason}. | 400 | 模板不正确，reason为具体原因。 |

#### GetTemplate

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetTemplate | 要执行的操作，取值：GetTemplate。 |
| RegionId | String | 是 | cn-hangzhou | 模板所属资源栈的地域ID。 |
| StackId | String | 否 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| ChangeSetId | String | 否 | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | 更改集ID。 |
| TemplateId | String | 否 | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

资源编排

| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
|---|---|---|---|
| TemplateBody | String | {\"ROSTemplateFo rmatVersion\": \"2015-09-01\"} | 模板的结构。 |

**示例**

请求示例

```
&RegionId=cn-hangzhou
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```json
        <TemplateBody>{"ROSTemplateFormatVersion": "2015-09-01", "Resources":
{"dummy2": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_has_default"}, "List": {"Ref": "param_list"}}}, "dummy": {"Type": "ALIYUN::DEBUG::Dummy", "Properties": {"Map": {"Ref": "param_json_dict"}, "String": {"R ef": "param_str"}, "List": {"Ref": "param_json_list"}, "Number": {"Ref": "param_float"}, "Bool": {"Ref": "param_bool"}, "Integer": {"Ref": "param_integer"}}}, " nested": {"Type": "ALIYUN::ROS::Stack", "Properties": {"TemplateURL": "oss://nested-sta ck/simple/nested_demo", "TimeoutMins": 16}}, "WaitConditionHandle": {"Type": "ALIYUN::R OS::WaitConditionHandle", "Properties": {"UpdateVersion": {"Ref": "UpdateVersion"}}}}, "Parameters": {"param_integer": {"Type": "Number"}, "param_float": {"Type": "Number"}, "param_bool": {"Type": "Boolean"}, "param_json_list": {"Type": "Json"}, "param_has_default": {"Default": "{\"c\": []}", "Type": "Json"}, "UpdateVersion": {"Typ e": "Number"}, "param_str": {"Type": "String"}, "param_list": {"Type": "CommaDelimitedList"}, "param_json_dict": {"Type": "Json"}}, "Outputs": {"param_integer": {"Value": {"Ref": "param_integer"}}, "param_float": {"Value": {"Ref": "param_float"}}, "param_bool": {"Value": {"Ref": "param_bool"}}, "param_json_list": {"V alue": {"Ref": "param_json_list"}}, "param_has_default": {"Value": {"Ref": "param_has_default"}}, "param_str": {"Value": {"Ref": "param_str"}}, "CurlCli": {"Value ": {"Fn::GetAtt": ["WaitConditionHandle", "CurlCli"]}}, "param_list": {"Value": {"Ref": "param_list"}}, "param_json_dict": {"Value": {"Ref": "param_json_dict"}}}} </TemplateBody>
        <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式资源编排

```json
{
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F",
   "TemplateBody": "{\"ROSTemplateFormatVersion\": \"2015-09-01\", \"Resources\": {\"du
mmy2\": {\"Type\": \"ALIYUN::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"para m_has_default\"}, \"List\": {\"Ref\": \"param_list\"}}}, \"dummy\": {\"Type\": \"ALIYUN ::DEBUG::Dummy\", \"Properties\": {\"Map\": {\"Ref\": \"param_json_dict\"}, \"String\": {\"Ref\": \"param_str\"}, \"List\": {\"Ref\": \"param_json_list\"}, \"Number\": {\"Ref\ ": \"param_float\"}, \"Bool\": {\"Ref\": \"param_bool\"}, \"Integer\": {\"Ref\": \"para m_integer\"}}}, \"nested\": {\"Type\": \"ALIYUN::ROS::Stack\", \"Properties\": {\"Templ ateURL\": \"oss://nested-stack/simple/nested_demo\", \"TimeoutMins\": 16}}, \"WaitCondi tionHandle\": {\"Type\": \"ALIYUN::ROS::WaitConditionHandle\", \"Properties\": {\"Updat eVersion\": {\"Ref\": \"UpdateVersion\"}}}}, \"Parameters\": {\"param_integer\": {\"Typ e\": \"Number\"}, \"param_float\": {\"Type\": \"Number\"}, \"param_bool\": {\"Type\": \ "Boolean\"}, \"param_json_list\": {\"Type\": \"Json\"}, \"param_has_default\": {\"Defau lt\": \"{\\\"c\\\": []}\", \"Type\": \"Json\"}, \"UpdateVersion\": {\"Type\": \"Number\"}, \"param_str\": {\"Type\": \"String\"}, \"param_list\": {\"Type\": \"CommaD elimitedList\"}, \"param_json_dict\": {\"Type\": \"Json\"}}, \"Outputs\": {\"param_integer\": {\"Value\": {\"Ref\": \"param_integer\"}}, \"param_float\": {\"Valu e\": {\"Ref\": \"param_float\"}}, \"param_bool\": {\"Value\": {\"Ref\": \"param_bool\"}}, \"param_json_list\": {\"Value\": {\"Ref\": \"param_json_list\"}}, \"p aram_has_default\": {\"Value\": {\"Ref\": \"param_has_default\"}}, \"param_str\": {\"Va lue\": {\"Ref\": \"param_str\"}}, \"CurlCli\": {\"Value\": {\"Fn::GetAtt\": [\"WaitCond itionHandle\", \"CurlCli\"]}}, \"param_list\": {\"Value\": {\"Ref\": \"param_list\"}}, \"param_json_dict\": {\"Value\": {\"Ref\": \"param_json_dict\"}}}}" }
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 模板不存在。ID为模板 ID。 |

#### DeleteTemplate

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DeleteTemplate | 要执行的操作，取值： DeleteTemplate。 |
| TemplateId | String | 是 | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |

资源编排

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | 请求ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=DeleteTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
```

`JSON` 格式

```json
{
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 模板不存在。 |

#### ListTemplates

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListTemplates | 要执行的操作，取值：ListTemplates。 |
| TemplateName | String | 否 | MyTemplate | 模板名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |

资源编排

| PageNumber | Long | 否 | 10 | 模板列表的页码。 起始值：1。 默认值：1。 |
|---|---|---|---|---|
| PageSize | Long | 否 | 1 | 分页查询时设置的每页行数。 取值范围：1~50。 默认值：10。 |
| Tag.N.Key | String | 否 | TestKey | 模板的标签键。N的取值范围：1~20。如果指定该值，则不允许为空字符串。 最多支持128个字符，不能以aliyun和 acs:开头，不能包含http://或者https://。 |
| Tag.N.Value | String | 否 | TestValue | 模板的标签值。N的取值范围：1~20。如果指定该值，可以为空字符串。 最多支持128个字符，不能以aliyun和 acs:开头，不能包含http://或者https://。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | C3A8413B-1F16- 4DED-AC3E- 61A00718DE8A | 请求ID。 |
| PageSize | Integer | 10 | 分页查询时设置的每页行数。 |
| PageNumber | Integer | 1 | 模板列表的页码。 起始值：1。 |
| TotalCount | Integer | 3 | 模板总数。 |
| Templates | Array of Template |  | 模板列表。 |
| CreateTime | String | 2019-10- 15T08:17:14.0000 00 | 创建时间。 |
| Description | String | test-description | 模板描述。 |
| TemplateId | String | 4d4f5aa2-3260- 4e47-863b- 763fbb12**** | 模板ID。 |
| TemplateNam e | String | test-list-templates | 模板名称。 |

资源编排

| UpdateTime | String | 2019-10- 15T08:17:14.0000 00 | 更新时间。 |
|---|---|---|---|

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <RequestId>C3A8413B-1F16-4DED-AC3E-61A00718DE8A</RequestId>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description-update</Description>
       <TemplateId>c8b8bd07-c488-4302-ac15-b88ef073****</TemplateId>
       <TemplateName>test-template-name-update</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:15.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>4d4f5aa2-3260-4e47-863b-763fbb12****</TemplateId>
       <TemplateName>test-list-templates-2</TemplateName>
       <UpdateTime>2019-10-15T08:17:15.000000</UpdateTime>
    </Templates>
    <Templates>
       <CreateTime>2019-10-15T08:17:14.000000</CreateTime>
       <Description>test-description</Description>
       <TemplateId>1e808bb6-c2d1-4196-98a3-3b2cb2a4****</TemplateId>
       <TemplateName>test-list-templates-1</TemplateName>
       <UpdateTime>2019-10-15T08:17:14.000000</UpdateTime>
    </Templates>
    <TotalCount>3</TotalCount>
```

`JSON` 格式资源编排

```json
{
    "PageNumber": 1,
    "PageSize": 10,
    "RequestId": "C3A8413B-1F16-4DED-AC3E-61A00718DE8A",
    "Templates": [
        {
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description-update",
            "TemplateId": "c8b8bd07-c488-4302-ac15-b88ef073****",
            "TemplateName": "test-template-name-update",
            "UpdateTime": "2019-10-15T08:17:15.000000"
        },
        {
            "CreateTime": "2019-10-15T08:17:15.000000",
            "Description": "test-description",
            "TemplateId": "4d4f5aa2-3260-4e47-863b-763fbb12****",
            "TemplateName": "test-list-templates-2",
            "UpdateTime": "2019-10-15T08:17:15.000000"
        },
        {
            "CreateTime": "2019-10-15T08:17:14.000000",
            "Description": "test-description",
            "TemplateId": "1e808bb6-c2d1-4196-98a3-3b2cb2a4****",
            "TemplateName": "test-list-templates-1",
            "UpdateTime": "2019-10-15T08:17:14.000000"
        }
```

`],`

```json
    "TotalCount": 3
}
```

#### CreateTemplate

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | CreateTemplate | 要执行的操作，取值： CreateTemplate。 |
| TemplateName | String | 是 | MyTemplate | 模板的名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |

资源编排

| TemplateURL | String | 否 | oss://ros/templat e/demo | 包含模板主体的文件的位置。URL必须指向位于Web服务器（HTTP或HTTPS）或阿里云OSS存储桶（例如： oss://ros/template/demo、 oss://ros/template/demo? RegionId=cn-hangzhou）中的模板，模板最大为524,288个字节。如果OSS地域未指定，默认与接口参数RegionId相同。 说明您可以指定 TemplateBody或TemplateURL参数，但不能同时指定。 URL的最大长度为：1024个字节。 |
|---|---|---|---|---|
| Description | String | 否 | It is a demo. | 模板的描述。最大长度为256个字符。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01"} | 模板的结构。长度为1~524,288个字节。 如果长度较大，建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | 请求ID。 |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=CreateTemplate &TemplateName=MyTemplate &TemplateURL=oss://ros/template/demo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式资源编排

```xml
          <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
          <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
```

`JSON` 格式

```json
{
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | InvalidSchema | {reason}. | 模板格式不正确。reason 为具体原因。 |
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 模板包含不正确的资源属性（输出）引用。 resource为资源名，name为属性名。 |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 模板资源定义中的字段类型不正确。resource为资源名，section为字段名。 |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 模板包含不正确的引用。 name为引用名，referencer为引用者。 |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | 模板包含无效的字段。 section为字段名。 |
| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | 模板版本不正确。reason 为具体原因。 |

#### UpdateTemplate

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|

资源编排

| Action | String | 是 | UpdateTemplate | 要执行的操作，取值： UpdateTemplate。 |
|---|---|---|---|---|
| TemplateId | String | 是 | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |
| TemplateURL | String | 否 | oss://ros/templat e/demo | 包含模板主体的文件的位置。URL必须指向位于Web服务器（HTTP或HTTPS）或阿里云OSS存储桶（例如： oss://ros/template/demo、 oss://ros/template/demo? RegionId=cn-hangzhou）中的模板，模板最大为524,288个字节。如果OSS地域未指定，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 URL的最大长度为：1024个字节。 |
| TemplateName | String | 否 | MyTemplate | 模板的名称。 长度不超过255个字符，必须以数字或英文字母开头，可包含数字、英文字母、短划线（-）和下划线（ ）。 _ |
| Description | String | 否 | It is a demo. | 模板的描述。最大长度为256个字符。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01"} | 模板的结构。长度为1~524,288个字节。 如果长度较大，建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 8C5D90E1-66B6- 496C-9371- 3807F8DA80A8 | 请求ID。 |
| TemplateId | String | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |

资源编排

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=UpdateTemplate &TemplateId=5ecd1e10-b0e9-4389-a565-e4c15efc**** &TemplateURL=oss://ros/template/demo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>8C5D90E1-66B6-496C-9371-3807F8DA80A8</RequestId>
    <TemplateId>5ecd1e10-b0e9-4389-a565-e4c15efc****</TemplateId>
```

`JSON` 格式

```json
{
    "RequestId": "8C5D90E1-66B6-496C-9371-3807F8DA80A8",
    "TemplateId": "5ecd1e10-b0e9-4389-a565-e4c15efc****"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 模板不存在。 |
| 400 | InvalidSchema | {reason}. | 模板格式不正确。reason 为具体原因。 |
| 400 | InvalidTemplateAttribu te | The Referenced Attribute ({resource} {name}) is incorrect. | 模板包含不正确的资源属性（输出）引用。 resource为资源名，name为属性名。 |
| 400 | InvalidTemplateProper tyType | The specified value type of ({resource} {section}) is incorrect. | 模板资源定义中的字段类型不正确。resource为资源名，section为字段名。 |
| 400 | InvalidTemplateRefere nce | The specified reference "{name}" (in {referencer}) is incorrect. | 模板包含不正确的引用。 name为引用名，referencer为引用者。 |
| 400 | InvalidTemplateSectio n | The template section is invalid: {section}. | 模板包含无效的字段。 section为字段名。 |

资源编排

| 400 | InvalidTemplateVersio n | The template version is invalid: {reason}. | 模板版本不正确。reason 为具体原因。 |
|---|---|---|---|

#### GetTemplateSummary

请求中至少指定StackId、ChangeSetId、TemplateId、TemplateBody或者TemplateURL其中一个参数，以确定查询对象。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GetTemplateSu mmary | 要执行的操作，取值： GetTemplateSummary。 |
| StackId | String | 否 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| TemplateBody | String | 否 | {"ROSTemplate FormatVersion": "2015-09-01"} | 模板的结构。长度为1~524,288个字节。 如果长度较大，建议通过HTTP POST+Body Param的方式，将参数放在请求体中进行传递，避免URL过长而导致请求失败。 说明您必须指定参数 TemplateBody或TemplateURL， 但不能同时指定。 |
| RegionId | String | 否 | cn-hangzhou | 模板所属资源栈的地域ID。 |
| TemplateId | String | 否 | 5ecd1e10-b0e9- 4389-a565- e4c15efc**** | 模板ID。 |
| TemplateURL | String | 否 | oss://ros/templat e/demo | 包含模板主体的文件的位置。URL必须指向位于Web服务器（HTTP或HTTPS）或阿里云OSS存储桶（例如： oss://ros/template/demo、 oss://ros/template/demo? RegionId=cn-hangzhou）中的模板，模板最大为524,288个字节。如果OSS地域未指定，默认与接口参数RegionId相同。 说明您必须指定 TemplateBody或TemplateURL参数，但不能同时指定。 URL的最大长度为：1024个字节。 |

资源编排

| ChangeSetId | String | 否 | 1f6521a4-05af- 4975-afe9- bc4b45ad**** | 更改集ID。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Description | String | No description | 资源栈模板的描述信息。 |
| Metadata | Map | {"key": "value"} | 模板中定义的Metadata。 |
| Parameters | List | [{"Description":"", "Label":"Name", "NoEcho":"false", "ParameterKey":"N ame", "Type":"String"}] | 参数声明的列表。描述参数的属性。 |
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |
| ResourceIdenti fierSummaries | Array of ResourceIdenti fierSummary |  | 资源标识符摘要的列表。 摘要描述了导入操作的目标资源以及在导入过程中可以提供的用于标识目标资源的属性。例如： VpcId是ALIYUN::ECS::VPC资源的标识符属性。 |
| LogicalResour ceIds | List | ["Vpc"] | 模板中类型为ResourceType的所有资源的逻辑 ID。 |
| ResourceIdenti fiers | List | ["VpcId"] | 资源属性。用来标识目标资源。 例如：VpcId是 ALIYUN::ECS::VPC资源的标识符属性。 |
| ResourceType | String | ALIYUN::ECS::VPC | 资源类型。 说明该资源类型支持资源导入。 |
| ResourceType s | List | ["ALIYUN::ECS::VPC "] | 模板中用到的所有资源类型。 |
| Version | String | 2015-09-01 | 模板版本。 |

**示例**

请求示例资源编排

```
http(s)://ros.aliyuncs.com/?Action=GetTemplateSummary &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &RegionId=cn-hangzhou &TemplateURL=oss://ros/template/demo
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <Description>No description</Description>
    <Metadata></Metadata>
    <Parameters>
       <Description>Description of the vpc, [2, 256] characters. Do not fill or empty,
the default is empty.</Description>
       <Label>Description</Label>
       <NoEcho>false</NoEcho>
       <ParameterKey>Description</ParameterKey>
       <Type>String</Type>
    </Parameters>
    <Parameters>
       <Description>Tags to attach to vpc. Max support 20 tags to add during create vpc
. Each tag with two properties Key and Value, and Key is required.</Description>
       <Label>Tags</Label>
       <MaxLength>20</MaxLength>
       <NoEcho>false</NoEcho>
       <ParameterKey>Tags</ParameterKey>
       <Type>Json</Type>
    </Parameters>
    <Parameters>
       <Description>IPv6 network cidr of the VPC.</Description>
       <Label>Ipv6CidrBlock</Label>
       <MinLength>1</MinLength>
       <NoEcho>false</NoEcho>
       <ParameterKey>Ipv6CidrBlock</ParameterKey>
       <Type>String</Type>
    </Parameters>
    <Parameters>
       <AllowedValues>True</AllowedValues>
       <AllowedValues>true</AllowedValues>
       <AllowedValues>False</AllowedValues>
       <AllowedValues>false</AllowedValues>
       <Default>false</Default>
       <Description>Whether to enable an IPv6 network cidr, the value is:False
(default): not turned on.True: On.</Description>
       <Label>EnableIpv6</Label>
       <NoEcho>false</NoEcho>
       <ParameterKey>EnableIpv6</ParameterKey>
       <Type>Boolean</Type>
    </Parameters>
    <Parameters>
       <Description>Resource group id.</Description>
       <Label>ResourceGroupId</Label>
```

资源编排

```xml
       <NoEcho>false</NoEcho>
       <ParameterKey>ResourceGroupId</ParameterKey>
       <Type>String</Type>
    </Parameters>
    <Parameters>
       <Description>Display name of the vpc instance, [2, 128] English or Chinese chara
cters, must start with a letter or Chinese in size, can contain numbers, '_' or '.', '- '</Description>
       <Label>VpcName</Label>
       <NoEcho>false</NoEcho>
       <ParameterKey>VpcName</ParameterKey>
       <Type>String</Type>
    </Parameters>
    <Parameters>
       <Description>
    The IP address range of the VPC in the CIDR block form. You can use the following I
P address ranges and their subnets:
    10.0.0.0/8
    172.16.0.0/12 (Default)
       192.168.0.0/16</Description>
       <Label>CidrBlock</Label>
       <NoEcho>false</NoEcho>
       <ParameterKey>CidrBlock</ParameterKey>
       <Type>String</Type>
    </Parameters>
    <RequestId>FD70598C-3F4B-4E66-9A76-67F2E2D36938</RequestId>
    <ResourceIdentifierSummaries>
       <LogicalResourceIds>Vpc</LogicalResourceIds>
       <ResourceIdentifiers>VpcId</ResourceIdentifiers>
       <ResourceType>ALIYUN::ECS::VPC</ResourceType>
    </ResourceIdentifierSummaries>
    <ResourceTypes>ALIYUN::ECS::VPC</ResourceTypes>
    <Version>2015-09-01</Version>
```

`JSON` 格式

```json
{
    "Description": "No description",
    "Metadata": {},
    "Parameters": [
        {
            "Description": "Description of the vpc, [2, 256] characters. Do not fill or
empty, the default is empty.",
            "Label": "Description",
            "NoEcho": "false",
            "ParameterKey": "Description",
            "Type": "String"
        },
        {
            "Description": "Tags to attach to vpc. Max support 20 tags to add during
create vpc. Each tag with two properties Key and Value, and Key is required.",
            "Label": "Tags",
            "MaxLength": 20,
```

资源编排 a

```
egt
```

: `0,`

```json
            "NoEcho": "false",
            "ParameterKey": "Tags",
            "Type": "Json"
        },
        {
            "Description": "IPv6 network cidr of the VPC.",
            "Label": "Ipv6CidrBlock",
            "MinLength": 1,
            "NoEcho": "false",
            "ParameterKey": "Ipv6CidrBlock",
            "Type": "String"
        },
        {
            "AllowedValues": [
                "True",
                "true",
                "False",
                "false"
```

`],`

```json
            "Default": false,
            "Description": "Whether to enable an IPv6 network cidr, the value is:False
(default): not turned on.True: On.",
            "Label": "EnableIpv6",
            "NoEcho": "false",
            "ParameterKey": "EnableIpv6",
            "Type": "Boolean"
        },
        {
            "Description": "Resource group id.",
            "Label": "ResourceGroupId",
            "NoEcho": "false",
            "ParameterKey": "ResourceGroupId",
            "Type": "String"
        },
        {
            "Description": "Display name of the vpc instance, [2, 128] English or
Chinese characters, must start with a letter or Chinese in size, can contain numbers, ' _' or '.', '-'",
            "Label": "VpcName",
            "NoEcho": "false",
            "ParameterKey": "VpcName",
            "Type": "String"
        },
        {
            "Description": "The IP address range of the VPC in the CIDR block form. You
can use the following IP address ranges and their subnets:\n10.0.0.0/8\n172.16.0.0/12 ( Default)\n192.168.0.0/16",
            "Label": "CidrBlock",
            "NoEcho": "false",
            "ParameterKey": "CidrBlock",
            "Type": "String"
        }
```

`],`

```json
    "RequestId": "FD70598C-3F4B-4E66-9A76-67F2E2D36938",
```

资源编排

```json
    "ResourceIdentifierSummaries": [
        {
            "LogicalResourceIds": [
                "Vpc"
```

`],`

```json
            "ResourceIdentifiers": [
                "VpcId"
```

`],`

```json
            "ResourceType": "ALIYUN::ECS::VPC"
        }
```

`],`

```json
    "ResourceTypes": [
        "ALIYUN::ECS::VPC"
```

`],`

```json
    "Version": "2015-09-01"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 400 | StackValidationFailed | {reason}. | 资源栈校验失败。reason 为具体原因。 |
| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
| 404 | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 模板不存在。ID为模板 ID。 |

### 其他接口

#### DescribeRegions

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeRegions | 要执行的操作，取值： DescribeRegions。 |
| AcceptLanguage | String | 否 | zh-CN | 根据汉语、英语和日语筛选返回结果。 取值： zh-CN（默认值） en-US ja |

资源编排

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| Regions | Array of Region |  | 地域信息集合。 |
| LocalName | String | 华东1（杭州） | 可用地域本地语言名。 |
| RegionEndpoin t | String | ros.aliyuncs.com | 地域访问地址。 |
| RegionId | String | cn-hangzhou | 地域ID。 |
| RequestId | String | 59F0F0A0-A637- 4292-9B91- 251EF5010913 | 请求ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=DescribeRegions
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <Regions>
        <Region>
            <RegionId>cn-qingdao</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华北 1</LocalName>
        </Region>
        <Region>
            <RegionId>cn-beijing</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华北 2</LocalName>
        </Region>
        <Region>
            <RegionId>cn-zhangjiakou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华北 3</LocalName>
        </Region>
        <Region>
            <RegionId>cn-huhehaote</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华北 5</LocalName>
        </Region>
        <Region>
            <RegionId>cn-hangzhou</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

华东资源编排

```xml
            <LocalName>华东 1</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shanghai</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华东 2</LocalName>
        </Region>
        <Region>
            <RegionId>cn-shenzhen</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>华南 1</LocalName>
        </Region>
        <Region>
            <RegionId>cn-chengdu</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`西南1（成都）`</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-northeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太东北 `1 (`东京`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-southeast-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太东南 `1 (`新加坡`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-southeast-2</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太东南 `2 (`悉尼`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-southeast-3</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太东南 `3 (`吉隆坡`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-southeast-5</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太东南 `5 (`雅加达`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>ap-south-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`亚太南部 `1 (`孟买`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>us-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`美国东部 `1 (`弗吉尼亚`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>us-west-1</RegionId>
```

`<R` i Ed

```
it>
```

`li`

```
</R
```

i Ed

```
it>
```

资源编排

```xml
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`美国西部 `1 (`硅谷`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>eu-west-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
            <LocalName>英国 (伦敦)</LocalName>
        </Region>
        <Region>
            <RegionId>me-east-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`中东东部 `1 (`迪拜`)</LocalName>`

```xml
        </Region>
        <Region>
            <RegionId>eu-central-1</RegionId>
            <RegionEndpoint>ros.aliyuncs.com</RegionEndpoint>
```

`<LocalName>`欧洲中部 `1 (`法兰克福`)</LocalName>`

```xml
        </Region>
    </Regions>
    <RequestId>59F0F0A0-A637-4292-9B91-251EF5010913</RequestId>
```

`JSON` 格式

```json
{
    "Regions": [
        {
            "LocalName": "华北 1",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-qingdao"
        },
        {
            "LocalName": "华北 2",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-beijing"
        },
        {
            "LocalName": "华北 3",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-zhangjiakou"
        },
        {
            "LocalName": "华北 5",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-huhehaote"
        },
        {
            "LocalName": "华东 1",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-hangzhou"
        },
        {
            "LocalName": "华东 2",
            "RegionEndpoint": "ros.aliyuncs.com",
```

资源编排

```json
            "RegionId": "cn-shanghai"
        },
        {
            "LocalName": "华南 1",
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-shenzhen"
        },
        {
```

`"LocalName": "`西南1（成都）`",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "cn-chengdu"
        },
        {
```

`"LocalName": "`亚太东北 `1 (`东京`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-northeast-1"
        },
        {
```

`"LocalName": "`亚太东南 `1 (`新加坡`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-1"
        },
        {
```

`"LocalName": "`亚太东南 `2 (`悉尼`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-2"
        },
        {
```

`"LocalName": "`亚太东南 `3 (`吉隆坡`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-3"
        },
        {
```

`"LocalName": "`亚太东南 `5 (`雅加达`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-southeast-5"
        },
        {
```

`"LocalName": "`亚太南部 `1 (`孟买`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "ap-south-1"
        },
        {
```

`"LocalName": "`美国东部 `1 (`弗吉尼亚`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-east-1"
        },
        {
```

`"LocalName": "`美国西部 `1 (`硅谷`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "us-west-1"
        },
        {
```

`"LocalName": "`英国 (伦敦`)",` 资源编排

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-west-1"
        },
        {
```

`"LocalName": "`中东东部 `1 (`迪拜`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "me-east-1"
        },
        {
```

`"LocalName": "`欧洲中部 `1 (`法兰克福`)",`

```json
            "RegionEndpoint": "ros.aliyuncs.com",
            "RegionId": "eu-central-1"
        }
```

`],`

```json
    "RequestId": "59F0F0A0-A637-4292-9B91-251EF5010913"
}
```

#### SignalResource

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | SignalResource | 要执行的操作，取值：SignalResource。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| LogicalResourceI d | String | 是 | WebServer | 资源逻辑ID，即模板中资源的名称。 |
| Status | String | 是 | SUCCESS | 信号的状态。故障信号会导致无法创建或更新资源栈，如果所有信号都是警告信号，则将无法创建或更新资源栈。取值： SUCCESS FAILURE WARNING |
| UniqueId | String | 是 | 27c7347b-352a- 4377-accf- 63d361c1**** | 信号的唯一ID。长度为1~64个字符。如果向单个资源发送多个信号（例如：发信号通知等待条件），则每个信号都需要不同的信息ID。 |

资源编排

| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。 该值由客户端生成， 并且必须是全局唯一的。 长度最大为64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | B288A0BE-D927- 4888-B0F7- B35EF84B6E6 | 请求ID。 |

**示例**

请求示例

```
http(s)://ros.aliyuncs.com/?Action=SignalResource &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691**** &LogicalResourceId=WebServer &Status=SUCCESS &UniqueId=27c7347b-352a-4377-accf-63d361c1****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
      <RequestId>B288A0BE-D927-4888-B0F7-B35EF84B6E6F</RequestId>
```

`JSON` 格式

```json
{
   "RequestId": "B288A0BE-D927-4888-B0F7-B35EF84B6E6F"
}
```

| HttpCode | 错误码 | 错误信息 | 描述 |
|---|---|---|---|
| 404 | ResourceNotAvailable | The Resource ({name}) is not available. | 资源处于不可用状态。 name为资源名。 |
| 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | 资源栈中不存某资源。 name为资源名，stack为资源栈名称或ID。 |

资源编排

| 404 | StackNotFound | The Stack ({name}) could not be found. | 资源栈不存在。name为资源栈名称或ID。 |
|---|---|---|---|

#### ListStackOperationRisks

调用ListStackOperationRisks接口检测删除资源栈操作可能涉及的高风险资源，并返回每个资源对应的风险原因。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListStackOperati onRisks | 要执行的操作，取值： ListStackOperationRisks。 |
| OperationType | String | 是 | DeleteStack | 需检测的操作类型。取值为 DeleteStack，表示检测删除资源栈操作涉及的高风险资源。 |
| RegionId | String | 是 | cn-hangzhou | 资源栈所属的地域ID。 |
| StackId | String | 是 | 4a6c9851-3b0f- 4f5f-b4ca- a14bf691**** | 资源栈ID。 |
| ClientToken | String | 否 | 123e4567-e89b- 12d3-a456- 42665544**** | 保证请求的幂等性。该值由客户端生成， 并且必须是全局唯一的。 长度不超过64个字符，可包含英文字母、 数字、短划线（-）和下划线（ ）。 _ |
| RamRoleName | String | 否 | test-role | RAM角色名称。 如果指定RAM角色，ROS将根据RAM角色的权限创建资源栈，使用角色的凭证代表用户进行接口调用。 如果不指定RAM角色，ROS将使用当前账号相关权限创建资源栈。 RAM角色名称最大长度为64个字节。 |
| RetainAllResourc es | Boolean | 否 | false | 是否保留该资源栈下的所有资源。取值： true：保留。 false（默认值）：不保留。 说明当OperationType取值为DeleteStack时该参数有效。 |

资源编排

| RetainResources .N | RepeatL ist | 否 | WebServer | 需要保留资源的列表。 说明当OperationType取值为DeleteStack时该参数有效。 |
|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 72108E7A-E874- 4A5E-B22C- A61E94AD12CD | 请求ID。 |
| RiskResources | Array of Resource |  | 风险信息。 |
| Code | String | NoPermission | 对资源进行风险检测失败时的错误码，风险检测正常时不返回该参数。 |
| LogicalResour ceId | String | MySG | 资源逻辑ID，即模板定义的资源名称。 |
| Message | String | You are not authorized to complete this action. | 对资源进行风险检测失败时的错误信息，风险检测正常时不返回该参数。 |
| PhysicalResou rceId | String | sg- bp1dpioafqphedg9 **** | 资源物理ID，即实际的资源ID。 |
| Reason | String | There are some ECS instances (i- bp18el96s4wq635 e****) depending on the security group. | 风险原因。 |
| RequestId | String | DF4296CF-F45F- 4845-A72B- BE617601DB25 | 对资源进行风险检测失败时的请求ID，风险检测正常时不返回该参数。 |
| ResourceType | String | ALIYUN::ECS::Secur ityGroup | 资源类型。 |
| RiskType | String | Referenced | 风险类型，取值： Referenced：当前资源被其他资源引用。 MaybeReferenced：当前资源可能被其他资源引用。 AdditionalRiskCheckRequired：嵌套资源栈需要额外进行风险检测。 |

**示例**

资源编排请求示例

```
http(s)://ros.aliyuncs.com/?Action=ListStackOperationRisks &RegionId=cn-hangzhou &StackId=4a6c9851-3b0f-4f5f-b4ca-a14bf691****
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
    <RequestId>72108E7A-E874-4A5E-B22C-A61E94AD12CD</RequestId>
    <RiskResources>
       <LogicalResourceId>MySG</LogicalResourceId>
       <PhysicalResourceId>sg-bp1dpioafqphedg9****</PhysicalResourceId>
       <ResourceType>ALIYUN::ECS::SecurityGroup</ResourceType>
       <Reason>There are some ECS instances (i-bp18el96s4wq635e****) depending on the s
ecurity group.</Reason>
       <RiskType>Referenced</RiskType>
    </RiskResources>
```

`JSON` 格式

```json
{
  "RequestId": "772108E7A-E874-4A5E-B22C-A61E94AD12CD",
  "RiskResources": [
    {
      "LogicalResourceId": "MySG",
      "PhysicalResourceId": "sg-bp1dpioafqphedg9****",
      "ResourceType": "ALIYUN::ECS::SecurityGroup",
      "Reason": "There are some ECS instances (i-bp18el96s4wq635e****) depending on the
security group.",
      "RiskType": "Referenced"
    }
```

]

```
}
```

资源编排

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

资源编排

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Policy | String | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resourc e": ["*"]}],"Version":" 1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 长度为1~1024个字符。 |

**返回结果**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | 无 | 无 | 访问凭证。 |
| AccessKeyId | String | STS.L4aBSCSJVMuK g5U1**** | 访问密钥ID。 |
| AccessKeySecret | String | ****************************************** | 访问密钥。 |
| SecurityToken | String | ******** | 安全令牌。 |
| Expiration | String | 2015-04- 09T11:52:19Z | 失效时间。 |
| AssumedRoleUser | 无 | 无 | 角色扮演时的临时身份。 |
| Arn | String | acs:ram::12345678 9012****:role/admi nrole/alice | 临时身份的ARN。 |
| AssumedRoleId | String | 34458433936495** **:alice | 临时身份的ID。 |

**示例**

**引入Pom依赖**

资源编排操作需要依赖阿里云核心库来实现，在Pom中引入阿里云核心库包的操作如下:

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

t 资源编排

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

下列代码以调用ECS的 `DescribeZones` 接口为示例。 资源编排

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

资源编排

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
