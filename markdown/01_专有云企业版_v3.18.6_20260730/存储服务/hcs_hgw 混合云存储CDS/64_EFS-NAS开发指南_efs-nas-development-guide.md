---
title: "混合云存储CDS EFS-NAS开发指南"
product_version: "v3.18.6-SP2607"
doc_version: "20260729"
pdf_pages: 91
source_pdf: "64_EFS-NAS开发指南_efs-nas-development-guide.pdf"
source_url: "https://apsara-doc.oss-cn-hangzhou.aliyuncs.com/apsara-pdf/enterprise/v_3_18_6_20260730/hcs_hgw/zh/efs-nas-development-guide.pdf"
converter: line-classifier (PyMuPDF)
---

# 混合云存储CDS EFS-NAS开发指南

阿里云弹性文件存储 EFS-NAS 开发

## 版本变更记录

本文介绍EFS-NAS产品各版本的特性变更记录，仅涵盖API接口以及调用示例的变更。

**v3.18.6 sp-2607**

相对于v3.18.6 sp-2605版本的特性变更说明请参见下表。

| 特性 | 变更说明 |
|---|---|
| 文件系统 | 支持批量冻结/解冻文件系统操作。 |
| 配额管理 | 新增配额管理相关操作。例如创建配额、获取配额信息等。 |
| 多集群 | 新增查询集群接口。 |

**v3.18.6 sp-2605**

相对于v3.18.6 sp-2512版本的特性变更说明请参见下表。

| 特性 | 变更说明 |
|---|---|
| 定时快照管理 | 新增定时快照和快照策略相关操作，例如创建定时快照策略、创建定时快照任务、获取定时快照任务关联的快照策略等。 |
| WORM策略 | 新增WORM相关操作，例如创建WORM策略、获取WORM配置信息等。 |

**v3.18.6 sp-2512**

相对于v3.18.6 sp-2510版本的特性变更说明请参见下表。

| 特性 | 变更说明 |
|---|---|
| 快照 | 新增快照相关操作，例如创建快照、获取快照信息等。 |
| 回收站 | 新增回收站相关操作，例如开启回收站、列举回收站中的文件、恢复误删文件等。 |

**v3.18.6 sp-2510**

首个版本发布。此版本的特性说明请参见下表。

| 特性 | 变更说明 |
|---|---|
| 文件系统 | 新增文件系统相关操作，例如创建文件系统、获取文件系统信息等。 |
| 用户与用户组 | 新增用户和用户组相关操作，例如创建文件系统用户、获取文件系统用户信息、创建文件系统用户组、获取文件系统用户组信息等。 |
| SMB共享与ACL | 新增SMB共享和SMB ACL相关操作，例如创建SMB共享、获取SMB共享连接情况、批量创建SMB访问控制列表、获取SMB访问控制列表信息等。 |
| NFS共享与ACL | 新增NFS共享和NFS ACL相关操作，例如创建NFS共享、获取NFS共享连接情况、批量创建NFS访问控制列表、获取NFS访问控制列表信息等。 |
| 地域 | 新增地域操作，用于查询地域下支持指定文件系统类型的可用区信息。 |

阿里云弹性文件存储 EFS-NAS 开发

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
阿里云弹性文件存储 EFS-NAS 开发
3. 在下拉列表中，选择对应的专有云版本。
4. 在左侧导航栏中，选择目标产品名称。
5. 在单击目标文档区域的**查看详情**或**下载****PDF**。

### API调用流程说明

阿里云专有云支持通过POP网关调用专有云API，为了使您拥有与公有云更一致的体验，自企业版V3.16.0开始，专有云API默认使用POP网关方式调用。本文介绍通过POP网关调用专有云API的流程。

**流程图**

**调用步骤**

1. 从API参考文档中获取API信息。
2. 获取AccessKey或STS AccessKey。
阿里云弹性文件存储 EFS-NAS 开发

**说明**

推荐使用个人AccessKey或STS AccessKey调用Apsara Uni-manager运营控制台及云产品接口。
3. 获取公共Header参数。
RegionID：地域ID。 组织ID：需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的GetOrganizationList章节。 资源集ID：需要通过API进行获取，获取方式请参见Apsara Uni-manager运营控制台开发指南中的ListResourceGroup章节。

**说明**

调用API时，请在Header参数中增加组织ID `<x-acs-organizationid>` 和资源集ID `<x-acs-resourcegroupid>`，指定资源所属的组织和资源集，实现实例资源的隔离查询。 不指定组织ID `<x-acs-organizationid>` ，则默认获取当前用户所属的组织。 不指定资源集ID `<x-acs-resourcegroupid>` ，则默认为空，如果指定资源集需要同时指定组织ID。
4. 通过自行拼接、飞天基础运维平台搜索的方式获取文件存储的Endpoint。
5. 获取阿里云官网的SDK核心库。
要使用EFS-NAS功能，直接安装阿里云官网的SDK核心库即可。
6. 调用云产品API。
阿里云弹性文件存储 EFS-NAS 开发

## 准备工作

### 获取文件存储的Endpoint

通过POP网关调用专有云API时需要使用云产品业务域的Endpoint。文件存储EFS-NAS的Endpoint可依照配置格式在飞天基础运维平台中获得对应变量值来自行拼装或在飞天基础运维平台中搜索获取。

**方法一：自行拼装Endpoint**

您可以根据文件存储Endpoint的配置格式，获取对应变量值来自行拼装Endpoint。

| 文件存储Endpoint的配置格式为 | efs-nas.${global:region}.${global:internet-domain} | 。 |
|---|---|---|
| 说明 ${global:internet-domain} 和 ${global:region} 为变量，请替换为您获取到的实际值。最终Endpoint中， ${global:} 不保留。 |  |  |

获取变量值的具体步骤如下：
1. 登录Apsara-Uni manager运维控制台。
2. 在顶部菜单栏，选择**平台运维** > **飞天基础运维平台** > **资源管理**，默认进入**产品集群运维**页面。
3. 在**产品集群运维**页面的**产品** | **集群**文本框中输入efs-nas，找到EfsNasControllerCluster-A-xxx集群，单击操作列的**集群详情**。
4. 在**集群详情**页面，选择**终态配置**页签。
5. 在左侧文件列表中，单击**kv.conf**，单击右侧文件内容，按Ctrl+F键分别搜索 `region` 和 `internet-domain` 。
获取到的 `region` 值将替换 ${global:region} ， `internet-domain` 值将替换 ${global:internet-domain} 。

**方法二：通过飞天基础运维平台获取**

1. 在飞天基础运维平台**产品集群运维**页面的**产品** | **集群**文本框中输入 `efs-nas` ，找到EfsNasControllerCluster-A-xxx集群，单击操作列的**集群详情**。
2. 在服务列表页面搜索 `efs-nas-mgr` 服务，单击下方列表中操作列的**详情**。
3. 在服务详情页面单击**EfsNasMgr#**组件，在组件信息中选择**资源列表**页签。
4. 搜索名为 `EFS-NAS` 的资源，单击下方**资源申请参数**列中的信息，查看**domain**值，即EFS -NAS的Endpoint。

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
| x-acs-instanceid | 实际操作的实例资源的实例ID。例如，文件系统的ID可以从文件系统列表中查询到。 |

1. 登录Apsara Uni-manager运营控制台。
2. 在系统界面右上角，单击当前登录用户头像，单击**个人信息**。
阿里云弹性文件存储 EFS-NAS 开发
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
i. 登录Apsara Uni-manager运维控制台。 ii. 在顶部菜单栏，选择平台运维**平台运维** > **飞天基础运维平台** > **资源管理**。 iii. 在飞天基础运维平台左侧导航栏中，单击。 iv. 在**产品集群运维**页面，设置**产品** | **集群**为**ascm-A**。 v. 单击集群**操作**列的**集群详情**。 vi. 在集群详情页面，单击**终态配置**页签。 vii. 在终态配置页面左侧文件列表中，单击**kv.conf**，单击右侧区域的**显示内容**。按Ctrl+F键搜索 `internet-domain` 的对应值。

| internet-domain | 的值替换 | ${global:internet-domain} |
|---|---|---|

**说明**

最终STS Endpoint中，${global:}不保留。
3. 通过调用STS的AssumeRole接口来获取三元组信息，以下为Java的STS SDK调用示例。

**说明**

以下代码示例

```
中 <yourRegionID> 、 <yourAccessKeyID> 、 <yourAccessKeySecret> 、 <yourRoleSessionName> 、 <yourRoleArn> 、 <sts.aliyuns.com> 均为可
```

变参数，需要替换为其实际值。尖括号（<>）在最终代码中不保留。 阿里云弹性文件存储 EFS-NAS 开发

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

4. 获取STS AccessKey三元组后，您就可以使用三元组信息调用云产品API接口。以下Java SDK示例以DescribeZones接口为例，使用STS AccessKey调用文件存储产品
接口。

|  | 说明以下代码示例中 <efs- nas.aliyuns.com> 、 <yourRegionID> 、 <yourStsAccesskeyID> 、 <yourStsAccessKeySecret> 、 <yourStsToken> 、 <yourResourceGroupID> 、 <yo 为可变参数，需要替换为其实际值。尖括号（<>）在最终代码中不保留。文件存储的Endpoint需配置为环境变量。 |  |  |
|---|---|---|---|
|  | nas.aliyuns.com> | <yo | u |

阿里云弹性文件存储 EFS-NAS 开发

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
    request.setSysMethod(com.aliyuncs.http.MethodType.POST);
```

`//`文件存储的`Endpoint`，请替换为实际值。

```
    request.setSysDomain("<efs-nas.aliyuns.com>");
    request.setSysVersion("2017-06-26");
    request.setSysAction("DescribeZones");
    request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
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
| x-acs-resourcegroupid | 实际操作的实例资源所属的资源集ID，获取方式请参见获取资源集ID。 |
| x-acs-instanceid | 实际操作的文件系统资源的ID，获取方式请参见获取文件系统ID。 |

**说明**

调用Apsara Uni-manager运营控制台的API时，可以不使用Header参数 `x-acs-organizationid` 、 `x-acs-resourcegroupid` 、 `x-acs-instanceid` 。 调用其他云产品的API时，需要在Header参数中增加组织ID `<x-acs-organizationid>` ，否则将返回调用异常，提示无权限。 调用其他云产品的API时，建议在Header参数中增加资源集ID `<x-acs-resourcegroupid>` 。指定资源所属的组织和资源集，实现实例资源的隔离查询。若不指定资源集ID `<x-acs-resourcegroupid>` ，则获取当前用户所属组织的默认资源集。

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
阿里云弹性文件存储 EFS-NAS 开发
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `GetOrganizationList` 进行在线调试，在name参数填写目标组织名称后发起调用，调用成功后查看**调用结果**中**id**的信息，即为组织ID。

**获取资源集ID**

资源集ID需要通过调用API方式获取，您可以在Apsara Uni-manager运营控制台中通过API在线调试功能快速获取资源集ID信息。
1. 管理员登录Apsara Uni-manager运营控制台。
2. 在顶部菜单栏，选择**产品** > **开发工具** > **API****与工具** > **开发者门户**。
3. 在**开发者门户**页面，选择**API****集成**> **API****调试**。
4. 单击
按钮，选择**云平台** > **统一云管平台**，**版本**选择**2019-05-10**。
5. 在文本框内输入 `ListResourceGroup` 进行在线调试，调用成功后查看**调用结果**中**id**的信息，即为资源集ID。

**获取文件系统ID**

文件系统ID可以通过Apsara Uni-manager运营控制台中的云产品资源列表进行获取。请在文件存储EFS -NAS产品控制台的文件系统列表中查看文件系统ID信息。
1. 登录Apsara Uni-manager运营控制台。
2. 在顶部的菜单栏，选择**产品** > **存储** > **文件存储****EFS-NAS**。
3. 在左侧导航栏，单击**文件系统管理**。
4. 在文件系统列表中查看**文件系统****ID/****名称**。

**公共返回参数**

在调用列表类的云产品资源实例接口时，在返回结果中默认包含以下公共返回参数。

| 名称 | 描述 |
|---|---|
| ResourceGroupName | 资源集名称。 |
| ResourceGroup | 资源集ID。 |
| DepartmentName | 组织名称。 |
| Department | 组织ID。 |

阿里云弹性文件存储 EFS-NAS 开发

## Java SDK调用示例

### 快速开始

本文介绍如何获取EFS-NAS Java SDK并开始调用。

**环境准备**

已安装1.8及以上版本的JDK。

**安装阿里云专有云Java SDK**

阿里云专有云Java SDK可以通过添加Maven依赖或下载阿里云开发工具包（SDK）的方式安装专有云Java SDK核心库。 要使用EFS-NAS功能，必须安装阿里云Java SDK核心库，SDK核心库推荐使用4.5.17及以上版本。具体操作，请参见安装Java SDK。

**使用Java SDK**

调用阿里云专有云Java SDK的主要操作步骤如下：
1. 创建并初始化DefaultAcsClient实例。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
使用EFS-NAS的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。涉及替换的可变参数如下： <efs-nas.aliyuns.com>，请替换为您实际的产品访问地址。 <readTimeout>，请根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请根据实际情况设置连接超时时间，单位为毫秒。 <http://192.168.XX:33XX>，请替换为实际的代理IP+端口。 阿里云弹性文件存储 EFS-NAS 开发

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) throws Exception {
```

`//` 初始化客户端

```
        DefaultProfile profile = DefaultProfile.getProfile(
            System.getenv("REGION_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        );
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

`//` 创建请求

```
        CommonRequest request = new CommonRequest();
```

`//` 设置请求方式。

```
        request.setSysMethod(com.aliyuncs.http.MethodType.POST);
```

`//` 文件存储的`Endpoint`地址，请根据实际替换。

```
        request.setSysDomain("<efs-nas.aliyuns.com>");
```

`//` 文件存储的接口信息参数。

```
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
```

`//` 设置接口业务参数。

```
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "10");
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-organizationid`、`x-acs-resourcegroupid`、`x-acs-instanceid`。详情 `//` 发送请求并输出结果

