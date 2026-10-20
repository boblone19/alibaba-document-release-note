---
title: "Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Developer Guide 20260831"
product_version: "V3.18.6_2607"
doc_version: "20260831"
pdf_pages: 98
source_pdf: "1d8d1790e07f265b_Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Developer Guide 20260"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/3816%202607/pdf%203/%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AE%A1%E8%AE%A1%EF%BC%88%E4%B8%93%E6%9C%89%E4%BA%91%EF%BC%89/Alibaba%20Cloud%20Apsara%20Stack%20v3.18.6-2607%20Database%20Audit%20Database%20Security%20Audit%20Developer%20Guide%2020260831.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack v3.18.6-2607 Database Audit Database Security Audit Developer Guide 20260831

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 Obtain the information and the endpoint of an API operation
  - 1.3 Obtain access credentials assigned by RAM
  - 1.4 Obtain access credentials assigned by STS
  - 1.5 Obtain the values of common request headers
- 2 Call examples
  - 2.1 SDK for Java
    - 2.1.1 Use the SDK
      - 2.1.1.1 Install the SDK for Java
      - 2.1.1.2 Configure authentication credentials
      - 2.1.1.3 Configure connection requests
      - 2.1.1.4 Initiate a request
      - 2.1.1.5 Troubleshooting
      - 2.1.1.6 Use CommonRequest to call API operations
  - 2.2 SDK for Python
    - 2.2.1 Use the SDK
      - 2.2.1.1 Install the SDK for Python
      - 2.2.1.2 Configure authentication credentials
      - 2.2.1.3 Configure HTTPS requests
      - 2.2.1.4 Initiate a request
      - 2.2.1.5 Troubleshooting
      - 2.2.1.6 Use CommonRequest to call API operations
  - 2.3 SDK for Go
    - 2.3.1 Use the SDK
      - 2.3.1.1 Install the core package of the SDK for Go
      - 2.3.1.2 Configure authentication credentials
      - 2.3.1.3 Initiate a request
      - 2.3.1.4 Troubleshooting
      - 2.3.1.5 Use CommonRequest to call API operations
- 3 Common parameters
- 4 DataBase Audit API reference
  - 4.1 Databases
    - 4.1.1 ListSupportDbTypesForDataSource
    - 4.1.2 ListDataSources
    - 4.1.3 CreateDataSource
    - 4.1.4 ModifyDataSource
    - 4.1.5 DeleteDataSource
  - 4.2 Agents
    - 4.2.1 GetAgentList
  - 4.3 Risk identification rules
    - 4.3.1 GetRuleList
    - 4.3.2 EnableRulesForThisDB
    - 4.3.3 DisableRulesForThisDB
  - 4.4 Audit
    - 4.4.1 GetDBAuditCount
    - 4.4.2 GetAuditSearchList
    - 4.4.3 GetFailedSqlList
    - 4.4.4 GetSessionSearchList
    - 4.4.5 GetFailedSessionList
    - 4.4.6 GetRiskSqlSearchList
    - 4.4.7 GetRiskBitsList
    - 4.4.8 GetApiSearchConditionResult
- 5 Error codes

## 1 Preparations

### 1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and
press Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Others > API Tool**.

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

### 1.3 Obtain access credentials assigned by RAM

**assigned by RAM**

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use either type of access credential for authentication when you make an API request. This topic describes how to obtain access credentials that are assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign access credentials for authentication. Use RAM to assign an AccessKey ID and an AccessKey secret to a third party. Use STS to assign an AccessKey ID, an AccessKey secret, and a security token to a third party. For more information, see Obtain access credentials assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts. To use the AccessKey pair of a personal account, you must configure the headers in the following table. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console and has limited permissions.

| Header | Description |
|---|---|
| x-acs-regionid | The region ID. Example: cn-hangzhou-*. |
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain an organization ID, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain a resource set ID, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. For example, you can use the ID of an Elastic Compute Service (ECS) instance obtained from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log in to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair.

> **Note:** The AccessKey pair provides full permissions on cloud resources within your account. You must keep the AccessKey pair strictly confidential.

### 1.4 Obtain access credentials assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to call Apsara Stack API operations.

**Background information**

Apsara Stack STS allows you to manage temporary access credentials for your Apsara Stack resources. You can use STS to call Apsara Stack API operations. Access credentials assigned by STS consist of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, these three elements are required.

**Procedure**

1. Obtain the Apsara Stack Resource Name (ARN) of your Resource Access Management
(RAM) role. i. Log in to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view the ARN of your RAM role.
2. Obtain the access credentials assigned by STS.

> **Note:** Replace the variables in the following sample code with actual values. Delete the angle brackets (<>) from the final code.
> The following list describes the variables:
> <yourRegionID>: Replace this variable with the actual region ID.
> <yourAccessKeyID>: Replace this variable with your AccessKey ID.
> <yourAccessKeySecret>: Replace this variable with your AccessKey secret.
> <yourRoleSessionName>: Replace this variable with the actual session name.
> You can customize the session name. We recommend that you set the session name to your identity information such as username. This way, users who assume the same RAM role to perform operations can be distinguished based on the value of the `RoleSessionName` variable. This facilitates user-specific audit. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_).
> <yourRoleArn>: Replace this variable with the actual ARN of your RAM role.
> "sts.aliyuns.com": Replace this variable with the actual endpoint of STS.

```xml
public static void main(String[] args) {
    // Create a DefaultAcsClient instance and initialize it.
    // Replace <yourRegionID>, <yourAccessKeyID>, and <yourAccessKeySecret> with the
actual region ID, your AccessKey ID, and your AccessKey secret.
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
    // Obtain the access credentials assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace sts.aliyuns.com with the actual endpoint of STS. The format of an STS
endpoint is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace <yourRoleSessionName> with the actual session name.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // Replace <yourRoleArn> with the ARN of your RAM role that is obtained in the pr
evious step.
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
```

`}`

```
    return null;
```

`}`
3. Use the access credentials assigned by STS to call an API operation of a service. The
following sample code provides an example on how to call the `DescribeZones` operation of Elastic Compute Service (ECS):

> **Note:** Replace the variables in the following sample code with actual values. Delete the angle brackets (<>) from the final code.
> The following list describes the variables:
> <yourRegionID>: Replace this variable with the actual region ID.
> <yourStsAccesskeyID>: Replace this variable with the AccessKey ID assigned by STS.
> <yourStsAccessKeySecret>: Replace this variable with the AccessKey secret assigned by STS.
> <yourStsToken>: Replace this variable with the security token assigned by STS.
> <yourResourceGroupID>: Replace this variable with the actual resource set ID.
> <yourOrganizationID>: Replace this variable with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace <yourRegionID> with the actual region ID.
    // Replace <yourStsAccessKeyID> and <yourStsAccessKeySecret> with the AccessKey I
D and AccessKey secret assigned by STS, which are obtained in the previous step.
    DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "
<yourStsAccesskey>", "<yourStsAccessSecret>");
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
    // Replace <yourRegionID> with the actual region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace <yourStsToken> with the security token assigned by STS, which is obtai
ned in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace <yourResourceGroupID> with the actual resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Optional. Replace <yourOrganizationID> with the actual organization ID.
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

`}` `}`

### 1.5 Obtain the values of common request headers

**request headers**

You must specify multiple request headers when you call Apsara Stack API operations. This topic describes the common request headers and how to obtain the values of the request headers. This topic also describes the return values of specific parameters after you call API operations.

**Common request headers**

| Header | Description |
|---|---|

| x-acs-regionid | The region ID. For more information about how to obtain region IDs, see Obtain a region ID. |
|---|---|
| x-acs-organizationid | The organization ID in the Apsara Uni-manager Management Console. For more information about how to obtain organization IDs, see Obtain an organization ID. |
| x-acs-resourcegroupid | The resource set ID in the Apsara Uni-manager Management Console. For more information about how to obtain resource set IDs, see Obtain a resource set ID. |
| x-acs-instanceid | The ID of the instance that you want to manage. For more information about how to obtain instance IDs, see Obtain an instance ID. |

**Obtain a region ID**

1. Log in to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of an organization.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You must call an API operation to obtain an organization ID. For more information about how to obtain organization IDs, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You must call an API operation to obtain a resource set ID. For more information about how to obtain resource set IDs, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain an instance ID**

You can obtain the ID of an instance in a service console of the Apsara Uni-manager Management Console. In this example, the Elastic Compute Service (ECS) console is used. Perform the following steps to obtain the ID of an ECS instance:
1. Log in to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Computing** > **Elastic Compute Service**.
3. In the left-side navigation pane, choose **Instances & Images > ECS Instances** .
4. On the **ECS Instances** page, view the ID of an ECS instance.

**Response parameters**

The following table describes the additional response parameters that are returned by default when you call API operations to query the instances of Apsara Stack services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The resource set ID. |
| DepartmentName | The name of the organization. |
| Department | The organization ID. |

## 2 Call examples

### 2.1 SDK for Java

#### 2.1.1 Use the SDK

##### 2.1.1.1 Install the SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 and later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit OpenAPI Explorer. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about SDK versions, visit SDK Center.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 2.1.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports identity authentication based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain access credentials assigned by RAM. If you want to use your AccessKey pair to access Apsara Stack services, you must configure the AccessKey pair as credentials when you initialize a client.

> **Note:** Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace this variable with the actual region ID.
    "<yourAccessKeyID>",      // Replace this variable with your AccessKey ID.
    "<yourAccessKeySecret>"); // Replace this variable with your AccessKey secret.
```

> **Note:** Replace the variables in the preceding sample code with actual values. Delete the angle brackets (<>) from the final code.

##### 2.1.1.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

> **Note:** Replace the variables in the following sample code with actual values. Delete the angle brackets (<>) from the final code.
> The following list describes the variables:
> <readTimeout>: Specify a read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Specify a connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
> <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
> <http://192.168.XX.XX:33XX>: Replace this variable with the IP address and port number of the proxy that you use.

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // Optional. Specify a read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // Optional. Specify a connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // Optional. Specify the maximum number of requests that are supported by each server. The supported data type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // Optional. Specify the maximum number of requests. The supported data type is INTEGER
```

`.`

```
clientConfig.setMaxRequests(<maxRequests>); // Optional. Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** Optional. Specify whether to configure a proxy based on your business requirements. Sample code: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`Or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace the variable with the IP address and port number of the proxy that you use.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

##### 2.1.1.4 Initiate a request

This topic describes how to initiate a request by using Apsara Stack SDK for Java.

**Procedure**

1. Create an AcsClient instance.

```
IAcsClient client = new DefaultAcsClient(profile);
```

2. Create a request.
The naming convention for requests is ${apiName}Request . **${apiName}** specifies the name of an API operation, such as DescribeInstances. When the SDKs of multiple services are used, different requests may have the same name. Differentiate the requests by using SDK package names.

```
DescribeInstancesRequest request = new DescribeInstancesRequest(); // Specify operation-specific parameters. request.setPageSize(10); request.setPageNumber(1); // Specify headers. For example, specify the organization ID and resource set ID to q uery specified resources. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
```

3. Initiate the request and handle the response.

```java
DescribeInstancesResponse response; try {
    response = client.getAcsResponse(request);
    for (DescribeInstancesResponse.Instance instance:response.getInstances()) {
        System.out.println(instance.getPublicIpAddress());
```

`}`

```
} catch (ServerException e) {
    e.printStackTrace();
} catch (ClientException e) {
    e.printStackTrace();
```

`}` In most cases, all returned parameters are deserialized into the response. You can call the `response.getXXX()` method to obtain the parameters in the response.

```
instanceStatus := response.getStatus()
```

If an exception occurs or you need the original HTTP response, you can use the `doAction()` method to obtain the original response.

```
HttpResponse response = client.doAction(request);
```

##### 2.1.1.5 Troubleshooting

If an error occurs on the server or in the SDK when you use Apsara Stack SDK for Java, an error response is returned. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by Apsara Stack SDK for Java. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

If you want to handle the SDK errors returned by Apsara Stack SDK for Java, refer to the following example to write your code:

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Handle the response.
    // ...
}catch (ServerException e){
    // Add your logic for handling errors.
    // For example, you can display the error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If the error persists, submit a ticket that includes the request ID (RequestId)
to request technical support.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your logic for handling errors.
    // For example, you can display the error information.
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}`

##### 2.1.1.6 Use CommonRequest to call API operations

**Prerequisites**

We recommend that you use CommonRequest to call Apsara Stack API operations. To view the recommended SDK version and sample code, perform the following operations: Log in to the Apsara Uni-manager Management Console. In the top navigation bar, choose **Products** >
**Development Tools** > **API & SDK** > **OpenAPI Explorer**. In the top navigation bar of the
page that appears, choose **API Integration** > **API Debugging**.

**Important**

We recommend that you do not download SDKs fromSDK Centerand use them in Apsara Stack. SDKs for the Alibaba Cloud public cloud may not support Apsara Stack API operations and may have compatibility issues. Proceed with caution.

**Use CommonRequest to call API operations**

The following sample code provides an example on how to call RPC API operations. In this example, the DescribeApiGroups operation of API Gateway is called, and the API version is 2016-07-14. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class DescribeApiGroups {
```

