---
title: "Cloud Parallel File Storage Developer Guide 20260701"
product_version: "V3.18.6"
pdf_pages: 38
source_pdf: "aad42bd7b73d3cfe_Alibaba Cloud Apsara Stack V3.18.6 Cloud Parallel File Storage Developer Guide 20260701.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.6%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%96%87%E4%BB%B6%E5%AD%98%E5%82%A8CPFS/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.6%20Cloud%20Parallel%20File%20Storage%20Developer%20Guide%2020260701.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings)
---

# Cloud Parallel File Storage Developer Guide 20260701

## Table of Contents

- 1 Preparations
  - 1.1 Obtain an AccessKey
  - 1.2 Obtain Endpoint information
  - 1.3 Get common header parameters
  - 1.4 Call Apsara Stack APIs Through the POP Gateway
- 2 Java SDK call examples
  - 2.1 Getting Started
  - 2.2 User guide
    - 2.2.1 Install the Java SDK
    - 2.2.2 Setting Identity Verification Credentials
    - 2.2.3 Request connection configuration
    - 2.2.4 Call APIs Using CommonRequest
    - 2.2.5 Error handling
- 3 Python SDK call examples
  - 3.1 Getting Started
  - 3.2 User guide
    - 3.2.1 Install the Python SDK
    - 3.2.2 Set identity verification credentials
    - 3.2.3 Call APIs Using CommonRequest
    - 3.2.4 Error handling
- 4 Go SDK call examples
  - 4.1 Getting Started
  - 4.2 User guide
    - 4.2.1 Install the Go SDK core package
    - 4.2.2 Set up identity verification credentials
    - 4.2.3 Call an API using CommonRequest
    - 4.2.4 Error Handling
- 5 API reference
  - 5.1 Call APIs
    - 5.1.1 Overview
    - 5.1.2 Request structure
    - 5.1.3 API Authorization
    - 5.1.4 Response
  - 5.2 RAM authorization
  - 5.3 Common Parameters
  - 5.4 File system
    - 5.4.1 CreateFileSystem
    - 5.4.2 DeleteFileSystem
    - 5.4.3 DescribeFileSystems
    - 5.4.4 ModifyFileSystem

## 1 Preparations

### 1.1 Obtain an AccessKey

AccessKey supports the RAM authorization pattern. This topic describes how to obtain an AccessKey using RAM authorization.

**Background information**

An AccessKey uses symmetric encryption with an AccessKey ID and an AccessKey secret to authenticate the identity of a request sender. The AccessKey ID identifies the user. The AccessKey secret is a string that the user uses to generate an encrypted signature. It is granted to a third-party requester through RAM authorization. The Apsara Uni-manager Management Console provides personal and organization AccessKeys. Only operations administrators and primary organization administrators can obtain organization AccessKeys. Use a personal account AccessKey to call the APIs of the Apsara Uni-manager Management Console and other cloud products. If you use a personal account AccessKey, add the following parameters to the header. Otherwise, an insufficient permissions error may occur:

**Warning**

A personal account AccessKey is a restricted AccessKey that is managed by the permission system of the Apsara Uni-manager Management Console. An organization AccessKey has greater permissions. An administrator must confirm the security of the operation.

| Parameter Name | Description |
|---|---|
| x-acs-regionid | The region. For example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the corresponding organization in Apsara Uni-manager Management Console. To obtain the ID, see the "GetOrganizationList" topic in the Apsara Uni-manager Management Console Development Guide. |
| x-acs-resourcegroupid | The ID of the corresponding resource group in Apsara Uni-manager Management Console. To obtain the ID, see the "ListResourceGroup" topic in the Apsara Uni-manager Management Console Development Guide. |
| x-acs-instanceid | The ID of the instance for the operation. For example, the instance ID of a CPFS instance is available in the CPFS file system list. |

**Obtain a personal account AccessKey**

You can obtain a personal account AccessKey as follows:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the interface, click the profile picture of the current user, and
then click **Personal Information**.
3. In the **AccessKey** section, view the AccessKey information for the personal account.

**Note**

The AccessKey ID and AccessKey secret are keys for accessing cloud resources. They grant full permissions to the account. Keep them confidential.

**Obtain an organization AccessKey**

You can obtain an organization AccessKey as follows:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose .
4. In the organization chart, click the name of the target primary organization.
5. Click **Manage AccessKey**.
6. In the dialog box that appears, view the organization AccessKey information.

### 1.2 Obtain Endpoint information

This topic describes how to obtain the Endpoint for a CPFS file system.

**Obtain an Endpoint**

1. You can log on to the Apsara Uni-manager Operations Console.
2. In the top menu bar, select **Platform Operation > Apsara Infrastructure Management**
**> O&M Tools**.
3. On the **Service Registration Variables Dashboard**, select **Service** and enter **nas-**
**yaochi**.
4. In the **Service Registration** column, click the
icon, and then click the information that appears.
5. In the **Register Variables** box, the value of **nas.openapi.endpoint** is the Endpoint for
the CPFS file system.

### 1.3 Get common header parameters

**parameters**

When you call Apsara Stack APIs, you must include several common request header parameters. The response also includes common response parameters.

**Common request parameters**

You must specify values for these common request parameters in your Apsara Stack API call code. For example, in a Java SDK call: `request.putHeadParameter("x-acs-resourcegroupid", "`