```java
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println("响应状态: " + response.getHttpStatus());
            System.out.println("响应数据: " + response.getData());
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

#### 4.2.1. 安装Java SDK

阿里云专有云Java SDK支持1.8及以上版本的JDK，可以通过添加Maven依赖或下载阿里云开发工具包（SDK）的方式安装专有云Java SDK。 要使用文件存储功能，只需安装阿里云Java SDK核心库，SDK核心库推荐使用4.5.17及以上版本。

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

阿里云弹性文件存储 EFS-NAS 开发

#### 4.2.2. 设置身份验证凭证

使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。

**配置访问凭证**

获取 AccessKey 或 STS 临时凭证和地域ID后，请按以下方式将其配置为环境变量。此处以AccessKey为例介绍，STS 临时凭证的配置类似。请根据所用平台类型进行配置。

**WIndows**

请按需选择CMD或者PowerShell配置环境变量。

**CMD**

1. 在CMD中运行以下命令设置环境变量。

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. 重启CMD后，运行以下命令，检查环境变量是否生效。

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. 在PowerShell中运行以下命令。

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. 运行以下命令，检查环境变量是否生效。

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

| 在命令行界面执行以下命令来将环境变量设置追加到 | ~/.bashrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc |  |  |

2. 执行以下命令使变更生效。

```
source ~/.bashrc
```

3. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. 在终端中执行以下命令，查看默认 Shell 类型。

```
echo $SHELL
```

2. 根据默认 Shell 类型进行操作。
Zsh

| 执行以下命令来将环境变量设置追加到 | ~/.zshrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc |  |  |

b. 执行以下命令使变更生效。

```
source ~/.zshrc
```

c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash

| 执行以下命令来将环境变量设置追加到 | ~/.bash_profile | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile |  |  |

阿里云弹性文件存储 EFS-NAS 开发 b. 执行以下命令使变更生效。

```
source ~/.bash_profile
```

c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**初始化Client**

目前Java SDK支持通过AccessKey或STS AccessKey进行身份验证。

```
DefaultProfile profile = DefaultProfile.getProfile(
```

`System.getenv("REGION_ID"), //` 获取环境变量中的地域`ID`。 `//` 获取环境变量中的 `AccessKey ID` 和 `AccessKey Secret`。

```
    System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
    System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
```

`//` 使用`STS AccessKey`进行身份验证时，请将账号的`SecurityToken`配置到环境变量`ALIBABA_CLOUD_STS_SECURITY_TOKEN.` `//`使用`AccessKey`进行身份验证时，`SecurityToken`置为`null`。

```
    System.getenv("ALIBABA_CLOUD_STS_SECURITY_TOKEN")
);
```

#### 4.2.3. 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

**说明**

以下代码示例中可变参数均需替换为实际的相关信息，尖括号（<>）在最终代码中不保留。 涉及替换的可变参数如下： <readTimeout>，请根据自身服务的能力，配置读取超时时间，单位为毫秒（ms）。 <connectionTimeout>，请根据自身服务的能力，配置连接超时时间，单位为毫秒（ms）。 <maxRequestsPerHost>，请根据自身服务的能力，配置每台服务器的最大请求数，数据类型为INT。 <maxRequests>，请根据自身服务的能力，配置最大请求数，数据类型为INT。 <http://192.168.XX.XX:33XX>，请替换为实际的代理IP+端口。 `//` 获取`HttpClientConfig`对象

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

#### 4.2.4. 发起调用

当您要调用某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest介绍**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在EFS-NAS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。 您需要获取 `Action` 参数，使用 `request.setSysAction("<Action>")` 的方式来指定API名称。 阿里云弹性文件存储 EFS-NAS 开发例如 `DescribeFileSystems` 接口，在发起 `CommonRequest` 请求时，需要使用 `request.setSysAction("DescribeFileSystems")` 来指定API名称。

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 `//` 创建`API`请求并设置参数。

```
CommonRequest request = new CommonRequest();
```

`//` 文件存储的接口信息参数。

```
request.setSysProduct("efs-nas"); request.setSysVersion("2017-06-26"); request.setSysAction("DescribeFileSystems"); request.setSysUriPattern("<yourCallUriPattern>");
```

`//` 文件存储的`Endpoint`地址。

```
request.setSysDomain("<efsnasEndpoint>");
```

`//` 设置请求方式。

```
request.setSysMethod(MethodType.POST);
```

`//` 设置`Headers`。 `//` 非必填，请替换为您实际的资源集`ID`。

```
request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
```

必填，请替换为您实际的组织`ID`。

```
request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");//
```

`//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

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

以上代码示例中 `<yourCallUriPattern>` 、 `<efsnasEndpoint>` 、 `<yourCallerSdkSource>` 均为可变参数，需要替换为其实际值，尖括号（<>）在最终代码中不保留。

**设置阿里云核心库SDK参数**

在使用阿里云核心库SDK发起API请求时，可以设置四种类型的参数：Path、Query、Body、Header。在调用具体API时，请根据开发文档中标注的参数位置对应设置。

| 参数类型 | 描述 | 代码示例 |
|---|---|---|
| Path | Path参数用于对请求Request中设置的UriPattern 进行变量替换。 例如：URI "/clusters/[ClusterId]" 中的 [ClusterId] 可以通过设置Path参数 "ClusterId=cluster1" 进行替换。 最终发起HTTP请求的URI则为 "/clusters/clusterId01" 。 | CommonRequest request = new CommonRequest(); request.setSysUriPattern("/clusters/[ClusterId]"); request.putPathParameter("ClusterId", "clusterId01"); |
| Query | Query参数用于对请求Request中的URL参数进行设置（一般用于GET请求）。 例如：“http://aliyun.com/api/? ClusterId=clusterId01&ClusterName=cluster Name01”。 | CommonRequest request = new CommonRequest(); request.putQueryParameter("ClusterId", "clusterId01"); request.putQueryParameter("ClusterName", "clusterName01"); |
| Body | Body参数用于对请求Request中的HTTP Content 进行设置（一般用于POST/PUT请求）。 目前支持两种格式： application/json application/x-www-form-urlencoded 说明在设置Body参数时，需要同时设置HTTP Content-Type。 | key-value形式设置Body参数，并设置HttpContentType。 CommonRequest request = new CommonRequest(); request.putBodyParameter("ClusterId", "clusterId01"); request.putBodyParameter("ClusterName", "clusterName01"); // 若Content-Type设置为application/x-www-form-urlencoded，请求到服务器的Content 数据格式为"ClusterId=clusterId01&ClusterName=clusterName01"的字符串。 request.setHttpContentType(FormatType.FORM); // 或，若Content-Type设置为application/json，请求到服务器的Content数据格式为" {\"ClusterId\":\"clusterId01\",\"ClusterName\":\"clusterName01\"}"的JSON串。 request.setHttpContentType(FormatType.JSON); 自行构造HTTP Content并直接设置HttpContent。 CommonRequest request = new CommonRequest(); //设置application/json格式的HTTP Content。 String body = "{\"ClusterId\": \"clusterId01\", \"ClusterName\": \"clusterName01\"}"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.JSON); //设置application/x-www-form-urlencoded格式的HTTP Content。 String body = "ClusterId=clusterId01&ClusterName=clusterName01"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.FORM); |
| Header | Header参数用于对请求Request中的HTTP Header进行设置。 | CommonRequest request = new CommonRequest(); request.putHeadParameter("x-acs-organizationid", "3"); request.putHeadParameter("x-acs-resourcegroupid", "2"); |

阿里云弹性文件存储 EFS-NAS 开发

**发起调用并处理应答**

可参考以下代码发起请求并处理返回结果。

```
try {
```

`//` 发起请求，并获取返回。

```java
    CommonResponse response = client.getCommonResponse(request);
    System.out.println("响应状态: " + response.getHttpStatus());
    System.out.println("响应数据: " + response.getData());
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    System.out.println("ErrCode:" + e.getErrCode());
    System.out.println("ErrMsg:" + e.getErrMsg());
    System.out.println("RequestId:" + e.getRequestId());
}
```

**完整示例**

以下代码为通过EFS-NAS的 `DescribeFileSystems` 接口查询文件系统列表的调用示例。 阿里云弹性文件存储 EFS-NAS 开发

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile;
    public static void main(String[] args) throws Exception {
```

`//` 初始化客户端

```
        DefaultProfile profile = DefaultProfile.getProfile(
            System.getenv("REGION_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
        );
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

`//` 创建请求

```
        CommonRequest request = new CommonRequest();
```

`//` 设置请求方式。

```
        request.setSysMethod(com.aliyuncs.http.MethodType.POST);
```

`//` 文件存储的`Endpoint`地址，请根据实际替换。

```
        request.setSysDomain("<efs-nas.aliyuns.com>");
```

`//` 文件存储的接口信息参数。

```
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
```

`//` 设置接口业务参数。

```
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "10");
```

`//` 设置`Headers`。 `//` 设置身份标识，标识调用来源，无实际作用，可随意设置，必填项。

```
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
```

`//` 调用专有云`API`时，一般需要提供多个公共`Header`参数，包括：`x-acs-regionid`、`x-acs-organizationid`、`x-acs-resourcegroupid`、`x-acs-instanceid`。详情可参 `//` 发送请求并输出结果

```java
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println("响应状态: " + response.getHttpStatus());
            System.out.println("响应数据: " + response.getData());
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

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。涉及替换的可变参数如下： <efs-nas.aliyuns.com>，请替换为您实际的产品访问地址。 <readTimeout>，请根据实际情况设置读取超时时间，单位为毫秒。 <connectionTimeout>，请根据实际情况设置连接超时时间，单位为毫秒。 <http://192.168.XX:33XX>，请替换为实际的代理IP+端口。

#### 4.2.5. 错误处理

在使用Java SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 阿里云弹性文件存储 EFS-NAS 开发一般情况下，无需对Java SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

如需对SDK的错误进行处理，可以参考如下示例编写代码：

```
try {
    AcsResponse response = client.getAcsResponse(request);
```

`//` 处理`Response`。

```
    // ...
}catch (ServerException e){
```

`//` 此处可以添加您自己的错误处理逻辑。 `//` 例如，打印具体的错误信息。

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

阿里云弹性文件存储 EFS-NAS 开发

## Python SDK调用示例

### 快速开始

本文介绍如何获取SDK并开始调用。

**环境准备**

要使用文件存储功能，只需安装阿里云Python SDK核心库。具体命令如下： 如果您使用的是Python 2.x，执行以下命令安装阿里云SDK核心库。

```
pip install aliyun-python-sdk-core
```

如果您使用的是Python 3.x，执行以下命令安装阿里云SDK核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

**使用Python SDK**

调用Python SDK的3个主要步骤如下：
1. 创建Client实例。在创建Client实例时，您需要获取Region ID、AccessKey ID和AccessKey Secret。
2. 创建API请求并设置参数。
3. 发起请求并处理应答或异常。
使用EFS-NAS的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID、ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。涉及替换的可变参数如下： <efs-nas.aliyuns.com>，请替换为您实际的产品访问地址。 <http://192.168.XX:33XX>，请替换为实际的代理IP+端口。

```java
import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest def main():
```

# 如需使用代理，请使用以下代码：

```
    #os.environ['http_proxy'] = "<http://192.168.XX:33XX>"
```

# 将`AccessKey`和地域`ID`配置为环境变量后再进行初始化。

```
    client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                       os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
                       os.environ['REGION_ID'])
```

# 创建请求对象。

```
    request = CommonRequest()
```

`request.set_domain('<efs-nas.aliyuns.com>') # API`服务地址，当前为示例值，请替换为您实际的产品访问地址。

```
    request.set_version('2017-06-26')  # API版本号。
```

`request.set_action_name('DescribeFileSystems') # API`名称，当调用`RPC`风格`API`时，必须配置`set_action_name()`指定接口名称。

```
    request.set_method('POST')  # API请求方式。
```

`request.set_protocol_type('HTTPS') #` 请求协议`HTTPS`或`HTTP`，建议使用`HTTPS`。

```
    request.add_query_param('PageNum', '1')
    request.add_query_param('PageSize', '30')
```

# 发起请求并处理响应。

```python
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    main()
```

### 使用手册

#### 5.2.1. 安装Python SDK

本文介绍如何安装及调用EFS-NAS Python SDK。

**背景信息**

阿里云专有云Python SDK支持Python 2.6.x、2.7.x和3.x及以上环境，可通过pip安装专有云Python SDK。 要使用文件存储功能，只需安装阿里云Python SDK核心库。具体命令如下： 如果您使用的是Python 2.x，执行以下命令安装阿里云SDK核心库。

```
pip install aliyun-python-sdk-core
```

阿里云弹性文件存储 EFS-NAS 开发如果您使用的是Python 3.x，执行以下命令安装阿里云SDK核心库。

```
pip3 install aliyun-python-sdk-core-v3
```

#### 5.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。

**配置访问凭证**

获取 AccessKey和地域ID后，请根据所用平台类型选择以下方式将其配置为环境变量。

**WIndows**

请按需选择CMD或者PowerShell配置环境变量。

**CMD**

1. 在CMD中运行以下命令设置环境变量。

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. 重启CMD后，运行以下命令，检查环境变量是否生效。

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. 在PowerShell中运行以下命令。

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. 运行以下命令，检查环境变量是否生效。

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

| 在命令行界面执行以下命令来将环境变量设置追加到 | ~/.bashrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc |  |  |

2. 执行以下命令使变更生效。

```
source ~/.bashrc
```

3. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. 在终端中执行以下命令，查看默认 Shell 类型。

```
echo $SHELL
```

2. 根据默认 Shell 类型进行操作。
Zsh

| 执行以下命令来将环境变量设置追加到 | ~/.zshrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc |  |  |

b. 执行以下命令使变更生效。

```
source ~/.zshrc
```

c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash 阿里云弹性文件存储 EFS-NAS 开发

| 执行以下命令来将环境变量设置追加到 | ~/.bash_profile | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile |  |  |

b. 执行以下命令使变更生效。

```
source ~/.bash_profile
```

c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**初始化Client**

Python SDK支持通过AccessKey进行身份验证。使用AccessKey作为访问凭据时，需要在初始化Client时设置凭证。

```
from aliyunsdkcore.client import AcsClient client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                   os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
                   os.environ['REGION_ID'])
```

#### 5.2.3. 设置HTTPS请求

Python SDK支持使用HTTP和HTTPS协议发起 API 请求。 使用Python SDK时，您可以为某个请求指定使用HTTP或HTTPS协议，您也可以设置全局默认协议。

**说明**

产品的默认协议（HTTP/HTTPS）优先于设置的全局默认协议。

**添加OpenSSL依赖**

Python SDK的HTTPS协议依赖Python的OpenSSL支持。要使用阿里云SDK通过HTTPS协议发送请求，您需要在Python中添加OpenSSL 支持。Open SSL支持TLS1.2及以上版本。 运行 `python -c "import ssl"` 检查Python环境是否支持OpenSSL。运行后，如果没有出现 `ImportError: No module named ssl` 的错误信息，说明已经支持 OpenSSL。 如果没有OpenSSL，运行以下命令安装： `pip install pyopenssl # Python 2`使用此命令。

**说明**

如果本地环境为Python 3，则运行 `pip3 install pyopenssl` 命令。

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

#### 5.2.4. 发起调用

当您要调用某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest介绍**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在EFS-NAS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 阿里云弹性文件存储 EFS-NAS 开发接口信息：要调用的接口名称。

| 要获取 | Action | 参数，使 |
|---|---|---|
| DescribeFileSystems |  |  |

| request.set_action_name("<Action>") |  |  |
|---|---|---|
| 口，在发起 | CommonRequest | 请求时，需要使 |

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。

```
request = CommonRequest()
```

`request.set_domain('<efs-nas.aliyuns.com>') # API`服务地址，当前为示例值，请替换为您实际的产品访问地址

```
request.set_version('2017-06-26') # API版本号
```

`request.set_action_name('DescribeFileSystems') # API`名称，当调用`RPC`风格`API`时，必须配置`set_action_name()`指定接口名称

```
request.set_method('POST') # API请求方式
```

`request.set_protocol_type('HTTPS') #` 请求协议`HTTPS`或`HTTP`，建议使用`HTTPS`。
# 接口业务参数设置。

```
request.add_query_param('PageNum', '1') request.add_query_param('PageSize', '30')
```

**说明**

以上代码示例中 `<efs-nas.aliyuns.com>` 为可变参数，请结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**发起调用并处理应答**

可参考以下代码发起请求并处理返回结果。
# 发起请求，并获取返回。

```python
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

**完整示例**

| 以下代码为通过EFS-NAS的 | DescribeFileSystems | 接口查询文件系统列表的调用示例。 |
|---|---|---|
| import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest def main(): # 如需使用代理，请使用以下代码： #os.environ['http_proxy'] = "<http://192.168.XX:33XX>" # 将AccessKey和地域ID配置为环境变量后再进行初始化。 client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'], os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'], os.environ['REGION_ID']) # 创建请求对象 request = CommonRequest() request.set_domain('<efs-nas.aliyuns.com>') # API服务地址，当前为示例值，请替换为您实际的产品访问地址 request.set_version('2017-06-26') # API版本号 request.set_action_name('DescribeFileSystems') # API名称，当调用RPC风格API时，必须配置set_action_name()指定接口名称 request.set_method('POST') # API请求方式 request.set_protocol_type('HTTPS') # 请求协议HTTPS或HTTP，建议使用HTTPS。 request.add_query_param('PageNum', '1') request.add_query_param('PageSize', '30') # 发起请求并处理响应 response = client.do_action_with_exception(request) print(response) if __name__ == '__main__': main() |  |  |

**说明**

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID、ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中可变参数均需替换为您实际的相关信息，尖括号（<>）在最终代码中不保留。涉及替换的可变参数如下： <efs-nas.aliyuns.com>，请替换为您实际的产品访问地址。 <http://192.168.XX:33XX>，请替换为实际的代理IP+端口。

#### 5.2.5. 错误处理

在使用Python SDK时，当服务端或者SDK端出错时，SDK会返回相应的异常信息。这些异常信息中会包含具体的错误信息包括错误码（Error Code）和错误消息（Error Message）。 一般情况下，无需对Python SDK返回的错误进行处理，只需要根据服务端的错误提示处理服务端错误即可。 `ServerException` 是服务端错误信息。 `ClientException` 是SDK端错误信息。 例如，当出现如下错误时，您可以根据具体的错误信息，修改AccessKey的ID即可。 阿里云弹性文件存储 EFS-NAS 开发

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

阿里云弹性文件存储 EFS-NAS 开发

## Go SDK调用示例

### 快速开始

阿里云Go SDK让您不用复杂编程即可访问云产品。本操作介绍如何获取阿里云EFS-NAS Go SDK并开始调用。

**环境准备**

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
使用EFS-NAS的DescribeFileSystems接口获取文件系统信息的示例代码如下：

**说明**

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中<efs-nas.aliyuns.com>为可变参数，请替换为您实际的产品访问地址。尖括号（<>）在最终代码中不保留。 阿里云弹性文件存储 EFS-NAS 开发

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
```

`//` 将`AccessKey`和地域`ID`配置为环境变量后再进行初始化。

```
    credential := credentials.NewStsTokenCredential(
```

`//` 获取环境变量中的 `AccessKey ID` 和 `AccessKey Secret`。

```
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
```

`//` 使用`STS AccessKey`进行身份验证时，请将账号的`SecurityToken`配置到环境变量`ALIBABA_CLOUD_STS_SECURITY_TOKEN`。 `//`使用`AccessKey`进行身份验证时，`SecurityToken`置为`""`。

```
        "",
```

)

```
    client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), credential)
    if err != nil {
        panic(err)
    }
```

`//` 创建请求。

```
    request := requests.NewCommonRequest()
    request.Method = "POST"  // API请求方式。
```

`request.Domain = "<efs-nas.aliyuns.com>" // API`服务地址，当前为示例值，请替换为您实际的产品访问地址。

```
    request.Product = "efs-nas"  // 产品名。
    request.Version = "2017-06-26"  // API版本号。
    request.ApiName = "DescribeFileSystems"  // API名称。
```

`//` 接口业务参数配置。

```
    request.QueryParams["PageSize"] = "20"
    request.QueryParams["PageNumber"] = "1"
```

`//` 可选 `Header`（一般不需要，除非企业有组织/资源组要求）。

```
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // 建议与 client 一致
    // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填
    // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"   // 必填（如需按组织隔离）
```

`//` 发送请求。

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
```

`//` 输出响应结果。

```
    fmt.Println(response.GetHttpContentString())
}
```

### 使用手册

#### 6.2.1. 安装Go SDK

| 阿里云Go SDK支持Go 1.10.x及以上版本。在项目目录中执行 | go mod init <DIRNAME> | 命令生成go.mod文件后，执行如下命令安装Go SDK核心包。 |
|---|---|---|
| 说明 <DIRNAME> 为项目目录路径，请以实际路径为准。 |  |  |

| <DIRNAME> | 为项目目录路径，请以实际路径为准。 |
|---|---|

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

如果出现网络报错，可尝试使用以下两种方式下载。 使用官方提供的下载方式。

```
GOPROXY=https://goproxy.cn,direct go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

使用代理服务器下载。

```
go env -W GOPROXY='https://goproxy.cn,direct'
```

#### 6.2.2. 设置身份验证凭证

当使用阿里云专有云SDK访问阿里云专有云服务时，您需要提供授权的账号进行身份验证。本文介绍了如何设置身份验证凭证。

**配置访问凭证**

阿里云弹性文件存储 EFS-NAS 开发获取 AccessKey 或 STS 临时凭证和地域ID后，请按以下方式将其配置为环境变量。此处以AccessKey为例介绍，STS 临时凭证的配置类似。请根据所用平台类型进行配置。

**WIndows**

请按需选择CMD或者PowerShell配置环境变量。

**CMD**

1. 在CMD中运行以下命令设置环境变量。

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. 重启CMD后，运行以下命令，检查环境变量是否生效。

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. 在PowerShell中运行以下命令。

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. 运行以下命令，检查环境变量是否生效。

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

| 在命令行界面执行以下命令来将环境变量设置追加到 | ~/.bashrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc |  |  |

2. 执行以下命令使变更生效。

```
source ~/.bashrc
```

3. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. 在终端中执行以下命令，查看默认 Shell 类型。

```
echo $SHELL
```

2. 根据默认 Shell 类型进行操作。
Zsh

| 执行以下命令来将环境变量设置追加到 | ~/.zshrc | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc |  |  |

b. 执行以下命令使变更生效。

```
source ~/.zshrc
```

c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash

| 执行以下命令来将环境变量设置追加到 | ~/.bash_profile | 文件中。 |
|---|---|---|
| echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile |  |  |

b. 执行以下命令使变更生效。

```
source ~/.bash_profile
```

阿里云弹性文件存储 EFS-NAS 开发 c. 执行以下命令检查环境变量是否生效。

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**初始化Client**

Go SDK支持通过AccessKey或STS AccessKey进行身份验证。

```
credential := credentials.NewStsTokenCredential(
```

`//` 获取环境变量中的 `AccessKey ID` 和 `AccessKey Secret`。

```
    os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
    os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
```

`//` 使用`STS AccessKey`进行身份验证时，请将账号的`SecurityToken`配置到环境变量`ALIBABA_CLOUD_STS_SECURITY_TOKEN`。 `//`使用`AccessKey`进行身份验证时，`SecurityToken`置为`""`。

```
    os.Getenv("ALIBABA_CLOUD_STS_SECURITY_TOKEN"),
```

)

```
client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), credential) if err != nil {
    panic(err)
}
```

#### 6.2.3. 请求连接配置

本文介绍了如何配置请求连接（HttpClientConfig）。 可通过以下代码配置HttpClientConfig，具体请根据自身服务能力自行选择配置项并做相应配置。

```
client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), credential) if err != nil {
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

以上代码示例中 `<connectionTimeout>` 、 `<readTimeout>` 、 `<http://192.168.XX.XX:33XX>` 均为可变参数，请结合自身服务替换为其实际值，尖括号（<>） 在最终代码中不保留。

#### 6.2.4. 发起调用

当您要调用某个API没有提供SDK时，或者提供的SDK中的请求Request参数和返回Response值不符合需求时，可以采用泛用型的API调用方式（CommonRequest）。使用CommonRequest调用方式可实现任意OpenAPI接口的调用。

**CommonRequest介绍**

CommonRequest的特点如下： 轻量：只需Core包即可发起调用，无需下载安装各产品的SDK。 简便：无需更新SDK即可调用最新发布的API。 快速迭代。 发起一次CommonRequest请求，您需要获取以下几个参数的值。您可以在EFS-NAS的API文档中获取以下参数的值。 域名(domain)：该产品的服务地址。 API版本(version)：该API的版本号，格式为YYYY-MM-DD。 您可以在各产品的API文档的公共参数部分获取API版本。 接口信息：要调用的接口名称。

| 要获取 | Action | 参数，使 |
|---|---|---|
| DescribeFileSystems |  |  |

| request.ApiName = "<Action>" |  |  |
|---|---|---|
| 口，在发起 | CommonRequest | 请求时 |

**创建请求CommonRequest**

使用CommonRequest调用方式可实现任意Open API接口的调用。 阿里云弹性文件存储 EFS-NAS 开发

```
request := requests.NewCommonRequest() request.Method = "POST" request.Domain = "<efs-nas.aliyuns.com>" // EFS-NAS服务域名。 request.Product = "efs-nas" // 产品名。 request.Version = "2017-06-26" // 指定API版本。 request.ApiName = "DescribeFileSystems" // API名称。
```

`//` 接口业务参数配置

```
request.QueryParams["PageSize"] = "20" request.QueryParams["PageNumber"] = "1"
```

`//` 可选 `Header`（一般不需要，除非企业有组织/资源组要求）

```
request.Headers["x-acs-regionid"] = "<yourRegionID>" // 建议与 client 一致 // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填 // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // 必填（如需按组织隔离）
```

**说明**

以上代码示例中 `<efs-nas.aliyuns.com>` 为可变参数，请结合自身服务替换为其实际值，尖括号（<>）在最终代码中不保留。

**发起调用并处理返回**

可参考以下代码发起请求并处理返回结果。

```
response, err := client.ProcessCommonRequest(request) if err != nil {
    panic(err)
} fmt.Println(response.GetHttpContentString())
```

**完整示例**

以下代码为通过EFS-NAS的 `DescribeFileSystems` 接口查询文件系统列表的调用示例。 阿里云弹性文件存储 EFS-NAS 开发

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

)

```
func main() {
```

`//` 将`AccessKey`和地域`ID`配置为环境变量后再进行初始化。

```
    credential := credentials.NewStsTokenCredential(
```

`//` 获取环境变量中的 `AccessKey ID` 和 `AccessKey Secret`。

```
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
```

`//` 使用`STS AccessKey`进行身份验证时，请将账号的`SecurityToken`配置到环境变量`ALIBABA_CLOUD_STS_SECURITY_TOKEN`。 `//`使用`AccessKey`进行身份验证时，`SecurityToken`置为`""`。

```
        "",
```

)

```
    client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), credential)
    if err != nil {
        panic(err)
    }
```

`//` 创建请求。

```
    request := requests.NewCommonRequest()
    request.Method = "POST"  // API请求方式。
```

`request.Domain = "<efs-nas.aliyuns.com>" // API`服务地址，当前为示例值，请替换为您实际的产品访问地址。

```
    request.Product = "efs-nas"  // 产品名。
    request.Version = "2017-06-26"  // API版本号。
    request.ApiName = "DescribeFileSystems"  // API名称。
```

`//` 接口业务参数配置。

```
    request.QueryParams["PageSize"] = "20"
    request.QueryParams["PageNumber"] = "1"
```

`//` 可选 `Header`（一般不需要，除非企业有组织/资源组要求）。

```
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // 建议与 client 一致
    // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // 非必填
    // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"   // 必填（如需按组织隔离）
```

`//` 发送请求。

```
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    }
```

`//` 输出响应结果。

```
    fmt.Println(response.GetHttpContentString())
}
```

**说明**

REGION_ID、ALIBABA_CLOUD_ACCESS_KEY_ID和ALIBABA_CLOUD_ACCESS_KEY_SECRET表示地域ID、账号的AccessKey ID、账号的AccessKey Secret，请分别设置为环境变量。 代码示例中<efs-nas.aliyuns.com>为可变参数，请替换为您实际的产品访问地址。尖括号（<>）在最终代码中不保留。

#### 6.2.5. 错误处理

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

当SDK内部的任意调用出现error，并无法自动化处理时，SDK会返回一个ClientError，您可以通过以下代码来判断并获取ClientError中的错误信息。 阿里云弹性文件存储 EFS-NAS 开发

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

阿里云弹性文件存储 EFS-NAS 开发

## API参考

### 调用API

**7.1.1. 概述**

API接口调用是向产品的服务端地址发送HTTP GET请求。您需要按照接口描述在请求中加入相应请求参数。调用后系统会返回处理结果。请求及返回结果都使用UTF-8字符集编码。

#### 7.1.2. 请求结构

**服务地址**

**请求方法**

支持HTTP GET方法发送请求，这种方式下请求参数需要包含在请求的URL中。

**通信协议**

支持通过HTTP或HTTPS通道进行请求通信。为了获得更高的安全性，推荐您使用HTTPS通道发送请求。

**请求参数**

每个请求都需要指定要执行的操作，即Action参数（例如CreateFileSystem），以及每个操作都需要包含的公共请求参数和指定操作所特有的请求参数。

**字符编码**

请求及返回结果都使用UTF-8字符集进行编码。

#### 7.1.3. 返回结果

调用API服务后返回数据采用统一格式，返回的HTTP状态码为2xx，代表调用成功；返回4xx或5xx的HTTP状态码代表调用失败。调用成功返回的数据格式仅支持JSON。

**说明**

本文档中的返回示例为了便于用户查看，做了格式化处理，实际返回结果是没有进行换行、缩进等处理的。

**成功结果**

```json
{
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
```

`/*` 返回结果数据 `*/`

```
}
```

**错误结果**

调用接口出错后，将不会返回结果数据。调用方可根据每个接口对应的错误码来定位错误原因。当调用出错时，HTTP请求返回一个4xx或5xx的HTTP状态码。返回的消息体中是具体的错误代码及错误信息。另外还包含一个全局唯一的请求ID：RequestId和一个您本次请求访问的站点ID：HostId。

```json
{
    "RequestId": "8906582E-6722-409A-A6C4-0E7863B733A5",
    "HostId": "efs-nas.example.com",
    "Code": "InvalidOwnerId",
    "Message": "The specified OwnerId is not valid."
}
```

### RAM鉴权

当RAM用户通过OpenAPI对阿里云账号的资源进行访问时，系统会向RAM进行权限检查，以确保资源拥有者的确将相关资源的相关权限授予了调用者。

**背景信息**

默认情况下，阿里云账号或者RAM用户均能使用EFS-NAS控制台或EFS-NAS API操作自己创建的资源。在以下场景中，会涉及到操作授权问题： RAM用户刚创建时没有权限操作阿里云账号的资源时。 从其他阿里云服务访问EFS-NAS资源，或者EFS-NAS访问其他阿里云服务时。 操作具有权限控制的EFS-NAS资源前，需要资源拥有者授权目标资源和目标API行为权限。 当其他账号通过EFS-NAS API访问阿里云账号资源时，阿里云EFS-NAS首先向RAM发起权限检查，以确保资源拥有者已经将相关权限授予调用者。不同的EFS-NAS API会根据涉及的资源以及API语义确定需要检查哪些资源的权限。

**规则详情**

每个不同的EFS-NAS API会根据涉及到的资源以及API的语义，确定需要检查的资源的权限。

### 公共参数

公共参数分为公共请求参数、公共Header参数和公共返回参数。

**公共请求参数**

公共请求参数是指每个接口都需要使用到的请求参数。

| 名称 | 类型 | 是否必须 | 描述 |
|---|---|---|---|

阿里云弹性文件存储 EFS-NAS 开发

| Format | String | 否 | 返回值的类型，仅支持JSON。 |
|---|---|---|---|
| Version | String | 是 | API版本号，以日期形式YYYY-MM-DD输入。取值为2017-06-26。 |
| AccessKeyId | String | 是 | 访问服务使用的密钥ID。 |
| AccessKeySecret | String | 是 | 访问服务使用的密钥值。 |
| RegionId | String | 是 | 访问服务所使用的地域ID。 |
| Product | String | 是 | 接口对应的产品名称，产品名称取值为efs-nas。 |

| 名称 | 描述 |
|---|---|
| x-acs-regionid | 实际操作的实例资源所属的地域ID。 |
| x-acs-organizationid | 实际操作的实例资源所属的组织ID。 |
| x-acs-resourcegroupid | 实际操作的实例资源所属的资源集ID。 |
| x-acs-instanceid | 实际操作的实例资源的实例ID。 |

**说明**

调用Apsara Uni-manager运营控制台的API时，可以不使用Header参数 `x-acs-organizationid` 、 `x-acs-resourcegroupid` 、 `x-acs-instanceid` 。 调用其他云产品的API时，需要在Header参数中增加组织ID `<x-acs-organizationid>` ，否则将返回调用异常，提示无权限。 调用其他云产品的API时，建议在Header参数中增加资源集ID `<x-acs-resourcegroupid>` 。指定资源所属的组织和资源集，实现实例资源的隔离查询。若不指定资源集ID `<x-acs-resourcegroupid>` ，则获取当前用户所属组织的默认资源集。

**公共返回参数**

API返回结果采用统一格式，通过返回HTTP状态码来表示状态。 返回2xx HTTP状态码代表调用成功。 返回4xx或5xx HTTP状态码代表调用失败。 调用成功返回的数据格式为JSON，每次接口调用，无论成功与否，系统都会返回一个唯一识别码RequestId。

### 集群

#### 7.4.1. DescribeClusters

查询集群列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsType | String | Query | 否 | standard | 文件系统类型。 |
| PageSize | Integer | Query | 否 | 100 | 分页查询时设置的每页行数。默认值为100。 默认值：100 |
| PageNum | Integer | Query | 否 | 1 | 分页查询时设置的页码。默认值为1。 默认值： 1 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TotalCount | Long | 10 | 集群总数量。 |
| PageSize | Integer | 100 | 每页行数。 |

| 阿里云弹性文件存储指南·API参考 | EFS-NAS 开发 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| PageNum | Integer | 1 | 当前页码。 |
| Clusters | Array | "Clusters": { "Cluster": [ { "Status": "RUNNING", "ZoneId": "cn-wulan-env232-na131c22001- a", "ClusterId": "EfsNasSsdCluster-A-20260716- 0dbd", "ClusterName": "EfsNasSsdCluster-A-20260716- 0dbd", "ClusterType": "AllFlash", "RegionId": "cn-wulan-env232- d01" }, { "Status": "RUNNING", "ZoneId": "cn-wulan-env232- na131c22001-a", "ClusterId": "EfsNasSsdCluster-A-20260309- 005b", "ClusterName": "EfsNasSsdCluster-A-20260309- 005b", "ClusterType": "AllFlash", "RegionId": "cn-wulan-env232- d01" } ] } | 集群信息列表。 |
| -ClusterId | String | cluster-123 | 集群ID。 |
| -ClusterName | String | test-cluster | 集群名称。 |
| -ClusterType | String | standard | 集群类型。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| -ZoneId | String | cn-hangzhou-a | 可用区ID。 |
| -Status | String | Running | 集群状态。 |
| RequestId | String | 473469C7-AA6F-4DC5-B3DB- A3DC0D****** | 请求 ID。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":10, "PageSize":100, "PageNum":1, "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0D******", "Clusters":[ { "Status":"Running", "ZoneId":"cn-hangzhou-a", "ClusterId":"cluster-123", "ClusterName":"test-cluster", "ClusterType":"standard", "RegionId":"cn-hangzhou" } ] } |  |

### 地域

#### 7.5.1. DescribeZones

查询地域下支持指定文件系统类型的可用区信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsType | String | Query | 否 | Performance | 文件系统类型。取值范围如下： Performance：性能型，全闪介质。 Capacity：容量型，混闪介质。 未指定文件系统类型时，将会返回所有文件系统类型支持的地域信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Zones | Array | [{}] | 可用区信息列表。 |
| -ZoneId | String | cn-hangzhou-** | 可用区ID。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Zones":[ { "ZoneId":"cn-hangzhou-**" } ] } |  |

### 文件系统

#### 7.6.1. CreateFileSystem

创建文件系统。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FsName | String | Query | 是 | myfs | 文件系统名称。 |
| Capacity | Long | Query | 是 | 1024 | 容量大小，单位为GiB。取值范围为 1~5242880。 |
| FsType | String | Query | 是 | Capacity | 文件系统类型。取值范围如下： Performance：性能型，全闪介质。 Capacity：容量型，混闪介质。 |
| ZoneId | String | Query | 否 | cn-hangzhou-** | 可用区ID。 |
| Description | String | Query | 否 | 测试使用 | 文件系统描述信息。 |
| NfsVersion | String | Query | 否 | v3,v4 | 使用的NFS协议版本。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

| 指南·API参考 |  |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| FsId | String | efs-nas-0***** | 文件系统ID。 |

**示例**

请求示例

```
&FsName=myfs &Capacity=1024 &FsType=Capacity
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "FsId":"efs-nas-0*****" } |  |

#### 7.6.2. DescribeFileSystems

查询文件系统列表，支持分页。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。该配置暂不生效。 |
| FsId | String | Query | 否 | efs-nas-0***** | 文件系统ID。 |
| ZoneId | String | Query | 否 | cn-hangzhou-** | 可用区ID。该配置暂不生效。 |
| Status | String | Query | 否 | RUNNING | 文件系统状态。取值包括INITIAL（初始化中）、RUNNING（运行中）、 MODIFYING（修改中）和DELETING（删除中）。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| FileSystems | Array | [{}] | 文件系统列表。 |
| -ZoneId | String | cn-hangzhou-** | 可用区ID。 |
| -RegionId | String | cn-hangzhou | 地域ID。 |
| -ClusterId | String | c****** | 集群ID。 |
| -FsId | String | efs-nas-0***** | 文件系统ID。 |
| -FsName | String | myfs | 文件系统名称。 |
| -UserId | String | 15577******8921 | 用户ID。 |
| -FsType | String | Performance | 文件系统类型。取值包含Performance（性能型，全闪）和Capacity（容量型， 混闪）。 |
| -Capacity | Long | 100 | 总容量。单位为GiB。 |

|  |  |  | 阿里云弹性文件存储 EFS-NAS 开发指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -Status | String | Running | 文件系统状态。取值包括INITIAL（初始化中）、RUNNING（运行中）、 MODIFYING（修改中）和DELETING（删除中）。 |
| -Description | String | 测试使用 | 文件系统描述信息。 |
| -CreateRequestId | String | F0A8B189-930D-5EC1-97C8- ************ | 文件系统的创建请求ID。 |
| -CreateTime | String | 2025-10-15T05:55:20Z | 文件系统的创建时间。 |
| -ModifyTime | String | 2025-10-16T09:55:41Z | 文件系统的最近一次修改时间。 |
| -UsedCapacity | Long | 1024 | 已使用容量。单位为字节。 |
| -NfsVersion | String | v3,v4 | 使用的NFS协议版本。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Long | 5 | 查询到的文件系统总数量。 |
| PageSize | Integer | 10 | 每页资源个数。 |
| PageNum | Integer | 1 | 分页页数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeFileSystems
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "FileSystems":[ { "Status":"Running", "ModifyTime":"2025-10-16T09:55:41Z", "Description":"测试使用", "ZoneId":"cn-hangzhou-**", "NfsVersion":"v3,v4", "ClusterId":"c******", "CreateTime":"2025-10-15T05:55:20Z", "FsType":"Performance", "FsId":"efs-nas-0*****", "UsedCapacity":1024, "FsName":"myfs", "Capacity":100, "CreateRequestId":"F0A8B189-930D-5EC1-97C8-************", "UserId":"15577******8921", "RegionId":"cn-hangzhou" } ], "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageSize":10, "PageNum":1 } |  |

#### 7.6.3. ModifyFileSystem

修改文件系统的容量、描述等信息。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c**** | 集群ID。 |

| 指南·API参考 |  |  |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsId | String | Query | 是 | efs-nas-0***** | 文件系统ID。 |
| Capacity | Long | Query | 否 | 100 | 文件系统容量。单位为GiB。取值范围为1～ 5242880。 修改后的文件系统容量不能小于当前容量且不能超过剩余配额。 |
| Description | String | Query | 否 | 测试使用 | 文件系统描述信息。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&FsId=efs-nas-0*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.6.4. DeleteFileSystem

删除文件系统。

**注意事项**

文件系统删除后不可恢复，请谨慎操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FsId | String | Query | 是 | efs-nas-8***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&FsId=efs-nas-8*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.6.5. BatchModifyFileSystem

批量修改文件系统状态。 接口说明阿里云弹性文件存储 EFS-NAS 开发

## 准备工作

获取文件系统的id。

**注意事项**

文件系统状态仅支持RUNNING（运行中）和FROZEN（已冻结）相互转换。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsIds | RepeatList | Query | 是 | efs-nas-97ce04 | 数据库文件系统ID。一次最多指定100个文件系统 ID。 |
| Status | String | Query | 是 | Running | 文件系统状态暂只支持RUNNING（运行中）和 FROZEN（已冻结）相互转换。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=BatchModifyFileSystem &FsIds= &Status=
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"" } |  |

### 配额

#### 7.7.1. CreateDfsQuota

创建DFS（分布式文件系统）配额，用于限制指定路径下的存储空间或文件数量。 本接口需通过AccessKey进行签名认证（authType=AK）。 请求方法：POST 必须指定文件系统ID（FileSystemId）与配额路径（Path）。 配额参数（如SizeHardQuota、FileSoftQuota等）根据业务需求选择性填写，具体生效逻辑由服务端校验。 路径（Path）需为文件系统内有效目录路径。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Body | 是 | fs-xxxxxx | 目标文件系统ID |
| Path | String | Body | 是 | /data/project | 配额生效的目录路径 |
| QuotaType | String | Body | 否 | user | 配额类型（如user/group/directory） |
| FsUserId | Long | Body | 否 | 1001 | 文件系统用户ID |
| FsUserGroupId | Long | Body | 否 | 2001 | 文件系统用户组ID |
| SizeHardQuota | Long | Body | 否 | 1073741824 | 空间硬限制（字节），超过将禁止写入 |

| 阿里云弹性文件 | 存储 EFS- | NAS 开发 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SizeSoftQuota | Long | Body | 否 | 858993459 | 空间软限制（字节），超过将触发告警 |
| FileHardQuota | Long | Body | 否 | 10000 | 文件数硬限制，超过将禁止创建新文件 |
| FileSoftQuota | Long | Body | 否 | 8000 | 文件数软限制，超过将触发告警 |
| SizeSuggestQuota | Long | Body | 否 | 536870912 | 建议空间配额（字节） |
| FileSuggestQuota | Long | Body | 否 | 5000 | 建议文件数配额 |
| SizeRatio | Float | Body | 否 | 0.8 | 空间配额比例（0~1） |
| FileRatio | Float | Body | 否 | 0.75 | 文件数配额比例（0~1） |
| SizeGraceTime | Long | Body | 否 | 604800 | 空间超限宽限时间（秒） |
| FileGraceTime | Long | Body | 否 | 604800 | 文件数超限宽限时间（秒） |
| AdId | Long | Body | 否 | 101 | AD域标识ID |
| LdapId | Long | Body | 否 | 201 | LDAP域标识ID |
| UserName | String | Body | 否 | admin | 关联用户名（用于用户级配额） |
| UserGroupName | String | Body | 否 | developers | 关联用户组名（用于组级配额） |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 12345678-1234-1234-1234- 123456789012 | 本次请求的唯一标识ID |
| Success | Boolean | true | 请求是否成功 |
| QuotaId | Long | 12345 | 成功创建的配额唯一标识 |

Success为true时，QuotaId有效，表示配额创建成功。 Success为false时，表示创建失败，具体原因需结合HTTP状态码及服务端返回的错误信息定位（错误信息结构遵循公共错误规范）。

**示例**

请求示例

```
&FileSystemId=fs-xxxxxx &Path=/data/project
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "QuotaId":12345, "RequestId":"12345678-1234-1234-1234-123456789012", "Success":true } |  |