```java
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request method.
        request.setSysMethod(MethodType.POST);
        // Specify the endpoint of the service.
        request.setSysDomain("<apigatewayEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-07-14");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("apigateway");
        // Specify the name of the API operation.
        request.setSysAction("DescribeApiGroups");
        // If you use access credentials assigned by Security Token Service (STS) to ca
ll RPC API operations, you must specify the SecurityToken parameter.
        // request.putBodyParameter("SecurityToken", "<your-SecurityToken>");
        // Configure service-related parameters.
        request.putQueryParameter("PageSize", "10");
        request.putQueryParameter("PageNumber", "1");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and del
ete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        try {
            // Initiate the request and handle the response or exception.
            CommonResponse response = client.getCommonResponse(request);
            System.out.println(response.getData());
```

`}`

```
th(S
```

`E` `ti` `)``{`

```java
        } catch (ServerException e) {
            e.printStackTrace();
        } catch (ClientException e) {
            System.out.println("ErrCode:" + e.getErrCode());
            System.out.println("ErrMsg:" + e.getErrMsg());
            System.out.println("RequestId:" + e.getRequestId());
```

`}` `}` `}` The following sample code provides an example on how to call ROA API operations. In this example, the GetNamespaceList operation of Container Registry is called, and the API version is 2016-06-07. Sample code:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.MethodType; import com.aliyuncs.profile.DefaultProfile; public class GetNamespaceList {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile("<your-regionid>", "
<yourAccessKeyId>", "<yourAccessSecret>");
        // Ignore SSL certificate verification.
        // HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        // clientConfig.setIgnoreSSLCerts(true);
        // Specify the timeout period for a connection.
        // clientConfig.setConnectionTimeoutMillis(3000L);
        // Specify the read timeout period.
        // clientConfig.setReadTimeoutMillis(10000L);
        // profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and specify the request parameters.
        CommonRequest request = new CommonRequest();
        // Specify the request protocol to HTTPS.
        request.setSysProtocol(ProtocolType.HTTP);
        // Specify the request method.
        request.setSysMethod(MethodType.GET);
        // Specify the endpoint of the service.
        request.setSysDomain("<crEndpoint>");
        // Specify the API version.
        request.setSysVersion("2016-06-07");
        // Specify the uriPattern parameter, which is required for ROA APIs.
```

```java
        request.setSysUriPattern("/namespace");
        // Specify the name of the service that you want to access and the region where
the service resides.
        request.setSysLocationProduct("cr");
        // Specify the name of the API operation.
        request.setSysAction("GetNamespaceList");
        // Required. Specify the call source.
        request.putHeadParameter("x-acs-caller-sdk-source", "ApiTestDemo");
        // Optional. The region ID. This parameter is required for Apsara Stack V3.15.0
and earlier.
        request.putHeadParameter("x-acs-regionid", "<your-regionid>");
        // Optional. Specify the ID of the resource set.
        request.putHeadParameter("x-acs-resourcegroupid", "<your-resourcegroupid>");
        // Required. Specify the organization ID.
        request.putHeadParameter("x-acs-organizationid", "<your-organizationid>");
        // Optional. The instance ID. This parameter is required for the modify and del
ete operations.
        // request.putHeadParameter("x-acs-instanceid", "<your-instanceid>");
        // If you use access credentials assigned by STS to call ROA API operations, yo
u must add the x-acs-security-token field to the header.
        // request.putHeadParameter("x-acs-security-token", "<your-securitytoken>");
        try {
            // Initiate the request and handle the response or exception.
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

### 2.2 SDK for Python

#### 2.2.1 Use the SDK

##### 2.2.1.1 Install the SDK for Python

This topic describes how to install and use Apsara Stack SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x and later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK for Python of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python.

If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip3 install aliyun-python-sdk-core-v3
```

##### 2.2.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDK for Python supports identity authentication based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain access credentials assigned by RAM. If you want to use your AccessKey pair to access Apsara Stack services, you must configure the AccessKey pair as credentials when you initialize a client.

> **Important:** Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

```
clt = client.AcsClient(secret_id, secret_key, region_id)
```

##### 2.2.1.3 Configure HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or specify a global default protocol.

> **Note:** The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

OpenSSL support in Python is required for sending HTTPS requests by using Apsara Stack SDK for Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports Transport Layer Security (TLS) 1.2 and later. Run the `python -c "import ssl"` command to check whether your Python environment supports OpenSSL. If the error message `ImportError: No module named ssl` does not appear, OpenSSL is supported. If OpenSSL is not supported, run the following command to install it:

```
pip install pyopenssl
```

**Set the protocol to HTTP or HTTPS for a single request**

The following sample code provides an example on how to set HTTPS as the protocol for a request:

```bash
request = DescribeInstancesRequest() request.set_protocol_type("https")
# Valid values: https and http.
```

**Specify a global default protocol**

The following sample code provides an example on how to specify a global default protocol:

```java
import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call the client.do_action_with_exception() method to send the re
quest.
```

##### 2.2.1.4 Initiate a request

This topic describes how to initiate a request by using Apsara Stack SDK for Python.

**Procedure**

1. Import the SDK for Python of a service.

```python
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
```

2. Create an AcsClient instance.

```
client.region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
```

3. Create a request.

```
request = DescribeInstancesRequest.DescribeInstancesRequest() request.set_accept_format('json')
```

4. Initiate the request and handle the response.

```
response = clt.do_action_with_exception(request) print response
```

##### 2.2.1.5 Troubleshooting

If an error occurs on the server or in the SDK when you use Apsara Stack SDK for Python, an error response is returned. The error response contains an error code and an error message. In most cases, you do not need to handle the errors returned by Apsara Stack SDK for Python. You need to only handle the errors returned by the server based on error messages. `ServerException` indicates a server error. `ClientException` indicates an SDK error. The following error indicates that the AccessKey ID is invalid. You must specify a valid AccessKey ID.

```
aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

If you want to handle the SDK errors returned by Apsara Stack SDK for Python, refer to the following example to write your code:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your logic for handling errors.
    # For example, you can display the error information.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

##### 2.2.1.6 Use CommonRequest to call API operations

**Prerequisites**

In Apsara Stack, use CommonRequest to make API calls. You can find the recommended SDK version and sample code in the Apsara Uni-manager Management Console. To do this, navigate to **Products** > **Development Tools** > **API And Tools** > **Developer Portal** and select **API Integration** > **API Debugging**.

**Important**

Do not download SDKs directly from the SDK Center for Apsara Stack scenarios. The SDKs for the public cloud may not support Apsara Stack APIs or have compatibility issues. Use them with caution.

**Background information**

Currently, you can call APIs only using the Remote Procedure Call (RPC) method.

**CommonRequest call example**

The following example shows how to call the DescribeInstances operation of ECS. The API version is 2014-05-26. The following is the sample code:

```java
from aliyunsdkcore.client import AcsClient import os from aliyunsdkcore.request import CommonRequest
# Create an AcsClient instance.
client = AcsClient(
    "<AccessKey ID>",
    "<AccessKey secret>",
    "<your-RegionID>",
    timeout=1000,  # Set the timeout period.
    verify=False, # Ignore the certificate or set verify='<certificate_path>'.
```

);

```bash
# Use with HTTPS.
```

```python
# client.set_verify(False)
# os.environ["HTTPS_PROXY"] = "http://127.0.0.1:8080"
# os.environ["HTTP_PROXY"] = "http://127.0.0.1:8080"
def describe_api_groups():
    # Create a request and set its parameters.
    request = CommonRequest()
    # When you call an RPC API using an STS AccessKey pair, add the SecurityToken field
to the parameters.
    # params = {"PageSize":"10","PageNumber":"1","SecurityToken":"<your-
SecurityToken>"};
    params = {"PageSize":"10","PageNumber":"1"};
    request.set_query_params(params)
    headers = {
        # Required. A description of the call source.
        "x-acs-caller-sdk-source":"ApiTestDemo",
        # Optional. Required for versions earlier than Enterprise Edition V3.15.0.
        "x-acs-regionid":"<your-RegionID>",
        # Optional. The resource group ID.
        "x-acs-resourcegroupid":"<your-ResourceGroupID>",
        # Required. The organization ID.
        "x-acs-organizationid":"<your-OrganizationID>"
        # Optional. Required for modify and delete operations.
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
    # Initiate the API request and print the return value.
    response = client.do_action_with_exception(request)
    print(response)
if __name__ == '__main__':
    print("Hello Aliyun OpenApi!")
    describe_api_groups()
```

**Set a proxy**

When you call an API, you may need to set the HTTP_PROXY and HTTPS_PROXY environment variables. The following is the sample code:

```bash
# HTTPS proxy
os.environ["HTTPS_PROXY"] = "http://x.x.x.x:xxxx"
# HTTP proxy
os.environ["HTTP_PROXY"] = "https://x.x.x.x:xxxx"
```

**HTTPS configuration**

This section describes how to access OpenAPI using the HTTPS protocol.

**Use the HTTPS protocol**

By default, the SDK uses the HTTPS protocol.

```
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
```

`)`

```
request = DescribeInstancesRequest() request.set_protocol_type('https') # Use HTTPS. client.do_action_with_exception(request)
```

**Ignore certificates**

> **Important:** When you access OpenAPI using the HTTPS protocol, the SDK verifies the SSL/TLS certificate by default. If your code environment does not have a certificate, a certificate verification error is reported.
> To ensure secure communication in a production environment, keep this verification enabled. If you must ignore certificate verification in a test environment, set the `verify` parameter.

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify=False  # Ignore SSL certificate verification.
```

`)`

**Specify a CA certificate file**

```
from aliyunsdkcore.client import AcsClient client = AcsClient(
    region_id='<region_id>',  # Region ID
    verify='./cacert.pem'  # Certificate path
```

`)`

### 2.3 SDK for Go

#### 2.3.1 Use the SDK

##### 2.3.1.1 Install the core package of the SDK for Go

This topic describes how to install the core package of Apsara Stack SDK for Go. Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core package of Apsara Stack SDK for Go:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

##### 2.3.1.2 Configure authentication credentials

When you use Apsara Stack SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. Apsara Stack SDK for Go supports identity authentication based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain access credentials assigned by RAM. If you want to use your AccessKey pair to access Apsara Stack services, you must configure the AccessKey pair as credentials when you initialize a client.

> **Important:** Do not disclose the code that contains your AccessKey pair. For example, do not commit the code to publicly accessible GitHub projects. Otherwise, your Apsara Stack tenant account may be compromised.

The following sample code provides an example on how to initialize an ecsClient instance:

```
// Initialize the ecsClient instance. ecsClient, err := ecs.NewClientWithAccessKey(
        "<yourRegionID>",                 // Replace this variable with the actual regio
n ID.
        "<yourAccessKeyID>",             // Replace this variable with your AccessKey ID
```

`.`

```
        "<yourAccessKeySecret>")        // Replace this variable with your AccessKey
secret.
```

> **Note:** Replace the variables in the preceding sample code with actual values. Delete the angle brackets (<>) from the final code.

##### 2.3.1.3 Initiate a request

This topic describes how to initiate a request by using Apsara Stack SDK for Go. In this example, a request is initiated by using Elastic Compute Service (ECS) SDK for Go.
1. Import ECS SDK for Go.

```java
import github.com/aliyun/alibaba-cloud-sdk-go/services/ecs
```

2. Create an ecsClient instance that contains all the API operations of ECS.

> **Note:** Replace the variables in the following sample code with actual values. Delete the angle brackets (<>) from the final code.

```
ecsClient,err := <ecs>.NewClientWithAccessKey( // Replace the <ecs> variable with th e name of the service.
    "<yourRegionID>",  // Replace this variable with the actual region ID.
    "<yourAccessKeyID>",  // Replace this variable with your AccessKey ID.
    "<yourAccessKeySecret>")  // Replace this variable with your AccessKey secret.