| ce | <yourResourceGroupID> |
|---|---|

ID.

| Name | Description |
|---|---|
| x-acs-regionid | The region ID of the instance resource you are operating on. For how to obtain it, see Get the region ID. |
| x-acs-organizationid | The organization ID of the instance resource you are operating on. For how to obtain it, see Get the organization ID. |
| x-acs-resourcegroupid | The resource group ID of the instance resource you are operating on. For how to obtain it, see Get the resource group ID. |
| x-acs-instanceid | The ID of the file system resource you are operating on. For how to obtain it, see Get the instance ID. |

| Note When you call APIs of the Apsara Uni-manager Management Console, you do not need to use the header parameters x-acs-organizationid , x-acs- resourcegroupid , or x-acs-instanceid . When you call APIs of other cloud products, you must include the organization ID <x-acs-organizationid> in the header parameters. Otherwise, the API call fails with a permission error. When you call APIs of other cloud products, you must include the resource group ID <x-acs-resourcegroupid> in the header parameters. This specifies the organization and resource group of the resource and enables isolated queries. If you omit <x-acs-resourcegroupid> , the system uses the default resource group of your organization. |   |   |
|---|---|---|
|   | x-acs- |   |

|   | x-acs-organizationid |
|---|---|
| x-acs-instanceid |   |

**Get the region ID**

You can view the region ID of a resource in the Apsara Uni-manager Management Console.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management** > **Region**
**Management**.
4. Click the target organization name.
5. In the **Region list** on the right, the value in the **Region name** column is the region ID.

**Get the organization ID**

You can obtain the organization ID by making an API call. You can use the online debugging feature in the Apsara Uni-manager Management Console to quickly retrieve the ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, choose **Products** > **Developer Tools** > **APIs and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button, choose **Cloud Platform** > **Unified Cloud Management Platform**, and set **Version** to **2019-05-10**.
5. In the text box, enter `GetOrganizationList` . Enter the target organization name in the
name parameter and invoke the API. After the API call is successful, find the **id** value in the
**Call Result** section. This value is the organization ID.

**Get the resource group ID**

You can obtain the resource group ID by making an API call. You can use the online debugging feature in the Apsara Uni-manager Management Console to quickly retrieve the ID.
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, choose **Products** > **Developer Tools** > **APIs and Tools** >
**Developer Portal**.
3. On the **Developer Portal** page, choose **API Integration** > **API Debugging**.
4. Click the
button, choose **Cloud Platform** > **Unified Cloud Management Platform**, and set **Version** to **2019-05-10**.
5. In the text box, enter `ListResourceGroup` . After the API call is successful, find the **id** value
in the **Call Result** section. This value is the resource group ID.

**Get the file system ID**

You can obtain the file system ID from the resource list for the cloud product in the Apsara Uni-manager Management Console. You can view the ID in the file system list of the Cloud Paralleled File System (CPFS) console.
1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, choose **Products > Storage > File Storage CPFS**.
3. In the navigation pane on the left, click **CPFS File System**.
4. View and copy the instance ID from the list.

**Common response parameters**

When you call list-type APIs for cloud product resources, the response includes the following common response parameters by default.

| Name | Description |
|---|---|
| ResourceGroupName | Resource group name. |
| ResourceGroup | Resource group ID. |

| DepartmentName | Organization name. |
|---|---|
| Department | Organization ID. |

### 1.4 Call Apsara Stack APIs Through the POP Gateway

**Through the POP Gateway**

To access a product domain name using the POP Java SDK, you must know the product's call method: RPC or ROA.

**Prerequisites**

Apsara Stack currently recommends using CommonRequest to call APIs. You can download version 1.0 of the SDK from the SDK Center.

**CommonRequest Call Example**

This example shows an RPC call to the DescribeFileSystems interface of the CPFS product, version 2017-06-26. The following code shows an example:

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace with your actual region ID.
            "<yourAccessKeyID>",      // Replace with your actual AccessKey ID.
            "<yourAccessKeySecret>"); // Replace with your actual AccessKey secret.
        // Set the endpoint for the current product. Replace placeholder values with yo
