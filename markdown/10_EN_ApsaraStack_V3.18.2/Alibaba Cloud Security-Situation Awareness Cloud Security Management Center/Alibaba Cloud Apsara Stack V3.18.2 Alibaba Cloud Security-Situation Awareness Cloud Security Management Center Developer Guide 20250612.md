---
title: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612"
product_version: "V3.18.2"
doc_version: "20250612"
pdf_pages: 269
source_pdf: "Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612.pdf"
source_url: "https://apsarastackdocument.oss-cn-hangzhou.aliyuncs.com/%E5%9B%BD%E9%99%85%E7%89%88%E6%96%87%E6%A1%A3/v3.18.2%E7%89%88%E6%9C%AC%E6%96%87%E6%A1%A3/%E6%80%81%E5%8A%BF%E6%84%9F%E7%9F%A5/Alibaba%20Cloud%20Apsara%20Stack%20V3.18.2%20Alibaba%20Cloud%20Security-Situation%20Awareness%20Cloud%20Security%20Management%20Center%20Developer%20Guide%2020250612.pdf"
converter: pdf2md (PyMuPDF line classifier, toc+numbered-headings+note-quotes)
---

# Alibaba Cloud Apsara Stack V3.18.2 Alibaba Cloud Security-Situation Awareness Cloud Security Management Center Developer Guide 20250612

## Table of Contents

- 1 Preparations
  - 1.1 Log on to OpenAPI Explorer
  - 1.2 View the information about an operation
  - 1.3 Obtain an AccessKey pair
  - 1.4 Obtain an AccessKey pair assigned by STS
  - 1.5 Obtain an endpoint
- 2 Call examples
  - 2.1 Call examples for SDK for Java
    - 2.1.1 Quick start
    - 2.1.2 Use SDK
      - 2.1.2.1 Install SDK for Java
      - 2.1.2.2 Use CommonRequest
  - 2.2 Call examples for SDK for Python
    - 2.2.1 Quick start
    - 2.2.2 Use SDK
      - 2.2.2.1 Install SDK for Python
      - 2.2.2.2 Use CommonRequest
  - 2.3 Call examples for SDK for Go
    - 2.3.1 Quick start
    - 2.3.2 Use SDK
      - 2.3.2.1 Install Go SDK
      - 2.3.2.2 Use CommonRequest
- 3 Common parameters
- 4 Security Operations Center
  - 4.1 Request method
    - 4.1.1 Request syntax
    - 4.1.2 Request signature
    - 4.1.3 Common parameters
    - 4.1.4 Response structure
  - 4.2 Operations
    - 4.2.1 DescribeAttacks
    - 4.2.2 DescribeAlarms
    - 4.2.3 DescribeVulFrangs
    - 4.2.4 DescribeHcFrangs
  - 4.3 Operations Center
    - 4.3.1 QueryThreats
    - 4.3.2 QueryThreatChartData
- 5 APIs
  - 5.1 CreateEventType
  - 5.2 DescribeEventType
  - 5.3 DeleteEventType
  - 5.4 CreateLogFilter
  - 5.5 DescribeLogFilter
  - 5.6 DeleteLogFilter
  - 5.7 CreateReceiver
  - 5.8 DescribeReceiver
  - 5.9 DeleteReceiver
  - 5.10 CreateRule
  - 5.11 DescribeRule
  - 5.12 EnableRule
  - 5.13 DisableRule
  - 5.14 DeleteRule
  - 5.15 CreateTask
  - 5.16 DescribeTask
  - 5.17 DeleteTask
  - 5.18 DescribeSetting
  - 5.19 ModifySetting
  - 5.20 DescribeLogType
  - 5.21 DescribeLogSource
  - 5.22 DescribeLogCountStat
  - 5.23 DescribeLog
  - 5.24 DescribeEventRisk
  - 5.25 DescribeEventRiskStat
  - 5.26 DescribeEventTypeStat
  - 5.27 DescribeEventCountStat
  - 5.28 DescribeEvent
  - 5.29 DescribeArchiveCountStat
  - 5.30 DescribeArchive
- 6 Threat Detection Service (TDS)
  - 6.1 Asset management
    - 6.1.1 DescribeFieldStatistics
    - 6.1.2 DescribeGroupedTags
    - 6.1.3 DescribeAllGroups
    - 6.1.4 DescribeInstanceStatistics
    - 6.1.5 DescribeCloudProductFieldStatistics
    - 6.1.6 DescribeCloudCenterInstances
    - 6.1.7 DescribeSummaryInfo
  - 6.2 Secure score
    - 6.2.1 DescribeSecureSuggestion
  - 6.3 Security alerts
    - 6.3.1 DescribeAlarmEventList
    - 6.3.2 DescribeAlarmEventDetail
    - 6.3.3 DescribeSuspEvents
    - 6.3.4 DescribeSuspEventDetail
  - 6.4 Configuration assessment
    - 6.4.1 DescribeRiskItemType
    - 6.4.2 StartBaselineSecurityCheck
    - 6.4.3 DescribeRiskCheckSummary
    - 6.4.4 DescribeRiskCheckResult
    - 6.4.5 DescribeSecurityCheckScheduleConfig
  - 6.5 Vulnerability management
    - 6.5.1 DescribeVulList
    - 6.5.2 DescribeVulWhitelist
    - 6.5.3 DescribeConcernNecessity
    - 6.5.4 DescribeGroupedVul
    - 6.5.5 DescribeAutoDelConfig
  - 6.6 Baseline check
    - 6.6.1 DescribeCheckWarningSummary
    - 6.6.2 DescribeStratety
    - 6.6.3 DescribeStrategyExecDetail
    - 6.6.4 DescribeCheckWarnings
    - 6.6.5 DescribeCheckWarningDetail
    - 6.6.6 DescribeWarningMachines
  - 6.7 Asset fingerprints
    - 6.7.1 DescribePropertyCount
    - 6.7.2 DescribePropertyPortDetail
    - 6.7.3 DescribePropertyProcDetail
    - 6.7.4 DescribePropertyPortItem
    - 6.7.5 DescribePropertyProcItem
    - 6.7.6 DescribePropertySoftwareDetail
    - 6.7.7 DescribePropertySoftwareItem
    - 6.7.8 DescribePropertyUserDetail
    - 6.7.9 DescribePropertyUserItem
    - 6.7.10 DescribeModuleConfig
  - 6.8 Asset exposure
    - 6.8.1 DescribeExposedInstanceList
- 7 Error codes

## 1 Preparations

### 1.1 Log on to OpenAPI Explorer

You can log on to OpenAPI Explorer from the Apsara Uni-manager Management Console.

**Prerequisites**

The URL of the Apsara Uni-manager Management Console is obtained from the deployment personnel. A browser is available. We recommend that you use Google Chrome.

**Procedure**

1. Enter the URL of the Apsara Uni-manager Management Console in the address bar of a
browser and press the Enter key.
2. Enter your username and password.
Obtain the username and password from an operations administrator.

> **Note:** The first time you log on to the Apsara Uni-manager Management Console, you must change the password of your account. For security purposes, your password must meet the minimum complexity requirements. The password must be 10 to 32 characters in length and must contain at least two of the following character types:
> Letters
> Digits
> Special characters, including exclamation points (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%)

3. Click **Log on**.
4. If multi-factor authentication (MFA) is enabled for your account, perform the corresponding
operations in the following scenarios: The first time you log on to the Apsara Uni-manager Management Console after MFA is enabled by the administrator. a. On the Bind Virtual MFA Device page, bind an MFA device. b. Re-enter the username and password as in Step 2 and click **Log On**. c. Enter a six-digit MFA verification code and click **Authenticate**. You have enabled MFA and bound an MFA device. Enter a six-digit MFA verification code and click **Authenticate**.

> **Note:** For more information, see the **Bind a virtual MFA device to enable MFA** topic in **Apsara Uni-manager Management Console User Guide** .

5. In the top navigation bar, choose **Products > Application Services > OpenAPI**
**Explorer**.

### 1.2 View the information about an operation

**operation**

When you use a service SDK to call an operation of the service, you must obtain the service name, operation name, and API version. This topic describes how to view the information about an operation.

**Background information**

The operations on the API Directory page are for reference only. For information about how to call operations, see API references of the corresponding services. If the information on the API Directory page is inconsistent with that in the API reference of the corresponding service, the information in the API reference takes precedence.

**Procedure**

1. Log on to OpenAPI Explorer.
2. In the left-side navigation pane, click **API Directory**.
3. On the **API Directory** page, select the required service from the drop-down list, enter a
keyword of an operation name in the search box, and then click Search.
4. View and record the service name, operation name, and API version.

### 1.3 Obtain an AccessKey pair

Access credentials are assigned by Resource Access Management (RAM) or Security Token Service (STS). You can use one type of access credential for authentication when you make an API request. This topic describes how to obtain an AccessKey pair that is assigned by RAM.

**Background information**

An AccessKey pair is used to verify the identity of a request sender. An AccessKey pair consists of an AccessKey ID and an AccessKey secret that are used to implement symmetric encryption. The AccessKey ID is used to identify a user. The AccessKey secret is used to encrypt the signature string. You can use RAM or STS to assign an access credential for authentication. An AccessKey pair that is assigned by RAM to a third party consists of an AccessKey ID and an AccessKey secret. An access credential that is assigned by STS to a third party consists of an AccessKey ID, an AccessKey secret, and a security token. For more information, see Obtain an AccessKey pair assigned by STS. The Apsara Uni-manager Management Console provides AccessKey pairs to personal accounts and organizations. Only the administrators of level-1 organizations and operations administrators can obtain the AccessKey pairs of organizations. We recommend that you use the AccessKey pairs of personal accounts to call the operations provided by the Apsara Unimanager Management Console and cloud services. If you use the AccessKey pair of a personal account, configure the header parameters that are described in the following table for access control. Otherwise, an error that indicates insufficient permissions may occur.

> **Warning:** The AccessKey pair of a personal account is managed and limited by the permission system of the Apsara Uni-manager Management Console. If you need to obtain the AccessKey pair of an organization, make sure that your operation is allowed by an administrator. This ensures security.

| Parameter | Description |
|---|---|
| x-acs-regionid | The ID of the region. Example: cn-hangzhou-*. |
| x-acs-organizationid | The ID of the organization in the Apsara Uni- manager Management Console. For more information about how to obtain an organization ID, see the GetOrganizationList section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-resourcegroupid | The ID of the resource set in the Apsara Uni- manager Management Console. For more information about how to obtain a resource set ID, see the "ListResourceGroup" section in Apsara Uni-manager Management Console Developer Guide. |
| x-acs-instanceid | The ID of the instance that you want to manage. If you want to obtain the ID of an Elastic Compute Service (ECS) instance, you can obtain the ID from the ECS instance list. |

**Obtain the AccessKey pair of a personal account**

To obtain the AccessKey pair of a personal account, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console.
2. Click the profile picture in the upper-right corner of the page and click **User Information**.
3. In the **AccessKey Pair** section, view the AccessKey pair of the personal account.

> **Note:** The AccessKey pair provides full permissions on cloud resources within your Alibaba Cloud account. You must keep the AccessKey pair confidential.

**Obtain the AccessKey pair of an organization**

To obtain the AccessKey pair of an organization, perform the following steps:
1. Log on to the Apsara Uni-manager Management Console as an administrator.
2. In the top navigation bar, click **Enterprise**.
3. In the left-side navigation pane, choose **Resources > Organizations**.
4. In the organization list, click the name of the level-1 organization whose AccessKey pair you
want to obtain.
5. On the right side of the page that appears, click **Management AccessKey**.
6. In the dialog box that appears, view the AccessKey pair of the organization.

### 1.4 Obtain an AccessKey pair assigned by STS

**assigned by STS**

This topic describes how to use Security Token Service (STS) to make API calls.

**Background information**

Alibaba Cloud STS allows you to manage temporary credentials to your Alibaba Cloud resources. You can use STS to make API calls. An AccessKey pair assigned by STS consists of an AccessKey ID, an AccessKey secret, and a security token. When you use STS to make API calls, you must use an AccessKey pair assigned by STS.

**Procedure**

1. Obtain your `RAM role` .
i. Log on to the Apsara Uni-manager Management Console. ii. Click the profile picture in the upper-right corner of the page and click **User**
**Information**.
iii. Click **View Current Role Policy**. In the **View Policies of Current Role** dialog box, view your `RAM role` .
2. Obtain the AccessKey pair assigned by STS.

> **Note:** You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourRoleSessionName>: Replace it with your current session name.
> In most cases, this variable is set to the identity of the user who make API calls. Example: Username. You can distinguish the users who assume the same RAM role to perform operations based on the value of the `RoleSessionName` variable. This way, you can perform user-specific auditing. The value of this variable must be 2 to 64 characters in length and can contain letters, digits, periods (.), at signs (@), hyphens (-), and underscores (_).
> <yourRoleArn>: Replace it with the Alibaba Cloud Resource Name (ARN) of your RAM role.
> "sts.aliyuns.com": Replace it with the actual endpoint of STS.

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
    // Obtain the AccessKey pair assigned by STS.
    String stsAK = credentials.getString("AccessKeyId");
    String stsSK = credentials.getString("AccessKeySecret");
    String stsToken = credentials.getString("SecurityToken");
```

`}`

```java
private static String callAssumeRole(IAcsClient client) {
    CommonRequest request = new CommonRequest();
    // Replace "sts.aliyuns.com" with the endpoint of STS. The format of an STS endpo
int is sts-vpc.${global:region}.${global:internet-domain}.
    request.setSysDomain("sts.aliyuns.com");
    request.setSysProduct("Sts");
    request.setSysAction("AssumeRole");
    request.setSysVersion("2015-04-01");
    request.setSysMethod(MethodType.POST);
    request.setHttpContentType(FormatType.FORM);
    // Replace "<yourRoleSessionName>" with the actual session name.
    request.putQueryParameter("RoleSessionName", "<yourRoleSessionName>");
    // The ARN of your RAM role. Replace "<yourRoleArn>" with the ARN of your RAM rol
e that is obtained in the previous step.
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
3. Use the AccessKey pair assigned by STS to call an operation of a cloud service. The
following sample code provides an example on how to use the AccessKey pair assigned by STS to call the `DescribeZones` operation of Elastic Compute Service (ECS):

> **Note:** You must use the actual values to replace the variables in the following sample code. The angle brackets <> are not retained in the final code.
> The following list describes the variables:
> <yourRegionID>: Replace it with the actual region ID.
> <yourAccessKeyID>: Replace it with the actual region ID.Replace it with your AccessKey ID.
> <yourAccessKeySecret>: Replace it with your AccessKey secret.
> <yourStsToken>: Replace it with the security token of the AccessKey pair assigned by STS.
> <yourResourceGroupID>: Replace it with the actual resource set ID.
> <yourResourceGroupID>: Replace it with the actual organization ID.

```java
public static void main(String[] args) {
    // Replace "<yourRegionID>" with the actual region ID.
    // Replace "<yourStsAccessKeyID>" and "<yourStsAccessKeySecret>" with the AccessK
ey ID and AccessKey secret of the AccessKey pair assigned by STS. The AccessKey ID an d AccessKey secret are obtained in the previous step.
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
    // Replace "<yourRegionID>" with the actual region ID.
    request.putHeadParameter("x-acs-regionid", "<yourRegionID>");
    // Replace "<yourStsToken>" with the STS token of the AccessKey pair assigned by
STS. The STS token is obtained in the previous step.
    request.putQueryParameter("SecurityToken", "<yourStsToken>");
    // Optional. Replace "<yourResourceGroupID>" with the actual resource set ID.
    // request.putHeadParameter("x-acs-resourcegroupid", "<yourResourceGroupID>");
    // Optional. Replace "<yourOrganizationID>" with the actual organization ID.
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

### 1.5 Obtain an endpoint

This topic describes how to obtain the endpoint of an Apsara Stack Security service.

**Background information**

To use the POP gateway to call the API operations of a cloud service, you must specify the endpoint of the cloud service. You can obtain the endpoint from Apsara Stack onsite O&M engineers. You can also perform the following steps to obtain the endpoint.

**Procedure**

1. Log on to the Apsara Uni-manager Operations Console.
2. In the top navigation bar, choose **Platform Operation > Resources**.
3. In the left-side navigation pane, click **Product & Cluster O&M**.
4. Enter sas-securityoperationscentercluster in the **Product | Cluster** search box. Then, click
**Cluster Details** in the Actions column.
5. On the **Services** tab, click the name of the service.
6. Click the **yundun-soc** component in the **Components** section. Then, click the
**Registration Variables** tab and enter yundunsoc.pop.endpoint in the search box to obtain
the endpoint of the service.
7. The endpoint of a service is in the following format:

```
${EndpointPre}.${global:region}.${global:internet-domain}
```

s

## 2 Call examples

### 2.1 Call examples for SDK for Java

#### 2.1.1 Quick start

This topic describes how to obtain and use Apsara Stack SDK for Java.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Java. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint. Java Development Kit (JDK) 1.8 or later is installed.

**Installation**

If you use Apache Maven to manage a Java project, you need to only import the JAR file of Apsara Stack SDK for Java to the pom.xml file of the project. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library.

**Usage**

To use Apsara Stack SDK for Java, perform the following steps:
1. Create a DefaultAcsClient instance and initialize the instance.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
> The following list describes the variables:
> <your-region-id>: Replace this variable with the region ID.
> <your-access-key-id>: Replace this variable with your AccessKey ID.
> <your-access-key-secret>: Replace this variable with your AccessKey secret.
> <your-endpoint>: Replace this variable with the endpoint of the service.
> <API-version>: Replace this variable with the version of the API.
> <your-action>: Replace this variable with the name of the API operation.

s

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<your-access-key-id>",      // The AccessKey ID.
            "<your-access-key-secret>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<your-endpooint>");// The endpoint of the service.
        request.setVersion("<API-version>");// The version of the API.
        request.setAction("<your-action>");// The name of the API operation.
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
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

#### 2.1.2 Use SDK

##### 2.1.2.1 Install SDK for Java

This topic describes how to install and use Apsara Stack Security SDK for Java. Apsara Stack SDK for Java supports Java Development Kit (JDK) 1.8 or later. You can install Apsara Stack SDK for Java by adding Maven dependencies or downloading the SDK. For more information, visit Alibaba Cloud SDKs. If you want to use Apsara Stack Security SDK for Java, you must install the core library of Apsara Stack SDK for Java. We recommend that you use V4.5.17 or later of the core library. When you install the core library, you must add the following dependency to the pom.xml file. For more information about the specific SDK version, visit Alibaba Cloud SDKs. s

```xml
<!-- Alibaba Cloud SDK for Java --> <dependency>
    <groupId>com.aliyun</groupId>
    <artifactId>aliyun-java-sdk-core</artifactId>
    <version>4.5.17</version>
</dependency>
```

##### 2.1.2.2 Use CommonRequest

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code shows how to use CommonRequest to call an API operation of Apsara Stack Security: s

```java
import com.aliyuncs.CommonRequest; import com.aliyuncs.CommonResponse; import com.aliyuncs.DefaultAcsClient; import com.aliyuncs.IAcsClient; import com.aliyuncs.exceptions.ClientException; import com.aliyuncs.exceptions.ServerException; import com.aliyuncs.profile.DefaultProfile; public class Sample {
    public static void main(String[] args) {
        // Create a DefaultAcsClient instance and initialize the instance.
        DefaultProfile profile = DefaultProfile.getProfile(
            "<your-region-id>",          // The ID of the region.
            "<YOUR-ACCESS-KEY-ID>",      // The AccessKey ID.
            "<YOUR-ACCESS-KEY-SECRET>"); // The AccessKey secret.
        IAcsClient client = new DefaultAcsClient(profile);
        // Create an API request and configure the required parameters.
        CommonRequest request = new CommonRequest();
        request.setDomain("<YOUR-ENDPOINT>");// The endpoint of the service.
        request.setVersion("<API-version>");// The version of the API.
        request.setAction("<YOUR-ACTION>");// The name of the API operation.
        request.putQueryParameter("PageNumber", "1");
        request.putQueryParameter("PageSize", "30");
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

### 2.2 Call examples for SDK for Python

**Python**

#### 2.2.1 Quick start

This topic describes how to obtain and use Apsara Stack SDK for Python.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Python. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Installation**

s If you use Python 2.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library of Apsara Stack SDK for Python:

```
pip3 install aliyun-python-sdk-core-v3
```

**Usage**

To use Apsara Stack SDK for Python, perform the following steps:
1. Create a client instance.
Before you create a client instance, you must obtain a region ID, an AccessKey ID, and an AccessKey secret.
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
> The following list describes the variables:
> <your_region_id>: Replace this variable with the region ID.
> <your_access_key_id>: Replace this variable with your AccessKey ID.
> <your_access_key_secret>: Replace this variable with your AccessKey secret.
> <your-endpoint>: Replace this variable with the endpoint of the service.
> <API-version>: Replace this variable with the version of the API.
> <your-action>: Replace this variable with the name of the API operation.

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<your-endpoint>')// The endpoint of the service. request.set_version('<API-version>')// The version of the API. request.set_action_name('<your-action>')// The name of the API operation.
# or:
# request =
CommonRequest(domain='<your-endpoint>', version='<API-version>', action_name='<your-action>') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

s

#### 2.2.2 Use SDK

##### 2.2.2.1 Install SDK for Python

This topic describes how to install and use SDK for Python. Apsara Stack SDK for Python supports Python 2.6.x, Python 2.7.x, and Python 3.x or later. You can install Apsara Stack SDK for Python by using pip.

> **Note:** To use the SDK of an Apsara Stack service, you must install the core library of Apsara Stack SDK for Python.

If you use Python 2.x, run the following command to install the core library:

```
pip install aliyun-python-sdk-core
```

If you use Python 3.x, run the following command to install the core library:

```
pip3 install aliyun-python-sdk-core-v3
```

##### 2.2.2.2 Use CommonRequest

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. s The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation:

```bash
from aliyunsdkcore.client import AcsClient from aliyunsdkcore.request import CommonRequest client = AcsClient('{your_access_key_id}', '{your_access_key_secret}', '{your_region_id}') request = CommonRequest() request.set_domain('<YOUR-ENDPOINT>') //The endpoint of the service. request.set_version('<API-version>') //The version of the API. request.set_action_name('<YOUR-ACTION>')//The name of the API operation.
# or:
# request = CommonRequest(domain='<your-endpoint>', version='<API-version>',
action_name='your-action') request.add_query_param('PageNumber', '1') request.add_query_param('PageSize', '30') response = client.do_action_with_exception(request)
```

### 2.3 Call examples for SDK for Go

#### 2.3.1 Quick start

Apsara Stack SDK for Go allows you to access services without complex coding. This topic describes how to obtain and use Apsara Stack SDK for Go.

**Prerequisites**

An Apsara Stack tenant account that has the required permissions and an AccessKey pair that consists of an AccessKey ID and an AccessKey secret are obtained before you can use Apsara Stack SDK for Go. You can view and obtain your AccessKey pair in the Apsara Unimanager Management Console. For more information, see Obtain an AccessKey pair. The endpoint of a service is obtained. For more information, see Obtain an endpoint.

**Install the core package of Apsara Stack SDK for Go**

Apsara Stack SDK for Go supports Go 1.10.x and later. You can run the following command to install the core library:

```
go get -u github.com/aliyun/alibaba-cloud-sdk-go/sdk
```

**Use Apsara Stack SDK for Go**

To use Apsara Stack SDK for Go, perform the following steps:
1. Initialize a client instance.
s
2. Create an API request and configure the required parameters.
3. Initiate the API request and process the response or exception.

> **Note:** |In the following sample code, replace the variables with actual values based on your business requirements and remove the angle brackets <> from the final code.
> The following list describes the variables:
> <your_region_id>: Replace this variable with the region ID.
> <your_access_key_id>: Replace this variable with your AccessKey ID.
> <your_access_key_secret>: Replace this variable with your AccessKey secret.
> <your-endpoint>: Replace this variable with the endpoint of the service.
> <API-version>: Replace this variable with the version of the API.
> <your-action>: Replace this variable with the name of the API operation.

```java
package main import ( "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests" "github.com/aliyun/alibaba-cloud-sdk-go/sdk" "fmt"
```

`)`

```
func main() { client, err := sdk.NewClientWithAccessKey("<your_region_id>", "{your_access_key_id}", "{your_access_key_secret}") if err != nil { panic(err)
```

`}`

```
 request
:= requests.NewCommonRequest() request.Domain = "<your-endpoint>"// The endpoint of the service. request.Version = "<API-version>"// The version of the API. request.ApiName = "<your-action>"// The name of the API operation. request.QueryParams["PageNumber"] = "1" request.QueryParams["PageSize"] = "30" response, err := client.ProcessCommonRequest(request) if err != nil { panic(err)
```

`}`

```
fmt.Print(response.GetHttpContentString())
```

`}`

#### 2.3.2 Use SDK

##### 2.3.2.1 Install Go SDK

This topic describes how to install the Go SDK. The Alibaba Cloud Go SDK supports Go 1.7 or later versions. Install the Go SDK manually.
1. Download the source code of the Go SDK from the official site of Apsara Stack.
s
2. Extract the package to the directory where the GO_PATH file of the current user resides.

##### 2.3.2.2 Use CommonRequest

> **Note:** If you want to call the API operations of an Apsara Stack service that does not provide SDKs, you can use CommonRequest. You can use CommonRequest to call API operations.

**Benefits**

CommonRequest provides the following benefits:
1. Lightweight: You need to only download the core package. You do not need to download
and install SDKs of Apsara Stack services.
2. Easy to use: You can call the newly released API operations of an Apsara Stack service
without the need to update the SDK for the service.
3. Fast iteration.

**Use CommonRequest to call an API operation**

Apsara Stack services provide remote procedure call (RPC) and RESTful APIs. The request method of CommonRequest varies based on the style of the API that you want to call. In most cases, an API uses the RPC style if the API operations include the Action parameter. An API uses the RESTful style if the API operations include the PathPattern parameter. All API operations of a service use the same API style. The API of each service supports only one style. If you pass an invalid identifier, another API operation may be called, or the `ApiNotFound` error is returned. If you want to send a CommonRequest request, you must obtain the values of the following parameters. For more information, see Common parameters. Endpoint: the endpoint of the service. Version: the version of the API. The version is in the YYYY-MM-DD format. Operation information: the name of the API operation that you want to call. The APIs of most Apsara Stack services, such as Threat Detection Service, are RPC APIs. If you want to call an RPC API operation, you must obtain the value of the Action parameter, and then specify the value in the `request.ApiName = "<Action>"` format. If you want to call a RESTful API operation of a service, such as Container Service for Kubernetes (ACK), you must obtain the value of the PathPattern parameter, and then specify the RESTful path in the `request.PathPattern = "<PathPattern>"` format.

**Example: Call an RPC API operation**

The following sample code provides an example on how to use CommonRequest to call an API operation: s

```java
package main import (
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
    "github.com/aliyun/alibaba-cloud-sdk-go/sdk"
    "fmt"
```

`)`

```
func main() {
    client, err := sdk.NewClientWithAccessKey("cn-hangzhou", "{your_access_key_id}", "{
your_access_key_secret}")
    if err != nil {
        panic(err)
```

`}`

```
    request := requests.NewCommonRequest()
    request.Domain = "<YOUR-ENDPOINT>"// The endpoint of the service.
    request.Version = "<API-version>"// The version of the API.
    request.ApiName = "<YOUR-ACTION>"// The name of the API operation.
    request.QueryParams["PageNumber"] = "1"
    request.QueryParams["PageSize"] = "30"
    response, err := client.ProcessCommonRequest(request)
    if err != nil {
        panic(err)
```

`}`

```
    fmt.Print(response.GetHttpContentString())
```

`}` ameters

## 3 Common parameters

**Common request parameters**

Common request parameters must be included in all Apsara Stack Security API requests. Table 1. Common request parameters

| Parameter | Type | Requi red | Description |
|---|---|---|---|
| Format | Strin g | No | The type of the returned value. Set the value to JSON. |
| Version | Strin g | Yes | The version number of the API. Specify the version number in the YYYY-MM-DD format. Valid values: 2018-01-16: Auditprivate 2019-07-23: yundunnextsoc 2018-12-03: Sas 2016-11-11: aegis 2021-10-11: yundun-css 2019-08-05: secspy 2018-01-16: Ddosprivate 2018-06-30: hsm-private 2017-12-07: Cloudfw 2019-01-03: Sddp 2020-07-01: semawaf 2018-12-03: soar |
| AccessKeyId | Strin g | Yes | The AccessKey ID that is provided by Apsara Stack. |
| AccessKeySe cret | Strin g | Yes | The AccessKey secret that is provided by Apsara Stack. |
| RegionId | Strin g | Yes | The region ID of the service. |

ameters

| Product | Strin g | Yes | The name of the service to which the operation belongs. Valid values: Auditprivate: basic components of Apsara Stack Security yundunnextsoc: Security Operations Center (SOC) Sas: Threat Detection Service aegis: Server Guard yundun-css: Container Protection secspy: Network Detection and Response Ddosprivate: Anti-DDoS Service hsm-private: Data Encryption Service Cloudfw: Cloud Firewall Sddp: Sensitive Data Discovery and Protection (SDDP) semawaf: Web Application Firewall (WAF) soar: Security Orchestration and Automation Response (SOAR) |
|---|---|---|---|
| EndpointPre | Strin g | Yes | The prefix in the endpoint of the service to which the operation belongs. Valid values: auditprivate: the prefix in the endpoint of basic components of Apsara Stack Security yundunnextsoc-pop: the prefix in the endpoint of SOC tds: the prefix in the endpoint of Threat Detection Service aegis: the prefix in the endpoint of Server Guard yundun-css: the prefix in the endpoint of Container Protection secspy-share: the prefix in the endpoint of Network Detection and Response ddosprivate: the prefix in the endpoint of Anti-DDoS Service hsmprivate: the prefix in the endpoint of Data Encryption Service cloudfw: the prefix in the endpoint of Cloud Firewall sddp-api: the prefix in the endpoint of SDDP semawaf: the prefix in the endpoint of WAF soar: the prefix in the endpoint of SOAR |

**Common response parameters**

API responses use the HTTP response format: A 2xx status code indicates a successful call. A 4xx or 5xx status code indicates a failed call. Responses are returned in the JSON format. Every response returns a unique RequestID regardless of whether the call is successful. rations Center

## 4 Security Operations Center

### 4.1 Request method

#### 4.1.1 Request syntax

where: `endpoint` : the endpoint of the Security Operations Center (SOC) API is `yundunnewsoc-pop.`

```
[ RegionId].example.com .
```

**Note**

`Action` : the name of the operation being performed. For example, if `Action=GetEcsProtectCount` ,You can call this operation to query the number of ECS instances with an online Server Guard agent and the number of ECS instances with an offline agent.

#### 4.1.2 Request signature

**Signature**

| Parameter | Description |
|---|---|
| Endpoint | http://yundunnewsoc-pop.[RegionId].example.com/? |
| Operation-specific parameters | Action=GetEcsProtectCount |
| Common parameters except Signature | &Timestamp=2016-02-23T12:46:24Z &Format=JSON &AccessKeyId=<yourAccessKeyId> &SignatureMethod=HMAC-SHA1 &SignatureNonce=3ee8c1b8-83d3-44af-a94f-4e0ad82fd6cf &Version=2019-07-23 &SignatureVersion=1.0 |
| Access Key Secret | <yourAccessKeySecret> |

1. Create a canonicalized query string by arranging the request parameters.
rations Center

> **Note:** The request parameters include operation-specific parameters and all common request parameters except Signature.

i. Sort the request parameters. Sort the request parameters in alphabetical order. ii. Encode the parameters. Encode the canonicalized query string in UTF-8 based on the following rules: Uppercase letters, lowercase letters, digits, and some special characters such as hyphens (-), underscores (_), periods (.), and tildes (~) do not need to be encoded. Other characters must be percent encoded in the %XY format. XY represents the ASCII code of the characters in hexadecimal notation. For example, double quotation marks (") are encoded as %22. Extended UTF-8 characters are encoded in the %XY%ZA… format. Spaces must be encoded as %20. Do not encode spaces as plus signs (+). iii. Connect the encoded parameter names and values by using equal signs (=). iv. Sort the pairs of parameter names and values that are connected by using equal signs (=) in alphabetical order. Connect the pairs with ampersands (&) to create a canonicalized query string.
2. Create a string-to-sign from the encoded canonicalized query string based on the following
rule:

```
StringToSign=HTTPMethod + "&" + percentEncode("/") + "&" + percentEncode(CanonicalizedQueryString)
```

3. Calculate the HMAC value of the string-to-sign based on the HMAC definition in RFC 2104.

> **Note:** Your AccessKey secret in combination with an ampersand (&) (ASCII:38) is used as the key for the HMAC calculation. The SHA1 algorithm is used to calculate the HMAC value of the string-to-sign.

4. Encode the HMAC value in Base64 to obtain the signature string.

```
LEW8N4y7Uasop******
```

5. Add the signature string to the request as the Signature parameter. The result is the signed
API request.

#### 4.1.3 Common parameters

Common request parameters must be included in all Apsara Stack Security API requests, such as the API version number and authentication information.

| Parameter | Type | Required | Description |
|---|---|---|---|
| Version | String | Yes | The version number of the API. The value is in the YYYY-MM-DD format. Set the value to 2019-07-23. |
| AccessKeyId | String | Yes | The AccessKey ID that is provided by Apsara Stack. |

rations Center

| Signature | String | Yes | The signature string of the request. |   |   |
|---|---|---|---|---|---|
| SignatureMethod | String | Yes | The encryption algorithm of the signature string. Set the value to HMAC-SHA1. |   |   |
| Timestamp | String | Yes | The timestamp of the request. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time must be in UTC. The value must be in the YYYY-MM- DDThh:mm:ssZ format. For example, use 2014-05- 26T12:00:00Z to indicate May 26, 2014, 12:00:00 (UTC+8). |   |   |
|   |   |   |   | YYYY-MM- |   |
| SignatureVersion | String | Yes | The version of the signature encryption algorithm. Set the value to 1.0. |   |   |
| SignatureNonce | String | Yes | A unique random number that is used to prevent replay attacks. You must use different numbers for different requests. |   |   |
| ResourceOwnerA ccount | String | No | The Apsara Stack tenant account to which the resource you want to access belongs, which is the username. |   |   |
| Format | String | No | The response format. Valid values: JSON and XML. Note Default value: XML. |   |   |

|   | DDThh:mm:ssZ |
|---|---|

#### 4.1.4 Response structure

Apsara Stack Security API responses can be returned in either the XML or JSON format. Every response returns a unique ID (indicated by **RequestId**) regardless of whether the call is successful.

**Sample responses (XML format)**

rations Center

```xml
<? xml version="1.0" encoding="UTF-8"? > <! --The root node of the result--> <Operation name+Response>
    <! --Returned request ID-->
    <RequestId>4C467B38-3910-447D-87BC-AC049166F216</RequestId>
    <! --Returned data-->
</Operation name+Response>
```

**Sample responses (JSON format)**

`{`

```json
"RequestId": "4C467B38-3910-447D-87BC-AC049166F216", /* Returned data */
```

`}`

### 4.2 Operations

#### 4.2.1 DescribeAttacks

Queries attacks on the user side or the platform side based on specified conditions.

**Request headers**

The CreateBackupPlan operation does not have operation-specific request headers and uses only common request headers. For more information, see the "Common headers" section of the "Common parameters" topic.

**Request parameters**

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Action | Strin g | Query | Yes | DescribeAttacks | The operation that you want to perform. Set the value to DescribeAttacks. |
| DataScop e | Integ er | Query | No | 1 | Specifies whether to query the attacks on the user side or the platform side. Valid values: 0: indicates the platform side. 1: indicates the user side. |
| PageSize | Integ er | Query | No | 10 | The number of entries per page. |
| PageNo | Integ er | Query | No | 1 | The page number. |

| r Developer ations Center | Guide·Se | curity Ope |   | Aliba | ba Cloud Security-Situation Awarenes |
|---|---|---|---|---|---|

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| SourceFro m | Integ er | Query | No | 41 | The source of attack data. Valid values: 40:Web Application Firewall. 41: Cloud Firewall. 42: Anti-DDoS (aliguard). 44: Network Traffic Monitoring System (IDS). 46: Threat detection (brute-force attack protection) |
| UserId | Long | Query | No | 2956140888888888 | The ID of the organization. |
| AttackTyp e | Strin g | Query | No | Brute-force Attack | The type of the attack. Valid values: Brute- force Attack , Non- web Attack , and SQL Injection . |
| ProcessSt ate | Integ er | Query | No | 1 | The handling status. Valid values: 2: The alert is sent. 1: Defended 3: cleaning. 4: The cleaning process ends. |
| StartTime | Long | Query | No | 1641398400000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | Query | No | 1643644800000 | The end of the time range to query. Unit: milliseconds. |

rations Center

| Parame ter | Typ e | Positi on | Require d | Examples | Description |
|---|---|---|---|---|---|
| Keyword | Strin g | Query | No | 192.168.XX.XX | The keyword to match. You can specify an attack name, an asset name, or the IP address of an asset. |
| Asset | Strin g | Query | No | ae3ef6ef-8888-4aee- 8bac-19879e68**** | The ID of the asset. |
| Lang | Strin g | Query | No | zh CN _ | The language of the content within the request and the response. Valid values: zh CN: Simplified _ Chinese zh TW: Traditional _ Chinese en US: English _ |
| AssetType | Strin g | Query | No | ECS | The type of the affected asset. Valid values include ECS , SLB , OSS , EIP , and RDS . |

**Response parameters**

| Parameter | Type | Examples | Description |
|---|---|---|---|
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The request ID. |
| Data | Struct |   | The data that is returned. |
| -Items | Array |   | The retrieved data. |
| --AttackerIp | String | 10.0.X.X | The IP address of the attacker. |
| --AttackType | Integer | 1 | The type of the attack. |
| --AttackId | Integer | 10154212 | The ID of the attack. |

| C e r | loud Security Ma r Developer Guid ations Center | nagement Cent e·Security Ope |   | Alibaba Cloud Security-Situation Awarenes | s |
|---|---|---|---|---|---|

| Parameter | Type | Examples | Description |
|---|---|---|---|
| --ProcessState | Integer | 1 | The handling status. Valid values: 2: The alert is sent. 1: Defended 3: cleaning. 4: The cleaning process ends. |
| --AttackTrait | String | 1 | This parameter is deprecated. |
| --SourceFrom | String |   | The source of attack data. Valid values: 40:Web Application Firewall. 41: Cloud Firewall. 42: Anti-DDoS (aliguard). 44: Network Traffic Monitoring System (IDS). 46: Threat detection (brute-force attack protection) |
| --UserId | Long | 295614088888888 8 | The ID of the organization. |
| --UserName | String | Organization A | The name of the organization. |
| --RaisedTime | Long | 1641548505000 | The time of the attack. |
| --AssetType | Integer | 1 | The type of the affected asset. |
| --AttackName | String | zz 78**** _ | The name of the attack. |
| --Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the attacked asset. |
| -- SourceFromIp | String | 10.0.X.X | The source IP address of the attack. |
| --TargetIp | String | 10.0.X.X | The destination IP address of the attack. |
| --AssetName | String | SSH brute- force**** | The name of the attacked asset. |
| -- AssetPublicIps | String | 192.168.XX.XX | The public IP address of the affected asset. |

rations Center

| Parameter | Type | Examples | Description |
|---|---|---|---|
| -- AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the affected asset. |
| -Total | Integer | 20 | The total number of entries returned. |
| -PageNo | Integer | 1 | The page number. |
| -PageSize | Integer | 10 | The number of entries per page. |

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAttacks &DataScope=1 &PageSize=20 &PageNo=1 &<Common request parameters>
```

Sample success response `JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"20","PageNo":"1","Items":[{"UserName":"Organization A","Attac kTrait":"1","SourceFrom":"1","AttackType":"1" "AttackerIp":"10.0.X.X","AssetName":"SSH brute force****","SourceFromIp":"10.0.X.X","AssetPrivateIps":"192. XX.XX","ProcessState":"1","AssetType":"1","AttackId":"10154212","Attack_Name":":" "2956 140888888888","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6 ef-8888-4aee-8bac-19879e6 8****","TargetIp":"10.0.X.X","RaisedTime":"1641548505000"}]}}
```

`XML` format rations Center

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>20</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>Organization A</UserName>
        <AttackTrait>1</AttackTrait>
        <SourceFrom>1</SourceFrom>
        <AttackType>1</AttackType>
        <AttackerIp>10.0.X.X</AttackerIp>
        <AssetName>SSH brute-force****</AssetName>
        <SourceFromIp>10.0.X.X</SourceFromIp>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>1</AssetType>
        <AttackId>10154212</AttackId>
        <AttackName>zz_78****</AttackName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <TargetIp>10.0.X.X</TargetIp>
        <RaisedTime>1641548505000</RaisedTime>
    </Items>
</Data>
```

#### 4.2.2 DescribeAlarms

Queries security alerts on the user side or the platform side based on specified conditions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarms | The operation that you want to perform. Set the value to DescribeAlarms. |
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: 0: platform 1: user |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| PageNo | Integer | No | 1 | The number of the page to return. |

rations Center

| StartTime | Long | No | 1609430400000 | The beginning of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|
| EndTime | Long | No | 1645977600000 | The end of the time range to query. Unit: milliseconds. |
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled 3: ignored |
| RiskLevels.N | RepeatL ist | No | 1 | The risk levels to query. Valid values: 0: reminder. 1: suspicious. 2: urgent. You can specify multiple values in an array. Separate the values with commas. |
| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify an alert name, an asset name, or an IP address of an asset. |
| SourceFrom | Integer | No | 20 | The source of data. Valid values: 20: Threat Detection Service or Server Guard |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| AlarmType | String | No | Suspicious network connection | The type of the alert. Valid values include Other, Suspicious network connection, Webshell, Suspicious process, and Unusual logon. |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| AssetType | String | No | ECS | The type of the affected asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |

rations Center

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The data that is returned. |
| Items | Array of Item |   | The list of the returned data. |
| AlarmId | Integer | 4008888 | The ID of the alert. |
| AlarmName | String | Reverse** | The name of the alert. |
| AlarmType | String | Suspicious process | The type of the alert. Valid values include Other, Suspicious network connection, Webshell, Suspicious process, and Unusual logon. |
| AlarmUniqueIn fo | String | eeee98dd0c4cd5cc 61c016b2bdcf**** | The unique identifier of the alert. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the affected asset. |
| AssetName | String | zzzz 88**** _ | The name of the affected asset. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the affected asset. |
| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the affected asset. |
| AssetType | String | ECS | The type of the affected asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Detail | String | {"lastTime": 1641536460051,"a ssetsType": 0,"modifiedTime": "2022-01-07 14:21:00"} | The details. |
| LastTime | Integer | 1641537619 | The time when the alert was last generated. Unit: milliseconds. |

rations Center

| ProcessState | Integer | 1 | The handling status. Valid values: 1: unhandled 2: handled 3: ignored |
|---|---|---|---|
| RaisedTime | Long | 1640931449000 | The time at which the alert was first generated. Unit: milliseconds. |
| RiskLevel | Integer | 2 | The risk level of the alert. Valid values: 0: reminder 1: suspicious 2: urgent |
| SourceFrom | Integer | 20 | The source of data. Valid values: 20: Threat Detection Service or Server Guard |
| UserId | Integer | 295614088 | The ID of the organization. |
| UserName | String | Organization A | The name of the organization. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeAlarms &RiskLevels=[0,1,2] &DataScope=1 &PageSize=20 &PageNo=1 &<Common request parameters>
```

Sample success responses `XML` format rations Center

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>20</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <AlarmId>4008888</AlarmId>
        <UserName>Organization A</UserName>
        <AlarmType>Suspicious process</AlarmType>
        <SourceFrom>20</SourceFrom>
        <AssetName>zzzz_88****</AssetName>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <AlarmName>Reverse**</AlarmName>
        <UserId>295614088</UserId>
        <AlarmUniqueInfo>eeee98dd0c4cd5cc61c016b2bdcf****</AlarmUniqueInfo>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <RaisedTime>1640931449000</RaisedTime>
        <RiskLevel>2</RiskLevel>
        <Detail>{"lastTime": 1641536460051,"assetsType": 0,"modifiedTime": "2022-01-07
14:21:00"}</Detail>
        <LastTime>1641537619</LastTime>
    </Items>
</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"20","Total":"200","PageNo":"1","Items": [{"AlarmId":"4008888","UserName":"Organization A","AlarmType":"Suspicious process","SourceFrom":"20","AssetName":"zzzz_88****","AssetPrivateIps":"192.168.XX.XX","P cessState":"1","AssetType":"ECS","AlarmName":"Reverse**","UserId":"295614088","AlarmUniqu nfo":"eeee98dd0c4cd5cc61c016b2bdcf****","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef 8888-4aee-8bac-19879e68****","RaisedTime":"1640931449000","RiskLevel":"2","Detail":"{\" lastTime\": 1641536460051,\"assetsType\": 0,\"modifiedTime\": \"2022-01-07 14:21:00\"}","LastTime":"1641537619"}]}}
```

#### 4.2.3 DescribeVulFrangs

Queries vulnerabilities based on specified conditions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulFran gs | The operation that you want to perform. Set the value to DescribeVulFrangs. |

rations Center

| RiskLevel | Integer | No | 1 | The severity of the vulnerability. Valid values: 0: low 1: medium 2: high |
|---|---|---|---|---|
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| VulType | String | No | cve | The type of the vulnerability. Valid values: cve, sys, sca, and emg. |
| PocFlag | Integer | No | 1 | Specifies whether to query data related to Proof of Concept (POC). Valid values: 0: no 1: yes |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: Valid values: 0: platform 1: user |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| UsageLevel | String | No | LOW | The exploitability of the vulnerability. Valid values include LOW, HIGH, MEDIUM, INSUFFICIENT INFO, and _ NONE. |
| StartTime | Long | No | 1641484800000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | 1643644800000 | The end of the time range to query. Unit: milliseconds. |
| Page | Integer | No | 1 | The number of the page to return. |
| NeedFix | String | No | necessity | The priority to fix the vulnerability. |

rations Center

| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify a vulnerability name, an asset name, or the IP address of an asset. |
|---|---|---|---|---|
| SourceFrom | Integer | No | 1 | The source of data. Valid values: 1: host vulnerabilities detected by Server Guard |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset affected by the vulnerability. |
| AssetType | String | No | ECS | The type of the asset affected by the vulnerability. Valid values include ECS, SLB, OSS, EIP, and RDS. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The data that is returned. |
| Items | Array of Item |   | The list of the returned data. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset affected by the vulnerability. |
| AssetName | String | zzz 75**** _ | The name of the asset affected by the vulnerability. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the asset affected by the vulnerability. |
| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the asset affected by the vulnerability. |
| AssetType | String | ECS | The type of the asset affected by the vulnerability. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Id | Long | 75489 | The ID of the data. |
| LastTime | String | 1642025151000 | The time when the vulnerability was last detected. Unit: milliseconds. |

rations Center

| NeedFix | String | necessity | The priority to fix the vulnerability. |
|---|---|---|---|
| ProcessState | Integer | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| RaisedTime | Integer | 2022 | The time of occurrence. The time follows the yyyy format. |
| RiskLevel | Integer | 1 | The severity of the vulnerability. Valid values: 0: low 1: medium 2: high |
| SourceFrom | Integer | 1 | The source of data. Valid values: 1: host vulnerabilities detected by Server Guard |
| SrcInnerName | String | oval:com.redhat.rh sa:def:2021**** | The name of the vulnerability. |
| UsageLevel | String | LOW | The exploitability of the vulnerability. Valid values include LOW, HIGH, MEDIUM, INSUFFICIENT INFO, and NONE. _ |
| UserName | String | Organization A | The name of the organization. |
| VulName | String | RHSA-2021:1180- Mode**** | The name of the vulnerability. |
| VulRelated | String | CVE-2017-100**** | The ID of the associated vulnerability. |
| VulType | String | cve | The type of the vulnerability. Valid values: cve, sys, sca, and emg. |
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

rations Center

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <NeedFix>necessity</NeedFix>
        <UserName>Organization A</UserName>
        <SourceFrom>1</SourceFrom>
        <VulName>RHSA-2021:1180-Mode****</VulName>
        <AssetName>zzz_75****</AssetName>
        <UsageLevel>LOW</UsageLevel>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>1</ProcessState>
        <AssetType>ECS</AssetType>
        <SrcInnerName>oval:com.redhat.rhsa:def:2021****</SrcInnerName>
        <VulRelated>CVE-2017-100****</VulRelated>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>75489</Id>
        <RaisedTime>2022</RaisedTime>
        <RiskLevel>1</RiskLevel>
        <LastTime>1642025151000</LastTime>
        <VulType>cve</VulType>
    </Items>
</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items": [{"NeedFix":"necessity","UserName":"Organization A","SourceFrom":"1","VulName":"RHSA-20 21:1180- Mode****","AssetName":"zzz_75****","UsageLevel":"LOW","AssetPrivateIps":"192.168.XX.XX"," ocessState":"1","AssetType":"ECS","SrcInnerName":"oval:com.redhat.rhsa:def:2021****","Vul lated":"CVE-2017-100****","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6ef-8888-4aee-8 bac- 19879e68****","Id":"75489","RaisedTime":"2022","RiskLevel":"1","LastTime":"1642025151000" VulType":"cve"}]}}
```

rations Center

#### 4.2.4 DescribeHcFrangs

Queries the risks in the host configurations on the user side.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeHcFran gs | The operation that you want to perform. Set the value to DescribeHcFrangs. |
| RiskLevel | Integer | No | 1 | The level of the risk. Valid values: 0: low 1: medium 2: high |
| ProcessState | Integer | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| HcType | String | No | Alibaba Cloud Standard - Windows 2016/2019 Security Baseline | The type of the risk in host configurations. Valid values: Alibaba Cloud Standard - Windows 2016/2019 Security Baseline, Alibaba Cloud Standard - Apache Tomcat Security Baseline, and Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| StartTime | Long | No | 1641484800000 | The beginning of the time range to query. Unit: milliseconds. |
| EndTime | Long | No | 1643731200000 | The end of the time range to query. Unit: milliseconds. |
| Page | Integer | No | 1 | The number of the page to return. |

rations Center

| Keyword | String | No | 192.168.XX.XX | The keyword to match. You can specify an asset name or the IP address of an asset. |
|---|---|---|---|---|
| DataScope | Integer | No | 1 | Specifies whether to query the data on the user side or the platform side. Valid values: 0: platform 1: user |
| UserId | Long | No | 2956140888888 888 | The ID of the organization. |
| SourceFrom | Integer | No | 2 | The source of data. Valid values: 2: host configuration check |
| Asset | String | No | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| AssetType | String | No | ECS | The type of the asset. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The data that is returned. |
| Items | Array of Item |   | The list of the returned data. |
| Asset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset that is affected by the risk. |
| AssetName | String | zz 78**** _ | The name of the asset that is affected by the risk. |
| AssetPrivateIp s | String | 192.168.XX.XX | The private IP address of the asset that is affected by the risk. |

rations Center

| AssetPublicIps | String | 172.12.XX.XX | The public IP address of the asset that is affected by the risk. |
|---|---|---|---|
| AssetType | String | ECS | The type of the asset that is affected by the risk. Valid values include ECS, SLB, OSS, EIP, and RDS. |
| HcAsset | String | ae3ef6ef-8888- 4aee-8bac- 19879e68**** | The ID of the asset. |
| HcName | String | CIS Standard*** | The name of the host configuration risk. |
| HcType | String | Alibaba Cloud Standard - Windows 2016/2019 Security Baseline | The type of the risk in host configurations. Valid values: Alibaba Cloud Standard - Windows 2016/2019 Security Baseline, Alibaba Cloud Standard - Apache Tomcat Security Baseline, and Alibaba Cloud Standard - CentOS Linux 7/8 Security Baseline Check. |
| Id | Long | 65357 | The ID of the record. |
| LastFoundTim e | String | 1642042910000 | The time when the risk was last detected. Unit: milliseconds. |
| ProcessState | Integer | 2 | The handling status of the risk. Valid values: 1: handled 2: unhandled |
| RiskLevel | Integer | 1 | The level of the risk. Valid values: 0: low 1: medium 2: high |
| SourceFrom | String | 2 | The source of data. Valid values: 2: host configuration check |
| UserId | Long | 295614088888888 8 | The ID of the organization. |

rations Center

| UserName | String | Organization A | The name of the organization. |
|---|---|---|---|
| PageNo | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| Total | Integer | 200 | The total number of entries returned. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://yundunnewsoc-pop.[RegionId].example.com/?Action=DescribeVulFrangs &DataScope=1 &PageSize=20 &Page=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>
    <PageSize>10</PageSize>
    <Total>200</Total>
    <PageNo>1</PageNo>
    <Items>
        <UserName>Organization A</UserName>
        <SourceFrom>2</SourceFrom>
        <HcType>Alibaba Cloud Standard - Windows 2016/2019 Security Baseline</HcType>
        <AssetName>zz_78****</AssetName>
        <HcAsset>ae3ef6ef-8888-4aee-8bac-19879e68****</HcAsset>
        <AssetPrivateIps>192.168.XX.XX</AssetPrivateIps>
        <ProcessState>2</ProcessState>
        <LastFoundTime>1642042910000</LastFoundTime>
        <AssetType>ECS</AssetType>
        <HcName>CIS standard***</HcName>
        <UserId>2956140888888888</UserId>
        <AssetPublicIps>172.12.XX.XX</AssetPublicIps>
        <Asset>ae3ef6ef-8888-4aee-8bac-19879e68****</Asset>
        <Id>65357</Id>
        <RiskLevel>1</RiskLevel>
    </Items>
</Data>
```