ecsClient.Domain = "ecs.aliyuns.com" // Specify the endpoint of the service.
```

3. Use the `xxx.CreateXXXRequest` method to create a request.
The naming convention for this method is ${service}.Create${apiName}Request , where:
**${service}**: the name of the service in lowercase, such as ecs.
**${apiName}**: the name of the API operation, such as DescribeInstances.

```
request := ecs.CreateDescribeInstanceAttributeRequest() request.InstanceId = ""
```

4. Initiate the request.

```
response, err := ecsClient.DescribeInstanceAttribute(request)
```

##### 2.3.1.4 Troubleshooting

When you use Apsara Stack SDK for Go, a `ClientError` response is returned if an error occurs on the client, or a `ServerError` response is returned if an error occurs on the server. Both error types are included in `sdk.errors` . The errors conform to the standard Go error interface and can be handled in the same manner as standard Go errors.

**Error handling**

You can use the following code to handle errors:

```
response,err := ecsClient.DescribeInstances(request) if err != nil {
    // Obtain the error information.
   err.Error()
```

`}`

**ClientError**

When you send a request, if an error occurs in the SDK and cannot be automatically handled, the SDK returns a `ClientError` response. The following sample code provides an example on how to identify and obtain the error message in a `ClientError` response returned by ECS SDK for Go:

> **Important:** When you use a specific error struct, you need to add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

> `)`

```
response, err := ecsClient.DescribeInstances(request) if clientError, ok := err.(*errors.ClientError); ok{
    // Obtain the error code.
    clientError.ErrorCode()
    // Obtain the error message.
    clientError.Message()
    // Obtain the original error. The return value may be nil.
    clientError.OriginError()
```

`}`

**ServerError**

When the server returns an error message, the SDK wraps the message into the `ServerError` response and returns it to the client. In this case, you can still obtain the original HTTP response from the response. The following sample code provides an example on how to identify and obtain the error message in a ServerError response and the response returned by ECS SDK for Go:

> **Important:** When you use a specific error struct, you need to add the error package `github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors` by using the following code:

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/services/ecs" // Replace ecs with the n
ame of the actual service.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    // The error package that you want to add.
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/errors"
    "fmt"
```

> `)`

```
response, err := ecsClient.DescribeInstances(request) if serverError, ok := err.(*errors.ServerError); ok{
    // Obtain the error code.
    serverError.ErrorCode()
    // Obtain the error message.
    serverError.Message()
    // Obtain the original HTTP response.
    response.GetOriginHttpResponse()
```

`}`

##### 2.3.1.5 Use CommonRequest to call API operations

**Prerequisites**

For Apsara Stack, use CommonRequest to make API calls. In the Apsara Uni-manager Management Console, go to **Products** > **Development Tools** > **API And Tools** >
**Developer Portal**. Then, choose **API Integration** > **API Debugging** to view the
recommended SDK versions and sample code.

**Important**

Do not download SDKs directly from the SDK Center for Apsara Stack environments. SDKs for the Alibaba Cloud public cloud might not support Apsara Stack APIs and can cause compatibility issues. Use them with caution.

**Background information**

You can call APIs using the Remote Procedure Call (RPC) or Resource-Oriented Architecture (ROA) style.

**CommonRequest call examples**

The API information for the RPC example is as follows: Product (apigateway), API operation (DescribeApiGroups), and Version (2016-07-14). The following code is an example:

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
cessKey secret>")
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<ApigatewayEndpoint>"
    request.Version = "2016-07-14"
    request.ApiName = "DescribeApiGroups"
    request.Product = "apigateway"
    // If you use an STS AccessKey pair to call an RPC API, add the SecurityToken param
eter.
    // request.QueryParams["SecurityToken"]="<your-SecurityToken>"
    // Required. Specify the source of the call.
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
    // Optional. Required for modify and delete operations.
    // request.Headers["x-acs-instanceid"] = "<your-InstanceID>"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` The API information for the ROA example is as follows: Product (CR), API operation (GetNamespaceList), and Version (2016-06-07). The following code is an example:

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
 // If you use an STS AccessKey pair to call a ROA API, add the x-acs-security-token fi
eld to the header.
 // request.Headers["x-acs-security-token"] = "<your-SecurityToken>"
 // Required. Specify the source of the call.
 request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo"
    // Optional. Required for Apsara Stack Enterprise Edition V3.15.0 and earlier.
    request.Headers["x-acs-regionid"] = "<your-RegionID>"
    // Optional. The resource group ID.
    request.Headers["x-acs-resourcegroupid"] = "<your-ResourceGroupID>"
    // Required. The organization ID.
    request.Headers["x-acs-organizationid"] = "<your-OrganizationID>"
 // Optional. Required for modify and delete operations.
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

**Set a proxy**

You may need to set a proxy when you call an instance. You can set the proxy in one of the following two ways. Set the proxy using environment variables. Use the HTTP_PROXY, HTTPS_PROXY, or NO_PROXY environment variables. The following code is an example:

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

`}` Set the proxy on the client. The following code is an example:

```
// Proxy settings on the client have a higher priority than environment variables. client.SetHttpProxy("http://x.x.x.x:xxxx") // Set the HTTP proxy. client.GetHttpProxy() // Get the HTTP proxy. client.SetHttpsProxy("https://x.x.x.x:xxxx") // Set the HTTPS proxy. client.GetHttpsProxy() // Get the HTTPS proxy. client.SetNoProxy("127.0.0.1,localhost") // Set the proxy whitelist. client.GetNoProxy() // Get the proxy whitelist.
```

**SSL verification**

**Summary**

This setting controls the SSL certificate verification behavior for requests. Set to `true` to disable certificate verification. This is an insecure practice. We recommend that you configure a certificate. Set to `false` to enable SSL certificate verification. By default, the operating system's CA certificates are used.

**Default value**

The default value is `false` .

**Settings**

> **Important:** When you access OpenAPI over HTTPS, the SDK enables SSL certificate validation by default. If your code environment does not have a certificate, a validation error occurs. To ensure secure communication in a production environment, keep this validation enabled. To ignore certificate validation in a test environment, use the following settings.

```
// Set HTTPSInsecure for the request (affects only the current request). request.SetHTTPSInsecure(true) // Set HTTPSInsecure for the re quest to true. isInsecure := request.GetHTTPSInsecure() // Get the HTTPSInsecure settin g for the request.
```

The client-level setting takes effect only if the request-level setting is not set.

```
// Set HTTPSInsecure for the client (affects all requests sent by the client). client.SetHTTPSInsecure(true) // Set HTTPSInsecure for the clien t to true. isInsecure := client.GetHTTPSInsecure() // Get the HTTPSInsecure setting f or the client.
```

## 3 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack API requests. Table 1: Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The format in which to return the response. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: If you call the API operations of the cloud service whose service code is Auditprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is yundunnextsoc, set the value to 2019-07-23. If you call the API operations of the cloud service whose service code is Sas, set the value to 2018-12-03. If you call the API operations of the cloud service whose service code is aegis, set the value to 2016-11-11. If you call the API operations of the cloud service whose service code is yundun-css, set the value to 2021-10-11. If you call the API operations of the cloud service whose service code is secspy, set the value to 2019-08-05. If you call the API operations of the cloud service whose service code is Ddosprivate, set the value to 2018-01-16. If you call the API operations of the cloud service whose service code is hsm-private, set the value to 2018-06-30. If you call the API operations of the cloud service whose service code is Cloudfw, set the value to 2017-12-07. If you call the API operations of the cloud service whose service code is Sddp, set the value to 2019-01-03. If you call the API operations of the cloud service whose service code is semawaf, set the value to 2020-07-01. If you call the API operations of the cloud service whose service code is soar, set the value to 2018-12-03. |
| AccessKeyId | Strin g | Yes | The AccessKey ID provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret provided by Apsara Stack. |

| RegionId | Strin g | Yes | The region ID of the service. |
|---|---|---|---|
| Product | Strin g | Yes | The code of the service to which the API operation belongs. Valid values: Auditprivate: the basic components of Apsara Stack Security. yundunnextsoc: Security Operations Center (SOC). Sas: Threat Detection Service. aegis: Server Guard. yundun-css: Container Protection. secspy: Network Detection and Response. Ddosprivate: Anti-DDoS. hsm-private: Cloud Hardware Security Module (HSM). Cloudfw: Cloud Firewall (CFW). Sddp: Sensitive Data Discovery and Protection (SDDP). semawaf: Web Application Firewall (WAF). soar: Security Orchestration and Automation Response (SOAR). |
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the API operation belongs. Valid values: auditprivate: the prefix in the endpoint of the basic components of Apsara Stack Security. yundunnextsoc-pop: the prefix in the endpoint of SOC. tds: the prefix in the endpoint of Threat Detection Service. aegis: the prefix in the endpoint of Server Guard. yundun-css: the prefix in the endpoint of Container Protection. secspy-share: the prefix in the endpoint of Network Detection and Response. ddosprivate: the prefix in the endpoint of Anti-DDoS. hsmprivate: the prefix in the endpoint of HSM. cloudfw: the prefix in the endpoint of CFW. sddp-api: the prefix in the endpoint of SDDP. semawaf: the prefix in the endpoint of WAF. soar: the prefix in the endpoint of SOAR. |

**Common response parameters**

Responses are returned in the unified format for API requests. The following HTTP status codes indicate different request states: A 2xx HTTP status code indicates a successful call. A 4xx or 5xx HTTP status code indicates a failed call. Responses are returned in the JSON format. Each response returns a unique request ID regardless of whether the call is successful.

## 4 DataBase Audit API reference

**reference**

### 4.1 Databases

#### 4.1.1 ListSupportDbTypesForDataSource

Queries a list of database types supported by Database Security Audit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListSupportDb TypesForDataS ource | The operation that you want to perform. Set the value to ListSupportDbTypesForDataSo urce. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| DbTypes | Array | None | The queried database types. |
| └ DbTypeName | String | Mysql | The name of the database type. |

| └ DbType | Integer | 3 | The code of the database type. Note The specific database type depends on the database type that you want to audit. You must specify the code of the database type when you add a database. |
|---|---|---|---|
| └ DbVersions | Array | None | The database versions. |
| └ DbVersionNa me | String | 5.7 | The name of the database version. |
| └ DbVersion | Integer | 5700 | The code of the database version. Note The specific database version depends on the database version that you want to audit. You must specify the code of the database version when you add a database. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ListSupportDbTypesForDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DbTypes":[
```

`{`

```json
            "DbVersions":[
```

`{`

```json
                    "DbVersion":5700,
                    "DbVersionName":"5.7"
```

`}` `],`

```json
            "DbType":3,
            "DbTypeName":"Mysql"
```

`}` `]` `}` `XML` format

```xml
<ListSupportDbTypesForDataSourceResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <DbTypes>
        <info>
            <DbTypeName>Mysql</DbTypeName>
            <DbType>3</DbType>
            <DbVersions>
                <info>
                    <DbVersionName>5.7</DbVersionName>
                    <DbVersion>5700</DbVersion>
                </info>
            </DbVersions>
        </info>
    </DbTypes>
</ListSupportDbTypesForDataSourceResponse>
```

#### 4.1.2 ListDataSources

Queries a list of databases to be audited.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ListDataSource s | The operation that you want to perform. Set the value to ListDataSources. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |

| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
|---|---|---|---|---|
| DbId | Integer | Yes | 1 | The database source ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| DataSources | Array | None | The queried databases. |
| └ DbId | Integer | 1 | The data source ID. |
| └ DbName | String | Platform Database | The name of the data source. |
| └ DbType | Integer | 3 | The code of the database type. |
| └ DbTypeName | String | Mysql | The name of the database type. |
| └ DbVersion | Integer | 5700 | The code of the database version. |
| └ DbVersionNa me | String | 5.7 | The name of the database version. |
| └ DbAddress | List | None | The address of the data source. |
| └ CreateTime | String | 2019-06-06 00:00:00 | The time when the data source was added. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ListDataSources &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DataSources":[
```

`{`

```json
            "DbVersion":5700,
            "CreateTime":"2019-06-06 00:00:00",
            "DbId":1,
            "DbName":"Platform Database",
            "DbVersionName":"5.7",
            "DbType":3,
            "DbTypeName":"Mysql"
```

`}` `]` `}` `XML` format

```xml
<ListDataSourcesResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <DataSources>
        <info>
            <DbId>1</DbId>
            <DbName>Platform Database</DbName>
            <DbType>3</DbType>
            <DbTypeName>Mysql</DbTypeName>
            <DbVersion>5700</DbVersion>
            <DbVersionName>5.7</DbVersionName>
            <DbAddresses>
                <info></info>
            </DbAddresses>
            <CreateTime>2019-06-06 00:00:00</CreateTime>
        </info>
    </DataSources>
</ListDataSourcesResponse>
```

#### 4.1.3 CreateDataSource

Adds a database to be audited.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateDataSou rce | The operation that you want to perform. Set the value to CreateDataSource. |

| RegionId | String | Yes | cn-hangzhou | The region ID. |
|---|---|---|---|---|
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbName | String | Yes | Platform Database | The name of the data source. |
| DbType | Integer | Yes | 32 | The database type of the data source. For more information, see ListSupportDbTypesForDataSourc e. |
| DbVersion | Integer | Yes | 6 | The database version of the data source. For more information, see ListSupportDbTypesForDataSourc e. |
| DbAddresses | String | Yes | 192.168.XX.XX | The IP address and port number of the data source. Separate multiple IP addresses and port numbers with commas (,). |

