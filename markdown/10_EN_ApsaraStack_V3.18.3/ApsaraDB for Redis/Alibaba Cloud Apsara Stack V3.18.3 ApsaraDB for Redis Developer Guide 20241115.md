---
title: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Developer Guide 20241115"
product_version: "V3.18.3"
doc_version: "20241115"
pdf_pages: 116
source_pdf: "Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Developer Guide 20241115.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/V3.18.3/Redis/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.3%20ApsaraDB%20for%20Redis%20Developer%20Guide%2020241115.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes+edge-junk)
---

# Alibaba Cloud Apsara Stack V3.18.3 ApsaraDB for Redis Developer Guide 20241115

## Table of Contents

- 1 Getting started
  - 1.1 Usage notes on development documentation
  - 1.2 Process of API calls
- 2 Preparations
  - 2.1 Obtain the information and the endpoint of an API operation
  - 2.2 Obtain an AccessKey pair
  - 2.3 Obtain the values of common request headers
  - 2.4 Obtain access credentials assigned by STS
- 3 Use POP to make API calls
  - 3.1 Preparations
  - 3.2 SDK for Java
  - 3.3 SDK for Go
  - 3.4 SDK for Python
- 4 API reference
  - 4.1 API overview
  - 4.2 Request structures
  - 4.3 Common parameters
  - 4.4 Responses
  - 4.5 Request signatures
  - 4.6 RAM-based authorization
    - 4.6.1 Grant resource permissions to a RAM user
    - 4.6.2 Authorized resource types in RAM
    - 4.6.3 Operation permissions granted to a RAM user
    - 4.6.4 API authentication rules
  - 4.7 Manage the lifecycle
    - 4.7.1 DescribeZones
    - 4.7.2 CreateInstance
    - 4.7.3 DeleteInstance
    - 4.7.4 ModifyInstanceSpec
  - 4.8 Manage instances
    - 4.8.1 RestartInstance
    - 4.8.2 FlushExpireKeys
    - 4.8.3 DescribeLogicInstanceTopology
    - 4.8.4 DescribeEngineVersion
    - 4.8.5 DescribeInstanceAttribute
    - 4.8.6 DescribeInstances
    - 4.8.7 DescribeRegions
    - 4.8.8 DescribeSecurityIps
    - 4.8.9 FlushInstance
    - 4.8.10 ModifyInstanceAttribute
    - 4.8.11 ModifyInstanceMaintainTime
    - 4.8.12 ModifyInstanceNetExpireTime
    - 4.8.13 ModifySecurityIps
    - 4.8.14 SwitchNetwork
  - 4.9 Data encryption
    - 4.9.1 DescribeEncryptionKey
    - 4.9.2 DescribeInstanceTDEStatus
    - 4.9.3 CheckCloudResourceAuthorized
  - 4.10 Account management
    - 4.10.1 DescribeUserInfo
    - 4.10.2 CreateAccount
  - 4.11 Network security
    - 4.11.1 DescribeInstanceSSL
  - 4.12 Connection management
    - 4.12.1 DescribeIntranetAttribute
    - 4.12.2 ModifyInstanceVpcAuthMode
    - 4.12.3 AllocateInstancePublicConnection
  - 4.13 Backup and recovery
    - 4.13.1 CreateBackup
    - 4.13.2 ModifyBackupPolicy
    - 4.13.3 DescribeBackupPolicy
    - 4.13.4 DescribeBackups
    - 4.13.5 RestoreInstance
  - 4.14 Manage monitoring
    - 4.14.1 DescribeMonitorItems
    - 4.14.2 DescribeHistoryMonitorValues
  - 4.15 Manage parameters
    - 4.15.1 DescribeInstanceConfig
    - 4.15.2 ModifyInstanceConfig
  - 4.16 Appendixes
    - 4.16.1 Instance types
    - 4.16.2 Error codes
    - 4.16.3 Instance configurations

## 1 Getting started

### 1.1 Usage notes on development documentation

**documentation**

This topic describes how to view the desired product development documentation when you use Apsara Stack API (ASAPI).

**Procedure**

You can follow the procedure described in the following figure to view the desired development documentation.

**Prerequisites**

The Apsara Stack version is obtained from an O&M personnel or operations administrator.

**Procedure**

You can go to the Apsara Stack documentation center and view the desired product documentation.
1. Go to the Apsara Stack Documentation Centerpage by using a browser.
2. Click the **Enterprise**, **Agility**, or **All-in-one** tab based on the Apsara Stack version that you
use.
3. Select an Apsara Stack version from the drop-down list.
4. In the left-side navigation pane, select the name of the product that you want to view.
5. In the upper-right corner of the product documentation section, click **View Details** or
**Download PDF**.

### 1.2 Process of API calls

You can use POP Gateway or the Apsara Stack API (ASAPI) gateway to call Apsara Stack API operations. From Apsara Stack Enterprise V3.16.0, POP Gateway is used by default to ensure that user experience is consistent with that in Alibaba Cloud public cloud. This topic describes how to use POP Gateway to call Apsara Stack API operations.

**Note**

You can continue to use the ASAPI gateway to call Apsara Stack API operations in Apsara Stack that is earlier than V3.16.0. For more information, see Process of API calls by using ASAPI, Generate an endpoint for ASAPI , and Obtain an SDK package for ASAPI.

**Flowchart**

**Procedure**

1. Obtain an AccessKey pair.
For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair or Obtain an AccessKey pair from STS.

> **Note:** If you want to make API calls to use the Apsara Uni-manager Management Console or other Apsara Stack services, we recommend that you use the AccessKey pair of a personal account.

2. Obtain the region ID.
For more information about how to obtain the value of the RegionID parameter, see Obtain header parameters.
3. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Develop er Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Develope r Guide.

| <x-acs- |   |
|---|---|

> **Note:** When you call an operation, specify the `<x-acs-organizationid>` and `<x-acs-`

|   | resourcegroupid>, |
|---|---|

> `resourcegroupid>,` header parameters. The organization ID <x-acs-organizationid> and resource set ID <x-acs-resourcegroupid> specify the organization and resource set to which a resource belong. This implements isolated query of instance resources.
> If you do not specify the `<x-acs-organizationid>` parameter, the organization to which the current user belongs is obtained by default.
> If you do not specify the `<x-acs-resourcegroupid>` parameter, no resource set IDs are specified by default. If you specify a resource set ID, you must specify an organization ID.

4. Obtain the API reference of a service.
For more information about how to view, use, and obtain the developer guide of a specific service, and understand the features and usage methods of operations, see Usage notes.
5. Obtain the endpoint of the service.
6. Obtain the service SDK and use the SDK to call an operation of the service.

## 2 Preparations

### 2.1 Obtain the information and the endpoint of an API operation

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

### 2.2 Obtain an AccessKey pair

An AccessKey pair consists of an AccessKey ID and an AccessKey secret. AccessKey pairs are used to implement symmetric encryption to verify the identity of requesters. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. This topic describes how to obtain an AccessKey pair.

**Prerequisites**

An account that assumes the operations administrator or level-1 organization administrator role is obtained. Only an operations administrator or a level-1 organization administrator can obtain an AccessKey pair of the organization.

**Background information**

AccessKey supports the following authorization methods: Use RAM to authorize the AccessKey ID and AccessKey secret to third-party requesters. Use STS to authorize the AccessKey ID, AccessKey secret, and security token to third-party requesters. This topic describes how to obtain an AccessKey pair authorized by RAM. For more information about how to obtain an AccessKey pair authorized by STS, see **Obtain an STS**
**AccessKey pair**.
We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions can occur.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region, such as cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which to perform operations. For example, you can query the ID of an Elastic Compute Service (ECS) instance from the ECS instance list. |

> **Warning:** The AccessKey pair of a personal account is managed and controlled by the permission system of the Apsara Uni-manage Management Console. If you need to obtain the AccessKey pair of an account that has permissions on an organization, make sure that your operation is allowed by an administrator. This ensures security. The account that has permissions on an organization is a privileged account.

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and
choose **User Information** from the shortcut menu.
3. In the **Apsara Stack AccessKey Pair** section, obtain the AccessKey pair.

> **Note:** The AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide you with full permissions on Apsara Stack resources. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization navigation tree, click the name of the level-1 organization for which you
want to obtain AccessKey pairs.
5. Click **Management AccessKey** on the right side of the page.
6. In the AccessKey message, view the AccessKey pair of the organization.

### 2.3 Obtain the values of common request headers

**request headers**

You must provide multiple request headers when you call API operations in Apsara Stack. This topic describes how to obtain the values of common request headers. This topic also explains the response parameters that are returned after you call API operations.

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the desired organization.
5. In the **Regions** list, obtain the region ID from the **Region Name** column.

**Obtain an organization ID**

You must call a specific API operation to obtain an organization ID. You can obtain an organization ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `GetOrganizationList` operation and debug the operation online. Set the
name parameter to the name of the organization that you want to query and click Initiate Call. Obtain the organization ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the GetOrganizationList topic in Apsara Uni-manager Operations Console Developer Guide.

**Obtain a resource set ID**

You must call a specific API operation to obtain a resource set ID. You can obtain a resource set ID by using the online debugging feature in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, choose **Products** > **Application Services** > **OpenAPI**
**Explorer**.
3. On the **OpenAPI Explorer** page, choose **API Integration** > **API Debugging** in the top
navigation bar.
4. Move the pointer over the
icon and choose **Platform** > **Apsara Uni-manager**. Select
**2019-05-10** from the **Version** drop-down list.
5. Search for the `ListResourceGroup` operation and debug the operation online. Obtain the
resource set ID from the **id** parameter on the **Call Result** tab. For more information about this operation, see the ListResourceGroup topic in Apsara Uni-manager Operations Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in the cloud service console of the Apsara Uni-manager Management Console. For example, to obtain the ID of an API gateway, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > Application Services > API Gateway.
3. In the left-side navigation pane, click **Instances**.
4. View the **instance ID** in the instance list.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |

| ResourceGroup | The ID of a resource set. |
|---|---|
| DepartmentName | The name of the organization. |
| Department | The ID of an organization. |

### 2.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call API operations in Apsara Stack.

**Background information**

STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call API operations.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your `Resource Access Management (RAM)`
`role` . i. Log on to the Apsara Uni-manager Management Console. ii. In the upper-right corner of the homepage, click the profile picture and then click **User**
**Information**.
iii. On the page that appears, click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your `RAM role` .

|   | stsAK |
|---|---|
| RAM role |   |

2. Use the following code to obtain an AccessKey ID ( `stsAK` ), AccessKey secret ( `stsSK` ),
and STS token ( `stsToken` ) by assuming the `RAM role` .

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
     // Specify the description of the call source.
        asClient.setSdkSource("test");
     // Specify the ARN.
        String assumeRole = AssumeRole(asClient, "<RAM Role>");
        JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole);
        JSONObject credentials = assumeRoleJson.getJSONObject("Credentials");
        // Obtain the access credentials assigned by STS.
        String stsAK = credentials.getString("AccessKeyId");
        String stsSK = credentials.getString("AccessKeySecret");
        String stsToken = credentials.getString("SecurityToken");
```

`}`

```
public static String AssumeRole(ASClient asClient, String roleArn) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "AssumeRole");
        reqParams.put("Product", "Sts");
        reqParams.put("Version", "2015-04-01");
        reqParams.put("regionId", regionId);
     // The AccessKey ID of the current user.
        reqParams.put("AccessKeyId", <The AccessKey ID of the current user>);
     // The AccessKey secret of the current user.
        reqParams.put("AccessKeySecret", <The AccessKey secret of the current user>);
        reqParams.put("roleSessionName", "StsUser");
        reqParams.put("roleArn", roleArn);
        return asClient.doRequest(endpoint, headers, reqParams);
```

`}`
3. Use the access credentials assigned by STS to call an API operation of a cloud service. In
this example, the Elastic Compute Service (ECS) API is used.

```
public static void main(String[] args) {
     ASClient asClient = new ASClient();
        asClient.setSdkSource("test");
  // Call an API operation of ECS.
        String ecsRes = DescribeZones(asClient,<stsAK>,<stsSK>,<stsToken>);
```

`}`

```
public static String DescribeZones(ASClient asClient, String stsAK, String stsSK, Str ing stsToken) {
        Map<String, String> headers = new HashMap<>();
        Map<String, Object> reqParams = new HashMap<>();
        reqParams.put("action", "DescribeZones");
        reqParams.put("Product", "Ecs");
        reqParams.put("Version", "2014-05-26");
        reqParams.put("regionId", "<your-RegionID>");
        // Specify the AccessKey ID, AccessKey secret, and STS token.
        reqParams.put("AccessKeyId", <stsAK>);
        reqParams.put("AccessKeySecret", <stsSK>);
        reqParams.put("SecurityToken", <stsToken>);
        return asClient.doRequest(endpoint, headers, reqParams, HttpMethod.GET);
```

`}` e API calls

## 3 Use POP to make API calls

### 3.1 Preparations

You can use the point of presence (POP) gateway to call API operations in Apsara Stack in the same way as in Alibaba Cloud public cloud. This topic describes the preparations before you use the POP gateway to call API operations.

**Background information**

To enable you to call API operations in the same way as that in Alibaba Cloud public cloud and have a more convenient and consistent experience, we recommend that you use the POP gateway to call API operations in Apsara Stack.

**Obtain service endpoints**

**Obtain an endpoint in OpenAPI Explorer**

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

**Obtain an endpoint in Apsara Infrastructure Management**

e API calls To use the POP gateway to call API operations in Apsara Stack, you must obtain the required service endpoints. You can obtain service endpoints from Apsara Stack onsite O&M engineers You can also obtain service endpoints by yourself. In this example, API Gateway is used.
1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation** > **Apsara Infrastructure**
**Management** > **O&M Tools**.
3. In the left-side navigation pane, choose **O&M Tools** > **Service Registration Variable**
**Dashboard**.
4. On the Service Registration Variable Dashboard page, click **Advanced Filter**.
5. Enter `apigateway` in the Service Registration field and click **Search**.
icon.
6. In the **Service Registration** column of the apigateway service, click the
7. Click the text information in the **Service Registration** column of the `apigateway` service.
In the **Registration Variables** message, obtain the endpoint from the value of apigateway.openapi.endpoint.

**Obtain common parameters**

You must obtain the parameters required when you use the POP gateway to call API operations, such as the organization ID, resource set ID, region ID, and instance ID. For more information, see Obtain the values of common request headers.

### 3.2 SDK for Java

Before you use an SDK for Java to call the API of a cloud service over the point of presence (POP) gateway, you must check the style of the service API. A service API can be of the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException;
```

e API calls `p` `y` `p` `p`

```java
import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the service endpoint.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the service code.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use Security Token Service (STS) to call RPC API operations, you must
specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Specify service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete
operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
```

e API calls

```java
        try {
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate validation.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the connection timeout period.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Set the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
//Specifytheserviceendpoint.
```

e API calls

```java
        // Specify the service endpoint.
        request.setSysDomain("<crEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-06-07");
        // Specify the uriPattern parameter, which is required for ROA APIs.
        request.setSysUriPattern("/namespace");
        // Specify the service code.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. The call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. The resource set ID.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. The organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for modify and delete
operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, yo
u must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
            // Initiate the request and handle the response or exceptions.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}`

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following setting:

e API calls Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable certificate verification for the client. clientConfig.setIgnoreSSLCerts(true)
```

### 3.3 SDK for Go

This topic describes how to use SDK for Go over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues. Proceed with caution.

**Background information**

Remote Procedure Call (RPC) and Resource-Oriented Architecture (ROA) APIs are supported.

**Examples**

The following sample code provides an example on how to call RPC APIs. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code: e API calls

```java
package main import (
    "fmt"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
```

`)`

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
    // If you use Security Token Service (STS) to call RPC API operations, you must spe
cify the SecurityToken parameter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. The call source.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. The instance ID. This parameter is required for modify and delete oper
ations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The following sample code provides an example on how to call ROA APIs. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06- 07. Sample code: e API calls

```java
package main import (
 "fmt"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
 "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
 "os"
```

`)`

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
 // If you use STS to call ROA API operations, you must specify the x-acs-security-
token header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. The call source.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0 and
earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource set ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. The instance ID. This parameter is required for modify and delete operati
ons.
 // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
 response, err := client.ProcessCommonRequest(request)
 if err != nil {
  panic(err)
```

`}`

```
 fmt.Print(response.GetHttpContentString())
```

`}`

**Proxy configuration**

You can configure proxies for API calls in one of the following ways: Configure proxies by using environment variables. Set the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variable. Sample code: e API calls

```java
import (
    "os"
```

`)`

```
func main(){
 os.Setenv("HTTP_PROXY", "http://x.x.x.x:xxxx") // Set the HTTP_PROXY environment var
iable.
 os.Setenv("HTTPS_PROXY", "https://x.x.x.x:xxxx") // Set the HTTPS_PROXY environment
variable.
```

`}` Configure proxies on the client. Sample code:

```
// The proxies that are configured on the client take precedence over those that are configured by using environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Configure the HTTP proxy. client.GetHttpProxy() // Query the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Configure the HTTPS proxy. client.GetHttpsProxy() // Query the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Configure the proxy whitelist. client.GetNoProxy() // Query the proxy whitelist.
```

**SSL verification**

**Description**

You can configure SSL verification for requests. If you set the HTTPSInsecure parameter to `true` , certificate verification is disabled. To ensure connection security, we recommend that you enable certificate verification. If you set the HTTPSInsecure parameter to `false` , certificate verification is enabled. By default, certificate authority (CA) certificates on the operating systems are used.

**Default value**

```
 false
```

**Configuration methods**

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported. To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can specify the following settings:

e API calls

```
// If you configure the HTTPSInsecure parameter for a request, the setting takes effect only on the current request. request.SetHTTPSInsecure(true) // Set the HTTPSInsecure parame ter to true for the request. isInsecure := request.GetHTTPSInsecure() // Query the setting of the HTT PSInsecure parameter for the request.
```

If you do not configure the HTTPSInsecure parameter for a request, the setting for a client takes effect.

```
// If you configure the HTTPSInsecure parameter for the client, the setting takes effec t on all requests that are initiated by the client. client.SetHTTPSInsecure(true) // Set the HTTPSInsecure parameter to true for the client. isInsecure := client.GetHTTPSInsecure() // Query the setting of the HTTPSI nsecure parameter for the client.
```

### 3.4 SDK for Python

This topic describes how to use SDK for Python over the point of presence (POP) gateway.

**Usage notes**

We recommend that you use CommonRequest to call Apsara Stack APIs. To view the recommended SDK version and sample code, log on to the Apsara Uni-manager Management Console and choose **Products** > **Application Services** > **OpenAPI Explorer** in the top navigation bar. On the OpenAPI Explorer page, choose **API Integration** > **SDK Sample**
**Code** in the top navigation bar.

**Important**

We recommend that you do not download SDKs from theSDK Centerand use them in Apsara Stack. SDKs for the public cloud may not support Apsara Stack APIs and may have compatibility issues.Proceed with caution.

**Background information**

Only remote procedure call (RPC) APIs are supported.

**Example**

The following sample code provides an example on how to make an API call. In this example, the DescribeInstances operation of Elastic Compute Service (ECS) is called, and the API version is 2014-05-26. Sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey Secret>",
```

e API calls

```
    "<your-RegionID>",
    timeout=1000,  # Specify the timeout period.
    verify=False, # Disable SSL certificate verification. To enable SSL certificate ver
ification, specify verify='<The path of the certificate>'.
```

);

```python
# Set the following parameters for the HTTPS request protocol:
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create an API request and specify the required parameters.
    request = CommonRequest()
    # If you use Security Token Service (STS) to call RPC API operations, you must spec
ify the SecurityToken parameter.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required. The call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. The region ID. This parameter is required for Apsara Stack Enterpri
se Edition V3.15.0 and earlier.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource set ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. The instance ID. This parameter is required for modify and delete o
perations.
        # "x-acs-instanceid":"<your-InstanceID>"
```

`}`

```python
    request.set_headers(headers)
    request.set_version("2016-07-14")
    request.set_action_name("DescribeApiGroups")
    request.set_endpoint("<ApigatewayEndpoint>")   // Replace <ApigatewayEndpoint> with
the actual endpoint.
    request.set_product("apigateway")
    request.set_method("POST")
    # Initiate the API request and display the response.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

e API calls

**Proxy configuration**

You can configure a proxy for API calls by setting the HTTP_PROXY or HTTPS_PROXY environment variable. Sample code:

```bash
# Configure the HTTPS proxy.
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# Configure the HTTP proxy.
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes related configurations for sending API requests over HTTPS.

**Use HTTPS**

By default, the SDKs use HTTPS as the request protocol.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Set the protocol to HTTPS. client.do_action_with_exception(request)
```

**Disable certificate verification**

> **Important:** By default, if you send API requests over HTTPS, the SDK enables certificate verification to verify the validity of SSL/TLS certificates. If no certificate is configured in the development environment, an error that indicates the certificate verification fails is reported.
> To ensure communication security in the production environment, we recommend that you enable certificate verification. If certificate verification must be ignored in the test environment, you can set the `verify` parameter to false.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify=False  # Disable SSL certificate verification.
```

`)`

**Enable certificate verification**

e API calls

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # The region ID.
    verify='./cacert.pem'  # The path of the certificate authority (CA) certificate.
```

`)`

## 4 API reference

### 4.1 API overview

Table 1. Instance lifecycle management API operations

| Operation | Description |
|---|---|
| CreateInstance | Creates an instance. |
| DeleteInstance | Releases an instance. |
| ModifyInstanceSpec | Changes the specifications of a specified instance. |

Table 2. Instance management API operations

| Operation | Description |
|---|---|
| DescribeInstanceAttribute | Queries detailed information about instances. |
| DescribeInstances | Queries basic information about instances. |
| DescribeRegions | Queries available regions. |
| DescribeSecurityIps | Queries the IP whitelist that allows connections to a specified instance from specified IP addresses or CIDR blocks. |
| FlushInstance | Clears an instance. |
| ModifyInstanceAttribute | Sets the attribute for a specified instance. |
| ModifyInstanceMaintainTime | Changes maintenance time for a specified instance. |
| ModifySecurityIps | Changes the whitelist for a specified instance. |
| ModifyInstanceNetExpireTime | Changes the period for retaining a domain name of a specified classic network. |
| SwitchNetwork | Changes the type of a network. |

Table 3. Backup and recovery API operations

| Operation | Description |
|---|---|
| CreateBackup | Creates a backup. |
| ModifyBackupPolicy | Changes a backup policy. |
| DescribeBackupPolicy | Queries backup policies. |
| DescribeBackups | Queries available backups. |
| RestoreInstance | Restore a specified instance based on a specified backup set. |

Table 4. Monitoring management API operations

| Operation | Description |
|---|---|
| DescribeMonitorItems | Queries available monitoring metrics. |
| DescribeHistoryMonitorValues | Queries historical monitoring data. |

Table 5. Parameter management API operations

| Operation | Description |
|---|---|
| DescribeInstanceConfig | Queries parameters of a specified instance. |
| ModifyInstanceConfig | Changes parameters of a specified instance. |

### 4.2 Request structures

**Endpoint**

The endpoint of the KVStore for Redis API is `r-kvstore.example.com` .

> **Note:** example.com is a domain name that is customized for a project. You can obtain the domain name from the administrator.

**Protocols**

You can send requests over HTTP or HTTPS. To enhance data security, we recommend that you send API requests by using HTTPS.

**Methods**

You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL.

**Request parameters**

You must specify the Action parameter for each request. For example, you can specify CreateInstance. You must also specify common request parameters and specific request parameters that are required by each operation.

**Encoding**

Requests and responses are both encoded in UTF-8.

### 4.3 Common parameters

Common request parameters must be included in all API requests.

**Common request parameters**

Table 1. Common request parameters

| Parameter | Type | Require d | Description |
|---|---|---|---|

| Format | String | Yes | The type of the returned value. Valid values: JSON and XML. Default value: XML |   |   |
|---|---|---|---|---|---|
| Version | String | Yes | The version of the API. Specify the version in the YYYY-MM-DD format. The current version is 2015-01- 01. |   |   |
| AccessKeyId | String | Yes | The AccessKey ID provided by Alibaba Cloud. |   |   |
| Signature | String | Yes | The signature string of the current request. For more information about how signatures are calculated, see Request signatures. |   |   |
| SignatureMeth od | String | Yes | The encryption method of the signature string. Set the value to HMAC-SHA1. |   |   |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time must be in UTC. For example, you can set the parameter to 2016-01- 01T12:00:00Z. This specifies 20:00:00, January 1, 2016, UTC+08:00. |   |   |
|   |   |   |   | yyyy-MM- |   |
| SignatureVersi on | String | Yes | The version of the signature algorithm. The current version is 1.0. |   |   |
| SignatureNonc e | String | Yes | The unique random number that is used to prevent replay attacks. You must use different random numbers for different requests. |   |   |

| es | ddTHH:mm:ssZ |
|---|---|

```
https:// r-kvstore.example.com/ ? Format=json &Version=2015-01-01 &Signature=Pc5xxxxxxxxxxxxxxxxxx &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &AccessKeyId=key-test &Timestamp=2016-01-01T12:00:00Z
```

**Common response parameters**

Each time you call an API operation, the system returns a globally unique ID (RequestId). This is regardless of whether the request is successful.

```xml
<? xml version="1.0" encoding="utf-8"? > <!-The root of the response--> <Operation name+Response> <!—The returned request tag--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The returned result--> </Operation name+Response>
```

### 4.4 Responses

After you call an API operation, KVStore for Redis returns data in the same format. In the

|   | 2xx |
|---|---|
| 5xx |   |

response, an HTTP status code in the `2xx` format indicates that the call is successful. An HTTP status code in the `4xx` or `5xx` format indicates that the call failed. The system returns responses for successful calls in XML or JSON format. You can specify the response format in request parameters. The system uses the XML format by default.

> **Note:** The response examples in this topic have been formatted with line breaks or indents to provide a clear view. The responses in your actual running environments are not properly formatted as these examples.

**Sample success response**

The response in XML format includes a message that indicates whether the call is successful and the specific service data. An example is as follows:

```xml
<? xml version="1.0" encoding="utf-8"? > <!—The root node of the response--> <Operation name+Response> <!—The request ID returned--> <RequestId>4C4fdsf38-3910-447D-87AD-AC078932216</RequestId> <!—The result data returned--> </Operation name+Response>
```

JSON format `{`

```json
"RequestId": "4C4fdsf38-3910-447D-87AD-AC078932216", /* The result data returned */
```

`}`

**Sample error response**

When an error occurs during an API call, no result data is returned. You can locate the cause of the error by referencing the attached list of error codes. If an error occurs when you call an operation over HTTP, an HTTP status code in the `4xx` or `5xx` format is returned. The returned message body includes the specific error code and error message. The message body also contains a globally unique request ID called RequestId and a target site ID called HostId. If you cannot locate the cause, request Apsara Stack customer service, and provide the HostId and RequestId for troubleshooting.

```xml
<? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>8906582E-6722-409A-A6C4-0E7863B733A5</RequestId> <HostId> r-kvstore.example.com</HostId> <Code>UnsupportedOperation</Code> <Message>The specified action is not supported. </Message> </Error>
```

JSON format

```json
"RequestId": "7463B73D-35CC-4D19-A010-6B8D65D242EF", "HostId": " r-kvstore.example.com", "Code": "UnsupportedOperation", "Message": "The specified action is not supported."
```

`}`

### 4.5 Request signatures

KVStore for Redis authenticates each access request. You need to include a signature when you submit an HTTP or HTTPS request. KVStore for Redis authenticates the request sender identity by using symmetric encryption based on an AccessKey pair that consists of an AccessKey ID and an AccessKey secret. An AccessKey ID and an AccessKey secret are issued to you by Alibaba Cloud. You can apply for and manage them on the Alibaba Cloud website. The AccessKey ID is used to verify the identity of the user. The AccessKey secret is used to encrypt and verify the signature string. You must keep your AccessKey secret strictly confidential. For more information about how to obtain the AccessKey pair, see Obtain an AccessKey pair.

**Sign a request**

Perform the following steps to sign an API request:
1. Create a canonicalized query string by using request parameters.
i. To construct a canonicalized query string, sort all request parameters by name in alphabetic order. These parameters include common request parameters and customized API request parameters. However, this does not include the Signature parameter.

> **Note:** When you use the GET method to submit requests, you specify these parameters in the request URI that follow the question mark (?) and are connected with the ampersand (&).

