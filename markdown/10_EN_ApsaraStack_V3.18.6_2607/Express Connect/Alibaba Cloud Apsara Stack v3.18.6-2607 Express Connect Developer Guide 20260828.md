---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Express Connect Developer Guide 20260828"
product_version: "V3.18.6_2607"
doc_version: "20260828"
pdf_pages: 151
source_pdf: "c24fd30c328bcb80_Alibaba Cloud Apsara Stack v3.18.6-2607 Express Connect Developer Guide 20260828.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E9%AB%98%E9%80%9F%E9%80%9A%E9%81%93/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Express%20Connect%20Developer%20Guide%2020260828.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Express Connect Developer Guide 20260828

## Table of Contents

- 1 Getting started
  - 1.1 Apsara Stack documentation
  - 1.2 Procedure for API calls
- 2 Preparations
  - 2.1 Obtain the information and the endpoint of an API operation
  - 2.2 Obtain an AccessKey pair
  - 2.3 Obtain the values of common request parameters
  - 2.4 Obtain STS credentials
  - 2.5 Obtain Express Connect SDK
- 3 Call examples for SDK for Java
  - 3.1 Quick start
  - 3.2 Use SDK
    - 3.2.1 Install SDK for Java
    - 3.2.2 Configure authentication credentials
    - 3.2.3 Configure connection requests
    - 3.2.4 Send a request
    - 3.2.5 Troubleshooting
    - 3.2.6 Use CommonRequest to call APIs
- 4 Call examples for SDK for Python
  - 4.1 Quick start
  - 4.2 Use SDK
    - 4.2.1 Install the SDK for Python
    - 4.2.2 Configure authentication credentials
    - 4.2.3 Set HTTPS requests
    - 4.2.4 Send a request
    - 4.2.5 Handle errors
    - 4.2.6 Use CommonRequest to call APIs
- 5 Call examples for SDK for Go
  - 5.1 Quick start
  - 5.2 Use SDK
    - 5.2.1 Install the core package of SDK for Go
    - 5.2.2 Configure authentication credentials
    - 5.2.3 Send a request
    - 5.2.4 Handle errors
    - 5.2.5 Use CommonRequest to call APIs
- 6 API Reference
  - 6.1 List of operations by function
  - 6.2 Invoke APIs
    - 6.2.1 Request syntax
    - 6.2.2 Authorization
    - 6.2.3 Signature
  - 6.3 RAM authentication
  - 6.4 Common parameters
  - 6.5 Physical connections
    - 6.5.1 CreatePhysicalConnection
    - 6.5.2 DescribeAccessPoints
    - 6.5.3 CancelPhysicalConnection
    - 6.5.4 DescribePhysicalConnections
    - 6.5.5 ModifyPhysicalConnectionAttribute
    - 6.5.6 TerminatePhysicalConnection
    - 6.5.7 EnablePhysicalConnection
    - 6.5.8 DeletePhysicalConnection
    - 6.5.9 CreatePhysicalConnectionOccupancyOrder
    - 6.5.10 ApplyPhysicalConnectionLOA
    - 6.5.11 CreatePhysicalConnectionSetupOrder
    - 6.5.12 CompletePhysicalConnectionLOA
    - 6.5.13 DescribePhysicalConnectionLOA
  - 6.6 VBR
    - 6.6.1 CreateVbrHa
    - 6.6.2 DeleteVbrHa
    - 6.6.3 DeleteNqa
    - 6.6.4 CreateVirtualBorderRouter
    - 6.6.5 DeleteVirtualBorderRouter
    - 6.6.6 DescribeVirtualBorderRouters
    - 6.6.7 DescribeVirtualBorderRoutersForPhysicalConnection
    - 6.6.8 TerminateVirtualBorderRouter
    - 6.6.9 RecoverVirtualBorderRouter
    - 6.6.10 ModifyVirtualBorderRouterAttribute
    - 6.6.11 AssociatePhysicalConnectionToVirtualBorderRouter
    - 6.6.12 UnassociatePhysicalConnectionFromVirtualBorderRouter
  - 6.7 BGP
    - 6.7.1 CreateBgpGroup
    - 6.7.2 DescribeBgpGroups
    - 6.7.3 ModifyBgpGroupAttribute
    - 6.7.4 DeleteBgpGroup
    - 6.7.5 CreateBgpPeer
    - 6.7.6 DescribeBgpPeers
    - 6.7.7 ModifyBgpPeerAttribute
    - 6.7.8 DeleteBgpPeer
    - 6.7.9 AddBgpNetwork
    - 6.7.10 DescribeBgpNetworks
    - 6.7.11 DeleteBgpNetwork
  - 6.8 Router interface
    - 6.8.1 CreateRouterInterface
    - 6.8.2 ConnectRouterInterface
    - 6.8.3 DeactivateRouterInterface
    - 6.8.4 ModifyRouterInterfaceSpec
    - 6.8.5 DeleteRouterInterface
    - 6.8.6 DescribeRouterInterfaces
    - 6.8.7 ActivateRouterInterface
    - 6.8.8 ModifyRouterInterfaceAttribute
- 7 Appendixes
  - 7.1 STS overview
    - 7.1.1 What is STS?
    - 7.1.2 AssumeRole

## 1 Getting started

### 1.1 Apsara Stack documentation

This topic describes how to find the required documentation when you call an API operation of an Apsara Stack service.

**Flowchart**

You can follow the procedure described in the following figure to view the specific documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center to view the desired documentation.
1. Go to the Apsara Stack documentation center.
2. Click the **Enterprise**, **Agility&XStack**, or **All-in-one** tab based on the Apsara Stack version that you use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the Apsara Stack service whose documentation you want to view.
5. In the product documentation section, click **View Details** or **Download PDF**.

### 1.2 Procedure for API calls

To provide consistent user experience, the API calls of Apsara Stack V3.16.0 and later are made by using the POP gateway by default. This topic describes how to use the POP gateway to call Apsara Stack API operations.

**Flowchart**

**Procedure**

1. Obtain security credentials used to call API operations.
For more information, see Obtain an AccessKey pair and Obtain Obtain STS credentials.

> **Note:** We recommend that you use the AccessKey pair of a personal account assigned by Resource Access Management (RAM) or an access credential assigned by Security Token Service (STS) to call the API operations of the Apsara Uni-manager Management Console and cloud services.

2. Obtain a region ID.
For more information about how to obtain a region ID, see Obtain the values of common headers.
3. Obtain the organization ID and the resource set ID.
Obtain the organization ID by calling the GetOrganizationList operation. For more information, see GetOrganizati onList in Apsara Uni-manager Management Console Developer Guide. Obtain the resource set ID by calling the ListResourceGroup operation. For more information, see ListResourceGr oup in Apsara Uni-manager Management Console Developer Guide.

> **Note:** When you call an API operation, set the `<x-acs-organizationid>` parameter to the organization ID that you obtained, and set the `<x-acs-resourcegroupid>` parameter to the resource set ID that you obtained. This way, you can query resources of the specified organization and resource set.
> If you do not specify the `<x-acs-organizationid>` parameter, the organization to which the current account belongs is queried.
> If you do not specify the `<x-acs-resourcegroupid>` parameter, this parameter is left empty. If you specify a resource set, you must also specify an organization ID.

4. View the developer guide of the cloud service on which you want to perform the operation.
For more information, see Apsara Stack documentation.
5. Obtain the endpoint of the service.
6. Obtain the SDK of the cloud service and make the API call.

## 2 Preparations

### 2.1 Obtain the information and the endpoint of an API operation

**endpoint of an API operation**

To call an API operation of a cloud service, you must obtain the information about the operation, including the service code, operation name, and API version.

**Background information**

The API information on the debugging page of the Apsara Uni-manager Management Console is for reference only. For more information about how to call API operations, see the developer guides of cloud services. If the information on the debugging page is different from that in the developer guide of a cloud service, the information in the developer guide prevails.

**Procedure**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top navigation bar.
4. In the left-side navigation pane, select the cloud service that you want to manage.
5. Select an API version from the **Version** drop-down list.
6. In the API operation list, you can view all API operations of the current version.
7. Click the operation that you want to call. Obtain the endpoint from the Endpoint parameter on the Parameter
tab.

### 2.2 Obtain an AccessKey pair

AccessKey pairs are classified into AccessKey pairs assigned by Resource Access Management (RAM) and those assigned by Security Token Service (STS). You can use either type of AccessKey pair for authentication when you call operations. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. You can use RAM or STS to assign an AccessKey pair for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see the ListResourceGroup section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, click the profile picture and then click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 2.3 Obtain the values of common request parameters

**parameters**

You must provide the values of the required parameters when you call Apsara Stack APIs. This topic describes the common request and response parameters used in Apsara Stack APIs and how to obtain the values of the request parameters.

**Request parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID of the environment. For more information, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni-manager Management Console. For more information, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni-manager Management Console. For more information, see Obtain the ID of a resource set. |
| x-acs-instanceid | The ID of the instance on which you want to perform the operation. For more information, see Obtain an instance ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can log on to the Apsara Uni-manager Management Console and navigate to homepage of the cloud service to obtain the instance ID. The following example shows how to go to the Express Connect homepage to obtain an instance ID:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Networking** > **Express Connect**.
3. In the left-side navigation pane, click **Exclusive Physical Connection**.
4. On the **Express Connect Circuit** page, you can view the ID of a connection over an Express Connect circuit in
the **ID/Name** column.

**Response parameters**

The following response parameters are returned by default when you call an API operation to query a list of instances.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 2.4 Obtain STS credentials

This topic describes how to use Security Token Service (STS) credentials to call Apsara Stack APIs.

**Background information**

STS allows you to use temporary credentials to access Apsara Stack resources. You can use STS credentials to call Apsara Stack APIs. To call Apsara Stack APIs, you must obtain an AccessKey ID, an AccessKey secret, and a security token assigned by STS. For more information, see STS.

**Procedure**

1. Obtain the `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User Information**. iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the STS credentials.

> **Note:** Replace the following variables with your actual information. Delete the angle brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourRoleSessionName>: Replace it with the name of the current session.
> <yourRoleArn>: Replace it with your RAM role.
> <sts.aliyuns.com>: Replace it with the STS endpoint.

```java
public static void main(String[] args) {
    // Create and initialize a DefaultAcsClient instance.
    Replace <AccessKeyId> and <AccessKeySecret> with your AccessKey ID and AccessKey secret.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "
<yourAccessKeySecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    String assumeRole = callAssumeRole(client);
    if (StringUtils.isEmpty(assumeRole)) return;
    JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
    JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
    // Obtain the AccessKey ID, AccessKey secret, and security token assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpoint is sts-vpc.${glo
bal:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the name of the current session.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace "<yourRoleArn>" with the RAM role ARN that is obtained in the previous step.
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

3. Use the AccessKey ID, AccessKey secret, and security token assigned by STS to call an API operation. In this
example, the Express Connect API operation `DescribePhysicalConnections` is called.

> **Note:** Replace the following variables with your actual information. Delete the angle brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourStsAccesskeyID>: Replace it with your AccessKey ID assigned by STS.
> <yourStsAccessKeySecret>: Replace it with your AccessKey secret assigned by STS.
> <yourStsToken>: Replace it with your security token assigned by STS.
> <yourResourceGroupID>: Replace it with your resource set ID.
> <yourOrganizationID>: Replace it with your organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with your region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and AccessKey
secret assigned by STS.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<yourStsA
ccessSecret>");
    HttpClientConfig clientConfig = HttpClientConfig.getDefault();
    clientConfig.setIgnoreSSLCerts(true);
    clientConfig.setProtocolType(ProtocolType.HTTPS);
    profile.setHttpClientConfig(clientConfig);
    IAcsClient client = new DefaultAcsClient(profile);
    CommonRequest request = new CommonRequest();
    request.setSysDomain("vpc.aliyuns.com");
    request.setSysProduct("vpc");
    request.setSysAction("DescribePhysicalConnections");
    request.setSysVersion("2016-04-28");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRegionID>" with your region ID.
    request.putHeaderParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the security token assigned by STS.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace it with your resource set ID.
    // request.putHeaderParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Required. Replace it with your organization ID.
    request.putHeaderParameter("x-acs-organizationid", "<yourOrganizationID>");
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

### 2.5 Obtain Express Connect SDK

When you use the Portable OpenAPI Proxy (POP) gateway to call an Apsara Stack API, you must obtain the SDK of the cloud service. This topic describes how to obtain Alibaba Cloud SDKs.

**Background information**

To use the features of Express Connect, you must install Virtual Private Cloud (VPC) SDK and the Alibaba Cloud core library. For example, to use VPC SDK for Java, you must download `aliyun-java-sdk-vpc` and `aliyun-java-`

```
sdk-core .
```

VPC SDK encapsulates the API released on April 28, 2016. The SDK identifies callers based on their AccessKey pairs and provides features such as automatic signing to allow you to create and manage resources by calling API operations. The SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The Alibaba Cloud core library is applicable to Alibaba Cloud and Apsara Stack services.

**References**

Alibaba Cloud SDK supports Java, Python, and Go. You can select an SDK from Alibaba Cloud SDK based on your business requirements.

> **Note:** We recommend that you use an SDK for Java, Python, or Go. If you use an SDK for another programming language, the SDK may be incompatible with your system.

or SDK for Java

## 3 Call examples for SDK for Java

### 3.1 Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Java. To use the features of Express Connect, you must install the VPC SDK.

**Environment requirements**

An authorized Apsara Stack account and an AccessKey pair are obtained. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. For more information, see Obtain the endpoint of Express Connect. Java Development Kit (JDK) 1.8 or later is required.

**Install Apsara Stack SDK for Java**

If you use Apache Maven to manage Java projects, you need to only add Maven commands to the pom.xml file of the projects. To use the VPC SDK, you must install the SDK core library and VPC SDK. We recommend that you use the core library version 4.5.17 or later, and use the SDK version 3.2.0.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

**Use Apsara Stack SDK for Java**

Perform the following operations to use Apsara Stack SDK for Java:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and set the required parameters.
3. Send the API request and handle the response or exceptions.

> **Note:** Replace the following variables with your actual information. Delete the angle brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <Product>: Replace it with the name of the service.
> <Endpoint>: Replace it with the endpoint of the service.
> <readTimeout>: Replace it with a read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Replace it with a connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Replace it with the maximum number of requests that are supported by each host.
> <maxRequests>: Replace it with the maximum number of requests.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

or SDK for Java

```java
import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.vpc.model.v20160428.*; import com.google.gson.Gson; public class Main {
     public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace it with the region ID.
            "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
        // Specify the endpoint of the service.
        profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>");
        // Set the request parameters.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);// Ignore this parameter.
        clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the read timeout period. Un
it: milliseconds.
        clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Specify the connection
timeout period. Unit: milliseconds.
        clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify the maximum number
of requests per host.
        clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum number of requests.
        clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the request protocol.
Default value: HTTP.
        /* Optional. Specify the IP address and port of the proxy.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>");
```

`*/`

```java
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the request parameters.
        DescribePhysicalConnectionsRequest request = new DescribePhysicalConnectionsRequest();
        // Set the service-related parameters.
        request.setPageSize(10);
        request.setPageNumber(1);
        // Specify the organization ID and resource set ID to query specified resources.
        request.putHeaderParameter("x-acs-organizationid", "1");
        request.putHeaderParameter("x-acs-resourcegroupid", "11");
        // Send the request and handle the response or exception.
        DescribePhysicalConnectionsResponse response;
       try {
            DescribePhysicalConnectionsResponse response = client.getAcsResponse(request);
            System.out.println(new Gson().toJson(response));
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

### 3.2 Use SDK

#### 3.2.1 Install SDK for Java

or SDK for Java This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Java. To use the features of Express Connect, you must install VPC SDK. Alibaba Cloud SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Alibaba Cloud SDK for Java by adding Maven dependencies or downloading Alibaba Cloud SDK. To use VPC SDK, you must install the core library of Alibaba Cloud SDK for Java and VPC SDK for Java. We recommend that you use the core library version 4.5.17 or later, and use VPC SDK for Java 3.2.0. To use VPC SDK for Java, you must install the core library of Alibaba Cloud SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDK.

```xml
<dependencies>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-core</artifactId>
            <version>4.5.17</version>
        </dependency>
        <dependency>
            <groupId>com.aliyun</groupId>
            <artifactId>aliyun-java-sdk-vpc</artifactId>
            <version>3.2.0</version>
        </dependency>
</dependencies>
```

#### 3.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports identity verification by providing an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

> **Note:** Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly- accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace it with the actual region ID.
    "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
```

> **Note:** Replace the preceding variables with the actual values and remove the brackets (<>).

#### 3.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements. or SDK for Java

> **Note:** You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
> <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following co de is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 3.2.4 Send a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Java to send a request. To use the features of Express Connect, you must install VPC SDK.

**Procedure**

1. Create an AcsClient object.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request . **${apiName}** specifies the name of an API operation, such as DescribePhysicalConnections. When you use the SDKs of multiple services, different requests may share the same name. Make sure that you differentiate the requests by SDK. or SDK for Java

```
DescribePhysicalConnectionsRequest request = new DescribePhysicalConnectionsRequest(); // Set the service-related parameters. request.setPageSize(10); request.setPageNumber(1); // Specify the organization ID and resource set ID to query specified resources. request.putHeaderParameter("x-acs-organizationid", "1"); request.putHeaderParameter("x-acs-resourcegroupid", "");
```

3. Send the request and handle the response.

```java
DescribePhysicalConnectionsResponse response; try {
   DescribePhysicalConnectionsResponse response = client.getAcsResponse(request);
   System.out.println(new Gson().toJson(response));
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

In normal cases, all returned fields are deserialized into the response. You can directly use `response.getXXX()` to obtain the response fields.

```
instanceStatus := response.getStatus()
```

However, if an exception occurs or you want to obtain the original HTTP response, use `doAction()` to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

#### 3.2.5 Troubleshooting

If the server or SDK encounters an error when you use SDK for Java, it returns an error response. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by SDK for Java. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. For example, when the following error occurs, you can modify the AccessKey ID based on the error message to solve the problem:

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle SDK errors, refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, you can submit a ticket with the request ID included.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // You can add your logic to handle errors.
    // For example, print the error message.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

or SDK for Java

#### 3.2.6 Use CommonRequest to call APIs

If you want to call the API of a cloud service that does not provide an SDK, or the requests and responses do not meet your business requirements, you can use CommonRequest. CommonRequest supports all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

If you want to send a CommonRequest request, you must obtain the values of the following parameters: You can obtain the values of these parameters from the API references of cloud services. Domain: the endpoint of the service. Version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the sections about common parameters in the API references. Action: the name of the API operation that you want to call. You must obtain the **Action** parameter and specify the API operation in the `request.setSysAction("<Action>")` format. For example, to call the DescribePhysicalConnections operation, you must specify

```
 request.setSysAction("DescribePhysicalConnections") .
```

**Example: Call an RPC API**

The `DescribePhysicalConnections` operation of Express Connect is used as an example to show how to make an RPC API call to query the status of instances.

> **Note:** Replace the following variables with your actual information. Remove the brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourSecurityToken>: Replace it with your security token.
> <yourResourceGroupID>: Replace it with your resource set ID.
> <yourOrganizationID>: Replace it with your organization ID.
> <yourInstanceID>: Replace it with your instance ID.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

or SDK for Java

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionUD>",          // Replace it with your region ID.
            "<yourAccessKeyID>",      // Replace it with your AccessKey ID.
            "<yourAccessKeySecret>"); // Replace it with your AccessKey secret.
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /**
        You can configure HTTP proxy based on your business requirements.
        To configure HTTP proxy, perform the following steps:
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
        Replace the parameter with the proxy IP address and port.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set the request parameters.
        CommonRequest request = new CommonRequest();
        // Replace the parameter with the domain name of your cloud service.
        request.setSysDomain("vpc.aliyuncs.com");
        request.setSysProduct("Vpc");
        request.setSysVersion("2016-04-28");
        request.setSysAction("DescribePhysicalConnections");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Specify the
resource set ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Specify the o
rganization ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. Specify the region ID. If
you use Apsara Stack Enterprise 3.15 or earlier versions, this parameter is required.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional. Specify the
instance ID. This parameter is required when you want to delete, modify, or query the detailed information about an instance.
        /**
        When you use STS credentials to call an API operation, you must specify the STS token.
        In this case, set the following parameter:
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
        Specify the STS token.
```

`*/`

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
```

or SDK for Python

## 4 Call examples for SDK for Python

### 4.1 Quick start

This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Python. To use the features of Express Connect, you must install VPC SDK.

**Environment requirements**

An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. You must obtain the endpoint of Express Connect. For more information, see Obtain the endpoint of Express Connect.
1. Install the SDK core library.
If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

2. Install VPC SDK for Python.
The following examples show how to install VPC SDK for Python: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-vpc
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-vpc
```

**Use VPC SDK for Python**

To use the SDK for Python, perform the following steps:
1. Create a client. When you create a client, you must specify a region ID, an AccessKey ID, and an AccessKey
secret.
2. Create an API request and set the required parameters.
3. Send the API request and process the response or exceptions.

> **Note:** Replace the following variables with your actual information. Remove the brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <vpc.aliyuns.com>: Replace it with the endpoint of the service.

or SDK for Python

```python
#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribeNatGatewaysRequest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify the AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify the AccessKey secret.
# product config
product_name = 'Vpc' # Specify the service name. endpoint = '<vpc.aliyuns.com>' # Specify the endpoint of the service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeNatGatewaysRequest.DescribeNatGatewaysRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print response # If you use Python 3.x, specify print (response).
```

### 4.2 Use SDK

#### 4.2.1 Install the SDK for Python

This topic describes how to install and use Virtual Private Cloud (VPC) SDK for Python. To use the features of Express Connect, you must install VPC SDK. Alibaba Cloud SDK for Python supports Python 2.6.x, Python 2.7.x, Python 3.x, and later versions. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK of a cloud service, you must install the core library of Alibaba Cloud SDK for Python. For example, if you want to use VPC SDK for Python, you must install the SDK core library for Python and VPC SDK for Python.

If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

The following example shows how to install VPC SDK: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-vpc
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-vpc
```

#### 4.2.2 Configure authentication credentials

When you use Alibaba Cloud SDK to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDK for Python supports identity verification by providing an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

> **Important:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

or SDK for Python

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

#### 4.2.3 Set HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

> **Note:** The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

OpenSSL support in Python is required for sending HTTPS requests by using SDK for Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later.

| Run the | python -c "import ssl" | c |
|---|---|---|
| ImportError: No module named ssl |   |   |

Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the `ImportError: No module named ssl` error message does not appear in the command output, OpenSSL is supported. If OpenSSL is not supported, run the following command to install it:

```
pip install pyopenssl# You need to use this command if you use Python 2 in your local environment.
```

> **Note:** If you use Python 3 in your local environment, run the `pip3 install pyopenssl"` command.

**Set the protocol to HTTP or HTTPS for a request**

The following sample code provides an example on how to set HTTPS as the protocol for a request:

```java
import DescribeInstancesRequest request = DescribeInstancesRequest() request.set_protocol_type("https")
# Set the value to https or http.
```

**Set a global default protocol**

The following sample code provides an example on how to set a global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.
```

#### 4.2.4 Send a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Python to send a request. To use the features of Express Connect, you must install VPC SDK.

**Procedure**

1. Import VPC SDK.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkvpc.request.v20160428 import DescribePhysicalConnectionsRequest
```

2. Create an AcsClient object.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

or SDK for Python
3. Create a request.

```
request = DescribePhysicalConnectionsRequest.DescribePhysicalConnectionsRequest() request.set_accept_format('json')
```

4. Send the request and process the response.

```
response = clt.do_action_with_exception(request) print response # If you use Python 3.x, the default value is print (response).
```

#### 4.2.5 Handle errors

If an error occurs on the server side or SDK side when you use the Python SDK, the Python SDK returns the corresponding exception message. An exception message contains the detailed error information, namely the error code and the error message. Generally, you are not required to handle the errors returned by the Python SDK. You are only required to handle the errors on the server side according to the error message. `ServerException` is the error message on the server side. `ClientException` is the error message on the SDK side. For example, if the following error occurs, modify the ID of AccessKey according to the detailed error message.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle the errors returned by the Python SDK, see the following code example for reference:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your own error handling logic here.
    # For example, print the detailed error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

#### 4.2.6 Use CommonRequest to call APIs

If you want to call the API of a cloud service that does not provide an SDK, or the requests and responses do not meet your business requirements, you can use CommonRequest. CommonRequest supports all API operations.

**Characteristics of CommonRequest calling**

The CommonRequest calling method has the following characteristics: Light weight: You only need the core package to initiate the call, without downloading or installing the SDK of each product. Easy and convenient: You can call the latest API without updating the SDK. Fast iteration

**Use CommonRequest**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API references of cloud services. Domain: the endpoint of the service. Version: the version of the API in the YYYY-MM-DD format. You can obtain the API version from the sections about common parameters in the API references. Action: the name of the API operation that you want to call. Example: Call an RPC API You must obtain the **Action** parameter and specify the API operation in the `request.set_action_name('Action')` format. For example, to call the DescribePhysicalConnections operation, you must specify

```
 request.set_action_name('DescribePhysicalConnections') .
```

or SDK for Python

**Example: Call an RPC API**

The `DescribePhysicalConnections` operation of Express Connect is used as an example to show how to make an RPC API call to query the status of instances.

> **Note:** Replace the following variables with your actual information. Remove the brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourSecurityToken>: Replace it with your security token.
> <yourResourceGroupID>: Replace it with your resource set ID.
> <yourOrganizationID>: Replace it with your organization ID.
> <yourInstanceID>: Replace it with the instance ID.
> <vpc.aliyuncs.com>: Replace it with the endpoint of the service.

```python
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('Vpc') request.set_action_name('DescribePhysicalConnections') request.set_version('2016-04-28') request.set_domain('<vpc.aliyuncs.com>') #Specify the endpoint of the service.
# or:
# request = = CommonRequest(product='Vpc', action_name='DescribePhysicalConnections',version='2016-04-28',d
omain='vpc.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# The following example shows how to set the request protocol to HTTPS:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# When you use STS credentials to call an API operation, you must specify the STS token.
In this case, set the following parameter:
# request.add_query_param("SecurityToken", "<yourSecurityToken>");
# Specify the STS token.
######
# Optional. Specify the resource set ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Specify the organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Optional. Specify the region ID. If you use Apsara Stack Enterprise 3.15 or earlier, this parameter is re
quired. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. This parameter is required if you want to modify, delete, or query the
detailed information about an instance.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))
```

or SDK for Go

## 5 Call examples for SDK for Go

### 5.1 Quick start

Alibaba Cloud SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Virtual Private Cloud (VPC) SDK for Go. To use the features of Express Connect, you must install VPC SDK.

**Environment requirements**

You must have an authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) to use Alibaba Cloud Go SDK. For more information, see Obtain an AccessKey pair. You must obtain the endpoint of Express Connect. For more information, see Obtain the endpoint of Express Connect.