#### 7.7.2. DescribeDfsQuotas

查询DFS文件系统配额信息列表，支持按路径、关键字等条件过滤及分页查询。 ：需使用AccessKey（AK）进行签名认证。

**认证方式**

：接口部署于外网隔离环境（isolationType=outer）。

**网络隔离**

：服务端处理超时时间为20秒（timeout=20000ms）。

**超时设置**

**调用前提**

：请确保已创建有效的DFS文件系统，并拥有对应操作权限。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Body | 是 | fs-xxxxxx | 目标DFS文件系统的唯一标识ID |
| Q | String | Body | 否 | efs-nas | 模糊查询关键字（支持配额路径、名称等字段匹配） |
| Path | String | Body | 否 | / | 配额路径（精确匹配） |
| Sort | String | Body | 否 | CreateTime:Desc | 排序规则，格式： 字段名:排序方式 （如 CreateTime:Desc） |
| PageSize | Integer | Body | 否 | 20 | 每页返回记录数，取值范围1~100，默认20 默认值：20 |
| PageNum | Integer | Body | 否 | 1 | 页码，从1开始，默认1 默认值：1 |

| 当 | TotalCount |  |  | 大于 |  | PageSize |  | 时，可通过 | PageNum |
|---|---|---|---|---|---|---|---|---|---|
| Path |  |  | 参数需以 | / |  | 开头，例如 | /project/data |  |  |
| 支持 |  | CreateTime |  |  | 、 | UpdateTime |  |  |  |