**Response parameters**

None.

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=CreateDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbName=Platform Database &DbType=32 &DbVersion=6 &DbAddresses=192.168.XX.XX
```

Sample success responses `JSON` format `{}` `XML` format

```xml
<CreateDataSourceResponse></CreateDataSourceResponse>
```

#### 4.1.4 ModifyDataSource

Modifies the information about an audited database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyDataSou rce | The operation that you want to perform. Set the value to ModifyDataSource. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbId | Integer | Yes | 1 | The database source ID. |
| DbName | String | Yes | Platform Database | The name of the data source. |
| DbVersion | Integer | Yes | 6 | The database version of the data source. For more information, see ListSupportDbTypesForDataSourc e. |
| DbAddresses | String | Yes | 192.168.XX.XX | The IP address and port number of the data source. Separate multiple IP addresses and port numbers with commas (,). |

**Response parameters**

None.

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=ModifyDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1 &DbName=Platform Database &DbVersion=6 &DbAddresses=192.168.XX.XX
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "DataSources":[
```

`{`

```json
            "DbVersion":5700,
            "CreateTime":"2019-06-06 00:00:00",
            "DbId":1,
            "DbName":"Platform Database",
            "DbVersionName":"5.7",
            "DbType":3,
            "DbTypeName":"Mysql"
```

`}` `]` `}` {} `XML` format

```xml
<ModifyDataSourceResponse></ModifyDataSourceResponse>
```

#### 4.1.5 DeleteDataSource

Removes a data source from Database Security Audit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteDataSou rce | The operation that you want to perform. Set the value to DeleteDataSource. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbId | Integer | Yes | 1 | The database source ID. |

**Response parameters**

None.

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=DeleteDataSource &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

Sample success responses `JSON` format `{}` `XML` format

```xml
<DeleteDataSourceResponse></DeleteDataSourceResponse>
```

### 4.2 Agents

#### 4.2.1 GetAgentList

Queries a list of installed agents.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetAgentList | The operation that you want to perform. Set the value to GetAgentList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| AgentIp | String | No | 192.168.XX.XX | The IP address of the agent. |

| AgentStatus | String | No | 0 | The state of the agent. Valid values: 0: all. 1: normal. 2: suspending. 3: actively suspended. 4: suspended due to timeout. 5: awakening. 6: interrupting. 7: interrupted. 8: abnormal. 9: abnormal version. 10: authenticating. 12: configuring. 13: upgrading. 14: upgrade failed. 15: upgrade timed out. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| AgentList | Array | None | The queried agents. |
| └ AgentIp | String | 192.168.XX.XX | The IP address of the agent. |
| └ AgentOs | String | redhat6 | The OS type of the agent. |
| └ AgentVersio n | String | 3.2.5.3 | The version of the agent. |
| └ AgentCpu | String | 3 | The CPU utilization (%) of the agent. |
| └ AgentMem | String | 3 | The memory usage (%) of the agent. |

| └ SendPacketC ount | String | 10000 | The total number of packets sent by the agent. |
|---|---|---|---|
| └ SendPackets | String | 100 | The packet rate of the agent. Unit: packets per second. |
| └ AgentStatus | String | 1 | The state of the agent. Valid values: 0: all. 1: normal. 2: suspending. 3: actively suspended. 4: suspended due to timeout. 5: awakening. 6: interrupting. 7: interrupted. 8: abnormal. 9: abnormal version. 10: authenticating. 12: configuring. 13: upgrading. 14: upgrade failed. 15: upgrade timed out. |
| └ FirstLoginTi me | String | 2020-09-01 00:00:00 | The time when the agent first logged in. |
| └ LastActiveTi me | String | 2020-09-02 00:00:00 | The last time when the agent sent packets. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetAgentList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &AgentIp=192.168.XX.XX &AgentStatus=0
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "AgentList":[
```

`{`

```json
            "AgentOs":"redhat6",
            "AgentStatus":"1",
            "AgentVersion":"3.2.5.3",
            "AgentIp":"192.168.XX.XX",
            "AgentCpu":"3",
            "LastActiveTime":"2020-09-01 00:00:00",
            "SendPackets":"100",
            "AgentMem":"3",
            "SendPacketCount":"10000",
            "FirstLoginTime":"2020-09-01 00:00:00"
```

`}` `]` `}` `XML` format

```xml
<GetAgentListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <AgentList>
        <info>
            <AgentIp>192.168.194.185</AgentIp>
            <AgentOs>redhat6</AgentOs>
            <AgentVersion>3.2.5.3</AgentVersion>
            <AgentCpu>3</AgentCpu>
            <AgentMem>3</AgentMem>
            <SendPacketCount>10000</SendPacketCount>
            <SendPackets>100</SendPackets>
            <AgentStatus>1</AgentStatus>
            <FirstLoginTime>2020-09-01 00:00:00</FirstLoginTime>
            <LastActiveTime>2020-09-01 00:00:00</LastActiveTime>
        </info>
    </AgentList>
</GetAgentListResponse>
```

**Error codes**

For a list of error codes, see Error codes.

### 4.3 Risk identification rules

#### 4.3.1 GetRuleList

Queries a list of rules contained in each rule group of Database Security Audit.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRuleList | The operation that you want to perform. Set the value to GetRuleList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| RuleGroupLis t | Array | None | The queried rule groups. |
| └ GroupId | Integer | 1001 | The rule group ID. |
| └ GroupName | String | Rule Group 1 | The name of the rule group. |
| └ RuleList | Array | None | The rules in the rule group. |
| └ RuleId | Integer | 2000001 | The rule ID. |
| └ RuleName | String | Batch Deletion | The name of the rule. |
| └ RiskLevel | Integer | 3 | The level of the risk that triggers the rule. |
| └ RiskType | Integer | 5 | The type of the risk that triggers the rule. |
| └ SysDefn | Integer | 0 | Indicates whether the rule is a system default rule. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRuleList &RegionId=cn-hangzhou &InstanceId=dbaudit-****
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "RuleGroupList":[
```

`{`

```json
            "GroupName":"Rule Group 1",
            "RuleList":[
```

`{`

```json
                    "SysDefn":"0",
                    "RuleId":"2000001",
                    "RiskLevel":"3",
                    "RuleName":"Batch Deletion",
                    "RiskType":"5"
```

`}` `],`

```json
            "GroupId":"1001"
```

`}` `]` `}` `XML` format

```xml
<GetRuleListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <RuleGroupList>
        <info>
            <GroupId>1001</GroupId>
            <GroupName>Rule Group 1</GroupName>
            <RuleList>
                <info>
                    <RuleId>2000001</RuleId>
                    <RuleName>Batch Deletion</RuleName>
                    <RiskLevel>3</RiskLevel>
                    <RiskType>5</RiskType>
                    <SysDefn>0</SysDefn>
                </info>
            </RuleList>
        </info>
    </RuleGroupList>
</GetRuleListResponse>
```

#### 4.3.2 EnableRulesForThisDB

Enables rules for a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableRulesFor ThisDB | The operation that you want to perform. Set the value to EnableRulesForThisDB. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbId | Integer | Yes | 1 | The database ID. |
| RuleIds | String | Yes | 94,106 | The rule IDs. Separate multiple rule IDs with commas (,). |

**Response parameters**

None.

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=EnableRulesForThisDB &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1 &RuleIds=94,106
```

Sample success responses `JSON` format `{}` `XML` format

```xml
<EnableRulesForThisDBResponse></EnableRulesForThisDBResponse>
```

#### 4.3.3 DisableRulesForThisDB

Disables rules for a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableRulesFo rThisDB | The operation that you want to perform. Set the value to DisableRulesForThisDB. |

| RegionId | String | Yes | cn-hangzhou | The region ID. |
|---|---|---|---|---|
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbId | Integer | Yes | 1 | The database ID. |
| RuleIds | String | Yes | 94,106 | The rule IDs. Separate multiple rule IDs with commas (,). |

**Response parameters**

None.

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=DisableRulesForThisDB &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1 &RuleIds=94,106
```

Sample success responses `JSON` format `{}` `XML` format

```xml
<DisableRulesForThisDBResponse></DisableRulesForThisDBResponse>
```

### 4.4 Audit

#### 4.4.1 GetDBAuditCount

Queries the audit statistics of a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetDBAuditCo unt | The operation that you want to perform. Set the value to GetDBAuditCount. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| DbId | String | Yes | 1 | The database ID. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| AuditInfo | Struct | None | The queried audit statistics. |
| └ RunTime | Long | 10000 | The duration of the audit. Unit: milliseconds. |
| └ AuditCount | Long | 20000 | The total number of audited statements. |
| └ SqlCount | Long | 15000 | The number of queried online statements. |
| └ CurrentSqlCo unt | Long | 30000 | The number of statements today. |
| └ CurrentSessi onCount | Long | 40000 | The number of sessions today. |
| └ CurrentFailS essionCount | Long | 10000 | The number of failed sessions today. |
| └ CurrentRiskC ount | Long | 10000 | The number of risks today. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetDBAuditCount &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &DbId=1
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "AuditInfo":{
        "SqlCount":10000,
        "CurrentSqlCount":20000,
        "AuditCount":15000,
        "RunTime":30000,
        "CurrentSessionCount":40000,
        "CurrentFailSessionCount":10000,
        "CurrentRiskCount":10000
```

`}` `}` `XML` format

```xml
<GetDBAuditCountResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <AuditInfo>
        <RunTime>10000</RunTime>
        <AuditCount>20000</AuditCount>
        <SqlCount>15000</SqlCount>
        <CurrentSqlCount>30000</CurrentSqlCount>
        <CurrentSessionCount>40000</CurrentSessionCount>
        <CurrentFailSessionCount>10000</CurrentFailSessionCount>
        <CurrentRiskCount>10000</CurrentRiskCount>
    </AuditInfo>
</GetDBAuditCountResponse>
```

#### 4.4.2 GetAuditSearchList

Queries a list of audit logs generated for SQL statements that are executed to connect a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetAuditSearc hList | The operation that you want to perform. Set the value to GetAuditSearchList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| PageNumber | Integer | Yes | 1 | The page number. |
| PageSize | Integer | Yes | 50 | The number of entries per page. Default value: 50. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |
| ClientIps | String | No | 192.168.XX.XX | The IP address of the client. Separate multiple IP addresses with commas (,). |
| DbUsers | String | No | root | The name of the database user. Separate multiple names with commas (,). |

| RiskLevels | String | No | 1 | The level of the risk. Separate multiple risk levels with commas (,). Valid values: 1: low risk. 3: medium risk. 5: high risk. |
|---|---|---|---|---|
| KeyWords | String | No | select,update | The keywords. Separate multiple keywords with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| ApiAuditSear chResult | Struct | None | The queried results. |
| └ FinalSize | Integer | 10000 | The total number of entries returned. The maximum value is 10000. |
| └ Data | Array | None | The logs. |
| └ Logsecquenc e | String | 162183812690744 01037 | The keyword of the log. |
| └ Dbid | String | 1 | The database ID. |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | The SQL statement. |
| └ Capturetime | String | 2020-05-24 14:17:26 | The time when the SQL statement was captured. |
| └ Dbserver | String | 100.100.XX.XX | The IP address of the database. |
| └ Serverport | String | 3306 | The port number of the database. |
| └ Dbuser | String | root | The name of the database user. |
| └ Dbclient | String | 192.168.XX.XX | The IP address of the client. |
| └ Responsecod e | Integer | 0 | The response code. |
| └ Responsetex t | String | None | The execution results. |
| └ Affectrows | String | 100 | The number of affected rows. |
| └ Execcostus | String | 323 | The response time. Unit: microseconds. |

| └ Fetchcostus | String | 323 | The execution duration of the SQL statement. Unit: microseconds. |
|---|---|---|---|
| └ Clientmac | String | 0EB6EF12**** | The Media Access Control (MAC) address of the client. |
| └ Programnm | String | libmysql | The tool or application. |
| └ Sid | String | test | The name of the OS user. |
| └ Machinenam e | String | compute-internal | The hostname. |
| └ Sessionid | String | 106288711982206 1570 | The session ID. |
| └ Logintime | String | 2020-05-24 14:17:15 | The time when the session started. |
| └ Logouttime | String | 2020-05-24 15:05:27 | The time when the session ended. |
| └ RiskLevel | String | 1 | The level of the risk. Separate multiple risk levels with commas (,). Valid values: 1: low risk. 3: medium risk. 5: high risk. |
| └ Appusernam e | String | user1 | The name of the application user. |
| └ Appclientip | String | 111.164.XX.XX | The IP address of the application client. |
| └ DbName | String | SCHEMA | The name of the database. |
| └ Dbinstancen ame | String | INS | The name of the Database Security Audit instance instance. |
| └ Dbsessionid | String | 0E320477 | The session ID of the database. |
| └ RelatedRule Name | String | Trusted Statement | The rule of the SQL statement. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetAuditSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &RiskLevels=1,3,5 &KeyWords=select,update
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiAuditSearchResult":{
        "FinalSize":10000,
        "Data":[
```