`JSON` format rations Center

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data": {"PageSize":"10","Total":"200","PageNo":"1","Items":[{"UserName":"Organization A","Sour ceFrom":"2","HcType":"Alibaba Cloud Standard - Windows 2016/2019 Security Baseline","AssetName":"zz_78****","HcAsset":"ae3ef6ef-8888-4aee-8bac- 19879e68****","AssetPrivateIps":"192.168.XX.XX","ProcessState":"2","LastFoundTime":"16420 910000","AssetType":"ECS","HcName":"CIS standard***","UserId":"2956140888888888","AssetPublicIps":"172.12.XX.XX","Asset":"ae3ef6e 8888-4aee-8bac-19879e68****","Id":"65357","RiskLevel":"1"}]}}
```

### 4.3 Operations Center

#### 4.3.1 QueryThreats

Queries attack data in the Operations Center dashboard.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreats | The operation that you want to perform. Set the value to QueryThreats. |
| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |
| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Aliuid | Long | No | 1 | This parameter is deprecated. |

rations Center

| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |
|---|---|---|---|---|
| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |
| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |
| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |

rations Center

| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |
|---|---|---|---|---|
| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| Tag | String | No | 121 | The tag. |
| DestinationIp | String | No | 192.168.XX.XX | The attacked IP address. |
| ThreatSourceIp | String | No | 172.12.XX.XX | The source IP address of the attack. |
| UrlHost | String | No | www.ecs****.co m | The website. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| Datas | List | {"lastTime":16415 49724000," logTi __ me":16415497242 87,"process way":" _ "} | The list of data records that are queried from Elasticsearch. Each array in the list represents a data record. |
| FromTime | Long | 1641484800000 | The start time of the attack. Unit: milliseconds. |
| HistogramInter val | Long | 0 | The interval of the histogram. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

rations Center

| ToTime | Long | 1641550177290 | The end time of the attack. Unit: milliseconds. |
|---|---|---|---|
| Total | Integer | 200 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=QueryThreats &CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<ToTime>1641550177290</ToTime> <PageSize>10</PageSize> <RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <HistogramInterval>0</HistogramInterval> <CurrentPage>1</CurrentPage> <Datas>{"lastTime":1641549724000,"__logTime":1641549724287,"process_way":""}</Datas> <Total>200</Total> <FromTime>1641484800000</FromTime>
```

`JSON` format

```json
{"ToTime":"1641550177290","PageSize":"10","RequestId":"8010791A-3154-4154-ACB2-866E56A6
****","HistogramInterval":"0","CurrentPage":"1","Datas":"
{\"lastTime\":1641549724000,\"__logTime\":1641549724287,\"process_way\":\"\"}","Total":"2 ","FromTime":"1641484800000"}
```

#### 4.3.2 QueryThreatChartData

Queries the data in a chart of the Operations Center dashboard.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | QueryThreatCha rtData | The operation that you want to perform. Set the value to QueryThreatChartData. |

rations Center

| FromTime | Long | No | 1640944798076 | The beginning of the time range to query. Unit: milliseconds. |
|---|---|---|---|---|
| ToTime | Long | No | 1641549603697 | The end of the time range to query. Unit: milliseconds. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| Index | String | No | threat | The data index. Set the value to threat. |
| Aliuid | Long | No | 1 | This parameter is deprecated. |
| UserIds | String | No | - 1,29561408888 8**** | The ID of the department. You can specify -1 or the ID of a tenant organization. The value -1 specifies that data on the platform side is queried. Separate multiple values with commas (,). |
| Query | String | No | 192.168.XX.XX | The keyword to match. You can specify the IP address of an alerting asset or the IP address in an attack. |
| ProcessStatus | String | No | 1 | The handling status. Valid values: 1: unhandled 2: handled |
| ThreatLevel | String | No | 1 | The risk level of the attack. Valid values: 1: low 2: medium 3: high |

rations Center

| SrcFrom | String | No | 20,40 | The source of data. Separate multiple values with commas (,). Valid values: 20: Server Guard 40: Web Application Firewall (WAF) 41: Cloud Firewall 44: Network Detection and Response (NDR) |
|---|---|---|---|---|
| ThreatType | String | No | Suspicious process | The type of the alert that is generated for the attack. Valid values include Non-web attack, Precise defense, Web attack, Other, and Suspicious process. |
| ThreatName | String | No | Suspicious encoded command | The name of the attack. |
| ProcessWay | String | No | 1 | The handling method. Valid values: 0: allow 1: intercept 2: ignore 3: manually handle 4: batch block 5: automatically handle 6: alert 7: discard 8: block |
| ThreatInoutside | String | No | 1 | The source of the attack. Valid values: 1: internal attack 2: external attack |
| ThreatResult | String | No | Success | The result of the attack. Valid values include Attempt, Success, and Failure. |
| Properties | String | No | {"x type":"term" _ ,"y config 1":"sr _ _ c from,count"} _ | The settings that are used to query the chart. Specify the value in the following JSON format: {"x type":"term"(X- _ axis),"y config 1":"src from(Y- _ _ _ axis),count(Count)"}. |

rations Center

| ChartType | String | No | pie | The type of the chart. Valid values include histogram, bar, line, pie, table, and value. |
|---|---|---|---|---|
| Lang | String | No | zh CN _ | The language of the content within the request and response. Valid values: zh CN: Simplified Chinese _ zh TW: Traditional Chinese _ en US: English _ |
| Tag | String | No | tem | The tag. |
| Size | String | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | List | {"20": {"src from,count":" _ 23507"}} | The list of data records that are queried from Elasticsearch. Each array in the list represents a data record. |
| RequestId | String | 8010791A-3154- 4154-ACB2- 866E56A6**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=QueryThreatChartData &CurrentPage=1 &PageSize=10 &FromTime=1641484800000 &ToTime=1641550177290 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>8010791A-3154-4154-ACB2-866E56A6****</RequestId> <Data>{"20":{"src_from,count":"23507"}}</Data>
```

`JSON` format

```json
{"RequestId":"8010791A-3154-4154-ACB2-866E56A6****","Data":"{\"20\": {\"src_from,count\":\"23507\"}}"}
```

## 5 APIs

### 5.1 CreateEventType

Creates an audit event type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateEventTyp e | The operation that you want to perform. Set the value to CreateEventType. |
| LogType | Integer | Yes | 5 | The type of the log. |
| Name | String | Yes | High-risk query | The name of the audit event type. |
| Remark | String | Yes | High-risk database query | The description of the audit event type. |
| SourceId | Long | Yes | 10000 | The ID of the log source. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EventType | Struct |   | The audit event type that is created. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Id | Integer | 10135 | The ID of the audit event type. |
| LogType | Integer | 1 | The type of the log. |
| Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The description of the audit event type. |

| Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |
|---|---|---|---|
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateEventType &LogType=5 &Name=High-risk query &Remark=High-risk database query &SourceId=10000 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****","EventType": {"CreateTime":"1639236844747","SourceId":"1000","LogType":"1","SourceName":"rds-ss12222 ","Id":"10135","Remark":"EVENT_TYPE_NAME__host__account_create","Name":"EVENT_TYPE_NAME__ st__account_create","Reserved":"true"}}
```

### 5.2 DescribeEventType

Queries audit event types.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventTy pe | The operation that you want to perform. Set the value to DescribeEventType |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| SourceId | Long | No | 1000 | The ID of the log source. |

| LogType | Integer | No | 1 | The type of the log. |
|---|---|---|---|---|
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| EventTypeList | Array of EventType |   | The list of audit event types. |
| Code | String | account create _ | The code of the audit event type. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Id | Integer | 10135 | The ID of the audit event type. |
| LogType | Integer | 1 | The type of the log. |
| Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| Remark | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The description of the audit event type. |
| Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

| TotalCount | Integer | 100 | The total number of entries returned. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventType &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"TotalCount":"100","PageSize":"20","RequestId":"7E0618A9-D5EF-4220-9471- C42B5E92****","CurrentPage":"1","EventTypeList": [{"CreateTime":"1639236844747","SourceId":"1000","LogType":"1","SourceName":"rds-ss1222 2","Id":"10135","Code":"account_create","Remark":"EVENT_TYPE_NAME__host__account_create", ame":"EVENT_TYPE_NAME__host__account_create","Reserved":"true"}]}
```

### 5.3 DeleteEventType

Deletes an audit event type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteEventTyp e | The operation that you want to perform. Set the value to DeleteEventType. |
| Id | Integer | Yes | 10135 | The ID of the audit event type. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteEventType &Id=10135 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"}
```

### 5.4 CreateLogFilter

Creates a filter condition to query audit logs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateLogFilter | The operation that you want to perform. Set the value to CreateLogFilter. |
| LogType | Integer | Yes | 1 | The type of the log. |
| Name | String | Yes | RDS-scscsc | The name of the filter condition. |
| Type | Integer | Yes | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 specifies a filter condition for logs, and the value 2 specifies a filter condition for audit events. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| SourceId | Long | No | 1000 | The ID of the log source. |
| Defaultable | Boolean | No | true | Specifies whether to use the filter condition as the default filter condition. Valid values: True and False. |
| EventRiskLevel | Integer | No | 1 | The level of the risk. |
| EventType | Integer | No | 1 | The type of the audit event. |

| Alertable | Boolean | No | true | Specifies whether an alert is triggered. Valid values: True and False. |
|---|---|---|---|---|
| Query | String | No | Get | The keyword for the query. |
| StartTime | Long | No | 1519813584985 | The beginning of the time range to query. This value is a timestamp. |
| EndTime | Long | No | 1519813584985 | The end of the time range to query. This value is a timestamp. |
| LogInitiatior | String | No | EQ:Initiator | The initiator. |
| LogTarget | String | No | EQ:target | The target. |
| LogAction | String | No | EQ:cmd | The operation. |
| LogOutcome | String | No | EQ:result | The result. |
| LogReason | String | No | EQ:reason | The reason. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogFilter | Struct |   | The filter condition that is created. For more information, see the following parameter descriptions. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Defaultable | Boolean | true | Indicates whether the filter condition is used as the default filter condition. Valid values: True and False. |
| EventType | Integer | 1 | The type of the audit event. |
| Id | Integer | 1000 | The ID of the filter condition. |
| LogType | Integer | 1 | The type of the log. |

| Name | String | RDS-scscsc | The name of the filter condition. |
|---|---|---|---|
| SourceId | Long | 1000 | The ID of the log source. |
| Type | Integer | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 indicates a filter condition for logs, and the value 2 indicates a filter condition for audit events. |
| UserId | String | 1000 | The ID of the creator. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateLogFilter &LogType=1 &Name=RDS-scscsc &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****","LogFilter": {"Type":"1","EventType":"1","UserId":"1000","CreateTime":"1639236844747","SourceId":"1000 "LogType":"1","Id":"1000","Name":"RDS-scscsc","Defaultable":"true"}}
```

### 5.5 DescribeLogFilter

Queries filter conditions for audit logs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLogFilte r | The operation that you want to perform. Set the value to DescribeLogFilter. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

| LogType | String | No | 1 | The type of the log. |
|---|---|---|---|---|
| SourceId | Long | No | 1001 | The ID of the log source. |
| Count | Integer | No | 1001 | The number of entries to return. |
| Type | String | No | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 specifies a filter condition for logs, and the value 2 specifies a filter condition for audit events. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogFilterList | Array of LogFilter |   | An array that consists of filter conditions. |
| Alertable | Boolean | true | Indicates whether an alert is triggered. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Defaultable | Boolean | true | Indicates whether the filter condition is used as the default filter condition. Valid values: True and False. |
| EndTime | Long | 1519813584985 | The end time of the query. This value is a timestamp. |
| EventRiskLeve l | Integer | 1 | The level of the risk. |
| EventType | Integer | 1 | The type of the audit event. |
| Id | Integer | 1000 | The ID of the filter condition. |
| LogAction | String | EQ:cmd | The operation. |
| LogInitiatior | String | EQ:Initiator | The initiator. |
| LogOutcome | String | EQ:result | The result. |
| LogReason | String | EQ:reason | The reason. |

| LogTarget | String | EQ:target | The target. |
|---|---|---|---|
| LogType | Integer | 1 | The type of the log. |
| Name | String | RDS-scscsc | The name of the filter condition. |
| Query | String | Get | The keyword for the query. |
| SourceId | Long | 1000 | The ID of the log source. |
| StartTime | Long | 1519813584985 | The start time of the query. This value is a timestamp. |
| Type | Integer | 1 | The type of the filter condition. Valid values: 1 and 2. The value 1 indicates a filter condition for logs, and the value 2 indicates a filter condition for audit events. |
| UserId | String | 100000 | The ID of the creator. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogFilter &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****","LogFilterList": [{"Query":"Get","EndTime":"1519813584985","EventType":"1","CreateTime":"1639236844747","S rceId":"1000","StartTime":"1519813584985","LogType":"1","EventRiskLevel":"1","LogTarget": Q:target","Name":"RDSscscsc","Type":"1","LogAction":"EQ:cmd","LogInitiatior":"EQ:Initiator","UserId":"100000", ogReason":"EQ:reason","LogOutcome":"EQ:result","Alertable":"true","Id":"1000","Defaultabl :"true"}]}
```

### 5.6 DeleteLogFilter

Deletes a filter condition for audit logs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteLogFilter | The operation that you want to perform. Set the value to DeleteLogFilter. |
| Id | Integer | Yes | 1000 | The ID of the filter condition. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteLogFilter &Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.7 CreateReceiver

Creates an alert recipient for audit events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateReceiver | The operation that you want to perform. Set the value to CreateReceiver. |
| Contact | String | Yes | *****@aliyun.co m | The contact information about the alert recipient. |

| EventRiskLevel | Integer | Yes | 1 | The level of the risk. |
|---|---|---|---|---|
| Name | String | Yes | Jack | The name of the alert recipient. |
| Type | Integer | Yes | 1 | The alert receiving method. Set the value to 1. The value 1 specifies that alerts are sent through emails. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integer | No | 1 | The code of the log type. |
| SourceId | Long | No | 1000 | The ID of the log source. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Receiver | Struct |   | The created alert recipient. For more information, see the following parameter descriptions. |
| Contact | String | *****@aliyun.com | The contact information about the alert recipient. |
| CreateTime | Long | 1639236844747 | The creation time. |
| EventRiskLeve l | Integer | 1 | The level of the risk. |
| Id | Integer | 10001 | The ID of the alert recipient. |
| LogType | Integer | 1 | The code of the log type. |
| Name | String | Jack | The name of the alert recipient. |
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |

| Type | Integer | 1 | The alert receiving method. The value is fixed as 1. The value 1 indicates that alerts are sent through emails. |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateReceiver &Contact=*****@aliyun.com &EventRiskLevel=1 &Name=Jack &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.8 DescribeReceiver

Queries information about alert recipients.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeReceive r | The operation that you want to perform. Set the value to DescribeReceiver. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | String | No | 1 | The code of the log type. |
| SourceId | Long | No | 1000 | The ID of the log source. |
| EventRiskLevel | String | No | 1 | The level of the risk. |
| Contact | String | No | 1***@qq.com | The contact information about the alert recipient. |

