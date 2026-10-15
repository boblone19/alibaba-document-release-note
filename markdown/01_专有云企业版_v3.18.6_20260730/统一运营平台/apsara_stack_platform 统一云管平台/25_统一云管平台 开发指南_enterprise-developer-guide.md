---
title: "统一云管平台 统一云管平台 开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 603
source_pdf: "25_统一云管平台 开发指南_enterprise-developer-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/apsara_stack_platform/zh/enterprise-developer-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 统一云管平台 统一云管平台 开发指南

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
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API。为了使您拥有与公有云一致的体验，自飞天企业版v3.16起，专有云API默认使用POP网关方式调用。

**流程图**

**调用步骤**

1. 获取API信息。
获取实际调用时所需的产品名称、API名称和API版本信息，具体方式参见获取API信息及其Endpoint。
2. 获取AccessKey或STS AccessKey，具体方式参见获取AccessKey或STS AccessKey。

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台接口。
3. 获取Header参数，具体方式参见获取公共Header参数。

**说明**

调用Apsara Uni-manager运营控制台的API时可以不使用Header参数 `x-acs-organizationid` 、 `x-acs-resourcegroupid` 、 `x-acs-instanceid` 。
4. 获取Apsara Uni-manager运营控制台的Endpoint，具体方式参见获取统一云管平台的Endpoint。
5. 获取Apsara Uni-manager运营控制台的SDK包。
Apsara Uni-manager运营控制台的SDK包可在阿里云开发工具包中获取，其中的SDK核心库即为所需的SDK包。
6. 调用Apsara Uni-manager运营控制台的API。

## 准备工作

### 获取API信息及其Endpoint

在通过SDK调用API接口时需要填写API接口的相关信息，包括产品名称（code）、开放API接口名称、API版本。

**背景信息**

Apsara Uni-manager运营控制台开发者门户中的API信息仅供调用参考，具体API的使用方式需要参见云产品的开发指南。如果发生不一致情况，以开发指南支持情况为准。

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择目标云产品。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取云产品的POP Endpoint信息。

### 获取AccessKey或STS AccessKey

AccessKey支持RAM和STS两种授权模式，在发起调用时选择使用其中一种AccessKey即可。

**背景信息**

AccessKey通过使用AccessKey ID和AccessKey Secret对称加密，实现验证某个请求发送者的身份的功能。其中AccessKey ID用于标识用户，AccessKey Secret是用户用于加密签名的字符串。 AccessKey的两种授权模式如下： 通过RAM授权给第三方请求者的AccessKey ID和AccessKey Secret。 通过STS授权给第三方请求者的AccessKey ID、AccessKey Secret和Security Token。 Apsara Uni-manager运营控制台提供了个人AccessKey和组织AccessKey。推荐使用个人账号AccessKey调用Apsara Uni-manager运营控制台及云产品相关接口。

**说明**

只有运营管理员和一级组织管理员可以获取组织AccessKey。

**获取个人账号AccessKey**

使用个人账号AccessKey，需要在Header中添加以下限制性参数，否则可能提示权限不足：

| 参数名称 | 描述 |
|---|---|
| x-acs-regionid | 实际操作的实例资源所属的地域ID，如：cn-qingdao-****-****。 |
| x-acs-organizationid | 实际操作的实例资源所属的组织ID，可参考获取公共Header参数中的获取组织ID获取。 |
| x-acs-resourcegroupid | 实际操作的实例资源所属的资源集ID，可参考获取公共Header参数中的获取资源集ID获取。 |
| x-acs-instanceid | 实际操作的实例资源的实例ID。例如，ECS的实例ID可以从ECS列表中查询到。 |

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
3. 在**AccessKey**区域，您可以查看个人账户的AccessKey信息。

**说明**

Accesskey ID和AccessKey Secret是您访问云资源时的密钥，具有该账号完整的权限，请您妥善保管。

**获取组织AccessKey**

**警告**

个人账号AccessKey是由Apsara Uni-manager运营控制台权限体系管控的受限AccessKey，组织AccessKey相对权限较大，需要管理员确认操作的安全性。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，单击**企业**。
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在组织结构中，单击目标一级组织名称。
5. 单击**管理****Accesskey**。
6. 在弹出的对话框中，查看组织AccessKey信息。

**获取STS Accesskey**

阿里云临时安全令牌STS（Security Token Service）是阿里云提供的一种临时访问权限管理服务。STS AccessKey由AccessKey ID、AccessKey Secret及 SecurityToken三元组组成，使用STS方式调用云产品API时，三元组缺一不可。
1. 获取用户角色的RAM Role。
i. 登录Apsara Uni-manager运营控制台。 ii. 单击页面右上角的用户头像，单击个人信息。 iii. 单击查看当前角色策略。 iv. 在当前选择角色策略对话框中查看RAM Role。
2. 获取STS的Endpoint。
i. 登录飞天基础运维控制台。 ii. 在飞天基础运维平台左侧导航栏中，单击**产品集群运维**。 iii. 在**产品** | **集群**搜索框中搜索**ascm-A**。 iv. 单击集群**操作**列的**集群详情** v. 在集群详情页面，单击**终态配置**页签。

|  | internet-domain |
|---|---|
| region |  |

```
值替换 ${global:internet-domain} 。
```

**说明**

最终STS Endpoint中，${global:}不保留。
3. 通过调用STS的AssumeRole接口来获取三元组信息，以下为Java的STS SDK调用示例。

**说明**

以下代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <yourRoleSessionName> 、 <yourRoleArn> 、 <sts.aliyuns.com> 均为可
```

变参数，需要替换为其实际值。尖括号（<>）在最终代码中不保留。

```
public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。 `//` 请替换为您实际的地域`ID`、`AccessKey ID`、`AccessKey Secret`。

```
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccessKeySecret>");
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
    // "sts.aliyuns.com" 请替换为实际的STS Endpoint，一般格式为sts-vpc.${global:region}.${global:internet-domain}。
    request.setSysDomain("<sts.aliyuns.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
```

`//` 角色会话名称。该参数为用户自定义参数。通常设置为调用该`API`的用户身份，例如：用户名。`"<yourRoleSessionName>"`请您替换为您自定义的值。

```
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
```

`//` 扮演的`RAM Role`的`ARN`。该角色是可信实体为`ASCM`用户的`RAM`角色。`"<yourRoleArn>"`请替换为第一步获取到的实际`RAM Role`。

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

4. 获取STS AccessKey三元组后，您就可以使用三元组信息调用云产品API接口。以下Java SDK示例以DescribeZones接口为例，使用STS AccessKey调用ECS产品接
口。

| 说明以下代码示例中 <yourRegionID> 、 <yourStsAccesskeyID> 、 <yourStsAccessKeySecret> 、 <yourStsToken> 、 <yourResourceGroupID> 、 <yourOrganizationID> 为可变参数，需要替换为其实际值。尖括号（<>）在最终代码中不保留。 |  |  |
|---|---|---|
|  | <yourOrganizationID> |  |

```
public static void main(String[] args) {
```

`// "<yourRegionID>"`请替换为实际操作的实例资源所属的地域`ID`。 `// "<yourStsAccessKeyID>", "<yourStsAccessKeySecret>"`请替换为前一步获取到的`STS`三元组中`AccessKeyID`、`AccessKeySecret`。

```
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<yourStsAccessSecret>");
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

`//"<yourRegionID>"` 请替换为实际操作的实例资源所属的地域`ID`。

```
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
```

`// "<yourStsToken>"` 请替换为您前一步获取到的`STS`三元组中`SecurityToken`。

```
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
```

`//` 非必填,请替换为实际操作的实例资源所属的资源集`ID`。

```
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

`//` 必填,请替换为实际操作的实例资源所属的组织`ID`。

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

调用专有云API时需要填写多个公共请求Header参数，在返回结果中也会包含公共返回参数。

**公共请求参数**

在专有云API调用的代码中需要指定这些公共请求参数的参数值。 例如：在Java SDK调用中的 `request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>")` ，需要将 `<yourResourceGroupID>` 替换为您获取到的实际的资源集ID。

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 实际操作的实例资源所属的地域ID，获取方式请参见获取Region ID。 |
| x-acs-organizationid | 实际操作的实例资源所属的组织ID，获取方式请参见获取组织ID。 |
| x-acs-organization-uuid | 实际操作的实例资源所属的组织UUID，获取方式请参见获取组织UUID |
| x-acs-resourcegroupid | 实际操作的实例资源所属的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-resourcegroup-uuid | 实际操作的实例资源所属的资源集UUID，获取方式请参见获取资源集UUID。 |
| x-acs-roleid | 实际操作的角色ID，获取方式请参见获取角色ID。 |
| x-acs-role-uuid | 实际操作的角色UUID，获取方式请参见获取角色UUID。 |
| x-acs-instanceid | 实际操作的实例资源的实例ID，获取方式请参见获取实例ID。 |

**说明**

公共请求参数中组织、资源集、角色可以传id(1、2、3...)或uuid（org-xxx、rs-xxx、ar-xxx）。id和uuid同时传入时，uuid的优先级高于id，如果uuid不存在，会直接报错。

|  | x-acs-organization-uuid |  |
|---|---|---|
| x-acs-resourcegroupid | 或 | x-acs-resourcegroup-uuid |

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
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调用成功后查看**调用结果**中**id**的信息，即为组织ID。接口信息详

**获取组织UUID**

您可以在Apsara Uni-manager运营控制台中查看资源所属的组织UUID。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**
3. 在左侧导航栏中，选择**资源管理** > **组织管理**。
4. 在左侧组织结构，单击组织名称。
5. 在右侧的基本信息区域，查看**组织****ID**，即为组织UUID。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源集ID。接口信息详见ListResourceGroup。

**获取资源集UUID**

您可以在Apsara Uni-manager运营控制台中查看资源所属的资源集UUID。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**
3. 在左侧导航栏中，选择**资源管理** > **资源集管理**。
4. 在资源集列表，查看资源集ID，即为资源集UUID。

**获取角色ID**

1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListRoles` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为角色ID。接口信息详见ListRoles。

**获取角色UUID**

您可以在Apsara Uni-manager运营控制台中查看角色UUID。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏中，单击**企业**
3. 在左侧导航栏中，选择**权限管理** > **角色授权**。
4. 在角色列表，查看角色的ID，即为角色UUID。

**获取实例ID**

实例ID可以通过Apsara Uni-manager运营控制台中的云产品实例列表进行获取。以ECS产品为例，您可以在云服务器ECS产品控制台的实例列表中查看实例ID信息。
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏，选择**产品** > **计算** > **云服务器** >**云服务器****ECS**。
3. 在左侧导航栏，单击**实例与镜像** > **ECS****实例**。
4. 在实例列表中查看**实例名称****/ID**。

**公共返回参数**

在调用列表类的云产品资源实例接口时，在返回结果中默认包含以下公共返回参数。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |

| ResourceGroup | 资源集ID。 |
|---|---|
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

## 通过POP网关调用专有云API

### 获取统一云管平台的Endpoint

统一云管平台的Endpoint可依照配置格式在飞天基础运维平台中获得对应变量值来自行拼装，也可以在飞天基础运维平台中搜索获取。

**背景信息**

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。您可以在阿里云驻场运维工程师处获取。您也可以通过如下方法自行获取Endpoint。

**方法一：自行拼装Endpoint**

您可以根据统一云管平台Endpoint的配置格式，获取对应变量值来自行拼装Endpoint。 统一云管平台中心Region Endpoint的配置格式： ascm.${global:internet-domain} 统一云管平台单元Region Endpoint的配置格式： ascm.${global:region}.${global:internet-domain}

**说明**

${global:internet-domain} 和 ${global:region} 为变量，需要替换为您获取到的实际值。最终Endpoint中， ${global:} 不保留。

**获取变量值的操作步骤**

1. 登录Apsara-Uni manager运维控制台。
2. 在顶部菜单栏，选择**平台运维** > **飞天基础运维平台** > **资源管理**，默认进入**产品集群运维**页面。
3. 在**产品集群运维**页面的**产品** | **集群**文本框中输入 `ascm-A` ，找到ascm-A-xxx集群，单击操作列的**集群详情**。
4. 在**集群详情**页面，选择**终态配置**页签。
5. 在左侧文件列表中，单击**kv.conf**，单击右侧文件内容，按Ctrl+F键分别搜索 `region` 和 `internet-domain` 。
获取到的 `region` 值将替换 ${global:region} ， `internet-domain` 值将替换 ${global:internet-domain} 。

**方法二：通过飞天基础运维平台获取**

**操作步骤**

1. 在飞天基础运维平台**产品集群运维**页面的**产品** | **集群**文本框中输入 `ascm-A` ，找到ascm-A-xxx集群，单击操作列的**集群详情**。
2. 在服务列表页面搜索 `ascm-brm` 服务，单击下方列表中操作列的**详情**。
3. 在服务详情页面单击**Manage#**组件，在组件信息中选择**资源列表**页签。
4. 搜索名为 `ascm-aliyun-com-dns` 的资源，单击下方**资源申请参数**列中的信息，查看**domain**值，即ASCM的Endpoint。

**方法三：通过开发者门户获取**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成** > **API****调试**。
4. 在左侧导航栏中选择**统一云管平台**。
5. 在**版本**下拉列表中，选择目标API版本。
6. 在下方API列表中可浏览当前版本的所有API接口。
7. 选中对应接口，在参数名下获取POP Endpoint信息。

### 获取统一云管平台的SDK包

**操作步骤**

1. 登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，单击**API****集成** > **API****调试**。
4. 单击页面左上方
，选择**统一云管平台**。
5. 选择版本。
6. 选择目标接口。
7. 在接口的**SDK****示例**页签，查看SDK信息。切换Java、Python、Go语言，可获取对应语言的SDK信息。

**说明**

Common版指泛化调用，支持调试。Common版的依赖通过**查看依赖文件**进行查看，此依赖可以在公开的中央仓库进行下载。 选择高级版后，支持查看发布报告，在发布报告中您可以查看SDK版本、SDK API列表、可用性说明等信息，高级版暂不支持调试。高级版则不会透出到公开的仓库，需要下载完整工程。 如果SDK类型置灰，不支持选择，则表示产品不支持高级版或没有数据。 在对应语言下，你还可以执行**下载完整工程**、**查看依赖文件**、**复制**操作。

### Java SDK调用

安装阿里云Java SDK后，您可以编写代码使用阿里云Java SDK访问阿里云POP网关，调用统一云管平台的API接口。

**前提条件**

已获取AccessKey或STS Accesskey，获取方式请参见获取AccessKey或STS AccessKey。 已获取统一云管平台的Endpoint，获取方式请参见获取统一云管平台的Endpoint。 已安装1.8及以上版本的JDK。

**安装Java SDK**

在项目目录下的pom.xml文件中，添加阿里云Java SDK核心库。

```xml
<!-- https://mvnrepository.com/artifact/com.aliyun/aliyun-java-sdk-core --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.30</version>
</dependency>
```

**说明**

建议您前往**开发者门户** > **API****集成** > **API****调试**页面获取SDK包最新版本依赖，详细操作请参见获取统一云管平台的SDK包。

**设置身份验证**

使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。Java SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。

```
    "<yourSecurityToken>"
```

`//`在使用`STS AccessKey`进行身份验证时，`<yourSecurityToken>`请替换为您实际的`SecurityToken`。 `//`在使用`AccessKey`进行身份验证时，`<yourSecurityToken>`为`null`。

```
);
```

**说明**

以上代码示例中 `<yourRegionID>` 、 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。 `//` 获取`HttpClientConfig`对象。

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault();
```

`//` 设置是否忽略证书。`true`：忽略；`false`：不忽略。

```
clientConfig.setIgnoreSSLCerts(true);
```

`//` （可选）设置创建连接超时时间，单位毫秒（`ms`）。

```
clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);
```

`//` （可选）设置读取超时时间，单位毫秒（`ms`）。

```
clientConfig.setReadTimeoutMillis(<readTimeout>);
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。若需要设置代理，请替换为您实际的代理`IP+`端口。

```
clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```
profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile);
```

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 `//` 创建`API`请求并设置参数。

```
CommonRequest request = new CommonRequest();
```

`//` 统一云管平台接口信息参数。

```
request.setSysProduct("ascm"); request.setSysVersion("2019-05-10"); request.setSysUriPattern("<yourCallUriPattern>");
```

`//` 统一云管平台的`Endpoint`地址。

```
request.setSysDomain("<ascmEndpoint>");
```

`//` 设置请求方式。

```
request.setSysMethod(MethodType.POST);
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 接口业务参数设置。

```
...
```

`//` 设置`Content-Type`。

```
request.setHttpContentType(FormatType.JSON);
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 代码示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | CommonRequest request = new CommonRequest(); request.setSysUriPattern("/clusters/[ClusterId]"); request.putPathParameter("ClusterId", "clusterId01"); |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | CommonRequest request = new CommonRequest(); request.putQueryParameter("ClusterId", "clusterId01"); request.putQueryParameter("ClusterName", "clusterName01"); |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | key-value形式设置Body参数，并设置HttpContentType。 CommonRequest request = new CommonRequest(); request.putBodyParameter("ClusterId", "clusterId01"); request.putBodyParameter("ClusterName", "clusterName01"); // 若Content-Type设置为application/x-www-form-urlencoded，请求到服务器的Content 数据格式为"ClusterId=clusterId01&ClusterName=clusterName01"的字符串。 request.setHttpContentType(FormatType.FORM); // 或，若Content-Type设置为application/json，请求到服务器的Content数据格式为" {\"ClusterId\":\"clusterId01\",\"ClusterName\":\"clusterName01\"}"的JSON串。 request.setHttpContentType(FormatType.JSON); 自行构造HTTP Content并直接设置HttpContent。 CommonRequest request = new CommonRequest(); //设置application/json格式的HTTP Content。 String body = "{\"ClusterId\": \"clusterId01\", \"ClusterName\": \"clusterName01\"}"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.JSON); //设置application/x-www-form-urlencoded格式的HTTP Content。 String body = "ClusterId=clusterId01&ClusterName=clusterName01"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.FORM); |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | CommonRequest request = new CommonRequest(); request.putHeadParameter("x-acs-organizationid", "3"); request.putHeadParameter("x-acs-resourcegroupid", "2"); |

**发起调用并处理应答**

可参考以下代码发起请求并处理返回结果。

```
try {
```

`//` 发起请求，并获取返回。

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
```

**错误处理**

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Java SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    AcsResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`。

```
    // ...
}catch (ServerException e){
```

`//` 这里可以添加您自己的错误处理逻辑。 `//` 例如，打印具体的错误信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`//` 如果遇上棘手问题，可联系阿里云技术支持，并提供`RequestID`。

```java
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
```

`//` 这里可以添加您自己的错误处理逻辑。 `//` 例如，打印具体的错误信息。

```java
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
}
```

**完整调用示例**

以下代码为通过统一云管平台的 `GetOrganizationList` 接口获取组织列表的调用示例。

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Demo {
    /**
```

* 本文提供的`API`调用样例仅供参考，更多详细`API`调用方法可参照开发文档中的“快速入门”。
`*/`

```
    public static void main(String[] args) {
```

`//` 创建`DefaultAcsClient`实例并初始化。

```
        DefaultProfile profile = DefaultProfile.getProfile(
```

`"<yourRegionID>", //` 请替换为您实际的地域`ID`。 `"<yourAccessKeyID>", //` 请替换为您实际的`AccessKeyID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKeySecret`。

```
                null);
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
```

请根据实际情况判断是否需要设置`HTTP`代理，设置方法如下。请替换为您实际代理`IP+`端口。

```
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`*/` `//` 设置连接超时，单位：`ms`。

```
        // clientConfig.setConnectionTimeoutMillis(1000L);
```

`//` 设置读取超时，单位：`ms`。

```
        // clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
```

`//` 创建`API`请求并设置参数。

```
        CommonRequest request = new CommonRequest();
```

`//` 统一云管平台接口信息参数。

```
        request.setSysProduct("ascm");
        request.setSysVersion("2019-05-10");
        request.setSysUriPattern("/ascm/auth/organization/queryList");
```

`//` 统一云管平台的`Endpoint`地址。

```
        request.setSysDomain("<ascmEndpoint>");
```

`//` 设置请求方式。

```
        request.setSysMethod(MethodType.POST);
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-organizationid`、`x-acs-resourcegroupid`、`x-acs-instanceid`。详情可参 `//` 接口业务参数设置。

```
        request.putBodyParameter("id","1");
        request.setHttpContentType(FormatType.JSON);
        try {
```

`//` 发起请求，并获取返回。

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

**说明**

以上代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <http://192.168.XX.XX:33XX> 、 <ascmEndpoint> 、 <yourCallerSdkSource> 均
```

为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### Python SDK调用

安装阿里云Python SDK，您就可以编写代码使用阿里云Python SDK访问专有云POP网关，调用Apsara Uni-manager运营控制台的API接口。

**前提条件**

已获取AccessKey或STS AccessKey，获取方式请参见获取AccessKey或STS AccessKey。 已获取Apsara Uni-manager运营控制台的Endpoint，获取方式请参见获取统一云管平台的Endpoint。

**安装Python SDK及依赖包**

**安装Python SDK**

阿里云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，您可以通过pip安装阿里云Python SDK。

**说明**

推荐使用python3.x。 Python 3.x执行：
#安装阿里云`SDK`核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

Python 2.x执行：
#安装阿里云`SDK`核心库。

```
pip install aliyun-python-sdk-core
```

**导入依赖包**

执行以下代码，导入Python SDK的依赖包。

```
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential
```

**设置身份验证**

Python SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
credentials = StsTokenCredential(
```

`'<yourAccessKeyID>', #` 请替换为您实际的`AccessKey ID`。 `'<yourAccessKeySecret>', #` 请替换为您实际的`AccessKey Secret`。

```
    '<yourSecurityToken>'
```

#使用`STS AccessKey`进行身份验证时，`<yourSecurityToken>`请替换为您实际的`SecurityToken`。
#使用`AccessKey`进行身份验证时，`<yourSecurityToken>`为`None`。
)

**说明**

以上代码示例中 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

```
client = AcsClient(region_id='<your-region-id>',
                   credential=credentials,
```

# （可选）设置创建连接超时时间，单位毫秒（`ms`）。

```
                   connect_timeout=<connectionTimeout>,
```

# （可选）设置读取超时时间，单位毫秒（`ms`）。

```
                   read_timeout=<readTimeout>,
```

# （可选）请根据实际情况判断是否设置代理，设置方法如下：

```bash
                   # proxy={
                   #     "http":"<http://192.168.XX.XX:33XX>",
                   #     "https":"<http://192.168.XX.XX:33XX>"
                   # }
```

)

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。
# 创建`API`请求并设置参数。

```
request = CommonRequest()
```

# 产品接口信息参数。

```
request.set_product("ascm") request.set_version('2019-05-10') request.set_uri_pattern("<yourCallUriPattern>")
```

# Apsara Uni-manager运营控制台的`Endpoint`地址。

```
request.set_domain('<ascmEndpoint>')
```

# 设置请求方式。

```
request.set_method('POST')
```

# 设置请求协议类型：`HTTP/HTTPS`。

```
request.set_protocol_type('https')
```

# 设置`Headers`。
# 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.add_header("x-acs-caller-sdk-source", "<yourCallerSdkSource>")
```

# 接口业务参数设置。

```
...
```

# 设置`Content-Type`。

```
request.set_content_type('application/json')
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | request = CommonRequest() request.set_uri_pattern("/clusters/[ClusterId]") request.add_path_param("ClusterId", "clusterId01") |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | request = CommonRequest() request.add_query_param("ClusterId", "clusterId01"); request.add_query_param("ClusterName", ""); |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | key-value形式设置Body参数，并设置HttpContentType。 request = CommonRequest() request.add_body_params("ClusterId", "clusterId01"); request.add_body_params("ClusterName", "clusterName01"); // 若Content-Type设置为application/x-www-form-urlencoded，请求数据格式为"ClusterId=clusterId01&ClusterName=clusterName01"的字符串。 request.set_content_type("application/x-www-form-urlencoded"); // 或，若Content-Type设置为application/json，请求数据格式为" {\"ClusterId\":\"clusterId01\",\"ClusterName\":\"clusterName01\"}"的JSON串。 request.set_content_type("application/json"); 自行构造请求HTTP Content并设置。 request = CommonRequest() //设置application/json格式的HTTP Content。 body = '''{"ClusterId": "clusterId01", "ClusterName": "clusterName01"}'''; request.set_content(body.encode("utf-8")); request.set_content_type("application/json"); //设置application/x-www-form-urlencoded格式的HTTP Content。 body = '''ClusterId=clusterId01&ClusterName=clusterName01'''; request.set_content(body.encode("utf-8")); request.set_content_type("application/x-www-form-urlencoded"); |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | request = CommonRequest() request.add_header("x-acs-organizationid", "3") request.add_header("x-acs-resourcegroupid", "2") |

**发起调用并处理返回**

# 发起请求，并获取返回。

```python
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

**错误处理**

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，您不需要对Python SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access keey is not found.
```

如果您需要对SDK的错误进行处理，可以参考如下示例编写代码：

```
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
```

# 这里可以添加您自己的错误处理逻辑。
# 例如，打印具体的错误信息。

```
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

**完整调用示例**

| 以下代码为通过ASCM的 | GetOrganizationList | 接口获取组织列表的调用示例。 |
|---|---|---|
| # coding=utf-8 # 导入依赖包。 from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest from aliyunsdkcore.auth.credentials import AccessKeyCredential from aliyunsdkcore.auth.credentials import StsTokenCredential # 本文提供的API调用样例仅供参考，更多详细API调用方法可参照开发文档中的“快速入门”。 credentials = AccessKeyCredential('<yourAccessKeyID>', '<yourAccessKeySecret>') client = AcsClient(region_id='<yourRegionID>', credential=credentials) # 创建API请求并设置参数。 request = CommonRequest() # Apsara Uni-manager运营控制台的接口信息参数。 request.set_product("ascm") request.set_version('2019-05-10') request.set_uri_pattern("/ascm/auth/organization/queryList") # Apsara Uni-manager运营控制台的Endpoint地址。 request.set_domain('<ascmEndpoint>') # 设置请求方式。 request.set_method('POST') # 设置请求协议类型。 request.set_protocol_type('http') # 设置Headers # 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。 request.add_header("x-acs-caller-sdk-source", "<yourCallerSdkSource>") # 调用专有云API时，一般需要提供多个公共Header参数，包括：x-acs-regionid、x-acs-organizationid、x-acs-resourcegroupid、x-acs-instanceid。详情可参照开发指南中的“获取公共Header参数"。 # 接口业务参数设置。 request.add_body_params("id", "1") request.set_content_type('application/json') # 发起请求，并获取返回。 response = client.do_action_with_exception(request) # python2: print(response) print(str(response, encoding='utf-8')) |  |  |

**说明**

以上代码示例中 `<yourRegionID>` 、 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

### Go SDK调用

安装阿里云Go SDK后，您可以编写代码使用阿里云Go SDK访问阿里云POP网关，调用Apsara Uni-manager运营控制台的API接口。

**前提条件**

已获取AccessKey或STS AccessKey，获取方式请参见获取AccessKey或STS AccessKey。 已获取Apsara Uni-manager运营控制台的Endpoint，获取方式请参见获取Apsara Uni-manager运营控制台的Endpoint。

**安装Go SDK**

阿里云Go SDK支持Go 1.10.x及以上版本，您可以通过执行以下命令下载安装Go SDK核心库。

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

若出现网络报错，可尝试使用以下两种方式下载。 使用官方提供的下载方式。

```
GOPROXY=https://goproxy.cn,direct go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

使用代理服务器下载。

```
go env -W GOPROXY='https://goproxy.cn,direct'
```

**设置身份验证**

Go SDK支持通过AccessKey或STS AccessKey进行身份验证。

**重要**

确保包含AccessKey或STS AccessKey的代码不会泄漏（例如提交到外部公开的GitHub项目），否则将会危害您的信息安全。

```
credential := credentials.NewStsTokenCredential(
```

`"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。

```
    "<yourStsToken>",
```

`//` 在使用`STS AccessKey`进行身份验证时，`<yourStsToken>`需替换为您实际的`Security Token`。 `//` 在使用`AccessKey`进行身份验证时，`<yourStsToken>`为`""`。 )

**说明**

以上代码示例中 `<yourAccessKeyID>` 、 `<yourAccessKeySecret>` 、 `<yourSecurityToken>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**创建并配置请求连接**

可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

```
client, err := sdk.NewClientWithOptions("<your-region-id>", sdk.NewConfig(), credential) if err != nil {
    panic(err)
}
```

`//` 设置是否忽略证书。`true`：忽略；`false`：不忽略。

```
client.SetHTTPSInsecure(true)
```

`//`（可选）设置创建连接超时时间，单位纳秒。计算公式为：X秒`*time.Second=X*1000000000`纳秒

```
client.SetConnectTimeout(1 * time.Second)
```

`//` （可选）设置读取超时时间，单位纳秒。计算公式为：X秒`*time.Second=X*1000000000`纳秒

```
client.SetReadTimeout(10 * time.Second)
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。请替换为您实际的代理`IP+`端口。

```
client.SetHttpProxy("<http://192.168.XX.XX:33XX>") client.SetHttpsProxy("<https://192.168.XX.XX:33XX>")
```

`*/`

**说明**

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号 （<>）在最终代码中不保留。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 `//` 创建`API`请求并设置参数。

```
request := requests.NewCommonRequest()
```

`// Apsara Uni-manager`运营控制台接口信息参数。

```
request.Product ="ascm" request.Version = "2019-05-10"
```

`//`被调用接口的`Restful`路径，例如`GetOrganizationList`接口的`Restful`路径为：`/ascm/auth/organization/queryList`。其它接口请查看对应接口文档。

```
request.PathPattern = "<yourCallUriPattern>"
```

`// Apsara Uni-manager`运营控制台的`Endpoint`地址

```
request.Domain = "<ascmEndpoint>"
```

`//` 设置请求方式。

```
request.Method = "POST"
```

`//` 设置协议类型，`https`或`http`。

```
request.Scheme = "https"
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
request.Headers["x-acs-caller-sdk-source"] = "<yourCallerSdkSource>"
```

`//` 接口业务参数设置。

```
...
```

`//` 设置`Content-Type`。

```
request.SetContentType("application/json")
```

**说明**

以上代码示例中 `<yourCallUriPattern>` 、 `<ascmEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要您结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | request := requests.NewCommonRequest() request.PathPattern = "/clusters/[ClusterId]" request.PathParams["ClusterId"] = "clusterId01" |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | request := requests.NewCommonRequest() request.QueryParams["ClusterId"] = "clusterId01" request.QueryParams["ClusterName"] = "clusterName01" |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | 自行构造HTTP Content并直接设置HttpContent。 request := requests.NewCommonRequest() //设置application/json格式的HTTP Content。 body := `{"ClusterId":"clusterId01","ClusterName":"clusterName01"}` request.Content = []byte(body) request.SetContentType(requests.Json) //设置application/x-www-form-urlencoded格式的HTTP Content。 body := `ClusterId=clusterId01&ClusterName=clusterName01` request.Content = []byte(body) request.SetContentType(requests.Form) |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | request := requests.NewCommonRequest() request.Headers["x-acs-organizationid"] = "3" request.Headers["x-acs-resourcegroupid"] = "2" |

**发起调用并处理返回**

可参考以下代码发起请求并处理返回结果。

```
response, err := client.ProcessCommonRequest(request) if err != nil {
   panic(err)
} fmt.Print(response.GetHttpContentString())
```

**错误处理**

阿里云Go SDK在服务端或者SDK端出错时，会返回相应的错误信息，即sdk.errors包下的ClientError和ServerError。这些错误是基于Go的标准Error接口实现的，您可以像处理Go标准错误一样来处理阿里云Go SDK返回的错误。

**简单处理异常**

您可以通过以下代码来简单处理错误。

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
```

`//`获取异常信息

```
   err.Error()
}
```

**ClientError**

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个ClientError，您可以通过以下代码来判断并获取ClientError中的错误信息。

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法可参考以下代码。

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.ProcessCommonRequest(request) if clientError, ok := err.(*errors.ClientError); ok{
```

`//` 获取错误码。

```
    clientError.ErrorCode()
```

`//` 获取错误描述。

```
    clientError.Message()
```

`//` 获取原始错误（可能为`nil`）。

```
    clientError.OriginError()
}
```

**ServerError**

当服务端返回错误的应答时，SDK会将该应答封装成ServerError返回。在这种情况下，您依然可以从Response中获得原始的HTTP应答，，您可以通过以下代码来判断并获取ServerError以及Response中的错误信息。

**重要**

使用具体异常结构时需要引入异常结构包 `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` ，引入方法可参考以下代码。

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`//` 新增的错误包。

```
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

)

```
response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{
```

`//` 获取错误码。

```
    serverError.ErrorCode()
```

`//` 获取错误描述。

```
    serverError.Message()
```

`//` 获取原始`HTTP`应答。

```
    response.GetOriginHttpResponse()
}
```

**完整调用示例**

以下代码为通过ASCM的 `GetOrganizationList` 接口获取组织列表的调用示例。

```java
package main import (
 "fmt"
 "time"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
 credential := credentials.NewStsTokenCredential(
```

`"<yourAccessKeyID>", //` 请替换为您实际的`AccessKey ID`。 `"<yourAccessKeySecret>", //` 请替换为您实际的`AccessKey Secret`。 `"<yourStsToken>", //` 请替换为您实际的`Security Token`（非`STS`调用时为`""`）。 )

```
 client, err := sdk.NewClientWithOptions("<yourRegionID>", sdk.NewConfig(), credential)
 if err != nil {
  panic(err)
 }
```

`//` 设置是否忽略证书。

```
 client.SetHTTPSInsecure(true)
```

`//` （可选）设置创建连接超时时间。

```
 client.SetConnectTimeout(1 * time.Second)
```

`//` （可选）设置读取超时时间。

```
 client.SetReadTimeout(10 * time.Second)
```

`/**` （可选）请根据实际情况判断是否设置代理，设置方法如下。请替换为您实际的代理`IP+`端口。

```
 client.SetHttpProxy("<http://192.168.XX.XX:33XX>")
 client.SetHttpsProxy("<https://192.168.XX.XX:33XX>")
```

`*/`

```
 request := requests.NewCommonRequest()
 request.Product = "ascm"
 request.Version = "2019-05-10"
```

`//`被调用接口的`Restful`路径，例如`GetOrganizationList`接口的`Restful`路径为：`/ascm/auth/organization/queryList`。其它接口请查看对应接口文档。

```
 request.PathPattern = "/ascm/auth/organization/queryList"
 request.Domain = "<ascmEndpoint>"
 request.Method = "POST"
 request.Scheme = "https" // https | http
 request.Headers["Content-Type"] = "application/json"
 request.Headers["x-acs-caller-sdk-source"] = "<yourCallerSdkSource>"
 request.SetContentType("application/json")
 body := `{"id": "1"}`
 request.Content = []byte(body)
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  if clientError, ok := err.(*errors.ClientError); ok {
```

`//` 获取错误码。

```
   fmt.Println(clientError.ErrorCode())
```

`//` 获取错误描述。

```
   fmt.Println(clientError.Message())
```

`//` 获取原始错误（可能为`nil`）。

```
   fmt.Println(clientError.OriginError())
   return
  } else if serverError, ok := err.(*errors.ServerError); ok {
```

`//` 获取错误码。

```
   fmt.Println(serverError.ErrorCode())
```

`//` 获取错误描述。

```
   fmt.Println(serverError.Message())
```

`//` 获取原始`HTTP`应答。

```
   fmt.Println(response.GetOriginHttpResponse())
   return
  } else {
   fmt.Println(err.Error())
   return
  }
 }
 fmt.Print(response.GetHttpContentString())
}
```

**说明**

以上代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <http://192.168.XX.XX:33XX> 、 <ascmEndpoint> 、 <yourCallerSdkSource> 均
```

为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

## ASCM API参考

### API列表

#### 4.1.1. 企业中心

##### 4.1.1.1. 组织管理

###### 4.1.1.1.1. CreateOrganization

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/add HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| name | String | Body | 否 | ascm-test | 组织名称。 说明该参数为必填。 |
| parentId | Integer | Body | 否 | 1 | 父组织ID。可通过调用GetOrganizationList接口获取。 说明 root（根）组织ID为1。 该参数为必填。 |
| orgParentUuid | String | Body | 否 | org- 101bbf866a930ae6******* * | 父组织唯一识别码。 |
| orgUuid | String | Body | 否 | org- 101bbf866a930ae6******* * | 组织UUID，该参数由系统自动生成。 |
| multiCloudStatus | String | Body | 否 | null | 多云状态字段。默认为null。 master：主云。 slave：从云。 null。 说明该字段已经废弃，但是出于兼容性要求，需要保留。 |
| extraInfo | String | Body | 否 | null | 额外信息。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用正常。 400: 组织名不可为空 。 父组织ID不可为空。 所选父组织不存在。 AccessKey不合法。 参数错误。 403: 没有权限。 500: 远程调用错误。 内部错误。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应数据。 |
| alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1606791494471 | 组织的创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| extraInfo | String | null | 附加信息。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1606791494471 | 组织最近一次的修改时间。 说明创建场景下，该参数返回值与创建时间相同。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织修改者的用户名。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 1 | 父组织ID。 说明 root（根）组织的ID为1。 |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | 可用区列表。 说明该参数仅对一级组织有效。若创建一级组织，该参数返回值为中心 RegionID；若创建二级及以下组织，该参数返回为空。 |

| supportRegions | String | cn-qingdao-env17-d01 | 可用区列表。 |
|---|---|---|---|
| uuid | String | 1231 | 组织UUID。 |
| message | String | success | 提示信息。 例如： success：调用成功。 Can't find user by specified accessKey：根据当前AccessKey无法找到用户。 Caller is not the parent of user: xxx：当前用户权限不足。 Calling manage returns empty body：调用信息返回为空。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功 false: 失败 |

**示例**

请求示例

```
POST /ascm/auth/organization/add HTTP/1.1
```

公共请求头

```json
{
    "name": "ascm-test",
    "parentId":1
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>cn-qingdao-****-d01</supportRegions> <mtime>1606791494471</mtime> <uuid>1231</uuid> <parentId>1</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList> <name>test</name> <ctime>1606791494471</ctime> <alias>test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message> |  |

`JSON` 格式

```json
{
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "data": {
        "muserId": "admin",
        "internal": "true",
        "level": "0.1",
        "supportRegions": "cn-qingdao-****-d01",
        "mtime": "1606791494471",
        "uuid": "1231",
        "parentId": "1",
        "multiCloudStatus": "master",
        "supportRegionList": "[\"cn-qingdao-****-d01\"]",
        "name": "test",
        "ctime": "1606791494471",
        "alias": "test",
        "id": "1",
        "cuserId": "admin"
    },
    "success": "true",
    "requestId": "16d09b14-8a59-****-****-7536fe897b66",
    "pureListData": "true",
    "message": "success"
}
```

###### 4.1.1.1.2. GetOrganization

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/query HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 32 | 组织ID。可通过调用GetOrganizationList接口获取。 说明 root（根）组织的ID为1。 |
| orgUuid | String | Body | 否 | org- 101****0b6a70ae6086*** ** | 组织唯一识别码。 说明若组织ID与组织UUID都传，则以组织ID为准。若都不传则返回为空。 |
| requestId | String | Body | 否 | 0a1a****1655458030688 2970d**** | 请求ID。 说明一般不需要填写该参数，默认由系统自动生成。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400：参数错误/查询组织缺少入参。 403：没有权限。 404：用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应数据。 |

| alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
|---|---|---|---|
| ctime | Long | 1606791494471 | 组织的创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| extraInfo | String | null | 外部对接映射组织信息。 |
| id | Integer | 1 | 组织ID。 说明 root（根）组织的ID为1。 |
| internal | Boolean | true | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1607512443989 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master为主云。 slave为从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 1 | 父组织ID。 说明 root（根）组织的ID为1。 |
| supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| uuid | String | 1231 | 组织UUID。 |
| message | String | success | 提示信息。例如： success：调用成功。 MissingParams：缺少入参参数。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |

| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/organization/query HTTP/1.1
```

公共请求头

```json
{
    "id": 32
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>cn-qingdao-****-d01</supportRegions> <mtime>1607512443989</mtime> <uuid>1231</uuid> <parentId>1</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList> <name>test</name> <ctime>1606791494471</ctime> <alias>test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": { "muserId": "admin", "internal": "true", "level": "0.1", "supportRegions": "cn-qingdao-****-d01", "mtime": "1607512443989", "uuid": "1231", "parentId": "1", "multiCloudStatus": "master", "supportRegionList": "[\"cn-qingdao-****-d01\"]", "name": "test", "ctime": "1606791494471", "alias": "test", "id": "1", "cuserId": "admin" }, "success": "true", "requestId": "16d09b14-8a59-****-****-7536fe897b66", "pureListData": "true", "message": "success" } |  |

###### 4.1.1.1.3. GetOrganizationList

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/queryList HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 1 | 组织ID。 说明 root（根）组织的ID为1。 请求参数为ID时，返回入参组织的下级组织列表。 |
| name | String | Body | 否 | test | 组织名称。 说明若组织ID与组织名称都传，则以组织ID为准，返回入参传入组织的下级组织列表。 若仅传组织名称，则以传入组织名为准，返回与之相等的组织信息，不返回下级组织。 若两者都未传，则返回数据为空。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 |
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应结果。 |
| alias | String | test | 组织别名。 |
| ctime | Long | 1606791494471 | 组织的创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| extraInfo | String | null | 外部对接映射组织信息。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | true | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1607512443989 | 组织最近一次修改的时间。 |

| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
|---|---|---|---|
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | test | 组织名称。 说明若请求参数仅输入id，则会返回该参数。 |
| parentId | Integer | 0 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| uuid | String | 1231 | 组织UUID。 |
| message | String | success | 错误提示信息。 调用成功：success。 调用失败: 签名验证失败。 请求输入AccessKey非法或无效。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
| success | Boolean | true | 接口调用是否成功。 true: 成功 false: 失败 |

**示例**

请求示例

```
POST /ascm/auth/organization/queryList HTTP/1.1
```

公共请求头

```json
{
    "id": 1,
    "name": "test"
}
```

正常返回示例 `XML` 格式

```xml
<redirect>true</redirect> <cost>10000</cost> <code>200</code> <data>
    <muserId>admin</muserId>
    <internal>true</internal>
    <level>0.1</level>
    <supportRegions>cn-qingdao-****-d01</supportRegions>
    <mtime>1607512443989</mtime>
    <uuid>1231</uuid>
    <parentId>0</parentId>
    <multiCloudStatus>master</multiCloudStatus>
    <name>test</name>
    <ctime>1606791494471</ctime>
    <alias>test</alias>
    <id>1</id>
    <cuserId>admin</cuserId>
</data> <data>
    <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
</data> <success>true</success> <requestId>1</requestId> <message>200</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": true, "cost": 10000, "code": 200, "data": [ { "muserId": "admin", "internal": true, "level": 0.1, "supportRegions": "cn-qingdao-****-d01", "mtime": 1607512443989, "uuid": 1231, "parentId": 0, "multiCloudStatus": "master", "name": "test", "ctime": 1606791494471, "alias": "test", "id": 1, "cuserId": "admin" }, { "supportRegionList": "[\"cn-qingdao-****-d01\"]" } ], "success": true, "requestId": 1, "message": 200 } |  |

###### 4.1.1.1.4. GetPrivateCloudAccountByOrganizationId

调用GetPrivateCloudAccountByOrganizationId获取一级组织对应的主账号信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/getPrivateCloudAccountByOrganizationId HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| OrganizationId | Integer | Body | 是 | 1 | 组织ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |

| data | Struct |  | 响应结果。 |
|---|---|---|---|
| aliyunid | String | 1 | 主账号ID。 |
| primaryKey | String | 212530506704030466 | 子账号PK。 |
| message | String | success | 提示信息。 |
| pureListData | Boolean | true | 是否只返回数据。 |
| redirect | Boolean | false | 是否重定向。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/getPrivateCloudAccountByOrganizationId HTTP/1.1
```

公共请求头

```json
{ "OrganizationId": "1" }
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <aliyunid>1</aliyunid> <primaryKey>212530506704030466</primaryKey> </data> <success>true</success> <pureListData>true</pureListData> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| {"redirect":"false","cost":"1000","code":"200","data": {"aliyunid":"1","primaryKey":"212530506704030466"},"success":"true","pureListData":"true","message":"success"} |  |

###### 4.1.1.1.5. RemoveOrganization

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/delete HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| orgUuid | String | Body | 否 | org- 101bbf866a930ae6******* * | 组织的UUID。 说明在调用该接口时，至少需要上传一个请求参数。组织UUID 可通过GetOrganization或GetOrganizationList接口获取。 |
| id | String | Body | 否 | 39 | 待删除组织的ID。 说明在调用该接口时，至少需要上传一个请求参数。组织ID可通过GetOrganizationList接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400: 组织ID不可为空。 所选组织不存在。 AccessKey不合法。 参数错误。 阿里云账号不支持此操作。 403: 没有权限。 404: AccessKey不存在。 角色不存在。 用户不存在。 用户没有该角色。 500: 内部错误。 删除资源集前，必须删除资源集下的所有云资源。 删除组织失败，此组织下的人员不为空，请先删除人员。 删除组织失败，此组织下的用户组不为空，请先删除用户组。 删除组织失败，此组织下的角色不为空，请先删除角色。 删除组织失败，此组织下的权限策略不为空，请先删除权限策略。 删除组织失败，此组织下的登录策略不为空，请先删除登录策略。 |
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| message | String | success | 提示信息。 success：调用成功。 Calling manage returns empty body：调用信息返回为空。 CheckResourceEmpty throws exception：该组织下资源集不为空。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 ture：调用成功。 false：调用失败。 |

**示例**

请求示例

```
POST /ascm/auth/organization/delete HTTP/1.1
```

公共请求头

```json
{
    "id": 39
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <pureListData>true</pureListData> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "10000", "code": "200", "success": "true", "requestId": "16d09b14-8a59-****-****-7536fe897b66", "pureListData": "true", "message": "success" } |  |

###### 4.1.1.1.6. UpdateOrganization

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/update HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | String | Body | 否 | 23 | 组织ID。可通过调用GetOrganizationList接口获取。 说明该参数为必填。 |
| name | String | Body | 否 | org-test | 待更新的组织名称。 说明该参数为必填。 |
| orgUuid | String | Body | 否 | org- 101****e53b40ae6086*** *m | 组织的UUID。可通过调用GetOrganization或 GetOrganizationList接口获取。 说明组织UUID不可通过接口修改。 |
| parentId | String | Body | 否 | 1 | 父组织ID。可通过调用GetOrganizationList接口获取。 说明 root（根）组织ID为1。 |
| level | String | Body | 否 | 0.1.3 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| personNum | String | Body | 否 | 10 | 用户数上限，取值为正整数。 说明预留字段，暂未使用。 |
| resourceGroupNum | String | Body | 否 | 10 | 资源集上限，取值为正整数。 说明预留字段，暂未使用。 |
| alias | String | Body | 否 | org-test | 组织别名。系统自动生成，一般与组织名称一致。 |

| multiCloudStatus | String | Body | 否 | null | 多云状态，默认为null。 master：主云。 slaver：从云。 null：非多云。 说明该字段已经废弃，但是出于兼容性要求，需要保留。 |
|---|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400： 组织ID不可为空。 组织名称重复。 参数错误。 创建组织缺少入参。 403：没有权限。 404：用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应结果。 |
| alias | String | org-test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1607512443989 | 组织创建时间。 |
| cuserId | String | 5003 | 组织创建者的用户名。 |
| id | Integer | 1 | 组织ID。 说明 root（根）组织的ID为1。 |
| internal | Boolean | true | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root（根）组织的level=0，其他所有一级组织的level=0.1。其中0.1中的 1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1606791494471 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | org-test | 修改后的组织名称，与入参取值一致。 |

| parentId | Integer | 0 | 父组织ID。 说明 root（根）组织的ID为1。 |
|---|---|---|---|
| supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| uuid | String | 1231 | 组织UUID。 |
| message | String | 200 | 提示信息。例如： OrgNameExist：组织名称已存在，不可重复。 missing uuid or id：入参缺少组织UUID或组织ID。 |
| requestId | String | 1 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/organization/update HTTP/1.1
```

公共请求头

```json
{
    "id": 23,
    "name": "org-test"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <cost>10000</cost> <code>200</code> <data> <muserId>admin</muserId> <internal>true</internal> <level>0.1</level> <supportRegions>cn-qingdao-****-d01</supportRegions> <mtime>1606791494471</mtime> <uuid>1231</uuid> <parentId>0</parentId> <multiCloudStatus>master</multiCloudStatus> <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList> <name>org-test</name> <ctime>1607512443989</ctime> <alias>org-test</alias> <id>1</id> <cuserId>admin</cuserId> </data> <success>true</success> <requestId>1</requestId> <message>200</message> |  |

`JSON` 格式

```json
{
    "cost": 10000,
    "code": 200,
    "data": {
        "muserId": "admin",
        "internal": true,
        "level": 0.1,
        "supportRegions": "cn-qingdao-****-d01",
        "mtime": 1606791494471,
        "uuid": 1231,
        "parentId": 0,
        "multiCloudStatus": "master",
        "supportRegionList": "[\"cn-qingdao-****-d01\"]",
        "name": "org-test",
        "ctime": 1607512443989,
        "alias": "org-test",
        "id": 1,
        "cuserId": "admin"
    },
    "success": true,
    "requestId": 1,
    "message": 200
}
```

###### 4.1.1.1.7. UpdateSupportRegionsForOrg

根据组织更新可用区列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/updateSupportRegionsForOrg HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| supportRegions | String | Body | 否 | RegionId1,RegionId2 | 待更新的RegionID列表，多个RegionID之间以英文半角逗号 （,）隔开。 |
| organizationId | Integer | Body | 否 | 5 | 组织ID。可通过调用GetOrganizationList接口获取。 说明 root（根）组织的ID为1。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400：参数错误/Accesskey已禁用。 403：没有权限。 404：实体不存在/用户不存在/AccessKey不存在。 |
| cost | Integer | 32 | 接口耗时，单位毫秒（ms）。 |
| message | String | success | 提示信息。 例如: Empty securityToken：安全令牌为空。 The ram role mapping is not exist：RAM角色映射不存在。 Can't find user by specified ascm user id: xxx：无法根据当前用户ID找到对应用户。 |
| pureListData | Boolean | false | 是否只返回数据。 falese：只返回数据。 ture：需要返回其他字段。 |
| redirect | Boolean | false | 是否重定向。 |
| success | Boolean | true | 本次请求是否成功。 |

**示例**

请求示例

```
POST null HTTP/1.1
```

公共请求头

```json
{
    "organizationId": 5,
    "supportRegions": "RegionId1,RegionId2"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>32</cost> <code>200</code> <success>true</success> <pureListData>false</pureListData> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "32", "code": "200", "success": "true", "pureListData": "false", "message": "success" } |  |

###### 4.1.1.1.8. CreateAndBindResourceGroup

创建并绑定多云资源集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resource/group/create/bind HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| platformCode | String | Body | 否 | pl-xxxx | 资源池Code。 |
| sourceOrganization Id | Integer | Body | 否 | 100 | 中心云组织ID。 |
| sourceResourceGro upId | Integer | Body | 否 | 100 | 中心云资源集ID。 |
| targetOrganizationI d | String | Body | 否 | 123456 | 目标云组织ID。如果目标云为公共云，则为主账号ID。 |
| name | String | Body | 否 | rs1 | 如果创建的是公共云资源组，需要填写的公共云资源组的名称标识。 |
| resourceGroupNam e | String | Body | 否 | testgroup | 创建的资源集或者资源组显示名称。 |

补充参数信息如下： 参数名称：tagIdList 类型： `List<Integer>` 位置：Body 是否必须：否示例值：[1,2] 说明：创建专有云资源集时的标签ID列表，可选参数，默认不填。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 响应结果。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| -code | String | 200 | 响应码。 |
| -product | String | ascm | 报错产品，默认ascm。 |
| -message | String | error | 错误提示信息。 |
| -requestId | String | 111 | 调用请求的ID。 |
| -errorKey | String | error | 错误类型关键字。 |
| -redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |

**示例**

请求示例

```json
POST /resource/group/create/bind HTTP/1.1 {
  "resourceGroupName": "rsg123",
  "name": "rsg123",
  "sourceOrganizationId": "10",
  "sourceResourceGroupId": "79",
  "platformCode": "pl-xxx",
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "data":{ "redirect":false, "code":"200", "success":true } } |  |

| XML | 格式 |
|---|---|
| <data> <redirect>false</redirect> <code>200</code> <success>true</success> </data> |  |

###### 4.1.1.1.9. GetOrganizationByPrimaryKey

根据组织云账号的UID获取组织信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| primaryKey | String | Query | 否 | 28********71 | 用户UID。 |
| organizationId | String | Query | 否 | 1 | 组织ID，用于指定组织范围。组织ID可通过调用 GetOrganizationList接口获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | ROLERESOURCEUSER _ _ | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 -406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | exampleErrKey | 错误码。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | [{"current": 35,"displayName": "\u8d44\u6e90\u96c6\u7ed1\u5b 9a\u7684\u6700\u5927\u7528\u6 237\u4e2a\u6570","hasDetail": true,"item": "MaxResourceSetBindAscmUserLi mit","quota": 10000,"updateTime": 1692013092000}] | 响应结果：流程回调是否成功。 |
| -id | Integer | 33 | 角色ID。 |
| -name | String | mytest | 组织名称。 |
| -internal | Boolean | false | 是否为预置组织。 预置组织即系统自动生成的组织，也称为默认组织。 |
| -supportRegions | String | cn-qingdao-****-d01 | 可选区列表。 |
| -uuid | String | 1231 | 组织UUID。 |
| -primaryKey | String | 25925866254468**** | RAM用户（子账号）的主键，作为账号的唯一标识。 与在ApsaraUni-manager 运营控制台的用户管理中的RAM用户（子账号）一致。 |
| -aliyunid | String | 192895059480**** | 阿里云用户ID。 |
| -defaultResourceSetId | Integer | 123 | 表示系统中默认的资源集合标识符，用于指定一组预定义的资源集合。 |
| -defaultResourceSetUuid | String | defaultUuid123 | 这是一个示例资源集UUID，用于表示系统中默认的资源集合标识符。 |
| -defaultResourceSetName | String | defaultResources | 默认资源集合名称，用于标识系统或应用中预设的一组资源，如内存、CPU、存储等配置参数。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"exampleErrKey", "code":"ROLE_RESOURCE_USER", "cost":121, "data":{ "aliyunid":"192895059480****", "internal":false, "defaultResourceSetId":123, "defaultResourceSetUuid":"defaultUuid123", "name":"mytest", "supportRegions":"cn-qingdao-****-d01", "defaultResourceSetName":"defaultResources", "id":33, "uuid":"1231", "primaryKey":"25925866254468****" }, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <errorKey>exampleErrKey</errorKey> <code>ROLE_RESOURCE_USER</code> <cost>121</cost> <data> <aliyunid>192895059480****</aliyunid> <internal>false</internal> <defaultResourceSetId>123</defaultResourceSetId> <defaultResourceSetUuid>defaultUuid123</defaultResourceSetUuid> <name>mytest</name> <supportRegions>cn-qingdao-****-d01</supportRegions> <defaultResourceSetName>defaultResources</defaultResourceSetName> <id>33</id> <uuid>1231</uuid> <primaryKey>25925866254468****</primaryKey> </data> <success>true</success> <message>success</message> |  |

##### 4.1.1.2. 资源集管理

###### 4.1.1.2.1. CreateResourceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/create_resource_group HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| organizationid _ | Integer | Body | 否 | 3 | 组织ID。可通过调用GetOrganizationList接口获取。 说明该参数为必填。 |
| resourcegroupname _ _ | String | Body | 否 | testrs | 资源集名称。长度为2-50个字符。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用正常。 400: 资源集名不可为空。 组织ID不可为空。 不能在ROOT组织下创建资源集。 所选组织不存在。 AccessKey不合法。 参数错误。 403: 没有权限。 404: AccessKey不存在。 组织不存在。 用户不存在。 组织AccessKey不存在。 500: 远程调用错误 。 内部错误。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应数据。 |
| creator | String | admin | 资源集创建人的用户名。 |
| gmtCreated | Long | 1607512443989 | 资源集创建时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 1 | 资源集所属组织的ID。 说明 root（根）组织的ID为1。 |
| resourceGroupName | String | test | 资源集名称，取值与入参一致。 |
| rsId | String | rs-1010e71e5e520aab******** | 资源集UUID。 |
| message | String | 200 | 提示信息。例如： Can't find user by specified accessKey：当前AccessKey不存在。 Caller is not the parent of user: xxx：当前用户权限不足。 Calling manage returns empty body：调用信息返回为空。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/create_resource_group HTTP/1.1
```

公共请求头

```json
{
    "organization_id": 3,
    "resource_group_name": "testrs"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <organizationID>1</organizationID> <resourceGroupName>test</resourceGroupName> <gmtCreated>1607512443989</gmtCreated> <rsId>rs-1010e71e5e520aab********</rsId> <id>1</id> </data> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <message>200</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": { "organizationID": "1", "resourceGroupName": "test", "gmtCreated": "1607512443989", "rsId": "rs-1010e71e5e520aab********", "id": "1" }, "success": "true", "requestId": "16d09b14-8a59-****-****-7536fe897b66", "message": "200" } |  |

###### 4.1.1.2.2. GetResourceGroups

批量获取资源集的详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /resourceGroups/action/batchGet HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| idList | RepeatList | Body | 否 | [5,2] | 资源集ID列表 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 资源集列表。 |
| -id | Integer | 2 | 资源集ID。 |
| -rsId | String | 123121a | 资源集唯一编码。 |
| -status | String | ACTIVE | 用户状态。 ACTIVE：激活。 INACTIVE：禁用。 |
| -resourceGroupName | String | restest _ | 资源集名称。 |
| -organizationId | Integer | 3 | 资源集所属组织ID。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -organizationName | String | orgTest | 组织名称。 |
| -resourceGroupType | Integer | 3 | 资源集类型，默认资源集为1，非默认资源集为0。 1：默认资源集 0：非默认资源集 |
| -gmtCreated | Long | 1606791494471 | 资源集创建时间。 |
| -gmtModified | Long | 1703575553000 | 修改时间。 |
| -creator | String | auditor | 资源集创建者的用户名。 |
| -modifier | String | 19xx7043xxxxxxx914 | 修改人。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /resourceGroups/action/batchGet HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "data": [ { "creator": "admin", "gmtCreated": 1754876798335, "gmtModified": 1754876798335, "id": 2, "modifier": "admin", "organizationId": 3, "organizationName": "ascmTest", "resourceGroupName": "ResourceSet(ascmTest)", "resourceGroupType": 1, "rsId": "rs-10336602e6ff0adf04a5000d", "status": "ACTIVE" }, { "creator": "admin", "gmtCreated": 1754893414576, "gmtModified": 1754893433804, "id": 5, "modifier": "admin", "organizationId": 3, "organizationName": "ascmTest", "resourceGroupName": "orgtest", "rsId": "rs-1033670072300adf04a5000e", "status": "ACTIVE" } ], "success": true } |  |

`XML` 格式

```xml
<data>
 <creator>admin</creator>
 <gmtCreated>1754876798335</gmtCreated>
 <gmtModified>1754876798335</gmtModified>
 <id>2</id>
 <modifier>admin</modifier>
 <organizationId>3</organizationId>
 <organizationName>ascmTest</organizationName>
 <resourceGroupName>ResourceSet(ascmTest)</resourceGroupName>
 <resourceGroupType>1</resourceGroupType>
 <rsId>rs-10336602e6ff0adf04a5000d</rsId>
 <status>ACTIVE</status>
</data> <data>
 <creator>admin</creator>
 <gmtCreated>1754893414576</gmtCreated>
 <gmtModified>1754893433804</gmtModified>
 <id>5</id>
 <modifier>admin</modifier>
 <organizationId>3</organizationId>
 <organizationName>ascmTest</organizationName>
 <resourceGroupName>orgtest</resourceGroupName>
 <rsId>rs-1033670072300adf04a5000e</rsId>
 <status>ACTIVE</status>
</data> <success>true</success>
```

###### 4.1.1.2.3. BindAscmUserAndResourceGroup

调用BindAscmUserAndResourceGroup将用户和资源集进行绑定。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/add_ascm_users HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourcegroupid _ _ | Integer | Body | 否 | 7 | 资源集ID，可通过调用ListResourceGroup接口获取。 说明若资源集ID和角色ID都不传或仅传其中一个请求参数的话， 则都返回报错。 |
| ascmuserids _ _ | String | Body | 否 | "[5017,5023]" | 待绑定的用户ID列表，多个用户ID间，以英文半角逗号（,）隔开。用户ID可通过调用ListUsers接口获取。 |
| ascmroleid _ _ | Integer | Body | 否 | 1 | 角色ID，可通过调用ListActiveRoles接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 400： 超过了资源集一次性可以添加的用户数量。 用户加入的资源集数量超过限制。 参数错误。 RAM授权不支持此操作。 403： 没有权限。 当前用户没有操作此资源集的权限。 用户不能对自身做此操作。 404： 资源集不存在。 AccessKey不存在。 用户没有该角色。 用户不存在。 角色不存在。 500：内部错误。 511：超过了每个资源集可以加入的用户数。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 提示信息。例如： success：调用成功。 内部错误。 User and resource set must be in the same top organization：用户和角色必须在同一一级组织下。 invalid ascmRoleId or ascmUserId：无效的角色ID或用户ID。 the role is not exist: xxx：该角色不存在。 |
| pureListData | Integer | 0 | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向该请求。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/add_ascm_users HTTP/1.1
```

公共请求头

```json
{
    "ascm_user_ids": "[5017,5023]",
    "resource_group_id": 7
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

`JSON` 格式

```json
{
    "redirect": "true",
    "cost": "10000",
    "code": "200",
    "success": "true",
    "message": "success"
}
```

###### 4.1.1.2.4. ListAscmUsersInsideResourceGroup

调用ListAscmUsersInsideResourceGroup获取资源集下的用户列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/list_ascm_users HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourceGroupId | Integer | Body | 否 | 7 | 资源集ID，可通过调用ListResourceGroup接口获取，若不传则返回为空。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认值为1。 |
| pageSize | Integer | Body | 否 | 10 | 分页大小。 |
| loginName | String | Body | 否 | admin | 当前用户登录名。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400：参数错误。 403：没有权限。 404： AccessKey不存在. 用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应数据。 |
| accessKeys | Array of accessKey |  | AccessKey。 |
| accesskeyId | String | JGdgSN2p******** | 当前用户的AccessKey ID。 |
| ctime | Long | 1606675230000 | 当前AccessKey的创建时间。 |
| cuserId | String | 1 | 当前AccessKey的创建者ID。 |
| id | Integer | 1 | AccessKey的识别主键。 |
| region | String | cn-qingdao-****-d01 | 当前AccessKey的可用区。 |
| status | String | ACTIVE | AccessKey状态。 active：启用。 deactive：停用。 |
| cellphoneNum | String | 1888888**** | 当前用户的手机号。 |

| default | Boolean | false | 是否为预置用户。 ture：预置用户。 false：非预置用户。 说明预置用户为系统自动创建的用户。 |
|---|---|---|---|
| defaultRole | Struct |  | 角色列表。 |
| active | Boolean | true | 当前角色是否有效。 说明该参数已废弃。 |
| arId | String | 111 | 当前角色的唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | defaultRole.operationAdmin.desc ription | 当前角色的描述。 |
| enable | Boolean | true | 当前角色是否禁用。 ture：已禁用。 false：未禁用。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色创建者的用户名。 |
| organizationVisibility | String | organizationVisibility.global | 共享范围。organizationVisibility.global为全局共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11321 | 角色等级。 说明该参数已废弃。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限。 roleRange.orgAndSubOrgs：本组织及其下级组织。 roleRange.allOrganizations：所有组织。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：预置角色、自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：Ram角色授权。 |
| deleted | Boolean | false | 用户是否删除。 |
| displayName | String | test | 用户的显示名。 |
| email | String | te**@163.com | 用户的邮箱地址。 |
| enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| enableEmail | Boolean | false | 是否启用邮件通知。 |

| enableShortMessage | Boolean | false | 是否启用短信通知。 |
|---|---|---|---|
| id | Integer | 1 | 用户ID。 |
| loginName | String | test | 用户名。 |
| loginPolicy | Struct |  | 登录策略。 |
| cuserId | String | admin | 登录策略创建者的用户名。 |
| default | Boolean | true | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |
| id | Integer | 1 | 登录策略ID。 |
| ipRanges | Array of ipRange |  | 登录策略的IP段。 |
| ipRange | String | 0.0.0.0/0 | IP范围。 |
| loginPolicyId | Integer | 1 | 所属登录策略ID。 |
| protocol | String | IPv4 | 登录策略所使用的协议。 说明目前仅支持IPv4协议。 |
| lpId | String | 111 | 登录策略的唯一编码。 |
| muserId | String | admin | 登录策略创建者的用户名。 |
| name | String | deafult.loginpolicy | 登录策略的名称。 |
| organizationVisibility | String | organizationVisibility.global | 共享范围。 organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rule | String | ALLOW | 策略属性。 Allow：白名单 Deny：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略中登录时间的时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1 | 所属登录策略ID。 |
| startTime | String | 00:00 | 开始时间 |
| mobileNationCode | String | 86 | 国际区号。 |
| organization | Struct |  | 组织信息。 |
| alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1606791494471 | 组织的创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |

| id | Integer | 1 | 用户所在组织的ID。 |
|---|---|---|---|
| internal | Boolean | false | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1606791494472 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织修改者的用户名。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 0 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-env17-d01 | 可用区列表。 |
| uuid | String | 1231 | 组织UUID。 |
| parentPk | String | 1689406703****** | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |
| primaryKey | String | 212530506704****** | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号） 一致。 |
| roles | Array of role |  | 角色列表。 |
| active | Boolean | true | 角色是否有效。 说明该参数已废弃。 |
| arId | String | 111 | 角色的唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| default | Boolean | true | 是否为预置角色。预置角色为系统自动成的角色。 ture：预置角色。 false：非预置角色。 |
| description | String | test | 角色描述。 |

| enable | Boolean | true | 角色是否禁用。 ture：已禁用。 false：未禁用。 |
|---|---|---|---|
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色创建者的用户名。 |
| organizationVisibility | String | organizationVisibility.global | 共享范围。organizationVisibility.global为全局共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11321 | 角色等级。 说明该参数已废弃。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限。 roleRange.orgAndSubOrgs：本组织及其下级组织。 roleRange.allOrganizations：所有组织。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：预置角色、自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：Ram角色授权。 |
| status | String | active | AccessKey的状态。 active：激活。 deactive：禁用。 |
| userGroupRoles | List | admin | 用户组角色列表。 |
| userGroups | List | admin | 用户组列表。 |
| userRoles | Array of userRole |  | 用户角色列表。 |
| active | Boolean | true | 角色是否有效。 说明该参数已废弃。 |
| arId | String | 1121 | 角色的唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| cuserId | String | admin | 角色创建者的用户名。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | roletest _ | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 共享范围。organizationVisibility.global为全局共享。 |

| ownerOrganizationId | Integer | 1 | 角色所属组织的ID。 |
|---|---|---|---|
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 1123 | 角色等级。 说明该参数已废弃。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。至多为64个字符。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限。 roleRange.orgAndSubOrgs：本组织及其下级组织。 roleRange.allOrganizations：所有组织。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：预置角色、自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：Ram角色授权。 |
| message | String | success | 提示信息。 success：调用成功。 User has no permission to access the resource set：用户无权限访问该资源集。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 10 | 总数据量。 |
| totalPage | Integer | 10 | 总页码。 |
| pureListData | Integer | 0 | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 0ba87292-fd63-****-****- c4f975b84cd0 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/list_ascm_users HTTP/1.1
```

公共请求头

```json
{
    "ResourceGroupId": 7
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</r1381380****de>200</code> <cost>49</cost> <data> <cellphoneNum>13813800138</cellphoneNum> d f l l |  |

```xml
    <defaultRole>
        <roleRange>roleRange.resourceSet</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <displayName>baixue1</displayName>
    <enableDingTalk>true</enableDingTalk>
    <roles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <roles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPv4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startT1899999****     <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931******</parentPk>
    <lastLoginTime>1592232390657</lastLoginTime>
    <userRoles>
```

```xml
        <roleRange>roleRange.resourceSet</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_USER</code>
        <active>true</active>
        <description>defaultRole.resourceUser.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <id>2</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        1381381****       <rAMRole>false</rAMRole>
        <code>ROLE_RESOURCE_SET_ADMIN</code>
        <active>true</active>
        <description>defaultRole.resourceSetAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceSetAdmin.name</roleName>
        <id>5</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1591931519000</ctime>
        <id>609</id>
        <region>cn-qingdao-****-d01</region>
        <accesskeyId>1KAjDIqCGM******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>baixue1</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>tets</name>
        <alias>tets</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5617</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>261424091942******</primaryKey>
    <status>ACTIVE</status>
</data> <data>
    <cellphoneNum>18999999999</cellphoneNum>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
```

```xml
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <displayName>test</displayName>
    <enableDingTalk>true</enableDingTalk>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931******</parentPk>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_YUNDUN_ORG_SEC_ADMIN</code>
        <active>true</active>
        <description>defaultRole.yundunOrgSecAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.yundunOrgSecAdmin.name</roleName>
        <id>8</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1591930977000</ctime>
        <id>607</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <accesskeyId>o4LEJ8SoW******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>test</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
<name>test</name>
```

```xml
        <name>test</name>
        <alias>tets</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5615</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>250944791941*****</primaryKey>
    <status>ACTIVE</status>
</data> <data>
    <cellphoneNum>13813813800</cellphoneNum>
    <displayName>baixue</displayName>
    <enableDingTalk>false</enableDingTalk>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1824191931******</parentPk>
    <accessKeys>
        <ctime>1591931388000</ctime>
        <id>608</id>
        <region>cn-qingdao-****-d01</region>
        <accesskeyId>cNaeitV1RB******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>baixue</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <supportRegionList>cn-qingdao-****-d01</supportRegionList>
        <level>0.1</level>
        <name>tets</name>
        <alias>tets</alias>
        <supportRegions>cn-qingdao-****-d01</supportRegions>
        <id>353</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>1</parentId>
    </organization>
    <id>5616</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>false</enableEmail>
    <email>mail@example.com</email>
    <enableShortMessage>false</enableShortMessage>
    <primaryKey>221543391942******</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pageInfo>
    <total>3</total>
    <totalPage>1</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { |  |

```json
    "redirect": false,
    "code": "200",
    "cost": 49,
    "data": [
      {
        "cellphoneNum": "1381381381380****    "defaultRole": {
          "roleRange": "roleRange.resourceSet",
          "muserId": "",
          "rAMRole": false,
          "code": "ROLE_RESOURCE_SET_ADMIN",
          "active": true,
          "description": "defaultRole.resourceSetAdmin.description",
          "roleType": "ROLETYPE_ASCM",
          "default": true,
          "ownerOrganizationId": 1,
          "enable": true,
          "roleName": "defaultRole.resourceSetAdmin.name",
          "id": 5,
          "roleLevel": 2147483647,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
        },
        "displayName": "baixue1",
        "enableDingTalk": true,
        "roles": [
          {
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_SET_ADMIN",
            "active": true,
            "description": "defaultRole.resourceSetAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceSetAdmin.name",
            "id": 5,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
          },
          {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "code": "ROLE_ORGANIZATION_ADMIN",
            "active": true,
            "description": "defaultRole.organizationAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "id": 4,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
          },
          {
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_USER",
            "active": true,
            "description": "defaultRole.resourceUser.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "id": 2,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
          }
```

`],`

```json
        "loginPolicy": {
          "ipRanges": [
            {
              "protocol": "IPv4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
            }
```

`],`

```json
          "muserId": "",
          "default": true,
          "ownerOrganizationId": 1,
          "timeRanges": [
            {
              "loginPolicyId": 1,
              "startTime": "00:00",
"endTime":"24:00"
```

```
              endTime: 24:00
            }
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
        },
        "parentPk": "1824191931******",
        "lastLoginTime": 1592232390657,
        "userGroups": [],
        "userRoles": [
          {
            "roleRange": "roleRange.resourceSet",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_USER",
            "active": true,
            "description": "defaultRole.resourceUser.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "id": 2,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
          },
          {
            "roleRange": "roleRange.orgAndSubOrgs",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_ORGANIZATION_ADMIN",
            "active": true,
            "description": "defaultRole.organizationAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "id": 4,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
          },
          {
            "roleRange": "roleRange.resourceSet",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_RESOURCE_SET_ADMIN",
            "active": true,
            "description": "defaultRole.resourceSetAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceSetAdmin.name",
            "id": 5,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
          }
```

`],`

```json
        "accessKeys": [
          {
            "ctime": 1591931519000,
            "id": 609,
            "region": "cn-qingdao-****-d01",
            "accesskeyId": "1KAjDIqCGM******",
            "status": "ACTIVE"
          }
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "baixue1",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "tets",
"alias" "tets"
```

```json
          "alias": "tets",
          "supportRegions": "cn-qingdao-****-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
        },
        "userGroupRoles": [],
        "id": 5617,
        "mobileNationCode": "86",
        "enableEmail": true,
        "email": "mail@example.com",
        "enableShortMessage": true,
        "primaryKey": "261424091942******",
        "status": "ACTIVE"
      },
      {
        "cellphoneNum": "18999999999",
        "defaultRole": {
          "roleRange": "roleRange.orgAndSubOrgs",
          "muserId": "",
          "rAMRole": false,
          "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
         1899999****true,
          "description": "defaultRole.yundunOrgSecAdmin.description",
          "roleType": "ROLETYPE_ASCM",
          "default": true,
          "ownerOrganizationId": 1,
          "enable": true,
          "roleName": "defaultRole.yundunOrgSecAdmin.name",
          "id": 8,
          "roleLevel": 2147483647,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
        },
        "displayName": "test",
        "enableDingTalk": true,
        "roles": [
          {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
            "active": true,
            "description": "defaultRole.yundunOrgSecAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.yundunOrgSecAdmin.name",
            "id": 8,
            "roleLevel": 2147483647,
            "organizationVisibility": "organizationVisibility.global"
          }
```

`],`

```json
        "loginPolicy": {
          "ipRanges": [
            {
              "protocol": "IPV4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
            }
```

`],`

```json
          "muserId": "",
          "default": true,
          "ownerOrganizationId": 1,
          "timeRanges": [
            {
              "loginPolicyId": 1,
              "startTime": "00:00",
              "endTime": "24:00"
            }
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
        },
        "parentPk": "1824191931******",
        "userGroups": [],
        "userRoles": [
          {
            "roleRange": "roleRange.orgAndSubOrgs",
            "muserId": "",
            "rAMRole": false,
            "code": "ROLE_YUNDUN_ORG_SEC_ADMIN",
```

```json
            "active": true,
            "description": "defaultRole.yundunOrgSecAdmin.description",
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.yundunOrgSecAdmin.name",
            "id": 8,
            "roleLevel": 2147483647,
            "cuserId": "",
            "organizationVisibility": "organizationVisibility.global"
          }
```

`],`

```json
        "accessKeys": [
          {
            "ctime": 1591930977000,
            "id": 607,
            "region": "cn-qingdao-****-d01",
            "cuserId": "admin",
            "accesskeyId": "o4LEJ8SoW******",
            "status": "ACTIVE"
          }
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "test",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "tets",
          "alias": "tets",
          "supportRegions": "cn-qingdao-****-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
        },
        "userGroupRoles": [],
        "id": 5615,
        "mobileNationCode": "86",
        "enableEmail": true,
        "email": "mail@example.com",
        "enableShortMessage": true,
        "primaryKey": "250944791941*****",
        "status": "ACTIVE"
      },
      {
        "cellphoneNum": "13813813800",
        "displayName": "baixue",
        "enableDingTalk": false,
        "loginPolicy": {
          "ipRanges": [
            {
              "protocol": "IPV4",
              "ipRange": "0.0.0.0/0",
              "loginPolicyId": 1
            }
```

`],`

```json
          "muserId": "",
          "default": true,
1381381****ownerOrganizationId": 1,
          "timeRanges": [
            {
              "loginPolicyId": 1,
              "startTime": "00:00",
              "endTime": "24:00"
            }
```

`],`

```json
          "enable": true,
          "name": "defaultLoginPolicy.name",
          "rule": "ALLOW",
          "id": 1,
          "cuserId": "",
          "organizationVisibility": "organizationVisibility.global"
        },
        "parentPk": "1824191931******",
        "userGroups": [],
        "userRoles": [],
        "accessKeys": [
          {
            "ctime": 1591931388000,
            "id": 608,
```

```json
            "region": "cn-qingdao-****-d01",
            "accesskeyId": "cNaeitV1RB******",
            "status": "ACTIVE"
          }
```

`],`

```json
        "default": false,
        "deleted": false,
        "loginName": "baixue",
        "organization": {
          "muserId": "",
          "internal": false,
          "multiCloudStatus": "",
          "supportRegionList": [
            "cn-qingdao-****-d01"
```

`],`

```json
          "level": "0.1",
          "name": "tets",
          "alias": "tets",
          "supportRegions": "cn-qingdao-****-d01",
          "id": 353,
          "cuserId": "",
          "uuid": "null",
          "parentId": 1
        },
        "userGroupRoles": [],
        "id": 5616,
        "mobileNationCode": "86",
        "enableEmail": false,
        "email": "mail@example.com",
        "enableShortMessage": false,
        "primaryKey": "221543391942******",
        "status": "ACTIVE"
      }
```

`],`

```json
    "success": true,
    "pageInfo": {
      "total": 3,
      "totalPage": 1,
      "pageSize": 10,
      "currentPage": 1
    },
    "pureListData": false,
    "message": "success"
  }
```

###### 4.1.1.2.5. ListMembersInsideResourceSet

获取某资源集下的用户或用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/listMembersInsideResourceGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourceSetId | Integer | Body | 否 | 4 | 资源集ID。 说明该参数为必填。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 分页大小。 |
| condition | String | Body | 否 | test | 过滤条件。 说明查询资源集成员的用户名中包含此字符串的用户，不区分大小写，若不传则返回所有该资源集的用户成员。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| action | String | ListMembersInsideResourceSet | 当前接口名称。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 22 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of resourceSetMember |  | 当前资源集下的用户或用户组。 |
| authorizedAlias | String | multi-role-user-3 | 被授权的用户或用户组别名。 说明被授权指的是将用户或者用户组添加为这个资源集的成员。若被授权对象的类型是用户，则返回值为用户显示名；若被授权对象的类型是用户组，则返回值为用户组名。 |
| authorizedId | Integer | 5039 | 被授权的主体用户组ID。 说明若被授权的类型是用户，则返回值为用户ID；若被授权的类型是用户组，则返回值为用户组ID。 |
| authorizedName | String | lsq-3 | 被授权的主体名。 说明若被授权对象的类型是用户，则返回值为用户名；若被授权对象的类型是用户组，则返回值为用户组名。 |
| authorizedRoleId | Integer | 2 | 授权角色的ID。 |
| authorizedRoleName | String | defaultRole.resourceUser.name | 授权的角色名称。 |
| authorizedTime | Long | 1657763863217 | 被授权的时间。 |
| authorizedType | String | User | 被授权的类型。 UserGroup：用户组。 User：用户。 |
| domain | String | ascm.aliyun.com | 报错服务的域名。 说明无论接口是否报错都会返回。 |

| errorKey | String | ascm.auth.InvalidParameter | 错误码。 ascm.auth.ServerUnknownException：服务内部发生未知异常。 ascm.auth.InternalError：内部错误。 ascm.auth.InvalidParameter：参数错误。 ascm.auth.SystemEncodeException：系统编码异常。 ascm.auth.NetIOException：后端网络存在异常。 ascm.auth.CallBackendServiceReturnEmptyException：调用后端服务, 返回了空的Response。 ascm.auth.ForbidCallTheInterface：该功能已经下线，禁止调用。 ascm.auth.NoPermission：没有权限。 ascm.auth.CallTairException：调用Tair服务异常。 ascm.auth.EntityNotExist.Organization：组织不存在。 ascm.auth.EntityNotExist.UserGroup：用户组不存在。 ascm.auth.account.notLoggedIn：用户未登录或登录状态失效。 ascm.auth.EntityNotExist.User：用户不存在。 ascm.auth.exceeded.userUserGroup：用户加入的用户组数量超过限制。 ascm.auth.UnknownException：内部未知异常。 ascm.auth.CallDataBaseException：访问数据库异常。 ascm.auth.PageSizeBeyondQuota：PageSize不能超过限定数值。 ascm.auth.internalServerError：服务出现内部错误，请检查服务。 ascm.auth.EntityNotExist：实体不存在。 |
|---|---|---|---|
| extraMessage | String | success | 额外的提示信息，对错误提示信息的补充说明。 说明仅在接口调用失败异常时返回。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页码。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 10 | 数据总条数。 |
| totalPage | Integer | 1 | 总页数。 |
| requestId | String | 5FE0023D-73C3-481E-926D- 17A2****** | 本次请求链路ID。 |
| serverRole | String | unimanager- base.IdentityService# | 接口对应服务的服务角色名称。 |
| successResponse | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/listMembersInsideResourceGroup HTTP/1.1
```

公共请求头

```json
{ "ResourceSetId": "4" }
```

正常返回示例 `XML` 格式

```xml
<serverRole>unimanager-base.IdentityService#</serverRole> <successResponse>true</successResponse> <errorKey>ascm.auth.InvalidParamete</errorKey> <cost>22</cost> <code>200</code> <data>
    <authorizedId>5039</authorizedId>
    <authorizedName>lsq-3</authorizedName>
    <authorizedTime>1657763863217</authorizedTime>
    <authorizedRoleName>defaultRole.resourceUser.name</authorizedRoleName>
    <authorizedAlias>multi-role-user-3</authorizedAlias>
    <authorizedRoleId>2</authorizedRoleId>
    <authorizedType>User</authorizedType>
</data> <requestId>5FE0023D-73C3-481E-926D-17A2******</requestId> <domain>ascm.aliyun.com</domain> <extraMessage>success</extraMessage> <pageInfo>
    <total>10</total>
    <totalPage>1</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <action>ListMembersInsideResourceSet</action> <message>success</message>
```

| JSON | 格式 |
|---|---|
| {"serverRole":"unimanager- base.IdentityService#","successResponse":"true","errorKey":"ascm.auth.InvalidParamete","cost":"22","code":"200","data": [{"authorizedId":"5039","authorizedName":"lsq- 3","authorizedTime":"1657763863217","authorizedRoleName":"defaultRole.resourceUser.name","authorizedAlias":"multi-role-user- 3","authorizedRoleId":"2","authorizedType":"User"}],"requestId":"5FE0023D-73C3-481E-926D- 17A2******","domain":"ascm.aliyun.com","extraMessage":"success","pageInfo": {"total":"10","totalPage":"1","pageSize":"10","currentPage":"1"},"action":"ListMembersInsideResourceSet","message":"success"} |  |

###### 4.1.1.2.6. ListResourceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/list_resource_group HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourceGroupName | String | Body | 否 | test | 待查询的资源集名称。 若传入组织ID，则返回该组织下所有的用户可见资源集。 若传入资源集名称，则返回资源集名称中包含该入参取值的用户可见的资源集。 |
| organizationId | Integer | Body | 否 | 1 | 组织ID。可通过调用GetOrganizationList接口获取。 说明获取当前组织下的资源集列表，不包含下级组织。 若不传或传参为1，则返回当前用户可见的所有资源集列表。 |
| pageNumber | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 每页显示数据条数，默认为10，返回符合以上条件的所有数据的条数。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| PageInfo | Struct |  | 分页信息。 |
| CurrentPage | Integer | 1 | 当前页码。 |

| PageSize | Integer | 10 | 每页数据条数。 |
|---|---|---|---|
| Total | Integer | 10 | 数据总条数。 |
| TotalPage | Integer | 1 | 总页数。 |
| code | String | 200 | 状态码。 200：调用正常。 403：没有权限。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应数据。 |
| creator | String | admin | 资源集创建者的用户名。 |
| gmtCreated | Float | 1606719003858 | 资源集创建时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 1 | 资源集所属组织的ID。 |
| organizationName | String | test | 资源集所属组织的名称。 |
| resourceGroupName | String | test | 资源集名称。 |
| rsId | String | rs-1010e71e5e520aab******** | 资源集唯一编码。 |
| message | String | success | 提示信息。 success：调用成功。 The caller is not organization account：当前用户无权限。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true：成功。 false：失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/list_resource_group HTTP/1.1
```

公共请求头

```json
{
    "resourceGroupName": "test"
}
```

正常返回示例 `XML` 格式

```xml
<redirect>true</redirect> <PageInfo>
    <TotalPage>1</TotalPage>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <Total>10</Total>
</PageInfo> <cost>10000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <creator>admin</creator>
    <resourceGroupName>test</resourceGroupName>
    <organizationName>test</organizationName>
    <gmtCreated>1606719003858</gmtCreated>
    <rsId>rs-1010e71e5e520aab********</rsId>
    <id>1</id>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": "true", "PageInfo": { "TotalPage": "1", "PageSize": "10", "CurrentPage": "1", "Total": "10" }, "cost": "10000", "code": "200", "data": [ { "organizationID": "1", "creator": "admin", "resourceGroupName": "test", "organizationName": "test", "gmtCreated": "1606719003858", "rsId": "rs-1010e71e5e520aab********", "id": "1" } ], "success": "true", "message": "success" } |  |

###### 4.1.1.2.7. ListResourceGroupByAscmUserId

调用ListResourceGroupByAscmUserId获取用户所在的资源集列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/list_resource_group_by_ascmuser_id HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| ascmuserid _ | Integer | Body | 否 | 5 | 用户ID，可通过调用ListUsers接口获取。 说明该参数为必填。 |
| ascmRoleId | Integer | Body | 否 | 2 | 角色ID，可通过调用ListActiveRoles接口获取。传入该参数，将返回该用户的指定角色所在的资源集；如果不传该参数，则返回该用户所有角色所在的资源集。 |
| pageNumber | Integer | Body | 否 | 1 | 起始页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 返回结果中每个分页展示的记录数。如果不传该参数，则将所有符合条件的记录在一页中返回。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400：参数错误。 403：没有权限。 404：用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应结果。 |
| creator | String | admin | 资源集创建者的用户名。 |
| gmtCreated | Long | 1606791494471 | 资源集创建时间。 |
| gmtModified | Long | 1606791494472 | 资源集最近一次修改的时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 1 | 资源集所属组织的ID。 |
| resourceGroupName | String | test | 资源集名称。 |
| resourceGroupType | Integer | 1 | 资源集类型： 1：默认资源集。默认资源集是在创建组织时，由系统自动生成的。 null：非默认资源集。 |
| rsId | String | rs-123144 | 资源集唯一编码。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter：参数错误。 Forbidden：没有权限。 NotExist：用户不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/list_resource_group_by_ascmuser_id HTTP/1.1
```

公共请求头

```json
{
    "ascmuser_id": 5,
    "ascmRoleId": 2,
    "pageNumber": 1,
    "pageSize": 10
}
```

正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <data>
    <organizationID>1</organizationID>
    <gmtModified>1606791494472</gmtModified>
    <creator>admin</creator>
    <resourceGroupName>test</resourceGroupName>
    <gmtCreated>1606791494471</gmtCreated>
    <rsId>rs-123144</rsId>
    <resourceGroupType>1</resourceGroupType>
    <id>1</id>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "data": { "organizationID": 1, "gmtModified": 1606791494472, "creator": "admin", "resourceGroupName": "test", "gmtCreated": 1606791494471, "rsId": "rs-123144", "resourceGroupType": 1, "id": 1 }, "success": true, "message": "success" } |  |

###### 4.1.1.2.8. ListResourceGroupByOrgId

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/organization/resourceGroupList HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | String | Body | 否 | 34 | 组织ID。可通过调用GetOrganizationList接口获取。 说明调用该接口时必须传入组织ID参数，否则返回结果为空。 |
| resourcegroupname _ _ | String | Body | 否 | testrs | 资源集名称。 说明该参数为废弃参数。 |
| default | String | Body | 否 | 1 | 资源集类型。 1：默认资源集。 0：非默认资源集。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用正常。 400： 组织ID不可为空。 所选组织不存在。 AccessKey不合法。 参数错误。 阿里云账号不支持此操作。 403： 没有权限。 用户当前的角色已被禁用，无法执行此操作，请管理员解禁后重试。 404： AccessKey不存在。 角色不存在。 用户不存在。 用户没有该角色。 500： 远程调用错误。 内部错误。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应数据。 |
| creator | String | admin | 组织创建人的用户名。 |
| gmtCreated | Float | 1607512443989 | 资源集的创建时间。 |
| gmtModified | Float | 1607512443999 | 资源集最近一次的修改时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 1 | 组织ID。 |
| organizationName | String | admin-org | 组织名称。 |
| resourceGroupName | String | resg-test | 资源集名称。 |
| resourceGroupType | Integer | 1 | 资源集类型。 1：默认资源集。 0：非默认资源集。 |
| message | String | 200 | 提示信息。例如： The caller is not organization account：当前用户无权限查看被调用的组织。 User and access-key not matched：当前用户与AccessKey不匹配。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 100 | 总数据条数。 |
| totalPage | Integer | 10 | 总页数。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |

| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/organization/resourceGroupList HTTP/1.1
```

公共请求头

```json
{
    "id": 34
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <data> <organizationID>1</organizationID> <gmtModified>1607512443999</gmtModified> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <organizationName>admin</organizationName> <gmtCreated>1607512443989</gmtCreated> <resourceGroupType>1</resourceGroupType> <id>1</id> </data> <success>true</success> <pageInfo> <total>100</total> <totalPage>10</totalPage> <pageSize>10</pageSize> <currentPage>1</currentPage> </pageInfo> <pureListData>true</pureListData> <message> 200</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "data": [ { "organizationID": "1", "gmtModified": "1607512443999", "creator": "admin", "resourceGroupName": "test", "organizationName": "admin", "gmtCreated": "1607512443989", "resourceGroupType": "1", "id": "1" } ], "success": "true", "pageInfo": { "total": "100", "totalPage": "10", "pageSize": "10", "currentPage": "1" }, "pureListData": "true", "message": " 200" } |  |

###### 4.1.1.2.9. RemoveResourceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/delete_resource_group HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourcegroupid _ _ | Integer | Body | 否 | 5 | 待删除资源集的ID，可通过调用ListResourceGroup接口获取， 若不传则返回为空。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400： AccessKey不合法。 不支持对默认资源集执行此操作。 删除资源集前，必须和用户组解除绑定。 删除资源集前，必须删除资源集下的所有云资源。 删除资源集前，必须和用户解除绑定。 参数错误。 403：没有权限。 404： AccessKey不存在。 组织不存在。 用户不存在。 组织AccessKey不存在。 500： 远程调用错误。 内部错误。 |
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| message | String | success | 提示信息。例如： success：调用成功。 Can't find user by specified accessKey：无法根据当前AccessKey找到用户。 Caller is not the parent of user: xxx：当前用户权限不足。 Calling manage returns empty body：调用信息返回为空。 |
| pureListData | Integer | 0 | 是否只返回数据，不返回其它字段。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| requestId | String | 16d09b14-8a59-****-****- 7536fe897b66 | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/delete_resource_group HTTP/1.1
```

公共请求头

```json
{
    "resource_group_id": 5
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <requestId>16d09b14-8a59-****-****-7536fe897b66</requestId> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "requestId": "16d09b14-8a59-****-****-7536fe897b66", "message": "success" } |  |

###### 4.1.1.2.10. UnbindAscmUserAndResourceGroup

调用UnbindAscmUserAndResourceGroup为资源集移除用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/remove_ascm_users HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourcegroupid _ _ | Integer | Body | 否 | 7 | 资源集ID。可通过调用ListResourceGroup接口获取。 说明该参数为必填。 |
| ascmuserids _ _ | String | Body | 否 | "[5017,5023]" | 待解绑的用户ID列表。多个用户ID之间，用英文半角逗号（,）隔开。用户ID可通过调用ListUsers接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200: 调用成功。 400: 参数错误。 RAM授权不支持此操作。 403: 没有权限。 当前用户没有操作此资源集的权限。 用户不能对自身做此操作。 404: 资源集不存在。 AccessKey不存在。 用户没有该角色。 用户不存在。 角色不存在。 500: 内部错误。 511: 超过了每个资源集可以加入的用户数。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |

| message | String | 200 | 提示信息。例如： 内部错误。 User and resource set must be in the same top organization：用户和资源集必须在同一一级组织下。 Invalid ascmRoleId or ascmUserId：无效的角色ID或用户ID。 The role is not exist: xxx：当前角色不存在。 |
|---|---|---|---|
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/remove_ascm_users HTTP/1.1
```

公共请求头

```json
{
    "resource_group_id": 7,
    "ascm_user_ids": "[5017,5023]"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>200</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "message": "200" } |  |

###### 4.1.1.2.11. UpdateResourceGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/resource_group/update_resource_group HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | String | Body | 否 | 16 | 待修改资源集的ID。可通过调用ListResourceGroup接口获取。 说明该参数为必填。 |

| resourceGroupName | String | Body | 否 | newres _ | 待修改资源集的新名称。长度为2-50个字符。 说明该参数为必填。 |
|---|---|---|---|---|---|

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用正常。 400： AccessKey不合法。 不支持对默认资源集执行此操作。 删除资源集前，必须和用户组解除绑定。 删除资源集前，必须删除资源集下的所有云资源。 删除资源集前，必须和用户解除绑定。 参数错误。 403：没有权限。 404： AccessKey不存在。 组织不存在。 用户不存在。 组织AccessKey不存在。 500： 远程调用错误。 内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 返回数据。 |
| creator | String | admin | 资源集创建者的用户名。 |
| gmtCreated | Float | 1653485365361 | 资源集的创建时间。 |
| gmtModified | Float | 1653485365362 | 资源集最近一次的修改时间。 |
| id | Integer | 3 | 资源集ID，与入参一致。 |
| organizationID | Integer | 2 | 资源集所属组织ID。 |
| organizationName | String | ascm-test | 资源集所属组织名称。 |
| resourceGroupName | String | newres _ | 更新后的资源集名称，取值与入参一致。 |
| resourceGroupType | Integer | 1 | 资源集类型。 0：非默认资源集。 1：默认资源集。 |
| message | String | success | 提示信息。例如： success：调用成功。 Can't find user by specified accessKey：无法根据当前AccessKey找到用户。 Caller is not the parent of user: xxx：当前用户权限不足。 Calling manage returns empty body：调用信息返回为空。 |
| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |

| redirect | Boolean | true | 是否重定向。 true：重定向。 false：不重定向。 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/resource_group/update_resource_group HTTP/1.1
```

公共请求头

```json
{
    "id": 16,
    "resourceGroupName": "new_res"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <pageInfo> <gmtModified>1606791494471</gmtModified> <resourceGroupName>new_res</resourceGroupName> <id>1</id> </pageInfo> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "true", "cost": "10000", "code": "200", "success": "true", "pageInfo": { "gmtModified": "1606791494471", "resourceGroupName": "new_res", "id": "1" }, "message": "success" } |  |

##### 4.1.1.3. 角色管理

###### 4.1.1.3.1. AddRoleToUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testu | 用户登录名。 |
| loginNameList | Json | Body | 否 | ["testu1","testu2"] | 用户登录名集合。 说明若同时传入loginName、loginNameList参数，则以 loginNameList参数为准。若不传loginNameList参数，则以loginName参数为准。若两个参数都不传则返回异常。 |

| roleId | Integer | Body | 否 | 2 | 角色ID。可通过调用ListActiveRoles接口获取。 说明若同时传入roleName、roleId参数，则以roleName参数为准。若仅传入roleId参数，则以roleId参数为准。若两个参数都不传则返回异常。 |
|---|---|---|---|---|---|
| roleName | String | Body | 否 | testr | 角色名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400： 参数错误。 缺少参数。 超过了角色一次性可以授权的用户数量。 不支持对默认用户执行此操作。 403：没有权限。 404： 用户不存在。 角色不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter： 参数错误。 缺少参数。 超过了角色一次性可以授权的用户数量。 不支持对默认用户执行此操作。 Forbidden：没有权限。 NotExist： 用户不存在。 角色不存在。。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
  "loginName": "testu" ,
  "loginNameList":["testu1","testu2"] ,
  "roleName":"testr",
  "roleId": 2
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.3.2. ListActiveRoles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| includeRAMRoles | Boolean | Body | 否 | true | 是否包含RAM角色，默认为true。若不传则返回所有可用于绑定的角色。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 |
| cost | Integer | 10000 | 接口耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 响应结果。 |
| active | Boolean | true | 角色是否有效。 说明该参数已废弃。角色状态请参考enable参数。 |
| arId | String | ar-9999****** | 角色唯一编码。 |
| code | String | 200 ROLERESOURCEUSER _ _ | 角色Code。 说明 Code由系统自动生成，每个角色都有Code且唯一，预置角色的Code为固定值。 |
| default | Boolean | true | 是否为预置角色。 说明预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |

| enable | Boolean | true | 角色是否启用。 true：启用。 false：未启用。 |
|---|---|---|---|
| id | Integer | 1 | 角色ID。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 角色所属组织的组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 说明该参数即将被弃用，不建议参考此参数返回值。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数目前无实际含义。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： oleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。RAM授权是一组RAM权限的模板，可给RAM用户（子账号）授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。预置角色和自定义角色都是将Apsara Uni-manager运营控制台定义的权限点进行组装而成的角色，其权限级别都是资源，无法实现指定实例级别的权限控制。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权。RAM角色授权是一个RAM角色模板，需要指定授信策略（AssumeRolePolicyDocument）和一组RAM权限。在指定一个一级组织（阿里云账号）实例化后，会生成一个 RAM角色。 |
| userCount | Integer | 12 | 拥有该角色的用户数。 |
| message | String | success | 错误提示信息。 success：调用成功。 Forbidden：没有权限。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 20 | 每页返回数据的条数。 |
| total | Integer | 780 | 返回数据总条数。 |
| totalPage | Integer | 39 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |

| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
|---|---|---|---|
| success | Boolean | true | 接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/auth/role/listActiveRoles HTTP/1.1 公共请求头 {
    "includeRAMRole": true
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <data> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <arId>ar-9999******</arId> <code>200 ROLE_RESOURCE_USER</code> <description>defaultRole.resourceUser.description</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <userCount>12</userCount> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <roleLevel>2147483647</roleLevel> <id>1</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> </data> <success>true</success> <pageInfo> <total>780</total> <totalPage>39</totalPage> <pageSize>20</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "data": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": false, "arId": "ar-9999******", "code": "200 ROLE_RESOURCE_USER", "description": "defaultRole.resourceUser.description", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "userCount": 12, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceUser.name", "roleLevel": 2147483647, "id": 1, "organizationVisibility": "organizationVisibility.global" }, "success": true, "pageInfo": { "total": 780, "totalPage": 39, "pageSize": 20, "currentPage": 1 }, "message": "success" } |  |

###### 4.1.1.3.3. ListRoles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 分页大小，默认为10。 |
| isDefault | Boolean | Body | 否 | false | 是否为预置角色。 说明预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| roleType | String | Body | 否 | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。RAM授权是一组RAM权限的模板，可给RAM用户（子账号） 授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。预置角色和自定义角色：都是将Apsara Uni-manager运营控制台定义的权限点进行组装而成的角色，其权限级别都是资源，无法实现指定实例级别的权限控制。 ROLETYPE _RAMROLEAUTHORIZATION： RAM角色授权。RAM角色授权是一个RAM角色模板，需要指定授信策略 （AssumeRolePolicyDocument）和一组 RAM权限。在指定一个一级组织（阿里云账号）实例化后，会生成一个RAM角色。 |
| roleRange | String | Body | 否 | roleRange.allOrganizations | 角色范围。 |
| roleName | String | Body | 否 | testr | 角色名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 响应结果。 |
| -active | Boolean | true | 角色是否有效。 说明该参数已废弃。 |
| -arId | String | ar-9999999902 | 角色唯一编码。 |
| -code | String | ROLERESOURCEUSER _ _ | 角色code。 说明 code由系统自动生成，每个角色都有code且唯一，预置角色的code为固定值。 |

| -default | Boolean | true | 是否为预置角色。 说明预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、 资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、 平台安全配置管理员和组织资源监察员。 |
|---|---|---|---|
| -description | String | defaultRole.resourceUser.descript ion | 角色描述。 |
| -enable | Boolean | true | 角色是否启用。 说明原参数active已废弃，使用该参数。 ture：表示启用状态。 false：表示禁用状态。 |
| -id | Integer | 1 | 角色ID。 |
| -muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| -organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| -ownerOrganizationId | Integer | 1 | 角色所属组织的ID。 |
| -rAMRole | Boolean | false | 是否为RAM角色。 说明保留字段，不建议使用。 |
| -roleLevel | Integer | 2147483647 | 角色等级。 说明该参数目前无实际含义。 |
| -roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| -roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| -roleType | String | ROLETYPEASCM _ | 角色类型： ROLETYPE _RAM：RAM授权。RAM授权是一组RAM权限的模板，可给RAM用户（子账号）授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。预置角色和自定义角色都是将Apsara Uni-manager运营控制台定义的权限点进行组装而成的角色，其权限级别都是资源，无法实现指定实例级别的权限控制。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权。RAM角色授权是一个RAM角色模板，需要指定授信策略（AssumeRolePolicyDocument）和一组RAM权限。在指定一个一级组织（阿里云账号）实例化后，会生成一个 RAM角色。 |

| -userCount | Integer | 12 | 拥有该角色的用户数。 |
|---|---|---|---|
| code | String | ROLERESOURCEUSER _ _ | 角色code。 说明 code由系统自动生成，每个角色都有code且唯一，预置角色的code为固定值。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 Forbidden：没有权限。 InternalServerError：内部错误。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| pageInfo | Struct | - | 分页信息。 |
| -currentPage | Integer | 1 | 当前页数。 |
| -pageSize | Integer | 20 | 每页大小。 |
| -total | Integer | 790 | 返回记录总数。 |
| -totalPage | Integer | 39 | 总页数。 |

**示例**

请求示例公共请求头

```json
{
    "currentPage": 1,
    "pageSize": 10,
    "isDefault": false,
    "roleType" :"ROLETYPE_ASCM",
    "roleName":"testr"
}
```

正常返回示例 `JSON` 格式

```json
{
 "code":"ROLE_RESOURCE_USER",
 "cost":10000,
 "data":[
  {
   "roleRange":"roleRange.orgAndSubOrgs",
   "arId":"ar-9999999902",
   "muserId":"admin",
   "rAMRole":false,
   "code":"ROLE_RESOURCE_USER",
   "active":true,
   "description":"defaultRole.resourceUser.description",
   "roleType":"ROLETYPE_ASCM",
   "default":true,
   "userCount":12,
   "ownerOrganizationId":1,
   "enable":true,
   "roleName":"defaultRole.resourceUser.name",
   "id":1,
   "roleLevel":2147483647,
   "organizationVisibility":"organizationVisibility.global"
  }
```

`],`

```json
 "success":true,
 "pageInfo":{
  "total":790,
  "totalPage":39,
  "pageSize":20,
  "currentPage":1
 },
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>ROLE_RESOURCE_USER</code> <cost>10000</cost> <data> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-9999999902</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>defaultRole.resourceUser.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <userCount>12</userCount> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <id>1</id> <roleLevel>2147483647</roleLevel> <organizationVisibility>organizationVisibility.global</organizationVisibility> </data> <success>true</success> <pageInfo> <total>790</total> <totalPage>39</totalPage> <pageSize>20</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

ascm 2019-05-10

###### 4.1.1.3.4. LockRole

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 3 | 需要锁定的角色ID。 说明：该参数为必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
{
    "roleId": 3
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.5. RelateSystemWithRole

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/role/relateSystemWithRole HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 3 | 需要关联外部系统的角色ID。 说明：该参数为必填。 |
| relativeSystem | String | Body | 否 | cmp | 关联的外部系统名称。 说明：如果不填写该参数，调用接口将清空指定用户的所有外部系统关联记录。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
POST /ascm/auth/role/relateSystemWithRole HTTP/1.1 {
    "roleId": 3,
    "relativeSystem":"cmp"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.6. SetDefaultRole

设置用户的默认角色。 一个用户可拥有多个角色，调用SetDefaultRole接口设置指定用户的默认角色后，该用户下一次登录Apsara Uni-manager运营控制台，则会以默认角色登入。登录后，您可以在个人中心或首页中切换角色。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testu | 用户登录名。 说明若不传，则默认使用当前操作用户的用户登录名。 |
| roleId | Integer | Body | 否 | 2 | 角色ID。可通过调用ListActiveRoles接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 404： 用户不存在。 角色不存在。 用户没有该角色。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |

| message | String | success | 错误提示信息。 success调用成功。 Forbidden：没有权限。 NotExist： 用户不存在。 角色不存在。 用户没有该角色。 InternalServerError：内部错误。 |
|---|---|---|---|
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```json
{
    "loginName": "testu",
    "roleId": 2
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.3.7. UnLockRole

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 3 | 需要解锁的角色ID。 说明：该参数为必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
{
    "roleId": 3
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.8. UpdateRoleInfo

编辑角色基本信息。 此接口用于修改ASCM系统内角色的基本信息。角色类型包括自定义角色、RAM角色授权、RAM授权。权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》 中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 1003 | 角色ID，必填。 |
| newRoleName | String | Body | 否 | newtestrole | 新的角色名称，自定义角色类型和RAM授权类型的角色支持修改角色名称，RAM角色授权类型的角色不支持修改角色名称，选填。 |
| newDescription | String | Body | 否 | 测试数据new。 | 角色描述信息，长度限制在500以内，选填。 |
| newAssumeRolePol icyDocument | String | Body | 否 | { "Version": "1", "Statement": [{ "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": ["dms.aliyuncs.com"], "RAM": ["acs:ram::1371111998******:root"] } } ] } | 自定义信任策略，仅支持角色类型为RAM角色授权时传入，JSON串长度限制在2048以内，选填。 |
| newActions | Json | Body | 否 | ["rds:*"] | 允许访问的资源描述符列表，只有被修改的角色类型为自定义角色时才生效。列表里每个元素的字符串长度总和限制在2048以内，选填。 |
| newNotActions | Json | Body | 否 | ["ecs:*"] | 禁止访问的资源描述符列表，只有被修改的角色类型为自定义角色时才生效。列表里每个元素的字符串长度总和限制在2048以内，选填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 31 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 编辑是否成功的标识。 true: 成功 false：失败 |

**示例**

请求示例

```json
{
    "newRoleName": "newtestrole",
    "newNotActions": ["rds:*"],
    "roleId": "1003",
```

`"description": "`测试数据`new`。`",`

```json
    "newActions": ["ecs:*"]
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":31, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>31</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.9. UpdateRAMPolicy

更新RAM权限策略。 RAM权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ramPolicyId | Integer | Body | 否 | 182 | RAM权限策略ID，必填。 |
| newPolicyName | String | Body | 否 | test-ram-policy | 策略名称，由字母、数字、横线组成，限制在50 个字符以内。策略名称全局唯一，不可重复，非必填。 |
| newDescription | String | Body | 否 | 创建权限策略。 | 描述信息，限制在100个字符以内，非必填。 |
| newPolicyDocument | String | Body | 否 | {\"Version\":\"1\",\"Statement\": [{\"Effect\":\"Allow\",\"Action\":\"ecs:*\",\"Re source\":\"*\",\"Condition\":{\"IpAddress\": {\"acs:SourceIp\":[\"1**.0.113.2\"]},\"Bool\": {\"acs:MFAPresent\":[\"true\"]}}}]} | 权限策略的内容，请按照权限策略语法和结构定义填写，长度限制在4096以内，非必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |

| cost | Integer | 19 | 接口耗时，单位毫秒。 |
|---|---|---|---|
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |
| data | Struct | - | RAM权限策略详情。 |
| -ctime | Long | 1715152881889 | 创建RAM权限策略的时间戳。 |
| -description | String | 创建权限策略。 | 描述信息。 |
| -id | Integer | 182 | RAM权限策略ID。 |
| -mtime | Long | 1715152881889 | 修改RAM权限策略的时间戳。 |
| -muserId | String | admin | 修改RAM权限策略的用户名称。 |
| -policyDocument | String | {\"Version\":\"1\",\"Statement\": [{\"Effect\":\"Allow\",\"Action\":\"e cs:*\",\"Resource\":\"*\",\"Conditio n\":{\"IpAddress\": {\"acs:SourceIp\": [\"1**.0.113.2\"]},\"Bool\": {\"acs:MFAPresent\": [\"true\"]}}}]} | RAM权限策略内容。 |
| -policyName | String | test-ram-policy | RAM权限策略名称。 |
| -region | String | cn-w***********-d01 | 区域。 |

**示例**

请求示例

```json
{
    "newPolicyName": "ram-test-data-new",
    "newPolicyDocument": "{  \"Statement\": [    {      \"Action\": \"ecs:RebootInstance\",      \"Effect\": \"Allow\",      \"Resource\":
\"*\", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\"}",
    "ramPolicyId": 2,
```

`"description": "`测试数据`new",`

```json
    "organizationVisibility": "organizationVisibility.global"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":19, "data":{ "policyDocument":"{\\\"Version\\\":\\\"1\\\",\\\"Statement\\\": [{\\\"Effect\\\":\\\"Allow\\\",\\\"Action\\\":\\\"ecs:*\\\",\\\"Resource\\\":\\\"*\\\",\\\"Condition\\\":{\\\"IpAddress\\\": {\\\"acs:SourceIp\\\":[\\\"1**.0.113.2\\\"]},\\\"Bool\\\":{\\\"acs:MFAPresent\\\":[\\\"true\\\"]}}}]}", "muserId":"admin", "policyName":"test-ram-policy", "ctime":1715152881889, "description":"创建权限策略。", "id":182, "mtime":1715152881889, "region":"cn-w***********-d01" }, "success":true, "message":"success" } |  |

`XML` 格式

```xml
<code>200</code> <cost>19</cost> <data>
 <policyDocument>{\&quot;Version\&quot;:\&quot;1\&quot;,\&quot;Statement\&quot;:
[{\&quot;Effect\&quot;:\&quot;Allow\&quot;,\&quot;Action\&quot;:\&quot;ecs:*\&quot;,\&quot;Resource\&quot;:\&quot;*\&quot;,\&quot;Condition\&quot {\&quot;IpAddress\&quot;:{\&quot;acs:SourceIp\&quot;:[\&quot;1**.0.113.2\&quot;]},\&quot;Bool\&quot;:{\&quot;acs:MFAPresent\&quot;: [\&quot;true\&quot;]}}}]}</policyDocument>
 <muserId>admin</muserId>
 <policyName>test-ram-policy</policyName>
 <ctime>1715152881889</ctime>
```

`<description>`创建权限策略。`</description>`

```xml
 <id>182</id>
 <mtime>1715152881889</mtime>
 <region>cn-w***********-d01</region>
</data> <success>true</success> <message>success</message>
```

ascm 2019-05-10

###### 4.1.1.3.10. RemoveRole

删除角色。 删除角色时，操作用户的当前角色范围必须大于被删除角色的角色范围。角色范围从大到小依次是所有组织、本组织及级联下级组织、资源集。删除RAM角色授权前，必须删除RAM角色授权下的所有RAM角色；删除角色前，必须解除角色与用户、用户组的绑定关系。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleName | String | Body | 否 | mytestrolenew | 角色名称，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 45 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true: 成功 false：失败 |

**示例**

请求示例

```json
{"roleName":"mytestrolenew"}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":45, "success":true, "message":"success" } |  |

`XML` 格式

```xml
<code>200</code> <cost>45</cost> <success>true</success> <message>success</message>
```

###### 4.1.1.3.11. RemoveRAMPolicyFromRole

从RAM授权、RAM角色授权类型角色的策略列表中移除指定的RAM权限策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/role/removeRAMPolicyFromRole HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 1004 | RAM授权或者RAM角色授权类型的角色ID，必填。 |
| ramPolicyId | Integer | Body | 否 | 2 | RAM权限策略ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 75 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |

**示例**

请求示例

```json
POST /ascm/auth/role/removeRAMPolicyFromRole HTTP/1.1 {"roleId":1004,"ramPolicyId":2}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":75, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>75</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.12. RemoveRAMPolicy

删除RAM权限策略。 被删除的策略对当前用户可见才可以删除，并且删除RAM策略前，必须和角色解除绑定。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ramPolicyId | Integer | Body | 否 | 2 | RAM权限策略ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 30 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true: 成功 false：失败 |

**示例**

请求示例

```json
{"ramPolicyId":2}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":30, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>30</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.13. GetRAMPolicy

获取权限策略信息。 根据权限策略ID获取权限策略信息。权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ramPolicyId | Integer | Body | 否 | 1 | 权限策略ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 19 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | - | 权限策略详情。 |
| ctime | Long | 1712261405521 | 创建时间的时间戳。 |
| description | String | 测试数据 | 描述信息。 |
| id | Integer | 1 | 权限策略ID。 |
| mtime | Long | 1712261405521 | 更新时间的时间戳。 |
| muserId | String | dcaasinner _ | 更新操作的用户名。 |
| policyDocument | String | {\"Statement\":[{\"Action\": [\"eps:ConfigAll\"],\"Effect\":\"Allo w\",\"Resource\": [\"acs:externaldcconfig:*:*:*\"]}],\ "Version\":\"1\"} | 权限策略内容。 |
| policyName | String | ConfigAll | 权限策略名称。 |
| region | String | cn-w********-d01 | 区域。 |

**示例**

请求示例

```json
{"ramPolicyId":1}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 33, "data": { "policyDocument": "{ \"Statement\": [ { \"Action\": \"ecs:RebootInstance\", \"Effect\": \"Allow\", \"Resource\": \"*\ ", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\"}", "policyName": "ramtestdata", "ctime": 1715651685633, "description": "测试数据", "id": 1, "region": "cn-w********-d01" }, "success": true, "message": "success" } |  |

###### 4.1.1.3.14. CreateRole

创建ASCM角色。 此接口用于创建ASCM自定义角色、RAM角色授权、RAM授权（不再推荐）。权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleName | String | Body | 否 | testrole | 角色名称，最大支持64个字符。 |

| roleRange | String | Body | 否 | roleRange.allOrganizations | 管理范围，枚举值。传roleRange.rawRamRole 创建的是RAM角色授权类型的角色；传其他值创建的是ASCM自定义角色。 roleRange.allOrganizations：所有组织 roleRange.orgAndSubOrgs： 本组织及级联下级组织 roleRange.resourceSet：资源集 roleRange.rawRamRole：原生RAM Role |
|---|---|---|---|---|---|
| description | String | Body | 否 | 测试 | 角色描述信息，选填，长度限制在500以内。 |
| privileges | Json | Body | 否 | ["PRIGSYSMETERINGREAD", _ _ _ "PRIGSYSBILLINGCLOUDPRODUCTBILLR _ _ _ _ EAD", "PRIGSYSBILLINGORGRSBILLREAD", _ _ _ _ "PRIGSYSBILLINGBILLEXPORT", _ _ _ _ "PRIGSYSBILLINGBILLMODIFY", _ _ _ _ "PRIGSYSORGREAD", _ _ _ "PRIGSYSORGCREATEDELETE", _ _ _ _ "PRIGSYSORGOPERATE", _ _ _ "PRIGSYSROLEREAD", _ _ _ "PRIGSYSROLECREATEDELETE", _ _ _ _ "PRIGSYSROLEOPERATE", _ _ _ "PRIGSYSROLELOCKUNLOCK", _ _ _ _ "PRIGSYSROLESERVICEAUTHORIZE"] _ _ _ _ | 系统权限点集合，此参数非必填并且仅在创建 ASCM自定义角色时生效。 |
| organizationVisibilit y | String | Body | 否 |  | 共享范围，非必填，缺省值为全局共享。 organizationVisibility.global：全局共享 organizationVisibility.organization：本组织内共享 organizationVisibility.orgAndSubOrgs：下级组织共享 |
| assumeRolePolicyD ocument | String | Body | 否 | { "Version": "1", "Statement": [{ "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": ["dms.aliyuncs.com"], "RAM": ["acs:ram::137**********972:root"] } } ] } | 授信策略，创建RAM角色授权类型的角色时此参数必填。 |
| ramPolicyIdList | Json | Body | 否 | [1] | 通过CreateRAMPolicy接口创建RAM策略ID列表，非必填。创建RAM角色授权类型和RAM授权类型的角色时填写此参数。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 200 ：操作成功其他：操作失败 |
| cost | Integer | 13 | 接口请求耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |
| data | Struct | - | 角色详情。 |
| active | Boolean | true | 此字段已经废弃，角色禁用状态以enable 字段为准。 |
| arId | String | ar-102a21cd6f200ad41430000s | 角色UUID，角色ID在页面是不可见的，角色UUID 在ASCM 控制台页面可见。 |
| code | String | ROLETESTROLEb1dafc _ _ | 角色编码。 |
| ctime | Long | 1715077737888 | 角色创建时间。 |
| cuserId | String | admin | 创建此角色的用户名。 |

| default | Boolean | false | 是否是预置角色，预置角色是系统预定义的。 创建的角色不是默认角色。 |
|---|---|---|---|
| description | String | 测试数据 | 角色描述信息。 |
| enable | Boolean | true | 角色是否被禁用标识。 |
| id | Integer | 1591 | 角色ID。 |
| organizationVisibility | String | organizationVisibility.global | 共享范围。 organizationVisibility.global：全局共享 organizationVisibility.organization：本组织内共享 organizationVisibility.orgAndSubOrgs：下级组织共享 |
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| assumeRolePolicyDocume nt | String | { \"Version\": \"1\", \"Statement\": [ { \"Action\": \"sts:AssumeRole\", \"Effect\": \"Allow\", \"Principal\": { \"Service\": [ \"rds.aliyuncs.com\" ], \"RAM\": [ \"acs:ram::1962515325388485:ro ot\" ] } } ] } | 授信策略。 角色类型为RAM角色授权时返回此字段。 |
| rAMRole | Boolean | false | 是否是RAM 角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 |
| roleName | String | testrole | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 管理范围。 roleRange.allOrganizations：所有组织 roleRange.orgAndSubOrgs：本组织及级联下级组织 roleRange.resourceSet：资源集 roleRange.rawRamRole：原生RAM Role |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM ：RAM授权，之前的版本也叫RAM角色 ROLETYPE _ASCM： ASCM角色，包含预置角色和自定义角色 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权 |

**示例**

请求示例

```json
{
    "roleRange": "roleRange.allOrganizations",
    "privileges": ["PRIG_SYS_METERING_READ", "PRIG_SYS_BILLING_CLOUDPRODUCTBILL_READ", "PRIG_SYS_BILLING_ORGRSBILL_READ",
"PRIG_SYS_BILLING_BILL_EXPORT", "PRIG_SYS_BILLING_BILL_MODIFY", "PRIG_SYS_ORG_READ", "PRIG_SYS_ORG_CREATE_DELETE", "PRIG_SYS_ORG_OPERATE", "PRIG_SYS_ROLE_READ", "PRIG_SYS_ROLE_CREATE_DELETE", "PRIG_SYS_ROLE_OPERATE", "PRIG_SYS_ROLE_LOCK_UNLOCK", "PRIG_SYS_ROLE_SERVICE_AUTHORIZE"],
    "roleName": "testrole",
```

`"description": "`测试数据`",`

```json
    "organizationVisibility": "organizationVisibility.global"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 51, "data": { "roleRange": "roleRange.allOrganizations", "arId": "ar-102a44ce4dc00a3119ab000m", "rAMRole": false, "code": "ROLE_TESTROLE_e90480", "active": true, "description": "测试数据", "roleType": "ROLETYPE_ASCM", "default": false, "ownerOrganizationId": 1, "enable": true, "roleName": "testrole", "ctime": 1715664997440, "id": 1006, "roleLevel": 2147483647, "cuserId": "admin", "organizationVisibility": "organizationVisibility.global" }, "success": true, "message": "success" } |  |

| XML | 格式 |
|---|---|
| <successResponse>true</successResponse> <eagleEyeTraceId>0ad40da717150777378645429d0066</eagleEyeTraceId> <asapiSuccess>true</asapiSuccess> <code>200</code> <cost>13</cost> <data> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-102a21cd6f200ad41430000s</arId> <rAMRole>false</rAMRole> <code>ROLE_TESTROLE_b1dafc</code> <active>true</active> <isActive>true</isActive> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <isDefault>false</isDefault> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>testrole</roleName> <ctime>1715077737888</ctime> <id>1591</id> <roleLevel>2147483647</roleLevel> <cuserId>admin</cuserId> <organizationVisibility>organizationVisibility.global</organizationVisibility> </data> <success>true</success> <dynamicMessages /> <message>success</message> |  |

ascm 2019-05-10

###### 4.1.1.3.15. CreateRAMPolicy

创建RAM权限策略。 权限策略是用语法结构描述的一组权限的集合，可以精确地描述被授权的资源集、操作集以及授权条件。权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| policyName | String | Body | 否 | ramtestdata | 权限策略名称，必填，由字母、数字、横线组成， 限制在50个字符以内。 |

| policyDocument | String | Body | 否 | { \"Statement\": [ { \"Action\": \"ecs:RebootInstance\", \"Effect\": \"Allow\", \"Resource\": \"*\", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\" } | 权限策略的内容，必填，请按照权限策略语法和结构定义填写，长度限制在4096以内。 |
|---|---|---|---|---|---|
| description | String | Body | 否 | 测试数据 | 描述信息，非必填，限制在100个字符以内。 |
| organizationVisibilit y | String | Body | 否 | organizationVisibility.global | 共享范围，必填。以下是枚举值定义。 organizationVisibility.global：全局共享 organizationVisibility.organization：本组织内共享 organizationVisibility.orgAndSubOrgs：下级组织共享 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 55 | 接口耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |
| data | Struct | - | 权限策略详情。 |
| ctime | Long | 1715152881889 | 创建时间的时间戳。 |
| id | Integer | 182 | 权限策略ID。 |
| policyDocument | String | { \"Statement\": [ { \"Action\": \"ecs:RebootInstance\", \"Effect\": \"Allow\", \"Resource\": \"*\", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\" } | 权限策略内容。 |
| policyName | String | test-ram-policy | 权限策略名称。 |
| region | String | cn-w***********-d01 | 区域。 |

**示例**

请求示例

```json
{"policyDocument":"{ \"Statement\": [ { \"Action\": \"ecs:RebootInstance\", \"Effect\": \"Allow\", \"Resource\": \"*\", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\"}","policyName":"ramtestdata","description":"测试数据","organizationVisibility":"organizationVisibility.global"}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 13, "data": { "policyDocument": "{ \"Statement\": [ { \"Action\": \"ecs:RebootInstance\", \"Effect\": \"Allow\", \"Resource\": \"*\ ", \"Condition\": { \"Bool\": { \"acs:MFAPresent\": \"true\" } } } ], \"Version\": \"1\"}", "policyName": "ramtestdata", "ctime": 1715652917774, "id": 2, "region": "cn-w***********-d01" }, "success": true, "message": "success" } |  |

ascm 2019-05-10

###### 4.1.1.3.16. AddRAMPolicyToRole

给RAM授权和RAM角色授权添加权限策略。 给RAM授权和RAM角色授权添加权限策略。权限策略概念请查看《Apsara Uni-manager运营控制台用户指南》中RAM权限策略相关内容。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 1588 | RAM授权或者RAM角色授权类型的角色ID，必填。 |
| ramPolicyId | Integer | Body | 否 | 182 | CreateRAMPolicy创建的RAM权限策略ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 错误码。 |
| cost | Integer | 53 | 接口请求耗时，单位毫秒。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 操作是否成功的标识。 true : 成功 false：失败 |

**示例**

请求示例

```json
{"roleId":1588,"ramPolicyId":182}
```

正常返回示例 `JSON` 格式

```json
{
    "code": "200",
    "cost": 61,
    "success": true,
    "message": "success"
}
```

###### 4.1.1.3.17. ListRolesByUserAndResourceSetId

根据当前用户和资源集ID，获取用户拥有此资源集权限的角色列表，包含全局类角色，不支持显示指定user.

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resourceSets/[resourceSetId]/roles HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceSetId | String | Path | 是 | 3 | 资源集ID，必须传递 |

只需传递resourceSetId即可，userId会自动从当前请求上下文获取当前用户的id

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| dynamicMessages | String | ["ascm", "2019-05-10", "YanxuTest"] | 动态变量替换值，一般无需关注 |
| data | Array | [ { "roleRange" : "roleRange.orgAndSubOrgs", "arId" : "ar-9999999904", "muserId" : "", "rAMRole" : false, "code" : "ROLEORGANIZATIONADMIN", _ _ "active" : true, "description" : "defaultRole.organizationAdmin.d escription", "roleType" : "ROLETYPEASCM", "default" : _ true, "ownerOrganizationId" : 1, "enable" : true, "roleName" : "defaultRole.organizationAdmin.n ame", "id" : 4, "roleLevel" : 2147483647, "locked" : false, "cuserId" : "", "organizationVisibility" : "organizationVisibility.global" }, { "roleRange" : "roleRange.resourceSet", "arId" : "ar-9999999902", "muserId" : "", "rAMRole" : false, "code" : "ROLERESOURCEUSER", _ _ "active" : true, "description" : "defaultRole.resourceUser.descri ption", "roleType" : "ROLETYPEASCM", "default" : _ true, "ownerOrganizationId" : 1, "enable" : true, "roleName" : "defaultRole.resourceUser.name" , "id" : 2, "roleLevel" : 2147483647, "locked" : false, "cuserId" : "", "organizationVisibility" : "organizationVisibility.global" } ] | 角色数据列表 |
| -roleRange | String | roleRange.orgAndSubOrgs | 角色范围 |
| -arId | String | ar-9999999904 | 字符串id |
| -muserId | String | 34243 | 修改人ID |
| -rAMRole | Boolean | false | 是否是ram role |
| -code | String | ROLEORGANIZATIONADMIN _ _ | 角色code |
| -active | Boolean | true | 此字段无用，角色禁用状态以enable字段为准 |
| -description | String | defaultRole.organizationAdmin.de scription | 角色解释 |
| -roleType | String | ROLETYPEASCM _ | 角色类型，ascm 角色还是ram 角色 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -default | Boolean | true | 是不是默认角色 |
| -relativeSystem | String | cmp | 角色关联的外部系统 |
| -ownerOrganizationId | Integer | 3 | 和organizationVisibility字段相关：如果是选的全局共享，对应的 ownerOrganizationId是1；如果是本组织共享和下级组织共享，对应的 ownerOrganizationId是创建者所在的组织。 |
| -enable | Boolean | true | 角色是否禁用 |
| -roleName | String | defaultRole.resourceUser.name（ 国际化翻译后：资源集管理员） | 角色名 |
| -id | Integer | 33 | 角色id |
| -roleLevel | Integer | 1 | 废弃 |
| -locked | Boolean | false | 角色是否被锁定编辑，某些场景会被锁定不允许编辑 |
| -cuserId | String | 33 | 创建人userId |
| -organizationVisibility | String | organizationVisibility.global | 建角色时传入的共享范围，对应的有三个值:全局共享(即全部组织)、本组织内共享、下级组织共享 |
| successResponse | Boolean | true | 调用是否成功 |
| code | String | 200 | 状态码。 200：调用正常。 400: AccessKey不合法。 参数错误。 资源集不存在。 403: 没有权限。 500: 远程调用错误。 内部错误。 |
| errorKey | String | ascm.auth.InternalError | 错误码 |
| message | String | listRolesByUserAndResourceSetId Exception | 错误提示信息 |
| extraMessage | String | listRolesByUserAndResourceSetId Exception | 额外的信息 |
| requestId | String | 04443434fdff3433f335t | 请求链路ID |
| action | String | listRolesByUserAndResourceSetId | 接口名称 |
| cost | Long | 10 | 请求耗时 |
| domain | String | a.b.com | 报错的domain地址 |
| serverRole | String | ascm.auth | 报错的服务 |

**示例**

请求示例

```
GET /resourceSets/[resourceSetId]/roles HTTP/1.1 &resourceSetId=
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "successResponse":"",
 "serverRole":"",
 "errorKey":"",
 "code":"",
 "cost":"",
 "data":{
  "roleRange":"",
  "arId":"",
  "muserId":"",
  "rAMRole":"",
  "code":"",
  "active":"",
  "description":"",
  "roleType":"",
  "default":"",
  "relativeSystem":"",
  "ownerOrganizationId":"",
  "enable":"",
  "roleName":"",
  "id":"",
  "roleLevel":"",
  "locked":"",
  "cuserId":"",
  "organizationVisibility":""
 },
 "requestId":"",
 "dynamicMessages":"",
 "extraMessage":"",
 "domain":"",
 "action":"",
 "message":""
}
```

| XML | 格式 |
|---|---|
| <successResponse /> <serverRole /> <errorKey /> <code /> <cost /> <data> <roleRange /> <arId /> <muserId /> <rAMRole /> <code /> <active /> <description /> <roleType /> <default /> <relativeSystem /> <ownerOrganizationId /> <enable /> <roleName /> <id /> <roleLevel /> <locked /> <cuserId /> <organizationVisibility /> </data> <requestId /> <dynamicMessages /> <extraMessage /> <domain /> <action /> <message /> |  |

###### 4.1.1.3.18. AuthorizeRAMRoleToOrganization

将RAM角色授权给组织。 该接口用于将指定的RAM角色授权给某个组织，适用于需要进行权限管理的场景。

**注意事项**

请确保传入的 `roleId` 和 `organizationId` 参数有效且符合业务要求。 接口调用需使用AK认证方式，确保安全性和合法性。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/role/authorizeRAMRoleToOrganization HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | Integer | Body | 否 | 8 | 需要授权的RAM角色ID，角色类型必须是RAM 角色授权。 |
| organizationId | Integer | Body | 否 | 3 | 目标一级组织的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 100 | 接口处理耗时（单位：毫秒）。 |
| message | String | Success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| success | Boolean | true | 接口调用是否成功。 |
| eagleEyeTraceId | String | abcdef123456 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| errorKey | String | InvalidParameter | 错误类型关键字。 |

**示例**

请求示例

```
POST /ascm/auth/role/authorizeRAMRoleToOrganization HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| {"code":"200","cost":12,"success":true,"message":"success"} |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>12</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.3.19. GetRole

获取角色详细信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| RoleId | Integer | Body | 是 | 1016 | 角色ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 -406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 121 | 接口响应耗时，单位毫秒（ms）。 |
| eagleEyeTraceId | String | 0ad40c441**********7e0024 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| errorKey | String | ascm.auth.InternalError | 错误类型关键字。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| data | Struct | {} | 角色详细信息。 |
| -privileges | Array | [] | 角色权限信息。 |
| --privilegeStructures | Array | [] | 角色的产品权限列表。 |
| ---privilegeGroups | Array | [] | 角色权限组列表。 |
| ----code | String | PRIGACOSALERTREAD _ _ _ | 权限点编码。 |
| ----name | String | 查看 | 权限点名称。 |
| ----type | String | TYPEREAD _ | 权限类型。 |
| ---code | String | PRISPRODUCTADBGENERAL _ _ _ | 权限点分组编码。 |
| ---name | String | 通用 | 权限点分组名称。 |
| --code | String | PRODUCTADB _ | 权限点所属产品编码。 |
| --name | String | 云原生数据仓库AnalyticDB MySQL 版3.0 | 权限点所属产品名称。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -active | Boolean | true | 此字段已经废弃，角色禁用状态以enable 字段为准。 |
| -arId | String | ar-******000z | 角色唯一编号。 |
| -code | String | ROLEGLOBALRESOURCEAUDIT _ _ _ OR | 角色编码。权限校验时角色编码用来确定角色类型，判断角色是否有对应的权限。 内置角色编码是固定的. 自定义角色的编码由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |
| -default | Boolean | false | 角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、 资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| -description | String | 测试数据。 | 角色的描述。 |
| -enable | Boolean | true | 角色是否有效。 |
| -isLocked | Boolean | false | 是否锁定。 |
| -locked | Boolean | false | 是否锁定。 |
| -id | Integer | 1016 | 角色ID。 |
| -organizationVisibility | String | organizationVisibility.global | 角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| -ownerOrganizationId | Integer | 3 | 角色所属组织ID。 |
| -ownerOrganizationName | String | 测试组织 | 表示资产或资源所属的组织名称。 |
| -rAMRole | Boolean | false | 角色是否为RAM角色。 |
| -roleLevel | Integer | 1 | 角色等级，该参数已废弃。 |
| -roleName | String | autotestdcyd0a | 角色名称。 |
| -roleRange | String | roleRange.allOrganizations | 角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| - assumeRolePolicyDocume nt | String | { "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "RAM": [ "acs:ram::1930274856231860:ro ot" ], "Service": [ "rds.aliyuncs.com" ] } } ], "Version": "1" } | RAM角色的信任策略。 |
| -roleType | String | ROLETYPEASCM _ | 角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |

**示例**

请求示例

```
{ }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "eagleEyeTraceId":"0ad40c441**********7e0024", "errorKey":"ascm.auth.InternalError", "code":"200", "cost":121, "data":{ "roleRange":"roleRange.allOrganizations", "arId":"ar-******000z", "rAMRole":false, "code":"ROLE_GLOBAL_RESOURCE_AUDITOR", "assumeRolePolicyDocument":"{ \"Statement\": [ { \"Action\": \"sts:AssumeRole\", \"Effect\": \"Allow\", \"Principal\": { \"RAM\": [ \"acs:ram::1930274856231860:root\" ], \"Service\": [ \"rds.aliyuncs.com\" ] } } ], \"Version\": \"1\"}", "ownerOrganizationName":"测试组织", "active":true, "description":"测试数据。", "roleType":"ROLETYPE_ASCM", "default":false, "ownerOrganizationId":3, "enable":true, "isLocked":false, "privileges":[ { "code":"PRODUCT_ADB", "name":"云原生数据仓库AnalyticDB MySQL版3.0", "privilegeStructures":[ { "code":"PRIS_PRODUCT_ADB_GENERAL", "privilegeGroups":[ { "code":"PRIG_ACOS_ALERT_READ", "name":"查看", "type":"TYPE_READ" } ], "name":"通用" } ] } ], "roleName":"autotestdcyd0a", "id":1016, "roleLevel":1, "locked":false, "organizationVisibility":"organizationVisibility.global" }, "success":true, "message":"success" } |  |

`XML` 格式

```xml
<eagleEyeTraceId>0ad40c441**********7e0024</eagleEyeTraceId> <errorKey>ascm.auth.InternalError</errorKey> <code>200</code> <cost>121</cost> <data>
 <roleRange>roleRange.allOrganizations</roleRange>
 <arId>ar-******000z</arId>
 <rAMRole>false</rAMRole>
 <code>ROLE_GLOBAL_RESOURCE_AUDITOR</code>
 <assumeRolePolicyDocument>{
    &quot;Statement&quot;: [
        {
            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,
            &quot;Effect&quot;: &quot;Allow&quot;,
            &quot;Principal&quot;: {
                &quot;RAM&quot;: [
                    &quot;acs:ram::1930274856231860:root&quot;
```

`],`

```
                &quot;Service&quot;: [
                    &quot;rds.aliyuncs.com&quot;
```

]

```
            }
        }
```

`],`

```xml
    &quot;Version&quot;: &quot;1&quot;
}</assumeRolePolicyDocument>
  <ownerOrganizationName>测试组织</ownerOrganizationName>
  <active>true</active>
```

`<description>`测试数据。`</description>`

```xml
  <roleType>ROLETYPE_ASCM</roleType>
  <default>false</default>
  <ownerOrganizationId>3</ownerOrganizationId>
  <enable>true</enable>
  <isLocked>false</isLocked>
  <privileges>
   <code>PRODUCT_ADB</code>
   <privilegeStructures>
    <code>PRIS_PRODUCT_ADB_GENERAL</code>
    <privilegeGroups>
     <code>PRIG_ACOS_ALERT_READ</code>
     <name>查看</name>
     <type>TYPE_READ</type>
    </privilegeGroups>
    <name>通用</name>
   </privilegeStructures>
  </privileges>
  <roleName>autotestdcyd0a</roleName>
  <id>1016</id>
  <roleLevel>1</roleLevel>
  <locked>false</locked>
  <organizationVisibility>organizationVisibility.global</organizationVisibility>
 </data>
 <success>true</success>
 <message>success</message>
```

##### 4.1.1.4. 用户管理

###### 4.1.1.4.1. UpdateProxyAdmin

跨租户代维变更接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| proxyAdminID | String | Body | 否 | pa-1036f07******abc186f000h | 代理管理员UUID。 |
| proxyRoleArId | String | Body | 否 | ar-******9904 | 代理角色UUID，角色的唯一编码。 |
| description | String | Body | 否 | 测试数据 | 描述信息。 |
| proxyTime | Json | Body | 否 | { "endTime": 1770112331114, "startTime": 1770025931114, "type": "TIMERANGE" } _ | 代理生效时间。 startTime为起始时间时间戳；endTime 为截至时间时间戳；type为时间类型，目前仅支持TIME _RANGE。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| -startTime | Long |  | 否 | 1770112331114 | 起始时间时间戳。 |
| -endTime | Long |  | 否 | 1770025931114 | 截至时间时间戳。 |
| -type | String |  | 否 | TIMERANGE _ | 时间类型。 枚举值: TIME _RANGE(时间范围) |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.EntityNotExist | 错误类型关键字。 |
| message | String | success | 提示信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| eagleEyeTraceId | String | 0ad40c441762******2308977e00 24 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| data | Struct | {} | 数据。 |
| -proxyEntityLevelAlias | List | ["root", "jumptestOrg", "test" ] | 代理实体层级展示名列表。 |
| -proxyAdminID | String | pa-1036f05******abc186f000l | 代理管理员UUID。 |
| -proxyEntityType | String | ORGANIZATION | 代理实体类型，枚举类如下，分别为组织和资源集合。 ORGANIZATION RESOURCESET _ |
| -proxyEntityID | String | org-1035b25******abc186f0004 | 代理实体UUID。 |
| -proxyRoleArId | String | ar-******9904 | 代理角色UUID。 |
| -proxyMethod | String | ASSIGN | 代理方式，枚举值为以下类型，业务含义分别为指定和邀请。 ASSIGN INVITE |
| -proxyStatus | String | AVAILABLE | 代理状态 AVAILABLE 生效中 DISABLED 已禁用 EXPIRED 已失效 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -description | String | 测试数据 | 描述信息。 |
| -enable | Boolean | true | 是否启用。 |
| -cuserId | String | admin | 创建者的用户名称。 |
| -muserId | String | admin | 修改者的用户名称。 |
| -ctime | Long | 1770084132909 | 创建时间的时间戳。 |
| -mtime | Long | 1770094932909 | 修改时间的时间戳。 |
| -originUser | Struct | {} | 源用户的信息。 持有者或者代理用户持有者. |
| --userId | Integer | 5189 | 用户ID。 |
| --loginName | String | jumporgmanager | 用户名称。 |
| --displayName | String | jumporgmanager | 用户显示名。 |
| --defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| --orgId | Integer | 35 | 组织Id。 |
| --orgUuid | String | org-1035dc4******abc2036000h | 组织的唯一标识。 |
| --orgAlias | String | jumptestOrg | 组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 用户角色唯一编码。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |
| -proxyUser | Struct | {} | 代理用户信息。 |
| --userId | Integer | 5190 | 用户ID。 |
| --loginName | String | ProxyUser-jumporgmanager- mam9 | 用户名称。 |
| --displayName | String | ProxyUser-jumporgmanager- mam9 | 用户显示名。 |
| --defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| --orgId | Integer | 35 | 组织Id。 |
| --orgUuid | String | org-1035b25******abc186f0004 | 组织的唯一标识。 |
| --orgAlias | String | shuguang | 组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 用户角色唯一编码。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |
| -proxyOrganization | Struct | {} | 代理的组织信息。 代理实体类型为组织时返回。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |

| --supportRegionList | List | ["cn-ece-******188-d01" ] | 可用区列表。 |
|---|---|---|---|
| --alias | String | shuguang | 组织别名。 |
| --level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| --parentId | Integer | 1 | 父组织ID。 |
| --supportRegions | String | cn-ece-******188-d01 | 支持Region列表，用英文逗号分隔。 |
| --description | String | 测试数据 | 测试数据。 |
| -proxyResourceSet | Struct | {} | 代理的资源集合信息。 代理实体类型为资源集合时返回。 |
| --organizationId | Integer | 35 | 资源集所属组织ID。 |
| --organizationName | String | shuguang | 资源集合所属组织名称。 |
| --resourceGroupName | String | test | 资源集合名称。 |
| --resourceGroupType | Integer | 0 | 资源集合类型，0是普通资源集合，1是组织默认资源集合 |
| -- isUserDefaultResourceSet | Boolean | false | 是否为用户默认的资源集合。 |
| --gmtCreated | Long | 1770028091941 | 资源集合创建时间。 |
| --gmtModified | Long | 1770028091941 | 资源集合修改时间。 |
| --creator | String | admin | 资源集合创建者的用户名。 |
| --modifier | String | admin | 资源集合修改人用户名。 |
| --description | String | 测试数据 | 资源集合描述信息。 |
| --rsId | String | rs-1036ed1******abc186f000h | 资源集合uuid，是资源集合的唯一标识。 |
| -proxyTime | Struct | {} | 代理生效时间。 |
| --startTime | Long | 1770082732740 | 起始时间。 |
| --endTime | Long | 1770169132740 | 结束时间。 |
| --type | String | TIMERANGE _ | 时间类型。 TIMERANGE _ |

**示例**

`JSON` 格式

```json
{
 "errorKey":"ascm.auth.EntityNotExist",
 "eagleEyeTraceId":"0ad40c441762******2308977e0024",
 "code":"200",
 "cost":121,
 "data":{
  "proxyEntityID":"org-1035b25******abc186f0004",
  "proxyStatus":"AVAILABLE",
  "muserId":"admin",
  "proxyUser":{
   "arId":"ar-******9904",
   "displayName":"ProxyUser-jumporgmanager-mam9",
   "roleId":4,
   "loginName":"ProxyUser-jumporgmanager-mam9",
   "roleName":"defaultRole.organizationAdmin.name",
   "userId":5190,
   "defaultRoleId":4,
   "orgId":35,
   "orgAlias":"shuguang",
   "orgUuid":"org-1035b25******abc186f0004"
  },
  "proxyTime":{
   "startTime":1770082732740,
   "endTime":1770169132740,
   "type":"TIME_RANGE"
  },
  "proxyEntityLevelAlias":" [\"root\", \"jumptestOrg\", \"test\" ]",
  "proxyAdminID":"pa-1036f05******abc186f000l",
```

`"description":"`测试数据`",`

```json
  "mtime":1770094932909,
  "proxyEntityType":"ORGANIZATION ",
  "enable":true,
  "proxyOrganization":{
   "supportRegionList":"[\"cn-ece-******188-d01\" ]",
   "level":"0.1",
   "alias":"shuguang",
   "supportRegions":"cn-ece-******188-d01",
```

`"description":"`测试数据`",`

```json
   "parentId":1
  },
  "proxyMethod":"ASSIGN",
  "ctime":1770084132909,
  "proxyRoleArId":"ar-******9904",
  "originUser":{
   "arId":"ar-******9904",
   "displayName":"jumporgmanager",
   "roleId":4,
   "loginName":"jumporgmanager",
   "roleName":"defaultRole.organizationAdmin.name",
   "userId":5189,
   "defaultRoleId":4,
   "orgId":35,
   "orgAlias":"jumptestOrg",
   "orgUuid":"org-1035dc4******abc2036000h"
  },
  "cuserId":"admin",
  "proxyResourceSet":{
   "organizationId":35,
   "isUserDefaultResourceSet":false,
   "gmtModified":1770028091941,
   "creator":"admin",
   "resourceGroupName":"test",
   "organizationName":"shuguang",
   "gmtCreated":1770028091941,
   "modifier":"admin",
   "resourceGroupType":0,
```

`"description":"`测试数据`",`

```json
   "rsId":"rs-1036ed1******abc186f000h"
  }
 },
 "success":true,
 "message":"success"
}
```

`XML` 格式

```xml
<errorKey>ascm.auth.EntityNotExist</errorKey> <eagleEyeTraceId>0ad40c441762******2308977e0024</eagleEyeTraceId> <code>200</code> <cost>121</cost> <data>
 <proxyEntityID>org-1035b25******abc186f0004</proxyEntityID>
 <proxyStatus>AVAILABLE</proxyStatus>
 <muserId>admin</muserId>
 <proxyUser>
  <arId>ar-******9904</arId>
  <displayName>ProxyUser-jumporgmanager-mam9</displayName>
  <roleId>4</roleId>
  <loginName>ProxyUser-jumporgmanager-mam9</loginName>
  <roleName>defaultRole.organizationAdmin.name</roleName>
  <userId>5190</userId>
  <defaultRoleId>4</defaultRoleId>
  <orgId>35</orgId>
  <orgAlias>shuguang</orgAlias>
  <orgUuid>org-1035b25******abc186f0004</orgUuid>
 </proxyUser>
 <proxyTime>
  <startTime>1770082732740</startTime>
  <endTime>1770169132740</endTime>
  <type>TIME_RANGE</type>
 </proxyTime>
 <proxyEntityLevelAlias> [&quot;root&quot;, &quot;jumptestOrg&quot;, &quot;test&quot; ]</proxyEntityLevelAlias>
 <proxyAdminID>pa-1036f05******abc186f000l</proxyAdminID>
 <description>测试数据</description>
 <mtime>1770094932909</mtime>
 <proxyEntityType>ORGANIZATION </proxyEntityType>
 <enable>true</enable>
 <proxyOrganization>
  <supportRegionList>[&quot;cn-ece-******188-d01&quot; ]</supportRegionList>
  <level>0.1</level>
  <alias>shuguang</alias>
  <supportRegions>cn-ece-******188-d01</supportRegions>
  <description>测试数据</description>
  <parentId>1</parentId>
 </proxyOrganization>
 <proxyMethod>ASSIGN</proxyMethod>
 <ctime>1770084132909</ctime>
 <proxyRoleArId>ar-******9904</proxyRoleArId>
 <originUser>
  <arId>ar-******9904</arId>
  <displayName>jumporgmanager</displayName>
  <roleId>4</roleId>
  <loginName>jumporgmanager</loginName>
  <roleName>defaultRole.organizationAdmin.name</roleName>
  <userId>5189</userId>
  <defaultRoleId>4</defaultRoleId>
  <orgId>35</orgId>
  <orgAlias>jumptestOrg</orgAlias>
  <orgUuid>org-1035dc4******abc2036000h</orgUuid>
 </originUser>
 <cuserId>admin</cuserId>
 <proxyResourceSet>
  <organizationId>35</organizationId>
  <isUserDefaultResourceSet>false</isUserDefaultResourceSet>
  <gmtModified>1770028091941</gmtModified>
  <creator>admin</creator>
  <resourceGroupName>test</resourceGroupName>
  <organizationName>shuguang</organizationName>
  <gmtCreated>1770028091941</gmtCreated>
  <modifier>admin</modifier>
  <resourceGroupType>0</resourceGroupType>
```

`<description>`测试数据

```xml
  </description>
  <rsId>rs-1036ed1******abc186f000h</rsId>
 </proxyResourceSet>
</data> <success>true</success> <message>success</message>
```

###### 4.1.1.4.2. UpdateProxyAdminStatus

启用/禁用代理管理员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| proxyAdminID | String | Body | 否 | pa-1036f05******abc186f000l | 代理管理员ID。 |
| enable | Boolean | Body | 否 | true | 启用/禁用。 枚举值: true(启用) false(禁用) |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.EntityNotExist | 错误类型关键字。 |
| message | String | success | 提示信息。 |
| eagleEyeTraceId | String | 0ad40c441762******2308977e00 24 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | {} | 数据。 |
| -proxyEntityLevelAlias | List | ["root", "shuguang"] | 代理实体层级展示名列表。 |
| -proxyAdminID | String | pa-1036f07******abc186f000h | 代理管理员UUID。 |
| -proxyEntityType | String | ORGANIZATION | 代理实体类型，枚举类如下，分别为组织和资源集合。 ORGANIZATION RESOURCESET _ |
| -proxyEntityID | String | org-1035b25******abc186f0004 | 代理实体UUID。 |
| -proxyRoleArId | String | ar-******9904 | 代理角色UUID。 |
| -proxyMethod | String | ASSIGN | 代理方式，枚举值为以下类型，业务含义分别为指定和邀请。 ASSIGN INVITE |
| -proxyStatus | String | AVAILABLE | 代理状态 AVAILABLE 生效中 DISABLED 已禁用 EXPIRED 已失效 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -description | String | 测试 | 描述信息。 |
| -enable | Boolean | true | 是否启用。 |
| -cuserId | String | admin | 创建者的用户名称。 |
| -muserId | String | admin | 修改者的用户名称。 |
| -ctime | Long | 1770084132909 | 创建时间的时间戳。 |
| -mtime | Long | 1770091332909 | 修改时间的时间戳。 |
| -originUser | Struct | {} | 源用户的信息。 持有者或者代理用户持有者. |
| --userId | Integer | 5189 | 用户ID。 |
| --loginName | String | jumporgmanager | 用户名称。 |
| --displayName | String | jumporgmanager | 用户显示名。 |
| --defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| --orgId | Integer | 35 | 组织Id。 |
| --orgUuid | String | org-10366fb******abc2036000d | 组织的唯一标识。 |
| --orgAlias | String | jumptestOrg | 组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 用户角色唯一编码。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |
| -proxyUser | Struct | {} | 源用户的信息。 持有者或者代理用户持有者。 |
| --userId | Integer | 5190 | 用户ID。 |
| --loginName | String | ProxyUser-jumporgmanager- mam9 | 用户名称。 |
| --displayName | String | ProxyUser-jumporgmanager- mam9 | 用户显示名。 |
| --defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| --orgId | Integer | 4 | 组织Id。 |
| --orgUuid | String | org-1035b25******abc186f0004 | 组织的唯一标识。 |
| --orgAlias | String | shuguang | 组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 用户角色唯一编码。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -proxyOrganization | Struct | {} | 代理的组织信息。 代理实体类型为组织时返回。 |
| --supportRegionList | List | ["cn-ece-******188-d01"] | 可用区列表。 |
| --alias | String | shuguang | 组织别名。 |
| --level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| --parentId | Integer | 1 | 父组织ID。 |
| --supportRegions | String | cn-ece-******188-d01 | 支持Region列表，用英文逗号分隔。 |
| --description | String | 测试 | 测试数据。 |
| -proxyResourceSet | Struct | {} | 代理的资源集合信息。 代理实体类型为资源集合时返回。 |
| --organizationId | Integer | 35 | 资源集所属组织ID。 |
| --organizationName | String | shuguang | 资源集合所属组织名称。 |
| --resourceGroupName | String | test | 资源集合名称。 |
| --resourceGroupType | Integer | 0 | 资源集合类型，0是普通资源集合，1是组织默认资源集合。 |
| -- isUserDefaultResourceSet | Boolean | false | 是否为用户默认的资源集合。 |
| --gmtCreated | Long | 1770028091941 | 资源集合创建时间。 |
| --gmtModified | Long | 1770028091941 | 资源集合修改时间。 |
| --creator | String | admin | 资源集合创建者的用户名。 |
| --modifier | String | admin | 资源集合修改人用户名。 |
| --description | String | 测试 | 资源集合描述信息。 |
| --rsId | String | rs-1036ed1******abc186f000h | 资源集合uuid，是资源集合的唯一标识。 |
| -proxyTime | Struct | {} | 代理生效时间。 |
| --startTime | Long | 1770082732740 | 起始时间。 |
| --endTime | Long | 1770169132740 | 结束时间。 |
| --type | String | TIMERANGE _ | 时间类型。 TIMERANGE _ |

**示例**

`JSON` 格式

```json
{
 "errorKey":"ascm.auth.EntityNotExist",
 "eagleEyeTraceId":"0ad40c441762******2308977e0024",
 "code":"200",
 "cost":121,
 "data":{
  "proxyEntityID":"org-1035b25******abc186f0004",
  "proxyStatus":"AVAILABLE",
  "muserId":"admin",
  "proxyUser":{
   "arId":"ar-******9904",
   "displayName":"ProxyUser-jumporgmanager-mam9",
   "roleId":4,
   "loginName":"ProxyUser-jumporgmanager-mam9",
   "roleName":"defaultRole.organizationAdmin.name",
   "userId":5190,
   "defaultRoleId":4,
   "orgId":4,
   "orgAlias":"shuguang",
   "orgUuid":"org-1035b25******abc186f0004"
  },
  "proxyTime":{
   "startTime":1770082732740,
   "endTime":1770169132740,
   "type":"TIME_RANGE"
  },
  "proxyEntityLevelAlias":"[\"root\", \"shuguang\"]",
  "proxyAdminID":"pa-1036f07******abc186f000h",
  "description":"测试",
  "mtime":1770091332909,
  "proxyEntityType":"ORGANIZATION",
  "enable":true,
  "proxyOrganization":{
   "supportRegionList":"[\"cn-ece-******188-d01\"]",
   "level":"0.1",
   "alias":"shuguang",
   "supportRegions":"cn-ece-******188-d01",
   "description":"测试",
   "parentId":1
  },
  "proxyMethod":"ASSIGN",
  "ctime":1770084132909,
  "proxyRoleArId":"ar-******9904",
  "originUser":{
   "arId":"ar-******9904",
   "displayName":"jumporgmanager",
   "roleId":4,
   "loginName":"jumporgmanager",
   "roleName":"defaultRole.organizationAdmin.name",
   "userId":5189,
   "defaultRoleId":4,
   "orgId":35,
   "orgAlias":"jumptestOrg",
   "orgUuid":"org-10366fb******abc2036000d"
  },
  "cuserId":"admin",
  "proxyResourceSet":{
   "organizationId":35,
   "isUserDefaultResourceSet":false,
   "gmtModified":1770028091941,
   "creator":"admin",
   "resourceGroupName":"test",
   "organizationName":"shuguang",
   "gmtCreated":1770028091941,
   "modifier":"admin",
   "resourceGroupType":0,
   "description":"测试",
   "rsId":"rs-1036ed1******abc186f000h"
  }
 },
 "success":true,
 "message":"success"
}
```

`XML` 格式

```xml
<errorKey>ascm.auth.EntityNotExist</errorKey> <eagleEyeTraceId>0ad40c4417628307082308977e0024</eagleEyeTraceId> <code>200</code> <cost>121</cost> <data>
 <proxyEntityID>org-1035b25ea5180abc186f0004</proxyEntityID>
 <proxyStatus>AVAILABLE</proxyStatus>
 <muserId>admin</muserId>
 <proxyUser>
  <arId>ar-9999999904</arId>
  <displayName>ProxyUser-jumporgmanager-mam9</displayName>
  <roleId>4</roleId>
  <loginName>ProxyUser-jumporgmanager-mam9</loginName>
  <roleName>defaultRole.organizationAdmin.name</roleName>
  <userId>5190</userId>
  <defaultRoleId>4</defaultRoleId>
  <orgId>4</orgId>
  <orgAlias>shuguang</orgAlias>
  <orgUuid>org-1035b25ea5180abc186f0004</orgUuid>
 </proxyUser>
 <proxyTime>
  <startTime>1770082732740</startTime>
  <endTime>1770169132740</endTime>
  <type>TIME_RANGE</type>
 </proxyTime>
 <proxyEntityLevelAlias>[&quot;root&quot;, &quot;shuguang&quot;]</proxyEntityLevelAlias>
 <proxyAdminID>pa-1036f07069ad0abc186f000h</proxyAdminID>
 <description>测试</description>
 <mtime>1770091332909</mtime>
 <proxyEntityType>ORGANIZATION</proxyEntityType>
 <enable>true</enable>
 <proxyOrganization>
  <supportRegionList>[&quot;cn-ece-entity188-d01&quot;]</supportRegionList>
  <level>0.1</level>
  <alias>shuguang</alias>
  <supportRegions>cn-ece-entity188-d01</supportRegions>
  <description>测试</description>
  <parentId>1</parentId>
 </proxyOrganization>
 <proxyMethod>ASSIGN</proxyMethod>
 <ctime>1770084132909</ctime>
 <proxyRoleArId>ar-9999999904</proxyRoleArId>
 <originUser>
  <arId>ar-9999999904</arId>
  <displayName>jumporgmanager</displayName>
  <roleId>4</roleId>
  <loginName>jumporgmanager</loginName>
  <roleName>defaultRole.organizationAdmin.name</roleName>
  <userId>5189</userId>
  <defaultRoleId>4</defaultRoleId>
  <orgId>35</orgId>
  <orgAlias>jumptestOrg</orgAlias>
  <orgUuid>org-10366fbeca910abc2036000d</orgUuid>
 </originUser>
 <cuserId>admin</cuserId>
 <proxyResourceSet>
  <organizationId>35</organizationId>
  <isUserDefaultResourceSet>false</isUserDefaultResourceSet>
  <gmtModified>1770028091941</gmtModified>
  <creator>admin</creator>
  <resourceGroupName>test</resourceGroupName>
  <organizationName>shuguang</organizationName>
  <gmtCreated>1770028091941</gmtCreated>
  <modifier>admin</modifier>
  <resourceGroupType>0</resourceGroupType>
  <description>测试</description>
  <rsId>rs-1036ed194ba30abc186f000h</rsId>
 </proxyResourceSet>
</data> <success>true</success> <message>success</message>
```

###### 4.1.1.4.3. ListProxyAdmins

查看代理管理员列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/proxyAdmin/list HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| proxyEntityType | String | Body | 否 | ORGANIZATION | 代理实体类型 |
| proxyEntityID | String | Body | 否 | org-1035b25******abc186f0004 | 代理实体ID。 |
| proxyStatus | String | Body | 否 | AVAILABLE | 代理状态。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 单页大小，默认为10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [] | 数据列表。 |
| -proxyEntityLevelAlias | List | [ "root", "shuguang" ] | 代理实体层级展示名列表。 |
| -proxyAdminID | String | pa-1036f07******abc186f000h | 代理管理员ID。 |
| -proxyEntityType | String | ORGANIZATION | 代理实体类型，枚举类如下，分别为组织和资源集合。 ORGANIZATION RESOURCESET _ |
| -proxyEntityID | String | org-1035b25******abc186f0004 | 代理实体ID。 |
| -proxyRoleArId | String | ar-******9904 | 代理角色ID。 |
| -proxyMethod | String | ASSIGN | 代理方式，枚举值为以下类型，业务含义分别为指定和邀请。 ASSIGN INVITE |
| -proxyStatus | String | AVAILABLE | 代理状态 AVAILABLE 生效中 DISABLED 已禁用 EXPIRED 已失效 |
| -description | String | 测试数据。 | 描述信息。 |
| -enable | Boolean | true | 是否启用。 |
| -cuserId | String | admin | 创建者的用户名称。 |
| -muserId | String | admin | 修改者的用户名称。 |
| -ctime | Long | 1770084132909 | 创建时间的时间戳。 |
| -mtime | Long | 1770084132909 | 修改时间的时间戳。 |
| -originUser | Struct | {} | 源用户的信息。 持有者或者代理用户持有者. |
| --userId | Integer | 5190 | 代理用户的ID。 |
| --loginName | String | ProxyUser-jumporgmanager- mam9 | 代理用户用户名。 |
| --displayName | String | ProxyUser-jumporgmanager- mam9 | 代理用户显示名。 |
| --defaultRoleId | Integer | 4 | 代理用户默认角色ID。 |
| --orgId | Integer | 3 | 代理用户所属组织ID。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --orgUuid | String | org-1035b25******abc186f0004 | 代理用户所属组织UUID。 |
| --orgAlias | String | shuguang | 代理用户所属组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 角色UUID。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| -proxyUser | Struct | {} | 代理用户信息。 |
| --userId | Integer | 5190 | 代理用户的ID。 |
| --loginName | String | ProxyUser-jumporgmanager- mam9 | 代理用户用户名。 |
| --displayName | String | ProxyUser-jumporgmanager- mam9 | 代理用户显示名。 |
| --defaultRoleId | Integer | 4 | 代理用户默认角色ID。 |
| --orgId | Integer | 3 | 代理用户所属组织ID。 |
| --orgUuid | String | org-1035b25******abc186f0004 | 代理用户所属组织UUID。 |
| --orgAlias | String | shuguang | 代理用户所属组织别名。 |
| --roleId | Integer | 4 | 角色ID。 |
| --arId | String | ar-******9904 | 角色UUID。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| -proxyOrganization | Struct | {} | 代理的组织信息。 代理实体类型为组织时返回。 |
| --supportRegionList | List | ["cn-ece-******188-d01"] | 可用区列表。 |
| --alias | String | shuguang | 组织别名。 |
| --level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| --parentId | Integer | 1 | 父组织ID。 |
| --supportRegions | String | cn-ece-******188-d01 | 支持Region列表，用英文逗号分隔。 |
| --description | String | 测试 | 组织描述信息。 |
| -proxyResourceSet | Struct | {} | 代理的资源集合信息。 代理实体类型为资源集合时返回。 |
| --organizationId | Integer | 35 | 资源集所属组织ID。 |
| --organizationName | String | testorg | 资源集合所属组织名称。 |
| --resourceGroupName | String | test | 资源集合名称。 |
| --resourceGroupType | Integer | 0 | 资源集合类型，0是普通资源集合，1是组织默认资源集合。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -- isUserDefaultResourceSet | Boolean | false | 是否为用户默认的资源集合。 |
| --gmtCreated | Long | 1770028091941 | 资源集合创建时间。 |
| --gmtModified | Long | 1770028091941 | 资源集合修改时间。 |
| --creator | String | admin | 资源集合创建者的用户名。 |
| --modifier | String | admin | 资源集合修改人用户名。 |
| --description | String | 测试数据 | 资源集合描述信息。 |
| --rsId | String | rs-1036ed1******abc186f000h | 资源集合uuid，是资源集合的唯一标识。 |
| -proxyTime | Struct | {} | 代理生效时间。 |
| --startTime | Long | 1770082732740 | 起始时间。 |
| --endTime | Long | 1770169132740 | 结束时间。 |
| --type | String | TIMERANGE _ | 时间类型。 TIMERANGE _ |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.EntityNotExist | 错误类型关键字。 |
| message | String | success | 提示信息。 |
| eagleEyeTraceId | String | 0ad40c441762******2308977e00 24 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| pageInfo | Struct | { "currentPage": 1, "pageSize": 10, "total": 1, "totalPage": 1 } | 返回分页信息。 |
| -currentPage | Integer | 1 | 分页查询时，当前页的页码。 |
| -pageSize | Integer | 10 | 分页查询时，每页数据显示的最大条数。 |
| -total | Integer | 10 | 数据总条数。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -totalPage | Integer | 1 | 分页查询时，返回总页数。 |

**示例**

请求示例

```
POST /ascm/auth/proxyAdmin/list HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.auth.EntityNotExist", "eagleEyeTraceId":"0ad40c441762******2308977e0024", "code":"200", "cost":121, "data":[ { "proxyEntityID":"org-1035b25******abc186f0004", "proxyStatus":"AVAILABLE", "muserId":"admin", "proxyUser":[ { "arId":"ar-******9904", "displayName":"ProxyUser-jumporgmanager-mam9", "roleId":4, "loginName":"ProxyUser-jumporgmanager-mam9", "roleName":"defaultRole.organizationAdmin.name", "userId":5190, "defaultRoleId":4, "orgId":3, "orgAlias":"shuguang", "orgUuid":"org-1035b25******abc186f0004" } ], "proxyTime":[ { "startTime":1770082732740, "endTime":1770169132740, "type":"TIME_RANGE" } ], "proxyEntityLevelAlias":"[ \"root\", \"shuguang\" ]", "proxyAdminID":"pa-1036f07******abc186f000h", "description":"测试数据。", "mtime":1770084132909, "proxyEntityType":"ORGANIZATION", "enable":true, "proxyOrganization":[ { "supportRegionList":" [\"cn-ece-******188-d01\"]", "level":"0.1", "alias":"shuguang", "supportRegions":"cn-ece-******188-d01", "description":"测试", "parentId":1 } ], "proxyMethod":"ASSIGN", "ctime":1770084132909, "proxyRoleArId":"ar-******9904", "originUser":[ { "arId":"ar-******9904", "displayName":"ProxyUser-jumporgmanager-mam9", "roleId":4, "loginName":"ProxyUser-jumporgmanager-mam9", "roleName":"defaultRole.organizationAdmin.name", "userId":5190, "defaultRoleId":4, "orgId":3, "orgAlias":"shuguang", "orgUuid":"org-1035b25******abc186f0004" } ], "cuserId":"admin", "proxyResourceSet":[ { "organizationId":35, "isUserDefaultResourceSet":false, |  |

```json
     "gmtModified":1770028091941,
     "creator":"admin",
     "resourceGroupName":"test",
     "organizationName":"testorg",
     "gmtCreated":1770028091941,
     "modifier":"admin",
     "resourceGroupType":0,
```

`"description":"`测试数据`",`

```json
     "rsId":"rs-1036ed1******abc186f000h"
    }
```

]

```
  }
```

`],`

```json
 "success":true,
 "pageInfo":{
  "total":10,
  "totalPage":1,
  "pageSize":10,
  "currentPage":1
 },
 "message":"success"
}
```

`XML` 格式

```xml
<errorKey>ascm.auth.EntityNotExist</errorKey> <eagleEyeTraceId>0ad40c441762******2308977e0024</eagleEyeTraceId> <code>200</code> <cost>121</cost> <data>
 <proxyEntityID>org-1035b25******abc186f0004</proxyEntityID>
 <proxyStatus>AVAILABLE</proxyStatus>
 <muserId>admin</muserId>
 <proxyUser>
  <arId>ar-******9904</arId>
  <displayName>ProxyUser-jumporgmanager-mam9</displayName>
  <roleId>4</roleId>
  <loginName>ProxyUser-jumporgmanager-mam9</loginName>
  <roleName>defaultRole.organizationAdmin.name</roleName>
  <userId>5190</userId>
  <defaultRoleId>4</defaultRoleId>
  <orgId>3</orgId>
  <orgAlias>shuguang</orgAlias>
  <orgUuid>org-1035b25******abc186f0004</orgUuid>
 </proxyUser>
 <proxyTime>
  <startTime>1770082732740</startTime>
  <endTime>1770169132740</endTime>
  <type>TIME_RANGE</type>
 </proxyTime>
 <proxyEntityLevelAlias>[
                &quot;root&quot;,
                &quot;shuguang&quot;
            ]</proxyEntityLevelAlias>
  <proxyAdminID>pa-1036f07******abc186f000h</proxyAdminID>
```

`<description>`测试数据。`</description>`

```xml
  <mtime>1770084132909</mtime>
  <proxyEntityType>ORGANIZATION</proxyEntityType>
  <enable>true</enable>
  <proxyOrganization>
   <supportRegionList> [&quot;cn-ece-******188-d01&quot;]</supportRegionList>
   <level>0.1</level>
   <alias>shuguang</alias>
   <supportRegions>cn-ece-******188-d01</supportRegions>
   <description>测试</description>
   <parentId>1</parentId>
  </proxyOrganization>
  <proxyMethod>ASSIGN</proxyMethod>
  <ctime>1770084132909</ctime>
  <proxyRoleArId>ar-******9904</proxyRoleArId>
  <originUser>
   <arId>ar-******9904</arId>
   <displayName>ProxyUser-jumporgmanager-mam9</displayName>
   <roleId>4</roleId>
   <loginName>ProxyUser-jumporgmanager-mam9</loginName>
   <roleName>defaultRole.organizationAdmin.name</roleName>
   <userId>5190</userId>
   <defaultRoleId>4</defaultRoleId>
   <orgId>3</orgId>
   <orgAlias>shuguang</orgAlias>
   <orgUuid>org-1035b25******abc186f0004</orgUuid>
  </originUser>
  <cuserId>admin</cuserId>
  <proxyResourceSet>
   <organizationId>35</organizationId>
   <isUserDefaultResourceSet>false</isUserDefaultResourceSet>
   <gmtModified>1770028091941</gmtModified>
   <creator>admin</creator>
   <resourceGroupName>test</resourceGroupName>
   <organizationName>testorg</organizationName>
   <gmtCreated>1770028091941</gmtCreated>
   <modifier>admin</modifier>
   <resourceGroupType>0</resourceGroupType>
   <description>测试数据</description>
   <rsId>rs-1036ed1******abc186f000h</rsId>
  </proxyResourceSet>
 </data>
 <success>true</success>
 <pageInfo>
  <total>10</total>
  <totalPage>1</totalPage>
  <pageSize>10</pageSize>
  <currentPage>1</currentPage>
 </pageInfo>
 <message>success</message>
```

###### 4.1.1.4.4. DeleteProxyAdmin

删除代理管理员。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/proxyAdmin/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| proxyAdminID | String | Body | 否 | pa-1036f05******abc186f000l | 代理管理员ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.EntityNotExist | 错误类型关键字。 |
| message | String | success | 错误类型关键字。 |
| eagleEyeTraceId | String | 0ad40c441762******2308977e00 24 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| cost | Long | 150 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
POST /ascm/auth/proxyAdmin/delete HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.auth.EntityNotExist", "eagleEyeTraceId":"0ad40c441762******2308977e0024", "code":"200", "cost":150, "success":true, "message":"success" } |  |

`XML` 格式

```xml
<errorKey>ascm.auth.EntityNotExist</errorKey> <eagleEyeTraceId>0ad40c441762******2308977e0024</eagleEyeTraceId> <code>200</code> <cost>150</cost> <success>true</success> <message>success</message>
```

###### 4.1.1.4.5. AssignProxyAdmin

运营管理员等全局管理员指派用户为代理管理员。 接口说明

**注意事项**

权限点：指派代理管理员 PRIG_SYS_PROXY_ADMIN_ASSIGN。 仅支持将其他一级组织下用户设置为代理管理员。 预置用户禁止被代维（admin、super等）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/proxyAdmin/assign HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| proxyEntityType | String | Body | 否 | ORGANIZATION | 代理实体类型枚举值: ORGANIZATION (组织) RESOURCE _SET(资源集合) |
| proxyEntityID | String | Body | 否 | org-1036052******adf04a5000i | 代理实体UUID。 |
| loginName | String | Body | 否 | testUser | 源用户用户名。 注意不是展示名，是用于登录的用户名。 |
| proxyRoleArId | String | Body | 否 | ar-******9904 | 代理角色UUID。 |
| description | String | Body | 否 | 测试数据。 | 描述信息。 |
| proxyTime | Json | Body | 否 | { "endTime": 1770112331114, "startTime": 1770025931114, "type": "TIMERANGE" } _ | 代理生效时间。 startTime为起始时间时间戳；endTime 为截至时间时间戳；type为时间类型，目前仅支持TIME _RANGE。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.EntityNotExist | 错误类型关键字。 |
| message | String | success | 提示信息。 |
| eagleEyeTraceId | String | 0ad40c441762******2308977e00 24 | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | {} | 数据。 |
| -proxyAdmin | Struct | {} | 代维管理员详情。 |
| --proxyEntityLevelAlias | List | [ "root","test"] | 代理实体层级展示名列表。 |
| --proxyAdminID | String | pa-1036dc8******adf0874000b | 代理管理员UUID。 |
| --proxyEntityType | String | ORGANIZATION | 代理实体类型，枚举类如下，分别为组织和资源集合。 ORGANIZATION RESOURCESET _ |
| --proxyEntityID | String | org-1036052******adf04a5000i | 代理实体UUID。 |
| --proxyRoleArId | String | ar-******9904 | 代理角色UUID。 |
| --proxyMethod | String | ASSIGN | 代理方式，枚举值为以下类型，业务含义分别为指定和邀请。 ASSIGN INVITE |
| --proxyStatus | String | AVAILABLE | 代理状态 AVAILABLE 生效中 DISABLED 已禁用 EXPIRED 已失效 |
| --description | String | 测试 | 描述信息。 |
| --enable | Boolean | true | 是否启用。 |
| --cuserId | String | admin | 创建者的用户名称。 |
| --muserId | String | admin | 修改者的用户名称。 |
| --ctime | Long | 1769750315780 | 创建时间的时间戳。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --mtime | Long | 1769750319380 | 修改时间的时间戳。 |
| --originUser | Struct | {} | 源用户的信息。 持有者或者代理用户持有者. |
| ---userId | Integer | 6356 | 用户ID。 |
| ---loginName | String | ProxyUser-orgResourceAuditor- splk | 用户名称。 |
| ---displayName | String | ProxyUser-orgResourceAuditor- splk | 用户显示名。 |
| ---defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| ---orgId | Integer | 356 | 组织Id。 |
| ---orgUuid | String | org-1036052******adf04a5000i | 组织的唯一标识。 |
| ---orgAlias | String | test | 组织别名。 |
| ---roleId | Integer | 4 | 角色ID。 |
| ---arId | String | ar-******9904 | 用户角色唯一编码。 |
| ---roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |
| --proxyUser | Struct | {} | 代理用户信息。 |
| ---userId | Integer | 6356 | 用户ID。 |
| ---loginName | String | ProxyUser-orgResourceAuditor- splk | 用户名称。 |
| ---displayName | String | ProxyUser-orgResourceAuditor- splk | 用户显示名。 |
| ---defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| ---orgId | Integer | 356 | 组织Id。 |
| ---orgUuid | String | org-1036052******adf04a5000i | 组织的唯一标识。 |
| ---orgAlias | String | test | 组织别名。 |
| ---roleId | Integer | 4 | 角色ID。 |
| ---arId | String | ar-******9904 | 用户角色唯一编码。 |
| ---roleName | String | defaultRole.organizationAdmin.na me | 用户角色名称。 |
| --proxyOrganization | Struct | {} | 代理的组织信息。 代理实体类型为组织时返回。 |
| ---supportRegionList | List | ["cn-wul******223-d01" ] | 可用区列表。 |
| ---alias | String | test | 组织别名。 |
| ---level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| ---parentId | Integer | 1 | 父组织ID。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---supportRegions | String | cn-wul******223-d01 | 支持Region列表，用英文逗号分隔。 |
| ---description | String | 测试数据。 | 测试数据。 |
| --proxyResourceSet | Struct | {} | 代理的资源集合信息。 代理实体类型为资源集合时返回。 |
| ---organizationId | Integer | 35 | 资源集所属组织ID。 |
| ---organizationName | String | testorg | 资源集合所属组织名称。 |
| ---resourceGroupName | String | test | 资源集合名称。 |
| ---resourceGroupType | Integer | 0 | 资源集合类型，0是普通资源集合，1是组织默认资源集合。 |
| --- isUserDefaultResourceSet | Boolean | false | 是否为用户默认的资源集合。 |
| ---gmtCreated | Long | 1770028091941 | 资源集合创建时间。 |
| ---gmtModified | Long | 1770028091941 | 资源集合修改时间。 |
| ---creator | String | admin | 资源集合创建者的用户名。 |
| ---modifier | String | admin | 资源集合修改人用户名。 |
| ---description | String | 测试数据 | 资源集合描述信息。 |
| ---rsId | String | rs-1036ed1******abc186f000h | 资源集合uuid，是资源集合的唯一标识。 |
| --proxyTime | Struct | {} | 代理生效时间。 |
| ---startTime | Long | 1769750313647 | 起始时间。 |
| ---endTime | Long | 1769836713647 | 结束时间。 |
| ---type | String | TIMERANGE _ | 时间类型。 TIMERANGE _ |

**示例**

请求示例

```
POST /ascm/auth/proxyAdmin/assign HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
 "errorKey":"ascm.auth.EntityNotExist",
 "eagleEyeTraceId":"0ad40c441762******2308977e0024",
 "code":"200",
 "cost":121,
 "data":{
  "proxyAdmin":{
   "proxyEntityID":"org-1036052******adf04a5000i",
   "proxyStatus":"AVAILABLE",
   "muserId":"admin",
   "proxyUser":{
    "arId":"ar-******9904",
    "displayName":"ProxyUser-orgResourceAuditor-splk",
    "roleId":4,
    "loginName":"ProxyUser-orgResourceAuditor-splk",
    "roleName":"defaultRole.organizationAdmin.name",
    "userId":6356,
    "defaultRoleId":4,
    "orgId":356,
    "orgAlias":"test",
    "orgUuid":"org-1036052******adf04a5000i"
   },
   "proxyTime":{
    "startTime":1769750313647,
    "endTime":1769836713647,
    "type":"TIME_RANGE"
   },
   "proxyEntityLevelAlias":"[ \"root\",\"test\"]",
   "proxyAdminID":"pa-1036dc8******adf0874000b",
   "description":"测试",
   "mtime":1769750319380,
   "originUser":{
    "arId":"ar-******9904",
    "displayName":"ProxyUser-orgResourceAuditor-splk",
    "roleId":4,
    "loginName":"ProxyUser-orgResourceAuditor-splk",
    "roleName":"defaultRole.organizationAdmin.name",
    "userId":6356,
    "defaultRoleId":4,
    "orgId":356,
    "orgAlias":"test",
    "orgUuid":"org-1036052******adf04a5000i"
   },
   "proxyOrganization":{
    "supportRegionList":"[\"cn-wul******223-d01\" ]",
    "level":"0.1",
    "alias":"test",
    "supportRegions":"cn-wul******223-d01",
```

`"description":"`测试数据。`",`

```json
    "parentId":1
   },
   "proxyResourceSet":{
    "organizationId":35,
    "isUserDefaultResourceSet":false,
    "gmtModified":1770028091941,
    "creator":"admin",
    "resourceGroupName":"test",
    "organizationName":"testorg",
    "gmtCreated":1770028091941,
    "modifier":"admin",
    "resourceGroupType":0,
```

`"description":"`测试数据`",`

```json
    "rsId":"rs-1036ed1******abc186f000h"
   },
   "proxyEntityType":"ORGANIZATION",
   "enable":true,
   "proxyMethod":"ASSIGN",
   "ctime":1769750315780,
   "proxyRoleArId":"ar-******9904",
   "cuserId":"admin"
  }
 },
 "success":true,
 "message":"success"
}
```

`XML` 格式

```xml
<errorKey>ascm.auth.EntityNotExist</errorKey> <eagleEyeTraceId>0ad40c441762******2308977e0024</eagleEyeTraceId> <code>200</code> <cost>121</cost> <data>
 <proxyAdmin>
  <proxyEntityID>org-1036052******adf04a5000i</proxyEntityID>
  <proxyStatus>AVAILABLE</proxyStatus>
  <muserId>admin</muserId>
  <proxyUser>
   <arId>ar-******9904</arId>
   <displayName>ProxyUser-orgResourceAuditor-splk</displayName>
   <roleId>4</roleId>
   <loginName>ProxyUser-orgResourceAuditor-splk</loginName>
   <roleName>defaultRole.organizationAdmin.name</roleName>
   <userId>6356</userId>
   <defaultRoleId>4</defaultRoleId>
   <orgId>356</orgId>
   <orgAlias>test</orgAlias>
   <orgUuid>org-1036052******adf04a5000i</orgUuid>
  </proxyUser>
  <proxyTime>
   <startTime>1769750313647</startTime>
   <endTime>1769836713647</endTime>
   <type>TIME_RANGE</type>
  </proxyTime>
  <proxyEntityLevelAlias>[ &quot;root&quot;,&quot;test&quot;]</proxyEntityLevelAlias>
  <proxyAdminID>pa-1036dc8******adf0874000b</proxyAdminID>
  <description>测试</description>
  <mtime>1769750319380</mtime>
  <originUser>
   <arId>ar-******9904</arId>
   <displayName>ProxyUser-orgResourceAuditor-splk</displayName>
   <roleId>4</roleId>
   <loginName>ProxyUser-orgResourceAuditor-splk</loginName>
   <roleName>defaultRole.organizationAdmin.name</roleName>
   <userId>6356</userId>
   <defaultRoleId>4</defaultRoleId>
   <orgId>356</orgId>
   <orgAlias>test</orgAlias>
   <orgUuid>org-1036052******adf04a5000i</orgUuid>
  </originUser>
  <proxyOrganization>
   <supportRegionList>[&quot;cn-wul******223-d01&quot; ]</supportRegionList>
   <level>0.1</level>
   <alias>test</alias>
   <supportRegions>cn-wul******223-d01</supportRegions>
```

`<description>`测试数据。`</description>`

```xml
   <parentId>1</parentId>
  </proxyOrganization>
  <proxyResourceSet>
   <organizationId>35</organizationId>
   <isUserDefaultResourceSet>false</isUserDefaultResourceSet>
   <gmtModified>1770028091941</gmtModified>
   <creator>admin</creator>
   <resourceGroupName>test</resourceGroupName>
   <organizationName>testorg</organizationName>
   <gmtCreated>1770028091941</gmtCreated>
   <modifier>admin</modifier>
   <resourceGroupType>0</resourceGroupType>
   <description>测试数据</description>
   <rsId>rs-1036ed1******abc186f000h</rsId>
  </proxyResourceSet>
  <proxyEntityType>ORGANIZATION</proxyEntityType>
  <enable>true</enable>
  <proxyMethod>ASSIGN</proxyMethod>
  <ctime>1769750315780</ctime>
  <proxyRoleArId>ar-******9904</proxyRoleArId>
  <cuserId>admin</cuserId>
 </proxyAdmin>
</data> <success>true</success> <message>success</message>
```

###### 4.1.1.4.6. GetUserInfo

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser2022 | 用户登录名。 |
| userAccessKeyId | String | Body | 否 | UyAna7V7RG****** | 用户AccessKey ID。 |
| pk | String | Body | 否 | 259258662544****** | 用户账号的主键。 |
| ascmUserId | Integer | Body | 否 | 123 | 用户的ID。 |

**说明**

入参支持填写loginName、userAccessKeyId、pk和ascmUserId参数。如果所有参数都不填写，则查询调用者自身信息，如果传入多个参数，则按照 loginName/userAccessKeyId/pk/ascmUserId顺序取一个作为实际查询参数。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 121 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| data | Struct | - | 响应结果。 |
| -roles | Array | - | 角色列表。 说明此参数已经废弃。 |
| --active | Boolean | true | 用户角色是否有效。 说明此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999999902 | 用户角色唯一编码。 |

| --code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的，自定义角色的code由系统生成。格式为：ROLE _ 英文大写的角色名称_随机串。 |
|---|---|---|---|
| --default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.resourceUser.descript ion | 用户角色的描述。 |
| --enable | Boolean | true | 用户角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --organizationVisibility | String | defaultRole.resourceUser.descript ion | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| --rAMRole | Boolean | false | 用户角色是否为RAM角色。 |
| --roleLevel | Integer | 1123 | 用户角色等级，该参数已废弃。 |
| --roleName | String | defaultRole.resourceUser.name | 用户角色名称。 |
| --roleRange | String | roleRange.resourceSet | 用户角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| --roleType | String | ROLETYPEASCM _ | 用户角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -userGroupRoles | Array | - | 用户组角色列表。 |
| --active | Boolean | true | 用户角色是否有效。 说明此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999999902 | 用户角色唯一编码。 |
| --code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的，自定义角色的code由系统生成。格式为：ROLE _ 英文大写的角色名称_随机串。 |
| --cuserId | String | admin | 用户角色创建者的用户名。 |

| --default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
|---|---|---|---|
| --description | String | defaultRole.resourceUser.descript ion | 用户角色的描述。 |
| --enable | Boolean | true | 用户角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --organizationVisibility | String | organizationVisibility.global | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| --rAMRole | Boolean | false | 用户角色是否为RAM角色。 |
| --roleLevel | Integer | 1123 | 用户角色等级，该参数已废弃。 |
| --roleName | String | defaultRole.resourceUser.name | 用户角色名称。 |
| --roleRange | String | roleRange.resourceSet | 用户角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| --roleType | String | ROLETYPEASCM _ | 用户角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -userGroups | Array | - | 用户组列表。 |
| --resourceSets | Array | - | 资源集列表。此参数已经废弃。 |
| ---creator | String | admin | 资源集创建者的用户名。 |
| ---gmtCreated | Long | 1606791494471 | 资源集创建时间。 |
| ---id | Integer | 2 | 角色ID。 |
| ---organizationID | Integer | 1 | 所属组织ID。 |
| ---resourceGroupName | String | restest _ | 资源集名称。 |
| ---rsId | String | 123121a | 资源集唯一编码。 |
| --roles | Array | - | 角色列表。此参数已经废弃。 |
| ---active | Boolean | true | 用户角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |
| ---arId | String | ar-9999999902 | 用户角色唯一编码。 |

| ---code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的. 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |
|---|---|---|---|
| ---cuserId | String | admin | 用户角色创建者的用户名。 |
| ---default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| ---description | String | defaultRole.resourceUser.descript ion | 用户角色的描述。 |
| ---enable | Boolean | true | 用户角色是否有效。 |
| ---id | Integer | 2 | 角色ID。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| ---organizationVisibility | String | organizationVisibility.global | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ---ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| ---rAMRole | Boolean | false | 用户角色是否为RAM角色。 |
| ---roleLevel | Integer | 1123 | 用户角色等级。该参数已废弃。 |
| ---roleName | String | defaultRole.resourceUser.name | 用户角色名称。 |
| ---roleRange | String | roleRange.resourceSet | 用户角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| ---roleType | String | ROLETYPEASCM _ | 用户角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| --users | Array | - | 用户列表。此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表。 |
| ---accountType | Integer | 1 | 账号类型。 该参数已废弃。 |
| ---active | Boolean | true | 用户角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |
| ---aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| ---backendAccountType | String | RamUser | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号。 RamUser：RAM子账号。 |
| ---cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ---ctime | Long | 1606791494471 | 用户创建的时间。 |

| ---default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
|---|---|---|---|
| ---defaultRoleId | Integer | 1 | 用户默认角色ID。 |
| ---deleted | Boolean | false | 用户是否已删除。 |
| ---email | String | te**@163.com | 用户邮箱地址。 |
| ---enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| ---enableEmail | Boolean | false | 是否启用邮件通知。 |
| ---enableShortMessage | Boolean | false | 是否启用短信通知。 |
| ---id | Integer | 2 | 角色ID。 |
| ---loginName | String | test | 用户登录名。 |
| ---loginTime | Long | 1606791494471 | 用户登录时间。 |
| ---mobileNationCode | String | 86 | 区号。 |
| ---mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| ---organizationId | Integer | 1 | 所属组织ID。 |
| ---ramUser | Boolean | true | 是否为RAM用户（子账号）。 |
| ---userLoginCtrlId | Integer | 34 | 登录控制ID。 |
| ---username | String | test | 用户显示名。 |
| --augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |
| --createTimeStamp | Long | 1606791494471 | 用户组创建时间。 |
| --groupName | String | testUserGroup01 | 用户组名称。 |
| --id | Integer | 2 | 角色ID。 |
| --organizationId | Integer | 1 | 所属组织ID。 |
| --organization | Struct | - | 创建的用户所属的组织信息。此参数已经废弃，若要查询用户所属组织详细信息， 请根据organizationId字段通过GetOrganization接口查询。 |
| ---supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| ---alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ---ctime | Long | 1606791494471 | 用户创建的时间。 |
| ---cuserId | String | admin | 用户角色创建者的用户名。 |
| ---id | Integer | 2 | 角色ID。 |
| ---internal | Boolean | false | 是否为预置组织。预置组织即系统自动生成的组织，也称为默认组织。 |

| ---level | String | 0.1 | 组织等级。root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
|---|---|---|---|
| ---mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |
| ---multiCloudStatus | String | master | 是否为多云同步组织。 该参数仅在多云场景下返回。 master：主云。 slave：从云。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| ---name | String | test | 组织名称。 |
| ---parentId | Integer | 0 | 父组织ID。 |
| ---supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| ---uuid | String | 1231 | 组织UUID。 |
| -userRoles | Array | - | 用户角色列表。 |
| --active | Boolean | true | 用户角色是否有效。 说明此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999999902 | 用户角色唯一编码。 |
| --code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的，自定义角色的code由系统生成。格式为：ROLE _ 英文大写的角色名称_随机串。 |
| --cuserId | String | admin | 用户角色创建者的用户名。 |
| --default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.resourceUser.descript ion | 用户角色的描述。 |
| --enable | Boolean | true | 用户角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --organizationVisibility | String | organizationVisibility.global | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| --rAMRole | Boolean | false | 用户角色是否为RAM角色。 |
| --roleLevel | Integer | 1123 | 用户角色等级，该参数已废弃。 |
| --roleName | String | defaultRole.resourceUser.name | 用户角色名称。 |

| --roleRange | String | roleRange.resourceSet | 用户角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
|---|---|---|---|
| --roleType | String | ROLETYPEASCM _ | 用户角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -cellphoneNum | String | 188****8888 | 用户手机号码。 |
| -default | Boolean | true | 用户角色是否为预置角色。 预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| -deleted | Boolean | false | 用户是否已删除。 |
| -displayName | String | testuser20220906**** | 用户显示名。 |
| -email | String | x*@163.com | 用户邮箱地址。 |
| -enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| -enableEmail | Boolean | false | 是否启用邮件通知。 |
| -enableShortMessage | Boolean | false | 是否启用短信通知。 |
| -id | Integer | 2 | 角色ID。 |
| -lastLoginTime | Long | 1730960807168 | 用户最近一次登录的时间。 说明此参数已经废弃。 |
| -loginName | String | test | 用户登录名。 |
| -mobileNationCode | String | 86 | 区号。 |
| -parentPk | String | 112715760893**** | 阿里云账号（主账号）的主键，作为账号的唯一标识。 与在ApsaraUni- manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |
| -primaryKey | String | 25925866254468**** | RAM用户（子账号）的主键，作为账号的唯一标识。 与在ApsaraUni-manager 运营控制台的用户管理中的RAM用户（子账号）一致。 |
| -status | String | ACTIVE | 用户状态。 ACTIVE：激活。 INACTIVE：禁用。 |
| -defaultRole | Struct | - | 默认角色。 用户登录时所使用的角色。 |
| --active | Boolean | true | 用户角色是否有效。 说明此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999999902 | 用户角色唯一编码。 |

| --code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的，自定义角色的code由系统生成。格式为：ROLE _ 英文大写的角色名称_随机串。 |
|---|---|---|---|
| --cuserId | String | admin | 用户角色创建者的用户名。 |
| --default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.resourceUser.descript ion | 用户角色的描述。 |
| --enable | Boolean | true | 用户角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --organizationVisibility | String | organizationVisibility.global | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| --rAMRole | Boolean | false | 用户角色是否为RAM角色。 |
| --roleLevel | Integer | 1123 | 用户角色等级，该参数已废弃。 |
| --roleName | String | defaultRole.resourceUser.name | 用户角色名称。 |
| --roleRange | String | roleRange.resourceSet | 用户角色的管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM授权所绑定的用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| --roleType | String | ROLETYPEASCM _ | 用户角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -loginPolicy | Struct | - | 用户所使用的登录策略。 |
| --ipRanges | Array | - | 登录策略IP段。 |
| ---ipRange | String | 0.0.0.0/0 | 登录策略IP范围。 |
| ---loginPolicyId | Integer | 1 | 所属登录策略的ID。 |
| ---protocol | String | IPV4 | 登录策略使用协议，仅支持IPv4。 |
| --timeRanges | Array | - | 登录策略的时间段。 |
| ---endTime | String | 24:00 | 登录策略生效时间段的结束时间。 |
| ---loginPolicyId | Integer | 1 | 所属登录策略的ID。 |

| ---startTime | String | 00:00 | 登录策略生效时间段的开始时间。 |
|---|---|---|---|
| --cuserId | String | admin | 用户角色创建者的用户名。 |
| --default | Boolean | true | 用户角色是否为预置角色。预置角色由系统自动生成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --enable | Boolean | true | 用户角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --lpId | String | lp-9999999999 | 登录策略唯一编码。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --name | String | test | 组织名称。 |
| --organizationVisibility | String | organizationVisibility.global | 用户角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 用户角色所属组织ID。 |
| --rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| -organization | Struct | - | 创建的用户所属的组织信息。此参数已经废弃，若要查询用户所属组织详细信息， 请根据organizationId 字段通过GetOrganization接口查询。 |
| --supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| --alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| --ctime | Long | 1606791494471 | 用户创建的时间。 |
| --cuserId | String | admin | 用户角色创建者的用户名。 |
| --id | Integer | 2 | 组织ID。 |
| --internal | Boolean | false | 是否为预置组织。预置组织即系统自动生成的组织，也称为默认组织。 |
| --level | String | 0.1 | 组织等级。root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| --mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |
| --multiCloudStatus | String | master | 是否为多云同步组织。该参数仅在多云场景下返回。 master：主云。 slave：从云。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --name | String | test | 组织名称。 |
| --parentId | Integer | 0 | 父组织ID。 |
| --supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| --uuid | String | 1231 | 组织UUID。 |

**示例**

请求示例

```
{ }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "redirect":"", "code":"200", "cost":121, "data":{ "cellphoneNum":"188****8888", "displayName":"testuser20220906****", "enableDingTalk":false, "defaultRole":{ "roleRange":"roleRange.resourceSet", "arId":"ar-9999999902", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"defaultRole.resourceUser.description", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.resourceUser.name", "id":2, "roleLevel":1123, "cuserId":"admin", "organizationVisibility":"defaultRole.resourceUser.description" }, "userRoles":[ { "roleRange":"roleRange.resourceSet", "arId":"ar-9999999902", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"defaultRole.resourceUser.description", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.resourceUser.name", "id":2, "roleLevel":1123, "cuserId":"admin", "organizationVisibility":"defaultRole.resourceUser.description" } ], "userGroups":[ { "roles":[ { "roleRange":"roleRange.resourceSet", "arId":"ar-9999999902", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"defaultRole.resourceUser.description", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.resourceUser.name", "id":2, "roleLevel":1123, "cuserId":"admin", "organizationVisibility":"defaultRole.resourceUser.description" } ], "organizationId":1, "users":[ { "cellphoneNum":"188****8888", "muserId":"admin", "aliyunUser":false, "backendAccountType":"RamUser" |  |

```json
      backendAccountType:RamUser,
      "enableDingTalk":false,
      "accountType":1,
      "active":true,
      "mtime":1606791494471,
      "organizationId":1,
      "default":true,
      "deleted":false,
      "loginTime":1606791494471,
      "userLoginCtrlId":34,
      "loginName":"test",
      "ctime":1606791494471,
      "id":2,
      "mobileNationCode":"86",
      "enableEmail":false,
      "ramUser":true,
      "defaultRoleId":1,
      "email":"te**@163.com",
      "enableShortMessage":false,
      "username":"test"
     }
```

`],`

```json
    "groupName":"testUserGroup01",
    "augId":"aug-101de696afc90a420d******",
    "resourceSets":[
     {
      "organizationID":1,
      "creator":"admin",
      "resourceGroupName":"res_test",
      "gmtCreated":1606791494471,
      "rsId":"123121a",
      "id":2
     }
```

`],`

```json
    "createTimeStamp":1606791494471,
    "organization":[
     {
      "muserId":"admin",
      "internal":false,
      "level":"0.1",
      "supportRegions":"cn-qingdao-****-d01",
      "mtime":1606791494471,
      "uuid":"1231",
      "parentId":0,
      "multiCloudStatus":"master",
      "supportRegionList":"[\"cn-qingdao-****-d01\"]",
      "name":"test",
      "alias":"test",
      "ctime":1606791494471,
      "id":2,
      "cuserId":"admin"
     }
```

`],`

```json
    "id":2
   }
```

`],`

```json
  "organization":{
   "muserId":"admin",
   "internal":false,
   "level":"0.1",
   "supportRegions":"cn-qingdao-****-d01",
   "mtime":1606791494471,
   "uuid":"1231",
   "parentId":0,
   "multiCloudStatus":"master",
   "supportRegionList":"[\"cn-qingdao-****-d01\"]",
   "name":"test",
   "alias":"test",
   "ctime":1606791494471,
   "id":2,
   "cuserId":"admin"
  },
  "parentPk":"112715760893****",
  "lastLoginTime":1730960807168,
  "default":true,
  "deleted":false,
  "roles":[
   {
    "roleRange":"roleRange.resourceSet",
    "arId":"ar-9999999902",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_RESOURCE_USER",
    "active":true,
    "description":"defaultRole.resourceUser.description",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
```

```json
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.resourceUser.name",
    "id":2,
    "roleLevel":1123,
    "organizationVisibility":"defaultRole.resourceUser.description"
   }
```

`],`

```json
  "userGroupRoles":[
   {
    "roleRange":"roleRange.resourceSet",
    "arId":"ar-9999999902",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_RESOURCE_USER",
    "active":true,
    "description":"defaultRole.resourceUser.description",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.resourceUser.name",
    "id":2,
    "roleLevel":1123,
    "cuserId":"admin",
    "organizationVisibility":"defaultRole.resourceUser.description"
   }
```

`],`

```json
  "loginName":"test",
  "id":2,
  "mobileNationCode":"86",
  "enableEmail":false,
  "email":"x*@163.com",
  "enableShortMessage":false,
  "primaryKey":"25925866254468****",
  "status":"ACTIVE",
  "loginPolicy":{
   "ipRanges":[
    {
     "protocol":"IPV4",
     "ipRange":"0.0.0.0/0",
     "loginPolicyId":1
    }
```

`],`

```json
   "timeRanges":[
    {
     "loginPolicyId":1,
     "startTime":"00:00",
     "endTime":"24:00"
    }
```

`],`

```json
   "muserId":"admin",
   "default":true,
   "ownerOrganizationId":1,
   "enable":true,
   "name":"test",
   "rule":"ALLOW",
   "id":2,
   "cuserId":"admin",
   "lpId":"lp-9999999999",
   "organizationVisibility":"defaultRole.resourceUser.description"
  }
 },
 "success":true,
 "pureListData":"",
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <redirect /> <code>200</code> <cost>121</cost> <data> <cellphoneNum>188****8888</cellphoneNum> <displayName>testuser20220906****</displayName> <enableDingTalk>false</enableDingTalk> <defaultRole> <roleRange>roleRange.resourceSet</roleRange> <arId>ar-9999999902</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>defaultRole.resourceUser.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> |  |

```xml
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>1123</roleLevel>
  <cuserId>admin</cuserId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </defaultRole>
 <userRoles>
  <roleRange>roleRange.resourceSet</roleRange>
  <arId>ar-9999999902</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_USER</code>
  <active>true</active>
  <description>defaultRole.resourceUser.description</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>1123</roleLevel>
  <cuserId>admin</cuserId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </userRoles>
 <userGroups>
  <roles>
   <roleRange>roleRange.resourceSet</roleRange>
   <arId>ar-9999999902</arId>
   <muserId>admin</muserId>
   <rAMRole>false</rAMRole>
   <code>ROLE_RESOURCE_USER</code>
   <active>true</active>
   <description>defaultRole.resourceUser.description</description>
   <roleType>ROLETYPE_ASCM</roleType>
   <default>true</default>
   <ownerOrganizationId>1</ownerOrganizationId>
   <enable>true</enable>
   <roleName>defaultRole.resourceUser.name</roleName>
   <id>2</id>
   <roleLevel>1123</roleLevel>
   <cuserId>admin</cuserId>
   <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
  </roles>
  <organizationId>1</organizationId>
  <users>
   <cellphoneNum>188****8888</cellphoneNum>
   <muserId>admin</muserId>
   <aliyunUser>false</aliyunUser>
   <backendAccountType>RamUser</backendAccountType>
   <enableDingTalk>false</enableDingTalk>
   <accountType>1</accountType>
   <active>true</active>
   <mtime>1606791494471</mtime>
   <organizationId>1</organizationId>
   <default>true</default>
   <deleted>false</deleted>
   <loginTime>1606791494471</loginTime>
   <userLoginCtrlId>34</userLoginCtrlId>
   <loginName>test</loginName>
   <ctime>1606791494471</ctime>
   <id>2</id>
   <mobileNationCode>86</mobileNationCode>
   <enableEmail>false</enableEmail>
   <ramUser>true</ramUser>
   <defaultRoleId>1</defaultRoleId>
   <email>te**@163.com</email>
   <enableShortMessage>false</enableShortMessage>
   <username>test</username>
  </users>
  <groupName>testUserGroup01</groupName>
  <augId>aug-101de696afc90a420d******</augId>
  <resourceSets>
   <organizationID>1</organizationID>
   <creator>admin</creator>
   <resourceGroupName>res_test</resourceGroupName>
   <gmtCreated>1606791494471</gmtCreated>
   <rsId>123121a</rsId>
   <id>2</id>
  </resourceSets>
  <createTimeStamp>1606791494471</createTimeStamp>
  <organization>
   <muserId>admin</muserId>
   <internal>false</internal>
   <level>0.1</level>
```

i i d

```
****d01/
```

i

```xml
   <supportRegions>cn-qingdao-****-d01</supportRegions>
   <mtime>1606791494471</mtime>
   <uuid>1231</uuid>
   <parentId>0</parentId>
   <multiCloudStatus>master</multiCloudStatus>
   <supportRegionList>[&quot;cn-qingdao-****-d01&quot;]</supportRegionList>
   <name>test</name>
   <alias>test</alias>
   <ctime>1606791494471</ctime>
   <id>2</id>
   <cuserId>admin</cuserId>
  </organization>
  <id>2</id>
 </userGroups>
 <organization>
  <muserId>admin</muserId>
  <internal>false</internal>
  <level>0.1</level>
  <supportRegions>cn-qingdao-****-d01</supportRegions>
  <mtime>1606791494471</mtime>
  <uuid>1231</uuid>
  <parentId>0</parentId>
  <multiCloudStatus>master</multiCloudStatus>
  <supportRegionList>[&quot;cn-qingdao-****-d01&quot;]</supportRegionList>
  <name>test</name>
  <alias>test</alias>
  <ctime>1606791494471</ctime>
  <id>2</id>
  <cuserId>admin</cuserId>
 </organization>
 <parentPk>112715760893****</parentPk>
 <lastLoginTime>1730960807168</lastLoginTime>
 <default>true</default>
 <deleted>false</deleted>
 <roles>
  <roleRange>roleRange.resourceSet</roleRange>
  <arId>ar-9999999902</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_USER</code>
  <active>true</active>
  <description>defaultRole.resourceUser.description</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>1123</roleLevel>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </roles>
 <userGroupRoles>
  <roleRange>roleRange.resourceSet</roleRange>
  <arId>ar-9999999902</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_USER</code>
  <active>true</active>
  <description>defaultRole.resourceUser.description</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>1123</roleLevel>
  <cuserId>admin</cuserId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </userGroupRoles>
 <loginName>test</loginName>
 <id>2</id>
 <mobileNationCode>86</mobileNationCode>
 <enableEmail>false</enableEmail>
 <email>x*@163.com</email>
 <enableShortMessage>false</enableShortMessage>
 <primaryKey>25925866254468****</primaryKey>
 <status>ACTIVE</status>
 <loginPolicy>
  <ipRanges>
   <protocol>IPV4</protocol>
   <ipRange>0.0.0.0/0</ipRange>
   <loginPolicyId>1</loginPolicyId>
  </ipRanges>
  <timeRanges>
   <loginPolicyId>1</loginPolicyId>
   <startTime>00:00</startTime>
   <endTime>24:00</endTime>
```

```xml
  </timeRanges>
  <muserId>admin</muserId>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <name>test</name>
  <rule>ALLOW</rule>
  <id>2</id>
  <cuserId>admin</cuserId>
  <lpId>lp-9999999999</lpId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </loginPolicy>
</data> <success>true</success> <pureListData /> <message>success</message>
```

ascm 2019-05-10

###### 4.1.1.4.7. ActivateUser

激活用户时，系统将自动激活用户所有的AccessKey。企业版v3.12.0版本自SP016后开始支持此接口。企业版v3.14.0版本自SP013后开始支持此接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser | 待激活用户的登录名。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 114 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 用户信息。 |

| accessKeys | Array of accessKey |  | Accesskey列表。 |
|---|---|---|---|
| accessKey |  |  |  |
| accesskeyId | String | tCr5mJhpjo****** | AccesskeyID。 |
| ctime | Long | 1606675230000 | Accesskey的创建时间。 |
| cuserId | String | admin | Accesskey创建者的用户名。 |
| id | Integer | 1 | AccessKey的识别主键。 说明此参数已经废弃。 |
| region | String | cn-qingdao-****-d01 | AccessKey的可用区。 |
| status | String | ACTIVE | AccessKey是否启用。 ACTIVE：启用。 INACTIVE：禁用。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 说明初始化自动创建的用户是预置用户，创建场景下此字段默认为false。 |
| defaultRole | Struct |  | 默认角色。 说明用户登录后的当前角色。 |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色状态以enable参数为准。 |
| arId | String | ar-999999*** | 角色唯一编码。 |
| code | String | ROLEORGANIZATIONADMIN _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明 -内置角色code是固定的。 -自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.organizationAdmin.de scription | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 true：有效。 false：无效。 |
| id | Integer | 4 | 角色ID。 |
| muserId | String | 3 | 角色最近一次修改的修改者ID。 |

|  | 串 |
|---|---|

| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明此参数无实际作用。 |
| roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| deleted | Boolean | false | 用户是否已被删除，已删除的用户为历史用户。 true：已经被删除。 false：未被删除。 |
| displayName | String | testuser202209071758 | 用户显示名。 |
| email | String | test@test.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | true | 是否启用钉钉通知。 |
| enableEmail | Boolean | true | 是否启用邮件通知。 |
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 5817 | 用户ID。 |
| lastLoginTime | Long | 1657608949009 | 用户最近一次登录的时间。 说明此参数已经废弃。 |
| loginName | String | testuser202209071758 | 用户登录名。 |
| loginPolicy | Struct |  | 用户绑定的登录策略。 |
| cuserId | String | test | 创建登录策略的用户名称说明此参数已经废弃。 |
| default | Boolean | false | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |

| id | Integer | 1084 | 登录策略ID。 |
|---|---|---|---|
| ipRanges | Array of ipRange |  | 登录策略IP段。 |
| ipRange |  |  |  |
| ipRange | String | 10.48.16.1/24 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| protocol | String | IPV4 | 登录策略使用的协议，仅支持IPv4。 |
| lpId | String | lp-101de13d33320a420d****** | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 登录策略名称。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 登录策略所属组织ID。 |
| rule | String | DENY | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略的时间段。 |
| timeRange |  |  |  |
| endTime | String | 18:00 | 结束时间。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| startTime | String | 08:00 | 开始时间。 |
| mobileNationCode | String | 86 | 国际区号。 |
| organization | Struct |  | 用户所属的组织。 |
| alias | String | sub-org-1 | 组织别名。 |
| ctime | Long | 1657608949009 | 组织的创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| id | Integer | 25 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 |
| level | String | 0.1.24 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织leve |
| mtime | Long | 1657608949009 | 组织最近一次修改的时间。 |

| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
|---|---|---|---|
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | sub-org-1 | 组织名称。 |
| parentId | Integer | 24 | 父组织ID。 |
| supportRegionList | List | ["cn-***-d01"] | 可用区列表。 |
| supportRegions | String | cn-***-d01 | 可用区列表。 说明此参数已经废弃。 |
| uuid | String | org- 101cc0654e910a420927000w | 组织UUID。 |
| parentPk | String | 1127157608****** | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |
| primaryKey | String | 259258662544****** | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号） 一致。 |
| roles | Array of role |  | 用户拥有的角色列表。 |
| role |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| arId | String | ar-9999****** | 角色唯一编码。 |
| code | String | ROLEORGANIZATIONADMIN _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明 -内置角色code是固定的。 -自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |
| cuserId | String | admin | 角色创建者的用户名。 |
| default | Boolean | false | 角色创建者的用户名。 |
| description | String | defaultRole.organizationAdmin.de scription | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |

|  | 串 |
|---|---|

| enable | Boolean | false | 角色是否有效。 |
|---|---|---|---|
| id | Integer | 4 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| status | String | ACTIVE | 用户状态。 active:激活。 inactive:禁用。 说明用户创建后状态默认为active。 |
| userGroupRoles | Array of userGroupRole |  | 用户所属用户组所拥有的角色列表。 说明可通过调用AddUsersToUserGroup接口将用户添加到用户组。 |
| userGroupRole |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| arId | String | ar-9999****** | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明 -内置角色code是固定的。 -自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |

|  | 串 |
|---|---|

| cuserId | String | admin | 角色创建者的用户名。 |
|---|---|---|---|
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 2 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| userGroups | Array of userGroup |  | 用户所属用户组列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |
| userGroup |  |  |  |
| augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |
| createTimeStamp | Long | 1657608949009 | 用户组创建时间。 说明此参数已经废弃。 |
| groupName | String | testUserGroup01 | 用户组名称。 |
| id | Integer | 145 | 用户组ID。 |

| organization | Struct |  | 创建的用户所属的组织信息。 说明此参数已经废弃，若要查询用户组所属组织详细信息，可通过调用 GetOrganization接口查询。 |
|---|---|---|---|
| alias | String | sub-org-1 | 组织别名。 |
| ctime | Long | 1657608949009 | 创建时间。 |
| cuserId | String | admin | 创建组织的用户名称。 |
| id | Integer | 25 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 |
| level | String | 0.1.24 | 组织等级。 |
| mtime | Long | 1657608949009 | 组织最后一次更新时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | sub-org-1 | 组织名称。 |
| parentId | Integer | 24 | 父组织ID。 |
| supportRegionList | List | ["cn-***-d01"] | 可用区列表。 说明此参数已经废弃。 |
| supportRegions | String | cn-***-d01 | 可用区列表。 说明此参数已经废弃。 |
| uuid | String | org- 101cc0654e910a420927000w | 组织UUID。 |
| organizationId | Integer | 24 | 用户组所属组织的ID。 |
| resourceSets | Array of resourceSet |  | 资源集列表。 说明此参数已经废弃。 |
| resourceSet |  |  |  |
| creator | String | admin | 资源集创建者的用户名。 |
| gmtCreated | Long | 1606791494471 | 资源集创建时间。 |
| id | Integer | 2 | 资源集ID。 |

| organizationID | Integer | 1 | 资源集所属组织的ID。 |
|---|---|---|---|
| resourceGroupName | String | resourcetest _ | 资源集名称。 |
| rsId | String | 123456 | 资源集唯一编码。 |
| roles | Array of role |  | 用户组角色列表。 说明此参数已经废弃。 |
| role |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色状态以enable字段为准。 |
| arId | String | ar-9999****** | 角色唯一编码。 |
| code | String | ROLERESOURCESETADMIN _ _ _ | 角色Code。 |
| cuserId | String | admin | 角色创建者。 |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.resourceSetAdmin.de scription | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 5 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际意义。 |
| roleName | String | defaultRole.resourceSetAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |

| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
|---|---|---|---|
| users | Array of user |  | 用户列表。 说明此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表。 |
| user |  |  |  |
| accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| active | Boolean | true | 用户是否有效。 |
| aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| backendAccountType | String | RamUser | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号（主账号）。 RamUser：RAM用户（子账号）。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ctime | Long | 1606791494471 | 用户创建时间。 |
| default | Boolean | false | 是否是预置用户。 |
| defaultRoleId | Integer | 2 | 用户默认角色ID。 |
| deleted | Boolean | false | 用户是否已删除。 |
| email | String | test@test.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | true | 是否启用钉钉通知。 |
| enableEmail | Boolean | true | 用户邮箱地址。 |
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 5817 | 用户ID。 |
| loginName | String | testuser202209071758 | 用户登录名。 |
| loginTime | Long | 1657608949009 | 用户登录时间。 |
| mobileNationCode | String | 86 | 区号。 |
| mtime | Long | 1657608949009 | 用户最近一次修改的时间。 |
| muserId | String | admin | 用户最近一次修改的修改者用户名。 |
| organizationId | Integer | 25 | 用户所属组织的ID。 |
| password | String | 1A*******zZ | 用户密码。 |

| ramUser | Boolean | false | 是否为RAM用户（子账号）。 |
|---|---|---|---|
| userLoginCtrlId | Integer | 1 | 登录策略ID。 |
| username | String | testuser202209071758 | 用户显示名。 |
| userRoles | Array of userRole |  | 用户角色列表，用户关联的角色列表。 |
| userRole |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| arId | String | ar-9999999902 | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明 -内置角色code是固定的。 -自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |
| cuserId | String | admin | 角色创建者的用户名。 说明此参数已经废弃。 |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 2 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际作用。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |

|  | 串 |
|---|---|

| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
|---|---|---|---|
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | true | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "loginName":"testuser"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>true</redirect> <cost>114</cost> <code>200</code> <data> <cellphoneNum>188****8888</cellphoneNum> <enableDingTalk>true</enableDingTalk> <displayName>testuser202209071758</displayName> <parentPk>1127157608******</parentPk> <lastLoginTime>1657608949009</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>testuser202209071758</loginName> <mobileNationCode>86</mobileNationCode> <id>5817</id> <enableEmail>true</enableEmail> <enableShortMessage>true</enableShortMessage> <email>test@test.com</email> <status>ACTIVE</status> <primaryKey>259258662544******</primaryKey> <userGroupRoles> <roleRange>roleRange.resourceSet</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>ar-9999******</arId> <code>ROLE_RESOURCE_USER</code> <description>defaultRole.resourceUser.description</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <roleLevel>2147483647</roleLevel> <id>2</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> |  |

```xml
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>24</organizationId>
        <groupName>testUserGroup01</groupName>
        <augId>aug-101de696afc90a420d******</augId>
        <createTimeStamp>1657608949009</createTimeStamp>
        <id>145</id>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>resource_test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123456</rsId>
            <id>2</id>
        </resourceSets>
        <users>
            <cellphoneNum>188****8888</cellphoneNum>
            <muserId>admin</muserId>
            <aliyunUser>false</aliyunUser>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>true</enableDingTalk>
            <accountType>1</accountType>
            <active>true</active>
            <mtime>1657608949009</mtime>
            <organizationId>25</organizationId>
            <password>1A*******zZ</password>
            <default>false</default>
            <loginTime>1657608949009</loginTime>
            <deleted>false</deleted>
            <userLoginCtrlId>1</userLoginCtrlId>
            <loginName>testuser202209071758</loginName>
            <ctime>1606791494471</ctime>
            <mobileNationCode>86</mobileNationCode>
            <id>5817</id>
            <ramUser>false</ramUser>
            <enableEmail>true</enableEmail>
            <enableShortMessage>true</enableShortMessage>
            <email>test@test.com</email>
            <defaultRoleId>2</defaultRoleId>
            <username>testuser202209071758</username>
        </users>
        <roles>
            <roleRange>roleRange.resourceSet</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>ar-9999******</arId>
            <code>ROLE_RESOURCE_SET_ADMIN</code>
            <description>defaultRole.resourceSetAdmin.description</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>true</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>defaultRole.resourceSetAdmin.name</roleName>
            <roleLevel>2147483647</roleLevel>
            <id>5</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
        <organization>
            <muserId>admin</muserId>
            <internal>false</internal>
            <multiCloudStatus>master</multiCloudStatus>
            <level>0.1.24</level>
            <name>sub-org-1</name>
            <supportRegions>cn-***-d01</supportRegions>
            <ctime>1657608949009</ctime>
            <alias>sub-org-1</alias>
            <id>25</id>
            <mtime>1657608949009</mtime>
            <uuid>org-101cc0654e910a420927000w</uuid>
            <cuserId>admin</cuserId>
            <parentId>24</parentId>
            <supportRegionList>["cn-***-d01"]</supportRegionList>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999999902</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>defaultRole.resourceUser.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
```

/

```xml
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>2</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>tCr5mJhpjo******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <description>defaultRole.organizationAdmin.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>false</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>4</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>3</muserId>
        <arId>ar-999999***</arId>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <description>defaultRole.organizationAdmin.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>4</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>mytest</name>
        <rule>DENY</rule>
        <id>1084</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>lp-101de13d33320a420d******</lpId>
        <cuserId>test</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>10.48.16.1/24</ipRange>
            <loginPolicyId>1084</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>08:00</startTime>
            <loginPolicyId>1084</loginPolicyId>
            <endTime>18:00</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <multiCloudStatus>master</multiCloudStatus>
        <level>0.1.24</level>
        <name>sub-org-1</name>
        <supportRegions>cn-***-d01</supportRegions>
        <ctime>1657608949009</ctime>
        <alias>sub-org-1</alias>
        <id>25</id>
        <mtime>1657608949009</mtime>
        <uuid>org-101cc0654e910a420927000w</uuid>
        <cuserId>admin</cuserId>
<parentId>24</parentId>
```

```xml
        <parentId>24</parentId>
        <supportRegionList>["cn-***-d01"]</supportRegionList>
    </organization>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": true, "cost": 114, "code": 200, "data": { "cellphoneNum": "188****8888", "enableDingTalk": true, "displayName": "testuser202209071758", "parentPk": "1127157608******", "lastLoginTime": 1657608949009, "default": false, "deleted": false, "loginName": "testuser202209071758", "mobileNationCode": 86, "id": 5817, "enableEmail": true, "enableShortMessage": true, "email": "test@test.com", "status": "ACTIVE", "primaryKey": "259258662544******", "userGroupRoles": { "roleRange": "roleRange.resourceSet", "rAMRole": false, "muserId": "admin", "arId": "ar-9999******", "code": "ROLE_RESOURCE_USER", "description": "defaultRole.resourceUser.description", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceUser.name", "roleLevel": 2147483647, "id": 2, "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "userGroups": { "organizationId": 24, "groupName": "testUserGroup01", "augId": "aug-101de696afc90a420d******", "createTimeStamp": 1657608949009, "id": 145, "resourceSets": { "organizationID": 1, "creator": "admin", "resourceGroupName": "resource_test", "gmtCreated": 1606791494471, "rsId": 123456, "id": 2 }, "users": { "cellphoneNum": "188****8888", "muserId": "admin", "aliyunUser": false, "backendAccountType": "RamUser", "enableDingTalk": true, "accountType": 1, "active": true, "mtime": 1657608949009, "organizationId": 25, "password": "1A*******zZ", "default": false, "loginTime": 1657608949009, "deleted": false, "userLoginCtrlId": 1, "loginName": "testuser202209071758", "ctime": 1606791494471, "mobileNationCode": 86, "id": 5817, "ramUser": false, "enableEmail": true, "enableShortMessage": true, "email": "test@test.com", "defaultRoleId": 2, "username": "testuser202209071758" }, |  |

,

```json
            "roles": {
                "roleRange": "roleRange.resourceSet",
                "rAMRole": false,
                "muserId": "admin",
                "arId": "ar-9999******",
                "code": "ROLE_RESOURCE_SET_ADMIN",
                "description": "defaultRole.resourceSetAdmin.description",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": true,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "defaultRole.resourceSetAdmin.name",
                "roleLevel": 2147483647,
                "id": 5,
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            },
            "organization": {
                "muserId": "admin",
                "internal": false,
                "multiCloudStatus": "master",
                "level": "0.1.24",
                "name": "sub-org-1",
                "supportRegions": "cn-***-d01",
                "ctime": 1657608949009,
                "alias": "sub-org-1",
                "id": 25,
                "mtime": 1657608949009,
                "uuid": "org-101cc0654e910a420927000w",
                "cuserId": "admin",
                "parentId": 24,
                "supportRegionList": "[\"cn-***-d01\"]"
            }
        },
        "userRoles": {
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999999902",
            "code": "ROLE_RESOURCE_USER",
            "description": "defaultRole.resourceUser.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "roleLevel": 2147483647,
            "id": 2,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "accessKeys": {
            "ctime": 1606675230000,
            "id": 1,
            "region": "cn-qingdao-****-d01",
            "cuserId": "admin",
            "status": "ACTIVE",
            "accesskeyId": "tCr5mJhpjo******"
        },
        "roles": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_ORGANIZATION_ADMIN",
            "description": "defaultRole.organizationAdmin.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": false,
            "ownerOrganizationId": 1,
            "enable": false,
            "roleName": "defaultRole.organizationAdmin.name",
            "roleLevel": 2147483647,
            "id": 4,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "defaultRole": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "muserId": 3,
            "arId": "ar-999999***",
            "code": "ROLE_ORGANIZATION_ADMIN",
            "description": "defaultRole.organizationAdmin.description",
"active":true
```

```json
            active: true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "roleLevel": 2147483647,
            "id": 4,
            "organizationVisibility": "organizationVisibility.global"
        },
        "loginPolicy": {
            "muserId": "admin",
            "default": false,
            "ownerOrganizationId": 1,
            "enable": true,
            "name": "mytest",
            "rule": "DENY",
            "id": 1084,
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "lp-101de13d33320a420d******",
            "cuserId": "test",
            "ipRanges": {
                "protocol": "IPV4",
                "ipRange": "10.48.16.1/24",
                "loginPolicyId": 1084
            },
            "timeRanges": {
                "startTime": "08:00",
                "loginPolicyId": 1084,
                "endTime": "18:00"
            }
        },
        "organization": {
            "muserId": "admin",
            "internal": false,
            "multiCloudStatus": "master",
            "level": "0.1.24",
            "name": "sub-org-1",
            "supportRegions": "cn-***-d01",
            "ctime": 1657608949009,
            "alias": "sub-org-1",
            "id": 25,
            "mtime": 1657608949009,
            "uuid": "org-101cc0654e910a420927000w",
            "cuserId": "admin",
            "parentId": 24,
            "supportRegionList": "[\"cn-***-d01\"]"
        }
    },
    "success": true,
    "message": "success"
}
```

###### 4.1.1.4.8. AddUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 是 | testuser2022 | 用户登录名，由大小写英文字母、数字、下划线 （_）、短划线（-）、半角句号（.）组成，长度为2~64个字符。该参数为必填。 |
| displayName | String | Body | 是 | testuser2022 | 用户显示名，由大小写英文字母、中文、数字、 短划线（-）、半角句号（.）、at（@）组成， 长度为1~128个字符。该参数为必填。 |
| password | String | Body | 否 | Pwd***** | 设置登录密码，需要满足平台配置的密码强度要求。 |
| passwordResetReq uired | Boolean | Body | 否 | true | 用户在下次登录时是否必须重置密码，默认 true。必须传入password字段，才会使用此配置。 |
| roleIdList | RepeatList | Body | 否 | [2,4] | 角色ID列表。可通过调用ListActiveRoles接口获取，如果创建用户时不指定角色，则用户角色默认为资源使用人。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginPolicyId | Integer | Body | 否 | 1 | 用户需要使用的登录策略ID，可通过调用 ListLoginPolicies接口获取。不传入时，指定的是默认策略。 |
| organizationId | Integer | Body | 是 | 60 | 用户所属组织的ID。可通过调用 GetOrganizationList接口获取。该参数为必填。 |
| organizationUuid | String | Body | 否 | lg-123456789 | 组织UUID。可通过调用GetOrganization接口获取。 |
| mobileNationCode | String | Body | 是 | 86 | 用户手机号码的国际区号。该参数为必填。 |
| cellphoneNum | String | Body | 是 | 188****8888 | 用户手机号码。该参数为必填。 |
| telephoneNum | String | Body | 否 | 11111111 | 用户座机号码。 |
| email | String | Body | 是 | test@example.com | 用户邮箱地址。该参数为必填。 |
| dingTalkToken | String | Body | 否 | zxcvbnm | 钉钉密钥。创建用户时指定的自定义钉钉机器人的加签名密钥。 |
| enableDingTalk | Boolean | Body | 否 | false | 是否启用钉钉通知。 |
| enableShortMessa ge | Boolean | Body | 否 | false | 是否启用短信通知。 |
| enableEmail | Boolean | Body | 否 | false | 是否启用邮件通知。 |
| multiCloudStatus | String | Body | 否 | null | 是否为多云同步用户，默认为null。 master：主云 slave：从云。 null。 |
| sendTunnel | String | Body | 否 | email | 发送通知的方式： email：邮箱 |
| mark | String | Body | 否 | sso | 用户标识，当前仅支持SSO。用户通过单点登录方式登录过就会显示该标识。 |
| enableConsoleLogi n | Boolean | Body | 否 | true | 是否启用控制台访问。 默认值：true |
| enableAccessKeyU se | Boolean | Body | 否 | true | 创建用户时是否创建AccessKey。 默认值： true |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |
| cost | Integer | 594 | 接口耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 该参数已废弃。 |
| redirect | Boolean | false | 该参数已废弃。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| data | Struct | - | 用户信息。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -accessKeys | Array | - | AccessKey信息列表。 说明只有平台管理员才能获取到系统预置用户的 AccessKey和AccessKeySecret。 |
| --accesskeyId | String | tCr5mJhpjo****** | 用户的AccessKey ID。 |
| --accesskeySecret | String | CqHL********** | 用户的AccessKey Secret。 |
| --ctime | Long | 1606791494471 | 用户创建时间。 |
| --id | Integer | 2 | 角色ID。 |
| --region | String | cn-qingdao-****-d01 | AccessKey的可用区。 |
| --status | String | active | 用户状态。 用户创建后默认为active。 active：激活。 inactive：禁用。 |
| -roles | Array | - | 角色列表。 |
| --active | Boolean | true | 角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999****** | 角色唯一编码。 |
| --code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | roletest _ | 角色描述。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| --organizationVisibility | String | defaultRole.resourceUser.descript ion | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| --rAMRole | Boolean | false | 是否为RAM角色。 |
| --roleLevel | Integer | 2147483647 | 角色等级。该字段无实际作用。 |
| --roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| --roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |  |
|---|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |  |
| -userGroupRoles | Array | - | 用户所属用户组所拥有的角色列表。 |  |
| --active | Boolean | true | 角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |  |
| --arId | String | ar-9999****** | 角色唯一编码。 |  |
| --code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |  |
| --cuserId | String | admin | 角色创建者。此参数已经废弃。 |  |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |
| --description | String | roletest _ | 角色描述。 |  |
| --enable | Boolean | true | 角色是否有效。 |  |
| --id | Integer | 2 | 角色ID。 |  |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |  |
| --organizationVisibility | String | defaultRole.resourceUser.descript ion | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |
| --ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |  |
| --rAMRole | Boolean | false | 是否为RAM角色。 |  |
| --roleLevel | Integer | 2147483647 | 角色等级。该字段无实际作用。 |  |
| --roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |
| --roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |  |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |
| -userGroups | Array | - | 用户所属用户组列表。可通过调用AddUsersToUserGroup接口将用户添加到用户组。 |  |
| --resourceSets | Array | - | 资源集列表。此参数已经废弃。 |  |
| ---creator | String | admin | 资源集创建者的用户名。 |  |
| ---gmtCreated | Long | 1606791494471 | 资源集创建时间。 |  |
| ---id | Integer | 2 | 角色ID。 |  |
| ---organizationID | Integer | 1 | 资源集所属组织的ID。 |  |
| ---resourceGroupName | String | restest _ | 资源集名称。 |  |

| 参数名称 | 类型 | 示例 | 说明 |  |
|---|---|---|---|---|
| ---rsId | String | 12312a | 资源集唯一编码。 |  |
| --roles | Array | - | 角色列表。此参数已经废弃。 |  |
| ---active | Boolean | true | 角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |  |
| ---arId | String | ar-9999****** | 角色唯一编码。 |  |
| ---code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |  |
| ---cuserId | String | admin | 角色创建者。 说明此参数已经废弃。 |  |
| ---default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |
| ---description | String | roletest _ | 角色描述。 |  |
| ---enable | Boolean | true | 角色是否有效。 |  |
| ---id | Integer | 2 | 角色ID。 |  |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |  |
| ---organizationVisibility | String | defaultRole.resourceUser.descript ion | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |
| ---ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |  |
| ---rAMRole | Boolean | false | 是否为RAM角色。 |  |
| ---roleLevel | Integer | 2147483647 | 角色等级。该字段无实际作用。 |  |
| ---roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |
| ---roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |  |
| ---roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |
| --users | Array | - | 用户列表。此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表。 |  |
| ---accountType | Integer | 1 | 账号类型。该参数已废弃。 |  |
| ---active | Boolean | true | 角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |  |
| ---aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |  |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---backendAccountType | String | RamUser | 后端映射账号类型： AscmUser为ASCM对客户可见的用户。 AliyunUser为阿里云账号。 RamUser为RAM子账号。 |
| ---cellphoneNum | String | 1888888**** | 用户手机号码。 |
| ---ctime | Long | 1606791494471 | 用户创建时间。 |
| ---default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| ---defaultRoleId | Integer | 1 | 用户默认角色ID。 |
| ---deleted | Boolean | false | 用户是否已删除。 |
| ---email | String | te**@163.com | 用户邮箱地址。 |
| ---enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| ---enableEmail | Boolean | false | 是否启用邮件通知。 |
| ---enableShortMessage | Boolean | false | 是否启用短信通知。 |
| ---id | Integer | 2 | 角色ID。 |
| ---loginName | String | test | 用户登录名。 |
| ---loginTime | Long | 1606791494471 | 用户登录时间。 |
| ---mobileNationCode | String | 86 | 用户手机号码的国际区号。 |
| ---mtime | Long | 1606791494471 | 用户最近一次修改的时间。 说明创建场景下该参数返回值与创建时间相同。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| ---organizationId | Integer | 1 | 用户所属组织的ID。 |
| ---password | String | H2xWNY8oitAhxMWLhtyjs******** | 初始密码系统自动生成。初次登录需要修改初始密码。 |
| ---ramUser | Boolean | true | 是否为RAM用户（子账号）。 |
| ---userLoginCtrlId | Integer | 34 | 用户所使用登录策略的ID。 |
| ---username | String | test | 用户显示名。 |
| --augId | String | aug-101de5c6c0e20a420****** | 用户组唯一编码。 |
| --createTimeStamp | Long | 1606791494471 | 用户组创建时间。此参数已经废弃。 |
| --groupName | String | testUserGroup | 用户组名称。 |
| --id | Integer | 2 | 角色ID。 |
| --organizationId | Integer | 1 | 用户所属组织的ID。 |
| --organization | Struct | - | 创建的用户所属的组织信息。此参数已经废弃，若要查询用户组所属组织详细信息，请根据organizationId字段通过调用GetOrganization接口查询。 |
| ---supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---alias | String | sub-org-1 | 组织别名。系统自动生成，一般与组织名称一致。 |
| ---ctime | Long | 1606791494471 | 用户创建时间。 |
| ---cuserId | String | admin | 角色创建者。 说明此参数已经废弃。 |
| ---id | Integer | 2 | 角色ID。 |
| ---internal | Boolean | false | 是否为预置组织。 |
| ---level | String | 0.1.24 | 组织等级。 |
| ---mtime | Long | 1606791494471 | 用户最近一次修改的时间。 说明创建场景下该参数返回值与创建时间相同。 |
| ---multiCloudStatus | String | master | 是否为多云同步组织，仅在多云状态下返回。 master为主云。 slave为从云。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| ---name | String | sub-org-1 | 组织名称。 |
| ---parentId | Integer | 24 | 父组织ID。 |
| ---supportRegions | String | cn-qingdao-****-d01 | 可用区列表。该参数已废弃。 |
| ---uuid | String | org- 101cc0654e910a420927000w | 组织UUID。 |
| -userRoles | Array | - | 用户角色列表，用户关联的角色列表，由请求参数roleIdList指定。 |
| --active | Boolean | true | 角色是否有效。此参数已经废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999****** | 角色唯一编码。 |
| --code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。 自定义角色的code由系统生成。格式为：ROLE _英文大写的角色名称_随机串。 |
| --cuserId | String | admin | 角色创建者。此参数已经废弃。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | roletest _ | 角色描述。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| --organizationVisibility | String | defaultRole.resourceUser.descript ion | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| --rAMRole | Boolean | false | 是否为RAM角色。 |
| --roleLevel | Integer | 2147483647 | 角色等级。该字段无实际作用。 |

| 参数名称 | 类型 | 示例 | 说明 |  |
|---|---|---|---|---|
| --roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |
| --roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 roleRange.rawRamRole：RAM角色授权创建的RAM Role。 |  |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |
| -cellphoneNum | String | 1888888**** | 用户手机号码。 |  |
| -default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |
| -deleted | Boolean | false | 用户是否已删除。 |  |
| -displayName | String | testuser2022 | 用户显示名。 |  |
| -email | String | te**@163.com | 用户邮箱地址。 |  |
| -enableDingTalk | Boolean | false | 是否启用钉钉通知。 |  |
| -enableEmail | Boolean | false | 是否启用邮件通知。 |  |
| -enableShortMessage | Boolean | false | 是否启用短信通知。 |  |
| -id | Integer | 2 | 角色ID。 |  |
| -loginName | String | test | 用户登录名。 |  |
| -enableConsoleLogin | Boolean | false | 是否启用控制台访问。 |  |
| -parentPk | String | 149595785389**** | 阿里云账号（主账号）的主键，作为账号的唯一标识。 与在ApsaraUni- manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |  |
| -primaryKey | String | 27365016246143**** | RAM用户（子账号）的主键，作为账号的唯一标识。与在ApsaraUni-manager 运营控制台的用户管理中的RAM用户（子账号）一致。 |  |
| -status | String | active | 用户状态。 active：激活。 inactive：禁用。 说明用户创建后默认为active。 |  |
| -loginPolicy | Struct | - | 登录策略。 |  |
| --ipRanges | Array | - | 登录策略的IP段。 |  |
| ---ipRange | String | 0.0.0.0/0 | 登录策略的IP范围。 |  |
| ---loginPolicyId | Integer | 1 | 所属登录策略ID。 |  |
| ---protocol | String | IPV4 | 登录策略所使用的IP协议，目前仅支持IPv4。 |  |
| --timeRanges | Array | - | 登录策略的时间段。 |  |
| ---endTime | String | 24:00 | 结束时间。 |  |
| ---loginPolicyId | Integer | 1 | 所属登录策略ID。 |  |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---startTime | String | 00:00 | 开始时间。 |
| --cuserId | String | admin | 角色创建者。此参数已经废弃。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --lpId | String | lp-9999****** | 登录策略唯一编码。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| --name | String | sub-org-1 | 组织名称。 |
| --organizationVisibility | String | defaultRole.resourceUser.descript ion | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| --rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |

**示例**

请求示例

```json
{ "loginName":"testuser2022", "displayName":"testuser2022", "email":"test@example.com", "organizationId":"60", "mobileNationCode":"86", "cellphoneNum":"188****8888" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"ROLE_RESOURCE_USER", "cost":594, "data":{ "cellphoneNum":"1888888****", "displayName":"testuser2022", "enableDingTalk":false, "userRoles":[ { "roleRange":"roleRange.orgAndSubOrgs", "arId":"ar-9999******", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"role_test", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.resourceUser.name", "id":2, "roleLevel":2147483647, "cuserId":"admin", "organizationVisibility":"defaultRole.resourceUser.description" } ], "userGroups":[ { |  |

```json
   {
    "roles":[
     {
      "roleRange":"roleRange.orgAndSubOrgs",
      "arId":"ar-9999******",
      "muserId":"admin",
      "rAMRole":false,
      "code":"ROLE_RESOURCE_USER",
      "active":true,
      "description":"role_test",
      "roleType":"ROLETYPE_ASCM",
      "default":true,
      "ownerOrganizationId":1,
      "enable":true,
      "roleName":"defaultRole.resourceUser.name",
      "id":2,
      "roleLevel":2147483647,
      "cuserId":"admin",
      "organizationVisibility":"defaultRole.resourceUser.description"
     }
```

`],`

```json
    "organizationId":1,
    "users":[
     {
      "cellphoneNum":"1888888****",
      "muserId":"admin",
      "aliyunUser":false,
      "backendAccountType":"RamUser",
      "enableDingTalk":false,
      "accountType":1,
      "active":true,
      "mtime":1606791494471,
      "organizationId":1,
      "default":true,
      "password":"H2xWNY8oitAhxMWLhtyjs********",
      "deleted":false,
      "loginTime":1606791494471,
      "userLoginCtrlId":34,
      "loginName":"test",
      "ctime":1606791494471,
      "id":2,
      "mobileNationCode":"86",
      "enableEmail":false,
      "ramUser":true,
      "defaultRoleId":1,
      "email":"te**@163.com",
      "enableShortMessage":false,
      "username":"test"
     }
```

`],`

```json
    "groupName":"testUserGroup",
    "augId":"aug-101de5c6c0e20a420******",
    "resourceSets":[
     {
      "organizationID":1,
      "creator":"admin",
      "resourceGroupName":"res_test",
      "gmtCreated":1606791494471,
      "rsId":"12312a",
      "id":2
     }
```

`],`

```json
    "createTimeStamp":1606791494471,
    "organization":[
     {
      "muserId":"admin",
      "internal":false,
      "level":"0.1.24",
      "supportRegions":"cn-qingdao-****-d01",
      "mtime":1606791494471,
      "uuid":"org-101cc0654e910a420927000w",
      "parentId":24,
      "multiCloudStatus":"master",
      "supportRegionList":"[\"cn-qingdao-****-d01\"]",
      "name":"sub-org-1",
      "alias":"sub-org-1",
      "ctime":1606791494471,
      "id":2,
      "cuserId":"admin"
     }
```

`],`

```json
    "id":2
   }
```

`],`

```json
  "parentPk":"149595785389****",
  "default":true,
  "deleted":false,
```

```json
  "roles":[
   {
    "roleRange":"roleRange.orgAndSubOrgs",
    "arId":"ar-9999******",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_RESOURCE_USER",
    "active":true,
    "description":"role_test",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.resourceUser.name",
    "id":2,
    "roleLevel":2147483647,
    "organizationVisibility":"defaultRole.resourceUser.description"
   }
```

`],`

```json
  "userGroupRoles":[
   {
    "roleRange":"roleRange.orgAndSubOrgs",
    "arId":"ar-9999******",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_RESOURCE_USER",
    "active":true,
    "description":"role_test",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.resourceUser.name",
    "id":2,
    "roleLevel":2147483647,
    "cuserId":"admin",
    "organizationVisibility":"defaultRole.resourceUser.description"
   }
```

`],`

```json
  "loginName":"test",
  "accessKeys":[
   {
    "ctime":1606791494471,
    "id":2,
    "accesskeySecret":"CqHL**********",
    "region":"cn-qingdao-****-d01",
    "accesskeyId":"tCr5mJhpjo******",
    "status":"active"
   }
```

`],`

```json
  "id":2,
  "enableEmail":false,
  "email":"te**@163.com",
  "enableShortMessage":false,
  "primaryKey":"27365016246143****",
  "status":"active",
  "loginPolicy":{
   "ipRanges":[
    {
     "protocol":"IPV4",
     "ipRange":"0.0.0.0/0",
     "loginPolicyId":1
    }
```

`],`

```json
   "timeRanges":[
    {
     "loginPolicyId":1,
     "startTime":"00:00",
     "endTime":"24:00"
    }
```

`],`

```json
   "muserId":"admin",
   "default":true,
   "ownerOrganizationId":1,
   "enable":true,
   "name":"sub-org-1",
   "rule":"ALLOW",
   "id":2,
   "cuserId":"admin",
   "lpId":"lp-9999******",
   "organizationVisibility":"defaultRole.resourceUser.description"
  }
 },
 "success":true,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>ROLE_RESOURCE_USER</code> <cost>594</cost> <data> <cellphoneNum>1888888****</cellphoneNum> <displayName>testuser2022</displayName> <enableDingTalk>false</enableDingTalk> <userRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-9999******</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>role_test</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <id>2</id> <roleLevel>2147483647</roleLevel> <cuserId>admin</cuserId> <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility> </userRoles> <userGroups> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-9999******</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>role_test</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <id>2</id> <roleLevel>2147483647</roleLevel> <cuserId>admin</cuserId> <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility> </roles> <organizationId>1</organizationId> <users> <cellphoneNum>1888888****</cellphoneNum> <muserId>admin</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>RamUser</backendAccountType> <enableDingTalk>false</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1606791494471</mtime> <organizationId>1</organizationId> <default>true</default> <password>H2xWNY8oitAhxMWLhtyjs********</password> <deleted>false</deleted> <loginTime>1606791494471</loginTime> <userLoginCtrlId>34</userLoginCtrlId> <loginName>test</loginName> <ctime>1606791494471</ctime> <id>2</id> <mobileNationCode>86</mobileNationCode> <enableEmail>false</enableEmail> <ramUser>true</ramUser> <defaultRoleId>1</defaultRoleId> <email>te**@163.com</email> <enableShortMessage>false</enableShortMessage> <username>test</username> </users> <groupName>testUserGroup</groupName> <augId>aug-101de5c6c0e20a420******</augId> <resourceSets> <organizationID>1</organizationID> <creator>admin</creator> <resourceGroupName>res_test</resourceGroupName> <gmtCreated>1606791494471</gmtCreated> <rsId>12312a</rsId> <id>2</id> </resourceSets> <createTimeStamp>1606791494471</createTimeStamp> <organization> <muserId>admin</muserId> <internal>false</internal> <level>0.1.24</level> |  |

```xml
   <supportRegions>cn-qingdao-****-d01</supportRegions>
   <mtime>1606791494471</mtime>
   <uuid>org-101cc0654e910a420927000w</uuid>
   <parentId>24</parentId>
   <multiCloudStatus>master</multiCloudStatus>
   <supportRegionList>[&quot;cn-qingdao-****-d01&quot;]</supportRegionList>
   <name>sub-org-1</name>
   <alias>sub-org-1</alias>
   <ctime>1606791494471</ctime>
   <id>2</id>
   <cuserId>admin</cuserId>
  </organization>
  <id>2</id>
 </userGroups>
 <parentPk>149595785389****</parentPk>
 <default>true</default>
 <deleted>false</deleted>
 <roles>
  <roleRange>roleRange.orgAndSubOrgs</roleRange>
  <arId>ar-9999******</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_USER</code>
  <active>true</active>
  <description>role_test</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>2147483647</roleLevel>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </roles>
 <userGroupRoles>
  <roleRange>roleRange.orgAndSubOrgs</roleRange>
  <arId>ar-9999******</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_USER</code>
  <active>true</active>
  <description>role_test</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.resourceUser.name</roleName>
  <id>2</id>
  <roleLevel>2147483647</roleLevel>
  <cuserId>admin</cuserId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </userGroupRoles>
 <loginName>test</loginName>
 <accessKeys>
  <ctime>1606791494471</ctime>
  <id>2</id>
  <accesskeySecret>CqHL**********</accesskeySecret>
  <region>cn-qingdao-****-d01</region>
  <accesskeyId>tCr5mJhpjo******</accesskeyId>
  <status>active</status>
 </accessKeys>
 <id>2</id>
 <enableEmail>false</enableEmail>
 <email>te**@163.com</email>
 <enableShortMessage>false</enableShortMessage>
 <primaryKey>27365016246143****</primaryKey>
 <status>active</status>
 <loginPolicy>
  <ipRanges>
   <protocol>IPV4</protocol>
   <ipRange>0.0.0.0/0</ipRange>
   <loginPolicyId>1</loginPolicyId>
  </ipRanges>
  <timeRanges>
   <loginPolicyId>1</loginPolicyId>
   <startTime>00:00</startTime>
   <endTime>24:00</endTime>
  </timeRanges>
  <muserId>admin</muserId>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <name>sub-org-1</name>
  <rule>ALLOW</rule>
  <id>2</id>
  <cuserId>admin</cuserId>
<lpId>lp-9999******</lpId>
```

```xml
  <lpId>lp9999
</lpId>
  <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
 </loginPolicy>
</data> <success>true</success> <message>success</message>
```

###### 4.1.1.4.9. DeactivateUser

禁用用户时，系统将自动禁用用户所有的AccessKey。v3.12.0版本自SP016后开始支持此接口，v3.14.0版本自SP013后开始支持此接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser2022 | 用户登录名。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 118 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 用户信息。 |
| accessKeys | Array of accessKey |  | AccessKey信息列表。 说明只有平台管理员才能获取预置用户的AccessKey和AccessKey Secret。 |
| accessKey |  |  |  |
| accesskeyId | String | tCr5mJhpjo****** | 用户的AccessKey ID。 |

| ctime | Long | 1606675230000 | AccessKey创建时间。 说明该参数已废弃。 |
|---|---|---|---|
| cuserId | String | admin | 创建AccessKey的用户ID。 说明该参数已废弃。 |
| id | Integer | 1 | AccessKey的识别主键。 说明该参数已废弃。 |
| region | String | cn-qingdao-****-d01 | AccessKey的可用区。 |
| status | String | ACTIVE | AccessKey是否启用。 ACTIVE：启用。 INACTIVE：禁用。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 说明预置用户为系统自动创建，创建场景下该参数默认为false。 |
| defaultRole | Struct |  | 默认角色。 说明用户登录后的当前角色。 |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| arId | String | ar-9999999904 | 角色唯一编码。 |
| code | String | ROLEORGANIZATIONADMIN _ _ | 角色code。 说明内置角色code 是固定的，自定义角色的code由系统生成，格式为：ROLE _ 角色名称(大写) _随机串。权限校验时code 用来确定角色类型，判断角色是否有对应的权限。 |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.organizationAdmin.de scription | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 4 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |

| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| deleted | Boolean | false | 用户是否已被删除，已删除的用户为历史用户。 true：已经被删除。 false：未被删除。 |
| displayName | String | testuser2022 | 用户显示名。 |
| email | String | test@example.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | true | 是否启用钉钉通知 |
| enableEmail | Boolean | true | 是否启用邮件通知。 |
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 5817 | 用户ID。 |
| lastLoginTime | Long | 1657608949009 | 用户最后登录时间。 说明此参数已经废弃。 |
| loginName | String | testuser202209071758 | 用户登录名。 |
| loginPolicy | Struct |  | 用户绑定的登录策略。 |
| cuserId | String | admin | 创建登录策略的用户名称说明此参数已经废弃。 |
| default | Boolean | false | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |

| id | Integer | 1084 | 登录策略ID。 |
|---|---|---|---|
| ipRanges | Array of ipRange |  | 登录策略IP段。 |
| ipRange |  |  |  |
| ipRange | String | 10.48.16.1/24 | 访问策略的IP范围。 |
| loginPolicyId | Integer | 1084 | 所属访问策略ID。 |
| protocol | String | IPV4 | 访问策略使用的协议，仅支持ipv4。 |
| lpId | String | lp-101de13d33320a420d****** | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 访问策略名称。 |
| organizationVisibility | String | organizationVisibility.global | 访问策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 策略所属组织ID。 |
| rule | String | DENY | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略的时间段。 |
| timeRange |  |  |  |
| endTime | String | 18:00 | 结束时间。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| startTime | String | 08:00 | 开始时间。 |
| mobileNationCode | String | 86 | 国际区号。 |
| organization | Struct |  | 用户所属的组织。 |
| alias | String | sub-org-1 | 组织别名。 |
| ctime | Long | 1657608949009 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 说明参数已经废弃。 |
| id | Integer | 25 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 说明置组织即系统自动生成的组织，也称为默认组织。 |

| level | String | 0.1.24 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织leve |  |  |  |
|---|---|---|---|---|---|---|
| mtime | Long | 1657608949009 | 组织最近一次修改的时间。 |  |  |  |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |  |  |  |
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |  |  |  |
| name | String | sub-org-1 | 组织名称。 |  |  |  |
| parentId | Integer | 24 | 组织名称。 |  |  |  |
| supportRegionList | List | cn-***-d01 | 可用区列表。 |  |  |  |
| supportRegions | String | ["cn-***-d01"] | 可用区列表。 说明此参数已经废弃。 |  |  |  |
| uuid | String | org-101cc0654e910a4209****** | 组织UUID。 |  |  |  |
| parentPk | String | 1127157608934563 | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |  |  |  |
| primaryKey | String | 259258662544685329 | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号） 一致。 |  |  |  |
| roles | Array of role |  | 用户拥有的角色列表。 |  |  |  |
| role |  |  |  |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-9999****** | 角色唯一编码。 |  |  |  |
| code | String | ROLEORGANIZATIONADMIN _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成，格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| cuserId | String | adimin | 创建角色的用户。 说明参数已经废弃。 |
|---|---|---|---|
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.organizationAdmin.de scription | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 4 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| status | String | INACTIVE | 用户状态。 说明用户创建后否默认为active。 active:激活。 inactive:禁用。 |
| userGroupRoles | Array of userGroupRole |  | 用户所属用户组所拥有的角色列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |
| userGroupRole |  |  |  |

| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
|---|---|---|---|---|---|---|
| arId | String | ar-9999****** | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成，格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 创建角色的用户名称。 |  |  |  |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否有效。 |  |  |  |
| id | Integer | 2 | 角色ID。 |  |  |  |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | organizationVisibility 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 角色所属组织id。 |  |  |  |
| rAMRole | Boolean | false | 是否是ram角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际作用。 |  |  |  |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |  |  |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| userGroups | Array of userGroup |  | 用户所属用户组列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |
|---|---|---|---|
| userGroup |  |  |  |
| augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |
| createTimeStamp | Long | 1606791494471 | 用户组创建时间。 |
| groupName | String | testUserGroup01 | 用户组名称。 |
| id | Integer | 24 | 用户组ID。 |
| organization | Struct |  | 创建的用户所属的组织信息。 说明此参数已经废弃，若要查询用户组所属组织详细信息，请根据 organizationId参数通过GetOrganization接口查询。 |
| alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1606791494471 | 组织创建时间。 |
| cuserId | String | admin | 创建者用户名。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 说明置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 2147483647 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1606791494471 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织最近一次修改的时间。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 1 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 说明此参数已经废弃。 |

| uuid | String | 123456 | 组织UUID。 |  |  |  |
|---|---|---|---|---|---|---|
| organizationId | Integer | 1 | 用户组所属组织的ID。 |  |  |  |
| resourceSets | Array of resourceSet |  | 资源集列表。 说明此参数已经废弃。 |  |  |  |
| resourceSet |  |  |  |  |  |  |
| creator | String | admin | 资源集创建者的用户名。 |  |  |  |
| gmtCreated | Long | 1606791494471 | 资源集创建时间。 |  |  |  |
| id | Integer | 2 | 资源集ID。 |  |  |  |
| organizationID | Integer | 1 | 资源集所属组织的ID。 |  |  |  |
| resourceGroupName | String | resourcetest _ | 资源集名称。 |  |  |  |
| rsId | String | 123456 | 资源集唯一编码。 |  |  |  |
| roles | Array of role |  | 资源集列表。 说明此参数已经废弃。 |  |  |  |
| role |  |  |  |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | 123456 | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成，格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者用户名称。 |  |  |  |
| default | Boolean | false | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | test | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否被禁用。 |  |  |  |
| id | Integer | 4 | 角色id。 |  |  |  |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际作用。 |
| roleName | String | test | 角色名称。 |
| roleRange | String | roleRange.allOrganizations | 角色管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| users | Array of user |  | 用户列表。 说明此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表 |
| user |  |  |  |
| accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| active | Boolean | true | 用户是否有效。 说明该参数已废弃。 |
| aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| backendAccountType | String | RamUser | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号。 RamUser：RAM子账号。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ctime | Long | 1606791494471 | 用户创建时间。 |
| default | Boolean | true | 是否是默认用户。 |
| defaultRoleId | Integer | 1 | 用户默认角色ID。 |
| deleted | Boolean | false | 用户是否被删除。 |

| email | String | test@example.com | 用户邮箱地址。 |  |  |  |
|---|---|---|---|---|---|---|
| enableDingTalk | Boolean | false | 是否发送钉钉消息。 |  |  |  |
| enableEmail | Boolean | false | 是否发送邮件。 |  |  |  |
| enableShortMessage | Boolean | false | 是否发动短信。 |  |  |  |
| id | Integer | 5930 | 用户ID。 |  |  |  |
| loginName | String | test | 用户登录名。 |  |  |  |
| loginTime | Long | 1606791494471 | 用户登录时间。 |  |  |  |
| mobileNationCode | String | 86 | 国际区号。 |  |  |  |
| mtime | Long | 1606791494471 | 用户信息被修改时间。 |  |  |  |
| muserId | String | admin | 最后一次更新用户数据时间。 |  |  |  |
| organizationId | Integer | 6 | 用户所属组织ID。 |  |  |  |
| password | String | ****************** | 用户密码说明此参数已经废弃。 |  |  |  |
| ramUser | Boolean | false | 是否是RAM用户。 |  |  |  |
| userLoginCtrlId | Integer | 1 | 登录策略ID。 |  |  |  |
| username | String | test | 用户显示名。 |  |  |  |
| userRoles | Array of userRole |  | 用户角色列表，用户关联的角色列表，由请求参数roleIdList指定。 |  |  |  |
| userRole |  |  |  |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-9999****** | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成，格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者的用户名。 |  |  |  |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否有效。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| id | Integer | 2 | 角色ID。 |
|---|---|---|---|
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际作用。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations为所有组织。 roleRange.orgAndSubOrgs为本组织及级联下级组织。 roleRange.resourceSet为资源集。 roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>118</cost> <code>200</code> |  |

```xml
<data>
    <cellphoneNum>188****8888</cellphoneNum>
    <enableDingTalk>true</enableDingTalk>
    <displayName>testuser2022</displayName>
    <parentPk>1127157608934563</parentPk>
    <lastLoginTime>1657608949009</lastLoginTime>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>testuser202209071758</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>5817</id>
    <enableEmail>true</enableEmail>
    <enableShortMessage>true</enableShortMessage>
    <email>test@example.com</email>
    <status>INACTIVE</status>
    <primaryKey>259258662544685340</primaryKey>
    <userGroupRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>defaultRole.resourceUser.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>2</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>1</organizationId>
        <groupName>testUserGroup01</groupName>
        <augId>aug-101de696afc90a420d******</augId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <id>24</id>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>resource_test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123456</rsId>
            <id>2</id>
        </resourceSets>
        <users>
            <cellphoneNum>188****8888</cellphoneNum>
            <muserId>admin</muserId>
            <aliyunUser>false</aliyunUser>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <accountType>1</accountType>
            <active>true</active>
            <mtime>1606791494471</mtime>
            <organizationId>6</organizationId>
            <password>******************</password>
            <default>true</default>
            <loginTime>1606791494471</loginTime>
            <deleted>false</deleted>
            <userLoginCtrlId>1</userLoginCtrlId>
            <loginName>test</loginName>
            <ctime>1606791494471</ctime>
            <mobileNationCode>86</mobileNationCode>
            <id>5930</id>
            <ramUser>false</ramUser>
            <enableEmail>false</enableEmail>
            <enableShortMessage>false</enableShortMessage>
            <email>test@example.com</email>
            <defaultRoleId>1</defaultRoleId>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.allOrganizations</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>123456</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>false</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
<roleName>test</roleName>
```

```xml
            <roleName>test</roleName>
            <roleLevel>2147483647</roleLevel>
            <id>4</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
        <organization>
            <muserId>admin</muserId>
            <internal>false</internal>
            <multiCloudStatus>master</multiCloudStatus>
            <level>2147483647</level>
            <name>test</name>
            <supportRegions>cn-qingdao-****-d01</supportRegions>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
            <id>1</id>
            <mtime>1606791494471</mtime>
            <uuid>123456</uuid>
            <cuserId>admin</cuserId>
            <parentId>1</parentId>
            <supportRegionList>["cn-qingdao-****-d01"]</supportRegionList>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>defaultRole.resourceUser.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>2</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-qingdao-env66-d01</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>tCr5mJhpjo******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <description>defaultRole.organizationAdmin.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>4</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>adimin</cuserId>
    </roles>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999999904</arId>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <description>defaultRole.organizationAdmin.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>4</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>false</default>
<onerOrganiationId>1</onerOrganiationId>
```

```xml
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>mytest</name>
        <rule>DENY</rule>
        <id>1084</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>lp-101de13d33320a420d******</lpId>
        <cuserId>admin</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>10.48.16.1/24</ipRange>
            <loginPolicyId>1084</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>08:00</startTime>
            <loginPolicyId>1084</loginPolicyId>
            <endTime>18:00</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <multiCloudStatus>master</multiCloudStatus>
        <level>0.1.24</level>
        <name>sub-org-1</name>
        <supportRegions>["cn-***-d01"]</supportRegions>
        <ctime>1657608949009</ctime>
        <alias>sub-org-1</alias>
        <id>25</id>
        <mtime>1657608949009</mtime>
        <uuid>org-101cc0654e910a4209******</uuid>
        <cuserId>admin</cuserId>
        <parentId>24</parentId>
        <supportRegionList>cn-***-d01</supportRegionList>
    </organization>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 118, "code": 200, "data": { "cellphoneNum": "188****8888", "enableDingTalk": true, "displayName": "testuser2022", "parentPk": 1127157608934563, "lastLoginTime": 1657608949009, "default": false, "deleted": false, "loginName": "testuser202209071758", "mobileNationCode": 86, "id": 5817, "enableEmail": true, "enableShortMessage": true, "email": "test@example.com", "status": "INACTIVE", "primaryKey": 259258662544685340, "userGroupRoles": { "roleRange": "roleRange.resourceSet", "rAMRole": false, "muserId": "admin", "arId": "ar-9999******", "code": "ROLE_RESOURCE_USER", "description": "defaultRole.resourceUser.description", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceUser.name", "roleLevel": 2147483647, "id": 2, "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "userGroups": { "organizationId": 1, "groupName": "testUserGroup01", "augId": "aug-101de696afc90a420d******", "createTimeStamp": 1606791494471, "id": 24, "resourceSets": { "organizationID": 1, |  |

```
oga ato
```

: ,

```json
                "creator": "admin",
                "resourceGroupName": "resource_test",
                "gmtCreated": 1606791494471,
                "rsId": 123456,
                "id": 2
            },
            "users": {
                "cellphoneNum": "188****8888",
                "muserId": "admin",
                "aliyunUser": false,
                "backendAccountType": "RamUser",
                "enableDingTalk": false,
                "accountType": 1,
                "active": true,
                "mtime": 1606791494471,
                "organizationId": 6,
                "password": "******************",
                "default": true,
                "loginTime": 1606791494471,
                "deleted": false,
                "userLoginCtrlId": 1,
                "loginName": "test",
                "ctime": 1606791494471,
                "mobileNationCode": 86,
                "id": 5930,
                "ramUser": false,
                "enableEmail": false,
                "enableShortMessage": false,
                "email": "test@example.com",
                "defaultRoleId": 1,
                "username": "test"
            },
            "roles": {
                "roleRange": "roleRange.allOrganizations",
                "rAMRole": false,
                "muserId": "admin",
                "arId": 123456,
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": false,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "test",
                "roleLevel": 2147483647,
                "id": 4,
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            },
            "organization": {
                "muserId": "admin",
                "internal": false,
                "multiCloudStatus": "master",
                "level": 2147483647,
                "name": "test",
                "supportRegions": "cn-qingdao-****-d01",
                "ctime": 1606791494471,
                "alias": "test",
                "id": 1,
                "mtime": 1606791494471,
                "uuid": 123456,
                "cuserId": "admin",
                "parentId": 1,
                "supportRegionList": "[\"cn-qingdao-****-d01\"]"
            }
        },
        "userRoles": {
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_RESOURCE_USER",
            "description": "defaultRole.resourceUser.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "roleLevel": 2147483647,
            "id": 2,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "accessKeys": {
"ctime":1606675230000
```

```json
            "ctime": 1606675230000,
            "id": 1,
            "region": "cn-qingdao-env66-d01",
            "cuserId": "admin",
            "status": "ACTIVE",
            "accesskeyId": "tCr5mJhpjo******"
        },
        "roles": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_ORGANIZATION_ADMIN",
            "description": "defaultRole.organizationAdmin.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "roleLevel": 2147483647,
            "id": 4,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "adimin"
        },
        "defaultRole": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999999904",
            "code": "ROLE_ORGANIZATION_ADMIN",
            "description": "defaultRole.organizationAdmin.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "roleLevel": 2147483647,
            "id": 4,
            "organizationVisibility": "organizationVisibility.global"
        },
        "loginPolicy": {
            "muserId": "admin",
            "default": false,
            "ownerOrganizationId": 1,
            "enable": true,
            "name": "mytest",
            "rule": "DENY",
            "id": 1084,
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "lp-101de13d33320a420d******",
            "cuserId": "admin",
            "ipRanges": {
                "protocol": "IPV4",
                "ipRange": "10.48.16.1/24",
                "loginPolicyId": 1084
            },
            "timeRanges": {
                "startTime": "08:00",
                "loginPolicyId": 1084,
                "endTime": "18:00"
            }
        },
        "organization": {
            "muserId": "admin",
            "internal": false,
            "multiCloudStatus": "master",
            "level": "0.1.24",
            "name": "sub-org-1",
            "supportRegions": "[\"cn-***-d01\"]",
            "ctime": 1657608949009,
            "alias": "sub-org-1",
            "id": 25,
            "mtime": 1657608949009,
            "uuid": "org-101cc0654e910a4209******",
            "cuserId": "admin",
            "parentId": 24,
            "supportRegionList": "cn-***-d01"
        }
    },
    "success": true,
    "message": "success"
}
```

###### 4.1.1.4.10. ListAccessKeysForManagedUsers

调用ListAccessKeysForManagedUsers接口查询当前用户管理范围内用户的Accesskey信息。 支持通过填写用户ID（ascmUserId）、组织ID（organizationId）、用户登录名（loginName）指定接口查询的组织、用户范围，如不指定则返回当前调用接口的用户管理范围内所有用户的Accesskey信息。 平台管理员（super）、资源监查员可以查询全部用户AK。 其他全局角色（如admin）可以查看除内部组织外用户AK。 组织管理员（或其他管理范围为本组织及级联下级组织的角色）可以查询本组织及下级组织用户AK。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /user/accesskey/listAccessKeysForManagedUsers HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ascmUserId | Integer | Body | 否 | 12 | 用户ID，用于指定用户。 |
| organizationId | Integer | Body | 否 | 1 | 组织ID，用于指定组织范围。组织ID可通过调用 GetOrganizationList接口获取。 |
| loginName | String | Body | 否 | test | 用户登录名，用于指定用户，支持模糊查询。 |
| pageNum | Integer | Body | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| pageSize | Integer | Body | 否 | 10 | 设置分页查询时，每页显示的记录数量。默认值为 10，表示每页显示10条记录；最大值为100。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 匹配查询范围内的用户AccessKey信息列表。 |
| -accessKeys | Array | - | 用户拥有的AccessKey信息列表。 |
| --accesskeyId | String | tCr5mJhpjo**** | AccessKey ID。 |
| --createTime | String | 1606675230000 | AccessKey的创建时间戳。 |
| --status | String | Inactive | AccessKey启用状态。 Active：启用。 Inactive：禁用。 |
| -loginName | String | testuser | 用户登录名。 |
| -primaryKey | String | 25925468**** | 用户的RAM用户（子账号）主键，作为账号的唯一标识。 |
| code | String | 200 | 状态响应码。 200：调用成功。 403：没有权限。 500：内部错误。 |
| cost | Integer | 188 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 success：调用成功。 NoPermission：没有权限。 InternalError：内部错误。 |
| success | Boolean | true | 接口请求成功标识。 |

| pageInfo | Struct | - | 返回分页信息。 |
|---|---|---|---|
| -currentPage | Integer | 1 | 分页查询时，当前页的页码。 |
| -pageSize | Integer | 10 | 分页查询时，每页数据显示的最大条数。 |
| -total | Integer | 1 | 分页查询时，返回的数据总条数。 |
| -totalPage | Integer | 1 | 分页查询时，返回总页数。 |

**示例**

请求示例

```
POST /user/accesskey/listAccessKeysForManagedUsers HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 714, "data": [ { "accessKeys": [ { "createTime": "2023-11-27T12:05:31Z", "accesskeyId": "Su0********", "status": "Inactive" } ], "loginName": "base******t", "primaryKey": "28846********" } ], "success": true, "pageInfo": { "total": 36214, "totalPage": 3622, "pageSize": 10, "currentPage": 1 }, "message": "success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>714</cost> <data> <accessKeys> <createTime>2023-11-27T12:05:31Z</createTime> <accesskeyId>Su0********</accesskeyId> <status>Inactive</status> </accessKeys> <loginName>base******t</loginName> <primaryKey>28846********</primaryKey> </data> <success>true</success> <pageInfo> <total>36214</total> <totalPage>3622</totalPage> <pageSize>10</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

ascm 2019-05-10

###### 4.1.1.4.11. DeleteUserAccessKey

删除用户AK。必须保证删除后用户至少有一个状态为ACTIVE的AK。 用户可以操作自己的AK。 平台管理员（super）可以操作全部用户AK。 其他全局角色（如admin）可以操作除内部组织外用户AK。 组织管理员（或其他管理范围为本组织及级联下级组织的角色）可以操作本组织及下级组织用户AK。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| deleteAccesskey | String | Query | 否 | qbvg****** | 当前需要删除的AK。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口操作成功标识。 |
| code | String | 200 | 状态响应码。 |
| message | String | success | 返回提示信息。 |
| cost | Long | 107 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":107, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>107</cost> <success>true</success> <message>success</message> |  |

ascm 2019-05-10

###### 4.1.1.4.12. UpdateUserAccessKeyStatus

更新单个AK状态，启用或禁用AK。更新后必须存在至少一个启用状态的AK，否则此接口会报错。 用户可以操作自己的AK。 平台管理员（super）可以操作全部用户AK。 其他全局角色（如admin）可以操作除内部组织外用户AK。 组织管理员（或其他管理范围为本组织及级联下级组织的角色）可以操作本组织及下级组织用户AK。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /user/accessKey/status HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| updateAccesskey | String | Body | 否 | qwe2h****** | 要启用或禁用的AK。 |
|---|---|---|---|---|---|
| updateAccesskeySt atus | String | Body | 否 | ACTIVE | AK更新后的状态。该项是必填项。 ACTIVE：启用。 INACTIVE：禁用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口请求成功标识。 |
| code | String | 200 | 状态响应码。 |
| message | String | 200 | 返回提示信息。 |
| cost | Long | 103 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
PUT /user/accessKey/status HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":103, "success":true, "message":"200" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>103</cost> <success>true</success> <message>200</message> |  |

ascm 2019-05-10

###### 4.1.1.4.13. CreateUserAccessKey

创建用户AK，每个用户最多可持有两对AK。 用户可以为自己创建，会返回AK和SK。 平台管理员（super）可以为全部用户创建，仅返回AK。 其他全局角色（如admin）可以操作除内部组织外用户，仅返回AK。 组织管理员（或其他管理范围为本组织及级联下级组织的角色）可以操作本组织及下级组织用户，仅返回AK。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /user/accessKey HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | Test | 用户名，置空则创建用户自己的AK。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口请求成功标识。 |
| code | String | 200 | 状态响应码。 |
| message | String | success | 返回提示信息。 |
| cost | Long | 100 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | - | 创建的Ak信息。 |
| -accesskeyId | String | qwe****** | 用户AccessKey ID. |
| -accesskeySecret | String | eb2hf****** | 用户AccessKey Secret。 |
| -status | String | ACTIVE | 用户AK的状态。默认为ACTIVE，表示启用。 |
| -ctime | Long | 1715835495000 | 用户AK创建时间。 |

**示例**

请求示例

```
POST /user/accessKey HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":100, "data":{ "ctime":1715835495000, "accesskeySecret":"eb2hf******", "accesskeyId":"qwe******", "status":"ACTIVE" }, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>100</cost> <data> <ctime>1715835495000</ctime> <accesskeySecret>eb2hf******</accesskeySecret> <accesskeyId>qwe******</accesskeyId> <status>ACTIVE</status> </data> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.14. GetRecentAkTrailForUser

查看AK审计日志。支持查询被禁用的AK的日志，无法获取被删除AK的日志。 AccessKey日志后端数据存在一定延迟(一般 1 小时)，且默认仅保存7天日志，请务必谨慎对AccessKey做变更处理。如需保存更长时间日志，需在配置中进行操作日志转存 （依赖SLS日志服务）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /user/accessKey/trail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageNum | Integer | Query | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| pageSize | Integer | Query | 否 | 20 | 设置分页查询时，每页显示的记录数量。默认值为20，表示每页显示20条记录。 |
| startTime | Long | Query | 否 | 1 | 查询起始时间，不传默认查过去一小时。 |
| endTime | Long | Query | 否 | 2 | 查询结束时间，不传默认查过去一小时。 |
| queryTrailAccessKe y | String | Query | 是 | qwertg****** | 要获取审计日志的AK。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口请求成功标识。 |
| code | String | 200 | 状态响应码。 |
| message | String | success | 返回提示信息。 |
| cost | Long | 100 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | AK审计日志信息。 |
| -events | Array |  | 调用事件。 |
| --eventId | String | dwe****** | 事件ID。 |
| --sourceIpAddress | String | 10.**.**.204 | 事件发生的IP。 |
| --eventRW | String | Write | 事件的读写类型。 Write：写。 Read：读。 |
| --eventTime | Long | 1687261342987 | 事件时间。 |
| --eventName | String | RunInstances | 事件API。 |
| --serviceName | String | ECS | 产品POP Code。 |
| --resourceType | String | ascm.resourceType.ecsinstance _ | 资源类型。 |
| -accessKey | String | qewq****** | 用户AK。 |

**示例**

请求示例

```
GET /user/accessKey/trail HTTP/1.1 &queryTrailAccessKey=qwertg******
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":100,
 "data":{
  "accessKey":"qewq******",
  "events":{
   "eventId":"dwe******",
   "eventTime":1687261342987,
   "sourceIpAddress":"10.**.**.204",
   "eventName":"RunInstances",
   "eventRW":"Write",
   "serviceName":"ECS",
   "resourceType":"ascm.resourceType.ecs_instance"
  }
 },
 "success":true,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>100</cost> <data> <accessKey>qewq******</accessKey> <events> <eventId>dwe******</eventId> <eventTime>1687261342987</eventTime> <sourceIpAddress>10.**.**.204</sourceIpAddress> <eventName>RunInstances</eventName> <eventRW>Write</eventRW> <serviceName>ECS</serviceName> <resourceType>ascm.resourceType.ecs_instance</resourceType> </events> </data> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.15. ListUserAccessKey

获取用户自己的AK列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /user/accessKeys HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 用户AK列表。 |
| -accesskeyId | String | x0Ur****** | 用户AccessKey ID。 |
| -accesskeySecret | String | lml2H****** | 用户Accesskey Secret。 |
| -status | String | ACTIVE | 用户AccessKey启用状态。 ACTIVE：启用。 INACTIVE：禁用。 |
| -createTime | String | 2024-03-06T05:55:29Z | UTC时间格式。 |
| -ctime | Long | 1709704529000 | AccessKey的创建时间，单位ms。 |
| success | Boolean | true | 接口请求成功标识。 |
| code | String | 200 | 状态响应码。 |
| message | String | success | 返回提示信息。 |
| cost | Long | 44 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
GET /user/accessKeys HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 23, "data": [ { "createTime": "2024-08-13T03:37:49Z", "ctime": 1723520269000, "accesskeySecret": "hZK********", "accesskeyId": "GmN********", "status": "ACTIVE" }, { "createTime": "2024-01-31T05:37:35Z", "ctime": 1706679455000, "accesskeySecret": "c4lu********", "accesskeyId": "hPC********", "status": "ACTIVE" } ], "success": true, "message": "success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>23</cost> <data> <createTime>2024-08-13T03:37:49Z</createTime> <ctime>1723520269000</ctime> <accesskeySecret>hZK********</accesskeySecret> <accesskeyId>GmN********</accesskeyId> <status>ACTIVE</status> </data> <data> <createTime>2024-01-31T05:37:35Z</createTime> <ctime>1706679455000</ctime> <accesskeySecret>c4lu********</accesskeySecret> <accesskeyId>hPC********</accesskeyId> <status>ACTIVE</status> </data> <success>true</success> <message>success</message> |  |

ascm 2019-05-10

###### 4.1.1.4.16. ListAvailableUsersByRoleId

获取加入某个角色的用户列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/listAvailableUsersByRoleId HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| organizationId | Integer | Body | 否 | 3 | 用户所属组织ID，可通过调用GetOrganizationList接口获取。 说明以用户所属组织ID为条件查询属于这个组织的用户信息，不传则忽略此条件。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |

| pageSize | Integer | Body | 否 | 10 | 每页显示数据条数，默认为符合以上条件的所有数据的条数。 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | test | 登录用户名的SQL正则表达式。 说明传入此参数会根据用户名正则匹配查询，不传则返回所有拥有该角色的用户。 |
| roleId | Integer | Body | 否 | 1 | 用户关联的角色ID，可通过调用ListRoles接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| action | String | ListAvailableUsersByRoleId | 当前接口的名称。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 22 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of userKeyInfo |  | 用户集。 |
| displayName | String | admin | 用户显示名。 |
| id | Integer | 5003 | 用户ID。 |
| loginName | String | admin | 用户登录名称。 |
| organizationId | Integer | 3 | 用户所属组织的ID。 |
| organizationName | String | test | 用户所属组织的名称。 |
| status | String | ACTIVE | 用户当前状态。 ACTIVE：激活。 INACTIVE：禁用。 |
| domain | String | ascm.aliyun.com | 报错服务的域名。 说明无论接口是否报错都会返回。 |

| errorKey | String | ascm.auth.InvalidParameter | 错误码。 ascm.auth.ServerUnknownException：服务内部发生未知异常。 ascm.auth.InternalError：内部错误。 ascm.auth.InvalidParameter：参数错误。 ascm.auth.SystemEncodeException：系统编码异常。 ascm.auth.NetIOException：后端网络存在异常。 ascm.auth.CallBackendServiceReturnEmptyException：调用后端服务，返回了空的Response。 ascm.auth.ForbidCallTheInterface：该功能已经下线，禁止调用。 ascm.auth.NoPermission：没有权限。 ascm.auth.CallTairException：调用Tair服务异常。 ascm.auth.EntityNotExist.Organization：组织不存在。 ascm.auth.EntityNotExist.UserGroup：用户组不存在。 ascm.auth.account.notLoggedIn：用户未登录或登录状态失效。 ascm.auth.EntityNotExist.User：用户不存在。 ascm.auth.exceeded.userUserGroup：用户加入的用户组数量超过限制。 ascm.auth.UnknownException：内部未知异常。 ascm.auth.CallDataBaseException：访问数据库异常。 ascm.auth.PageSizeBeyondQuota：PageSize不能超过限定数值。 ascm.auth.internalServerError：服务出现内部错误，请检查服务。 ascm.auth.EntityNotExist：实体不存在。 |
|---|---|---|---|
| extraMessage | String | success | 额外的提示信息，是对错误提示信息的补充说明。 说明仅在接口调用失败异常时返回。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页码。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 10 | 数据总条数。 |
| totalPage | Integer | 1 | 总页数。 |
| requestId | String | 5FE0023D-73C3-481E-926D- 17A2CF****** | 本次请求链路ID。 |
| serverRole | String | unimanager- base.IdentityService# | 接口对应服务的服务角色名称。 |
| successResponse | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/listAvailableUsersByRoleId HTTP/1.1
```

公共请求头

```json
{ "RoleId": "1" }
```

正常返回示例 `XML` 格式

```xml
<ServerRole>unimanager-base.IdentityService#</ServerRole> <Action>ListAvailableUsersByRoleId</Action> <SuccessResponse>true</SuccessResponse> <PageInfo>
    <TotalPage>1</TotalPage>
    <PageSize>10</PageSize>
    <CurrentPage>1</CurrentPage>
    <Total>10</Total>
</PageInfo> <RequestId>5FE0023D-73C3-481E-926D-17A2CF******</RequestId> <Message>success</Message> <ErrorKey>ascm.auth.InvalidParamete</ErrorKey> <Data>
    <OrganizationName>Test</OrganizationName>
    <Status>ACTIVE</Status>
    <LoginName>admin</LoginName>
    <DisplayName>admin</DisplayName>
    <OrganizationId>3</OrganizationId>
    <Id>5002</Id>
</Data> <Domain>ascm.aliyun.com</Domain> <ExtraMessage>success</ExtraMessage> <Cost>22</Cost> <Code>200</Code>
```

| JSON | 格式 |
|---|---|
| { "ServerRole": "unimanager-base.IdentityService#", "Action": "ListAvailableUsersByRoleId", "SuccessResponse": true, "PageInfo": { "TotalPage": 1, "PageSize": 10, "CurrentPage": 1, "Total": 10 }, "RequestId": "5FE0023D-73C3-481E-926D-17A2CF******", "Message": "success", "ErrorKey": "ascm.auth.InvalidParamete", "Data": { "OrganizationName": "Test", "Status": "ACTIVE", "LoginName": "admin", "DisplayName": "admin", "OrganizationId": 3, "Id": 5002 }, "Domain": "ascm.aliyun.com", "ExtraMessage": "success", "Cost": 22, "Code": 200 } |  |

###### 4.1.1.4.17. ListDeletedUsers

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | ListDeletedUsers | 系统规定参数。取值：ListDeletedUsers。 |
| LoginName | String | 否 | testu | 用户登录名。 |
| CurrentPage | Integer | 否 | 1 | 分页页码。 |
| PageSize | Integer | 否 | 10 | 分页大小。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |

| data | Array of dataItem |  | 响应结果。 |
|---|---|---|---|
| dataItem |  |  |  |
| cellphoneNum | String | 00000000000 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 |
| deleted | Boolean | true | 用户是否删除。 |
| displayName | String | test | 用户显示名。 |
| email | String | test@163.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| enableEmail | Boolean | false | 是否启用邮件通知。 |
| enableShortMessage | Boolean | false | 是否启用短信通知。 |
| id | Integer | 1 | 用户ID。 |
| lastLoginTime | Long | 1231212 | 用户最后登录时间。 |
| loginName | String | test | 用户登录名。 |
| mobileNationCode | String | 86 | 区号。 |
| status | String | ACTIVE | 用户状态：active为激活，inactive为禁用。 |
| message | String | success | 错误提示信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 20 | 每页大小。 |
| total | Integer | 2 | 总条数。 |
| totalPage | Integer | 39 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据，不返回其它字段。 |
| redirect | Boolean | false | 是否重定向。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>1000</cost> <code>200</code> <data>
    <cellphoneNum>00000000000</cellphoneNum>
    <enableDingTalk>false</enableDingTalk>
    <displayName>test</displayName>
    <lastLoginTime>1231212</lastLoginTime>
    <default>false</default>
    <deleted>true</deleted>
    <loginName>test</loginName>
    <mobileNationCode>86</mobileNationCode>
    <id>1</id>
    <enableEmail>false</enableEmail>
    <enableShortMessage>false</enableShortMessage>
    <email>test@163.com</email>
    <status>ACTIVE</status>
</data> <success>true</success> <pageInfo>
    <total>2</total>
    <totalPage>39</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": [ { "cellphoneNum": "00000000000", "enableDingTalk": "false", "displayName": "test", "lastLoginTime": "1231212", "default": "false", "deleted": "true", "loginName": "test", "mobileNationCode": "86", "id": "1", "enableEmail": "false", "enableShortMessage": "false", "email": "test@163.com", "status": "ACTIVE" } ], "success": "true", "pageInfo": { "total": "2", "totalPage": "39", "pageSize": "20", "currentPage": "1" }, "pureListData": "false", "message": "success" } |  |

###### 4.1.1.4.18. ListUsers

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser | 用户登录名，由大小写英文字母、数字、下划线（_）、短划线 （-）、半角句号（.）组成，长度为2~64个字符。 说明传入此参数则以用户登录名进行模糊查询，若所有请求参数都不传，则返回当前调用用户能看到的所有用户。 |

| roleId | Integer | Body | 否 | 6 | 角色ID。可通过调用ListActiveRoles接口获取。 说明传入此参数则返回绑定该角色且当前调用用户可见的所有用户。 |
|---|---|---|---|---|---|
| loginPolicyId | Integer | Body | 否 | 1084 | 登录策略的ID。可通过调用ListActiveRoles接口获取。 说明传入此参数则返回使用该登录策略且当前调用用户可见的所有用户。 |
| organizationId | Integer | Body | 否 | 25 | 组织ID。可通过调用ListActiveRoles接口获取。 说明传入此参数则返回该组织下且当前调用用户可见的所有用户。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 每页显示数据条数，默认为符合以上条件的所有数据的条数，默认为10。 |
| status | String | Body | 否 | active | 用户状态。 active：激活。 inactive：禁用。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| cost | Integer | 24 | 接口响应耗时，单位毫秒（ms）。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| data | Array of dataItem |  | 响应结果。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 说明预置用户在系统初始化时生成，创建的用户此字段默认为fasle。 |
| defaultRole | Struct |  | 用户的默认角色。 |

| active | Boolean | true | 用户的默认角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |  |  |  |
|---|---|---|---|---|---|---|
| arId | String | ar-99999****** | 用户的默认角色唯一编码。 |  |  |  |
| code | String | ROLEORGANIZATIONADMIN _ _ | 用户的默认角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| default | Boolean | true | 用户的默认是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.organizationAdmin.de scription | 用户的默认角色描述。 |  |  |  |
| enable | Boolean | true | 用户的默认角色是否有效。 |  |  |  |
| id | Integer | 4 | 用户的默认角色ID。 |  |  |  |
| muserId | String | admin | 用户的默认角色最近一次修改的修改者用户名。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 用户的默认角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 用户的默认角色所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 用户的默认是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 用户的默认角色等级。 说明该参数无实际作用。 |  |  |  |
| roleName | String | defaultRole.organizationAdmin.na me | 用户的默认角色名称。 |  |  |  |
| roleRange | String | roleRange.orgAndSubOrgs | 用户的默认角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 用户的默认角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |  |  |
| deleted | Boolean | false | 用户的默认用户是否已删除。 |  |  |  |
| displayName | String | testuser2022 | 用户显示名称。 |  |  |  |
| email | String | test@example.com | 用户邮箱。 |  |  |  |
| enableDingTalk | Boolean | true | 是否启用钉钉通知。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| enableEmail | Boolean | true | 是否启用邮件通知。 |
|---|---|---|---|
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 5817 | 用户ID。 |
| lastLoginTime | Long | 1606675230000 | 用户最近一次登录的时间。 说明此参数已经废弃。 |
| loginName | String | testuser2022 | 用户登录名。 |
| loginPolicy | Struct |  | 用户所使用的登录策略。 |
| cuserId | String | admin | 登录策略创建者的用户名。 |
| default | Boolean | false | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |
| id | Integer | 1084 | 登录策略ID。 |
| ipRanges | Array of ipRange |  | 登录策略IP段。 |
| ipRange | String | 10.48.16.1/24 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| protocol | String | IPV4 | 登录策略使用的协议，仅支持IPv4。 |
| lpId | String | lp-101de13d33320a420d27000p | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 登录策略名称。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 策略所属组织ID。 |
| rule | String | DENY | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略的时间段。 |
| endTime | String | 18:00 | 登录策略生效时间段的结束时间。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| startTime | String | 08:00 | 登录策略生效时间段的开始时间。 |
| mobileNationCode | String | 86 | 用户手机号码的国际区号。 |
| organization | Struct |  | 用户所属组织的信息。 |
| alias | String | sub-org-1 | 组织别名。系统自动生成，一般与组织名称一致。 |

| ctime | Long | 1657608949009 | 用户所属组织创建的时间。 |
|---|---|---|---|
| cuserId | String | admin | 用户所属组织创建者的用户名。 |
| id | Integer | 25 | 用户所属组织ID。 |
| internal | Boolean | false | 用户所属组织是否为预置组织。 说明置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1.24 | 用户所属组织的等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1657608949009 | 用户所属组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 用户所属组织是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 用户所属组织最近一次修改的修改者用户名。 |
| name | String | sub-org-1 | 用户所属组织的名称。 |
| parentId | Integer | 24 | 用户所属组织的父组织ID。 |
| supportRegionList | List | cn-***-d01 | 用户所属组织的可用区列表。 |
| supportRegions | String | ["cn-***-d01"] | 用户所属组织的可用区列表。 说明此参数已经废弃。 |
| uuid | String | org- 101cc0654e910a420927000w | 用户所属组织UUID。 |
| parentPk | String | 1127157608934563 | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |
| primaryKey | String | 259258662544685329 | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号） 一致。 |
| roles | Array of role |  | 角色列表。 |
| active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |
| arId | String | ar-99999****** | 角色唯一编码。 |

| code | String | ROLEGLOBALRESOURCEAUDIT _ _ _ OR | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者的用户名。 |  |  |  |
| default | Boolean | true | 角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、 平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.globalResourceAudito r.description | 角色描述。 |  |  |  |
| enable | Boolean | true | 用户角色是否有效。 |  |  |  |
| id | Integer | 6 | 角色ID。 |  |  |  |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 角色是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 角色的等级。 说明该参数无实际作用。 |  |  |  |
| roleName | String | defaultRole.globalResourceAudito r.name | 角色的名称。 |  |  |  |
| roleRange | String | roleRange.allOrganizations | 角色的管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |  |  |
| status | String | active | 用户状态。 active：激活。 inactive：禁用。 |  |  |  |
| userGroupRoles | Array of userGroupRole |  | 用户所属用户组所绑定的角色列表。 |  |  |  |
| active | Boolean | true | 用户组所绑定的角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-99999****** | 用户组所绑定的角色唯一编码。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| code | String | ROLERESOURCESETADMIN _ _ _ | 用户组所绑定的角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|---|---|---|---|---|---|---|
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 用户组所绑定的角色创建者的用户名。 |  |  |  |
| default | Boolean | true | 用户组所绑定的是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.resourceSetAdmin.de scription | 用户组所绑定的角色描述。 |  |  |  |
| enable | Boolean | true | 用户组所绑定的角色是否有效。 |  |  |  |
| id | Integer | 5 | 用户组所绑定的角色ID。 |  |  |  |
| muserId | String | admin | 用户组所绑定的角色最近一次修改的修改者用户名。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 用户组所绑定的角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 用户组所绑定角色的所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 用户组所绑定的角色是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 用户组所绑定角色的等级。 说明保留字段，无实际作用。 |  |  |  |
| roleName | String | defaultRole.resourceSetAdmin.na me | 用户组所绑定角色的名称。 |  |  |  |
| roleRange | String | roleRange.resourceSet | 用户组所绑定角色的管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 用户组所绑定角色的类型。 ROLETYPE _RAM：RAM角色 ROLETYPE _ASCM：自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role |  |  |  |
| userGroups | Array of userGroup |  | 用户所属用户组列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |  |  |  |
| augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |  |  |  |
| createTimeStamp | Long | 1606791494471 | 用户组创建时间。 |  |  |  |
| groupName | String | testUserGroup01 | 用户组名称。 |  |  |  |
| id | Integer | 24 | 用户组ID。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| organization | Struct |  | 创建的用户所属的组织信息。 说明此参数已经废弃，若要查询用户组所属组织详细信息，请根据 organizationId参数通过GetOrganization接口查询。 |
|---|---|---|---|
| alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1606791494471 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | true | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 123 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1606791494471 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 1 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| uuid | String | 123456 | 组织UUID。 |
| organizationId | Integer | 1 | 用户组所属组织的ID。 |
| resourceSets | Array of resourceSet |  | 资源集列表。 说明此参数已经废弃。 |
| creator | String | admin | 资源集创建者的用户名。 |
| gmtCreated | Long | 1606791494471 | 资源集创建时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 2 | 资源集所属组织的ID。 |

| resourceGroupName | String | resourcetest _ | 资源集名称。 |  |  |  |
|---|---|---|---|---|---|---|
| rsId | String | 123456 | 资源集唯一编码。 |  |  |  |
| roles | Array of role |  | 用户组角色列表。 说明此参数已经废弃。 |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |  |  |  |
| arId | String | 123456 | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者。 |  |  |  |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | test | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否有效。 |  |  |  |
| id | Integer | 1 | 角色ID。 |  |  |  |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 1231 | 角色等级。 说明该参数无实际意义。 |  |  |  |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |  |  |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
|---|---|---|---|
| users | Array of user |  | 用户列表。 说明此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表。 |
| accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| active | Boolean | true | 用户是否有效。 |
| aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| backendAccountType | String | RamUser | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号。 RamUser：RAM子账号。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ctime | Long | 1606791494471 | 用户创建时间。 |
| default | Boolean | true | 是否为预置用户。 |
| defaultRoleId | Integer | 1 | 用户默认角色ID。 |
| deleted | Boolean | false | 用户是否已删除。 |
| email | String | test@example.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| enableEmail | Boolean | false | 是否启用邮件通知。 |
| enableShortMessage | Boolean | false | 是否启用短信通知。 |
| id | Integer | 1 | 用户ID。 |
| loginName | String | test | 用户登录名。 |
| loginTime | Long | 1606791494471 | 用户登录时间。 |
| mobileNationCode | String | 86 | 用户手机号码的国际区号。 |
| mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |
| muserId | String | admin | 用户最近一次修改的修改者用户名。 |
| organizationId | Integer | 1 | 用户所属组织的ID。 |
| password | String | H2xWN****** | 用户密码。 |
| ramUser | Boolean | true | 是否为RAM用户（子账号）。 |

| userLoginCtrlId | Integer | 34 | 登录策略ID。 |  |  |  |
|---|---|---|---|---|---|---|
| username | String | test | 用户显示名。 |  |  |  |
| userRoles | Array of userRole |  | 用户所绑定的角色的列表。 |  |  |  |
| active | Boolean | true | 用户所绑定的角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-9999****** | 用户所绑定角色的唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 用户所绑定角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 用户所绑定角色创建者的用户名。 |  |  |  |
| default | Boolean | true | 用户所绑定角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.resourceUser.descript ion | 用户所绑定角色的描述。 |  |  |  |
| enable | Boolean | true | 用户所绑定角色是否有效。 |  |  |  |
| id | Integer | 2 | 用户所绑定角色ID。 |  |  |  |
| muserId | String | admin | 用户所绑定角色最近一次修改的修改者用户名。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 用户所绑定角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 用户所绑定角色的所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 用户所绑定角色是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 用户所绑定角色的等级。 说明保留字段，无实际作用。 |  |  |  |
| roleName | String | defaultRole.resourceUser.name | 用户所绑定角色的名称。 |  |  |  |
| roleRange | String | roleRange.resourceSet | 用户所绑定角色的管理权限： roleRange.allOrganizations为所有组织。 roleRange.orgAndSubOrgs为本组织及级联下级组织。 roleRange.resourceSet为资源集。 roleRange.userGroup为RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 用户所绑定角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
|---|---|---|---|
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 1 | 数据总条数。 |
| totalPage | Integer | 1 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "loginName": "testuser",
    "roleId": 6
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>188</cost> <code>200</code> <data> <cellphoneNum>188*****188</cellphoneNum> <enableDingTalk>false</enableDingTalk> <displayName>user_test</displayName> <parentPk>1689406703302188</parentPk> <lastLoginTime>1606675230000</lastLoginTime> <default>false</default> <deleted>false</deleted> <loginName>user_test</loginName> <mobileNationCode>86</mobileNationCode> <id>1</id> <enableEmail>false</enableEmail> <enableShortMessage>false</enableShortMessage> <email>xxx@alibaba-inc.com</email> <status>ACTIVE</status> <primaryKey>212530506704030466</primaryKey> </data> <data> <userGroupRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>111</arId> <code>ROLE_RESOURCE_USER</code> <description>test</description> |  |

```xml
desc pto test/desc pto
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>111</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userGroupRoles>
    <userGroups>
        <organizationId>1</organizationId>
        <createTimeStamp>1606791494471</createTimeStamp>
        <groupName>ack-user-old</groupName>
        <augId>1111</augId>
        <id>1</id>
    </userGroups>
    <userGroups>
        <resourceSets>
            <organizationID>1</organizationID>
            <creator>admin</creator>
            <resourceGroupName>resource_test</resourceGroupName>
            <gmtCreated>1606791494471</gmtCreated>
            <rsId>123456</rsId>
            <id>1</id>
        </resourceSets>
        <users>
            <muserId>admin</muserId>
            <backendAccountType>RamUser</backendAccountType>
            <enableDingTalk>false</enableDingTalk>
            <mtime>1606791494471</mtime>
            <organizationId>1</organizationId>
            <password>H2xWN******</password>
            <default>true</default>
            <loginTime>1606791494471</loginTime>
            <userLoginCtrlId>34</userLoginCtrlId>
            <loginName>test</loginName>
            <ctime>1606791494471</ctime>
            <id>1</id>
            <enableShortMessage>false</enableShortMessage>
            <email>xxx@alibaba-inc.com</email>
            <defaultRoleId>1</defaultRoleId>
            <cellphoneNum>00000000000</cellphoneNum>
            <aliyunUser>false</aliyunUser>
            <accountType>1</accountType>
            <active>true</active>
            <deleted>false</deleted>
            <mobileNationCode>86</mobileNationCode>
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.orgAndSubOrgs</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>123456</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>test</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>true</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>defaultRole.resourceUser.name</roleName>
            <roleLevel>1231</roleLevel>
            <id>1</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
    </userGroups>
    <userGroups>
        <organization>
            <muserId>admin</muserId>
            <internal>true</internal>
            <level>123</level>
            <supportRegions>["cn-**-d01"]</supportRegions>
            <mtime>1606791494471</mtime>
            <uuid>123456</uuid>
            <parentId>1</parentId>
            <multiCloudStatus>master</multiCloudStatus>
            <supportRegionList>cn-**-d01</supportRegionList>
            <name>test</name>
            <ctime>1606791494471</ctime>
            <alias>test</alias>
<id>1</id>
```

```xml
            <id>1</id>
            <cuserId>admin</cuserId>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>1111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>123</roleLevel>
        <id>1</id>
        <organizationVisibility>defaultRole.resourceUser.description</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-**-d01</region>
        <cuserId>5013</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>JGdgSN2p******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>111</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </roles>
</data> <data>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>111</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>test</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>role_test</roleName>
        <roleLevel>1</roleLevel>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <ipRanges>
            <ipRange>0.0.0.0</ipRange>
            <protocol>IPV4</protocol>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <startTime>00.00</startTime>
            <loginPolicyId>1</loginPolicyId>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>policy_test</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>111</lpId>
```

```xml
        <cuserId>admin</cuserId>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>true</internal>
        <level>0.1</level>
        <supportRegions>["cn-***-d01"]</supportRegions>
        <mtime>1606791494471</mtime>
        <uuid>123456</uuid>
        <parentId>1</parentId>
        <multiCloudStatus>master</multiCloudStatus>
        <supportRegionList>cn-***-d01</supportRegionList>
        <name>test</name>
        <ctime>1607512443989</ctime>
        <alias>test</alias>
        <id>1</id>
        <cuserId>admin</cuserId>
    </organization>
</data> <success>true</success> <pageInfo>
    <total>40</total>
    <totalPage>2</totalPage>
    <pageSize>20</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 188, "code": 200, "data": [ { "cellphoneNum": "188*****188", "enableDingTalk": false, "displayName": "user_test", "parentPk": 1689406703302188, "lastLoginTime": 1606675230000, "default": false, "deleted": false, "loginName": "user_test", "mobileNationCode": 86, "id": 1, "enableEmail": false, "enableShortMessage": false, "email": "xxx@alibaba-inc.com", "status": "ACTIVE", "primaryKey": 212530506704030460 }, { "userGroupRoles": { "roleRange": "roleRange.orgAndSubOrgs", "rAMRole": false, "muserId": "admin", "arId": 111, "code": "ROLE_RESOURCE_USER", "description": "test", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "role_test", "roleLevel": 111, "id": 1, "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "userGroups": [ { "organizationId": 1, "createTimeStamp": 1606791494471, "groupName": "ack-user-old", "augId": 1111, "id": 1 }, { "resourceSets": { "organizationID": 1, "creator": "admin", "resourceGroupName": "resource_test", "gmtCreated": 1606791494471, "rsId": 123456, "id": 1 |  |

```json
                        id: 1
                    },
                    "users": {
                        "muserId": "admin",
                        "backendAccountType": "RamUser",
                        "enableDingTalk": false,
                        "mtime": 1606791494471,
                        "organizationId": 1,
                        "password": "H2xWN******",
                        "default": true,
                        "loginTime": 1606791494471,
                        "userLoginCtrlId": 34,
                        "loginName": "test",
                        "ctime": 1606791494471,
                        "id": 1,
                        "enableShortMessage": false,
                        "email": "xxx@alibaba-inc.com",
                        "defaultRoleId": 1,
                        "cellphoneNum": 0,
                        "aliyunUser": false,
                        "accountType": 1,
                        "active": true,
                        "deleted": false,
                        "mobileNationCode": 86,
                        "ramUser": true,
                        "enableEmail": false,
                        "username": "test"
                    },
                    "roles": {
                        "roleRange": "roleRange.orgAndSubOrgs",
                        "rAMRole": false,
                        "muserId": "admin",
                        "arId": 123456,
                        "code": "ROLE_RESOURCE_USER",
                        "description": "test",
                        "active": true,
                        "roleType": "ROLETYPE_ASCM",
                        "default": true,
                        "ownerOrganizationId": 1,
                        "enable": true,
                        "roleName": "defaultRole.resourceUser.name",
                        "roleLevel": 1231,
                        "id": 1,
                        "organizationVisibility": "organizationVisibility.global",
                        "cuserId": "admin"
                    }
                },
                {
                    "organization": {
                        "muserId": "admin",
                        "internal": true,
                        "level": 123,
                        "supportRegions": "[\"cn-**-d01\"]",
                        "mtime": 1606791494471,
                        "uuid": 123456,
                        "parentId": 1,
                        "multiCloudStatus": "master",
                        "supportRegionList": "cn-**-d01",
                        "name": "test",
                        "ctime": 1606791494471,
                        "alias": "test",
                        "id": 1,
                        "cuserId": "admin"
                    }
                }
```

`],`

```json
            "userRoles": {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": false,
                "muserId": "admin",
                "arId": 1111,
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": true,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "defaultRole.resourceUser.name",
                "roleLevel": 123,
                "id": 1,
                "organizationVisibility": "defaultRole.resourceUser.description",
                "cuserId": "admin"
            },
            "accessKeys": {
                "ctime": 1606675230000,
                "id": 1,
```

```json
                "region": "cn-**-d01",
                "cuserId": 5013,
                "status": "ACTIVE",
                "accesskeyId": "JGdgSN2p******"
            },
            "roles": {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": false,
                "muserId": "admin",
                "arId": 111,
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": true,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "role_test",
                "roleLevel": 111,
                "id": 1,
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            }
        },
        {
            "defaultRole": {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": false,
                "muserId": "admin",
                "arId": 111,
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": true,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "role_test",
                "roleLevel": 1,
                "id": 1,
                "organizationVisibility": "organizationVisibility.global"
            },
            "loginPolicy": {
                "ipRanges": {
                    "ipRange": "0.0.0.0",
                    "protocol": "IPV4",
                    "loginPolicyId": 1
                },
                "muserId": "admin",
                "default": false,
                "ownerOrganizationId": 1,
                "timeRanges": {
                    "startTime": 0,
                    "loginPolicyId": 1,
                    "endTime": "24:00"
                },
                "enable": true,
                "name": "policy_test",
                "rule": "ALLOW",
                "id": 1,
                "organizationVisibility": "organizationVisibility.global",
                "lpId": 111,
                "cuserId": "admin"
            },
            "organization": {
                "muserId": "admin",
                "internal": true,
                "level": 0.1,
                "supportRegions": "[\"cn-***-d01\"]",
                "mtime": 1606791494471,
                "uuid": 123456,
                "parentId": 1,
                "multiCloudStatus": "master",
                "supportRegionList": "cn-***-d01",
                "name": "test",
                "ctime": 1607512443989,
                "alias": "test",
                "id": 1,
                "cuserId": "admin"
            }
        }
```

`],`

```json
    "success": true,
    "pageInfo": {
        "total": 40,
        "totalPage": 2,
        "pageSize": 20,
```

```json
        "currentPage": 1
    },
    "message": "success"
}
```

###### 4.1.1.4.19. ListUsersInsideRole

查询某角色下用户集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/listUsersInsideRole HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| organizationId | Integer | Body | 否 | 3 | 用户所属组织ID，可通过调用GetOrganizationList接口获取。 说明以用户所属组织ID为条件查询属于这个组织的用户信息，不传则忽略此条件。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 每页显示数据条数，默认为符合以上条件的所有数据的条数。 |
| loginName | String | Body | 否 | test | 登录用户名的SQL正则表达式。 说明传入此参数会根据用户名正则匹配查询，不传则返回所有拥有该角色的用户。 |
| roleId | Integer | Body | 否 | 1 | 用户关联的角色ID，可通过调用ListRoles接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| action | String | ListUsersInsideRole |  |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |

| cost | Long | 22 | 接口响应耗时，单位毫秒（ms）。 |
|---|---|---|---|
| data | Array of userKeyInfo |  | 用户集。 |
| Id | Integer | 5003 | 用户ID。 |
| displayName | String | admin | 用户显示名。 |
| loginName | String | admin | 用户名称。 |
| organizationId | Integer | 3 | 用户所属组织的ID。 |
| organizationName | String | test | 用户所属组织的名称。 |
| status | String | ACTIVE | 用户当前状态。 ACTIVE：激活。 INACTIVE：禁用。 |
| domain | String | ascm.aliyun.com | 报错服务的域名。 说明无论接口是否报错都会返回。 |
| errorKey | String | ascm.auth.InvalidParameter | 错误码。 ascm.auth.ServerUnknownException：服务内部发生未知异常。 ascm.auth.InternalError：内部错误。 ascm.auth.InvalidParameter：参数错误。 ascm.auth.SystemEncodeException：系统编码异常。 ascm.auth.NetIOException：后端网络存在异常。 ascm.auth.CallBackendServiceReturnEmptyException：调用后端服务，返回了空的Response。 ascm.auth.ForbidCallTheInterface：该功能已经下线，禁止调用。 ascm.auth.NoPermission：没有权限。 ascm.auth.CallTairException：调用Tair服务异常。 ascm.auth.EntityNotExist.Organization：组织不存在。 ascm.auth.EntityNotExist.UserGroup：用户组不存在。 ascm.auth.account.notLoggedIn：用户未登录或登录状态失效。 ascm.auth.EntityNotExist.User：用户不存在。 ascm.auth.exceeded.userUserGroup：用户加入的用户组数量超过限制。 ascm.auth.UnknownException：内部未知异常。 ascm.auth.CallDataBaseException：访问数据库异常。 ascm.auth.PageSizeBeyondQuota：PageSize不能超过限定数值。 ascm.auth.internalServerError：服务出现内部错误，请检查服务。 ascm.auth.EntityNotExist：实体不存在。 |
| extraMessage | String | success | 额外的提示信息，对错误提示信息的补充说明。 说明仅在接口调用失败异常时返回。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页码。 |
| pageSize | Integer | 10 | 每页数据条数。 |
| total | Integer | 10 | 数据总条数。 |

| totalPage | Integer | 1 | 总页数。 |
|---|---|---|---|
| requestId | String | 5FE0023D-73C3-481E-926D- 17A2CF****** | 本次请求链路ID。 |
| serverRole | String | unimanager- base.IdentityService# | 接口对应服务的SR（服务角色）名称。 |
| successResponse | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/listUsersInsideRole HTTP/1.1
```

公共请求头

```json
{ "RoleId": "1" }
```

正常返回示例

| XML | 格式 |
|---|---|
| <ServerRole>unimanager-base.IdentityService#</ServerRole> <Action> ListUsersInsideRole</Action> <SuccessResponse>true</SuccessResponse> <PageInfo> <TotalPage>1</TotalPage> <PageSize>10</PageSize> <CurrentPage>1</CurrentPage> <Total>10</Total> </PageInfo> <RequestId>5FE0023D-73C3-481E-926D-17A2CF******</RequestId> <Message>success</Message> <ErrorKey>ascm.auth.InvalidParamete</ErrorKey> <Data> <OrganizationName>test</OrganizationName> <Status>ACTIVE</Status> <LoginName>admin</LoginName> <DisplayName>admin</DisplayName> <OrganizationId>3</OrganizationId> <Id>5003</Id> </Data> <Domain>ascm.aliyun.com</Domain> <ExtraMessage>success</ExtraMessage> <Cost>22</Cost> <Code>200</Code> |  |

| JSON | 格式 |
|---|---|
| { "ServerRole": "unimanager-base.IdentityService#", "Action": "ListUsersInsideRole", "SuccessResponse": true, "PageInfo": { "TotalPage": 1, "PageSize": 10, "CurrentPage": 1, "Total": 10 }, "RequestId": "5FE0023D-73C3-481E-926D-17A2CF******", "Message": "success", "ErrorKey": "ascm.auth.InvalidParamete", "Data": { "OrganizationName": "test", "Status": "ACTIVE", "LoginName": "admin", "DisplayName": "admin", "OrganizationId": 3, "Id": 5003 }, "Domain": "ascm.aliyun.com", "ExtraMessage": "success", "Cost": 22, "Code": 200 } |  |

###### 4.1.1.4.20. LockUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 3 | 用户ID。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要锁定的用户。 |
| loginName | String | Body | 否 | testuser | 用户登录名。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要锁定的用户。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
{
    "loginName": "testuser"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.21. TransferUser

TransferUser API允许管理员在统一云管平台中进行用户转移及角色重新分配。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /user/action/transfer HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser | 用户登录名。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizationId | Integer | Body | 否 | 1 | 组织ID，用于指定组织范围。组织ID可通过调用 GetOrganizationList接口获取。 |
| roleIdList | RepeatList | Body | 是 | {"RoleIdList": [ "5", "6", "8" ]} | 角色ID列表。可通过调用ListActiveRoles接口获取。 此参数为非必填，缺省值是资源使用人角色的ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的. 自定义角色的code由系统生成。格式为： ROLE _英文大写的角色名称_随机串。 |
| errorKey | String | exampleErrKey | 错误码。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例

```
PUT /user/action/transfer HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"exampleErrKey", "code":"ROLE_RESOURCE_USER", "cost":121, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <errorKey>exampleErrKey</errorKey> <code>ROLE_RESOURCE_USER</code> <cost>121</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.22. ModifyUserInformation

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/modifyUserInformation HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 5817 | 根据用户ID修改用户信息时传入的被修改用户的 ID。 说明当传入loginName时，id参数可不传。id和loginName同时传入时，id参数的优先级更高。系统用户id可通过调用ListUsers接口获取。历史用户id可通过调用ListDeletedUsers接口获取。 |
| loginName | String | Body | 否 | testuser2022 | 根据用户登录名称修改用户信息时传入的被修改用户的登录名称。 说明当传入id参数时，此参数可不传。id和loginName同时传入时，id参数的优先级更高。 |
| displayName | String | Body | 否 | testuser2022 | 修改后的用户显示名。用户显示名由英文大小写字母、数字、中文、短划线（-）、半角句号 （.）、或at（@）组成，长度为1~128个字符。 |
| loginPolicyId | Integer | Body | 否 | 1084 | 修改后的与用户绑定的登录策略id，可通过调用 ListLoginPolicies接口获取。 |
| mobileNationCode | String | Body | 否 | 86 | 修改后用户手机号码的国际区号。 |
| cellphoneNum | String | Body | 否 | 188****8888 | 修改后的用户手机号码。 |
| telephoneNum | String | Body | 否 | 029******* | 修改后的用户座机号码。 |
| email | String | Body | 否 | test@example.com | 修改后的用户邮箱地址。 |
| description | String | Body | 否 | test data | 修改后的用户描述。 |
| dingTalkToken | String | Body | 否 | 177****62sdsa | 修改后的钉钉密钥。 说明创建用户时指定的自定义钉钉机器人的加签名密钥。 |
| enableDingTalk | Boolean | Body | 否 | true | 是否启用钉钉通知。 true：启用。 false：关闭。 |
| enableShortMessa ge | Boolean | Body | 否 | true | 是否启用短信通知。 true：启用。 false：关闭。 |
| enableEmail | Boolean | Body | 否 | true | 是否启用邮件通知。 true：启用。 false：关闭。 |
| multiCloudStatus | String | Body | 否 | slave | 是否为多云同步用户，默认为null。 master：主云。 slave：从云。 null。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 89 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| data | Struct | - | 修改后的用户信息。 |
| -accessKeys | Array | - | AccessKey信息列表。只有超级管理员才能获取预置用户的AccessKey和 AccessKey Secret。 |
| --accesskeyId | String | JGdgSN2pVY****** | AccessKey ID。 |
| --ctime | Long | 1606675230000 | AccessKey创建时间。 |
| --cuserId | String | admin | AccessKey创建者的用户名。 |
| --id | Integer | 1 | AccessKey的识别主键。 |
| --region | String | cn-qingdao-****-d01 | AccessKey可用区域。 |
| --status | String | active | AccessKey状态。 active：激活。 inactive：禁用。 |
| -roles | Array | - | 角色列表。 |
| --active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |
| --arId | String | ar-9999****** | 角色唯一编码。 |
| --code | String | ROLEGLOBALRESOURCEAUDIT _ _ _ OR | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。自定义角色的code由系统生成，格式为：ROLE _英文大写的角色名称_随机串。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --default | Boolean | true | 是否为预置角色。 预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.globalResourceAudito r.description | 角色描述。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 6 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| --organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| --rAMRole | Boolean | false | 是否为RAM角色。 |
| --roleLevel | Integer | 11231 | 角色等级。 说明保留字段，无实际作用。 |
| --roleName | String | defaultRole.globalResourceAudito r.name | 角色名称。 |
| --roleRange | String | roleRange.allOrganizations | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -userGroupRoles | Array | - | 用户组角色列表。 |
| --active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| --arId | String | ar-9999****** | 角色唯一编码。 |
| --code | String | ROLERESOURCESETADMIN _ _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。自定义角色的code由系统生成，格式为：ROLE _英文大写的角色名称_随机串。 |
| --cuserId | String | admin | 角色创建者的用户名。 说明此参数已经废弃。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.resourceSetAdmin.de scription | 角色描述。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 1 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |
| --organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| --rAMRole | Boolean | false | 是否为RAM角色。 |
| --roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| --roleName | String | defaultRole.resourceSetAdmin.na me | 角色名称。 |
| --roleRange | String | roleRange.resourceSet | 角色管理权限范围： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：为RAM角色所在用户组。 |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -userGroups | Array | - | 用户组列表。 |
| --resourceSets | Array | - | 资源集列表。此参数已经废弃。 |
| ---creator | String | admin | 资源集创建者的用户名。 |
| ---gmtCreated | Long | 1606675230000 | 资源集创建时间。 |
| ---id | Integer | 1 | 资源集ID。 |
| ---organizationID | Integer | 1 | 资源集所属组织的ID。 |
| ---resourceGroupName | String | restest _ | 资源集名称。 |
| ---rsId | String | 11231a | 资源集唯一编码。 |
| --roles | Array | - | 角色列表。此参数已经废弃。 |
| ---active | Boolean | true | 角色是否有效。 说明该参数已废弃。 |
| ---arId | String | 11231 | 角色唯一编码。 |
| ---code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。内置角色code是固定的。自定义角色的code由系统生成，格式为：ROLE _英文大写的角色名称_随机串。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---cuserId | String | admin | 角色创建者的用户名。 |
| ---default | Boolean | false | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| ---description | String | roletest _ | 角色描述。 |
| ---enable | Boolean | true | 角色是否有效。 |
| ---id | Integer | 1 | 角色ID。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| ---organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ---ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| ---rAMRole | Boolean | false | 是否为RAM角色。 |
| ---roleLevel | Integer | 11231 | 角色等级。 说明该参数目前无实际含义。 |
| ---roleName | String | roletest _ | 角色名称。 |
| ---roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限范围： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| ---roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| --users | Array | - | 用户列表。 说明此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表。 |
| ---accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| ---active | Boolean | true | 用户是否有效。 |
| ---aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| ---backendAccountType | String | AscmUser | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号。 RamUser：RAM子账号。 |
| ---cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ---ctime | Long | 1607071602000 | 用户创建时间。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---default | Boolean | false | 是否为预置用户。 |
| ---defaultRoleId | Integer | 1 | 用户默认角色ID。 |
| ---deleted | Boolean | false | 用户是否已删除。 |
| ---email | String | test@example.com | 用户邮箱地址。 |
| ---enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| ---enableEmail | Boolean | false | 是否启用邮件通知。 |
| ---enableShortMessage | Boolean | false | 是否启用短信通知。 |
| ---id | Integer | 1 | 用户ID。 |
| ---loginName | String | test | 用户登录名。 |
| ---loginTime | Long | 1606675230000 | 用户最近一次登录的时间。 |
| ---mobileNationCode | String | 86 | 国际电话区号。 |
| ---mtime | Long | 1712261405521 | 用户最近一次修改的时间。 |
| ---muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| ---organizationId | Integer | 1 | 所属组织ID。 |
| ---password | String | Harbor****** | 用户密码。 |
| ---ramUser | Boolean | false | 是否为RAM用户（子账号）。 |
| ---userLoginCtrlId | Integer | 34 | 登录控制ID。 |
| ---username | String | test | 用户显示名。 |
| --augId | String | 11231 | 用户组唯一编码。 |
| --createTimeStamp | Long | 1527690629357 | 用户组创建时间。 |
| --groupName | String | test | 用户组名称。 |
| --id | Integer | 145 | 用户组ID。 |
| --organizationId | Integer | 3 | 所属组织ID。 |
| --organization | Struct | - | 组织信息。 |
| ---supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| ---alias | String | sub-org-1 | 组织别名。系统自动生成，一般与组织名称一致。 |
| ---ctime | Long | 1606791494471 | 组织创建的时间。 |
| ---cuserId | String | admin | 组织创建者的用户名。 |
| ---id | Integer | 25 | 组织ID。 |
| ---internal | Boolean | false | 是否为预置组织。预置组织即系统自动生成的组织，也称为默认组织。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---level | String | 0.1.24 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| ---mtime | Long | 1712261405521 | 组织最近一次修改的时间。 |
| ---multiCloudStatus | String | slave | 是否为多云同步组织。 说明该参数仅在多云场景下返回。 master：主云。 slave：从云。 |
| ---muserId | String | admin | 组织最近一次修改的修改者用户名。 |
| ---name | String | sub-org-1 | 组织名称。 |
| ---parentId | Integer | 24 | 父组织ID。 |
| ---supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 说明该参数已经废弃。 |
| ---uuid | String | org-101cc0654e910a42092****w | 组织UUID。 |
| -userRoles | Array | - | 用户角色列表。 |
| --active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |
| --arId | String | ar-9999****** | 角色唯一编码。 |
| --code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。自定义角色的code由系统生成，格式为：ROLE _英文大写的角色名称_随机串。 |
| --cuserId | String | admin | 角色创建者的用户名。 说明该参数已废弃。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.resourceUser.descript ion | 角色描述。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 2 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。 说明该参数已废弃。 |
| --organizationVisibility | String | organizationVisibility.global | 共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 所属组织ID。 |

| 参数名称 | 类型 | 示例 | 说明 |  |
|---|---|---|---|---|
| --rAMRole | Boolean | false | 是否为RAM角色。 |  |
| --roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |  |
| --roleName | String | defaultRole.resourceUser.name | 角色名称。 |  |
| --roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限范围： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |
| -cellphoneNum | String | 188****8888 | 修改后的用户手机号码。 |  |
| -telephoneNum | String | 029******* | 修改后的用户座机号码。 |  |
| -default | Boolean | false | 是否为预置用户。 |  |
| -deleted | Boolean | false | 用户是否已被删除，已删除的用户为历史用户，历史用户可被修改。 true：已经被删除。 false：未被删除。 |  |
| -displayName | String | testuser2022 | 用户显示名。 |  |
| -email | String | test@example.com | 用户邮箱地址。 |  |
| -enableDingTalk | Boolean | true | 是否启用钉钉通知。 |  |
| -enableEmail | Boolean | true | 是否启用邮件通知。 |  |
| -enableShortMessage | Boolean | true | 是否启用短信通知。 |  |
| -id | Integer | 5817 | 用户ID。 |  |
| -lastLoginTime | Long | 1606675230000 | 用户最近一次登录的时间。 |  |
| -loginName | String | testuser2022 | 用户登录名。 |  |
| -mobileNationCode | String | 86 | 国际电话区号。 |  |
| -parentPk | String | 112715760893**** | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |  |
| -primaryKey | String | 25925866254468**** | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号）一致。 |  |
| -status | String | active | 用户状态。 active：激活。 inactive：禁用。 |  |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -defaultRole | Struct | - | 默认角色。 |
| --active | Boolean | true | 角色是否有效。 说明此参数已经废弃，角色状态以enable参数为准。 |
| --arId | String | ar-9999**** | 角色唯一编码。 |
| --code | String | ROLEORGANIZATIONADMIN _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。自定义角色的code由系统生成，格式为：ROLE _英文大写的角色名称_随机串。 |
| --default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、 全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| --description | String | defaultRole.organizationAdmin.de scription | 角色描述。 |
| --enable | Boolean | true | 角色是否有效。 |
| --id | Integer | 4 | 角色ID。 |
| --muserId | String | admin | 角色最近一次修改的修改者用户名。此参数已经废弃。 |
| --organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| --ownerOrganizationId | Integer | 1 | 角色所属组织的ID。 |
| --rAMRole | Boolean | false | 是否为RAM角色。 |
| --roleLevel | Integer | 2147483647 | 角色等级。该参数无实际作用。 |
| --roleName | String | defaultRole.organizationAdmin.na me | 角色名称。 |
| --roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限范围： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| --roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| -loginPolicy | Struct | - | 登录策略。 |
| --ipRanges | Array | - | IP段。 |
| ---ipRange | String | 10.***.***.1/24 | 登录策略的IP范围, |
| ---loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| ---protocol | String | IPV4 | 登录策略所使用的协议，目前仅支持IPv4。 |
| --timeRanges | Array | - | 时间段。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---endTime | String | 18:00 | 结束时间。 |
| ---loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| ---startTime | String | 08:00 | 开始时间。 |
| --cuserId | String | admin | 登录策略创建者。 |
| --default | Boolean | false | 是否为默认登录策略。 |
| --enable | Boolean | true | 登录策略是否有效。 |
| --id | Integer | 1084 | 登录策略ID。 |
| --lpId | String | lp-101de13d33320a420d2***** | 登录策略唯一编码。 |
| --muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| --name | String | mytest | 登录策略名。 |
| --organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享 |
| --ownerOrganizationId | Integer | 1 | 登录策略所属组织的ID。 |
| --rule | String | DENY | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| -organization | Struct | - | 创建的用户所属的组织信息。 说明此参数已经废弃，若要查询用户组所属组织详细信息，请根据 organizationId参数通过GetOrganization接口查询。 |
| --supportRegionList | List | ["cn-qingdao-****-d01"] | 可用区列表。 |
| --alias | String | test | 组织别名。系统自动生成，一般与组织名称一致。 |
| --ctime | Long | 1606675230000 | 组织创建时间。 |
| --cuserId | String | admin | 组织创建者的用户名。 |
| --id | Integer | 1 | 组织ID。 |
| --internal | Boolean | false | 是否为预置组织。预置组织即系统自动生成的组织，也称为默认组织。 |
| --level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的 level=0.1。其中0.1中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为3的一级组织的直接下级组织level=0.1.3。 |
| --mtime | Long | 1606675230001 | 组织最近一次修改的时间。 |
| --multiCloudStatus | String | master | 是否为多云同步组织。 说明该参数仅在多云场景下返回。 master：主云。 slave：从云。 |
| --muserId | String | admin | 组织最近一次修改的修改者用户名。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --name | String | test | 组织名称。 |
| --parentId | Integer | 0 | 父组织ID。 |
| --supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |
| --uuid | String | 11231 | 组织UUID。 |

**示例**

请求示例

```json
POST /ascm/auth/user/modifyUserInformation HTTP/1.1 {
    "id":5817,
    "loginName":"testuser2022"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":89, "data":{ "cellphoneNum":"188****8888", "telephoneNum":"029*******", "displayName":"testuser2022", "enableDingTalk":true, "defaultRole":{ "roleRange":"roleRange.orgAndSubOrgs", "arId":"ar-9999****", "muserId":"admin", "rAMRole":false, "code":"ROLE_ORGANIZATION_ADMIN", "active":true, "description":"defaultRole.organizationAdmin.description", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.organizationAdmin.name", "id":4, "roleLevel":2147483647, "organizationVisibility":"organizationVisibility.global" }, "userRoles":[ { "roleRange":"roleRange.orgAndSubOrgs", "arId":"ar-9999******", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"defaultRole.resourceUser.description", "roleType":"ROLETYPE_ASCM", "default":true, "ownerOrganizationId":1, "enable":true, "roleName":"defaultRole.resourceUser.name", "id":2, "roleLevel":2147483647, "cuserId":"admin", "organizationVisibility":"organizationVisibility.global" } ], "userGroups":[ { "roles":[ { "roleRange":"roleRange.orgAndSubOrgs", "arId":"11231", "muserId":"admin", "rAMRole":false, "code":"ROLE_RESOURCE_USER", "active":true, "description":"role_test", "roleType":"ROLETYPE_ASCM", "default":false, "ownerOrganizationId":1, "enable":true, |  |

,

```json
      "roleName":"role_test",
      "id":1,
      "roleLevel":11231,
      "cuserId":"admin",
      "organizationVisibility":"organizationVisibility.global"
     }
```

`],`

```json
    "organizationId":3,
    "users":[
     {
      "cellphoneNum":"188****8888",
      "muserId":"admin",
      "aliyunUser":false,
      "backendAccountType":"AscmUser",
      "enableDingTalk":false,
      "accountType":1,
      "active":true,
      "mtime":1712261405521,
      "organizationId":1,
      "default":false,
      "password":"Harbor******",
      "deleted":false,
      "loginTime":1606675230000,
      "userLoginCtrlId":34,
      "loginName":"test",
      "ctime":1607071602000,
      "id":1,
      "mobileNationCode":"86",
      "enableEmail":false,
      "ramUser":false,
      "defaultRoleId":1,
      "email":"test@example.com",
      "enableShortMessage":false,
      "username":"test"
     }
```

`],`

```json
    "groupName":"test",
    "augId":"11231",
    "resourceSets":[
     {
      "organizationID":1,
      "creator":"admin",
      "resourceGroupName":"res_test",
      "gmtCreated":1606675230000,
      "rsId":"11231a",
      "id":1
     }
```

`],`

```json
    "createTimeStamp":1527690629357,
    "organization":[
     {
      "muserId":"admin",
      "internal":false,
      "level":"0.1.24",
      "supportRegions":"cn-qingdao-****-d01",
      "mtime":1712261405521,
      "uuid":"org-101cc0654e910a42092****w",
      "parentId":24,
      "multiCloudStatus":"slave",
      "supportRegionList":"[\"cn-qingdao-****-d01\"]",
      "name":"sub-org-1",
      "alias":"sub-org-1",
      "ctime":1606791494471,
      "id":25,
      "cuserId":"admin"
     }
```

`],`

```json
    "id":145
   }
```

`],`

```json
  "organization":{
   "muserId":"admin",
   "internal":false,
   "level":"0.1",
   "supportRegions":"cn-qingdao-****-d01",
   "mtime":1606675230001,
   "uuid":"11231",
   "parentId":0,
   "multiCloudStatus":"master",
   "supportRegionList":"[\"cn-qingdao-****-d01\"]",
   "name":"test",
   "alias":"test",
   "ctime":1606675230000,
   "id":1,
   "cuserId":"admin"
  },
"parentPk":"112715760893****"
```

```json
  parentPk:112715760893****,
  "lastLoginTime":1606675230000,
  "default":false,
  "deleted":false,
  "roles":[
   {
    "roleRange":"roleRange.allOrganizations",
    "arId":"ar-9999******",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_GLOBAL_RESOURCE_AUDITOR",
    "active":true,
    "description":"defaultRole.globalResourceAuditor.description",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.globalResourceAuditor.name",
    "id":6,
    "roleLevel":11231,
    "organizationVisibility":"organizationVisibility.global"
   }
```

`],`

```json
  "userGroupRoles":[
   {
    "roleRange":"roleRange.resourceSet",
    "arId":"ar-9999******",
    "muserId":"admin",
    "rAMRole":false,
    "code":"ROLE_RESOURCE_SET_ADMIN",
    "active":true,
    "description":"defaultRole.resourceSetAdmin.description",
    "roleType":"ROLETYPE_ASCM",
    "default":true,
    "ownerOrganizationId":1,
    "enable":true,
    "roleName":"defaultRole.resourceSetAdmin.name",
    "id":1,
    "roleLevel":2147483647,
    "cuserId":"admin",
    "organizationVisibility":"organizationVisibility.global"
   }
```

`],`

```json
  "loginName":"testuser2022",
  "accessKeys":[
   {
    "ctime":1606675230000,
    "id":1,
    "region":"cn-qingdao-****-d01",
    "cuserId":"admin",
    "accesskeyId":"JGdgSN2pVY******",
    "status":"active"
   }
```

`],`

```json
  "id":5817,
  "mobileNationCode":"86",
  "enableEmail":true,
  "email":"test@example.com",
  "enableShortMessage":true,
  "primaryKey":"25925866254468****",
  "status":"active",
  "loginPolicy":{
   "ipRanges":[
    {
     "protocol":"IPV4",
     "ipRange":"10.***.***.1/24",
     "loginPolicyId":1084
    }
```

`],`

```json
   "timeRanges":[
    {
     "loginPolicyId":1084,
     "startTime":"08:00",
     "endTime":"18:00"
    }
```

`],`

```json
   "muserId":"admin",
   "default":false,
   "ownerOrganizationId":1,
   "enable":true,
   "name":"mytest",
   "rule":"DENY",
   "id":1084,
   "cuserId":"admin",
   "lpId":"lp-101de13d33320a420d2*****",
   "organizationVisibility":"organizationVisibility.global"
  }
```

```json
 },
 "success":true,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>89</cost> <data> <cellphoneNum>188****8888</cellphoneNum> <telephoneNum>029*******</telephoneNum> <displayName>testuser2022</displayName> <enableDingTalk>true</enableDingTalk> <defaultRole> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-9999****</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_ORGANIZATION_ADMIN</code> <active>true</active> <description>defaultRole.organizationAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.organizationAdmin.name</roleName> <id>4</id> <roleLevel>2147483647</roleLevel> <organizationVisibility>organizationVisibility.global</organizationVisibility> </defaultRole> <userRoles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>ar-9999******</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>defaultRole.resourceUser.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceUser.name</roleName> <id>2</id> <roleLevel>2147483647</roleLevel> <cuserId>admin</cuserId> <organizationVisibility>organizationVisibility.global</organizationVisibility> </userRoles> <userGroups> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <arId>11231</arId> <muserId>admin</muserId> <rAMRole>false</rAMRole> <code>ROLE_RESOURCE_USER</code> <active>true</active> <description>role_test</description> <roleType>ROLETYPE_ASCM</roleType> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>role_test</roleName> <id>1</id> <roleLevel>11231</roleLevel> <cuserId>admin</cuserId> <organizationVisibility>organizationVisibility.global</organizationVisibility> </roles> <organizationId>3</organizationId> <users> <cellphoneNum>188****8888</cellphoneNum> <muserId>admin</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>AscmUser</backendAccountType> <enableDingTalk>false</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1712261405521</mtime> <organizationId>1</organizationId> <default>false</default> <password>Harbor******</password> <deleted>false</deleted> <loginTime>1606675230000</loginTime> <userLoginCtrlId>34</userLoginCtrlId> <loginName>test</loginName> <ctime>1607071602000</ctime> <id>1</id> |  |

```xml
   <id>1</id>
   <mobileNationCode>86</mobileNationCode>
   <enableEmail>false</enableEmail>
   <ramUser>false</ramUser>
   <defaultRoleId>1</defaultRoleId>
   <email>test@example.com</email>
   <enableShortMessage>false</enableShortMessage>
   <username>test</username>
  </users>
  <groupName>test</groupName>
  <augId>11231</augId>
  <resourceSets>
   <organizationID>1</organizationID>
   <creator>admin</creator>
   <resourceGroupName>res_test</resourceGroupName>
   <gmtCreated>1606675230000</gmtCreated>
   <rsId>11231a</rsId>
   <id>1</id>
  </resourceSets>
  <createTimeStamp>1527690629357</createTimeStamp>
  <organization>
   <muserId>admin</muserId>
   <internal>false</internal>
   <level>0.1.24</level>
   <supportRegions>cn-qingdao-****-d01</supportRegions>
   <mtime>1712261405521</mtime>
   <uuid>org-101cc0654e910a42092****w</uuid>
   <parentId>24</parentId>
   <multiCloudStatus>slave</multiCloudStatus>
   <supportRegionList>[&quot;cn-qingdao-****-d01&quot;]</supportRegionList>
   <name>sub-org-1</name>
   <alias>sub-org-1</alias>
   <ctime>1606791494471</ctime>
   <id>25</id>
   <cuserId>admin</cuserId>
  </organization>
  <id>145</id>
 </userGroups>
 <organization>
  <muserId>admin</muserId>
  <internal>false</internal>
  <level>0.1</level>
  <supportRegions>cn-qingdao-****-d01</supportRegions>
  <mtime>1606675230001</mtime>
  <uuid>11231</uuid>
  <parentId>0</parentId>
  <multiCloudStatus>master</multiCloudStatus>
  <supportRegionList>[&quot;cn-qingdao-****-d01&quot;]</supportRegionList>
  <name>test</name>
  <alias>test</alias>
  <ctime>1606675230000</ctime>
  <id>1</id>
  <cuserId>admin</cuserId>
 </organization>
 <parentPk>112715760893****</parentPk>
 <lastLoginTime>1606675230000</lastLoginTime>
 <default>false</default>
 <deleted>false</deleted>
 <roles>
  <roleRange>roleRange.allOrganizations</roleRange>
  <arId>ar-9999******</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_GLOBAL_RESOURCE_AUDITOR</code>
  <active>true</active>
  <description>defaultRole.globalResourceAuditor.description</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <roleName>defaultRole.globalResourceAuditor.name</roleName>
  <id>6</id>
  <roleLevel>11231</roleLevel>
  <organizationVisibility>organizationVisibility.global</organizationVisibility>
 </roles>
 <userGroupRoles>
  <roleRange>roleRange.resourceSet</roleRange>
  <arId>ar-9999******</arId>
  <muserId>admin</muserId>
  <rAMRole>false</rAMRole>
  <code>ROLE_RESOURCE_SET_ADMIN</code>
  <active>true</active>
  <description>defaultRole.resourceSetAdmin.description</description>
  <roleType>ROLETYPE_ASCM</roleType>
  <default>true</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
```

l df l l S di / l

```xml
  <roleName>defaultRole.resourceSetAdmin.name</roleName>
  <id>1</id>
  <roleLevel>2147483647</roleLevel>
  <cuserId>admin</cuserId>
  <organizationVisibility>organizationVisibility.global</organizationVisibility>
 </userGroupRoles>
 <loginName>testuser2022</loginName>
 <accessKeys>
  <ctime>1606675230000</ctime>
  <id>1</id>
  <region>cn-qingdao-****-d01</region>
  <cuserId>admin</cuserId>
  <accesskeyId>JGdgSN2pVY******</accesskeyId>
  <status>active</status>
 </accessKeys>
 <id>5817</id>
 <mobileNationCode>86</mobileNationCode>
 <enableEmail>true</enableEmail>
 <email>test@example.com</email>
 <enableShortMessage>true</enableShortMessage>
 <primaryKey>25925866254468****</primaryKey>
 <status>active</status>
 <loginPolicy>
  <ipRanges>
   <protocol>IPV4</protocol>
   <ipRange>10.***.***.1/24</ipRange>
   <loginPolicyId>1084</loginPolicyId>
  </ipRanges>
  <timeRanges>
   <loginPolicyId>1084</loginPolicyId>
   <startTime>08:00</startTime>
   <endTime>18:00</endTime>
  </timeRanges>
  <muserId>admin</muserId>
  <default>false</default>
  <ownerOrganizationId>1</ownerOrganizationId>
  <enable>true</enable>
  <name>mytest</name>
  <rule>DENY</rule>
  <id>1084</id>
  <cuserId>admin</cuserId>
  <lpId>lp-101de13d33320a420d2*****</lpId>
  <organizationVisibility>organizationVisibility.global</organizationVisibility>
 </loginPolicy>
</data> <success>true</success> <message>success</message>
```

###### 4.1.1.4.23. RecoverUserByLoginName

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | RecoverUserByLoginName | 系统规定参数。取值：RecoverUserByLoginName。 |
| LoginName | String | 是 | testtest | 用户登录名。 |
| OrganizationId | Integer | 是 | 5 | 组织ID。 |
| roleIdList | Json | 否 | {"RoleIdList": [ "5", "6", "8" ]} | 角色列表。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| data | Struct |  | 响应结果。 |
| accessKeys | Array of accessKey |  | AccessKey信息列表。 |
| accesskeyId | String | JGdgSN2p****** | AccessKey ID。 |

| ctime | Long | 1606675230000 | AccessKey创建时间。 |
|---|---|---|---|
| cuserId | String | admin | AccessKey创建者。 |
| id | Integer | 1 | AccessKey ID。 |
| region | String | cn-qingdao-env17-d01 | AccessKey可用区域。 |
| status | String | ACTIVE | AccessKey是否有效：active为有效，inactive为无效。 |
| cellphoneNum | String | 00000000000 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 |
| defaultRole | Struct |  | 默认角色。 |
| active | Boolean | true | 角色是否有效。 |
| arId | String | 111 | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | test | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色修改者。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围：organizationVisibility.global为全局共享，organizationVisibility.organization为本组织内共享，organizationVisibility.orgAndSubOrgs为下级组织共享。共享范围。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11321 | 角色等级。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限：roleRange.allOrganizations为所有组织，roleRange.orgAndSubOrgs为本组织及级联下级组织，roleRange.resourceSet为资源集，roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型：ROLETYPE _RAM为RAM角色，ROLETYPE _ASCM为自定义角色。 |
| deleted | Boolean | false | 用户是否删除。 |
| displayName | String | test | 用户显示名。 |
| email | String | test@163.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | false | 是否启用钉钉通知 |
| enableEmail | Boolean | false | 是否启用邮件通知。 |
| enableShortMessage | Boolean | false | 是否启用短信通知。 |

| id | Integer | 1 | 用户ID。 |
|---|---|---|---|
| lastLoginTime | Long | 1606675230000 | 用户最后登录时间。 |
| loginName | String | test | 用户登录名。 |
| loginPolicy | Struct |  | 登录策略。 |
| cuserId | String | admin | 登录策略创建者。 |
| default | Boolean | true | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |
| id | Integer | 1 | 登录策略ID。 |
| ipRanges | Array of ipRang |  | IP段。 |
| ipRange | String | 0.0.0.0/0 | IP范围。 |
| loginPolicyId | Integer | 1 | 所属登录策略ID。 |
| protocol | String | IPV4 | 使用协议。 |
| lpId | String | 11231 | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略修改者。 |
| name | String | default.loginpolicy | 登录策略名。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围：organizationVisibility.global为全局共享，organizationVisibility.organization为本组织内共享，organizationVisibility.orgAndSubOrgs为下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rule | String | ALLOW | 规则：Allow为白名单，Deny为黑名单。 |
| timeRanges | Array of timeRang |  | 时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1 | 所属登录策略ID。 |
| startTime | String | 00:00 | 开始时间。 |
| mobileNationCode | String | 86 | 区号。 |
| organization | Struct |  | 组织信息。 |
| alias | String | test | 组织别名。 |
| ctime | Long | 1606791494471 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 |
| level | String | 0.1 | 组织等级。 |
| mtime | Long | 1606791494471 | 组织修改时间。 |

| multiCloudStatus | String | master | 是否为多云同步组织：master为主云，slave为从云。 |
|---|---|---|---|
| muserId | String | admin | 组织修改者。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 0 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | 可选区列表。 |
| supportRegions | String | cn-qingdao-env17-d01 | 可选区列表。 |
| uuid | String | 11231 | 组织UUID。 |
| parentPk | String | 1689406703302188 | 主账号PK。 |
| primaryKey | String | 212530506704030466 | 子账号PK。 |
| roles | Array of role |  | 角色列表。 |
| active | Boolean | true | 角色是否有效。 |
| arId | String | 112311 | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| cuserId | String | admin | 角色创建者。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | roletest _ | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色修改者。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围：organizationVisibility.global为全局共享，organizationVisibility.organization为本组织内共享，organizationVisibility.orgAndSubOrgs为下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11231 | 角色等级。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限：roleRange.allOrganizations为所有组织，roleRange.orgAndSubOrgs为本组织及级联下级组织，roleRange.resourceSet为资源集，roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型：ROLETYPE _RAM为RAM角色，ROLETYPE _ASCM为自定义角色。 |
| status | String | ACTIVE | 用户状态：active为激活，inactive为禁用。 |
| userGroupRoles | Array of userGroupRole |  | 用户组角色列表。 |

| active | Boolean | true | 角色是否有效。 |
|---|---|---|---|
| arId | String | 11231 | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| cuserId | String | admin | 角色创建者。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | test | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色修改者。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围：organizationVisibility.global为全局共享，organizationVisibility.organization为本组织内共享，organizationVisibility.orgAndSubOrgs为下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11231 | 角色等级。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限：roleRange.allOrganizations为所有组织，roleRange.orgAndSubOrgs为本组织及级联下级组织，roleRange.resourceSet为资源集，roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型：ROLETYPE _RAM为RAM角色，ROLETYPE _ASCM为自定义角色。 |
| userGroups | Array of userGroups |  | 用户组列表。 |
| augId | String | 11231 | 用户组唯一编码。 |
| createTimeStamp | Long | 1606675230000 | 用户组创建时间。 |
| groupName | String | grouptest _ | 用户组名称。 |
| id | Integer | 1 | 用户组ID。 |
| organization | Struct |  | 组织信息。 |
| alias | String | test | 组织别名。 |
| ctime | Long | 1606675230000 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者。 |
| id | Integer | 1 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 |
| level | String | 0.1 | 组织等级。 |
| mtime | Long | 1606675230000 | 组织修改时间。 |

| multiCloudStatus | String | master | 是否为多云同步组织：master为主云，slave为从云。 |
|---|---|---|---|
| muserId | String | admin | 组织修改者。 |
| name | String | test | 组织名称。 |
| parentId | Integer | 0 | 父组织ID。 |
| supportRegionList | List | ["cn-qingdao-env17-d01"] | 可选区列表。 |
| supportRegions | String | cn-qingdao-env17-d01 | 可选区列表。 |
| uuid | String | 11231 | 组织UUID。 |
| organizationId | Integer | 1 | 所属组织ID。 |
| resourceSets | Array of resourceSet |  | 资源集列表。 |
| creator | String | admin | 资源集创建者。 |
| gmtCreated | Long | 1606675230000 | 资源集创建时间。 |
| id | Integer | 1 | 资源集ID。 |
| organizationID | Integer | 1 | 所属组织ID。 |
| resourceGroupName | String | restest _ | 资源集名称。 |
| rsId | String | 11231 | 资源集唯一编码。 |
| roles | Array of role |  | 角色列表。 |
| active | Boolean | true | 角色是否有效。 |
| arId | String | 11231 | 角色唯一编码。 |
| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
| cuserId | String | admin | 角色创建者。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | test | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色修改者。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围：organizationVisibility.global为全局共享，organizationVisibility.organization为本组织内共享，organizationVisibility.orgAndSubOrgs为下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11231 | 角色等级。 |
| roleName | String | roletest _ | 角色名称。 |

| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限：roleRange.allOrganizations为所有组织，roleRange.orgAndSubOrgs为本组织及级联下级组织，roleRange.resourceSet为资源集，roleRange.userGroup为RAM角色所在用户组。 |
|---|---|---|---|
| roleType | String | ROLETYPEASCM _ | 角色类型：ROLETYPE _RAM为RAM角色，ROLETYPE _ASCM为自定义角色。 |
| users | Array of user |  | 用户列表。 |
| accountType | Integer | 1 | 账号类型，此字段废弃，代码中不做处理，按默认值处理即可。 |
| active | Boolean | true | 用户是否有效。 |
| aliyunUser | Boolean | false | 是否为主账号。 |
| backendAccountType | String | 1 | 后端映射账号类型：AscmUser为ASCM对客户可见的用户，AliyunUser为阿里云账号，RamUser为RAM子账号。 |
| cellphoneNum | String | 00000000000 | 用户手机号码。 |
| ctime | Long | 1606675230000 | 用户创建时间。 |
| default | Boolean | false | 是否为预置用户。 |
| defaultRoleId | Integer | 1 | 默认角色ID。 |
| deleted | Boolean | false | 用户是否删除。 |
| email | String | test@163.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | false | 是否启用钉钉通知。 |
| enableEmail | Boolean | false | 是否启用邮件通知。 |
| enableShortMessage | Boolean | false | 是否启用短信通知。 |
| id | Integer | 1 | 用户ID。 |
| loginName | String | test | 用户登录名。 |
| loginTime | Long | 1606675230000 | 用户登录时间。 |
| mobileNationCode | String | 86 | 区号。 |
| mtime | Long | 1606675230000 | 用户修改时间。 |
| muserId | String | admin | 用户修改者。 |
| organizationId | Integer | 1 | 所属组织ID。 |
| password | String | H2xWN****** | 用户密码。 |
| ramUser | Boolean | true | 是否为子账号。 |
| userLoginCtrlId | Integer | 34 | 登录控制ID。 |
| username | String | test | 用户显示名。 |
| userRoles | Array of userRole |  | 用户角色列表。 |
| active | Boolean | true | 角色是否有效。 |
| arId | String | 11321 | 角色唯一编码。 |

| code | String | ROLERESOURCEUSER _ _ | 角色Code。 |
|---|---|---|---|
| cuserId | String | admin | 角色创建者。 |
| default | Boolean | true | 是否为预置角色。 |
| description | String | test | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 1 | 角色ID。 |
| muserId | String | admin | 角色修改者。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享 organizationVisibility.organization：本组织内共享 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 11231 | 角色等级。 |
| roleName | String | roletest _ | 角色名称。 |
| roleRange | String | roleRange.orgAndSubOrgs | 角色管理权限：roleRange.allOrganizations为所有组织，roleRange.orgAndSubOrgs为本组织及级联下级组织，roleRange.resourceSet为资源集，roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型：ROLETYPE _RAM为RAM角色，ROLETYPE _ASCM为自定义角色。 |
| message | String | success | 错误提示信息。 |
| pureListData | Boolean | false | 是否只返回数据，不返回其它字段。 |
| redirect | Boolean | false | 是否重定向。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RecoverUserByLoginName &LoginName=testtest &OrganizationId=5
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <code>200</code> <cost>746</cost> <data> <cellphoneNum>13311111111</cellphoneNum> <displayName>fengyueSubOrgAdmin2</displayName> <enableDingTalk>true</enableDingTalk> <roles> <roleRange>roleRange.orgAndSubOrgs</roleRange> <rAMRole>false</rAMRole> <code>ROLE_ORGANIZATION_ADMIN</code> <active>true</active> <description>defaultRole.organizationAdmin.description</description> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.organizationAdmin.name</roleName> / |  |

```xml
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </roles>
    <loginPolicy>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>0.0.0.0/0</ipRange>
            <loginPolicyId>1</loginPolicyId>
        </ipRanges>
        <muserId/>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <timeRanges>
            <loginPolicyId>1</loginPolicyId>
            <startTime>00:00</startTime>
            <endTime>24:00</endTime>
        </timeRanges>
        <enable>true</enable>
        <name>defaultLoginPolicy.name</name>
        <rule>ALLOW</rule>
        <id>1</id>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </loginPolicy>
    <parentPk>1809392454221726</parentPk>
    <lastLoginTime>1592465207953</lastLoginTime>
    <userRoles>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <muserId/>
        <rAMRole>false</rAMRole>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <active>true</active>
        <description>defaultRole.organizationAdmin.description</description>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <id>4</id>
        <roleLevel>2147483647</roleLevel>
        <cuserId/>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </userRoles>
    <accessKeys>
        <ctime>1592454572000</ctime>
        <id>673</id>
        <region>cn-qingdao-env17-d01</region>
        <cuserId>admin</cuserId>
        <accesskeyId>0qZ6FBm******</accesskeyId>
        <status>ACTIVE</status>
    </accessKeys>
    <default>false</default>
    <deleted>false</deleted>
    <loginName>admin</loginName>
    <organization>
        <muserId/>
        <internal>false</internal>
        <multiCloudStatus/>
        <level>0.1.377</level>
        <name>suborg</name>
        <alias>suborg</alias>
        <id>379</id>
        <cuserId/>
        <uuid>null</uuid>
        <parentId>377</parentId>
    </organization>
    <id>5679</id>
    <mobileNationCode>86</mobileNationCode>
    <enableEmail>true</enableEmail>
    <email>1@1.com</email>
    <enableShortMessage>true</enableShortMessage>
    <primaryKey>228648192465372091</primaryKey>
    <status>ACTIVE</status>
</data> <success>true</success> <pureListData>false</pureListData> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "cellphoneNum": "00000000000" |  |

```json
        cellphoneNum: 00000000000,
        "defaultRole": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": "false",
            "muserId": "admin",
            "arId": "111",
            "code": "ROLE_RESOURCE_USER",
            "description": "test",
            "active": "true",
            "roleType": "ROLETYPE_ASCM",
            "default": "true",
            "ownerOrganizationId": "1",
            "enable": "true",
            "roleName": "role_test",
            "roleLevel": "11321",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global"
        },
        "enableDingTalk": "false",
        "displayName": "test",
        "roles": [
            {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "112311",
                "code": "ROLE_RESOURCE_USER",
                "description": "role_test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            }
```

`],`

```json
        "loginPolicy": {
            "ipRanges": [
                {
                    "ipRange": "0.0.0.0/0",
                    "protocol": "IPV4",
                    "loginPolicyId": "1"
                }
```

`],`

```json
            "muserId": "admin",
            "default": "true",
            "ownerOrganizationId": "1",
            "timeRanges": [
                {
                    "startTime": "00:00",
                    "loginPolicyId": "1",
                    "endTime": "24:00"
                }
```

`],`

```json
            "enable": "true",
            "name": "default.loginpolicy",
            "rule": "ALLOW",
            "id": "1",
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "11231",
            "cuserId": "admin"
        },
        "parentPk": "1689406703302188",
        "lastLoginTime": "1606675230000",
        "userGroups": [
            {
                "organizationId": "1",
                "createTimeStamp": "1606675230000",
                "groupName": "group_test",
                "augId": "11231",
                "id": "1"
            },
            {
                "resourceSets": [
                    {
                        "organizationID": "1",
                        "creator": "admin",
                        "resourceGroupName": "res_test",
                        "gmtCreated": "1606675230000",
                        "rsId": "11231",
                        "id": "1"
                    }
```

`],` " " [

```json
                "users": [
                    {
                        "muserId": "admin",
                        "backendAccountType": "1",
                        "enableDingTalk": "false",
                        "mtime": "1606675230000",
                        "organizationId": "1",
                        "password": "H2xWN******",
                        "default": "false",
                        "loginTime": "1606675230000",
                        "userLoginCtrlId": "34",
                        "loginName": "test",
                        "ctime": "1606675230000",
                        "id": "1",
                        "enableShortMessage": "false",
                        "email": "test@163.com",
                        "defaultRoleId": "1",
                        "cellphoneNum": "00000000000",
                        "aliyunUser": "false",
                        "accountType": "1",
                        "active": "true",
                        "deleted": "false",
                        "mobileNationCode": "86",
                        "ramUser": "true",
                        "enableEmail": "false",
                        "username": "test"
                    }
```

`],`

```json
                "roles": [
                    {
                        "roleRange": "roleRange.orgAndSubOrgs",
                        "rAMRole": "false",
                        "muserId": "admin",
                        "arId": "11231",
                        "code": "ROLE_RESOURCE_USER",
                        "description": "test",
                        "active": "true",
                        "roleType": "ROLETYPE_ASCM",
                        "default": "true",
                        "ownerOrganizationId": "1",
                        "enable": "true",
                        "roleName": "role_test",
                        "roleLevel": "11231",
                        "id": "1",
                        "organizationVisibility": "organizationVisibility.global",
                        "cuserId": "admin"
                    }
```

]

```json
            },
            {
                "organization": {
                    "muserId": "admin",
                    "internal": "false",
                    "level": "0.1",
                    "supportRegions": "cn-qingdao-env17-d01",
                    "mtime": "1606675230000",
                    "uuid": "11231",
                    "parentId": "0",
                    "multiCloudStatus": "master",
                    "supportRegionList": "[\"cn-qingdao-env17-d01\"]",
                    "name": "test",
                    "ctime": "1606675230000",
                    "alias": "test",
                    "id": "1",
                    "cuserId": "admin"
                }
            }
```

`],`

```json
        "userRoles": [
            {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11321",
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            }
```

`],`

```json
        "default": "false",
        "accessKeys": [
            {
                "ctime": "1606675230000",
                "id": "1",
                "region": "cn-qingdao-env17-d01",
                "cuserId": "admin",
                "status": "ACTIVE",
                "accesskeyId": "JGdgSN2p******"
            }
```

`],`

```json
        "deleted": "false",
        "loginName": "test",
        "organization": {
            "muserId": "admin",
            "internal": "false",
            "level": "0.1",
            "supportRegions": "cn-qingdao-env17-d01",
            "mtime": "1606791494471",
            "uuid": "11231",
            "parentId": "0",
            "multiCloudStatus": "master",
            "supportRegionList": "[\"cn-qingdao-env17-d01\"]",
            "name": "test",
            "ctime": "1606791494471",
            "alias": "test",
            "id": "1",
            "cuserId": "admin"
        },
        "userGroupRoles": [
            {
                "roleRange": "roleRange.orgAndSubOrgs",
                "rAMRole": "false",
                "muserId": "admin",
                "arId": "11231",
                "code": "ROLE_RESOURCE_USER",
                "description": "test",
                "active": "true",
                "roleType": "ROLETYPE_ASCM",
                "default": "true",
                "ownerOrganizationId": "1",
                "enable": "true",
                "roleName": "role_test",
                "roleLevel": "11231",
                "id": "1",
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            }
```

`],`

```json
        "mobileNationCode": "86",
        "id": "1",
        "enableEmail": "false",
        "enableShortMessage": "false",
        "email": "test@163.com",
        "status": "ACTIVE",
        "primaryKey": "212530506704030466"
    },
    "success": "true",
    "pureListData": "false",
    "message": "success"
}
```

###### 4.1.1.4.24. RelateSystemWithUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/relateSystemWithUser HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 3 | 用户ID。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要关联外部系统的用户。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser | 用户登录名。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要关联外部系统的用户。 |
| relativeSystem | String | Body | 否 | cmp | 关联的外部系统名称。 说明：如果不填写该参数，调用接口将清空指定用户的所有外部系统关联记录。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
POST /ascm/auth/user/relateSystemWithUser HTTP/1.1 {
    "id":3,
    "relativeSystem": "cmp"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.25. RemoveRoleFromUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser | 需要移除角色的用户登录名。 说明：该参数为必填。 |
| roleId | Integer | Body | 否 | 6 | 需要移除的角色ID。 说明：该参数为必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常 |
| cost | Integer | 1022 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| pureListData | Boolean | false | 是否只返回列表数据。 说明：该参数已不再实际使用。 |
| redirect | Boolean | false | 是否重定向。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
{
    "roleId":6,
    "loginName":"testuser"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "redirect":false, "code":"200", "cost":1022, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <code>200</code> <cost>1022</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.26. RemoveUserByLoginName

删除后的用户为历史用户，可通过调用RecoverUserByLoginName接口恢复历史用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/removeUserByLoginName HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser2022 | 用户登录名。由大小写英文字母、数字、下划线（_）、短划线 （-）、半角句号（.）组成，长度为2~64个字符。根据传入的用户登录名来精准查找待删除的用户。 说明该参数为必填。 |
| multiCloudStatus | String | Body | 否 | master | 是否为多云同步用户，默认为null。 master：主云。 slave：从云。 null。 说明该字段已废弃，但是出于兼容性要求，需要保留。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 371 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/removeUserByLoginName HTTP/1.1
```

公共请求头

```json
{
    "loginName":"testuser2022"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>371</cost> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 371, "success": true, "message": "success" } |  |

###### 4.1.1.4.27. RemoveCompletelyUserByLoginName

调用RemoveCompletelyUserByLoginName接口彻底删除用户，彻底删除用户后无法再恢复。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/removeCompletelyUserByLoginName HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser2022 | 历史用户的登录名，由大小写英文字母、数字、 下划线（_）、短划线（-）、半角句号（.）、 at（@）符号组成，长度为2~64个字符。此参数必填，只有历史用户才能被彻底删除。 |
| multiCloudStatus | String | Body | 否 | null | 是否为多云同步用户，默认为null。该字段已废弃，但是出于兼容性要求，需要保留。 master：主云 slave：从云 null。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| message | String | success | 错误提示信息。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```json
POST /ascm/auth/user/removeCompletelyUserByLoginName HTTP/1.1 {
  "loginName":"testuser2022"
}
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":1000,
 "success":true,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.28. ResetPasswordByLoginName

只有组织管理员才可以重置该组织下的用户密码。 调用ResetPasswordByLoginName重置指定用户密码后，该用户的登录密码将被重置为系统自动生成的随机密码。重置后的密码可在Apsara Uni-manager运营控制台 >用户管理>查看用户信息中获取。用户重置密码后首次登录需要修改密码。 企业版v3.17.0及以上版本不推荐使用此接口，建议使用新接口ResetUserPasswordByLoginName。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/resetPasswordByLoginName HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testu | 用户登录名。 说明该参数为必选。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 404：用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 Forbidden：没有权限。 NotExist：用户不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/resetPasswordByLoginName HTTP/1.1
```

公共请求头

```json
{
    "loginName": "testu"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.4.29. ResetUserPasswordByLoginName

重置用户密码。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/resetUserPasswordByLoginName HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | autotest | 用户登录名。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| errorKey | String | ascm.auth.InternalError | 错误码。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |

**示例**

请求示例

```json
POST /ascm/auth/user/resetUserPasswordByLoginName HTTP/1.1 { "loginName":"autotest" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 165, "message": "success", "success": true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>165</cost> <message>success</message> <success>true</success> |  |

###### 4.1.1.4.30. UnLockUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 3 | 用户ID。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要解锁的用户。 |
| loginName | String | Body | 否 | testuser | 用户登录名。 说明：用户登录名（loginName）与用户 ID（id）两个参数填写其中之一即可，指定需要解锁的用户。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
{
    "id":3
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":1000, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>1000</cost> <success>true</success> <message>success</message> |  |

###### 4.1.1.4.31. UpdatePassword

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| oldPassword | String | Body | 否 | 123456 | 当前用户的旧密码。 说明该参数为必填。 |
| newPassword | String | Body | 否 | 999999 | 当前用户的新密码。新密码格式必须符合Apsara Uni-manage 运营控制台中设置的密码安全策略要求。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400： 参数错误。 阿里云账号不支持此操作。 404：用户不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter： 参数错误。 阿里云账号不支持此操作。 Forbidden：没有权限。 NotExist：用户不存在。 InternalServerError：内部错误。 |

| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
|---|---|---|---|
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "oldPassword": "123456" ,
    "newPassword":"999999"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

##### 4.1.1.5. 用户组管理

###### 4.1.1.5.1. AddResourceSetToUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 1 | 用户组ID。可通过调用ListUserGroups接口获取。 说明请求参数userGroupId与userGroupIdList两者必传其一， 若两个参数都传，则以userGroupIdList为准，若两个参数都不传，则返回报错。 |
| resourceSetId | Integer | Body | 否 | 1 | 资源集ID。可通过调用ListResourceGroup接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 400： 缺少参数。 超过了资源集一次性可以添加的用户组数量。 403：没有权限。 404：用户组/角色/资源集不存在。 500：内部错误。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter： 缺少参数。 超过了资源集一次性可以添加的用户组数量。 Forbidden：没有权限。 NotExist：用户组/角色/资源集不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/addResourceSetToUserGroup HTTP/1.1
```

公共请求头

```json
{
    "resourceSetId": 1,
    "userGroupId": 1,
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.5.2. AddRoleToUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 4 | 用户组ID。可通过调用ListUserGroups接口获取。 说明此参数用于绑定单个用户组。请求参数中userGroupId与 userGroupIdList两个参数必传其一，若都传则以 userGroupIdList为准，若都不传则返回报错。 |
| userGroupIdList.N | RepeatList | Body | 否 | 4 | 用户组ID列表。 说明此参数用于绑定多个用户组。参数类型为List<Integer>， 多个用户组ID之间用英文逗号（,）隔开。例如： [4,5,6] 。 |
| roleId | Integer | Body | 否 | 2 | 角色ID。可通过调用ListActiveRoles接口获取。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400： 缺少参数。 超过了角色一次性可以授权的用户组数量。 403：没有权限。 404：用户组/角色不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter： 缺少参数。 超过了角色一次性可以授权的用户组数量。 Forbidden：没有权限。 NotExist：用户组/角色不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "roleId":2
    "userGroupId": 1,
}
```

正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.5.3. AddUsersToUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/addUsersToUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 186 | 目标用户组ID。可通过调用ListUserGroups接口获取。 说明该参数为必填。 |
| loginNameList.N | RepeatList | Body | 否 | ["test"] | 用户名列表，由大小写英文字母、数字、下划线（_）、短划线 （-）、半角句号（.）组成，长度为2~64个字符。多个用户名之间用英文逗号隔开。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 264 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/addUsersToUserGroup HTTP/1.1
```

公共请求头

```json
{
    "loginNameList": "["test"]",
    "userGroupId": "186"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>264</cost> <success>true</success> <message>success</message> |  |

`JSON` 格式

```json
{
    "code": "200",
    "cost": 264,
    "success": true,
    "message": "success"
}
```

###### 4.1.1.5.4. CreateUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| groupName | String | Body | 否 | testUserGroup01 |  | 用户组名称。 说明该参数为必填。 |  |  |  |  |
| description | String | Body | 否 | test |  | 用户组描述。若不传则返回null。 |  |  |  |  |
| organizationId | Integer | Body | 否 | 24 |  | 所属组织ID。可通过调用GetOrganizationList接口获取。 说明该参数为必填。 不支持在root（根）组织下创建用户组，该参数不能传入root（根）组织的ID，root（根）组织的ID 为1。 |  |  |  |  |
| roleIdList.N | RepeatList | Body | 否 | ["5","6"] |  | 角色列表。用户组可关联多个角色，若不传用户组则无关联角色。角色ID可通过调用ListActiveRoles接口获取。 说明该参数需要按照格式传入，格式为 ["<角色1ID>",''<角色2ID>",..."<角色N ID>"] |  |  |  |  |
|  |  |  |  |  |  |  |  | ["<角色1ID>",''<角 |  |  |
|  |  |  |  |  |  |  | 色2ID>",..."<角色N ID>"] |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| cost | Integer | 121 | 接口响应耗时，单位毫秒（ms）。 |

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| data | Struct |  | 响应数据。 |
| augId | String | aug-101e08e2202d0a4209****** | 用户组唯一编码。 |
| groupName | String | testUserGroup01 | 用户组名称。 |
| id | String | 186 | 用户组ID。 |
| organizationId | Integer | 24 | 用户组所属组织ID。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "groupName": "testUserGroup01",
    "organizationId": 24
}
```

正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>121</cost> <code>200</code> <data>
    <organizationId>24</organizationId>
    <groupName>testUserGroup01</groupName>
    <augId>aug-101e08e2202d0a4209******</augId>
    <id>186</id>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 121, "code": 200, "data": { "organizationId": 24, "groupName": "testUserGroup01", "augId": "aug-101e08e2202d0a4209******", "id": 186 }, "success": true, "message": "success" } |  |

###### 4.1.1.5.5. DeleteUserGroup

**说明**

删除用户组前，系统将自动解绑角色、用户、资源集等关联资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 190 | 用户组ID。可通过调用ListUserGroups接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 104 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "userGroupId": "190"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>104</cost> <success>true</success> <message>success</message> |  |

`JSON` 格式

```json
{
    "code": "200",
    "cost": 104,
    "success": true,
    "message": "success"
}
```

###### 4.1.1.5.6. ListUserGroups

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testuser2022 | 用户登录名，由大小写英文字母、数字、下划线（_）、短划线 （-）、半角句号（.）组成，长度为2~64个字符。 说明传入此参数会以用户登录名进行模糊查询。若请求参数都不传，则返回所有用户组信息。 |
| userGroupName | String | Body | 否 | testUserGroup01 | 用户组名称，由英文字母大小写、数字、中文、下划线（_）、短划线（-）、半角句号（.）、和at（@）组成，长度为3~255个字符说明传入此参数会以用户组名称进行模糊查询。 |
| roleId | Integer | Body | 否 | 2 | 角色ID。可通过调用ListRoles接口获取。 说明传入此参数则返回绑定该角色的所有用户组。 |
| resourceSetId | Integer | Body | 否 | 447 | 资源集ID。可通过调用ListResourceGroup接口获取。 说明传入此参数则返回绑定该资源集的所有用户组。 |
| organizationId | Integer | Body | 否 | 25 | 组织ID。可通过调用GetOrganizationList接口获取。 说明传入此参数则返回该组织下的所有用户组。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 分页大小，默认为10。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of itemData |  | 响应结果。 |
| augId | String | aug-101e09e801fe0a420****** | 用户组唯一编码。 |
| createTimeStamp | Long | 1606791494471 | 用户组创建时间。 |
| groupName | String | testUserGroup01 | 用户组名称。 |
| id | Integer | 190 | 用户组ID。 |
| organization | Struct |  | 用户组所属组织的信息。 |
| alias | String | ascm-tester | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1657608934419 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 说明此参数已经废弃。 |
| id | Integer | 24 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 说明预置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1 | 组织等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1662542569753 | 组织最近一次修改的时间。 |

| multiCloudStatus | String | master | 是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |  |  |  |
|---|---|---|---|---|---|---|
| muserId | String | admin | 组织最近一次修改的修改者用户名。 |  |  |  |
| name | String | ascm-tester | 组织名称。 |  |  |  |
| parentId | Integer | 1 | 父组织ID。 |  |  |  |
| supportRegionList | List | [ "cn-qingdao-****-d01" ] | 可用区列表。 |  |  |  |
| supportRegions | String | cn-qingdao-****-d01 | 可用区列表。 |  |  |  |
| uuid | String | org-101cc06515930a4209****** | 组织UUID。 |  |  |  |
| organizationId | Integer | 24 | 所属组织ID。 |  |  |  |
| resourceSets | Array of resourceSet |  | 资源集列表。 |  |  |  |
| creator | String | admin | 资源集创建者。 |  |  |  |
| gmtCreated | Long | 1662531985752 | 资源集创建时间。 |  |  |  |
| id | Integer | 447 | 资源集ID。 |  |  |  |
| organizationID | Integer | 24 | 资源集所属组织的ID。 |  |  |  |
| resourceGroupName | String | ascmtestresourceset _ _ | 资源集名称。 |  |  |  |
| rsId | String | rs-101de5d4e2d80a4209******* | 资源集唯一编码。 |  |  |  |
| roles | Array of role |  | 角色列表。 |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |  |  |  |
| arId | String | ar-9999****** | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCESETADMIN _ _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者的用户名。 |  |  |  |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.resourceSetAdmin.de scription | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否有效。 |  |  |  |
| id | Integer | 5 | 角色ID。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| muserId | String | admin | 角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |
|---|---|---|---|
| organizationVisibility | String | organizationVisibility.global | 角色共享范围。 organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.resourceSetAdmin.na me | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限。 roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| users | Array of user |  | 用户列表。 |
| accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| active | Boolean | true | 用户是否有效。 |
| aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| backendAccountType | String | RamUser | 后端映射账号类型。 AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：（阿里云）主账号。 RamUser：RAM用户（子账号）。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| ctime | Long | 1663137217142 | 用户创建时间。 |
| default | Boolean | false | 是否为预置用户。 说明预置用户在部署的时候由初始化服务生成，创建的用户部署预置用户。 |
| defaultRoleId | Integer | 4 | 用户默认角色ID。 |
| deleted | Boolean | false | 用户是否已删除。 |

| email | String | 1776236****17762364***@aliba ba-inc.com | 用户邮箱地址。 |
|---|---|---|---|
| enableDingTalk | Boolean | true | 是否启用钉钉通知。 |
| enableEmail | Boolean | true | 是否启用邮件通知。 |
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 6002 | 用户ID。 |
| loginName | String | testuser2022 | 用户登录名。 |
| loginTime | Long | 1606791494471 | 用户最近一次登录的时间。 |
| mobileNationCode | String | 86 | 用户手机号码的国际区号。 |
| mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |
| muserId | String | admin | 用户最近一次修改的修改者用户名。 |
| organizationId | Integer | 25 | 用户所属组织的ID。 |
| password | String | H2xWNY8oitAhxMW****** | 用户密码。 |
| ramUser | Boolean | true | 是否为RAM用户（子账号）。 |
| userLoginCtrlId | Integer | 647 | 登录控制ID。 |
| username | String | testuser2022 | 用户显示名。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 10 | 每页返回数据的条数。 |
| total | Integer | 1 | 返回记录总数。 |
| totalPage | Integer | 1 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "loginName":"testuser2022",
    "userGroupName":"testUserGroup01",
    "roleId":2
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <data> <organizationId>24</organizationId> <groupName>testUserGroup01</groupName> <augId>aug-101e09e801fe0a420******</augId> <createTimeStamp>1606791494471</createTimeStamp> <id>190</id> <resourceSets> <organizationID>24</organizationID> <creator>admin</creator> <resourceGroupName>ascm_test_resourceset</resourceGroupName> <gmtCreated>1662531985752</gmtCreated> <rsId>rs-101de5d4e2d80a4209*******</rsId> <id>447</id> </resourceSets> <users> <cellph1776236*******8888</cellphoneNum> <muserId>admin</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>RamUser</backendAccountType> <enableDingTalk>true</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1606791494471</mtime> <organizationId>25</organizationId> <password>H2xWNY8oitAhxMW******</password> <default>false</default> <loginTime>1606791494471</loginTime> <deleted>false</deleted> <userLoginCtrlId>647</userLoginCtrlId> <loginName>testuser2022</loginName> <ctime>1663137217142</ctime> <mobileNationCode>86</mobileNationCode> <id>6002</id> <ramUser>true</ramUser> <enableEmail>true</enableEmail> <enableShortMessage>true</enableShortMessage> <email>17762364361@alibaba-inc.com</email> <defaultRoleId>4</defaultRoleId> <username>testuser2022</username> </users> <roles> <roleRange>roleRange.resourceSet</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>ar-9999******</arId> <code>ROLE_RESOURCE_SET_ADMIN</code> <description>defaultRole.resourceSetAdmin.description</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceSetAdmin.name</roleName> <roleLevel>2147483647</roleLevel> <id>5</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </roles> <organization> <muserId>admin</muserId> <internal>false</internal> <multiCloudStatus>master</multiCloudStatus> <level>0.1</level> <name>ascm-tester</name> <supportRegions>cn-qingdao-****-d01</supportRegions> <ctime>1657608934419</ctime> <alias>ascm-tester</alias> <id>24</id> <mtime>1662542569753</mtime> |  |

```xml
        <mtime>1662542569753</mtime>
        <uuid>org-101cc06515930a4209******</uuid>
        <cuserId>admin</cuserId>
        <parentId>1</parentId>
        <supportRegionList>[ "cn-qingdao-****-d01" ]</supportRegionList>
    </organization>
</data> <success>true</success> <pageInfo>
    <total>1</total>
    <totalPage>1</totalPage>
    <pageSize>10</pageSize>
    <currentPage>1</currentPage>
</pageInfo> <pureListData>false</pureListData> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "data": { "organizationId": 24, "groupName": "testUserGroup01", "augId": "aug-101e09e801fe0a420******", "createTimeStamp": 1606791494471, "id": 190, "resourceSets": { "organizationID": 24, "creator": "admin", "resourceGroupName": "ascm_test_resourceset", "gmtCreated": 1662531985752, "rsId": "rs-101de5d4e2d80a4209*******", "id": 447 }, "users": { "cellphoneNum": "188****8888", "muserId": "admin", "aliyunUser": false, "backendAccountType": "RamUser", "enableDingTalk": true, "accountType": 1, "active": true, "mtime": 1606791494471, "organizationId": 25, "password": "H2xWNY8oitAhxMW******", "default": false, "loginTime": 1606791494471, "deleted": false, "userLoginCtrlId": 647, "loginName": "testuser2022", "ctime": 1663137217142, "mobileNationCode": 86, "id": 6002, "ramUser": true, "enableEmail": true, "enableShortMessage": true, "email": "17762364361@alibaba-inc.com", "defaultRoleId": 4, "username": "testuser2022" }, "roles": { "roleRange": "roleRange.resourceSet", "rAMRole": false, "muserId": "admin", "arId": "ar-9999******", "code": "ROLE_RESOURCE_SET_ADMIN", "description": "defaultRole.resourceSetAdmin.description", "active": true, "roleType": "ROLETYPE_ASCM", "default": true, "ownerOrganizationId": 1, "enable": true, "roleName": "defaultRole.resourceSetAdmin.name", "roleLevel": 2147483647, "id": 5, "organizationVisibility": "organizationVisibility.global", "cuserId": "admin" }, "organization": { "muserId": "admin", "internal": false, "multiCloudStatus": "master", "level": 0.1, "name": "ascm-tester", |  |

,

```json
            "supportRegions": "cn-qingdao-****-d01",
            "ctime": 1657608934419,
            "alias": "ascm-tester",
            "id": 24,
            "mtime": 1662542569753,
            "uuid": "org-101cc06515930a4209******",
            "cuserId": "admin",
            "parentId": 1,
            "supportRegionList": "[ \"cn-qingdao-****-d01\" ]"
        }
    },
    "success": true,
    "pageInfo": {
        "total": 1,
        "totalPage": 1,
        "pageSize": 10,
        "currentPage": 1
    },
    "pureListData": false,
    "message": "success"
}
```

###### 4.1.1.5.7. UpdateUserGroup

更新指定用户组的名称和描述信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
PUT /userGroups/[userGroupId] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| userGroupId | Integer | Path | 是 | 123 | 用户组Id。 |
| newGroupName | String | Body | 否 | NewTestGroup | 这是一个表示工作环境中团队的新名称，例如"营销部"或"项目X小组"。 |
| newDescription | String | Body | 是 | 此角色用于测试 | 描述信息，限制在100个字符以内，非必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | ROLERESOURCEUSER _ _ | 用户角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的. 自定义角色的code由系统生成。格式为： ROLE _英文大写的角色名称_随机串。 |
| errorKey | String | exampleErrKey | 错误码。 |
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | - | 响应结果：流程回调是否成功。 |
| -id | Integer | 33 | 角色ID。 |
| -groupName | String | testUserGroup01 | 用户组名称。 |
| -organizationId | Integer | 3 | 所属组织ID。 |
| -augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |

**示例**

请求示例

```json
PUT /userGroups/[userGroupId] HTTP/1.1 { "userGroupId":"123" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"exampleErrKey", "code":"ROLE_RESOURCE_USER", "cost":121, "data":{ "organizationId":3, "groupName":"testUserGroup01", "augId":"aug-101de696afc90a420d******", "id":33 }, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <errorKey>exampleErrKey</errorKey> <code>ROLE_RESOURCE_USER</code> <cost>121</cost> <data> <organizationId>3</organizationId> <groupName>testUserGroup01</groupName> <augId>aug-101de696afc90a420d******</augId> <id>33</id> </data> <success>true</success> <message>success</message> |  |

###### 4.1.1.5.8. ListUsersInUserGroup

通过ListUsersInUserGroup接口获取指定用户组中的各个用户的信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/listUsersInUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 145 | 用户组ID。可通过调用ListUserGroups接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 24 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of itemData |  | 响应结果。 |
| accessKeys | Array of accessKey |  | AccessKey信息列表。 说明只有超级管理员才可获取预置用户的AccessKey和AccessKey Secret。 |
| accesskeyId | String | tCr5mJh****** | 用户的AccessKey ID。 |
| ctime | Long | 1606675230000 | AccessKey创建时间。 说明此参数已经废弃。 |
| cuserId | String | admin | 创建AccessKey的用户名。 说明此参数已经废弃。 |
| id | Integer | 1 | AccessKey的识别主键。 说明此参数已经废弃。 |
| region | String | cn-qingdao-****-d01 | AccessKey的可用区。 |
| status | String | ACTIVE | AccessKey是否有效。 ACTIVE：有效。 INACTIVE：无效。 |
| cellphoneNum | String | 188****8888 | 用户手机号码。 |
| default | Boolean | false | 是否为预置用户。 说明初始化自动创建的用户是预置用户，创建场景下此字段默认为false。 |

| defaultRole | Struct |  | 默认角色。 说明用户登录后的当前角色。 |  |  |  |
|---|---|---|---|---|---|---|
| active | Boolean | true | 默认角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-99999****** | 默认角色的唯一编码。 |  |  |  |
| code | String | ROLEORGANIZATIONADMIN _ _ | 默认角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| default | Boolean | true | 默认角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.organizationAdmin.de scription | 默认角色描述。 |  |  |  |
| enable | Boolean | true | 默认角色是否有效。 |  |  |  |
| id | Integer | 4 | 默认角色ID。 |  |  |  |
| muserId | String | admin | 默认角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 默认角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 默认角色所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 默认角色是否为RAM角色。 |  |  |  |
| roleLevel | Integer | 2147483647 | 默认角色的等级。 说明该参数无实际作用。 |  |  |  |
| roleName | String | defaultRole.organizationAdmin.na me | 默认角色的名称。 |  |  |  |
| roleRange | String | roleRange.orgAndSubOrgs | 默认角色的管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |  |  |  |
| roleType | String | ROLETYPEASCM _ | 默认角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| deleted | Boolean | true | 用户是否已被删除，已删除的用户为历史用户。 true：已经被删除。 false：未被删除。 |
|---|---|---|---|
| displayName | String | testuser2022 | 用户显示名。 |
| email | String | tets@example.com | 用户邮箱地址。 |
| enableDingTalk | Boolean | true | 是否启用钉钉通知。 |
| enableEmail | Boolean | true | 是否启用邮件通知。 |
| enableShortMessage | Boolean | true | 是否启用短信通知。 |
| id | Integer | 5817 | 用户ID。 |
| lastLoginTime | Long | 1657608949009 | 用户最后登录时间。 说明此参数已经废弃。 |
| loginName | String | testuser2022 | 用户登录名。 |
| loginPolicy | Struct |  | 用户绑定的登录策略。 |
| cuserId | String | admin | 登录策略创建者。 说明此参数已经废弃 |
| default | Boolean | false | 是否为默认登录策略。 |
| enable | Boolean | true | 登录策略是否有效。 |
| id | Integer | 1084 | 登录策略ID。 |
| ipRanges | Array of itemIpRange |  | 登录策略的IP段。 |
| ipRange | String | 10.48.16.1/24 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| protocol | String | IPV4 | 使用IP协议，目前仅支持IPv4。 |
| lpId | String | lp-101de13d33320a420d27000p | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略创建者。 |
| name | String | mytest | 登录策略名。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rule | String | DENY | 策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of itemTimeRange |  | 登录策略的时间段。 |

| endTime | String | 18:00 | 结束时间。 |
|---|---|---|---|
| loginPolicyId | Integer | 1084 | 所属登录策略ID。 |
| startTime | String | 08:00 | 开始时间。 |
| mobileNationCode | String | 86 | 用户手机号码的国际区号。 |
| organization | Struct |  | 用户所属的组织。 |
| alias | String | sub-org-1 | 组织别名。系统自动生成，一般与组织名称一致。 |
| ctime | Long | 1657608949009 | 用户所属组织创建的时间。 说明此参数已经废弃。 |
| cuserId | String | admin | 用户所属组织创建者的用户名。 说明此参数已经废弃。 |
| id | Integer | 25 | 用户所属组织ID。 |
| internal | Boolean | false | 用户所属组织是否为预置组织。 说明置组织即系统自动生成的组织，也称为默认组织。 |
| level | String | 0.1.24 | 用户所属组织的等级。 说明 root组织（根组织）的level=0，其他所有一级组织的level=0.1。其中0.1 中的1表示本组织的父组织（root组织）的ID为1。以此类推，例如：某ID为 3的一级组织的直接下级组织level=0.1.3。 |
| mtime | Long | 1657608949009 | 组织最近一次修改的时间。 |
| multiCloudStatus | String | 86 | 用户所属组织是否为多云同步组织。 master：主云。 slave：从云。 说明该参数仅在多云场景下返回。 |
| muserId | String | admin | 用户所属组织最近一次修改的修改者用户名。 说明此参数已经废弃。 |
| name | String | sub-org-1 | 用户所属组织的名称。 |
| parentId | Integer | 24 | 用户所属组织的父组织ID。 |
| supportRegionList | List | ["cn-***-d01"] | 可用区列表。 |
| supportRegions | String | ["cn-***-d01"] | 可用区列表。 说明此参数已经废弃。 |
| uuid | String | org- 101cc0654e910a420927000w | 用户所属组织UUID。 |

| parentPk | String | 1127157608934563 | 阿里云账号（主账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的阿里云账号（主账号）UID一致。 |  |  |  |
|---|---|---|---|---|---|---|
| primaryKey | String | 259258662544685329 | RAM用户（子账号）的主键，作为账号的唯一标识。 说明与在ApsaraUni-manager运营控制台的用户管理中的RAM用户（子账号） 一致。 |  |  |  |
| roles | Array of itemRole |  | 用户拥有的角色列表。 |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-9999****** | 角色唯一编码。 |  |  |  |
| code | String | ROLEGLOBALRESOURCEAUDIT _ _ _ OR | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者的用户名。 说明参数已经废弃。 |  |  |  |
| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |  |  |  |
| description | String | defaultRole.globalResourceAudito r.description | 角色描述。 |  |  |  |
| enable | Boolean | true | 角色是否有效。 |  |  |  |
| id | Integer | 6 | 角色ID。 |  |  |  |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |  |  |  |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |
| ownerOrganizationId | Integer | 1 | 角色所属组织ID。 |  |  |  |
| rAMRole | Boolean | false | 是否为RAM角色。 |  |  |  |

| AUDIT _ |  | 名称_随机串 |
|---|---|---|

| roleLevel | Integer | 2147483647 | 角色等级。 说明该参数无实际作用。 |
|---|---|---|---|
| roleName | String | defaultRole.globalResourceAudito r.name | 角色名称。 |
| roleRange | String | roleRange.allOrganizations | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| status | String | ACTIVE | 用户状态。 说明用户创建后否默认为active。 active:激活。 inactive:禁用。 |
| userGroupRoles | Array of itemUserGroupRole |  | 用户所属用户组所拥有的角色列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |
| active | Boolean | true | 用户所属用户组所拥有的角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |
| arId | String | ar-9999****** | 用户所属用户组所拥有的角色唯一编码。 |
| code | String | ROLERESOURCESETADMIN _ _ _ | 用户所属用户组所拥有的角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| cuserId | String | admin | 创建用户所属用户组所拥有的角色的用户ID。 说明此参数已经废弃。 |
| default | Boolean | true | 用户所属用户组所拥有的角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
| description | String | defaultRole.resourceSetAdmin.de scription | 用户所属用户组所拥有的角色的描述。 |
| enable | Boolean | true | 用户所属用户组所拥有的角色是否有效。 |
| id | Integer | 5 | 用户所属用户组所拥有角色的ID。 |

| muserId | String | admin | 用户所属用户组所拥有角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |
|---|---|---|---|
| organizationVisibility | String | organizationVisibility.global | 用户所属用户组所拥有角色的共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 用户所属用户组所拥有角色的所属组织ID。 |
| rAMRole | Boolean | false | 用户所属用户组所拥有的角色是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 用户所属用户组所拥有角色的等级。 说明该参数无实际作用。 |
| roleName | String | defaultRole.resourceSetAdmin.na me | 用户所属用户组所拥有角色的名称。 |
| roleRange | String | roleRange.resourceSet | 用户所属用户组所拥有角色的管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 用户所属用户组所拥有角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| userGroups | Array of itemUserGroup |  | 用户所属用户组列表。 说明可通过AddUsersToUserGroup接口将用户添加到用户组。 |
| augId | String | aug- 101de696afc90a420d270003 | 用户组唯一编码。 |
| createTimeStamp | Long | 1657608949009 | 用户组创建时间。 |
| groupName | String | testUserGroup01 | 用户组名称。 |
| id | Integer | 145 | 用户组ID。 |
| organization | Struct |  | 创建的用户所属的组织信息。 说明此参数已经废弃，若要查询用户组所属组织详细信息，请根据 organizationId参数通过GetOrganization接口查询。 |
| alias | String | sub-org-1 | 组织别名。 |
| ctime | Long | 1657608949009 | 组织创建时间。 |
| cuserId | String | admin | 组织创建者的用户名。 |
| id | Integer | 25 | 组织ID。 |
| internal | Boolean | false | 是否为预置组织。 |

| level | String | 0.1.24 | 组织等级。 |  |  |  |
|---|---|---|---|---|---|---|
| mtime | Long | 1657608949009 | 组织最后修改时间。 |  |  |  |
| multiCloudStatus | String | master | 多云状态参数。 |  |  |  |
| muserId | String | admin | 组织最后一次修改者的用户名。 |  |  |  |
| name | String | sub-org-1 | 组织名称。 |  |  |  |
| parentId | Integer | 24 | 父组织ID。 |  |  |  |
| supportRegionList | List | [ "cn-qingdao-****-d01"] | 可用区列表。 |  |  |  |
| supportRegions | String | [ "cn-qingdao-****-d01"] | 可用区列表。 |  |  |  |
| uuid | String | org- 101cc0654e910a420927000w | 组织的UUID。 |  |  |  |
| organizationId | Integer | 24 | 用户组所属组织的ID。 |  |  |  |
| resourceSets | Array of itemResourceSet |  | 资源集列表。 说明此参数已经废弃。 |  |  |  |
| creator | String | admin | 资源集创建者的用户名。 |  |  |  |
| gmtCreated | Long | 1657608949009 | 资源集创建时间。 |  |  |  |
| id | Integer | 6 | 资源集ID。 |  |  |  |
| organizationID | Integer | 3 | 资源集所属组织的ID。 |  |  |  |
| resourceGroupName | String | test | 资源集名称。 |  |  |  |
| rsId | String | rs-9999****** | 资源集唯一编码。 |  |  |  |
| roles | Array of itemRole |  | 资源集列表。 说明此参数已经废弃。 |  |  |  |
| active | Boolean | true | 角色是否有效。 说明此参数已废弃，角色状态以enable参数为准。 |  |  |  |
| arId | String | lp-101de13d33320a420d27000p | 角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 角色创建者。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| default | Boolean | true | 是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
|---|---|---|---|
| description | String | defaultRole.resourceUser.descript ion | 角色描述。 |
| enable | Boolean | true | 角色是否有效。 |
| id | Integer | 2 | 角色ID。 |
| muserId | String | admin | 角色最近一次修改的修改者用户名。 |
| organizationVisibility | String | organizationVisibility.global | 角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 角色等级。 说明保留字段，无实际意义。 |
| roleName | String | defaultRole.resourceUser.name | 角色名称。 |
| roleRange | String | roleRange.resourceSet | 角色管理权限： roleRange.allOrganizations：所有组织。 roleRange.orgAndSubOrgs：本组织及级联下级组织。 roleRange.resourceSet：资源集。 roleRange.userGroup：RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 角色类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| users | Array of itemUser |  | 用户列表。 说明此参数已经废弃，可通过ListUsersInUserGroup接口查询用户组内用户列表 |
| accountType | Integer | 1 | 账号类型。 说明该参数已废弃。 |
| active | Boolean | true | 用户是否有效。 |
| aliyunUser | Boolean | false | 是否为阿里云账号（主账号）。 |
| backendAccountType | String | 用户是否有效。 | 后端映射账号类型： AscmUser：Apsara Uni-manager运营控制台对客户可见的用户。 AliyunUser：阿里云账号。 RamUser：RAM子账号。 |
| cellphoneNum | String | 1606791494471 | 用户手机号码。 |

| ctime | Long | 1606791494471 | 用户创建时间。 |  |  |  |
|---|---|---|---|---|---|---|
| default | Boolean | false | 是否为预置用户。 |  |  |  |
| defaultRoleId | Integer | 3 | 用户默认角色ID。 |  |  |  |
| deleted | Boolean | false | 用户是否已删除。 |  |  |  |
| email | String | tets@example.com | 用户邮箱地址。 |  |  |  |
| enableDingTalk | Boolean | false | 是否启用钉钉通知。 |  |  |  |
| enableEmail | Boolean | false | 是否启用邮件通知。 |  |  |  |
| enableShortMessage | Boolean | false | 是否启用短信通知。 |  |  |  |
| id | Integer | 5673 | 用户ID。 |  |  |  |
| loginName | String | test | 用户登录名。 |  |  |  |
| loginTime | Long | 1606791494471 | 用户登录时间。 |  |  |  |
| mobileNationCode | String | 86 | 区号。 |  |  |  |
| mtime | Long | 1606791494471 | 用户最近一次修改的时间。 |  |  |  |
| muserId | String | 5002 | 用户最近一次修改的修改者用户名。 |  |  |  |
| organizationId | Integer | 24 | 用户所属组织的ID。 |  |  |  |
| password | String | 123456789 | 用户密码。 |  |  |  |
| ramUser | Boolean | true | 是否为RAM用户（子账号）。 |  |  |  |
| userLoginCtrlId | Integer | 1 | 登录策略ID。 |  |  |  |
| username | String | test | 用户显示名。 |  |  |  |
| userRoles | Array of itemUserRole |  | 用户角色列表，用户关联的角色列表，由请求参数roleIdList指定。 |  |  |  |
| active | Boolean | true | 用户关联的角色是否有效。 说明此字段已废弃，角色禁用状态以enable字段为准。 |  |  |  |
| arId | String | ar-9999****** | 用户关联角色唯一编码。 |  |  |  |
| code | String | ROLERESOURCEUSER _ _ | 用户关联角色code。权限校验时code用来确定角色类型，判断角色是否有对应的权限。 说明内置角色code是固定的。 自定义角色的code由系统生成。格式为： ROLE_英文大写的角色名称_随机串 。 |  |  |  |
|  |  |  |  | ROLE_英文大写的角色 |  |  |
| cuserId | String | admin | 用户关联角色创建者的用户名。 说明此参数已经废弃。 |  |  |  |

|  |  | 名称_随机串 |
|---|---|---|

| default | Boolean | true | 用户关联角色是否为预置角色。预置角色由系统自动成，包括资源使用人、组织管理员、资源集管理员、资源监察员、组织安全管理员、安全审计员、安全系统配置管理员、全局组织安全管理员、平台安全管理员、全局组织安全监察员、平台安全监察员、平台安全配置管理员和组织资源监察员。 |
|---|---|---|---|
| description | String | defaultRole.resourceUser.descript ion | 用户关联角色的描述。 |
| enable | Boolean | true | 用户关联角色是否有效。 |
| id | Integer | 2 | 用户关联的角色ID。 |
| muserId | String | admin | 用户关联角色最近一次修改的修改者用户名。 说明此参数已经废弃。 |
| organizationVisibility | String | organizationVisibility.global | 用户关联角色共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 用户关联角色所属组织ID。 |
| rAMRole | Boolean | false | 是否为RAM角色。 |
| roleLevel | Integer | 2147483647 | 用户关联角色等级。 说明保留字段，无实际作用。 |
| roleName | String | defaultRole.resourceUser.name | 用户关联角色的名称。 |
| roleRange | String | roleRange.resourceSet | 用户关联角色的管理权限： roleRange.allOrganizations为所有组织。 roleRange.orgAndSubOrgs为本组织及级联下级组织。 roleRange.resourceSet为资源集。 roleRange.userGroup为RAM角色所在用户组。 |
| roleType | String | ROLETYPEASCM _ | 用户关联角色的类型。 ROLETYPE _RAM：RAM授权。 ROLETYPE _ASCM：Apsara Uni-manage运营控制台系统的角色，包含预置角色和自定义角色。 ROLETYPE _RAMROLEAUTHORIZATION：RAM角色授权，用于创建RAM Role模板，绑定一级组织主账号时实例化为RAM Role。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |

| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |
|---|---|---|---|

**示例**

请求示例

```
POST /ascm/auth/user/listUsersInUserGroup HTTP/1.1
```

公共请求头

```json
{
    "userGroupId": 145
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>24</cost> <code>200</code> <data> <cellphoneNum>188****8888</cellphoneNum> <enableDingTalk>true</enableDingTalk> <displayName>testuser2022</displayName> <parentPk>1127157608934563</parentPk> <lastLoginTime>1657608949009</lastLoginTime> <default>false</default> <deleted>true</deleted> <loginName>testuser2022</loginName> <mobileNationCode>86</mobileNationCode> <id>5817</id> <enableEmail>true</enableEmail> <enableShortMessage>true</enableShortMessage> <email>tets@example.com</email> <status>ACTIVE</status> <primaryKey>259258662544685340</primaryKey> <userGroupRoles> <roleRange>roleRange.resourceSet</roleRange> <rAMRole>false</rAMRole> <muserId>admin</muserId> <arId>ar-9999******</arId> <code>ROLE_RESOURCE_SET_ADMIN</code> <description>defaultRole.resourceSetAdmin.description</description> <active>true</active> <roleType>ROLETYPE_ASCM</roleType> <default>true</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <roleName>defaultRole.resourceSetAdmin.name</roleName> <roleLevel>2147483647</roleLevel> <id>5</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <cuserId>admin</cuserId> </userGroupRoles> <userGroups> <organizationId>24</organizationId> <groupName>testUserGroup01</groupName> <augId>aug-101de696afc90a420d270003</augId> <createTimeStamp>1657608949009</createTimeStamp> <id>145</id> <resourceSets> <organizationID>3</organizationID> <creator>admin</creator> <resourceGroupName>test</resourceGroupName> <gmtCreated>1657608949009</gmtCreated> <rsId>rs-9999******</rsId> <id>6</id> </resourceSets> <users> <cellphoneNum>1606791494471</cellphoneNum> <muserId>5002</muserId> <aliyunUser>false</aliyunUser> <backendAccountType>用户是否有效。</backendAccountType> <enableDingTalk>false</enableDingTalk> <accountType>1</accountType> <active>true</active> <mtime>1606791494471</mtime> <organizationId>24</organizationId> <password>123456789</password> <default>false</default> <loginTime>1606791494471</loginTime> <deleted>false</deleted> <userLoginCtrlId>1</userLoginCtrlId> <loginName>test</loginName> < ti >1606791494471</ ti > |  |

```xml
            <ctime>1606791494471</ctime>
            <mobileNationCode>86</mobileNationCode>
            <id>5673</id>
            <ramUser>true</ramUser>
            <enableEmail>false</enableEmail>
            <enableShortMessage>false</enableShortMessage>
            <email>tets@example.com</email>
            <defaultRoleId>3</defaultRoleId>
            <username>test</username>
        </users>
        <roles>
            <roleRange>roleRange.resourceSet</roleRange>
            <rAMRole>false</rAMRole>
            <muserId>admin</muserId>
            <arId>lp-101de13d33320a420d27000p</arId>
            <code>ROLE_RESOURCE_USER</code>
            <description>defaultRole.resourceUser.description</description>
            <active>true</active>
            <roleType>ROLETYPE_ASCM</roleType>
            <default>true</default>
            <ownerOrganizationId>1</ownerOrganizationId>
            <enable>true</enable>
            <roleName>defaultRole.resourceUser.name</roleName>
            <roleLevel>2147483647</roleLevel>
            <id>2</id>
            <organizationVisibility>organizationVisibility.global</organizationVisibility>
            <cuserId>admin</cuserId>
        </roles>
        <organization>
            <muserId>admin</muserId>
            <internal>false</internal>
            <multiCloudStatus>master</multiCloudStatus>
            <level>0.1.24</level>
            <name>sub-org-1</name>
            <supportRegions>[ "cn-qingdao-****-d01"]</supportRegions>
            <ctime>1657608949009</ctime>
            <alias>sub-org-1</alias>
            <id>25</id>
            <mtime>1657608949009</mtime>
            <uuid>org-101cc0654e910a420927000w</uuid>
            <cuserId>admin</cuserId>
            <parentId>24</parentId>
            <supportRegionList>[ "cn-qingdao-****-d01"]</supportRegionList>
        </organization>
    </userGroups>
    <userRoles>
        <roleRange>roleRange.resourceSet</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_RESOURCE_USER</code>
        <description>defaultRole.resourceUser.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.resourceUser.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>2</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <cuserId>admin</cuserId>
    </userRoles>
    <accessKeys>
        <ctime>1606675230000</ctime>
        <id>1</id>
        <region>cn-qingdao-****-d01</region>
        <cuserId>admin</cuserId>
        <status>ACTIVE</status>
        <accesskeyId>tCr5mJh******</accesskeyId>
    </accessKeys>
    <roles>
        <roleRange>roleRange.allOrganizations</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-9999******</arId>
        <code>ROLE_GLOBAL_RESOURCE_AUDITOR</code>
        <description>defaultRole.globalResourceAuditor.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.globalResourceAuditor.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>6</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
```

```xml
        <cuserId>admin</cuserId>
    </roles>
    <defaultRole>
        <roleRange>roleRange.orgAndSubOrgs</roleRange>
        <rAMRole>false</rAMRole>
        <muserId>admin</muserId>
        <arId>ar-99999******</arId>
        <code>ROLE_ORGANIZATION_ADMIN</code>
        <description>defaultRole.organizationAdmin.description</description>
        <active>true</active>
        <roleType>ROLETYPE_ASCM</roleType>
        <default>true</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <roleName>defaultRole.organizationAdmin.name</roleName>
        <roleLevel>2147483647</roleLevel>
        <id>4</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
    </defaultRole>
    <loginPolicy>
        <muserId>admin</muserId>
        <default>false</default>
        <ownerOrganizationId>1</ownerOrganizationId>
        <enable>true</enable>
        <name>mytest</name>
        <rule>DENY</rule>
        <id>1084</id>
        <organizationVisibility>organizationVisibility.global</organizationVisibility>
        <lpId>lp-101de13d33320a420d27000p</lpId>
        <cuserId>admin</cuserId>
        <ipRanges>
            <protocol>IPV4</protocol>
            <ipRange>10.48.16.1/24</ipRange>
            <loginPolicyId>1084</loginPolicyId>
        </ipRanges>
        <timeRanges>
            <startTime>08:00</startTime>
            <loginPolicyId>1084</loginPolicyId>
            <endTime>18:00</endTime>
        </timeRanges>
    </loginPolicy>
    <organization>
        <muserId>admin</muserId>
        <internal>false</internal>
        <multiCloudStatus>86</multiCloudStatus>
        <level>0.1.24</level>
        <name>sub-org-1</name>
        <supportRegions>["cn-***-d01"]</supportRegions>
        <ctime>1657608949009</ctime>
        <alias>sub-org-1</alias>
        <id>25</id>
        <mtime>1657608949009</mtime>
        <uuid>org-101cc0654e910a420927000w</uuid>
        <cuserId>admin</cuserId>
        <parentId>24</parentId>
        <supportRegionList>["cn-***-d01"]</supportRegionList>
    </organization>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 24, "code": 200, "data": { "cellphoneNum": "188****8888", "enableDingTalk": true, "displayName": "testuser2022", "parentPk": 1127157608934563, "lastLoginTime": 1657608949009, "default": false, "deleted": true, "loginName": "testuser2022", "mobileNationCode": 86, "id": 5817, "enableEmail": true, "enableShortMessage": true, "email": "tets@example.com", "status": "ACTIVE", "primaryKey": 259258662544685340, "userGroupRoles": { "roleRange": "roleRange.resourceSet", "rAMRole": false, "m serId" "admin" |  |

```json
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_RESOURCE_SET_ADMIN",
            "description": "defaultRole.resourceSetAdmin.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceSetAdmin.name",
            "roleLevel": 2147483647,
            "id": 5,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "userGroups": {
            "organizationId": 24,
            "groupName": "testUserGroup01",
            "augId": "aug-101de696afc90a420d270003",
            "createTimeStamp": 1657608949009,
            "id": 145,
            "resourceSets": {
                "organizationID": 3,
                "creator": "admin",
                "resourceGroupName": "test",
                "gmtCreated": 1657608949009,
                "rsId": "rs-9999******",
                "id": 6
            },
            "users": {
                "cellphoneNum": 1606791494471,
                "muserId": 5002,
                "aliyunUser": false,
```

`"backendAccountType": "`用户是否有效。`",`

```json
                "enableDingTalk": false,
                "accountType": 1,
                "active": true,
                "mtime": 1606791494471,
                "organizationId": 24,
                "password": 123456789,
                "default": false,
                "loginTime": 1606791494471,
                "deleted": false,
                "userLoginCtrlId": 1,
                "loginName": "test",
                "ctime": 1606791494471,
                "mobileNationCode": 86,
                "id": 5673,
                "ramUser": true,
                "enableEmail": false,
                "enableShortMessage": false,
                "email": "tets@example.com",
                "defaultRoleId": 3,
                "username": "test"
            },
            "roles": {
                "roleRange": "roleRange.resourceSet",
                "rAMRole": false,
                "muserId": "admin",
                "arId": "lp-101de13d33320a420d27000p",
                "code": "ROLE_RESOURCE_USER",
                "description": "defaultRole.resourceUser.description",
                "active": true,
                "roleType": "ROLETYPE_ASCM",
                "default": true,
                "ownerOrganizationId": 1,
                "enable": true,
                "roleName": "defaultRole.resourceUser.name",
                "roleLevel": 2147483647,
                "id": 2,
                "organizationVisibility": "organizationVisibility.global",
                "cuserId": "admin"
            },
            "organization": {
                "muserId": "admin",
                "internal": false,
                "multiCloudStatus": "master",
                "level": "0.1.24",
                "name": "sub-org-1",
                "supportRegions": "[ \"cn-qingdao-****-d01\"]",
                "ctime": 1657608949009,
                "alias": "sub-org-1",
                "id": 25,
                "mtime": 1657608949009,
                "uuid": "org-101cc0654e910a420927000w",
                "cuserId": "admin",
                "parentId": 24,
```

```json
                "supportRegionList": "[ \"cn-qingdao-****-d01\"]"
            }
        },
        "userRoles": {
            "roleRange": "roleRange.resourceSet",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_RESOURCE_USER",
            "description": "defaultRole.resourceUser.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.resourceUser.name",
            "roleLevel": 2147483647,
            "id": 2,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "accessKeys": {
            "ctime": 1606675230000,
            "id": 1,
            "region": "cn-qingdao-****-d01",
            "cuserId": "admin",
            "status": "ACTIVE",
            "accesskeyId": "tCr5mJ******"
        },
        "roles": {
            "roleRange": "roleRange.allOrganizations",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-9999******",
            "code": "ROLE_GLOBAL_RESOURCE_AUDITOR",
            "description": "defaultRole.globalResourceAuditor.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.globalResourceAuditor.name",
            "roleLevel": 2147483647,
            "id": 6,
            "organizationVisibility": "organizationVisibility.global",
            "cuserId": "admin"
        },
        "defaultRole": {
            "roleRange": "roleRange.orgAndSubOrgs",
            "rAMRole": false,
            "muserId": "admin",
            "arId": "ar-99999******",
            "code": "ROLE_ORGANIZATION_ADMIN",
            "description": "defaultRole.organizationAdmin.description",
            "active": true,
            "roleType": "ROLETYPE_ASCM",
            "default": true,
            "ownerOrganizationId": 1,
            "enable": true,
            "roleName": "defaultRole.organizationAdmin.name",
            "roleLevel": 2147483647,
            "id": 4,
            "organizationVisibility": "organizationVisibility.global"
        },
        "loginPolicy": {
            "muserId": "admin",
            "default": false,
            "ownerOrganizationId": 1,
            "enable": true,
            "name": "mytest",
            "rule": "DENY",
            "id": 1084,
            "organizationVisibility": "organizationVisibility.global",
            "lpId": "lp-101de13d33320a420d27000p",
            "cuserId": "admin",
            "ipRanges": {
                "protocol": "IPV4",
                "ipRange": "10.48.16.1/24",
                "loginPolicyId": 1084
            },
            "timeRanges": {
                "startTime": "08:00",
                "loginPolicyId": 1084,
                "endTime": "18:00"
            }
        },
        "organization": {
```

```json
            "muserId": "admin",
            "internal": false,
            "multiCloudStatus": 86,
            "level": "0.1.24",
            "name": "sub-org-1",
            "supportRegions": "[\"cn-***-d01\"]",
            "ctime": 1657608949009,
            "alias": "sub-org-1",
            "id": 25,
            "mtime": 1657608949009,
            "uuid": "org-101cc0654e910a420927000w",
            "cuserId": "admin",
            "parentId": 24,
            "supportRegionList": "[\"cn-***-d01\"]"
        }
    },
    "success": true,
    "message": "success"
}
```

###### 4.1.1.5.9. GetUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| userGroupId | Integer | Query | 否 | 123 | 用户组ID。 |
| augId | String | Query | 否 | aug-101de696afc90a420d****** | 用户组唯一编码。 |

userGroupId和augId两个入参至少填写其中一个。如果都填写，则取augId入参。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 121 | 状态码。 |
| errorKey | String | ascm.auth.InvalidParameter | 错误码。 |
| message | String | success | 错误提示信息，无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| cost | Long | 36 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct | - | 响应结果。 |
| -id | Integer | 123 | 用户组ID。 |
| -groupName | String | TestGroup | 用户组名称。 |
| -organizationId | Integer | 3 | 用户组所属组织ID。 |
| -createTimeStamp | Long | 1606791494471 | 用户组创建时间。 |
| -augId | String | aug-101de696afc90a420d****** | 用户组唯一编码。 |

**示例**

请求示例 &公共请求参数

```json
{
    "userGroupId":"123",
    "augId":"aug-101de696afc90a420d******"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.auth.InvalidParameter", "code":"121", "cost":36, "data":{ "organizationId":3, "groupName":"TestGroup", "augId":"aug-101de696afc90a420d******", "createTimeStamp":1606791494471, "id":123 }, "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <errorKey>ascm.auth.InvalidParameter</errorKey> <code>121</code> <cost>36</cost> <data> <organizationId>3</organizationId> <groupName>TestGroup</groupName> <augId>aug-101de696afc90a420d******</augId> <createTimeStamp>1606791494471</createTimeStamp> <id>123</id> </data> <success>true</success> <message>success</message> |  |

###### 4.1.1.5.10. RemoveResourceSetFromUserGroup

调用RemoveResourceSetFromUserGroup从用户组删除资源集。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/removeResourceSetFromUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 1 | 用户组ID，可通过调用ListUserGroups接口获取。 说明该参数为必填。 |
| resourceSetId | Integer | Body | 否 | 1 | 资源集ID，可通过调用ListResourceGroup接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 400：缺少参数。 403：没有权限。 404：用户组/资源集不存在。 500：内部错误。 |
|---|---|---|---|
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter：缺少参数。 Forbidden：没有权限。 NotExist：用户组/资源集不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/removeResourceSetFromUserGroup HTTP/1.1
```

公共请求头

```json
{
    "resourceSetId": 1,
    "userGroupId": 1
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.5.11. RemoveRoleFromUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/removeRoleFromUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 1 | 用户组ID，可通过调用ListUserGroups接口获取。 说明该参数为必填。 |
| roleId | Integer | Body | 否 | 2 | 角色ID，可通过调用ListActiveRoles接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400： 参数错误。 缺少参数。 403：没有权限。 404： 用户组不存在。 角色不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 success：调用成功。 InvalidParameter： 参数错误。 缺少参数。 Forbidden：没有权限。 NotExist： 用户组不存在。 角色不存在。 InternalServerError：内部错误。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/removeRoleFromUserGroup HTTP/1.1
```

公共请求头

```json
{
    "roleId": "1",
    "userGroupId": "2"
}
```

正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "success": true, "message": "success" } |  |

###### 4.1.1.5.12. RemoveUsersFromUserGroup

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/removeUsersFromUserGroup HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| userGroupId | Integer | Body | 否 | 190 | 用户组ID。可通过调用ListUserGroups接口获取。 说明该参数为必填。 |
| loginNameList.N | RepeatList | Body | 否 | ["testuser2022"] | 用户登录名列表。用户登录名，由大小写英文字母、数字、下划线（_）、短划线（-）、半角句号（.）组成，长度为2~64个字符。支持批量移除多个用户，多个用户名之间用英文逗号（,）隔开。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 453 | 接口响应耗时，单位毫秒（ms）。 |

| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
|---|---|---|---|
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/user/removeUsersFromUserGroup HTTP/1.1
```

公共请求头

```json
{
    "loginNameList": "["testuser2022"]",
    "userGroupId": 190
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>453</cost> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 453, "success": true, "message": "success" } |  |

##### 4.1.1.6. 登录策略管理

###### 4.1.1.6.1. AddLoginPolicy

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/addLoginPolicy HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| name | String | Body | 否 | mytest | 登录策略名。长度为2~50个字符。 说明该参数为必填。 |

| description | String | Body | 否 | test |  | 登录策略描述。 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| rule | String | Body | 否 | DENY |  | 登录策略的策略属性，默认为ALLOW。 ALLOW：白名单。 DENY：黑名单。 |  |  |  |
| ipRanges | Json |  |  |  |  | 登录策略的IP段，不传则为空。 说明该参数需要按照格式传入，格式为 [{"protocol":"<登 |  |  |  |
|  |  |  |  |  |  |  | 说明该参数需要按照格式传入，格式为 [{"protocol":"<登 |  |  |
|  |  |  |  |  |  |  |  | [{"protocol":"<登 |  |
|  |  |  |  |  |  |  | 录策略所使用协议>","ipRange":"<登录策略IP段 |  |  |
|  |  | Body | 否 | [{"protocol":"IPV4","ipRan ge":"192.168.1.0/24"}] |  |  | >"}] |  |  |
| timeRanges | Json | Body | 否 | [{"startTime":"00:00","en dTime":"24:00"}] |  | 登录策略的时间段，不传则为空。 说明该参数需要按照格式传入，格式为 [{"startTime":"< |  |  |  |
|  |  |  |  |  |  |  | 说明该参数需要按照格式传入，格式为 [{"startTime":"< |  |  |
|  |  |  |  |  |  |  |  | [{"startTime":"< |  |
|  |  |  |  |  | :00"}] |  | 开始时间>","endTime":"<结束时间>}] |  |  |
| enable | Boolean | Body | 否 | true |  | 登录策略是否有效，不传默认为true。 |  |  |  |
| organizationVisibility | String | Body | 否 | organizationVisibility.glob al |  | 登录策略共享范围,不传默认全局共享： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 19 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 登录策略数据。 |

| cuserId | String | admin | 登录策略创建者的用户名。 说明参数已经废弃 |
|---|---|---|---|
| default | Boolean | true | 是否为默认登录策略。 ture：是 。 false：不是。 说明默认策略由系统自动生成，不可修改。 |
| description | String | test | 登录策略描述。 |
| enable | Boolean | true | 登录策略是否有效。 ture：有效。 false：无效。 |
| id | Integer | 1081 | 登录策略ID。 |
| ipRanges | Array of ipRang |  | 登录策略IP段。 |
| ipRange | String | 192.168.1.0/24 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1081 | 所属登录策略的ID。 |
| protocol | String | IPV4 | 登录策略使用协议，目前仅支持IPv4。 |
| lpId | String | lp-101de08b72030a420d****** | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 说明该参数已经废弃。 |
| name | String | defaultLoginPolicy.name | 登录策略名。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 登录策略所属组织的ID。 |
| rule | String | DENY | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRang |  | 登录策略的时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1081 | 所属登录策略的ID。 |
| startTime | String | 00:00 | 开始时间。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |

| pureListData | Boolean | true | 是否只返回数据。 说明该参数已废弃。 |
|---|---|---|---|
| redirect | Boolean | false | 是否重定向。 说明该参数已经废弃 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/addLoginPolicy HTTP/1.1
```

公共请求头

```json
{
    "name": "mytest",
    "rule": "DENY"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>19</cost> <data> <muserId/> <timeRanges> <loginPolicyId>1081</loginPolicyId> <startTime>00:00</startTime> <endTime>24:00</endTime> </timeRanges> <description>test</description> <rule>DENY</rule> <lpId>lp-101de08b72030a420d27000a</lpId> <ipRanges> <protocol>IPV4</protocol> <ipRange>192.168.1.0/24</ipRange> <loginPolicyId>1081</loginPolicyId> </ipRanges> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <name>mytest</name> <id>1081</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> </data> <success>true</success> <message>success</message> |  |

`JSON` 格式

```json
{
    "code": "200",
    "cost": 19,
    "data": {
        "muserId": "",
        "timeRanges": [
            {
                "loginPolicyId": 1081,
                "startTime": "00:00",
                "endTime": "24:00"
            }
```

`],`

```json
        "description": "test",
        "rule": "DENY",
        "lpId": "lp-101de08b72030a420d27000a",
        "ipRanges": [
            {
                "protocol": "IPV4",
                "ipRange": "192.168.1.0/24",
                "loginPolicyId": 1081
            }
```

`],`

```json
        "default": false,
        "ownerOrganizationId": 1,
        "enable": true,
        "name": "mytest",
        "id": 1081,
        "organizationVisibility": "organizationVisibility.global"
    },
    "success": true,
    "message": "success"
}
```

###### 4.1.1.6.2. CheckLoginPolicy

该接口实际效果是在指定条件下模拟登录Apsara Uni-manager运营控制台，用于检测指定用户所使用的登录策略是否生效。被检测的登录策略为请求参数中用户名对应的用户所绑定的登录策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/checkLoginPolicy HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | WFAdmin | 用于检测的用户登录名。 说明该参数为必填。 |
| ip | String | Body | 否 | 192.168.1.0 | 用于检测的用户登录IP，分为白名单策略和黑名单策略。 说明该参数为必填。 |
| time | Long | Body | 否 | 1662446863445 | 用于检测的用户登录时间戳，默认为系统当前时间戳。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 7 | 接口响应耗时，单位毫秒（ms）。 |
| data | Boolean | true | 请求参数是否通过登录策略校验。 true: 通过校验。例如，登录策略为黑名单策略，用户登录IP不在黑名单中，则 data返回true。 false: 未通过校验。例如，登录策略为黑名单策略，用户登录IP在黑名单中， 则data返回false。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/checkLoginPolicy HTTP/1.1
```

公共请求头

```json
{
    "loginName": "WFAdmin",
    "ip": "192.168.1.0"
}
```

正常返回示例 `XML` 格式

```xml
<code>200</code> <cost>7</cost> <data>true</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 7, "data": true, "success": true, "message": "success" } |  |

###### 4.1.1.6.3. GetLoginPolicyById

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/getLoginPolicyById HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 1083 | 登录策略ID。可通过调用ListLoginPolicies接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 14 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应结果。 |

| cuserId | String | admin | 登录策略创建者的用户名。 说明该参数已经废弃。 |
|---|---|---|---|
| default | Boolean | false | 是否为默认登录策略。 说明默认登录策略由系统自动生成，不可修改。 |
| description | String | test | 登录策略的描述。 |
| enable | Boolean | true | 登录策略是否有效。 true：有效。 false：无效。 |
| id | Integer | 1083 | 登录策略ID。 |
| ipRanges | Array of ipRange |  | 登录策略的IP段。 |
| ipRange | String | 192.168.1.0/24 | IP范围。 |
| loginPolicyId | Integer | 1083 | 所属登录策略ID。 |
| protocol | String | IPV4 | 登录策略使用的协议，仅支持IPv4。 |
| lpId | String | lp-101de0c1fa870a4209****** | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 登录策略名。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1 | 所属登录策略的ID. |
| startTime | String | 00:00 | 开始时间。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |

| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/getLoginPolicyById HTTP/1.1
```

公共请求头

```json
{
    "id":"1083"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>14</cost> <code>200</code> <data> <muserId>admin</muserId> <default>false</default> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <name>mytest</name> <rule>ALLOW</rule> <description>test</description> <id>1083</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>lp-101de0c1fa870a4209******</lpId> <cuserId>admin</cuserId> <ipRanges> <protocol>IPV4</protocol> <ipRange>192.168.1.0/24</ipRange> <loginPolicyId>1083</loginPolicyId> </ipRanges> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1</loginPolicyId> <endTime>24:00</endTime> </timeRanges> </data> <success>true</success> <message>success</message> |  |

`JSON` 格式

```json
{
    "redirect": false,
    "cost": 14,
    "code": 200,
    "data": {
        "muserId": "admin",
        "default": false,
        "ownerOrganizationId": 1,
        "enable": true,
        "name": "mytest",
        "rule": "ALLOW",
        "description": "test",
        "id": 1083,
        "organizationVisibility": "organizationVisibility.global",
        "lpId": "lp-101de0c1fa870a4209******",
        "cuserId": "admin",
        "ipRanges": {
            "protocol": "IPV4",
            "ipRange": "192.168.1.0/24",
            "loginPolicyId": 1083
        },
        "timeRanges": {
            "startTime": "00:00",
            "loginPolicyId": 1,
            "endTime": "24:00"
        }
    },
    "success": true,
    "message": "success"
}
```

###### 4.1.1.6.4. GetLoginPolicyByLoginName

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/getLoginPolicyByLoginName HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | WFAdmin | 用户登录名。 说明该参数为必选。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 25 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应结果。 |
| cuserId | String | admin | 登录策略创建者的用户名。 说明该参数已废弃。 |
| default | Boolean | true | 是否为默认登录策略。 说明默认策略由系统自动生成，不可修改。 |
| description | String | test | 登录策略的描述。 |
| enable | Boolean | true | 登录策略的状态。 true：有效。 false：无效。 |
| id | Integer | 1 | 登录策略ID。 |
| ipRanges | Array of ipRange |  | 登录策略的IP段。 |
| ipRange | String | 0.0.0.0/0 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1 | 所属登录策略的ID。 |
| protocol | String | IPV4 | 登录策略使用的协议，目前仅支持IPv4。 |
| lpId | String | lp-9999999999 | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | defaultLoginPolicy.name | 登录策略名。 |
| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |

| ownerOrganizationId | Integer | 1 | 登录策略拥有者所属组织的ID。 |
|---|---|---|---|
| rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRange |  | 登录策略的时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1081 | 所属登录策略的ID。 |
| startTime | String | 00:00 | 开始时间。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 说明该参数已废弃。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/getLoginPolicyByLoginName HTTP/1.1
```

公共请求头

```json
{
    "loginName": "WFAdmin"
}
```

正常返回示例 `XML` 格式

```xml
<redirect>false</redirect> <cost>10000</cost> <code>200</code> <data>
    <ipRanges>
        <ipRange>0.0.0.0/0</ipRange>
        <protocol>IPV4</protocol>
        <loginPolicyId>1</loginPolicyId>
    </ipRanges>
    <muserId>admin</muserId>
    <default>true</default>
    <ownerOrganizationId>1</ownerOrganizationId>
    <timeRanges>
        <startTime>00:00</startTime>
        <loginPolicyId>1</loginPolicyId>
        <endTime>24:00</endTime>
    </timeRanges>
    <enable>true</enable>
    <name>defaultLoginPolicy.name</name>
    <rule>ALLOW</rule>
    <id>1</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
    <lpId>111</lpId>
    <cuserId>admin</cuserId>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 25, "data": { "muserId": "", "timeRanges": [ { "loginPolicyId": 1, "startTime": "00:00", "endTime": "24:00" } ], "rule": "ALLOW", "lpId": "lp-9999999999", "ipRanges": [ { "protocol": "IPV4", "ipRange": "0.0.0.0/0", "loginPolicyId": 1 } ], "default": true, "ownerOrganizationId": 1, "enable": true, "name": "defaultLoginPolicy.name", "id": 1, "cuserId": "", "organizationVisibility": "organizationVisibility.global" }, "success": true, "message": "success" } |  |

###### 4.1.1.6.5. ListLoginPolicies

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/listLoginPolicies HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| name | String | Body | 否 | mytest | 登录策略名。使用登录策略名进行模糊查询，不传则返回Apsara Uni-manager运营控制台中全部登录策略。 |

| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
|---|---|---|---|---|---|
| pageSize | Integer | Body | 否 | 10 | 返回结果中每个分页展示的记录数。默认为10，即在返回结果中每个分页展示10条返回数据。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 16 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of dataItem |  | 登录策略列表。 |
| cuserId | String | admin | 登录策略创建者的用户名。 |
| default | Boolean | false | 是否为默认登录策略。 |
| description | String | test | 登录策略的描述。 |
| enable | Boolean | true | 登录策略是否有效。 true：有效。 false：无效。 |
| id | Integer | 1081 | 登录策略ID。 |
| ipRanges | Array of ipRang |  | 登录策略的IP段。 |
| ipRange | String | 0.0.0.0/0 | 登录策略的IP范围。 |
| loginPolicyId | Integer | 1081 | 所属登录策略的ID。 |
| protocol | String | IPv4 | 登录策略所使用的协议，仅支持IPv4。 |
| lpId | String | lp-101de08b72030a420****** | 登录策略唯一编码。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 登录策略名。 |

| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | 所属组织ID。 |
| rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRang |  | 登录策略的时间段。 |
| endTime | String | 24:00 | 结束时间。 |
| loginPolicyId | Integer | 1081 | 所属登录策略的ID。 |
| startTime | String | 00:00 | 开始时间。 |
| userCount | Integer | 12 | 使用该登录策略的人数。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 10 | 每页大小。 |
| total | Integer | 1 | 返回记录总数。 |
| totalPage | Integer | 1 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/listLoginPolicies HTTP/1.1
```

公共请求头

```json
{
    "name": "mytest",
    "currentPage: 1,
    "pageSize": 10
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>16</cost> <code>200</code> <data> <muserId>admin</muserId> <default>false</default> <userCount>12</userCount> <ownerOrganizationId>1</ownerOrganizationId> <enable>true</enable> <name>mytest</name> <rule>ALLOW</rule> <description>test</description> <id>1081</id> <organizationVisibility>organizationVisibility.global</organizationVisibility> <lpId>lp-101de08b72030a420******</lpId> <cuserId>admin</cuserId> <ipRanges> <protocol>IPv4</protocol> <ipRange>0.0.0.0/0</ipRange> <loginPolicyId>1081</loginPolicyId> </ipRanges> <timeRanges> <startTime>00:00</startTime> <loginPolicyId>1081</loginPolicyId> <endTime>24:00</endTime> </timeRanges> </data> <success>true</success> <pageInfo> <total>1</total> <totalPage>1</totalPage> <pageSize>10</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 16, "code": 200, "data": { "muserId": "admin", "default": false, "userCount": 12, "ownerOrganizationId": 1, "enable": true, "name": "mytest", "rule": "ALLOW", "description": "test", "id": 1081, "organizationVisibility": "organizationVisibility.global", "lpId": "lp-101de08b72030a420******", "cuserId": "admin", "ipRanges": { "protocol": "IPv4", "ipRange": "0.0.0.0/0", "loginPolicyId": 1081 }, "timeRanges": { "startTime": "00:00", "loginPolicyId": 1081, "endTime": "24:00" } }, "success": true, "pageInfo": { "total": 1, "totalPage": 1, "pageSize": 10, "currentPage": 1 }, "message": "success" } |  |

###### 4.1.1.6.6. ModifyLoginPolicy

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/modifyLoginPolicy HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 |  |  | 是否必选 | 示例值 |  | 描述 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| id | Integer | Body |  |  | 否 | 1083 |  | 登录策略ID。可通过调用ListLoginPolicies接口获取。 说明该参数为必填。 |  |  |  |  |
| name | String | Body |  |  | 否 | mytest |  | 修改后的登录策略名，若不传则不修改登录策略名称。 |  |  |  |  |
| description | String | Body |  |  | 否 | test |  | 修改后的登录策略描述，若不传则不修改描述。 |  |  |  |  |
| rule | String | Body |  |  | 否 | DENY |  | 修改后的登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |  |  |  |  |
| ipRanges | Json | Body |  |  |  |  |  | 修改后的IP段，若不传则不修改IP网段校验规则。 说明该参数需要按照格式传入，格式为 [{"ipRange":"<登录 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 说明该参数需要按照格式传入，格式为 [{"ipRange":"<登录 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [{"ipRange":"<登录 |  |  |
|  |  |  |  |  |  |  |  |  | 策略IP段>","loginPolicyId":<登录策略 |  |  |  |
|  |  |  |  |  |  | [{"ipRange":"10.48.16.1/2 |  |  | ID>,"protocol":"<登录策略协议>"}] |  |  |  |
|  |  |  |  |  | 否 | 4","loginPolicyId":1083,"pr otocol":"IPV4"}] |  |  |  |  |  |  |
| timeRanges | Json | Body |  |  |  |  |  | 修改后的登录时间段，若不传则不修改登录时间段校验规则。 说明该参数需要按照格式传入，格式为 [{"endTime":"<结束 |  |  |  |  |
|  |  |  |  |  |  |  |  |  | 说明该参数需要按照格式传入，格式为 [{"endTime":"<结束 |  |  |  |
|  |  |  |  |  |  |  |  |  |  | [{"endTime":"<结束 |  |  |
|  |  |  |  |  |  |  |  |  | 时间>","loginPolicyId":<登录策略 |  |  |  |
|  |  |  |  |  |  | [{"endTime":"18:00","logi |  |  | ID>,"startTime":"<开始时间>"}] |  |  |  |
|  |  |  |  |  | 否 | nPolicyId":1083,"startTime ":"08:00"}] |  |  |  |  |  |  |
| enable | Boolean | Body |  |  | 否 | true |  | 登录策略的状态。 true：有效。 false：无效。 说明若传入false，则该登录策略将被禁用，登录策略状态将变为无效。禁用策略后绑定该策略的用户将无法登录 Apsara Uni-manager运营控制台。若不传则不修改登录策略的状态。 |  |  |  |  |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 50 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 响应结果。 |
| cuserId | String | admin | 登录策略创建者的用户名。 说明此参数已经废弃。 |
| default | Boolean | false | 是否为默认登录策略。 说明默认策略由系统自动生成，不可修改。 |
| description | String | test | 登录策略的描述。 |
| enable | Boolean | true | 登录策略的状态。 true：有效。 false：无效。 说明若传入false，则该登录策略将被禁用，登录策略状态将变为无效。禁用策略后绑定该策略的用户将无法登录Apsara Uni-manager运营控制台。若不传则不修改登录策略的状态。 |
| id | Integer | 1083 | 登录策略ID。 |
| ipRanges | Array of ipRang |  | 登录策略的IP段。 |
| ipRange | String | 10.48.16.1/24 | IP范围。 |
| loginPolicyId | Integer | 1083 | 所属登录策略ID。 |
| protocol | String | IPV4 | 登录策略使用的协议，仅支持ipv4。 |
| lpId | String | lp-101de0c1fa870a420927000x | 登录策略唯一编码。 |
| mtime | Long | 1608175299345 | 登录策略最近一次修改的时间。 |
| muserId | String | admin | 登录策略最近一次修改的修改者用户名。 |
| name | String | mytest | 登录策略名。 |

| organizationVisibility | String | organizationVisibility.global | 登录策略共享范围： organizationVisibility.global：全局共享。 organizationVisibility.organization：本组织内共享。 organizationVisibility.orgAndSubOrgs：下级组织共享。 |
|---|---|---|---|
| ownerOrganizationId | Integer | 1 | 登录策略所属组织的ID。 |
| rule | String | ALLOW | 登录策略的策略属性。 ALLOW：白名单。 DENY：黑名单。 |
| timeRanges | Array of timeRang |  | 登录策略时间段。 |
| endTime | String | 18:00 | 结束时间。 |
| loginPolicyId | Integer | 1083 | 所属登录策略ID。 |
| startTime | String | 08:00 | 开始时间。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/modifyLoginPolicy HTTP/1.1
```

公共请求头

```json
{
    "id": 2
}
```

正常返回示例 `XML` 格式

```xml
<code>200</code> <cost>50</cost> <data>
    <muserId/>
    <timeRanges>
        <loginPolicyId>1083</loginPolicyId>
        <startTime>08:00</startTime>
        <endTime>18:00</endTime>
    </timeRanges>
    <description>test</description>
    <rule>DENY</rule>
    <mtime>1662446862771</mtime>
    <lpId>lp-101de0c1fa870a420927000x</lpId>
    <ipRanges>
        <protocol>IPV4</protocol>
        <ipRange>10.48.16.1/24</ipRange>
        <loginPolicyId>1083</loginPolicyId>
    </ipRanges>
    <default>false</default>
    <ownerOrganizationId>1</ownerOrganizationId>
    <enable>true</enable>
    <name>mytest</name>
    <id>1083</id>
    <organizationVisibility>organizationVisibility.global</organizationVisibility>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 50, "data": { "muserId": "", "timeRanges": [ { "loginPolicyId": 1083, "startTime": "08:00", "endTime": "18:00" } ], "description": "test", "rule": "DENY", "mtime": 1662446862771, "lpId": "lp-101de0c1fa870a420927000x", "ipRanges": [ { "protocol": "IPV4", "ipRange": "10.48.16.1/24", "loginPolicyId": 1083 } ], "default": false, "ownerOrganizationId": 1, "enable": true, "name": "mytest", "id": 1083, "organizationVisibility": "organizationVisibility.global" }, "success": true, "message": "success" } |  |

##### 4.1.1.7. 变更管理

###### 4.1.1.7.1. UpdateInstanceBelong

不能跨一级组织变更实例归属。 调用时会检查是否超出目标组织该产品的配额，若超出配额则会返回报错信息，错误码为510。 ECS安全组和VPC交换机仅支持在所属VPC共享范围内变更。 变更ECS实例会同步变更ECS实例下的磁盘、快照和弹性网卡。 变更VPC实例会同步变更VPC下的路由表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceType | String | Body | 是 | ecsinstance _ | 资源类型。 可以登录Apsara Unimanager运营控制台前往企业->资源管理->变更管理选择组织中的资源集，依次选择产品类型和资源类型 ， 下方列表中资源类型列的值即为所需的实际值。 |
| InstanceId | String | Body | 是 | i-0jp******* | 实例ID。 |
| RegionName | String | Body | 是 | cn-****-d01 | 实例所在地域。 |
| TargetResourceSetI d | String | Body | 否 | 2 | 目标资源集ID。 可通过调用ListResourceGroup接口获取， 或直接登录Apsara Uni-manager运营控制台在_企业>资源管理>资源集管理_中查看。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| Code | String | 200 | 状态码。 200：调用正常。 400： 无效的资源类型。 未找到资源集。 无效的实例ID。 顶级组织不匹配。 变更失败。 403：没有权限。 510：超过配额。 |
| Message | String | exampleerrmessage | 提示信息。例如： 成功则返回为空。 失败则返回具体失败信息。 |
| RequestId | String | 530dxxx-dxx******-x6b61axxxxx | 变更某资源集的请求ID。 |
| ErrorKey | String | exampleErrKey | 异常状态码。 |
| Cost | Long | 934 | 接口响应耗时，单位毫秒（ms）。 |
| Path | String | examplepath | 请求路径 |
| Redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| IsPureListData | Boolean | false | 当前是否包含数据返回。 |
| PureListDataString | String | false | 数据详情。 |

**示例**

`JSON` 格式

```json
{
 "Path":"examplepath",
 "PureListDataString":"false",
 "Message":"exampleerrmessage",
 "RequestId":"530dxxx-dxx******-x6b61axxxxx",
 "IsPureListData":false,
 "ErrorKey":"exampleErrKey",
 "Redirect":false,
 "Code":"200",
 "Cost":934,
 "Success":true
}
```

| XML | 格式 |
|---|---|
| <Path>examplepath</Path> <PureListDataString>false</PureListDataString> <Message>exampleerrmessage</Message> <RequestId>530dxxx-dxx******-x6b61axxxxx</RequestId> <IsPureListData>false</IsPureListData> <ErrorKey>exampleErrKey</ErrorKey> <Redirect>false</Redirect> <Code>200</Code> <Cost>934</Cost> <Success>true</Success> |  |

###### 4.1.1.7.2. UpdateInstancesBelong

调用UpdateInstanceBelong接口变更同一资源类型的多个实例的归属。不能跨一级组织变更实例归属。调用时会检查是否超出目标组织该产品的配额，若超出配额则会返回报错信息，错误码为510。 ECS安全组和VPC交换机仅支持在所属VPC共享范围内变更。变更ECS实例会同步变更ECS实例下的磁盘、快照和弹性网卡。变更VPC实例会同步变更VPC下的路由表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /belong/updateInstances HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceType | String | Body | 是 | ecsinstance _ | 资源类型，必填 |
| instanceList | String | Body | 是 | [{\"instanceId\":\"vpc- 4wqbagxxxx\",\"regionId\":\"cn-wulan- xxxx\"},{\"instanceId\":\"vpc- 4wq3xxxx\",\"regionId\":\"cn-xxxx\"}] | 实例列表，必填 |
| targetResourceSetI d | String | Body | 是 | 1 | 目标资源集ID，必填 |
| platformCode | String | Body | 否 | default | 平台代码默认值：default |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 是否成功 |
| Code | String | 200 | 状态码 |
| Message | String | success | 提示信息 |
| RequestId | String | E43F52CE-42B8-581B-B818- 3C50B276566C | 请求ID |
| ErrorKey | String | error | 错误键 |
| Cost | Long | 100 | 耗时 |
| Path | String | examplepath | 路径 |
| Redirect | Boolean | false | 是否重定向 |
| IsPureListData | Boolean | false | 是否为纯列表数据 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PureListDataString | String | xxx | 纯列表数据字符串 |

**示例**

请求示例

```
POST /belong/updateInstances HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "Path":"", "PureListDataString":"", "Message":"success", "RequestId":"E43F52CE-42B8-581B-B818-3C50B276566C", "IsPureListData":false, "ErrorKey":"", "Redirect":false, "Code":"200", "Cost":100, "Success":true } |  |

###### 4.1.1.7.3. UpdateOrganizationBelong

更新组织归属关系不能跨一级组织变更组织归属。 调用时会检查是否超出目标组织所有产品的配额，若超出配额则会返回报错信息，错误码为510。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| orgId | String | Body | 是 | 4 | 被变更归属的组织id，必填。 |
| targetOrgId | String | Body | 是 | 3 | 目标组织id，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| Code | String | 400 | 状态码。 200：调用正常。 400： 无效的资源类型。 未找到资源集。 无效的实例ID。 顶级组织不匹配。 变更失败。 403：没有权限。 |
| Message | String | "success" | 提示信息。 成功则返回为空。 失败则返回具体失败信息。 |
| RequestId | String | 0a1128a916917198245846573e 0*** | 变更某资源集的请求ID。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ErrorKey | String | ascm.manage.InternalError | 异常状态码。 该参数已废弃。 |
| Cost | Long | 100 | 接口响应耗时，单位毫秒（ms）。 接口经过ASAPI网关时，若从请求发起到响应超过10秒就被判定为超时。 |
| Path | String | /xxx/ | 请求路径该参数已废弃。 |
| Redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| IsPureListData | Boolean | false | 当前是否包含返回数据。 该参数已废弃。 |
| PureListDataString | String | xxx | 数据详情。 该参数已废弃。 |

**示例**

请求示例

```json
{ "orgId":"4", "targetOrgId":"3" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "Path":"/xxx/", "PureListDataString":"xxx", "Message":"\"success\"", "RequestId":"0a1128a916917198245846573e0***", "IsPureListData":false, "ErrorKey":"ascm.manage.InternalError", "Redirect":false, "Code":"400", "Cost":100, "Success":true } |  |

| XML | 格式 |
|---|---|
| <Path>/xxx/</Path> <PureListDataString>xxx</PureListDataString> <Message>&quot;success&quot;</Message> <RequestId>0a1128a916917198245846573e0***</RequestId> <IsPureListData>false</IsPureListData> <ErrorKey>ascm.manage.InternalError</ErrorKey> <Redirect>false</Redirect> <Code>400</Code> <Cost>100</Cost> <Success>true</Success> |  |

###### 4.1.1.7.4. UpdateResourceSetBelong

更新资源集归属关系，仅允许一级组织范围内变更归属，不允许跨一级组织变更资源集归属。 不能跨一级组织变更资源集归属。 调用时会检查是否超出目标组织所有产品的配额，若超出配额则会返回报错信息，错误码为510。 变更资源集归属会同步变更资源集下所有实例的归属。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /belong/updateResourceSet HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceSetId | String | Body | 是 | 3 | 待变更的资源集ID ，必填。 |
| targetOrgId | String | Body | 是 | 3 | 目标组织 ID，必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| Code | String | 400 | 状态码。 200：调用正常。 400： 无效的资源类型。 未找到资源集。 无效的实例ID。 顶级组织不匹配。 变更失败。 403：没有权限。 |
| Message | String | success | 提示信息。例如： 成功则返回为空。 失败则返回具体失败信息。 |
| RequestId | String | 0a1128a916917198245846573e 0*** | 变更某资源集的请求ID。 |
| ErrorKey | String | ascm.manage.InternalError | 异常状态码。 该参数已废弃。 |
| Cost | Long | 100 | 接口响应耗时，单位毫秒（ms）。 接口经过ASAPI网关时，若从请求发起到响应超过10秒就被判定为超时。 |
| Path | String | /xxx/ | 请求路径该参数已废弃。 |
| Redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| IsPureListData | Boolean | false | 当前是否包含返回数据。 该参数已废弃。 |
| PureListDataString | String | xxx | 数据详情。 该参数已废弃。 |

**示例**

请求示例

```json
POST /belong/updateResourceSet HTTP/1.1 { "resourceSetId":"3", "targetOrgId":"3" }
```

正常返回示例 `JSON` 格式

```json
{
 "Path":"/xxx/",
 "PureListDataString":"xxx",
 "Message":"success",
 "RequestId":"0a1128a916917198245846573e0***",
 "IsPureListData":false,
 "ErrorKey":"ascm.manage.InternalError",
 "Redirect":false,
 "Code":"400",
 "Cost":100,
 "Success":true
}
```

| XML | 格式 |
|---|---|
| <Path>/xxx/</Path> <PureListDataString>xxx</PureListDataString> <Message>success</Message> <RequestId>0a1128a916917198245846573e0***</RequestId> <IsPureListData>false</IsPureListData> <ErrorKey>ascm.manage.InternalError</ErrorKey> <Redirect>false</Redirect> <Code>400</Code> <Cost>100</Cost> <Success>true</Success> |  |

#### 4.1.2. 运营中心

##### 4.1.2.1. QueryOrderOpenApi

查询订单的开放API接口，用于外部系统调用以获取订单相关信息。 调用QueryOrderOpenApi查询订单，支持按照云平台、产品、订单id等条件筛选。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /order/queryOrder HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integer | Body | 否 | 10 | 每页数量。 |
| pageNumber | Integer | Body | 否 | 1 | 页码。 起始值：1。 |
| orderId | String | Body | 否 | 202508291358290000010011 | 订单ID。 |
| orgId | String | Body | 否 | 123367 | 订单所属组织的ID。 |
| createTimeStartUtc | String | Body | 否 | 2025-10-22T11:15:00Z | 订单创建时间-起始，YYYY-MM- ddTHH:mm:ssZ，时区： UTC。 |
| createTimeEndUtc | String | Body | 否 | 2025-10-25T11:15:00Z | 订单创建时间-结束，YYYY-MM- ddTHH:mm:ssZ，时区： UTC。 |
| userIds | RepeatList | Body | 否 | ["5003"] | 订单创建人uid列表。 |
| platformCode | String | Body | 否 | default | 云平台code，默认是default，多云时会有不同的平台code。 |
| serviceId | String | Body | 否 | CS000001 | 服务ID。 |
| productCode | String | Body | 否 | ecs | 云产品编码。 |
| templateCodeList | RepeatList | Body | 否 | ["ecs#securitygroup"] _ | 资源项编码列表。 |
| orderType | String | Body | 否 | new | 订单类型。 |
| instanceId | String | Body | 否 | i-pb400oibibyasklqotqv | 实例ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| chargeType | String | Body | 否 | postPay | 订单类型。 |
| statusList | RepeatList | Body | 否 | ["success","cancel"] | 订单状态。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [] | 查询结果 |
| -instanceList | Array | [] | 实例列表。 |
| --instanceId | String | i-pb400oibibyasklqotqv | 实例ID。 |
| --instanceName | String | test111 | 实例名称。 |
| --regionId | String | cn-shanghai-d01 | 订单账所属区域。 |
| --createTimeUtc | String | 2025-10-25T11:15:00Z | 订单创建时间，格式：YYYY-MM-ddTHH:mm:ssZ，时区： UTC |
| --expireTimeUtc | String | 2025-10-29T11:15:00Z | 订单到期时间，格式：YYYY-MM-ddTHH:mm:ssZ，时区： UTC |
| -orderId | String | 202508291348290000010001 | 订单ID。 |
| -orderType | String | new | 订单类型。 枚举值: 新购(new) 变配(modify) 退订(unsubscribe) 续费(renew) 包月转按量(monthlyPayToPostPay) 按量转包月(postPayToMonthlyPay) |
| -platformCode | String | default | 云平台Code。 单云或多云主云为default。 公共云从云、专有云从云为pl-xxxxx。 |
| -platformName | String | 中心云 | 云平台名称。 |
| -previewInfo | String | {\"chargeType\":{\"preview\":\"按量计费\",\"label\":\"计费方式 \"},\"SupportHotUpgrade\": {\"preview\":\"是\",\"label\":\"开启热变配\"}} | 下单请求时服务目录配置信息 |
| -chargeType | String | postPay | 订单类型。 枚举值: 包年包月(monthlyPay) 按量计费(postPay) |
| -num | Integer | 1 | 购买数量 |
| -duration | String | P4D | 时长信息，只在包年包月订单有 |
| -price | String | 10.00 | 费用，仅支付费用，退款时为空 |
| -refund | String | 10.00 | 退款，退订时如产生退款则有，其他情况为空 |
| -currency | String | CNY | 货币单位。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -orderStatus | String | new | 订单状态枚举值: 审批中(auditing) 审批拒绝(audit _reject) 待处理(waiting) 处理中(delivering) 处理失败(deliver _fail) 处理完成(success) 取消(cancel) 审批取消(approve _cancel) |
| -orgId | String | 112267 | 组织ID。 |
| -orgName | String | 部门1 | 组织名称。 |
| -resourceGroupId | String | resourceGroupTest | 资源集ID。 |
| -resourceGroupName | String | 资源集test | 资源集名称。 |
| -gmtCreateUtc | String | 订单创建时间 | 订单创建时间，格式：YYYY-MM-ddTHH:mm:ssZ，时区： UTC |
| -serviceInfo | Struct | {} | 服务详情。 |
| --serviceId | String | CS000001 | 服务ID。 |
| --serviceName | String | ECS实例 | 服务名称。 |
| --productName | String | 云服务器 ECS | 云产品名称。 |
| -userInfo | Struct | {} | 用户信息。 |
| --userId | String | 5003 | 用户ID。 |
| --userName | String | 用户名 | 用户显示名。 |
| --loginName | String | admin | 用户登录名。 |
| -deliverInfo | Struct | {} | 订单履约详情。 |
| --totalInstanceCount | Integer | 5 | 实例总数。 |
| --successInstanceCount | Integer | 3 | 成功实例数。 |
| --failedInstanceCount | Integer | 1 | 失败实例数。 |
| --canceledInstanceCount | Integer | 1 | 已取消实例数。 |
| total | Integer | 100 | 订单总条数。 |
| pageSize | Integer | 10 | 每页大小。 |
| pageNumber | Integer | 1 | 当前页码。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 响应码。 |
| errorCode | String | UnknownError | 返回错误码。 |
| errorMessage | String | UnknownError | 返回错误信息。 |

**示例**

请求示例

```json
POST /order/queryOrder HTTP/1.1 {
  "platformCode":"default","serviceId":"CS000003",
"chargeType":"postPay","statusList":["auditing","waiting","success","deliver_fail"], "pageNumber":1,"pageSize":10 }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "total":100, "pageNumber":1, "code":"200", "data":[ { "orderType":"new", "orgName":"部门1", "resourceGroupName":"资源集test", "deliverInfo":[ { "successInstanceCount":3, "failedInstanceCount":1, "canceledInstanceCount":1, "totalInstanceCount":5 } ], "orderId":"202508291348290000010001", "userInfo":[ { "loginName":"admin", "userName":"用户名", "userId":"5003" } ], "num":1, "chargeType":"postPay", "orderStatus":"new", "instanceList":[ { "instanceId":"i-pb400oibibyasklqotqv", "expireTimeUtc":"2025-10-29T11:15:00Z", "instanceName":"test111", "regionId":"cn-shanghai-d01", "createTimeUtc":"2025-10-25T11:15:00Z" } ], "orgId":"112267", "duration":"P4D", "previewInfo":"{\\\"chargeType\\\":{\\\"preview\\\":\\\"按量计费\\\",\\\"label\\\":\\\"计费方式\\\"},\\\"SupportHotUpgrade\\\": {\\\"preview\\\":\\\"是\\\",\\\"label\\\":\\\"开启热变配\\\"}}", "serviceInfo":[ { "serviceId":"CS000001", "serviceName":"ECS实例", "productName":"云服务器 ECS" } ], "price":"10.00", "currency":"CNY", "resourceGroupId":"resourceGroupTest", "platformName":"中心云", "platformCode":"default", "refund":"10.00" } ], "success":true, "errorMessage":"UnknownError", "pageSize":10, "errorCode":"UnknownError" } |  |

##### 4.1.2.2. AddCommonSpec

添加自定义规格。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/saleconf/commonSpec/add HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| status | String | Body | 否 | Available | 状态。 |
| specName | String | Body | 否 | 企业增强版 | 中文规格名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 返回数据集。 |
| validationInfo | String | “” | 校验标示。 |
| code | String | 200 | 状态码。 |
| httpOk | Boolean | true | 返回状态。 |
| ip | String | “” | IP地址。 |
| message | String | success | 报错信息。 |
| requestId | String | 0a1ec3c216087759426241251d0 2bd | 请求ID。 |
| success | Boolean | true | 成功标示。 |
| eagleEyeTraceId | String | “” |  |

**示例**

请求示例

```
&resourceType=RDS
```

`&specName=`企业增强版

```
&status=Available
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <data> <success>true</success> <validationInfo>“”</validationInfo> </data> <httpOk>true</httpOk> <requestId>0a1ec3c216087759426241251d02bd</requestId> <success>true</success> <ip>“”</ip> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "data": { "success": "true", "validationInfo": "“”" }, "httpOk": "true", "requestId": "0a1ec3c216087759426241251d02bd", "success": "true", "ip": "“”", "message": "success" } |  |

##### 4.1.2.3. CreateQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| requestId | String | System | 否 | d0c6ed24-45af-4703-866f-5103302b**** | 请求ID。 |
| productName | String | Body | 否 | ecs | 产品名称。例如：ecs、oss、vpc、rds、slb、 odps、eip、adb、gpdb、r-kvstore、drds、 ots、nas或dds等。 |
| quotaBody | Json | Body | 否 | {"totalCpu":100,"totalMem":100,"totalGpu": 100, "totalDiskcloudssd":100,"totalDiskcloud _ _ _ _ efficiency":100} | 产品具体的Quota参数。 |
| quotaTypeId | Integer | Body | 否 | 1 | 如果给组织设置配额，则输入组织ID。 如果给资源集设置配额，则输入资源集ID。 |
| quotaType | String | Body | 否 | organization | 如果为组织创建配额，则输入organization。 如果为资源集创建配额，则输入 resourceGroup。 |
| regionName | String | Body | 否 | cn-****-d01 | Region名称。 |
| clusterName | String | Body | 否 | "" | 预留字段。表示集群名称，可不填写或者传空字符串。 |
| targetType | String | Body | 否 | "" | 如果为RDS产品则输入对应引擎的名称，支持 MySQL和SQLServer。 其他产品则可不填或者传空字符串。 |

云产品的productName及quotaBody参数示例如下：

```json
{"productName":"ecs",
    "quotaBody":{"totalCpu":100,"totalMem":100,"totalGpu":100,
    "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100}
} {"productName":"oss",
    "quotaBody":{"totalAmount":100}
} {"productName":"vpc",
    "quotaBody":{"totalVPC":100}
}
```

云数据库RDS：

```json
{"productName":"rds",
    "quotaBody":{"totalCpu":100,"totalMem":100,"totalDisk":100}
} {"productName":"slb",
    "quotaBody":{"totalVipInternal":100,"totalVipPublic":100}
}
```

MaxCompute（ODPS）：

```json
{"productName":"odps",
    "quotaBody":{"totalCu":100,"totalDisk":100}
}
```

弹性公网EIP：

```json
{"productName":"eip",
    "quotaBody":{"totalEIP":100}
}
```

分析型数据库MySQL版（ADB） :

```json
{"productName": "adb",
    "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}
}
```

分析型数据库PostgreSQL版（GPDB）:

```json
{"productName": "gpdb",
    "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}
}
```

云数据库Redis（R-KVStore） :

```json
{"productName": "r-kvstore",
    "quotaBody":{"totalMem": 100}
} {"productName": "drds",
    "quotaBody":{"totalCpu": 100}
}
 {"productName": "ots",
     "quotaBody":{"totalDisk": 100}
}
 {"productName": "nas",
     "quotaBody":{"totalDisk": 100}
}
```

云数据库MongoDB：

```json
 {"productName": "dds",
     "quotaBody":{"totalCpu": 100, "totalMem": 100, "totalDisk":100}
}
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| requestId | String | 111 | 请求ID。 |
| success | Boolean | true | 是否成功。 |
| pureListData | Boolean | false | 是否只返回数据。 |
| message | String | 200 | 提示信息。 |
| data | Struct | - | 响应数据。 |
| -cluster | String | "" | 集群。 |
| -quotaType | String | organization | 配额类型。 |
| -quotaTypeId | Integer | 1 | 配额ID。 |
| -total | String | {"Cpu":10} | 产品在该组织/资源集的下所有配额项的配额总数。 |
| -allocate | String | {"Cpu":2} | 产品在该组织/资源集的下所有配额项的配额已分配情况。 |
| -used | String | {"Cpu":0} | 产品在该组织/资源集的下所有配额项的配额已使用情况。 |

| -dtFlag | Boolean | false | DT标识。 |
|---|---|---|---|
| -ctime | Float | 1608519825999 | 创建时间。 |
| -targetType | String | mysql | 集群类别。 |
| -id | Integer | 1 | 主键ID。 |
| -region | String | cn-qingdao-env17-d01 | 地域。 |
| -totalGpu | Integer | 10 | 配额总数（GPU）。 |
| -usedGpu | Integer | 1 | 已使用配额（GPU）。 |
| -allocateGpu | Integer | 1 | 已分配配额（GPU）。 |
| -usedMem | Integer | 1 | 已使用配额（内存）。 |
| -totalMem | Integer | 10 | 配额总数（内存）。 |
| -allocateMem | Integer | 1 | 已分配配额（内存）。 |
| -totalDiskcloudssd _ _ | Integer | 10 | 配额总数（SSD）。 |
| -usedDiskcloudssd _ _ | Integer | 1 | 已使用配额（SSD）。 |
| -allocateDiskcloudssd _ _ | Integer | 1 | 已分配配额（SSD）。 |
| -totalDiskcloudefficiency _ _ | Integer | 10 | 配额总数（高效云盘）。 |
| - usedDiskcloudefficiency _ _ | Integer | 1 | 已使用配额（高效云盘）。 |
| - allocateDiskcloudefficie _ _ ncy | Integer | 1 | 已分配配额（高效云盘）。 |
| -usedCpu | Integer | 1 | 已使用配额（CPU）。 |
| -allocateCpu | Integer | 1 | 已分配配额（CPU）。 |
| -totalCpu | Integer | 10 | 配额总数（CPU）。 |
| -totalVPC | Integer | 10 | 配额总数（VPC）。 |
| -usedVPC | Integer | 1 | 已使用配额（VPC）。 |
| -allocateVPC | Integer | 1 | 已分配（VPC）。 |
| -allocateDisk | Integer | 1 | 已分配配额（磁盘）。 |
| -totalDisk | Integer | 10 | 配额总数（磁盘）。 |
| -usedDisk | Integer | 1 | 已使用配额（磁盘）。 |
| -allocateHAVIP | Integer | 1 | 已分配配额（高可用虚拟IP）。 |
| -totalHAVIP | Integer | 10 | 配额总数（高可用虚拟IP）。 |
| -usedHAVIP | Integer | 1 | 已使用配额（高可用虚拟IP）。 |
| -totalAmount | Integer | 10 | 配额总数（Bucket阈值容量）。 |

| -usedAmount | Integer | 1 | 已使用配额（Bucket阈值容量）。 |
|---|---|---|---|
| -allocateAmount | Integer | 1 | 已分配配额（Bucket阈值容量）。 |
| -allocateVipInternal | Integer | 1 | 已分配配额（内网IP配额-VPC网络）。 |
| -allocateVipPublic | Integer | 1 | 已分配配额（公网IP配额）。 |
| -totalVipInternal | Integer | 10 | 配额总数（内网IP配额-VPC网络）。 |
| -totalVipPublic | Integer | 10 | 配额总数（公网IP配额）。 |
| -usedVipInternal | Integer | 1 | 已使用配额（内网IP配额-VPC网络）。 |
| -usedVipPublic | Integer | 1 | 已使用配额（公网IP配额）。 |
| -allocateCu | Integer | 1 | 已分配配额（CU）。 |
| -totalCu | Integer | 10 | 配额总数（CU）。 |
| -usedCu | Integer | 1 | 已使用配额（CU）。 |
| -allocateMQ | Integer | 1 | 已分配配额（MQ）。 |
| -totalMQ | Integer | 10 | 配额总数（MQ）。 |
| -usedMQ | Integer | 1 | 已使用配额（MQ）。 |

**示例**

请求示例

```
&ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1
```

`&<`公共请求参数> 正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":1000,
 "data":{
  "cluster":"\"\"",
  "totalVipInternal":10,
  "used":"{\"Cpu\":0}",
  "usedMQ":1,
  "allocateCu":1,
  "totalDisk":10,
  "totalDisk_cloud_ssd":10,
  "totalCpu":10,
  "ctime":1.6085198E12,
  "id":1,
  "usedGpu":1,
  "totalCu":10,
  "allocateMem":1,
  "totalGpu":10,
  "usedCpu":1,
  "allocateDisk":1,
  "allocateMQ":1,
  "quotaTypeId":1,
  "totalVipPublic":10,
  "usedCu":1,
  "totalMQ":10,
  "totalMem":10,
  "allocateVPC":1,
  "usedDisk":1,
  "quotaType":"organization",
  "totalAmount":10,
  "allocateHAVIP":1,
  "allocate":"{\"Cpu\":2}",
  "dtFlag":false,
  "totalHAVIP":10,
  "usedHAVIP":1,
  "region":"cn-qingdao-env17-d01",
  "allocateDisk_cloud_ssd":1,
  "usedVipInternal":1,
  "allocateVipPublic":1,
  "usedAmount":1,
  "allocateAmount":1,
  "totalDisk_cloud_efficiency":10,
  "total":"{\"Cpu\":10}",
  "usedDisk_cloud_ssd":1,
  "totalVPC":10,
  "usedVPC":1,
  "allocateDisk_cloud_efficiency":1,
  "usedVipPublic":1,
  "allocateVipInternal":1,
  "targetType":"mysql",
  "allocateGpu":1,
  "usedMem":1,
  "allocateCpu":1,
  "usedDisk_cloud_efficiency":1
 },
 "requestId":"111",
 "success":true,
 "pureListData":false,
 "message":"200"
}
```

`XML` 格式

```xml
<code>200</code> <cost>1000</cost> <data>
 <cluster>&quot;&quot;</cluster>
 <totalVipInternal>10</totalVipInternal>
 <used>{&quot;Cpu&quot;:0}</used>
 <usedMQ>1</usedMQ>
 <allocateCu>1</allocateCu>
 <totalDisk>10</totalDisk>
 <totalDisk_cloud_ssd>10</totalDisk_cloud_ssd>
 <totalCpu>10</totalCpu>
 <ctime>1608519800000</ctime>
 <id>1</id>
 <usedGpu>1</usedGpu>
 <totalCu>10</totalCu>
 <allocateMem>1</allocateMem>
 <totalGpu>10</totalGpu>
 <usedCpu>1</usedCpu>
 <allocateDisk>1</allocateDisk>
 <allocateMQ>1</allocateMQ>
 <quotaTypeId>1</quotaTypeId>
 <totalVipPublic>10</totalVipPublic>
 <usedCu>1</usedCu>
 <totalMQ>10</totalMQ>
 <totalMem>10</totalMem>
 <allocateVPC>1</allocateVPC>
 <usedDisk>1</usedDisk>
 <quotaType>organization</quotaType>
 <totalAmount>10</totalAmount>
 <allocateHAVIP>1</allocateHAVIP>
 <allocate>{&quot;Cpu&quot;:2}</allocate>
 <dtFlag>false</dtFlag>
 <totalHAVIP>10</totalHAVIP>
 <usedHAVIP>1</usedHAVIP>
 <region>cn-qingdao-env17-d01</region>
 <allocateDisk_cloud_ssd>1</allocateDisk_cloud_ssd>
 <usedVipInternal>1</usedVipInternal>
 <allocateVipPublic>1</allocateVipPublic>
 <usedAmount>1</usedAmount>
 <allocateAmount>1</allocateAmount>
 <totalDisk_cloud_efficiency>10</totalDisk_cloud_efficiency>
 <total>{&quot;Cpu&quot;:10}</total>
 <usedDisk_cloud_ssd>1</usedDisk_cloud_ssd>
 <totalVPC>10</totalVPC>
 <usedVPC>1</usedVPC>
 <allocateDisk_cloud_efficiency>1</allocateDisk_cloud_efficiency>
 <usedVipPublic>1</usedVipPublic>
 <allocateVipInternal>1</allocateVipInternal>
 <targetType>mysql</targetType>
 <allocateGpu>1</allocateGpu>
 <usedMem>1</usedMem>
 <allocateCpu>1</allocateCpu>
 <usedDisk_cloud_efficiency>1</usedDisk_cloud_efficiency>
</data> <requestId>111</requestId> <success>true</success> <pureListData>false</pureListData> <message>200</message>
```

ascm 2019-05-10

##### 4.1.2.4. DeleteQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/quota/delete HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| quotaTypeId | Integer | Body | 否 | 10 | 配额类型ID。 |
| quotaType | String | Body | 否 | organization | 配额类型。 |

| productName | String | Body | 否 | rds | 产品名称。 |
|---|---|---|---|---|---|
| regionName | String | Body | 否 | regionName | 区域名称。 |
| clusterName | String | Body | 否 | clusterName | 集群名称。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| message | String | 200 | 提示信息。 |
| pureListData | Boolean | false | 是否只返回数据。 |
| redirect | Boolean | false | 是否重定向。 |
| requestId | String | 111 | 请求ID。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |  |

##### 4.1.2.5. DescribeGpdbModifiableInstanceType

获取Gpdb可变配规格接口。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeGpdbModifiableInsta nceType | 系统规定参数。取值：DescribeGpdbModifiableInstanceType。 |
| instanceId | String | 是 | sdfsdfsdfsfdsdf | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 结果集。 |

| result | Array of dataItem |  | 结果集。 |
|---|---|---|---|
| baseVersion | String | 3.13 | 规格版本。 |
| cpu | String | 1 | 处理器数量。 |
| engineVersion | String | 5.6 | 引擎版本。 |
| gmtCreate | String | 2020-12-23 19:08:15 | 创建时间。 |
| gmtModified | String | 2020-12-23 19:08:15 | 修改时间。 |
| label | String | “” | 是否输出国际化： true/false。 |
| memory | String | 4 | 内存。 |
| node | String | “” | 节点。 |
| regionId | String | cn-qingdao-env66-d01 | 区域。 |
| resourceType | String | GDB | 资源类型。 |
| specFrom | String | system | 规格来源。 |
| specification | String | gdb.r.13xlarge | 规格。 |
| status | String | Available | 规格是否可用。 |
| storage | String | 20 | 存储。 |
| status | Integer | 200 | 返回状态。 |
| success | String | true | 请求成功标示。 |
| host | String | “” | host地址。 |
| status | Integer | 200 | 返回状态。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeGpdbModifiableInstanceType &instanceId=sdfsdfsdfsfdsdf
```

`&<`公共请求参数> 正常返回示例 `XML` 格式

```xml
<data>
    <result>
        <engineVersion>5.6</engineVersion>
        <gmtModified>2020-12-23 19:08:15</gmtModified>
        <memory>4</memory>
        <baseVersion>3.13</baseVersion>
        <cpu>1</cpu>
        <specification>gdb.r.13xlarge</specification>
        <specFrom>system</specFrom>
        <storage>20</storage>
        <label>“”</label>
        <gmtCreate>2020-12-23 19:08:15</gmtCreate>
        <node>“”</node>
        <regionId>cn-qingdao-env66-d01</regionId>
        <status>Available</status>
        <resourceType>GDB</resourceType>
    </result>
    <success>true</success>
    <status>200</status>
</data> <host>“”</host> <status>200</status>
```

| JSON | 格式 |
|---|---|
| { "data": { "result": [ { "engineVersion": "5.6", "gmtModified": "2020-12-23 19:08:15", "memory": "4", "baseVersion": "3.13", "cpu": "1", "specification": "gdb.r.13xlarge", "specFrom": "system", "storage": "20", "label": "“”", "gmtCreate": "2020-12-23 19:08:15", "node": "“”", "regionId": "cn-qingdao-env66-d01", "status": "Available", "resourceType": "GDB" } ], "success": "true", "status": "200" }, "host": "“”", "status": "200" } |  |

##### 4.1.2.6. ListEnterpriseCenterQuotas

调用ListEnterpriseCenterQuotas接口获得企业中心使用限制概览信息。 企业中心使用限制包含12项配额数据，调用成功后返回企业中心限制配额和当前云平台各项数据的最大值信息。 MaxResourceSetBindAscmUserLimit：资源集绑定的最大用户个数信息。 MaxResourceSetBindAscmUserGroupLimit：资源集绑定的最大用户组个数信息。 MaxUserGroupCanJoinUserLimit：用户组加入的最大用户个数信息。 MaxUserAddResourceSetLimit：用户指定角色加入的最大资源集个数信息。 MaxUserGroupAddResourceLimit：用户组加入的最大资源集个数信息。 MaxRoleBindAscmUserLimit：用户绑定的最大角色个数信息。 MaxRoleAuthorizationBindAscmUserLimit：用户绑定的最大RAM授权类型角色个数信息。 MaxRoleBindAscmUserGroupLimit：用户组绑定的最大角色个数信息。 MaxPolicyLimit：云账号中创建的最大自定义策略个数信息。 MaxRamGroupLimit：云账号中创建的最大RAM Group个数信息。 MaxRamRoleLimit：账号中可创建的最大RAM Role个数信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /enterpriseCenter/Quotas HTTP/1.1
```

该接口无需填写请求参数。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 以List数据格式返回12项企业中心使用限制配额记录 （EnterpriseCenterQuotaEntry），具体包含以下字段： item：企业中心使用限制配额项。 current：当前该使用限制项实际最大值。 displayName：显示字段。 hasDetail：是否展示详情。 quota：该使用限制项配额。 updateTime：最近一次更新时间戳。 |
| -current | Integer | 16 | 当前该使用限制项实际最大值。 |
| -quota | Integer | 10000 | 该使用限制项配额。 |
| -displayName | String | 资源集绑定的最大用户个数 | 显示字段。 |
| -hasDetail | Boolean | true | 是否展示详情。 |
| -item | String | MaxResourceSetBindAscmUserLi mit | 企业中心使用限制配额项。 |
| -updateTime | Long | 1701932609000 | 最近一次更新时间戳。 |
| code | String | 200 | 状态响应码。 |
| cost | Integer | 150 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```
GET /enterpriseCenter/Quotas HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 131, "data": [ { "hasDetail": true, "current": 16, "item": "MaxResourceSetBindAscmUserLimit", "displayName": "资源集绑定的最大用户个数", "quota": 10000, "updateTime": 1701932609000 }, { "hasDetail": true, "current": 1, "item": "MaxResourceSetBindAscmUserGroupLimit", "displayName": "资源集绑定的最大用户组个数", "quota": 500, "updateTime": 1701932609000 }, { "hasDetail": false, "current": 55, "item": "MaxLevelOneOrganizationLimit", "displayName": "创建的一级组织个数", "quota": 1000, "updateTime": 1701932609000 }, { "hasDetail": true, "current": 2, "item": "MaxUserGroupCanJoinUserLimit", "displayName": "用户组加入的最大用户个数", "quota": 300, |  |

```json
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 1,
            "item": "MaxUserAddUserGroupLimit",
```

`"displayName": "`用户加入的最大用户组个数`",`

```json
            "quota": 30,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 3,
            "item": "MaxUserAddResourceSetLimit",
```

`"displayName": "`用户指定角色加入的最大资源集个数`",`

```json
            "quota": 100,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 1,
            "item": "MaxUserGroupAddResourceLimit",
```

`"displayName": "`用户组加入的最大资源集个数`",`

```json
            "quota": 30,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 8,
            "item": "MaxRoleBindAscmUserLimit",
```

`"displayName": "`用户绑定的最大角色个数`",`

```json
            "quota": 50,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 2,
            "item": "MaxRoleAuthorizationBindAscmUserLimit",
```

`"displayName": "`用户绑定的最大`Ram`授权类型角色个数`",`

```json
            "quota": 30,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 4,
            "item": "MaxRoleBindAscmUserGroupLimit",
```

`"displayName": "`用户组绑定的最大角色个数`",`

```json
            "quota": 15,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 126,
            "item": "MaxPolicyLimit",
```

`"displayName": "`一个阿里云账号中创建的最大自定义策略个数`",`

```json
            "quota": 50000,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 7,
            "item": "MaxRamGroupLimit",
```

`"displayName": "`一个阿里云账号中创建的最大`ram group`个数`",`

```json
            "quota": 500,
            "updateTime": 1701932609000
        },
        {
            "hasDetail": true,
            "current": 214,
            "item": "MaxRamRoleLimit",
```

`"displayName": "`一个阿里云账号中可创建的最大`ram role`个数`",`

```json
            "quota": 10000,
            "updateTime": 1701932609000
        }
```

`],`

```json
    "success": true,
    "message": "success",
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>131</cost> <data> <hasDetail>true</hasDetail> <current>16</current> <item>MaxResourceSetBindAscmUserLimit</item> |  |

```xml
 <item>MaxResourceSetBindAscmUserLimit</item>
```

`<displayName>`资源集绑定的最大用户个数`</displayName>`

```xml
 <quota>10000</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>1</current>
 <item>MaxResourceSetBindAscmUserGroupLimit</item>
```

`<displayName>`资源集绑定的最大用户组个数`</displayName>`

```xml
 <quota>500</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>false</hasDetail>
 <current>55</current>
 <item>MaxLevelOneOrganizationLimit</item>
```

`<displayName>`创建的一级组织个数`</displayName>`

```xml
 <quota>1000</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>2</current>
 <item>MaxUserGroupCanJoinUserLimit</item>
```

`<displayName>`用户组加入的最大用户个数`</displayName>`

```xml
 <quota>300</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>1</current>
```

`<displayName>`用户加入的最大用户组个数`</displayName>`

```xml
 <quota>30</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>3</current>
 <item>MaxUserAddResourceSetLimit</item>
```

`<displayName>`用户指定角色加入的最大资源集个数`</displayName>`

```xml
 <quota>100</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>1</current>
 <item>MaxUserGroupAddResourceLimit</item>
```

`<displayName>`用户组加入的最大资源集个数`</displayName>`

```xml
 <quota>30</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>8</current>
 <item>MaxRoleBindAscmUserLimit</item>
```

`<displayName>`用户绑定的最大角色个数`</displayName>`

```xml
 <quota>50</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>2</current>
 <item>MaxRoleAuthorizationBindAscmUserLimit</item>
```

`<displayName>`用户绑定的最大`Ram`授权类型角色个数`</displayName>`

```xml
 <quota>30</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>4</current>
 <item>MaxRoleBindAscmUserGroupLimit</item>
```

`<displayName>`用户组绑定的最大角色个数`</displayName>`

```xml
 <quota>15</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>126</current>
 <item>MaxPolicyLimit</item>
```

`<displayName>`一个阿里云账号中创建的最大自定义策略个数`</displayName>`

```xml
 <quota>50000</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
```

/

```xml
 <current>7</current>
 <item>MaxRamGroupLimit</item>
```

`<displayName>`一个阿里云账号中创建的最大`ram group`个数`</displayName>`

```xml
 <quota>500</quota>
 <updateTime>1701932609000</updateTime>
</data> <data>
 <hasDetail>true</hasDetail>
 <current>214</current>
 <item>MaxRamRoleLimit</item>
```

`<displayName>`一个阿里云账号中可创建的最大`ram role`个数`</displayName>`

```xml
 <quota>10000</quota>
 <updateTime>1701932609000</updateTime>
</data> <success>true</success> <message>success</message>
```

ascm 2019-05-10

##### 4.1.2.7. GetEnterpriseCenterQuotaDetail

调用GetEnterpriseCenterQuotaDetail接口获取当前云平台中已超出指定企业中心使用限制配额或超出指定数量的用户、用户组、资源集或云账号详细信息。 通过调用该接口，可以查询当前云平台中已超出指定企业中心使用限制配额的用户、用户组、资源集或云账号详细信息；也可以在请求时通过指定具体数量，查询当前云平台中已超出该数量的用户、用户组、资源集或云账号详细信息，用于提前告警。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /enterpriseCenter/Quota/[type] HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| type | String | Path | 否 | MaxResourceSetBind AscmUserLimit | 企业中心使用限制配额项，包括： MaxResourceSetBindAscmUserLimit：资源集绑定的最大用户个数信息。 MaxResourceSetBindAscmUserGroupLimit：资源集绑定的最大用户组个数信息。 MaxUserGroupCanJoinUserLimit：用户组加入的最大用户个数信息。 MaxUserAddUserGroupLimit：用户加入的最大用户组个数信息。 MaxUserAddResourceSetLimit：用户指定角色加入的最大资源集个数信息。 MaxUserGroupAddResourceLimit：用户组加入的最大资源集个数信息。 MaxRoleBindAscmUserLimit：用户绑定的最大角色个数信息。 MaxRoleAuthorizationBindAscmUserLimit：用户绑定的最大 RAM授权类型角色个数信息。 MaxRoleBindAscmUserGroupLimit：用户组绑定的最大角色个数信息。 MaxPolicyLimit：云账号中创建的最大自定义策略个数信息。 MaxRamGroupLimit：云账号中创建的最大RAM Group个数信息。 MaxRamRoleLimit：账号中可创建的最大RAM Role个数信息。 |
| limit | Integer | Query | 否 | 100 | 指定数量，即返回当前云平台超过该数量的相关用户、用户组、资源集或云账号详细信息。如果不指定该参数，默认返回当前云平台超过该配额项限制的用户、用户组、资源集或云账号详细信息。 |
| currentPage | Integer | Query | 否 | 1 | 设置从返回结果的第几页开始显示查询结果。默认值为1，表示从第1页开始显示。 |
| pageSize | Integer | Query | 否 | 10 | 设置分页查询时，每页显示的记录数量。默认值为10，表示每页显示10 条记录，最大值为500。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|

| data | Array | - | 根据指定的type参数，以List数据格式返回符合查询条件的用户（UserEntry）、 用户组（UserGroupEntry）、资源集（ResoourceSetEntry）或云账号 （RamEntry）信息，详细说明参见data参数补充说明。 |
|---|---|---|---|
| -aliyunId | String | 192895059480**** | 云账号ID。 |
| -accountKp | String | 123456 | 云账号主键，作为账号的唯一标识，即云账号UID。 |
| -organizationName | String | orgTest | 所属组织名称。 |
| -count | Integer | 100 | 当前实际数量，即type参数值对应的企业中心使用限制配额项。 |
| -updateTime | Long | 1652085686179 | 最近一次更新时间戳。 |
| -id | Integer | 40617 | 根据指定的type参数，返回符合查询条件的用户ID、资源集ID或用户组ID。 |
| -rsId | String | 112*** | 资源集唯一编码。 |
| -resourceGroupName | String | restest _ | 资源集名称。 |
| -username | String | test | 用户显示名。 |
| -loginName | String | test | 用户登录名。 |
| -isActive | Boolean | true | 是否启用。 |
| -roleId | Integer | 1 | 默认角色ID。 |
| -roleName | String | defaultRole.globalResourceAudito r.name | 默认角色名称。 |
| -augId | String | 11** | 用户组唯一编码。 |
| -groupName | String | nameTest | 用户组名称。 |
| code | String | 200 | 状态响应码。 |
| cost | Integer | 17 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 返回提示信息。 |
| success | Boolean | true | 接口请求成功标识。 true：成功。 false：失败。 |
| pageInfo | Struct | - | 返回分页信息。 |
| -currentPage | Integer | 1 | 分页查询时，当前页的页码。 |
| -pageSize | Integer | 10 | 分页查询时，每页数据显示的最大条数。 |
| -total | Integer | 9629 | 分页查询时，返回的数据总条数。 |
| -totalPage | Integer | 936 | 分页查询时，返回总页数。 |

**示例**

请求示例

```
GET /enterpriseCenter/Quota/[type] HTTP/1.1
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":17,
 "data":[
  {
   "roleId":1,
   "count":100,
   "updateTime":1652085686179,
   "isActive":true,
   "loginName":"test",
   "roleName":"defaultRole.globalResourceAuditor.name",
   "id":40617,
   "username":"test"
  }
```

`],`

```json
 "success":true,
 "pageInfo":{
  "total":9629,
  "totalPage":936,
  "pageSize":10,
  "currentPage":1
 },
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>17</cost> <data> <resourceGroupName>res_test</resourceGroupName> <augId>11**</augId> <organizationName>orgTest</organizationName> <roleId>1</roleId> <count>100</count> <rsId>112***</rsId> <updateTime>1652085686179</updateTime> <accountKp>123456</accountKp> <isActive>true</isActive> <aliyunId>192895059480****</aliyunId> <groupName>nameTest</groupName> <loginName>test</loginName> <roleName>defaultRole.globalResourceAuditor.name</roleName> <id>40617</id> <username>test</username> </data> <success>true</success> <pageInfo> <total>9629</total> <totalPage>936</totalPage> <pageSize>10</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

**文档补充说明**

**data参数补充说明**

当type参数值为MaxUserAddUserGroupLimit、MaxUserAddResourceSetLimit、MaxRoleBindAscmUserLimit或MaxRoleAuthorizationBindAscmUserLimit 时，返回用户（UserEntry）类型详细信息，具体包含字段：id（用户ID）、username（用户显示名）、loginName（用户登录名）、isActive（是否启用）、 roleId（默认角色ID）、roleName（默认角色名称）、count（当前实际数量，即type参数值对应的企业中心使用限制配额项）、updateTime（最近一次更新时间戳）。 当type参数值为MaxUserGroupCanJoinUserLimit、MaxUserGroupAddResourceLimit或MaxRoleBindAscmUserGroupLimit时，返回用户组 （UserGroupEntry）类型详细信息，具体包含字段：id（用户组ID）、augId（用户组唯一编码）、groupName（用户组名称）、organizationName（所属组织名称）、count（当前实际数量，即type参数值对应的企业中心使用限制配额项）、updateTime（最近一次更新时间戳）。 当type参数值为MaxResourceSetBindAscmUserLimit或MaxResourceSetBindAscmUserGroupLimit时，返回资源集（ResourceSetEntry）类型详细信息，具体包含字段：id（资源集ID）、rsId（资源集唯一编码）、resourceGroupName（资源集名称）、organizationName（所属组织名称）、count（当前实际数量，即 type参数值对应的企业中心使用限制配额项）、updateTime（最近一次更新时间戳）。 当type参数值为MaxPolicyLimit、MaxRamGroupLimit或MaxRamRoleLimit时，返回云账号（RamEntry）类型详细信息，具体包含字段：aliyunId（云账号ID）、 accountKp（云账号主键）、organizationName（所属组织名称）、count（当前实际数量，即type参数值对应的企业中心使用限制配额项）、updateTime（最近一次更新时间戳）。 ascm 2019-05-10

##### 4.1.2.8. GetQuota

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/quota/query HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| quotaType | String | Body | 否 | organization | 配额类型。 |
| quotaTypeId | Integer | Body | 否 | 3 | 配额类型ID。 |
| productName | String | Body | 否 | RDS | 产品名称。 |
| regionName | String | Body | 否 | regionName | 区域名称。 |
| clusterName | String | Body | 否 | clusterName | 集群名称。 |
| targetType | String | Body | 否 | MySQL | 目标类型。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| data | Struct |  | 响应数据。 |
| allocateAmount | Integer | 1 | 已分配。 |
| allocateCpu | Integer | 1 | 分配CPU。 |
| allocateCu | Integer | 1 | 分配CU。 |
| allocateDisk | Integer | 100 | 分配磁盘量。 |
| allocateDiskcloudefficie _ _ ncy | Integer | 100 | 分配高效盘量。 |
| allocateDiskcloudssd _ _ | Integer | 100 | 分配SSD盘量 |
| allocateGpu | Integer | 100 | 分配GPU。 |
| allocateHAVIP | Integer | 5 | 分配高可用IP量。 |
| allocateMQ | Integer | 5 | 分配MQ。 |
| allocateMem | Integer | 100 | 分配内存。 |
| allocateVPC | Integer | 1 | 分配VPC。 |
| allocateVipInternal | Integer | 1 | 分配的内部VIP。 |
| allocateVipPublic | Integer | 1 | 分配的公共VIP。 |
| cluster | String | cn-qingdao-env17-d01 | 集群。 |
| ctime | Float | 1608519825999 | 创建时间。 |
| cuserId | String | admin | 创建者。 |
| dtFlag | Boolean | false | DT标识。 |
| id | Integer | 1 | 识别主键。 |

| muserId | String | admin | 修改者。 |
|---|---|---|---|
| quotaType | String | organization | 配额类型。 |
| quotaTypeId | Integer | 1 | 配额ID。 |
| region | String | cn-qingdao-env17-d01 | 地域。 |
| targetType | String | mysql | 集群类别。 |
| totalAmount | Integer | 10 | 配额总数。 |
| totalCpu | Integer | 1 | 总CPU。 |
| totalCu | Integer | 1 | 总CU。 |
| totalDisk | Integer | 100 | 总磁盘。 |
| totalDiskcloudefficiency _ _ | Integer | 100 | 总高效云盘量。 |
| totalDiskcloudssd _ _ | Integer | 100 | 总SSD磁盘量。 |
| totalGpu | Integer | 100 | 总GPU。 |
| totalHAVIP | Integer | 1 | 总高可用VIP量。 |
| totalMQ | Integer | 1 | 总MQ。 |
| totalMem | Integer | 100 | 总内存量。 |
| totalVPC | Integer | 1 | 总VPC量。 |
| totalVipInternal | Integer | 1 | 总内部VIP量。 |
| totalVipPublic | Integer | 1 | 总共有VIP量 |
| usedAmount | Integer | 1 | 已使用配额。 |
| usedCpu | Integer | 1 | 已使用CPu量。 |
| usedCu | Integer | 1 | 已使用CU量。 |
| usedDisk | Integer | 100 | 已使用磁盘量。 |
| usedDiskcloudefficiency _ _ | Integer | 100 | 已使用高效磁盘量。 |
| usedDiskcloudssd _ _ | Integer | 100 | 已使用SSD盘量。 |
| usedGpu | Integer | 1 | 已使用GPU量。 |
| usedHAVIP | Integer | 1 | 已使用高可用VIP量。 |
| usedMQ | Integer | 1 | 已使用MQ量。 |
| usedMem | Integer | 100 | 已使用内存。 |
| usedVPC | Integer | 1 | 已使用VPC。 |
| usedVipInternal | Integer | 1 | 已使用内部VIp。 |
| usedVipPublic | Integer | 1 | 已使用共有VIP。 |

| message | String | 200 | 提示信息。 |
|---|---|---|---|
| pureListData | Boolean | false | 是否只返回数据。 |
| redirect | Boolean | false | 是否重定向。 |
| requestId | String | 111 | 请求ID。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
&ProductName=ECS &QuotaType=organization &QuotaTypeId=1
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <usedVipInternal>1</usedVipInternal> <allocateDisk_cloud_ssd>100</allocateDisk_cloud_ssd> <muserId>admin</muserId> <cluster>cn-qingdao-env17-d01</cluster> <allocateVipPublic>1</allocateVipPublic> <totalVipInternal>1</totalVipInternal> <usedAmount>1</usedAmount> <allocateAmount>1</allocateAmount> <totalDisk_cloud_efficiency>100</totalDisk_cloud_efficiency> <usedMQ>1</usedMQ> <allocateCu>1</allocateCu> <totalDisk>100</totalDisk> <totalVPC>1</totalVPC> <usedDisk_cloud_ssd>100</usedDisk_cloud_ssd> <totalDisk_cloud_ssd>100</totalDisk_cloud_ssd> <totalCpu>1</totalCpu> <usedVPC>1</usedVPC> <ctime>1608519825999</ctime> <totalCu>1</totalCu> <usedGpu>1</usedGpu> <id>1</id> <allocateMem>100</allocateMem> <cuserId>admin</cuserId> <allocateDisk_cloud_efficiency>100</allocateDisk_cloud_efficiency> <allocateDisk>100</allocateDisk> <usedCpu>1</usedCpu> <totalGpu>100</totalGpu> <allocateMQ>5</allocateMQ> <totalVipPublic>1</totalVipPublic> <quotaTypeId>1</quotaTypeId> <totalMQ>1</totalMQ> <usedCu>1</usedCu> <usedVipPublic>1</usedVipPublic> <totalMem>100</totalMem> <allocateVipInternal>1</allocateVipInternal> <allocateVPC>1</allocateVPC> <allocateGpu>100</allocateGpu> <targetType>mysql</targetType> <usedDisk>100</usedDisk> <usedMem>100</usedMem> <allocateCpu>1</allocateCpu> <usedDisk_cloud_efficiency>100</usedDisk_cloud_efficiency> <totalAmount>10</totalAmount> <quotaType>organization</quotaType> <allocateHAVIP>5</allocateHAVIP> <dtFlag>false</dtFlag> <totalHAVIP>1</totalHAVIP> <usedHAVIP>1</usedHAVIP> <region>cn-qingdao-env17-d01</region> </data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |  |

`JSON` 格式

```json
{"redirect":"false","cost":"1000","code":"200","data":{"usedVipInternal":"1","allocateDisk_cloud_ssd":"100","muserId":"admin","cluster":"cn-qi ngdao-env17d01","allocateVipPublic":"1","totalVipInternal":"1","usedAmount":"1","allocateAmount":"1","totalDisk_cloud_efficiency":"100","usedMQ":"1","alloca ":"1","totalDisk":"100","totalVPC":"1","usedDisk_cloud_ssd":"100","totalDisk_cloud_ssd":"100","totalCpu":"1","usedVPC":"1","ctime":"160851982599 otalCu":"1","usedGpu":"1","id":"1","allocateMem":"100","cuserId":"admin","allocateDisk_cloud_efficiency":"100","allocateDisk":"100","usedCpu":"1 talGpu":"100","allocateMQ":"5","totalVipPublic":"1","quotaTypeId":"1","totalMQ":"1","usedCu":"1","usedVipPublic":"1","totalMem":"100","allocateVi ernal":"1","allocateVPC":"1","allocateGpu":"100","targetType":"mysql","usedDisk":"100","usedMem":"100","allocateCpu":"1","usedDisk_cloud_efficien "100","totalAmount":"10","quotaType":"organization","allocateHAVIP":"5","dtFlag":"false","totalHAVIP":"1","usedHAVIP":"1","region":"cnqingdao-env17-d01"},"success":"true","requestId":"111","pureListData":"false","message":"200"}
```

##### 4.1.2.9. MeteringQuery

分页查询某个产品在一段时间内的计量数据。 请使用个人（管理平台右上角个人中心页面）的AccessKey ID和AccessKey Secret进行调用，不支持用组织的AccessKey ID和AccessKey Secret，另外需要在请求 Header中增加x-acs-roleId，value为要使用的角色Id，如果不传，则会使用用户的默认角色进行查询。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/metering/ots/query HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| productName | String | Body | 否 | ECS | 产品名称，该参数必选。 ECS： 云服务器 ECS VPC： 专有网络 VPC SLB： 负载均衡 SLB OSS： 对象存储 OSS RDS： 云数据库 RDS MySQL EIP： 弹性公网 IP NAS： 文件存储 NAS OTS： 表格存储 TableStore DRDS： 云原生分布式数据库 PolarDB-X REDIS： 云数据库 Redis ADB： 云原生数据仓库 AnalyticDB MySQL 版3.0 GPDB： 云原生数据仓库AnalyticDB PostgreSQL版 DDS： 云数据库 MongoDB ONS： 消息队列 MQ RDS _POSTGRESQL： 云数据库 RDS PostgreSQL RDS _SQLSERVER： 云数据库 RDS SQLServer SLS： 日志服务 SLS EBS： ECS磁盘 EBS SNAPSHOT： ECS快照 SNAPSHOT ESS： 伸缩组规则 HBASE： 云数据库 HBase CLOUDAPI： API网关 KMS： 密钥管理服务 ADS： 云原生数据仓库AnalyticDB MySQL 版2.0 TSDB： 云数据库 TSDB DDH： 专有宿主机 DDH OCEANBASE： 云数据库 OceanBase VPN： VPN网关 IPV6： IPv6网关 NAT： NAT网关 DATAHUB： 数据总线 DataHub GDB： 图数据库 GDB ExpressConnect： 高速通道 ACK： 容器服务 Kubernetes ODPS： 大数据计算 MaxCompute CR： 容器镜像服务 CR BLINK： 实时计算 Realtime Compute BastionHost： 老版堡垒机 BastionHostSfd： 云原生堡垒机 YundunCcfw： 云防火墙-CCFW YundunIcfw： 云防火墙-ICFW YundunAliguard： DDoS清洗 YundunBeaver： 流量安全监控 Semawaf： Web应用防火墙 DedicatedSAS： 态势感知 DbAuditAhjh： 数据库审计 Aegis： 安骑士 DMS： 数据管理 DMS CSB： 云服务总线 CSB EDASINSTANCES： 企业级分布式应用服务 EDAS ELASTICSEARCHK8S： Elasticsearch on k8s Hologres： 交互式分析 Hologres HAVIP： 高可用虚拟IP KMS _CRYPTO： 密码服务 Gws：无影云桌面Gws BMS：裸机管理BMS EHPC：弹性高性能计算E-HPC DATAV：数据可视化DataV PAI _DSW：交互式建模PAI _DSW PAI _DLC：云原生深度学习训练PAI _DLC PAI _EAS：模型在线服务PAI _EAS |
| startTime | String | Body | 否 | 2022-01-01T16:00:00Z | 开始时间，UTC时间格式，该参数必选。 |
| endTime | String | Body | 否 | 2022-01-01T16:00:00Z | 结束时间，UTC时间格式，该参数必选。 说明计量时间段最小间隔为1小时，间隔设置少于1小时则无返回结果。 |

| 统一云管平台 |  |  |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| orgId | String | Body | 否 | 3 | 组织ID，该参数必选。可通过调用 GetOrganizationList接口获取。 |
| resourceGId | String | Body | 否 | 21 | 资源集ID。 |
| region | String | Body | 否 | cn-wulan-env180-d01 | 区域。非特殊情况，不建议使用此参数进行频繁查询 |
| insId | String | Body | 否 | i-nn901czk0tkyclwffvcp | 实例ID。非特殊情况，不建议使用此参数进行频繁查询 |
| pageSize | Integer | Body | 否 | 50 | 分页大小，默认20，最大1000。 |
| token | String | Body | 否 | {"InsId":"i- nn901lg2uex9kk3gt9o3","Pos":"ECS0000 _ 0000032022-11- _ 01T01:00:00Z","ResourceGId":"2415","Re gionId":"cn-wulan-env180-d01"} | 分页查询使用的token。如果查询的结果超出 pageSize，则会返回一个token，输入该值查看下一页内容。 |
| isParentId | Integer | Body | 否 | 1 | 是否查询指定组织下的所有子组织的计量数据， 默认0。 0： 只查指定组织，不查子组织数据。 1： 查询指定组织以及子组织的数据。 说明该参数为必填。 |
| isFullResult | Integer | Body | 否 | 1 | 是否查询所有计量字段，默认0。 0： 只返回默认的必要展示字段。 1： 返回所有的计量字段。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array |  | 计量数据。 |
| -Pos | String | ECS00000000032022-11- _ _ 01T00:00:00Z | 数据的OTS主键，由产品、组织ID和开始时间组成。 |
| -OrgName | String | astbbigdata | 组织名称。 |
| -ResourceGId | Integer | 2 | 资源集ID。 |
| -ResourceGName | String | ResourceSet(astbbigdata) | 资源集名称。 |
| -InsId | String | i-nn901gtz4gd1mfrpfvvt | 实例ID。 |
| -RegionId | String | cn-wulan-env136-d01 | 区域。 |
| -StartTime | String | 2022-11-01T00:00:00Z | 开始时间。 |
| -EndTime | String | 2022-11-01T01:00:00Z | 结束时间。 |
| -CreateTime | String | 2022-09-21T05:38:00Z | 创建时间。 |
| code | String | 200 | 返回码。 200: 正常。 400: 无权限或参数错误。 500: 服务内部错误。 |
| cost | Integer | 29 | 耗时，单位毫秒。 |
| message | String | success | 返回信息。 |
| requestId | String | 0ab4142316690259582686866d 004a | 该返回字段已废弃。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 调接口是否成功。 |
| token | String | {"InsId":"i- nn901lg2uex9kk3gt9o3","Pos":"E CS00000000032022-11- _ _ 01T01:00:00Z","ResourceGId":"2 415","RegionId":"cn-wulan- env180-d01"} | 分页查询使用的token，下次查询时必填。 |
| total | Integer | 15 | 本次返回的数据数量。 |

**示例**

请求示例

```
POST /ascm/metering/ots/query HTTP/1.1
```

公共请求头正常返回示例

| JSON | 格式 |
|---|---|
| { "total":15, "code":"200", "cost":29, "data":{ "InsId":"i-nn901gtz4gd1mfrpfvvt", "EndTime":"2022-11-01T01:00:00Z", "Pos":"ECS_0000000003_2022-11-01T00:00:00Z", "CreateTime":"2022-09-21T05:38:00Z", "StartTime":"2022-11-01T00:00:00Z", "OrgName":"astbbigdata", "ResourceGId":2, "ResourceGName":"ResourceSet(astbbigdata)", "RegionId":"cn-wulan-env136-d01" }, "requestId":"0ab4142316690259582686866d004a", "success":true, "message":"success", "token":"{\"InsId\":\"i-nn901lg2uex9kk3gt9o3\",\"Pos\":\"ECS_0000000003_2022-11-01T01:00:00Z\",\"ResourceGId\":\"2415\",\"RegionId\":\"cn-wul an-env180-d01\"}" } |  |

##### 4.1.2.10. SelectCommonSpec

按条件查询产品规格信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/saleconf/commonSpec/select HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| Action | String | Query | 是 | SelectCommonSpec | 系统规定参数。取值：SelectCommonSpec。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 数据集。 |
| result | Array of dataItem |  | 结果集合。 |
| dataItem |  |  |  |
| baseVersion | String | 3.13 | 规格版本。 |
| gmtCreate | String | 2019-10-27 17:47:27 | 规格创建时间。 |
| gmtModified | String | 2019-10-27 17:47:27 | 规格修改时间。 |

| pageOrder | String | 1 | 页面顺序。 |
|---|---|---|---|
| pageSize | Integer | 5 | 单页面展示数量。 |
| pageSort | String | null | 页面排序。 |
| pageStart | Integer | 1 | 查询第几页，从1开始计算。 |
| regionId | String | cn-qingdao-env66-d01 | 区域。 |
| resourceType | String | RDS | 资源类型。 |
| specFrom | String | system | 规格来源。 |
| status | String | Available | 规格是否可用。 |
| status | Integer | 200 | 返回状态。 |
| success | String | true | 成功标示。 |
| host | String | "" | host地址。 |
| status | Integer | 200 | 返回状态。 |

**示例**

请求示例 `&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <data> <result> <gmtModified>2019-10-27 17:47:27</gmtModified> <pageOrder>1</pageOrder> <pageSort>null</pageSort> <regionId>cn-qingdao-env66-d01</regionId> <baseVersion>3.13</baseVersion> <pageStart>1</pageStart> <pageSize>5</pageSize> <specFrom>system</specFrom> <gmtCreate>2019-10-27 17:47:27</gmtCreate> <status>Available</status> <resourceType>RDS</resourceType> </result> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |  |

`JSON` 格式

```json
{
    "data": {
        "result": [
            {
                "gmtModified": "2019-10-27 17:47:27",
                "pageOrder": "1",
                "pageSort": "null",
                "regionId": "cn-qingdao-env66-d01",
                "baseVersion": "3.13",
                "pageStart": "1",
                "pageSize": "5",
                "specFrom": "system",
                "gmtCreate": "2019-10-27 17:47:27",
                "status": "Available",
                "resourceType": "RDS"
            }
```

`],`

```json
        "success": "true",
        "status": "200"
    },
    "host": "\"\"",
    "status": "200"
}
```

##### 4.1.2.11. UpdateCommonSpecStatus

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateCommonSpecStatus | 系统规定参数。取值：UpdateCommonSpecStatus。 |
| ids | String | 是 | 1 | 规格ID。 |
| status | String | 是 | Unavailable | 取值为Available或者Unavailable。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| data | Integer | 200 | 数据集合。 |
| message | String | success | 提示信息。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=UpdateCommonSpecStatus &ids=1 &status=Unavailable
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <data>200</data> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "data": "200", "success": "true", "message": "success" } |  |

##### 4.1.2.12. UpdateQuota

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | UpdateQuota | 系统规定参数。取值：UpdateQuota。 |
| ProductName | String | 是 | ECS | 产品名称：ECS 、OSS、VPC、RDS、SLB、ODPS、EIP。 |
| QuotaBody | Json | 是 | {"totalCpu":100,"totalMem": 100,"totalGpu":100, "totalDiskcloudssd":100,"to _ _ talDiskcloudefficiency":100 _ _ } | 具体的Quota参数： ECS: {"totalCpu":100,"totalMem":100,"totalGpu":100,"total Disk_cloud_ssd":100,"totalDisk_cloud_efficiency":100 } OSS: {"totalAmount":100} VPC: {"totalVPC":100} RDS: {"totalCpu":100,"totalMem":100,"totalDisk":100} SLB: {"totalVipInternal":100,"totalVipPublic":100} ODPS: {"totalCu":100,"totalDisk":100} EIP: {"totalEIP":100} |
| QuotaType | String | 是 | organization | 如果给组织创建配额，则输入organization，如果给资源集创建配额，则输入resourceGroup。 |
| QuotaTypeId | Integer | 是 | 1 | 如果为组织设置配额，则输入组织ID；如果为资源集设置配额，则输入资源集ID。 |
| RegionName | String | 是 | cn-*******-****-d01 | Region名称。 |
| RequestId | String | 否 | 84319b92-835e-4aeb-9190- 0c12c9****** | 请求ID。 |
| ClusterName | String | 否 | TEST | 预留字段，集群名称，可不填写或者传空字符串。 |
| TargetType | String | 否 | MySQL | 如果为RDS产品则输入对应引擎的名称，本版本支持MySQL和 SQLServer。对于其他产品则可不填或者传空字符串。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 1000 | 耗时时间。 |
| data | Struct |  | 响应数据。 |
| allocateVPC | Integer | 1 | 已分配（VPC）。 |
| cluster | String | cn-qingdao-env17-d01 | 集群。 |
| ctime | Float | 1608519825999 | 创建时间。 |
| dtFlag | Boolean | false | DT标识。 |
| id | Integer | 1 | 识别主键。 |
| quotaType | String | organization | 配额类型。 |
| quotaTypeId | Integer | 1 | 配额ID。 |
| region | String | cn-qingdao-env17-d01 | 地域。 |

| targetType | String | mysql | 集群类别。 |
|---|---|---|---|
| totalVPC | Integer | 10 | 配额总数（VPC）。 |
| usedVPC | Integer | 1 | 已使用配额（VPC）。 |
| message | String | 200 | 提示信息。 |
| pureListData | Boolean | false | 是否只返回数据。 |
| redirect | Boolean | false | 是否重定向。 |
| requestId | String | 111 | 请求ID。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
&ProductName=ECS &QuotaBody={"totalCpu":100,"totalMem":100,"totalGpu":100, "totalDisk_cloud_ssd":100,"totalDisk_cloud_efficiency":100} &QuotaType=organization &QuotaTypeId=1
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <data> <quotaType>organization</quotaType> <cluster>cn-qingdao-env17-d01</cluster> <totalVPC>10</totalVPC> <dtFlag>false</dtFlag> <quotaTypeId>1</quotaTypeId> <usedVPC>1</usedVPC> <ctime>1608519825999</ctime> <allocateVPC>1</allocateVPC> <targetType>mysql</targetType> <id>1</id> <region>cn-qingdao-env17-d01</region> </data> <success>true</success> <requestId>111</requestId> <pureListData>false</pureListData> <message>200</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": "false", "cost": "1000", "code": "200", "data": { "quotaType": "organization", "cluster": "cn-qingdao-env17-d01", "totalVPC": "10", "dtFlag": "false", "quotaTypeId": "1", "usedVPC": "1", "ctime": "1608519825999", "allocateVPC": "1", "targetType": "mysql", "id": "1", "region": "cn-qingdao-env17-d01" }, "success": "true", "requestId": "111", "pureListData": "false", "message": "200" } |  |

##### 4.1.2.13. AscmExternalFlowCallBack

三方流程审批结束后，调用AscmExternalFlowCallBack接口将审批结果、审批意见通知给ASCM流程。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | 0a1128a916917198245846573e 002a | 请求链路ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 |
| message | String | "success" | 提示信息。 |
| data | Boolean | true | 响应结果：流程回调是否成功。 |

**示例**

请求示例

```json
POST /ascm/process/instance/externalFlow/trigger HTTP/1.1 {
  "callbackParams" : {
    "executionId" : "9647a5eafc9111ef84a502420a881454",
    "processInstanceId" : "91fb8f88fc8f11efaa2902420a881454",
    "verification" : "Item_404eaa38-710a-408e-aaa4-6b4c7da4b407"
  },
  "approveResult" : true,
```

`"approveComment" : "`审批意见"

```
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"0a1128a916917198245846573e002a", "success":true, "message":"\"success\"" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>0a1128a916917198245846573e002a</requestId> <success>true</success> <message>&quot;success&quot;</message> |  |

##### 4.1.2.14. BillQuery

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/billing/web/query/public HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cycleType | String | Body | 是 | Daily | 账单周期类型，支持按天维度（Daily）。该参数为必填参数。 |
| groupByType | String | Body | 是 | instance | 账单聚合类型，支持按实例(instance：)聚合。 该参数为必填参数。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| orgId | String | Body | 否 | 3 | 账单所属组织的ID。 |
| resourceSetId | String | Body | 否 | 2 | 账单所属资源集的ID。 |
| pageSize | Integer | Body | 否 | 10 | 设置分页查询时，每页显示的记录数量。默认值为10，表示每页显示10条记录；最大值为 100。 |
| billingCycle | String | Body | 是 | 2023-07 | 账期，格式为YYYY-MM。当账单周期类型 （cycleType）为Monthly时，该参数为必填。 |
| productName | String | Body | 否 | ECS | 账单所属产品名称。 |
| startTime | String | Body | 否 | 2023-06-30T16:00:00Z | 账单开始时间。 |
| endTime | String | Body | 否 | 2023-07-31T15:00:00Z | 账单结束时间。 |
| region | String | Body | 否 | cn-qingdao-***-d01 | 账单所属区域。 |
| token | String | Body | 否 | {"InsId":"i- f9m05tzk3wtss0y8****","Pos":"Hourly- instanceECS00000000032023-07- _ _ _ 21T09:00:00Z","ResourceGId":"2","Region Id":"cn-qingdao-***-d01"} | 指定查询开始的位置。具体设置方法需了解OTS 查询方法。当要查询的账单存储在OTS数据库时，该参数有效。 |
| isParentId | Integer | Body | 否 | 0 | 是否查询子组织账单。默认值为0，即默认不查询子组织。 0：否 1：是 |
| insId | String | Body | 否 | i-f9m05j7zfc7b3mhux*** | 账单所属实例的ID，用于过滤指定实例的账单。 |
| pageNumber | Integer | Body | 否 | 10 | 页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 账单信息。 |
| -instanceSpec | List | ecs.xn4.small | 实例规格。 |
| -cloudType | String | cloud- 15190b1df8c742e1bd16c1ee695f d26f | 该参数已弃用，由platformCode参数取代。 |
| -currency | String | CNY | 账单金额单位，如CNY。 |
| -cycleType | String | Hourly | 账单周期类型。 |
| -groupByType | String | instance | 账单聚合类型。 |
| -regionId | String | cn-qingdao-***-d01 | 账单所属区域。 |
| -insId | String | i-f9m05j7zfc7b3mhu**** | 账单所属实例的ID。 |
| -orgId | String | 3 | 账单所属组织的ID。 |
| -orgName | String | dtstest _ | 账单所属组织的名称。 |
| -resourceGid | String | 2 | 账单所属资源集的ID。 |
| -resourceGroupName | String | ResourceSet(dtstest) _ | 账单所属资源集的名称。 |
| -product | String | ECS | 账单所属产品。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -startTime | String | 2023-07-21T03:00:00Z | 计费开始时间。 |
| -endTime | String | 2023-07-21T04:00:00Z | 计费结束时间。 |
| -price | Float | 0.3 | 账单实际费用。 |
| -discountPrice | Float | 0.1 | 账单优惠费用。 |
| -originalPrice | Float | 0.4 | 账单原始费用。 |
| -reliefPrice | Float | 0 | 减免金额。 |
| -relievedPrice | Float | 0 | 已减免金额。 |
| -roundingAmount | Float | 0 | 抹零金额。 |
| -billingChan | String | 66-36-1-1 | 计费模型ID链信息，包括：计费项1-计费项2-计费项规则ID-计费策略ID-计费计划 ID。 |
| -billingTime | String | 2023-07-21T21:00:03Z | 记账时间。 |
| -modifiedBy | String | 4 | 修改人用户ID。 |
| -modifiedTime | String | 2023-07-21T21:00:03Z | 修改时间。 |
| -mergeCount | Integer | 0 | 聚合次数。如果账单信息经过聚合，返回聚合的次数。 |
| -billCycle | String | 2023-07 | 账期。 |
| -payType | String | postPay | 计费类型： monthlyPay：按月收费。 postPay：按量计费。 |
| -instanceSpecDetail | Map | { "ecs.n4.xlarge": [ { "featureValue": "0", "featureName": "GPU数量", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. gpuAmount", "needTrans": false }, { "featureValue": "8.0", "featureName": "内存(GB)", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. memorySize", "needTrans": false }, { "featureValue": "cloud _sperf", "featureName": "磁盘类型", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. systemDisk", "needTrans": false }, { "featureValue": "4", "featureName": "vCPU内核数目", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. cpuCoreCount", "needTrans": false }, { "featureValue": "", "featureName": "GPU类型", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. gpuSpec", "needTrans": false } ] } | 实例规格属性详情。 |
| -instanceTag | Map | { "EnableHotUpgrade": [ "true" ] } | 实例标签。 |
| -platformCode | String | default | 实例所属云平台。 |
| -identifier | String | ecs | 实例所属云产品。 |
| -identifierGroup | String | GRP001 | 实例所属云产品分组。 |
| -financialUnitId | String | 10001 | 实例所属财务单元ID。 |
| -financialName | String | TEST01 | 实例所示财务单元名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -paySubType | String | NEW | 账单子类型。 |
| -orderId | String | 2023111716053700**** | 账单关联订单ID。 |
| -extraInfo | Map | { "allocatedQuantity":"50GB" } | 额外信息。 |
| code | String | 200 | 状态响应码。 |
| cost | Integer | 112 | 接口响应耗时，单位毫秒（ms）。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识。 |
| errorCode | String | 403 | 返回错误码。 |
| errorMessage | String | no permission | 返回错误信息。 |
| token | String | {"InsId":"i- f9m05tzk3wtss0y8****","Pos":"Ho urly- instanceECS00000000032023- _ _ _ 07- 21T09:00:00Z","ResourceGId":"2" ,"RegionId":"cn-qingdao-***- d01"} | 当查询的账单存储在MySQL数据库时，该参数值为null。 当查询的账单存储在OTS数据库时，该参数记录查询到的最后一条账单的后一条账单所对应的OTS Token值。 |
| pageSize | Integer | 20 | 每页显示的记录数量。 |
| pageNumber | Integer | 10 | 页码。 |

**示例**

请求示例

```json
POST /ascm/billing/billing/web/query/public HTTP/1.1 { "cycleType":"Daily", "groupByType":"instance", "billingCycle":"2023-07" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":112, "pageNumber":10, "data":[ { "resourceGid":"2", "roundingAmount":0.0, "modifiedTime":"2023-07-21T21:00:03Z", "relievedPrice":0.0, "originalPrice":0.4, "paySubType":"NEW", "financialName":"TEST01", "orderId":"2023111716053700****", "discountPrice":0.1, "orgId":"3", "insId":"i-f9m05j7zfc7b3mhu****", "payType":"postPay", "financialUnitId":"10001", "billingChan":"66-36-1-1", "identifierGroup":"GRP001", "cloudType":"cloud-15190b1df8c742e1bd16c1ee695fd26f", "price":0.3, "instanceSpecDetail":{ "ecs.n4.xlarge":[ { "featureValue":"0", "featureName":"GPU数量", "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.gpuAmount", "needTrans":false }, { |  |

```json
      "featureValue":"8.0",
      "featureName":"内存(GB)",
      "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.memorySize",
      "needTrans":false
     },
     {
      "featureValue":"cloud_sperf",
```

`"featureName":"`磁盘类型`",`

```json
      "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.systemDisk",
      "needTrans":false
     },
     {
      "featureValue":"4",
```

`"featureName":"vCPU`内核数目`",`

```json
      "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.cpuCoreCount",
      "needTrans":false
     },
     {
      "featureValue":"",
      "featureName":"GPU类型",
      "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.gpuSpec",
      "needTrans":false
     }
```

]

```json
   },
   "currency":"CNY",
   "startTime":"2023-07-21T03:00:00Z",
   "modifiedBy":"4",
   "mergeCount":0,
   "identifier":"ecs",
   "product":"ECS",
   "orgName":"dts_test",
   "resourceGroupName":"ResourceSet(dts_test)",
   "groupByType":"instance",
   "billingTime":"2023-07-21T21:00:03Z",
   "cycleType":"Hourly",
   "instanceTag":{
    "EnableHotUpgrade":[
     "true"
```

]

```json
   },
   "reliefPrice":0.0,
   "regionId":"cn-qingdao-***-d01",
   "instanceSpec":"ecs.xn4.small",
   "endTime":"2023-07-21T04:00:00Z",
   "billCycle":"2023-07",
   "platformCode":"default",
   "extraInfo":{
    "allocatedQuantity":"50GB"
   }
  }
```

`],`

```json
 "requestId":"0a1128a916917198245846573e****",
 "success":true,
 "errorMessage":"no permission",
 "errorCode":"403",
 "pageSize":20,
 "token":"{\"InsId\":\"i-f9m05tzk3wtss0y8****\",\"Pos\":\"Hourly-instance_ECS_0000000003_2023-07-
21T09:00:00Z\",\"ResourceGId\":\"2\",\"RegionId\":\"cn-qingdao-***-d01\"}" }
```

`XML` 格式

```xml
<code>200</code> <cost>112</cost> <pageNumber>10</pageNumber> <data>
 <resourceGid>2</resourceGid>
 <roundingAmount>0</roundingAmount>
 <modifiedTime>2023-07-21T21:00:03Z</modifiedTime>
 <relievedPrice>0</relievedPrice>
 <originalPrice>0.4</originalPrice>
 <paySubType>NEW</paySubType>
 <financialName>TEST01</financialName>
 <orderId>2023111716053700****</orderId>
 <discountPrice>0.1</discountPrice>
 <orgId>3</orgId>
 <insId>i-f9m05j7zfc7b3mhu****</insId>
 <payType>postPay</payType>
 <financialUnitId>10001</financialUnitId>
 <billingChan>66-36-1-1</billingChan>
 <identifierGroup>GRP001</identifierGroup>
 <cloudType>cloud-15190b1df8c742e1bd16c1ee695fd26f</cloudType>
 <price>0.3</price>
 <instanceSpecDetail>
  <ecs.n4.xlarge>
   <featureValue>0</featureValue>
   <featureName>GPU数量</featureName>
   <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.gpuAmount</nameTransKey>
   <needTrans>false</needTrans>
  </ecs.n4.xlarge>
  <ecs.n4.xlarge>
   <featureValue>8.0</featureValue>
   <featureName>内存(GB)</featureName>
   <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.memorySize</nameTransKey>
   <needTrans>false</needTrans>
  </ecs.n4.xlarge>
  <ecs.n4.xlarge>
   <featureValue>cloud_sperf</featureValue>
   <featureName>磁盘类型</featureName>
   <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.systemDisk</nameTransKey>
   <needTrans>false</needTrans>
  </ecs.n4.xlarge>
  <ecs.n4.xlarge>
   <featureValue>4</featureValue>
   <featureName>vCPU内核数目</featureName>
   <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.cpuCoreCount</nameTransKey>
   <needTrans>false</needTrans>
  </ecs.n4.xlarge>
  <ecs.n4.xlarge>
   <featureValue  />
   <featureName>GPU类型</featureName>
   <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.gpuSpec</nameTransKey>
   <needTrans>false</needTrans>
  </ecs.n4.xlarge>
 </instanceSpecDetail>
 <currency>CNY</currency>
 <startTime>2023-07-21T03:00:00Z</startTime>
 <modifiedBy>4</modifiedBy>
 <mergeCount>0</mergeCount>
 <identifier>ecs</identifier>
 <product>ECS</product>
 <orgName>dts_test</orgName>
 <resourceGroupName>ResourceSet(dts_test)</resourceGroupName>
 <groupByType>instance</groupByType>
 <billingTime>2023-07-21T21:00:03Z</billingTime>
 <cycleType>Hourly</cycleType>
 <instanceTag>
  <EnableHotUpgrade>true</EnableHotUpgrade>
 </instanceTag>
 <reliefPrice>0</reliefPrice>
 <regionId>cn-qingdao-***-d01</regionId>
 <instanceSpec>ecs.xn4.small</instanceSpec>
 <endTime>2023-07-21T04:00:00Z</endTime>
 <billCycle>2023-07</billCycle>
 <platformCode>default</platformCode>
 <extraInfo>
  <allocatedQuantity>50GB</allocatedQuantity>
 </extraInfo>
</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> <errorMessage>no permission</errorMessage> <errorCode>403</errorCode> <pageSize>20</pageSize> <token>{&quot;InsId&quot;:&quot;i-f9m05tzk3wtss0y8****&quot;,&quot;Pos&quot;:&quot;Hourly-instance_ECS_0000000003_2023-07- 21T09:00:00Z&quot;,&quot;ResourceGId&quot;:&quot;2&quot;,&quot;RegionId&quot;:&quot;cn-qingdao-***-d01&quot;}</token>
```

##### 4.1.2.15. TagResources

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/tag_manage/tagResources HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceType | String | Body | 是 | ecsinstance _ | 资源类型。 |
| ResourceId | RepeatList | Body | 是 | i-nn901koe5tx5ei45**** | 待绑定标签的资源ID。 |
| Tag | RepeatList | Body | 是 | - | 标签列表。 |
| -Key | String |  | 否 | testtagk1 | 标签键。不支持以aliyun和acs:开头，不能包含 http://或者https:// 。不允许为空字符串，最多支持128个字符。 |
| -Value | String |  | 否 | testtagv1 | 标签值。不能包含http://或者https://。允许为空字符串。最多支持128个字符。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 |
| message | String | TagResources success. | 返回提示信息。 |
| requestId | String | 530dxxx-dxx******-x6b61axxxxx | 请求ID。 |
| errorKey | String | ascm.auth.InternalError | 错误码。 |
| pureListData | Boolean | false | 是否只返回数据。 |

**示例**

请求示例

```json
POST /ascm/manage/tag_manage/tagResources HTTP/1.1 { "ResourceType":"ecs_instance", "ResourceId.1":"i-nn901koe5tx5ei45****", "Tag.1.Key":"testtagk1", "Tag.1.Value":"testtagv1", }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.auth.InternalError", "code":"200", "success":true, "requestId":"530dxxx-dxx******-x6b61axxxxx", "pureListData":false, "message":"TagResources success." } |  |

`XML` 格式

```xml
<errorKey>ascm.auth.InternalError</errorKey> <code>200</code> <success>true</success> <requestId>530dxxx-dxx******-x6b61axxxxx</requestId> <pureListData>false</pureListData>
```

##### 4.1.2.16. UnTagResources

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ResourceType | String | Body | 是 | ecsinstance _ | 资源类型。 |
| ResourceId | RepeatList | Body | 是 | i-nn901koe5tx5ei45**** | 待解绑标签的资源ID。 |
| TagKey | RepeatList | Body | 是 | testtagk1 | 标签键。不允许为空字符串，最多支持128个字符。不支持以aliyun和acs:开头，不能包含 http://或者https://。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 |
| message | String | UnTagResources success. | 返回提示信息。 |
| requestId | String | 530dxxx-dxx******-x6b61axxxxx | 请求ID。 |
| errorKey | String | ascm.auth.InternalError | 错误码。 |
| pureListData | Boolean | false | 是否只返回数据。 |

**示例**

请求示例

```json
POST /ascm/manage/tag_manage/unTagResources HTTP/1.1 { "ResourceType":"ecs_instance", "ResourceId.1":"i-nn901koe5tx5ei45****", "TagKey.1":"testtagk1" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.auth.InternalError", "code":"200", "success":true, "requestId":"530dxxx-dxx******-x6b61axxxxx", "pureListData":false, "message":"UnTagResources success." } |  |

| XML | 格式 |
|---|---|
| <errorKey>ascm.auth.InternalError</errorKey> <code>200</code> <success>true</success> <requestId>530dxxx-dxx******-x6b61axxxxx</requestId> <pureListData>false</pureListData> <message>UnTagResources success.</message> |  |

##### 4.1.2.17. QueryServiceCategoryTreeOpenApi

查询用户有权限的服务分类树OpenAPI

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /serviceCatalog/queryServiceCategoryTree HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | {} | 服务分类树。 |
| -children | Array | [] | 此一级服务分类的二级分类列表。 |
| --value | String | CloudServer | 二级服务分类Code。 |
| --label | String | 云服务器 | 二级服务分类名称。 |
| --isPreset | Boolean | true | 是否是预置服务分类。 |
| -value | String | ElasticComputing | 一级服务分类Code。 |
| -label | String | 计算 | 一级服务分类名称。 |
| -isPreset | Boolean | true | 是否是预置服务分类。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态响应码。 |
| errorCode | String | ascm.coms.catalog.CallApiError | 返回错误码。 |
| errorMessage | String | 调用API错误 | 返回错误信息。 |

**示例**

请求示例

```
POST /serviceCatalog/queryServiceCategoryTree HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":[ { "isPreset":true, "label":"计算", "children":[ { "isPreset":true, "label":"云服务器", "value":"CloudServer" } ], "value":"ElasticComputing" } ], "success":true, "errorMessage":"", "errorCode":"" } |  |

`XML` 格式

```xml
<code>200</code> <data>
 <isPreset>true</isPreset>
 <label>计算</label>
 <children>
  <isPreset>true</isPreset>
```

`<label>`云服务器`</label>`

```xml
  <value>CloudServer</value>
 </children>
 <value>ElasticComputing</value>
</data> <success>true</success> <errorMessage /> <errorCode />
```

##### 4.1.2.18. QueryServiceCatalogPageOpenApi

查询服务目录列表OpenAPI

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /serviceCatalog/queryServiceCatalogPage HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | String | Body | 否 | ecs | 服务名称搜索关键字。 |
| categoryCode | String | Body | 否 | ElasticComputing | 服务分类Code，可传递一级服务分类Code、二级服务分类Code。 从服务分类树接口“QueryServiceCategoryTreeOpenApi”中获取服务分类Code。 |
| pageSize | Integer | Body | 否 | 10 | 每页数量。 默认值：10 取值范围：<1, 50> |
| pageNumber | Integer | Body | 否 | 1 | 页码。 默认值：1 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [] | 服务列表数据。 |
| -catalogId | String | CS000711 | 服务ID。 |
| -name | String | ECS实例 | 服务名称。 |
| -description | String | ECS实例的预置基础服务，无任何限制规则 | 服务描述。 |
| -identifierName | String | 云服务器 ECS | 服务对应的产品的菜单名称。 |
| -resourceTypeName | String | ECS实例 | 服务对应的资源类型名称。 |
| -createUrl | String | /ascm/buy?product=server- public&fromServiceCatalog=true &catalogId=CS000711&AscmPlat formCode=pl- txvnpuvsqxrm2ced&aliyunmcm _ _ cloudtype=ALIYUN _ | 服务开通页地址。 |
| -createUrlType | String | CATALOGLINK _ | 服务开通页地址的类型。 CATALOG _LINK：服务开通页链接类型。 CLOUD _PRODUCT _LINK：云产品页面链接类型。 SPECIFY _URL：指定URL直接跳转类型。 |
| total | Integer | 11 | 服务总数。 |
| pageSize | Integer | 10 | 每页大小。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| pageNumber | Integer | 1 | 当前页码。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态响应码。 |
| errorCode | String | ascm.coms.catalog.CallApiError | 返回错误码。 |
| errorMessage | String | 调用API错误 | 返回错误信息。 |

**示例**

请求示例

```json
POST /serviceCatalog/queryServiceCatalogPage HTTP/1.1 {
    "name": "ecs",
    "categoryCode": "ElasticComputing",
    "pageNumber": 1,
    "pageSize": 10
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "total":11, "pageNumber":1, "pageSize":10, "code":"200", "data":[ { "identifierName":"云服务器 ECS", "catalogId":"CS000711", "name":"ECS实例", "description":"ECS实例的预置基础服务，无任何限制规则", "createUrl":"/ascm/buy?product=server-public&fromServiceCatalog=true&catalogId=CS000711&AscmPlatformCode=pl- txvnpuvsqxrm2ced&aliyun_mcm_cloud_type=ALIYUN", "resourceTypeName":"ECS实例", "createUrlType":"CATALOG_LINK" } ], "success":true, "errorMessage":"", "errorCode":"" } |  |

| XML | 格式 |
|---|---|
| <total>11</total> <pageNumber>1</pageNumber> <pageSize>10</pageSize> <code>200</code> <data> <identifierName>云服务器 ECS</identifierName> <catalogId>CS000711</catalogId> <name>ECS实例</name> <description>ECS实例的预置基础服务，无任何限制规则</description> <createUrl>/ascm/buy?product=server-public&amp;fromServiceCatalog=true&amp;catalogId=CS000711&amp;AscmPlatformCode=pl- txvnpuvsqxrm2ced&amp;aliyun_mcm_cloud_type=ALIYUN</createUrl> <resourceTypeName>ECS实例</resourceTypeName> <createUrlType>CATALOG_LINK</createUrlType> </data> <success>true</success> <errorMessage /> <errorCode /> |  |

##### 4.1.2.19. QueryBudgetAccountDetail

查询预算账户信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/budget/budgetAccount/queryBudgetAccountDetail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| bizId | String | Body | 否 | 77 | 预算账户ID。 |
| includeDeleted | Boolean | Body | 否 | true | 是否查询已删除的。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| cost | Integer | 121 | 耗时时间。 |
| requestId | String | FEB7A954-F07F-45EA-B6A3- 980DD0F9**** | 本次调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 错误码。 |
| errorMessage | String | Specified access key is not found. | 错误信息。 |
| token | String | affe0c6042f09722fec95a21b8b** **** | Token值。 |
| data | Struct | {} | 响应结果。 |
| -independentDetail | Struct | {} | 预算账户详细信息。 |
| --accountName | String | 组织cmm | 账号名称。 |
| --mod | String | ORG | mod是指预算账户采用的模式，分为财务单元模式和组织模式。 |
| --accountType | String | INDEPENDENT | 账户类型。 |
| --total | String | 900 | 总额度。 |
| --freeze | String | 0 | 冻结额度。 |
| --available | String | 900 | 可用额度。 |
| --used | String | 0 | 已用额度。 |

**示例**

请求示例

```json
POST /ascm/budget/budgetAccount/queryBudgetAccountDetail HTTP/1.1 { "bizId":"77", "includeDeleted":"true" }
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":121,
 "data":{
  "independentDetail":{
   "total":"900",
   "mod":"ORG",
   "freeze":"0",
   "accountName":"组织cmm",
   "accountType":"INDEPENDENT",
   "available":"900",
   "used":"0"
  }
 },
 "requestId":"FEB7A954-F07F-45EA-B6A3-980DD0F9****",
 "success":true,
 "errorMessage":"Specified access key is not found.",
 "errorCode":"InvalidAccessKeyId.NotFound",
 "token":"affe0c6042f09722fec95a21b8b******"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data> <independentDetail> <total>900</total> <mod>ORG</mod> <freeze>0</freeze> <accountName>组织cmm</accountName> <accountType>INDEPENDENT</accountType> <available>900</available> <used>0</used> </independentDetail> </data> <requestId>FEB7A954-F07F-45EA-B6A3-980DD0F9****</requestId> <success>true</success> <errorMessage>Specified access key is not found.</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>affe0c6042f09722fec95a21b8b******</token> |  |

##### 4.1.2.20. BillSummaryQuery

账单汇总查询。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/billing/web/query/range HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| cycleType | String | Body | 是 | Monthly | 账单周期类型。此接口中仅保证账单周期类型为 Monthly，用于返回汇总数据。 |
| groupByType | String | Body | 否 | instance | 账单聚合类型： instance：按实例 product：按产品 region：按区域 organization：按组织 resourceSet：按资源集 orgAllProduct：聚合组织下所有产品 resAllProduct：聚合资源集下所有产品 overall：聚合所有 |
| startTime | String | Body | 否 | 2025-11 | 账期。 |
| orgIdList | String | Body | 否 | [3,4] | 组织ID列表。 |
| resourceGidList | String | Body | 否 | [2,3] | 资源集ID列表。 |
| pageSize | Integer | Body | 否 | 10 | 每页数量。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| productList | String | Body | 否 | ["ecs", "vpc"] | 产品列表。 |
| isParentId | Integer | Body | 否 | 1 | 是否查询子组织账单。默认值为0，即默认不查询子组织。 0：否 1：是 |
| insId | String | Body | 否 | i-f9m05j7zfc7b3mhux*** | 实例ID。 |
| pageNumber | Integer | Body | 否 | 1 | 页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [ ] | 响应结果。 |
| -currency | String | CNY | 货币单位。 |
| -cycleType | String | Monthly | 账单周期类型。此接口中仅保证账单周期类型为Monthly，用于返回汇总数据。 |
| -groupByType | String | instance | 账单聚合类型。 |
| -orgId | String | 3 | 组织ID。 |
| -orgName | String | astbbigdata | 组织名称。 |
| -resourceGid | String | 2 | 资源集ID。 |
| -resourceGroupName | String | ResourceSet(astbbigdata) | 资源集名称。 |
| -product | String | 专有网络 VPC | 产品名称。 |
| -startTime | String | 2025-10-31T17:00:00Z | 开始时间。 |
| -endTime | String | 2025-11-30T17:00:00Z | 结束时间。 |
| -price | Float | 1615.5 | 应付金额。 |
| -discountPrice | Float | 0 | 折扣金额。 |
| -originalPrice | Float | 1615.5 | 消费金额。 |
| -reliefPrice | Float | 0 | 减免金额。 |
| -relievedPrice | Float | 0 | 已减免金额。 |
| -roundingAmount | Float | 0 | 抹零金额。 |
| -modifiedTime | String | 2025-11-28 05:00:39 | 修改时间。 |
| -billCycle | String | 2025-11 | 账期。 |
| -payType | String | all | 付费类型。 |
| -identifier | String | 专有网络 VPC | 云产品。 |
| -identifierGroup | String | 网络 | 云产品分组。 |
| code | String | 200 | 响应码。 |
| cost | Integer | 121 | 耗时时间。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | FEB7A954-F07F-45EA-B6A3- 980DD0F9**** | 本次调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| errorCode | String | InternalServerError | 错误码。 |
| errorMessage | String | InternalServerError | 错误信息。 |
| token | String | affe0c6042f09722fec95a21b8b** **** | Token值。 |
| pageSize | Integer | 10 | 单页数量。 |
| pageNumber | Integer | 1 | 页码。 |

**示例**

请求示例

```json
POST /ascm/billing/billing/web/query/range HTTP/1.1 { "cycleType": "Monthly", "groupByType":"instance", "startTime": "2025-11", }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "pageNumber":1, "data":[ { "resourceGid":"2", "roundingAmount":0.0, "modifiedTime":"2025-11-28 05:00:39", "identifier":"专有网络 VPC", "product":"专有网络 VPC", "relievedPrice":0.0, "orgName":"astbbigdata", "resourceGroupName":"ResourceSet(astbbigdata)", "originalPrice":1615.5, "groupByType":"instance", "discountPrice":0.0, "orgId":"3", "cycleType":"Monthly", "reliefPrice":0.0, "payType":"all", "identifierGroup":"网络", "price":1615.5, "currency":"CNY", "startTime":"2025-10-31T17:00:00Z", "endTime":"2025-11-30T17:00:00Z", "billCycle":"2025-11" } ], "requestId":"FEB7A954-F07F-45EA-B6A3-980DD0F9****", "success":true, "errorMessage":"InternalServerError", "errorCode":"InternalServerError", "pageSize":10, "token":"affe0c6042f09722fec95a21b8b******" } |  |

`XML` 格式

```xml
<code>200</code> <cost>121</cost> <pageNumber>1</pageNumber> <data>
 <resourceGid>2</resourceGid>
 <roundingAmount>0</roundingAmount>
 <modifiedTime>2025-11-28 05:00:39</modifiedTime>
 <relievedPrice>0</relievedPrice>
 <orgName>astbbigdata</orgName>
 <resourceGroupName>ResourceSet(astbbigdata)</resourceGroupName>
 <originalPrice>1615.5</originalPrice>
 <groupByType>instance</groupByType>
 <discountPrice>0</discountPrice>
 <orgId>3</orgId>
 <cycleType>Monthly</cycleType>
 <reliefPrice>0</reliefPrice>
 <payType>all</payType>
 <identifierGroup>网络</identifierGroup>
 <price>1615.5</price>
 <currency>CNY</currency>
 <startTime>2025-10-31T17:00:00Z</startTime>
 <endTime>2025-11-30T17:00:00Z</endTime>
 <billCycle>2025-11</billCycle>
</data> <requestId>FEB7A954-F07F-45EA-B6A3-980DD0F9****</requestId> <success>true</success> <errorMessage>InternalServerError</errorMessage> <errorCode>InternalServerError</errorCode> <pageSize>10</pageSize> <token>affe0c6042f09722fec95a21b8b******</token>
```

##### 4.1.2.21. UpdateIndependentAmountByBizId

调整账户的额度。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/budget/budgetAccountOpen/UpdateIndependentAmountByBizId HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| bizId | String | Body | 否 | 77 | 预算账户ID，一般情况下即为要充值的组织ID。 |
| updateType | String | Body | 否 | ADD | 调整类型。 ADD：表示增加。 MINUS：表示减少。 |
| amount | String | Body | 否 | 299 | 金额。 |
| memo | String | Body | 否 | 增加 | 备注。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| cost | Integer | 121 | 耗时时间。 |
| requestId | String | 64C8D24A-2266-44AA-8CF7- 1783F4C7**** | 本次调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 错误码。 |
| errorMessage | String | Specified access key is not found. | 错误信息。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| token | String | affe0c6042f09722fec95a21b8b** **** | Token值。 |
| data | Boolean | true | 响应结果。 |

**示例**

请求示例

```json
POST /ascm/budget/budgetAccountOpen/UpdateIndependentAmountByBizId HTTP/1.1 { "bizId":"77", "updateType":"ADD", "amount":"299",
```

`"memo":"`增加"

```
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "data":true, "requestId":"64C8D24A-2266-44AA-8CF7-1783F4C7****", "success":true, "errorMessage":"Specified access key is not found.", "errorCode":"InvalidAccessKeyId.NotFound", "token":"affe0c6042f09722fec95a21b8b******" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data>true</data> <requestId>64C8D24A-2266-44AA-8CF7-1783F4C7****</requestId> <success>true</success> <errorMessage>Specified access key is not found.</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>affe0c6042f09722fec95a21b8b******</token> |  |

##### 4.1.2.22. PageCashFlow

查询用户所属组织的收支明细列表数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| query | Json | Body | 否 | {"bizId":"77"} | 查询条件。bizId的值即为用户当前所属组织的 ID。 |
| pageNumber | Integer | Body | 否 | 1 | 页码。 |
| pageSize | Integer | Body | 否 | 10 | 每页数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [ ] | 响应结果。 |
| -cashFlowId | String | 12495928662072**** | 流水号。 |
| -amount | String | 1000 | 金额。 |
| -consumerTime | Long | 1764299800000 | 流水发生的时间。 |
| -assignAccountName | String | 组织cmm | 分配账户名称。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -cashFlowType | String | DEPOSIT | 流水类型。 DEPOSIT：表示调整额度。 ADJUST：表示分配调整。 FREEZE：表示冻结。 UNFREEZE：表示解冻。 SETTLE：表示结算。 REFUND：表示退款。 |
| -operator | String | admin | 操作人。 |
| - independentAccountName | String | 组织cmm | 独立账户名称。 |
| -billingDate | String | 2025-11-28 | 账单日期。 |
| -incomeExpenseType | String | INCOME | 收支类型。 INCOME：表示收入。 EXPENSE：表示支出。 |
| -billingCycle | String | 2025-11 | 账期。 |
| -consumerTimeUtc | String | 2025-11-28T03:16:40Z | 流水发生的UTC时间。 |
| -currency | String | CNY | 货币单位。 |
| -id | Long | 1 | 流水ID。 |
| code | String | 200 | 响应码。 |
| cost | Integer | 150 | 耗时时间。 |
| requestId | String | F6D1E15E-5AC9-4D74-A111- B47FC1FA**** | 调用请求的ID。 |
| success | Boolean | true | 接口请求成功标识。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 错误码。 |
| errorMessage | String | Specified access key is not found. | 错误信息。 |
| token | String | affe0c6042f09722fec95a21b8b** **** | Token值。 |
| pageSize | Integer | 10 | 每页大小。 |
| pageNumber | Integer | 1 | 页码。 |

**示例**

请求示例

```json
POST /ascm/budget/budgetAccountOpen/PageCashFlow HTTP/1.1 { "pageNumber": 1, "pageSize": 10, "query": {
    "bizId": "77"
} }
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "cost":150,
 "pageNumber":1,
 "data":[
  {
   "cashFlowId":"12495928662072****",
   "amount":"1000",
   "consumerTime":1764299800000,
   "assignAccountName":"组织cmm",
   "cashFlowType":"DEPOSIT",
   "operator":"admin",
   "independentAccountName":"组织cmm",
   "billingDate":"2025-11-28",
   "incomeExpenseType":"INCOME",
   "billingCycle":"2025-11",
   "consumerTimeUtc":"2025-11-28T03:16:40Z",
   "currency":"CNY",
   "id":1
  }
```

`],`

```json
 "requestId":"F6D1E15E-5AC9-4D74-A111-B47FC1FA****",
 "success":true,
 "errorMessage":"Specified access key is not found.",
 "errorCode":"InvalidAccessKeyId.NotFound",
 "pageSize":10,
 "token":"affe0c6042f09722fec95a21b8b******"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>150</cost> <pageNumber>1</pageNumber> <data> <cashFlowId>12495928662072****</cashFlowId> <amount>1000</amount> <consumerTime>1764299800000</consumerTime> <assignAccountName>组织cmm</assignAccountName> <cashFlowType>DEPOSIT</cashFlowType> <operator>admin</operator> <independentAccountName>组织cmm</independentAccountName> <billingDate>2025-11-28</billingDate> <incomeExpenseType>INCOME</incomeExpenseType> <billingCycle>2025-11</billingCycle> <consumerTimeUtc>2025-11-28T03:16:40Z</consumerTimeUtc> <currency>CNY</currency> <id>1</id> </data> <requestId>F6D1E15E-5AC9-4D74-A111-B47FC1FA****</requestId> <success>true</success> <errorMessage>Specified access key is not found.</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <pageSize>10</pageSize> <token>affe0c6042f09722fec95a21b8b******</token> |  |

##### 4.1.2.23. QueryIssueOpenApi

查询工单列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /issue/queryIssue HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| pageSize | Integer | Body | 否 | 10 | 单页大小。默认为10，最大为50。 |
| pageNumber | Integer | Body | 否 | 1 | 页码，从1开始，不能小于1。 |
| issueId | Integer | Body | 否 | ti-20251110125412674*** | 筛选项入参，工单业务编号，用于模糊查找。 |
| issueCategoryId | Integer | Body | 否 | 1 | 筛选项入参，工单分类ID。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| modifiedStartTime | Integer | Body | 否 | 2025-11-10T09:49:17Z | 筛选项入参，修改时间-起始，YYYY-MM- ddTHH:mm:ssZ，时区：UTC。 |
| modifiedEndTime | Integer | Body | 否 | 2025-11-10T09:49:17Z | 筛选项入参，修改时间-结束，YYYY-MM- ddTHH:mm:ssZ，时区：UTC。 |
| modifier | Integer | Body | 否 | 500 | 筛选项入参，工单修改人ID。 |
| finishStartTime | Integer | Body | 否 | 2025-11-10T09:49:17Z | 筛选项入参，完结时间-起始，YYYY-MM- ddTHH:mm:ssZ，时区：UTC。 |
| finishEndTime | Integer | Body | 否 | 2025-11-10T09:49:17Z | 筛选项入参，完结时间-起始，YYYY-MM- ddTHH:mm:ssZ，时区：UTC。 |
| status | Integer | Body | 否 | COMPLETED | 筛选项入参，工单状态code。 WAIT：待认领 WITHDRAWN：已撤回 PROGRESS：处理中 FEEDBACK：待反馈 CONFIRM：待确认 COMPLETED：已完结 PENDING：挂起中 |
| tab | Integer | Body | 否 | TODO | 筛选项入参，列表类型，当前只透出 tab=“TODO”类型。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 工单列表信息。 |
| -id | Long | 6 | 工单自增ID。 |
| -issueId | String | ti-20251110125412674*** | 工单业务编号。 |
| -issueCategoryId | Long | 2 | 工单分类ID。 |
| -issueCategoryName | String | 产品使用问题 | 工单分类名称。 |
| -creator | Long | 600 | 工单创建人ID。 |
| -creatorName | String | test-person | 工单创建人名称。 |
| -createTime | String | 2025-11-10T09:49:17Z | 工单创建时间，YYYY-MM-ddTHH:mm:ssZ，时区：UTC。 |
| -modifiedTime | String | 2025-11-10T09:49:17Z | 工单修改时间，YYYY-MM-ddTHH:mm:ssZ，时区：UTC。 |
| -processor | Long | 800 | 工单处理人ID。 |
| -processorName | String | test123 | 工单处理人名称。 |
| -finishTime | String | 2025-11-10T09:49:17Z | 工单完结时间，YYYY-MM-ddTHH:mm:ssZ，时区：UTC。 |
| -status | String | COMPLETED | 工单状态code。 |
| -version | Integer | 5 | 工单版本，每做一次操作会自增的值，用于判断工单是否过期。 |
| total | Integer | 100 | 总条数。 |
| pageSize | Integer | 10 | 单页大小。默认为10，最大为50。 |
| pageNumber | Integer | 1 | 页码，从1开始，不能小于1。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 响应码。 |
| errorCode | String | InternalServerError | 错误码。 |
| errorMessage | String | InternalServerError | 错误信息。 |

**示例**

请求示例

```json
POST /issue/queryIssue HTTP/1.1 {
    "issueId": "ti-202511",
    "issueCategoryId": 5,
    "modifier": 5003,
    "status": "COMPLETED",
    "tab": "ALL",
    "pageNumber": 1,
    "pageSize": 10,
    "modifiedStartTime": "2025-11-01T07:42:16Z",
    "modifiedEndTime": "2025-11-22T07:42:16Z",
    "finishStartTime": "2025-11-01T07:41:52Z",
    "finishEndTime": "2025-11-23T07:41:52Z"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "total":100, "pageNumber":1, "code":"200", "data":[ { "issueCategoryName":"产品使用问题", "modifiedTime":"2025-11-10T09:49:17Z", "issueId":"ti-20251110125412674***", "creator":600, "finishTime":"2025-11-10T09:49:17Z", "creatorName":"test-person", "processor":800, "version":5, "issueCategoryId":2, "createTime":"2025-11-10T09:49:17Z", "processorName":"test123", "id":6, "status":"COMPLETED" } ], "success":true, "pageSize":10, } |  |

| XML | 格式 |
|---|---|
| <total>100</total> <pageNumber>1</pageNumber> <code>200</code> <data> <issueCategoryName>产品使用问题</issueCategoryName> <modifiedTime>2025-11-10T09:49:17Z</modifiedTime> <issueId>ti-20251110125412674***</issueId> <creator>600</creator> <finishTime>2025-11-10T09:49:17Z</finishTime> <creatorName>test-person</creatorName> <processor>800</processor> <version>5</version> <issueCategoryId>2</issueCategoryId> <createTime>2025-11-10T09:49:17Z</createTime> <processorName>test123</processorName> <id>6</id> <status>COMPLETED</status> </data> <success>true</success> <pageSize>10</pageSize> |  |

##### 4.1.2.24. CreateDiscount

创建折扣。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | String | Body | 是 | 测试折扣001 | 折扣名称。 |
| priority | Integer | Body | 是 | 1 | 折扣优先级。 |
| discountType | String | Body | 是 | uni | 折扣类型。 uni：统一折扣。 product：分产品折扣。 |
| periodValidStartTi me | String | Body | 是 | 2026-01-17 | 折扣适用时间范围开始时间。 |
| periodValidEndTim e | String | Body | 是 | 2026-01-19 | 折扣适用时间范围结束时间。 |
| productDiscountDe tail | Json | Body | 是 | {"discountValueUni":1,"productDiscounts" : [{"productCode":"Gws","discountValue":1 }, {"productCode":"EBS","discountValue":1} ],"platformList":[]} | 折扣具体详情。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识。 |
| data | Struct | - | 创建结果详情。 |
| -id | Long | 29 | 折扣ID。 |

**示例**

请求示例

```
POST /ascm/trade/discount/create HTTP/1.1 {
```

`"name":"`测试折扣`001",`

```json
"priority":"1", "discountType":"uni", "periodValidStartTime":"2026-01-17", "periodValidEndTime":"2026-01-19", "productDiscountDetail":"{"discountValueUni":1,"productDiscounts":[{"productCode":"Gws","discountValue":1}, {"productCode":"EBS","discountValue":1}],"platformList":[]}" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":{ "id":29 }, "requestId":"0a1128a916917198245846573e****", "success":true } |  |

`XML` 格式

```xml
<code>200</code> <data>
 <id>29</id>
</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success>
```

##### 4.1.2.25. UpdateDiscount

更新折扣。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/update HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 是 | 29 | 折扣ID。 |
| name | String | Body | 是 | 测试折扣001 | 折扣名称。 |
| priority | Integer | Body | 是 | 1 | 折扣优先级。 |
| discountType | String | Body | 是 | uni | 折扣类型： uni：统一折扣。 product：分产品折扣。 |
| periodValidStartTi me | String | Body | 是 | 2026-01-17 | 折扣适用时间范围开始时间。 |
| periodValidEndTim e | String | Body | 是 | 2026-01-19 | 折扣适用时间范围结束时间。 |
| productDiscountDe tail | Json | Body | 是 | {"discountValueUni":1,"productDiscounts" : [{"productCode":"Gws","discountValue":1 }, {"productCode":"EBS","discountValue":1} ],"platformList":[]} | 折扣具体详情。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| data | Boolean | true | 更新结果。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
POST /ascm/trade/discount/update HTTP/1.1 { "id":"29",
```

`"name":"`测试折扣`001",`

```json
"priority":"1", "discountType":"uni", "periodValidStartTime":"2026-01-17", "periodValidEndTime":"2026-01-19", "productDiscountDetail":"{"discountValueUni":1,"productDiscounts":[{"productCode":"Gws","discountValue":1}, {"productCode":"EBS","discountValue":1}],"platformList":[]}" }
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "data":true,
 "requestId":"0a1128a916917198245846573e****",
 "success":true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> |  |

##### 4.1.2.26. EnableDiscount

启用折扣。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/enable HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 是 | 29 | 折扣ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识： true: 成功。 false: 失败。 |
| data | Struct | - | 启用结果详情。 |
| -id | Long | 29 | 折扣ID。 |
| -result | Boolean | true | 启用结果： true: 成功。 false: 失败。 |
| -status | Integer | 0 | 折扣状态： 0：表示停用。 1：表示启用。 |

**示例**

请求示例

```json
POST /ascm/trade/discount/enable HTTP/1.1 { "id":"29" }
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "data":{
  "result":true,
  "id":29,
  "status":0
 },
 "requestId":"0a1128a916917198245846573e****",
 "success":true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <data> <result>true</result> <id>29</id> <status>0</status> </data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> |  |

##### 4.1.2.27. DisableDiscount

禁用折扣。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/disable HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 是 | 29 | 折扣ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| data | Struct | - | 停用折扣详情。 |
| -id | Long | 29 | 折扣ID。 |
| -result | Boolean | true | 停用结果： true：成功。 false：失败。 |
| -status | Integer | 0 | 折扣状态： 0：表示停用。 1：表示启用。 |

**示例**

请求示例

```json
POST /ascm/trade/discount/disable HTTP/1.1 { "id":"29" }
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "data":{
  "result":true,
  "id":29,
  "status":0
 },
 "requestId":"0a1128a916917198245846573e****",
 "success":true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <data> <result>true</result> <id>29</id> <status>0</status> </data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> |  |

##### 4.1.2.28. QueryDiscount

查询折扣详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/query HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | String | Body | 否 | 测试折扣001 | 折扣名称。 |
| orgIds | RepeatList | Body | 否 | ["3","4"] | 组织ID列表。 |
| resourceGroupIds | RepeatList | Body | 否 | ["2","3"] | 资源集ID列表。 |
| statuses | RepeatList | Body | 否 | ["0","1"] | 状态列表。 |
| pageNumber | Integer | Body | 否 | 1 | 查询页码。 默认值：1 |
| pageSize | Integer | Body | 否 | 20 | 查询页大小。 默认值：20 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 折扣列表详情。 |
| -orgs | Array | - | 组织列表详情。 |
| --orgId | String | 3 | 组织ID。 |
| --orgName | String | 测试组织001 | 组织名称。 |
| -resourceGroups | Array | - | 资源集列表详情。 |
| --resourceGroupId | String | 2 | 资源集ID。 |
| --resourceGroupName | String | 测试资源集001 | 资源集名称。 |
| -id | Long | 29 | 折扣ID。 |
| -uuid | String | Dis202512045*** | 折扣UUID。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -name | String | 测试折扣001 | 折扣名称。 |
| -description | String | 这是一段描述文字 | 折扣描述。 |
| -status | Integer | 0 | 折扣状态： 0：表示停用。 1：表示启用。 |
| -priority | Integer | 1 | 折扣优先级。 |
| -discountType | String | uni | 折扣类型： uni：统一折扣。 product：分产品折扣。 |
| -periodValidStartTime | String | 2025-12-01 00:00:00 | 折扣适用时间范围的开始时间（服务器部署时区）。 |
| -periodValidStartTimeUtc | String | 2025-11-30T16:00:00Z | 折扣适用时间范围的开始时间（UTC时区）。 |
| -periodValidEndTime | String | 2025-12-08 00:00:00 | 折扣适用时间范围的结束时间（服务器部署时区）。 |
| -periodValidEndTimeUtc | String | 2025-12-07T16:00:00Z | 折扣适用时间范围的结束时间（UTC时区）。 |
| -auditId | String | pi-2508111640110*** | 审批ID。 |
| -createdBy | String | admin | 创建人。 |
| -modifiedBy | String | admin | 修改人。 |
| -gmtModified | String | 2025-12-04T17:20:19 | 修改时间（服务器部署时区）。 |
| -gmtModifiedUtc | String | 2025-12-04T09:20:19Z | 修改时间（UTC时区）。 |
| -deleted | Integer | 0 | 删除标记。 |
| -productDiscountDetail | Struct | - | 产品折扣详情。 |
| --productDiscounts | Array | - | 产品折扣详情。 |
| ---productCode | String | EBS | 资源Code。 |
| ---displayName | String | ECS磁盘 | 资源名称。 |
| ---discountValue | Float | 0.7 | 折扣值。 |
| --platformList | Array | - | 适用平台详情。 |
| ---regionList | Array | - | 适用地域详情。 |
| ----regionId | String | cn-test | 地域ID。 |
| ----regionName | String | region01 | 地域名称。 |
| ---platformCode | String | pl-xjtshhyjnyvt4*** | 平台Code。 |
| ---displayName | String | 公共云账户001 | 平台名称。 |
| --discountValueUni | Float | 0.7 | 统一折扣值。 |
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| pageNumber | Integer | 1 | 页码。 |
| pageSize | Integer | 20 | 页大小。 |
| total | Long | 3 | 总页数。 |

**示例**

请求示例

```
POST /ascm/trade/discount/query HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "total":3,
 "code":"200",
 "pageNumber":1,
 "data":[
  {
   "auditId":"pi-2508111640110***",
   "gmtModified":"2025-12-04T17:20:19",
   "periodValidStartTimeUtc":"2025-11-30T16:00:00Z",
```

`"description":"`这是一段描述文字`",`

```json
   "periodValidEndTime":"2025-12-08 00:00:00",
   "priority":1,
   "uuid":"Dis202512045***",
   "gmtModifiedUtc":"2025-12-04T09:20:19Z",
   "productDiscountDetail":[
    {
     "discountValueUni":0.7,
     "productDiscounts":[
      {
       "productCode":"EBS",
       "displayName":"ECS磁盘",
       "discountValue":0.7
      }
```

`],`

```json
     "platformList":[
      {
       "regionList":[
        {
         "regionId":"cn-test",
         "regionName":"region01"
        }
```

`],` `"displayName":"`公共云账户`001",`

```json
       "platformCode":"pl-xjtshhyjnyvt4***"
      }
```

]

```
    }
```

`],`

```json
   "periodValidStartTime":"2025-12-01 00:00:00",
   "orgs":[
    {
```

`"orgName":"`测试组织`001",`

```json
     "orgId":"3"
    }
```

`],`

```json
   "periodValidEndTimeUtc":"2025-12-07T16:00:00Z",
   "deleted":0,
   "createdBy":"admin",
```

`"name":"`测试折扣`001",`

```json
   "discountType":"uni",
   "modifiedBy":"admin",
   "resourceGroups":[
    {
```

`"resourceGroupName":"`测试资源集`001",`

```json
     "resourceGroupId":"2"
    }
```

`],`

```json
   "id":29,
   "status":0
  }
```

`],`

```json
 "requestId":"0a1128a916917198245846573e****",
 "success":true,
 "pageSize":20
}
```

`XML` 格式

```xml
<total>3</total> <code>200</code> <pageNumber>1</pageNumber> <data>
 <auditId>pi-2508111640110***</auditId>
 <gmtModified>2025-12-04T17:20:19</gmtModified>
 <periodValidStartTimeUtc>2025-11-30T16:00:00Z</periodValidStartTimeUtc>
```

`<description>`这是一段描述文字`</description>`

```xml
 <periodValidEndTime>2025-12-08 00:00:00</periodValidEndTime>
 <priority>1</priority>
 <uuid>Dis202512045***</uuid>
 <gmtModifiedUtc>2025-12-04T09:20:19Z</gmtModifiedUtc>
 <productDiscountDetail>
  <discountValueUni>0.7</discountValueUni>
  <productDiscounts>
   <productCode>EBS</productCode>
   <displayName>ECS磁盘</displayName>
   <discountValue>0.7</discountValue>
  </productDiscounts>
  <platformList>
   <regionList>
    <regionId>cn-test</regionId>
    <regionName>region01</regionName>
   </regionList>
   <displayName>公共云账户001</displayName>
   <platformCode>pl-xjtshhyjnyvt4***</platformCode>
  </platformList>
 </productDiscountDetail>
 <periodValidStartTime>2025-12-01 00:00:00</periodValidStartTime>
 <orgs>
```

`<orgName>`测试组织`001</orgName>`

```xml
  <orgId>3</orgId>
 </orgs>
 <periodValidEndTimeUtc>2025-12-07T16:00:00Z</periodValidEndTimeUtc>
 <deleted>0</deleted>
 <createdBy>admin</createdBy>
```

`<name>`测试折扣`001</name>`

```xml
 <discountType>uni</discountType>
 <modifiedBy>admin</modifiedBy>
 <resourceGroups>
  <resourceGroupName>测试资源集001</resourceGroupName>
  <resourceGroupId>2</resourceGroupId>
 </resourceGroups>
 <id>29</id>
 <status>0</status>
</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> <pageSize>20</pageSize>
```

##### 4.1.2.29. DeleteDiscount

删除折扣。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/delete HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 是 | 29 | 折扣ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| data | Boolean | true | 删除结果。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```json
POST /ascm/trade/discount/delete HTTP/1.1 { "id":"29" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"0a1128a916917198245846573e****", "success":true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> |  |

##### 4.1.2.30. DescribeDiscount

查询折扣详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/detail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | String | Body | 是 | 29 | 折扣ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e 0*** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| data | Struct | - | 折扣详情数据。 |
| -orgs | Array | - | 适用组织详情数据。 |
| --orgId | String | 3 | 组织ID。 |
| --orgName | String | 测试组织001 | 组织名称。 |
| -resourceGroups | Array | - | 资源集详情数据。 |
| --resourceGroupId | String | 2 | 资源集ID。 |
| --resourceGroupName | String | 测试资源集001 | 资源集名称。 |
| -id | Long | 29 | 折扣ID。 |
| -uuid | String | Dis202512045*** | 折扣UUID。 |
| -name | String | 测试折扣001 | 折扣名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -description | String | 这是一段描述文字 | 折扣描述。 |
| -status | Integer | 1 | 折扣状态： 0：表示停用。 1：表示启用。 |
| -priority | Integer | 1 | 折扣优先级。 |
| -discountType | String | uni | 折扣类型： uni：统一折扣。 product：分产品折扣。 |
| -periodValidStartTime | String | 2025-12-01 00:00:00 | 折扣适用时间范围的开始时间（服务器部署时区）。 |
| -periodValidStartTimeUtc | String | 2025-11-30T16:00:00Z | 折扣适用时间范围的开始时间（UTC时区）。 |
| -periodValidEndTime | String | 2025-12-08 00:00:00 | 折扣适用时间范围的结束时间（服务器部署时区）。 |
| -periodValidEndTimeUtc | String | 2025-12-07T16:00:00Z | 折扣适用时间范围的结束时间（UTC时区）。 |
| -auditId | String | pi-2508111640110*** | 审批ID。 |
| -createdBy | String | admin | 创建人。 |
| -modifiedBy | String | admin | 修改人。 |
| -gmtModified | String | 2025-12-04T17:20:19 | 修改时间（服务器部署时区）。 |
| -gmtModifiedUtc | String | 2025-12-04T09:20:19Z | 修改时间（UTC时区）。 |
| -deleted | Integer | 0 | 删除标记。 |
| -productDiscountDetail | Struct | - | 产品折扣详情。 |
| --productDiscounts | Array | - | 产品折扣详情。 |
| ---productCode | String | EBS | 资源Code。 |
| ---displayName | String | 公共云账户001 | 平台名称。 |
| ---discountValue | Float | 0.7 | 折扣值。 |
| --platformList | Array | - | 适用平台详情。 |
| ---regionList | Array | - | 适用地域详情。 |
| ----regionId | String | cn-test | 地域ID。 |
| ----regionName | String | region01 | 地域名称。 |
| ---platformCode | String | pl-xjtshhyjnyvt4*** | 平台Code。 |
| ---displayName | String | 公共云账户001 | 平台名称。 |
| --discountValueUni | Float | 0.7 | 统一折扣值。 |

**示例**

请求示例

```json
POST /ascm/trade/discount/detail HTTP/1.1 { "id":"29" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":{ "auditId":"pi-2508111640110***", "gmtModified":"2025-12-04T17:20:19", "periodValidStartTimeUtc":"2025-11-30T16:00:00Z", "description":"这是一段描述文字", "periodValidEndTime":"2025-12-08 00:00:00", "priority":1, "uuid":"Dis202512045***", "gmtModifiedUtc":"2025-12-04T09:20:19Z", "productDiscountDetail":{ "discountValueUni":0.7, "productDiscounts":[ { "productCode":"EBS", "displayName":"公共云账户001", "discountValue":0.7 } ], "platformList":[ { "regionList":[ { "regionId":"cn-test", "regionName":"region01" } ], "displayName":"公共云账户001", "platformCode":"pl-xjtshhyjnyvt4***" } ] }, "periodValidStartTime":"2025-12-01 00:00:00", "orgs":[ { "orgName":"测试组织001", "orgId":"3" } ], "periodValidEndTimeUtc":"2025-12-07T16:00:00Z", "deleted":0, "createdBy":"admin", "name":"测试折扣001", "discountType":"uni", "modifiedBy":"admin", "resourceGroups":[ { "resourceGroupName":"测试资源集001", "resourceGroupId":"2" } ], "id":29, "status":1 }, "requestId":"0a1128a916917198245846573e0***", "success":true } |  |

`XML` 格式

```xml
<code>200</code> <data>
 <auditId>pi-2508111640110***</auditId>
 <gmtModified>2025-12-04T17:20:19</gmtModified>
 <periodValidStartTimeUtc>2025-11-30T16:00:00Z</periodValidStartTimeUtc>
```

`<description>`这是一段描述文字`</description>`

```xml
 <periodValidEndTime>2025-12-08 00:00:00</periodValidEndTime>
 <priority>1</priority>
 <uuid>Dis202512045***</uuid>
 <gmtModifiedUtc>2025-12-04T09:20:19Z</gmtModifiedUtc>
 <productDiscountDetail>
  <discountValueUni>0.7</discountValueUni>
  <productDiscounts>
   <productCode>EBS</productCode>
   <displayName>公共云账户001</displayName>
   <discountValue>0.7</discountValue>
  </productDiscounts>
  <platformList>
   <regionList>
    <regionId>cn-test</regionId>
    <regionName>region01</regionName>
   </regionList>
   <displayName>公共云账户001</displayName>
   <platformCode>pl-xjtshhyjnyvt4***</platformCode>
  </platformList>
 </productDiscountDetail>
 <periodValidStartTime>2025-12-01 00:00:00</periodValidStartTime>
 <orgs>
```

`<orgName>`测试组织`001</orgName>`

```xml
  <orgId>3</orgId>
 </orgs>
 <periodValidEndTimeUtc>2025-12-07T16:00:00Z</periodValidEndTimeUtc>
 <deleted>0</deleted>
 <createdBy>admin</createdBy>
```

`<name>`测试折扣`001</name>`

```xml
 <discountType>uni</discountType>
 <modifiedBy>admin</modifiedBy>
 <resourceGroups>
  <resourceGroupName>测试资源集001</resourceGroupName>
  <resourceGroupId>2</resourceGroupId>
 </resourceGroups>
 <id>29</id>
 <status>1</status>
</data> <requestId>0a1128a916917198245846573e0***</requestId> <success>true</success>
```

##### 4.1.2.31. ListDiscountPriority

折扣优先级列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/discount/listPriority HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 折扣优先级详情。 |
| -id | Long | 29 | 折扣ID。 |
| -priority | Integer | 1 | 折扣优先级。 |
| -name | String | 测试折扣001 | 折扣名称。 |
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e 0*** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |

**示例**

请求示例

```
POST /ascm/trade/discount/listPriority HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":[ { "name":"测试折扣001", "id":29, "priority":1 } ], "requestId":"0a1128a916917198245846573e0***", "success":true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data> <name>测试折扣001</name> <id>29</id> <priority>1</priority> </data> <requestId>0a1128a916917198245846573e0***</requestId> <success>true</success> |  |

##### 4.1.2.32. BillingProductList

获取计费产品三级列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/productMgr/products/web HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 计费产品三级列表详情。 |
| -identifierDetails | Array | - | 该分类下的详情内容。 |
| --productDetails | Array | - | 该菜单Code下的详情内容。 |
| ---productName | String | EBS | 资源Code |
| ---displayName | String | ECS磁盘 | 资源名称 |
| --identifier | String | ecs | 菜单Code。 |
| --displayName | String | 云服务器 ECS | 产品名称。 |
| -navigationName | String | 计算 | 分类名称。 |
| code | String | 200 | 状态响应码。 |
| requestId | String | 0a1128a916917198245846573e* *** | 请求ID。 |
| success | Boolean | true | 接口请求成功标识。 |

**示例**

请求示例

```
POST /ascm/billing/productMgr/products/web HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":[ { "navigationName":"计算", "identifierDetails":[ { "identifier":"ecs", "displayName":"云服务器 ECS", "productDetails":[ { "displayName":"ECS磁盘", "productName":"EBS" } ] } ] } ], "requestId":"0a1128a916917198245846573e****", "success":true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data> <navigationName>计算</navigationName> <identifierDetails> <identifier>ecs</identifier> <displayName>云服务器 ECS</displayName> <productDetails> <displayName>ECS磁盘</displayName> <productName>EBS</productName> </productDetails> </identifierDetails> </data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> |  |

##### 4.1.2.33. CountProductInstancesByResourceSet

按资源集统计产品实例数量。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /resourceSets/[resourceSetId]/instances HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceSetId | Integer | Path | 是 | 2 | 资源集ID ，必填。 |
| withEmptyResourc e | Boolean | Query | 否 | true | 是否返回空资源的产品统计。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 响应结果。 |
| -productList | Array | - | 产品列表。 |
| --resourceTypeList | Array | - | 资源类型列表。 |
| ---identifierType | String | Networking | 产品分类。 |
| ---productName | String | 专有网络 VPC | 产品名称。 |
| ---resourceType | String | vpcinstance _ | 资源类型。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---organizationId | Integer | 3 | 所属组织ID。 |
| ---resourceSetId | Integer | 2 | 资源集ID。 |
| ---link | String | /vpc/console/sslServicePage? organizationId=3&regionId=cn- wulan-***- d01&resourceGroupId=2 | 产品控制台链接。 |
| ---consoleType | String | oneconsole | console控制台类型。 |
| ---num | Integer | 3 | 对应资源集下的资源数量。 |
| --productName | String | 专有网络 VPC | 产品名称。 |
| --num | Integer | 3 | 对应产品分类下的资源数量。 |
| -identifierType | String | Networking | 产品分类。 |
| -num | Integer | 3 | 资源总数量。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态响应码。 |
| message | String | success | 提示信息。 |

**示例**

请求示例

```
GET /resourceSets/[resourceSetId]/instances HTTP/1.1 &resourceSetId=2
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":[ { "num":3, "identifierType":"Networking", "productList":[ { "num":3, "resourceTypeList":[ { "organizationId":3, "num":3, "link":"/vpc/console/sslServicePage?organizationId=3&regionId=cn-wulan-***-d01&resourceGroupId=2", "identifierType":"Networking", "resourceSetId":2, "productName":"专有网络 VPC", "resourceType":"vpc_instance", "consoleType":"oneconsole" } ], "productName":"专有网络 VPC" } ] } ], "success":true, "message":"success" } |  |

`XML` 格式

```xml
<code>200</code> <data>
 <num>3</num>
 <identifierType>Networking</identifierType>
 <productList>
  <num>3</num>
  <resourceTypeList>
   <organizationId>3</organizationId>
   <num>3</num>
   <link>/vpc/console/sslServicePage?organizationId=3&amp;regionId=cn-wulan-***-d01&amp;resourceGroupId=2</link>
   <identifierType>Networking</identifierType>
   <resourceSetId>2</resourceSetId>
   <resourceType>vpc_instance</resourceType>
   <consoleType>oneconsole</consoleType>
  </resourceTypeList>
 </productList>
</data> <success>true</success> <message>success</message>
```

##### 4.1.2.34. ListCouponTemplate

优惠券模板信息列表查询。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/listCouponTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| couponName | String | Body | 否 | 新用户满减券 | 优惠券名称。 |
| couponId | String | Body | 否 | 200001 | 优惠券模板ID。 |
| status | String | Body | 否 | EFFECTIVE | 模板状态。 |
| expireBeginDate | String | Body | 否 | 2026-02-09T00:00:00 | 范围查询，开始时间。 |
| expireEndDate | String | Body | 否 | 2026-02-10T00:00:00 | 范围查询，结束时间。 |
| orderBy | String | Body | 否 | updateTime | 排序字段，可不填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 响应数据结构体。 |
| -orgRange | List | ["iaastest"] _ | 适用的组织范围。 |
| -resourceRange | List | ["ecs"] | 适用的资源范围。 |
| -couponId | Long | 200001 | 模板ID。 |
| -couponName | String | 春节红包券 | 优惠券模板名称。 |
| -description | String | 仅节日期间可用 | 优惠券描述。 |
| -totalAmount | Float | 1000.00 | 总额。 |
| -totalPublishAmount | Float | 1000.00 | 已经发放的总额。 |
| -remainUnPublishAmount | Float | 0.00 | 未发放的总额。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -totalUsedAmount | Float | 0.00 | 已被消费的金额。 |
| -totalCount | Long | 10 | 发放总量。 |
| -denomination | Float | 100.00 | 每张优惠券的面额。 |
| -publishedCount | Long | 10 | 已经发放的数量。 |
| -remainUnPublishCount | Long | 0 | 未发放的数量。 |
| -totalUsedCount | Integer | 10 | 已经被使用的数量。 |
| -status | String | EFFECTIVE | 优惠券模板状态。 |
| -resourceMode | String | PARTAVAILABLE _ | 适用的资源模式： ALL： 全都可用 PART _AVAILABLE：部分可用 PART _DISABLE：部分不可用 |
| -orgMode | String | ALL | 适用的组织的模式： ALL：全部可用 PART _AVAILABLE：指定组织可用 |
| -validFrom | String | 2023-12-31T16:00:00Z | 模板有效期开始时间。 |
| -validTo | String | 2023-12-31T16:00:00Z | 模板有效期结束时间。 |
| -gmtModified | String | 2023-12-31T16:00:00Z | 模板更新时间。 |
| -modifier | String | admin | 最后修改人。 |
| code | String | 200 | 响应码。 |
| message | String | success | 响应信息。 |
| requestId | String | 748326947932*** | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| pageNumber | Integer | 1 | 页码。 |
| pageSize | Integer | 10 | 页面大小。 |
| total | Long | 10 | 数据总量。 |

**示例**

请求示例

```
POST /ascm/trade/coupon/admin/listCouponTemplate HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "total":10,
 "code":"200",
 "pageNumber":1,
 "data":[
  {
   "totalUsedCount":10,
```

`"couponName":"`春节红包券`",`

```json
   "resourceMode":"PART_AVAILABLE",
   "gmtModified":"2023-12-31T16:00:00Z",
   "orgRange":"[\"iaas_test\"]",
   "modifier":"admin",
```

`"description":"`仅节日期间可用`",`

```json
   "orgMode":"ALL",
   "validFrom":"2023-12-31T16:00:00Z",
   "resourceRange":"[\"ecs\"]",
   "couponId":200001,
   "totalCount":10,
   "denomination":100.0,
   "totalAmount":1000.0,
   "remainUnPublishAmount":0.0,
   "totalPublishAmount":1000.0,
   "publishedCount":10,
   "totalUsedAmount":0.0,
   "remainUnPublishCount":0,
   "status":"EFFECTIVE",
   "validTo":"2023-12-31T16:00:00Z"
  }
```

`],`

```json
 "requestId":"748326947932***",
 "success":true,
 "pageSize":10,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <total>10</total> <code>200</code> <pageNumber>1</pageNumber> <data> <totalUsedCount>10</totalUsedCount> <couponName>春节红包券</couponName> <resourceMode>PART_AVAILABLE</resourceMode> <gmtModified>2023-12-31T16:00:00Z</gmtModified> <orgRange>[&quot;iaas_test&quot;]</orgRange> <modifier>admin</modifier> <description>仅节日期间可用</description> <orgMode>ALL</orgMode> <validFrom>2023-12-31T16:00:00Z</validFrom> <resourceRange>[&quot;ecs&quot;]</resourceRange> <couponId>200001</couponId> <totalCount>10</totalCount> <denomination>100</denomination> <totalAmount>1000</totalAmount> <remainUnPublishAmount>0</remainUnPublishAmount> <totalPublishAmount>1000</totalPublishAmount> <publishedCount>10</publishedCount> <totalUsedAmount>0</totalUsedAmount> <remainUnPublishCount>0</remainUnPublishCount> <status>EFFECTIVE</status> <validTo>2023-12-31T16:00:00Z</validTo> </data> <requestId>748326947932***</requestId> <success>true</success> <pageSize>10</pageSize> <message>success</message> |  |

##### 4.1.2.35. CreateCouponTemplate

创建优惠券模板。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/createCouponTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| couponName | String | Body | 否 | 新人券 | 优惠券模板名称。 |
| couponType | String | Body | 否 | CASHVOUCHER _ | 优惠券类型，默认代金券 （CASH _VOUCHER）。 |
| validFromDate | String | Body | 否 | 2026-01-01 | 模板有效期开始时间，只需精确到天。 |
| validToDate | String | Body | 否 | 2026-01-31 | 模板有效期结束时间，只需精确到天。 |
| description | String | Body | 否 | 新人无门槛券 | 优惠券描述。 |
| denomination | Float | Body | 否 | 100.00 | 每张优惠券的面额。 |
| totalCount | Long | Body | 否 | 10 | 发放的总数量。 |
| resourceMode | String | Body | 否 | ALL | 适用的资源的模式： ALL：全都可用 PART _AVAILABLE：部分可用 PART _DISABLE：部分不可用 |
| resourceRange | String | Body | 否 | ECS,SLB | 指定可用/不可用的资源。 |
| orgMode | String | Body | 否 | ALL | 适用的组织的模式： ALL：全都可用 PART _AVAILABLE：指定组织可用 |
| orgRange | String | Body | 否 | 1,2,3 | 组织列表。 |
| amountMode | String | Body | 否 | NOLIMIT _ | 是否有金额门槛： HAVE _LIMIT：有金额门槛。 NO _LIMIT：无金额门槛。 |
| amountLimit | Float | Body | 否 | 100.00 | 金额门槛。 |
| activeMode | String | Body | 否 | IMMEDIATELY | 领取后是立即生效还是延迟生效。 SAME _AS _TEMPLATE：同模板有效期 IMMEDIATELY：立即生效 DELAY：延迟若干天生效 FIXED：指定时间生效 |
| activeDelay | Integer | Body | 否 | 3 | 延迟几天生效。 |
| activeFrom | String | Body | 否 | 2026-01-01 | 指定生效开始时间。 |
| activeTo | String | Body | 否 | 2026-01-31 | 指定生效结束时间。 |
| periodAvailable | Integer | Body | 否 | 10 | 有效期持续多长时间。 |
| ruleDesc | String | Body | 是 | 仅新人可用 | 优惠券使用规则。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| data | Boolean | true | true(成功) 或 false(失败)。 |
| message | String | success | 响应的信息。 |
| requestId | String | 3794632643781366273*** | 请求 ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/trade/coupon/admin/createCouponTemplate HTTP/1.1 {
    "couponName": "新人券",
    "couponType": "CASH_VOUCHER",
    "validFromDate": "2026-01-01",
    "validToDate": "2026-01-31",
```

`"description": "`新人无门槛券`",`

```json
    "denomination": 100.00,
    "totalCount": 10,
    "resourceMode": "ALL",
    "resourceRange": "ecs,slb",
    "orgMode": "ALL",
    "orgRange": "1,2,3,4",
    "amountMode": "NO_LIMIT",
    "amountLimit": 0.00,
    "activeMode": "IMMEDIATELY",
    "activeDelay": 0,
    "activeFrom": "2026-01-01",
    "activeTo": "2026-01-31",
    "periodAvailable": 9999999
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"3794632643781366273723", "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>3794632643781366273723</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.36. UpdateCouponTemplate

更新优惠券模板信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/updateCouponTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 否 | 200001 | 优惠券模板ID。 |
| couponName | String | Body | 否 | VIP优惠券 | 优惠券模板名称。 |
| description | String | Body | 否 | 仅VIP可用 | 优惠券描述信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Boolean | true | true(成功) 或 false(失败)。 |
| message | String | success | 响应信息。 |
| requestId | String | 74387643027937479326*** | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/trade/coupon/admin/updateCouponTemplate HTTP/1.1 {
    "id": 200001,
    "couponName": "VIP优惠券",
    "description": "仅VIP可用"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"74387643027937479326***", "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>74387643027937479326***</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.37. DeleteCouponTemplate

删除优惠券模板。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/deleteCouponTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 否 | 20001 | 优惠券模板ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| data | Boolean | true | true(成功) 或 false(失败)。 |
| message | String | success | 响应信息。 |
| requestId | String | 43797493629473924*** | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/trade/coupon/admin/deleteCouponTemplate HTTP/1.1 {
    "id": 20001
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"43797493629473924***", "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>43797493629473924***</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.38. QueryCouponTemplateDetail

查询优惠券模板详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/queryCouponTemplateDetail HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 否 | 200001 | 优惠券模板ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| message | String | success | 响应信息。 |
| requestId | String | 6438647392648732*** | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| data | Struct | - | 响应数据结构体。 |
| -couponId | Long | 200001 | 优惠券模板ID。 |
| -couponName | String | 新人优惠券 | 优惠券模板名称。 |
| -status | String | EFFECTIVE | 优惠券模板状态。 |
| -denomination | Float | 100.00 | 优惠券面额。 |
| -couponType | String | CASHVOUCHER _ | 优惠券类型。CASH _VOUCHER表示代金券。 |
| -validFrom | String | 2019-04-01T15:10:20Z | 模板有效期开始时间。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -validTo | String | 2019-04-02T15:10:20Z | 模板有效期结束时间。 |
| -description | String | 新人无门槛券 | 优惠券描述。 |
| -totalCount | Long | 10 | 发放总数。 |
| -resourceMode | String | ALL | 适用的资源的模式： ALL： 全部可用 PART _AVAILABLE：部分可用 PART _DISABLE：部分不可用 |
| -resourceRange | String | ECS,SLB | 可用/不可用的资源列表。 |
| -orgMode | String | ALL | 适用的组织的模式： ALL：全部可用 PART _AVAILABLE：指定可用 |
| -orgRange | String | 1,2,3,4 | 指定可用的组织ID列表。 |
| -amountMode | String | NOLIMIT _ | 是否有金额门槛： HAVE _LIMIT：有金额门槛。 NO _LIMIT：无金额门槛。 |
| -amountLimit | Float | 1000.00 | 金额门槛。 |
| -activeMode | String | IMMEDIATELY | 是否立即生效。 SAME _AS _TEMPLATE：同模板有效期 IMMEDIATELY：立即生效 DELAY：延迟若干天生效 FIXED：指定时间生效 |
| -activeDelay | Integer | 3 | 延迟几天生效。 |
| -activeFrom | String | 2019-04-01T15:10:20Z | 指定生效开始时间。 |
| -activeTo | String | 2019-05-01T15:10:20Z | 指定生效结束时间。 |
| -periodAvailable | Integer | 10 | 有效期持续几天。 |
| -ruleDesc | String | 仅新用户可用 | 优惠券使用描述信息。 |

**示例**

请求示例

```json
POST /ascm/trade/coupon/admin/queryCouponTemplateDetail HTTP/1.1 {
    "id": 20001
}
```

正常返回示例 `JSON` 格式

```json
{
 "code":"200",
 "data":{
  "amountLimit":1000.0,
```

`"couponName":"`新人优惠券`",`

```json
  "resourceMode":"ALL",
  "orgRange":"1,2,3,4",
```

`"description":"`新人无门槛券`",`

```json
  "activeTo":"2019-05-01T15:10:20Z",
  "periodAvailable":10,
  "validFrom":"2019-04-01T15:10:20Z",
  "orgMode":"ALL",
  "couponId":200001,
  "totalCount":10,
  "resourceRange":"ECS,SLB",
  "denomination":100.0,
  "activeDelay":3,
  "amountMode":"NO_LIMIT",
  "couponType":"CASH_VOUCHER",
```

`"ruleDesc":"`仅新用户可用`",`

```json
  "activeMode":"IMMEDIATELY",
  "activeFrom":"2019-04-01T15:10:20Z",
  "status":"EFFECTIVE",
  "validTo":"2019-04-02T15:10:20Z"
 },
 "requestId":"6438647392648732***",
 "success":true,
 "message":"success"
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <data> <amountLimit>1000</amountLimit> <couponName>新人优惠券</couponName> <resourceMode>ALL</resourceMode> <orgRange>1,2,3,4</orgRange> <description>新人无门槛券</description> <activeTo>2019-05-01T15:10:20Z</activeTo> <periodAvailable>10</periodAvailable> <validFrom>2019-04-01T15:10:20Z</validFrom> <orgMode>ALL</orgMode> <couponId>200001</couponId> <totalCount>10</totalCount> <resourceRange>ECS,SLB</resourceRange> <denomination>100</denomination> <activeDelay>3</activeDelay> <amountMode>NO_LIMIT</amountMode> <couponType>CASH_VOUCHER</couponType> <ruleDesc>仅新用户可用</ruleDesc> <activeMode>IMMEDIATELY</activeMode> <activeFrom>2019-04-01T15:10:20Z</activeFrom> <status>EFFECTIVE</status> <validTo>2019-04-02T15:10:20Z</validTo> </data> <requestId>6438647392648732***</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.39. PublishCouponTemplate

发放优惠券。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/trade/coupon/admin/publishCouponTemplate HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| id | Long | Body | 否 | 200001 | 优惠券模板ID。 |
| publishCount | Integer | Body | 否 | 10 | 本次发放的数量。 |
| orgIdList | RepeatList | Body | 否 | ["3","4"] | 发放给哪些组织。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| data | Boolean | true | true(成功) 或 false(失败)。 |
| message | String | success | 响应信息。 |
| requestId | String | 3829369916873943*** | 请求ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/trade/coupon/admin/publishCouponTemplate HTTP/1.1 {
    "id": 20001,
    "publishCount": 10,
    "orgIdList": ["3", "4"]
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":true, "requestId":"3829369916873943***", "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <requestId>3829369916873943***</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.40. PutMeteringData

产商品管理中三方产品向ASCM主动推送计量数据的接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/metering/custom/product/put/metering/data HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| productCode | String | Body | 否 | custom-resourceCode | 资源类型的resourceType，且该资源类型的计量表来源为OpenAPI接入。 |
| data | String | Body | 否 | { "InsId": "insId-example1", "StartTime": 1756346400, "EndTime": 1756350000, "fieldKey1": "fieldValue1" }, { "InsId": "insId-example2", "StartTime": 1756346400, "EndTime": 1756350000, "fieldKey1": "fieldValue1" } } | 计量数据的json字符串。需要注意的是： 一次请求最多推送100个实例的计量数据。 每个实例的计量数据，除了资源集 ID(ResourceGId)、资源集名称 (ResourceGName)、组织ID(OrgId)、组织名称(OrgName)、地域(RegionId)和计量表版本(TableVersion)这六个字段，其余字段均需要推送。 计量数据中的实例都已经被资源管理所纳管，InsId为该实例在资源管理中的实例ID。 计量数据中的StartTime和EndTime需要是整点的，且开始结束时间相差一小时，时间戳的单位为秒。且一个请求中，所有实例的 StartTime和EndTime都必须是同一计量周期。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态响应码。 |
| cost | Integer | 121 | 接口响应耗时。 |
| message | String | success | 提示信息。 |
| requestId | String | 0a1128a91691**** | 调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/metering/custom/product/put/metering/data HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "requestId":"0a1128a91691****", "success":true, "message":"success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <requestId>0a1128a91691****</requestId> <success>true</success> <message>success</message> |  |

##### 4.1.2.41. QueryBillingCycleSettleStatus

查询计费周期结算状态

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/budget/billSettle/queryBillingCycleSettleStatus HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| billingCycle | String | Body | 是 | 2023-07 | 账期，格式为YYYY-MM |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Integer | 0 | 0：未结算 1：结算中 2：结算成功 -1：结算失败 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```json
POST /ascm/budget/billSettle/queryBillingCycleSettleStatus HTTP/1.1 { "billingCycle":"2023-07" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "data": 0, "success":"true" } |  |

| XML | 格式 |
|---|---|
| <data>0</data> <success>true</success> |  |

##### 4.1.2.42. CreateBillingPushTask

创建账单导入任务。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/import/billingPush/tasks/create HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| startBillingDate | String | Body | 否 | 2025-01-01 | 账单的开始日期。 |
| endBillingDate | String | Body | 否 | 2025-01-15 | 账单的结束日期。 |
| productList | String | Body | 否 | ["custom-custom"] | 要推送的账单的资源列表。 |

billCycle：推送的账单的所属账期。 taskName：导入任务的名字，非必填。未传入则系统自动生成导入任务名字。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 121 | 接口响应耗时。 |
| requestId | String | 0a1128a916917198245846573e* *** | 调用请求的ID。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 返回错误码。 |
| errorMessage | String | 调用API错误。 | 返回错误信息。 |
| token | String | e59f61b2482b4d0562ab542d*** | Token值。 |
| data | Long | 2 | 返回同步任务ID。 |

**示例**

请求示例

```
POST /ascm/billing/import/billingPush/tasks/create HTTP/1.1 { }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "data":2, "requestId":"0a1128a916917198245846573e****", "success":true, "errorMessage":"调用API错误。", "errorCode":"InvalidAccessKeyId.NotFound", "token":"e59f61b2482b4d0562ab542d***" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data>2</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> <errorMessage>调用API错误。</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>e59f61b2482b4d0562ab542d***</token> |  |

##### 4.1.2.43. BatchPushBilling

批量导入推送。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/import/billingPush/tasks/batchPush HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 响应结果。 |
| -failedBillsAndReason | Array | - | 失败的账单和原因。 |
| --reason | String | test | 失败原因。 |
| --bill | Struct | - | 账单。 |
| ---instanceSpec | List | ecs.xn4.small | 实例规格。 |
| ---cloudType | String | default | 云平台类型。 单云或者多云主云为default。 公共云从云为ALIYUN。 专有云从云为Apsara。 |
| ---currency | String | CNY | 账单金额单位，如CNY。 |
| ---cycleType | String | Daily | 账单周期类型。 |
| ---groupByType | String | instance | 账单聚合类型。 |
| ---regionId | String | cn-test | 区域。 |
| ---insId | String | i-f9m05j7zfc7b3mhu**** | 实例ID。 |
| ---orgId | String | 3 | 组织ID。 |
| ---orgName | String | Test | 组织名称。 |
| ---resourceGid | String | 2 | 资源集ID。 |
| ---resourceGroupName | String | ResourceSet(Test) | 资源集名称。 |

| 参数名称 | 类型 | 示例 | 说明 |  |
|---|---|---|---|---|
| ---product | String | custom | 产品。 |  |
| ---startTime | String | 2024-12-31T16:00:00Z | 开始时间。 |  |
| ---endTime | String | 2025-01-01T16:00:00Z | 结束时间。 |  |
| ---price | Float | 100.5 | 价格。 |  |
| ---discountPrice | Float | 10 | 折扣金额。 |  |
| ---originalPrice | Float | 110 | 原价。 |  |
| ---reliefPrice | Float | 5 | 减免金额。 |  |
| ---relievedPrice | Float | 90.5 | 已减免金额。 |  |
| ---roundingAmount | Float | 0.5 | 抹零金额。 |  |
| ---billingChan | String | billingitem1-billingitem2- _ _ _ _ ruleid-planid _ _ | 计费模型ID链信息，包括：计费项1-计费项2-计费项规则ID-计费策略ID-计费计划 ID。 |  |
| ---billingTime | String | 2025-01-01T10:00:00Z | 记账时间。 |  |
| ---modifiedBy | String | user333 _ | 修改人。 |  |
| ---modifiedTime | String | 2025-02-01T10:00:00Z | 修改时间。 |  |
| ---mergeCount | Integer | 1 | 聚合次数。如果账单信息经过聚合，返回聚合的次数。 |  |
| ---billCycle | String | 2025-01-01 | 账期。 |  |
| ---payType | String | postPay | 付费类型。 |  |
| ---instanceSpecDetail | Map | { "ecs.n4.xlarge": [ { "featureValue": "0", "featureName": "GPU数量", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. gpuAmount", "needTrans": false }, { "featureValue": "8.0", "featureName": "内存(GB)", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. memorySize", "needTrans": false }, { "featureValue": "cloud _sperf", "featureName": "磁盘类型", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. systemDisk", "needTrans": false }, { "featureValue": "4", "featureName": "vCPU内核数目", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. cpuCoreCount", "needTrans": false }, { "featureValue": "", "featureName": "GPU类型", "nameTransKey": "csp- cubes.SpecInfo.ecs.InstanceType. gpuSpec", "needTrans": false } ] } | 实例规格属性详情。 |  |
| ---instanceTag | Map | { "EnableHotUpgrade": [ "true" ] } | 实例标签。 |  |
| ---platformCode | String | default | 云平台。 |  |
| ---identifier | String | custom-resource | 云产品。 |  |
| ---identifierGroup | String | compute | 云产品分组。 |  |
| ---financialUnitId | String | financialunit111 _ _ | 实例所属财务单元ID。 |  |
| ---financialName | String | 测试财务单元 | 实例所属财务单元名称。 |  |

| 开发指南 | 参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---paySubType | String | POST | 账单子类型。 |
| ---orderId | String | order444 _ | 订单ID。 |
| -taskId | Long | 2 | 任务ID。 |
| -totalCount | Integer | 2 | 总记录数。 |
| -successCount | Integer | 2 | 成功数量。 |
| -failureCount | Integer | 0 | 失败的数量。 |
| -batchId | Integer | 1 | 批量操作ID。 |
| code | String | 200 | 状态码。 |
| cost | Integer | 121 | 接口响应耗时。 |
| requestId | String | FEB7A954-F07F-45EA-B6A3- 980DD0F9**** | 调用请求的ID。 |
| success | Boolean | true | 接口请求成功标识： true: 成功。 false: 失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 错误码。 |
| errorMessage | String | InternalServerError。 | 返回错误信息。 |
| token | String | eyJhY2NvdW*****VnZpgXQC5A= = | Token值。 |

**示例**

请求示例

```json
POST /ascm/billing/import/billingPush/tasks/batchPush HTTP/1.1 {
    "taskId": 7,
    "pushingBills": [
        {
            "platformCode": "default",
            "currency": "CNY",
            "cycleType": "Daily",
            "groupByType": "instance",
            "product": "custom-lzw",
            "productCode": "ecs",
```

`"productName": "`云服务器`ECS",`

```json
            "meterTableId": "ecs_meter_table",
            "orgId": "3",
            "orgName": "ascmTest",
            "resourceGid": "2",
            "resourceGroupName": "ResourceSet(ascmTest)",
            "regionId": "cn-hangzhou",
            "insId": "i-bp11g50ng545928g5kkkkk",
            "startTime": "2024-12-31T16:00:00Z",
            "endTime": "2025-01-01T16:00:00Z",
            "billCycle": "2025-01-01",
            "payType": "postPay",
            "price": 100.5,
            "discountPrice": 10,
            "relievedPrice": 90.5,
            "reliefPrice": 5,
            "financialUnitId": "financial_unit_111",
```

`"financialName": "`测试财务单元`",`

```json
            "financialUid": "financial_uid_222",
            "originalPrice": 110,
            "billingChan": "billing_item_1-billing_item_2-rule_id-plan_id",
            "billingTime": "2025-01-01T10:00:00Z",
            "modifiedBy": "user_333",
            "modifiedTime": "2025-02-01T10:00:00Z",
            "monthNum": 1,
            "mergeCount": 1,
            "platformType": "public",
            "passThrough": false,
            "identifier": "custom-xiangling-resource",
            "identifierCode": "custom-xiangling-resource",
            "identifierName": "ECS实例",
            "orderId": "order_444",
            "paySubType": "POST",
            "identifierGroup": "compute",
            "billSource": "RULE",
            "publicRevenue": 100,
            "publicCloudCost": 90,
            "publicProfit": 10,
            "roundingAmount": 0.5
        }
```

]

```
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "data":[ { "failedBillsAndReason":[ { "reason":"test", "bill":[ { "resourceGid":"2", "roundingAmount":0.5, "modifiedTime":"2025-02-01T10:00:00Z", "relievedPrice":90.5, "originalPrice":110.0, "paySubType":"POST", "financialName":"测试财务单元", "orderId":"order_444", "discountPrice":10.0, "orgId":"3", "insId":"i-f9m05j7zfc7b3mhu****", "payType":"postPay", "financialUnitId":"financial_unit_111", "billingChan":"billing_item_1-billing_item_2-rule_id-plan_id", "identifierGroup":"compute", "cloudType":"default", "price":100.5, "instanceSpecDetail":{ "ecs n4 xlarge":[ |  |

```json
        ecs.n4.xlarge:[
         {
          "featureValue":"0",
          "featureName":"GPU数量",
          "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.gpuAmount",
          "needTrans":false
         },
         {
          "featureValue":"8.0",
          "featureName":"内存(GB)",
          "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.memorySize",
          "needTrans":false
         },
         {
          "featureValue":"cloud_sperf",
```

`"featureName":"`磁盘类型`",`

```json
          "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.systemDisk",
          "needTrans":false
         },
         {
          "featureValue":"4",
```

`"featureName":"vCPU`内核数目`",`

```json
          "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.cpuCoreCount",
          "needTrans":false
         },
         {
          "featureValue":"",
          "featureName":"GPU类型",
          "nameTransKey":"csp-cubes.SpecInfo.ecs.InstanceType.gpuSpec",
          "needTrans":false
         }
```

]

```json
       },
       "currency":"CNY",
       "startTime":"2024-12-31T16:00:00Z",
       "modifiedBy":"user_333",
       "mergeCount":1,
       "identifier":"custom-resource",
       "product":"custom",
       "orgName":"Test",
       "resourceGroupName":"ResourceSet(Test)",
       "groupByType":"instance",
       "billingTime":"2025-01-01T10:00:00Z",
       "cycleType":"Daily",
       "instanceTag":{
        "EnableHotUpgrade":[
         "true"
```

]

```json
       },
       "reliefPrice":5.0,
       "regionId":"cn-test",
       "instanceSpec":"ecs.xn4.small",
       "endTime":"2025-01-01T16:00:00Z",
       "billCycle":"2025-01-01",
       "platformCode":"default"
      }
```

]

```
    }
```

`],`

```json
   "successCount":2,
   "totalCount":2,
   "batchId":1,
   "taskId":2,
   "failureCount":0
  }
```

`],`

```json
 "requestId":"FEB7A954-F07F-45EA-B6A3-980DD0F9****",
 "success":true,
 "errorMessage":"InternalServerError。",
 "errorCode":"InvalidAccessKeyId.NotFound",
 "token":"eyJhY2NvdW*****VnZpgXQC5A=="
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data> <failedBillsAndReason> <reason>test</reason> <bill> <resourceGid>2</resourceGid> <roundingAmount>0.5</roundingAmount> <modifiedTime>2025-02-01T10:00:00Z</modifiedTime> <relievedPrice>90.5</relievedPrice> <originalPrice>110</originalPrice> <paySubType>POST</paySubType> |  |

`<financialName>`测试财务单元`</financialName>`

```xml
   <orderId>order_444</orderId>
   <discountPrice>10</discountPrice>
   <orgId>3</orgId>
   <insId>i-f9m05j7zfc7b3mhu****</insId>
   <payType>postPay</payType>
   <financialUnitId>financial_unit_111</financialUnitId>
   <billingChan>billing_item_1-billing_item_2-rule_id-plan_id</billingChan>
   <identifierGroup>compute</identifierGroup>
   <cloudType>default</cloudType>
   <price>100.5</price>
   <instanceSpecDetail>
    <ecs.n4.xlarge>
     <featureValue>0</featureValue>
     <featureName>GPU数量</featureName>
     <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.gpuAmount</nameTransKey>
     <needTrans>false</needTrans>
    </ecs.n4.xlarge>
    <ecs.n4.xlarge>
     <featureValue>8.0</featureValue>
     <featureName>内存(GB)</featureName>
     <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.memorySize</nameTransKey>
     <needTrans>false</needTrans>
    </ecs.n4.xlarge>
    <ecs.n4.xlarge>
     <featureValue>cloud_sperf</featureValue>
     <featureName>磁盘类型</featureName>
     <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.systemDisk</nameTransKey>
     <needTrans>false</needTrans>
    </ecs.n4.xlarge>
    <ecs.n4.xlarge>
     <featureValue>4</featureValue>
     <featureName>vCPU内核数目</featureName>
     <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.cpuCoreCount</nameTransKey>
     <needTrans>false</needTrans>
    </ecs.n4.xlarge>
    <ecs.n4.xlarge>
     <featureValue  />
     <featureName>GPU类型</featureName>
     <nameTransKey>csp-cubes.SpecInfo.ecs.InstanceType.gpuSpec</nameTransKey>
     <needTrans>false</needTrans>
    </ecs.n4.xlarge>
   </instanceSpecDetail>
   <currency>CNY</currency>
   <startTime>2024-12-31T16:00:00Z</startTime>
   <modifiedBy>user_333</modifiedBy>
   <mergeCount>1</mergeCount>
   <identifier>custom-resource</identifier>
   <product>custom</product>
   <orgName>Test</orgName>
   <resourceGroupName>ResourceSet(Test)</resourceGroupName>
   <groupByType>instance</groupByType>
   <billingTime>2025-01-01T10:00:00Z</billingTime>
   <cycleType>Daily</cycleType>
   <instanceTag>
    <EnableHotUpgrade>true</EnableHotUpgrade>
   </instanceTag>
   <reliefPrice>5</reliefPrice>
   <regionId>cn-test</regionId>
   <instanceSpec>ecs.xn4.small</instanceSpec>
   <endTime>2025-01-01T16:00:00Z</endTime>
   <billCycle>2025-01-01</billCycle>
   <platformCode>default</platformCode>
  </bill>
 </failedBillsAndReason>
 <successCount>2</successCount>
 <totalCount>2</totalCount>
 <batchId>1</batchId>
 <taskId>2</taskId>
 <failureCount>0</failureCount>
</data> <requestId>FEB7A954-F07F-45EA-B6A3-980DD0F9****</requestId> <success>true</success> <errorMessage>InternalServerError。</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>eyJhY2NvdW*****VnZpgXQC5A==</token>
```

##### 4.1.2.44. UpdateStatusPushFinished

更新状态为推送完成。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/import/billingPush/tasks/updateStatusPushFinished HTTP/1.1
```

taskId：导入任务ID。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 |
| cost | Integer | 121 | 接口耗时。 |
| requestId | String | 0a1128a916917198245846573e* *** | 调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 返回错误码。 |
| errorMessage | String | 调用API错误。 | 返回错误信息。 |
| token | String | eyJhY2NvdW*****VnZpgXQC5A= = | Token值。 |
| data | Boolean | true | 响应结果。 |

**示例**

请求示例

```
POST /ascm/billing/import/billingPush/tasks/updateStatusPushFinished HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "data":true, "requestId":"0a1128a916917198245846573e****", "success":true, "errorMessage":"调用API错误。", "errorCode":"InvalidAccessKeyId.NotFound", "token":"eyJhY2NvdW*****VnZpgXQC5A==" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data>true</data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> <errorMessage>调用API错误。</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>eyJhY2NvdW*****VnZpgXQC5A==</token> |  |

##### 4.1.2.45. QueryBillingPushTaskStatus

查询任务状态。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/billing/import/billingPush/tasks/queryStatus HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 响应结果。 |
| -taskId | Long | 5 | 任务ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -taskStatus | String | CREATED | 任务状态。 |
| code | String | 200 | 状态码。 |
| cost | Integer | 121 | 耗时时间。 |
| requestId | String | 0a1128a916917198245846573e* *** | 调用请求的ID。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| errorCode | String | InvalidAccessKeyId.NotFound | 错误码。 |
| errorMessage | String | InternalServerError | 错误信息。 |
| token | String | eyJhY2NvdW*****VnZpgXQC5A= = | Token值。 |

**示例**

请求示例

```json
POST /ascm/billing/import/billingPush/tasks/queryStatus HTTP/1.1 {
  "taskId" : 5,
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "cost":121, "data":[ { "taskId":5, "taskStatus":"CREATED" } ], "requestId":"0a1128a916917198245846573e****", "success":true, "errorMessage":"InternalServerError", "errorCode":"InvalidAccessKeyId.NotFound", "token":"eyJhY2NvdW*****VnZpgXQC5A==" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <cost>121</cost> <data> <taskId>5</taskId> <taskStatus>CREATED</taskStatus> </data> <requestId>0a1128a916917198245846573e****</requestId> <success>true</success> <errorMessage>InternalServerError</errorMessage> <errorCode>InvalidAccessKeyId.NotFound</errorCode> <token>eyJhY2NvdW*****VnZpgXQC5A==</token> |  |

##### 4.1.2.46. DataCenterSearch

在数据中台环境中检索资源。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /datacenter/action/search HTTP/1.1
```

**入参信息**

| 参数名 | 参数类型 | 是否必填 | 示例 | 说明 |
|---|---|---|---|---|

| sortField | String | 否 | CreateTime __ __ | 排序字段，用于分页查询，可不填。CreateTime：创建时间。 |
|---|---|---|---|---|
| nextToken | String | 否 | *** | 用于游标查询(下一页)，性能好， 但是不返回总数。 |
| previousToken | String | 否 | *** | 用于游标查询(上一页)，性能好， 但是不返回总数。 |
| orderType | String | 否 | desc | 排序类型，默认'asc'，仅对于分页查询及传递了sortFiled参数时才生效。 正向排序逆向排序 |
| returnInstanceDetail | boolean | 否 | true | 是否返回实例详情，默认为true。 仅用于实例查询场景 (type=Instance)。 |
| page | Integer | 否 | 1 | 页码，空或小于1表示游标查询， 分页查询有大小限制，最大返回前 10000个。如果需要全量获取，请使用游标查询(不传page)。 |
| pageSize | Integer | 否 | 10 | 每页数量，默认10，最大1000。 |
| groupConfig | json | 否 | {“groupField”:“Category”,"gro upDocsPage":"1","groupDocsP ageSize":"10","groupPage":"1" ,"groupPageSize":"100"} | groupField：分组字段。支持 Category、ResourceType、 Product和__Type __。 groupPage：分组页，默认1。 groupPageSize：分组页大小，默认10。 groupDocsPage：组内文档页，默认1。 groupDocsPageSize：组内文档页大小，默认100。 |
| returnFields | Set | 否 | [" InstanceId ","" Instance __ __ __ Name "] __ | 指定返回列，该值为空表示返回全部支持版本： 3.16: 3.16.2 SP015及之后 3.18: 3.18.1及之后 |

**出参信息**

实例查询(type=Instance)的出参说明。

| 参数名 | 参数说明 | 备注 |
|---|---|---|
| InstanceId __ __ | 实例ID，可用于过滤排序。 | - |
| InstanceName __ __ | 实例名称，可用于过滤排序。 | 可能为空。 |
| Detail __ __ | 实例详情。 | 通过搜索参数returnInstanceDetail控制，默认返回。 |
| CreateTime _ __ | 实例创建时间，可用于排序。 | - |
| Tag __ __ | 实例标签。 | map格式，如 {"tag1":"v1","tag2":"v2"}。 |
| Ip __ __ | 实例ip列表。 | 例如: ["192.168.***.42","192.168.***.48"]。 |
| IResourceType | 资源类型。 | 如：ecs _instance。 |
| OrganizationId | 组织ID。 | - |
| OrganizationName | 组织名称。 | 如：- |
| ResourceSetId | 资源集ID。 | 如：ecs _instance。 |
| ResourceSetName | 资源集名称。 | 如：ecs _instance。 |
| RegionId | Region ID。 | 如：ecs _instance。 |
| CreateUser | 创建人。 | 如：test。 |

**示例**

请求示例

```json
POST /datacenter/action/search HTTP/1.1 {
    "type":"Instance",
    "resourceTypes": ["disk"],
    "sortField": "__CreateTime__",
    "orderType": "asc",
    "returnInstanceDetail": true,
    "page": 2,
    "pageSize": 5
}
```

正常返回示例 `JSON` 格式

```json
{
    "code": "200",
    "cost": 13,
    "data": {
        "details": [
            {
                "__InstanceName__": "dt_flowtest_SystemDisk",
                "__CreateTime__": "1667975973000",
                "__Detail__": "
{\"DetachedTime\":\"\",\"Category\":\"cloud_pperf\",\"Description\":\"\",\"KMSKeyId\":\"\",\"ResourceGroupId\":\"\",\"Encrypted\":false,\"Size\" "DeleteAutoSnapshot\":false,\"DiskChargeType\":\"PostPaid\",\"MultiAttach\":\"Disabled\",\"Attachments\":{\"Attachment\": [{\"AttachedTime\":\"2022-11-09T06:39:38Z\",\"InstanceId\":\"i-st601kc2exadb4zc6ocx\",\"Device\":\"/dev/xvda\"}]},\"ExpiredTime\":\"2999-09- 08T16:00Z\",\"ImageId\":\"centos_7_6_x86_64_20G_alibase_20211030.vhd\",\"RMRegionId\":\"cn-qingdao-***-d01\",\"StorageSetId\":\"\",\"Tags\":{\ "Tag\":[]},\"Status\":\"In_use\",\"AttachedTime\":\"2022-11-09T06:39:38Z\",\"StorageClusterId\":\"\",\"ZoneId\":\"cn-qingdao-***-amtest66001-a \",\"InstanceId\":\"ist601kc2exadb4zc6ocx\",\"ProductCode\":\"\",\"SourceSnapshotId\":\"\",\"Device\":\"/dev/xvda\",\"PerformanceLevel\":\"\",\"DeleteWithInstance\":t \"EnableAutomatedSnapshotPolicy\":false,\"EnableAutoSnapshot\":true,\"AutoSnapshotPolicyId\":\"\",\"DiskName\":\"dt_flowtest_SystemDisk\",\"Opera Locks\":{\"OperationLock\": []},\"BdfId\":\"\",\"Portable\":false,\"Type\":\"system\",\"SerialNumber\":\"st601kc2exadb4zkfrmc\",\"CreationTime\":\"2022-11- 09T06:39:33Z\",\"RegionId\":\"cn-qingdao-***-d01\",\"DiskId\":\"d-st601kc2exadb4zkfrmc\"}",
                "ResourceType": "disk",
                "OrganizationId": "17",
                "__InstanceId__": "d-st601kc2exadb4zkfrmc",
                "RegionId": "cn-qingdao-***-d01",
                "ResourceSetId": "17"
            }
```

`],`

```json
        "page": 2,
        "pageSize": 5,
        "total": 98
    },
    "message": "success",
    "success": true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>13</cost> <data> <details> <ResourceType>disk</ResourceType> <OrganizationId>17</OrganizationId> <RegionId>cn-qingdao-***-d01</RegionId> <ResourceSetId>17</ResourceSetId> </details> <page>2</page> <pageSize>5</pageSize> <total>98</total> </data> <message>success</message> <success>true</success> |  |

##### 4.1.2.47. DataCenterStatistics

数据中心统计信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /datacenter/action/statistics HTTP/1.1
```

**入参信息**

| 参数名 | 参数类型 | 是否必填 | 示例 | 说明 |
|---|---|---|---|---|

| statisticsField | String | 否 | ResourceType | 默认统计字段： ResourceType：资源类型 Category：分类 OrganizationId：组织 ResourceSetId：资源集 RegionId：Region Product: 后端产品Code Identifier：前端展示产品Code 自定义统计字段：用户自定义统计字段，如实例属性统计。 聚合函数：与统计字段联合使用， 如sum(stroage)，默认为整型数值，通过参数指定类型，如 sum(stroage,float)。 aggregate：所有聚合信息 sum：求和 avg：平均值 min：最小值 max：最大值 |
|---|---|---|---|---|
| statisticsFields | Set | 否 | ["ResourceType","Organizatio n"] | 多维度统计，仅当statisticsField 为空时才生效。 |
| orderType | String | 否 | desc | 排序类型，默认为空，自然返回结果，不做排序。分页场景下最好传递该参数。 asc：根据统计数量正向排序 desc：根据统计数量你想排序 |
| page | Integer | 否 | 1 | 页码，默认为空。不分页，全部返回。 |
| pageSize | Integer | 否 | 10 | 每页数量，默认为空。不分页，全部返回。 |
| timestampSeries | List | 否 | [1658246400000,0] | 该参数仅针对基于序列的统计。0 表示当前时间，列表最大数量为 10。 |
| querySeries | QuerySeries | 否 | {"field":"day", "values": ["2022-07-14", "2022-08- 26"]} | 该参数仅针对基于序列的统计。 |
| groupBy | String | 否 | OrganizationId | 仅用于分组统计。 |

**示例**

请求示例

```json
POST /datacenter/action/statistics HTTP/1.1 {
   "type":"Instance",
   "statisticsField": "ResourceType",
   "resourceSetIds": [3]
}
```

正常返回示例 `JSON` 格式

```json
{
    "code": "200",
    "cost": 2,
    "data": {
        "statistics": [
            {
                "label": "Starting",
                "value": 2
            },
            {
                "label": "Stopping",
                "value": 1
            },
            {
                "label": "Stopped",
                "value": 9
            },
            {
                "label": "Pending",
                "value": 1
            },
            {
                "label": "Running",
                "value": 136
            }
```

`],`

```json
        "statisticsCount": 5,
        "total": 149
    },
    "message": "success",
    "success": true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>2</cost> <data> <statistics> <label>Starting</label> <value>2</value> </statistics> <statistics> <label>Stopping</label> <value>1</value> </statistics> <statistics> <label>Stopped</label> <value>9</value> </statistics> <statistics> <label>Pending</label> <value>1</value> </statistics> <statistics> <label>Running</label> <value>136</value> </statistics> <statisticsCount>5</statisticsCount> <total>149</total> </data> <message>success</message> <success>true</success> |  |

#### 4.1.3. 云产品管理

##### 4.1.3.1. DescribeInstanceTypeFamilies

调用DescribeInstanceTypeFamilies查询云服务器ECS的实例规格族。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/saleconf/ecsSpec/describeInstanceTypeFamilies HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|

| resourceType | String | Body | 否 | ECS | 资源类型，默认为ECS。 |
|---|---|---|---|---|---|
| status | String | Body | 否 | Available | 资源状态。 Available：启用。 Unavailable：未启用。 说明该参数为必填。 |
| groupFiled | String | Body | 否 | "" | 分类字段。 说明该参数已废弃。 |
| zoneId | String | Body | 否 | cn-qingdao-****d01 | 可用区ID。 说明该参数为必填。 |
| deploymentSetId | String | Body | 否 | 1 | 部署集ID。可以通过调用ECS的DescribeDeploymentSets接口获取部署集ID列表。 说明当传入该参数时，会对ECS规格族列表进行筛选，如果某一规格族在ECS DescribeDeploymentSetSupportedInstanceTypeFam ily接口的返回结果中，则该规格族可以在本接口中被返回， 如果不在则不会返回。 |
| specFrom | String | Body | 否 | system | 规格来源类型。 system：系统自动生成。 user：用户自建。 说明若该参数不传则填默认为system。 |
| isReadOnlyRds | String | Body | 否 | true | 是否只读。 说明该参数已废弃。 |
| label | String | Body | 否 | true | 是否返回规格描述。 说明该参数已废弃。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 响应结果。 |
| instanceTypeFamilies | Array of instanceTypeFamilies |  | 云服务器ECS实例规格族信息。 |
| generation | String | "" | Apsara Uni-manager运营控制台请求调用云服务器ECS DescribeInstanceTypeFamilies接口的过程。 说明该参数无实际意义，默认为空。 |
| instanceTypeFamilyId | String | ecs.d1 | 云服务器ECS实例规格族ID。 |
| status | Integer | 200 | 返回状态。 说明该参数已废弃。 |
| success | String | true | 本次接口调用是否成功。 成功：true。 失败：false。 |

**示例**

请求示例

```
POST /ascm/manage/saleconf/ecsSpec/describeInstanceTypeFamilies HTTP/1.1
```

公共请求头

```json
{
    "resourceType":"ECS",
    "status":"Available ",
    "zoneId":"cn-qingdao-****d01"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <data> <instanceTypeFamilies> <generation>""</generation> <instanceTypeFamilyId>ecs.d1</instanceTypeFamilyId> </instanceTypeFamilies> </data> <success>true</success> <status>200</status> |  |

| JSON | 格式 |
|---|---|
| { "data": { "instanceTypeFamilies": { "generation": "\"\"", "instanceTypeFamilyId": "ecs.d1" } }, "success": true, "status": 200 } |  |

##### 4.1.3.2. DescribeModifiableInstanceType

ECS实例可变配规格查询。

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | DescribeModifiableInstanceT ype | 系统规定参数。取值：DescribeModifiableInstanceType。 |
| destinationResource | String | 是 | sfdsf | 取值instanceType。 |
| instanceId | String | 是 | sfdsfsfdsfsfdsf | 实例ID。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 结果集合。 |
| result | Array of dataItem |  | 数据集合。 |
| baselineCredit | Integer | 1 | 突发性能实例t5、t6的基准vCPU计算性能（所有vCPU之和）。 |
| cpuCoreCount | Integer | 1 | vCPU内核数目 |
| eniPrivateIpAddressQuanti ty | Integer | 2 | 单块弹性网卡的私有IP地址上限 |
| eniQuantity | Integer | 2 | 支持挂载的弹性网卡上限 |
| gPUAmount | Integer | 0 | gpu数量 |
| gPUSpec | String | “” | gpu规格 |
| initialCredit | Integer | 1 | 突发性能实例t5、t6的初始vCPU积分值 |
| instanceBandwidthRx | Integer | 1 | 内网入方向带宽限制。单位：kbit/s |
| instanceBandwidthTx | Integer | 1 | 内网出方向带宽限制。单位：kbit/s |
| instanceFamilyLevel | String | EnterpriseLevel | 实例规格族级别 |
| instancePpsRx | Long | 1 | 内网入方向网络收发包能力。单位：Pps |
| instancePpsTx | Long | 1 | 内网出方向网络收发包能力。单位：Pps |

| instanceTypeFamily | String | ecs.sn2.large | InstanceTypeFamily |
|---|---|---|---|
| instanceTypeId | String | ecs.sn2.large | 实例规格ID |
| localStorageAmount | Integer | 1 | 实例挂载的本地盘的数量 |
| localStorageCapacity | Long | 2000 | 实例挂载的本地盘的单盘容量。单位：GiB |
| localStorageCategory | String | 2000 | 实例挂载的本地盘的单盘容量。单位：GiB |
| memorySize | Integer | 4 | 内存大小。单位：GiB |
| status | Integer | 200 | 返回状态。 |
| success | String | true | 成功标示。 |
| host | String | "" | host地址。 |
| status | Integer | 200 | 返回状态。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeModifiableInstanceType &destinationResource=sfdsf &instanceId=sfdsfsfdsfsfdsf
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <data> <result> <instancePpsTx>1</instancePpsTx> <instanceTypeFamily>ecs.sn2.large</instanceTypeFamily> <localStorageCapacity>2000</localStorageCapacity> <instanceTypeId>ecs.sn2.large</instanceTypeId> <instancePpsRx>1</instancePpsRx> <cpuCoreCount>1</cpuCoreCount> <initialCredit>1</initialCredit> <localStorageAmount>1</localStorageAmount> <gPUAmount>0</gPUAmount> <memorySize>4</memorySize> <instanceFamilyLevel>EnterpriseLevel</instanceFamilyLevel> <eniQuantity>2</eniQuantity> <instanceBandwidthRx>1</instanceBandwidthRx> <eniPrivateIpAddressQuantity>2</eniPrivateIpAddressQuantity> <localStorageCategory>2000</localStorageCategory> <instanceBandwidthTx>1</instanceBandwidthTx> <baselineCredit>1</baselineCredit> <gPUSpec>“”</gPUSpec> </result> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |  |

`JSON` 格式

```json
{
    "data": {
        "result": [
            {
                "instancePpsTx": "1",
                "instanceTypeFamily": "ecs.sn2.large",
                "localStorageCapacity": "2000",
                "instanceTypeId": "ecs.sn2.large",
                "instancePpsRx": "1",
                "cpuCoreCount": "1",
                "initialCredit": "1",
                "localStorageAmount": "1",
                "gPUAmount": "0",
                "memorySize": "4",
                "instanceFamilyLevel": "EnterpriseLevel",
                "eniQuantity": "2",
                "instanceBandwidthRx": "1",
                "eniPrivateIpAddressQuantity": "2",
                "localStorageCategory": "2000",
                "instanceBandwidthTx": "1",
                "baselineCredit": "1",
                "gPUSpec": "“”"
            }
```

`],`

```json
        "success": "true",
        "status": "200"
    },
    "host": "\"\"",
    "status": "200"
}
```

##### 4.1.3.3. DescribeSeriesIdFamilies

调用DescribeSeriesIdFamilies查询云原生分布式数据库PolarDB-X 1.0的实例系列。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/saleconf/drdsSpec/describeSeriesIdFamilies HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| resourceType | String | Body | 否 | DRDS | 资源类型，默认为DRDS。 说明该参数为枚举类型，且严格区分大小写。在当前接口下，该参数仅在传入DRDS时才有效，若传入其他值，则无返回数据。 |
| status | String | Body | 否 | Available | 规格状态。 Available：启用。 Unavailable：禁用。规格禁用则无法创建对应规格的DRDS 实例。 |
| label | String | Body | 否 | true | 是否返回实例系列的英文名称。默认为false。 true：返回。 false：不返回。 |

**说明**

若三个请求参数都不填，则返回云原生分布式数据库PolarDB-X 1.0产品所有的实例系列信息。

**返回参数**

**code**：状态码。参数类型：String。
200：调用成功。 500：调用失败。
**data**：返回数据集。参数类型：String。
**creator**：实例的创建者。参数类型：String。
**gmtModified**：实例的创建时间。参数类型：float。
**seriesName**：云原生分布式数据库PolarDB-X 1.0的实例系列的名称。参数类型：String。
**modifier**：实例最后一次修改的修改者。参数类型：String。
**orderBy**：默认根据ID，进行asc方式排序可不关注参数类型：String。
**pageSize**：分页页数，默认为8。参数类型：Integer。
**gmtCreate**：实例系列创建者的用户名。该参数值为虚拟字段，可不做关注。参数类型：String。
**seriesId**：实例系列的ID。参数类型：String。
**deleted**：实例是否已删除。参数类型：Boolean。
false：未删除。 true：已删除。
**pageOrder**：排序方式：asc。参数类型：String。
**isDeleted**：是否删除，N 表示未删除，Y 已删除参数类型：String。
**pageSort**：排序字段，可不做关注。参数类型：String。
**pageStart**：默认起始页，从0开始。参数类型：Integer。
**seriesNameLabel**：实例系列的英文名称。参数类型：String。
**resourceType**：资源类型，为DRDS。参数类型：String。
**httpOk**：是否发送HTTP请求，默认为false。参数类型：Boolean。
**success**：本次接口调用是否成功。参数类型：Boolean。
true：成功。 false失败。
**message**：提示信息。成功提示信息为“describeSeriesIdFamilies success”，失败则提示相应失败信息。参数类型：String。

**示例**

请求示例

```
POST /ascm/manage/saleconf/drdsSpec/describeSeriesIdFamilies HTTP/1.1
```

公共请求头

```json
{
    "resourceType":"DRDS",
    "status":"Available"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <data> <creator>deploy</creator> <gmtModified>1663266761567</gmtModified> <seriesName>drds.sn2.8c32g</seriesName> <modifier>deploy</modifier> <orderBy> <id>ASC</id> </orderBy> <pageSize>8</pageSize> <gmtCreate>1663266761567</gmtCreate> <seriesId>drds.sn2.8c32g</seriesId> <deleted>false</deleted> <pageOrder>ASC</pageOrder> <isDeleted>N</isDeleted> <pageSort>id</pageSort> <pageStart>0</pageStart> <seriesNameLabel>标准版</seriesNameLabel> <resourceType>DRDS</resourceType> </data> <data> <creator>deploy</creator> <gmtModified>1663266761567</gmtModified> <seriesName>drds.sn2.16c64g</seriesName> <modifier>deploy</modifier> <orderBy> <id>ASC</id> </orderBy> <pageSize>8</pageSize> <gmtCreate>1663266761567</gmtCreate> <seriesId>drds.sn2.16c64g</seriesId> <deleted>false</deleted> <pageOrder>ASC</pageOrder> <isDeleted>N</isDeleted> <pageSort>id</pageSort> <pageStart>0</pageStart> <seriesNameLabel>企业版</seriesNameLabel> <resourceType>DRDS</resourceType> </data> <httpOk>false</httpOk> <success>true</success> <message>describeSeriesIdFamilies success</message> |  |

`JSON` 格式

```json
{
    "code": 200,
    "data": [
        {
            "creator": "deploy",
            "gmtModified": 1663266761567,
            "seriesName": "drds.sn2.8c32g",
            "modifier": "deploy",
            "orderBy": {
                "id": "ASC"
            },
            "pageSize": 8,
            "gmtCreate": 1663266761567,
            "seriesId": "drds.sn2.8c32g",
            "deleted": false,
            "pageOrder": "ASC",
            "isDeleted": "N",
            "pageSort": "id",
            "pageStart": 0,
            "seriesNameLabel": "标准版",
            "resourceType": "DRDS"
        },
        {
            "creator": "deploy",
            "gmtModified": 1663266761567,
            "seriesName": "drds.sn2.16c64g",
            "modifier": "deploy",
            "orderBy": {
                "id": "ASC"
            },
            "pageSize": 8,
            "gmtCreate": 1663266761567,
            "seriesId": "drds.sn2.16c64g",
            "deleted": false,
            "pageOrder": "ASC",
            "isDeleted": "N",
            "pageSort": "id",
            "pageStart": 0,
            "seriesNameLabel": "企业版",
            "resourceType": "DRDS"
        }
```

`],`

```json
    "httpOk": false,
    "success": true,
    "message": "describeSeriesIdFamilies success"
}
```

##### 4.1.3.4. GetRegionsByProduct

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/basic/cmdb/region/product HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| identifier | String | Body | 否 | ecs | 产品名称。 说明如果参数identifier的值为空，则返回当前 Region。如果参数identifier的值不为空且该产品没有在任何Region部署，则默认返回中心 Region。 identifier的参数值，可联系阿里云服务支持获取。 |
| organization | String | Body | 否 | 23 | 组织ID。可通过调用GetOrganizationList接口获取。 说明如果organization为空，则返回包含参数 identifier对应产品的所有Region。如果organization不为空，则返回关联了该组织且包含参数identifier对应产品的所有Region。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| body | Struct |  | 返回体。 |
|---|---|---|---|
| RegionList | Array of Region |  | 返回的Region列表。 |
| RegionId | String | cn-qingdao-****-d01 | RegionID信息。 |
| RegionType | String | center | Region类型。 center：中心Region。 cell：单元Region。 |
| code | Integer | 200 | 返回码。 200：调用正常。 500：内部错误。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| successResponse | Boolean | true | 返回是否成功。 |

**示例**

请求示例

```
POST /ascm/basic/cmdb/region/product HTTP/1.1
```

公共请求头

```json
{
    "identifier": ecs,
    "organization": "23"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <successResponse>true</successResponse> <code>200</code> <body> <RegionList> <RegionType>center</RegionType> <RegionId>cn-qingdao-**** -d01</RegionId> </RegionList> </body> |  |

| JSON | 格式 |
|---|---|
| { "successResponse": "true", "code": "200", "body": { "RegionList": [ { "RegionType": "center", "RegionId": "cn-qingdao-**** -d01" } ] } } |  |

##### 4.1.3.5. GroupCommonSpec

**请求参数**

| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|
| Action | String | 是 | GroupCommonSpec | 系统规定参数。取值：GroupCommonSpec。 |
| groupFiled | String | 是 | storageType | 需要获取枚举值的字段。 |
| resourceType | String | 是 | RDS | 资源类型。 |
| label | String | 否 | "" | 标签。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| data | Struct |  | 数据集。 |
| data | List | [ { "storageType":"AutoTestWn4MR _ xEkKK" }, { "storageType":"AutoTestUZOBA _ EDvil" }, { "storageType":"AutoTest8WqAc _ 6rtpp" }, { "storageType":"AutoTestaCPiv2n _ Ih3" }, { "storageType":"Standard" }, { "storageType":"1" } ] | 结果集合。 |
| status | Integer | 200 | 返回状态。 |
| success | String | true | 成功标示。 |
| host | String | "" | host地址。 |
| status | Integer | 200 | 返回状态值。 |

**示例**

请求示例

```
&groupFiled=storageType &resourceType=RDS
```

`&<`公共请求参数> 正常返回示例

| XML | 格式 |
|---|---|
| <data> <data>[ { "storageType":"AutoTest_Wn4MRxEkKK" }, { "storageType":"AutoTest_UZOBAEDvil" }, { "storageType":"AutoTest_8WqAc6rtpp" }, { "storageType":"AutoTest_aCPiv2nIh3" }, { "storageType":"Standard" }, { "storageType":"1" } ]</data> <success>true</success> <status>200</status> </data> <host>""</host> <status>200</status> |  |

| JSON | 格式 |
|---|---|
| { "data": { "data": "[ { \"storageType\":\"AutoTest_Wn4MRxEkKK\" }, { \"storageType\":\"AutoTest_UZOBAEDvil\" }, { \"storageType\":\"AutoTest_8WqAc6rtpp\" }, { \"storageType\":\"AutoTest_aCPiv2nIh3\" }, { \"storageType\":\"Standard\" }, { \"storageType\":\"1\" } ]", "success": "true", "status": "200" }, "host": "\"\"", "status": "200" } |  |

##### 4.1.3.6. InitFromOnline

调用InitFromOnline接口，根据资源类型resourceType在线初始化资源规格。 调用该接口会根据传入的资源类型刷新规格数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/manage/saleconf/commonSpec/initFromOnline HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceType | String | Body | 否 | ECS | 资源类型，当前仅支持以下四种产品。 ECS：云服务器ECS。 ADB：云原生数据仓库AnalyticDB MySQL 版3.0。 SLB：负载均衡SLB。 DRDS：云原生分布式数据库 PolarDB-X。 该参数为必填，且严格区分大小写。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | exampledata | 返回信息。 成功则返回为空值。 失败返回具体信息如下： resourceType is required. resourceType: rds not supported online init spec. |
| success | String | true | 本次调用是否成功 true：成功。 false：失败。 |
| message | String | init ECS success | 同步成功或失败返回的信息。 成功：init ECS success. 失败：提供具体报错信息。 |
| code | String | 200 | 调用code。 200：成功。 500：失败。 |

**示例**

请求示例

```json
POST /ascm/manage/belong/updateInstance HTTP/1.1 { "resourceType":"ECS" }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":"200", "data":"exampledata", "success":"true", "message":"init ECS success" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>exampledata</data> <success>true</success> <message>init ECS success</message> |  |

##### 4.1.3.7. GetAllRegionsInfo

获取本云的全量region相关信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /cmdb/regions/info HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 返回数据。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -zones | Array | - | 返回的可用区列表。 |
| --regionId | String | cn-*****-******-d01 | 可用区所属的地域id。 |
| --zoneId | String | cn-*******-******-a | 可用区的id。 |
| --zoneName | String | cn-*******-******-a | 可用区的名称。 |
| -regionName | String | cn-*****-******-d01 | 地域名称。 |
| -regionId | String | cn-*****-******-d01 | 地域id。 |
| -cloudId | String | cloud-********* | 地域对应的云id。 |
| -isCenter | String | y | 是否为中心region，y表示是中心region，n表示是单元region。 |
| -cloudType | String | private | 云类型，默认为private表示专有云。 |
| code | Integer | 200 | 返回码。 |
| message | String | success | 返回信息。 |
| success | Boolean | true | 请求是否成功，true表示成功，false表示失败。 |
| errorKey | String | null | 错误码。 |

**示例**

请求示例

```
GET /cmdb/regions/info HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":200, "data":{ "isCenter":"y", "regionId":"cn-*****-******-d01", "cloudType":"private", "regionName":"cn-*****-******-d01", "cloudId":"cloud-*********", "zones":{ "regionId":"cn-*****-******-d01", "zoneId":"cn-*******-******-a", "zoneName":"cn-*******-******-a" } }, "success":true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data> <isCenter>y</isCenter> <regionId>cn-*****-******-d01</regionId> <cloudType>private</cloudType> <regionName>cn-*****-******-d01</regionName> <cloudId>cloud-*********</cloudId> <zones> <regionId>cn-*****-******-d01</regionId> <zoneId>cn-*******-******-a</zoneId> <zoneName>cn-*******-******-a</zoneName> </zones> </data> <success>true</success> |  |

##### 4.1.3.8. CloudSearchResources

通用混合云资源搜索接口。支持对多级组织、多云产品、多地域的资源进行统一搜索。只支持租户侧账号调用，不支持服务账号或者主账号进行调用。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /search/resources HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| organizationIds | RepeatList | Body | 否 | [3, 5] | 组织ID列表。 当参数长度为1时，会考虑该组织及子组织， 如[3]。 如果仅希望过滤某一特定组织，不考虑传入组织的子组织，可以在参数后加-1，如[3,-1]。 当参数长度大于1且不为[组织ID, -1]格式时， 仅考虑传入组织，不考虑传入组织的子组织， 如[3,33]。 root组织ID为1，入参中包括root组织则其他传入组织不再生效。 |
| resourceSetIds | RepeatList | Body | 否 | [2, 3] | 资源集ID列表，如果传了resourceSetIds，则以resourceSetIds为准，organizationIds不生效。 |
| regionIds | RepeatList | Body | 否 | ["cn-region-d01","cnregion-02"] | Region列表。 不传会从headers中获取x-acs-regionid。 传[]标识不按照region过滤，单元region只能查到本region的数据。 多云场景，按照从云region过滤需要传入对应的platformCode。 |
| instanceId | String | Body | 否 | 123**** | 实例ID，支持模糊查询。 |
| instanceIds | RepeatList | Body | 否 | ["i-lkjl13413","i-fasfd46546"] | 实例ID列表，只支持精确查询。 |
| instanceName | String | Body | 否 | myinstance | 实例名称，支持模糊查询。 |
| instanceIp | String | Body | 否 | 192.168.**.** | 实例IP，支持模糊查询。 |
| keyword | String | Body | 否 | key | 搜索关键词，实际搜索时会去掉前后空格。 |
| createUser | String | Body | 否 | testuser | 资源创建人。 |
| tagFilters | RepeatList | Body | 否 | - | 标签过滤列表，多个元素为AND关系。 |
| -tagKey | String | Body | 否 | testKey | 标签键。 |
| -tagValues | RepeatList | Body | 否 | TestValue | 标签值列表，每个值都是OR关系。 |
| sortField | String | Body | 否 | InstanceName | 排序字段，resourceTypes为空或者数目大于1 时默认按照创建时间（CreateTime）排序。 |
| orderType | String | Body | 否 | DESC | 排序规则。 DESC：降序，默认。 ASC：升序。 |
| page | Integer | Body | 否 | 1 | 当前页的页码，默认为1。 |
| pageSize | Integer | Body | 否 | 50 | 每页数量，默认为50，最大1000。 |
| returnInstanceDeta il | Boolean | Body | 否 | true | 是否返回实例详细信息的标识，默认为true。 为true时返回详细信息。 为false时返回结果中不包括detail字段。 |
| resourceTypes | RepeatList | Body | 否 | ["vpcinstance"] _ | 资源类型列表，传不存在的资源类型时API会抛错。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| platformCodes | RepeatList | Body | 否 | default | 云平台Code列表，单云场景下忽略， 多云场景下不传查全部，传参一次只能查询一个云平台。 单云或者多云主云为default。 公共云从云、专有云从云为pl-xxxxx。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 |
| message | String | success | 返回提示信息。 |
| requestId | String | a****** | 请求ID。 |
| errorKey | String | ascm.manage.InternalError | 错误码。 |
| data | Struct | - | 响应结果。 |
| -resources | Array | - | 资源列表。 |
| --product | String | ecs | 资源所属产品。 |
| --resourceType | String | vpcinstance _ | 资源类型。 |
| --regionId | String | cn-*****-******-d01 | 地域ID。 |
| --instanceId | String | lb-dw********* | 实例ID。 |
| --instanceName | String | test | 实例名称。 |
| --instanceIp | String | 192.*.*.* | 实例IP地址。 |
| --createTime | Long | 1731406665759 | 创建时间。 |
| --organizationId | Long | 3 | 组织ID。 |
| --resourceSetId | Long | 2 | 资源集ID。 |
| --organizationName | String | orgTest | 组织名称。 |
| --resourceSetName | String | ResourceSet(*****) | 资源集名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --detail | String | {\"Status\":\"Available\",\"IsDefau lt\":false,\"CenStatus\":\"Detache d\",\"Description\":\"\",\"Resource GroupId\":\"rg- acfm3kvxmvd****\",\"VSwitchIds\ ":{\"VSwitchId\":[\"vsw- zb6iacykkmshx7mg8****\",\"vsw- zb6ntnj505v43er2n****\"]},\"Sec ondaryCidrBlocks\": {\"SecondaryCidrBlock\": []},\"CidrBlock\":\"192.*.*.*/16\",\" RouterTableIds\": {\"RouterTableIds\":[\"vtb- zb6qxwp2t47n5mpii****\"]},\"Use rCidrs\":{\"UserCidr\": []},\"NetworkAclNum\":0,\"VRout erId\":\"vrt- zb6an46cvgi1lqk5m****\",\"Adva ncedResource\":false,\"NatGatew ayIds\":{\"NatGatewayIds\": []},\"VpcId\":\"vpc- zb6watlefg6klhaz5****\",\"OwnerI d\":183805211466****,\"Creation Time\":\"2025-08- 07T09:09:18Z\",\"VpcName\":\"高网-test\",\"RegionId\":\"cn-**- d01\",\"Ipv6CidrBlock\":\"\",\"Tags \":{\"Tag\": [{\"Value\":\"tjtest\",\"Key\":\"tjtes t\"}]}} | 资源详细信息，仅入参returnInstanceDetail为true时返回。 |
| --tags | String | {"k1": "v1", "k2": "v2"} | 资源标签，不同云产品格式统一。 |
| --shareType | Long | 0 | 资源共享范围。 0表示本资源集。 1表示本组织及下级组织。 2表示本组织。 |
| --createUser | String | testuser | 资源创建人。 |
| --platformCode | String | default | 云平台Code。 单云或多云主云为default。 公共云从云、专有云从云为pl-xxxxx。 |
| --resourceTypeDesc | String | 专有网络VPC | 资源类型显示名。 |
| --platformName | String | 中心云 | 云平台名称。 |
| --regionName | String | cn-**** | 地域名称。 |
| --cloudType | String | default | 云平台类型。 单云或者多云主云为default。 公共云从云为ALIYUN。 专有云从云为Apsara。 |
| --clusterId | String | c8ca91e0907d94efaba7fb0827eb 9**** | 集群ID。 |
| -page | Integer | 1 | 当前页码。 |
| -pageSize | Integer | 50 | 每页数量。 |
| -total | Integer | 790 | 资源总数。 |

**示例**

请求示例

```
POST /search/resources HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "errorKey":"ascm.manage.InternalError",
 "code":"200",
 "data":{
  "total":790,
  "pageSize":50,
  "page":1,
  "resources":[
   {
    "product":"ecs",
    "organizationName":"orgTest",
    "instanceName":"test",
    "regionName":"cn-****",
    "clusterId":"c8ca91e0907d94efaba7fb0827eb9****",
    "shareType":0,
    "tags":"{\"k1\": \"v1\", \"k2\": \"v2\"}",
    "organizationId":3,
    "resourceTypeDesc":"专有网络VPC",
    "instanceId":"lb-dw*********",
    "regionId":"cn-*****-******-d01",
    "createTime":1731406665759,
    "cloudType":"default",
    "resourceSetName":"ResourceSet(*****)",
    "createUser":"testuser",
    "detail":"
{\\\"Status\\\":\\\"Available\\\",\\\"IsDefault\\\":false,\\\"CenStatus\\\":\\\"Detached\\\",\\\"Description\\\":\\\"\\\",\\\"ResourceGroupId\\\ "rg-acfm3kvxmvd****\\\",\\\"VSwitchIds\\\":{\\\"VSwitchId\\\":[\\\"vsw-zb6iacykkmshx7mg8****\\\",\\\"vswzb6ntnj505v43er2n****\\\"]},\\\"SecondaryCidrBlocks\\\":{\\\"SecondaryCidrBlock\\\": []},\\\"CidrBlock\\\":\\\"192.*.*.*/16\\\",\\\"RouterTableIds\\\":{\\\"RouterTableIds\\\":[\\\"vtbzb6qxwp2t47n5mpii****\\\"]},\\\"UserCidrs\\\":{\\\"UserCidr\\\":[]},\\\"NetworkAclNum\\\":0,\\\"VRouterId\\\":\\\"vrtzb6an46cvgi1lqk5m****\\\",\\\"AdvancedResource\\\":false,\\\"NatGatewayIds\\\":{\\\"NatGatewayIds\\\":[]},\\\"VpcId\\\":\\\"vpczb6watlefg6klhaz5****\\\",\\\"OwnerId\\\":183805211466****,\\\"CreationTime\\\":\\\"2025-08-07T09:09:18Z\\\",\\\"VpcName\\\":\\\"高网test\\\",\\\"RegionId\\\":\\\"cn-**-d01\\\",\\\"Ipv6CidrBlock\\\":\\\"\\\",\\\"Tags\\\":{\\\"Tag\\\": [{\\\"Value\\\":\\\"tjtest\\\",\\\"Key\\\":\\\"tjtest\\\"}]}}",
    "resourceSetId":2,
    "platformName":"中心云",
    "platformCode":"default",
    "resourceType":"vpc_instance",
    "instanceIp":"192.*.*.*"
   }
```

]

```json
 },
 "success":true,
 "requestId":"a******",
 "message":"success"
}
```

`XML` 格式

```xml
<errorKey>ascm.manage.InternalError</errorKey> <code>200</code> <data>
 <total>790</total>
 <pageSize>50</pageSize>
 <page>1</page>
 <resources>
  <product>ecs</product>
  <organizationName>orgTest</organizationName>
  <instanceName>test</instanceName>
  <regionName>cn-****</regionName>
  <clusterId>c8ca91e0907d94efaba7fb0827eb9****</clusterId>
  <shareType>0</shareType>
  <tags>{&quot;k1&quot;: &quot;v1&quot;, &quot;k2&quot;: &quot;v2&quot;}</tags>
  <organizationId>3</organizationId>
  <resourceTypeDesc>专有网络VPC</resourceTypeDesc>
  <instanceId>lb-dw*********</instanceId>
  <regionId>cn-*****-******-d01</regionId>
  <createTime>1731406665759</createTime>
  <cloudType>default</cloudType>
  <resourceSetName>ResourceSet(*****)</resourceSetName>
  <createUser>testuser</createUser>
  <detail>
{\&quot;Status\&quot;:\&quot;Available\&quot;,\&quot;IsDefault\&quot;:false,\&quot;CenStatus\&quot;:\&quot;Detached\&quot;,\&quot;Description\&qu \&quot;\&quot;,\&quot;ResourceGroupId\&quot;:\&quot;rg-acfm3kvxmvd****\&quot;,\&quot;VSwitchIds\&quot;:{\&quot;VSwitchId\&quot;:[\&quot;vsw-zb 6iacykkmshx7mg8****\&quot;,\&quot;vsw-zb6ntnj505v43er2n****\&quot;]},\&quot;SecondaryCidrBlocks\&quot;:{\&quot;SecondaryCidrBlock\&quot;: []},\&quot;CidrBlock\&quot;:\&quot;192.*.*.*/16\&quot;,\&quot;RouterTableIds\&quot;:{\&quot;RouterTableIds\&quot;:[\&quot;vtbzb6qxwp2t47n5mpii****\&quot;]},\&quot;UserCidrs\&quot;:{\&quot;UserCidr\&quot;: []},\&quot;NetworkAclNum\&quot;:0,\&quot;VRouterId\&quot;:\&quot;vrtzb6an46cvgi1lqk5m****\&quot;,\&quot;AdvancedResource\&quot;:false,\&quot;NatGatewayIds\&quot;:{\&quot;NatGatewayIds\&quot;: []},\&quot;VpcId\&quot;:\&quot;vpc-zb6watlefg6klhaz5****\&quot;,\&quot;OwnerId\&quot;:183805211466****,\&quot;CreationTime\&quot;:\&quot;2025- 08-07T09:09:18Z\&quot;,\&quot;VpcName\&quot;:\&quot;高网-test\&quot;,\&quot;RegionId\&quot;:\&quot;cn-**d01\&quot;,\&quot;Ipv6CidrBlock\&quot;:\&quot;\&quot;,\&quot;Tags\&quot;:{\&quot;Tag\&quot;: [{\&quot;Value\&quot;:\&quot;tjtest\&quot;,\&quot;Key\&quot;:\&quot;tjtest\&quot;}]}}</detail>
  <resourceSetId>2</resourceSetId>
  <platformName>中心云</platformName>
  <platformCode>default</platformCode>
  <resourceType>vpc_instance</resourceType>
  <instanceIp>192.*.*.*</instanceIp>
 </resources>
</data> <success>true</success> <requestId>a******</requestId> <message>success</message>
```

##### 4.1.3.9. CloudUpdateResource

通用混合云资源更新接口。只支持租户侧账号调用，不支持服务账号或者主账号进行调用。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /update/resource HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| resourceType | String | Body | 是 | ecsinstance _ | 资源类型。 说明此参数必填。 |
| resourceId | String | Body | 是 | i-a8u00nuf7a3dlx9r**** | 资源ID。 说明此参数必填。 |
| resourceRegionId | String | Body | 是 | cn-**** | 资源地域ID。 说明此参数必填。 |
| deletedFlag | String | Body | 否 | false | 资源逻辑删除操作。不传默认更新。 true：删除。 false：更新。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| code | String | 200 | 状态码。 |
| message | String | success | 返回提示信息。 |
| requestId | String | 530dxxx-dxx******-x6b61axxxxx | 请求ID。 |
| errorKey | String | ascm.manage.InternalError | 错误码。 |

**示例**

请求示例

```json
POST /update/resource HTTP/1.1 {
    "resourceType":"ecs_instance",
    "resourceId":"i-a8u00nuf7a3dlx9r****",
    "resourceRegionId":"cn-****",
    "deletedFlag":"false"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "errorKey":"ascm.manage.InternalError", "code":"200", "success":true, "requestId":"530dxxx-dxx******-x6b61axxxxx", "message":"success" } |  |

| XML | 格式 |
|---|---|
| <errorKey>ascm.manage.InternalError</errorKey> <code>200</code> <success>true</success> <requestId>530dxxx-dxx******-x6b61axxxxx</requestId> <message>&quot;success&quot;</message> |  |

#### 4.1.4. 配置中心

##### 4.1.4.1. EditResourceAccountPlatform

接入资源账号。 只允许平台管理员和绑定了公共云的运营管理员调用该接口。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /platforms/edit/resource/account HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| platformType | String | Body | 否 | ALIYUN | 资源池类型。 |
| displayName | String | Body | 否 | testuser | 资源账号名称。 |
| account | String | Body | 否 | 123 | 资源账号id。 |
| parentPlatformCod e | String | Body | 否 | pl-a | 管理账号code。 |
| description | String | Body | 否 | test | 账号说明。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 响应结果。 |
| -platformId | String | 1 | 资源池ID。 |
| -code | String | ALIYUN | 资源池类型code。 |
| -logo | String | a.png | 资源池图标。 |
| -displayName | String | test | 资源池名称。 |
| -account | String | 16********** | 账号id。 |
| -gmtCreate | Long | 1703575552000 | 创建时间。 |
| -gmtModified | Long | 1770028091941 | 修改时间。 |
| -status | Integer | 100 | 接入状态。 |
| -disabled | Boolean | false | 资源池是否禁止选择，true表示禁止选择，false表示允许选择，默认为false。 |
| -deleteDisabled | Boolean | false | 资源池是否禁止删除，true表示禁止删除，false表示允许删除。 |
| -enableStatus | Integer | 1 | 资源池启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| -bound | Boolean | false | 资源池是否被绑定。 true：表示被绑定过。 false：表示未被绑定过。 |
| -allowMulTopOrgMapping | Boolean | false | 是否允许多一级组织映射同一个平台，true表示允许，false表示不允许。 |
| -accountType | String | managerAccount | 资源池类型。 |
| -description | String | 测试数据。 | 资源池说明信息，最长256个字符 |
| -platformType | Struct | {} | 资源池类型。 |
| --code | String | ALIYUN | 资源池类型code。 |
| --displayName | String | 公共云 | 资源池类型显示名称。 |
| --enterprise | Boolean | true | 是否为专有云。 true：专有云。 false：非专有云。 |
| --platformType | String | ALIYUN | 资源池类型： Apsara：表示专有云。 ALIYUN：表示公共云。 |
| -config | Struct | {} | 资源池配置。 |
| --cloudUniqueId | String | 123 | 资源池实例id，如果是专有云则为专有云实例id，如果是公共云则为公共云主账号 UID。 |
| --cloudVersion | String | Enterprisev3***** _ | 资源池的版本，专有云的版本，公共云则为空。 |
| --defaultRegion | String | cn-***** | 默认的地域。 |
| --consoleEndpoint | String | a.com | 专有云OneConsole的Endpoint。公共云为空。 |
| --authentication | Struct | {} | 认证配置。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---metadataUrl | String | http://******.xml | SSO元数据的URL链接。 |
| ---type | String | saml | SSO认证类型，默认为SAML协议。 |
| -connectStatus | Struct | {} | 资源池连通状态。 |
| --id | Long | 29 | 资源池连接状态ID。 |
| --platformId | Long | 123 | 资源池ID。 |
| --endpointStatus | Integer | 1 | 资源池网络连接状态。 1：正常。 0：异常。 |
| --credentialStatus | Integer | 1 | 资源池凭证状态。 1：正常。 0：异常。 |
| --message | String | error | 异常信息。 |
| --updateTime | String | 2026-03-27T07:16:15.000+00:00 | 连接状态更新时间。 |
| -parentPlatform | Struct | {} | 管理账号信息。 |
| --account | String | 16********** | 管理账号ID。 |
| --platformCode | String | pl-xxx | 管理账号的资源池code。 |
| --displayName | String | 公共云 | 资源池类型显示名称。 |
| --accountType | String | managerAccount | 资源池类型。 |
| --enableStatus | Integer | 1 | 平台启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| --platformType | Struct | ALIYUN | 资源池类型： Apsara：表示专有云。 ALIYUN：表示公共云。 |
| ---code | String | ALIYUN | 资源池类型的code： Apsara：专有云。 ALIYUN：公共云。 |
| ---displayName | String | 公共云 | 资源池类型显示名称。 |
| ---enterprise | Boolean | false | 是否为专有云。 true：专有云。 false：非专有云。 |
| ---platformType | String | ALIYUN | 资源池类型。 |

**示例**

请求示例

```
POST /platforms/edit/resource/account HTTP/1.1 {
```

`"parentPlatformCode":"`所属管理账号的平台`code",`

```json
  "platformType":"ALIYUN",
```

`"displayName": "`新建资源账号的显示名`",` `"description": "`新建资源账号的说明`",`

```json
  "accountType": "RESOURCE_ACCOUNT"
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":{
  "gmtModified":1770028091941,
  "code":"ALIYUN",
  "allowMulTopOrgMapping":false,
  "displayName":"test",
  "bound":false,
  "accountType":"managerAccount",
```

`"description":"`测试数据。`",`

```json
  "platformId":"1",
  "gmtCreate":1703575552000,
  "deleteDisabled":false,
  "platformType":{
   "code":"ALIYUN",
   "displayName":"公共云",
   "enterprise":true,
   "platformType":"ALIYUN"
  },
  "connectStatus":{
   "endpointStatus":1,
   "updateTime":"2026-03-27T07:16:15.000+00:00",
   "id":29,
   "platformId":123,
   "message":"error",
   "credentialStatus":1
  },
  "parentPlatform":{
   "displayName":"公共云",
   "accountType":"managerAccount",
   "platformType":{
    "code":"ALIYUN",
    "displayName":"公共云",
    "enterprise":false,
    "platformType":"ALIYUN"
   },
   "enableStatus":1,
   "account":"16**********",
   "platformCode":"pl-xxx"
  },
  "config":{
   "cloudUniqueId":"123",
   "cloudVersion":"Enterprise_v3*****",
   "authentication":{
    "metadataUrl":"http://******.xml",
    "type":"saml"
   },
   "defaultRegion":"cn-*****",
   "consoleEndpoint":"a.com"
  },
  "logo":"a.png",
  "disabled":false,
  "enableStatus":1,
  "account":"16**********",
  "status":100
 }
}
```

`XML` 格式

```xml
<data>
 <gmtModified>1770028091941</gmtModified>
 <code>ALIYUN</code>
 <allowMulTopOrgMapping>false</allowMulTopOrgMapping>
 <displayName>test</displayName>
 <bound>false</bound>
 <accountType>managerAccount</accountType>
```

`<description>`测试数据。`</description>`

```xml
 <platformId>1</platformId>
 <gmtCreate>1703575552000</gmtCreate>
 <deleteDisabled>false</deleteDisabled>
 <platformType>
  <code>ALIYUN</code>
  <displayName>公共云</displayName>
  <enterprise>true</enterprise>
  <platformType>ALIYUN</platformType>
 </platformType>
 <connectStatus>
  <endpointStatus>1</endpointStatus>
  <updateTime>2026-03-27T07:16:15.000+00:00</updateTime>
  <id>29</id>
  <platformId>123</platformId>
  <message>error</message>
  <credentialStatus>1</credentialStatus>
 </connectStatus>
 <parentPlatform>
  <displayName>公共云</displayName>
  <accountType>managerAccount</accountType>
  <platformType>
   <code>ALIYUN</code>
   <displayName>公共云</displayName>
   <enterprise>false</enterprise>
   <platformType>ALIYUN</platformType>
  </platformType>
  <enableStatus>1</enableStatus>
  <account>16**********</account>
  <platformCode>pl-xxx</platformCode>
 </parentPlatform>
 <config>
  <cloudUniqueId>123</cloudUniqueId>
  <cloudVersion>Enterprise_v3*****</cloudVersion>
  <authentication>
   <metadataUrl>http://******.xml</metadataUrl>
   <type>saml</type>
  </authentication>
  <defaultRegion>cn-*****</defaultRegion>
  <consoleEndpoint>a.com</consoleEndpoint>
 </config>
 <logo>a.png</logo>
 <disabled>false</disabled>
 <enableStatus>1</enableStatus>
 <account>16**********</account>
 <status>100</status>
</data>
```

##### 4.1.4.2. BatchCreateRAMServiceRole

调用BatchCreateRAMServiceRole接口批量创建RAM服务角色。创建成功可通过ListRAMServiceRoles接口查询。 RAM服务角色主要在受信的云服务访问或操作其他云资源时使用。 用户创建云产品时，若该云产品需要访问其它云产品服务，系统则会默认为该云产品创建对应的RAM服务角色，该RAM服务角色隶属于创建云产品时所选组织的一级组织下。 例如，云服务器ECS需要创建对象存储OSS Bucket来提供存储镜像的能力，其原理是ECS通过扮演OSS提供的RAM服务角色，将OSS的操作权限策略默认授权给该RAM角色，从而得到操作OSS资源的权限点。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/ramServiceRole/batchCreateRAMServiceRole HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|

| organizationIdList.N | RepeatList | Body | 否 | ["14","18","19","21","23"," 24"] | 组织ID列表，多个组织ID之间使用英文逗号隔开。组织ID可通过调用GetOrganizationTree接口获取。 说明该参数为必填。 |
|---|---|---|---|---|---|
| productName | String | Body | 否 | NAS | 产品名称，可通过调用ListRAMServiceRoleProducts接口获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 22 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 true：重定向。 false：不重定向。 |

| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
|---|---|---|---|

**示例**

请求示例

```
POST /ascm/auth/ramServiceRole/batchCreateRAMServiceRole HTTP/1.1
```

公共请求头

```json
{
    "organizationIdList.N":"["14","18","19","21","23","24"]",
    "productName":"NAS"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>11</cost> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 11, "success": true, "message": "success" } |  |

##### 4.1.4.3. GetPasswordPolicy

调用GetPasswordPolicy获取Apsara Uni-manager运营控制台当前的密码策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

无

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 500：服务内部错误，发生未识别的异常时会返回此错误码。 |
| cost | Integer | 5 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 密码策略数据。 |
| hardExpiry | Boolean | true | 密码是否过期。 true：过期，过期后用户不能登录Apsara Uni-manager运营控制台。 false：不过期。 说明可通过maxPasswordAge参数了解密码有效期，用户需要在有效期结束前及时更新密码。若密码已过期，需要联系运营管理员或平台管理员重置密码。 |
| maxLoginAttemps | Integer | 5 | 密码错误容忍周期内使用错误密码尝试登录的最大次数。 说明取值范围0~32。 |

| maxPasswordAge | Integer | 90 | 密码有效期，单位：天。0表示不启用密码过期策略。 说明取值范围0~1095。 |
|---|---|---|---|
| minimumPasswordLength | Integer | 10 | 最小密码长度。 说明取值范围8~32。 |
| passwordErrorCaptchaTim e | Integer | 3 | 触发人机验证（验证码）校验的密码错误次数。 |
| passwordErrorLockPeriod | Integer | 30 | 账号冷冻时长，单位：分钟。 说明若超过密码输入错误次数，则进入账号冷冻期，冷冻期内不能进行登录。取值范围0~1440。 |
| passwordErrorToleranceP eriod | Integer | 60 | 密码错误容忍周期，默认为60分钟，即60分钟内容忍密码输错N次。可通过 maxLoginAttemps参数了解密码错误容忍周期内密码错误输入的次数。 |
| passwordReusePrevention | Integer | 5 | 禁止使用前N次密码。0表示不启用历史密码检查策略，默认不启用。 说明取值范围0~24。 |
| requireLowercaseCharact ers | Boolean | true | 密码中是否必须包含小写英文字母元素。 |
| requireNumbers | Boolean | true | 密码中是否必须包含阿拉伯数字元素。 |
| requireSymbols | Boolean | true | 密码中是否必须包含特殊符号元素。 |
| requireUppercaseCharact ers | Boolean | true | 密码中是否必须包含大写英文字母元素。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 说明该参数已废弃。 |
| success | Boolean | true | 是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例公共请求头

```
{ }
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>5</cost> <data> <passwordErrorTolerancePeriod>60</passwordErrorTolerancePeriod> <passwordErrorCaptchaTime>3</passwordErrorCaptchaTime> <minimumPasswordLength>10</minimumPasswordLength> <requireSymbols>true</requireSymbols> <passwordErrorLockPeriod>30</passwordErrorLockPeriod> <passwordReusePrevention>5</passwordReusePrevention> <maxLoginAttemps>5</maxLoginAttemps> <requireLowercaseCharacters>true</requireLowercaseCharacters> <hardExpiry>true</hardExpiry> <requireNumbers>true</requireNumbers> <maxPasswordAge>90</maxPasswordAge> <requireUppercaseCharacters>true</requireUppercaseCharacters> </data> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 5, "data": { "passwordErrorTolerancePeriod": 60, "passwordErrorCaptchaTime": 3, "minimumPasswordLength": 10, "requireSymbols": true, "passwordErrorLockPeriod": 30, "passwordReusePrevention": 5, "maxLoginAttemps": 5, "requireLowercaseCharacters": true, "hardExpiry": true, "requireNumbers": true, "maxPasswordAge": 90, "requireUppercaseCharacters": true }, "success": true, "message": "success" } |  |

##### 4.1.4.4. ListRAMPolicies

获取RAM权限策略列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| policyName | String | Body | 否 | testPolicy | RAM权限策略名称。 说明按照传入的字符串进行模糊查询，若不传则返回全部策略。 |
| description | String | Body | 否 | test | RAM权限策略的描述信息。 说明按照传入的字符串进行模糊查询，若不传则查询结果不通过该参数进行过滤。 |
| roleId | Integer | Body | 否 | 2 | 角色ID，可通过ListRoles接口获取。 说明若不传则查询结果不通过角色ID过滤。 |

| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
|---|---|---|---|---|---|
| pageSize | Integer | Body | 否 | 10 | 分页大小，默认为10 ，即每页10条。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 404：角色不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of itemData |  | 响应结果。 |
| ctime | Long | 1607512443989 | RAM权限策略的创建时间。 |
| id | Integer | 1 | RAM权限策略ID。 |
| mtime | Long | 1607512443999 | RAM权限策略最近一次修改的时间。 |
| muserId | String | admin | 最近一次修改的修改者用户名。 |
| policyDocument | String | a | RAM权限策略的内容。 |
| policyName | String | testpolicy _ | RAM权限策略名称。 |
| region | String | cn-qingdao-****-d01 | RAM权限策略的可用区。 |
| message | String | success | 错误提示信息。 success：调用成功。 Forbidden：没有权限。 NotExist：角色不存在。 InternalServerError：内部错误。 |
| pageInfo | Struct |  | 分页信息。 |
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 5 | 每页大小。 |
| total | Integer | 10 | 返回记录总数。 |
| totalPage | Integer | 2 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例公共请求头

```json
{
    "policyName":"testPolicy",
    "description":"test",
    "roleId":2,
    "currentPage":1,
    "pageSize":10
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <data> <policyDocument>a</policyDocument> <muserId>admin</muserId> <policyName>test_policy</policyName> <ctime>1607512443989</ctime> <id>1</id> <region>cn-qingdao-****-d01</region> <mtime>1607512443999</mtime> </data> <success>true</success> <pageInfo> <total>10</total> <totalPage>2</totalPage> <pageSize>5</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 10000, "code": 200, "data": { "policyDocument": "a", "muserId": "admin", "policyName": "test_policy", "ctime": 1607512443989, "id": 1, "region": "cn-qingdao-****-d01", "mtime": 1607512443999 }, "success": true, "pageInfo": { "total": 10, "totalPage": 2, "pageSize": 5, "currentPage": 1 }, "message": "success" } |  |

##### 4.1.4.5. ListRAMPoliciesForUser

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/dataPrivilege/listRAMPoliciesForUser HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| loginName | String | Body | 否 | testu | 用户登录名。以用户登录名精准查找该用户所绑定的RAM策略。 说明该参数为必填。 |

**返回参数**

**redirect**：是否重定向。参数类型：Boolean。
true：重定向。 false：不重定向。
**cost**：接口耗时，单位毫秒（ms）。参数类型：String。
**code**：状态码。参数类型：String。
200：调用成功。 403：没有权限。 404：角色不存在。 500：内部错误。
**data**：响应结果。参数类型：Array of itemData。
**policyDocument**：RAM权限策略的内容。参数类型：String。
**policyName**：RAM权限策略名称。参数类型：float。
**attachDate**：用户与RAM权限策略绑定的日期。参数类型：String。
**policyType**：策略类型。参数类型：String。
**description**：策略描述信息。参数类型：String。
**defaultVersion**：策略默认版本。参数类型：String。
**success**：本次接口调用是否成功。参数类型：Boolean。
true: 成功。 false: 失败是否成功。
**message**：错误提示信息。参数类型：String。
success：调用成功。 Forbidden：没有权限。 NotExist：角色不存在。 InternalServerError：内部错误。

**示例**

请求示例

```
POST /ascm/auth/dataPrivilege/listRAMPoliciesForUser HTTP/1.1
```

公共请求头

```json
{
    "loginName": "testu"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>200</cost> <code>200</code> <data> <policyDocument>{ "Statement": [{ "Action": ["oss:*"], "Effect": "Allow", "Resource": ["acs:oss:*:*:*"]}], "Version": "1"} </policyDocument> <policyName>testp</policyName> <attachDate>1663312000943</attachDate> <policyType>Custom</policyType> <description>policy for oss</description> <defaultVersion>v1</defaultVersion> </data> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 200, "code": 200, "data": { "policyDocument": "{ \"Statement\": [{ \"Action\": [\"oss:*\"], \"Effect\": \"Allow\", \"Resource\": [\"acs:oss:*:*:*\"]}], \"Version\" : \"1\"}", "policyName": "testp", "attachDate": 1663312000943, "policyType": "Custom", "description": "policy for oss", "defaultVersion": "v1" }, "success": true, "message": "success" } |  |

##### 4.1.4.6. ListRAMServiceRoles

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/role/listRAMServiceRoles HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| regionName | String | Body | 否 | test-region | 可用区。 说明该参数已废弃。 |
| productName | String | Body | 否 | ecs | 服务名称。 说明传入服务名称，则返回该服务相关的RAM服务角色。若请求参数都不传，则返回所有RAM服务角色。若同时传入所有请求参数，则返回符合所有条件的RAM服务角色。 |
| roleName | String | Body | 否 | testr | RAM服务角色名称。 说明传入此参数会根据RAM服务角色名称进行模糊查询，返回 RAM服务角色名称中包含该参数值的RAM服务角色。 |
| organizationId | Integer | Body | 否 | 3 | RAM服务角色所属组织的ID。可通过调用GetOrganizationList 接口获取。 说明传入该参数则根据组织ID精确查找属于该组织下的RAM服务角色。 |
| currentPage | Integer | Body | 否 | 1 | 分页页码，默认为1。 |
| pageSize | Integer | Body | 否 | 10 | 分页大小，默认为10，即每页10条返回数据。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 403：没有权限。 404：用户/组织不存在。 500：内部错误。 |
| cost | Integer | 10000 | 接口响应耗时，单位毫秒（ms）。 |
| data | Array of itemData |  | 响应结果。 |
| aliyunUserId | Integer | 12 | 阿里云账号（主账号）ID。 |
| arn | String | acs:ram::123456789012****:role/ ECSAdmin | 角色的资源描述符。 |
| assumeRolePolicyDocume nt | String | {"Statement": [{"Action": "sts:testAction", "Effect": "Allow", "Principal": {"Service": ["***.aliyuncs.com"]}}], "Version": "1"} | RAM服务角色信任策略的内容。 说明策略内容为JSON格式。 |

| description | String | ECS管理角色 | RAM服务角色的描述。 |
|---|---|---|---|
| id | Integer | 1 | RAM服务角色ID。 |
| organizationId | Integer | 1 | RAM服务角色所属组织的ID。 |
| organizationName | String | organizationtest _ | RAM服务角色所属组织的名称。 |
| policies | Array of itemPolicy |  | RAN服务角色的角色策略。 说明该参数及其子节点参数已全部废弃。 |
| aliyunUserId | Integer | 1 | 阿里云账号（主账号）ID。 |
| ascmRamPolicyId | Integer | 1 | RAM策略ID。 |
| attachDate | Long | 1607512443989 | 策略绑定日期。 |
| defaultVersion | String | 1.0 | 策略默认版本 |
| description | String | "" | 策略描述信息 |
| id | Integer | 1 | 策略自增ID |
| policyDocument | String | "" | 策略内容。 |
| policyName | String | "" | 策略名称。 |
| policyType | String | "" | 策略类型。 |
| privilegeId | Integer | 1 | 权限点ID。 |
| ramGroupId | Integer | 1 | ram用户组ID。 |
| ramRoleId | Integer | 1 | ram角色ID。 |
| region | String | "" | 地域。 |
| resourceSetId | Integer | 1 | 资源集ID。 |
| product | String | ecs | RAM服务角色绑定的服务名称。 |
| region | String | cn-qingdao-****-d01 | RAM服务角色所在的地域。 |
| roleId | String | 39405704233030**** | 角色ID。 说明 RAM服务侧的角色ID。 |
| roleName | String | AliyunECS****DefaultRole | RAM服务角色的名称。 |
| roleType | String | System | RAM服务角色的类型。 System：系统定义类型。 Custom：自定义类型。 |
| message | String | success | 错误提示信息。 success：调用成功。 Forbidden：没有权限。 NotExist：用户/组织不存在。 InternalServerError：内部错误。 |

| pageInfo | Struct |  | 分页信息。 |
|---|---|---|---|
| currentPage | Integer | 1 | 当前页数。 |
| pageSize | Integer | 5 | 每页返回数据条数。 |
| total | Integer | 10 | 返回数据总条数。 |
| totalPage | Integer | 2 | 总页数。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |
| success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/role/listRAMServiceRoles HTTP/1.1
```

公共请求头

```json
{
    "regionName","test-region",
    "productName":"ecs",
    "roleName","testr",
    "organizationId":3,
    "currentPage":1,
    "pageSize": 10
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>10000</cost> <code>200</code> <data> <organizationId>1</organizationId> <aliyunUserId>12</aliyunUserId> <product>ecs</product> <organizationName>organization_test</organizationName> <assumeRolePolicyDocument>{"Statement": [{"Action": "sts:testAction", "Effect": "Allow", "Principal": {"Service": ["***.aliyuncs.com"]}}], "Version": "1"}</assumeRolePolicyDocument> <roleId>39405704233030****</roleId> <roleName>AliyunECS****DefaultRole</roleName> <description>ECS管理角色</description> <id>1</id> <roleType>System</roleType> <region>cn-qingdao-****-d01</region> <arn>acs:ram::123456789012****:role/ECSAdmin</arn> </data> <success>true</success> <pageInfo> <total>10</total> <totalPage>2</totalPage> <pageSize>5</pageSize> <currentPage>1</currentPage> </pageInfo> <message>success</message> |  |

`JSON` 格式

```json
{
    "redirect": false,
    "cost": 10000,
    "code": 200,
    "data": {
        "organizationId": 1,
        "aliyunUserId": 12,
        "product": "ecs",
        "organizationName": "organization_test",
        "assumeRolePolicyDocument": "{\"Statement\": [{\"Action\": \"sts:testAction\", \"Effect\": \"Allow\", \"Principal\": {\"Service\": [\"*
**.aliyuncs.com\"]}}], \"Version\": \"1\"}",
        "roleId": "39405704233030****",
        "roleName": "AliyunECS****DefaultRole",
```

`"description": "ECS`管理角色`",`

```json
        "id": 1,
        "roleType": "System",
        "region": "cn-qingdao-****-d01",
        "arn": "acs:ram::123456789012****:role/ECSAdmin"
    },
    "success": true,
    "pageInfo": {
        "total": 10,
        "totalPage": 2,
        "pageSize": 5,
        "currentPage": 1
    },
    "message": "success"
}
```

##### 4.1.4.7. RemoveLoginPolicyById

删除登录策略前，需要将所有绑定该登录策略的用户解绑。可通过调用ModifyUserInformation接口修改用户所使用的登录策略完成解绑。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/removeLoginPolicyById HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| id | Integer | Body | 否 | 1083 | 需要删除的登录策略ID。登录策略ID可通过调用 ListLoginPolicies获取。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|

| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
|---|---|---|---|
| cost | Integer | 19 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据，不返回其它字段。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/removeLoginPolicyById HTTP/1.1
```

公共请求头

```json
{
    "id":1083
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>19</cost> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 19, "success": true, "message": "success" } |  |

##### 4.1.4.8. RemoveLoginPolicyByName

删除登录策略前，需要将所有绑定该登录策略的用户解绑。可通过调用ModifyUserInformation接口修改用户所使用的登录策略完成解绑。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/loginPolicy/removeLoginPolicyByName HTTP/1.1
```

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| name | String | Body | 否 | test | 登录策略名称。根据传入的登录策略名称来精确查找待删除的登录策略。 说明该参数为必填。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Integer | 1000 | 接口响应耗时，单位毫秒（ms）。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据，不返回其它字段。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 说明该参数已废弃。 |

| success | Boolean | true | 本次接口调用是否成功。 true：成功。 false：失败。 |
|---|---|---|---|

**示例**

请求示例

```
POST /ascm/auth/loginPolicy/removeLoginPolicyByName HTTP/1.1
```

公共请求头

```json
{
    "name": "test"
}
```

正常返回示例

| XML | 格式 |
|---|---|
| <redirect>false</redirect> <cost>1000</cost> <code>200</code> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "redirect": false, "cost": 1000, "code": 200, "success": true, "message": "success" } |  |

##### 4.1.4.9. ResetPasswordPolicy

调用ResetPasswordPolicy重置Apsara Uni-manager运营控制台当前的密码策略。 调用ResetPasswordPolicy接口后，原密码策略将重置为Apsara Uni-manager运营控制台的默认密码策略，如果需要修改，可调用SetPasswordPolicy接口。 Apsara Uni-manager运营控制台的默认密码策略详见返回数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /ascm/auth/user/resetPasswordPolicy HTTP/1.1
```

**请求参数**

无

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 500：服务内部错误，发生未识别的异常时会返回此错误码。 |
| cost | Integer | 14 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 密码策略数据。 |
| hardExpiry | Boolean | true | 密码是否过期。 true：过期，过期后用户不能登录Apsara Uni-manager运营控制台。 false：不过期。、 说明可通过maxPasswordAge参数了解密码有效期，用户需要在有效期结束前及时更新密码。若密码已过期，需要联系运营管理员或平台管理员重置密码。 |

| maxLoginAttemps | Integer | 5 | 密码错误容忍周期内使用错误密码尝试登录的最大次数。 说明取值范围0~32。 |
|---|---|---|---|
| maxPasswordAge | Integer | 90 | 密码有效期，单位：天。0表示不启用密码过期策略。 说明取值范围0~1095。 |
| minimumPasswordLength | Integer | 10 | 最小密码长度。 说明取值范围8~32。 |
| passwordErrorCaptchaTim e | Integer | 3 | 触发人机验证（验证码）校验的密码错误次数。 |
| passwordErrorLockPeriod | Integer | 30 | 账号冷冻时长，单位：分钟。 说明若超过密码输入错误次数，则进入账号冷冻期，冷冻期内不能进行登录。取值范围0~1440。 |
| passwordErrorToleranceP eriod | Integer | 5 | 密码错误容忍周期，默认为60分钟，即60分钟内容忍密码输错N次。可通过 maxLoginAttemps参数了解密码错误容忍周期内密码错误输入的次数。 |
| passwordReusePrevention | Integer | 5 | 禁止使用前N次密码。0表示不启用历史密码检查策略，默认不启用。 说明取值范围0~24。 |
| requireLowercaseCharact ers | Boolean | true | 密码中是否必须包含小写英文字母元素。 |
| requireNumbers | Boolean | true | 密码中是否必须包含阿拉伯数字元素。 |
| requireSymbols | Boolean | true | 密码中是否必须包含特殊符号元素。 |
| requireUppercaseCharact ers | Boolean | true | 密码中是否必须包含大写英文字母元素。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 说明该参数已废弃。 |
| success | Boolean | true | 是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例

```
POST /ascm/auth/user/resetPasswordPolicy HTTP/1.1
```

公共请求头

```
{ }
```

正常返回示例

| XML | 格式 |
|---|---|
| <code>200</code> <cost>14</cost> <data> <passwordErrorTolerancePeriod>60</passwordErrorTolerancePeriod> <passwordErrorCaptchaTime>3</passwordErrorCaptchaTime> <minimumPasswordLength>10</minimumPasswordLength> <requireSymbols>true</requireSymbols> <passwordErrorLockPeriod>30</passwordErrorLockPeriod> <passwordReusePrevention>5</passwordReusePrevention> <maxLoginAttemps>5</maxLoginAttemps> <requireLowercaseCharacters>true</requireLowercaseCharacters> <hardExpiry>true</hardExpiry> <requireNumbers>true</requireNumbers> <maxPasswordAge>90</maxPasswordAge> <requireUppercaseCharacters>true</requireUppercaseCharacters> </data> <success>true</success> <message>success</message> |  |

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 14, "data": { "passwordErrorTolerancePeriod": 60, "passwordErrorCaptchaTime": 3, "minimumPasswordLength": 10, "requireSymbols": true, "passwordErrorLockPeriod": 30, "passwordReusePrevention": 5, "maxLoginAttemps": 5, "requireLowercaseCharacters": true, "hardExpiry": true, "requireNumbers": true, "maxPasswordAge": 90, "requireUppercaseCharacters": true }, "success": true, "message": "success" } |  |

##### 4.1.4.10. SetPasswordPolicy

调用SetPasswordPolicy修改Apsara Uni-manager运营控制台当前的密码策略。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 名称 | 类型 | 位置 | 是否必选 | 示例值 | 描述 |
|---|---|---|---|---|---|
| hardExpiry | Boolean | Body | 否 | true | 密码是否过期。 true：过期，过期后用户不能登录Apsara Uni-manager运营控制台。 false：不过期。 说明若请求参数都不传，则返回Apsara Uni-manager运营控制台当前的密码策略。 |
| requireNumbers | Boolean | Body | 否 | true | 密码中是否必须包含阿拉伯数字元素。 |

| requireSymbols | Boolean | Body | 否 | true | 密码中是否必须包含特殊符号元素。 |
|---|---|---|---|---|---|
| requireLowercaseCharacte rs | Boolean | Body | 否 | true | 密码中是否必须包含小写英文字母元素。 |
| requireUppercaseCharacte rs | Boolean | Body | 否 | true | 密码中是否必须包含大写英文字母元素。 |
| maxLoginAttemps | Integer | Body | 否 | 5 | 密码错误容忍周期内使用错误密码尝试登录的最大次数。 说明取值范围为：0~32。 |
| maxPasswordAge | Integer | Body | 否 | 90 | 密码有效期，单位：天。0表示不启用密码过期策略。 说明取值范围为：0~1095。 |
| minimumPasswordLength | Integer | Body | 否 | 10 | 最小密码长度。 说明取值范围为：8~32。 |
| passwordReusePrevention | Integer | Body | 否 | 5 | 禁止使用前N次密码。0表示不启用历史密码检查策略，默认不启用。 说明取值范围为：0~24。 |

**返回数据**

| 名称 | 类型 | 示例值 | 描述 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 400：参数错误。 500：服务内部错误，发生未识别的异常时会返回此错误码。 |
| cost | Integer | 20 | 接口响应耗时，单位毫秒（ms）。 |
| data | Struct |  | 密码策略数据。 |
| hardExpiry | Boolean | true | 密码是否过期。 true：过期，过期后用户不能登录Apsara Uni-manager运营控制台。 false：不过期。 说明可通过maxPasswordAge参数了解密码有效期，用户需要在有效期结束前及时更新密码。若密码已过期，需要联系运营管理员或平台管理员重置密码。 |
| maxLoginAttemps | Integer | 5 | 密码错误容忍周期内使用错误密码尝试登录的最大次数。 说明取值范围0~32。 |
| maxPasswordAge | Integer | 90 | 密码有效期，单位：天。0表示不启用密码过期策略。 说明取值范围0~1095。 |
| minimumPasswordLength | Integer | 10 | 最小密码长度。 说明取值范围8~32。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| passwordErrorCaptchaTim e | Integer | 3 | 触发人机验证（验证码）校验的密码错误次数。 |
|---|---|---|---|
| passwordErrorLockPeriod | Integer | 0 | 账号冷冻时长，单位：分钟。 说明若超过密码输入错误次数，则进入账号冷冻期，冷冻期内不能进行登录。取值范围0~1440。 |
| passwordErrorToleranceP eriod | Integer | 60 | 密码错误容忍周期，默认为60分钟，即60分钟内容忍密码输错N次。可通过 maxLoginAttemps参数了解密码错误容忍周期内密码错误输入的次数。 |
| passwordReusePrevention | Integer | 5 | 禁止使用前N次密码。0表示不启用历史密码检查策略，默认不启用。 说明取值范围0~24。 |
| requireLowercaseCharact ers | Boolean | true | 密码中是否必须包含小写英文字母元素。 |
| requireNumbers | Boolean | true | 密码中是否必须包含阿拉伯数字元素。 |
| requireSymbols | Boolean | true | 密码中是否必须包含特殊符号元素。 |
| requireUppercaseCharact ers | Boolean | true | 密码中是否必须包含大写英文字母元素。 |
| message | String | success | 错误提示信息。 说明无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| pureListData | Boolean | false | 是否只返回数据。 说明该参数已废弃。 |
| redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 说明该参数已废弃。 |
| success | Boolean | true | 是否成功。 true: 成功。 false: 失败。 |

**示例**

请求示例公共请求头

```json
{
    "hardExpiry": true,
    "requireSymbols": true
}
```

正常返回示例 `XML` 格式

```xml
<code>200</code> <cost>20</cost> <data>
    <passwordErrorTolerancePeriod>60</passwordErrorTolerancePeriod>
    <passwordErrorCaptchaTime>3</passwordErrorCaptchaTime>
    <minimumPasswordLength>10</minimumPasswordLength>
    <requireSymbols>true</requireSymbols>
    <passwordErrorLockPeriod>0</passwordErrorLockPeriod>
    <passwordReusePrevention>5</passwordReusePrevention>
    <maxLoginAttemps>5</maxLoginAttemps>
    <requireLowercaseCharacters>true</requireLowercaseCharacters>
    <hardExpiry>true</hardExpiry>
    <requireNumbers>true</requireNumbers>
    <maxPasswordAge>90</maxPasswordAge>
    <requireUppercaseCharacters>true</requireUppercaseCharacters>
</data> <success>true</success> <message>success</message>
```

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 20, "data": { "passwordErrorTolerancePeriod": 60, "passwordErrorCaptchaTime": 3, "minimumPasswordLength": 10, "requireSymbols": true, "passwordErrorLockPeriod": 0, "passwordReusePrevention": 5, "maxLoginAttemps": 5, "requireLowercaseCharacters": true, "hardExpiry": true, "requireNumbers": true, "maxPasswordAge": 90, "requireUppercaseCharacters": true }, "success": true, "message": "success" } |  |

##### 4.1.4.11. GetSAMLSpMetadata

使用SAML2协议单点登录，ASCM作为SP时，用于获取ASCM提供给IdP的元数据。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| IdPId | String | Body | 否 | idP-10354026b9730ad40d55000g | 局部IdP的uuid，为空时获取全局IdP配置信息， 不为空时获取局部IdP配置信息。 此参数非必填。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| successResponse | Boolean | true | 调用是否成功 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| errorKey | String | ascm.auth.InternalError | 异常状态码。 该参数已废弃。 |
| message | String | success | 提示信息。 成功则返回为空。 失败则返回具体失败信息。 |
| extraMessage | String | success | 额外的信息。 |
| eagleEyeTraceId | String | 0ad40c4417628307082308977e 0024 | 鹰眼ID。 |
| requestId | String | FEB7A954-F07F-45EA-B6A3- 980DD0F9EF60 | 本次调用请求的ID，是阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Domain | String | example.com | 报错的domain。 |
| ServerRole | String | unimanager-base.IdentityService | 服务角色名称。 |
| data | Struct | {"encodeSAMLSpMetadataDocum ent":"******"} | 数据。 |
| - encodeSAMLSpMetadataD ocument | String | ******* | ASCM向IdP服务提供的元数据。 获取成功后使用base64解密会得到元数据内容。 |

**示例**

请求示例

```
POST /ascm/auth/saml2/spMetadata/get HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "successResponse":true,
 "errorKey":"ascm.auth.InternalError",
 "eagleEyeTraceId":"0ad40c4417628307082308977e0024",
 "ServerRole":"unimanager-base.IdentityService",
 "code":"200",
 "cost":121,
 "data":{
  "encodeSAMLSpMetadataDocument":"******"
 },
 "requestId":"FEB7A954-F07F-45EA-B6A3-980DD0F9EF60",
 "extraMessage":"success",
 "message":"success",
 "Domain":"example.com"
}
```

| XML | 格式 |
|---|---|
| <successResponse>true</successResponse> <errorKey>ascm.auth.InternalError</errorKey> <eagleEyeTraceId>0ad40c4417628307082308977e0024</eagleEyeTraceId> <ServerRole>unimanager-base.IdentityService</ServerRole> <code>200</code> <cost>121</cost> <data> <encodeSAMLSpMetadataDocument>******</encodeSAMLSpMetadataDocument> </data> <requestId>FEB7A954-F07F-45EA-B6A3-980DD0F9EF60</requestId> <extraMessage>success</extraMessage> <message>success</message> <Domain>example.com</Domain> |  |

##### 4.1.4.12. ResetIdPConfig

重置ASCM全局身份提供商配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| successResponse | Boolean | true | 接口返回成功标识。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 121 | 接口响应耗时，单位毫秒（ms）。 |
| errorKey | String | ascm.manage.InternalError | 异常状态码。 该参数已废弃。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| message | String | success | 提示信息。 成功则返回为空。 失败则返回具体失败信息。 |
| extraMessage | String | success | 额外的信息。 |
| eagleEyeTraceId | String | 0a880c8717059272470618228d 002d | 鹰眼ID。 |
| requestId | String | 2AAF774D-53A7-442E-ADE9- A1E795377748 | 本次调用请求的ID，是阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Domain | String | example.com | 报错的domain。 |
| ServerRole | String | ascm.auth | SR的名称。 |

**示例**

请求示例正常返回示例

| JSON | 格式 |
|---|---|
| { "successResponse":true, "errorKey":"ascm.manage.InternalError", "eagleEyeTraceId":"0a880c8717059272470618228d002d", "ServerRole":"ascm.auth", "code":"200", "cost":121, "requestId":"2AAF774D-53A7-442E-ADE9-A1E795377748", "extraMessage":"success", "message":"success", "Domain":"example.com" } |  |

| XML | 格式 |
|---|---|
| <successResponse>true</successResponse> <errorKey>ascm.manage.InternalError</errorKey> <eagleEyeTraceId>0a880c8717059272470618228d002d</eagleEyeTraceId> <ServerRole>ascm.auth</ServerRole> <code>200</code> <cost>121</cost> <requestId>2AAF774D-53A7-442E-ADE9-A1E795377748</requestId> <extraMessage>success</extraMessage> <message>success</message> <Domain>example.com</Domain> |  |

##### 4.1.4.13. SetIdPConfig

用于配置ASCM全局身份提供商配置。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| IdpName | String | Body | 否 | test | IdP服务名称。 必填，SAML 2.0协议和OAuth 2.0协议对接时都需要配置。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Protocol | String | Body | 否 | OAUTH2 | SSO单点认证协议。 必填，单点登录协议的枚举值，SAML 2.0 协议和OAuth 2.0协议对接时都需要配置。 SAML2。 OAUTH2。 |
| SingleSignOnServic eUrl | String | Body | 否 | http://example.com/auth/oauth/authorize | 第三方认证服务地址。 必填，SAML 2.0协议和OAuth 2.0协议对接时都需要配置。 |
| X509Certificate | String | Body | 否 | UeV8iwRo1ki6JcX7vywhHSmW5kIyEY3**** RtrhdNniU0J9s1FFDLA7ZE0h0wdt6LZu+A ZRd2AphBRnQuEzX6 | x509证书内容，SAML 2.0方式单点登录必填。 必填，仅SAML 2.0协议对接时需要配置。 |
| SingleSignLogoutS erviceUrl | String | Body | 否 | http://example.com/auth/saml/spLogout | SAML 2.0协议单点登出ASCM的入口地址。 选填，仅适用SAML 2.0协议。 |
| SingleLogoutServic eBinding | String | Body | 否 | urn:oasis:names:tc:SAML:2.0:bindings:HT TP-Redirect | SAML 2.0协议单点登出请求方式。 仅适用SAML 2.0协议。 urn:oasis:names:tc:SAML:2.0:bindings: HTTP-POST urn:oasis:names:tc:SAML:2.0:bindings: HTTP-Redirect |
| ClientId | String | Body | 否 | vhzuCPeRTq | 第三方用户唯一凭证。 必填，OAuth 2.0协议对接时必须配置。 |
| ClientSecret | String | Body | 否 | eyJh****** | 第三方用户唯一凭证密钥。 必填，OAuth 2.0协议对接时必须配置。 |
| TokenService | String | Body | 否 | http://example.com/auth/oauth/token | 获取AccessToken接口的地址。 必填，OAuth 2.0协议对接时必须配置， 默认通过POST方式发起请求。 |
| TokenServiceConte ntType | String | Body | 否 | application/x-www-form-urlencoded | 获取AccessToken的消息头中设置的Content- Type。 必填，OAuth 2.0协议对接时必须配置。 application/json; charset=utf-8 application/x-www-form urlencoded |
| UserService | String | Body | 否 | http://example.com/auth/user/info | OAauth 2.0单点登录获取用户信息接口的地址。 必填，OAuth 2.0协议对接时必须配置。 |
| UserServiceReques tMethod | String | Body | 否 | POST | 通过AccessToken获取认证用户信息的请求方式。 必填，OAuth 2.0协议对接时必须配置。 GET POST |
| UserServiceConten tType | String | Body | 否 | application/x-www-form-urlencoded | 通过AccessToken获取认证用户信息的消息头中设置的Content-Type。 必填，OAuth 2.0协议对接时必须配置。 application/json; charset=utf-8 application/x-www-formurlencoded |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| UserServiceHeader Template | String | Body | 否 | [{"key":"accesstoken","value":" _ {{accesstoken}}"}] _ |  | 获取认证用户信息请求头模板。 配置要求： 必填项：OAuth 2.0协议对接时必须配置。 默认值：无默认值，需显式配置。 模板格式：请求头模板需要配置为JSON数组格式，数组中的每个元素包含两个固定字段。 [key]：HTTP请求头的名称。 [value]：请求头的值，可以是固定值或使用占位符 {{access_token}} 。 占位符处理机制： 系统会自动将 {{access_token}} 占位符替换为实际获取到的 accessToken 值。 发送请求时，会将模板中[key]字段的值作为Header名称，[value]字段的值作为 Header值。 配置示例： [ { "key": "access _token", "value": "{{access _token}}" } ]。 示例说明：当 accessToken 值为 KqXk3nm****** 时，发送给用户信息接口的HTTP Header为 access _token: KqXk3nm******。 |  |  |  |
| UserServiceParame terTemplate | String | Body | 否 | [{"key":"accesstoken","value":" _ {{accesstoken}}"}] _ |  | ASCM调用IdP获取认证用户接口的参数模板配置。 配置要求： 必填项: OAuth 2.0协议对接时必须配置参数模板。 配置格式: JSON数组，每个元素包含固定字段 [key]和 [value]。 不同请求类型的模板配置： GET请求或POST + application/x-www- form-urlencoded： 默认值：[ {"key": "参数名称","value": "固定值或 {{access _token}}}]。 示例:[{ "key": "accesstoken","value": " _ {{access _token}}"}]，当 accessToken 为 NIUUzhBOJLNcqR****** 时，实际发送参数为: access_token=NIUUzhBOJLNcqR |  |  |  |
|  |  |  |  |  |  |  | access_token=NIUUzhBOJLNcqR |  |  |
|  |  |  |  |  |  | ****** |  |  |  |
|  |  |  |  |  |  |  |  | {"access_token": |  |

|  | "NIUUzhBOJLNcqR******"} |
|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 |  | 说明 |  |
|---|---|---|---|---|---|---|---|
| UserServiceLoginN amePath | String | Body | 否 | user.name |  | 获取认证用户名的解析路径配置。 配置要求： 必填项：OAuth 2.0协议对接时必须配置返回格式：获取认证用户的服务必须返回 JSON对象格式路径解析规则： 使用半角句号（[.]表示用户名在JSON对象中的层级结构。 支持多层嵌套的对象结构解析。 配置示例： [user]：表示用户名位于JSON对象的第一层。 data.user ：表示用户名位于JSON对象的第二层，即在 data 对象下的 [user]字段。 data.profile.username ：表示用户名位于三层嵌套结构中。 示例说明：假设用户信息服务返回 {"data": { "user": |  |
|  |  |  |  |  |  |  | {"data": { "user": |
|  |  |  |  |  |  | "john_doe"}} |  |
|  |  |  |  |  |  |  | john_doe ， |
|  |  |  |  |  |  |  | data.user |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| successResponse | Boolean | true | 请求是否成功。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 121 | 接口耗时，单位毫秒。 |
| errorKey | String | ascm.auth.InternalError | 异常状态码。 该参数已废弃。 |
| message | String | success | 提示信息。 |
| extraMessage | String | success | 额外的信息，对提示信息的补充说明。 |
| eagleEyeTraceId | String | 0a880c8717059272470618228d 002d | 鹰眼ID。 |
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | 本次调用请求的ID，是由阿里云为该请求生成的唯一标识符，可用于排查和定位问题。 |
| Domain | String | ascm- auth.inter.env66.shuguang.com | 报错的domain。 |
| ServerRole | String | unimanager-base.IdentityService | SR的名称。 |

**示例**

请求示例

```
{ }
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "successResponse":true, "errorKey":"ascm.auth.InternalError", "eagleEyeTraceId":"0a880c8717059272470618228d002d", "ServerRole":"unimanager-base.IdentityService", "code":"200", "cost":121, "requestId":"F0A8A039-930D-5EC1-97C8-************", "extraMessage":"success", "message":"success", "Domain":"ascm-auth.inter.env66.shuguang.com" } |  |

| XML | 格式 |
|---|---|
| <successResponse>true</successResponse> <errorKey>ascm.auth.InternalError</errorKey> <eagleEyeTraceId>0a880c8717059272470618228d002d</eagleEyeTraceId> <ServerRole>unimanager-base.IdentityService</ServerRole> <code>200</code> <cost>121</cost> <requestId>F0A8A039-930D-5EC1-97C8-************</requestId> <extraMessage>success</extraMessage> <message>success</message> <Domain>ascm-auth.inter.env66.shuguang.com</Domain> |  |

##### 4.1.4.14. GetIdPConfig

获取ASCM侧配置的全局身份提供商配置信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| successResponse | Boolean | true | 调用是否成功。 |
| code | String | 200 | 状态码。 200：调用成功。 401：用户未认证。 400：参数错误。 402：Cookie无效。 403：禁止操作，禁止访问某个资源。 404：要访问的资源不存在。 406：账户未被激活。 409：需要保存、添加的数据已经存在。 418：验证码校验失败。 419：第三方服务认证失败。 420：签名校验失败。 421：证书校验失败。 425：服务不存在。 426：证书不存在。 427：AccessKey是有效的，AccessKey所属的用户不能执行此项操作。 428：AccessKey是无效的，AccessKey不存在或者状态异常。 500：服务内部错误，发生未识别的异常时会返回此错误码。 511：参数超过限定的阈值。 512：STS服务颁发的安全令牌失效。 513：依赖的服务异常。 |
| cost | Long | 121 | 接口耗时，单位毫秒（ms）。 |
| errorKey | String | ascm.auth.InternalError | 异常状态码。 该参数已废弃。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| message | String | success | 错误提示信息。无论是否调用成功都会返回。一般调用成功返回success，调用失败返回自定义的错误信息或者返回异常栈中的错误信息。 |
| extraMessage | String | success | 额外的信息，对提示信息的补充说明。 |
| eagleEyeTraceId | String | 0a880c8717059272470618228d 002d | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | API 请求的唯一ID，用于查询API网关的调用日志。 |
| Domain | String | ascm.aliyun.com | 报错的domain。 |
| ServerRole | String | unimanager- base.IdentityService# | SR的名称。 |
| data | Struct | - | IdP配置数据。 |
| -IdpName | String | test | IdP服务名称。 |
| -Protocol | String | OAUTH2 | SSO单点认证协议。 SAML2。 OAUTH2。 |
| -SingleSignOnServiceUrl | String | http://example.com/auth/oauth/a uthorize | 第三方认证服务地址。 |
| -X509Certificate | String | UeV8iwRo1ki6JcX7vywhHSmW5kI yEY3******RtrhdNniU0J9s1FFDLA 7ZE0h0wdt6LZu+AZRd2AphBRn QuEzX6 | x509证书内容，SAML 2.0方式单点登录必填。 |
| - SingleSignLogoutServiceU rl | String | http://example.com/auth/saml/sp Logout | SAML 2.0 协议单点登出ASCM的入口地址。 |
| - SingleLogoutServiceBindi ng | String | urn:oasis:names:tc:SAML:2.0:bind ings:HTTP-Redirect | SAML 2.0 协议单点登出请求方式。 urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect |
| -ClientId | String | vhzuCPeRTq | 第三方用户唯一凭证。 OAuth 2.0 协议对接时必须配置。 |
| -ClientSecret | String | eyJh****** | 第三方用户唯一凭证密钥。 OAuth 2.0 协议对接时必须配置。 |
| -UserService | String | http://example.com/auth/user/inf o | OAuth 2.0单点登录获取用户信息接口地址。 OAuth 2.0 协议对接时必须配置。 |
| -TokenService | String | http://example.com/auth/oauth/to ken | 获取AccessToken的服务地址。 OAuth 2.0 协议对接时必须配置。 |
| - TokenServiceContentType | String | application/x-www-form- urlencoded | 获取AccessToken的消息头中设置的Content Type。 application/json; charset=utf-8 application/x-www-form urlencoded |
| - UserServiceHeaderTempl ate | String | [{"key":"accesstoken","value":" _ {{accesstoken}}"}] _ | 获取认证用户信息消息头模板。默认值为 [{ "key": "access _token", "value": " {{access _token}}" }] 。 {{access _token}}会替换成获取到的AccessToken信息，必须保留。 Apsara Uni-manager运营控制台会将模板内的Key/Value作为 Header参数的Key/Value信息，请求认证用户的服务地址。 |
| - UserServiceRequestMetho d | String | POST | 通过AccessToken获取认证用户信息的服务地址。 GET POST |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| - UserServiceParameterTe mplate | String | [{"key":"accesstoken","value":" _ {{accesstoken}}"}] _ | ASCM调IdP获取认证用户接口的参数模板。 请求类型选择GET： 默认值为 AccessToke n请求Body模板说明获取认证用户名的解析路径 Apsara Uni-manager运营控制台用户指南·配置中心 [{ "key": "access _token", "value": " {{access _token}}" }] 。 请求类型选择POST： Content-Type选择application/json; charset=utf-8时，默认值为 { "access _token": "{{access _token}}" } 。 Content-Type选择 application/x-www-form-urlencoded时，默认值为 [{ "key": "access _token", "value": " {{access _token}}" }] 。 {{access _token}}会替换成获取到的AccessToken信息，必须保留。 Apsara Uni-manager运营控制台会将模板内的Key/Value作为 Body参数的Key/Value信息，请求认证用户的服务地址。 |
| -UserServiceContentType | String | application/x-www-form- urlencoded | 通过AccessToken获取认证用户信息设置的消息头中的Content Type。 application/json; charset=utf-8 application/x-www-form urlencoded |
| - UserServiceLoginNamePat h | String | user.name | 输入获取认证用户名的解析路径，获取认证用户的服务必须返回的是JSON对象。 通过半角句号（.）代表用户名所在对象的层级。例如 user 表示用户名在对象的第一层； ascm.user 表示用户名在对象的第二层。 |

**示例**

| JSON | 格式 |
|---|---|
| { "successResponse":"", "errorKey":"", "eagleEyeTraceId":"", "ServerRole":"unimanager-base.IdentityService#", "code":"", "cost":"", "data":{ "UserServiceHeaderTemplate":"[{\"key\":\"access_token\",\"value\":\"{{access_token}}\"}]", "UserServiceRequestMethod":"POST", "UserService":"http://example.com/auth/user/info", "SingleSignLogoutServiceUrl":"http://example.com/auth/saml/spLogout", "TokenServiceContentType":"application/x-www-form-urlencoded", "X509Certificate":"UeV8iwRo1ki6JcX7vywhHSmW5kIyEY3********************************************************************************************** **********RtrhdNniU0J9s1FFDLA7ZE0h0wdt6LZu+AZRd2AphBRnQuEzX6", "UserServiceParameterTemplate":"[{\"key\":\"access_token\",\"value\":\"{{access_token}}\"}]", "SingleSignOnServiceUrl":"http://example.com/auth/oauth/authorize", "UserServiceReqTemplate":"[{\"key\":\"access_token\",\"value\":\"{{access_token}}\"}]", "SingleLogoutServiceBinding":"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect", "ClientSecret":"eyJh******", "UniqueUserIdKey":"id", "ClientId":"vhzuCPeRTq", "UserServiceContentType":"application/x-www-form-urlencoded", "IdpName":"test", "UserServiceLoginNamePath":"user.name", "Protocol":"OAUTH2", "TokenService":"http://example.com/auth/oauth/token" }, "requestId":"", "extraMessage":"", "message":"", "Domain":"ascm.aliyun.com" } |  |

`XML` 格式

```xml
<successResponse /> <errorKey /> <eagleEyeTraceId /> <ServerRole>unimanager-base.IdentityService#</ServerRole> <code /> <cost /> <data>
 <UserServiceHeaderTemplate>[{&quot;key&quot;:&quot;access_token&quot;,&quot;value&quot;:&quot;{{access_token}}&quot;}]
</UserServiceHeaderTemplate>
 <UserServiceRequestMethod>POST</UserServiceRequestMethod>
 <UserService>http://example.com/auth/user/info</UserService>
 <SingleSignLogoutServiceUrl>http://example.com/auth/saml/spLogout</SingleSignLogoutServiceUrl>
 <TokenServiceContentType>application/x-www-form-urlencoded</TokenServiceContentType>
<X509Certificate>UeV8iwRo1ki6JcX7vywhHSmW5kIyEY3*************************************************************************************************
********RtrhdNniU0J9s1FFDLA7ZE0h0wdt6LZu+AZRd2AphBRnQuEzX6</X509Certificate>
 <UserServiceParameterTemplate>[{&quot;key&quot;:&quot;access_token&quot;,&quot;value&quot;:&quot;{{access_token}}&quot;}]
</UserServiceParameterTemplate>
 <SingleSignOnServiceUrl>http://example.com/auth/oauth/authorize</SingleSignOnServiceUrl>
 <UserServiceReqTemplate>[{&quot;key&quot;:&quot;access_token&quot;,&quot;value&quot;:&quot;{{access_token}}&quot;}]</UserServiceReqTemplate>
 <SingleLogoutServiceBinding>urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect</SingleLogoutServiceBinding>
 <ClientSecret>eyJh******</ClientSecret>
 <UniqueUserIdKey>id</UniqueUserIdKey>
 <ClientId>vhzuCPeRTq</ClientId>
 <UserServiceContentType>application/x-www-form-urlencoded</UserServiceContentType>
 <IdpName>test</IdpName>
 <UserServiceLoginNamePath>user.name</UserServiceLoginNamePath>
 <Protocol>OAUTH2</Protocol>
 <TokenService>http://example.com/auth/oauth/token</TokenService>
</data> <requestId /> <extraMessage /> <message /> <Domain>ascm.aliyun.com</Domain>
```

##### 4.1.4.15. ListAvailablePlatforms

获取当前用户有权限查看的资源池列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| name | String | Query | 否 | cloud1 | 资源池的名称。 |
| code | String | Query | 否 | pl-abcd1230201 | 资源池的编码。 |
| includeDefault | Boolean | Query | 否 | true | 是否需要返回中心云信息，默认为false。 false：表示不返回。 true：表示返回。 |
| forceIncludeDefaul t | Boolean | Query | 否 | false | 是否需要强制返回中心云信息。当传入有效的中心云sourceOrgId，且未绑定其他云组织时，需要includeDefault和forceIncludeDefault均为 true，才能返回中心云的信息。 |
| platformType | String | Query | 否 | Apsara | 资源池类型，精确搜索。 Apsara：专有云。 ALIYUN：公共云。 |
| sourceUserId | Integer | Query | 否 | 123 | 中心云用户的ID。 |
| sourceOrgId | Integer | Query | 否 | 5 | 中心云查询的组织ID。 |
| filterBoundPlatform | Boolean | Query | 否 | false | 是否过滤被绑定的资源池。 true：表示过滤。 false：表示不过滤。 |
| applyCurrentUser | Boolean | Query | 否 | false | 是否根据当前用户查询，不区分启用禁用。 true：表示不区分启用禁用的资源池。 false：表示仅返回启用的资源池。 |
| parentPlatformCod e | String | Query | 否 | pl-a | 管理账号code。 |

| 统一云管平台 |  |  |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| filterCustomPlatfor m | Boolean | Query | 否 | true | 是否过滤自定义资源池： true：过滤 false：不过滤 |
| filterBoundOrganiz ationId | Integer | Query | 否 | 5 | 资源账号绑定的组织id。 |
| pageNumber | Integer | Query | 否 | 1 | 页码，从1开始，不能小于1。默认值为1。 |
| pageSize | Integer | Query | 否 | 10 | 每页数量，最大1000。默认值为10。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 接口返回数据。 |
| -platformData | Array | [] | 资源池数据列表。 |
| --platformId | String | 1 | 资源池ID。 |
| --code | String | pl-*********** | 资源池编码。 |
| --logo | String | ******.png | 资源池图标。 |
| --displayName | String | 资源池1 | 资源池显示名称。 |
| --account | String | 16********** | 账号ID。 |
| --gmtCreate | Long | 1703575552000 | 创建时间。 |
| --gmtModified | Long | 1703575553000 | 修改时间。 |
| --status | Integer | 100 | 资源池接入状态值，取值与对应含义如下： 0：初始状态。 20：未授权状态，用户未填写账号信息。 50：已授权状态。 80：初始化异步任务已经启动。 90：初始化失败。 100：初始化成功，资源池已可以使用。 |
| --disabled | Boolean | false | 资源池是否禁止选择，默认为false。 true：表示禁止选择。 false：表示允许选择。 |
| --deleteDisabled | Boolean | false | 资源池是否禁止删除。 true：表示禁止删除。 false：表示允许删除。 |
| --enableStatus | Integer | 1 | 资源池启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| --bound | Boolean | false | 资源池是否被绑定。 true：表示被绑定过。 false：表示未被绑定过。 |
| --allowMulTopOrgMapping | Boolean | false | 是否允许多一级组织映射同一个资源池。 true：表示允许。 false：表示不允许。 |
| --accountType | String | managerAccount | 公共云账号类型。 singleAccount：独立主账号。 managerAccount：资源目录管理账号。 resourceAccount：资源账号。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --description | String | 测试数据。 | 资源池描述。 |
| --platformType | Struct | {} | 资源池类型。 |
| ---code | String | Apsara | 资源池类型的code： Apsara：专有云。 ALIYUN：公共云。 |
| ---displayName | String | 专有云 | 资源池类型的显示名称。 |
| ---enterprise | Boolean | true | 是否为专有云。 true：专有云。 false：非专有云。 |
| ---platformType | String | Apsara | 资源池类型： Apsara：表示专有云 ALIYUN：表示公共云 |
| --config | Struct | {} | 资源池配置。 |
| ---cloudUniqueId | String | cloud***** _ | 资源池实例ID。如果是专有云则为专有云实例ID，如果是公共云则为公共云主账号UID。 |
| ---cloudVersion | String | Enterprisev3***** _ | 资源池的版本。专有云显示版本，公共云则为空。 |
| ---defaultRegion | String | cn-***** | 默认的地域。 |
| ---consoleEndpoint | String | one.console.******.com | 专有云OneConsole的Endpoint。 |
| ---authentication | Struct | {} | 认证配置。 |
| ----metadataUrl | String | http://******.xml | SSO元数据的URL链接。 |
| ----type | String | saml | SSO认证类型，默认为SAML协议。 |
| --connectStatus | Struct | {} | 资源池连通状态。 |
| ---id | Long | 1 | 平台连接状态ID。 |
| ---platformId | Long | 1 | 平台ID。 |
| ---endpointStatus | Integer | 1 | 平台网络连接状态。 1：正常。 0：异常。 |
| ---credentialStatus | Integer | 1 | 平台凭证状态。 1：正常。 0：异常。 |
| ---message | String | "" | 异常状态的信息。 |
| ---updateTime | String | 2025-12-18T01:48:18.000+00:00 | 连接状态更新时间。 |
| --parentPlatform | Struct | {} | 管理账号信息。 |
| ---account | String | 16********** | 账号ID。 |
| ---platformCode | String | pl-xxx | 资源池code。 |
| ---displayName | String | 专有云 | 资源池类型的显示名称。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ---accountType | String | managerAccount | 公共云账号类型。 singleAccount：独立主账号。 managerAccount：资源目录管理账号。 resourceAccount：资源账号。 |
| ---enableStatus | Integer | 1 | 资源池启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| ---gmtCreate | Long | 1703575552000 | 创建时间。 |
| ---platformType | Struct | Apsara | 资源池类型： Apsara：表示专有云 ALIYUN：表示公共云 |
| ----code | String | pl-*********** | 资源池类型的code： Apsara：专有云。 ALIYUN：公共云。 |
| ----displayName | String | 资源池2 | 资源池类型的显示名称。 |
| ----enterprise | Boolean | true | 是否为专有云。 true：专有云。 false：非专有云。 |
| ----platformType | String | ALIYUN | 资源池类型： Apsara：表示专有云 ALIYUN：表示公共云 |
| -pageNumber | Integer | 1 | 查询的页码数。 |
| -pageSize | Integer | 10 | 单页数量。 |
| -totalSize | Long | 3 | 总条数。 |

**示例**

请求示例

```
POST /platforms/list/available HTTP/1.1 { }
```

正常返回示例 `JSON` 格式

```json
{
 "data":{
  "pageNumber":1,
  "totalSize":3,
  "pageSize":10,
  "platformData":[
   {
    "gmtModified":1703575553000,
    "code":"pl-***********",
    "allowMulTopOrgMapping":false,
    "displayName":"资源池1",
    "bound":false,
    "platformType":[
     {
      "code":"Apsara",
      "displayName":"专有云",
      "enterprise":true,
      "platformType":"Apsara"
     }
```

`],`

```json
    "platformId":"1",
    "gmtCreate":1703575552000,
    "config":[
     {
      "cloudUniqueId":"cloud_*****",
      "cloudVersion":"Enterprise_v3*****",
      "defaultRegion":"cn-*****",
      "consoleEndpoint":"one.console.******.com",
      "authentication":[
       {
        "metadataUrl":"http://******.xml",
        "type":"saml"
       }
```

]

```
     }
```

`],`

```json
    "deleteDisabled":false,
    "connectStatus":[
     {
      "endpointStatus":1,
      "updateTime":"2025-12-18T01:48:18.000+00:00",
      "id":1,
      "platformId":1,
      "message":"\"\"",
      "credentialStatus":1
     }
```

`],`

```json
    "logo":"******.png",
    "disabled":false,
    "enableStatus":1,
    "account":"16**********",
    "status":100
   }
```

]

```
 }
}
```

`XML` 格式

```xml
<data>
 <pageNumber>1</pageNumber>
 <totalSize>3</totalSize>
 <pageSize>10</pageSize>
 <platformData>
  <gmtModified>1703575553000</gmtModified>
  <code>pl-***********</code>
  <allowMulTopOrgMapping>false</allowMulTopOrgMapping>
  <displayName>资源池1</displayName>
  <bound>false</bound>
  <platformType>
   <code>Apsara</code>
   <displayName>专有云</displayName>
   <enterprise>true</enterprise>
   <platformType>Apsara</platformType>
  </platformType>
  <platformId>1</platformId>
  <gmtCreate>1703575552000</gmtCreate>
  <config>
   <cloudUniqueId>cloud_*****</cloudUniqueId>
   <cloudVersion>Enterprise_v3*****</cloudVersion>
   <defaultRegion>cn-*****</defaultRegion>
   <consoleEndpoint>one.console.******.com</consoleEndpoint>
   <authentication>
    <metadataUrl>http://******.xml</metadataUrl>
    <type>saml</type>
   </authentication>
  </config>
  <deleteDisabled>false</deleteDisabled>
  <connectStatus>
   <endpointStatus>1</endpointStatus>
   <updateTime>2025-12-18T01:48:18.000+00:00</updateTime>
   <id>1</id>
   <platformId>1</platformId>
   <message>&quot;&quot;</message>
   <credentialStatus>1</credentialStatus>
  </connectStatus>
  <logo>******.png</logo>
  <disabled>false</disabled>
  <enableStatus>1</enableStatus>
  <account>16**********</account>
  <status>100</status>
 </platformData>
</data>
```

##### 4.1.4.16. ListResourceAccounts

多云管理场景，获取管理账号下的资源账号列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| platformCode | String | Body | 是 | pl-xxx | 管理账号code。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 响应结果。 |
| -accountData | Array | [] | 账号数据。 |
| --status | String | CreateSuccess | 账号状态。 |
| --joinMethod | String | created | 加入方式。 |
| --modifyTime | String | 1970-01-01T00:00:00.000+00:00 | 修改时间。 |
| --type | String | ResourceAccount | 账号类型。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --resourceDirectoryId | String | 123 | 资源目录ID。 |
| --accountId | String | 1232334 | 账号ID。 |
| --displayName | String | testuser20220906**** | 账号名称。 |
| --joinTime | String | 1970-01-01T00:00:00.000+00:00 | 加入时间。 |
| --folderId | String | ab-cde | 文件夹ID。 |
| --resourceDirectoryPath | String | rd-k3****/123 | 资源目录路径。 |
| --accountName | String | abc | 账号名称。 |
| --bound | Boolean | false | 当前资源账号是否绑定组织。 |
| --deletionStatus | String | pendingDeletion | 当前资源账号的删除状态，为空则表示没有删除。 |
| -success | Boolean | true | 本次接口调用是否成功。 true: 成功。 false: 失败。 |
| -code | String | 200 | 响应code。 |
| -product | String | ascm | 接口所属的产品名称。 |
| -message | String | “failed" | 错误提示信息。调用成功则不返回。 |
| -requestId | String | 111 | 调用请求的ID。 |
| -errorKey | String | abc | 错误类型关键字。 |
| -redirect | Boolean | false | 是否重定向。 true：重定向。 false：不重定向。 |

**示例**

请求示例

```json
{
  "platformCode":"pl-abc"
}
```

正常返回示例 `JSON` 格式

```json
{
 "data":{
  "redirect":false,
  "errorKey":"abc",
  "product":"ascm",
  "code":"200",
  "success":true,
  "requestId":"111",
  "accountData":[
   {
    "joinMethod":"created",
    "joinTime":"1970-01-01T00:00:00.000+00:00",
    "accountName":"abc",
    "displayName":"testuser20220906****",
    "bound":false,
    "type":"ResourceAccount",
    "folderId":"ab-cde",
    "accountId":"1232334",
    "modifyTime":"1970-01-01T00:00:00.000+00:00",
    "deletionStatus":"pendingDeletion",
    "resourceDirectoryPath":"rd-k3****/123",
    "resourceDirectoryId":"123",
    "status":"CreateSuccess"
   }
```

`],`

```json
  "message":"success"
 }
}
```

**文档补充说明**

只允许平台管理员和绑定了公共云的运营管理员调用该接口。

##### 4.1.4.17. ListSubPlatforms

根据管理账号列出所有接入资源账号的资源池。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| parentPlatformCod e | String | Body | 否 | pl-a | 管理账号code。 |
| filterBoundPlatform | Boolean | Body | 否 | false | 是否过滤被绑定的资源账号。 true：表示过滤。 false：表示不过滤。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | {} | 接口返回数据。 |
| -platformData | Array | [] | 资源池数据列表。 |
| --platformId | String | 1 | 资源池ID。 |
| --code | String | pl-*********** | 资源池code。 |
| --logo | String | ******.png | 平台图标。 |
| --displayName | String | 云平台1 | 资源池名称。 |
| --account | String | 16********** | 账号ID。 |
| --gmtCreate | Long | 1703575552000 | 创建时间。 |
| --gmtModified | Long | 1770028091941 | 修改时间。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --status | Integer | 100 | 平台接入状态值，取值与对应含义如下： 0：初始状态。 20：未授权状态，用户未填写账号信息。 50：已授权状态。 80：初始化异步任务已经启动。 90：初始化失败。 100：初始化成功，云平台已可以使用。 |
| --disabled | Boolean | false | 平台是否禁止选择，默认为false。 true：表示禁止选择。 false：表示允许选择。 |
| --deleteDisabled | Boolean | false | 平台是否禁止删除。 true：表示禁止删除。 false：表示允许删除。 |
| --enableStatus | Integer | 1 | 平台启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| --bound | Boolean | false | 平台是否被绑定。 true：表示被绑定过。 false：表示未被绑定过。 |
| --allowMulTopOrgMapping | Boolean | false | 是否允许多一级组织映射同一个平台。 true：表示允许。 false：表示不允许。 |
| --accountType | String | resourceAccount | 公共云账号类型。 singleAccount：独立主账号。 managerAccount：资源目录管理账号。 resourceAccount：资源账号。 |
| --description | String | 测试数据。 | 资源池说明。 |
| --platformType | Struct | {} | 平台类型。 |
| ---code | String | ALIYUN | 资源池类型code。 |
| ---displayName | String | 公共云 | 资源池类型显示名称。 |
| ---enterprise | Boolean | false | 是否为专有云。 true：专有云。 false：非专有云。 |
| ---platformType | String | ALIYUN | 平台类型： Apsara：表示专有云 ALIYUN：表示公共云 |
| --config | Struct | {} | 资源池配置。 |
| ---cloudUniqueId | String | 123 | 资源池实例ID。如果是专有云则为专有云实例ID，如果是公共云则为公共云主账号UID。 |
| ---cloudVersion | String | Enterprisev3***** _ | 资源池的版本。专有云显示版本，公共云则为空。 |
| ---defaultRegion | String | cn-***** | 默认的地域。 |
| ---consoleEndpoint | String | one.console.******.com | 专有云OneConsole的Endpoint。 |
| ---authentication | Struct | {} | 认证配置。 |
| ----metadataUrl | String | http://******.xml | SSO元数据的URL链接。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| ----type | String | saml | SSO认证类型，默认为SAML协议。 |
| --connectStatus | Struct | {} | 资源池连通状态。 |
| ---id | Long | 1 | 资源池连接状态ID。 |
| ---platformId | Long | 1 | 资源池ID。 |
| ---endpointStatus | Integer | 1 | 网络连接状态。 1：正常。 0：异常。 |
| ---credentialStatus | Integer | 1 | 资源池凭证状态。 1：正常。 0：异常。 |
| ---message | String | error | 异常信息。 |
| ---updateTime | String | 2025-12-18T01:48:18.000+00:00 | 连接状态更新时间。 |
| --parentPlatform | Struct | {} | 管理账号信息。 |
| ---account | String | 16********** | 账号ID。 |
| ---platformCode | String | pl-xxx | 资源池code。 |
| ---displayName | String | 管理账号 | 资源池名称。 |
| ---accountType | String | managerAccount | 公共云账号类型。 singleAccount：独立主账号。 managerAccount：资源目录管理账号。 resourceAccount：资源账号。 |
| ---enableStatus | Integer | 1 | 资源池启用/禁用状态。 1：表示启用。 0：表示禁用。 |
| ---gmtCreate | Long | 1703575552000 | 创建时间。 |
| ---platformType | Struct | {} | 资源池类型。 |
| ----code | String | ALIYUN | 资源池类型code。 |
| ----displayName | String | 公共云 | 资源池类型显示名称。 |
| ----enterprise | Boolean | false | 是否为专有云。 true：专有云。 false：非专有云。 |
| ----platformType | String | ALIYUN | 资源池类型。 |
| -pageNumber | Integer | 1 | 查询的页码数。 |
| -pageSize | Integer | 10 | 单页数量。 |
| -totalSize | Long | 100 | 总数据量。 |

**示例**

请求示例

```json
{
    "parentPlatformCode":"pl-123456"
}
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "data":{ "pageNumber":1, "totalSize":100, "pageSize":10, "platformData":[ { "gmtModified":1770028091941, "code":"pl-***********", "allowMulTopOrgMapping":false, "displayName":"云平台1", "bound":false, "accountType":"resourceAccount", "platformType":[ { "code":"ALIYUN", "displayName":"公共云", "enterprise":false, "platformType":"ALIYUN" } ], "description":"测试数据。", "platformId":"1", "gmtCreate":1703575552000, "config":[ { "cloudUniqueId":"123", "cloudVersion":"Enterprise_v3*****", "defaultRegion":"cn-*****", "consoleEndpoint":"one.console.******.com", "authentication":[ { "metadataUrl":"http://******.xml", "type":"saml" } ] } ], "deleteDisabled":false, "connectStatus":[ { "endpointStatus":1, "updateTime":"2025-12-18T01:48:18.000+00:00", "id":1, "platformId":1, "message":"error", "credentialStatus":1 } ], "logo":"******.png", "disabled":false, "enableStatus":1, "account":"16**********", "status":100, "parentPlatform":[ { "displayName":"管理账号", "platformType":[ { "code":"ALIYUN", "displayName":"公共云", "enterprise":false, "platformType":"ALIYUN" } ], "accountType":"managerAccount", "gmtCreate":1703575552000, "enableStatus":1, "account":"16**********", "platformCode":"pl-xxx" } ] } ] } } |  |

`XML` 格式

```xml
<data>
 <pageNumber>1</pageNumber>
 <totalSize>100</totalSize>
 <pageSize>10</pageSize>
 <platformData>
  <gmtModified>1770028091941</gmtModified>
  <code>pl-***********</code>
  <allowMulTopOrgMapping>false</allowMulTopOrgMapping>
  <displayName>云平台1</displayName>
  <bound>false</bound>
  <accountType>resourceAccount</accountType>
  <platformType>
   <code>ALIYUN</code>
   <displayName>公共云</displayName>
   <enterprise>false</enterprise>
   <platformType>ALIYUN</platformType>
  </platformType>
```

`<description>`测试数据。`</description>`

```xml
  <platformId>1</platformId>
  <gmtCreate>1703575552000</gmtCreate>
  <config>
   <cloudUniqueId>123</cloudUniqueId>
   <cloudVersion>Enterprise_v3*****</cloudVersion>
   <defaultRegion>cn-*****</defaultRegion>
   <consoleEndpoint>one.console.******.com</consoleEndpoint>
   <authentication>
    <metadataUrl>http://******.xml</metadataUrl>
    <type>saml</type>
   </authentication>
  </config>
  <deleteDisabled>false</deleteDisabled>
  <connectStatus>
   <endpointStatus>1</endpointStatus>
   <updateTime>2025-12-18T01:48:18.000+00:00</updateTime>
   <id>1</id>
   <platformId>1</platformId>
   <message>error</message>
   <credentialStatus>1</credentialStatus>
  </connectStatus>
  <logo>******.png</logo>
  <disabled>false</disabled>
  <enableStatus>1</enableStatus>
  <account>16**********</account>
  <status>100</status>
  <parentPlatform>
   <displayName>管理账号</displayName>
   <platformType>
    <code>ALIYUN</code>
    <displayName>公共云</displayName>
    <enterprise>false</enterprise>
    <platformType>ALIYUN</platformType>
   </platformType>
   <accountType>managerAccount</accountType>
   <gmtCreate>1703575552000</gmtCreate>
   <enableStatus>1</enableStatus>
   <account>16**********</account>
   <platformCode>pl-xxx</platformCode>
  </parentPlatform>
 </platformData>
</data>
```

##### 4.1.4.18. ListCloudServices

获取专有云RAM支持的云服务列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | [ ] | 专有云RAM支持的云服务编码和云服务别名映射。 |
| -serviceAlias | String | asr.aliyuncs.com | 云服务别名。 |
| -code | String | asr | 云服务编码。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | String | 200 | 响应码。 |
| cost | Integer | 121 | 接口响应耗时，单位毫秒（ms）。 |
| eagleEyeTraceId | String | 0ad40c4417628307082308977e 0*** | 鹰眼ID，请求的唯一标识，用于查询日志信息。 |
| message | String | success | 提示信息。 成功则返回为空。 失败则返回具体失败信息。 |
| success | Boolean | true | 接口请求成功标识： true：成功。 false：失败。 |
| successResponse | Boolean | true | 接口返回成功标识。 |

**示例**

请求示例正常返回示例

| JSON | 格式 |
|---|---|
| { "code": "200", "cost": 0, "data": [ { "code": "rds", "serviceAlias": "rds.aliyuncs.com" }, { "code": "asr", "serviceAlias": "asr.aliyuncs.com" }, { "code": "faas", "serviceAlias": "faas.aliyuncs.com" }, { "code": "ess", "serviceAlias": "ess.aliyuncs.com" }, { "code": "nasbackup", "serviceAlias": "nasbackup.hbr.aliyuncs.com" }, { "code": "dcaasbms", "serviceAlias": "dcaasbms.aliyuncs.com" }, { "code": "aipaas", "serviceAlias": "aipaas.aliyuncs.com" }, { "code": "dms", "serviceAlias": "dms.aliyuncs.com" }, { "code": "apsaraxdm", "serviceAlias": "apsaraxdm.aliyuncs.com" }, { "code": "datahub", "serviceAlias": "datahub.aliyuncs.com" }, { "code": "oss", "serviceAlias": "oss.aliyuncs.com" }, { "code": "ossbackup", "serviceAlias": "ossbackup.hbr.aliyuncs.com" }, { "code": "cgw", |  |

```json
            "serviceAlias": "cgw.aliyuncs.com"
        },
        {
            "code": "oos",
            "serviceAlias": "oos.aliyuncs.com"
        },
        {
            "code": "ecs",
            "serviceAlias": "ecs.aliyuncs.com"
        },
        {
            "code": "oceanbase",
            "serviceAlias": "oceanbase.aliyuncs.com"
        },
        {
            "code": "pai",
            "serviceAlias": "pai.aliyuncs.com"
        },
        {
            "code": "nat",
            "serviceAlias": "nat.aliyuncs.com"
        },
        {
            "code": "nas",
            "serviceAlias": "nas.aliyuncs.com"
        },
        {
            "code": "workflow",
            "serviceAlias": "workflow.aliyuncs.com"
        },
        {
            "code": "usermgmt",
            "serviceAlias": "usermgmt.hologres.aliyuncs.com"
        },
        {
            "code": "slb",
            "serviceAlias": "slb.aliyuncs.com"
        },
        {
            "code": "dbaudit",
            "serviceAlias": "dbaudit.aliyuncs.com"
        },
        {
            "code": "odps",
            "serviceAlias": "odps.aliyuncs.com"
        },
        {
            "code": "mts",
            "serviceAlias": "mts.aliyuncs.com"
        },
        {
            "code": "yundun-dashboard",
            "serviceAlias": "yundun-dashboard.aliyuncs.com"
        },
        {
            "code": "drds",
            "serviceAlias": "drds.aliyuncs.com"
        },
        {
            "code": "dbs",
            "serviceAlias": "dbs.aliyuncs.com"
        },
        {
            "code": "soar",
            "serviceAlias": "soar.aliyuncs.com"
        },
        {
            "code": "arms",
            "serviceAlias": "arms.aliyuncs.com"
        },
        {
            "code": "edas",
            "serviceAlias": "edas.aliyuncs.com"
        },
        {
            "code": "cdscm",
            "serviceAlias": "cdscm.aliyuncs.com"
        },
        {
            "code": "dataworks",
            "serviceAlias": "dataworks.aliyuncs.com"
        },
        {
            "code": "log",
            "serviceAlias": "log.aliyuncs.com"
        },
{
```

```json
        {
            "code": "hologres",
            "serviceAlias": "hologres.aliyuncs.com"
        },
        {
            "code": "smc",
            "serviceAlias": "smc.aliyuncs.com"
        },
        {
            "code": "imm",
            "serviceAlias": "imm.aliyuncs.com"
        },
        {
            "code": "emr",
            "serviceAlias": "emr.aliyuncs.com"
        },
        {
            "code": "hcs-sgw",
            "serviceAlias": "hcs-sgw.aliyuncs.com"
        },
        {
            "code": "vaultencryption",
            "serviceAlias": "vaultencryption.hbr.aliyuncs.com"
        },
        {
            "code": "cen",
            "serviceAlias": "cen.aliyuncs.com"
        },
        {
            "code": "kms",
            "serviceAlias": "kms.aliyuncs.com"
        },
        {
            "code": "apds",
            "serviceAlias": "apds.aliyuncs.com"
        },
        {
            "code": "stream",
            "serviceAlias": "stream.aliyuncs.com"
        },
        {
            "code": "ecsbackup",
            "serviceAlias": "ecsbackup.hbr.aliyuncs.com"
        },
        {
            "code": "ros",
            "serviceAlias": "ros.aliyuncs.com"
        },
        {
            "code": "prometheus",
            "serviceAlias": "prometheus.aliyuncs.com"
        },
        {
            "code": "waf",
            "serviceAlias": "waf.aliyuncs.com"
        },
        {
            "code": "cloudfw",
            "serviceAlias": "cloudfw.aliyuncs.com"
        },
        {
            "code": "dts",
            "serviceAlias": "dts.aliyuncs.com"
        },
        {
            "code": "sas",
            "serviceAlias": "sas.aliyuncs.com"
        },
        {
            "code": "edgepaas",
            "serviceAlias": "edgepaas.aliyuncs.com"
        },
        {
            "code": "bastionhost",
            "serviceAlias": "bastionhost.aliyuncs.com"
        },
        {
            "code": "cr",
            "serviceAlias": "cr.aliyuncs.com"
        },
        {
            "code": "cs",
            "serviceAlias": "cs.aliyuncs.com"
        },
        {
            "code": "hdm",
            "serviceAlias": "hdm.aliyuncs.com"
}
```

```json
        },
        {
            "code": "csb",
            "serviceAlias": "csb.aliyuncs.com"
        },
        {
            "code": "ons",
            "serviceAlias": "ons.aliyuncs.com"
        },
        {
            "code": "cloudmonitor",
            "serviceAlias": "cloudmonitor.aliyuncs.com"
        },
        {
            "code": "hdr",
            "serviceAlias": "hdr.aliyuncs.com"
        },
        {
            "code": "ebs",
            "serviceAlias": "ebs.aliyuncs.com"
        },
        {
            "code": "ehpc",
            "serviceAlias": "ehpc.aliyuncs.com"
        },
        {
            "code": "asm",
            "serviceAlias": "asm.aliyuncs.com"
        },
        {
            "code": "config",
            "serviceAlias": "config.aliyuncs.com"
        },
        {
            "code": "pds",
            "serviceAlias": "pds.aliyuncs.com"
        }
```

`],`

```json
    "message": "success",
    "success": true,
    "successResponse": true
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <cost>0</cost> <data> <code>rds</code> <serviceAlias>rds.aliyuncs.com</serviceAlias> </data> <data> <code>asr</code> <serviceAlias>asr.aliyuncs.com</serviceAlias> </data> <data> <code>faas</code> <serviceAlias>faas.aliyuncs.com</serviceAlias> </data> <data> <code>ess</code> <serviceAlias>ess.aliyuncs.com</serviceAlias> </data> <data> <code>nasbackup</code> <serviceAlias>nasbackup.hbr.aliyuncs.com</serviceAlias> </data> <data> <code>dcaasbms</code> <serviceAlias>dcaasbms.aliyuncs.com</serviceAlias> </data> <data> <code>aipaas</code> <serviceAlias>aipaas.aliyuncs.com</serviceAlias> </data> <data> <code>dms</code> <serviceAlias>dms.aliyuncs.com</serviceAlias> </data> <data> <code>apsaraxdm</code> <serviceAlias>apsaraxdm.aliyuncs.com</serviceAlias> </data> <data> <code>datahub</code> <serviceAlias>datahub.aliyuncs.com</serviceAlias> </data> |  |

```xml
</data> <data>
 <code>oss</code>
 <serviceAlias>oss.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ossbackup</code>
 <serviceAlias>ossbackup.hbr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cgw</code>
 <serviceAlias>cgw.aliyuncs.com</serviceAlias>
</data> <data>
 <code>oos</code>
 <serviceAlias>oos.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ecs</code>
 <serviceAlias>ecs.aliyuncs.com</serviceAlias>
</data> <data>
 <code>oceanbase</code>
 <serviceAlias>oceanbase.aliyuncs.com</serviceAlias>
</data> <data>
 <code>pai</code>
 <serviceAlias>pai.aliyuncs.com</serviceAlias>
</data> <data>
 <code>nat</code>
 <serviceAlias>nat.aliyuncs.com</serviceAlias>
</data> <data>
 <code>nas</code>
 <serviceAlias>nas.aliyuncs.com</serviceAlias>
</data> <data>
 <code>workflow</code>
 <serviceAlias>workflow.aliyuncs.com</serviceAlias>
</data> <data>
 <code>usermgmt</code>
 <serviceAlias>usermgmt.hologres.aliyuncs.com</serviceAlias>
</data> <data>
 <code>slb</code>
 <serviceAlias>slb.aliyuncs.com</serviceAlias>
</data> <data>
 <code>dbaudit</code>
 <serviceAlias>dbaudit.aliyuncs.com</serviceAlias>
</data> <data>
 <code>odps</code>
 <serviceAlias>odps.aliyuncs.com</serviceAlias>
</data> <data>
 <code>mts</code>
 <serviceAlias>mts.aliyuncs.com</serviceAlias>
</data> <data>
 <code>yundun-dashboard</code>
 <serviceAlias>yundun-dashboard.aliyuncs.com</serviceAlias>
</data> <data>
 <code>drds</code>
 <serviceAlias>drds.aliyuncs.com</serviceAlias>
</data> <data>
 <code>dbs</code>
 <serviceAlias>dbs.aliyuncs.com</serviceAlias>
</data> <data>
 <code>soar</code>
 <serviceAlias>soar.aliyuncs.com</serviceAlias>
</data> <data>
 <code>arms</code>
 <serviceAlias>arms.aliyuncs.com</serviceAlias>
</data> <data>
 <code>edas</code>
 <serviceAlias>edas.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cdscm</code>
<sericeAlias>cdscmali ncscom</sericeAlias>
```

```xml
 <serviceAlias>cdscm.aliyuncs.com</serviceAlias>
</data> <data>
 <code>dataworks</code>
 <serviceAlias>dataworks.aliyuncs.com</serviceAlias>
</data> <data>
 <code>log</code>
 <serviceAlias>log.aliyuncs.com</serviceAlias>
</data> <data>
 <code>hologres</code>
 <serviceAlias>hologres.aliyuncs.com</serviceAlias>
</data> <data>
 <code>smc</code>
 <serviceAlias>smc.aliyuncs.com</serviceAlias>
</data> <data>
 <code>imm</code>
 <serviceAlias>imm.aliyuncs.com</serviceAlias>
</data> <data>
 <code>emr</code>
 <serviceAlias>emr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>hcs-sgw</code>
 <serviceAlias>hcs-sgw.aliyuncs.com</serviceAlias>
</data> <data>
 <code>vaultencryption</code>
 <serviceAlias>vaultencryption.hbr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cen</code>
 <serviceAlias>cen.aliyuncs.com</serviceAlias>
</data> <data>
 <code>kms</code>
 <serviceAlias>kms.aliyuncs.com</serviceAlias>
</data> <data>
 <code>apds</code>
 <serviceAlias>apds.aliyuncs.com</serviceAlias>
</data> <data>
 <code>stream</code>
 <serviceAlias>stream.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ecsbackup</code>
 <serviceAlias>ecsbackup.hbr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ros</code>
 <serviceAlias>ros.aliyuncs.com</serviceAlias>
</data> <data>
 <code>prometheus</code>
 <serviceAlias>prometheus.aliyuncs.com</serviceAlias>
</data> <data>
 <code>waf</code>
 <serviceAlias>waf.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cloudfw</code>
 <serviceAlias>cloudfw.aliyuncs.com</serviceAlias>
</data> <data>
 <code>dts</code>
 <serviceAlias>dts.aliyuncs.com</serviceAlias>
</data> <data>
 <code>sas</code>
 <serviceAlias>sas.aliyuncs.com</serviceAlias>
</data> <data>
 <code>edgepaas</code>
 <serviceAlias>edgepaas.aliyuncs.com</serviceAlias>
</data> <data>
 <code>bastionhost</code>
 <serviceAlias>bastionhost.aliyuncs.com</serviceAlias>
</data> <data>
```

```xml
 <code>cr</code>
 <serviceAlias>cr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cs</code>
 <serviceAlias>cs.aliyuncs.com</serviceAlias>
</data> <data>
 <code>hdm</code>
 <serviceAlias>hdm.aliyuncs.com</serviceAlias>
</data> <data>
 <code>csb</code>
 <serviceAlias>csb.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ons</code>
 <serviceAlias>ons.aliyuncs.com</serviceAlias>
</data> <data>
 <code>cloudmonitor</code>
 <serviceAlias>cloudmonitor.aliyuncs.com</serviceAlias>
</data> <data>
 <code>hdr</code>
 <serviceAlias>hdr.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ebs</code>
 <serviceAlias>ebs.aliyuncs.com</serviceAlias>
</data> <data>
 <code>ehpc</code>
 <serviceAlias>ehpc.aliyuncs.com</serviceAlias>
</data> <data>
 <code>asm</code>
 <serviceAlias>asm.aliyuncs.com</serviceAlias>
</data> <data>
 <code>config</code>
 <serviceAlias>config.aliyuncs.com</serviceAlias>
</data> <data>
 <code>pds</code>
 <serviceAlias>pds.aliyuncs.com</serviceAlias>
</data> <message>success</message> <success>true</success> <successResponse>true</successResponse>
```

#### 4.1.5. 计量接口相关参数

##### 4.1.5.1. 弹性计算

###### 4.1.5.1.1. 弹性高性能计算E-HPC

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍弹性高性能计算返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | E-HPC实例所属组织的名称。 |
| ResourceGId | 资源集id | E-HPC实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | E-HPC实例所属资源集的名称。 |
| InsId | 实例id | E-HPC实例的ID。 |
| RegionId | 区域 | E-HPC实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |

| CreateTime | 创建时间 | E-HPC实例的创建时间。 |
|---|---|---|
| Name | 实例名称 | E-HPC实例的名称。 |
| Status | 实例状态 | E-HPC实例的状态。 uninit：未初始化 creating：创建中 Init：初始化中 running：运行中 exception：异常 releasing：释放中 |
| InstanceType | 计算节点类型 | 集群计算节点的规格。例如：ecs.e4v2.xlarge 说明具体节点规格说明，请参见云服务器ECS实例规格族&实例规格手册。 |
| Count | 计算节点数 | 集群计算节点数量。取值范围：1~99。 |
| ClusterSumCoreTime | 集群总核时 | 集群总核时。 说明核时，即CPU核数*时间（小时）。 |
| ClusterUsedCoreTime | 集群已用核时 | 集群已用核时。 说明核时，即CPU核数*时间（小时）。 |
| SchedulerType | 调度器类型 | 调度服务器类型。 说明目前仅支持PBS。 |
| OsTag | 操作系统类型 | 操作系统镜像标签。 |

###### 4.1.5.1.2. 裸机管理BMS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍裸机管理返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | BMS实例所属组织的名称。 |
| ResourceGId | 资源集id | BMS实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | BMS实例所属资源集的名称。 |
| InsId | 实例id | BMS实例的ID。 |
| RegionId | 区域 | BMS实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 创建时间 | BMS实例的创建时间（UTC时间）。 |
| InstanceName | 实例名称 | BMS实例的名称。 |

| SN | 序列号 | BMS实例的序列号。 |
|---|---|---|
| ApplicationGroup | 实例类型 | BMS实例类型。取值： instance：纳管实例。 ib _stock：带内托管实例。 oob _stock：带外托管实例。 |
| BMCIP | 带外IP | BMS实例的带外IP。 |
| IP | 专有网络ID | BMS实例的VPC ID。 |

###### 4.1.5.1.3. 智能计算灵骏EFLOPS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍智能计算灵骏监控返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | EFLOPS实例所属组织的名称。 |
| ResourceGId | 资源集id | EFLOPS实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | EFLOPS实例所属资源集的名称。 |
| InsId | 实例id | EFLOPS实例的ID。 |
| RegionId | 区域 | EFLOPS实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| nodeHostname | 实例名称 | EFLOPS实例的名称 |
| imageType | 镜像类型 | EFLOPS实例镜像的类型。默认为eflops。 |
| image | 镜像名称 | EFLOPS实例镜像的名称。 |
| zoneId | 可用区ID | EFLOPS实例归属的可用区ID。 |
| ip | 网络地址 | EFLOPS实例的IP地址。 |
| nodeDesc | 节点规格 | EFLOPS实例的节点规格。例如： CPU：Intel * 1 \| 内存：1024GB \| 存储：SSD1024GB \| GPU：NVIDIA Tesla PCIe A10 24GB*8 |

###### 4.1.5.1.4. 容器镜像服务

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍容器镜像服务返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 容器镜像服务实例所属组织的名称。 |
| ResourceGId | 资源集id | 容器镜像服务实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 容器镜像服务实例所属资源集的名称。 |
| InsId | 实例id | 容器镜像服务实例的ID。 |

| RegionId | 区域 | 容器镜像服务实例所属的地域ID。 |
|---|---|---|
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | 容器镜像服务实例的创建时间。 |
| repoName | 仓库名称 | 仓库名称。长度限制1~64，支持英文小写字母、数字、短划线（-）、下划线（_） （不能以短划线和下划线开头）。 |
| repoNamespace | 命名空间 | 仓库所属命名空间。长度限制2~30，支持英文小写字母、数字、短划线（-）、下划线（_） （不能以短划线和下划线开头）。 |
| repoStatus | 仓库状态 | 仓库状态，取值： NORMAL ：正常。 DELETING ：删除中。 DELETED ：已删除。 |
| repoType | 仓库类型 | 仓库类型，取值： PUBLIC ：公开。 PRIVATE ：私有。 |
| repoAuthorizeType | 仓库权限 | 仓库权限。 |
| repoBuildType | 构建类型 | 仓库构建类型，取值： AUTO ：自动触发构建。 MANUAL ：手动触发构建。 |

###### 4.1.5.1.5. 容器服务Kubernetes版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍容器服务Kubernetes版返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 容器服务实例所属组织的名称。 |
| ResourceGId | 资源集id | 容器服务实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 容器服务实例所属资源集的名称。 |
| InsId | 实例id | 容器服务实例的ID。 |
| RegionId | 区域 | 容器服务实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间） |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间） |
| CreateTime | 实例创建时间 | 容器服务实例的创建时间。 |
| name | 集群名称 | 集群名称。 命名规则：由数字、汉字、英文字符或短划线（-）组成，长度范围1~63个字符， 且不能以短划线（-）开头。 |
| profile | 集群标识 | 集群标识，取值： Edge：边缘托管版集群。 Default：非边缘托管版集群。 |

| state | 运行状态 | 集群运行状态，取值： initial：集群创建中。 failed：集群创建失败。 running：集群运行中。 updating：集群升级中。 updating _failed：集群升级失败。 scaling：集群伸缩中。 stopped：集群已经停止运行。 deleting：集群删除中。 deleted：集群已经被删除。 delete _failed：集群删除失败。 |
|---|---|---|
| clustertype _ | 集群类型 | 集群类型，取值： Kubernetes: 专有版集群。 ManagedKubernetes：托管版集群。 Ask：Serverless集群。 ExternalKubernetes：注册集群。 |
| currentversion _ | 当前版本 | 集群当前版本。 |
| dockerversion _ | Docker版本 | 集群Docker版本。 |
| size | 节点数量 | 集群当前节点数量，包含Master节点以及 Worker节点。 |
| networkmode _ | 网络模式 | 集群网络模式，取值： classic：经典网络。 vpc：专有网络。 overlay：叠加网络。 calico：Calico网络。 |
| zoneid _ | 可用区ID | 集群所属可用区ID。 |
| securitygroupid _ _ | 安全组ID | 集群安全组ID。 |
| vpcid _ | 专有网络ID | 集群专有网络ID。 |
| vswitchid _ | 虚拟交换机ID | 虚拟交换机ID，创建集群时可选择1~3个虚拟交换机。为保证集群高可用，建议选择不同可用区的虚拟交换机，多个虚拟交换机ID之间用逗号分隔。 |
| privatezone _ | Private Zone配置 | 集群Private Zone配置，取值： true：启用Private Zone。 false：不启用Private Zone。 |
| deletionprotection _ | 集群删除保护 | 防止通过控制台或API误删除集群。取值： true：启用集群删除保护，将不能通过控制台或API删除集群。 false：不启用集群删除保护，则能通过控制台或API删除集群。 |

###### 4.1.5.1.6. 专有云宿主机DDH

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍专有云宿主机DDH返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | DDH实例所在的地域ID。 |
| ResourceGId | 资源集ID | DDH实例所属资源集的ID。 |
| InsId | 实例ID | DDH实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |

| OrgName | 组织名称 | DDH实例所属组织的名称。 |
|---|---|---|
| ResourceGName | 资源集名称 | DDH实例所属资源集的名称。 |
| ActionOnMaintenance | 当专有宿主机发生故障时，为其所宿实例设置迁移方案。 | 当专有宿主机发生故障时，为其所宿实例设置迁移方案。取值范围： Migrate：专有宿主机整机迁移至另一物理服务器，并对故障前非关机状态的实例进行启动。 Stop：在当前专有宿主机上停止实例，确认无法修复专有宿主机后，迁移实例到其他物理机并重新启动实例。 当专有宿主机上挂载云盘存储时，默认值为Migrate；当专有宿主机上挂载本地盘存储时默认值为Stop。 |
| AutoPlacement | 允许自动部署 | 专有宿主机是否加入自动部署资源池。取值范围： on：加入自动部署资源池。 off：不加入自动部署资源池。 |
| AvailableLocalStorage | 剩余的本地盘容量 | 剩余的本地盘容量。单位：GiB。 |
| AvailableMemory | 剩余的内存容量 | 剩余的内存容量。单位：GiB。 |
| AvailableVcpus | 剩余的vCPU核数 | 剩余的vCPU核数。 |
| AvailableVgpus | 可用虚拟GPU数量 | 可用虚拟GPU数量。 |
| ChargeType | 专有宿主机的计费方式 | 专有宿主机的计费方式。 |
| Cores | 物理核数 | 单个CPU的核数。 |
| CreateTime | 创建时间 | 实例的创建时间 |
| DedicatedHostClusterId | 所属宿主机组 | 专有宿主机集群ID。 |
| DedicatedHostName | 实例名称 | 专有宿主机的名称。 |
| DedicatedHostType | 主机类型 | 专有宿主机的规格类型。 |
| Description | 专有宿主机的描述信息 | 专有宿主机的描述信息。 |
| GPUSpec | GPU型号 | GPU型号。 |
| LocalStorageCategory | 本地盘类型 | 本地盘类型。 |
| OrgName | 组织名称 | 专有宿主机实例所属组织的名称。 |
| PhysicalGpu | 物理GPU数量 | 物理GPU数量。 |
| Sockets | Socket数 | 物理处理器（CPU）数量。 |
| Status | 实例状态 | 专有宿主机的使用状态。取值： Available：运行中。专有宿主机的正常运行状态。 UnderAssessment：物理机风险，即故障潜伏期，其物理机处于可用状态，但可能导致专有宿主机中的ECS实例出现问题。 PermanentFailure：故障。永久性故障，专有宿主机不可用。 |
| TotalMemory | 内存总容量 | 内存总容量。单位：GiB。 |
| TotalVcpus | vCPU总核数 | vCPU总核数。 |
| TotalVgpus | 总虚拟GPU数量 | 总虚拟GPU数量。 |
| ZoneId | 可用区ID | 可用区ID。 |

###### 4.1.5.1.7. 弹性伸缩ESS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍ESS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| LifecycleState | 状态 | 伸缩组的状态信息。取值范围： Active：生效状态，处于生效状态的伸缩组才能接收执行伸缩规则的请求并触发伸缩活动。 Inactive：失效状态，处于失效状态的伸缩组不接收任何执行伸缩规则的请求。 Deleting：伸缩组正在删除，处于删除中状态的伸缩组不接收任何执行伸缩规则的请求，并且不能修改伸缩组相关参数。 |
| ScalingPolicy | 回收模式 | 指定伸缩组的回收模式。取值范围： recycle：伸缩组的回收模式为停机回收模式 。 release：伸缩组的回收模式为释放模式 。 |
| VSwitchId | 虚拟交换机ID | 伸缩组关联虚拟交换机的ID。 |
| ScalingGroupName | 伸缩组名称 | 伸缩组的名称。 |
| VpcId | VPC ID | 伸缩组所属VPC的ID。 |
| MultiAZPolicy | 多可用区扩缩容策略 | 多可用区伸缩组ECS实例扩缩容策略。取值范围： PRIORITY：根据您定义的虚拟交换机扩缩容。当优先级较高的虚拟交换机所在可用区无法创建ECS实例时，自动使用下一优先级的虚拟交换机创建ECS实例。 COST _OPTIMIZED：按vCPU单价从低到高进行尝试创建。当伸缩配置设置了抢占式计费方式的多实例规格时，优先创建对应抢占式实例。 BALANCE：在伸缩组指定的多可用区之间均匀分配ECS实例。 |
| PendingWaitCapacity | 加入挂起中的数量 | 伸缩组中处于加入挂起状态的ECS实例的数量。 |
| TotalCapacity | 总数量 | 当伸缩组设置了实例规格权重，表示伸缩组内所有ECS实例的加权容量总和。否则，表示伸缩组内所有ECS实例的数量。 |
| RemovingWaitCapacity | 处于移除挂起中的数量 | 伸缩组中处于移除挂起状态的ECS实例的数量。 |
| ProtectedCapacity | 保护中的数量 | 伸缩组中处于保护中状态的ECS实例的数量。 |
| StandbyCapacity | 备用中的数量 | 伸缩组中处于备用状态的实例数量。 |
| RemovingCapacity | 移出中的数量 | 正在移出伸缩组的ECS实例的数量。 |
| PendingCapacity | 加入中的数量 | 正在加入伸缩组，还未完成相关配置的ECS实例的数量。 |
| ActiveCapacity | 服务中的数量 | 已成功加入伸缩组，并正常运行的ECS实例数量。 |
| StoppedCapacity | 停用中的数量 | 伸缩组中处于停机不收费状态的实例数量。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| MaxSize | 最大实例数 | 伸缩组内ECS实例台数的最大值。 |
| MinSize | 最小实例数 | 伸缩组内ECS实例台数的最小值。 |
| DefaultCooldown | 默认冷却时间 | 伸缩组默认的冷却时间。冷却时间内，该伸缩组不执行其它的伸缩活动，仅针对云监控报警任务触发的伸缩活动有效。 |

###### 4.1.5.1.8. 块存储EBS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍EBS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Description | 描述 | 云盘或本地盘描述。 |
| DiskCategory | 云盘或本地盘种类 | 云盘或本地盘种类。取值范围： all：所有云盘以及本地盘。 cloud：普通云盘。 cloud _efficiency：高效云盘。 cloud _ssd：SSD盘。 cloud _essd：ESSD云盘。 local _ssd _pro：I/O密集型本地盘。 local _hdd _pro：吞吐密集型本地盘。 ephemeral：（已停售）本地盘。 ephemeral _ssd：（已停售）本地SSD盘。 默认值：all。 |
| ExpiredTime | 过期时间 | 云盘的过期时间。 |
| ImageId | 镜像ID | 创建ECS实例时使用的镜像ID，只有通过镜像创建的云盘才有值，否则为空。这个值在云盘的生命周期内始终不变。 |
| Status | 云盘状态 | 云盘状态。取值范围： In _use。 Available。 Attaching。 Detaching。 Creating。 ReIniting。 All。 默认值：All。 |

| 字段 | 名称 | 描述 |
|---|---|---|
| AttachedTime | 挂载时间 | 挂载时间。 按照ISO8601标准表示，使用UTC+0时间。该参数值仅在Status参数值为Available时才有意义。 |
| BindInstanceId | 挂载的实例ID | 云盘或本地盘挂载的实例ID。该参数值仅在Status参数值为In _use时才有值，其他状态时为空。 |
| Device | 挂载点 | 云盘或本地盘的挂载点。 |
| DiskName | 云盘或本地盘名称 | 云盘或本地盘名称。 |
| Type | 云盘或本地盘类型 | 云盘或本地盘类型。可能值： system：系统盘。 data：数据盘。 |
| KMSKeyId | KMS密钥ID | 云盘使用的KMS密钥ID。 |
| DiskSize | 云盘或本地盘大小 | 云盘或本地盘大小，单位GiB。 |

###### 4.1.5.1.9. 快照Snapshot

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍Snapshot返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Status | 实例状态 | 快照状态。取值范围： progressing：正在创建的快照。 accomplished：创建成功的快照。 failed：创建失败的快照。 all（默认）：所有快照状态。 |
| Progress | 创建进度 | 快照创建的进度，示例：100%。 |
| Usage | 快照是否被使用 | 快照是否被用作创建镜像或云盘。取值范围： image：使用快照创建了自定义镜像。 disk：使用快照创建了云盘。 image _disk：使用快照创建了数据盘和自定义镜像。 none：暂未使用。 |
| Description | 快照描述 | 快照描述。 |

| 字段 | 名称 | 描述 |
|---|---|---|
| SnapshotCategory | 快照类型 | 快照类型。取值范围： standard：普通快照。 flash：本地快照。 |
| SnapshotName | 快照名称 | 快照名称。 |
| SourceDiskId | 源磁盘ID | 源磁盘ID。 |
| SourceStorageType | 源磁盘类型 | 源磁盘类型。 |
| SnapshotSN | 快照序列号 | 快照序列号。 |
| LastModifiedTime | 快照的最后变更时间 | 快照的最后变更时间。 按照ISO8601标准表示，并使用UTC +0时间，格式为yyyy-MM-ddTHH:mm:ssZ。 |
| SnapshotType | 快照创建类型 | 快照创建类型。可能值： auto或者timer：自动创建快照。 user：手动创建快照。 all：所有的快照创建类型。 |
| SourceDiskType | 源磁盘属性 | 源云盘属性。可能值：systemdata。 |
| SourceDiskSize | 源磁盘大小 | 源磁盘大小，单位：GiB。 |
| RetentionDays | 自动快照保留天数 | 自动快照保留天数。 |

###### 4.1.5.1.10. 云服务器ECS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍ECS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| ZoneId | 可用区 | 实例所属可用区。 |
| InstanceType | 实例规格 | ECS实例规格定义了实例的基本属性：CPU和内存（包括CPU型号、主频等）。 |
| InstanceTypeFamily | 实例规格族 | 根据业务场景和使用场景，ECS实例可以分为多种实例规格族。 根据CPU、内存等配置，一种实例规格族又分为多种实例规格。 |
| SerialNumber | 序列号 | ECS的序列号 |

| 字段 | 名称 | 描述 |
|---|---|---|
| InstanceNetworkType | 实例网络类型 | 实例的网络类型，一般分为： Classic：经典网络。 VPC：专有网络。 |
| ExpiredTime | 过期时间 | 实例过期时间。 |
| HostName | 主机名称 | ECS实例的主机名称。 |
| Status | 实例状态 | 实例状态。取值范围： Pending：创建中。 Running：运行中。 Starting：启动中。 Stopping：停止中。 Stopped：已停止。 |
| InstanceName | 实例名称 | ECS实例的实例名称。 |
| PrivateIpAddress | 内网IP地址 | VPC网络类型实例的私有IP。当InstanceNetworkType=vpc时生效，取值可以由多个IP组成。 |
| OSName | 系统名称 | 实例所装的系统的名称。 |
| EipAddress | 弹性外网IP | 实例的弹性公网IP列表。 |
| NatIpAddress | 网络转换地址 | ECS的公网或者私网IP地址。 |
| VpcId | 专有网络ID | 专有网络VPC ID。 |
| EipBandwidth | EIP带宽 | ECS绑定EIP的带宽。 |
| IoOptimized | 是否IO优化 | 是否是I/O优化型实例。 |
| InternetMaxBandwidthIn | 公网入带宽最大值 | 取值范围：1~200。 单位：Mbps。 |
| GPUAmount | GPU个数 | GPU实例对应的GPU数量。 单位：个 |
| GPUSpec | GPU型号 | GPU实例对应的GPU型号。 |
| InstanceBandwidthTx | 内网出方向带宽限制 | 单位：KB/s。 |
| Memory | 内存 | 内存大小。 单位：MB。 |
| Cpu | 处理器 | 处理器个数。 单位：个。 |
| SysDiskSize | 系统盘大小 | 系统盘大小。 单位：GB。 |
| DataDiskSize | 数据盘大小 | 数据盘大小。 单位：GB。 |

###### 4.1.5.1.11. 裸金属算力平台BMCP

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍裸金属算力平台BMCP返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |

| OrgName | 组织名称 | 实例所属组织的名称。 |
|---|---|---|
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CPUNumber | CPU核数 | CPU核数。 |
| GpuNum | GPU数量 | GPU数量。 |
| Memory | 内存(GB) | 内存容量，单位GB。 |
| VideoMemory | 显存（GB） | 显存容量，单位GB。 |

###### 4.1.5.1.12. 容器-智算算力集群

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍容器-智算算力集群返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| Status | 实例状态 | 实例的状态。 |
| CpuCount | CPU（核） | CPU核数，单位：核。 |
| MemCount | 内存（GB） | 内存容量，单位：GB。 |
| VideoMemory | 显存（GB） | 显存容量，单位：GB。 |
| FlopsCount | 算力（TFLOPS） | 算力，单位：TFLOPS。 |

###### 4.1.5.1.13. 裸金属-智算算力集群

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍裸金属-智算算力集群返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |

| OrgName | 组织名称 | 实例所属组织的名称。 |
|---|---|---|
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| Status | 实例状态 | 实例的状态。 |
| CpuCount | CPU（核） | CPU核数，单位：核。 |
| MemCount | 内存（GB） | 内存容量，单位：GB。 |
| VideoMemory | 显存（GB） | 显存容量，单位：GB。 |
| FlopsCount | 算力（TFLOPS） | 算力，单位：TFLOPS。 |

###### 4.1.5.1.14. 裸金属-超算算力集群

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍裸金属-超算算力集群返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| Status | 实例状态 | 实例的状态。 |
| CpuCount | CPU（核） | CPU核数，单位：核。 |
| MemCount | 内存（GB） | 内存容量，单位：GB。 |
| VideoMemory | 显存（GB） | 显存容量，单位：GB。 |
| FlopsCount | 算力（TFLOPS） | 算力，单位：TFLOPS。 |

###### 4.1.5.1.15. EVPC

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍EVPC返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|

| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
|---|---|---|
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |

**4.1.5.2. 存储**

###### 4.1.5.2.1. 表格存储Tablestore

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍Tablestore返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| InstanceType | 实例类型 | 实例类型，示例：ssd。 |
| TableName | 表名称 | 表名称。 |
| InstanceName | 实例名称 | 实例名称。 |
| Description | 实例注释 | 实例注释。 |
| Status | 实例状态 | 实例状态。 |
| Version | 数据库版本 | 数据库版本。 |

###### 4.1.5.2.2. 文件存储NAS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍NAS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Zone | 可用区 | 文件系统所在的可用区。 |
| VolumeType | 存储规格 | 包括以下几种规格： ssd：性能型。 hybrid：容量型。 |
| Description | 描述信息 | 文件系统的描述信息。 |
| ProtocolType | 协议类型 | 文件系统协议类型。包括： NFS：NFS文件协议。 SMB：SMB文件协议。 CPFS：CPFS文件系统支持的协议类型。 |
| StorageType | 存储类型 | 存储类型。包括： 通用型NAS：Capacity（容量型）、Performance（性能型）。 极速型NAS：standard（标准型）、advance（高级型）。 CPFS：advance _100（100 MB/s/TiB基线）、advance _200（200 MB/s/TiB基线）。 |
| Version | 版本号 | 文件系统版本号。该字段仅适用于极速型NAS。 |
| VolumeSize | 配额 | NAS存储的配额。单位：Bytes。 |
| UsedVolumeSize | 已用量 | NAS存储的已用量。单位：Bytes。 |
| MountTargets | 挂载点数量 | 挂载点数量。 |
| MeteredSize | 文件系统的使用量 | 文件系统的使用量。非实时使用量，为上一小时最大使用量，单位：Bytes。 |

###### 4.1.5.2.3. 对象存储OSS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍OSS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| ChargeType | 计费方式 | 取值范围： PayByBandwidth：按固定带宽计费。 PayByTraffic：按使用流量计费。 |
| StoreSpace | 容量阀值 | 对 Bucket 设置容量阈值，超过该阈值后，Bucket禁止写入操作。 单位：GB。 |
| CdnOut | CDN回源流量 | 从OSS流出至阿里云CDN的流量。 单位：Bytes。 |
| IntranetIn | 内网入流量 | 单位：Bytes。 |
| ChargedDatasize | 实际计费存储空间 | 低频（本地冗余LRS）或归档存储（本地冗余LRS）的实际计费存储空间。 单位：Bytes。 |
| GetRequest | GET请求次数 | 在StartTime和EndTime时间段内发生的GET请求次数。 |
| RetrievalData | 数据取回量 | 低频或归档存储的数据取回量。单位：Bytes。 |
| PutRequest | PUT请求次数 | 在StartTime和EndTime时间段内发生的PUT请求次数。 |
| IntranetOut | 内网出流量 | 单位：Bytes。 |
| ProcessI | 截帧张数 | 视频截帧的张数。 |
| ProcessImgSize | 图片处理量 | 图片处理量。 单位：Bytes。 |
| SelectScanSize | 扫描的数据量 | OSS select查询功能，扫描的数据量。 |
| NetworkOut | 网络出流量 | 在StartTime和EndTime时间段内发生的从OSS流出到外部网络的数据量。 单位：Bytes。 |
| Storage | 存储量 | 标准型（本地冗余LRS）存储空间。 单位：Bytes。 |
| NetworkIn | 网络入流量 | 在StartTime和EndTime时间段内发生的从外部网络流入OSS的数据量。 单位：Bytes。 |
| AvailabilityAverage _ | 可用性平均值 | EndTime时间点查询CMS获取的可用性平均值。 |
| AvailabilityMaximum _ | 可用性最大值 | EndTime时间点查询CMS获取的可用性最大值。 |
| AvailabilityMinimum _ | 可用性最小值 | EndTime时间点查询CMS获取的可用性最小值。 |
| MeteringStorageUtilizationAverage _ | 容量平均值 | EndTime时间点查询CMS获取的容量平均值。 单位：字节。 |
| MeteringStorageUtilizationMaximum _ | 容量最大值 | EndTime时间点查询CMS获取的容量最大值。 单位：字节。 |

| 字段 | 名称 | 描述 |
|---|---|---|
| MeteringStorageUtilizationMinimum _ | 容量最小值 | EndTime时间点查询CMS获取的容量最小值。 单位：字节。 |

###### 4.1.5.2.4. 日志服务SLS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍SLS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| description | 描述 | 实例描述。 |
| status | 状态 | 实例的状态。 |
| ShardSize | 活跃Shard个数 | 活跃Shard的个数，单位：个*天（包含小数）。 |
| OutflowSize | 读流量 | 从StartTime至EndTime时间段内（包含StartTime），日志服务的读流量大小（压缩后）， 单位：Bytes。 |
| InflowSize | 写流量 | 从StartTime至EndTime时间段内（包含StartTime），日志服务的写流量大小（压缩后）， 单位：Bytes。 |
| WriteCount | 写入次数 | 从StartTime至EndTime时间段内（包含StartTime），日志服务的写入次数。 |
| ReadCount | 读取次数 | 从StartTime至EndTime时间段内（包含StartTime），日志服务的读取次数。 |
| IndexSum | 总索引量大小 | 日志服务目前占用的总索引量大小，单位：Bytes。 |
| RawSum | 数据总大小 | 日志服务目前占用的总数据量大小，单位：Bytes。 |
| IndexSize | 索引的数据量 | 从StartTime至EndTime时间段内（包含StartTime），日志服务索引的数据量大小，单位： Bytes。 |

**4.1.5.3. 网络**

###### 4.1.5.3.1. 高可用虚拟IP

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍高可用虚拟IP（HaVip）返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | HaVip实例所属组织的名称。 |

| ResourceGId | 资源集id | HaVip实例所属资源集的ID。 |
|---|---|---|
| ResourceGName | 资源集名称 | HaVip实例所属资源集的名称。 |
| InsId | 实例id | HaVip实例的ID。 |
| RegionId | 区域 | HaVip实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | HaVip实例创建的时间。 |
| Name | 实例的名称 | HaVip实例的名称。 |
| Status | 实例状态 | HaVip实例的状态。取值： Creating：创建中。 Available：可用。 Deleting：删除中。 |
| AssociatedInstanceType | 绑定实例类型 | 与HaVip绑定的实例类型。取值： EcsInstance：云服务器ECS实例。 NetworkInterface：弹性网卡实例。 |
| AssociatedInstances | 与HaVip绑定的实例ID | 与HaVip绑定的实例ID。 |
| MasterInstanceId | 与HaVip绑定的主实例ID | 与HaVip绑定的主实例ID。 |
| IpAddress | 私网IP地址 | HaVip的私网IP地址。 |
| VpcId | 专有网络ID | HaVip实例所属的VPC ID。 |
| VSwitchId | 虚拟交换机ID | HaVip实例所属的虚拟交换机ID。 |

###### 4.1.5.3.2. 高速通道

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍高速通道返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 高速通道实例所属组织的名称。 |
| ResourceGId | 资源集id | 高速通道实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 高速通道实例所属资源集的名称。 |
| InsId | 实例id | 高速通道实例的ID。 |
| RegionId | 区域 | 高速通道实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | 高速通道实例的创建时间。 |

| ResourceType | 资源类型 | 高速通道分为专有网络对等连接、独享物理专线和边界路由器三种。专有网络对等连接分为VPC互连和VBR上连两种。 VRouter2VRouter：VPC互连 VBR2VRouter：VBR上连 VBR：边界路由器 PC：物理专线 |
|---|---|---|
| OppositeVpcInstanceId | 对端VPC的ID | 对等连接对端VPC的ID。 说明该字段为对等连接专属字段。 |
| OppositeInterfaceId | 对端路由器接口ID | 对等连接对端路由器接口的ID。 说明该字段为对等连接专属字段。 |
| OppositeRouterId | 连接对端的路由器接口所属的路由器ID | 对等连接对端的路由器接口所属的路由器ID。 说明该字段为对等连接专属字段。 |
| OppositeRegionId | 连接对端所在的地域ID | 对等连接对端所在的地域ID。 说明该字段为对等连接专属字段。 |
| VpcInstanceId | 对等连接中本端VPC的ID | 对等连接中本端VPC的ID。 说明该字段为对等连接专属字段。 |
| RouterId | 路由条目所在路由器的ID | 路由条目所在路由器的ID。 说明该字段为对等连接专属字段。 |
| BusinessStatus | 业务状态 | 路由器接口的业务状态。 Normal：正常 FinancialLocked：欠费锁定 SecurityLocked：安全风控锁定 |
| Spec | 路由器接口的规格 | 路由器接口的规格。 说明该字段为对等连接和物理专线的专属字段。 |
| Name | 名称 | 物理专线的名称。 说明该字段为物理专线专属字段。 |
| LineOperator | 提供接入物理线路的运营商 | 提供接入物理线路的运营商。 CT：中国电信。 CU：中国联通。 CM：中国移动。 CO：中国其他。 Equinix：Equinix。 Other：境外其他。 说明该字段为物理专线专属字段。 |

| PeerLocation | 本地数据中心的地理位置 | 本地数据中心的地理位置。 说明该字段为物理专线专属字段。 |
|---|---|---|
| AdLocation | 专线接入设备所在的物理位置 | 专线接入设备所在的物理位置。 说明该字段为物理专线专属字段。 |
| AccessPointId | 物理专线接入点的ID | 物理专线接入点的ID。 说明该字段为物理专线专属字段。 |
| PortType | 物理专线接入端口类型 | 物理专线接入端口的类型。 100Base-T：百兆电口。 1000Base-T：千兆电口。 1000Base-LX：千兆单模光口（10千米）。 10GBase-T：万兆电口。 10GBase-LR：万兆单模光口（10千米）。 说明该字段为物理专线专属字段。 |
| Bandwidth | 带宽 | 对等连接和物理专线的带宽。单位：Mbps。 说明该字段为对等连接和物理专线的专属字段。 |
| VbrType | 边界路由器类型 | 边界路由器类型。 说明该字段为边界路由器专属字段。 |

###### 4.1.5.3.3. NAT网关

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍NAT网关返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | NAT网关实例所属组织的名称。 |
| ResourceGId | 资源集id | NAT网关实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | NAT网关实例所属资源集的名称。 |
| InsId | 实例id | NAT网关实例的ID。 |
| RegionId | 区域 | NAT网关实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | NAT网关实例的创建时间。 |
| Name | 名称 | NAT网关实例的名称。 |

| Status | 状态 | NAT网关的状态。 Creating：创建NAT网关是异步操作，在创建完成之前是Creating状态。 Available：NAT网关创建完成后的状态，是稳定状态。 Modifying：变配NAT网关是异步操作，在变配的过程中是Modifying状态。 Deleting：删除NAT网关是异步操作，在删除的过程中是Deleting状态。 Converting：普通型NAT网关转换到增强型NAT网关是异步操作，在转换过程中是 Converting状态。 |
|---|---|---|
| Spec | 规格 | Small：小型 Middle：中型 Large：大型 |
| BusinessStatus | 业务状态 | Normal：正常 FinancialLocked：欠费锁定状态 |
| NatType | 类型 | Normal：普通型NAT网关 Enhanced：增强型NAT网关 |
| InternetChargeType | 计费类型 | PayBySpec：按固定规格计费 PayByLcu：按使用量计费 |
| VpcId | 网关所属的VPC的ID | NAT网关所属VPC的ID。 |
| Description | 描述 | NAT网关的描述。 |
| IpListSize | 网关绑定的弹性公网IP数量 | NAT网关绑定的弹性公网IP的数量。 |

###### 4.1.5.3.4. IPv6网关

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍IPv6网关返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | IPv6网关实例所属组织的名称。 |
| ResourceGId | 资源集id | IPv6网关实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | IPv6网关实例所属资源集的名称。 |
| InsId | 实例id | IPv6网关实例的ID。 |
| RegionId | 区域 | IPv6网关实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | IPv6网关实例的创建时间。 |
| Name | 网关名称 | IPv6网关的名称。 长度为2~128个字符，必须以字母或中文开头，可包含数字、下划线（_）和短划线（-），但不能以 http:// 或 https:// 开头。 |
| Spec | 规格 | IPv6网关的规格，取值： Small（默认值）：免费版。 Medium：企业版。 Large：企业增强版。 不同规格的IPv6网关的转发能力不同。 |
| Status | 运行状态 | IPv6网关的运行状态。 |

| BusinessStatus | 业务状态 | IPv6网关的业务状态，取值： Normal：正常。 FinancialLocked：欠费锁定。 |
|---|---|---|
| VpcId | 关联的VPC ID | IPv6网关关联的VPC ID。 |
| Description | 描述 | IPv6网关的描述信息。 |
| InstanceChargeType | 计费方式 | IPv6网关的计费方式。 |

###### 4.1.5.3.5. VPN网关

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍VPN网关返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | VPN网关实例所属组织的名称。 |
| ResourceGId | 资源集id | VPN网关实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | VPN网关实例所属资源集的名称。 |
| InsId | 实例id | VPN网关实例的ID。 |
| RegionId | 区域 | VPN网关实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | VPN网关实例的创建时间。 |
| Name | 网关的名称 | VPN网关的名称，默认值为VPN网关的ID。 长度为2~128个英文或中文字符，必须以大小字母或中文开头，可包含数字、下划线（_）和短划线（-），不能以 http:// 或 https:// 开头。 |
| Status | 网关的状态 | VPN网关的状态。 init：初始化。 provisioning：准备中。 active：正常。 updating：更新中。 deleting：删除中。 |
| IpsecVpn | IPSec功能状态 | 是否开启了IPsec-VPN功能。 enable：已开启 disable：未开启 |
| SslVpn | SSL功能状态 | 是否开启了SSL-VPN功能。 enable：已开启 disable：未开启 |
| Description | 描述 | VPN网关的描述。 |
| VpcId | 所属VPC的ID | VPN网关实例所属VPC的ID。 |
| VSwitchId | 所属交换机的ID | VPN网关实例所属交换机的ID。 |
| BusinessStatus | 付费状态 | VPN网关实例的付费状态。 Normal：正常。 FinancialLocked：欠费锁定。 |

| InternetIp | 公网IP | VPN网关的公网IP。 |
|---|---|---|
| ChargeType | 付费类型 | 付费类型。取值：PostpayByFlow。 |
| Spec | 带宽峰值 | VPN网关的带宽峰值，单位：Mbps。 |

###### 4.1.5.3.6. 专有网络VPC

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍VPC返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Status | 实例状态 | VPC的状态，取值： Pending：配置中。 Available：可用。 |
| CidrBlock | IPv4网段 | VPC的IPv4网段。 |
| VRouterId | 路由器ID | VPC路由器的ID。 |
| VpcName | VPC 名称 | VPC的名称。 |
| Ipv6CidrBlock | IPv6网段 | VPC的IPv6网段。 |
| Description | 描述信息 | VPC的描述信息。 |
| IsDefault | 默认专有网络 | 是否是该地域的默认VPC。 true：是该地域的默认VPC。 false：不是该地域的默认VPC。 |

###### 4.1.5.3.7. 弹性网关EIP

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍EIP返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| PrivateIpAddress | 内网IP地址 | 交换机网段内的一个IP地址。 |
| Name | 实例名称 | EIP实例的名称。 |
| ExpiredTime | 到期时间 | 按照ISO8601标准表示，并需要使用UTC时间。 格式为：YYYY-MM-DDThh:mmZ。 |
| BandwidthPackageId | 加入的共享带宽ID | 加入的共享带宽ID。 |
| Status | 实例状态 | EIP的状态。 Associating：绑定中。 Unassociating：解绑中。 InUse：已分配。 Available：可用。 |
| ISP | 线路类型 | 线路类型，取值： BGP CUCCAZ1 _ CMCCAZ1 _ PrivateEIPAZ1 _ CTCAZ1 _ |
| Mode | 绑定模式 | 绑定模式，取值： NAT（默认值）：NAT模式（普通模式）。 MULTI _BINDED：多EIP网卡可见模式。 BINDED：EIP网卡可见模式。 仅InstanceType配置为NetworkInterface时，才需要配置该参数。 |
| BandwidthPackageType | 带宽的类型 | 带宽的类型，仅支持返回CommonBandwidthPackage（共享带宽）。 |
| IpAddress | 网络地址 | EIP的IP地址。 |
| BindInstanceId | 绑定实例ID | 当前绑定实例的实例ID。 |
| BindInstanceType | 绑定实例类型 | 当前绑定的实例类型。 EcsInstance：VPC类型的ECS实例。 SlbInstance：VPC类型的SLB实例。 Nat：NAT网关。 HaVip：高可用虚拟IP。 NetworkInterface：辅助弹性网卡。 |
| BindInstanceName | 绑定实例名称 | 当前绑定的实例名称，当前值返回EcsInstance的实例名称。 |
| Bandwidth | 带宽峰值 | EIP的带宽峰值，单位：Mbps。 |

###### 4.1.5.3.8. 负载均衡SLB

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍SLB返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|

| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
|---|---|---|
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| ChargeType | 计费方式 | 取值范围： PayByBandwidth：按固定带宽计费。 PayByTraffic：按使用流量计费。 |
| StoreSpace | 容量阈值 | 对 Bucket 设置容量阈值，超过该阈值后，Bucket禁止写入操作。 单位：GB。 |
| CdnOut | CDN回源流量 | 从OSS流出至阿里云CDN的流量。 单位：Bytes。 |
| IntranetIn | 内网入流量 | 单位：Bytes。 |
| ChargedDatasize | 实际计费存储空间 | 低频（本地冗余LRS）或归档存储（本地冗余LRS）的实际计费存储空间。 单位：Bytes。 |
| GetRequest | GET请求次数 | 在StartTime和EndTime时间段内发生的GET请求次数。 |
| RetrievalData | 数据取回量 | 低频或归档存储的数据取回量。单位：Bytes。 |
| PutRequest | PUT请求次数 | 在StartTime和EndTime时间段内发生的PUT请求次数。 |
| IntranetOut | 内网出流量 | 单位：Bytes。 |
| ProcessI | 截帧张数 | 视频截帧的张数。 |
| ProcessImgSize | 图片处理量 | 图片处理量。 单位：Bytes。 |
| SelectScanSize | 扫描的数据量 | OSS select查询功能，扫描的数据量。 |
| NetworkOut | 网络出流量 | 在StartTime和EndTime时间段内发生的从OSS流出到外部网络的数据量。 单位：Bytes。 |
| Storage | 存储量 | 标准型（本地冗余LRS）存储空间。 单位：Bytes。 |
| NetworkIn | 网络入流量 | 在StartTime和EndTime时间段内发生的从外部网络流入OSS的数据量。 单位：Bytes。 |
| AvailabilityAverage _ | 可用性平均值 | EndTime时间点查询CMS获取的可用性平均值。 |
| AvailabilityMaximum _ | 可用性最大值 | EndTime时间点查询CMS获取的可用性最大值。 |
| AvailabilityMinimum _ | 可用性最小值 | EndTime时间点查询CMS获取的可用性最小值。 |

| MeteringStorageUtilizationAverage _ | 容量平均值 | EndTime时间点查询CMS获取的容量平均值。 单位：字节。 |
|---|---|---|
| MeteringStorageUtilizationMaximum _ | 容量最大值 | EndTime时间点查询CMS获取的容量最大值。 单位：字节。 |
| MeteringStorageUtilizationMinimum _ | 容量最小值 | EndTime时间点查询CMS获取的容量最小值。 单位：字节。 |

###### 4.1.5.3.9. 租户内网域名AUTH_ZONE

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍租户内网域名返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | AUTH _ZONE实例所属组织的名称。 |
| ResourceGId | 资源集id | AUTH _ZONE实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | AUTH _ZONE实例所属资源集的名称。 |
| InsId | 实例id | AUTH _ZONE实例的ID。 |
| RegionId | 区域 | AUTH _ZONE实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| Name | 实例名称 | AUTH _ZONE实例的名称。 |
| RecordCount | 解析记录集总数 | AUTH _ZONE实例记录集的总数。 |
| QueryPerDay | 查询量 | 请求量。 说明统计的是从运营商localdns向AUTH _ZONE发起的 AUTH _ZONE的请求次数，此统计不等同于网站访问量。 |

##### 4.1.5.4. 大数据

###### 4.1.5.4.1. 数据可视化DataV

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据可视化监控返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | DataV实例所属组织的名称。 |
| ResourceGId | 资源集id | DataV实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | DataV实例所属资源集的名称。 |
| InsId | 实例id | DataV实例的ID。 |
| RegionId | 区域 | DataV实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |

| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
|---|---|---|
| UserCount | 用户数量 | 已经登录过DataV的用户数量。 |
| ScreenCount | 大屏数量 | 已创建大屏的数量。 |

###### 4.1.5.4.2. 云原生深度学习训练PAI_DLC

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云原生深度学习训练返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | PAI _DLC实例所属组织的名称。 |
| ResourceGId | 资源集id | PAI _DLC实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | PAI _DLC实例所属资源集的名称。 |
| InsId | 实例id | PAI _DLC实例的ID。 |
| RegionId | 区域 | PAI _DLC实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| BillingType | 计费类型 | 计费类型。取值： byResource：按资源计费。 byMachineType：按机型计费。 |
| WorkspaceId | 工作空间ID | 资源所属工作空间ID。 |
| ResourceType | 资源类型 | 计算资源类型。取值： PAIEFLOPS _ PAIPAASTraining _ _ |
| ResourceId | 资源ID | 计算资源组的ID。 |
| ResourceName | 资源名称 | 计算资源组名称。 |
| RequestCpu | CPU核数 | 机器资源的CPU核数。 |
| RequestMemory | 内存 | 机器资源的内存。单位：MB。 |
| RequestGpu | GPU数量 | 机器资源GPU的数量。 |
| RunTime | 服务时长 | 任务或实例运行的时长。单位：秒。 |

###### 4.1.5.4.3. 模型在线服务PAI_EAS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍模型在线服务返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | PAI _EAS实例所属组织的名称。 |
| ResourceGId | 资源集id | PAI _EAS实例所属资源集的ID。 |

| ResourceGName | 资源集名称 | PAI _EAS实例所属资源集的名称。 |
|---|---|---|
| InsId | 实例id | PAI _EAS实例的ID。 |
| RegionId | 区域 | PAI _EAS实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 创建时间 | PAI _EAS实例的创建时间（UTC时间）。 |
| BillingType | 计费类型 | 计费类型。取值： ● byMachine：按机型计费。 ● byResource：按CPU和内存计费。 |
| MachineType | 机器型号 | 机器资源的型号。例如：ecs.gn5-c4g1.xlarge |
| MachineQuota | 机器数量 | 机器资源的数量。 |
| CPU | CPU核数 | 机器资源的CPU核数。 |
| Memory | 内存 | 机器资源的内存。单位：MB。 |

###### 4.1.5.4.4. 交互式建模PAI_DSW

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍交互式建模返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | PAI _DSW实例所属组织的名称。 |
| ResourceGId | 资源集id | PAI _DSW实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | PAI _DSW实例所属资源集的名称。 |
| InsId | 实例id | PAI _DSW实例的ID。 |
| RegionId | 区域 | PAI _DSW实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| BillingType | 计费类型 | 计费类型。取值： byResource：按资源计费。 byMachineType：按机型计费。 |
| WorkspaceId | 工作空间ID | PAI _DSW实例所属工作空间的ID。 |
| ResourceType | 资源类型 | 计算资源类型。取值： PAIEFLOPS _ PAIPAASTraining _ _ |
| ResourceId | 资源ID | 计算资源组ID。 |
| ResourceName | 资源名称 | 计算资源组的名称。 |
| RequestCpu | CPU核数 | 机器资源CPU的核数。 |

| RequestMemory | 内存 | 机器资源的内存。单位：MB。 |
|---|---|---|
| RequestGpu | GPU数量 | 机器资源GPU的数量。 |
| RunTime | 服务时长 | 任务或实例运行的时长。单位：秒。 |

###### 4.1.5.4.5. 交互式分析Hologres

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍交互式分析Hologres返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | Hologres实例所属组织的名称。 |
| ResourceGId | 资源集id | Hologres实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | Hologres实例所属资源集的名称。 |
| InsId | 实例id | Hologres实例的ID。 |
| RegionId | 区域 | Hologres实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | Hologres实例创建的时间。 |
| ComputeType | 实例规格 | Hologres实例的规格。 |
| IsAvailable | 目前实例状态 | Hologres实例当前的状态。 running：运行中。 suspend：用户主动停止。 其他：实例异常。 |
| CpuQuota | 创建一个实例申请的cpu数目（多少core) | 创建一个实例申请的CPU数目。 |
| MemPerCore | CPU内存比 | 单个Hologres实例的内存CPU比，计算公式为：内存/CPU。 |
| CU | 申请的CU数 | 创建一个实例申请的CU数。 |
| StorageUsage | 目前存储量 | 目前存储量，单位：Byte。 |
| MemQuota | 创建一个实例申请的内存大小 | 创建一个实例申请的内存大小，单位：MB。 |

###### 4.1.5.4.6. 大数据计算MaxCompute

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍大数据计算MaxCompute返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | MaxCompute实例所属组织的名称。 |
| ResourceGId | 资源集id | MaxCompute实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | MaxCompute实例所属资源集的名称。 |
| InsId | 项目名称 | MaxCompute项目的名称。 |

| RegionId | 区域 | MaxCompute实例所属的地域ID。 |
|---|---|---|
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间） |
| CreateTime | 实例创建时间 | MaxCompute实例的创建时间。 |
| EngineId | 引擎ID | MaxCompute引擎的ID。 |
| Cluster | 集群名称 | 集群名称。 |
| FileLengthQuota | 存储配额 | 逻辑存储配额，单位：GB。 |
| FileNumberQuota | 文件数配额 | 文件数配额，单位：个。 |
| FuxiQuotaId | 计算配额组(cu)id | 计算配额组（cu）ID。 |
| FuxiQuotaName | 计算配额组(cu)名称 | 计算配额组（cu）名称。 |
| MaxCu | 计算配置额最大cu | 计算配置额最大cu。 |
| MinCu | 计算配置额保障cu | 计算配置额保障cu。 |
| TotalCostCpu | 昨日总消耗cpu | 昨日总消耗CPU。 |
| TotalCostMen | 昨日总消耗mem | 昨日总消耗内存，单位：MB。 |
| TotalTaskNum | 昨日任务量 | 昨日任务量。 |
| StorageSize | 昨日盘古存储量 | 逻辑存储大小，单位GB。 |
| ds | 采集数据的日期 | 采集数据的日期。 |
| ODPSCompute | 扩展计算集群 | 扩展计算集群规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| ODPSComputeEE | 跨域软件增强包 | 跨域软件增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| isODPSFederationEE | 联合计算增强包 | 联合计算增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| isODPSMetaEE | 智能元数据软件增强包 | 智能元数据软件增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| isODPSInsideHadoopEE | InsideHadoop相关功能增强包 | InsideHadoop相关功能增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| isODPSVVPFlinkEE | VVP 增强包 | VVP On MaxCompute增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| odps.sql.decimal.odps2.0 | MaxCompute 2.0的Decimal数据类型的开关 | MaxCompute 2.0的Decimal数据类型配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |

| odps.sql.external.table.enable | 联合计算增强包 | 联合计算增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
|---|---|---|
| odps.sql.hive.compatible | MaxCompute Hive兼容模式 | MaxCompute Hive兼容模式配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| odps.sql.type.system.odps2.0 | MaxCompute 2.0数据类型版本 | MaxCompute 2.0数据类型版本配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |
| isODPSSecurity | 安全增强包 | 安全增强包规格配置项，取值： 0：表示关闭或者没有该配置。 1：表示开启。 |

###### 4.1.5.4.7. 数据总线DataHub

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据总线DataHub返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成 |
| OrgName | 组织名称 | DataHub实例所属组织的名称。 |
| ResourceGId | 资源集id | DataHub实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | DataHub实例所属资源集的名称。 |
| InsId | 实例id | DataHub实例的ID。 |
| RegionId | 区域 | DataHub实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | DataHub实例的创建时间。 |
| Comment | 项目名称 | DataHub项目名称。 |
| Creator | 创建者 | DataHub项目的创建者。 |
| StorageSize | 存储量 | DataHub项目下各个topic的汇总，单位GB。 |
| ActiveTime | 所有Shard的活跃时长 | 所有Shard的活跃时长。 说明该字段数据为DataHub项目下各个topic的汇总。 |
| WriteTimes | 写次数 | DataHub项目下各个topic写次数的汇总。 |
| ReadTimes | 读次数 | DataHub项目下各个topic读次数的汇总。 |
| WriteDataSize | 写流量 | DataHub项目下各个topic写流量的汇总，单位GB。 |
| ReadDataSize | 读流量 | DataHub项目下各个topic读流量的汇总，单位GB。 |
| ConnectorDataSize | Connector同步数据流量 | DataHub项目下各个topicConnector同步数据流量的汇总，单位GB。 |

###### 4.1.5.4.8. 实时计算Blink

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍实时计算Blink返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | Blink实例所属组织的名称。 |
| ResourceGId | 资源集id | Blink实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | Blink实例所属资源集的名称。 |
| InsId | 实例id | Blink实例的ID。 |
| RegionId | 区域 | Blink实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | Blink实例的创建时间。 |
| ClusterId | 集群ID | 集群ID。 |
| State | 项目状态 | 项目状态。 |
| TotalCu | 项目申请的cu数 | 项目申请的cu数。 |
| UsedCu | 项目使用的cu数 | 项目使用的cu数。 |
| DeployType | 集群类型 | 集群类型。 CELL：独享集群 PUBLIC：共享集群 |
| Description | 描述 | 集群描述。 |

###### 4.1.5.4.9. 实时计算Realtime Compute Flink

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍实时计算Realtime Compute Flink返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集id | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例id | 实例的ID。 |
| RegionId | 区域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| Queue | 队列名称 | 用户申请的namespace的名称。 |
| CpuUsed | 已使用的CU数 | 当前namespace已使用的CU数。 |

| GuaranteeQuota | 申请的CU数 | 用户申请的CU数。 |
|---|---|---|

##### 4.1.5.5. 中间件

###### 4.1.5.5.1. 云服务总线CSB

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云服务总线CSB返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | CSB实例所属组织的名称。 |
| ResourceGId | 资源集id | CSB实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | CSB实例所属资源集的名称。 |
| InsId | 实例id | CSB实例的ID。 |
| RegionId | 区域 | CSB实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | CSB实例的创建时间。 |
| InstanceName | 实例名称 | CSB实例名称。 |
| UserId | 用户ID | 用户ID。 |
| MemoryCount | 内存大小 | 内存大小，单位：MB。 |
| VCpuCount | CPU核数 | CPU核数。 |
| BrokerAddress | 节点地址 | CSB节点地址。 |

###### 4.1.5.5.2. 消息队列RocketMQ版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍消息队列RocketMQ版返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| cluster | 集群ID | 集群ID。 |
| instanceName | 实例名称 | 实例名称。 |
| spInstanceId | 实例ID | 实例ID。 |
| independentNaming | 是否有独立命名空间 | 是否有独立命名空间。 |
| instanceType | 实例类型 | 实例类型。 |
| instanceStatus | 实例状态 | 实例状态。 |
| topicCapacity | topic容量 | Topic容量。单位：个。 |

###### 4.1.5.5.3. 企业级分布式应用服务EDAS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍EDAS返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | EDAS实例所在的地域ID。 |
| ResourceGId | 资源集ID | EDAS实例所属资源集的ID。 |
| InsId | 实例ID | EDAS实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | EDAS实例所属组织的名称。 |
| ResourceGName | 资源集名称 | EDAS实例所属资源集的名称。 |
| EcsInstanceNum | ECS实例个数 | ECS实例个数。 |
| K8sInstanceNum | K8s实例个数 | K8s实例个数。 |
| ProductId | 产品ID | 产品ID。 |
| UserId | 用户ID | 用户ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |

##### 4.1.5.6. 数据库

###### 4.1.5.6.1. 云原生关系型数据库PolarDB

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云原生关系型数据库PolarDB返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | PolarDB实例所属组织的名称。 |
| ResourceGId | 资源集id | PolarDB实例所属资源集的ID。 |

| ResourceGName | 资源集名称 | PolarDB实例所属资源集的名称。 |
|---|---|---|
| InsId | 实例id | PolarDB实例的ID。 |
| RegionId | 区域 | PolarDB实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| DBClusterId | 集群ID | PolarDB实例所属集群的ID。 |
| DBClusterDescription | 集群名称 | PolarDB实例所属集群的名称。 |
| NodeId | 节点ID | PolarDB实例主节点的ID。 |
| StorageType | 集群磁盘类型 | PolarDB实例的磁盘类型。取值： essdpl1：高性能云盘一级。 essdpl2：高性能云盘二级。 essdpl3：高性能云盘三级。 |
| DiskSize | 集群磁盘容量 | PolarDB实例的磁盘容量大小。单位：GB。 |
| DBClusterNetworkType | 网络类型 | 实例的网络类型。默认为VPC，即VPC网络。 |
| VpcId | 虚拟专有网ID | PolarDB实例的VPC ID。 |
| DBInstanceSpec | 实例规格 | PolarDB实例的规格。 |
| HotStandbyCluster | 集群是否具备Standby节点 | ON：具备Standby节点。 OFF：不具备Standby节点。 |

###### 4.1.5.6.2. 数据传输服务DTS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据传输服务返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | DTS实例所属组织的名称。 |
| ResourceGId | 资源集id | DTS实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | DTS实例所属资源集的名称。 |
| InsId | 实例id | DTS实例的ID。 |
| RegionId | 区域 | DTS实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| Name | 实例名称 | DTS实例名称。 |

| Status | 实例状态 | 迁移任务状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Migrating：迁移中。 Suspending：暂停中。 MigrationFailed：迁移失败。 Finished：完成。 订阅任务的状态，返回值为： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Starting：启动中。 Normal：正常。 Abnormal：异常。 同步任务的状态，返回值： NotStarted：未启动。 Prechecking：预检查中。 PrecheckFailed：预检查失败。 Initializating ：同步初始化。 InitializeFailed：同步初始化失败。 Synchronizing ：同步中。 Failed：同步失败。 Suspending：暂停。 Modifying：同步对象变更中。 Finished：完成。 |
|---|---|---|
| SourceInstanceType | 源实例类型 | 源实例类型，取值为： RDS：阿里云RDS实例。 Redis：阿里云Redis实例。 PolarDB：阿里云PolarDB集群（仅支持MySQL或兼容 Oracle语法的引擎）。 ECS：ECS上的自建数据库。 Express：通过专线接入的自建数据库。 dg：通过数据库网关DG接入的自建数据库。 cen：通过云企业网CEN接入的自建数据库。 |
| SourceInstanceId | 源实例ID | 源实例的ID。 说明仅支持订阅任务和同步任务。 |
| SourceEngineName | 源数据库类型 | 源数据库类型，取值为：MySQL、Oracle。 说明仅支持同步任务。 |
| DestinationInstanceType | 目标实例类型 | 目标实例类型，取值为： Redis：阿里云Redis实例。 RDS：阿里云RDS实例。 PolarDB：阿里云PolarDB集群（仅支持MySQL或兼容 Oracle语法的引擎）。 ECS：ECS上的自建数据库。 Express：通过专线接入的本地数据库。 DataHub：阿里云DataHub实例。 MaxCompute：阿里云MaxCompute实例。 AnalyticDB：云原生数据仓库。AnalyticDB MySQL 3.0和2.0版本。 Greenplum：云原生数据仓库ADB PostgreSQL版（原分析型数据库PostgreSQL版）。 说明仅支持同步任务。 |

| DestinationInstanceId | 目标实例ID | 目标实例ID。 说明仅支持同步任务。 |
|---|---|---|
| DestinationEngineName | 目标数据库类型 | 目标数据库类型，取值为： MySQL：MySQL数据库（包括RDSMySQL和自建 MySQL）。 PolarDB：PolarDB MySQL。 polardb _o：PolarDB O引擎。 polardb _pg：PolarDB PostgreSQL。 Redis：Redis数据库（包括云数据库Redis和自建 Redis）。 DRDS：云原生分布式数据库PolarDB-X1.0和2.0。 PostgreSQL：自建PostgreSQL。 odps：MaxCompute。 oracle：自建Oracle。 mongodb：MongoDB数据库（包括云数据库MongoDB 和自建MongoDB）。 tidb：TiDB数据库。 ADS：云原生数仓AnalyticDB MySQL2.0。 ADB30：云原生数仓 AnalyticDB MySQL 3.0。 Greenplum：云原生数仓 AnalyticDB PostgreSQL。 MSSQL：SQL Server数据库（包括RDS SQL Server和自建SQL Server）。 kafka：Kafka数据库（包括消息队列Kafka版和自建 Kafka）。 DataHub：阿里云流式数据服务DataHub。 clickhouse：云数据库ClickHouse。 DB2：自建DB2 LUW。 as400：AS/400。 Tablestore：表格存储Tablestore。 说明仅支持同步任务。 |

###### 4.1.5.6.3. 数据管理DMS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据管理DMS返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | DMS实例所属组织的名称。 |
| ResourceGId | 资源集id | DMS实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | DMS实例所属资源集的名称。 |
| InsId | 实例id | DMS实例的ID。 |
| RegionId | 区域 | DMS实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| TenantId | 租户ID | 租户ID，同时也是实例ID。 |
| FreeNum | 自由操作实例数 | DMS自由操作管控模式实例数。 |
| SafeNum | 安全协同实例数 | DMS安全操作管控模式实例数。 |

###### 4.1.5.6.4. 图数据库GDB

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据图数据库GDB返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 图数据库实例所属组织的名称。 |
| ResourceGId | 资源集id | 图数据库实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 图数据库实例所属资源集的名称。 |
| InsId | 实例id | 图数据库实例的ID。 |
| RegionId | 区域 | 图数据库实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | 图数据库实例的创建时间。 |
| DBInstanceDescription | 名称 | 图数据库实例名称。 |
| Category | 实例系列 | 图数据库实例系列。 HA：高可用版。 SINGLE：单节点版。 |
| DBInstanceType | 实例类型 | 图数据库实例类型。取值为：common，即高可用版本。 |
| DBNodeClass | 实例规格 | 图数据库实例规格。 gdb.r.2xlarge：8核64GB gdb.r.4xlarge：16核128GB gdb.r.8xlarge：32核256GB gdb.r.13xlarge：52核384GB gdb.r5.16xlarge：64核512GB gdb.r.26xlarge：104核 768GB |
| DBInstanceStatus | 状态 | 图数据库实例状态。 Creating：创建中。 Running：使用中。 Deleting：删除中。 Rebooting：重启中。 DBInstanceClassChanging：升降级中。 NetAddressCreating：网络地址创建中。 NetAddressDeleting：网络地址删除中。 |
| DBVersion | 版本 | 图数据库内核版本。 1.0：gremlin。 1.0-OpenCypher：opencypher。 |
| MasterInstanceId | 主实例ID | 主实例ID，当此字段为空时，表示此实例为主实例。 |
| PayType | 付费类型 | 付费类型。Postpaid：按时付费。 |
| VpcId | 虚拟专有网ID | 图数据库实例所属VPC的ID。 |
| VSwitchId | 虚拟交换机ID | 图数据库实例所属交换机Vswitch的ID。 |
| DBNodeStorage | 存储空间 | 图数据库实例存储空间的大小。 |

###### 4.1.5.6.5. 云数据库OceanBase

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云数据库OceanBase返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | OceanBase实例所在的地域ID。 |
| ResourceGId | 资源集ID | OceanBase实例所属资源集的ID。 |
| InsId | 实例ID | OceanBase实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | OceanBase实例所属组织的名称。 |
| ResourceGName | 资源集名称 | OceanBase实例所属资源集的名称。 |
| ClusterId | 集群ID | 集群ID。 |
| TenantId | 租户ID | 租户ID。 |
| HostCount | 主机个数 | 主机个数。 |
| ClusterDisk | 集群磁盘总量 | 集群磁盘总量。 |
| ClusterCpu | 集群CPU核数 | 集群CPU的总核数。 |
| ClusterMemory | 集群内存总量 | 集群内存总量。 |
| DiskSiz | 租户磁盘使用量 | 租户磁盘使用量。 |
| CpuHolder | 租户CPU占用量 | 租户CPU占用量。 |
| MemoryHolder | 租户内存占用量 | 租户内存占用量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID |

###### 4.1.5.6.6. 时间序列数据库TSDB

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍TSDB返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| InstanceDescription | 实例描述 | 实例描述。 |
| InstanceTps | TPS | 实例TPS性能，单位：请求/秒。 |
| InstanceStorage | 实例存储 | 实例存储， 单位GB。 |
| ZoneId | 实例可用区ID | 实例可用区ID。 |
| InstanceClass | 实例规格 | 实例规格。 |
| InstanceAlias | 实例名称 | 实例名称。 |
| InstanceStatus | 实例状态 | 实例状态，取值如下： ACTIVATION：运行中。 CREATING：创建中。 NET _CREATING：创建网络链接中。 CLASS _CHANGING：实例变配中。 LOCKED：已锁定。 DELETED：已删除。 |
| ChargeType | 付费类型 | 付费类型： PREPAY：包年包月。 POSTPAY：按量付费。 |
| NetworkType | 实例网络类型 | 实例网络类型。 |
| ReverseVpcIp | 实例反向专有网络IP | 实例反向专有网络IP。 |
| ReverseVpcPort | 实例反向专有网络端口 | 实例反向专有网络端口。 |

###### 4.1.5.6.7. 云原生数据仓库AnalyticDB MySQL版2.0

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍ADS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| ClusterName | 集群名称 | 集群名称。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| Status | 实例状态 | 实例状态。 |
| ZoneId | 可用区 | 可用区。 |
| EcuType | ECU类型 | ECU类型。 |
| EcuCount | ECU数量 | ECU数量。 |

###### 4.1.5.6.8. 云数据库HBase版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍HBase返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| MasterInstanceType | Master节点规格 | 主节点实例类型，示例：hbase.sn1.2xlarge。 |
| NetworkType | 网络类型 | 网络类型： VPC：专有网络。 Classic：经典网络。 |
| CoreInstanceType | Core节点规格 | Core节点实例类型。 |
| ClusterId | 集群ID | 集群ID，系统生成的唯一标识码。 |
| ClusterName | 集群名称 | 集群名称。 |
| Engine | 数据引擎 | 产品引擎HBasesparkgeomesa。 |
| MajorVersion | 主版本 | 主版本号。 |
| Status | 集群状态 | 集群状态： CREATING：创建中。 ACTIVATION：运行中。 DELETING：删除中。 RESTARTING：重启中。 |
| PayType | 付费类型 | 付费类型： Prepaid：预付费。 Postpaid：后付费。 |
| VswitchId | 虚拟交换机ID | 虚拟交换机ID。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| InstanceName | 实例名称 | 实例名称。 |
| VpcId | 专有网络ID | 专有网络ID。 |
| CoreDiskType | Core节点磁盘类型 | core节点磁盘类型 cloud _efficiency：高效云盘。 cloud _ssd：ssd云盘。 |
| MasterDiskType | Master节点磁盘类型 | 主节点磁盘类型 cloud _efficiency：高效云盘。 cloud _ssd：SSD云盘。 |
| MasterNodeCount | Master节点数 | 主节点个数。 |
| CoreNodeCount | Core节点数 | Core节点数。 |
| CoreDiskSize | Core节点单磁盘大小 | Core节点单磁盘大小。 单位：GB。 |

###### 4.1.5.6.9. 云数据库SQLServer版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍RDS for SQLServer返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| DBInstanceDescription | 实例备注 | 实例备注。 |
| Category | 实例系列 | 实例系列，取值： Basic：基础版。 HighAvailability：高可用版。 AlwaysOn：集群版。 Finance：三节点企业版。 |
| ClassCode | 规格代码 | 规格代码，示例：mssql.x4.medium.s2。 |
| DBType | 数据库类型 | 数据库类型。 |
| DBVersion | 数据库版本 | 数据库版本。 |
| Zone | 可用区 | 可用区。 |

| 字段 | 名称 | 描述 |
|---|---|---|
| LockMode | 锁定模式 | 实例锁定模式： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前的自动锁定。 LockByDiskQuota：实例空间满自动锁定。 LockReadInstanceByDiskQuota：只读实例空间满自动锁定。 |
| DBInstanceStatus | 实例状态 | 实例状态。 |
| DBInstanceType | 实例类型 | 实例类型，取值： Primary：主实例。 Readonly：只读实例。 Guard：灾备实例。 Temp：临时实例。 |
| Port | 端口 | 内网连接端口。 |
| DBInstanceClassType | 实例规格族 | 实例规格族，取值： s：共享型。 x：通用型。 d：独享套餐。 h：独占物理机。 |
| DBInstanceStorageType | 储存类型 | 实例储存类型，取值： local _ssd或ephemeral _ssd：本地SSD盘。 cloud _ssd：SSD云盘。 cloud _essd：ESSD云盘。 |
| AvailabilityValue | 可用性状态 | 实例可用性状态，单位：百分比。 |
| IpAddress | IP地址 | IP地址。 |
| VPCId | VPC ID | VPC ID。 |
| BackupStorage | 备份存储量 | 备份存储量，单位：Bytes。 |
| IORequest | IO请求数 | IO请求数。 |
| NetworkIn | 网络入流量 | 在StartTime和EndTime时间段内发生的从外部网络流入的数据量，单位Bytes。 |
| NetworkOut | 网络出流量 | 在StartTime和EndTime时间段内发生的流出到外部网络的数据量，单位Bytes。 |
| Storage | 存储量 | 存储量，单位：Bytes。 |
| UsedStorage | 已用存储 | 已用存储空间，单位：Bytes。 |
| AccountMaxQuantity | 可创建账号的最大数量 | 可创建账号的最大数量。 |
| DBInstanceCPU | CPU个数 | 实例CPU数量。 |
| MaxConnections | 最大并发连接数 | 最大并发连接数。 |
| DBInstanceMemory | 内存 | 实例内存，单位：MB。 |
| DBInstanceDiskUsed | 已用存储 | 已用存储空间，单位：Bytes。 |
| MaxIOPS | 最大IOPS | 最大每秒IO请求次数。 |
| DBMaxQuantity | 可创建最大数据库数量 | 一个实例下可创建最大数据库数量。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| DBInstanceStorage | 存储 | 实例存储空间，单位：GB。 |

###### 4.1.5.6.10. 云数据库PostgreSQL版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍RDS for PostgreSQL返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Port | 端口 | 内网连接端口。 |
| DBInstanceClassType | 实例规格族 | 实例规格族，取值： s：共享型。 x：通用型。 d：独享套餐。 h：独占物理机。 |
| DBInstanceClass | 实例规格 | 实例规格，示例：rds.mys2.small。 |
| DBInstanceNetType | 内外网 | 实例是内网或外网，取值： Internet：外网。 Intranet：内网。 |
| DBInstanceType | 实例类型 | 实例类型，取值： Primary：主实例。 Readonly：只读实例。 Guard：灾备实例。 Temp：临时实例。 |
| InstanceNetworkType | 实例网络类型 | 实例的网络类型，取值： Classic：经典网络。 VPC：专有网络。 |
| DBInstanceDescription | 实例备注 | 实例备注。 |
| DBType | 数据库类型 | 数据库类型。 |
| DBVersion | 数据库版本 | 数据库版本。 |
| ZoneId | 可用区ID | 可用区ID。 |

| 字段 | 名称 | 描述 |
|---|---|---|
| LockMode | 锁定模式 | 实例锁定模式： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前的自动锁定。 LockByDiskQuota：实例空间满自动锁定。 LockReadInstanceByDiskQuota：只读实例空间满自动锁定。 |
| ConnectionMode | 访问模式 | 实例的访问模式，取值： Standard：标准访问模式。 Safe：数据库代理模式。 |
| DBInstanceStorageType | 储存类型 | 实例储存类型，取值： local _ssd或ephemeral _ssd：本地SSD盘。 cloud _ssd：SSD云盘。 cloud _essd：ESSD云盘。 |
| DBInstanceStatus | 实例状态 | 实例状态。 |
| AvailabilityValue | 可用性状态 | 实例可用性状态，单位：百分比。 |
| IpAddress | IP地址 | IP地址。 |
| VPCId | VPC ID | VPC ID。 |
| AccountMaxQuantity | 可创建账号的最大数量 | 可创建账号的最大数量。 |
| DBInstanceCPU | 实例CPU数量 | 实例CPU数量。 |
| MaxConnections | 最大并发连接数 | 最大并发连接数。 |
| DBInstanceMemory | 内存 | 实例内存，单位：MB。 |
| DBInstanceDiskUsed | 已用存储 | 已用存储，单位：Bytes。 |
| MaxIOPS | 最大IOPS | 最大每秒IO请求次数。 |
| DBMaxQuantity | 可创建最大数据库数量 | 一个实例下可创建最大数据库数量。 |
| DBInstanceStorage | 存储 | 实例存储空间，单位：GB。 |

###### 4.1.5.6.11. 云数据库MongoDB版本

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍MongoDB返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | MongoDB实例所属组织的名称。 |
| ResourceGId | 资源集id | MongoDB实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | MongoDB实例所属资源集的名称。 |
| InsId | 实例id | MongoDB实例的ID。 |
| RegionId | 区域 | MongoDB实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |

| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
|---|---|---|
| CreateTime | 实例创建时间 | MongoDB实例的创建时间。 |
| DBInstanceType | 实例类型 | MongoDB实例类型，取值如下： sharding：分片集群实例。 replicate：副本集实例或单节点实例。 默认值为replicate。 |
| ShardingType | 分片集类型 | 分片集群类型。取值： Shard Mongos ConfigServer 说明当字段DBInstanceType=sharding时才会有值。 |
| DBInstanceClass | 实例规格 | MongoDB实例规格。 |
| DBInstanceStatus | 实例状态 | MongoDB实例状态。 |
| DBInstanceStorage | 实例存储 | MongoDB实例存储空间。取值范围：10~3000，单位：GB。每10GB递增。 |
| ReplicateSetCount | 副本集数量 | 副本集数量。 说明 Mongos没有该字段。 |
| DBInstanceDescription | 描述 | MongoDB实例的描述。 |
| ZoneId | 可用区 | MongoDB实例所属的可用区ID。 说明您可以通过DescribeRegions接口查询可用的可用区。 |
| Engine | 引擎 | 数据库引擎，取值：MongoDB。 |
| EngineVersion | 引擎版本 | 数据库版本号，取值：3.2、3.4、4.0或4.2。 说明调用本接口用于克隆实例时，该值必须与源实例保持一致。 |
| CpuNum | CPU核数 | CPU核数。 |
| MemoryNum | 内存大小 | 内存大小，单位：GB。 |
| NetworkType | 网络类型 | 实例的网络类型，取值： classic：经典网络。 vpc：专有网络。 默认网络类型为经典网络。 说明当本参数值为vpc时，还需要传入 VpcId 参数和 VSwit chId 参数。 |

###### 4.1.5.6.12. 云原生数据仓库AnalyticDB PostgreSQL版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍GPDB返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |

| 字段 | 名称 | 描述 |  |
|---|---|---|---|
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |  |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |  |
| InsId | 实例ID | 实例的ID。 |  |
| RegionId | 地域 | 实例所属的地域ID。 |  |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |  |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |  |
| CreateTime | 实例创建时间 | 实例的创建时间。 |  |
| EngineVersion | 引擎版本 | 数据库版本。 |  |
| ZoneId | 可用区ID | 可用区ID。 |  |
| DBInstanceNetType | 网卡类型 | 实例网卡类型。 |  |
| InstanceNetworkType | 实例网络类型 | 实例网络类型： Classic：经典网络。 VPC：专有网络。 |  |
| DBInstanceDescription | 实例描述 | 实例描述。 |  |
| Engine | 引擎 | 数据库引擎。 |  |
| DBInstanceStatus | 实例状态 | 实例状态。 |  |
| LockMode | 锁定方式 | 锁定方： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前的自动锁定。 LockByDiskQuota：实例空间满自动锁定。 |  |
| LockReason | 锁定原因 | 锁定原因。 |  |
| ConnectionMode | 访问模式 | 访问模式。 Performance：标准访问模式。 Safty：高安全访问模式。 |  |
| HostType | 计算组机器类型 | 计算组机器类型取值： 0：SSD。 1：HDD。 |  |
| DBInstanceClass | 实例规格 | 实例规格。 |  |
| DBInstanceClassType | 实例规格族 | 实例规格族： s：共享型。 x：通用型。 d：独享套餐。 h：独占物理机。 |  |
| AvailabilityValue | 可用性状态 | 查询当前实例可用性状态，单位：百分比。 |  |
| VpcId | VPC ID | VPC ID。 |  |
| Port | 端口 | 端口。 |  |

| 字段 | 名称 | 描述 |
|---|---|---|
| DBInstanceDiskMBPS | 磁盘吞吐量 | Group最大的BPS（磁盘吞吐量），单位：Mbps。 |
| MaxConnections | 最大连接数 | 实例的最大并发连接数。 |
| DBInstanceGroupCount | 计算组Group数量 | 计算组Group数量。 |
| DBInstanceMemory | 内存 | 实例内存，单位：MB。 |
| DBInstanceStorage | 存储 | 实例存储空间，单位：GB。 |
| DBInstanceCpuCores | CPU | CPU核数。 |

###### 4.1.5.6.13. 云原生数据仓库AnalyticDB MySQL版3.0

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍ADB返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| DBClusterStatus | 实例状态 | 实例状态。 |
| DBClusterDescription | 实例描述 | 实例描述。 |
| LockMode | 实例锁定模式 | 实例锁定模式： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前自动锁定。 LockByDiskQuota：实例空间满自动锁定。 |
| DBNodeClass | 节点规格 | 节点规格。 |
| DBClusterType | 实例类型 | 实例类型： Common：常规。 RdsAnalysis：MySQL分析实例。 |
| DBVersion | 引擎版本 | 数据库版本。 |
| LockReason | 锁定原因 | 锁定原因。 |
| NetworkType | 网络类型 | 网络类型。 |
| Port | 端口 | 实例的端口。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| IPAddress | IP地址 | IP地址。 |
| VPCId | VPC ID | VPC ID。 |
| VSwitchId | 交换机ID | 交换机ID。 |
| DBNodeCount | 节点个数 | 节点个数。 |
| DBNodeStorage | 节点存储容量 | 存储空间，单位：GB。 |
| ConnectionUsageAverage _ | 连接数使用率平均值 | EndTime时间点查询CMS获取的连接数使用率平均值。 |
| ConnectionUsageMaximum _ | 连接数使用率最大值 | EndTime时间点查询CMS获取的连接数使用率最大值。 |
| ConnectionUsageMinimum _ | 连接数使用率最小值 | EndTime时间点查询CMS获取的连接数使用率最小值。 |
| CpuUsageAverage _ | CPU使用率平均值 | EndTime时间点查询CMS获取的CPU使用率平均值。 |
| CpuUsageMaximum _ | CPU使用率最大值 | EndTime时间点查询CMS获取的CPU使用率最大值。 |
| CpuUsageMinimum _ | CPU使用率最小值 | EndTime时间点查询CMS获取的CPU使用率最小值。 |
| DiskUsageAverage _ | 磁盘使用率平均值 | EndTime时间点查询CMS获取的磁盘使用率平均值。 |
| DiskUsageMaximum _ | 磁盘使用率最大值 | EndTime时间点查询CMS获取的磁盘使用率最大值。 |
| DiskUsageMinimum _ | 磁盘使用率最小值 | EndTime时间点查询CMS获取的磁盘使用率最小值。 |
| IOPSUsageAverage _ | IOPS使用率平均值 | EndTime时间点查询CMS获取的IOPS使用率平均值。 |
| IOPSUsageMaximum _ | IOPS使用率最大值 | EndTime时间点查询CMS获取的IOPS使用率最大值。 |
| IOPSUsageMinimum _ | IOPS使用率最小值 | EndTime时间点查询CMS获取的IOPS使用率最小值。 |
| MemoryUsageAverage _ | 内存使用率平均值 | EndTime时间点查询CMS获取的内存使用率平均值。 |
| MemoryUsageMaximum _ | 内存使用率最大值 | EndTime时间点查询CMS获取的内存使用率最大值。 |
| MemoryUsageMinimum _ | 内存使用率最小值 | EndTime时间点查询CMS获取的内存使用率最小值。 |

###### 4.1.5.6.14. 云数据库KVStore for Redis

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍Redis返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| ConnectionDomain | 私网连接地址 | 实例的私网连接地址。 |
| NetworkType | 网络类型 | 网络类型，返回值： CLASSIC：经典网络。 VPC：专有网络。 |
| InstanceStatus | 实例状态 | 实例状态。 |
| PackageType | 套餐类型 | 套餐类型，返回值： standard：标准套餐。 customized：定制套餐。 |
| InstanceType | 实例类型 | 实例类型。 |
| ArchitectureType | 实例的架构 | 实例的架构，返回值： cluster：集群版。 standard：标准版。 rwsplit：读写分离版。 |
| EngineVersion | 引擎版本 | 数据库版本。 |
| ZoneId | 可用区ID | 可用区ID。 |
| InstanceClass | 实例规格 | 实例规格。 |
| InstanceName | 实例名称 | 实例名称。 |
| NodeType | 节点类型 | 节点类型，返回值： double：双副本。 single：单副本。 |
| HasRenewChangeOrder | 是否有未生效的续费变配订单 | 是否有未生效的续费变配订单，返回值： true：是。 false：否。 |
| IsRds | 是否属RDS管控 | 是否属RDS管控，返回值： true：是。 false：否。 |
| Connections | 连接数 | 实例连接数限制。 |
| Port | 端口 | Redis服务端口。 |
| QPS | QPS | 理论最大QPS值。 |
| Capacity | 容量 | 存储容量， 单位：MB。 |
| Bandwidth | 带宽 | 带宽， 单位：MB/s。 |
| ConnectionUsageAverage _ | 连接数使用率平均值 | EndTime时间点查询CMS获取的连接数使用率平均值。 |
| ConnectionUsageMaximum _ | 连接数使用率最大值 | EndTime时间点查询CMS获取的连接数使用率最大值。 |
| ConnectionUsageMinimum _ | 连接数使用率最小值 | EndTime时间点查询CMS获取的连接数使用率最小值。 |
| FailedCountAverage _ | 失败数平均值 | EndTime时间点查询CMS获取的失败数平均值。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| FailedCountMaximum _ | 失败数最大值 | EndTime时间点查询CMS获取的失败数最大值。 |
| FailedCountMinimum _ | 失败数最小值 | EndTime时间点查询CMS获取的失败数最小值。 |
| IntranetInAverage _ | 写入带宽平均值 | EndTime时间点查询CMS获取的写入带宽平均值。 |
| IntranetInMaximum _ | 写入带宽最大值 | EndTime时间点查询CMS获取的写入带宽最大值。 |
| IntranetInMinimum _ | 写入带宽最小值 | EndTime时间点查询CMS获取的写入带宽最小值。 |
| IntranetInRatioAverage _ | 写入带宽使用率平均值 | EndTime时间点查询CMS获取的写入带宽使用率平均值。 |
| IntranetInRatioMaximum _ | 写入带宽使用率最大值 | EndTime时间点查询CMS获取的写入带宽使用率最大值。 |
| IntranetInRatioMinimum _ | 写入带宽使用率最小值 | EndTime时间点查询CMS获取的写入带宽使用率最小值。 |
| IntranetOutAverage _ | 读取带宽平均值 | EndTime时间点查询CMS获取的读取带宽平均值。 |
| IntranetOutMaximum _ | 读取带宽最大值 | EndTime时间点查询CMS获取的读取带宽最大值。 |
| IntranetOutMinimum _ | 读取带宽最小值 | EndTime时间点查询CMS获取的读取带宽最小值。 |
| IntranetOutRatioAverage _ | 读取带宽使用率平均值 | EndTime时间点查询CMS获取的读取带宽使用率平均值。 |
| IntranetOutRatioMaximum _ | 读取带宽使用率最大值 | EndTime时间点查询CMS获取的读取带宽使用率最大值。 |
| IntranetOutRatioMinimum _ | 读取带宽使用率最小值 | EndTime时间点查询CMS获取的读取带宽使用率最小值。 |
| MemoryUsageAverage _ | 内存使用率平均值 | EndTime时间点查询CMS获取的内存使用率平均值。 |
| MemoryUsageMaximum _ | 内存使用率最大值 | EndTime时间点查询CMS获取的内存使用率最大值。 |
| MemoryUsageMinimum _ | 内存使用率最小值 | EndTime时间点查询CMS获取的内存使用率最小值。 |

###### 4.1.5.6.15. 云原生分布式数据库PolarDB-X

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍PolarDB-X返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Status | 实例状态 | 实例状态。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| Description | 描述 | 数据库描述。 |
| InstanceSpec | 实例规格 | 实例的规格，示例：drds.sn2.4c16g.8C32G。 |
| ZoneId | 可用区ID | 可用区的ID。 |
| MachineType | 实例机器类型 | 实例机器类型，只有ECS。 |
| Label | 实例标签 | 实例标签： 普通实例：NORMAL。 高可用实例：HAVPC。 实例：VPC。 |
| InstanceSeries | 实例系列 | 实例的规格系列，示例：drds.sn2.4c16g/。 |
| VersionAction | 实例版本可用操作 | 实例版本可用操作。 |
| Type | 实例类型 | 实例类型： 独享实例PRIVATE。 共享实例PUBLIC。 |
| VpcId | VPC ID | VPC ID。 |
| OrderInstanceId | 购买的实例ID | 购买的实例ID。 |
| InstRole | 实例角色 | 实例角色： 主实例 MASTER。 分析型只读实例 SLAVE。 并发型只读实例 LAVE _FLOW。 |
| NetworkType | 网络类型 | 网络类型： 经典网络：CLASSIC。 VPC：专有网络。 |
| CommodityCode | 商品代码 | 商品代码。 |
| IpAddress | 网络地址 | IP地址。 |

###### 4.1.5.6.16. 云数据库 RDS MySQL版

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍RDS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| DBInstanceDescription | 实例备注 | 实例备注。 |
| Category | 实例系列 | 实例系列，取值示例： Finance：三节点企业版。 HighAvailability：双机高可用版本。 |
| ClassCode | 规格名称 | 规格代码，示例：rds.mysql.t1.small。 |
| DBType | 引擎类型 | 数据库类型，示例：MySQL。 |
| DBVersion | 引擎版本 | 数据库版本，示例：8.0。 |
| Zone | 可用区ID | 可用区ID。 |
| DBInstanceStatus | 实例状态 | RDS实例状态。 |
| DBInstanceType | 实例系列 | 实例类型，取值： Primary：主实例。 Readonly：只读实例。 Guard：灾备实例。 Temp：临时实例。 |
| LockMode | 锁定模式 | 实例锁定模式： Unlock：正常。 ManualLock：手动触发锁定。 LockByExpiration：实例过期自动锁定。 LockByRestoration：实例回滚前的自动锁定。 LockByDiskQuota：实例空间满自动锁定。 LockReadInstanceByDiskQuota：只读实例空间满自动锁定。 |
| Port | 端口 | 内网连接端口。 |
| DBInstanceClassType | 实例规格族 | 实例规格族，取值： s：共享型。 x：通用型。 d：独享套餐。 h：独占物理机。 |
| DBInstanceStorageType | 储存类型 | 实例储存类型，取值： local _ssd或ephemeral _ssd：本地SSD盘。 cloud _ssd：SSD云盘。 cloud _essd：ESSD云盘。 |
| AvailabilityValue | 可用性 | 实例可用性状态，单位：百分比。 |
| IpAddress | 网络地址 | IP地址。 |
| VPCId | VPC ID | VPC ID。 |
| BackupStorage | 备份存储量 | 单位：Bytes。 |
| NetworkIn | 网络入流量 | 在StartTime和EndTime时间段内发生的从外部网络流入RDS的数据量，单位：Bytes。 |
| NetworkOut | 网络出流量 | 在StartTime和EndTime时间段内发生的从RDS流出到外部网络的数据量，单位：Bytes。 |
| Storage | 存储量 | 总存储量。单位：Bytes。 |
| UsedStorage | 已使用存储量 | 已使用的存储量。单位：Bytes。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| AccountMaxQuantity | 可创建账号的最大数量 | 可创建账号的最大数量。 |
| DBInstanceCPU | CPU个数 | 实例CPU数量。 |
| MaxConnections | 最大连接数 | 最大并发连接数。 |
| DBInstanceMemory | 内存 | 实例内存，单位：MB。 |
| MaxIOPS | 最大IOPS | 最大每秒IO请求次数。 |
| DBMaxQuantity | 可创建最大数据库数量 | 一个实例下可创建最大数据库数量。 |
| CpuUsageMaximum _ | CPU使用率最大值 | EndTime时间点查询CMS获取的CPU使用率最大值。 |
| CpuUsageMinimum _ | CPU使用率最小值 | EndTime时间点查询CMS获取的CPU使用率最小值。 |
| DiskUsageAverage _ | 磁盘使用率平均值 | EndTime时间点查询CMS获取的磁盘使用率平均值。 |
| DiskUsageMaximum _ | 磁盘使用率最大值 | EndTime时间点查询CMS获取的磁盘使用率最大值。 |
| DiskUsageMinimum _ | 磁盘使用率最小值 | EndTime时间点查询CMS获取的磁盘使用率最小值。 |
| IOPSUsageAverage _ | IOPS使用率平均值 | EndTime时间点查询CMS获取的IOPS使用率平均值。 |
| IOPSUsageMaximum _ | IOPS使用率最大值 | EndTime时间点查询CMS获取的IOPS使用率最大值。 |
| IOPSUsageMinimum _ | IOPS使用率最小值 | EndTime时间点查询CMS获取的IOPS使用率最小值。 |
| MemoryUsageAverage _ | 内存使用率平均值 | EndTime时间点查询CMS获取的内存使用率平均值。 |
| MemoryUsageMaximum _ | 内存使用率最大值 | EndTime时间点查询CMS获取的内存使用率最大值。 |
| MemoryUsageMinimum _ | 内存使用率最小值 | EndTime时间点查询CMS获取的内存使用率最小值。 |

##### 4.1.5.7. 应用服务

###### 4.1.5.7.1. API网关

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍API网关返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |

| 开发指南·ASCM API参考 |  | 统一云管平台 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| ApiName | API名称 | API名称。 |
| GroupId | 分组ID | 指定的分组编号。 |
| GroupName | 分组名称 | 指定的分组名称。 |
| Visibility | 类型 | API类型。 |

##### 4.1.5.8. 人工智能与机器学习

###### 4.1.5.8.1. 在线服务

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍在线服务返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| ServiceId | 在线服务实例ID | 在线服务实例的ID。 |
| ServiceName | 在线服务实例名称 | 在线服务实例的名称。 |
| ApikeyUid | ApiKey的Uid | ApiKey的UID。 |
| ApikeyName | ApiKey的名称 | ApiKey的名称。 |
| InputTokenPerHour | 输入token数 | 每小时输入的token数量。 |
| OutputTokenPerHour | 输出token数 | 每小时输出的token数量。 |
| TotalInputToken | 总输入token数 | 总的输入token数量。 |
| TotalOutputToken | 总输出token数 | 总的输出token数量。 |
| ModelId | 模型ID | 模型的ID。 |
| ModelName | 模型名称 | 模型的名称。 |
| ModelType | 模型类型 | 模型的类型。 |
| ModelVersion | 模型版本 | 模型的版本。 |
| RequestCountPerHour | 调用次数 | 每小时的调用的次数。 |
| TotalRequestCount | 总调用次数 | 总的调用次数。 |

| FailedRequestCountPerHour | 失败调用次数 | 每小时失败的调用次数。 |
|---|---|---|
| FailedRequestRatio | 调用失败率 | 调用的失败率。 |
| TotalFailedRequestCount | 总失败调用次数 | 总的失败调用次数。 |

###### 4.1.5.8.2. AI资源配额（共享型）

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍AI资源配额（共享型）返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| ResourceQuotaName | 实例名称 | 实例的名称。 |
| ResourceQuotaMinElasticCpuCount | CPU弹性配额下限（核） | CPU弹性配额下限核数。 |
| ResourceQuotaMaxElasticCpuCount | CPU弹性配额上限（核） | CPU弹性配额上限核数。 |
| ResourceQuotaMinElasticMemCount | 内存弹性配额下限（GB） | 内存弹性配额下限容量。 |
| ResourceQuotaMaxElasticMemCount | 内存弹性配额上限（GB） | 内存弹性配额上限容量。 |
| ResourceQuotaMinElasticGpuCount | GPU弹性配额下限（卡数） | GPU弹性配额下限卡数。 |
| ResourceQuotaMaxElasticGpuCount | GPU弹性配额上限（卡数） | GPU弹性配额上限卡数。 |
| ResourceQuotaMinElasticGpuMemCount | 显存弹性配额下限（GB） | 显存弹性配额下限容量。 |
| ResourceQuotaMaxElasticGpuMemCount | 显存弹性配额上限（GB） | 显存弹性配额上限容量。 |
| UsageCpuCount | 已使用CPU（核） | 已使用CPU核数。 |
| UsageMemCount | 已使用内存（GB） | 已使用内存容量。 |
| UsageGpuCount | 已使用GPU（卡数） | 已使用GPU卡数。 |
| UsageGpuMemCount | 已使用显存（GB） | 已使用显存容量。 |
| ResourceType | 算力类型 | 算力类型。 |
| ResourceQuotaStatus | 实例状态 | 实例的状态。 |

###### 4.1.5.8.3. AI资源配额（独占型）

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍AI资源配额（独占型）返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| ResourceQuotaName | 实例名称 | 实例的名称。 |
| ResourceQuotaCpuCount | CPU配额（核） | CPU配额核数。 |
| ResourceQuotaMemCount | 内存配额（GB） | 内存配额容量。 |
| ResourceQuotaGpuCount | GPU配额（卡数） | GPU配额卡数。 |
| ResourceQuotaGpuMemCount | 显存配额（GB） | 显存配额容量。 |
| TotalNodeCount | 总节点数 | 总节点数量。 |
| UsageCpuCount | 已使用CPU（核） | 已使用的CPU核数。 |
| UsageMemCount | 已使用内存（GB） | 已使用的内存容量。 |
| UsageGpuCount | 已使用GPU（卡数） | 已使用的GPU卡数。 |
| UsageGpuMemCount | 已使用显存（GB） | 已使用的显存容量。 |
| ResourceType | 算力类型 | 算力类型。 |
| ResourceQuotaStatus | 实例状态 | 实例的状态。 |

###### 4.1.5.8.4. AI资源池

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍AI资源池返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |

| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
|---|---|---|
| ResourcePoolName | 实例名称 | 实例的名称。 |
| ResourcePoolCPU | CPU总数（核） | CPU总核数。 |
| ResourcePoolGPU | GPU总数（卡数） | GPU总卡数。 |
| ResourcePoolMem | 内存总数（GB） | 内存总容量。 |
| AssignedNodeCount | 已分配节点数 | 已分配的节点数。 |
| TotalNodeCount | 总节点数 | 总节点数。 |
| ResourcePoolStatus | 实例状态 | 实例的状态。 |

###### 4.1.5.8.5. 可视化建模

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍可视化建模返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域 | 实例所属的地域ID |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| Cpu | CPU(核时) | CPU的使用量，单位：核时。 |
| Memory | 内存(GB时) | 内存的使用量，单位：GB时。 |
| Gpu | GPU(卡时) | GPU的使用量，单位：卡时。 |
| GpuMemory | 显存(GB时) | 显存的使用量，单位：GB时。 |

**4.1.5.9. 安全**

###### 4.1.5.9.1. 云安全管理中心SOC

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云安全管理中心返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集id | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |

| InsId | 实例id | 实例的ID。 |
|---|---|---|
| RegionId | 区域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| DataStorageSize | 数据存储量 | SOC统一日志分析存储量，单位：Byte。 |

###### 4.1.5.9.2. 流量检测与响应

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍流量检测与响应返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集id | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例id | 实例的ID。 |
| RegionId | 区域 | 实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| InBytes | 入向流量 | 入向流量，单位：Byte。 |
| OutBytes | 出向流量 | 出向流量，单位：Byte。 |
| Qps | QPS | 每秒请求次数，单位：次。 |

###### 4.1.5.9.3. 密码服务

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍密码服务返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 密码服务实例所属组织的名称。 |
| ResourceGId | 资源集id | 密码服务实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 密码服务实例所属资源集的名称。 |
| InsId | 实例id | 密码服务实例的ID。 |
| RegionId | 区域 | 密码服务实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| CreateTime | 实例创建时间 | 密码服务实例创建的时间。 |

| CryptoServiceType | 密码服务类型 | 密码服务的类型。 KeyManger：密钥管理服务。 TransCrypto：数据加解密服务。 SslGateWay：SSL网关服务。 Sign：签名验签服务。 ESign：电子签章服务。 TimeStamp：时间戳服务。 DatabaseEncrypt：数据库加密服务。 FolderEncrypt：文件加密服务。 SslVpn：SSLVPN服务。 |
|---|---|---|
| InstanceCount | 密码服务数量 | 密码服务实例的数量。 |

###### 4.1.5.9.4. 加密服务

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍加密服务监控返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 加密服务实例所属组织的名称。 |
| ResourceGId | 资源集id | 加密服务实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 加密服务实例所属资源集的名称。 |
| InsId | 实例id | 加密服务实例的ID。 |
| RegionId | 区域 | 加密服务实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| InstanceNumber | 实例数量 | 用户在指定地域内使用加密服务实例的数量。 |

###### 4.1.5.9.5. 流量安全监控

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍流量安全监控返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 流量安全监控实例所在的地域ID。 |
| ResourceGId | 资源集ID | 流量安全监控实例所属资源集的ID。 |
| InsId | 实例ID | 流量安全监控实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 流量安全监控实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 流量安全监控实例所属资源集的名称。 |
| UsedNumber | 当前用户接入beaver产品的套数 | 当前用户接入Beaver产品的套数。 |
| ProductId | 产品ID | 产品ID。 |

| LastModify | 最后修改时间 | 最后修改时间。 |
|---|---|---|
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.6. DDos流量清洗

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍DDos流量清洗返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | DDos流量清洗实例所在的地域ID。 |
| ResourceGId | 资源集ID | DDos流量清洗实例所属资源集的ID。 |
| InsId | 实例ID | DDos流量清洗实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | DDos流量清洗实例所属组织的名称。 |
| ResourceGName | 资源集名称 | DDos流量清洗实例所属资源集的名称。 |
| UsedNumber | 当前用户接入aliguard的套数 | 当前用户接入aliguard的套数。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.7. 安骑士

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍安骑士返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 实例所在的地域ID。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| InsId | 实例ID | 实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| EcsNumber | 在安骑士产品中实际管理机器数量（含云外主机） | 在安骑士产品中实际管理机器数量（含云外主机）。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |

| UserId | 用户ID | 用户ID。 |
|---|---|---|

###### 4.1.5.9.8. 云防火墙CCFW

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云防火墙CCFW返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 云防火墙CCFW实例所在的地域ID。 |
| ResourceGId | 资源集ID | 云防火墙CCFW实例所属资源集的ID。 |
| InsId | 实例ID | 云防火墙CCFW实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 云防火墙CCFW实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 云防火墙CCFW实例所属资源集的名称。 |
| EcsNumber | 当前用户的ecs数量 | 当前用户拥有的云服务器ECS数量。 |
| VpcNumber | 当前用户的vpc数量 | 当前用户拥有的虚拟网络VPC数量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.9. WEB应用防火墙

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍WEB应用防火墙返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | WEB应用防火墙实例所在的地域ID。 |
| ResourceGId | 资源集ID | WEB应用防火墙实例所属资源集的ID。 |
| InsId | 实例ID | WEB应用防火墙实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | WEB应用防火墙实例所属组织的名称。 |
| ResourceGName | 资源集名称 | WEB应用防火墙实例所属资源集的名称。 |
| Count | 在WAF产品上回源站点的数量 | 在WEB应用防火墙产品上回源站点的数量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |

| UserId | 用户ID | 用户ID。 |
|---|---|---|

###### 4.1.5.9.10. 数据库审计

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍数据库审计返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 数据库审计实例所在的地域ID。 |
| ResourceGId | 资源集ID | 数据库审计实例所属资源集的ID。 |
| InsId | 实例ID | 数据库审计实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 数据库审计实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 数据库审计实例所属资源集的名称。 |
| DbCount | 已授权数据库连接数量 | 已授权数据库连接数量。 |
| InstanceNumber | 使用的数据库审计实例数量 | 使用的数据库审计实例数量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.11. 态势感知

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍态势感知返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 态势感知实例所在的地域ID。 |
| ResourceGId | 资源集ID | 态势感知实例所属资源集的ID。 |
| InsId | 实例ID | 态势感知实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 态势感知实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 态势感知实例所属资源集的名称。 |
| EcsNumber | 实际管理的ECS数量 | 态势感知实际管理的ECS数量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |

| UserId | 用户ID | 用户ID。 |
|---|---|---|

###### 4.1.5.9.12. 云防火墙ICFW

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云防火墙ICFW返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 云防火墙ICFW实例所在的地域ID。 |
| ResourceGId | 资源集ID | 云防火墙ICFW实例所属资源集的ID。 |
| InsId | 实例ID | 云防火墙ICFW实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 云防火墙ICFW实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 云防火墙ICFW实例所属资源集的名称。 |
| EcsNumber | 当前用户的ecs数量 | 当前用户拥有的云服务器ECS实例的数量。 |
| VpcNumber | 当前用户的vpc数量 | 当前用户拥有的虚拟网络VPC实例的数量。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.13. 云原生堡垒机

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍云原生堡垒机返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 云原生堡垒机实例所在的地域ID。 |
| ResourceGId | 资源集ID | 云原生堡垒机实例所属资源集的ID。 |
| InsId | 实例ID | 云原生堡垒机实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 云原生堡垒机实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 云原生堡垒机实例所属资源集的名称。 |
| InstanceNumber | 使用的堡垒机实例数量 | 使用的堡垒机实例数量。 |
| AssetCount | 授权的资产数量 | 授权的资产数量。 |
| ProductId | 产品ID | 产品ID。 |

| LastModify | 最后修改时间 | 最后修改时间。 |
|---|---|---|
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.14. 堡垒机

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍堡垒机返回的参数字段。

| 字段 | 中文名 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| RegionId | 区域 | 堡垒机实例所在的地域ID。 |
| ResourceGId | 资源集ID | 堡垒机实例所属资源集的ID。 |
| InsId | 实例ID | 堡垒机实例ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |
| OrgName | 组织名称 | 堡垒机实例所属组织的名称。 |
| ResourceGName | 资源集名称 | 堡垒机实例所属资源集的名称。 |
| InstanceNumber | 创建ECS时选择堡垒机镜像的实例个数 | 创建ECS时选择堡垒机镜像的实例个数 |
| AssetCount | 资源计数 | 资源计数。 |
| ProductId | 产品ID | 产品ID。 |
| LastModify | 最后修改时间 | 最后修改时间。 |
| UserId | 用户ID | 用户ID。 |

###### 4.1.5.9.15. 密钥管理服务KMS

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍KMS返回的参数字段。

| 字段 | 名称 | 描述 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | 实例所属组织的名称。 |
| ResourceGId | 资源集ID | 实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | 实例所属资源集的名称。 |
| InsId | 实例ID | 实例的ID。 |
| RegionId | 地域ID | 实例所属的地域ID。 |
| StartTime | 开始时间 | 数据所属时间片的开始时间，使用UTC时间。 |
| EndTime | 结束时间 | 数据所属时间片的结束时间，使用UTC时间。 |
| CreateTime | 实例创建时间 | 实例的创建时间。 |
| Description | 描述 | 密钥描述。 |

| 统一云管平台 |  | 开发指南·ASCM API参考 |
|---|---|---|

| 字段 | 名称 | 描述 |
|---|---|---|
| KeySpec | 密钥类型 | 密钥类型。 |
| KeyState | 密钥状态 | 密钥状态。 |
| KeyUsage | 密钥用途 | 密钥用途。 |
| PrimaryKeyVersion | 密钥主版本 | 密钥主版本。 |
| DeleteDate | 预计删除时间 | 预计删除时间。 |
| Creator | 创建者 | 创建者。 |
| KeyArn | 密钥ARN | 密钥ARN。 |
| Origin | 密钥材料来源 | 密钥材料来源。 |
| MaterialExpireTime | 密钥材料的过期时间 | 密钥材料的过期时间（UTC）。当该值为空时，表示密钥材料不会过期。 |
| ProtectionLevel | 保护级别 | 密钥的保护级别。 |
| AutomaticRotation | 自动轮转状态 | 是否开启自动密钥轮转，取值如下： Enabled：自动轮转处于开启状态。 Disabled：自动轮转处于未开启状态。 Suspended：自动轮转被暂停执行。 仅适用于对称类型的CMK。非对称类型的CMK不支持自动轮转。 |
| LastRotationDate | 上次轮转时间 | 最近一次轮转的时间（UTC）。如果是新创建密钥，则为初始密钥版本生成时间。 |

**4.1.5.10. 其他**

###### 4.1.5.10.1. 无影云桌面Gws

调用MeteringQuery获取计量内容后，除了公共返回参数外还会根据不同的产品，返回不同的参数。本文将为您介绍无影云桌面监控返回的参数字段。

| 字段 | 中文名 | 说明 |
|---|---|---|
| Pos | 数据主键 | 由产品、组织ID和开始时间组成。 |
| OrgName | 组织名称 | Gws实例所属组织的名称。 |
| ResourceGId | 资源集id | Gws实例所属资源集的ID。 |
| ResourceGName | 资源集名称 | Gws实例所属资源集的名称。 |
| InsId | 实例id | Gws实例的ID。 |
| RegionId | 区域 | Gws实例所属的地域ID。 |
| StartTime | 开始时间 | 计量数据所属时间片段的开始时间（UTC时间）。 |
| EndTime | 结束时间 | 计量数据所属时间片段的结束时间（UTC时间）。 |

| DesktopType | 云桌面规格 | Gws实例的规格。例如： eds.graphics.16c1t4 eds.graphics.24c1t4 eds.hf.12c24g eds.hf.8c16g eds.hf.4c8g eds.general.8c32g eds.general.16c32g eds.general.8c16g |
|---|---|---|
| EndUserID | 用户ID | 终端用户ID。 |
| TenantId | 租户ID | 阿里云账号ID |
| ConnectionTime | 连接时长 | Gws实例的使用时长。 |
| EcsInstanceId | ECS实例ID | Gws实例对应后端ECS实例的ID。 |
| EcsInstanceType | ECS实例规格 | Gws实例对应后端ECS实例的规格。 |
| SystemDiskCategory | 系统盘类型 | Gws实例系统盘的类型。取值： cloud：普通云盘 cloud _efficiency：高效云盘 cloud _ssd：SSD云盘 cloud _essd：ESSD云盘 |
| SystemDiskSize | 系统盘大小 | Gws实例系统盘的大小。单位：GB。 |
| GpuType | GPU规格 | Gws实例GPU的规格。 |
| GpuCount | GPU数量 | Gws实例GPU的数量。 |
| ZoneID | 可用区ID | Gws实例归属的可用区ID。 |

#### 4.1.6. 操作审计

##### 4.1.6.1. LookupInnerEvents

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /trails/innerOplog HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | String | Query | 否 | 1 | 角色Id。 |
| orgId | Long | Query | 否 | 3 | 组织Id。 |
| username | String | Query | 否 | ascm-org*** | 用户名称。 |
| serviceName | String | Query | 否 | ascm.productName.ros | 产品名称。 |
| keyword | String | Query | 否 | keyword | 关键词。 |
| sourceIp | String | Query | 否 | 10.XXX.XX.XX | 源Ip。 |
| resourceId | String | Query | 否 | 1 | 资源Id。 |

| 统一云管平台 |  |  |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| eventId | String | Query | 否 | 1 | 事件Id。 |
| eventRW | String | Query | 否 | Read | 读写类型。 |
| eventType | String | Query | 否 | SYSTEM | 事件类型。 |
| startTime | Long | Query | 否 | 1685721600000 | 开始时间。 |
| endTime | Long | Query | 否 | 1722441599000 | 结束时间。 |
| pageSize | Integer | Query | 否 | 10 | 单页数量。 |
| currentPage | Integer | Query | 否 | 1 | 当前页面。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 返回数据。 |
| -referencedResources | Array | - | 关联资源信息。 |
| --instanceId | String | dw91**** | 机器Id。 |
| --resourceType | String | ACS::SLB::LoadBalancer | 资源类型。 |
| --arnTag | String | - | arn信息。 |
| --rsName | String | SLB实例 | 实例名称。 |
| --multi | Boolean | false | 是否关联多个实例。 |
| -eventId | String | 1 | 事件Id。 |
| -eventVersion | Integer | 1 | 事件版本。 |
| -eventSource | String | normal | 事件来源。 |
| -requestParameterJson | Map | - | 请求参数。 |
| -sourceIpAddress | String | 10.XXX.XX.XX | 事件源Ip地址。 |
| -userAgent | String | - | userAgent。 |
| -eventRW | String | Read | 读写类型。 |
| -eventType | String | ConsoleOperation | 事件类型。 |
| -serviceName | String | ascm.productName.slb | 服务名称。 |
| -additionalEventData | Map | - | 附加事件信息。 |
| -apiVersion | String | 2014-05-15 | api版本。 |
| -requestId | String | a****** | 请求Id。 |
| -eventTime | String | 1722495439000 | 事件时间。 |
| -isGlobal | Boolean | false | isGlobal。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -acsRegion | String | cn-*****-******-d01 | 访问控制region。 |
| -eventName | String | 查看SLB | 事件名称。 |
| -errorCode | String | - | 错误码。 |
| -errorMessage | String | - | 错误信息。 |
| -resourceType | String | ACS::SLB::LoadBalancer | 资源类型。 |
| -instanceId | String | lb-dw********* | 机器Id。 |
| -instanceDetail | String | - | 事件详情。 |
| -apiName | String | DescribeLoadBalancerAttribute | 调用api。 |
| -status | String | 成功 | 调用api状态。 |
| -resourceName | String | SLB实例 | 资源名称。 |
| -responseElements | Map | - | 响应元素。 |
| -requestElements | Map | - | 请求元素。 |
| -headers | Map | ***** | 请求头。 |
| -eventApi | String | - | 事件Api。 |
| -source | String | 控制台调用 | 调用方式 |
| -product | String | SLB | 产品。 |
| -sourceIp | String | 10.XXX.XX.XX | 源ip。 |
| -url | String | - | 请求地址。 |
| -apiDesc | String | - | api信息。 |
| -userIdentity | Struct | - | 用户信息。 |
| --accessKeyId | String | *** | ak信息。 |
| --accessKeyType | Integer | 0 | ak类型。 |
| --accountId | String | *** | 用户Id。 |
| --principalId | String | *** | principalId。 |
| --principalName | String | - | principalName。 |
| --stsRoleName | String | - | sts角色名称。 |
| --type | String | root-account | 账号类型。 |
| --userName | String | ascm-org-170114**** | 用户名。 |
| --roleId | String | - | 角色Id。 |
| --roleName | String | - | 角色名称。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --orgId | String | 1 | 组织Id。 |
| --orgName | String | *** | 组织名称。 |
| --sysUid | String | 5012 | ascm用户Id。 |
| --resourceSetId | String | *** | 资源集Id。 |
| --resourceSetName | String | ResourceSet(*****) | 资源集名称。 |
| -docVO | Struct | - | api文档链接。 |
| --guideCode | String | enterprise-developer-guide | guideCode。 |
| --productCode | String | slb | 产品code。 |
| --productTitle | String | 负载均衡SLB | 产品标题。 |
| --guideTitle | String | 开发指南 | guide标题。 |
| code | Integer | 200 | 返回代码。 |
| message | String | true | 返回信息。 |
| success | Boolean | true | 是否成功。 |
| errorKey | String | null | 错误Key。 |
| pageInfo | Struct | - | 页码信息。 |
| -total | Long | 100 | 查询总数。 |
| -totalPage | Integer | 10 | 全部页码。 |
| -currentPage | Integer | 1 | 当前页码。 |
| -pageSize | Integer | 10 | 单页数量。 |

**示例**

请求示例

```
GET /trails/innerOplog HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
    "code": 200,
    "data": [
        {
            "apiName": "DescribeLoadBalancerAttribute",
            "docVO": {
```

`"productTitle": "`负载均衡 `SLB",`

```json
                "productCode": "slb",
```

`"guideTitle": "`开发指南`",`

```json
                "guideCode": "enterprise-developer-guide"
            },
            "eventVersion": 1,
            "responseElements": "",
            "eventSource": "normal",
            "sourceIpAddress": "10.XXX.XX.XX",
            "source": "ApiCall",
            "userIdentity": {
                "accessKeyId": "P7fsZ******",
                "accountId": "187670*****951",
                "accessKeyType": 0,
                "orgName": "dd-test",
                "roleId": "null",
                "sysUid": "5012",
                "resourceSetName": "ResourceSet(*****)",
                "principalId": "null",
                "type": "root-account",
                "userName": "ascm-org-1701142131832",
                "resourceSetId": "5",
                "orgId": "6"
            },
            "additionalEventData": {
                "originProductName": "slb",
                "uploadId": "lb-dw***********",
                "originalResourceType": "-"
            },
            "apiVersion": "2014-05-15",
            "instanceId": "7f0000011*******",
            "eventTime": 1722243689706,
            "eventName": "查看SLB",
            "eventId": "7f00000117222438680694302d0022",
            "instanceDetail": "null",
            "headers": "*****",
            "product": "ascm.productName.slb",
            "resourceName": "SLB实例",
            "eventRW": "Read",
            "eventType": "ApiCall",
            "referencedResources": [
                {
                    "instanceId": "lb-dw**********",
                    "rsName": "SLB实例",
                    "resourceType": "ACS::SLB::LoadBalancer",
                    "multi": false
                }
```

`],`

```json
            "serviceName": "ascm.productName.slb",
            "requestElements": "***",
            "sourceIp": "10.XXX.XX.XX",
            "isGlobal": false,
            "acsRegion": "cn-*****-******-d01",
            "resourceType": "-",
            "status": "ascm-monitor.src.util.operation-log-utils.Success"
        }
```

`],`

```json
    "pageInfo": {
        "total": 9964,
        "totalPage": 1,
        "pageSize": 10,
        "currentPage": 1
    }
}
```

`XML` 格式

```xml
<code>200</code> <data>
 <apiName>DescribeLoadBalancerAttribute</apiName>
 <docVO>
  <productCode>slb</productCode>
  <guideTitle>开发指南</guideTitle>
  <guideCode>enterprise-developer-guide</guideCode>
 </docVO>
 <eventVersion>1</eventVersion>
 <responseElements  />
 <eventSource>normal</eventSource>
 <sourceIpAddress>10.XXX.XX.XX</sourceIpAddress>
 <source>ApiCall</source>
 <userIdentity>
  <accessKeyId>P7fsZ******</accessKeyId>
  <accountId>187670*****951</accountId>
  <accessKeyType>0</accessKeyType>
  <orgName>dd-test</orgName>
  <roleId>null</roleId>
  <sysUid>5012</sysUid>
  <resourceSetName>ResourceSet(*****)</resourceSetName>
  <principalId>null</principalId>
  <type>root-account</type>
  <userName>ascm-org-1701142131832</userName>
  <resourceSetId>5</resourceSetId>
  <orgId>6</orgId>
 </userIdentity>
 <additionalEventData>
  <originProductName>slb</originProductName>
  <uploadId>lb-dw***********</uploadId>
  <originalResourceType>-</originalResourceType>
 </additionalEventData>
 <apiVersion>2014-05-15</apiVersion>
 <instanceId>7f0000011*******</instanceId>
 <eventTime>1722243689706</eventTime>
 <eventName>查看SLB</eventName>
 <eventId>7f00000117222438680694302d0022</eventId>
 <instanceDetail>null</instanceDetail>
 <headers>*****</headers>
 <product>ascm.productName.slb</product>
 <resourceName>SLB实例</resourceName>
 <eventRW>Read</eventRW>
 <eventType>ApiCall</eventType>
 <referencedResources>
  <instanceId>lb-dw**********</instanceId>
  <rsName>SLB实例</rsName>
  <resourceType>ACS::SLB::LoadBalancer</resourceType>
  <multi>false</multi>
 </referencedResources>
 <serviceName>ascm.productName.slb</serviceName>
 <requestElements>***</requestElements>
 <sourceIp>10.XXX.XX.XX</sourceIp>
 <isGlobal>false</isGlobal>
 <acsRegion>cn-*****-******-d01</acsRegion>
 <resourceType>-</resourceType>
 <status>ascm-monitor.src.util.operation-log-utils.Success</status>
</data> <pageInfo>
 <total>9964</total>
 <totalPage>1</totalPage>
 <pageSize>10</pageSize>
 <currentPage>1</currentPage>
</pageInfo>
```

##### 4.1.6.2. RetryAuditTask

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /trails/auditFile/action/retry HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | Long | Body | 否 | 3 | 转存任务Id（必填）。 |

| 开发指南·ASCM | API参考 |  |  |  | 统一云管平台 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| roleId | String | Body | 否 | 6 | 角色Id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Boolean | true | 转存任务是否成功。 |
| code | Integer | 200 | 返回code。 |
| message | String | success | 返回信息。 |
| success | Boolean | true | 是否成功。 |

**示例**

请求示例

```
POST /trails/auditFile/action/retry HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": 200, "data": true, "success": true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>true</data> <success>true</success> |  |

##### 4.1.6.3. ListAuditFile

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /trails/auditFile HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskName | String | Query | 否 | test | 下载任务名。 |
| username | String | Query | 否 | auditor | 创建者。 |
| currentUser | String | Query | 否 | auditor | 当前用户。 |
| status | String | Query | 否 | false | 任务状态code。 |
| startTime | Long | Query | 否 | 1721893052000 | 任务开始时间。 |
| endTime | Long | Query | 否 | 1721893080000 | 任务结束时间。 |
| pageSize | Integer | Query | 否 | 10 | 单页数量。 |
| pageIndex | Integer | Query | 否 | 1 | 当前页码。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 返回结果。 |
| -id | Long | 1 | id。 |
| -creator | String | auditor | 创建人。 |
| -taskName | String | test | 任务名。 |
| -taskType | Integer | 0 | 任务类型。 |
| -status | Integer | 3 | 状态。 |
| -startTime | Long | 1721893052000 | 开始时间。 |
| -endTime | Long | 1721893080000 | 结束时间。 |
| -url | String | https://ascm-default-backend- oss-2021-01.oss-cn-*****-******- d01- a.intra.env***.shuguang.com/aud itexport/test322.xlsx? _ _ _ Expires=******* | 下载链接(换链)。 |
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | true | 请求是否成功。 |
| errorKey | String | - | 错误码。 |
| pageInfo | Struct | - | 页码信息。 |
| -total | Long | 100 | 查询总数。 |
| -totalPage | Integer | 10 | 页码总数。 |
| -currentPage | Integer | 1 | 当前页码。 |
| -pageSize | Integer | 10 | 单页数量。 |

**示例**

请求示例

```
GET /trails/auditFile HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": 200, "data": [ { "creator": "auditor", "taskType": 0, "taskName": "test1", "startTime": 1721893052000, "id": 20, "endTime": 1721893080000, "status": 3 }, { "creator": "auditor", "taskType": 0, "taskName": "test", "startTime": 1721891258000, "id": 18, "endTime": 1721891282000, "status": 3 }, { |  |

```json
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "指定IP10.XXX.XX.XX",
            "startTime": 1718621642000,
            "id": 17,
            "endTime": 1718621701000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
```

`"taskName": "`日志转存测试`",`

```json
            "startTime": 1718621547000,
            "id": 16,
            "endTime": 1718621583000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "testecs",
            "startTime": 1717661204000,
            "id": 15,
            "endTime": 1717736071000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "test",
            "startTime": 1717660875000,
            "id": 14,
            "endTime": 1717686147000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "test111",
            "startTime": 1713509757000,
            "id": 13,
            "endTime": 1713509774000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
```

`"taskName": "`用户登录日志导出`",`

```json
            "startTime": 1709519931000,
            "id": 12,
            "endTime": 1709519955000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "test001",
            "startTime": 1709186060000,
            "id": 11,
            "endTime": 1709186278000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "auditor_baserservicetest_",
            "startTime": 1704802226000,
            "id": 9,
            "endTime": 1704804651000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "basesevice_all",
            "startTime": 1704802076000,
            "id": 8,
            "endTime": 1704802080000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
```

`"taskName": "`测试数据`",`

```json
            "startTime": 1704801277000,
            "id": 7,
```

```json
            "endTime": 1704801301000,
            "status": 3
        },
        {
            "creator": "auditor",
            "taskType": 0,
            "taskName": "test",
            "startTime": 1702283580000,
            "id": 5,
            "endTime": 1702283618000,
            "status": 3
        }
```

`],`

```json
    "pageInfo": {
        "total": 13,
        "pageSize": 20,
        "currentPage": 1
    }
}
```

| XML | 格式 |
|---|---|
| <code>200</code> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>test1</taskName> <startTime>1721893052000</startTime> <id>20</id> <endTime>1721893080000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>test</taskName> <startTime>1721891258000</startTime> <id>18</id> <endTime>1721891282000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>指定IP10.XXX.XX.XX</taskName> <startTime>1718621642000</startTime> <id>17</id> <endTime>1718621701000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>日志转存测试</taskName> <startTime>1718621547000</startTime> <id>16</id> <endTime>1718621583000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>testecs</taskName> <startTime>1717661204000</startTime> <id>15</id> <endTime>1717736071000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>test</taskName> <startTime>1717660875000</startTime> <id>14</id> <endTime>1717686147000</endTime> <status>3</status> </data> <data> <creator>auditor</creator> <taskType>0</taskType> <taskName>test111</taskName> <startTime>1713509757000</startTime> <id>13</id> <endTime>1713509774000</endTime> <status>3</status> </data> <data> |  |

```xml
<data>
 <creator>auditor</creator>
 <taskType>0</taskType>
```

`<taskName>`用户登录日志导出`</taskName>`

```xml
 <startTime>1709519931000</startTime>
 <id>12</id>
 <endTime>1709519955000</endTime>
 <status>3</status>
</data> <data>
 <creator>auditor</creator>
 <taskType>0</taskType>
 <taskName>test001</taskName>
 <startTime>1709186060000</startTime>
 <id>11</id>
 <endTime>1709186278000</endTime>
 <status>3</status>
</data> <data>
 <creator>auditor</creator>
 <taskType>0</taskType>
 <taskName>auditor_baserservicetest_</taskName>
 <startTime>1704802226000</startTime>
 <id>9</id>
 <endTime>1704804651000</endTime>
 <status>3</status>
</data> <data>
 <creator>auditor</creator>
 <taskType>0</taskType>
 <taskName>basesevice_all</taskName>
 <startTime>1704802076000</startTime>
 <id>8</id>
 <endTime>1704802080000</endTime>
 <status>3</status>
</data> <data>
 <creator>auditor</creator>
 <taskType>0</taskType>
```

`<taskName>`测试数据`</taskName>`

```xml
 <startTime>1704801277000</startTime>
 <id>7</id>
 <endTime>1704801301000</endTime>
 <status>3</status>
</data> <data>
 <creator>auditor</creator>
 <taskType>0</taskType>
 <taskName>test</taskName>
 <startTime>1702283580000</startTime>
 <id>5</id>
 <endTime>1702283618000</endTime>
 <status>3</status>
</data> <pageInfo>
 <total>13</total>
 <pageSize>20</pageSize>
 <currentPage>1</currentPage>
</pageInfo>
```

##### 4.1.6.4. ListTrailStorage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /trails/storage HTTP/1.1
```

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | true | 请求是否成功。 |
| data | Struct | - | 返回数据。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -metaInfos | Array | - | sls元数据信息。 |
| --orgId | String | 1 | 组织id。 |
| --endpoint | String | data.cn-*****-******- d01.sls.inter.******.shuguang.co m | 请求端点。 |
| --regionId | String | cn-*****-******-d01 | region名称。 |
| --project | String | ascm-asapi | sls 项目。 |
| --logStore | String | api-audit | 存放和管理日志数据的存储单元。 |
| -storeMode | Integer | 0 | 存储模式。其中： 0 表示sls-inner模式。 1 表示global模式。 2 表示tenant模式。 |
| -storageTime | Integer | 1722500571000 | 存储时间。 |
| -recordType | Integer | 0 | 操作事件记录类型。其中： 0 代表all类型。 1 代表write类型。 2 代表read类型。 |
| -userId | String | 0 | 用户ID。 |

**示例**

请求示例

```
GET /trails/storage HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": 200, "data": { "storeMode": 2, "storageTime": 30, "recordType": 0, "metaInfos": [ { "logStore": "test", "regionId": "cn-*****-******-d01", "project": "test", "orgId": "1" } ] }, "success": true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data> <storeMode>2</storeMode> <storageTime>30</storageTime> <recordType>0</recordType> <metaInfos> <logStore>test</logStore> <regionId>cn-*****-******-d01</regionId> <project>test</project> <orgId>1</orgId> </metaInfos> </data> <success>true</success> |  |

##### 4.1.6.5. ListAccessKeyEvents

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
GET /trails/accessKeyEvents HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| queryRegion | String | Query | 否 | cn-*****-******-d01 | 请求region。 |
| serviceName | String | Query | 否 | - | 服务名称。 |
| resourceType | String | Query | 否 | - | 资源类型。 |
| ip | String | Query | 否 | 10.XXX.XX.XX | 请求Ip。 |
| startTime | Long | Query | 否 | 1722494956000 | 开始时间。 |
| endTime | Long | Query | 否 | 1722494962000 | 结束时间。 |
| queryAk | String | Query | 否 | P7fs********73AVx | 请求AK。 |
| currentPage | Integer | Query | 否 | 1 | 当前页码。 |
| pageSize | Integer | Query | 否 | 10 | 单页数量。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Array | - | 返回数据。 |
| -referencedResources | Array | - | 关联资源信息。 |
| --instanceId | String | dw91**** | 机器Id。 |
| --resourceType | String | ACS::SLB::LoadBalancer | 资源类型。 |
| --arnTag | String | - | arn信息。 |
| --rsName | String | SLB实例 | 实例名称。 |
| --multi | Boolean | false | 是否关联多个实例。 |
| -eventId | String | 1 | 事件Id。 |
| -eventVersion | Integer | 1 | 事件版本。 |
| -eventSource | String | normal | 事件来源。 |
| -requestParameterJson | Map | *** | 请求参数。 |
| -sourceIpAddress | String | 10.XXX.XX.XX | 事件源Ip地址。 |
| -userAgent | String | - | userAgent。 |
| -eventRW | String | Read | 读写类型。 |
| -eventType | String | ApiCall | 事件类型。 |
| -serviceName | String | ascm.productName.slb | 服务名称。 |

| 统一云管平台 |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -additionalEventData | Map | - | 附加事件信息。 |
| -apiVersion | String | 2014-05-15 | api版本。 |
| -requestId | String | a****** | 请求Id。 |
| -eventTime | String | 1722495439000 | 事件时间。 |
| -isGlobal | Boolean | false | isGlobal。 |
| -acsRegion | String | cn-*****-******-d01 | 访问控制region。 |
| -eventName | String | 查看SLB | 事件名称。 |
| -errorCode | String | - | 错误码。 |
| -errorMessage | String | - | 错误信息。 |
| -resourceType | String | ACS::SLB::LoadBalancer | 资源类型。 |
| -instanceId | String | lb-dw********* | 机器Id。 |
| -instanceDetail | String | null | instanceDetail。 |
| -apiName | String | DescribeLoadBalancerAttribute | Api名称。 |
| -status | String | ascm-monitor.src.util.operation- log-utils.Success | 状态。 |
| -resourceName | String | SLB实例 | 资源名称。 |
| -responseElements | Map | - | 响应元素。 |
| -requestElements | Map | - | 请求元素。 |
| -headers | Map | ***** | 请求头。 |
| -eventApi | String | - | 事件Api。 |
| -source | String | ApiCall | 来源。 |
| -product | String | SLB | 产品。 |
| -sourceIp | String | 10.XXX.XX.XX | 来源Ip。 |
| -url | String | - | 请求地址。 |
| -apiDesc | String | - | api信息。 |
| -userIdentity | Struct |  | 用户信息。 |
| --accessKeyId | String | *** | ak信息。 |
| --accessKeyType | Integer | 0 | ak类型。 |
| --accountId | String | - | 用户Id。 |
| --principalId | String | null | principalId。 |
| --principalName | String | - | principalName。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| --stsRoleName | String | - | sts角色名称。 |
| --type | String | root-account | 账号类型。 |
| --userName | String | ascm-org-170114**** | 用户名。 |
| --roleId | String | - | 角色Id。 |
| --roleName | String | - | 角色名称。 |
| --orgId | String | 1 | 组织Id。 |
| --orgName | String | test | 组织名称。 |
| --sysUid | String | 5012 | ascm用户Id。 |
| --resourceSetId | String | 111 | 资源集Id。 |
| --resourceSetName | String | ResourceSet(*****) | 资源集名称。 |
| -docVO | Struct | - | api文档链接。 |
| --guideCode | String | enterprise-developer-guide | guideCode。 |
| --productCode | String | slb | 产品code。 |
| --productTitle | String | 负载均衡SLB | 产品标题。 |
| --guideTitle | String | 开发指南 | guide标题。 |
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | true | 请求是否成功。 |
| errorKey | String | null | 错误码。 |
| pageInfo | Struct | - | 分页信息。 |
| -total | Long | 100 | 查询总量。 |
| -totalPage | Integer | 10 | 页码总数。 |
| -currentPage | Integer | 1 | 当前页码。 |
| -pageSize | Integer | 10 | 单页数量。 |

**示例**

请求示例

```
GET /trails/accessKeyEvents HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
    "code": 200,
    "data": [
        {
            "apiName": "DescribeLoadBalancerAttribute",
            "docVO": {
```

`"productTitle": "`负载均衡 `SLB",`

```json
                "productCode": "slb",
```

`"guideTitle": "`开发指南`",`

```json
                "guideCode": "enterprise-developer-guide"
            },
            "eventVersion": 1,
            "responseElements": "",
            "eventSource": "normal",
            "sourceIpAddress": "10.XXX.XX.XX",
            "source": "ApiCall",
            "userIdentity": {
                "accessKeyId": "P7fsZ******",
                "accountId": "187670*****951",
                "accessKeyType": 0,
                "orgName": "dd-test",
                "roleId": "null",
                "sysUid": "5012",
                "resourceSetName": "ResourceSet(*****)",
                "principalId": "null",
                "type": "root-account",
                "userName": "ascm-org-1701142131832",
                "resourceSetId": "5",
                "orgId": "6"
            },
            "additionalEventData": {
                "originProductName": "slb",
                "uploadId": "lb-dw***********",
                "originalResourceType": "-"
            },
            "apiVersion": "2014-05-15",
            "instanceId": "7f0000011*******",
            "eventTime": 1722243689706,
            "eventName": "查看SLB",
            "eventId": "7f00000117222438680694302d0022",
            "instanceDetail": "null",
            "headers": "*****",
            "product": "ascm.productName.slb",
            "resourceName": "SLB实例",
            "eventRW": "Read",
            "eventType": "ApiCall",
            "referencedResources": [
                {
                    "instanceId": "lb-dw**********",
                    "rsName": "SLB实例",
                    "resourceType": "ACS::SLB::LoadBalancer",
                    "multi": false
                }
```

`],`

```json
            "serviceName": "ascm.productName.slb",
            "requestElements": "***",
            "sourceIp": "10.XXX.XX.XX",
            "isGlobal": false,
            "acsRegion": "cn-*****-******-d01",
            "resourceType": "-",
            "status": "ascm-monitor.src.util.operation-log-utils.Success"
        }
```

`],`

```json
    "pageInfo": {
        "total": 9964,
        "totalPage": 1,
        "pageSize": 10,
        "currentPage": 1
    }
}
```

`XML` 格式

```xml
<code>200</code> <data>
 <apiName>DescribeLoadBalancerAttribute</apiName>
 <docVO>
  <productCode>slb</productCode>
  <guideTitle>开发指南</guideTitle>
  <guideCode>enterprise-developer-guide</guideCode>
 </docVO>
 <eventVersion>1</eventVersion>
 <responseElements  />
 <eventSource>normal</eventSource>
 <sourceIpAddress>10.XXX.XX.XX</sourceIpAddress>
 <source>ApiCall</source>
 <userIdentity>
  <accessKeyId>P7fsZ******</accessKeyId>
  <accountId>187670*****951</accountId>
  <accessKeyType>0</accessKeyType>
  <orgName>dd-test</orgName>
  <roleId>null</roleId>
  <sysUid>5012</sysUid>
  <resourceSetName>ResourceSet(*****)</resourceSetName>
  <principalId>null</principalId>
  <type>root-account</type>
  <userName>ascm-org-1701142131832</userName>
  <resourceSetId>5</resourceSetId>
  <orgId>6</orgId>
 </userIdentity>
 <additionalEventData>
  <originProductName>slb</originProductName>
  <uploadId>lb-dw***********</uploadId>
  <originalResourceType>-</originalResourceType>
 </additionalEventData>
 <apiVersion>2014-05-15</apiVersion>
 <instanceId>7f0000011*******</instanceId>
 <eventTime>1722243689706</eventTime>
 <eventName>查看SLB</eventName>
 <eventId>7f00000117222438680694302d0022</eventId>
 <instanceDetail>null</instanceDetail>
 <headers>*****</headers>
 <product>ascm.productName.slb</product>
 <resourceName>SLB实例</resourceName>
 <eventRW>Read</eventRW>
 <eventType>ApiCall</eventType>
 <referencedResources>
  <instanceId>lb-dw**********</instanceId>
  <rsName>SLB实例</rsName>
  <resourceType>ACS::SLB::LoadBalancer</resourceType>
  <multi>false</multi>
 </referencedResources>
 <serviceName>ascm.productName.slb</serviceName>
 <requestElements>***</requestElements>
 <sourceIp>10.XXX.XX.XX</sourceIp>
 <isGlobal>false</isGlobal>
 <acsRegion>cn-*****-******-d01</acsRegion>
 <resourceType>-</resourceType>
 <status>ascm-monitor.src.util.operation-log-utils.Success</status>
</data> <pageInfo>
 <total>9964</total>
 <totalPage>1</totalPage>
 <pageSize>10</pageSize>
 <currentPage>1</currentPage>
</pageInfo>
```

##### 4.1.6.6. CreateTrailStorage

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求语法**

```
POST /trails/storage HTTP/1.1
```

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| storeMode | Integer | Body | 否 | 0 | 存储模式。其中： 0 表示sls-inner模式。 1 表示global模式。 2 表示tenant模式。 |
| storageTime | Integer | Body | 否 | 30 | 全局，保存时间。 |
| metaInfos | RepeatList | Body | 否 | - | sls元数据信息。 |
| -orgId | String | Body | 否 | 1 | 组织id。 |
| -endpoint | String | Body | 否 | - | sls endpoint。 |
| -regionId | String | Body | 否 | cn-*****-******-d01 | sls regionId。 |
| -project | String | Body | 否 | ascm-asapi | sls项目。 |
| -logStore | String | Body | 否 | api-audit | sls存放和管理日志数据的存储单元。 |
| recordType | Integer | Body | 否 | 0 | 操作事件记录类型。其中： 0 代表all类型。 1 代表write类型。 2 代表read类型。 |
| userId | String | Body | 否 | 0 | 用户ID。 |
| roleId | String | Body | 否 | 0 | 角色Id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | ture | 请求是否成功。 |
| data | Struct | - | 返回数据。 |
| -metaInfos | Array | - | sls元数据信息。 |
| --orgId | String | 1 | 组织id。 |
| --endpoint | String | - | sls endpoint。 |
| --regionId | String | cn-*****-******-d01 | sls regionId。 |
| --project | String | ascm-asapi | sls项目。 |
| --logStore | String | api-audit | 存放和管理日志数据的存储单元。 |
| -storeMode | Integer | 0 | 存储模式。其中： 0 表示sls-inner模式。 1 表示global模式。 2 表示tenant模式。 |
| -storageTime | Integer | 30 | 全局，保存时间。 |
| -recordType | Integer | 0 | 操作事件记录类型。其中： 0 代表all类型。 1 代表write类型。 2 代表read类型。 |

| 开发指南·ASCM AP | I参考 |  | 统一云管平台 |
|---|---|---|---|
| 参数名称 | 类型 | 示例 | 说明 |
| -userId | String | 1 | 用户Id。 |

**示例**

请求示例

```
POST /trails/storage HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code":200, "data":{ "storeMode":0, "storageTime":30, "recordType":0, "metaInfos":{ "logStore":"api-audit", "endpoint":"-", "regionId":"cn-*****-******-d01", "project":"ascm-asapi", "orgId":"1" }, "userId":"1" }, "success":false, "message":"true" } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data> <storeMode>0</storeMode> <storageTime>30</storageTime> <recordType>0</recordType> <metaInfos> <logStore>api-audit</logStore> <endpoint>-</endpoint> <regionId>cn-*****-*****-d01</regionId> <project>ascm-asapi</project> <orgId>1</orgId> </metaInfos> <userId>1</userId> </data> <success>false</success> <message>true</message> |  |

##### 4.1.6.7. DownloadAuditFile

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| startTime | Long | Body | 否 | 1721891230000 | 开始时间。 |
| endTime | Long | Body | 否 | 1721891231000 | 结束时间。 |
| pageSize | Integer | Body | 否 | 10 | 单页数量。 |
| reportName | String | Body | 否 | test4 _ | 转存名称。 |
| currentPage | Integer | Body | 否 | 1 | 当前页码。 |
| orgId | Long | Body | 否 | 3 | 组织id。 |
| username | String | Body | 否 | test | 用户名称。 |

| 统一云管平台 |  |  |  |  | 开发指南·ASCM API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| serviceName | String | Body | 否 | ascm | 产品类型。 |
| keyword | String | Body | 否 | test | 关键词。 |
| sourceIp | String | Body | 否 | 10.XXX.XX.XX | 源Ip。 |
| resourceId | String | Body | 否 | 0 | 资源Id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Long | 19 | 转存Id。 |
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | ture | 请求是否成功。 |

**示例**

请求示例

```
POST /trails/auditFile/action/download HTTP/1.1
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "code": 200, "data": 19, "success": true } |  |

| XML | 格式 |
|---|---|
| <code>200</code> <data>19</data> <success>true</success> |  |

##### 4.1.6.8. GetDownloadUrl

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| taskId | String | Query | 否 | 3 | 任务Id。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | String | - | 下载链接。 |
| code | Integer | 200 | 返回码。 |
| message | String | true | 返回信息。 |
| success | Boolean | true | 请求是否成功。 |

**示例**

请求示例

```
GET /trails/auditFileUrl HTTP/1.1
```

正常返回示例 `JSON` 格式

```json
{
    "code": 200,
    "data": "https://ascm-default-backend-oss-2021-01.oss-cn-*****-******-d01-a.intra.env***.shuguang.com/audit_export/test_3_22.xlsx?
Expires=*******",
    "success": true
}
```

`XML` 格式

```xml
<code>200</code> <data>https://ascm-default-backend-oss-2021-01.oss-cn-*****-******-d01-a.intra.env***.shuguang.com/audit_export/test_3_22.xlsx?Expires=******* </data> <success>true</success>
```

## STS API参考

### 获取STS的Endpoint

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint，您可以通过如下方法自行获取Endpoint。

**操作步骤**

1. 登录Apsara-Uni manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**首页**中的**API****集成**页签下，单击**查看云产品调用****Endpoint****访问地址**。
4. 在**云产品****Endpoint**页面的**归属产品**选择**统一云管平台**后，获取STS的Endpoint访问地址。

### AssumeRole - 获取扮演角色的临时身份凭证

通过调用AssumeRole接口，获取一个扮演RAM角色的临时身份凭证（STS Token）。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| DurationSeconds | Long | Query | 否 | 3600 | Token有效期。单位：秒。 Token有效期最小值为900秒，最大值为要扮演角色的MaxSessionDuration时间。默认值为3600 秒。 |
| Policy | String | Query | 否 | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | 为STS Token额外添加的一个权限策略，进一步限制STS Token的权限。具体如下： 如果指定该权限策略，则STS Token最终的权限策略取RAM角色权限策略与该权限策略的交集。 如果不指定该权限策略，则STS Token最终的权限策略取RAM角色的权限策略。 长度为1~1024个字符。 |

| RoleArn | String | Query | 是 | acs:ram::123456789012****:role/adminrole | 要扮演的RAM角色ARN。 该角色是可信实体为阿里云账号类型的RAM角色。 更多信息，请参见创建可信实体为阿里云账号的 RAM角色或CreateRole。 格式：acs:ram:: <account _id>:role/<role _name> 。 |
|---|---|---|---|---|---|
| RoleSessionName | String | Query | 是 | alice | 角色会话名称。 该参数为用户自定义参数。通常设置为调用该API 的用户身份，例如：用户名。在操作审计日志中， 即使是同一个RAM角色执行的操作，也可以根据不同的RoleSessionName来区分实际操作者，以实现用户级别的访问审计。 长度为2~64个字符，可包含英文字母、数字和特殊字符.@- _。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5-88FA- F32781734A7F | 请求ID。 |
| Credentials | Struct |  | 访问凭证。 |
| -SecurityToken | String | ******** | 安全令牌。 说明安全令牌的长度不固定，我们强烈建议您不要对安全令牌的最大长度做任何限制。 |
| -AccessKeySecret | String | wyLTSmsyPGP1ohvvw8xYgB29dl GI8KMiH2pK**** | 访问密钥。 |
| -AccessKeyId | String | STS.L4aBSCSJVMuKg5U1**** | 访问密钥ID。 |
| -Expiration | String | 2015-04-09T11:52:19Z | Token到期失效时间（UTC时间）。 |
| AssumedRoleUser | Struct |  | 角色扮演时的临时身份。 |
| -Arn | String | acs:ram::123456789012****:role/ adminrole/alice | 临时身份的ARN。 |
| -AssumedRoleId | String | 34458433936495****:alice | 临时身份的ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=AssumeRole &RoleArn=acs:ram::123456789012****:role/adminrole &RoleSessionName=alice
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"6894B13B-6D71-4EF5-88FA-F32781734A7F", "AssumedRoleUser":{ "Arn":"acs:ram::123456789012****:role/adminrole/alice ", "AssumedRoleId":"34458433936495****:alice" }, "Credentials":{ "SecurityToken":"********", "AccessKeyId":"STS.L4aBSCSJVMuKg5U1****", "AccessKeySecret":"wyLTSmsyPGP1ohvvw8xYgB29dlGI8KMiH2pK****", "Expiration":"2015-04-09T11:52:19Z" } } |  |

### GetCallerIdentity - 获取当前调用者的身份信息

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| IdentityType | String | RAMUser | 身份类型。取值： Account：阿里云账号（主账号）。 RAMUser：RAM用户。 AssumedRoleUser：RAM角色。 |
| AccountId | String | 196813200012**** | 当前调用者所属阿里云账号ID。 |
| RequestId | String | 3C87BF47-3724-5443-ADC1- 5AEAD9A03EB1 | 请求ID。 |
| PrincipalId | String | 28877424437521**** | 身份标识。 |
| UserId | String | 216959339000**** | 用户ID。具体如下： 如果当前调用者是阿里云账号，则返回阿里云账号ID。 如果当前调用者是RAM用户，则返回RAM用户ID。 仅限当前调用者是阿里云账号或RAM用户时返回该参数。 |
| Arn | String | acs:ram::196813200012****:user /admin | 当前调用者的ARN。 |
| RoleId | String | 33537620082992**** | RAM角色ID。 仅限当前调用者是RAM角色时返回该参数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=GetCallerIdentity
```

正常返回示例

| JSON | 格式 |
|---|---|
| { "IdentityType":"RAMUser", "AccountId":"196813200012****", "RequestId":"3C87BF47-3724-5443-ADC1-5AEAD9A03EB1", "PrincipalId":"28877424437521****", "UserId":"216959339000****", "Arn":"acs:ram::196813200012****:user/admin", "RoleId":"33537620082992****" } |  |

## 开发者门户 API参考

### GetApiInfo

获取开发者门户的指定OpenApi信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Product | String | Query | 是 | ecs | 云产品Code。 |
| ExtVersion | String | Query | 是 | 2014-05-26 | 云产品版本。 |
| Api | String | Query | 是 | DeleteInstance | 接口名称。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| data | Struct | { "httpMethod": [ "POST" ], "httpProtocol": [ "HTTP", "HTTPS" ], "id": 5098, "invokeGatewayType": [ "POP" ], "metaType": "POPXML", "name": _ "ActivateUser", "product": "ascm", "status": "ENABLED", "version": "2019-05-10", "zhName": "激活用户账号" } | 返回数据。 |

**示例**

请求示例

```
&Product=ecs &ExtVersion=2014-05-26 &Api=DeleteInstance
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "data":"{ \"httpMethod\": [ \"POST\" ], \"httpProtocol\": [ \"HTTP\", \"HTTPS\" ], \"id\": 5098, \"invokeGatewayType\": [ \"POP\" ], \"metaType\ \"POP_XML\", \"name\": \"ActivateUser\", \"product\": \"ascm\", \"status\": \"ENABLED\", \"version\": \"2019-05-10\", \"zhName\": \"激活用户账号\" }", "requestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### GetProductList

获取开发者门户的产品列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| data | Struct | { "code": "cms", "category": "监控与运维服务", "categoryEn": "Alarm", "productName": "云监控", "productNameEn": "CloudMonitor", "categorySort": "10", "productSort": "120", "deployment": true, "apiList": [ { "extVersion": "2017-03-01", "content": [ { "content": "其他", "zhContent": "", "isTerminalNode": false, "apiCode": "", "namespace": "", "extVersion": "", "subNode": [ { "content": "AccessKeyGenerate", "zhContent": "生成专有云API访问密钥", "isTerminalNode": true, "apiCode": "AccessKeyGenerate", "namespace": "Cms", "extVersion": "2017-03-01", "subNode": null } ] } ] } ] } | 返回数据。 |

**示例**

| JSON | 格式 |
|---|---|
| { "data":"{ \"code\": \"cms\", \"category\": \"监控与运维服务\", \"categoryEn\": \"Alarm\", \"productName\": \"云监控\", \"productNameEn\": \"CloudMonitor\", \"categorySort\": \"10\", \"productSort\": \"120\", \"deployment\": true, \"api List\": [ { \"extVersion\": \"2017-03-01\", \"content\": [ { content\": \"其他\", \"zhContent\": \"\", \"isTerminalNode\": false, \"apiCode\": \"\", \"namespace\": \"\", \"extVersion\": \"\", \"subNode\": { \"content\": \"AccessKeyGenerate\", \"zhContent\": \"生成专有云API访问密钥\", \"isTerminalNode\": true, \"apiCode\": \"AccessKeyGenerate\", \"namespace\": \"Cms\", \"extVersion\": \"2017-03-01\", \"subNode\": null } ] } ] } ] }", "requestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### GetApiDocs

获取开发者门户对应产品和版本下的OpenApi详情。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Product | String | Query | 是 | ecs | 云产品Code。 |
| ExtVersion | String | Query | 是 | 2014-05-26 | 云产品版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| data | Struct | { "apis": [ { "httpMethod": [ "POST" ], "httpProtocol": [ "HTTP", "HTTPS" ], "id": 5098, "invokeGatewayType": [ "POP" ], "metaType": "POPXML", "name": _ "ActivateUser", "product": "ascm", "status": "ENABLED", "version": "2019-05-10", "zhName": "激活用户账号" } ] } | 返回数据。 |

**示例**

| JSON | 格式 |
|---|---|
| { "data":"{ \"apis\": [ { \"httpMethod\": [ \"POST\" ], \"httpProtocol\": [ \"HTTP\", \"HTTPS\" ], \"id\": 5098, \"invokeGatewayType\": [ \"POP\" \"metaType\": \"POP_XML\", \"name\": \"ActivateUser\", \"product\": \"ascm\", \"status\": \"ENABLED\", \"version\": \"2019-05-10\", \"zhName\": \"激活用户账号\" } ]}", "requestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### GetApiOverview

获取开发者门户对应产品和版本下的OpenApi简介。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Product | String | Query | 是 | ecs | 云产品Code。 |
| ExtVersion | String | Query | 是 | 2014-05-16 | 云产品版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| requestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| data | Struct | { "content": [ { "extVersion": "", "apiCode": "", "namespace": "", "zhContent": "", "content": "组织管理", "isTerminalNode": false, "subNode": [ { "extVersion": "2019-05-10", "apiCode": "GetPrivateCloudAccountByOrgan izationId", "namespace": "ascm", "zhContent": "根据组织ID获取专有云账号信息", "content": "GetPrivateCloudAccountByOrgan izationId", "isTerminalNode": true } ] } ], "product": "apsarastackplatform", _ _ "version": "2019-05-10" } | 返回数据。 |

**示例**

请求示例

```
&Product=ecs &ExtVersion=2014-05-16
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "data":"{ \"content\": [ { \"extVersion\": \"\", \"apiCode\": \"\", \"namespace\": \"\", \"zhContent\": \"\", \"content\": \"组织管理\", \"isTerminalNode\": false, \"subNode\": [ { \"extVersion\": \"2019-05-10\", \"apiCode\": \"GetPrivateCloudAccountByOrganizationId\", \"namespace\": \"ascm\", \"zhContent\": \"根据组织ID获取专有云账号信息\", \"content\": \"GetPrivateCloudAccountByOrganizationId\", \"isTerminalNode\": true } ] } ], \"product\": \"apsara_stack_platform\", \"version\": \"2019-05-10\" }", "requestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

## 统一云管平台被集成

**背景**

面向用户侧在使用专有云过程中，需要有自运维或自运营相关的管理能力，通常会在统一云管平台之上开发或采购三方控制台进行业务能力的组装，因此在之前各个客户或三方开发商，会基于专有云的能力进行集成，为了快速的集成专有云控制台的能力，我们提供标准的集成方案。

**价值**

基于统一云管平台控制台功能，提供快速被集成能力，方便用户进行三方控制台研发。

### 操作流程

**总体流程**

| 账号认证打通 |  | 页面集成配置 【统一云管平台】 |  | 页面URL嵌入 【第三方】 |
|---|---|---|---|---|

与统一云管平台登开启集成开关页面被嵌入URL地录集成址应用信息配置完成集成外观配置产品渠道链接配置
1. 账号认证打通：通过统一云管平台提供的SSO认证能力，将需要嵌入的应用与被嵌入的专有云统一云管平台进行认证打通，从而确保用户在平台间跳转时做到免多次登录的
2. 页面集成配置：通过统一云管平台提供的页面开放配置，来修改统一云管平台页面的外观与主题色、语言等内容，来适配需要嵌入的三方管理控制台，从而做到页面体验一
3. 页面URL嵌入：完成页面开放配置后，您可以从开放页面列表，获取到各个页面URL地址，您只需要将对应的URL地址通过Iframe方式嵌入到需要嵌入的管理平台中，即可

#### 7.1.1. 账号认证打通

**所需功能**

集成方若希望用户直接使用集成方账号登录统一云管平台，则需实现以下功能： 组织用户同步：需要按照集成方多级账号体系，在统一云管平台创建对应层级的组织和用户。 单点登录：使用集成方账号登录统一云管平台，需要维护集成方账号到统一云管平台用户的映射；需要支持身份提供商功能，响应统一云管平台侧单点登录请求，或主动发起单点登录，来登录集成方账号映射到的统一云管平台用户。

**实现方式**

**方案一：现场购买IDaaS**

如现场购买IDaaS，集成方仅需通过IDaaS侧标准方案把现场账号系统同步到IDaaS，无需集成方额外开发。

**方案二：现场无IDaaS**

如无IDaaS，集成方需自行开发来实现组织用户同步，以及单点登录（SSO）能力。
1. 组织用户同步
集成方工作： 需要自行管理统一云管平台上组织用户生命周期。统一云管平台提供接口支持。 统一云管平台支持： 用户和组织的增删改查OpenAPI。接口文档可参考对应版本《统一云管平台开发指南》的企业中心章节。
2. 单点登录
集成方工作： 需要自行维护集成方组织用户到统一云管平台组织用户的映射关系。 需要提供IdP功能，与统一云管平台侧SP进行单点登录交互。 统一云管平台支持： 统一云管平台侧作为SP，支持SAML 2.0/OAuth 2.0单点登录协议。文档可参考《统一云管平台用户指南》的“第三方认证”章节。 在统一云管平台获在企业IdP获取在企业IdP中配置取SP元数据 SAML元数据统一云管平台为可信SP并配置SAML 断言在统一云管平台侧配置企业IdP为可

**免密登录成功后回跳统一云管平台集成页面地址**

```xml
<!DOCTYPE html> <html>
    <head>
        <meta charset="utf-8" />
    </head>
<body >
    <form action="https://one.console.***.com/ascm/spLogin" method="post">
       <div> SAMLResponse:<textarea name="SAMLResponse">sp</textarea></div>
       <div>RelayState:<textarea name="RelayState">统一云管平台嵌入页面</textarea></div><div><input type="submit" value="Continue" /></div>
    </form>
</body> </html>
```

RelayState是你免密登录成功后回跳的统一云管平台地址，即你嵌入的统一云管平台地址。

#### 7.1.2. 页面集成配置

**配置页面入口**

设置统一云管平台页面可被集成，菜单入口在**产品** > **开发工具** > **开发者门户** > **页面集成**下的**页面开放配置**。

**重要**

当前只有运营管理员和平台管理员有权限。 页面集成页面开放设置

**页面集成总开关**

页面集成的开关打开后，统一云管平台才能支持被集成，即可iframe嵌入。平台会根据该开关状态进行业务逻辑判断。

**左侧导航栏**

隐藏左侧导航仅在被集成场景可用，可以通过开关灵活设置左侧导航栏的隐藏或者显示，同时集成开关打开才能展示隐藏左侧导航信息开关按钮。

**开关设置**

**效果图**

隐藏左侧导航开启后，效果图如下所示：

**页面样式配置**

页面样式调整后，会同时适用于直接打开统一云管平台场景和集成场景，即样式在集成和非集成场景下是共享配置。 平台语言：支持**简体中文**、**繁體中文**和**English**，可设置平台默认语言。 外观和主体：外观可选择**浅色模式**或**深色模式**，主题色可按推荐主题色直接选择或自定义色板。 页面水印：设置水印开关是否开启，开启后可自定义水印内容。

**资源链接自定义能力**

比如将云服务器ECS的“创建实例”按钮的URL设置为自定义链接，则单击该按钮就会跳转到配置的渠道链接值上。

**配置入口**

#### 7.1.3. 页面URL嵌入

**页面组成**

当前统一云管平台页面组成分为上面的吊顶、左侧的左导航、右侧的页面主体【展示业务】及右下角的悬浮球。

**页面集成示例**

ISV嵌入统一云管平台代码如下：

```xml
<iframe src="https://one.console.inter.***.com/ecs/console/instance?organizationId=1&regionId=cn-***-d01" scrolling="no" frameborder="0" style="width: 100%; height:500px;">
  </iframe>
```

使用标签<iframe src="需要被集成页面的URL地址"></iframe>

**吊顶隐藏**

对于被集成场景来说，第三方通常都会使用自己的吊顶页面，所以在集成场景下我们会自动隐藏吊顶。 在集成场景中吊顶是隐藏的，隐藏效果如下： 同时吊顶提供的能力如切换组织、切换Region、切换资源集等，可通过以下两步实现：
1. 先通过接口获取参数列表。
2. 在集成链接URL中添加对应参数来设置。

**切换组织**

1. 获取组织树，调用GetOrganizationList获取指定组织的下级组织列表。
2. 集成链接需要加上参数organizationId。例如：https://one.console.***.com/ecs/console/home?organizationId=3

**切换资源集**

1. 获取资源集列表，调用ListResourceGroupByOrgId获取组织下的资源集列表。
2. 集成链接需要加上参数resourceGroupId。例如：https://one.console.***.com/ecs/console/home?&resourceGroupId=58

**Region切换**

可通过集成链接需要加上参数regionId参数，完成切换region的操作。例如：https://one.console.***.com/ecs/console/home?regionId=cn-***-d01

**多云切换**

1. 获取多云列表，调用ListAvailablePlatforms获取当前用户有权限查看的云平台列表。
2. 可以通过在集成链接拼接AscmPlatformCode 与aliyun_mcm_cloud_type这两个参数来变更云平台Code和云平台类型。例如：
https://one.console.***.com/ess/console/dashboard?organizationId=3&regionId=cn-***d01&AscmPlatformCode=default&aliyun_mcm_cloud_type=Apsara 参数AscmPlatformCode 与aliyun_mcm_cloud_type： AscmPlatformCode：云平台Code。 主云：default。 从云（公共云与专有云格式一致）：pl-xxxxxx。 aliyun_mcm_cloud_type：云平台类型，专有云或公共云。 专有云：Apsara。 公共云：ALIYUN。

**帮助文档**

在被集成的场景，页面中自动跳转“了解更多”的功能会自动隐藏，ISV需要自己编写帮助手册以供用户使用。

**Iframe区域内跳转链接新开页面**

默认情况下，在iframe中的所有跳转链接都只在iframe的区域进行刷新，并不会新开一个tab，如果你的自定义链接需要新开tab，则需要将自定义配置的链接加上 target=_blank参数。 例如将配置的链接变更为：https://one.console.***.com/ascm/buy?product=vpc&target=_blank

**监听Iframe内URL链接变化**

在iframe集成统一云管平台时，当我们内部的链接发生变化时，我们会发送postMessage消息出来，ISV可根据监听此消息，进行相应的业务处理，比如说高亮左侧导航的某个菜单。 postMessage格式如下： `//biz-nav-console:pathname-change` 为统一云管平台广播的`type`

```
window.addEventListener('message', function (event) {
  if (event.data.type === 'biz-nav-console:pathname-change') {
    console.log('收到的消息:', event.data);
  }
});
```

`//event.data` 的定义

```
interface IEventData {
  type: string;
  pathname: string; // location.pathname
  search: string;   // location.search
}
```

**业务页面集成**

业务页面集成的时候，集成的链接一定要带上必填参数outerAscmEmbed=true。

**获取目标页面链接**

进入统一云管平台，打开你想嵌入的页面（如云服务器ECS实例列表），复制浏览器地址。 例如：https://one.console.***.com/ecs/console/instance

**添加嵌入参数**

集成的链接一定要带上必填参数outerAscmEmbed=true。 例如：https://one.console.***.com/ecs/console/instance?outerAscmEmbed=true

**在ISV系统中嵌入Iframe**

```xml
<div class="cloud-console-wrapper">
```

`<h2>`我的云服务器`</h2>`

```xml
  <iframe
    src="https://one.console.***.com/ecs/console/instance?outerAscmEmbed=true"
    width="100%"
    height="800"
    frameborder="0"
    sandbox="allow-same-origin allow-scripts allow-forms"
    loading="lazy">
  </iframe>
</div>
```

**混合云产品资源集成**

**链接参数**

公有云产品集成的链接需要增加AscmPlatformCode 与aliyun_mcm_cloud_type两个参数来标记产品，即集成的URL上增加这两个参数。 AscmPlatformCode：云平台 Code。从云（公共云与专有云格式一致）："pl-xxxxxx" aliyun_mcm_cloud_type：云平台类型。公共云：ALIYUN。

**自定义操作链接**

在**页面集成** > **页面开放配置** > **嵌入页面列表配置**中配置，找到“阿里云公共云”类型，查看支持自定义操作链接的产品及操作链接。

**管控**

单击产品linkID（detail）**操作**列的**编辑**，在**修改链接**对话框中填写对应的目标地址。如果需要新打开链接则增加参数target=_blank，如果需要增加示例ID，则需要填写的 URL中填写占位符{instanceId}，可参考原始链接的占位符格式。

**创建**

单击产品linkID（create）**操作**列的**编辑**，在**修改链接**对话框中填写对应的目标地址。如果需要新打开链接则增加参数target=_blank，如果需要增加示例ID，则需要填写的 URL中填写占位符{instanceId}，可参考原始链接的占位符格式。 效果如下： 单击操作按钮，即可访问自定义链接。

**产商品页面集成**

ISV会使用我们的产商品能力纳管第三方云平台的资源。通过产商品能力搭建一个产品资源的生命周期相关操作。具体如何构建接入一个产品，可查看产商品相关能力，可在“帮助文档”查看。 产商品的使用可参见对应版本《统一云管平台用户指南》中的“产品管理”文档： 接口对接可参见对应版本《统一云管平台用户指南》中“产品管理”下的“实例管理SPI对接”文档： 参考代码可参见对应版本《统一云管平台用户指南》中“产品管理”下的“三方产品管理对接”文档：

**列表页**

通过产商品能力后，我们会得到一个该产品的列表页面。例如：https://one.console.***.com/custom/console/list?productCode=custom-test URL参数详解：productCode是产品代码，用于确定访问的具体第三方产品控制台。

**自定义跳转链接**

目前只有详情和自定义操作可以配置跳转链接。如果要新打开tab，则需要配置的链接加上参数target=_blank。

**详情**

效果如下：

**自定义操作**

列表展示效果如下： 单击定义的操作按钮，即可访问自定义链接。

**安全类产品集成**

安全控制台由于是跳转类控制台，所以有一些特殊的地方：
1. 控制台的域名是独立的域名，可从菜单获取。
2. 安全类产品需要切换到具体的角色才可以。

**隐藏菜单左导**

需要集成链接中增加hideSidebar参数，hideSidebar=true。

**安全产品集成页面**

安全产品根据URL参数p和identifier来定位具体的产品。 例如集成页面链接：https://yundun.console.***.com/?p=soar&identifier=soar&outerAscmEmbed=true，表示集成产品为《安全编排自动化响应SOAR》。 具体其他产品可参考菜单的配置。

**URL公共参数**

使用公共参数设置控制台页面。

| 参数名 | 类型 | 是否必选 | 说明 | 示例 |
|---|---|---|---|---|
| outerAscmEmbed | boolean | 是 | 标识页面嵌入。 | outerAscmEmbed=true |
| regionId | String | 否 | 操作的region，不填默认为当前域名所属的 region。 | regionId=cn-***-d01 |
| organizationId | int | 否 | 统一云管平台的组织ID，不填为登录用户所属组织。 | organizationId=3 |
| resourceGroupId | int | 否 | 统一云管平台的资源集ID，不填默认为空，取默认资源集。 | resourceGroupId=29 |
| AscmPlatformCode | String | 否 | 云平台Code，不填默认default。 主云：default。 从云（公共云与专有云格式一致）：pl- xxxxxx。 | AscmPlatformCode=default |
| aliyunmcmcloudtype _ _ _ | String | 否 | 云平台类型，不填默认Apsara。 专有云：Apsara 公共云：ALIYUN | aliyunmcmcloudtype=Apsara _ _ _ |
| productCode | String | 否 | 产商品特有，是产品代码，用于确定访问的具体第三方产品控制台。 | productCode=custom-test |

**登录态校验**

在进行页面嵌入的时候，ISV的页面可以通过跨域调用/user/checkLogin.json的形式来判断当前统一云管平台登录态是否失效。

**登录态有效**

请求方式：GET请求 URL域名：统一云管平台的域名 URL path ：/user/checkLogin.json 正确返回格式：

```json
{
    "code": "200",
    "data": true,
    "cost": 18,
    "apiCost": 0,
    "eagleEyeTraceId": "0adf085317689999387036897e0***",
    "ascmCode": false,
    "successResponse": true
}
```

判断登录有效的条件："successResponse"返回true ，并且"data"返回true。 参考代码

```
function checkLoginStatus() {
  fetch('https://one.console.***.com/user/checkLogin.json', {
    method: 'GET',
    credentials: 'include'  // 确保携带 cookie
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('HTTP ' + response.status);
      }
      return response.json();
    })
      if (data.data === true) {
```

`//`判断登录有效处理，按照自己业务进行处理。

```
      } else {
```

`alert('`登录已失效，请重新登录！'); //需要进行业务登录相关处理 `//` 可选：跳转到登录页

```
        // window.location.href = 'https://isv.com/login';
      }
    })
    .catch(err => {
```

`//` 注意：网络错误、跨域、`500`等都会走到这里

```
    });
}
```

**登录页面监听**

当访问统一云管平台登录页时，前端会发送以下消息，ISV可监听以下消息跳转回ISV登录页或者其他操作。 `//` 登录页是内嵌状态

```
window.addEventListener('message', function (event) {
  if (event.data.type === 'one-console-login:embedded') {
    console.log('收到的消息:', event.data);
  }
});
```

返回消息如下:

```json
{
    "pathname": "/ascm/login",
    "search": "?oauth_callback=https%3A%2F%2Fone.console.***.com%2Fecs%2Fconsole%2Fimage%2Fecs%2Fself%3ForganizationId%3D3%26regionId%3Dcn-
***-
d01%26ascmState%3DeyJvcmdhbml6YXRpb25JZCI6IjMiLCJyZWdpb25JZCI6ImNuLXd1bGFuLWVudjIyMy1kMDE***%26AscmPlatformCode%3Ddefault%26aliyun_mcm_cloud_type psara",
    "hash": "",
    "type": "one-console-login:embedded"
}
```

**角色切换**

GET请求调用oneConsole地址 path：/data/redirect.json? 参数如下：

| product | identityService | 固定 |
|---|---|---|
| action | switchRole | 固定 |
| version | 2019-05-10 | 固定 |
| params | {"arId":"ar- 9999999***","targetUrl":"https://one.console .***.com"} | json格式，arid为角色中的arid字段，targetUrl为切换角色成功后回跳的地址。 |

arid可在统一云管平台中的**企业** > **权限管理** > **角色授权**下获取： 调用参考示例：

```
https://one.console.***.com/data/redirect.json?product=identityService&action=switchRole&version=2019-05-10&params=%7B%22arId%22%3A%22ar- 9999999***%22%2C%22targetUrl%22%3A%22https%3A%2F%2Fone.console.***.com%22%7D
```

其中params参数如下：

```json
{"arId":"ar-9999999***","targetUrl":"https://one.console.***.com"}
```

### API集成

API集成目前是通过POP SDK集成，通过POP SDK调用OpenAPI开放接口。调用OpenAPI接口时，需使用代表用户身份的AK和SK进行调用。

**用户AK和SK获取**

1. 登录统一云管平台。
2. 在页面右上角，单击当前登录用户的头像。
3. 单击**个人信息**。
4. 在**AccessKey**区域，查看个人的AccessKey ID和AccessKey Secret信息。

**用户AK和SK维护的最佳实践**

**仅维护并使用运营管理员的AK和SK**

使用该方式，针对用户的数据需要ISV进行过滤展示。运营管理员拉取到的是全局视角数据，如需过滤出某用户+角色可见的数据，需要ISV侧根据接口和用户+角色进行过滤组装。 运营侧流程审批相关接口无法使用运营管理员身份进行调用。 有其他少量接口不支持运营管理员调用。

**维护并使用运营管理员和全量管理用户的AK和SK**

ISV初始化并维护用户角色、组织资源集生命周期，并存储全量用户AK和SK。此操作需运营管理员身份执行。 创建用户成功后，后续使用用户的AK、SK进行相关接口调用。 使用该方式，需要维护好用户的AK和SK的生命周期，保持和统一云管平台同步。

**参考手册**

API接口的使用可参考对应版本的《统一云管平台开发指南》，手册路径“帮助” > "统一云管平台" > "API文档"。 帮助 API文档

### 前端样式规范

本文对统一云管平台前端设计规范进行相关介绍。 统一云管平台前端设计遵循统一规范，以确保用户体验的一致性、开发协作的高效性、代码的可维护性以及多端适配的可靠性。具体规范可参见云管设计规范.zip。
