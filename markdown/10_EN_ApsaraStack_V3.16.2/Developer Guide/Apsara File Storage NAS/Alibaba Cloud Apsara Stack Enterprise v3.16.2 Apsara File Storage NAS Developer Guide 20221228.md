---
title: "Alibaba Cloud Apsara Stack Enterprise v3.16.2 Apsara File Storage NAS Developer Guide 20221228"
product_version: "V3.16.2"
doc_version: "20221228"
pdf_pages: 95
source_pdf: "a1c92bd8586d6963_Alibaba Cloud Apsara Stack Enterprise v3.16.2 Apsara File Storage NAS Developer Guide 20221228.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/01_ApsaraStackEnterprise/20230602/Alibaba%20Cloud%20Apsara%20Stack%20Enterprise%20v3.16.2%20Apsara%20File%20Storage%20NAS%20Developer%20Guide%2020221228.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack Enterprise v3.16.2 Apsara File Storage NAS Developer Guide 20221228

## Table of Contents

- 1 Preparations
  - 1.1 Log on to the API Tool console
  - 1.2 View the information about API operations
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain an STS AccessKey 3-tuple
  - 1.5 Obtain the values of common header parameters
  - 1.6 Obtain the endpoint of NAS
  - 1.7 Obtain NAS SDKs
- 2 Call examples for SDK for Java
  - 2.1 Quick start
  - 2.2 Use SDK
    - 2.2.1 Install NAS SDK for Java
    - 2.2.2 Configure authentication credentials
    - 2.2.3 Configure connection requests
    - 2.2.4 Initiate a request
    - 2.2.5 Handle errors
    - 2.2.6 Use CommonRequest to call API operations
- 3 Call examples for SDK for Python
  - 3.1 Quick start
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
    - 4.2.2 Request structure
  - 4.3 Region
    - 4.3.1 DescribeRegions
  - 4.4 NAS instance
    - 4.4.1 CreateFileSystem
    - 4.4.2 DeleteFileSystem
    - 4.4.3 ModifyFileSystem
    - 4.4.4 DescribeFileSystems
  - 4.5 Mount point
    - 4.5.1 CreateMountTarget
    - 4.5.2 DeleteMountTarget
    - 4.5.3 DescribeMountTargets
    - 4.5.4 ModifyMountTarget
  - 4.6 Permission group
    - 4.6.1 CreateAccessGroup
    - 4.6.2 DeleteAccessGroup
    - 4.6.3 ModifyAccessGroup
    - 4.6.4 DescribeAccessGroups
    - 4.6.5 CreateAccessRule
    - 4.6.6 DeleteAccessRule
    - 4.6.7 ModifyAccessRule
    - 4.6.8 DescribeAccessRules
  - 4.7 Appendix: Error codes
- 5 Appendixes
  - 5.1 Use the ASAPI gateway to call API operations
  - 5.2 Use the ASAPI gateway to make API calls
    - 5.2.1 Obtain an endpoint of ASAPI
    - 5.2.2 Obtain Apsara Stack SDKs
  - 5.3 STS overview
    - 5.3.1 What is STS?
    - 5.3.2 AssumeRole

## 1 Preparations

### 1.1 Log on to the API Tool console

You can log on to the API Tool console from the Apsara Uni-manager Management Console.

**Prerequisites**

Before you log on to the Apsara Uni-manager Management Console, the endpoint of the console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar and press
Enter.
2. Enter your username and password.
Obtain the username and password that are used to log on to the Apsara Uni-manager Management Console from the operations administrator.

> **Note:** When you log on to the Apsara Uni-manager Management Console for the first time, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Uppercase or lowercase letters
> Digits
> Special characters, which include ! @ # $ %

3. Click **Log On**.
4. If your account has multi-factor authentication (MFA) enabled, perform corresponding
operations in the following scenarios: You log on to the Apsara Uni-manager Management Console for the first time after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Enter the username and password again as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the Bind a virtual MFA device to enable MFA topic in Apsara Uni-manager Management Console User Guide.

5. In the top navigation bar, choose **Products > Others > API Tool**.

### 1.2 View the information about API operations

**operations**

This topic describes how to view the information about API operations. The information includes service names, API operation names, and API versions. The information is required when you use an SDK to call API operations.

**Context**

The API operations on the API Directory page are only for reference. For information about how to call API operations, see developer guides of the corresponding cloud services. If the information on the API Directory page is inconsistent with that in the developer guide of the corresponding cloud service, the information in the developer guide prevails.

**Procedure**

1. Go to the API Tool console. For more information, see Log on to the API Tool console.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the service that you want to use from the drop-down list,
enter a keyword of an API operation name in the search box, and then click Search.
4. View and record the service name, API operation name, and API version of the API operation
that you want to call.

### 1.3 Obtain an AccessKey pair

AccessKey credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of AccessKey credentials for authentication when you call API operations. This topic describes how to obtain an AccessKey pair.

**Context**

An AccessKey ID and an AccessKey secret are used to implement symmetric encryption and verify the identity of request senders. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt a signature string. AccessKey credentials can be assigned by RAM or STS: An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An AccessKey 3-tuple that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an STS AccessKey 3tuple. The Apsara Uni-manager Management Console provides AccessKey pairs for personal accounts and organizations. Only operations administrators and the administrators of level-1 organizations can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Uni-manager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the request headers that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The region ID, for example, cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For information about how to obtain an organization ID, see the "GetOrganizationList" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni- manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance on which an operation is performed. You can obtain the ID of a NAS file system from the NAS file system list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. In the upper-right corner of the homepage, move the pointer over the profile picture and click
**Personal Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of your account.

> **Note:** An AccessKey pair consists of an AccessKey ID and an AccessKey secret. These credentials provide full permissions on cloud resources within your account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. Click **Management Accesskey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.4 Obtain an STS AccessKey 3-tuple

This topic describes how to use Security Token Service (STS) to call Apsara Stack API operations.

**Background information**

STS allows you to manage temporary credentials to your Apsara Stack resources. You can use STS to call Apsara Stack API operations. An STS AccessKey 3-tuple consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to call API operations, you must specify an STS AccessKey 3-tuple. For more information about STS, see What is STS?

**Procedure**

1. Obtain the RAM role .
i. Log on to the Apsara Uni-manager Management Console. ii. Move the pointer over the profile picture in the upper-right corner of the page and click
**Personal Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your RAM role .
2. Obtain the STS AccessKey 3-tuple.

> **Note:** In the following sample code, replace the variables with the actual values. Delete the angle brackets <> in the final code.