ur actual values.
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /** Configure a proxy (optional). Replace with your actual proxy IP address and
port.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
        Replace with your actual proxy IP address and port.
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set parameters.
```

```
//Ceatea equestadsetpaaetes.
        CommonRequest request = new CommonRequest();
        // Replace with your actual endpoint.
        request.setDomain("<Endpoint>");
        request.setSysProduct("CPFS");
        request.setVersion("2017-06-26");
        request.setAction("DescribeFileSystems");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>"); //
Optional. Replace with your actual resource group ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>"); // Re
quired. Replace with your actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo"); // Required.
Describe the caller source.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>"); // Optional. Requ
ired only for Enterprise Edition versions V3.15.0 and earlier. Replace with your actual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>"); //
Optional. Required only when modifying, deleting, or querying details of a single insta nce. Replace with your actual instance ID.
        /**
        When you use STS AccessKeys to call an API, include the SecurityToken
parameter.
        Use this method:
        request.putQueryParameter("SecurityToken", "<yourSecurityToken>");
        Replace with your actual token.
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

`}` `}` `}`

**Important**

When you use HTTPS to access OpenAPI, the SDK validates SSL/TLS certificates by default. If your runtime environment does not support certificate validation, the SDK throws a certificate validation error. To keep production traffic secure, leave certificate validation enabled. If you must disable it in a staging environment, use the following setting: Java

```
HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Disable server certificate validation clientConfig.setIgnoreSSLCerts(true)
```

es

## 2 Java SDK call examples

This topic describes how to obtain the Java SDK and start making calls.

### 2.1 Getting Started

This topic describes how to obtain the Java SDK and start making calls.

**Prerequisites**

To use the Apsara Stack Java software development kit (SDK), you must have an authorized account, an AccessKey ID, and an AccessKey secret. For more information, see Obtain an AccessKey. Obtain the Endpoint for the product that corresponds to the feature you want to use. For more information, see Obtain Endpoint information. The Apsara Stack Java SDK requires Java Development Kit (JDK) 1.8 or later.

**Install the Apsara Stack Java SDK**

If you use Apache Maven to manage your Java project, add the SDK dependency to your project's pom.xml file. To use the SDK for a product, you must install both the core SDK library and the productspecific SDK. The core SDK library must be version 4.5.17 or later. For more information, see Install the Java SDK.

**Use the Java SDK**

The main steps to make calls using the Apsara Stack Java SDK are as follows:
1. Create and initialize a DefaultAcsClient instance.
2. Create an API request and set its parameters.
3. Send the request and handle the response or exceptions.

### 2.2 User guide

#### 2.2.1 Install the Java SDK

This topic describes how to install and call the Java SDK. The Apsara Stack Java SDK is compatible with JDK 1.8 or later. You can install the SDK by adding a Maven dependency or by downloading the Alibaba Cloud SDK. If you want to use the CPFS feature, you must also install the Alibaba Cloud Java SDK core library, version 4.5.17 or later.

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

es

#### 2.2.2 Setting Identity Verification Credentials

**Credentials**

When you use the Apsara Stack SDK to access Apsara Stack services, you must provide credentials for identity verification. This topic describes how to set these credentials. The Java SDK supports identity verification using an AccessKey. For more information about how to obtain an AccessKey, see Obtain an AccessKey. When you use an AccessKey as an access credential, you must set the credential during client initialization.

**Note**

Ensure that code containing the AccessKey is not leaked, for example, by committing it to a publicly accessible GitHub project. Otherwise, your account security may be compromised.

```
DefaultProfile profile = DefaultProfile.getProfile(
    "<yourRegionID>",          // Replace with your actual region ID
    "<yourAccessKeyID>",      // Replace with your actual AccessKey ID
    "<yourAccessKeySecret>"); // Replace with your actual AccessKey secret
```

**Note**

In the preceding code example, replace the variable parameters with your actual values. Do not include the angle brackets (<>) in the final code.

#### 2.2.3 Request connection configuration

This topic describes how to configure request connections (HttpClientConfig). Use the following code to configure HttpClientConfig. You can select and set the configuration items according to your requirements.

**Note**

In the following code sample, replace the variable parameters with your actual values. Do not include the angle brackets (<>) in your code. The variable parameters are described as follows: <readTimeout>: Set the read timeout period in milliseconds (ms). <connectionTimeout>: Set the connection timeout period in milliseconds (ms). <maxRequestsPerHost>: Set the maximum number of concurrent requests for each server. The data type is integer. <maxRequests>: Set the maximum number of concurrent requests across all servers. The data type is integer. <http://192.168.XX.XX:33XX>: Replace this with your actual proxy IP address and port. es

```
// Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore SSL certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Set the read timeout period in milliseconds (ms). clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Set the connection timeout period in milliseconds (ms). clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Set the maximum number of requests for each host. The data type is INT. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Set the maximum number of requests. The data type is INT. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Set the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Set a proxy as needed. The methods are as follows: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace this with your actual proxy IP address and port.
```

`*/`

```
profile.setHttpClientConfig(clientConfig);
```

#### 2.2.4 Call APIs Using CommonRequest

Use CommonRequest when no SDK is available for an API. You can also use it when the request parameters or response values in the provided SDK do not meet your needs. CommonRequest lets you call any OpenAPI interface.

**CommonRequest Features**

CommonRequest has these features: Lightweight: You only need the Core package. You do not need to download or install SDKs for individual products. Simple: You can call newly released APIs without updating the SDK. Fast iteration.

**Use CommonRequest**

To make a CommonRequest call, obtain the following parameter values. Domain name: The service endpoint for the product. API version: The version number of the API, in YYYY-MM-DD format. You can find the API version in the Common Parameters section of the product's API documentation. Operation name: The name of the API you want to call.

| Action |   |
|---|---|
|   | . |

Obtain the `Action` parameter. Then, set the API name using `request.setSysAction("`

```xml
<Action>") .
```

| For example, to call the | CreateFileSystem |   |
|---|---|---|
| request.setSysAction("CreateFileSystem") |   |   |

For example, to call the `CreateFileSystem` API, use `CommonRequest` and set the action as

**Example: Call an RPC-style API**

es The following sample code shows how to call the CPFS DescribeFileSystems API to retrieve file system information.

**Note**

In the code below, replace all variable parameters with your actual values. Remove the angle brackets (<>) from the final code. Replace these parameters: <yourRegionID>: Replace with your actual region ID. <yourAccessKeyID>: Replace with your actual AccessKey ID. <yourAccessKeySecret>: Replace with your actual AccessKey secret. <Endpoint>: Replace with the actual endpoint for your product. <yourSecurityToken>: Replace with your actual SecurityToken. <yourResourceGroupID>: Replace with your actual resource group ID. <yourOrganizationID>: Replace with your actual organization ID. <yourInstanceID>: Replace with your actual instance ID. <http://192.168.XX.XX:33XX>: Replace with your actual proxy IP address and port.

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create and initialize a DefaultAcsClient instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<yourRegionID>",          // Replace with your actual region ID.
            "<yourAccessKeyID>",      // Replace with your actual AccessKey ID.
            "<yourAccessKeySecret>"); // Replace with your actual AccessKey secret.
        // Set the endpoint for your product. Replace the variable with your actual val