| Name | String | No | Jack | The name of the alert recipient. |
|---|---|---|---|---|
| SourceName | String | No | rds-ss12222 | The name of the log source. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| ReceiverList | Array of Receiver |   | An array that consists of alert recipients. |
| Contact | String | *****@aliyun.com | The contact information about the alert recipient. |
| CreateTime | Long | 1639236844747 | The creation time. |
| EventRiskLeve l | Integer | 1 | The level of the risk. |
| Id | Integer | 10001 | The ID of the alert recipient. |
| LogType | Integer | 1 | The code of the log type. |
| Name | String | Jack | The name of the alert recipient. |
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |
| Type | Integer | 1 | The alert receiving method. The value is fixed as 1. The value 1 indicates that alerts are sent through emails. |

| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeReceiver &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.9 DeleteReceiver

Deletes an alert recipient for audit events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteReceiver | The operation that you want to perform. Set the value to DeleteReceiver. |
| Id | Integer | Yes | 1000 | The ID of the alert recipient. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteReceiver &Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.10 CreateRule

Creates an audit rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateRule | The operation that you want to perform. Set the value to CreateRule. |
| Alertable | Boolean | Yes | true | Specifies whether an alert is triggered. |
| EventRiskLevel | Integer | Yes | 1 | The level of the risk. |
| EventTypeId | Integer | Yes | 10001 | The type of the audit event. |
| LogType | Integer | Yes | 1 | The code of the log type. |
| RuleName | String | Yes | High-risk deletion operation | The name of the audit rule. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| SourceId | Long | No | 1000 | The ID of the log source. |
| Expression | String | No | action INCLUDE \"Delete instance\" OR action INCLUDE \"Delete cluster\" OR action INCLUDE \"Delete host\" | The expression in the audit rule. |
| Remark | String | No | remark | The remarks. |

| StartTime | String | No | 1640442436125 | The start time. This value is a timestamp. |
|---|---|---|---|---|
| EndTime | String | No | 1640442436125 | The end time. This value is a timestamp. |
| AlertActionList | String | No | 1 | The alert recipient in the rule. Separate multiple alert recipients with commas (,). |
| LogInitiatior | String | No | EQ:Initiator | The initiator. |
| LogTarget | String | No | EQ:target | The target. |
| LogAction | String | No | EQ:cmd | The audit object. |
| LogOutcome | String | No | EQ:result | The result. |
| LogReason | String | No | EQ:reason | The reason. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| Rule | Struct |   | The created audit rule. For more information, see the following parameter descriptions. |
| AlertActions | String | 1 | The alert recipient in the rule. |
| Alertable | Boolean | true | Indicates whether an alert is triggered. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Enabled | Boolean | true | Indicates whether the rule is enabled. |
| EventRiskLeve l | Integer | 1 | The level of the risk. |

| EventTypeId | Integer | 10001 | The type of the audit event. |
|---|---|---|---|
| EventTypeNa me | String | Resource Management event | The name of the event type. |
| Id | Integer | 1000 | The ID of the audit rule. |
| LogType | Integer | 1 | The code of the log type. |
| Name | String | High-risk deletion operation | The name of the audit rule. |
| Reserved | Boolean | false | Indicates whether the audit rule is reserved. |
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateRule &Alertable=true &EventRiskLevel=1 &EventTypeId=10001 &LogType=1 &RuleName=High-risk deletion operation &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****","Rule": {"CreateTime":"1639236844747","SourceId":"1000","LogType":"1","SourceName":"rds-ss12222 ","EventTypeName":"Resource Management event","EventTypeId":"10001","Enabled":"true","AlertActions":"1","Id":"1000","Alertable": rue","EventRiskLevel":"1","Name":"High-risk deletion operation,"Reserved":"false"}}
```

### 5.11 DescribeRule

Queries audit rules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRule | The operation that you want to perform. Set the value to DescribeRule. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integer | No | 1 | The code of the log type. |
| SourceId | Long | No | 1000 | The ID of the log source. |
| EventTypeId | Long | No | 10001 | The type of the audit event. |
| Expression | String | No | action INCLUDE \"Delete instance\" OR action INCLUDE \"Delete cluster\" OR action INCLUDE \"Delete host\" | The expression in the audit rule. |
| EventRiskLevel | Integer | No | 1 | The level of the risk. |
| Alertable | Boolean | No | true | Specifies whether an alert is triggered. |
| Enabled | Boolean | No | true | Specifies whether the rule is enabled. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |

| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
|---|---|---|---|
| RuleList | Array of Rule |   | An array that consists of audit rules. |
| AlertActions | String | 1 | The alert recipient in the rule. |
| Alertable | Boolean | true | Indicates whether an alert is triggered. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Enabled | Boolean | true | Indicates whether the rule is enabled. |
| EventRiskLeve l | Integer | 1 | The level of the risk. |
| EventTypeId | Integer | 10001 | The type of the audit event. |
| EventTypeNa me | String | Resource Management event | The name of the event type. |
| Expression | String | action INCLUDE \"Delete instance\" OR action INCLUDE \"Delete cluster\" OR action INCLUDE \"Delete host\" | The expression in the audit rule. |
| Id | Integer | 1000 | The ID of the audit rule. |
| LogType | Integer | 1 | The code of the log type. |
| Name | String | High-risk deletion operation | The name of the audit rule. |
| Reserved | Boolean | true | Indicates whether the audit rule is reserved. |
| SourceName | String | rds-ss12222 | The name of the log source. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRule &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"TotalCount":"100","RuleList":[{"Expression":"action INCLUDE \\\"Delete instance\\\" O R action INCLUDE \\\"Delete cluster\\\" OR action INCLUDE \\\"Delete host\\\"","CreateTime":"1639236844747","LogType":"1","SourceName":"rdsss12222","Enabled":"true","EventTypeName":"Resource Management event","EventTypeId":"10001","AlertActions":"1","Alertable":"true","Id":"1000","EventRisk vel":"1","Name":"High-risk deletion operation","Reserved":"true"}],"PageSize":"20","RequestId":"7E0618A9-D5EF-4220-9471-C42 B5E92****","CurrentPage":"1"}
```

### 5.12 EnableRule

Enables an audit rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | EnableRule | The operation that you want to perform. Set the value to EnableRule. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
| Id | Integer | No | 1 | The ID of the audit rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=EnableRule &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.13 DisableRule

Disables an audit rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DisableRule | The operation that you want to perform. Set the value to DisableRule. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
| Id | Integer | No | 1 | The ID of the audit rule. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DisableRule &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.14 DeleteRule

Deletes an audit rule.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DeleteRule | The operation that you want to perform. Set the value to DeleteRule. |
|---|---|---|---|---|
| Id | Integer | Yes | 1000 | The ID of the audit rule. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteRule &Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.15 CreateTask