`{`

```json
                "Dbsessionid":"0E320477",
                "Machinename":"compute-internal",
                "Dbuser":"root",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:17:15",
                "Logouttime":"2020-05-24 15:05:27",
                "Dbserver":"100.100.XX.XX",
                "Responsecode":"0",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "DbName":"SCHEMA",
                "Appusername":"user1",
                "Dbinstancename":"INS",
                "RelatedRuleName":"Trusted Statement",
                "Capturetime":"2020-05-24 14:17:26",
                "Execcostus":"323",
                "Fetchcostus":"323",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Affectrows":"100",
                "Appclientip":"111.164.XX.XX",
                "Sessionid":"0E320477",
                "RiskLevel":"1"
```

`}` `]` `}` `}` `XML` format

```xml
<GetAuditSearchListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiAuditSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsecode>0</Responsecode>
                <Responsetext></Responsetext>
                <Affectrows>100</Affectrows>
                <Execcostus>323</Execcostus>
                <Fetchcostus>323</Fetchcostus>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Machinename>compute-internal</Machinename>
                <Sessionid>1062887119822061570</Sessionid>
                <Logintime>2020-05-24 14:17:15</Logintime>
                <Logouttime>2020-05-24 15:05:27</Logouttime>
                <RiskLevel>0</RiskLevel>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <DbName>SCHEMA</DbName>
                <Dbinstancename>INS</Dbinstancename>
                <Dbsessionid>0E320477</Dbsessionid>
                <RelatedRuleName>Trusted Statement</RelatedRuleName>
            </info>
        </Data>
    </ApiAuditSearchResult>
</GetAuditSearchListResponse>
```

#### 4.4.3 GetFailedSqlList

Queries a list of SQL statements that failed to connect to a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetFailedSqlLis t | The operation that you want to perform. Set the value to GetFailedSqlList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |

| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
|---|---|---|---|---|
| PageNumber | Integer | Yes | 1 | The page number. |
| PageSize | Integer | Yes | 50 | The number of entries per page. Default value: 50. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |
| ClientIps | String | No | 192.168.XX.XX | The IP address of the client. Separate multiple IP addresses with commas (,). |
| DbUsers | String | No | root | The name of the database user. Separate multiple names with commas (,). |
| AckNum | Integer | No | 100002 | The error code. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| ApiAuditSear chResult | Struct | None | The queried results. |
| └ FinalSize | Integer | 10000 | The total number of entries returned. The maximum value is 10000. |
| └ Data | Array | None | The logs. |
| └ Logsecquenc e | String | 162183812690744 01037 | The keyword of the log. |
| └ Dbid | String | 1 | The database ID. |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | The SQL statement. |
| └ Capturetime | String | 2020-05-24 14:17:26 | The time when the SQL statement was captured. |
| └ Dbserver | String | 100.100.XX.XX | The IP address of the database. |
| └ Serverport | String | 3306 | The port number of the database. |

| └ Dbuser | String | root | The name of the database user. |
|---|---|---|---|
| └ Dbclient | String | 192.168.XX.XX | The IP address of the client. |
| └ Responsecod e | Integer | 1001 | The response code. |
| └ Responsetex t | String | Table G STATUS _ doesn't exist | The execution results. |
| └ Clientmac | String | 0EB6EF124C47 | The Media Access Control (MAC) address of the client. |
| └ Programnm | String | libmysql | The tool or application. |
| └ Sid | String | test | The name of the OS user. |
| └ Sessionid | String | 106288711982206 1570 | The session ID. |
| └ Logintime | String | 2020-05-24 14:17:15 | The time when the session started. |
| └ Logouttime | String | 2020-05-24 15:05:27 | The time when the session ended. |
| └ Appusernam e | String | user1 | The name of the application user. |
| └ Appclientip | String | 111.164.XX.XX | The IP address of the application client. |
| └ DbName | String | SCHEMA | The name of the database. |
| └ Dbinstancen ame | String | INS | The name of the Database Security Audit instance instance. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetFailedSqlList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &AckNum=100002
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiAuditSearchResult":{
        "FinalSize":10000,
        "Data":[
```

`{`

```json
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"Table G_STATUS doesn't exist",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:17:15",
                "Logouttime":"2020-05-24 15:05:27",
                "Dbserver":"100.100.XX.XX",
                "Responsecode":"1001",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "DbName":"SCHEMA",
                "Appusername":"user1",
                "Appclientip":"111.164.XX.XX",
                "Dbinstancename":"INS",
                "Capturetime":"2020-05-24 14:17:26",
                "Sessionid":"1062887119822061570"
```

`}` `]` `}` `}` `XML` format

```xml
<GetFailedSqlListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiAuditSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <Dbserver>100.100.100.81</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsecode>1001</Responsecode>
                <Responsetext>Table G_STATUS doesn't exist</Responsetext>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Sessionid>1062887119822061570</Sessionid>
                <Logintime>2020-05-24 14:17:15</Logintime>
                <Logouttime>2020-05-24 15:05:27</Logouttime>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <DbName>SCHEMA</DbName>
                <Dbinstancename>INS</Dbinstancename>
            </info>
        </Data>
    </ApiAuditSearchResult>
</GetFailedSqlListResponse>
```

#### 4.4.4 GetSessionSearchList

Queries a list of sessions that are established to connect to a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetSessionSea rchList | The operation that you want to perform. Set the value to GetSessionSearchList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| PageNumber | Integer | Yes | 1 | The page number. |
| PageSize | Integer | Yes | 50 | The number of entries per page. Default value: 50. |
| Dbid | String | Yes | 1 | The database ID. |

| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
|---|---|---|---|---|
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |
| ClientIps | String | No | 192.168.XX.XX | The IP address of the client. Separate multiple IP addresses with commas (,). |
| DbUsers | String | No | root | The name of the database user. Separate multiple names with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| ApiAuditSear chResult | Struct | None | The queried results. |
| └ FinalSize | Integer | 10000 | The total number of entries returned. The maximum value is 10000. |
| └ Data | Array | None | The logs. |
| └ Sessionid | String | 106288711982206 1570 | The keyword of the log. |
| └ Dbserver | String | 100.100.XX.XX | The IP address of the database. |
| └ Serverport | String | 3306 | The port number of the database. |
| └ Dbuser | String | root | The name of the database user. |
| └ Dbclient | String | 192.168.XX.XX | The IP address of the client. |
| └ Clientmac | String | 0EB6EF12**** | The Media Access Control (MAC) address of the client. |
| └ Programnm | String | libmysql | The tool or application. |
| └ Sid | String | test | The name of the OS user. |
| └ Logintime | String | 2020-05-24 14:00:00 | The time when the session started. |
| └ Logouttime | String | 2020-05-24 15:00:00 | The time when the session ended. |
| └ Statetime | String | 60 | The duration of the session. Unit: minutes. |
| └ Dback | String | 0 | The error code. |

| └ Dbackmessa ge | String | None | The login information. |
|---|---|---|---|

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetSessionSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiSessionSearchResult":{
        "FinalSize":10000,
        "Data":[
```

`{`

```json
                "Dback":"0",
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Serverport":"3306",
                "Sid":"test",
                "Clientmac":"0EB6EF124C47",
                "Programnm":"libmysql",
                "Logintime":"2020-05-24 14:00:00",
                "Logouttime":"2020-05-24 15:00:00",
                "Statetime":"60",
                "Dbackmessage":"",
                "Dbserver":"100.100.XX.XX",
                "Sessionid":"1062887119822061570"
```

`}` `]` `}` `}` `XML` format

```xml
<GetSessionSearchListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiSessionSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Sessionid>1062887119822061570</Sessionid>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Clientmac>0EB6EF124C47</Clientmac>
                <Programnm>libmysql</Programnm>
                <Sid>test</Sid>
                <Logintime>2020-05-24 14:00:00</Logintime>
                <Logouttime>2020-05-24 15:00:00</Logouttime>
                <Statetime>60</Statetime>
                <Dback>0</Dback>
                <Dbackmessage></Dbackmessage>
            </info>
        </Data>
    </ApiSessionSearchResult>
</GetSessionSearchListResponse>
```

#### 4.4.5 GetFailedSessionList

Queries a list of sessions that failed to log in to a database.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetFailedSessi onList | The operation that you want to perform. Set the value to GetFailedSessionList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| PageNumber | Integer | Yes | 1 | The page number. |
| PageSize | Integer | Yes | 50 | The number of entries per page. Default value: 50. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |

| ClientIps | String | No | 192.168.XX.XX | The IP address of the client. Separate multiple IP addresses with commas (,). |
|---|---|---|---|---|
| DbUsers | String | No | root | The name of the database user. Separate multiple names with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| SessionList | Array | None | The queried sessions. |
| └ Sessionid | String | 106288711982206 1570 | The keyword of the session. |
| └ Dbserver | String | 100.100.XX.XX | The IP address of the database. |
| └ Serverport | String | 3306 | The port number of the database. |
| └ Dbuser | String | root | The name of the database user. |
| └ Dbclient | String | 192.168.XX.XX | The IP address of the client. |
| └ Clientmac | String | 0EB6EF12**** | The Media Access Control (MAC) address of the client. |
| └ Programnm | String | libmysql | The tool or application. |
| └ Sid | String | test | The name of the OS user. |
| └ Connecttime | String | 2020-05-24 14:00:00 | The time when the session was established. |
| └ Dback | String | 1045 | The error code. |
| └ Dbackmessa ge | String | Access denied for user 'root'@ (using password: YES) | The login information. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetFailedSessionList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "SessionList":[
```

`{`

```json
            "Clientmac":"0EB6EF12****",
            "Programnm":"libmysql",
            "Dbackmessage":"Access denied for user 'root'@ (using password: YES)",
            "Dbserver":"100.100.XX.XX",
            "Dback":"1045",
            "Dbuser":"root",
            "Dbclient":"192.168.XX.XX",
            "Sessionid":"1062887119822061570",
            "Serverport":"3306",
            "Connecttime":"2020-05-24 14:00:00",
            "Sid":"test"
```

`}` `]` `}` `XML` format

```xml
<GetFailedSessionListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <SessionList>
        <info>
            <Sessionid>1062887119822061570</Sessionid>
            <Dbserver>100.100.XX.XX</Dbserver>
            <Serverport>3306</Serverport>
            <Dbuser>root</Dbuser>
            <Dbclient>192.168.XX.XX</Dbclient>
            <Clientmac>0EB6EF12****</Clientmac>
            <Programnm>libmysql</Programnm>
            <Sid>test</Sid>
            <Connecttime>2020-05-24 14:00:00</Connecttime>
            <Dback>1045</Dback>
            <Dbackmessage>Access denied for user 'root'@ (using password: YES)
</Dbackmessage>
        </info>
    </SessionList>
</GetFailedSessionListResponse>
```

#### 4.4.6 GetRiskSqlSearchList

Queries a list of risky SQL statements.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRiskSqlSear chList | The operation that you want to perform. Set the value to GetRiskSqlSearchList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| PageNumber | Integer | Yes | 1 | The page number. Default value: 1. |
| PageSize | Integer | Yes | 50 | The number of entries per page. Default value: 50. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |
| ClientIps | String | No | 192.168.XX.XX | The IP address of the client. Separate multiple IP addresses with commas (,). |

| DbUsers | String | No | root | The name of the database user. Separate multiple names with commas (,). |
|---|---|---|---|---|
| RiskLevels | String | No | 1 | The risk level of the SQL statement. Separate multiple risk levels with commas (,). Valid values: 1: low risk. 3: medium risk. 5: high risk. |
| RiskTypes | String | No | 5 | The risk type of the SQL statement. Separate multiple risk types with commas (,). Valid values: 2: sensitive statement. 3: SQL injection. 4: vulnerability attack. 5: operation rule. 6: access rule. 7: password attack. |
| RuleName | String | No | Batch Query Rule 1 | The name of the risk rule that is hit by the SQL statement. |
| ExcuteResult | String | No | 0 | The execution result of the SQL statement. Valid values: 0: failed. 1: successful. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| ApiAuditSear chResult | Struct | None | The queried results. |
| └ FinalSize | Integer | 10000 | The total number of entries returned. The maximum value is 10000. |
| └ Data | Array | None | The logs. |
| └ Logsecquenc e | String | 162183812690744 01037 | The keyword of the log. |
| └ Dbid | String | 1 | The database ID. |
| └ Writeprepare dsql | String | SELECT*FROM G STATUS LIMIT _ 0,1000 | The SQL statement. |

| └ Capturetime | String | 2020-05-24 14:17:26 | The time when the query was performed. |
|---|---|---|---|
| └ RiskType | String | 5 | The risk type of the SQL statement. Separate multiple risk types with commas (,). Valid values: 2: sensitive statement. 3: SQL injection. 4: vulnerability attack. 5: operation rule. 6: access rule. 7: password attack. |
| └ RuleName | String | Batch Query Rule 1 | The name of the risk rule that is hit by the SQL statement. |
| └ RiskLevel | String | 1 | The risk level of the SQL statement. Separate multiple risk levels with commas (,). Valid values: 1: low risk. 3: medium risk. 5: high risk. |
| └ Dbserver | String | 100.100.XX.XX | The IP address of the database. |
| └ Serverport | String | 3306 | The port number of the database. |
| └ Dbuser | String | root | The name of the database user. |
| └ Dbclient | String | 192.168.XX.XX | The IP address of the client. |
| └ Responsetex t | String | 0 | The execution result of the SQL statement. Valid values: 0: failed. 1: successful. |
| └ Affectrows | String | 1000 | The number of rows affected by the SQL statement. |
| └ Programnm | String | libmysql | The tool used to connect to the database. |
| └ Appusernam e | String | user1 | The name of the application user. |
| └ Appclientip | String | 111.164.XX.XX | The IP address of the application client. |
| └ Dbinstancen ame | String | INS | The name of the Database Security Audit instance instance. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRiskSqlSearchList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &PageNumber=1 &PageSize=50 &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &ClientIps=192.168.XX.XX &DbUsers=root &RiskLevels=1,3,5 &RiskTypes=5 &RuleName=Batch Query Rule 1 &ExcuteResult=0
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiRiskSearchResult":{
        "FinalSize":10000,
        "Data":[
```