**分页逻辑**

**路径规范**

**排序字段**

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4C467B38-391A-512B-8855- 2B3B8D3C3D3D | 本次请求的唯一标识 |
| TotalCount | Integer | 100 | 满足查询条件的配额总数量 |
| PageNum | Integer | 1 | 当前返回页码 |
| PageSize | Integer | 20 | 每页配额数量 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 下一页令牌（空值表示无更多数据） |
| Quotas | Array | [] | 配额信息列表 |
| -Id | Long | 123456 | 配额唯一ID |
| -Path | String | / | 配额生效路径 |
| -Type | String | user | 配额类型（user/group/project） |
| -Status | String | active | 配额状态（active/inactive） |
| -ActionStatus | String | normal | 配额操作状态 |
| -DfsRootfsId | Long | 789012 | DFS根文件系统ID |
| -DfsRootfsName | String | rootfs-prod | DFS根文件系统名称 |
| -SizeHardQuota | Long | 10737418240 | 空间硬限制（单位：字节） |
| -SizeSoftQuota | Long | 8589934592 | 空间软限制（单位：字节） |
| -SizeSuggestQuota | Long | 5368709120 | 建议空间配额（单位：字节） |
| -FilesHardQuota | Long | 100000 | 文件数硬限制 |
| -FilesSoftQuota | Long | 80000 | 文件数软限制 |
| -FilesSuggestQuota | Long | 50000 | 建议文件数配额 |
| -SizeRatio | Float | 0.75 | 当前空间使用率 |