Creates an export task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | CreateTask | The operation that you want to perform. Set the value to CreateTask. |
| Param | String | Yes | {\"id\":421711} | The query parameters in the JSON format. |
| Type | Integer | Yes | 1 | The type of the export task. |

| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| Task | Struct |   | The created export task. For more information, see the following parameter descriptions. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Id | Integer | 1000 | The ID of the export task. |
| Param | String | {\"id\":421711} | The query parameters in the JSON format. |
| Result | String | {\"url\":\"https://yu ndun-auditlog- archive.oss- ***.aliyun.com/OPS /20211224151432 914- e902e5b4/EVENT/O PS-******.zip?} | The result of the export task. |
| Status | Integer | 3 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 indicates that the task is being prepared. The value 2 indicates that the task is in progress. The value 3 indicates that the task is successful. The value 4 indicates that the task failed. |
| Type | Integer | 1 | The type of the export task. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=CreateTask &Param={\"id\":421711} &Type=1 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.16 DescribeTask

Queries information about export tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeTask | The operation that you want to perform. Set the value to DescribeTask. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
| Type | Integer | No | 1 | The type of the export task. |
| Status | Integer | No | 1 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 specifies that the task is being prepared. The value 2 specifies that the task is in progress. The value 3 specifies that the task is successful. The value 4 specifies that the task failed. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

| TaskList | Array of Task |   | An array that consists of information about export tasks. |
|---|---|---|---|
| CreateTime | Long | 1639236844747 | The creation time. |
| EndTime | Long | 1639236844747 | The end time of the task. This value is a timestamp. |
| Id | Integer | 1000 | The ID of the export task. |
| Param | String | {\"id\":421711} | The query parameters in the JSON format. |
| Result | String | {\"url\":\"https://yu ndun-auditlog- archive.oss-cn- neimeng-env30- d01- a.intra.env30.shug uang.com/OPS/202 11224151432914- e902e5b4/EVENT/O PS- 20211224151432.z ip?} | The result of the export task. |
| StartTime | Long | 1639236844747 | The start time of the task. This value is a timestamp. |
| Status | Integer | 1 | The status of the task. Valid values: 1, 2, 3, and 4. The value 1 indicates that the task is being prepared. The value 2 indicates that the task is in progress. The value 3 indicates that the task is successful. The value 4 indicates that the task failed. |
| Type | Integer | 1 | The type of the export task. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeTask &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.17 DeleteTask

Deletes an export task.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DeleteTask | The operation that you want to perform. Set the value to DeleteTask. |
| Id | Integer | Yes | 1000 | The ID of the export task. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DeleteTask &Id=1000 &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.18 DescribeSetting

Queries the system parameter settings of security audit.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeSetting | The operation that you want to perform. Set the value to DescribeSetting. |
|---|---|---|---|---|
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| SettingList | Array of Setting |   | An array that consists of system parameter settings. |
| Id | Integer | 1 | The ID of the system parameter. |
| Name | String | max day alert nu _ _ _ mber | The name of the system parameter. |
| Remark | String | Maximum number of alerts sent per day | The description of the system parameter. |
| Type | Integer | 2 | The type of data. |
| UpdateTime | Long | 1639236844747 | The time at which the system parameter was last modified. |
| Value | String | -1 | The value of the system parameter. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSetting &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"SettingList":[{"Type":"2","Value":"- 1","UpdateTime":"1639236844747","Id":"1","Remark":"Maximum number of alerts sent per da y","Name":"max_day_alert_number"}],"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****"}
```

### 5.19 ModifySetting

Modifies the system parameter settings of security audit.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | ModifySetting | The operation that you want to perform. Set the value to ModifySetting. |
| Name | String | Yes | max day alert n _ _ _ umber | The name of the system parameter. |
| Value | String | Yes | -1 | The value of the system parameter. |
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=ModifySetting &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.20 DescribeLogType

Queries log types.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribeLogTyp e | The operation that you want to perform. Set the value to DescribeLogType. |
|---|---|---|---|---|
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| LogTypeList | Array of LogType |   | An array that consists of log types. |
| Remark | String | Platform database | The name of the log type. |
| Type | Integer | 1 | The code of the log type. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogType &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"LogTypeList":[{"Type":"1","Remark":"Platform database"}],"RequestId":"7E0618A9-D5EF-4 220-9471-C42B5E92****"}
```

### 5.21 DescribeLogSource

Queries log source information.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLogSou rce | The operation that you want to perform. Set the value to DescribeLogSource. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

| LogType | Integer | No | 1 | The code of the log type. |
|---|---|---|---|---|
| Enabled | Boolean | No | true | Specifies whether the log source is enabled. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| LogSourceList | Array of LogSource |   | An array that consists of log sources. |
| Alertable | Boolean | true | Indicates whether an alert is triggered. |
| Code | String | RDS-scscsc | The code of the log source. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Enabled | Boolean | true | Indicates whether the log source is enabled. |
| Id | Integer | 1000 | The ID of the log source. |
| LogType | Integer | 1 | The code of the log type. |
| Name | String | RDS-scscsc | The name of the log source. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| TotalCount | Integer | 1000 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogSource &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.22 DescribeLogCountStat

Queries raw log statistics.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLogCou ntStat | The operation that you want to perform. Set the value to DescribeLogCountStat. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| LogTypeList | String | No | 1,2,3,4,5 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | String | No | 1639725751259 | The end of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| StatList | Array of Stat |   | An array that consists of raw log statistics. |
| LogType | Integer | 1 | The code of the log type. |
| StatItemList | Array of StatItem |   | An array that consists of raw log data. |

| Capacity | Float | 1000.0 | The storage usage. |
|---|---|---|---|
| Count | Integer | 1000 | The number of raw logs. |
| Time | Long | 1640244151259 | The time at which the statistics were collected. This value is a timestamp. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLogCountStat &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.23 DescribeLog

Queries the details about raw logs.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeLog | The operation that you want to perform. Set the value to DescribeLog. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integer | No | 1 | The type of the log. |
| SourceId | Long | No | 1001 | The ID of the log source. |
| Query | String | No | Get | The keyword for the query. |
| StartTime | Long | No | 1639236844747 | The beginning of the time range to query. This value is a timestamp. |

| EndTime | Long | No | 1639236844747 | The end of the time range to query. This value is a timestamp. |
|---|---|---|---|---|
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The number of the page to return. |
| HistogramList | Array of Histogram |   | An array that consists of chart information about the number of raw logs. |
| Completed | Boolean | true | Indicates whether all of the raw logs that are generated within the specified time range have been collected. If not, the Count parameter shows an estimated value. |
| Count | Integer | 1000 | The number of raw logs. |
| EndTime | Long | 1639236844747 | The end of the time range. This value is a timestamp. |
| StartTime | Long | 1639236844747 | The beginning of the time range. This value is a timestamp. |
| LogList | Array of Log |   | An array that consists of raw logs. |
| ColumnList | Array of Column |   | An array that consists of log details. |
| Key | String | value | The name of the column. |
| TokenList | Array of Token |   | An array that consists of tokens. |
| Delimit | Boolean | false | Indicates whether the token is a delimiter token. |

| Word | String | 012 | The fixed value of the token. |
|---|---|---|---|
| Value | String | 012 | The value of the column. |
| LogTime | Long | 1640244151259 | The time at which the log was generated. |
| Source | String | 1 | The name of the log source. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeLog &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.24 DescribeEventRisk

Queries the risk level information about audit events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventRi sk | The operation that you want to perform. Set the value to DescribeEventRisk. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| EventRiskList | Array of EventRisk |   | An array that consists of risk level information. |
|---|---|---|---|
| Level | Integer | 0 | The risk level. |
| Name | String | Global risk | The name of the risk level. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRisk &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"RequestId":"7E0618A9-D5EF-4220-9471-C42B5E92****","EventRiskList": [{"Level":"0","Name":"Global risk"}]}
```

### 5.25 DescribeEventRiskStat

Queries audit event statistics by risk level.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventRi skStat | The operation that you want to perform. Set the value to DescribeEventRiskStat. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| LogTypeList | String | No | 1,2,3 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | String | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| StatList | Array of Stat |   | An array that consists of audit event statistics. |
| LogType | Integer | 1 | The type of the log. |
| StatItemList | Array of StatItem |   | An array that consists of statistical details. |
| Capacity | Integer | 44 | The storage usage. |
| Count | Integer | 1 | The number of audit events. |
| EventRiskLeve l | Integer | 1 | The risk level. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventRiskStat &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.26 DescribeEventTypeStat

Queries audit event statistics by event type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventTy peStat | The operation that you want to perform. Set the value to DescribeEventTypeStat. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |

| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
|---|---|---|---|---|
| LogTypeList | String | No | 1,2,3,4,5 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | String | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| StatList | Array of Stat |   | An array that consists of audit event statistics. |
| Capacity | Float | 8991.659133 | The storage usage. |
| Count | Integer | 10001 | The number of audit events. |
| Id | Integer | 10135 | The type of the audit event. |
| Name | String | EVENT TYPE NAME _ _ host account cr __ __ _ eate | The name of the audit event type. |
| Reserved | Boolean | true | Indicates whether the event type is reserved in the system. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventTypeStat &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.27 DescribeEventCountStat

Queries audit event statistics.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEventC ountStat | The operation that you want to perform. Set the value to DescribeEventCountStat. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| LogTypeList | String | No | 1,2,3 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | String | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| StatList | Array of Stat |   | An array that consists of audit event statistics. For more information, see the following parameter description. |
| LogType | Integer | 1 | The type of the log. |
| StatItemList | Array of StatItem |   | The audit event statistics. For more information, see the following parameter description. |
| Capacity | Integer | 8991 | The storage usage. |
| Count | Integer | 10001 | The number of audit events. |
| Time | Long | 1639929600000 | The time at which the log was generated. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEventCountStat &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.28 DescribeEvent

Queries audit event details.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeEvent | The operation that you want to perform. Set the value to DescribeEvent. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| lang | String | No | zh | The language of the content within the request and response. Valid values: zh and en. The value zh indicates Chinese, and the value en indicates English. |
| LogType | Integer | No | 1 | The type of the log. |
| SourceId | Long | No | 1000 | The ID of the log source. |
| EventRiskLevel | Integer | No | 1 | The risk level. |
| Alertable | Boolean | No | true | Specifies whether an alert is triggered. |
| EventTypeId | Long | No | 10001 | The type of the audit event. |
| StartTime | Long | No | 1639236844747 | The beginning of the time range to query. This value is a timestamp. |

| EndTime | Long | No | 1639236844747 | The end of the time range to query. This value is a timestamp. |
|---|---|---|---|---|
| Keyword | String | No | Describe | The keyword for the query. |
| RuleId | Long | No | 1000 | The ID of the audit rule. |
| LogInitiatior | String | No | EQ:Initiator | The initiator. |
| LogTarget | String | No | EQ:Target | The target. |
| LogAction | String | No | EQ:cmd | The operation. |
| LogOutcome | String | No | EQ:result | The result. |
| LogReason | String | No | EQ:reason | The reason. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| EventList | Array of Event |   | An array that consists of audit events. |
| CreateTime | Long | 1639236844747 | The creation time. |
| EventRiskLeve l | Integer | 1 | The risk level. |
| EventTypeId | Integer | 1001 | The type of the audit event. |
| EventTypeNa me | String | Resource Management event | The name of the audit event type. |

| EventTypeRes erved | Boolean | true | Indicates whether the event type is reserved in the system. |
|---|---|---|---|
| Id | Long | 1000 | The ID of the audit event. |
| LogAction | String | EQ:cmd | The operation. |
| LogContent | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The content of the log. |
| LogInitiatior | String | EQ:Initiator | The initiator. |
| LogMd5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | The MD5 hash value of the log file. |
| LogOutcome | String | EQ:result | The result. |
| LogReason | String | EQ:reason | The reason. |
| LogSha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The SHA-256 value of the log file. |
| LogTarget | String | EQ:target | The target. |
| LogTime | Long | 1639929600000 | The time at which the log was generated. |
| LogType | Integer | 1 | The type of the log. |
| Receivers | String | 123.qq.com | The alert recipient. |
| RuleId | Integer | 1000 | The ID of the audit rule. |
| SourceId | Long | 1000 | The ID of the log source. |
| SourceName | String | rds-ss12222 | The name of the log source. |
| HistogramList | Array of Histogram |   | An array that consists of chart information about the number of audit events. |

| Completed | Boolean | true | Indicates whether all of the audit events that occurred within the specified time range have been collected. If not, the Count parameter shows an estimated value. |
|---|---|---|---|
| Count | Integer | 1001 | The number of audit events. |
| EndTime | Long | 1639236844747 | The end of the time range. This value is a timestamp. |
| StartTime | Long | 1639236844747 | The beginning of the time range. This value is a timestamp. |
| PageSize | Integer | 20 | The number of entries returned on each page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeEvent &<Common request parameters>
```

Sample success responses `JSON` format

```json
{"TotalCount":"100","HistogramList": [{"EndTime":"1639236844747","Completed":"true","StartTime":"1639236844747","Count":"1001" ,"PageSize":"20","RequestId":"7E0618A9-D5EF-4220-9471- C42B5E92****","CurrentPage":"1","EventList": [{"EventTypeReserved":"true","LogMd5":"36c22c2020d473881f8b8bbf1c3eaf08","RuleId":"1000", eceivers":"123.qq.com","CreateTime":"1639236844747","LogTime":"1639929600000","SourceId": 000","LogType":"1","SourceName":"rdsss12222","EventTypeId":"1001","EventRiskLevel":"1","LogTarget":"EQ:target","LogAction":"E cmd","LogInitiatior":"EQ:Initiator","LogSha256":"929724b41deb5adc78764976f0a397109f2602ba 7dcced2cb26b8d37a97b5d","LogReason":"EQ:reason","LogContent":"929724b41deb5adc78764976f0a 7109f2602ba5c7dcced2cb26b8d37a97b5d","LogOutcome":"EQ:result","EventTypeName":"Resource Management event","Id":"1000"}]}
```

### 5.29 DescribeArchiveCountStat

Queries archived statistics about logs and events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeArchive CountStat | The operation that you want to perform. Set the value to DescribeArchiveCountStat. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| LogTypeList | String | No | 1,2,3 | The type of the log. Separate multiple log types with commas (,). |
| EndTime | String | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| StatList | Array of Stat |   | An array that consists of archived statistics. For more information, see the following parameter description. |
| LogType | Integer | 1 | The type of the log. |
| StatItemList | Array of StatItem |   | The archiving information. For more information, see the following parameter description. |
| Capacity | Float | 6.6 | The storage used for the archives. |
| Count | Integer | 3 | The number of the archives. |
| Time | Long | 1639929600000 | The time at which the statistics were collected. This value is a timestamp. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeArchiveCountStat &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

### 5.30 DescribeArchive

Queries the details of archived logs and events.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeArchive | The operation that you want to perform. Set the value to DescribeArchive. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| LogType | Integer | No | 1 | The type of the log. |
| StartTime | String | No | 1639725751259 | The beginning of the time range to query. This value is a timestamp. |
| EndTime | String | No | 1640244151259 | The end of the time range to query. This value is a timestamp. |
| Type | Integer | No | 1 | The type of the archive. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The page number of the current page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ArchiveList | Array of Archive |   | An array that consists of archived data. For more information, see the following parameter description. |

| loud Security Ma r Developer Guid | nagement Cent e·APIs |   | Alibaba Cloud Security-Situation Awarenes |
|---|---|---|---|

| CompactAlg | Integer | 1 | The compression algorithm. |
|---|---|---|---|
| Count | Integer | 3 | The number of the archives. |
| CreateTime | Long | 1639236844747 | The creation time. |
| Id | Integer | 1000 | The archive ID. |
| LogType | Integer | 1 | The type of the log. |
| Md5 | String | 36c22c2020d4738 81f8b8bbf1c3eaf0 8 | The MD5 hash value of the archive file. |
| Name | String | NETWORK/202112 24153332996- 44a9fc6e/EVENT/N ETWORK- 20211224153332.z ip | The name of the archive file. |
| Sha256 | String | 929724b41deb5ad c78764976f0a3971 09f2602ba5c7dcce d2cb26b8d37a97b 5d | The SHA-256 value of the archive file. |
| Type | Integer | 1 | The type of the archive. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeArchive &<Common request parameters>
```

Sample success responses `JSON` format

```
null
```

## 6 Threat Detection Service (TDS)

**(TDS)**

### 6.1 Asset management

#### 6.1.1 DescribeFieldStatistics

Queries assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeFieldSta tistics | The operation that you want to perform. Set the value to DescribeFieldStatistics. |
| RegionId | String | No | cn-hangzhou | The region ID of the asset. |
| MachineTypes | String | No | ecs | The types of the assets that you want to query. Separate multiple types with commas (,). If no asset types are specified, all types of assets are returned. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | Struct |   | The asset information. |
| AliYunInstance Count | Integer | 10 | The number of instances that are provided by Alibaba Cloud. |

| ExposedInstan ceCount | Integer | 10 | The number of instances that are exposed on the Internet. |
|---|---|---|---|
| GeneralAssetC ount | Integer | 10 | The number of general instances. |
| GroupCount | Integer | 10 | The number of groups. |
| IdcInstanceCo unt | Integer | 10 | The number of servers outside the cloud. |
| ImportantAsse tCount | Integer | 10 | The number of important instances. |
| InstanceCount | Integer | 10 | The number of instances. |
| InstanceSyncT askCount | Integer | 10 | The number of synchronization tasks. |
| NewInstanceC ount | Integer | 10 | The number of new instances. |
| NotRunningSta tusCount | Integer | 10 | The number of servers that are not running. |
| OfflineInstanc eCount | Integer | 10 | The number of offline instances. |
| ProviderCount | Integer | 10 | The number of service providers. |
| RegionCount | Integer | 10 | The number of regions. |
| RiskInstanceC ount | Integer | 10 | The number of vulnerable instances. |
| TencentInstan ceCount | Integer | 10 | The number of instances that are provided by Tencent Cloud. |
| TestAssetCoun t | Integer | 10 | The number of test instances. |
| UnprotectedIn stanceCount | Integer | 10 | The number of unprotected instances. |
| VpcCount | Integer | 10 | The number of virtual private clouds (VPCs). |
| RequestId | String | 7E06****9-D5EF- 4220-9471- ***5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E06****9-D5EF-4220-9471-***5E92719F</RequestId> <GroupedFields>
    <ProviderCount>10</ProviderCount>
    <ExposedInstanceCount>10</ExposedInstanceCount>
    <GroupCount>10</GroupCount>
    <InstanceSyncTaskCount>10</InstanceSyncTaskCount>
    <TencentInstanceCount>10</TencentInstanceCount>
    <RiskInstanceCount>10</RiskInstanceCount>
    <ImportantAssetCount>10</ImportantAssetCount>
    <IdcInstanceCount>10</IdcInstanceCount>
    <GeneralAssetCount>10</GeneralAssetCount>
    <TestAssetCount>10</TestAssetCount>
    <UnprotectedInstanceCount>10</UnprotectedInstanceCount>
    <InstanceCount>10</InstanceCount>
    <OfflineInstanceCount>10</OfflineInstanceCount>
    <VpcCount>10</VpcCount>
    <AliYunInstanceCount>10</AliYunInstanceCount>
    <RegionCount>10</RegionCount>
    <NotRunningStatusCount>10</NotRunningStatusCount>
    <NewInstanceCount>10</NewInstanceCount>
</GroupedFields>
```

`JSON` format `{`

```json
    "RequestId": "7E06****9-D5EF-4220-9471-***5E92719F",
    "GroupedFields": {
        "ProviderCount": 10,
        "ExposedInstanceCount": 10,
        "GroupCount": 10,
        "InstanceSyncTaskCount": 10,
        "TencentInstanceCount": 10,
        "RiskInstanceCount": 10,
        "ImportantAssetCount": 10,
        "IdcInstanceCount": 10,
        "GeneralAssetCount": 10,
        "TestAssetCount": 10,
        "UnprotectedInstanceCount": 10,
        "InstanceCount": 10,
        "OfflineInstanceCount": 10,
        "VpcCount": 10,
        "AliYunInstanceCount": 10,
        "RegionCount": 10,
        "NotRunningStatusCount": 10,
        "NewInstanceCount": 10
```

`}` `}`

#### 6.1.2 DescribeGroupedTags

Queries the statistics of asset tags.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dTags | The operation that you want to perform. Set the value to DescribeGroupedTags. |
| MachineTypes | String | No | 0 | The types of the assets whose tags you want to query. Separate multiple types with commas (,). Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 2 | The number of entries returned on the current page. |
| GroupedFileds | Array of GroupedFiled |   | An array that consists of the statistics of the asset tags. |
| Count | String | 2 | The number of assets to which a tag is attached. |
| Name | String | test | The name of the tag. |
| TagId | Integer | 5 | The ID of the tag. |
| HttpStatusCod e | Integer | 1 | This parameter is deprecated. |
| RequestId | String | 7E0618A9-D5EF- ***-9471- C42B5E92719F | The ID of the request. |
| Success | Boolean | true | This parameter is deprecated. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedTags &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-***-9471-C42B5E92719F</RequestId> <HttpStatusCode>1</HttpStatusCode> <GroupedFileds>
    <TagId>5</TagId>
    <Count>2</Count>
    <Name>test</Name>
</GroupedFileds> <Count>2</Count> <Success>true</Success>
```

`JSON` format `{`

```json
    "RequestId": "7E0618A9-D5EF-***-9471-C42B5E92719F",
    "HttpStatusCode": 1,
    "GroupedFileds": {
        "TagId": 5,
        "Count": 2,
        "Name": "test"
```

`},`

```json
    "Count": 2,
    "Success": true
```

`}`

#### 6.1.3 DescribeAllGroups

Queries the information about server groups.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAllGrou ps | The operation that you want to perform. Set the value to DescribeAllGroups. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The number of entries returned on the current page. |
| Groups | Array of Group |   | An array that consists of the information about server groups. |
| GroupFlag | Integer | 1 | The flag of the server group. Valid values: 0: default group 1: other groups |
| GroupId | Integer | 3 | The ID of the server group. |

| GroupName | String | Group name | The name of the server group. |
|---|---|---|---|
| RequestId | String | 7E0618A9-****- 4220-9471- C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAllGroups &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-****-4220-9471-C42B5E92719F</RequestId> <Groups>
    <GroupName>Group name</GroupName>
    <GroupFlag>1</GroupFlag>
    <GroupId>3</GroupId>
</Groups> <Count>1</Count>
```

`JSON` format `{`

```json
    "RequestId": "7E0618A9-****-4220-9471-C42B5E92719F",
    "Groups": {
        "GroupName": "Group name",
        "GroupFlag": 1,
        "GroupId": 3
```

`},`

```json
    "Count": 1
```

`}`

#### 6.1.4 DescribeInstanceStatistics

Queries the risk information about assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeInstanc eStatistics | The operation that you want to perform. Set the value to DescribeInstanceStatistics. |

| From | String | Yes | sas | The source of data. Set the value to sas. |
|---|---|---|---|---|
| Uuid | String | Yes | a51cec37-ed73- 4c53-b467-*** | The UUIDs of the assets. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Array of Data |   | An array that consists of the risk information about assets. |
| Account | Integer | 1 | The number of logon accounts. |
| AppNum | Integer | 0 | The number of application vulnerabilities. |
| CmsNum | Integer | 2 | The number of Web-CMS vulnerabilities. |
| CveNum | Integer | 1 | The number of Linux software vulnerabilities. |
| EmgNum | Integer | 0 | The number of urgent vulnerabilities. |
| ExposedCount | Integer | 1 | This parameter is deprecated. |
| Health | Integer | 1 | The number of risk items. |
| ScaNum | Integer | 5 | The number of vulnerabilities that are detected based on software component analysis. |
| Suspicious | Integer | 2 | The number of alerts. |

| SysNum | Integer | 1 | The number of Windows system vulnerabilities. |
|---|---|---|---|
| Trojan | Integer | 1 | The number of trojans. |
| Uuid | String | us1233****** | The UUID of the asset. |
| Vul | Integer | 4 | The total number of vulnerabilities. Note Total number of vulnerabilities = CveNum + EmgNum + SysNum + CmsNum + AppNum. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeInstanceStatistics &From=sas &Uuid=a51cec37-ed73-4c53-b467-*** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <Data>
    <Account>1</Account>
    <Uuid>us1233******</Uuid>
    <Suspicious>2</Suspicious>
    <Health>1</Health>
    <CveNum>1</CveNum>
    <ExposedCount>1</ExposedCount>
    <ScaNum>5</ScaNum>
    <CmsNum>2</CmsNum>
    <Trojan>1</Trojan>
    <SysNum>1</SysNum>
    <EmgNum>0</EmgNum>
    <AppNum>0</AppNum>
    <Vul>4</Vul>
</Data>
```

`JSON` format `{`

```json
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "Data": {
        "Account": 1,
        "Uuid": "us1233******",
        "Suspicious": 2,
        "Health": 1,
        "CveNum": 1,
        "ExposedCount": 1,
        "ScaNum": 5,
        "CmsNum": 2,
        "Trojan": 1,
        "SysNum": 1,
        "EmgNum": 0,
        "AppNum": 0,
        "Vul": 4
```

`}` `}`

#### 6.1.5 DescribeCloudProductFieldStatistics

Queries the statistics of cloud services.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudPr oductFieldStatist ics | The operation that you want to perform. Set the value to DescribeCloudProductFieldStatis tics. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| GroupedFields | Struct |   | The statistics of cloud services. |
| CategoryCount | String | [{"MachineType":1 ,"Count":11}] | The statistics on the numbers of assets of different types. MachineType indicates the type of the assets. Count indicates the number of assets that belong to the type. Valid values of MachineType: 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB instance |

| InstanceCount | Integer | 100 | The number of instances. |
|---|---|---|---|
| RiskInstanceC ount | Integer | 90 | The number of vulnerable instances. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudProductFieldStatistics &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId> <GroupedFields>
    <InstanceCount>100</InstanceCount>
    <CategoryCount>[{"MachineType":1,"Count":11}]</CategoryCount>
    <RiskInstanceCount>90</RiskInstanceCount>
</GroupedFields>
```

`JSON` format `{`

```json
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
    "GroupedFields": {
        "InstanceCount": 100,
        "CategoryCount": "[{\"MachineType\":1,\"Count\":11}]",
        "RiskInstanceCount": 90
```

`}` `}`

#### 6.1.6 DescribeCloudCenterInstances

Queries the asset information on the Assets page, such as the name and region of an asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCloudC enterInstances | The operation that you want to perform. Set the value to DescribeCloudCenterInstances. |

| RegionId | String | No | cn-demo-***-*** | The ID of the region. |
|---|---|---|---|---|
| Criteria | String | No | [{\"name\":\"risk Status\",\"value\ ":\"YES\"}, {\"name\":\"inte rnetIp\",\"value\" :\"1.2.3.4\"}] | The search conditions. Note Supported search conditions include the instance ID, instance name, virtual private cloud (VPC) ID, region, and public IP address. You can call the DescribeCriteria operation to query the supported search conditions. Set the value in the following format: [{\"name\":\"Name of condition 1\",\"value\":\"Value of condition 1\"}, {\"name\":\"Name of condition 2\",\"value\":\"Value of condition 2\"},{},...] |
| MachineTypes | String | No | 0 | The type of the asset that you want to query. Valid values: 0: Elastic Compute Service (ECS) instance 1: Server Load Balancer (SLB) instance 2: NAT gateway 3: ApsaraDB RDS database 4: ApsaraDB for MongoDB database 6: container image 7: container |
| LogicalExp | String | No | OR | The logical relationship among multiple search conditions. Valid values: OR: The logical relationship among multiple search conditions is OR. AND: The logical relationship among multiple search conditions is AND. |

| NoPage | Boolean | No | true | Specifies whether to enable paged query. Valid values: true: yes false: no |
|---|---|---|---|---|
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| Importance | Integer | No | 1 | This parameter is deprecated. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Instances | Array of Instance |   | An array that consists of the details of the asset. |
| AlarmStatus | String | NO | Indicates whether alerts are triggered for the asset. Valid values: YES NO |
| AssetType | String | ecs | The type of the asset. |
| AutoSnapshots Level | Integer | 1 | This parameter is deprecated. |
| ClientStatus | String | online | Indicates whether the asset is protected by the agent. Valid values: online: The asset is protected by the agent. offline: The asset is not protected by the agent. pause: The agent suspends protection for the asset. |
| ClientVersion | String | 11 11 _ | The version of the agent. |
| ClusterId | String | 16392368***** | The ID of the cluster. |
| ClusterName | String | demo-cluster | The name of the cluster. |

| CreatedTime | Long | 1609988137000 | The time when the asset was created. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|
| ExposedCount | Integer | 5 | The number of vulnerabilities that are detected on the asset. |
| ExposedStatus | Integer | 0 | Indicates whether the asset is exposed on the Internet. Valid values: 0: no 1: yes |
| Flag | Integer | 1 | This parameter is deprecated. |
| GroupId | String | 3 | The ID of the group. |
| HcStatus | String | NO | Indicates whether baseline risks are detected on the asset. Valid values: YES NO |
| HealthCheckC ount | Integer | 0 | The number of risk items. |
| Importance | Integer | 1 | This parameter is deprecated. |
| InstanceId | String | i-m5*** | The ID of the instance. |
| InstanceName | String | yztest-l*** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The private IP address. |
| Ip | String | 192.168.XX.XX | The IP address that is displayed for the asset. If the asset has a public IP address, the public IP address is returned. Otherwise, the private IP address is returned. |
| Os | String | Linux | The operating system. |
| OsName | String | CentOS 7.6 64-bit | The name of the operating system. |

| PodCount | Integer | 1 | The number of pods. |
|---|---|---|---|
| ProviderAzId | Long | 1 | This parameter is deprecated. |
| ProviderAzNa me | String | None | This parameter is deprecated. |
| ProviderId | Long | 1 | This parameter is deprecated. |
| ProviderName | String | None | This parameter is deprecated. |
| ProviderRegio nId | Long | 1 | This parameter is deprecated. |
| ProviderRegio nName | String | None | This parameter is deprecated. |
| Region | String | cn-demo-***-*** | The region. |
| RegionId | String | cn-demo-***-*** | The ID of the region. |
| RegionName | String | China (Hangzhou) | The name of the region. |
| RiskCount | String | {} | The details of risks. |
| RiskStatus | String | NO | Indicates whether risks are detected on the asset. Valid values: YES NO |
| SafeEventCou nt | Integer | 5 | The number of alerts that are generated for the asset. |
| Status | String | Running | The status of the asset. Valid values: Running: The asset is running. notRunning: The asset is stopped. |
| Tag | String | InternetIp | The tag that is added to the asset. |
| Uuid | String | c9107c04-942f- 40c1-981a-f1c1*** | The UUID of the asset. |
| VpcInstanceId | String | classic | The ID of the VPC to which the asset belongs. |

| VulCount | Integer | 2 | The number of vulnerabilities that are detected on the asset. |
|---|---|---|---|
| VulStatus | String | YES | Indicates whether the asset is exposed to vulnerabilities. Valid values: YES NO |
| WeakPassword Count | Integer | 2 | The number of weak passwords. |
| WeakPassword Status | String | YES | Indicates whether weak passwords are detected on the asset. Valid values: YES NO |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 50 | The total number of entries returned. |
| RequestId | String | 32A73759-4C0F- 4801-****- 901223ACEE9A | The ID of the request. |
| Success | Boolean | true | Indicates whether the request is successful. Valid values: true: yes false: no |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCloudCenterInstances &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Instances>
    <ProviderId>1</ProviderId>
    <ProviderAzName>None</ProviderAzName>
    <CreatedTime>1609988137000</CreatedTime>
    <Os>Linux</Os>
    <VulStatus>YES</VulStatus>
    <ExposedCount>5</ExposedCount>
    <Ip>192.168.XX.XX</Ip>
    <ProviderRegionName>None</ProviderRegionName>
    <ClientVersion>11_11</ClientVersion>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <RiskCount>{}</RiskCount>
    <PodCount>1</PodCount>
    <Importance>1</Importance>
    <AutoSnapshotsLevel>1</AutoSnapshotsLevel>
    <ProviderRegionId>1</ProviderRegionId>
    <InternetIp>47.100.XX.XX</InternetIp>
    <RegionName>China (Hangzhou)</RegionName>
    <ClusterName>demo-cluster</ClusterName>
    <ExposedStatus>0</ExposedStatus>
    <Status>Running</Status>
    <ClientStatus>online</ClientStatus>
    <SafeEventCount>5</SafeEventCount>
    <ClusterId>16392368*****</ClusterId>
    <InstanceId>i-m5***</InstanceId>
    <WeakPasswordCount>2</WeakPasswordCount>
    <OsName>CentOS 7.6 64-bit</OsName>
    <HealthCheckCount>0</HealthCheckCount>
    <ProviderAzId>1</ProviderAzId>
    <WeakPasswordStatus>YES</WeakPasswordStatus>
    <RiskStatus>NO</RiskStatus>
    <Flag>0</Flag>
    <GroupId>3</GroupId>
    <VulCount>2</VulCount>
    <InstanceName>yztest-l***</InstanceName>
    <ProviderName>None</ProviderName>
    <AssetType>ecs</AssetType>
    <Uuid>c9107c04-942f-40c1-981a-f1c1***</Uuid>
    <AlarmStatus>NO</AlarmStatus>
    <Region>cn-demo-***-***</Region>
    <VpcInstanceId>classic</VpcInstanceId>
    <RegionId>cn-demo-***-***</RegionId>
    <Tag>InternetIp</Tag>
    <HcStatus>NO</HcStatus>
</Instances> <PageInfo>
    <TotalCount>50</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>10</Count>
</PageInfo> <RequestId>32A73759-4C0F-4801-****-901223ACEE9A</RequestId> <Success>true</Success>
```

`JSON` format `{`

```json
    "Instances": {
        "ProviderId": 1,
        "ProviderAzName": "None",
        "CreatedTime": 1609988137000,
        "Os": "Linux",
        "VulStatus": "YES",
        "ExposedCount": 5,
        "Ip": "192.168.XX.XX",
        "ProviderRegionName": "None",
        "ClientVersion": "11_11",
        "IntranetIp": "192.168.XX.XX",
        "RiskCount": "{}",
        "PodCount": 1,
        "Importance": 1,
        "AutoSnapshotsLevel": 1,
        "ProviderRegionId": 1,
        "InternetIp": "47.100.XX.XX",
        "RegionName": "China (Hangzhou)",
        "ClusterName": "demo-cluster",
        "ExposedStatus": 0,
        "Status": "Running",
        "ClientStatus": "online",
        "SafeEventCount": 5,
        "ClusterId": "16392368*****",
        "InstanceId": "i-m5***",
        "WeakPasswordCount": 2,
        "OsName": "CentOS 7.6 64bit",
        "HealthCheckCount": 0,
        "ProviderAzId": 1,
        "WeakPasswordStatus": "YES",
        "RiskStatus": "NO",
        "Flag": 0,
        "GroupId": 3,
        "VulCount": 2,
        "InstanceName": "yztest-l***",
        "ProviderName": "None",
        "AssetType": "ecs",
        "Uuid": "c9107c04-942f-40c1-981a-f1c1***",
        "AlarmStatus": "NO",
        "Region": "cn-demo-***-***",
        "VpcInstanceId": "classic",
        "RegionId": "cn-demo-***-***",
        "Tag": "InternetIp",
        "HcStatus": "NO"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 50,
        "PageSize": 20,
        "CurrentPage": 1,
        "Count": 10
```

`},`

```json
    "RequestId": "32A73759-4C0F-4801-****-901223ACEE9A",
    "Success": true
```

`}`

#### 6.1.7 DescribeSummaryInfo

Queries the security information about assets, such as the security score of your assets, the number of protected assets, and the number of unprotected assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSumma ryInfo | The operation that you want to perform. Set the value to DescribeSummaryInfo. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ResourceDirecto ryAccountId | String | No | None | This parameter is deprecated. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| AegisClientOffl ineCount | Integer | 12 | The number of unprotected assets. |
| AegisClientOnl ineCount | Integer | 127 | The number of protected assets. |
| RequestId | String | D40198E1-6EA8- 482E-****- D9573D75C0CA | The ID of the request. |

| SecurityScore | Integer | 44 | The security score of your assets. Valid values: 95 to 100: The assets are secure. 85 to 94: The assets are exposed to a few security risks. We recommend that you reinforce your security system at the earliest opportunity. 70 to 84: The assets are exposed to a number of security risks. We recommend that you reinforce your security system at the earliest opportunity. 69 or lower: The current security system is unable to protect the asset against attacker intrusions. We recommend that you reinforce your security system at the earliest opportunity. |
|---|---|---|---|
| Success | Boolean | true | This parameter is deprecated. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSummaryInfo &<Common request parameters>
```

Sample success responses `XML` format

```xml
<AegisClientOnlineCount>127</AegisClientOnlineCount> <RequestId>D40198E1-6EA8-482E-****-D9573D75C0CA</RequestId> <AegisClientOfflineCount>12</AegisClientOfflineCount> <SecurityScore>44</SecurityScore> <Success>true</Success>
```

`JSON` format `{`

```json
    "AegisClientOnlineCount": 127,
    "RequestId": "D40198E1-6EA8-482E-****-D9573D75C0CA",
    "AegisClientOfflineCount": 12,
    "SecurityScore": 44,
    "Success": true
```

`}`

### 6.2 Secure score

#### 6.2.1 DescribeSecureSuggestion

Queries suggestions on how to handle the security risks that affect the security score.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecure Suggestion | The operation that you want to perform. Set the value to DescribeSecureSuggestion. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | F35F45B0-5D6B- ****-BE02- A62D0760E840 | The ID of the request. |
| Suggestions | Array of Suggestion |   | An array that consists of the suggestions. |
| Detail | Array of Detail |   | An array that consists of the details about the suggestions. |
| Description | String | You have four ApsaraDB RDS instances at risk. | The description of the suggestion. |
| SubType | String | CLOUD HC RDS _ _ | The sub-type of the unhandled risk. |
| Title | String | The check on security policies of ApsaraDB RDS instances has failed. The instances are at risk | The name of the unhandled risk. |
| Points | Integer | 40 | The penalty point of each item. |

| SuggestType | String | SS ALARM _ | The type of the unhandled risk. Valid values: SS REINFORCE: Key features, such as _ the antivirus feature, are not configured. SS ALARM: unhandled alerts. _ SS VUL: unfixed vulnerabilities. _ SS HC: baseline risks. _ SS AK: AccessKey pair leaks. _ SS CLOUD HC: configuration risks in _ _ Alibaba Cloud services. OTHER: other risks. |
|---|---|---|---|
| TotalCount | Integer | 15 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecureSuggestion &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Suggestions>
    <Points>40</Points>
    <SuggestType>SS_ALARM</SuggestType>
    <Detail>
        <SubType>CLOUD_HC_RDS</SubType>
        <Description>You have four ApsaraDB RDS instances at risk.</Description>
        <Title>The check on security policies of ApsaraDB RDS instances has failed. The
instances are at risk</Title>
    </Detail>
</Suggestions> <TotalCount>15</TotalCount> <RequestId>F35F45B0-5D6B-****-BE02-A62D0760E840</RequestId>
```

`JSON` format `{`

```json
    "Suggestions": {
        "Points": 40,
        "SuggestType": "SS_ALARM",
        "Detail": {
            "SubType": "CLOUD_HC_RDS",
            "Description": "You have four ApsaraDB RDS instances at risk.",
            "Title": "The check on security policies of ApsaraDB RDS instances has fail
ed. The instances are at risk"
```

`}` `},`

```json
    "TotalCount": 15,
    "RequestId": "F35F45B0-5D6B-****-BE02-A62D0760E840"
```

`}`

### 6.3 Security alerts

#### 6.3.1 DescribeAlarmEventList

Queries alert events on the Alerts page. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmE ventList | The operation that you want to perform. Set the value to DescribeAlarmEventList. |
| CurrentPage | Integer | Yes | 1 | The number of the page to return. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| PageSize | String | Yes | 20 | The number of entries to return on each page. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Dealed | String | No | Y | The status of the alert event. Valid values: N: unhandled Y: handled |
|---|---|---|---|---|
| Levels | String | No | serious | The severities of the alert events. Separate multiple severities with commas (,). Valid values: serious suspicious remind |
| Remark | String | No | database server _ | The name of the alert, or the asset information. |
| GroupId | String | No | tst*** | The group ID of the affected asset. |
| AlarmEventNam e | String | No | DDoS trojan | The name of the alert event. |
| AlarmEventType | String | No | Malicious process | The type of the alert event. |
| UniqueInfo | String | No | asdasjhdk**** | The unique identifier of the alert event. |

| OperateErrorCod eList.N | RepeatL ist | No | ignore. Success | The handling result code of the alert event. Set the value in the following format: Operation type.Operation result code. Operation types include: Common: performs common operations. deal: handles the alert. ignore: ignores the alert. offline handled: marks the alert _ as handled. mark mis info: adds the alerts to _ _ the whitelist. rm mark mis info: removes the _ _ _ alerts from the whitelist. quara: quarantines the source file of the malicious process. kill and quara: terminates the _ _ malicious process and quarantines the source file. kill virus: deletes the source file _ of the malicious process. block ip: blocks the source file of _ the malicious process. manual handled: manually _ handles the alert. Operation result codes include: Success: The operation is successful. Failure: The operation fails. AgentOffline: The agent is offline. |
|---|---|---|---|---|
| ClusterId | String | No | dasdaS****** | The ID of the cluster. |
| ContainerFieldN ame | String | No | containerId | The key that is used to query the container. |
| ContainerFieldV alue | String | No | sadskdjhaskjdha sd***** | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |

| Count | Integer | 1 | The total number of returned pages. |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| RequestId | String | 28267723-D857- 4DD8-****- 013100000000 | The ID of the request. |
| SuspEvents | Array of SuspEvents |   | An array that consists of the information about the alert event. |
| AlarmEventNa me | String | Execution of malicious commands | The name of the alert event. |
| AlarmEventNa meOriginal | String | Precise defense against malicious commands | The original parent name of the alert event. |
| AlarmEventTy pe | String | Suspicious process | The type of the alert event. |
| AlarmUniqueIn fo | String | 8df9******f4211fbf 756ef***** | The ID of the alert event. |
| AppName | String | app1 | The name of the application. |
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the alert event is supported, such as quarantining the source file of the malicious process, adding the alert event to the whitelist, and ignoring the alert event. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert as a false positive. Valid values: true: yes false: no |

| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
|---|---|---|---|
| ContainerId | String | sadjadash*** | The ID of the container. |
| ContainerImag eId | String | cri-asdaks***** | The ID of the image to which the container belongs. |
| ContainerImag eName | String | centos1 | The name of the image to which the container belongs. |
| DataSource | String | aegis *** _ | The source of data. |
| Dealed | Boolean | false | Indicates whether the alert is handled. Valid values: true: yes false: no |
| Description | String | After an attacker accesses a server, the attacker may import malicious shell scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. | The description of the alert event. |
| EndTime | Long | 1543740301000 | The end time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| GmtModified | Long | 1569235879000 | The time when the alert was last triggered. The value is a UNIX timestamp. Unit: milliseconds. |
| HasTraceInfo | Boolean | true | Indicates whether the alert has tracing information. Valid values: true: yes false: no |
| InstanceId | String | i-e*** | The ID of the affected asset. |
| InstanceName | String | Test server | The name of the affected asset. |

| InternetIp | String | 47.100.XX.XX | The public IP address of the affected asset. |
|---|---|---|---|
| IntranetIp | String | 192.168.XX.XX | The private IP address of the affected asset. |
| K8sClusterId | String | cb9218d50728c47 0fb7dfbc16***** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | cqqtesttest | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-system | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km100o6qy****** | The ID of the node in the Kubernetes cluster. |
| K8sNodeName | String | node1 | The name of the node in the Kubernetes cluster. |
| K8sPodName | String | podname1 | The pod name of the Kubernetes cluster. |
| Level | String | serious | The severity of the alert event. Valid values: serious suspicious remind |
| OperateErrorC ode | String | kill and quara.Suc _ _ cess | The handling result code of the alert event. |
| OperateTime | Long | 1234567890123 | The time when the operation is performed. The value is a UNIX timestamp. Unit: milliseconds. |
| SaleVersion | String | 1 | The edition in which alert event detection can be enabled. Valid values: 0: the Basic edition 1: the Enterprise edition |
| SecurityEventI ds | String | 1 | The IDs of associated exceptions. |

| Solution | String | Check the malicious URLs that are listed in the alert. Check the directory for malicious files. Terminate malicious processes. If you manually run the processes, you can mark them as false positives in the console. | The solution to the alert event. |
|---|---|---|---|
| Stages | String | ["attack entrance"] _ | The phase of the alert event. |
| StartTime | Long | 1543740301000 | The start time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| SuspiciousEve ntCount | Integer | 1 | The number of associated exceptions. |
| Uuid | String | 47900178-885d- 4fa4-9d77-*** | The ID of the associated instance. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventList &CurrentPage=1 &From=sas &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>28267723-D857-4DD8-****-013100000000</RequestId> <SuspEvents>
    <K8sNodeId>i-km100o6qy******</K8sNodeId>
    <Description>After an attacker accesses a server, the attacker may import malicious
shell scripts into scheduled tasks to keep malicious programs running. The scheduled ta sks include crontab and systemd. </Description>
    <K8sNodeName>node1</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1543740301000</EndTime>
    <OperateErrorCode>kill_and_quara.Success</OperateErrorCode>
    <AlarmEventName>Execution of malicious commands</AlarmEventName>
    <SecurityEventIds>1</SecurityEventIds>
    <GmtModified>1569235879000</GmtModified>
    <HasTraceInfo>true</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218d50728c470fb7dfbc16*****</K8sClusterId>
    <AppName>app1</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>sadjadash***</ContainerId>
    <AlarmEventType>Suspicious process</AlarmEventType>
    <Solution>Check the malicious URLs that are listed in the alert. Check the director
y for malicious files. Terminate malicious processes. If you manually run the processes , you can mark them as false positives in the console. </Solution>
    <CanCancelFault>false</CanCancelFault>
    <AlarmEventNameOriginal>Precise defense against malicious
commands</AlarmEventNameOriginal>
    <InstanceId>i-e***</InstanceId>
    <Stages>["attack_entrance"]</Stages>
    <StartTime>1543740301000</StartTime>
    <K8sPodName>podname1</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <Dealed>false</Dealed>
    <ContainerImageId>cri-asdaks*****</ContainerImageId>
    <DataSource>aegis_***</DataSource>
    <InstanceName>Test server</InstanceName>
    <OperateTime>1234567890123</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <K8sClusterName>cqqtesttest</K8sClusterName>
    <Uuid>47900178-885d-4fa4-9d77-***</Uuid>
    <ContainerImageName>centos1</ContainerImageName>
    <SuspiciousEventCount>1</SuspiciousEventCount>
    <AlarmUniqueInfo>8df9******f4211fbf756ef*****</AlarmUniqueInfo>
    <Level>serious</Level>
</SuspEvents>
```

`JSON` format

| { "PageInfo": { "TotalCount": 1, "PageSize": 20, "CurrentPage": 1, "Count": 1 }, "RequestId": "28267723-D857-4DD8-****-013100000000", "SuspEvents": { "K8sNodeId": "i-km100o6qy******", "Description": "After an attacker accesses a server, the attacker may import ma licious shell scripts into scheduled tasks to keep malicious programs running. The sche duled tasks include crontab and systemd.", "K8sNodeName": "node1", "ContainHwMode": false, "EndTime": 1543740301000, "OperateErrorCode": "kill and quara.Success", _ _ "AlarmEventName": "Execution of malicious commands", "SecurityEventIds": 1, "GmtModified": 1569235879000, "HasTraceInfo": true, "IntranetIp": "192.168.XX.XX", "K8sClusterId": "cb9218d50728c470fb7dfbc16*****", "AppName": "app1", "K8sNamespace": "kube-system", "InternetIp": "47.100.XX.XX", "ContainerId": "sadjadash***", "AlarmEventType": "Suspicious process", "Solution": "Check the malicious URLs that are listed in the alert. Check the d irectory for malicious files. Terminate malicious processes. If you manually run the pr ocesses, you can mark them as false positives in the console.", "CanCancelFault": false, "AlarmEventNameOriginal": "Precise defense against malicious commands", "InstanceId": "i-e***", "Stages": "[\"attack entrance\"]", _ "StartTime": 1543740301000, "K8sPodName": "podname1", "SaleVersion": 1, "Dealed": false, "ContainerImageId": "cri-asdaks*****", "DataSource": "aegis ***", _ "InstanceName": "Test server", "OperateTime": 1234567890123, "CanBeDealOnLine": true, "K8sClusterName": "cqqtesttest", "Uuid": "47900178-885d-4fa4-9d77-***", "ContainerImageName": "centos1", "SuspiciousEventCount": 1, "AlarmUniqueInfo": "8df9******f4211fbf756ef*****", "Level": "serious" } } |   |
|---|---|

#### 6.3.2 DescribeAlarmEventDetail

Queries the details of an alert event. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAlarmE ventDetail | The operation that you want to perform. Set the value to DescribeAlarmEventDetail. |
| AlarmUniqueInfo | String | Yes | 8df************* *********** | The ID of the alert event. Note To query the details of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to obtain the ID of the alert event. |
| From | String | Yes | sas | The ID of the request source. Set the value to sas. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Data | Struct |   | The details of the alert event. |
| AlarmEventAli asName | String | Webshell - Webshell file | The alias of the alert type. |

| AlarmEventDe sc | String | After an attacker accesses a server, the attacker may import malicious shell scripts into scheduled tasks to keep malicious programs running. The scheduled tasks include crontab and systemd. | The description of the alert event. |
|---|---|---|---|
| AlarmUniqueIn fo | String | asds************ | The ID of the alert event. |
| AppName | String | demo-name | The name of the Kubernetes application. |
| CanBeDealOnL ine | Boolean | false | Indicates whether the online processing of alert events is supported, such as blocking an alert, adding an alert to the whitelist, and ignoring an alert. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert event as a false positive. Valid values: true: yes false: no |
| CauseDetails | Array of CauseDetail |   | An array that consists of the cause of the alert event, which can be used to trace the alert. |
| Key | String | item | The key of the field that displays the tracing information. |
| Value | Array of Value |   | An array that consists of the value of the field that displays the tracing information. |
| Name | String | Solutions | The name of the field that displays the tracing information. |
| Type | String | html | The format of the field that displays the tracing information. Valid values: html text |

| Value | String | Check for the exploited pages of your web services and vulnerabilities in parameter configuration, and resolve these issues. | The value of the field that displays the tracing information. |
|---|---|---|---|
| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
| ContainerId | String | B4*****-3***-4***- B***-9F******** | The ID of the container. |
| ContainerImag eId | String | docker- pullable://registry.a cs.demo.com/acs/a liyun-demo- controller:demo | The ID of the image to which the container belongs. |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun- demo- controller:demo | The name of the image to which the container belongs. |
| DataSource | String | demo *** _ | The source of data. |
| EndTime | Long | 1542366542000 | The end time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| InstanceName | String | worker-k8s-for-cs- cb9****** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address. |
| K8sClusterId | String | cb9218*********** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | demo******* | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-system | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km10********** | The ID of the node in the Kubernetes cluster. |

| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | The name of the node in the Kubernetes cluster. |
|---|---|---|---|
| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | The pod name of the Kubernetes cluster. |
| Level | String | serious | The severity of the alert event. Valid values: serious suspicious remind |
| Solution | String | Check the malicious URLs that are listed in the alert. Check the directory for malicious file downloads. Stop the malicious processes that are running. If you trust the processes, mark the alert as a false positive in the console, and submit a ticket to security engineers. | The solution to the alert event. |
| StartTime | Long | 1542378601000 | The start time of the alert event. The value is a UNIX timestamp. Unit: milliseconds. |
| Type | String | Suspicious network connection | The type of the alert event. |
| Uuid | String | B41******-3***- 4***-B***- 9********* | The UUID of the server. |
| RequestId | String | B41******-3***- 4***-B***- 9********* | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeAlarmEventDetail &AlarmUniqueInfo=8df914418f4211fbf756efe7a6f40cbc &From=sas &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>B41******-3***-4***-B***-9*********</RequestId> <Data>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <EndTime>1542366542000</EndTime>
    <IntranetIp>192.168.0.100</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <AppName>demo-name</AppName>
    <K8sNamespace>kube-system</K8sNamespace>
    <InternetIp>123.123.123.123</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
    <AlarmEventDesc>After an attacker accesses a server, the attacker may import malici
ous shell scripts into scheduled tasks to keep malicious programs running. The schedule d tasks include crontab and systemd. </AlarmEventDesc>
    <Solution>Check the malicious URLs that are listed in the alert. Check the director
y for malicious file downloads. Stop the malicious processes that are running. If you t rust the processes, mark the alert as a false positive in the console, and submit a tic ket to security engineers. </Solution>
    <CanCancelFault>false</CanCancelFault>
    <StartTime>1542378601000</StartTime>
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <ContainerImageId>docker-pullable://registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageId>
    <DataSource>demo_***</DataSource>
    <InstanceName>worker-k8s-for-cs-cb9******</InstanceName>
    <CanBeDealOnLine>false</CanBeDealOnLine>
    <Type>Suspicious network connection</Type>
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>B41******-3***-4***-B***-9*********</Uuid>
    <ContainerImageName>registry.acs.demo.com/acs/aliyun-demo-
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>asds************</AlarmUniqueInfo>
    <AlarmEventAliasName>Webshell - Webshell file</AlarmEventAliasName>
    <Level>serious</Level>
    <CauseDetails>
        <Key>item</Key>
        <Value>
            <Type>html</Type>
            <Value>Check for the exploited pages of your web services and
vulnerabilities in parameter configuration, and resolve these issues. </Value>
            <Name>Solutions</Name>
        </Value>
    </CauseDetails>
</Data>
```

`JSON` format `{`

```json
    "RequestId": "B41******-3***-4***-B***-9*********",
    "Data": {
        "K8sNodeId": "i-km10**********",
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "EndTime": 1542366542000,
        "IntranetIp": "192.168.0.100",
        "K8sClusterId": "cb9218***********",
        "AppName": "demo-name",
        "K8sNamespace": "kube-system",
        "InternetIp": "123.123.123.123",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
        "AlarmEventDesc": "After an attacker accesses a server, the attacker may import
malicious shell scripts into scheduled tasks to keep malicious programs running. The sc heduled tasks include crontab and systemd.",
        "Solution": "Check the malicious URLs that are listed in the alert. Check the d
irectory for malicious file downloads. Stop the malicious processes that are running. I f you trust the processes, mark the alert as a false positive in the console, and submi t a ticket to security engineers.",
        "CanCancelFault": false,
        "StartTime": 1542378601000,
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "ContainerImageId": "docker-pullable://registry.acs.demo.com/acs/aliyun-demo-co
ntroller:demo",
        "DataSource": "demo_***",
        "InstanceName": "worker-k8s-for-cs-cb9******",
        "CanBeDealOnLine": false,
        "Type": "Suspicious network connection",
        "K8sClusterName": "demo*******",
        "Uuid": "B41******-3***-4***-B***-9*********",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-demo-controller:demo",
        "AlarmUniqueInfo": "asds************",
        "AlarmEventAliasName": "Webshell - Webshell file",
        "Level": "serious",
        "CauseDetails": {
            "Key": "item",
            "Value": {
                "Type": "html",
                "Value": "Check for the exploited pages of your web services and
vulnerabilities in parameter configuration, and resolve these issues.",
                "Name": "Solutions"
```

`}` `}` `}` `}`

#### 6.3.3 DescribeSuspEvents

Queries the information about an exception. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv ents | The operation that you want to perform. Set the value to DescribeSuspEvents. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Dealed | String | No | N | The status of the exception. Valid values: N: unhandled Y: handled |
| Name | String | No | ecs-xxx | The name of the exception or the affected server. Fuzzy match is supported. |
| Levels | String | No | serious | The severity of the exception. Separate multiple severities with commas (,). The following severities are listed in descending order: serious suspicious remind |

| ParentEventTyp es | String | No | Webshell | The type of the alert event. Valid values: Suspicious process Webshell Unusual logon Exception Sensitive file tampering Malicious process (cloud threat detection) Suspicious network connection Other Abnormal account Application intrusion event Cloud threat detection Precise defense Application whitelist Persistent webshell Web application threat detection Malicious script Threat intelligence Malicious network activity |
|---|---|---|---|---|
| Remark | String | No | Test server | The IP address or name of the server. |
| Status | String | No | None | This parameter is deprecated. |
| PageSize | String | No | 20 | The number of entries to return on each page. |
| CurrentPage | String | No | 1 | The number of the page to return. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| AlarmUniqueInfo | String | No | 8df914418f4211 fbf*** | The ID of the alert event to which the exception is related. Note To query the details about the exceptions of an alert event, you must specify the ID of the alert event. You can call the DescribeAlarmEventList operation to query the IDs of alert events. |
|---|---|---|---|---|
| UniqueInfo | String | No | a0************** ******* | The unique information that identifies the exception. |
| From | String | No | sas | The data source of the exception. Set the value to sas. |
| Source | String | No | 47.100.XX.XX | The source IP address of the request. |
| GroupId | Long | No | 1 | The ID of the group. |
| Uuids | String | No | xxxx-xx-xxxx- xxxx-xxxx | The UUIDs of servers. Separate multiple UUIDs with commas (,). |
| OperateErrorCod eList.N | RepeatL ist | No | None | This parameter is deprecated. |
| ClusterId | String | No | 1 | The ID of the cluster. |
| ContainerFieldN ame | String | No | appName1 | The key that is used to query the container. |
| ContainerFieldV alue | String | No | nginx-***- controller | The value that is used to query the container. |
| TargetType | String | No | containerId | The container that matches both the value of ContainerFieldName and the value of ContainerFieldValue. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 1 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |

| PageSize | Integer | 20 | The number of entries returned per page. |
|---|---|---|---|
| RequestId | String | 43F670F3-AB40- 4E91-****- C57400000000 | The ID of the request. |
| SuspEvents | Array of WarningSumm ary |   | An array that consists of the information about the exception. |
| Advanced | Boolean | false | Indicates whether the Advanced edition is purchased. Valid values: true: yes false: no |
| AlarmEventNa me | String | DDoS trojan | The name of the alert event. |
| AlarmEventNa meDisplay | String | None | This parameter is deprecated. |
| AlarmEventTy pe | String | Malicious process (cloud threat detection) | The type of the alert event. |
| AlarmEventTy peDisplay | String | None | This parameter is deprecated. |
| AlarmUniqueIn fo | String | 8df914418f*** | The ID of the alert event. |
| AppName | String | demo-name | The name of the Kubernetes application. |
| AutoBreaking | Boolean | false | Indicates whether the exception is automatically blocked. Valid values: true: yes false: no |
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of the exception is supported, such as quarantining a file. Valid values: true: yes false: no |
| CanCancelFaul t | Boolean | false | Indicates whether you can cancel marking the alert event as a false positive. Valid values: true: yes false: no |

| ContainHwMod e | Boolean | false | Indicates whether network protection is enabled. Valid values: true: yes false: no |
|---|---|---|---|
| ContainerId | String | B4*****-3***-4***- B***-9F******** | The ID of the container. |
| ContainerImag eId | String | docker- pullable://registry.a cs.***.com/acs/aliy un-**- controller:demo | The ID of the image to which the container belongs. |
| ContainerImag eName | String | registry.acs.demo. com/acs/aliyun-**- controller:demo | The name of the image to which the container belongs. |
| DataSource | String | aegis suspicious * _ _ ** | The source of data. |
| Desc | String | XOR DDoS trojan | The description of the exception. |
| Details | Array of QuaraFile |   | An array that consists of the exception details. |
| InfoType | String | download url _ | The type of the icon. |
| Name | String | Alert description | The name in the exception details. |
| NameDisplay | String | None | This parameter is deprecated. |
| Type | String | html | The format of the exception details. Valid values: text html |
| Value | String | Description | The content in the exception details. |
| ValueDisplay | String | None | This parameter is deprecated. |
| EventNotes | Array of EventNote |   | An array that consists of the remarks. |
| Note | String | Remarks | The content of the remarks. |
| NoteId | Long | 1 | The ID of the remarks. |

| NoteTime | String | 2018-12-12 12:00:00 | The time when the remarks were created. The time is in the yyyy-MM-dd HH:mm:ss format. |
|---|---|---|---|
| EventStatus | Integer | 1 | The status of the exception. Valid values: 1: unhandled 2: ignored 4: confirmed 8: marked as a false positive 16: handling 32: handled 64: expired |
| EventSubType | String | XOR DDoS trojan | The name of the exception. |
| HasTraceInfo | Boolean | false | This parameter is deprecated. |
| Id | Long | 1000 | The ID of the exception. |
| InstanceId | String | i-km10********* | The ID of the instance. |
| InstanceName | String | nginx | The name of the associated instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the associated instance. |
| IntranetIp | String | 192.168.XX.XX | The private IP address of the associated instance. |
| K8sClusterId | String | cb9218*********** | The ID of the Kubernetes cluster. |
| K8sClusterNa me | String | demo******* | The name of the Kubernetes cluster. |
| K8sNamespac e | String | kube-**** | The namespace of the Kubernetes cluster. |
| K8sNodeId | String | i-km10********** | The ID of the node in the Kubernetes cluster. |
| K8sNodeName | String | cn-wulan-env116- d01.i- km10*********** | The node name of the Kubernetes cluster. |

| K8sPodName | String | nginx-ingress- controller-5b******- l4*** | The pod name of the Kubernetes cluster. |
|---|---|---|---|
| LastTime | String | 2018-09-26 01:51:01 | The time when the exception was last detected. The time is in the yyyy-MM-dd HH:mm:ss format. |
| LastTimeStam p | Long | 1639236844747 | The time when the exception was last detected. The value is a UNIX timestamp. Unit: milliseconds. |
| Level | String | serious | The severity of the exception. Valid values: serious suspicious remind |
| MarkMisRules | String | ***Trojan file path*****Contain** ** | The advanced whitelist rule. |
| Name | String | Malicious process (cloud threat detection) - XOR DDoS trojan | The complete name of the exception. |
| OccurrenceTi me | String | 2018-09-26 01:51:01 | The time when the exception first occurred. The time is in the yyyy-MM-dd HH:mm:ss format. |
| OccurrenceTi meStamp | Long | 1639236844747 | The time when the exception was first detected. The value is a UNIX timestamp. Unit: milliseconds. |
| OperateErrorC ode | String | quara.Succes | The handling result of the exception. |
| OperateMsg | String | success | The remarks of the exception operation. |
| OperateTime | Long | 1639236844747 | The time when the operation is performed. The value is a UNIX timestamp. Unit: milliseconds. |
| SaleVersion | String | 1 | The edition in which exception detection can be enabled. Valid values: 0: the Basic edition 1: the Enterprise edition |
| SecurityEventI ds | String | None | This parameter is deprecated. |

| Stages | String | [] | The phase of the exception. |
|---|---|---|---|
| UniqueInfo | String | e17e*** | The ID of the exception. |
| Uuid | String | bf6b30d3-eea8- 4924-9f0a-*** | The ID of the associated instance. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEvents &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>100</TotalCount> <PageSize>20</PageSize> <RequestId>43F670F3-AB40-4E91-****-C57400000000</RequestId> <CurrentPage>1</CurrentPage> <Count>1</Count> <SuspEvents>
    <K8sNodeId>i-km10**********</K8sNodeId>
    <Advanced>false</Advanced>
    <K8sNodeName>cn-wulan-env116-d01.i-km10***********</K8sNodeName>
    <ContainHwMode>false</ContainHwMode>
    <OperateErrorCode>quara.Succes</OperateErrorCode>
    <AlarmEventName>DDoS trojan</AlarmEventName>
    <SecurityEventIds>None</SecurityEventIds>
    <EventStatus>1</EventStatus>
    <HasTraceInfo>false</HasTraceInfo>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>cb9218***********</K8sClusterId>
    <EventSubType>XOR DDoS trojan</EventSubType>
    <AppName>demo-name</AppName>
    <Name>Malicious process (cloud threat detection) - XOR DDoS trojan</Name>
    <K8sNamespace>kube-****</K8sNamespace>
    <Desc>XOR DDoS trojan</Desc>
    <LastTimeStamp>1639236844747</LastTimeStamp>
    <InternetIp>47.100.XX.XX</InternetIp>
    <ContainerId>B4*****-3***-4***-B***-9F********</ContainerId>
    <AlarmEventType>Malicious processes (cloud threat detection)</AlarmEventType>
    <AlarmEventNameDisplay>None</AlarmEventNameDisplay>
    <UniqueInfo>e17e***</UniqueInfo>
    <CanCancelFault>false</CanCancelFault>
    <AlarmEventTypeDisplay>None</AlarmEventTypeDisplay>
    <InstanceId>i-km10*********</InstanceId>
    <Stages>[]</Stages>
```

```xml
    <MarkMisRules>***Trojan file path*****Contain****</MarkMisRules>
    <K8sPodName>nginx-ingress-controller-5b******-l4***</K8sPodName>
    <SaleVersion>1</SaleVersion>
    <ContainerImageId>docker-pullable://registry.acs.***.com/acs/aliyun-**-
controller:demo</ContainerImageId>
    <DataSource>aegis_suspicious_***</DataSource>
    <InstanceName>nginx</InstanceName>
    <OccurrenceTime>2018-09-26 01:51:01</OccurrenceTime>
    <OperateTime>1639236844747</OperateTime>
    <CanBeDealOnLine>true</CanBeDealOnLine>
    <OperateMsg>success</OperateMsg>
    <K8sClusterName>demo*******</K8sClusterName>
    <Uuid>bf6b30d3-eea8-4924-9f0a-***</Uuid>
    <ContainerImageName>registry.acs.demo.com/acs/aliyun-**-
controller:demo</ContainerImageName>
    <AlarmUniqueInfo>8df914418f***</AlarmUniqueInfo>
    <AutoBreaking>false</AutoBreaking>
    <OccurrenceTimeStamp>1639236844747</OccurrenceTimeStamp>
    <Level>serious</Level>
    <Id>1000</Id>
    <LastTime>2018-09-26 01:51:01</LastTime>
    <Details>
        <Type>html</Type>
        <Value>Description</Value>
        <ValueDisplay>None</ValueDisplay>
        <InfoType>download_url</InfoType>
        <NameDisplay>None</NameDisplay>
        <Name>Alert description</Name>
    </Details>
    <EventNotes>
        <NoteId>1</NoteId>
        <Note>Remarks</Note>
        <NoteTime>2018-12-12 12:00:00</NoteTime>
    </EventNotes>
</SuspEvents>
```

`JSON` format `{`

```json
    "TotalCount": 100,
    "PageSize": 20,
    "RequestId": "43F670F3-AB40-4E91-****-C57400000000",
    "CurrentPage": 1,
    "Count": 1,
    "SuspEvents": {
        "K8sNodeId": "i-km10**********",
        "Advanced": false,
        "K8sNodeName": "cn-wulan-env116-d01.i-km10***********",
        "ContainHwMode": false,
        "OperateErrorCode": "quara.Succes",
        "AlarmEventName": "DDoS trojan",
        "SecurityEventIds": "None",
        "EventStatus": 1,
        "HasTraceInfo": false,
```

`,`

```json
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "cb9218***********",
        "EventSubType": "XOR DDoS trojan",
        "AppName": "demo-name",
        "Name": "Malicious process (cloud threat detection) - XOR DDoS trojan",
        "K8sNamespace": "kube-****",
        "Desc": "XOR DDoS trojan",
        "LastTimeStamp": 1639236844747,
        "InternetIp": "47.100.XX.XX",
        "ContainerId": "B4*****-3***-4***-B***-9F********",
        "AlarmEventType": "Malicious process (cloud threat detection)",
        "AlarmEventNameDisplay": "None",
        "UniqueInfo": "e17e***",
        "CanCancelFault": false,
        "AlarmEventTypeDisplay": "None",
        "InstanceId": "i-km10*********",
        "Stages": "[]",
        "MarkMisRules": "***Trojan file path*****Contain****",
        "K8sPodName": "nginx-ingress-controller-5b******-l4***",
        "SaleVersion": 1,
        "ContainerImageId": "docker-pullable://registry.acs.***.com/acs/aliyun-**-contr
oller:demo",
        "DataSource": "aegis_suspicious_***",
        "InstanceName": "nginx",
        "OccurrenceTime": "2018-09-26 01:51:01",
        "OperateTime": 1639236844747,
        "CanBeDealOnLine": true,
        "OperateMsg": "success",
        "K8sClusterName": "demo*******",
        "Uuid": "bf6b30d3-eea8-4924-9f0a-***",
        "ContainerImageName": "registry.acs.demo.com/acs/aliyun-**-controller:demo",
        "AlarmUniqueInfo": "8df914418f***",
        "AutoBreaking": false,
        "OccurrenceTimeStamp": 1639236844747,
        "Level": "serious",
        "Id": 1000,
        "LastTime": "2018-09-26 01:51:01",
        "Details": {
            "Type": "html",
            "Value": "Description",
            "ValueDisplay": "None",
            "InfoType": "download_url",
            "NameDisplay": "None",
            "Name": "Alert description"
```

`},`

```json
        "EventNotes": {
            "NoteId": 1,
            "Note": "Remarks",
            "NoteTime": "2018-12-12 12:00:00"
```

`}` `}` `}`

#### 6.3.4 DescribeSuspEventDetail

Queries the details of an exception. An alert event consists of an alert and exceptions. Each alert event is associated with multiple exceptions.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSuspEv entDetail | The operation that you want to perform. Set the value to DescribeSuspEventDetail. |
| From | String | Yes | sas | The data source of the exception. Set the value to sas. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| SuspiciousEventI d | Integer | No | 1 | The ID of the exception. Note To query the details of an exception, you must specify the ID of the exception. You can call the DescribeSuspEvents operation to query the IDs of exceptions. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CanBeDealOnL ine | Boolean | true | Indicates whether the online processing of exceptions is supported. Valid values: true: yes false: no |
| DataSource | String | aegis suspicious * _ _ ** | The data source of the exception. |

| Details | Array of QuaraFile |   | An array that consists of the details about the exception. |
|---|---|---|---|
| InfoType | String | download url _ | The type of the icon. |
| Name | String | Alert description | The title in the exception details. |
| Type | String | html | The format of the exception details. Valid values: text html |
| Value | String | Description | The content in the exception details. |
| EventDesc | String | This file may have been uploaded by an attacker who has intruded into your website. Check the validity of this file. | The description of the exception. |
| EventName | String | WEBSHELL | The name of the exception. |
| EventStatus | String | 32 | The status of the exception. Valid values: 1: pending handling 2: ignored 4: confirmed 8: marked as false positive 16: handling 32: handled 64: expired |
| EventTypeDes c | String | Webshell - Webshell file | The type of the exception. |
| Id | Integer | 1 | The ID of the alert event. |
| InstanceName | String | worker-k8s-for-cs- cb9****** | The name of the instance. |
| InternetIp | String | 47.100.XX.XX | The public IP address. |
| IntranetIp | String | 192.168.XX.XX | The private IP address. |

| LastTime | String | 2018-10-30 11:43:46 | The time when the exception last occurred. The time is in the yyyy-MM-dd HH:mm:ss format. |
|---|---|---|---|
| Level | String | serious | The severity of the exception. Valid values: serious suspicious remind |
| OperateErrorC ode | String | quara.Succes | The handling result of the exception. |
| OperateMsg | String | success | The message that describes the handling result of the exception. |
| RequestId | String | 1 | The ID of the request. |
| SaleVersion | String | None | This parameter is deprecated. |
| SasId | String | None | This parameter is deprecated. |
| Uuid | String | B41******-3***- 4***-B***- 9********* | The UUID of the server. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSuspEventDetail &From=sas &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EventDesc>This file may have been uploaded by an attacker who has intruded into your w ebsite. Check the validity of this file.</EventDesc> <EventTypeDesc>Webshell - Webshell file</EventTypeDesc> <RequestId>1</RequestId> <OperateErrorCode>quara.Succes</OperateErrorCode> <EventStatus>32</EventStatus> <EventName>WEBSHELL</EventName> <SaleVersion>None</SaleVersion> <IntranetIp>192.168.XX.XX</IntranetIp> <DataSource>aegis_suspicious_***</DataSource> <InstanceName>worker-k8s-for-cs-cb9******</InstanceName> <CanBeDealOnLine>true</CanBeDealOnLine> <OperateMsg>success</OperateMsg> <Uuid>B41******-3***-4***-B***-9*********</Uuid> <Details>
    <Type>html</Type>
    <Value>Description</Value>
    <InfoType>download_url</InfoType>
    <Name>Alert description</Name>
</Details> <InternetIp>47.100.XX.XX</InternetIp> <Level>serious</Level> <Id>1</Id> <LastTime> 2018-10-30 11:43:46 </LastTime> <SasId>None</SasId>
```

`JSON` format `{`

```json
    "EventDesc": "This file may have been uploaded by an attacker who has intruded into
your website. Check the validity of this file.",
    "EventTypeDesc": "Webshell - Webshell file",
    "RequestId": 1,
    "OperateErrorCode": "quara.Succes",
    "EventStatus": 32,
    "EventName": "WEBSHELL",
    "SaleVersion": "None",
    "IntranetIp": "192.168.XX.XX",
    "DataSource": "aegis_suspicious_***",
    "InstanceName": "worker-k8s-for-cs-cb9******",
    "CanBeDealOnLine": true,
    "OperateMsg": "success",
    "Uuid": "B41******-3***-4***-B***-9*********",
    "Details": {
        "Type": "html",
        "Value": "Description",
        "InfoType": "download_url",
        "Name": "Alert description"
```

`},`

```json
    "InternetIp": "47.100.XX.XX",
    "Level": "serious",
    "Id": 1,
    "LastTime": "2018-10-30 11:43:46",
    "SasId": "None"
```

`}`

### 6.4 Configuration assessment

#### 6.4.1 DescribeRiskItemType

Queries the types of check items in configuration assessment. Each check item is categorized into a type. The types of check items include identity authentication and permissions, network access control, log audit, data security, monitoring and alerting, and basic security protection.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskIte mType | The operation that you want to perform. Set the value to DescribeRiskItemType. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |

| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| List | Array of ItemType |   | An array that consists of the types of check items. |
| Id | Long | 1 | The ID of the check item. |
| Title | String | Identity authentication and permissions | The type of the check item. |
| RequestId | String | 3B3F3A90-46A5- ***-A2D8- D68B14262F96 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskItemType &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>3B3F3A90-46A5-***-A2D8-D68B14262F96</RequestId> <List>
    <Title>Identity authentication and permissions</Title>
    <Id>1</Id>
</List>
```

`JSON` format `{`

```json
    "RequestId": "3B3F3A90-46A5-***-A2D8-D68B14262F96",
    "List": {
        "Title": "Identity authentication and permissions",
        "Id": 1
```

`}` `}`

#### 6.4.2 StartBaselineSecurityCheck

Checks cloud service configurations. You can check all items or a specific item and verify whether an item is checked.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | StartBaselineSe curityCheck | The operation that you want to perform. Set the value to StartBaselineSecurityCheck. |
| Type | String | Yes | check | The type of the check task. Valid values: check verify |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ItemIds.N | RepeatL ist | No | 1 | The ID of the check item. Note To perform a check task on cloud service configurations, you must specify the ID of the check item. You can call the DescribeRiskItemType operation to obtain the IDs of check items. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-***- 0995757C47E9 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=StartBaselineSecurityCheck &Type=check &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>48D2E9A9-A1B0-4295-***-0995757C47E9</RequestId>
```

`JSON` format `{`

```json
    "RequestId": "48D2E9A9-A1B0-4295-***-0995757C47E9"
```

`}`

#### 6.4.3 DescribeRiskCheckSummary

Queries the summary information about the check results of cloud service configurations. The operation returns the following information: the number of risk items, the risk rate, the number of affected assets, the last check time, and the statistics of each type of check items.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckSummary | The operation that you want to perform. Set the value to DescribeRiskCheckSummary. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| ResourceDirecto ryAccountId | String | No | None | This parameter is deprecated. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 291B49F9-1685- 4005-****- 606B6F78740F | The ID of the request. |

| RiskCheckSum mary | Struct |   | The summary information about the check results of cloud service configurations. |
|---|---|---|---|
| AffectedAsset Count | Integer | 0 | The number of affected assets. |
| DisabledRiskC ount | Integer | 0 | The number of the check items that fail the check. |
| EnabledRiskCo unt | Integer | 3 | The number of the check items that pass the check. |
| Groups | Array of group |   | An array that consists of the statistics of each type of check item. |
| CountByStatus | Array of statusCount |   | An array that consists of the statistics of check items. |
| Count | Integer | 2 | The number of detected risk items. |
| Status | String | pass | The status of a check item after the check is finished. Valid values: pass: The check item passes the check, which indicates that the check item is normal. failed: The check item fails the check, which indicates that risks are detected for the check item. |
| Id | Long | 1 | The type ID of the check item. |
| RemainingTim e | Integer | 0 | The time when the next check will be performed. |
| Sort | Integer | 1 | The sequence number of the check item type in the All Types drop-down list in the console. |
| Status | String | finish | The status of the check. Valid values: finish: The check is finished. running: The check is in process. waiting: The check is pending. notStart: The check is not started. |
| Title | String | Identity authentication and permissions | The type of the check items. |

| ItemCount | Integer | 4 | The number of check items. |
|---|---|---|---|
| PreviousCount | Integer | 0 | The number of detected risk items in the last check. |
| PreviousTime | Long | 1545012926000 | The time when the last check was performed. The value is a UNIX timestamp. Unit: milliseconds. |
| RiskCount | Integer | 1 | The number of detected risk items. |
| RiskLevelCoun t | Array of levelCount |   | The number of check items at each risk level. Valid values: high medium low |
| Count | Integer | 1 | The number of risk items of the risk level. |
| Key | String | medium | The risk level of a check item. |
| RiskRate | Float | 0.25 | The proportion of risk items to all check items. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckSummary &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>291B49F9-1685-4005-****-606B6F78740F</RequestId> <RiskCheckSummary>
    <DisabledRiskCount>0</DisabledRiskCount>
    <PreviousTime>1545012926000</PreviousTime>
    <RiskRate>0.25</RiskRate>
    <ItemCount>4</ItemCount>
    <PreviousCount>0</PreviousCount>
    <EnabledRiskCount>3</EnabledRiskCount>
    <AffectedAssetCount>0</AffectedAssetCount>
    <RiskCount>1</RiskCount>
    <Groups>
        <Status>finish</Status>
        <RemainingTime>0</RemainingTime>
        <Sort>1</Sort>
        <Title>Identity authentication and permissions</Title>
        <Id>1</Id>
        <CountByStatus>
            <Status>pass</Status>
            <Count>2</Count>
        </CountByStatus>
    </Groups>
    <RiskLevelCount>
        <Count>1</Count>
        <Key>medium</Key>
    </RiskLevelCount>
</RiskCheckSummary>
```

`JSON` format `{`

```json
    "RequestId": "291B49F9-1685-4005-****-606B6F78740F",
    "RiskCheckSummary": {
        "DisabledRiskCount": 0,
        "PreviousTime": 1545012926000,
        "RiskRate": 0.25,
        "ItemCount": 4,
        "PreviousCount": 0,
        "EnabledRiskCount": 3,
        "AffectedAssetCount": 0,
        "RiskCount": 1,
        "Groups": {
            "Status": "finish",
            "RemainingTime": 0,
            "Sort": 1,
            "Title": "Identity authentication and permissions",
            "Id": 1,
            "CountByStatus": {
                "Status": "pass",
                "Count": 2
```

`}` `},`

```json
        "RiskLevelCount": {
            "Count": 1,
            "Key": "medium"
```

`}` `}` `}`

#### 6.4.4 DescribeRiskCheckResult

Queries the check results of cloud service configurations by check item type or name.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeRiskChe ckResult | The operation that you want to perform. Set the value to DescribeRiskCheckResult. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| GroupId | Long | No | 21000 | The type ID of the check item. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| RiskLevel | String | No | high | The risk level of the check item. Valid values: high medium low |
| Status | String | No | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| ItemIds.N | RepeatL ist | No | sde*** | The ID of the check item. |
| AssetType | String | No | RDS | The type of the cloud service. Valid values: RDS: ApsaraDB RDS ECS: Elastic Compute Service (ECS) OSS: Object Storage Service (OSS) MongoDB: ApsaraDB for MongoDB Redis: KVStore for Redis |
| Name | String | No | Cloud platform - MFA configuration of Apsara Stack tenant accounts | The name of the check item. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| QueryFlag | String | No | None | This parameter is deprecated. |
| regionId | String | No | hangzhou** | The ID of the region. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| List | Array of RiskCheckRes ultForDisplay |   | An array that consists of the information about the check item. |
| AffectedCount | Integer | 0 | The number of affected assets. |
| CheckTime | Long | 1543991525000 | The time when the last check was performed. The value is a UNIX timestamp. Unit: milliseconds. |
| ItemId | Long | 1 | The ID of the check item. |
| RemainingTim e | Integer | 0 | This parameter is deprecated. |
| RepairStatus | String | disabled | Indicates whether the risk of the check item can be fixed. Valid values: enabled: yes disabled: no |
| RiskAssertTyp e | String | ECS | The type of the affected asset. |
| RiskItemResou rces | Array of RiskItemResou rce |   | An array that consists of the details about the check item. |
| ContentResour ce | Json | { "type": "link", "value": "Risk: MFA is disabled\n", "url": "https://***.aliyun.c om/#/secure\n" } | The content in the check item details. |
| ResourceNam e | String | bestPractice | The title in the check item details. Valid values: bestPractice: description influence: risk suggestion: solution helpResource: reference |

| RiskLevel | String | high | The risk level of the check item. Valid values: high medium low |
|---|---|---|---|
| Sort | Integer | 1 | The sequence number of the check result. |
| StartStatus | String | enabled | Indicates whether the check item is supported. Valid values: enabled: yes disable: no |
| Status | String | pass | The status of the check result. Valid values: pass failed running waiting ignored falsePositive |
| TaskId | Long | 7 | The ID of the check task. |
| Title | String | Cloud platform - MFA configuration of Apsara Stack tenant accounts | The title of the check item. |
| Type | String | Identity authentication and permissions | The type of the check item. |
| PageCount | Integer | 20 | The total number of pages returned. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | AD271C07-4ACE- ***-AA9B- F14FD3B7717F | The ID of the request. |
| TotalCount | Integer | 12 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeRiskCheckResult &<Common request parameters>
```

Sample success responses `XML` format

```json
<TotalCount>12</TotalCount> <PageSize>10</PageSize> <PageCount>20</PageCount> <RequestId>AD271C07-4ACE-***-AA9B-F14FD3B7717F</RequestId> <CurrentPage>1</CurrentPage> <List>
    <RiskAssertType>ECS</RiskAssertType>
    <Status>pass</Status>
    <CheckTime>1543991525000</CheckTime>
    <StartStatus>enabled</StartStatus>
    <Type>Identity authentication and permissions</Type>
    <TaskId>7</TaskId>
    <RemainingTime>0</RemainingTime>
    <AffectedCount>0</AffectedCount>
    <Sort>1</Sort>
    <Title>Cloud platform - MFA configuration of Apsara Stack tenant accounts</Title>
    <RepairStatus>disabled</RepairStatus>
    <RiskLevel>high</RiskLevel>
    <ItemId>1</ItemId>
    <RiskItemResources>
        <ContentResource>{   "type": "link",   "value": "Risk: MFA is disabled\n",
"url": "https://***.aliyun.com/#/secure\n" }</ContentResource>
        <ResourceName>bestPractice</ResourceName>
    </RiskItemResources>
</List> <Count>10</Count>
```

`JSON` format `{`

```json
    "TotalCount": 12,
    "PageSize": 10,
    "PageCount": 20,
    "RequestId": "AD271C07-4ACE-***-AA9B-F14FD3B7717F",
    "CurrentPage": 1,
    "List": {
        "RiskAssertType": "ECS",
        "Status": "pass",
        "CheckTime": 1543991525000,
        "StartStatus": "enabled",
        "Type": "Identity authentication and permissions",
        "TaskId": 7,
        "RemainingTime": 0,
        "AffectedCount": 0,
        "Sort": 1,
        "Title": "Cloud platform - MFA configuration of Apsara Stack tenant accounts",
        "RepairStatus": "disabled",
        "RiskLevel": "high",
        "ItemId": 1,
        "RiskItemResources": {
            "ContentResource": "{   \"type\": \"link\",   \"value\": \"Risk: MFA is disa
bled\\n\", \"url\": \"https://***.aliyun.com/#/secure\\n\" }",
            "ResourceName": "bestPractice"
```

`}` `},`

```json
    "Count": 10
```

`}`

#### 6.4.5 DescribeSecurityCheckScheduleConfig

Queries the custom check cycle and time period.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeSecurit yCheckSchedule Config | The operation that you want to perform. Set the value to DescribeSecurityCheckScheduleC onfig. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 48D2E9A9-A1B0- 4295-****- 0995757C47E9 | The ID of the request. |
| RiskCheckJobC onfig | Struct |   | The settings of scheduled check tasks. |
| DaysOfWeek | String | 1,2,3 | The day of the week when the check tasks are performed. You can specify multiple days. Separate multiple values with commas (,). Valid values: 1: Monday 2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday |
| EndTime | Integer | 12 | The time range during which the check tasks end. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |
| StartTime | Integer | 6 | The time range during which the check tasks start. Valid values: 6: 00:00 to 06:00 12: 06:00 to 12:00 18: 12:00 to 18:00 24: 18:00 to 24:00 |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeSecurityCheckScheduleConfig &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RiskCheckJobConfig>
    <DaysOfWeek>1,2,3</DaysOfWeek>
    <EndTime>12</EndTime>
    <StartTime>6</StartTime>
</RiskCheckJobConfig> <RequestId>48D2E9A9-A1B0-4295-****-0995757C47E9</RequestId>
```

`JSON` format `{`

```json
    "RiskCheckJobConfig": {
        "DaysOfWeek": "1,2,3",
        "EndTime": 12,
        "StartTime": 6
```

`},`

```json
    "RequestId": "48D2E9A9-A1B0-4295-****-0995757C47E9"
```

`}`

### 6.5 Vulnerability management

#### 6.5.1 DescribeVulList

Queries vulnerabilities by type.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulList | The operation that you want to perform. Set the value to DescribeVulList. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| Remark | String | No | 47.200.XX.XX | The tag to query, which can be the internal IP address, public IP address, or name of the asset. |
| GroupId | String | No | 9207613 | The ID of the asset group. |

| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|---|
| Uuids | String | No | 1587bedb-fdb4- 48c4-9330- ************ | The UUIDs of assets. Separate multiple UUIDs with commas (,). |
| AliasName | String | No | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| Level | String | No | serious | The severity of the vulnerability. Valid values: serious high medium low |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerabilities. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: yes n: no |
| BatchName | String | No | Test | The name that identifies the group of vulnerabilities. |
| Resource | String | No | vulnerability | The source of the group of vulnerabilities. Valid values: vulnerability and host. |
| CreateTsStart | Long | No | 1512949391000 | The beginning of the creation time. The value is a UNIX timestamp. Unit: milliseconds. |

| CreateTsEnd | Long | No | 1512949392000 | The end of the creation time. The value is a UNIX timestamp. Unit: milliseconds. |
|---|---|---|---|---|
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| ModifyTsStart | Long | No | 1512949391000 | The beginning of the time range during which the vulnerability is modified. The value is a UNIX timestamp. Unit: milliseconds. |
| ModifyTsEnd | Long | No | 1512949392000 | The end of the time range during which the vulnerability is modified. The value is a UNIX timestamp. Unit: milliseconds. |
| AttachTypes | String | No | sca | The additional type of vulnerability. You can specify this parameter when you query application vulnerabilities. If Type is set to app, you must specify this parameter. Set the value to sca. |
| ContainerFieldN ame | String | No | None | This parameter is deprecated. |
| ContainerFieldV alue | String | No | None | This parameter is deprecated. |
| TargetType | String | No | groupId | The type of the asset to query. Valid values: groupId: the ID of an asset group. uuid: the UUID of an asset. |
| ClusterId | String | No | Test cluster 1 | The ID of the cluster. |
| MinScore | Integer | No | 100 | The minimum score. |
| VpcInstanceIds | String | No | vpc-xxx | The ID of the virtual private cloud (VPC). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | ECDE6715-6286- 40E6-A32D- 3094051FD74D | The ID of the request. |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| VulRecords | Array of VulRecord |   | An array that consists of the information about the vulnerability. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| ContainerId | String | None | This parameter is deprecated. |
| ContainerImag eId | String | None | This parameter is deprecated. |
| ContainerImag eName | String | None | This parameter is deprecated. |
| ContainerInner Path | String | None | This parameter is deprecated. |
| ContainerNam e | String | None | This parameter is deprecated. |
| ExtendContent Json | Struct |   | The extended information. |
| AbsolutePath | String | /roo/www/web | The absolute path. |
| AliasName | String | RHSA-2017:0574: gnutls security, bug fix, and enhancement update | The alias of the vulnerability. |
| Ip | String | 47.200.XX.XX | The IP address of the asset that is associated with the vulnerability. By default, the public IP address is displayed. If the public IP address does not exist, the private IP address is displayed. |
| LastTs | Long | 1554189334000 | The timestamp when the vulnerability is last detected. Unit: milliseconds. |

| Necessity | Struct |   | The priority to fix the vulnerability. |
|---|---|---|---|
| Assets factor _ | String | 1 | The asset score. |
| Cvss factor _ | String | 7.8 | The Common Vulnerability Scoring System (CVSS) score. |
| Enviroment fa _ ctor | String | 1.0 | The environmental score. |
| Is calc _ | String | 1 | Indicates whether the vulnerability severity score is calculated. Valid values: 0: no 1: yes |
| Status | String | normal | The status of the vulnerability severity score. Valid values: none: No score is generated. pending: The score is pending calculation. miss: The score failed to be calculated. normal: The calculation is normal. |
| Time factor _ | String | 1.0 | The temporal score. |
| Total score _ | String | 7.8 | The total vulnerability severity score. |
| Os | String | centos | The operating system. |
| OsRelease | String | 7 | The version of the operating system. |
| PrimaryId | Long | 111 | The ID of the vulnerability. |
| RpmEntityList | Array of RpmEntity |   | An array that consists of the information about RPM Package Manager (RPM) packages. |
| FullVersion | String | 3.10.0-693.2.2.el7 | The complete version number. |
| MatchDetail | String | python-perf version less than 0:3.10.0- 693.21.1.el7 | The matching details. |

| Name | String | python-perf | The name of the RPM package. |
|---|---|---|---|
| Path | String | /usr/lib64/python2. 7/site-packages | The path. |
| UpdateCmd | String | *** update python- perf | The command that is used to fix the vulnerability. |
| Version | String | 3.10.0 | The version number. |
| Status | String | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag that is added to the vulnerability. |
| cveList | List | ["CVE-2016-8610", "CVE-2017-5335" ] | The Common Vulnerabilities and Exposures (CVE) list. |
| FirstTs | Long | 1554189334000 | The time when the vulnerability was first detected. The value is a UNIX timestamp. Unit: milliseconds. |
| GroupId | Integer | 281801 | The ID of the asset group. |
| InstanceId | String | i-bp18t*** | The ID of the asset. |
| InstanceName | String | Test ECS instance | The name of the asset. |
| InternetIp | String | 47.200.XX.XX | The public IP address of the asset. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address of the asset. |

| wareness |   |   | er Developer Guide·Threat Dete tion Service (TDS |
|---|---|---|---|

| K8sClusterId | String | None | This parameter is deprecated. |
|---|---|---|---|
| K8sNamespac e | String | None | This parameter is deprecated. |
| K8sNodeId | String | None | This parameter is deprecated. |
| K8sNodeName | String | None | This parameter is deprecated. |
| K8sPodName | String | None | This parameter is deprecated. |
| LastTs | Long | 1541207563000 | The timestamp when the vulnerability was last detected. Unit: milliseconds. |
| ModifyTs | Long | 1541207563000 | The timestamp when the vulnerability was modified. Unit: milliseconds. |
| Name | String | oval:com.redhat.rh sa:def:20170574 | The name of the vulnerability. |
| Necessity | String | asap | The priority to fix the vulnerability. Valid values: asap: high later: medium nntf: low |
| Online | Boolean | true | Indicates whether the asset is online. Valid values: true: yes false: no |
| OsVersion | String | linux | The version of the operating system. |
| PrimaryId | Long | 101162078 | The ID of the vulnerability. |
| Related | String | CVE-2017- 7518,CVE-2017- 12188 | The list of CVEs related to the vulnerability. Multiple CVEs are separated by commas (,). |
| RepairTs | Long | 1541207563000 | The timestamp when the vulnerability was fixed. Unit: milliseconds. |

| ResultCode | String | 0 | The code returned after the vulnerability is fixed. |
|---|---|---|---|
| ResultMessage | String | timeout | The message returned after the vulnerability is fixed. |
| Status | Integer | 1 | The status of the vulnerability. Valid values: 1: unfixed 2: fix failed 3: rollback failed 4: fixing 5: rolling back 6: verifying 7: fixed 8: fixed and to be restarted 9: rolled back 10: ignored 11: rolled back and to be restarted 12: not found 20: expired |
| Tag | String | oval | The tag that is added to the vulnerability. |
| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities emg: urgent vulnerabilities app: application vulnerabilities |
| Uuid | String | 04c56617-23fc- 43a5-ab9b- ************ | The UUID of the asset. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>ECDE6715-6286-40E6-A32D-3094051FD74D</RequestId> <VulRecords>
```

```xml
    <K8sNodeId>None</K8sNodeId>
    <K8sNodeName>None</K8sNodeName>
    <OsVersion>linux</OsVersion>
    <ContainerInnerPath>None</ContainerInnerPath>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <K8sClusterId>None</K8sClusterId>
    <Name>oval:com.redhat.rhsa:def:20170574</Name>
    <K8sNamespace>None</K8sNamespace>
    <RepairTs>1541207563000</RepairTs>
    <ModifyTs>1541207563000</ModifyTs>
    <InternetIp>47.200.XX.XX</InternetIp>
    <ContainerId>None</ContainerId>
    <ContainerName>None</ContainerName>
    <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
    <Status>1</Status>
    <InstanceId>i-bp18t***</InstanceId>
    <Necessity>asap</Necessity>
    <LastTs>1541207563000</LastTs>
    <K8sPodName>None</K8sPodName>
    <ResultMessage>timeout</ResultMessage>
    <ContainerImageId>None</ContainerImageId>
    <GroupId>281801</GroupId>
    <InstanceName>Test ECS instance</InstanceName>
    <FirstTs>1554189334000</FirstTs>
    <Type>cve</Type>
    <Related>CVE-2017-7518,CVE-2017-12188</Related>
    <Uuid>04c56617-23fc-43a5-ab9b-************</Uuid>
    <ContainerImageName>None</ContainerImageName>
    <Tag>oval</Tag>
    <Online>true</Online>
    <ResultCode>0</ResultCode>
    <PrimaryId>101162078</PrimaryId>
    <ExtendContentJson>
        <Status>1</Status>
        <Os>centos</Os>
        <Ip>47.200.XX.XX</Ip>
        <AliasName>RHSA-2017:0574: gnutls security, bug fix, and enhancement
update</AliasName>
        <LastTs>1554189334000</LastTs>
        <Tag>oval</Tag>
        <AbsolutePath>/roo/www/web</AbsolutePath>
        <OsRelease>7</OsRelease>
        <PrimaryId>111</PrimaryId>
        <RpmEntityList>
            <Path>/usr/lib64/python2.7/site-packages</Path>
            <UpdateCmd>*** update python-perf</UpdateCmd>
            <Version>3.10.0</Version>
            <FullVersion>3.10.0-693.2.2.el7</FullVersion>
            <MatchDetail>python-perf version less than 0:3.10.0-
693.21.1.el7</MatchDetail>
            <Name>python-perf</Name>
        </RpmEntityList>
        <cveList>["CVE-2016-8610", "CVE-2017-5335" ]</cveList>
```

```xml
        <Necessity>
            <Total_score>7.8</Total_score>
            <Status>normal</Status>
            <Time_factor>1.0</Time_factor>
            <Cvss_factor>7.8</Cvss_factor>
            <Is_calc>1</Is_calc>
            <Enviroment_factor>1.0</Enviroment_factor>
            <Assets_factor>1</Assets_factor>
        </Necessity>
    </ExtendContentJson>
</VulRecords> <CurrentPage>1</CurrentPage>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "ECDE6715-6286-40E6-A32D-3094051FD74D",
    "VulRecords": {
        "K8sNodeId": "None",
        "K8sNodeName": "None",
        "OsVersion": "linux",
        "ContainerInnerPath": "None",
        "IntranetIp": "192.168.XX.XX",
        "K8sClusterId": "None",
        "Name": "oval:com.redhat.rhsa:def:20170574",
        "K8sNamespace": "None",
        "RepairTs": 1541207563000,
        "ModifyTs": 1541207563000,
        "InternetIp": "47.200.XX.XX",
        "ContainerId": "None",
        "ContainerName": "None",
        "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement update"
```

`,`

```json
        "Status": 1,
        "InstanceId": "i-bp18t***",
        "Necessity": "asap",
        "LastTs": 1541207563000,
        "K8sPodName": "None",
        "ResultMessage": "timeout",
        "ContainerImageId": "None",
        "GroupId": 281801,
        "InstanceName": "Test ECS instance",
        "FirstTs": 1554189334000,
        "Type": "cve",
        "Related": "CVE-2017-7518,CVE-2017-12188",
        "Uuid": "04c56617-23fc-43a5-ab9b-************",
        "ContainerImageName": "None",
        "Tag": "oval",
        "Online": true,
        "ResultCode": 0,
        "PrimaryId": 101162078,
"ExtendContentJson":{
```

```json
        ExtendContentJson: {
            "Status": 1,
            "Os": "centos",
            "Ip": "47.200.XX.XX",
            "AliasName": "RHSA-2017:0574: gnutls security, bug fix, and enhancement upd
ate",
            "LastTs": 1554189334000,
            "Tag": "oval",
            "AbsolutePath": "/roo/www/web",
            "OsRelease": 7,
            "PrimaryId": 111,
            "RpmEntityList": {
                "Path": "/usr/lib64/python2.7/site-packages",
                "UpdateCmd": "*** update python-perf",
                "Version": "3.10.0",
                "FullVersion": "3.10.0-693.2.2.el7",
                "MatchDetail": "python-perf version less than 0:3.10.0-693.21.1.el7",
                "Name": "python-perf"
```

`},`

```json
            "cveList": "[\"CVE-2016-8610\", \"CVE-2017-5335\" ]",
            "Necessity": {
                "Total_score": 7.8,
                "Status": "normal",
                "Time_factor": 1,
                "Cvss_factor": 7.8,
                "Is_calc": 1,
                "Enviroment_factor": 1,
                "Assets_factor": 1
```

`}` `}` `},`

```json
    "CurrentPage": 1
```

`}`

#### 6.5.2 DescribeVulWhitelist

Queries the whitelist of vulnerabilities by page.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeVulWhit elist | The operation that you want to perform. Set the value to DescribeVulWhitelist. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| PageSize | Integer | No | 10 | The number of entries to return on each page. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 74F97EF7-B543- 43FD-XXXX- 18456731F9C5 | The ID of the request. |
| TotalCount | Integer | 1 | The total number of entries returned. |
| VulWhitelists | Array of VulWhitelist |   | An array that consists of the information about the vulnerability whitelist. |
| AliasName | String | RHSA-xxxx | The alias of the vulnerability. |
| Name | String | oval:com.redh.xxx xx | The name of the vulnerability. |
| Reason | String | Not urgent | The reason why you add the vulnerability to the whitelist. |
| Type | String | cve | The type of the vulnerability. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeVulWhitelist &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>1</TotalCount> <PageSize>10</PageSize> <RequestId>74F97EF7-B543-43FD-XXXX-18456731F9C5</RequestId> <VulWhitelists>
    <Type>cve</Type>
    <AliasName>RHSA-xxxx</AliasName>
    <Reason>Not urgent</Reason>
    <Name>oval:com.redh.xxxxx</Name>
</VulWhitelists> <CurrentPage>1</CurrentPage>
```

`JSON` format `{`

```json
    "TotalCount": 1,
    "PageSize": 10,
    "RequestId": "74F97EF7-B543-43FD-XXXX-18456731F9C5",
    "VulWhitelists": {
        "Type": "cve",
        "AliasName": "RHSA-xxxx",
        "Reason": "Not urgent",
        "Name": "oval:com.redh.xxxxx"
```

`},`

```json
    "CurrentPage": 1
```

`}`

#### 6.5.3 DescribeConcernNecessity

Queries the priorities to fix vulnerabilities.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeConcer nNecessity | The operation that you want to perform. Set the value to DescribeConcernNecessity. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| ConcernNeces sity | List | [ "asap", "later", "nntf"] | The priorities to fix the vulnerabilities. Valid values: asap: high later: medium nntf: low |
|---|---|---|---|
| RequestId | String | 9139DAF6-5CE0- 49A0-XXXX- 07243A290F70 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeConcernNecessity &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>9139DAF6-5CE0-49A0-XXXX-07243A290F70</RequestId> <ConcernNecessity>[ "asap", "later", "nntf"]</ConcernNecessity>
```

`JSON` format `{`

```json
    "RequestId": "9139DAF6-5CE0-49A0-XXXX-07243A290F70",
    "ConcernNecessity": "[ \"asap\", \"later\", \"nntf\"]"
```

`}`

#### 6.5.4 DescribeGroupedVul

Queries information about vulnerabilities by group.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeGroupe dVul | The operation that you want to perform. Set the value to DescribeGroupedVul. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

| Type | String | No | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|---|
| Uuids | String | No | d42f938c-d962- 48a0-90f9- 05e4ea****** | The UUIDs of assets. Separate multiple UUIDs with commas (,). |
| AliasName | String | No | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| Necessity | String | No | asap,later,nntf | The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values: asap: high later: medium nntf: low |
| Dealed | String | No | n | Specifies whether the vulnerability is handled. Valid values: y: yes n: no |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| GroupId | String | No | weds**** | The ID of the asset group. |
| ContainerFieldN ame | String | No | XXX | The name of the container filed. |
| ContainerFieldV alue | String | No | XXX | The value of the container filed. |
| TargetType | String | No | groupId | The type of the asset to query. Valid values: groupId: the ID of an asset group. uuid: the UUID of an asset. |
| ClusterId | String | No | Test 1 | The ID of the cluster. |

| MinScore | Integer | No | 100 | The minimum score. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 0DFCADBA-7065- 42DA-XXXX- 6868B9C2A8CF | The ID of the request. |
| TotalCount | Integer | 2 | The total number of entries returned. |
| GroupedVulIte ms | Array of GroupedVulIte m |   | An array that consists of the information about vulnerabilities by group. |
| AliasName | String | RHSA-2019:***- Important: polkit security update | The alias of the vulnerability. |
| AsapCount | Integer | 0 | The number of vulnerabilities that have the high priority. |
| GmtLast | Long | 1554185744000 | The time when the vulnerability was last detected. The value is a UNIX timestamp. Unit: milliseconds. |
| HandledCount | Integer | 0 | The number of handled vulnerabilities. |
| LaterCount | Integer | 0 | The number of vulnerabilities that have the medium priority. |
| Name | String | ***glibc security and bug fixes | The name of the vulnerability. |
| NntfCount | Integer | 59 | The number of vulnerabilities that have the low priority. |
| Tags | String | Restart required | The tag that is added to the vulnerability. |
| TotalFixCount | Long | 0 | The total number of fixed vulnerabilities. |

| Type | String | cve | The type of the vulnerability. Valid values: cve: Linux software vulnerabilities sys: Windows system vulnerabilities cms: Web-CMS vulnerabilities app: application vulnerabilities emg: urgent vulnerabilities |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeGroupedVul &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>2</TotalCount> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <GroupedVulItems>
    <Type>cve</Type>
    <LaterCount>0</LaterCount>
    <GmtLast>1554185744000</GmtLast>
    <HandledCount>0</HandledCount>
    <AliasName>RHSA-2019:***-Important: polkit security update</AliasName>
    <AsapCount>0</AsapCount>
    <TotalFixCount>0</TotalFixCount>
    <NntfCount>59</NntfCount>
    <Tags>Restart required</Tags>
    <Name>***glibc security and bug fixes</Name>
</GroupedVulItems>
```

`JSON` format `{`

```json
    "TotalCount": 2,
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-XXXX-6868B9C2A8CF",
    "CurrentPage": 1,
    "GroupedVulItems": {
        "Type": "cve",
        "LaterCount": 0,
        "GmtLast": 1554185744000,
        "HandledCount": 0,
        "AliasName": "RHSA-2019:***-Important: polkit security update",
        "AsapCount": 0,
        "TotalFixCount": 0,
        "NntfCount": 59,
        "Tags": "Restart required",
        "Name": "***glibc security and bug fixes"
```

`}` `}`

#### 6.5.5 DescribeAutoDelConfig

Queries the configurations for automatic vulnerability deletion.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeAutoDel Config | The operation that you want to perform. Set the value to DescribeAutoDelConfig. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Days | Integer | 7 | The number of days that a detected vulnerability is retained. Unit: days. |
| RequestId | String | 43186B14-5A39- 44E0-XXXX- 8B24D1EF82CC | The ID of the request. |

**Examples**

Sample requests

```
/?Action=DescribeAutoDelConfig &<Common request parameters>
```

Sample success responses `XML` format

```xml
<RequestId>43186B14-5A39-44E0-XXXX-8B24D1EF82CC</RequestId> <Days>7</Days>
```

`JSON` format `{`

```json
    "RequestId": "43186B14-5A39-44E0-XXXX-8B24D1EF82CC",
    "Days": 7
```

`}`

### 6.6 Baseline check

#### 6.6.1 DescribeCheckWarningSummary

Queries the statistical information about baseline check results. The information includes the number of servers on which a baseline check is performed, the number of baseline check items, and the pass rate of check items in the last baseline check.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningSummary | Set the value to DescribeCheckWarningSummary. |
| SourceIp | String | No | 1.2.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| TypeName | String | No | database | The type of check items. |
| Status | String | No | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |

| RiskStatus | Integer | No | 1 | The status of the check item. Valid values: 1: failed 3: passed |
|---|---|---|---|---|
| RiskName | String | No | Redis security baseline check | The name of the risk item. |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| Uuids | String | No | f03259d8-1e81- 4fae-bcbb- 275fb5****** | The ID of the server on which the baseline check is performed. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |
| RequestId | String | 00BD7CE2-284A- 4534-BD09-*** | The ID of the request. |
| TotalCount | Integer | 100 | The total number of baseline check items. |
| WarningSumm arys | Array of WarningSumm ary |   | The statistics of check items. |
| CheckCount | Integer | 10 | The number of check items. |
| HighWarningC ount | Integer | 1 | The number of high-risk items. |
| LastFoundTim e | String | 2019-01-01 12:23:00 | The time when the last baseline check was performed. |

| Level | String | high | The severity of the risk item. Valid values: high medium low |
|---|---|---|---|
| LowWarningCo unt | Integer | 3 | The number of low-risk items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk items. |
| RiskId | Long | 1 | The ID of the risk item. |
| RiskName | String | Redis password | The name of the risk item. |
| SubTypeAlias | String | Redis | The sub-type type of the risk item. |
| TypeAlias | String | Database | The type of the check item. Valid values: database, system, weak password, and middleware. |
| WarningMachi neCount | Integer | 11 | The number of assets on which risk items are detected. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningSummary &Lang=zh &TypeName=database &Status=1 &RiskStatus=1 &RiskName=Redis security baseline check &StrategyId=1 &Uuids=f03259d8-1e81-4fae-bcbb-275fb5****** &CurrentPage=1 &PageSize=20 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeCheckWarningSummary>
   <TotalCount>25</TotalCount>
   <PageSize>20</PageSize>
   <RequestId>DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD</RequestId>
   <CurrentPage>1</CurrentPage>
   <Count>20</Count>
```

`W` `i` `S`

```xml
   <WarningSummarys>
      <RiskId>43</RiskId>
      <LastFoundTime>2019-04-10 00:33:00</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>3</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>8</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>
   CentOS Linux 7 security baseline check
                              </SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>
   CentOS Linux 7 security baseline check
                              </RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>47</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>7</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance (Level-3 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance (Level-3 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>48</RiskId>
      <LastFoundTime>2019-04-10 00:58:11</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>2</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>6</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 7 security standard compliance (Level-2 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 7 security standard compliance (Level-2 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>3</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
<CheckCount>1</CheckCount>
```

```xml
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Redis security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Redis security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>19</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Linux weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>12</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Anonymous FTP logon</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Anonymous FTP logon</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>13</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>1</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>1</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Windows weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>23</RiskId>
      <LastFoundTime>2019-04-10 14:00:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>8</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
```

`e``e`

```xml
edu /ee
      <TypeAlias>Middleware</TypeAlias>
      <SubTypeAlias>Apache Tomcat security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Apache Tomcat security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>2</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>PostgreSQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>PostgreSQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>11</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>MySQL weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>MySQL weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>20</RiskId>
      <LastFoundTime>2019-04-10 08:31:32</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>FTP weak password</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>FTP weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>17</RiskId>
      <LastFoundTime>2019-04-10 06:58:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>1</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>Weak password</TypeAlias>
      <SubTypeAlias>Microsoft SQL Server weak password</SubTypeAlias>
```

```xml
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Microsoft SQL Server weak password</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>24</RiskId>
      <LastFoundTime>2019-04-10 06:52:05</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>2</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>Database</TypeAlias>
      <SubTypeAlias>Memcached security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Memcached security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>42</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>49</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance (Level-2 classified sec
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance (Level-2 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>50</RiskId>
      <LastFoundTime>2019-02-19 14:59:17</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>CentOS Linux 6 security standard compliance (Level-3 classified sec
```

```xml
urity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>CentOS Linux 6 security standard compliance (Level-3 classified
security protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>55</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>14</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance (Level-2 classified secur
ity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance (Level-2 classified security
protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>56</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>15</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>medium</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security standard compliance (Level-3 classified secur
ity protection)</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security standard compliance (Level-3 classified security
protection)</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>54</RiskId>
      <LastFoundTime>2019-02-19 12:57:23</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>16</CheckCount>
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Linux Ubuntu security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Linux Ubuntu security baseline check</RiskName>
   </WarningSummarys>
   <WarningSummarys>
      <RiskId>51</RiskId>
      <LastFoundTime>2019-02-19 12:44:58</LastFoundTime>
      <MediumWarningCount>0</MediumWarningCount>
      <WarningMachineCount>0</WarningMachineCount>
      <CheckCount>12</CheckCount>
```

`/`

```xml
      <HighWarningCount>0</HighWarningCount>
      <Level>high</Level>
      <TypeAlias>System</TypeAlias>
      <SubTypeAlias>Windows 2012 R2 security baseline check</SubTypeAlias>
      <LowWarningCount>0</LowWarningCount>
      <RiskName>Windows 2012 R2 security baseline check</RiskName>
   </WarningSummarys>
</DescribeCheckWarningSummary>
```

`JSON` format `{`

```json
 "TotalCount":25,
 "PageSize":20,
 "RequestId":"DFA6CDC5-E826-4D18-A499-BEF9DA31F1AD",
 "CurrentPage":1,
 "Count":20,
 "WarningSummarys":[
```

`{`

```json
   "RiskId":43,
   "LastFoundTime":"2019-04-10 00:33:00",
   "MediumWarningCount":0,
   "WarningMachineCount":3,
   "CheckCount":16,
   "HighWarningCount":8,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security baseline check\n
\n ",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security baseline check\n
\n "
```

`},` `{`

```json
   "RiskId":47,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":15,
   "HighWarningCount":7,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-3",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security standard compliance (Level-3 classified security
protection)"
```

`},` `{`

```json
   "RiskId":48,
   "LastFoundTime":"2019-04-10 00:58:11",
   "MediumWarningCount":0,
   "WarningMachineCount":2,
   "CheckCount":12,
   "HighWarningCount":6,
```

```json
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 7 security standard compliance - MLPS level-2",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 7 security standard compliance (Level-2 classified security
protection)"
```

`},` `{`

```json
   "RiskId":3,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Database",
   "SubTypeAlias":"Redis security baseline check",
   "LowWarningCount":0,
   "RiskName":"Redis security baseline check",
```

`},` `{`

```json
   "RiskId":19,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Linux weak password",
   "LowWarningCount":0,
   "RiskName":"Linux weak password"
```

`},` `{`

```json
   "RiskId":12,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Anonymous FTP logon",
   "LowWarningCount":0,
   "RiskName":"Anonymous FTP logon"
```

`},` `{`

```json
   "RiskId":13,
   "LastFoundTime":"2019-04-10 06:58:58",
   "MediumWarningCount":0,
   "WarningMachineCount":1,
   "CheckCount":1,
   "HighWarningCount":1,
   "Level":"high",
```

```json
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Windows weak password",
   "LowWarningCount":0,
   "RiskName":"Windows weak password"
```

`},` `{`

```json
   "RiskId":23,
   "LastFoundTime":"2019-04-10 14:00:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":8,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"Middleware",
   "SubTypeAlias":"Apache Tomcat security baseline check",
   "LowWarningCount":0,
   "RiskName":"Apache Tomcat security baseline check"
```

`},` `{`

```json
   "RiskId":2,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"PostgreSQL weak password",
   "LowWarningCount":0,
   "RiskName":"PostgreSQL weak password"
```

`},` `{`

```json
   "RiskId":11,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"MySQL weak password",
   "LowWarningCount":0,
   "RiskName":"MySQL weak password"
```

`},` `{`

```json
   "RiskId":20,
   "LastFoundTime":"2019-04-10 08:31:32",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"FTP weak password",
```

`"L` `W` `i`

```
t"0
```

```json
   "LowWarningCount":0,
   "RiskName":"FTP weak password"
```

`},` `{`

```json
   "RiskId":17,
   "LastFoundTime":"2019-04-10 06:58:58",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":1,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"Weak password",
   "SubTypeAlias":"Microsoft SQL Server weak password",
   "LowWarningCount":0,
   "RiskName":"Microsoft SQL Server weak password"
```

`},` `{`

```json
   "RiskId":24,
   "LastFoundTime":"2019-04-10 06:52:05",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":2,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"Database",
   "SubTypeAlias":"Memcached security baseline check",
   "LowWarningCount":0,
   "RiskName":"Memcached security baseline check"
```

`},` `{`

```json
   "RiskId":42,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security baseline check",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 6 security baseline check"
```

`},` `{`

```json
   "RiskId":49,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security standard compliance (Level-2 classified secu
rity protection)",
   "LowWarningCount":0,
"RiskName":"CentOSLinux6securitystandardcompliance(Level-2classifiedsecurity
```

```
   RiskName:CentOS Linux 6 security standard compliance (Level2 classified security
protection)"
```

`},` `{`

```json
   "RiskId":50,
   "LastFoundTime":"2019-02-19 14:59:17",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"CentOS Linux 6 security standard compliance (Level-3 classified secu
rity protection)",
   "LowWarningCount":0,
   "RiskName":"CentOS Linux 6 security standard compliance (Level-3 classified security
protection)"
```

`},` `{`

```json
   "RiskId":55,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":14,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security standard compliance (Level-2 classified securi
ty protection)",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security standard compliance (Level-2 classified security p
rotection)"
```

`},` `{`

```json
   "RiskId":56,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":15,
   "HighWarningCount":0,
   "Level":"medium",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security standard compliance (Level-3 classified securi
ty protection)",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security standard compliance (Level-3 classified security p
rotection)"
```

`},` `{`

```json
   "RiskId":54,
   "LastFoundTime":"2019-02-19 12:57:23",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":16,
   "HighWarningCount":0,
```

`g` `g` `,`

```json
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"Linux Ubuntu security baseline check",
   "LowWarningCount":0,
   "RiskName":"Linux Ubuntu security baseline check"
```

`},` `{`

```json
   "RiskId":51,
   "LastFoundTime":"2019-02-19 12:44:58",
   "MediumWarningCount":0,
   "WarningMachineCount":0,
   "CheckCount":12,
   "HighWarningCount":0,
   "Level":"high",
   "TypeAlias":"System",
   "SubTypeAlias":"Windows 2012 R2 security baseline check",
   "LowWarningCount":0,
   "RiskName":"Windows 2012 R2 security baseline check"
```

`}` `]` `}`

#### 6.6.2 DescribeStratety

Queries the configurations of baseline check policies.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStratety | The operation that you want to perform. Set the value to DescribeStratety. |
| Lang | String | No | zh | The natural language of the request and response. Valid values: zh: Chinese en: English |
| SourceIp | String | No | 1.2.3.4 | The source IP address of the request. |
| StrategyIds | String | No | test1,test2,test3 | The IDs of the baseline check policies. Separate multiple IDs with commas (,). |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|

| RequestId | String | 16B9826C-B99F- 4F8A-8048- EA81D6D3DE8B | The ID of the request. |
|---|---|---|---|
| Strategies | Array |   | The information about the baseline check policy. |
| ConfigTargets | Array |   | The information about the group associated with the baseline check policy. |
| Flag | String | add | The related ID. |
| Target | String | 3259405 | The ID of the related group. |
| TargetType | String | groupId | The type of the related group. |
| CycleDays | Integer | 1 | The cycle of the baseline check. 1: every second day 3: every fourth day 7: every eighth day 30: every 31st day |
| CycleStartTim e | Integer | 6 | The time when the baseline check starts. Valid values: 0, 6, 12, and 18. |
| EcsCount | Integer | 5 | The number of servers on which baseline checks were performed based on the specified baseline check policy. |
| ExecStatus | Integer | 1 | The execution status of the baseline check. Valid values: 1: The baseline check is not running. 2: The baseline check is running. |
| Id | Integer | 212635 | The ID of the policy. |
| Name | String | test | The name of the policy. |
| PassRate | Integer | 80 | The pass rate of the latest baseline check. |
| ProcessRate | Integer | 80 | The progress of the baseline check. |
| RiskCount | Integer | 5 | The number of selected check items. |

| Type | Integer | 1 | The type of the baseline check policy. Valid values: 1: default policy 2: custom policy |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStratety ? Lang=zh &SourceIp=127.0.0.1 &StrategyIds=1,2,3 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribeStratety>
   <RequestId>ACAFE09B-3346-433B-BDA8-369AB3D9B4F9</RequestId>
   <Strategies>
      <CycleStartTime>6</CycleStartTime>
      <EcsCount>0</EcsCount>
      <Type>2</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>3</CycleDays>
      <Id>15161</Id>
      <ConfigTargets>
         <Target>4361221</Target>
         <TargetType>groupId</TargetType>
         <Flag>add</Flag>
      </ConfigTargets>
      <RiskCount>1</RiskCount>
      <Name>test</Name>
   </Strategies>
   <Strategies>
      <CycleStartTime>0</CycleStartTime>
      <EcsCount>17</EcsCount>
      <PassRate>81</PassRate>
      <Type>1</Type>
      <ExecStatus>1</ExecStatus>
      <ProcessRate>0</ProcessRate>
      <CycleDays>1</CycleDays>
      <Id>20</Id>
      <ConfigTargets>
         <Target>281801</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <ConfigTargets>
         <Target>4790960</Target>
         <TargetType>groupId</TargetType>
         <Flag>del</Flag>
      </ConfigTargets>
      <RiskCount>13</RiskCount>
      <Name>Default policy</Name>
   </Strategies>
</DescribeStratety>
```

`JSON` format `{`

```json
 "RequestId":"ACAFE09B-3346-433B-BDA8-369AB3D9B4F9",
 "Strategies":[
```

`{`

```json
   "Name":"test",
   "RiskCount":1,
   "CycleDays":3,
   "Type":2,
   "CycleStartTime":6,
   "ConfigTargets":[
```

`{`

```json
     "Flag":"add",
     "Target":"4361221",
     "TargetType":"groupId"
```

`}` `],`

```json
   "ProcessRate":0,
   "Id":15161,
   "ExecStatus":1,
   "EcsCount":0
```

`},` `{`

```json
   "Name":"Default policy",
   "RiskCount":13,
   "PassRate":81,
   "CycleDays":1,
   "Type":1,
   "CycleStartTime":0,
   "ConfigTargets":[
```

`{`

```json
     "Flag":"del",
     "Target":"281801",
     "TargetType":"groupId"
```

`},` `{`

```json
     "Flag":"del",
     "Target":"4790960",
     "TargetType":"groupId"
```

`}` `],`

```json
   "ProcessRate":0,
   "Id":20,
   "ExecStatus":1,
   "EcsCount":17
```

`}` `]` `}`

**Error codes**

For a list of error codes, see Error codes.

#### 6.6.3 DescribeStrategyExecDetail

Queries the details of the last baseline check by using a baseline check policy. The details include the time when the check was performed, the number of risk items, and the details of baseline risks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeStrateg yExecDetail | Set the value to DescribeStrategyExecDetail. |
| StrategyId | Integer | Yes | 1 | The ID of the baseline check policy. Note To query the results of a baseline check that uses a baseline check policy, you must specify the ID of the policy. |
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| EndTime | String | 2019-01-08 20:11:20 | The time when the baseline check ends. The time is in the yyyy-MM-dd HH:mm:ss format. |
| FailCount | Integer | 94 | The number of check items that failed to pass the baseline check. This type of check item is considered risk items. |
| FailedEcsList | Array of FailedEcs |   | An array consisting of the servers on which risk items were detected. |
| IP | String | 192.168.XX.XX | The IP address of the server on which the baseline check was performed. |
| InstanceName | String | Test-20180703 | The name of the server. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address. |

| Reason | String | Detect timeout | The failure cause for the check item. |
|---|---|---|---|
| InProcessCoun t | Integer | 0 | The number of baseline checks that are running. |
| Percent | String | 100% | The progress of the baseline check. |
| RequestId | String | 09322632-4668- 4AD9-****- 32757DEFBBA6 | The ID of the request. |
| Source | String | Manual | The type of the baseline check. Valid values: Schedule: automatic check that periodically runs Manual: intermediate check that is manually performed |
| StartTime | String | 2019-01-08 19:41:12 | The time when the baseline check starts. The time is in the yyyy-MM-dd HH:mm:ss format. |
| SuccessCount | Integer | 81 | The number of check items that passed the baseline check. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeStrategyExecDetail &StrategyId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<EndTime>2019-01-08 20:11:20</EndTime> <RequestId>09322632-4668-4AD9-BD0D-32757DEFBBA6</RequestId> <Percent>100%</Percent> <FailCount>94</FailCount> <StartTime>2019-01-08 19:41:12</StartTime> <SuccessCount>81</SuccessCount> <Source>Manual</Source> <FailedEcsList>
    <InstanceName>Test-20180703</InstanceName>
    <IP>192.168.XX.XX</IP>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <Reason>Detect timeout</Reason>
</FailedEcsList> <InProcessCount>0</InProcessCount>
```

`JSON` format `{`

```json
    "EndTime": "2019-01-08 20:11:20",
    "RequestId": "09322632-4668-4AD9-BD0D-32757DEFBBA6",
    "Percent": "100%",
    "FailCount": 94,
    "StartTime": "2019-01-08 19:41:12",
    "SuccessCount": 81,
    "Source": "Manual",
    "FailedEcsList": {
        "InstanceName": "Test-20180703",
        "IP": "192.168.XX.XX",
        "IntranetIp": "192.168.XX.XX",
        "Reason": "Detect timeout"
```

`},`

```json
    "InProcessCount": 0
```

`}`

#### 6.6.4 DescribeCheckWarnings

Queries specified risk items and check items of a specified server.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arnings | Set the value to DescribeCheckWarnings. |

| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the IDs of the risk items. |
|---|---|---|---|---|
| Uuid | String | Yes | d42f938c-d962- 48a0-90f9- 05********** | The ID of the server on which a baseline check is performed. The ID of the risk item. Note To query specified risk items and check items of a specified server, you must specify the ID of the server on which the baseline check is performed. |
| SourceIp | String | No | 192.168.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| PageSize | Integer | No | 20 | The number of entries to return on each page. Default value: 20. |
| CurrentPage | Integer | No | 1 | The number of the page to return. Pages start from page 1. Default value: 1. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| CheckWarning s | Array of CheckWarning |   | An array that consists of the information about the check item. |
| CheckId | Long | 1 | The ID of the check item. |
| CheckWarning Id | Long | 10 | The ID of the alert. |

| Item | String | Password expiration alert | The name of the check item. |
|---|---|---|---|
| Level | String | high | The severity of the risk item. Valid values: high medium low |
| Status | Integer | 1 | The status of the check item. Valid values: 1: failed 2: verifying 3: passed 5: expired 6: ignored |
| Type | String | Identity authentication | The type of the check item. |
| Uuid | String | d42f938c-d962- 48a0-90f9- *********** | The ID of the server on which the baseline check was performed. |
| Count | Integer | 10 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| RequestId | String | 0DFCADBA-7065- 42DA-AF17- 6868B9C2A8CF | The ID of the request. |
| TotalCount | Integer | 100 | The total number of entries returned. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarnings &RiskId=1 &Uuid=d42f938c-d962-48a0-90f9-05********** &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>100</TotalCount> <CheckWarnings>
    <Status>1</Status>
    <Item>Password expiration alert</Item>
    <Type>Identity authentication</Type>
    <Uuid>d42f938c-d962-48a0-90f9-***********</Uuid>
    <CheckId>1</CheckId>
    <CheckWarningId>10</CheckWarningId>
    <Level>high</Level>
</CheckWarnings> <PageSize>20</PageSize> <RequestId>0DFCADBA-7065-42DA-AF17-6868B9C2A8CF</RequestId> <CurrentPage>1</CurrentPage> <Count>10</Count>
```

`JSON` format `{`

```json
    "TotalCount": 100,
    "CheckWarnings": {
        "Status": 1,
        "Item": "Password expiration alert",
        "Type": "Identity authentication",
        "Uuid": "d42f938c-d962-48a0-90f9-***********",
        "CheckId": 1,
        "CheckWarningId": 10,
        "Level": "high"
```

`},`

```json
    "PageSize": 20,
    "RequestId": "0DFCADBA-7065-42DA-AF17-6868B9C2A8CF",
    "CurrentPage": 1,
    "Count": 10
```

`}`

#### 6.6.5 DescribeCheckWarningDetail

Queries the details of a specified check item.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeCheckW arningDetail | Set the value to DescribeCheckWarningDetail. |

| CheckWarningId | Long | Yes | 1 | The ID of the alert triggered by the check item. Note To query the details of a check item, you must specify the ID of the alert triggered by the check item. |
|---|---|---|---|---|
| SourceIp | String | No | 192.168.x.x | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Advice | String | Fix now | The suggestion for the management of the risk item. |
| CheckId | Long | 1 | The ID of the check item. |
| Description | String | Password expiring | The additional details of the risk item. |
| Item | String | Password expiration alert | The name of the check item. |
| Level | String | high | The severity of the risk item. Valid values: high: The item is a high-risk one and highlighted in red. medium: The item is a medium-risk one and highlighted in orange. low: The item is a low-risk one and highlighted in gray. |
| Prompt | String | Password expiration alert | The prompt for the risk item. |
| RequestId | String | 09969D2C-4FAD- 429E-BFBF- 9A60DEF8BF6F | The ID of the request. |
| Type | String | Identity authentication | The type of the check item. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeCheckWarningDetail &CheckWarningId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Item>Password expiration alert</Item> <Type>Identity authentication</Type> <Description>Password expiring</Description> <CheckId>1</CheckId> <RequestId>09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F</RequestId> <Prompt>Password expiration alert</Prompt> <Level>high</Level> <Advice>Fix now</Advice>
```

`JSON` format `{`

```json
    "Item": "Password expiration alert",
    "Type": "Identity authentication",
    "Description": "Password expiring",
    "CheckId": 1,
    "RequestId": "09969D2C-4FAD-429E-BFBF-9A60DEF8BF6F",
    "Prompt": "Password expiration alert",
    "Level": "high",
    "Advice": "Fix now"
```

`}`

#### 6.6.6 DescribeWarningMachines

Queries information about servers on which a baseline check is performed. The information includes the statistics of a risk item, the status of the risk item, the IDs of the servers, and the names of the servers.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeWarnin gMachines | Set the value to DescribeWarningMachines. |

| RiskId | Long | Yes | 1 | The ID of the risk item. Note To query information about servers on which a baseline check is performed, you must specify the ID of a risk item that is detected in the baseline check. You can call the DescribeCheckWarningSumm ary operation to query the ID of the risk item. |
|---|---|---|---|---|
| SourceIp | String | No | 47.100.XX.XX | The source IP address of the request. |
| Lang | String | No | zh | The language of the content within the request and response. Valid values: zh: Chinese en: English |
| MachineName | String | No | Baseline check server | The name of the server on which the baseline check is performed. |
| Uuids | String | No | xxx-aaa-bbb-ccc | The ID of the server on which the baseline check is performed. Separate multiple IDs with commas (,). |
| StrategyId | Long | No | 1 | The ID of the baseline check policy. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Count | Integer | 10 | The total number of returned pages. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 10 | The number of entries returned per page. |

| RequestId | String | 00BD7CE2-284A- 4534-BD09- FB69836DD750 | The ID of the request. |
|---|---|---|---|
| TotalCount | Integer | 100 | The total number of entries returned. |
| WarningMachi nes | Array of WarningMachi ne |   | An array that consists of the information about the servers on which alerts are generated. |
| HighWarningC ount | Integer | 10 | The number of high-risk items. |
| InstanceId | String | i- m5ee8b9nr3h30m hb**** | The ID of the server. |
| InstanceName | String | aaawebtest | The name of the server. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the server. |
| IntranetIp | String | 192.168.XX.XX | The internal IP address of the server. |
| LowWarningCo unt | Integer | 3 | The number of low-risk items. |
| MediumWarni ngCount | Integer | 2 | The number of medium-risk items. |
| PassCount | Integer | 10 | The number of the check items that have passed the baseline check. |
| RegionId | String | cn-qingdao** | The ID of the region in which the server is deployed. |
| Status | Integer | 1 | The verification status of the risk item that is fixed. Valid values: 1: complete 2: verifying |
| Uuid | String | xxx-aaa-bbb-ccc | The ID of the server on which the baseline check is performed. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeWarningMachines &RiskId=1 &<Common request parameters>
```

Sample success responses `XML` format

```xml
<TotalCount>100</TotalCount> <PageSize>10</PageSize> <RequestId>00BD7CE2-284A-4534-BD09-FB69836DD750</RequestId> <CurrentPage>1</CurrentPage> <WarningMachines>
    <Status>1</Status>
    <InstanceName>aaawebtest</InstanceName>
    <MediumWarningCount>2</MediumWarningCount>
    <Uuid>xxx-aaa-bbb-ccc</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstanceId>i-m5ee8b9nr3h30mhb****</InstanceId>
    <HighWarningCount>10</HighWarningCount>
    <RegionId>cn-qingdao</RegionId>
    <PassCount>10</PassCount>
    <IntranetIp>192.168.XX.XX</IntranetIp>
    <LowWarningCount>3</LowWarningCount>
</WarningMachines> <Count>10</Count>
```

`JSON` format `{`

```json
    "TotalCount": 100,
    "PageSize": 10,
    "RequestId": "00BD7CE2-284A-4534-BD09-FB69836DD750",
    "CurrentPage": 1,
    "WarningMachines": {
        "Status": 1,
        "InstanceName": "aaawebtest",
        "MediumWarningCount": 2,
        "Uuid": "xxx-aaa-bbb-ccc",
        "InternetIp": "47.100.XX.XX",
        "InstanceId": "i-m5ee8b9nr3h30mhb****",
        "HighWarningCount": 10,
        "RegionId": "cn-qingdao",
        "PassCount": 10,
        "IntranetIp": "192.168.XX.XX",
        "LowWarningCount": 3
```

`},`

```json
    "Count": 10
```

`}`

### 6.7 Asset fingerprints

#### 6.7.1 DescribePropertyCount

Queries the statistics of asset fingerprints, including the numbers of processes, ports, software assets, accounts, and scheduled tasks.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yCount | The operation that you want to perform. Set the value to DescribePropertyCount. |
| Type | String | No | port | The type of the asset fingerprint. Valid values: user: accounts software: software assets process: processes port: ports cron: scheduled tasks Note If you do not specify a type, all types of asset fingerprints are queried. |
| UuidList | String | No | [c4678332- ef3**,c46***] | The UUIDs of the assets. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| Autorun | Integer | 123 | The number of startup items. |
| Cron | Integer | 261 | The number of scheduled tasks. |
| Port | Integer | 163 | The number of listening ports. |
| Process | Integer | 367 | The number of running processes. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92**** | The ID of the request. |
| Sca | Integer | 125 | The number of middleware assets. |
| Software | Integer | 5073 | The number of software assets. |

| User | Integer | 114 | The number of accounts. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyCount &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Sca>125</Sca> <User>114</User> <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92****</RequestId> <Port>163</Port> <Software>5073</Software> <Process>367</Process> <Autorun>123</Autorun> <Cron>261</Cron>
```

`JSON` format `{`

```json
    "Sca": 125,
    "User": 114,
    "RequestId": "7E0618A9-D5EF-4220-9471-C42B5E92****",
    "Port": 163,
    "Software": 5073,
    "Process": 367,
    "Autorun": 123,
    "Cron": 261
```

`}`

#### 6.7.2 DescribePropertyPortDetail

Queries the details of a port.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortDetail | The operation that you want to perform. Set the value to DescribePropertyPortDetail. |

| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
|---|---|---|---|---|
| Port | String | No | 22 | The number of the port. |
| ProcName | String | No | sshd | The name of the process. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The UUID of the asset. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 6 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 762 | The total number of entries returned. |
| Propertys | Array of PropertyPort |   | An array that consists of the details of the port. |
| BindIp | String | 47.100.XX.XX | The IP addresses that are bound to the port. |
| Create | String | 2019-05- 13T10:39Z | The time when the data was last collected. |
| CreateTimesta mp | Long | 1557715141000 | The timestamp when the data was last collected. Unit: milliseconds. |
| InstanceId | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fxxx | The ID of the asset that is associated with the port. |

| InstanceName | String | test-*** | The name of the asset that is associated with the port. |
|---|---|---|---|
| InternetIp | String | 42.2.X.X | The public IP address of the asset. |
| IntranetIp | String | 192.168.X.X | The private IP address of the asset. |
| Ip | String | 42.2.X.X | The public IP address of the asset. |
| Port | String | 22 | The port number. |
| ProcName | String | sshd | The name of the process that uses the port. |
| Proto | String | tcp | The network protocol of the port. |
| Uuid | String | 50d213b4-3a35- 427a-b8a5- 04b0c7e1fXX | The UUID of the asset that is associated with the port. |
| pid | String | 1 | The ID of the parent process. |
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Propertys>
    <InstanceName>test-***</InstanceName>
    <Uuid>50d213b4-3a35-427a-b8a5-04b0c7e1fXX</Uuid>
    <InternetIp>42.2.X.X</InternetIp>
    <Proto>tcp</Proto>
    <InstanceId>50d213b4-3a35-427a-b8a5-04b0c7e1fxxx</InstanceId>
    <Create>2019-05-13T10:39Z</Create>
    <ProcName>sshd</ProcName>
    <Ip>42.2.X.X</Ip>
    <Port>22</Port>
    <pid>1</pid>
    <IntranetIp>192.168.X.X</IntranetIp>
    <CreateTimestamp>1557715141000</CreateTimestamp>
    <BindIp>47.100.XX.XX</BindIp>
</Propertys> <PageInfo>
    <TotalCount>762</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>5</Count>
</PageInfo> <RequestId> FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` format `{`

```json
    "Propertys": {
        "InstanceName": "test-***",
        "Uuid": "50d213b4-3a35-427a-b8a5-04b0c7e1fXX",
        "InternetIp": "42.2.X.X",
        "Proto": "tcp",
        "InstanceId": "50d213b4-3a35-427a-b8a5-04b0c7e1fxxx",
        "Create": "2019-05-13T10:39Z",
        "ProcName": "sshd",
        "Ip": "42.2.X.X",
        "Port": 22,
        "pid": 1,
        "IntranetIp": "192.168.X.X",
        "CreateTimestamp": 1557715141000,
        "BindIp": "47.100.XX.XX"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 762,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 5
```

`},`

```json
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
```

`}`

#### 6.7.3 DescribePropertyProcDetail

Queries the details of a process.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yProcDetail | The operation that you want to perform. Set the value to DescribePropertyProcDetail. |
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| Name | String | No | 8888 | The name of the process. |
| User | String | No | root | The user who runs the process. |
| Cmdline | String | No | ./8888 | The startup parameter of the process. |
| Uuid | String | No | c4678332-ef35- 4ad4-*** | The UUID of the asset that is associated with the process. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 1 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 1 | The total number of entries returned. |

| Propertys | Array of PropertyProc |   | An array that consists of the information about the process. |
|---|---|---|---|
| Cmdline | String | ./8888 | The startup parameter of the process. |
| Create | String | 2019-05- 15T11:08Z | The time when the data was last collected. |
| CreateTimesta mp | Long | 1565686951000 | The timestamp when the data was last collected. Unit: milliseconds. |
| EuidName | String | root | The permissions required to run the process. |
| InstanceId | String | c4678332-ef35- 4ad4-8358-*** | The ID of the asset that is associated with the process. |
| InstanceName | String | test-*** | The name of the asset that is associated with the process. |
| InternetIp | String | 40.2.x.x | The public IP address of the asset. |
| IntranetIp | String | 192.168.x.x | The private IP address of the asset. |
| Md5 | String | N/A | The MD5 hash value of the process file. |
| Name | String | 8888 | The name of the process. |
| Path | String | /root/Oracle/Middle ware/***/8888 | The path of the process. |
| Pid | String | 12826 | The ID of the process. |
| Pname | String | start***.s | The name of the parent process to which the process belongs. |
| StartTime | String | 2019-08-07 10:09:05 | The time when the process was started. The time is in the yyyy-MM-dd HH:mm:ss format. |
| User | String | root | The user who runs the process. |

| Uuid | String | c4678332-ef35- 4ad4-8358-6*** | The UUID of the asset that is associated with the process. |
|---|---|---|---|
| RequestId | String | 64388374-A309- 4191-8606- 3346CCA364B0 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Propertys>
    <Path>/root/Oracle/Middleware/***/8888</Path>
    <Pname>start***.s</Pname>
    <User>root</User>
    <InstanceId>c4678332-ef35-4ad4-8358-***</InstanceId>
    <StartTime>2019-08-07 10:09:05</StartTime>
    <Pid>12826</Pid>
    <EuidName>root</EuidName>
    <IntranetIp>192.168.x.x</IntranetIp>
    <Name>8888</Name>
    <InstanceName>test-***</InstanceName>
    <Uuid>c4678332-ef35-4ad4-8358-6***</Uuid>
    <InternetIp>40.2.x.x</InternetIp>
    <Create>2019-05-15T11:08Z</Create>
    <Cmdline>./8888</Cmdline>
    <CreateTimestamp>1565686951000</CreateTimestamp>
    <Md5>N/A</Md5>
</Propertys> <PageInfo>
    <TotalCount>1</TotalCount>
    <PageSize>5</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>1</Count>
</PageInfo> <RequestId>64388374-A309-4191-8606-3346CCA364B0</RequestId>
```

`JSON` format `{`

```json
    "Propertys": {
        "Path": "/root/Oracle/Middleware/***/8888",
        "Pname": "start***.s",
        "User": "root",
        "InstanceId": "c4678332-ef35-4ad4-8358-***",
        "StartTime": "2019-08-07 10:09:05",
        "Pid": 12826,
        "EuidName": "root",
        "IntranetIp": "192.168.x.x",
        "Name": 8888,
        "InstanceName": "test-***",
        "Uuid": "c4678332-ef35-4ad4-8358-6***",
        "InternetIp": "40.2.x.x",
        "Create": "2019-05-15T11:08Z",
        "Cmdline": "./8888",
        "CreateTimestamp": 1565686951000,
        "Md5": "N/A"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 1,
        "PageSize": 5,
        "CurrentPage": 1,
        "Count": 1
```

`},`

```json
    "RequestId": "64388374-A309-4191-8606-3346CCA364B0"
```

`}`

#### 6.7.4 DescribePropertyPortItem

Queries information about all ports.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yPortItem | The operation that you want to perform. Set the value to DescribePropertyPortItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| Port | String | No | 22 | The port number. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |

| PageSize | Integer | No | 5 | The number of entries to return on each page. |
|---|---|---|---|---|

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 163 | The total number of entries returned. |
| PropertyItems | Array of PropertyItem |   | An array that consists of the information about the port. |
| Count | Integer | 495 | The number of servers that use the port. |
| Port | String | 22 | The number of the listening port. |
| Proto | String | tcp | The network protocol of the port. |
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyPortItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyPortItemResponse>
        <RequestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</RequestId>
        <PropertyItems>
       <Port>22</Port>
       <Proto>tcp</Proto>
       <Count>495</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>111</Port>
       <Proto>tcp</Proto>
       <Count>43</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>6000</Port>
       <Proto>tcp</Proto>
       <Count>2</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>53</Port>
       <Proto>tcp</Proto>
       <Count>1</Count>
     </PropertyItems>
     <PropertyItems>
       <Port>80</Port>
       <Proto>tcp</Proto>
       <Count>38</Count>
     </PropertyItems>
        <PageInfo>
       <Count>5</Count>
       <PageSize>5</PageSize>
       <TotalCount>163</TotalCount>
       <CurrentPage>1</CurrentPage>
     </PageInfo>
</DescribePropertyPortItemResponse>
```

`JSON` format `{`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "PropertyItems": [
```

`{`

```json
        "Port": "22",
        "Proto": "tcp",
        "Count": 495
```

`},` `{`

```json
        "Port": "111",
        "Proto": "tcp",
        "Count": 43
```

`},` `{`

```json
        "Port": "6000",
        "Proto": "tcp",
        "Count": 2
```

`},` `{`

```json
        "Port": "53",
        "Proto": "tcp",
        "Count": 1
```

`},` `{`

```json
        "Port": "80",
        "Proto": "tcp",
        "Count": 38
```

`}` `],`

```json
  "PageInfo": {
      "Count": 5,
      "PageSize": 5,
      "TotalCount": 163,
      "CurrentPage": 1
```

`}` `}`

#### 6.7.5 DescribePropertyProcItem

Queries information about all processes.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yProcItem | The operation that you want to perform. Set the value to DescribePropertyProcItem. |

| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
|---|---|---|---|---|
| Name | String | No | test | The name of the process. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 5 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 5 | The number of entries returned per page. |
| TotalCount | Integer | 372 | The total number of entries returned. |
| PropertyItems | Array of PropertyProcIt em |   | An array that consists of the information about the process. |
| Count | Integer | 8888 | The number of servers on which the process runs. |
| Name | String | .ss | The name of the process. |
| RequestId | String | BD8AD4C6-A169- 4FA3-BA1F- ED40ED52973B | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyProcItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertyProcItem>
  <PropertyItems>
        <Name>(sd-**)</Name>
        <Count>7</Count>
  </PropertyItems>
  <PropertyItems>
        <Name>6Cm***</Name>
        <Count>1</Count>
  </PropertyItems>
  <RequestId>BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B</RequestId>
  <PageInfo>
        <Count>2</Count>
        <TotalCount>395</TotalCount>
        <PageSize>2</PageSize>
        <CurrentPage>1</CurrentPage>
  </PageInfo>
</DescribePropertyProcItem>
```

`JSON` format `{`

```json
 "PropertyItems": [
```

`{`

```json
   "Name": "(sd-**)",
   "Count": 7
```

`},` `{`

```json
   "Name": "6Cm***",
   "Count": 1
```

`}` `],`

```json
 "RequestId": "BD8AD4C6-A169-4FA3-BA1F-ED40ED52973B",
 "PageInfo": {
  "Count": 2,
  "TotalCount": 395,
  "PageSize": 2,
  "CurrentPage": 1
```

`}` `}`

#### 6.7.6 DescribePropertySoftwareDetail

Queries the details of a software asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|

| Action | String | Yes | DescribePropert ySoftwareDetail | The operation that you want to perform. Set the value to DescribePropertySoftwareDetail. |
|---|---|---|---|---|
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| Name | String | No | tes*** | The name of the software. |
| Path | String | No | /etc/test | The directory in which the software is installed. |
| SoftwareVersion | String | No | 11 | The version of the software. |
| Uuid | String | No | 50d213b4-3a35- 427a-b8a5-*** | The ID of the instance on which the software is installed. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 5 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 23 | The total number of entries returned. |
| Propertys | Array of PropertySoftw are |   | An array that consists of the details about the software. |
| Create | Long | 1565539587000 | The time when the data was last collected. Unit: milliseconds. |

| CreateTimesta mp | Long | 1565539587000 | The timestamp when the data was last collected. Unit: milliseconds. |
|---|---|---|---|
| InstallTime | String | 2017-09-07 10:54:49 | The time when the software was installed. The time is in the yyyy-MM-dd HH:mm:ss format. |
| InstallTimeSta mp | Long | 1565539587000 | The timestamp when the software was installed. Unit: milliseconds. |
| InstanceId | String | i-uf*** | The ID of the asset. |
| InstanceName | String | test | The name of the asset. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the asset. |
| IntranetIp | String | 192.168.0.1 | The private IP address of the asset. |
| Ip | String | 47.100.XX.XX | The IP address that is displayed for the asset. Note If the asset has a public IP address, the public IP address is returned. Otherwise, the private IP address is returned. |
| Name | String | aaa base _ | The name of the software. |
| Path | String | /etc/test | The directory in which the software is installed. |
| Uuid | String | 4ef1115b-e423- 4b4b-b930-*** | The UUID of the asset. |
| Version | String | 11 | The version of the software. |
| RequestId | String | 9C5AE850-7140- 4DE6-B892- 055EB0D9F28A | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Propertys>
    <InstanceName>test</InstanceName>
    <Path>/etc/test</Path>
    <Uuid>4ef1115b-e423-4b4b-b930-***</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <InstallTimeStamp>1565539587000</InstallTimeStamp>
    <InstanceId>i-uf***</InstanceId>
    <Version>11</Version>
    <InstallTime>2017-09-07 10:54:49</InstallTime>
    <Create>1565539587000</Create>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <CreateTimestamp>1565539587000</CreateTimestamp>
    <Name>aaa_base</Name>
</Propertys> <PageInfo>
    <TotalCount>23</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>9C5AE850-7140-4DE6-B892-055EB0D9F28A</RequestId>
```

`JSON` format `{`

```json
    "Propertys": {
        "InstanceName": "test",
        "Path": "/etc/test",
        "Uuid": "4ef1115b-e423-4b4b-b930-***",
        "InternetIp": "47.100.XX.XX",
        "InstallTimeStamp": 1565539587000,
        "InstanceId": "i-uf***",
        "Version": 11,
        "InstallTime": "2017-09-07 10:54:49",
        "Create": 1565539587000,
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "CreateTimestamp": 1565539587000,
        "Name": "aaa_base"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 23,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
```

`},`

```json
    "RequestId": "9C5AE850-7140-4DE6-B892-055EB0D9F28A"
```

`}`

#### 6.7.7 DescribePropertySoftwareItem

Queries information about all software assets.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert ySoftwareItem | The operation that you want to perform. Set the value to DescribePropertySoftwareItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| Name | String | No | test | The name of the software that you want to query. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| PageSize | Integer | No | 10 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 5037 | The total number of entries returned. |
| PropertyItems | Array of PropertySoftw areItem |   | An array that consists of the returned software assets. |

| Count | Integer | 23 | The number of servers on which the software is installed. |
|---|---|---|---|
| Name | String | aaa base _ | The name of the returned software. |
| RequestId | String | 3A85CFCF-05C8- 451A-9E41- C0D5E96BA407 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertySoftwareItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
<DescribePropertySoftwareItemResponse>
   <PageInfo>
       <Count>2</Count>
       <PageSize>2</PageSize>
       <TotalCount>5037</TotalCount>
       <CurrentPage>1</CurrentPage>
   </PageInfo>
   <PropertyItems>
       <Name>a11y-profile-manager-indicator</Name>
       <Count>1</Count>
   </PropertyItems>
   <PropertyItems>
       <Name>aaa_base</Name>
       <Count>23</Count>
   </PropertyItems>
   <requestId>3A85CFCF-05C8-451A-9E41-C0D5E96BA407</requestId>
</DescribePropertySoftwareItemResponse>
```

`JSON` format `{`

```json
  "PageInfo": {
      "Count": 2,
      "PageSize": 2,
      "TotalCount": 5037,
      "CurrentPage": 1
```

`},`

```json
    "PropertyItems": [
```

`{`

```json
        "Name": "a11y-profile-manager-indicator",
        "Count": 1
```

`},` `{`

```json
        "Name": "aaa_base",
        "Count": 23
```

`}` `],`

```json
     "requestId": "3A85CFCF-05C8-451A-9E41-C0D5E96BA407"
```

`}`

#### 6.7.8 DescribePropertyUserDetail

Queries the details of a specified account.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserDetail | The operation that you want to perform. Set the value to DescribePropertyUserDetail. |
| Remark | String | No | 47.100.XX.XX | The name or IP address of the server. |
| User | String | No | tes*** | The name of the account that you want to query. |
| IsRoot | String | No | 0 | Specifies whether the account has root permissions. Valid values: 0: no 1: yes |
| Uuid | String | No | 50d213b4-*****- 427a-b8a5- 04b0c7****** | The UUID of the asset that you want to query. |

| CurrentPage | Integer | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 384 | The total number of entries returned. |
| Propertys | Array of PropertyUser |   | An array that consists of the details of the account. |
| AccountsExpir ationDate | String | None | This parameter is deprecated. |
| Create | String | 2022-01- 03T06:43Z | The time when the data was last collected. The time is in the yyyy-MM-dd HH:mm:ss format. |
| CreateTimesta mp | Long | 1565644643000 | The timestamp when the data was collected. Unit: milliseconds. |
| GroupNames | List | adm | The name of the user group. |
| InstanceId | String | 02c4a5dc-****- 483a-9015- f972b****** | The ID of the asset. |
| InstanceName | String | e21g06001.cloud.g 06.xxx | The name of the asset. |
| InternetIp | String | 47.100.XX.XX | The public IP address of the asset. |

| IntranetIp | String | 192.168.0.1 | The private IP address of the asset. |
|---|---|---|---|
| Ip | String | 47.100.XX.XX | The IP address of the asset. |
| IsRoot | String | 0 | Indicates whether the account has the root permissions. Valid values: 0: no 1: yes |
| LastLoginIp | String | 47.100.XX.XX | The source IP address of the last logon. |
| LastLoginTime | String | 2022-01-03 06:33:33 | The time of the last logon. The time is in the yyyy-MM-dd HH:mm:ss format. |
| LastLoginTime stamp | Long | 1565644643000 | The timestamp of the last logon. Unit: milliseconds. |
| PasswordExpir ationDate | String | None | This parameter is deprecated. |
| Status | String | 0 | The logon status of the account. Valid values: 0: The account cannot be used for logon. 1: The account can be used for logon. |
| User | String | adm | The name of the account. |
| Uuid | String | 02c4a5dc-c2d2- 483a-9015- f972b4****** | The UUID of the asset. |
| RequestId | String | FAA793EF-5B14- 4CDD-B3E0- B14D4342C422 | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserDetail &<Common request parameters>
```

Sample success responses `XML` format

```xml
<Propertys>
    <Status>0</Status>
    <IsRoot>0</IsRoot>
    <User>adm</User>
    <InstanceId>02c4a5dc-****-483a-9015-f972b******</InstanceId>
    <LastLoginIp>47.100.XX.XX</LastLoginIp>
    <Ip>47.100.XX.XX</Ip>
    <IntranetIp>192.168.0.1</IntranetIp>
    <AccountsExpirationDate>None</AccountsExpirationDate>
    <InstanceName>e21g06001.cloud.g06.xxx</InstanceName>
    <LastLoginTime>2022-01-03 06:33:33</LastLoginTime>
    <Uuid>02c4a5dc-c2d2-483a-9015-f972b4******</Uuid>
    <InternetIp>47.100.XX.XX</InternetIp>
    <LastLoginTimestamp>1565644643000</LastLoginTimestamp>
    <Create>2022-01-03T06:43Z</Create>
    <CreateTimestamp>1565644643000</CreateTimestamp>
    <PasswordExpirationDate>None</PasswordExpirationDate>
    <GroupNames>adm</GroupNames>
</Propertys> <PageInfo>
    <TotalCount>384</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>FAA793EF-5B14-4CDD-B3E0-B14D4342C422</RequestId>
```

`JSON` format `{`

```json
    "Propertys": {
        "Status": 0,
        "IsRoot": 0,
        "User": "adm",
        "InstanceId": "02c4a5dc-****-483a-9015-f972b******",
        "LastLoginIp": "47.100.XX.XX",
        "Ip": "47.100.XX.XX",
        "IntranetIp": "192.168.0.1",
        "AccountsExpirationDate": "None",
        "InstanceName": "e21g06001.cloud.g06.xxx",
        "LastLoginTime": "2022-01-03 06:33:33",
        "Uuid": "02c4a5dc-c2d2-483a-9015-f972b4******",
        "InternetIp": "47.100.XX.XX",
        "LastLoginTimestamp": 1565644643000,
        "Create": "2022-01-03T06:43Z",
        "CreateTimestamp": 1565644643000,
        "PasswordExpirationDate": "None",
        "GroupNames": "adm"
```

`},`

```json
    "PageInfo": {
        "TotalCount": 384,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
```

`},`

```json
    "RequestId": "FAA793EF-5B14-4CDD-B3E0-B14D4342C422"
```

`}`

#### 6.7.9 DescribePropertyUserItem

Queries the account information about an asset.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribePropert yUserItem | The operation that you want to perform. Set the value to DescribePropertyUserItem. |
| ForceFlush | Boolean | No | true | Specifies whether to forcefully refresh the data that you want to query. |
| User | String | No | adm | The account information about the asset fingerprint. |

| CurrentPage | Integer | No | 1 | The number of the page to return. |
|---|---|---|---|---|
| PageSize | Integer | No | 2 | The number of entries to return on each page. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 2 | The number of entries returned per page. |
| TotalCount | Integer | 114 | The total number of entries returned. |
| PropertyItems | Array of PropertyUserIt em |   | An array that consists of the account information. |
| Count | Integer | 384 | The number of servers that belong to the account. |
| User | String | adm | The name of the account. |
| RequestId | String | 76068BE2-F9C4- 4EDD-967B- F503B8CCXXXX | The ID of the request. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribePropertyUserItem &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageInfo>
    <TotalCount>114</TotalCount>
    <PageSize>2</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>76068BE2-F9C4-4EDD-967B-F503B8CCXXXX</RequestId> <PropertyItems>
    <User>adm</User>
    <Count>384</Count>
</PropertyItems>
```

`JSON` format `{`

```json
    "PageInfo": {
        "TotalCount": 114,
        "PageSize": 2,
        "CurrentPage": 1,
        "Count": 2
```

`},`

```json
    "RequestId": "76068BE2-F9C4-4EDD-967B-F503B8CCXXXX",
    "PropertyItems": {
        "User": "adm",
        "Count": 384
```

`}` `}`

#### 6.7.10 DescribeModuleConfig

Queries the configurations of asset fingerprint modules.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeModule Config | The operation that you want to perform. Set the value to DescribeModuleConfig. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| RequestId | String | 7E0618A9-D5EF- 4220-9471- C42B5E92719F | The ID of the request. |

| Success | Boolean | true | Indicates whether the request is successful. |
|---|---|---|---|
| Count | Integer | 2 | The number of module configurations. |
| HttpStatusCod e | Integer | 200 | The HTTP status code. |
| ModuleConfigL ist | Array |   | The list of module configurations. |
| ConfigName | String | timescan | The name of the configuration. |
| ModuleName | String | alihids | The name of the template. |
| Items | Array |   | The list of configuration items. |
| InstanceId | String | lb-xxx | The ID of the instance. |
| InstanceName | String | ssxxxxxxxx | The name of the instance. |
| GroupId | Integer | 173 | The ID of the group. |
| Ip | String | 2.2.2.2 | The IP address of the instance. |
| Region | String | outside-of-aliyun | The region where the instance is deployed. |
| Uuid | String | lb-xxxx-xxxx-xxxx- xxxx | The UUID of the server. |

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeModuleConfig &<Common request parameters>
```

Sample success responses `XML` format

```xml
<code>200</code> <data>
    <Count>2</Count>
    <ModuleConfigList>
        <ConfigName>timescan</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>ssxxxxxxxx</InstanceName>
            <Uuid>lb-xxxx-xxxx-xxxx-xxxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.1.2.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
    <ModuleConfigList>
        <ConfigName>sysvulfix</ConfigName>
        <ModuleName>alihids</ModuleName>
        <Items>
            <InstanceName>xx</InstanceName>
            <Uuid>lb-xxx</Uuid>
            <InstanceId>lb-xxx</InstanceId>
            <Ip>2.2.2.2</Ip>
            <Region>cn-qingdao</Region>
            <GroupId>173</GroupId>
        </Items>
        <Items>
            <InstanceName>3a04702ca5a0</InstanceName>
            <Uuid>inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6</Uuid>
            <Ip>192.168.5.3</Ip>
            <Region>outside-of-aliyun</Region>
            <GroupId>343</GroupId>
        </Items>
    </ModuleConfigList>
</data> <requestId>7E0618A9-D5EF-4220-9471-C42B5E92719F</requestId> <success>true</success>
```

`JSON` format `{`

```json
  "code": 200,
  "data": {
    "Count": 2,
    "ModuleConfigList": [{
        "ConfigName": "timescan",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "ssxxxxxxxx",
            "Uuid": "lb-xxxx-xxxx-xxxx-xxxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
```

`},` `{`

```json
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.1.2.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
```

`}` `]` `},` `{`

```json
        "ConfigName": "sysvulfix",
        "ModuleName": "alihids",
        "Items": [{
            "InstanceName": "xx",
            "Uuid": "lb-xxx",
            "InstanceId": "lb-xxx",
            "Ip": "2.2.2.2",
            "Region": "cn-qingdao",
            "GroupId": 173
```

`},` `{`

```json
            "InstanceName": "3a04702ca5a0",
            "Uuid": "inet-db626549-870c-4d3e-b0b5-4d8a5c7268a6",
            "Ip": "192.168.5.3",
            "Region": "outside-of-aliyun",
            "GroupId": 343
```

`}` `]` `}` `]` `},`

```json
  "requestId": "7E0618A9-D5EF-4220-9471-C42B5E92719F",
  "success": true
```

`}`

**Error codes**

For a list of error codes, see Error codes.

### 6.8 Asset exposure

#### 6.8.1 DescribeExposedInstanceList

Queries the assets that are exposed.

**Request parameters**

| Parameter | Type | Requir ed | Example | Description |
|---|---|---|---|---|
| Action | String | Yes | DescribeExpose dInstanceList | The operation that you want to perform. Set the value to DescribeExposedInstanceList. |
| PageSize | Integer | No | 20 | The number of entries to return on each page. |
| CurrentPage | Integer | No | 1 | The number of the page to return. |
| GroupId | Long | No | 9469268 | The ID of the server group. |
| VulStatus | Boolean | No | true | Specifies whether the server has vulnerabilities. Valid values: true: yes false: no |
| HealthStatus | Boolean | No | true | Specifies whether baseline risks exist in the server. |
| ExposureCompo nent | String | No | openssl | The server component that is exposed on the Internet. |
| ExposurePort | String | No | 22 | The port that is exposed on the Internet. |
| ExposureIp | String | No | 116.12.XX.XX | The public IP address of the server. |
| InstanceId | String | No | i- bp1g6wxdwps7s 9dz**** | The ID of the server. |
| InstanceName | String | No | abc centos7.2 0 _ _ 05 | The name of the server. |

**Response parameters**

| Parameter | Type | Example | Description |
|---|---|---|---|
| ExposedInstan ces | Array of ExposedInstan ce |   | An array that consists of the details of the exposed asset. |
| AsapVulCount | Integer | 0 | The number of high-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| ExploitHealthC ount | Integer | 0 | The number of baseline risks that can be exploited. |
| ExposureCom ponent | String | openssl,openssh | The server component that is exposed on the Internet. |
| ExposureIp | String | 116.12.XX.XX | The public IP address that is exposed on the Internet. |
| ExposurePort | String | 22 | The port that is exposed on the Internet. |
| ExposureType | String | INTERNET IP _ | The resource from which the asset is exposed. Valid values: INTERNET IP: the IP address of the _ Elastic Compute Service (ECS) instance SLB: the public IP address of the Server Load Balancer (SLB) instance EIP: the elastic IP address (EIP) DNAT: the NAT gateway that connects to the Internet by using the DNAT feature |
| ExposureTypeI d | String | i-ew11313a**** | The ID of the instance from which the asset is exposed. The value of this parameter varies based on the value of the ExposureType parameter. If the value of the ExposureType parameter is INTERNET IP, the value _ of this parameter is an empty string. If the value of the ExposureType parameter is SLB, the value of this parameter is the ID of the Internet- facing SLB instance. If the value of the ExposureType parameter is EIP, the value of this parameter is the ID of the EIP. If the value of the ExposureType parameter is DNAT, the value of this parameter is the ID of the NAT gateway. |

| GroupId | Long | 9469268 | The ID of the server group. |
|---|---|---|---|
| GroupName | String | Ungrouped | The name of the server group. |
| InstanceId | String | i- bp1g6wxdwps7s9d z**** | The ID of the server. |
| InstanceName | String | abc centos7.2 005 _ _ | The name of the server. |
| InternetIp | String | 116.12.XX.XX | The public IP address of the server. |
| IntranetIp | String | 192.168.XX.XX | The private IP address of the server. |
| LaterVulCount | Integer | 0 | The number of medium-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| NntfVulCount | Integer | 0 | The number of low-risk vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| RegionId | String | cn-hangzhou | The ID of the region where the server resides. |
| TotalVulCount | Integer | 0 | The total number of vulnerabilities that are exposed on the Internet and can be exploited by attackers. |
| Uuid | String | dd803d9e-a337- 4add-9c5b- 7d503e08**** | The UUID of the server. |
| PageInfo | Struct |   | The pagination information. |
| Count | Integer | 2 | The number of entries returned on the current page. |
| CurrentPage | Integer | 1 | The page number of the returned page. |
| PageSize | Integer | 20 | The number of entries returned per page. |
| TotalCount | Integer | 2 | The total number of entries returned. |

| RequestId | String | 598A4A61-ABA7- 456B-8725- 7378258276D9 | The ID of the request. |
|---|---|---|---|

**Examples**

Sample requests

```
http(s)://[Endpoint]/?Action=DescribeExposedInstanceList &<Common request parameters>
```

Sample success responses `XML` format

```xml
<PageInfo>
    <TotalCount>2</TotalCount>
    <PageSize>20</PageSize>
    <CurrentPage>1</CurrentPage>
    <Count>2</Count>
</PageInfo> <RequestId>598A4A61-ABA7-456B-8725-7378258276D9</RequestId> <ExposedInstances>
    <GroupName>Ungrouped</GroupName>
    <TotalVulCount>0</TotalVulCount>
    <ExposureType>INTERNET_IP</ExposureType>
    <InstanceId>i-bp1g6wxdwps7s9dz****</InstanceId>
    <ExposureComponent>openssl,openssh</ExposureComponent>
    <ExposurePort>22</ExposurePort>
    <NntfVulCount>0</NntfVulCount>
    <AsapVulCount>0</AsapVulCount>
    <ExploitHealthCount>0</ExploitHealthCount>
    <IntranetIp>192.168.XX.XX </IntranetIp>
    <GroupId>9469268</GroupId>
    <InstanceName>abc_centos7.2_005 </InstanceName>
    <Uuid>dd803d9e-a337-4add-9c5b-7d503e08****</Uuid>
    <ExposureIp>116.12.XX.XX </ExposureIp>
    <ExposureTypeId>i-ew11313a****</ExposureTypeId>
    <InternetIp>116.12.XX.XX</InternetIp>
    <LaterVulCount>0</LaterVulCount>
    <RegionId>cn-hangzhou</RegionId>
</ExposedInstances>
```

`JSON` format

```json
{"PageInfo": {"TotalCount":"2","PageSize":"20","CurrentPage":"1","Count":"2"},"RequestId":"598A4A61- ABA7-456B-8725-7378258276D9","ExposedInstances": [{"GroupName":"Ungrouped","TotalVulCount":"0","ExposureType":"INTERNET_IP","InstanceId":" bp1g6wxdwps7s9dz****","ExposureComponent":"openssl,openssh","ExposurePort":"22","NntfVulC nt":"0","AsapVulCount":"0","ExploitHealthCount":"0","IntranetIp":"192.168.XX.XX\t","Group ":"9469268","InstanceName":"abc_centos7.2_005\t","Uuid":"dd803d9e-a337-4add-9c5b-7d503e 08****","ExposureIp":"116.12.XX.XX\t","ExposureTypeId":"iew11313a****","InternetIp":"116.12.XX.XX","LaterVulCount":"0","RegionId":"cn-hangzhou"}
```

`]}`

## 7 Error codes

This topic describes the error codes returned for operations in Apsara Stack Security. Table 1. Common errors

| Error code | Error message | Description |
|---|---|---|
| yd.error.all.10001 | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.10002 | A system error occurred. Try again later. | The error message returned because a system error occurred. Try again later. |
| yd.error.all.10003 | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request parameter and try again. |
| yd.error.all.other | A system exception occurred. | The error message returned because a system error occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1001 _ | An unknown error occurred. | The error message returned because an unknown error occurred. Try again later. |
| yd.error.all.ConsoleSystemError 1007 _ | The specified API operation is unpublished. | The error message returned because the specified API operation is unpublished. Contact Alibaba Cloud technical support. |
| yd.error.all.ConsoleSystemError 1008 _ | An error occurred while verifying postOnly. | The error message returned because the verification failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1009 _ | The csrfToken field is not specified. | The error message returned because the csrfToken field is empty. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1010 _ | An error occurred while verifying csrfToken. | The error message returned because the verification failed. Check the common request parameters and try again. |
| yd.error.all.ConsoleSystemError 1011 _ | The regionId parameter is not specified. | The error message returned because the RegionId parameter is not specified. Check the parameter. |
| yd.error.all.ConsoleSystemError 1012 _ | The format of the specified regionId parameter is invalid. | The error message returned because the format of the specified RegionId parameter is invalid. Check the parameter. |

| yd.error.all.ConsoleSystemError 1013 _ | The parameter is not specified. | The error message returned because the parameter is not specified. Check the parameter and try again. |
|---|---|---|
| yd.error.all.ConsoleSystemError 1014 _ | The format of the specified parameter is invalid. | The error message returned because the format of the specified parameter is invalid. Check the parameter and try again. |
| yd.error.all.ConsoleNeedLogin | You are not logged on. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.InvalidApi | An operation exception occurred. | The error message returned because an operation exception occurred. Try again later. |
| yd.error.all.InvalidParameter | The parameter is invalid. | The error message returned because the specified parameter is invalid. Check the request parameter and try again. |
| yd.error.all.InvalidResult | The return value is invalid. | The error message returned because the return value is invalid. Try again later. |
| yd.error.all.PropertyConvertFail ed | An error occurred during conversion. | The error message returned because property conversion failed. Try again later. |
| yd.error.all.NoPermission | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.all.ServerError | A server error occurred. | The error message returned because a server error occurred. Try again later or contact Alibaba Cloud technical support. |
| yd.error.all.UnkownError | An unknown error occurred. | The error message returned because an unknown error occurred. Try again later or contact Alibaba Cloud technical support. |

Table 2. Error codes specific to Threat Detection Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.sas.1 | The specified field does not exist in the metadata. | The error message returned because the field you queried does not exist in the metadata. Check the request and try again. |

| yd.error.sas.2 | An error occurred while invoking the task engine. Try again. | The error message returned because the system failed to invoke the task engine. Try again later. |
|---|---|---|
| yd.error.sas.3 | An error occurred while starting the task. Try again. | The error message returned because the system failed to start the task. Try again later. |
| yd.error.sas.4 | An error occurred while stopping the task. Try again. | The error message returned because the system failed to stop the task. Try again later. |
| yd.error.sas.5 | An error occurred while restarting the task. Try again. | The error message returned because the system failed to restart the task. Try again later. |
| yd.error.sas.6 | An error occurred while obtaining the task status. Try again. | The error message returned because the system failed to obtain the task status. Try again later. |
| yd.error.sas.7 | An error occurred while deleting the task. Try again. | The error message returned because the system failed to delete the task. Try again later. |
| yd.error.sas.8 | The specified table does not contain metadata. | The error message returned because the table you queried does not contain metadata. Check the request and try again. |
| yd.error.sas.100 | Request failed. Refresh the page and try again. | The error message returned because the request failed. Try again later. |
| yd.error.sas.101 | The parameter is invalid. | The error message returned because the parameter is invalid. Check the parameter and try again. |
| yd.error.sas.103 | Request failed. | The error message returned because the request failed. Check the request and try again later. |
| yd.error.sas.400 | The asset is under protection. Uninstall the Server Guard agent and try again. | The error message returned because the asset that you want to delete is protected by the Server Guard agent. Uninstall the Server Guard agent from the server and try again. |
| yd.error.sas.500 | A system error occurred. | The error message returned because a system error occurred. Contact Alibaba Cloud technical support. |
| yd.error.sas.501 | The feature is not available in the current version. | The error message returned because the version you used does not support this feature. |

| yd.error.sas.502 | You are not authorized to access the server. | The error message returned because you are not authorized to manage the server. |
|---|---|---|

Table 3. Error codes specific to Anti-DDoS Service

| Error code | Error message | Description |
|---|---|---|
| yd.error.ddos.400 | An error occurred while accessing the server. Try again. | The error message returned because the system failed to access the server. Try again later. |
| yd.error.ddos.500 | An error occurred on the server. Contact technical support. | The error message returned because an error occurred on the server. Contact Alibaba Cloud technical support. |
| yd.error.ddos.UNKNOWN EXCE _ PTION | An unknown error occurred. | The error message returned because an unknown error occurred. Contact Alibaba Cloud technical support. |
| yd.error.ddos.REQUEST TIMEO _ UT | The request timed out. | The error message returned because the request timed out. Try again later. |
| yd.error.ddos.SERVER FAILED _ | The operation failed. | The error message returned because the operation failed. Contact Alibaba Cloud technical support. |
| yd.error.ddos.NOT AUTHORIZE _ D | Authorization required. | The error message returned because you are not authorized to perform the operation. Check the account permissions. |
| yd.error.ddos.PARAMETER INVA _ LID | The parameter is invalid or is not specified. | The error message returned because the specified request parameter is invalid. Check the parameter and try again. |
| yd.error.ddos.IP SEGMENT INV _ _ ALID | The specified CIDR block is invalid. Check the parameter and enter another value. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT REP _ _ EAT | One CIDR block cannot be used in different regions. Enter another CIDR block. | The error message returned because the specified CIDR block is invalid. Check the CIDR block specified in the request parameter. |
| yd.error.ddos.IP SEGMENT ALR _ _ EADY | The specified CIDR block already exists. | The error message returned because the specified CIDR block is in use. Check the CIDR block specified in the request parameter. |

| yd.error.ddos.IP SEGMENT MAS _ _ K LENGTH ERR _ _ | The mask can contain a maximum of 24 bits. | The error message returned because the mask contains more than 24 bits. Check the mask of the CIDR block specified in the request parameter. |
|---|---|---|
| yd.error.ddos.QUERY REGION L _ _ IST ERR _ | An error occurred while obtaining the region list. | The error message returned because the system failed to obtain the region list. Try again later. |
| yd.error.ddos.IP SEGMENT OPE _ _ RATION ERR _ | An error occurred while processing the CIDR block. | The error message returned because the system failed to process the CIDR block. Try again later. |
| yd.error.ddos.QUERY IP SEGME _ _ NT ERR _ | An error occurred while obtaining the CIDR block. | The error message returned because the system failed to obtain the CIDR block. Try again later. |
| yd.error.ddos.MODIFY IP SEGM _ _ ENT ERR _ | An error occurred while modifying the CIDR block. | The error message returned because the system failed to modify the CIDR block. Try again later. |
| yd.error.ddos.IP SEGMENT TYP _ _ E ERR _ | Check whether the type of the CIDR block (internal or external) is specified. | The error message returned because the CIDR block type is not specified. Check the CIDR block type and try again. |
| yd.error.ddos.CANCEL FLOW C _ _ LEAN ERR _ | An error occurred while canceling traffic scrubbing. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to cancel traffic scrubbing. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY FLOW AN _ _ ALYSIS ERR _ | An error occurred while obtaining the traffic analysis result. Check whether the network connection to Network Detection and Response is normal. | The error message returned because the system failed to obtain the traffic analysis result. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.QUERY BEAVER _ _ URL ERR _ | An error occurred while obtaining the URL of Network Detection and Response. | The error message returned because the system failed to obtain the URL of Network Detection and Response. Check the network connection to Network Detection and Response and try again. |
| yd.error.ddos.SET VALVE INVA _ _ LID | The threshold validation failed. Check the thresholds and enter correct values. | The error message returned because the threshold verification failed. Check the thresholds and try again. |

| yd.error.ddos.VALVE DEFAULT _ _ ALREADY | The specified request is invalid. You cannot add the default threshold. | The error message returned because the system failed to add the default threshold. The default threshold can only be modified. |
|---|---|---|
| yd.error.ddos.NOT BELONG BE _ _ AVER IP SEGMENT _ _ | Check whether the specified CIDR block belongs to the internal network of Network Detection and Response. | The error message returned because the CIDR block you entered does not belong to the internal network of Network Detection and Response. Check the CIDR block. |
| yd.error.ddos.VALVE DELETE E _ _ RR | The default threshold or the threshold configured for 128.0.XX.XX/XX cannot be deleted. | The error message returned because the system failed to delete the default threshold or the threshold configured for 128.0.XX.XX/XX. |
| yd.error.ddos.QUERY CODE ER _ _ R | An error occurred while obtaining the product configuration. | The error message returned because the system failed to obtain the product configuration. Try again later. |
| yd.error.ddos.IS OPENED _ | Enabled. | The error message returned because the specified switch has been turned on. |
| yd.error.ddos.IS CLOSED _ | Disabled. | The error message returned because the specified switch has been turned off. |

Table 4. Error codes specific to Server Guard

| Error code | Error message | Description |
|---|---|---|
| yd.error.aqs.REQUEST FAILED _ | Request failed. Try again later. | The error message returned because the request failed. Try again later. |

Table 7. Error codes specific to Cloud Firewall

| Error code | Error message |
|---|---|
| yd.error.code.200 | The request is successful. |
| yd.error.code.-360100 | The request method is invalid. |
| yd.error.code.-360101 | Authentication failed. |
| yd.error.code.-360102 | Invocation failed. |
| yd.error.code.-360103 | The parameter is invalid. Try again. |
| yd.error.code.-360104 | The specified application is invalid. Try again. |
| yd.error.code.-360105 | An error occurred while obtaining the logs. |
| yd.error.code.-360106 | An error occurred while obtaining the logs. |

| yd.error.code.-360107 | The specified UID is invalid.Try again. |
|---|---|
| yd.error.code.-360108 | An error occurred while paging. |
| yd.error.code.-360109 | The service is not supported. |
| yd.error.code.-360110 | The format of the specified IP address is invalid. Enter another value. |
| yd.error.code.-360111 | The specified time is invalid. Enter another value. |
| yd.error.code.-360112 | A parsing error occurred. |
| yd.error.code.-360113 | The name of the firewall is invalid. Enter another value. |
| yd.error.code.-360114 | The specified network instance is invalid. Enter another value. |
| yd.error.code.-360115 | The specified VPC is invalid. Enter another value. |
| yd.error.code.-360116 | The specified region is invalid. Enter another value. |
| yd.error.code.-360117 | The specified destination CIDR block is invalid. Enter another value. |
| yd.error.code.-360118 | The specified VPC firewall does not exist. Enter another value. |
| yd.error.code.-360119 | The firewall is configured and cannot be repeatedly created. |
| yd.error.code.-360120 | Authorized required. You must grant permissions to the firewall. |
| yd.error.code.-360121 | The specified security group is invalid. |
| yd.error.code.-360122 | The specified security group is invalid. |
| yd.error.code.-360123 | An error occurred while calling the ECS operation. |
| yd.error.code.-360124 | An error occurred while calling the VPC operation. |
| yd.error.code.-360125 | The format of the specified CIDR block is invalid. Enter another value. |
| yd.error.code.-360126 | An error occurred while creating a vSwitch. |
| yd.error.code.-360127 | An error occurred while creating an endpoint. |
| yd.error.code.-360128 | An error occurred while deleting an endpoint. |
| yd.error.code.-360129 | Authorization required. Try again. |
| yd.error.code.-360130 | The specified ECS instance is unavailable. |
| yd.error.code.-360131 | An unknown error occurred. |

| yd.error.code.-360132 | An error occurred while searching the route table. |
|---|---|
| yd.error.code.-360133 | The ID of the firewall is invalid. |
| yd.error.code.-360134 | The status of the firewall is invalid. Try again later. |
| yd.error.code.-360135 | The specified switch of the firewall is invalid. Enter another value. |
| yd.error.code.-360136 | The specified status of the firewall is invalid. Enter another value. |
| yd.error.code.-360137 | Unknown user. Try again. |
| yd.error.code.-360138 | The specified VPC for the firewall is invalid. Enter another value. |
| yd.error.code.-360139 | The specified VPC for the firewall is invalid. Enter another value. |
| yd.error.code.-360140 | The specified firewall does not exist. Enter another value. |
| yd.error.code.-360141 | The firewall is not configured. Configure the firewall. |
| yd.error.code.-360142 | The firewall is enabled. |
| yd.error.code.-360143 | The firewall is disabled. |
| yd.error.code.-360144 | The firewall cannot be enabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360145 | The firewall cannot be disabled because the status of the firewall is invalid. Try again later. |
| yd.error.code.-360146 | The NIC of the firewall is invalid. Check the parameter. |
| yd.error.code.-360147 | The destination CIDR block is invalid. Specify another value. |
| yd.error.code.-360148 | The same CIDR block cannot be repeatedly configured. Specify another CIDR block. |
| yd.error.code.-360149 | The number of destination CIDR blocks exceeds the upper limit. Reduce the number of CIDR blocks. |
| yd.error.code.-360150 | The ID of the firewall is invalid. |
| yd.error.code.-360151 | The status of the endpoint is invalid. |
| yd.error.code.-360152 | The endpoint is invalid. |
| yd.error.code.-360153 | The endpoint is invalid. |
| yd.error.code.-360154 | A timeout error occurred while creating the endpoint. |

| yd.error.code.-360155 | A timeout error occurred while deleting the endpoint. |
|---|---|
| yd.error.code.-360156 | Permissions required. Try again. |
| yd.error.code.-360157 | The specified route table does not exist. |
| yd.error.code.-360158 | The route entry is invalid. |
| yd.error.code.-360159 | An error occurred while creating the route. |
| yd.error.code.-360160 | An error occurred while deleting the route. |
| yd.error.code.-360161 | A timeout error occurred while creating a route. |
| yd.error.code.-360162 | A timeout error occurred while deleting a route. |
| yd.error.code.-360163 | The route is invalid. |
| yd.error.code.-360164 | The task status is invalid. |
| yd.error.code.-360165 | An error occurred while enabling the firewall. Try again. |
| yd.error.code.-360166 | An error occurred while disabling the firewall. Try again. |
| yd.error.code.-360167 | The parameter is invalid. Try again. |
| yd.error.code.-360168 | The parameter is invalid. Try again. |
| yd.error.code.-360169 | The parameter is invalid. Try again. |
| yd.error.code.-360170 | The parameter is invalid. Try again. |
| yd.error.code.-360171 | The value of the Region parameter is invalid. |
| yd.error.code.-360172 | The system is busy. |
| yd.error.code.-360173 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360174 | The number of configured VPC firewalls reaches the upper limit. Increase the VPC firewall quota. |
| yd.error.code.-360175 | The parameter is invalid. Try again. |
| yd.error.code.-360176 | The parameter is invalid. Try again. |
| yd.error.code.-360177 | The parameter is invalid. Try again. |
| yd.error.code.-360178 | An unknown error occurred. |
| yd.error.code.-360179 | An error occurred while calling the operation. |
| yd.error.code.-360180 | The number of VPCs that are attached to the CEN instance is insufficient. |

| yd.error.code.-360181 | The firewall of the CEN instance is overwritten. You do not need to create a firewall. |
|---|---|
| yd.error.code.-360182 | The security group does not exist. |
| yd.error.code.-360183 | The security group cannot be deleted. |
| yd.error.code.-360184 | An unknown error occurred. |
| yd.error.code.-360185 | An error occurred while updating the firewall route. |
| yd.error.code.-360186 | You cannot configure the firewall because the status of the firewall is invalid. |
| yd.error.code.-360187 | The number of VPCs in the region is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360188 | The quota is insufficient. You cannot configure the VPC firewall. Increase the quota. |
| yd.error.code.-360189 | The ECS instance does not exist. |
| yd.error.code.-360190 | An error occurred while calling the operation. |
| yd.error.code.-360191 | The parameter is invalid. Try again. |
| yd.error.code.-360192 | The account is invalid. Enter another value. |
| yd.error.code.-360193 | The account does not have the required permissions, and Cloud Firewall is not purchased. |
| yd.error.code.-360194 | An error occurred while configuring IPS. |
| yd.error.code.-360195 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360196 | VPC firewalls can be created only in the same region. |
| yd.error.code.-360197 | A conflict occurred. |
| yd.error.code.-360198 | The destination CIDR block is not specified. The firewall cannot be created. |
| yd.error.code.-360199 | A timeout error occurred while attaching Cloud Firewall to the CEN instance. |
| yd.error.code.-360200 | A timeout error occurred while creating the vSwitch. |
| yd.error.code.-360201 | A timeout error occurred while deleting the vSwitch. |
| yd.error.code.-360202 | The specified network instance ID is invalid. |
| yd.error.code.-360203 | The specified VPC does not exist. |
| yd.error.code.-360204 | A timeout error occurred while creating a VPC. |

| yd.error.code.-360205 | A timeout error occurred while creating a VPC. |
|---|---|
| yd.error.code.-360206 | The specified ECS instance does not exist. |
| yd.error.code.-360207 | An error occurred while disabling the ECS instance. Try again. |
| yd.error.code.-360208 | An error occurred while obtaining the backup ECS instance. |
| yd.error.code.-360209 | You are not allowed to create a firewall for a HUB VPC. |
| yd.error.code.-360210 | The specified CEN instance ID is invalid. |
| yd.error.code.-360211 | The parameter is invalid. Try again. |
| yd.error.code.-360212 | The number of VPCs that are attached to the CEN instance is insufficient. The VPC firewall cannot be enabled. |
| yd.error.code.-360213 | The CEN instance does not exist. |
| yd.error.code.-360214 | The request timed out. Try again. |
| yd.error.code.-360215 | The parameter is invalid. Try again. |
| yd.error.code.-360216 | The Express Connect circuit for the data center is invalid. |
| yd.error.code.-360217 | The specified firewall mode is invalid. |
| yd.error.code.-360218 | An error occurred while calling the operation of Apsara Stack Network Operations Platform (NET). |
| yd.error.code.-360300 | A backend error occurred. |
| yd.error.code.-360301 | A backend error occurred. |
| yd.error.code.-360302 | A backend error occurred. |
| yd.error.code.-360303 | A backend error occurred. |
| yd.error.code.-360304 | A backend error occurred. |
| yd.error.code.-360305 | A backend error occurred. |
| yd.error.code.-360306 | A backend error occurred. |
| yd.error.code.-360307 | A backend error occurred. |
| yd.error.code.-360308 | An error occurred while querying the cluster ID. |
| yd.error.code.-360309 | An error occurred while updating the information about the cluster. |
| yd.error.code.-360310 | An error occurred while updating the Express Connect circuit. |

| yd.error.code.-360311 | An error occurred while inserting the VLAN. |
|---|---|
| yd.error.code.-360312 | An error occurred while querying the IP address pool. |
| yd.error.code.-360313 | An error occurred while updating the IP address pool. |
| yd.error.code.-360314 | An error occurred while updating the information about the VPC route. |
| yd.error.code.-360315 | An error occurred while updating the status of the VPC. |
| yd.error.code.-360316 | An error occurred while inserting the firewall ns. |
| yd.error.code.-360317 | An error occurred while updating the VLAN. |
| yd.error.code.-360318 | An error occurred while updating the endpoint information about the firewall. |
| yd.error.code.-360319 | An error occurred while updating the network information about the firewall. |
| yd.error.code.-360320 | An error occurred while updating the health check configurations. |
| yd.error.code.-360321 | An error occurred while updating the route table. |
| yd.error.code.-360322 | An error occurred while updating the information about the Express Connect circuit for the data center. |
| yd.error.code.-360323 | An error occurred while updating the information about the route of the data center. |
| yd.error.code.-360400 | An unknown error occurred. |
| yd.error.code.-360401 | No VLAN is available. |
| yd.error.code.-360402 | An error occurred while calling the VPC operation. |
| yd.error.code.-360403 | An error occurred while creating the virtual firewall. |
| yd.error.code.-360404 | An error occurred while creating the Express Connect circuit. |
| yd.error.code.-360405 | An error occurred while enabling the Express Connect circuit. |
| yd.error.code.-360406 | An error occurred while creating the VBR. |
| yd.error.code.-360407 | An error occurred while updating the attributes of the VBR. |
| yd.error.code.-360408 | An error occurred while querying the VBR. |
| yd.error.code.-360409 | An error occurred while creating the RI. |

| yd.error.code.-360410 | An error occurred while updating the attributes of the RI. |
|---|---|
| yd.error.code.-360411 | An error occurred while connecting the RI. |
| yd.error.code.-360412 | An error occurred while creating an Express Connect circuit for the data center. |
| yd.error.code.-360413 | An error occurred while enabling an Express Connect circuit for the data center. |
| yd.error.code.-360414 | An error occurred while querying an RI. |
| yd.error.code.-360415 | An error occurred while querying the monitored IP addresses that are used for communications between VPCs. |
| yd.error.code.-360416 | An error occurred while querying the monitored IP addresses that are used for communications between a data center and a VPC. |
| yd.error.code.-360417 | The VPC monitoring mode is abnormal. |
| yd.error.code.-360418 | The status of the instance is invalid. |
| yd.error.code.-193000 | An unknown error occurred. |
| yd.error.code.-193001 | The specified HTTP request method is invalid. |
| yd.error.code.-193002 | An error occurred while calling the operation by using HTTP. |
| yd.error.code.-193003 | Permissions required. |
| yd.error.code.-193004 | Unsupported operation. |
| yd.error.code.-193005 | Authentication failed. |
| yd.error.code.-193006 | An error occurred while accessing the database. |
| yd.error.code.-193007 | Accessed native method. |
| yd.error.code.-193101 | An error occurred while encoding JSON data. |
| yd.error.code.-193102 | An error occurred while parsing JSON data. |
| yd.error.code.-193103 | An error occurred while parsing INT data. |
| yd.error.code.-193104 | An error occurred while parsing BOOL data. |
| yd.error.code.-193105 | An error occurred while parsing the body of the HTTP request. |
| yd.error.code.-193201 | The specified parameters are insufficient. |
| yd.error.code.-193202 | The specified parameter value is invalid. |
| yd.error.code.-193203 | The specified time is invalid. |

| yd.error.code.-193204 | The parameter is invalid. |
|---|---|
| yd.error.code.-193205 | The IP address is not in the value of traffic forwarding configuration. |
| yd.error.code.-193301 | The CIDR block already exists. |
| yd.error.code.-193302 | The firewall UUID is invalid. |
| yd.error.code.-193303 | The mode of the firewall is being switched. |
| yd.error.code.-193304 | The mode of the firewall is invalid. |
| yd.error.code.-193305 | The switch of the firewall mode in unauthorized. |
| yd.error.code.-193306 | The mode of the device is being switched. |
| yd.error.code.-193307 | An error occurred during the instance health check. The instance cannot be switched to the normal mode. |
| yd.error.code.-193308 | All devices are bypassed, and the instance mode cannot be switched. |
| yd.error.code.-193309 | The working mode of the instance takes precedence over the working mode of the device. |
| yd.error.code.-193310 | The specified page number is invalid. |
| yd.error.code.-193311 | The route type is invalid. |
| yd.error.code.-193312 | An error occurred while deleting the route. |
| yd.error.code.-193313 | An error occurred while deleting the route. |
| yd.error.code.-193314 | An error occurred while creating the route. |
| yd.error.code.-193315 | An error occurred while creating the route. |
| yd.error.code.-193316 | The ID of the Cloud Firewall instance is invalid. |
| yd.error.code.-193317 | The Cloud Firewall instance must be specified. |
| yd.error.code.-200100 | The request method is invalid. |
| yd.error.code.-200101 | Authentication failed. |
| yd.error.code.-200102 | Invocation failed. |
| yd.error.code.-200103 | The parameter is invalid. Try again. |
| yd.error.code.-200104 | The specified UID is invalid.Try again. |
| yd.error.code.-200105 | An error occurred while paging. |
| yd.error.code.-200106 | The IP address in the address book is invalid. Check the parameter and enter another value. |
| yd.error.code.-200107 | The address book already exists. |

| yd.error.code.-200108 | An error occurred. Try again. |
|---|---|
| yd.error.code.-200109 | The address book is in use and cannot be deleted. |
| yd.error.code.-200110 | The specified parameter is invalid. |
| yd.error.code.-200111 | The specified parameter is invalid. |
| yd.error.code.-200112 | The specified parameter is invalid. |
| yd.error.code.-200113 | The specified parameter is invalid. |
| yd.error.code.-200114 | The specified parameter is invalid. |
| yd.error.code.-200115 | The specified parameter is invalid. |
| yd.error.code.-200116 | The specified parameter is invalid. |
| yd.error.code.-200117 | The security group rule does not exist. |
| yd.error.code.-200118 | The specified priority is invalid, or the number of rules reaches the upper limit. |
| yd.error.code.-200119 | The specified priority is invalid, or the number of rules reaches the upper limit. |
| yd.error.code.-200120 | An error occurred. Try again. |
| yd.error.code.-200121 | The domain name is invalid. Check the parameter and enter another value. |
| yd.error.code.-200122 | The number of addresses in the address book exceeds the upper limit. |
| yd.error.code.-200123 | The specified parameter is invalid. |
| yd.error.code.-200124 | The specified parameter is invalid. |
| yd.error.code.-200125 | The specified parameter is invalid. |
| yd.error.code.-200126 | The specified parameter is invalid. |
| yd.error.code.-200127 | The number of ports in the address book exceeds the upper limit. |
| yd.error.code.-200128 | The port in the address book is invalid. Check the parameter and enter another value. |
| yd.error.code.-200129 | The number of address books exceeds the upper limit. |
| yd.error.code.-200130 | The number of address books exceeds the upper limit. |
| yd.error.code.-200200 | A backend error occurred. |
| yd.error.code.-200201 | A backend error occurred. |

| yd.error.code.-200202 | A backend error occurred. |
|---|---|
| yd.error.code.-200203 | A backend error occurred. |
| yd.error.code.-200300 | A backend error occurred. |
| yd.error.code.-200301 | A backend error occurred. |
| yd.error.code.-200302 | A backend error occurred. |
| yd.error.code.-200400 | An unknown error occurred. |
| yd.error.code.-200500 | An error occurred while calling the operation. |
| yd.error.code.200 | The request is successful. |
| yd.error.code.-210100 | The request method is invalid. |
| yd.error.code.-210101 | Authentication failed. |
| yd.error.code.-210102 | Invocation failed. |
| yd.error.code.-210103 | The parameter is invalid. Try again. |
| yd.error.code.-210104 | The specified UID is invalid.Try again. |
| yd.error.code.-210105 | An error occurred while paging. Try again. |
| yd.error.code.-210106 | The parameter is invalid. Try again. |
| yd.error.code.-210107 | The parameter is invalid. Try again. |
| yd.error.code.-210108 | The parameter is invalid. Try again. |
| yd.error.code.-210109 | The parameter is invalid. Try again. |
| yd.error.code.-210110 | The parameter is invalid. Try again. |
| yd.error.code.-210111 | The parameter is invalid. Try again. |
| yd.error.code.-210200 | A backend error occurred. |
| yd.error.code.-210201 | A backend error occurred. |
| yd.error.code.-210202 | A backend error occurred. |
| yd.error.code.-210203 | A backend error occurred. |
| yd.error.code.-210300 | A backend error occurred. |
| yd.error.code.-210301 | A backend error occurred. |
| yd.error.code.-210302 | An error occurred. Try again. |
| yd.error.code.-210400 | An error occurred. Try again. |
| yd.error.code.200 | Success |

| yd.error.code.-230100 | The request method is invalid. |
|---|---|
| yd.error.code.-230101 | Authentication failed. |
| yd.error.code.-230102 | An error occurred while sending the request to the local server. |
| yd.error.code.-230103 | The operation failed authentication. |
| yd.error.code.-230104 | The parameter is invalid. |
| yd.error.code.-230105 | The policy template already exists. |
| yd.error.code.-230106 | The policy template does not exist. |
| yd.error.code.-230107 | The user ID is invalid. |
| yd.error.code.-230108 | The security group ID is invalid. |
| yd.error.code.-230109 | The security group ID is invalid. |
| yd.error.code.-230110 | The direction of the rule is invalid. |
| yd.error.code.-230111 | An IP protocol error occurred. |
| yd.error.code.-230112 | The rule policy is invalid. |
| yd.error.code.-230113 | The priority of the policy is invalid. Enter another value. |
| yd.error.code.-230114 | The port in the policy is invalid. Enter another value. |
| yd.error.code.-230115 | The CIDR block is invalid. Enter another value. |
| yd.error.code.-230116 | The description is invalid. Enter another value. |
| yd.error.code.-230117 | The policy already exists. |
| yd.error.code.-230118 | The policy does not exist. |
| yd.error.code.-230119 | The rule ID is invalid. |
| yd.error.code.-230120 | The number of policies exceeds the limit. We recommend that you delete policies that you no longer use. |
| yd.error.code.-230121 | An error occurred while paging. |
| yd.error.code.-230122 | The rule is being published. Try again. |
| yd.error.code.-230123 | The submission status is invalid. |
| yd.error.code.-230124 | The policy group is rolled back. |
| yd.error.code.-230125 | The submitted information is invalid. |
| yd.error.code.-230126 | The rule is not changed. You do not need to publish the rule. |

| yd.error.code.-230127 | The security group ID is invalid. |
|---|---|
| yd.error.code.-230128 | The IP address in the rule is invalid. |
| yd.error.code.-230129 | The network type of the rule is invalid. Select another value. |
| yd.error.code.-230130 | An error occurred while managing the rule. |
| yd.error.code.-230131 | The policy cannot be submitted. |
| yd.error.code.-230150 | The policy group does not exist. Specify another value. |
| yd.error.code.-230151 | The number of policy groups exceeds the limit. |
| yd.error.code.-230152 | The policy group cannot be modified. |
| yd.error.code.-230153 | The policy group is prestarted. |
| yd.error.code.-230154 | The rule ID is invalid. |
| yd.error.code.-230200 | A backend error occurred. |
| yd.error.code.-230300 | A backend error occurred. |
| yd.error.code.-230301 | A backend error occurred. |
| yd.error.code.-230302 | A backend error occurred. |
| yd.error.code.-230400 | An unknown error occurred. |

**Error codes specific to Network Detection and Response**

| Error code | Error message | Description |
|---|---|---|
| ErrorNeedLogin.-210204 | need login (You are not logged on.) | The error message returned because you are not logged on. Log on first. |
| ErrorAuthentication.-210101 | authentication error (An authentication error occurred.) | The error message returned because an authentication error occurred. Use a RAM role that has the required permissions. |
| ErrorParametersAliUid.-210902 | invalid AliUid (The value of the AliUid parameter is invalid.) | The error message returned because the value of the AliUid parameter is invalid. Specify a valid value. |
| ErrorParametersIpType.-210920 | invalid para ip type (The value of the ipType parameter is invalid.) | The error message returned because the value of the ipType parameter is invalid. Specify a valid value. |

| ErrorParametersSrcIP.-210919 | invalid para src ip (The value of the SrcIP parameter is invalid.) | The error message returned because the value of the SrcIP parameter is invalid. Specify a valid value. |
|---|---|---|
| ErrorParametersDstIP.-210921 | invalid para dst ip (The value of the dstIP parameter is invalid.) | The error message returned because the value of the dstIP parameter is invalid. Specify a valid value. |
| ErrorParametersPort.-210208 | invalid port, must 0~65535 (The specified port number is invalid. The port number must range from 0 to 65535.) | The error message returned because the specified port number is invalid. Specify a port number ranging from 0 to 65535. |
| ErrorParametersLiveTime.- 210922 | invalid para live time (The value of the liveTime parameter is invalid.) | The error message returned because the value of the liveTime parameter is invalid. Specify a valid value. |
| ErrorDBInsert.-210122 | internal error: sql insert (An internal error occurred while executing the INSERT statement.) | The error message returned because an internal error occurred while executing the INSERT statement. |
| ErrorInnerUuid.-210606 | internal error: uuid list is 0 (The internal error of empty UUID list occurred.) | The error message returned because the UUID list is empty. |
| ErrorDBSelect.-210124 | internal error: sql select (An internal error occurred while executing the SELECT statement.) | The error message returned because an internal error occurred while executing the SELECT statement. |
| ErrorParasAddressCidrFeild.- 210915 | paras addressCidrList filed (Failed to reset the addressCidrList rule.) | The error message returned because the system failed to reset the addressCidrList rule. |
| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
| ErrorPortAddressGroup.-210303 | get port in address group failed (Failed to obtain port information from the address group.) | The error message returned because the system failed to obtain port information from the address group. |
| ErrorSourceAddressGroup.- 210304 | get source address in address group failed (Failed to obtain source addresses from the address group.) | The error message returned because the system failed to obtain source addresses from the address group. |
| ErrorSourceAddressRange.- 210306 | source address range error, must be like \"192.168.XX.XX/192.168.XX.X X\" (The source address range is invalid. Example: \"192.168.XX.XX/192.168.XX.X X\") | The error message returned because the source address range is invalid. Specify the value in the \"192.168.XX.XX/192.168.XX.X X\" format. |

| ErrorDestAddressGroup.- 210305 | get dest address in address group failed (Failed to obtain destination addresses from the address group.) | The error message returned because the system failed to obtain destination addresses from the address group. |
|---|---|---|
| ErrorNoBeaverRules.-210226 | no beaver rules for online (The specified Network Detection and Response rule does not exist.) | The error message returned because the specified Network Detection and Response rule does not exist. |
| ErrorDBUpdate.-210121 | internal error: sql update (An internal error occurred while executing the UPDATE statement.) | The error message returned because an internal error occurred while executing the UPDATE statement. |
| ErrorDBDelete.-210123 | internal error: sql delete (An internal error occurred while executing the DELETE statement.) | The error message returned because an internal error occurred while executing the DELETE statement. |
| ErrorMarshalJSON.-210125 | internal error: marshal json (An internal error occurred while marshaling JSON data.) | The error message returned because an internal error occurred while marshaling JSON data. |