ii. Encode the name and value of each request parameter. Perform URL encoding on the names and values by using the UTF-8 character set. The following section shows the URL encoding rules: Uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), hyphens (-), underscores (_), periods (.), and tildes (~) are not encoded. Encode other characters in the %XY format, where `XY` specifies the ASCII code of the characters in the hexadecimal format. For example, double quotation marks (") are encoded as %22 . Extended UTF-8 characters are encoded in the %XY%ZA format. Spaces must be encoded as %20 . Do not encode spaces as plus signs (+).

|   | Note Libraries that support URL encoding, such as java.net.URLEncoder, follow the Multipurpose Internet Mail Extensions (MIME) encoding rules of application/x- www-form-urlencoded . If this encoding method is used, replace the plus signs (+) in the encoded strings with %20 , the asterisks (*) with %2A , and %7E with a tilde (~) to conform to the encoding rules. |
|---|---|
|   | www-form-urlencoded |

iii. Connect the encoded parameter name and value with an equal sign (=). iv. Sort the key-value pairs connected by equal signs (=) in alphabetical order and separate them with ampersands (&).
2. Create a string-to-sign from the encoded canonicalized query string that is obtained in the
preceding step based on the following rules:

```
 StringToSign=
 HTTPMethod + "&" +
 percentEncode("/") + "&" +
 percentEncode(CanonicalizedQueryString)
```

In this example, `HTTPMethod` specifies the HTTP method that is used to submit the request, such as GET. `percentEncode("/")` is the value ( %2F ) as the result of encoding the slash sign (/) based on the URL encoding rule described in Step 1.b. `percentEncode(CanonicalizedQueryString)` is the string that results from encoding the canonicalized query string described in Step 1 based on the URL encoding rules described in Step 1.b.
3. As defined in RFC 2104, use the preceding signature string to calculate the signature into
an HMAC value.

> **Note:** The key that is used for calculating the signature is your AccessKey secret followed by an ampersand (&) (ASCII:38). The SHA1 algorithm is used for the calculation.

4. Encode the HMAC value in Base64 to obtain the signature string.
5. Add the signature string to the request as the Signature parameter.

> **Note:** When you submit the signature string to the KVStore for Redis instance as the final request parameter value, perform URL encoding on this parameter based on RFC 3986 rules. This is the same method that is used to process other parameters.

**Example**

DescribeDrdsInstances is used in this example. The following section shows the canonicalized query string:

```
http://r-kvstore.example.com/?Timestamp=2013-06- 01T10:33:56Z&Format=XML&AccessKeyId=testid&Action=DescribeInstances&SignatureMethod=HMAC- SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&Version=2015-01- 01&SignatureVersion=1.0
```

The following section shows the calculated StringToSign:

```
GET&%2F&AccessKeyId%3Dtestid&Action%3DDescribeInstances&Format%3DXML&RegionId%3Dregion1&S natureMethod%3DHMAC- SHA1&SignatureNonce%3DNwDAxvLU6tFE0DVb&SignatureVersion%3D1.0&Timestamp%3D2013-06-01T10 %253A33%253A56Z&Version%3D2015-01-01
```

| xample, if the AccessKey ID is testid and used for HMAC calculation is testsecret& BIxxxxxxxxxxxxxxxxxxxxxx= . |   |   | testid | and |
|---|---|---|---|---|
|   | testsecret& |   |   |   |
| BIxxxxxxxxxxxxxxxxxxxxxx= |   |   |   |   |
|   |   | . |   |   |

The following section shows the signed request URL that includes the Signature parameter:

```
http://r-kvstore.example.com/?Timestamp=2013-06- 01T10%3A33%3A56Z&Format=XML&AccessKeyId=testid&Action=DescribeInstances&SignatureMethod=H
```

`C-`

```
SHA1&RegionId=region1&SignatureNonce=NwDAxvLU6tFE0DVb&SignatureVersion=1.0&Version=2015- 01-01&Signature=BIPOMlxxxxxxxxxxxxxxxxxxu8LXBeZtLQkJTw6iFvw1E%3D
```

### 4.6 RAM-based authorization

#### 4.6.1 Grant resource permissions to a RAM user

**user**

The instances that you create by using your Alibaba Cloud account are the resources owned by the account. An account has the full operation permissions on the resources under this account by default. Alibaba Cloud Resource Access Management (RAM) allows you to grant the access and management permissions on resources under a cloud account to RAM users.

> **Note:** Ignore this topic if you do not use Resource Access Management (RAM).

#### 4.6.2 Authorized resource types in RAM

KVStore for Redis only supports RAM authorization for Redis instances. The following table lists the description of resources when you use RAM to authorize access permissions to these resources.

| Resource | Resource description in authorization policy |
|---|---|
| Instance | acs:kvstore:$regionid:$accountid:instance/$insta nceid acs:kvstore:$regionid:$accountid:instance/ acs:kvstore:::instance/ |

All $regionids must be the ID of a region or an asterisk ( `*` ). All $instanceids must be the ID of an instance or an asterisk ( `*` ). Similarly, $account-id is the numerical ID of your Apsara Stack tenant account, which can be replaced by an asterisk ( `*` ).

#### 4.6.3 Operation permissions granted to a RAM user

**RAM user**

You are authorized to call the following API operations to manage the specified resource as a Resource Access Management (RAM) user: RenewInstance RenewMultiInstance TransformToPrePaid

#### 4.6.4 API authentication rules

When you use API operations to access resources as a Resource Access Management (RAM) user, the system queries the RAM service and checks whether the RAM user is granted the required permissions. Each API operation determines the resources for permission check according to the involved resources and the semantics of the API operation. The following table lists the authentication rules corresponding to different API operations.Table 1. Authentication rules

| Operation | Authentication rule |
|---|---|
| CreateDBInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DeleteInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceSpec | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RenewInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RenewMultiInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| TransformToPrePaid | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| FlushInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeInstances | acs:kvstore:$regionid:$accountid:instance/$insta nceid |

| DescribeInstanceAttribute | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
|---|---|
| ModifyInstanceMaintainTime | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifySecurityIps | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| SwitchNetwork | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceNetExpireTime | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| CreateBackup | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeBackupPolicy | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeBackups | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| RestoreInstance | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeHistoryMonitorValues | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| DescribeInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$insta nceid |
| ModifyInstanceConfig | acs:kvstore:$regionid:$accountid:instance/$insta nceid |

### 4.7 Manage the lifecycle

#### 4.7.1 DescribeZones

Queries the zones that support KVStore for Redis in a specific region.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| RegionId | Strin g | Domain | No | cn-huhehaote | The region ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 1D42F072-72FE- 4DC4-BB8E- 64B1D298**** | The request ID. |
| Zones | Array |   | The queried zones. |
| -RegionId | String | cn-huhehaote | The ID of the region. |
| -ZoneId | String | cn-huhehaote-b | The ID of a zone in the region. |
| -ZoneName | String | Hohhot Zone B | The name of a zone in the region. |
| - SwitchNetwork | Boolean | true | Indicates whether the network type of the instance can be changed from the classic network to Virtual Private Cloud (VPC). Valid values: true false |
| -IsRds | Boolean | true | Indicates whether the zone is managed by ApsaraDB RDS. The return value of this parameter is true in KVStore for Redis instances. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeZones &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"1D42F072-72FE-4DC4-BB8E-64B1D298****",
 "Zones":{
  "ZoneName":"Hohhot Zone B",
  "ZoneId":"cn-huhehaote-b",
  "SwitchNetwork":true,
  "RegionId":"cn-huhehaote",
  "IsRds":true
```

#### 4.7.2 CreateInstance

Creates a KVStore for Redis instance.

**Request parameters**

| Parameter | Type |   | Require d | Example |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| <Common request parameters> | N/A |   | Yes | N/A |   | For more information, see Common parameters. |   |   |   |   |
| Action | String |   | Yes | CreateInstanc e |   | The operation that you want to perform. Set this parameter to CreateInstance. |   |   |   |   |
| InstanceName | String |   | No | apitest |   | The name of the instance. The name must be 2 to 128 characters in length. The name must start with a letter. It cannot contain spaces or the following special characters: @ / : = " < > { [ ] } |   |   |   |   |
| Password | String |   | No | Pass!123456 |   | The password that is used to connect to the instance. The password must be 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Note Special characters are not supported, such as ! < > |   |   |   |   |
|   |   |   |   |   |   |   | Note Special characters are not supported, such as ! < > |   |   |   |
|   |   |   |   |   |   |   |   | ! < > |   |   |
|   |   |   |   |   |   |   | ( ) [ ] { } , ` ~ . - _ |   |   |   |
|   |   |   |   |   |   |   | @ # $ % ^ & * |   |   |   |
| InstanceClass | String |   | Yes | redis.master.s mall.default |   | The type of the KVStore for Redis instance. For more information, see Instance types. |   |   |   |   |
| RegionId | String |   | Yes | cn-hangzhou |   | The region ID of the instance. You can query available regions by calling the DescribeRegions operation. |   |   |   |   |
| ZoneId | String |   | No | cn-hangzhou-e |   | The zone ID of the instance. You can query available zones by calling the DescribeRegions operation. |   |   |   |   |
| Token | String |   | No | ChargeType |   | The client token that is used to ensure the idempotence of requests. The value of this parameter is generated by the client and must be unique among different requests. The value is case-sensitive and can be up to 64 ASCII characters in length. |   |   |   |   |

| @ / : = " |   |
|---|---|

|   | < > { [ ] } |
|---|---|

| NetworkType | String | No | VPC | The type of the network. Default value: Classic. Valid values: Classic VPC |
|---|---|---|---|---|
| VpcId | String | No | vpc- bp1nme44gek 34slfc**** | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | No | vsw- bp1e7clcw529l 773d**** | The ID of the vSwitch to which the instance belongs. Note This parameter is required if the VpcId parameter is specified. |
| PrivateIp | String | No | 172.16.0.*** | The private IP address of the instance. |
| SrcDBInstanceI d | String | No | r- bp1zxszhcgatn x**** | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the instance that generates the backup set. |
| BackupId | String | No | 111111111 | If an instance created based on a backup set generated by another instance is valid, specifies the ID of the generated backup set. You can query backup set IDs by calling the DescribeBackups operation. |
| InstanceType | String | No | Redis | The category of the instance. Valid values: Redis and Memcache. Default value: Redis. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| InstanceId | String | r-bp1zxszhcgatnx**** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceName | String | apitest | The name of the instance. |

> **Note:** Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields as needed in the future.

**Sample requests**

```
https://r-kvstore.example.com ?<Common request parameters> &Action=CreateInstance &RegionId=cn-hangzhou &Password=Pass!123456 &InstanceClass=redis.master.small.default
```

**Sample responses**

XML format

```xml
<CreateInstanceResponse>
    <InstanceId>r-n8r8c5119d2e****</InstanceId>
    <InstanceName>testdb</InstanceName>
</CreateInstanceResponse>
```

JSON format `{`

```json
"InstanceId":"r-n8r8c5119d2e****", "InstanceName":"testdb"
```

`}`

#### 4.7.3 DeleteInstance

Deletes a specified instance. The instance must be in the **running** state.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DeleteInstance | The operation that you want to perform. Set the value to DeleteInstance. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The globally unique identifier (GUID) of the KVStore for Redis instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.example.com &Action=DeleteInstance &InstanceId=r-n8r8c5119d2e**** &Common request parameters
```

**Sample responses**

XML format

```xml
<DeleteInstanceResponse>
      <RequestId>5D622714-AEDD-4609-9167-F5DDD3D190D2</RequestId>
</DeleteInstanceResponse>
```

JSON format `{`

```json
    "RequestId": "5D622714-AEDD-4609-9167-F5DDD3D190D2"
```

`}`

#### 4.7.4 ModifyInstanceSpec

Changes the specifications of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters > | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInsta nceSpec | The operation that you want to perform. Set this parameter to ModifyInstanceSpec. |
| InstanceId | String | Yes | r- bp1zxszhcg atnx**** | The ID of the instance. |
| InstanceClas s | String | Yes | redis.logic.s harding.drre dissdb1g.1d b.0rodb.4pr oxy.default | The type of the KVStore for Redis instance. For more information, see Instance types. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common request parameters> | N/A | N/A | For more information, see Common parameters. |
| OrderId | String | 20722623431**** | The ID of the order. |

**Sample requests**

```
https://r-kvstore.example.com &Action=ModifyInstanceSpec &InstanceId=r-n8r8c5119d2e**** &InstanceClass= redis.master.mid.default &<Common request parameters>
```

**Sample responses**

XML format

```xml
<ModifyInstanceSpecResponse>
      <RequestId>A4828C10-AF0A-4CD7-8FBE-737C6CC1193E</RequestId>
      <OrderId>20722623431****</OrderId>
</ModifyInstanceSpecResponse>
```

JSON format `{`

```json
    "RequestId": "A4828C10-AF0A-4CD7-8FBE-737C6CC1193E",
    "OrderId": "20722623431****"
```

`}`

### 4.8 Manage instances

#### 4.8.1 RestartInstance

Restarts a Redis instance that is running.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| Action | Strin g | Query | Yes | RestartInstance | The operation name. Set the value to RestartInstance. |
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |
| EffectiveTi me | Strin g | Query | No | Immediately | The time when you want to restart the instance. Default value: Immediately. Valid values: Immediately : immediately restarts the instance. MaintainTime : restarts the instance during the maintenance window. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | EFC9161F-15E3- 4A6E-8A99- C33331**** | The request ID. |
| InstanceId | String | r- bp1zxszhcgatnx*** * | The instance ID. |
| TaskId | String | 11111**** | The task ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=RestartInstance &Action= &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
 "TaskId":"11111****",
 "RequestId":"EFC9161F-15E3-4A6E-8A99-C33331****",
 "InstanceId":"r-bp1zxszhcgatnx****"
```

`}`

#### 4.8.2 FlushExpireKeys

Deletes the expired keys from a Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |
| EffectiveTi me | Strin g | Query | No | Immediately | The time when you want to delete the expired keys. Default value: Immediately. Valid values: Immediately : deletes the keys immediately. MaintainTime : deletes the keys during the maintenance window. You can call the ModifyInstanceMain tainTime operation to modify the maintenance window of a Redis instance. |
| Action | Strin g | Query | Yes | FlushExpireKeys | The operation name. Set the value to FlushExpireKeys. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TaskId | String | 21986**** | The task ID. |
| RequestId | String | 82E30AB7-E3A4- 46AC-88A0- 3E4DCDC5**** | The request ID. |
| InstanceId | String | r- bp1zxszhcgatnx*** * | The instance ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=FlushExpireKeys &InstanceId=r-bp1zxszhcgatnx**** &Action=FlushExpireKeys &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TaskId":"21986****",
 "RequestId":"82E30AB7-E3A4-46AC-88A0-3E4DCDC5****",
 "InstanceId":"r-bp1zxszhcgatnx****"
```

`}`

#### 4.8.3 DescribeLogicInstanceTopology

Queries the logical topology of a Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RedisShardList | Array |   | Details about data shards, including node information such as NodeInfo. |
| -NodeId | String | r- bp10noxlhcoim2** **-db-0#688**** | The node ID. |
| -Connection | String | 10000 | The maximum number of connections. |
| -Bandwidth | String | 96 | The maximum bandwidth of the node. Unit: Mbit/s. |
| -Capacity | String | 2048 | The storage capacity of the node. Unit: MB. |
| -NodeType | String | db | The type of the node. Valid values: proxy : proxy node db : data node |
| RequestId | String | 794120D1-E0CF- 4713-BAE4- EBAEA04506AF | The request ID. |
| InstanceId | String | r- bp1zxszhcgatnx*** * | The instance ID. |
| RedisProxyList | Array |   | Details about proxy nodes. |
| -NodeId | String | r- bp10noxlhcoim2** **-proxy- 3#542**** | The node ID. |
| -Connection | String | 320000 | The maximum number of connections. |
| -Bandwidth | String | 96 | The maximum bandwidth of the node. Unit: Mbit/s. |
| -Capacity | String | 5120 | The storage capacity of the node. Unit: MB. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| -NodeType | String | proxy | The type of the node. Valid values: db : a data node. normal : a management node, which can be a proxy node or a Configserver node. For specific instances, the return value of this parameter is proxy or cs, instead of normal. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogicInstanceTopology &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RedisShardList":{
  "Capacity":"2048",
  "Bandwidth":"96",
  "NodeType":"db",
  "NodeId":"r-bp10noxlhcoim2****-db-0#688****",
  "Connection":"10000"
```

`},`

```json
 "RequestId":"794120D1-E0CF-4713-BAE4-EBAEA04506AF",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "RedisProxyList":{
  "Capacity":"5120",
  "Bandwidth":"96",
  "NodeType":"proxy",
  "NodeId":"r-bp10noxlhcoim2****-proxy-3#542****",
  "Connection":"320000"
```

`}` `}`

#### 4.8.4 DescribeEngineVersion

Queries the major version and minor version of a Redis instance, including the release notes for the minor version.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. You can call the DescribeInstances operation to query instance IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| MajorVersion | String | 5.0 | The major version of the instance. |
| RequestId | String | A52974D1-9D57- 4805-86CC- 92E6EDE8**** | The request ID. |
| MinorVersion | String | redis-5.0 0.5.0 _ | The current minor version of the instance. |
| EnableUpgrad eMajorVersion | Boolean | true | Specifies whether the major version can be upgraded for the instance. Valid values: true : The major version can be upgraded. false : The major version is the latest version and cannot be upgraded. To upgrade the major version, call the ModifyInstanceMajorVersion operation. |
| IsLatestVersio n | Boolean | false | Specifies whether the instance minor version is the latest version. Valid values: true false |
| EnableUpgrad eMinorVersion | Boolean | true | Specifies whether the minor version can be updated for the instance. Valid values: true : The minor version can be updated. false : The minor version is the latest version and cannot be updated. To update the minor version, call the ModifyInstanceMinorVersion operation. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Engine | String | redis | The database engine. Valid values: redis and memcache . |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEngineVersion &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "MajorVersion":"5.0",
 "IsLatestVersion":false,
 "RequestId":"A52974D1-9D57-4805-86CC-92E6EDE8****",
 "MinorVersion":"redis-5.0_0.5.0",
 "EnableUpgradeMinorVersion":true,
 "Engine":"redis",
 "EnableUpgradeMajorVersion":true
```

`}`

#### 4.8.5 DescribeInstanceAttribute

Queries detailed information about a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeInstance Attribute | The operation that you want to perform. Set this parameter to DescribeInstance Attribute. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | List | N/A | An array that consists of the DBInstanceAttribute values. |

**Parameters of DBInstanceAttribute**

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | r-bp1d72gwl41z7f**** | The ID of the instance. |
| InstanceName | String | apitest | The name of the instance. |
| Capacity | Long | 1024 | The capacity of the instance. Unit: MB. |
| InstanceClass | String | redis.logic.sharding.drr edissdb1g.1db.0rodb.4 proxy.default | The type of the instance. |
| Bandwidth | Long | 10 | The bandwidth threshold of the instance. Unit: Mbit/s. |
| Connections | Long | 10000 | The maximum connections allowed to the instance. |
| ConnectionDomain | String | r- bp1d72gwl41z7f****.r edis.rds.aliyuncs.com | The endpoint of the instance. This endpoint only supports connections over an internal network. |
| Port | Int | 6379 | The port of the instance. |
| RegionId | String | cn-hangzhou | The region ID of the instance. For more information, see DescribeRegions. |
| ZoneId | String | cn-hangzhou-b | The zone ID of the instance. For more information, see DescribeRegions. |
| InstanceStatus | String | Normal | The status of the instance. Valid values: Normal Creating Changing Inactive |

| CreateTime | String | 2019-03- 06T10:42:03Z |   | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC. |   |   |
|---|---|---|---|---|---|---|
|   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   | DDThh:mm:ssZ |   |   |
| EndTime | String | 2019-04- 06T10:42:03Z |   | The time when the subscription instance expires. The time follows the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The time is displayed in UTC. |   |   |
| NetworkType | String | VPC |   | The network type of the instance. Valid values: Classic and VPC. |   |   |
| VpcId | String | vpc- bp1nme44gek34slfc** ** |   | The ID of the VPC to which the instance belongs. |   |   |
| VSwitchId | String | vsw- bp1e7clcw529l773d*** * |   | The ID of the vSwitch to which the instance belongs. |   |   |
| MaintainStartTime | String | 18:00Z |   | The start time of the maintenance window. |   |   |
| MaintainEndTime | String | 22:00Z |   | The end time of the maintenance window. |   |   |
| SecurityIPList | String | 127.0.0.1 |   | The IP whitelist. |   |   |
| AvailabilityValue | String | 100% |   | The availability metric of the current month. |   |   |

|   |   | YYYY-MM- |   |
|---|---|---|---|
|   | DDThh:mm:ssZ |   |   |

> **Note:** Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config and Region for the operation. Alibaba Cloud will delete these fields in the future.

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceAttribute &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

**Sample responses**

XML format

```xml
<DescribeInstanceAttributeResponse>
```

```xml
      <Instances>
            <DBInstanceAttribute>
                  <Connections>10000</Connections>
                  <ResourceGroupId>rg-acfmyiu4ekp****</ResourceGroupId>
                  <Config>{"EvictionPolicy":"volatile-lru","hash-max-ziplist-entries":51
2,"zset-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-value ":64,"zset-max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value": 64}</Config>
                  <Port>6379</Port>
                  <HasRenewChangeOrder>false</HasRenewChangeOrder>
                  <ZoneType>singlezone</ZoneType>
                  <ConnectionDomain>r-
bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com</ConnectionDomain>
                  <MaintainEndTime>22:00Z</MaintainEndTime>
                  <Capacity>1024</Capacity>
                  <QPS>100000</QPS>
                  <PrivateIp>172.16.49.***</PrivateIp>
                  <SecurityIPList>127.0.0.1</SecurityIPList>
                  <InstanceStatus>Normal</InstanceStatus>
                  <NetworkType>VPC</NetworkType>
                  <Bandwidth>10</Bandwidth>
                  <PackageType>standard</PackageType>
                  <InstanceReleaseProtection>false</InstanceReleaseProtection>
                  <InstanceType>Redis</InstanceType>
                  <AvailabilityValue>100.0%</AvailabilityValue>
                  <Engine>Redis</Engine>
                  <MaintainStartTime>18:00Z</MaintainStartTime>
                  <Tags>
                        <Tag>
                              <Value>Community Edition</Value>
                              <Key>Type</Key>
                        </Tag>
                  </Tags>
                  <ArchitectureType>standard</ArchitectureType>
                  <EngineVersion>5.0</EngineVersion>
                  <ZoneId>cn-hangzhou-f</ZoneId>
                  <InstanceId>r-bp1wcw2rlw76ac****</InstanceId>
                  <VSwitchId>vsw-bp1w9ouei2nm66qlz****</VSwitchId>
                  <CreateTime>2020-03-31T14:56:22Z</CreateTime>
<InstanceClass>redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default</InstanceClass>
                  <AuditLogRetention>7</AuditLogRetention>
                  <IsRds>true</IsRds>
                  <ReplicationMode>master-slave</ReplicationMode>
                  <InstanceName>CommunityEditionMasterReplica50</InstanceName>
                  <VpcId>vpc-bp1opxu1zkhn00gzv****</VpcId>
                  <ChargeType>PostPaid</ChargeType>
                  <VpcAuthMode>Open</VpcAuthMode>
                  <NodeType>double</NodeType>
                  <VpcCloudInstanceId>r-bp1wcw2rlw76ac****</VpcCloudInstanceId>
                  <RegionId>cn-hangzhou</RegionId>
            </DBInstanceAttribute>
      </Instances>
<ReqestId>D67A69DFC1FC4B01B239B17888CCFD2A</ReqestId>
```

```xml
      <RequestId>D67A69DF-C1FC-4B01-B239-B17888CCFD2A</RequestId>
</DescribeInstanceAttributeResponse>
```

JSON format `{`

```json
 "Instances": {
  "DBInstanceAttribute": [
```

`{`

```json
    "Connections": 10000,
    "ResourceGroupId": "rg-acfmyiu4ekp****",
    "Config": "{\"EvictionPolicy\":\"volatile-lru\",\"hash-max-ziplist-
entries\":512,\"zset-max-ziplist-entries\":128,\"list-max-ziplist-entries\":512,\"listmax-ziplist-value\":64,\"zset-max-ziplist-value\":64,\"set-max-intsetentries\":512,\"hash-max-ziplist-value\":64}",
    "Port": 6379,
    "HasRenewChangeOrder": "false",
                "ZoneType":"singlezone",
    "ConnectionDomain": "r-bp1wcw2rlw76acc5k****.redis.rds.aliyuncs.com",
    "MaintainEndTime": "22:00Z",
    "Capacity": 1024,
    "QPS": 100000,
    "PrivateIp": "172.16.49.***",
    "SecurityIPList": "127.0.0.1",
    "InstanceStatus": "Normal",
    "NetworkType": "VPC",
    "Bandwidth": 10,
    "PackageType": "standard",
    "InstanceReleaseProtection": false,
    "InstanceType": "Redis",
    "AvailabilityValue": "100.0%",
    "Engine": "Redis",
    "MaintainStartTime": "18:00Z",
    "Tags": {
     "Tag": [
```

`{`

```json
       "Value": "Community Edition",
       "Key": "Type"
```

`}` `]` `},`

```json
    "ArchitectureType": "standard",
    "EngineVersion": "5.0",
    "ZoneId": "cn-hangzhou-f",
    "InstanceId": "r-bp1wcw2rlw76ac****",
    "VSwitchId": "vsw-bp1w9ouei2nm66qlz****",
    "CreateTime": "2020-03-31T14:56:22Z",
    "InstanceClass": "redis.logic.sharding.drredissdb1g.1db.0rodb.4proxy.default",
    "AuditLogRetention": "7",
    "IsRds": true,
    "ReplicationMode": "master-slave",
    "InstanceName": "CommunityEditionMasterReplica50",
    "VpcId": "vpc-bp1opxu1zkhn00gzv****",
    "ChargeType": "PostPaid",
```

```json
    "VpcAuthMode": "Open",
    "NodeType": "double",
    "VpcCloudInstanceId": "r-bp1wcw2rlw76ac****",
    "RegionId": "cn-hangzhou"
```

`}` `]` `},`

```json
 "RequestId": "D67A69DF-C1FC-4B01-B239-B17888CCFD2A"
```

`}`

#### 4.8.6 DescribeInstances

Queries information about one or more KVStore for Redis instances.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters > | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeIns tances | The operation that you want to perform. Set this parameter to DescribeInstances. |
| InstanceIds | String | No | r- n8r8c5119d 2e**** | The globally unique identifier (GUID) of the KVStore for Redis instance. Note If you specify multiple instance IDs, separate the instance IDs with commas (,). If the parameter value is left blank, all instances that belong to the specified account are displayed by default. |
| InstanceSta tus | String | No | Normal | Specifies the status of the instances to be returned. Valid values: Normal Creating Changing Inactive |
| RegionId | String | Yes | cn- hangzhou | The region ID of the instance. You can call DescribeRegions to query the latest region list. |

| InstanceTyp e | String | No | Redis | Specifies the engine type of the instances to be returned. Valid values: Memcache Redis |
|---|---|---|---|---|
| PageNumbe r | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 1 to 50. Default value: 10. |
| NetworkTyp e | String | No | VPC | Specifies the network type of the instances to be returned. Valid values: Classic VPC |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| Instances | List | N/A | Details about instances. For more information, see Parameters of an instance. |
| TotalCount | Integer | 1 | The total number of instances. |
| PageNumber | Integer | 1 | The number of the returned page. |
| PageSize | Integer | 10 | The number of entries per page. |

**Parameters of an instance**

| Parameter | Type | Example | Description |
|---|---|---|---|
| InstanceId | String | r- n8r8c5119d2e **** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceName | String | testdb | The name of the instance. |
| Capacity | Long | 512 | The capacity of the instance. Unit: MB. |
| InstanceClass | String | redis.master. mid.default | The type of the instance. |

| Bandwidth | Long | 128 | The bandwidth threshold of the instance. Unit: Mbit/s. |
|---|---|---|---|
| Connections | Long | 300 | The maximum connections allowed to the instance. |
| ConnectionDo main | String | de5d88e34d0 0****.m.cnhzal icm10pub001. r- kvstore.examp le.com | The endpoint of the instance. This endpoint only supports connections over an internal network. |
| Port | Int | 11211 | The port of the instance. |
| UserName | String | testuser | The account for the instance. |
| RegionId | String | cn-qingdao | The region ID of the instance. |
| ZoneId | String | cn-qingdao-b | The zone ID of the instance. |
| InstanceStatus | String | Normal | The status of the instance. Valid values: Normal Creating Changing Inactive Transforming BackupRecovering MinorVersionUpgrading |
| ChargeType | String | PostPaid | The billing method of the instance. Valid values: PrePaid and PostPaid. |
| CreateTime | String | 2019-03- 06T10:42:03Z | The time when the instance was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| EndTime | String | 2019-04- 06T10:42:03Z | The time when the subscription instance expires. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC. |
| NetworkType | String | VPC | The network type of the instance. Valid values: Classic and VPC. |
| VpcId | String | vpc- bp1nme44gek 34slfc**** | The ID of the VPC to which the instance belongs. |
| VSwitchId | String | vsw- bp1e7clcw529l 773d**** | The ID of the vSwitch to which the instance belongs. |
| PrivateIpAddr | String | 172.16.**.*** | The private IP address of the instance. |

> **Note:** Due to the compatibility with earlier versions, this topic does not describe some returned fields such as Config for the operation. Alibaba Cloud will delete these fields in the future.

**Sample requests**

```
https://r-kvstore.example.com ?<Common request parameters> &Action=DescribeInstances &PageNumber=1 &PageSize=10 &InstanceId=r-n8r8c5119d2e****
```

**Sample responses**

XML format

```xml
<DescribeInstancesResponse>
    <Instances>
        <Instance>
            <Bandwidth>128</Bandwidth>
            <Capacity>512</Capacity>
            <ConnectionDomain>de5d88e34d00****.m.cnhzalicm10pub001.r-
kvstore.example.com</ConnectionDomain>
            <Connections>300</Connections>
            <ZoneId>cn-qingdao-b</ZoneId>
            <InstanceId>r-n8r8c5119d2e****</InstanceId>
            <InstanceName>testdb</InstanceName>
            <InstanceStatus>Available</InstanceStatus>
            <InstanceClass>redis.master.mid.default</InstanceClass>
            <Port>11211</Port>
            <RegionId>cn-qingdao</RegionId>
            <UserName>testuser</UserName>
            <NetworkType>CLASSSIC</NetworkType>
            <ChargeType> PostPaid</ChargeType>
        </Instance>
    </Instances>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
    <TotalCount>1</TotalCount>
    <RequestId>969D0A1D-C91A-4837-9F70-49785DF9BDCE</RequestId>
</DescribeInstancesResponse>
```

JSON format

```json
    "Instances" : {
        "Instance" : [{
                "Bandwidth" : 128,
                "Capacity" : 512,
                "ConnectionDomain" : "de5d88e34d00****.m.cnhzalicm10pub001.r-kvstore.exa
mple.com",
                "Connections" : 300,
                "ZoneId" : "cn-qingdao-b",
                "InstanceId" : "r-n8r8c5119d2e****",
                "InstanceName" : "testdb",
                "InstanceStatus" : "Available",
                 "InstanceClass" : "redis.master.mid.default",
                "Port" : 11211,
                "RegionId" : "cn-qingdao",
                "UserName" : "testuser"
                "NetworkType":"CLASSSIC"
"ChargeType":" PostPaid"
```

`}` `]` `},`

```json
    "PageNumber" : 1,
    "PageSize" : 10,
    "TotalCount" : 1,
    "RequestId" : "969D0A1D-C91A-4837-9F70-49785DF9BDCE"
```

`}`

#### 4.8.7 DescribeRegions

Queries the regions where KVStore for Redis instances can be created.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set this parameter to DescribeRegions. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

| RegionIds | List | N/A | The list in which each element contains RegionId and ZoneIds. The value of the ZoneIds parameter is a string in which multiple ZoneIds are separated by commas (,). |
|---|---|---|---|

**Sample requests**

```
https://r-kvstore.aliyuncs.com?Action=DescribeRegions &Common request parameters
```

**Sample responses**

XML format

```xml
<DescribeRegionsResponse>
      <RegionIds>
            <KVStoreRegion>
              <RegionId>cn-hangzhou</RegionId>
              <ZoneIdList>
                    <ZoneId>cn-hangzhou-h</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ10(h,i)</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ9(g,h)</ZoneId>
                    <ZoneId>cn-hangzhou-b</ZoneId>
                    <ZoneId>cn-hangzhou-d</ZoneId>
                    <ZoneId>cn-hangzhou-e</ZoneId>
                    <ZoneId>cn-hangzhou-MAZ6(b,f)</ZoneId>
                    <ZoneId>cn-hangzhou-f</ZoneId>
                    <ZoneId>cn-hangzhou-g</ZoneId>
              </ZoneIdList>
              <RegionEndpoint>r-kvstore.aliyuncs.com</RegionEndpoint>
              <ZoneIds>cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),cn-