| 阿里云弹性文件存储指南·API参考 | EFS-NAS 开发 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -FilesRatio | Float | 0.65 | 当前文件数使用率 |
| -SizeGraceTime | Long | 604800 | 空间宽限期（单位：秒） |
| -FilesGraceTime | Long | 604800 | 文件数宽限期（单位：秒） |
| -SizeExceedTime | String | 2023-01-01T12:00:00Z | 空间超限时间（ISO8601格式） |
| -FilesExceedTime | String | 2023-01-01T12:00:00Z | 文件数超限时间（ISO8601格式） |
| -FsUserId | Long | 1001 | 文件系统用户ID |
| -FsUserGroupId | Long | 100 | 文件系统用户组ID |
| -FsUserName | String | dfsuser _ | 文件系统用户名 |
| -FsUserGroupName | String | dfsgroup _ | 文件系统用户组名 |
| -DomainUserName | String | domain\user1 | 域账号用户名 |
| -DomainUserGroupName | String | domain\group1 | 域账号用户组名 |
| -SourceType | String | local | 配额来源类型 |
| -SourceUuid | String | uuid-xxxx-xxxx | 配额来源唯一标识 |
| -Shared | Boolean | false | 是否为共享配额 |
| -Inode | Long | 12345678 | 配额对应inode号 |
| -ClusterId | Long | 999 | 所属集群ID |
| -ClusterName | String | cluster-prod | 所属集群名称 |
| -CreateTime | String | 2023-01-01T10:00:00Z | 配额创建时间（ISO8601格式） |
| -UpdateTime | String | 2023-01-02T14:30:00Z | 配额更新时间（ISO8601格式） |
| -Samples | Array | [] | 配额采样数据列表 |
| --Create | String | 2023-07-01T08:00:00Z | 采样时间点（ISO8601格式） |
| --UsedFiles | Long | 5000 | 已使用文件数 |
| --UsedKbyte | Long | 102400 | 已使用空间（单位：KB） |

| ActionStatus |  |  |
|---|---|---|
| 进入宽限期（ | SizeGraceTime | / FilesGraceTime |

**配额状态说明**

**宽限期逻辑**

： `Samples` 提供历史使用量快照，用于容量规划分析。

**采样数据**

**示例**

请求示例

```
&FileSystemId=fs-xxxxxx
```

&公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "TotalCount":100,
 "RequestId":"4C467B38-391A-512B-8855-2B3B8D3C3D3D",
 "PageNum":1,
 "PageSize":20,
 "NextToken":"",
 "Quotas":[
  {
   "FilesSuggestQuota":50000,
   "FilesHardQuota":100000,
   "FilesExceedTime":"2023-01-01T12:00:00Z",
   "SourceUuid":"uuid-xxxx-xxxx",
   "SourceType":"local",
   "DfsRootfsName":"rootfs-prod",
   "FsUserGroupId":100,
   "FsUserName":"dfs_user",
   "Shared":false,
   "ActionStatus":"normal",
   "SizeSuggestQuota":5368709120,
   "ClusterName":"cluster-prod",
   "FsUserGroupName":"dfs_group",
   "SizeHardQuota":10737418240,
   "FilesRatio":0.65,
   "FsUserId":1001,
   "Path":"/",
   "Status":"active",
   "SizeRatio":0.75,
   "ClusterId":999,
   "CreateTime":"2023-01-01T10:00:00Z",
   "Samples":[
    {
     "Create":"2023-07-01T08:00:00Z",
     "UsedFiles":5000,
     "UsedKbyte":102400
    }
```

`],`

```json
   "DfsRootfsId":789012,
   "FilesSoftQuota":80000,
   "Type":"user",
   "Inode":12345678,
   "DomainUserGroupName":"domain\\group1",
   "SizeSoftQuota":8589934592,
   "SizeGraceTime":604800,
   "SizeExceedTime":"2023-01-01T12:00:00Z",
   "UpdateTime":"2023-01-02T14:30:00Z",
   "DomainUserName":"domain\\user1",
   "Id":123456,
   "FilesGraceTime":604800
  }
```

]

```
}
```

**文档补充说明**

配额查询结果按创建时间倒序排列。若需实时监控配额使用情况，建议结合 `Samples` 字段分析历史趋势。配额管理操作（如创建、修改）请参考DFS配额管理相关API。

#### 7.7.3. DeleteDfsQuota

删除分布式文件系统（DFS）配额配置

**授权方式**

：需使用AccessKey（AK）进行签名认证。 ：支持HTTP/HTTPS，请求方法为POST。

**请求协议**

：该API为外网隔离（outer）类型，请确保在合规网络环境中调用。

**网络隔离**

：默认请求超时时间为20秒。

**超时设置**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| QuotaId | Long | Body | 是 | 1000001 | 待删除的DFS配额唯一标识ID |
| FileSystemId | String | Body | 是 | fs-12345678 | 所属文件系统ID |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 12345-67890 | 本次请求的唯一标识，用于问题追踪与排查 |

| 阿里云弹性文件存储指南·API参考 | EFS-NAS 开发 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Success | Boolean | true | 操作执行结果，true表示成功，false表示失败 |
| QuotaId | Long | 1000001 | 已成功删除的配额ID |

**示例**

请求示例

```
&QuotaId=1000001 &FileSystemId=fs-12345678
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "QuotaId":1000001, "RequestId":"12345-67890", "Success":true } |  |

#### 7.7.4. ModifyDfsQuota

修改分布式文件系统（DFS）的配额配置参数。 ：需使用AccessKey（AK）进行签名认证。

**认证方式**

：接口部署于外网隔离环境（isolationType=outer）。

**网络隔离**

**超时设置**

：服务端处理超时时间为20秒（timeout=20000ms）。 ：请确保已创建有效的DFS文件系统，并拥有对应操作权限。

**调用前提**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| QuotaId | Long | Body | 是 | 12345 | 配额规则唯一标识ID |
| FileSystemId | String | Body | 是 | fs-abcdef123456 | 目标文件系统ID |
| SizeHardQuota | Long | Body | 否 | 1073741824 | 硬性空间配额（单位：字节） |
| SizeSoftQuota | Long | Body | 否 | 805306368 | 软性空间配额（单位：字节） |
| FileHardQuota | Long | Body | 否 | 10000 | 硬性文件数量配额 |
| FileSoftQuota | Long | Body | 否 | 8000 | 软性文件数量配额 |
| SizeSuggestQuota | Long | Body | 否 | 900000000 | 建议空间配额（单位：字节） |
| FileSuggestQuota | Long | Body | 否 | 9000 | 建议文件数量配额 |
| SizeRatio | Float | Body | 否 | 0.85 | 空间配额比例（0~1） |
| FileRatio | Float | Body | 否 | 0.8 | 文件数量配额比例（0~1） |
| SizeGraceTime | Long | Body | 否 | 604800 | 空间超限宽限期（单位：秒） |
| FileGraceTime | Long | Body | 否 | 604800 | 文件数超限宽限期（单位：秒） |

1. QuotaId` 与 `FileSystemId` 为必填参数，用于定位目标配额规则。
2. 配额参数（如SizeHardQuota、FileSoftQuota等）为可选，未传入时保留原配置。
3. 比例类参数（SizeRatio/FileRatio）需在0~1范围内，宽限期单位为秒。
4. 建议配额（SuggestQuota）仅作参考提示，不影响实际硬/软限制。

**返回数据**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | 4C467B38-1A2B-3C4D-5E6F- 7890ABCDEF12 | 本次请求唯一标识 |
| Success | Boolean | true | 操作结果状态（true=成功，false=失败） |
| QuotaId | Long | 12345 | 已更新的配额规则ID |

`Success` 为false时，建议结合业务日志排查具体失败原因。 `QuotaId` 与请求参数中的配额ID一致，用于确认操作目标。

**示例**

请求示例

```
&QuotaId=12345 &FileSystemId=fs-abcdef123456
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "QuotaId":12345, "RequestId":"4C467B38-1A2B-3C4D-5E6F-7890ABCDEF12", "Success":true } |  |

**文档补充说明**

1. 修改配额前请评估业务影响，避免因配额骤降导致服务异常。
2. 软配额触发后进入宽限期，宽限期内仍可写入，超期后按硬配额限制。
3. 配额参数存在依赖关系（如软配额不可大于硬配额），参数校验由服务端执行。
4. 集群ID（ClusterId）在多集群部署场景下需显式指定，单集群环境可省略。

### 用户

#### 7.8.1. CreateFsUser

创建文件系统用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | String | Query | 是 | myuser | 文件系统用户名。 |
| Password | String | Query | 是 | ab****** | 文件系统用户密码。密码长度为8位，由大小写字母、特殊字符、数字组成。 |
| Uid | Long | Query | 是 | 10000 | 用户ID。 |
| PrimaryGroupId | Long | Query | 否 | 10000 | 主用户组ID。不填写则为空。 |
| UserGroupIds | String | Query | 否 | [10001,10002] | 附属用户组ID列表。不填写则为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| FsUserId | Long | 100000 | 文件系统用户ID。 |

**示例**

请求示例

```
&Name=myuser &Password=ab****** &Uid=10000
```

&公共请求参数阿里云弹性文件存储 EFS-NAS 开发正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "FsUserId":100000
}
```

#### 7.8.2. DescribeFsUsers

查询文件系统用户列表，支持分页和按文件系统用户ID查询。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserId | Long | Query | 否 | 100000 | 文件系统用户ID。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| FsUsers | Array | [{}] | 文件系统用户列表。 |
| -FsUserId | Long | 100000 | 文件系统用户ID。 |
| -Uid | Long | 10000 | 用户ID。 |
| -Name | String | myuser | 文件系统用户名。 |
| -PrimaryGroupId | Long | 10000 | 主用户组ID,。 |
| -SecondaryGroupIds | String | [10001,10002] | 附属用户组ID列表。 |
| -CreateTime | String | 2025-10-15T09:55:41Z | 文件系统用户的创建时间。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | 文件系统用户的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页个数。 |
| TotalCount | Integer | 5 | 文件系统用户的总数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "FsUsers":[
  {
   "Uid":10000,
   "CreateTime":"2025-10-15T09:55:41Z",
   "FsUserId":100000,
   "PrimaryGroupId":10000,
   "Name":"myuser",
   "SecondaryGroupIds":"[10001,10002]"
  }
```

]

```
}
```

#### 7.8.3. ModifyFsUser

修改文件系统用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserId | Long | Query | 是 | 100000 | 文件系统用户ID， |
| Password | String | Query | 否 | bc****** | 文件系统用户密码。密码长度为8位，由大小写字母、特殊字符、数字组成。 |
| PrimaryGroupId | Long | Query | 否 | 10000 | 主用户组ID。不填写会将用户的主用户组置为空。 |
| UserGroupIds | String | Query | 否 | [10001,10002] | 附属用户组ID列表。不填写会将用户的附属用户组置为空。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| FsUserId | Long | 100000 | 文件系统用户ID。 |
| Name | String | myuser | 用户名称。 |
| Uid | Long | 10000 | 用户ID。 |

**示例**

请求示例

```
&FsUserId=100000
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "Uid":1000000000000000, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "FsUserId":100000, "Name":"myuser" } |  |

#### 7.8.4. DeleteFsUser

删除文件系统用户。

**注意事项**

文件系统用户删除后不可恢复，请谨慎操作。

**请求头**

阿里云弹性文件存储 EFS-NAS 开发该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserId | Long | Query | 是 | 100000 | 文件系统用户ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |

**示例**

请求示例

```
&FsUserId=100000
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

### 用户组

#### 7.9.1. CreateFsUserGroup

创建文件系统用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Name | String | Query | 是 | myusergroup | 用户组名称。 |
| GroupId | Long | Query | 是 | 10000 | 用户组ID。 |
| FsUserIds | String | Query | 是 | [100000,100001] | 文件系统用户ID列表，最多100个。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| FsUserGroupId | Long | 10000 | 文件系统用户组ID。 |

**示例**

请求示例

```
&Name=myusergroup &GroupId=10000 &FsUserIds=[100000,100001]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "FsUserGroupId":10000 } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.9.2. AddFsUsersToGroup

将文件系统用户添加到指定用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserGroupId | Long | Query | 是 | 10000 | 文件系统用户组ID。 |
| FsUserIds | String | Query | 是 | [100000,100001] | 文件系统用户ID列表，最多100个。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |

**示例**

请求示例

```
&FsUserGroupId=10000 &FsUserIds=[100000,100001]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

#### 7.9.3. RemoveFsUsersFromGroup

从指定用户组中移除文件系统用户。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserGroupId | Long | Query | 是 | 10000 | 文件系统用户组ID。 |
| FsUserIds | String | Query | 是 | [100000,100001] | 文件系统用户ID列表，最多100个。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=RemoveFsUsersFromGroup &FsUserGroupId=10000 &FsUserIds=[100000,100001]
```

&公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
}
```

#### 7.9.4. DescribeFsUserGroups

查询文件系统用户组列表，支持分页和按文件系统用户组ID查询。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserGroupId | Long | Query | 否 | 10000 | 文件系统用户组ID，用于查询指定用户组详情。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| FsUserGroups | Array | [{}] | 文件系统用户组列表。 |
| -FsUserGroupId | Long | 10000 | 文件系统用户组ID。 |
| -Gid | Long | 10000 | 组ID。 |
| -Name | String | myusergroup | 用户组名称。 |
| -FsUserIds | String | [100000,100001] | 用户ID列表。 |
| -CreateTime | String | 2025-10-15T09:55:41Z | 文件系统用户组的创建时间。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | 文件系统用户组的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeFsUserGroups
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "FsUserGroups":[ { "FsUserIds":"[100000,100001]", "Gid":10000, "CreateTime":"2025-10-15T09:55:41Z", "FsUserGroupId":10000, "Name":"myusergroup" } ], "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10 } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.9.5. DeleteFsUserGroup

删除文件系统用户组。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FsUserGroupId | Long | Query | 是 | 10000 | 文件系统用户组ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | TRUE | 请求是否成功。返回值为TRUE表示成功。 |

**示例**

请求示例

```
&FsUserGroupId=10000
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

### SMB共享

#### 7.10.1. CreateSmbShare

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| ShareName | String | Query | 是 | myshare | 共享名称。 |
| MountTargetInfo | String | Query | 否 | /efs-nas-73**** | 挂载点信息。创建时无需配置。 |
| CaseSensitive | Boolean | Query | 否 | false | 文件和目录名称的匹配是否大小写敏感。 true：大小写敏感。 false（默认值）：大小写不敏感。 |
| AbeEnabled | Boolean | Query | 否 | false | 是否启用ABE（Access-Based Enumeration，基于访问权限的枚举）。默认值false表示未启用， 启用后，用户在浏览共享目录时，只能看到自己有权限访问的共享文件和目录，无法查看无权访问的项。 |
| OpportunisticLockE nabled | Boolean | Query | 否 | false | 是否启用机会锁，适用于读多写少、用户间不频繁共享同一文件的环境。默认值false表示未启用。 启用后，允许客户端在一段时间内独占性地访问共享文件，以减少对文件服务器的频繁访问和网络传输。但也可能导致某些问题，如文件并发访问冲突等，请谨慎配置和使用。 |

| 阿里云弹性文件指南·API参考 | 存储 EFS- | NAS 开发 |  |  |  |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |

| ContactIpList | String | Query | 否 | [192.168.10.1,192.168.10.2] | 联系人IP地址列表，包含多个IPv4地址，用于标识可通信的设备或服务节点。 |
|---|---|---|---|---|---|
| VSwitchId | String | Query | 否 | vsw-bp1s5fnvk4gn2tws0**** | 虚拟交换机ID。 |
| VpcId | String | Query | 否 | vpc-bp1b1xjllp3ve5yze**** | VPC ID。 |
| Acls | String | Query | 否 | [{"AccessType":"local","UserType":"user", "Permission":"RO","UserId":10000000000 00000,"userName":"JL-USER-02"}, {"AccessType":"local","UserType":"user"," Permission":"RO","UserId":100000000000 0001,"userName":"JL-USER-01"}] | 访问控制策略组列表，格式为JSON格式的数组。单个ACL包括如下配置： UserId（Long，可选）：用户ID。 GroupId（Long，可选）：用户组ID。 UserType（String,，必选）：用户类型，取值为user（用户）、user _group（用户组）、everyone（所有人）。 Permission（String，必选）：权限类型。 取值为RO（只读）、RW（读写）、 forbid _delete（读写但禁止删除）、 full _control（完全控制）、 forbid _access（禁止访问）。当用户类型为 everyone时只支持RW和RO。 AccessType（String，可选）：访问类型， 取值为local（本地访问）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| ShareId | String | 3e47da**** | 共享ID。 |

**示例**

请求示例

```json
&FileSystemId=efs-nas-c***** &ShareName=myshare &Acls=[{"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000000,"userName":"JL-USER-02"}, {"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000001,"userName":"JL-USER-01"}]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "ShareId":"3e47da****", "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.10.2. DescribeSmbConnections

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