public static void main(String[] args) { // Create and initialize a DefaultAcsClient instance. // Specify the region ID, AccessKey ID, and AccessKey secret. DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccess KeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); String assumeRole = callAssumeRole(client); if (StringUtils.isEmpty(assumeRole)) return; JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole); JSONObject credentials = assumeRoleJson.getJSONObject("Credentials"); // Obtain the STS AccessKey 3-tuple. String stsAK = credentials.getString("AccessKeyId"); String stsSK = credentials.getString("AccessKeySecret"); String stsToken = credentials.getString("SecurityToken"); } private static String callAssumeRole(IAcsClient client) { CommonRequest request = new CommonRequest(); // Replace sts.aliyuns.com with the endpoint of STS. The endpoint of STS is in the sts-vpc.${global:regio n}.${global:internet-domain} format. request.setSysDomain("sts.aliyuns.com"); request.setSysProduct("Sts"); request.setSysAction("AssumeRole"); request.setSysVersion("2015-04-01"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // Replace <yourRoleSessionName> with the name of the current session. request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>"); // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role in the preceding ste p. request.putQueryParameter("RoleArn", "<yourRoleArn>"); try { CommonResponse response = client.getCommonResponse(request); return response.getData(); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } return null; }
3. Use the STS AccessKey 3-tuple to call an API operation of a cloud service. The following sample
code provides an example on how to call the DescribeRegions operation of Apsara File Storage NAS.

> **Note:** In the following sample code, replace the variables with the actual values. Delete the angle brackets <> in the final code.

public static void main(String[] args) { // Replace "<yourRegionID>" with the actual region ID. // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessKey ID and AccessK ey secret of the 3-tuple obtained in the preceding step. DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccesskey>", "<yourStsAcc essSecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); CommonRequest request = new CommonRequest(); request.setSysDomain("nas.aliyuns.com"); request.setSysProduct("NAS"); request.setSysAction("DescribeRegions"); request.setSysVersion("2017-06-26"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // Replace "<yourRegionID>" with the actual region ID. request.putHeadParameter("x-acs-regionid", "<yourRegionID>"); // Replace "<yourStsToken>" with the security token of the 3-tuple obtained in the preceding step. request.putQueryParameter("SecurityToken", "<yourStsToken>"); // Optional. Replace "<yourResourceGroupID>" with the actual resource set ID. // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>"); // Required. Replace "<yourOrganizationID>" with the actual organization ID. request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>"); try { CommonResponse response = client.getCommonResponse(request); System.out.println(response.getData()); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } }

### 1.5 Obtain the values of common header parameters

**header parameters**

You must provide multiple header parameters when you call Apsara Stack API operations. This topic describes the header parameters and how to obtain the values of the parameters. This topic also describes the return values of some parameters after you call API operations.

**Header parameters**

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. For more information about how to obtain a region ID, see Obtain a region ID. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain an organization ID, see Obtain an organization ID. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain a resource set ID, see Obtain a resource set ID . |
| x-acs-instanceid | The ID of the NAS file system on which you want to perform operations. For more information about how to obtain a file system ID, see Obtain a file system ID. |

**Obtain a region ID**

1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources** > **Regions**.
4. Click the name of the organization whose region ID you want to view.
5. View the region ID in the **Regions** section.

**Obtain an organization ID**

You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide.

**Obtain a resource set ID**

You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer Guide.

**Obtain a file system ID**

You can obtain the ID of a NAS file system in the Apsara Uni-manager Management Console. Perform the following operations to obtain a file system ID:
1. Log on to the Apsara Uni-manager Management Console.
2. In the top navigation bar, choose **Products** > **Storage** > **NAS**.
3. In the left-side navigation pane, click **File System List**.
4. On the **File System List** page, view the ID of the NAS file system.

**Response parameters**

The following table describes the additional response parameters returned by default when you call operations to query the instances of cloud services.

| Parameter | Description |
|---|---|
| ResourceGroupName | The name of the resource set. |
| ResourceGroup | The ID of the resource set. |
| DepartmentName | The name of the organization. |
| Department | The ID of the organization. |

### 1.6 Obtain the endpoint of NAS

This topic describes how to obtain the endpoint of Apsara File Storage NAS.

**Background information**

When you call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must obtain the endpoint of your cloud service. You can obtain an endpoint from onsite Apsara Stack O&M engineers. You can also perform the following operations to obtain an endpoint.

**Procedure**

1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, choose **Products** > **Platforms** > **Apsara Infrastructure Management**
**Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for Registration Vars of Services . In the report list that appears,
click the name of the report.
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for

| NAS |   | . |
|---|---|---|
| Find | nas-yaochi |   |

5. Find nas-yaochi . Right-click the value in the **Service Registration** column and select **Show**
**More**.
On the **Details** page, view the **nas.openapi.endpoint** value, which is the endpoint .

### 1.7 Obtain NAS SDKs

When you call Apsara Stack API operations by using the Portable OpenAPI Proxy (POP) gateway, you must use an SDK of your cloud service. This topic describes how to obtain Apsara File Storage NAS SDKs. An SDK includes code and examples. You can create cloud applications by using an SDK in the programming language that you require. The SDKs for Java, Python, and Go are provided. You can obtain the SDKs from Apsara Stack SDKs based on your business requirements.

> **Note:** We recommend that you use an SDK for Java or Python. If you use SDKs in other programming languages, the SDKs may be incompatible with your system.

We recommend that you use the SDK core library that is provided on the Alibaba Cloud official website. The SDK core library is shared by all cloud services and is compatible with Apsara Stack. The following table provides links to the references and GitHub source code of NAS SDKs for different programming languages.

| Programming language | GitHub source code |
|---|---|
| Java | NAS SDK for Java |
| Python | NAS SDK for Python |

SDK for Java

## 2 Call examples for SDK for Java

### 2.1 Quick start

This topic describes how to obtain and use Apsara File Storage NAS SDK for Java.

**Prerequisites**

An authorized account and an AccessKey pair are obtained. The AccessKey pair consists of an AccessKey ID and an AccessKey secret. For more information, see Obtain an AccessKey pair. The endpoint of NAS is obtained. For more information, see Obtain the endpoint of NAS. Apsara Stack SDK for Java 1.8 or later is installed.

**Install NAS SDK for Java**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project.

> **Note:** To use a NAS SDK, you must install the core library of Apsara Stack SDK for Java and NAS SDK for Java. We recommend that you use the core library V4.5.17 or later, and use NAS SDK for Java V2.0.2.

**Use NAS SDK for Java**

To use NAS SDK for Java, perform the following steps:
1. Create and initialize a DefaultAcsClient instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and handle the response or exceptions.

> **Note:** In the following sample code, replace the variables with the actual values. Delete the angle brackets <> in the final code.

import com.aliyuncs.profile.DefaultProfile; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsRequest; import com.aliyuncs.nas.model.v20170626.DescribeFileSystemsResponse; public class Main { public static void main(String[] args) { // Create and initialize a DefaultAcsClient instance. DefaultProfile profile = DefaultProfile.getProfile( "<yourRegionID>" // Replace the parameter with the region ID SDK for Java <yourRegionID>, // Replace the parameter with the region ID. "<yourAccessKeyID>", // Replace the parameter with your AccessKey ID. "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret. // Specify the endpoint of the service. Replace the variables with the actual values. profile.addEndpoint("<yourRegionID>", "<Product>", "<Endpoint>"); // Configure the request parameters. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true);// Ignore the certificate. clientConfig.setReadTimeoutMillis(<readTimeout>);// Optional. Specify the read timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>);// Optional. Specify the connection ti meout period. Unit: milliseconds. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>);// Optional. Specify the maximum num ber of requests for each host. clientConfig.setMaxRequests(<maxRequests>);// Optional. Specify the maximum number of requests. clientConfig.setProtocolType(ProtocolType.HTTP); // Optional. Specify the request protocol. Default v alue: HTTP. /* Optional. Specify the IP address and port of the proxy. clientConfig.setHttpProxy("http://192.168.XX.XX:33XX"); or clientConfig.setHttpsProxy("https://192.168.XX.XX:33XX"); */ profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); // Create an API request and configure the parameters. DescribeFileSystemsRequest request = new DescribeFileSystemsRequest(); // Business parameters. request.setPageSize(10); request.setPageNumber(1); // The header parameters that are used for resource isolation. Replace the values with your actual or ganization ID and resource set ID. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "11"); // Initiate the request and handle the response or exceptions. DescribeFileSystemsResponse response; try { response = client.getAcsResponse(request); for (DescribeFileSystemsResponse.FileSystem fileSystem:rsp.getFileSystems()) { System.out.println(fileSystem.getFileSystemId()); } } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { e.printStackTrace(); } } }

### 2.2 Use SDK

#### 2.2.1 Install NAS SDK for Java

SDK for Java This topic describes how to install NAS SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, see Alibaba Cloud SDKs. To use a NAS SDK, you must install the core library of Apsara Stack SDK for Java and NAS SDK for Java. We recommend that you use the core library V4.5.17 or later, and use NAS SDK for Java V2.0.2. To use NAS SDK for Java, you must install the core library of Apsara Stack SDK for Java and add the following dependencies to the pom.xml file. For more information about the specific SDK version, see Alibaba Cloud SDKs. <!-- Alibaba Cloud SDK for Java --> <dependency> <groupId>com.aliyun</groupId> <artifactId>aliyun-java-sdk-core</artifactId> <version>4.5.17</version> </dependency> <!-- NAS Java SDK --> <dependency> <groupId>com.aliyun</groupId> <artifactId>aliyun-java-sdk-nas</artifactId> <version>2.0.2</version> </dependency>

#### 2.2.2 Configure authentication credentials

When you use Alibaba Cloud SDKs to access Apsara Stack services, you must provide an Apsara Stack tenant account for authentication. This topic describes how to configure authentication credentials. Apsara Stack SDK for Java supports authentication based on AccessKey pairs. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must specify the AccessKey pair as the credentials when you initialize the client.

> **Note:** Do not disclose any code that contains your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

DefaultProfile profile = DefaultProfile.getProfile( "<yourRegionID>", // Replace the parameter with the region ID. "<yourAccessKeyID>", // Replace the parameter with your AccessKey ID. "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret. SDK for Java

> **Note:** In the preceding sample code, replace the variables with the actual values. Delete the angle brackets <> in the final code.

#### 2.2.3 Configure connection requests

This topic describes how to configure a connection request by using the HttpClientConfig object. You can use the following code to configure the HttpClientConfig object. We recommend that you select and configure the following parameters based on your business requirements.

> **Note:** You must use actual values to replace the variables in the following sample code. Do not retain the angle brackets (<>) in the final code.
> The following list describes the variables:
> <readTimeout>: Specify the read timeout period based on your business requirements. Unit: milliseconds.
> <connectionTimeout>: Specify the connection timeout period based on your business requirements. Unit: milliseconds.
> <maxRequestsPerHost>: Specify the maximum number of requests that are supported by each server based on your business requirements. The supported data type is INTEGER.
> <maxRequests>: Specify the maximum number of requests based on your business requirements. The supported data type is INTEGER.
> <http://192.168.XX.XX:33XX>: Replace it with the actual IP address and port of the proxy.

SDK for Java // Obtain the HttpClientConfig object. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); // Specify whether to ignore certificates. clientConfig.setIgnoreSSLCerts(true); // (Optional) Specify the read timeout period. Unit: milliseconds. clientConfig.setReadTimeoutMillis(<readTimeout>); // (Optional) Specify the connection timeout period. Unit: milliseconds. clientConfig.setConnectionTimeoutMillis(<connectionTimeout>); // (Optional) Specify the maximum number of requests that are supported by each server. The supported da ta type is INTEGER. clientConfig.setMaxRequestsPerHost(<maxRequestsPerHost>); // (Optional) Specify the maximum number of requests. The supported data type is INTEGER. clientConfig.setMaxRequests(<maxRequests>); // (Optional) Specify the protocol type. clientConfig.setProtocolType(ProtocolType.HTTP); /** (Optional) Specify whether to configure the proxy based on your business requirements. The following c ode is available: clientConfig.setHttpProxy("<http://192.168.XX.XX:33XX>"); Or clientConfig.setHttpsProxy("<https://192.168.XX.XX:33XX>"); Replace https://192.168.XX.XX:33XX with the actual IP address and port of the proxy. */ profile.setHttpClientConfig(clientConfig);

#### 2.2.4 Initiate a request

This topic describes how to use the SDK for Java to initiate a request.

**Procedure**

1. Create an AcsClient instance.
IAcsClient client = new DefaultAcsClient(profile);
2. Create a request.
Name the request in the ${apiName}Request format. Replace ${apiName} with the name of the API operation, for example, DescribeFileSystems. When multiple service SDKs are used, different requests may have the same name. You can differentiate the requests based on package names. DescribeFileSystemsRequest request = new DescribeFileSystemsRequest(); // Business parameters. request.setFileSystemType("all"); request.setPageSize(10); // The header parameters that are used for resource isolation. Replace the values with your actual organi zation ID and resource set ID. request.putHeadParameter("x-acs-organizationid", "1"); request.putHeadParameter("x-acs-resourcegroupid", "");
3. Initiate the request and handle the response.
SDK for Java try { DescribeFileSystemsResponse response = client.getAcsResponse(request); System.out.println(new Gson().toJson(response)); } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { System.out.println("ErrCode:" + e.getErrCode()); System.out.println("ErrMsg:" + e.getErrMsg()); System.out.println("RequestId:" + e.getRequestId()); } In normal cases, all returned fields are deserialized into the response. You can call response.get XXX() to obtain the values of the response fields. instanceStatus = response.getStatus(); However, if an exception occurs or you need to obtain the original HTTP response, call doAction () to obtain the original response. HttpResponse response = client.doAction(request);

#### 2.2.5 Handle errors

If the server or SDK encounters an error when you use the SDK for Java, the SDK returns an error response. The error response contains an error code and an error message. Among the errors returned by the SDK for Java, you do not need to handle the SDK errors, but must solve the server errors.

| ServerException |   |
|---|---|
| ClientException |   |

ServerException indicates a server error. ClientException indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message: com.aliyuncs.exceptions.ClientException: InvalidAccessKeyId.NotFound : Specified access key is not found. If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: SDK for Java try { FooResponse response = client.getAcsResponse(request); // Handle the response. }catch (ServerException e){ // You can add your error handling logic here. // For example, display the error message. System.out.println("ErrorCode=" + e.getErrCode()); System.out.println("ErrorMessage=" + e.getErrMsg()); // If you are unable to fix the error, submit a ticket and provide RequestId to Alibaba Cloud technical supp ort personnel. System.out.println("ResponseId=" + e.getRequestId()); }catch (ClientException e){ // You can add your error handling logic here. // For example, display the error message. System.out.println("ErrorCode=" + e.getErrCode()); System.out.println("ErrorMessage=" + e.getErrMsg()); }

#### 2.2.6 Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API reference of Apsara File Storage NAS. Domain: the endpoint of NAS. Version: the version number of the API, in the YYYY-MM-DD format. You can obtain the API version in the Common parameters topic of the API reference. Operation information: the name of the API operation that you want to call. You need to obtain the value of the Action parameter and specify an API operation in request.se tSysAction("<Action>") . For example, if you want to call the CreateFileSystem operation, you must use request.setSysActi on("CreateFileSystem") to specify the API operation when you initiate a CommonRequest request. SDK for Java

**Example: Call an RPC API operation**

This example shows how to call the DescribeFileSystems operation to query file systems.

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> You need to configure the following variables:
> <yourRegionID>: Replace the parameter with the region ID.
> <yourAccessKeyID>: Replace the parameter with your AccessKey ID.
> <yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
> <yourSecurityToken>: Replace the parameter with your security token.
> <yourResourceGroupID>: Replace the parameter with the resource set ID.
> <yourOrganizationID>: Replace the parameter with the organization ID.
> <yourInstanceID>: Replace the parameter with the instance ID.
> <http://192.168.XX.XX:33XX>: Replace the parameter with the IP address and port of the proxy.

import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; class DescribeFileSystems { public static void main(String[] args) { // Create and initialize a DefaultAcsClient instance. DefaultProfile profile = DefaultProfile.getProfile( "<yourRegionID>", // Replace the parameter with the region ID. "<yourAccessKeyID>", // Replace the parameter with your AccessKey ID. "<yourAccessKeySecret>"); // Replace the parameter with your AccessKey secret. HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setProtocolType(ProtocolType.HTTP); /** Optional. Configure the HTTP proxy based on your business requirements. Format: clientConfig.setHttpProxy("http://192.168.XX.XX:33XX"); Specify the IP address and port of the proxy. */ profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); // Create an API request and configure the parameters. CommonRequest request = new CommonRequest(); // Specify the endpoint of the service. request.setSysDomain("nas.cn-hangzhou.com"); request.setSysProduct("NAS"); request.setSysVersion("2017-06-26"); SDK for Java q y ( ) request.setSysAction("DescribeFileSystems"); request.putQueryParameter("PageNumber", "1"); request.putQueryParameter("PageSize", "10"); request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");// Optional. Specify th e resource set ID. request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>");// Required. Specify the o rganization ID. request.putHeadParameter("x-acs-caller-sdk-source","ApiTestDemo");// Required. Specify the source o f the API call. request.putHeadParameter("x-acs-regionid", "<yourRegionID>");// Optional. Specify the region ID. If yo u use Apsara Stack Enterprise V3.15.0 or earlier, this parameter is required. request.putHeadParameter("x-acs-instanceid", "<yourInstanceID>");// Optional Specify the instance ID . If you need to delete, modify, or query an instance, this parameter is required. /** When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field i n the request parameters. Format: request.putQueryParameter("SecurityToken", "<yourSecurityToken>"); Specify your security token. */ try { CommonResponse response = client.getCommonResponse(request); System.out.println(response.getData()); } catch (ServerException e) { e.printStackTrace(); } catch (ClientException e) { System.out.println("ErrCode:" + e.getErrCode()); System.out.println("ErrMsg:" + e.getErrMsg()); System.out.println("RequestId:" + e.getRequestId()); } } } SDK for Python

## 3 Call examples for SDK for Python

**Python**

### 3.1 Quick start

This topic describes how to obtain and use Apsara File Storage NAS SDK for Python.

**Prerequisites**

An authorized account and an AccessKey pair (AccessKey ID and AccessKey secret) are obtained. For more information, see Obtain an AccessKey pair. The endpoint of NAS is obtained. For more information, see Obtain the endpoint of NAS.

**Install the SDK for Python**

1. Install the SDK core library.
If you use Python 2.x, run the following command to install the SDK core library: pip install aliyun-python-sdk-core If you use Python 3.x, run the following command to install the SDK core library: pip3 install aliyun-python-sdk-core-v3
2. Install NAS SDK.
If you use Python 2.x, run the following command to install NAS SDK: pip install aliyun-python-sdk-nas If you use Python 3.x, run the following command to install NAS SDK: pip3 install aliyun-python-sdk-nas

**Use the SDK for Python**

To use the SDK for Python, perform the following steps:
1. Create a client instance. When you create a client instance, you must obtain a region ID,
AccessKey ID, and AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and handle the response or exception.
SDK for Python
#!/usr/bin/env python
# coding=utf-8
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
# global config
region_id = '<yourRegionID>' # Specify the region ID. access_key = '<yourAccessKeyID>' # Specify the AccessKey ID. acces_secret = '<yourAccessKeySecret>' # Specify the AccessKey secret.
# product config
product_name = 'NAS' # Specify the service name. endpoint = 'nas.aliyuns.com' # Specify endpoint of the service.
# create client
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, acces_secret, region_id)
# setup request
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest() request.set_accept_format('json') # Specify the response format.
# get response
response = clt.do_action_with_exception(request) print(response)

### 3.2 Use SDK

#### 3.2.1 Install the SDK for Python

This topic describes how to install Alibaba Cloud SDK for Python and Apsara File Storage NAS SDK for Python.
1. Install Alibaba Cloud SDK for Python.
Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python. For example, if you want to use NAS SDK for Python, you must install the SDK core library for Python and NAS SDK for Python.

If you use Python 2.x, run the following command to install the SDK core library: pip install aliyun-python-sdk-core If you use Python 3.x, run the following command to install the SDK core library: pip3 install aliyun-python-sdk-core-v3
2. Install NAS SDK for Python.
If you use Python 2.x, run the following command to install NAS SDK for Python: pip install aliyun-python-sdk-nas If you use Python 3.x, run the following command to install NAS SDK for Python: SDK for Python pip3 install aliyun-python-sdk-nas

#### 3.2.2 Configure authentication credentials

When you use an Apsara Stack SDK to access Apsara Stack services, you must provide an authorized account for authentication. NAS SDK for Python supports authentication based on an AccessKey pair. For more information about how to obtain an AccessKey pair, see Obtain an AccessKey pair. If you want to use your AccessKey pair to access Apsara Stack, you must configure the AccessKey pair as the credentials when you initialize the client.

> **Important:** Do not disclose any code containing your AccessKey pair. For example, do not commit the code to public GitHub projects. Otherwise, your account may be compromised.

clt = client.AcsClient(access_key, access_secret, region_id)

#### 3.2.3 Set HTTPS requests

Apsara Stack SDK for Python allows you to initiate API requests over HTTP and HTTPS. You can specify the HTTP or HTTPS protocol for a specific request, or set a global default protocol.

> **Note:** The default HTTP or HTTPS protocol of a service takes precedence over the global default protocol.

**Add OpenSSL support**

The HTTPS protocol support of Apsara Stack SDK for Python is based on the OpenSSL support in Python. To use Apsara Stack SDK for Python to send HTTPS requests, you must add OpenSSL support in Python. OpenSSL supports TLS 1.2 and later. Run the python -c "import ssl" command to check whether your Python environment supports OpenSSL. If the error message ImportError: No module named ssl is not returned, OpenSSL is already supported. Otherwise, run the following command to install it: pip install pyopenssl

**Set the protocol to HTTP or HTTPS for a single request**

The following sample code provides an example on how to set HTTPS as the protocol for a request: request = DescribeInstancesRequest() request.set_protocol_type("https")
# Set the value to https or http.
SDK for Python

**Set a global default protocol**

The following sample code provides an example on how to set a global default protocol: import aliyunsdkcore.request aliyunsdkcore.request.set_default_protocol_type("https")
# Create a request and call client.do_action_with_exception() to send the request.

#### 3.2.4 Initiate a request

This topic describes how to use Apsara File Storage NAS SDK for Python to initiate a request.

**Procedure**

1. Import NAS SDK for Python.
from aliyunsdkcore import client from aliyunsdkcore.profile import region_provider from aliyunsdknas.request.v20170626 import DescribeFileSystemsRequest
2. Create an AcsClient instance.
region_provider.modify_point(product_name, region_id, endpoint) clt = client.AcsClient(access_key, access_secret, region_id)
3. Create a request object.
request = DescribeFileSystemsRequest.DescribeFileSystemsRequest() request.set_accept_format('json')
4. Initiate the request and handle the response.
response = clt.do_action_with_exception(request) print(response)

#### 3.2.5 Handle errors

If the server or SDK encounters an error when you use the SDK for Python, the SDK returns an error response. The error response contains an error code and an error message. Among the errors returned by the SDK for Python, you do not need to handle the SDK errors, but must solve the server errors.

| ServerException |   |
|---|---|
| ClientException |   |

ServerException indicates a server error. ClientException indicates an SDK error. For example, if the following error occurs, you can modify the AccessKey ID based on the error message: aliyunsdkcore.acs\_exception.exceptions.ServerException: HTTP Status: 404 Error:InvalidAccessKeyId.NotFo und Specified access key is not found. SDK for Python If you want to handle the SDK errors returned by the SDK, refer to the following example to write your code: try: response = client.do_action_with_exception(request) except ServerException as e:
# You can add your error handling logic here.
# For example, display the error message.
print e.get_http_status() print e.get_error_code() print e.get_error_msg()

#### 3.2.6 Use CommonRequest to call API operations

If you want to call the API operations of a cloud service that does not provide SDKs, or you cannot use an SDK to call API operations whose requests and responses meet your business requirements, you can use CommonRequest to call API operations. You can use CommonRequest to call all API operations.

**Benefits**

CommonRequest provides the following benefits: Lightweight: You only need to download the core package. You do not need to download and install SDKs of Apsara Stack services. Easy to use: You can call the newly released API operations of a service without the need to update the SDK for the service. Fast iteration.

**Use CommonRequest to call an API operation**

If you want to send a CommonRequest request, you must obtain the values of the following parameters. You can obtain the values of these parameters from the API reference of Apsara File Storage NAS. Domain: the endpoint of NAS. Version: the version number of the API, in the YYYY-MM-DD format. You can obtain the API version in the Common parameters topic of the API reference. Operation information: the name of the API operation that you want to call. You need to obtain the value of the Action parameter and specify an API operation in request.se t_action_name("Action") . For example, if you want to call the CreateFileSystem operation, you must use request.set_action _name("CreateFileSystem") to specify the API operation when you initiate a CommonRequest request.

**Example: Call an RPC API operation**

This example shows how to call the DescribeFileSystems operation to query file systems. SDK for Python

> **Note:** In the following code, replace the variables with actual values. Delete the angle brackets <> in the final code.
> You need to configure the following variables:
> <yourRegionID>: Replace the parameter with the region ID.
> <yourAccessKeyID>: Replace the parameter with your AccessKey ID.
> <yourAccessKeySecret>: Replace the parameter with your AccessKey secret.
> <yourSecurityToken>: Replace the parameter with your security token.
> <yourResourceGroupID>: Replace the parameter with the resource set ID.
> <yourOrganizationID>: Replace the parameter with the organization ID.
> <yourInstanceID>: Replace the parameter with the instance ID.

SDK for Python from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest
# Specify the AccessKey ID, AccessKey secret, and region ID.
client = AcsClient('{<yourAccessKeyID>}', '{<yourAccessKeySecret>}', '{<yourRegionID>}') request = CommonRequest() request.set_product('NAS') request.set_action_name('DescribeFileSystems') request.set_version('2017-06-26') request.set_domain('<nas.aliyuncs.com>') # Specify the endpoint of the service.
# or:
# request = = CommonRequest(product='NAS', action_name='DescribeFileSystems',version='2017-06-26',do
main='nas.aliyuncs.com')
######
# Specify the request protocol. Valid values: https and http. Default value: http.
# You can specify HTTPS as the protocol:
# request.set_protocol_type('https')
######
request.set_accept_format('json') request.set_method('POST') request.add_query_param('PageNumber','1') request.add_query_param('PageSize','30')
######
# When you use an STS AccessKey 3-tuple to call an API operation, you must add the SecurityToken field in t
he request parameters.
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
# Optional. Specify the region ID. If you use Apsara Stack Enterprise V3.15.0 or earlier, this parameter is requ
ired. request.add_header("x-acs-regionid", "<yourRegionID>")
# Optional. Specify the instance ID. If you need to delete, modify, or query an instance, this parameter is req
uired.
# request.add_header("x-acs-instanceid", "<yourInstanceID>")
response = client.do_action_with_exception(request) print(str(response, encoding = 'utf-8'))

## 4 API Reference

### 4.1 List of operations by function

APIs lists the APIs provided by NAS. APIs

| Number | Category | API | Description |
|---|---|---|---|
| 1 | Region | DescribeRegions | Returns all region IDs. |
| 2 | NAS | CreateFileSystem | Creates a NAS instance. |
| 3 | NAS | DeleteFileSystem | Deletes an existing NAS instance. |
| 4 | NAS | DescribeFileSystems | Returns the description of a NAS instance. |
| 5 | NAS | ModifyFileSystem | Modifies the information of a NAS instance. |
| 6 | Mount point | CreateMountTarget | Create a mount point. |
| 7 | Mount point | DeleteMountTarget | Deletes an existing mount point. |
| 8 | Mount point | DescribeMountTargets | Returns the description of a mount point. |
| 9 | Mount point | ModifyMountTarget | Modifies the attributes of a mount point. |
| 10 | Permission group | CreateAccessGroup | Creates a permission group. |
| 11 | Permission group | DeleteAccessGroup | Deletes an existing permission group. |
| 12 | Permission group | DescribeAccessGroups | Returns the description of a permission group. |
| 13 | Permission group | ModifyAccessGroup | Modifies the attributes of a permission group. |
| 14 | Permission group | CreateAccessRule | Creates a permission rule. |
| 15 | Permission group | DeleteAccessRule | Deletes an existing permission rule. |

| Number | Category | API | Description |
|---|---|---|---|
| 16 | Permission group | DescribeAccessRules | Returns the description of a permission rule. |
| 17 | Permission group | ModifyAccessRule | Modifies the attributes of a permission rule. |

### 4.2 Make API requests

#### 4.2.1 Common parameters

**Common request parameters**

Common request parameters are available to all APIs. Common request parameters

| Name | Type | Required | Description |
|---|---|---|---|
| Format | String | No | The type of response. Valid values: JSON and XML. Default value: JSON. |
| Version | String | Yes | The API version, which is represented as a date in the format of YYYY-MM-DD . The current API version is 2017-06- 26. |
| AccessKeyId | String | Yes | The AccessKey ID that is used to access services. For more information, see Obtain an AccessKey pair. |
| Signature | String | Yes | The string that represents signature. |
| SignatureMethod | String | Yes | The type of signature. Valid value: HMAC-SHA1. |
| Timestamp | String | Yes | The time when you send the request. Specify the time in the ISO 8601 standard in the YYYY- MM-DDThh:mm:ssZ format. The time must be in UTC. For example, 2017-05- 26T12:00:00Z. |
| SignatureVersion | String | Yes | The version of the signature algorithm. The current version is 1.0. |

|   | MM-DDThh:mm:ssZ |
|---|---|

| Apsara File Storage NAS |   |   | Developer Guide·API Referenc |
|---|---|---|---|

| Name | Type | Required | Description |
|---|---|---|---|
| SecurityToken | String | No | If Security Token Service (STS) credentials are required, you must specify this parameter. |
| SignatureNonce | String | No | A unique random number. This parameter is used to prevent replay attacks. You must use different random numbers for different requests. |

**Sample request**

GET https://nas.regionid.example.com/?Action=<Action> &Format=xml &Version=2017-06-26 &AccessKeyId=key-test &Signature=Pc5***%3D &SignatureMethod=HMAC-SHA1 &SignatureNonce=15215528852396 &SignatureVersion=1.0 &Timestamp=2012-06-01T12:00:00Z ...

**Common response parameters**

Whenever you send an API request, a GUID that is included in the **RequestId** parameter will be returned to you regardless of whether the request is successful. Common response parameters

| Name | Type | Description |
|---|---|---|
| RequestId | Integer | The GUID generated by Alibaba Cloud for the request. |

**Sample response**

XML format <? xml version="1.0" encoding="UTF-8"? > <An API name+Response> <! --Returned RequestId--> <RequestId> 6D9F62C5-BF52-447C-AA34-C77F7AFCCC12</RequestId> <! --Response parameters--> </An API name+Response> JSON format { "RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Response parameters*/ }

#### 4.2.2 Request structure

**Endpoints**

The format of a NAS API endpoint is described in Generate the endpoint of ASAPI.

**Protocols**

You can send API requests by using HTTP or HTTPS. We recommend that you use HTTPS to ensure high security.

**Request methods**

You can send requests by using the HTTP GET method. This method requires that you specify request parameters in the request URL.

**Request parameters**

You must specify the required operation for the Action parameter of each request, such as DescribeRegions . Each operation must include common request parameters and other request parameters that are specific to the operation.

**Character encoding**

Requests or responses are all encoded by UTF-8 .

### 4.3 Region

#### 4.3.1 DescribeRegions

Queries available regions.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRegions | The operation that you want to perform. Set the value to DescribeRegions. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| PageSize | Integer | No | 10 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| FileSystemType | String | No | standard | The type of the file system. Valid values: standard: the default value, which indicates General-purpose NAS file systems. extreme: Extreme NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| Regions | Array of Region |   | The list of regions. |
| Region |   |   |   |
| LocalName | String | East China 1 | The name of the region. |
| RegionEndpoin t | String | nas.cn- hangzhou.aliyuncs. com | The endpoint of the region. |
| RegionId | String | cn-hangzhou | The ID of the region. |
| RequestId | String | A70BEE5D-76D3- 49FB-B58F- 1F398211**** | The ID of the request. |

| Developer Guide·A | PI Reference |   | Apsara File Storage NA |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 4 | The total number of regions. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DescribeRegions &<Common request parameters> Sample success responses XML format <TotalCount>4</TotalCount> <PageSize>2</PageSize> <RequestId>A70BEE5D-76D3-49FB-B58F-1F398211****</RequestId> <PageNumber>1</PageNumber> <Regions> <RegionId>cn-hangzhou</RegionId> <RegionEndpoint>nas.cn-hangzhou.aliyuncs.com</RegionEndpoint> <LocalName>East China 1</LocalName> </Regions> JSON format { "TotalCount": 4, "PageSize": 2, "RequestId": "A70BEE5D-76D3-49FB-B58F-1F398211****", "PageNumber": 1, "Regions": { "RegionId": "cn-hangzhou", "RegionEndpoint": "nas.cn-hangzhou.aliyuncs.com", "LocalName": "East China 1" } }

### 4.4 NAS instance

#### 4.4.1 CreateFileSystem

Creates a file system.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateFileSystem | The operation that you want to perform. Set the value to CreateFileSystem. |
| ProtocolType | String | Yes | NFS | The type of the protocol. Valid values: NFS: Network File System (NFS) SMB: Server Message Block (SMB) |
| StorageType | String | Yes | Performance | The type of the storage. Valid values: Performance: Performance NAS file systems Capacity: Capacity NAS file systems |
| ZoneId | String | No | cn-hangzhou-b | The ID of the zone. Each region has multiple isolated locations known as zones. The power supply and network of each zone are independent. Note An Elastic Compute Service (ECS) instance can access a NAS file system in the same region but a different zone. We recommend that you select the zone where the ECS instance resides. This prevents cross-zone latency between the file system and the ECS instance. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| EncryptType | Integer | No | 1 | Specifies whether to encrypt the data in the file system. The EncryptType parameter is not supported. |
| Description | String | No | balabala | The description of the file system. Limits: The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https:// . The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |
| VolumeSize | Long | No | 100 | The capacity of the General-purpose NAS file system. Unit: bytes. Valid values: Valid values for Capacity NAS file systems: 0 to 10 PB. Valid values for Performance NAS file systems: 0 to 1 PB. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| FileSystemId | String | 1ca404**** | The ID of the file system that is created. |
| RequestId | String | 98696EF0-1607- 4E9D-B01D- F20930B6**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/?Action=CreateFileSystem &ProtocolType=NFS &StorageType=Performance &<Common request parameters> Sample success responses XML format <RequestId>98696EF0-1607-4E9D-B01D-F20930B6****</RequestId> <FileSystemId>1ca404****</FileSystemId> JSON format { "RequestId": "98696EF0-1607-4E9D-B01D-F20930B6****", "FileSystemId": "1ca404****" }

#### 4.4.2 DeleteFileSystem

Deletes a file system. Before you delete a file system, you must remove all the mount targets from the file system. After the file system is deleted, the data on the file system cannot be restored. Proceed with caution.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteFileSystem | The operation that you want to perform. Set the value to DeleteFileSystem. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DeleteFileSystem &FileSystemId=1ca404**** &<Common request parameters> Sample success responses XML format <RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId> JSON format { "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****" }

#### 4.4.3 ModifyFileSystem

Modifies the details of a file system.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyFileSyste m | The operation that you want to perform. Set the value to ModifyFileSystem. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| Description | String | No | N/A | The description of the file system. Limits: The description must be 2 to 128 characters in length. The description must start with a letter but cannot start with http:// or https://. The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| VolumeSize | Long | No | 1000 | The capacity of the file system. Valid values: Valid values for NAS Capacity file systems: 0 to 10 PB. Valid values for NAS Performance file systems: 0 to 1 PB. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=ModifyFileSystem &FileSystemId=1ca404**** &<Common request parameters> Sample success responses XML format <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId> JSON format { "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****" }

#### 4.4.4 DescribeFileSystems

Queries the information of file systems.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFileSyste ms | The operation that you want to perform. Set the value to DescribeFileSystems. |
| FileSystemId | String | No | 109c04**** | The ID of the file system. |
| FileSystemType | String | No | standard | The type of the file system. Valid value: standard, which indicates General-purpose NAS file systems. |
| VpcId | String | No | vpc- bp1sevsgtqvk5g xbl**** | The ID of the virtual private cloud (VPC). If you want to mount the file system on an Elastic Compute Service (ECS) instance, you must set this parameter to the VPC where the ECS instance resides. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 035B3A3A-E514- 4B41-B906- 5D906CFB**** | The ID of the request. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| TotalCount | Integer | 1 | The total number of file systems. |
| FileSystems | Array of FileSystem |   | The list of file systems. |
| FileSystem |   |   |   |
| Bandwidth | Long | 150 | The bandwidth of the file system. Unit: MB/s. This parameter is unavailable for General-purpose NAS file systems. |
| ChargeType | String | PayAsYouGo | The billing method of the file system. Valid values: Subscription: The subscription billing method is used. PayAsYouGo: The pay-as-you-go billing method is used. Package: A storage plan is attached to the file system. |
| CreateTime | String | 2017-05- 27T15:43:06CST | The time when the file system was created. |
| Description | String | This can be the description of the created file system. | The description of the file system. |
| EncryptType | Integer | 1 | The type of the encryption. Valid values: 0: The file system is not encrypted. 1: The file system is encrypted. |
| ExpiredTime | String | 1572174830000 | The time when the file system expires. |
| FileSystemId | String | 109c04**** | The ID of the file system. |
| FileSystemType | String | all | The type of the file system. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Ldap | Struct |   | The details of the Lightweight Directory Access Protocol (LDAP) service. This parameter is available only for CPFS file systems. |
| BindDN | String | cn=alibaba,dc=com | An LDAP entry. |
| SearchBase | String | dc=example | An LDAP search base. |
| URI | String | ldap://ldap.exampl e.example | The URL of an LDAP server. |
| MeteredIASize | Long | 1000 | The used capacity of the Infrequent Access (IA) storage medium. |
| MeteredSize | Long | 1611661312 | The used capacity of the file system. The value of this parameter is the maximum used capacity of the file system over the last hour. Unit: bytes. |
| MountTargets | Array of MountTarget |   | The list of mount targets. |
| MountTarget |   |   |   |
| AccessGroupN ame | String | test-001 | The name of the permission group that is attached to the mount target. |
| MountTargetD omain | String | 109c042666- w****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| NetworkType | String | vpc | The type of the network. Valid values: vpc: the virtual private cloud (VPC) network. classic: the classic network. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. |
| VpcId | String | vpc- bp1sevsgtqvk5gxbl **** | The ID of the VPC. |
| VswId | String | vsw- bp1omfzsszekkvax n**** | The ID of the vSwitch. |
| Packages | Array of Package |   | The list of storage plans. |
| Package |   |   |   |
| ExpiredTime | String | 2020-01- 05T16:00:00Z | The time when the storage plan expires. |
| PackageId | String | naspackage- 0be9c4b624-37**** | The ID of the storage plan. |
| PackageType | String | hybrid | The type of the storage plan. |
| Size | Long | 107374182400 | The capacity of the storage plan. |
| StartTime | String | 2019-12- 05T01:40:56Z | The start time of the validity period for the storage plan. |
| ProtocolType | String | NFS | The type of the protocol. Valid values: NFS: the Network File System (NFS) protocol. SMB: the Server Message Block (SMB) protocol. |
| QuotaSize | Long | 100 | The capacity of the file system. |
| RegionId | String | cn-hangzhou | The ID of the region. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Pending | The status of the file system. Valid values: Pending: The file system is being created or modified. Running: The file system is available. Before you create a mount target for the file system, make sure that the file system is in the Running state. Stopped: The file system is unavailable. Extending: The file system is being scaled up. Stopping: The file system is being stopped. Deleting: The file system is being deleted. |
| StorageType | String | Performance | The type of the storage. Valid values: Performance: NAS Performance file systems. Capacity: NAS Capacity file systems. |
| SupportedFeat ures | List | Lifecycle | The features that are supported by the file system. Valid values: Lifecycle: the lifecycle management feature. Quota: the quota management feature. |
| VolumeSize | Long | 1000 | The capacity of the General-purpose NAS file system. Valid values: Valid values for NAS Capacity file systems: 0 to 10 PB. Valid values for NAS Performance file systems: 0 to 1 PB. |
| ZoneId | String | cn-hangzhou-b | The ID of the zone where the file system resides. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DescribeFileSystems &<Common request parameters> Sample success responses XML format <FileSystems> <Status>Pending</Status> <StorageType>Performance</StorageType> <Description>This can be the description of the created file system. </Description> <ZoneId>cn-hangzhou-b</ZoneId> <MeteredIASize>1000</MeteredIASize> <CreateTime>2017-05-27T15:43:06CST</CreateTime> <QuotaSize>100</QuotaSize> <MeteredSize>1611661312</MeteredSize> <EncryptType>1</EncryptType> <ChargeType>PayAsYouGo</ChargeType> <ProtocolType>NFS</ProtocolType> <Bandwidth>150</Bandwidth> <FileSystemType>all</FileSystemType> <ExpiredTime>1572174830000</ExpiredTime> <FileSystemId>109c04****</FileSystemId> <RegionId>cn-hangzhou</RegionId> <VolumeSize>1000</VolumeSize> </FileSystems> <FileSystems> <MountTargets> <Status>active</Status> <VswId>vsw-bp1omfzsszekkvaxn****</VswId> <VpcId>vpc-bp1sevsgtqvk5gxbl****</VpcId> <MountTargetDomain>109c042666-w****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain> <NetworkType>vpc</NetworkType> <AccessGroupName>test-001</AccessGroupName> </MountTargets> <Packages> <StartTime>2019-12-05T01:40:56Z</StartTime> <PackageId>naspackage-0be9c4b624-37****</PackageId> <Size>107374182400</Size> <ExpiredTime>2020-01-05T16:00:00Z</ExpiredTime> <PackageType>hybrid</PackageType> </Packages> </FileSystems> <FileSystems> <SupportedFeatures>Lifecycle</SupportedFeatures> </FileSystems> <FileSystems> <Ldap> <SearchBase>dc=example</SearchBase> <URI>ldap://ldap.example.example</URI> <BindDN>cn=alibaba,dc=com</BindDN> </Ldap> </FileSystems> <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>035B3A3A-E514-4B41-B906-5D906CFB****</RequestId> <PageNumber>1</PageNumber> JSON format { { "FileSystems": [ { "Status": "Pending", "StorageType": "Performance", "Description": "This can be the description of the created file system.", "ZoneId": "cn-hangzhou-b", "MeteredIASize": 1000, "CreateTime": "2017-05-27T15:43:06CST", "QuotaSize": 100, "MeteredSize": 1611661312, "EncryptType": 1, "ChargeType": "PayAsYouGo", "ProtocolType": "NFS", "Bandwidth": 150, "FileSystemType": "all", "ExpiredTime": 1572174830000, "FileSystemId": "109c04****", "RegionId": "cn-hangzhou", "VolumeSize": 1000 }, { "MountTargets": { "Status": "active", "VswId": "vsw-bp1omfzsszekkvaxn****", "VpcId": "vpc-bp1sevsgtqvk5gxbl****", "MountTargetDomain": "109c042666-w****.cn-hangzhou.nas.aliyuncs.com", "NetworkType": "vpc", "AccessGroupName": "test-001" }, "Packages": { "StartTime": "2019-12-05T01:40:56Z", "PackageId": "naspackage-0be9c4b624-37****", "Size": 107374182400, "ExpiredTime": "2020-01-05T16:00:00Z", "PackageType": "hybrid" } }, { "SupportedFeatures": "Lifecycle" }, { "Ldap": { "SearchBase": "dc=example", "URI": "ldap://ldap.example.example", "BindDN": "cn=alibaba,dc=com" } } ], "TotalCount": 1, "PageSize": 1, "RequestId": "035B3A3A-E514-4B41-B906-5D906CFB****", "PageNumber": 1 }

### 4.5 Mount point

#### 4.5.1 CreateMountTarget

Creates a mount target.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateMountTarg et | The operation that you want to perform. Set the value to CreateMountTarget. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPC) and DEFAULT CLASSIC GROUP NAME (the _ _ _ default permission group for the classic network). |
| FileSystemId | String | Yes | 174494**** | The ID of the file system. |
| NetworkType | String | Yes | VPC | The network type of the mount target. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
| VpcId | String | No | vpc- 2zesj9afh3y518k 9o**** | The ID of the VPC. This parameter is valid and required if the mount target resides in a VPC. |
| VSwitchId | String | No | vsw- 2zevmwkwyztjuo ffg**** | The ID of the vSwitch. This parameter is valid and required if the mount target resides in a VPC. |
| SecurityGroupId | String | No | sg- bp1fg655nh68xy z9**** | The ID of the security group. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargetD omain | String | 174494b666- x****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| RequestId | String | 70EACC9C-D07A- 4A34-ADA4- 77506C42**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=CreateMountTarget &AccessGroupName=classic-test &FileSystemId=174494**** &NetworkType=VPC &<Common request parameters> Sample success responses XML format <RequestId>70EACC9C-D07A-4A34-ADA4-77506C42****</RequestId> <MountTargetDomain>174494b666-x****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain> JSON format { "RequestId": "70EACC9C-D07A-4A34-ADA4-77506C42****", "MountTargetDomain": "174494b666-x****.cn-hangzhou.nas.aliyuncs.com" }

#### 4.5.2 DeleteMountTarget

Deletes a mount target. After you delete a mount target, the mount target cannot be restored. Proceed with caution.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteMountTarg et | The operation that you want to perform. Set the value to DeleteMountTarget. |
| FileSystemId | String | Yes | 174494**** | The ID of the file system. |
| MountTargetDom ain | String | Yes | 174494b666- x****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5BC5CB97-9F28- 42FE-84A4- 0CD0DF42**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DeleteMountTarget &FileSystemId=174494**** &MountTargetDomain=174494b666-x****.cn-hangzhou.nas.aliyuncs.com &<Common request parameters> Sample success responses XML format <RequestId>5BC5CB97-9F28-42FE-84A4-0CD0DF42****</RequestId> JSON format { "RequestId": "5BC5CB97-9F28-42FE-84A4-0CD0DF42****" }

#### 4.5.3 DescribeMountTargets

Queries the information of mount targets.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeMountTa rgets | The operation that you want to perform. Set the value to DescribeMountTargets. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| MountTargetDom ain | String | No | 1ca404a666- x****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| MountTargets | Array of MountTarget |   | The list of mount targets. |
| MountTarget |   |   |   |
| AccessGroup | String | DEFAULT VPC GRO _ _ UP NAME _ | The name of the permission group that is attached to the mount target. |
| MountTargetD omain | String | 1ca404a666- w****.cn- hangzhou.nas.aliyu ncs.com | The domain name of the mount target. |
| NetworkType | String | Vpc | The network type of the mount target. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| Status | String | Active | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. Note A file system can be mounted only if the file system is in the Active state. |
| VpcId | String | vpc- 2zesj9afh3y518k9o* *** | The ID of the virtual private cloud (VPC). |
| VswId | String | vsw- 2zevmwkwyztjuoffg **** | The ID of the vSwitch. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 3BAB90FD-B4A0- 48DA-9F09- 2B963510A0EF | The ID of the request. |
| TotalCount | Integer | 1 | The total number of mount targets. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DescribeMountTargets &FileSystemId=1ca404**** &<Common request parameters> Sample success responses XML format <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>3BAB90FD-B4A0-48DA-9F09-2B963510A0EF</RequestId> <PageNumber>1</PageNumber> <MountTargets> <Status>Active</Status> <VswId>vsw-2zevmwkwyztjuoffg****</VswId> <VpcId>vpc-2zesj9afh3y518k9o****</VpcId> <MountTargetDomain>1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com</MountTargetDomain> <AccessGroup>DEFAULT_VPC_GROUP_NAME</AccessGroup> <NetworkType>Vpc</NetworkType> </MountTargets> JSON format { "TotalCount": 1, "PageSize": 1, "RequestId": "3BAB90FD-B4A0-48DA-9F09-2B963510A0EF", "PageNumber": 1, "MountTargets": { "Status": "Active", "VswId": "vsw-2zevmwkwyztjuoffg****", "VpcId": "vpc-2zesj9afh3y518k9o****", "MountTargetDomain": "1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com", "AccessGroup": "DEFAULT_VPC_GROUP_NAME", "NetworkType": "Vpc" } }

#### 4.5.4 ModifyMountTarget

Modifies a mount target.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyMountTar get | The operation that you want to perform. Set the value to ModifyMountTarget. |
| FileSystemId | String | Yes | 1ca404**** | The ID of the file system. |
| MountTargetDom ain | String | Yes | 1ca404a666- w****.cn- hangzhou.nas.al iyuncs.com | The domain name of the mount target. |

| Developer Guide·API | Reference |   |   | Apsara File Storage NA |
|---|---|---|---|---|

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| AccessGroupNam e | String | No | classic-test | The name of the permission group that is attached to the mount target. |
| Status | String | No | Inactive | The status of the mount target. Valid values: Active: The mount target is available. Inactive: The mount target is unavailable. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | FF387D95-34C4- 4879-B65A- 99D1FA1**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=ModifyMountTarget &FileSystemId=1ca404**** &MountTargetDomain=1ca404a666-w****.cn-hangzhou.nas.aliyuncs.com &<Common request parameters> Sample success responses XML format <RequestId>FF387D95-34C4-4879-B65A-99D1FA1****</RequestId> JSON format { "RequestId": "FF387D95-34C4-4879-B65A-99D1FA1****" }

### 4.6 Permission group

#### 4.6.1 CreateAccessGroup

Creates a permission group.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessGro up | The operation that you want to perform. Set the value to CreateAccessGroup. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter and can contain letters, digits, underscores ( ), and hyphens (-). _ The name of the permission group must be different from the name of the default permission groups. Default permission groups: DEFAULT VPC GROUP NAME (the _ _ _ default permission group for VPC) and DEFAULT CLASSIC GROUP NAME (the _ _ _ default permission group for the classic network). |
| AccessGroupTyp e | String | Yes | Classic | The type of the permission group. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
| Description | String | No | classictestaccess group | The description of the permission group. Limits: By default, the description of a permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length. The description must start with a letter and cannot start with http:// or https://. The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessGroupN ame | String | classic-test | The name of the permission group. |
| RequestId | String | 55C5FFD6-BF99- 41BD-9C66- FFF39189**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=CreateAccessGroup &AccessGroupName=classic-test &AccessGroupType=Classic &<Common request parameters> Sample success responses XML format <RequestId>55C5FFD6-BF99-41BD-9C66-FFF39189****</RequestId> <AccessGroupName>classic-test</AccessGroupName> JSON format { "RequestId": "55C5FFD6-BF99-41BD-9C66-FFF39189****", "AccessGroupName": "classic-test" }

#### 4.6.2 DeleteAccessGroup

Deletes a permission group. Default permission groups include DEFAULT_VPC_GROUP_NAME and DEFAULT_CLASSIC_GROUP_NAME. You cannot delete the default permission groups.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessGro up | The operation that you want to perform. Set the value to DeleteAccessGroup. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 9E15E394-38A6- 457A-A62A- D9797C9A**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DeleteAccessGroup &AccessGroupName=classic-test &<Common request parameters> Sample success responses XML format <RequestId>9E15E394-38A6-457A-A62A-D9797C9A****</RequestId> JSON format { "RequestId": "9E15E394-38A6-457A-A62A-D9797C9A****" }

#### 4.6.3 ModifyAccessGroup

Modifies a permission group.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccessGro up | The operation that you want to perform. Set the value to ModifyAccessGroup. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. Limits: The name must be 3 to 64 characters in length. The name must start with a letter. The name can contain letters, digits, underscores ( ), and hyphens (-). _ |
| Description | String | No | classic-test | The description of the permission group. Limits: By default, the description of the permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length. The description must start with a letter and cannot start with http:// or https:// . The description can contain digits, colons (:), underscores ( ), and _ hyphens (-). |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | ED2AE737-9D50- 4CA4-B0DA- 31BD610C**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=ModifyAccessGroup &AccessGroupName=classic-test &<Common request parameters> Sample success responses XML format <RequestId>ED2AE737-9D50-4CA4-B0DA-31BD610C****</RequestId> JSON format { "RequestId": "ED2AE737-9D50-4CA4-B0DA-31BD610C****" }

#### 4.6.4 DescribeAccessGroups

Queries the information of permission groups.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessG roups | The operation that you want to perform. Set the value to DescribeAccessGroups. |
| AccessGroupNam e | String | No | classic-test | The name of the permission group. |
| PageSize | Integer | No | 2 | The number of entries to return per page. Valid values: 1 to 100. Default value: 10. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |
| UseUTCDateTime | Boolean | No | true | Specifies whether the time to return is in UTC. Valid values: true: the default value. The time is returned in the UTC format. false: The time is not returned in the UTC format. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessGroups | Array of AccessGroup |   | The list of permission groups. |
| AccessGroup |   |   |   |
| AccessGroupN ame | String | classic-test | The name of the permission group. |
| AccessGroupTy pe | String | Classic | The type of the permission group. Valid values: Vpc: the virtual private cloud (VPC) network. Classic: the classic network. |
| Description | String | This is a classic test access group~ | The description of the permission group. |
| MountTargetCo unt | Integer | 0 | The number of mount targets to which the permission group is attached. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| RuleCount | Integer | 0 | The total number of rules in the permission group. |
| PageNumber | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| RequestId | String | 2514F97E-FFF0- 4A1F-BF04- 729CEAC64B6F | The ID of the request. |
| ResourceOwne rId | String | 258456 | The ID of the resource. |
| TotalCount | Integer | 2 | The total number of permission groups. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DescribeAccessGroups &<Common request parameters> Sample success responses XML format <AccessGroups> <RuleCount>0</RuleCount> <AccessGroupType>Classic</AccessGroupType> <Description>This is a classic test access group~</Description> <MountTargetCount>0</MountTargetCount> <AccessGroupName>classic-test</AccessGroupName> </AccessGroups> <TotalCount>2</TotalCount> <PageSize>2</PageSize> <RequestId>2514F97E-FFF0-4A1F-BF04-729CEAC64B6F</RequestId> <PageNumber>1</PageNumber> <ResourceOwnerId>258456</ResourceOwnerId> JSON format { "AccessGroups": { "RuleCount": 0, "AccessGroupType": "Classic", "Description": "This is a classic test access group~", "MountTargetCount": 0, "AccessGroupName": "classic-test" }, "TotalCount": 2, "PageSize": 2, "RequestId": "2514F97E-FFF0-4A1F-BF04-729CEAC64B6F", "PageNumber": 1, "ResourceOwnerId": 258456 }

#### 4.6.5 CreateAccessRule

Creates a rule for a permission group.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateAccessRul e | The operation that you want to perform. Set the value to CreateAccessRule. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. |
| SourceCidrIp | String | Yes | 10.0.*. */** | The IP address or CIDR block of the authorized object. It must be an IP address or CIDR block. Note If the permission group resides in the classic network, only IP addresses are supported. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| RWAccessType | String | No | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates read and write permissions. RDONLY: the read-only permissions. |
| UserAccessType | String | No | no squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash: allows access from root _ users to the file system. root squash: grants root users the _ least permissions as the nobody user. all squash: grants all users the _ least permissions as the nobody user. The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system. |
| Priority | Integer | No | 1 | The priority of the rule. The rule with the highest priority takes effect if multiple rules are attached to the authorized object. Valid values: 1 to 100. The value 1 indicates the highest priority. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessRuleId | String | 1 | The ID of the rule. |
| RequestId | String | A323836B-5BC6- 45A6-8048- 60675C23**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=CreateAccessRule &AccessGroupName=classic-test &SourceCidrIp=10.0. *. */** &<Common request parameters> Sample success responses XML format <RequestId>A323836B-5BC6-45A6-8048-60675C23****</RequestId> <AccessRuleId>1</AccessRuleId> JSON format { "RequestId": "A323836B-5BC6-45A6-8048-60675C23****", "AccessRuleId": 1 }

#### 4.6.6 DeleteAccessRule

Deletes a rule from a permission group.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteAccessRul e | The operation that you want to perform. Set the value to DeleteAccessRule. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. |

|   | Apsara File Storage N | AS |   |   | Developer Guide·API Referenc | e |
|---|---|---|---|---|---|---|

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| AccessRuleId | String | Yes | 1 | The ID of the rule. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 5B4511A7-C99E- 4071-AA8C- 32E2529D**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DeleteAccessRule &AccessGroupName=classic-test &AccessRuleId=1 &<Common request parameters> Sample success responses XML format <RequestId>5B4511A7-C99E-4071-AA8C-32E2529D****</RequestId> JSON format { "RequestId": "5B4511A7-C99E-4071-AA8C-32E2529D****" }

#### 4.6.7 ModifyAccessRule

Modifies a rule in a permission group.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifyAccessRul e | The operation that you want to perform. Set the value to ModifyAccessRule. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. |
| AccessRuleId | String | Yes | 1 | The ID of the rule. |
| SourceCidrIp | String | No | 192.1**. *. * | The IP address or CIDR block of the authorized object. It must be an IP address or CIDR block. Note If the permission group resides in the classic network, only IP addresses are supported. |
| RWAccessType | String | No | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates the read and write permissions. RDONLY: the read-only permissions. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| UserAccessType | String | No | all squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash: allows access from root _ users to the file system. root squash: grants root users the _ least permissions as the nobody user. all squash: grants all users the _ least permissions as the nobody user. The nobody user has the least permissions in Linux and can access only the public content of the file system. This ensures the security of the file system. |
| Priority | Integer | No | 1 | The priority of the rule in the permission group. Valid values: 1 to 100. Default value: 1, which indicates the highest priority. |
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6299428C-3861- 435D-AE54- 9B330A00**** | The ID of the request. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=ModifyAccessRule &AccessGroupName=classic-test &AccessRuleId=1 &<Common request parameters> Sample success responses XML format <RequestId>6299428C-3861-435D-AE54-9B330A00****</RequestId> JSON format { "RequestId": "6299428C-3861-435D-AE54-9B330A00****" }

#### 4.6.8 DescribeAccessRules

Queries the information about rules.

**Request parameters**

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAccessR ules | The operation that you want to perform. Set the value to DescribeAccessRules. |
| AccessGroupNam e | String | Yes | classic-test | The name of the permission group. |
| AccessRuleId | String | No | 1 | The ID of the rule. |
| PageSize | Integer | No | 1 | The number of entries to return on each page. Valid values: 1 to 100. Default value: 10. |
| PageNumber | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

| Parameter | Type | Require d | Example | Description |
|---|---|---|---|---|
| FileSystemType | String | No | standard | The type of the file system. Default value: standard, which indicates General-purpose NAS file systems. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessRules | Array of AccessRule |   | The list of rules. |
| AccessRule |   |   |   |
| AccessRuleId | String | 1 | The ID of the rule. |
| Priority | Integer | 1 | The priority of the rule. If multiple rules are attached to the authorized object, the rule with the highest priority takes effect. Valid values: 1 to 100. The value 1 indicates the highest priority. |
| RWAccess | String | RDWR | Grants access permissions on the file system to the authorized object. Valid values: RDWR: the default value, which indicates the read and write permissions. RDONLY: the read-only permissions. |
| SourceCidrIp | String | 10.0.*. */** | The IP address or CIDR block of the authorized object. |
| UserAccess | String | no squash _ | The access permissions for different types of users in the authorized object. Valid values: no squash, root squash, and all squash. _ _ _ Default value: no squash. _ |
| PageNumber | Integer | 1 | The page number of the returned page. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageSize | Integer | 1 | The number of entries returned per page. |
| RequestId | String | 86D89E82-4297- 4343-8E1E- A2495B35CC70 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of rules. |

**Examples**

Sample requests http(s)://[Endpoint]/? Action=DescribeAccessRules &AccessGroupName=classic-test &<Common request parameters> Sample success responses XML format <TotalCount>1</TotalCount> <PageSize>1</PageSize> <RequestId>86D89E82-4297-4343-8E1E-A2495B35CC70</RequestId> <PageNumber>1</PageNumber> <AccessRules> <RWAccess>RDWR</RWAccess> <AccessRuleId>1</AccessRuleId> <UserAccess>no_squash</UserAccess> <Priority>1</Priority> <SourceCidrIp>10.0. *. */**</SourceCidrIp> </AccessRules> JSON format { "TotalCount": 1, "PageSize": 1, "RequestId": "86D89E82-4297-4343-8E1E-A2495B35CC70", "PageNumber": 1, "AccessRules": { "RWAccess": "RDWR", "AccessRuleId": 1, "UserAccess": "no_squash", "Priority": 1, "SourceCidrIp": "10.0. *. */**" } }

### 4.7 Appendix: Error codes

An error code consists of four components, as listed in Error codes. Error codes

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
| 503 | VpcSubRam.CheckFaile d | The Vpc sub user ram check has failed due to some internal error. | Please try again later. |
| 400 | MissingParameter.calle rUid | Request parameter missing: callerUid is not specified. | Add the callerUid request parameter. |
| 400 | MissingParameter.Regi onId | Request parameter missing: RegionId of the domain name is not specified. | Add the RegionId field to the domain name. |
| 400 | MissingParameter.VSwi tchId | Request parameter missing: VSwitchId is not specified. | Add the VSwitchId request parameter. |

| Developer Guide·API Refer | ence |   | Apsara File Storage NA |
|---|---|---|---|

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 400 | MissingParameter.VpcI d | Request parameter missing: VpcId is not specified. | Add the VpcId request parameter. |
| 400 | InvalidParameter.Stora geType | Invalid request parameter: StorageType is invalid. | Set StorageType to Performance or Capacity. |
| 400 | InvalidParameter.Proto calType | Invalid request parameter: ProtocalType is invalid. | Set ProtocalType to NFS. |
| 400 | InvalidParameter.Descr iption | Invalid request parameter: Description contains invalid characters. | Set Description to a string that contains English letters and special characters such as at signs (@), number signs (#), dollar signs ($), underscores ( ), _ plus signs (+), and hyphens (-). |
| 404 | InvalidFileSystem.NotF ound | The specified NAS instance does not exist. | The specified NAS instance does not exist or has been deleted. |
| 403 | InvalidFileSystem.Alrea dyExisted | The specified NAS instance already exists. | Call DescribeFileSystems and specify the NAS instance ID to view the instance information. |
| 404 | InvalidMountTarget.Not Found | The specified mount point does not exist. | The specified mount point does not exist or has been deleted. |
| 404 | InvalidAccessGroup.Not Found | The specified permission group does not exist. | The specified permission group does not exist or has been deleted. |
| 403 | InvalidAccessGroup.Alr eadyExisted | The specified permission group already exists. | Call DescribeMountTargets and specify the permission group to view its information. |
| 403 | InvalidAccessGroup.Alr eadyAttached | The specified permission group has been bound to a mount point. | Unbind the permission group from the mount point before deleting the permission group. |

| Apsara File Storage NAS |   | Deve | loper Guide·API Referenc |
|---|---|---|---|

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 404 | InvalidAccessRule.NotF ound | The specified permission rule does not exist. | The specified permission rule does not exist or has been deleted. |
| 404 | InvalidLocatin.NotFoun d | The specified location does not exist. | The requested location does not exist or is not providing services. |
| 404 | InvalidRegionId.NotFou nd | The specified region does not exist. | The requested region does not exist or is not providing services. |
| 404 | InvalidAZone.NotFound | The specified zone does not exist. | The requested zone does not exist or is not providing services. |
| 404 | InvalidVpc.NotFound | The specified VPC does not exist. | Create a VPC first. |
| 404 | InvalidVip.NotFound | The specified VIP does not exist. | Make sure that there are available IP addresses in your VPC. |
| 404 | InvalidLBid.NotFound | The specified LBid does not exist. | Please try again later. |
| 404 | InvalidVpcTunnelId.Not Found | The specified VPC tunnelId does not exist. | Check the VPC information first. |
| 404 | InvalidVpc.CreationFail ed | The specified vpc instance creation failed. | Make sure that the VPC information is correct and there is an available IP address for the VPC, and then try again. |
| 403 | OperationDenied.Defau ltAccessGroupCannotDe lete | Operation not allowed: The default permission group cannot be deleted. | You can only edit custom permission groups. |
| 403 | OperationDenied.Defau ltAccessGroupCannotM odify | Operation not allowed: The default permission group cannot be modified. | You can only edit custom permission groups. |
| 403 | OperationDenied.Netw orkTypeNotMatched | Operation not allowed: The mount point network type does not match the AccessGroupType. | Make sure that the NetworkType of the mount point and the AccessGroupType of the permission group are consistent. |

| HTTP status code | Code | Message | Advice |
|---|---|---|---|
| 403 | OperationDenied.Moun tTargetNotEmpty | Operation not allowed: The specified NAS instance already has a mount point. Delete the existing mount point first. | Delete the existing mount points first. |
| 403 | OperationDenied.FileSy stemCountsExceeded | The number of NAS instances has already reached the upper limit (a user can create a maximum of 10 NAS instances). | To raise the limit, contact technical support. |
| 403 | OperationDenied.Moun tTargetCountsExceeded | The number of mount points has already reached the upper limit (a maximum of two mount points can be created for each NAS instance). | To raise the limit, contact technical support. |
| 403 | OperationDenied.Acces sGroupCountsExceeded | The number of permission groups has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | OperationDenied.Acces sRuleCountsExceeded | The number of permission rules has already reached the upper limit. | To raise the limit, contact technical support. |
| 403 | Forbidden.InvalidUserT ype | No permission: The user type is invalid. | Sorry, this API does not support your account type. |
| 403 | Forbbiden.Ram | User not authorized to operate on the specified resource, or this API doesn’t support RAM. | Access RAM to grant required NAS permissions. |
| 403 | NotQualified | No public beta qualification yet | Please initiate an application for a trial of the related features. If your application fails to be approved, contact the technical support. |

**Error response examples**

XML format <? xml version="1.0" encoding="UTF-8"? > <Error> <RequestId>B71B4C68-6C6B-4D4B-AD70-8951BD7D188E</RequestId> <HostId>nas.regionid.example.com</HostId> <Code>InvalidFileSystem.NotFound</Code> <Message>The specified NAS instance does not exist.</Message> </Error> JSON format { "RequestId": "B71B4C68-6C6B-4D4B-AD70-8951BD7D188E", "HostId": " nas.regionid.example.com ", "Code": "InvalidFileSystem.NotFound", "Message": "The specified NAS instance does not exist." }

## 5 Appendixes

### 5.1 Use the ASAPI gateway to call API operations

**operations**

You can use the Apsara Stack API (ASAPI) gateway to call API operations of most Apsara Stack services. This topic describes how to call API operations by using the ASAPI gateway and provides links to references.

**Procedure**

1. Obtain the ASAPI SDK.
Before you use ASAPI to call an API operation, you must obtain the ASAPI SDK. For more information, see Obtain the ASAPI SDK.
2. Obtain the endpoint of ASAPI. For more information, see Obtain the endpoint of ASAPI.
3. Obtain an AccessKey pair.
Obtain the AccessKey pair that is required for calling an API operation.

> **Note:** We recommend that you use the AccessKey pair of a personal account to call the API operations of the Apsara Uni-manager Management Console and cloud services.

4. Obtain the region ID.
Obtain the region ID that is required for calling an API operation.
5. Obtain the organization ID and resource set ID.
You can call the GetOrganizationList operation to obtain the organization ID. For more information, see GetOrganizationList in Apsara Uni-manager Management Console Developer Guide. You can call the ListResourceGroup operation to obtain the resource set ID. For more information, see ListResourceGroup in Apsara Uni-manager Management Console Developer G uide.

> **Note:** When you call an API operation, you can specify the organization ID and resource set ID by using the <x-acs-organizationid> and <x-acs-resourcegroupid> parameters. This allows you to query specified resources.
> If you do not set the <x-acs-organizationid> parameter, the organization to which the current user belongs is used by default.
> If you do not set the <x-acs-resourcegroupid> parameter, it is empty by default. If you specify a resource set ID, you must also specify an organization ID.

6. Refer to the API reference.
Obtain the developer guide of the Apsara Stack service that you want to use. You can learn the features of API operations and how to call the API operations. For more information, see Use developer guides.
7. Use ASAPI SDK to call API operations.
After you complete the preceding steps, you can use the ASAPI SDK to call API operations. For more information about how to use SDKs for different languages, see the relevant topics. The following example shows how to call the DescribeInstances operation of Elastic Compute Service (ECS) by using SDK for Java: public static void main(String[] args) { ASClient client = new ASClient(); // Specify the caller. The caller is recorded in logs. client.setSdkSource("autoTest"); // Set request parameters. Map<String, Object> parameters = new HashMap<String, Object>();; parameters.put("Product", "Ecs");// Specify the POP code, which is the same as the POP code in the corr esponding API directory. parameters.put("Action", "DescribeInstances"); // Specify the name of the API operation. Use the same l etter case as the corresponding API directory. parameters.put("Version", "2014-05-26"); // Specify the API version. // Specify the region ID that you obtained. parameters.put("RegionId", "xxx"); // Specify your AccessKey ID and AccessKey secret. parameters.put("AccessKeyId", "xxx"); parameters.put("AccessKeySecret", "xxx"); // Add the parameters based on the API reference. Take note that the parameters are case-sensitive. parameters.put("PageNumber",1); parameters.put("PageSize",10); Map<String,String> headers=new HashMap<>(); // Specify the organization ID in the Apsara Uni-manager Management Console. headers.put("x-acs-organizationid","3"); // Specify the resource set ID in the Apsara Uni-manager Management Console. //headers.put("x-acs-resourcegroupid", "<your-resourcegroupid>"); // Specify the endpoint of ASAPI. String endpoint="https://public.asapi.xxx.xxx/asapi/v3"; // Initiate the request. String result = client.doPost(endpoint,headers, parameters); // Display the results. System.out.println(JSONObject.toJSONString(JSONObject.parseObject(result), SerializerFeature.PrettyFo rmat)); }

### 5.2 Use the ASAPI gateway to make API calls

**calls**

#### 5.2.1 Obtain an endpoint of ASAPI

This topic describes three methods that you can use to obtain an endpoint of Apsara Stack API (ASAPI) and how to verify the endpoint.

**Methods**

**Method 1: Use Registration Vars of Services to obtain an endpoint**

1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. Choose **Platforms** > **Apsara Infrastructure Management Framework**.
2. In the left-side navigation pane, click **Reports**.
3. On the **All Reports** page, search for Registration Vars of Services and click the report name.
4. On the **Registration Vars of Services** page, click the
icon next to **Service** and search for asapi .
5. Find the asapi service, right-click in the **Service Registration** column, and then select **Show More**
from the shortcut menu. In the **Details** dialog box, obtain the value of **asapi.public.endpoint**.
6. Generate an endpoint of ASAPI based on the following format:
https://<asapi.public.endpoint>/asapi/v3

**Method 2: Use cluster resources to generate an endpoint**

1. Log on to the Apsara Infrastructure Management console.
i. Log on to the Apsara Uni-manager Operations Console. ii. In the top navigation bar, click **Products**. iii. Choose **Platforms** > **Apsara Infrastructure Management Framework**.
2. Go to the Clusters page.
i. In the left-side navigation pane, choose **Operations** > **Cluster Operations**. ii. In the **Cluster** search box, enter ascm . iii. Click **Operations** in the **Actions** column.
3. Obtain the value of the domain parameter.
i. Click the **Cluster Resources** tab. ii. In the **Name** field, search for asapi_dns_public . iii. Click **Details** in the **Application Parameter** column. In the **Application Parameter** message, obtain the value of the **domain** parameter.
4. Generate an endpoint of ASAPI based on the following format:
https://<domain>/asapi/v3

**Method 3: Concatenate strings to generate an endpoint**

You can also concatenate strings to generate an endpoint based on the following format: https://public.asapi.<region>.<internet-domain>/asapi/v3

**Note**

1. Replace <region> with the actual region ID.
2. Replace <internet-domain> with the root domain of your Apsara Stack service. To obtain
the root domain, contact Apsara Stack O&M personnel. Take note of this point: Use the internet-domain parameter instead of the intranet-domain parameter. If the **region** value is cn-****-****-d01 and the **internet-domain** value is inter.****.****.com , the following endpoint is used: https://public.asapi.cn-****-****-d01.inter.****.****.com/asapi/v3

**Verify the endpoint**

Enter the following code. If you cannot access the endpoint, the endpoint is unavailable. You can use the historical endpoint. curl https://public.asapi.${global:region}.${global:internet-domain}/api/version -k

> **Note:** ${global:region} and ${global:internet-domain} are variables. You must replace them with the actual values that you obtained.

Available endpoint example: Unavailable endpoint example:

**Historical endpoint**

Only the HTTP protocol is supported. The historical endpoint is suffixed with intranet-domain and in the following format: http://server.asapi.${global:region}.${global:intranet-domain}/asapi/v3

> **Note:** ${global:region} and ${global:intranet-domain} are variables. You must replace them with the actual values that you obtained.

**Procedure**

To obtain the actual values of the variables ${global:region}, ${global:internet-domain}, and ${global:intranet-domain}, perform the following operations:
1. In the address bar, enter the region-id.aso.intranet-domain-id.com URL and press the Enter
key.

> **Note:** You can select a language from the drop-down list in the upper-right corner of the page.

2. Enter your username and password.

> **Note:** Obtain the username and password used to log on to the Apsara Uni-manager Operations Console from the deployment personnel or an administrator.

When you log on to the Apsara Uni-manager Operations Console for the first time, you must change the password of your username. To enhance security, your password must meet the following requirements: The password contains uppercase and lowercase letters. The password contains digits. The password contains special characters such as exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%). The password is 10 to 20 characters in length.
3. Click **Log On** to log on to the **Apsara Uni-manager Operations Console**.
4. In the top navigation bar, choose **Products** > **Platforms** > **Apsara Infrastructure Management**
**Framework** to go to Apsara Infrastructure Management.
5. In the left-side navigation pane, choose **Operations** > **Cluster Operations**.
6. On the **Clusters** page, enter **ascm-A** in the Cluster search box to find the cluster. Click the cluster
name.
7. On the **Cluster Dashboard** page, click **Operations Menu** > **Configuration Files**.
8. In the **File List** window on the left side of the **Cluster Configuration** page, click **kv.conf**, click the
file content in the right window, and then press Ctrl + F. Search for region, internet-domain, and intranet-domain.

| ained region value, | ${global:internet-domain} |   |
|---|---|---|
| ${global:intranet-domain} |   |   |
|   |   | with the obtained in |

domain value.

> **Note:** ${global:} is not included in the endpoint of ASAPI that you can use.

#### 5.2.2 Obtain Apsara Stack SDKs

Apsara Stack API (ASAPI) is a unified portal provided by Apsara Stack. You can use ASAPI to connect to all Apsara Stack services. Apsara Stack provides SDKs for API calls.

**Public environment**

If you are using the public environment, you can go to the Apsara Stack documentation page and download the Apsara Stack SDKs in the **Other Resources** section at the lower part of the page.

**Private environment**

If you are using the private environment, you must switch to the public environment and then go to the Apsara Stack documentation page. At the lower part of the page, download the Apsara Stack SDKs in the **Other Resources** section. Apsara Stack SDK for Java

| greopId | artifactId | Version |
|---|---|---|
| com.alibaba | alicrypto-java-aliyun | 1.0.4 |
| com.alibaba | fastjson | 1.2.68 |
| org.bouncycastle | bcprov-jdk15to18 | 1.66 |

| Apsara File Storage NAS |   | Developer Guide·Appendixe |
|---|---|---|
| greopId | artifactId | Version |
| org.bouncycastle | bcpkix-jdk15on | 1.65 |
| org.bouncycastle | bcprov-jdk15on | 1.65 |
| com.aliyun | gmsse | 1.1.0 |
| org.apache.commons | commons-lang3 | 3.0 |
| commons-codec | commons-codec | 1.11 |
| commons-logging | commons-logging | 1.2 |
| org.apache.httpcomponents | httpcore | 4.4.11 |
| org.apache.httpcomponents | httpclient | 4.5.7 |

Apsara Stack SDK for Python

| Package | Version |
|---|---|
| aliyun-python-sdk-core | 2.13.35 |
| certifi | 2021.5.30 |
| cffi | 1.14.6 |
| charset-normalizer | 2.0.4 |
| cryptography | 3.4.8 |
| idna | 3.2 |
| jmespath | 0.10.0 |
| pycparser | 2.20 |
| requests | 2.26.0 |
| urllib3 | 1.26.6 |

> **Note:** You can use the version for each package listed in the preceding table or a later version.

### 5.3 STS overview

#### 5.3.1 What is STS?

Security Token Service (STS) allows you to manage temporary credentials to your Apsara Stack resources. Resource Access Management (RAM) provides RAM users and RAM roles. A RAM role does not have permanent identity credentials. A RAM role can be assumed to access Apsara Stack resources by using an issued STS token. When the STS token is issued, you can specify a validity period and access permissions for the STS token.

**Use a RAM user to obtain an STS token**

An authorized RAM user can use an AccessKey pair to call the AssumeRole operation. This way, the RAM user can obtain an STS token of a RAM role and can use the STS token to access Apsara Stack resources.

**Benefits**

STS tokens help reduce the risks of AccessKey pair leaks. An AccessKey pair is a long-term credential for a RAM user. STS tokens are temporary credentials. You can specify the validity period for STS tokens. After STS tokens expire, they become invalid. Therefore, you do not need to rotate the STS tokens on a regular basis. You can attach custom policies to STS tokens for flexible and fine-grained authorization.

#### 5.3.2 AssumeRole

Obtains a Security Token Service (STS) token that is used by a RAM user to assume a RAM role. In this example, an Apsara Stack tenant account is used as the trusted entity of the RAM role.

**Request parameters**

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | AssumeRole | The operation that you want to perform. Set the value to AssumeRole. |
| RoleArn | String | Yes | acs:ram::1234567 89012****:role/ad minrole | The Apsara Stack Resource Name (ARN) of the RAM role. The trusted entity of the RAM role is an Apsara Stack tenant account. |

| Parameter | Type | Requi red | Example | Description |
|---|---|---|---|---|
| RoleSessionName | String | Yes | alice | The name of the role session. Set this parameter based on your business requirements. In most cases, you can set this parameter to the identity of the user who calls the operation. For example, specify a username. In ActionTrail logs, you can distinguish the users who assume the same RAM role to perform operations based on the value of the RoleSessionName parameter. This way, you can perform user-specific auditing. The name must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| Policy | String | No | {"Statement": [{"Action": ["*"],"Effect": "Allow","Resource ": ["*"]}],"Version":"1 "} | The policy that specifies the permissions of the STS token. You can use this parameter to grant the STS token fewer permissions than the permissions granted to the RAM role. The policy must be 1 to 1,024 characters in length. |

**Responses**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 6894B13B-6D71- 4EF5-88FA- F32781734A7F | The ID of the request. |
| Credentials | None | None | The access credentials. |
| AccessKeyId | String | STS.L4aBSCSJVMuKg 5U1**** | The AccessKey ID. |

| Parameter | Type | Example | Description |
|---|---|---|---|
| AccessKeySecret | String | ****************************************** | The AccessKey secret. |
| SecurityToken | String | ******** | The security token. |
| Expiration | String | 2015-04- 09T11:52:19Z | The time when the STS token expires. |
| AssumedRoleUser | None | None | The temporary identity that you use to assume the RAM role. |
| Arn | String | acs:ram::123456789 012****:role/adminr ole/alice | The ARN of the temporary identity that you use to assume the RAM role. |
| AssumedRoleId | String | 34458433936495**** :alice | The ID of the temporary identity that you use to assume the RAM role. |

**Examples**

**Add Project Object Model (POM) dependencies**

The Alibaba Cloud core library is required. Perform the following steps to add the Alibaba Cloud core library to POM: <dependency> <groupId>com.aliyun</groupId> <artifactId>aliyun-java-sdk-core</artifactId> <version>[4.4.9,5.0.0)</version> </dependency>

**Call an API operation to obtain the STS AccessKey 3-tuple.**

In the following sample code, the Sts::AssumeRole::2015-04-01 operation is used to obtain the 3tuple. package com.aliyuns.test; import com.alibaba.fastjson.JSONObject; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; import org.apache.commons.lang3.StringUtils; public class STSAccessKeyDemo { public static void main(String[] args) { // Create and initialize a DefaultAcsClient instance. DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourAccessKeyID>", "<yourAccess KeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); CommonRequest request = new CommonRequest(); // Replace "sts.aliyuns.com" with the actual endpoint of STS. In most cases, the endpoint is in the follow ing format: sts-vpc.${global:region}.${global:internet-domain}. request.setSysDomain("sts.aliyuns.com"); request.setSysProduct("Sts"); request.setSysAction("AssumeRole"); request.setSysVersion("2015-04-01"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); // Replace "<yourRoleSessionName>" with the alias that you specify for the current role session. request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>"); // Replace "<yourRoleArn>" with the actual ARN that you obtained for the RAM role in the preceding ste p. request.putQueryParameter("RoleArn", "<yourRoleArn>"); try { CommonResponse response = client.getCommonResponse(request); String assumeRole = response.getData(); if (StringUtils.isEmpty(assumeRole)) return; JSONObject assumeRoleJson = JSONObject.parseObject(assumeRole); JSONObject credentials = assumeRoleJson.getJSONObject("Credentials"); // Obtain the STS AccessKey 3-tuple. String stsAK = credentials.getString("AccessKeyId"); String stsSK = credentials.getString("AccessKeySecret"); String stsToken = credentials.getString("SecurityToken"); System.out.println("stsAk: " + stsAK +"\nstsSk: " + stsSK + "\nstsToken: " + stsToken); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } } }

**Call examples**

In the following sample code, the DescribeZones operation in Elastic Compute Service (ECS) is used. package com.aliyuns.test; import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.http.FormatType; import com.aliyuncs.http.HttpClientConfig; import com.aliyuncs.http.MethodType; import com.aliyuncs.http.ProtocolType; import com.aliyuncs.profile.DefaultProfile; public class DescribeZonesDemo { public static void main(String[] args) { // Replace "<yourRegionID>" with the actual region ID. // Replace "<yourStsAccesskey>" and "<yourStsAccessKeySecret>" with the AccessKey ID and secret in t he 3-tuple that you obtained in the preceding step. DefaultProfile profile = DefaultProfile.getProfile("<yourRegionID>", "<yourStsAccessKey>", "<yourStsAcc essKeySecret>"); HttpClientConfig clientConfig = HttpClientConfig.getDefault(); clientConfig.setIgnoreSSLCerts(true); clientConfig.setProtocolType(ProtocolType.HTTPS); profile.setHttpClientConfig(clientConfig); IAcsClient client = new DefaultAcsClient(profile); CommonRequest request = new CommonRequest(); request.setSysDomain("ecs.aliyuns.com"); request.setSysProduct("Ecs"); request.setSysAction("DescribeZones"); request.setSysVersion("2014-05-26"); request.setSysMethod(MethodType.POST); request.setHttpContentType(FormatType.FORM); //Replace "<yourRegionID>" with the actual region ID. request.putHeadParameter("x-acs-regionid", "<yourRegionID>"); // Replace "<yourStsToken>" with the STS token in the 3-tuple that you obtained in the preceding step. request.putQueryParameter("SecurityToken", "<yourStsToken>"); // Optional. Specify the resource set ID. // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>"); // Required. Specify the organization ID. request.putHeadParameter("x-acs-organizationid", "<yourOrganizationID>"); try { CommonResponse response = client.getCommonResponse(request); System.out.println(response.getData()); } catch (ServerException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } catch (ClientException e) { System.out.println(e.getErrCode()); System.out.println(e.getErrMsg()); } } }

**Error codes**

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleA rn | The parameter RoleArn is wrongly formed. | The error message returned because the ARN format of the RAM role is invalid. |
| 400 | InvalidParameter.RoleS essionName | The parameter RoleSessionName is wrongly formed. | The error message returned because the value of the RoleSessionName parameter is in an invalid format. The value must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores ( ). _ |
| 400 | InvalidParameter.Durat ionSeconds | The Min/Max value of DurationSeconds is 15min/1hr. | The error message returned because the value of the DurationSeconds parameter is invalid. The minimum value is 900, and the maximum value is equal to the value of the MaxSessionDuration parameter. |
| 400 | InvalidParameter.Policy Grammar | The parameter Policy has not passed grammar check. | The error message returned because the syntax of the policy is invalid. |

| HttpCode | Error code | Error message | Description |
|---|---|---|---|
| 400 | InvalidParameter.Policy Size | The size of Policy must be smaller than 1024 bytes. | The error message returned because the length of the specified policy string exceeds the upper limit. The policy string can be up to 1,024 characters in length. |
| 403 | NoPermission | You are not authorized to do this action. You should be authorized by RAM. | The error message returned because the STS token does not have the required permissions. |
| 404 | EntityNotExist.Role | The specified Role not exists. | The error message returned because the specified RAM role does not exist. |
| 500 | InternalError | STS Server Internal Error happened. | The error message returned because an internal server error occurred. |