ue.
        profile.addEndpoint("<Endpoint>");
        HttpClientConfig clientConfig = HttpClientConfig.getDefault();
        clientConfig.setProtocolType(ProtocolType.HTTP);
        /** Configure a proxy (optional). Replace with your actual proxy IP address and
port.
        clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>");
```

`or`

```
        clientConfig.setHttpsProxy("<https://192.168.XX:33XX>");
```

`*/`

```
        profile.setHttpClientConfig(clientConfig);
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and set parameters.
        CommonRequest request = new CommonRequest();
        // Replace with your actual domain name.
```

es

```java
        request.setDomain("<Endpoint>");
        request.setSysProduct("CPFS");
        request.setVersion("2017-06-26");
        request.setSysAction("DescribeFileSystems");
        request.putQueryParameter("FileSystemType", "bmcpfs");
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
        request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// O
ptional. Replace with your actual resource group ID.
        request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Req
uired. Replace with your actual organization ID.
        request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required.
Describe the caller source.
        request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional.
Required only for Enterprise Edition v3.15.0 and earlier versions. Replace with your ac tual region ID.
        // request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");//
Optional. Required only when modifying, deleting, or querying details of a single insta nce. Replace with your actual instance ID.
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

`}` `}` `}`

#### 2.2.5 Error handling

When you use the Java software development kit (SDK), an exception is returned if a serverside or client-side error occurs. The exception contains a specific error code and an error message. In most cases, you do not need to handle client-side errors that are returned by the Java SDK. You can simply handle server-side errors based on the error messages from the server. `ServerException` indicates a server-side error. `ClientException` indicates a client-side error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message.

```
com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found.
```

To handle SDK errors, you can write your code as shown in the following example: es

```java
try {
    FooResponse response = client.getAcsResponse(request);
    // Process the response
    // ...
}catch (ServerException e){
    // Add your custom error handling logic here
    // For example, print the specific error message
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
    // If you encounter a complex issue, submit a ticket and provide the RequestId.
    System.out.println("ResponseId=" + e.getRequestId());
}catch (ClientException e){
    // Add your custom error handling logic here
    // For example, print the specific error message
    System.out.println("ErrorCode=" + e.getErrCode());
    System.out.println("ErrorMessage=" + e.getErrMsg());
```

`}` mples

## 3 Python SDK call examples

### 3.1 Getting Started

This topic describes how to obtain the software development kit (SDK) and start making calls.

**Prerequisites**

To use the Apsara Stack Python SDK, you need an authorized account, an AccessKey ID, and an AccessKey secret. For more information, see Get an AccessKey. Obtain the Endpoint for the product that provides the feature you want to use. For more information, see Get an Endpoint.

**Install the Python SDK core library**

You must install the Alibaba Cloud Python SDK core library to use the CPFS feature. The installation steps are as follows: If you use Python 2.x, run the following command to install the Alibaba Cloud SDK core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the Alibaba Cloud SDK core library:

```
pip3 install aliyun-python-sdk-core-v3
```

**Use the Python SDK**

Calling the Python SDK involves three main steps:
1. Create a Client instance. You must provide the Region ID, AccessKey ID, and AccessKey
secret when you create the instance.
2. Create an API request and set the parameters.
3. Send the request and handle the response or exceptions.

### 3.2 User guide

#### 3.2.1 Install the Python SDK

This topic describes how to install and use the Python SDK.

**Background information**

The Apsara Stack Python SDK is compatible with Python 2.6.x, 2.7.x, and 3.x or later. You can install the SDK using pip.

**Note**

You must install the Alibaba Cloud Python SDK core library to use the SDK for any Alibaba Cloud product.

**Install the Python SDK core library**

mples The CPFS feature requires you to install the Alibaba Cloud Python SDK core library. The installation steps are as follows: If you use Python 2.x, run the following command:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command:

```
pip3 install aliyun-python-sdk-core-v3
```

#### 3.2.2 Set identity verification credentials

When you use the Apsara Stack software development kit (SDK) to access Apsara Stack services, you must provide credentials for identity verification. This topic describes how to set identity verification credentials. The Python SDK supports identity verification using an AccessKey. For more information about how to obtain an AccessKey, see Obtain an AccessKey. When you use an AccessKey as an access credential, set the credential when you initialize the Client.

**Note**

Ensure that code containing your AccessKey is not leaked, for example, by submitting it to a public GitHub project. Otherwise, your information security will be compromised.

```python
from aliyunsdkcore import client clt = client.AcsClient(access_key, access_secret, region_id)
```

