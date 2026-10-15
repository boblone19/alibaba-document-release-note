---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Developer Guide 20260827"
product_version: "V3.18.6_2607"
doc_version: "20260827"
pdf_pages: 129
source_pdf: "7c4a3ca49af0e46d_Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Developer Guide 20260827.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8%20NAS/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Apsara%20File%20Storage%20NAS%20Developer%20Guide%2020260827.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Apsara File Storage NAS Developer Guide 20260827

## Table of Contents

- 1 Preparations
  - 1.1 Log on to OpenAPI Explorer
  - 1.2 Obtain the information and the endpoint of an API operation
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain an access credential assigned by STS
  - 1.5 Obtain common header parameters
  - 1.6 Obtain NAS SDKs
- 2 Call examples for SDK for Java
  - 2.1 Getting started
  - 2.2 Use SDK
    - 2.2.1 Install NAS SDK for Java
    - 2.2.2 Configure authentication credentials
    - 2.2.3 Configure connection requests
    - 2.2.4 Initiate a request
    - 2.2.5 Handle errors
    - 2.2.6 Use CommonRequest to call API operations
- 3 Call examples for SDK for Python
  - 3.1 Getting started
  - 3.2 Use SDK
    - 3.2.1 Install the SDK for Python
    - 3.2.2 Configure authentication credentials
    - 3.2.3 Set HTTPS requests
    - 3.2.4 Initiate a request
    - 3.2.5 Handle errors
    - 3.2.6 Use CommonRequest to call API operations
- 4 API Reference
  - 4.1 List of operations by function
  - 4.2 Make API requests
    - 4.2.1 Common parameters
    - 4.2.2 Request syntax
  - 4.3 Regions
    - 4.3.1 DescribeRegions
    - 4.3.2 DescribeZones
  - 4.4 NAS file system
    - 4.4.1 CreateFileSystem
    - 4.4.2 DeleteFileSystem
    - 4.4.3 ModifyFileSystem
    - 4.4.4 DescribeFileSystems
  - 4.5 Mount target
    - 4.5.1 CreateMountTarget
    - 4.5.2 DeleteMountTarget
    - 4.5.3 DescribeMountTargets
    - 4.5.4 ModifyMountTarget
    - 4.5.5 DescribeMountedClients
  - 4.6 Permission group
    - 4.6.1 CreateAccessGroup
    - 4.6.2 DeleteAccessGroup
    - 4.6.3 ModifyAccessGroup
    - 4.6.4 DescribeAccessGroups
    - 4.6.5 CreateAccessRule
    - 4.6.6 DeleteAccessRule
    - 4.6.7 ModifyAccessRule
    - 4.6.8 DescribeAccessRules
  - 4.7 Quotas
    - 4.7.1 SetDirQuota
    - 4.7.2 CancelDirQuota
    - 4.7.3 DescribeDirQuotas
  - 4.8 Unified namespaces
    - 4.8.1 CreateNamespace
    - 4.8.2 DeleteNamespace
    - 4.8.3 ModifyNamespace
    - 4.8.4 DescribeNamespaces
    - 4.8.5 AddFileSystemToNamespace
    - 4.8.6 RemoveFileSystemFromNamespace
    - 4.8.7 RenameMappedPathInNamespace
    - 4.8.8 ListFileSystemsInNamespace
    - 4.8.9 CreateNamespaceMountTarget
    - 4.8.10 DeleteNamespaceMountTarget
    - 4.8.11 ModifyNamespaceMountTarget
    - 4.8.12 DescribeNamespaceMountTargets
    - 4.8.13 AddNamespaceToGroup
    - 4.8.14 RemoveNamespaceFromGroup
    - 4.8.15 DescribeNamespaceGroup
  - 4.9 Lifecycle management
    - 4.9.1 CreateLifecyclePolicy
    - 4.9.2 DeleteLifecyclePolicy
    - 4.9.3 ModifyLifecyclePolicy
    - 4.9.4 DescribeLifecyclePolicies
  - 4.10 NFS NAS ACL
    - 4.10.1 EnableNfsAcl
    - 4.10.2 DisableNfsAcl
    - 4.10.3 DescribeNfsAcl
  - 4.11 Appendix: Error codes

## 1 Preparations

### 1.1 Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A web browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password from an operations administrator.

**Note**

The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types: Letters Digits Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)
3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

**Note**

For more information, see the **Bind a virtual MFA device to enable MFA** topic in
**Apsara Uni-manager Management Console User Guide** .
5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.

### 1.2 Obtain the information and the endpoint of an API operation

**the endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter
on the Parameter tab.

### 1.3 Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you call an API operation. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. Access credentials can be assigned to request senders by RAM or STS: RAM: assigns an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. STS: assigns an access credential that consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an access credential assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the headers for access control. Otherwise, an error that indicates insufficient permissions may occur. The following table describes the headers.

**Warning**

The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you want to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator to ensure security.

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which an operation is performed. You can obtain the ID of an File Storage NAS (NAS) file system from the NAS file system list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

**Note**

The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.4 Obtain an access credential assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call Apsara Stack API operations.

**Background information**

STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call Apsara Stack API operations. To call API operations in Apsara Stack by using STS, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS.

**Procedure**

1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click
**Personal Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain an access credential assigned by STS.

**Note**

In the following sample code, replace the variables with the actual values. Delete the angle brackets <> from the final code.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    // Specify the region ID, AccessKey ID, and AccessKey secret.
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
    // Obtain an access credential assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace sts.aliyuns.com with the endpoint of STS. The endpoint of STS is in th
e sts-vpc.${global:region}.${global:internet-domain} format.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role
in the preceding step.
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

3. Use the access credential assigned by STS to call an API operation of a cloud service. The
following sample code shows how to call the `DescribeRegions` operation of File Storage NAS (NAS).

**Note**

In the following sample code, replace the variables with the actual values. Delete the angle brackets <> from the final code.

```xml
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret obtained in the preceding step.
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
    // Replace "<yourRegionID>" with the actual region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token obtained in the preceding ste
```

`p.`

