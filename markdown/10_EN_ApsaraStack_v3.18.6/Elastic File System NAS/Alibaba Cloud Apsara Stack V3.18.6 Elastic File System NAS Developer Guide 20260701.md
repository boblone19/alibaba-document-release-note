---
title: "Elastic File System NAS Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 145
source_pdf: "0e4378161fd9fc4f_Alibaba Cloud Apsara Stack V3.18.6 Elastic File System NAS Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E9%98%BF%E9%87%8C%E4%BA%91%E5%BC%B9%E6%80%A7%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20EFS-NAS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Elastic%20File%20System%20NAS%20Developer%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Elastic File System NAS Developer Guide 20260701

## Table of Contents

- 1 Preparations
  - 1.1 Get the file storage Endpoint
  - 1.2 Obtain AccessKey credentials
  - 1.3 Obtain the values of common request headers
- 2 Java SDK call examples
  - 2.1 Getting started
  - 2.2 User guide
    - 2.2.1 Install the Java SDK
    - 2.2.2 Set identity verification credentials
    - 2.2.3 Request connection configuration
    - 2.2.4 Make a call
    - 2.2.5 Error handling
- 3 Python SDK call examples
  - 3.1 Getting started
  - 3.2 User guide
    - 3.2.1 Install the Python SDK
    - 3.2.2 Set identity verification credentials
    - 3.2.3 Set HTTPS requests
    - 3.2.4 Make a call
    - 3.2.5 Error handling
- 4 Go SDK call examples
  - 4.1 Getting started
  - 4.2 User guide
    - 4.2.1 Install the Go SDK
    - 4.2.2 Set identity verification credentials
    - 4.2.3 Request connection configuration
    - 4.2.4 Make a call
    - 4.2.5 Error handling
- 5 API reference
  - 5.1 Call APIs
    - 5.1.1 Overview
    - 5.1.2 Request structure
    - 5.1.3 Return results
  - 5.2 RAM authentication
  - 5.3 Common parameters
  - 5.4 Region
    - 5.4.1 DescribeZones
  - 5.5 File system
    - 5.5.1 CreateFileSystem
    - 5.5.2 DescribeFileSystems
    - 5.5.3 ModifyFileSystem
    - 5.5.4 DeleteFileSystem
  - 5.6 User
    - 5.6.1 CreateFsUser
    - 5.6.2 DescribeFsUsers
    - 5.6.3 ModifyFsUser
    - 5.6.4 DeleteFsUser
  - 5.7 User group
    - 5.7.1 CreateFsUserGroup
    - 5.7.2 AddFsUsersToGroup
    - 5.7.3 RemoveFsUsersFromGroup
    - 5.7.4 DescribeFsUserGroups
    - 5.7.5 DeleteFsUserGroup
  - 5.8 SMB share
    - 5.8.1 CreateSmbShare
    - 5.8.2 DescribeSmbConnections
    - 5.8.3 DescribeSmbShares
    - 5.8.4 ModifySmbShare
    - 5.8.5 DeleteSmbShare
  - 5.9 SMB ACL
    - 5.9.1 BatchCreateSmbAcl
    - 5.9.2 DescribeSmbAcls
    - 5.9.3 BatchUpdateSmbAcl
    - 5.9.4 BatchDeleteSmbAcl
  - 5.10 NFS share
    - 5.10.1 CreateNfsShare
    - 5.10.2 DescribeNfsConnections
    - 5.10.3 DescribeNfsShares
    - 5.10.4 ModifyNfsShare
    - 5.10.5 DeleteNfsShare
  - 5.11 NFS ACL
    - 5.11.1 BatchCreateNfsAcl
    - 5.11.2 DescribeNfsAcls
    - 5.11.3 BatchUpdateNfsAcl
    - 5.11.4 BatchDeleteNfsAcl
  - 5.12 Snapshot
    - 5.12.1 CreateSnapshot
    - 5.12.2 ModifySnapshot
    - 5.12.3 DescribeSnapshots
    - 5.12.4 DeleteSnapshot
    - 5.12.5 CreateScheduledSnapshot
    - 5.12.6 DescribeSnapshotPolicyBindings
    - 5.12.7 DeleteScheduledSnapshot
  - 5.13 Snapshot policy
    - 5.13.1 CreateSnapshotPolicy
    - 5.13.2 ModifySnapshotPolicy
    - 5.13.3 DescribeSnapshotPolicies
    - 5.13.4 DeleteSnapshotPolicy
  - 5.14 WORM
    - 5.14.1 CreateWorm
    - 5.14.2 UpdateWorm
    - 5.14.3 DescribeWorms
  - 5.15 Recycle bin
    - 5.15.1 EnableTrash
    - 5.15.2 UpdateTrash
    - 5.15.3 ListTrashFiles
    - 5.15.4 RestoreTrashFile
    - 5.15.5 RemoveTrashFile
    - 5.15.6 DisableAndCleanTrash
    - 5.15.7 EmptyTrash

## 1 Preparations

### 1.1 Get the file storage Endpoint

When calling Apsara Stack APIs through the POP gateway, you must specify the service endpoint for the target cloud product.For EFS-NAS, you can construct the endpoint using the predefined format and variable values provided by the Apsara Infrastructure Management Platform. Alternatively, you can directly search for the endpoint in the platform's console.

**Method one: construct the Endpoint**

You can construct the file storage Endpoint using the predefined naming format and required variable values. The configuration format for the file storage Endpoint is `efs-`

```
nas.${global:region}.${global:internet-domain} .
```

**Note**

|   | ${global:region} |
|---|---|
| ${global:} |   |

To obtain the variable values, follow these steps:
1. Log on to the Apsara-Uni Manager O&M console.
2. In the top menu bar, choose **Platform O&M** > **Apsara Infrastructure Management** >
**Resource Management**. The **Product Cluster O&M** page appears.
3. On the **Product Cluster O&M** page, enter efs-nas in the **Product | Cluster** text box. Find
the EfsNasControllerCluster-A-xxx cluster and click **Cluster Details** in the Actions column.
4. On the **Cluster Details** page, select the **Desired State****Configuration** tab.
5. In the file list on the left, click **kv.conf**. Click the file content on the right and press Ctrl+F
to search for `region` and `internet-domain` .

| ${global:region} |   | with the value of |
|---|---|---|
| with the value of |   |   |

**Method two: find the Endpoint on the Apsara Infrastructure**

**Management platform**

1. On the **Product Cluster O&M** page of the Apsara Infrastructure Management platform,
enter `efs-nas` in the **Product | Cluster** text box. Find the EfsNasControllerCluster-A-xxx cluster and click **Cluster Details** in the Actions column.
2. On the service list page, search for the `efs-nas-mgr` service and click **Details** in the
Actions column.
3. On the service details page, click the **EfsNasMgr#** component. In the component
information section, select the **Resources** tab.
4. Search for the resource named `EFS-NAS` . Click the information in the **Resource Request**
**Parameters** column. The value of the **domain** parameter is the Endpoint for EFS-NAS.

### 1.2 Obtain AccessKey credentials

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one of the preceding types of AccessKey credentials for authentication when you call API operations.

**Background information**

An AccessKey pair is used to verify the identity of a request sender based on symmetric encryption. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. AccessKey credentials can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token.

**Obtain an AccessKey pair**

The Apsara Uni-manager Management Console provides two types of AccessKey pairs: those for personal accounts and those for organization accounts. We recommend that you use AccessKey pairs for personal accounts to call the API operations of the Apsara Uni-manager Management Console and cloud services.

> **Note:** Only operations administrators and level-1 organization administrators can obtain AccessKey pairs for organization accounts.

**Obtain the AccessKey pair of a personal account**

To use AccessKey pairs for personal accounts, you must configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region to which the instance that you want to access belongs. Example: cn-qingdao-****-****. |
| x-acs-organizationid | The ID of the organization to which the instance that you want to access belongs. For information about how to obtain the ID, see the Obtain an organization ID section of the Obtain the values of common request headers topic. |
| x-acs-resourcegroupid | The ID of the resource group to which the target instance belongs. For information about how to obtain the ID, see the Obtain a resource group ID section of the Obtain common Header parameters topic. |
| x-acs-instanceid | The ID of the instance resource that you want to access. For example, you can find the ID of a file system in the file system list. |

1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

> **Note:** The AccessKey ID and AccessKey secret provide access to your cloud resources and grant full permissions to your account. Keep them confidential.

**Obtain the AccessKey pair of an organization**

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. To obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

**Obtain an STS AccessKey 3-tuple**

Alibaba Cloud Security Token Service (STS) is a service for managing temporary access permissions. An STS AccessKey is a trituple that consists of an AccessKey ID, an AccessKey secret, and a SecurityToken. All three components are required when you use STS to call the APIs of cloud products.
1. Obtain the RAM role.
i. Log on to the Apsara Uni-manager Operations Console. ii. Click the profile picture in the upper-right corner of the page and then click User Information. iii. Click View Current Role Policy. iv. In the View Policies of Current Role dialog box, view your RAM role.
2. Obtain the endpoint of STS.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top menu bar, choose **Platform O&M > Apsara Infrastructure Management >**
**Resource Management**.
iii. In the navigation pane on the left of Apsara Infrastructure Management, click iv. On the **Product and Cluster O&M** page, set **Product | Cluster** to **ascm-A**. v. In the **Operation** column for the cluster, click **Cluster Details**. vi. On the cluster details page, click the **Desired State Configuration** tab. vii. In the left-side file list, click **kv.conf**. In the right-side pane, click **Show Content**. Press Ctrl+F and search for the value of `internet-domain` . viii. After you obtain the value, construct the Endpoint using the format `sts-` vpc.${global:internet-domain} . Replace ${global:internet-domain} with the value of

```
 internet-domain .
```

> **Note:** Delete ${global:} in the final endpoint.

3. Call the AssumeRole operation of STS to obtain the AccessKey 3-tuple. The following
example shows how to call the operation using STS SDK for Java.

**Note**

|   | <yourAccessKeyID> |
|---|---|
| <yourRoleSessionName> |   |

> `<sts.aliyuns.com>` are placeholders. Replace them with your actual values. Do not include the angle brackets (<>).

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Replace the placeholders with your actual region ID, AccessKey ID, and AccessK
ey secret.
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
    // Obtain the STS trituple.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the actual STS Endpoint. The format is typicall
y sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("<sts.aliyuns.com>");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // The name of the role session. This is a custom parameter. It is usually set to
the identity of the user who calls the API operation, such as the username. Replace " <yourRoleSessionName>" with your custom value.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // The Alibaba Cloud Resource Name (ARN) of the RAM role to assume. This role mus
t be a RAM role that has an ASCM user as a trusted entity. Replace "<yourRoleArn>" wi th the actual RAM Role ARN that you obtained in Step 1.
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
    return null;
```

4. After you obtain the STS AccessKey trituple, you can use it to call cloud product API
operations. The following Java SDK example shows how to use an STS AccessKey to call a file storage API operation. The DescribeZones API operation is used as an example.

> **Note:** In the following code example, `<efs-nas.aliyuns.com>` , `<yourRegionID>` ,

| <yourStsAccessKeySecret> |   |   |   |
|---|---|---|---|
|   |   | , |   |

> `<yourResourceGroupID>` , and `<yourOrganizationID>` are placeholders. Replace them with your actual values. Do not include the angle brackets (<>). The file storage Endpoint must be configured as an environment variable.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the ID of the region where the instance resource
resides.
    // Replace "<yourStsAccesskey>" and "<yourStsAccessSecret>" with the AccessKey ID
and AccessKey secret from the STS trituple that you obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysMethod(com.aliyuncs.http.MethodType.POST);
    // The file storage Endpoint. Replace it with the actual value.
    request.setSysDomain("<efs-nas.aliyuns.com>");
    request.setSysVersion("2017-06-26");
    request.setSysAction("DescribeZones");
    request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
    // Replace "<yourRegionID>" with the ID of the region where the instance resource
resides.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token from the STS trituple that yo
u obtained in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace this with the ID of the resource group to which the instance
resource belongs.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace this with the ID of the organization to which the instance r
esource belongs.
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
```

### 1.3 Obtain the values of common request headers

**request headers**

In Apsara Stack, you must specify multiple common request headers to call API operations. Then, common response parameters are returned in the results.

**Common request parameters**

You must specify the common request parameters in the code to call API operations in Apsara Stack.

| For example, in a Java SDK call, replace | <yourResourceGroupID> | in |
|---|---|---|
| request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>") |   |   |

resource group ID that you obtained.

| Name | Description |
|---|---|
| x-acs-regionid | The ID of the region in which the instance resource on which you want to perform operations resides. For more information, see the Obtain a region ID section of this topic. |
| x-acs-organizationid | The ID of the organization to which the instance resource on which you want to perform operations belongs. For more information, see the Obtain an organization ID section of this topic. |
| x-acs-resourcegroupid | The ID of the resource set to which the instance resource on which you want to perform operations belongs. For more information, see the Obtain a resource set ID section of this topic. |
| x-acs-instanceid | The ID of the file system resource that you want to manage. For more information, see Obtain a file system ID. |

| Note When you call Apsara Uni-manager Management Console APIs, you do not need to use the x-acs-organizationid , x-acs-resourcegroupid , or x-acs-instanceid header parameters. When you call APIs of other cloud products, you must include the x-acs- organizationid header parameter. Otherwise, the call fails and a permission error is returned. When you call APIs for other cloud products, add the resource group ID <x-acs- resourcegroupid> to the header parameters. This scopes your queries to the instance resources within the specified organization and resource group. If you do not specify the resource group ID <x-acs-resourcegroupid> , the default resource group for your organization is used. |   |   |
|---|---|---|
|   | <x-acs- |   |

| x-acs- |   |
|---|---|

**Obtain a region ID**

You can view the region IDs of resources in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resources** > **Regions**.
4. On the Regions page, find the organization that you want to view and click its name in the
organization tree.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call an API operation to obtain the ID of an organization. You can obtain the organization ID using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Development Tools** > **API & SDK** >
**OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. In the text box, enter `GetOrganizationList` to debug the API operation online. Set the
name parameter to the name of the target organization and initiate the call. After the call is successful, the value of the **id** field in the **Call Result** section is the organization ID.

**Obtain a resource set ID**

You must call an API operation to obtain the ID of a resource set. You can obtain the resource set ID using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Development Tools** > **API & SDK** >
**OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. In the text box, enter `ListResourceGroup` to debug the API operation online. After the call
is successful, the value of the **id** field in the **Call Result** section is the resource group ID.

**Obtain a file system ID**

You can obtain the file system ID from the file system list in the File Storage EFS-NAS console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products** > **Storage** > **File Storage EFS-NAS**.
3. In the navigation pane on the left, click **File System Management**.
4. In the file system list, obtain the file system ID from the **File System ID/Name** column.

**Common response parameters**

The following table describes the common response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Name | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |

| ResourceGroup | The ID of the resource set. |
|---|---|
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

## 2 Java SDK call examples

### 2.1 Getting started

This topic describes how to obtain the EFS-NAS Java SDK and use it to make API calls.

**Prerequisites**

Obtain an AccessKey or a Security Token Service (STS) AccessKey. Obtain the endpoint for file storage. Install JDK 1.8 or later versions.

**Install the Apsara Stack Java SDK**

To use the Apsara Stack Java SDK core library, add the corresponding dependency to your pom.xml file or download the Alibaba Cloud SDK. The EFS-NAS feature requires version 4.5.17 or later of the Alibaba Cloud Java SDK core library. For more information, see Install the Java SDK.

**Use the Java SDK**