#### 3.2.3 Call APIs Using CommonRequest

Use CommonRequest when no SDK is available for a CPFS API or when the SDK’s request parameters or response values do not meet your requirements. CommonRequest enables you to call any OpenAPI interface.

**CommonRequest Features**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK of the service. Fast in iteration.

**Use CommonRequest**

To make a CommonRequest call, obtain the following parameter values. You can find them in the API documentation for each product. Domain name: the service endpoint for the product. API version: the version number of the API, in YYYY-MM-DD format. You can find the API version in the common parameters section of the product’s API documentation. mples Operation name: the name of the API to call. Obtain the `Action` parameter. Set it using `request.set_action_name('Action')` . For example, to call the `DescribeFileSystems` API, specify the operation name using

```
 request.set_action_name('DescribeFileSystems')  in your  CommonRequest .
```

**Example: Call an RPC-style API**

The following Python code shows how to call the DescribeFileSystems operation to retrieve file system information.

**Note**

Replace all placeholder values in the code with your actual values. Do not include the angle brackets (<>) in your final code. Replace these placeholders: Replace <yourRegionID> with your actual region ID. Replace <yourAccessKeyID> with your AccessKey ID. Replace <yourAccessKeySecret> with your AccessKey secret. Replace <yourSecurityToken> with your actual security token. <yourResourceGroupID> with your actual resource group ID. <yourOrganizationID> Replace this placeholder with your actual organization ID. Replace <yourInstanceID> with your instance ID. Replace <Endpoint> with the actual endpoint for your product. mples

```xml
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Replace these values with your actual AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('CPFS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26') request.set_domain('<Endpoint>') # The domain name for the product. This is an example value. Replace it with your actual endpoint.
# or:
# request = CommonRequest(product='CPFS',
action_name='DescribeFileSystems',version='2017-06-26',domain='<Endpoint>')
######
# Set the request protocol. Use https or http. The default is http.
# To use https, run:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('FileSystemType', 'bmcpfs') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30')
######
# When you use STS credentials, add the SecurityToken parameter.
# To add it, run:
# request.add_query_param("SecurityToken", "<yourSecurityToken>")
# Replace <yourSecurityToken> with your actual SecurityToken.
######
# Optional. Replace <yourResourceGroupID> with your actual resource group ID.
request.add_header("x-acs-resourcegroupid", "<yourResourceGroupID>")
# Required. Replace <yourOrganizationID> with your actual organization ID.
request.add_header("x-acs-organizationid", "<yourOrganizationID>")
# Required. Describe the caller source.
request.add_header("x-acs-caller-sdk-source","ApiTestDemo")
# Optional. Required only for Enterprise Edition versions earlier than V3.15.0. Replace
<yourRegionID> with your actual region ID. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Required only when you modify, delete, or query details for a single instan
ce. Replace <yourInstanceID> with your actual instance ID.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request)
# Python 2: print(response)
print(str(response, encoding = 'utf-8'))
```

#### 3.2.4 Error handling

mples The Python Software Development Kit (SDK) returns an exception if an error occurs on the server-side or within the SDK. This exception includes a specific error code and error message. In most cases, you do not need to handle errors that originate from the Python SDK. Handle server-side errors based on the error messages that the server returns. `ServerException` indicates a server-side error. `ClientException` indicates an SDK error. For example, if the following error occurs, modify the AccessKey ID based on the error message.

```
aliyunsdkcore.acs_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFound Specified access key is not found.
```

To handle SDK errors, use the following code example:

```bash
try:
    response = client.do_action_with_exception(request)
except ServerException as e:
    # Add your custom error handling logic here.
    # For example, print the specific error message.
    print e.get_http_status()
    print e.get_error_code()
    print e.get_error_msg()
```

s

## 4 Go SDK call examples

### 4.1 Getting Started

The Alibaba Cloud Go SDK lets you access cloud services without complex programming. This topic describes how to install the Alibaba Cloud Go SDK and start making calls.

**Prepare your environment**

Before you use the Go SDK, you need an authorized account, an AccessKey ID, and an AccessKey secret. For more information, see Obtain an AccessKey. Obtain the Endpoint for the product that you want to use. For more information, see Obtain endpoint information.

**Install the Alibaba Cloud Go SDK core package**

The Alibaba Cloud Go SDK supports Go 1.10.x and later. Run the following command to install the core package.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use the Go SDK**

To use the Go SDK, follow these steps:
1. Initialize a client instance.
2. Create an API request and set parameters.
3. Send the request and handle the acknowledgement or exception.

### 4.2 User guide

#### 4.2.1 Install the Go SDK core package

This topic describes how to install the Go SDK core package. The Alibaba Cloud Go SDK supports Go 1.10.x and later. You can run the following command to install the Go SDK core package.

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

#### 4.2.2 Set up identity verification credentials

When you use the Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for identity verification. This topic describes how to set up identity verification credentials. Currently, the Go SDK supports identity verification using an AccessKey. For information about how to obtain an AccessKey, see Obtain an AccessKey. When you use an AccessKey as an access credential, set the credential during client initialization. s

**Note**

Ensure that code containing an AccessKey does not leak (such as by being committed to a public GitHub project). Otherwise, your information security will be compromised. Replace the variable parameters in the code example with your actual information. The angle brackets (<>) are not retained in the final code.