`{`

```json
                "Dbuser":"root",
                "Dbclient":"192.168.XX.XX",
                "Responsetext":"",
                "Serverport":"3306",
                "Writepreparedsql":"SELECT*FROM G_STATUS LIMIT 0,1000",
                "Programnm":"libmysql",
                "Affectrows":"1000",
                "Dbserver":"100.100.100.81",
                "Logsecquence":"16218381269074401037",
                "Dbid":"1",
                "Appusername":"user1",
                "Appclientip":"111.164.XX.XX",
                "Dbinstancename":"INS",
                "Capturetime":"2020-05-24 14:17:26",
                "RiskLevel":"1",
                "RiskType":"5",
                "RuleName":"Batch Query Rule 1"
```

`}` `]` `}` `}` `XML` format

```xml
<GetRiskSqlSearchListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiRiskSearchResult>
        <FinalSize>10000</FinalSize>
        <Data>
            <info>
                <Logsecquence>16218381269074401037</Logsecquence>
                <Dbid>1</Dbid>
                <Writepreparedsql>SELECT*FROM G_STATUS LIMIT 0,1000</Writepreparedsql>
                <Capturetime>2020-05-24 14:17:26</Capturetime>
                <RiskType>5</RiskType>
                <RuleName>Batch Query Rule 1</RuleName>
                <RiskLevel>1</RiskLevel>
                <Dbserver>100.100.XX.XX</Dbserver>
                <Serverport>3306</Serverport>
                <Dbuser>root</Dbuser>
                <Dbclient>192.168.XX.XX</Dbclient>
                <Responsetext>0</Responsetext>
                <Affectrows>1000</Affectrows>
                <Programnm>libmysql</Programnm>
                <Appusername>user1</Appusername>
                <Appclientip>111.164.XX.XX</Appclientip>
                <Dbinstancename>INS</Dbinstancename>
            </info>
        </Data>
    </ApiRiskSearchResult>
</GetRiskSqlSearchListResponse>
```

#### 4.4.7 GetRiskBitsList

Queries the statistics of hit risk rules.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | GetRiskBitsList | The operation that you want to perform. Set the value to GetRiskBitsList. |
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |

| RiskLevel | String | No | 5 | The level of the risk. Valid values: 1: low risk. 3: medium risk. 5: high risk. |
|---|---|---|---|---|
| RiskType | String | No | 5 | The type of the risk. Valid values: 2: sensitive statement. 3: SQL injection. 4: vulnerability attack. 5: operation rule. 6: access rule. 7: password attack. |
| RuleName | String | No | Batch Deletion Rule 1 | The name of the rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| ApiRiskHitLis t | Array | None | The hit risk rules. |
| └ RuleId | String | 2000001 | The rule ID. |
| └ RuleName | String | Batch Deletion Rule 1 | The name of the rule. |
| └ RiskType | String | 5 | The type of the risk. Separate multiple risk types with commas (,). Valid values: 2: sensitive statement. 3: SQL injection. 4: vulnerability attack. 5: operation rule. 6: access rule. 7: password attack. |
| └ RiskLevel | String | 1 | The level of the risk. Separate multiple risk levels with commas (,). Valid values: 1: low risk. 3: medium risk. 5: high risk. |
| └ HitCount | String | 35 | The number of risks. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetRiskBitsList &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &Dbid=1 &StartTime=2020-01-01 00:00:00 &EndTime=2020-01-01 23:59:59 &RiskLevel=5 &RiskType=5 &RuleName=Batch Deletion Rule 1
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "ApiRiskHitList":[
```

`{`

```json
            "HitCount":"35",
            "RuleId":"2000001",
            "RiskLevel":"1",
            "RuleName":"Batch Deletion Rule 1",
            "RiskType":"5"
```

`}` `]` `}` `XML` format

```xml
<GetRiskBitsListResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <ApiRiskHitList>
        <info>
            <RuleId>2000001</RuleId>
            <RuleName>Batch Deletion Rule 1</RuleName>
            <RiskType>5</RiskType>
            <RiskLevel>1</RiskLevel>
            <HitCount>35</HitCount>
        </info>
    </ApiRiskHitList>