hangzhou-b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzhoug</ZoneIds>
              <LocalName>China (Hangzhou)</LocalName>
            </KVStoreRegion>
      </RegionIds>
      <RequestId>AD425AD3-CC7B-4EE2-A5CB-2F61BA73****</RequestId>
</DescribeRegionsResponse>
```

JSON format

```json
    "RegionIds": {
        "KVStoreRegion": [{
                "RegionId": "cn-hangzhou",
                "ZoneIdList": {
                    "ZoneId": [
                        "cn-hangzhou-h",
                        "cn-hangzhou-MAZ10(h,i)",
                        "cn-hangzhou-MAZ9(g,h)",
                        "cn-hangzhou-b",
                        "cn-hangzhou-d",
                        "cn-hangzhou-e",
                        "cn-hangzhou-MAZ6(b,f)",
                        "cn-hangzhou-f",
                        "cn-hangzhou-g"
```

`]` `},`

```json
                "RegionEndpoint": "r-kvstore.aliyuncs.com",
                "ZoneIds": "cn-hangzhou-h,cn-hangzhou-MAZ10(h,i),cn-hangzhou-MAZ9(g,h),c
n-hangzhou-b,cn-hangzhou-d,cn-hangzhou-e,cn-hangzhou-MAZ6(b,f),cn-hangzhou-f,cn-hangzho u-g",
                "LocalName": "China (Hangzhou)"
```

`}` `]` `},`

```json
    "RequestId": "AD425AD3-CC7B-4EE2-A5CB-2F61BA73****"
```

`}`

#### 4.8.8 DescribeSecurityIps

Queries IP whitelists of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeSecurityI ps | The operation that you want to perform. Set this parameter to DescribeSecurityI ps. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| SecurityIpGroups | List | N/A | Details about IP whitelists. |

**Parameters of SecurityIpGroups**

| Parameter | Type | Example |   | Description |   |   |
|---|---|---|---|---|---|---|
| SecurityIpGroupName | String | default |   | The name of the IP whitelist. |   |   |
| SecurityIpList | String | 100.100.202.***/24,10 .10.10.*** |   | The IP addresses in the IP whitelist. A maximum of 1,000 IP addresses or CIDR blocks are allowed. IP addresses are separated with commas (,). Supported formats are IP addresses such as 0.0.0.0/0 and 10.23.12.24 , or CIDR blocks such as 10.23.12.24/24 . /24 indicates the length of the IP address prefix. The IP address prefix can consist of 1 to 32 bits. |   |   |
|   |   |   |   |   | 0.0.0.0/0 and |   |
|   |   |   |   | 10.23.12.24 |   |   |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeSecurityIps &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeSecurityIpsResponse>
      <SecurityIpGroups>
            <SecurityIpGroup>
                  <SecurityIpList>127.0.0.1</SecurityIpList>
                  <SecurityIpGroupAttribute></SecurityIpGroupAttribute>
                  <SecurityIpGroupName>default</SecurityIpGroupName>
            </SecurityIpGroup>
            <SecurityIpGroup>
                  <SecurityIpList>100.100.202.***/24,10.10.10.***</SecurityIpList>
                  <SecurityIpGroupAttribute>hidden</SecurityIpGroupAttribute>
                  <SecurityIpGroupName>rds_replica_group</SecurityIpGroupName>
            </SecurityIpGroup>
      </SecurityIpGroups>
      <RequestId>EFC9161F-15E3-4A6E-8A99-C09916D1****</RequestId>
</DescribeSecurityIpsResponse>
```

JSON format `{`

```json
    "SecurityIpGroups": {
        "SecurityIpGroup": [
```

`{`

```json
                "SecurityIpList": "127.0.0.1",
                "SecurityIpGroupAttribute": "",
                "SecurityIpGroupName": "default"
```

`},` `{`

```json
                "SecurityIpList": "100.100.202.***/24,10.10.10.***",
                "SecurityIpGroupAttribute": "hidden",
                "SecurityIpGroupName": "rds_replica_group"
```

`}` `]` `},`

```json
    "RequestId": "EFC9161F-15E3-4A6E-8A99-C09916D1****"
```

`}`

#### 4.8.9 FlushInstance

Deletes the data of a KVStore for Redis instance. Deleted data cannot be recovered.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |

| Action | String | Yes | FlushInstance | The operation that you want to perform. Set this parameter to FlushInstance. |
|---|---|---|---|---|
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The globally unique identifier (GUID) of the KVStore for Redis instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=FlushInstance &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

**Sample responses**

XML format

```xml
<FlushInstanceResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
</FlushInstanceResponse>
```

JSON format `{`

```json
  "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E7"
```

`}`

#### 4.8.10 ModifyInstanceAttribute

Modifies the attributes of a KVStore for Redis instance such as the name or password.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |

| Action | String | Yes | ModifyInstanc eAttribute | The operation that you want to perform. Set this parameter to ModifyInstanceAttribute. |
|---|---|---|---|---|
| InstanceId | String | Yes | r- bp1zxszhcgat nx**** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| InstanceNam e | String | No | TestInstance | The new name of the instance. The name must be 2 to 128 characters in length. The name must start with a letter. It cannot contain spaces or the following special characters: @ / : = " < > { [ ] } |
| NewPassword | String | No | Qa12345678 | The new password of the instance. The password must be 8 to 30 characters in length and must contain uppercase letters, lowercase letters, and digits. Note Special characters are not supported, such as ! < > ( ) [ ] { } , ` ~ . - @ # $ % _ ^ & * |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.example.com &Action=ModifyInstanceAttribute &InstanceId=r-bp1zxszhcgatnx**** &NewPassword=Qa12345678 &InstanceName=TestInstance &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifyInstanceAttributeResponse>
    <RequestId>E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59</RequestId>
</ModifyInstanceAttributeResponse>
```

JSON format

```json
"RequestId" : "E3B35BEA-9EB0-402C-88CF-C46CCCC1EE59"
```

#### 4.8.11 ModifyInstanceMaintainTime

Modifies the maintenance window of a KVStore for Redis instance. Alibaba Cloud maintains the KVStore for Redis instance in the specified maintenance window.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceM aintainTime | The operation that you want to perform. Set this parameter to ModifyInstanceM aintainTime. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |
| MaintainStartTim e | String | Yes | 03:00Z | The start time of the maintenance window. |
| MaintainEndTime | String | Yes | 04:00Z | The end time of the maintenance window. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceMaintainTime &InstanceId=r-bp1zxszhcgatnx**** &MaintainStartTime=17:00Z &MaintainEndTime=18:00Z &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifyInstanceMaintainTimeResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76</RequestId>
</ModifyInstanceMaintainTimeResponse>
```

JSON format `{`

```json
    "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B3E76"
```

`}`

#### 4.8.12 ModifyInstanceNetExpireTime

Extends the retention period of the classic network endpoint of a KVStore for Redis instance. You can call this operation after you change the network type of the KVStore for Redis instance from classic network to VPC with the classic network endpoint retained.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceN etExpireTime | The operation that you want to perform. Set this parameter to ModifyInstanceN etExpireTime. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |
| ConnectionString | String | Yes | r- bp1zxszhcgatnx* ***.redis.rds.aliyu ncs.com | The endpoint of the classic network. |
| ClassicExpiredDa ys | String | Yes | 14 | The number of the days when the classic network IP is retained. Valid values: 14, 30, 60, and 120. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceNetExpireTime &ClassicExpiredDays=14 &ConnectionString=r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com &InstanceId=r-bp1zxszhcgatnx**** &Common request parameters
```

**Sample responses**

XML format

```xml
<ModifyInstanceNetExpireTimeResponse>
      <RequestId>9C4AF387-1EA3-4C84-8013-3F6B973EDDF5</RequestId>
</ModifyInstanceNetExpireTimeResponse>
```

JSON format `{`

```json
    "RequestId": "9C4AF387-1EA3-4C84-8013-3F6B973EDDF5",
```

`}`

#### 4.8.13 ModifySecurityIps

Modifies the IP addresses in a whitelist of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifySecurityIps | The operation that you want to perform. Set this parameter to ModifySecurityIps . |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The globally unique identifier (GUID) of the KVStore for Redis instance. |
| SecurityIps | String | Yes | 100.64.***.0/24,1 0.101.11.*** | The IP addresses to be modified. |
| SecurityIpGroupN ame | String | Yes | default | The name of the IP whitelist. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=ModifySecurityIps &InstanceId=r-bp1zxszhcgatnx**** &SecurityIps=100.64.***.0/24,10.101.11.*** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<ModifySecurityIpsResponse>
      <RequestId>AAAF99B1-69ED-4E80-8CD5-272C09E4****</RequestId>
</ModifySecurityIpsResponse>
```

JSON format `{`

```json
    "RequestId" : "AAAF99B1-69ED-4E80-8CD5-272C09E4****"
```

`}`

#### 4.8.14 SwitchNetwork

Changes the network type of a KVStore for Redis instance from classic network to VPC.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | SwitchNetwork | The operation that you want to perform. Set this parameter to SwitchNetwork. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

| TargetNetworkTy pe | String | Yes | VPC | The type of the network that you want to switch to. VPC Classic You can only switch from classic network to VPC. In this case, this parameter must be set to VPC. |
|---|---|---|---|---|
| VpcId | String | No | vpc- bp1nme44gek34 slfc**** | The ID of the VPC that you want to switch to. |
| VSwitchId | String | No | vsw- bp1e7clcw529l77 3d**** | The ID of the vSwitch in the VPC that you want to switch to. This parameter is required if the ID of the VPC is specified. |
| RetainClassic | String | No | True | Specifies whether to retain the classic network IP address. Default value: False. Valid values: True: The classic network IP address is retained. False: The classic network IP address is not retained. |
| ClassicExpiredDa ys | String | No | 30 | The number of the days when the classic network IP is retained. Unit: days. Valid values: 14, 30, 60, and 120. If you set the RetainClassic parameter to true, you must also specify this parameter. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com?Action=SwitchNetwork &InstanceId=r-bp1zxszhcgatnx**** &TargetNetworkType=VPC &VpcId=vpc-bp1nme44gek34slfc**** &VSwitchId=vsw-bp1e7clcw529l773d**** &RetainClassic=True &ClassicExpiredDays=30 &<Common request parameters>
```

**Sample responses**

XML format

```xml
<SwitchNetworkResponse>
      <TaskId>578678678</TaskId>
      <requestId>F0997EE8-F4C2-4503-9168-85177ED78C70</requestId>
</SwitchNetworkResponse>
```

JSON format `{`

```json
    "TaskId":"578678678",
    "requestId": "F0997EE8-F4C2-4503-9168-85177ED78C70"
```

`}`

### 4.9 Data encryption

#### 4.9.1 DescribeEncryptionKey

Queries the detailed information about a custom key used for transparent data encryption (TDE) in a KVStore for Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. You can call the DescribeInstances operation to query instance IDs. |
| Encryptio nKey | Strin g | Query | No | ad463061-992d-4195- 8a94-ed63******** | The ID of the custom key. You can call the DescribeEncryptionKeyLi st operation to query key IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Origin | String | Aliyun KMS _ | The source of the custom key. A value of Aliyun KMS indicates Key _ Management Service (KMS) of Alibaba Cloud. |
| Description | String | testkey | The description of the custom key. This parameter is empty by default. |
| RequestId | String | 9A931CE5-C926- 5E09-B0EC- 6299C4A6**** | The request ID. |
| EncryptionKey Status | String | Enabled | The status of the custom key. Valid values: Enabled : The custom key is available. Disabled : The custom key is unavailable. |
| MaterialExpire Time | String | 2021-09- 24T18:22:03Z | The time when the custom key expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC. If the return value is an empty string, the custom key does not expire. |
| KeyUsage | String | ENCRYPT/DECRYPT | The purpose of the custom key. A value of ENCRYPT/DECRYPT indicates encryption and decryption. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| EncryptionKey | String | ad463061-992d- 4195-8a94- ed63******** | The ID of the custom key. |
| Creator | String | 17649847******** | The ID of the Alibaba Cloud account that is used to create the custom key. |
| DeleteDate | String | 2021-09- 24T18:22:03Z | The time when the custom key is expected to be deleted. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. If the return value is an empty string, the custom key cannot be automatically deleted. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEncryptionKey &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "Origin":"Aliyun_KMS",
 "Description":"testkey",
 "RequestId":"9A931CE5-C926-5E09-B0EC-6299C4A6****",
 "EncryptionKeyStatus":"Enabled",
 "MaterialExpireTime":"2021-09-24T18:22:03Z",
 "KeyUsage":"ENCRYPT/DECRYPT",
 "EncryptionKey":"ad463061-992d-4195-8a94-ed63********",
 "Creator":"17649847********",
 "DeleteDate":"2021-09-24T18:22:03Z"
```

`}`

#### 4.9.2 DescribeInstanceTDEStatus

Queries whether transparent data encryption (TDE) is enabled for a KVStore for Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. You can call the DescribeInstances operation to query instance IDs. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| TDEStatus | String | Enabled | Indicates whether TDE is enabled. Valid values: Enabled Disabled |
| RequestId | String | 5D622714-AEDD- 4609-9167- F5DDD3D1**** | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceTDEStatus &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "TDEStatus":"Enabled",
 "RequestId":"5D622714-AEDD-4609-9167-F5DDD3D1****"
```

`}`

#### 4.9.3 CheckCloudResourceAuthorized

Queries whether a KVStore for Redis instance is authorized to use Key Management Service (KMS).

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. You can call the DescribeInstances operation to query instance IDs. |
| RoleArn | Strin g | Query | No | acs:ram::123456789012 ****:role/AliyunRdsInsta nceEncryptionDefaultRol e | The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role that you want to attach to the instance. The ARN must be in the format of acs:ram::$accountID: role/$roleName . After the role is attached, the instance can use KMS. $accountID : the ID of the Alibaba Cloud account. To view the account ID, log on to the Alibaba Cloud Management Console, move the pointer over your profile picture in the upper-right corner of the page, and then select Security Settings . $roleName : the name of the RAM role. Set the value to AliyunRdsInsta nceEncryption DefaultRole . |

|   |   | acs:ram::$accountID: |
|---|---|---|
|   | role/$roleName |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AuthorizationS tate | Integer | 1 | Indicates whether the instance is authorized to use KMS. Valid values: 0 : The instance is authorized to use KMS. 1 : The instance is not authorized to use KMS. 2 : KMS is not activated. For more information, see Activate KMS. |
| RequestId | String | A501A191-BD70- 5E50-98A9- C2A486A82**** | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CheckCloudResourceAuthorized &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "AuthorizationState":1,
 "RequestId":"A501A191-BD70-5E50-98A9-C2A486A82****"