**Initialize client instance**

```
   client, err := sdk.NewClientWithAccessKey(
        "<yourRegionID>",        // Replace with your actual region ID.
        "<yourAccessKeyID>",     // Replace with your actual AccessKey ID.
        "<yourAccessKeySecret>") // Replace with your actual AccessKey Secret.
```

#### 4.2.3 Call an API using CommonRequest

Use the generic API call method (CommonRequest) if a product API does not have a software development kit (SDK). You can also use this method if the request parameters or response values in an SDK do not meet your needs. The CommonRequest method lets you call any OpenAPI.

**Features of CommonRequest calls**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK of the service. Fast in iteration.

**Use CommonRequest**

To make a CommonRequest call, obtain the values for the following parameters from the API documentation. Domain name (domain): The service endpoint for the product. API version (version): The version number of the API. The format is YYYY-MM-DD. You can find the API version in the common parameters section of the product's API documentation. API information: The name of the API to call. Obtain the `Action` parameter and use `request.ApiName("<Action>")` to specify the API name.

| For example, to call the | DescribeFileSystems |   |
|---|---|---|
| request.ApiName("<DescribeFileSystem>") |   |   |
|   |   | wh |

**Example: Call an RPC-style API**

The following sample code shows how to use the DescribeFileSystems API to retrieve file system information: s

**Note**

In the following code sample, replace the variable parameters with your actual information. Do not include the angle brackets (<>) in the final code. The variable parameters that you must replace are as follows: <yourRegionID>: Replace with your actual region ID. <yourAccessKeyID>: Replace with your actual AccessKey ID. <yourAccessKeySecret>: Replace with your actual AccessKey secret. <yourSecurityToken>: Replace with your actual SecurityToken. <yourResourceGroupID>: Replace with your actual resource group ID. <yourOrganizationID>: Replace with your actual organization ID. <yourInstanceID>: Replace with your actual instance ID. <Endpoint>: Replace with the actual endpoint of your product. s

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
        "<yourRegionID>",        // Replace with your actual region ID.
        "<yourAccessKeyID>",     // Replace with your actual AccessKey ID.
        "<yourAccessKeySecret>") // Replace with your actual AccessKey secret.
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Method = "POST"
    request.Domain = "<endpoint>" // The endpoint. This is an example value. Replace it
with the actual endpoint.
    request.Product = "CPFS"
    request.Version = "2017-06-26"
    // Because this is an RPC API, you must specify the ApiName (Action).
    request.ApiName = "DescribeFileSystems"
    // Business parameters
    request.QueryParams["FileSystemType"] = "bmcpfs"
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
```

`/*`

```
     When you use an STS AccessKey to call an RPC API, you must add the SecurityToken f
ield to the parameters.
     Example:
     request.QueryParams["SecurityToken"]="<yourSecurityToken>"
     Replace with your actual SecurityToken.
```

`*/`

```
    request.Headers["x-acs-caller-sdk-source"] = "ApiTestDemo" // Required. A descripti
on of the call source.
    request.Headers["x-acs-regionid"] = "<yourRegionID>" // Optional. Required for Ente
rprise Edition V3.15.0 and earlier. Replace with your actual region ID.
    request.Headers["x-acs-resourcegroupid"] = "<yourResourceGroupID>" // Optional. Rep
lace with your actual resource group ID.
    request.Headers["x-acs-organizationid"] = "<yourOrganizationID>" // Required. Repla
ce with your actual organization ID.
    // request.Headers["x-acs-instanceid"] = "<yourInstanceID>" // Optional. Required w