</GetRiskBitsListResponse>
```

#### 4.4.8 GetApiSearchConditionResult

Queries the conditions that can be used to query SQL statements.

**Request parameters**

| Parameter | Type | Required | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | GetApiSearchC onditionResult | The operation that you want to perform. Set the value to GetApiSearchConditionResult. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-hangzhou | The region ID. |
| InstanceId | String | Yes | dbaudit-**** | The Database Security Audit instance ID. |
| Dbid | String | Yes | 1 | The database ID. |
| StartTime | String | No | 2020-01-01 00:00:00 | The beginning of the time range to query. |
| EndTime | String | No | 2020-01-01 23:59:59 | The end of the time range to query. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 53e59af3-3209- 452a-853c- ac10ad815929 | The request ID. |
| Conditions | Struct | None | The queried results. |
| └ DbClientList | List | 192.168.XX.XX | The client IP addresses. |
| └ DbUserList | List | root | The names of database users. |

**Examples**

Sample requests

```
https://dbauditprivate.[RegionId].aliyuncs.com/?Action=GetApiSearchConditionResult &RegionId=cn-hangzhou &InstanceId=dbaudit-**** &Dbid=1
```

Sample success responses `JSON` format `{`

```json
    "RequestId":"53e59af3-3209-452a-853c-ac10ad815929",
    "Conditions":[
```

`{`

```json
        "DbClientList":"192.168.XX.XX",
        "DbUserList":"root",
```

`}` `}` `XML` format

```xml
<GetApiSearchConditionResultResponse>
    <RequestId>53e59af3-3209-452a-853c-ac10ad815929</RequestId>
    <Conditions>
        <DbClientList>
            <info>192.168.XX.XX</info>
        </DbClientList>
        <DbUserList>
            <info>root</info>
        </DbUserList>
    </Conditions>
</GetApiSearchConditionResultResponse>
```

## 5 Error codes

This topic describes the error codes returned for API operations in Apsara Stack Security. Table 1: Common error codes of Apsara Stack Security

| Error code | Error message | Solution |
|---|---|---|
| yd.error.all.10001 | You do not have the required permissions. | Check your account permissions. |
| yd.error.all.10002 | A system error has occurred. | Try again later. |
| yd.error.all.10003 | One or more parameters are invalid. | Check the request parameters and try again. |
| yd.error.all.other | A system error has occurred. | Try again later. |
| yd.error.all.ConsoleSystemError 1001 _ | An unknown error has occurred. | Try again later. |
| yd.error.all.ConsoleSystemError 1007 _ | The specified API operation is unpublished. | Contact Apsara Stack technical support. |
| yd.error.all.ConsoleSystemError 1008 _ | Failed to verify the postOnly parameter. | Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1009 _ | The csrfToken parameter is not specified. | Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1010 _ | Failed to verify the csrfToken parameter. | Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1011 _ | The regionId parameter is not specified. | Check the regionId parameter. |
| yd.error.all.ConsoleSystemError 1012 _ | The specified regionId parameter is invalid. | Check the regionId parameter. |
| yd.error.all.ConsoleSystemError 1013 _ | One or more parameters are not specified. | Check the request parameters and try again. |
| yd.error.all.ConsoleSystemError 1014 _ | One or more parameters are invalid. | Check the request parameters and try again. |
| yd.error.all.ConsoleNeedLogin | You have not logged in. | Check your account permissions. |
| yd.error.all.InvalidApi | An operation exception has occurred. | Try again later. |
| yd.error.all.InvalidParameter | One or more parameters are invalid. | Check the request parameters and try again. |
| yd.error.all.InvalidResult | One or more return values are invalid. | Try again later. |
| yd.error.all.PropertyConvertFail ed | An error occurred during conversion. | Try again later. |

| yd.error.all.NoPermission | You do not have the required permissions. | Check your account permissions. |
|---|---|---|
| yd.error.all.ServerError | A server error has occurred. | Try again later or contact Apsara Stack technical support. |
| yd.error.all.UnkownError | An unknown error has occurred. | Try again later or contact Apsara Stack technical support. |

Table 2: Error codes of Threat Detection Service

| Error code | Error message | Solution |
|---|---|---|
| yd.error.sas.1 | The specified parameter does not exist in the metadata. | Check the request parameters and try again. |
| yd.error.sas.2 | Failed to call the task engine. | Try again later. |
| yd.error.sas.3 | Failed to start the task. | Try again later. |
| yd.error.sas.4 | Failed to stop the task. | Try again later. |
| yd.error.sas.5 | Failed to restart the task. | Try again later. |
| yd.error.sas.6 | Failed to obtain the task status. | Try again later. |
| yd.error.sas.7 | Failed to delete the task. | Try again later. |
| yd.error.sas.8 | The specified table does not contain metadata. | Check the request parameters and try again. |
| yd.error.sas.100 | The request failed. | Try again later. |
| yd.error.sas.101 | One or more parameters are invalid. | Check the request parameters and try again. |
| yd.error.sas.103 | The request failed. | Try again later. |
| yd.error.sas.400 | The asset is under protection. | Uninstall the Server Guard agent and try again. |
| yd.error.sas.500 | A system error has occurred. | Contact Apsara Stack technical support. |
| yd.error.sas.501 | The feature is not available in the current version. | N/A |
| yd.error.sas.502 | You are not authorized to access the server. | N/A |

Table 3: Error codes of Anti-DDoS

| Error code | Error message | Solution |
|---|---|---|
| yd.error.ddos.400 | An error occurred while accessing the server. | Check the request parameters and try again. |
| yd.error.ddos.500 | A server error has occurred. | Contact Apsara Stack technical support. |

| yd.error.ddos.UNKNOWN EXCE _ PTION | An unknown error has occurred. | Contact Apsara Stack technical support. |
|---|---|---|
| yd.error.ddos.REQUEST TIMEO _ UT | The request timed out. | Try again later. |
| yd.error.ddos.SERVER FAILED _ | The operation failed. | Contact Apsara Stack technical support. |
| yd.error.ddos.NOT AUTHORIZE _ D | You do not have the required permissions. | Check your account permissions. |
| yd.error.ddos.PARAMETER INVA _ LID | One or more parameters are invalid or are not specified. | Check the request parameters and try again. |
| yd.error.ddos.IP SEGMENT INV _ _ ALID | The specified CIDR block is invalid. | Check the CIDR block specified in the request parameters. |
| yd.error.ddos.IP SEGMENT REP _ _ EAT | A CIDR block cannot be used in different regions. | Check the CIDR block specified in the request parameters. |
| yd.error.ddos.IP SEGMENT ALR _ _ EADY | The CIDR block already exists. | Check the CIDR block specified in the request parameters. |
| yd.error.ddos.IP SEGMENT MAS _ _ K LENGTH ERR _ _ | The mask can be up to 24 bits in length. | Check the mask of the CIDR block specified in the request parameters. |
| yd.error.ddos.QUERY REGION L _ _ IST ERR _ | Failed to obtain the region list. | Try again later. |
| yd.error.ddos.IP SEGMENT OPE _ _ RATION ERR _ | Failed to process the CIDR block. | Try again later. |
| yd.error.ddos.QUERY IP SEGME _ _ NT ERR _ | Failed to obtain the CIDR block. | Try again later. |
| yd.error.ddos.MODIFY IP SEGM _ _ ENT ERR _ | Failed to modify the CIDR block. | Try again later. |
| yd.error.ddos.IP SEGMENT TYP _ _ E ERR _ | The type of the CIDR block (internal or external) is not specified. | Check the type of the CIDR block and try again. |
| yd.error.ddos.CANCEL FLOW C _ _ LEAN ERR _ | Failed to cancel traffic scrubbing. | Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY FLOW AN _ _ ALYSIS ERR _ | Failed to obtain the traffic analysis result. | Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY BEAVER _ _ URL ERR _ | Failed to obtain the URL of Network Detection and Response. | Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.SET VALVE INVA _ _ LID | Failed to verify the thresholds. | Check the thresholds and try again. |

| yd.error.ddos.VALVE DEFAULT _ _ ALREADY | The specified request is invalid. You cannot add the default threshold. | The default threshold can only be modified. |
|---|---|---|
| yd.error.ddos.NOT BELONG BE _ _ AVER IP SEGMENT _ _ | The specified CIDR block does not belong to the internal network of Network Detection and Response. | Check the CIDR block. |
| yd.error.ddos.VALVE DELETE E _ _ RR | Failed to delete the default threshold or the threshold configured for 128.0.XX.XX/XX. | The default threshold or the threshold configured for 128.0.XX.XX/XX cannot be deleted. |
| yd.error.ddos.QUERY CODE ER _ _ R | An error occurred while obtaining service configurations. | Try again later. |
| yd.error.ddos.IS OPENED _ | The specified switch has been turned on. | The specified switch cannot be turned on again. |
| yd.error.ddos.IS CLOSED _ | The specified switch has been turned off. | The specified switch cannot be turned off again. |

Table 4: Error codes of Server Guard

| Error code | Error message | Solution |
|---|---|---|
| yd.error.aqs.REQUEST FAILED _ | The request failed. | Try again later. |

Table 7: Error codes of Cloud Firewall

| Error code | Error message |
|---|---|
| yd.error.code.200 | The request was successful. |
| yd.error.code.-360100 | The specified request method is invalid. |
| yd.error.code.-360101 | The authentication failed. |
| yd.error.code.-360102 | A local call error has occurred. |
| yd.error.code.-360103 | One or more parameters are invalid. Try again. |
| yd.error.code.-360104 | The specified application is invalid. Try again. |
| yd.error.code.-360105 | Failed to obtain the logs. |
| yd.error.code.-360106 | Failed to obtain the logs. |
| yd.error.code.-360107 | The specified UID is invalid. Try again. |
| yd.error.code.-360108 | A pagination error has occurred. |
| yd.error.code.-360109 | The service is not supported. |
| yd.error.code.-360110 | The specified IP address is invalid. Specify another value. |

| yd.error.code.-360111 | The specified time is invalid. Specify another value. |
|---|---|
| yd.error.code.-360112 | A parsing error has occurred. |
| yd.error.code.-360113 | The name of the firewall is invalid. Specify another value. |
| yd.error.code.-360114 | The specified connection type is invalid. Specify another value. |
| yd.error.code.-360115 | The specified VPC is invalid. Specify another value. |
| yd.error.code.-360116 | The specified region is invalid. Specify another value. |
| yd.error.code.-360117 | The specified destination CIDR block is invalid. Specify another value. |
| yd.error.code.-360118 | The specified VPC firewall does not exist. Specify another value. |
| yd.error.code.-360119 | The firewall is configured and cannot be repeatedly created. |
| yd.error.code.-360120 | You are not authorized to access the firewall. |
| yd.error.code.-360121 | The specified security group is invalid. |
| yd.error.code.-360122 | The specified security group is invalid. |
| yd.error.code.-360123 | An error occurred while calling the ECS API operation. |
| yd.error.code.-360124 | An error occurred while calling the VPC API operation. |
| yd.error.code.-360125 | The specified CIDR block is invalid. Specify another value. |
| yd.error.code.-360126 | An error occurred while creating the vSwitch. |
| yd.error.code.-360127 | An error occurred while creating the endpoint. |
| yd.error.code.-360128 | An error occurred while deleting an endpoint. |
| yd.error.code.-360129 | You do not have the required permissions. |
| yd.error.code.-360130 | The specified ECS instance is unavailable. |
| yd.error.code.-360131 | An unknown error has occurred. |
| yd.error.code.-360132 | Failed to search the route table. |
| yd.error.code.-360133 | The specified firewall ID is invalid. |
| yd.error.code.-360134 | The status of the firewall is invalid. Try again later. |

| yd.error.code.-360135 | The specified switch of the firewall is invalid. Specify another value. |
|---|---|
| yd.error.code.-360136 | The specified status of the firewall is invalid. Specify another value. |
| yd.error.code.-360137 | Unknown user. Try again. |
| yd.error.code.-360138 | The specified VPC of the firewall is invalid. Specify another value. |
| yd.error.code.-360139 | The specified VPC of the firewall is invalid. Specify another value. |
| yd.error.code.-360140 | The specified firewall does not exist. Specify another value. |
| yd.error.code.-360141 | The firewall is not configured. Configure the firewall. |
| yd.error.code.-360142 | The firewall is already enabled. |
| yd.error.code.-360143 | The firewall is already disabled. |
| yd.error.code.-360144 | The firewall cannot be enabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360145 | The firewall cannot be disabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360146 | The NIC of the firewall is invalid. Check the parameter. |
| yd.error.code.-360147 | The destination CIDR block is invalid. Specify another value. |
| yd.error.code.-360148 | The same CIDR block cannot be repeatedly configured. Specify another CIDR block. |
| yd.error.code.-360149 | The number of destination CIDR blocks exceeds the upper limit. Reduce the number of CIDR blocks. |
| yd.error.code.-360150 | The specified firewall ID is invalid. |
| yd.error.code.-360151 | The status of the endpoint is invalid. |
| yd.error.code.-360152 | The endpoint is invalid. |
| yd.error.code.-360153 | The endpoint is invalid. |
| yd.error.code.-360154 | A timeout error occurred while creating the endpoint. |
| yd.error.code.-360155 | A timeout error occurred while deleting the endpoint. |
| yd.error.code.-360156 | You do not have the required permissions. |
| yd.error.code.-360157 | The specified route table does not exist. |

| yd.error.code.-360158 | The route entry is invalid. |
|---|---|
| yd.error.code.-360159 | Failed to create the route. |
| yd.error.code.-360160 | Failed to delete the route. |
| yd.error.code.-360161 | A timeout error occurred while creating the route. |
| yd.error.code.-360162 | A timeout error occurred while deleting a route. |
| yd.error.code.-360163 | The route is invalid. |
| yd.error.code.-360164 | The status of the task is invalid. |
| yd.error.code.-360165 | Failed to enable the firewall. Try again. |
| yd.error.code.-360166 | Failed to disable the firewall. Try again. |
| yd.error.code.-360167 | One or more parameters are invalid. Try again. |
| yd.error.code.-360168 | One or more parameters are invalid. Try again. |
| yd.error.code.-360169 | One or more parameters are invalid. Try again. |
| yd.error.code.-360170 | One or more parameters are invalid. Try again. |
| yd.error.code.-360171 | The specified region is invalid. |
| yd.error.code.-360172 | The system is busy. |
| yd.error.code.-360173 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360174 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360175 | One or more parameters are invalid. Try again. |
| yd.error.code.-360176 | One or more parameters are invalid. Try again. |
| yd.error.code.-360177 | One or more parameters are invalid. Try again. |
| yd.error.code.-360178 | An unknown error has occurred. |
| yd.error.code.-360179 | Failed to call the API operation. |
| yd.error.code.-360180 | The number of VPCs that are attached to the CEN instance is insufficient. |
| yd.error.code.-360181 | The firewall of the CEN instance is overwritten. You do not need to create a firewall. |
| yd.error.code.-360182 | The specified security group does not exist. |
| yd.error.code.-360183 | The security group cannot be deleted. |
| yd.error.code.-360184 | An unknown error has occurred. |
| yd.error.code.-360185 | Failed to update the firewall route. |

| yd.error.code.-360186 | You cannot configure the firewall because the status of the firewall is invalid. |
|---|---|
| yd.error.code.-360187 | The number of VPCs in the region is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360188 | The quota is insufficient. You cannot configure the VPC firewall. Increase the quota. |
| yd.error.code.-360189 | The specified ECS instance does not exist. |
| yd.error.code.-360190 | Failed to call the API operation. |
| yd.error.code.-360191 | One or more parameters are invalid. Try again. |
| yd.error.code.-360192 | The account is invalid. Specify another value. |
| yd.error.code.-360193 | The account does not have the required permissions, and Cloud Firewall is not purchased. |
| yd.error.code.-360194 | Failed to configure the intrusion prevention system (IPS). |
| yd.error.code.-360195 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360196 | VPC firewalls can be created only in the same region. |
| yd.error.code.-360197 | A conflict occurred. |
| yd.error.code.-360198 | The destination CIDR block is not specified. The firewall cannot be created. |
| yd.error.code.-360199 | A timeout error occurred while attaching Cloud Firewall instances to the CEN instance. |
| yd.error.code.-360200 | A timeout error occurred while creating the vSwitch. |
| yd.error.code.-360201 | A timeout error occurred while deleting the vSwitch. |
| yd.error.code.-360202 | The specified network instance ID is invalid. |
| yd.error.code.-360203 | The specified VPC does not exist. |
| yd.error.code.-360204 | A timeout error occurred while creating the VPC. |
| yd.error.code.-360205 | A timeout error occurred while creating the VPC. |
| yd.error.code.-360206 | The specified ECS instance does not exist. |
| yd.error.code.-360207 | Failed to disable the ECS instance. Try again. |
| yd.error.code.-360208 | Failed to obtain the backup ECS instance. |
| yd.error.code.-360209 | You are not allowed to create a firewall for a HUB VPC. |

| yd.error.code.-360210 | The specified CEN instance ID is invalid. |
|---|---|
| yd.error.code.-360211 | One or more parameters are invalid. Try again. |
| yd.error.code.-360212 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360213 | The specified CEN instance does not exist. |
| yd.error.code.-360214 | The request timed out. Try again. |
| yd.error.code.-360215 | One or more parameters are invalid. Try again. |
| yd.error.code.-360216 | The Express Connect circuit for the data center is invalid. |
| yd.error.code.-360217 | The specified firewall mode is invalid. |
| yd.error.code.-360218 | Failed to call the API operation of Apsara Stack Network Operations Platform (NET). |
| yd.error.code.-360300 | A backend error has occurred. |
| yd.error.code.-360301 | A backend error has occurred. |
| yd.error.code.-360302 | A backend error has occurred. |
| yd.error.code.-360303 | A backend error has occurred. |
| yd.error.code.-360304 | A backend error has occurred. |
| yd.error.code.-360305 | A backend error has occurred. |
| yd.error.code.-360306 | A backend error has occurred. |
| yd.error.code.-360307 | A backend error has occurred. |
| yd.error.code.-360308 | Failed to query the cluster ID. |
| yd.error.code.-360309 | Failed to update the information about the cluster. |
| yd.error.code.-360310 | Failed to update the Express Connect circuit. |
| yd.error.code.-360311 | Failed to insert the VLAN. |
| yd.error.code.-360312 | Failed to query the IP address pool. |
| yd.error.code.-360313 | Failed to update the IP address pool. |
| yd.error.code.-360314 | Failed to update the information about the VPC route. |
| yd.error.code.-360315 | Failed to update the status of the VPC. |
| yd.error.code.-360316 | Failed to insert the firewall namespace. |
| yd.error.code.-360317 | Failed to update the VLAN. |

| yd.error.code.-360318 | Failed to update the endpoint information of the firewall. |
|---|---|
| yd.error.code.-360319 | Failed to update the network information of the firewall. |
| yd.error.code.-360320 | Failed to update the health check configurations. |
| yd.error.code.-360321 | Failed to update the route table. |
| yd.error.code.-360322 | Failed to update the information about the Express Connect circuit for the data center. |
| yd.error.code.-360323 | Failed to update the information about the route of the data center. |
| yd.error.code.-360400 | An unknown error has occurred. |
| yd.error.code.-360401 | No VLAN is available. |
| yd.error.code.-360402 | Failed to call the VPC API operation. |
| yd.error.code.-360403 | Failed to create the virtual firewall. |
| yd.error.code.-360404 | Failed to create the Express Connect circuit. |
| yd.error.code.-360405 | Failed to enable the Express Connect circuit. |
| yd.error.code.-360406 | Failed to create the VBR. |
| yd.error.code.-360407 | Failed to update the attributes of the VBR. |
| yd.error.code.-360408 | Failed to query the VBR. |
| yd.error.code.-360409 | Failed to create the router interface. |
| yd.error.code.-360410 | Failed to update the attributes of the router interface. |
| yd.error.code.-360411 | Failed to connect the router interface. |
| yd.error.code.-360412 | Failed to create the Express Connect circuit for the data center. |
| yd.error.code.-360413 | Failed to enable the Express Connect circuit for the data center. |
| yd.error.code.-360414 | Failed to query the router interface. |
| yd.error.code.-360415 | Failed to query the monitored IP addresses that are used for communications between VPCs. |
| yd.error.code.-360416 | Failed to query the monitored IP addresses that are used for communications between a data center and a VPC. |
| yd.error.code.-360417 | The VPC monitoring mode is abnormal. |
| yd.error.code.-360418 | The status of the instance is invalid. |

| yd.error.code.-193000 | An unknown error has occurred. |
|---|---|
| yd.error.code.-193001 | The specified HTTP request method is invalid. |
| yd.error.code.-193002 | Fail to call the API operation by using HTTP. |
| yd.error.code.-193003 | You do not have the required permissions. |
| yd.error.code.-193004 | The operation is not supported. |
| yd.error.code.-193005 | The authentication failed. |
| yd.error.code.-193006 | An error occurred while accessing the database. |
| yd.error.code.-193007 | A local method is called. |
| yd.error.code.-193101 | Failed to encode JSON-formatted data. |
| yd.error.code.-193102 | Failed to parse JSON-formatted data. |
| yd.error.code.-193103 | Failed to parse INT data. |
| yd.error.code.-193104 | Failed to parse BOOLEAN data. |
| yd.error.code.-193105 | Failed to parse the body of the HTTP request. |
| yd.error.code.-193201 | One or more required parameters are not specified. |
| yd.error.code.-193202 | The specified parameter value is invalid. |
| yd.error.code.-193203 | The specified time is invalid. |
| yd.error.code.-193204 | One or more parameters are invalid. |
| yd.error.code.-193205 | The IP address is not in the CIDR block configured for traffic redirection. |
| yd.error.code.-193301 | The CIDR block already exists. |
| yd.error.code.-193302 | The specified firewall UUID is invalid. |
| yd.error.code.-193303 | The mode of the firewall is being switched. |
| yd.error.code.-193304 | The mode of the firewall is invalid. |
| yd.error.code.-193305 | The switch of the firewall mode in unauthorized. |
| yd.error.code.-193306 | The mode of the device is being switched. |
| yd.error.code.-193307 | An error occurred while checking the health status of the instance. The instance cannot be switched to the normal mode. |
| yd.error.code.-193308 | All devices are bypassed, and the instance mode cannot be switched. |
| yd.error.code.-193309 | The working mode of the instance takes precedence over the working mode of the device. |

| yd.error.code.-193310 | The specified page number is invalid. |
|---|---|
| yd.error.code.-193311 | The specified route type is invalid. |
| yd.error.code.-193312 | Failed to delete the route. |
| yd.error.code.-193313 | Failed to delete the route. |
| yd.error.code.-193314 | Failed to create the route. |
| yd.error.code.-193315 | Failed to create the route. |
| yd.error.code.-193316 | The ID of the Cloud Firewall instance is invalid. |
| yd.error.code.-193317 | The Cloud Firewall instance must be specified. |
| yd.error.code.-200100 | The specified request method is invalid. |
| yd.error.code.-200101 | The authentication failed. |
| yd.error.code.-200102 | A local call error has occurred. |
| yd.error.code.-200103 | One or more parameters are invalid. Try again. |
| yd.error.code.-200104 | The specified UID is invalid. Try again. |
| yd.error.code.-200105 | A pagination error has occurred. |
| yd.error.code.-200106 | The IP address in the address book is invalid. Check the parameter and specify another value. |
| yd.error.code.-200107 | The address book already exists. |
| yd.error.code.-200108 | An error has occurred. Try again. |
| yd.error.code.-200109 | The address book is in use and cannot be deleted. |
| yd.error.code.-200110 | One or more parameters are invalid. |
| yd.error.code.-200111 | One or more parameters are invalid. |
| yd.error.code.-200112 | One or more parameters are invalid. |
| yd.error.code.-200113 | One or more parameters are invalid. |
| yd.error.code.-200114 | One or more parameters are invalid. |
| yd.error.code.-200115 | One or more parameters are invalid. |
| yd.error.code.-200116 | One or more parameters are invalid. |
| yd.error.code.-200117 | The specified security group rule does not exist. |
| yd.error.code.-200118 | The specified priority is invalid, or the number of rules reaches the upper limit. |
| yd.error.code.-200119 | The specified priority is invalid, or the number of rules reaches the upper limit. |

| yd.error.code.-200120 | An error has occurred. Try again. |
|---|---|
| yd.error.code.-200121 | The domain name is invalid. Check the parameter and specify another value. |
| yd.error.code.-200122 | The number of addresses in the address book exceeds the upper limit. |
| yd.error.code.-200123 | One or more parameters are invalid. |
| yd.error.code.-200124 | One or more parameters are invalid. |
| yd.error.code.-200125 | One or more parameters are invalid. |
| yd.error.code.-200126 | One or more parameters are invalid. |
| yd.error.code.-200127 | The number of ports in the address book exceeds the upper limit. |
| yd.error.code.-200128 | The port in the address book is invalid. Check the parameter and specify another value. |
| yd.error.code.-200129 | The number of address books exceeds the upper limit. |
| yd.error.code.-200130 | The number of address books exceeds the upper limit. |
| yd.error.code.-200200 | A backend error has occurred. |
| yd.error.code.-200201 | A backend error has occurred. |
| yd.error.code.-200202 | A backend error has occurred. |
| yd.error.code.-200203 | A backend error has occurred. |
| yd.error.code.-200300 | A backend error has occurred. |
| yd.error.code.-200301 | A backend error has occurred. |
| yd.error.code.-200302 | A backend error has occurred. |
| yd.error.code.-200400 | An unknown error has occurred. |
| yd.error.code.-200500 | An error occurred while calling the API operation. |
| yd.error.code.200 | The request was successful. |
| yd.error.code.-210100 | The specified request method is invalid. |
| yd.error.code.-210101 | The authentication failed. |
| yd.error.code.-210102 | A local call error has occurred. |
| yd.error.code.-210103 | One or more parameters are invalid. Try again. |
| yd.error.code.-210104 | The specified UID is invalid. Try again. |
| yd.error.code.-210105 | A pagination error has occurred. Try again. |

| yd.error.code.-210106 | One or more parameters are invalid. Try again. |
|---|---|
| yd.error.code.-210107 | One or more parameters are invalid. Try again. |
| yd.error.code.-210108 | One or more parameters are invalid. Try again. |
| yd.error.code.-210109 | One or more parameters are invalid. Try again. |
| yd.error.code.-210110 | One or more parameters are invalid. Try again. |
| yd.error.code.-210111 | One or more parameters are invalid. Try again. |
| yd.error.code.-210200 | A backend error has occurred. |
| yd.error.code.-210201 | A backend error has occurred. |
| yd.error.code.-210202 | A backend error has occurred. |
| yd.error.code.-210203 | A backend error has occurred. |
| yd.error.code.-210300 | A backend error has occurred. |
| yd.error.code.-210301 | A backend error has occurred. |
| yd.error.code.-210302 | An error has occurred. Try again. |
| yd.error.code.-210400 | An error has occurred. Try again. |
| yd.error.code.200 | The request was successful. |
| yd.error.code.-230100 | The specified request method is invalid. |
| yd.error.code.-230101 | The authentication failed. |
| yd.error.code.-230102 | Failed to send the request to the local server. |
| yd.error.code.-230103 | The operation failed authentication. |
| yd.error.code.-230104 | One or more parameters are invalid. |
| yd.error.code.-230105 | The policy template already exists. |
| yd.error.code.-230106 | The specified policy template does not exist. |
| yd.error.code.-230107 | The specified user ID is invalid. |
| yd.error.code.-230108 | The specified security group ID is invalid. |
| yd.error.code.-230109 | The specified security group ID is invalid. |
| yd.error.code.-230110 | The direction of the rule is invalid. |
| yd.error.code.-230111 | An IP protocol error has occurred. |
| yd.error.code.-230112 | The rule policy is invalid. |
| yd.error.code.-230113 | The priority of the policy is invalid. Specify another value. |

| yd.error.code.-230114 | The port in the policy is invalid. Specify another value. |
|---|---|
| yd.error.code.-230115 | The CIDR block is invalid. Specify another value. |
| yd.error.code.-230116 | The description is invalid. Specify another value. |
| yd.error.code.-230117 | The policy already exists. |
| yd.error.code.-230118 | The specified policy does not exist. |
| yd.error.code.-230119 | The specified rule ID is invalid. |
| yd.error.code.-230120 | The number of policies exceeds the upper limit. We recommend that you delete policies that you no longer use. |
| yd.error.code.-230121 | A pagination error has occurred. |
| yd.error.code.-230122 | The rule is being published. Try again. |
| yd.error.code.-230123 | The submission status is invalid. |
| yd.error.code.-230124 | The policy group is rolled back. |
| yd.error.code.-230125 | An error occurred while submitting the information. |
| yd.error.code.-230126 | The rule is not changed. You do not need to publish the rule. |
| yd.error.code.-230127 | The specified security group ID is invalid. |
| yd.error.code.-230128 | The IP address in the rule is invalid. |
| yd.error.code.-230129 | The network type of the rule is invalid. Specify another value. |
| yd.error.code.-230130 | An error occurred while managing the rule. |
| yd.error.code.-230131 | The policy cannot be submitted. |
| yd.error.code.-230150 | The specified policy group does not exist. Specify another value. |
| yd.error.code.-230151 | The number of policy groups exceeds the upper limit. |
| yd.error.code.-230152 | The policy group cannot be modified. |
| yd.error.code.-230153 | The policy group is pre-started. |
| yd.error.code.-230154 | The specified rule ID is invalid. |
| yd.error.code.-230200 | A backend error has occurred. |
| yd.error.code.-230300 | A backend error has occurred. |
| yd.error.code.-230301 | A backend error has occurred. |

| yd.error.code.-230302 | A backend error has occurred. |
|---|---|
| yd.error.code.-230400 | An unknown error has occurred. |

**Error codes of Network Detection and Response**

| Error code | Error message | Description |
|---|---|---|
| ErrorNeedLogin.-210204 | need login | You have not logged in. Log in first. |
| ErrorAuthentication.-210101 | authentication error | An authentication error has occurred. Use a Resource Access Management (RAM) role that has the required permissions. |
| ErrorParametersAliUid.-210902 | invalid AliUid | The specified AliUid parameter is invalid. Specify a valid value. |
| ErrorParametersIpType.-210920 | invalid para ip type | The specified ipType parameter is invalid. Specify a valid value. |
| ErrorParametersSrcIP.-210919 | invalid para src ip | The specified SrcIP parameter is invalid. Specify a valid value. |
| ErrorParametersDstIP.-210921 | invalid para dst ip | The specified dstIP parameter is invalid. Specify a valid value. |
| ErrorParametersPort.-210208 | invalid port, must 0~65535 | The specified port number is invalid. Specify a port number in the range of 0 to 65535. |
| ErrorParametersLiveTime.- 210922 | invalid para live time | The specified liveTime parameter is invalid. Specify a valid value. |
| ErrorDBInsert.-210122 | internal error: sql insert | An internal error occurred while executing the INSERT statement. |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0 | The UUID list is empty. |
| ErrorDBSelect.-210124 | internal error: sql select | An internal error occurred while executing the SELECT statement. |
| ErrorParasAddressCidrFeild.- 210915 | paras addressCidrList filed | Failed to reset the addressCidrList rule. |
| ErrorPortAddressGroup.-210303 | get port in address group failed | Failed to obtain port information from the address group. |
| ErrorPortAddressGroup.-210303 | get port in address group failed | Failed to obtain port information from the address group. |

| ErrorSourceAddressGroup.- 210304 | get source address in address group failed | Failed to obtain source addresses from the address group. |
|---|---|---|
| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.X X\" | The source address range is invalid. Specify the value in the \"192.168.XX.XX/192.168.XX.X X\" format. |
| ErrorDestAddressGroup.- 210305 | get dest address in address group failed | Failed to obtain destination addresses from the address group. |
| ErrorNoBeaverRules.-210226 | no beaver rules for online | The specified Network Detection and Response rule does not exist. |
| ErrorDBUpdate.-210121 | internal error: sql update | An internal error occurred while executing the UPDATE statement. |
| ErrorDBDelete.-210123 | internal error: sql delete | An internal error occurred while executing the DELETE statement. |
| ErrorMarshalJSON.-210125 | internal error: marshal json | An internal error occurred while marshaling JSON-formatted data. |