```java
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace "<yourResourceGroupID>" with the actual resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace "<yourOrganizationID>" with the actual organization ID.
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

### 1.5 Obtain common header parameters

**parameters**

You must specify multiple request headers when you call Apsara Stack API operations. This topic describes the common request headers and how to obtain the values of the request headers. This topic also describes the return values of specific parameters after you call API operations.

**Common request headers**

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. For more information about how to obtain region IDs, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the file system on which you want to perform operations. For more information about how to obtain file system IDs, see Obtain a file system ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

Call an operation to obtain an organization ID. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

Call an operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain a file system ID**

You can obtain the ID of an File Storage NAS (NAS) file system in the Apsara Uni-manager Management Console. Perform the following steps to obtain a file system ID:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Storage** > **NAS**.
3. In the left-side navigation pane, click **File System List**.
4. On the **File System List** page, view the ID of the NAS file system.
The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of Apsara Stack services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The organization name. |
| Department | The organization ID. |

### 1.6 Obtain NAS SDKs

When you call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK of your cloud service. This topic describes how to obtain File Storage NAS SDKs. An SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. The SDKs for Java, Python, and Go are provided. You can obtain the SDKs from Apsara Stack SDKs based on your business requirements.

**Note**

We recommend that you use an SDK for Java or Python. If you use SDKs in other programming languages, the SDKs may be incompatible with your system. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack. The following table provides links to the references and GitHub source code of NAS SDKs for different programming languages.

| Programming language | GitHub source code |
|---|---|
| Java | NAS SDK for Java |
| Python | NAS SDK for Python |

or SDK for Java

## 2 Call examples for SDK for Java

**Java**

### 2.1 Getting started

This topic describes how to obtain and use File Storage NAS (NAS) SDK for Java.

**Prerequisites**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. The endpoint of NAS is obtained. For more information, see Obtain the information and the endpoint of an API operation. Java Development Kit (JDK) 1.8 or later is installed.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage Java projects, import JAR files to the pom.xml file of the projects.

**Note**

To use a NAS SDK, you must install the core library of Apsara Stack SDK for Java and NAS SDK for Java. We recommend that you use the core library V4.5.17 or later, and use NAS SDK for Java V2.0.2.

**Use Apsara Stack SDK for Java**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and specify the required parameters.
3. Initiate the API request and handle the response or exceptions.

**Note**

In the following sample code, replace the variables with the actual values. Delete the angle brackets <> in the final code.

```java
import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsRequest; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsResponse; public class Main {
    public static void main(String[] args) {
       // Create and initialize a DefaultAcsClient instance.
       DefaultProfile profile = DefaultProfile.getProfile(
           "<yourRegionID>",          // Replace the variable with your region ID.
```

or SDK for Java

```
           "<yourAccessKeyID>",      // Replace the variable with your AccessKey ID.
           "<yourAccessKeySecret>"); // Replace the variable with your AccessKey
secret.
       // Specify the endpoint of the service. Replace the variables with the actual
values.
       profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
       // Configure the request parameters.
       HttpClientConfig clientConfig = HttpClientConfig.getDefault();
       clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate.
       clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the read
timeout period. Unit: milliseconds.
       clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Spec
ify the connection timeout period. Unit: milliseconds.
       clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify
the maximum number of requests for each host.
       clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum nu
mber of requests.
       clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the requ
est protocol. Default value: HTTP.
       /* Optional. Specify the IP address and port of the proxy.
       clientConfig.setHttpProxy("http://192.168.XX.XX:33XX");
```

`or`

```
       clientConfig.setHttpsProxy("https://192.168.XX.XX:33XX");
```

`*/`

```java
       profile.setHttpClientConfig(clientConfig);
       IAcsClient client = new DefaultAcsClient(profile);
       // Create an API request and specify the request parameters.
       DescribeFileSystemsRequest request = new DescribeFileSystemsRequest();
       // Business parameters.
       request.setPageSize(10);
       request.setPageNumber(1);
       // The header parameters that are used for resource isolation. Replace the val
ues with your organization ID and resource set ID.
       request.putHeadParameter("x-acs-organizationid", "1");
       request.putHeadParameter("x-acs-resourcegroupid", "11");
       // Initiate the request and handle the response or exceptions.
       DescribeFileSystemsResponse response;
       try {
           response = client.getAcsResponse(request);
           for (DescribeFileSystemsResponse.FileSystem
fileSystem:rsp.getFileSystems()) {
               System.out.println(fileSystem.getFileSystemId());
       } catch (ServerException e) {
           e.printStackTrace();
       } catch (ClientException e) {
           e.printStackTrace();
```

### 2.2 Use SDK

or SDK for Java

#### 2.2.1 Install NAS SDK for Java

This topic describes how to install NAS SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, see Alibaba Cloud SDKs. To use a NAS SDK, you must install the core library of Apsara Stack SDK for Java and NAS SDK for Java. We recommend that you use the core library V4.5.17 or later, and use NAS SDK for Java V2.0.2. To use NAS SDK for Java, you must install the core library of Apsara Stack SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDKs.

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

#### 2.2.2 Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports authentication based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

**Note**

Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly-accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace the variable with your region ID.
    "<yourAccessKeyID>",      // Replace the variable with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace the variable with your AccessKey secret.
```

or SDK for Java

**Note**

In the preceding sample code, replace the variables with the actual values. Delete the angle brackets (<>) from the final code.

#### 2.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

**Note**

You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code. The following list describes the variables: <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds. <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds. <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER. <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER. <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy. or SDK for Java

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGE
```

`R.`

```
clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following code is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 2.2.4 Initiate a request

This topic describes how to use the SDK for Java to initiate a request.

**Procedure**

1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
Name the request in the ${apiName}Request format. Replace **${apiName}** with the name of the API operation, for example, DescribeFileSystems. When multiple service SDKs are used, different requests may have the same name. You can differentiate the requests based on package names.

```
DescribeFileSystemsRequest request = new DescribeFileSystemsRequest(); // Business parameters. request.setFileSystemType("all"); request.setPageSize(10); // The header parameters that are used for resource isolation. Replace the values wit h your actual organization ID and resource set ID. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. Initiate the request and handle the response.
or SDK for Java

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
```

In normal cases, all returned fields are deserialized into the response. You can call `response.getXXX()` to obtain the values of the response fields.

```
instanceStatus = response.getStatus();
```

However, if an exception occurs or you need to obtain the original HTTP response, call `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### 2.2.5 Handle errors

If an error occurs on the server or SDK when you use the SDK for Java, an error response is returned. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by the SDK for Java. You only need to handle the errors returned by the server based on the error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

The following sample code shows how to handle SDK errors: or SDK for Java

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
}catch (ServerException e){
    // Add a computing logic for handling errors.
    // For example, you can display the exception information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, submit a ticket that includes the request ID (RequestId)
to request technical support.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your logic for handling exceptions.
    // For example, you can display the exception information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

#### 2.2.6 Use CommonRequest to call API operations

**operations**

If you want to call the API operations of a cloud service that does not provide SDKs, or the requests and responses of API operations that you call by using an SDK do not meet your business requirements, you can use CommonRequest to call API operations. CommonRequest supports all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API reference of File Storage NAS (NAS). Domain: the endpoint of NAS. Version: the API version, which is in the YYYY-MM-DD format. You can find the API version of a service in the Common parameters section of the API reference. Operation information: the name of the API operation that you want to call. You need to obtain the **Action** parameter and specify the API operation name in the format

```
of request.setSysAction("<Action>") .
```

or SDK for Java For example, if you want to call the CreateFileSystem operation, you must use `request.setSysAction("CreateFileSystem")` to specify the API operation when you initiate a CommonRequest request.

**Call a remote procedure call (RPC) API operation**

This example shows how to call the DescribeFileSystems operation to query file systems.

**Note**

In the following sample code, replace the variables with the actual values. Delete the angle brackets (<>) from the final code. Variables: <yourRegionID>: Replace the variable with your region ID. <yourAccessKeyID>: Replace the variable with your AccessKey ID. <yourAccessKeySecret>: Replace the variable with your AccessKey secret. <yourSecurityToken>: Replace the variable with your security token. <yourResourceGroupID>: Replace the variable with your resource set ID. <yourOrganizationID>: Replace the variable with your organization ID. <yourInstanceID>: Replace the variable with your instance ID. <http://192.168.XX.XX:33XX>: Replace the variable with your IP address and port of the proxy.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; class DescribeFileSystems {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
                "<yourRegionID>",          // Replace the variable with your region ID.
                "<yourAccessKeyID>",      // Replace the variable with your AccessKey ID
```

`.`

```
                "<yourAccessKeySecret>"); // Replace the variable with your AccessKey se
cret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
         Configure the HTTP proxy based on your business requirements.
         To configure HTTP proxy, perform the following steps:
         clientConfig.setHttpProxy("http://192.168.XX.XX:33XX");
```

`S` `if` `h` `dd` `d` `f` `h` or SDK for Java

```
         Specify the IP address and port of the proxy.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the endpoint of the required service.
        request.setSysDomain("nas.cn-hangzhou.com");
        request.setSysProduct("NAS");
        request.setSysVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "10");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// O
ptional. Specify the resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Specify the organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Specify the source of the API call.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional.
Specify the region ID. This parameter is required if you use Apsara Stack Enterprise V3 .15.0 or earlier.
         request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional.
Specify the instance ID. This parameter is required if you want to modify, delete, or q uery an instance.
        /**
         When you use a Security Token Service (STS) AccessKey 3-tuple to call an API o
peration, you must add the SecurityToken field in the request parameters.
         Format:
         request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
         Specify your security token.
```

`*/`

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
```

or SDK for Python

## 3 Call examples for SDK for Python

**Python**

### 3.1 Getting started

This topic describes how to obtain and use File Storage NAS (NAS) SDK for Python.

**Prerequisites**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. The endpoint of NAS is obtained. For more information, see Obtain the information and the endpoint of an API operation.

**Install Apsara Stack SDK for Python**

1. Install the SDK core library.
If you use Python 2.x, run the following command to install the SDK core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install NAS SDK for Python.
If you use Python 2.x, run the following command to install NAS SDK:

```
pip install aliyun-python-sdk-nas
```

If you use Python 3.x, run the following command to install NAS SDK:

```
pip3 install aliyun-python-sdk-nas
```

**Use NAS SDK for Python**

To use NAS SDK for Python, perform the following steps:
1. Create a client instance. Before you create a client instance, you must obtain a region ID,
an AccessKey ID, and an AccessKey secret.
2. Create an API request and specify the required parameters.
3. Initiate the request and handle the response or exceptions.
or SDK for Python

```python
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
# global config
region_id = '<yourRegionID>' # Replace the variable with your region ID. access_key = '<yourAccessKeyID>' # Replace the variable with your AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Replace the variable with your AccessKey se cret.
# product config
product_name = 'NAS' # Specify the service name. endpoint = 'nas.aliyuns.com' # Specify the endpoint of the service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print(response)
```

### 3.2 Use SDK

#### 3.2.1 Install the SDK for Python

This topic describes how to install Alibaba Cloud SDK for Python and File Storage NAS SDK for Python.
1. Install Alibaba Cloud SDK for Python.
Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

**Note**

To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. For example, if you want to use NAS SDK for Python, you must install the SDK core library for Python and NAS SDK for Python. If you use Python 2.x, run the following command to install the SDK core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install NAS SDK for Python.
If you use Python 2.x, run the following command to install NAS SDK for Python: or SDK for Python

```
pip install aliyun-python-sdk-nas
```

If you use Python 3.x, run the following command to install NAS SDK for Python:

```
pip3 install aliyun-python-sdk-nas
```

#### 3.2.2 Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDK for Python supports authentication based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

**Important**

Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly-accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
clt = client.AcsClient(access_key, access_secret, region_id)
```

#### 3.2.3 Set HTTPS requests

The Python SDK supports using HTTP and HTTPS to initiate API requests. When using the Python SDK, you can specify a protocol (HTTP or HTTPS) for a specific request to use, or set a global default protocol for all requests to use.

**Note**

The default protocol (HTTP or HTTPS) of a product takes precedence over the global default protocol you set.

**Add OpenSSL dependency**

HTTPS of the Python SDK depends on the OpenSSL support in Python. To use Alibaba Cloud SDK to send HTTPS requests, you must add OpenSSL support in Python.

| python -c "import ssl" |   | command to chec |
|---|---|---|
| L. If the |   |   |

OpenSSL is supported in Python. If Python does not support OpenSSL, run the following command to install OpenSSL:

```
pip install pyopenssl
```

**Set HTTP/HTTPS for a request**

See the following code example for reference to set the HTTPS call for an API:

```bash
request = CreateInstanceRequest.CreateInstanceRequest() request.set_protocol_type("https")
# Value: "https" or "http"
```

or SDK for Python

**Set global default protocol for all requests**

See the following code example for reference to set the global default protocol for all requests:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 3.2.4 Initiate a request

This topic describes how to use File Storage NAS SDK for Python to initiate a request.

**Procedure**

1. Import NAS SDK for Python.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
```

2. Create an AcsClient instance.

```
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. Create a request object.

```
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest() request.set_accept_format('json')
```

4. Initiate the request and handle the response.

```python
response = clt.do_action_with_exception(request) print(response)
```

#### 3.2.5 Handle errors

If the server or SDK encounters an error when you use the SDK for Python, the SDK returns an error response. The error response contains an error code and an error message. Among the errors returned by the SDK for Python, you do not need to handle the SDK errors, but must solve the server errors. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message:

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: or SDK for Python

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # You can add your error handling logic here.
    # For example, display the error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### 3.2.6 Use CommonRequest to call API operations

**operations**

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API reference of File Storage NAS. Domain: the endpoint of NAS. Version: the version number of the API, in the YYYY-MM-DD format. You can obtain the API version in the Common parameters topic of the API reference. Operation information: the name of the API operation that you want to call. You need to obtain the value of the **Action** parameter and specify an API operation in

```
 request.set_action_name("Action") .
```

For example, if you want to call the CreateFileSystem operation, you must use `request.set_action_name("CreateFileSystem")` to specify the API operation when you initiate a CommonRequest request.

**Example: Call an RPC API operation**

This example shows how to call the DescribeFileSystems operation to query file systems. or SDK for Python

**Note**

In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code. You need to configure the following variables: <yourRegionID>: Replace the parameter with the region ID. <yourAccessKeyID>: Replace the parameter with your AccessKey ID. <yourAccessKeySecret>: Replace the parameter with your AccessKey secret. <yourSecurityToken>: Replace the parameter with your security token. <yourResourceGroupID>: Replace the parameter with the resource set ID. <yourOrganizationID>: Replace the parameter with the organization ID. <yourInstanceID>: Replace the parameter with the instance ID. or SDK for Python

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('NAS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26') request.set_domain('<nas.aliyuncs.com>') # Specify the endpoint of the service.
# or:
# request = = CommonRequest(product='NAS',
action_name='DescribeFileSystems',version='2017-06-26',domain='nas.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS as the protocol:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber','1') request.add_query_param('PageSize','30')
######
# When you use an STS AccessKey 3-tuple to call an API operation, you must add the Secu
rityToken field in the request parameters.
# Format:
# Specify your security token.
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Specify the source of the API call.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Specify the region ID. If you use Apsara Stack Enterprise V3.15.0 or earlie
r, this parameter is required. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. If you need to delete, modify, or query an instanc
e, this parameter is required.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

## 4 API Reference

### 4.1 List of operations by function

The API operations table lists the API operations that are available for use in File Storage NAS (NAS). Table 1. API operations

| Category | API operation | Description |
|---|---|---|
| Region | DescribeRegions | Queries all region IDs. |
|   | DescribeZones | Queries all zones in a region and the file system types that are supported in each zone. |
| File system | CreateFileSystem | Creates a file system. |
|   | DeleteFileSystem | Deletes a file system. |
|   | DescribeFileSystems | Queries file systems. |
|   | ModifyFileSystem | Modifies the description of a file system. |
| Mount target | CreateMountTarget | Creates a mount target. |
|   | DeleteMountTarget | Deletes a mount target. |
|   | DescribeMountTargets | Queries mount targets. |
|   | ModifyMountTarget | Modifies a mount target. |
|   | DescribeMountedClients | Queries the clients on which a file system is mounted. |
|   | CreateAccessGroup | Create a permission group. |
|   | DeleteAccessGroup | Deletes a permission group. |
|   | DescribeAccessGroups | Queries permission groups. |

| psara File Storage NA |   |   |
|---|---|---|
| Permission group |   |   |
|   | ModifyAccessGroup | Modifies a permission group. |
|   | CreateAccessRule | Creates a rule for a permission group. |
|   | DeleteAccessRule | Deletes a rule from a permission group. |
|   | DescribeAccessRules | Queries the information about rules in a permission group. |
|   | ModifyAccessRule | Modifies a rule in a permission group. |
| Quota | SetDirQuota | Creates a directory quota for a file system. |
|   | CancelDirQuota | Cancels the directory quotas of a file system. |
|   | DescribeDirQuotas | Queries the directory quotas of a file system. |
| Unified namespace | CreateNamespace | Creates a namespace. |
|   | DeleteNamespace | Deletes a namespace. |
|   | ModifyNamespace | Modifies a namespace. |
|   | DescribeNamespaces | Queries namespaces. |
|   | AddFileSystemToNamespace | Adds a file system to a namespace. |
|   | RemoveFileSystemFromNamespac | Deletes a file system from a namespace. |
|   | RenameMappedPathInNamespace | Modifies the mapping name of a file system in a namespace. |
|   | ListFileSystemsInNamespace | Queries the mapped file systems in a namespace. |

|   | CreateNamespaceMountTarget | Creates a mount target for a namespace. |
|---|---|---|
|   | DeleteNamespaceMountTarget | Deletes a mount target for a namespace. |
|   | ModifyNamespaceMountTarget | Modifies a mount target for a namespace. |
|   | DescribeNamespaceMountTargets | Queries the mount targets of a namespace. |
|   | AddNamespaceToGroup | Creates cross-domain mount orchestration. |
|   | RemoveNamespaceFromGroup | Deletes cross-domain mount orchestration. |
|   | DescribeNamespaceGroup | Queries the Cross-domain Mount Orchestration page. |
| Lifecycle management | CreateLifecyclePolicy | Creates a lifecycle policy. |
|   | DeleteLifecyclePolicy | Deletes a lifecycle policy. |
|   | ModifyLifecyclePolicy | Modifies a lifecycle policy. |
|   | DescribeLifecyclePolicies | Queries lifecycle policies. |
| NFS NAS ACL | EnableNfsAcl | Enables the Network File System (NFS) access control list (ACL) feature for a file system. |
|   | DisableNfsAcl | Disables the NFS ACL feature for a file system. |
|   | DescribeNfsAcl | Queries whether the NFS ACL feature is enabled for a file system. |

### 4.2 Make API requests

#### 4.2.1 Common parameters

**Common request parameters**

Common request parameters are required in all API requests. Table 1. Common request parameters

| Parameter | Type | Required |   | Description |   |   |
|---|---|---|---|---|---|---|
| Format | String | No |   | The format in which to return the response. Valid values: JSON and XML. Default value: JSON. |   |   |
| Version | String | Yes |   | The API version. The value is represented as a date in the YYYY-MM-DD format. The current API version is 2017- 06-26. |   |   |
| AccessKeyId | String | Yes |   | The AccessKey ID that is used to access services. For more information, see Obtain an AccessKey pair. |   |   |
| Signature | String | Yes |   | The signature string of the request. |   |   |
| SignatureMethod | String | Yes |   | The signature method. Set the value to HMAC-SHA1. |   |   |
| Timestamp | String | Yes |   | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time must be in UTC. Example: 2017-05- 26T12:00:00Z. |   |   |
|   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   | DDThh:mm:ssZ |   |   |
| SignatureVersion | String | Yes |   | The version of the signature encryption algorithm. Set the value to 1.0. |   |   |

| SecurityToken | String | No | The Security Token Service (STS) token. This parameter is required when STS is used. |
|---|---|---|---|
| SignatureNonce | String | No | A unique random number that is used to prevent replay attacks. You must use different numbers for different requests. |

```
GET https://nas.regionid.example.com/?Action=<Action> &Format=xml &Version=2017-06-26 &AccessKeyId=key-test &Signature=Pc5***%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &Timestamp=2012-06-01T12:00:00Z ...
```

**Common response parameters**

Every response returns a unique request ID (indicated by **RequestId**) regardless of whether the request is successful. Table 2. Common response parameters

| Parameter | Type | Description |
|---|---|---|
| RequestId | Integer | The unique ID of the request. |

```xml
<?xml version="1.0" encoding="UTF-8"?> <Operation Name + Response>
  <!--Return Request Tag-->
  <RequestId> 6D9F62C5-BF52-447C-AA34-C77F7AFCCC12</RequestId>
  <!--Return Result Data-->
</Operation Name + Response>
```

```json
  "RequestId": "4C467B38-3910-447D-87BC-AC049166F216",
  /* The returned data */
```

#### 4.2.2 Request syntax

**Endpoints**

The format of the endpoint for an File Storage NAS (NAS) API is described in Obtain the information and the endpoint of an API operation.

**Protocols**

You can use HTTP or HTTPS to send requests. We recommend that you use HTTPS to improve security.

**Request methods**

You can call an API operation by sending an HTTP GET request. If you use this method, the request parameters must be included in the request URL. In each request, you must set the Action parameter to specify the operation that you want to perform, for example, `DescribeRegions` . You must also specify the common request parameters and the operation-specific parameters.

**Character encoding**

All requests and responses are encoded in `UTF-8` .

### 4.3 Regions

#### 4.3.1 DescribeRegions

Queries available regions.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |

| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
|---|---|---|---|---|
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| Regions | Array of Region |   | The array of regions. |
| Region |   |   |   |
| LocalName | String | East China 1 | The name of the region. |
| RegionEndpoin t | String | nas.cn- hangzhou.aliyuncs. com | The endpoint of the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | A70BEE5D-76D3- 49FB-B58F- 1F398211**** | The ID of the request. |
| TotalCount | Integer | 4 | The total number of regions. |

```
http(s)://[Endpoint]/?Action=DescribeRegions
```

```json
<TotalCount>4</TotalCount> <PageSize>2</PageSize> <RequestId>A70BEE5D-76D3-49FB-B58F-1F398211****</RequestId> <PageNumber>1</PageNumber> <Regions>
    <RegionId>cn-hangzhou</RegionId>
    <RegionEndpoint>nas.cn-hangzhou.aliyuncs.com</RegionEndpoint>
    <LocalName>East China 1</LocalName>
</Regions>
    "TotalCount": 4,
    "PageSize": 2,
    "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211****",
    "PageNumber": 1,
    "Regions": {
        "RegionId": "cn-hangzhou",
        "RegionEndpoint": "nas.cn-hangzhou.aliyuncs.com",
        "LocalName": "East China 1"
```

#### 4.3.2 DescribeZones

Queries all zones in a region and the file system types that are supported in each zone.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeZones | The operation that you want to perform. Set the value to DescribeZones. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A70BEE5D-76D3- 49FB-B58F- 1F398211A5C3 | The request ID. |
| Zones | Array of Zone |   | The zones. |
| Zone |   |   |   |
| Capacity | List | 1 | The Capacity NAS file system. |
| Clusters | Array of Cluster |   | The queried clusters. |
| Cluster |   |   |   |
| ClusterId | String | StandarNasCluster | The cluster ID. |
| ClusterType | String | NAS | The cluster type. |
| ClusterVersion | String | 3.16.0 | The cluster version. |
| InstanceTypes | Array of InstanceType |   | The instance type. |
| InstanceType |   |   |   |
| ProtocolType | String | NFS | The protocol type. Valid value: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
| StorageType | String | Performance | The storage class. Valid values: Performance: Performance NAS file systems Capacity: Capacity NAS file systems |

| SupportedFeat ures | List | ["ACL","Quota","Lif ecycle","Namespac e"] | The advanced features supported by NAS. Valid values: ACL: access control lists (ACLs) Quota: quotas Lifecycle: lifecycle policies Namespace: unified namespaces |
|---|---|---|---|
| Performance | List | 0 | The Performance NAS file system. |
| ZoneId | String | cn-hangzhou-b | The zone ID. |

```xml
http(s)://[Endpoint]/?Action=DescribeZones &RegionId=cn-hangzhou <RequestId>A70BEE5D-76D3-49FB-B58F-1F398211A5C3</RequestId> <Zones>
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

```json
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
```

`},`

```json
        "Capacity": 1,
        "Performance": 0
```

**Error codes**

| HttpCod e | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The request failed due to an unknown error. Try again later. |
| 404 | InvalidRegionId.Not Found | The specified Region is not found. | The requested region does not exist or the query service is unavailable in this region. |

### 4.4 NAS file system

#### 4.4.1 CreateFileSystem

Creates a file system.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateFileSyste m | The operation that you want to perform. Set the value to CreateFileSystem. |

| ProtocolType | String | Yes | NFS | The type of the protocol. Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
|---|---|---|---|---|
| StorageType | String | Yes | Performance | The type of the storage. Valid values: Performance: Performance NAS file systems Capacity: Capacity NAS file systems |
| ZoneId | String | No | cn-hangzhou-b | The ID of the zone. Each region has multiple isolated locations known as zones. The power supply and network of each zone are independent. Note An Elastic Compute Service (ECS) instance can access a NAS file system in the same region but a different zone. We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance. |
| EncryptType | Integer | No | 1 | Specifies whether to encrypt the data in the file system. The EncryptType parameter is not supported. |
| Description | String | No | balabala | The description of the file system. Limits: The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |

| VolumeSize | Long | No | 100 | The capacity of the General-purpose NAS file system. Unit: bytes. Valid values: Valid values for Capacity NAS file systems: 0 to 10 PB. Valid values for Performance NAS file systems: 0 to 1 PB. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | The ID of the file system that is created. |
| RequestId | String | 98696EF0-1607- 4E9D-B01D- F20930B6**** | The ID of the request. |

```json
http(s)://[Endpoint]/?Action=CreateFileSystem &ProtocolType=NFS &StorageType=Performance <RequestId>98696EF0-1607-4E9D-B01D-F20930B6****</RequestId> <FileSystemId>1ca404****</FileSystemId>
    "RequestId": "98696EF0-1607-4E9D-B01D-F20930B6****",
    "FileSystemId": "1ca404****"
```

#### 4.4.2 DeleteFileSystem

Deletes a file system. Before you delete a file system, you must remove all the mount targets from the file system. After the file system is deleted, the data on the file system cannot be restored. Proceed with caution.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteFileSyste m | The operation that you want to perform. Set the value to DeleteFileSystem. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=DeleteFileSystem &FileSystemId=1ca404**** <RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId>
    "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****"
```

#### 4.4.3 ModifyFileSystem

Modifies the details of a file system.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyFileSyste m | The operation that you want to perform. Set the value to ModifyFileSystem. |
|---|---|---|---|---|
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| Description | String | No | N/A | The description of the file system. Limits: The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https://. The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |
| VolumeSize | Long | No | 1000 | The capacity of the file system. Valid values: Valid values for NAS Capacity file systems: 0 to 10 PB. Valid values for NAS Performance file systems: 0 to 1 PB. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=ModifyFileSystem &FileSystemId=1ca404**** <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId>
```

```json
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****"
```

#### 4.4.4 DescribeFileSystems

Queries file systems.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFileSy stems | The operation that you want to perform. Set the value to DescribeFileSystems. |
| FileSystemId | String | No | 109c04**** | The ID of the file system. |
| FileSystemTyp e | String | No | standard | The type of the file system. Valid value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |
| VpcId | String | No | vpc- bp1sevsgtqvk 5gxbl**** | The ID of the virtual private cloud (VPC). If you want to mount the file system on an Elastic Compute Service (ECS) instance, you must set this parameter to the VPC where the ECS instance resides. |
| PageSize | Integer | No | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| UseUTCDateTi me | Boolea n | No | true | Specifies whether the time to return is displayed in UTC. Valid values: true (default): The time is displayed in UTC. false: The time is not displayed in UTC. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integer | 1 | The number of entries per page. |
| RequestId | String | 035B3A3A-E514- 4B41-B906- 5D906CFB**** | The request ID. |
| TotalCount | Integer | 1 | The total number of file systems. |
| FileSystems | Array of FileSystem |   | The queried file systems. |
| FileSystem |   |   |   |
| Bandwidth | Long | 150 | The bandwidth of the file system. Unit: MB/s. This parameter is unavailable for General-purpose NAS file systems. |
| ChargeType | String | PayAsYouGo | The billing method. Valid values: Subscription: The subscription billing method is used. PayAsYouGo: The pay-as-you-go billing method is used. Package: A storage plan is attached to the file system. |
| CreateTime | String | 2017-05- 27T15:43:06CST | The time when the file system was created. |
| Description | String | This can be the description of the created file system. | The description of the file system. |
| EncryptType | Integer | 1 | Indicates whether the data in the file system is encrypted. Valid values: 0: The data is not encrypted. 1: The data is encrypted. |

| ExpiredTime | String | 1572174830000 | The time when the file system expires. |
|---|---|---|---|
| FileSystemId | String | 109c04**** | The ID of the file system. |
| FileSystemTyp e | String | all | The type of the file system. |
| MeteredIASize | Long | 1000 | The storage usage of the Infrequent Access (IA) storage class. |
| MeteredSize | Long | 1611661312 | The storage usage of the file system. The value of this parameter is the maximum storage usage of the file system within the previous hour. Unit: bytes. |
| MountTargets | Array of MountTarget |   | The queried mount targets. |
| MountTarget |   |   |   |
| AccessGroupN ame | String | test-001 | The name of the permission group that is attached to the mount target. |
| MountTargetD omain | String | 109c04****- w****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| NetworkType | String | vpc | The network type. Valid values: vpc: VPC classic: classic network |
| Status | String | active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. |
| VpcId | String | vpc- bp1sevsgtqvk5gxbl **** | The VPC ID. |

| VswId | String | vsw- bp1omfzsszekkvax n**** | The vSwitch ID. |
|---|---|---|---|
| Packages | Array of Package |   | The queried storage plans. |
| Package |   |   |   |
| ExpiredTime | String | 2020-01- 05T16:00:00Z | The time when the storage plan expires. |
| PackageId | String | naspackage- 0be9c4b624- 37**** | The ID of the storage plan. |
| PackageType | String | hybrid | The type of the storage plan. |
| Size | Long | 107374182400 | The capacity of the storage plan. |
| StartTime | String | 2019-12- 05T01:40:56Z | The start time of the validity period for the storage plan. |
| ProtocolType | String | NFS | The protocol type of the file system. Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
| QuotaSize | Long | 100 | The capacity of the file system. |
| RegionId | String | cn-hangzhou | The region ID. |

| Status | String | Pending | The status of the file system. Valid values: Pending: The file system is being created or modified. Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state. Stopped: The file system is unavailable. Extending: The file system is being scaled up. Stopping: The file system is being stopped. Deleting: The file system is being deleted. |
|---|---|---|---|
| StorageType | String | Performance | The storage class. Valid values: Capacity: Capacity NAS file systems Performance: Performance NAS file systems |
| SupportedFeat ures | List | Lifecycle | The feature that is supported by the file system. Valid values: Lifecycle: lifecycle management Quota: quota management |
| VolumeSize | Long | 1000 | The capacity of the General-purpose NAS file system. Valid values: Valid values for Capacity NAS file systems: 0 to 10 PB. Valid values for Performance NAS file systems: 0 to 1 PB. |
| ZoneId | String | cn-hangzhou-b | The ID of the zone where the file system resides. |

```
http(s)://[Endpoint]/?Action=DescribeFileSystems
```

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
        <MountTargetDomain>109c04****-w****.cn-
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

| { "FileSystems": [ { "Status": "Pending", "StorageType": "Performance", "Description": "This can be the description of the created file system.", "ZoneId": "cn-hangzhou-b", "MeteredIASize": 1000, "CreateTime": "2017-05-27T15:43:06CST", "QuotaSize": 100, "MeteredSize": 1611661312, "EncryptType": 1, "ChargeType": "PayAsYouGo", "ProtocolType": "NFS", "Bandwidth": 150, "FileSystemType": "all", "ExpiredTime": 1572174830000, "FileSystemId": "109c04****", "RegionId": "cn-hangzhou", "VolumeSize": 1000 }, { "MountTargets": { "Status": "active", "VswId": "vsw-bp1omfzsszekkvaxn****", "VpcId": "vpc-bp1sevsgtqvk5gxbl****", "MountTargetDomain": "109c04****-w****.cn-hangzhou.nas.aliyuncs.com", "NetworkType": "vpc", "AccessGroupName": "test-001" }, "Packages": { "StartTime": "2019-12-05T01:40:56Z", "PackageId": "naspackage-0be9c4b624-37****", "Size": 107374182400, "ExpiredTime": "2020-01-05T16:00:00Z", "PackageType": "hybrid" } }, { "SupportedFeatures": "Lifecycle" }, { "Ldap": { "SearchBase": "dc=example", "URI": "ldap://ldap.example.example", "BindDN": "cn=alibaba,dc=com" } } ], "TotalCount": 1, "PageSize": 1, "RequestId": "035B3A3A-E514-4B41-B906-5D906CFB****", "PageNumber": 1 } |   |
|---|---|

### 4.5 Mount target

#### 4.5.1 CreateMountTarget

Creates a mount target.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMountTar get | The operation that you want to perform. Set the value to CreateMountTarget. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPC) and DEFAULT CLASSIC GROUP NAME _ _ _ (the default permission group for the classic network). |
| FileSystemId | String | Yes | 174494**** | The ID of the file system. |
| NetworkType | String | Yes | VPC | The network type of the mount target. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
| VpcId | String | No | vpc- 2zesj9afh3y518 k9o**** | The ID of the VPC. This parameter is valid and required if the mount target resides in a VPC. |
| VSwitchId | String | No | vsw- 2zevmwkwyztju offg**** | The ID of the vSwitch. This parameter is valid and required if the mount target resides in a VPC. |
| SecurityGroupId | String | No | sg- bp1fg655nh68x yz9**** | The ID of the security group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| RequestId | String | 70EACC9C-D07A- 4A34-ADA4- 77506C42**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=CreateMountTarget &AccessGroupName=classic-test &FileSystemId=174494**** &NetworkType=VPC <RequestId>70EACC9C-D07A-4A34-ADA4-77506C42****</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
    "RequestId": "70EACC9C-D07A-4A34-ADA4-77506C42****",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
```

#### 4.5.2 DeleteMountTarget

Deletes a mount target. After you delete a mount target, the mount target cannot be restored. Proceed with caution.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMountTar get | The operation that you want to perform. Set the value to DeleteMountTarget. |

| FileSystemId | String | Yes | 174494**** | The ID of the file system. |
|---|---|---|---|---|
| MountTargetDo main | String | Yes | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=DeleteMountTarget &FileSystemId=174494**** &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId>
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****"
```

#### 4.5.3 DescribeMountTargets

Queries the information of mount targets.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMountT argets | The operation that you want to perform. Set the value to DescribeMountTargets. |

| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
|---|---|---|---|---|
| MountTargetDo main | String | No | 1ca404a666- x****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargets | Array of MountTarget |   | The list of mount targets. |
| MountTarget |   |   |   |
| AccessGroup | String | DEFAULT VPC GRO _ _ UP NAME _ | The name of the permission group that is attached to the mount target. |
| MountTargetD omain | String | 1ca404a666- w****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| NetworkType | String | Vpc | The network type of the mount target. |
| Status | String | Active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. Note A file system can be mounted only if the file system is in the Active state. |
| VpcId | String | vpc- 2zesj9afh3y518k9o **** | The ID of the virtual private cloud (VPC). |

| VswId | String | vsw- 2zevmwkwyztjuoff g**** | The ID of the vSwitch. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | The ID of the request. |
| TotalCount | Integer | 1 | The total number of mount targets. |

```xml
http(s)://[Endpoint]/? Action=DescribeMountTargets &FileSystemId=1ca404**** <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>3BAB90FD-B4A0-48DA-9F09-2B963510A0EF</RequestId> <PageNumber>1</PageNumber> <MountTargets>
    <Status>Active</Status>
    <VswId>vsw-2zevmwkwyztjuoffg****</VswId>
    <VpcId>vpc-2zesj9afh3y518k9o****</VpcId>
    <MountTargetDomain>1ca404a666-w****.cn-
hangzhou.nas.aliyuncs.com</MountTargetDomain>
    <AccessGroup>DEFAULT_VPC_GROUP_NAME</AccessGroup>
    <NetworkType>Vpc</NetworkType>
</MountTargets>
```

```json
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
```

#### 4.5.4 ModifyMountTarget

Modifies a mount target.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyMountTar get | The operation that you want to perform. Set the value to ModifyMountTarget. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| MountTargetDo main | String | Yes | 1ca404a666- w****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |
| AccessGroupNa me | String | No | classic-test | The name of the permission group that is attached to the mount target. |
| Status | String | No | Inactive | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. |

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | FF387D95-34C4- 4879-B65A- 99D1FA1**** | The ID of the request. |
|---|---|---|---|

```json
http(s)://[Endpoint]/? Action=ModifyMountTarget &FileSystemId=1ca404**** &MountTargetDomain=1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com <RequestId>FF387D95-34C4-4879-B65A-99D1FA1****</RequestId>
    "RequestId": "FF387D95-34C4-4879-B65A-99D1FA1****"
```

#### 4.5.5 DescribeMountedClients

Queries the clients on which a file system is mounted.

**Request headers**

The DescribeMountedClients operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Query | Yes | cn-hangzhou-balbala | The region ID. |
| FileSyste mId | Strin g | Query | Yes | 1ca404**** | The ID of the file system. |
| MountTar getDomai n | Strin g | Query | Yes | 1ca404a666-x****.cn- hangzhou.nas.aliyuncs.c om | The domain name of the mount target. |
| ClientIP | Strin g | Query | No | 192.**.16.17 | The IP address of the client. |

| psara File St | orage NA | S |   | Dev | eloper Guide·API Referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| PageSize | Integ er | Query | No | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Clients | Array | 192.***.6.17 | The IP addresses of the mounted clients. |
| -ClientIP | String | 192.***.6.17 | The IP address of the client. |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | The request ID. |
| TotalCount | Integer | 3 | The total number of entries returned. |
| PageSize | Integer | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | 1 | The page number. Pages start from page 1. Default value: 1. |

```
http(s)://[Endpoint]/?Action=DescribeMountedClients &RegionId=cn-hangzhou-balbala &FileSystemId=1ca404**** &MountTargetDomain=1ca404a666-x****.cn-hangzhou.nas.aliyuncs.com
```

```json
  "TotalCount": 10,
  "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211****",
  "PageSize": 10,
  "PageNumber": 1,
  "Clients": {
    "Client": [
        "ClientIP": "10.10.10.1"
```

`]`

### 4.6 Permission group

#### 4.6.1 CreateAccessGroup

Creates a permission group.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessGr oup | The operation that you want to perform. Set the value to CreateAccessGroup. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ The name of the permission group must be different from the name of the default permission groups. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPC) and DEFAULT CLASSIC GROUP NAME _ _ _ (the default permission group for the classic network). |

| AccessGroupTyp e | String | Yes | Classic | The type of the permission group. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
|---|---|---|---|---|
| Description | String | No | classictestacces sgroup | The description of the permission group. Limits: By default, the description of a permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length. The description must start with a letter and cannot start with http:// or https://. The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessGroupN ame | String | classic-test | The name of the permission group. |
| RequestId | String | 55C5FFD6-BF99- 41BD-9C66- FFF39189**** | The ID of the request. |

```xml
http(s)://[Endpoint]/? Action=CreateAccessGroup &AccessGroupName=classic-test &AccessGroupType=Classic <RequestId>55C5FFD6-BF99-41BD-9C66-FFF39189****</RequestId> <AccessGroupName>classic-test</AccessGroupName>
```

```json
    "RequestId": "55C5FFD6-BF99-41BD-9C66-FFF39189****",
    "AccessGroupName": "classic-test"
```

#### 4.6.2 DeleteAccessGroup

Deletes a permission group. Default permission groups include DEFAULT_VPC_GROUP_NAME and DEFAULT_CLASSIC_GROUP_NAME. You cannot delete the default permission groups.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessGr oup | The operation that you want to perform. Set the value to DeleteAccessGroup. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | The ID of the request. |

```
http(s)://[Endpoint]/? Action=DeleteAccessGroup &AccessGroupName=classic-test
```

```json
<RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId>
    "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****"
```

#### 4.6.3 ModifyAccessGroup

Modifies a permission group.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccessGr oup | The operation that you want to perform. Set the value to ModifyAccessGroup. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, underscores ( ), and _ hyphens (-). |
| Description | String | No | classic-test | The description of the permission group. Limits: By default, the description of the permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length. The description must start with a letter and cannot start with http:// or https:// . The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |

| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ED2AE737-9D50- 4CA4-B0DA- 31BD610C**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=ModifyAccessGroup &AccessGroupName=classic-test <RequestId>ED2AE737-9D50-4CA4-B0DA-31BD610C****</RequestId>
    "RequestId": "ED2AE737-9D50-4CA4-B0DA-31BD610C****"
```

#### 4.6.4 DescribeAccessGroups

Queries the information of permission groups.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccess Groups | The operation that you want to perform. Set the value to DescribeAccessGroups. |
| AccessGroupNa me | String | No | classic-test | The name of the permission group. |

| PageSize | Integer | No | 2 | The number of entries to return per page. Valid values: 1 to 100. Default value: 10. |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| UseUTCDateTim e | Boolean | No | true | Specifies whether the time to return is in UTC. Valid values: true: the default value. The time is returned in the UTC format. false: The time is not returned in the UTC format. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessGroups | Array of AccessGroup |   | The list of permission groups. |
| AccessGroup |   |   |   |
| AccessGroupN ame | String | classic-test | The name of the permission group. |
| AccessGroupT ype | String | Classic | The type of the permission group. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
| Description | String | This is a classic test access group~ | The description of the permission group. |
| MountTargetC ount | Integer | 0 | The number of mount targets to which the permission group is attached. |

| RuleCount | Integer | 0 | The total number of rules in the permission group. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| RequestId | String | 2514F97E-FFF0- 4A1F-BF04- 729CEAC64B6F | The ID of the request. |
| ResourceOwne rId | String | 258456 | The ID of the resource. |
| TotalCount | Integer | 2 | The total number of permission groups. |

```xml
http(s)://[Endpoint]/? Action=DescribeAccessGroups <AccessGroups>
    <RuleCount>0</RuleCount>
    <AccessGroupType>Classic</AccessGroupType>
    <Description>This is a classic test access group~</Description>
    <MountTargetCount>0</MountTargetCount>
    <AccessGroupName>classic-test</AccessGroupName>
</AccessGroups> <TotalCount>2</TotalCount> <PageSize>2</PageSize> <RequestId>2514F97E-FFF0-4A1F-BF04-729CEAC64B6F</RequestId> <PageNumber>1</PageNumber> <ResourceOwnerId>258456</ResourceOwnerId>
```

```json
    "AccessGroups": {
        "RuleCount": 0,
        "AccessGroupType": "Classic",
        "Description": "This is a classic test access group~",
        "MountTargetCount": 0,
        "AccessGroupName": "classic-test"
```

`},`

```json
    "TotalCount": 2,
    "PageSize": 2,
    "RequestId": "2514F97E-FFF0-4A1F-BF04-729CEAC64B6F",
    "PageNumber": 1,
    "ResourceOwnerId": 258456
```

#### 4.6.5 CreateAccessRule

Creates a rule for a permission group.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessRul e | The operation that you want to perform. Set the value to CreateAccessRule. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. |
| SourceCidrIp | String | Yes | 10.0.*. */** | The IP address or CIDR block of the authorized object. It must be an IP address or CIDR block. Note If the permission group resides in the classic network, only IP addresses are supported. |
| RWAccessType | String | No | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates read and write permissions. RDONLY: the read-only permissions. |

| UserAccessType | String | No | no squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash: allows access from _ root users to the file system. root squash: grants root users the _ least permissions as the nobody user. all squash: grants all users the _ least permissions as the nobody user. The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system. |
|---|---|---|---|---|
| Priority | Integer | No | 1 | The priority of the rule. The rule with the highest priority takes effect if multiple rules are attached to the authorized object. Valid values: 1 to 100. The value 1 indicates the highest priority. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessRuleId | String | 1 | The ID of the rule. |
| RequestId | String | A323836B-5BC6- 45A6-8048- 60675C23**** | The ID of the request. |

```
http(s)://[Endpoint]/? Action=CreateAccessRule &AccessGroupName=classic-test &SourceCidrIp=10.0. *. */**
```

```json
<RequestId>A323836B-5BC6-45A6-8048-60675C23****</RequestId> <AccessRuleId>1</AccessRuleId>
    "RequestId": "A323836B-5BC6-45A6-8048-60675C23****",
    "AccessRuleId": 1
```

#### 4.6.6 DeleteAccessRule

Deletes a rule from a permission group.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessRul e | The operation that you want to perform. Set the value to DeleteAccessRule. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. |
| AccessRuleId | String | Yes | 1 | The ID of the rule. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5B4511A7-C99E- 4071-AA8C- 32E2529D**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=DeleteAccessRule &AccessGroupName=classic-test &AccessRuleId=1 <RequestId>5B4511A7-C99E-4071-AA8C-32E2529D****</RequestId>
    "RequestId": "5B4511A7-C99E-4071-AA8C-32E2529D****"
```

#### 4.6.7 ModifyAccessRule

Modifies a rule in a permission group.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccessRul e | The operation that you want to perform. Set the value to ModifyAccessRule. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. |
| AccessRuleId | String | Yes | 1 | The ID of the rule. |
| SourceCidrIp | String | No | 192.1**. *. * | The IP address or CIDR block of the authorized object. It must be an IP address or CIDR block. Note If the permission group resides in the classic network, only IP addresses are supported. |

| RWAccessType | String | No | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates the read and write permissions. RDONLY: the read-only permissions. |
|---|---|---|---|---|
| UserAccessType | String | No | all squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash: allows access from _ root users to the file system. root squash: grants root users the _ least permissions as the nobody user. all squash: grants all users the _ least permissions as the nobody user. The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system. |
| Priority | Integer | No | 1 | The priority of the rule in the permission group. Valid values: 1 to 100. Default value: 1, which indicates the highest priority. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6299428C-3861- 435D-AE54- 9B330A00**** | The ID of the request. |

```json
http(s)://[Endpoint]/? Action=ModifyAccessRule &AccessGroupName=classic-test &AccessRuleId=1 <RequestId>6299428C-3861-435D-AE54-9B330A00****</RequestId>
    "RequestId": "6299428C-3861-435D-AE54-9B330A00****"
```

#### 4.6.8 DescribeAccessRules

Queries the information about rules.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccess Rules | The operation that you want to perform. Set the value to DescribeAccessRules. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. |
| AccessRuleId | String | No | 1 | The ID of the rule. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessRules | Array of AccessRule |   | The list of rules. |
| AccessRule |   |   |   |
| AccessRuleId | String | 1 | The ID of the rule. |
| Priority | Integer | 1 | The priority of the rule. If multiple rules are attached to the authorized object, the rule with the highest priority takes effect. Valid values: 1 to 100. The value 1 indicates the highest priority. |
| RWAccess | String | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates the read and write permissions. RDONLY: the read-only permissions. |
| SourceCidrIp | String | 10.0.*. */** | The IP address or CIDR block of the authorized object. |
| UserAccess | String | no squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash, root squash, and _ _ all squash. Default value: no squash. _ _ |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 86D89E82-4297- 4343-8E1E- A2495B35CC70 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of rules. |

| Developer Guide·A | PI Reference |   | Apsara File Storage NAS |
|---|---|---|---|

```json
http(s)://[Endpoint]/? Action=DescribeAccessRules &AccessGroupName=classic-test <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>86D89E82-4297-4343-8E1E-A2495B35CC70</RequestId> <PageNumber>1</PageNumber> <AccessRules>
    <RWAccess>RDWR</RWAccess>
    <AccessRuleId>1</AccessRuleId>
    <UserAccess>no_squash</UserAccess>
    <Priority>1</Priority>
    <SourceCidrIp>10.0. *. */**</SourceCidrIp>
</AccessRules>
    "TotalCount": 1,
    "PageSize": 1,
    "RequestId": "86D89E82-4297-4343-8E1E-A2495B35CC70",
    "PageNumber": 1,
    "AccessRules": {
        "RWAccess": "RDWR",
        "AccessRuleId": 1,
        "UserAccess": "no_squash",
        "Priority": 1,
        "SourceCidrIp": "10.0. *. */**"
```

### 4.7 Quotas

#### 4.7.1 SetDirQuota

Creates a directory quota for a file system.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | SetDirQuota | The operation that you want to perform. Set the value to SetDirQuota. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| Path | String | Yes | /data/sub1 | The absolute path of the directory in the file system. |
| QuotaType | String | Yes | Accounting | The quota type. Valid value: Accounting: a statistical quota. If you set this parameter to Accounting, File Storage NAS (NAS) calculates only the storage usage of the directory. Enforcement: a restrictive quota. If you set this parameter to Enforcement and the storage usage exceeds the quota, you can no longer create files or subdirectories for the directory, or write data to the directory. |
| UserType | String | Yes | Uid | The user type. Valid values: Uid: user ID Gid: user group ID AllUsers: all users |
| UserId | String | No | 500 | The UID or GID of the user for whom you want to set a directory quota. This parameter is required and valid only if the UserType parameter is set to Uid or Gid. Example: If you want to set a directory quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500. If you want to set a directory quota for a user group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100. |

| SizeLimit | Long | No | 1024 | The maximum size of files that can be created in the directory. Unit: GB. If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters. |
|---|---|---|---|---|
| FileCountLimit | Long | No | 10000 | The maximum number of files that can be created in the directory. The value includes the number of files, subdirectories, and special files. If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

```xml
http(s)://[Endpoint]/?Action=SetDirQuota &FileSystemId=1ca404**** &Path=/data/sub1 &QuotaType=Accounting &UserType=Uid <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
```

```json
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
```

#### 4.7.2 CancelDirQuota

Cancels the directory quotas of a file system.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelDirQuota | The operation that you want to perform. Set the value to CancelDirQuota. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| Path | String | Yes | /data/sub1 | The absolute path of the directory in the file system. |
| UserType | String | Yes | Uid | The type of the user ID. Valid values: Uid: user ID Gid: user group ID AllUsers: all users |
| UserId | String | No | 500 | The ID of an object for which you want to cancel a quota. This parameter is required and valid only if the UserType parameter is set to Uid or Gid. Example: If you want to cancel a quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500. If you want to cancel a quota for a group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100. To cancel the quotas for all users, set the UserType parameter to AllUsers. The UserId parameter can be left empty. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

```json
http(s)://[Endpoint]/?Action=CancelDirQuota &FileSystemId=1ca404**** &Path=/data/sub1 &UserType=Uid <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
```

#### 4.7.3 DescribeDirQuotas

Queries the directory quotas of a file system.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeDirQuot as | The operation that you want to perform. Set the value to DescribeDirQuotas. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |

| Path | String | No | /data/sub1 | The absolute path of the directory in the file system. If you do not specify the parameter, the operation returns all directories that have quotas applied. |
|---|---|---|---|---|
| PageSize | Integer | No | 1 | The number of entries per page. |
| PageNumber | Integer | No | 1 | The page number. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| DirQuotaInfos | Array of DirQuotaInfo |   | The details of quotas for directories. |
| DirInode | String | 1123 | The inode number of the directory. |
| Path | String | /data/sub1 | The absolute path of the directory in the file system. |
| Status | String | Normal | The status of the quota created for the directory. Valid values: Initializing and Normal. The Initializing state indicates that the quota is being created. The Normal state indicates that the quota is created. |
| UserQuotaInfo s | Array of UserQuotaInfo |   | The details of quotas for users. |
| FileCountLimit | Long | 10000 | The maximum number of files that can be created in the directory. |
| FileCountReal | Long | 5100 | The total number of files that have been created in the directory. |
| QuotaType | String | Accounting | The quota type. Valid values: Accounting and Enforcement. |
| SizeLimit | Long | 1024 | The maximum size of files that can be created in the directory. Unit: GB. |
| SizeReal | Long | 800 | The total size of files that have been created in the directory. Unit: GB. |

| UserId | String | 500 | The ID of the user that you specify to create a quota for the directory. The value depends on the value of the UserType parameter. |
|---|---|---|---|
| UserType | String | Uid | The type of the user ID. Valid values: Uid, Gid, and AllUsers. If the parameter is set to Uid or Gid, the value of the UserId parameter is returned. If the parameter is set to AllUsers, the value of the UserID parameter is empty. |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 1 | The number of entries per page. |
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |

```
http(s)://[Endpoint]/?Action=DescribeDirQuotas &FileSystemId=1ca404****
```

```json
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
```

`},`

```json
    "PageSize": 1,
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "PageNumber": 1
```

### 4.8 Unified namespaces

#### 4.8.1 CreateNamespace

Creates a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNamespa ce | The operation that you want to perform. Set the value to CreateNamespace. |
| ProtocolType | String | Yes | NFS | The protocol type. Only the Network File System (NFS) protocol is supported. |
| StorageType | String | Yes | Performance | The storage class. Valid values: Performance: Performance File Storage NAS (NAS) file systems Capacity: Capacity NAS file systems |
| ZoneId | String | No | cn-hangzhou-b | The zone ID. Each region has multiple isolated locations known as zones. Each zone has its own independent power supply and networks. Note An Elastic Compute Service (ECS) instance and a NAS file system that reside in different zones of the same region can access each other. We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |
| ClusterId | String | No | StandardNasClu ster | The cluster ID. |

| EncryptType | String | No | 0 | Specifies whether to encrypt data in the file system in the namespace. You can use a key that is managed by Key Management Service (KMS) to encrypt the data that is stored in a file system. When you read and write the encrypted data, the data is automatically decrypted. Valid values: 0 (default): does not encrypt the data. 1: encrypts the data. |
|---|---|---|---|---|
| Description | String | No | balabala | The description of the file system. Limits: The description must be 2 to 128 characters in length. The decription must start with a letter and cannot start with http:// or https:// . The description can contain letters, digits, colons (:), underscores ( ), periods (.), and _ hyphens (-). |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | The namespace ID. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```
http(s)://[Endpoint]/?Action=CreateNamespace &ProtocolType=NFS &StorageType=Performance
```

```json
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
```

#### 4.8.2 DeleteNamespace

Deletes a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNamespa ce | The operation that you want to perform. Set the value to DeleteNamespace. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | The namespace ID. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```json
http(s)://[Endpoint]/?Action=DeleteNamespace &NasNamespaceId=1NS244**** <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
```

#### 4.8.3 ModifyNamespace

Modifies a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNamespa ce | The operation that you want to perform. Set the value to ModifyNamespace. |
| Description | String | Yes | test | The namespace description. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | The namespace ID. |

| Developer Guide·A | PI Reference |   | Apsara File Storage NAS |
|---|---|---|---|

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
|---|---|---|---|

```json
http(s)://[Endpoint]/?Action=ModifyNamespace &Description=test &NasNamespaceId=1NS244**** <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
```

#### 4.8.4 DescribeNamespaces

Queries namespaces.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeNames paces | The operation that you want to perform. Set the value to DescribeNamespaces. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose Apsara File Storage NAS (NAS) file systems. |
| NasNamespaceI d | String | No | 1NS244**** | The namespace ID. |

| Description | String | No | test | The namespace description. |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries per page. Default value: 10. Valid values: 1 to 100. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| StorageType | String | No | Performance | The storage class. Valid values: Performance: Performance NAS file systems Capacity: Capacity NAS file systems |
| OrderByField | String | No | CreateTime | The field based on which the returned results are sorted. Default value: CreateTime, which specifies that the returned results are sorted based on creation time. |
| SortOrder | String | No | ASC | The sorting order. Valid values: ASC (default): ascending order DESC: descending order |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac eCreateLimit | Integer | 2 | The maximum number of namespaces that are created. |
| NasNamespac es | Array of NasNamespac e |   | The queried namespaces. |
| CreateTime | String | 2022-07- 20T10:08:08Z | The time when the namespace was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. |

| Description | String | balabala | The description of the file system. Limits: The description must be 2 to 128 characters in length. The description must start with a letter and cannot start with http:// or https:// . The description can contain letters, digits, colons (:), underscores ( ), _ periods (.), and hyphens (-). |
|---|---|---|---|
| EncryptType | Integer | 1 | Indicates whether data in the file system is encrypted in the namespace. You can use a key that is managed by Key Management Service (KMS) to encrypt the data that is stored in a file system. When you read and write the encrypted data, the data is automatically decrypted. Valid values: 0: The data is not encrypted. 1: The data is encrypted. |
| FileSystemTyp e | String | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |
| MountTargets | Array of MountTarget |   | The queried mount targets of the file system in the namespace. |
| AccessGroupN ame | String | classic-test | The name of the permission group. |
| MountTargetD omain | String | 1ca404a666- w****.cn- hangzhou.nas.aliyu ncs.com | The mount target of the file system. |
| NetworkType | String | Vpc | The network type. Valid values: Vpc: virtual private cloud (VPC) Classic: classic network |

| Status | String | Active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. Pending: The mount target is being created or modified. Deleting: The mount target is being deleted. |
|---|---|---|---|
| VpcId | String | vpc- 2zesj9afh3y518k9o **** | The VPC ID. |
| VswId | String | vsw- 2zevmwkwyztjuoff g**** | The vSwitch ID. |
| NasNamespac eId | String | 1NS244**** | The namespace ID. |
| ProtocolType | String | NFS | The protocol type. Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
| RegionId | String | cn-hangzhou | The region ID. |
| Status | String | Normal | The status of the quota created for the directory. Valid values: Initializing and Normal. The Initializing state indicates that the quota is being created. The Normal state indicates that the quota is created. |
| StorageType | String | Performance | The storage class. Valid values: Performance: Performance NAS file systems Capacity: Capacity NAS file systems |
| ZoneId | String | cn-hangzhou-b | The zone ID. |
| PageNumber | Integer | 1 | The page number. Pages start from page 1. Default value: 1. |
| PageSize | Integer | 1 | The number of entries per page. |

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of entries returned. |

```xml
http(s)://[Endpoint]/?Action=DescribeNamespaces <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <NasNamespaceCreateLimit>2</NasNamespaceCreateLimit> <NasNamespaces>
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

```json
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
```

#### 4.8.5 AddFileSystemToNamespace

Adds a file system to a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddFileSystemT oNamespace | The operation that you want to perform. Set the value to AddFileSystemToNamespace. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| MappedPath | String | Yes | tmp path _ | The mapped path. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |

| FileSystemType | String | No | standard | The type of the file system. Valid values: standard (default): General-purpose File Storage NAS (NAS) file system |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | The ID of the file system. |
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |

```json
http(s)://[Endpoint]/?Action=AddFileSystemToNamespace &FileSystemId=1ca404**** &MappedPath=tmp_path &NasNamespaceId=1NS244**** <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <FileSystemId>1ca404****</FileSystemId>
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "FileSystemId": "1ca404****"
```

#### 4.8.6 RemoveFileSystemFromNamespace

Deletes a file system from a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | RemoveFileSyst emFromNamesp ace | The operation that you want to perform. Set the value to RemoveFileSystemFromNamespace. |
|---|---|---|---|---|
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | The ID of the file system. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```json
http(s)://[Endpoint]/?Action=RemoveFileSystemFromNamespace &FileSystemId=1ca404**** &NasNamespaceId=1NS244**** <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <FileSystemId>1ca404****</FileSystemId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "FileSystemId": "1ca404****"
```

#### 4.8.7 RenameMappedPathInNamespace

Modifies the mapping name of a file system in a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RenameMapped PathInNamespac e | The operation that you want to perform. Set the value to RenameMappedPathInNamespace. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| MappedPath | String | Yes | tmp path _ | The mapped path. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac eId | String | 1NS244**** | The namespace ID. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```
http(s)://[Endpoint]/?Action=RenameMappedPathInNamespace &FileSystemId=1ca404**** &MappedPath=tmp_path &NasNamespaceId=1NS244****
```

```json
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <NasNamespaceId>1NS244****</NasNamespaceId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "NasNamespaceId": "1NS244****"
```

#### 4.8.8 ListFileSystemsInNamespace

Queries the mapped file systems in a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListFileSystemsI nNamespace | The operation that you want to perform. Set the value to ListFileSystemsInNamespace. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |
| NasNamespaceI d | String | No | 1NS244**** | The namespace ID. |
| Description | String | No | test | The namespace description. |
| PageSize | Integer | No | 10 | The number of entries per page. |
| PageNumber | Integer | No | 1 | The page number. |
| FileSystemId | String | No | 1ca404**** | The ID of the file system. |
| MappedPath | String | No | tmp path _ | The mapped path. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NSMembers | Array of NSMember |   | The queried file systems. |
| CreateTime | String | 2022-07- 25T15:43:06CST | The creation time. |
| FileSystemId | String | 1ca404**** | The ID of the file system. |
| FileSystemTyp e | String | standard | The type of the file system. standard: General-purpose NAS file system. |
| MappedPath | String | tmp path _ | The mapped path. |
| Status | String | Running | The status of the file system. Valid values: Pending: The file system is being created or modified. Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state. Stopped: The file system is unavailable. Extending: The file system is being scaled up. Stopping: The file system is being stopped. Deleting: The file system is being deleted. |
| StorageType | String | Performance | The storage class. Valid values: Capacity: Capacity NAS file systems Performance: Performance NAS file systems |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 1 | The number of entries per page. |

| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of entries returned. |

```json
http(s)://[Endpoint]/?Action=ListFileSystemsInNamespace <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <NSMembers>
    <Status>Running</Status>
    <StorageType>Performance</StorageType>
    <FileSystemType>standard</FileSystemType>
    <CreateTime>2022-07-25T15:43:06CST</CreateTime>
    <FileSystemId>1ca404****</FileSystemId>
    <MappedPath>tmp_path</MappedPath>
</NSMembers>
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
```

#### 4.8.9 CreateNamespaceMountTarget

Creates a mount target for a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateNamespa ceMountTarget | The operation that you want to perform. Set the value to CreateNamespaceMountTarget. |
| AccessGroupNa me | String | Yes | classic-test | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ The name of the permission group must be different from the names of the default permission groups. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPCs) and DEFAULT CLASSIC GROUP NAME _ _ _ (the default permission group for the classic network). |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| NetworkType | String | Yes | Vpc | The network type of the mount target. Valid values: Vpc: virtual private cloud (VPC) Classic: classic network |
| FileSystemType | String | No | standard | The type of the file system. Valid values: standard: General-purpose File Storage NAS (NAS) file system |
| VpcId | String | No | vpc- 2zesj9afh3y518 k9o**** | The VPC ID. This parameter is valid and required if the mount target resides in a VPC. |

| VSwitchId | String | No | vsw- 2zevmwkwyztju offg**** | The vSwitch ID. This parameter is valid and required if the mount target resides in a VPC. |
|---|---|---|---|---|
| SecurityGroupId | String | No | sg- bp1fg655nh68x yz9**** | The ID of the security group. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```json
http(s)://[Endpoint]/?Action=CreateNamespaceMountTarget &AccessGroupName=classic-test &NasNamespaceId=1NS244**** &NetworkType=Vpc <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
```

#### 4.8.10 DeleteNamespaceMountTarget

Deletes a mount target for a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteNamespa ceMountTarget | The operation that you want to perform. Set the value to DeleteNamespaceMountTarget. |
| MountTargetDo main | String | Yes | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```xml
http(s)://[Endpoint]/?Action=DeleteNamespaceMountTarget &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NS244**** <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain>
```

```json
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com"
```

#### 4.8.11 ModifyNamespaceMountTarget

Modifies the status of the mount target for a namespace.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyNamespa ceMountTarget | The operation that you want to perform. Set the value to ModifyNamespaceMountTarget. |
| MountTargetDo main | String | Yes | 1ca404****- kvr2.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target for the file system in the namespace. |
| NasNamespaceI d | String | Yes | 1NSc24**** | The namespace ID. |
| AccessGroupNa me | String | No | DEFAULT VPC G _ _ ROUP NAME _ | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ The name of the permission group must be different from the names of the default permission groups. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPCs) and DEFAULT CLASSIC GROUP NAME _ _ _ (the default permission group for the classic network). |

| Status | String | No | Active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. |
|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |

```json
http(s)://[Endpoint]/?Action=ModifyNamespaceMountTarget &MountTargetDomain=1ca404****-kvr2.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NSc24**** <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId>
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8"
```

#### 4.8.12 DescribeNamespaceMountTargets

Queries the mount targets of a namespace.

**Request headers**

The DescribeNamespaceMountTargets operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| NasName spaceId | Strin g | Query | Yes | ns1ca404**** | The namespace ID. |
| MountTar getDomai n | Strin g | Query | No | ns-1NS724****-0****.cn- wulan-en****- d01.nas.inter.en****.sh* ***ng.com | The domain name of the mount target. |
| PageSize | Integ er | Query | No | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNum ber | Integ er | Query | No | 1 | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargets | Array | - | The queried mount targets. |
| - MountTargetD omain | String | ns-1NS724****- 0****.cn-wulan- en****- d01.nas.inter.en*** *.sh****ng.com | The domain name of the mount target. |
| -NetworkType | String | Classic | The network type of the mount target. Valid values: Classic: classic network Vpc: virtual private cloud (VPC) |
| -VpcId | String | vpc- gxxxxxlzw21fj9k | The VPC ID. |
| -VswId | String | vsw- g4xxxxxxpf4mb6o m6j | The vSwitch ID. |
| -AccessGroup | String | pri | The name of the permission group that is attached to the mount target. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -Status | String | Active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. You can mount a file system only when the mount target of the file system is in the Active state. |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | The request ID. |
| TotalCount | Integer | 3 | The total number of mount targets. |
| PageSize | Integer | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | 1 | The page number. Pages start from page 1. Default value: 1. |

```
http(s)://[Endpoint]/?Action=DescribeNamespaceMountTargets &NasNamespaceId=ns1ca404****
```

```json
HTTP/1.1 200 OK Content-Type:application/json
 "TotalCount":3,
 "RequestId":"3BAB90FD-B4A0-48DA-9F09-2B963510A0EF",
 "PageSize":1,
 "PageNumber":1,
 "MountTargets":[
   "Status":"Active",
   "VpcId":"vpc-gxxxxxlzw21fj9k",
   "VswId":"vsw-g4xxxxxxpf4mb6om6j",
   "MountTargetDomain":"ns-1NS724****-0****.cn-wulan-en****-
d01.nas.inter.en****.sh****ng.com",
   "NetworkType":"Classic",
   "AccessGroup":"pri"
```

`]`

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

#### 4.8.13 AddNamespaceToGroup

Creates a cross-domain mount orchestration.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddNamespaceT oGroup | The operation that you want to perform. Set the value to AddNamespaceToGroup. |

| MappedPath | String | Yes | data | The mapped path for cross-domain mount orchestration. |
|---|---|---|---|---|
| MountTargetDo main | String | Yes | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | The mount target of the namespace. |
| NasNamespaceI d | String | Yes | 1NS244**** | The namespace ID. |
| NasNamespaceR egion | String | Yes | cn-hangzhou | The region where the namespace resides. |
| NetworkType | String | Yes | Vpc | The network type. Valid values: Vpc: virtual private cloud (VPC) Classic: classic network |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose File Storage NAS (NAS) file systems. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E |   |

```
http(s)://[Endpoint]/?Action=AddNamespaceToGroup &MappedPath=data &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com &NasNamespaceId=1NS244**** &NasNamespaceRegion=cn-hangzhou &NetworkType=Vpc
```

```json
<RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

#### 4.8.14 RemoveNamespaceFromGroup

Deletes a cross-domain mount orchestration.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RemoveNamesp aceFromGroup | The operation that you want to perform. Set the value to RemoveNamespaceFromGroup. |
| MemberId | String | Yes | 1 | The ID of the cross-domain mount orchestration. |
| FileSystemType | String | No | 1ca404**** | The ID of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| MemberId | String | 1 | The ID of the cross-domain mount orchestration. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

```
http(s)://[Endpoint]/?Action=RemoveNamespaceFromGroup &MemberId=1
```

```json
<MemberId>1</MemberId> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId>
    "MemberId": 1,
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E"
```

#### 4.8.15 DescribeNamespaceGroup

Queries the Cross-domain Mount Orchestration page.

**Request headers**

The DescribeNamespaceGroup operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parameter | Type | Posit ion | Required | Example | Description |
|---|---|---|---|---|---|
| FileSystem Type | Strin g | Quer y | No | standard | The type of the file system. Default value: standard, which indicates General- purpose File Storage NAS (NAS) file systems. |
| PageSize | Integ er | Quer y | No | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumb er | Integ er | Quer y | No | 1 | The page number. Pages start from page 1. Default value: 1. |
| MountTarg etDomain | Strin g | Quer y | No | ns-1Nxxxx-9cb81.cn- wulan-envxx- d01.nas.intra.envxx.shxxx ang.com. | The mount target of the namespace. |

| NasNames paceRegio n | Strin g | Quer y | No | cn-xxxn-envxxx-d01 | The region where the namespace resides. |
|---|---|---|---|---|---|
| Status | Strin g | Quer y | No | Enabled | The status of the namespace. Valid values: All Enabled Disable |
| MappedPat h | Strin g | Quer y | No | nas | The mapped path for cross-domain mount orchestration. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| NasNamespac es | Array | - | The queried namespaces. |
| - ResourceOwne rId | String | 12xxxxx8974995 | The user ID (UID) of the user organization. |
| -MemberId | String | 6 | The sequence ID. |
| -NetworkType | String | Vpc | The network type. Valid values: Vpc: virtual private cloud (VPC) Classic: classic network |
| - NasNamespac eRegion | String | cn-xxxn-envxxx- d01 | The domain name. |
| - NasNamespac eId | String | 1NSxxx26 | The namespace ID. |

| - MountTargetD omain | String | ns-1Nxxxx- 9cb81.cn-wulan- envxx- d01.nas.intra.envx x.shxxxang.com. | The mount target of the namespace. |
|---|---|---|---|
| -MappedPath | String | nas | The mapped path for cross-domain mount orchestration. |
| -CreateTime | String | 2023-12- 29T09:18:10Z | The creation time. |
| -Status | String | Enabled | The status of the namespace. Valid values: All Enabled Disable |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| PageSize | Integer | 1 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | 1 | The page number. Pages start from page 1. Default value: 1. |

```
http(s)://[Endpoint]/?Action=DescribeNamespaceGroup
```

```json
HTTP/1.1 200 OK Content-Type:application/json
 "TotalCount":1,
 "RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
 "PageSize":1,
 "PageNumber":1,
 "NasNamespaces":[
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
```

`]`

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

NAS 2017-06-26

### 4.9 Lifecycle management

#### 4.9.1 CreateLifecyclePolicy

Creates a lifecycle policy.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLifecycleP olicy | The operation that you want to perform. Set the value to CreateLifecyclePolicy. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| LifecyclePolicyN ame | String | Yes | lifecyclepolicy 0 _ 1 | The name of the lifecycle policy. The name must be 3 to 64 characters in length and can contain letters, digits, underscores ( ), and _ hyphens (-). The name must start with a letter. |
| LifecycleRuleNa me | String | Yes | DEFAULT ATIME _ 14 _ | The management rule that is associated with the lifecycle policy. Valid values: DEFAULT ATIME 14: Files that are _ _ not accessed in the last 14 days are dumped to the IA storage class. DEFAULT ATIME 30: Files that are _ _ not accessed in the last 30 days are dumped to the IA storage class. DEFAULT ATIME 60: Files that are _ _ not accessed in the last 60 days are dumped to the IA storage class. DEFAULT ATIME 90: Files that are _ _ not accessed in the last 90 days are dumped to the IA storage class. |
| OssBucket | String | Yes | rick-test-005 | The Object Storage Service (OSS) bucket to which cold data is dumped. |
| Path | String | Yes | /pathway/to/fold er | The absolute path of the directory that is associated with the lifecycle policy. If you specify this parameter, you can associate the lifecycle policy with only one directory. The path must start with a forward slash (/) and must be a path that exists in the mount target. |

| StorageType | String | Yes | InfrequentAcces s | The storage class of the data that is dumped. Default value: InfrequentAccess |
|---|---|---|---|---|
| Recursive | Boolean | No | true | Specifies whether to traverse directories. If the value is true, all subdirectories in the directory are traversed. Valid values: true false (default) |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF4211C8 | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

```xml
http(s)://[Endpoint]/?Action=CreateLifecyclePolicy &FileSystemId=1ca404**** &LifecyclePolicyName=lifecyclepolicy_01 &LifecycleRuleName=DEFAULT_ATIME_14 &OssBucket=rick-test-005 &Path=/pathway/to/folder &StorageType=InfrequentAccess <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8</RequestId> <Success>true</Success>
```

```json
    "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF4211C8",
    "Success": true
```

#### 4.9.2 DeleteLifecyclePolicy

Deletes a lifecycle policy.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLifecycleP olicy | The operation that you want to perform. Set the value to DeleteLifecyclePolicy. |
| FileSystemId | String | Yes | 106174**** | The ID of the file system. |
| LifecyclePolicyN ame | String | Yes | lifecycle | The name of the lifecycle policy. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

```xml
http(s)://[Endpoint]/?Action=DeleteLifecyclePolicy &FileSystemId=106174**** &LifecyclePolicyName=lifecycle <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <Success>true</Success>
```

```json
{"RequestId":"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E","Success":"true"}
```

#### 4.9.3 ModifyLifecyclePolicy

Modifies a lifecycle policy.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyLifecycleP olicy | The operation that you want to perform. Set the value to ModifyLifecyclePolicy. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| LifecyclePolicyN ame | String | Yes | ifecyclepolicy 0 _ 1 | The name of the lifecycle policy. |
| LifecycleRuleNa me | String | Yes | DEFAULT ATIME _ 14 _ | The management rule that is associated with the lifecycle policy. Valid values: DEFAULT ATIME 14: Files that are _ _ not accessed in the last 14 days are dumped to the IA storage class. DEFAULT ATIME 30: Files that are _ _ not accessed in the last 30 days are dumped to the IA storage class. DEFAULT ATIME 60: Files that are _ _ not accessed in the last 60 days are dumped to the IA storage class. DEFAULT ATIME 90: Files that are _ _ not accessed in the last 90 days are dumped to the IA storage class. |
| Path | String | Yes | /pathway/to/fold er | The absolute path of a directory with which the lifecycle policy is associated. |

| Recursive | Boolean | Yes | true | Specifies whether to traverse directories. If the value is true, all subdirectories in the directory are traversed. Valid values: true false (default) |
|---|---|---|---|---|
| StorageType | String | No | InfrequentAcces s | The storage class of the data that is dumped. Default value: InfrequentAccess |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
| Success | Boolean | true | Indicates whether the request was successful. Valid values: true false |

```xml
http(s)://[Endpoint]/?Action=ModifyLifecyclePolicy &FileSystemId=1ca404**** &LifecyclePolicyName=ifecyclepolicy_01 &LifecycleRuleName=DEFAULT_ATIME_14 &Path=/pathway/to/folder &Recursive=true <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <Success>true</Success>
```

```json
    "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
    "Success": true
```

#### 4.9.4 DescribeLifecyclePolicies

Queries lifecycle policies.

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLifecycl ePolicies | The operation that you want to perform. Set the value to DescribeLifecyclePolicies. |
| FileSystemId | String | No | 1ca404**** | The ID of the file system. |
| PageSize | Integer | No | 10 | The number of entries per page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The page number. Pages start from page 1. Default value: 1. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| LifecyclePolici es | Array of LifecyclePolicy |   | The queried lifecycle policies. |
| CreateTime | String | 2019-10- 30T10:08:08Z | The time when the lifecycle policy was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. |
| FileSystemId | String | 1ca404**** | The ID of the file system. |
| LifecyclePolicy Name | String | lifecyclepolicy 01 _ | The name of the lifecycle policy. |

| LifecycleRuleN ame | String | DEFAULT ATIME 1 _ _ 4 | The management rule that is associated with the lifecycle policy. Valid values: DEFAULT ATIME 14: Files that are not _ _ accessed in the last 14 days are dumped to the IA storage class. DEFAULT ATIME 30: Files that are not _ _ accessed in the last 30 days are dumped to the IA storage class. DEFAULT ATIME 60: Files that are not _ _ accessed in the last 60 days are dumped to the IA storage class. DEFAULT ATIME 90: Files that are not _ _ accessed in the last 90 days are dumped to the IA storage class. |
|---|---|---|---|
| OssBucket | String | rick-test-005 | The Object Storage Service (OSS) bucket to which cold data is dumped. |
| Path | String | /pathway/to/folder | The absolute path of a directory with which the lifecycle policy is associated. |
| Recursive | Boolean | true | Specifies whether to traverse directories. If the value is true, all subdirectories in the directory are traversed. Valid values: true false (default) |
| StorageType | String | InfrequentAccess | The storage class of the data that is dumped. Default value: InfrequentAccess |
| PageNumber | Integer | 1 | The page number. |
| PageSize | Integer | 10 | The number of entries per page. |
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
| TotalCount | Integer | 10 | The total number of lifecycle policies. |

```json
http(s)://[Endpoint]/?Action=DescribeLifecyclePolicies <TotalCount>10</TotalCount> <PageSize>10</PageSize> <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E</RequestId> <PageNumber>1</PageNumber> <LifecyclePolicies>
    <Path>/pathway/to/folder</Path>
    <LifecyclePolicyName>lifecyclepolicy_01</LifecyclePolicyName>
    <StorageType>InfrequentAccess</StorageType>
    <LifecycleRuleName>DEFAULT_ATIME_14</LifecycleRuleName>
    <CreateTime>2019-10-30T10:08:08Z</CreateTime>
    <OssBucket>rick-test-005</OssBucket>
    <FileSystemId>1ca404****</FileSystemId>
    <Recursive>true</Recursive>
</LifecyclePolicies>
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
```

### 4.10 NFS NAS ACL

#### 4.10.1 EnableNfsAcl

Enables the Network File System (NFS) access control list (ACL) feature for a file system.

**Request headers**

The EnableNfsAcl operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | Yes | 43f264xxxx | The ID of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 29F4F360-A6A8- 561A-A45B- A0F6882969BA | The request ID. |

```json
http(s)://[Endpoint]/?Action=EnableNfsAcl &FileSystemId=43f264xxxx HTTP/1.1 200 OK Content-Type:application/json
 "RequestId":"29F4F360-A6A8-561A-A45B-A0F6882969BA"
<RequestId>29F4F360-A6A8-561A-A45B-A0F6882969BA</RequestId>
```

#### 4.10.2 DisableNfsAcl

Disables the Network File System (NFS) access control list (ACL) feature for a file system.

**Request headers**

The DisableNfsAcl operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | Yes | 91fcdxxxx | The ID of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 24487C24-AE54- 57EC-B4E4- 4EDEEEB83B01 | The request ID. |

```json
http(s)://[Endpoint]/?Action=DisableNfsAcl &FileSystemId=91fcdxxxx HTTP/1.1 200 OK Content-Type:application/json
 "RequestId":"24487C24-AE54-57EC-B4E4-4EDEEEB83B01"
<RequestId>24487C24-AE54-57EC-B4E4-4EDEEEB83B01</RequestId>
```

#### 4.10.3 DescribeNfsAcl

Queries whether the Network File System (NFS) access control list (ACL) feature is enabled for a file system.

**Request headers**

The DescribeNfsAcl operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| FileSyste mId | Strin g | Query | Yes | 206614xxxx | The ID of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A1098673-1746- 505E-A5F1- 08527B7EDBDF | The request ID. |
| Acl | Struct | - | The ACL information. |
| -Enabled | Boolean | True | Indicates whether the NFS ACL feature is enabled. true: The NFS ACL feature is enabled. false: The NFS ACL feature is disabled. |

```json
http(s)://[Endpoint]/?Action=DescribeNfsAcl &FileSystemId=206614xxxx HTTP/1.1 200 OK Content-Type:application/json
 "RequestId":"A1098673-1746-505E-A5F1-08527B7EDBDF",
 "Acl":{
  "Enabled":true
<RequestId>A1098673-1746-505E-A5F1-08527B7EDBDF</RequestId> <Acl>
 <Enabled>true</Enabled>
</Acl>
```

### 4.11 Appendix: Error codes

An error code consists of four components, as listed in Error codes. Table 1. Error codes

| Component | Description |
|---|---|
| HttpCode | The HTTP response code that complies with HTTP syntax |
| Code | The error code |
| Message | The error message |
| Advice | The recommended solution |

**Error codes**

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 500 | InternalError | A system internal error occurred. | Please try again later. |
| 503 | ServiceUnavailable | This service is unavailable right now. | Please try again later. |
| 504 | ServiceTimeout | Service request timed out. | Please try again later. |
| 503 | SubRam.CheckFailed | The sub user ram check has failed due to some internal error. | Please try again later. |
| 503 | VpcRam.CheckFailed | The Vpc ram check has failed due to some internal error. | Please try again later. |
| 503 | VpcSubRam.CheckFail ed | The Vpc sub user ram check has failed due to some internal error. | Please try again later. |
| 400 | MissingParameter.call erUid | Request parameter missing: callerUid is not specified. | Add the callerUid request parameter. |
| 400 | MissingParameter.Regi onId | Request parameter missing: RegionId of the domain name is not specified. | Add the RegionId field to the domain name. |
| 400 | MissingParameter.VSw itchId | Request parameter missing: VSwitchId is not specified. | Add the VSwitchId request parameter. |
| 400 | MissingParameter.VpcI d | Request parameter missing: VpcId is not specified. | Add the VpcId request parameter. |

| 400 | InvalidParameter.Stora geType | Invalid request parameter: StorageType is invalid. | Set StorageType to Performance or Capacity. |
|---|---|---|---|
| 400 | InvalidParameter.Proto calType | Invalid request parameter: ProtocalType is invalid. | Set ProtocalType to NFS. |
| 400 | InvalidParameter.Desc ription | Invalid request parameter: Description contains invalid characters. | Set Description to a string that contains English letters and special characters such as at signs (@), number signs (#), dollar signs ($), underscores ( ), _ plus signs (+), and hyphens (-). |
| 404 | InvalidFileSystem.NotF ound | The specified NAS instance does not exist. | The specified NAS instance does not exist or has been deleted. |
| 403 | InvalidFileSystem.Alre adyExisted | The specified NAS instance already exists. | Call DescribeFileSystem s and specify the NAS instance ID to view the instance information. |
| 404 | InvalidMountTarget.No tFound | The specified mount point does not exist. | The specified mount point does not exist or has been deleted. |
| 404 | InvalidAccessGroup.No tFound | The specified permission group does not exist. | The specified permission group does not exist or has been deleted. |
| 403 | InvalidAccessGroup.Alr eadyExisted | The specified permission group already exists. | Call DescribeMountTarg ets and specify the permission group to view its information. |
| 403 | InvalidAccessGroup.Alr eadyAttached | The specified permission group has been bound to a mount point. | Unbind the permission group from the mount point before deleting the permission group. |
| 404 | InvalidAccessRule.Not Found | The specified permission rule does not exist. | The specified permission rule does not exist or has been deleted. |
| 404 | InvalidLocatin.NotFoun d | The specified location does not exist. | The requested location does not exist or is not providing services. |

| 404 | InvalidRegionId.NotFou nd | The specified region does not exist. | The requested region does not exist or is not providing services. |
|---|---|---|---|
| 404 | InvalidAZone.NotFoun d | The specified zone does not exist. | The requested zone does not exist or is not providing services. |
| 404 | InvalidVpc.NotFound | The specified VPC does not exist. | Create a VPC first. |
| 404 | InvalidVip.NotFound | The specified VIP does not exist. | Make sure that there are available IP addresses in your VPC. |
| 404 | InvalidLBid.NotFound | The specified LBid does not exist. | Please try again later. |
| 404 | InvalidVpcTunnelId.Not Found | The specified VPC tunnelId does not exist. | Check the VPC information first. |
| 404 | InvalidVpc.CreationFail ed | The specified vpc instance creation failed. | Make sure that the VPC information is correct and there is an available IP address for the VPC, and then try again. |
| 403 | OperationDenied.Defa ultAccessGroupCannot Delete | Operation not allowed: The default permission group cannot be deleted. | You can only edit custom permission groups. |
| 403 | OperationDenied.Defa ultAccessGroupCannot Modify | Operation not allowed: The default permission group cannot be modified. | You can only edit custom permission groups. |
| 403 | OperationDenied.Netw orkTypeNotMatched | Operation not allowed: The mount point network type does not match the AccessGroupType. | Make sure that the NetworkType of the mount point and the AccessGroupType of the permission group are consistent. |
| 403 | OperationDenied.Moun tTargetNotEmpty | Operation not allowed: The specified NAS instance already has a mount point. Delete the existing mount point first. | Delete the existing mount points first. |
| 403 | OperationDenied.FileS ystemCountsExceeded | The number of NAS instances has already reached the upper limit (a user can create a maximum of 10 NAS instances). | To raise the limit, contact technical support. |

| 403 | OperationDenied.Moun tTargetCountsExceede d | The number of mount points has already reached the upper limit (a maximum of two mount points can be created for each NAS instance). | To raise the limit, contact technical support. |
|---|---|---|---|
| 403 | OperationDenied.Acce ssGroupCountsExceed ed | The number of permission groups has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | OperationDenied.Acce ssRuleCountsExceede d | The number of permission rules has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | Forbidden.InvalidUserT ype | No permission: The user type is invalid. | Sorry, this API does not support your account type. |
| 403 | Forbbiden.Ram | User not authorized to operate on the specified resource, or this API doesn’t support RAM. | Access RAM to grant required NAS permissions. |
| 403 | NotQualified | No public beta qualification yet | Please initiate an application for a trial of the related features. If your application fails to be approved, contact the technical support. |

**Error response examples**

```json
<? xml version="1.0" encoding="UTF-8"? > <Error>
  <RequestId>B71B4C68-6C6B-4D4B-AD70-8951BD7D188E</RequestId>
  <HostId>nas.regionid.example.com</HostId>
  <Code>InvalidFileSystem.NotFound</Code>
  <Message>The specified NAS instance does not exist.</Message>
</Error>
  "RequestId": "B71B4C68-6C6B-4D4B-AD70-8951BD7D188E",
  "HostId": " nas.regionid.example.com ",
  "Code": "InvalidFileSystem.NotFound",
  "Message": "The specified NAS instance does not exist."
```