hen you modify, delete, or view the details of a single instance. Replace with your act ual instance ID.
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` s

#### 4.2.4 Error Handling

The Alibaba Cloud Go SDK returns an error message when a fault occurs on the server side or within the SDK. These errors implement Go's standard Error interface, which lets you handle them in the same way as standard Go errors.

**Handle errors simply**

Use the following code for simple error handling.

```
response, err := client.ProcessCommonRequest(request) if err != nil {
    panic(err)
```

`}`

## 5 API reference

### 5.1 Call APIs

#### 5.1.1 Overview

An API operation call is an HTTP GET request that is sent to a product's service endpoint and includes the required parameters as specified in the API reference. After the call, the system returns a response. Both the request and the response are encoded in UTF-8.

#### 5.1.2 Request structure

**Service endpoint**

For more information about how to obtain the endpoint for a product, see Obtain endpoint information.

**HTTP method**

You can use the HTTP GET method to send requests. Include all request parameters in the request URL.

**Communication protocol**

Requests support both HTTP and HTTPS. Use HTTPS for improved security.

**Request parameters**

Each request must specify an operation using the Action parameter, such as CreateFileSystem. Each request must also include common request parameters and any operation-specific request parameters.

**Character encoding**

All requests and responses use UTF-8 encoding.

#### 5.1.3 API Authorization

To ensure account security, use the identity credentials of a Resource Access Management (RAM) user to call APIs. If you use a RAM user to call CPFS file storage APIs, create and attach an appropriate authorization policy to that RAM user. In RAM, you can grant permissions for the following actions on a CPFS resource.

| Categorization | List of Actions |
|---|---|
| File System | CreateFileSystem DeleteFileSystem DescribeFileSystems ModifyFileSystem |

#### 5.1.4 Response

API calls return data in a standard format. An HTTP status code in the 2xx range indicates a successful call, while a status code in the 4xx or 5xx range indicates a failed call.

### 5.2 RAM authorization

When a Resource Access Management (RAM) user uses OpenAPI to access resources of an Alibaba Cloud account, the system uses RAM to check permissions. This ensures that the resource owner has granted the required permissions to the caller.

**Background information**

By default, an Alibaba Cloud account or a RAM user can use the CPFS console or CPFS API to manage the resources they create. Authorization for operations is required in the following scenarios: A newly created RAM user lacks permissions to manage the resources of an Alibaba Cloud account. An Alibaba Cloud service needs to access CPFS resources, or CPFS needs to access another Alibaba Cloud service. Before you can perform an access-controlled operation on a CPFS resource, the resource owner must grant you permission for that resource and the specific API behavior. When another account uses the CPFS API to access the resources of an Alibaba Cloud account, Alibaba Cloud CPFS first checks permissions using RAM. This ensures that the resource owner has granted the required permissions to the caller. Different CPFS APIs determine which resource permissions to check based on the resources and API semantics involved.

**Rule details**

Each CPFS API determines which resource permissions to check based on the resources involved and the semantics of the API call.

### 5.3 Common Parameters

Common parameters include common request parameters, common header parameters, and common response parameters.

**Common Request Parameters**

Every API requires common request parameters. Table 1. Common Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The return value type. Only JSON is supported. |
| Version | String | Yes | The API version number. Enter it in YYYY-MM-DD format. The value is 2017-06-26. |

| AccessKeyId | String | Yes | The AccessKey ID used to access the service. |
|---|---|---|---|
| AccessKeySecre t | String | Yes | The AccessKey secret used to access the service. |
| RegionId | String | Yes | The region ID used to access the service. |
| Product | String | Yes | The product name for the API. The product name is CPFS. |

**Common Header Parameters**

| Name | Description |
|---|---|
| x-acs-organizationid | The organization ID on the Apsara Uni-manager Management Console. For details, see Get Organization ID. |
| x-acs-resourcegroupid | The resource group ID on the Apsara Uni-manager Management Console. For details, see Get Resource Group ID. |
| x-acs-instanceid | The instance ID for the operation. For details, see Get Instance ID. |

**Note**

When you call cloud product APIs, add the actual values for parameters such as **x-acs-**
**instanceid**, **x-acs-organizationid**, and **x-acs-resourcegroupid** to the request header
in your code. This specifies the instance ID of the current instance (the instance ID does not exist when you create instances or query instance lists), and its organization and resource group. If you do not add the actual values for these header parameters, the call defaults to the root organization and root resource group.

**Common Response Parameters**

API responses use a unified format. HTTP status codes indicate the call status. A 2xx HTTP status code indicates that the call succeeded. A 4xx or 5xx HTTP status code indicates that the call failed. Successful calls return data in JSON format. For each API call, whether successful or not, the system returns a unique RequestId.

**Get Region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top menu bar, click **Enterprise**.
3. In the navigation pane on the left, choose **Resource Management** > **Region**
**Management**.
4. Click the target organization name.
5. View the Region ID in the **Region List** on the right.

**Get Organization ID**

Retrieve the organization ID by calling an API. For details, see the GetOrganizationList section in the Apsara Uni-manager Management Console Developer Guide.

**Get Resource Group ID**

Retrieve the resource group ID by calling an API. For details, see the ListResourceGroup section in the Apsara Uni-manager Management Console Developer Guide.

**Get Instance ID**

1. Log on to the Apsara Uni-manager Management Console.
2. In the top menu bar, click **Product > Storage > Cloud Paralleled File System (CPFS)** .
3. In the navigation pane on the left, click **CPFS List**.
4. View the instance ID in the list and copy it.

### 5.4 File system

#### 5.4.1 CreateFileSystem

This topic describes how to create a CPFS file system by calling the CreateFileSystem operation.

**Request parameters**

| Name | Type | Requi red | Example value | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateFileSystem | A required parameter. If you construct an HTTP or HTTPS URL to send an API request, set Action to CreateFileSystem. |
| RegionId | String | Yes | cn-qingdao-exxx- d01 | The region ID. Call DescribeRegions to view the latest list of Alibaba Cloud regions. |
| ZoneId | String | Yes | cn-qingdao-exxx- axxx-a | The zone ID. This is a required parameter. |
| FileSystemType | String | Yes | bmcpfs | The file system type. Only bmcpfs is supported. |
| Capacity | Long | Yes | 20480 | The capacity in GiB. Valid values are multiples of 10240 and greater than 20480. For compute-optimized instances, the maximum capacity is 10240000. |

| StorageType | String | Yes | bm advance 300 _ _ _ private | The file system specification. This corresponds to fsSpec in fscd. For bmcpfs, only bm advance 300 private (compute- _ _ _ optimized instance) is supported. |
|---|---|---|---|---|
| ZoneId | String | Yes | cn-wulan-exxx- axxx-a | The zone ID. |
| ClusterId | String | Yes | a20231214-02cc | The Apsara Stack cluster ID. Call DescribeZones to retrieve this ID. |
| ProtocolType | String | Yes | CPFS | The file transfer protocol type. For bmcpfs, only CPFS is supported. |
| EncryptType | String | Yes | 0 | Set to 0 to disable encryption. Set to 1 to enable encryption. Encryption is not supported in Apsara Stack. |
| Description | String | No | - | The description. Specify a string that meets the following requirements. 1. The length must be 2 to 128 characters. Characters can be English letters, digits, or Chinese characters. 2. The string must start with an English letter (uppercase or lowercase) or a Chinese character. It cannot start with http:// or https://. 3. The string can contain digits, colons (:), underscores ( ), or _ hyphens (-). |

**Response data**

| Name | Type | Example value | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |
| FileSystemId | String | bmcpfs-01b06fa3 | The filesystem ID. |

**Examples**

Successful response

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```