**返回数据**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SmbConnections | Array | [{}] | SMB共享连接列表。 |
| -ShareId | String | 3e47****** | SMB共享ID。 |
| -ClientIp | String | 10.10.10.** | 客户端IP。 |
| -AccessUser | String | myusertest | 用户名。 |
| -ProtocolVersion | String | 3.0 | 协议版本。 |
| -ConnectTime | String | 1500 | 客户端与服务器建立连接的持续时间。单位为秒。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | SMB共享连接的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSmbConnections &ShareId=3e47******
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10, "SmbConnections":[ { "ShareId":"3e47******", "ProtocolVersion":"3.0", "ConnectTime":"1500", "ClientIp":"10.10.10.**", "AccessUser":"myusertest" } ] } |  |

#### 7.10.3. DescribeSmbShares

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FileSystemId | String | Query | 否 | efs-nas-0***** | 文件系统ID。 |
| ShareId | String | Query | 否 | 3e47****** | 共享ID。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

**返回数据**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SmbShares | Array | [{}] | SMB共享列表。 |
| -ShareId | String | 3e47****** | SMB共享ID。 |
| -ShareName | String | myshare | SMB共享名称。 |
| -FileSystemId | String | efs-nas-0***** | 共享所属文件系统ID。 |
| -Status | String | ACTIVE | SMB共享当前状态。取值为ACTIVE（运行中）、PENDING（初始化中或修改中） 、DELETING（删除中）。 |
| -CreateTime | String | 2025-10-16T09:55:41Z | SMB共享的创建时间。 |
| -VpcId | String | vpc-bp1gsk7h12ew7oegk**** | VPC ID。 |
| -Azone | String | cn-hangzhou-** | 可用区。 |
| -MountTargetDomain | String | 04f314****-at***.cn- hangzhou.**.***.com | 挂载点域名。 |
| -MountTargetInfo | String | /efs-nas-73**** | 挂载点信息。 |
| -VswitchId | String | vsw-bp1e7clcw529l773d**** | 虚拟交换机ID。 |
| -CaseSensitive | Boolean | false | 文件和目录名称是否大小写敏感。 |
| -AbeEnabled | Boolean | false | 是否已启用ABE。启用后，用户在浏览共享目录时，只能看到自己有权限访问的共享文件和目录，无法查看无权访问的项。 |
| - OpportunisticLockEnabled | Boolean | false | 是否已启用机会锁。启用后，允许客户端在一段时间内独占性地访问共享文件， 以减少对文件服务器的频繁访问和网络传输。但也可能导致某些问题，如文件并发访问冲突等，请谨慎配置和使用。 |
| -ContactIpList | String | [192.168.10.1,192.168.10.2] | 联系人IP地址列表，包含多个IPv4地址，用于标识可通信的设备或服务节点。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | SMB共享的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "SmbShares":[
  {
   "Status":"ACTIVE",
   "Azone":"cn-hangzhou-**",
   "CreateTime":"2025-10-16T09:55:41Z",
   "ShareName":"myshare",
   "AbeEnabled":false,
   "VswitchId":"vsw-bp1e7clcw529l773d****",
   "OpportunisticLockEnabled":false,
   "ShareId":"3e47******",
   "VpcId":"vpc-bp1gsk7h12ew7oegk****",
   "MountTargetDomain":"04f314****-at***.cn-hangzhou.**.***.com",
   "MountTargetInfo":"/efs-nas-73****",
   "ContactIpList":"[192.168.10.1,192.168.10.2]",
   "FileSystemId":"efs-nas-0*****",
   "CaseSensitive":false
  }
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
}
```

#### 7.10.4. ModifySmbShare

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |
| ShareName | String | Query | 否 | myshare | SMB共享名称。 |
| CaseSensitive | Boolean | Query | 否 | false | 文件和目录名称的匹配是否大小写敏感。 true：大小写敏感。 false（默认值）：大小写不敏感。 |
| AbeEnabled | Boolean | Query | 否 | false | 是否启用ABE（Access-Based Enumeration，基于访问权限的枚举）。默认值false表示未启用， 启用后，用户在浏览共享目录时，只能看到自己有权限访问的共享文件和目录，无法查看无权访问的项。 |
| OpportunisticLockE nabled | Boolean | Query | 否 | false | 是否启用机会锁，适用于读多写少、用户间不频繁共享同一文件的环境。默认值false表示未启用。 启用后，允许客户端在一段时间内独占性地访问共享文件，以减少对文件服务器的频繁访问和网络传输。但也可能导致某些问题，如文件并发访问冲突等，请谨慎配置和使用。 |
| ContactIpList | String | Query | 否 | [192.168.10.1,192.168.10.2] | 联系人IP地址列表，包含多个IPv4地址，用于标识可通信的设备或服务节点。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47****** &ContactIpList=[192.168.10.1,192.168.10.2]
```

&公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
}
```

#### 7.10.5. DeleteSmbShare

**注意事项**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |
| Force | Boolean | Query | 否 | false | 是否强制删除。默认值为false。 当 SMB 共享存在活跃连接或文件被打开时，默认删除操作将失败。此时可启用强制删除选项， 以忽略活动会话并移除共享配置，但可能导致客户端连接中断，请谨慎使用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47******
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### SMB ACL

#### 7.11.1. BatchCreateSmbAcl

批量创建SMB访问控制列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Acls | String | Query | 是 | [{"AccessType":"local","UserType":"user", "Permission":"RO","UserId":10000000000 00000,"userName":"JL-USER-02"}, {"AccessType":"local","UserType":"user"," Permission":"RO","UserId":100000000000 0001,"userName":"JL-USER-01"}] | 访问控制策略组列表，格式为JSON格式的数组。单个ACL包括如下配置： UserId（Long，可选）：用户ID。 GroupId（Long，可选）：用户组ID。 UserType（String,，必选）：用户类型，取值为user（用户）、user _group（用户组）、everyone（所有人）。 Permission（String，必选）：权限类型。 取值为RO（只读）、RW（读写）、 forbid _delete（读写但禁止删除）、 full _control（完全控制）、 forbid _access（禁止访问）。当用户类型为 everyone时只支持RW和RO。 AccessType（String，可选）：访问类型， 取值为local（本地访问）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```json
&ShareId=3e47****** &Acls=[{"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000000,"userName":"JL-USER-02"}, {"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000001,"userName":"JL-USER-01"}]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.11.2. DescribeSmbAcls

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| AclEntries | Array | [{}] | SMB访问控制列表信息。 |
| -AclId | Long | 1000000000 | ACL规则ID。 |
| -UserId | Long | 1000000000000000 | 文件系统用户ID。 |
| -GroupId | Long | 10000 | 文件系统用户组ID。 |
| -UserType | String | everyone | 用户类型。取值为user（用户）、user _group（用户组）、everyone（所有人）。 |

| 阿里云弹性文件存储指南·API参考 | EFS-NAS 开发 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| -UserName | String | myuser | 用户名。 |
| -UserGroupName | String | myusergroup | 用户组名称。 |
| -Permission | String | RO | 权限类型。取值为RO（只读）、RW（读写）、forbid _delete（读写但禁止删除）、full _control（完全控制）、forbid _access（禁止访问）。 当用户类型为everyone时只支持RW和RO。 |
| -AccessType | String | local | 访问类型。取值为local（本地访问）。 |
| -CreateTime | String | 2025-10-16T09:55:41Z | SMB ACL的创建时间。 |
| -ModifyTime | String | 2025-10-17T09:55:41Z | SMB ACL最近一次的修改时间。如果未修改过则与创建时间相同。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | SMB ACL的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例

```
&ShareId=3e47******
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "AclEntries":[ { "ModifyTime":"2025-10-17T09:55:41Z", "UserName":"myuser", "UserId":1000000000000000, "AclId":1000000000, "UserGroupName":"myusergroup", "CreateTime":"2025-10-16T09:55:41Z", "Permission":"RO", "UserType":"everyone", "AccessType":"local", "GroupId":10000 } ], "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10 } |  |

#### 7.11.3. BatchUpdateSmbAcl

批量更新SMB访问控制列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。 |

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Acls | String | Query | 是 | [{"AclId": 1000000000,"Permission":"RO"},{"AclId": 1000000001,"Permission":"RO"}] | 访问控制策略组列表，格式为JSON格式的数组。单个ACL包括如下配置： AclId（Long，必选）: ACL ID，请通过 DescribeSmbAcls接口获取。 Permission（String，必选）：权限类型。 取值为"RO"（只读）、"RW"（读写）、 "forbid _delete"（读写但禁止删除）、 "full _control"（完全控制）、 "forbid _access"（禁止访问）。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47****** &Acls=[{"AclId": 1000000000,"Permission":"RO"},{"AclId": 1000000001,"Permission":"RO"}]
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.11.4. BatchDeleteSmbAcl

批量删除SMB访问控制列表。

**注意事项**

删除 SMB ACL 将直接影响用户或组对共享资源的访问权限，可能导致访问中断，请确认无业务依赖后再执行删除操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 是 | 3e47****** | SMB共享ID。请通过DescribeSmbShares接口获取。 |
| AclIds | String | Query | 是 | [1000000000,1000000001] | ACL ID列表，最多100个。请通过 DescribeSmbAcls接口获取。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47****** &AclIds=[1000000000,1000000001]
```

&公共请求参数正常返回示例

### NFS共享

#### 7.12.1. CreateNfsShare

阿里云弹性文件存储 EFS-NAS 开发

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| ShareName | String | Query | 是 | mynfsshare | NFS共享名称。长度为2～128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（_）和短划线（-）。 |
| MountTargetDomai n | String | Query | 否 | 1ca404a666-x****.cn- hangzhou.*****.*****.com | 挂载点域名。废弃参数，无需配置。 |
| MountTargetInfo | String | Query | 否 | /efs-nas-73**** | 挂载点信息。废弃参数，无需配置。 |
| Networks | String | Query | 否 | - | 网络配置。废弃参数，无需配置。 |
| NfsVersion | String | Query | 否 | - | NFS版本字符串。废弃参数，无需配置。 |
| VSwitchId | String | Query | 否 | vsw-bp1s5fnvk4gn2tws0**** | 虚拟交换机ID。 |
| VpcId | String | Query | 否 | vpc-bp1b1xjllp3ve5yze**** | VPC ID。 |
| DfsNfsShareAcls | String | Query | 否 | - | NFS客户端访问控制列表。废弃参数，无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| ShareId | String | 3e47****** | 共享ID。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &ShareName=mynfsshare
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "ShareId":"3e47******", "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.12.2. DescribeNfsConnections

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

|  |  |  |  | 阿里 | 云弹性文件存储 EFS-NAS 开发指南·API参考 |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| NfsConnections | Array | [{}] | NFS共享连接列表。 |
| -ShareId | String | 3e47****** | NFS共享ID。 |
| -ClientIp | String | 10.10.10.** | 客户端IP。 |
| -NfsVersion | String | v3 | 协议版本。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | NFS共享连接的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeNfsConnections &FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "NfsConnections":[ { "ShareId":"3e47******", "NfsVersion":"v3", "ClientIp":"10.10.10.**" } ], "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10 } |  |

#### 7.12.3. DescribeNfsShares

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| FileSystemId | String | Query | 否 | efs-nas-0***** | 文件系统ID。 |
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID， |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

**返回数据**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| NfsShares | Array | [{}] | NFS共享列表。 |
| -ShareId | String | 3e47****** | NFS共享ID。 |
| -ShareName | String | mynfsshare | NFS共享名称。 |
| -FileSystemId | String | efs-nas-0***** | 共享所属文件系统ID。 |
| -Status | String | ACTIVE | NFS共享当前状态。取值为ACTIVE（运行中）、PENDING（初始化中或修改中） 、DELETING（删除中）。 |
| -CreateTime | String | 2025-10-17T09:55:41Z | NFS共享的创建时间。 |
| -VpcId | String | vpc-bp15zckdt37pq72zv**** | VPC ID。 |
| -Azone | String | cn-hangzhou-** | 可用区。 |
| -MountTargetDomain | String | 04f314****-at***.cn- hangzhou.**.***.com | 挂载点域名。 |
| -MountTargetInfo | String | /efs-nas-73**** | 挂载点信息。 |
| -VswitchId | String | vsw-bp1e7clcw529l773d**** | 虚拟交换机ID。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | NFS共享的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10, "NfsShares":[ { "Status":"ACTIVE", "Azone":"cn-hangzhou-**", "ShareId":"3e47******", "VpcId":"vpc-bp15zckdt37pq72zv****", "MountTargetDomain":"04f314****-at***.cn-hangzhou.**.***.com", "CreateTime":"2025-10-17T09:55:41Z", "MountTargetInfo":"/efs-nas-73****", "ShareName":"mynfsshare", "FileSystemId":"efs-nas-0*****", "VswitchId":"vsw-bp1e7clcw529l773d****" } ] } |  |

#### 7.12.4. ModifyNfsShare

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 是 | 3e47****** | NFS共享ID。 |
| ShareName | String | Query | 否 | mynfssharenew | NFS共享名称。长度为2～128个字符，必须以字母或中文开头，可包含数字、半角句号（.）、 下划线（_）和短划线（-）。 |
| NfsVersion | String | Query | 否 | - | NFS版本字符串。废弃参数，无需配置。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47****** &ShareName=mynfssharenew
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.12.5. DeleteNfsShare

**注意事项**

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ShareId | String | Query | 是 | 3e47****** | NFS共享ID。 |
| Force | Boolean | Query | 否 | false | 当NFS共享存在活跃连接或文件被打开时，默认删除操作将失败。此时可启用强制删除选项，以忽略活动会话并移除共享配置，但可能导致客户端连接中断，请谨慎使用。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&ShareId=3e47******
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### NFS ACL

阿里云弹性文件存储 EFS-NAS 开发

#### 7.13.1. BatchCreateNfsAcl