```

`}`

### 4.10 Account management

#### 4.10.1 DescribeUserInfo

Queries user information.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 3A40BE4E-1890- 4972-889C- FEFA376XXX | The request ID. |

|   | Developer Guide·A | PI reference |   | ApsaraDB for Redi | s |
|---|---|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| IsAuthenticatio n | Boolean | true | Indicates whether authentication is enabled. |
| IsFinance | Boolean | false | Indicates whether the queried user is a financial customer. |
| BalanceAmoun t | Long | 0 | The balance. |
| AlreadyHasRe sourceNum | Struct |   | The number of existing resources. |
| -EcsBought | Long | 22 | The number of resources purchased from Elastic Compute Service (ECS). |
| -KVSBought | Long | 29 | The number of resources purchased from KVS. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeUserInfo
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "BalanceAmount":0,
 "RequestId":"3A40BE4E-1890-4972-889C-FEFA376XXX",
 "IsAuthentication":true,
 "IsFinance":false,
 "AlreadyHasResourceNum":{
  "EcsBought":22,
  "KVSBought":29
```

`}` `}`

#### 4.10.2 CreateAccount

Creates an account that has specific permissions in a KVStore for Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |
| AccountN ame | Strin g | Query | Yes | demoaccount | The username of the account. The username must meet the following requirements: The username can contain lowercase letters, digits, and hyphens (-), and must start with a lowercase letter. The username can be up to 100 characters in length. The username cannot be one of the reserved words listed in the Reserved words for Redis account names section. |
| AccountPr ivilege | Strin g | Query | No | RoleReadOnly | The permissions of the account. Valid values: RoleReadOnly : The account has read- only permissions. RoleReadWrite (default): The account has read and write permissions. |
| AccountPa ssword | Strin g | Query | Yes | uWonno21**** | The password of the account. The password must be 8 to 32 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and specific special characters. These special characters include ! @ # $ % ^ & * ( ) + - = _ |

|   |   | ! @ # $ % ^ |
|---|---|---|
|   | & * ( ) + - = _ |   |

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| AccountD escription | Strin g | Query | No | testaccount | The description of the account. The description must start with a letter, and cannot start with http:// or https:// . The description can contain letters, digits, underscores ( ), and _ hyphens (-). The description must be 2 to 256 characters in length |
| AccountTy pe | Strin g | Query | No | Normal | The type of the account. Set the value to Normal . |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ABAF95F6-35C1- 4177-AF3A- 70969EBD**** | The request ID. |
| InstanceId | String | r- bp1zxszhcgatnx*** * | The instance ID. |
| AcountName | String | demoaccount | The account username. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateAccount &InstanceId=r-bp1zxszhcgatnx**** &AccountName=demoaccount &AccountPassword=uWonno21**** &<Common request parameters>
```

Sample success responses `JSON` format

```json
HTTP/1.1 200 OK Content-Type:application/json
 "RequestId":"ABAF95F6-35C1-4177-AF3A-70969EBD****",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "AcountName":"demoaccount"
```

`}`

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidAccountNam e.Duplicate | InvalidAccountName.Duplicate | Specified AccountName already exists in this instance. |
| 400 | InvalidAccountNam e.Format | InvalidAccountName.Format | Specified AccountName is not valid. |
| 400 | IncorrectEngineVer sion | InvalidEngineVersion.Format | Current EngineVersion does not support operations. |
| 400 | InvalidAccountDesc ription.Format | InvalidAccountDescription.For mat | Specified AccountDescription is not valid. |
| 400 | InvalidAccountPass word.Format | InvalidAccountPassword.Forma t | Specified AccountPassword is not valid. |
| 400 | IncorrectDBInstanc eAccountMode | InvalidDBInstanceAccountMod e.Format | Current DB instance AccountMode does not support this operation. |
| 400 | InvalidAccountNam e.Forbid | InvalidAccountName.Forbid | Specified AccountName is a keyword. |
| 403 | AccountLimitExcee ded | AccountLimitExceeded | Exceeding the allowed amount of account. |

### 4.11 Network security

#### 4.11.1 DescribeInstanceSSL

Queries whether TLS (SSL) encryption is enabled for a KVStore for Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| SSLExpiredTim e | String | 2020-08- 05T09:05:53Z | The time when the CA certificate expires. |
| RequestId | String | 02260F96-913E- 4655-9BA5- A3651CAF**** | The request ID. |
| SSLEnabled | String | Enable | The status of the TLS (SSL) encryption feature. Valid values: Enable : TLS (SSL) encryption is enabled. Disable : TLS (SSL) encryption is disabled. |
| InstanceId | String | r- bp1zxszhcgatnx*** * | The instance ID. |
| CertCommonN ame | String | r- bp1zxszhcgatnx*** *.redis.rds.aliyuncs .com | The common name of the CA certificate. The default value is the internal endpoint of the instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceSSL &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "SSLExpiredTime":"2020-08-05T09:05:53Z",
 "RequestId":"02260F96-913E-4655-9BA5-A3651CAF****",
 "SSLEnabled":"Enable",
 "InstanceId":"r-bp1zxszhcgatnx****",
 "CertCommonName":"r-bp1zxszhcgatnx****.redis.rds.aliyuncs.com"
```

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 403 | IncorrectCharacter Type | IncorrectCharacterType | Current DB instance CharacterType does not support this operation. |
| 403 | IncorrectEngineVer sion | IncorrectEngineVersion | Current engine version does not support operations. |

### 4.12 Connection management

#### 4.12.1 DescribeIntranetAttribute

Queries the internal bandwidth of a KVStore for Redis instance. If you have purchased extra internal bandwidth, the expiration time of the purchased bandwidth is also returned.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| IntranetBandw idth | Integer | 102 | The internal bandwidth of the instance. Unit: Mbit/s. |
| RequestId | String | 25D42CC3-FBA1- 4AEC-BCE2- B8DD3137**** | The request ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExpireTime | String | 0 | The time when the extra internal bandwidth that you purchased for temporary use expires. The time follows the ISO 8601 standard in the yyyy-MM- ddTHH:mm:ssZ format. The time is displayed in UTC. If no internal bandwidth for temporary use is purchased or the internal bandwidth that you purchased for temporary use has expired, a value of 0 is returned for this parameter. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeIntranetAttribute &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "IntranetBandwidth":102,
 "RequestId":"25D42CC3-FBA1-4AEC-BCE2-B8DD3137****",
 "ExpireTime":"0"
```

`}`

#### 4.12.2 ModifyInstanceVpcAuthMode

Enables or disables password-free access over Virtual Private Cloud (VPC) for a KVStore for Redis instance. Password-free access allows you to connect to databases more conveniently while ensuring security.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes | r-bp1zxszhcgatnx**** | The instance ID. |

| psaraDB for | Redis |   |   | Dev | eloper Guide·API referenc |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Example | Description |
|---|---|---|---|---|---|
| VpcAuthM ode | Strin g | Query | Yes | Close | Specifies whether to enable password-free access. Valid values: Open : disables password-free access. Close : enables password-free access. The default value is Open . |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ABAF95F6-35C1- 4177-AF3A- 70969EBD**** | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifyInstanceVpcAuthMode &InstanceId=r-bp1zxszhcgatnx**** &VpcAuthMode=Close &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"ABAF95F6-35C1-4177-AF3A-70969EBD****"
```

`}`

#### 4.12.3 AllocateInstancePublicConnection

Applies for a public endpoint for a KVStore for Redis instance.

**Request headers**

This operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common request parameters" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d |   | Example |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| InstanceId | Strin g | Query | Yes |   | r-bp1zxszhcgatnx**** |   | The instance ID. |   |   |   |
| Connectio nStringPre fix | Strin g | Query | Yes |   | r-bp1zxszhcgatnx**** |   | The prefix of the public endpoint. The prefix must be 8 to 40 characters in length and can contain lowercase letters and digits. It must start with a lowercase letter. Specify the endpoint in the <prefix>.redis. rds.aliyuncs.com format. |   |   |   |
|   |   |   |   |   |   |   |   |   | <prefix>.redis. |   |
|   |   |   |   |   |   |   |   | rds.aliyuncs.com |   |   |
| Port | Strin g | Query | Yes |   | 6379 |   | The port number of the instance. Valid values: 1024 to 65535 . |   |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 20C8341E-B5AD- 4B24-BD82- D73241522ABF | The request ID. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=AllocateInstancePublicConnection &InstanceId=r-bp1zxszhcgatnx**** &ConnectionStringPrefix=r-bp1zxszhcgatnx**** &Port=6379 &<Common request parameters>
```

Sample success responses `JSON` format

```
HTTP/1.1 200 OK Content-Type:application/json
```

`{`

```json
 "RequestId":"20C8341E-B5AD-4B24-BD82-D73241522ABF"
```

`}`

**Error codes**

| HttpCo de | Error code | Error message | Description |
|---|---|---|---|
| 400 | MissingInstanceId | MissingInstanceId | InstanceId is mandatory for this action. |
| 400 | MissingConnection String | MissingConnectionString | ConnectionStringPrefix is mandatory for this action. |
| 400 | MissingPort | MissingPort | Port is mandatory for this action. |
| 400 | NetTypeExists | NetTypeExists | Specified net type already existed. |
| 400 | InvalidConnectionS tring.Format | InvalidConnectionString.Forma t | Specified connection string is not valid. |

### 4.13 Backup and recovery

#### 4.13.1 CreateBackup

Backs up a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | CreateBackup | The operation that you want to perform. Set this parameter to CreateBackup. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=CreateBackup &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<CreateBackupResponse>
      <RequestId>2FF6158E-3394-4A90-B634-79C49184****</RequestId>
      <BackupJobID>1162****</BackupJobID>
</CreateBackupResponse>
```

JSON format `{`

```json
    "RequestId": "2FF6158E-3394-4A90-B634-79C49184****",
    "BackupJobID": "1162****"
```

`}`

#### 4.13.2 ModifyBackupPolicy

Modifies the backup policy of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A |   | For more information, see Common parameters. |   |   |
| Action | String | Yes | ModifyBackupPoli cy |   | The operation that you want to perform. Set this parameter to ModifyBackupPoli cy. |   |   |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** |   | The ID of the instance. |   |   |
| PreferredBackup Time | String | Yes | 00:00Z-04:00Z |   | The time to execute backup. Specify the time in the HH:mmZ- HH:mmZ format. |   |   |
|   |   |   |   |   |   | HH:mmZ- |   |
|   |   |   |   |   | HH:mmZ |   |   |

| PreferredBackupP eriod | String | Yes | Tuesday | The days of the week to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyBackupPolicy &InstanceId=r-bp1zxszhcgatnx**** &PreferredBackupTime=00:00Z-04:00Z &PreferredBackupPeriod=Tuesday &<Common request parameters>
```

**Sample responses**

XML format

```xml
<ModifyBackupPolicyResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</ModifyBackupPolicyResponse>
```

JSON format `{`

```json
    "RequestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

`}`

#### 4.13.3 DescribeBackupPolicy

Queries the backup policy of a KVStore for Redis instance. The backup policy includes information such as the backup cycle and the backup time.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
|---|---|---|---|---|
| Action | String | Yes | DescribeBackupP olicy | The operation that you want to perform. Set this parameter to DescribeBackupP olicy. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| BackupRetentionPerio d | String | 7 | The backup retention period. Unit: days. |
| PreferredBackupTime | String | 05:00Z-06:00Z | The time to execute backup. The time is in the HH:mmZ-HH:mmZ format. |
| PreferredBackupPeriod | String | Monday,Tuesday,Wed nesday,Thursday,Frida y,Saturday,Sunday | The days of the week to execute backup. Valid values: Monday Tuesday Wednesday Thursday Friday Saturday Sunday |
| PreferredNextBackupTi me | String | 2019-03-14T05:28Z | The scheduled time for the next backup. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackupPolicy &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeBackupPolicyResponse> <PreferredBackupPeriod>Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday</Preferre ackupPeriod>
      <RequestId>90B82DB7-FB28-4CC2-ADBF-1F8659F3****</RequestId>
      <PreferredNextBackupTime>2018-10-26T19:05Z</PreferredNextBackupTime>
      <PreferredBackupTime>19:00Z-20:00Z</PreferredBackupTime>
      <BackupRetentionPeriod>7</BackupRetentionPeriod>
</DescribeBackupPolicyResponse>
```

JSON format `{`

```json
 "PreferredBackupPeriod": "Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday",
 "RequestId": "90B82DB7-FB28-4CC2-ADBF-1F8659F3****",
 "PreferredNextBackupTime": "2018-10-26T19:05Z",
 "PreferredBackupTime": "19:00Z-20:00Z",
 "BackupRetentionPeriod": "7"
```

`}`

#### 4.13.4 DescribeBackups

Queries the backup files of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeBackups | The operation that you want to perform. Set this parameter to DescribeBackups . |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |
| BackupId | String | No | 11611111 | The ID of the backup set. |
| PageSize | String | Yes | 30 | The number of entries to return on each page. Valid values: 30, 50, and 100. |

| PageNumber | String | Yes | 1 | The number of the page to return. The value must be an integer that is greater than 0. |
|---|---|---|---|---|
| StartTime | String | Yes | 2019-03- 11T10:00Z | The beginning of the time range to query. |
| EndTime | String | Yes | 2019-03- 14T18:00Z | The end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| Backups | List | N/A | Details about of backup files. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| TotalCount | Integer | 5 | The total number of backup files that were returned. |
| PageSize | Integer | 30 | The number of entries returned per page. |

**Parameters of a backup file**

| Parameter | Type | Example | Description |
|---|---|---|---|
| BackupId | String | 111111111 | The ID of the backup set. |
| BackupDBNames | String | all | The name of the database that was backed up. |
| BackupStatus | String | Success | The status of the backup set. Success Failed |
| BackupStartTime | String | 2019-03- 14T05:28:50Z | The time when the backup started. |
| BackupEndTime | String | 2019-03- 14T05:31:13Z | The time when the backup ended. |

| BackupType | String | FullBackup | The type of the backup. Valid values: FullBackup IncrementalBackup |
|---|---|---|---|
| BackupMode | String | Automated | The mode in which data was backed up. Valid values: Automated Manual |
| BackupMethod | String | Physical | The method of the backup. Valid values: Logical Physical |
| BackupDownloadURL | String | https://rdsbak-hk45- v2.oss-cn- hongkong.aliyuncs.co m/******** | The download URL of the backup file. |
| BackupSize | String | 1024 | The size of the backup set. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeBackups &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2019-03-11T10:00Z &EndTime=2019-03-14T18:00Z &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeBackupsResponse>
      <TotalCount>1</TotalCount>
      <RequestId>721E2D39-351D-40E2-BF7C-B5075B0A****</RequestId>
      <PageSize>30</PageSize>
      <PageNumber>1</PageNumber>
      <Backups>
            <Backup>
                  <BackupMethod>Physical</BackupMethod>
                  <EngineVersion>4.0</EngineVersion>
                  <BackupIntranetDownloadURL>http://rdsbak-hz-v3.oss-cn-hangzhou-interna
l.aliyuncs.com/********</BackupIntranetDownloadURL>
                  <BackupMode>Automated</BackupMode>
                  <BackupSize>2263040</BackupSize>
                  <BackupId>775661111</BackupId>
                  <NodeInstanceId>r-bp12fdcf4dea****</NodeInstanceId>
                  <BackupDBNames>all</BackupDBNames>
                  <BackupDownloadURL>http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/********</BackupDownloadURL>
                  <BackupEndTime>2020-10-30T17:31:26Z</BackupEndTime>
                  <BackupStartTime>2020-10-30T17:28:28Z</BackupStartTime>
                  <BackupType>FullBackup</BackupType>
                  <BackupStatus>Success</BackupStatus>
            </Backup>
      </Backups>
</DescribeBackupsResponse>
```

JSON format

```json
    "TotalCount": 1,
    "RequestId": "721E2D39-351D-40E2-BF7C-B5075B0A****",
    "PageSize": 30,
    "PageNumber": 1,
    "Backups": {
        "Backup": [
```

`{`

```json
                "BackupMethod": "Physical",
                "EngineVersion": "4.0",
                "BackupIntranetDownloadURL": "http://rdsbak-hz-v3.oss-cn-hangzhou-intern
al.aliyuncs.com/********",
                "BackupMode": "Automated",
                "BackupSize": 2263040,
                "BackupId": 775661111,
                "NodeInstanceId": "r-bp12fdcf4dea****",
                "BackupDBNames": "all",
                "BackupDownloadURL": "http://rdsbak-hz-v3.oss-cn-
hangzhou.aliyuncs.com/********",
                "BackupEndTime": "2020-10-30T17:31:26Z",
                "BackupStartTime": "2020-10-30T17:28:28Z",
                "BackupType": "FullBackup",
                "BackupStatus": "Success"
```

`}` `]` `}` `}`

#### 4.13.5 RestoreInstance

Restores the data of a KVStore for Redis instance from a backup file to the instance. If you use the operation together with the data flashback feature, you can restore data of a specified key to a specified point in time that is accurate to the second.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | RestoreInstance | The operation that you want to perform. Set this parameter to RestoreInstance. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |
| BackupId | String | Yes | 78241**** | The ID of the backup set. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |

**Sample requests**

```
http(s)://r-kvstore.aliyuncs.com/?Action=RestoreInstance &InstanceId=r-bp1zxszhcgatnx**** &RestoreType=1 &RestoreTime=2021-07-06T07:25:57Z &FilterKey=key:00000007198* &Common request parameters
```

**Sample responses**

XML format

```xml
<RestoreInstanceResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</RestoreInstanceResponse>
```

JSON format `{`

```json
    "RequestId": "8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

`}`

### 4.14 Manage monitoring

#### 4.14.1 DescribeMonitorItems

Queries the metrics of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeMonitorIt ems | The operation that you want to perform. Set the value to DescribeMonitorIt ems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| MonitorItems | List | N/A | Details about metrics. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeMonitorItems &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeMonitorItemsResponse>
    <MonitorItems>
        <MonitorItem>
            <MonitorKey>GetQ</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>Flush</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>UsedMemCache</MonitorKey>
            <Unit>Bytes</Unit>
        </MonitorItem>
        <MonitorItem>
            <MonitorKey>ReplaceQ</MonitorKey>
            <Unit>Counts/s</Unit>
        </MonitorItem>
    </MonitorItems>
    <RequestId>B906A893-58A3-4644-AC2D-A2C9B08706C1</RequestId>
</DescribeMonitorItemsResponse>
```