#### 5.4.2 DeleteFileSystem

Deletes a CPFS file system.

**Request parameters**

| Name | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteFileSyste m | A required parameter. If you initiate an API request by constructing an HTTP or HTTPS URL, you must specify the Action parameter. Set the value to DeleteFileSystem. |
| RegionId | String | Yes | cn-qingdao- exxx-d01 | The ID of the region. You can call the DescribeRegions operation to view the list of regions. |
| ZoneId | String | No | cn-qingdao- exxx-axxx-a | The zone ID. |
| FileSystemId | String | Yes | bmcpfs- 0156ec1d | The ID of the file system. |

**Response parameters**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample success response

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```

#### 5.4.3 DescribeFileSystems

This topic describes how to call the DescribeFileSystems operation to query CPFS file systems that you have created.

**Request Parameters**

| > Document Versio | n: 20260701 |   |   | 3 |
|---|---|---|---|---|

| Name | Type | Requir ed | Example Value | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFileSyst ems | required parameter. For API requests you initiate by manually constructing HTTP/HTTPS URLs, Action is a required parameter. Value: DescribeFileSystems. |
| RegionId | String | Yes | cn-qingdao- exxx-d01 | The region ID. Call the DescribeRegions interface to view the list of regions. |
| ZoneId | String | No | cn-qingdao- exxx-axxx-a | Zone ID. |
| FileSystemId | String | No | bmcpfs- 0156ec1d | File system ID. |
| Description | String | No | - | Description. |
| FileSystemType | String | Yes | bmcpfs | File system type. |
| PageSize | Integer | No | 10(default value) | Page size. |
| PageNumber | Integer | No | 1(default value) | Page number. |

**Response Data**

| Name | Type | Example Value | Description |
|---|---|---|---|
| FileSystemId | String | bmcpfs-0156ec1d | File system ID. |

| Status | String | Running | File system status. All statuses are as follows: Initializing Running Deleting Scaling up Scaling down Starting Stopping Stopped |
|---|---|---|---|
| MeteredSize | Integer | 1000 | Used capacity, in GiB. |
| Capacity | Integer | 1000 | Total capacity, in GiB. |
| MountTarget | String | - | Mount target information. |
| MountTargetDomain | String | - | Mount target name. |

**Example**

Example of a normal response `{`

```json
    "FileSystems": {
        "FileSystem": [
```

`{`

```json
                "Status": "Running",
                "Description": "cpfs",
                "StorageType": "performance",
                "MountTargetCountLimit": 100,
                "ZoneId": "cn-wulan-exxx-axxx-a",
                "CreateTime": "2024-03-26T19:22:47CST",
                "MeteredIASize": 0,
                "SupportedFeatures": {
                    "SupportedFeature": [
```

`]` `},`

```json
                "MountTargets": {
                    "MountTarget": [
```

`]` `},`

```json
                "MeteredSize": 0,
                "QuotaSize": 40960,
                "EncryptType": 0,
                "ProtocolType": "CPFS",
                "Packages": {
                    "Package": [
```

`]` `},`

```json
                "FileSystemType": "bmcpfs",
                "FileSystemId": "bmcpfs-0156ec1d",
                "RegionId": "cn-wulan-***-d01",
                "VolumeSize": 40960
```

`}` `]` `},`

```json
    "TotalCount": 1,
    "RequestId": "4306B744-C87D-45C7-8083-64C4E153F46C",
    "PageSize": 10,
    "PageNumber": 1
```

`}`

#### 5.4.4 ModifyFileSystem

This topic describes how to call the ModifyFileSystem operation to modify a CPFS file system.

**Request parameters**

| Name | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | ModifyFileSyste m | Required parameter. If you manually construct an HTTP or HTTPS URL to send an API request, you must include the Action parameter. Set the value to ModifyFileSystem. |
|---|---|---|---|---|
| RegionId | String | Yes | cn-qingdao- exxx-d01 | The region ID. You can call DescribeRegions to view the list of regions. |
| ZoneId | String | No | cn-qingdao- exxx-axxx-a | The zone ID. |
| FileSystemId | String | Yes | bmcpfs- 0156ec1d | The file system ID. |
| Description | String | No | - | The description of the file system. |
| Capacity | Long | No | 20480 | The capacity of the file system. The value must be greater than 20480 and a multiple of 10240. Only scale- out is supported. |

**Response data**

| Name | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 473469C7-AA6F- 4DC5-B3DB- A3DC0DE3C83E | The request ID. |

**Examples**

Sample success response

```json
{"RequestId":"7EA4C27A-7EB5-47FD-89DE-EB274970CF87","FileSystemId":"bmcpfs-01b06fa3"}
```