批量创建NFS访问控制列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID。 |
| Acls | String | Query | 是 | [{"Type":"every- client","Permission":"RO","RootSquash":tr ue,"AllSquash":false}] | NFS客户端访问控制列表。每个客户端ACL包含如下配置： ClientIp（String，必选）：客户端IP或网段。当Type为client时才需要指定此项。 Permission（String，必选）：访问权限。 取值为RO（只读）、RW（读写）。 RootSquash（Boolean，可选）：是否启用 Root压缩。默认值为true表示启用Root压缩。启用后，远程客户端的root用户将自动映射为匿名用户，从而禁止其在服务器端的超级用户权限。当客户端以 root 身份写入文件时，服务器上该文件所有者变为 nobody，而非 root。 AllSquash（Boolean，可选）：是否启用全部压缩。默认值为false表示未启用全部压缩。启用后，所有客户端用户将均映射为匿名用户，所有文件操作都以匿名用户身份执行， 无法保留原始用户信息。 Type（String，可选）：类型，取值为 every-client（所有客户端，默认值）和 client（指定客户端）。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&Acls=[{"Type":"every-client","Permission":"RO","RootSquash":true,"AllSquash":false}] &FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.13.2. DescribeNfsAcls

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID。 |
| PageNum | Integer | Query | 否 | 1 | 分页页数。默认值为1。 |
| PageSize | Integer | Query | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |

阿里云弹性文件存储 EFS-NAS 开发

|  |  |  |  |  | 指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| AclEntries | Array | [{}] | NFS访问控制列表信息。 |
| -AclId | Long | 2000000000 | ACL规则ID。 |
| -ClientIp | String | 10.10.10.** | 客户端IP。 |
| -Permission | String | RO | 访问权限。取值为RO（只读）、RW（读写）。 |
| -RootSquash | Boolean | true | 是否启用Root压缩。默认值为true表示启用Root压缩。 启用后，远程客户端的root用户将自动映射为匿名用户，从而禁止其在服务器端的超级用户权限。当客户端以 root 身份写入文件时，服务器上该文件所有者变为 nobody，而非 root。 |
| -AllSquash | Boolean | false | 是否启用全部压缩。默认值为false表示未启用全部压缩。 启用后，所有客户端用户将均映射为匿名用户，所有文件操作都以匿名用户身份执行，无法保留原始用户信息。 |
| -Type | String | client | 类型，取值为every-client（所有客户端，默认值）和client（指定客户端）。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | NFS ACL的总数。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "AclEntries":[ { "AllSquash":false, "Type":"client", "AclId":2000000000, "Permission":"RO", "RootSquash":true, "ClientIp":"10.10.10.**" } ], "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10 } |  |

#### 7.13.3. BatchUpdateNfsAcl

批量更新NFS访问控制列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID。 |
| Acls | String | Query | 是 | [{"AclId": 2000000000,"Permission":"RO"},{"AclId": 2000000001,"Permission":"RO"}] | 访问控制策略组列表，格式为JSON格式的数组。单个ACL包括如下配置： AclId（Long，必选）: ACL ID，请通过 DescribeNfsAcls接口获取。 Permission（String，必选）：权限类型。 取值为RO（只读）、RW（读写）。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&Acls=[{"AclId": 2000000000,"Permission":"RO"},{"AclId": 2000000001,"Permission":"RO"}] &FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

#### 7.13.4. BatchDeleteNfsAcl

批量删除NFS访问控制列表。

**注意事项**

删除NFS ACL将直接影响用户或组对共享资源的访问权限，可能导致访问中断，请确认无业务依赖后再执行删除操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Query | 否 | c****** | 集群ID。 |
| ShareId | String | Query | 否 | 3e47****** | NFS共享ID。 |
| AclIds | String | Query | 是 | [2000000000,2000000001] | ACL ID列表，最多100个。请通过 DescribeNfsAcls接口获取。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |

**示例**

请求示例

```
&AclIds=[2000000000,2000000001] &FileSystemId=efs-nas-c*****
```

&公共请求参数阿里云弹性文件存储 EFS-NAS 开发正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************" } |  |

### 快照

#### 7.14.1. CreateSnapshot

创建一个快照。

**注意事项**

单个文件系统推荐128个快照，不能超过2048个。所有文件系统总共最多支持创建8192个快照。 如果一个文件系统的快照还未创建完成，则无法为该文件系统再次创建快照，建议快照的创建时间间隔10分钟以上。 快照只会备份某一时刻的数据，创建快照期间，操作文件系统产生的增量数据不会同步到快照中。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Body | 是 | efs-nas-c***** | 文件系统ID。 |
| SnapshotName | String | Body | 否 | testSnapshotName | 快照名称。 |
| Description | String | Body | 否 | 测试使用 | 快照描述信息。 |
| Lock | String | Body | 否 | true | 是否锁定快照。取值范围如下： true：锁定。 false（默认）：未锁定。 快照锁定后，当快照超过保留时间后系统不会自动删除该快照，且快照只有手动解锁后才能删除。 |
| Retention | String | Body | 否 | never | 快照的保留时间，系统会自动删除超过保留时间的快照。 如需由系统自动管理快照生命周期，请设置此参数为正整数和单位组成的字符串。其中单位可选h（小时）、d（天数）、m（月）、 y（年）。例如取值为24h或者1d，表示创建的快照保留24小时或1天后删除。 如需快照永不过期，请设置此参数为never。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| SnapshotId | String | snap-1764836************ | 快照ID。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &SnapshotName=testSnapshotName
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "SnapshotId":"snap-1764836************", "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.14.2. ModifySnapshot

修改指定快照的名称、描述信息、保留时间等属性。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotId | String | Body | 是 | snap-1764836************ | 快照ID。 |
| SnapshotName | String | Body | 否 | testSnapshotName | 快照名称。 |
| Description | String | Body | 否 | 测试使用 | 快照描述信息。 |
| Lock | String | Body | 否 | true | 是否锁定快照。取值范围如下： true：锁定。 false（默认）：未锁定。 快照锁定后，当快照超过保留时间后系统不会自动删除该快照，且快照无法手动删除。 |
| Retention | String | Body | 否 | 7d | 快照的保留时间，系统会自动删除超过保留时间的快照。 如需由系统自动管理快照生命周期，请设置此参数为正整数和单位组成的字符串。其中单位可选h（小时）、d（天数）、m（月）、 y（年）。例如取值为24h或者1d，表示创建的快照保留24小时或1天后删除。 如需快照永不过期，请设置此参数为never。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| SnapshotId | String | snap-1764836************ | 快照ID。 |

**示例**

请求示例

```
&SnapshotId=snap-1764836************
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "SnapshotId":"snap-1764836************", "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

#### 7.14.3. DescribeSnapshots

查询指定文件系统一个或多个快照的信息。

**注意事项**

如果未设置参数，则系统会返回所有文件系统的快照列表。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Body | 否 | efs-nas-0***** | 文件系统ID。 |
| SnapshotId | String | Body | 否 | snap-1764836************ | 快照ID。 |

阿里云弹性文件存储 EFS-NAS 开发

|  |  |  |  |  | 指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| PageSize | Integer | Body | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |
| PageNum | Integer | Body | 否 | 1 | 分页页数。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |  |  |
|---|---|---|---|---|---|
| Snapshots | Array | [{}] | 快照列表。 |  |  |
| -SnapshotId | String | snap-1764836************ | 快照ID。 |  |  |
| -SnapshotName | String | testSnapshotName | 快照名称。 |  |  |
| -FileSystemId | String | efs-nas-0***** | 快照所属文件系统ID。 |  |  |
| -Status | String | progressing | 快照状态。返回值如下： 1：创建成功 0：创建失败 |  |  |
| -CreateTime | String | 2025-12-15T09:55:41Z | 快照创建时间。按照ISO 8601标准表示，并使用 UTC 时间。格式为 yyyy-MM- ddThh:mmZ 。 |  |  |
|  |  |  |  | yyyy-MM- |  |
| -ExpirationTime | String | 2026-12-15T09:55:41Z | 快照过期时间。按照ISO 8601标准表示，并使用 UTC 时间。格式为yyyy-MM- ddThh:mmZ。 |  |  |
| -Retention | String | never | 快照保留时间。返回值为never（永不过期）或由正整数和单位组成的字符串。单位可选h（小时）、d（天数）、m（月）、y（年）。 |  |  |
| -Description | String | 测试使用 | 快照描述信息。 |  |  |
| -Lock | Boolean | true | 快照锁定状态。返回值为true（锁定）或false（未锁定）。 |  |  |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |  |  |
| TotalCount | Integer | 5 | 查询到的快照总数量。 |  |  |
| PageNum | Integer | 10 | 分页页数。 |  |  |
| PageSize | Integer | 1 | 每页资源个数。 |  |  |

|  | ddThh:mmZ |
|---|---|

**示例**

请求示例 &公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":10, "PageSize":1, "Snapshots":[ { "Status":"progressing", "SnapshotId":"snap-1764836************", "Description":"测试使用", "CreateTime":"2025-12-15T09:55:41Z", "FileSystemId":"efs-nas-0*****", "ExpirationTime":"2026-12-15T09:55:41Z", "Retention":"never", "SnapshotName":"testSnapshotName", "Lock":true } ] } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.14.4. DeleteSnapshot

删除指定的快照或取消正在创建的快照任务。

**注意事项**

快照删除后不支持恢复，请谨慎操作。 锁定状态的快照不支持删除，请调用ModifySnapshot接口解锁快照后再删除。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotId | String | Body | 是 | snap-1764836************ | 快照ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Result | String | true | 操作是否成功。返回值为true时表示成功。 |

**示例**

请求示例

```
&SnapshotId=snap-1764836************
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Result":"true" } |  |

#### 7.14.5. CreateScheduledSnapshot

为文件系统创建定时快照。创建后，系统将按照指定时间周期自动为文件系统生成快照。

**注意事项**

单个文件系统推荐保留 128 个快照，最多创建 2048 个快照。所有文件系统最多创建 8192 个快照。 如果一个文件系统的快照还未创建完成，则无法为该文件系统再次创建快照，建议快照的创建时间间隔10分钟以上。 快照只会备份某一时刻的数据，创建快照期间，操作文件系统产生的增量数据不会同步到快照中。 如果为单个文件系统多次绑定不同的定时快照策略，则这些定时快照策略会同时对该文件系统生效。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotPolicyId | String | Query | 是 | sp-17748631231******** | 定时快照策略ID。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| Trigger | Boolean | Query | 是 | true | 创建绑定后是否立即触发一次快照创建。 false（默认）：遵从快照定时策略中的时间进行创建。 true：立即执行首次快照创建。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |

|  |  |  | 指南·API参考 |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |
| ScheduledSnapshotId | String | snap-17781404842******** | 定时快照绑定ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateScheduledSnapshot &SnapshotPolicyId=sp-17748631231******** &FileSystemId=efs-nas-c***** &Trigger=true
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "ScheduledSnapshotId":"snap-17781404842********", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |

#### 7.14.6. DescribeSnapshotPolicyBindings

查询快照策略与文件系统的绑定关系列表，支持按策略ID或文件系统ID过滤，支持分页。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotPolicyId | String | Body | 否 | sp-177909055113******** | 快照策略ID。 |
| FileSystemId | String | Body | 否 | efs-nas-c***** | 文件系统ID。 |
| PageSize | Integer | Body | 否 | 10 | 分页查询时每页返回的资源数量。默认值为20。 |
| PageNum | Integer | Body | 否 | 1 | 分页页数。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SnapshotPolicyBindings | Array | {[]} | 定时快照策略绑定的文件系统列表。 |
| -FileSystemId | String | efs-nas-0***** | 文件系统ID。 |
| -SnapshotPolicyId | String | sp-17748631231******** | 定时快照策略ID。 |
| -CreateTime | String | 2026-05-25T09:55:41Z | 为文件系统绑定该定时快照策略的时间。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 5 | 查询到的文件系统总数量。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

| 阿里云弹性文件存储指南·API参考 | EFS-NAS 开发 |  |  |
|---|---|---|---|

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 下一个查询开始的Token，NextToken为空表示没有下一个。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSnapshotPolicyBindings
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "SnapshotPolicyBindings":[ { "SnapshotPolicyId":"sp-17748631231********", "CreateTime":"2026-05-25T09:55:41Z", "FileSystemId":"efs-nas-0*****" } ] } |  |

#### 7.14.7. DeleteScheduledSnapshot

解除文件系统与快照策略的绑定，停止该文件系统上的定时快照。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotPolicyId | String | Query | 是 | sp-17748631231******** | 定时快照策略ID。 |
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |
| ScheduledSnapshotId | String | snap-17781404842******** | 删除的定时快照绑定ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteScheduledSnapshot &SnapshotPolicyId=sp-17748631231******** &FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ScheduledSnapshotId":"snap-17781404842********",
 "HttpStatusCode":"200",
 "Code":"200",
 "Success":true
}
```

### 快照策略

#### 7.15.1. CreateSnapshotPolicy

创建一个快照策略，用于后续绑定到文件系统实现定时快照。

**注意事项**

用户可创建的定时快照策略上限为128个。单个文件系统最多支持绑定8个定时快照策略。 定时快照策略可应用于所选组织、资源集和地域内的任一文件系统，请在配置前根据集群存储容量及备份需求合理评估，避免资源浪费或性能影响。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| ClusterId | String | Body | 是 | cluster-123 | 集群ID。 |
| SnapshotPolicyNa me | String | Body | 是 | mysnapshotpolicy | 快照策略名称。 |
| CronExpression | String | Body | 是 | 0 0 * * * | Cron表达式，定义快照触发周期。 |
| ExpireType | Boolean | Body | 是 | true | 快照是否按时间过期。取值范围如下： true：表示按时间过期，需配合 RetentionNum和RetentionUnit使用。 false：永不过期。 |
| RetentionNum | Integer | Body | 否 | 30 | 过期时间时长。仅当设置ExpireType为true时有效。 |
| RetentionUnit | String | Body | 否 | d | 过期时间单位。仅当设置ExpireType为true时有效。可选值包括h（小时）、d（天）、 t（月）、y（年）。 |
| Description | String | Body | 否 | snapshotpolicy test | 策略描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| SnapshotPolicyId | String | sp-17748631431******** | 快照策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=CreateSnapshotPolicy &SnapshotPolicyName=mysnapshotpolicy &CronExpression=0 0 2 ? * 1-7 &ExpireType=true
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "SnapshotPolicyId":"sp-17748631431********", "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.15.2. ModifySnapshotPolicy

修改已有快照策略的配置，包括快照周期、过期删除等。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotPolicyId | String | Body | 是 | sp-17748631431******** | 快照策略ID。 |
| SnapshotPolicyNa me | String | Body | 否 | mysnapshotpolicy | 快照策略名称。 |
| CronExpression | String | Body | 否 | 0 0 * * * | Cron表达式，定义快照触发周期。 |
| ExpireType | Boolean | Body | 否 | true | 快照是否按时间过期。取值范围如下： true：表示按时间过期，需配合 RetentionNum和RetentionUnit使用。 false：永不过期。 |
| RetentionNum | Integer | Body | 否 | 30 | 过期时间时长。仅当设置ExpireType为true时有效。 |
| RetentionUnit | String | Body | 否 | d | 过期时间单位。仅当设置ExpireType为true时有效。可选值包括h（小时）、d（天）、 t（月）、y（年）。 |
| Description | String | Body | 否 | testDescription | 策略描述。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| SnapshotPolicyId | String | sp-17748631431******** | 快照策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=ModifySnapshotPolicy &SnapshotPolicyId=sp-17748631431********
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "SnapshotPolicyId":"sp-17748631431********", "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

#### 7.15.3. DescribeSnapshotPolicies

查询快照策略列表，支持按文件系统或策略ID过滤，支持分页。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Body | 否 | efs-nas-c***** | 文件系统ID。 |
| SnapshotPolicyId | String | Body | 否 | sp-177909055113******** | 快照策略ID。 |
| PageSize | Integer | Body | 否 | 10 | 页面大小，默认值为10。 |

阿里云弹性文件存储 EFS-NAS 开发

|  |  |  |  |  | 指南·API参考 |
|---|---|---|---|---|---|
| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
| PageNum | Integer | Body | 否 | 1 | 页码，默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| SnapshotPolicies | Array | [{}] | 自快照策略详情列表。 |
| -SnapshotPolicyId | String | sp-17748631431******** | 快照策略ID。 |
| -SnapshotPolicyName | String | mysnapshotpolicy | 快照策略名称。 |
| -CronExpression | String | 0 0 * * * | Cron表达式。表示快照触发周期。 |
| -ExpireType | String | true | 是否按时间过期。 |
| -RetentionNum | Integer | 30 | 过期时间时长。 |
| -RetentionUnit | String | d | 过期时间单位。 |
| -Description | String | my sanpshot policy | 快照策略描述信息。 |
| -CreateTime | String | 2025-10-15T09:55:41Z | 快照策略的创建时间。 |
| - AssociatedDirectoryCount | Integer | 1 | 快照策略关联的目录数量。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Long | 5 | 查询到的快照策略总数量。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |
| NextToken | String | FFmyTO70tTpLG6I3FmYAXGKPd* *** | 下一个查询开始的Token，NextToken为空表示没有下一个。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DescribeSnapshotPolicies
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "TotalCount":5, "RequestId":"F0A8A039-930D-5EC1-97C8-************", "PageNum":1, "PageSize":10, "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****", "SnapshotPolicies":[ { "RetentionNum":30, "AssociatedDirectoryCount":1, "SnapshotPolicyId":"sp-17748631431********", "Description":"my sanpshot policy", "RetentionUnit":"d", "CreateTime":"2025-10-15T09:55:41Z", "ExpireType":"true", "SnapshotPolicyName":"mysnapshotpolicy", "CronExpression":"0 0 * * *" } ] } |  |

#### 7.15.4. DeleteSnapshotPolicy

阿里云弹性文件存储 EFS-NAS 开发删除指定的快照策略。

**注意事项**

删除定时快照策略前请确保该策略不存在关联目录。解除关联操作不会删除关联目录本身。 定时快照策略删除后不可恢复，请谨慎操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| SnapshotPolicyId | String | Body | 是 | sp-17748631431******** | 快照策略ID。 |
| Force | Boolean | Body | 否 | true | 是否强制删除。默认值为false。快照策略仍绑定有文件系统时需指定为true才能删除。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| SnapshotPolicyId | String | sp-17748631431******** | 删除的快照策略ID。 |

**示例**

请求示例

```
http(s)://[Endpoint]/?Action=DeleteSnapshotPolicy &SnapshotPolicyId=sp-17748631431********
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "SnapshotPolicyId":"sp-17748631431********", "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Success":true } |  |