The main steps to call the Apsara Stack Java SDK are as follows:
1. Create and initialize a DefaultAcsClient instance.
2. Create an API request and set its parameters.
3. Send the request and handle the response or exceptions.
The following sample code shows how to use the DescribeFileSystems operation of EFS-NAS to retrieve file system information:

> **Note:** Set the REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET environment variables to your region ID, AccessKey ID, and AccessKey secret.
> Replace the variable parameters in the sample code with your actual information. The angle brackets (<>) are placeholders and should not be included in your final code. The following parameters must be replaced:
> <efs-nas.aliyuns.com>: Replace with your actual product endpoint.
> <readTimeout>: Set the read timeout period in milliseconds as needed.
> <connectionTimeout>: Set the connection timeout period in milliseconds as needed.
> <http://192.168.XX:33XX>: Replace with your actual proxy IP address and port.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig;
```

`i` `li` `h` `l`

```java
import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeFileSystemsExample {
    public static void main(String[] args) throws Exception {
        // Initialize the client.
        DefaultProfile profile = DefaultProfile.getProfile(
            System.getenv("REGION_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
```

);

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        Determine whether to set an HTTP proxy as needed. To set a proxy, use the fol
lowing method. Replace the placeholder with your actual proxy IP address and port.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`*/`

```java
        // Set the connection timeout period in milliseconds.
        // clientConfig.setConnectionTimeoutMillis(1000L);
        // Set the read timeout period in milliseconds.
        // clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create a request.
        CommonRequest request = new CommonRequest();
        // Set the request method.
        request.setSysMethod(com.aliyuncs.http.MethodType.POST);
        // The endpoint of file storage. Replace it with the actual endpoint.
        request.setSysDomain("<efs-nas.aliyuns.com>");
        // The parameters for the file storage API.
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
        // Set the business parameters for the operation.
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "10");
        // Set the headers.
        // Set the identity to indicate the call source. This parameter is required b
ut has no practical effect. Set it to any value.
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
        // When calling an Apsara Stack API, include common request headers such as x
-acs-regionid, x-acs-organizationid, x-acs-resourcegroupid, and x-acs-instanceid.
        // For details, refer to "Obtain Common Header Parameters" in the Development
Guide.
        // Send the request and print the result.
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println("Response status: " + response.getHttpStatus());
            System.out.println("Response data: " + response.getData());
        } catch (ServerException e) {
eprintStackTrace();
```

```java
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

### 2.2 User guide

#### 2.2.1 Install the Java SDK

This topic describes how to install the Java SDK. The Apsara Stack Java SDK supports JDK 1.8 and later. You can install the Apsara Stack Java SDK by adding a Maven dependency or by downloading the Alibaba Cloud Developer Toolkit (SDK). To use the file storage feature, install version 4.5.17 or later of the Alibaba Cloud Java SDK core library.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

#### 2.2.2 Set identity verification credentials

Before using the Apsara Stack SDK to call services, you must configure authentication credentials. This topic describes the supported methods.

**Configure access credentials**

After you obtain an AccessKey or a temporary credential from the Security Token Service (STS) and a region ID, set them as environment variables. This section uses an AccessKey as an example. The configuration for an STS temporary credential is similar. Follow the instructions for your platform.

**Windows**

Configure the environment variables in CMD or PowerShell.

**CMD**

1. Run the following commands in CMD to set the environment variables.

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. Restart CMD. Then, run the following commands to check whether the environment
variables are set.

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. Run the following commands in PowerShell.

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. You can run the following command to check if the environment variable has taken effect.

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

1. Run the following commands in the command-line interface (CLI) to append the
environment variable settings to the ~/.bashrc file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```

2. Run the following command to apply the changes.

```
source ~/.bashrc
```

3. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. Run the following command in the terminal to check the default shell type.

```
echo $SHELL
```

2. Follow the steps for your default shell type.
Zsh a. Run the following commands to append the environment variable settings to the ~/.zshrc file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshr
```

`c` b. Run the following command to apply the changes.

```
source ~/.zshrc
```

c. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash a. Run the following commands to append the environment variable settings to the ~/.bash_profile file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash _profile
```

b. Run the following command to apply the changes.

```
source ~/.bash_profile
```

c. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**Initialize the client**

The Java SDK supports identity verification using an AccessKey or an STS AccessKey.

```
DefaultProfile profile = DefaultProfile.getProfile(
    System.getenv("REGION_ID"), // Get the region ID from the environment variable.
    // Get the AccessKey ID and AccessKey secret from the environment variables.
    System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
    System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
    // To use an STS AccessKey for identity verification, set the SecurityToken to the
ALIBABA_CLOUD_STS_SECURITY_TOKEN environment variable.
    // To use an AccessKey, set SecurityToken to null.
    System.getenv("ALIBABA_CLOUD_STS_SECURITY_TOKEN")
```

);

#### 2.2.3 Request connection configuration

This topic describes how to configure request connections using HttpClientConfig. Use the following code to configure HttpClientConfig. You can select and set the configuration items as needed.

> **Note:** Replace the variables in the following code example with your actual information. Do not include the angle brackets (<>) in your code.
> The variables to replace are as follows:
> Replace <readTimeout> with the read timeout in milliseconds (ms).
> Replace <connectionTimeout> with the connection timeout in milliseconds (ms).
> Replace <maxRequestsPerHost> with the maximum number of requests per host. The value must be an integer.
> Replace <maxRequests> with the maximum number of requests. The value must be an integer.
> Replace <http://192.168.XX.XX:33XX> with the actual proxy IP address and port.

```
// Obtain the HttpClientConfig object HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Set whether to ignore SSL certificates clientConfig.setIgnoreSSLCerts(true); // (Optional) Set the read timeout in milliseconds (ms) clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Set the connection timeout in milliseconds (ms) clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Set the maximum number of requests per host. The data type is INT. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Set the maximum number of requests. The data type is INT. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Set the protocol type clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Set a proxy as needed. The methods are as follows: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace with your actual proxy IP address and port.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 2.2.4 Make a call

You can use the generic CommonRequest method to call an API operation if an SDK is not available or if the provided SDK does not meet your needs. The CommonRequest method lets you call any OpenAPI operation.

**Introduction to CommonRequest**

CommonRequest has the following features: Lightweight: You only need the core package to make calls. You do not need to download and install the SDK for each product. Simple: You can call the latest API operations without updating the SDK. Fast iteration. To make a CommonRequest, you need the following parameters. You can find these parameters in the EFS-NAS API documentation. Domain: The endpoint of the product. API version: The version number of the API operation. The format is YYYY-MM-DD. You can find the API version in the common parameters section of the API documentation for each product. API operation information: The name of the API operation to call. Obtain the `Action` parameter. Use `request.setSysAction("<Action>")` to specify the API operation name.

| For example, for the |   | DescribeFileSystems |   | ope |
|---|---|---|---|---|
| request.setSysAction("DescribeFileSystems") |   |   |   |   |
| you make a | CommonRequest |   | . |   |

**Create a CommonRequest**

You can use the CommonRequest method to call any OpenAPI operation.

```
// Create an API request and set the parameters. CommonRequest request = new CommonRequest(); // API operation information parameters for file storage. request.setSysProduct("efs-nas"); request.setSysVersion("2017-06-26"); request.setSysAction("DescribeFileSystems"); request.setSysUriPattern("<yourCallUriPattern>"); // Endpoint of file storage. request.setSysDomain("<efsnasEndpoint>"); // Set the request method. request.setSysMethod(MethodType.POST); // Set the headers. // Optional. Replace with your actual resource group ID. request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>"); // Required. Replace with your actual organization ID. request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>"); // Set the identity to identify the call source. This has no practical effect and can be set to any value. This parameter is required. request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>"); // Set the business parameters for the API operation. ... // Set the Content-Type. request.setHttpContentType(FormatType.JSON);
```

**Note**

|   | <yourCallUriPattern> |
|---|---|
| <yourCallerSdkSource> |   |

> include the angle brackets (<>) in your final code.

**Set Alibaba Cloud core SDK parameters**

When you use the Alibaba Cloud core SDK to make an API request, you can set four types of parameters: Path, Query, Body, and Header. When you call a specific API operation, set the parameters according to their locations specified in the development document.

|   |   | Parameter type | Description |   | Code sample |
|---|---|---|---|---|---|
|   |   |   | Path parameters are used to replace variables in the UriPattern set in the request. For example, in the URI "/clusters/[ClusterId] " , [ClusterId] can be replaced by setting the Path parameter "ClusterId=cluster1" . The final URI for the HTTP request is "/clusters/clusterId01 " . |   | CommonRequest request = new CommonRequest(); request.setSysUriPattern("/clusters/[ClusterId] "); request.putPathParameter("ClusterId", "clusterId01"); |
|   |   |   |   | "/clusters/[ClusterId] |   |
|   |   |   | " |   |   |
|   |   | Path |   |   |   |
|   |   |   |   | "ClusterId=cluster1" |   |
|   |   |   |   | "/clusters/clusterId01 |   |
|   |   |   | " |   |   |
|   |   | Query | Query parameters are used to set the URL parameters in the request. They are generally used for GET requests. For example: "http://aliyun.com/api/? ClusterId=clusterId01&Clu sterName=clusterName01 ". |   | CommonRequest request = new CommonRequest(); request.putQueryParameter("ClusterId", "clusterId01"); request.putQueryParameter("ClusterName", "clusterName01"); |

| Body | Body parameters are used to set the HTTP content in the request. They are generally used for POST or PUT requests. Two formats are supported: application/json application/x-www-form- urlencoded Note When you set Body parameters, you must also set the HTTP Content-Type. | Set Body parameters as key-value pairs and set the HttpContentType. CommonRequest request = new CommonRequest(); request.putBodyParameter("ClusterId", "clusterId01"); request.putBodyParameter("ClusterName", "clusterName01"); // If Content-Type is set to application/x- www-form-urlencoded, the content data sent to the server is the string "ClusterId=clusterId01&ClusterName=clusterNam e01". request.setHttpContentType(FormatType.FORM); // Alternatively, if Content-Type is set to application/json, the content data sent to the server is the JSON string " {\"ClusterId\":\"clusterId01\",\"ClusterName\ ":\"clusterName01\"}". request.setHttpContentType(FormatType.JSON); Construct the HTTP content yourself and set HttpContent directly. CommonRequest request = new CommonRequest(); //Set the HTTP content in application/json format. String body = "{\"ClusterId\": \"clusterId01\", \"ClusterName\": \"clusterName01\"}"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.JSON); //Set the HTTP content in application/x- www-form-urlencoded format. String body = "ClusterId=clusterId01&ClusterName=clusterNam e01"; request.setHttpContent(body.getBytes(), "utf-8", FormatType.FORM); |
|---|---|---|
| Header | Header parameters are used to set the HTTP headers in the request. | CommonRequest request = new CommonRequest(); request.putHeadParameter("x-acs- organizationid", "3"); request.putHeadParameter("x-acs- resourcegroupid", "2"); |

**Make the call and process the response**

Refer to the following code to make the request and process the response.

```java
try {
    // Make the request and get the response.
    CommonResponse response = client.getCommonResponse(request);
    System.out.println("Response status: " + response.getHttpStatus());
    System.out.println("Response data: " + response.getData());
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    System.out.println("ErrCode:" + e.getErrCode());
    System.out.println("ErrMsg:" + e.getErrMsg());
    System.out.println("RequestId:" + e.getRequestId());
```

**Complete example**

The following code provides an example of how to call the EFS-NAS `DescribeFileSystems` operation to query a list of file systems.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeFileSystemsExample {
    public static void main(String[] args) throws Exception {
        // Initialize the client
        DefaultProfile profile = DefaultProfile.getProfile(
            System.getenv("REGION_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
            System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET")
```

);

```
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        Determine whether to set an HTTP proxy based on your needs. The following code
shows how to set a proxy. Replace with your actual proxy IP address and port.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`*/`

```
        // Set the connection timeout in milliseconds.
        // clientConfig.setConnectionTimeoutMillis(1000L);
        // Set the read timeout in milliseconds.
        // clientConfig.setReadTimeoutMillis(10000L);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create the request
CommonReqestreqest
```

`ne`

```
CommonReqest()
```

```java
        CommonRequest request = new CommonRequest();
        // Set the request method.
        request.setSysMethod(com.aliyuncs.http.MethodType.POST);
        // The endpoint of file storage. Replace it as needed.
        request.setSysDomain("<efs-nas.aliyuns.com>");
        // API operation information parameters for file storage.
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.setSysProtocol(com.aliyuncs.http.ProtocolType.HTTP);
        // Set the business parameters for the API operation.
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "10");
        // Set the headers.
        // Set the identity to identify the call source. This has no practical effect a
nd can be set to any value. This parameter is required.
        request.putHeadParameter("x-acs-caller-sdk-source","<yourCallerSdkSource>");
        // When you call an Apsara Stack API operation, you generally need to provide m
ultiple common header parameters, including x-acs-regionid, x-acs-organizationid, x-acs -resourcegroupid, and x-acs-instanceid. For more information, see "Obtain common header parameters" in the development guide.
        // Send the request and print the result
        try {
            CommonResponse response = client.getCommonResponse(request);
            System.out.println("Response status: " + response.getHttpStatus());
            System.out.println("Response data: " + response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

> **Note:** REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET represent the region ID, the AccessKey ID, and the AccessKey secret of your account. Set them as environment variables.
> In the code sample, replace all variables with your actual information. Do not include the angle brackets (<>) in your final code. The variables that need to be replaced are as follows:
> <efs-nas.aliyuns.com>: Replace with the actual endpoint of the product.
> <readTimeout>: Set the read timeout in milliseconds as needed.
> <connectionTimeout>: Set the connection timeout in milliseconds as needed.
> <http://192.168.XX:33XX>: Replace with the actual proxy IP address and port.

#### 2.2.5 Error handling

The Java SDK throws an exception when an error occurs. This error can be a server-side error or an SDK-side error. The exception contains an error code and an error message. In most cases, you only need to handle server-side errors based on the returned error messages. You do not need to handle errors that originate from the Java SDK. `ServerException` represents server-side errors. `ClientException` represents SDK-side errors. For example, if the following error occurs, modify the AccessKey ID based on the error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

To handle SDK errors, see the following code example:

```java
try {
    AcsResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // Add your error handling logic here.
    // For example, print the specific error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you encounter a difficult issue, contact Alibaba Cloud technical support and
provide the RequestID.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your error handling logic here.
    // For example, print the specific error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

s

## 3 Python SDK call examples

### 3.1 Getting started

This topic describes how to obtain the software development kit (SDK) and make calls.

**Prerequisites**

obtained an AccessKey or a Security Token Service (STS) AccessKey. obtained the endpoint for file storage.

**Install the core library for Python SDK**

To use the file storage feature, you must install the core library for the Alibaba Cloud Python SDK. The installation commands are as follows: If you use Python 2.x, run the following command to install the Alibaba Cloud SDK core library.

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the Alibaba Cloud SDK core library.

```
pip3 install aliyun-python-sdk-core-v3
```

**Use the Python SDK**

To call the Python SDK, follow these three steps:
1. Create a Client instance. To create the instance, you must specify the Region ID, AccessKey
ID, and AccessKey Secret.
2. Create an API request and set the parameters.
3. Initiate the request and handle the response or exceptions.
The following sample code shows how to call the EFS-NAS DescribeFileSystems operation to retrieve file system information:

> **Note:** REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET represent the region ID, your account's AccessKey ID, and your account's AccessKey secret. You must set these as environment variables.
> Replace the placeholders in the sample code with your actual values. Do not include the angle brackets (<>) in your code. The placeholders are:
> Replace <efs-nas.aliyuns.com> with the actual product endpoint.
> Replace <http://192.168.XX:33XX> with the actual proxy IP address and port.

s

```java
import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest def main():
    # To use a proxy, use the following code:
    #os.environ['http_proxy'] = "<http://192.168.XX:33XX>"
    # Configure the AccessKey and region ID as environment variables before initializ
ation.
    client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                       os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
                       os.environ['REGION_ID'])
    # Create a request object.
    request = CommonRequest()
    request.set_domain('<efs-nas.aliyuns.com>')  # The API endpoint. This is an examp
le. Replace it with the actual product endpoint.
    request.set_version('2017-06-26')  # The API version number.
    request.set_action_name('DescribeFileSystems')  # The API name. You must call set
_action_name() to specify the operation name when you call an RPC API.
    request.set_method('POST')  # The API request method.
    request.set_protocol_type('HTTPS')  # The request protocol, HTTPS or HTTP. Use HT
TPS.
    request.add_query_param('PageNum', '1')
    request.add_query_param('PageSize', '30')
    # Initiate the request and handle the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    main()
```

### 3.2 User guide

#### 3.2.1 Install the Python SDK

This topic describes how to install and call the EFS-NAS Python SDK.

**Background information**

The Apsara Stack Python SDK supports Python 2.6.x, 2.7.x, and 3.x or later. You can install the SDK using pip.

**Install the Python SDK**

To use the file storage feature, you must install the core library for the Alibaba Cloud Python SDK. The installation commands are as follows: If you use Python 2.x, run the following command to install the Alibaba Cloud SDK core library.

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the Alibaba Cloud SDK core library. s

```
pip3 install aliyun-python-sdk-core-v3
```

#### 3.2.2 Set identity verification credentials

Before using the Apsara Stack SDK to call services, you must configure authentication credentials. This topic describes the supported methods.

**Configure access credentials**

After you obtain an AccessKey and a region ID, choose one of the following methods to set them as environment variables based on your platform.

**Windows**

You can use either CMD or PowerShell to set the environment variables.

**CMD**

1. Run the following commands in CMD to set the environment variables.

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. Restart CMD. Then, run the following commands to check whether the environment
variables are set.

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. Run the following commands in PowerShell.

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. Run the following commands to check whether the environment variables are set.

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

1. Run the following commands in the command-line interface (CLI) to append the
environment variable settings to the ~/.bashrc file. s

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```

2. Run the following command to apply the changes.

```
source ~/.bashrc
```

3. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. Run the following command in the terminal to check the default shell type.

```
echo $SHELL
```

2. Follow the steps for your default shell type.
Zsh a. Run the following commands to append the environment variable settings to the ~/.zshrc file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshr
```

`c` b. Run the following command to apply the changes.

```
source ~/.zshrc
```

c. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash a. Run the following commands to append the environment variable settings to the ~/.bash_profile file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash _profile
```

b. Run the following command to apply the changes.

```
source ~/.bash_profile
```

s c. Run the following commands to check whether the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**Initialize the client**

The Python SDK supports identity verification using an AccessKey. When you use an AccessKey as your access credential, you must set the credential during client initialization.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                   os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
                   os.environ['REGION_ID'])
```

#### 3.2.3 Set HTTPS requests

The Python SDK supports API requests using the HTTP and HTTPS protocols. The Python SDK lets you specify the HTTP or HTTPS protocol for a single request. You can also set a global default protocol.

> **Note:** The default protocol set for a product takes precedence over the global default protocol.

**Add the OpenSSL dependency**

The Python SDK requires OpenSSL support in your Python environment to send HTTPS requests. OpenSSL must support Transport Layer Security (TLS) 1.2 or later.

| python -c "import ssl" |   | to check if your Python environm |
|---|---|---|
| mand runs without the |   |   |

supported. If OpenSSL is not installed, run the following command to install it:

```
pip install pyopenssl # Use this command for Python 2.
```

> **Note:** If you are using Python 3, run the `pip3 install pyopenssl` command.

**Set the HTTP/HTTPS protocol for a single request**

Use the following code to set HTTPS for a single request:

```java
import DescribeInstancesRequest request = DescribeInstancesRequest() request.set_protocol_type("https")
# Valid values: "https" or "http"
```

s

**Set the global default protocol**

Use the following code to set the global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 3.2.4 Make a call

If an SDK is not available for an API that you want to call, or if the request parameters and response values in the provided SDK do not meet your requirements, you can use the generic API call method (CommonRequest). The CommonRequest method lets you call any OpenAPI operation.

**About CommonRequest**

CommonRequest has the following features: Lightweight: You can make calls using only the Core package. You do not need to download and install the SDK for each product. Simple: You can call the latest published APIs without updating the SDK. Fast iteration. To make a CommonRequest, you must obtain the values for the following parameters. You can find these values in the EFS-NAS API documentation. Domain (domain): The endpoint of the product. API version (version): The version number of the API. The format is YYYY-MM-DD. You can find the API version in the common parameters section of the API documentation for each product. API operation: The name of the API operation that you want to call. Obtain the `Action` parameter. Use `request.set_action_name("<Action>")` to specify the API name.

| For example, for the |   |   | DescribeFileSystems | API op |
|---|---|---|---|---|
| request.set action name('DescribeFileSystems') _ _ |   |   |   |   |
| a | CommonRequest | . |   |   |

**Create a CommonRequest**

Use the CommonRequest method to call any OpenAPI operation.

```bash
request = CommonRequest() request.set_domain('<efs-nas.aliyuns.com>') # The endpoint of the API. This is an exam ple. Replace it with the actual endpoint of your product. request.set_version('2017-06-26') # The API version number. request.set_action_name('DescribeFileSystems') # The API name. When you call an RPC-st yle API, you must configure set_action_name() to specify the API name. request.set_method('POST') # The API request method. request.set_protocol_type('HTTPS') # The request protocol, HTTPS or HTTP. Use HTTPS.
# Set the business parameters for the API operation.
request.add_query_param('PageNum', '1') request.add_query_param('PageSize', '30')
```

s

> **Note:** In the preceding code sample, `<efs-nas.aliyuns.com>` is a variable. Replace it with the actual value for your service. Do not include the angle brackets (<>) in the final code.

**Make a call and process the response**

The following code shows how to make a request and process the response.

```python
# Make the request and get the response.
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
```

**Complete example**

The following code provides an example of how to call the EFS-NAS `DescribeFileSystems` API operation to query a list of file systems.

```java
import os from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest def main():
    # To use a proxy, use the following code:
    #os.environ['http_proxy'] = "<http://192.168.XX:33XX>"
    # Configure the AccessKey and region ID as environment variables before initializat
ion.
    client = AcsClient(os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
                       os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
                       os.environ['REGION_ID'])
    # Create a request object.
    request = CommonRequest()
    request.set_domain('<efs-nas.aliyuns.com>')  # The endpoint of the API. This is an
example. Replace it with the actual endpoint of your product.
    request.set_version('2017-06-26')  # The API version number.
    request.set_action_name('DescribeFileSystems')  # The API name. When you call an RP
C-style API, you must configure set_action_name() to specify the API name.
    request.set_method('POST')  # The API request method.
    request.set_protocol_type('HTTPS')  # The request protocol, HTTPS or HTTP. Use HTTP
```

`S.`

```python
    request.add_query_param('PageNum', '1')
    request.add_query_param('PageSize', '30')
    # Make the request and process the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    main()
```

s

> **Note:** REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET represent your region ID, AccessKey ID, and AccessKey secret. You must set them as environment variables.
> Replace all variables in the code sample with your actual information. Do not include the angle brackets (<>) in the final code. The variables that need to be replaced are as follows:
> <efs-nas.aliyuns.com>: Replace this with the actual endpoint of your product.
> <http://192.168.XX:33XX>: Replace this with the actual proxy IP address and port.

#### 3.2.5 Error handling

The Python SDK throws an exception when a server or SDK error occurs. This exception contains an error code and an error message. You do not typically need to handle errors from the Python SDK. Instead, you can handle server errors based on the messages that the server returns. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message.

```
aliyunsdkcore.acs_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle SDK errors, use the following code example:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own error handling logic here.
    # For example, print the specific error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

## 4 Go SDK call examples

### 4.1 Getting started

The Alibaba Cloud Go SDK lets you access cloud products without complex programming. This topic describes how to obtain the Alibaba Cloud EFS-NAS Go SDK and start making calls.

**Prerequisites**

Obtain an AccessKey or an STS AccessKey. Obtain the file storage endpoint.

**Install the Alibaba Cloud Go SDK core package**

The Alibaba Cloud Go SDK supports Go 1.10.x and later. Run the following command to install the Go SDK core package.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use the Go SDK**

Follow these steps to use the Go SDK:
1. Initialize a Client instance.
2. Create an API request and set its parameters.
3. Send the request and handle the response or exceptions.
The following sample code shows how to use the DescribeFileSystems operation of EFS-NAS to retrieve file system information:

> **Note:** REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET represent the region ID, your AccessKey ID, and your AccessKey secret. Set them as environment variables.
> In the sample code, <efs-nas.aliyuns.com> is a placeholder. Replace it with your actual product endpoint. Do not include the angle brackets (<>).

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    // Set the AccessKey and region ID as environment variables before
initialization.
    credential := credentials.NewStsTokenCredential(
```

```
        // Get the AccessKey ID and AccessKey secret from the environment variables.
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
        // If you use an STS AccessKey for identity verification, set the
SecurityToken of your account to the ALIBABA_CLOUD_STS_SECURITY_TOKEN environment var iable.
        // If you use an AccessKey for identity verification, set SecurityToken to ""
```

`.`

```
        "",
```

`)`

```
    client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(),
credential)
    if err != nil {
        panic(err)
    // Create a request.
    request := requests.NewCommonRequest()
    request.Method = "POST"  // The method of the API request.
    request.Domain = "<efs-nas.aliyuns.com>" // The endpoint of the API. This is an e
xample. Replace it with your actual product endpoint.
    request.Product = "efs-nas"  // The product name.
    request.Version = "2017-06-26"  // The API version number.
    request.ApiName = "DescribeFileSystems"  // The API name.
    // Configure the business parameters of the operation.
    request.QueryParams["PageSize"] = "20"
    request.QueryParams["PageNumber"] = "1"
    // Optional headers. These are usually not required unless your enterprise has sp
ecific organization or resource group requirements.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Set this to be consistent
with the client.
    // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional
```

`.`

```
    // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"   // Required
to isolate resources by organization.
    // Send the request.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    // Print the response.
    fmt.Println(response.GetHttpContentString())
```

### 4.2 User guide

#### 4.2.1 Install the Go SDK

This document describes how to install the Go SDK core package. The Alibaba Cloud Go SDK supports Go 1.10.x and later. After running the `go mod init` `<DIRNAME>` command in your project folder to generate a go.mod file, run the following command to install the Go SDK core package.

**Note**

| <DIRNAME> | specifies the path to your project folder. Replace it with the actual path. |
|---|---|

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

If a network error occurs, you can use one of the following methods to download the package. Use the official download method.

```
GOPROXY=https://goproxy.cn,direct go get -u github.com/aliyun/alibaba-cloud-sdk-go/s
```

`dk` Download using a proxy server.

```
go env -W GOPROXY='https://goproxy.cn,direct'
```

#### 4.2.2 Set identity verification credentials

Before using the Apsara Stack SDK to call services, you must configure authentication credentials. This topic describes the supported methods.

**Configure access credentials**

After you obtain an AccessKey or a Security Token Service (STS) temporary credential and a region ID, configure them as environment variables. This section uses an AccessKey as an example. The configuration process for an STS temporary credential is similar. Configure the variables on your platform.

**Windows**

Configure the environment variables in either Command Prompt (CMD) or PowerShell.

**CMD**

1. Run the following commands in CMD to set the environment variables.

```
setx REGION_ID "YOUR_REGION_ID" setx ALIBABA_CLOUD_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx ALIBABA_CLOUD_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
```

2. Restart CMD. Then, run the following commands to verify that the environment variables
are set.

```
echo %REGION_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_ID% echo %ALIBABA_CLOUD_ACCESS_KEY_SECRET%
```

**PowerShell**

1. Run the following commands in PowerShell to set the environment variables.

```
[Environment]::SetEnvironmentVariable("REGION_ID", "YOUR_REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

2. Run the following commands to verify that the environment variables are set.

```
[Environment]::GetEnvironmentVariable("REGION_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("ALIBABA_CLOUD_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
```

**Linux**

1. Run the following commands in the command-line interface (CLI) to append the
environment variable settings to the ~/.bashrc file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
```

2. Run the following command to apply the changes.

```
source ~/.bashrc
```

3. Run the following commands to verify that the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**macOS**

1. Run the following command in the terminal to determine your default shell type.

```
echo $SHELL
```

2. Follow the steps for your default shell type.
Zsh a. Run the following commands to append the environment variable settings to the ~/.zshrc file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshr
```

`c` b. Run the following command to apply the changes.

```
source ~/.zshrc
```

c. Run the following commands to verify

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

Bash a. Run the following command to append the environment variable configuration to the ~/.bash_profile file.

```
echo "export REGION_ID='YOUR_REGION_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export ALIBABA_CLOUD_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash _profile
```

b. Run the following command for the changes to take effect.

```
source ~/.bash_profile
```

c. Run the following command to verify that the environment variables are set.

```
echo $REGION_ID echo $ALIBABA_CLOUD_ACCESS_KEY_ID echo $ALIBABA_CLOUD_ACCESS_KEY_SECRET
```

**Initialize the client**

The Go SDK uses an AccessKey or an STS AccessKey for identity verification.

```
credential := credentials.NewStsTokenCredential(
        // Obtain the AccessKey ID and AccessKey secret from the environment variables.
    os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
    os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
    // To use an STS AccessKey for identity verification, configure the SecurityToken o
f the account to the ALIBABA_CLOUD_STS_SECURITY_TOKEN environment variable.
    // To use an AccessKey for identity verification, set SecurityToken to "".
    os.Getenv("ALIBABA_CLOUD_STS_SECURITY_TOKEN"),
```

`)`

```
client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), creden tial) if err != nil {
    panic(err)
```

#### 4.2.3 Request connection configuration

This topic describes how to configure request connection settings (HttpClientConfig). Use the following code to configure HttpClientConfig. Select and set the configuration items based on your requirements.

```
client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), creden tial) if err != nil {
    panic(err)
// Specifies whether to ignore the certificate. `true` ignores the certificate. `false` does not. client.SetHTTPSInsecure(true) // (Optional) Sets the connection timeout in nanoseconds. Formula: X seconds × time.Sec ond = X × 1,000,000,000 nanoseconds. client.SetConnectTimeout(1 * time.Second) // (Optional) Sets the read timeout in nanoseconds. Formula: X seconds × time.Second = X × 1,000,000,000 nanoseconds. client.SetReadTimeout(10 * time.Second) /** (Optional) Set a proxy as needed. Replace the placeholder with your actual proxy IP address and port. client.SetHttpProxy("<http://192.168.XX.XX:33XX>") client.SetHttpsProxy("<https://192.168.XX.XX:33XX>")
```

`*/`

**Note**

|   | <connectionTimeout> |
|---|---|
| <http://192.168.XX.XX:33XX> |   |

> values and remove the angle brackets (<>).

#### 4.2.4 Make a call

If an API does not have a software development kit (SDK), or if the request parameters and response values in a provided SDK do not meet your needs, you can use the generic API call method (CommonRequest). The CommonRequest method lets you call any OpenAPI operation.

**Introduction to CommonRequest**

CommonRequest has the following features: Lightweight: You can make calls using only the core package. You do not need to download and install an SDK for each product. Simple: You can call the latest APIs without updating the SDK. Fast iteration. To make a CommonRequest, you must obtain the values for the following parameters. You can find these values in the EFS-NAS API documentation. Domain: The endpoint of the product. API version: The version number of the API in YYYY-MM-DD format. You can find the API version in the common parameters section of the API documentation for each product. API operation information: The name of the API operation to call. Obtain the `Action` parameter. Use `request.ApiName = "<Action>"` to specify the API name.

| DescribeFileSystems |   | operation, set the API nam |
|---|---|---|
| using |   |   |

**Create a CommonRequest**

You can use the CommonRequest method to call any OpenAPI operation.

```
request := requests.NewCommonRequest() request.Method = "POST" request.Domain = "<efs-nas.aliyuns.com>" // The endpoint of the EFS-NAS service. request.Product = "efs-nas" // The product name. request.Version = "2017-06-26" // The API version. request.ApiName = "DescribeFileSystems" // The API name. // Configure the business parameters of the API operation. request.QueryParams["PageSize"] = "20" request.QueryParams["PageNumber"] = "1" // Optional header. This is usually not required unless your enterprise has organizatio n or resource group requirements. request.Headers["x-acs-regionid"] = "<yourRegionID>" // Set this to the same value as t he client. // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required to im plement fencing by organization.
```

> **Note:** In the preceding code sample, `<efs-nas.aliyuns.com>` is a variable. Replace it with the actual endpoint for your service. Do not include the angle brackets (<>) in your final code.

**Make the call and process the response**

Use the following code to make the request and process the response.

```
response, err := client.ProcessCommonRequest(request) if err != nil {
    panic(err)
fmt.Println(response.GetHttpContentString())
```

**Complete example**

The following code provides an example of how to call the `DescribeFileSystems` operation for EFS-NAS to query a list of file systems.

```java
package main import (
 "fmt"
 "os"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
```

```
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/auth/credentials"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

```
func main() {
    // Configure the AccessKey and region ID as environment variables before initializa
tion.
    credential := credentials.NewStsTokenCredential(
        // Get the AccessKey ID and AccessKey secret from the environment variables.
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"),
        os.Getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"),
        // To use an STS AccessKey for identity verification, set the
ALIBABA_CLOUD_STS_SECURITY_TOKEN environment variable to your SecurityToken.
        // To use an AccessKey for identity verification, set SecurityToken to "".
        "",
```

`)`

```
    client, err := sdk.NewClientWithOptions(os.Getenv("REGION_ID"), sdk.NewConfig(), cr
edential)
    if err != nil {
        panic(err)
    // Create a request.
    request := requests.NewCommonRequest()
    request.Method = "POST"  // The request method of the API.
    request.Domain = "<efs-nas.aliyuns.com>" // The API endpoint. This is a sample valu
e. Replace it with the actual endpoint of your product.
    request.Product = "efs-nas"  // The product name.
    request.Version = "2017-06-26"  // The API version number.
    request.ApiName = "DescribeFileSystems"  // The API name.
    // Configure the business parameters of the API operation.
    request.QueryParams["PageSize"] = "20"
    request.QueryParams["PageNumber"] = "1"
    // Optional header. This is usually not required unless your enterprise has organiz
ation or resource group requirements.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Set this to the same value
as the client.
    // request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional.
    // request.Headers["x-acs-organizationid"] = "<yourOrganizationID>"   // Required t
o implement fencing by organization.
    // Send the request.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    // Print the response.
    fmt.Println(response.GetHttpContentString())
```

> **Note:** Set the REGION_ID, ALIBABA_CLOUD_ACCESS_KEY_ID, and ALIBABA_CLOUD_ACCESS_KEY_SECRET environment variables. These variables represent the region ID, your AccessKey ID, and your AccessKey secret.
> In the code sample, <efs-nas.aliyuns.com> is a variable. Replace it with the actual endpoint for your product. Do not include the angle brackets (<>) in your final code.

#### 4.2.5 Error handling

When an error occurs on the server or in the Alibaba Cloud Go SDK, the SDK returns a `ClientError` or `ServerError` message from the `sdk.errors` package. These errors are based on Go's standard `Error` interface. You can handle errors from the Alibaba Cloud Go SDK in the same way that you handle standard Go errors.

**Handle a simple error**

Use the following code to handle a simple error.

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Get the error message.
   err.Error()
```

**ClientError**

The SDK returns a `ClientError` when an internal call fails and cannot be handled automatically. Use the following code to identify a `ClientError` and retrieve its error message.

| Important To use a specific error structure, import the github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors package. The following code shows an example. package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // The new error package. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |   |   |
|---|---|---|
|   | github.com/aliyun/alibaba-cloud-sdk- |   |

```
response, err := client.ProcessCommonRequest(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Get the error code.
    clientError.ErrorCode()
    // Get the error description.
    clientError.Message()
    // Get the original error. This may be nil.
    clientError.OriginError()
```

**ServerError**

When the server returns an error response, the SDK encapsulates it into a `ServerError`. You can still retrieve the original HTTP response from the `Response` object. Use the following code to identify the `ServerError` and retrieve error information from both the `ServerError` and the `Response`.

| Important To use a specific error structure, import the github.com/aliyun/alibaba-cloud-sdk- go/sdk/errors package. The following code shows an example. package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" // The new error package. "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors" "fmt" ) |   |   |
|---|---|---|
|   | github.com/aliyun/alibaba-cloud-sdk- |   |

```
response, err := client.ProcessCommonRequest(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Get the error code.
    serverError.ErrorCode()
    // Get the error description.
    serverError.Message()
    // Get the original HTTP response.
    response.GetOriginHttpResponse()
```

## 5 API reference

### 5.1 Call APIs

#### 5.1.1 Overview

An API call is an HTTP GET request sent to a product's service endpoint. The request must include the required parameters as specified in the API reference. The service processes the request and returns a response. Both the request and the response are encoded in the UTF-8 character set.

#### 5.1.2 Request structure

**Endpoint**

For more information about product endpoints, see Obtain the endpoint for file storage.

**Request method**

The service supports the HTTP GET method. For GET requests, the parameters must be included in the request URL.

**Communication protocol**

You can send requests over HTTP or HTTPS channels. For greater security, use the HTTPS channel. Each request must specify an operation to execute using the Action parameter, such as CreateFileSystem. Each request must also include common request parameters and parameters that are specific to the specified operation.

**Character encoding**

Requests and responses are encoded using the UTF-8 character set.

#### 5.1.3 Return results

API calls return data in a standard format. An HTTP status code in the 2xx range indicates a successful call. A status code in the 4xx or 5xx range indicates a failed call. For successful calls, data is returned in JSON format only.

> **Note:** The response examples in this document are formatted for readability. The actual response does not include line breaks or indentation.

**Successful results**

```json
    "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
    /* Response data */
```

**Error results**

If an API call fails, no result data is returned. You can use the error code returned by the API to find the cause of the failure. A failed call returns an HTTP status code in the 4xx or 5xx range. The response body contains the specific error code and error message. The body also includes a globally unique request ID (RequestId) and the ID of the accessed site (HostId).

```json
    "RequestId": "8906582E-6722-409A-A6C4-0E7863B733A5",
    "HostId": "efs-nas.example.com",
    "Code": "InvalidOwnerId",
    "Message": "The specified OwnerId is not valid."
```

### 5.2 RAM authentication

When a Resource Access Management (RAM) user accesses resources of an Alibaba Cloud account using OpenAPI, the system uses RAM to check permissions. This check ensures that the resource owner has granted the caller the required permissions to access the resources.

**Background information**

By default, an Alibaba Cloud account or a RAM user can use the EFS-NAS console or call the EFS-NAS API to manage the resources that they create. However, authorization issues can occur in the following scenarios: A newly created RAM user does not have permissions to manage resources that belong to the Alibaba Cloud account. An Alibaba Cloud service needs to access EFS-NAS resources, or EFS-NAS needs to access another Alibaba Cloud service. To manage EFS-NAS resources that are protected by access control, the resource owner must grant permissions for the target resources and API operations. When a user from another account calls the EFS-NAS API to access resources that belong to an Alibaba Cloud account, EFS-NAS uses RAM to check permissions. This check verifies that the resource owner has granted the required permissions to the caller. Each EFS-NAS API determines which resource permissions to check based on the resources and API semantics involved.

**Rule details**

Each EFS-NAS API determines which resource permissions to check based on the resources and API semantics involved.

### 5.3 Common parameters

Common parameters include request parameters, header parameters, and response parameters.

**Common request parameters**

Common request parameters are parameters required for every API call.

| Name | Type | Requir ed | Description |
|---|---|---|---|

| Format | String | No | The format of the return value. Only JSON is supported. |
|---|---|---|---|
| Version | String | Yes | The API version number. Enter the value in the YYYY- MM-DD format. The value is 2017-06-26. |
| AccessKeyId | String | Yes | The ID of the AccessKey used to access the service. |
| AccessKeySecre t | String | Yes | The secret of the AccessKey used to access the service. |
| RegionId | String | Yes | The ID of the region where the service is accessed. |
| Product | String | Yes | The name of the product that corresponds to the API. The product name is efs-nas. |

**Common header parameters**

For more information, see Obtain common header parameters.

| Name | Description |
|---|---|
| x-acs-regionid | The region ID of the instance resource that you operate on. |
| x-acs-organizationid | The organization ID of the instance resource that you operate on. |
| x-acs-resourcegroupid | The resource group ID of the instance resource that you operate on. |
| x-acs-instanceid | The instance ID of the instance resource that you operate on. |

| Note When you call the APIs of Apsara Uni-manager Management Console, you can omit the x-acs-organizationid , x-acs-resourcegroupid , and x-acs-instanceid header parameters. When you call the APIs of other cloud products, add the organization ID <x-acs- organizationid> to the header parameters. Otherwise, an exception is returned indicating that you do not have the required permissions. When you call the APIs of other cloud products, you can add the resource group ID <x-acs-resourcegroupid> to the header parameters. This lets you specify the organization and resource group of a resource to perform isolated queries. If you do not specify the resource group ID <x-acs-resourcegroupid> , the default resource group of your organization is used. |   |   |
|---|---|---|
|   | <x-acs- |   |

**Common response parameters**

API responses use a unified format. The status of a call is indicated by the returned HTTP status code. An HTTP status code in the 2xx range indicates that the call is successful. An HTTP status code in the 4xx or 5xx range indicates that the call failed. If a call is successful, the response is returned in JSON format. A unique RequestId is returned for each API call, regardless of whether the call is successful.

### 5.4 Region

#### 5.4.1 DescribeZones

Queries the zones that support a specified file system type in a region.

**Request header**

This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsType | Strin g | Query | No | Performance | The type of the file system. Valid values: Performance: a compute-optimized instance that uses all- flash media. Capacity: a storage- optimized instance that uses hybrid flash media. If you do not specify this parameter, the zones that support all file system types are returned. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Zones | Array | [{}] | A list of zone information. |
| -ZoneId | String | cn-hangzhou-** | The ID of the zone. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeZones &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Zones":[
   "ZoneId":"cn-hangzhou-**"
```

`]`

### 5.5 File system

#### 5.5.1 CreateFileSystem

Creates a file system. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| FsName | Strin g | Query | Yes | myfs | The name of the file system. |
| Capacity | Long | Query | Yes | 1024 | The capacity of the file system in GiB. Valid values: 1 to 5242880. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsType | Strin g | Query | Yes | Capacity | The type of the file system. Valid values: Performance: a compute-optimized file system that uses all-flash media. Capacity: a storage- optimized file system that uses hybrid flash media. |
| ZoneId | Strin g | Query | No | cn-hangzhou-** | The ID of the zone. |
| Descriptio n | Strin g | Query | No | For testing | The description of the file system. |
| NfsVersio n | Strin g | Query | No | v3,v4 | The version of the NFS protocol. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| FsId | String | efs-nas-0***** | The ID of the file system. |

Request example

```
http(s)://[Endpoint]/?Action=CreateFileSystem &FsName=myfs &Capacity=1024 &FsType=Capacity &<Common request parameters>
```

Successful response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "FsId":"efs-nas-0*****"
```

#### 5.5.2 DescribeFileSystems

This operation queries a list of file systems and supports paged queries.

**Request header**

This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. This parameter is not in use. |
| FsId | Strin g | Query | No | efs-nas-0***** | The file system ID. |
| ZoneId | Strin g | Query | No | cn-hangzhou-** | The zone ID. This parameter is not in use. |
| Status | Strin g | Query | No | RUNNING | The status of the file system. Valid values: INITIAL (initializing), RUNNING (running), MODIFYING (modifying), and DELETING (deleting). |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. Default value: 20. |
| PageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |

**Response data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| FileSystems | Array | [{}] | A list of file systems. |
| -ZoneId | String | cn-hangzhou-** | The zone ID. |
| -RegionId | String | cn-hangzhou | The region ID. |

| lastic File System Guide·API refere | NAS Develope nce |   |   |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| -ClusterId | String | c****** | The cluster ID. |
| -FsId | String | efs-nas-0***** | The file system ID. |
| -FsName | String | myfs | The name of the file system. |
| -UserId | String | 15577******8921 | The user ID. |
| -FsType | String | Performance | The type of the file system. Valid values: Performance (all-flash) and Capacity (hybrid flash). |
| -Capacity | Long | 100 | The total capacity. Unit: GiB. |
| -Status | String | Running | The status of the file system. Valid values: INITIAL (initializing), RUNNING (running), MODIFYING (modifying), and DELETING (deleting). |
| -Description | String | For testing | The description of the file system. |
| - CreateRequest Id | String | F0A8B189-930D- 5EC1-97C8- ************ | The ID of the request to create the file system. |
| -CreateTime | String | 2025-10- 15T05:55:20Z | The time when the file system was created. |
| -ModifyTime | String | 2025-10- 16T09:55:41Z | The time when the file system was last modified. |
| -UsedCapacity | Long | 1024 | The used capacity. Unit: bytes. |
| -NfsVersion | String | v3,v4 | The version of the NFS protocol that is used. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Long | 5 | The total number of file systems found. |

|   |   |   | Elastic File System NAS Develop |
|---|---|---|---|

| Parameter name | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 10 | The number of resources on each page. |
| PageNum | Integer | 1 | The page number. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeFileSystems &Common request parameters
```

Successful response example

```json
 "FileSystems":[
   "Status":"Running",
   "ModifyTime":"2025-10-16T09:55:41Z",
   "Description":"For testing",
   "ZoneId":"cn-hangzhou-**",
   "NfsVersion":"v3,v4",
   "ClusterId":"c******",
   "CreateTime":"2025-10-15T05:55:20Z",
   "FsType":"Performance",
   "FsId":"efs-nas-0*****",
   "UsedCapacity":1024,
   "FsName":"myfs",
   "Capacity":100,
   "CreateRequestId":"F0A8B189-930D-5EC1-97C8-************",
   "UserId":"15577******8921",
   "RegionId":"cn-hangzhou"
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageSize":10,
 "PageNum":1
```

#### 5.5.3 ModifyFileSystem

Modifies the properties of a file system, such as its capacity and description. This operation uses common request headers and does not require special request headers. For more information, see the Common request parameters document.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c**** | The ID of the cluster. |
| FsId | Strin g | Query | Yes | efs-nas-0***** | The ID of the file system. |
| Capacity | Long | Query | No | 100 | The capacity of the file system. Unit: GiB. The value must be an integer from 1 to 5242880. The new capacity cannot be smaller than the current capacity or larger than the remaining quota. |
| Descriptio n | Strin g | Query | No | For testing | The description of the file system. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Sample request

```
http(s)://[Endpoint]/?Action=ModifyFileSystem &FileSystemId=efs-nas-0***** &<Common request parameters>
```

Sample response The response is returned in `JSON` format.

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.5.4 DeleteFileSystem

Deletes a file system.

**Notes**

Deleted file systems cannot be recovered. Proceed with caution. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| FsId | Strin g | Query | Yes | efs-nas-8***** | The ID of the file system. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteFileSystem &FsId=efs-nas-8***** &Common request parameters
```

Successful response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

### 5.6 User

#### 5.6.1 CreateFsUser

Creates a file system user. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | Yes | myuser | The username of the file system user. |
| Password | Strin g | Query | Yes | ab****** | The password of the file system user. The password must be 8 characters long and contain uppercase letters, lowercase letters, special characters, and digits. |
| Uid | Long | Query | Yes | 10000 | The user ID. |
| PrimaryGr oupId | Long | Query | No | 10000 | The ID of the primary user group. If you do not specify this parameter, it is left empty. |
| UserGrou pIds | Strin g | Query | No | [10001,10002] | The IDs of the secondary user groups. If you do not specify this parameter, the list is empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| FsUserId | Long | 100000 | The ID of the file system user. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateFsUser &Name=myuser &Password=ab****** &Uid=10000 &<Common request parameters>
```

Sample response The response is in `JSON` format.

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "FsUserId":100000
```

#### 5.6.2 DescribeFsUsers

Queries the users of a file system. This operation supports paged queries and queries by file system user ID. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserId | Long | Query | No | 100000 | The ID of the file system user. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. Default value: 20. |
| PageNum | Integ er | Query | No | 1 | The page number. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| FsUsers | Array | [{}] | The list of file system users. |
| -FsUserId | Long | 100000 | The ID of the file system user. |
| -Uid | Long | 10000 | The user ID. |
| -Name | String | myuser | The username of the file system user. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - PrimaryGroupI d | Long | 10000 | The ID of the primary user group. |
| - SecondaryGro upIds | String | [10001,10002] | The list of secondary user group IDs. |
| -CreateTime | String | 2025-10- 15T09:55:41Z | The time when the file system user was created. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of file system users. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| TotalCount | Integer | 5 | The total number of file system users. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeFsUsers &<Common request parameters>
```

Response example

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "FsUsers":[
   "Uid":10000,
   "CreateTime":"2025-10-15T09:55:41Z",
   "FsUserId":100000,
   "PrimaryGroupId":10000,
   "Name":"myuser",
   "SecondaryGroupIds":"[10001,10002]"
```

`]`

#### 5.6.3 ModifyFsUser

Modifies a file system user. This operation uses only common request headers. For more information, see Common parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserId | Long | Query | Yes | 100000 | The ID of the file system user. |
| Password | Strin g | Query | No | bc****** | The password of the file system user. The password must be 8 characters long and contain uppercase letters, lowercase letters, special characters, and digits. |
| PrimaryGr oupId | Long | Query | No | 10000 | The ID of the primary user group. If you do not specify this parameter, the primary user group of the user is set to empty. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| UserGrou pIds | Strin g | Query | No | [10001,10002] | The list of secondary user group IDs. If you do not specify this parameter, the secondary user groups of the user are set to empty. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| FsUserId | Long | 100000 | The ID of the file system user. |
| Name | String | myuser | The username. |
| Uid | Long | 10000 | The user ID. |

Sample request

```
http(s)://[Endpoint]/?Action=ModifyFsUser &FsUserId=100000 &<Common request parameters>
```

Sample response

```json
 "Uid":1000000000000000,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "FsUserId":100000,
 "Name":"myuser"
```

#### 5.6.4 DeleteFsUser

Deletes a file system user.

**Notes**

A file system user cannot be recovered after it is deleted. Proceed with caution. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserId | Long | Query | Yes | 100000 | The ID of the file system user. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates success. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteFsUser &FsUserId=100000 &<Common request parameters>
```

Successful response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

### 5.7 User group

#### 5.7.1 CreateFsUserGroup

Creates a file system user group. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter name | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Name | Strin g | Query | Yes | myusergroup | The name of the user group. |
| GroupId | Long | Query | Yes | 10000 | The ID of the user group. |
| FsUserIds | Strin g | Query | Yes | [100000,100001] | A list of up to 100 file system user IDs. |

**Response data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| FsUserGroupId | Long | 10000 | The ID of the file system user group. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateFsUserGroup &Name=myusergroup &GroupId=10000 &FsUserIds=[100000,100001] &<Common request parameters>
```

Sample success response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "FsUserGroupId":10000
```

#### 5.7.2 AddFsUsersToGroup

Adds file system users to a specified user group. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter name | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserGro upId | Long | Query | Yes | 10000 | The ID of the file system user group. |
| FsUserIds | Strin g | Query | Yes | [100000,100001] | A list of file system user IDs. You can specify up to 100 IDs. |

**Response data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation succeeded. |

Sample request

```
http(s)://[Endpoint]/?Action=AddFsUsersToGroup &FsUserGroupId=10000 &FsUserIds=[100000,100001] &<Common request parameters>
```

Sample successful response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

#### 5.7.3 RemoveFsUsersFromGroup

Removes file system users from a specified user group. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserGro upId | Long | Query | Yes | 10000 | The ID of the user group. |
| FsUserIds | Strin g | Query | Yes | [100000,100001] | A list of file system user IDs. You can specify up to 100 user IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true is returned if the operation is successful. |

Request example

```
http(s)://[Endpoint]/?Action=RemoveFsUsersFromGroup &FsUserGroupId=10000 &FsUserIds=[100000,100001] &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

#### 5.7.4 DescribeFsUserGroups

Queries a list of file system user groups. This operation supports paged queries and lets you query by file system user group ID. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserGro upId | Long | Query | No | 10000 | The ID of the file system user group. Use this parameter to query the details of a specific user group. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page for a paged query. The default value is 20. |
| PageNum | Integ er | Query | No | 1 | The page number for a paged query. The default value is 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| FsUserGroups | Array | [{}] | A list of file system user groups. |
| - FsUserGroupId | Long | 10000 | The ID of the file system user group. |
| -Gid | Long | 10000 | The group ID (GID). |
| -Name | String | myusergroup | The name of the user group. |
| -FsUserIds | String | [100000,100001] | A list of user IDs. |
| -CreateTime | String | 2025-10- 15T09:55:41Z | The time when the file system user group was created. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of file system user groups. |

| lastic File System | NAS Develope |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources per page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeFsUserGroups &<Common request parameters>
```

Sample response

```json
 "TotalCount":5,
 "FsUserGroups":[
   "FsUserIds":"[100000,100001]",
   "Gid":10000,
   "CreateTime":"2025-10-15T09:55:41Z",
   "FsUserGroupId":10000,
   "Name":"myusergroup"
```

`],`

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
```

#### 5.7.5 DeleteFsUserGroup

Deletes a file system user group. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FsUserGro upId | Long | Query | Yes | 10000 | The ID of the file system user group. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. A value of true indicates success. |

Sample request

```
http(s)://[Endpoint]/?Action=DeleteFsUserGroup &FsUserGroupId=10000 &<Common request parameters>
```

Sample success response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

### 5.8 SMB share

#### 5.8.1 CreateSmbShare

Creates an SMB share. This operation uses common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The ID of the file system. |
| ShareNam e | Strin g | Query | Yes | myshare | The name of the share. |

| lastic File Sy | stem NAS | Develope |   |   |   |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| MountTar getInfo | Strin g | Query | No | /efs-nas-73**** | Information about the mount target. Do not configure this parameter when you create a share. |
| CaseSensi tive | Boole an | Query | No | false | Specifies whether file and folder names are case-sensitive. true: Case-sensitive. false (default): Case- insensitive. |
| AbeEnabl ed | Boole an | Query | No | false | Specifies whether to enable Windows access- based enumeration (ABE). The default value is false. If you enable ABE, users can see only the files and folders that they have permission to access when they browse the shared directory. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Opportuni sticLockEn abled | Boole an | Query | No | false | Specifies whether to enable opportunistic locking. This feature is suitable for environments with more read operations than write operations and where users do not frequently share the same files. The default value is false. If you enable this feature, a client can exclusively access a shared file for a period of time. This reduces frequent access to the file server and network traffic. However, this may cause issues such as concurrent access conflicts. Configure and use this feature with caution. |
| ContactIp List | Strin g | Query | No | [192.168.10.1,192.168.1 0.2] | A list of IPv4 addresses that identify the devices or service nodes that can communicate. |
| VSwitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The ID of the virtual switch. |
| VpcId | Strin g | Query | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the VPC. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Acls | Strin g | Query | No | [{"AccessType":"local"," UserType":"user","Permi ssion":"RO","UserId":100 0000000000000,"userN ame":"JL-USER-02"}, {"AccessType":"local","U serType":"user","Permis sion":"RO","UserId":1000 000000000001,"userNa me":"JL-USER-01"}] | A list of access control policies in a JSON- formatted array. A single access control list (ACL) includes the following settings: `UserId` (Long, optional): The ID of the user. `GroupId` (Long, optional): The ID of the user group. `UserType` (String, required): The type of user. Valid values: `user`, `user group`, _ and `everyone`. `Permission` (String, required): The type of permission. Valid values: `RO` (read- only), `RW` (read- write), `forbid delete` _ (read-write but delete is forbidden), `full control`, and _ `forbid access`. _ When `UserType` is set to `everyone`, only `RW` and `RO` are supported. `AccessType` (String, optional): The type of access. Valid value: `local`. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| ShareId | String | 3e47da**** | The ID of the share. |

Request example

```json
http(s)://[Endpoint]/?Action=CreateSmbShare &FileSystemId=efs-nas-c***** &ShareName=myshare &Acls= [{"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000000,"use ame":"JL-USER-02"}, {"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000001,"user me":"JL-USER-01"}] &<Common request parameters>
```

Response example

```json
 "ShareId":"3e47da****",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.8.2 DescribeSmbConnections

Retrieves the details and total number of connections for a Server Message Block (SMB) share. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. The default value is 20. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SmbConnectio ns | Array | [{}] | A list of connections for the SMB share. |

| lastic File System | NAS Develope |   |   |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -ShareId | String | 3e47****** | The ID of the SMB share. |
| -ClientIp | String | 10.10.10.** | The client IP address. |
| -AccessUser | String | myusertest | The username. |
| - ProtocolVersio n | String | 3.0 | The protocol version. |
| -ConnectTime | String | 1500 | The duration of the connection between the client and the server. Unit: seconds. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of connections for the SMB share. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeSmbConnections &ShareId=3e47****** &<Common request parameters>
```

Sample response

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "SmbConnections":[
   "ShareId":"3e47******",
   "ProtocolVersion":"3.0",
   "ConnectTime":"1500",
   "ClientIp":"10.10.10.**",
   "AccessUser":"myusertest"
```

`]`

#### 5.8.3 DescribeSmbShares

Queries a list of Server Message Block (SMB) shares. This operation supports paged queries. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. |
| FileSyste mId | Strin g | Query | No | efs-nas-0***** | The file system ID. |
| ShareId | Strin g | Query | No | 3e47****** | The share ID. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page for a paged query. The default value is 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SmbShares | Array | [{}] | The list of SMB shares. |
| -ShareId | String | 3e47****** | The ID of the SMB share. |
| -ShareName | String | myshare | The name of the SMB share. |
| -FileSystemId | String | efs-nas-0***** | The ID of the file system to which the share belongs. |
| -Status | String | ACTIVE | The current status of the SMB share. Valid values: ACTIVE (running), PENDING (initializing or being modified), and DELETING (being deleted). |
| -CreateTime | String | 2025-10- 16T09:55:41Z | The time when the SMB share was created. |
| -VpcId | String | vpc- bp1gsk7h12ew7oe gk**** | The VPC ID. |
| -Azone | String | cn-hangzhou-** | The zone. |
| - MountTargetD omain | String | 04f314****- at***.cn- hangzhou.**.***.co m | The domain name of the mount target. |
| - MountTargetIn fo | String | /efs-nas-73**** | The information about the mount target. |
| -VswitchId | String | vsw- bp1e7clcw529l773 d**** | The virtual switch ID. |
| -CaseSensitive | Boolean | false | Indicates whether file and folder names are case-sensitive. |
| -AbeEnabled | Boolean | false | Indicates whether Windows access-based enumeration (ABE) is enabled. If ABE is enabled, users can only see the shared files and folders that they have permission to access when they browse the shared directory. They cannot see items that they do not have permission to access. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| - OpportunisticL ockEnabled | Boolean | false | Indicates whether opportunistic locking is enabled. If enabled, a client can have exclusive access to a shared file for a period of time. This reduces frequent access to the file server and network traffic. However, this may cause issues such as file access conflicts. Configure and use this feature with caution. |
| -ContactIpList | String | [192.168.10.1,192. 168.10.2] | A list of IPv4 addresses for communicable devices or service nodes. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of SMB shares. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeSmbShares &Common request parameters
```

Sample response

```json
 "SmbShares":[
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
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
```

#### 5.8.4 ModifySmbShare

Modifies the configuration of a Server Message Block (SMB) share. This operation has no special request headers. For more information about common request headers, see Common parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |
| ShareNam e | Strin g | Query | No | myshare | The name of the SMB share. |
| CaseSensi tive | Boole an | Query | No | false | Specifies whether file and folder names are case-sensitive. true: Case-sensitive. false (default): Case- insensitive. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AbeEnabl ed | Boole an | Query | No | false | Specifies whether to enable Windows access- based enumeration (ABE). The default value is false. When enabled, users who browse the shared folder can see only the files and folders that they have permission to access. |
| Opportuni sticLockEn abled | Boole an | Query | No | false | Specifies whether to enable opportunistic locking. This feature is suitable for environments with more reads than writes and where users do not frequently share the same files. The default value is false. When enabled, this feature lets clients exclusively access a shared file for a period. This reduces frequent access to the file server and network traffic. However, it may cause issues such as concurrent access conflicts. Configure and use this feature with caution. |
| ContactIp List | Strin g | Query | No | [192.168.10.1,192.168.1 0.2] | A list of contact IP addresses. These IPv4 addresses identify devices or service nodes that can communicate. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Request example

```
http(s)://[Endpoint]/?Action=ModifySmbShare &ShareId=3e47****** &ContactIpList=[192.168.10.1,192.168.10.2] &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.8.5 DeleteSmbShare

Deletes an SMB share.

**Notes**

Before you delete an SMB share, confirm that no services depend on it. Deleting a share makes its resources inaccessible to all users. An SMB share cannot be recovered after it is deleted. Proceed with caution. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |
| Force | Boole an | Query | No | false | Specifies whether to force delete the share. Default value: false. If the share has active connections or open files, the delete operation fails by default. Set this parameter to true to ignore active sessions and remove the share configuration. This action might break client connections. Use this parameter with caution. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteSmbShare &ShareId=3e47****** &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

### 5.9 SMB ACL

#### 5.9.1 BatchCreateSmbAcl

Creates multiple Server Message Block (SMB) access control lists. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Acls | Strin g | Query | Yes | [{"AccessType":"local"," UserType":"user","Permi ssion":"RO","UserId":100 0000000000000,"userN ame":"JL-USER-02"}, {"AccessType":"local","U serType":"user","Permis sion":"RO","UserId":1000 000000000001,"userNa me":"JL-USER-01"}] | A JSON array of access control policies. A single access control list (ACL) includes the following configurations: UserId (Long, Optional): The ID of the user. GroupId (Long, Optional): The ID of the user group. UserType (String, Required): The type of user. Valid values: user, user group, and _ everyone. Permission (String, Required): The permission type. Valid values: RO (read- only), RW (read and write), forbid delete _ (read and write, but cannot delete), full control, and _ forbid access (no _ access). If UserType is set to everyone, Permission can only be set to RW or RO. AccessType (String, Optional): The access type. Valid value: local. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Request example

```json
http(s)://[Endpoint]/?Action=BatchCreateSmbAcl &ShareId=3e47****** &Acls= [{"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000000,"use ame":"JL-USER-02"}, {"AccessType":"local","UserType":"user","Permission":"RO","UserId":1000000000000001,"user me":"JL-USER-01"}] &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.9.2 DescribeSmbAcls

Queries the Server Message Block (SMB) access control lists (ACLs). This operation supports paginated queries. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. The default value is 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclEntries | Array | [{}] | A list of SMB ACLs. |

| E r | lastic File System Guide·API refere | NAS Develope nce |   |   |   |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| -AclId | Long | 1000000000 | The ID of the ACL rule. |
| -UserId | Long | 100000000000000 0 | The ID of the file system user. |
| -GroupId | Long | 10000 | The ID of the file system user group. |
| -UserType | String | everyone | The type of the user. Valid values: user, user group, and everyone. _ |
| -UserName | String | myuser | The username. |
| - UserGroupNa me | String | myusergroup | The name of the user group. |
| -Permission | String | RO | The permission type. Valid values: RO (read-only), RW (read/write), forbid delete _ (read/write but cannot delete), full control, _ and forbid access (cannot access). _ If UserType is set to everyone, only RW and RO are supported. |
| -AccessType | String | local | The access type. Valid value: local. |
| -CreateTime | String | 2025-10- 16T09:55:41Z | The time when the SMB ACL was created. |
| -ModifyTime | String | 2025-10- 17T09:55:41Z | The time when the SMB ACL was last modified. If the SMB ACL has not been modified, this value is the same as the creation time. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of SMB ACLs. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Request example

```
http(s)://[Endpoint]/?Action=DescribeSmbAcls &ShareId=3e47****** &<Common request parameters>
```

Response example

```json
 "AclEntries":[
   "ModifyTime":"2025-10-17T09:55:41Z",
   "UserName":"myuser",
   "UserId":1000000000000000,
   "AclId":1000000000,
   "UserGroupName":"myusergroup",
   "CreateTime":"2025-10-16T09:55:41Z",
   "Permission":"RO",
   "UserType":"everyone",
   "AccessType":"local",
   "GroupId":10000
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
```

#### 5.9.3 BatchUpdateSmbAcl

Updates multiple SMB access control lists at a time. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Acls | Strin g | Query | Yes | [{"AclId": 1000000000,"Permissio n":"RO"},{"AclId": 1000000001,"Permissio n":"RO"}] | A list of access control list (ACL) entries. The value must be a JSON array. A single ACL entry contains the following parameters: AclId (Long, Required): The ID of the ACL. Call the DescribeSmbAcls operation to obtain the ID. Permission (String, Required): The permission type. Valid values: "RO" (read- only), "RW" (read/write), "forbid delete" _ (read/write but delete is denied), "full control" (full _ control), and "forbid access" _ (access denied). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Request example

```
http(s)://[Endpoint]/?Action=BatchUpdateSmbAcl &ShareId=3e47****** &Acls=[{"AclId": 1000000000,"Permission":"RO"},{"AclId": 1000000001,"Permission":"RO"}] &<Common request parameters>
```

Sample success response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.9.4 BatchDeleteSmbAcl

Deletes one or more Server Message Block (SMB) access control lists (ACLs).

**Notes**

Deleting an SMB ACL affects access permissions for users and groups. This action can interrupt access to shared resources. Confirm that no services depend on the ACL before you delete it. Deleted SMB ACLs cannot be recovered. Perform this operation with caution. This operation uses common request headers. No special request headers are used. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. |
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the SMB share. Call the DescribeSmbShares operation to obtain this ID. |
| AclIds | Strin g | Query | Yes | [1000000000,10000000 01] | A list of ACL IDs. You can specify up to 100 IDs. Call the DescribeSmbAcls operation to obtain the IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Request example

```
http(s)://[Endpoint]/?Action=BatchDeleteSmbAcl &ShareId=3e47****** &AclIds=[1000000000,1000000001] &<Common request parameters>
```

Response example

### 5.10 NFS share

#### 5.10.1 CreateNfsShare

Creates a Network File System (NFS) share. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The ID of the file system. |
| ShareNam e | Strin g | Query | Yes | mynfsshare | The name of the NFS share. The name must be 2 to 128 characters long. It must start with a letter or a Chinese character and can contain digits, periods (.), underscores ( ), and _ hyphens (-). |
| MountTar getDomai n | Strin g | Query | No | 1ca404a666-x****.cn- hangzhou.*****.*****.co m | The domain name of the mount target. This parameter is deprecated and no longer needs to be configured. |
| MountTar getInfo | Strin g | Query | No | /efs-nas-73**** | Information about the mount target. This parameter is deprecated and no longer needs to be configured. |
| Networks | Strin g | Query | No | - | The network configuration. This parameter is deprecated and no longer needs to be configured. |
| NfsVersio n | Strin g | Query | No | - | The NFS version string. This parameter is deprecated and no longer needs to be configured. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| VSwitchId | Strin g | Query | No | vsw- bp1s5fnvk4gn2tws0**** | The ID of the virtual switch. |
| VpcId | Strin g | Query | No | vpc- bp1b1xjllp3ve5yze**** | The ID of the VPC. |
| DfsNfsSha reAcls | Strin g | Query | No | - | The access control list (ACL) for NFS clients. This parameter is deprecated and no longer needs to be configured. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| ShareId | String | 3e47****** | The ID of the share. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateNfsShare &FileSystemId=efs-nas-c***** &ShareName=mynfsshare &<Common request parameters>
```

Sample success response

```json
 "ShareId":"3e47******",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.10.2 DescribeNfsConnections

Queries the details and the number of connections for a Network File System (NFS) share. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | No | 3e47****** | The ID of the NFS share. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. The default value is 20. |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The ID of the file system. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NfsConnection s | Array | [{}] | The list of NFS share connections. |
| -ShareId | String | 3e47****** | The ID of the NFS share. |
| -ClientIp | String | 10.10.10.** | The client IP address. |
| -NfsVersion | String | v3 | The protocol version. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of NFS share connections. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeNfsConnections &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Sample response

```json
 "NfsConnections":[
   "ShareId":"3e47******",
   "NfsVersion":"v3",
   "ClientIp":"10.10.10.**"
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
```

#### 5.10.3 DescribeNfsShares

Queries a paginated list of Network File System (NFS) shares. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. |
| FileSyste mId | Strin g | Query | No | efs-nas-0***** | The file system ID. |
| ShareId | Strin g | Query | No | 3e47****** | The NFS share ID. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page for a paged query. The default value is 20. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| NfsShares | Array | [{}] | The list of NFS shares. |
| -ShareId | String | 3e47****** | The NFS share ID. |
| -ShareName | String | mynfsshare | The NFS share name. |
| -FileSystemId | String | efs-nas-0***** | The ID of the file system to which the share belongs. |
| -Status | String | ACTIVE | The current status of the NFS share. Valid values: ACTIVE (running), PENDING (initializing or modifying), and DELETING (deleting). |
| -CreateTime | String | 2025-10- 17T09:55:41Z | The time when the NFS share was created. |
| -VpcId | String | vpc- bp15zckdt37pq72z v**** | The VPC ID. |
| -Azone | String | cn-hangzhou-** | The zone. |
| - MountTargetD omain | String | 04f314****- at***.cn- hangzhou.**.***.co m | The domain name of the mount target. |
| - MountTargetIn fo | String | /efs-nas-73**** | The information about the mount target. |
| -VswitchId | String | vsw- bp1e7clcw529l773 d**** | The virtual switch ID. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of NFS shares. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeNfsShares &Common request parameters
```

Sample response

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "NfsShares":[
   "Status":"ACTIVE",
   "Azone":"cn-hangzhou-**",
   "ShareId":"3e47******",
   "VpcId":"vpc-bp15zckdt37pq72zv****",
   "MountTargetDomain":"04f314****-at***.cn-hangzhou.**.***.com",
   "CreateTime":"2025-10-17T09:55:41Z",
   "MountTargetInfo":"/efs-nas-73****",
   "ShareName":"mynfsshare",
   "FileSystemId":"efs-nas-0*****",
   "VswitchId":"vsw-bp1e7clcw529l773d****"
```

`]`

#### 5.10.4 ModifyNfsShare

Modifies the configuration of an NFS share.

**Request header**

This operation uses common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the NFS share. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareNam e | Strin g | Query | No | mynfssharenew | The name of the NFS share. The name must be 2 to 128 characters in length. It must start with a letter and can contain digits, periods (.), underscores ( ), and _ hyphens (-). |
| NfsVersio n | Strin g | Query | No | - | The NFS version string. This parameter is deprecated and does not need to be specified. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Sample request

```
http(s)://[Endpoint]/?Action=ModifyNfsShare &ShareId=3e47****** &ShareName=mynfssharenew &<Common request parameters>
```

Sample success response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.10.5 DeleteNfsShare

Deletes an NFS share.

**Notes**

Deleting an NFS share prevents all users from accessing resources on the share. Confirm that no services depend on the share before you delete it. An NFS share cannot be recovered after it is deleted. Proceed with caution. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ShareId | Strin g | Query | Yes | 3e47****** | The ID of the NFS share. |
| Force | Boole an | Query | No | false | If the NFS share has active connections or open files, the delete operation fails by default. You can enable the force delete option to ignore active sessions and remove the share configuration. This might break client connections. Use this option with caution. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteNfsShare &ShareId=3e47****** &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

### 5.11 NFS ACL

#### 5.11.1 BatchCreateNfsAcl

Creates multiple Network File System (NFS) access control lists (ACLs) in a batch operation. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| ShareId | Strin g | Query | No | 3e47****** | The ID of the NFS share. |

| Parame ter | Typ e | Locati on | Require d | Example | Description |
|---|---|---|---|---|---|
| Acls | Strin g | Query | Yes | [{"Type":"every- client","Permission":"RO ","RootSquash":true,"All Squash":false}] | The ACL for NFS clients. Each client ACL contains the following parameters: ClientIp (String, Required): The IP address or network segment of the client. This parameter is required only when you set Type to client. Permission (String, Required): The access permissions. Valid values are RO (read- only) and RW (read/write). RootSquash (Boolean, Optional): Specifies whether to enable root squash. The default value is true. If you enable root squash, the root user of a remote client is mapped to an anonymous user. This prevents the client from having superuser privileges on the server. When a client writes a file as the root user, the file owner on the server becomes `nobody` instead of `root`. AllSquash (Boolean, Optional): Specifies whether to enable all squash. The default value is false. If you enable all squash, all client users are mapped to an anonymous user. All file operations are then performed as the anonymous user, and the original user information is not retained. Type (String, Optional): The type of client. Valid values are `every-client` (all clients) and `client` (a specific client). The default value is `every-client`. |

| Parame FteilerSyste mId | Typ Setrin g | Locati on Query | Require d Yes | Example efs-nas-c***** | Description The ID of the file system. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Request example

```
http(s)://[Endpoint]/?Action=BatchCreateNfsAcl &Acls=[{"Type":"every-client","Permission":"RO","RootSquash":true,"AllSquash":false}] &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.11.2 DescribeNfsAcls

Queries the access control lists (ACLs) of a Network File System (NFS). This operation supports paged queries. This operation uses only common request headers. For more information, see the Common request parameters document.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. |
| ShareId | Strin g | Query | No | 3e47****** | The NFS share ID. |
| PageNum | Integ er | Query | No | 1 | The page number. The default value is 1. |

|   |   |   |   | Elastic | File System NAS Develop |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 10 | The number of resources to return on each page. The default value is 20. |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The file system ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AclEntries | Array | [{}] | The information about the NFS access control lists. |
| -AclId | Long | 2000000000 | The ID of the ACL rule. |
| -ClientIp | String | 10.10.10.** | The client IP address. |
| -Permission | String | RO | The access permissions. Valid values: `RO` (read-only) and `RW` (read/write). |
| -RootSquash | Boolean | true | Specifies whether to enable root squash. The default value is `true`. If enabled, the root user of a remote client is mapped to an anonymous user. This prevents the root user from having superuser permissions on the server. When the client writes a file as the root user, the file owner on the server becomes `nobody` instead of `root`. |
| -AllSquash | Boolean | false | Specifies whether to enable all squash. The default value is `false`. If enabled, all client users are mapped to an anonymous user. All file operations are then performed as the anonymous user, and the original user information is not saved. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Type | String | client | The type. Valid values: `every-client` (all clients, default) and `client` (a specific client). |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| TotalCount | Integer | 5 | The total number of NFS ACLs. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeNfsAcls &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Sample response

```json
 "AclEntries":[
   "AllSquash":false,
   "Type":"client",
   "AclId":2000000000,
   "Permission":"RO",
   "RootSquash":true,
   "ClientIp":"10.10.10.**"
```

`],`

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10
```

#### 5.11.3 BatchUpdateNfsAcl

Updates multiple Network File System (NFS) access control lists in a batch. This operation uses only common request headers. For more information, see Common request parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The ID of the cluster. |
| ShareId | Strin g | Query | No | 3e47****** | The ID of the NFS share. |
| Acls | Strin g | Query | Yes | [{"AclId": 2000000000,"Permissio n":"RO"},{"AclId": 2000000001,"Permissio n":"RO"}] | A list of access control lists (ACLs) in a JSON array. Each ACL contains the following parameters: `AclId` (Long, Required): The ID of the ACL. Obtain this ID by calling the `DescribeNfsAcls` operation. `Permission` (String, Required): The permission type. Valid values are `RO` (read-only) and `RW` (read/write). |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The ID of the file system. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

Sample request

```
http(s)://[Endpoint]/?Action=BatchUpdateNfsAcl &Acls=[{"AclId": 2000000000,"Permission":"RO"},{"AclId": 2000000001,"Permission":"RO"}] &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Sample response

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

#### 5.11.4 BatchDeleteNfsAcl

Deletes multiple Network File System (NFS) access control lists (ACLs) in a batch operation.

**Notes**

Deleting an NFS ACL affects the access permissions of users or groups for shared resources and can cause access interruptions. Before you delete an NFS ACL, confirm that no services depend on it. You cannot recover an NFS ACL after it is deleted. Proceed with caution. This operation uses only common request headers. For more information, see Common parameters.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| ClusterId | Strin g | Query | No | c****** | The cluster ID. |
| ShareId | Strin g | Query | No | 3e47****** | The ID of the NFS share. |
| AclIds | Strin g | Query | Yes | [2000000000,20000000 01] | A list of ACL IDs. You can specify up to 100 IDs. Call the DescribeNfsAcls operation to obtain the ACL IDs. |
| FileSyste mId | Strin g | Query | Yes | efs-nas-c***** | The file system ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |

Request example

```
http(s)://[Endpoint]/?Action=BatchDeleteNfsAcl &AclIds=[2000000000,2000000001] &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Response example

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************"
```

### 5.12 Snapshot

#### 5.12.1 CreateSnapshot

Create a snapshot.

**Notes**

A single file system supports a recommended maximum of 128 snapshots and an absolute maximum of 2,048 snapshots. You can create a maximum of 8,192 snapshots in total for all your file systems. If a snapshot is being created for a file system, you cannot create another snapshot for that file system. You must wait at least 10 minutes between creating snapshots. A snapshot backs up data at a specific point in time. Incremental data generated by file system operations during the snapshot creation process is not synchronized with the snapshot. This operation uses only common request headers. For more information, see Common parameters.

| Parameter Name | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Body | Yes | efs-nas-c***** | The ID of the file system. |
| SnapshotN ame | Strin g | Body | No | testSnapshotName | The name of the snapshot. |
| Descriptio n | Strin g | Body | No | For testing. | The description of the snapshot. |

| Lock | Strin g | Body | No | true | Specify whether to lock the snapshot. Valid values: true: The item is locked. false (default): Does not lock the snapshot. After a snapshot is locked, it is not automatically deleted when its retention period expires. You must manually unlock the snapshot before you can delete it. |
|---|---|---|---|---|---|
| Retention | Strin g | Body | No | never | The retention period of the snapshot. The system automatically deletes snapshots that have expired. To have the system manage the snapshot lifecycle, set this parameter to a string that consists of a positive integer and a unit. Valid units are h (hours), d (days), m (months), and y (years). For example, a value of 24h or 1d means that the snapshot is deleted after 24 hours or 1 day. To create a snapshot that never expires, set this parameter to never. |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates success. |
| SnapshotId | String | snap- 1764836********** ** | The ID of the snapshot. |

Sample request

```
http(s)://[Endpoint]/?Action=CreateSnapshot &FileSystemId=efs-nas-c***** &SnapshotName=testSnapshotName &<Common request parameters>
```

Sample response

```json
    "SnapshotId":"snap-1764836************",
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true
```

#### 5.12.2 ModifySnapshot

Modify the properties of a specified snapshot, such as its name, description, and retention period. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|

| SnapshotI d | Strin g | Body | Yes | snap- 1764836************ | The ID of the snapshot. |
|---|---|---|---|---|---|
| SnapshotN ame | Strin g | Body | No | testSnapshotName | The name of the snapshot. |
| Descriptio n | Strin g | Body | No | For testing. | The description of the snapshot. |
| Lock | Strin g | Body | No | true | Specify whether to lock the snapshot. Valid values: true: The item is locked. false (default): Does not lock the snapshot. If a snapshot is locked, it is not automatically deleted when its retention period expires. You also cannot manually delete the locked snapshot. |
| Retention | Strin g | Body | No | 7d | The retention period of the snapshot. The system automatically deletes snapshots that have expired. To have the system automatically manage the snapshot lifecycle, set this parameter to a string that consists of a positive integer and a unit. Valid units are h (hours), d (days), m (months), and y (years). For example, a value of 24h or 1d indicates that the snapshot is retained for 24 hours or 1 day before it is deleted. To retain the snapshot permanently, set this parameter to never. |

**Returned Data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates success. |
| SnapshotId | String | snap- 1764836********** ** | The ID of the snapshot. |

Sample request

```
http(s)://[Endpoint]/?Action=ModifySnapshot &SnapshotId=snap-1764836************ &<Common request parameters>
```

Sample response

```json
    "SnapshotId":"snap-1764836************",
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Success":true
```

#### 5.12.3 DescribeSnapshots

Query information about one or more snapshots of a specified file system.

**Notes**

If you do not specify any parameters, this operation returns snapshots for all file systems. This operation uses only common request headers. For more information, see Common request parameters.

| > Document V | ersion: 2 | 0260701 |   |   | 10 |
|---|---|---|---|---|---|

| Parameter Name | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Body | No | efs-nas-0***** | The ID of the file system. |
| SnapshotI d | Strin g | Body | No | snap- 1764836************ | The ID of the snapshot. |
| PageSize | Integ er | Body | No | 10 | The number of resources to return on each page. Default value: 20 |
| PageNum | Integ er | Body | No | 1 | The page number. Default value: 1 |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| Snapshots | Array | [{}] | A list of snapshots. |
| -SnapshotId | String | snap- 1764836********** ** | The ID of the snapshot. |
| - SnapshotNam e | String | testSnapshotName | The name of the snapshot. |
| -FileSystemId | String | efs-nas-0***** | The ID of the file system to which the snapshot belongs. |
| -Status | String | progressing | The status of the snapshot. 1: Creation successful 0: Creation failed |
| -CreateTime | String | 2025-12- 15T09:55:41Z | The time when the snapshot was created. The time is in UTC and is formatted in ISO 8601 standard as yyyy-MM-ddThh:mmZ . |

| - ExpirationTim e | String | 2026-12- 15T09:55:41Z | The time when the snapshot expires. The time is in UTC and is formatted in ISO 8601 standard as yyyy-MM-ddThh:mmZ. |
|---|---|---|---|
| -Retention | String | never | The retention period of the snapshot. A value of `never` indicates that the snapshot never expires. Other values are strings that consist of a positive integer and a unit. Valid units: h (hours), d (days), m (months), and y (years). |
| -Description | String | For testing | The description of the snapshot. |
| -Lock | Boolean | true | The lock status of the snapshot. Valid values: true (locked) and false (unlocked). |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| TotalCount | Integer | 5 | The total number of snapshots. |
| PageNum | Integer | 10 | The page number. |
| PageSize | Integer | 1 | The number of resources on each page. |

Sample request

```
http(s)://[Endpoint]/?Action=DescribeSnapshots &<Common request parameters>
```

Sample response

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":10,
 "PageSize":1,
 "Snapshots":[
   "Status":"progressing",
   "SnapshotId":"snap-1764836************",
   "Description":"For testing.",
   "CreateTime":"2025-12-15T09:55:41Z",
   "FileSystemId":"efs-nas-0*****",
   "ExpirationTime":"2026-12-15T09:55:41Z",
   "Retention":"never",
   "SnapshotName":"testSnapshotName",
   "Lock":true
```

`]`

#### 5.12.4 DeleteSnapshot

Delete a specified snapshot or cancels an in-progress snapshot creation task.

**Notes**

Deleted snapshots cannot be recovered. Proceed with caution. Locked snapshots cannot be deleted. You can call the ModifySnapshot operation to unlock the snapshot before you delete it. This operation uses common request headers. Special request headers are not required. For more information, see Common request parameters.

| Parameter | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotI d | Strin g | Body | Yes | snap- 1764836************ | The ID of the snapshot. |

**Returned Data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| Result | String | true | Indicates whether the operation was successful. A value of `true` is returned on success. |

Request example

```
http(s)://[Endpoint]/?Action=DeleteSnapshot &SnapshotId=snap-1764836************ &<Common request parameters>
```

Sample successful response

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Result":"true"
```

#### 5.12.5 CreateScheduledSnapshot

Creates a scheduled snapshot for a file system. After the policy is created, the system automatically generates snapshots for the file system periodically.

**Notes**

We recommend that you retain up to 128 snapshots for a single file system. You can create a maximum of 2,048 snapshots for a single file system and 8,192 snapshots for all file systems. If a snapshot for a file system is still being created, you cannot create another snapshot for the same file system. To avoid conflicts, we recommend that you set an interval of more than 10 minutes between snapshot creations. A snapshot backs up data at a specific point in time. Any incremental data generated during the snapshot creation process will not be synchronized to the snapshot. If you associate multiple scheduled snapshot policies with a single file system, all these policies will take effect simultaneously on that file system. This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|

| SnapshotP olicyId | Strin g | Quer y | Yes | sp-17748631231******** | The ID of the scheduled snapshot policy. |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Trigger | Bool ean | Quer y | Yes | true | Specifies whether to immediately trigger a snapshot creation upon association. false (default): The system creates snapshots based on the schedule defined in the snapshot policy. true: The system immediately creates the first snapshot. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |
| Code | String | 200 | The status code or Post Office Protocol (POP) error code of the operation. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |
| ScheduledSna pshotId | String | snap- 17781404842***** *** | The association ID of the scheduled snapshot. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateScheduledSnapshot &SnapshotPolicyId=sp-17748631231******** &FileSystemId=efs-nas-c***** &Trigger=true &Common request parameters
```

Sample success responses

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ScheduledSnapshotId":"snap-17781404842********",
 "HttpStatusCode":"200",
 "Code":"200",
 "Success":true
```

#### 5.12.6 DescribeSnapshotPolicyBindings

Lists the association relationships between snapshot policies and file systems. You can filter results by policy ID or file system ID, and you can paginate the results. This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotP olicyId | Strin g | Body | No | sp- 177909055113******** | The ID of the snapshot policy. |
| FileSystem Id | Strin g | Body | No | efs-nas-c***** | The ID of the file system. |
| PageSize | Integ er | Body | No | 10 | The number of entries to return on each page. Default value: 20. |
| PageNum | Integ er | Body | No | 1 | The number of the page to return. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnapshotPolic yBindings | Array | {[]} | The list of file systems bound to the scheduled snapshot policy. |
| -FileSystemId | String | efs-nas-0***** | The ID of the file system. |
| - SnapshotPolic yId | String | sp- 17748631231***** *** | The ID of the scheduled snapshot policy. |
| -CreateTime | String | 2026-05- 25T09:55:41Z | The time when the scheduled snapshot policy was bound to the file system. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| TotalCount | Integer | 5 | The total number of file systems queried. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources per page. |
| NextToken | String | FFmyTO70tTpLG6I 3FmYAXGKPd**** | The token that marks the start of the next query. If NextToken is empty, no more results are available. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSnapshotPolicyBindings &Common request parameters
```

Sample success responses

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "SnapshotPolicyBindings":[
   "SnapshotPolicyId":"sp-17748631231********",
   "CreateTime":"2026-05-25T09:55:41Z",
   "FileSystemId":"efs-nas-0*****"
```

`]`

#### 5.12.7 DeleteScheduledSnapshot

Disassociates a file system from a snapshot policy and stops scheduled snapshots for the file system. This operation uses common request headers only. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotP olicyId | Strin g | Quer y | Yes | sp-17748631231******** | The ID of the scheduled snapshot policy. |
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |

| Code | String | 200 | The status code or Post Office Protocol (POP) error code of the API. |
|---|---|---|---|
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |
| ScheduledSna pshotId | String | snap- 17781404842***** *** | The association ID of the deleted scheduled snapshot. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteScheduledSnapshot &SnapshotPolicyId=sp-17748631231******** &FileSystemId=efs-nas-c***** &Common request parameters
```

Sample success responses

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "ScheduledSnapshotId":"snap-17781404842********",
 "HttpStatusCode":"200",
 "Code":"200",
 "Success":true
```

### 5.13 Snapshot policy

#### 5.13.1 CreateSnapshotPolicy

Creates a snapshot policy and associates it with a file system for scheduled snapshots.

**Notes**

You can create up to 128 scheduled snapshot policies, and associate up to 8 policies with a single file system. You can apply a scheduled snapshot policy to any file system within the selected organization, resource set, and region. Evaluate your cluster's storage capacity and backup requirements before configuration to avoid resource waste or performance degradation. This operation uses common request headers only. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotP olicyName | Strin g | Body | Yes | mysnapshotpolicy | The name of the snapshot policy. |
| CronExpre ssion | Strin g | Body | Yes | 0 0 * * * | The cron expression that defines the snapshot trigger cycle. |
| ExpireTyp e | Bool ean | Body | Yes | true | Specifies whether the snapshot expires by time. Valid values: true: The snapshot expires by time. You must also specify RetentionNum and RetentionUnit. false: The snapshot never expires. |
| Retention Num | Integ er | Body | No | 30 | The retention duration. This parameter takes effect only when ExpireType is set to true. |
| RetentionU nit | Strin g | Body | No | d | The retention unit. This parameter takes effect only when ExpireType is set to true. Valid values include h (hours), d (days), t (months), and y (years). |
| Descriptio n | Strin g | Body | No | snapshotpolicy test | The description of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |

| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |
|---|---|---|---|
| SnapshotPolic yId | String | sp- 17748631431***** *** | The ID of the snapshot policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateSnapshotPolicy &SnapshotPolicyName=mysnapshotpolicy &CronExpression=0 0 2 ? * 1-7 &ExpireType=true &Common request parameters
```

Sample success responses

```json
 "SnapshotPolicyId":"sp-17748631431********",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

#### 5.13.2 ModifySnapshotPolicy

Modifies the configuration of an existing snapshot policy, including the snapshot cycle and deletion upon expiration. This operation uses common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotP olicyId | Strin g | Body | Yes | sp-17748631431******** | The ID of the snapshot policy. |
| SnapshotP olicyName | Strin g | Body | No | mysnapshotpolicy | The name of the snapshot policy. |

| CronExpre ssion | Strin g | Body | No | 0 0 * * * | The cron expression that defines the snapshot trigger cycle. |
|---|---|---|---|---|---|
| ExpireTyp e | Bool ean | Body | No | true | Specifies whether snapshots expire by time. Valid values: true: Snapshots expire by time. You must specify RetentionNum and RetentionUnit. false: Snapshots never expire. |
| Retention Num | Integ er | Body | No | 30 | The retention period. This parameter takes effect only when ExpireType is set to true. |
| RetentionU nit | Strin g | Body | No | d | The unit of the retention period. This parameter takes effect only when ExpireType is set to true. Valid values: h (hours), d (days), t (months), and y (years). |
| Descriptio n | Strin g | Body | No | testDescription | The description of the policy. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |
| SnapshotPolic yId | String | sp- 17748631431***** *** | The ID of the snapshot policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySnapshotPolicy &SnapshotPolicyId=sp-17748631431******** &Common request parameters
```

Sample success responses

```json
 "SnapshotPolicyId":"sp-17748631431********",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

#### 5.13.3 DescribeSnapshotPolicies

List snapshot policies. You can filter the list by file system or policy ID. Pagination is supported. This operation uses common request headers only. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Body | No | efs-nas-c***** | The ID of the file system. |
| SnapshotP olicyId | Strin g | Body | No | sp- 177909055113******** | The ID of the snapshot policy. |
| PageSize | Integ er | Body | No | 10 | The number of entries per page. Default value: 10. |
| PageNum | Integ er | Body | No | 1 | The page number. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SnapshotPolici es | Array | [{}] | The list of snapshot policy details. |

| - SnapshotPolic yId | String | sp- 17748631431***** *** | The ID of the snapshot policy. |
|---|---|---|---|
| - SnapshotPolic yName | String | mysnapshotpolicy | The name of the snapshot policy. |
| - CronExpressio n | String | 0 0 * * * | The cron expression that defines the snapshot trigger cycle. |
| -ExpireType | String | true | Indicates whether the snapshot expires based on time. |
| - RetentionNum | Integer | 30 | The retention period duration. |
| -RetentionUnit | String | d | The unit of the retention period. |
| -Description | String | my sanpshot policy | The description of the snapshot policy. |
| -CreateTime | String | 2025-10- 15T09:55:41Z | The creation time of the snapshot policy. |
| - AssociatedDire ctoryCount | Integer | 1 | The number of directories associated with the snapshot policy. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| TotalCount | Long | 5 | The total number of snapshot policies queried. |
| PageNum | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of resources per page. |
| NextToken | String | FFmyTO70tTpLG6I 3FmYAXGKPd**** | The token for the next query. If NextToken is empty, no more results are available. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSnapshotPolicies &Common request parameters
```

Sample success responses

```json
 "TotalCount":5,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "NextToken":"FFmyTO70tTpLG6I3FmYAXGKPd****",
 "SnapshotPolicies":[
   "RetentionNum":30,
   "AssociatedDirectoryCount":1,
   "SnapshotPolicyId":"sp-17748631431********",
   "Description":"my sanpshot policy",
   "RetentionUnit":"d",
   "CreateTime":"2025-10-15T09:55:41Z",
   "ExpireType":"true",
   "SnapshotPolicyName":"mysnapshotpolicy",
   "CronExpression":"0 0 * * *"
```

`]`

#### 5.13.4 DeleteSnapshotPolicy

Deletes a specified snapshot policy.

**Notes**

Before you delete a scheduled snapshot policy, ensure that it is not associated with any directories. Disassociating a policy does not delete the associated directories. Deleted scheduled snapshot policies cannot be restored. Proceed with caution. This operation uses common request headers only. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| SnapshotP olicyId | Strin g | Body | Yes | sp-17748631431******** | The ID of the snapshot policy. |

| Force | Bool ean | Body | No | true | Specifies whether to forcibly delete a snapshot policy. Default value: false. If the snapshot policy is still associated with a file system, you must set this parameter to true to delete the policy. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |
| SnapshotPolic yId | String | sp- 17748631431***** *** | The ID of the deleted snapshot policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteSnapshotPolicy &SnapshotPolicyId=sp-17748631431******** &Common request parameters
```

Sample success responses

```json
 "SnapshotPolicyId":"sp-17748631431********",
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Success":true
```

### 5.14 WORM

#### 5.14.1 CreateWorm

Enables the Write Once Read Many (WORM) policy for a file system. Once enabled, files automatically or manually enter a protected state upon write completion. During the protection period, you can only read the files, and any modifications or deletions are prohibited.

**Considerations**

Currently, only compliance mode is supported. In this mode, no user can delete or modify directories or files that are under WORM protection. For compliance reasons, the WORM policy cannot be disabled or reconfigured once enabled for a file system. Proceed with caution. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| MinProtect Period | Strin g | Quer y | Yes | 5d | The minimum protection period. This value defines the minimum duration a file must remain protected when you manually set its protection period. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, use a number followed by a unit suffix. The maximum value is 30y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 5d. Set to infinity to configure the protection period to its maximum value. |

| MaxProtec tPeriod | Strin g | Quer y | Yes | 1y | The maximum protection period. This value defines the maximum duration a file can remain protected when you manually set its protection period. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, use a number followed by a unit suffix. The maximum value is 70y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 1y. Set to infinity to configure the protection period to its maximum value. |
|---|---|---|---|---|---|
| DefaultPro tectPeriod | Strin g | Quer y | Yes | 1t | The default protection period. This value defines the default duration a file remains protected when no manual protection period is configured. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, use a number followed by a unit suffix. The maximum value is 70y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 1t. If you set the value to infinity, the file receives permanent protection. |

| AutoLockP eriod | Strin g | Quer y | Yes | 3d | The auto-lock period. After a file is written, if it remains unmodified beyond this period, the system automatically places it into the WORM- protected state. Specify the value as a number followed by a unit suffix. The maximum value is 45d. Valid unit suffixes include h (hours), d (days), and t (months). Example: 3d. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates the operation was successful. |
| Code | String | 200 | The status code or Post Office Protocol (POP) error code. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |
| WormId | String | worm-******** | The ID of the WORM policy. |

Sample requests

```
http(s)://[Endpoint]/?Action=CreateWorm &FileSystemId=efs-nas-c***** &MinProtectPeriod=5d &MaxProtectPeriod=1y &DefaultProtectPeriod=1t &AutoLockPeriod=3d &Common request parameters
```

Sample success responses

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "HttpStatusCode":"200",
 "WormId":"worm-********",
 "Code":"200",
 "Success":true
```

#### 5.14.2 UpdateWorm

Modifies the protection period configuration of a Write Once Read Many (WORM) protection policy.

**Considerations**

In compliance mode, you can only extend the protection period. You also cannot modify the automatic lock period. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| WormId | Strin g | Quer y | Yes | worm-******** | The ID of the WORM policy. |

| MinProtect Period | Strin g | Quer y | No | 5d | Extend the minimum protection period. When you manually set the protection period for a file, this value defines the minimum duration the file must remain protected. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, combine a number with a unit suffix. The maximum value is 30y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 5d. Set to infinity to configure the protection period to its maximum value. |
|---|---|---|---|---|---|
| MaxProtec tPeriod | Strin g | Quer y | No | 1y | Extend the maximum protection period. When you manually set the protection period for a file, this value defines the maximum duration the file can remain protected. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, combine a number with a unit suffix. The maximum value is 70y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 1y. Set to infinity to configure the protection period to its maximum value. |

| DefaultPro tectPeriod | Strin g | Quer y | No | 1t | Extend the default protection period. When no manual protection period is set, this value defines the default duration a file remains protected after entering the protected state. You can specify a specific duration or set it to infinity (indefinite). To specify a specific duration, combine a number with a unit suffix. The maximum value is 70y. Valid unit suffixes include h (hours), d (days), t (months), and y (years). Example: 1t. Set to infinity to permanently protect the file. |
|---|---|---|---|---|---|
| AutoLockP eriod | Strin g | Quer y | No | - | You cannot modify the automatic lock period. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates the operation was successful. |
| Code | String | 200 | The status code or Post Office Protocol (POP) error code of the API. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

| WormId | String | worm-******** | The ID of the WORM policy. |
|---|---|---|---|

Sample requests

```
http(s)://[Endpoint]/?Action=UpdateWorm &WormId=worm-******** &MinProtectPeriod=5d &Common request parameters
```

Sample success responses

```json
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "Message":"success",
 "HttpStatusCode":"200",
 "WormId":"worm-********",
 "Code":"200",
 "Success":true
```

#### 5.14.3 DescribeWorms

Lists WORM protection policies. You can filter the list by WORM ID or file system ID. Pagination is supported. This operation uses common request headers and does not require special request headers. For more information, see Common request parameters.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| WormId | Strin g | Body | No | worm-6***** | The ID of the WORM policy. |
| FileSystem Id | Strin g | Body | No | efs-nas-c***** | The ID of the file system. |
| PageSize | Integ er | Body | No | 20 | The number of entries to return on each page. Default value: 20. |

| PageNum | Integ er | Body | No | 1 | The number of the pages to return. Default value: 1. |
|---|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Worms | Array | [{}] | The list of WORM policies. |
| -WormId | String | worm-******** | The ID of the WORM policy. |
| -FileSystemId | String | efs-nas-0***** | The ID of the file system. |
| -Status | String | active | The status of the WORM policy. |
| -Mode | String | compliance | The mode of the WORM policy. Only compliance mode is supported. |
| -Path | String | /efs-nas-******** | The path protected by the WORM policy. |
| - MinProtectPeri od | String | 5d | The minimum protection period. |
| - MaxProtectPer iod | String | 1y | The maximum protection period. |
| - DefaultProtect Period | String | 1t | The default protection period. |
| - AutoLockPerio d | String | 3d | The auto-lock period. |
| -CreateTime | String | 2026-05- 17T16:26:22Z | The time when the WORM policy was created. The time follows the ISO 8601 format. |
| -UpdateTime | String | 2026-05- 17T16:26:22Z | The time when the WORM policy was last modified. The time follows the ISO 8601 format. |

| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of WORM policies. |
| PageNum | Integer | 1 | The number of pages returned. |
| PageSize | Integer | 10 | The number of entries per page. |

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWorms &Common request parameters
```

Sample success responses

```json
 "TotalCount":1,
 "RequestId":"F0A8A039-930D-5EC1-97C8-************",
 "PageNum":1,
 "PageSize":10,
 "Worms":[
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
```

`]`

### 5.15 Recycle bin

#### 5.15.1 EnableTrash

Enable the recycle bin feature, which moves deleted files to the recycle bin instead of permanently deleting them. This operation requires only common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Filter | Strin g | Quer y | No | *.tmp,*.txt | A filter rule. Files with a matching prefix or suffix are not moved to the recycle bin. The asterisk (*) wildcard character represents any string of characters. You can configure multiple rules. Nested rules are not allowed, such as *ab and *b , or cd* and c* . Separate multiple rules with a comma (,). If no filter rule is set, all deleted files from the file system are moved to the recycle bin. |
| ExpiredTi me | Long | Quer y | No | 1440 | The retention period for files in the recycle bin, in minutes. The default value is 0. Valid values: 0 (never expire), or an integer from 1440 (1 day) to 525600 (1 year), inclusive. When a file has been in the recycle bin for the specified retention period, the system automatically deletes the expired file. |

**Response data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation succeeded. A value of `true` indicates success. |
| Code | String | 200 | The API status or a POP error code. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

Request example

```
http(s)://[Endpoint]/?Action=EnableTrash &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Successful response example

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```

#### 5.15.2 UpdateTrash

Update the retention period for data in the recycle bin or the file filtering rules. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter name | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Filter | Strin g | Quer y | No | *.tmp | The rules to filter files. Files that match the specified prefixes or suffixes are not moved to the recycle bin. The asterisk (*) wildcard character represents any number of characters. You can specify multiple rules. However, nested rules are prohibited, such as *ab and *b , or cd* and c* . Separate multiple rules with a comma (,). If no filtering rules are set, all deleted files from the file system are moved to the recycle bin. |
| ExpiredTi me | Long | Quer y | No | 14400 | The retention period for files in the recycle bin, in minutes. The default value is 0. Valid values: 0 (never expires), or an integer from 1440 (1 day) to 525600 (1 year). When the retention period of a file in the recycle bin ends, the system automatically deletes the expired file. |

|   | *ab |
|---|---|
| cd* |   |

|   | *b |
|---|---|
| c* |   |

**Return data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of `true` indicates success. |

| Code | String | 200 | The status of the API call or the POP error code. |
|---|---|---|---|
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

Request example

```
http(s)://[Endpoint]/?Action=UpdateTrash &FileSystemId=efs-nas-c***** &ExpiredTime=14400 &Common request parameters
```

Successful response example

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```

#### 5.15.3 ListTrashFiles

Query the files or folders in the recycle bin of a file system. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Limit | Long | Quer y | No | 10 | The number of resources to return. |

| Path | Strin g | Quer y | No | /test | The path of the file in the recycle bin that you want to query. |
|---|---|---|---|---|---|
| Start | Strin g | Quer y | No | file10 | The position to start the query. Enter a file name. For example, if a folder contains files from file1 to file100 and you set Limit to 10, the first page returns file1 to file10. If you then set Start to file10, the query returns file11 to file20. |
| Prefix | Strin g | Quer y | No | file | Matches files or folders with the specified prefix. |

**Returned data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| TrashFiles | Array | [{}] | A list of files staged in the recycle bin. |
| -Files | Long | 1 | The number of files. If the queried object is a file, the return value is 1. If the queried object is a folder, the return value is the total number of files in the folder. |
| -TrashPath | String | /efs-nas- ba4c37/.trash/curr ent/file11 | The storage path of the file in the recycle bin. |
| -Name | String | file11 | The name of the file. |
| -Size | Long | 1024 | The size of the file, in bytes. If the queried object is a file, the return value is the file size. If the queried object is a folder, the return value is the total size of all files in the folder. |
| -ExpiredTime | String | 2025-12- 15T16:00:00Z | The time when the file expires in the recycle bin. |

| -Type | String | Regular File | The type of the returned object. Valid values: Directory: a folder Regular File: a file |
|---|---|---|---|
| -Change | String | 2025-12- 10T16:00:00Z | The time when the file was last modified. |
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| TotalCount | Integer | 10 | This parameter is deprecated and is not returned. |

Request example

```
http(s)://[Endpoint]/?Action=ListTrashFiles &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Response example

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "TrashFiles":[
            "Type":"Regular File",
            "Size":1024,
            "ExpiredTime":"2025-12-15T16:00:00Z",
            "Change":"2025-12-10T16:00:00Z",
            "Files":1,
            "TrashPath":"/efs-nas-ba4c37/.trash/current/file11",
            "Name":"file11"
```

`]`

#### 5.15.4 RestoreTrashFile

Recover a file or folder from the recycle bin.

**Notes**

You can recover only one file or folder at a time. When you recover a folder, all files in that folder are recursively recovered. After a file is recovered, the system organizes the data. During this process, the performance of read requests may slightly decrease. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Loca tion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Path | Strin g | Quer y | Yes | /test | The full path of the file in the recycle bin that you want to recover. |
| Overwrite | Bool ean | Quer y | No | false | Specifies whether to overwrite a file or folder that has the same name in the specified path. Valid values: false (default): Skips the file or folder that has the same name in the original path. true: Overwrites the file or folder that has the same name in the original path. |

**Response data**

| Parameter name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates that the operation was successful. |
| Code | String | 200 | The API status or a POP error code. |
| Message | String | success | The error message. |

| HttpStatusCod e | String | 200 | The HTTP status code. |
|---|---|---|---|

Sample request

```
http(s)://[Endpoint]/?Action=RestoreTrashFile &FileSystemId=efs-nas-c***** &Path=/test &<Common request parameters>
```

Sample successful response

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```

#### 5.15.5 RemoveTrashFile

Permanently delete files or folders from the recycle bin.

**Usage notes**

When you permanently delete a folder, its contents are recursively deleted. A file system can run only one permanent deletion operation at a time. While a file or folder is being permanently deleted, you cannot start other recovery or cleanup operations. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter Name | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |
| Path | Strin g | Quer y | Yes | /test | The path of the file or folder to delete. |

**Response parameters**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The ID of the request. |
| Success | Boolean | true | Indicates whether the operation was successful. A value of true indicates success. |
| Code | String | 200 | The status of the API call or a POP error code. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

Sample request

```
http(s)://[Endpoint]/?Action=RemoveTrashFile &FileSystemId=efs-nas-c***** &Path=/test &<Common request parameters>
```

Sample response

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```

#### 5.15.6 DisableAndCleanTrash

Disable the recycle bin feature for a file system and deletes all files in the recycle bin.

**Notes**

Disabling the recycle bin permanently deletes all files within it. When you re-enable the recycle bin, it is empty. Files deleted before it was re-enabled cannot be recovered. This operation uses only common request headers. For more information, see Common request parameters.

| Parameter | Type | Positi on | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |

**Returned data**

| Parameter Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation was successful. A return value of true indicates success. |
| Code | String | 200 | The API status or a POP error code. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

Request example

```
http(s)://[Endpoint]/?Action=DisableAndCleanTrash &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Response example

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```

#### 5.15.7 EmptyTrash

Empty the recycle bin of a specified file system.

**Notes**

Deleted files cannot be recovered after you empty the recycle bin. Use this operation with caution. This operation uses common request headers. No special request headers are required. For more information, see Common request parameters.

| Parameter | Type | Locat ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Id | Strin g | Quer y | Yes | efs-nas-c***** | The ID of the file system. |

**Returned data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F0A8A039-930D- 5EC1-97C8- ************ | The request ID. |
| Success | Boolean | true | Indicates whether the operation is successful. A value of true indicates success. |
| Code | String | 200 | The status of the API call or a POP error code. |
| Message | String | success | The error message. |
| HttpStatusCod e | String | 200 | The HTTP status code. |

Sample request

```
http(s)://[Endpoint]/?Action=EmptyTrash &FileSystemId=efs-nas-c***** &<Common request parameters>
```

Sample response

```json
    "RequestId":"F0A8A039-930D-5EC1-97C8-************",
    "Message":"success",
    "HttpStatusCode":"200",
    "Code":"200",
    "Success":true
```