JSON format

```json
    "MonitorItems" : {
        "MonitorItem" : [{
                "MonitorKey" : "GetQ",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "Flush",
                "Unit" : "Counts/s"
            }, {
                "MonitorKey" : "UsedMemCache",
                "Unit" : "Bytes"
            }, {
                "MonitorKey" : "ReplaceQ",
                "Unit" : "Counts/s"
```

`}` `]` `},`

```json
    "RequestId" : "B906A893-58A3-4644-AC2D-A2C9B08706C1"
```

`}`

#### 4.14.2 DescribeHistoryMonitorValues

Queries the monitoring history of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example |   | Description |   |   |
|---|---|---|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A |   | For more information, see Common parameters. |   |   |
| Action | String | Yes | DescribeHistoryM onitorValues |   | The operation that you want to perform. Set this parameter to DescribeHistoryM onitorValues. |   |   |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** |   | The ID of the instance. |   |   |
| StartTime | String | Yes | 2018-10- 18T12:00:00Z |   | The beginning of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. |   |   |
|   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   |   | DDThh:mm:ssZ |   |   |

| EndTime | String | Yes | 2018-10- 19T12:00:00Z |   | The end of the time range to query. Specify the time in the ISO 8601 standard in the YYYY-MM- DDThh:mm:ssZ format. The end of the time range must be later than or equal to the beginning of the time range. |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | YYYY-MM- |   |
|   |   |   |   | 00Z | DDThh:mm:ssZ |   |   |
| IntervalForHistor y | String | Yes | 01m |   | The sampling interval of the monitoring data. Valid values: 01, 05, 15, and 60. Unit: minutes. The sampling points are collected every N minutes. |   |   |
| MonitorKeys | String | No | CpuUsage |   | The keys of the metrics. You can query the value of the parameter by calling the DescribeMonitorIt ems operation. |   |   |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| MonitorHistory | String | {\"2020-11- 18T00:00:00Z\": {\"CpuUsage\":\"0.30\" },\"2020-11- 18T00:02:00Z\": {\"CpuUsage\":\"0.60\" },\"2020-11- 18T00:03:00Z\": {\"CpuUsage\":\"0.60\" }} | The metrics returned in the JSON format. For more information, see DescribeMonitorItems. Note To improve the data transmission efficiency, only metrics whose values are not 0 are returned. Metrics not displayed are all set to the default value 0. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeHistoryMonitorValues &InstanceId=r-bp1zxszhcgatnx**** &StartTime=2018-10-18T12:00:00Z &EndTime=2018-10-18T12:03:00Z &IntervalForHistory=01m &MonitorKeys=CpuUsage &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeHistoryMonitorValuesResponse>
      <MonitorHistory>{"2020-11-18T00:00:00Z":{"CpuUsage":"0.30"},"2020-11-
18T00:02:00Z":{"CpuUsage":"0.60"},"2020-11-18T00:03:00Z":{"CpuUsage":"0.60"}} </MonitorHistory>
      <RequestId>689E8093-3094-4DC2-A2A2-30D40097****</RequestId>
</DescribeHistoryMonitorValuesResponse>
```

JSON format `{`

```json
    "MonitorHistory": "{\"2020-11-18T00:00:00Z\":{\"CpuUsage\":\"0.30\"},\"2020-11-18T0
0:02:00Z\":{\"CpuUsage\":\"0.60\"},\"2020-11-18T00:03:00Z\":{\"CpuUsage\":\"0.60\"}}",
    "RequestId": "689E8093-3094-4DC2-A2A2-30D40097****"
```

`}`

### 4.15 Manage parameters

#### 4.15.1 DescribeInstanceConfig

Queries the configuration parameters of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | DescribeInstance Config | The operation that you want to perform. Set this parameter to DescribeInstance Config. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
| Config | String | {"#no loose statistics _ _ - cmds":"SET,GET","Evic tionPolicy":"volatile- lru","hash-max-ziplist- entries":512,"slowlog- log-slower- than":"1000","notify- keyspace- events":"$","zset-max- ziplist- entries":128,"list-max- ziplist- entries":512,"list-max- ziplist-value":64,"zset- max-ziplist- value":64,"set-max- intset- entries":512,"hash- max-ziplist- value":64,"#no loose _ _ disabled- commands":"flushall"} | The configuration parameters of the instance. For more information, see Instance configurations. |

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=DescribeInstanceConfig &InstanceId=r-bp1zxszhcgatnx**** &<Common request parameters>
```

**Sample responses**

XML format

```xml
<DescribeInstanceConfigResponse>
      <RequestId>4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****</RequestId>
      <Config>{"#no_loose_statistics-cmds":"SET,GET","EvictionPolicy":"volatile-lru","h
ash-max-ziplist-entries":512,"slowlog-log-slower-than":"1000","notify-keyspace-events": "$","zset-max-ziplist-entries":128,"list-max-ziplist-entries":512,"list-max-ziplist-val ue":64,"zset-max-ziplist-value":64,"set-max-intset-entries":512,"hash-max-ziplist-value ":64,"#no_loose_disabled-commands":"flushall"}</Config> </DescribeInstanceConfigResponse>
```

JSON format

```json
    "RequestId": "4E2C08F6-2D11-4ECD-9A4C-27EF2D3D****",
    "Config": "{\"#no_loose_statistics-
cmds\":\"SET,GET\",\"EvictionPolicy\":\"volatile-lru\",\"hash-max-ziplistentries\":512,\"slowlog-log-slower-than\":\"1000\",\"notify-keyspaceevents\":\"$\",\"zset-max-ziplist-entries\":128,\"list-max-ziplistentries\":512,\"list-max-ziplist-value\":64,\"zset-max-ziplist-value\":64,\"set-max-int set-entries\":512,\"hash-max-ziplist-value\":64,\"#no_loose_disabledcommands\":\"flushall\"}"
```

`}`

#### 4.15.2 ModifyInstanceConfig

Modifies configuration parameters of a KVStore for Redis instance.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| <Common request parameters> | N/A | Yes | N/A | For more information, see Common parameters. |
| Action | String | Yes | ModifyInstanceCo nfig | The operation that you want to perform. Set this parameter to ModifyInstanceCo nfig. |
| InstanceId | String | Yes | r- bp1zxszhcgatnx* *** | The ID of the instance. |
| Config | String | Yes | {"EvictionPolicy": "volatile-lru","list- max-ziplist- entries":512,"zse t-max-ziplist- entries":128,"has h-max-ziplist- entries":512,"has h-max-ziplist- value":64,"list- max-ziplist- value":64,"set- max-intset- entries":512,"zse t-max-ziplist- value":64} | The configuration parameters of the instance (JSON string). For more information, see Instance configurations. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| <Common response parameters> | N/A | N/A | For more information, see Common parameters. |
|---|---|---|---|

**Sample requests**

```
https://r-kvstore.aliyuncs.com/?Action=ModifyInstanceConfig &InstanceId=r-bp1zxszhcgatnx**** &Config={"EvictionPolicy":"volatile-lru","list-max-ziplist-entries":512,"zset-max-zipli st-entries":128,"hash-max-ziplist-entries":512,"hash-max-ziplist-value":64,"list-max-zi plist-value":64,"set-max-intset-entries":512,"zset-max-ziplist-value":64} &<Common request parameters>
```

**Sample responses**

XML format

```xml
<ModifyInstanceConfigResponse>
      <RequestId>8D0C0AFC-E9CD-47A4-8395-5C31BF9B****</RequestId>
</ModifyInstanceConfigResponse>
```

JSON format `{`

```json
  "requestId":"8D0C0AFC-E9CD-47A4-8395-5C31BF9B****"
```

`}`

### 4.16 Appendixes

#### 4.16.1 Instance types

KVStore for Redis provides instances of Community Edition and performance-enhanced instances of Enhanced Edition. Performance-enhanced instances of Enhanced Edition support the standard, cluster, and read/write splitting architectures. Instances of Community Edition support the standard and cluster architectures. This topic describes the specifications of different instance types, such as memory capacity, maximum number of connections, and maximum bandwidth value.

**Calculation rules for bandwidth**

If network resources are sufficient, bandwidth is unlimited. However, if network resources are insufficient, the bandwidth is limited. The upper limit of the total bandwidth for a cluster instance is 2,048 MB/s. After the upper limit is reached, the bandwidth cannot be increased even if the number of shards is increased. The bandwidth value applies to the upstream and downstream bandwidths. For example, if the bandwidth of an instance is 10 MB/s, the upstream and downstream bandwidths of the instance are both 10 MB/s. The bandwidth in the tables is the internal bandwidth of the KVStore for Redis instance. The Internet bandwidth is determined by the internal bandwidth and is limited by the bandwidth of the connection between the KVStore for Redis instance and the client. We recommend that you connect to the instance over an internal network to maximize performance.

**Performance-enhanced instances of KVStore for Redis**

**Enhanced Edition**

Table 1. Standard master-replica instances

| Specification | InstanceClass (used in API operations) | I/O thread s | Connecti ons per second | Maximu m connecti ons | Total bandwid th (MB/s) |
|---|---|---|---|---|---|
| 1 GB master- replica performance- enhanced instance | redis.amber.master.small.m ultithread | 6 | 10000 | 30000 | 96 |
| 2 GB master- replica performance- enhanced instance | redis.amber.master.mid.mul tithread | 6 | 10000 | 30000 | 96 |
| 4 GB master- replica performance- enhanced instance | redis.amber.master.stand.m ultithread | 6 | 10000 | 30000 | 96 |
| 8 GB master- replica performance- enhanced instance | redis.amber.master.large.m ultithread | 6 | 10000 | 30000 | 96 |
| 16 GB master- replica performance- enhanced instance | redis.amber.master.2xlarge. multithread | 6 | 10000 | 30000 | 96 |
| 32 GB master- replica performance- enhanced instance | redis.amber.master.4xlarge. multithread | 6 | 10000 | 30000 | 96 |
| 64 GB master- replica performance- enhanced instance | redis.amber.master.8xlarge. multithread | 6 | 10000 | 30000 | 96 |

Table 2. Cluster instances

| Specification | InstanceClass (used in API operations) | I/O thr ead s | Sha rds | Pro xy ser ver s | Con nec tion s per sec ond | Ma xim um con nec tion s | Ma xim um ban dwi dth val ue per sha rd | Tot al ban dwi dth (MB /s) |
|---|---|---|---|---|---|---|---|---|
| 2 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.sh arding.1g.2db.0rodb. 6proxy.multithread | 6 | 2 | 4 | 500 00 | 600 00 | 96 | 192 |
| 4 GB cluster performance- enhanced instance (2 shards) | redis.amber.logic.sh arding.2g.2db.0rodb. 6proxy.multithread | 6 | 2 | 4 | 500 00 | 500 00 | 96 | 192 |
| 8 GB cluster performance- enhanced instance (4 shards) | redis.amber.logic.sh arding.2g.4db.0rodb. 12proxy.multithread | 6 | 4 | 4 | 500 00 | 120 000 | 96 | 384 |
| 16 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.sh arding.2g.8db.0rodb. 24proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.sh arding.4g.8db.0rodb. 24proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 64 GB cluster performance- enhanced instance (8 shards) | redis.amber.logic.sh arding.8g.8db.0rodb. 24proxy.multithread | 6 | 8 | 8 | 500 00 | 240 000 | 96 | 768 |
| 32 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.sh arding.2g.16db.0rod b.48proxy.multithrea d | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 64 GB cluster performance- enhanced (16 shards) | redis.amber.logic.sh arding.4g.16db.0rod b.48proxy.multithrea d | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 128 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.sh arding.8g.16db.0rod b.48proxy.multithrea d | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |
| 256 GB cluster performance- enhanced instance (16 shards) | redis.amber.logic.sh arding.16g.16db.0ro db.48proxy.multithr ead | 6 | 16 | 16 | 500 00 | 480 000 | 96 | 153 6 |

| 512 GB cluster performance- enhanced instance (32 shards) | redis.amber.logic.sh arding.16g.32db.0ro db.96proxy.multithr ead | 6 | 32 | 32 | 500 00 | 500 000 | 96 | 204 8 |
|---|---|---|---|---|---|---|---|---|
| 1,024 GB cluster performance- enhanced instance (64 shards) | redis.amber.logic.sh arding.16g.64db.0ro db.192proxy.multith read | 6 | 64 | 64 | 500 00 | 500 000 | 96 | 204 8 |
| 2,048 GB cluster performance- enhanced instance (128 shards) | redis.amber.logic.sh arding.16g.128db.0r odb.384proxy.multit hread | 6 | 128 | 128 | 500 00 | 500 000 | 96 | 204 8 |
| 4,096 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.sh arding.16g.256db.0r odb.768proxy.multit hread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |
| 8,192 GB cluster performance- enhanced instance (256 shards) | redis.amber.logic.sh arding.32g.256db.0r odb.768proxy.multit hread | 6 | 256 | 256 | 500 00 | 500 000 | 96 | 204 8 |

**Community Edition instances**

Table 3. Standard master-replica instances

| Specification | InstanceClass (used in API operations) | Maximum connections | Total bandwidth (MB/s) | CPU |
|---|---|---|---|---|
| 1GB master- replica instance | redis.master.small.default | 10000 | 10 | 1 core |
| 2 GB master- replica instance | redis.master.mid.default | 10000 | 16 | 1 core |
| 4 GB master- replica instance | redis.master.stand.default | 10000 | 24 | 1 core |
| 8 GB master- replica instance | redis.master.large.default | 10000 | 24 | 1 core |
| 16 GB master- replica instance | redis.master.2xlarge.defa ult | 10000 | 32 | 1 core |
| 32 GB master- replica instance | redis.master.4xlarge.defa ult | 10000 | 32 | 1 core |
| 64 GB master- replica instance | redis.master.8xlarge.defa ult | 10000 | 48 | 1 core |

Table 4. Cluster instances

| Specification | InstanceClass (used in API operations) | Shar ds | Maximu m connect ions | Total bandwi dth (MB/s) | CPU |
|---|---|---|---|---|---|
| 16 GB cluster instance | redis.logic.sharding.2g.8db.0rodb.8pr oxy.default | 8 | 80000 | 768 | 8 cores |
| 32 GB cluster instance | redis.logic.sharding.4g.8db.0rodb.8pr oxy.default | 8 | 80000 | 768 | 8 cores |
| 64 GB cluster instance | redis.logic.sharding.8g.8db.0rodb.8pr oxy.default | 8 | 80000 | 768 | 8 cores |
| 128 GB cluster instance | redis.logic.sharding.8g.16db.0rodb.16 proxy.default | 16 | 160000 | 1536 | 16 cores |
| 256 GB cluster instance | redis.logic.sharding.16g.16db.0rodb.1 6proxy.default | 16 | 160000 | 1536 | 16 cores |
| 512 GB cluster instance | redis.logic.sharding.16g.32db.0rodb.3 2proxy.default | 32 | 320000 | 2048 | 32 cores |
| 1 TB cluster instance | redis.logic.sharding.16g.64db.0rodb.6 4proxy.default | 64 | 500000 | 2048 | 64 cores |
| 2 TB cluster instance | redis.logic.sharding.16g.128db.0rodb. 128proxy.default | 128 | 500000 | 2048 | 128 cores |
| 4 TB cluster instance | redis.logic.sharding.16g.256db.0rodb. 256proxy.default | 256 | 500000 | 2048 | 256 cores |

Table 5. Read/write splitting instances

| Specification | InstanceClass (used in API operations) | Read repli cas | Connec tions per second | Maxim um connec tions | Tota l ban dwid th (MB/ s) | QPS |
|---|---|---|---|---|---|---|
| 1 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.s mall.1db.1rodb.4pro xy.default | 1 | 20000 | 20000 | 96 | 200000 |
| 1 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.s mall.1db.3rodb.4pro xy.default | 3 | 40000 | 40000 | 192 | 400000 |
| 2 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.mi d.1db.1rodb.4proxy. default | 1 | 20000 | 20000 | 192 | 200000 |
| 2 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.mi d.1db.3rodb.4proxy. default | 3 | 40000 | 40000 | 384 | 400000 |

| 4 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.st and.1db.1rodb.4pro xy.default | 1 | 20000 | 20000 | 192 | 200000 |
|---|---|---|---|---|---|---|
| 4 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.st and.1db.3rodb.4pro xy.default | 3 | 40000 | 40000 | 384 | 400000 |
| 8 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.lar ge.1db.1rodb.4proxy .default | 1 | 20000 | 20000 | 192 | 200000 |
| 8 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.lar ge.1db.3rodb.4proxy .default | 3 | 40000 | 40000 | 384 | 400000 |
| 16 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.2x large.1db.1rodb.4pr oxy.default | 1 | 20000 | 20000 | 192 | 200000 |
| 16 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.2x large.1db.3rodb.4pr oxy.default | 3 | 40000 | 40000 | 384 | 400000 |
| 32 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.4x large.1db.1rodb.4pr oxy.default | 1 | 20000 | 20000 | 192 | 200000 |
| 32 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.4x large.1db.3rodb.4pr oxy.default | 3 | 40000 | 40000 | 384 | 400000 |
| 64 GB read/write splitting instance (1 shard, 1 read replica) | redis.logic.splitrw.8x large.1db.1rodb.4pr oxy.default | 1 | 20000 | 20000 | 192 | 200000 |
| 64 GB read/write splitting instance (1 shard, 3 read replicas) | redis.logic.splitrw.8x large.1db.3rodb.4pr oxy.default | 3 | 40000 | 40000 | 384 | 400000 |

#### 4.16.2 Error codes

| Description | Error code | Error message | HTTP status code |
|---|---|---|---|
| The error message returned because RAM users are not authorized to call the API operation. | Forbidden.RAM | User not authorized to operate on the specified resource, or this API doesn't support RAM. | 403 |
| The error message returned because the operation is unavailable for RAM users. | Forbedden.NotSupport RAM | This action does not support accessed by RAM mode. | 403 |
| The error message returned because an exception or error occurs on the server. | ServiceUnavailable | The request has failed due to a temporary failure of the server. | 503 |

| The error message returned because the instance status that you specified does not exist. | InvalidStatus.NotFoun d | The Status provided does not exist in our records. | 404 |
|---|---|---|---|
| The error message returned because the specified value of the parameter is invalid. | InvalidParameter | The specified parameter InstanceName is not valid. | 400 |
| The error message returned because you are not authorized to call the administrator- specific API operations. | Forbbiden.NotAdminUs er | User not authorized to operate on the specified API as you are not the | 403 |
| The error message returned because the parameter is missing. | MissingParameter | Specified parameter is missing. | 400 |
| The error message returned because neither InstanceName nor NewPassword is specified. | MissingParameter | InstanceName/NewPas sword at least one is mandatory for this action. | 400 |
| The error message returned because OwnerId is not specified for this operation. | MissingParameter | The input parameter OwnerId, OwnerAccount that is mandatory for processing this request | 403 |
| The error message returned because the specified Token parameter is invalid. | InvalidToken.Malforme d | The Specified parameter "Token" is not valid. | 400 |
| The error message returned because the specified InstanceName parameter is invalid. | InvalidInstanceName. Malformed | The Specified parameter "InstanceName" is not valid. | 400 |
| The error message returned because the specified Password parameter is invalid. | InvalidPassword.Malfor med | The Specified parameter "Password" is not valid." | 400 |
| The error message returned because the specified Instances parameter is invalid. | InvalidInstances.Malfor med | The Specified parameter "Instances" is not valid. | 400 |
| The error message returned because the specified StartTime parameter is invalid. | InvalidStartTime.Malfo rmed | The Specified parameter "StartTime" is not valid. | 400 |

| The error message returned because the specified EndTime parameter is invalid. | InvalidEndTime.Malfor med | The Specified parameter "EndTime" is not valid. | 400 |
|---|---|---|---|
| The error message returned because the specified InstanceIds parameter is invalid. | InvalidInstanceIds.Malf ormed | The Specified parameter "InstanceIds" is not valid. | 400 |
| The error message returned because your balance is insufficient to perform the current operation. | InsufficientBalance | Your account does not have enough balance. | 400 |
| The error message returned because your account fails to pass the real-name authentication. | RealNameAuthenticati onError | Your account has not passed the real-name authentication yet. | 403 |
| The error message returned because your instance quota has been exhausted. | QuotaExcee | Living afterpay instances quota exceeded. | 400 |
| The error message returned because the capacity configuration is invalid. | InvalidCapacity.NotFou nd | The Capacity provided does not exist in our records. | 400 |
| The error message returned because the ClientToken parameter used for this request has already been used for a different request. | IdempotentParameter Mismatch | Request uses a client token in a previous request but is not identical to that request. | 400 |
| The error message returned because the inventory of instances in the specified zone is insufficient. | QuotaNotEnough | Quota not enough in this zone. | 400 |
| The error message returned because you are not authorized to call the order-class API operations. | Forbbiden.SubUser | The specified action is not available for you. | 403 |
| The error message returned because the Apsara Stack risk control system denies this access request. | Forbidden.RiskControl | This operation is forbidden by Aliyun Risk Control system. | 403 |
| The error message returned because the specified region does not exist. | InvalidRegion.NotFoun d | The RegionId or ZoneId provided does not exist in our records. | 404 |

| The error message returned because the specified ZoneId parameter is invalid. | InvalidZoneId.NotFoun d | The ZoneId provided is invalid. | 400 |
|---|---|---|---|
| The error message returned because the ID of the instance does not exist. | InvalidInstanceId.NotF ound | The InstanceId provided does not exist in our records. | 404 |
| The error message returned because the password is incorrect. | IncorrectPassword | The Password provided is not correct. | 400 |
| The error message returned because the service is unavailable. | ServiceNotSupported | The specified service is not supported. | 400 |
| The error message returned because a renewal and configuration change order has not taken effect. | HasRenewChangeOrde r | This instance has a renewChange order. | 400 |
| The error message returned because an internal error occured. | InternalError | The request processing has failed due to some unknown error. | 500 |
| The error message returned because the specified backup time is invalid. | InvalidPreferredBacku pTime | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup type is invalid. | InvalidBackupType.For mat | Specified backup type is not valid. | 400 |
| The error message returned because the specified backup method is invalid. | InvalidBackupMethod. Format | Specified backup method is not valid. | 400 |
| The error message returned because the backup task already exists. | BackupJobExists | A backup job already exists in the specified DB instance. | 400 |
| The error message returned because the maximum number of daily backup operations has been reached. | BackupTimesExceeded | Exceeding the daily backup times of this DB instance. | 400 |
| The error message returned because no parameters are specified. | ParameterLeastAssoci ate | Must input at least one optional parameter. | 400 |

| The error message returned because the specified backup period is invalid. | InvalidBackupRetentio nPeriod.Malformed | Specified backup retention period is not valid. | 400 |
|---|---|---|---|
| The error message returned because the specified next backup time is invalid. | InvalidPreferredBacku pTime.Format | Specified preferred backup time is not valid. | 400 |
| The error message returned because the specified backup period is invalid. | InvalidPreferredBacku pPeriod.Malformed | Specified backup period is not valid. | 400 |
| The error message returned because the operation is not supported by the current instance type. | IncorrectDBInstanceTy pe | Current DB instance type does not support this operation | 400 |
| The error message returned because the specified key is invalid. | InvalidKey.Malformed | Specified key is not valid. | 400 |
| The error message returned because the nonce signature is used and cannot be used again. | SignatureNonceUsed | Specified signature nonce was used already. | 400 |
| The error message returned because no virtual IP address can be assigned. | AllocateVpcIp.NotEnou gh | Ip resource is not enough | 400 |
| The error message returned because instances of the specified type cannot be created in the zone. | Zone.NotSupport | Specified zone does not support creating with instance class. | 400 |
| The error message returned because the code for the instance type is invalid. | MissingClassCode | Capacity or InstanceClass is mandatory for this action. | 400 |
| The error message returned because the specified instance type is not supported. | InvalidDBInstanceClas s.NotFound | Specified DB instance class is not found. | 404 |
| The error message returned because the instance is locked. | IncorrectDBInstanceLo ckMode | Current DB instance lock mode does not support this operation. | 400 |
| The error message returned because the ID of the backup set does not exist. | InvalidBackupSetID.No tFound | Specified backup set ID does not exist. | 400 |

| The error message returned because the operation is not supported while the instance is in the current state. | IncorrectDBInstanceSt ate | Current DB instance state does not support this operation. | 400 |
|---|---|---|---|
| The error message returned when the available resource capacity in the specified instance is insufficient. | InsufficientResourceCa pacity | There is insufficient capacity available for the requested instance. | 400 |
| The error message returned because the specified end time is invalid. | InvalidEndTime.Format | Specified end time is not valid. | 400 |
| The error message returned because the specified duration for reserving a classic IP address is invalid. | InvalidClassicExpiredD ays.Format | The specified classicExpiredDays format is not valid. | 400 |
| The error message returned because the operation is not supported while the backup set is in the current state. | IncorrectBackupSetSta te | Current backup set state does not support operations. | 400 |
| The error message returned when the specified whitelist is not correct in format. | InvalidSecurityIPList.Fo rmat | Specified security IP list format is not valid. | 400 |

#### 4.16.3 Instance configurations

Table 1. KVStore for Redis instance configurations

| Parameter | Description | Value |
|---|---|---|

| maxmemory-policy | The eviction policy that a KVStore for Redis instance uses to evict data when the memory exceeds the threshold. KVStore for Redis supports six data eviction policies. | VolatileLRU: only evicts original data that has Time To Live (TTL) configured based on the Least Recently Used (LRU) algorithm. VolatileTTL: only evicts data that has TTL configured based on the TTL values in ascending order. AllKeysLRU: evicts original data based on the LRU algorithm. VolatileRandom: only evicts original data that has TTL configured randomly. AllKeysRandom: evicts original data randomly. NoEviction: evicts no data, but returns an error message when you write new data to the instance. |
|---|---|---|
| hash-max-ziplist-entries | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list- max-ziplist-entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list- max-ziplist-value. | Default value: 512. |
| hash-max-ziplist-value | A hash object uses ziplist encoding only if the hash object meets both of the following conditions: The number of key-value pairs stored in the hash object is smaller than or equal to the value of list- max-ziplist-entries. The string lengths of keys and values in all key-value pairs stored in the hash object are smaller than or equal to the value of list- max-ziplist-value. | Default value: 64. |

| list-max-ziplist-entries | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist- value. | Default value: 512. |
|---|---|---|
| list-max-ziplist-value | A list object uses ziplist encoding only if the list object meets both of the following conditions: The number of key-value pairs stored in the list object is smaller than or equal to the value of list-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the list object are smaller than or equal to the value of list-max-ziplist- value. | Default value: 64. |
| set-max-intset-entries | A set object uses intset encoding only if: the number of entries is smaller than or equal to the value of set-max-intset- entries and all entries are decimal integers. | Default value: 512. |
| zset-max-ziplist-entries | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 128. |

| zset-max-ziplist-value | A zset object uses ziplist encoding only if the zset object meets both of the following conditions: The number of key-value pairs stored in the zset object is smaller than or equal to the value of zset-max-ziplist- entries. The string lengths of keys and values in all key-value pairs stored in the zset object are smaller than or equal to the value of zset-max-ziplist- value. | Default value: 64. |
|---|---|---|
| notify-keyspace-events | The keyspace notifications allow clients to subscribe to channels or modes to receive events where Redis datasets were modified in some way. | K: the keyspace notifications. All notifications are prefixed with \ keyspace\@ \ . __ _ _ E: the keyevent notifications. All notifications are prefixed with keyevent@ . __ __ g: the notifications about general commands that are non-type specific, such as DEL, EXPIRE, and RENAME. $: the string command notifications. l: the list command notifications. s: the set command notifications. h: the hash command notifications. z: the sorted set command notifications. x: the expiration events. The system sends an expiration event after the system deletes an expired key. e: the eviction events. The system sends an eviction event after the system evicts a key according to the maxmemory policy. A: the alias for g$lshzxe. |