### WORM

#### 7.16.1. CreateWorm

为文件系统启用WORM策略。文件系统启用WORM策略后，文件在写入完成时可手动设置或自动进入保护状态。在保护期间，文件仅允许读取，禁止修改与删除。

**注意事项**

目前仅支持合规模式，合规模式下任何用户不可删除和修改处于WORM保护期内的目录/文件。 基于合规考虑，文件系统启用WORM策略后，该文件系统的WORM不支持取消，且不可重复配置，请谨慎操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| MinProtectPeriod | String | Query | 是 | 5d | 最小保护期。手动设置文件的保护期时，文件遵循的最小保护时长。可选具体时长或 infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为30y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 5d。 设置为infinity时，表示将保护期设置为最大。 |

阿里云弹性文件存储 EFS-NAS 开发

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| MaxProtectPeriod | String | Query | 是 | 1y | 最大保护期。手动设置文件的保护期时，文件遵循的最大保护时长。可选具体时长或 infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为70y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 1y。 设置为infinity时，表示将保护期设置为最大。 |
| DefaultProtectPerio d | String | Query | 是 | 1t | 默认保护期。未手动设置保护期时，文件进入保护状态后遵循的默认保护时长。可选具体时长或 infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为70y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 1t。 设置为infinity时，表示永久保护文件。 |
| AutoLockPeriod | String | Query | 是 | 3d | 自动锁定期。文件写入后，当超过自动锁定期且未被再次修改时，文件将自动进入WORM保护中状态。 取值由数字和单位后缀组成，最大值为45d。其中单位后缀可选h（小时）、d（天）和 t（月）。例如3d。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |
| WormId | String | worm-******** | WORM策略ID。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &MinProtectPeriod=5d &MaxProtectPeriod=1y &DefaultProtectPeriod=1t &AutoLockPeriod=3d
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "WormId":"worm-********", "Code":"200", "Success":true } |  |

#### 7.16.2. UpdateWorm

修改 WORM 保护策略的保护期配置。

**注意事项**

合规模式下保护期只能延长不能缩短，且不允许修改自动锁定期。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。 阿里云弹性文件存储 EFS-NAS 开发

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WormId | String | Query | 是 | worm-******** | WORM策略ID。 |
| MinProtectPeriod | String | Query | 否 | 5d | 延长最小保护期。手动设置文件的保护期时，文件遵循的最小保护时长。可选具体时长或 infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为30y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 5d。 设置为infinity时，表示将保护期设置为最大。 |
| MaxProtectPeriod | String | Query | 否 | 1y | 延长最大保护期。手动设置文件的保护期时，文件遵循的最大保护时长。可选具体时长或 infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为70y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 1y。 设置为infinity时，表示将保护期设置为最大。 |
| DefaultProtectPerio d | String | Query | 否 | 1t | 延长默认保护期。未手动设置保护期时，文件进入保护状态后遵循的默认保护时长。可选具体时长或infinity（无限期）。 设置为具体时长时，需由数字和单位后缀组成，最大值为70y。其中单位后缀可选h（小时）、d（天）、t（月）和y（年）。例如 1t。 设置为infinity时，表示永久保护文件。 |
| AutoLockPeriod | String | Query | 否 | - | 自动锁定期不支持修改。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |
| WormId | String | worm-******** | WORM策略ID。 |

**示例**

请求示例

```
&WormId=worm-******** &MinProtectPeriod=5d
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "WormId":"worm-********", "Code":"200", "Success":true } |  |

#### 7.16.3. DescribeWorms

查询 WORM 保护策略列表，支持按 WormId 或文件系统ID过滤，支持分页。

**请求头**

阿里云弹性文件存储 EFS-NAS 开发该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| WormId | String | Body | 否 | worm-6***** | WORM策略ID。 |
| FileSystemId | String | Body | 否 | efs-nas-c***** | 文件系统ID。 |
| PageSize | Integer | Body | 否 | 20 | 页面大小，默认值为20。 |
| PageNum | Integer | Body | 否 | 1 | 页码。默认值为1。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| Worms | Array | [{}] | WORM 策略列表。 |
| -WormId | String | worm-******** | WORM策略ID。 |
| -FileSystemId | String | efs-nas-0***** | 文件系统ID。 |
| -Status | String | active | WORM状态。 |
| -Mode | String | compliance | WORM模式。仅支持compliance（合规模式）。 |
| -Path | String | /efs-nas-******** | WORM 保护路径。 |
| -MinProtectPeriod | String | 5d | 最小保护期。 |
| -MaxProtectPeriod | String | 1y | 最大保护期。 |
| -DefaultProtectPeriod | String | 1t | 默认保护期。 |
| -AutoLockPeriod | String | 3d | 自动锁定期。 |
| -CreateTime | String | 2026-05-17T16:26:22Z | WORM策略的创建时间。时间为ISO 8601格式。 |
| -UpdateTime | String | 2026-05-17T16:26:22Z | WORM策略的修改时间。时间为ISO 8601格式。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 1 | WORM策略的总数量。 |
| PageNum | Integer | 1 | 分页页数。 |
| PageSize | Integer | 10 | 每页资源个数。 |

**示例**

请求示例 &公共请求参数正常返回示例 `JSON` 格式阿里云弹性文件存储 EFS-NAS 开发

```json
{
 "TotalCount":1,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "Worms":[
  {
   "Status":"active",
   "Path":"/efs-nas-********",
   "MinProtectPeriod":"5d",
   "Mode":"compliance",
   "CreateTime":"2026-05-17T16:26:22Z",
   "WormId":"worm-********",
   "MaxProtectPeriod":"1y",
   "PathId":"busybox",
   "AutoLockPeriod":"3d",
   "DefaultProtectPeriod":"1t",
   "RootfsName":"/",
   "UpdateTime":"2026-05-17T16:26:22Z",
   "FileSystemId":"efs-nas-0*****",
   "RootfsId":"busybox"
  }
```

]

```
}
```

### 回收站

#### 7.17.1. EnableTrash

启用回收站功能，允许删除的文件被移至回收站而非永久删除。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| Filter | String | Query | 否 | *.tmp,*.txt | 过滤规则，匹配前缀或后缀名的文件将不进入回收站。可使用通配符星号（*）代表任意字符。 单次支持配置多个规则，但是禁止配置嵌套规则 （例如 *ab 和 *b 、 cd* 和 c* ）。多个规则之间用半角逗号（,）分隔。 如果不设置任何过滤规则，则文件系统中的所有文件删除均会保存到回收站。 |
| ExpiredTime | Long | Query | 否 | 1440 | 回收站中的文件保留时间。单位为分钟。默认值为0。取值范围为0（永不过期）或大于等于 1440（1天）小于等于525600（1年）。 当文件在回收站中的保留时长达到设定的保留周期后，系统会自动清理回收站中过期的文件。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例阿里云弹性文件存储 EFS-NAS 开发

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |

#### 7.17.2. UpdateTrash

更新回收站中数据的保留时间或者过滤文件规则。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| Filter | String | Query | 否 | *.tmp | 过滤规则，匹配前缀或后缀名的文件将不进入回收站。可使用通配符星号（*）代表任意字符。 单次支持配置多个规则，但是禁止配置嵌套规则 （例如 *ab 和 *b 、 cd* 和 c* ）。多个规则之间用半角逗号（,）分隔。 如果不设置任何过滤规则，则文件系统中的所有文件删除均会保存到回收站。 |
| ExpiredTime | Long | Query | 否 | 14400 | 回收站中的文件保留时间。单位为分钟。默认值为0。取值范围为0（永不过期）或大于等于 1440（1天）小于等于525600（1年） 当文件在回收站中的保留时长达到设定的保留周期后，系统会自动清理回收站中过期的文件。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &ExpiredTime=14400
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |

#### 7.17.3. ListTrashFiles

查询文件系统的回收站中暂存的文件或目录。

**请求头**

阿里云弹性文件存储 EFS-NAS 开发该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| Limit | Long | Query | 否 | 10 | 返回资源个数。 |
| Path | String | Query | 否 | /test | 要查询的回收站中的文件路径。 |
| Start | String | Query | 否 | file10 | 开始查询的位置。填写文件名。例如目录下有 file1～file100，设置limit为10，则第一页查询到file1～file10，如果设置start为file10，则会查询到file11～file20。 |
| Prefix | String | Query | 否 | file | 匹配指定前缀的文件或目录。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| TrashFiles | Array | [{}] | 回收站中暂存的文件列表。 |
| -Files | Long | 1 | 文件数量。 当查询到的对象为文件时，返回值表示文件数量，固定为1。 当查询到的对象为目录时，返回值表示该目录下所有文件的总数。 |
| -TrashPath | String | /efs-nas- ba4c37/.trash/current/file11 | 回收站中文件的存放路径。 |
| -Name | String | file11 | 文件名称。 |
| -Size | Long | 1024 | 文件大小，单位为字节。 当查询到的对象为文件时，返回值表示文件大小。 当查询到的对象为目录时，返回值表示该目录下所有文件的总大小。 |
| -ExpiredTime | String | 2025-12-15T16:00:00Z | 文件在回收站过期的时间。 |
| -Type | String | Regular File | 返回对象类型。返回值如下： Directory：目录 Regular File：文件 |
| -Change | String | 2025-12-10T16:00:00Z | 文件的修改时间。 |
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| TotalCount | Integer | 10 | 废弃参数，无此返回值。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "TrashFiles":[ { "Type":"Regular File", "Size":1024, "ExpiredTime":"2025-12-15T16:00:00Z", "Change":"2025-12-10T16:00:00Z", "Files":1, "TrashPath":"/efs-nas-ba4c37/.trash/current/file11", "Name":"file11" } ] } |  |

阿里云弹性文件存储 EFS-NAS 开发

#### 7.17.4. RestoreTrashFile

恢复回收站中暂存的文件。

**注意事项**

单次操作只能恢复一个文件或目录，恢复指定目录时会递归恢复目录下的所有文件。 文件被恢复后会进行数据整理，数据整理期间读请求性能稍有下降。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |
| Path | String | Query | 是 | /test | 要恢复的回收站中文件完整路径。 |
| Overwrite | Boolean | Query | 否 | false | 是否覆盖指定路径中的同名文件或目录。取值范围如下： false（默认）：跳过原路径中的同名文件或目录。 true：覆盖原路径中的同名文件或目录。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &Path=/test
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |

#### 7.17.5. RemoveTrashFile

彻底删除回收站中暂存的文件或目录。

**注意事项**

彻底删除目录时，目录中的内容会被递归清理。 单个文件系统一次只能执行一个彻底删除操作。正在彻底删除文件或目录时，无法发起新的恢复或清理操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

| 阿里云弹性文件指南·API参考 | 存储 EFS- | NAS 开发 |  |  |  |
|---|---|---|---|---|---|

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| Path | String | Query | 是 | /test | 要删除的文件或目录路径。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c***** &Path=/test
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |

#### 7.17.6. DisableAndCleanTrash

关闭文件系统的回收站功能，并清空回收站。

**注意事项**

关闭回收站会彻底删除回收站内的所有文件。 已关闭的回收站重新开启后，回收站内容为空，无法找回开启回收站功能前删除的文件。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例阿里云弹性文件存储 EFS-NAS 开发

```
http(s)://[Endpoint]/?Action=DisableAndCleanTrash &FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例 `JSON` 格式

```json
{
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "HttpStatusCode":"200",
 "Code":"200",
 "Success":true
}
```

#### 7.17.7. EmptyTrash

清空指定文件系统的回收站。

**注意事项**

回收站清空后，删除的文件不可恢复，请谨慎操作。

**请求头**

该接口使用公共请求头，无特殊请求头。请参见公共请求参数文档。

**请求参数**

| 参数名称 | 类型 | 位置 | 是否必选 | 示例 | 说明 |
|---|---|---|---|---|---|
| FileSystemId | String | Query | 是 | efs-nas-c***** | 文件系统ID。 |

**返回数据**

| 参数名称 | 类型 | 示例 | 说明 |
|---|---|---|---|
| RequestId | String | F0A8A039-930D-5EC1-97C8- ************ | 请求ID。 |
| Success | Boolean | true | 操作是否成功。返回值为true时表示成功。 |
| Code | String | 200 | 接口状态或POP错误码。 |
| Message | String | success | 错误信息。 |
| HttpStatusCode | String | 200 | HTTP状态码。 |

**示例**

请求示例

```
&FileSystemId=efs-nas-c*****
```

&公共请求参数正常返回示例

| JSON | 格式 |
|---|---|
| { "RequestId":"F0A8A039-930D-5EC1-97C8-************", "Message":"success", "HttpStatusCode":"200", "Code":"200", "Success":true } |  |