**Install VPC SDK for Go**

Alibaba Cloud SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package: You can check whether the latest version of the core package is installed on the Alibaba Cloud SDK for Go page.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use VPC SDK for Go**

The following sample code shows how to use VPC SDK for Go:
1. Initialize a client.
2. Create an API request and set the required parameters.
3. Send the API request and process the response or exceptions.

> **Note:** Replace the following variables with your actual information. Remove the brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <Endpoint>: Replace it with the endpoint of the service.

or SDK for Go

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "fmt"
```

`)`

```
func main() {
    // Create a VPC client.
    vpcClient, err := vpc.NewClientWithAccessKey(
        "<yourRegionID>",             // Replace it with the region ID.
        "<yourAccessKeyID>",         // Replace it with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace it with your AccessKey secret.
    if err != nil {
        // Handle exceptions.
        panic(err)
    // Create an API request and set the request parameters.
    request := vpc.CreatDescribePhysicalConnectionsRequest()
    // Specify the endpoint of the service.
    request.Domain = "<Endpoint>"
    // Set request.PageSize to 10.
    request.PageSize = requests.NewInteger(10)
    // Send the request and handle exceptions.
    response, err := vpcClient.DescribePhysicalConnections(request)
    if err != nil {
        // Handle exceptions.
        panic(err)
    fmt.Println(response)
```

4. Optional. Switch to HTTP or HTTPS.

```
request.Scheme = "HTTPS"
```

### 5.2 Use SDK

#### 5.2.1 Install the core package of SDK for Go

This topic describes how to install the core package of SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 5.2.2 Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDK for Go supports identify verification by providing an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair when you initialize the client.

> **Important:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

The following sample code shows how to initialize a VPC client: or SDK for Go

```
// Initialize a VPC client. vpcClient, err := vpc.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace it with the region ID.
        "<yourAccessKeyID>",             // Replace it with your AccessKey ID.
        "<yourAccessKeySecret>")        // Replace it with your AccessKey secret.
```

> **Note:** Replace the preceding variables with your actual information. Remove the brackets (<>) when you specify the parameters.

#### 5.2.3 Send a request

This topic describes how to use Virtual Private Cloud (VPC) SDK for Go to send a request. To use the features of Express Connect, you must install the VPC SDK. The following example shows how to use VPC SDK for Go to send a request.
1. Import VPC SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/vpc
```

2. Create a VPC client. The client includes all operations of the VPC API.

> **Note:** Replace the preceding variables with your actual information. Remove the angle brackets (<>) when you specify the parameters.

```
vpcClient,err := <vpc>.NewClientWithAccessKey( //Replace it with the name of the service.
    "<yourRegionID>",  // Replace it with your region ID.
    "<yourAccessKeyID>",  // Replace it with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace it with your AccessKey secret.
vpcClient.Domain = "vpc.aliyuns.com" //Specify the endpoint of the service.
```

3. Create a request by specifying `xxx.CreateXXXRequest` .
The naming convention is ${service}.Create${apiName}Request .
**${service}** is the service name in lowercase, such as vpc.
**${apiName}** is the name of the API operation, such as DescribePhysicalConnections.

```
request := vpc.CreateDescribePhysicalConnectionsRequest() request.InstanceId = ""
```

4. Send the request.

```
response, err := vpcClient.DescribePhysicalConnections(request)
```

#### 5.2.4 Handle errors

| ClientError |   | or a | ServerError |   |
|---|---|---|---|---|
| e included in | sdk.errors |   |   | . The er |

interface and can be handled in a similar way as standard Go errors. You can run the following code to handle errors:

```
response,err := vpcClient.DescribePhysicalConnections(request) if err != nil {
    // Obtain the error information.
   err.Error()
```

**ClientError**

If an error occurs in the SDK when you send a request and the error cannot be automatically handled, the SDK returns a `ClientError` . or SDK for Go The following code shows how to determine and obtain the information about the error in a `ClientError` :

> **Important:** When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Specify the error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

`)`

```
response, err := vpcClient.DescribePhysicalConnections(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The returned value may be nil.
    clientError.OriginError()
```

**ServerError**

The SDK wraps the error returned by the server into a `ServerError` and returns it to the client. In this case, you can still obtain the original HTTP response. The following code shows how to determine and obtain the error message in a ServerError and Response:

> **Important:** When you use a specific error struct, you must add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/vpc" // Replace vpc with the name of the service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // Specify the error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

> `)`

```
response, err := vpcClient.DescribePhysicalConnections(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

#### 5.2.5 Use CommonRequest to call APIs

If you want to call the API of a cloud service that does not provide an SDK, or the requests and responses do not meet your business requirements, you can use CommonRequest. CommonRequest supports all API operations.

**Example: Call an RPC API**

The `DescribePhysicalConnections` operation of Express Connect is used as an example to show how to make an RPC API call to query the status of instances. or SDK for Go

> **Note:** Replace the preceding variables with your actual information. Remove the angle brackets (<>) when you specify the parameters.
> Variables:
> <yourRegionID>: Replace it with your region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <vpc.aliyuncs.com>: Replace it with the endpoint of the service.
> <yourSecurityToken>: Replace it with your security token.
> <yourResourceGroupID>: Replace it with your resource set ID.
> <yourOrganizationID>: Replace it with your organization ID.
> <yourInstanceID>: Replace it with the instance ID.

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",        //Replace it with your region ID.
        "<yourAccessKeyID>",     //Replace it with your AccessKey ID.
        "<yourAccessKeySecret>") //Replace it with your AccessKey secret.
    if err != nil {
        panic(err)
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<vpc.aliyuncs.com>" // Replace it with the endpoint of the service.
    request.Product = "Vpc"
    request.Version = "2016-04-28"
    // This is an RPC API operation. Therefore, the APIName(Action) parameter must be specified.
    request.ApiName = "DescribePhysicalConnections"
    // Set the service-related parameters.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use STS credentials to call an RPC API operation, you must specify the STS token.
     In this case, set the following parameter:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Specify your security token.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Optional. Specify the API caller.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Specify your region ID. This paramete
r is required if you use Apsara Stack Enterprise 3.15 or earlier.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Specify the resource se
t ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Optional. Specify the organization
ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Specify the instance ID. This
parameter is required if you want to modify, delete, or query the detailed information about an instance.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
    fmt.Print(response.GetHttpContentString())
```

## 6 API Reference

### 6.1 List of operations by function

The following tables list API operations available for use in Express Connect.

| API | Description |
|---|---|
| Express Connect circuits |   |
| CreatePhysicalConnection | Applies for an Express Connect circuit. |
| DescribeAccessPoints | Queries the access points in a specified region. You can call the ConnectRouterInterface operation to enable an initiator router interface to send a connection request to an acceptor router interface. |
| CancelPhysicalConnection | Cancels the application of an Express Connect circuit. |
| DescribePhysicalConnections | Queries connections over Express Connect circuits. |
| ModifyPhysicalConnectionAttribute | Modifies a connection over an Express Connect circuit. |
| TerminatePhysicalConnection | Disables a connection over an Express Connect circuit. |
| EnablePhysicalConnection | Enables a connection over an Express Connect circuit in the Confirmed state. |
| DeletePhysicalConnection | Deletes a connection over an Express Connect circuit. |
| CreatePhysicalConnectionOccupancyOr der | Creates an order for resource occupation. |
| ApplyPhysicalConnectionLOA | Applies for a Letter of Authorization (LOA). |
| CreatePhysicalConnectionSetupOrder | Creates an order for installing an Express Connect circuit. |
| CompletePhysicalConnectionLOA | Confirms that the installation of an Express Connect circuit is completed. |
| DescribePhysicalConnectionLOA | Queries the LOA of an Express Connect circuit. |
| VBRs |   |
| CreateVirtualBorderRouter | Creates a virtual border router (VBR). |
| DeleteVirtualBorderRouter | Deletes a VBR. |
| ModifyVirtualBorderRouterAttribute | Modifies a VBR. |
| DescribeVirtualBorderRouters | Queries VBRs. |
| DescribeVirtualBorderRoutersForPhysic alConnection | Queries VBRs on a specified Express Connect circuit, including VBRs that belong to the owner of the Express Connect circuit, and VBRs that belong to the tenants of the Express Connect circuit. |
| TerminateVirtualBorderRouter | Disables a VBR. |
| RecoverVirtualBorderRouter | Resumes a VBR. |
| AssociatePhysicalConnectionToVirtualB orderRouter | Associates a VBR with a connection over an Express Connect circuit. |
| UnassociatePhysicalConnectionFromVir tualBorderRouter | Disassociates a VBR from a connection over an Express Connect circuit. |
| BGP |   |
| CreateBgpGroup | Creates a Border Gateway Protocol (BGP) group for a specified VBR. |
| DescribeBgpGroups | Queries BGP groups in a specified region. |
| ModifyBgpGroupAttribute | Modifies the configuration of BGP groups. |

| DeleteBgpGroup | Deletes a specified BGP group. |
|---|---|
| CreateBgpPeer | Adds a BGP peer to a specified BGP group. |
| DescribeBgpPeers | Queries BGP peers in a specified region. |
| ModifyBgpPeerAttribute | Modifies a BGP peer. |
| DeleteBgpPeer | Deletes a specified BGP peer. |
| AddBgpNetwork | Advertises a BGP CIDR block. |
| DescribeBgpNetworks | Queries advertised BGP CIDR blocks. |
| DeleteBgpNetwork | Deletes an advertised BGP CIDR block. |
| Router interfaces |   |
| CreateRouterInterface | Creates a router interface. |
| ConnectRouterInterface | Enables an initiator router interface to send a connection request to an acceptor router interface. |
| DeactivateRouterInterface | Disables a router interface. |
| ModifyRouterInterfaceSpec | Modifies the specification of a router interface. |
| DeleteRouterInterface | Deletes a router interface. |
| DescribeRouterInterfaces | Queries router interfaces in a specified region. |
| ActivateRouterInterface | Enables a router interface that is in the Inactive state. |
| ModifyRouterInterfaceAttribute | Modifies the configurations of a router interface. |

### 6.2 Invoke APIs

#### 6.2.1 Request syntax

To call an Express Connect API operation, you must send an HTTP GET request to the endpoint of the Express Connect API. You must specify the request parameters for the operation. A response is returned for each request. Both requests and responses are encoded in UTF-8. Express Connect API operations use the RPC protocol. You can call Express Connect API operations by sending HTTP GET requests. The request syntax is as follows:

```
http://Endpoint/?Action=xx&Parameters
```

Where:
**Endpoint**: The endpoint of the Express Connect API is `vpc.example.com` .
`example.com` is a custom domain name of the project. For more information, see Obtain the endpoint of Express Connect.
**Action**: The operation that you want to perform. For example, you can call CreateRouterInterface to create a
router interface.
**Version**: The version number of the API. The API version number for Virtual Private Cloud (VPC) is 2016-04-28.
**Parameters**: The request parameters. Separate multiple parameters with ampersands (&).
Request parameters include common parameters and operation-specific parameters. Common parameters include the API version number and authentication information. For more information, see Common parameters. The following example shows how to call the CreateRouterInterface operation to create a router interface:

> **Note:** The sample request is formatted to improve readability.

```
https://vpc.example.com/?Action=CreateRouterInterface &Format=xml &Version=2016-04-28 &Signature=xxxx%xxxx%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2012-06-01T12:00:00Z
```

#### 6.2.2 Authorization

To ensure the security of your account, we recommend that you call Express Connect API operations as a RAM user. To do so, you must create and add an authorization policy that grants permissions to call specific API operations. For more information about the Express Connect resources and API operations that allow the authorization, see RAM authentication.

#### 6.2.3 Signature

You must sign all API requests to ensure security. Request signatures are used to verify the identities of API callers. Express Connect implements symmetric encryption with an AccessKey pair to verify the identity of the request sender. An AccessKey pair is an identity credential issued to Alibaba Cloud accounts and RAM users that is similar to a logon username and password. An AccessKey pair consists of an AccessKey ID and an AccessKey secret. The AccessKey ID is used to verify the identity of the user, while the AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to create an AccessKey pair, see Obtain an AccessKey pair. You must add the signature to the API request in the following format:

```
 https://endpoint/?SignatureVersion=1.0&SignatureMethod=HMAC-
SHA1&Signature=xxxx%xxxx%3D&SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf
```

Take CreateRouterInterface as an example. Assume that the AccessKey ID is `testid` and the AccessKey secret is `testsecret` , the original request URL is shown in the following content:

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

Perform the following operations to calculate the signature:
1. Use the request parameters to create a string-to-sign.

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeVpcs&Format%3DXML&SignatureMethod%3DHMAC- SHA1&SignatureNonce%3D3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf&SignatureVersion%3D1.0&TimeStamp%3D2016-02-23T 12%253A46%253A24Z&Version%3D2014-05-15
```

2. Calculate the HMAC value of the string to be signed.
Add an ampersand (&) after the AccessKey secret as the key to calculate the HMAC value. In this example, the key is `testsecret&` .

```
CT9X0VtwR86fNWSnsc6v8YGOjuE=
```

3. Add the signature string to the request:

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0 &Signature=xxxx%xxxx%3D
```

### 6.3 RAM authentication

Before you call an Express Connect operation as a RAM user, you must use an Apsara Stack tenant account to create an authorization policy to grant permissions to the RAM user. In the authorization policy, an Alibaba Cloud Resource Name (ARN) is used to specify a resource.

**Resource types that can be authorized**

The following table lists the Express Connect resources that allow authorized access and their ARNs.

| Resource type | ARN |
|---|---|
| VPCs | acs:vpc:$regionid:$accountid:vpc/$vpcid |
|   | acs:vpc:$regionid:$accountid:vpc/* |
|   | acs:vpc:*:$accountid:vpc/* |
| VRouters | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
|   | acs:vpc:$regionid:$accountid:vrouter/* |
|   | acs:vpc:*:$accountid:vrouter/* |
| VSwitches | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
|   | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:*:$accountid:vswitch/* |
| Route tables | acs:vpc:$regionid:$accountid:routetable/$routetableid |
|   | acs:vpc:$regionid:$accountid:routetable/* |
|   | acs:vpc:*:$accountid:routetable/* |
| Elastic IP addresses (EIPs) | acs:vpc:$regionid:$accountid:eip/$allocationid |
|   | acs:vpc:$regionid:$accountid:eip/* |
|   | acs:vpc:*:$accountid:eip/* |
| NAT gateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |
|   | acs:vpc:$regionid:$accountid:natgateway/* |
|   | acs:vpc*:$accountid:vpc/* |
| NAT bandwidth packages | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |
|   | aacs:vpc:*:$accountid:vpc/* |
|   | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |
| > Document Version: 2 | 0260828 36 |

| Developer Guide·API R | eference Express Connec |
|---|---|
| Forwarding tables |   |
|   | acs:vpc:$regionid:$accountid:forwardtable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| SNAT tables | acs:vpc:$regionid:$accountid:snattable/$snattableid |
|   | acs:vpc:$regionid:$accountid:snattable/* |
|   | acs:vpc:*:$accountid:vpc/* |
| General resources | acs:vpc:$regionid:$accountid:* |
|   | acs:vpc:*:$accountid:* |

$regionid/accountid/vrouterid indicates the ID of the specified resource, and `*` indicates all resources.

**API operations that allow authorized access**

The following table lists the Express Connect API operations that allow authorized access and their ARNs.

| Operation | ARN |
|---|---|
| vpc:CreateVpc | acs:vpc:$regionid:$accountid:vpc/* |
| vpc:DeleteVpc | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVpcs | vpc:$regionid:$accountid:vpc/* |
| vpc:ModifyVpcAttribute | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DescribeVRouters | acs:vpc:$regionid:$accountid:vrouter/* |
|   | The VRouter ID is specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
|   | The VRouter ID is not specified: "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/*" |
| vpc:ModifyVRouterAttribute | acs:vpc:$regionid:$accountid:vrouter/$vrouterid |
| vpc:CreateVSwitch | acs:vpc:$regionid:$accountid:vswitch/* |
|   | acs:vpc:$regionid:$accountid:vpc/$vpcid |
| vpc:DeleteVSwitch | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:DescribeVSwitches | acs:vpc:$regionid:$accountid:vswitch/* |
|   | "vpc:Vpc":"acs:vpc:$regionid:$accountid:vpc/$vpcid" |
| vpc:ModifyVSwitchAttribute | acs:vpc:$regionid:$accountid:vswitch/$vswitchid |
| vpc:CreateRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |
| vpc:DeleteRouteEntry | acs:vpc:$regionid:$accountid:routetable/$routetableid |
| vpc:DescribeRouteTables | acs:vpc:$regionid:$accountid:routetable/* |
|   | "vpc:VRouter":"acs:vpc$regionid:$accountid:vrouter/$vrouterid" |
| vpc:AllocateEipAddress | acs:vpc:$regionid:$accountid:eip/* |
| A i t Ei Add | acs:vpc:$regionid:$accountid:eip/* |
| 37 | > Document Version: 20260828 |

| Express Connect | Developer Guide·API Reference |   |
|---|---|---|
| vpc:AssociateEipAddres | Associates an EIP with an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:eip/* Disassociates an EIP from an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:eip/$allocationid acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:natgateway/* acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:vpc:$regionid:$accountid:natgateway/* acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:natgateway/$natgatewayid acs:ecs:$regionid:$accountid:instance/$instanceid acs:vpc:$regionid:$accountid:bandwidthpackage/* acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/* acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
|   | Associates an EIP with an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |
| vpc:DescribeEipAddresses | acs:vpc:$regionid:$accountid:eip/* |   |
| vpc:UnassociateEipAddress | Disassociates an EIP from an ECS instance. acs:vpc:$regionid:$accountid:eip/$allocationid acs:ecs:$regionid:$accountid:instance/$instanceid |   |
| vpc:ReleaseEipAddress | acs:vpc:$regionid:$accountid:eip/$allocationid |   |
| vpc:DescribeEipMonitorData | acs:vpc:$regionid:$accountid:eip/$allocationid |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |
| vpc:CreateNatGateway | acs:vpc:$regionid:$accountid:natgateway/* |   |
| vpc:DescribeNatGateways | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
|   | acs:vpc:$regionid:$accountid:natgateway/* |   |
| vpc:ModifyNatGatewaySpec | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
| vpc:ModifyNatGatewayAttribute | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |
| vpc:DeleteNatGateway | acs:vpc:$regionid:$accountid:natgateway/$natgatewayid |   |
|   | acs:ecs:$regionid:$accountid:instance/$instanceid |   |
| vpc:CreateBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:DescribeBandwidthPackages |   |   |
|   | acs:vpc:$regionid:$accountid:bandwidthpackage/* |   |
| vpc:ModifyBandwidthPackageSpec | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:ModifyBandwidthPackageAttribute | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:AddBandwidthPackageIps | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:RemoveBandwidthPackageIps | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:DeleteBandwidthPackage | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |   |
|   |   | acs:vpc:$regionid:$accountid:bandwidthpackage/$bandwidthpackageid |
| vpc:CreateForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:DeleteForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:ModifyForwardEntry | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |
| vpc:DescribeForwardTableEntries | acs:vpc:$regionid:$accountid:forwardtable/$forwardtableid |   |

| vpc:CreateSnatEntry | acs:vpc:$regionid:$accountid:snattable/* |
|---|---|
| vpc:ModifySnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |
| vpc:DescribeSnatTableEntries | acs:vpc:$regionid:$accountid:snattable/$snattableid |
| vpc:DeleteSnatEntry | acs:vpc:$regionid:$accountid:snattable/$snattableid |

### 6.4 Common parameters

This topic describes the common parameters that are required for calling Express Connect API operations.

**Common request parameters**

Common request parameters must be included in all Express Connect API requests. Table 1. Common request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|
| Format | String | No | The format in which to return the response. Valid values: JSON and XML. Default value: XML. |
| Version | String | Yes | The version number of the API. Format: YYYY-MM-DD . Set the value to 2016-04-28 |
| AccessKeyId | String | Yes | The AccessKey ID provided to you by Alibaba Cloud. |
| Signature | String | Yes | The signature string of the current request. |
| SignatureMetho d | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1 |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2013-01-10T12:00:00Z. |
| SignatureVersio n | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0 |
| SignatureNonce | String | Yes | A unique and random number used to prevent replay attacks. You must use different numbers for different requests. |

Examples

```
http://vpc.example.com/?Action=CreateRouterInterface &Timestamp=2016-02-23T12:46:24Z &Format=XML &AccessKeyId=testid &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2016-04-28 &SignatureVersion=1.0
```

**Common response parameters**

API responses use the HTTP response format where a 2xx status code indicates a successful call and a 4xx or 5xx status code indicates a failed call. Responses can be returned in either the JSON or XML format. You can specify the response format in the request. The default response format is XML. Every response returns a unique **RequestId** regardless of whether the call is successful. XML format

```xml
<? xml version="1.0" encoding="utf-8"? >
      <!—Result Root Node-->
      <Interface Name+Response>
      <!—Return Request Tag-->
      <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
      <!—Return Result Data-->
      </Interface Name+Response>
```

JSON format `{`

```json
      "RequestId":"4C467B38-3910-447D-87BC-AC049166F216",
      /*Return Result Data*/
```

### 6.5 Physical connections

#### 6.5.1 CreatePhysicalConnection

Applies for an Express Connect circuit.

**Descriptions**

After your application is approved, the Express Connect circuit changes to the **Initial** state. You can contact the Internet service provider (ISP) to start construction. When you call this operation, take note of the following limits: If your Apsara Stack tenant account has more than five Express Connect circuits that are not in the **Enabled** state, you cannot apply for another Express Connect circuit. If your account has an Express Connect circuit with overdue payments, you cannot apply for another Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConne ction | The operation that you want to perform. Set the value to CreatePhysicalConnection. |
| AccessPointId | String | Yes | ap-cn-beijing-**** | The ID of the access point to which the Express Connect circuit belongs. |
| ClientToken | String | Yes | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LineOperator | String | Yes | CT | The ISP of the Express Connect circuit. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in mainland China Equinix: Equinix Other: other ISPs outside mainland China |
| PeerLocation | String | Yes | XX street | The geographical location of the data center. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| Type | String | No | VPC | The type of the Express Connect circuit. Default value: VPC. |
| bandwidth | Integer | No | 10 | The bandwidth value of the bandwidth plan. Unit: Mbit/s. Valid values: 5 to 5000. |
| PortType | String | No | 1000Base-T | The port type of the Express Connect circuit. Valid values: 100Base-T: a copper port that supports 100 Mbit/s of bandwidth 1000Base-T: a copper port that supports 1,000 Mbit/s of bandwidth 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s of bandwidth (10 kilometers) 10GBase-T: a copper port that supports 10,000 Mbit/s of bandwidth 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s of bandwidth (10 kilometers) |
| RedundantPhysicalC onnectionId | String | No | pc-119mfjzm7****** | The ID of the standby Express Connect circuit. The standby Express Connect circuit must be in the Allocated, Confirmed, or Enabled state. |
| Description | String | No | Description | The description of the Express Connect circuit. The description must be 2 to 256 characters in length. It must start with a letter and cannot start with http:// or https:// . |
| Name | String | No | test | The name of the Express Connect circuit. The name must be 2 to 128 characters in length and can contain digits, underscores ( ), _ and hyphens (-). It must start with a letter, but cannot start with http:// or https:// . |
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) of the Express Connect circuit. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nId | String | pc-bp12mw****** | The ID of the Express Connect circuit. |
| RequestId | String | 8A6A5EC5-6F6C-4906- 9689-56ACE58A13E0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnection &AccessPointId=ap-cn-beijing-**** &ClientToken=123e4567-e89b-12d3-a456-426655440000 &LineOperator=CT &PeerLocation=XX street &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionResponse>
      <RequestId>8A6A5EC5-6F6C-4906-9689-56ACE58A13E0</RequestId>
      <PhysicalConnectionId>pc-bp12mw******</PhysicalConnectionId>
</CreatePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "CreatePhysicalConnectionResponse": {
        "RequestId": "8A6A5EC5-6F6C-4906-9689-56ACE58A13E0",
        "PhysicalConnectionId": "pc-bp12mw******"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccessPointId.Not Enabled | Invalid access point status. | The error message returned because the access point is unavailable. |
| 400 | InvalidType.Malformd | The Type provided was invalid. | The error message returned because Type is set to an invalid value. |
| 400 | InvalidPeerLocation.Malf ormd | The PeerLocation provided was invalid. | The error message returned because PeerLocation is set to an invalid value. |
| 400 | InvalidLineOperator.Malf ormd | The LineOperator provided was invalid. | The error message returned because LineOperator is set to an invalid value. |
| 400 | InvalidPortType.Malform d | The PortType provided was invalid. | The error message returned because the specified port type is invalid. |
| 400 | InvalidDescription.Malfor med | The specifid ?Description? is not valid. | The error message returned because the format of the resource description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | InvalidRedundantPhysic alConnectionId.NotFoun d | The RedundantPhysicalConnectionId does not found. | The error message returned because the specified standby Express Connect circuit does not exist. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | QuotaExceeded.pConnP erAP | Physical connection count per ap quota exceed. | The error message returned because the number of Express Connect circuits that are associated with the specified access point has reached the upper limit. |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | The error message returned because the specified bandwidth value of the Express Connect circuit is invalid. |

| 400 | InvalidRedundantPhysic alConnection | redundant physical connection doesn't belong to current user. | The error message returned because the specified standby Express Connect circuit does not belong to your Apsara Stack tenant account. |
|---|---|---|---|
| 400 | InvalidRedundantPhysic alConnectionStatus | invalid redundant physical connection status. | The error message returned because the standby Express Connect circuit is in an invalid state. |
| 400 | InvalidCircuitCode.Malfo rmed | circuitCode is illegal. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | QuotaExceeded.freePco nnPerAP | free physical connections count excceeded. | The error message returned because the quota on Express Connect circuits is reached. |

#### 6.5.2 DescribeAccessPoints

Queries the access points of Express Connect circuits in a specified region.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessPoint s | The operation that you want to perform. Set the value to DescribeAccessPoints. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the access point. You can call the DescribeRegions operation to query the most recent region list. |
| Filter.N.Key | String | No | name | Specifies filter conditions. You can specify at most five filter conditions. |
| Filter.N.Value.N | RepeatList | No | test | Specifies filter values based on keys. You can specify multiple filter values for one key. The logical operator between filter values is OR. If one filter value is matched, the filter condition is matched. |
| Type | String | No | VPC | The network type of the Express Connect circuit. Default value: VPC. |
| Name | String | No | Hangzhou-Yuhang-C | The name of the access point. |
| HostOperator | String | No | China Telecom | The Internet service provider (ISP) of the access point. Valid values: China Mobile China Unicom China Telecom Other ISPs in China ISPs outside China |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessPointSet | Array of AccessPointType |   | The information about the access points. |
| AccessPointType |   |   |   |
| AccessPointId | String | ap-cn-hangzhou-**** | The ID of the access point. |
| AttachedRegionNo | String | cn-qingdao-env66-d01 | The region ID of the access point. |
| Description | String | Access point description | The description of the access point. |
| HostOperator | String | China Telecom | The Internet service provider (ISP) of the access point. Valid values: China Mobile China Unicom China Telecom Other ISPs in China ISPs outside China |
| Location | String | Qingdao | The geographical location of the access point. |
| Name | String | Qingdao-Laoshan-A | The name of the access point. |
| Status | String | recommended | The status of the access point. Valid values: recommended: The access point is ready for use. hot: A large number of Express Connect circuits are connected to the access point. full: The number of Express Connect circuits connected to the access point has reached the upper limit. disabled: The access point is unavailable. |
| Type | String | VPC | The network type of the Express Connect circuit. |
| TotalCount | Integer | 5 | The number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |
| RequestId | String | 3E85D803-C7CF-4BCD- 9CFE-6DBA1DFFA027 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAccessPoints &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeAccessPointsResponse>
      <AccessPointSet>
            <Status>recommended</Status>
            <Type>VPC</Type>
            <Description>ap-cn-hangzhou-dq-A-EU95</Description>
            <AttachedRegionNo>cn-qingdao-env66-d01</AttachedRegionNo>
            <HostOperator>China Telecom</HostOperator>
            <AccessPointId>ap-cn-hangzhou-xs-D</AccessPointId>
            <Name>Qingdao-Laoshan-A</Name>
            <Location>Qingdao</Location>
      </AccessPointSet>
      <TotalCount>5</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027</RequestId>
      <PageNumber>1</PageNumber>
</DescribeAccessPointsResponse>
```

`JSON` format `{`

```json
    "DescribeAccessPointsResponse": {
        "AccessPointSet": {
            "Status": "recommended",
            "Type": "VPC",
            "Description": "ap-cn-hangzhou-dq-A-EU95",
            "AttachedRegionNo": "cn-qingdao-env66-d01",
            "HostOperator": "China Telecom",
            "AccessPointId": "ap-cn-hangzhou-xs-D",
            "Name": "Qingdao-Laoshan-A",
            "Location": "Qingdao"
```

`},`

```json
        "TotalCount": 5,
        "PageSize": 10,
        "RequestId": "3E85D803-C7CF-4BCD-9CFE-6DBA1DFFA027",
        "PageNumber": 1
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotSupp ort | The RegionId provided does not support in our records. | The error message returned because the specified region ID is invalid. |

#### 6.5.3 CancelPhysicalConnection

Cancels an Express Connect circuit before it is enabled. After you cancel an Express Connect circuit, it changes to the **Canceled** state.

**Limits**

You can cancel only an Express Connect circuit that is in the **Initial**, **Approved**, **Allocated**, or **Confirmed** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CancelPhysicalConne ction | The operation that you want to perform. Set the value to CancelPhysicalConnection. |
| PhysicalConnectionId | String | Yes | pc-119mf**** | The ID of the Express Connect circuit. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CancelPhysicalConnection &PhysicalConnectionId=pc-119mf**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CancelPhysicalConnectionResponse>
      <RequestId>BE36E95A-F83E-4127-A29E-F2F35D4C999A</RequestId>
</CancelPhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedIn State | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### 6.5.4 DescribePhysicalConnections

Queries Express Connect circuits in a region.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribePhysicalCon nections | The operation that you want to perform. Set the value to DescribePhysicalConnections . |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 10 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| Filter.N.Key | String | No | 1 | The filter condition. Valid values of N are 1 to 5. The following filter conditions are supported: PhysicalConnectionId: the ID of the Express Connect circuit AccessPointId: the ID of the access point Type: the type of the Express Connect circuit LineOperator: the Internet service provider (ISP) of the Express Connect circuit Spec: the specification of the Express Connect circuit Status: the status of the Express Connect circuit Name: the name of the Express Connect circuit The logical relation between values in a filter condition is OR, which means that the filter condition is met if one of the values is met. The logical relation between filter conditions is AND. In this case, the result is returned only when all conditions are met. |
| Filter.N.Value.N | RepeatList | No | 1 | The value of the filter condition. Valid values of N are 1 to 5. |
| IncludeReservationD ata | Boolean | No | false | Specifies whether to return the orders that have not taken effect. true: yes false (default): no |
| ClientToken | String | No | 23243242rggy**** | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nSet | Array of PhysicalConnectio nType |   | The details about the Express Connect circuits. |

| PhysicalConnectio nType |   |   |   |
|---|---|---|---|
| AccessPointId | String | eip- 2zeerraiwb7uj6i0******* | The ID of the access point. |
| AdLocation | String | Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen, Guangdong | The geographical location of the access device. |
| Bandwidth | Long | 10 | The bandwidth of the Express Connect circuit. Unit: Mbit/s. |
| BusinessStatus | String | Normal | The payment status of the Express Connect circuit. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked for security reasons |
| ChargeType | String | Prepaid | The billing method. The value is set to Prepaid, which indicates the subscription billing method. |
| CircuitCode | String | longtel001 | The circuit code provided by the ISP for the Express Connect circuit. |
| CreationTime | String | 2017-06-08T12:20:55 | The time when the Express Connect circuit was created. |
| Description | String | The Express Connect circuit | The description of the Express Connect circuit. |
| EnabledTime | String | 2017-06-08T12:20:55 | The time when the Express Connect circuit was enabled. |
| EndTime | String | 2019-02-25T11:01:04Z | The time when the Express Connect circuit expires. |
| HasReservationDa ta | String | true | Indicates whether you have subscription messages. true: yes false: no |
| LineOperator | String | CT | The ISP of the Express Connect circuit. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other ISPs in China Equinix: Equinix Other: other ISPs outside China |
| LoaStatus | String | Available | The status of the letter of authorization (LOA). |
| Name | String | name | The name of the Express Connect circuit. |

| PeerLocation | String | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |
|---|---|---|---|
| PhysicalConnectio nId | String | pc-119mfjzm***** | The ID of the Express Connect circuit. |
| PortNumber | String | 80 | The port number of the access device. |
| PortType | String | 1000Base-T | The port type of the Express Connect circuit. Valid values: 100Base-T: a copper port that supports 100 Mbit/s of bandwidth 1000Base-T: a copper port that supports 1,000 Mbit/s of bandwidth 1000Base-LX: a single-mode fiber port that supports 1,000 Mbit/s of bandwidth (10 kilometers) 10GBase-T: a copper port that supports 10,000 Mbit/s of bandwidth 10GBase-LR: a single-mode fiber port that supports 10,000 Mbit/s of bandwidth (10 kilometers) |
| RedundantPhysical ConnectionId | String | pc-119mfjzm******* | The ID of the standby Express Connect circuit. |
| ReservationActive Time | String | 2019-02-25T11:01:04Z | The time when the renewal takes effect. |
| ReservationInterne tChargeType | String | PayByBandwidth | The renewal type. |
| ReservationOrderT ype | String | RENEW | The type of the renewal order. |
| Spec | String | Large | The specification of the Express Connect circuit. |
| Status | String | Initial | The status of the Express Connect circuit. Valid values: Initial: pending approval Approved: approved Allocating: allocating resources Allocated: under construction Confirmed: waiting for user confirmation Enabled: enabled Rejected: rejected Canceled: canceled Allocation Failed: resource allocation failed Terminated: disabled |
| Type | String | VPC | The type of the Express Connect circuit. Default value: VPC. |
| TotalCount | Integer | 10 | The total number of entries returned. |
| PageNumber | Integer | 10 | The number of the page returned. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned on each page. Maximum value: 50. Default value: 10. |

| RequestId | String | EEC8EAB1-F299-4F5C- 8E54-0A3129164C27 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnections &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionsResponse>
      <PhysicalConnectionSet>
            <Status>Initial</Status>
            <Description>Express Connect circuit</Description>
            <EndTime>2019-02-25T11:01:04Z</EndTime>
            <LineOperator>CT</LineOperator>
            <CircuitCode>longtel001</CircuitCode>
            <PhysicalConnectionId>pc-119mfjzm*****</PhysicalConnectionId>
            <HasReservationData>true</HasReservationData>
            <RedundantPhysicalConnectionId>pc-119mfjzm*******</RedundantPhysicalConnectionId>
            <PeerLocation>Building XX, XX Avenue, XX District, Hangzhou, Zhejiang</PeerLocation>
            <BusinessStatus>Normal</BusinessStatus>
            <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
            <Name>name</Name>
            <ReservationOrderType>RENEW</ReservationOrderType>
            <LoaStatus>Available</LoaStatus>
            <Type>VPC</Type>
            <AdLocation>Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen,
Guangdong</AdLocation>
            <ChargeType>Prepaid</ChargeType>
            <Bandwidth>10</Bandwidth>
            <CreationTime>2017-06-08T12:20:55</CreationTime>
            <AccessPointId>eip-2zeerraiwb7uj6i0*******</AccessPointId>
            <EnabledTime>2017-06-08T12:20:55</EnabledTime>
            <ReservationActiveTime>2019-02-25T11:01:04Z</ReservationActiveTime>
            <PortNumber>80</PortNumber>
            <Spec>Large</Spec>
            <PortType>1000Base-T</PortType>
      </PhysicalConnectionSet>
      <TotalCount>10</TotalCount>
      <PageSize>10</PageSize>
      <RequestId>EEC8EAB1-F299-4F5C-8E54-0A3129164C27</RequestId>
      <PageNumber>10</PageNumber>
</DescribePhysicalConnectionsResponse>
```

`JSON` format `{`

```json
    "PhysicalConnectionSet": {
        "Status": "Initial",
        "Description": "Express Connect circuit",
        "EndTime": "2019-02-25T11:01:04Z",
        "LineOperator": "CT",
        "CircuitCode": "longtel001",
        "PhysicalConnectionId": "pc-119mfjzm*****",
        "HasReservationData": true,
        "RedundantPhysicalConnectionId": "pc-119mfjzm*******",
        "PeerLocation": "Building XX, XX Avenue, XX District, Hangzhou, Zhejiang",
        "BusinessStatus": "Normal",
        "ReservationInternetChargeType": "PayByBandwidth",
        "Name": "name",
        "ReservationOrderType": "RENEW",
        "LoaStatus": "Available",
        "Type": "VPC",
        "AdLocation": "Ax-x Bxx, Building xx, xxx Base, Binhai Boulevard, Nanshan District, Shenzhen,
Guangdong",
        "ChargeType": "Prepaid",
        "Bandwidth": 10,
        "CreationTime": "2017-06-08T12:20:55",
        "AccessPointId": "eip-2zeerraiwb7uj6i0*******",
        "EnabledTime": "2017-06-08T12:20:55",
        "ReservationActiveTime": "2019-02-25T11:01:04Z",
        "PortNumber": 80,
        "Spec": "Large",
        "PortType": "1000Base-T"
```

`},`

```json
    "TotalCount": 10,
    "PageSize": 10,
    "RequestId": "EEC8EAB1-F299-4F5C-8E54-0A3129164C27",
    "PageNumber": 10
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |

#### 6.5.5 ModifyPhysicalConnectionAttribute

Modifies the configurations of an Express Connect circuit.

**Usage notes**

Before you call this operation, take note of the following limits: You can modify the specifications and the redundant Express Connect circuit ID of an Express Connect circuit that is in the **Initial**, **Enabled**, or **Rejected** state. You cannot modify the configurations of an Express Connect that is in the **Canceled**, **Allocating**,
**AllocationFailed**, or **Terminated** state.
After you modify the configurations of an Express Connect that is in the **Rejected** state, the Express Connect enters the **Initial** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyPhysicalConne ctionAttribute | The operation that you want to perform. Set the value to ModifyPhysicalConnectionAttribute. |

| PhysicalConnectionId | String | Yes | pc-119mfjzm**** | The ID of the Express Connect circuit that you want to modify. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| LineOperator | String | No | CT | The connectivity provider of the Express Connect circuit. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other connectivity providers in the Chinese mainland Equinix: Equinix Other: other connectivity providers outside the Chinese mainland |
| bandwidth | Integer | No | 5 | The new bandwidth value for the Express Connect circuit. Valid values: 2 to 10240. Unit: Mbit/s. |
| PeerLocation | String | No | Building XX, XX Avenue, XX District, Hangzhou, Zhejiang | The geographical location of the data center. |
| PortType | String | No | 1000Base-LX | The type of the Express Connect circuit. Valid values: 100Base-T: 100 Mbit/s copper Ethernet port 1000Base-T (default): 1,000 Mbit/s copper Ethernet port 1000Base-LX: 1,000 Mbit/s single-mode optical port (10 km) 10GBase-T: 10,000 Mbit/s copper Ethernet port 10GBase-LR: 10,000 Mbit/s single-mode optical port (10 km) |
| RedundantPhysicalC onnectionId | String | No | pc-119mfjzm7**** | The ID of the redundant Express Connect circuit. The redundant Express Connect circuit must be in the Allocated, Confirmed, or Enabled state. |
| Description | String | No | Description | The description of the Express Connect circuit. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | Name | The name of the Express Connect circuit. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must _ start with a letter but cannot start with http:// or https:// . |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
|---|---|---|---|---|
| CircuitCode | String | No | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 013EE132-A109-4247- 91B0-099A8FF49AD7 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyPhysicalConnectionAttribute &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyPhysicalConnectionAttributeResponse>
  <RequestId>013EE132-A109-4247-91B0-099A8FF49AD7</RequestId>
</ModifyPhysicalConnectionAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "013EE132-A109-4247-91B0-099A8FF49AD7"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the Express Connect circuit does not exist. |
| 400 | InvalidLineOperator.Malf ormd | The LineOperator provided was invalid. | The error message returned because LineOperator is set to an invalid value. |
| 400 | InvalidPeerLocation.Malf ormd | The PeerLocation provided was invalid. | The error message returned because PeerLocation is set to an invalid value. |
| 400 | InvalidPortType.Malform d | The PortType provided was invalid. | The error message returned because the specified port type is invalid. |

| 400 | InvalidDescription.Malfor med | The specifid ?Description? is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
|---|---|---|---|
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidStatus | invalid physical connection status. | The error message returned because the Express Connect circuit is in an invalid state. |
| 400 | InvalidBandwidth | invalid physical connection banwidth. | The error message returned because the specified bandwidth value of the Express Connect circuit is invalid. |
| 400 | InvalidRedundantPhysic alConnection | redundant physical connection doesn't belong to current user. | The error message returned because the specified standby Express Connect circuit does not belong to your Apsara Stack account. |
| 400 | InvalidRedundantPhysic alConnectionStatus | invalid redundant physical connection status. | The error message returned because the standby Express Connect circuit is in an invalid state. |
| 400 | InvalidCircuitCode.Malfo rmed | circuitCode is illegal. | The error message returned because CircuitCode is set to an invalid value. |

#### 6.5.6 TerminatePhysicalConnection

Disables an Express Connect circuit after it is enabled.

**Descriptions**

After you call this operation, the specified Express Connect circuit changes to the **Terminating** state. After the Express Connect circuit is disabled, it changes to the **Terminated** state. When you call this operation, take note of the following limits: You can only terminate an Express Connect circuit that is in the **Enabled** state. Before you disable an Express Connect circuit, you must delete the virtual border routers (VBRs) associated with it.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminatePhysicalCo nnection | The operation that you want to perform. Set the value to TerminatePhysicalConnection. |
| PhysicalConnectionId | String | Yes | pc-119mfjzm**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 513E0A50-4F2D-4CBE- BF35-40559DF65D79 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TerminatePhysicalConnection &PhysicalConnectionId=pc-119mfjzm**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminatePhysicalConnectionResponse>
      <RequestId>513E0A50-4F2D-4CBE-BF35-40559DF65D79</RequestId>
</TerminatePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "TerminatePhysicalConnectionResponse": {
        "RequestId": "513E0A50-4F2D-4CBE-BF35-40559DF65D79"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedIn State | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### 6.5.7 EnablePhysicalConnection

Enables an Express Connect circuit that is in the **Confirmed** state. After you enable an Express Connect circuit, it changes to the **Enabled** state.

**Descriptions**

When you call this operation, take note of the following limits: You can enable only an Express Connect circuit that is in the **Confirmed** state. After you enable an Express Connect circuit, it changes to the **Enabled** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnablePhysicalConne ction | The operation that you want to perform. Set the value to EnablePhysicalConnection. |
| PhysicalConnectionId | String | Yes | pc-119mfjz**** | The ID of the Express Connect circuit. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 0ED8D006-F706-4D23- 88ED-E11ED28DCAC0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnablePhysicalConnection &PhysicalConnectionId=pc-119mfjz**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EnablePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</EnablePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the Express Connect circuit does not exist. |
| 400 | Forbidden.NotAllowedIn State | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### 6.5.8 DeletePhysicalConnection

Deletes a physical connection.

> **Note:** You can delete only physical connections that are in the following states:**Rejected**,**Canceled**,**AllocationFailed**, and**Terminated**.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeletePhysicalConne ction | The operation that you want to perform. Set the value to DeletePhysicalConnection. |
| PhysicalConnectionId | String | Yes | pc- 119mfjzm7********* | The ID of the physical connection. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the physical connection is deployed. You can call the DescribeRegions operation to query region IDs. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 2B3670CD-670E-4540- 8C13-6DE929AEDD3B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=DeletePhysicalConnection &PhysicalConnectionId=pc-119mfjzm7********* &RegionId=cn-shanghai &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeletePhysicalConnectionResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</DeletePhysicalConnectionResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the specified physical connection does not exist. |
| 400 | Forbidden.NotAllowedIn State | The request does not allow in this state. | The error message returned because the state is invalid and the operation cannot be performed. |

| 400 | InvalidPhysicalConnectio nId.NotMatched | instance id not matched. | The error message returned because the instance ID does not match. |
|---|---|---|---|
| 400 | Forbidden.VBRExists | physical connection owner's vbr still exists. | The error message returned because the virtual border router (VBR) of the physical connection still exists. |
| 400 | Forbidden.VBRExists | vbr owner's vbr still exists. | The error message returned because the VBR still exists. |
| 400 | Forbidden.AssociateToV BR | The physical connection still associate to VBR. | The error message returned because the physical connection is already associated with a VBR. |

#### 6.5.9 CreatePhysicalConnectionOccupancyOrder

Creates an order for resource usage.

**Limits**

Only an Express Connect circuit that is in the **Pending** state supports this operation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreatePhysicalConne ctionOccupancyOrde r | The operation that you want to perform. Set the value to CreatePhysicalConnectionOccupancyOrde r. |
| PhysicalConnectionId | String | Yes | pc- bp1hp0wr072f6**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Period | Integer | No | 1 | The subscription duration. If PricingCycle is set to Month, set Period to a value from 1 to 9. If PricingCycle is set to Year, set Period to a value from 1 to 5. Note If InstanceChargeType is set to PrePaid, you must specify this parameter. You do not need to specify this parameter if InstanceChargeType is set to PostPaid. |
| InstanceChargeType | String | No | PostPaid | The billing method of the instance. Valid values: PrePaid: subscription If you choose this billing method, make sure that your Apsara Stack account supports balance payments or credit payments. PostPaid: pay-as-you-go. This is the default value. |

| AutoPay | Boolean | No | false | Specifies whether to enable automatic payment. Valid values: true: enables automatic payment. Make sure that you have a sufficient balance in your account. Otherwise, your order becomes invalid and is automatically canceled. false: disables automatic payment. This is the default value. |
|---|---|---|---|---|
| PricingCycle | String | No | Month | The unit of the subscription cycle. Valid values: Year Month |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9B9300FE-11E2-4E3B- 949C-BED3B44DD26D | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnectionOccupancyOrder &PhysicalConnectionId=pc-bp1hp0wr072f6**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionOccupancyOrder>
    <RequestId>9B9300FE-11E2-4E3B-949C-BED3B44DD26D</RequestId>
</CreatePhysicalConnectionOccupancyOrder>
```

`JSON` format `{`

```json
    "RequestId": "9B9300FE-11E2-4E3B-949C-BED3B44DD26D"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidPhysicalConnectio nId.NotFound | The PhysicalConnectionId provided does not exist in our records. | The error message returned because the Express Connect circuit does not exist. |
|---|---|---|---|
| 400 | Forbidden.NotAllowedIn State | The request does not allow in this state. | The error message returned because the operation cannot be performed when the Express Connect circuit in the current state. |

#### 6.5.10 ApplyPhysicalConnectionLOA

Applies for a Letter of Authorization (LOA) for an Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ApplyPhysicalConnec tionLOA | The operation that you want to perform. Set the value to ApplyPhysicalConnectionLOA. |
| CompanyName | String | Yes | company | The name of the customer company that requires the Express Connect circuit. |
| ConstructionTime | String | Yes | 2021-02- 28T16:00:00.000Z | The time when construction started. |
| InstanceId | String | Yes | pc- bp1qrb3044eqi**** | The ID of the Express Connect circuit. |
| LineType | String | Yes | FIBRE | The type of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect. You can call the DescribeRegions operation to query the most recent region list. |
| Si | String | Yes | Apsara Stack | The construction company. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
| Bandwidth | Integer | No | 3 | The bandwidth of the Express Connect circuit. |
| PeerLocation | String | No | Hangzhou | The geographical location of the Express Connect. |
| PMInfo.N.PMName | String | No | Tom | The name of the construction engineer. N is a natural number. Replace N with a value when you call this operation. |

| PMInfo.N.PMContactI nfo | String | No | 1320000**** | The contact information about the construction personnel. N is a natural number. Replace N with a value when you call this operation. |
|---|---|---|---|---|
| PMInfo.N.PMCertificat eType | String | No | IDCard | The ID type of the construction engineer. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMCertificat eNo | String | No | 3210xxxxxxxxxxxxxx | The identity number of the construction engineer. N is a natural number. Replace N with a value when you call this operation. |
| PMInfo.N.PMGender | String | No | Male | The gender of the construction engineer. N is a natural number. Replace N with a value when you call this operation. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | A47BD386-7FDE-42C4- 8D22-C6223D18AA1C | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ApplyPhysicalConnectionLOA &CompanyName=company &ConstructionTime=2021-02-28T16:00:00.000Z &InstanceId=pc-bp1qrb3044eqi**** &LineType=FIBRE &RegionId=cn-qingdao-env66-d01 &Si=Apsara Stack &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ApplyPhysicalConnectionLOAResponse>
  <RequestId>A47BD386-7FDE-42C4-8D22-C6223D18AA1C</RequestId>
</ApplyPhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "RequestId":"A47BD386-7FDE-42C4-8D22-C6223D18AA1C"
```

#### 6.5.11 CreatePhysicalConnectionSetupOrder

Creates an order for initial installation of an Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | CreatePhysicalConne ctionSetupOrder | The operation that you want to perform. Set the value to CreatePhysicalConnectionSetupOrder. |
|---|---|---|---|---|
| AccessPointId | String | Yes | ap-cn-qingdao-ft-A | The ID of the access point. |
| LineOperator | String | Yes | CT | The connectivity provider of the Express Connect circuit. Valid values: CT: China Telecom CU: China Unicom CM: China Mobile CO: other connectivity providers in the Chinese mainland Equinix: Equinix Other: other connectivity providers outside the Chinese mainland |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| PortType | String | No | 100Base-T | The port type. Valid values: 100Base-T: 100 Mbit/s copper Ethernet port 1000Base-T (default): 1,000 Mbit/s copper Ethernet port 1000Base-LX: 1,000 Mbit/s single-mode optical port (10 km) 10GBase-T: 10,000 Mbit/s copper Ethernet port 10GBase-LR: 10,000 Mbit/s single-mode optical port (10 km) |
| RedundantPhysicalC onnectionId | String | No | pc-bp10zsv5ntp**** | The ID of the redundant Express Connect circuit. The redundant Express Connect circuit must be in the Allocated, Confirmed, or Enabled state. |
| AutoPay | Boolean | No | true | Specifies whether to enable automatic payment. Valid values: true: yes false (default): no |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | String | 202844382740728 | The ID of the order. |
| PhysicalConnectio nId | String | pc- 2zegmc02v7ss4****** | The ID of the Express Connect circuit. |
| RequestId | String | F7A6301A-64BA-41EC- 8284-8F4838C15D1F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreatePhysicalConnectionSetupOrder &AccessPointId=ap-cn-beijing-ft-A &LineOperator=CT &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreatePhysicalConnectionSetupOrderResponse>
  <RequestId>F7A6301A-64BA-41EC-8284-8F4838C15D1F</RequestId>
  <PhysicalConnectionId>pc-2zegmc02v7ss4******</PhysicalConnectionId>
  <OrderId>202844382740728</OrderId>
</CreatePhysicalConnectionSetupOrderResponse>
```

`JSON` format `{`

```json
    "RequestId": "F7A6301A-64BA-41EC-8284-8F4838C15D1F",
    "PhysicalConnectionId": "pc-2zegmc02v7ss4******",
    "OrderId": 202844382740728
```

#### 6.5.12 CompletePhysicalConnectionLOA

Generates a report for an installed Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CompletePhysicalCo nnectionLOA | The operation that you want to perform. Set the value to CompletePhysicalConnectionLOA. |
| InstanceId | String | Yes | pc- bp10tvlhnwkw**** | The ID of the Express Connect circuit. |
| LineCode | String | Yes | aaa111 | The circuit code provided by the connectivity provider. |
| LineLabel | String | Yes | bbb222 | The label of the cable in the data center. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8983C74-E068-4509- B442-89BD82C8F43B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CompletePhysicalConnectionLOA &InstanceId=pc-bp10tvlhnwkw**** &LineCode=aaa111 &LineLabel=bbb222 &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CompletePhysicalConnectionLOAResponse>
  <RequestId>F8983C74-E068-4509-B442-89BD82C8F43B</RequestId>
</CompletePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "RequestId": "F8983C74-E068-4509-B442-89BD82C8F43B"
```

#### 6.5.13 DescribePhysicalConnectionLOA

Queries letter of authorization (LOA) information about an Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePhysicalCon nectionLOA | The operation that you want to perform. Set the value to DescribePhysicalConnectionLOA. |

| InstanceId | String | Yes | pc- bp1ca4wca27ex***** * | The ID of the Express Connect circuit. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 318BB676-0A2B- 43A0-9AD8- F1D34E93750F | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PhysicalConnectio nLOAType | Struct |   | The LOA information about the Express Connect circuit. |
| CompanyLocalized Name | String | company | The name of the construction company. |
| CompanyName | String | AppCompany**** | The name of the organization that requires the Express Connect circuit. |
| ConstructionTime | String | 2019-02-26T08:00:00Z | The time when construction starts. |
| InstanceId | String | pc-bp1ca4wca27****** | The ID of the Express Connect circuit. |
| LineCode | String | lincode**** | The circuit code provided by the Internet service provider (ISP). |
| LineLabel | String | linetest**** | The label of the cable in the data center. |
| LineType | String | MSTP | The type of the Express Connect circuit. Valid values: MSTP Other SDH MPLSVPN FIBRE |
| LoaUrl | String | http://****** | The download URL of the LOA file. |
| PMInfo | Array of PMInfo |   | The information about the construction workers. |
| PMInfo |   |   |   |
| PMCertificateNo | String | engineer**** | The identity document number of the construction worker. |

| PMCertificateType | String | Other | The type of the identity document. Valid values: IDCard: identity card Other: other identity documents Passport: passport |
|---|---|---|---|
| PMContactInfo | String | 18910010****** | The phone number of the construction worker. |
| PMGender | String | Male | The gender of the construction worker. |
| PMName | String | name | The name of the construction worker. |
| SI | String | ctcu | The on-site construction company. |
| Status | String | Enabled | The status of the Express Connect circuit. Valid values: Initial: pending approval Approved: approved Allocating: allocating resources Allocated: under construction Confirmed: waiting for user confirmation Enabled: enabled Rejected: rejected Canceled: canceled Allocation Failed: resource allocation failed Terminated: disabled |
| RequestId | String | 318BB676-0A2B-43A0- 9AD8-F1D34E93750F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePhysicalConnectionLOA &InstanceId=pc-bp1ca4wca27ex****** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePhysicalConnectionLOAResponse>
   <code>200</code>
   <data>
      <companyName>test1234</companyName>
      <constructionTime>2019-02-26T08:00:00Z</constructionTime>
      <instanceId>pc-bp1ca4wca27ert****</instanceId>
      <lineType>MSTP</lineType>
      <loaUrl>http://********</loaUrl>
      <pmInfo>
         <nextPMIndex>1</nextPMIndex>
         <pmCertificateNo>12345**</pmCertificateNo>
         <pmCertificateType>Other</pmCertificateType>
         <pmContactInfo>189100100**0</pmContactInfo>
         <pmGender>Male</pmGender>
         <pmName>test</pmName>
      </pmInfo>
      <si>ctcu</si>
      <status>Available</status>
   </data>
   <message>successful</message>
   <requestId>318BB676-0A2B-43A0-9AD8-F1D34E93750F</requestId>
   <success>true</success>
    </DescribePhysicalConnectionLOAResponse>
```

`JSON` format `{`

```json
    "code": "200",
    "data": {
        "companyName": "test1234",
        "constructionTime": "2019-02-26T08:00:00Z",
        "instanceId": "pc-bp1ca4wca27erts****",
        "lineType": "MSTP",
        "loaUrl":"http://*******",
        "pmInfo": [
```

`{`

```json
                "nextPMIndex": 1,
                "pmCertificateNo": "1234567",
                "pmCertificateType": "Other",
                "pmContactInfo": "18910010***",
                "pmGender": "Male",
                "pmName": "test"
```

`],`

```json
        "si": "ctcu",
        "status": "Available"
```

`},`

```json
    "message": "successful",
    "requestId": "318BB676-0A2B-43A0-9AD8-F1D34E93750F",
    "success": true
```

### 6.6 VBR

#### 6.6.1 CreateVbrHa

Creates a virtual border router (VBR) failover group.

**Request headers**

This operation uses only common request headers. For more information, see Common request parameters.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| Description | String | Query | No | This is my vswitch. | Description of the vSwitch. The description must be 2 to 256 characters in length, start with a letter or a Chinese character, and not start with http:// or https:// . |
| Name | String | Query | No | test123 | The name of the VBR failover group. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and can contain digits, underscores ( ), and _ hyphens (-). The name cannot start with http:// or https:// . |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. Generate a client token to ensure that it is unique among different requests. If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request. |
| DryRun | Boolea n | Query | No | true | Specifies whether request detection is enabled. Valid values: true : Sends a check request. false (default): Sends a normal request. |
| VbrId | String | Query | Yes | vbr-bp1lhl0taikrte**** | The VBR instance ID. |
| PeerVbrId | String | Query | Yes | vbr-bp12mw1f8k3jgygk9**** | The ID of the other VBR in the VBR failover group. |
| RegionId | String | Query | Yes | cn-qingdao-env66-d01 | The ID of the region where the IPsec-VPN connection is located. You can call the DescribeRegions operation to query the most recent region list. |
| OwnerId | Long | Query | No | 1234567890 | This is a system parameter for authentication. Do not set this parameter. |
| ResourceOwn erAccount | String | Query | No | test | This is a system parameter for authentication. Do not set this parameter. |

| Developer Gu | ide·API R | eference |   |   | Express Connec |
|---|---|---|---|---|---|
| Parameter | Type | Position | Required | Example | Description |
| ResourceOwn erId | Long | Query | No | 345678912345 | This is a system parameter for authentication. Do not set this parameter. |
| OwnerAccoun t | String | Query | No | test | This is a system parameter for authentication. Do not set this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrHaId | String | vbrha- sa1sxheuxtd98**** | The instance ID of the VBR failover group. |
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The request ID. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=CreateVbrHa &VbrId=vbr-bp1lhl0taikrte**** &PeerVbrId=vbr-bp12mw1f8k3jgygk9**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "VbrHaId":"vbrha-sa1sxheuxtd98****",
 "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE"
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationFailed.VbrCen NotConsistent | OperationFailed.VbrCenNotConsistent | The VBR and the peer VBR are attached to different Cloud Enterprise Network (CEN) instances. |
| 400 | OperationFailed.VbrAliUi dNotConsistent | OperationFailed.VbrAliUidNotConsisten t | The VBR and the peer VBR belong to different Alibaba Cloud accounts. |
| 400 | OperationFailed.VbrAcce ssDeviceSame | OperationFailed.VbrAccessDeviceSam e | The VBR and the peer VBR are connected to the same access point. |
| 400 | OperationFailed.VbrBan dWidthExceed | OperationFailed.VbrBandWidthExceed | The bandwidth of the VBR exceeds the limit. |
| 400 | OperationFailed.VbrInUs edByOtherHa | OperationFailed.VbrInUsedByOtherHa | The VBR is already part of another VBR high availability (HA) configuration. |

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | OperationFailed.VbrBgp PeerNotEnableBfd | OperationFailed.VbrBgpPeerNotEnable Bfd | Bidirectional Forwarding Detection (BFD) is not enabled for the Border Gateway Protocol (BGP) peer of the VBR. |
| 400 | OperationFailed.VbrCen NotRelation | OperationFailed.VbrCenNotRelation | The VBR is not attached to a Cloud Enterprise Network (CEN) instance. |
| 404 | ResourceNotFound.Vbr | ResourceNotFound.Vbr | The specified VBR does not exist. |

#### 6.6.2 DeleteVbrHa

Deletes a Virtual Border Router (VBR) failover group.

**Request headers**

This operation uses only common request headers. For more information about common request parameters, see Common request parameters.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44- 0016e04115b | A client token to ensure the idempotence of the request. Generate this value on your client. Make sure the value is unique for different requests. If you do not specify this parameter, the system uses the request ID as the client token. The request ID can be different for each request. |
| InstanceId | String | Query | Yes | pc-bp1qrb3044eqi**** | The resource instance ID. |
| RegionId | String | Query | Yes | cn-qingdao-env66-d01 | The ID of the region where the IPsec-VPN connection is created. Call the DescribeRegions operation to obtain the region ID. |
| OwnerId | Long | Query | No | 1234567890 | A system parameter for authentication. Do not specify this parameter. |
| ResourceOwn erAccount | String | Query | No | test | A system parameter for authentication. Do not specify this parameter. |
| ResourceOwn erId | Long | Query | No | 345678912345 | A system parameter for authentication. Do not specify this parameter. |
| OwnerAccoun t | String | Query | No | test | A system parameter for authentication. Do not specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The request ID. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DeleteVbrHa &InstanceId=pc-bp1qrb3044eqi**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE"
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | ResourceNotFound.VbrH a | ResourceNotFound.VbrHa | The specified VBR failover group is not found. |

#### 6.6.3 DeleteNqa

Deletes a specified Network Quality Analyzer (NQA) instance.

**Request headers**

This operation uses only common request headers. For more information, see Common parameters.

**Request parameters**

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| Action | String | Query | No | DeleteNqa | A required system parameter. Set the value to DeleteNqa. |
| OwnerId | Long | Query | No | 1234567890 | A system parameter for authentication. Do not set this parameter. |
| ResourceOwn erAccount | String | Query | No | test | A system parameter for authentication. Do not set this parameter. |
| ResourceOwn erId | Long | Query | No | 345678912345 | A system parameter for authentication. Do not set this parameter. |

| Parameter | Type | Position | Required | Example | Description |
|---|---|---|---|---|---|
| RegionId | String | Query | Yes | cn-qingdao-env66-d01 | The ID of the region where the IPsec-VPN connection is deployed. Call the DescribeRegions operation to obtain the region ID. |
| NqaId | String | Query | Yes | nqa-xxxxxxxxxxx | The ID of the NQA instance. |
| ClientToken | String | Query | No | 02fb3da4-130e-11e9-8e44- 0016e04115b | A client-generated token that is used to ensure the idempotence of the request. Make sure that the token is unique for each request. If you do not specify this parameter, the system uses the RequestId as the ClientToken. The RequestId may be different for each request. |
| OwnerAccoun t | String | Query | No | test | A system parameter for authentication. Do not set this parameter. |

**Response data**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BE01CD7-5A50-472D- AC14-CA181C5C03BE | The request ID. |

**Examples**

Sample request

```
http(s)://[Endpoint]/?Action=DeleteNqa &RegionId=cn-qingdao-env66-d01 &NqaId=nqa-xxxxxxxxxxx &<Common request parameters>
```

Sample response `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"5BE01CD7-5A50-472D-AC14-CA181C5C03BE"
```

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 404 | REGION NOT FOUND _ _ | InvalidRegionId.NotFound | The specified value of "regionId" is not supported. |

| Developer Gu | ide·API Reference |   | Express Connec |
|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | BGP PEER COUNT PER _ _ _ _ VBR QUOTA EXCEED _ _ | QuotaExceeded.Bgp | The number of Border Gateway Protocol (BGP) peers for the VBR has reached the quota. |
| 400 | NQA COUNT PER VBR _ _ _ _ QUOTA EXCEED _ | QuotaExceeded.Nqa | The number of NQA instances for the VBR has reached the quota. |
| 400 | BGP NETWORK COUNT _ _ _ PER VBR QUOTA EXCEE _ _ _ D | QuotaExceeded.BgpNetwork | The number of BGP networks for the VBR has reached the quota. |
| 400 | MULTI PCONN PEER IP _ _ _ _ ADDRESS CANNOT BE _ _ _ NULL | InvalidPeerIpAddress | The peer IP address cannot be null for a connection with multiple physical connections. |
| 400 | VBR NETWORK NOT EXI _ _ _ STS | InvalidVbrNetwork | The specified VBR network does not exist. |
| 400 | BGP GROUP NOT EXIST _ _ _ S | InvalidBgpGroup | The specified BGP group does not exist. |
| 400 | NAME ILLEGAL _ | InvalidBgpName.Malformed | The specified BGP Group name is not valid. |
| 400 | DESCRIPTION ILLEGAL _ | InvalidBgpDiscription.Malformed | The specified BGP Group description is not valid. |
| 400 | AUTH KEY ILLEGAL _ _ | InvalidBgpAuthkey.Malformed | The specified BGP Group authentication key is not valid. |
| 404 | REGION NOT FOUND _ _ | InvalidRegionId.NotFound | The specified RegionId is not found. |
| 400 | IP MALFORMED _ | InvalidIP.Malformed | The specified IP address is malformed. |
| 400 | PEER ASN CANNOT EQ _ _ _ UALS ALIYUN PUBLIC A _ _ _ SN | InvalidPeerAsn.Malformed | The peer ASN cannot be the same as the Alibaba Cloud ASN (45104). |
| 400 | PARAMETER MUST NOT _ _ NULL _ | InvalidParams.NotNull | The peer ASN cannot be the Alibaba Cloud ASN (45104). |
| 400 | INSTANCE NOT EXISTS _ _ | InvalidParams.NotFound | The specified instance does not exist. |
| 400 | VPC NOT EXIST _ _ | InvalidParams.NotFound | The specified VPC instance does not exist. |
| 400 | BGP NETWORK CIDR EX _ _ _ ISTS | InvalidParams.AlreadyExists | The specified BGP network already exists. |
| 400 | NOT STABLE STATUS C _ _ _ AN NOT OPERATION _ _ | InvalidStatus.CannotOperate | The operation cannot be performed due to an invalid status. |
| 400 | ERROR VBR HAS 0 OR _ _ _ _ _ MORE THAN 1 SUBIF _ _ _ | InvalidParams.PeerIpAddressMustPoint Out | You must specify the peer IP address because the VBR has zero or more than one subinterface. |
| 400 | BGP PEER IP ADDRESS _ _ _ _ ALREADY USED CANNO _ _ T CREATE BGP PEER _ _ _ | InvalidParams.PeerIpAddressInUse | A BGP peer cannot be created because the specified peer IP address is already in use. |
| 404 | REGION NOT FOUND _ _ | InvalidRegionId.NotFound | The specified RegionId does not exist in our records. |

#### 6.6.4 CreateVirtualBorderRouter

Creates a virtual border router (VBR).

**Usage notes**

After you create a VBR for the current organization, the VBR is in the **Active** state. After you create a VBR for another organization, the VBR is in the **Unconfirmed** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateVirtualBorderR outer | The operation that you want to perform. Set the value to CreateVirtualBorderRouter. |
| PhysicalConnectionId | String | Yes | pc-2zextbehcx**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| VlanId | Integer | Yes | 0 | The VLAN ID of the VBR. Valid values:0 to 2999. Note Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same the Express Connect circuit must be different. |
| VbrOwnerId | Long | No | 2534607317069112 58 | The ID of the Apsara Stack tenant account to which the VBR belongs. The default ID is the ID of the current Apsara Stack tenant account or the owner account of the Express Connect circuit. |
| CircuitCode | String | No | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. Note Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR. |
| PeerGatewayIp | String | No | 192.168.XX.XX | The IP address of the gateway device in the data center. Only the owner of the VBR can set or modify this parameter. This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another organization. |
| PeeringSubnetMask | String | No | 255.255.255.252 | The subnet mask of the IP addresses of the VBR and the gateway device in the data center. The two IP addresses must fall within the same subnet. |

| Description | String | No | Description | The description of the VBR. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
|---|---|---|---|---|
| Name | String | No | test | The name of the VBR. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:1 a2b | The IPv6 address of the VBR. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:2 a2b | The IPv6 address of the gateway device in the data center. Only the owner of the VBR can set or modify this parameter. This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another organization. |
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400::/5 6 | The subnet mask of the IPv6 addresses of the VBR and the gateway device in the data center. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable IPv6. Valid values: true: yes false (default): no |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VbrId | String | vbr- bp1jcg5cmxjbl9xgc**** | The ID of the VBR. |
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateVirtualBorderRouter &PhysicalConnectionId=pc-2zextbehcx**** &RegionId=cn-qingdao-env66-d01 &VlanId=0 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
      <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
      <VbrId>vbr-bp1jcg5cmxjbl9xgc****</VbrId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "VbrId": "vbr-bp1jcg5cmxjbl9xgc****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId is not found. | The error message returned because the specified Express Connect circuit ID does not exist. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | The error message returned because the PhysicalConnectionId parameter is not specified. |
| 400 | InvalidPhysicalConnectio nId.NotEnabled | The specified PhysicalConnectionId is not in Enabled state. | The error message returned because the Express Connect circuit is in an invalid state. Check the Express Connect circuit and try again. |
| 404 | InvalidVbrOwnerId.NotF ound | The specified VbrOwnerId is not valid. | The error message returned because VbrOwnerId is set to an invalid value. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because the value of VlanId is invalid. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because LocalGatewayIp is not set. |
| 400 | InvalidLocalGatewayIp.M alformed | The specified LocalGatewayIp is not valid. | The error message returned because the IP address of the VBR is invalid. |
| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because PeerGatewayIp is not set. |

| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | The error message returned because PeeringSubnetMask is not set. |
|---|---|---|---|
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.LocalGateway IpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGatewayI pNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubne tMaskNotAllowedByCalle r | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.NameNotAllo wedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionNo tAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfor med | The specifid ?Description? is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | QuotaExceeded.vbrPerp Conn | Virtual boarder router per PhysicalConnection quota exceed. | The error message returned because the number of VBRs of each Express Connect circuit has reached the upper limit. Reduce the number of VBRs and try again. |
| 400 | QuotaExceeded.freevbr | Free virtual boarder router quota exceed. | The error message returned because the number of VBRs has reached the upper limit. |
| 400 | InvalidIp.NotSameSubne t | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |
| 404 | CROSS BID.FORBIDDEN _ | Create VBR across bid is illegal | The error message returned because you are not allowed to create a VBR for another Apsara Stack tenant account. |

#### 6.6.5 DeleteVirtualBorderRouter

Deletes a virtual border router (VBR).

**Usage notes**

When you call this operation, take note of the following limits: Before you delete a VBR, you must delete all router interfaces of the VBR. You can delete only a VBR that is in the **Unconfirmed**, **Enabled**, or **Terminated** state. If the owner of an Express Connect circuit wants to delete a VBR that belongs to another Apsara Stack tenant account, the VBR must be in the **Unconfirmed** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteVirtualBorderR outer | The operation that you want to perform. Set the value to DeleteVirtualBorderRouter. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp12mw1f8k3jgygk9 **** | The ID of the VBR. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F8BF7D24-F3EB-4E23- 9208-B77C6EB78E75 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp12mw1f8k3jgygk9**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteVirtualBorderRouterResponse>
  <RequestId>F8BF7D24-F3EB-4E23-9208-B77C6EB78E75</RequestId>
</DeleteVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "F8BF7D24-F3EB-4E23-9208-B77C6EB78E75"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
|---|---|---|---|
| 400 | InvalidOperation.RouterI nterfaceNotDeleted | The specified VirutalBorderRouter still has routerInterface. | The error message returned because the VBR is associated with a router interface. |
| 400 | InvalidOperation.Operati onNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the specified VBR is in an invalid state. Check the status of the VBR. |
| 403 | Forbidden.OperationNot AllowedByUser | The caller is not allowed to delete the specified VirtualBorderRouter. | The error message returned because you are not allowed to delete the VBR. |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | The error message returned because multiple VLAN router interfaces exist. |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | The error message returned because no VLAN router interface is available. |
| 400 | InvalidStatus.NotAllowe d | The virtual border has been associated by physicalConnection. | The error message returned because the VBR is associated with an Express Connect circuit. |

#### 6.6.6 DescribeVirtualBorderRouters

Queries virtual border routers (VBRs).

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBorde rRouters | The operation that you want to perform. Set the value to DescribeVirtualBorderRouters. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBRs. You can call the DescribeRegions operation to query the most recent region list. |
| PageNumber | Integer | No | 1 | The page number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
| Filter.N.Key | String | No | Status | The key of filter condition N. Valid values of N: 1 to 5. Valid values of filter conditions: PhysicalConnectionId: Filter by Express Connect circuit ID. VbrId: Filter by VBR ID. Status: Filter by VBR status. Name: Filter by VBR name. AccessPointId: Filter by access point ID. eccId: Filter by Express Cloud Connect (ECC) instance ID. type: Filter by Express Connect circuit type. |

| Filter.N.Value.N | RepeatList | No | Active | The filter values for keys. You can specify multiple filter values for one key. The logical operator between filter values is OR. If one filter value is matched, the filter key is matched. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VirtualBorderRoute rSet | Array of VirtualBorderRoute rType |   | The information about the VBR. |
| VirtualBorderRoute rType |   |   |   |
| AccessPointId | String | ap-cn-kojok1**** | The ID of the access point that is associated with the Express Connect circuit. |
| ActivationTime | String | 2020-06-08T12:20:55 | The first time when the VBR was activated. |
| AssociatedCens | Array of AssociatedCen |   | The information about the Cloud Enterprise Network (CEN) instance. |
| AssociatedCen |   |   |   |
| CenId | String | cen-kojok19**** | The ID of the CEN instance. |
| CenOwnerId | Long | 253460731706911258 | The ID of the Apsara Stack tenant account to which the CEN instance belongs. |
| CenStatus | String | Attached | The status of the CEN instance. Valid values: |
| AssociatedPhysical Connections | Array of AssociatedPhysical Connection |   | The Express Connect circuit with which the VBR is associated. |
| AssociatedPhysical Connection |   |   |   |
| CircuitCode | String | 12 | The circuit code of the VBR interface. The circuit code is provided by the connectivity provider. |
| EnableIpv6 | Boolean | false | Indicates whether IPv6 is enabled. |
| LocalGatewayIp | String | 116.62.XX.XX | The IPv4 address of the VBR. |
| LocalIpv6GatewayI p | String | 2001:XXXX:4:4:4:4:4:4 | The IPv6 address of the VBR. |
| PeerGatewayIp | String | 116.12.XX.XX | The IPv4 address of the gateway device on the user side. |
| PeerIpv6GatewayI p | String | 2001:XXXX:3:3:4:4:4:4 | The IPv6 address of the gateway device on the user side. |
| PeeringIpv6Subnet Mask | String | 2408:4004:cc:400::/56 | The subnet mask of the IPv6 addresses configured on the user side and Apsara Stack side. |

| Developer Guide· | API Reference |   | Express Connec |
|---|---|---|---|

| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the IPv4 addresses configured on the user side and Apsara Stack side. |
|---|---|---|---|
| PhysicalConnectio nBusinessStatus | String | Normal | The business status of the Express Connect circuit. |
| PhysicalConnectio nId | String | pc-119mfjzm7**** | The ID of the Express Connect circuit. |
| PhysicalConnectio nOwnerUid | String | 283117732402483989 | The Apsara Stack tenant account of the Express Connect circuit owner. |
| PhysicalConnectio nStatus | String | Normal | The connection status of the Express Connect circuit. |
| Status | String | Enabled | The status of the Express Connect circuit. Valid values: |
| VlanId | String | 0 | The virtual LAN (VLAN) ID of the VBR. |
| VlanInterfaceId | String | ri-kojok19x3j0q6k**** | The ID of the VBR interface. |
| CircuitCode | String | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. |
| CreationTime | String | 2020-06-08T20:20:55 | The time when the VBR was created. |
| Description | String | VBR | The description of the VBR. |
| DetectMultiplier | Long | 3 | The maximum number of dropped packets that is allowed by the receiver when the initiator transmits packets. This value can be used to check whether a connection works as expected. Valid values: 3 to 10. |
| EccId | String | ecc-h**** | The ID of the ECC instance. |
| EnableIpv6 | Boolean | false | Indicates whether IPv6 is enabled. |
| LocalGatewayIp | String | 116.62.XX.XX | The IPv4 address of the VBR. |
| LocalIpv6GatewayI p | String | 2001:XXXX:4:4:4:4:4:4 | The IPv6 address of the VBR. |
| MinRxInterval | Long | 200 | The interval at which Bidirectional Forwarding Detection (BFD) packets are received. Valid values: 200 to 1000. Unit: milliseconds. |
| MinTxInterval | Long | 200 | The interval at which Bidirectional Forwarding Detection (BFD) packets are sent. Valid values: 200 to 1000. Unit: milliseconds. |

| Name | String | test | The name of the VBR. |
|---|---|---|---|
| PConnVbrExpireTi me | String | 2020-06-08T20:20:55 | The time when the VBR expires. |
| PeerGatewayIp | String | 116.12.XX.XX | The IPv4 address of the gateway device on the user side. |
| PeerIpv6GatewayI p | String | 2001:XXXX:3:3:4:4:4:4 | The IPv6 address of the gateway device on the user side. |
| PeeringIpv6Subnet Mask | String | 2000:1234:0:a000::/55 | The subnet mask of the IPv6 addresses configured on the user side and Apsara Stack side. |
| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the IPv4 addresses configured on the user side and Apsara Stack side. |
| PhysicalConnectio nBusinessStatus | String | Normal | The business status of the Express Connect circuit. |
| PhysicalConnectio nId | String | pc-119mfjzm7x**** | The ID of the Express Connect circuit to which the VBR belongs. |
| PhysicalConnectio nOwnerUid | String | 283117732402483989 | The Apsara Stack tenant account of the Express Connect circuit owner. |
| PhysicalConnectio nStatus | String | Normal | The connection status of the Express Connect circuit. |
| RecoveryTime | String | 2020-06-09T12:20:55 | The last time when the status of the VBR changed from Terminated to Active. |
| RouteTableId | String | rtb-bp1n**** | The ID of the route table of the VBR. |
| Status | String | Enabled | The status of the Express Connect circuit. Valid values: Initial: The application is under review. Approved: The application is approved. Allocating: The system is allocating resources. Allocated: The Express Connect circuit is under construction. Confirmed: The Express Connect circuit is pending user confirmation. Enabled: The Express Connect circuit is enabled. Rejected: The application is rejected. Canceled: The application is canceled. Allocation Failed: The system failed to allocate resources. Terminated: The Express Connect circuit is disabled. |
| TerminationTime | String | 2020-06-08T20:20:55 | The last time when the VBR was disabled. |
| Type | String | pconnVBR | The type of the VBR. |
| VbrId | String | vbr-kojok19xx**** | The ID of the VBR. |

| VlanId | Integer | 10 | The VLAN ID of the VBR. |
|---|---|---|---|
| VlanInterfaceId | String | ri-2zeo3xzyf38r4xx**** | The ID of the VBR interface. |
| TotalCount | Integer | 1 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. Default value: 1. |
| PageSize | Integer | 10 | The number of entries returned per page. Maximum value: 50. Default value: 10. |
| RequestId | String | DE77A7F3-3B74-41C0- A5BC-CAFD188C28B6 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVirtualBorderRouters &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVirtualBorderRoutersResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
  <VirtualBorderRouterSet>
        <MinRxInterval>200</MinRxInterval>
        <PeerGatewayIp>116.12.XX.XX</PeerGatewayIp>
        <Description>VBR</Description>
        <RouteTableId>rtb-bp1n****</RouteTableId>
        <ActivationTime>2020-06-08T12:20:55</ActivationTime>
        <PhysicalConnectionId>pc-119mfjzm7x****</PhysicalConnectionId>
        <PhysicalConnectionStatus>Normal</PhysicalConnectionStatus>
        <VlanInterfaceId>ri-2zeo3xzyf38r4xx****</VlanInterfaceId>
        <VbrId>vbr-kojok19xx****</VbrId>
        <PhysicalConnectionOwnerUid>283117732402483989</PhysicalConnectionOwnerUid>
        <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
        <TerminationTime>2020-06-08T20:20:55</TerminationTime>
        <EnableIpv6>false</EnableIpv6>
        <PeeringIpv6SubnetMask>2000:1234:0:a000::/55</PeeringIpv6SubnetMask>
        <Name>test</Name>
        <RecoveryTime>2020-06-09T12:20:55</RecoveryTime>
        <EccId>ecc-h****</EccId>
        <LocalIpv6GatewayIp>2001:XXXX:4:4:4:4:4:4</LocalIpv6GatewayIp>
        <VlanId>10</VlanId>
        <Status>Enabled</Status>
        <CircuitCode>longtel001</CircuitCode>
        <MinTxInterval>200</MinTxInterval>
        <PeerIpv6GatewayIp>2001:XXXX:3:3:4:4:4:4</PeerIpv6GatewayIp>
        <DetectMultiplier>3</DetectMultiplier>
        <Type>pconnVBR</Type>
        <LocalGatewayIp>116.62.XX.XX</LocalGatewayIp>
        <AccessPointId>ap-cn-kojok1****</AccessPointId>
        <CreationTime>2020-06-08T20:20:55</CreationTime>
        <PConnVbrExpireTime>2020-06-08T20:20:55</PConnVbrExpireTime>
        <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
        <AssociatedPhysicalConnections>
              <Status>Enabled</Status>
              <PeerGatewayIp>116.12.XX.XX</PeerGatewayIp>
              <CircuitCode>12</CircuitCode>
              <PhysicalConnectionId>pc-119mfjzm7****</PhysicalConnectionId>
              <PhysicalConnectionStatus>Normal</PhysicalConnectionStatus>
              <VlanInterfaceId>ri-kojok19x3j0q6k****</VlanInterfaceId>
              <PeerIpv6GatewayIp>2001:XXXX:3:3:4:4:4:4</PeerIpv6GatewayIp>
              <PhysicalConnectionOwnerUid>283117732402483989</PhysicalConnectionOwnerUid>
              <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
              <EnableIpv6>false</EnableIpv6>
              <PeeringIpv6SubnetMask>2408:4004:cc:400::/56</PeeringIpv6SubnetMask>
              <LocalGatewayIp>116.62.XX.XX</LocalGatewayIp>
              <LocalIpv6GatewayIp>2001:XXXX:4:4:4:4:4:4</LocalIpv6GatewayIp>
              <VlanId>0</VlanId>
              <PhysicalConnectionBusinessStatus>Normal</PhysicalConnectionBusinessStatus>
        </AssociatedPhysicalConnections>
        <AssociatedCens>
              <CenStatus>Attached</CenStatus>
              <CenOwnerId>253460731706911258</CenOwnerId>
              <CenId>cen-kojok19****</CenId>
        </AssociatedCens>
  </VirtualBorderRouterSet>
</DescribeVirtualBorderRoutersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6",
    "PageNumber": 1,
    "VirtualBorderRouterSet": {
        "MinRxInterval": 200,
        "PeerGatewayIp": "116.12.XX.XX",
        "Description": "VBR",
        "RouteTableId": "rtb-bp1n****",
        "ActivationTime": "2020-06-08T12:20:55",
        "PhysicalConnectionId": "pc-119mfjzm7x****",
        "PhysicalConnectionStatus": "Normal",
        "VlanInterfaceId": "ri-2zeo3xzyf38r4xx****",
        "VbrId": "vbr-kojok19xx****",
        "PhysicalConnectionOwnerUid": 283117732402484000,
        "PeeringSubnetMask": "255.255.255.252",
        "TerminationTime": "2020-06-08T20:20:55",
        "EnableIpv6": false,
        "PeeringIpv6SubnetMask": "2000:1234:0:a000::/55",
        "Name": "test",
        "RecoveryTime": "2020-06-09T12:20:55",
        "EccId": "ecc-h****",
        "LocalIpv6GatewayIp": "2001:XXXX:4:4:4:4:4:4",
        "VlanId": 10,
        "Status": "Enabled",
        "CircuitCode": "longtel001",
        "MinTxInterval": 200,
        "PeerIpv6GatewayIp": "2001:XXXX:3:3:4:4:4:4",
        "DetectMultiplier": 3,
        "Type": "pconnVBR",
        "LocalGatewayIp": "116.62.XX.XX",
        "AccessPointId": "ap-cn-kojok1****",
        "CreationTime": "2020-06-08T20:20:55",
        "PConnVbrExpireTime": "2020-06-08T20:20:55",
        "PhysicalConnectionBusinessStatus": "Normal",
        "AssociatedPhysicalConnections": {
            "Status": "Enabled",
            "PeerGatewayIp": "116.12.XX.XX",
            "CircuitCode": 12,
            "PhysicalConnectionId": "pc-119mfjzm7****",
            "PhysicalConnectionStatus": "Normal",
            "VlanInterfaceId": "ri-kojok19x3j0q6k****",
            "PeerIpv6GatewayIp": "2001:XXXX:3:3:4:4:4:4",
            "PhysicalConnectionOwnerUid": 283117732402484000,
            "PeeringSubnetMask": "255.255.255.252",
            "EnableIpv6": false,
            "PeeringIpv6SubnetMask": "2408:4004:cc:400::/56",
            "LocalGatewayIp": "116.62.XX.XX",
            "LocalIpv6GatewayIp": "2001:XXXX:4:4:4:4:4:4",
            "VlanId": 0,
            "PhysicalConnectionBusinessStatus": "Normal"
```

`},`

```json
        "AssociatedCens": {
            "CenStatus": "Attached",
            "CenOwnerId": 253460731706911260,
            "CenId": "cen-kojok19****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |
|---|---|---|---|

#### 6.6.7 DescribeVirtualBorderRoutersForPhysicalConnection

Queries virtual border routers (VBRs) that are associated with an Express Connect circuit. The VBRs can be created by the owner of the Express Connect circuit and by other Apsara Stack tenant accounts.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVirtualBorde rRoutersForPhysicalC onnection | The operation that you want to perform. Set the value to DescribeVirtualBorderRoutersForPhysica lConnection. |
| PhysicalConnectionId | String | Yes | pc-119mfj**** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the Express Connect circuit is deployed. You can call the DescribeRegions operation to query the most recent region list. |
| Filter.N.Key | String | No | 1 | The key of the filter condition. Valid values of N: 1 to 5. Valid values of filter conditions: PhysicalConnectionId: Filter by Express Connect circuit ID. VbrId: Filter by VBR ID. Status: Filter by VBR status. Name: Filter by VBR name. AccessPointId: Filter by access point ID. eccId: Filter by Express Cloud Connect (ECC) instance ID. type: Filter by VBR type. |
| Filter.N.Value.N | RepeatList | No | 1 | The value of the filter condition. Valid values of N: 1 to 5. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| VirtualBorderRoute rForPhysicalConne ctionSet | Array of VirtualBorderRoute rForPhysicalConne ctionType |   | The details of the VBR. |
| VirtualBorderRoute rForPhysicalConne ctionType |   |   |   |

| ActivationTime | String | 2021-06-08T12:20:55 | The first time when the VBR was activated. |
|---|---|---|---|
| Bandwidth | String | 10 | The bandwidth of the VBR associated with the Express Connect circuit. Unit: Mbit/s. |
| CircuitCode | String | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. |
| CreationTime | String | 2021-06-08T12:20:55 | The time when the VBR was created. |
| EccId | String | ecc-sjghe**** | The ID of the ECC instance. |
| EnableIpv6 | Boolean | false | Indicates whether IPv6 is enabled. Valid values: false: no true: yes |
| LocalGatewayIp | String | 10.0.XX.XX | The IPv4 address of the VBR. |
| LocalIpv6GatewayI p | String | 2001:XXXX:3c4d:0015:0 000:0000:0000:1a2b | The IPv6 address of the VBR. |
| PConnVbrBussines sStatus | String | Available | The status of the VBR. |
| PConnVbrChargeT ype | String | PrePaid | The billing method of the VBR. Valid values: PrePaid: subscription If you select subscription, make sure that your Apsara Stack tenant account supports balance payments or credit payments. PostPaid: pay-as-you-go |
| PConnVbrExpireTi me | String | 2021-06-22T12:20:55 | The time when the VBR expires. |
| PeerGatewayIp | String | 10.0.XX.XX | The IPv4 address of the gateway device on the user side. |
| PeerIpv6GatewayI p | String | 2001:XXXX:3c4d:0015:0 000:0000:0000:2a2b | The IPv6 address of the gateway device on the user side. |
| PeeringIpv6Subnet Mask | String | 2000:1234:0:a000::/55 | The subnet mask of the IPv6 addresses configured on the user side and Apsara Stack side. |
| PeeringSubnetMas k | String | 255.255.255.252 | The subnet mask of the IPv4 addresses configured on the user side and Apsara Stack side. |
| RecoveryTime | String | 2021-06-08T12:20:55 | The last time when the status of the VBR changed from Terminated to Active. |
| Status | String | Available | The status of the VBR. |
| TerminationTime | String | 2021-06-08T20:20:55 | The last time when the VBR was disabled. |
| Type | String | pconnVBR | The type of the VBR. |

| VbrId | String | vbr- bp16ksp61j7e0tk**** | The ID of the VBR. |
|---|---|---|---|
| VbrOwnerUid | Long | 253460731706911258 | The Apsara Stack tenant account ID of the VBR owner. If the VBR and Express Connect circuit belong to the same Apsara Stack tenant account, this value is empty. |
| VlanId | Integer | 1678 | The virtual LAN (VLAN) ID of the VBR. |
| TotalCount | Integer | 2 | The number of entries returned. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 7C5AE8B3-A2D8-428D- A2FF-93A225C0821E | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVirtualBorderRoutersForPhysicalConnection &PhysicalConnectionId=pc-119mfj**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeVirtualBorderRoutersResponse>
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>7C5AE8B3-A2D8-428D-A2FF-93A225C0821E</RequestId>
  <PageNumber>1</PageNumber>
  <VirtualBorderRouterForPhysicalConnectionSet>
        <Status>Available</Status>
        <PeerGatewayIp>10.0.XX.XX</PeerGatewayIp>
        <ActivationTime>2021-06-08T12:20:55</ActivationTime>
        <VbrOwnerUid>253460731706911260</VbrOwnerUid>
        <CircuitCode>longtel001</CircuitCode>
        <PeerIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:2a2b</PeerIpv6GatewayIp>
        <VbrId>vbr-bp16ksp61j7e0tk****</VbrId>
        <PConnVbrChargeType>PrePaid</PConnVbrChargeType>
        <PeeringSubnetMask>255.255.255.252</PeeringSubnetMask>
        <TerminationTime>2021-06-08T20:20:55</TerminationTime>
        <EnableIpv6>false</EnableIpv6>
        <PeeringIpv6SubnetMask>2000:1234:0:a000::/55</PeeringIpv6SubnetMask>
        <RecoveryTime>2021-06-08T12:20:55</RecoveryTime>
        <LocalGatewayIp>10.0.XX.XX</LocalGatewayIp>
        <Type>pconnVBR</Type>
        <Bandwidth>10</Bandwidth>
        <CreationTime>2021-06-08T12:20:55</CreationTime>
        <EccId>ecc-sjghe****</EccId>
        <PConnVbrExpireTime>2021-06-22T12:20:55</PConnVbrExpireTime>
        <LocalIpv6GatewayIp>2001:XXXX:3c4d:0015:0000:0000:0000:1a2b</LocalIpv6GatewayIp>
        <VlanId>1678</VlanId>
        <PConnVbrBussinessStatus>Available</PConnVbrBussinessStatus>
  </VirtualBorderRouterForPhysicalConnectionSet>
</DescribeVirtualBorderRoutersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "7C5AE8B3-A2D8-428D-A2FF-93A225C0821E",
    "PageNumber": 1,
    "VirtualBorderRouterForPhysicalConnectionSet": {
        "Status": "Available",
        "PeerGatewayIp": "10.0.XX.XX",
        "ActivationTime": "2021-06-08T12:20:55",
        "VbrOwnerUid": 253460731706911260,
        "CircuitCode": "longtel001",
        "PeerIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:2a2b",
        "VbrId": "vbr-bp16ksp61j7e0tk****",
        "PConnVbrChargeType": "PrePaid",
        "PeeringSubnetMask": "255.255.255.252",
        "TerminationTime": "2021-06-08T20:20:55",
        "EnableIpv6": false,
        "PeeringIpv6SubnetMask": "2000:1234:0:a000::/55",
        "RecoveryTime": "2021-06-08T12:20:55",
        "LocalGatewayIp": "10.0.XX.XX",
        "Type": "pconnVBR",
        "Bandwidth": 10,
        "CreationTime": "2021-06-08T12:20:55",
        "EccId": "ecc-sjghe****",
        "PConnVbrExpireTime": "2021-06-22T12:20:55",
        "LocalIpv6GatewayIp": "2001:XXXX:3c4d:0015:0000:0000:0000:1a2b",
        "VlanId": 1678,
        "PConnVbrBussinessStatus": "Available"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId does not belong to user. | The error message returned because the specified Express Connect circuit does not belong to your Apsara Stack tenant account. |

#### 6.6.8 TerminateVirtualBorderRouter

Terminates a virtual border router (VBR). After the operation is called, the VBR changes from the **Enabled** state to the **Terminating** state. After the VBR is terminated, it enters the **Terminated** state.

> **Note:** Only the owner of an Express Connect circuit can call this operation.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | TerminateVirtualBor derRouter | The operation that you want to perform. Set the value to TerminateVirtualBorderRouter. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| VbrId | String | Yes | vbr- bp15zckdt37pq72*** * | The ID of the VBR. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=TerminateVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp15zckdt37pq72**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TerminateVirtualBorderRouterResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</TerminateVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidOperation.Operati onNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the specified VBR is in an invalid state. Check the status of the VBR. |

| 403 | Forbidden.OperationTer minateNotAllowedByUse r | The caller is not allowed to terminate the specified VirtualBorderRouter. | The error message returned because you do not have the permissions to terminate the VBR. |
|---|---|---|---|

#### 6.6.9 RecoverVirtualBorderRouter

Recovers a terminated virtual border router (VBR).

**Usage notes**

After the operation is called, the VBR changes from the **Terminated** state to the **Recovering** state. When the VBR recovers, it enters the **Enabled** state. When you call this operation, take note of the following items: Only the owner of an Express Connect circuit can call this operation. The Express Connect circuit to which the VBR belongs must be in the **Enabled** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | RecoverVirtualBorder Router | The operation that you want to perform. Set the value to RecoverVirtualBorderRouter. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp1lhl0taikrte**** | The ID of the VBR. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RecoverVirtualBorderRouter &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp1lhl0taikrte**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RecoverVirtualBorderRouterResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</RecoverVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidOperation.Operati onNotAllowedInState | The specified VirutalBorderRouter is in invalid state | The error message returned because the status of the VBR interface is invalid. |
| 400 | OperationFailed.VlanIdAl readyInUse | The specifed vlanId has been used. | The error message returned because the VLAN ID is being used. |
| 403 | Forbidden.OperationRec overNotAllowedByUser | The caller is not allowed to recover the specified VirtualBorderRouter. | The error message returned because you do not have the permissions to recover the VBR. |

#### 6.6.10 ModifyVirtualBorderRouterAttribute

Modifies the configuration of a virtual border router (VBR).

**Descriptions**

Only the owner of an Express Connect circuit can modify the **VlanId** parameter. One VLAN ID of an Express Connect circuit cannot be used by two VBRs at the same time. The VLAN ID of a VBR in the **Terminated** state is reserved for seven days and cannot be used by other VBRs. The VLAN ID can be used by other VBRs after 7 days. You cannot set **LocalGatewayIp**, **PeerGatewayIp**, or **PeeringSubnetMask** for VBRs that do not belong to your Apsara Stack tenant account. Set **PeeringSubnetMask** to a subnet mask with 24 to 30 bits in length (255.255.255.0～255.255.255.252). Set **LocalGatewayIp** and **PeerGatewayIp** to IP addresses that belong to the same CIDR block. For example, you can set LocalGatewayIp to 192.168.XX.XX, PeerGatewayIp to 192.168.XX.XX, and PeeringSubnetMask to 255.255.255.248.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyVirtualBorderR outerAttribute | The operation that you want to perform. Set the value to ModifyVirtualBorderRouterAttribute. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the VBR. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- 2zehfr9ovv4b**** | The ID of the VBR. |

| VlanId | Integer | No | 0 | The VLAN ID of the VBR. Valid values:0 to 2999. Note Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same Express Connect circuit must be different. |
|---|---|---|---|---|
| CircuitCode | String | No | longtel001 | The circuit code provided by the Internet service provider (ISP) for the Express Connect circuit. Note Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 192.168.XX.XX | The IP address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |
| PeeringSubnetMask | String | No | 255.255.255.252 | The subnet mask for the IP addresses of the VBR on the Apsara Stack side and on the user side. The two IP addresses must belong to the same subnet. |
| MinTxInterval | Long | No | 300 | The time interval to send BFD packets. Valid values: 200 to 1000. Unit: milliseconds. |
| MinRxInterval | Long | No | 300 | The time interval to receive BFD packets. Valid values: 200 to 1000. Unit: milliseconds. |
| DetectMultiplier | Long | No | 3 | The maximum number of dropped packets that is allowed by the receiver when the initiator transmits packets. This value can be used to check whether a connection works as expected. Valid values: 3 to 10. |
| Description | String | No | desc | The description of the VBR. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | VBR | The name of the VBR. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. It cannot start with http:// or https:// . |

| AssociatedPhysicalCo nnections | String | No | pc-kojok19****** | The ID of the Express Connect circuit. |
|---|---|---|---|---|
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 00xxxxxxxx | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:1 a2b | The IPv6 address of the VBR on the Apsara Stack side. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:1 a2b | The IPv6 address of the VBR on the user side. Only the owner of the VBR can set this parameter. This parameter is required when you create a VBR for the owner of the Express Connect. You can ignore this parameter when you create a VBR for another Apsara Stack tenant account. |
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400::/5 6 | The subnet mask for the IPv6 addresses of the VBR on the Apsara Stack side and on the user side. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | Boolean | No | false | Specifies whether to enable IPv6. Valid values: true: yes false (default): no |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyVirtualBorderRouterAttribute &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-2zehfr9ovv4b**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyVirtualBorderRouterAttributeResponse>
      <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</ModifyVirtualBorderRouterAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidVbrId.NotFound | The specified VirutalBorderRouter is not found. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because VlanId is set to an invalid value. |
| 400 | InvalidIp.Malformed | The specified ip address is not valid. | The error message returned because the specified private IP address is invalid. Check the private IP address. |
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.CircuitCodeN otAllowedByCaller | The caller is not allowed to modify. | The error message returned because you are not allowed to modify CircuitCode. |
| 403 | Forbidden.CircuitCodeN otAllowedByCaller | The caller is not allowed to specify the CircuitCode parameter. | The error message returned because you are not allowed to set CircuitCode. |
| 403 | Forbidden.LocalGateway IpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGatewayI pNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubne tMaskNotAllowedByCalle r | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.VlanIdNotAllo wedByCaller | The caller is not allowed to specify the VlanId. | The error message returned because you are not allowed to specify the VLAN ID. |
| 403 | Forbidden.NameNotAllo wedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionNo tAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidIp.NotSameSubne t | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |

#### 6.6.11 AssociatePhysicalConnectionToVirtualBorderRouter

Associates a virtual border router (VBR) with an Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssociatePhysicalCo nnectionToVirtualBor derRouter | The operation that you want to perform. Set the value to AssociatePhysicalConnectionToVirtualBo rderRouter. |
| PhysicalConnectionId | String | Yes | pc- bp1qrb3044eqixog** ** | The ID of the Express Connect circuit. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp186tnz6rijyhj**** | The ID of the VBR. |
| VlanId | String | Yes | 123 | The VLAN ID of the VBR. Valid values: 1 to 2999. Note Only the owner of the Express Connect circuit can set this parameter. The VLAN IDs of two VBRs of the same the Express Connect circuit must be different. |
| CircuitCode | String | No | longtel001 | The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider. Note Only the owner of the Express Connect circuit can set this parameter. |
| LocalGatewayIp | String | No | 10.10.XX.XX | The IP address of the VBR on the Apsara Stack side. |
| PeerGatewayIp | String | No | 10.10.XX.XX | The IP address of the peer router interface of the VBR. Only the owner of the VBR can set or modify the value. If the VBR is in the Enabled state, you cannot leave this parameter empty. |
| PeeringSubnetMask | String | No | 255.255.255.0 | The subnet mask for the IP addresses of the VBR on the Apsara Stack side and on the user side. The two IP addresses must fall within the same subnet. |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
|---|---|---|---|---|
| LocalIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:1 a2b | The IPv6 address of the gateway device on the Apsara Stack side. |
| PeerIpv6GatewayIp | String | No | 2001:XXXX:3c4d:001 5:0000:0000:0000:2 a2b | The IPv6 address of the gateway device in the data center. |
| PeeringIpv6SubnetM ask | String | No | 2408:4004:cc:400::/5 6 | The subnet mask for the IPv6 addresses of the gateway devices in the data center and the VBRs. The two IPv6 addresses must fall within the same subnet. |
| EnableIpv6 | String | No | true | Specifies whether to enable IPv6. Valid values: true: yes false: no |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AssociatePhysicalConnectionToVirtualBorderRouter &PhysicalConnectionId= pc-bp1qrb3044eqixog**** &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp186tnz6rijyhj**** &VlanId=123 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AssociatePhysicalConnectionToVirtualBorderRouterResponse>
  <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</AssociatePhysicalConnectionToVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidInstanceId.NotFou nd | The specified Instance does not exist in the specified region. | The error message returned because the instance does not exist in the specified region. |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 400 | InvalidOperation.RouterI nterfaceNotDeleted | The specified VirutalBorderRouter still has routerInterface. | The error message returned because the VBR is associated with a router interface. |
| 400 | InvalidOperation.Operati onNotAllowedInState | The specified VirutalBorderRouter is in invalid state. | The error message returned because the specified VBR is in an invalid state. Check the status of the VBR. |
| 403 | Forbidden.OperationNot AllowedByUser | The caller is not allowed to delete the specified VirtualBorderRouter. | The error message returned because you are not allowed to delete the VBR. |
| 403 | Forbidden.MultiVlanRi | Multiple vlan router interfaces are found. | The error message returned because multiple VLAN router interfaces exist. |
| 403 | Forbidden.NoRiFound | No vlan router interfaces are found. | The error message returned because no VLAN router interface is available. |
| 400 | InvalidStatus.NotAllowe d | Invalid virtual border router status. | The error message returned because the status of the VBR does not support this operation. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidPhysicalConnectio nId.NotFound | The specified PhysicalConnectionId is not found. | The error message returned because the specified Express Connect circuit ID does not exist. |
| 400 | InvalidVlanId.Used | The specified VlanId has been used. | The error message returned because the VLAN ID is being used. |
| 400 | MissingParameter | The input parameter 'PhysicalConnectionId' that is mandatory for processing this request is not supplied. | The error message returned because the PhysicalConnectionId parameter is not specified. |
| 400 | InvalidPhysicalConnectio nId.NotEnabled | The specified PhysicalConnectionId is not in Enabled state. | The error message returned because the Express Connect circuit is in an invalid state. Check the Express Connect circuit and try again. |
| 404 | InvalidVbrOwnerId.NotF ound | The specified VbrOwnerId is not valid. | The error message returned because VbrOwnerId is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'VlanId' that is mandatory for processing this request is not supplied. | The error message returned because VlanId is not set. |
| 400 | InvalidVlanId.Malformed | The specified VlanId is not valid. | The error message returned because the value of VlanId is invalid. |
| 400 | InvalidCircuitCode.Malfo rmed | The specified CircuitCode is not valid. | The error message returned because CircuitCode is set to an invalid value. |
| 400 | MissingParameter | The input parameter 'LocalGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because LocalGatewayIp is not set. |
| 400 | InvalidLocalGatewayIp.M alformed | The specified LocalGatewayIp is not valid. | The error message returned because the IP address of the VBR is invalid. |

| 400 | MissingParameter | The input parameter 'PeerGatewayIp' that is mandatory for processing this request is not supplied. | The error message returned because PeerGatewayIp is not set. |
|---|---|---|---|
| 400 | InvalidPeerGatewayIp.M alformed | The specified PeerGatewayIp is not valid. | The error message returned because the value of PeerGatewayIp is invalid. |
| 400 | MissingParameter | The input parameter 'PeeringSubnetMask' that is mandatory for processing this request is not supplied. | The error message returned because PeeringSubnetMask is not set. |
| 400 | InvalidPeeringSubnetMa sk.Malformed | The specified PeeringSubnetMask is not valid. | The error message returned because PeeringSubnetMask is set to an invalid value. Check whether PeeringSubnetMask is set to a valid value. |
| 403 | Forbidden.LocalGateway IpNotAllowedByCaller | The caller is not allowed to specify the LocalGatewayIp parameter. | The error message returned because you are not allowed to set LocalGatewayIp. |
| 403 | Forbidden.PeerGatewayI pNotAllowedByCaller | The caller is not allowed to specify the PeerGatewayIp parameter. | The error message returned because you are not allowed to set PeerGatewayIp. |
| 403 | Forbidden.PeeringSubne tMaskNotAllowedByCalle r | The caller is not allowed to specify the PeeringSubnetMask parameter. | The error message returned because you are not allowed to set PeeringSubnetMask. |
| 403 | Forbidden.NameNotAllo wedByCaller | The caller is not allowed to specify the Name parameter. | The error message returned because you are not allowed to set Name. |
| 403 | Forbidden.DescriptionNo tAllowedByCaller | The caller is not allowed to specify the Description parameter. | The error message returned because you are not allowed to set Description. |
| 400 | InvalidName.Malformed | The specified ?Name? is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfor med | The specifid ?Description? is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | QuotaExceeded.vbrPerp Conn | Virtual boarder router per PhysicalConnection quota exceed. | The error message returned because the number of VBRs of each Express Connect circuit has reached the upper limit. Reduce the number of VBRs and try again. |
| 400 | EXCEED ASSOCIATE MA _ _ X NUM _ | assocaite virtual boarder num too many. | The error message returned because the number of associated VBRs has reached the upper limit. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidIp.NotSameSubne t | Local gateway ip and peer gateway ip are not in the same subnet. | The error message returned because the IP addresses of the local gateway and the peer gateway do not fall within the same subnet. |
| 400 | InvalidStatus.StatusNotE nabled | The physical connection status is invalid. | The error message returned because the status of the Express Connect circuit does not support this operation. Check the status of the Express Connect circuit. |
| 400 | PHYSICAL NOT ALLOW _ _ _ ASSOCIATE VBR _ | The specified operation not allow. | The error message returned because the Express Connect circuit is associated with a VBR and the operation cannot be performed. |

#### 6.6.12 UnassociatePhysicalConnectionFromVirtualBorderRouter

Disassociates a virtual border router (VBR) from an Express Connect circuit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | UnassociatePhysical ConnectionFromVirtu alBorderRouter | The operation that you want to perform. Set the value to UnassociatePhysicalConnectionFromVirt ualBorderRouter. |
| PhysicalConnectionId | String | Yes | pc- bp1qrb3044eqixog** ** | The ID of the Express Connect circuit from which you want to disassociate a VBR. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the Express Connect circuit. You can call the DescribeRegions operation to query the most recent region list. |
| VbrId | String | Yes | vbr- bp16ksp61j7e0tkn** *** | The ID of the VBR. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 980960B0-2969-40BF- 8542-EBB34FD358AB | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=UnassociatePhysicalConnectionFromVirtualBorderRouter &PhysicalConnectionId=pc-bp1qrb3044eqixog**** &RegionId=cn-qingdao-env66-d01 &VbrId=vbr-bp16ksp61j7e0tkn***** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
  <RequestId>980960B0-2969-40BF-8542-EBB34FD358AB</RequestId>
</UnassociatePhysicalConnectionFromVirtualBorderRouterResponse>
```

`JSON` format `{`

```json
    "RequestId": "980960B0-2969-40BF-8542-EBB34FD358AB"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter does not exist in our records. | The error message returned because the specified VBR does not exist. Check whether the parameter is set to a valid value. |
| 404 | InvalidVbrId.NotFound | The specified VirutalBorderRouter or PhysicalConnection does not exist in our records. | The error message returned because the VBR or the Express Connect circuit does not exist. |
| 400 | PARAMETER MUST NOT _ _ NULL _ | The specified physical connection id or vbrId must not be null. | The error message returned because the VbrId and PhysicalConnectionId parameters are not set. |
| 400 | PHYSICAL NOT ASSOCIA _ _ TE TO VBR _ _ | The specified PhysicalConnection have not associate to the vbr. | The error message returned because no VBR is created for the Express Connect circuit. |
| 400 | ROUTER INTERFACE RE _ _ FERED BY ROUTEENTRY _ _ | The specified VlanInterface has been used by routeEntry. | The error message returned because the VLAN interface is being used by a route entry. |
| 400 | InvalidStatus.NotAllowe d | Invalid virtual border router status. | The error message returned because the status of the VBR does not support this operation. |
| 400 | PHYSICAL NOT ALLOW _ _ _ ASSOCIATE VBR _ | The specified operation not allow. | The error message returned because the Express Connect circuit is associated with a VBR and the operation cannot be performed. |

### 6.7 BGP

#### 6.7.1 CreateBgpGroup

Creates a Border Gateway Protocol (BGP) group for a specified virtual border router (VBR). BGP groups allow VBRs to communicate with data centers. Each BGP group is associated with a VBR. You can add a BGP peer that needs to communicate with a VBR to the corresponding BGP group and advertise the BGP network in the VBR. BGP groups are used to simplify BGP configurations. You can save time and effort by adding BGP peers that use the same configurations to one BGP group. You must use an autonomous system (AS) number to create a BGP group. When you call this operation, take note of the following limits: Only BGP4 is supported by the BGP groups. BGP groups support IPv4 BGP. IPv6 BGP is not supported.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBgpGroup | The operation that you want to perform. Set the value to CreateBgpGroup. |
| PeerAsn | Long | Yes | 65515 | The AS number of the on-premises device. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| RouterId | String | Yes | vbr- m5eadkqe6budw4sj* *** | The ID of the VBR that is associated with the BGP group. |
| Name | String | No | test | The name of the BGP group. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). It must start with a letter. _ It cannot start with http:// or https:// . |
| Description | String | No | BGP | The description of the BGP group. The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with http:// or https:// . |
| LocalAsn | Long | No | 45104 | The AS number of the device on the Apsara Stack side. |
| AuthKey | String | No | !PWZ**** | The authentication key of the BGP group. |
| IsFakeAsn | Boolean | No | true | Specifies whether to use a fake ASN. Valid values: false (default): no true: yes Note A running BGP router typically belongs to only one AS. If you want to replace the current AS with a new one (for example, the current AS needs to be migrated or merged with another one) and you cannot modify BGP configurations, you can specify a fake AS number to establish connections to the on-premises device. This ensures that your services are not interrupted. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
| IpVersion | String | No | ipv4 | The IP version. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpGroupId | String | bgpg- 2zendnzngq9lkjkhv**** | The ID of the BGP group. |
| RequestId | String | C1221A1F-2ACD-4592- 8F27-474E02883159 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateBgpGroup &PeerAsn=45103 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBgpGroupResponse>
  <RequestId>C1221A1F-2ACD-4592-8F27-474E02883159</RequestId>
  <BgpGroupId>bgpg-2zendnzngq9lkjkhv****</BgpGroupId>
</CreateBgpGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "C1221A1F-2ACD-4592-8F27-474E02883159",
    "BgpGroupId": "bgpg-2zendnzngq9lkjkhv****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDescription.M alformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |

| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId is not found. | The error message returned because the specified region ID is invalid. Check whether the service is available in the specified region. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |

#### 6.7.2 DescribeBgpGroups

Queries Border Gateway Protocol (BGP) groups in a region.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpGroups | The operation that you want to perform. Set the value to DescribeBgpGroups. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouterId | String | No | vbr- m5eadkqe6budw4sj0 **** | The ID of the virtual border router (VBR) that is associated with the BGP group that you want to query. |
| BgpGroupId | String | No | bgpg- wz9f62v4fbg2g**** | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the specified BGP group is the default one. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |

| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 10 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| BgpGroups | Array of BgpGroup |   | The detailed information about the BGP group. |
| BgpGroup |   |   |   |
| AuthKey | String | !PWZ**** | The key used by the BGP group. |
| BgpGroupId | String | bgpg- wz9f62v4fbg2g**** | The ID of the BGP group. |
| Description | String | test | The description of the BGP group. |
| Hold | String | 30 | The hold time to receive BGP messages. If no message is received within the hold time, the BGP peer is considered disconnected. |
| IpVersion | String | IPv4 | The IP version. |
| IsFake | String | true | Indicates whether the AS number is fake. |
| Keepalive | String | 10 | The keepalive time. |
| LocalAsn | String | 45104 | The AS number of the device on the Apsara Stack side. |
| Name | String | Name | The name of the BGP group. |
| PeerAsn | String | 1**** | The AS number of the on-premises device. |
| RegionId | String | cn-shangha | The ID of the region to which the BGP group belongs. |
| RouteLimit | String | 99 | The maximum number of routes. |
| RouterId | String | vbr- m5eadkqe6budw4sj0*** * | The ID of the VBR. |
| Status | String | Available | The status of the BGP group. |
| RequestId | String | 1D0971B2-A35A-42C1- A44C-E91360C36C0B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBgpGroups &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpGroupsResponse>
  <TotalCount>10</TotalCount>
  <PageSize>5</PageSize>
  <RequestId>1D0971B2-A35A-42C1-A44C-E91360C36C0B</RequestId>
  <PageNumber>1</PageNumber>
  <BgpGroups>
        <Status>Available</Status>
        <Description>test</Description>
        <IpVersion>IPv4</IpVersion>
        <Keepalive>10</Keepalive>
        <RouterId>vbr-m5eadkqe6budw4sj0****</RouterId>
        <PeerAsn>1****</PeerAsn>
        <Name>BGPname </Name>
        <LocalAsn>45104</LocalAsn>
        <IsFake>true</IsFake>
        <AuthKey>!PWZ****</AuthKey>
        <RouteLimit>99</RouteLimit>
        <RegionId>cn-shangha</RegionId>
        <Hold>30</Hold>
        <BgpGroupId>bgpg-wz9f62v4fbg2g****</BgpGroupId>
  </BgpGroups>
</DescribeBgpGroupsResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "PageSize": 5,
    "RequestId": "1D0971B2-A35A-42C1-A44C-E91360C36C0B",
    "PageNumber": 1,
    "BgpGroups": {
        "Status": "Available",
        "Description": "test",
        "IpVersion": "IPv4",
        "Keepalive": 10,
        "RouterId": "vbr-m5eadkqe6budw4sj0****",
        "PeerAsn": "1****",
        "Name": "BGPname",
        "LocalAsn": 45104,
        "IsFake": true,
        "AuthKey": "!PWZ****",
        "RouteLimit": 99,
        "RegionId": "cn-shangha",
        "Hold": 30,
        "BgpGroupId": "bgpg-wz9f62v4fbg2g****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 6.7.3 ModifyBgpGroupAttribute

Modifies the configuration of a Border Gateway Protocol (BGP) group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBgpGroupAttri bute | The operation that you want to perform. Set the value to ModifyBgpGroupAttribute. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2g**** | The ID of the BGP group. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
| Name | String | No | test | The name of the BGP group. The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores ( ), and hyphens (-). The name _ must start with a letter and cannot start with http:// or https:// . |
| Description | String | No | BGP | The description of the BGP group. The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| LocalAsn | Long | No | 45104 | The autonomous system (AS) number of the device on the Apsara Stack side. |
| PeerAsn | Long | No | 65515 | The AS number of the on-premises device. |
| AuthKey | String | No | !PWZ2**** | The authentication key of the BGP group. |
| IsFakeAsn | Boolean | No | false | Specifies whether to use a fake AS number. Valid values: false (default): no true: yes Note A running BGP router typically belongs to only one AS. If you want to replace the current AS with a new one (for example, the current AS needs to be migrated or merged with another one) and you cannot modify BGP configurations, you can specify a fake AS number to establish connections to the on-premises device. This ensures that your services are not interrupted. |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 8C3C6D7C-A1CE-4FD8- BC57-DC493A55F76F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBgpGroupAttribute &BgpGroupId=bgpg-wz9f62v4fbg2g**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBgpGroupAttributeResponse>
  <RequestId>8C3C6D7C-A1CE-4FD8-BC57-DC493A55F76F</RequestId>
</ModifyBgpGroupAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "8C3C6D7C-A1CE-4FD8-BC57-DC493A55F76F"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |

| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
|---|---|---|---|
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

#### 6.7.4 DeleteBgpGroup

Deletes a Border Gateway Protocol (BGP) group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpGroup | The operation that you want to perform. Set the value to DeleteBgpGroup. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg2g**** | The ID of the BGP group that you want to delete. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 97E2E97F-968C-48AF- A310-AC4D068854DB | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteBgpGroup &BgpGroupId=bgpg-wz9f62v4fbg2g**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpGroupResponse>
  <RequestId>97E2E97F-968C-48AF-A310-AC4D068854DB</RequestId>
</DeleteBgpGroupResponse>
```

`JSON` format `{`

```json
    "RequestId": "97E2E97F-968C-48AF-A310-AC4D068854DB"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |

| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
|---|---|---|---|
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

#### 6.7.5 CreateBgpPeer

Adds a Border Gateway Protocol (BGP) peer to a BGP group.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateBgpPeer | The operation that you want to perform. Set the value to CreateBgpPeer. |
| BgpGroupId | String | Yes | bgpg- wz9f62v4fbg**** | The ID of the BGP group to which you want to add a BGP peer. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| PeerIpAddress | String | No | 116.62.XX.XX | The IP address of the BGP peer. |
| EnableBfd | Boolean | No | true | Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values: true: enables BFD. false: disables BFD. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
| IpVersion | String | No | ipv4 | The IP version. |
| BfdMultiHop | Integer | No | 3 | The multihop BFD feature. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpPeerId | String | bgp- m5eoyp2mwegk8ce9v** ** | The ID of the BGP peer. |
| RequestId | String | D4B7649A-61BB-4C64- A586-1DFF1EDA6A42 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateBgpPeer &BgpGroupId=bgpg-wz9f62v4fbg**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateBgpPeerResponse>
  <BgpPeerId>bgp-m5eoyp2mwegk8ce9v****</BgpPeerId>
  <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId>
</CreateBgpPeerResponse>
```

`JSON` format `{`

```json
    "BgpPeerId": "bgp-m5eoyp2mwegk8ce9v****",
    "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |

| Express Conn | ect |   | Developer Guide·API Reference |
|---|---|---|---|

| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
|---|---|---|---|
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

#### 6.7.6 DescribeBgpPeers

Queries Border Gateway Protocol (BGP) peers in a specific region.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpPeers | The operation that you want to perform. Set the value to DescribeBgpPeers. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region to which the BGP group belongs. You can call the DescribeRegions operation to query the most recent region list. |
| RouterId | String | No | vbr- 2zecmmvg5gvu8i4te **** | The ID of the virtual border router (VBR) that is associated with the BGP group. |
| BgpPeerId | String | No | bgp- 2ze3un0ft1jd1xd**** | The ID of the BGP peer. |
| BgpGroupId | String | No | bgpg- 2zev8h2wo414sfh*** * | The ID of the BGP group. |
| IsDefault | Boolean | No | false | Specifies whether the BGP group is the default BGP group. Value true: no false: yes |
| PageNumber | Integer | No | 1 | The page number of the page to return. Default value: 1. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpPeers | Array of BgpPeer |   | The detailed information about the BGP peer. |
| BgpPeer |   |   |   |
| Name | String | test | The name of the BGP peer. |

| PeerIpAddress | String | 116.62.XX.XX | The IP address of the BGP peer. |
|---|---|---|---|
| AuthKey | String | !PWZ**** | The authentication key of the BGP group. |
| RouterId | String | vbr- 2zecmmvg5gvu8i4te*** * | The ID of the VBR that is associated with the BGP group. |
| Status | String | Available | The status of the BGP peer. Valid values: Pending: being configured Available: available Modifying: being modified Deleting: being deleted Deleted: deleted |
| BfdMultiHop | Integer | 3 | The multihop Bidirectional Forwarding Detection (BFD) feature. |
| BgpGroupId | String | bgp- 2zev8h2wo414sfh**** | The ID of the BGP group. |
| BgpPeerId | String | bgp- 2ze3un0ft1jd1xd**** | The ID of the BGP peer. |
| BgpStatus | String | Connect | The status of the BGP connection. Valid values: creating: being created Connect: being used modifying: being modified deleting: being deleted deleted: deleted |
| Description | String | test | The description of the BGP peer. |
| EnableBfd | Boolean | true | Indicates whether the BFD protocol is enabled. |
| Hold | String | 30 | The hold time. |
| IpVersion | String | ipv4 | The IP version. |
| IsFake | String | true | Indicates whether a fake autonomous system (AS) number is used. |
| Keepalive | String | 10 | The keepalive time. |
| LocalAsn | String | 45104 | The AS number of the device on the Apsara Stack side. |
| PeerAsn | String | 65515 | The AS number of the BGP peer. |
| RegionId | String | cn-qingdao-env66-d01 | The ID of the region to which the BGP peer belongs. |
| RouteLimit | String | 99 | The maximum number of routes. |

| TotalCount | Integer | 10 | The number of entries returned. |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| RequestId | String | DE77A7F3-3B74-41C0- A5BC-CAFD188C28B6 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBgpPeers &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpPeersResponse>
  <TotalCount>10</TotalCount>
  <BgpPeers>
        <Status>active</Status>
        <Description>test</Description>
        <IpVersion>ipv4</IpVersion>
        <PeerIpAddress>116.62.XX.XX</PeerIpAddress>
        <Keepalive>10</Keepalive>
        <RouterId>vbr-2zecmmvg5gvu8i4te****</RouterId>
        <PeerAsn>65515</PeerAsn>
        <Name>test</Name>
        <BgpPeerId>bgp-2ze3un0ft1jd1xd****</BgpPeerId>
        <LocalAsn>45104</LocalAsn>
        <BfdMultiHop>3</BfdMultiHop>
        <EnableBfd>true</EnableBfd>
        <BgpStatus>Connect</BgpStatus>
        <IsFake>true</IsFake>
        <AuthKey>!PWZ****</AuthKey>
        <RouteLimit>99</RouteLimit>
        <RegionId>cn-qingdao-env66-d01</RegionId>
        <Hold>30</Hold>
        <BgpGroupId>bgp-2zev8h2wo414sfh****</BgpGroupId>
  </BgpPeers>
  <PageSize>2</PageSize>
  <RequestId>DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6</RequestId>
  <PageNumber>1</PageNumber>
</DescribeBgpPeersResponse>
```

`JSON` format `{`

```json
    "TotalCount": 10,
    "BgpPeers": {
        "Status": "active",
        "Description": "test",
        "IpVersion": "ipv4",
        "PeerIpAddress": "116.62.XX.XX",
        "Keepalive": 10,
        "RouterId": "vbr-2zecmmvg5gvu8i4te****",
        "PeerAsn": 65515,
        "Name": "test",
        "BgpPeerId": "bgp-2ze3un0ft1jd1xd****",
        "LocalAsn": 45104,
        "BfdMultiHop": 3,
        "EnableBfd": true,
        "BgpStatus": "Connect",
        "IsFake": true,
        "AuthKey": "!PWZ****",
        "RouteLimit": 99,
        "RegionId": "cn-qingdao-env66-d01",
        "Hold": 30,
        "BgpGroupId": "bgp-2zev8h2wo414sfh****"
```

`},`

```json
    "PageSize": 2,
    "RequestId": "DE77A7F3-3B74-41C0-A5BC-CAFD188C28B6",
    "PageNumber": 1
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 6.7.7 ModifyBgpPeerAttribute

Modifies the configuration of a Border Gateway Protocol (BGP) peer.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyBgpPeerAttrib ute | The operation that you want to perform. Set the value to ModifyBgpPeerAttribute. |
| BgpPeerId | String | Yes | Bgp- m5eoyp2mwegk8ce 9v**** | The ID of the BGP peer that you want to modify. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the BGP peer. You can call the DescribeRegions operation to query the most recent region list. |
| BgpGroupId | String | No | bgpg- wz9f62v4fbg**** | The ID of the BGP group. |
| PeerIpAddress | String | No | 116.62.XX.XX | The IP address of the BGP peer. |

| EnableBfd | Boolean | No | true | Specifies whether to enable the Bidirectional Forwarding Detection (BFD) feature. Valid values: true: enables BFD. false: disables BFD. |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
| BfdMultiHop | Integer | No | 3 | The multihop BFD feature. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | D4B7649A-61BB-4C64- A586-1DFF1EDA6A42 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyBgpPeerAttribute &BgpPeerId=Bgp-m5eoyp2mwegk8ce9v**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyBgpPeerAttributeResponse>
  <RequestId>D4B7649A-61BB-4C64-A586-1DFF1EDA6A42</RequestId>
</ModifyBgpPeerAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "D4B7649A-61BB-4C64-A586-1DFF1EDA6A42"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 6.7.8 DeleteBgpPeer

Deletes a Border Gateway Protocol (BGP) peer.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpPeer | The operation that you want to perform. Set the value to DeleteBgpPeer. |
| BgpPeerId | String | Yes | bgp- wz977wcrmb69a**** | The ID of the BGP peer that you want to delete. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the BGP peer. You can call the DescribeRegions operation to query the most recent region list. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | AEBB1EB6-3C15-4A35- B4CE-03485200C143 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteBgpPeer &BgpPeerId=bgp-wz977wcrmb69a**** &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpPeerResponse>
  <RequestId>AEBB1EB6-3C15-4A35-B4CE-03485200C143</RequestId>
</DeleteBgpPeerResponse>
```

`JSON` format `{`

```json
    "RequestId": "AEBB1EB6-3C15-4A35-B4CE-03485200C143"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|

| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the virtual border router (VBR) has reached the upper limit. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified virtual private cloud (VPC) does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

#### 6.7.9 AddBgpNetwork

Advertises a Border Gateway Protocol (BGP) network.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AddBgpNetwork | The operation that you want to perform. Set the value to AddBgpNetwork. |
| DstCidrBlock | String | Yes | 10.10.**. **/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |
| RegionId | String | Yes | cn-shanghai | The ID of the region where the virtual border router (VBR) is deployed. You can call the DescribeRegions operation to query region IDs. |
| RouterId | String | Yes | vrt- 2zeo3xzyf38r4u***** * | The ID of the vRouter associated with the router interface. |
| VpcId | String | No | vpc- bp1qpo0kug3a2***** | The ID of the VPC. |
| ClientToken | String | No | 02fb3da4-130e- 11e9-8e44- 0016e04115b | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9C7FA9D6-72E0-48A9- A9C3-2DA8569CD5EB | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/? Action=AddBgpNetwork &DstCidrBlock=10.10. **. **/32 &RegionId=cn-shanghai &RouterId=vrt-2zeo3xzyf38r4u****** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AddBgpNetworkResponse>
      <RequestId>0ED8D006-F706-4D23-88ED-E11ED28DCAC0</RequestId>
</AddBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "0ED8D006-F706-4D23-88ED-E11ED28DCAC0"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number exceeds the VBR quota. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the quota. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple physical connections cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified vRouter does not exist. Check whether the ID of the VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the verification key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as that of Apsara Stack. |
| 400 | InvalidParams.NotNull | parameter must not null. | The error message returned because a required parameter is not set. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because the state is invalid and the operation cannot be performed. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | QuotaExceeded.Bgp | bgp group count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the quota. |

#### 6.7.10 DescribeBgpNetworks

Queries advertised Border Gateway Protocol (BGP) networks.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeBgpNetwork s | The operation that you want to perform. Set the value to DescribeBgpNetworks. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the virtual border router (VBR) to which the advertised BGP CIDR blocks belong. You can call the DescribeRegions operation to query the most recent region list. |
| IpVersion | String | No | ipv4 | The IP version. |
| RouterId | String | No | vbr- m5eadkqe6budw4sj0 **** | The ID of the VBR to which the advertised BGP CIDR block belongs. |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BgpNetworks | Array of BgpNetwork |   | The details of the advertised BGP CIDR blocks. |
| BgpNetwork |   |   |   |
| DstCidrBlock | String | 10.10.XX.XX/32 | The advertised BGP CIDR block. |
| RouterId | String | vbr- m5eadkqe6budw4sj**** | The ID of the VBR to which the advertised BGP CIDR blocks belong. |
| Status | String | Available | The status of the advertised BGP CIDR block. |
| VpcId | String | vpc-bp1qpo0kug3a**** | The ID of the virtual private cloud (VPC). |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 6F513A15-669F-419D- B511-08A85292059B | The ID of the request. |
| TotalCount | Integer | 1 | The number of advertised BGP CIDR blocks. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeBgpNetworks &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeBgpNetworksResponse>
  <TotalCount>1</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>6F513A15-669F-419D-B511-08A85292059B</RequestId>
  <PageNumber>1</PageNumber>
  <BgpNetworks>
        <Status>Available</Status>
        <DstCidrBlock>10.10.XX.XX/32</DstCidrBlock>
        <VpcId>vpc-bp1qpo0kug3a****</VpcId>
        <RouterId>vbr-m5eadkqe6budw4sj****</RouterId>
  </BgpNetworks>
</DescribeBgpNetworksResponse>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "6F513A15-669F-419D-B511-08A85292059B",
    "PageNumber": 1,
    "BgpNetworks": {
        "Status": "Available",
        "DstCidrBlock": "10.10.XX.XX/32",
        "VpcId": "vpc-bp1qpo0kug3a****",
        "RouterId": "vbr-m5eadkqe6budw4sj****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 500 | InternalError | The request processing has failed due to some unknown error. | The error message returned because an unknown error occurred. |
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |

#### 6.7.11 DeleteBgpNetwork

Deletes an advertised Border Gateway Protocol (BGP) network.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteBgpNetwork | The operation that you want to perform. Set the value to DeleteBgpNetwork. |
| DstCidrBlock | String | Yes | 10.10.XX.XX/32 | The CIDR block of the virtual private cloud (VPC) or vSwitch that you want to connect to a data center. |

| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the virtual border router (VBR). You can call the DescribeRegions operation to query the most recent region list. |
|---|---|---|---|---|
| RouterId | String | Yes | vbr- m5eadkqe6budw4sj0 **** | The ID of the VBR to which the BGP network to be deleted belongs. |
| IpVersion | String | No | ipv4 | The IP version. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 22F4C006-D3BB-4F96- 9FF9-4C8335276D70 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteBgpNetwork &DstCidrBlock=10.10.XX.XX/32 &RegionId=cn-qingdao-env66-d01 &RouterId= vbr-m5eadkqe6budw4sj0**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteBgpNetworkResponse>
  <RequestId>22F4C006-D3BB-4F96-9FF9-4C8335276D70</RequestId>
</DeleteBgpNetworkResponse>
```

`JSON` format `{`

```json
    "RequestId": "22F4C006-D3BB-4F96-9FF9-4C8335276D70"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | Specified value of "regionId" is not supported. | The error message returned because RegionId is set to an invalid value. Check whether the service is available in the specified region. |

| 400 | QuotaExceeded.Bgp | bgp peer count per vbr quota exceed. | The error message returned because the number of BGP groups in the VBR has reached the upper limit. |
|---|---|---|---|
| 400 | QuotaExceeded.Nqa | nqa count per vbr quota exceed. | The error message returned because the Network Quality Analyzer (NQA) number has reached the upper limit. |
| 400 | QuotaExceeded.BgpNet work | bgp network count per vbr quota exceed. | The error message returned because the number of BGP networks in the VBR has reached the upper limit. |
| 400 | InvalidPeerIpAddress | multi pconn peer ip can not be null. | The error message returned because the IP addresses of multiple Express Connect circuits cannot be empty. |
| 400 | InvalidVbrNetwork | vbr netowrk not exists | The error message returned because the specified VBR does not exist. Check whether the specified VBR is valid. |
| 400 | InvalidBgpGroup | bgp group not exists | The error message returned because the BGP group does not exist. |
| 400 | InvalidBgpName.Malfor med | Specified Bgp Group name is not valid. | The error message returned because the name of the BGP group is invalid. |
| 400 | InvalidBgpDiscription.Ma lformed | Specified Bgp Group description is not valid. | The error message returned because the description of the BGP group is invalid. |
| 400 | InvalidBgpAuthkey.Malfo rmed | Specified Bgp Group authkey is not valid. | The error message returned because the authentication key of the BGP group is invalid. |
| 400 | InvalidIP.Malformed | Ip malformed. | The error message returned because the format of the IP address is invalid. |
| 400 | InvalidPeerAsn.Malforme d | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous system (AS) number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotNull | invalid peer asn cannot equals aliyun asn:45104 | The error message returned because the autonomous AS number cannot be the same as the AS number on the Apsara Stack side. |
| 400 | InvalidParams.NotFound | instance not found | The error message returned because the specified instance does not exist. |
| 400 | InvalidParams.NotFound | vpc instance not found | The error message returned because the specified VPC does not exist. Check whether the specified VPC ID is valid. |
| 400 | InvalidParams.AlreadyEx ists | bgp network already exists | The error message returned because the BGP network already exists. |
| 400 | InvalidStatus.CannotOpe rate | invalid status cannot operate | The error message returned because you cannot perform the operation when the specified resource is in the current state. |

### 6.8 Router interface

#### 6.8.1 CreateRouterInterface

Creates a router interface.

**Usage notes**

When you call this operation, take note of the following limits: You can create only one pair of interfaces to be connected between two routers. You can create a maximum of five router interfaces for a router. Each destination CIDR block of route entries in the same route table must be unique. A virtual border router (VBR) can serve only as an initiator. The VBR must be in the Activated state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRouterInterfac e | The operation that you want to perform. Set the value to CreateRouterInterface. |
| OppositeRegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the acceptor. |
| RegionId | String | Yes | cn-qingdao-env33- d01 | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| Role | String | Yes | InitiatingSide | The role of the router interface. Valid values: InitiatingSide: initiator AcceptingSide: acceptor |
| RouterId | String | Yes | vrt- n3619981j2qdfyhfc** ** | The ID of the router that is associated with the router interface. |
| RouterType | String | Yes | VRouter | The type of the router associated with the router interface. Valid values: VRouter: a vRouter VBR: a VBR |
| Spec | String | Yes | Mini.2 | The specification of the router interface. Valid values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s Note When Role is set to AcceptingSide (acceptor), Spec is set to Negative. |
| OppositeInterfaceId | String | No | ri- 2zeo3xzyf38r4urzd** ** | The ID of the peer router interface. |
| OppositeRouterId | String | No | vrt- bp1lhl0taikrteen8*** * | The ID of the peer router. |

| OppositeRouterType | String | No | VRouter | The type of the router associated with the peer router interface. Valid values: VRouter: a vRouter VBR: a VBR |
|---|---|---|---|---|
| OppositeInterfaceOw nerId | String | No | 2348**** | The ID of the account to which the peer router interface belongs. |
| HealthCheckSourceIp | String | No | 116.62.XX.XX | The source IP address that is used to perform health checks. The source IP address must be an idle IP address of the local virtual private cloud (VPC). Note You can set this parameter if an Express Connect circuit is used. |
| HealthCheckTargetIp | String | No | 116.12.XX.XX | The destination IP address that is used to perform health checks. Note This parameter is required when the HealthCheckSourceIp parameter is set. |
| AccessPointId | String | No | ap-cn-sha**** | The ID of the access point to which the VBR belongs. You can call the DescribeAccessPoints operation to query the most recent access point list. Note This parameter is required when the VBR is connected to an Express Connect circuit. |
| OppositeAccessPointI d | String | No | ap-cn-sha**** | The ID of the access point to which the peer belongs. Note This parameter is required when the peer router interface is associated with a VBR. The specified value cannot be changed after the router interface is created. |
| Description | String | No | Description | The description of the router interface. The description must be 2 to 255 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| Name | String | No | Name | The name of the router interface. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores ( ), and hyphens (-). The _ name must start with a letter. |

| Period | Integer | No | 3 | The subscription duration. Valid values: Valid values when the PricingCycle parameter is set to Month: 1 to 9. Valid values when the PricingCycle parameter is set to Year: 1 to 3. Note This parameter is required when InstanceChargeType is set to PrePaid. |
|---|---|---|---|---|
| InstanceChargeType | String | No | PrePaid | The billing method of the router interface. Valid values: PrePaid: subscription PostPaid (default): pay-as-you-go |
| AutoPay | Boolean | No | false | Specifies whether to enable auto-renewal for the instance. Valid values: false: disables automatic payment. After an order is generated, you must go to the Order Center to complete the payment. true: enables automatic payment. Payments are automatically completed. Note This parameter is required when InstanceChargeType is set to PrePaid. |
| PricingCycle | String | No | Month | The billing cycle of the subscription. Valid values: Month (default): monthly subscription Year: annual subscription Note This parameter is required when InstanceChargeType is set to PrePaid. |
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| OrderId | Long | 202008594930117 | The order number. This parameter is returned when InstanceChargeType is set to PrePaid. |
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

| RouterInterfaceId | String | ri-2ze7fbuohm**** | The ID of the router interface. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateRouterInterface &OppositeRegionId=cn-qingdao-env66-d01 &RegionId=cn-qingdao-env33-d01 &Role=InitiatingSide &RouterId=vrt-123**** &RouterType=VRouter &Spec=Mini.2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<CreateRouterInterfaceResponse>
  <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
  <OrderId>202008594930117</OrderId>
  <RouterInterfaceId>ri-2ze7fbuohm****</RouterInterfaceId>
</CreateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907",
    "OrderId": 202008594930117,
    "RouterInterfaceId": "ri-2ze7fbuohm****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The regionId provided does not exist in our records. | The error message returned because the specified region ID does not exist. Check whether the region ID is valid. |
| 400 | InvalidRole.ValueNotSup ported | The specified Role is not valid. | The error message returned because Role is set to an invalid value. Check whether the specified value is valid. |
| 400 | InvalidSpec.ValudNotSu pported | The specified Spec is not supported. | The error message returned because the specification does not support this operation. Change the specification and try again. |
| 400 | InvalidRouterType.Value NotSupported | The specified RouterType is not valid. | The error message returned because the type of the router is invalid. |
| 404 | InvalidRouterId.NotFoun d | The specified RouterId does not exist in our recored. | The error message returned because the specified router ID does not exist. |
| 400 | InvalidName.Malformed | The specified "Name" is not valid. | The error message returned because the format of the name is invalid. |
| 400 | InvalidDescription.Malfor med | The specifid "Description" is not valid. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |

| 400 | Forbidden.BillsOutstandi ng | You cannot create more RouterInterface because you have bills outstanding. | The error message returned because the router interface cannot be created when you have unsettled bills. |
|---|---|---|---|
| 400 | LimitationExceed.Interfa ceNumberOnRouter | Total number of RouterInterfaces on a Router exceeded. | The error message returned because the number of router interfaces reaches the quota. |
| 400 | Forbidden.NotInRouterIn terfaceCreateWhitelist | Not in router interface create whitelist. | The error message returned because you are not included in the whitelist to create router interfaces. |
| 400 | RI CREATE ONE LIMIT B _ _ _ _ Y SYNC _ | Create ri only one limit by sync. | The error message returned because you can create only one router interface at a time. |
| 400 | InvalidAccessPoint.Value NotAllowed | The non-vbr router interface cannot have access point configured. | The error message returned because you cannot configure access points for the router interface of a vRouter. |
| 400 | InvalidAccessPoint.Value NotAllowed | The non-vbr opposite router interface cannot have opposite access point configured. | The error message returned because you cannot configure access points for the router interface of a vRouter. |
| 400 | InvalidAccessPoint.NotM atch | The accessPoint id is not matched | The error message returned because the specified ID of the access point is invalid. |
| 400 | InvalidAccessPoint.NotE xist | The accessPoint not exit | The error message returned because the access point does not exist. |
| 400 | InvalidRouterType.Value NotSupported | The specified RouterType is not valid | The error message returned because the type of the router is invalid. |

#### 6.8.2 ConnectRouterInterface

Initiates a connection from the initiator router interface to the acceptor. After you call this operation, the router interface enters the Connecting state. When the connection is established, it enters the Active state. When you call this operation, take note of the following: Only an initiator router interface in the Idle state can initiate a connection. You can interconnect only a single pair of router interfaces between two routers. You cannot initiate a connection if your account contains a router interface with overdue payments.

**Request parameters**

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ConnectRouterInterfac e | The operation that you want to perform. Set the value to ConnectRouterInterface. |
| RegionId | String | Yes | cn-hangzhou | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterface Id | String | Yes | ri-2ze7fbuohm**** | The ID of the initiator router interface. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |
|---|---|---|---|

**Examples**

**Sample requests**

```
https://vpc.example.com/?Action=ConnectRouterInterface &RegionId=cn-hangzhou &RouterInterfaceId=ri-2ze7fbuohm**** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<? xml version="1.0" encoding="UTF-8"? > <ConnectRouterInterfaceResponse>
     <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ConnectRouterInterfaceResponse>
```

JSON format `{`

```json
   "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

#### 6.8.3 DeactivateRouterInterface

Disables a router interface.

**Usage notes**

After you call this operation, the status of the router interface changes to **Deactivating**. After the router interface is disabled, its status changes to **Inactive**.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeactivateRouterInte rface | The operation that you want to perform. Set the value to DeactivateRouterInterface. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz*** * | The ID of the router interface. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | BE7EB53A-99AB-4DA8- AEDE-75FA90D046A6 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeactivateRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ActivateRouterInterfaceResponse>
  <RequestId>BE7EB53A-99AB-4DA8-AEDE-75FA90D046A6</RequestId>
</ActivateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "BE7EB53A-99AB-4DA8-AEDE-75FA90D046A6"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRouterInterfaceId. NotFound | The specified RouterInterfaceId does not exist in our record. | The error message returned because the specified router interface does not exist. Check whether the specified router interface is valid. |
| 400 | IncorrectStatus | RouterInterface can be operated by this action only when it's status is Active. | The error message returned because the operation cannot be performed. The operation can be performed only when the the router interface is in the Active state. |

#### 6.8.4 ModifyRouterInterfaceSpec

Modifies the specification of a router interface.

**Usage notes**

After you call this operation, the router interface enters the **Activating** state. When the router interface is activated, it enters the **Active** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterfac eSpec | The operation that you want to perform. Set the value to ModifyRouterInterfaceSpec. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The region ID of the router interface. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urzd** ** | The ID of the router interface. |

| Spec | String | Yes | Mini.2 | The specification of the router interface. Valid values: Mini.2: 2 Mbit/s Mini.5: 5 Mbit/s Small.1: 10 Mbit/s Small.2: 20 Mbit/s Small.5: 50 Mbit/s Middle.1: 100 Mbit/s Middle.2: 200 Mbit/s Middle.5: 500 Mbit/s Large.1: 1,000 Mbit/s Large.2: 2,000 Mbit/s Large.5: 5,000 Mbit/s Xlarge.1: 10,000 Mbit/s Note When Role is set to AcceptingSide (acceptor), Spec is set to Negative. |
|---|---|---|---|---|
| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |
| Spec | String | Mini.2 | The specification of the router interface. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRouterInterfaceSpec &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urzd**** &Spec=Mini.2 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyRouterInterfaceSpecResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
  <Spec>Mini.2</Spec>
</ModifyRouterInterfaceSpecResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF",
    "Spec": "Mini.2"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidSpec.ValudNotSu pported | The specified Spec is not supported. | The error message returned because the specification does not support this operation. Change the specification and try again. |
| 404 | InvalidRouterInterfaceId. NotFound | The specified RouterInterfaceId does not exist in our record. | The error message returned because the specified router interface does not exist. Check whether the specified router interface is valid. |
| 400 | InvalidInstanceOwner.Er ror | The router instance owener error. | The error message returned because the vRouter does not belong to your Apsara Stack tenant account. |
| 400 | InvalidInstance.StatusEr ror | The router instance owener error. | The error message returned because the state of the instance is invalid. |
| 400 | InvalidOpposite.NotFoun d | The opposite not exit. | The error message returned because the peer does not exist. |

#### 6.8.5 DeleteRouterInterface

Deletes a router interface.

**Usage notes**

When you call this operation, take note of the following limits: You can delete only a router interface that is in the **Idle** or **Inactive** state. Before you delete a router interface, you must delete all custom route entries destined for the router interface.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteRouterInterfac e | The operation that you want to perform. Set the value to DeleteRouterInterface. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the router interface is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz*** * | The ID of the router interface. |

| ClientToken | String | No | 123e4567-e89b- 12d3-a456- 426655440000 | The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Note If you do not set this parameter, the system automatically uses RequestId as ClientToken. RequestId of each API request may be different. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DeleteRouterInterfaceResponse>
  <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</DeleteRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | IncorrectStatus | This openeration would be allowed only when status of this RouterInterface is Idle/Inactive. | The error message returned because you are not authorized to perform the specified operation. The error message returned because the router interface is not in the Idle or Inactive state. You can call this operation only when the router interface is in the Idle or Inactive state. |
| 400 | DependencyViolation.Ro uterInterfaceReferedByR outeEntry | RouterInterface cannot be deleted when it is refered by a route table entry as next hop. | The error message returned because the router interface is used as a next hop of a route entry and cannot be deleted. Delete the route entry before you delete the router interface. |
| 404 | InvalidInstanceId.NotFou nd | The InstanceId provided does not exist in our records. | The error message returned because the specified Elastic Compute Service (ECS) instance does not exist in the virtual private cloud (VPC). |

| 400 | InvalidRouterInterfaceC hargeType.Malformed | The prepaid routerinterface can not delete. | The error message returned because you cannot delete a subscription router interface. |
|---|---|---|---|

#### 6.8.6 DescribeRouterInterfaces

Queries router interfaces in a region.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRouterInterf aces | The operation that you want to perform. Set the value to DescribeRouterInterfaces. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the router interface is created. You can call the DescribeRegions operation to query the most recent region list. |
| IncludeReservationD ata | Boolean | No | false | Specifies whether to include renewal data. Valid values: true: yes false (default): no |
| PageNumber | Integer | No | 1 | The number of the page to return. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Maximum value: 50. Default value: 10. |

| Filter.N.Key | String | No | status | The filter condition. You can specify at most five filter conditions. The following filter conditions are supported: RouterInterfaceId: the ID of the router interface. RouterId: the ID of the router. RouterType: the router type. Valid values: VRouter and VBR. RouterInterfaceOwnerId: the ID of the Apsara Stack tenant account to which the router interface belongs. OppositeInterfaceId: the ID of the peer router interface. OppositeRouterType: the type of the peer router interface. Valid values: VRouter and VBR. OppositeRouterId: the ID of the peer router interface. OppositeInterfaceOwnerId: the ID of the Apsara Stack tenant account to which the peer router interface belongs. Status: the status of the router interface. Name: the name of the router interface. Note The logical operator between multiple values in a filter condition is OR. In this case, the filter condition is met if one of the values is matched. The logical operator between filter conditions is AND, which means that a result is returned only when all conditions are met. |
|---|---|---|---|---|
| Filter.N.Value.N | RepeatList | No | Active | The filter values for keys. You can specify multiple filter values for one key. The logical operator between filter values is OR. If one filter value is matched, the filter key is matched. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 2 | The number of entries returned. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | C7F6FCBD-F9CC-4501- 8EF3-CDC9577CAE45 | The ID of the request. |
| RouterInterfaceSet | Array of RouterInterfaceTy pe |   | The details about the router interface. |
| RouterInterfaceTy pe |   |   |   |
| AccessPointId | String | ap-cn-shanghaiSZ-**** | The ID of the access point. |

| Bandwidth | Integer | 10 | The maximum bandwidth of the router interface. Unit: Mbit/s. |
|---|---|---|---|
| BusinessStatus | String | Normal | The service status of the router interface. Valid values: Normal: normal FinancialLocked: locked due to overdue payments SecurityLocked: locked due to security reasons |
| ChargeType | String | PayByTraffic | The billing method. |
| ConnectedTime | String | 2021-06-08T12:20:55 | The time when the connection was established. |
| CreationTime | String | 2021-06-08T12:20:55 | The time when the route table was created. |
| CrossBorder | Boolean | false | Indicates whether the connection is a cross-border connection. |
| Description | String | The description of the router interface. | The description of the router interface. |
| EndTime | String | 2021-06-08T12:20:55 | The end of the time range queried. |
| HasReservationDa ta | String | false | Indicates whether renewal data is included. |
| HcRate | Integer | 1 | The rate of heath checks. |
| HcThreshold | Integer | 2 | The healthy threshold. |
| HealthCheckSourc eIp | String | 116.62.XX.XX | The source IP address that is used for health checks. |
| HealthCheckTarge tIp | String | 116.62.XX.XX | The destination IP address that is used for health checks. |
| Ipv6Status | String | on | Indicates whether IPv6 protection is enabled. Valid values: on: yes off: no unsupport: not supported |
| Name | String | test | The custom name. |
| OppositeAccessPoi ntId | String | ap-cn-shanghaiSZ-**** | The ID of the peer access point. |
| OppositeBandwidt h | Integer | 12 | The maximum bandwidth of the peer router interface. Unit: Mbit/s. |
| OppositeInterface BusinessStatus | String | Normal | The service status of the peer router interface. |
| OppositeInterfaceI d | String | ri- bp1itx13bwe6f2wfh**** | The ID of the peer router interface. |

| Express Connect |   |   | Developer Guide·API Reference |
|---|---|---|---|

| OppositeInterface OwnerId | String | 123157908552**** | The ID of the Apsara Stack tenant account to which the peer router interface belongs. |
|---|---|---|---|
| OppositeInterfaceS pec | String | Large | The specification of the peer router interface. |
| OppositeInterfaceS tatus | String | Normal | The status of the peer router interface. |
| OppositeRegionId | String | cn-qingdao-env66-d01 | The region ID of the peer router interface. |
| OppositeRouterId | String | vrt- bp1d3bxtdv68tfd7g**** | The ID of the router to which the peer router interface belongs. |
| OppositeRouterTy pe | String | VRouter | The type of the router to which the peer router interface belongs. |
| OppositeVpcInstan ceId | String | vpc- bp1qpo0kug3a20qqe*** * | The ID of the peer virtual private cloud (VPC). |
| ReservationActive Time | String | 2021-08-11T16:00:00Z | The time when the renewal takes effect. |
| ReservationBandw idth | String | 10 | The maximum bandwidth after the renewal takes effect. Unit: Mbit/s. |
| ReservationInterne tChargeType | String | PayByBandwidth | The metering method that is used after the renewal takes effect. |
| ReservationOrderT ype | String | RENEWCHANGE | The type of the renewal order. |
| Role | String | InitiatingSide | The role of the router interface in the peering connection. |
| RouterId | String | vrt- bp1d3bxtdv68tfd7g**** | The ID of the router to which the route belongs. |
| RouterInterfaceId | String | ri- 2zenfgfpyu3v93koa**** | The ID of the router interface. |
| RouterType | String | VRouter | The type of the router to which the route table belongs. Valid values: VRouter: a vRouter VBR: a virtual border router (VBR) |
| Spec | String | Large | The specification of the router interface. |
| Status | String | active | The status of the router interface. |
| VpcInstanceId | String | vpc- 2ze3tq4uxhysg717x**** | The ID of the local VPC. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRouterInterfaces &RegionId=cn-qingdao-env66-d01 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeRouterInterfacesResponse>
  <TotalCount>2</TotalCount>
  <PageSize>10</PageSize>
  <RequestId>C7F6FCBD-F9CC-4501-8EF3-CDC9577CAE45</RequestId>
  <PageNumber>1</PageNumber>
  <RouterInterfaceSet>
        <OppositeInterfaceStatus>Normal</OppositeInterfaceStatus>
        <OppositeInterfaceId>ri-bp1itx13bwe6f2wfh****</OppositeInterfaceId>
        <OppositeRouterId>vrt-bp1d3bxtdv68tfd7g****</OppositeRouterId>
        <Description>Description </Description>
        <EndTime>2021-06-08T12:20:55</EndTime>
        <RouterId>vrt-bp1d3bxtdv68tfd7g****</RouterId>
        <BusinessStatus>Normal</BusinessStatus>
        <Name>test</Name>
        <ReservationOrderType>RENEWCHANGE</ReservationOrderType>
        <OppositeRouterType>VRouter</OppositeRouterType>
        <OppositeBandwidth>12</OppositeBandwidth>
        <Bandwidth>10</Bandwidth>
        <ConnectedTime>2021-06-08T12:20:55</ConnectedTime>
        <ReservationActiveTime>2021-08-11T16:00:00Z</ReservationActiveTime>
        <HcThreshold>2</HcThreshold>
        <ReservationBandwidth>10</ReservationBandwidth>
        <Status>active</Status>
        <OppositeInterfaceOwnerId>123157908552****</OppositeInterfaceOwnerId>
        <OppositeRegionId>cn-qingdao-env66-d01</OppositeRegionId>
        <HealthCheckSourceIp>116.62.XX.XX</HealthCheckSourceIp>
        <HasReservationData>false</HasReservationData>
        <CrossBorder>false</CrossBorder>
        <HcRate>1</HcRate>
        <ReservationInternetChargeType>PayByBandwidth</ReservationInternetChargeType>
        <OppositeInterfaceSpec>Large</OppositeInterfaceSpec>
        <Role>InitiatingSide</Role>
        <OppositeVpcInstanceId>vpc-bp1qpo0kug3a20qqe****</OppositeVpcInstanceId>
        <RouterType>VRouter</RouterType>
        <Ipv6Status>on</Ipv6Status>
        <ChargeType>PayByTraffic</ChargeType>
        <AccessPointId>ap-cn-shanghaiSZ-****</AccessPointId>
        <CreationTime>2021-06-08T12:20:55</CreationTime>
        <VpcInstanceId>vpc-2ze3tq4uxhysg717x****</VpcInstanceId>
        <OppositeInterfaceBusinessStatus>Normal</OppositeInterfaceBusinessStatus>
        <OppositeAccessPointId>ap-cn-shanghaiSZ-****</OppositeAccessPointId>
        <Spec>Large</Spec>
        <HealthCheckTargetIp>116.62.XX.XX</HealthCheckTargetIp>
        <RouterInterfaceId>ri-2zenfgfpyu3v93koa****</RouterInterfaceId>
  </RouterInterfaceSet>
</DescribeRouterInterfacesResponse>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 10,
    "RequestId": "C7F6FCBD-F9CC-4501-8EF3-CDC9577CAE45",
    "PageNumber": 1,
    "RouterInterfaceSet": {
        "OppositeInterfaceStatus": "Normal",
        "OppositeInterfaceId": "ri-bp1itx13bwe6f2wfh****",
        "OppositeRouterId": "vrt-bp1d3bxtdv68tfd7g****",
        "Description": "RouterInterfaceDescription",
        "EndTime": "2021-06-08T12:20:55",
        "RouterId": "vrt-bp1d3bxtdv68tfd7g****",
        "BusinessStatus": "Normal",
        "Name": "test",
        "ReservationOrderType": "RENEWCHANGE",
        "OppositeRouterType": "VRouter",
        "OppositeBandwidth": 12,
        "Bandwidth": 10,
        "ConnectedTime": "2021-06-08T12:20:55",
        "ReservationActiveTime": "2021-08-11T16:00:00Z",
        "HcThreshold": 2,
        "ReservationBandwidth": 10,
        "Status": "active",
        "OppositeInterfaceOwnerId": "123157908552****",
        "OppositeRegionId": "cn-qingdao-env66-d01",
        "HealthCheckSourceIp": "116.62.XX.XX",
        "HasReservationData": false,
        "CrossBorder": false,
        "HcRate": 1,
        "ReservationInternetChargeType": "PayByBandwidth",
        "OppositeInterfaceSpec": "Large",
        "Role": "InitiatingSide",
        "OppositeVpcInstanceId": "vpc-bp1qpo0kug3a20qqe****",
        "RouterType": "VRouter",
        "Ipv6Status": "on",
        "ChargeType": "PayByTraffic",
        "AccessPointId": "ap-cn-shanghaiSZ-****",
        "CreationTime": "2021-06-08T12:20:55",
        "VpcInstanceId": "vpc-2ze3tq4uxhysg717x****",
        "OppositeInterfaceBusinessStatus": "Normal",
        "OppositeAccessPointId": "ap-cn-shanghaiSZ-****",
        "Spec": "Large",
        "HealthCheckTargetIp": "116.62.XX.XX",
        "RouterInterfaceId": "ri-2zenfgfpyu3v93koa****"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidFilterKey.ValueNo tSupported | Specified filter key is not supported: Filter.X.key | The error message returned because Filter.X.key is not supported. |
| 400 | InvalidParam.NotNull | The parameter must not be null. | The error message returned because a required parameter is not set. |

#### 6.8.7 ActivateRouterInterface

Activates a router interface that is in the Inactive state.

**Usage notes**

After you call this operation, the router interface enters the **Activating** state. When the router interface is activated, it enters the **Active** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ActivateRouterInterf ace | The operation that you want to perform. Set the value to ActivateRouterInterface. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the router interface is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz*** * | The ID of the router interface. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 079874CD-AEC1-43E6- AC03-ADD96B6E4907 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ActivateRouterInterface &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ActivateRouterInterfaceResponse>
  <RequestId>079874CD-AEC1-43E6-AC03-ADD96B6E4907</RequestId>
</ActivateRouterInterfaceResponse>
```

`JSON` format `{`

```json
    "RequestId": "079874CD-AEC1-43E6-AC03-ADD96B6E4907"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidRouterInterfaceId. NotFound | The specified RouterInterfaceId does not exist in our records. | The error message returned because the specified router interface does not exist. Check whether the specified router interface is valid. |
| 400 | IncorrectStatus | RouterInterface can be operated by this action only when it's status is Inactive. | The error message returned because the operation cannot be performed. The operation can be performed only when the router interface is in the Inactive state. |

| 400 | Forbbiden | The Router instance owener error | The error message returned because the specified router does not belong to your Apsara Stack tenant account. |
|---|---|---|---|

#### 6.8.8 ModifyRouterInterfaceAttribute

Modifies the configuration of a router interface.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyRouterInterfac eAttribute | The operation that you want to perform. Set the value to ModifyRouterInterfaceAttribute. |
| RegionId | String | Yes | cn-qingdao-env66- d01 | The ID of the region where the router interface is created. You can call the DescribeRegions operation to query the most recent region list. |
| RouterInterfaceId | String | Yes | ri- 2zeo3xzyf38r4urz*** * | The ID of the router interface. |
| Name | String | No | test | The name of the router interface. The name must be 2 to 128 characters in length, and can contain letters, digits, underscores ( ), and hyphens (-). The name _ must start with a letter. |
| Description | String | No | Router interfaces | The description of the router interface. The description must be 2 to 255 characters in length. It must start with a letter but cannot start with http:// or https:// . |
| OppositeInterfaceId | String | No | ri- 2zeo3xzyf38r4urz*** * | The ID of the peer router interface. |
| OppositeRouterId | String | No | vrt- bp1jcg5cmxjbl9xgc** ** | The ID of the peer router. |
| OppositeRouterType | String | No | VRouter | The type of the router to which the peer router interface belongs. Valid values: VRouter VBR (default) |
| OppositeInterfaceOw nerId | Long | No | 10 | The ID of the Apsara Stack tenant account to which the peer router interface belongs. |
| HealthCheckSourceIp | String | No | 116.62.XX.XX | The source IP address that is used to perform health checks. The source IP address must be an idle IP address of the local virtual private cloud (VPC). Note You can set this parameter if an Express Connect circuit is used. |

| HealthCheckTargetIp | String | No | 116.62.XX.XX | The destination IP address that is used to perform health checks. Note This parameter is required when the HealthCheckSourceIp parameter is set. |
|---|---|---|---|---|
| HcThreshold | Integer | No | 12 | The healthy threshold. |
| HcRate | Integer | No | 2 | The rate of heath checks. |
| DeleteHealthCheckIp | Boolean | No | true | Specifies whether to delete the IP addresses for health checks configured on the router interface. Valid values: true: yes false (default): no |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 4EC47282-1B74-4534- BD0E-403F3EE64CAF | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyRouterInterfaceAttribute &RegionId=cn-qingdao-env66-d01 &RouterInterfaceId=ri-2zeo3xzyf38r4urz**** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ModifyRouterInterfaceAttributeResponse>
      <RequestId>4EC47282-1B74-4534-BD0E-403F3EE64CAF</RequestId>
</ModifyRouterInterfaceAttributeResponse>
```

`JSON` format `{`

```json
    "RequestId": "4EC47282-1B74-4534-BD0E-403F3EE64CAF"
```

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 404 | InvalidRegionId.NotFoun d | The specified RegionId does not exist in our records. | The error message returned because the specified region ID does not exist. |
| 404 | InvalidRouterInterfaceId. NotFound | The specified RouterInterfaceId does not exist in our records. | The error message returned because the specified router interface does not exist. Check whether the specified router interface is valid. |
| 400 | Forbidden.FinancileLock ed | This RouterInterface is financiel locked because of bills outstanding. | The error message returned because the router interface is locked due to overdue payments. |

| 400 | InvalidName.Malformd | The attribute name is illeagl. | The error message returned because the format of the name is invalid. |
|---|---|---|---|
| 400 | InvalidOppositeRouterTy pe.ValueNotSupported | The specified OppositeRouterType is not valid. | The error message returned because OppositeRouterType is set to an invalid value. |
| 400 | InvalidDescription.Malfor med | The Description is illeagl. | The error message returned because the specified description is invalid. The description must be 2 to 256 characters in length and cannot start with http:// or https://. |
| 400 | Forbbiden | The Router instance owener error | The error message returned because the specified router does not belong to your Apsara Stack tenant account. |
| 400 | LinkRole.NotSupport | This linkrole is not supported | The error message returned because this link is not supported. |
| 400 | InvalidParam.ModifyRou terInterface | Modify routerinterface param invalide | The error message returned because the value of the parameter that you set to modify the router interface is invalid. |

## 7 Appendixes

### 7.1 STS overview

#### 7.1.1 What is STS?

Apsara Stack Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed for Apsara Stack resource access only by using an STS token. When an STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use an STS token to assume a RAM role**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify a validity period for an STS token. The token automatically becomes invalid when it expires. You do not need to rotate STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 7.1.2 AssumeRole

Obtains a Security Token Service (STS) token to assume a RAM role. In this operation, an Alibaba Cloud account is used as the trusted entity of the Resource Access Management (RAM) role.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::1234567890 12****:role/adminrole | The Alibaba Cloud Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Alibaba Cloud account. |
| RoleSessionName | String | Yes | alice | The custom name of the role session. You can specify the value of this parameter based on your business requirements. In most cases, this parameter is set to the identity of the user who calls the operation, such as the username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource": ["*"]}],"Version":"1"} | The policy that specifies the permissions of the returned STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The value of the parameter must be 1 to 1,024 characters in length. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71-4EF5- 88FA-F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg5U1 **** | The AccessKey ID. |
| AccessKeySecret | String | ***************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The STS token. |
| Expiration | String | 2015-04-09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789012 ****:role/adminrole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495****:ali ce | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM:

```xml
    <dependency>
      <groupId>com.aliyun</groupId>
      <artifactId>aliyun-java-sdk-core</artifactId>
      <version>[4.4.9,5.0.0)</version>
    </dependency>
```

**Call an API operation to obtain the STS AccessKey triplet.**

In the following sample code, the `Sts::AssumeRole::2015-04-01` operation is used to obtain the triplet.

```java
package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "
<yourAccessKeySecret>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setIgnoreSSLCerts(true);
        clientConfig.setProtocolType(ProtocolType.HTTPS);
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        CommonRequest request = new CommonRequest();
        // Replace "sts.aliyuns.com" with the actual endpoint of the STS token. In most cases, the STS toke
n is in the following format: sts-vpc.${global:region}.${global:internet-domain}.
        request.setSysDomain("sts.aliyuns.com");
        request.setSysProduct("Sts");
        request.setSysAction("AssumeRole");
        request.setSysVersion("2015-04-01");
        request.setSysMethod(MethodType.POST);
        request.setHttpContentType(FormatType.FORM);
        // Replace "<yourRoleSessionName>" with the alias that you specify in this API operation for the ro
le session. It is a business parameter.
        request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
        // Replace "<yourRoleArn>" with the actual ARN that you obtain in the preceding step for the RAM ro
le.
        request.putQueryParameter("RoleArn", "<yourRoleArn>");
        try {
            CommonResponse response = client.getCommonResponse(request);
            String assumeRole = response.getData();
            if (StringUtils.isEmpty(assumeRole)) return;
            JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
            JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
            // Obtain the STS triplet.
            String stsAK = credentials.getString("AccessKeyId");
            String stsSK = credentials.getString("AccessKeySecret");
            String stsToken = credentials.getString("SecurityToken");
            System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken);
        } catch (ServerException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
        } catch (ClientException e) {
            System.out.println(e.getErrCode());
            System.out.println(e.getErrMsg());
```

**Call examples**

In the following sample code, the `DescribeZones` operation in Elastic Compute Service (ECS) is used.

```java
package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo {
    public static void main(String[] args) {
        // Replace "<yourRegionID>" with the actual region ID.
        // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret in
the STS triplet that you obtain in the preceding step.
        DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "
<yourStsAccessKeySecret>");
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
        //Replace "<yourRegionID>" with the actual region ID.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
        // Replace "<yourStsToken>" with the STS token in the STS triplet that you obtain in the preceding
step.
        request.putQueryParameter("SecurityToken", "<yourStsToken>");
        // Specify the resource set ID. It is optional.
        // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
        // Specify the organization ID. It is required.
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

**Error codes**

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |

|   | Developer Guide·Appendi | xes |   | Express Connec | t |
|---|---|---|---|---|---|

| HTTP status code | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.RoleArn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleSessio nName | The parameter RoleSessionName is wrongly formed. | The error message returned because the format of the RoleSessionName parameter is invalid. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.DurationSe conds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The value must be greater than or equal to 900 and less than or equal to the MaxSessionDuration value. |
| 400 | InvalidParameter.PolicyGram mar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the specified policy is invalid. |
| 400 | InvalidParameter.PolicySize | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error has occurred. |
